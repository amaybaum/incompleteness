#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""proof_census.py — enumerate the corpus's CANONICAL mathematical statements.

Canonical means `papers/*.md`. The book chapters and `book/*FULL.md` are mirrors under AGENTS.md
§A.14/§A.25 and the `.tex`/`.pdf` are build products; none of them is a separate result, and
counting them would inflate every coverage number this census exists to report.

A statement is recognised by the corpus's own typographic convention: a line beginning with a bold
`**Theorem`/`**Lemma`/`**Corollary`/`**Proposition`/`**Claim`/`**Definition`/`**Axiom`. That is the
form the manuscripts actually use, and it is what `claims_check.py` and `voice_check.py` already
read, so the census sees the same objects the rest of the gate does.

EACH ENTRY CARRIES A FINGERPRINT of the statement text. The ledger records what was mapped; the
fingerprint records WHAT WAS MAPPED TO. When a manuscript statement is edited, its fingerprint
moves, the ledger entry goes stale, and `coverage_check.py` fails — which is the only mechanical
defence against a ledger that certifies a sentence the manuscript no longer contains.

Usage:
    python3 tools/proof_census.py              # human-readable census
    python3 tools/proof_census.py --json       # machine-readable, the ledger's input
"""
import glob
import hashlib
import json
import os
import re
import sys

KINDS = ('Theorem', 'Lemma', 'Corollary', 'Proposition', 'Claim', 'Definition', 'Axiom')
KIND_LETTER = {'Theorem': 'T', 'Lemma': 'L', 'Corollary': 'C', 'Proposition': 'P',
               'Claim': 'K', 'Definition': 'D', 'Axiom': 'X'}

HEAD = re.compile(r'^\*\*(' + '|'.join(KINDS) + r')\b([^*]*)\*\*', re.M)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STOP = {'the', 'a', 'an', 'of', 'and', 'for', 'in', 'on', 'to', 'with', 'is', 'are', 'its'}


def slug(kind, tail, body):
    """A stable, human-legible identifier fragment.

    Prefer the statement's own label -- a number (`Lemma 1`, `Theorem A.5`) or a parenthetical name
    (`Theorem (D-gauge completeness)`). Both are authored text and move only when the author
    renames the statement, which is exactly when the ledger entry SHOULD be revisited. Falling back
    to the opening words of the body would make the id drift on any prose edit, so it is used only
    when there is no label at all, and then it is recorded as `unnamed-<hash>`.
    """
    tail = tail.strip()
    num = re.match(r'^([0-9A-Za-z.]+)', tail)
    paren = re.search(r'\(([^)]*)\)', tail)
    parts = []
    if num and num.group(1).rstrip('.'):
        parts.append(num.group(1).rstrip('.'))
    if paren:
        words = re.findall(r'[A-Za-z0-9]+', paren.group(1).lower())
        parts += [w for w in words if w not in STOP][:5]
    if not parts:
        return 'unnamed-' + hashlib.sha256(body.encode()).hexdigest()[:8]
    return '-'.join(parts).lower().strip('-')


def statement_text(lines, idx):
    """The statement proper: the header line and any immediately following non-blank lines.

    The manuscripts put the formal content in italics on the header line and often continue with a
    displayed equation or a short qualifier before the first blank line. Prose commentary starts
    after that break, and is deliberately NOT fingerprinted -- a ledger that went stale every time
    an explanatory sentence was reworded would be ignored within a round.
    """
    out = []
    for line in lines[idx:]:
        if not line.strip() and out:
            break
        out.append(line)
    return '\n'.join(out).strip()


def census():
    rows = []
    for path in sorted(glob.glob(os.path.join(REPO, 'papers', '*.md'))):
        rel = os.path.relpath(path, REPO)
        paper = os.path.splitext(os.path.basename(path))[0]
        text = open(path, encoding='utf-8').read()
        lines = text.split('\n')
        seen = {}
        for m in HEAD.finditer(text):
            line_no = text[:m.start()].count('\n') + 1
            body = statement_text(lines, line_no - 1)
            s = slug(m.group(1), m.group(2), body)
            key = f'{paper.upper()}:{KIND_LETTER[m.group(1)]}-{s}'
            # Distinct statements sharing a label (SM restates `Corollary` unnamed three times)
            # get a disambiguating suffix in order of appearance, which is stable under edits that
            # do not add or remove one of them.
            seen[key] = seen.get(key, 0) + 1
            if seen[key] > 1:
                key = f'{key}~{seen[key]}'
            rows.append({
                'id': key,
                'paper': rel,
                'line': line_no,
                'kind': m.group(1),
                'label': m.group(2).strip(' .'),
                'statement': body,
                'fingerprint': hashlib.sha256(body.encode()).hexdigest()[:16],
            })
    return rows


def main():
    rows = census()
    if '--json' in sys.argv:
        json.dump(rows, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return 0
    by_paper = {}
    for r in rows:
        by_paper.setdefault(r['paper'], []).append(r)
    for paper, rs in sorted(by_paper.items()):
        print(f'{paper}  ({len(rs)})')
        for r in rs:
            print(f'  {r["line"]:>5}  {r["fingerprint"]}  {r["id"]}')
    print()
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    print('by kind: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))
    print(f'canonical statements: {len(rows)}')
    ids = [r['id'] for r in rows]
    assert len(set(ids)) == len(ids), 'identifier collision'
    return 0


if __name__ == '__main__':
    sys.exit(main())
