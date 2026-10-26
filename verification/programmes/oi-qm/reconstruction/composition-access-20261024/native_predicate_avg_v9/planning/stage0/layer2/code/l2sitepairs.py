"""NP-AVG-1 Stage 0 Layer 2: the site-pair count, a count-only diagnostic (r5).

Usage: python3 -I -B l2sitepairs.py --profile P --out FILE [--authorization FILE --owner-check FILE]

Status. The owner conditionally approved this count on v8's index space (2026-10-26) as a separate,
strictly count-only diagnostic, after independent review of this exact implementation, and has not
authorized its dispatch. Until the owner names this module's digest and commit in an authorization
of its own scope, the v8 profile is refused before anything is counted; every other profile runs
without one. The shard planner (l2plan) uses this module for every non-v8 profile and, on v8, reads
only a count file this module wrote.

The algorithm (published before dispatch, as the owner requires). It reads the profile's dim, rho,
tlast and port, and nothing else.
- region: the sites x in Z^dim with |x|_1 <= rho, in lexicographic order (site index i);
  slices: -1 .. tlast, nt of them; the record index space is the singles (site, slice) in site
  order, then the pairs i < j in lexicographic order, each with its nt x nt slice pairs.
- group: the signed coordinate permutations that map the region onto itself and fix the port and the
  two axis points (0, .., 0, -1) and (0, .., 0, 1) (C4v for dim 3 with the port on the last axis).
- a single site i: nt records; nt representatives if i is the least site of its group orbit, else 0.
- a site pair i < j: nt^2 records ((i, t1), (j, t2)), each compared with its images under the group
  in the record order (first site, its slice, second site, its slice). For an element with images
  (a, b) of (i, j):
    min(a, b) < i: every image precedes its record: 0 representatives;
    min(a, b) > i, or (a, b) = (i, j): no constraint;
    a = i, b < j: every image precedes: 0;   a = i, b > j: no constraint;
    b = i (the element carries j to i): the image is (i, t2, a, t1), which precedes the record iff
      t2 < t1, or t2 = t1 and a < j: so a representative needs t1 <= t2 if a >= j, and t1 < t2 if
      a < j.
  The pair's count is 0, nt^2, nt(nt + 1)/2 (t1 <= t2) or nt(nt - 1)/2 (t1 < t2), the strictest
  constraint over the group deciding; the four values are distinct for nt >= 2.
- totals: N, the records, and R, the representatives. R must equal Burnside's orbit count, computed
  independently from fixed points; the count fails closed (VOID, nothing written) if it does not.
No record, slice pair or (site, slice) item is ever formed: the loop runs over site indices and
group images only.

Permitted outputs, exactly (validated before the file is written): the schema, the profile name, the
setup's (dim, rho, tlast, port), nt, the number of sites and of site pairs, the per-site and
per-site-pair representative counts (integer lists in index order), the totals N and R, Burnside's
orbit count, this module's SHA-256, and the authorization decision string. Nothing else is written
or printed.

Guards (the owner's restrictions):
- imports: the standard library modules named in ALLOWED_IMPORTS and l2config; no engine, reference,
  analysis or run module (checked statically by l2selftest L2-COUNTONLY, and at run time: none is
  loaded at start, none is loaded at the end, and any import after the guard starts is refused);
- data flow: after the authorization step a runtime audit hook refuses every file open except the
  single write of the output file, every import, every process launch and every network call, and
  standard output and error are replaced by streams that refuse writes; the only output is the
  validated object (or a VOID object naming a fixed reason);
- resources: RLIMIT_CPU and RLIMIT_AS are set to RESOURCE_LIMIT before counting (the count on v8's
  region, 129 sites, is about 8,300 site pairs times 8 group elements: well under a second).
"""
import hashlib
import json
import os
import sys
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import l2config as CFG  # noqa: E402

SCHEMA = 'np-avg-1/stage0/layer2/site-pair-count/1'
AUTH_SCHEMA = 'np-avg-1/stage0/v8-site-pair-count-authorization/1'
OWNER_SCHEMA = 'np-avg-1/stage0/v8-site-pair-count-owner-check/1'
AUTH_SCOPE = 'NP-AVG-1 Stage 0, the count-only site-pair count on v8\'s index space (l2sitepairs.py), nothing else'
OWNER = 'amaybaum'
REPO_URL = 'https://github.com/amaybaum/incompleteness/'
AUTH_KEYS = {'schema', 'scope', 'commit', 'module_sha256', 'owner', 'designation_url', 'designated_at'}
OWN_KEYS = {'schema', 'comment_url', 'author_login', 'commit', 'body_contains_required_line'}
V8_KEY = (3, 6, (0, 0, -3))
ALLOWED_IMPORTS = {'hashlib', 'json', 'os', 'sys', 'resource', 'subprocess', 'itertools', 'l2config'}
FORBIDDEN_MODULES = ('s0geom', 's0ref', 's0native', 's0controls', 's0s6', 's0symcheck', 'l2analysis', 'l2enum',
                     'l2refcheck', 'l2s1a', 'l2merge', 'l2preflight', 'l2calib', 'l2cert', 'l2auth', 'l2landing',
                     'l2plan', 'l2mutants', 'l2run', 'l2selftest')
RESOURCE_LIMIT = {'cpu_seconds': 60, 'address_space_bytes': 1 << 30, 'job_timeout_minutes': 5}
OUT_KEYS = {'schema', 'profile', 'setup', 'nt', 'sites', 'site_pairs', 'singles_representatives',
            'pairs_representatives', 'records_total', 'representatives_total', 'burnside_orbits', 'module_sha256',
            'authorization'}


def required_line(commit, module_sha256):
    return 'NP-AVG-1 Stage 0 v8 site-pair count authorized at %s module_sha256 %s' % (commit, module_sha256)


def module_sha256():
    with open(os.path.abspath(__file__), 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def _hex(s, n):
    return type(s) is str and len(s) == n and all(c in '0123456789abcdef' for c in s)


def decide(art, own, facts):
    """'ok' or 'refused: <reason>' for the v8 profile; a pure function of the artifact, the owner check
    and the checkout's facts (head_commit, tree_clean, module_sha256)."""
    if art is None:
        return 'refused: no authorization for the v8 site-pair count (default)'
    if type(art) is not dict or set(art) != AUTH_KEYS or art['schema'] != AUTH_SCHEMA:
        return 'refused: artifact fields'
    if art['scope'] != AUTH_SCOPE:
        return 'refused: scope'
    if not _hex(art['commit'], 40) or art['commit'] != facts.get('head_commit'):
        return 'refused: commit is not the checked-out HEAD'
    if facts.get('tree_clean') is not True:
        return 'refused: Layer-2 directory differs from HEAD'
    if art['module_sha256'] != facts.get('module_sha256'):
        return 'refused: module digest differs'
    if art['owner'] != OWNER or type(art['designation_url']) is not str or \
            not art['designation_url'].startswith(REPO_URL):
        return 'refused: owner or designation URL'
    if own is None:
        return 'refused: no owner check'
    if type(own) is not dict or set(own) != OWN_KEYS or own['schema'] != OWNER_SCHEMA:
        return 'refused: owner-check fields'
    if own['comment_url'] != art['designation_url'] or own['author_login'] != OWNER or \
            own['commit'] != art['commit'] or own['body_contains_required_line'] is not True:
        return 'refused: owner check'
    return 'ok'


def _facts():
    import subprocess

    def git(*a):
        p = subprocess.run(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-C', HERE] + list(a),
                           capture_output=True, text=True)
        return p.returncode, p.stdout.strip()
    rc, head = git('rev-parse', 'HEAD')
    rc2, st = git('status', '--porcelain', '--untracked-files=all', '--', os.path.dirname(HERE))
    return {'head_commit': head if rc == 0 else None, 'tree_clean': rc2 == 0 and st == '',
            'module_sha256': module_sha256()}


def _load(path):
    if not path:
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {'unreadable': True}


# -- the count ----------------------------------------------------------------------------------

def region(dim, rho):
    return sorted(c for c in product(range(-rho, rho + 1), repeat=dim) if sum(abs(v) for v in c) <= rho)


def group_perms(dim, rho, port):
    """The group as permutations of site indices (one list per element, identity included)."""
    reg = region(dim, rho)
    idx = {c: i for i, c in enumerate(reg)}
    fixed = [tuple(port), tuple(-1 if j == dim - 1 else 0 for j in range(dim)),
             tuple(1 if j == dim - 1 else 0 for j in range(dim))]
    out = []
    for pp in permutations(range(dim)):
        for ss in product((1, -1), repeat=dim):
            def a(c):
                return tuple(ss[i]*c[pp[i]] for i in range(dim))
            img = [a(c) for c in reg]
            if all(x in idx for x in img) and all(a(f) == f for f in fixed):
                out.append([idx[x] for x in img])
    return out


def count(setup):
    """The permitted output's counts for setup = {'dim', 'rho', 'tlast', 'port'} (see the docstring)."""
    dim, rho, tlast, port = setup['dim'], setup['rho'], setup['tlast'], setup['port']
    nt = tlast + 2
    ns = len(region(dim, rho))
    perms = group_perms(dim, rho, port)
    singles = [nt if min(p[i] for p in perms) == i else 0 for i in range(ns)]
    pairs = []
    for i in range(ns):
        for j in range(i + 1, ns):
            least, le, lt = True, False, False
            for p in perms:
                a, b = p[i], p[j]
                if min(a, b) < i or (a == i and b < j):
                    least = False
                    break
                if b == i:
                    if a < j:
                        lt = True
                    else:
                        le = True
            pairs.append(0 if not least else nt*(nt - 1)//2 if lt else nt*(nt + 1)//2 if le else nt*nt)
    # Burnside, independently: fixed singles and fixed unordered pairs-with-slices per element
    fix = 0
    for p in perms:
        nf = sum(1 for i in range(ns) if p[i] == i)
        sw = sum(1 for i in range(ns) if p[i] != i and p[p[i]] == i)//2
        fix += nf*nt + (nf*(nf - 1)//2)*nt*nt + sw*nt
    burnside = fix//len(perms)
    return {'nt': nt, 'sites': ns, 'site_pairs': ns*(ns - 1)//2, 'singles_representatives': singles,
            'pairs_representatives': pairs, 'records_total': ns*nt + (ns*(ns - 1)//2)*nt*nt,
            'representatives_total': sum(singles) + sum(pairs), 'burnside_orbits': burnside}


def validate(out, setup):
    """True iff out carries exactly the permitted outputs, each of its permitted type and size."""
    if type(out) is not dict or set(out) != OUT_KEYS or out['schema'] != SCHEMA:
        return False
    ints = ('nt', 'sites', 'site_pairs', 'records_total', 'representatives_total', 'burnside_orbits')
    if any(type(out[k]) is not int for k in ints):
        return False
    if type(out['profile']) is not str or type(out['authorization']) is not str or not _hex(out['module_sha256'], 64):
        return False
    if out['setup'] != {'dim': setup['dim'], 'rho': setup['rho'], 'tlast': setup['tlast'], 'port': list(setup['port'])}:
        return False
    s, p = out['singles_representatives'], out['pairs_representatives']
    if type(s) is not list or type(p) is not list or len(s) != out['sites'] or len(p) != out['site_pairs']:
        return False
    if any(type(v) is not int for v in s + p):
        return False
    return out['representatives_total'] == sum(s) + sum(p) == out['burnside_orbits']


# -- the guard ----------------------------------------------------------------------------------

class GuardViolation(Exception):
    pass


class _Sealed:
    """A stream that refuses every write while the guard is active."""
    def __init__(self, real, state):
        self.real, self.state = real, state

    def write(self, s):
        if not self.state['emit']:
            raise GuardViolation('write to a standard stream')
        return self.real.write(s)

    def flush(self):
        return self.real.flush()


def _install_guard(out_path, state):
    target = os.path.abspath(out_path)

    def hook(event, args):
        if not state['on']:
            return
        if event == 'open':
            path, mode = args[0], args[1]
            ok = (isinstance(path, str) and os.path.abspath(path) == target and isinstance(mode, str) and 'w' in mode
                  and state['emit'] and not state['written'])
            if not ok:
                raise GuardViolation('file open refused')
            state['written'] = True
        elif event == 'import':
            raise GuardViolation('import refused')
        elif event.startswith(('subprocess.', 'os.system', 'os.exec', 'os.spawn', 'os.posix_spawn', 'os.fork',
                               'socket.', 'ctypes.', 'os.remove', 'os.rename', 'os.unlink', 'shutil.')):
            raise GuardViolation('%s refused' % event.split('.')[0])
    sys.addaudithook(hook)
    sys.stdout = _Sealed(sys.stdout, state)
    sys.stderr = _Sealed(sys.stderr, state)


def _emit(state, obj, out_path=None):
    state['emit'] = True
    text = json.dumps(obj, sort_keys=True)
    if out_path is not None:
        with open(out_path, 'w') as f:
            f.write(text + '\n')
    sys.stdout.write(text + '\n')
    sys.stdout.flush()


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    pname = args[args.index('--profile') + 1]
    out_path = args[args.index('--out') + 1]
    prof = CFG.profile(pname)
    st = prof['setup']
    setup = {'dim': st['dim'], 'rho': st['rho'], 'tlast': st['tlast'], 'port': tuple(st['port'])}
    loaded = [m for m in FORBIDDEN_MODULES if m in sys.modules]
    if loaded:
        print(json.dumps({'label': 'VOID', 'reason': 'a forbidden module is loaded at start: %s' % loaded}))
        return 2
    decision = 'not required (not v8)'
    if (st['dim'], st['n'], tuple(st['port'])) == V8_KEY:
        art = _load(args[args.index('--authorization') + 1]) if '--authorization' in args else None
        own = _load(args[args.index('--owner-check') + 1]) if '--owner-check' in args else None
        decision = decide(art, own, _facts() if art is not None else {})
        if decision != 'ok':
            print(json.dumps({'label': 'VOID', 'refused': 'v8 site-pair count', 'reason': decision}))
            return 2
    digest = module_sha256()
    try:
        import resource
        resource.setrlimit(resource.RLIMIT_CPU, (RESOURCE_LIMIT['cpu_seconds'], RESOURCE_LIMIT['cpu_seconds']))
        resource.setrlimit(resource.RLIMIT_AS, (RESOURCE_LIMIT['address_space_bytes'],
                                                RESOURCE_LIMIT['address_space_bytes']))
    except (ImportError, ValueError, OSError):
        print(json.dumps({'label': 'VOID', 'reason': 'resource limit could not be set'}))
        return 2
    state = {'on': True, 'emit': False, 'written': False}
    _install_guard(out_path, state)
    try:
        c = count(setup)
        out = dict(c, schema=SCHEMA, profile=pname, module_sha256=digest, authorization=decision,
                   setup={'dim': setup['dim'], 'rho': setup['rho'], 'tlast': setup['tlast'],
                          'port': list(setup['port'])})
        reason = None
        if not validate(out, setup):
            reason = 'output is not exactly the permitted outputs, or R differs from Burnside'
        elif [m for m in FORBIDDEN_MODULES if m in sys.modules]:
            reason = 'a forbidden module was loaded during the count'
    except GuardViolation as e:
        reason = 'guard: %s' % e
    except Exception as e:  # noqa: BLE001 (the message could carry data: only the class is reported)
        reason = 'error: %s' % type(e).__name__
    if reason is not None:
        _emit(state, {'label': 'VOID', 'reason': reason})
        return 2
    _emit(state, out, out_path)
    return 0


if __name__ == '__main__':
    sys.exit(main())
