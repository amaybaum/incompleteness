"""Reconciliation records (sec. 13.3, schema oi-reconciliation/1) and side-change classes (sec. 13.1, S3, S7).

The tool evaluates every checkable condition of a reconciliation record itself, from git objects (S5): the
ledger binding (R13, first), the commit list (R1), the blob at M (R2), uniqueness and translation (R3-R5), the
composed blob and the candidate blob (R6-R8), the protected bytes (R9), the other ledgered files (R10), the
classified side changes (R11) and an empty `changes_decisions_on_X` (R12). The composition itself is computed
independently of any record (S6).
"""
from . import segments as sg
from . import util
from .gitobj import Unresolvable, blob_id_of, on_first_parent_chain

condition_order = ['R13', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12']


def occurrences(buf, needle):
    """Overlapping occurrences of `needle` in `buf`."""
    out = []
    if not needle:
        return out
    i = buf.find(needle)
    while i != -1:
        out.append(i)
        i = buf.find(needle, i + 1)
    return out


def binding(led, path):
    """Canonical sha256 of the path's files entry, its splice list and its edit-list entries, as the ledger and the
    edit list hold them (sorted keys, no whitespace, utf-8)."""
    raw = led.get('raw') or {}
    fe = (raw.get('files') or {}).get(path) if isinstance(raw.get('files'), dict) else None
    sl = [s for s in raw.get('splices', []) if s.get('file') == path]
    el = [e for e in raw.get('edits', []) if e.get('file') == path]
    return {'ledger_base': led.get('base'),
            'files_entry_sha256': None if fe is None else util.sha256(util.canonical(fe)),
            'splices_sha256': util.sha256(util.canonical(sl)),
            'edit_records_sha256': util.sha256(util.canonical(el))}


# ---- side-change classes ---------------------------------------------------------------------------------------

def class_pins(cls):
    """[(path, git_blob, blob_sha256)] a class binds; a prefix never classifies by itself."""
    out = []
    for p in cls.get('pins', []):
        out.append((p.get('path'), p.get('git_blob'), p.get('blob_sha256')))
    if cls.get('paths') and ('blob_sha256' in cls or 'git_blob' in cls):
        for p in cls['paths']:
            out.append((p, cls.get('git_blob'), cls.get('blob_sha256')))
    return out


def classify_side(repo, M, path, classes, record_refs):
    """(class id, None) when the path's blob at M equals a class pin for it; (None, why) otherwise. A class record
    itself is classified by the configuration's pin of it (record_refs: {path: blob_sha256})."""
    data = repo.read(M, path)
    bid = repo.blob_id(M, path)
    sha = util.sha256(data) if data is not None else None
    if path in record_refs:
        return ('class-record', None) if record_refs[path] == sha else (None, 'the class record differs from its pin')
    why = 'no class lists the path'
    for c in classes:
        for p, gb, bs in class_pins(c):
            if p != path:
                continue
            if (gb is None or gb == bid) and bs == sha and bs is not None:
                return c['id'], None
            why = 'the blob at M differs from the pin of class %s' % c['id']
        if why == 'no class lists the path' and any(path.startswith(x) for x in c.get('prefixes', [])):
            why = 'under a prefix of class %s but not listed with its blob' % c['id']
    return None, why


def duplicate_class_ids(class_docs):
    seen, dup = set(), []
    for d in class_docs:
        for c in (d or {}).get('classes', []):
            if c.get('id') in seen:
                dup.append(c.get('id'))
            seen.add(c.get('id'))
    return dup


# ---- the record's conditions ----------------------------------------------------------------------------------

def compose(repo, H, M, path, splices):
    """M's bytes with the splices applied at M-translated offsets (each old bytes unique at M, old_sha256
    re-verified); (bytes, [(splice, start_M, end_M)]) or (None, why)."""
    m = repo.read(M, path) or b''
    h = repo.read(H, path) or b''
    placed = []
    for sp in sorted(splices, key=lambda s: s['start']):
        old = h[sp['start']:sp['end']]
        if util.sha256(old) != sp['old_sha256']:
            return None, '%s: old bytes at H do not hash to old_sha256' % sp['id']
        occ = occurrences(m, old)
        if len(occ) != 1:
            return None, '%s: old bytes occur %d times at M' % (sp['id'], len(occ))
        placed.append((sp, occ[0], occ[0] + len(old)))
    out, pos = [], 0
    for sp, a, b in sorted(placed, key=lambda x: x[1]):
        if a < pos:
            return None, 'translated splices overlap at M'
        out.append(m[pos:a])
        out.append(sp['new_bytes'])
        pos = b
    out.append(m[pos:])
    return b''.join(out), placed


def evaluate(repo, ctx, H, M, X, led, rdoc, entry, classes, record_refs):
    """Each condition of one path entry of a reconciliation record, evaluated from git objects. Returns
    {'holds': {R: bool}, 'failed': [R...], 'composed_blob', 'composed_sha256'}."""
    path = entry.get('path')
    res = {}
    # R13 first
    b = binding(led, path)
    want = dict(rdoc.get('ledger_binding') or {})
    want.update(entry.get('ledger_binding') or {})
    res['R13'] = b['ledger_base'] == H == want.get('ledger_base') and b['files_entry_sha256'] is not None and \
        all(b[k] == want.get(k) for k in ('files_entry_sha256', 'splices_sha256', 'edit_records_sha256'))
    # R1
    changes = []
    try:
        on_chain = on_first_parent_chain(repo, H, M)
    except Unresolvable:
        on_chain = False
    if on_chain:
        chain, c = [], M
        while c != H:
            chain.append(c)
            c = repo.parents(c)[0]
        prev = H
        for c in reversed(chain):
            if repo.blob_id(c, path) != repo.blob_id(prev, path):
                changes.append(c)
            prev = c
        res['R1'] = changes == list(entry.get('side_change_commits') or [])
    else:
        res['R1'] = False
    m = repo.read(M, path)
    res['R2'] = m is not None and repo.blob_id(M, path) == entry.get('m') and util.sha256(m) == entry.get('m_sha256')
    h = repo.read(H, path) or b''
    m = m or b''
    sps = [s for s in led['splices'] if s['file'] == path]
    rsp = {s.get('id'): s for s in entry.get('splices', [])}
    r3 = r4 = r5 = bool(sps)
    common = 0
    while common < min(len(h), len(m)) and h[common] == m[common]:
        common += 1
    for sp in sps:
        old = h[sp['start']:sp['end']]
        r = rsp.get(sp['id'], {})
        r3 = r3 and occurrences(h, old) == [sp['start']] and util.sha256(old) == sp['old_sha256'] and \
            r.get('start_H') == sp['start'] and r.get('end_H') == sp['end']
        om = occurrences(m, old)
        r4 = r4 and len(om) == 1 and om[0] == r.get('start_M') and util.sha256(m[om[0]:om[0] + len(old)]) == \
            sp['old_sha256']
        if r.get('translation') == 'identity':
            r5 = r5 and common >= sp['end'] and r.get('start_M') == sp['start']
        else:
            delta = r.get('start_M', -1) - sp['start']
            r5 = r5 and bool(om) and om[0] - sp['start'] == delta
    res['R3'], res['R4'], res['R5'] = r3, r4, r5
    comp, placed = compose(repo, H, M, path, sps)
    x = repo.read(X, path)
    if comp is None:
        res.update(R6=False, R7=False, R9=False)
    else:
        img_ok, shift = True, 0
        for sp, a, e in sorted(placed, key=lambda q: q[1]):
            at = a + shift
            img_ok = img_ok and comp[at:at + len(sp['new_bytes'])] == sp['new_bytes'] and \
                util.sha256(sp['new_bytes']) == sp['new_sha256'] and \
                rsp.get(sp['id'], {}).get('new_sha256') == sp['new_sha256'] and \
                (x or b'')[sp['start']:sp['start'] + len(sp['new_bytes'])] == sp['new_bytes']
            shift += len(sp['new_bytes']) - (e - a)
        res['R6'] = img_ok
        res['R7'] = blob_id_of(comp) == entry.get('l') and util.sha256(comp) == entry.get('l_sha256')
        delta = sum(len(sp['new_bytes']) - (e - a) for sp, a, e in placed)
        last_end = max(e for _, _, e in placed) if placed else 0
        r9 = comp[last_end + delta:] == m[last_end:]
        for pr in entry.get('protected', []):
            a, e = pr.get('start_M'), pr.get('end_M')
            if not isinstance(a, int) or not isinstance(e, int):
                r9 = False
                continue
            seg = m[a:e]
            r9 = r9 and util.sha256(seg) == pr.get('sha256') and len(occurrences(m, seg)) == 1 and \
                len(occurrences(comp, seg)) == 1 and a >= last_end and comp[a + delta:e + delta] == seg
        res['R9'] = r9
    fe = (led.get('files') or {}).get(path) if isinstance(led.get('files'), dict) else None
    res['R8'] = x is not None and repo.blob_id(X, path) == entry.get('x') and util.sha256(x) == entry.get('x_sha256') \
        and fe is not None and fe.get('expected_sha256') == util.sha256(x)
    r10 = True
    for f, v in (led.get('files') or {}).items() if isinstance(led.get('files'), dict) else []:
        if f == path:
            continue
        if repo.blob_id(H, f) != repo.blob_id(M, f) or util.sha256(repo.read(M, f) or b'') != v.get('base_sha256'):
            r10 = False
    res['R10'] = r10
    r11 = True
    hp, mp = repo.paths(H), repo.paths(M)
    for p in sorted(set(hp) | set(mp)):
        if p == path or hp.get(p) == mp.get(p):
            continue
        if ctx is not None and ctx.in_corpus(p):
            r11 = False
            continue
        cid, _ = classify_side(repo, M, p, classes, record_refs)
        if cid is None:
            r11 = False
    res['R11'] = r11
    res['R12'] = not rdoc.get('changes_decisions_on_X')
    failed = [k for k in condition_order if not res.get(k)]
    return {'path': path, 'holds': res, 'failed': failed,
            'composed_blob': blob_id_of(comp) if comp is not None else None,
            'composed_sha256': util.sha256(comp) if comp is not None else None,
            'side_change_commits': changes}


def draft(repo, ctx, H, M, X, led, path, protected=(), classes=(), record_refs=None):
    """A draft reconciliation record for one path, every value derived from git objects (for writers and
    controls). A draft is never admitted without its review chain (sec. 6.3)."""
    b = binding(led, path)
    sps = [s for s in led['splices'] if s['file'] == path]
    h = repo.read(H, path) or b''
    m = repo.read(M, path) or b''
    x = repo.read(X, path)
    common = 0
    while common < min(len(h), len(m)) and h[common] == m[common]:
        common += 1
    comp, placed = compose(repo, H, M, path, sps)
    if comp is None:
        return None
    rsp = []
    for sp, a, e in placed:
        rsp.append({'id': sp['id'], 'start_H': sp['start'], 'end_H': sp['end'], 'start_M': a, 'end_M': e,
                    'translation': 'identity' if a == sp['start'] and common >= sp['end'] else 'shift',
                    'new_sha256': sp['new_sha256']})
    prot = []
    for a, e in protected:
        prot.append({'start_M': a, 'end_M': e, 'sha256': util.sha256(m[a:e])})
    entry = {'path': path, 'm': repo.blob_id(M, path), 'm_sha256': util.sha256(m),
             'x': repo.blob_id(X, path), 'x_sha256': util.sha256(x or b''),
             'l': blob_id_of(comp), 'l_sha256': util.sha256(comp), 'splices': rsp, 'protected': prot}
    ev = evaluate(repo, ctx, H, M, X, led, {'ledger_binding': b}, dict(entry, side_change_commits=[]),
                  list(classes), record_refs or {})
    entry['side_change_commits'] = ev['side_change_commits']
    return {'schema': 'oi-reconciliation/1', 'record_id': 'draft-%s' % path, 'supersedes': None,
            'ledger_binding': b, 'paths': [entry], 'changes_decisions_on_X': []}
