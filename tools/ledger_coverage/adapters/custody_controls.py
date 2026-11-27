"""Local controls for the OBL-29 custody design c7 (verification/audits/foundations/a1exit-obl29-custody-20261126/ at
4cf463945f1ce1a078bf98f23e9ee3d091ecebe4), D-1 option (ii): the controls of its CONTROLS.json that apply to variant
(ii) or to both variants, run where the in-memory fixture can express them. The fixture is the r9 post-freeze world
(a configuration citing reassessment A of finding f with repair Q); the bootstrap blob constant is set, for the run
only, to the fixture's bootstrap version, as the design's fixture states ("custody constants PATH and BOOT").

Usage: python3 -I -B tools/ledger_coverage/adapters/custody_controls.py OUT
Writes OUT/custody-controls.json and exits 0 when every control holds, 1 otherwise.
"""
import importlib.util
import json
import os
import shutil
import sys
import tempfile

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage import record_authority as ra  # noqa: E402
from ledger_coverage.adapters import synthetic_fixture as sf  # noqa: E402
from ledger_coverage.adapters import postfreeze_controls as pfc  # noqa: E402
from ledger_coverage.engine import custody as cust  # noqa: E402
from ledger_coverage.engine import gitobj  # noqa: E402
from ledger_coverage.engine import records as rec  # noqa: E402

RESULTS = []
PATH = ra.custody_path
CDIR = PATH.rsplit('/', 1)[0] + '/'
WRITER_C, REVIEWER_C = 'writer-c', 'reviewer-c'


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


def canon(doc):
    return json.dumps(doc, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')


def version(entries, pred=None, author=WRITER_C):
    return canon({'schema': cust.schema, 'predecessor': pred, 'author': author, 'entries': entries})


def blob(b):
    return gitobj.blob_id_of(b)


def review(vbytes, items, reviewer=REVIEWER_C, dissent=None, path=None):
    d = {'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': PATH, 'blob_sha256': sf.sha(vbytes)},
         'method': 'read ' + blob(vbytes), 'verdicts': [{'item': i, 'verdict': 'accept', 'reason': ''} for i in items]}
    if dissent:
        d['dissent'] = dissent
    return pfc.jb(d)


P_PATH = 'verification/audits/syn-repair/p.json'
S_PATH = 'verification/audits/syn-sib/s.json'


P2_PATH = 'verification/audits/syn-repair/p2.json'
S2_PATH = 'verification/audits/syn-sib/s2.json'


def lineage_finding_world(r, variant=None, edits=None, two_hop=False):
    """pfc.finding_world with the repair record Q superseding a reviewed record P of the same lineage; with two_hop,
    P itself supersedes a reviewed record P2 of that lineage (Q -> P -> P2)."""
    w = pfc.World(r, variant=variant, edits=edits)
    orig = pfc.rcmod.edit_key(pfc.World(r).led, 'E1')
    f = pfc.invalidating(w, sf.DOC, edit='E1')
    f['paths'][0]['scientific_effect']['invalidated'][0]['sha256'] = orig
    base = pfc.invalidating(pfc.World(r), sf.DOC)
    f['paths'][0]['scientific_effect']['configuration'] = base['paths'][0]['scientific_effect']['configuration']
    if 'target' in base['paths'][0]['scientific_effect']['invalidated'][0]:
        f['paths'][0]['scientific_effect']['invalidated'][0]['target'] = \
            base['paths'][0]['scientific_effect']['invalidated'][0]['target']
    bw = pfc.World(r)
    w.M = w.repo.derive(w.M, {q: b for q, b in bw.files.items() if isinstance(b, bytes)}, parents=[w.M],
                        subject='the base configuration lands (it resolves, R6.RECON.33)')
    pfc.land(w, [(pfc.RD + 'finding.json', f)])
    w.findings = [{'path': pfc.RD + 'finding.json', 'blob_sha256': sf.sha(pfc.jb(f))}]
    w.M = w.repo.derive(w.M, {sf.DOC: w.repo.read(w.M, sf.DOC).replace(b'changed on main', b'repaired on main')},
                        parents=[w.M], subject='repair')
    w.repair_commit = w.M
    if two_hop:
        P2 = w.record(record_id='syn-repair', author=pfc.REPAIR_AUTHOR)
        pfc.land(w, [(P2_PATH, P2)], 'the earliest record P2 of the repair lineage')
        w.p2_ref = {'path': P2_PATH, 'blob_sha256': sf.sha(pfc.jb(P2))}
        P = w.record(record_id='syn-repair', author=pfc.REPAIR_AUTHOR, supersedes=dict(w.p2_ref))
    else:
        P = w.record(record_id='syn-repair', author=pfc.REPAIR_AUTHOR)
    pfc.land(w, [(P_PATH, P)], 'the earlier record P of the repair lineage')
    w.p_ref = {'path': P_PATH, 'blob_sha256': sf.sha(pfc.jb(P))}
    rep = w.record(record_id='syn-repair', author=pfc.REPAIR_AUTHOR, supersedes=dict(w.p_ref))
    rp = 'verification/audits/syn-repair/repair.json'
    pfc.land(w, [(rp, rep)], 'the repair record Q, superseding P')
    w.repair_entry = {'path': rp, 'blob_sha256': sf.sha(pfc.jb(rep))}
    return w


R_PATH = 'verification/audits/syn-repl/r.json'


def replacement(w, reviewer='reviewer-z', tokens=True):
    """R': a reconciliation record of another lineage (syn-repl) for the same path, and Z, its only review in its
    directory: an accepting review by a reviewer outside NR-3's exclusions whose method holds, when `tokens`, the git
    blob ids of Q (the disputed record of the lineage witness) and of S (the record forming it) (NR-4). Both land on
    main in main2. Returns (R' path, R' bytes, Z path, Z bytes)."""
    rb = pfc.jb(w.record(record_id='syn-repl', author='writer-r2'))
    sb = sibling(w)[S_PATH]
    qb = w.repo.read(w.M, w.repair_entry['path'])
    method = 'read ' + (' '.join([gitobj.blob_id_of(qb), gitobj.blob_id_of(sb)]) if tokens else 'every object')
    zb = pfc.jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': R_PATH,
                                                                                 'blob_sha256': sf.sha(rb)},
                 'method': method, 'verdicts': [{'item': i, 'verdict': 'accept'}
                                                for i in rec.item_ids(json.loads(rb))]})
    return R_PATH, rb, R_PATH[:-5] + '.review.json', zb


def sibling2(w, author='writer-s2'):
    """S2: a record of the lineage naming P2 in supersedes, a sibling of P (the second edge P -> P2)."""
    S = w.record(record_id='syn-repair', author=author, supersedes=dict(w.p2_ref))
    data = pfc.jb(S)
    return {S2_PATH: data, S2_PATH[:-5] + '.review.json': w.review(S2_PATH, data)}


def sibling(w, author='writer-s'):
    """S: another record of Q's lineage and schema naming the same exact P in supersedes, with its review."""
    S = w.record(record_id='syn-repair', author=author, supersedes=dict(w.p_ref))
    data = pfc.jb(S)
    return {S_PATH: data, S_PATH[:-5] + '.review.json': w.review(S_PATH, data)}


class CW:
    """A cited-discharge world (finding f, repair Q, reassessment A cited by the configuration) with custody commits
    appended on main."""

    def __init__(self, r, cite=True):
        w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
        self.w = pfc.finding_world(r, variant=pfc.cite(pfc.reassessment(w1)) if cite else None,
                                   edits=pfc.EDITS_REWORDED)
        self.boot = None
        self.n = 0

    @classmethod
    def lineage(cls, r, repl=False, cite_repl=False, cite_q=False, two_hop=False, tl_prefix=None):
        """A CW world whose repair record Q supersedes an earlier record P of its lineage (both reviewed on main), so
        that a configuration pinning Q makes Q's R6.REC.7 check, and its edge Q -> P, operative.

        repl: the current configuration cites A2, a reassessment of the same finding whose repair entry is the
        replacement R' (lineage syn-repl; it lands with its review Z in main2, see replacement()), so that it relies
        on a witness against Q only through (r3). cite_repl: the current configuration also cites R' and Z (NR-2).
        cite_q: the current configuration cites Q and its review (with P and P's review at F), making Q's lineage
        check operative in the current run (the live rule of R6.OBL29.3)."""
        self = cls.__new__(cls)
        w1 = lineage_finding_world(r, edits=pfc.EDITS_REWORDED, two_hop=two_hop)
        if repl:
            rp_, rb, zp, zb = replacement(w1)
            cur = pfc.reassessment(w1, repair={'commits': [w1.repair_commit],
                                                'entry': {'path': rp_, 'blob_sha256': sf.sha(rb),
                                                          'entry_path': sf.DOC}})
        else:
            cur = pfc.reassessment(w1)
        base = pfc.cite(cur)
        extra_files, extra_recs = {}, []
        if repl and cite_repl:
            extra_files.update({rp_: rb, zp: zb})
            extra_recs += [{'kind': 'reconciliation', 'path': rp_, 'blob_sha256': sf.sha(rb)},
                           {'kind': 'review', 'path': zp, 'blob_sha256': sf.sha(zb)}]
        if cite_q:
            q, qp = w1.repair_entry, w1.repair_entry['path']
            # cite_q == 'without-p': P and its review are left out of F, so Q's edge does not resolve there
            # 'without-p-review': P is at F without its review, so the predecessor lint of Q's lineage check fails
            with_p = {'without-p': (), 'without-p-review': (P_PATH,)}.get(cite_q, (P_PATH, P_PATH[:-5] + '.review.json'))
            if two_hop:
                with_p += (P2_PATH, P2_PATH[:-5] + '.review.json')
            for pth in (qp, qp[:-5] + '.review.json') + with_p:
                extra_files[pth] = w1.repo.read(w1.M, pth)
            extra_recs += [dict(q, kind='reconciliation'),
                           {'kind': 'review', 'path': qp[:-5] + '.review.json',
                            'blob_sha256': sf.sha(extra_files[qp[:-5] + '.review.json'])}]

        def variant(w_):
            v = base(w_)
            out = {'files': dict(v['files'], **extra_files), 'add_records': list(v['add_records']) + extra_recs}
            if tl_prefix:
                # a tool-landing class whose prefix is tl_prefix (the class record of obl29_controls.tl_variant)
                from ledger_coverage.adapters.obl29_controls import tl_variant
                t = tl_variant(tl_prefix)(w_)
                out['files'].update(t['files'])
                out['add_records'] += t['add_records']
                out['extra'] = t['extra']
            return out
        self.w = lineage_finding_world(r, variant=variant, edits=pfc.EDITS_REWORDED, two_hop=two_hop)
        self.boot = None
        self.n = 0
        self.ctx_a = pfc.reassessment(w1)
        return self

    def step(self, files, subject='custody step', parents=None):
        w = self.w
        w.M = w.repo.derive(w.M, files, parents=parents or [w.M], subject=subject)
        return w.M

    def bootstrap(self, base=None):
        v0 = version([{'base': base or self.w.M, 'type': 'bootstrap'}])
        self.boot = blob(v0)
        self.step({PATH: v0}, 'custody bootstrap')
        return v0

    def succ(self, prev, new_entries, reviewed=True, extra=None, review_kw=None):
        pd = json.loads(prev)
        v = version(pd['entries'] + new_entries, pred=blob(prev))
        files = {PATH: v}
        if reviewed:
            self.n += 1
            items = cust.item_ids(json.loads(v), pd)
            files[CDIR + 'v%d.review.json' % self.n] = review(v, items, **(review_kw or {}))
        files.update(extra or {})
        self.step(files, 'custody successor')
        return v

    def run(self, boot=None):
        saved = ra.custody_bootstrap_blob
        ra.custody_bootstrap_blob = boot if boot is not None else (self.boot or saved)
        try:
            code, out = self.w.run([], harness=True)
        finally:
            ra.custody_bootstrap_blob = saved
        out = out or {}
        c3 = out.get('category3') or {}
        cu = c3.get('custody') or {}
        return {'exit': code, 'stop': (out.get('stop') or {}).get('class'),
                'stop_msg': (out.get('stop') or {}).get('message', '')[:200],
                'status': cu.get('status'), 'items': sorted({p['item'] for p in cu.get('problems') or []}),
                'whys': [p['why'][:160] for p in cu.get('problems') or []][:4],
                # the whole why of every custody-run-shape problem, for controls that assert its reason
                'shape_whys': [p['why'] for p in cu.get('problems') or [] if p['item'] == 'custody-run-shape'],
                'witnesses': cu.get('witnesses') or [],
                'full_whys': [p['why'] for p in cu.get('problems') or []],
                'contexts': len(cu.get('contexts') or []),
                'invalid_details': [d for i in out.get('items', []) if i['class'] == 'record-invalid'
                                    for d in (i.get('detail') or [])],
                'invalid_subjects': sorted({i.get('subject') for i in out.get('items', [])
                                            if i['class'] == 'record-invalid'}),
                'decisions': [(d['blocked'], d['route'], d['clauses']) for d in cu.get('decisions') or []],
                'adjudications': cu.get('adjudications') or [],
                'reassess_why': [d for i in out.get('items', []) if i['class'] == 'record-invalid' and
                                 i.get('subject') == pfc.RA_PATH for d in (i.get('detail') or [])],
                'findings': c3.get('findings') or [],
                'blocked_full': [(b['record']['path'], b.get('edit')) for b in c3.get('blocked') or []],
                'reassessments': c3.get('reassessments'), 'blocked': [b['record']['path'] for b in c3.get('blocked')
                                                                       or []],
                'classes': sorted({i['class'] for i in out.get('items', [])})}


def guarded_run(make):
    """Runs one control world on its own: an exception is recorded for that case (which then fails its own assertion)
    instead of ending the suite's group."""
    try:
        return make()
    except Exception as e:  # noqa: BLE001 - a crash is the case's failure, reported in it
        return {'error': '%s: %s' % (type(e).__name__, str(e)[:200]), 'status': None, 'items': [], 'classes': [],
                'reassessments': None, 'full_whys': [], 'whys': [], 'witnesses': [], 'shape_whys': []}


def failed_with(o, item):
    return o['status'] == 'unestablished' and item in o['items'] and 'retirement-blocked' in o['classes'] and \
        not o['reassessments']


def schema_chain_controls(r):
    c = CW(r)
    c.bootstrap()
    o = c.run()
    case('CU-P1', 'V0 at PATH, no discharge-bearing configuration reachable: custody established and the cited '
                  'discharge applies (the finding is not blocked)', o,
         o['status'] == 'established' and bool(o['reassessments']) and not o['blocked'])
    c = CW(r)
    o = c.run(boot='0' * 40)
    case('CU-N1', 'no file at PATH: custody-missing; the discharge is inapplicable and the block stands', o,
         failed_with(o, 'custody-missing'))
    c = CW(r, cite=False)
    code, out = c.w.run([], harness=True)
    cu = ((out or {}).get('category3') or {}).get('custody') or {}
    case('CU-P7', 'no file at PATH and no cited discharge: custody is not required (the no-edit route needs none)',
         cu, cu.get('status') == 'not-required')
    # CU-N2: schema variants
    base = None
    variants = {}
    for name, mk in (('trailing newline', lambda b0: version([{'base': b0, 'type': 'bootstrap'}]) + b'\n'),
                     ('unknown key', lambda b0: canon({'schema': cust.schema, 'predecessor': None, 'author': WRITER_C,
                                                       'entries': [{'base': b0, 'type': 'bootstrap'}], 'note': 'x'})),
                     ('entry type clear', lambda b0: version([{'base': b0, 'type': 'bootstrap'},
                                                              {'f': b0, 'type': 'clear'}])),
                     ('short commit id', lambda b0: version([{'base': b0[:12], 'type': 'bootstrap'}])),
                     ('free-text field', lambda b0: version([{'base': b0, 'type': 'bootstrap', 'why': 'x'}])),
                     ('run without rev', lambda b0: version([{'base': b0, 'type': 'bootstrap'},
                                                             {'f': b0, 'runs': [{'m': b0}], 'type': 'close'}]))):
        c = CW(r)
        v = mk(c.w.M)
        c.boot = blob(v)
        c.step({PATH: v})
        variants[name] = c.run()
    case('CU-N2', 'V_M fails the schema (trailing newline, unknown key, entry type clear, short id, free text, run '
                  'without rev): custody-schema', variants,
         all(failed_with(o, 'custody-schema') for o in variants.values()))
    c = CW(r)
    v0 = c.bootstrap()
    v1 = version(json.loads(v0)['entries'] + [{'config': {'path': 'x/y.json', 'blob_sha256': '1' * 64},
                                               'type': 'unfrozen'}], pred='2' * 40)
    c.step({PATH: v1})
    o = c.run()
    case('CU-N3', 'V_M\'s predecessor names a blob that never stood at PATH: custody-chain', o,
         failed_with(o, 'custody-chain'))
    c = CW(r)
    v0 = c.bootstrap()
    forged = version([{'base': c.w.M, 'type': 'bootstrap'}], author='writer-z')
    c.step({PATH: forged})
    o = c.run()
    case('CU-N4', 'a forged predecessor-null version other than BOOT heads the chain: custody-chain', o,
         failed_with(o, 'custody-chain'))
    # successors: build an unfrozen entry that is valid only as an acknowledgement (no discharge-bearing config:
    # an unfrozen entry naming none is custody-unsupported), so use void entries of malformed versions instead
    c = CW(r)
    v0 = c.bootstrap()
    bad1 = b'{not json'
    c.step({PATH: bad1}, 'a malformed version')
    v1 = c.succ(v0, [{'blob': blob(bad1), 'type': 'void'}])
    o = c.run()
    case('CU-P4', 'a malformed version acknowledged by a void entry in a reviewed successor: established', o,
         o['status'] == 'established')
    prefix = {}
    for name in ('drop', 'reorder', 'append nothing'):
        c = CW(r)
        v0 = c.bootstrap()
        b1, b2 = b'{bad one', b'{bad two'
        c.step({PATH: b1})
        c.step({PATH: b2})
        v1 = c.succ(v0, [{'blob': blob(b1), 'type': 'void'}, {'blob': blob(b2), 'type': 'void'}])
        e1 = json.loads(v1)['entries']
        if name == 'drop':
            new = e1[:2]
        elif name == 'reorder':
            new = [e1[0], e1[2], e1[1]]
        else:
            new = e1
        v2 = version(new, pred=blob(v1))
        items = ['entry:%d' % i for i in range(len(e1), len(new))]
        c.step({PATH: v2, CDIR + 'v2.review.json': review(v2, items)})
        prefix[name] = c.run()
    case('CU-N5', 'a successor drops, reorders or appends nothing: custody-prefix', prefix,
         all(failed_with(o, 'custody-prefix') for o in prefix.values()))
    c = CW(r)
    v0 = c.bootstrap()
    b1, b2 = b'{bad one', b'{bad two'
    c.step({PATH: b1})
    v1 = c.succ(v0, [{'blob': blob(b1), 'type': 'void'}])
    c.step({PATH: b2})
    v2 = c.succ(v1, [{'blob': blob(b2), 'type': 'void'}])
    c.step({PATH: v1}, 'revert to v1')
    o = c.run()
    case('CU-N6', 'M\'s tree holds V1 again after V2 stood at PATH (a revert): custody-regressed', o,
         failed_with(o, 'custody-regressed'))
    c = CW(r)
    v0 = c.bootstrap()
    c.step({PATH: b'{unacknowledged'})
    c.step({PATH: v0}, 'restore v0')
    o = c.run()
    case('CU-N8', 'a malformed version in Vers(M) without a void entry: custody-stray', o,
         failed_with(o, 'custody-stray'))
    c = CW(r)
    v0 = c.bootstrap()
    v1 = c.succ(v0, [{'blob': blob(v0), 'type': 'void'}])
    o = c.run()
    case('CU-N8b', 'a void entry names a well-formed version: custody-stray', o, failed_with(o, 'custody-stray'))
    c = CW(r)
    v0 = c.bootstrap()
    b1 = b'{bad one'
    c.step({PATH: b1})
    v1 = version(json.loads(v0)['entries'] + [{'blob': blob(b1), 'type': 'void'},
                                              {'blob': blob(b1), 'type': 'void'}], pred=blob(v0))
    c.step({PATH: v1, CDIR + 'r.json': review(v1, ['entry:1', 'entry:2'])})
    o = c.run()
    case('CU-N5-DUP', 'two equal entries in V_M: custody-duplicate (s5)', o, failed_with(o, 'custody-duplicate'))
    # R6.CUST.8
    revs = {}
    for name, kw in (('no review', None), ('author review', {'reviewer': WRITER_C}),
                     ('second review dissents', 'dissent'), ('omits an item', 'omit')):
        c = CW(r)
        v0 = c.bootstrap()
        b1, b2 = b'{bad one', b'{bad two'
        c.step({PATH: b1})
        c.step({PATH: b2})
        new = [{'blob': blob(b1), 'type': 'void'}, {'blob': blob(b2), 'type': 'void'}]
        if kw is None:
            c.succ(v0, new, reviewed=False)
        elif kw == 'dissent':
            v1 = c.succ(v0, new)
            c.step({CDIR + 'dissent.review.json': review(v1, ['entry:1', 'entry:2'], reviewer='reviewer-d',
                                                         dissent='the void entries are not justified')})
        elif kw == 'omit':
            v1 = version(json.loads(v0)['entries'] + new, pred=blob(v0))
            c.step({PATH: v1, CDIR + 'r.json': review(v1, ['entry:1'])})
        else:
            c.succ(v0, new, review_kw=kw)
        revs[name] = c.run()
    case('CU-N15', 'a version adding entries without an accepting non-author review of every added entry:<i> item, '
                   'or with a dissenting review: custody-unreviewed', revs,
         all(failed_with(o, 'custody-unreviewed') for o in revs.values()))
    c = CW(r)
    v0 = c.bootstrap()
    a = version(json.loads(v0)['entries'] + [{'blob': '3' * 40, 'type': 'void'}], pred='4' * 40)
    b = version(json.loads(v0)['entries'] + [{'blob': '3' * 40, 'type': 'void'}], pred=blob(a))
    a = version(json.loads(v0)['entries'] + [{'blob': '3' * 40, 'type': 'void'}], pred=blob(b))
    c.step({PATH: a})
    o = c.run()
    case('CU-N19', 'a version naming a predecessor that is not a well-formed version reachable (a broken cycle): '
                   'custody-chain', o, failed_with(o, 'custody-chain'))
    c = CW(r)
    v0 = c.bootstrap()
    c.step({PATH: None, CDIR + 'moved.json': v0}, 'move the custody file')
    o = c.run()
    case('CU-X3', 'the custody file moved to another path with identical bytes: custody-missing', o,
         failed_with(o, 'custody-missing'))


def config_doc(w, admission=None, reassessment=True, corpus_path=None):
    """The fixture's configuration citing a reassessment (R6.CFG.4: no admission key). `admission` adds a key the
    schema does not have (a configuration the loader refuses); `corpus_path` adds an exact corpus path."""
    d = json.loads(w.files[w.p])
    if corpus_path is not None:
        d['corpus'] = dict(d['corpus'], paths=[corpus_path])
    if reassessment:
        d['records'] = list(d['records']) + [{'kind': 'reassessment', 'path': 'syn/cfg/ra.json',
                                              'blob_sha256': '5' * 64}]
    if admission is not None:
        d['admission'] = {'mode': admission}
    return pfc.jb(d)


def configuration_controls(r):
    KP = 'verification/audits/syn-plan/config.json'
    c = CW(r)
    v0 = c.bootstrap()
    kb = config_doc(c.w)
    c.step({KP: kb}, 'a discharge-bearing configuration lands on main')
    kref = {'path': KP, 'blob_sha256': sf.sha(kb)}
    v1 = c.succ(v0, [{'config': kref, 'type': 'unfrozen'}])
    o = c.run()
    case('CU-P5', 'a discharge-bearing configuration landed without a freeze, named by a reviewed unfrozen entry: '
                  'established', o, o['status'] == 'established')
    c = CW(r)
    c.bootstrap()
    c.step({KP: kb})
    o = c.run()
    case('CU-N11', 'a discharge-bearing configuration in R*(M) that no context admits and no unfrozen entry names: '
                   'custody-incomplete', o, failed_with(o, 'custody-incomplete'))
    c = CW(r)
    v0 = c.bootstrap()
    c.step({KP: kb})
    c.step({KP: None}, 'deleted')
    o = c.run()
    case('CU-N11-DELETED', 'the same configuration later deleted from main: still in R*(M), custody-incomplete', o,
         failed_with(o, 'custody-incomplete'))
    c = CW(r)
    v0 = c.bootstrap()
    c.succ(v0, [{'config': {'path': KP, 'blob_sha256': '6' * 64}, 'type': 'unfrozen'}])
    o = c.run()
    case('CU-N11-UNSUPPORTED', 'an unfrozen entry naming no discharge-bearing configuration in R*(M): '
                               'custody-unsupported', o, failed_with(o, 'custody-unsupported'))
    c = CW(r)
    c.bootstrap()
    c.step({KP: config_doc(c.w)})
    o = c.run()
    case('CU-N11-NO-ADMISSION', 'a configuration citing a reassessment, with no admission key (R6.CFG.4 has none), '
                                'that no context admits and no unfrozen entry names: discharge-bearing (owner decision '
                                '2, no admission.mode condition), custody-incomplete', o,
         failed_with(o, 'custody-incomplete'))
    c = CW(r)
    c.bootstrap()
    c.step({KP: config_doc(c.w, admission='harness')})
    o = c.run()
    case('CU-N23-HARNESS', 'a configuration citing a reassessment that carries an admission.mode harness key: '
                           'discharge-bearing all the same (owner decision 2: no admission.mode condition), so with no '
                           'unfrozen entry custody-incomplete', o, failed_with(o, 'custody-incomplete'))
    # the pin rule (c4)
    def pin_world(unfrozen_before_pin, merge_old_branch=False):
        c = CW(r)
        v0 = c.bootstrap()
        c.step({KP: kb}, 'planning commit')
        fork = c.w.M
        pre = PATH.rsplit('/', 1)[0]
        kref = {'path': KP, 'blob_sha256': sf.sha(kb)}
        v = None
        if unfrozen_before_pin:
            v = c.succ(v0, [{'config': kref, 'type': 'unfrozen'}])
        c.step({KP.rsplit('/', 1)[0] + '/PREREG.md': ('### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n'
                                                     '| `config.json` | `%s` |\n' % sf.sha(kb)).encode()},
               'the pin is introduced')
        if not unfrozen_before_pin:
            v = c.succ(v0, [{'config': kref, 'type': 'unfrozen'}])
        if merge_old_branch:
            side = c.w.repo.derive(fork, {'notes/side.txt': b's\n'}, parents=[fork], subject='old branch')
            c.step({'notes/side.txt': b's\n'}, 'merge an old branch', parents=[c.w.M, side])
        del pre
        return c.run()
    o = pin_world(True)
    case('CU-N32', 'an unfrozen entry written before the configuration was pinned is its only cover: '
                   'custody-incomplete', o, failed_with(o, 'custody-incomplete'))
    oa, ob = pin_world(False), pin_world(False, merge_old_branch=True)
    case('CU-P11', 'an unfrozen entry written after the pin\'s introduction covers it; a later merge of a branch forked '
                   'before the pin is not a pinning commit', {'a': oa, 'b': ob},
         oa['status'] == 'established' and ob['status'] == 'established')


def freeze_controls(r):
    """Variant (ii): reviewed freeze entries, landing merges, close entries and run results."""
    KD = 'verification/audits/syn-plan/'
    KP = KD + 'config.json'

    def freeze_world(close=True, landing_kind='merge', runs=(), results=(), early_close=False, prereg_lists=True,
                     config_at_f=True, pre=None, classes=None, corpus_path=None, admission=None, world=None,
                     main_files=None, cfg_records=(), ctx_reassessment=None, extra_ctx=None, f_files=None,
                     main_steps=None):
        c = world(r) if world is not None else CW(r)
        v0 = c.bootstrap()
        main_before = c.w.M
        # the world's configuration already cites its reassessment (with the record at f), so no further reference
        kb = config_doc(c.w, corpus_path=corpus_path, admission=admission, reassessment=False)
        ctx_files = {}
        if ctx_reassessment is not None:
            # the context's configuration cites another reassessment (bytes) in place of the current one
            ab = pfc.jb(ctx_reassessment)
            ap = KD + 'reassessment.json'
            ctx_files[ap] = ab
            d_ = json.loads(kb)
            d_['records'] = [x for x in d_['records'] if x.get('path') not in (pfc.RA_PATH, pfc.RA_PATH[:-5] +
                                                                              '.review.json')] + \
                [{'kind': 'reassessment', 'path': ap, 'blob_sha256': sf.sha(ab)}]
            kb = pfc.jb(d_)
        if cfg_records:
            d_ = json.loads(kb)
            d_['records'] = list(d_['records']) + [dict(x) for x in cfg_records]
            kb = pfc.jb(d_)
        cls_files = {}
        if classes is not None:
            # roles.side_change_classes names a class record at f; classes = (record bytes, pinned blob_sha256 or
            # None, and optionally False to leave the record out of f's tree)
            cb, pin = classes[:2]
            present = classes[2] if len(classes) > 2 else True
            d = json.loads(kb)
            d['roles'] = dict(d['roles'], side_change_classes={'path': KD + 'classes.json',
                                                               'blob_sha256': pin or sf.sha(cb)})
            kb = pfc.jb(d)
            cls_files = {KD + 'classes.json': cb} if present else {}
        files = {KD + 'PREREG.md': ('### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n| `config.json` | `%s` |\n'
                                    % (sf.sha(kb) if prereg_lists else '0' * 64)).encode()}
        if config_at_f:
            files[KP] = kb
            # the records and adapter inputs the configuration names, at f beside it, so that its ledger is read at f
            # through its own adapter (R6.RECON.1)
            files.update({q: b for q, b in c.w.files.items() if isinstance(b, bytes) and q != c.w.p})
        files.update(cls_files)
        files.update(ctx_files)
        files.update(f_files or {})
        if corpus_path is not None:
            files[corpus_path] = b'# a corpus path of the context\n'
        F1 = c.w.repo.derive(main_before, files, parents=[main_before], subject='freeze F1')
        tip = F1
        # the landing carries the plan's own files; the configuration's adapter inputs stay in f's tree (they would
        # otherwise overwrite the base configuration's inputs on main, which the finding's configuration resolves to)
        wfiles = {q for q in c.w.files if q != c.w.p}
        branch = {q: b for q, b in files.items() if q not in wfiles or q in (f_files or {}) or q in ctx_files}
        for i, res in enumerate(results):
            rf = {KD + 'op-c-runs/run%d/result.json' % i: pfc.jb(res)}
            branch.update(rf)
            tip = c.w.repo.derive(tip, rf, parents=[tip], subject='run result')
        for i_, mf in enumerate(main_steps or ()):
            c.step(mf, 'main step %d' % i_)
        main2 = c.step(dict({'notes/main.txt': b'main moves\n'}, **(main_files or {})), 'main moves')
        c.main2 = main2
        # a merge's tree carries the branch's files (the in-memory reader derives a tree from its first parent)
        if landing_kind == 'merge':
            L = c.step(branch, 'land F1', parents=[main2, tip])
        elif landing_kind == 'self':
            L = F1
        elif landing_kind == 'foxtrot-m':
            # a foxtrot fast-forward before the landing: main's next commit has another line as first parent and
            # main2 as second (carrying main2's tree), so main2 and the repair commit leave the first-parent chain
            # while the landing merge stays on it
            other = c.w.repo.derive(c.w.syn.H, {'notes/other.txt': b'o\n'}, parents=[c.w.syn.H], subject='line')
            tree = {p_: c.w.repo.read(main2, p_) for p_ in c.w.repo.entries(main2)}
            c.step(tree, 'foxtrot', parents=[other, main2])
            c.fox = c.w.M
            L = c.step(branch, 'land F1', parents=[c.w.M, tip])
        elif landing_kind == 'foxtrot':
            # the landing merge, then a foxtrot fast-forward: main's next commit has another line as first parent and
            # the landing as second, so the landing leaves M's first-parent chain (R-C4)
            L = c.step(branch, 'land F1', parents=[main2, tip])
            other = c.w.repo.derive(main_before, {'notes/other.txt': b'o\n'}, parents=[main_before], subject='line')
            c.step(dict(branch, **{'notes/main.txt': b'main moves\n'}), 'foxtrot', parents=[other, L])
        else:
            L = c.step(branch, 'land F1', parents=[main2, tip])
            L = c.step({'notes/later.txt': b'l\n'}, 'a later merge', parents=[L, tip])
        if pre is not None:
            runs = pre(c, main_before)
        c.runs_seen = list(runs)
        kref = {'path': KP, 'blob_sha256': sf.sha(kb)}
        fe = {'config': kref, 'f': F1, 'landing': L, 'type': 'freeze'}
        ents = [fe]
        if close:
            ents.append({'f': F1, 'runs': [{'m': m, 'rev': rv} for m, rv in runs], 'type': 'close'})
        if extra_ctx is not None:
            # a later context F3: configuration kb3 (records: extra_ctx['records'], files at F3: extra_ctx['files'])
            # in its own plan directory, landed by a merge, with a reviewed freeze entry and a close of no runs
            KD3 = 'verification/audits/syn-plan3/'
            d3 = json.loads(config_doc(c.w, reassessment=False))
            d3['records'] = list(d3['records']) + [dict(x) for x in extra_ctx.get('records', ())]
            kb3 = pfc.jb(d3)
            f3 = dict(extra_ctx.get('files', {}), **{KD3 + 'config.json': kb3, KD3 + 'PREREG.md': (
                '### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n| `config.json` | `%s` |\n' % sf.sha(kb3)).encode()})
            F3 = c.w.repo.derive(c.w.M, f3, parents=[c.w.M], subject='freeze F3')
            m3 = c.step({'notes/m3.txt': b'm3\n'}, 'main moves again')
            L3 = c.step(f3, 'land F3', parents=[m3, F3])
            kref3 = {'path': KD3 + 'config.json', 'blob_sha256': sf.sha(kb3)}
            ents += [{'config': kref3, 'f': F3, 'landing': L3, 'type': 'freeze'}, {'f': F3, 'runs': [], 'type': 'close'}]
            c.F3 = F3
        if early_close:
            # the custody version holding the close is committed on a branch forked before the landing, then merged
            v1 = version(json.loads(v0)['entries'] + ents, pred=blob(v0))
            vf = {PATH: v1, CDIR + 'early.review.json': review(v1, cust.item_ids(json.loads(v1), json.loads(v0)))}
            side = c.w.repo.derive(main2, vf, parents=[main2], subject='close written before the landing')
            c.step(vf, 'merge the early close', parents=[c.w.M, side])
        else:
            c.succ(v0, ents)
        return c, F1, L, kref

    c, F1, L, kref = freeze_world()
    o = c.run()
    case('CU-P2', 'variant (ii): a reviewed freeze entry of a discharge-bearing configuration admitted at F1 and landed '
                  'by a merge on main, with a close of no runs and no run results: established', o,
         o['status'] == 'established')
    c, F1, L, kref = freeze_world(close=False)
    o = c.run()
    case('CU-N9', 'a context with no close entry: custody-unclosed', o, failed_with(o, 'custody-unclosed'))
    neg = {'config absent at f': freeze_world(config_at_f=False)[0].run(),
           'PREREG.md does not list it': freeze_world(prereg_lists=False)[0].run()}
    case('CU-N31', 'variant (ii): the freeze entry\'s configuration is not at its path in f\'s tree, or the PREREG.md '
                   'beside it does not list its SHA-256: custody-unsupported', neg,
         all(failed_with(o, 'custody-unsupported') for o in neg.values()))
    o = freeze_world(landing_kind='self')[0].run()
    case('CU-N33', 'a freeze entry naming landing = f: custody-unsupported', o, failed_with(o, 'custody-unsupported'))
    o = freeze_world(landing_kind='later')[0].run()
    case('CU-N34', 'landing names a later merge whose first parent already contains f: custody-unsupported', o,
         failed_with(o, 'custody-unsupported'))
    o = freeze_world(early_close=True)[0].run()
    case('CU-N29', 'a close for F1 stands at a commit that does not descend from its landing: custody-early-close', o,
         failed_with(o, 'custody-early-close'))
    o = freeze_world(landing_kind='foxtrot')[0].run()
    case('CU-RC4-FOXTROT', 'a foxtrot fast-forward takes the landing merge off M\'s first-parent chain: the freeze '
                           'entry fails at this M (custody-unsupported; the liveness hazard R-C4)', o,
         failed_with(o, 'custody-unsupported'))

    def rev_pre(kind):
        def pre(c, main_before):
            m = main_before
            rec_doc = {'schema': 'oi-reconciliation/2', 'M': m, 'record_id': 'x'}
            files = {'verification/audits/syn-recon-r/rec.json': pfc.jb(rec_doc)}
            parents = [m]
            if kind == 'plan-dir':
                files = {KD + 'stray.json': pfc.jb(rec_doc)}
            elif kind == 'tool-landing':
                files = {'verification/audits/syn-tool/rec.json': pfc.jb(rec_doc)}
            elif kind == 'outside-audits':
                files = {'notes/recon/rec.json': pfc.jb(rec_doc)}
            elif kind == 'modifies':
                files = dict(files, **{sf.DOC: b'changed\n'})
            elif kind == 'no-record':
                files = {'verification/audits/syn-recon-r/rec.json': pfc.jb(dict(rec_doc, M='8' * 40))}
            elif kind == 'two-parents':
                parents = [m, c.w.repo.parents(m)[0]]
            base = m
            if kind == 'other-parent':
                base = c.w.repo.parents(m)[0]
                parents = [base]
            rev = c.w.repo.derive(base, files, parents=parents, subject='REV')
            c.step(files, 'merge REV', parents=[c.w.M, rev])
            return [(m, rev)]
        return pre
    from ledger_coverage.engine import cli as cli_mod

    def ran(cw):
        return cw.run()
    want = {'plan-dir': 'inside the plan record directory', 'modifies': 'changes more than adding',
            'no-record': 'adds no oi-reconciliation/2 record', 'two-parents': 'exactly the one parent',
            'other-parent': 'exactly the one parent'}
    # the class record of the context: a tool-landing class whose prefix holds the REV's file, and another class
    tl_classes = pfc.jb({'classes': [{'id': 'tool-landing', 'prefixes': ['verification/audits/syn-tool/']},
                                     {'id': 'other-class', 'prefixes': ['verification/audits/syn-recon-r/']}]})
    want.update({'tool-landing': 'under a prefix of the tool-landing class',
                 'ledgered-dir': 'its directory holds a ledgered or corpus path',
                 'outside-audits': 'not under verification/audits/',
                 'class-unverified': 'the context\'s side-change class record cannot be read at f'})

    def guarded(make):
        # each variant runs on its own: an exception is recorded for that variant, which then fails its assertion
        try:
            return make()
        except Exception as e:  # noqa: BLE001 - a crash is the variant's failure, reported in the case
            return {'error': '%s: %s' % (type(e).__name__, str(e)[:160]), 'shape_whys': [], 'items': [],
                    'whys': [], 'status': None, 'classes': [], 'reassessments': None}
    shapes = {k: guarded(lambda k=k: ran(freeze_world(pre=rev_pre(k))[0]))
              for k in ('plan-dir', 'modifies', 'no-record', 'two-parents', 'other-parent')}
    shapes['tool-landing'] = guarded(lambda: ran(freeze_world(pre=rev_pre('tool-landing'),
                                                                      classes=(tl_classes, None))[0]))
    # a corpus path of the context's configuration in the REV file's directory, read at f by the real reader
    shapes['ledgered-dir'] = guarded(lambda: ran(freeze_world(
        pre=rev_pre('ok'), corpus_path='verification/audits/syn-recon-r/corpus.md')[0]))
    shapes['outside-audits'] = guarded(lambda: ran(freeze_world(pre=rev_pre('outside-audits'))[0]))
    # roles.side_change_classes names a path with no record at f (its pin is the record's hash, the path is absent)
    shapes['class-unverified'] = guarded(lambda: ran(freeze_world(pre=rev_pre('ok'),
                                                                          classes=(tl_classes, None, False))[0]))
    case('CU-N14', 'a close run\'s REV with two parents, a parent other than its m, a changed existing path, a file added '
                   'in the plan record directory (elsewhere under verification/audits/ than a reconciliation '
                   'directory, R6.RECON.1), a file under a prefix of the context\'s tool-landing class, a file in a '
                   'directory holding a ledgered path, a file outside verification/audits/, a context whose class '
                   'record does not verify at f, or no oi-reconciliation/2 record naming m: custody-run-shape, each '
                   'for its own reason', {k: v.get('error') or v['shape_whys'][:1] for k, v in shapes.items()},
         all(failed_with(o, 'custody-run-shape') and any(want[k] in w_ for w_ in o['shape_whys'])
             for k, o in shapes.items()))
    # a REV whose directory is a prefix of a class other than the tool-landing class: a reconciliation directory
    o = guarded(lambda: ran(freeze_world(pre=rev_pre('ok'), classes=(tl_classes, None))[0]))
    case('CU-N14-OTHER-CLASS', 'the REV\'s directory is a prefix of a class other than the context\'s tool-landing '
                               'class: no custody-run-shape (only the tool-landing class\'s prefixes are excluded)',
         o, 'error' not in o and o['status'] is not None and 'custody-run-shape' not in o['items'])
    # the context's ledgered paths are read at f through its configuration's own ledger adapter (no substitution);
    # a configuration the loader refuses (here: an admission key, which R6.CFG.4 does not have) leaves them unread
    ok = ran(freeze_world(pre=rev_pre('ok'))[0])
    undecided = freeze_world(pre=rev_pre('ok'), admission='chain')[0].run()
    case('CU-REV-LEDGER-UNREADABLE', 'the same REV when the context\'s ledgered paths cannot be read (a configuration '
                                     'the loader refuses): the directory is undecided, custody-run-shape (fail '
                                     'closed)', undecided,
         failed_with(undecided, 'custody-run-shape') and
         any('ledgered paths cannot be read' in w_ for w_ in undecided['shape_whys']))
    case('CU-REV-SHAPE-OK', 'a REV adding one oi-reconciliation/2 record naming m in a reconciliation directory: no '
                            'custody-run-shape (the run results still decide the rest)', ok,
         'custody-run-shape' not in ok['items'])

    def off_main(c, main_before):
        off = c.w.repo.derive(main_before, {'notes/off.txt': b'off\n'}, parents=[main_before], subject='off main')
        return [(off, None)]
    o = freeze_world(pre=off_main)[0].run()
    case('CU-N12', 'a close run whose m is in the store but not reachable from M: custody-unreachable', o,
         failed_with(o, 'custody-unreachable'))
    c = CW(r)
    v0 = c.bootstrap()
    c.succ(v0, [{'f': c.w.M, 'runs': [], 'type': 'close'}])
    o = c.run()
    case('CU-N10', 'a close naming an f that is no context: custody-unsupported', o,
         failed_with(o, 'custody-unsupported'))

    def result(F1, kref, m, outcome='FAIL', **upd):
        res = {'schema': 'oi-ledger-coverage/5', 'operation': 'execution', 'outcome': outcome,
               'config': {'commit': F1, 'blob_sha256': kref['blob_sha256'], 'admission': {'mode': 'chain'}},
               'roles': {'M': m}, 'inputs': {'classify_records': []}}
        res.update(upd)
        return res
    # CU-N35: the close lists (M1, null); results disagree
    c0 = CW(r)
    m1 = c0.w.M
    variants = {}
    c, F1, L, kref = freeze_world(runs=[(m1, None)])
    variants['a: no result'] = c.run()
    for name, mk in (('b: another freeze', lambda F1_, k_: result('7' * 40, k_, m1)),
                     ('c: operation other', lambda F1_, k_: result(F1_, k_, m1, operation='coverage')),
                     ('e: errored only', lambda F1_, k_: result(F1_, k_, m1, outcome='ERROR'))):
        # two passes: the first world gives the freeze's ids (commit ids are content hashes), the second lands
        # results built from them
        c, F1, L, kref = freeze_world(runs=[(m1, None)])
        c2, F2, L2, kref2 = freeze_world(runs=[(m1, None)], results=[mk(F1, kref)])
        variants[name] = c2.run()
    case('CU-N35', 'the close lists (M1, null) and the landed results do not record it (none; another freeze; another '
                   'operation; only an errored result): custody-runs-mismatch', variants,
         all(failed_with(o, 'custody-runs-mismatch') for o in variants.values()))
    c, F1, L, kref = freeze_world(runs=[], results=[result('0' * 40, {'blob_sha256': '0' * 64}, m1)])
    o = c.run()
    case('CU-N26', 'a close with runs [] while a landed result file records a run: custody-runs-mismatch', o,
         failed_with(o, 'custody-runs-mismatch'))
    # a matching run (M1, null): R6.CUST.6 replays it at M1; no witness, so the cited discharge applies
    c, F1, L, kref = freeze_world(runs=[(m1, None)])
    c2, F2, L2, kref2 = freeze_world(runs=[(m1, None)], results=[result(F1, kref, m1)])
    o = c2.run()
    case('CU-P2-REPLAY', 'a closed context whose run (M1, null) matches its landed result: the run replays at M1 with no '
                         'witness, custody is established and the cited discharge applies', o,
         o['status'] == 'established' and not o['witnesses'] and bool(o['reassessments']) and
         'retirement-blocked' not in o['classes'])
    # a run naming a REV: R6.RECON.2 (a) binds the record to the run's X, which no row of the mapping table names
    def rev_run(cc, mb):
        return rev_pre('ok')(cc, mb)
    c, F1, L, kref = freeze_world(pre=rev_run)
    (m_r, rev_r), = c.runs_seen
    o = guarded_run(lambda: freeze_world(pre=rev_run, results=[result(F1, kref, m_r, inputs={
        'classify_records': [{'rev': rev_r}]})])[0].run())
    case('CU-N17-NO-X', 'a run (m, REV) whose landed result records no roles.X: the replay of R6.RECON.2 (a)-(g) has no '
                        'X, so the run does not replay (custody-replay)', o,
         failed_with(o, 'custody-replay') and any('roles.X' in w_ for w_ in o['full_whys']))
    replay_controls(r, freeze_world, result)


def adjudication_run_controls(r, two_pass, pin_q, sib, drop_sib):
    """#1605 sec. 6 rows wired into runs (route 2 as Adjudicated(W, D), the lineage edge U -> P). In the CU-N16 world a
    lineage witness (context F1, run M1, S against Q's edge Q -> P) blocks the current discharge through (r1), which
    only Inapplicable or an adjudication clears. An adjudication J by adj-j, authorized by the owner, reviewed by t,
    lands in a dedicated commit on main; the current configuration, rebuilt at main's tip (in a control-harness run the
    configuration's commit is F'), cites J and its review."""
    from ledger_coverage.engine import adjudication as adjm
    from datetime import datetime as _dt, timezone as _tz

    def world(mut=None, cite=True, land=True, extra_upheld=None):
        c, m = two_pass(world=CW.lineage, cfg_records=pin_q, main_files=sib, pre=drop_sib)
        w = c.w
        q, p_ref = dict(w.repair_entry), dict(w.p_ref)
        sref = {'path': S_PATH, 'blob_sha256': sf.sha(sib[S_PATH])}
        a_bytes = w.files[pfc.RA_PATH]
        A = json.loads(a_bytes)
        aref = {'path': pfc.RA_PATH, 'blob_sha256': sf.sha(a_bytes)}

        def git_at_m(path):
            return w.repo.entries(w.M)[path][1]
        g_s, g_q, g_f, g_a = gitobj.blob_id_of(sib[S_PATH]), git_at_m(q['path']), \
            git_at_m(pfc.RD + 'finding.json'), gitobj.blob_id_of(a_bytes)
        entry = dict(A['repair']['entry'])
        J = {'schema': adjm.schema, 'record_id': 'adj-1', 'supersedes': None, 'author': 'adj-j',
             'authorization': {'quote': 'I authorize adj-j to adjudicate this witness for this replacement.',
                               'author': ra.OWNER_IDENTITIES[0], 'time': '2026-11-27T10:00Z',
                               'source': '#1169 (owner record)', 'adjudicator': 'adj-j',
                               'finding': dict(A['finding']), 'witness_sources': [dict(sref)],
                               'replacement': dict(entry)},
             'finding': dict(A['finding']),
             'witness': {'class': 'lineage', 'disputed': dict(q), 'edge': {'successor': dict(q), 'predecessor': p_ref},
                         'sources': [dict(sref)], 'adverse': [{'ref': dict(sref), 'item': 'edge'}],
                         'original_configuration': dict(c.kref)},
             'replacement': dict(entry), 'reassessment': aref, 'dissents_addressed': [], 'disposition': 'cleared',
             'grounds': [{'id': 'g1', 'target': {'ref': dict(sref), 'item': 'edge'},
                          'reasoning': 'S was withdrawn before any run relied on it; Q -> P stands',
                          'evidence': [g_s, g_q, g_q]}],
             'method': 'read %s %s %s %s' % (g_f, g_s, g_q, g_a), 'conflicts': 'none'}
        if mut:
            mut(J)
        jdir = q['path'].rsplit('/', 1)[0] + '/'
        jp, tp = jdir + 'adj.json', jdir + 'adj.review.json'
        jb = pfc.jb(J)
        T = {'schema': rec.review_schema, 'reviewer': 't', 'reviewed': {'path': jp, 'blob_sha256': sf.sha(jb)},
             'method': 'read %s %s' % (gitobj.blob_id_of(jb), g_s),
             'verdicts': [{'item': i, 'verdict': 'accept', 'reason': 'checked against the git objects'}
                          for i in adjm.item_ids(J)]}
        tb = pfc.jb(T)
        if land:
            lc = c.step({jp: jb, tp: tb}, 'the adjudication lands (dedicated)')
            w.repo.mem[lc]['time'] = int(_dt(2026, 11, 27, 12, 0, tzinfo=_tz.utc).timestamp())
        if extra_upheld is not None:
            extra_upheld(c, J, jdir)
        # the configuration commit is built in place of main's tip (sf.Syn.build derives it with the tip's parents), so
        # one more main commit makes the landing an ancestor of it
        c.step({'notes/after-adjudication.txt': b'later\n'}, 'a later main commit')
        spec = dict(w.build_spec)
        if cite:
            spec['files'] = dict(spec['files'], **{jp: jb, tp: tb})
            spec['add_records'] = list(spec.get('add_records') or []) + [
                {'kind': 'adjudication', 'path': jp, 'blob_sha256': sf.sha(jb)},
                {'kind': 'review', 'path': tp, 'blob_sha256': sf.sha(tb)}]
        w.c, w.p, _s, w.files = w.syn.build(spec, at=w.M)
        o = c.run()
        return o

    def cleared(o):
        return o['status'] == 'established' and bool(o['reassessments']) and \
            'adjudication' in [x[1] for x in o['decisions'] if not x[0]] and 'retirement-blocked' not in o['classes']

    def still_blocked(o, code=None):
        return not o.get('error') and not o['reassessments'] and 'retirement-blocked' in o['classes'] and \
            (code is None or any(code in x['failures'] for x in o['adjudications']))
    o = guarded_run(lambda: world())
    case('ADJ-P-LINEAGE', 'a lineage witness relying through (r1) (S against the operative edge Q -> P); an '
                          'adjudication, edge {Q, P}, sources [S], adverse [{S, edge}], authorized, independent, '
                          'reviewed, landed in a dedicated commit and cited: Adjudicated(W, D), the witness is cleared '
                          'by route adjudication and the discharge applies',
         o.get('error') or [o['decisions'], o['adjudications']],
         cleared(o) and any(e.get('path', '').endswith('/adj.json') and e.get('applies')
                            for f in o['findings'] for e in f.get('adjudications') or []))
    o = guarded_run(lambda: world(mut=lambda J: J['witness'].update(edge={'successor': J['witness']['sources'][0],
                                                                        'predecessor': J['witness']['edge']
                                                                        ['predecessor']})))
    case('ADJ-N-LINEAGE-EDGE-S-P', 'the same adjudication naming the edge {S, P}: the witness does not reproduce (the '
                                   'edge is U -> P), ADJ-BIND, the witness stands', o.get('error') or o['reassess_why'],
         still_blocked(o, 'ADJ-BIND'))
    o = guarded_run(lambda: world(cite=False))
    case('ADJ-N-NOT-CITED-RUN', 'the adjudication landed but not cited by the current configuration: not admitted, the '
                                'witness stands', o.get('error') or o['reassess_why'],
         still_blocked(o) and not o['adjudications'])
    o = guarded_run(lambda: world(mut=lambda J: J['authorization'].update(author='lead')))
    case('ADJ-N-AUTH-NOT-OWNER-RUN', 'the authorization attributed to someone outside OWNER_IDENTITIES: ADJ-AUTH-OWNER, '
                                     'the witness stands', o.get('error') or o['reassess_why'],
         still_blocked(o, 'ADJ-AUTH-OWNER'))
    o = guarded_run(lambda: world(land=False))
    case('ADJ-N-NOT-LANDED-RUN', 'the adjudication cited but never on M\'s first-parent chain: ADJ-LANDED, the witness '
                                 'stands', o.get('error') or o['reassess_why'], still_blocked(o, 'ADJ-LANDED'))

    def upheld(c, J, jdir):
        J2 = json.loads(pfc.jb(J))
        J2.update(record_id='adj-2', author='adj-k', disposition='upheld')
        J2['authorization'].update(adjudicator='adj-k')
        j2b = pfc.jb(J2)
        j2p = jdir + 'adj2.json'
        T2 = {'schema': rec.review_schema, 'reviewer': 't2', 'reviewed': {'path': j2p, 'blob_sha256': sf.sha(j2b)},
              'method': 'read %s %s' % (gitobj.blob_id_of(j2b), J2['grounds'][0]['evidence'][0]),
              'verdicts': [{'item': i, 'verdict': 'accept', 'reason': 'checked'} for i in adjm.item_ids(J2)]}
        lc = c.step({j2p: j2b, j2p[:-5] + '.review.json': pfc.jb(T2)}, 'an upheld adjudication lands, cited by none')
        c.w.repo.mem[lc]['time'] = int(_dt(2026, 11, 27, 13, 0, tzinfo=_tz.utc).timestamp())
    o = guarded_run(lambda: world(extra_upheld=upheld))
    case('ADJ-N-UPHELD-UNCITED-RUN', 'a matching upheld adjudication by another adjudicator, valid for adverse use and '
                                     'cited by none: it contradicts J (ADJ-CONTRA), the witness stands',
         o.get('error') or o['reassess_why'], still_blocked(o, 'ADJ-CONTRA'))


def replay_controls(r, freeze_world, result):
    """R6.CUST.6: each run of each context replayed at its exact m with the context's configuration and selector; its
    witnesses decide the current run's discharges under r9 sec. 2.2 (CU-N16, CU-P9, CU-N18, CU-N20)."""
    def two_pass(m_of=lambda c_: c_.main2, pre=None, **kw):
        # commit ids are content hashes: the first pass gives F1, the run's m and the configuration's reference, the
        # second lands the result naming them
        def wrap(runs):
            if pre is None:
                return None
            def p_(cc, mb):
                pre(cc, mb)
                return runs
            return p_
        c, F1, L, kref = freeze_world(runs=[], pre=wrap([]), **kw)
        m = m_of(c)
        c2, F2, L2, kref2 = freeze_world(runs=[(m, None)], results=[result(F1, kref, m)], pre=wrap([(m, None)]),
                                         **kw)
        c2.kref = kref2
        return c2, m
    Q_REF = lambda c_: c_.w.repair_entry  # noqa: E731
    w0 = CW.lineage(r)
    pin_q = [{'kind': 'reconciliation', 'path': w0.w.repair_entry['path'],
              'blob_sha256': w0.w.repair_entry['blob_sha256']}]
    # the records that land in main2 are drafted from the world without a configuration variant (the same
    # construction CW.lineage uses for the current configuration's references)
    wb = lineage_finding_world(r, edits=pfc.EDITS_REWORDED)
    sib = sibling(wb)
    rp_, rb, zp, zb = replacement(wb)
    repl_files = {rp_: rb, zp: zb}

    def drop_sib(cc, mb):
        # S leaves main after M1 (removal is never a discharge): it stays in R*(M1), and the current scan no longer
        # holds it, so the current freeze's own checks do not see it
        cc.step({x: None for x in sib}, 'S removed from main')
    # CU-N16: F1's configuration pins Q (Q -> P operative from f); sibling S of P lands on main after f and before
    # M1, so S is in R*(M1) and selected by F1's selector. The current freeze cites the same Q (reliance r1) without
    # pinning it: the replayed lineage witness blocks the discharge
    c, m = two_pass(world=CW.lineage, cfg_records=pin_q, main_files=sib, pre=drop_sib)
    o = c.run()
    lw = [x for x in o['witnesses'] if x['kind'] == 'lineage']
    case('CU-N16', 'context F1 pins Q and sibling S of P qualifies over R*(M1) for run (M1, null); the current freeze '
                   'cites the same Q: a lineage witness (context F1, run M1, S) blocks, FAIL record-invalid and '
                   'retirement-blocked', {'o': o, 'lineage': lw},
         o['status'] == 'established' and len(lw) == 1 and lw[0]['run'] == m and
         lw[0]['forming'][0]['path'] == S_PATH and lw[0]['disputed'] == Q_REF(c) and
         'record-invalid' in o['classes'] and 'retirement-blocked' in o['classes'] and not o['reassessments'] and
         len(o['reassess_why']) == 1 and 'blocked by the lineage witness' in o['reassess_why'][0] and
         'r1' in o['reassess_why'][0])
    # CU-N16-TWO-HOP: F1 pins Q (Q -> P -> P2 resolved from f) and S2, a sibling of P under P2, is in R*(M1): the
    # replay checks every edge of Q's lineage, so a lineage witness on the edge P -> P2 blocks
    wb2 = lineage_finding_world(r, edits=pfc.EDITS_REWORDED, two_hop=True)
    s2 = sibling2(wb2)

    def drop_s2(cc, mb):
        cc.step({x: None for x in s2}, 'S2 removed from main')
    c, m = two_pass(world=lambda r_: CW.lineage(r_, two_hop=True), cfg_records=[dict(wb2.repair_entry,
                                                                                      kind='reconciliation')],
                    main_files=s2, pre=drop_s2)
    o = c.run()
    lw = [x for x in o['witnesses'] if x['kind'] == 'lineage']
    case('CU-N16-TWO-HOP', 'context F1 pins Q (Q -> P -> P2) and S2, a sibling of P under P2, is in R*(M1): a lineage '
                           'witness on the edge P -> P2 blocks', {'o': o, 'lineage': lw},
         o['status'] == 'established' and len(lw) == 1 and lw[0]['forming'][0]['path'] == S2_PATH and
         lw[0]['edge'] == [wb2.p_ref['blob_sha256'], wb2.p2_ref['blob_sha256']] and not o['reassessments'] and
         'retirement-blocked' in o['classes'])
    # CU-N16-SELECTOR: as CU-N16 with S's path under a prefix of F1's tool-landing class: not selected, no witness
    tl_sib = pfc.jb({'classes': [{'id': 'tool-landing', 'prefixes': ['verification/audits/syn-sib/']}]})
    c, m = two_pass(world=CW.lineage, cfg_records=pin_q, main_files=sib, pre=drop_sib, classes=(tl_sib, None))
    o = c.run()
    case('CU-N16-SELECTOR', 'as CU-N16 with S under a prefix of F1\'s tool-landing class: F1\'s selector excludes S, no '
                            'lineage witness', o,
         o['status'] == 'established' and not [x for x in o['witnesses'] if x['kind'] == 'lineage'])
    adjudication_run_controls(r, two_pass, pin_q, sib, drop_sib)
    # CU-N17: as CU-N16, but F1's repair Q_rev is admitted through REV1 in run (M1, REV1): Q_rev supersedes Q (the
    # head of the lineage on main) and lies only in REV1 (child of M1); a sibling S of Q_rev (naming Q) is in M1's
    # history, landed and removed before M1, so REV1's scan does not hold it and REV1 admits Q_rev. X is roles.X of the
    # run's landed result (owner decision of 2026-11-27). The REV admission replays, but the repair entry is read in
    # the scanned set of M1 only (mapping table; R6.CUST.9; r9 sec. 2.2: no witness for a frozen discharge that never
    # made the lineage check operative), and Q_rev is not there: custody-replay
    sq = wb.record(record_id='syn-repair', author='writer-s', supersedes=dict(wb.repair_entry))
    sqb = pfc.jb(sq)
    sib_q = {S_PATH: sqb, S_PATH[:-5] + '.review.json': wb.review(S_PATH, sqb)}
    s_add = sib_q
    s_del = dict({x: None for x in sib_q}, **{sf.DOC: wb.repo.read(wb.M, sf.DOC) + b'changed after F1\n'})
    QREV = 'verification/audits/syn-rev/q.json'

    def q_rev_bytes(cc, m_):
        save = cc.w.M
        cc.w.M = m_
        try:
            q = cc.w.record(record_id='syn-repair', author='writer-q2', supersedes=dict(cc.w.repair_entry))
        finally:
            cc.w.M = save
        qb_ = pfc.jb(q)
        return qb_, cc.w.review(QREV, qb_)

    # pass 0: M1 (main2) does not depend on the configuration or the results
    c0, _f, _l, _k = freeze_world(runs=[], world=CW.lineage, main_steps=[s_add], main_files=s_del)
    m1 = c0.main2
    qb_, qrv = q_rev_bytes(c0, m1)
    a_rev = pfc.reassessment(wb, repair={'commits': [wb.repair_commit],
                                         'entry': {'path': QREV, 'blob_sha256': sf.sha(qb_), 'entry_path': sf.DOC}})

    def rev1(cc, mb):
        r1 = cc.w.repo.derive(m1, {QREV: qb_, QREV[:-5] + '.review.json': qrv}, parents=[m1], subject='REV1')
        cc.step({QREV: qb_, QREV[:-5] + '.review.json': qrv}, 'merge REV1', parents=[cc.w.M, r1])
        cc.rev1 = r1
        return [(m1, r1)]
    c1, F1, L1, kref1 = freeze_world(world=CW.lineage, main_steps=[s_add], main_files=s_del, ctx_reassessment=a_rev,
                                     pre=rev1)
    res = result(F1, kref1, m1, inputs={'classify_records': [{'rev': c1.rev1, 'path': QREV, 'sha256': sf.sha(qb_)}]},
                 roles={'M': m1, 'X': c1.w.X})
    o = guarded_run(lambda: freeze_world(world=CW.lineage, main_steps=[s_add], main_files=s_del,
                                         ctx_reassessment=a_rev, pre=rev1, results=[res])[0].run())
    case('CU-N17', 'F1\'s repair Q_rev was admitted through REV1 in run (M1, REV1): REV1\'s admission replays with X '
                   'from the landed result, but Q_rev is not in the scanned set of M1, so the run does not replay '
                   '(custody-replay)', o['full_whys'],
         failed_with(o, 'custody-replay') and any('does not resolve in the scanned set' in w_ for w_ in o['full_whys']))
    # a REV adding one record the route admits (Q_rev) and one it refuses (another M), the landed result recording
    # Q_rev only; the context's repair is Q on main: the REV replays (a refused record is no failure), custody is
    # established; with the landed result recording both records, the admitted sets differ: custody-replay
    QBAD = 'verification/audits/syn-rev2/bad.json'
    bad = json.loads(qb_)
    bad.update(record_id='syn-rev-bad', M='0' * 40, supersedes=None)
    badb = pfc.jb(bad)

    def rev2(cc, mb):
        files = {QREV: qb_, QREV[:-5] + '.review.json': qrv, QBAD: badb,
                 QBAD[:-5] + '.review.json': cc.w.review(QBAD, badb)}
        r2 = cc.w.repo.derive(m1, files, parents=[m1], subject='REV2')
        cc.step(files, 'merge REV2', parents=[cc.w.M, r2])
        cc.rev2 = r2
        return [(m1, r2)]
    c1, F1, L1, kref1 = freeze_world(world=CW.lineage, main_steps=[s_add], main_files=s_del, pre=rev2)
    lst = [{'rev': c1.rev2, 'path': QREV, 'sha256': sf.sha(qb_)}]
    outs = {}
    for name, listing in (('recorded-admitted', lst),
                          ('recorded-both', lst + [{'rev': c1.rev2, 'path': QBAD, 'sha256': sf.sha(badb)}])):
        res2 = result(F1, kref1, m1, inputs={'classify_records': listing}, roles={'M': m1, 'X': c1.w.X})
        outs[name] = guarded_run(lambda res2=res2: freeze_world(world=CW.lineage, main_steps=[s_add],
                                                                main_files=s_del, pre=rev2,
                                                                results=[res2])[0].run())
    # two landed results for the same (M1, REV2) listing different admitted sets: custody-replay
    r_a = result(F1, kref1, m1, inputs={'classify_records': lst}, roles={'M': m1, 'X': c1.w.X})
    r_b = result(F1, kref1, m1, inputs={'classify_records': lst + [{'rev': c1.rev2, 'path': QBAD,
                                                                    'sha256': sf.sha(badb)}]},
                 roles={'M': m1, 'X': c1.w.X})
    o2 = guarded_run(lambda: freeze_world(world=CW.lineage, main_steps=[s_add], main_files=s_del, pre=rev2,
                                          results=[r_a, r_b])[0].run())
    case('CU-N17-RESULTS-DISAGREE', 'two landed results for the same (M1, REV2) list different admitted sets: the run '
                                    'does not replay (custody-replay)', o2.get('error') or o2['full_whys'][:1],
         failed_with(o2, 'custody-replay') and any('disagree on the records' in w_ for w_ in o2['full_whys']))
    case('CU-N17-REFUSED-RECORD', 'a REV with one refused record whose landed result records the admitted one: it '
                                  'replays (custody established); a landed result recording both differs from the '
                                  'replayed admitted set: custody-replay',
         {k: [v['status'], v['full_whys'][:1]] for k, v in outs.items()},
         outs['recorded-admitted']['status'] == 'established' and
         failed_with(outs['recorded-both'], 'custody-replay') and
         any('differ from those its landed result records' in w_ for w_ in outs['recorded-both']['full_whys']))
    # the roles.M filter: two landed results naming the same REV, for M1 and for another M with another X
    from ledger_coverage.engine import category3 as c3m
    repo = gitobj.Overlay()
    rx = {'path': 'verification/audits/syn-plan/config.json', 'blob_sha256': '0' * 64}
    d_ = 'verification/audits/syn-plan/op-c-runs/'
    lst_ = [{'rev': 'e' * 40, 'path': QREV, 'sha256': '1' * 64}]
    files = {d_ + 'a/result.json': pfc.jb({'outcome': 'FAIL', 'roles': {'M': 'a' * 40, 'X': 'b' * 40},
                                           'inputs': {'classify_records': lst_}}),
             d_ + 'b/result.json': pfc.jb({'outcome': 'FAIL', 'roles': {'M': 'c' * 40, 'X': 'd' * 40},
                                           'inputs': {'classify_records': lst_}})}
    land_ = repo.add_commit(files, [])
    try:
        got = c3m.run_roles_x(repo, {'config': rx, 'landing': land_}, 'a' * 40, 'e' * 40)[0]
    except c3m.ReplayFailure as exc:
        got = 'ReplayFailure: %s' % exc
    case('CU-N17-ROLES-M-FILTER', 'two landed results naming the same REV, for M1 and for another M with another X: '
                                  'the replay reads the X of the result whose roles.M is M1', got, got == 'b' * 40)
    # the same run with REV1's record failing R6.RECON.2 in the replay (the result names another X): custody-replay
    res_bad = dict(res, roles={'M': m1, 'X': '7' * 40})
    o = guarded_run(lambda: freeze_world(world=CW.lineage, main_steps=[s_add], main_files=s_del,
                                         ctx_reassessment=a_rev, pre=rev1, results=[res_bad])[0].run())
    case('CU-N17-REV-NOT-ADMITTED', 'the same run whose landed roles.X differs from the X REV1\'s record binds: REV1 '
                                    'does not replay under R6.RECON.2 (a), custody-replay', o,
         failed_with(o, 'custody-replay') and any('R6.RECON.2' in w_ for w_ in o['full_whys']))
    # CU-N16-ROUTE: as CU-N16, with the run's m a foxtrot commit whose first-parent chain lacks the repair commit
    # (main2, with S, is its second parent): the original positive route was not operative at m, so S forms no
    # lineage witness
    c, m = two_pass(world=CW.lineage, cfg_records=pin_q, main_files=sib, pre=drop_sib, landing_kind='foxtrot-m',
                    m_of=lambda c_: c_.fox)
    o = c.run()
    case('CU-N16-ROUTE', 'as CU-N16 with the run\'s m a commit whose first-parent chain lacks the repair commit: the '
                         'positive route was not operative at m, so no lineage witness', o,
         o['status'] == 'established' and not [x for x in o['witnesses'] if x['kind'] == 'lineage'])
    # CU-X4: the current freeze cites A2, whose repair is the replacement R' (reliance only through r3), and does
    # not admit R'. Context F1 cites A (repair Q), pins Q and pins R' with its accepting review Z: a replayed
    # context supplies no NR-2 admission, so the lineage witness blocks
    pin_r = [{'kind': 'reconciliation', 'path': rp_, 'blob_sha256': sf.sha(rb)},
             {'kind': 'review', 'path': zp, 'blob_sha256': sf.sha(zb)}]

    def repl_world(cite_repl):
        return lambda r_: CW.lineage(r_, repl=True, cite_repl=cite_repl)
    c, m = two_pass(world=repl_world(False), cfg_records=pin_q + pin_r, main_files=dict(sib, **repl_files),
                    pre=drop_sib, ctx_reassessment=pfc.reassessment(wb), f_files=repl_files)
    o = c.run()
    lw = [x for x in o['witnesses'] if x['kind'] == 'lineage']
    case('CU-X4', 'context F1 pins Q and admits R\' with an accepting review; the current freeze cites A2 (repair R\', '
                  'reliance only r3) without admitting R\': NR-2 is not met, the lineage witness blocks', {'o': o},
         o['status'] == 'established' and len(lw) == 1 and not o['reassessments'] and
         len(o['reassess_why']) == 1 and 'blocked by the lineage witness' in o['reassess_why'][0] and
         o['reassess_why'][0].endswith('clauses r3'))
    # countercontrol: the same world with the current freeze admitting R' and Z (NR-1 to NR-4 hold): the witness is
    # cleared and the discharge applies
    c, m = two_pass(world=repl_world(True), cfg_records=pin_q + pin_r, main_files=dict(sib, **repl_files),
                    pre=drop_sib, ctx_reassessment=pfc.reassessment(wb), f_files=repl_files)
    o = c.run()
    case('CU-X4-COUNTER', 'the CU-X4 world with the current freeze admitting R\' and its review Z, whose method holds '
                          'the git blob ids of Q and S: NR-1 to NR-4 hold, the witness is cleared and the discharge '
                          'applies', o,
         o['status'] == 'established' and bool(o['reassessments']) and len(o['witnesses']) >= 1 and
         'retirement-blocked' not in o['classes'] and
         ('non-reliance (NR-1 to NR-4)' in [x[1] for x in o['decisions'] if not x[0]]))
    # CU-X1: the CU-X4 world, plus a later context F3 citing A2 that admits R' with a review Z' by another reviewer
    # lacking NR-4's tokens, with its own close: a later context is not a clearance; F1's witness still blocks
    zb3 = json.loads(zb)
    zb3.update(reviewer='reviewer-other', method='read every object')
    zb3 = pfc.jb(zb3)
    z3p = 'verification/audits/syn-plan3/z.review.json'
    c, m = two_pass(world=repl_world(False), cfg_records=pin_q + pin_r, main_files=dict(sib, **repl_files),
                    pre=drop_sib, ctx_reassessment=pfc.reassessment(wb), f_files=repl_files,
                    extra_ctx={'records': [pin_r[0], {'kind': 'review', 'path': z3p, 'blob_sha256': sf.sha(zb3)}],
                               'files': {z3p: zb3}})
    o = c.run()
    lw = [x for x in o['witnesses'] if x['kind'] == 'lineage']
    case('CU-X1', 'the CU-X4 world with a later closed context F3 admitting R\' under a review lacking NR-4\'s tokens: '
                  'F1\'s lineage witness still blocks (no clearance route)', {'o': o},
         o['status'] == 'established' and o['contexts'] == 2 and len(lw) == 1 and
         lw[0]['context'] != getattr(c, 'F3', None) and
         not o['reassessments'] and any('blocked by the lineage witness' in x for x in o['reassess_why']))
    # CU-P9: S lands on main only after M1, so S is not in R*(M1): no witness from custody, the discharge applies
    def after(cc, mb):
        cc.step(sib, 'S lands after M1')
        drop_sib(cc, mb)
    c, m = two_pass(world=CW.lineage, cfg_records=pin_q, pre=after)
    o = c.run()
    case('CU-P9', 'F1\'s only run is (M1, null) and sibling S lands after M1: S is not in R*(M1), no witness, PASS', o,
         o['status'] == 'established' and not o['witnesses'] and bool(o['reassessments']))
    # the same world with F1 not pinning Q: Q found only by the entry lookup at M1 has no lineage check, so S is no
    # witness. F1 pins P instead (with its review), so that Q's directory is read at f and Q's edge resolves there
    # without failure: the only condition that fails is that F1 does not cite Q
    pp = P_PATH[:-5] + '.review.json'
    pin_p = [dict(wb.p_ref, kind='reconciliation'),
             {'kind': 'review', 'path': pp, 'blob_sha256': sf.sha(wb.repo.read(wb.M, pp))}]
    c, m = two_pass(world=CW.lineage, main_files=sib, pre=drop_sib, cfg_records=pin_p)
    o = c.run()
    case('CU-P9-UNPINNED', 'the CU-N16 world with F1 not pinning Q: a repair found solely by the entry lookup at m has '
                           'no lineage check, so S forms no witness and the discharge applies', o,
         o['status'] == 'established' and not o['witnesses'] and bool(o['reassessments']))
    # CU-N20: as CU-N16, then a foxtrot fast-forward takes M1 and Q's repair commit off the current M's first-parent
    # chain; the replay evaluates the positive route at M1, so the witness stands
    c, m = two_pass(world=CW.lineage, cfg_records=pin_q, main_files=sib, pre=drop_sib, landing_kind='foxtrot-m')
    o = c.run()
    lw = [x for x in o['witnesses'] if x['kind'] == 'lineage']
    case('CU-N20', 'as CU-N16, with a foxtrot fast-forward after M1 putting M1 and the repair commit off the current '
                   'first-parent chain: the replay at M1 still yields the lineage witness (context F1, run M1, S)',
         {'o': o, 'lineage': lw}, len(lw) == 1 and lw[0]['run'] == m and 'retirement-blocked' in o['classes'] and
         not o['reassessments'])
    # a review witness: an adverse non-author review of Q lands in Q's directory before M1 and leaves main after it;
    # the replay qualifies it over R*(M1) and reports it
    qd = w0.w.repair_entry['path'].rsplit('/', 1)[0] + '/'
    qdoc = json.loads(w0.w.repo.read(w0.w.M, w0.w.repair_entry['path']))
    adverse = pfc.jb({'schema': rec.review_schema, 'reviewer': 'reviewer-adverse', 'reviewed': dict(w0.w.repair_entry),
                      'method': 'read', 'verdicts': [{'item': i, 'verdict': 'reject', 'reason': 'x'}
                                                     for i in rec.item_ids(qdoc)]})
    adv = {qd + 'q.adverse.review.json': adverse}

    def drop_adv(cc, mb):
        cc.step({x: None for x in adv}, 'the adverse review leaves main')
    c, m = two_pass(world=CW.lineage, main_files=adv, pre=drop_adv)
    o = c.run()
    rw = [x for x in o['witnesses'] if x['kind'] == 'review']
    case('CU-REPLAY-REVIEW-WITNESS', 'an adverse non-author review of Q in R*(M1), removed from main later: the replay '
                                     'qualifies a review witness against Q (context F1, run M1) and reports it', o,
         len(rw) == 1 and rw[0]['disputed'] == w0.w.repair_entry and rw[0]['run'] == m and
         rw[0]['forming'][0]['path'] == qd + 'q.adverse.review.json' and 'retirement-blocked' in o['classes'])
    # CU-N18: the run's m precedes the finding (it does not resolve in R*(m)), or precedes the repair record (the
    # repair entry does not resolve in the scanned set of m): custody-replay
    def before(path):
        def m_of(c_):
            cur = c_.main2
            while c_.w.repo.read(cur, path) is not None:
                cur = c_.w.repo.parents(cur)[0]
            return cur
        return m_of
    neg = {}
    for name, path in (('finding', pfc.RD + 'finding.json'), ('repair entry', 'verification/audits/syn-repair/'
                                                                              'repair.json')):
        c, m = two_pass(m_of=before(path))
        neg[name] = c.run()
    want = {'finding': 'does not resolve in R*(m)', 'repair entry': 'does not resolve in the scanned set'}
    case('CU-N18', 'the reassessment\'s finding does not resolve in R*(m), or its repair entry does not resolve at m: '
                   'custody-replay, each for its own reason', {k: v['full_whys'] for k, v in neg.items()},
         all(failed_with(o, 'custody-replay') and any(want[k] in w_ for w_ in o['full_whys']) for k, o in neg.items()))


def unit_controls(r):
    """Checks a harness run cannot reach: the run's own F (CU-N28), the R6.CUST.10 gate mode, the review item ids."""
    from ledger_coverage.engine import category3 as c3m, config as cfgmod, recon_route
    KD = 'verification/audits/syn-plan/'
    KP = KD + 'config.json'
    c = CW(r)
    v0 = c.bootstrap()
    base = c.w.M
    kb = config_doc(c.w)
    F1 = c.w.repo.derive(base, {KP: kb, KD + 'PREREG.md': ('### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n'
                                                             '| `config.json` | `%s` |\n' % sf.sha(kb)).encode()},
                         parents=[base], subject='F1')
    main2 = c.step({'notes/m.txt': b'm\n'})
    L = c.step({}, 'land', parents=[main2, F1])
    c.succ(v0, [{'config': {'path': KP, 'blob_sha256': sf.sha(kb)}, 'f': F1, 'landing': L, 'type': 'freeze'},
                {'f': F1, 'runs': [], 'type': 'close'}])
    saved = ra.custody_bootstrap_blob
    ra.custody_bootstrap_blob = c.boot
    try:
        cum = c3m.Cumulative(c.w.repo, [c.w.M], ('oi-reconciliation/1', 'oi-reconciliation/2'),
                             recon_route.audits_root)
        chk = cust.Check(c.w.repo, c.w.M, F1, PATH, c.boot, cum, recon_route.audits_root, cfgmod.read_pin_table,
                         recon_route.audits_root)
        rep = chk.run()
        chk2 = cust.Check(c.w.repo, c.w.M, None, PATH, c.boot, cum, recon_route.audits_root, cfgmod.read_pin_table,
                          recon_route.audits_root)
        rep2 = chk2.run()
    finally:
        ra.custody_bootstrap_blob = saved
    case('CU-N28', 'the run\'s own F is the f of a closed context: custody-closed-freeze (the same custody without that '
                   'F is established)', {'with_F1': rep['problems'], 'without': rep2['status']},
         any(p['item'] == 'custody-closed-freeze' for p in rep['problems']) and rep2['status'] == 'established')
    # the gate mode (R6.CUST.10)
    from ledger_coverage.engine import cli
    out = tempfile.mkdtemp(dir=TMP)
    os.rmdir(out)
    ra.custody_bootstrap_blob = c.boot
    try:
        code, res = cli.run(['custody', '--commit', c.w.M, '--out', out], repo=c.w.repo)
        cg = CW(r)
        v0g = cg.bootstrap()
        cg.succ(v0g, [{'f': cg.w.M, 'runs': [], 'type': 'close'}], reviewed=False)
        out2 = tempfile.mkdtemp(dir=TMP)
        os.rmdir(out2)
        ra.custody_bootstrap_blob = cg.boot
        code2, res2 = cli.run(['custody', '--commit', cg.w.M, '--out', out2], repo=cg.w.repo)
    finally:
        ra.custody_bootstrap_blob = saved
    case('CU-GATE', 'the R6.CUST.10 gate mode: a well-formed reviewed custody with a closed context holds (exit 0); an '
                    'unreviewed version adding a close naming no context fails (exit 20) with custody-unreviewed and '
                    'custody-unsupported', {'ok': [code, (res or {}).get('custody', {}).get('status')],
                                            'bad': [code2, sorted({p['item'] for p in (res2 or {}).get('custody', {})
                                                                   .get('problems') or []})]},
         code == 0 and code2 == 20 and {'custody-unreviewed', 'custody-unsupported'} <=
         {p['item'] for p in (res2 or {}).get('custody', {}).get('problems') or []})
    v0d = json.loads(version([{'base': '1' * 40, 'type': 'bootstrap'}]))
    v1d = dict(v0d, entries=v0d['entries'] + [{'blob': '2' * 40, 'type': 'void'}, {'blob': '3' * 40, 'type': 'void'}])
    case('CU-ITEM-IDS', 'R6.CUST.8 item ids are entry:<i> for each index a version adds', cust.item_ids(v1d, v0d),
         cust.item_ids(v1d, v0d) == ['entry:1', 'entry:2'])
    case('CU-PLACEHOLDER', 'the bootstrap blob constant is the marked placeholder until B0 is designated, so no chain '
                           'ends at it', ra.custody_bootstrap_blob, ra.custody_bootstrap_blob.startswith('PLACEHOLDER'))


def live_lineage_controls(r):
    """r9 R6.OBL29.3 on the current run's own lineage checks: where the current configuration cites the repair record
    Q (Q -> P operative from F), a qualifying competing successor S of P in M's ancestry fails the cited discharge
    (FAIL record-invalid), with or without custody."""
    wb = lineage_finding_world(r, edits=pfc.EDITS_REWORDED)
    sib = sibling(wb)
    live_why = 'competing successor %s in M\'s ancestry' % S_PATH

    def world(cite_q=True, s_files=None, boot=True):
        c = CW.lineage(r, cite_q=cite_q)
        if boot:
            c.bootstrap()
        if s_files:
            # S lands on main and leaves it again: it stays in M's ancestry, and neither F nor M's tree holds it
            c.step(s_files, 'S lands')
            c.step({x: None for x in s_files}, 'S removed')
        return c.run()

    def live(o):
        return [x for x in o['reassess_why'] if live_why in x]
    o = world(s_files=sib)
    case('LIVE-N', 'the current freeze cites Q (Q -> P operative from F) and sibling S of P is in M\'s ancestry: FAIL '
                   'record-invalid for the cited discharge naming S, and retirement-blocked', o,
         o['status'] == 'established' and live(o) and not o['reassessments'] and
         'retirement-blocked' in o['classes'])
    o = world(s_files=sib, boot=False)
    case('LIVE-N-NOCUSTODY', 'the same without any custody record: the competing successor still fails the discharge '
                             '(with or without custody)', o, o['status'] == 'unestablished' and live(o) and
         not o['reassessments'])
    o = world()
    case('LIVE-P', 'the current freeze cites Q and no competing successor of P is in M\'s ancestry: no live lineage '
                   'failure, the discharge applies', o, o['status'] == 'established' and not live(o) and
         bool(o['reassessments']))
    other = json.loads(sib[S_PATH])
    other['record_id'] = 'syn-other-lineage'
    ob = pfc.jb(other)
    o = world(s_files={S_PATH: ob, S_PATH[:-5] + '.review.json': wb.review(S_PATH, ob)})
    case('LIVE-OTHER-LINEAGE', 'a record naming the same P in supersedes but of another lineage: not a competing '
                               'successor under R6.REC.7, the discharge applies', o,
         not live(o) and bool(o['reassessments']))
    o = world(cite_q='without-p', s_files=sib)
    case('LIVE-EDGE-UNRESOLVED', 'the current freeze cites Q but P is not at F, so Q\'s required lineage does not '
                                 'resolve under its anchor: the discharge is inapplicable (FAIL record-invalid) and '
                                 'the finding stays retirement-blocked', o,
         any('required lineage of the cited repair record' in x and 'does not resolve' in x
             for x in o['reassess_why']) and not o['reassessments'] and 'retirement-blocked' in o['classes'])
    o = world(cite_q='without-p-review')
    case('LIVE-EDGE-LINT', 'the current freeze cites Q and P resolves at F without its review: Q\'s required lineage '
                           'check fails, so the discharge is inapplicable (FAIL record-invalid, retirement-blocked)', o,
         any('required lineage check of the cited repair record' in x for x in o['reassess_why']) and
         not o['reassessments'] and 'retirement-blocked' in o['classes'])
    # two hops: Q -> P -> P2 cited and resolved from F; S2, a sibling of P under P2, is in M's ancestry
    wb2 = lineage_finding_world(r, edits=pfc.EDITS_REWORDED, two_hop=True)
    s2 = sibling2(wb2)

    def world2(s_files, **kw):
        c = CW.lineage(r, cite_q=True, two_hop=True, **kw)
        c.bootstrap()
        if s_files:
            c.step(s_files, 'S2 lands')
            c.step({x: None for x in s_files}, 'S2 removed')
        return c.run()
    o = world2(s2)
    case('LIVE-TWO-HOP', 'the current freeze cites Q (Q -> P -> P2 resolved from F) and S2, a sibling of P under P2, '
                         'is in M\'s ancestry: the second edge is checked, FAIL record-invalid naming S2', o,
         any(('competing successor %s' % S2_PATH) in x for x in o['reassess_why']) and not o['reassessments'] and
         'retirement-blocked' in o['classes'])
    o = world2(None)
    case('LIVE-TWO-HOP-P', 'the same two-hop lineage with no competing successor: the discharge applies', o,
         not o['reassess_why'] and bool(o['reassessments']))
    # the current configuration's selector: S under a prefix of its tool-landing class is not selected
    c = CW.lineage(r, cite_q=True, tl_prefix='verification/audits/syn-sib/')
    c.bootstrap()
    c.step(sib, 'S lands')
    c.step({x: None for x in sib}, 'S removed')
    o = c.run()
    case('LIVE-SELECTOR', 'S lies under a prefix of the current configuration\'s tool-landing class: the R6.RECON.2 '
                          '(d) selector excludes it, no live lineage failure', o,
         not live(o) and not any('required lineage' in x for x in o['reassess_why']))
    o = world(cite_q=False, s_files=sib)
    case('LIVE-UNCITED', 'S in M\'s ancestry but the current freeze does not cite Q (Q found only by the entry lookup at '
                         'M): no lineage check is operative, the discharge applies', o,
         not live(o) and bool(o['reassessments']))


def amendment_1_controls(r):
    """r9 Amendment 1 (adopted at e79e7ca9): provisional blocks and genuine findings. A second-kind review whose
    reviewed names a record absent from R* is a provisional block (FAIL record-invalid and retirement-blocked, A1.3);
    once the exact record is in R* it resolves: disqualified when the record's author is the reviewer, otherwise a
    genuine finding, permanent where the record has a durable witness in M's ancestry (A1.1, A1.2); Keys (b) applies
    only while the record is absent from the run's whole R* (A1.4)."""
    QP = pfc.RD + 'q.json'
    item = sf.DOC + ':scientific_effect'

    def records(reviewer, q_author, zp=pfc.RD + 'q.second.review.json'):
        w0 = pfc.World(r)
        qb = pfc.jb(w0.record(record_id='syn-recon-q', author=q_author))
        inv = pfc.invalidating(w0, sf.DOC)['paths'][0]['scientific_effect']
        verdicts = [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(json.loads(qb))]
        for v in verdicts:
            if v['item'] == item:
                v.update(verdict='invalidates', reason='the change invalidates the planned edit',
                         invalidated=inv['invalidated'], configuration=inv['configuration'])
        zb = pfc.jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': {'path': QP,
                                                                                     'blob_sha256': sf.sha(qb)},
                     'method': 'read ' + 'a' * 40, 'verdicts': verdicts})
        return qb, zb, zp

    def a_null(zp, zb):
        return {'schema': 'oi-reassessment/1', 'record_id': 'syn-reassessment-null', 'author': sf.WRITER,
                'supersedes': None, 'finding': {'path': zp, 'blob_sha256': sf.sha(zb), 'item': item},
                'repair': None, 'edit': None,
                'rederivation': 'control fixture: the review names no record the scan finds (Keys (b))',
                'verdict': 'no-effect'}

    def world(variant=None):
        c = CW.__new__(CW)
        c.w = pfc.World(r, variant=variant)
        c.boot, c.n = None, 0
        c.bootstrap()
        return c

    def z_finding(o, zp):
        return [f for f in o['findings'] if (f.get('record') or {}).get('path') == zp]

    def provisional(o, zp):
        return o['exit'] == 20 and 'retirement-blocked' in o['classes'] and 'record-invalid' in o['classes'] and \
            zp in o['blocked'] and bool(z_finding(o, zp)) and \
            any('names no record the scan finds' in d for d in o['reassess_why'] + o['invalid_details'])

    def genuine(o, zp):
        return 'retirement-blocked' in o['classes'] and zp in o['blocked'] and bool(z_finding(o, zp)) and \
            not any('names no record the scan finds' in d for d in o['invalid_details'])

    qb, zb, ZP = records('reviewer-x', 'writer-q')
    c = world()
    c.step({ZP: zb}, 'the invalidating review lands first')
    before = c.run()
    c.step({QP: qb}, 'the named record lands, another author')
    after = c.run()
    case('A1-INDEPENDENT-RECORD-LANDS-LATER', 'before the record lands: FAIL record-invalid and retirement-blocked '
                                              '(A1.3); after, with another author: a genuine finding that binds',
         {'before': before['classes'], 'after': after['classes']}, provisional(before, ZP) and genuine(after, ZP))
    c.step({QP: None, ZP: None}, 'the record and the review are deleted')
    o = c.run()
    case('A1-INDEPENDENT-RECORD-THEN-DELETED', 'the record and the review deleted from later trees: the genuine finding '
                                               'still binds (A1.1, R6.OBL29.6)', o['classes'], genuine(o, ZP))
    c = world()
    c.step({ZP: zb}, 'the review lands')
    for i in range(3):
        c.step({'notes/n%d.txt' % i: b'n\n'}, 'later commit %d' % i)
    o = c.run()
    case('A1-PROVISIONAL-RECORD-NEVER-LANDS', 'the named record never enters R*: FAIL record-invalid and '
                                              'retirement-blocked at a later M', o['classes'], provisional(o, ZP))
    qb_s, zb_s, _ = records('reviewer-x', 'reviewer-x')
    forged = json.loads(qb_s)
    forged['record_id'] = 'syn-recon-forged'
    c = world()
    c.step({ZP: zb}, 'the review lands')
    c.step({QP: pfc.jb(forged)}, 'a byte-different record at the named path, author the reviewer')
    o = c.run()
    case('A1-PROVISIONAL-FORGED-SAME-PATH', 'a byte-different record at the named path whose author is the reviewer: '
                                            'another reference, the block stays provisional', o['classes'],
         provisional(o, ZP))
    c = world()
    c.step({ZP: zb}, 'the review lands')
    c.step({QP: qb}, 'the record lands, another author')
    c.step({QP: pfc.jb(forged)}, 'a byte-different record at the same path naming the reviewer as author')
    o = c.run()
    case('A1-GENUINE-THEN-SAME-PATH-REWRITE', 'after the genuine finding, a byte-different record at the same path '
                                              'naming the reviewer as author: the genuine finding still binds (A1.2)',
         o['classes'], genuine(o, ZP))
    c = world()
    c.step({ZP: zb}, 'the review lands')
    copy_q = json.loads(qb)
    copy_q['author'] = 'reviewer-x'
    c.step({pfc.RD + 'q-copy.json': qb, pfc.RD + 'q-forged.json': pfc.jb(copy_q)},
           'a byte-identical copy at another path')
    o = c.run()
    case('A1-PROVISIONAL-COPY-AT-OTHER-PATH', 'a byte-identical copy of the named record at another path while the '
                                              'named reference stays absent: the block stays provisional', o['classes'],
         provisional(o, ZP))
    qb1, zb1, Z1 = records('writer-q', 'writer-q', pfc.RD + 'q.self.review.json')
    _qb2, zb2, Z2 = records('reviewer-y', 'writer-q', pfc.RD + 'q.other.review.json')
    c = world()
    c.step({Z1: zb1, Z2: zb2}, 'two invalidating reviews name the same record')
    c.step({QP: qb1}, 'the record lands, its author the first reviewer')
    o = c.run()
    case('A1-TWO-REVIEWS-ONE-RECORD', 'two reviews name the same record, one by its eventual author: the first is '
                                      'disqualified, the second is a genuine finding that binds',
         {'z1': z_finding(o, Z1), 'z2_blocked': Z2 in o['blocked']}, not z_finding(o, Z1) and genuine(o, Z2))
    # Keys (b), A1.4
    c = world(pfc.cite(a_null(ZP, zb)))
    c.step({ZP: zb}, 'the review lands')
    before = c.run()
    c.step({QP: qb}, 'the named record lands, another author')
    after = c.run()
    case('A1-PROVISIONAL-NULL-DISCHARGE-THEN-INDEPENDENT-LANDS', 'while provisional, a repair: null reassessment '
                                                                 'under Keys (b) applies; once the named record lands '
                                                                 'with another author the finding binds and the '
                                                                 'reassessment no longer applies (A1.4)',
         {'before': [before['status'], before['reassessments'], before['reassess_why']],
          'after': [after['reassessments'], after['reassess_why'][:2]]},
         bool(before['reassessments']) and ZP not in before['blocked'] and
         not after['reassessments'] and genuine(after, ZP) and
         any('repair is null where an independent reviewer' in d for d in after['reassess_why']))

    # the named record seen only through an explicit input (the configuration cites it, with its review), never on
    # main: r9 R-1. INDEPENDENT-RECORD-VIA-REV-ONLY itself is not built in the control harness: a record REV admits
    # must name the run's M, which holds the review naming that record's bytes (a cycle); the explicit input exercises
    # the same rule (A1.4: entries seen only through F, REV or an explicit input)
    def cite_q_and(doc):
        base = pfc.cite(doc)

        def variant(w_):
            v = base(w_)
            files = dict(v['files'], **{QP: qb})
            review = sf.Syn.chain(None, files, QP, sf.REVIEWER)
            return {'files': files, 'add_records': list(v['add_records']) +
                    [{'kind': 'reconciliation', 'path': QP, 'blob_sha256': sf.sha(qb)}] + review}
        return variant
    c = world(cite_q_and(a_null(ZP, zb)))
    c.step({ZP: zb}, 'the review lands')
    first = c.run()
    later = world(pfc.cite(a_null(ZP, zb)))
    later.step({ZP: zb}, 'the review lands')
    o_later = later.run()
    bare = world()
    bare.step({ZP: zb}, 'the review lands')
    o_bare = bare.run()
    case('A1-INDEPENDENT-RECORD-VIA-EXPLICIT-ONLY', 'the named record, with an independent author, is seen only as an '
                                                    'explicit input (the configuration cites it): the Keys (b) '
                                                    'reassessment does not apply and the genuine finding binds; a '
                                                    'later run that does not read it and cites no reassessment sees '
                                                    'the review provisional again; a later run citing the same Keys '
                                                    '(b) reassessment applies there (the r9 R-1 residual)',
         {'first': [first['reassessments'], first['reassess_why'][:1], ZP in first['blocked']],
          'later-null': [o_later['reassessments'], ZP in o_later['blocked']], 'later-bare': o_bare['classes']},
         not first['reassessments'] and genuine(first, ZP) and
         any('repair is null where an independent reviewer' in d for d in first['reassess_why']) and
         bool(o_later['reassessments']) and ZP not in o_later['blocked'] and provisional(o_bare, ZP))


def amendment_7_keys_controls(r):
    """r13 Amendment 7, Keys as amended: a finding with a valid element naming E1 and an element with an unknown id
    binds E1 and, additively, its lineage at run level. A null-edit reassessment lifts the run-level binding only; a
    reassessment naming E1 lifts E1 only; both together lift the finding."""
    unknown = {'id': 'NO-SUCH-EDIT', 'sha256': '0' * 64,
               'target': {'path': 'nowhere.md', 'start_H': 0, 'old_sha256': '0' * 64}}
    w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED, extra_elems=[unknown])
    a_edit = pfc.reassessment(w1)
    a_null = pfc.reassessment(w1, edit=None, record_id='syn-reassessment-null')

    def cite_all(docs):
        def variant(w_):
            files, recs = {}, []
            for i, d in enumerate(docs):
                p_ = pfc.RA_PATH if i == 0 else 'syn/cfg/reassessment-%d.json' % i
                b = pfc.jb(d)
                files[p_] = b
                recs.append({'kind': 'reassessment', 'path': p_, 'blob_sha256': sf.sha(b)})
                recs += sf.Syn.chain(None, files, p_, sf.REVIEWER)
            return {'files': files, 'add_records': recs}
        return variant

    def run(docs):
        c = CW.__new__(CW)
        c.w = pfc.finding_world(r, variant=cite_all(docs), edits=pfc.EDITS_REWORDED, extra_elems=[unknown])
        c.boot, c.n = None, 0
        c.bootstrap()
        o = c.run()
        return o
    outs = {'edit only': run([a_edit]), 'null only': run([a_null]), 'both': run([a_edit, a_null])}

    def bl(o):
        return o['blocked_full']
    case('A7-KEYS-EDIT-ONLY', 'an applying reassessment naming E1 (C3): E1 is lifted, the run-level binding stays, '
                              'retirement-blocked; the reassessment itself is well formed and applies',
         {k: [v['blocked_full'], v['reassessments'] and len(v['reassessments'])] for k, v in outs.items()},
         [e for _p, e in bl(outs['edit only'])] == [None] and len(outs['edit only']['reassessments'] or []) == 1)
    case('A7-KEYS-NULL-ONLY', 'an applying reassessment with edit null: the run-level binding is lifted, E1 stays '
                              'bound, retirement-blocked on E1 (case 8)', bl(outs['null only']),
         [e for _p, e in bl(outs['null only'])] == ['E1'] and len(outs['null only']['reassessments'] or []) == 1)
    case('A7-KEYS-BOTH', 'both reassessments (C2 and C4): the finding is lifted, not retirement-blocked',
         bl(outs['both']), bl(outs['both']) == [] and 'retirement-blocked' not in outs['both']['classes'])


SUITES = [('schema-chain', schema_chain_controls), ('configurations', configuration_controls),
          ('freeze', freeze_controls), ('unit', unit_controls), ('live-lineage', live_lineage_controls),
          ('amendment-1', amendment_1_controls), ('amendment-7-keys', amendment_7_keys_controls)]
TMP = None


def main(out):
    global TMP
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    TMP = tempfile.mkdtemp(prefix='custody-', dir=out)
    r = sf.Runner(TMP)
    for name, fn in SUITES:
        try:
            fn(r)
        except Exception as exc:  # a suite that cannot run is a failed control of its own
            import traceback
            case(name + '/group-error', 'the suite runs', '%s: %s %s' % (type(exc).__name__, exc,
                                                                          traceback.format_exc()[-1500:]), False)
    with open(os.path.join(out, 'custody-controls.json'), 'w') as f:
        json.dump({'schema': 'oi-local-controls/1', 'suite': 'custody', 'cases': RESULTS}, f, indent=1,
                  sort_keys=True, default=str)
        f.write('\n')
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'custody-controls-out'))
