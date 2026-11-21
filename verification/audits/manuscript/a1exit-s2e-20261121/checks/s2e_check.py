#!/usr/bin/env python3
"""A1-EXIT S2-E edit checker.

Modes:
  base     every old string occurs exactly once in its file (and once in FULL.md for a
           book edit), on the preregistered line of the file; no new string occurs.
  apply    perform the base check, then replace each old string by its new string in the
           file and, for a book edit, in FULL.md.
  applied  (default) every new string occurs exactly once in its file (and in FULL.md for a
           book edit); no old string survives except inside its own new string; each book
           line carrying an edit is byte-identical to its FULL.md counterpart. With
           s2e_amend1.json present, a base edit's expected new string carries its amendment
           (and is checked for uniqueness as above), and each amendment's old string does not
           occur in ch18 or FULL.md.
  apply-amend  check each amendment's old string occurs exactly once in ch18 and in FULL.md,
           then apply.
Exit status 0 on success, 1 on any failure.
"""
import json, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[".."] * 5))
FULL = "book/The-Incompleteness-of-Observation-FULL.md"
EDITS = json.load(open(os.path.join(os.path.dirname(__file__), "s2e_edits.json"), encoding="utf-8"))
_AM = os.path.join(os.path.dirname(__file__), "s2e_amend1.json")
AMEND = json.load(open(_AM, encoding="utf-8")) if os.path.exists(_AM) else []
# In `applied` mode a base edit's expected new string carries its amendment.
_BY_ID = {e["id"]: e for e in EDITS}
for a in AMEND:
    b = _BY_ID[a["amends"]]
    assert b["new"].count(a["old"]) == 1, a["id"]
    b["new_preregistered"] = b["new"]
    b["new"] = b["new"].replace(a["old"], a["new"])


def read(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def write(p, s):
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(s)


def targets(e):
    return [e["file"]] + ([FULL] if e["full_mirror"] else [])


def check_base():
    bad = 0
    for e in EDITS:
        for f in targets(e):
            t = read(f)
            n = t.count(e["old"])
            if n != 1:
                print(f"FAIL {e['id']} {f}: old occurs {n}x"); bad += 1
            if e["new"] in t:
                print(f"FAIL {e['id']} {f}: new already present"); bad += 1
        lines = read(e["file"]).split("\n")
        if e["old"] not in lines[e["line"] - 1]:
            print(f"FAIL {e['id']} {e['file']}: old not on line {e['line']}"); bad += 1
    return bad


def check_applied():
    bad = 0
    for e in EDITS:
        for f in targets(e):
            t = read(f)
            n = t.count(e["new"])
            if n != 1:
                print(f"FAIL {e['id']} {f}: new occurs {n}x"); bad += 1
            if t.replace(e["new"], "").count(e["old"]):
                print(f"FAIL {e['id']} {f}: old survives"); bad += 1
        if e["full_mirror"]:
            line = [l for l in read(e["file"]).split("\n") if e["new"] in l]
            full = [l for l in read(FULL).split("\n") if e["new"] in l]
            if len(line) != 1 or line != full:
                print(f"FAIL {e['id']}: book line and FULL line differ"); bad += 1
    return bad


def check_amend(applied):
    bad = 0
    for a in AMEND:
        for f in targets(a):
            t = read(f)
            # The amended full new string of the base edit is checked by check_applied; an
            # amendment's own new string may be a substring of other text (A1-R1a), so here
            # only the old string is counted.
            n = t.count(a["old"])
            if applied and n:
                print(f"FAIL {a['id']} {f}: old survives"); bad += 1
            if not applied and n != 1:
                print(f"FAIL {a['id']} {f}: old occurs {n}x"); bad += 1
    return bad


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "applied"
    if mode == "apply-amend":
        bad = check_amend(False)
        if bad:
            print(f"amendment base check: {bad} failure(s)"); return 1
        for a in AMEND:
            for f in targets(a):
                write(f, read(f).replace(a["old"], a["new"], 1))
        print(f"amendment applied ({len(AMEND)} edits)")
        return 0
    if mode in ("base", "apply") and AMEND:
        for e in EDITS:
            e["new"] = e.get("new_preregistered", e["new"])
    if mode in ("base", "apply"):
        bad = check_base()
        if bad:
            print(f"base check: {bad} failure(s)"); return 1
        print(f"base check PASS ({len(EDITS)} edits)")
        if mode == "apply":
            for e in EDITS:
                for f in targets(e):
                    write(f, read(f).replace(e["old"], e["new"], 1))
            print("applied")
        return 0
    bad = check_applied() + check_amend(True)
    print(f"applied check {'PASS' if not bad else 'FAIL'} ({len(EDITS)} edits, {len(AMEND)} amending, {bad} failure(s))")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
