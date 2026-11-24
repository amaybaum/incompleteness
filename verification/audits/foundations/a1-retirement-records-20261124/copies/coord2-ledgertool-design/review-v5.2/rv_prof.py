"""Review profiles extracted from blobs (not retyped): p0-core/p0-para from Phase-0 sites.json at H,
ledger-ext from R/ledger_check.py at H via ast, PTR/REPO_PAT from P's edits_check.py via ast."""
import ast, re, json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g
P0 = g.load('sites.json')
def _ast_assign(src, name):
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return node.value
    raise KeyError(name)
_lc = open(os.path.join(g.DATA, 'ledger_check.py')).read()
EXT = ast.literal_eval(_ast_assign(_lc, 'EXTENDED_PATTERNS'))
PROFILES = {
  'p0-core': [re.compile(v) for v in P0['core_patterns'].values()],
  'p0-para': [re.compile(v) for v in P0['paraphrase_patterns'].values()],
  'ledger-ext': [re.compile(v) for v in EXT.values()],
  'count-grep': [re.compile(re.escape(x)) for x in ('Fourteen', 'six structural', 'sixth of')],
}
_ec = open(os.path.join(g.DATA, 'edits_check.py')).read()
def _regex_of(name):
    v = _ast_assign(_ec, name)
    if isinstance(v, ast.Call):
        args = v.args
        pat = ast.literal_eval(args[0])
        flags = 0
        if len(args) > 1:
            fl = ast.unparse(args[1])
            for f in ('I', 'IGNORECASE', 'M', 'S', 'X'):
                if 're.' + f in fl: flags |= getattr(re, f)
        return re.compile(pat, flags)
    return re.compile(ast.literal_eval(v))
for nm in ('PTR', 'REPO_PAT'):
    try:
        PROFILES[{'PTR': 'ptr', 'REPO_PAT': 'repo'}[nm]] = [_regex_of(nm)]
    except Exception as ex:
        print('profile extract fail', nm, ex)
def hits(line, names):
    return sorted(n for n in names if any(rx.search(line) for rx in PROFILES[n]))
P0EXT = ('p0-core', 'p0-para', 'ledger-ext')
