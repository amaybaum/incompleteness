#!/usr/bin/env python3
"""Coordinator's replay harness for the round-5 experiment scripts of one research thread.

Usage: python3 -I -B replay_r5.py <worktree> <thread> <r4head> <head> <outdir> [--timeout S] [--only a.py,b.py]

Lists research/<thread>/experiments/*.py added or modified between <r4head> and <head> (git diff --name-status),
excluding kept-run copies (*.runN.py), exports each script and its committed .out at <head> into a fresh directory
<outdir>/<thread>-replay/ (the whole experiments/ tree at <head> is exported, so sibling imports and data files resolve),
runs `python3 -I -B <script>` from that directory with the given timeout, and compares stdout byte-for-byte with the
committed <script-stem>.out.  Prints one line per script: IDENTICAL / DIFFERENT (first differing line) / NO-OUT /
TIMEOUT / EXIT <code>.  Nothing is written into the thread's worktree.
"""
import os
import shutil
import subprocess
import sys
import time

wt, thread, r4, head, outdir = sys.argv[1:6]
timeout = 1800
only = None
args = sys.argv[6:]
for i, a in enumerate(args):
    if a == '--timeout':
        timeout = int(args[i + 1])
    if a == '--only':
        only = set(args[i + 1].split(','))
pref = f'research/{thread}/experiments/'
names = subprocess.run(['git', '-C', wt, 'diff', '--name-status', f'{r4}..{head}', '--', pref],
                       capture_output=True, text=True, check=True).stdout.splitlines()
scripts = []
for ln in names:
    st, *paths = ln.split('\t')
    p = paths[-1]
    if st.startswith('D') or not p.endswith('.py'):
        continue
    base = os.path.basename(p)
    if '.run' in base and base.split('.run')[1].split('.')[0].isdigit():
        continue
    if only and base not in only:
        continue
    scripts.append(base)
work = os.path.join(outdir, f'{thread}-replay')
if os.path.exists(work):
    shutil.rmtree(work)
os.makedirs(work)
# export the experiments tree at head
tar = subprocess.run(['git', '-C', wt, 'archive', head, pref], capture_output=True, check=True).stdout
subprocess.run(['tar', '-x', '-C', work], input=tar, check=True)
edir = os.path.join(work, pref)
print(f'thread {thread}: {len(scripts)} round-5 scripts between {r4[:8]} and {head[:8]}; replay dir {edir}', flush=True)
for s in sorted(scripts):
    stem = s[:-3]
    outp = os.path.join(edir, stem + '.out')
    if not os.path.exists(outp):
        print(f'NO-OUT    {s}', flush=True)
        continue
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, '-I', '-B', s], cwd=edir, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(f'TIMEOUT   {s} after {timeout}s', flush=True)
        continue
    dt = time.time() - t0
    with open(os.path.join(work, stem + '.coord.out'), 'wb') as f:
        f.write(r.stdout)
    with open(os.path.join(work, stem + '.coord.err'), 'wb') as f:
        f.write(r.stderr)
    ref = open(outp, 'rb').read()
    if r.returncode != 0:
        print(f'EXIT {r.returncode:<4} {s} ({dt:.0f}s); stderr tail: {r.stderr.decode(errors="replace")[-200:]!r}', flush=True)
        continue
    if r.stdout == ref:
        print(f'IDENTICAL {s} ({dt:.0f}s, {len(ref)} bytes)', flush=True)
    else:
        a = ref.decode(errors='replace').splitlines()
        b = r.stdout.decode(errors='replace').splitlines()
        k = next((i for i in range(min(len(a), len(b))) if a[i] != b[i]), min(len(a), len(b)))
        print(f'DIFFERENT {s} ({dt:.0f}s): first difference at line {k + 1}: committed {a[k][:80] if k < len(a) else "<eof>"!r} '
              f'vs replay {b[k][:80] if k < len(b) else "<eof>"!r}', flush=True)
