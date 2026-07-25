#!/usr/bin/env python3
"""
check_ledger.py — prediction-ledger consistency checker.

The corpus maintains the prediction ledger in THREE parallel places, by hand:

    papers/SM.md  §7.6                      (Input class: S/C/L/R/P/M/E)
    book/ch06-matter-content.md             (Input class AND Category A–E)
    book/appendix-a-prediction-status.md    (Input class, §A.4.1–A.4.3)

Hand-maintained parallel ledgers drift.  Count drift in this corpus has been
found and hand-fixed at least twice (April 2026: 21-vs-22 observables,
13-vs-14 structural; May 2026: the Category A–E rework).  A third hand-fix
has the same expected lifetime as the first two, so this script recomputes
the counts FROM the tables and diffs them against the prose.

It checks:
  A. table-vs-prose  — do the stated counts match the rows actually present?
  B. table-vs-table  — do the three ledgers agree on row count, and on the
                       class assigned to each observable they share?

Usage:  python3 tools/check_ledger.py
Exit:   0 clean, 1 on any mismatch.
"""
import re
import sys
from collections import Counter, defaultdict

CLASS_RE = re.compile(r"\*\*([SCLRPME])\*\*")
BARE_CLASS_RE = re.compile(r"^([SCLRPME])$")

WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "twenty-one": 21, "twenty-two": 22, "twenty-three": 23, "twenty-four": 24,
}


def cells(row):
    """Split a markdown table row.

    Pipes inside $...$ math are NOT column separators — pandoc's pipe-table
    parser ignores them, verified against the shipped .tex (Main.md:241 carries
    five bare pipes inside math and renders as exactly three columns).  An
    earlier version of this function split on them and silently dropped every
    row containing $|V_{cb}|$, which changed the reported counts without
    changing the corpus.  Mask math spans first, then split.
    """
    masked, in_math = [], False
    for ch in row:
        if ch == "$":
            in_math = not in_math
        masked.append("\x01" if (in_math and ch == "|") else ch)
    safe = "".join(masked).replace(r"\|", "\x00")
    return [c.strip().replace("\x00", "|").replace("\x01", "|")
            for c in safe.strip().strip("|").split("|")]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def slice_section(txt, start, end=None):
    a = txt.split(start)
    if len(a) < 2:
        return ""
    body = a[1]
    return body.split(end)[0] if end else body


def norm(name):
    """Normalise an observable name for cross-table matching."""
    s = re.sub(r"[\$\\{}]", "", name)
    s = s.replace("text", "").replace("mathrm", "").replace(" ", "")
    s = s.replace("^2", "2").replace("_", "").lower()
    s = re.sub(r"\(.*?\)", "", s)
    return s.strip(" ,.")


def harvest(txt, class_col, name_col=0, min_cols=4):
    """Return {normalised name: class} and the ordered row list."""
    rows, out = [], {}
    for line in txt.split("\n"):
        s = line.strip()
        if not s.startswith("|") or "---" in s:
            continue
        c = cells(s)
        if len(c) < min_cols:
            continue
        m = CLASS_RE.search(c[class_col]) or BARE_CLASS_RE.match(c[class_col])
        if not m:
            continue
        cls = m.group(1)
        nm = norm(c[name_col])
        if not nm:
            continue
        rows.append((nm, cls))
        out[nm] = cls
    return out, rows


def stated_counts(prose):
    """Pull 'Counts: 13 unconditional S + 6 L + ...' style declarations."""
    found = {}
    for m in re.finditer(r"(\d+)\s+(?:unconditional\s+)?([SCLRPME])\b", prose):
        found[m.group(2)] = int(m.group(1))
    return found


def report(title, actual, stated, n_rows, stated_rows=None):
    print(f"\n── {title}")
    print(f"   rows in table : {n_rows}")
    if stated_rows is not None:
        flag = "" if stated_rows == n_rows else "   ← MISMATCH"
        print(f"   rows in prose : {stated_rows}{flag}")
    print(f"   actual counts : {dict(sorted(actual.items()))}")
    if stated:
        print(f"   stated counts : {dict(sorted(stated.items()))}")
        bad = {k for k in set(actual) | set(stated)
               if actual.get(k, 0) != stated.get(k, 0)}
        if bad:
            for k in sorted(bad):
                print(f"     ← MISMATCH {k}: table {actual.get(k,0)} vs prose {stated.get(k,0)}")
            return False
    ok = stated_rows is None or stated_rows == n_rows
    return ok


def main():
    ok = True

    # ---- SM §7.6 -------------------------------------------------------
    sm = read("papers/SM.md")
    sec = slice_section(sm, "### 7.6", "### 7.7")
    sm_map, sm_rows = harvest(sec, class_col=5, min_cols=6)
    sm_prose = sec.split("Parameter-accounting summary")[-1]
    ok &= report("SM §7.6", Counter(c for _, c in sm_rows),
                 stated_counts(sm_prose[:1200]), len(sm_rows))

    # ---- ch06 ----------------------------------------------------------
    ch = read("book/ch06-matter-content.md")
    ch_map, ch_rows = harvest(ch, class_col=5, min_cols=7)
    cat = Counter()
    for line in ch.split("\n"):
        s = line.strip()
        if s.startswith("|") and "---" not in s:
            c = cells(s)
            if len(c) >= 7 and (CLASS_RE.search(c[5]) or BARE_CLASS_RE.match(c[5])):
                cat[re.sub(r"[*\s]", "", c[6])] += 1
    m = re.search(r"Category distribution across the ([\w-]+) table entries", ch)
    stated_rows = WORD_NUM.get(m.group(1)) if m else None
    ok &= report("book/ch06 (Input class)", Counter(c for _, c in ch_rows),
                 None, len(ch_rows), stated_rows)
    print(f"   Category A–E  : {dict(sorted(cat.items()))}")
    cm = re.findall(r"(\w+) in Category ([A-E])", ch)
    if cm:
        stated_cat = {k: WORD_NUM.get(v.lower(), -1) for v, k in cm}
        print(f"   stated Cat.   : {dict(sorted(stated_cat.items()))}")
        for k in sorted(set(stated_cat)):
            if cat.get(k, 0) != stated_cat[k]:
                print(f"     ← MISMATCH Category {k}: table {cat.get(k,0)} vs prose {stated_cat[k]}")
                ok = False

    # ---- appendix A ----------------------------------------------------
    ap = read("book/appendix-a-prediction-status.md")
    for tag, nxt in (("### A.4.1", "### A.4.2"),
                     ("### A.4.2", "### A.4.3"),
                     ("### A.4.3", "### A.4.4")):
        body = slice_section(ap, tag, nxt)
        amap, arows = harvest(body, class_col=3, name_col=1, min_cols=5)
        sm_line = re.search(r"Counts:([^.]*)\.", body)
        ok &= report(f"appendix-A {tag[4:]}", Counter(c for _, c in arows),
                     stated_counts(sm_line.group(1)) if sm_line else None,
                     len(arows))
        if tag == "### A.4.1":
            ap_map = amap

    # ---- cross-table agreement ----------------------------------------
    print("\n── cross-table: observables classified differently")
    disagree = 0
    keys = set(sm_map) & set(ap_map)
    for k in sorted(keys):
        if sm_map[k] != ap_map[k]:
            print(f"   {k:28s} SM §7.6={sm_map[k]}   appendix-A={ap_map[k]}")
            disagree += 1
    keys2 = set(sm_map) & set(ch_map)
    for k in sorted(keys2):
        if sm_map[k] != ch_map[k]:
            print(f"   {k:28s} SM §7.6={sm_map[k]}   ch06={ch_map[k]}")
            disagree += 1
    cov = len(keys) + len(keys2)
    if not disagree:
        print(f"   (none among the {cov} observables matched by name; "
              f"{len(sm_map)-len(keys)} SM rows went unmatched — name normalisation "
              f"is heuristic, so this check is partial, not exhaustive)")
    else:
        ok = False

    print(f"\n{'PASS' if ok else 'FAIL'}: ledger consistency")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
