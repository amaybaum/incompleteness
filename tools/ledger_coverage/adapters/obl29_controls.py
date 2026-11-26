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
from ledger_coverage.engine import category3 as c3  # noqa: E402

RESULTS = []
FP = pfc.RD + 'finding.json'


def case(cid, expected, actual, holds):
    RESULTS.append({'id': cid, 'expected': expected, 'actual': actual, 'status': 'PASS' if holds else 'FAIL'})


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
                             i.get('subject') == pfc.RA_PATH for d in (i.get('detail') or [])]}


def custody_only(o):
    """OBL-29 sec. 2.2 fail-closed: the cited reassessment's only problem is the unestablished custody, so that it
    would apply apart from custody, and the block stands (FAIL record-invalid and retirement-blocked)."""
    return o['reassess_why'] == [c3.custody_unverified] and 'retirement-blocked' in o['classes'] and \
        not o['reassessments']


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
    # the BOM-prefixed file fails the strict parse (R6.RECON.29) and is a class (b) malformed finding with an
    # invalidation signal; a malformed finding has no entry, and whether R6.RECON.26's side_change_commits gate admits
    # it is not settled: the run stops with ERROR DESIGN_UNSETTLED (fail closed, no verdict)
    case('N-PREPEND', 'bytes prepended to f: the prefixed copy is a malformed finding whose applicability the design '
                      'does not settle, so the run stops with ERROR DESIGN_UNSETTLED', o,
         o['exit'] == 65 and o['stop'] == 'DESIGN_UNSETTLED')
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
    rej = {'reviewer': 'reviewer-k', 'reviewed': dict(R['ref']), '_dir': 'verification/audits/r', 'method': 'read',
           'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'} for k, i in
                        enumerate(rec.item_ids(Rd))]}
    b = o.decide(D(R['ref'], Rd), W, R=R, Z=Z(), nr2=True, finding_git=fgit, reviews_of_R=[rej])
    case('NR5-NONACCEPT-REVIEW-pred', 'another eligible review of R rejecting an item without a dissent field: NR-3\'s '
                                      'dissent test fails NR-5, the witness stands', b, b[0] and b[1] == ['r3'])
    V2 = dict(V, reviewer='reviewer-w')
    W2 = dict(W, forming=W['forming'] + [{'doc': V2, 'git': blob_id_of(jb(V2)), 'path': 'v2'}])
    toks2 = toks + [o.item_token(W2['forming'][1]['git'], p + ':scientific_effect')]
    meth = ' '.join([W['disputed_git'], W2['forming'][0]['git'], W2['forming'][1]['git']] + toks2 + [ftok])
    reason2 = 'the corrected record restores the basis ' + ' '.join(toks2)
    zv = Z(method=meth, verdicts=[{'item': i, 'verdict': 'accept', 'reason': reason2} for i in rec.item_ids(Rd)])
    zw = dict(zv, reviewer='reviewer-w')
    b1 = o.decide(D(R['ref'], Rd), W2, R=R, Z=[zv], nr2=True, finding_git=fgit)
    b2 = o.decide(D(R['ref'], Rd), W2, R=R, Z=[zv, zw], nr2=True, finding_git=fgit)
    case('NR5-EVERY-V-pred', 'a review witness formed by two adverse reviews: resolving only the first leaves it '
                             'standing; a resolution by each reviewer clears it', [b1, b2], b1[0] and not b2[0])
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
    adverse = pfc.jb({'schema': rec.review_schema, 'reviewer': 'reviewer-z',
                      'reviewed': {'path': PP, 'blob_sha256': sf.sha(pb)}, 'method': 'read',
                      'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'}
                                   for k, i in enumerate(ids)]})
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
    adverse = pfc.jb({'schema': rec.review_schema, 'reviewer': 'reviewer-z',
                      'reviewed': {'path': PP, 'blob_sha256': sf.sha(pb)}, 'method': 'read',
                      'verdicts': [{'item': i, 'verdict': 'reject' if k == 0 else 'accept'}
                                   for k, i in enumerate(ids)]})
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
                         {'schema': rec.review_schema, 'kind': 'widening', 'reviewer': 'widener-z', 'reviewed': ref,
                          'method': 'read', 'verdicts': [{'item': 'ra:widened', 'verdict': self.verdict}]})]
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

    def second_kind_world(reviewer='reviewer-x', withdraw=False, reviewed_missing=False):
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
        z = pfc.jb({'schema': rec.review_schema, 'reviewer': reviewer, 'reviewed': ref,
                    'method': 'read ' + 'a' * 40, 'verdicts': verdicts})
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
    w, c1, ZP = second_kind_world(reviewer='https://example.invalid/runs/1')
    o = outcome(w)
    case('SECOND-KIND-RUN-REVIEWER', 'the same verdict by a run (a URL in reviewer): disqualified, no finding', o,
         not [f for f in o['all'] if f.get('kind') == 2])
    w, c1, ZP = second_kind_world(reviewed_missing=True)
    o = outcome(w)
    case('SECOND-KIND-REVIEWED-MISSING', 'an invalidates verdict whose reviewed names no record the scan finds: it '
                                         'counts (form failure) but has no entry; its applicability is not settled: '
                                         'ERROR DESIGN_UNSETTLED', o, o['exit'] == 65 and o['stop'] == 'DESIGN_UNSETTLED')
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
    case('N-MALFORMED-DELETED', 'a class (c) malformed finding landed and deleted: still in R*; a malformed finding has '
                                'no entry, so its applicability is not settled: ERROR DESIGN_UNSETTLED', o,
         o['exit'] == 65 and o['stop'] == 'DESIGN_UNSETTLED')
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
    del d0['paths'][0]['scientific_effect']['configuration']
    w = pfc.World(r, edits=pfc.EDITS_OTHER, first_id=2)
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
    good = rdm.problems(w.repo, out, [w.M])
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
    case('P-REPRESENTATIVE-READ-DOMAINS', 'the category-3 reads recorded with their source commit, path and blob all '
                                          'come from the named root or its verified history under the prefix; a read '
                                          'from an unrelated commit, outside the prefix, or with another blob is '
                                          'refused', {'good': good, 'reads': len(rd.get('reads') or []),
                                                      'forged': rdm.problems(w.repo, forged, [w.M]),
                                                      'outside': rdm.problems(w.repo, outside, [w.M]),
                                                      'wrong': rdm.problems(w.repo, wrong, [w.M])},
         good == [] and bool(rd.get('reads')) and rdm.problems(w.repo, forged, [w.M]) and
         rdm.problems(w.repo, outside, [w.M]) and rdm.problems(w.repo, wrong, [w.M]))


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
    # depends on R6.PUR.12 (SIDE-NONREG), as N-SYMLINK
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


SUITES = [('removal', removal_controls), ('topology', topology_controls), ('unreadable', unreadable_controls),
          ('positive', positive_controls), ('reassessment', reassessment_controls),
          ('clearance-predicates', clearance_predicates), ('identity-and-set', identity_and_set_controls),
          ('more-negative', more_negative_controls), ('monotone', monotone_controls),
          ('predecessor-widening', predecessor_widening_unit),
          ('pairing-predecessor', pairing_predecessor_controls),
          ('pairing-review-order', pairing_review_order_control), ('r13-form', r13_form_controls),
          ('read-domain', read_domain_controls)]


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
