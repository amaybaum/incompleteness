"""Reconciliation records (sec. 13.3, schema oi-reconciliation/1) and side-change classes (sec. 13.1, S3, S7).

The tool evaluates every checkable condition of a reconciliation record itself, from git objects (S5): the
ledger binding (RC13, first), the commit list (RC1), the blob at M (RC2), uniqueness and translation (RC3-RC5), the
composed blob and the candidate blob (RC6-RC8), the protected bytes (RC9), the other ledgered files (RC10), the
classified side changes (RC11) and an empty `changes_decisions_on_X` (RC12). The composition itself is computed
independently of any record (S6).
"""
from . import outcome as oc
from . import segments as sg
from . import util
from .gitobj import Unresolvable, blob_id_of, on_first_parent_chain, regular_modes, tree_entry

condition_order = ['RC13', 'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8', 'RC9', 'RC10', 'RC11', 'RC12',
                   'RC14']
# design r6 amendment 3: the per-path binding and scientific effect change the record's shape (oi-reconciliation/2)
reconciliation_schemas = ('oi-reconciliation/1', 'oi-reconciliation/2')
local_conditions = ('RC13', 'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8', 'RC9', 'RC12', 'RC14')
# paths a check executes (a script, a Lean file, a workflow), whose scientific effect names the check re-run at l
executed_suffixes = ('.py', '.lean', '.yml', '.yaml', '.sh')


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
    cid, why, _ = classify_side_named(repo, M, path, classes, record_refs)
    return cid, why


def classify_side_named(repo, M, path, classes, record_refs):
    # classify_side with a third value, `named`: true when a class pin names the path or the path is a class record
    # the configuration pins, whether or not it matches (amendment r4, A.6 rows 1 and 2); false otherwise (row 3).
    #
    # R6.PUR.12, R6.RDIR.7, R6.TREE.8: the entry's mode is read before any byte, inside the record directory or outside
    # it; a symbolic link or submodule is never read as file content and never raises: it is unclassified with the
    # reason `not a regular file` (REVIEW_REQUIRED side-change-unclassified).
    e = repo.entries(M).get(path)
    if e is not None and e[0] not in regular_modes:
        return None, 'not a regular file', False
    data = repo.read(M, path)
    bid = repo.blob_id(M, path)
    sha = util.sha256(data) if data is not None else None
    if path in record_refs:
        return (('class-record', None, True) if record_refs[path] == sha else
                (None, 'the class record differs from its pin', True))
    why = 'no class lists the path'
    named = False
    for c in classes:
        for p, gb, bs in class_pins(c):
            if p != path:
                continue
            named = True
            if (gb is None or gb == bid) and bs == sha and bs is not None:
                return c['id'], None, True
            why = 'the blob at M differs from the pin of class %s' % c['id']
        if why == 'no class lists the path' and any(path.startswith(x.rstrip('/') + '/') for x in c.get('prefixes', [])):
            why = 'under a prefix of class %s but not listed with its blob' % c['id']
    return None, why, named


# ---- the plan's record directory on M (design amendment r4, O-9) ------------------------------------------------

record_directory_class = 'record-directory'


def inside(d, path):
    """A.2: the one membership predicate of the record-directory rule; `path` is inside `d` when it begins with `d`
    followed by `/`."""
    return path.startswith(d + '/')


def clean_path(path):
    """A.6: no component of the path is empty, `.` or `..`."""
    return all(c not in ('', '.', '..') for c in path.split('/'))


class RecordDirectory:
    """The context of the record-directory rule for one run (A.2-A.5): built once by an operation that evaluates M
    with F, and shared by the M role and the RC11 condition of every reconciliation record it evaluates (A.7).

    `authorized` is the tool's tuple of authorized record directories (A.3); `ledgered` the ledgered paths;
    `in_corpus` the configuration's corpus predicate; `classes` the run's admitted side-change classes from both routes
    (the configuration's class records and those admitted through --classify)."""

    def __init__(self, repo, H, F, M, cpath, authorized, ledgered, in_corpus, classes):
        self.repo, self.H, self.F, self.M = repo, H, F, M
        self.d = cpath.rsplit('/', 1)[0] if '/' in cpath else ''
        self.authorized = self.d in tuple(authorized)
        self.active = False
        self.state = None
        self.equal = {}
        self.unequal = {}
        # A.8: the outcome of each guard. Dir2-Dir5: True held, False failed (the run then stops), None not evaluated;
        # authority: whether the directory is authorized (False with the rule inactive, or with the authority ERROR)
        self.conditions = {'authority': None, 'Dir2': None, 'Dir3': None, 'Dir4': None, 'Dir5': None}
        # Dir5: the reserved class id, over the admitted class set of both routes
        if any(isinstance(c, dict) and c.get('id') == record_directory_class for c in classes):
            self._stop('Dir5', 'a side-change class uses the class id reserved for the record-directory rule')
        self.conditions['Dir5'] = True
        self.conditions['authority'] = self.authorized
        e_h = [p for p in repo.entries(H) if inside(self.d, p)]
        e_m = {p: e for p, e in repo.entries(M).items() if inside(self.d, p)}
        if not self.authorized:
            if not e_m:
                self.state = 'inactive: unauthorized, absent on M'
                return
            if e_h:
                self.state = 'inactive: unauthorized, present at H'
                return
            self._stop('authority', 'the configuration\'s directory is not an authorized record directory, is absent '
                                    'at H and appears on M')
        # Dir2: the directory is introduced after H
        if e_h:
            self._stop('Dir2', 'the record directory holds entries at H: %s' % e_h[0])
        self.conditions['Dir2'] = True
        e_f = {p: e for p, e in repo.entries(F).items() if inside(self.d, p)}
        # Dir3: no ledgered, corpus, class-prefix or workflow path inside the directory, at F or at M
        prefixes = [x.rstrip('/') + '/' for c in classes if isinstance(c, dict)
                    for x in c.get('prefixes', []) if isinstance(x, str) and x]
        for p in sorted(set(e_f) | set(e_m)):
            if p in ledgered or in_corpus(p) or any(p.startswith(x) for x in prefixes) or p.startswith('.github/'):
                self._stop('Dir3', 'a ledgered, corpus, class-prefix or workflow path lies in the record directory: %s'
                           % p)
        self.conditions['Dir3'] = True
        # Dir4: F holds the configuration and the file of record pins in the directory
        prereg = self.d + '/' + 'PREREG.md'
        if (e_f.get(cpath) or (None,))[0] not in regular_modes or (e_f.get(prereg) or (None,))[0] not in regular_modes:
            self._stop('Dir4', 'F does not hold the configuration and its file of record pins in the record directory')
        self.conditions['Dir4'] = True
        self.active = True
        self.state = 'active'
        self._complete(e_f, e_m)

    def _stop(self, cond, msg):
        self.conditions[cond] = False
        raise oc.Stop(oc.error, 'CONFIG_INCONSISTENT', 'record directory (%s): %s' % ('directory not admitted' if cond == 'authority' else cond, msg),
                      {'directory': self.d, 'condition': cond, 'conditions': dict(self.conditions)})

    def _complete(self, e_f, e_m):
        """A.5: the entries inside the directory at F and at M compared path by path over their union; entry types
        are checked before any bytes are read."""
        for p in sorted(set(e_f) | set(e_m)):
            if p not in e_m:
                self.unequal[p] = 'absent at M'
                continue
            if p not in e_f:
                self.unequal[p] = 'absent at F'
                continue
            (mf, of), (mm, om) = e_f[p], e_m[p]
            if mf not in regular_modes or mm not in regular_modes:
                self.unequal[p] = 'not a regular file'
                continue
            if mf != mm or of != om:
                self.unequal[p] = 'differs from F'
                continue
            # both entries are regular files (checked above), so the byte reads cannot meet a non-regular entry
            sf, sm = util.sha256(self.repo.read(self.F, p) or b''), util.sha256(self.repo.read(self.M, p) or b'')
            if sf != sm:
                self.unequal[p] = 'differs from F'
                continue
            self.equal[p] = {'mode': mm, 'f': of, 'm': om, 'f_sha256': sf, 'm_sha256': sm}

    def entry(self, path, which):
        e = self.repo.entries(which).get(path)
        return {'mode': e[0], 'id': e[1]} if e else None

    def summary(self):
        reasons = {}
        for why in self.unequal.values():
            reasons[why] = reasons.get(why, 0) + 1
        return {'directory': self.d, 'authorized': self.authorized, 'state': self.state,
                'conditions': dict(self.conditions), 'equal': len(self.equal), 'unequal': reasons}


def side_class(repo, M, path, classes, record_refs, rd=None):
    """(class id, why): the one side-change classification of the M role and of RC11 (amendment r4, A.6). Without an
    active record-directory context it is classify_side."""
    active = rd is not None and rd.active
    if active and inside(rd.d, path):
        e = repo.entries(M).get(path)
        if e is not None and e[0] not in regular_modes:
            # a non-regular entry in the directory never reaches the classifier's byte read
            return None, 'not a regular file'
    cid, why, named = classify_side_named(repo, M, path, classes, record_refs)
    if cid is not None or named or not active:
        return cid, why
    if not inside(rd.d, path):
        return None, 'outside the record directory'
    if not clean_path(path):
        return None, 'not a clean path'
    if path in rd.equal:
        return record_directory_class, None
    return None, rd.unequal.get(path, 'differs from F')


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


def ledger_lists(led, path):
    """Whether the ledger lists the path: a files entry, a splice or an edit entry for it."""
    raw = led.get('raw') or {}
    files = led.get('files') if isinstance(led.get('files'), dict) else {}
    return path in files or any(s.get('file') == path for s in led.get('splices', [])) or \
        any(e.get('file') == path for e in (raw.get('edits') or []) if isinstance(e, dict))


def entry_binding(rdoc, entry):
    """The binding an entry states: its own `ledger_binding` (oi-reconciliation/2) with the record's `ledger_base`,
    or the record-level binding of an oi-reconciliation/1 record."""
    if rdoc.get('schema') == 'oi-reconciliation/2':
        want = dict(entry.get('ledger_binding') or {})
        want['ledger_base'] = rdoc.get('ledger_base')
        return want
    want = dict(rdoc.get('ledger_binding') or {})
    want.update(entry.get('ledger_binding') or {})
    return want


def context_windows(h, sps, corpus, sentences=None):
    """[(splice, window start, window end)] at H: the bytes from the start of the first line that overlaps the
    splice's span to the end of the last such line; for a corpus path widened to the lines of the splitter-v2
    sentences that overlap those lines (sentence windows rounded to whole lines). `sentences`: [(first, last)] line
    numbers (1-based) of the file's sentences at H."""
    starts = [0] + [i + 1 for i, c in enumerate(h) if c == 0x0a]

    def line_of(off):
        lo, hi = 0, len(starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if starts[mid] <= off:
                lo = mid
            else:
                hi = mid - 1
        return lo
    out = []
    for sp in sps:
        a = line_of(sp['start'])
        b = line_of(max(sp['start'], sp['end'] - 1))
        if corpus and sentences:
            changed = True
            while changed:
                changed = False
                for first, last in sentences:
                    if first - 1 <= b and last - 1 >= a and (first - 1 < a or last - 1 > b):
                        a, b = min(a, first - 1), max(b, last - 1)
                        changed = True
        ws = starts[a]
        we = starts[b + 1] if b + 1 < len(starts) else len(h)
        out.append((sp, ws, we))
    return out


def retained_windows(repo, H, led, paths):
    """Read the whole lines containing each retained edit's selected text at the scientific base."""
    windows, base = {}, {}
    for item in led['retained']:
        path = item.get('file')
        if path not in paths:
            continue
        if path not in base:
            base[path] = repo.read(H, path) or b''
        h, text = base[path], item.get('text')
        text = text.encode('utf-8') if isinstance(text, str) else b''
        window = None
        if text and h.count(text) == 1:
            start = h.find(text)
            begin = h.rfind(b'\n', 0, start) + 1
            end = h.find(b'\n', start + len(text) - 1)
            window = h[begin:] if end < 0 else h[begin:end + 1]
        windows.setdefault(path, []).append((item.get('site_ref') or item['id'], window))
    return windows


# design r6 R6.RECON.24 (RC14)
def rc14(h, m, windows, placed, retained_lines):
    """RC14: each window occurs exactly once at M, at the splice's translated offset less its distance
    from the window's start; each retained site's line occurs exactly once at M. Returns [problem]."""
    at = {sp['id']: a for sp, a, _e in (placed or [])}
    out = []
    for sp, ws, we in windows:
        win = h[ws:we]
        occ = occurrences(m, win)
        want = at.get(sp['id'])
        if want is None:
            out.append('%s: the splice has no translated offset at M' % sp['id'])
        elif occ != [want - (sp['start'] - ws)]:
            out.append('%s: its context window occurs %d times at M, not once at the translated offset'
                       % (sp['id'], len(occ)))
    for site, line in retained_lines:
        if line is None:
            out.append('%s: the retained site text does not occur exactly once at the scientific base' % site)
            continue
        whole = [p for p in occurrences(m, line) if (not p or m[p - 1:p] == b'\n')
                 and (line.endswith(b'\n') or p + len(line) == len(m))]
        if len(whole) != 1:
            out.append('%s: the retained site line does not occur exactly once at M' % site)
    return out


def path_conflicts(repo, ctx, H, M, path, led, retained_lines=()):
    """The conflicts RC14 finds for a path, from git objects alone (no record is read): its category is 2 when there
    is one, or when a splice's old bytes do not occur once at M."""
    sps = [s for s in led['splices'] if s['file'] == path]
    h = repo.read(H, path) or b''
    m = repo.read(M, path) or b''
    comp, placed = compose(repo, H, M, path, sps)
    if comp is None:
        return ['%s' % placed]
    corpus = ctx is not None and ctx.in_corpus(path)
    return rc14(h, m, context_windows(h, sps, corpus, file_sentences(ctx, H, path) if corpus else None), placed,
                retained_lines)


def file_sentences(ctx, commit, path):
    try:
        return [(a, b) for _s, a, b in ctx.sentences(commit, path)]
    except Exception:  # a context without a splitter (controls) reads lines only
        return None


def ledger_edits(led):
    raw = led.get('raw') or {}
    return {e.get('id'): e for e in (raw.get('edits') or []) if isinstance(e, dict) and e.get('id')}


# design r6 R6.RECON.25 and R6.RECON.26: the key of a finding
def edit_key(led, edit_id):
    """The key of an edit in the frozen plan: the canonical sha256 of its edit-list entry.
    Kept apart so that a later amendment can change how a finding is keyed."""
    e = ledger_edits(led).get(edit_id)
    return util.sha256(util.canonical(e)) if e is not None else None


# design r6 R6.RECON.25
def scientific_problems(entry, led):
    """The form of an entry's scientific_effect: present and non-empty; conclusions are edit ids of the
    ledger or none; assessment and method non-empty; verdict no-effect or invalidates, the latter with invalidated
    edit ids whose sha256 equals the edit-list entry's; for an executed path, method names the composed blob l."""
    se = entry.get('scientific_effect')
    if not isinstance(se, dict) or not se:
        return ['no scientific_effect']
    out = []
    edits = ledger_edits(led)
    con = se.get('conclusions')
    if con != 'none' and not (isinstance(con, list) and con and all(isinstance(c, str) and c in edits for c in con)):
        out.append('conclusions name no edit id of the ledger')
    for k in ('assessment', 'method'):
        if not (isinstance(se.get(k), str) and se[k].strip()):
            out.append('%s is empty' % k)
    v = se.get('verdict')
    if v not in ('no-effect', 'invalidates'):
        out.append('no verdict')
    if v == 'invalidates':
        inv = se.get('invalidated')
        if not (isinstance(inv, list) and inv):
            out.append('invalidates without an invalidated edit')
        else:
            from .category3 import read_invalidated
            for x in inv:
                eid, esha, _target = read_invalidated(x)
                if not isinstance(x, dict) or edit_key(led, eid) is None or edit_key(led, eid) != esha:
                    out.append('an invalidated sha256 differs from the edit-list entry')
                    break
    path = entry.get('path') or ''
    if path.endswith(executed_suffixes) and entry.get('l') and entry['l'] not in (se.get('method') or ''):
        out.append('the method names no check re-run at the composed blob')
    return out


def evaluate(repo, ctx, H, M, X, led, rdoc, entry, classes, record_refs, rd=None, covered=None, retained_lines=()):
    """Each condition of one path entry of a reconciliation record, evaluated from git objects. Returns
    {'holds': {R: bool}, 'failed': [R...], 'composed_blob', 'composed_sha256'}. `rd` is the run's record-directory
    context (amendment r4, A.7), shared with the M role; None outside its scope. `covered`: the paths covered by the
    run's locally valid entries (amendment 3: RC10 and RC11 are read over them); None reads only the entry's path."""
    path = entry.get('path')
    res = {}
    listed = ledger_lists(led, path)
    # RC13 first
    b = binding(led, path)
    want = entry_binding(rdoc, entry)
    if listed:
        res['RC13'] = b['ledger_base'] == H == want.get('ledger_base') and b['files_entry_sha256'] is not None and \
            all(b[k] == want.get(k) for k in ('files_entry_sha256', 'splices_sha256', 'edit_records_sha256'))
    else:
        # a corpus path the ledger does not list: the three values are null (R6.RECON.5)
        res['RC13'] = b['ledger_base'] == H == want.get('ledger_base') and \
            all(want.get(k, 0) is None for k in ('files_entry_sha256', 'splices_sha256', 'edit_records_sha256'))
    # RC1
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
            if tree_entry(repo, c, path) != tree_entry(repo, prev, path):
                changes.append(c)
            prev = c
        res['RC1'] = changes == list(entry.get('side_change_commits') or [])
    else:
        res['RC1'] = False
    m = repo.read(M, path)
    res['RC2'] = m is not None and repo.blob_id(M, path) == entry.get('m') and util.sha256(m) == entry.get('m_sha256')
    h = repo.read(H, path) or b''
    m = m or b''
    sps = [s for s in led['splices'] if s['file'] == path]
    rsp = {s.get('id'): s for s in entry.get('splices', [])}
    x = repo.read(X, path)
    fe = (led.get('files') or {}).get(path) if isinstance(led.get('files'), dict) else None
    comp, placed = compose(repo, H, M, path, sps)
    if not listed:
        # R6.RECON.3, R6.RECON.8: an entry without splices for a corpus path the ledger does not list
        empty = not sps and not entry.get('splices')
        res.update(RC3=empty, RC4=empty, RC5=empty, RC6=empty)
        res['RC7'] = entry.get('l') == repo.blob_id(M, path) and entry.get('l_sha256') == util.sha256(m)
        res['RC8'] = entry.get('x') == repo.blob_id(H, path) and fe is None and \
            entry.get('x_sha256') == util.sha256(repo.read(H, path) or b'')
        res['RC9'] = res['RC7']
        res['RC14'] = not rc14(h, m, [], [], retained_lines)
    else:
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
        res['RC3'], res['RC4'], res['RC5'] = r3, r4, r5
        if comp is None:
            res.update(RC6=False, RC7=False, RC9=False)
        else:
            x_offsets, x_shift = {}, 0
            for sp in sorted(sps, key=lambda s: s['start']):
                x_offsets[sp['id']] = sp['start'] + x_shift
                x_shift += len(sp['new_bytes']) - (sp['end'] - sp['start'])
            img_ok, shift = True, 0
            for sp, a, e in sorted(placed, key=lambda q: q[1]):
                at = a + shift
                at_x = x_offsets[sp['id']]
                img_ok = img_ok and comp[at:at + len(sp['new_bytes'])] == sp['new_bytes'] and \
                    util.sha256(sp['new_bytes']) == sp['new_sha256'] and \
                    rsp.get(sp['id'], {}).get('new_sha256') == sp['new_sha256'] and \
                    (x or b'')[at_x:at_x + len(sp['new_bytes'])] == sp['new_bytes']
                shift += len(sp['new_bytes']) - (e - a)
            res['RC6'] = img_ok
            res['RC7'] = blob_id_of(comp) == entry.get('l') and util.sha256(comp) == entry.get('l_sha256')
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
            res['RC9'] = r9
        res['RC8'] = x is not None and repo.blob_id(X, path) == entry.get('x') and \
            util.sha256(x) == entry.get('x_sha256') and fe is not None and fe.get('expected_sha256') == util.sha256(x)
        corpus = ctx is not None and ctx.in_corpus(path)
        conflicts = rc14(h, m, context_windows(h, sps, corpus, file_sentences(ctx, H, path) if corpus else None),
                         placed if comp is not None else [], retained_lines) if comp is not None else ['no composition']
        res['RC14'] = not conflicts
    cov = set(covered or ()) | {path}
    r10, r10_named = True, []
    for f, v in (led.get('files') or {}).items() if isinstance(led.get('files'), dict) else []:
        if f in cov:
            continue
        if repo.blob_id(H, f) != repo.blob_id(M, f) or util.sha256(repo.read(M, f) or b'') != v.get('base_sha256'):
            r10 = False
            r10_named.append(f)
    res['RC10'] = r10
    r11 = True
    hp, mp = repo.paths(H), repo.paths(M)
    for p in sorted(set(hp) | set(mp)):
        if p in cov or hp.get(p) == mp.get(p):
            continue
        if ctx is not None and ctx.in_corpus(p):
            r11 = False
            continue
        cid, _ = side_class(repo, M, p, classes, record_refs, rd)
        if cid is None:
            r11 = False
    # A.5 is a mandatory invariant: an unequal entry of the record directory fails RC11 whatever classifies it
    if rd is not None and rd.active and rd.unequal:
        r11 = False
    res['RC11'] = r11
    res['RC12'] = not rdoc.get('changes_decisions_on_X')
    failed = [k for k in condition_order if not res.get(k)]
    out = {'path': path, 'holds': res, 'failed': failed,
           'composed_blob': blob_id_of(comp) if comp is not None else None,
           'composed_sha256': util.sha256(comp) if comp is not None else None,
           'side_change_commits': changes}
    if r10_named:
        out['rc10_files'] = sorted(r10_named)
    return out


# design r6 R6.RECON.4, R6.RECON.15, R6.RECON.16, R6.RECON.22, R6.RECON.25
def assess(repo, ctx, H, M, X, led, records, classes, record_refs, rd, paths, retained=None):
    """The run-level reconciliation assessment: every entry of every record for the drifted paths is evaluated locally (RC1-RC9, RC12-RC14); RC10 and RC11 are
    then read over the paths the locally valid entries cover. An entry applies when every condition holds and its
    scientific_effect has the reviewed verdict no-effect (an oi-reconciliation/1 record carries none and never
    applies). Returns {path: {'evaluations', 'applies', 'form'}}."""
    retained = retained or {}
    first = {}
    for r in records:
        for e in r.get('paths', []):
            p = e.get('path')
            if p not in paths:
                continue
            ev = evaluate(repo, ctx, H, M, X, led, r, e, classes, record_refs, rd,
                          retained_lines=retained.get(p, ()))
            first.setdefault(p, []).append((r, e, ev))
    covered = {p for p, lst in first.items() for _r, _e, ev in lst
               if all(ev['holds'].get(k) for k in local_conditions)}
    out = {}
    for p in paths:
        evs, applies, forms = [], None, []
        for r, e, _ev in first.get(p, []):
            ev = evaluate(repo, ctx, H, M, X, led, r, e, classes, record_refs, rd, covered=covered - {p},
                          retained_lines=retained.get(p, ()))
            ev['record'] = r.get('_ref')
            form = scientific_problems(e, led) if r.get('schema') == 'oi-reconciliation/2' else \
                ['schema oi-reconciliation/1 carries no scientific_effect']
            ev['scientific_effect'] = {'problems': form, 'verdict': (e.get('scientific_effect') or {}).get('verdict')}
            forms.append((r, e, form))
            evs.append(ev)
            if applies is None and not ev['failed'] and not form and ev['scientific_effect']['verdict'] == 'no-effect':
                applies = dict(e, _ref=r.get('_ref'))
        out[p] = {'evaluations': evs, 'applies': applies, 'form': forms}
    return out


def draft(repo, ctx, H, M, X, led, path, protected=(), classes=(), record_refs=None, scientific_effect=None):
    """A draft reconciliation record (oi-reconciliation/2) for one path, every value derived from git objects (for
    writers and controls). A draft is never admitted without its review chain (sec. 6.3). The scientific effect is the
    writer's statement, never derived: without one the draft carries an empty statement, which fails its form."""
    b = binding(led, path)
    listed = ledger_lists(led, path)
    sps = [s for s in led['splices'] if s['file'] == path]
    h = repo.read(H, path) or b''
    m = repo.read(M, path) or b''
    x = repo.read(X, path)
    common = 0
    while common < min(len(h), len(m)) and h[common] == m[common]:
        common += 1
    if listed:
        comp, placed = compose(repo, H, M, path, sps)
        if comp is None:
            return None
    else:
        comp, placed = m, []
    rsp = []
    for sp, a, e in placed:
        rsp.append({'id': sp['id'], 'start_H': sp['start'], 'end_H': sp['end'], 'start_M': a, 'end_M': e,
                    'translation': 'identity' if a == sp['start'] and common >= sp['end'] else 'shift',
                    'new_sha256': sp['new_sha256']})
    prot = []
    for a, e in protected:
        prot.append({'start_M': a, 'end_M': e, 'sha256': util.sha256(m[a:e])})
    eb = {k: (b[k] if listed else None) for k in ('files_entry_sha256', 'splices_sha256', 'edit_records_sha256')}
    xb = x if listed else (repo.read(H, path) or b'')
    entry = {'path': path, 'ledger_binding': eb,
             'scientific_effect': scientific_effect or {'conclusions': 'none', 'assessment': '', 'method': '',
                                                        'verdict': None},
             'm': repo.blob_id(M, path), 'm_sha256': util.sha256(m),
             'x': repo.blob_id(X if listed else H, path), 'x_sha256': util.sha256(xb or b''),
             'l': blob_id_of(comp), 'l_sha256': util.sha256(comp), 'splices': rsp, 'protected': prot}
    doc = {'schema': 'oi-reconciliation/2', 'record_id': 'draft-%s' % path, 'supersedes': None,
           'ledger_base': b['ledger_base'], 'paths': [entry], 'changes_decisions_on_X': []}
    ev = evaluate(repo, ctx, H, M, X, led, doc, dict(entry, side_change_commits=[]), list(classes), record_refs or {})
    entry['side_change_commits'] = ev['side_change_commits']
    return doc
