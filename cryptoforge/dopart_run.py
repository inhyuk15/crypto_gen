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

def sh(cmd, cwd=None, env=None, timeout=None):
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True,
                          timeout=timeout)

# try '1회 실행'의 상한(초). 모델 impl 이 무한루프/미종료면 여기서 끊는다(SUPERCOP killafter 대응).
# 정상 impl 은 초 단위로 끝나므로 이 상한은 오직 망가진(무한루프) impl 에만 걸린다.
RUN_TIMEOUT = int(os.environ.get('CRYPTOFORGE_RUN_TIMEOUT', '300'))

def gen_op_h(o, op, prim):
    """<op>.h (generic→namespaced 매크로 매핑). do-part의 sed/grep 파이프 재현."""
    macros = sh(['grep','-E', f'{o}$|{o}\\(|{o}_', os.path.join(BASE,'MACROS')]).stdout
    lines = [f'#ifndef {o}_H', f'#define {o}_H', '', f'#include "{op}.h"', '']
    for m in macros.splitlines():
        mop = m.replace(o, op, 1)              # sed s/$o/$op/ (first occ)
        d = f'#define {mop} {mop}'.replace(op, o, 1)  # | sed s/$op/$o/ (first occ)
        lines.append(d)
    lines += [f'#define {o}_PRIMITIVE "{prim}"',
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

# 키드 op의 결정적 randombytes 스택: knownrandombytes → crypto_rng(chacha20) →
# crypto_stream(chacha20). 상수는 chacha20 고정(알고리즘 무관).
_RNG_SHIMS = {
'crypto_stream.h':
    '#ifndef crypto_stream_h\n#define crypto_stream_h\n'
    '#define crypto_stream crypto_stream_chacha20\n'
    '#define crypto_stream_xor crypto_stream_chacha20_xor\n'
    '#define crypto_stream_KEYBYTES 32\n#define crypto_stream_NONCEBYTES 8\n#endif\n',
'crypto_stream_chacha20.h':
    '#ifndef crypto_stream_chacha20_h\n#define crypto_stream_chacha20_h\n'
    '#define crypto_stream_chacha20_KEYBYTES 32\n#define crypto_stream_chacha20_NONCEBYTES 8\n'
    'extern int crypto_stream_chacha20(unsigned char *,unsigned long long,'
    'const unsigned char *,const unsigned char *);\n'
    'extern int crypto_stream_chacha20_xor(unsigned char *,const unsigned char *,'
    'unsigned long long,const unsigned char *,const unsigned char *);\n#endif\n',
'crypto_rng.h':
    '#ifndef crypto_rng_h\n#define crypto_rng_h\n'
    'extern int crypto_rng_chacha20(unsigned char *,unsigned char *,const unsigned char *);\n'
    '#define crypto_rng crypto_rng_chacha20\n'
    '#define crypto_rng_KEYBYTES 32\n#define crypto_rng_OUTPUTBYTES 736\n#endif\n',
'try.h':
    '#ifndef try_h\n#define try_h\n'
    'extern void randombytes_callback(const unsigned char *,unsigned long long);\n#endif\n',
}

def _build_known_randombytes(work, cc, inc):
    """결정적 randombytes.o 스택 빌드 → [obj...] 또는 (None, err).
    shim 헤더가 impl 컴파일에 새지 않도록 work/_rng/ 에 격리."""
    sw = os.path.join(work, '_rng'); os.makedirs(sw, exist_ok=True)
    for name, txt in _RNG_SHIMS.items():
        open(os.path.join(sw, name), 'w').write(txt)
    stream = os.path.join(BASE, 'crypto_stream', 'chacha20', 'e', 'ref')
    rng = os.path.join(BASE, 'crypto_rng', 'chacha20', 'ref')
    krb = os.path.join(BASE, 'knownrandombytes', 'knownrandombytes.c')
    swi = ['-I', sw]
    ns = '-DCRYPTO_NAMESPACE(name)=crypto_stream_chacha20_##name'
    jobs = [  # (src, 추가 include, 추가 def)
        (os.path.join(stream, 'api.c'),    ['-I', stream], [ns]),
        (os.path.join(stream, 'chacha.c'), ['-I', stream], [ns]),
        (os.path.join(rng, 'rng.c'),       ['-I', rng],    []),
        (krb,                              ['-I', os.path.join(BASE,'knownrandombytes')], []),
    ]
    objs = []
    for src, extra, defs in jobs:
        o = os.path.join(sw, os.path.basename(src) + '.o')
        r = sh([*cc, '-DSUPERCOP', *defs, *inc, *swi, *extra, '-c', src, '-o', o])
        if r.returncode != 0:
            return None, f'knownrandombytes stack fail {os.path.basename(src)}:\n{r.stderr[:800]}'
        objs.append(o)
    return objs, None


def build_support(work, cc, keyed):
    """cpucycles(스텁) + optblockers + randombytes 오브젝트.
    비키드: kernelrandombytes(urandom). 키드: 결정적 knownrandombytes 스택."""
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
    # optblockers + kernelrandombytes(urandom): 하네스 엔트로피 심볼. 항상 필요.
    # (urandom 은 kernelrandombytes 만 정의 — impl 이 쓰는 randombytes 와 다른 심볼)
    obs = [f for f in glob.glob(os.path.join(BASE,'cryptoint','*_optblocker.c'))
           if not re.search(r'/u?intN_optblocker\.c$', f)]  # intN/uintN은 템플릿
    urandom = os.path.join(BASE,'kernelrandombytes','urandom.c')
    for src in [stub, urandom] + obs:
        o = os.path.join(work, os.path.basename(src)+'.o')
        r = sh([*cc, '-DSUPERCOP', *inc, '-c', src, '-o', o])
        if r.returncode != 0:
            return None, f'support build fail {os.path.basename(src)}:\n{r.stderr[:800]}'
        objs.append(o)
    # 키드 op: impl 이 소비할 결정적 randombytes(=knownrandombytes chacha20 스택) 추가
    if keyed:
        robjs, err = _build_known_randombytes(work, cc, inc)
        if robjs is None:
            return None, err
        objs += robjs
    return objs, None

def run(op, prim, impldir, keep=False):
    # (전역 상태 없음 → 스레드 병렬 안전)
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
        open(os.path.join(work, f'{o}.h'),'w').write(gen_op_h(o, opf, prim))
        for opp in opp_list:
            open(os.path.join(work, f'{opp}.h'),'w').write(
                gen_opp_h(o, opf, opi, opp, api_text, impldir))
        # 4) 지원 오브젝트 (키드 op = 결정적 randombytes 스택)
        keyed = op in KEYED
        sup, err = build_support(work, cc, keyed)
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
        # 6) trylibs (randombytes 는 build_support 가 이미 sup 에 포함)
        trylibs = list(sup)
        # 7) try-small / try 링크 + 실행
        out = {}
        for name, exp in (('try-small',exp_small),('try',exp_big)):
            exe = os.path.join(work,name)
            r = sh([*cc,'-DSUPERCOP',*inc,'-o',exe,
                    os.path.join(work,name+'.c'),os.path.join(work,'try-anything.c'),
                    lib,*trylibs,'-lm'])
            if r.returncode != 0:
                return _res('LINK_FAIL', f'{name}:\n{r.stderr[:1200]}')
            try:
                rr = sh([exe, VERSION, 'x86', impldir, 'gcc'], timeout=RUN_TIMEOUT)
            except subprocess.TimeoutExpired:
                return _res('RUN_TIMEOUT',
                            f'{name}: impl 이 {RUN_TIMEOUT}s 내 미종료(무한루프/과다연산 추정)')
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
