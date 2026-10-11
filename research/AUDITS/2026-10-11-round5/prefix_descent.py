"""Append-only descent: does some line-boundary prefix of the committed file hash to the recorded digest?
Usage: python3 -I -B prefix_descent.py <worktree> <ref> <path> <recorded-sha256>
Prints PREFIX-MATCH with the prefix's line count and the number of lines appended after it, or NO-PREFIX-MATCH.
"""
import hashlib, subprocess, sys
wt, ref, path, rec = sys.argv[1:5]
b = subprocess.run(['git', '-C', wt, 'show', f'{ref}:{path}'], capture_output=True, check=True).stdout
lines = b.split(b'\n')
acc = b''
for i, ln in enumerate(lines):
    acc_nl = acc + ln + b'\n' if i < len(lines) - 1 else acc + ln
    for cand in (acc_nl, acc + ln):
        if hashlib.sha256(cand).hexdigest() == rec:
            print(f'PREFIX-MATCH {path} at {ref[:8]}: first {i + 1} of {len(lines)} lines ({len(cand)} of {len(b)} bytes); appended after: {len(b) - len(cand)} bytes')
            sys.exit(0)
    acc = acc_nl
print(f'NO-PREFIX-MATCH {path} at {ref[:8]}')
