#!/usr/bin/env python3
"""Text checks for the C14 correction packages (packages.json). Read-only.

For each package, at a given commit (default HEAD), it checks:
  (a) the old text occurs exactly once in its file, or is already applied (the new text occurs
      exactly once and the old text does not);
  (b) for a book chapter with mirror_in_FULL, the same holds in FULL.md;
  (c) the old text lies on no line that #1477's ledger (edits.json at 55544cc3) edits, and
      overlaps no ledger edit's old text;
  (d) the package names a canonical source and its dependencies.
Assumption about the ledger's FULL.md entries, checked and failed closed: every ledger edit whose
file is FULL.md is a mirror entry whose `site` names its chapter line (site == mirror_of), so a
chapter-line check in (c) also covers the FULL.md mirror. At 55544cc3 this holds for all 77
FULL.md entries. A FULL.md-only ledger edit would not be covered, so the checker stops if one exists.
It also reports guard pins: any guard, census or check source containing a 30-character span of
an old text. Pins are reported, not failed: the owning check must be updated with the package.

Usage (from the repository root):  python3 -I <this file> [commit]
Exit 0 only if (a)-(d) hold for every package (READY).
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FULL = "book/The-Incompleteness-of-Observation-FULL.md"
LEDGER = ("55544cc3", "verification/audits/foundations/a1exit-deletion-20261121/edits.json")
PIN_SOURCES = ("tools/", "papers/oi_lattice_code/", "verification/lean/", "verification/audit-census.json",
               "verification/lean-manuscript-census.json")
SPAN = 30


def show(commit, path):
    r = subprocess.run(["git", "show", f"{commit}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def ls(commit):
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", commit], capture_output=True, text=True, check=True).stdout
    return out.split("\n")


def state(text, old, new):
    if text is None:
        return "MISSING-FILE"
    o, n = text.count(old), text.count(new)
    if o == 1:
        return "ok"
    if o == 0 and n == 1:
        return "applied"
    return f"old x{o}"


def main():
    commit = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    pk = json.load(open(os.path.join(HERE, "packages.json"), encoding="utf8"))["packages"]
    led = json.loads(show(*LEDGER))["edits"]
    full_entries = [e for e in led if e["file"] == FULL]
    if any(e.get("mirror_of") != e["site"] for e in full_entries):
        sys.exit("ledger has a FULL.md entry that is not a chapter mirror; check (c) would not cover it")
    led_lines = {(e["site"].rsplit(":", 1)[0], int(e["site"].rsplit(":", 1)[1])) for e in led}
    led_old = [(e["site"].rsplit(":", 1)[0], e.get("old") or "") for e in led]
    pin_files = [p for p in ls(commit) if p.startswith(PIN_SOURCES) and p.endswith((".py", ".json", ".lean"))]
    pin_text = {p: show(commit, p) or "" for p in pin_files}
    cache = {}
    bad = 0
    for p in pk:
        f = p["file"]
        cache.setdefault(f, show(commit, f))
        txt = cache[f]
        a = state(txt, p["old"], p["new"])
        b = "-"
        if p["mirror_in_FULL"]:
            cache.setdefault(FULL, show(commit, FULL))
            b = state(cache[FULL], p["old"], p["new"])
        c = "ok"
        if txt is not None and p["old"] in txt:
            start = txt.index(p["old"])
            l0 = txt.count("\n", 0, start) + 1
            l1 = l0 + p["old"].count("\n")
            if any((f, n) in led_lines for n in range(l0, l1 + 1)):
                c = f"LEDGER-LINE {l0}"
            elif any(lf == f and lo and (lo in p["old"] or p["old"] in lo) for lf, lo in led_old):
                c = "LEDGER-OVERLAP"
        d = "ok" if p.get("canonical") and p.get("preserve") else "MISSING"
        pins = sorted({q for q, t in pin_text.items() if q != f and any(
            p["old"][i:i + SPAN] in t for i in range(0, max(1, len(p["old"]) - SPAN + 1), 5))})
        good = a in ("ok", "applied") and b in ("-", "ok", "applied") and c == "ok" and d == "ok"
        bad += not good
        print(f"{p['id']:<9} {f:<52} a={a:<8} b={b:<8} c={c:<14} d={d:<7} pins={','.join(pins) or '-'}")
    print(f"\n{len(pk)} packages; {bad} failing; verdict {'READY' if bad == 0 else 'PARTIAL'} at {commit}")
    sys.exit(0 if bad == 0 else 1)


if __name__ == "__main__":
    main()
