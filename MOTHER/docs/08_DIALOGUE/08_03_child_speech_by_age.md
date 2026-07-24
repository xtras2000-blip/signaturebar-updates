# 08_03 Child Speech by Age

가이드 문서. `speaker: "child"` line의 챕터(연령)별 발화 형태·표기 규칙을 정의한다. 실제 언어 발달 단계를 근거로 하되(Pillar 2), 목적은 의학적 정확성이 아니라 "우리 애도 저랬지"라는 재인이다. 데이터 구조는 08_01, 문체 일반 규칙은 08_02를 따른다.

## 1. 연령별 발달 요약

| 챕터 | 연령 | 발화 형태 | 데이터화 방식 | 핵심 감정(01_04) |
|---|---|---|---|---|
| CH1 | 0~12개월 | 울음·옹알이 | `vocal_tag`만 사용, `text_kr` 금지 | overwhelmed, wonder, isolation |
| CH2 | 1~3세 | 한 단어 → 두 단어 조합 | `text_kr` 2어절 이내 | joy, burnout, reward |
| CH3 | 3~5세 | 완전한 문장 + 문법 오류 | `text_kr` 1문장, 오류 재현 | pride, worry, comparison |
| CH4 | 5~6세 | 또래 어휘, 속마음 숨기기 시작 | `text_kr` + `subtext_kr` | guilt, reconciliation |
| CH5 | 6~7세 | 유창한 문장, 의도적 거리 | `text_kr` + `subtext_kr` | letting_go, fulfillment, loss |

## 2. CH1 — 울음·옹알이 (`vocal_tag` 사전)

텍스트로 "(운다)"라고 쓰지 않는다. 의미 태그로만 데이터화하고, 실제 전달은 사운드(11_SOUND)와 애니메이션(10_ART)이 담당한다. 플레이어는 태그를 볼 수 없고 맥락으로 추측해야 한다 — CH1 압도됨(overwhelmed)의 핵심 장치.

| `vocal_tag` | 의미 | 연출 힌트 |
|---|---|---|
| `cry_hunger` | 배고픔 | 규칙적 리듬, 입 오물거림 |
| `cry_sleepy` | 졸림 | 늘어지는 톤, 눈 비빔 |
| `cry_discomfort` | 기저귀·더움 등 불편 | 짧게 끊어지는 울음, 몸 비틀기 |
| `cry_pain` | 통증 (병원 이벤트 연동, 03_01) | 높고 날카로운 톤 |
| `cry_unknown` | 원인 불명 | 위 패턴의 랜덤 혼합. CH1 초반 가중치 최대 |
| `babble_soft` | 만족 옹알이 | wonder 장면 전용 |
| `babble_call` | 엄마를 향한 옹알이 (10개월~) | `attachment ≥ 70`(secure)에서 빈도 증가 |

- 표기 규칙: CH1 child line은 `vocal_tag` 필수, `text_kr` 정의 시 린트 리젝(08_01 DL-07 준용).

## 3. CH2 — 한 단어에서 두 단어로

| 규칙 | 내용 | 예시 |
|---|---|---|
| 어절 수 | 1~2어절. 조사 전면 생략 | "엄마 물", "이거 또" |
| 발음 표기 | 허용 사전(`child_lexicon`) 내 단순화 표기만 | "시러"(싫어), "마니"(많이), "암마"(엄마, 1세 전반) |
| 시기 구분 | 1세: 한 단어 / 2세: 두 단어 조합 진입 | "물" → "엄마 물" |
| 금지 | 완전한 조사·복문. 성인 어휘 | ~~"엄마 물 주세요"~~ |

- `child_lexicon`은 12_DATABASE 상수 테이블로 관리하며, 사전 외 임의 발음 표기는 린트 리젝.

## 4. CH3 — 완전한 문장과 문법 오류의 재현

문법 오류는 귀여움 연출이 아니라 발달의 사실적 재현이다(Pillar 2). **문장당 오류 1개 이하** — 과도하면 희화화가 된다.

| 오류 유형 | 규칙 | 예시 |
|---|---|---|
| 어순 도치 | 목적어를 문미로 후치 | "내가 했어 그거" |
| 과잉일반화 | 부정어 위치 오류 | "안 밥 먹어" |
| 조사 혼용 | 소유·주격 혼동 | "이거 내가 꺼야" |
| 존댓말 혼입 | 어린이집에서 배운 존댓말이 섞임 | "엄마, 이거 하세요 빨리" |

- CH3 후반(5세 접근)에는 오류 빈도를 낮춰 성장의 변주를 만든다(01_04 §2 "일상의 변주").

## 5. CH4~CH5 — 또래 어휘와 속마음 숨기기

| 규칙 | 내용 |
|---|---|
| 또래 어휘 | 어린이집·학교 준비 맥락의 유행어 소량 허용("젤 좋아", "짱"). 15_QA 어휘 검수 대상 |
| 속마음 분리 | 겉말은 `text_kr`, 숨긴 속마음은 `subtext_kr`에 기록. **화면에 표시하지 않는다** |
| 속마음의 전달 | `subtext_kr`는 행동 애니메이션·후속 이벤트 트리거의 근거로만 소비 (감정 전달 1순위 수단으로 회수) |
| 예시 | `text_kr: "안 갈래. 그냥."` / `subtext_kr: "엄마가 바빠 보여서 말 안 함"` |
| 회수 | `subtext_kr`가 있는 line은 관련 `memory_tag`와 짝지어 CH5·엔딩에서 회수한다(Pillar 4) |

## 6. `expressiveness`가 말수에 미치는 영향

성격 축 `expressiveness`(0~100, init 50, D-008)는 child line의 **밀도**를 바꾼다. 08_01의 `condition`(`type: "trait"`)으로 구현하며, 내용이 아니라 양과 형태가 변한다.

| 구간 | `speech_density` | 규칙 |
|---|---|---|
| `expressiveness < 30` | `low` | scene당 child line 수 −1 (최소 1 유지). 단답·침묵 변형 우선. CH4~5에서 `subtext_kr` 부착 line 비율 증가 |
| 30 ≤ … < 70 | `mid` | 기본 line 구성 그대로 |
| `expressiveness ≥ 70` | `high` | 추가 line 후보 활성(조건부 line). CH2 옹알이·CH3 재잘거림 빈도 증가, 묻지 않은 것도 말함 |

- 밀도 변형도 폴백 규칙(08_01)을 따른다: `low`/`high` 전용 line은 반드시 `mid` 기본 line과 같은 `line_slot`에 배치한다.

## 7. JSON 예시 (챕터별 child line)

```json
[
  {"line_id": "ch1_ev_003_s1_l1", "speaker": "child", "vocal_tag": "cry_unknown", "emotion": "overwhelmed"},
  {"line_id": "ch2_ev_011_s1_l2", "speaker": "child", "text_kr": "엄마 물", "emotion": "joy"},
  {"line_id": "ch3_ev_007_s2_l3", "speaker": "child", "text_kr": "내가 했어 그거", "emotion": "pride"},
  {"line_id": "ch4_ev_009_s1_l4", "speaker": "child", "text_kr": "안 갈래. 그냥.",
   "subtext_kr": "엄마가 바빠 보여서 말 안 함", "emotion": "guilt",
   "condition": [{"type": "trait", "key": "expressiveness", "op": "lt", "value": 30}]}
]
```

## 8. 검수 체크리스트 (15_QA 연동)

| 항목 | 통과 기준 |
|---|---|
| CH1 | child line에 `text_kr` 0건, `vocal_tag` 100% |
| CH2 | child `text_kr` ≤ 2어절, `child_lexicon` 외 발음 표기 0건 |
| CH3 | 문장당 문법 오류 ≤ 1, 오류 유형이 §4 표 내일 것 |
| CH4~5 | `subtext_kr` 화면 출력 0건, 백로그 미표시(08_01) |
| 공통 | 챕터와 발화 형태 불일치 0건 (예: CH2에 복문) |
