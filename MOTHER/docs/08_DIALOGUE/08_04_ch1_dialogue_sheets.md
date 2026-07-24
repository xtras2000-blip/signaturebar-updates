# 08_04 CH1 Dialogue Sheets

CH1 대표 이벤트 3종(`ch1_ev_004` 첫 미소, `ch1_ev_010` 돌잔치, `ch1_ev_005` 산후우울 신호)의 전체 대사 시트. 이벤트 확정 JSON은 07_03 §2, 구조·condition 문법은 08_01, 문체는 08_02, CH1 아이 발화는 08_03(`vocal_tag`만 허용)을 따른다. 재생 중 HUD는 `hidden`(D-004).

## 0. 공통 표기 규칙

- **line_id**: `{scene_id}_l{번호}`. 선택 후 분기 라인은 각 이벤트에 후속 씬 `s3`를 신설해 배치한다 — 07_03 `scenes` 배열에 `s3` 추가가 필요하며 동기화 대상으로 표기해 둔다.
- **지문**: `speaker: system` 라인(13_03 §2 준용). 화면 지시문 전용, 60자 이내, 감정 직접 서술 금지.
- **condition**: 표에는 축약 표기. 실제 JSON은 08_01 스키마를 따른다. 예: `mind < 30` → `{"type":"stat","key":"mind","op":"lt","value":30}`.
  - `husband_support`는 보조 수치(D-011)로, `stat` 조건 키 어휘에 추가가 필요하다(13_03 린트 확장, 제안 상태).
  - `temperament_seed` 조건은 `{"type":"seed","value":"sensitive"}` 확장 표기를 제안한다(13_03 반영 전까지 제안 상태).
- **slot**: 같은 slot 내 첫 참 조건 line 1개만 표시. 조건 변형을 앞에, 무조건 기본 line을 마지막에 배치한다(08_01 폴백 규칙).
- **emotion**: CH1 어휘 `overwhelmed` / `wonder` / `isolation` / `neutral`(08_01).
- 선택지 `choice_id`·`effects`·`memory_tag`는 07_03 확정 JSON과 1:1 — 본 문서는 대사만 추가하며 수치를 변경하지 않는다.

---

## 1. ch1_ev_004 첫 미소 (day 45~60, wonder)

### 1.1 씬 구성 개요

| scene | location / time | 내용 |
|---|---|---|
| s1 | loc_home_living / midday | 빨래를 걷다 돌아본 순간, 아이가 처음 웃는다 |
| s2 | loc_home_living / midday | 휴대폰을 찾는 손. 웃음이 사라질까 봐 눈을 못 뗀다 → choices |
| s3 (신설) | loc_home_living / midday | 선택 직후 마무리. 선택별 `memory_tag` 조건으로 분기 |

### 1.2 씬별 라인 표

| line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|
| ch1_ev_004_s1_l1 | system | — | 건조대의 빨래를 걷다가 돌아본다. | — | neutral |
| ch1_ev_004_s1_l2 | system | — | 매트 위의 아이가 눈을 맞춘다. 입꼬리가 올라간다. | — | wonder |
| ch1_ev_004_s1_l3 | child | — | `babble_soft` | — | wonder |
| ch1_ev_004_s1_l4 | player | — | …방금, 웃은 거야? | — | wonder |
| ch1_ev_004_s1_l5 | player | A | 그래. 너는 웃는구나. | `mind < 30` (tone_exhausted) | overwhelmed |
| ch1_ev_004_s1_l6 | player | A | 다시. 한 번만 다시 웃어 봐. | — (기본) | wonder |
| ch1_ev_004_s1_l7 | system | — | 빨래가 바닥에 떨어진다. | — | neutral |
| ch1_ev_004_s2_l1 | system | — | 손이 저절로 휴대폰을 찾는다. | — | neutral |
| ch1_ev_004_s2_l2 | player | B | 아빠도 봐야 되는데. | `husband_support >= 60` | wonder |
| ch1_ev_004_s2_l3 | player | B | …이걸 나 혼자 보네. | `husband_support < 30` | isolation |
| ch1_ev_004_s2_l4 | player | B | 잠깐만, 잠깐만 있어 봐. | — (기본) | wonder |
| ch1_ev_004_s2_l5 | child | — | `babble_soft` | — | wonder |

### 1.3 선택지별 분기 대사 (s3)

| choice_id | line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|---|
| c1 마주 웃는다 | ch1_ev_004_s3_l1 | system | — | 사진은 없다. 눈에 담는 시간이 길다. | `mem_ch1_first_smile` exists | wonder |
| c1 | ch1_ev_004_s3_l2 | player | — | 엄마 여기 있어. 봤어, 다 봤어. | 〃 | wonder |
| c2 동영상부터 | ch1_ev_004_s3_l3 | system | — | 영상 속 웃음은 삼 초. 손 떨림이 그대로 담겼다. | `mem_ch1_first_smile_video` exists | wonder |
| c2 | ch1_ev_004_s3_l4 | player | — | 여보한테 보내야지. …아니, 저장부터. | 〃 | wonder |
| c3 남편에게 전화 | ch1_ev_004_s3_l5 | player | — | 여보, 애가 웃었어. 방금, 나 보고. | `mem_ch1_first_smile_call` exists | wonder |
| c3 | ch1_ev_004_s3_l6 | npc_husband | C | 진짜? 영상 있어? 나 지금 나갈게. | 〃 + `husband_support >= 60` | neutral |
| c3 | ch1_ev_004_s3_l7 | npc_husband | C | 어. 나 회의 중이야. 이따 하자. | 〃 + `husband_support < 30` | neutral |
| c3 | ch1_ev_004_s3_l8 | npc_husband | C | 웃었어? 미안, 좀 이따 전화할게. | 〃 (기본) | neutral |
| c3 | ch1_ev_004_s3_l9 | system | — | 통화가 끊긴 뒤에도 아이는 웃고 있다. | 〃 | wonder |

### 1.4 조건부 변형 주석

- **slot A (s1_l5/l6)**: tone_exhausted 변형. 지친 상태에서는 감탄 대신 짧은 확인으로 낮춘다 — 문장 길이로 상태를 보여준다(08_02 §6 CH1 톤).
- **slot B (s2_l2~l4)**: `husband_support` 변형. 같은 순간이 "같이 볼 사람"의 유무에 따라 wonder/isolation으로 갈린다.
- **slot C (s3_l6~l8)**: c3 한정 남편 응답 3분기. `husband_support` 밴드가 CH4 회수(`mem_ch1_first_smile_call`)의 온도를 예고한다.

---

## 2. ch1_ev_010 돌잔치 (day 360~370, wonder·overwhelmed)

### 2.1 씬 구성 개요

| scene | location / time | 내용 |
|---|---|---|
| s1 | loc_home_living / morning | 돌상 준비. 시어머니의 전화, 남편의 온도, 한복 입은 아이 |
| s2 | loc_home_living / afternoon | 돌잡이 상 앞. 하객·카메라·훈수 속의 아이 손 → choices |
| s3 (신설) | loc_home_living / afternoon | 선택 직후 마무리. 선택별 `memory_tag` 조건으로 분기 |

### 2.2 씬별 라인 표

| line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|
| ch1_ev_010_s1_l1 | system | — | 돌상 대여 박스, 답례품 스티커, 한복 소매의 풀기. | — | neutral |
| ch1_ev_010_s1_l2 | npc_mother_in_law | — | 대추는 홀수로 올려라. 그게 법도야. | — | neutral |
| ch1_ev_010_s1_l3 | player | A | 네, 어머니. …네. | `mind < 30` (tone_exhausted) | overwhelmed |
| ch1_ev_010_s1_l4 | player | A | 네, 어머니. 그렇게 할게요. | — (기본) | neutral |
| ch1_ev_010_s1_l5 | npc_husband | B | 상은 내가 나를게. 당신은 애 옷 입혀. | `husband_support >= 60` | neutral |
| ch1_ev_010_s1_l6 | npc_husband | B | 나 뭐 하면 돼? | `husband_support < 30` | neutral |
| ch1_ev_010_s1_l7 | npc_husband | B | 몇 시까지 가면 되지? | — (기본) | neutral |
| ch1_ev_010_s1_l8 | child | C | `cry_discomfort` (한복 소매에 몸을 비튼다) | `seed = sensitive` | overwhelmed |
| ch1_ev_010_s1_l9 | child | C | `babble_soft` | — (기본) | wonder |
| ch1_ev_010_s2_l1 | system | — | 카메라 여섯 대. 아이 손이 실과 연필 사이 허공을 젓는다. | — | overwhelmed |
| ch1_ev_010_s2_l2 | npc_cohort_yujin | — | 요즘은 청진기도 놔요. 지호는 그거 잡았는데. | — | neutral |
| ch1_ev_010_s2_l3 | npc_mother_in_law | — | 연필 잡아야지. 아가, 연필. | — | neutral |
| ch1_ev_010_s2_l4 | child | D | `cry_unknown` (낯선 얼굴들 앞에서 굳는다) | `seed = sensitive` | overwhelmed |
| ch1_ev_010_s2_l5 | child | D | `babble_call` (상 위로 몸을 던지려 한다) | `seed = active` | wonder |
| ch1_ev_010_s2_l6 | child | D | `babble_soft` | — (기본) | wonder |
| ch1_ev_010_s2_l7 | player | — | {child_name}, 천천히 해도 돼. | — | wonder |

### 2.3 선택지별 분기 대사 (s3)

| choice_id | line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|---|
| c1 기다린다 | ch1_ev_010_s3_l1 | npc_mother_in_law | — | 애 팔 아프겠다. 얼른 쥐여 줘라. | `mem_ch1_doljanchi_wait` exists | neutral |
| c1 | ch1_ev_010_s3_l2 | player | — | 조금만 더요, 어머니. | 〃 | neutral |
| c1 | ch1_ev_010_s3_l3 | system | — | 박수 소리가 잦아든다. 아이가 무언가를 잡는다. | 〃 | wonder |
| c1 | ch1_ev_010_s3_l4 | player | — | …그래. 그거였구나. | 〃 | wonder |
| c2 연필을 옮긴다 | ch1_ev_010_s3_l5 | system | — | 연필이 아이 손 닿는 곳으로 옮겨진다. 플래시가 터진다. | `mem_ch1_doljanchi_pencil` exists | neutral |
| c2 | ch1_ev_010_s3_l6 | npc_mother_in_law | — | 그래, 그래야지. 우리 강아지. | 〃 | neutral |
| c2 | ch1_ev_010_s3_l7 | player | — | … | 〃 | overwhelmed |
| c3 진행을 서두른다 | ch1_ev_010_s3_l8 | system | — | 답례품 명단, 축의금 봉투. 식은 삼십 분 만에 끝난다. | `mem_ch1_doljanchi_rush` exists | overwhelmed |
| c3 | ch1_ev_010_s3_l9 | npc_cohort_sunny | — | {child_name} 엄마, 얼굴이 반쪽이야. | 〃 | neutral |
| c3 | ch1_ev_010_s3_l10 | player | — | 끝나고 얘기해. 나 정산부터. | 〃 | overwhelmed |

### 2.4 조건부 변형 주석

- **slot A (s1_l3/l4)**: tone_exhausted 변형. 응답이 문장에서 음절로 줄어든다.
- **slot B (s1_l5~l7)**: `husband_support` 변형. 06_03 밴드 표와 정합 — "자발적 분담 / 용건 중심 / 보통"의 세 온도.
- **slot C·D (s1_l8~l9, s2_l4~l6)**: `temperament_seed` 변형. 기질은 vocal_tag와 행동 지문으로만 드러나며, 어느 기질도 문제로 묘사하지 않는다(05_01 §3).
- c2의 단독 침묵 `…`(s3_l7)은 해당 씬 1회 한도 내 사용(08_02 §3). CH5 입학식 회수(`callback_plan`)에서 이 침묵의 값이 정해진다.

---

## 3. ch1_ev_005 산후우울 신호 (conditional·mind<35, isolation)

### 3.1 민감성 처리 원칙 (01_03 §5)

- **콘텐츠 고지**: 이벤트 진입 직전 전면 고지 카드를 1회 표시한다. 문구(안): "이 장면은 산후우울을 다룹니다. 지금 보지 않으려면 다음 아침으로 넘어갈 수 있습니다." — [계속] / [다음에] 2버튼. [다음에] 선택 시 다음 `morning` 블록으로 이월(트리거 조건 유지).
- **정답 없음**: 세 선택 모두 대사가 평가·훈계하지 않는다. 도움을 청하지 않는 c3도 서사적으로 낙인찍지 않는다 — 차이는 CH4 회수(`callback_plan`)의 결로만 남는다.
- 07_03 QA 메모 준수: 진입~종료까지 HUD 완전 숨김, `mind` 값 직·간접 언급 금지, 감정 직접 서술 0건.

### 3.2 씬 구성 개요

| scene | location / time | 내용 |
|---|---|---|
| s1 | loc_home_bedroom / morning | 몸이 이불 밖으로 나가지지 않는 아침. 옆방의 울음 |
| s2 | loc_home_bedroom / morning | 부재중 없음. 사흘 만의 어른 목소리를 찾아 → choices |
| s3 (신설) | loc_home_bedroom / morning | 선택 직후 마무리. 선택별 `memory_tag` 조건으로 분기 |

### 3.3 씬별 라인 표

| line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|
| ch1_ev_005_s1_l1 | system | — | 커튼 틈으로 해가 든다. 몸이 이불 밖으로 나가지지 않는다. | — | isolation |
| ch1_ev_005_s1_l2 | child | — | `cry_unknown` (옆방에서) | — | overwhelmed |
| ch1_ev_005_s1_l3 | player | A | 열까지. …다시 열까지. | `mind < 30` (tone_exhausted) | isolation |
| ch1_ev_005_s1_l4 | player | A | …열까지만 세고 일어나자. | — (기본) | isolation |
| ch1_ev_005_s1_l5 | system | — | 숫자는 열에서 다시 하나로 돌아온다. | — | isolation |
| ch1_ev_005_s2_l1 | system | — | 부재중 없음. 마지막 통화는 사흘 전 택배였다. | — | isolation |
| ch1_ev_005_s2_l2 | system | B | 남편 자리는 새벽에 이미 비어 있었다. | `husband_support < 30` | isolation |
| ch1_ev_005_s2_l3 | npc_husband | B | (메시지) 오늘 일찍 갈게. 뭐 먹고 싶어? | `husband_support >= 60` | neutral |
| ch1_ev_005_s2_l4 | system | B | 휴대폰 화면이 어두워질 때까지 들고 있는다. | — (기본) | isolation |
| ch1_ev_005_s2_l5 | player | — | …아무한테나, 아무 말이나. | — | isolation |

### 3.4 선택지별 분기 대사 (s3)

| choice_id | line_id | speaker | slot | text_kr / vocal_tag | condition | emotion |
|---|---|---|---|---|---|---|
| c1 친정엄마에게 전화 | ch1_ev_005_s3_l1 | player | — | 엄마. …그냥 걸었어. | `mem_ch1_dark_morning_call` exists | isolation |
| c1 | ch1_ev_005_s3_l2 | npc_grandma | — | 밥은 먹었나. 목소리가 와 그렇노. | 〃 | neutral |
| c1 | ch1_ev_005_s3_l3 | player | — | 먹었어. 김에 밥 싸서. | 〃 | neutral |
| c1 | ch1_ev_005_s3_l4 | system | — | 별일 아닌 얘기가 한 시간을 간다. 커튼이 걷혀 있다. | 〃 | neutral |
| c2 검진 예약까지 | ch1_ev_005_s3_l5 | system | — | 검색창. 산후 자가검진. 예약 버튼 위에서 손이 멈춘다. | `mem_ch1_dark_morning_screening` exists | isolation |
| c2 | ch1_ev_005_s3_l6 | player | — | …가 보기나 하자. 아니면 말고. | 〃 | isolation |
| c2 | ch1_ev_005_s3_l7 | system | — | 예약 확인 문자가 온다. 옆방에서 아이가 뒤척인다. | 〃 | neutral |
| c3 괜찮다고 쓰고 지운다 | ch1_ev_005_s3_l8 | system | — | 맘카페 글쓰기 화면. 세 줄을 쓰고, 지운다. | `mem_ch1_dark_morning_alone` exists | isolation |
| c3 | ch1_ev_005_s3_l9 | player | — | 다들 이러고 사는 거겠지. | 〃 | isolation |
| c3 | ch1_ev_005_s3_l10 | child | — | `cry_hunger` | 〃 | neutral |
| c3 | ch1_ev_005_s3_l11 | player | — | 가. 엄마 가. | 〃 | isolation |
| c3 | ch1_ev_005_s3_l12 | system | — | 이불을 걷는다. 방문이 열린다. | 〃 | neutral |

### 3.5 조건부 변형 주석

- **slot A (s1_l3/l4)**: tone_exhausted 변형. 트리거(mind<35)보다 깊은 밴드(mind<30)에서 일어나자는 다짐마저 무너진 반복문이 된다.
- **slot B (s2_l2~l4)**: `husband_support` 변형. 빈자리/메시지/무응답 — 고립의 밀도가 남편 축으로 달라진다. 어느 쪽도 대사로 원망을 명시하지 않는다.
- 모든 분기가 행동(커튼, 문자, 방문)으로 끝난다 — 교훈적 마무리 금지(08_02 §7) 및 c3 비낙인 원칙의 구현.

---

## 4. 검수 메모 (15_QA 연동)

| 항목 | 확인 |
|---|---|
| CH1 child line | `text_kr` 0건, 전량 `vocal_tag`(08_03 §2 사전 내: cry_unknown, cry_discomfort, cry_hunger, babble_soft, babble_call) |
| babble_call 사용 | `ch1_ev_010`(12개월)에서만 사용 — 08_03 "10개월~" 제한 준수 |
| 길이·침묵 | 전 `text_kr` ≤ 40자·≤ 2문장. 단독 `…`는 ev_010 s3 1회. 연속 line `…` 없음 |
| 폴백 | 슬롯 A~D 전부 무조건 기본 line 포함, 변형 line을 배열 앞쪽 배치(08_01) |
| 동기화 필요 | ① 각 이벤트 `scenes`에 s3 추가(07_03) ② `husband_support` stat 키·`seed` 조건 타입(13_03 린트 어휘) — 제안 상태 |
