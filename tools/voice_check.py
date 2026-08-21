#!/usr/bin/env python3
"""voice_check.py - does the manuscript narrate its own revision history?

AGENTS.md: "The document never narrates its own history. No 'formerly,' no
'is not listed,' no 'withdrawn from' in the manuscript's voice." Correction
rounds reintroduce this language faster than it can be caught by reading.

Exempt: AGENTS.md (states the rule) and papers/Complexity.md (its claims
ladder records withdrawn EMPIRICAL verdicts, which is honest reporting of a
failed analysis, not narration of the document's own edits).

Usage:  python3 voice_check.py [--root DIR]
Exit 1 if manuscript-voice history narration is present.
"""
import os, re, sys

EXEMPT = {'AGENTS.md', 'Complexity.md'}
PATTERNS = [
    (r'\bwithdraw(n|s|al)?\b',        "revision narration: 'withdrawn'"),
    (r'[Ee]arlier drafts?',           "revision narration: 'earlier draft'"),
    (r'\bformerly\b|\bFormer\b',      "revision narration: 'former(ly)'"),
    (r'\bnow (separates|states|says|reads)\b', "revision narration: 'now ...'"),
    (r'\bpreviously (said|stated|read|claimed)\b', "revision narration"),
    (r'\bwe (were|had) (wrong|mistaken)\b', "first-person revision narration"),
]

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    hits = 0
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith('.md') or f in EXEMPT:
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding='utf-8', errors='replace').read()
            for pat, why in PATTERNS:
                for m in re.finditer(pat, s):
                    ln = s.count('\n', 0, m.start()) + 1
                    frag = s[max(0, m.start()-60):m.start()+60].replace('\n', ' ')
                    print(f"  VOICE {p}:{ln}  {why}\n        ...{frag}...")
                    hits += 1
    if hits:
        print(f"\nvoice_check: FAILED ({hits} instance(s) of manuscript-voice "
              f"history narration)")
        return 1
    print("voice_check: OK (no manuscript-voice history narration)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
