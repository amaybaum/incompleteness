#!/usr/bin/env python3
"""voice_check.py - does the manuscript narrate its own revision history?

AGENTS.md: "The document never narrates its own history. No 'formerly,' no
'is not listed,' no 'withdrawn from' in the manuscript's voice." Correction
rounds reintroduce this language faster than it can be caught by reading.

SCOPE IS POSITIVE, NOT AN EXEMPT LIST. The rule is about the MANUSCRIPT's
voice, so only publication manuscript Markdown is scanned: papers/*.md and the
book manuscript files under book/. Everything else - verification/ audits and
results, control-plane preregistrations and their amendments, root process docs
- is outside the manuscript and is never scanned. Those records exist partly to
narrate history, and a checker whose docstring says "manuscript" while walking
the whole repository will eventually flag one of them; it did, on a frozen
control-plane amendment, which is what made the scope explicit here.

Exempt within scope: papers/Complexity.md, and that path only (its claims ladder
records withdrawn EMPIRICAL verdicts, which is honest reporting of a failed
analysis, not narration of the document's own edits). The exception is keyed to
the papers/ surface, not to the bare filename, so a future book/Complexity.md
would still be scanned. book/README.md is directory documentation rather than
manuscript prose and is not in scope.

Usage:  python3 voice_check.py [--root DIR]
Exit 1 if manuscript-voice history narration is present.
"""
import os, re, sys

# Exceptions are PATH-SPECIFIC, not filename-specific. The documented exception
# is `papers/Complexity.md`; a filename-only rule would silently exempt a future
# `book/Complexity.md`, which nothing justifies.
PAPERS_EXEMPT = {'Complexity.md'}
# Directory documentation that lives beside the book manuscript but is not it.
BOOK_NON_MANUSCRIPT = {'README.md'}


def manuscript_files(root):
    """The publication manuscript, positively enumerated.

    papers/*.md are the papers build.sh builds; book/*.md are the book
    manuscript and its chapters, less directory documentation.
    """
    out = []
    papers = os.path.join(root, 'papers')
    if os.path.isdir(papers):
        for f in sorted(os.listdir(papers)):
            if f.endswith('.md') and f not in PAPERS_EXEMPT:
                out.append(os.path.join(papers, f))
    book = os.path.join(root, 'book')
    if os.path.isdir(book):
        for f in sorted(os.listdir(book)):
            # PAPERS_EXEMPT deliberately does not apply here.
            if f.endswith('.md') and f not in BOOK_NON_MANUSCRIPT:
                out.append(os.path.join(book, f))
    return out
PATTERNS = [
    (r'\bwithdraw(n|s|al)?\b',        "revision narration: 'withdrawn'"),
    (r'[Ee]arlier drafts?',           "revision narration: 'earlier draft'"),
    (r'\bformerly\b|\bFormer\b',      "revision narration: 'former(ly)'"),
    (r'\bnow (separates|states|says|reads)\b', "revision narration: 'now ...'"),
    (r'\bpreviously (said|stated|read|claimed)\b', "revision narration"),
    (r'\bno longer (presents|claims|says|states|asserts)\b',
     "revision narration: 'no longer ...'"),
    (r'\b(has|have) since been (revised|corrected|dropped)\b',
     "revision narration: 'has since been ...'"),
    (r'\bwe (were|had) (wrong|mistaken)\b', "first-person revision narration"),
]

def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    # This check applies to the MANUSCRIPT only. The session transfer exists to
    # narrate history, so pointing this at a transfer produces hundreds of
    # meaningless failures. Refuse rather than mislead.
    if not os.path.isdir(os.path.join(root, 'papers')) and \
       os.path.exists(os.path.join(root, 'NEXT-SESSION.md')):
        print("voice_check: SKIPPED - this looks like a session transfer, not "
              "the manuscript tree.")
        print("             The transfer is where revision history BELONGS; "
              "this check applies")
        print("             only to a tree containing papers/.")
        return 0
    hits = 0
    for p in manuscript_files(root):
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
    print("voice_check: OK (no manuscript-voice history narration; "
          f"{len(manuscript_files(root))} manuscript file(s) scanned)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
