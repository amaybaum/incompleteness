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


class CW:
    """A cited-discharge world (finding f, repair Q, reassessment A cited by the configuration) with custody commits
    appended on main."""

    def __init__(self, r, cite=True):
        w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
        self.w = pfc.finding_world(r, variant=pfc.cite(pfc.reassessment(w1)) if cite else None,
                                   edits=pfc.EDITS_REWORDED)
        self.boot = None
        self.n = 0

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
                'reassessments': c3.get('reassessments'), 'blocked': [b['record']['path'] for b in c3.get('blocked')
                                                                       or []],
                'classes': sorted({i['class'] for i in out.get('items', [])})}


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


def config_doc(w, admission='chain', reassessment=True):
    d = json.loads(w.files[w.p])
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
    c.step({KP: config_doc(c.w, admission=None)})
    o = c.run()
    case('CU-STOP-ADMISSION', 'a configuration citing a reassessment without an admission key (R6.CFG.4 has none): '
                              'whether it is discharge-bearing is not settled, so the run stops with ERROR '
                              'DESIGN_UNSETTLED', o, o['exit'] == 65 and o['stop'] == 'DESIGN_UNSETTLED')
    c = CW(r)
    c.bootstrap()
    c.step({KP: config_doc(c.w, admission='harness')})
    o = c.run()
    case('CU-N23-HARNESS', 'a configuration citing a reassessment with admission.mode harness is not discharge-bearing '
                           '(no unfrozen entry needed): established', o, o['status'] == 'established')
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
                     config_at_f=True, pre=None, classes=None):
        c = CW(r)
        v0 = c.bootstrap()
        main_before = c.w.M
        kb = config_doc(c.w)
        cls_files = {}
        if classes is not None:
            # roles.side_change_classes names a class record at f; classes = (record bytes, pinned blob_sha256 or None)
            cb, pin = classes
            d = json.loads(kb)
            d['roles'] = dict(d['roles'], side_change_classes={'path': KD + 'classes.json',
                                                               'blob_sha256': pin or sf.sha(cb)})
            kb = pfc.jb(d)
            cls_files = {KD + 'classes.json': cb}
        files = {KD + 'PREREG.md': ('### 1.1 Record pins\n\n| file | sha256 |\n|---|---|\n| `config.json` | `%s` |\n'
                                    % (sf.sha(kb) if prereg_lists else '0' * 64)).encode()}
        if config_at_f:
            files[KP] = kb
        files.update(cls_files)
        F1 = c.w.repo.derive(main_before, files, parents=[main_before], subject='freeze F1')
        tip = F1
        branch = dict(files)
        for i, res in enumerate(results):
            rf = {KD + 'op-c-runs/run%d/result.json' % i: pfc.jb(res)}
            branch.update(rf)
            tip = c.w.repo.derive(tip, rf, parents=[tip], subject='run result')
        main2 = c.step({'notes/main.txt': b'main moves\n'}, 'main moves')
        # a merge's tree carries the branch's files (the in-memory reader derives a tree from its first parent)
        if landing_kind == 'merge':
            L = c.step(branch, 'land F1', parents=[main2, tip])
        elif landing_kind == 'self':
            L = F1
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
        kref = {'path': KP, 'blob_sha256': sf.sha(kb)}
        fe = {'config': kref, 'f': F1, 'landing': L, 'type': 'freeze'}
        ents = [fe]
        if close:
            ents.append({'f': F1, 'runs': [{'m': m, 'rev': rv} for m, rv in runs], 'type': 'close'})
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

    def with_ledger(cw, extra=()):
        # the ledgered paths supplied from the fixture's own ledger (see CU-REV-SHAPE-OK), so that each case fails for
        # its own reason, not for an unreadable ledger; `extra` adds ledgered paths to that set
        real = cli_mod.context_ledger_files
        cli_mod.context_ledger_files = lambda repo: (lambda c_: set((cw.w.led.get('files') or {}).keys()) | set(extra))
        try:
            return cw.run()
        finally:
            cli_mod.context_ledger_files = real
    want = {'plan-dir': 'inside the plan record directory', 'modifies': 'changes more than adding',
            'no-record': 'adds no oi-reconciliation/2 record', 'two-parents': 'exactly the one parent',
            'other-parent': 'exactly the one parent'}
    shapes = {k: with_ledger(freeze_world(pre=rev_pre(k))[0]) for k in want}
    # the class record of the context: a tool-landing class whose prefix holds the REV's file, and another class
    tl_classes = pfc.jb({'classes': [{'id': 'tool-landing', 'prefixes': ['verification/audits/syn-tool/']},
                                     {'id': 'other-class', 'prefixes': ['verification/audits/syn-recon-r/']}]})
    # the reasons are matched on a prefix that fits the truncated `whys` text
    want.update({'tool-landing': 'under a prefix of the tool-landing',
                 'ledgered-dir': 'its directory holds a ledgered or',
                 'outside-audits': 'not under verification/audits/',
                 'class-unverified': 'side-change class'})
    shapes['tool-landing'] = with_ledger(freeze_world(pre=rev_pre('tool-landing'), classes=(tl_classes, None))[0])
    # a ledgered path of the context in the REV file's directory (added to the substituted ledger set)
    shapes['ledgered-dir'] = with_ledger(freeze_world(pre=rev_pre('ok'))[0],
                                         extra=['verification/audits/syn-recon-r/ledgered.md'])
    shapes['outside-audits'] = with_ledger(freeze_world(pre=rev_pre('outside-audits'))[0])
    # roles.side_change_classes pins a blob other than the record at its path at f
    shapes['class-unverified'] = with_ledger(freeze_world(pre=rev_pre('ok'), classes=(tl_classes, '6' * 64))[0])
    case('CU-N14', 'a close run\'s REV with two parents, a parent other than its m, a changed existing path, a file added '
                   'in the plan record directory (elsewhere under verification/audits/ than a reconciliation '
                   'directory, R6.RECON.1), a file under a prefix of the context\'s tool-landing class, a file in a '
                   'directory holding a ledgered path, a file outside verification/audits/, a context whose class '
                   'record does not verify at f, or no oi-reconciliation/2 record naming m: custody-run-shape, each '
                   'for its own reason', {k: v['whys'][:1] for k, v in shapes.items()},
         all(failed_with(o, 'custody-run-shape') and any(want[k] in w_ for w_ in o['whys'])
             for k, o in shapes.items()))
    # the context's configuration carries the synthetic `admission` key that stop 1 requires, which the configuration
    # loader refuses as an unknown key, so its ledgered paths cannot be read through it: an unreadable ledger leaves
    # the directory undecided (custody-run-shape, fail closed); for these cases the ledgered paths are supplied from
    # the fixture's own ledger (an in-process substitution, documented here)
    ok = with_ledger(freeze_world(pre=rev_pre('ok'))[0])
    undecided = freeze_world(pre=rev_pre('ok'))[0].run()
    case('CU-REV-LEDGER-UNREADABLE', 'the same REV when the context\'s ledgered paths cannot be read: the directory is '
                                     'undecided, custody-run-shape (fail closed)', undecided,
         failed_with(undecided, 'custody-run-shape') and any('ledgered paths cann' in w_ for w_ in undecided['whys']))
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
    # a matching run: the replay of R6.CUST.6 is not implemented, so the run stops (fail closed)
    c, F1, L, kref = freeze_world(runs=[(m1, None)])
    c2, F2, L2, kref2 = freeze_world(runs=[(m1, None)], results=[result(F1, kref, m1)])
    o = c2.run()
    case('CU-STOP-REPLAY', 'a closed context with a run matching its landed result: R6.CUST.6 replay is not '
                           'implemented, so the run stops with ERROR NOT_IMPLEMENTED (no discharge applies)', o,
         o['exit'] == 65 and o['stop'] == 'NOT_IMPLEMENTED')


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


SUITES = [('schema-chain', schema_chain_controls), ('configurations', configuration_controls),
          ('freeze', freeze_controls), ('unit', unit_controls)]
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
