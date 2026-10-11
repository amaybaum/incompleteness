"""Descent of the origin thread's dev-origin/drive files across its commit chain.
Usage: python3 -I -B dev_descent.py <interruption-manifest> <dev-worktree> <checkpoint-worktree> <checkpoint-manifest-path> <commit>...
For each 'dev-origin-drive' row of the interruption manifest and each row of the checkpoint manifest, prints the digest of the
path's blob at each listed commit (ABSENT if missing) and marks the commits whose blob equals the recorded digest; then
checks the checkpoint copy's own blob against its recorded digest.
"""
import hashlib, subprocess, sys
man, wt, cwt, cman = sys.argv[1:5]
commits = sys.argv[5:]
def blob(w, ref, p):
    r = subprocess.run(['git', '-C', w, 'show', f'{ref}:{p}'], capture_output=True)
    return None if r.returncode else r.stdout
def dig(b):
    return 'ABSENT' if b is None else hashlib.sha256(b).hexdigest()
rows = []
for ln in open(man):
    if ln.startswith('#') or not ln.strip():
        continue
    h, st, mt, loc = ln.split()
    w, p = loc.split(':', 1)
    if w == 'dev-origin-drive':
        rows.append(('interruption', h, mt, p))
for ln in subprocess.run(['git', '-C', cwt, 'show', f'HEAD:{cman}'], capture_output=True, text=True, check=True).stdout.splitlines():
    if 'dev-origin-drive@' in ln:
        f = ln.split()
        rows.append(('checkpoint', f[0], f[1], f[-1]))
for src, h, mt, p in rows:
    hits = [c[:8] for c in commits if dig(blob(wt, c, p)) == h]
    print(f'{src:12s} {mt} {h[:12]} {p}: matches at {hits if hits else "NONE"}')
    for c in commits:
        print(f'    {c[:8]} {dig(blob(wt, c, p))[:12]}')
cdir = cman.rsplit('/', 1)[0]
for src, h, mt, p in rows:
    if src == 'checkpoint':
        b = blob(cwt, 'HEAD', f'{cdir}/dev-origin-drive/{p}')
        print(f'checkpoint copy {cdir}/dev-origin-drive/{p}: {"IDENTICAL to recorded" if dig(b) == h else "DIFFERS " + dig(b)[:12]}')
