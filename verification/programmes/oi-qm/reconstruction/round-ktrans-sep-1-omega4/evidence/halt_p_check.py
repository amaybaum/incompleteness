"""Builds evidence/halt-control-p.json for the KTRANS-SEP-1 halt: the frozen control P's sub-check for F's run,
evaluated with the frozen controls.py on the record's own files. Run from the repository root at the halt commit; its stdout is the file."""
import importlib.util, json, hashlib, sys
R = 'verification/programmes/oi-qm/reconstruction/round-ktrans-sep-1-omega4/'
F = '7e9aef691f47edaec9111ef5923ed9e946854737'
spec = importlib.util.spec_from_file_location('ctl', R + 'controls.py')
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
read = lambda p: open(R + p, encoding='utf-8').read()
fr, pt, pre = read('evidence/f-run/results.json'), read('evidence/predicted-tree-run.json'), read('preregistration.md')
ph = c.predicted_head(pre)
sha = lambda p: hashlib.sha256(open(R + p, 'rb').read()).hexdigest()
w = json.loads(fr)['observed']['transseparation_window']
out = {
 'schema': 'oi-evidence-result', 'version': 1, 'form': 'complete',
 'kind': 'halt control: the frozen control P for F\'s exact-head run',
 'recipe': 'from the repository root at the halt commit: python3 -I -B ' + R + 'evidence/halt_p_check.py > ' + R + 'evidence/halt-control-p.json; it loads the round\'s controls.py '
           '(blob 412802eb11e74200734e4ae6511dcbef4d76613e) and calls its run_window_ok, the function behind P\'s line '
           '"F\'s exact-head run is retained, names F, is green on every job and places the module\'s build line, '
           'reports and gate inside its served window"',
 'inputs': {'controls.py': sha('controls.py'), 'evidence/f-run/results.json': sha('evidence/f-run/results.json'),
            'evidence/predicted-tree-run.json': sha('evidence/predicted-tree-run.json'),
            'preregistration.md': sha('preregistration.md')},
 'f': F, 'predicted_head': ph,
 'results': [
  {'case': 'the failing control: F\'s run result against F', 'run_window_ok': c.run_window_ok(fr, F),
   'reason': 'F is D plus the preregistration, so its run builds no OIBridge.TransSeparation; the result\'s '
             'observed.transseparation_window records no build line, no report and no gate block', 'window': w},
  {'case': 'positive control: the predicted tree\'s run against the predicted tree', 'run_window_ok': c.run_window_ok(pt, ph)},
  {'case': 'head control: the predicted tree\'s run against F', 'run_window_ok': c.run_window_ok(pt, F)},
 ],
 'evidence_ok_f_run': bool(c.evidence_ok(fr)),
}
ok = out['results'][0]['run_window_ok'] is False and out['results'][1]['run_window_ok'] is True and \
     out['results'][2]['run_window_ok'] is False and out['evidence_ok_f_run']
if not ok:
    sys.exit('halt control: unexpected results %r' % [r['run_window_ok'] for r in out['results']])
sys.stdout.write(json.dumps(out, indent=1, ensure_ascii=False) + '\n')
