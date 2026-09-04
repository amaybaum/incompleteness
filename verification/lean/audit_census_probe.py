#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The audit census: makes an audit's NEGATIVE findings as reproducible as its positive ones.

An audit that reports only its hits cannot be checked. The clean axes -- "no manuscript assumes the
substratum is passively minimal", "nothing claims hidden memory follows automatically from coupling"
-- are exactly the claims a reader cannot verify from the audit note, and exactly the ones that
silently stop being true when someone adds a paragraph two rounds later.

verification/audit-census.json records, for every vocabulary an audit searched: the pattern, the
files and counts it hits, the disposition, and why. This probe re-runs each one over the scoped
corpus and fails on any drift -- a new hit in a file the manifest does not list, a changed count, a
repaired form that has gone missing from one of its parallel sources.

DRIFT IS NOT AUTOMATICALLY A DEFECT. The corpus moves, and a mismatch means the audit's disposition
has to be re-decided at that location, not that the text is wrong. The manifest's `on_drift` field
carries the rule: re-read, decide, and update `expect` in the same commit as the text change with
the reason in the commit message. Widening a pattern to make a mismatch disappear defeats the
instrument and is the one move this file exists to make expensive.

WHAT THIS PROBE IS NOT. Not a claim that the vocabularies exhaust the corpus: an audit's charter
fixes its patterns, and a different charter would find different things. Not a semantic check --
matching text is not the same as asserting it, so a manifest entry records a HUMAN disposition,
and the probe checks only that the text the disposition was formed against has not moved.
"""

import json
import os
import sys
import time
from glob import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MANIFEST = os.path.join(os.path.dirname(HERE), 'audit-census.json')

FAILURES = []


def check(label, ok, msg):
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}")
    if not ok:
        FAILURES.append(label)


def scoped_files(patterns):
    out = []
    for pat in patterns:
        out.extend(sorted(glob(os.path.join(ROOT, pat))))
    return out


def census(pattern, files):
    hits = {}
    for path in files:
        n = open(path, encoding='utf-8').read().count(pattern)
        if n:
            hits[os.path.relpath(path, ROOT)] = n
    return hits


def main():
    t0 = time.time()
    print("audit_census_probe: corpus audit census, positive and negative findings alike")
    print()

    man = json.load(open(MANIFEST, encoding='utf-8'))
    files = scoped_files(man['scope'])
    if not files:
        check('X0', False, f"no files matched the manifest scope {man['scope']}")
        return 1

    for audit in man['audits']:
        drift = []
        rows = []
        for v in audit['vocabularies']:
            got = census(v['pattern'], files)
            want = v['expect']
            if got != want:
                drift.append((v['id'], want, got))
            total = sum(got.values())
            rows.append(f"{v['id']} [{v['disposition']}] {total} hit(s)")
        n_clean = sum(1 for v in audit['vocabularies'] if v['disposition'] == 'clean')
        n_open = sum(1 for v in audit['vocabularies'] if v['disposition'] == 'finding-open')
        n_rep = sum(1 for v in audit['vocabularies'] if v['disposition'] == 'repaired')
        check(f"AUDIT-{audit['id']}", not drift,
              f"{audit['title']}: {len(audit['vocabularies'])} vocabularies re-run over "
              f"{len(files)} scoped files -- {n_clean} clean, {n_rep} repaired, {n_open} open. "
              f"Every recorded count reproduces exactly, so the audit's negative findings are "
              f"checkable rather than asserted. Charter: {audit['charter']}"
              + (f"  [DRIFT, re-decide the disposition at these locations and update the "
                 f"manifest deliberately: {drift}]" if drift else ""))
        for r in rows:
            print(f"          {r}")

    # the manifest must keep its own operating rule, since the failure mode is a lazy repair
    check('X1', 'on_drift' in man and 'Never widen a pattern' in man['on_drift'],
          "the manifest carries its drift rule: re-read the location, decide whether the "
          "disposition still holds, update `expect` in the same commit as the text change with the "
          "reason in the commit message, and never widen a pattern to make a mismatch go away")

    # every vocabulary must carry a reason -- a bare pattern with a count is not provenance
    missing = [v['id'] for a in man['audits'] for v in a['vocabularies']
               if not v.get('why') or not v.get('disposition')]
    check('X2', not missing,
          "every vocabulary carries a disposition and the reason it was given, so a later reader "
          "can tell a clean axis from an unexamined one"
          + (f"  [bare entries: {missing}]" if missing else ""))

    print()
    if FAILURES:
        print(f"audit_census_probe: FAILED -> {', '.join(FAILURES)}  [{time.time()-t0:.1f}s]")
        return 1
    print(f"audit_census_probe: ALL CHECKS PASS  [{time.time()-t0:.1f}s]")
    return 0


if __name__ == '__main__':
    sys.exit(main())
