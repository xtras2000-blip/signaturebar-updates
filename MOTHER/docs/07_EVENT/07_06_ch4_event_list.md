# 07_06 CH4 Event List

CH4(5~6세) 이벤트 카탈로그. 시스템 규칙은 07_01, 작성 규칙은 07_02를 따른다.
CH4 감정 목표: 미안함 — 죄책감(`guilt`), 화해(`reconciliation`) — 01_04.
CH4는 회수 챕터다: CH1~CH3에서 심은 `memory_tag`를 `trigger.conditions`의 memory 조건으로 되살리는 이벤트를 6종 포함한다 (2절 매트릭스).

## 1. 이벤트 카탈로그

| event_id | 제목 | class | 트리거 (유형 · 조건 요약) | emotion_tags | 대표 memory_tag | 회수 챕터 |
|---|---|---|---|---|---|---|
| `ch4_ev_001` | 크게 혼낸 날 | major | scheduled · day 1860~1875 | guilt | `mem_ch4_big_scolding` | CH4 (`ch4_ev_002` 화해 체인), CH5 (입학 전날 밤 회상) |
| `ch4_ev_002` | 화해 | major | conditional · has `mem_ch4_big_scolding` | reconciliation | `mem_ch4_reconcile_drawing` | CH5 (입학 전날 밤 — 화해 그림을 책가방에 넣는 장면) |
| `ch4_ev_003` | 아이의 비밀 | major | conditional · has `mem_ch3_first_quarrel` AND time_block=afternoon | guilt | `mem_ch4_child_secret` | CH5 (마지막 등원 — 신발장 앞 같은 침묵의 대비) |
| `ch4_ev_004` | 학원 보낼까 고민 | minor | conditional · has `mem_ch3_compare_night` AND time_block=night | guilt | `mem_ch4_academy_debate` | CH5 (입학 준비물 구매 — "필요한 것"의 기준 재등장) |
| `ch4_ev_005` | 동생 있는 친구 부러워하기 | minor | random · weight 15 | guilt | `mem_ch4_sibling_envy` | CH5 (입학 전날 밤 — "나 혼자여도 좋아" 라인 분기) |
| `ch4_ev_006` | 엄마의 옛 꿈 발견 | minor | random · weight 10 | reconciliation | `mem_ch4_old_dream` | CH5 (엔딩 편지 — 아이 그림 속 "엄마의 것" 소재, 02_04) |
| `ch4_ev_007` | 부부 갈등 목격 | major | conditional · rel_npc_husband<40 AND has `mem_ch1_husband_fight` | guilt | `mem_ch4_fight_witnessed` | CH4 (`ch4_ev_008` 위로 체인), CH5 (입학식 나란히 선 두 사람) |
| `ch4_ev_008` | 아이가 엄마를 위로한 날 | major | conditional · mind<40 | reconciliation, guilt | `mem_ch4_child_comfort` | CH5 (엔딩 몽타주 상위 후보, 02_04) |
| `ch4_ev_009` | 조부모 건강 이상 신호 | major | scheduled · day 2100~2130 | guilt | `mem_ch4_grandma_sign` | CH5 (`ch5_ev_011` 역전된 돌봄) |
| `ch4_ev_010` | 남편의 뒤늦은 사과 | minor | conditional · has `mem_ch1_dark_morning_alone` AND rel_npc_husband>=55 | reconciliation | `mem_ch4_late_apology` | CH5 (입학식 — 최상위 대사 분기 해금 재료, 06_03 4절) |
| `ch4_ev_011` | 빈 식탁의 재등장 | minor | conditional · has `mem_ch1_alone_evening` AND time_block=evening | guilt | `mem_ch4_empty_table` | CH5 (입학 전날 밤 — 세 사람이 모인 식탁과의 대비) |
| `ch4_ev_012` | 유진의 고백 | minor | random · weight 15 | reconciliation | `mem_ch4_yujin_confession` | CH5 (입학 준비물 — 유진이 보낸 준비물 목록 문자 회수) |
| `ch4_ev_013` | 시어머니의 인정 | minor | conditional · has `mem_ch3_inlaw_discipline` AND holiday=chuseok | reconciliation | `mem_ch4_inlaw_acknowledge` | CH5 (입학식 — 가족석 구도, 06_03 아크 완결) |

- 회수 챕터 열은 각 이벤트 JSON `callback_plan`과 1:1로 교차 검증한다 (07_02 2절).
- `once`는 전 이벤트 true. major 6종의 발생 창·조건은 겹치지 않게 설계했고, 겹칠 경우 07_01 선정 규칙으로 해소.
- `ch4_ev_010`의 rel 조건: 사과는 관계가 회복된 뒤에만 온다 — 냉랭·서먹 밴드(06_03 4절)에서는 영구 미발생일 수 있으며 의도된 설계다 (D-002, 실패 아님).
- 교차 챕터 태그는 07_04/07_05 카탈로그의 실제 `memory_tag`와 대조 완료(2026-07-24, Doc QA).

## 2. 이전 챕터 memory_tag 회수 매트릭스

| 회수 이벤트 | 조건으로 요구하는 태그 | 원천 | 회수 방식 |
|---|---|---|---|
| `ch4_ev_002` 화해 | (라인 조건) `mem_ch1_first_smile` 계열 | 07_03 `ch1_ev_004` | 앨범/동영상 장면 라인 분기 — 트리거 조건 아님 (선택별 접미 태그가 갈리므로 발생을 막지 않는다) |
| `ch4_ev_003` 아이의 비밀 | `mem_ch3_first_quarrel` | CH3 친구 갈등 | 도윤과의 다툼 전력이 "말 안 하는 이유"가 된다 |
| `ch4_ev_004` 학원 고민 | `mem_ch3_compare_night` | CH3 비교 불안 | 맘카페 비교 불안이 사교육 고민으로 재점화 |
| `ch4_ev_007` 부부 갈등 목격 | `mem_ch1_husband_fight` | 07_03 `ch1_ev_006` | CH1과 같은 문장이 다시 나오고, 이번엔 아이가 듣는다 |
| `ch4_ev_010` 남편의 뒤늦은 사과 | `mem_ch1_dark_morning_alone` | 07_03 `ch1_ev_005` | 혼자 삼켰던 그 아침을 남편이 처음 언급한다 |
| `ch4_ev_011` 빈 식탁의 재등장 | `mem_ch1_alone_evening` | 07_03 `ch1_ev_016` | 그때의 식탁 구도를 이번엔 아이의 눈으로 본다 |
| `ch4_ev_013` 시어머니의 인정 | `mem_ch3_inlaw_discipline` | CH3 시댁 훈육 갈등(추석) | "네 방식대로 잘 키웠다" 또는 침묵 (06_03 아크) |

## 3. 대표 이벤트 전체 JSON

### 3.1 ch4_ev_001 크게 혼낸 날

```json
{
  "event_id": "ch4_ev_001", "chapter": 4, "title_kr": "크게 혼낸 날", "event_class": "major",
  "emotion_tags": ["guilt"], "priority": 95, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [{ "type": "day_range", "min": 1860, "max": 1875 }] },
  "scenes": [
    { "scene_id": "ch4_ev_001_s1", "location_id": "loc_home_living", "time_block": "evening",
      "script_kr": ["물감이 소파를 지나 벽지까지 갔다. 하지 말라고 한 말이 세 번째였다.",
        "목소리가 커진다. 생각했던 것보다 훨씬 크게, 생각보다 훨씬 길게.",
        "아이의 어깨가 움츠러든다. 물감 묻은 손이 등 뒤로 숨는다."] },
    { "scene_id": "ch4_ev_001_s2", "location_id": "loc_home_child_room", "time_block": "night",
      "script_kr": ["반쯤 열린 문틈. 아이가 이불을 머리끝까지 덮고 있다.",
        "벽지의 물감 자국은 지워졌다. 아까의 목소리는 집 안 어딘가에 그대로 남아 있다."] }
  ],
  "choices": [
    { "choice_id": "ch4_ev_001_c1", "text_kr": "지금 방에 들어가 이불째 끌어안는다",
      "effects": { "attachment": 4, "stamina": -2, "mind": -2 }, "memory_tag": "mem_ch4_big_scolding" },
    { "choice_id": "ch4_ev_001_c2", "text_kr": "문 앞에서 돌아선다 — 내일 아침에 말하자",
      "effects": { "mind": -4, "stamina": 2 }, "memory_tag": "mem_ch4_big_scolding" },
    { "choice_id": "ch4_ev_001_c3", "text_kr": "남편을 먼저 들여보내고 물감 값을 검색한다",
      "effects": { "rel_npc_husband": 3, "attachment": -2, "money": -30000 }, "memory_tag": "mem_ch4_big_scolding" }
  ],
  "callback_plan": [
    { "chapter": 4, "memory_tag": "mem_ch4_big_scolding",
      "usage_kr": "CH4 화해(ch4_ev_002)의 트리거 조건이자, 그날 밤 어떻게 했는지(choice_id)에 따라 화해 도입 라인이 갈린다 (같은 챕터 회수는 보조 — 07_02 2절)" },
    { "chapter": 5, "memory_tag": "mem_ch4_big_scolding",
      "usage_kr": "CH5 입학 전날 밤(ch5_ev_last), 짐을 싸다 멈춘 손 위로 그날 밤 문틈 구도를 1컷 회상으로 회수" }
  ]
}
```

- 세 선택이 같은 `mem_ch4_big_scolding`을 공유한다 — 회수 분기는 memory_log의 `choice_id`로 수행한다 (07_02 6절 공유 규칙).

### 3.2 ch4_ev_002 화해

```json
{
  "event_id": "ch4_ev_002", "chapter": 4, "title_kr": "화해", "event_class": "major",
  "emotion_tags": ["reconciliation"], "priority": 90, "once": true, "cooldown_days": 0,
  "trigger": { "type": "conditional", "conditions": [
    { "type": "memory", "memory_tag": "mem_ch4_big_scolding", "exists": true },
    { "type": "time_block", "value": "midday" } ] },
  "scenes": [
    { "scene_id": "ch4_ev_002_s1", "location_id": "loc_home_living", "time_block": "midday",
      "script_kr": ["아이가 스케치북을 들고 온다. 두 사람이 손을 잡은 그림이다.",
        "\"이건 엄마 화났을 때 얼굴. 이건 지금 얼굴.\"", "두 얼굴 사이의 거리는 크레파스 한 뼘이다."] },
    { "scene_id": "ch4_ev_002_s2", "location_id": "loc_home_living", "time_block": "midday",
      "script_kr": ["남편이 책장에서 앨범을 꺼내 온다. 갓난아기가 처음 웃던 날의 페이지가 펼쳐진다.",
        "아이가 사진 속 자신을 들여다본다. \"이게 나야?\""] }
  ],
  "choices": [
    { "choice_id": "ch4_ev_002_c1", "text_kr": "그날 왜 화가 났는지, 아이의 말로 끝까지 설명한다",
      "effects": { "attachment": 5, "expressiveness": 2, "stamina": -3 }, "memory_tag": "mem_ch4_reconcile_words" },
    { "choice_id": "ch4_ev_002_c2", "text_kr": "말 대신 그림 옆에 엄마의 그림을 그려 넣는다",
      "effects": { "attachment": 4, "empathy": 2, "stamina": -2, "mind": -1 }, "memory_tag": "mem_ch4_reconcile_drawing" },
    { "choice_id": "ch4_ev_002_c3", "text_kr": "사과 대신 아이가 제일 좋아하는 저녁상을 차린다",
      "effects": { "attachment": 2, "child_condition": 2, "stamina": -4, "money": -25000 }, "memory_tag": "mem_ch4_reconcile_meal" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch4_reconcile_drawing",
      "usage_kr": "CH5 입학 전날 밤(ch5_ev_last), 아이가 새 책가방 앞주머니에 화해 그림을 접어 넣는 장면으로 회수" }
  ]
}
```

- s2의 앨범 장면은 `mem_ch1_first_smile` 계열(`_video`/`_call` 접미 포함, 07_03 `ch1_ev_004`)의 라인 조건 회수다. 트리거 조건이 아니므로 어떤 선택 이력이든 화해는 발생한다.

## 4. QA 메모 (15_QA 연동)

- 카탈로그 13종의 `emotion_tags`는 전부 CH4 태그 집합 `{guilt, reconciliation}`의 부분집합임을 빌드 검증에 포함한다 (D-005).
- 교차 챕터 태그 3종(`mem_ch3_inlaw_discipline`, `mem_ch3_first_quarrel`, `mem_ch3_compare_night`)은 07_05 확정 태그와 일치함을 확인했다.
- `ch4_ev_001`~`002`는 감정 장면 — 진입~종료까지 수치 HUD 완전 숨김 (D-004). 대본 전 라인은 감정 직접 서술 금지 검사 대상 (07_02 금지 패턴 2).
- `npc_cohort_yujin`(`ch4_ev_012`)·`npc_daycare_teacher`(`ch4_ev_003`)의 등장 챕터는 CH4까지다 (06_03) — CH5 회수 계획은 인물 재등장이 아니라 사물(문자·신발장)로만 수행한다.
- day 값(1860~2130)은 CH4 재생일 캘린더(`ch4_day_01`~`ch4_day_14`) 확정 시 재생일 매핑으로 조정한다 (02_03 1절).
- `money` 효과는 12_DATABASE 물가 상수 확정 시 상수 참조로 교체한다.
