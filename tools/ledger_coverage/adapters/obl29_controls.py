"""Local controls for the OBL-29 remedy r9 (verification/audits/foundations/a1exit-obl29-remedy-20261126/, adopted at
77a73c022091f598cf807fcf89d66c3cf43208de): the cumulative record set R*, detection over it, removal never a discharge,
the direct review checks over R*, the result fields and an unreadable history.

The tool detects findings of the first kind only (a reviewed `invalidates` entry of a reconciliation record), so each
control of CONTROLS.json is run here where it is mechanical for that kind; `f` is such a finding landed on main, in
the post-freeze synthetic world of postfreeze_controls.py. The control ids are those of CONTROLS.json; the expectation
rows are not registered by this suite (registration is an adoption act), so its records are local evidence only.

Usage: python3 -I -B tools/ledger_coverage/adapters/obl29_controls.py OUT
Writes OUT/obl29-controls.json and exits 0 when every control holds, 1 otherwise.
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

from ledger_coverage.adapters import control_records  # noqa: E402
from ledger_coverage.adapters.identity_fixture import review_record  # noqa: E402
from ledger_coverage.adapters import synthetic_fixture as sf  # noqa: E402
from ledger_coverage.adapters import postfreeze_controls as pfc  # noqa: E402
from ledger_coverage.engine import records as rec  # noqa: E402
from ledger_coverage.engine import category3 as c3  # noqa: E402

RESULTS = []
# R6.GATE.5 and R6.GATE.7: the runs captured since the previous case are its evidence
LOCAL = control_records.LocalSuite('obl29')
FP = pfc.RD + 'finding.json'


def case(cid, expected, actual, holds, attested=None):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL',
                    'attested': attested})
    LOCAL.case(cid)


def outcome(w, classify=(), **kw):
    code, out = w.run(list(classify), harness=True, **kw)
    out = out or {}
    c3 = out.get('category3') or {}
    fs = [f for f in c3.get('findings') or [] if (f.get('record') or {}).get('path') == FP]
    return {'exit': code, 'classes': sorted({i['class'] for i in out.get('items', [])}),
            'stop': (out.get('stop') or {}).get('class'), 'finding': fs, 'all': c3.get('findings') or [],
            'blocked': [b['record']['path'] for b in c3.get('blocked') or []],
            'reassessments': c3.get('reassessments'),
            'invalid': [d for i in out.get('items', []) if i['class'] == 'record-invalid'
                        for d in (i.get('detail') or [])][:3],
            'reassess_why': [d for i in out.get('items', []) if i['class'] == 'record-invalid' and
                             i.get('subject') == pfc.RA_PATH for d in (i.get('detail') or [])],
            'runlevel': [b['record']['path'] for b in c3.get('blocked') or [] if b.get('edit') is None],
            'form_items': [i.get('evidence') or {} for i in out.get('items', []) if i['class'] == 'record-invalid' and
                           any('form failure of a category-3' in d for d in (i.get('detail') or []))]}


def runlevel_fail(o, path, cls=None):
    """Owner decision 5 (#1169 comment 7207734407): a malformed finding, or one with no readable entry, blocks at run
    level (FAIL retirement-blocked) with FAIL record-invalid, its evidence and provenance kept in the result: the
    finding's path and blob, its witness (source commit) and its detection class."""
    fs = [f for f in o['all'] if (f.get('record') or {}).get('path') == path]
    its = [i for i in o['form_items'] if (i.get('finding') or {}).get('path') == path]
    return o['exit'] == 20 and o['stop'] is None and 'retirement-blocked' in o['classes'] and \
        'record-invalid' in o['classes'] and path in o['runlevel'] and bool(fs) and bool(its) and \
        all(isinstance(f.get('witness'), str) and (f.get('record') or {}).get('blob_sha256') for f in fs) and \
        all(any(f.get('record') == i.get('finding') and f.get('witness') == i.get('source') for f in fs) and
            (cls is None or i.get('class') == cls) for i in its)


def custody_only(o):
    """OBL-29 sec. 2.2 fail-closed: the cited reassessment's only problem is the unestablished custody, so that it
    would apply apart from custody, and the block stands (FAIL record-invalid and retirement-blocked)."""
    # every remaining problem is a custody condition (R6.CUST.9); with no custody record in the fixture that is
    # custody-missing
    return bool(o['reassess_why']) and all(d.startswith('custody-') for d in o['reassess_why']) and \
        'retirement-blocked' in o['classes'] and not o['reassessments']


def refused_for(o, *phrases):
    """The block stands and the cited reassessment is refused for the stated reason (each phrase occurs in one of its
    problems), besides the custody condition."""
    return 'retirement-blocked' in o['classes'] and not o['reassessments'] and \
        all(any(ph in d for d in o['reassess_why']) for ph in phrases)


def blocked(o, present=False, witness=None):
    ok = o['exit'] == 20 and 'retirement-blocked' in o['classes'] and FP in o['blocked'] and len(o['finding']) >= 1
    if ok:
        ok = any(f.get('present_at_M') is present and (witness is None or f.get('witness') == witness)
                 for f in o['finding'])
    return ok


def land_original_plan(w, r):
    """The original plan's configuration files (the base World's) land on w's main, so that a finding naming that
    configuration resolves (R6.RECON.33)."""
    bw = pfc.World(r)
    files = {q: bw.repo.read(bw.c, q) for q, e in bw.repo.entries(bw.c).items()
             if q.startswith('syn/') and e[0] in ('100644', '100755')}
    step(w, {q: b for q, b in files.items() if w.repo.read(w.M, q) != b}, 'the original plan lands')


def landed(r):
    """f landed on main by its own commit c1 (with its review); returns (world, c1, f's bytes)."""
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    c1 = pfc.land(w, [(FP, doc)])
    return w, c1, pfc.jb(doc)


def step(w, files, subject='later main commit', parents=None):
    w.M = w.repo.derive(w.M, files, parents=parents or [w.M], subject=subject)
    return w.M


def removal_controls(r):
    rv = FP[:-5] + '.review.json'
    w, c1, fb = landed(r)
    o = outcome(w)
    case('P-PRESENT-UNCHANGED', 'f present at M: FAIL retirement-blocked; present_at_M true; witness M', o,
         blocked(o, True, w.M))
    w, c1, fb = landed(r)
    step(w, {FP: None, rv: None}, 'delete f')
    o = outcome(w)
    case('N-DEL', 'f deleted after landing: still blocked; present_at_M false; witness c1 (newest on the first-parent '
                  'chain)', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: fb.replace(b'"invalidates"', b'"no-effect"')}, 'rewrite the verdict')
    o = outcome(w)
    case('N-REWRITE-VERDICT', 'the verdict rewritten to no-effect: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: None, rv: None, 'notes/finding.json': fb}, 'move out of verification/audits/')
    o = outcome(w)
    case('N-MOVE-OUT', 'f moved out of the prefix: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: ('symlink', 'elsewhere.json')}, 'replace by a symbolic link')
    o = outcome(w)
    # R6.PUR.12 (SIDE-NONREG): the symbolic link is a side change whose mode is read before any byte; it is
    # side-change-unclassified (not a regular file), never a byte read, and category 3 is evaluated
    case('N-SYMLINK', 'f replaced by a symbolic link: still blocked, present_at_M false', o, blocked(o, False, c1))
    # SIDE-NONREG: a symbolic-link and a submodule side change outside the plan record directory
    w = pfc.World(r)
    # M is H plus the two side changes only (no drift of a ledgered path), so that they decide the outcome
    w.M = w.syn.H
    step(w, {'notes/link': ('symlink', b'target'), 'notes/sub': ('submodule', '9' * 40)}, 'non-regular side changes')
    # the byte reads of the two non-regular paths the run attempts (R6.PUR.12: the mode is read before any byte)
    reads, real_read = [], w.repo.read

    def logged_read(cid, path):
        if path in ('notes/link', 'notes/sub'):
            reads.append(path)
        return real_read(cid, path)
    w.repo.read = logged_read
    try:
        code, out = w.run([], harness=True)
    finally:
        w.repo.read = real_read
    out = out or {}
    nonreg = sorted(i.get('subject') for i in out.get('items', []) if i['class'] == 'side-change-unclassified'
                    and i.get('why') == 'not a regular file')
    # the one run is the evidence of both expectation cases, each binding $p to its path
    run = LOCAL.rec.pending[-1] if LOCAL.rec.pending else None
    if run is not None:
        LOCAL.rec.pending[-1:] = [dict(run, case=n, bindings={'p': q}) for n, q in (
            ('a side change outside the plan record directory that is a symbolic link at M', 'notes/link'),
            ('a side change outside the plan record directory that is a submodule entry at M', 'notes/sub'))]
    att = {'no_exception': code != 70, 'bytes_read_before_type_check': bool(reads)}
    case('SIDE-NONREG', 'a symbolic-link and a submodule side change outside the plan record directory: each '
                        'REVIEW_REQUIRED side-change-unclassified with the reason "not a regular file", no ERROR',
         {'exit': code, 'stop': out.get('stop'), 'nonreg': nonreg, 'reads': reads},
         code != 65 and nonreg == ['notes/link', 'notes/sub'] and
         all(i['decision'] == 'REVIEW_REQUIRED' for i in out.get('items', []) if i['class'] == 'side-change-unclassified'
             and i.get('subject') in nonreg) and not reads,
         attested={n: att for n in ('a side change outside the plan record directory that is a symbolic link at M',
                                    'a side change outside the plan record directory that is a submodule entry at M')})
    # same-blob mode changes: syn/note.txt (a regular file at H) becomes a symbolic link with the same blob id, and
    # syn/witness.md flips from 100644 to 100755 with the same bytes
    note = w.repo.read(w.syn.H, 'syn/note.txt')
    wit = w.repo.read(w.syn.H, 'syn/witness.md')
    w2 = pfc.World(r)
    mode_commit = step(w2, {'syn/note.txt': ('symlink', note), 'syn/witness.md': ('exec', wit)}, 'mode-only changes')
    step(w2, {'notes/after.txt': b'a later commit\n'}, 'a later commit')
    code2, out2 = w2.run([], harness=True)
    out2 = out2 or {}
    items2 = {i.get('subject'): i for i in out2.get('items', []) if i['class'] == 'side-change-unclassified'}
    sides2 = {x.get('path'): x for x in out2.get('side_changes') or []}
    same_blob = w2.repo.entries(w2.M).get('syn/note.txt', (None, None))[1] == \
        w2.repo.entries(w2.syn.H).get('syn/note.txt', (None, None))[1]
    case('SIDE-NONREG-MODE-ONLY', 'a same-blob change from a regular file to a symbolic link is a side change reported '
                                  '"not a regular file"; a same-blob 100644 to 100755 flip is a side change that goes '
                                  'to the classifier (unclassified: no class lists the path)',
         {'exit': code2, 'stop': out2.get('stop'), 'same_blob': same_blob,
          'note': (items2.get('syn/note.txt') or {}).get('why'), 'witness': (items2.get('syn/witness.md') or {}).get('why'),
          'commits': [(sides2.get(q) or {}).get('commit') for q in ('syn/note.txt', 'syn/witness.md')],
          'modes': [((sides2.get(q) or {}).get('h_mode'), (sides2.get(q) or {}).get('m_mode'))
                    for q in ('syn/note.txt', 'syn/witness.md')]},
         code2 != 65 and same_blob and (items2.get('syn/note.txt') or {}).get('why') == 'not a regular file' and
         (items2.get('syn/witness.md') or {}).get('why') == 'no class lists the path' and
         all((sides2.get(q) or {}).get('commit') == mode_commit for q in ('syn/note.txt', 'syn/witness.md')) and
         (sides2.get('syn/note.txt') or {}).get('h_mode') == '100644' and
         (sides2.get('syn/note.txt') or {}).get('m_mode') == '120000' and
         (sides2.get('syn/witness.md') or {}).get('m_mode') == '100755' and
         (items2.get('syn/note.txt') or {}).get('m_mode') == '120000')
    # a mode-only change on a ledgered path: doc/s.md flips 100644 -> 100755 with the same bytes; it is drift
    w3 = pfc.World(r)
    doc_h = w3.repo.read(w3.syn.H, sf.DOC)
    w3.M = w3.repo.derive(w3.syn.H, {sf.DOC: ('exec', doc_h)}, parents=[w3.syn.H], subject='ledgered mode flip')
    code3, out3 = w3.run([], harness=True)
    out3 = out3 or {}
    d3 = [x for x in out3.get('side_changes') or [] if x.get('path') == sf.DOC]
    case('SIDE-NONREG-MODE-LEDGERED', 'a mode-only change (100644 to 100755, same bytes) on a ledgered path is drift: '
                                      'base-drift, with the modes in its evidence',
         {'exit': code3, 'stop': out3.get('stop'), 'entry': d3,
          'classes': sorted({i['class'] for i in out3.get('items', [])})},
         code3 != 65 and len(d3) == 1 and d3[0].get('class') == 'base-drift' and d3[0].get('h_mode') == '100644' and
         d3[0].get('m_mode') == '100755' and 'base-drift' in {i['class'] for i in out3.get('items', [])})
    w, c1, fb = landed(r)
    step(w, {FP: ('submodule', '9' * 40)}, 'replace by a gitlink')
    o = outcome(w)
    case('N-GITLINK', 'f replaced by a gitlink: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: b'\xef\xbb\xbf' + fb}, 'prepend bytes')
    o = outcome(w)
    # the BOM-prefixed file fails the strict parse (R6.RECON.29) and is a class (b) malformed finding with an
    # invalidation signal; a malformed finding blocks at run level (owner decision 5)
    case('N-PREPEND', 'bytes prepended to f: the prefixed copy is a class (b) malformed finding: run-level FAIL '
                      'retirement-blocked and FAIL record-invalid, with its path, blob, witness and class in the '
                      'result, the entry-less reason stated', o,
         runlevel_fail(o, FP, 'b') and any('no readable entry' in d and 'blocks at run level' in d
                                           for d in o['invalid']))
    w, c1, fb = landed(r)
    step(w, {FP: fb[:len(fb) // 2]}, 'truncate')
    o = outcome(w)
    case('N-TRUNCATE', 'f truncated: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    a2 = pfc.RD + 'renamed-1.json'
    step(w, {FP: None, rv: None, a2: fb}, 'rename once')
    step(w, {a2: None, pfc.RD2 + 'renamed-2.json': fb}, 'rename twice')
    o = outcome(w)
    case('N-RENAME-CHAIN', 'f renamed twice: the original reference still blocks', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: None, rv: None}, 'delete')
    step(w, {FP: fb.replace(b'"invalidates"', b'"no-effect"')}, 're-add altered')
    o = outcome(w)
    case('N-READD-ALTERED', 'f deleted and re-added altered: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    for i in range(300):
        step(w, {'notes/n.txt': ('%d\n' % i).encode()} if i else {FP: None, rv: None}, 'step %d' % i)
    o = outcome(w)
    case('N-BOUND-DEPTH', 'f removed and 300 commits follow: still blocked (no depth bound)', o,
         blocked(o, False, c1))
    # supersession, then deletion
    w, c1, fb = landed(r)
    later = pfc.invalidating(w, sf.DOC)
    later['paths'][0]['scientific_effect'] = dict(pfc.CONTROL_EFFECT)
    later['supersedes'] = {'path': FP, 'blob_sha256': sf.sha(fb)}
    c2 = pfc.land(w, [(pfc.RD2 + 'later.json', later)], 'supersede f')
    step(w, {FP: None, rv: None}, 'delete the superseded record')
    o = outcome(w)
    case('N-SUPERSEDE-DELETE', 'f superseded by a no-effect record, then deleted: still blocked; witness c2 (the '
                               'newest first-parent commit holding f)', o, blocked(o, False, c2))


def topology_controls(r):
    rv = FP[:-5] + '.review.json'
    # the finding landed on a side branch merged as a second parent, then deleted
    w = pfc.World(r)
    base = w.M
    doc = pfc.invalidating(w, sf.DOC)
    side = pfc.land(w, [(FP, doc)], 'the finding on a side branch')
    w.M = base
    mainline = step(w, {'notes/m.txt': b'main\n'}, 'main moves')
    merged = w.repo.derive(mainline, {FP: pfc.jb(doc), rv: w.review(FP, pfc.jb(doc))}, parents=[mainline, side],
                           subject='merge the side branch')
    w.M = merged
    step(w, {FP: None, rv: None}, 'delete after the merge')
    o = outcome(w)
    case('N-MERGE-SECOND-PARENT', 'f reached main through a second parent and was then deleted: still blocked; the '
                                  'witness on the first-parent chain (the merge)', o, blocked(o, False, merged))
    # a merge whose resolution drops the record
    w = pfc.World(r)
    base = w.M
    side = pfc.land(w, [(FP, doc)], 'the finding on a side branch')
    w.M = base
    mainline = step(w, {'notes/m.txt': b'main\n'}, 'main moves')
    w.M = w.repo.derive(mainline, {'notes/m.txt': b'main\n'}, parents=[mainline, side], subject='merge dropping f')
    o = outcome(w)
    case('N-MERGE-RESOLUTION', 'a two-parent merge whose resolution drops f: still blocked; witness the side commit',
         o, blocked(o, False, side))
    # add and remove on a branch merged later
    w = pfc.World(r)
    base = w.M
    side = pfc.land(w, [(FP, doc)], 'draft')
    side2 = step(w, {FP: None, rv: None}, 'removed on the branch')
    w.M = base
    mainline = step(w, {'notes/m.txt': b'main\n'}, 'main moves')
    w.M = w.repo.derive(mainline, {'notes/b.txt': b'b\n'}, parents=[mainline, side2], subject='merge the branch')
    o = outcome(w)
    case('N-BRANCH-DRAFT', 'f added and removed on a branch merged with its history: still blocked', o,
         blocked(o, False, side))
    # foxtrot: the old M reached only through a second parent of the new M
    w, c1, fb = landed(r)
    other = w.repo.derive(pfc.World(r).M, {'notes/o.txt': b'o\n'}, parents=[pfc.World(r).M], subject='other line')
    w.M = w.repo.derive(other, {FP: None, rv: None}, parents=[other, c1], subject='foxtrot merge')
    o = outcome(w)
    case('P-FOXTROT', 'the finding\'s commit reachable only through a second parent after a foxtrot merge: still '
                      'found and blocking (all-parent walk; side-change applicability by any-parent ancestry)', o,
         blocked(o, False, c1))
    # a parentless commit carrying the record, merged in and removed in its child
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    root = w.repo.add_commit({FP: pfc.jb(doc), rv: w.review(FP, pfc.jb(doc))}, [], 'a second root')
    w.M = w.repo.derive(w.M, {'notes/r.txt': b'r\n'}, parents=[w.M, root], subject='merge a root')
    o = outcome(w)
    case('N-ROOT', 'f present only at a parentless commit merged into main: still blocked; witness the root', o,
         blocked(o, False, root))
    # a finding only on an unmerged branch (boundary: not reachable)
    w = pfc.World(r)
    base = w.M
    doc = pfc.invalidating(w, sf.DOC)
    pfc.land(w, [(FP, doc)], 'unmerged')
    w.M = base
    step(w, {'notes/m.txt': b'main\n'}, 'main')
    o = outcome(w)
    case('B-UNREACHABLE', 'f only on a branch never merged: not in R*, not reported (the R-1 boundary)', o,
         not o['finding'] and 'retirement-blocked' not in o['classes'])
    # a history rewrite omitting c1 (residual R-2)
    w, c1, fb = landed(r)
    w.M = w.repo.derive(pfc.World(r).M, {'notes/x.txt': b'x\n'}, parents=[pfc.World(r).M], subject='rewritten main')
    o = outcome(w)
    case('B-MAIN-REWRITE', 'a main whose history omits c1: the finding is absent (residual R-2, undetectable by the '
                           'walk)', o, not o['finding'])


def unreadable_controls(r):
    w, c1, fb = landed(r)
    w.M = w.repo.derive(w.M, {'notes/s.txt': b's\n'}, parents=[w.M, '7' * 40], subject='a parent the store lacks')
    o = outcome(w)
    case('N-SHALLOW', 'a reachable parent absent from the store (as in a shallow store): ERROR, no verdict', o,
         o['exit'] == 65 and o['stop'] == 'UNRESOLVABLE')


def positive_controls(r):
    rv = FP[:-5] + '.review.json'
    w = pfc.World(r)
    ne = w.record(record_id='syn-no-effect')
    pfc.land(w, [(FP, ne)])
    step(w, {FP: None, rv: None}, 'remove a non-finding')
    o = outcome(w)
    case('P-NONFINDING-REMOVAL', 'a reviewed no-effect record removed: no finding, not blocked', o,
         not o['finding'] and 'retirement-blocked' not in o['classes'])
    w, c1, fb = landed(r)
    o1, o2 = outcome(w), outcome(w)
    case('P-DETERMINISM', 'the same inputs twice: the same category-3 findings, witnesses and blocked set',
         [o1['finding'], o1['blocked']], o1['finding'] == o2['finding'] and o1['blocked'] == o2['blocked'])
    # a revised plan that no longer carries the edit: the finding remains visible and binds nothing
    w = pfc.World(r, edits=pfc.EDITS_OTHER, first_id=2)
    # the finding was made under the original plan: a readable element for E1 with its target there, naming that
    # plan's configuration, which lands on main and resolves (an unresolvable one binds every configuration at run
    # level, r13 Amendment 7); its E1 is not carried by the revised plan, and E2's old bytes differ from E1's target
    land_original_plan(w, r)
    old_se = pfc.invalidating(pfc.World(r), sf.DOC)['paths'][0]['scientific_effect']
    eff = dict(pfc.CONTROL_EFFECT, conclusions='none', verdict='invalidates', invalidated=old_se['invalidated'],
               configuration=old_se['configuration'])
    # its splice table is the original plan's (R6.RECON.30 beside the tables)
    doc = pfc.rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, pfc.World(r).led, sf.DOC, scientific_effect=eff)
    doc.update(record_id='syn-finding-old-plan', author=sf.WRITER, supersedes=None, M=w.M, X=w.X)
    pfc.land(w, [(FP, doc)])
    step(w, {FP: None, rv: None}, 'delete f')
    o = outcome(w)
    case('P-REMOVE-EDIT', 'the configuration carries no edit the finding binds: not blocked; the finding still '
                          'reported with present_at_M false', o,
         'retirement-blocked' not in o['classes'] and any(f.get('present_at_M') is False for f in o['finding']))


def reassessment_controls(r):
    """Applying and failing reassessments over R*. Two passes as in BLOCK-KEY: the first World gives the finding,
    repair commit and entry; the second cites the reassessment. `after(w)` adds main commits after the repair."""
    def world(mk, after=None, reviewer=sf.REVIEWER):
        w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
        w2 = pfc.finding_world(r, variant=pfc.cite(mk(w1), reviewer), edits=pfc.EDITS_REWORDED)
        if after:
            after(w2)
        return w2

    def adverse(ref_doc, ref_path, reviewer='session.fixture-reviewer-z', verdict='reject', drop_item=False, dissent=None):
        ids = rec.item_ids(ref_doc)
        v = [{'item': i, 'verdict': verdict if k == 0 else 'accept', 'reason': ''} for k, i in enumerate(ids)]
        if drop_item:
            v = v[1:]
        d = review_record({'schema': rec.review_schema, 'reviewer': reviewer,
             'reviewed': {'path': ref_path, 'blob_sha256': sf.sha(pfc.jb(ref_doc))}, 'method': 'read',
             'verdicts': v})
        if dissent:
            d['dissent'] = dissent
        return pfc.jb(d)

    def repair_doc(w):
        return json.loads(w.repo.read(w.M, w.repair_entry['path']))

    o = outcome(world(lambda w1: pfc.reassessment(w1)))
    case('P-REASSESS-CURRENT-BASELINE', 'a reassessment meeting every other condition, all reviews present: its '
                                        'only problem is the unestablished custody (fail closed), the block stands',
         o, custody_only(o))
    case('FAIL-CLOSED-CUSTODY', 'until custody exists every cited discharge fails closed: FAIL record-invalid for the '
                                'reassessment, naming custody, and retirement-blocked', o,
         o['exit'] == 20 and 'record-invalid' in o['classes'] and custody_only(o))

    def delete_finding(w):
        step(w, {FP: None, FP[:-5] + '.review.json': None}, 'delete f')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=delete_finding))
    case('P-REASSESS-AFTER-DELETE', 'f deleted; a reassessment naming its original reference meets every condition but '
                                    'custody (fail closed); f '
                                    'reported with present_at_M false', o,
         custody_only(o) and any(f.get('present_at_M') is False for f in o['finding']))

    def repair_dissent(kind):
        def after(w):
            qd = repair_doc(w)
            q = w.repair_entry['path']
            d = q.rsplit('/', 1)[0] + '/'
            name = d + 'repair.second-review.json'
            b = adverse(qd, q, drop_item=(kind == 'items'), verdict='reject' if kind == 'reject' else 'accept',
                        dissent='the repair does not restore the basis' if kind == 'dissent' else None)
            step(w, {name: b}, 'a second review of the repair')
            step(w, {name: None}, 'delete it')
        return after
    for cid, kind, what in (('N-REPAIR-DISSENT-DELETED', 'reject', 'an eligible review of the repair record '
                                                                   'rejecting an item, in its directory, then deleted'),
                            ('N-HISTORICAL-REVIEW-ITEMS', 'items', 'an eligible review of the repair record omitting '
                                                                   'an item, then deleted'),
                            ('N-REPAIR-DISSENT-FIELD-DELETED', 'dissent', 'an accepting review of the repair record '
                                                                          'with a dissent, then deleted')):
        o = outcome(world(lambda w1: pfc.reassessment(w1), after=repair_dissent(kind)))
        why = {'reject': 'an item is not accepted', 'items': 'an item is omitted', 'dissent': 'it dissents'}[kind]
        case(cid, what + ': the discharge fails (record-invalid, %s) and the block stands' % why, o,
             'record-invalid' in o['classes'] and refused_for(o, 'repair.second-review.json', why))

    def repair_dissent_elsewhere(w):
        qd = repair_doc(w)
        step(w, {'verification/audits/syn-other/repair.review.json': adverse(qd, w.repair_entry['path'])},
             'a rejecting review of the repair in another directory')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=repair_dissent_elsewhere))
    case('P-REPAIR-REVIEW-OTHER-DIRECTORY', 'a rejecting review of the repair record outside its directory does not '
                                            'count for the repair-review check: the reassessment applies', o,
         custody_only(o))

    def reassess_dissent(w):
        a = json.loads(w.repo.read(w.c, pfc.RA_PATH))
        name = 'verification/audits/syn-dissent/reassessment.review.json'
        step(w, {name: adverse(a, pfc.RA_PATH)}, 'a rejecting review of the reassessment')
        step(w, {name: None}, 'delete it')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=reassess_dissent))
    case('N-REASSESS-DISSENT-DELETED', 'an eligible review of the cited reassessment rejecting an item, landed on main '
                                       'and then deleted: the discharge fails and the block stands', o,
         'record-invalid' in o['classes'] and refused_for(o, 'syn-dissent/reassessment.review.json',
                                                          'an item is not accepted'))

    def self_review(w):
        a = json.loads(w.repo.read(w.c, pfc.RA_PATH))
        step(w, {'verification/audits/syn-dissent/self.review.json': adverse(a, pfc.RA_PATH, reviewer=sf.WRITER)},
             'a rejecting review by the reassessment\'s author')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=self_review))
    case('P-HISTORICAL-SELF-REVIEW', 'a rejecting review by the reassessment\'s own author is not eligible: the '
                                     'reassessment meets every condition but custody', o, custody_only(o))

    # an operative predecessor of the reassessment: A supersedes P (same record id, both reviewed in the plan
    # directory); an eligible review of P rejecting an item lands on main and is deleted
    PP = 'syn/cfg/reassessment-p.json'

    def cite_with_predecessor(mk):
        def variant(w_):
            pdoc = mk(w_)
            pdoc = dict(pdoc, rederivation=pdoc['rederivation'] + ' (first version)')
            pb = pfc.jb(pdoc)
            adoc = dict(mk(w_), supersedes={'path': PP, 'blob_sha256': sf.sha(pb)})
            ab = pfc.jb(adoc)
            files, recs = {PP: pb, pfc.RA_PATH: ab}, [{'kind': 'reassessment', 'path': pfc.RA_PATH,
                                                     'blob_sha256': sf.sha(ab)}]
            for q, d, b in ((PP, pdoc, pb), (pfc.RA_PATH, adoc, ab)):
                rv = pfc.jb(review_record({'schema': rec.review_schema, 'reviewer': sf.REVIEWER,
                             'reviewed': {'path': q, 'blob_sha256': sf.sha(b)}, 'method': 'read',
                             'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(d)]}))
                files[q[:-5] + '.review.json'] = rv
                recs.append({'kind': 'review', 'path': q[:-5] + '.review.json', 'blob_sha256': sf.sha(rv)})
            return {'files': files, 'add_records': recs}
        return variant

    def pred_world(after=None):
        w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
        w2 = pfc.finding_world(r, variant=cite_with_predecessor(lambda w_: pfc.reassessment(w1)),
                               edits=pfc.EDITS_REWORDED)
        if after:
            after(w2)
        return w2
    o0 = outcome(pred_world())

    def pred_dissent(w):
        pdoc = json.loads(w.repo.read(w.c, PP))
        name = 'verification/audits/syn-dissent/predecessor.review.json'
        step(w, {name: adverse(pdoc, PP)}, 'a rejecting review of the predecessor')
        step(w, {name: None}, 'delete it')
    o1 = outcome(pred_world(pred_dissent))
    case('P-REASSESS-OPERATIVE-SUPERSEDES', 'a reassessment superseding a reviewed predecessor, every review accepting: '
                                            'the reassessment meets every condition but custody', o0, custody_only(o0))
    case('N-OPERATIVE-PREDECESSOR-DISSENT-DELETED', 'an eligible review of the operative predecessor rejecting an item, '
                                                    'landed and deleted: the discharge fails and the block stands', o1,
         'record-invalid' in o1['classes'] and refused_for(o1, 'predecessor syn/cfg/reassessment-p.json',
                                                           'an item is not accepted'))

    def rewrite(w):
        # verdict no-effect and no invalidated: the rewritten blob carries no finding (Form (i))
        d = json.loads(w.repo.read(w.M, FP))
        se = d['paths'][0]['scientific_effect']
        se['verdict'] = 'no-effect'
        se.pop('invalidated', None)
        step(w, {FP: pfc.jb(d)}, 'rewrite f')
    w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
    rewrite(w1)
    new_ref = {'path': FP, 'blob_sha256': sf.sha(w1.repo.read(w1.M, FP)), 'item': sf.DOC}
    o = outcome(world(lambda w_: pfc.reassessment(w_, finding=new_ref), after=rewrite))
    case('N-FORGED-REASSESS-NEWBLOB', 'a reassessment naming the rewritten blob, which carries no finding: it fails '
                                      'and the original finding still blocks', o,
         'record-invalid' in o['classes'] and refused_for(o, 'not a finding in the cumulative record set'))


def clearance_predicates(r):
    """Sec. 2.2 at the level of its mechanical predicates (engine/obl29.py), over explicit records: the token rule,
    reliance (r1)-(r3), NR-1, NR-3 to NR-5 and the decision. A run does not call them yet (custody format unfixed),
    so these are predicate controls (id suffix -pred), not run outcomes."""
    from ledger_coverage.engine import obl29 as o
    from ledger_coverage.engine.gitobj import blob_id_of
    jb = pfc.jb
    case('TOKEN-RULE-pred', 'tokens split at runs of space, tab, LF and CR; exact bytes only (no case change, '
                            'punctuation or abbreviation)',
         [o.holds('a  b\tc\r\nd', 'c'), o.holds('(abc)', 'abc'), o.holds('ABC', 'abc'), o.holds(None, 'x'),
          o.item_token('a' * 40, 'p q'), o.item_token('A' * 40, 'i')],
         o.holds('a  b\tc\r\nd', 'c') and not o.holds('(abc)', 'abc') and not o.holds('ABC', 'abc') and
         not o.holds(None, 'x') and o.item_token('a' * 40, 'p q') is None and o.item_token('A' * 40, 'i') is None)
    p, p2 = 'doc/s.md', 'doc/t.md'
    Q = {'schema': 'oi-reconciliation/2', 'record_id': 'q', 'author': 'session.fixture-writer-q', 'supersedes': None,
         'paths': [{'path': p, 'side_change_commits': ['c' * 40]}, {'path': p2, 'side_change_commits': ['d' * 40]}]}
    qb = jb(Q)
    qref = {'path': 'verification/audits/q/rec.json', 'blob_sha256': sf.sha(qb)}
    V = review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-v', 'reviewed': dict(qref), 'method': 'read',
         'verdicts': [{'item': i, 'verdict': 'reject' if i == p + ':scientific_effect' else 'accept',
                       'reason': 'the repair does not restore the basis'} for i in rec.item_ids(Q)]})
    vb = jb(V)
    W = {'kind': 'review', 'disputed': qref, 'disputed_doc': Q, 'disputed_git': blob_id_of(qb), 'edge': None,
         'forming': [{'doc': V, 'git': blob_id_of(vb), 'path': 'verification/audits/q/rec.review.json'}],
         'contested': [], 'original': (('f', 'item'), p + ':scientific_effect')}
    fgit = 'f' * 40
    Rd = {'schema': 'oi-reconciliation/2', 'record_id': 'r', 'author': 'session.fixture-writer-r', 'supersedes': None,
          'paths': [{'path': p, 'side_change_commits': ['c' * 40]}]}
    rb = jb(Rd)
    R = {'ref': {'path': 'verification/audits/r/rec.json', 'blob_sha256': sf.sha(rb)}, 'doc': Rd,
         'lineage_blobs': [], 'lineage_edges': []}
    A = {'doc': {'author': 'session.fixture-writer-a'}}

    def D(entry_ref, entry_doc, entry_path=p, finding=(('g', 'x'), 'i'), commits=('e' * 40,)):
        return {'reassessment': A, 'finding': finding, 'lineage_blobs': [], 'lineage_edges': [],
                'repair': {'entry': entry_ref, 'entry_doc': entry_doc, 'entry_path': entry_path,
                           'commits': list(commits)}}
    toks = [o.item_token(W['forming'][0]['git'], p + ':scientific_effect')]
    ftok = o.item_token(fgit, 'i')
    reason = 'the corrected record restores the basis ' + ' '.join(toks)

    def Z(**kw):
        z = review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-v', 'reviewed': dict(R['ref']),
             'method': ' '.join([W['disputed_git'], W['forming'][0]['git']] + toks + [ftok]),
             'verdicts': [{'item': i, 'verdict': 'accept', 'reason': reason} for i in rec.item_ids(Rd)],
             '_dir': 'verification/audits/r'})
        z.update(kw)
        if z.get('independence') == '__drop__':
            z.pop('independence')
        return z
    d_other_entry = D(qref, Q, entry_path=p2)
    got = o.reliance(d_other_entry, W)
    case('N-REFREEZE-OTHER-ENTRY-SAME-Q-pred', 'a discharge citing another entry of the same multi-path disputed record '
                                               'relies through (r1) (and (r3) on shared commits)', got, 'r1' in got)
    copy_ref = {'path': 'verification/audits/copy/rec.json', 'blob_sha256': qref['blob_sha256']}
    got = o.reliance(D(copy_ref, Q), W)
    case('N-REFREEZE-REVIEW-WITNESS-COPY-pred', 'a byte-identical copy of the disputed record at another path relies '
                                                'through (r1)', got, 'r1' in got)
    unrelated = {'schema': 'oi-reconciliation/2', 'record_id': 'q', 'author': 'session.fixture-writer-u', 'supersedes': None,
                 'paths': [{'path': p, 'side_change_commits': ['9' * 40]}]}
    ub = jb(unrelated)
    got = o.reliance(D({'path': 'verification/audits/u/rec.json', 'blob_sha256': sf.sha(ub)}, unrelated,
                       commits=('8' * 40,)), W)
    case('P-UNRELATED-FREEZE-NOT-BURDENED-pred', 'same schema, lineage label and path, different blob, disjoint '
                                                 'commits, another finding: no reliance', got, got == [])
    got = o.reliance(dict(D(R['ref'], Rd), unresolved=True), W)
    case('RELIANCE-UNDECIDABLE-pred', 'a required reference that does not resolve counts as reliance', got,
         got == ['undecidable'])
    dR = D(R['ref'], Rd)
    blocked, clauses, route = o.decide(dR, W, R=R, Z=Z(), nr2=True, finding_git=fgit)
    case('P-REFREEZE-REVIEW-WITNESS-RESOLVED-pred', 'reliance through (r3) only; Z by V\'s reviewer carries every '
                                                    'token and reason: cleared under NR-1, NR-2, NR-4 and NR-5',
         [blocked, clauses, route], not blocked and clauses == ['r3'] and route and 'NR-5' in route)
    # staging S-2 sec. 7: a respelling by case and separator is the same identity (S2.2); a padded string is not an
    # identity string (S2.1), so with it the witness stands
    got = o.decide(dR, W, R=R, Z=Z(reviewer='Session_Fixture-Reviewer-V'), nr2=True, finding_git=fgit)
    case('NR5-SAME-NORMALIZED-REVIEWER-pred', 'Z is by the same reviewer as V under the adopted identity comparison',
         got, not got[0] and got[2] and 'NR-5' in got[2])
    got = o.decide(dR, W, R=R, Z=Z(reviewer=' SESSION.FIXTURE-REVIEWER-V '), nr2=True, finding_git=fgit)
    case('NR5-SAME-NORMALIZED-REVIEWER-pred/padded', 'Z\'s reviewer padded with spaces is not an identity string: '
         'the witness stands', got, got[0])
    negs = [
        ('N-REFREEZE-REVIEW-WITNESS-OTHER-REVIEWER-pred', 'Z by an independent reviewer other than V\'s',
         dict(Z=Z(reviewer='session.fixture-reviewer-x'))),
        ('N-REFREEZE-REVIEW-WITNESS-SELF-pred', 'Z by V\'s reviewer who is also the reassessment\'s author',
         dict(Z=Z(), A_author='session.fixture-reviewer-v')),
        ('NR5-REVIEWER-AUTHOR-ALIAS-pred', 'the reassessment author names the same identity as V and Z',
         dict(Z=Z(), A_author='Session_Fixture-Reviewer-V')),
        ('N-REFREEZE-REVIEW-WITNESS-NO-IDENTITY-pred', 'V\'s reviewer is not an identity string (a URL)',
         dict(Z=Z(reviewer='https://example.invalid/run/1'), V_reviewer='https://example.invalid/run/1')),
        ('NR5-MISSING-ITEM-TOKEN-pred', 'Z\'s method lacks the <b>#<item> token',
         dict(Z=Z(method=' '.join([W['disputed_git'], W['forming'][0]['git'], ftok])))),
        ('NR5-MISSING-FINDING-TOKEN-pred', 'Z\'s method lacks the finding token',
         dict(Z=Z(method=' '.join([W['disputed_git'], W['forming'][0]['git']] + toks)))),
        ('NR5-REASON-pred', 'the reason on the entry item lacks the token',
         dict(Z=Z(verdicts=[{'item': i, 'verdict': 'accept', 'reason': 'fixed'} for i in rec.item_ids(Rd)]))),
        ('NR5-GENERAL-ACCEPT-pred', 'a general accept by V\'s reviewer with no tokens',
         dict(Z=Z(method='read', verdicts=[{'item': i, 'verdict': 'accept', 'reason': 'ok'}
                                           for i in rec.item_ids(Rd)]))),
        ('NR5-DISSENT-pred', 'Z carries a dissent', dict(Z=Z(dissent='still disputed'))),
        ('S2-NR5-UNDECLARED-pred', 'Z carries no independence declaration (staging S-2 S2.4)',
         dict(Z=Z(independence='__drop__'))),
        ('S2-NR5-DECLARED-AUTHOR-pred', 'Z declares a dependency on the author of R (staging S-2 S2.4)',
         dict(Z=Z(independence={'not_author': True, 'depends_on': ['session.fixture-writer-r']}))),
        ('NR5-WRONG-DIRECTORY-pred', 'Z outside R\'s directory', dict(Z=Z(_dir='verification/audits/other'))),
        ('NR5-NO-NR2-pred', 'R not admitted through an operative route (NR-2 false)', dict(Z=Z(), nr2=False)),
        ('NR5-SHA256-SPELLING-pred', 'the SHA-256 of V in place of its git blob id in the <b>#<item> token',
         dict(Z=Z(method=' '.join([W['disputed_git'], W['forming'][0]['git'],
                                   sf.sha(vb) + '#' + p + ':scientific_effect', ftok])))),
    ]
    for cid, what, kw in negs:
        Wv = W
        if 'V_reviewer' in kw:
            Vx = dict(V, reviewer=kw['V_reviewer'])
            Wv = dict(W, forming=[{'doc': Vx, 'git': W['forming'][0]['git'], 'path': W['forming'][0]['path']}])
        dd = D(R['ref'], Rd)
        if 'A_author' in kw:
            dd['reassessment'] = {'doc': {'author': kw['A_author']}}
        b, cl, rt = o.decide(dd, Wv, R=R, Z=kw['Z'], nr2=kw.get('nr2', True), finding_git=fgit)
        case(cid, what + ': the witness stands (blocked)', [b, cl, rt], b and cl == ['r3'])
    rej = review_record({'reviewer': 'session.fixture-reviewer-k', 'reviewed': dict(R['ref']), '_dir': 'verification/audits/r', 'method': 'read',
           'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'} for k, i in
                        enumerate(rec.item_ids(Rd))]})
    b = o.decide(D(R['ref'], Rd), W, R=R, Z=Z(), nr2=True, finding_git=fgit, reviews_of_R=[rej])
    case('NR5-NONACCEPT-REVIEW-pred', 'another eligible review of R rejecting an item without a dissent field: NR-3\'s '
                                      'dissent test fails NR-5, the witness stands', b, b[0] and b[1] == ['r3'])
    V2 = dict(V, reviewer='session.fixture-reviewer-w')
    W2 = dict(W, forming=W['forming'] + [{'doc': V2, 'git': blob_id_of(jb(V2)), 'path': 'v2'}])
    toks2 = toks + [o.item_token(W2['forming'][1]['git'], p + ':scientific_effect')]
    meth = ' '.join([W['disputed_git'], W2['forming'][0]['git'], W2['forming'][1]['git']] + toks2 + [ftok])
    reason2 = 'the corrected record restores the basis ' + ' '.join(toks2)
    zv = Z(method=meth, verdicts=[{'item': i, 'verdict': 'accept', 'reason': reason2} for i in rec.item_ids(Rd)])
    zw = dict(zv, reviewer='session.fixture-reviewer-w')
    b1 = o.decide(D(R['ref'], Rd), W2, R=R, Z=[zv], nr2=True, finding_git=fgit)
    b2 = o.decide(D(R['ref'], Rd), W2, R=R, Z=[zv, zw], nr2=True, finding_git=fgit)
    case('NR5-EVERY-V-pred', 'a review witness formed by two adverse reviews: resolving only the first leaves it '
                             'standing; a resolution by each reviewer clears it', [b1, b2], b1[0] and not b2[0])
    wsp = dict(Q, paths=[{'path': 'doc/s s.md', 'side_change_commits': ['c' * 40]}])
    Vs = review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-v', 'reviewed': dict(qref), 'method': 'read',
          'verdicts': [{'item': 'doc/s s.md', 'verdict': 'reject', 'reason': 'x'}]})
    Ws = dict(W, disputed_doc=wsp, forming=[{'doc': Vs, 'git': blob_id_of(jb(Vs)), 'path': 'x'}])
    got = o.nr5(Z(), Ws['forming'][0], Ws, R, D(R['ref'], Rd), fgit, [])
    case('N-REFREEZE-REVIEW-WITNESS-WHITESPACE-ITEM-pred', 'an adverse item id with a space: no Z can meet NR-5', got,
         got == ['an adverse item id of V cannot form a token'])
    Wl = dict(W, kind='lineage', forming=[{'doc': {}, 'git': 'b' * 40, 'path': 's'}])
    rv = review_record({'reviewer': 'session.fixture-reviewer-n', 'reviewed': dict(R['ref']), '_dir': 'verification/audits/r',
          'method': ' '.join([W['disputed_git'], 'b' * 40]),
          'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(Rd)]})
    b1 = o.decide(dR, Wl, R=R, required_review=rv, excluded=['session.fixture-writer-r', 'session.fixture-writer-q', 'session.fixture-reviewer-v'], nr2=True)
    b2 = o.decide(dR, Wl, R=R, required_review=dict(rv, reviewer='session.fixture-writer-q'),
                  excluded=['session.fixture-writer-r', 'session.fixture-writer-q', 'session.fixture-reviewer-v'], nr2=True)
    b3 = o.decide(dR, Wl, R=R, required_review=dict(rv, method='read'),
                  excluded=['session.fixture-writer-r', 'session.fixture-writer-q', 'session.fixture-reviewer-v'], nr2=True)
    case('P-REFREEZE-INDEPENDENT-REPLACEMENT-pred', 'a lineage witness, reliance through (r3) only, an independent '
                                                    'replacement meeting NR-1 to NR-4: cleared', b1,
         b1[0] is False and b1[2] and 'NR-1' in b1[2])
    ex = ['session.fixture-writer-r', 'session.fixture-writer-q', 'session.fixture-reviewer-v']
    b4 = o.decide(dR, Wl, R=R, required_review={k: v for k, v in rv.items() if k != 'independence'}, excluded=ex,
                  nr2=True)
    b5 = o.decide(dR, Wl, R=R, required_review=dict(rv, independence={'not_author': True,
                                                                      'depends_on': ['session.fixture-writer-q']}),
                  excluded=ex, nr2=True)
    case('S2-NR3-DECLARATION-pred', 'the NR-3 reviewer carries no independence declaration, or declares a dependency '
                                    'on an excluded author (staging S-2 S2.4): the witness stands', [b4, b5],
         b4[0] and b5[0])
    case('N-REFREEZE-NONRELIANCE-UNSUPPORTED-pred', 'the NR-3 reviewer is an excluded author, or NR-4\'s tokens are '
                                                    'absent: the witness stands', [b2, b3], b2[0] and b3[0])
    got = o.decide(dR, Wl, R=R, required_review=dict(rv, reviewer='Session_Fixture-Writer-Q'),
                   excluded=['session.fixture-writer-r', 'session.fixture-writer-q', 'session.fixture-reviewer-v'], nr2=True)
    case('NR3-EXCLUDED-AUTHOR-ALIAS-pred', 'the required reviewer matches an excluded author after normalization',
         got, got[0])
    Rl = dict(R, lineage_blobs=[qref['blob_sha256']])
    b4 = o.decide(dR, Wl, R=Rl, required_review=rv, excluded=[], nr2=True)
    case('NR1-LINEAGE-pred', 'R\'s lineage holds the disputed record\'s blob: NR-1 fails, the witness stands', b4,
         b4[0])
    b5 = o.decide(D(qref, Q), W, R=R, Z=Z(), nr2=True, finding_git=fgit)
    case('N-REFREEZE-INAPPLICABILITY-ASSERTED-pred', 'reliance through (r1) is conclusive: NR evidence cannot clear '
                                                     'it (only Inapplicable(W) or route 2)', b5, b5[0])


def identity_and_set_controls(r):
    """Finding identity by record reference (path and blob) and detection over R* as a set (R6.OBL29.1, .2, .3)."""
    rv = FP[:-5] + '.review.json'
    COPY = pfc.RD + 'finding-copy.json'
    w, c1, fb = landed(r)
    step(w, {COPY: fb, COPY[:-5] + '.review.json': w.review(COPY, fb)}, 'a byte-identical copy with its own review')
    step(w, {FP: None, rv: None}, 'delete the original')
    code, out = w.run([], harness=True)
    refs = sorted({(f['record']['path'], f['record']['blob_sha256']) for f in out['category3']['findings']})
    blocked_paths = sorted({b['record']['path'] for b in out['category3']['blocked']})
    case('COPY-THEN-DELETE', 'f copied byte for byte to a second path (reviewed there), then the original deleted: both '
                             'references are findings (a copy is another record), the original still reported and '
                             'blocking', {'refs': refs, 'blocked': blocked_paths},
         refs == sorted([(FP, sf.sha(fb)), (COPY, sf.sha(fb))]) and FP in blocked_paths)
    f_orig = {'record': {'path': FP, 'blob_sha256': sf.sha(fb)}, 'path': sf.DOC}
    lifted = c3.lifting([({'finding': {'path': COPY, 'blob_sha256': sf.sha(fb)}, 'edit': {'id': 'E1'}}, None)])
    case('COPY-REASSESSMENT-SCOPE', 'a reassessment naming the copy\'s reference does not name the original\'s: it '
                                    'cannot lift the original finding', lifted(f_orig, 'E1'), lifted(f_orig, 'E1') is False)
    w, c1, fb = landed(r)
    step(w, {COPY: fb}, 'an unreviewed copy')
    step(w, {FP: None, rv: None}, 'delete the original')
    o = outcome(w)
    case('COPY-UNREVIEWED-THEN-DELETE', 'an unreviewed copy, then the original deleted: the original reference still '
                                        'blocks; witness c1', o, blocked(o, False, None))
    # the record and its review never in one tree
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    b = pfc.jb(doc)
    c1 = step(w, {FP: b}, 'the record lands without a review')
    step(w, {FP: None}, 'the record is deleted')
    step(w, {rv: w.review(FP, b)}, 'an accepting review naming its exact reference lands')
    o = outcome(w)
    case('SET-PAIRING', 'a record and an accepting review of its exact reference that never share a tree: R* holds both, '
                        'so the finding is detected and blocks (R6.OBL29.2 over R* as a set)', o, blocked(o, False, c1))
    w = pfc.World(r)
    step(w, {FP: b}, 'the record lands without a review')
    step(w, {FP: None}, 'the record is deleted')
    step(w, {'verification/audits/elsewhere/r.json': w.review(FP, b)}, 'a review outside the record\'s directory')
    o = outcome(w)
    case('SET-PAIRING-LOCATION', 'the same, the review outside the record\'s directory: still a finding, since a '
                                 'first-kind finding counts whatever its review says (r13 Form of a finding (i))', o,
         blocked(o, False, None))


def monotone_controls(r):
    """Detection is monotone in history (R6.OBL29.2, sec. 2.3): evidence that lands later never removes a finding."""
    def superseding_world():
        w = pfc.World(r)
        doc = pfc.invalidating(w, sf.DOC)
        P = w.record(record_id=doc['record_id'])
        pb = pfc.jb(P)
        PP = pfc.RD + 'predecessor.json'
        pfc.land(w, [(PP, P)], 'the predecessor P')
        doc['supersedes'] = {'path': PP, 'blob_sha256': sf.sha(pb)}
        c1 = pfc.land(w, [(FP, doc)], 'f supersedes P')
        return w, c1, P, PP, pb, doc
    w, c1, P, PP, pb, doc = superseding_world()
    o0 = outcome(w)
    S = dict(P, assessment_note='a competing successor')
    S['supersedes'] = {'path': PP, 'blob_sha256': sf.sha(pb)}
    pfc.land(w, [(pfc.RD2 + 'competing.json', S)], 'a competing successor of P lands later')
    o = outcome(w)
    case('COMPETING-SUCCESSOR-LATER', 'f supersedes a reviewed P and blocks; a competing successor of P lands later: f '
                                      'still blocks (a later fork never removes a finding)', {'before': o0, 'after': o},
         blocked(o0, True, None) and blocked(o, True, None))
    w, c1, P, PP, pb, doc = superseding_world()
    o0 = outcome(w)
    ids = rec.item_ids(P)
    adverse = pfc.jb(review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-z',
                      'reviewed': {'path': PP, 'blob_sha256': sf.sha(pb)}, 'method': 'read',
                      'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'}
                                   for k, i in enumerate(ids)]}))
    step(w, {pfc.RD + 'predecessor.second-review.json': adverse}, 'an adverse review of P lands later')
    o = outcome(w)
    case('ADVERSE-PREDECESSOR-REVIEW-LATER', 'f supersedes a reviewed P and blocks; a rejecting review of P lands '
                                             'later: f still blocks', {'before': o0, 'after': o},
         blocked(o0, True, None) and blocked(o, True, None))
    # the first review fails lint, a later one passes; record and reviews never share a tree
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    b = pfc.jb(doc)
    c1 = step(w, {FP: b}, 'the record lands without a review')
    step(w, {FP: None}, 'the record is deleted')
    step(w, {pfc.RD + 'a-self.review.json': w.review(FP, b, reviewer=sf.WRITER),
             pfc.RD + 'b-good.review.json': w.review(FP, b)}, 'two reviews: the first by the author')
    o = outcome(w)
    case('SET-PAIRING-LATER-REVIEW', 'two reviews of the exact reference, never with the record: the first (by the '
                                     'author) fails lint, the later one passes; the finding is detected', o,
         blocked(o, False, c1))


def pairing_predecessor_controls(r):
    """Half (b) of the monotone detection with a predecessor: each hop accepted on positive evidence found anywhere
    in R*; no history-wide ambiguity scan or other review is read."""
    def world(competing=False):
        w = pfc.World(r)
        doc = pfc.invalidating(w, sf.DOC)
        P = w.record(record_id=doc['record_id'])
        pb = pfc.jb(P)
        PP = pfc.RD + 'predecessor.json'
        pfc.land(w, [(PP, P)], 'P lands reviewed')
        doc['supersedes'] = {'path': PP, 'blob_sha256': sf.sha(pb)}
        b = pfc.jb(doc)
        c1 = step(w, {FP: b}, 'f supersedes P, lands unreviewed')
        step(w, {FP: None}, 'f is deleted')
        step(w, {FP[:-5] + '.review.json': w.review(FP, b)}, "f's accepting review lands")
        if competing:
            S = dict(P, assessment='a competing successor of P')
            S['supersedes'] = {'path': PP, 'blob_sha256': sf.sha(pb)}
            pfc.land(w, [(pfc.RD2 + 'competing.json', S)], 'a competing successor of P lands later')
        return w, c1
    w, c1 = world()
    o = outcome(w)
    case('SET-PAIRING-PREDECESSOR', 'P lands reviewed; f supersedes P, lands unreviewed and is deleted; then f\'s '
                                    'accepting review lands: f is detected (half (b), P accepted on its own review) and '
                                    'blocks', o, blocked(o, False, c1))
    w, c1 = world(competing=True)
    o = outcome(w)
    case('SET-PAIRING-NO-HISTORY-SCAN', 'the same with a competing successor of P landing later: f still blocks '
                                        '(detection reads one file and the record it names, Form (i))', o,
         blocked(o, False, c1))
def pairing_review_order_control(r):
    """Half (b): the predecessor P has an adverse review that sorts first and a later accepting review in the same
    directory; the hop tries each review alone, so P is accepted on the accepting one and f is detected."""
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    P = w.record(record_id=doc['record_id'])
    pb = pfc.jb(P)
    PP = pfc.RD + 'predecessor.json'
    ids = rec.item_ids(P)
    adverse = pfc.jb(review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-z',
                      'reviewed': {'path': PP, 'blob_sha256': sf.sha(pb)}, 'method': 'read',
                      'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'}
                                   for k, i in enumerate(ids)]}))
    step(w, {PP: pb, pfc.RD + 'a-adverse.review.json': adverse,
             pfc.RD + 'b-accept.review.json': w.review(PP, pb)}, 'P with an adverse and an accepting review')
    doc['supersedes'] = {'path': PP, 'blob_sha256': sf.sha(pb)}
    b = pfc.jb(doc)
    c1 = step(w, {FP: b}, 'f supersedes P, lands unreviewed')
    step(w, {FP: None}, 'f is deleted')
    step(w, {FP[:-5] + '.review.json': w.review(FP, b)}, "f's accepting review lands")
    o = outcome(w)
    case('SET-PAIRING-PREDECESSOR-REVIEW-ORDER', 'P\'s adverse review sorts before its accepting review in the same '
                                                 'directory: P is accepted on the accepting review alone and f is '
                                                 'detected and blocks', o, blocked(o, False, c1))


def predecessor_widening_unit(r):
    """R6.OBL29.3 predecessor reviews, the widening review where the lineage requires one (review finding 9): a
    rejecting widening review of the exact predecessor in R*, since removed from the tree, keeps the discharge
    inapplicable. Unit level: reassessments require no widening, so the lineage's widening is supplied."""
    pred = {'schema': 'oi-reassessment/1', 'record_id': 'ra', 'author': sf.WRITER, 'supersedes': None, 'x': 1}
    pb = pfc.jb(pred)
    pref = {'path': 'syn/cfg/ra-p.json', 'blob_sha256': sf.sha(pb)}
    doc = dict(pred, x=2, supersedes=pref)
    st = rec.Store([(pref['path'], pb)])
    st.widening = lambda old, new: ['ra:widened'] if new is not None and new.get('x') == 1 else []

    class Cum:
        def __init__(self, verdict):
            self.verdict = verdict

        def reviews_naming(self, ref, directory=None):
            if ref == pref:
                return [('verification/audits/gone/ra-p.widening.json',
                         review_record({'schema': rec.review_schema, 'kind': 'widening', 'reviewer': 'session.fixture-widener-z', 'reviewed': ref,
                          'method': 'read', 'verdicts': [{'item': 'ra:widened', 'verdict': self.verdict}]}))]
            return []

    def problems(verdict):
        return c3.predecessor_review_problems(doc, {'path': 'syn/cfg/ra.json', 'blob_sha256': '0' * 64}, st,
                                              Cum(verdict))
    rej, acc = problems('reject'), problems('accept')

    class CumDup(Cum):
        def reviews_naming(self, ref, directory=None):
            got = Cum.reviews_naming(self, ref, directory)
            for _p, d in got:
                d['verdicts'] = d['verdicts'] * 2
            return got
    dup = c3.predecessor_review_problems(doc, {'path': 'syn/cfg/ra.json', 'blob_sha256': '0' * 64}, st,
                                         CumDup('accept'))
    case('PREDECESSOR-WIDENING-ITEMS', 'the predecessor\'s widening review lists its item twice: refused (item coverage '
                                       'as widening_review_problems)', dup,
         any('more than one verdict' in x for x in dup))
    case('PREDECESSOR-WIDENING-REJECT-DELETED', 'the operative predecessor\'s widening review in R* rejects (and has left '
                                                'the tree): the discharge is inapplicable; an accepting one: no problem',
         {'reject': rej, 'accept': acc}, bool(rej) and acc == [])


def r13_form_controls(r):
    """Amendment 6 r13 Form of a finding (i)-(iv) and R6.RECON.35 classes, as R6.OBL29.2 applies them to R*."""
    from ledger_coverage.engine import findings as fdm
    rv = FP[:-5] + '.review.json'
    # R6.RECON.35 classes on bytes
    cls = {
        'strict recon': fdm.classify(b'{"schema": "oi-reconciliation/2"}'),
        'duplicate key': fdm.classify(b'{"schema": "oi-review-record/1", "schema": "oi-review-record/1"}'),
        'NaN': fdm.classify(b'{"schema": "oi-reconciliation/2", "x": NaN}'),
        'utf-16 BOM': fdm.classify('{"schema": "oi-review-record/1"}'.encode('utf-16')),
        'nested schema': fdm.classify(b'{"a": [{"schema": " OI-Reconciliation/9 "}]}'),
        'review shape': fdm.classify(b'{"reviewed": {}, "verdicts": [{"invalidated": []}]}'),
        'unparseable': fdm.classify(b'{"schema": "oi-reconciliation/2", invalidates'),
        'escaped': fdm.classify(b'{"x": "oi-reconcili\\u0061tion/2" ,,'),
        'prose': fdm.classify(b'# oi-reconciliation/2 quoted in prose'),
        'other json': fdm.classify(b'{"schema": "oi-term-rules/2"}'),
    }
    want = {'strict recon': ('a', 'oi-reconciliation/2'), 'duplicate key': ('b', False), 'NaN': ('b', False),
            'utf-16 BOM': ('b', False), 'nested schema': ('b', False), 'review shape': ('b', True),
            'unparseable': ('c', True), 'escaped': ('c', False), 'prose': None, 'other json': None}
    case('SCAN-CLASSES', 'R6.RECON.35 selection and classes (a), (b), (c) and the invalidation signal on fixed bytes',
         {k: list(v) if v else v for k, v in cls.items()}, cls == want)

    def second_kind_world(reviewer='session.fixture-reviewer-x', withdraw=False, reviewed_missing=False,
                          independence=None):
        w = pfc.World(r)
        q = w.record(record_id='syn-recon-q')
        qb = pfc.jb(q)
        QP = pfc.RD + 'q.json'
        pfc.land(w, [(QP, q)], 'a reviewed no-effect record q')
        inv = pfc.invalidating(w, sf.DOC)['paths'][0]['scientific_effect']
        ref = {'path': QP if not reviewed_missing else pfc.RD + 'absent.json', 'blob_sha256': sf.sha(qb)}
        verdicts = [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(q)]
        for v in verdicts:
            if v['item'] == sf.DOC + ':scientific_effect':
                v.update(verdict='invalidates', reason='the change invalidates the planned edit',
                         invalidated=inv['invalidated'], configuration=inv['configuration'])
        zd = review_record({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': ref,
                    'method': 'read ' + 'a' * 40, 'verdicts': verdicts})
        if independence == 'absent':
            zd.pop('independence')
        elif independence is not None:
            zd['independence'] = independence
        z = pfc.jb(zd)
        ZP = pfc.RD + 'q.second.review.json'
        c1 = step(w, {ZP: z}, 'an independent review finds invalidation')
        if withdraw:
            step(w, {ZP: None}, 'the review is withdrawn')
        return w, c1, ZP
    w, c1, ZP = second_kind_world()
    o = outcome(w)
    sk = [f for f in o['all'] if f.get('kind') == 2]
    case('SECOND-KIND', 'an independent reviewer\'s invalidates verdict on <path>:scientific_effect of a no-effect '
                        'record: a second-kind finding that blocks', o,
         'retirement-blocked' in o['classes'] and sk and sk[0]['record']['path'] == ZP)
    # staging S-2 sec. 7 S2-NO-RETRO-LAPSE (P3): later records cannot lapse a genuine finding
    later = {}
    from ledger_coverage import record_authority as ra_
    for name in ('a later review declaring a dependency on the author', 'a later record naming the reviewer as author'):
        w, c1, ZP = second_kind_world()
        q = w.record(record_id='syn-recon-q')
        qref = {'path': pfc.RD + 'q.json', 'blob_sha256': sf.sha(pfc.jb(q))}
        lp = pfc.RD + ('q.later.review.json' if name.startswith('a later review') else 'other.json')
        if name.startswith('a later review'):
            step(w, {lp: pfc.jb(review_record(
                {'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-x', 'reviewed': qref,
                 'method': 'read', 'verdicts': [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(q)],
                 'independence': {'not_author': True, 'depends_on': [sf.WRITER]}}))}, name)
        else:
            step(w, {lp: pfc.jb(w.record(record_id='syn-recon-other',
                                                            author='session.fixture-reviewer-x'))}, name)
        o = outcome(w)
        sk = [f for f in o['all'] if f.get('kind') == 2]
        # the later file is in the scanned set R* of the run's M, so the detection read it
        scanned = lp in {p_ for p_, _o in c3.Cumulative(w.repo, [w.M], ('oi-reconciliation/1', 'oi-reconciliation/2'),
                                                         ra_.reconciliation_root).entries()}
        later[name] = scanned and bool(sk) and sk[0]['record']['path'] == ZP and 'retirement-blocked' in o['classes']
    case('S2-NO-RETRO-LAPSE', 'a genuine second-kind finding; later a review by its reviewer declaring a dependency on '
                              'the author, or a record at another path naming the reviewer as author, each in the '
                              'scanned set: the finding keeps binding', later, all(later.values()))
    w, c1, ZP = second_kind_world(withdraw=True)
    o = outcome(w)
    sk = [f for f in o['all'] if f.get('kind') == 2]
    case('N-INDEP-WITHDRAWN', 'the independent review deleted after landing: the second-kind finding still blocks', o,
         'retirement-blocked' in o['classes'] and sk and sk[0]['present_at_M'] is False and sk[0]['witness'] == c1)
    w, c1, ZP = second_kind_world(reviewer=sf.WRITER, withdraw=True)
    o = outcome(w)
    case('SECOND-KIND-SELF-REVIEW', 'the same verdict by the reviewed record\'s own author (independence fails): no '
                                    'finding', o, not [f for f in o['all'] if f.get('kind') == 2]
         and 'retirement-blocked' not in o['classes'])
    # staging S-2 sec. 7 S2-INVALIDATING-RESPELL: the same identity as the author (S2.2) without byte equality does not
    # lapse the review (S2.5): a genuine finding with a form failure
    respelled = sf.WRITER.upper().replace('.', '_')
    w, c1, ZP = second_kind_world(reviewer=respelled, withdraw=True)
    o = outcome(w)
    sk = [f for f in o['all'] if f.get('kind') == 2]
    case('S2-INVALIDATING-RESPELL', 'the same verdict by %s, the author respelled: not disqualified, a genuine finding '
         'with a form failure' % respelled, o,
         bool(sk) and 'record-invalid' in o['classes'] and 'retirement-blocked' in o['classes'])
    # staging S-2 sec. 7 S2-INVALIDATING-DECLARED and the S2-INVALIDATING-MALFORMED variant: a declaration naming the
    # author, or none at all, by a reviewer of another identity: a genuine finding with a form failure that blocks
    for cid, ind, what in (('S2-INVALIDATING-DECLARED', {'not_author': True, 'depends_on': [sf.WRITER]},
                            'depends_on naming the author'),
                           ('S2-INVALIDATING-MALFORMED/independence-missing', 'absent', 'no independence declaration')):
        w, c1, ZP = second_kind_world(independence=ind, withdraw=True)
        o = outcome(w)
        sk = [f for f in o['all'] if f.get('kind') == 2]
        case(cid, 'the same verdict by another identity with %s: a genuine finding with a form failure' % what, o,
             bool(sk) and 'record-invalid' in o['classes'] and 'retirement-blocked' in o['classes'])
    w, c1, ZP = second_kind_world(reviewer='https://example.invalid/runs/1')
    o = outcome(w)
    sk = [f for f in o['all'] if f.get('kind') == 2]
    case('SECOND-KIND-RUN-REVIEWER', 'the same verdict by a run (a URL in reviewer): not an identity string, so a '
         'genuine finding with a form failure that still blocks (staging S-2 S2.5)', o,
         bool(sk) and 'record-invalid' in o['classes'] and 'retirement-blocked' in o['classes'])
    w, c1, ZP = second_kind_world(reviewed_missing=True)
    o = outcome(w)
    case('SECOND-KIND-REVIEWED-MISSING', 'an invalidates verdict whose reviewed names no record the scan finds: it '
                                         'counts (form failure) and has no readable entry: run-level FAIL '
                                         'retirement-blocked and FAIL record-invalid, with its provenance', o,
         runlevel_fail(o, ZP))
    # first kind with no review at all
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    step(w, {FP: pfc.jb(doc)}, 'an invalidating entry with no review')
    o = outcome(w)
    case('FIRST-KIND-UNREVIEWED', 'an invalidating entry whose record has no review: a finding that blocks (detection '
                                  'precedes lint)', o, blocked(o, True, w.M))
    # malformed files
    MP = pfc.RD + 'broken.json'
    w = pfc.World(r)
    step(w, {MP: b'{"schema": "oi-reconciliation/2", "record_id": "x", "record_id": "y"}'}, 'a malformed record')
    o = outcome(w)
    case('MALFORMED-NONFINDING-AT-M', 'a class (b) file without an invalidation signal at M: FAIL record-invalid (the '
                                      'ordinary malformed-nonfinding lint), no finding', o,
         'record-invalid' in o['classes'] and any('malformed record' in d for d in o['invalid']) and not o['finding'])
    step(w, {MP: None}, 'deleted')
    o = outcome(w)
    case('P-HISTORICAL-MALFORMED-NONFINDING', 'the same file deleted: history alone gives neither a finding nor a '
                                              'diagnostic', o, not o['finding'] and
         not any('malformed record' in d for d in o['invalid']))
    w = pfc.World(r)
    step(w, {MP: b'{"schema": "oi-reconciliation/2", "x": "invalidates"'}, 'an unparseable malformed finding')
    step(w, {MP: None}, 'deleted')
    o = outcome(w)
    case('N-MALFORMED-DELETED', 'a class (c) malformed finding landed and deleted: still in R*; run-level FAIL '
                                'retirement-blocked and FAIL record-invalid (it binds), with its path, blob, witness '
                                'and class in the result, the entry-less reason stated', o,
         runlevel_fail(o, MP, 'c') and any('no readable entry' in d and 'blocks at run level' in d
                                           for d in o['invalid']))
    TLP = 'verification/audits/syn-tl/'
    w = pfc.World(r, variant=tl_variant(TLP))
    step(w, {TLP + 'broken.json': b'{"schema": "oi-review-record/1", "a": 1, "a": 2}'}, 'malformed under a TL prefix')
    o = outcome(w)
    case('P-TL-MALFORMED-NONFINDING', 'a malformed non-finding under a tool-landing prefix at M, not read by the run: '
                                      'no malformed-record FAIL (the existing selector)', o,
         not any('malformed record' in d for d in o['invalid']))
    # form failures and binding
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    del doc['paths'][0]['scientific_effect']['configuration']
    c1 = pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('FORM-III-CURRENT', 'a finding at M without configuration: FAIL record-invalid (form failure) and still '
                             'blocks (global scope)', o, blocked(o, True, w.M) and
         any('configuration is absent' in d for d in o['invalid']))
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    doc['paths'][0]['scientific_effect']['invalidated'][0]['sha256'] = '0' * 64
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('FORM-II-MISMATCH', 'an invalidated element whose sha256 differs from the named configuration\'s ledger: FAIL '
                             'record-invalid and still blocks', o, blocked(o, True, w.M) and
         any('differs from the named configuration' in d for d in o['invalid']))
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    se = doc['paths'][0]['scientific_effect']
    se.pop('invalidated')
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('FALLBACK-CONCLUSIONS', 'invalidates without invalidated, conclusions naming E1: bound through the Form (iv) '
                                 'fallback (E1), with a form failure', o, blocked(o, True, w.M) and
         'record-invalid' in o['classes'])
    w = pfc.World(r)
    other = 'doc/other.md'
    w.M = w.repo.derive(w.M, {other: b'# other\n\nchanged on main\n'}, parents=[w.M], subject='corpus change')
    doc = pfc.invalidating(w, other)
    se = doc['paths'][0]['scientific_effect']
    se.pop('invalidated')
    se['conclusions'] = 'none'
    pfc.land(w, [(FP, doc)])
    code, out = w.run([], harness=True)
    rl = [b for b in ((out or {}).get('category3') or {}).get('blocked') or [] if b.get('edit') is None]
    case('RUN-LEVEL', 'invalidates with no invalidated, conclusions none, on a path the ledger does not list: bound at '
                      'run level for the configuration of its lineage', {'exit': code, 'run_level': rl},
         code == 20 and bool(rl))
    w0 = pfc.World(r)
    d0 = pfc.invalidating(w0, sf.DOC)
    # a form failure (an empty assessment) under the original plan's configuration, resolvable on main; the revised
    # plan carries no edit it binds (an absent configuration would bind every configuration, r13 Amendment 7)
    d0['paths'][0]['scientific_effect']['assessment'] = ''
    w = pfc.World(r, edits=pfc.EDITS_OTHER, first_id=2)
    land_original_plan(w, r)
    pfc.land(w, [(FP, d0)])
    step(w, {FP: None, rv: None}, 'deleted')
    o = outcome(w)
    case('FORM-FAILURE-HISTORICAL-UNBOUND', 'a historical-only finding with a form failure that binds nothing the run\'s '
                                            'configuration carries: no FAIL from its form (R6.OBL29.2)', o,
         'retirement-blocked' not in o['classes'] and not any('form failure of a category-3' in d for d in o['invalid']))
    # Keys
    def keys_world(**upd):
        w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
        return pfc.finding_world(r, variant=pfc.cite(pfc.reassessment(w1, **upd)), edits=pfc.EDITS_REWORDED)
    o = outcome(keys_world(repair=None))
    case('N-KEYS-A-BYPASS', 'repair null for a first-kind finding with no rejecting review of its scientific effect: '
                            'refused (Keys (a))', o, refused_for(o, 'repair is null where an independent reviewer'))
    o = outcome(keys_world(edit=None))
    case('KEYS-EDIT-NULL', 'edit null for a finding not bound at run level: refused (Keys)', o,
         refused_for(o, 'edit is null for a finding not bound at run level'))
    w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
    o = outcome(keys_world(finding=w1.findings[0]))
    case('KEYS-ITEM-MISSING', 'a reassessment finding without item: a form failure of its keys', o,
         refused_for(o, '$.finding.item: missing'))


def read_domain_controls(r):
    """OBL-29 r9 sec. 5.3: the category-3 read domain is recorded and checked independently (adapters/read_domain)."""
    from ledger_coverage.adapters import read_domain as rdm
    w, c1, fb = landed(r)
    step(w, {FP: None}, 'delete f')
    code, out = w.run([], harness=True)
    out = out or {}
    good = rdm.problems(w.repo, out, [w.M], [w.c])
    rd = out.get('category3_read_domain') or {}
    import copy
    forged = copy.deepcopy(out)
    unrelated = w.repo.derive(pfc.World(r).syn.H, {pfc.RD + 'x.json': fb}, parents=[], subject='unrelated root')
    forged['category3_read_domain']['reads'].append({'commit': unrelated, 'path': pfc.RD + 'x.json',
                                                    'blob_sha256': sf.sha(fb)})
    outside = copy.deepcopy(out)
    outside['category3_read_domain']['reads'].append({'commit': c1, 'path': 'doc/s.md',
                                                     'blob_sha256': sf.sha(w.repo.read(c1, 'doc/s.md'))})
    wrong = copy.deepcopy(out)
    wrong['category3_read_domain']['reads'][0]['blob_sha256'] = '0' * 64
    exp = rd.get('explicit') or []
    badsrc = copy.deepcopy(out)
    if badsrc['category3_read_domain']['explicit']:
        badsrc['category3_read_domain']['explicit'][0]['source'] = w.M
    badpre = copy.deepcopy(out)
    badpre['category3_read_domain']['prefix'] = ''
    case('READ-DOMAIN-EXPLICIT', 'explicitly read records come from the configuration commit with their blob; a '
                                 'substituted source, or a recorded prefix other than verification/audits/, is '
                                 'refused', {'explicit': len(exp), 'badsrc': rdm.problems(w.repo, badsrc, [w.M], [w.c]),
                                             'badpre': rdm.problems(w.repo, badpre, [w.M], [w.c])},
         bool(exp) and bool(rdm.problems(w.repo, badsrc, [w.M], [w.c])) and
         bool(rdm.problems(w.repo, badpre, [w.M], [w.c])))
    case('P-REPRESENTATIVE-READ-DOMAINS', 'the category-3 reads recorded with their source commit, path and blob all '
                                          'come from the named root or its verified history under the prefix; a read '
                                          'from an unrelated commit, outside the prefix, or with another blob is '
                                          'refused', {'good': good, 'reads': len(rd.get('reads') or []),
                                                      'forged': rdm.problems(w.repo, forged, [w.M], [w.c]),
                                                      'outside': rdm.problems(w.repo, outside, [w.M], [w.c]),
                                                      'wrong': rdm.problems(w.repo, wrong, [w.M], [w.c])},
         good == [] and bool(rd.get('reads')) and rdm.problems(w.repo, forged, [w.M], [w.c]) and
         rdm.problems(w.repo, outside, [w.M], [w.c]) and rdm.problems(w.repo, wrong, [w.M], [w.c]))


def milestone_controls(r):
    """Review findings on 4ba24dd3: the unreadable-invalidated fallback, the R6.RECON.30 beside-table stop, the global
    id scope, the historical form-failure FAIL and the self-review boundary."""
    rv = FP[:-5] + '.review.json'
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    doc['paths'][0]['scientific_effect']['invalidated'] = [{'note': 'no readable element'}]
    c1 = pfc.land(w, [(FP, doc)])
    step(w, {FP: None, rv: None}, 'delete f')
    o = outcome(w)
    case('UNREADABLE-INVALIDATED-FALLBACK', 'invalidated with no readable {id, sha256, target} element, landed then '
                                            'deleted: bound through the Form (iv) fallback (conclusions E1) and still '
                                            'blocks', o, blocked(o, False, c1))
    # beside the tables: end_M disagrees
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    sp = doc['paths'][0]['splices']
    if sp:
        sp[0]['end_M'] = sp[0]['end_M'] + 1
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('BESIDE-TABLES-STOP', 'a finding record whose splice end_M is not start_M + end_H - start_H (an R6.RECON.30 '
                               'check beside the tables): a malformed finding, run-level FAIL retirement-blocked and '
                               'FAIL record-invalid naming the beside-table failure', {'o': o, 'had_splice': bool(sp)},
         bool(sp) and runlevel_fail(o, FP) and any('beside its tables' in d for d in o['invalid']))
    # global id scope: an unresolved configuration binds a same-id edit on another path, outside the lineage
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    se = doc['paths'][0]['scientific_effect']
    se['configuration'] = {'path': 'syn/none/config.json', 'blob_sha256': '0' * 64}
    se['invalidated'][0]['target'] = {'path': 'doc/other.md', 'start_H': 0, 'old_sha256': '1' * 64}
    pfc.land(w, [(FP, doc)])
    code, out = w.run([], harness=True)
    edits = [b.get('edit') for b in ((out or {}).get('category3') or {}).get('blocked') or []]
    case('GLOBAL-ID-SCOPE-UNRESOLVED', 'a finding whose configuration does not resolve, its element naming E1 on another '
                                       'path: the id match is global (Form (iii)), so the run\'s E1 on doc/s.md is bound',
         {'exit': code, 'edits': edits}, code == 20 and 'E1' in edits)
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    se = doc['paths'][0]['scientific_effect']
    se['invalidated'][0]['target'] = {'path': 'doc/other.md', 'start_H': 0, 'old_sha256': '1' * 64}
    pfc.land(w, [(FP, doc)])
    code, out = w.run([], harness=True)
    edits = [b.get('edit') for b in ((out or {}).get('category3') or {}).get('blocked') or []]
    inv = [d for i in (out or {}).get('items', []) if i['class'] == 'record-invalid' for d in (i.get('detail') or [])]
    case('GLOBAL-ID-SCOPE-MISMATCH', 'an element whose target differs from the named configuration\'s ledger: a Form (ii) '
                                     'failure, FAIL record-invalid, and E1 bound', {'exit': code, 'edits': edits},
         code == 20 and 'E1' in edits and any('differs from the named configuration' in d for d in inv))
    # historical form failure while it binds
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    del doc['paths'][0]['scientific_effect']['configuration']
    c1 = pfc.land(w, [(FP, doc)])
    step(w, {FP: None, rv: None}, 'delete f')
    o = outcome(w)
    case('FORM-FAILURE-HISTORICAL-BOUND', 'a historical-only finding with a form failure that binds the run\'s E1: '
                                          'FAIL record-invalid for its form and retirement-blocked (R6.OBL29.2)', o,
         blocked(o, False, c1) and any('form failure of a category-3' in d for d in o['invalid']))
    # the self-review boundary: the invalidating review lands first with its record absent, then the record lands and
    # shows reviewer = author. Owner-confirmed reading (#1169 comment 7207734407, decision 4): the finding is
    # disqualified once the record is found.
    w = pfc.World(r)
    q = w.record(record_id='syn-recon-q')
    qb = pfc.jb(q)
    QP = pfc.RD + 'q.json'
    inv = pfc.invalidating(w, sf.DOC)['paths'][0]['scientific_effect']
    verdicts = [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(q)]
    for v in verdicts:
        if v['item'] == sf.DOC + ':scientific_effect':
            v.update(verdict='invalidates', reason='x', invalidated=inv['invalidated'],
                     configuration=inv['configuration'])
    z = pfc.jb(review_record({'schema': rec.review_schema, 'reviewer': sf.WRITER, 'reviewed': {'path': QP, 'blob_sha256': sf.sha(qb)},
                'method': 'read ' + 'a' * 40, 'verdicts': verdicts}))
    step(w, {pfc.RD + 'q.second.review.json': z}, 'the invalidating review lands first')
    o1 = outcome(w)
    step(w, {QP: qb}, 'the reviewed record lands, its author the reviewer')
    o2 = outcome(w)
    case('SELF-REVIEW-RECORD-LANDS-LATER', 'owner-confirmed reading: before the record lands the review names no '
                                           'record the scan finds (no readable entry: run-level FAIL '
                                           'retirement-blocked); once it lands, reviewer = author disqualifies the '
                                           'review and no second-kind finding remains',
         {'before': [o1['exit'], o1['stop'], o1['runlevel']],
          'after_kind2': [f for f in o2['all'] if f.get('kind') == 2]},
         runlevel_fail(o1, pfc.RD + 'q.second.review.json') and not [f for f in o2['all'] if f.get('kind') == 2])


def nits_0cafbdc0_controls(r):
    """Review nits on 0cafbdc0: a resolved configuration outside the lineage where the global id scope decides; an
    identity translation without prefix agreement; an explicit record at a source the caller did not supply; elements
    with an id but a missing key binding through the fallback of (iii)."""
    import copy
    from ledger_coverage.adapters import read_domain as rdm

    def other_cfg_world():
        w = pfc.World(r)
        pd = w.files['syn/patch.json']
        oc_, op_, os_, ofiles = w.syn.build({'patch_sha': sf.sha(pd), 'files': {'syn/patch.json': pd},
                                             'config_path': 'syn/other/config.json',
                                             'extra': {'retirement': {'name': 'other', 'issue': 'other'},
                                                       'config_id': 'other-retirement-config'}})
        step(w, {q: b for q, b in ofiles.items() if isinstance(b, bytes)}, 'another retirement\'s configuration on main')
        return w, {'path': op_, 'blob_sha256': os_}

    def run_case(mutate, path=sf.DOC):
        w, oref = other_cfg_world()
        if path != sf.DOC:
            step(w, {path: b'# other\n\nchanged on main\n'}, 'a corpus change')
        doc = pfc.invalidating(w, path)
        se = doc['paths'][0]['scientific_effect']
        se['configuration'] = oref
        mutate(se)
        pfc.land(w, [(FP, doc)])
        code, out = w.run([], harness=True)
        out = out or {}
        edits = [b_.get('edit') for b_ in (out.get('category3') or {}).get('blocked') or []]
        inv = [d for i in out.get('items', []) if i['class'] == 'record-invalid' for d in (i.get('detail') or [])]
        return {'exit': code, 'stop': (out.get('stop') or {}).get('class'), 'edits': edits, 'invalid': inv[:4]}

    def element_missing_target(se):
        # an element with id and sha256 but no target; conclusions none on a path without edits, so that only the
        # element's id can bind, through the global id scope of (iii)
        del se['invalidated'][0]['target']
        se['conclusions'] = 'none'

    def element_mismatch(se):
        se['invalidated'][0]['target'] = dict(se['invalidated'][0]['target'], path='doc/other.md')
    got = run_case(element_missing_target, path='doc/other.md')
    case('GLOBAL-ID-SCOPE-OUTSIDE-LINEAGE-ELEMENT', 'a resolved configuration of another retirement (outside the '
                                                    'lineage); the only element has an id but no target: it binds '
                                                    'through the fallback of (iii) with the id match global, so E1 is '
                                                    'bound', got, got['exit'] == 20 and 'E1' in got['edits'])
    got = run_case(element_mismatch)
    case('GLOBAL-ID-SCOPE-OUTSIDE-LINEAGE-MISMATCH', 'the same resolved configuration outside the lineage; the element\'s '
                                                     'target names another path, a Form (ii) mismatch: the id match is '
                                                     'global and E1 is bound', got,
         got['exit'] == 20 and 'E1' in got['edits'] and
         any('differs from the named configuration' in d for d in got['invalid']))
    # an unreadable element beside a readable one, the configuration resolved and outside the lineage: the
    # unreadable element makes the id match global (Form (ii), "blocks through the fallback of (iii)"), and that alone
    # binds the run's E1. The named configuration's ledger has E1 (another edit than the run's) and E2; the readable
    # element names E2 correctly, the unreadable one carries only the id E1
    w = pfc.World(r)
    two = pfc.EDITS_REWORDED + pfc.EDITS_OTHER
    pd2 = sf.patch_doc(w.syn.H, two, 1)
    oc2, op2, os2, of2 = w.syn.build({'patch_sha': sf.sha(pd2), 'files': {'syn/patch.json': pd2},
                                      'config_path': 'syn/other2/config.json',
                                      'extra': {'retirement': {'name': 'other2', 'issue': 'other2'},
                                                'config_id': 'other2-retirement-config'}})
    step(w, {q: b for q, b in of2.items() if isinstance(b, bytes)}, 'another retirement\'s configuration (E2)')
    w2 = pfc.World(r, edits=two, first_id=1)
    sp2 = [x for x in w2.led['splices'] if x['id'] == 'E2'][0]
    readable = {'id': 'E2', 'sha256': pfc.rcmod.edit_key(w2.led, 'E2'),
                'target': {'path': sp2['file'], 'start_H': sp2['start'], 'old_sha256': sp2['old_sha256']}}
    # the record's splice table drafted from the named configuration's ledger, as R6.RECON.30 requires beside it
    eff = dict(pfc.CONTROL_EFFECT, conclusions='none', verdict='invalidates', invalidated=[{'id': 'E1'}, readable],
               configuration={'path': op2, 'blob_sha256': os2},
               assessment='control fixture: an unreadable element beside a readable one')
    doc = pfc.rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, w2.led, sf.DOC, scientific_effect=eff)
    doc.update(record_id='syn-finding-beside', author=sf.WRITER, supersedes=None, M=w.M, X=w.X)
    se = doc['paths'][0]['scientific_effect']
    se['conclusions'] = 'none'
    pfc.land(w, [(FP, doc)])
    code, out = w.run([], harness=True)
    out = out or {}
    edits = [b_.get('edit') for b_ in (out.get('category3') or {}).get('blocked') or []]
    inv = [d for i in out.get('items', []) if i['class'] == 'record-invalid' for d in (i.get('detail') or [])]
    stop = out.get('stop')
    case('GLOBAL-ID-SCOPE-UNREADABLE-BESIDE-READABLE', 'an element with only an id beside a readable element, the '
                                                       'configuration resolved outside the lineage: the id match is '
                                                       'global and the run\'s E1 is bound (removing that global scope '
                                                       'fails this control)', {'exit': code, 'edits': edits,
                                                                               'invalid': inv[:3], 'stop': stop},
         code == 20 and 'E1' in edits and not any('configuration is absent' in d for d in inv) and
         not any('differs from the named configuration' in d for d in inv))
    # an identity translation whose H and M prefixes disagree
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    bad_m = w.repo.derive(w.M, {sf.DOC: b'# SYNTHETIC' + w.repo.read(w.M, sf.DOC)[11:]}, parents=[w.M],
                          subject='a tree whose prefix differs')
    doc['M'] = bad_m
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('BESIDE-TABLES-IDENTITY-PREFIX', 'a finding record whose identity translation has H and M bytes that disagree '
                                          'before the splice end: an R6.RECON.30 beside-table failure, a malformed '
                                          'finding: run-level FAIL retirement-blocked and FAIL record-invalid', o,
         runlevel_fail(o, FP) and any('identity without prefix agreement' in d for d in o['invalid']))
    # an explicit record present at a source the caller did not supply
    w, c1, fb = landed(r)
    code, out = w.run([], harness=True)
    out = out or {}
    other = w.repo.derive(w.c, {'notes/x.txt': b'x\n'}, parents=[w.c], subject='another commit holding the record')
    sub = copy.deepcopy(out)
    exp = sub.get('category3_read_domain', {}).get('explicit') or []
    if exp:
        exp[0]['source'] = other
    probs = rdm.problems(w.repo, sub, [w.M], [w.c])
    case('READ-DOMAIN-UNSUPPLIED-SOURCE', 'an explicit record whose recorded source holds its blob but is not a source '
                                          'the caller supplied (the configuration commit or an admitted REV): refused',
         probs, bool(exp) and any('neither the configuration commit' in x for x in probs))


def explicit_review_controls(r):
    """findings_of_records also extracts second-kind findings from review records the run reads explicitly."""
    from ledger_coverage.engine import category3 as c3m, gitobj
    w = pfc.World(r)
    q = w.record(record_id='syn-recon-q')
    qb = pfc.jb(q)
    qref = {'path': pfc.RD + 'q.json', 'blob_sha256': sf.sha(qb)}
    inv = pfc.invalidating(w, sf.DOC)['paths'][0]['scientific_effect']
    verdicts = [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(q)]
    for v in verdicts:
        if v['item'] == sf.DOC + ':scientific_effect':
            v.update(verdict='invalidates', reason='x', invalidated=inv['invalidated'],
                     configuration=inv['configuration'])
    z = review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-x', 'reviewed': qref, 'method': 'read ' + 'a' * 40,
         'verdicts': verdicts, '_ref': {'path': 'syn/cfg/z.review.json', 'blob_sha256': '5' * 64}})
    got = c3m.findings_of_records([z], ('oi-reconciliation/1', 'oi-reconciliation/2'),
                                  lambda ref: q if ref == qref else None)
    case('EXPLICIT-REVIEW-SECOND-KIND', 'a review record the run reads explicitly carries a second-kind finding: it is '
                                        'extracted with its entry', [(f['kind'], f['item']) for f in got],
         [(f['kind'], f['item'], bool(f['entry'])) for f in got] == [(2, sf.DOC + ':scientific_effect', True)])


def tl_variant(prefix, pins=()):
    """The synthetic configuration with a tool-landing class whose prefix is `prefix` (and pins for `pins`)."""
    from ledger_coverage import record_authority as ra

    def variant(w):
        doc = {'schema': 'oi-side-change-classes/1', 'record_id': 'syn-tool-landing', 'author': sf.WRITER,
               'supersedes': None, 'classes': [{'id': ra.tool_landing_class_id, 'prefixes': [prefix],
                                                'reason': 'synthetic tool landing',
                                                'pins': [{'path': q, 'blob_sha256': sf.sha(x)} for q, x in pins]}]}
        b = pfc.jb(doc)
        ref = {'path': 'syn/cfg/classes.json', 'blob_sha256': sf.sha(b)}
        files = {ref['path']: b}
        review = sf.Syn.chain(None, files, ref['path'], sf.REVIEWER)
        return {'files': files, 'add_records': [dict(ref, kind='side-change-classes')] + review,
                'extra': {'roles': {'scientific_base': w.syn.H, 'pin': w.syn.pin, 'side_change_classes': ref}}}
    return variant


def more_negative_controls(r):
    rv = FP[:-5] + '.review.json'
    TL = 'verification/audits/syn-tl/'
    w = pfc.World(r, variant=tl_variant(TL))
    doc = pfc.invalidating(w, sf.DOC)
    fb = pfc.jb(doc)
    c1 = pfc.land(w, [(FP, doc)])
    step(w, {FP: None, rv: None, TL + 'finding.json': fb}, 'move f under a tool-landing prefix, unpinned')
    o = outcome(w)
    case('N-MOVE-TL', 'f moved under a tool-landing prefix, unpinned: still blocked (no tool-landing exclusion in '
                      'detection) and the side change unclassified', o,
         blocked(o, False, c1) and 'side-change-unclassified' in o['classes'])
    w0 = pfc.World(r)
    fb0 = pfc.jb(pfc.invalidating(w0, sf.DOC))
    w = pfc.World(r, variant=tl_variant(pfc.RD, pins=[(FP, fb0)]))
    doc = pfc.invalidating(w0, sf.DOC)
    c1 = pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('N-TL-WIDEN', 'a configuration whose tool-landing class covers f\'s directory and pins f\'s blob: f is still '
                       'detected and blocks (R6.OBL29.5)', {'o': o, 'same_blob': fb0 == pfc.jb(doc)},
         blocked(o, True, w.M) and fb0 == pfc.jb(doc))
    w, c1, fb = landed(r)
    step(w, {FP: ('symlink', fb)}, 'mode 120000 with the same object id')
    o = outcome(w)
    # R6.PUR.12 (SIDE-NONREG), as N-SYMLINK
    case('N-SYMLINK-SAME-BLOB', 'f\'s entry turned into a symbolic link with the same object id: still blocked, '
                                'present_at_M false, witness c1', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    d = json.loads(fb)
    d['paths'][0]['scientific_effect'].pop('invalidated', None)
    step(w, {FP: pfc.jb(d)}, 'remove the key invalidated')
    o = outcome(w)
    case('N-REWRITE-INVALIDATED', 'the key invalidated removed: still blocked (the record-invalid form failure of '
                                  'r13 Form (i) is not implemented by this tool)', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    d = json.loads(fb)
    d['paths'] = [e for e in d['paths'] if e.get('path') != sf.DOC]
    step(w, {FP: pfc.jb(d)}, 'remove the entry')
    o = outcome(w)
    case('N-REWRITE-ENTRY', 'the invalidating entry removed from the record: still blocked', o, blocked(o, False, c1))
    # a record seen only in a REV dropped at merge
    w = pfc.World(r)
    c1 = w.M
    doc = pfc.invalidating(w, sf.DOC)
    rev1, _p, _d = w.standard(w.record(), path=pfc.RD2 + 'doc.json',
                              extra={FP: pfc.jb(doc), rv: w.review(FP, pfc.jb(doc))})
    w.M = w.repo.derive(c1, {'notes/m.txt': b'm\n'}, parents=[c1, rev1], subject='merge dropping the REV records')
    rev2, p2, _d = w.standard(w.record(record_id='syn-recon-2'), path=pfc.RD2 + 'doc2.json')
    o = outcome(w, classify=['%s:%s' % (rev2, p2)])
    case('N-REV-DROP', 'a finding added by an earlier REV whose merge into main dropped it, a later run naming another '
                       'REV: still blocked through the merge\'s ancestry; witness the earlier REV', o,
         blocked(o, False, rev1))
    # the REV root: a finding only in the named REV's tree
    w = pfc.World(r)
    doc = pfc.invalidating(w, sf.DOC)
    revx, px, _d = w.standard(w.record(), path=pfc.RD2 + 'doc.json',
                              extra={FP: pfc.jb(doc), rv: w.review(FP, pfc.jb(doc))})
    o = outcome(w, classify=['%s:%s' % (revx, px)])
    case('REV-ROOT', 'a finding present only in the named REV\'s tree: detected through the REV root and blocking; '
                     'witness REV', o, blocked(o, False, revx))
    # a predicted M on an object-store M0 whose history holds f landed then deleted
    from ledger_coverage.engine import gitobj
    w, c1, fb = landed(r)
    M0 = step(w, {FP: None, rv: None}, 'delete f')
    w.repo = gitobj.Overlay(w.repo)
    w.M = w.repo.derive(M0, {'tools/syn-tool/x.py': b'x = 1\n'}, parents=[M0], subject='predicted M')
    o = outcome(w)
    case('N-PREDICTED-M', 'a predicted M built in memory on M0, whose history holds f landed then deleted: still '
                          'blocked (the walk crosses from the in-memory chain into M0\'s history)', o,
         blocked(o, False, c1))
    # F first in the witness order
    def with_f(w_):
        d0 = pfc.invalidating(pfc.World(r), sf.DOC)
        b0 = pfc.jb(d0)
        return {'files': {FP: b0, rv: pfc.World(r).review(FP, b0)}}
    w = pfc.World(r, variant=with_f)
    doc = pfc.invalidating(w, sf.DOC)
    pfc.land(w, [(FP, doc)])
    step(w, {FP: None, rv: None}, 'delete f on main')
    from ledger_coverage.adapters import host_fixture as hf
    F = hf.freeze(w.repo, w.c, w.p)
    code, out = w.run([], harness=False)
    fs = [f for f in ((out or {}).get('category3') or {}).get('findings') or [] if f['record']['path'] == FP]
    case('P-WITNESS-F', 'f absent at M, present in F\'s tree and on M\'s first-parent chain: the witness is F (order '
                        'M, REV, F, then the first-parent chain)', {'exit': code, 'findings': fs, 'F': F,
                                                                   'stop': (out or {}).get('stop')},
         bool(fs) and all(f['witness'] == F and f['present_at_M'] is False for f in fs))


def amendment_7_controls(r):
    """r13 Amendment 7 (adopted at fbfeac8a with every-configuration binding). Gap (i): side_change_commits limit the
    runs a finding blocks only when every element is a held commit that changes the entry's path against its first
    parent and is an ancestor of a witness of the record carrying the entry; otherwise the finding blocks every run in
    which it is found and the list is a form failure. Gap (ii): an element whose id is missing, not a string or not an
    edit id of the named configuration binds its lineage at run level, in addition to the edits bound otherwise; an
    unresolvable configuration binds every configuration at run level."""
    rv = FP[:-5] + '.review.json'

    def scope_fail(o):
        return 'retirement-blocked' in o['classes'] and 'record-invalid' in o['classes'] and \
            any('does not scope the finding' in d for d in o['invalid'] + o['reassess_why'])

    def with_scc(scc, prep=None, delete=False):
        w = pfc.World(r)
        extra = prep(w) if prep else None
        doc = pfc.invalidating(w, sf.DOC)
        doc['paths'][0]['side_change_commits'] = scc(w, extra) if callable(scc) else scc
        pfc.land(w, [(FP, doc)])
        if delete:
            step(w, {FP: None, rv: None}, 'delete f')
        return outcome(w)
    o = with_scc([])
    case('A7-I-1', 'a first-kind finding whose entry has side_change_commits []: FAIL retirement-blocked and '
                   'record-invalid', o, scope_fail(o))
    o = with_scc([], delete=True)
    case('A7-I-2', 'the same, the record deleted later: FAIL retirement-blocked', o,
         'retirement-blocked' in o['classes'] and FP in o['blocked'])
    o = with_scc(['1' * 40])
    case('A7-I-3', 'the list holds a well-formed commit id the store does not hold: FAIL retirement-blocked and '
                   'record-invalid', o, scope_fail(o))

    def notes_commit(w):
        return step(w, {'notes/other.txt': b'other\n'}, 'a commit that does not change the path')
    o = with_scc(lambda w, c: [c], prep=notes_commit)
    case('A7-I-4', 'the list holds a held commit that does not change the entry\'s path: FAIL retirement-blocked and '
                   'record-invalid', o, scope_fail(o))

    def branch_commit(w):
        return w.repo.derive(w.M, {sf.DOC: w.repo.read(w.M, sf.DOC) + b'branch\n'}, parents=[w.M],
                             subject='a change on an unmerged branch')
    o = with_scc(lambda w, c: [c, 'junk'], prep=branch_commit)
    case('A7-I-5', 'the list holds a commit that changes the path but is not in the run\'s M, and "junk": FAIL '
                   'retirement-blocked and record-invalid', o, scope_fail(o))
    o = with_scc(lambda w, c: [c], prep=branch_commit)
    case('A7-I-8', 'the list holds only a held commit on an unmerged branch that changes the path and is no ancestor '
                   'of a witness of the record: FAIL retirement-blocked and record-invalid', o, scope_fail(o))

    def merge_same_first(w):
        side = w.repo.derive(w.M, {sf.DOC: w.repo.read(w.M, sf.DOC) + b'side\n'}, parents=[w.M], subject='side')
        return step(w, {'notes/merge.txt': b'm\n'}, 'a merge keeping the first parent\'s path', parents=[w.M, side])
    o = with_scc(lambda w, c: [c], prep=merge_same_first)
    case('A7-I-9', 'the list holds only a merge commit whose tree entry for the path equals its first parent\'s: FAIL '
                   'retirement-blocked and record-invalid', o, scope_fail(o))
    w, c1, fb = landed(r)
    o = outcome(w)
    case('A7-I-SCOPED', 'a well-formed finding whose list names the commits that changed the path before the record '
                        'landed: no scope failure, it blocks as before', o,
         'retirement-blocked' in o['classes'] and not any('does not scope' in d for d in o['invalid']))
    # a second-kind finding on an entry whose side_change_commits is []
    w = pfc.World(r)
    q = w.record(record_id='syn-recon-q')
    q['paths'][0]['side_change_commits'] = []
    qb = pfc.jb(q)
    QP = pfc.RD + 'q.json'
    pfc.land(w, [(QP, q)], 'a no-effect record with an empty list')
    inv = pfc.invalidating(w, sf.DOC)['paths'][0]['scientific_effect']
    verdicts = [{'item': i, 'verdict': 'accept', 'reason': ''} for i in rec.item_ids(q)]
    for v in verdicts:
        if v['item'] == sf.DOC + ':scientific_effect':
            v.update(verdict='invalidates', reason='x', invalidated=inv['invalidated'],
                     configuration=inv['configuration'])
    z = pfc.jb(review_record({'schema': rec.review_schema, 'reviewer': 'session.fixture-reviewer-x', 'reviewed': {'path': QP,
                                                                                  'blob_sha256': sf.sha(qb)},
                'method': 'read ' + 'a' * 40, 'verdicts': verdicts}))
    step(w, {pfc.RD + 'q.second.review.json': z}, 'an independent review finds invalidation')
    o = outcome(w)
    case('A7-I-6', 'a second-kind finding on an entry whose side_change_commits is []: FAIL retirement-blocked and '
                   'record-invalid', o, scope_fail(o))

    # gap (ii)
    unknown = {'id': 'NO-SUCH-EDIT', 'sha256': '0' * 64,
               'target': {'path': 'nowhere.md', 'start_H': 0, 'old_sha256': '0' * 64}}

    def with_elems(mk, world=None, cfg=None, delete=False, pre=None):
        w = world() if world else pfc.World(r)
        if pre:
            pre(w)
        doc = pfc.invalidating(w, sf.DOC)
        se = doc['paths'][0]['scientific_effect']
        se['invalidated'] = mk(se['invalidated'][0])
        se['conclusions'] = 'none'
        if cfg is not None:
            se['configuration'] = cfg
        pfc.land(w, [(FP, doc)])
        if delete:
            step(w, {FP: None, rv: None}, 'delete f')
        return outcome(w)

    def run_level(o):
        return 'retirement-blocked' in o['classes'] and FP in o['runlevel']
    o = with_elems(lambda e: [dict(unknown)])
    case('A7-II-1', 'an element whose id is no edit of the named configuration (its target held by no ledger), under '
                    'the run\'s configuration: FAIL run-level retirement-blocked and record-invalid', o,
         run_level(o) and 'record-invalid' in o['classes'])
    o = with_elems(lambda e: [dict(unknown)], delete=True)
    case('A7-II-2', 'the same, the record deleted later: FAIL run-level retirement-blocked', o, run_level(o))
    w_ = pfc.World(r)
    o4 = with_elems(lambda e: [e, dict(unknown)])
    case('A7-II-4', 'a valid element naming E1 and an unknown id: category3.blocked holds E1 and a run-level entry',
         {'blocked': o4['blocked'], 'runlevel': o4['runlevel']},
         FP in o4['runlevel'] and o4['blocked'].count(FP) >= 2)
    o5 = {'no id': with_elems(lambda e: [e, {k: v for k, v in unknown.items() if k != 'id'}]),
          'numeric id': with_elems(lambda e: [e, dict(unknown, id=5)])}
    case('A7-II-5', 'a valid element and a second element without id, or with a numeric id: FAIL run-level '
                    'retirement-blocked and record-invalid', {k: v['runlevel'] for k, v in o5.items()},
         all(run_level(v) and 'record-invalid' in v['classes'] for v in o5.values()))
    o = with_elems(lambda e: [dict(unknown, target=dict(e['target']))])
    case('A7-II-6', 'an unknown id whose target matches the run\'s E1 by path and old_sha256: FAIL run-level (the '
                    'target match does not keep it below run level)', o, run_level(o))

    def other_retirement():
        return pfc.World(r, variant=lambda w_: {'extra': {'retirement': {'name': 'other', 'issue': 'other'},
                                                           'config_id': 'other-retirement-config'}})
    o = with_elems(lambda e: [dict(unknown)], world=other_retirement,
                   cfg={'path': 'syn/none/config.json', 'blob_sha256': '0' * 64})
    case('A7-II-7', 'an unknown id under a configuration that cannot be resolved, the run under another retirement: '
                    'FAIL run-level retirement-blocked and record-invalid (every configuration)', o,
         run_level(o) and 'record-invalid' in o['classes'])
    base_cfg = pfc.invalidating(pfc.World(r), sf.DOC)['paths'][0]['scientific_effect']['configuration']
    o = with_elems(lambda e: [dict(unknown)], world=other_retirement, cfg=base_cfg,
                   pre=lambda w: land_original_plan(w, r))
    case('A7-II-C1', 'case 1\'s finding naming the original plan (resolvable), the run under another retirement '
                     'outside its lineage that carries neither the id nor the target: not retirement-blocked', o,
         'retirement-blocked' not in o['classes'])
    del w_


def amendment_7_unit_controls(r):
    """r13 Amendment 7 at the level of c3.scope_problems on an in-memory history (gap (i) 8b, C1, C3) and of the binding
    with a retained edit id (gap (ii)); gap (ii) case 3 at run level."""
    from ledger_coverage.engine import category3 as c3m, gitobj
    schemas = ('oi-reconciliation/1', 'oi-reconciliation/2')
    prefix = 'verification/audits/'
    repo = gitobj.Overlay()
    rp = 'verification/audits/u/rec.json'
    rb = pfc.jb({'schema': 'oi-reconciliation/2', 'record_id': 'u-rec', 'paths': []})
    rref = {'path': rp, 'blob_sha256': sf.sha(rb)}
    m0 = repo.add_commit({'doc.md': b'a\n'}, [], 'root')
    b1 = repo.derive(m0, {'doc.md': b'b\n'}, parents=[m0], subject='the change, on a branch')
    b2 = repo.derive(b1, {rp: rb}, parents=[b1], subject='the record lands on the branch')
    ms = repo.derive(m0, {'doc.md': b'b\n', rp: rb}, parents=[m0], subject='the record squash-landed on M')
    cum = c3m.Cumulative(repo, [ms, b2], schemas, prefix)
    cum_m = c3m.Cumulative(repo, [ms], schemas, prefix)
    got8b = c3m.scope_problems(repo, [b1], 'doc.md', rref, cum, cum_m)
    case('A7-I-8B', 'the list\'s only element is a branch commit that changes the path and is an ancestor of a witness '
                    'reached through F, while the record\'s witness in M\'s ancestry (a squash landing) does not descend '
                    'from it: the list does not scope the finding', got8b, bool(got8b))
    # C1: the record has no witness in M's ancestry and is found through REV; the list's commits change the path, are
    # ancestors of that witness, and are not in M
    rev = repo.derive(b1, {rp: rb}, parents=[b1], subject='REV holding the record')
    cum_r = c3m.Cumulative(repo, [m0, rev], schemas, prefix)
    cum_r_m = c3m.Cumulative(repo, [m0], schemas, prefix)
    c1 = c3m.scope_problems(repo, [b1], 'doc.md', rref, cum_r, cum_r_m)
    case('A7-I-C1', 'a record with no witness in M\'s ancestry, found through REV, whose list names a commit changing '
                    'the path, an ancestor of that witness and not in M: the list scopes the finding (and M does not '
                    'contain it, so the run is not blocked)', {'problems': c1, 'in_m': c3m.in_m(repo, m0, [b1])},
         c1 == [] and not c3m.in_m(repo, m0, [b1]))
    side = repo.derive(m0, {'other.md': b'o\n'}, parents=[m0], subject='another line')
    mg = repo.derive(side, {'doc.md': b'b\n'}, parents=[side, b1], subject='a merge bringing the change in')
    rev3 = repo.derive(mg, {rp: rb}, parents=[mg], subject='REV after the merge')
    c3 = c3m.scope_problems(repo, [mg], 'doc.md', rref, c3m.Cumulative(repo, [m0, rev3], schemas, prefix), cum_r_m)
    case('A7-I-C3', 'C1 with the only element a merge commit whose tree entry for the path differs from its first '
                    'parent\'s, an ancestor of the witness: the list scopes the finding', c3, c3 == [])

    # C2: a no-effect entry, not a finding, with side_change_commits [] on a mode-only change of the ledgered path
    w = pfc.World(r)
    w.M = w.repo.derive(w.syn.H, {sf.DOC: ('exec', w.repo.read(w.syn.H, sf.DOC))}, parents=[w.syn.H],
                        subject='a mode-only change')
    q = w.record(record_id='syn-recon-c2')
    q['paths'][0]['side_change_commits'] = []
    rv_, pth, _ = w.standard(q)
    code, out = w.run(['%s:%s' % (rv_, pth)], harness=True)
    out = out or {}
    cls = sorted({i['class'] for i in out.get('items', [])})
    inv = [i.get('subject') for i in out.get('items', []) if i['class'] == 'record-invalid']
    case('A7-I-C2', 'a no-effect entry (not a finding) with side_change_commits [] on a mode-only change: FAIL '
                    'base-drift, not retirement-blocked; the record is not record-invalid unless the post-freeze '
                    'route refuses it, which it does here: R6.RECON.2 (b) compares blobs, so a mode-only path is no '
                    'drifted path (the recorded mode gap)',
         {'classes': cls, 'invalid': inv},
         'base-drift' in cls and 'retirement-blocked' not in cls)
    # gap (ii): an element naming a retained edit of the named configuration is a known id (no run-level binding)
    class B:
        repo = None
        led = {'raw': {'edits': []}, 'splices': [], 'retained': []}

        def finding_config(self, cref):
            return ({}, {'raw': {'edits': []}, 'splices': [],
                         'retained': [{'id': 'R1', 'file': 'doc.md', 'text': 'kept\n'}]}, 'H')

        def in_lineage(self, fdoc, fref):
            return True
    elem = {'id': 'R1', 'sha256': '0' * 64, 'target': {'path': 'doc.md', 'start_H': 0, 'old_sha256': '0' * 64}}
    f = {'kind': 2, 'form': [], 'configuration': {'path': 'x', 'blob_sha256': '0' * 64}, 'invalidated': [elem],
         'verdict_item': 'doc.md:scientific_effect', 'entry': {'path': 'doc.md'}}

    class Repo:
        def read(self, c, p):
            return b'kept\nother\n'
    B.repo = Repo()
    bound = c3m.bind(f, B())
    unknown = c3m.bind(dict(f, invalidated=[dict(elem, id='NO-SUCH')]), B())
    case('A7-II-RETAINED', 'an element naming a retained edit of the named configuration is an edit id of its edit '
                           'list (retained edits included): no run-level binding; an unknown id binds at run level',
         {'retained': bound[1], 'unknown': unknown[1]}, bound[1] is False and unknown[1] is True)
    # gap (ii) case 3: the run under a later version of the same retirement that carries no edit of that id
    unknown_el = {'id': 'NO-SUCH-EDIT', 'sha256': '0' * 64,
                  'target': {'path': 'nowhere.md', 'start_H': 0, 'old_sha256': '0' * 64}}
    w = pfc.World(r, edits=pfc.EDITS_OTHER, first_id=2, variant=lambda w_: {'extra': {'version': 2}})
    land_original_plan(w, r)
    doc = pfc.invalidating(pfc.World(r), sf.DOC)
    doc = pfc.rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, pfc.World(r).led, sf.DOC,
                          scientific_effect=dict(doc['paths'][0]['scientific_effect'], invalidated=[unknown_el],
                                                 conclusions='none'))
    doc.update(record_id='syn-finding-v1', author=sf.WRITER, supersedes=None, M=w.M, X=w.X)
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('A7-II-3', 'the finding names the original plan (resolvable); the run under a later version of the same '
                    'retirement (in its lineage) that carries no edit of that id: FAIL run-level retirement-blocked',
         {'classes': o['classes'], 'runlevel': o['runlevel']},
         'retirement-blocked' in o['classes'] and FP in o['runlevel'])


def run_level_ledger_controls(r):
    """Owner decision of 2026-11-27: a resolvable configuration whose ledger cannot be read, several splices for one
    edit, retained text not unique at H, an edit with neither splice nor retained text, and an unreadable delegation
    contract of a named configuration bind the finding at run level (FAIL retirement-blocked with FAIL record-invalid,
    evidence and provenance kept), not ERROR."""
    from ledger_coverage.engine import category3 as c3m, findings as fd
    # end to end: the finding names another retirement's configuration, resolvable on main, whose ledger input does
    # not match its pin, so the ledger cannot be read through it
    w = pfc.World(r)
    pd = w.files['syn/patch.json']
    oc_, op_, os_, ofiles = w.syn.build({'patch_sha': '0' * 64, 'files': {'syn/patch.json': pd},
                                         'config_path': 'syn/other/config.json',
                                         'extra': {'retirement': {'name': 'other', 'issue': 'other'},
                                                   'config_id': 'other-retirement-config'}})
    step(w, {q: b for q, b in ofiles.items() if isinstance(b, bytes)}, 'another retirement\'s configuration on main')
    doc = pfc.invalidating(w, sf.DOC)
    doc['paths'][0]['scientific_effect']['configuration'] = {'path': op_, 'blob_sha256': os_}
    pfc.land(w, [(FP, doc)])
    o = outcome(w)
    case('RUNLEVEL-LEDGER-UNREADABLE', 'the finding names a resolvable configuration whose ledger cannot be read: '
                                       'run-level FAIL retirement-blocked and FAIL record-invalid with evidence and '
                                       'provenance, the reason stated, no ERROR', o,
         runlevel_fail(o, FP) and any('ledger of the named configuration' in d for d in o['invalid']))

    # the ledger targets, at the level of the predicate and of the binding
    class H_repo:
        def read(self, c, p):
            return b'same\nsame\n'
    led_multi = {'splices': [{'id': 'E1', 'file': 'a'}, {'id': 'E1', 'file': 'b'}], 'retained': [], 'raw': {}}
    led_ret = {'splices': [], 'retained': [{'id': 'E1', 'file': 'a', 'text': 'same\n'}], 'raw': {}}
    led_none = {'splices': [], 'retained': [], 'raw': {'edits': [{'id': 'E1'}]}}
    got = {}
    for name, led in (('multi', led_multi), ('retained', led_ret), ('none', led_none)):
        try:
            c3m.expected_target(H_repo(), led, 'H', 'E1')
            got[name] = 'no block'
        except fd.RunLevelBlock as exc:
            got[name] = 'block: ' + str(exc)[:80]
        except fd.Unsettled as exc:
            got[name] = 'unsettled: ' + str(exc)[:80]

    class B:
        def finding_config(self, cref):
            raise fd.RunLevelBlock('Form (ii): the ledger of the named configuration x cannot be read (y)')
    bound = c3m.bind({'form': [], 'configuration': {'path': 'x', 'blob_sha256': '0' * 64}, 'kind': 1}, B())
    case('RUNLEVEL-LEDGER-TARGETS', 'several splices for one edit, retained text twice at H, an edit with neither '
                                    'splice nor retained text: each a run-level block (not ERROR); a block raised '
                                    'while binding gives (no edits, run level, the reason as a form failure)',
         {'targets': got, 'bind': bound},
         all(v.startswith('block') for v in got.values()) and bound[0] == [] and bound[1] is True and
         any('binds at run level' in x for x in bound[2]))


SUITES = [('removal', removal_controls), ('topology', topology_controls), ('unreadable', unreadable_controls),
          ('positive', positive_controls), ('reassessment', reassessment_controls),
          ('clearance-predicates', clearance_predicates), ('identity-and-set', identity_and_set_controls),
          ('more-negative', more_negative_controls), ('monotone', monotone_controls),
          ('predecessor-widening', predecessor_widening_unit),
          ('pairing-predecessor', pairing_predecessor_controls),
          ('pairing-review-order', pairing_review_order_control), ('r13-form', r13_form_controls),
          ('run-level-ledger', run_level_ledger_controls), ('amendment-7', amendment_7_controls),
          ('amendment-7-unit', amendment_7_unit_controls),
          ('read-domain', read_domain_controls), ('milestone', milestone_controls),
          ('explicit-review', explicit_review_controls), ('nits-0cafbdc0', nits_0cafbdc0_controls)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    LOCAL.start()
    root = tempfile.mkdtemp(prefix='obl29-', dir=out)
    r = sf.Runner(root)
    for name, fn in SUITES:
        try:
            fn(r)
        except Exception as exc:  # a suite that cannot run is a failed control of its own
            import traceback
            case(name + '/group-error', 'the suite runs', '%s: %s %s' % (type(exc).__name__, exc,
                                                                          traceback.format_exc()[-1500:]), False)
    with open(os.path.join(out, 'obl29-controls.json'), 'w') as f:
        json.dump({'schema': 'oi-local-controls/1', 'suite': 'obl29', 'cases': RESULTS}, f, indent=1,
                  sort_keys=True, default=str)
        f.write('\n')
    LOCAL.write(out, RESULTS)
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'obl29-controls-out'))
