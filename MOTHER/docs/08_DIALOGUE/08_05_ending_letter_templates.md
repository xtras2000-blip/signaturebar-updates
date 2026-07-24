# 08_05 Ending Letter Templates

## Purpose

입학식 엔딩(`ending_entrance_day`, 02_04)의 마지막 장면 `ending_letter`에서 출력되는
"아이가 그린 그림 + 한 줄 편지"의 `letter_line` 템플릿 12종 본문을 확정한다.
성격 축 4종(D-008) × 구간 3단계(low/mid/high) = 12종이며, 소유권은 08_DIALOGUE에 있다.
편지는 만 7세 아이가 스케치북에 직접 쓴 것이다 — 어휘·맞춤법은 08_03, 절제 원칙은 08_02를 따른다.

## 1. 선정 규칙 (02_04 인용)

02_04의 축 선정 알고리즘을 그대로 따른다. 본 문서는 문구만 소유하고 선정 로직을 재정의하지 않는다.

1. **대표 축 1개 선택**: `dominant_axis` = 성격 축 4종 중 최종값 최대 축.
   동률 시 `confidence → empathy → independence → expressiveness` 우선(02_04 Variables).
2. **구간 판정**: `personality_band` = 해당 축의 `low`(0~39) / `mid`(40~69) / `high`(70~100). 엔딩 구간 경계는 02_04가 정본이다.
3. **템플릿 결정**: `letter_line_id` = `letter_{dominant_axis}_{band}`.
4. **노출 수량**: 12종 중 실제 노출은 **1회 플레이당 1종**이다. 나머지 11종은 해당 회차에서 절대 등장하지 않는다(재플레이 유인, Pillar 4).
5. 알고리즘은 결정적이다 — 동일 세이브 2회 클리어 시 동일 템플릿(02_04 QA ED-05).

> 정합성 메모: 02_04 JSON 절의 `letter_{dominant_axis}_{attachment_band}` 표기는 Variables 표의
> `letter_{axis}_{band}`(성격 밴드)와 충돌한다. 본 문서는 Variables 표를 기준으로 하며, 02_04 JSON 절은 수정 대상으로 기록한다.
> `attachment_band`는 편지 자체가 아니라 편지 장면의 **연출 온도**(엄마의 리액션 지문)에만 쓴다.

## 2. 문구 작성 규칙

| 규칙 | 내용 | 근거 |
|---|---|---|
| 길이 | 한 줄 15자 내외(공백 포함). 서툰 손글씨 폰트 전제 | 02_04 UI |
| 맞춤법 | 문장당 오류 1개 이하 — 과하면 희화화 | 08_03 §4 준용 |
| 감정 명명 금지 | "슬퍼/좋아/보고 싶어" 금지. 구체적 사물·기억·부탁으로만 | 08_02 §1, 01_04 §3 |
| low ≠ 결핍 | low 구간에 슬픔·모자람 연출 금지. 낮음은 다른 모습일 뿐 | 01_04 §3, D-002 |
| 그림 낙서 | 각 템플릿의 `doodle_kr`는 글줄 옆 여백의 작은 낙서 묘사다. 엔딩 메인 그림(`drawing_id`)은 02_04의 emotion_tags 규칙으로 별도 결정된다 | 02_04 JSON |
| 어휘 | 또래 어휘("젤") 소량 허용, 시대 불일치 유행어 금지 | 08_03 §5 |

## 3. 템플릿 12종

### 3.1 confidence (자신감)

| letter_id | letter_text_kr | doodle_kr | 연출 주석 |
|---|---|---|---|
| `letter_confidence_low` | 학교 앞까지 가치 가자 | 교문 앞에 나란히 선 큰 신발과 작은 신발 | 글씨가 뒤로 갈수록 조금 작아진다. 부탁이 아니라 내일의 약속처럼 |
| `letter_confidence_mid` | 교문에서 손 흔드러 줘 | 창문 안에서 밖을 내다보는 얼굴과 흔드는 손 | "흔드러"를 한 번 지웠다 다시 쓴 흔적을 남긴다 |
| `letter_confidence_high` | 내일은 내가 먼저 갈께 | 앞서 달리는 아이, 가방끈이 뒤로 날린다 | 글씨가 크고 줄을 벗어난다. 마지막 획이 길게 삐친다 |

### 3.2 empathy (공감)

| letter_id | letter_text_kr | doodle_kr | 연출 주석 |
|---|---|---|---|
| `letter_empathy_low` | 학교 미끄럼틀이 젤 커 | 사람보다 두 배 큰 미끄럼틀, 구석에 작은 아이 하나 | 사물이 사람보다 크게 그려진다. 관찰자의 시선, 쓸쓸함 연출 금지 |
| `letter_empathy_mid` | 짝꿍 이름 아라 올게 | 나란히 붙은 책상 두 개, 의자 하나는 비어 있다 | 빈 의자 위에 물음표 하나가 연하게 그려져 있다 |
| `letter_empathy_high` | 친구 울면 손 자바줄게 | 손을 잡은 두 아이, 한 명의 볼에 물방울 하나 | 잡은 손 부분만 색이 진하다. 여러 번 덧칠한 흔적 |

### 3.3 independence (자립심)

| letter_id | letter_text_kr | doodle_kr | 연출 주석 |
|---|---|---|---|
| `letter_independence_low` | 신발 끈은 엄마가 무꺼 줘 | 커다란 나비 리본 매듭 하나가 종이 가운데 | 리본은 정성껏 그려져 있다. 못 하는 일이 아니라 엄마 몫으로 남겨 둔 일 |
| `letter_independence_mid` | 가방은 인재 내가 멜게 | 제 몸보다 큰 가방을 멘 아이의 뒷모습 | 가방이 아이보다 크지만 어깨끈은 두 줄 다 채워져 있다 |
| `letter_independence_high` | 준비물 내가 다 챙겨써 | 줄 맞춰 그린 연필·지우개·실내화 주머니 | 물건마다 서툰 이름표 글씨. 목록을 세듯 그린 정돈된 낙서 |

### 3.4 expressiveness (표현력)

| letter_id | letter_text_kr | doodle_kr | 연출 주석 |
|---|---|---|---|
| `letter_expressiveness_low` | 이거 엄마야 | 종이의 대부분을 차지한 큰 사람과 작은 사람, 화살표 하나 | 글은 여섯 자뿐, 화살표가 큰 사람을 가리킨다. 그림이 말을 대신한다 |
| `letter_expressiveness_mid` | 학교 다녀오게씀니다 | 배꼽 인사하는 아이와 마주 선 엄마 | 또박또박 눌러 쓴 획. 배운 문장을 그대로 옮긴 성실함 |
| `letter_expressiveness_high` | 오늘 이야기 백 개 해줄게 | 아이 입에서 나온 말풍선이 종이 끝까지 이어진다 | 말풍선 속은 아직 비어 있다. 백 개는 이따 채워질 예정 |

- `letter_text_kr`는 전량 15자 내외·감정 단어 0건·문장당 맞춤법 오류 1개 이하를 만족한다(§2).
- 02_04 JSON 예시의 `letter_text_kr`("엄마, 나 이제 진짜 학교 다녀…")는 본 문서 확정 문구로 교체 대상.

## 4. memory_log 연동 가변 조각 4종

편지 본문 아래에 덧붙는 **반 줄**(추신 낙서). 몽타주로 선정된 기억 8건(`picked_memories`, 02_04)에
해당 `memory_tag`(07_03 실물 태그)가 포함될 때만 붙는다. 복수 충족 시 아래 표 순서로 **최대 1개**만 노출(결정적).

| frag_id | 조건 memory_tag | 덧붙는 반 줄 | 비고 |
|---|---|---|---|
| `letter_frag_doljanchi` | `mem_ch1_doljanchi_wait` / `_pencil` / `_rush` 계열 | 돌잔치 사진 또 보자 | 07_03 ch1_ev_010. CH5 회수 계획(입학식=두 번째 돌잔치)과 연동 |
| `letter_frag_smile_video` | `mem_ch1_first_smile_video` | 아기 때 동영상 또 틀어 줘 | 07_03 ch1_ev_004 c2. 아이가 집에서 본 적 있는 그 영상 |
| `letter_frag_cohort` | `mem_ch1_cohort_meetup` | 내일도 친구랑 가치 갈래 | 07_03 ch1_ev_014. 조리원 동기 자녀와 같은 학교 재회(회수 챕터 CH5) |
| `letter_frag_grandma` | `mem_ch1_grandma_visit` | 할머니도 오라 그래 줘 | 07_03 ch1_ev_007. 역전된 돌봄(CH5 회수)의 아이 시점 |

- 반 줄은 본문보다 작은 글씨로, 본문 표기 완료 후 0.8초 뒤에 나타난다(추신을 뒤늦게 쓴 아이의 시간).
- 조건 판정은 memory_log 전체가 아니라 **선정 8건** 기준이다 — 몽타주에서 본 기억만 편지에서 되돌아온다(Pillar 4).

## 5. JSON

```json
{
  "letter_line_id": "letter_independence_mid",
  "letter_text_kr": "가방은 인재 내가 멜게",
  "doodle_kr": "제 몸보다 큰 가방을 멘 아이의 뒷모습",
  "fragment": {
    "frag_id": "letter_frag_doljanchi",
    "condition": {"type": "picked_memory_tag", "prefix": "mem_ch1_doljanchi_"},
    "text_kr": "돌잔치 사진 또 보자"
  }
}
```

## 6. QA 체크리스트 (15_QA 연동)

| 항목 | 통과 기준 |
|---|---|
| 조합 커버리지 | 4축 × 3구간 = 12종 전부 존재, `letter_{axis}_{band}` 명명 일치 |
| 노출 수량 | 1회 클리어당 편지 1종 + 조각 최대 1개, 동일 세이브 재클리어 시 동일 출력(ED-05) |
| 길이·표기 | 본문 15자 내외, 맞춤법 오류 문장당 ≤1, `…`·느낌표 규칙은 08_02 준수 |
| 감정 명명 | 본문·조각·주석에 감정 형용사 직접 서술 0건(01_04 §3) |
| low 구간 톤 | low 3종에 결핍·슬픔 연출 0건 — 배드엔딩 표기 없음(D-002) |
| 조각 태그 | 4종 조건 태그가 07_03 카탈로그에 실존, 선정 8건 기준 판정 |
