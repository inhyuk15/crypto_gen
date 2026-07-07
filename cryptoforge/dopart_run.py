#!/usr/bin/env python3
"""D — 최소 SUPERCOP do-part 채점기 (독립 재현).

do-part(991줄, 전체 스윕)에서 '한 (operation, primitive, impl)을 빌드→try 실행→checksum 대조'
하는 핵심 체인만 떼어 재현한다. 목적:
  1) LLM 생성 impl을 SUPERCOP 규약대로 채점(pass/fail)
  2) 그 전에 ref 소스로 알려진 checksum을 재현하는지 검증(채점기 자체의 정확성)

사용:  python3 dopart_run.py <crypto_op> <primitive> <impl_dir> [--keep]
예:    python3 dopart_run.py crypto_hash sha256 supercop-20260330/crypto_hash/sha256/ref
       checksum 기대값은 supercop-.../<op>/<primitive>/checksum{small,big} 에서 읽음.

핵심 규약(do-part에서 확인):
  - 네임스페이스: -D'CRYPTO_NAMESPACE(name)=<opi>_##name' (opi = <op>_<primitive>)
  - 생성 헤더 2종: <op>.h, <opi>.h  (api.h의 CRYPTO_* 를 sed로 <opi>_ 네임스페이스)
  - try-small = '#define SMALL' + try.c ; 첫 출력필드 = checksum
  - crypto_hash 등 비키드 op: trylibs = cpucycles + kernelrandombytes
    키드 op(kem/sign/encrypt/dh/box/scalarmult): + knownrandombytes(결정적 난수)
"""
import os, sys, re, subprocess, tempfile, shutil, glob

# repo 루트(= cryptoforge의 부모)의 supercop 트리. 환경변수로 재정의 가능.
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.environ.get('CRYPTOFORGE_SUPERCOP', os.path.join(_ROOT, 'supercop-20260330'))
KEYED = {'crypto_kem','crypto_sign','crypto_encrypt','crypto_dh','crypto_box','crypto_scalarmult'}

def sh(cmd, cwd=None, env=None):
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True)

def gen_op_h(o, op):
    """<op>.h (generic→namespaced 매크로 매핑). do-part의 sed/grep 파이프 재현."""
    macros = sh(['grep','-E', f'{o}$|{o}\\(|{o}_', os.path.join(BASE,'MACROS')]).stdout
    lines = [f'#ifndef {o}_H', f'#define {o}_H', '', f'#include "{op}.h"', '']
    for m in macros.splitlines():
        mop = m.replace(o, op, 1)              # sed s/$o/$op/ (first occ)
        d = f'#define {mop} {mop}'.replace(op, o, 1)  # | sed s/$op/$o/ (first occ)
        lines.append(d)
    lines += [f'#define {o}_PRIMITIVE "{PRIM}"',
              f'#define {o}_IMPLEMENTATION {op}_IMPLEMENTATION',
              f'#define {o}_VERSION {op}_VERSION', '', '#endif']
    return '\n'.join(lines) + '\n'

def gen_opp_h(o, op, opi, opp, api_text, impldir):
    """<opi>.h / <opi>_publicinputs.h. api.h의 CRYPTO_* 를 opi_ 로 네임스페이스."""
    api_ns = sh(['sed', r's/[ \t]CRYPTO_/ '+opi+r'_/g'],).stdout  # placeholder; replaced below
    # sed는 stdin 필요 → 직접 치환
    api_ns = re.sub(r'(?<=[ \t])CRYPTO_', opi+'_', api_text)
    protos = sh(['grep','-E', f'{o}$|{o}\\(|{o}_', os.path.join(BASE,'PROTOTYPES.c')]).stdout
    protos = protos.replace(o, opi)            # sed s/$o/$opi/
    macros = sh(['grep','-E', f'{o}$|{o}\\(|{o}_', os.path.join(BASE,'MACROS')]).stdout
    lines = [f'#ifndef {opp}_H', f'#define {opp}_H', '', api_ns, ' ',
             '#ifdef __cplusplus', 'extern "C" {', '#endif', protos.rstrip('\n'),
             '#ifdef __cplusplus', '}', '#endif', '']
    for m in macros.splitlines():
        mopi = m.replace(o, opi, 1)
        d = f'#define {mopi} {mopi}'.replace(opi, opp, 1)
        lines.append(d)
    lines += [f'#define {opp}_IMPLEMENTATION "{impldir}"',
              f'#ifndef {opi}_VERSION', f'#define {opi}_VERSION "-"', '#endif',
              f'#define {opp}_VERSION {opi}_VERSION', '', '#endif']
    return '\n'.join(lines) + '\n'

def build_support(work, cc):
    """cpucycles(스텁) + kernelrandombytes + optblockers 오브젝트 생성."""
    inc = ['-I', os.path.join(BASE,'include'), '-I', os.path.join(BASE,'cryptoint'),
           '-I', os.path.join(BASE,'cpucycles')]
    objs = []
    # cpucycles 스텁 (checksum은 사이클과 무관)
    stub = os.path.join(work, 'cpucycles_stub.c')
    open(stub,'w').write(
        '#include "cpucycles.h"\n'
        'static long long z(void){return 0;}\n'
        'long long (*cpucycles)(void)=z;\n'
        'long long cpucycles_persecond(void){return 1000000000LL;}\n'
        'const char *cpucycles_implementation(void){return "stub";}\n'
        'const char *cpucycles_version(void){return "stub";}\n'
        'void cpucycles_tracesetup(void){}\n')
    # kernelrandombytes (urandom)
    krb = os.path.join(BASE,'kernelrandombytes','urandom.c')
    # optblockers
    obs = [f for f in glob.glob(os.path.join(BASE,'cryptoint','*_optblocker.c'))
           if not re.search(r'/u?intN_optblocker\.c$', f)]  # intN/uintN은 템플릿
    for src in [stub, krb] + obs:
        o = os.path.join(work, os.path.basename(src)+'.o')
        r = sh([*cc, '-DSUPERCOP', *inc, '-c', src, '-o', o])
        if r.returncode != 0:
            return None, f'support build fail {os.path.basename(src)}:\n{r.stderr[:800]}'
        objs.append(o)
    return objs, None

def run(op, prim, impldir, keep=False):
    global PRIM
    PRIM = prim
    # 네임스페이스 3층 (do-part 규약):
    #   o      = crypto_aead                         (generic, try.c가 사용)
    #   opf    = crypto_aead_ascon128v12             (primitive, = ${o}_${p}, 헤더 파일명)
    #   opi    = crypto_aead_ascon128v12_ref_...     (impl, api.h 상수/함수의 실제 네임스페이스)
    o = op; opf = f'{op}_{prim}'
    rel = os.path.relpath(os.path.abspath(impldir), BASE)
    security = 'constbranchindex'
    opi = re.sub(r'[./-]', '_', f'{rel}/{security}')
    opp_list = [opf, f'{opf}_publicinputs']
    impldir = os.path.abspath(impldir)
    algodir = os.path.join(BASE, op, prim)
    exp_small = _read(os.path.join(algodir,'checksumsmall'))
    exp_big   = _read(os.path.join(algodir,'checksumbig'))
    cc = ['gcc','-O2','-fPIC']

    work = tempfile.mkdtemp(prefix='dopart_')
    try:
        # 1) impl 소스 + api.h 복사
        srcs = []
        for f in glob.glob(impldir+'/*'):
            if f.endswith(('.c','.h','.cc','.cpp','.C','.inc','.S','.s')):
                shutil.copy(f, work)
        api_path = os.path.join(impldir,'api.h')
        api_text = open(api_path).read() if os.path.isfile(api_path) else ''
        # 2) 하네스 파일 복사
        for f in ['try.c','measure.c']:
            shutil.copy(os.path.join(BASE, op, f), work)
        for f in ['try-anything.c','measure-anything.c','MACROS','PROTOTYPES.c']:
            shutil.copy(os.path.join(BASE, f), work)
        open(os.path.join(work,'try-small.c'),'w').write('#define SMALL\n#include "try.c"\n')
        open(os.path.join(work,'test-more.inc'),'w').close()
        open(os.path.join(work,'test-loops.inc'),'w').close()
        # 3) 네임스페이스 헤더 생성
        open(os.path.join(work, f'{o}.h'),'w').write(gen_op_h(o, opf))
        for opp in opp_list:
            open(os.path.join(work, f'{opp}.h'),'w').write(
                gen_opp_h(o, opf, opi, opp, api_text, impldir))
        # 4) 지원 오브젝트
        sup, err = build_support(work, cc)
        if sup is None: return _res('SUPPORT_FAIL', err)
        # 5) impl 컴파일 (네임스페이스 매크로)
        nsdef = [f'-DCRYPTO_NAMESPACE(name)={opi}_##name',
                 f'-D_CRYPTO_NAMESPACE(name)=_{opi}_##name',
                 f'-DCRYPTO_SHARED_NAMESPACE(name)={opi}_##name',
                 f'-D_CRYPTO_SHARED_NAMESPACE(name)=_{opi}_##name',
                 f'-DCRYPTO_NAMESPACETOP={opi}',
                 f'-D_CRYPTO_NAMESPACETOP=_{opi}',
                 '-DCRYPTO_ALIGN(n)=__attribute__((aligned(n)))']
        inc = ['-I', work, '-I', os.path.join(BASE,'include'),
               '-I', os.path.join(BASE,'cryptoint'), '-I', os.path.join(BASE,'cpucycles')]
        impl_c = [f for f in glob.glob(work+'/*.c')
                  if os.path.basename(f) not in
                  ('try.c','try-small.c','measure.c','try-anything.c','measure-anything.c',
                   'cpucycles_stub.c')]
        objs = []
        for c in impl_c:
            ob = c+'.o'
            r = sh([*cc,'-DSUPERCOP',*nsdef,*inc,'-c',c,'-o',ob])
            if r.returncode != 0:
                return _res('IMPL_COMPILE_FAIL', f'{os.path.basename(c)}:\n{r.stderr[:1200]}')
            objs.append(ob)
        lib = os.path.join(work, f'lib{opi}.a')
        sh(['ar','cr',lib,*objs]); sh(['ranlib',lib])
        # 6) trylibs
        trylibs = list(sup)
        if op in KEYED:
            kob = os.path.join(work,'knownrandombytes.o')
            r = sh([*cc,'-DSUPERCOP',*inc,'-c',os.path.join(BASE,'knownrandombytes','knownrandombytes.c'),'-o',kob])
            if r.returncode != 0: return _res('SUPPORT_FAIL', 'knownrandombytes:\n'+r.stderr[:800])
            trylibs = [kob]+trylibs
        # 7) try-small / try 링크 + 실행
        out = {}
        for name, exp in (('try-small',exp_small),('try',exp_big)):
            exe = os.path.join(work,name)
            r = sh([*cc,'-DSUPERCOP',*inc,'-o',exe,
                    os.path.join(work,name+'.c'),os.path.join(work,'try-anything.c'),
                    lib,*trylibs,'-lm'])
            if r.returncode != 0:
                return _res('LINK_FAIL', f'{name}:\n{r.stderr[:1200]}')
            rr = sh([exe, VERSION, 'x86', impldir, 'gcc'])
            if rr.returncode != 0:
                return _res('RUN_FAIL', f'{name} rc={rr.returncode}\n{rr.stdout[:400]}\n{rr.stderr[:800]}')
            cks = rr.stdout.split()[0] if rr.stdout.split() else ''
            out[name] = (cks, exp, cks == exp if exp else None)
        verdict = 'PASS' if all(out[n][2] for n in out) else 'CHECKSUM_MISMATCH'
        return _res(verdict, None, out)
    finally:
        if keep: print('workdir kept:', work)
        else: shutil.rmtree(work, ignore_errors=True)

VERSION = open(os.path.join(BASE,'version')).read().strip()
def _read(p): return open(p).read().strip() if os.path.isfile(p) else ''
def _res(verdict, err=None, out=None):
    return {'verdict':verdict, 'error':err, 'checksums':out}

if __name__ == '__main__':
    keep = '--keep' in sys.argv
    a = [x for x in sys.argv[1:] if x != '--keep']
    op, prim, impldir = a[0], a[1], a[2]
    res = run(op, prim, impldir, keep=keep)
    print('VERDICT:', res['verdict'])
    if res['checksums']:
        for n,(got,exp,ok) in res['checksums'].items():
            print(f'  {n:9} got={got[:24]}... exp={exp[:24]}... {"OK" if ok else "MISMATCH" if exp else "no-expected"}')
    if res['error']:
        print('--- error ---'); print(res['error'])
