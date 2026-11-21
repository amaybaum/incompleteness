#!/usr/bin/env python3
"""Checker for the A1 deletion edit list (edits.json). Standard library only. It never writes a manuscript.

Usage (from the repository root):
  python3 -I -B verification/audits/foundations/a1exit-deletion-20261121/edits_check.py --commit REV [--simulate]
  python3 -I -B .../edits_check.py --tree DIR [--simulate]
  python3 -I -B .../edits_check.py --static
  python3 -I -B .../edits_check.py --self-test

--commit REV  reads each target file as `git show REV:path` and checks that every edit's old string ("old",
              or "old_step2" where given) occurs exactly once in its file. Exit status 1 on any failure.
--tree DIR    the same on a directory holding papers/ and book/ (for example a projected integration).
--simulate    additionally applies the edits in memory only (nothing is written) and reports the residual
              A1-pointer scan of the result, which must be empty apart from the listed false positives.
--static      checks the replacement strings alone: the infinity-assertion scan (zero hits required), the
              register scan of §A.32/§A.33 on added text (zero hits required), the identifier rule (no
              surviving identifier renumbered, no "A1" printed) and the count of ptr sites (194).
"""
import argparse, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
EDITS = os.path.join(HERE, 'edits.json')

# Residual pointer scan: ledger P0 core patterns P1, P2, P5 and the B1 "finiteness posit" pattern.
PTR = re.compile(r'\bA1\b|[Tt]otal[- ]finiteness|totally finite|(?<![A-Za-z])finite total (system|configuration|state)'
                 r'|posit \(ii\)|ledger item \(ii\)|item \(ii\) of the posit|ledger \(ii\)|posit-\(ii\)|[Ff]initeness posit')
# Lines the ledger classifies as false positives or as owned by other units (S2-E / #1468), by file and a
# distinctive substring that survives line moves.
RESIDUAL_ALLOW = [
    ('book/appendix-b-derivations.md', '(A1)', 'ledger FP: anomaly condition (A1), appB:235/246'),
    ('book/The-Incompleteness-of-Observation-FULL.md', '(A1)', 'ledger FP: FULL mirror of the appB anomaly conditions'),
    ('papers/GR.md', 'For a finite total system, restrict it', 'finite-scope wording of ledger X-70 (P2 matches "finite total system")'),
]
# Infinity assertions that no replacement string may introduce (owner decision, cardinality neutrality).
INF = re.compile(r'(?:\b(?:is|are|be|being|been)\s+infinite\b(?!-))|\binfinitely many\b|\bcountably infinite\b'
                 r'|\buncountably infinite\b|\binfinite (?:substratum|universe|configuration space|carrier|set|number)\b'
                 r'|\|S\|\s*=\s*\\infty|\bS\s+is\s+infinite\b|\binfinite in (?:extent|size|cardinality)\b')
NEUTRAL = re.compile(r'\bneither\b[^.]*\bnor\b')
# §A.32/§A.33 register families on added text.
REG = re.compile(r'\b(now|no longer|formerly|corrected|is not listed|withdrawn from|retired|in its current form'
                 r'|as redefined|is now settled|should not be read|the reader should note|honest(?:ly)?)\b', re.I)
CAPS = re.compile(r'(?<![A-Za-z\\])[A-Z]{4,}(?![A-Za-z])')


def load():
    with open(EDITS, encoding='utf-8') as f:
        return json.load(f)


def reader(commit, tree):
    def read(path):
        if tree:
            with open(os.path.join(tree, path), encoding='utf-8') as f:
                return f.read()
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (commit, path)], capture_output=True)
        if r.returncode:
            raise SystemExit('cannot read %s at %s' % (path, commit))
        return r.stdout.decode('utf-8')
    return read


def variant(e, text):
    """Return (old, new, label) for the variant whose old occurs exactly once, else (None, None, counts)."""
    cands = [('old', e['old'], e['new'])]
    if 'old_step2' in e:
        cands.append(('old_step2', e['old_step2'], e['new_step2']))
    counts = []
    for label, o, n in cands:
        c = text.count(o)
        counts.append('%s=%d' % (label, c))
        if c == 1:
            return o, n, label
    return None, None, ','.join(counts)


def check(data, read, simulate):
    texts, fails, used = {}, [], {}
    for e in data['edits']:
        if e['file'] not in texts:
            texts[e['file']] = read(e['file'])
    for e in data['edits']:
        o, n, label = variant(e, texts[e['file']])
        if o is None:
            fails.append('%s %s (%s part %d): old string not unique (%s)' % (e['id'], e['file'], e['site'], e['part'], label))
        else:
            used[label] = used.get(label, 0) + 1
    print('uniqueness: %d edits, %d fail; variants used %s' % (len(data['edits']), len(fails), used))
    for x in fails:
        print('  FAIL ' + x)
    if simulate and not fails:
        sim = dict(texts)
        for e in data['edits']:
            o, n, _ = variant(e, sim[e['file']])
            if o is None:
                fails.append('%s: old string lost during in-memory application' % e['id'])
                continue
            sim[e['file']] = sim[e['file']].replace(o, n, 1)
        res = []
        for path in sorted(set(corpus(read)) | set(sim)):
            t = sim.get(path) or read(path)
            for i, line in enumerate(t.split('\n'), 1):
                if PTR.search(line):
                    why = [w for f_, s_, w in RESIDUAL_ALLOW if f_ == path and s_ in line and not
                           re.search(r'\bA1\b(?!\))', line.replace('(A1)', ''))]
                    res.append((path, i, why[0] if why else None, PTR.search(line).group(0)))
        bad = [r for r in res if r[2] is None]
        print('simulation: residual pointer lines %d (%d allowed as listed, %d unqualified)' % (len(res), len(res) - len(bad), len(bad)))
        for p, i, w, m in res:
            print('  %s %s:%d [%s]%s' % ('allow' if w else 'RESIDUAL', p, i, m, (' ' + w) if w else ''))
        if bad:
            fails.append('residual pointer lines remain')
    return not fails


def corpus(read):
    try:
        out = subprocess.run(['git', '-C', ROOT, 'ls-files', 'papers/*.md', 'book/*.md'], capture_output=True, text=True).stdout.split()
    except Exception:
        out = []
    return out


def static(data):
    ok = True
    inf, reg, caps, ids = [], [], [], []
    for e in data['edits']:
        new = e.get('new_step2') or e['new']
        old = e.get('old_step2') or e['old']
        for sent in re.split(r'(?<=[.;:])\s+', new):
            for m in INF.finditer(sent):
                if not NEUTRAL.search(sent):
                    inf.append((e['id'], m.group(0), sent[:120]))
        added = new
        for tok in set(REG.findall(added)) - set(REG.findall(old)):
            reg.append((e['id'], tok))
        for tok in set(CAPS.findall(added)) - set(CAPS.findall(old)):
            caps.append((e['id'], tok))
        if re.search(r'\bA1\b', new):
            ids.append((e['id'], 'A1 printed in a replacement'))
        for a in ('A2', 'A3', 'A4', 'A5', 'A6'):
            if old.count(a) and not new.count(a) and a not in ('A1',) and e['row'] not in ('X-00',):
                # a surviving identifier must not disappear from a range rewrite unless the clause is deleted
                if new.strip():
                    ids.append((e['id'], '%s dropped from a non-empty replacement' % a))
        if re.search(r'\bA[1-6]\s*[–-]\s*A[1-6]\b', new):
            for m in re.finditer(r'\bA([1-6])\s*[–-]\s*A([1-6])\b', new):
                if m.group(1) == '1':
                    ids.append((e['id'], 'range starting at A1'))
        for m in re.finditer(r'\((ii)\)', new):
            ids.append((e['id'], 'retired ledger identifier (ii) printed'))
    print('infinity-assertion scan: %d hits' % len(inf))
    for x in inf:
        print('  HIT %s %r in: %s' % x)
    print('register scan (added text, §A.32/§A.33): %d hits, new capitals %d' % (len(reg), len(caps)))
    for x in reg:
        print('  REG %s %r' % x)
    for x in caps:
        print('  CAPS %s %r' % x)
    print('identifier rule: %d findings' % len(ids))
    for x in ids:
        print('  ID %s %s' % x)
    ptr_sites = {(e['site'] if not e['mirror_of'] else e['file'] + '@' + e['site']) for e in data['edits'] if e['kind'] == 'ptr'}
    print('ptr sites with a drafted rewrite (chapter site and FULL mirror counted separately): %d' % len(ptr_sites))
    ok = not inf and not reg and not caps and not ids and len(ptr_sites) == 194
    return ok


def self_test():
    data = {'edits': [{'id': 'T1', 'file': 'x', 'site': 'x:1', 'part': 1, 'old': 'abc', 'new': 'abd'},
                      {'id': 'T2', 'file': 'x', 'site': 'x:1', 'part': 2, 'old': 'zz', 'new': '', 'old_step2': 'qq', 'new_step2': ''}]}
    rd = lambda p: 'abc qq'
    assert check(data, rd, False), 'unique strings must pass'
    rd2 = lambda p: 'abc abc qq'
    assert not check(data, rd2, False), 'a duplicated old string must fail'
    rd3 = lambda p: 'abc'
    assert not check(data, rd3, False), 'a missing old string must fail'
    bad = {'edits': [{'id': 'T3', 'kind': 'x', 'row': 'X-01', 'site': 's', 'file': 'f', 'mirror_of': None,
                      'old': 'a set (finite under A1)', 'new': 'a set, and the substratum is infinite'}]}
    assert INF.search(bad['edits'][0]['new']), 'infinity assertion must be detected'
    assert not INF.search('neither finite nor infinite-dimensional'), 'infinite-dimensional is not an assertion'
    s = 'the framework assumes neither that the substratum is finite nor that it is infinite'
    assert INF.search(s) and NEUTRAL.search(s), 'neutral statement is matched and exempted'
    assert REG.search('the claim is now settled'), 'register family must be detected'
    print('self-test PASS')
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--commit')
    ap.add_argument('--tree')
    ap.add_argument('--simulate', action='store_true')
    ap.add_argument('--static', action='store_true')
    ap.add_argument('--self-test', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test() else 1)
    data = load()
    ok = True
    if a.static:
        ok = static(data) and ok
    if a.commit or a.tree:
        ok = check(data, reader(a.commit, a.tree), a.simulate) and ok
    print('RESULT ' + ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
