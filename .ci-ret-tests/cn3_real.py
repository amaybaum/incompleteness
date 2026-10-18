"""The 39 prototype controls of CN3-DESIGN.md plus the 3 named boundary controls, re-expressed against the REAL
implementation (scratch; never committed). argv: <base worktree at 7c5f97d9> <ret-fix dir> <new worktree> <out dir>
Columns b* are the base's own functions (as in the prototype); columns p* are now the committed code's functions:
check_objects.pending_citation (O10), check_objects.o7_entry + tranche_failures (O7 with O3's tranche pin), and
check_retention.research_lifecycle (R13). The prototype's own rule functions below are kept but unused.

Runs every control twice:
  base      the worktree's own, unmodified functions: check_objects.pending_citation (O10), check_objects.lifecycle and
            cited_by_rule inside a verbatim transcription of check()'s O7 loop (lines 648-672 at 7c5f97d9), and
            check_retention.research_lifecycle (R13);
  proposed  the rule of CN3-DESIGN.md §B, implemented below from scratch, reusing only the base's id_forms, HEXWORD,
            run_word (for the base-identical first O7 conditions), ci_head and citing_lines.
A record named R13* is #829's: it has no research-build entry, so R13 on it is the parity question, not a gate verdict.
Fixture records are written to a temporary root inside the ret-fix dir and removed at the end; each fixture is
reported by its exact edit of the real record and the sha256 of the resulting text. Exit 0 iff every measured verdict
equals its stated expectation (base and proposed)."""
import hashlib, json, os, re, shutil, string, sys, types

WT, RF, NWT, OUTD = sys.argv[1:5]
A = os.path.join(WT, 'verification/audits/evidence-retention')


def load(name, modname):
    p = os.path.join(A, name)
    m = types.ModuleType(modname)
    m.__file__ = p
    exec(compile(open(p, encoding='utf-8').read(), p, 'exec'), m.__dict__)
    return m


co = load('check_objects.py', 'co_base')
cr = load('check_retention.py', 'cr_base')
NA = os.path.join(NWT, 'verification/audits/evidence-retention')


def nload(name, modname):
    p = os.path.join(NA, name)
    m = types.ModuleType(modname)
    m.__file__ = p
    exec(compile(open(p, encoding='utf-8').read(), p, 'exec'), m.__dict__)
    return m


nco = nload('check_objects.py', 'co_real')
ncr = nload('check_retention.py', 'cr_real')
OBJ = json.load(open(os.path.join(A, 'objects', 'manifest.json'), encoding='utf-8'))
RET = json.load(open(os.path.join(A, 'manifest.json'), encoding='utf-8'))
ENT = {e['oid']: e for e in OBJ['objects']}

REC829 = 'verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md'
REC831 = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/preregistration.md'
TXT = {'829': open(os.path.join(RF, 'r829.md'), encoding='utf-8').read(),
       '831': open(os.path.join(RF, 'r831.md'), encoding='utf-8').read()}
PATH = {'829': REC829, '831': REC831}
T = {'1ab0': ('1ab0fd9dd2c6701197f2e0ab18401cafb76a090d', '39043849411', '829', 423),
     '6959': ('6959ced4c327ebb800cf6d463a049e4066e37288', '39056982958', '829', 439),
     'e684': ('e684897da41b1c3d066b880194c9beb87a19b7ad', '38450187534', '831', 69),
     'febf': ('febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3', '38454439833', '831', 127)}

# ------------------------------------------------------------------------------------------------ proposed rule
JOIN = {'-', '_', '.'}
LET = set(string.ascii_letters)
ALNUM = set(string.ascii_letters + string.digits)
HEXANY = re.compile(r'(?<![0-9A-Fa-f])[0-9A-Fa-f]{7,}(?![0-9A-Fa-f])')
TRANCHE_PINS = {2: (920, '3e1800891ab153d53046f742f2e5557f36c2febfd1508c7039baa67b22cf937f'),
                4: (66, 'e05c857702a55756c8d6dbc8fed29c4d2ac94b010bba745c1e23172fbd4add47')}


def occurrences(run, line):
    """Each digit-bounded occurrence of run (R13's match, used by both checkers): 'free' or 'embedded'. Embedded: an
    ASCII letter directly beside it, or a joiner (- _ .) beside it that is itself followed (or preceded) by an ASCII
    letter or digit, so the run is part of one identifier or file name."""
    out = []
    for m in re.finditer(r'(?<![0-9])%s(?![0-9])' % re.escape(run), line):
        s, e = m.start(), m.end()
        b, b2 = line[s - 1:s], line[s - 2:s - 1] if s > 1 else ''
        a, a2 = line[e:e + 1], line[e + 1:e + 2]
        emb = b in LET or a in LET or (b in JOIN and b != '' and b2 in ALNUM and b2 != '') or \
            (a in JOIN and a != '' and a2 in ALNUM and a2 != '')
        out.append('embedded' if emb else 'free')
    return out


def line_class(run, line):
    o = occurrences(run, line)
    return None if not o else 'free' if 'free' in o else 'embedded'


def other_heads(oid, line):
    """Hex words naming another commit, case-folded (N1): 7-40 digits as the base's other_ids; 41-63 digits always
    (no commit id or sha256 has that length, and it can hide a 40-digit id); 64 or more never (a digest)."""
    bad = []
    for w in HEXANY.findall(line):
        lw, n = w.lower(), len(w)
        if n <= 40:
            if (lw != oid) if n == 40 else (not w.isdigit() and not oid.startswith(lw)):
                bad.append(w)
        elif n < 64:
            bad.append(w)
    return bad


def win(L, n):
    return [L[k - 1] for k in (n - 1, n, n + 1) if 1 <= k <= len(L)]


def full_rule(oid, L, n):
    bad = sorted({w for l in win(L, n) for w in other_heads(oid, l)})
    if bad:
        return 'names another head beside the run on line %d (%s)' % (n, ', '.join(bad))
    if not any(oid in co.HEXWORD.findall(l) for l in win(L, n)):
        return 'does not state the full id beside the run on line %d' % n
    return None


def quiet_rule(oid, L, n):
    bad = sorted({w for l in win(L, n) for w in other_heads(oid, l)})
    return 'names another head beside its embedded mention on line %d (%s)' % (n, ', '.join(bad)) if bad else None


def scan(oid, run, L):
    """(free lines, embedded-only lines, first violation or None) for run in L."""
    F = [n for n, l in enumerate(L, 1) if line_class(run, l) == 'free']
    E = [n for n, l in enumerate(L, 1) if line_class(run, l) == 'embedded']
    for n in sorted(F + E):
        r = full_rule(oid, L, n) if n in F else quiet_rule(oid, L, n)
        if r:
            return F, E, r
    return F, E, None


def prop_o10(oid, run, L):
    if L is None:
        return 'pending', None
    at = [n for n, l in enumerate(L, 1) if co.id_forms(oid, l)]
    if not at:
        return 'FAIL', 'does not cite it'
    F, E, r = scan(oid, run, L)
    if not F:
        return 'FAIL', 'does not cite run %s free-standing beside it (embedded only: %s)' % (run, E)
    if r:
        return 'FAIL', r
    return 'eligible', {'qualifying': sorted(set(at) | set(F)), 'id': at, 'free': F, 'embedded': E}


def pins(objs):
    """CN-1 as planned: (labels valid, pins hold, reason)."""
    tb = {int(k) for k in OBJ.get('tranche_bases', {}) if re.fullmatch(r'[1-9][0-9]*', str(k)) and int(k) >= 5}
    allowed = set(TRANCHE_PINS) | tb
    bad = [e['oid'][:12] for e in objs if type(e.get('tranche')) is not int or e['tranche'] not in allowed]
    if bad:
        return False, False, 'O3 tranche label not an exact allowed int: %s' % bad[:3]
    for t, (n, d) in TRANCHE_PINS.items():
        s = sorted(e['oid'] for e in objs if e['tranche'] == t)
        if len(s) != n or hashlib.sha256(''.join(o + '\n' for o in s).encode()).hexdigest() != d:
            return True, False, 'O3 tranche %d membership is not the pinned set (%d entries)' % (t, len(s))
    return True, True, None


def prop_lifecycle(e, pins_hold):
    return e.get('type') == 'commit' and not (type(e.get('tranche')) is int and e['tranche'] == 2 and pins_hold)


def prop_o7(e, texts, life):
    """The base's first four O7 conditions unchanged; then, for a lifecycle entry, the proposed rule."""
    oid, cites = e['oid'], e.get('cited', [])
    base_first = base_o7(e, texts, life=False)
    if base_first:
        return 'FAIL', base_first[0]
    if not life:
        return 'cited', 'token rule (pinned legacy)'
    locs = [c['location'] for c in cites]
    if len(set(locs)) != len(locs):
        return 'FAIL', 'a location is mapped twice'
    if not any(c.get('run') for c in cites):
        return 'FAIL', 'cited without a run citation'
    runs = sorted({str(c['run']) for c in cites if c.get('run')})
    for c in cites:
        f, _, ln = c['location'].rpartition(':')
        L, n = texts[f], int(ln)
        if any(t not in co.id_forms(oid, L[n - 1]) for t in c.get('tokens') or []
               if re.fullmatch(r'[0-9a-f]{7,40}', t) and not t.isdigit()):
            return 'FAIL', '%s does not hold its token as a word that is a form of its id' % c['location']
        if c.get('run'):
            if line_class(str(c['run']), L[n - 1]) != 'free':
                return 'FAIL', '%s is mapped as a run citation but holds no free-standing citation of it' % c['location']
        elif other_heads(oid, L[n - 1]):
            return 'FAIL', '%s names another id' % c['location']
    for f in sorted({c['location'].rpartition(':')[0] for c in cites}):
        L = texts[f]
        mapped = {int(c['location'].rpartition(':')[2]) for c in cites if c['location'].rpartition(':')[0] == f}
        q = {n for n, l in enumerate(L, 1) if co.id_forms(oid, l)}
        for r in runs:
            F, E, v = scan(oid, r, L)
            if v:
                return 'FAIL', '%s %s' % (f.split('/')[-2], v)
            q |= set(F)
        if not q <= mapped:
            return 'FAIL', 'qualifying citation(s) %s of %s not mapped' % (sorted(q - mapped), f.split('/')[-2])
    for r in runs:
        ok, h = co.ci_head(ROOT, r)
        if not ok or h not in (None, oid):
            return 'FAIL', 'run %s retained with another head' % r
    return 'cited', None


def prop_r13(rid, head, rec, line, L, mapped=None):
    """R13 as proposed, inside the record; the rule for lines outside the record is the base's, unchanged."""
    cl = cr.citing_lines(ROOT, rid, os.path.join(ROOT, '__archive__'))
    if mapped is None:
        if any(p != rec for p, _ in cl):
            return 'FAIL', 'cited outside the record while pending'
        if L is None:
            return 'pending', None
        F, E, v = scan(head, rid, L)
        if not F and not E:
            return 'FAIL', 'does not cite run %s' % rid
        if line not in F:
            return 'FAIL', 'the recorded line %d is not a free-standing citation (free %s, embedded %s)' % (line, F, E)
        if v:
            return 'FAIL', v
        return 'eligible', {'free': F, 'embedded': E}
    if len(set(mapped)) != len(mapped):
        return 'FAIL', 'a line is mapped twice'
    F, E, v = scan(head, rid, L)
    if any(p != rec for p, _ in cl):
        return 'FAIL', 'cited outside the mapped record'
    if not set(F) <= set(mapped):
        return 'FAIL', 'free-standing citation(s) %s not mapped' % sorted(set(F) - set(mapped))
    if not set(mapped) <= set(F):
        return 'FAIL', 'mapped line(s) %s hold no free-standing citation' % sorted(set(mapped) - set(F))
    if v:
        return 'FAIL', v
    return 'cited', None


# ------------------------------------------------------------------------------------------------ base harness
def base_o7(e, texts, life=None):
    """check()'s O7 loop at 7c5f97d9, lines 648-672, transcribed for one entry; life=None uses the base lifecycle()."""
    fails, F = [], None
    F = fails.append
    oid = e['oid']
    lc = co.lifecycle(e) if life is None else life
    for c in e.get('cited', []):
        f, _, ln = c.get('location', '').rpartition(':')
        lines = texts.get(f)
        toks = list(c.get('tokens') or []) + ([c['run']] if c.get('run') else [])
        if lines is None or not ln.isdigit() or int(ln) > len(lines):
            F('O7 %s: citing location %s does not exist' % (oid[:12], c.get('location')))
        elif not toks or not any(t in lines[int(ln) - 1] for t in toks):
            F('O7 %s: %s does not hold its token' % (oid[:12], c.get('location')))
        elif c.get('run') and not co.run_word(str(c['run'])).search(lines[int(ln) - 1]):
            F('O7 %s: %s does not hold its run %s' % (oid[:12], c.get('location'), c['run']))
        elif any(isinstance(t, str) and re.fullmatch(r'[0-9a-f]{7,40}', t) and not t.isdigit() and
                 not oid.startswith(t) for t in toks):
            F('O7 %s: %s records a hex token that is not a prefix of its id' % (oid[:12], c.get('location')))
        elif lc:
            r = co.cited_by_rule(oid, c, lines, int(ln), ROOT)
            if r:
                F('O7 %s: %s %s' % (oid[:12], c.get('location'), r))
    if lc and e.get('cited') and not any(c.get('run') for c in e['cited']):
        F('O7 %s: a commit of tranche %d or later is cited without a run citation' % (oid[:12], co.LIFECYCLE_TRANCHE))
    return fails


def base_o10(oid, run, rec):
    aw = dict(ENT[oid].get('awaiting_citation') or {'pull_request': 1, 'round': 'X', 'record': rec, 'run': run})
    fails = []
    st = co.pending_citation(oid, aw, ROOT, fails.append)
    return (st[0], st[1]) if st else ('FAIL', fails[0] if fails else '?')


def base_r13(rid, head, rec, line, mapped=None):
    cr.R13_STATES.clear()
    fails = []
    aw = {'pull_request': 1, 'record': rec, 'round': 'X', 'line': line, 'head': '0' * 40}
    e = {'awaiting_citation': aw} if mapped is None else \
        {'citations': [{'path': rec, 'line': n} for n in mapped]}
    cr.research_lifecycle(e, 'research-' + rid, rid, head, aw if mapped is None else None, True,
                          os.path.join(ROOT, '__archive__'), ROOT, fails.append)
    if fails:
        return 'FAIL', fails[0]
    return cr.R13_STATES.get('research-' + rid, ('none', None))


# ------------------------------------------------------------------------------------------------ real implementation
def real_o10(oid, run, rec):
    aw = dict(ENT[oid]['awaiting_citation'])
    fails = []
    st = nco.pending_citation(oid, aw, ROOT, fails.append)
    return (st[0], st[1]) if st else ('FAIL', fails[0] if fails else '?')


def real_o7(e, texts, objs):
    fails = []
    nco.o7_entry(e['oid'], e, lambda f: texts.get(f), ROOT, fails.append)
    t = nco.tranche_failures({x['oid']: x for x in objs}, OBJ.get('tranche_bases', {}))
    allf = t + fails
    return ('FAIL', '; '.join(allf)) if allf else ('cited', None)


def real_r13(rid, head, rec, line, mapped=None):
    ncr.R13_STATES.clear()
    fails = []
    aw = {'pull_request': 1, 'record': rec, 'round': 'X', 'line': line, 'head': '0' * 40}
    e = {'awaiting_citation': aw} if mapped is None else {'citations': [{'path': rec, 'line': n} for n in mapped]}
    ncr.research_lifecycle(e, 'research-' + rid, rid, head, aw if mapped is None else None, True,
                           os.path.join(ROOT, '__archive__'), ROOT, fails.append)
    if fails:
        return 'FAIL', fails[0]
    return ncr.R13_STATES.get('research-' + rid, ('none', None))


# ------------------------------------------------------------------------------------------------ controls
ROOT = os.path.join(RF, 'fx-root')
RIDHEAD = {'38450187534': 'e684897da41b1c3d066b880194c9beb87a19b7ad',
           '38454439833': 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3'}
HEX64 = '4e6303690387740559e4e37ca35037722f22c45a0b3da311365be06ca3be9b5c'


def setroot(which, text):
    if os.path.isdir(ROOT):
        shutil.rmtree(ROOT)
    p = os.path.join(ROOT, PATH[which])
    os.makedirs(os.path.dirname(p))
    if text is not None:
        open(p, 'w', encoding='utf-8').write(text)


def repl(which, n, new):
    L = TXT[which].split('\n')
    L[n - 1] = new
    return '\n'.join(L)


def app(which, extra):
    return TXT[which] + extra


def cite(oid, spec):
    """spec: [(line, tokens, run or None)] -> an entry promoted to those citations of its record."""
    which = T[[k for k in T if T[k][0] == oid][0]][2]
    e = dict(ENT[oid])
    e.pop('awaiting_citation', None)
    e['cited'] = [dict({'location': '%s:%d' % (PATH[which], n), 'tokens': t}, **({'run': r} if r else {}))
                  for n, t, r in spec]
    return e


def good_map(k):
    oid, run, which, rl = T[k]
    return [(rl - 1, [oid], None), (rl, [run] if which == '831' else [oid[:8]], run)]


C = []


def ctrl(name, kind, k, text, edit, expect, o7=None, r13map=None, label=None):
    C.append(dict(name=name, kind=kind, k=k, text=text, edit=edit, expect=expect, o7=o7, r13map=r13map, label=label))


NEARMISS = repl('829', 422, TXT['829'].split('\n')[421].replace('1ab0fd9dd2c6701197f2e0ab18401cafb76a090d',
                                                                    '1ab0fd9dd2c6701197f2e0ab18401cafb76a0900'))
# expect keys: bO10 bO7 bR13 pO10 pO7 pR13 ('pass' | 'fail' | '-')
# -- positive
for k in ('1ab0', '6959', 'e684', 'febf'):
    rl = T[k][3]
    ctrl('P-%s real record, landed (eligible)' % k, '+', k, TXT[T[k][2]], 'none (real blob)',
         dict(bO10='pass', bR13='fail' if k == '1ab0' else 'pass', pO10='pass', pR13='pass'))
    ctrl('P-%s real record, promoted to its qualifying lines' % k, '+', k, TXT[T[k][2]], 'none (real blob)',
         dict(bO7='pass', bR13='fail' if k == '1ab0' else 'pass', pO7='pass', pR13='pass'),
         o7=good_map(k), r13map=[rl])
ev = '\n| path | sha256 |\n| --- | --- |\n| `evidence/run1-38450187534.json` | `%s` |\n' % HEX64
ctrl('P-evidence-filename mention on #831 (the #829 :482 form)', '+', 'e684', app('831', ev), 'append %r' % ev,
     dict(bO10='pass', bR13='fail', pO10='pass', pR13='pass'))
ctrl('P-evidence-filename mention on #831, promoted to 68+69', '+', 'e684', app('831', ev), 'append %r' % ev,
     dict(bO7='pass', bR13='fail', pO7='pass', pR13='pass'), o7=good_map('e684'), r13map=[69])
dg = '\nThe log digest is `ab38450187534cd%s`.\n' % ('0' * 49)
ctrl('P-run digits inside a 64-hex digest', '+', 'e684', app('831', dg), 'append %r' % dg,
     dict(bO10='pass', bR13='fail', pO10='pass', pR13='pass'))
up = '\n| `evidence/run1-38450187534.json` | `%s` |\n' % HEX64.upper()
ctrl('P-uppercase 64-hex digest beside an embedded mention', '+', 'e684', app('831', up), 'append %r' % up,
     dict(bO10='pass', bR13='fail', pO10='pass', pR13='pass'))
dup = ('\ncompiled again at `e684897da41b1c3d066b880194c9beb87a19b7ad`, workflow run\n'
       '[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534).\n')
ctrl('P-a second correct free-standing citation, pending (eligible)', '+', 'e684', app('831', dup), 'append %r' % dup,
     dict(bO10='pass', bR13='pass', pO10='pass', pR13='pass'))
# -- negative
far = '\nRun 38450187534 passed.\n'
ctrl('N-d-far-nohead', '-', 'e684', app('831', far), 'append %r' % far,
     dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))
ctrl('N-incorrect head beside a free-standing citation (#829 :423 states 6959ced4)', '-', '1ab0',
     repl('829', 423, TXT['829'].split('\n')[422].replace('`1ab0fd9d…`', '`6959ced4…`')), ':423 `1ab0fd9d…` -> `6959ced4…`',
     dict(bO10='fail', bR13='fail', pO10='fail', pR13='fail'))
ctrl('N-incorrect head in UPPERCASE beside a free-standing citation (d-upper)', '-', '1ab0',
     repl('829', 423, TXT['829'].split('\n')[422].replace('`1ab0fd9d…`', '`6959CED4…`')), ':423 `1ab0fd9d…` -> `6959CED4…`',
     dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))   # base R13* fails only through :482
dfar = '\nRun 38450187534 was dispatched on `febfe5e2…`.\n'
ctrl('N-d-far (far free-standing citation, another head)', '-', 'e684', app('831', dfar), 'append %r' % dfar,
     dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))
cdup = ('\ncompiled again at `febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3`, workflow run\n'
        '[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534).\n')
ctrl('N-duplicate free-standing citation with a conflicting full head', '-', 'e684', app('831', cdup), 'append %r' % cdup,
     dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))
emb = '\n| `evidence/run1-39043849411.json` | head `6959ced4c327ebb800cf6d463a049e4066e37288` |\n'
ctrl('N-embedded mention beside a different full head', '-', '1ab0', app('829', emb), 'append %r' % emb,
     dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))
only = '`evidence/run1-38450187534.json` is the run\'s log.'
ctrl('N-run cited only through an embedded mention (#831 :69 replaced)', '-', 'e684', repl('831', 69, only),
     ':69 -> %r' % only, dict(bO10='pass', bR13='pass', pO10='fail', pR13='fail'))
ctrl('N-f1 promotion maps the run line only (#831 :69)', '-', 'e684', TXT['831'], 'none',
     dict(bO7='pass', pO7='fail'), o7=[(69, ['38450187534'], '38450187534')])
ctrl('N-f5 a second correct citation left unmapped (O7 68+69, R13 69)', '-', 'e684', app('831', dup), 'append %r' % dup,
     dict(bO7='pass', bR13='fail', pO7='fail', pR13='fail'), o7=good_map('e684'), r13map=[69])
f6 = '\nThe source commit is `e684897da41b1c3d066b880194c9beb87a19b7ad`.\n'
ctrl('N-f6 the id cited again, unmapped (O7 68+69)', '-', 'e684', app('831', f6), 'append %r' % f6,
     dict(bO7='pass', pO7='fail'), o7=good_map('e684'))
ctrl('N-partial promotion near miss: #829 1ab0fd9d mapped at :423 only', '-', '1ab0', TXT['829'], 'none',
     dict(bO7='pass', pO7='fail'), o7=[(423, ['1ab0fd9d'], '39043849411')])
ctrl('N-a location mapped twice', '-', '1ab0', TXT['829'], 'none', dict(bO7='pass', pO7='fail'),
     o7=good_map('1ab0') + [(423, ['1ab0fd9d'], '39043849411')])
ctrl('N-the embedded :482 mapped as a run citation', '-', '1ab0', TXT['829'], 'none', dict(bO7='fail', pO7='fail'),
     o7=good_map('1ab0') + [(482, ['39043849411'], '39043849411')])
for lab in (3, '4', 2, True, 4.0, 4):
    ctrl('N-CN-1 near-miss head at :422, token-rule promotion, tranche %r' % (lab,), '-', '1ab0', NEARMISS,
         ':422 full id ...a090d -> ...a0900', dict(bO7='fail' if (type(lab) is int and lab == 4) else 'pass', pO7='fail'),  # base: type(t) is int and t >= 4
         o7=[(422, ['1ab0fd9d'], None), (423, ['1ab0fd9d'], '39043849411')], label=lab)
sm = {'filename carries another head\'s 8-digit form':
      '\n| `evidence/run1-39043849411-6959ced4.json` | `%s` |\n' % HEX64,
      'another full head in UPPERCASE beside the filename':
      '\n| `evidence/run1-39043849411.json` | `6959CED4C327EBB800CF6D463A049E4066E37288` |\n',
      'another full head glued into the file name (52 hex digits)':
      '\n| `evidence/run1-39043849411a6959ced4c327ebb800cf6d463a049e4066e37288.json` |\n',
      'another full head on the next line':
      '\n| `evidence/run1-39043849411.json` | log |\n| head | `6959ced4c327ebb800cf6d463a049e4066e37288` |\n',
      'a path with a slash-bounded run and another head':
      '\nSee `evidence/39043849411/6959ced4.json`.\n'}
for nm, x in sm.items():
    ctrl('N-smuggle: %s' % nm, '-', '1ab0', app('829', x), 'append %r' % x,
         dict(bO10='pass', bR13='fail', pO10='fail', pR13='fail'))
bnd = '\n| `evidence/run1-39043849411.json` | `%s6959ced4c327ebb800cf6d463a049e4066e37288` |\n' % ('0' * 24)
ctrl('B-boundary: another head as the last 40 digits of a 64-hex word', 'b', '1ab0', app('829', bnd), 'append %r' % bnd,
     dict(bO10='pass', bR13='fail', pO10='pass', pR13='pass'))


l69 = TXT['831'].split('\n')[68]
bA = repl('831', 69, l69 + ' sha256 `%s`.' % HEX64)
ctrl('BC-a genuine digest beside the citation passes', '+', 'e684', bA, ':69 += %r' % (' sha256 `%s`.' % HEX64),
     dict(bO10='pass', bR13='pass', pO10='pass', pR13='pass'))
bB = repl('831', 69, '`evidence/run1-38450187534.json` sha256 `%se684897da41b1c3d066b880194c9beb87a19b7ad`.' % ('0' * 24))
ctrl('BC-b embedded file name plus digest cannot establish the citation', '-', 'e684', bB, ':69 -> %r' % bB.split('\n')[68],
     dict(bO10='pass', bR13='pass', pO10='fail', pR13='fail'))
bC = repl('831', 69, l69 + ' head `febfe5e2…`, sha256 `%s`.' % HEX64)
ctrl('BC-c conflicting free-standing head beside a digest fails', '-', 'e684', bC,
     ':69 += %r' % (' head `febfe5e2…`, sha256 `%s`.' % HEX64), dict(bO10='fail', bR13='fail', pO10='fail', pR13='fail'))


def v(st):
    return 'pass' if st[0] in ('pending', 'eligible', 'cited') else 'fail'


rows, bad = [], 0
pv, ph, preason = pins(OBJ['objects'])
print('CN-1 pins on the real manifest: labels valid %s, pins hold %s %s' % (pv, ph, preason or ''))
for c in C:
    oid, run, which, rl = T[c['k']]
    setroot(which, c['text'])
    texts = {PATH[which]: c['text'].split('\n')}
    L = texts[PATH[which]]
    got, why = {}, {}
    if c['o7'] is None:
        s = base_o10(oid, run, PATH[which]); got['bO10'], why['bO10'] = v(s), s[1] if s[0] == 'FAIL' else s[0]
        s = real_o10(oid, run, PATH[which]); got['pO10'], why['pO10'] = v(s), s[1]
    else:
        e = cite(oid, c['o7'])
        objs = OBJ['objects']
        if c['label'] is not None:
            e['tranche'] = c['label']
            objs = [e if x['oid'] == oid else x for x in OBJ['objects']]
        f = base_o7(e, texts); got['bO7'], why['bO7'] = ('fail', f[0]) if f else ('pass', 'cited')
        s = real_o7(e, texts, objs if c['label'] is not None else [e if x['oid'] == oid else x for x in OBJ['objects']])
        got['pO7'], why['pO7'] = v(s), s[1]
    if run in RIDHEAD or True:
        if c['o7'] is None or c['r13map'] is not None:
            s = base_r13(run, oid, PATH[which], rl, c['r13map']); got['bR13'], why['bR13'] = v(s), s[1] if s[0] == 'FAIL' else s[0]
            s = real_r13(run, oid, PATH[which], rl, c['r13map']); got['pR13'], why['pR13'] = v(s), s[1] if s[0] == 'FAIL' else s[0]
    sha = hashlib.sha256(c['text'].encode()).hexdigest()
    mism = [k for k, x in c['expect'].items() if got.get(k) != x]
    bad += bool(mism)
    rows.append(dict(name=c['name'], kind=c['kind'], target=oid[:8] + '/' + run, record=which, edit=c['edit'],
                     fixture_sha256=sha, expect=c['expect'], got=got, why=why, mismatch=mism))
    print('%s %-78s %s%s' % ('OK ' if not mism else 'MISMATCH', c['name'][:78],
                             ' '.join('%s=%s' % (k, got.get(k, '-')) for k in ('bO10', 'bO7', 'bR13', 'pO10', 'pO7', 'pR13')
                                      if k in got), '' if not mism else '  expected %s' % c['expect']))
    for k in sorted(got):
        print('      %-5s %s' % (k, json.dumps(why[k], default=str)[:180]))

# legacy tranche-2 positive control on the real tree (root = the worktree, read-only)
ROOT = WT
leg = ENT['0004afc9360117ba61523b72854de1aaf63705f0']
texts = {}
for c in leg['cited']:
    f = c['location'].rpartition(':')[0]
    texts[f] = open(os.path.join(WT, f), encoding='utf-8').read().split('\n')
f = base_o7(leg, texts)
s = real_o7(leg, texts, OBJ['objects'])
c0 = leg['cited'][0]
f0, _, n0 = c0['location'].rpartition(':')
info = full_rule(leg['oid'], texts[f0], int(n0))
lm = [] if (not f and v(s) == 'pass') else ['legacy']
bad += bool(lm)
print('%s P-legacy tranche-2 run citation %s at %s: base O7 %s; proposed (pinned legacy, token rule) %s; '
      'for information, the lifecycle rule on that line: %s' % ('OK ' if not lm else 'MISMATCH', leg['oid'][:8],
                                                                c0['location'], 'pass' if not f else f[0], v(s), info))
rows.append(dict(name='P-legacy tranche-2 run citation (real tree)', kind='+', target=leg['oid'][:8],
                 location=c0['location'], got={'bO7': 'pass' if not f else 'fail', 'pO7': v(s)},
                 info_lifecycle_rule_on_line=info, mismatch=lm))
shutil.rmtree(os.path.join(RF, 'fx-root'), ignore_errors=True)
json.dump(rows, open(os.path.join(OUTD, 'cn3_real.json'), 'w'), indent=1, default=str)
print('controls: %d, mismatches: %d' % (len(rows), bad))
sys.exit(1 if bad else 0)
