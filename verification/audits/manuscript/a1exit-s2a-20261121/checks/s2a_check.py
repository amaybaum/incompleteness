#!/usr/bin/env python3
"""S2-A edit check (stdlib only, deterministic). Run from the repository root:
    python3 -I verification/audits/manuscript/a1exit-s2a-20261121/checks/s2a_check.py [--pre | --apply]
--pre   : exit 0 iff every old string occurs exactly once in its file and in its mirror (base state).
--apply : the --pre check, then apply every edit (old -> new) to the file and its mirror.
default : exit 0 iff every new string occurs exactly once in its file and in its mirror, and no old
          string occurs outside its own new string.
The verdict is the exit status; printed lines are diagnostics.
"""
import json
import sys

D = "verification/audits/manuscript/a1exit-s2a-20261121/checks/"
EDITS = json.load(open(D + "s2a_edits.json", encoding="utf-8"))


def targets(e):
    return [e["file"]] + ([e["mirror"][0]] if "mirror" in e else [])


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--post"
    ok = True
    for e in EDITS:
        for f in targets(e):
            txt = open(f, encoding="utf-8").read()
            if mode in ("--pre", "--apply"):
                c = txt.count(e["old"])
                good = c == 1
                print(f"{e['id']:12s} {f}: old x{c} {'ok' if good else 'FAIL'}")
            else:
                cn = txt.count(e["new"])
                co = txt.count(e["old"]) - (cn if e["old"] in e["new"] else 0)
                good = cn == 1 and co == 0
                print(f"{e['id']:12s} {f}: new x{cn}, stray old x{co} {'ok' if good else 'FAIL'}")
            ok = ok and good
    if mode == "--apply" and ok:
        for e in EDITS:
            for f in targets(e):
                txt = open(f, encoding="utf-8").read()
                with open(f, "w", encoding="utf-8") as fh:
                    fh.write(txt.replace(e["old"], e["new"], 1))
        print("applied")
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
