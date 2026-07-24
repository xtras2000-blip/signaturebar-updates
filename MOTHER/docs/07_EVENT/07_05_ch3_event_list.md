# 07_05 CH3 Event List

CH3(3~5세) 이벤트 카탈로그. 시스템 규칙은 07_01, 작성 규칙은 07_02를 따른다.
CH3 감정 목표: 서툰 자부심(`pride`), 걱정(`worry`), 비교 불안(`comparison`) — 01_04.
게임 내 일차(day)는 연속: CH3는 day 1096~1825 (만 3~5세). 기관 장소는 06_02 등록 ID인 `loc_daycare`를 사용한다(하단 QA 메모 참조).

## 1. 이벤트 카탈로그

| event_id | 제목 | class | 트리거 (유형 · 조건 요약) | emotion_tags | 대표 memory_tag | 회수 챕터 |
|---|---|---|---|---|---|---|
| `ch3_ev_001` | 원 발표회 | major | scheduled · day 1400~1420 | pride, worry | `mem_ch3_recital_stage` | CH5 (입학식 운동장, 무대의 노래 흥얼거림) |
| `ch3_ev_002` | 또래 비교 — 맘카페와 놀이터 서열 | major | conditional · memory `mem_ch1_momcafe_compare` AND time_block=night | comparison, worry | `mem_ch3_compare_night` | CH4 (npc_cohort_yujin의 힘듦 고백에서 회수) |
| `ch3_ev_003` | 한글 조기교육 고민 | major | conditional · day 1300~1500 | worry, comparison | `mem_ch3_hangul_decision` | CH5 (입학 서류에 제 이름 쓰는 손) |
| `ch3_ev_004` | 친구 다툼과 사과 | major | conditional · day 1200~1500 · npc_peer_doyun 장난감 다툼 (관계 수치 미보유 — memory로만 기록) | worry, pride | `mem_ch3_first_quarrel` | CH4 (도윤이 절교 소동의 전사) |
| `ch3_ev_005` | 편식 전쟁 | minor | conditional · child_condition<60 | worry | `mem_ch3_picky_eating` | CH5 (학교 급식 적응 걱정으로 회수) |
| `ch3_ev_006` | 아이의 첫 거짓말 | major | conditional · day 1400~1700 | worry, pride | `mem_ch3_first_lie` | CH4 (아이의 비밀 이벤트의 전사) |
| `ch3_ev_007` | 수족구 격리 일주일 | major | conditional · child_condition<50 AND day 1150~1600 | worry | `mem_ch3_hfmd_quarantine` | CH5 (입학 전 마지막 검진, 익숙해진 병원) |
| `ch3_ev_008` | 시댁 훈육 갈등 | major | scheduled · holiday=chuseok | worry | `mem_ch3_inlaw_discipline` | CH4 ("네 방식대로 잘 키웠다" 또는 침묵 — 06_03 아크) |
| `ch3_ev_009` | 둘째 질문 | minor | random · weight 15 | worry, comparison | `mem_ch3_second_child_question` | CH5 (입학식 날 가족 구도의 완결감) |
| `ch3_ev_050` | 재취업 준비 | major | scheduled · CH3 시작 +30일 · `preset_fulltime` 전용(04_01 정본 예약 id) | worry, comparison | `mem_ch3_reemployment_search` | CH5 (입학 후의 나 — 경력 재시작 결정) |
| `ch3_ev_010` | 독감 접종의 계절 | minor | scheduled · season=winter, day 1350~1380 | worry | `mem_ch3_flu_shot` | CH5 (입학 전 예방접종 증명서 발급으로 회수) |
| `ch3_ev_011` | 키즈카페 생일파티 초대 | minor | random · weight 15 | comparison, pride | `mem_ch3_birthday_party` | CH4 (초대 명단에서 빠진 날의 전사) |
| `ch3_ev_012` | 학부모 상담 주간 | minor | scheduled · day 1250~1280 | pride, worry | `mem_ch3_parent_meeting` | CH4 (교사의 관찰 기록이 갈등 장면의 근거로 회수) |
| `ch3_ev_013` | 아빠 참여수업 | minor | scheduled · day 1500~1530 | pride | `mem_ch3_dad_class_day` | CH4 (화해 장면의 자산 — 남편의 성장 증거) |

- CH1 memory_tag 회수 이벤트 (3종, 07_03 "회수 챕터" 열과 교차 검증):
  `ch3_ev_002`(`mem_ch1_momcafe_compare` — 비교 불안의 재점화), `ch3_ev_007`(`mem_ch1_first_fever` — 첫 열 감기 대비 의연해진 두 번째 밤),
  `ch3_ev_010`(`mem_ch1_first_vaccine` — 접종에 익숙해진 대기실 대비). 보조 회수: `ch3_ev_005`가 `mem_ch1_first_babyfood`(첫 이유식)를 대사에서 재참조.
- CH2 회수: `ch3_ev_007`은 `mem_ch2_febrile_seizure`(열경련의 밤)도 함께 회수한다 (07_04 교차 검증).
- `once`는 전 이벤트 true, 단 `ch3_ev_005`(편식 전쟁)·`ch3_ev_009`(둘째 질문)는 `once:false, cooldown_days:14`.
- `ch3_ev_050`은 04_01 5절이 정본 소유한 `preset_fulltime` 전용 예약 id를 카탈로그에 등재한 것 — 번호 체계(001~)와 별도 유지.

## 2. 대표 이벤트 전체 JSON

### 2.1 ch3_ev_001 원 발표회

```json
{
  "event_id": "ch3_ev_001", "chapter": 3, "title_kr": "원 발표회", "event_class": "major",
  "emotion_tags": ["pride", "worry"], "priority": 95, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [{ "type": "day_range", "min": 1400, "max": 1420 }] },
  "scenes": [
    { "scene_id": "ch3_ev_001_s1", "location_id": "loc_home_living", "time_block": "morning",
      "script_kr": ["다림질한 무대 의상, 머리핀 두 개, 손수건.", "아이는 어젯밤 이불 속에서도 노래를 연습했다. 2절에서 자꾸 같은 데를 틀리면서."] },
    { "scene_id": "ch3_ev_001_s2", "location_id": "loc_daycare", "time_block": "afternoon",
      "script_kr": ["강당 앞줄은 삼각대의 숲. 막이 오르고, 아이가 무대 가운데에서 3초간 얼어 있다.", "객석을 훑던 눈이 한 자리에 멈춘다."] }
  ],
  "choices": [
    { "choice_id": "ch3_ev_001_c1", "text_kr": "맨 앞줄에서 크게 손을 흔든다",
      "effects": { "expressiveness": 2, "mind": 2, "stamina": -2 },
      "memory_tag": "mem_ch3_recital_stage_wave" },
    { "choice_id": "ch3_ev_001_c2", "text_kr": "소리 내지 않고 눈만 맞추며 고개를 끄덕인다",
      "effects": { "confidence": 2, "attachment": 2, "expressiveness": -1 },
      "memory_tag": "mem_ch3_recital_stage" },
    { "choice_id": "ch3_ev_001_c3", "text_kr": "화면 너머로 본다 — 가족 단톡방 실시간 중계",
      "effects": { "rel_npc_husband": 3, "rel_npc_mother_in_law": 3, "attachment": -2 },
      "memory_tag": "mem_ch3_recital_stage_camera" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch3_recital_stage",
      "usage_kr": "CH5 입학식 운동장에서 아이가 발표회 노래를 흥얼거리는 장면으로 회수 — 얼었던 3초가 끝난 자리" }
  ]
}
```

### 2.2 ch3_ev_002 또래 비교 — 맘카페와 놀이터 서열

```json
{
  "event_id": "ch3_ev_002", "chapter": 3, "title_kr": "또래 비교", "event_class": "major",
  "emotion_tags": ["comparison", "worry"], "priority": 85, "once": true, "cooldown_days": 0,
  "trigger": { "type": "conditional", "conditions": [
    { "type": "memory", "memory_tag": "mem_ch1_momcafe_compare", "exists": true },
    { "type": "day_range", "min": 1150, "max": 1400 },
    { "type": "time_block", "value": "night" } ] },
  "scenes": [
    { "scene_id": "ch3_ev_002_s1", "location_id": "loc_playground", "time_block": "afternoon",
      "script_kr": ["미끄럼틀 앞. 하율이는 보조바퀴 뗀 자전거를 타고, 도윤이는 제 이름 석 자를 모래에 쓴다.", "벤치의 대화가 자연스럽게 원아 수업 얘기로 넘어간다. '그 집은 벌써 시작했대.'"] },
    { "scene_id": "ch3_ev_002_s2", "location_id": "loc_momcafe", "time_block": "night",
      "script_kr": ["검색창에 반쯤 쓰다 만 문장. '5세 한글'.", "스크롤이 빨라진다. 댓글 마흔세 개. 몇 년 전 그 밤과 같은 엄지의 움직임."] }
  ],
  "choices": [
    { "choice_id": "ch3_ev_002_c1", "text_kr": "휴대폰을 덮고 잠든 아이의 얼굴을 보러 간다",
      "effects": { "mind": 2, "attachment": 2, "stamina": -3 },
      "memory_tag": "mem_ch3_compare_night_close" },
    { "choice_id": "ch3_ev_002_c2", "text_kr": "유진에게 메시지를 보낸다 — '그 학습지 어디 거야?'",
      "effects": { "rel_npc_cohort_yujin": 4, "mind": -3, "money": -45000 },
      "memory_tag": "mem_ch3_compare_night_ask" },
    { "choice_id": "ch3_ev_002_c3", "text_kr": "발달 검사 예약 페이지를 저장해 둔다",
      "effects": { "mind": -2, "money": -50000, "stamina": -1 },
      "memory_tag": "mem_ch3_compare_night_screening" }
  ],
  "callback_plan": [
    { "chapter": 4, "memory_tag": "mem_ch3_compare_night",
      "usage_kr": "CH4에서 npc_cohort_yujin이 제 힘듦을 고백하는 장면의 전제로 회수 — 비교의 진원지가 입체화된다 (06_03 아크)" }
  ]
}
```

## 3. QA 메모 (15_QA 연동)

- 카탈로그 14종의 `emotion_tags`는 전부 CH3 태그 집합 `{pride, worry, comparison}`의 부분집합 (D-005, 빌드 검증 포함).
- 유치원 전용 장소가 06_02에 미등록이므로 기관 장면은 등록 ID `loc_daycare`(연결 이벤트 풀에 "재롱잔치" 포함)를 사용했다. 유치원 분리가 결정되면 06_02에 `loc_kindergarten` 등록 후 일괄 교체한다 (미등록 식별자 금지 — 07_02 금지 패턴 6).
- `ch3_ev_002`의 memory_tag는 회수 분기가 필요해 접미어(`_close`/`_ask`/`_screening`)로 구분하며, callback_plan의 `mem_ch3_compare_night`는 공통 접두 회수를 뜻한다 (07_02 6절).
- `ch3_ev_004`·`ch3_ev_011`의 npc_peer_doyun·npc_peer_hayul은 관계 수치 미보유(06_03) — `effects`에 `rel_*` 사용 금지, memory_log로만 흔적을 남긴다.
- `ch3_ev_008`의 `holiday:chuseok`, `ch3_ev_010`의 `season:winter`는 06_01 계절·명절 식별자를 참조한다.
- `ch3_ev_002`의 학습지 구독료(-45,000원/월)·발달 검사비는 12_DATABASE 물가 상수 확정 시 상수 참조로 교체한다.
- CH1 회수 3종 + CH2 회수 1종의 대본·트리거는 07_03/07_04 각 `callback_plan`과 1:1 교차 검증 완료 (07_02 2절).
