#!/usr/bin/env python3
"""
check_xrefs.py — cross-reference validator for the OI corpus.

Catches the two failure modes that have actually occurred:

  (1) LINE-NUMBER REFS.  Working-notes shorthand ("§125" meaning "line 125
      of SM.md") leaking into manuscript prose.  These are unresolvable for
      a reader — the papers are built with section numbering OFF, so no
      section number is rendered at all — and they are *unstable*, because
      §A.27 mandates appending dated status notes in place, which shifts
      every line number below the insertion point.  Observed drift: refs
      written as "§127" had already slipped two lines off their intended
      target before this checker existed.

  (2) DANGLING TARGETS.  "SM §9.4" where SM has no §9.4.

Usage:  python3 tools/check_xrefs.py [--warn-self]
Exit:   0 clean, 1 if any error-level finding.
"""
import re
import sys
import glob
import os
from collections import defaultdict

PAPERS_DIR = "papers"
BOOK_DIR = "book"

# The threshold for "this bare §N is a line number, not a section" is derived
# from the corpus itself rather than hard-coded.  A fixed guess is wrong:
# Methodology.md legitimately numbers sections up to §27, and an early version
# of this script flagged all twenty of its §22–§26 references as false
# positives.  The rule below is self-calibrating and cannot make that mistake.
def max_section(idx):
    """Highest top-level section number appearing anywhere in the corpus."""
    tops = [int(s.split(".")[0]) for secs in idx.values() for s in secs]
    return max(tops) if tops else 0

HEADING_RE = re.compile(r"^#{1,6}\s+\**((?:\d+)(?:\.\d+)*)\.?\s")
# "[18, §7.3]" is a numeric-citation form, not a section cross-reference.
BRACKET_CITE_RE = re.compile(r"\[\s*\d+\s*,\s*§")


def section_index(path):
    """Set of section numbers defined by headings in a file."""
    out = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = HEADING_RE.match(line)
            if m:
                out.add(m.group(1))
    return out


def build_indices():
    idx = {}
    for p in sorted(glob.glob(os.path.join(PAPERS_DIR, "*.md"))):
        idx[os.path.basename(p)[:-3]] = section_index(p)
    return idx


def corpus_files():
    return sorted(glob.glob(os.path.join(PAPERS_DIR, "*.md"))) + sorted(
        glob.glob(os.path.join(BOOK_DIR, "*.md"))
    )


def main(warn_self=False):
    idx = build_indices()
    ceiling = max_section(idx)
    names = sorted(idx, key=len, reverse=True)
    named_re = re.compile(
        r"\b(" + "|".join(names) + r")\b[^\]\n§]{0,20}?§\s?(\d+(?:\.\d+)*)"
    )
    bare_re = re.compile(r"§\s?(\d+(?:\.\d+)*)")

    errors = defaultdict(list)
    warnings = defaultdict(list)

    for f in corpus_files():
        own = os.path.basename(f)[:-3]
        with open(f, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if BRACKET_CITE_RE.search(line):
                    line = BRACKET_CITE_RE.sub("[CITE ", line)

                # (1) line-number-style refs, anywhere
                for m in bare_re.finditer(line):
                    sec = m.group(1)
                    if "." not in sec and int(sec) > ceiling:
                        errors["line-number ref"].append(
                            f"{f}:{ln}  §{sec}  (exceeds the corpus's highest section "
                            f"number, §{ceiling} — almost certainly a line number)"
                        )

                # (2) named cross-paper refs to non-existent sections
                for m in named_re.finditer(line):
                    tgt, sec = m.group(1), m.group(2)
                    if tgt in idx and idx[tgt] and sec not in idx[tgt]:
                        if "." in sec or int(sec) <= ceiling:
                            errors["dangling target"].append(
                                f"{f}:{ln}  {tgt} §{sec}  (no such section in {tgt}.md)"
                            )

                # (3) self-refs — noisy (papers cite each other without naming),
                #     so warn-only and opt-in.
                if warn_self and own in idx and idx[own]:
                    stripped = named_re.sub(" ", line)
                    for m in bare_re.finditer(stripped):
                        sec = m.group(1)
                        if sec not in idx[own] and (
                            "." in sec or int(sec) <= ceiling
                        ):
                            warnings["possible self-ref"].append(
                                f"{f}:{ln}  §{sec}  (not a section of {own}.md)"
                            )

    n_err = sum(len(v) for v in errors.values())
    for kind, items in errors.items():
        print(f"\nERROR — {kind}  ({len(items)})")
        for it in items:
            print("   ", it)
    for kind, items in warnings.items():
        print(f"\nwarning — {kind}  ({len(items)})")
        for it in items[:25]:
            print("   ", it)
        if len(items) > 25:
            print(f"    ... and {len(items) - 25} more")

    print(f"\n{'FAIL' if n_err else 'PASS'}: {n_err} error-level finding(s) "
          f"across {len(corpus_files())} files.")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main(warn_self="--warn-self" in sys.argv))
