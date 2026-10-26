"""NP-AVG-1 Stage 0 Layer 2: one planted-set timing calibration for the CI runner class (PROPOSAL;
the owner authorized, conditionally, "a separate, planted-set-only CI timing calibration, provided
it cannot access v8 and its exact workflow and resource limits are reviewed before dispatch").

It cannot construct a v8 setup, by construction:
- it imports no Layer-2 module and no engine module. From ../code/s0geom.py, ../code/s0ref.py and
  ../code/l2refcheck.py it reads the source, checks each file's SHA-256 against
  ../code/LAYER2-MANIFEST.json, and executes only the named geometry and closure definitions
  (ENGINE, REFERENCE, CACHED below), so Setup, V8, Context, record_at, num_records,
  record_samples, ref_context and the grants never exist in this process;
- before timing, it fails closed if any forbidden name is present in the extracted namespaces or
  any Layer-2 or engine module is imported;
- after timing, it scans the interpreter's objects and fails closed if any object is a Setup,
  Context or grant, or carries v8's (dim, n, port) = (3, 6, (0, 0, -3)).
A failure prints {"label": "VOID", ...}, writes no output file and exits 2.

The procedure is l2calib.py's (whose SHA-256 is also checked): planted quantity sets of sizes
8-40, 12 sets per size, seed 20261026, ball(4) displaced to (40, 0, 0), slices -1..23, pairs
(7, 8) and (-1, 0), the eleven-quantity planted frame; timings only, no retained set. Locally,
--check-equivalence (not used in CI) imports the real engine and confirms that the extracted
closure returns the engine's closure on every planted set; --tripwire-selftest plants a v8-keyed
object and must exit 2.

Usage: python3 -I -B calib_ci.py --out FILE [--index I] [--sets 12]
"""
import ast
import gc
import hashlib
import json
import os
import platform
import random
import sys
import time
import types

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, '..', 'code'))
ENGINE = ('axes', 'vadd', 'l1', 'lball', 'Rule', 'FROZEN', 'Pair', '_slices', 'in_cone', 'tip_labels', 'tips',
          'closure')
REFERENCE = ('unit', 'shift', 'cells_within', 'RefGeometry', 'self_supporting', 'greatest')
CACHED = ('CachedGeo',)
FORBIDDEN = {'Setup', 'V8', 'V8_PARAMS', 'V8Grant', 'RefGrant', 'Context', 'record_at', 'num_records',
             'record_samples', 'ref_context', 'ref_retained', '_guard', 'bind_running_digests', 'analyse'}
FORBIDDEN_MODULES = ('s0geom', 's0ref', 's0native', 's0controls', 'l2refcheck', 'l2config', 'l2plan', 'l2enum',
                     'l2auth', 'l2cert', 'l2calib', 'l2s1a', 'l2merge', 'l2preflight', 'l2analysis')
V8_KEY = (3, 6, (0, 0, -3))
SIZES = (8, 12, 16, 20, 24, 28, 32, 36, 40)


def void(reason):
    print(json.dumps({'label': 'VOID', 'reason': reason}, sort_keys=True))
    sys.exit(2)


def manifest_sha(fn):
    with open(os.path.join(CODE, 'LAYER2-MANIFEST.json')) as f:
        return json.load(f)['files'][fn]


def extract(fn, names, extra_ns=None):
    """Execute only the top-level definitions of names from fn (hash-checked), in a fresh namespace."""
    path = os.path.join(CODE, fn)
    with open(path, 'rb') as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != manifest_sha(fn):
        void('%s differs from LAYER2-MANIFEST.json' % fn)
    tree = ast.parse(raw.decode())
    keep = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
            keep.append(node)
        elif isinstance(node, ast.Assign) and all(isinstance(t, ast.Name) and t.id in names for t in node.targets):
            keep.append(node)
        elif isinstance(node, ast.ImportFrom) and node.module == 'itertools':
            keep.append(node)
    found = {n.name if not isinstance(n, (ast.Assign, ast.ImportFrom)) else
             (n.targets[0].id if isinstance(n, ast.Assign) else None) for n in keep} - {None}
    if found != set(names):
        void('%s: definitions not found: %s' % (fn, sorted(set(names) - found)))
    ns = {'__name__': 'calib_' + fn.split('.')[0]}
    ns.update(extra_ns or {})
    exec(compile(ast.Module(body=keep, type_ignores=[]), fn, 'exec'), ns)
    return ns


def tripwire(namespaces):
    bad = [m for m in FORBIDDEN_MODULES if m in sys.modules]
    for ns in namespaces:
        bad += sorted(FORBIDDEN & set(ns))
    for o in gc.get_objects():
        cls = type(o).__name__
        if cls in ('Setup', 'Context', 'V8Grant', 'RefGrant'):
            bad.append('object of type %s' % cls)
        elif isinstance(o, types.SimpleNamespace) or hasattr(o, '__dict__'):
            try:
                d = vars(o)
            except TypeError:
                continue
            port = d.get('port')
            if d.get('dim') == 3 and d.get('n') == 6 and port is not None and tuple(port) == (0, 0, -3):
                bad.append('object carrying v8\'s (dim, n, port)')
    if bad:
        void('tripwire: %s' % sorted(set(bad))[:5])


def main():
    args = sys.argv[1:]
    nsets = int(args[args.index('--sets') + 1]) if '--sets' in args else 12
    out_path = args[args.index('--out') + 1]
    with open(os.path.join(CODE, 'l2calib.py'), 'rb') as f:
        if hashlib.sha256(f.read()).hexdigest() != manifest_sha('l2calib.py'):
            void('l2calib.py differs from LAYER2-MANIFEST.json')
    Gns = extract('s0geom.py', ENGINE)
    Rns = extract('s0ref.py', REFERENCE)
    Cns = extract('l2refcheck.py', CACHED, {'REF': types.SimpleNamespace(RefGeometry=Rns['RefGeometry'])})
    G, REF = types.SimpleNamespace(**Gns), types.SimpleNamespace(**Rns)
    if '--tripwire-selftest' in args:
        class Setup:                      # noqa: D401  a planted v8-keyed object: the tripwire must fire
            def __init__(self):
                self.dim, self.n, self.port = V8_KEY[0], V8_KEY[1], V8_KEY[2]
        planted = Setup()                 # noqa: F841
    tripwire((Gns, Rns, Cns))
    rng = random.Random(20261026)
    centre = (40, 0, 0)
    pA, pG = G.Pair(7), G.Pair(-1)
    toy_frame = [(G.vadd(centre, e), 3) for e in G.axes(3)] + [(centre, 4), (centre, 2)] + \
        [(G.vadd(centre, (0, 0, -2)), s) for s in (0, 1, 2)]
    memo = {}

    def elig(u):
        v = memo.get(u)
        if v is None:
            v = memo[u] = not any(G.in_cone(u, f, pG) for f in toy_frame)
        return v
    pool = [(G.vadd(centre, c), t) for c in G.lball(4, 3) for t in range(-1, 24) if (G.l1(c) + t) % 2 == 0]
    out = {'schema': 'np-avg-1/stage0/layer2/ci-calib/1', 'python': sys.version.split()[0], 'sets_per_size': nsets,
           'closure_ns_A': {}, 'closure_ns_G': {}, 'ref_c7_ns_A': {}, 'ref_c7_ns_G': {}, 'deterministic': False,
           'index': args[args.index('--index') + 1] if '--index' in args else None,
           'runner': {'platform': platform.platform(), 'cpu_count': os.cpu_count(),
                      'RUNNER_OS': os.environ.get('RUNNER_OS'), 'RUNNER_ARCH': os.environ.get('RUNNER_ARCH'),
                      'ImageOS': os.environ.get('ImageOS'), 'ImageVersion': os.environ.get('ImageVersion')},
           'procedure': 'l2calib.py, transcribed; engine definitions executed from hash-checked sources'}
    check = '--check-equivalence' in args
    if check:
        sys.path.insert(0, CODE)
        import s0geom as REAL     # local check only; never in CI
    mism = 0
    for m in SIZES:
        sets = [set(rng.sample(pool, m)) for _ in range(nsets)]
        for conv, pair, el in (('A', pA, None), ('G', pG, elig)):
            t0 = time.perf_counter_ns()
            for S_ in sets:
                ret, _ = G.closure(set(), S_, pair, 3, G.FROZEN, el)
                if check:
                    rr, _ = REAL.closure(set(), S_, REAL.Pair(pair.E), 3, REAL.FROZEN, el)
                    mism += set(rr) != set(ret)
            out['closure_ns_%s' % conv][str(m)] = (time.perf_counter_ns() - t0)//nsets
            refel = (lambda u: True) if el is None else el
            t0 = time.perf_counter_ns()
            for S_ in sets[:3]:
                REF.greatest(set(), S_, Cns['CachedGeo'](3, pair.E), refel, 8)
            out['ref_c7_ns_%s' % conv][str(m)] = (time.perf_counter_ns() - t0)//3
    if check:
        out['equivalence_with_engine'] = {'mismatches': mism}
    else:
        tripwire((Gns, Rns, Cns))
    with open(out_path, 'w') as f:
        f.write(json.dumps(out, indent=1, sort_keys=True) + '\n')
    print(json.dumps({'written': os.path.basename(out_path), 'pass': not mism}, sort_keys=True))
    sys.exit(0 if not mism else 2)


if __name__ == '__main__':
    main()
