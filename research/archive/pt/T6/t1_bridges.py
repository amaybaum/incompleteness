# t1_bridges.py -- T6 node D1: does any kernel module or declaration at L carry an H-, M- or G-level item to the
# pair carrier W 3 (an H->P, M->P or G->P bridge)?  Read-only on pt/base.  Exact (text and graph computation only).
# DECISION RULE (fixed before the first run, 19:01:27Z by date -u):
#  Tree: ../base/verification/lean-mathlib/OIBridge/*.lean and the root ../base/verification/lean-mathlib/OIBridge.lean.
#  Module graph: lines `import OIBridge.X` (X a module of the tree); the root is module `OIBridge`.
#  closure(m) = m together with every module it imports transitively inside the tree.
#  P-vocabulary (pair carrier and cone): the defining modules of the names W (abbrev), maxCone, actT, actC, cnot,
#    CandidateCone, prodState (def), NativeGate, IsNot -- each found by the regex
#    ^(noncomputable )?(abbrev|def|structure|class) NAME\b ; P-anchor = a module defining one of them.
#  HMG-vocabulary (matrix carrier, general carrier, substratum class, sealed core): FiniteOperationalTheory,
#    HasParallelReferenceExtension, ImplementationLocality, StructurallyClosed, ContextStable, LayerFlowExecutable,
#    DerivedOI, EmbeddedObservation, CompletedOI, OIPlus, ObservationalIndependence, substratumClass,
#    RealizesSealedOICore, OICore, QuantumArchitecture, HasCompositeUnitaryControl, PhysicalCompletionConditions,
#    WellFormed, ShadowQuantum, DrivesElementary, PairFlowSourced, InertSpectatorCompositionality -- defining modules by
#    the same regex (any namespace); a name with no definition is printed MISSING (a list error, not a verdict input).
#  B1 MEET = modules m with closure(m) containing a P-anchor and an HMG-anchor.
#  B2 ROOT: every declaration of the root (theorem/lemma/def/abbrev/structure/class/instance/example/noncomputable def)
#    is scanned for P-tokens (maxCone, actT, actC, cnot, CandidateCone, prodState, NativeGate, IsNot, CompositeDimension,
#    K2Guard, 'W 3', 'W d') and HMG-tokens (the HMG names); ROOT-CLEAN iff no root declaration carries a token of both.
#  B3 MEET-DECL: for each module in MEET other than the root, the same scan of its declarations; MEET-DECL-CLEAN iff none.
#  B4 SHARED = closure(P-anchors) intersect closure(HMG-anchors); printed with each module's count of top-level
#    `structure`/`class`/`def ... : Prop` declarations (for reading; not a verdict input).
#  B5 TEXT: lines of ../base/papers/*.md, ../base/book/*.md, ../base/verification/ROADMAP.md carrying a P-term
#    (maxCone, actC, actT, CandidateCone, `W 3`, W 3 written as "W 3", "pair cone", "composite cone") and an HMG-term
#    (FiniteOperationalTheory, HasParallelReferenceExtension, ImplementationLocality, StructurallyClosed, ContextStable,
#    LayerFlowExecutable, DerivedOI, EmbeddedObservation, "observational independence", "implementation locality",
#    "structural closure", "layer-flow", "matrix carrier") are printed file:line for reading; their count is recorded.
#  Countercontrol CC1: the same MEET computation after adding one synthetic import edge
#    (the importer of CompositeDimension named EffectSpace -> the first HMG-anchor module in sorted order) must
#    contain EffectSpace (detector live).  CC2: the token scan must flag a synthetic declaration text
#    "theorem x : maxCone = FiniteOperationalTheory" as carrying both.
#  VERDICT NO-BRIDGE-AT-L printed iff MEET subset of {OIBridge}, ROOT-CLEAN, MEET-DECL-CLEAN (vacuous if MEET = root),
#    no P-name MISSING, CC1 and CC2 behave.  Otherwise VERDICT NONE with the failing clause.
#  Scope of the verdict: kernel declarations at L.  A declaration can name only what its module's import closure
#    defines (Lean scoping), so no declaration outside MEET can state a fact mentioning both vocabularies.
#  RUN-2 AMENDMENT (19:02:29Z, after run 1, kept as t1_bridges.run1.*; run 1 printed VERDICT NO-BRIDGE-AT-L): the
#    P-name `W` matched `def W (u : PS s) : Matrix ...` in WeylTwirl.lean:151 (a Weyl operator, not the pair carrier),
#    making WeylTwirl a false P-anchor; this can only enlarge MEET (run 1's MEET = {OIBridge} stands) but it inflated
#    B4 SHARED with WeylTwirl's imports.  Amendment: the P-name W is matched only as `abbrev W (d : ℕ)` (the pair
#    carrier, CompositeDimension.lean:97); B4 is additionally printed for the closure of the genuine P-anchors, and
#    the closure of CompositeDimension (the K cluster below the carrier) is printed.  Nothing else changes.
import os, re, sys

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'base'))
LM = os.path.join(BASE, 'verification', 'lean-mathlib')
TREE = os.path.join(LM, 'OIBridge')
ROOT = os.path.join(LM, 'OIBridge.lean')

mods = {}
for fn in sorted(os.listdir(TREE)):
    if fn.endswith('.lean'):
        mods[fn[:-5]] = os.path.join(TREE, fn)
mods['OIBridge'] = ROOT
text = {m: open(p, encoding='utf-8').read() for m, p in mods.items()}
imp_re = re.compile(r'^import\s+OIBridge\.([A-Za-z0-9_]+)\s*$', re.M)
imports = {m: sorted(set(x for x in imp_re.findall(t) if x in mods)) for m, t in text.items()}
print('modules: %d (tree %d + root)' % (len(mods), len(mods) - 1))

def closure(m, imp):
    seen, st = set(), [m]
    while st:
        x = st.pop()
        if x in seen: continue
        seen.add(x); st.extend(imp.get(x, []))
    return seen

def defmods(name):
    if name == 'W':
        r = re.compile(r'^abbrev\s+W\s+\(d\s*:\s*ℕ\)', re.M)
    else:
        r = re.compile(r'^(?:noncomputable\s+)?(?:abbrev|def|structure|class|inductive)\s+' + re.escape(name) + r'\b', re.M)
    return sorted(m for m, t in text.items() if r.search(t))

PNAMES = ['W', 'maxCone', 'actT', 'actC', 'cnot', 'CandidateCone', 'prodState', 'NativeGate', 'IsNot']
HNAMES = ['FiniteOperationalTheory', 'HasParallelReferenceExtension', 'ImplementationLocality', 'StructurallyClosed',
          'ContextStable', 'LayerFlowExecutable', 'DerivedOI', 'EmbeddedObservation', 'CompletedOI', 'OIPlus',
          'ObservationalIndependence', 'substratumClass', 'RealizesSealedOICore', 'OICore', 'QuantumArchitecture',
          'HasCompositeUnitaryControl', 'PhysicalCompletionConditions', 'WellFormed', 'ShadowQuantum',
          'DrivesElementary', 'PairFlowSourced', 'InertSpectatorCompositionality']
pmiss, panch = [], set()
for n in PNAMES:
    d = defmods(n)
    print('P-name %-16s defined in %s' % (n, ', '.join(d) if d else 'MISSING'))
    if not d: pmiss.append(n)
    panch.update(d)
hanch = set()
for n in HNAMES:
    d = defmods(n)
    print('HMG-name %-31s defined in %s' % (n, ', '.join(d) if d else 'MISSING'))
    hanch.update(d)
print('P-anchors (%d): %s' % (len(panch), ', '.join(sorted(panch))))
print('HMG-anchors (%d): %s' % (len(hanch), ', '.join(sorted(hanch))))

def meet(imp):
    out = []
    for m in sorted(mods):
        c = closure(m, imp)
        if c & panch and c & hanch: out.append(m)
    return out
MEET = meet(imports)
print('B1 MEET (%d): %s' % (len(MEET), ', '.join(MEET)))

decl_re = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?'
                     r'(theorem|lemma|def|abbrev|structure|class|instance|example)\b', re.M)
PTOK = re.compile(r'\b(maxCone|actT|actC|cnot|CandidateCone|prodState|NativeGate|IsNot|CompositeDimension|K2Guard)\b|\bW [3d]\b')
HTOK = re.compile(r'\b(' + '|'.join(HNAMES) + r')\b')
def decls(t):
    starts = [mt.start() for mt in decl_re.finditer(t)] + [len(t)]
    return [t[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]
def both(d):
    return bool(PTOK.search(d)) and bool(HTOK.search(d))
rootdecls = decls(text['OIBridge'])
rootboth = [d.split('\n')[0][:90] for d in rootdecls if both(d)]
rootP = sum(1 for d in rootdecls if PTOK.search(d)); rootH = sum(1 for d in rootdecls if HTOK.search(d))
print('B2 ROOT: %d declarations; with P-token %d; with HMG-token %d; with both %d' % (len(rootdecls), rootP, rootH, len(rootboth)))
for x in rootboth: print('  ROOT-BOTH', x)
mdb = []
for m in MEET:
    if m == 'OIBridge': continue
    for d in decls(text[m]):
        if both(d): mdb.append((m, d.split('\n')[0][:90]))
print('B3 MEET-DECL (modules other than the root): %d declarations carrying both' % len(mdb))
for m, x in mdb: print('  MEET-BOTH', m, x)
shared = set()
for a in panch: shared |= closure(a, imports)
sh2 = set()
for a in hanch: sh2 |= closure(a, imports)
SHARED = sorted(shared & sh2)
propdef = re.compile(r'^(?:noncomputable\s+)?(?:structure|class)\s+\w+|^def\s+\w+[^\n:=]*:\s*Prop', re.M)
print('B4 SHARED (%d): %s' % (len(SHARED), ', '.join('%s[%d]' % (m, len(propdef.findall(text[m]))) for m in SHARED)))
cdc = sorted(closure('CompositeDimension', imports))
print('B4 closure(CompositeDimension) (%d): %s' % (len(cdc), ', '.join(cdc)))
importers = sorted(m for m in mods if 'CompositeDimension' in closure(m, imports) and m != 'CompositeDimension')
print('B4 modules importing CompositeDimension transitively (%d): %s' % (len(importers), ', '.join(importers)))
# B5 manuscripts and roadmap
PT5 = re.compile(r'maxCone|actC|actT|CandidateCone|`W 3`|\bW 3\b|pair cone|composite cone')
HT5 = re.compile(r'FiniteOperationalTheory|HasParallelReferenceExtension|ImplementationLocality|StructurallyClosed|'
                 r'ContextStable|LayerFlowExecutable|DerivedOI|EmbeddedObservation|observational independence|'
                 r'implementation locality|structural closure|layer-flow|matrix carrier', re.I)
files = []
for sub in ['papers', 'book']:
    dd = os.path.join(BASE, sub)
    files += [os.path.join(dd, f) for f in sorted(os.listdir(dd)) if f.endswith('.md')]
files.append(os.path.join(BASE, 'verification', 'ROADMAP.md'))
hits = []
for fp in files:
    for i, line in enumerate(open(fp, encoding='utf-8'), 1):
        if PT5.search(line) and HT5.search(line):
            hits.append('%s:%d: %s' % (os.path.relpath(fp, BASE), i, line.strip()[:160]))
print('B5 TEXT co-occurrence lines: %d' % len(hits))
for h in hits: print('  TEXT', h)
# countercontrols
imp2 = {m: list(v) for m, v in imports.items()}
tgt = sorted(hanch)[0]
imp2['EffectSpace'] = sorted(set(imp2.get('EffectSpace', []) + [tgt]))
M2 = meet(imp2)
cc1 = 'EffectSpace' in M2
print('CC1 synthetic edge EffectSpace -> %s: MEET size %d, contains EffectSpace: %s' % (tgt, len(M2), cc1))
cc2 = both('theorem x : maxCone = FiniteOperationalTheory')
print('CC2 synthetic declaration flagged: %s' % cc2)
ok = set(MEET) <= {'OIBridge'} and not rootboth and not mdb and not pmiss and cc1 and cc2
if ok:
    print('VERDICT NO-BRIDGE-AT-L: no kernel module other than the root reaches both vocabularies; no root declaration '
          'mentions both; %d manuscript/roadmap co-occurrence lines printed for reading' % len(hits))
else:
    print('VERDICT NONE: MEET=%s rootboth=%d meetdecl=%d pmiss=%s cc1=%s cc2=%s' % (MEET, len(rootboth), len(mdb), pmiss, cc1, cc2))
