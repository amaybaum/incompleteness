"""Act 41 surface rendering: fills the edit ledger's templates from measured values and splices them into D41's files.

render(template, values)   -- `{slot}` and `[[text if true | text if false : flag]]`
apply_ledger(values)       -- {path: new file contents} for every path the ledger touches
values_from_measurements(meas) -- the slot dict from a measurements.json object {"production", "independent", "hulls"}

Numbers are written in words below one hundred and in digits from one hundred; a set of integers is written
`{1, −1}`, elements in the order given, digits, with the Unicode minus; a list of strings (the maximal flats) is written
comma-separated, with the Unicode minus. Only the selected branch of a selector
is rendered, so a slot that appears only in the unselected branch need not be measured.

Run as a script, it renders the ledger with the values measured at D41 (schema41.md; hull.bijection assumed true) and
writes each resulting file to rendered/<path> beside this file.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, 'ledger41.json')
REPO = '/home/user/incompleteness'
D41 = '78ea3c39004e97aad027ee6153051c6d372bdd55'

SLOT = re.compile(r'\{([a-z][A-Za-z0-9_]*\.[A-Za-z0-9_]+)\}')
SELECTOR = re.compile(r'\[\[(.*?)\|(.*?):\s*([a-z][A-Za-z0-9_]*\.[A-Za-z0-9_]+)\s*\]\]', re.S)
MINUS = '−'

_ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
         'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
_TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# the values measured at D41 (schema41.md), for orientation only; hull.bijection is assumed true
D41_VALUES = {
    'sig.partitions': 20, 'sig.per_form': 10, 'sig.p44': 5, 'sig.p82': 2, 'sig.p28': 3, 'sig.alignments': 976,
    'sig.classes_full': 70, 'sig.classes_tfree': 140, 'sig.porbits_full': 10, 'sig.porbits_tfree': 20,
    'sig.strict_eq_relaxed': True, 'sig.sorted_partitions': 18, 'sig.sorted_porbits': 9,
    'hull.params': 31168, 'hull.sorted_params': 492, 'hull.distinct_mat': 3896, 'hull.distinct_gauge': 3896,
    'hull.bijection': True, 'hull.dims': [14], 'hull.dF_ok': True, 'hull.span': 49, 'hull.W_in': 0,
    'p.partitions': 2, 'p.p44': 0, 'p.p82': 0, 'p.p28': 1, 'p.alignments': 128,
    'w.exclusive': True, 'w.exc_strict': [1], 'w.exc_relaxed': [1, -1], 'w.at1': 20, 'w.m1_strict': 2,
    'w.m1_relaxed': 20,
    'e.exc_strict': [1, -1], 'e.exc_relaxed': [1, -1], 'e.m1': 4, 'e.m1_k4_exchanged': True, 'e.sig_only_at_1': True,
    'h3.candidates': 46, 'h3.nonempty': 43, 'h3.strict_eq_relaxed': True, 'h3.flats': 21, 'h3.noncoord': 4,
    'h3.five_faces': True, 'h3.at_one': 20, 'h3.at_mone': 4, 'h3.sorted_nonempty': 30,
    'p.no_44_82': True, 'e.exc_is_pm1': True,
    'h3.maximal': ['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1'],
}


def number(n):
    """words below one hundred, digits from one hundred"""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('not an integer: %r' % (n,))
    if n < 0:
        return MINUS + number(-n)
    if n >= 100:
        return str(n)
    if n < 20:
        return _ONES[n]
    t, u = divmod(n, 10)
    return _TENS[t] + ('' if u == 0 else '-' + _ONES[u])


def element(x):
    if isinstance(x, bool) or not isinstance(x, int):
        raise TypeError('set element not an integer: %r' % (x,))
    return (MINUS + str(-x)) if x < 0 else str(x)


def value_text(name, v):
    if isinstance(v, bool):
        raise TypeError('slot {%s} holds a boolean; booleans are read only by selectors' % name)
    if isinstance(v, int):
        return number(v)
    if isinstance(v, (list, tuple, set, frozenset)) and v and all(isinstance(x, str) for x in v):
        return ', '.join(x.replace('-', MINUS) for x in v)   # rendered strings, e.g. the maximal flats
    if isinstance(v, (list, tuple, set, frozenset)):
        return '{' + ', '.join(element(x) for x in v) + '}'
    if isinstance(v, str):
        return v
    raise TypeError('slot {%s}: unsupported value %r' % (name, v))


def render(template, values):
    """fill `[[a | b : flag]]` (a when the boolean flag holds, else b; branches stripped of outer whitespace), then
    `{slot}`; a missing value or a non-boolean flag raises"""
    def sel(m):
        a, b, flag = m.group(1), m.group(2), m.group(3)
        if flag not in values:
            raise KeyError('flag %s not measured' % flag)
        if not isinstance(values[flag], bool):
            raise TypeError('flag %s is not a boolean' % flag)
        return (a if values[flag] else b).strip()
    out = SELECTOR.sub(sel, template)

    def slot(m):
        name = m.group(1)
        if name not in values:
            raise KeyError('slot %s not measured' % name)
        return value_text(name, values[name])
    return SLOT.sub(slot, out)


# ---------------------------------------------------------------- measurements.json -> slots
PROBE_LOGS = os.path.join(os.path.dirname(HERE), 'probes')
# the hull census object with the D41 values (schema41.md), used until run_hulls.log prints its object
HULLS_D41_STUB = {'params': 31168, 'sorted_params': 492, 'distinct_mat': 3896, 'distinct_gauge': 3896, 'bijection': True,
                  'dims': [14], 'dF_ok': True, 'span': 49, 'W_in': 0}
P_CASES = ('P = Pu(u60)', 'Pu(u5)')


def _unit(flat):
    """'u1 = 1' -> 1, 'u1 = -1' -> -1; any other flat stays its string"""
    m = re.fullmatch(r'u1 = (-?\d+)', flat)
    return int(m.group(1)) if m else flat


def _unit_set(flats):
    xs = [_unit(f) for f in flats]
    ints = sorted((x for x in xs if isinstance(x, int)), reverse=True)
    rest = sorted(x for x in xs if not isinstance(x, int))
    if rest:
        raise ValueError('exceptional set with points other than integer units: %r' % flats)
    return ints


def _by(entries, orient=None, shape=None):
    return [x for x in entries if (orient is None or x[0] == orient) and (shape is None or list(x[1]) == list(shape))]


def _per_orientation(entries, shape=None):
    col, row = len(_by(entries, 'column', shape)), len(_by(entries, 'row', shape))
    if col != row:
        raise ValueError('column and row counts differ (%d, %d)' % (col, row))
    return col


def _canon(entries):
    return sorted(json.dumps(x, sort_keys=True) for x in entries)


def values_from_measurements(meas):
    """the slot dict of schema41.md from a measurements.json object {"production": ..., "independent": ..., "hulls": ...};
    each entry of a partition-structure list is [orientation, [m, n], blocks, row classes, valid alignments]"""
    pr, ind, hu = meas['production'], meas['independent'], meas['hulls']
    cases = pr['cases']
    # the two paths must agree at every named test case and notion before any value is read
    if set(cases) != set(ind['cases']) or any(_canon(cases[c][n]) != _canon(ind['cases'][c][n])
                                              for c in cases for n in ('strict', 'relaxed')):
        raise ValueError('the production and independent paths disagree')
    v = {}
    ss, sr = pr['sig']['strict'], pr['sig']['relaxed']
    cen = ss['census']
    v['sig.partitions'] = len(cen)
    v['sig.per_form'] = _per_orientation(cen)
    v['sig.p44'], v['sig.p82'], v['sig.p28'] = (_per_orientation(cen, s) for s in ((4, 4), (8, 2), (2, 8)))
    v['sig.alignments'] = sum(x[4] for x in cen)
    for k in ('classes_full', 'classes_tfree', 'porbits_full', 'porbits_tfree'):
        v['sig.' + k] = ss[k]
    v['sig.strict_eq_relaxed'] = _canon(cen) == _canon(sr['census']) and all(
        ss[k] == sr[k] for k in ('classes_full', 'classes_tfree', 'porbits_full', 'porbits_tfree', 'triples'))
    v['sig.sorted_partitions'] = pr['sig_sorted']['partitions']
    v['sig.sorted_porbits'] = pr['sig_sorted']['porbits_full']
    for k, src in (('params', 'params'), ('sorted_params', 'sorted_params'), ('distinct_mat', 'distinct_mat'),
                   ('distinct_gauge', 'distinct_gauge'), ('bijection', 'bijection'), ('dims', 'dims'), ('dF_ok', 'dF_ok'),
                   ('span', 'span'), ('W_in', 'W_in')):
        v['hull.' + k] = hu[src]
    pst = [cases[c]['strict'] for c in P_CASES]
    if len(pst[0]) != len(pst[1]):
        raise ValueError('p.partitions: P and Pu(u5) differ')
    v['p.partitions'] = len(pst[0])
    v['p.p44'], v['p.p82'], v['p.p28'] = (_per_orientation(pst[0], s) for s in ((4, 4), (8, 2), (2, 8)))
    v['p.alignments'] = sum(x[4] for x in _by(pst[0], 'column', (2, 8)))
    v['p.no_44_82'] = all(not _by(cases[c][n], None, s) for c in P_CASES for n in ('strict', 'relaxed') for s in ((4, 4), (8, 2)))
    w = pr['w']
    v['w.exclusive'] = w['exclusive']
    v['w.exc_strict'], v['w.exc_relaxed'] = _unit_set(w['strict']['exceptional']), _unit_set(w['relaxed']['exceptional'])
    v['w.at1'], v['w.m1_strict'], v['w.m1_relaxed'] = len(w['strict']['at1']), len(w['strict']['atm1']), len(w['relaxed']['atm1'])
    e = pr['e']
    v['e.exc_strict'], v['e.exc_relaxed'] = _unit_set(e['strict']['exceptional']), _unit_set(e['relaxed']['exceptional'])
    v['e.exc_is_pm1'] = v['e.exc_strict'] == [1, -1] and v['e.exc_relaxed'] == [1, -1]
    if len(e['strict']['atm1']) != len(e['relaxed']['atm1']):
        raise ValueError('e.m1: strict and relaxed counts differ')
    v['e.m1'] = len(e['strict']['atm1'])
    v['e.m1_k4_exchanged'], v['e.sig_only_at_1'] = e['m1_k4_exchanged'], e['sig_only_at_1']
    h = pr['h3']
    for k in ('candidates', 'nonempty', 'strict_eq_relaxed', 'flats', 'five_faces'):
        v['h3.' + k] = h[k]
    v['h3.noncoord'] = len(h['noncoord'])
    v['h3.maximal'] = list(h['maximal'])
    v['h3.at_one'], v['h3.at_mone'] = len(h['at_one']), len(h['at_mone'])
    # h3.sorted_nonempty (act 40's recorded 30) is carried by no measured object and is used by no template
    return v


def measurements_from_logs(logdir=PROBE_LOGS):
    """the measurements.json object as the probes print it; hulls from the stub until run_hulls.log carries its object"""
    def read(fn, tag):
        f = os.path.join(logdir, fn)
        if not os.path.exists(f):
            return None
        for line in open(f, encoding='utf-8'):
            if line.startswith('A41-MEASUREMENTS %s ' % tag):
                return json.loads(line[len('A41-MEASUREMENTS %s ' % tag):])
        return None
    hulls = read('run_hulls.log', 'hulls')
    return {'production': read('run_prod.log', 'production'), 'independent': read('run_indep.log', 'independent'),
            'hulls': hulls if hulls is not None else dict(HULLS_D41_STUB)}, hulls is None


def d41_blob(path, repo=REPO):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (D41, path)], capture_output=True,
                          check=True).stdout.decode('utf-8')


def load_ledger(path=LEDGER):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def spans(ledger, blobs):
    """(path -> sorted [(start, end, entry)]), each old occurring exactly once in D41's blob, spans disjoint"""
    out = {}
    for e in ledger:
        text = blobs[e['path']]
        n = text.count(e['old'])
        if n != 1:
            raise ValueError('%s: old occurs %d times in %s at D41' % (e['id'], n, e['path']))
        s = text.index(e['old'])
        out.setdefault(e['path'], []).append((s, s + len(e['old']), e))
    for path, lst in out.items():
        lst.sort(key=lambda x: x[0])
        for (s1, e1, a), (s2, e2, b) in zip(lst, lst[1:]):
            if s2 < e1:
                raise ValueError('%s and %s overlap in %s' % (a['id'], b['id'], path))
    return out


def apply_ledger(values, ledger=None, blobs=None, repo=REPO):
    """the new contents of every path the ledger touches: each entry's new text rendered from values and spliced
    over its span of D41's blob"""
    ledger = load_ledger() if ledger is None else ledger
    if blobs is None:
        blobs = {p: d41_blob(p, repo) for p in sorted(set(e['path'] for e in ledger))}
    result = {}
    for path, lst in spans(ledger, blobs).items():
        text, pieces, pos = blobs[path], [], 0
        for s, t, e in lst:
            pieces.append(text[pos:s]); pieces.append(render(e['new'], values)); pos = t
        pieces.append(text[pos:])
        result[path] = ''.join(pieces)
    return result


def main():
    out_root = os.path.join(HERE, 'rendered')
    files = apply_ledger(D41_VALUES)
    for path, text in sorted(files.items()):
        dest = os.path.join(out_root, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'w', encoding='utf-8') as f:
            f.write(text)
        print('rendered', path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
