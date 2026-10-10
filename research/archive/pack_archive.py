#!/usr/bin/env python3
"""Pack the scratchpad research records into the research/archive worktree.

Usage: python3 -I -B pack_archive.py --dry-run | --copy <dest-dir>
Rules (recorded in EXCLUDED.md of the archive):
  R1 nested git repositories (directories whose root holds .git) are not copied; they are catalogued in WORKTREES.md
     with branch, HEAD and dirtiness (their content is on GitHub by branch, or is a Mathlib clone).
  R2 repository snapshots (a directory holding the kernel tree verification/lean-mathlib, or verification/lean with tools/, or AGENTS.md with papers/ and book/) are not copied; the
     base commit they cite is recorded; the records that used them cite that commit themselves.
  R3 vendored sources and tool caches are not copied: mathlib sources (ml-v433-src, mathlib433, mathlib-ref), the
     pandoc wheel (pd), __pycache__ and *.pyc, .lake, node_modules.
  R4 files larger than 5 MiB (text-like extensions) or 2 MiB (binary extensions) are not copied; their path, size and sha256 are recorded in EXCLUDED-LARGE.sha256.
  R5 everything else is copied byte for byte to <dest>/research/archive/<relative path>; MANIFEST.sha256 lists every
     copied file with its sha256 (paths relative to research/archive/).
"""
import os, sys, hashlib, shutil
SCRATCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = 5 * 1024 * 1024
BIN_LIMIT = 2 * 1024 * 1024
TEXT_EXT = {'.md', '.txt', '.py', '.sh', '.lean', '.json', '.tsv', '.csv', '.out', '.err', '.log', '.yml', '.yaml', '.tex', '.patch', '.sha256', '.toml', '.cfg', '.ini', '.rst', '.html', '.xml', '.bib', '.gz'}
NAMED_SNAPSHOTS = {'base0f', 'landedL', 'cnt', 'd41'}
VENDORED = {'ml-v433-src', 'mathlib433', 'mathlib-ref', 'pd'}
SKIP_DIRNAMES = {'__pycache__', '.lake', 'node_modules', '.mypy_cache', '.pytest_cache', 'pyf', 'pyflakes', 'site-packages'}
def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''): h.update(chunk)
    return h.hexdigest()
def is_repo_snapshot(d):
    # a copy of the repository tree (full or partial): the kernel tree, or the manuscript tree with its build script
    if os.path.isdir(os.path.join(d, 'verification', 'lean-mathlib')): return True
    if os.path.isdir(os.path.join(d, 'verification', 'lean')) and os.path.isdir(os.path.join(d, 'tools')): return True
    return os.path.isfile(os.path.join(d, 'AGENTS.md')) and os.path.isdir(os.path.join(d, 'papers')) and os.path.isdir(os.path.join(d, 'book'))
def walk():
    """Yield (kind, relpath, size) with kind in {'file', 'git', 'snapshot', 'vendored', 'large', 'cache'}."""
    for root, dirs, files in os.walk(SCRATCH):
        rel = os.path.relpath(root, SCRATCH)
        if rel == '.': rel = ''
        # prune
        keep = []
        for d in sorted(dirs):
            dp = os.path.join(root, d); rp = os.path.join(rel, d) if rel else d
            if d in SKIP_DIRNAMES or d == '.git':
                yield ('cache', rp, 0); continue
            if rel == '' and d in VENDORED:
                yield ('vendored', rp, 0); continue
            if os.path.exists(os.path.join(dp, '.git')):
                yield ('git', rp, 0); continue
            if (rel == '' and d in NAMED_SNAPSHOTS) or is_repo_snapshot(dp):
                yield ('snapshot', rp, 0); continue
            keep.append(d)
        dirs[:] = keep
        for f in sorted(files):
            fp = os.path.join(root, f); rp = os.path.join(rel, f) if rel else f
            if f.endswith('.pyc'): yield ('cache', rp, 0); continue
            try: sz = os.path.getsize(fp)
            except OSError: continue
            if os.path.islink(fp): yield ('cache', rp, 0); continue
            ext = os.path.splitext(f)[1].lower()
            lim = LIMIT if ext in TEXT_EXT else BIN_LIMIT
            if sz > lim: yield ('large', rp, sz); continue
            yield ('file', rp, sz)
def main():
    mode = sys.argv[1]
    dest = sys.argv[2] if mode == '--copy' else None
    counts = {}; sizes = {}; entries = {'git': [], 'snapshot': [], 'vendored': [], 'large': []}
    files = []
    for kind, rp, sz in walk():
        counts[kind] = counts.get(kind, 0) + 1; sizes[kind] = sizes.get(kind, 0) + sz
        if kind in entries: entries[kind].append((rp, sz))
        if kind == 'file': files.append((rp, sz))
    # per top-level totals of copied files
    top = {}
    for rp, sz in files:
        t = rp.split('/')[0]; a = top.setdefault(t, [0, 0]); a[0] += 1; a[1] += sz
    print('counts', counts); print('sizes MB', {k: round(v / 1e6, 1) for k, v in sizes.items()})
    print('copied-file total MB', round(sum(s for _, s in files) / 1e6, 1), 'files', len(files))
    for t, (n, s) in sorted(top.items(), key=lambda kv: -kv[1][1])[:40]:
        print(f'  {t:40s} {n:6d} files {s/1e6:8.1f} MB')
    print('large files:');
    for rp, sz in entries['large']: print(f'  {sz/1e6:8.1f} MB  {rp}')
    print('snapshots:', [rp for rp, _ in entries['snapshot']])
    print('git dirs:', len(entries['git']))
    if mode != '--copy': return
    base = os.path.join(dest, 'research', 'archive'); os.makedirs(base, exist_ok=True)
    man = []
    for rp, sz in files:
        src = os.path.join(SCRATCH, rp); dst = os.path.join(base, rp)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        man.append((sha256(dst), rp))
    with open(os.path.join(base, 'MANIFEST.sha256'), 'w', encoding='utf-8') as f:
        for h, rp in man: f.write(f'{h}  {rp}\n')
    with open(os.path.join(base, 'EXCLUDED-LARGE.sha256'), 'w', encoding='utf-8') as f:
        for rp, sz in entries['large']: f.write(f'{sha256(os.path.join(SCRATCH, rp))}  {sz:12d}  {rp}\n')
    with open(os.path.join(base, 'EXCLUDED-SNAPSHOTS.txt'), 'w', encoding='utf-8') as f:
        for rp, _ in entries['snapshot']:
            n = sum(len(fs) for _, _, fs in os.walk(os.path.join(SCRATCH, rp)))
            f.write(f'{rp}\t{n} files\n')
    print('copied', len(man), 'files; manifest written')
main()
