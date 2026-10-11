"""Extract the audit-relevant lines of a saved GitHub Actions job log (the Mathlib bridge job of verify.yml).

Usage: python3 -I -B joblog_extract.py <saved-log-file> [module-name]
Prints: the Build step's module line(s), 'Build completed'/'error' lines, every '#print axioms' result line
(`depends on axioms`), the release-gate step lines (PASS/FAILED/OK), lean-axioms, legacy-records, v3-receipts,
and a count of standard vs sorryAx prints for the named module.
"""
import re
import sys

path = sys.argv[1]
mod = sys.argv[2] if len(sys.argv) > 2 else None
raw = open(path, encoding='utf-8', errors='replace').read()
# The MCP tool returns the log as one logical line with literal newlines or escaped ones; normalize both.
if raw.count('\n') < 50 and '\\n' in raw:
    raw = raw.replace('\\n', '\n')
lines = raw.split('\n')
print(f'lines: {len(lines)}')

def strip_ts(s):
    return re.sub(r'^\S*\d{4}-\d{2}-\d{2}T[\d:.]+Z\s?', '', s)

pat = re.compile(r"(Built OIBridge\.|Build completed|Building OIBridge\.|error:|depends on axioms|"
                 r"^\S*\s*(PASS|FAILED|OK)\b|lean-axioms|legacy|receipt|named result|sorry|"
                 r"##\[group\]Run |##\[error\]|VERDICT|UNCLASSIFIED|problem)", re.I)
std = sorry_ = 0
for ln in lines:
    s = strip_ts(ln)
    if pat.search(s):
        if 'depends on axioms' in s:
            if mod is None or f'.{mod}.' in s or f' {mod}.' in s or f'OIBridge.{mod}' in s:
                if '[propext, Classical.choice, Quot.sound]' in s:
                    std += 1
                elif 'sorryAx' in s:
                    sorry_ += 1
        print(s[:300])
print(f'PRINTS({mod}): standard={std} sorryAx={sorry_}')
