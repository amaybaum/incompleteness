"""E3: check a retained expected result against the original job log it was derived from, and other runs' logs.

Usage:
    python3 -I E3_joblog_check.py TOOLS_DIR EXPECTED.json LEAN_TREE LOG [LOG ...]

TOOLS_DIR      a directory holding extract_result.py and compare_result.py of the frozen evidence-retention archive
               (`git show 48b18ac5:verification/audits/evidence-retention/<name>`)
EXPECTED.json  papers/introduction_repro/results-121598983127.json (at 4a260ca9)
LEAN_TREE      a directory holding verification/lean-mathlib/OIBridge/ at 17b830bc
LOG            a GitHub Actions job log, fetched whole (`gh api repos/<o>/<r>/actions/jobs/<id>/logs > LOG`)

For each log: sha256 of the whole log; the log cut at the release gate's verdict line; sha256 of that cut
(lines joined by newline, no trailing newline, as the archive counts); the frozen extractor on the cut; and the frozen
comparator against EXPECTED.json with --tree LEAN_TREE. For the first log, the digests are also compared with the
expected result's recorded `source.sha256`/`served_sha256`. Also reports, per log (within the cut), how many OIBridge modules lake
`Built` (elaborated in that job) versus `Replayed` (restored from the build cache).
Exit status 0 iff every comparison holds and the first log's digests match.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile


def main():
    tools, expected, tree, logs = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    exp = json.load(open(expected, encoding='utf-8'))
    src = exp['source']
    want_full = re.search(r'sha256 ([0-9a-f]{64})', src['kind']).group(1)
    bad = 0
    for i, log in enumerate(logs):
        raw = open(log, 'rb').read()
        lines = raw.split(b'\n')
        full = hashlib.sha256(raw).hexdigest()
        gate = next(k for k, l in enumerate(lines) if b'release gate: ' in l)
        cut = b'\n'.join(lines[:gate + 1])
        served = hashlib.sha256(cut).hexdigest()
        built = len(re.findall(rb'Built OIBridge[.\w]* \(', cut))
        replayed = len(re.findall(rb'Replayed OIBridge', cut))
        with tempfile.TemporaryDirectory() as d:
            cp = os.path.join(d, 'cut.log')
            open(cp, 'wb').write(cut)
            rep = os.path.join(d, 'rep.json')
            with open(rep, 'w') as f:
                subprocess.run([sys.executable, '-I', os.path.join(tools, 'extract_result.py'), cp], stdout=f, check=True)
            p = subprocess.run([sys.executable, '-I', os.path.join(tools, 'compare_result.py'), expected, rep,
                                '--tree', tree], capture_output=True, text=True)
        verdict = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr.strip()
        print(f'{os.path.basename(log)}: lines={len(raw.split(chr(10).encode())) - (1 if raw.endswith(b"\n") else 0)} '
              f'sha256={full} cut_at={gate + 1} cut_sha256={served} built={built} replayed={replayed}')
        print(f'  compare: {verdict}')
        for l in p.stdout.splitlines():
            if l.startswith('FAIL'):
                print('   ', l)
        if p.returncode != 0:
            bad += 1
        if i == 0:
            ok = full == want_full and served == src['served_sha256'] and gate + 1 == src['served_lines']
            print(f'  recorded digests (full {want_full[:16]}…, served {src["served_sha256"][:16]}…, '
                  f'{src["served_lines"]} lines): {"match" if ok else "MISMATCH"}')
            bad += 0 if ok else 1
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
