"""Records of the engine controls (the self-test's controls of engine/controls_engine.py) for the gate (design r6,
R6.GATE.5 and R6.GATE.7).

It runs every engine control exactly as `ledger_coverage.py self-test` does, with the engine's capture hook set:
each in-process stage result the controls compute (coverage, execution and terms items, with sites and side
changes) is retained as a result document whose outcome and exit status the tool's own outcome function gives,
and bound to the control assigned next. It writes `control-records.json` (oi-control-records/1) and
`evidence/engine-self-test/<id>/` into DIR. A group that raises is one FAIL record, `<group>-group-error`.

Usage: python3 -I -S -B tools/ledger_coverage/adapters/engine_controls.py DIR
"""
import json
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
if 'ledger_coverage' not in sys.modules:
    # the package is loaded by its location, as the entry point loads it; no directory is put on sys.path
    import importlib.util
    _pkg = os.path.dirname(here)
    _spec = importlib.util.spec_from_file_location('ledger_coverage', os.path.join(_pkg, '__init__.py'),
                                                   submodule_search_locations=[_pkg])
    sys.modules['ledger_coverage'] = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(sys.modules['ledger_coverage'])

from ledger_coverage.engine import controls_engine as ce  # noqa: E402
from ledger_coverage.adapters import control_records  # noqa: E402

JOB = 'engine-self-test'


class Capture(object):
    def __init__(self, rec):
        self.rec = rec
        self.runs_of = {}

    def result_map(self):
        return control_records.RunMap(self.rec, self.runs_of)

    def name_last(self, case, bindings, baseline=None):
        """Names the last stage result; `baseline` names an earlier case of the same control whose result a
        restored case is compared with."""
        base = None
        if baseline is not None:
            base = next((r for r in self.rec.pending if r['case'] == baseline), None)
        self.rec.name_last(case, bindings=dict(bindings), baseline=base)

    def attest(self, case, values):
        """Values the runner states for a named case (checked by the gate for integrity only)."""
        run = next((r for r in self.rec.pending if r['case'] == case), None)
        if run is not None and values:
            run['attested'] = dict(run.get('attested') or {}, **values)

    def count(self):
        return len(self.rec.pending)

    def bind_first(self, bindings):
        run = next((r for r in self.rec.pending if r['case'] is None), None)
        if run is not None:
            run['case'], run['bindings'] = '', dict(bindings)

    def stage(self, label, items, **facts):
        self.rec.capture_doc('engine control stage: %s (controls_engine.py)' % label,
                             control_records.stage_doc(items, operation=label, **facts))


def extra_controls(cap):
    """Rows whose runner is this adapter rather than the self-test: RECLINT-ORPHAN (R6.REC.10) and
    PIPE-UNRESOLVED (R6.PIPE.7), on the engine's neutral in-memory trees."""
    out = cap.result_map()
    ce.capture_hook = cap
    try:
        # RECLINT-ORPHAN: an HP adjudication entry naming a site_id that no tracked site carries
        w, h, sg = ce.hp_world()
        sid = '%s:%d@%s' % (ce.doc_path, 5, w.pin[:8])
        steps = ce.walk_steps(w, h, sg, 5)
        good = {'site_id': sid, 'steps': steps, 'carried': {'row': 'row-x', 'code': 'code-x', 'owner': 'owner-x'},
                'semantic_classification': 'stated', 'author': 'eng-writer'}
        orphan_id = '%s:%d@%s' % (ce.doc_path, 99, w.pin[:8])
        orphan = dict(good, site_id=orphan_id)
        cv, it = w.coverage(h, [sg], adj={'hp': [good, orphan]}, hits=False)
        ce._case('an HP adjudication record entry that, on a tree and in a segment to which the record applies, '
                 'matches no subject (orphan)', entry=orphan_id)
        c1 = any(i['class'] == 'stale-adjudication' and i['obligation'] == 'HP' and i['subject'] == orphan_id
                 for i in it)
        cv, it2 = w.coverage(h, [sg], adj={'hp': [good]}, hits=False)
        ce._case('the record without the orphan and duplicate entries (positive)')
        c5 = not [i for i in it2 if i['class'] in ('stale-adjudication', 'record-invalid')]
        # the context and hit classification orphans, the duplicate and the out-of-scope cases are not run here
        out['RECLINT-ORPHAN'] = False
        out['_RECLINT-ORPHAN'] = {'hp_orphan': c1, 'positive': c5,
                                  'not_run': ['context or hit classification orphan', 'duplicate', 'out of scope']}

        # PIPE-UNRESOLVED: a site lost in the first of two segments is reported there only, its state unresolved
        w = ce.World()
        line = 'beta line two stands here.\n'
        x1 = w.child(w.pin, ce.base_text.replace(line, ''), subject='site removed')
        x2 = w.child(x1, files={ce.other_path: b'unrelated\n'}, subject='unrelated change')
        s1, s2 = ce.seg(w.pin, x1), ce.seg(x1, x2)
        cv, it = w.coverage(x2, [s1, s2], hits=False)
        site = '%s:5@%s' % (ce.doc_path, w.pin[:8])
        n1, n2 = '%s..%s' % (w.pin[:8], x1[:8]), '%s..%s' % (x1[:8], x2[:8])
        ce._case('', site=site, first_segment=n1, second_segment=n2)
        mine = [(i['class'], i['segment']) for i in it if i['subject'] == site]
        x2r = w.child(w.pin, files={ce.other_path: b'unrelated\n'}, subject='restored')
        w.coverage(x2r, [ce.seg(w.pin, x2r)], hits=False)
        ce._case('baseline')
        w.coverage(x2r, [ce.seg(w.pin, x2r)], hits=False)
        ce._case('restored', baseline='baseline')
        from ledger_coverage.engine.cli import site_state
        state = site_state(cv.site_out[site])
        out['PIPE-UNRESOLVED'] = mine == [('missing', n1)] and state == 'unresolved'
        out['_PIPE-UNRESOLVED'] = {'items': mine, 'state': state}
    finally:
        ce.capture_hook = None
    return out


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rec = control_records.Recorder(JOB, out_dir)
    cap = Capture(rec)
    ce.capture_hook = cap
    try:
        results = ce.run(None)
    finally:
        ce.capture_hook = None
    try:
        extra = extra_controls(cap)
    except Exception as exc:
        extra = {'extra-group-error': '%s: %s' % (type(exc).__name__, exc)}
    from ledger_coverage.adapters import recon_controls
    try:
        extra.update(recon_controls.recon_controls(cap))
    except Exception as exc:
        import traceback
        extra['recon-group-error'] = '%s: %s %s' % (type(exc).__name__, exc, traceback.format_exc()[-1200:])
    for cid, v in sorted(extra.items()):
        if cid.startswith('_'):
            continue
        rec.pending = cap.runs_of.get(cid, [])
        rec.record(cid, 'PASS' if v is True else 'FAIL', {'value': v, 'detail': extra.get('_' + cid)},
                   'the boolean computed for this id in adapters/engine_controls.py')
    for r in results:
        cid = r['id'] if 'error' not in r else '%s-group-error' % r['id']
        rec.pending = cap.runs_of.get(r['id'], []) if 'error' not in r else []
        rec.record(cid, 'PASS' if r['passed'] else 'FAIL', r.get('error', r['passed']),
                   'the boolean computed for this id in engine/controls_engine.py')
    rec.write()
    n = sum(1 for r in results if r['passed'])
    print(json.dumps({'controls': len(results), 'passed': n}))
    return 0 if n == len(results) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
