"""Reviewer probe: run ci/calib_ci.py under an audit hook; record every file opened and every
module imported. Usage: python3 -I -B calib_audit.py <layer2/ci/calib_ci.py> <out.json>"""
import sys, runpy, json, os
opened, imported = set(), set()
def hook(ev, args):
    if ev == 'open' and isinstance(args[0], str):
        opened.add(os.path.abspath(args[0]))
    elif ev == 'import':
        imported.add(args[0])
sys.addaudithook(hook)
script, out = sys.argv[1], sys.argv[2]
sys.argv = [script, '--out', out, '--sets', '1', '--index', '0']
code = 0
try:
    runpy.run_path(script, run_name='__main__')
except SystemExit as e:
    code = e.code
print(json.dumps({'exit': code,
                  'opened_nonstdlib': sorted(f for f in opened if '/python3' not in f and '/lib/python' not in f),
                  'imported_nonstdlib_suspects': sorted(m for m in imported if m.split('.')[0] in
                      ('s0geom','s0ref','s0native','s0controls','l2refcheck','l2config','l2plan','l2enum','l2auth',
                       'l2cert','l2calib','l2s1a','l2merge','l2preflight','l2analysis','l2run','l2selftest'))}, indent=1), file=sys.stderr)
