#!/usr/bin/env python3
"""Content check for the two scratch files of research/origin that the coordinator's first transcript replay re-wrote
(dev_replay.run1: the thread's commands of 10:13:58Z and 10:44:00Z, which write scratchpad/origin-r5/check/names.py
and names2.py).  Re-executes the same two transcript commands with both the thread's scratch directory and the dev
worktree rewritten into a fresh sandbox, then compares the sandbox files with the thread's scratch files by sha256.
Usage: python3 -I -B names_sandbox_check.py <transcript.jsonl> <thread-scratch-dir> <dev-worktree> <sandbox>
Prints one line per file: IDENTICAL or DIFFERENT, with both digests.
"""
import hashlib, json, os, shutil, subprocess, sys
tr, th, dev, sb = sys.argv[1:5]
want = ['2026-10-11T10:13:58.218Z', '2026-10-11T10:44:00.304Z']
cmds = {}
for ln in open(tr, encoding='utf-8'):
    try:
        m = json.loads(ln)
    except Exception:
        continue
    c = (m.get('message') or {}).get('content')
    if not isinstance(c, list):
        continue
    for x in c:
        if x.get('type') == 'tool_use' and m.get('timestamp') in want:
            cmds[m['timestamp']] = x['input']['command']
if os.path.exists(sb):
    shutil.rmtree(sb)
os.makedirs(os.path.join(sb, 'check'))
os.makedirs(os.path.join(sb, 'dev'))
for ts in want:
    cmd = cmds[ts].replace(th, os.path.join(sb, 'check')).replace(dev, os.path.join(sb, 'dev'))
    r = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True)
    print(f'{ts} re-executed in the sandbox (exit {r.returncode}; a nonzero exit comes from the analysis tail, which '
          f'reads the dev tree, not from the file write)')
for f in ['names.py', 'names2.py']:
    a = hashlib.sha256(open(os.path.join(sb, 'check', f), 'rb').read()).hexdigest()
    b = hashlib.sha256(open(os.path.join(th, f), 'rb').read()).hexdigest()
    print(f'{"IDENTICAL" if a == b else "DIFFERENT"} {f}: sandbox {a} thread scratch {b}')
