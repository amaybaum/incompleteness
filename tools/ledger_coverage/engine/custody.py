"""OBL-29 custody (design c7, adopted with D-1 option (ii), OQ-17, OQ-19 with roles.M as a named field, R6.CUST.8,
R6.CUST.10, OQ-12; OQ-20 declined): the record `oi-obl29-custody/1`, its versions over reachable history, the
completeness of discharge-bearing contexts, and the gate on discharge (R6.CUST.1-10).

The custody path and the bootstrap blob id are the tool's constants (record_authority); the engine names no
retirement. Every object is read through the verified reader; a missing or corrupt object is the reader's
Unresolvable (ERROR). Custody only ever adds conditions: until it is established at effective M no cited discharge
applies (R6.CUST.7, R6.CUST.9).
"""
import json
import posixpath
import re

from . import findings as fd
from . import records as rec
from . import util

schema = 'oi-obl29-custody/1'
config_schema = 'oi-retirement-config/1'
result_schema = 'oi-ledger-coverage/5'
regular = ('100644', '100755')
_hex40 = re.compile(r'[0-9a-f]{40}\Z')
non_evaluating = ('USAGE', 'ERROR', 'VOID', 'INTERNAL')


class Unimplemented(Exception):
    """A part of the adopted design this tool revision does not implement: the run stops with ERROR (fail closed)."""


def _commit(v):
    return isinstance(v, str) and bool(_hex40.match(v))


def _keep_all(_oid):
    return True


# ---- R6.CUST.2 schema -----------------------------------------------------------------------------------------

def parse(data):
    """(doc, problems) of one custody version: canonical JSON of one object, strict parse, exact keys and entries."""
    doc = fd.strict_parse(data)
    if doc is None:
        return None, ['not a strict-parsed JSON object']
    canon = json.dumps(doc, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    out = []
    if canon != data:
        out.append('the bytes are not the canonical JSON of the object (no trailing newline)')
    if set(doc) != {'schema', 'predecessor', 'author', 'entries'}:
        out.append('keys are not exactly schema, predecessor, author, entries')
    if doc.get('schema') != schema:
        out.append('schema is not %s' % schema)
    p = doc.get('predecessor')
    if p is not None and not _commit(p):
        out.append('predecessor is neither a blob id nor null')
    tmp = []
    fd._type_ok('identity', doc.get('author'), 'author', tmp)
    out += tmp
    ents = doc.get('entries')
    if not isinstance(ents, list) or not ents:
        return doc, out + ['entries is not a non-empty array']
    for i, e in enumerate(ents):
        out += ['entries[%d]: %s' % (i, x) for x in entry_problems(e)]
    if not (isinstance(ents[0], dict) and ents[0].get('type') == 'bootstrap'):
        out.append('entries[0] is not the bootstrap entry')
    if sum(1 for e in ents if isinstance(e, dict) and e.get('type') == 'bootstrap') != 1:
        out.append('there is not exactly one bootstrap entry')
    return doc, out


def _ref_ok(v):
    tmp = []
    fd.validate(fd.REF, v, 'ref', tmp)
    return not tmp


def entry_problems(e):
    if not isinstance(e, dict):
        return ['not an object']
    t = e.get('type')
    keys = {'bootstrap': {'base'}, 'freeze': {'f', 'config', 'landing'}, 'close': {'f', 'runs'},
            'unfrozen': {'config'}, 'void': {'blob'}}.get(t)
    if keys is None:
        return ['entry type %r is not in the table' % (t,)]
    if set(e) != keys | {'type'}:
        return ['the keys of a %s entry are not exactly %s' % (t, sorted(keys | {'type'}))]
    out = []
    for k in ('base', 'f', 'landing', 'blob'):
        if k in keys and not _commit(e[k]):
            out.append('%s is not a full id' % k)
    if 'config' in keys and not _ref_ok(e['config']):
        out.append('config is not a reference')
    if t == 'close':
        runs = e['runs']
        if not isinstance(runs, list):
            out.append('runs is not an array')
        else:
            for r in runs:
                if not isinstance(r, dict) or set(r) != {'m', 'rev'} or not _commit(r.get('m')) or \
                        not (r.get('rev') is None or _commit(r.get('rev'))):
                    out.append('a run is not exactly {m, rev} with commit ids')
    return out


def item_ids(version, predecessor):
    """R6.CUST.8 review-lint item ids: `entry:<i>` for each index the version adds to its predecessor."""
    n = len((predecessor or {}).get('entries') or []) if predecessor is not None else 1
    return ['entry:%d' % i for i in range(n, len(version.get('entries') or []))]


# ---- the walk over M's history -----------------------------------------------------------------------------------

class History:
    """Every commit reachable from M through any parent, with the custody version at each (R6.CUST.4 Vers(M)), and
    the discharge-bearing configurations in R*(M) (R6.CUST.5 (c4))."""

    def __init__(self, repo, M, path, audits_prefix):
        self.repo, self.M, self.path = repo, M, path
        self.dir = posixpath.dirname(path) + '/'
        self.commits = []
        self.version_at = {}
        self.vers = {}
        seen, stack = set(), [M]
        cache = repo.__dict__.setdefault('_cust_cfg', {})
        info = cache
        self.configs = {}

        def keep_cfg(oid):
            if oid not in info:
                data = repo.read_blob_uncached(oid)
                doc = fd.strict_parse(data)
                info[oid] = None
                if isinstance(doc, dict) and doc.get('schema') == config_schema and any(
                        isinstance(r, dict) and r.get('kind') == 'reassessment' for r in doc.get('records') or []):
                    info[oid] = (util.sha256(data), doc)
            return info[oid] is not None
        keep_cfg_fn = repo.__dict__.setdefault('_cust_keep_cfg', keep_cfg)
        while stack:
            c = stack.pop()
            if c in seen:
                continue
            seen.add(c)
            self.commits.append(c)
            stack.extend(repo.parents(c))
            _k, ents = repo.prefix_entries(c, self.dir, _keep_all)
            got = [o for p, m, o in ents if p == path and m in regular]
            self.version_at[c] = got[0] if got else None
            if got and got[0] not in self.vers:
                self.vers[got[0]] = repo.read_blob_uncached(got[0])
            _k, cents = repo.prefix_entries(c, audits_prefix, keep_cfg_fn)
            for p, m, o in cents:
                sha, doc = info[o]
                self.configs.setdefault((p, sha), doc)
        self.seen = seen

    def reachable(self, c):
        return c in self.seen


def discharge_bearing(doc):
    """Sec. 1: a configuration citing a reassessment whose admission.mode is chain. The configuration schema
    (R6.CFG.4) has no `admission` key; where it is absent the clause cannot be evaluated."""
    adm = doc.get('admission') if isinstance(doc, dict) else None
    if adm is None:
        raise fd.Unsettled('custody sec. 1: "a configuration is discharge-bearing when ... its admission.mode is '
                           '\'chain\'": oi-retirement-config/1 (R6.CFG.4) has no admission key, so a configuration '
                           'citing a reassessment cannot be classed')
    return isinstance(adm, dict) and adm.get('mode') == 'chain'


# ---- the check ---------------------------------------------------------------------------------------------------

class Check:
    def __init__(self, repo, M, run_F, path, boot_blob, cum, audits_prefix, read_pin_table, recon_root):
        self.repo, self.M, self.run_F = repo, M, run_F
        self.path, self.boot = path, boot_blob
        self.cum, self.read_pin_table, self.recon_root = cum, read_pin_table, recon_root
        self.audits_prefix = audits_prefix
        self.problems = []
        self.contexts = []
        self.runs = {}
        self.gate = False

    def fail(self, item, msg):
        self.problems.append((item, msg))

    def run(self, gate=False):
        """The checks of R6.CUST.2-.8 at M (with gate=True, only those R6.CUST.10 names). Returns the report."""
        repo, M = self.repo, self.M
        self.gate = gate
        h = self.h = History(repo, M, self.path, self.audits_prefix)
        vm = h.version_at.get(M)
        report = {'path': self.path, 'version': vm}
        if vm is None:
            self.fail('custody-missing', 'no regular file at the custody path in M\'s tree')
            return self.report(report)
        docs = {}
        bad = set()
        for oid, data in h.vers.items():
            d, probs = parse(data)
            if probs:
                bad.add(oid)
            else:
                docs[oid] = d
        if vm in bad:
            self.fail('custody-schema', 'V_M fails R6.CUST.2: %s' % parse(h.vers[vm])[1][0])
            return self.report(report)
        V = docs[vm]
        # (s1) chain
        chain, cur, seen = [], vm, set()
        while True:
            if cur in seen:
                self.fail('custody-chain', 'the predecessor chain repeats a blob')
                break
            seen.add(cur)
            if cur not in docs:
                self.fail('custody-chain', 'the chain names %s, which is not a well-formed version in Vers(M)' % cur)
                break
            chain.append(cur)
            p = docs[cur]['predecessor']
            if p is None:
                if cur != self.boot:
                    self.fail('custody-chain', 'the chain ends at a predecessor-null version other than the bootstrap')
                break
            cur = p
        chained = list(reversed(chain))
        # (s2) prefix
        for a, b in zip(chained, chained[1:]):
            pe, ve = docs[a]['entries'], docs[b]['entries']
            if ve[:len(pe)] != pe or len(ve) <= len(pe):
                self.fail('custody-prefix', 'version %s does not extend %s by appending entries' % (b, a))
        # (s3) inclusion
        for oid, d in docs.items():
            for e in d['entries']:
                if e.get('type') != 'bootstrap' and e not in V['entries']:
                    self.fail('custody-regressed', 'an entry of version %s is not an entry of V_M' % oid)
                    break
        # (s4) malformed versions and voids
        voids = {e['blob'] for e in V['entries'] if e['type'] == 'void'}
        for oid in bad:
            if oid not in voids:
                self.fail('custody-stray', 'a malformed version %s in Vers(M) is not named by a void entry' % oid)
        for b_ in voids:
            if b_ not in bad:
                self.fail('custody-stray', 'a void entry names %s, which is not a malformed version in Vers(M)' % b_)
        # (s5) duplicates
        canon = [json.dumps(e, sort_keys=True) for e in V['entries']]
        if len(canon) != len(set(canon)):
            self.fail('custody-duplicate', 'two entries of V_M are equal')
        # R6.CUST.8 reviews of every chained version that adds entries (the bootstrap is verified by sec. 3)
        for a, b in zip(chained, chained[1:]):
            self.review_check(b, docs[b], docs[a])
        self.contexts_check(V)
        report.update(chain=chained, contexts=self.contexts, runs=self.runs)
        return self.report(report)

    def review_check(self, oid, d, pred):
        ref = {'path': self.path, 'blob_sha256': util.sha256(self.h.vers[oid])}
        items = item_ids(d, pred)
        reviews = self.cum.reviews_naming(ref) if self.cum is not None else []
        here = [(p, r) for p, r in reviews if posixpath.dirname(p) + '/' == self.h.dir]
        ok = False
        for p, r in here:
            if r.get('kind', 'review') != 'review' or fd.same_identity(r.get('reviewer'), d.get('author')) or \
                    not rec._person(r.get('reviewer')):
                continue
            vs = [v for v in r.get('verdicts') or [] if isinstance(v, dict)]
            names = [v.get('item') for v in vs]
            if sorted(names) == sorted(items) and len(set(names)) == len(names) and \
                    all(v.get('verdict') == 'accept' for v in vs):
                ok = True
        for p, r in reviews:
            if r.get('kind', 'review') != 'review' or fd.same_identity(r.get('reviewer'), d.get('author')):
                continue
            vs = [v for v in r.get('verdicts') or [] if isinstance(v, dict)]
            if (isinstance(r.get('dissent'), str) and r['dissent'].strip()) or \
                    any(v.get('verdict') != 'accept' for v in vs) or \
                    set(items) - {v.get('item') for v in vs}:
                self.fail('custody-unreviewed', 'an eligible review %s of version %s dissents' % (p, oid))
        if not ok:
            self.fail('custody-unreviewed', 'version %s has no accepting non-author review of every added item %s'
                      % (oid, items))

    def lists_pin(self, c, cref):
        """A tree lists the pin of a configuration (R6.CUST.5 (c4) pin rule)."""
        repo = self.repo
        d = posixpath.dirname(cref['path']) + '/'
        _k, ents = repo.prefix_entries(c, d, _keep_all)
        hit = [o for p, m, o in ents if p == cref['path'] and m in regular]
        if not hit or util.sha256(repo.read_blob_uncached(hit[0])) != cref['blob_sha256']:
            return False
        pt = [o for p, m, o in ents if p == d + 'PREREG.md' and m in regular]
        if not pt:
            return False
        try:
            table = self.read_pin_table(repo.read_blob_uncached(pt[0]))
        except Exception:  # an unreadable pin table lists no pin
            return False
        return table.get(cref['path'][len(d):]) == cref['blob_sha256']

    def contexts_check(self, V):
        repo, h = self.repo, self.h
        ents = V['entries']
        fp_chain = set()
        c = self.M
        while c:
            fp_chain.add(c)
            ps = repo.parents(c)
            c = ps[0] if ps else None
        # (c5) reachability
        for e in ents:
            for k in ('base', 'f', 'landing'):
                if k in e and not h.reachable(e[k]):
                    repo.parents(e[k])  # a commit absent from the store is ERROR (R6.REC.17)
                    self.fail('custody-unreachable', '%s %s is not reachable from M' % (k, e[k]))
            for r in e.get('runs') or []:
                for k in ('m', 'rev'):
                    if r.get(k) and not h.reachable(r[k]):
                        repo.parents(r[k])
                        self.fail('custody-unreachable', 'run %s %s is not reachable from M' % (k, r[k]))
        # (c1) variant (ii): freeze entries
        for e in ents:
            if e['type'] != 'freeze':
                continue
            f, cref, landing = e['f'], e['config'], e['landing']
            why = None
            data = repo.read(f, cref['path']) if repo.mode(f, cref['path']) in regular else None
            doc = fd.strict_parse(data) if data is not None else None
            if data is None or util.sha256(data) != cref['blob_sha256']:
                why = 'f\'s tree does not hold the configuration at its path with its SHA-256'
            elif not (isinstance(doc, dict) and doc.get('schema') == config_schema and
                      any(isinstance(r, dict) and r.get('kind') == 'reassessment' for r in doc.get('records') or [])
                      and discharge_bearing(doc)):
                why = 'the configuration is not discharge-bearing'
            elif not self.lists_pin(f, cref):
                why = 'the PREREG.md beside the configuration does not list its SHA-256 at f'
            else:
                ps = repo.parents(landing) if h.reachable(landing) else []
                if landing == f or landing not in fp_chain or len(ps) < 2 or repo.is_ancestor(f, ps[0]) or \
                        not any(repo.is_ancestor(f, p) for p in ps[1:]):
                    why = 'landing is not the merge on M\'s first-parent chain that landed f'
            if why:
                self.fail('custody-unsupported', 'freeze entry for %s: %s' % (f, why))
                continue
            self.contexts.append({'f': f, 'config': cref, 'landing': landing})
        ctx_f = {c_['f']: c_ for c_ in self.contexts}
        closes = [e for e in ents if e['type'] == 'close']
        # (c2) closing statements
        for c_ in self.contexts:
            # the gate (R6.CUST.10) does not require a close for every context: a round lands before its close
            if not self.gate and not any(e['f'] == c_['f'] for e in closes):
                self.fail('custody-unclosed', 'context %s has no close entry' % c_['f'])
        for e in closes:
            if e['f'] not in ctx_f:
                self.fail('custody-unsupported', 'a close names %s, which is no discharge-bearing context' % e['f'])
        docs_at = {}
        for c_ in self.commits_with_version():
            docs_at[c_] = fd.strict_parse(h.vers[h.version_at[c_]]) or {}
        for c_, d in docs_at.items():
            for e in d.get('entries') or []:
                if isinstance(e, dict) and e.get('type') == 'close' and e.get('f') in ctx_f and \
                        not repo.is_ancestor(ctx_f[e['f']]['landing'], c_):
                    self.fail('custody-early-close', 'a close for %s stands at %s, which does not descend from its '
                                                     'landing' % (e['f'], c_))
        # (c3) runs: shape, and equality with the landed run results (OQ-17, OQ-19 roles.M)
        for c_ in self.contexts:
            runs = set()
            for e in closes:
                if e['f'] == c_['f']:
                    runs |= {(r['m'], r['rev']) for r in e['runs']}
            self.runs[c_['f']] = sorted([list(r) for r in runs], key=str)
            for m, rev in runs:
                if rev is not None:
                    self.rev_shape(m, rev)
            self.results_check(c_, runs)
        # R6.CUST.7: the run's own F is the f of a closed context
        if not self.gate and self.run_F and self.run_F in ctx_f and any(e['f'] == self.run_F for e in closes):
            self.fail('custody-closed-freeze', 'the run\'s own F is the f of a closed context')
        # (c4) configurations
        frozen = {(c_['config']['path'], c_['config']['blob_sha256']) for c_ in self.contexts}
        unfrozen = [e for e in ents if e['type'] == 'unfrozen']
        bearing = {k for k, d in h.configs.items() if discharge_bearing(d)}
        for k in bearing:
            if k in frozen:
                continue
            cover = [e for e in unfrozen if (e['config']['path'], e['config']['blob_sha256']) == k]
            if not cover:
                self.fail('custody-incomplete', 'the discharge-bearing configuration %s is unaccounted for' % k[0])
                continue
            if not self.cover_after_pins(cover[0], {'path': k[0], 'blob_sha256': k[1]}):
                self.fail('custody-incomplete', 'the unfrozen entry for %s is the only cover of a configuration '
                                                'pinned after it' % k[0])
        for e in unfrozen:
            if (e['config']['path'], e['config']['blob_sha256']) not in bearing:
                self.fail('custody-unsupported', 'an unfrozen entry names no discharge-bearing configuration in R*(M)')
        # R6.CUST.6: replaying the runs of earlier contexts
        # (only when nothing else has already left custody unestablished: the cited discharges are then inapplicable
        # whatever a replay would add)
        if not self.gate and not self.problems and any(self.runs.get(c_['f']) for c_ in self.contexts):
            raise Unimplemented('R6.CUST.6 replay of the runs of a discharge-bearing context needs the R6.REC.7 '
                                'competing-successor evidence of the R6.RECON.2 (d) scope and the retained-witness '
                                'route of r9 sec. 2.2, which this tool revision does not implement')

    def commits_with_version(self):
        return [c for c in self.h.commits if self.h.version_at.get(c) is not None]

    def cover_after_pins(self, entry, cref):
        repo, h = self.repo, self.h
        pinning = [c for c in h.commits if self.lists_pin(c, cref) and
                   not any(self.lists_pin(p, cref) for p in repo.parents(c))]
        holders = []
        for c in self.commits_with_version():
            d = fd.strict_parse(h.vers[h.version_at[c]]) or {}
            if entry in (d.get('entries') or []):
                holders.append(c)
        return all(repo.is_ancestor(p, c) for c in holders for p in pinning)

    def rev_shape(self, m, rev):
        repo = self.repo
        ps = repo.parents(rev)
        if len(ps) != 1 or ps[0] != m:
            self.fail('custody-run-shape', 'REV %s does not have exactly the one parent %s' % (rev, m))
            return
        a, b = repo.entries(m), repo.entries(rev)
        changed = [p for p in set(a) | set(b) if a.get(p) != b.get(p)]
        if any(p in a or b[p][0] not in regular or not p.startswith(self.recon_root) for p in changed):
            self.fail('custody-run-shape', 'REV %s changes more than regular files added under %s'
                      % (rev, self.recon_root))
            return
        named = False
        for p in changed:
            d = fd.strict_parse(repo.read(rev, p))
            if isinstance(d, dict) and d.get('schema') == 'oi-reconciliation/2' and d.get('M') == m:
                named = True
        if not named:
            self.fail('custody-run-shape', 'REV %s adds no oi-reconciliation/2 record naming %s' % (rev, m))

    def results_check(self, c_, runs):
        """(c3) with OQ-17 adopted: the union of the close runs for f equals the runs of the landed results."""
        repo = self.repo
        d = posixpath.dirname(c_['config']['path']) + '/op-c-runs/'
        got = set()
        for p, (m, o) in sorted(repo.entries(c_['landing']).items()):
            if not p.startswith(d) or posixpath.basename(p) != 'result.json':
                continue
            res = fd.strict_parse(repo.read(c_['landing'], p)) if m in regular else None
            if not isinstance(res, dict) or res.get('schema') != result_schema:
                self.fail('custody-runs-mismatch', '%s is not a strict-parsed %s result' % (p, result_schema))
                continue
            if res.get('outcome') in non_evaluating:
                continue
            cfg = res.get('config') or {}
            if res.get('operation') != 'execution' or cfg.get('commit') != c_['f'] or \
                    cfg.get('blob_sha256') != c_['config']['blob_sha256'] or \
                    (cfg.get('admission') or {}).get('mode') != 'chain' or 'harness' in res:
                self.fail('custody-runs-mismatch', '%s is not a chain op C run of %s under its configuration'
                          % (p, c_['f']))
                continue
            mm = (res.get('roles') or {}).get('M')
            revs = {x.get('rev') for x in (res.get('inputs') or {}).get('classify_records') or []
                    if isinstance(x, dict)}
            if not _commit(mm) or len(revs) > 1:
                self.fail('custody-runs-mismatch', '%s records no M in roles.M or more than one REV' % p)
                continue
            got.add((mm, next(iter(revs)) if revs else None))
        if got != runs:
            self.fail('custody-runs-mismatch', 'the close runs of %s %s differ from its landed results %s'
                      % (c_['f'], sorted(runs, key=str), sorted(got, key=str)))

    def report(self, base):
        base.update(status='established' if not self.problems else 'unestablished',
                    problems=[{'item': i, 'why': w} for i, w in self.problems])
        base.setdefault('contexts', self.contexts)
        base.setdefault('runs', self.runs)
        base['witnesses'] = []
        return base
