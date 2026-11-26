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

    def stage(self, label, items, **facts):
        self.rec.capture_doc('engine control stage: %s (controls_engine.py)' % label,
                             control_records.stage_doc(items, operation=label, **facts))


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    rec = control_records.Recorder(JOB, out_dir)
    cap = Capture(rec)
    ce.CAPTURE = cap
    try:
        results = ce.run(None)
    finally:
        ce.CAPTURE = None
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
