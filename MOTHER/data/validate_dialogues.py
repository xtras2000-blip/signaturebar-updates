#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MOTHER 대사 씬 JSON 검증 스크립트.

data/dialogues/ch{n}/*.json 전체를 schemas/dialogue.schema.json(13_03 정본에서
추출)으로 검증한다. jsonschema(draft-07)가 있으면 그것을 쓰고, 없으면 표준
라이브러리만으로 필수 필드·패턴·enum을 직접 검사한다(폴백).

스키마 외 추가 린트(13_03 §4):
  - lint_filename_id   : 파일명 == scene_id + ".json"
  - lint_chapter_dir   : 디렉터리 ch{n} == scene_id 접두 == 참조 이벤트 chapter
  - lint_line_id       : line_id는 scene_id + "_l" 접두, 씬 내 유일
  - lint_rel_npc       : condition의 rel 대상은 14_02 명부의 npc_id만 허용
  - lint_ch1_child     : CH1 child 라인의 text_kr은 08_03 vocal_tag 사전 표기만 허용

참조 무결성 린트(13_01 §6, events ↔ dialogues):
  - events/ch{n}/*.json 의 scenes 배열이 가리키는 모든 scene_id에
    dialogues/ch{n}/{scene_id}.json 존재
  - 역으로 어떤 이벤트도 참조하지 않는 고아 씬 파일 없음
  - dialogues/ch{n}/ 디렉터리가 없는 챕터(대사 미제작)는 스킵하고 알린다.
    "_"로 시작하는 파일(예: _scene_map.json)은 씬 파일로 취급하지 않는다.

사용법: python3 MOTHER/data/validate_dialogues.py
종료 코드: 전 파일·전 참조 통과 0, 위반 1.
"""
import json
import os
import re
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
EVENTS_DIR = os.path.join(DATA_DIR, "events")
DIALOGUES_DIR = os.path.join(DATA_DIR, "dialogues")
SCHEMA_PATH = os.path.join(DATA_DIR, "schemas", "dialogue.schema.json")

RE_SCHEMA_VERSION = re.compile(r"^[0-9]+\.[0-9]+$")
RE_SCENE_ID = re.compile(r"^ch([1-5])_sc_[0-9]{3}$")
RE_LINE_ID = re.compile(r"^ch[1-5]_sc_[0-9]{3}_l[0-9]{2}$")
RE_MEMORY = re.compile(r"^mem_ch[1-5]_[a-z0-9_]+$")
RE_NPC = re.compile(r"^npc_[a-z_]+$")

SPEAKER_FIXED = ["player", "child", "system"]
EMOTION_ENUM = ["neutral", "soft", "warm", "tired", "tearful", "bright", "firm", "hesitant"]
STAT_ENUM = [
    "attachment", "child_condition", "stamina", "mind", "money",
    "husband_support", "confidence", "empathy", "independence",
    "expressiveness", "day_counter", "chapter",
]
OP_ENUM = ["lt", "lte", "gt", "gte", "eq", "neq"]
CTX_ENUM = ["time_block", "holiday", "preset", "seed"]

# 14_02 NPC 명부 — condition의 rel 대상 검증용 (13_03 §4-3)
NPC_ROSTER = ["npc_husband", "npc_grandma", "npc_daycare_teacher", "npc_cohort_sunny"]

# 08_03 §2 CH1 vocal_tag 사전 — CH1 child 라인 text_kr 허용 표기 (13_03 §4-4)
CH1_VOCAL_TAGS = [
    "cry_hunger", "cry_sleepy", "cry_discomfort", "cry_pain", "cry_unknown",
    "babble_soft", "babble_call",
]


def load_json(path, errors):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as exc:
        errors.append("JSON 파싱 실패: %s" % exc)
        return None


# --- 폴백 검증 (jsonschema 부재 시) -------------------------------------------

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
        if not isinstance(cond["value"], int) or isinstance(cond["value"], bool):
            errors.append(where + ".value: 정수여야 함")
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
        v = cond["value"]
        if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 100:
            errors.append(where + ".value: 0~100 정수여야 함")
    elif keys == {"ctx", "eq"}:
        if cond["ctx"] not in CTX_ENUM:
            errors.append("%s: ctx enum 위반 (%r)" % (where, cond["ctx"]))
        if not isinstance(cond["eq"], str):
            errors.append(where + ".eq: 문자열이어야 함")
    else:
        errors.append("%s: 허용되지 않는 조건 형식 %s" % (where, sorted(keys)))


def check_line(line, errors, where):
    if not isinstance(line, dict):
        errors.append(where + ": line은 객체여야 함")
        return
    for req in ("line_id", "speaker", "text_kr"):
        if req not in line:
            errors.append("%s: 필수 필드 %r 누락" % (where, req))
    allowed = {"line_id", "speaker", "text_kr", "condition", "emotion"}
    for k in line:
        if k not in allowed:
            errors.append("%s: 허용되지 않는 키 %r" % (where, k))
    lid = line.get("line_id")
    if not isinstance(lid, str) or not RE_LINE_ID.match(lid):
        errors.append("%s: line_id 패턴 위반 (%r)" % (where, lid))
    spk = line.get("speaker")
    if not (spk in SPEAKER_FIXED or (isinstance(spk, str) and RE_NPC.match(spk))):
        errors.append("%s: speaker 위반 (%r)" % (where, spk))
    text = line.get("text_kr")
    if not isinstance(text, str) or not 1 <= len(text) <= 120:
        errors.append("%s: text_kr 길이(1~120) 위반" % where)
    if "condition" in line:
        cond = line["condition"]
        if isinstance(cond, list):
            if not cond:
                errors.append(where + ".condition: 빈 배열 금지")
            for i, c in enumerate(cond):
                check_condition(c, errors, "%s.condition[%d]" % (where, i))
        else:
            check_condition(cond, errors, where + ".condition")
    if "emotion" in line and line["emotion"] not in EMOTION_ENUM:
        errors.append("%s: emotion enum 위반 (%r)" % (where, line.get("emotion")))


def validate_stdlib(data, errors):
    """13_03 스키마와 등가인 표준 라이브러리 검사."""
    required = ["schema_version", "scene_id", "lines"]
    for req in required:
        if req not in data:
            errors.append("필수 필드 %r 누락" % req)
    for k in data:
        if k not in required:
            errors.append("허용되지 않는 루트 키 %r" % k)
    sv = data.get("schema_version")
    if not isinstance(sv, str) or not RE_SCHEMA_VERSION.match(sv):
        errors.append("schema_version 패턴 위반 (%r)" % sv)
    sid = data.get("scene_id")
    if not isinstance(sid, str) or not RE_SCENE_ID.match(sid):
        errors.append("scene_id 패턴 위반 (%r)" % sid)
    lines = data.get("lines")
    if not isinstance(lines, list) or len(lines) < 1:
        errors.append("lines: 최소 1개 배열이어야 함")
    else:
        for i, line in enumerate(lines):
            check_line(line, errors, "lines[%d]" % i)


# --- 스키마 외 추가 린트 (13_03 §4) -------------------------------------------

def iter_conditions(line):
    cond = line.get("condition")
    if isinstance(cond, dict):
        yield cond
    elif isinstance(cond, list):
        for c in cond:
            if isinstance(c, dict):
                yield c


def lint(data, path, errors):
    fname = os.path.basename(path)
    sid = data.get("scene_id")
    if isinstance(sid, str) and fname != sid + ".json":
        errors.append("lint_filename_id: 파일명 %r != scene_id %r + .json" % (fname, sid))
    chdir = os.path.basename(os.path.dirname(path))
    m = re.match(r"^ch([1-5])$", chdir)
    chapter = int(m.group(1)) if m else None
    if chapter is not None and isinstance(sid, str) and not sid.startswith("ch%d_" % chapter):
        errors.append("lint_chapter_dir: 디렉터리 %s != scene_id 접두 (%r)" % (chdir, sid))

    seen_ids = set()
    for i, line in enumerate(data.get("lines") or []):
        if not isinstance(line, dict):
            continue
        where = "lines[%d]" % i
        lid = line.get("line_id")
        if isinstance(lid, str):
            if isinstance(sid, str) and not lid.startswith(sid + "_l"):
                errors.append("lint_line_id: %s line_id %r가 scene_id 접두 불일치" % (where, lid))
            if lid in seen_ids:
                errors.append("lint_line_id: %s line_id %r 중복" % (where, lid))
            seen_ids.add(lid)
        for cond in iter_conditions(line):
            if set(cond) == {"rel", "op", "value"} and cond.get("rel") not in NPC_ROSTER:
                errors.append("lint_rel_npc: %s rel %r는 14_02 명부에 없음" % (where, cond.get("rel")))
        if chapter == 1 and line.get("speaker") == "child":
            if line.get("text_kr") not in CH1_VOCAL_TAGS:
                errors.append("lint_ch1_child: %s CH1 child text_kr은 08_03 vocal_tag "
                              "사전 표기만 허용 (%r)" % (where, line.get("text_kr")))


# --- 참조 무결성 (events ↔ dialogues) -----------------------------------------

def check_ref_integrity(problems):
    """events/ch{n}의 scenes 참조 ↔ dialogues/ch{n} 파일 존재를 양방향 검사.

    dialogues/ch{n}/ 디렉터리가 없는 챕터는 대사 미제작으로 간주하고 스킵한다.
    반환: 검사한 챕터 목록, 스킵한 챕터 목록.
    """
    checked, skipped = [], []
    if not os.path.isdir(EVENTS_DIR):
        problems.append("events 디렉터리 없음: %s" % EVENTS_DIR)
        return checked, skipped
    for chdir in sorted(os.listdir(EVENTS_DIR)):
        ev_dir = os.path.join(EVENTS_DIR, chdir)
        if not (os.path.isdir(ev_dir) and re.match(r"^ch[1-5]$", chdir)):
            continue
        dlg_dir = os.path.join(DIALOGUES_DIR, chdir)
        if not os.path.isdir(dlg_dir):
            skipped.append(chdir)
            continue
        checked.append(chdir)

        referenced = {}  # scene_id -> [event_id, ...]
        for fname in sorted(os.listdir(ev_dir)):
            if not fname.endswith(".json"):
                continue
            errors = []
            data = load_json(os.path.join(ev_dir, fname), errors)
            if data is None:
                problems.append("events/%s/%s: %s" % (chdir, fname, "; ".join(errors)))
                continue
            eid = data.get("event_id", fname)
            for sid in data.get("scenes") or []:
                if isinstance(sid, str):
                    referenced.setdefault(sid, []).append(eid)

        existing = set()
        for fname in sorted(os.listdir(dlg_dir)):
            if fname.endswith(".json") and not fname.startswith("_"):
                existing.add(fname[:-len(".json")])

        for sid in sorted(referenced):
            if sid not in existing:
                problems.append("참조 무결성: %s 씬 파일 없음 (dialogues/%s/%s.json, 참조: %s)"
                                % (sid, chdir, sid, ", ".join(referenced[sid])))
        for sid in sorted(existing - set(referenced)):
            problems.append("참조 무결성: 고아 씬 파일 dialogues/%s/%s.json "
                            "(어떤 이벤트 scenes에도 미참조)" % (chdir, sid))
    return checked, skipped


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
    if os.path.isdir(DIALOGUES_DIR):
        for root, _dirs, files in os.walk(DIALOGUES_DIR):
            for fname in sorted(files):
                if fname.endswith(".json") and not fname.startswith("_"):
                    targets.append(os.path.join(root, fname))
    targets.sort()

    if not targets:
        print("검증 대상 없음: %s" % DIALOGUES_DIR)
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
    ref_problems = []
    checked, skipped = check_ref_integrity(ref_problems)
    for ch in skipped:
        print("[SKIP] events/%s: dialogues/%s 미제작 챕터 — 참조 무결성 스킵" % (ch, ch))
    for ch in checked:
        print("[LINT] events/%s ↔ dialogues/%s 참조 무결성 검사" % (ch, ch))
    if ref_problems:
        for p in ref_problems:
            print("       - %s" % p)

    print("---")
    print("검증기: %s / 씬 파일 %d, 통과 %d, 실패 %d / 참조 무결성 위반 %d (검사 %s, 스킵 %s)"
          % (mode, len(targets), len(targets) - failed, failed, len(ref_problems),
             ", ".join(checked) or "-", ", ".join(skipped) or "-"))
    return 1 if failed or ref_problems else 0


if __name__ == "__main__":
    sys.exit(main())
