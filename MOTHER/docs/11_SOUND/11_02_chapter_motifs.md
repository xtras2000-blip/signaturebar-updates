# 11_02 Chapter Motifs

11_01의 원칙(BGM은 감정 장면에만, 01_04 우선순위 4번)을 전제로, 챕터별 음악 모티프와 자동 선곡 규칙을 정의한다.

## 1. 챕터별 모티프 표

| 챕터 | 모티프명 | 악기 편성 | BPM 범위 | 조성 | 연동 emotion_tags |
|---|---|---|---|---|---|
| CH1 | `motif_smallhours` (새벽의 시간) | 펠트 피아노 솔로 + 룸 노이즈 잔향 | 54~62 | A 단조 | `overwhelmed`, `isolation` |
| CH1 | `motif_lullaby` (자장가, §2) | 엄마 허밍(무반주) | 60~66 | F 장조 | `wonder` |
| CH2 | `motif_firststeps` (첫걸음) | 어쿠스틱 기타 + 글로켄슈필 + 브러시 퍼커션 | 92~104 | C 장조 | `joy`, `reward` |
| CH2 | `motif_smallhours_var1` (새벽의 시간 변주) | 펠트 피아노 + 첼로 지속음 | 50~58 | A 단조 | `burnout` |
| CH3 | `motif_playground` (놀이터) | 우쿨렐레 + 피치카토 스트링 + 멜로디카 | 100~112 | G 장조 | `pride` |
| CH3 | `motif_othersgarden` (남의 집 아이) | 피아노 + 비브라폰, 지속 페달 | 66~74 | E 단조 | `worry`, `comparison` |
| CH4 | `motif_halflight` (반쯤 남은 빛) | 나일론 기타 + 첼로 듀오 | 60~70 | D 단조 → 후반 D 장조 전조 | `guilt`, `reconciliation` |
| CH5 | `motif_springgate` (교문 앞 봄) | 실내악(현 4부 + 목관 2) | 76~84 | F 장조 | `letting_go`, `fulfillment` |
| CH5 | `motif_emptyroom` (빈 방) | 펠트 피아노 솔로(CH1 음색 재사용) | 54~60 | A 단조 → F 장조 종지 | `loss` |

- 파일명은 11_01 규칙: `bgm_ch{n}_{motif}_{variant}` 예: `bgm_ch3_othersgarden_a`.
- 전 트랙 공통 제약: 크레셴도 상한 +6dB, 스트링 스웰 단독 금지(11_01 §1-3). 60초 내 자연 종지 가능한 구조로 작곡(감정 장면 길이 가변 대응).

## 2. 핵심 장치 — 자장가 모티프의 7년 변주

`motif_lullaby`는 게임 전체를 관통하는 단일 선율(F 장조, 8마디)이다. 부르는 주체가 엄마 → 아이 → 세계로 옮겨가며 Pillar 4(선택은 쌓여서 사람이 된다)를 음악으로 구현한다.

| 단계 | 트랙 | 챕터·장면 | 편성·처리 | 의미 |
|---|---|---|---|---|
| 1 | `bgm_ch1_lullaby_hum` | CH1 야간 수유·재우기 장면 (`wonder` 성립 시) | 엄마 허밍 무반주, 60~66 BPM, 로파이 룸 톤 | 엄마가 아이에게 주는 소리 |
| 2 | `bgm_ch3_lullaby_child` | CH3 아이가 인형을 재우며 따라 부르는 이벤트 | 아이 목소리(음정 불안정 그대로 녹음) + 오르골 | 소리가 아이에게 옮겨감. attachment ≥ 70(`secure` 밴드)일 때만 발생하는 conditional 이벤트로 07_EVENT에 등록 |
| 3 | `bgm_ch5_lullaby_orch` | CH5 입학식 엔딩 장면 | 실내악 전체 편성(§1 CH5 편성) + 마지막 4마디 무반주 허밍 회귀 | 7년의 회수. memory_log 엔딩 연출의 음악적 결론 |

- 규칙: 단계 2는 단계 1을 플레이어가 실제로 들은 세이브에서만 발생한다(memory_log에 `mem_ch1_lullaby_heard` 기록 필요). 듣지 못한 세이브에서는 단계 3이 오르골 버전(`bgm_ch5_lullaby_orch_b`, 허밍 없음)으로 대체된다 — 회수 없는 연출 금지(Pillar 4).
- 선율 원본 악보와 스템은 12_DATABASE 에셋 테이블에서 버전 관리한다.

## 3. 트리거 규칙 — emotion_tags 자동 선곡

BGM은 이벤트별 수동 지정이 아니라 event JSON의 `emotion_tags`(D-005 필수 필드)로 자동 선곡한다. 콘텐츠 제작자는 음악을 신경 쓰지 않아도 된다.

1. 이벤트의 감정 장면 진입(HUD 페이드아웃, D-004 시점) 시 `emotion_tags`를 §1 표에서 조회한다.
2. 태그 복수 매칭 시 우선순위: 챕터 일치 모티프 > 첫 번째 태그(`emotion_tags[0]`이 핵심 감정) > BPM이 낮은 트랙.
3. 매칭 결과가 없거나 이벤트에 `silence: true`가 지정되면 무음 설계(11_01 §1-4)를 따른다. **무음이 기본값이다** — 억지로 채우지 않는다.
4. 페이드인 3초, 장면 종료 시 페이드아웃 4초 후 `bus_bgm` 뮤트 복귀. 같은 트랙은 게임 내 3일 쿨다운(07_EVENT `cooldown_days`와 동일 단위)으로 반복 피로를 방지한다.

```json
{
  "bgm_select_rules": {
    "source_field": "emotion_tags",
    "priority": ["chapter_match", "first_tag", "lowest_bpm"],
    "fallback": "silence",
    "fade_in_sec": 3,
    "fade_out_sec": 4,
    "track_cooldown_days": 3
  }
}
```

`bgm_tag_map` 초기값 (13개 태그 전체):

| emotion_tag | 기본 track_id |
|---|---|
| `overwhelmed` | `bgm_ch1_smallhours_a` |
| `wonder` | `bgm_ch1_lullaby_hum` |
| `isolation` | (무음 — §3 규칙 3, 의도적 미매핑) |
| `joy` / `reward` | `bgm_ch2_firststeps_a` |
| `burnout` | `bgm_ch2_smallhours_var1_a` |
| `pride` | `bgm_ch3_playground_a` |
| `worry` / `comparison` | `bgm_ch3_othersgarden_a` |
| `guilt` / `reconciliation` | `bgm_ch4_halflight_a` |
| `letting_go` / `fulfillment` | `bgm_ch5_springgate_a` |
| `loss` | `bgm_ch5_emptyroom_a` |

- 스키마 소유: 매핑 테이블(`bgm_tag_map`: emotion_tag, chapter, track_id)은 12_DATABASE, 필드 규격은 13_JSON.
- QA: `emotion_tags`가 있으나 매핑이 비어 있는 조합은 빌드 린트에서 경고(리젝 아님 — 무음이 유효한 선택이므로). 검증 항목은 15_02 QA-11 계열.

## 4. 구현 규격 — 스템·레이어

| 항목 | 규격 |
|---|---|
| 스템 분리 | 트랙당 최대 3스템(`_stem_lead` / `_stem_harm` / `_stem_perc`). 장면 길이에 따라 harm/perc 스템을 뺀 축소 편성으로 시작해 층을 더한다 |
| 루프 구조 | 인트로 4마디 + 루프 본체 + 종지 4마디. 장면 종료 신호 수신 시 다음 마디 경계에서 종지로 점프 |
| 템포 동기 | 없음. 게임플레이 리듬(블록 진행)과 음악을 동기화하지 않는다 — 음악이 진행을 재촉하는 인상 금지 |
| 믹스 기준 | 11_01 §5 라우드니스(-18 LUFS) 준수. `motif_lullaby` 계열만 −20 LUFS(더 멀리, 더 작게) |
| 납품 | 48kHz/24bit WAV 스템 + 풀믹스. 파일명 예: `bgm_ch4_halflight_a_stem_lead` |

- 작곡 발주서에는 본 문서 §1 표의 행(편성·BPM·조성·태그)과 레퍼런스 장면 스크립트(07_EVENT)를 함께 전달한다. 태그 정의 없이 "슬픈 곡" 같은 형용사 발주 금지.
- 신규 모티프 추가는 챕터 감정 목표(01_04 §1)와의 매핑을 명시해 본 문서 §1 표에 등록한 뒤에만 제작한다.
