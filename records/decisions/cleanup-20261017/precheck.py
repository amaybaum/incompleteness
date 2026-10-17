"""Read-only pre-deletion checks for the Tier 1 targets. Prints one block per target; deletes nothing."""
import os, subprocess, sys, json
S = sys.argv[1]
targets = [l.strip() for l in open(os.path.join(S, 'cleanup-20261017/targets.txt')) if l.strip()]
env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
def git(repo, *a):
    p = subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, env=env)
    return p.returncode, p.stdout.strip()
def inside(p, t):
    p, t = os.path.realpath(p), os.path.realpath(t)
    return p == t or p.startswith(t + os.sep)
# 1. processes whose cwd, root, exe or open files lie inside a target
procs = {t: [] for t in targets}
for pid in filter(str.isdigit, os.listdir('/proc')):
    paths = []
    for l in ('cwd', 'root', 'exe'):
        try: paths.append(os.readlink('/proc/%s/%s' % (pid, l)))
        except OSError: pass
    try:
        for fd in os.listdir('/proc/%s/fd' % pid):
            try: paths.append(os.readlink('/proc/%s/fd/%s' % (pid, fd)))
            except OSError: pass
    except OSError: pass
    for t in targets:
        if any(inside(p, t) for p in paths if p.startswith('/')):
            procs[t].append(pid)
# 2. alternates anywhere (scratchpad repos and the main clone) that point into a target
alt_users = {t: [] for t in targets}
roots = [S, '/home/user/incompleteness']
for root in roots:
    for dp, dns, fns in os.walk(root):
        if dp.endswith(os.path.join('objects', 'info')) and 'alternates' in fns:
            owner = dp[:-len('/objects/info')]
            for line in open(os.path.join(dp, 'alternates')):
                a = line.strip()
                if not a or a.startswith('#'):
                    continue
                a = a if os.path.isabs(a) else os.path.normpath(os.path.join(dp, '..', a))
                for t in targets:
                    if inside(a, t) and not inside(owner, t):
                        alt_users[t].append(owner)
        dns[:] = [d for d in dns if d != 'node_modules']
# 3. registered worktrees of the main clone that lie inside a target
_, wl = git('/home/user/incompleteness', 'worktree', 'list', '--porcelain')
wts = [l.split(' ', 1)[1] for l in wl.splitlines() if l.startswith('worktree ')]
for t in targets:
    print('== %s' % t[len(S) + 1:])
    print('   exists: %s' % os.path.isdir(t))
    print('   bytes: %s' % subprocess.run(['du', '-sb', t], capture_output=True, text=True).stdout.split('\t')[0])
    print('   processes using it: %s' % (procs[t] or 'none'))
    print('   kept repos borrowing its objects: %s' % (alt_users[t] or 'none'))
    print('   main-clone worktrees inside it: %s' % ([w for w in wts if inside(w, t)] or 'none'))
    repos = []
    for dp, dns, fns in os.walk(t):
        if os.path.isdir(os.path.join(dp, '.git')) or (os.path.isfile(os.path.join(dp, 'HEAD')) and os.path.isdir(os.path.join(dp, 'objects'))):
            repos.append(dp)
        if os.path.isfile(os.path.join(dp, '.git')):
            repos.append(dp)
        dns[:] = [d for d in dns if d not in ('.git', 'objects')]
    for r in repos:
        rc, wt_list = git(r, 'worktree', 'list', '--porcelain')
        others = [l.split(' ', 1)[1] for l in wt_list.splitlines() if l.startswith('worktree ')]
        ext = [w for w in others if not inside(w, t)]
        _, dirty = git(r, 'status', '--porcelain', '--untracked-files=no') if not r.endswith('.git') else (0, '')
        _, refs = git(r, 'for-each-ref', '--format=%(objectname) %(refname)')
        unique = []
        for line in refs.splitlines():
            sha, ref = line.split(' ', 1)
            rc2, typ = git('/home/user/incompleteness', 'cat-file', '-t', sha)
            if rc2 != 0:
                unique.append(ref + ' ' + sha[:12])
        rc3, head = git(r, 'rev-parse', 'HEAD')
        head_unique = rc3 == 0 and git('/home/user/incompleteness', 'cat-file', '-t', head)[0] != 0
        print('   repo %s: external worktrees %s; modified files %d; refs %d, refs whose object the main clone lacks %d%s; HEAD %s%s' % (
            r[len(t):] or '.', ext or 'none', len(dirty.splitlines()), len(refs.splitlines()), len(unique),
            (' ' + str(unique[:6])) if unique else '', head[:12] if rc3 == 0 else 'none', ' (HEAD object absent from the main clone)' if head_unique else ''))
