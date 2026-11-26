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

from ledger_coverage.adapters import synthetic_fixture as sf  # noqa: E402
from ledger_coverage.adapters import postfreeze_controls as pfc  # noqa: E402
from ledger_coverage.engine import records as rec  # noqa: E402

RESULTS = []
FP = pfc.RD + 'finding.json'


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


def outcome(w, **kw):
    code, out = w.run([], harness=True, **kw)
    out = out or {}
    c3 = out.get('category3') or {}
    fs = [f for f in c3.get('findings') or [] if (f.get('record') or {}).get('path') == FP]
    return {'exit': code, 'classes': sorted({i['class'] for i in out.get('items', [])}),
            'stop': (out.get('stop') or {}).get('class'), 'finding': fs,
            'blocked': [b['record']['path'] for b in c3.get('blocked') or []],
            'reassessments': c3.get('reassessments'),
            'invalid': [d for i in out.get('items', []) if i['class'] == 'record-invalid'
                        for d in (i.get('detail') or [])][:3]}


def blocked(o, present=False, witness=None):
    ok = o['exit'] == 20 and 'retirement-blocked' in o['classes'] and FP in o['blocked'] and len(o['finding']) >= 1
    if ok:
        ok = any(f.get('present_at_M') is present and (witness is None or f.get('witness') == witness)
                 for f in o['finding'])
    return ok


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
    # depends on R6.PUR.12 (SIDE-NONREG): the side-change classifier at this tool revision reads the symbolic link's
    # bytes and refuses (ERROR UNRESOLVABLE) before category 3 is evaluated; that correction is outside OBL-29
    case('N-SYMLINK', 'f replaced by a symbolic link: still blocked, present_at_M false', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: ('submodule', '9' * 40)}, 'replace by a gitlink')
    o = outcome(w)
    case('N-GITLINK', 'f replaced by a gitlink: still blocked', o, blocked(o, False, c1))
    w, c1, fb = landed(r)
    step(w, {FP: b'\xef\xbb\xbf' + fb}, 'prepend bytes')
    o = outcome(w)
    case('N-PREPEND', 'bytes prepended to f: still blocked', o, blocked(o, False, c1))
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
    eff = dict(pfc.CONTROL_EFFECT, conclusions='none', verdict='invalidates',
               invalidated=[{'id': 'E1', 'sha256': pfc.rcmod.edit_key(pfc.World(r).led, 'E1')}])
    doc = pfc.rcmod.draft(w.repo, w.ctx, w.syn.H, w.M, w.X, w.led, sf.DOC, scientific_effect=eff)
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

    def adverse(ref_doc, ref_path, reviewer='reviewer-z', verdict='reject', drop_item=False, dissent=None):
        ids = rec.item_ids(ref_doc)
        v = [{'item': i, 'verdict': verdict if k == 0 else 'accept'} for k, i in enumerate(ids)]
        if drop_item:
            v = v[1:]
        d = {'schema': rec.review_schema, 'reviewer': reviewer,
             'reviewed': {'path': ref_path, 'blob_sha256': sf.sha(pfc.jb(ref_doc))}, 'method': 'read',
             'verdicts': v}
        if dissent:
            d['dissent'] = dissent
        return pfc.jb(d)

    def repair_doc(w):
        return json.loads(w.repo.read(w.M, w.repair_entry['path']))

    o = outcome(world(lambda w1: pfc.reassessment(w1)))
    case('P-REASSESS-CURRENT-BASELINE', 'an applying reassessment with all reviews present: not blocked', o,
         'retirement-blocked' not in o['classes'] and o['reassessments'])

    def delete_finding(w):
        step(w, {FP: None, FP[:-5] + '.review.json': None}, 'delete f')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=delete_finding))
    case('P-REASSESS-AFTER-DELETE', 'f deleted; a reassessment naming its original reference applies: not blocked; f '
                                    'reported with present_at_M false', o,
         'retirement-blocked' not in o['classes'] and o['reassessments'] and
         any(f.get('present_at_M') is False for f in o['finding']))

    def repair_dissent(kind):
        def after(w):
            qd = repair_doc(w)
            q = w.repair_entry['path']
            d = q.rsplit('/', 1)[0] + '/'
            name = d + 'repair.second-review.json'
            b = adverse(qd, q, drop_item=(kind == 'items'), verdict='accept' if kind == 'items' else 'reject',
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
        case(cid, what + ': the discharge fails (record-invalid) and the block stands', o,
             'retirement-blocked' in o['classes'] and 'record-invalid' in o['classes'] and not o['reassessments'])

    def repair_dissent_elsewhere(w):
        qd = repair_doc(w)
        step(w, {'verification/audits/syn-other/repair.review.json': adverse(qd, w.repair_entry['path'])},
             'a rejecting review of the repair in another directory')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=repair_dissent_elsewhere))
    case('P-REPAIR-REVIEW-OTHER-DIRECTORY', 'a rejecting review of the repair record outside its directory does not '
                                            'count for the repair-review check: the reassessment applies', o,
         'retirement-blocked' not in o['classes'] and o['reassessments'])

    def reassess_dissent(w):
        a = json.loads(w.repo.read(w.c, pfc.RA_PATH))
        name = 'verification/audits/syn-dissent/reassessment.review.json'
        step(w, {name: adverse(a, pfc.RA_PATH)}, 'a rejecting review of the reassessment')
        step(w, {name: None}, 'delete it')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=reassess_dissent))
    case('N-REASSESS-DISSENT-DELETED', 'an eligible review of the cited reassessment rejecting an item, landed on main '
                                       'and then deleted: the discharge fails and the block stands', o,
         'retirement-blocked' in o['classes'] and 'record-invalid' in o['classes'] and not o['reassessments'])

    def self_review(w):
        a = json.loads(w.repo.read(w.c, pfc.RA_PATH))
        step(w, {'verification/audits/syn-dissent/self.review.json': adverse(a, pfc.RA_PATH, reviewer=sf.WRITER)},
             'a rejecting review by the reassessment\'s author')
    o = outcome(world(lambda w1: pfc.reassessment(w1), after=self_review))
    case('P-HISTORICAL-SELF-REVIEW', 'a rejecting review by the reassessment\'s own author is not eligible: the '
                                     'reassessment applies', o,
         'retirement-blocked' not in o['classes'] and o['reassessments'])

    def rewrite(w):
        b = w.repo.read(w.M, FP)
        step(w, {FP: b.replace(b'"invalidates"', b'"no-effect"')}, 'rewrite f')
    w1 = pfc.finding_world(r, edits=pfc.EDITS_REWORDED)
    rewrite(w1)
    new_ref = {'path': FP, 'blob_sha256': sf.sha(w1.repo.read(w1.M, FP))}
    o = outcome(world(lambda w_: pfc.reassessment(w_, finding=new_ref), after=rewrite))
    case('N-FORGED-REASSESS-NEWBLOB', 'a reassessment naming the rewritten blob, which carries no finding: it fails '
                                      'and the original finding still blocks', o,
         'retirement-blocked' in o['classes'] and 'record-invalid' in o['classes'])


SUITES = [('removal', removal_controls), ('topology', topology_controls), ('unreadable', unreadable_controls),
          ('positive', positive_controls), ('reassessment', reassessment_controls)]


def main(out):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
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
    bad = [c['id'] for c in RESULTS if c['status'] != 'PASS']
    print(json.dumps({'cases': len(RESULTS), 'failed': bad}))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'obl29-controls-out'))
