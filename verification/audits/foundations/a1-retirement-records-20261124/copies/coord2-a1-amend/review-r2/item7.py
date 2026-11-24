# Reviewer: item 7 exactly as frozen (P PREREG lines 4631-4632) on H + the proposed ledger, over papers/*.md and book/*.md.
# Pointer clause: `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit" -> only the ledger's false positives
# (LEDGER.md:304 at H: "(A1)" anomaly conditions at appB:235/:246; FULL mirrors). Count clause: "Fourteen", "six structural", "sixth of" -> zero.
import sys, json, subprocess, hashlib, re
REPO, LEDGER = sys.argv[1], sys.argv[2]
H = '53c6601a10419b6b333cc992474272501ab542af'
def git(*a): return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, check=True).stdout
led = json.load(open(LEDGER)); assert led['base'] == H
files = [f for f in git('ls-tree', '-r', '--name-only', H, 'papers', 'book').decode().split('\n')
         if re.match(r'^(papers|book)/[^/]+\.md$', f)]
by = {}
for s in led['splices']: by.setdefault(s['file'], []).append(s)
tree = {}
for f in files:
    b = bytearray(git('show', '%s:%s' % (H, f)))
    for s in sorted(by.get(f, []), key=lambda s: s['start'], reverse=True):
        assert hashlib.sha256(bytes(b[s['start']:s['end']])).hexdigest() == s['old_sha256']
        b[s['start']:s['end']] = s['new'].encode()
    tree[f] = b.decode()
PTR = re.compile(r'\bA1\b|total-finiteness|posit \(ii\)|item \(ii\)|finiteness posit')
CNT = re.compile(r'Fourteen|six structural|sixth of')
FP = re.compile(r'^\(A1\) ')  # the anomaly-condition label lines
def run(t, tag):
    ptr = [(f, i + 1, l) for f, x in t.items() for i, l in enumerate(x.split('\n')) if PTR.search(l)]
    cnt = [(f, i + 1, l) for f, x in t.items() for i, l in enumerate(x.split('\n')) if CNT.search(l)]
    bad_ptr = [p for p in ptr if not (p[0] in ('book/appendix-b-derivations.md', 'book/The-Incompleteness-of-Observation-FULL.md') and FP.match(p[2]))]
    ok = not cnt and not bad_ptr
    print('%-34s ptr=%d (non-FP %d) count=%d -> %s' % (tag, len(ptr), len(bad_ptr), len(cnt), 'PASS' if ok else 'FAIL'))
    for p in ptr + cnt: print('   ', p[0], p[1], p[2][:90])
    return ok
run(tree, 'proposed tree (H + 407 splices)')
def mut(f, old, new, tag):
    t = dict(tree); assert t[f].count(old) == 1, (tag, t[f].count(old)); t[f] = t[f].replace(old, new); return run(t, tag)
SM = 'papers/SM.md'
newD402 = 'they hold under the assumptions of the local spatial/gauge construction of §2.3 together with cubic-group representation theory, and under the conditions marked at each entry.'
mut(SM, newD402, 'they hold for every bijection satisfying the six structural properties.', 'NC1 SM:1394 phrase reinstated')
mut('book/ch09-universality.md', 'the structural properties developed in Chapter 5 (', 'the six structural properties developed in Chapter 5 (', 'NC2 ch09:137 count reinstated')
mut('papers/Main.md', 'The posit ledger.', 'The posit ledger. Fourteen items, of unequal weight.', 'NC3 "Fourteen items" added')
mut(SM, 'Structural predictions', 'Structural predictions (under A1)', 'NC4 bare A1 pointer added')
mut('book/glossary.md', '**Background independence (A6).**', '**Background independence (A6).** The sixth of the structural assumptions.', 'NC5 "sixth of" added')
