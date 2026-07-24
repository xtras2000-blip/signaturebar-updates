# 13_03 Dialogue JSON Schema

대사 씬 파일(`data/dialogues/ch{n}/{scene_id}.json`, 13_01)의 JSON Schema(draft-07)와 **조건식 문법의 단일 정의**. 이벤트 트리거(13_02)와 라인 조건은 모두 본 문서의 조건식 문법을 공유한다. scene/line 구조는 캐논(scene_id, line_id, speaker, text_kr, condition, emotion)을 따른다.

## 1. 조건식 문법 (condition)

조건 1개는 아래 3형식 중 하나의 객체다. 배열로 나열하면 **AND** 결합이며, OR는 지원하지 않는다(필요 시 라인·이벤트를 분리 제작 — 콘텐츠 단순성 우선).

| 형식 | 구조 | 예시 | 의미 |
|---|---|---|---|
| 수치 비교 | `{"stat": s, "op": o, "value": n}` | `{"stat": "attachment", "op": "gte", "value": 67}` | 핵심 수치·성격 축·`day_counter`·`chapter` 비교 |
| 기억 존재 | `{"memory": m, "exists": b}` | `{"memory": "mem_ch1_first_smile", "exists": true}` | memory_log에 해당 `memory_tag` 존재 여부 |
| NPC 관계 | `{"rel": npc, "op": o, "value": n}` | `{"rel": "npc_husband", "op": "lt", "value": 30}` | npc_relations의 `rel` 비교(14_02 톤 분기) |

- `op` 허용값: `lt`, `lte`, `gt`, `gte`, `eq`, `neq`.
- 평가 시점: 씬 재생 직전에 1회 평가하고 씬 재생 중에는 재평가하지 않는다(연출 중 수치 변화로 라인이 뒤바뀌는 것을 방지).
- `condition`이 없는 라인은 항상 재생된다.

## 2. 스키마 정의

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://mother-game.local/schemas/dialogue.schema.json",
  "title": "dialogue_scene",
  "type": "object",
  "required": ["schema_version", "scene_id", "lines"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+$" },
    "scene_id": { "type": "string", "pattern": "^ch[1-5]_sc_[0-9]{3}$" },
    "lines": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/definitions/line" }
    }
  },
  "definitions": {
    "line": {
      "type": "object",
      "required": ["line_id", "speaker", "text_kr"],
      "additionalProperties": false,
      "properties": {
        "line_id": { "type": "string", "pattern": "^ch[1-5]_sc_[0-9]{3}_l[0-9]{2}$" },
        "speaker": {
          "oneOf": [
            { "enum": ["player", "child", "system"] },
            { "type": "string", "pattern": "^npc_[a-z_]+$" }
          ]
        },
        "text_kr": { "type": "string", "minLength": 1, "maxLength": 120 },
        "condition": {
          "oneOf": [
            { "$ref": "#/definitions/condition" },
            { "type": "array", "minItems": 1, "items": { "$ref": "#/definitions/condition" } }
          ]
        },
        "emotion": {
          "enum": ["neutral", "soft", "warm", "tired", "tearful", "bright", "firm", "hesitant"]
        }
      }
    },
    "condition": {
      "oneOf": [
        {
          "type": "object",
          "required": ["stat", "op", "value"],
          "additionalProperties": false,
          "properties": {
            "stat": { "enum": ["attachment", "child_condition", "stamina", "mind", "money", "confidence", "empathy", "independence", "expressiveness", "day_counter", "chapter"] },
            "op": { "enum": ["lt", "lte", "gt", "gte", "eq", "neq"] },
            "value": { "type": "integer" }
          }
        },
        {
          "type": "object",
          "required": ["memory", "exists"],
          "additionalProperties": false,
          "properties": {
            "memory": { "type": "string", "pattern": "^mem_ch[1-5]_[a-z0-9_]+$" },
            "exists": { "type": "boolean" }
          }
        },
        {
          "type": "object",
          "required": ["rel", "op", "value"],
          "additionalProperties": false,
          "properties": {
            "rel": { "type": "string", "pattern": "^npc_[a-z_]+$" },
            "op": { "enum": ["lt", "lte", "gt", "gte", "eq", "neq"] },
            "value": { "type": "integer", "minimum": 0, "maximum": 100 }
          }
        }
      ]
    }
  }
}
```

- `speaker: "system"`은 화면 지시문 전용이며 감정 서술 문장 금지(01_04 §3 — "엄마는 슬펐다" 류 리젝).
- `emotion`은 연기 지시(보이스·표정·애니메이션 큐)로, 01_04의 `emotion_tags`(챕터 감정 목표)와는 다른 축이다.

## 3. 유효 예시

`data/dialogues/ch1/ch1_sc_001.json` — 이벤트 `ch1_ev_001`(13_02 §2)이 참조하는 씬:

```json
{
  "schema_version": "1.0",
  "scene_id": "ch1_sc_001",
  "lines": [
    {
      "line_id": "ch1_sc_001_l01",
      "speaker": "system",
      "text_kr": "새벽 세 시. 좁은 거실에 울음소리가 가득 찬다.",
      "emotion": "neutral"
    },
    {
      "line_id": "ch1_sc_001_l02",
      "speaker": "player",
      "text_kr": "그래, 그래. 엄마 여기 있어.",
      "emotion": "tired"
    },
    {
      "line_id": "ch1_sc_001_l03",
      "speaker": "npc_husband",
      "text_kr": "내가 안아 볼까? 당신 좀 누워.",
      "condition": { "rel": "npc_husband", "op": "gte", "value": 70 },
      "emotion": "soft"
    },
    {
      "line_id": "ch1_sc_001_l04",
      "speaker": "player",
      "text_kr": "…이 시간이 언제까지 계속되는 걸까.",
      "condition": [
        { "stat": "mind", "op": "lt", "value": 30 },
        { "memory": "mem_ch1_first_night", "exists": false }
      ],
      "emotion": "hesitant"
    }
  ]
}
```

## 4. 검증 규칙 (린트, 13_01 §6)

1. `scene_id` 챕터 접두와 디렉터리·참조 이벤트의 `chapter` 일치.
2. `line_id`는 `scene_id` + `_l` 접두를 가져야 하며 씬 내 유일.
3. `condition`의 `rel` 대상 NPC는 14_02 명부에 등록된 `npc_id`여야 한다.
4. `speaker: "child"`의 발화 라인은 챕터별 언어 발달 제한(05_CHILD)을 따른다 — CH1은 `text_kr`에 옹알이 표기만 허용.
