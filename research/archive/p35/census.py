"""Probe membership census for the core-shard split: the probes named by the core loops of the workflow at a base
commit versus the working tree; every probe must appear exactly once in each version and the two sets must be equal."""
import re, subprocess, sys, collections
base = sys.argv[1]
old = subprocess.run(['git', 'show', base + ':.github/workflows/verify.yml'], capture_output=True, text=True, check=True).stdout
new = open('.github/workflows/verify.yml', encoding='utf-8').read()
def loops(txt):
    """every `for p in ...; do` list under a `verification/lean` step, as (step name, [probes])"""
    out = []
    for m in re.finditer(r'- name: (Core probes[^\n]*)\n\s+working-directory: verification/lean\n\s+run: \|\n\s+for p in (.*?); do', txt, re.S):
        out.append((m.group(1), m.group(2).replace('\\\n', ' ').split()))
    return out
lo, ln = loops(old), loops(new)
co = collections.Counter(p for _, ps in lo for p in ps); cn = collections.Counter(p for _, ps in ln for p in ps)
print('base %s: %s' % (base[:8], ', '.join('%s (%d)' % (n, len(ps)) for n, ps in lo)))
print('working tree: %s' % ', '.join('%s (%d)' % (n, len(ps)) for n, ps in ln))
dup_o = [p for p, c in co.items() if c != 1]; dup_n = [p for p, c in cn.items() if c != 1]
print('each probe exactly once: base %s, new %s' % (not dup_o, not dup_n), dup_o, dup_n)
print('same probe set: %s; missing %s; added %s' % (set(co) == set(cn), sorted(set(co) - set(cn)), sorted(set(cn) - set(co))))
print('probes on disk not in any core loop (new):', sorted(set(re.sub(r'_probe\.py$', '', f) for f in __import__('os').listdir('verification/lean') if f.endswith('_probe.py')) - set(cn)))
sys.exit(0 if not dup_o and not dup_n and set(co) == set(cn) else 1)
