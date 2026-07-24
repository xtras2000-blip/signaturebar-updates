# 04_01 Player Profile

주인공(엄마, `player`)의 생성 옵션과 배경 프리셋을 정의하는 프로필 문서다. 표 중심 구성이며, 스탯의 동작 규칙은 04_02, 행동 목록은 04_03에서 정의한다.

## 1. 캐릭터 생성 옵션

| 항목 | 식별자 | 규칙 |
|---|---|---|
| 엄마 이름 | `player_name` | 한글 2~6자 커스텀 입력. 기본 제안값 "서연". 비속어 필터(12_DATABASE 금칙어 테이블) 통과 필수 |
| 배경 프리셋 | `background_preset` | 3종 중 1개 선택: `preset_worker` / `preset_freelancer` / `preset_fulltime`. 게임 시작 후 변경 불가 |
| 남편 이름 | `husband_name` | 한글 2~6자 커스텀 입력. 기본 제안값 "준호" |

- 이름은 모든 대사·이벤트 텍스트에서 치환 토큰 `{player_name}`, `{husband_name}`, `{child_name}`(05_01)으로 사용한다.

## 2. 배경 프리셋 3종

| 프리셋 | `background_preset` | 설정 | 핵심 서사 갈등 |
|---|---|---|---|
| 육아휴직 중 회사원 | `preset_worker` | 중견기업 대리, 출산 직후 1년 육아휴직 시작 | 복직 시한과 회사의 눈치, 경력 유지 vs 아이 |
| 프리랜서 | `preset_freelancer` | 재택 디자이너. 일감이 있을 때만 수입 발생 | 마감과 돌봄의 시간 블록 충돌, 수입 불안정 |
| 전업 | `preset_fulltime` | 외벌이 가구의 전업 엄마 | 남편 단일 수입 의존, 사회적 고립감(`isolation`) |

## 3. 프리셋별 초기 자원·수입 차등

D-009의 `money` 초기값 3,000,000원은 기준 프리셋(`preset_worker`)의 값이며, 다른 프리셋은 아래 보정을 적용한다.

| 프리셋 | 초기 `money` (원) | 월수입 `monthly_income` (원) | 수입 지급 방식 |
|---|---|---|---|
| `preset_worker` | 3,000,000 | 1,500,000 (육아휴직 급여) → 복직 후 2,800,000 | 매월 25일 자동 입금 |
| `preset_freelancer` | 2,400,000 | 800,000~2,000,000 (수주 이벤트 결과에 따라 변동, 기대값 1,400,000) | `act_work_remote_task` 완료 건별 입금 |
| `preset_fulltime` | 2,000,000 | 2,600,000 (남편 급여) | 매월 25일 자동 입금, 생활비 협의 이벤트로 조정 가능 |

- 월 고정 지출(주거·공과금·보험)은 프리셋 공통 1,900,000원. 상세 항목은 12_DATABASE 가계 상수 테이블에서 관리한다.
- 육아비(분유·기저귀·의료 등)는 챕터별 변동 지출로 07_EVENT와 04_03 행동 비용에서 발생한다.

## 4. 프리셋별 복직·일 압박 이벤트 차등

모든 이벤트는 D-005에 따라 `emotion_tags` 필수, D-010의 3유형 트리거를 따른다.

| 프리셋 | 이벤트(예시 id) | 트리거 | 내용 | 주요 `emotion_tags` |
|---|---|---|---|---|
| `preset_worker` | `ch1_ev_030` | scheduled (day 240) | 인사팀 복직 예정 확인 전화 | `overwhelmed` |
| `preset_worker` | `ch1_ev_031` | scheduled (day 330) | 복직 vs 휴직 연장 선택 (money·mind 분기) | `overwhelmed`, `isolation` |
| `preset_worker` | `ch2_ev_040` | conditional (`money` < 1,000,000) | 팀장의 조기 복귀 회유 연락 | `burnout` |
| `preset_freelancer` | `ch1_ev_032` | random (주당 가중치 0.25) | 급한 수정 요청, 밤 블록 작업 강요 | `overwhelmed` |
| `preset_freelancer` | `ch2_ev_041` | conditional (30일간 수입 0) | 장기 클라이언트 이탈 통보 | `burnout` |
| `preset_fulltime` | `ch2_ev_042` | random (월 가중치 0.3) | 동창의 복직 소식, 경력 공백 불안 | `isolation` |
| `preset_fulltime` | `ch3_ev_050` | scheduled (CH3 시작 +30일) | 재취업 정보 검색 선택 이벤트 | `worry`, `comparison` |

- `preset_worker`는 복직 압박이 scheduled 중심(시한이 정해진 압박), `preset_freelancer`는 random 중심(불규칙한 압박), `preset_fulltime`은 직접 압박 대신 비교·고립 계열로 차등화한다.

## 5. 남편의 육아 참여도

| 항목 | 식별자 | 범위 | 초기값 |
|---|---|---|---|
| 남편 육아 참여도 | `husband_support` | 0~100 | 프리셋별 차등 (아래) |

| 프리셋 | `husband_support` 초기값 | 근거 |
|---|---|---|
| `preset_worker` | 45 | 맞벌이 전제, 야근 잦은 직장 설정 |
| `preset_freelancer` | 50 | 재택 병행으로 분담 협의 여지가 가장 큼 |
| `preset_fulltime` | 40 | "집에 있으니 네가"라는 역할 고정 관념 반영 |

- `husband_support`는 D-003의 핵심 수치 5종에 포함되지 않는 보조 수치다. 신규 수치 추가 규칙에 따라 DECISION_LOG 등재(제안 D-011) 및 00_04 용어집 등록을 선행 조건으로 한다.
- 효과: `husband_support` ≥ 60이면 밤 블록 돌봄 이벤트의 50%를 남편이 대신 처리(엄마 `stamina` 소모 면제), ≤ 30이면 부부 갈등 conditional 이벤트 활성화. 변화는 선택 `effects`로만 발생하며 1회 변동 상한 ±5.

## 6. JSON

프로필 저장 스키마 예시 (13_JSON 세이브 포맷에 병합):

```json
{
  "player_profile": {
    "player_name": "서연",
    "background_preset": "preset_worker",
    "husband_name": "준호",
    "husband_support": 45,
    "monthly_income": 1500000,
    "money": 3000000
  }
}
```

## 7. QA 체크리스트

| ID | 확인 항목 | 통과 기준 |
|---|---|---|
| QA-0401-01 | 프리셋 3종 각각 새 게임 시작 | 초기 `money`·`monthly_income`·`husband_support`가 본 문서 표와 일치 |
| QA-0401-02 | `preset_worker`로 day 240 도달 | `ch1_ev_030` 발생, 타 프리셋에서는 미발생 |
| QA-0401-03 | 이름 커스텀에 7자 이상·특수문자 입력 | 입력 거부 및 안내 문구 표시 |
| QA-0401-04 | `husband_support` 변동 이벤트 반복 | 1회 변동이 ±5를 초과하지 않음 |
