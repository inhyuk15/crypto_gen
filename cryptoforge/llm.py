#!/usr/bin/env python3
"""LLM 클라이언트 — OpenAI 호환. provider 교체는 config.resolve()가 처리.

complete(system, user) 하나로 통일. 재시도/토큰로깅 포함.
gpt-5.4mini(지금) → gemini/claude(OpenAI호환 엔드포인트)/qwen(vLLM) 로 base_url만 바뀜.
"""
import time
from openai import OpenAI
import config


class LLM:
    def __init__(self, model=None):
        r = config.resolve(model)
        self.model = r['model']
        self.provider = r['provider']
        kw = {'api_key': r['api_key']}
        if r['base_url']:
            kw['base_url'] = r['base_url']
        self.client = OpenAI(**kw)
        self.total_in = 0
        self.total_out = 0

    def complete(self, system, user, temperature=None, max_tokens=None):
        """1회 completion. 반환: (text, usage_dict)."""
        temperature = config.TEMPERATURE if temperature is None else temperature
        max_tokens = max_tokens or config.MAX_OUTPUT_TOKENS
        msgs = []
        if system:
            msgs.append({'role': 'system', 'content': system})
        msgs.append({'role': 'user', 'content': user})

        last = None
        for attempt in range(config.MAX_RETRIES):
            try:
                resp = self.client.chat.completions.create(
                    model=self.model, messages=msgs,
                    temperature=temperature, max_tokens=max_tokens,
                    timeout=config.REQUEST_TIMEOUT,
                )
                txt = resp.choices[0].message.content or ''
                u = getattr(resp, 'usage', None)
                usage = {'in': getattr(u, 'prompt_tokens', 0),
                         'out': getattr(u, 'completion_tokens', 0)}
                self.total_in += usage['in']; self.total_out += usage['out']
                return txt, usage
            except Exception as e:
                last = e
                msg = str(e)
                # 파라미터 비호환(신형 모델: temperature/max_tokens 명칭 차이) 1회 자동보정
                if 'max_tokens' in msg and 'max_completion_tokens' in msg:
                    return self._retry_completion_tokens(msgs, max_tokens)
                if 'temperature' in msg and 'unsupported' in msg.lower():
                    temperature = 1
                    continue
                # 비재시도성: 쿼터/모델없음/인증 → 즉시 실패
                if any(s in msg for s in ('insufficient_quota', 'model_not_found',
                                          'invalid_api_key', 'Incorrect API key', '401')):
                    break
                time.sleep(2 * (attempt + 1))
        raise RuntimeError(f'LLM 호출 실패({self.model}): {last}')

    def _retry_completion_tokens(self, msgs, max_tokens):
        resp = self.client.chat.completions.create(
            model=self.model, messages=msgs,
            max_completion_tokens=max_tokens, timeout=config.REQUEST_TIMEOUT,
        )
        txt = resp.choices[0].message.content or ''
        u = getattr(resp, 'usage', None)
        usage = {'in': getattr(u, 'prompt_tokens', 0), 'out': getattr(u, 'completion_tokens', 0)}
        self.total_in += usage['in']; self.total_out += usage['out']
        return txt, usage


if __name__ == '__main__':
    # 스모크 테스트: 키/모델 동작 확인
    llm = LLM()
    print(f'model={llm.model} provider={llm.provider}')
    txt, usage = llm.complete('You are a terse assistant.',
                              'Reply with exactly: OK', temperature=0, max_tokens=20)
    print('reply:', repr(txt))
    print('usage:', usage)
