#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOTHER 이벤트 JSON 검증 스크립트.

data/events/ch{n}/*.json 전체를 schemas/event.schema.json(13_02 정본에서 추출)으로
검증한다. jsonschema(draft-07)가 있으면 그것을 쓰고, 없으면 표준 라이브러리만으로
필수 필드·패턴·enum·범위를 직접 검사한다(폴백).

스키마 외 추가 린트(13_01 §6 일부):
  - lint_filename_id  : 파일명 == event_id + ".json"
  - lint_chapter_dir  : 디렉터리 ch{n} == chapter == event_id 접두
  - lint_memory_tag   : 모든 choice에 memory_tag 존재 (07_02 체크리스트 2)
  - lint_random_weight: trigger.weight는 type=random일 때만 (13_02 §1 비고)

사용법: python3 MOTHER/data/validate_events.py
종료 코드: 전 파일 통과 0, 위반 1.
"""
import json
import os
import re
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
EVENTS_DIR = os.path.join(DATA_DIR, "events")
SCHEMA_PATH = os.path.join(DATA_DIR, "schemas", "event.schema.json")

EMOTION_ENUM = [
    "overwhelmed", "wonder", "isolation", "joy", "burnout", "reward", "pride",
    "worry", "comparison", "guilt", "reconciliation", "letting_go",
    "fulfillment", "loss",
]
STAT_ENUM = [
    "attachment", "child_condition", "stamina", "mind", "money", "confidence",
    "empathy", "independence", "expressiveness", "day_counter", "chapter",
]
OP_ENUM = ["lt", "lte", "gt", "gte", "eq", "neq"]
TRIGGER_TYPES = ["scheduled", "conditional", "random"]
TRAIT_KEYS = ["confidence", "empathy", "independence", "expressiveness"]
STAT_EFFECT_KEYS = ["attachment", "child_condition", "stamina", "mind"]

RE_SCHEMA_VERSION = re.compile(r"^[0-9]+\.[0-9]+$")
RE_EVENT_ID = re.compile(r"^ch[1-5]_ev_([0-9]{3}|[a-z][a-z0-9_]*)$")
RE_SCENE = re.compile(r"^ch[1-5]_sc_[0-9]{3}$")
RE_CHOICE_ID = re.compile(r"^ch[1-5]_ev_([0-9]{3}|[a-z][a-z0-9_]*)_c[0-9]+$")
RE_MEMORY = re.compile(r"^mem_ch[1-5]_[a-z0-9_]+$")
RE_NPC = re.compile(r"^npc_[a-z_]+$")


def load_json(path, errors):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as exc:
        errors.append("JSON 파싱 실패: %s" % exc)
        return None


# --- 폴백 검증 (jsonschema 부재 시) -------------------------------------------

def check_int(obj, key, errors, minimum=None, maximum=None, where=""):
    v = obj.get(key)
    if not isinstance(v, int) or isinstance(v, bool):
        errors.append("%s%s: 정수여야 함" % (where, key))
        return
    if minimum is not None and v < minimum:
        errors.append("%s%s: %d < 최소 %d" % (where, key, v, minimum))
    if maximum is not None and v > maximum:
        errors.append("%s%s: %d > 최대 %d" % (where, key, v, maximum))


def check_condition(cond, errors, where):
    if not isinstance(cond, dict):
        errors.append(where + ": 조건은 객체여야 함")
        return
    keys = set(cond)
    if keys == {"stat", "op", "value"}:
        if cond["stat"] not in STAT_ENUM:
            errors.append("%s: stat enum 위반 (%r)" % (where, cond["stat"]))
        if cond["op"] not in OP_ENUM:
            errors.append("%s: op enum 위반 (%r)" % (where, cond["op"]))
        check_int(cond, "value", errors, where=where + ".")
    elif keys == {"memory", "exists"}:
        if not isinstance(cond["memory"], str) or not RE_MEMORY.match(cond["memory"]):
            errors.append("%s: memory 패턴 위반 (%r)" % (where, cond.get("memory")))
        if not isinstance(cond["exists"], bool):
            errors.append(where + ": exists는 boolean이어야 함")
    elif keys == {"rel", "op", "value"}:
        if not isinstance(cond["rel"], str) or not RE_NPC.match(cond["rel"]):
            errors.append("%s: rel 패턴 위반 (%r)" % (where, cond.get("rel")))
        if cond["op"] not in OP_ENUM:
            errors.append("%s: op enum 위반 (%r)" % (where, cond["op"]))
        check_int(cond, "value", errors, 0, 100, where + ".")
    else:
        errors.append("%s: 허용되지 않는 조건 형식 %s" % (where, sorted(keys)))


def check_effects(eff, errors, where):
    if not isinstance(eff, dict):
        errors.append(where + ": effects는 객체여야 함")
        return
    allowed = STAT_EFFECT_KEYS + TRAIT_KEYS + ["money", "rel"]
    for k in eff:
        if k not in allowed:
            errors.append("%s: 허용되지 않는 effects 키 %r" % (where, k))
    for k in STAT_EFFECT_KEYS:
        if k in eff:
            check_int(eff, k, errors, -20, 20, where + ".")
    for k in TRAIT_KEYS:
        if k in eff:
            check_int(eff, k, errors, -3, 3, where + ".")
    if "money" in eff:
        check_int(eff, "money", errors, where=where + ".")
    if "rel" in eff:
        rel = eff["rel"]
        if not isinstance(rel, dict):
            errors.append(where + ".rel: 객체여야 함")
        else:
            for npc, v in rel.items():
                if not RE_NPC.match(npc):
                    errors.append("%s.rel: npc 키 패턴 위반 (%r)" % (where, npc))
                if not isinstance(v, int) or isinstance(v, bool) or not -10 <= v <= 10:
                    errors.append("%s.rel.%s: -10~10 정수여야 함" % (where, npc))


def check_choice(choice, errors, where):
    if not isinstance(choice, dict):
        errors.append(where + ": choice는 객체여야 함")
        return
    for req in ("choice_id", "text_kr", "effects"):
        if req not in choice:
            errors.append("%s: 필수 필드 %r 누락" % (where, req))
    allowed = {"choice_id", "text_kr", "requires", "effects", "memory_tag"}
    for k in choice:
        if k not in allowed:
            errors.append("%s: 허용되지 않는 키 %r" % (where, k))
    cid = choice.get("choice_id")
    if not isinstance(cid, str) or not RE_CHOICE_ID.match(cid):
        errors.append("%s: choice_id 패턴 위반 (%r)" % (where, cid))
    text = choice.get("text_kr")
    if not isinstance(text, str) or not 1 <= len(text) <= 60:
        errors.append("%s: text_kr 길이(1~60) 위반" % where)
    if "requires" in choice:
        req = choice["requires"]
        if not isinstance(req, dict):
            errors.append(where + ".requires: 객체여야 함")
        else:
            for k in req:
                if k not in ("mind_min", "stamina_min", "money_min"):
                    errors.append("%s.requires: 허용되지 않는 키 %r" % (where, k))
            for k in ("mind_min", "stamina_min"):
                if k in req:
                    check_int(req, k, errors, 0, 100, where + ".requires.")
            if "money_min" in req:
                check_int(req, "money_min", errors, 0, None, where + ".requires.")
    if "effects" in choice:
        check_effects(choice["effects"], errors, where + ".effects")
    if "memory_tag" in choice:
        mt = choice["memory_tag"]
        if not isinstance(mt, str) or not RE_MEMORY.match(mt):
            errors.append("%s: memory_tag 패턴 위반 (%r)" % (where, mt))


def validate_stdlib(data, errors):
    """13_02 스키마와 등가인 표준 라이브러리 검사."""
    required = ["schema_version", "event_id", "chapter", "title_kr",
                "emotion_tags", "trigger", "priority", "scenes", "choices",
                "once", "cooldown_days"]
    for req in required:
        if req not in data:
            errors.append("필수 필드 %r 누락" % req)
    for k in data:
        if k not in required:
            errors.append("허용되지 않는 루트 키 %r" % k)

    sv = data.get("schema_version")
    if not isinstance(sv, str) or not RE_SCHEMA_VERSION.match(sv):
        errors.append("schema_version 패턴 위반 (%r)" % sv)
    eid = data.get("event_id")
    if not isinstance(eid, str) or not RE_EVENT_ID.match(eid):
        errors.append("event_id 패턴 위반 (%r)" % eid)
    check_int(data, "chapter", errors, 1, 5)
    title = data.get("title_kr")
    if not isinstance(title, str) or not 1 <= len(title) <= 40:
        errors.append("title_kr 길이(1~40) 위반")

    tags = data.get("emotion_tags")
    if not isinstance(tags, list) or len(tags) < 1:
        errors.append("emotion_tags: 최소 1개 배열이어야 함")
    else:
        if len(set(map(str, tags))) != len(tags):
            errors.append("emotion_tags: 중복 금지")
        for t in tags:
            if t not in EMOTION_ENUM:
                errors.append("emotion_tags: enum 위반 (%r)" % t)

    trig = data.get("trigger")
    if not isinstance(trig, dict):
        errors.append("trigger: 객체여야 함")
    else:
        for req in ("type", "conditions"):
            if req not in trig:
                errors.append("trigger: 필수 필드 %r 누락" % req)
        for k in trig:
            if k not in ("type", "conditions", "weight"):
                errors.append("trigger: 허용되지 않는 키 %r" % k)
        if trig.get("type") not in TRIGGER_TYPES:
            errors.append("trigger.type enum 위반 (%r)" % trig.get("type"))
        conds = trig.get("conditions")
        if not isinstance(conds, list):
            errors.append("trigger.conditions: 배열이어야 함")
        else:
            for i, c in enumerate(conds):
                check_condition(c, errors, "trigger.conditions[%d]" % i)
        if "weight" in trig:
            check_int(trig, "weight", errors, 1, 100, "trigger.")

    check_int(data, "priority", errors, 0, 100)

    scenes = data.get("scenes")
    if not isinstance(scenes, list):
        errors.append("scenes: 배열이어야 함")
    else:
        for i, s in enumerate(scenes):
            if not isinstance(s, str) or not RE_SCENE.match(s):
                errors.append("scenes[%d]: 패턴 위반 (%r)" % (i, s))

    choices = data.get("choices")
    if not isinstance(choices, list) or not 1 <= len(choices) <= 4:
        errors.append("choices: 1~4개 배열이어야 함")
    else:
        for i, c in enumerate(choices):
            check_choice(c, errors, "choices[%d]" % i)

    if not isinstance(data.get("once"), bool):
        errors.append("once: boolean이어야 함")
    check_int(data, "cooldown_days", errors, 0, None)


# --- 스키마 외 추가 린트 ------------------------------------------------------

def lint(data, path, errors):
    fname = os.path.basename(path)
    eid = data.get("event_id")
    if isinstance(eid, str) and fname != eid + ".json":
        errors.append("lint_filename_id: 파일명 %r != event_id %r + .json" % (fname, eid))
    chdir = os.path.basename(os.path.dirname(path))
    m = re.match(r"^ch([1-5])$", chdir)
    if m:
        n = int(m.group(1))
        if data.get("chapter") != n:
            errors.append("lint_chapter_dir: 디렉터리 %s != chapter %r" % (chdir, data.get("chapter")))
        if isinstance(eid, str) and not eid.startswith("ch%d_" % n):
            errors.append("lint_chapter_dir: event_id 접두 불일치 (%r)" % eid)
    for i, c in enumerate(data.get("choices") or []):
        if isinstance(c, dict) and "memory_tag" not in c:
            errors.append("lint_memory_tag: choices[%d]에 memory_tag 없음 (07_02)" % i)
    trig = data.get("trigger")
    if isinstance(trig, dict) and "weight" in trig and trig.get("type") != "random":
        errors.append("lint_random_weight: weight는 type=random 전용")


# --- 메인 ---------------------------------------------------------------------

def main():
    try:
        import jsonschema
        with open(SCHEMA_PATH, encoding="utf-8") as f:
            schema = json.load(f)
        validator = jsonschema.Draft7Validator(schema)
        mode = "jsonschema draft-07"
    except ImportError:
        validator = None
        mode = "stdlib fallback"

    targets = []
    for root, _dirs, files in os.walk(EVENTS_DIR):
        for fname in sorted(files):
            if fname.endswith(".json"):
                targets.append(os.path.join(root, fname))
    targets.sort()

    if not targets:
        print("검증 대상 없음: %s" % EVENTS_DIR)
        return 1

    failed = 0
    for path in targets:
        errors = []
        data = load_json(path, errors)
        if data is not None:
            if validator is not None:
                for err in sorted(validator.iter_errors(data), key=str):
                    loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
                    errors.append("%s: %s" % (loc, err.message))
            else:
                validate_stdlib(data, errors)
            lint(data, path, errors)
        rel = os.path.relpath(path, DATA_DIR)
        if errors:
            failed += 1
            print("[FAIL] %s" % rel)
            for e in errors:
                print("       - %s" % e)
        else:
            print("[PASS] %s" % rel)

    print("---")
    print("검증기: %s / 전체 %d, 통과 %d, 실패 %d"
          % (mode, len(targets), len(targets) - failed, failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
