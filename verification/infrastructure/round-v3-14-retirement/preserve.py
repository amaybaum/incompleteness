#!/usr/bin/env python3
"""preserve.py -- round V3-14's preservation oracle for the guard transformation.

Usage:
    python3 preserve.py <guard at D> <census.json> <ledger.json> <guard after>
    python3 preserve.py --self-test <guard at D> <census.json> <ledger.json> <guard after>

It is independent of the transformation: it imports nothing from retire.py and decides nothing from
its logic. From the guard at D, the census and the frozen splice ledger alone it derives what the
transformed guard must be, and checks the transformed guard against that:

  L1  the ledger: its base blob is the guard at D, its output blob the guard after; its splices are
      in D order, disjoint, and each one's old text has the SHA-256 it records;
  L2  reconstruction: the guard at D with every splice applied, and nothing else, is the guard
      after, byte for byte;
  S1  selection: every predicate the census retires, and the six of the amendment, lies wholly in
      a splice, as does every predicate and the call of every check the census removes whole;
      no other predicate the census rows name has a line in any splice;
  S2  retained functions: every function whose `def` line lies in no splice has no line in any
      splice, and every function whose `def` line lies in a splice lies wholly in splices;
  S3  control flow: every `continue`, `break`, `return`, `raise` and `assert` at D that lies in a
      splice has its governing block wholly in splices -- for `continue` and `break` the nearest
      enclosing loop, for the others the nearest enclosing function or, at module level, the
      top-level statement holding it;
  S4  regression: the seven statements V3-13's transformation deleted from code it retained are in
      no splice;
  S5  surviving blocks: inside every module-level `for`, `while`, `if`, `with` or `try` whose first
      line lies in no splice, every statement that lies wholly in splices, with its enclosing
      statement not, is a predicate the census retires, one of the amendment's, a counter
      increment (`x += <int>`), or a block holding at least one such predicate and nothing but
      such predicates, counter increments and control flow. Dead code is never removed from a
      block that survives.

--self-test runs the checks on the real inputs, then on mutations of them, each of which must fail
the check named: for each regression site the statement deleted through a consistent splice (S2,
S3 or S5, and S4); one byte of the guard after changed (L2); a splice's old hash changed (L1); a retained
predicate deleted through a consistent splice (S1); a retired predicate restored (S1); and a
condition inside a retained function rewritten through a consistent splice (S2)."""
import ast
import hashlib
import json
import sys

RETIRE = {'redundant', 'retire-history', 'retire-machinery', 'retire-whole'}
# V3-13's amendment to V3-12's census, adopted by V3-14: check, line at D, the census's text hash
AMENDMENT = {('R7-PC4S', 17854, '1459be91d4a5bcbb'), ('R7-PC4S', 17999, 'cfaf77fc616d9bc3'),
             ('R7-PC4S', 18000, '2e5e128c60b1684a'), ('R7-PC4S', 18001, '3a685893e4885af0'),
             ('R7-OLT', 24113, '27f4b1d56c51ac71'), ('R7-OLN', 24549, '2175b51bb131cb5f')}
# the seven statements V3-13's transformation deleted from code it retained: D line, exact text
REGRESSION = (
    ((180, '        if induced_by(n, perm, E) is not None:'), (181, '            continue')),
    ((193, '                break'),),
    ((292, '                changed = True'),),
    ((232, '        if piv is None:'), (233, '            continue')),
    ((304, '        if len(clique) + len(cand) - i <= best:'), (305, '            break')),
    ((25309, '        if not l.strip():'), (25310, '            break')),
    ((26777, '            if depth == 0:'), (26778, '                break')),
)


def blob(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def apply(d_text, splices):
    lines = d_text.split('\n')
    for s in sorted(splices, key=lambda s: s['d_start'], reverse=True):
        lines[s['d_start'] - 1:s['d_end']] = s['new']
    return '\n'.join(lines)


def spliced(splices):
    out = set()
    for s in splices:
        out.update(range(s['d_start'], s['d_end'] + 1))
    return out


def check(d_text, census, ledger, after):
    """[(check id, ok, detail)]."""
    res = []
    lines = d_text.split('\n')
    sp = ledger['splices']
    # L1
    bad = []
    if ledger.get('schema') != 'v3-14-splice-ledger' or ledger.get('base', {}).get('blob') != \
            blob(d_text) or ledger.get('output', {}).get('blob') != blob(after):
        bad.append('blobs')
    prev = 0
    for s in sp:
        if not (prev < s['d_start'] <= s['d_end'] + 1 <= len(lines) + 1):
            bad.append('order at %d' % s['d_start'])
        if sha256('\n'.join(lines[s['d_start'] - 1:s['d_end']])) != s['old_sha256'] or \
                sha256('\n'.join(s['new'])) != s['new_sha256']:
            bad.append('hash at %d' % s['d_start'])
        prev = s['d_end']
    res.append(('L1', not bad, '%d splice(s)%s' % (len(sp), ('; ' + ', '.join(bad[:3])) if bad else '')))
    # L2
    res.append(('L2', apply(d_text, sp) == after, 'reconstruction from D and the ledger'))
    gone = spliced(sp)
    tree = ast.parse(d_text)
    funcs = set()
    for f in ast.walk(tree):
        if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs.update(range(f.lineno, f.end_lineno + 1))
    at = {}
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.Expr)) and n.lineno not in funcs:
            at.setdefault(n.lineno, []).append(n)
    # S1
    disp = {c['check']: c['disposition'] for c in census['checks']}
    amend = {(c, l): h for c, l, h in AMENDMENT}
    want_gone, want_kept, miss = 0, 0, []
    n_ret, n_kept = 0, 0
    for row in census['predicates']:
        chk, line, cls, h = row[0], row[1], row[2], row[6]
        cands = [n for n in at.get(line, [])
                 if hashlib.sha256(ast.unparse(n).encode('utf-8')).hexdigest()[:16] == h]
        if len(cands) != 1:
            miss.append('%s %d unlocated' % (chk, line))
            continue
        span = set(range(cands[0].lineno, cands[0].end_lineno + 1))
        retire = cls in RETIRE or disp[chk] == 'removed whole' or amend.get((chk, line)) == h
        if retire:
            want_gone += 1
            n_ret += cls in RETIRE or (chk, line) in amend
            if not span <= gone:
                miss.append('%s %d kept' % (chk, line))
        else:
            want_kept += 1
            n_kept += cls == 'retain'
            if span & gone:
                miss.append('%s %d touched' % (chk, line))
    for n in tree.body:
        if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and \
                getattr(n.value.func, 'id', None) == 'check':
            tag = n.value.args[0].value
            span = set(range(n.lineno, n.end_lineno + 1))
            if disp.get(tag) == 'removed whole' and not span <= gone:
                miss.append('check %s kept' % tag)
            if disp.get(tag) != 'removed whole' and n.lineno in gone and \
                    n.value.args[0].lineno in gone:
                miss.append('check %s removed' % tag)
    res.append(('S1', not miss, '%d predicates retired, %d retained; %d rows in splices, %d outside'
                '%s' % (n_ret, n_kept, want_gone, want_kept, ('; ' + ', '.join(miss[:3])) if miss
                        else '')))
    # S2
    bad, kept_f = [], 0
    for f in ast.walk(tree):
        if not isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        lo = min([f.lineno] + [x.lineno for x in f.decorator_list])
        span = set(range(lo, f.end_lineno + 1))
        if f.lineno in gone:
            if not span <= gone:
                bad.append('%s partly removed' % f.name)
        else:
            kept_f += 1
            if span & gone:
                bad.append('%s edited' % f.name)
    res.append(('S2', not bad, '%d retained function(s) untouched%s' % (
        kept_f, ('; ' + ', '.join(bad[:3])) if bad else '')))
    # S3
    parent = {}
    for p in ast.walk(tree):
        for c in ast.iter_child_nodes(p):
            parent[c] = p
    bad, total, removed = [], 0, 0
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Continue, ast.Break, ast.Return, ast.Raise, ast.Assert)):
            continue
        total += 1
        if n.lineno not in gone:
            continue
        removed += 1
        g, a = None, parent.get(n)
        while a is not None and a is not tree:
            if isinstance(n, (ast.Continue, ast.Break)) and isinstance(a, (ast.For, ast.While)):
                g = a
                break
            if isinstance(a, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                g = a
                break
            if parent.get(a) is tree:
                g = a
                break
            a = parent.get(a)
        if g is None or not set(range(g.lineno, g.end_lineno + 1)) <= gone:
            bad.append('%s at %d' % (type(n).__name__, n.lineno))
    res.append(('S3', not bad, '%d control-flow statement(s), %d removed with their governing '
                'block%s' % (total, removed - len(bad), ('; ' + ', '.join(bad[:3])) if bad else '')))
    # S4
    bad = [l for site in REGRESSION for l, txt in site if lines[l - 1] != txt or l in gone]
    res.append(('S4', not bad, '%d regression site(s) preserved%s' % (
        len(REGRESSION) - len({s for s in REGRESSION for l, _t in s if l in bad}),
        ('; lines ' + ', '.join(map(str, bad))) if bad else '')))
    # S5
    retired = set()
    for row in census['predicates']:
        if row[2] in RETIRE or disp[row[0]] == 'removed whole' or \
                amend.get((row[0], row[1])) == row[6]:
            retired.add(row[1])

    def whole(n):
        return set(range(n.lineno, n.end_lineno + 1)) <= gone

    def counter(n):
        return isinstance(n, ast.AugAssign) and isinstance(n.op, ast.Add) and \
            isinstance(n.value, ast.Constant) and isinstance(n.value.value, int)

    def residue(n):
        simple = [x for x in ast.walk(n) if isinstance(x, ast.stmt) and not isinstance(
            x, (ast.For, ast.While, ast.If, ast.With, ast.Try))]
        return any(x.lineno in retired for x in simple) and all(
            x.lineno in retired or counter(x) or isinstance(
                x, (ast.Continue, ast.Break, ast.Pass)) for x in simple)
    bad, blocks = [], 0
    for top in tree.body:
        if not isinstance(top, (ast.For, ast.While, ast.If, ast.With, ast.Try)) or top.lineno in gone:
            continue
        blocks += 1
        for n in ast.walk(top):
            if n is top or not isinstance(n, ast.stmt) or not whole(n):
                continue
            if parent.get(n) is not top and isinstance(parent.get(n), ast.stmt) and \
                    whole(parent[n]):
                continue
            if not (n.lineno in retired or counter(n) or residue(n)):
                bad.append('%s at %d' % (type(n).__name__, n.lineno))
    res.append(('S5', not bad, '%d surviving module-level block(s), no dead code removed from '
                'them%s' % (blocks, ('; ' + ', '.join(bad[:4])) if bad else '')))
    return res


def mutate(ledger, d_text, lo, hi, new, why):
    """The ledger with the D lines lo..hi replaced by `new`, merged into any splice it meets."""
    lines = d_text.split('\n')
    sp = [dict(s) for s in ledger['splices']]
    meet = [s for s in sp if s['d_start'] <= hi + 1 and s['d_end'] >= lo - 1]
    keep = [s for s in sp if s not in meet]
    a = min([lo] + [s['d_start'] for s in meet])
    b = max([hi] + [s['d_end'] for s in meet])
    # rebuild the merged span from D, applying the met splices and the new change in D order
    out, i = [], a
    ms = sorted(meet, key=lambda s: s['d_start'])
    while i <= b:
        s = next((s for s in ms if s['d_start'] == i), None)
        if lo <= i <= hi:
            if i == lo:
                out.extend(new)
            i += 1
            continue
        if s is not None:
            out.extend(s['new'])
            i = s['d_end'] + 1
            continue
        out.append(lines[i - 1])
        i += 1
    m = {'d_start': a, 'd_end': b, 'old_sha256': sha256('\n'.join(lines[a - 1:b])),
         'new': out, 'new_sha256': sha256('\n'.join(out)), 'reasons': [why]}
    led = dict(ledger)
    led['splices'] = sorted(keep + [m], key=lambda s: s['d_start'])
    after = apply(d_text, led['splices'])
    led['output'] = {'blob': blob(after)}
    return led, after


def self_test(d_text, census, ledger, after):
    fails = []
    real = check(d_text, census, ledger, after)
    for cid, ok, detail in real:
        print('REAL  %s  %s  %s' % (cid, 'holds' if ok else 'FAILS', detail))
        if not ok:
            fails.append('real ' + cid)
    lines = d_text.split('\n')

    def expect(label, led, aft, must):
        got = {c: ok for c, ok, _d in check(d_text, census, led, aft)}
        failed = sorted(c for c, ok in got.items() if not ok)
        ok = all(not got[c] for c in must)
        print('MUTANT  %-58s fails %s  %s' % (label, ','.join(failed) or 'nothing',
                                                'as required' if ok else 'NOT AS REQUIRED'))
        if not ok:
            fails.append(label)
    for site in REGRESSION:
        lo, hi = site[0][0], site[-1][0]
        led, aft = mutate(ledger, d_text, lo, hi, [], 'mutant')
        inside = any(lo in range(f.lineno, f.end_lineno + 1) for f in ast.walk(ast.parse(d_text))
                     if isinstance(f, ast.FunctionDef))
        flow = any(isinstance(x, (ast.Continue, ast.Break)) for x in ast.walk(ast.parse(d_text))
                   if isinstance(x, ast.stmt) and lo <= x.lineno <= hi)
        expect('regression site %d deleted' % lo, led, aft,
               ['S4'] + (['S2'] if inside else ['S5']) + (['S3'] if flow else []))
    k = after.index('ok_')
    expect('one byte of the guard after changed', ledger, after[:k] + 'X' + after[k + 1:], ['L2'])
    led = json.loads(json.dumps(ledger))
    led['splices'][0]['old_sha256'] = '0' * 64
    expect('a splice\'s old hash changed', led, after, ['L1'])
    row = next(r for r in census['predicates'] if r[2] == 'retain')
    led, aft = mutate(ledger, d_text, row[1], row[1], [], 'mutant')
    expect('retained predicate %s %d deleted' % (row[0], row[1]), led, aft, ['S1'])
    row = next(r for r in census['predicates'] if r[2] in RETIRE and lines[r[1] - 1].startswith('ok'))
    s = next(s for s in ledger['splices'] if s['d_start'] <= row[1] <= s['d_end'])
    led = json.loads(json.dumps(ledger))
    led['splices'] = [x for x in led['splices'] if x['d_start'] != s['d_start']]
    before = lines[s['d_start'] - 1:row[1] - 1]
    after_ = lines[row[1]:s['d_end']]
    part = []
    if before:
        part.append({'d_start': s['d_start'], 'd_end': row[1] - 1,
                     'old_sha256': sha256('\n'.join(before)), 'new': [],
                     'new_sha256': sha256(''), 'reasons': ['mutant']})
    if after_:
        part.append({'d_start': row[1] + 1, 'd_end': s['d_end'],
                     'old_sha256': sha256('\n'.join(after_)), 'new': [],
                     'new_sha256': sha256(''), 'reasons': ['mutant']})
    led['splices'] = sorted(led['splices'] + part, key=lambda x: x['d_start'])
    aft = apply(d_text, led['splices'])
    led['output'] = {'blob': blob(aft)}
    expect('retired predicate %s %d restored' % (row[0], row[1]), led, aft, ['S1'])
    lo = 232
    assert lines[lo - 1] == '        if piv is None:'
    led, aft = mutate(ledger, d_text, lo, lo, ['        if piv is not None:'], 'mutant')
    expect('condition inside rank() rewritten', led, aft, ['S2'])
    print('preserve: self-test %s' % ('OK' if not fails else 'FAILED: ' + '; '.join(fails)))
    return not fails


def main(argv):
    test = argv[:1] == ['--self-test']
    if test:
        argv = argv[1:]
    if len(argv) != 4:
        print(__doc__.split('\n\n')[1])
        return 2
    d_text, after = open(argv[0], encoding='utf-8').read(), open(argv[3], encoding='utf-8').read()
    census = json.load(open(argv[1], encoding='utf-8'))
    ledger = json.load(open(argv[2], encoding='utf-8'))
    if test:
        return 0 if self_test(d_text, census, ledger, after) else 1
    res = check(d_text, census, ledger, after)
    for cid, ok, detail in res:
        print('%s  %s  %s' % (cid, 'holds' if ok else 'FAILS', detail))
    ok = all(ok for _c, ok, _d in res)
    print('preserve: %s' % ('all hold' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
