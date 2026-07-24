# 07_03 CH1 Event List

CH1(0~12개월) 이벤트 카탈로그. 시스템 규칙은 07_01, 작성 규칙은 07_02를 따른다.
CH1 감정 목표: 압도됨(`overwhelmed`), 경이(`wonder`), 고립감(`isolation`) — 01_04.

## 1. 이벤트 카탈로그

| event_id | 제목 | class | 트리거 (유형 · 조건 요약) | emotion_tags | 대표 memory_tag | 회수 챕터 |
|---|---|---|---|---|---|---|
| `ch1_ev_001` | 조리원 퇴소 | major | scheduled · day 1 | overwhelmed | `mem_ch1_leaving_center` | CH5 (입학식 아침, 같은 가방) |
| `ch1_ev_002` | 첫 예방접종 | minor | scheduled · day 28~35 | overwhelmed, wonder | `mem_ch1_first_vaccine` | CH3 (접종에 익숙해진 대기실 대비) |
| `ch1_ev_003` | 밤중 수유 연속 3일 | major | conditional · streak night_feeding≥3 AND stamina<40 | overwhelmed | `mem_ch1_night_feeding` | CH2 (통잠 첫날 회상) |
| `ch1_ev_004` | 첫 미소 | major | scheduled · day 45~60 | wonder | `mem_ch1_first_smile` | CH4 (화해 장면, 앨범 사진) |
| `ch1_ev_005` | 산후우울 신호 | major | conditional · mind<35 | isolation | `mem_ch1_dark_morning` | CH4 (남편의 뒤늦은 사과) |
| `ch1_ev_006` | 남편 육아 갈등 | major | conditional · rel_npc_husband<45 | overwhelmed, isolation | `mem_ch1_husband_fight` | CH4 (같은 문장의 재등장) |
| `ch1_ev_007` | 친정엄마 방문 | minor | random · weight 20 | isolation | `mem_ch1_grandma_visit` | CH5 (역전된 돌봄) |
| `ch1_ev_008` | 맘카페 비교 | minor | random · time_block=night, weight 15 | isolation | `mem_ch1_momcafe_compare` | CH3 (비교 불안의 재점화) |
| `ch1_ev_009` | 복직 압박 전화 | major | scheduled · day 270~300 | overwhelmed | `mem_ch1_return_pressure` | CH2 (복직 첫날 조퇴) |
| `ch1_ev_010` | 돌잔치 | major | scheduled · day 360~370 | wonder, overwhelmed | `mem_ch1_doljanchi` | CH5 (입학식 = 두 번째 돌잔치) |
| `ch1_ev_011` | 첫 뒤집기 | minor | random · day 90~150, weight 25 | wonder | `mem_ch1_first_rollover` | CH2 (첫 걸음과 병치) |
| `ch1_ev_012` | 이유식 시작 | minor | scheduled · day 180~200 | overwhelmed, wonder | `mem_ch1_first_babyfood` | CH2 (편식 전쟁의 기원) |
| `ch1_ev_013` | 첫 열 감기 | major | conditional · child_condition<50 | overwhelmed | `mem_ch1_first_fever` | CH3 (의연해진 두 번째 밤) |
| `ch1_ev_014` | 조리원 동기 모임 | minor | random · weight 15 | isolation | `mem_ch1_cohort_meetup` | CH5 (같은 학교 재회) |
| `ch1_ev_015` | 어린이집 입소 대기 신청 | minor | scheduled · day 200~240 | overwhelmed | `mem_ch1_daycare_waitlist` | CH2 (입소 통보 전화) |
| `ch1_ev_016` | 남편 야근 연속 | minor | random · time_block=evening, weight 15 | isolation | `mem_ch1_alone_evening` | CH4 (빈 식탁의 재등장) |

- 회수 챕터 열은 각 이벤트 JSON `callback_plan`과 1:1로 교차 검증한다 (07_02 2절).
- `once`는 전 이벤트 true, 단 `ch1_ev_008`(맘카페 비교)·`ch1_ev_016`(야근 연속)은 `once:false, cooldown_days:14`.
- 슬롯 검증: major 8종은 발생 창이 겹치지 않도록 day 창·조건을 설계했다. 겹칠 경우 07_01 선정 규칙으로 해소.

## 2. 대표 이벤트 전체 JSON

### 2.1 ch1_ev_004 첫 미소

```json
{
  "event_id": "ch1_ev_004", "chapter": 1, "title_kr": "첫 미소", "event_class": "major",
  "emotion_tags": ["wonder"], "priority": 80, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [{ "type": "day_range", "min": 45, "max": 60 }] },
  "scenes": [
    { "scene_id": "ch1_ev_004_s1", "location_id": "loc_home_living", "time_block": "midday",
      "script_kr": ["건조대의 빨래를 걷다가 돌아본다.", "매트 위의 아이가 눈을 맞춘다. 입꼬리가 올라간다.", "빨래가 바닥에 떨어진다."] },
    { "scene_id": "ch1_ev_004_s2", "location_id": "loc_home_living", "time_block": "midday",
      "script_kr": ["손이 저절로 휴대폰을 찾는다. 그 사이에도 웃음이 사라질까 봐 눈을 못 뗀다."] }
  ],
  "choices": [
    { "choice_id": "ch1_ev_004_c1", "text_kr": "사진이고 뭐고, 그냥 마주 웃는다",
      "effects": { "attachment": 5, "stamina": -2 }, "memory_tag": "mem_ch1_first_smile" },
    { "choice_id": "ch1_ev_004_c2", "text_kr": "떨리는 손으로 동영상부터 찍는다",
      "effects": { "attachment": 2, "rel_npc_husband": 3 }, "memory_tag": "mem_ch1_first_smile_video" },
    { "choice_id": "ch1_ev_004_c3", "text_kr": "남편에게 바로 전화를 건다 — 회의 중이라도",
      "effects": { "rel_npc_husband": 5, "attachment": 1, "mind": 2 }, "memory_tag": "mem_ch1_first_smile_call" }
  ],
  "callback_plan": [
    { "chapter": 4, "memory_tag": "mem_ch1_first_smile",
      "usage_kr": "CH4 화해 장면에서 남편이 앨범(또는 그날의 동영상)을 꺼내며 갈등을 푸는 매개로 회수" }
  ]
}
```

### 2.2 ch1_ev_010 돌잔치

```json
{
  "event_id": "ch1_ev_010", "chapter": 1, "title_kr": "돌잔치", "event_class": "major",
  "emotion_tags": ["wonder", "overwhelmed"], "priority": 95, "once": true, "cooldown_days": 0,
  "trigger": { "type": "scheduled", "conditions": [
    { "type": "day_range", "min": 360, "max": 370 },
    { "type": "holiday", "value": "child_birthday" } ] },
  "scenes": [
    { "scene_id": "ch1_ev_010_s1", "location_id": "loc_home_living", "time_block": "morning",
      "script_kr": ["돌상 대여 박스, 답례품 스티커, 한복 소매의 뻣뻣한 풀기.", "시어머니는 벌써 두 번 전화했다. 상에 대추가 몇 개 올라가는지에 대해서."] },
    { "scene_id": "ch1_ev_010_s2", "location_id": "loc_home_living", "time_block": "afternoon",
      "script_kr": ["돌잡이 상 앞. 조리원 동기들, 양가 어른들, 카메라 여섯 대.", "아이의 손이 실과 연필과 지폐 사이에서 허공을 젓는다."] }
  ],
  "choices": [
    { "choice_id": "ch1_ev_010_c1", "text_kr": "아이가 잡을 때까지 기다린다 — 어른들의 훈수는 웃어넘긴다",
      "effects": { "attachment": 4, "independence": 2, "rel_npc_mother_in_law": -3, "stamina": -5 },
      "memory_tag": "mem_ch1_doljanchi_wait" },
    { "choice_id": "ch1_ev_010_c2", "text_kr": "시어머니가 미는 연필을 슬쩍 아이 앞으로 옮겨 준다",
      "effects": { "rel_npc_mother_in_law": 5, "independence": -2, "mind": -3 },
      "memory_tag": "mem_ch1_doljanchi_pencil" },
    { "choice_id": "ch1_ev_010_c3", "text_kr": "돌잡이보다 답례품 정산이 급하다 — 진행을 서두른다",
      "effects": { "money": -600000, "stamina": 3, "attachment": -2 },
      "memory_tag": "mem_ch1_doljanchi_rush" }
  ],
  "callback_plan": [
    { "chapter": 5, "memory_tag": "mem_ch1_doljanchi_wait",
      "usage_kr": "CH5 입학식 아침, 돌잡이에서 아이가 잡았던(혹은 어른이 쥐여 준) 물건을 책가방에 넣어 주는 장면으로 회수" }
  ]
}
```

### 2.3 ch1_ev_005 산후우울 신호

```json
{
  "event_id": "ch1_ev_005", "chapter": 1, "title_kr": "산후우울 신호", "event_class": "major",
  "emotion_tags": ["isolation"], "priority": 90, "once": true, "cooldown_days": 0,
  "trigger": { "type": "conditional", "conditions": [
    { "type": "stat", "key": "mind", "op": "<", "value": 35 },
    { "type": "time_block", "value": "morning" } ] },
  "scenes": [
    { "scene_id": "ch1_ev_005_s1", "location_id": "loc_home_bedroom", "time_block": "morning",
      "script_kr": ["커튼 틈으로 해가 들어왔는데, 몸이 이불 밖으로 나가지지 않는다.", "옆방에서 아이가 칭얼거린다. 숫자를 센다. 열까지. 다시 열까지."] },
    { "scene_id": "ch1_ev_005_s2", "location_id": "loc_home_bedroom", "time_block": "morning",
      "script_kr": ["휴대폰 화면. 부재중 없음. 마지막 어른과의 대화는 사흘 전 택배 기사님이었다."] }
  ],
  "choices": [
    { "choice_id": "ch1_ev_005_c1", "text_kr": "친정엄마에게 전화를 걸어 아무 말이나 한다",
      "effects": { "mind": 6, "rel_npc_grandma": 4, "stamina": -3 }, "memory_tag": "mem_ch1_dark_morning_call" },
    { "choice_id": "ch1_ev_005_c2", "text_kr": "보건소 산후우울 검사를 검색해 예약 버튼까지 간다",
      "effects": { "mind": 4, "money": -20000, "stamina": -5 }, "memory_tag": "mem_ch1_dark_morning_screening" },
    { "choice_id": "ch1_ev_005_c3", "text_kr": "괜찮다고 쓰고, 맘카페 글을 지운다",
      "effects": { "mind": -4, "stamina": 2 }, "memory_tag": "mem_ch1_dark_morning_alone" }
  ],
  "callback_plan": [
    { "chapter": 4, "memory_tag": "mem_ch1_dark_morning_alone",
      "usage_kr": "CH4 부부 화해 장면에서 남편이 '그때 몰랐다'고 그 아침을 처음 언급하며 회수. 도움을 청했던 선택이면 사과의 결이 달라진다" }
  ]
}
```

## 3. QA 메모 (15_QA 연동)

- `ch1_ev_005`는 D-004 적용 대표 케이스: 진입~종료까지 수치 HUD 완전 숨김, `mind` 값 언급 금지.
- 대본 전 라인은 감정 직접 서술 금지 검사 대상 (07_02 금지 패턴 2 — "엄마는 슬펐다" 류 리젝).
- 카탈로그 16종의 `emotion_tags`는 전부 CH1 태그 집합 `{overwhelmed, wonder, isolation}`의 부분집합임을 빌드 검증에 포함한다 (D-005).
- `ch1_ev_010`의 `money` 효과(-600,000원)는 12_DATABASE 물가 상수 확정 시 상수 참조로 교체한다.
