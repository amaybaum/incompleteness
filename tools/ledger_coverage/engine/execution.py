"""Operation C: a candidate is exactly the scientific base plus the ledger; tree roles H, M, X, C, L (sec. 13)."""
import ast
import difflib
import re
import warnings

from . import outcome as oc
from . import reconcile as rc
from . import segments as sg
from . import util
from .gitobj import Unresolvable, on_first_parent_chain


def comment_strip(text):
    """Source with nested block comments /- -/ and line comments -- removed."""
    out, i, depth, n = [], 0, 0, len(text)
    while i < n:
        if text.startswith('/-', i):
            depth += 1
            i += 2
            continue
        if depth and text.startswith('-/', i):
            depth -= 1
            i += 2
            continue
        if depth:
            i += 1
            continue
        if text.startswith('--', i):
            j = text.find('\n', i)
            i = n if j < 0 else j
            continue
        out.append(text[i])
        i += 1
    return ''.join(out)


def py_literals(src, min_len):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            tree = ast.parse(src)
    except SyntaxError:
        return []
    return [(n.lineno, ' '.join(n.value.split())) for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) >= min_len]


def norm(s):
    return ' '.join(s.split())


_literal_cache = {}


class Execution:
    def __init__(self, ctx, H, X, ledger, delegation=None, M=None, L=None, C=None, side_classes=None,
                 reconciliations=(), evidence=None, records_after_freeze=(), pin_ok=()):
        self.ctx = ctx
        self.repo = ctx.repo
        self.H, self.X, self.M, self.L, self.C = H, X, M, L, C or X
        self.compositions = []
        self.ledger = ledger
        self.delegation = delegation
        self.side_classes = side_classes or []
        self.reconciliations = list(reconciliations)
        self.evidence = evidence or {}
        self.items = []
        self.checks = []
        self.side_changes = []
        self.pin_ok = list(pin_ok)
        self.records_after_freeze = list(records_after_freeze)
        self.freeze = None
        # amendment r4 (O-9): {'F', 'cpath', 'authorized'}, set by an operation that evaluates M with F (A.4, A.7)
        self.record_dir_args = None
        self.rd = None

    def item(self, obligation, cls, subject, fp=None, **kw):
        self.items.append(oc.make_item(obligation, cls, subject, kw.pop('segment', None), fp, **kw))

    # ---- integrity: base and preconditions at H ----
    def integrity(self):
        led = self.ledger
        if led['base'] != self.H:
            raise oc.Stop(oc.error, 'SCIENTIFIC_BASE_MISMATCH', 'the ledger base is not the scientific base')
        bad = []
        for path, f in led['files'].items():
            d = self.repo.read(self.H, path)
            if d is None or util.sha256(d) != f['base_sha256']:
                bad.append('%s: base_sha256 differs at H' % path)
        for sp in led['splices']:
            d = self.repo.read(self.H, sp['file']) or b''
            if util.sha256(d[sp['start']:sp['end']]) != sp['old_sha256']:
                bad.append('%s: old_sha256 does not match its span at H' % sp['id'])
        sids = {sp['id'] for sp in led['splices']}
        for r in led['retained']:
            if r['id'] in sids:
                bad.append('%s: retained edit has a splice' % r['id'])
        if bad:
            raise oc.Stop(oc.error, 'LEDGER_INTEGRITY', bad[0], {'problems': bad[:50], 'count': len(bad)})
        self.checks.append({'name': 'preconditions-at-H', 'holds': True, 'splices': len(led['splices']),
                            'edit_units': len(led.get('edit_units', []))})

    # ---- candidate X ----
    def candidate(self, commit=None, parent=None):
        X = commit or self.X
        parent = parent or self.H
        ps = self.repo.parents(X)
        if ps != [parent]:
            self.item('RET', 'candidate-parent', X, {'parents': ps}, detail={'parents': ps, 'expected': parent})
        led = self.ledger
        hp, xp = self.repo.paths(self.H), self.repo.paths(X)
        deleg_paths = set(self.delegation.paths()) if self.delegation else set()
        record_prefixes = self.delegation.record_prefixes() if self.delegation else []
        by_file = {}
        for sp in led['splices']:
            by_file.setdefault(sp['file'], []).append(sp)
        conform = 0
        for path in sorted(set(hp) | set(xp)):
            if hp.get(path) == xp.get(path):
                continue
            if path in led['files']:
                if self.delegation and self.delegation.owns_ledgered(path):
                    continue
                h = self.repo.read(self.H, path) or b''
                expected = sg.apply_splices(h, by_file.get(path, []))
                x = self.repo.read(X, path)
                if x != expected:
                    self.item('RET', 'unauthorized-edit', path, {'expected_sha256': util.sha256(expected),
                                                                 'actual_sha256': util.sha256(x or b'')},
                              file=path, detail={'ranges': sg.diff_ranges(expected, x or b'')})
                else:
                    conform += 1
                continue
            if path in deleg_paths or any(path.startswith(p) for p in record_prefixes):
                continue
            self.item('RET', 'unauthorized-change', path, {'h': hp.get(path), 'x': xp.get(path)}, file=path)
        unchanged_ledgered = [p for p in led['files'] if hp.get(p) == xp.get(p)]
        for p in unchanged_ledgered:
            if by_file.get(p):
                self.item('RET', 'unauthorized-edit', p, {'expected': 'splices applied', 'actual': hp.get(p)},
                          file=p)
        self.checks.append({'name': 'ledgered-files-conform', 'conforming_changed_files': conform,
                            'ledgered_files': len(led['files'])})
        # splice postconditions: each new at its translated span
        for path, sps in by_file.items():
            x = self.repo.read(X, path) or b''
            ss = sorted(sps, key=lambda s: (s['start'], s['end']))
            for sp in ss:
                t = sg.translate(sp['start'], [o for o in ss if o is not sp])
                if x[t:t + len(sp['new_bytes'])] != sp['new_bytes'] and not \
                        (self.delegation and self.delegation.owns_ledgered(path)):
                    self.item('RET', 'unauthorized-edit', '%s@%s' % (sp['id'], path), {'splice': sp['id']},
                              file=path, splice=sp['id'])
        self.retained(X)
        self.mirrors()
        self.lean(X)

    def commits_after(self, chain, F=None):
        """B4: each commit after X on the chain to C, with its parent, classified path by path as X is against
        H: ledgered (H plus the splices), delegated (checked by its class at C) or record (admitted after F);
        anything else fails as unauthorized-change, naming the commit."""
        led = self.ledger
        by_file = {}
        for sp in led['splices']:
            by_file.setdefault(sp['file'], []).append(sp)
        deleg_paths = set(self.delegation.paths()) if self.delegation else set()
        record_prefixes = self.delegation.record_prefixes() if self.delegation else []
        report = []
        prev = self.X
        for c in chain:
            ps = self.repo.parents(c)
            if ps != [prev]:
                self.item('RET', 'candidate-parent', c, {'c': c, 'parents': ps})
            pp, cp = self.repo.paths(prev), self.repo.paths(c)
            row = {'commit': c, 'paths': []}
            for path in sorted(set(pp) | set(cp)):
                if pp.get(path) == cp.get(path):
                    continue
                cls = None
                if path in led['files']:
                    if self.delegation and self.delegation.owns_ledgered(path):
                        cls = 'delegated'
                    else:
                        want = sg.apply_splices(self.repo.read(self.H, path) or b'', by_file.get(path, []))
                        cls = 'ledgered' if self.repo.read(c, path) == want else None
                        if cls is None:
                            self.item('RET', 'unauthorized-edit', '%s@%s' % (path, c[:12]), {'commit': c},
                                      file=path, commit=c)
                            row['paths'].append({'path': path, 'class': 'unauthorized-edit'})
                            continue
                elif path in deleg_paths:
                    cls = 'delegated'
                else:
                    for d in record_prefixes:
                        if path.startswith(d + 'execution/') and (F is None or self.repo.blob_id(F, path) is None):
                            cls = 'record'
                if cls is None:
                    self.item('RET', 'unauthorized-change', '%s@%s' % (path, c[:12]), {'commit': c, 'path': path},
                              file=path, commit=c)
                    cls = 'unauthorized-change'
                row['paths'].append({'path': path, 'class': cls})
            report.append(row)
            prev = c
        self.checks.append({'name': 'commits-after-X', 'commits': report})

    def retained(self, X):
        sids = {sp['id'] for sp in self.ledger['splices']}
        for r in self.ledger['retained']:
            ok = r['id'] not in sids and r.get('text') is not None
            if ok:
                h = (self.repo.read(self.H, r['file']) or b'').decode('utf-8', 'replace')
                x = (self.repo.read(X, r['file']) or b'').decode('utf-8', 'replace')
                ok = h.count(r['text']) == 1 and x.count(r['text']) == 1
            if not ok:
                self.item('RET', 'retained-changed', r['id'], {'site': r.get('site_ref')}, file=r.get('file'))

    def mirrors(self):
        sp = {s['id']: s for s in self.ledger['splices']}
        for m in self.ledger['mirrors']:
            a, b = sp.get(m['id']), sp.get(m['mirror_of'])
            if a is None or b is None or a['new_sha256'] != b['new_sha256'] or a['old_sha256'] != b['old_sha256']:
                self.item('RET', 'mirror-mismatch', m['id'], {'mirror_of': m['mirror_of']})

    def lean(self, X):
        for path in self.ledger['files']:
            if not path.endswith('.lean'):
                continue
            h = (self.repo.read(self.H, path) or b'').decode('utf-8', 'replace')
            x = (self.repo.read(X, path) or b'').decode('utf-8', 'replace')
            if comment_strip(h) != comment_strip(x):
                self.item('RET', 'lean-code-change', path, {'h': util.sha256(h), 'x': util.sha256(x)}, file=path)

    # ---- pins ----
    def pins(self, rules, X=None):
        X = X or self.X
        led = self.ledger
        files = [f for f in led['files'] if not f.endswith('.py')]
        before = {f: norm((self.repo.read(self.H, f) or b'').decode('utf-8', 'replace')) for f in files}
        after = {f: norm((self.repo.read(X, f) or b'').decode('utf-8', 'replace')) for f in files}
        grams = set()
        g = max(1, min(20, rules['min_len']))  # invariant: every pinned literal is at least g characters long
        for f in files:
            h = self.repo.read(self.H, f) or b''
            for sp in led['splices']:
                if sp['file'] == f:
                    seg = norm(h[max(0, sp['start'] - 100):sp['end'] + 100].decode('utf-8', 'replace'))
                    for i in range(max(1, len(seg) - g + 1)):
                        grams.add(seg[i:i + g])

        def near_splice(lit):
            # a literal overlapping a splice shares a 20-character window with the text around it
            return any(lit[i:i + g] in grams for i in range(max(1, len(lit) - g + 1)))
        pyfiles = [p for p in self.repo.paths(self.H) if p.endswith('.py')
                   and not p.startswith(tuple(rules['skip_prefixes']))]
        broken = []
        for pf in sorted(pyfiles):
            bid = self.repo.blob_id(self.H, pf)
            key = (bid, rules['min_len'])
            if key not in _literal_cache:
                src = (self.repo.read(self.H, pf) or b'').decode('utf-8', 'replace')
                _literal_cache[key] = py_literals(src, rules['min_len'])
            lits = _literal_cache[key]
            if not lits:
                continue
            changed = self.repo.blob_id(self.H, pf) != self.repo.blob_id(X, pf)
            new_lits = {l for _, l in py_literals((self.repo.read(X, pf) or b'').decode('utf-8', 'replace'),
                                                   rules['min_len'])} if changed else None
            for ln, lit in lits:
                if not near_splice(lit):
                    continue
                for f in files:
                    if lit not in before[f] or lit in after[f]:
                        continue
                    if new_lits is not None and lit not in new_lits:
                        continue
                    if any(pf == a and lit.startswith(b) for a, b in [(o['file'], o['prefix'])
                                                                      for o in rules['ok'] + self.pin_ok]):
                        continue
                    broken.append((pf, ln, lit, f))
        for pf, ln, lit, f in broken:
            self.item('RET', 'pin-broken', '%s:%d' % (pf, ln), {'literal': lit, 'target': f}, file=pf, line=ln,
                      target=f)
        for o in self.pin_ok:
            if self.freeze is None or not self.repo.is_ancestor(o.get('recorded_at', ''), self.freeze):
                self.item('RET', 'pin-broken', 'pin-ok %s' % o['file'], {'entry': o},
                          detail='a pin exemption recorded after the freeze')
        # updated pins must occur in their targets (the selection rules live in the ledger adapter)
        for g in led.get('guard_pins', []):
            pf = g['file']
            old = {l for _, l in py_literals((self.repo.read(self.H, pf) or b'').decode('utf-8', 'replace'),
                                             rules['min_len'])}
            new = [l for _, l in py_literals((self.repo.read(X, pf) or b'').decode('utf-8', 'replace'),
                                             rules['min_len']) if l not in old]
            mine = [l for l in new if any(x in l for x in g['pieces'])]
            if not mine:
                self.item('RET', 'pin-target-missing', g['id'], {'file': pf}, detail='no new literal found')
            for t in g.get('targets') or []:
                tt = norm((self.repo.read(X, t) or b'').decode('utf-8', 'replace'))
                for l in mine:
                    if l not in tt:
                        self.item('RET', 'pin-target-missing', '%s->%s' % (g['id'], t), {'literal': l})
        self.checks.append({'name': 'pins', 'python_files': len(pyfiles), 'broken': len(broken)})

    # ---- integration base M and landing L ----
    def main_role(self, ledgered_or_corpus, record_tree=None, record_path=None):
        M = self.M
        if not on_first_parent_chain(self.repo, self.H, M):
            raise oc.Stop(oc.error, 'MAIN_NOT_DESCENDANT', 'H is not on the first-parent chain of M')
        if record_tree is not None and self.repo.tree_id(M, record_path) != record_tree:
            raise oc.Stop(oc.error, 'RECORD_TREE_MISMATCH', 'the frozen record tree differs at M')
        hp, mp = self.repo.paths(self.H), self.repo.paths(M)
        chain = []
        c = M
        while c != self.H:
            chain.append(c)
            c = self.repo.parents(c)[0]
        chain.reverse()
        self.rd = rd = self._record_directory(ledgered_or_corpus)
        if rd is not None and rd.active:
            # A.5: an independent, mandatory invariant, issued whatever any other route decides about the path
            for path, why in sorted(rd.unequal.items()):
                self.item('MAIN', 'side-change-unclassified', path,
                          {'f': rd.entry(path, rd.F), 'm': rd.entry(path, M)}, file=path, why=why,
                          rule='record-directory completeness')
        for path in sorted(set(hp) | set(mp)):
            if hp.get(path) == mp.get(path):
                continue
            made = None
            prev = self.H
            for c in chain:
                if self.repo.blob_id(c, path) != self.repo.blob_id(prev, path):
                    made = c
                prev = c
            entry = {'path': path, 'h': hp.get(path), 'm': mp.get(path), 'commit': made}
            if path in ledgered_or_corpus:
                rec, ev = self._reconciled(path)
                entry['class'] = 'base-drift'
                entry['reconciled'] = bool(rec)
                entry['record_conditions'] = ev
                if not rec:
                    self.item('MAIN', 'base-drift', path, {'h': hp.get(path), 'm': mp.get(path)}, file=path,
                              commit=made, failed_conditions=[e['failed'] for e in ev])
                for e in ev:
                    if 'R12' in e['failed']:
                        self.item('RECORD', 'record-invalid', '%s:%s' % ((e.get('record') or {}).get('path'), path),
                                  {'why': 'R12'}, detail='the record states decisions it changes on X (R12)')
            else:
                cls, why = self._side_class(path)
                entry['class'] = cls
                if cls == rc.RECORD_DIRECTORY:
                    entry['record_directory'] = dict(rd.equal[path])
                if cls is None:
                    if rd is not None and rd.active:
                        entry['why'] = why
                    # an unequal path of the record directory already carries A.5's item
                    if not (rd is not None and rd.active and path in rd.unequal):
                        self.item('MAIN', 'side-change-unclassified', path, {'h': hp.get(path), 'm': mp.get(path)},
                                  file=path, commit=made, why=why)
            self.side_changes.append(entry)

    def _record_directory(self, ledgered_or_corpus):
        """Amendment r4, A.4 and A.7: the record-directory context, built once per M role when the operation
        evaluates M with F; None otherwise (the rule and A.5 are then not evaluated)."""
        a = self.record_dir_args
        if not a or not a.get('F') or not a.get('cpath'):
            return None
        in_corpus = getattr(self.ctx, 'in_corpus', None) or (lambda p: False)
        ledgered = set(self.ledger['files']) | set(ledgered_or_corpus)
        return rc.RecordDirectory(self.repo, self.H, a['F'], self.M, a['cpath'], a['authorized'], ledgered, in_corpus,
                                  self.side_classes)

    def _side_class(self, path):
        """S3: a path matches a class only if its blob at M equals the class pin; amendment r4, A.6."""
        return rc.side_class(self.repo, self.M, path, self.side_classes, getattr(self, 'record_refs', {}), self.rd)

    def _reconciled(self, path):
        """(entry, evaluations): the record entry that applies (every condition holds, S5), or None."""
        evs = []
        for r in self.reconciliations:
            for e in r.get('paths', []):
                if e.get('path') != path:
                    continue
                ev = rc.evaluate(self.repo, self.ctx, self.H, self.M, self.X, self.ledger, r, e, self.side_classes,
                                 getattr(self, 'record_refs', {}), self.rd)
                ev['record'] = r.get('_ref')
                evs.append(ev)
                if not ev['failed']:
                    return dict(e, _ref=r.get('_ref')), evs
        return None, evs

    def landing(self, generated_rx=None):
        L, M, C = self.L, self.M, self.C
        ps = self.repo.parents(L)
        if len(ps) != 2 or ps[1] != C:
            self.item('MAIN', 'landing-parents', L, {'parents': ps}, detail={'parents': ps})
            return
        if ps[0] != M:
            self.item('MAIN', 'landing-first-parent-not-M', L, {'first': ps[0], 'm': M})
            return
        hp, mp, cp, lp = (self.repo.paths(x) for x in (self.H, M, C, L))
        led = self.ledger
        by_file = {}
        for sp in led['splices']:
            by_file.setdefault(sp['file'], []).append(sp)
        for path in sorted(set(hp) | set(mp) | set(cp) | set(lp)):
            h, m, c, l = hp.get(path), mp.get(path), cp.get(path), lp.get(path)
            dX, dM = c != h, m != h
            if not dX and not dM:
                if l != h:
                    self.item('MAIN', 'landing-extra-change', path, {'l': l, 'h': h}, file=path)
            elif dX and not dM:
                if l != c:
                    self.item('MAIN', 'landing-extra-change' if l != h else 'landing-extra-change', path,
                              {'l': l, 'c': c}, file=path, detail='the landing does not carry the execution change')
            elif dM and not dX:
                if l != m:
                    self.item('MAIN', 'landing-drops-main-change', path, {'l': l, 'm': m}, file=path)
            else:
                if c == m:
                    if l != m:
                        self.item('MAIN', 'landing-extra-change', path, {'l': l, 'm': m}, file=path)
                    continue
                if path in led['files']:
                    # S6: the composition is evaluated for every path, with or without a record; a record's l is
                    # only a prediction checked against it
                    comp, _ = rc.compose(self.repo, self.H, M, path, by_file.get(path, []))
                    comp_id = rc.blob_id_of(comp) if comp is not None else None
                    self.compositions.append({'path': path, 'composed_blob': comp_id, 'l': l})
                    recs = [(r, e) for r in self.reconciliations for e in r.get('paths', []) if e.get('path') == path]
                    for r, e in recs:
                        if e.get('l') != comp_id:
                            self.item('RECORD', 'record-invalid', '%s:%s' % ((r.get('_ref') or {}).get('path'), path),
                                      {'l': e.get('l'), 'composed': comp_id}, file=path,
                                      detail='the record\'s l differs from the composition (the record\'s R7)')
                    if comp is not None and l is not None and l == comp_id:
                        continue
                if generated_rx is not None and generated_rx.search(path):
                    self.item('MAIN', 'delegated-evidence-missing', path, {'l': l}, file=path,
                              detail='generated artifact conflict: regenerate from the landing sources')
                    continue
                self.item('MAIN', 'landing-conflict-unresolved', path, {'l': l, 'm': m, 'c': c}, file=path)

    def translate_onto_main(self, path, splices):
        """M's bytes with C's splices applied at M-translated offsets, each old_sha256 re-verified."""
        h = self.repo.read(self.H, path) or b''
        m = self.repo.read(self.M, path) or b''
        hl, ml = h.split(b'\n'), m.split(b'\n')
        hs, ms = [0], [0]
        for x in hl:
            hs.append(hs[-1] + len(x) + 1)
        for x in ml:
            ms.append(ms[-1] + len(x) + 1)
        blocks = difflib.SequenceMatcher(None, hl, ml, autojunk=False).get_matching_blocks()
        out = []
        for sp in splices:
            mapped = None
            for a, b, n in blocks:
                if n and hs[a] <= sp['start'] and sp['end'] <= hs[a + n]:
                    mapped = ms[b] + (sp['start'] - hs[a])
                    break
            if mapped is None:
                return None
            ln = sp['end'] - sp['start']
            if util.sha256(m[mapped:mapped + ln]) != sp['old_sha256']:
                return None
            out.append(dict(sp, start=mapped, end=mapped + ln))
        return sg.apply_splices(m, out)


def compose_landing(repo, H, M, C, ledger, overlay):
    """An in-memory landing built by the composition rule (for the RT-L controls); never committed."""
    hp, mp, cp = repo.paths(H), repo.paths(M), repo.paths(C)
    changes = {}
    ex = Execution.__new__(Execution)
    ex.repo, ex.H, ex.M = repo, H, M
    by_file = {}
    for sp in ledger['splices']:
        by_file.setdefault(sp['file'], []).append(sp)
    for path in sorted(set(hp) | set(mp) | set(cp)):
        h, m, c = hp.get(path), mp.get(path), cp.get(path)
        if c != h and m == h:
            changes[path] = repo.read(C, path)
        elif c != h and m != h and c != m:
            want = ex.translate_onto_main(path, by_file.get(path, [])) if path in ledger['files'] else None
            changes[path] = want if want is not None else repo.read(C, path)
    return overlay.derive(M, changes, parents=[M, C], subject='in-memory landing')
