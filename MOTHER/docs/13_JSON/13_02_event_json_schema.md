# 13_02 Event JSON Schema

이벤트 파일(`data/events/ch{n}/{event_id}.json`, 13_01)의 JSON Schema(draft-07). 이벤트 골격은 07_EVENT의 캐논 구조를 따르고, `trigger.conditions`와 라인 조건의 문법은 13_03이 소유한 조건식 정의와 동일하다.

## 1. 스키마 정의

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://mother-game.local/schemas/event.schema.json",
  "title": "event",
  "type": "object",
  "required": ["schema_version", "event_id", "chapter", "title_kr", "emotion_tags", "trigger", "priority", "scenes", "choices", "once", "cooldown_days"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "type": "string", "pattern": "^[0-9]+\\.[0-9]+$" },
    "event_id": { "type": "string", "pattern": "^ch[1-5]_ev_[0-9]{3}$" },
    "chapter": { "type": "integer", "minimum": 1, "maximum": 5 },
    "title_kr": { "type": "string", "minLength": 1, "maxLength": 40 },
    "emotion_tags": {
      "type": "array",
      "minItems": 1,
      "uniqueItems": true,
      "items": {
        "enum": ["overwhelmed", "wonder", "isolation", "joy", "burnout", "reward", "pride", "worry", "comparison", "guilt", "reconciliation", "letting_go", "fulfillment", "loss"]
      }
    },
    "trigger": {
      "type": "object",
      "required": ["type", "conditions"],
      "additionalProperties": false,
      "properties": {
        "type": { "enum": ["scheduled", "conditional", "random"] },
        "conditions": { "type": "array", "items": { "$ref": "#/definitions/condition" } },
        "weight": { "type": "integer", "minimum": 1, "maximum": 100 }
      }
    },
    "priority": { "type": "integer", "minimum": 0, "maximum": 100 },
    "scenes": {
      "type": "array",
      "items": { "type": "string", "pattern": "^ch[1-5]_sc_[0-9]{3}$" }
    },
    "choices": {
      "type": "array",
      "minItems": 1,
      "maxItems": 4,
      "items": { "$ref": "#/definitions/choice" }
    },
    "once": { "type": "boolean" },
    "cooldown_days": { "type": "integer", "minimum": 0 }
  },
  "definitions": {
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
    },
    "effects": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "attachment": { "type": "integer", "minimum": -20, "maximum": 20 },
        "child_condition": { "type": "integer", "minimum": -20, "maximum": 20 },
        "stamina": { "type": "integer", "minimum": -20, "maximum": 20 },
        "mind": { "type": "integer", "minimum": -20, "maximum": 20 },
        "money": { "type": "integer" },
        "confidence": { "type": "integer", "minimum": -3, "maximum": 3 },
        "empathy": { "type": "integer", "minimum": -3, "maximum": 3 },
        "independence": { "type": "integer", "minimum": -3, "maximum": 3 },
        "expressiveness": { "type": "integer", "minimum": -3, "maximum": 3 },
        "rel": {
          "type": "object",
          "additionalProperties": false,
          "patternProperties": { "^npc_[a-z_]+$": { "type": "integer", "minimum": -10, "maximum": 10 } }
        }
      }
    },
    "choice": {
      "type": "object",
      "required": ["choice_id", "text_kr", "effects"],
      "additionalProperties": false,
      "properties": {
        "choice_id": { "type": "string", "pattern": "^ch[1-5]_ev_[0-9]{3}_c[0-9]+$" },
        "text_kr": { "type": "string", "minLength": 1, "maxLength": 60 },
        "requires": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mind_min": { "type": "integer", "minimum": 0, "maximum": 100 },
            "stamina_min": { "type": "integer", "minimum": 0, "maximum": 100 },
            "money_min": { "type": "integer", "minimum": 0 }
          }
        },
        "effects": { "$ref": "#/definitions/effects" },
        "memory_tag": { "type": "string", "pattern": "^mem_ch[1-5]_[a-z0-9_]+$" }
      }
    }
  }
}
```

스키마로 표현하지 않는 규칙(빌드 린트 검사, 13_01 §6): ① `event_id`의 챕터 접두와 `chapter` 값 일치 ② `emotion_tags`가 소속 챕터의 01_04 목표 감정에 부합 ③ `scenes`·`memory_tag` 참조 무결성 ④ `trigger.weight`는 `type: random`일 때만 허용.

## 2. 유효 예시

```json
{
  "schema_version": "1.0",
  "event_id": "ch1_ev_001",
  "chapter": 1,
  "title_kr": "낯선 첫 밤",
  "emotion_tags": ["overwhelmed", "isolation"],
  "trigger": { "type": "scheduled", "conditions": [{ "stat": "day_counter", "op": "eq", "value": 1 }] },
  "priority": 90,
  "scenes": ["ch1_sc_001"],
  "choices": [
    {
      "choice_id": "ch1_ev_001_c1",
      "text_kr": "우는 아이를 안고 거실을 서성인다",
      "effects": { "attachment": 3, "stamina": -6 },
      "memory_tag": "mem_ch1_first_night"
    },
    {
      "choice_id": "ch1_ev_001_c2",
      "text_kr": "잠시 두고 심호흡부터 한다",
      "effects": { "mind": 2, "attachment": -1 }
    }
  ],
  "once": true,
  "cooldown_days": 0
}
```

## 3. 무효 예시 1 — 패턴·최소 개수 위반

```jsonc
{
  "schema_version": "1.0",
  "event_id": "ch6_ev_001",        // 실패: 패턴 ^ch[1-5]_ev_[0-9]{3}$ 위반 (챕터는 1~5뿐, D-001)
  "chapter": 6,                    // 실패: maximum 5 위반
  "title_kr": "초등 2학년",
  "emotion_tags": [],              // 실패: minItems 1 위반 (감정 태그 필수, D-005)
  "trigger": { "type": "scheduled", "conditions": [] },
  "priority": 10,
  "scenes": [],
  "choices": [{ "choice_id": "ch6_ev_001_c1", "text_kr": "…", "effects": {} }],
  "once": true,
  "cooldown_days": 0
}
```

## 4. 무효 예시 2 — enum·상한·명명 위반

```jsonc
{
  "schema_version": "1.0",
  "event_id": "ch2_ev_030",
  "chapter": 2,
  "title_kr": "떼쓰기 대치",
  "emotion_tags": ["burnout"],
  "trigger": { "type": "daily", "conditions": [] },   // 실패: type enum(scheduled|conditional|random) 위반, D-010
  "priority": 20,
  "scenes": [],
  "choices": [
    {
      "choice_id": "ch2_ev_030_c1",
      "text_kr": "끝까지 기다려 준다",
      "effects": { "independence": 5 },               // 실패: 성격 축 maximum 3 위반 (1회 변동 상한 ±3, D-008)
      "memory_tag": "first_tantrum"                   // 실패: 패턴 ^mem_ch[1-5]_… 위반 (mem_ch2_first_tantrum 이어야 함)
    }
  ],
  "once": false,
  "cooldown_days": 2
}
```

무효 예시의 `//` 주석은 문서 설명용(jsonc)이며 실제 데이터 파일에서는 주석 금지(13_01 §5).
