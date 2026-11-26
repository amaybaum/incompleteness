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
                rv = pfc.jb({'schema': rec.review_schema, 'reviewer': sf.REVIEWER,
                             'reviewed': {'path': q, 'blob_sha256': sf.sha(b)}, 'method': 'read',
                             'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(d)]})
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
                                            'the reassessment applies', o0,
         'retirement-blocked' not in o0['classes'] and o0['reassessments'])
    case('N-OPERATIVE-PREDECESSOR-DISSENT-DELETED', 'an eligible review of the operative predecessor rejecting an item, '
                                                    'landed and deleted: the discharge fails and the block stands', o1,
         'retirement-blocked' in o1['classes'] and 'record-invalid' in o1['classes'] and not o1['reassessments'])

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
    Q = {'schema': 'oi-reconciliation/2', 'record_id': 'q', 'author': 'writer-q', 'supersedes': None,
         'paths': [{'path': p, 'side_change_commits': ['c' * 40]}, {'path': p2, 'side_change_commits': ['d' * 40]}]}
    qb = jb(Q)
    qref = {'path': 'verification/audits/q/rec.json', 'blob_sha256': sf.sha(qb)}
    V = {'schema': rec.review_schema, 'reviewer': 'reviewer-v', 'reviewed': dict(qref), 'method': 'read',
         'verdicts': [{'item': i, 'verdict': 'reject' if i == p + ':scientific_effect' else 'accept',
                       'reason': 'the repair does not restore the basis'} for i in rec.item_ids(Q)]}
    vb = jb(V)
    W = {'kind': 'review', 'disputed': qref, 'disputed_doc': Q, 'disputed_git': blob_id_of(qb), 'edge': None,
         'forming': [{'doc': V, 'git': blob_id_of(vb), 'path': 'verification/audits/q/rec.review.json'}],
         'contested': [], 'original': (('f', 'item'), p + ':scientific_effect')}
    fgit = 'f' * 40
    Rd = {'schema': 'oi-reconciliation/2', 'record_id': 'r', 'author': 'writer-r', 'supersedes': None,
          'paths': [{'path': p, 'side_change_commits': ['c' * 40]}]}
    rb = jb(Rd)
    R = {'ref': {'path': 'verification/audits/r/rec.json', 'blob_sha256': sf.sha(rb)}, 'doc': Rd,
         'lineage_blobs': [], 'lineage_edges': []}
    A = {'doc': {'author': 'writer-a'}}

    def D(entry_ref, entry_doc, entry_path=p, finding=(('g', 'x'), 'i'), commits=('e' * 40,)):
        return {'reassessment': A, 'finding': finding, 'lineage_blobs': [], 'lineage_edges': [],
                'repair': {'entry': entry_ref, 'entry_doc': entry_doc, 'entry_path': entry_path,
                           'commits': list(commits)}}
    toks = [o.item_token(W['forming'][0]['git'], p + ':scientific_effect')]
    ftok = o.item_token(fgit, 'i')
    reason = 'the corrected record restores the basis ' + ' '.join(toks)

    def Z(**kw):
        z = {'schema': rec.review_schema, 'reviewer': 'reviewer-v', 'reviewed': dict(R['ref']),
             'method': ' '.join([W['disputed_git'], W['forming'][0]['git']] + toks + [ftok]),
             'verdicts': [{'item': i, 'verdict': 'accept', 'reason': reason} for i in rec.item_ids(Rd)],
             '_dir': 'verification/audits/r'}
        z.update(kw)
        return z
    d_other_entry = D(qref, Q, entry_path=p2)
    got = o.reliance(d_other_entry, W)
    case('N-REFREEZE-OTHER-ENTRY-SAME-Q-pred', 'a discharge citing another entry of the same multi-path disputed record '
                                               'relies through (r1) (and (r3) on shared commits)', got, 'r1' in got)
    copy_ref = {'path': 'verification/audits/copy/rec.json', 'blob_sha256': qref['blob_sha256']}
    got = o.reliance(D(copy_ref, Q), W)
    case('N-REFREEZE-REVIEW-WITNESS-COPY-pred', 'a byte-identical copy of the disputed record at another path relies '
                                                'through (r1)', got, 'r1' in got)
    unrelated = {'schema': 'oi-reconciliation/2', 'record_id': 'q', 'author': 'writer-u', 'supersedes': None,
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
    negs = [
        ('N-REFREEZE-REVIEW-WITNESS-OTHER-REVIEWER-pred', 'Z by an independent reviewer other than V\'s',
         dict(Z=Z(reviewer='reviewer-x'))),
        ('N-REFREEZE-REVIEW-WITNESS-SELF-pred', 'Z by V\'s reviewer who is also the reassessment\'s author',
         dict(Z=Z(), A_author='reviewer-v')),
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
    wsp = dict(Q, paths=[{'path': 'doc/s s.md', 'side_change_commits': ['c' * 40]}])
    Vs = {'schema': rec.review_schema, 'reviewer': 'reviewer-v', 'reviewed': dict(qref), 'method': 'read',
          'verdicts': [{'item': 'doc/s s.md', 'verdict': 'reject', 'reason': 'x'}]}
    Ws = dict(W, disputed_doc=wsp, forming=[{'doc': Vs, 'git': blob_id_of(jb(Vs)), 'path': 'x'}])
    got = o.nr5(Z(), Ws['forming'][0], Ws, R, D(R['ref'], Rd), fgit, [])
    case('N-REFREEZE-REVIEW-WITNESS-WHITESPACE-ITEM-pred', 'an adverse item id with a space: no Z can meet NR-5', got,
         got == ['an adverse item id of V cannot form a token'])
    Wl = dict(W, kind='lineage', forming=[{'doc': {}, 'git': 'b' * 40, 'path': 's'}])
    rv = {'reviewer': 'reviewer-n', 'reviewed': dict(R['ref']), '_dir': 'verification/audits/r',
          'method': ' '.join([W['disputed_git'], 'b' * 40]),
          'verdicts': [{'item': i, 'verdict': 'accept'} for i in rec.item_ids(Rd)]}
    b1 = o.decide(dR, Wl, R=R, required_review=rv, excluded=['writer-r', 'writer-q', 'reviewer-v'], nr2=True)
    b2 = o.decide(dR, Wl, R=R, required_review=dict(rv, reviewer='writer-q'),
                  excluded=['writer-r', 'writer-q', 'reviewer-v'], nr2=True)
    b3 = o.decide(dR, Wl, R=R, required_review=dict(rv, method='read'),
                  excluded=['writer-r', 'writer-q', 'reviewer-v'], nr2=True)
    case('P-REFREEZE-INDEPENDENT-REPLACEMENT-pred', 'a lineage witness, reliance through (r3) only, an independent '
                                                    'replacement meeting NR-1 to NR-4: cleared', b1,
         b1[0] is False and b1[2] and 'NR-1' in b1[2])
    case('N-REFREEZE-NONRELIANCE-UNSUPPORTED-pred', 'the NR-3 reviewer is an excluded author, or NR-4\'s tokens are '
                                                    'absent: the witness stands', [b2, b3], b2[0] and b3[0])
    Rl = dict(R, lineage_blobs=[qref['blob_sha256']])
    b4 = o.decide(dR, Wl, R=Rl, required_review=rv, excluded=[], nr2=True)
    case('NR1-LINEAGE-pred', 'R\'s lineage holds the disputed record\'s blob: NR-1 fails, the witness stands', b4,
         b4[0])
    b5 = o.decide(D(qref, Q), W, R=R, Z=Z(), nr2=True, finding_git=fgit)
    case('N-REFREEZE-INAPPLICABILITY-ASSERTED-pred', 'reliance through (r1) is conclusive: NR evidence cannot clear '
                                                     'it (only Inapplicable(W) or route 2)', b5, b5[0])


SUITES = [('removal', removal_controls), ('topology', topology_controls), ('unreadable', unreadable_controls),
          ('positive', positive_controls), ('reassessment', reassessment_controls),
          ('clearance-predicates', clearance_predicates)]


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
