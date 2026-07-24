# 02_05 Vertical Slice Scope

CH1(0~12개월)의 재생일 4일 분량을 실제 모바일 기기에서 플레이 가능한 빌드로 만드는 수직 슬라이스의 범위 정의. 코어 루프는 02_01, 시간 블록은 02_02, 재생일 구조는 02_03, 이벤트 정본은 07_03, 화면 흐름은 09_02를 따른다. 본 문서는 "무엇을 넣고 무엇을 뺄지"만 소유하며, 각 시스템의 명세는 원 소유 문서를 변경하지 않는다.

## 1. 목표 정의

- **정의**: 수직 슬라이스 = CH1 재생일 4일(`day_start → block_allocation → block_resolution ×5 → day_end_summary → autosave` 완전 루프 4회)을 실제 모바일 기기(iOS/Android 각 1대 이상, D-017)에서 설치·플레이 가능한 빌드.
- **목적**: (a) "20~40분 세션에 재생일 3~5일"(D-016)이 모바일 세로 화면·한 손 탭에서 성립하는지 검증 (b) CH1 감정 목표(압도됨·경이·고립감, 01_04)가 수치 숨김(D-004) 상태의 연출만으로 전달되는지 검증.

성공 기준:

| 구분 | 기준 | 근거 |
|---|---|---|
| 감정 | 플레이테스트 설문에서 CH1 감정 형용사(`overwhelmed`/`wonder`/`isolation`) 선택률 60% 이상 | 01_04 §4 |
| 감정 | `ch1_ev_004`(첫 미소) 장면에서 목표 감정 `wonder` 선택률 60% 이상(장면 단위 문항 추가) | 01_04 §1 |
| 기술 | 세로 화면 고정, 한 손 탭만으로 4일 완주 가능(뒤로가기 버튼 0개) | D-017, 09_02 QA SF-06 |
| 기술 | day_end_summary 직후 autosave 동작, 강제 종료 후 이어하기 시 전일 마감 지점에서 재개 | 02_01 §2.5, 09_02 QA SF-04 |
| 기술 | 재생일 체감 시간: milestone 10~15분, routine 3~5분 범위 준수 | D-016 |

## 2. 포함 재생일 4일 선정과 근거

02_03의 CH1 구성(16일 = milestone 7 + routine 8 + transition 1)에서 milestone 2일 + routine 2일을 발췌한다. 선정 원칙: ① CH1 감정 태그 3종을 모두 1회 이상 커버 ② 트리거 유형 scheduled·conditional을 모두 검증 ③ 4일이 연출 없이도 하나의 감정 곡선(도착 → 소모 → 경이 → 침몰)을 이루도록 배열.

| 슬라이스 순번 | day_id | day_kind | 날 정의 | 포함 이벤트 (event_id) | 선정 근거 |
|---|---|---|---|---|---|
| 1 | `ch1_day_01` | milestone | 조리원 퇴소일 (day 1) | `ch1_ev_001`(scheduled), `ch1_ev_night_feeding`(system) | 게임 시작일 = 튜토리얼. 블록 배분·행동 실행·야간 수유 강제 이벤트를 첫날에 전부 학습. `overwhelmed` 개시 |
| 2 | `ch1_day_03` | routine | 밤중 수유 루틴일 | `ch1_ev_003`(conditional: streak night_feeding≥3 AND stamina<40), `ch1_ev_night_feeding` | routine 일의 3~5분 리듬 검증 + conditional 트리거·`night_rest_bonus`=0 누적으로 stamina가 깎이는 "자원은 항상 부족하다"(Pillar 2) 체감일 |
| 3 | `ch1_day_04` | milestone | 첫 미소일 (day 45~60 창) | `ch1_ev_004`(scheduled), `ch1_ev_night_feeding` | 슬라이스의 감정 정점. `wonder` 단독 태그 이벤트로 D-004(수치 숨김 + 연출 전달)의 대표 검증 케이스 |
| 4 | `ch1_day_05` | routine | 산후우울 신호일 | `ch1_ev_005`(conditional: mind<35, morning), `ch1_ev_night_feeding` | `isolation` 커버 + 수치 조건 트리거의 2차 검증. 07_03 QA 메모의 D-004 대표 케이스(HUD 완전 숨김, mind 언급 금지) 포함 |

- 재생일 사이 건너뛴 기간은 02_03 §1의 경과 자막("6주 후" 형식)으로 처리한다. 몽타주 연출(챕터 전환)은 제외 대상이므로 자막만 구현.
- `ch1_ev_005`의 mind<35 성립을 위해 슬라이스 밸런스는 D-009 초기값(mind 60)에서 day 1~3의 소모가 임계 아래로 내려가도록 검수한다. 미성립 시 `ch1_day_05`는 일반 routine으로 진행되어도 완주 가능해야 한다(실패 없음, D-002).
- 랜덤 이벤트(`ch1_ev_007`/`008` 등)는 4일 어디에도 포함하지 않는다 — 3절 제외 표 참조.

## 3. 포함 시스템 / 제외 시스템

### 3.1 포함

| 시스템 | 범위 | 원 소유 문서 |
|---|---|---|
| 시간 블록 루프 | `day_start → block_allocation → block_resolution ×5 → day_end_summary → autosave` 전체. 블록 상태 머신(`idle`~`resolved`) 완전 구현 | 02_01, 02_02 |
| 이벤트 트리거 | scheduled + conditional 2유형과 4개 윈도우(`on_day_start`/`on_block_start`/`on_block_end`/`on_day_end`). random은 판정 코드만 두고 이벤트 풀 비움 | D-010, 02_01 §3 |
| 대사 재생 | scenes 순차 재생, 선택지 탭, 백로그(`ovl_backlog`) | 08_01 |
| 수치 5종 | attachment/child_condition/stamina/mind/money 내부 연산 전량 + 간접 표현(게이지·연출, 감정 장면 수치 숨김) | D-003, D-004, 03_01 |
| 자동 저장 | `autosave_slot` 단일 슬롯 덮어쓰기, 실패 시 1회 재시도, 이어하기 | 02_01 §2.5, 03_04 |
| memory_log | 선택 시 `memory_tag` 기록(기록만, 회수 연출 없음) | 03_03 |
| 화면 흐름 | `scr_title → scr_save_select → 하루 루프` + `ovl_pause` | 09_02 |

### 3.2 제외

| 시스템 | 제외 사유 | 슬라이스 내 처리 |
|---|---|---|
| 월 정산·가계 경제(03_02) | 4일 범위에서 월 주기 미도래 | day_end 생활비 차감(-30,000원)만 구현, `ovl_ledger` 제외 |
| NPC 스케줄 AI(14_02) | 슬라이스 이벤트에 NPC 자율 개입 불요 | 이벤트 대본 내 NPC 등장만. `rel_*` 수치는 효과 적용·기록만 |
| 챕터 전환·몽타주 | 4일은 CH1 내부 구간 | `ch1_day_05` autosave 후 "슬라이스 종료" 카드 1장 |
| 엔딩(02_04) | CH5 전용 | 미구현 |
| 성격 축 장기 누적(D-008) | 효과 반영 장면이 CH3 이후 | 선택 효과의 축 변화를 `child_state`에 기록만, 표현 없음 |
| random 트리거 이벤트 | 재현 불가한 QA 변수 제거 | 트리거 판정기는 존재, 풀 비움(3.1) |
| 수동 세이브 슬롯 3개 | autosave 검증이 목적 | `scr_save_select`는 자동 슬롯 1개만 표시 |

## 4. 필요 에셋 최소 세트

### 4.1 아트 (10_01 명명 규칙, 팔레트 `pal_ch1_dawn` 고정)

| 분류 | 에셋 id | 수량 | 비고 |
|---|---|---|---|
| 배경 — 거실 | `bg_livingroom_morning` / `_midday` / `_evening` / `_night` (+ 각 `_light` 레이어) | 4+4 | `loc_home_living`. 튜토리얼·첫 미소(`ch1_ev_004`) 무대 |
| 배경 — 안방 | `bg_bedroom_morning` / `_night` (+ 각 `_light` 레이어) | 2+2 | `loc_home_bedroom`. 야간 수유·산후우울(`ch1_ev_005`) 무대 |
| 캐릭터 — 엄마 | `spr_player_stable_idle`, `spr_player_strained_idle`, `spr_player_depleted_sit` | 3 | mind 밴드 3종 포즈 세트(10_02 §1) 최소 각 1점 |
| 캐릭터 — 아기 | `spr_child_age0_lying`, `spr_child_age0_held`, `spr_child_age0_smile` | 3 | `age0` 단계만. `_smile`은 첫 미소 전용 컷 |
| 표정 세트 | `spr_player_stable_{expression}` 6종, `spr_child_age0_{expression}` 4종 | 10 | 10_02 §4 규격의 축약본(엄마 12종→6종, 아기 8종→4종) |
| UI 위젯 | `ui_blockbar_lock`, `ui_blockbar_slot`, `ui_stamina_gauge`, `ui_dayend_arrow_up`, `ui_dayend_arrow_down`, `ui_autosave_icon` | 6 | 09_03 위젯 중 블록 바·게이지·마감 요약·저장 아이콘만 |

### 4.2 사운드 (11_01 명명 규칙, 라우드니스 규격 준수)

| 분류 | 에셋 id | 수량 | 비고 |
|---|---|---|---|
| 생활음 | `sfx_ricecooker_steam`, `sfx_washer_end`, `sfx_bottle_shake`, `sfx_door_apt_close`, `sfx_clock_wall_tick`, `sfx_ui_confirm`, `amb_apt_night`, `amb_livingroom_morning` | 8 | 11_01 §5 P0 목록 우선. `sfx_clock_wall_tick`은 무음 설계 장면(야간 수유) 전용 |
| 자장가 모티프 | `bgm_ch1_lullaby_hum` | 1 | 11_02 §2. `wonder` 성립 시 종료 3초 전 페이드인 규칙 포함 |
| 울음 3유형 | `sfx_child_cry_fussy_01`, `sfx_child_cry_hunger_01`, `sfx_child_cry_pain_01`, `sfx_child_sob_calm` | 4 | 유형당 1테이크로 축약(정식 3테이크 라운드로빈은 슬라이스 이후). 달래기 종료용 `sob_calm` 포함 |

## 5. 기술 스택 제안 — D-021 제안 (미확정)

> 아래 엔진 선택은 **D-021 제안**으로 DECISION_LOG에 Pending 등재를 요청하는 안이며, **확정은 사용자 승인이 필요하다.** 승인 전 슬라이스 착수 금지.

| 기준 | Godot 4 | Unity |
|---|---|---|
| 비용 | 완전 무료(MIT) | Personal 무료지만 정책 변동 이력 |
| 빌드 경량성 | 모바일 2D 빌드 수십 MB 수준 | 런타임 포함으로 상대적으로 무거움 |
| 2D 내러티브 적합성 | 2D 전용 렌더러, 세로 해상도·앵커 대응 우수 | 2D는 3D 위 서브셋. 가능하나 과잉 스펙 |
| JSON 데이터 파이프라인 | `data/` JSON을 런타임 그대로 로드(내장 JSON 파서), 임포트 변환 불요 | ScriptableObject 변환 계층을 두는 관행 → 12_01 "정적 JSON 정본" 원칙과 마찰 |
| 팀 규모 적합성 | 소규모·문서 주도 파이프라인에 적합 | 대규모 에셋·3D 프로젝트에 강점 |

- **추천: Godot 4** — 무료·경량·2D 특화이며, 12_01 §3의 "정적 데이터 = `data/` JSON 읽기 전용" 경계를 변환 계층 없이 그대로 지킬 수 있다.
- 데이터 파이프라인: `data/events/ch1/*.json`(13_02 스키마 v1.1)과 `data/dialogues/`(13_03)를 빌드에 그대로 포함해 로드한다. 13_01 §의 스키마(draft-07) 검증 + 린트 규칙을 `validate` 스크립트로 작성하고 CI에서 커밋마다 실행, 실패 시 빌드 차단(D-005 자동 리젝의 구현체).

## 6. 작업 분해 (WBS)

기간은 상대 크기만 표기: S(수일) < M(1~2주 상당) < L(그 이상). 절대 일정은 기입하지 않는다.

| 트랙 | 작업 항목 | 크기 | 선행 |
|---|---|---|---|
| 프로그래밍 | 하루 루프 상태 머신(02_01 5단계) + 블록 상태 머신(02_02) | L | 엔진 확정(D-021) |
| 프로그래밍 | 이벤트 트리거 판정기(scheduled/conditional, 4윈도우, priority 선정) | M | 루프 골격 |
| 프로그래밍 | 대사 재생기(scenes/choices/백로그) + D-004 HUD 숨김 전환 | M | 루프 골격 |
| 프로그래밍 | 수치 5종 연산 + 간접 표현(게이지·포즈 세트 교체 훅) | M | 루프 골격 |
| 프로그래밍 | autosave/이어하기(단일 슬롯, 재시도 1회) | S | 루프 골격 |
| 프로그래밍 | 모바일 빌드 파이프라인(iOS/Android, 세로 고정) | M | 엔진 확정 |
| 아트 | 배경 2종 × 블록 라이팅 레이어(4.1 표) | L | 팔레트 캐논(10_01) |
| 아트 | 엄마·아기 스프라이트 + 표정 축약 세트 | M | 10_02 규격 |
| 아트 | UI 위젯 6종 | S | 09_03 명세 |
| 사운드 | 생활음 8종 녹음·정리(라우드니스 규격) | M | — |
| 사운드 | 울음 3유형 + `sob_calm`, 파라미터(피치·지터) 적용 | M | 버스 구조 구현 |
| 사운드 | `bgm_ch1_lullaby_hum` 1트랙 + 무음 설계 장면 연동 | S | 11_02 모티프 확정 |
| 데이터 | 4일치 이벤트 JSON(`ch1_ev_001/003/004/005`, `ch1_ev_night_feeding`) 정규화 | M | 13_02 v1.1 |
| 데이터 | 대사 JSON(08_04 정본 → 13_03 변환) 4일 분량 | M | 이벤트 JSON |
| 데이터 | validate 스크립트 + CI 연동(스키마·린트·emotion_tags 검사) | S | 13_01 규칙 |
| 데이터 | 슬라이스 밸런스 시트(2절 mind<35 성립 검수 포함) | S | 수치 연산 구현 |

## 7. 리스크와 컷 라인

### 7.1 잘라서는 안 되는 것 (슬라이스의 존재 이유)

1. **`ch1_ev_004` 첫 미소의 감정 순간** — 수치 숨김 + 라이팅 보정 + 무음→모티프 페이드인이 함께 성립해야 하는 슬라이스의 검증 목적 그 자체. 이 장면의 완성도가 미달이면 슬라이스는 실패로 판정한다.
2. 야간 수유 강제 이벤트와 `night_rest_bonus`=0 누적(압도됨의 시스템 구현).
3. autosave·이어하기(모바일 세션 패턴 D-017의 최소 요건).
4. 한 손 탭 완주(뒤로가기 0개, 09_02).

### 7.2 잘라도 되는 것 (일정 압박 시 컷 우선순위 순)

| 순위 | 컷 후보 | 컷 시 처리 |
|---|---|---|
| 1 | 표정 세트 축약분 일부(엄마 6→4종, 아기 4→3종) | `smile` 계열은 유지 |
| 2 | 울음 파라미터(피치 랜덤·지터) | 고정 재생으로 대체 |
| 3 | `ovl_backlog` | 설정에서 텍스트 속도만 제공 |
| 4 | `ch1_day_03`(밤중 수유 루틴일) → 3일 구성으로 축소 | conditional 검증은 `ch1_day_05`가 대체. 단 4일 미만은 D-016 세션 검증력이 약해지므로 최후 수단 |
| 5 | 블록 라이팅 레이어 일부(`_evening` 등 미사용 블록) | 인접 블록 레이어 재사용 |

- 주요 리스크: ① 엔진 확정(D-021) 지연 시 프로그래밍 트랙 전체 착수 불가 — 승인 전에는 데이터·아트·사운드 트랙만 선행 ② `ch1_ev_005` 조건 미성립 밸런스 — 2절의 검수 항목으로 관리 ③ 모바일 실기기 성능(배경 레이어 합성) — 아트 원본 규격(10_01 §5)을 유지하되 내보내기 해상도만 기기 프로파일로 조정.
