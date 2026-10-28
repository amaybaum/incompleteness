"""SC-36 added-line scan: the §A.32/§A.33 phrase family, revision voice and caps emphasis on added
manuscript lines, and a secrets / local-path scan on every added line of the branch.
Run from the repository root: python3 -I <this file> <base>."""
import re, subprocess, sys

base = sys.argv[1]
diff = subprocess.run(['git', 'diff', '-U0', base, '--', '.', ':(exclude)*.pdf', ':(exclude)*.tex',
                       ':(exclude)*/sc36_scan.py',  # this file holds the patterns themselves
                       ':(exclude)*/sc36_*.out'],   # generated outputs, including this scan's own
                      capture_output=True, text=True).stdout
cur = None
added = []
for line in diff.splitlines():
    if line.startswith('+++ '):
        cur = line[6:]
    elif line.startswith('+') and not line.startswith('+++'):
        added.append((cur, line[1:]))

PHRASES = [r'discipline', r'\bhonest', r'should not be read', r'the reader', r'neither borrows',
           r'temptation', r'in that register', r'now settled', r'in its current form', r'corrected form',
           r'as redefined', r'no longer', r'formerly', r'is not listed', r'withdrawn', r'earlier revision',
           r'previously', r'was stated', r'has been corrected', r'we now']
WHITELIST = {'GW250114', 'QFT', 'LIGO', 'KAGRA', 'DESI', 'CPTP', 'MOND', 'KMS', 'JUNO', 'XENON', 'CODATA', 'BTFR'}
hits = 0
for f, l in added:
    if not (f.startswith('papers/') or f.startswith('book/')) or not f.endswith('.md'):
        continue
    for p in PHRASES:
        if re.search(p, l, re.I):
            hits += 1; print(f'PHRASE {p!r}: {f}: {l[:140]}')
    prose = re.sub(r'\$[^$]*\$', '', l)
    for w in re.findall(r'(?<![\w-])[A-Z]{4,}(?![\w-])', prose):
        if w not in WHITELIST:
            hits += 1; print(f'CAPS {w}: {f}: {l[:140]}')
SECRETS = [r'/tmp/', r'/home/', r'/root/', r'claude-0', r'scratchpad', r'gh[pousr]_[A-Za-z0-9]{20,}',
           r'-----BEGIN', r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}', r'\b\d{1,3}(\.\d{1,3}){3}\b',
           r'X-Amz-Signature', r'sig=']
for f, l in added:
    for p in SECRETS:
        if re.search(p, l):
            hits += 1; print(f'SECRET/PATH {p!r}: {f}: {l[:140]}')
print(f'added lines scanned: {len(added)}; hits: {hits}')
sys.exit(1 if hits else 0)
