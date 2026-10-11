"""Compare each file in INTERRUPTION-MANIFEST.sha256 with its committed version on the thread branch.
Usage: python3 -I -B interrupt_descent.py <manifest> <thread> <worktree> <ref>
For each manifest row of <thread>: IDENTICAL if sha256(blob at <ref>) == recorded digest; CHANGED if the path exists
at <ref> with another digest (then the commits after the interruption that touched it are listed); ABSENT if it does not
exist at <ref>.  For the 'dev-origin-drive' rows the path is looked up on the thread's dev branch named in argv[5] if given.
"""
import hashlib, subprocess, sys
man, thread, wt, ref = sys.argv[1:5]
devref = sys.argv[5] if len(sys.argv) > 5 else None
rows = []
for ln in open(man):
    if ln.startswith('#') or not ln.strip(): continue
    h, st, mt, loc = ln.split()
    w, p = loc.split(':', 1)
    if w == thread or (w == 'dev-origin-drive' and thread == 'origin'):
        rows.append((h, st, mt, w, p))
for h, st, mt, w, p in rows:
    r = ref if w == thread else devref
    if r is None:
        print(f'SKIP      {w}:{p} (no ref given)'); continue
    b = subprocess.run(['git', '-C', wt, 'show', f'{r}:{p}'], capture_output=True)
    if b.returncode != 0:
        print(f'ABSENT    {w}:{p} at {r[:8]}'); continue
    d = hashlib.sha256(b.stdout).hexdigest()
    if d == h:
        print(f'IDENTICAL {w}:{p}')
    else:
        log = subprocess.run(['git', '-C', wt, 'log', '--format=%h %cI %s', f'{r}', '--since=2026-10-11T08:00:00Z', '--', p], capture_output=True, text=True).stdout.strip().splitlines()
        print(f'CHANGED   {w}:{p} recorded {h[:12]} committed {d[:12]}; commits touching it since 08:00Z: {[l[:60] for l in log]}')
