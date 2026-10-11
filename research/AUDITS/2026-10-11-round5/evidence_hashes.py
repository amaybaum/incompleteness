#!/usr/bin/env python3
"""Evidence hashes for one research thread's round: every file under research/<thread>/ added or modified between
<from> and <head> (git diff --name-status, deletions excluded), hashed at <head> from the object store, with the
commit (8 hex) that last wrote it in <from>..<head>.  One line per file: `sha256  path  thread@commit`.

Usage: python3 -I -B evidence_hashes.py <worktree> <thread> <from> <head>
"""
import hashlib
import subprocess
import sys

wt, thread, frm, head = sys.argv[1:5]
pref = f'research/{thread}/'


def git(*a, binary=False):
    r = subprocess.run(['git', '-C', wt, *a], capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode()


rows = []
for ln in git('diff', '--name-status', '--no-renames', f'{frm}..{head}', '--', pref).splitlines():
    st, p = ln.split('\t', 1)
    if st.startswith('D'):
        continue
    blob = git('show', f'{head}:{p}', binary=True)
    c = git('log', '-1', '--format=%H', f'{frm}..{head}', '--', p).strip()[:8]
    rows.append((p, hashlib.sha256(blob).hexdigest(), c))
for p, h, c in sorted(rows):
    print(f'{h}  {p}  {thread}@{c}')
