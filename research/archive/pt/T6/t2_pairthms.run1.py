# t2_pairthms.py -- T6 nodes D2/D3: (a) which kernel declarations at L quantify over a pair cone, (b) which theorems
# at L mention the one-token actions actC/actT and what they conclude, (c) Anc(P) over G6's edge table including the
# kernel-completed (KC) edges, (d) the carriers of the object-specific discharges.  Read-only; exact text/graph work.
# DECISION RULE (fixed before the first run, 19:04:06Z by date -u):
#  Scope of (a),(b): the K cluster that can name the pair carrier = CompositeDimension and every module whose import
#    closure contains it (t1 run 2: DenseOrbit, EffectSpace, K1Bridge, K2Guard, OddChar, ParityNot, RelcSelectBlock,
#    RelcSelectC5, RelcSelectParity, RelcSelectSqueeze, SharpTests; the root OIBridge has no P-token, t1 B2).
#    Declarations split at lines starting (after attributes/modifiers) with theorem|lemma|def|abbrev|structure|class|
#    instance|example; statement = text up to the first top-level ':=' (or ' where' for structures, whole text).
#  (a) CONE-BINDERS: declarations whose statement contains `Set (W` (a set of pair vectors).  Printed with kind.
#  (b) ACT-THEOREMS: theorems/lemmas whose statement contains the identifier actC or actT.  Each is tagged by the
#    shape of its conclusion (text after the first top-level ':' of the statement): EQ (contains '=' and no '∈'),
#    MEM (contains '∈'), FALSE (ends in False), OTHER.  A MEM-tagged theorem whose conclusion has an actC/actT term
#    followed by '∈' is printed as ACT-MEM for reading; the reading (antecedent of '→ False' = a no-go; conclusion =
#    a composite-action theorem) is recorded in TEST.md [W].
#  (c) Anc(P): BFS over ../G6/graph.tsv (read as data) from the seeds I3.1, I3.6, I3.7, I3.11, I3.43, I3.147-I3.153
#    along edges of kinds R, RA, RN, KC (src depends on dst); report the node count, the levels present (column
#    'level' of the node table; kernel declarations reached by RN/KC without a record are counted separately), and
#    every KC edge inside Anc(P).  ANC-PO iff every recorded node of Anc(P) has a level string made only of P and O.
#  (d) DISCHARGES: for each named theorem, its file:line, its module's closure contains CompositeDimension (yes/no),
#    and the carrier tokens in its statement (FiniteOperationalTheory, Matrix, substratumClass, substratumTheory,
#    ExactAllFiniteEndomorphicQuantumOps, HasCompositeUnitaryControl, MixC, W, maxCone, actC, actT).
#    DISCHARGE-OFF-P iff no discharge's module reaches CompositeDimension and no statement has a P-token.
#  Countercontrols: CC1 the (a) scan must find CandidateCone and no_candidateCone_cnot_reflY (K2Guard.lean:95, :143);
#    CC2 the (b) scan must find actT_prodState (K2Guard.lean:173) tagged EQ; CC3 a BFS from I1.1 (Axiom 1) along the
#    same edges reversed-from-seeds must not be needed -- instead: adding the synthetic edge I3.1 -> I1.1 must put an
#    H-level node into Anc(P) (detector live).
#  VERDICT D2-D3-SCAN printed with the counts iff CC1-CC3 behave; the verdict states facts, the reading is [W].
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', 'base'))
TREE = os.path.join(BASE, 'verification', 'lean-mathlib', 'OIBridge')
mods = {fn[:-5]: os.path.join(TREE, fn) for fn in sorted(os.listdir(TREE)) if fn.endswith('.lean')}
text = {m: open(p, encoding='utf-8').read() for m, p in mods.items()}
imp_re = re.compile(r'^import\s+OIBridge\.([A-Za-z0-9_]+)\s*$', re.M)
imports = {m: sorted(set(x for x in imp_re.findall(t) if x in mods)) for m, t in text.items()}
def closure(m):
    seen, st = set(), [m]
    while st:
        x = st.pop()
        if x in seen: continue
        seen.add(x); st.extend(imports.get(x, []))
    return seen
KCL = sorted(m for m in mods if 'CompositeDimension' in closure(m))
print('K cluster naming the pair carrier (%d): %s' % (len(KCL), ', '.join(KCL)))

decl_re = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?'
                     r'(theorem|lemma|def|abbrev|structure|class|instance|example)\s+([^\s(:{\[]+)', re.M)
def decls(m):
    t = text[m]
    ms = list(decl_re.finditer(t))
    out = []
    for i, mt in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        body = t[mt.start():end]
        line = t.count('\n', 0, mt.start()) + 1
        out.append((mt.group(1), mt.group(2), line, body))
    return out
def statement(kind, body):
    if kind in ('structure', 'class'): return body
    depth, i = 0, 0
    while i < len(body) - 1:
        c = body[i]
        if c in '([{⟨': depth += 1
        elif c in ')]}⟩': depth -= 1
        elif c == ':' and body[i + 1] == '=' and depth == 0: return body[:i]
        i += 1
    return body
def conclusion(st):
    depth = 0
    for i, c in enumerate(st):
        if c in '([{⟨': depth += 1
        elif c in ')]}⟩': depth -= 1
        elif c == ':' and depth == 0 and i > 0 and st[i + 1:i + 2] != '=':
            return st[i + 1:]
    return ''
squash = lambda s: re.sub(r'\s+', ' ', s).strip()
ACT = re.compile(r'\b(actC|actT)\b')
coneb, actthm = [], []
for m in KCL:
    for kind, name, line, body in decls(m):
        st = statement(kind, body)
        if 'Set (W' in st: coneb.append((m, line, kind, name))
        if kind in ('theorem', 'lemma') and ACT.search(st):
            con = squash(conclusion(st))
            tag = 'FALSE' if con.endswith('False') else ('MEM' if '∈' in con else ('EQ' if '=' in con else 'OTHER'))
            actmem = bool(re.search(r'\b(actC|actT)\b[^,]*∈', con))
            actthm.append((m, line, name, tag, actmem, con[:220]))
print('(a) CONE-BINDERS (%d):' % len(coneb))
for m, line, kind, name in coneb: print('  %s.lean:%d %s %s' % (m, line, kind, name))
tags = {}
for x in actthm: tags[x[3]] = tags.get(x[3], 0) + 1
print('(b) ACT-THEOREMS (%d): %s' % (len(actthm), ', '.join('%s %d' % (k, tags[k]) for k in sorted(tags))))
for m, line, name, tag, am, con in actthm:
    print('  %-5s %s %s.lean:%d %s :: %s' % (tag, 'ACT-MEM' if am else '-', m, line, name, con))
nam = sum(1 for x in actthm if x[4])
print('(b) ACT-MEM count: %d' % nam)

# (c) Anc(P) over G6's table
G = os.path.join(HERE, '..', 'G6', 'graph.tsv')
nodes, edges, sec = {}, [], None
for ln in open(G, encoding='utf-8'):
    ln = ln.rstrip('\n')
    if ln.startswith('#table nodes'): sec = 'n'; continue
    if ln.startswith('#table edges'): sec = 'e'; continue
    if ln.startswith('#') or not ln: continue
    f = ln.split('\t')
    if sec == 'n' and f[0] != 'id': nodes[f[0]] = f[3]
    if sec == 'e' and f[0] != 'src': edges.append((f[0], f[1], f[2]))
SEEDS = ['I3.1', 'I3.6', 'I3.7', 'I3.11', 'I3.43', 'I3.147', 'I3.148', 'I3.149', 'I3.150', 'I3.151', 'I3.152', 'I3.153']
KINDS = {'R', 'RA', 'RN', 'KC'}
def anc(extra=()):
    adj = {}
    for s, d, k in list(edges) + list(extra):
        if k in KINDS: adj.setdefault(s, []).append(d)
    seen, st = set(), list(SEEDS)
    while st:
        x = st.pop()
        if x in seen: continue
        seen.add(x); st.extend(adj.get(x, []))
    return seen
A = anc()
rec = sorted(x for x in A if x in nodes)
nonrec = sorted(x for x in A if x not in nodes)
lv = sorted(set(nodes[x] for x in rec))
anc_po = all(set(re.sub(r'[^A-Z]', '', nodes[x])) <= {'P', 'O'} for x in rec)
kc_in = sorted((s, d) for s, d, k in edges if k == 'KC' and s in A)
print('(c) Anc(P): %d nodes (%d inventory records, %d kernel declarations without a record)' % (len(A), len(rec), len(nonrec)))
print('(c) levels of the records: %s' % ' | '.join(lv))
print('(c) records: %s' % ', '.join(rec))
print('(c) non-record members: %s' % ', '.join(nonrec))
print('(c) KC edges with source in Anc(P) (%d): %s' % (len(kc_in), ', '.join('%s->%s' % e for e in kc_in)))
print('(c) ANC-PO: %s' % anc_po)
A2 = anc([('I3.1', 'I1.1', 'R')])
cc3 = any(x in nodes and 'H' in nodes[x] for x in A2)
print('CC3 synthetic edge I3.1 -> I1.1: Anc(P) %d nodes, H-level member present: %s' % (len(A2), cc3))

# (d) discharges
DIS = ['substratumClass_contextStable', 'mixC_contextStable', 'substratumClass_structurallyClosed',
       'hcompRealized_consistent_with_parallelReferenceExtension', 'layerFlowExecutable_of_control',
       'implementationLocality_of_qm', 'reversibleImplementationLocality_of_qm', 'embeddedObservation_of_qm',
       'genTheory_embeddedObservation', 'substratumTheory_derivedOI']
CAR = re.compile(r'\b(FiniteOperationalTheory|Matrix|substratumClass|substratumTheory|ExactAllFiniteEndomorphicQuantumOps|'
                 r'HasCompositeUnitaryControl|MixC|LabelInvariant|maxCone|actC|actT|cnot)\b|\bW [3d]\b')
offp = True
for n in DIS:
    found = [(m, line, kind, body) for m in sorted(mods) for kind, name, line, body in decls(m) if name == n]
    if not found:
        print('(d) %s NOT FOUND' % n); offp = False; continue
    for m, line, kind, body in found:
        st = squash(statement(kind, body))
        toks = sorted(set(x.group(0) for x in CAR.finditer(st)))
        reach = 'CompositeDimension' in closure(m)
        ptok = any(t in ('maxCone', 'actC', 'actT', 'cnot', 'W 3', 'W d') for t in toks)
        offp &= (not reach) and (not ptok)
        print('(d) %s.lean:%d %s | reaches CompositeDimension: %s | carrier tokens: %s' % (m, line, n, reach, ', '.join(toks) or '-'))
        print('      %s' % st[:300])
print('(d) DISCHARGE-OFF-P: %s' % offp)
cc1 = any(n == 'CandidateCone' for _, _, _, n in coneb) and any(n == 'no_candidateCone_cnot_reflY' for _, _, _, n in coneb)
cc2 = any(n == 'actT_prodState' and t == 'EQ' for _, _, n, t, _, _ in actthm)
print('CC1 cone-binder scan finds CandidateCone and no_candidateCone_cnot_reflY: %s' % cc1)
print('CC2 act scan finds actT_prodState tagged EQ: %s' % cc2)
print('CC3 detector live: %s' % cc3)
if cc1 and cc2 and cc3:
    print('VERDICT D2-D3-SCAN: cone-binders %d, act-theorems %d (ACT-MEM %d), Anc(P) %d nodes ANC-PO %s, '
          'DISCHARGE-OFF-P %s' % (len(coneb), len(actthm), nam, len(A), anc_po, offp))
else:
    print('VERDICT NONE: cc1=%s cc2=%s cc3=%s' % (cc1, cc2, cc3))
