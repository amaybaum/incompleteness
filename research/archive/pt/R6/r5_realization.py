# r5_realization.py -- R6 node R5: does any statement at L attach an embedded-observer realization to a pair-cone object?
# DECISION RULE (fixed before the first run, 18:25Z by date -u; read-only scan of pt/base at L):
#  Files: every verification/lean-mathlib/OIBridge/*.lean and the root OIBridge.lean; papers/*.md; book/*.md;
#   verification/ROADMAP.md; verification/README.md; the K-programme round notes
#   verification/programmes/oi-qm/reconstruction/round-*/result.md.
#  Pair-level tokens P: W 3 | W d | CompositeDimension | K2Guard | prodState | maxCone | CandidateCone | NativeGate |
#   actC | actT | pair cone | composite cone | cnot (word).
#  Realization tokens H: RealizesSealedOICore | OICore | realiz(e|es|ed|ation|ations) | embedded observer | embedded
#   realization | Axiom 1 | Axiom 2 | C1–C4 | substratum.
#  (a) Lean import graph: the modules whose import closure contains a pair module {CompositeDimension, K2Guard,
#   KInfFoundations} and an H-level realization module {OIRealization, RouteB, ManuscriptAxioms, SubstratumInterface,
#   SubstratumInterfaceAudit, StructuralClosure, CombRealization, InstrumentRealization}; (b) Lean modules whose own text
#   carries both a P token and an H token; (c) text lines (non-Lean files) carrying both kinds.
#  Every hit of (b)/(c) is printed (file:line, 170 chars) as an attachment candidate; reading and classifying the hits is
#   done in NOTES, not by this script. The script decides only the counts.
#  CONTROLS: the root OIBridge.lean must appear in (a) (positive control of the closure computation); Main.md:562 must
#   carry an H token and CompositeDimension.lean a P token (positive controls of the regexes); a scan with the P regex
#   replaced by a token absent from the corpus (QQQ-ABSENT) must return zero hits (countercontrol).
import os, re

BASE = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/base'
LEAN = BASE + '/verification/lean-mathlib/OIBridge'
P_RE = re.compile(r'\bW 3\b|\bW d\b|CompositeDimension|K2Guard|prodState|maxCone|CandidateCone|NativeGate|\bactC\b|\bactT\b|'
                  r'pair cone|composite cone|\bcnot\b')
H_RE = re.compile(r'RealizesSealedOICore|OICore|[Rr]ealiz(e|es|ed|ation|ations)\b|embedded observer|embedded realization|'
                  r'Axiom 1\b|Axiom 2\b|C1[–-]C4|[Ss]ubstratum')
def rd(p):
    with open(p, encoding='utf-8') as f: return f.read()
mods = {f[:-5]: rd(os.path.join(LEAN, f)) for f in sorted(os.listdir(LEAN)) if f.endswith('.lean')}
root = rd(BASE + '/verification/lean-mathlib/OIBridge.lean')
def imports(txt): return set(re.findall(r'^import OIBridge\.(\w+)', txt, re.M))
imp = {m: imports(t) for m, t in mods.items()}
imp['ROOT:OIBridge'] = imports(root)
def closure(m, seen=None):
    seen = set() if seen is None else seen
    for n in imp.get(m, ()):
        if n not in seen: seen.add(n); closure(n, seen)
    return seen
PMODS = {'CompositeDimension', 'K2Guard', 'KInfFoundations'}
HMODS = {'OIRealization', 'RouteB', 'ManuscriptAxioms', 'SubstratumInterface', 'SubstratumInterfaceAudit', 'StructuralClosure',
         'CombRealization', 'InstrumentRealization'}
print('modules', len(mods), '+ root; H-level modules present:', sorted(HMODS & set(mods)), '; pair modules present:', sorted(PMODS & set(mods)))
both = sorted(m for m in imp if (closure(m) | {m}) & PMODS and (closure(m) | {m}) & HMODS)
print('(a) modules reaching both a pair module and an H-level realization module:', both)
hits_b = []
for m, t in mods.items():
    pl = [i + 1 for i, l in enumerate(t.split('\n')) if P_RE.search(l)]
    hl = [i + 1 for i, l in enumerate(t.split('\n')) if H_RE.search(l)]
    if pl and hl: hits_b.append((m, len(pl), len(hl), pl[:3], hl[:3]))
print('(b) Lean modules whose text carries both kinds:', len(hits_b))
for h in hits_b: print('  B %-28s P-lines %d (first %s) H-lines %d (first %s)' % (h[0], h[1], h[3], h[2], h[4]))
files = [os.path.join('papers', f) for f in sorted(os.listdir(BASE + '/papers')) if f.endswith('.md')]
files += [os.path.join('book', f) for f in sorted(os.listdir(BASE + '/book')) if f.endswith('.md')]
files += ['verification/ROADMAP.md', 'verification/README.md']
RB = BASE + '/verification/programmes/oi-qm/reconstruction'
files += [os.path.join('verification/programmes/oi-qm/reconstruction', d, 'result.md') for d in sorted(os.listdir(RB))
          if os.path.exists(os.path.join(RB, d, 'result.md'))]
def scan(p_re):
    out = []
    for f in files:
        for i, l in enumerate(rd(os.path.join(BASE, f)).split('\n')):
            if p_re.search(l) and H_RE.search(l): out.append((f, i + 1, l))
    return out
hits_c = scan(P_RE)
print('(c) text files scanned:', len(files), '; lines carrying both kinds:', len(hits_c))
for f, n, l in hits_c:
    ps = sorted(set(m.group(0) for m in P_RE.finditer(l))); hs = sorted(set(m.group(0) for m in H_RE.finditer(l)))
    print('  C %s:%d P%s H%s | %s' % (f, n, ps, hs, re.sub(r'\s+', ' ', l)[:170]))
ok = {}
ok['ctrl root in (a)'] = 'ROOT:OIBridge' in both
ok['ctrl Main.md:562 H token'] = bool(H_RE.search(rd(BASE + '/papers/Main.md').split('\n')[561]))
ok['ctrl CompositeDimension P token'] = bool(P_RE.search(mods['CompositeDimension']))
ok['countercontrol absent token'] = len(scan(re.compile(r'QQQ-ABSENT'))) == 0
for k, v in ok.items(): print('CHECK', k, 'PASS' if v else 'FAIL')
if all(ok.values()):
    print('VERDICT R5-SCAN-EXACT: (a) %d module(s) reach both kinds: %s; (b) %d Lean module(s) and (c) %d text line(s) carry both '
          'kinds of token (each read in NOTES); controls green' % (len(both), both, len(hits_b), len(hits_c)))
else:
    print('NO VERDICT')
