"""Partial Mathlib import-graph search over locally present blobs only (no fetch).

Usage: python3 -I ml_reach.py <present.txt: 'sha path' lines> <blobdir> <starts file> <target>...
<blobdir> holds one file per sha (pre-extracted with git cat-file, no network).
Prints, for each target, a chain from a start module if one exists through present files, and the
count of frontier modules whose source is not present (so a negative answer is inconclusive).
"""
import collections
import os
import re
import sys

IMPORT_RE = re.compile(r'^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z0-9_.]+)', re.M)


def header_imports(text):
    # drop block comments and line comments, then read import lines until the first other command
    text = re.sub(r'/-.*?-/', '', text, flags=re.S)
    text = re.sub(r'--[^\n]*', '', text)
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s == 'module' or s == 'prelude':
            continue
        m = IMPORT_RE.match(line)
        if m:
            out.append(m.group(1))
            continue
        break
    return out


def main():
    present_file, blobdir, starts_file = sys.argv[1:4]
    targets = sys.argv[4:]
    path_of = {}
    for line in open(present_file, encoding='utf-8'):
        sha, path = line.split()
        if path.endswith('.lean'):
            path_of[path[:-5].replace('/', '.')] = sha
    starts = [l.strip() for l in open(starts_file, encoding='utf-8') if l.strip()]
    parent = {s: None for s in starts}
    q = collections.deque(starts)
    missing = set()
    while q:
        m = q.popleft()
        sha = path_of.get(m)
        if sha is None:
            missing.add(m)
            continue
        with open(os.path.join(blobdir, sha), encoding='utf-8') as f:
            imps = header_imports(f.read())
        for i in imps:
            if i not in parent:
                parent[i] = m
                q.append(i)
    print('visited %d modules, %d with source absent locally' % (len(parent), len(missing)))
    for t in targets:
        if t in parent:
            chain = [t]
            while parent[chain[-1]] is not None:
                chain.append(parent[chain[-1]])
            print('REACHED %s via %s' % (t, ' <- '.join(chain)))
        else:
            print('NOT REACHED %s (inconclusive: %d frontier modules absent)' % (t, len(missing)))


if __name__ == '__main__':
    main()
