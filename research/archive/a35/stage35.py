"""Split the green dev module into the stage-1 and stage-2 module texts (frozen header kept).
usage: python3 stage35.py <dev module .lean> -> stage1.lean, stage2.lean beside it, with controls.module_label
for both, and the audit of landed helpers off the provenance list."""
import re, sys, importlib.util, subprocess, json, os
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('c35', os.path.join(S, 'controls.py')); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
src = open(sys.argv[1], encoding='utf-8').read()

def cut(text, name):
    m = re.search(r'(?m)^theorem %s :\n' % re.escape(name), text)
    assert m, name
    e = re.search(r'(?m)^#print axioms %s\n(?:\n)?' % re.escape(name), text[m.start():])
    assert e, name
    return text[:m.start()] + text[m.start() + e.end():], text[m.start():m.start() + e.end()]

body1, verdict = cut(src, 'a35_dita_stratified')
body1, coroll = cut(body1, 'a35_c_exclusive')
tail = 'end DitaHull\nend OIBridge\n'
assert body1.endswith(tail)
stage1 = body1
stage2 = body1[:-len(tail)] + verdict + coroll + tail
open(os.path.join(S, 'stage1.lean'), 'w', encoding='utf-8').write(stage1)
open(os.path.join(S, 'stage2.lean'), 'w', encoding='utf-8').write(stage2)
for nm, txt in (('stage1', stage1), ('stage2', stage2)):
    lab, f = C.module_label(txt)
    print(nm, 'label', lab, 'findings', f, 'theorems', len(C.theorems(C.strip_comments(txt))))
    print(nm, 'blob', subprocess.run(['git', 'hash-object', os.path.join(S, nm + '.lean')], capture_output=True, text=True).stdout.strip())

# ---- audit: landed helpers consumed by proofs, against the preregistration's provenance list
F = '62479b5780c1c3e3809e5d49cf7e1cf3684ced80'
WT = os.path.join(S, '..', 'wt-d35')
files = subprocess.run(['git', 'ls-tree', '-r', '--name-only', F, 'verification/lean-mathlib/OIBridge/'], capture_output=True, text=True, cwd=WT).stdout.split()
names = {}
for p in files:
    s = subprocess.run(['git', 'show', F + ':' + p], capture_output=True, text=True, cwd=WT).stdout
    for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+|noncomputable[ \t]+)*(?:theorem|lemma|def|abbrev)[ \t]+(\S+)', s):
        names.setdefault(m.group(1), p.split('/')[-1][:-5])
pre = open(os.path.join(S, 'rec', 'preregistration.md'), encoding='utf-8').read()
prov = pre[pre.index('## Provenance'):pre.index('## Locating controls')]
PROV = set(re.findall(r'`([A-Za-z0-9_\']+)`', prov))
code = C.strip_comments(stage2)
by_helper = {}
for b in re.split(r'(?m)^(?=theorem )', code):
    m = re.match(r'theorem (\S+)', b)
    if not m: continue
    proof = b[b.index(':= by') + 5:] if ':= by' in b else b
    for ident in set(re.findall(r"(?<![A-Za-z0-9_'.])[A-Za-z_][A-Za-z0-9_']*", proof)):
        if ident in names and ident not in PROV and not ident.startswith('a35_') and not (ident.startswith('a34_') or ident.startswith('a33_')):
            by_helper.setdefault((ident, names[ident]), []).append(m.group(1))
print('\nOFF-LIST LANDED HELPERS (name, module, consumers):')
for (h, f), ts in sorted(by_helper.items()):
    print(' ', h, f, len(ts), ts[:6])
