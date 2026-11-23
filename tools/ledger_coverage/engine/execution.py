"""Operation C: a candidate is exactly the scientific base plus the ledger; tree roles H, M, X, C, L (sec. 13)."""
import ast
import difflib
import re
import warnings

from . import outcome as oc
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
        retained = {r['id'] for r in led['retained']}
        for e in led.get('edits', []):
            t = (self.repo.read(self.H, e['file']) or b'').decode('utf-8', 'replace')
            if t.count(e['old']) != 1:
                bad.append('%s: old text does not occur exactly once at H' % e['id'])
            if e['id'] in retained:
                if e['id'] in sids:
                    bad.append('%s: retained edit has a splice' % e['id'])
            elif e['id'] not in sids:
                bad.append('%s: edit maps to no splice' % e['id'])
        eids = {e['id'] for e in led.get('edits', [])}
        for s in sids - eids if eids else ():
            bad.append('%s: splice maps to no edit' % s)
        if bad:
            raise oc.Stop(oc.error, 'LEDGER_INTEGRITY', bad[0], {'problems': bad[:50], 'count': len(bad)})
        self.checks.append({'name': 'preconditions-at-H', 'holds': True, 'splices': len(led['splices']),
                            'edits': len(led.get('edits', []))})

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
        diff_paths = {p for p in set(hp) | set(xp) if hp.get(p) != xp.get(p)}
        for r in self.reconciliations:
            for e in r.get('paths', []):
                if e.get('path') in diff_paths:
                    self.item('RECORD', 'record-invalid', 'reconciliation %s' % e.get('path'), {'path': e.get('path')},
                              detail='a reconciliation record never changes a decision of op C on the candidate')
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
        for f in files:
            h = self.repo.read(self.H, f) or b''
            for sp in led['splices']:
                if sp['file'] == f:
                    seg = norm(h[max(0, sp['start'] - 100):sp['end'] + 100].decode('utf-8', 'replace'))
                    for i in range(max(1, len(seg) - 19)):
                        grams.add(seg[i:i + 20])

        def near_splice(lit):
            # a literal overlapping a splice shares a 20-character window with the text around it
            return any(lit[i:i + 20] in grams for i in range(max(1, len(lit) - 19)))
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
        # updated pins must occur in their targets
        for e in led.get('edits', []):
            if e.get('kind') != 'guard-pin' or e.get('pin_note') in ('message', 'comment'):
                continue
            pf = e['file']
            old = {l for _, l in py_literals((self.repo.read(self.H, pf) or b'').decode('utf-8', 'replace'), 20)}
            new = [l for _, l in py_literals((self.repo.read(X, pf) or b'').decode('utf-8', 'replace'), 20)
                   if l not in old]
            pieces = [norm(x) for x in re.split(r'[\'"]', e['new'])]
            pieces = [x for x in pieces if len(x) >= 12 and not x.startswith(('ok', 'in ', '#'))]
            mine = [l for l in new if any(x in l for x in pieces)]
            if not mine:
                self.item('RET', 'pin-target-missing', e['id'], {'file': pf}, detail='no new literal found')
            for t in e.get('targets') or []:
                tt = norm((self.repo.read(X, t) or b'').decode('utf-8', 'replace'))
                for l in mine:
                    if l not in tt:
                        self.item('RET', 'pin-target-missing', '%s->%s' % (e['id'], t), {'literal': l})
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
                rec = self._reconciled(path)
                entry['class'] = 'base-drift'
                entry['reconciled'] = bool(rec)
                if not rec:
                    self.item('MAIN', 'base-drift', path, {'h': hp.get(path), 'm': mp.get(path)}, file=path,
                              commit=made)
            else:
                cls = self._side_class(path)
                entry['class'] = cls
                if cls is None:
                    self.item('MAIN', 'side-change-unclassified', path, {'h': hp.get(path), 'm': mp.get(path)},
                              file=path, commit=made)
            self.side_changes.append(entry)

    def _side_class(self, path):
        for c in self.side_classes:
            for p in c.get('paths', []):
                if path == p:
                    return c['id']
            for p in c.get('prefixes', []):
                if path.startswith(p):
                    return c['id']
        return None

    def _reconciled(self, path):
        for r in self.reconciliations:
            for e in r.get('paths', []):
                if e.get('path') == path and e.get('m') == self.repo.blob_id(self.M, path):
                    return e
        return None

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
                rec = self._reconciled(path)
                if rec and rec.get('l') == l:
                    continue
                if path in led['files']:
                    want = self.translate_onto_main(path, by_file.get(path, []))
                    if want is not None and l is not None and self.repo.read(L, path) == want:
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
