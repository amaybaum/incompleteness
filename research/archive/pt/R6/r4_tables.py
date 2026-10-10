# r4_tables.py -- R6 node R4: the verdict tables, generated mechanically from R1's item list and the R2/R3/R5/R6 outputs.
# DECISION RULE (fixed before the first run, 18:29:08Z by date -u; the class rules are NOTES N3, fixed at 18:09Z):
#  Inputs: r1_inventory.out (APPL lines, VERDICT required), r2_cones.out, r3_seeds.out, r5_realization.out, r6_single.out
#  (each VERDICT line required; otherwise no table is printed).
#  Each applicable item is given a class (data below, one entry per I3 id; I4.236 'inh'; I1.17 and the 55 HMG-dna ids
#  'hmg'). Verdicts per column -- explicit cones K(E0), K(Z_F); the EXOTIC-E alternatives (one column, rows coincide);
#  the comparison object Q3 -- follow the class:
#   def  SATISFIES [K-indep]                 thm  SATISFIES [K-indep]          gate  SATISFIES [K-indep] (certified instance)
#   cone SATISFIES [cone]                    kthm SATISFIES [K] (its conclusion holds; checked C7 on the explicit cones)
#   dna  FAILS [hyp]  (a do-not-assume item: failure of a hypothesis, never an exclusion)
#   d4f  FAILS [hyp]  (a [D] four-token hypothesis, uniform assignment)   d4v SATISFIES (vacuous: its hypothesis fails)
#   d4s  SATISFIES [W]  nr   NOT REACHED (no bridge at L / no >= 3-token structure at L)   inh  SATISFIES [inherit]
#   b1   SATISFIES [inherit] through B1/B2 (fixes maxCone (eball 3), which bounds every alternative)
#   cand FAILS [hyp] (PT-record candidate H; T: FAILS for the explicit cones, UNDECIDED for EXOTIC-E)
#   hmg  NOT REACHED (levels H, M, G, X; no H->P, M->P, G->P bridge at L)
#  Q3 column: SATISFIES for every class except nr and hmg (NOT REACHED).
#  CONTROLS: (1) every APPL item has a class, and every class entry names an APPL item (no orphan, no gap); (2) the Q3
#  column contains no FAILS; (3) an item whose status begins 'proved [K]' or is a definition at L with verdict FAILS in
#  any column is listed as EXCLUDED-BY-L (none expected; listed, not hidden); (4) every FAILS row of the explicit cones
#  that cites a C8 map has that map with a WITNESS line in r2_cones.out for that cone; (5) the I3 class counts by
#  bearing reproduce R1's (80/25/20/17).
import re

R6 = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/R6'
def rd(n):
    with open(R6 + '/' + n, encoding='utf-8') as f: return f.read()
outs = {n: rd(n) for n in ['r1_inventory.out', 'r2_cones.out', 'r3_seeds.out', 'r5_realization.out', 'r6_single.out']}
green = {n: bool(re.search(r'^VERDICT ', t, re.M)) for n, t in outs.items()}
items = []
for l in outs['r1_inventory.out'].split('\n'):
    if l.startswith('APPL '):
        f = [x.strip() for x in l[5:].split(' | ')]
        items.append(dict(id=f[0], bcls=f[1], level=f[2], status=f[3], flag=f[4], title=f[5]))
# ---- class and evidence per item: id -> (class, evidence for explicit cones, evidence for EXOTIC-E, note)
D = {}
def put(ids, cls, ex, ee='', note=''):
    for i in ids.split():
        D['I3.' + i] = (cls, ex, ee if ee else ex, note)
put('1', 'def', '[K] CD:95-97; LT is encoded by the carrier (as for Q3)')
put('2 3 4 5', 'def', '[K] CD:160-195 (definitions)')
put('6 7', 'def', '[K] CD:197-202; [X] r2 D0c', note='invariance of K under a rotation: rows I3.150-153')
put('11', 'def', '[K] CD:741-798; [X] r2 D0a (cnot = Ad(CNOT), control first)')
put('49 113 143', 'def', '[K] definitions (I3.143 [D])')
put('115', 'def', '[K] CompositeInterface §E: LT is a theorem of the coordinate model W 3')
put('12', 'thm', '[K] CD:838-860; [X] r2 D1b, D1d, D1e')
put('13', 'thm', '[K] CD:1159; [X] r2 D1g')
put('14', 'thm', '[K] CD:1378; [X] r2 D1f')
put('15 16 17 20 22 25 26 27 28 30 32 33 34 41 42 46 120 121 122', 'thm', '[K] (statement does not quantify over K)')
put('185', 'thm', '[K] CD:1923-1931, K2Guard:172 (products only)')
put('9', 'gate', '[K] nativeGate_cnot CD:1159; [X] r2 D1b, D1d, D1g')
put('10', 'gate', '[K] entangling_cnot CD:1378; [X] r2 D1f')
put('23', 'gate', '[K] gateRel_cnot (ParityNot); [X] r2 D1b')
put('29', 'gate', '[K] ctrlGate_of_nativeGate RelcSelectBlock:53')
put('35', 'gate', '[W] from nativeGate_cnot: maxCone ⊆ maxConeOf avail for every effect-sound avail')
put('36', 'gate', '[W] = Entangling once maxConeOf avail = maxCone (B1); [K] entangling_cnot')
put('129', 'gate', '[D] NClass: cnot with identity locals (KT4-PREM-1 record, M_Q)')
put('43', 'cone', '[X] r2 C1 (H1), C5 (maxCone bound)', '[W] H1 from cone(G.SEP) ⊆ K; K = K* ⊆ SEP* = maxCone')
put('130', 'cone', '[X] r2 C1, C5; convex cone by construction', '[W] as I3.43; EBF output is a convex cone')
put('131', 'cone', '[A] SD1/SD2 closedness (AUDIT-X); [W] a self-dual cone is closed', '[W] a self-dual cone is closed')
put('132 148', 'cone', '[X] r2 C2 (level (i) for K(E0); level (ii) for K(Z_F))', '[W] cnot ∈ G-hat, G16 ⊆ G-hat (level (ii))')
put('147', 'cone', '[X] r2 C1 (symbolic SOS, whole ball)', '[W] cone(G-hat.SEP) ⊆ K')
put('149', 'cone', '[X] r2 C3 certificates + [A] SD1/SD2 (AUDIT-X)', '[A] EBF (AUDIT-X) over the r3 seed')
put('114 116 159', 'cone', '[W] over [X] r2 C1, C5, C6 (slice convex, compact, products inside, effects valid, unit pairing)', '[W] as for the explicit cones')
put('118 156', 'cone', '[X] r2 C2, C6, D1a (cnot preserves the body, involutive)', '[W] cnot ∈ G-hat')
put('44', 'kthm', '[K] K2Guard:143; [X] r2 C7 (actT reflY moves the cone)', '[K] K2Guard:143 (no node group contains actT reflY [W])')
put('137', 'dna', '[X] r2 C8 (rotation witnesses)', '[W] IE1 ⊇ (b_S4) ⇒ K = Q3 (stage 4 Y2 [A]); K ≠ Q3 [X] r3')
put('142', 'dna', '[X] r2 C8 (rot3 pi: K(E0); cyc3: K(Z_F))', '[W] {ball3Drive flow, J} forces Q3 (C5 census [A]); K ≠ Q3 [X] r3')
put('144', 'dna', '[X] r2 C4 (a pure state outside K); r2 CC twin (K ≠ twin)', '[X] r3 S (the seed excludes its own pure state)')
put('150', 'dna', '[X] r2 C8 actC rot3(pi) (K(E0)), actC cyc3 (K(Z_F))', '[W] stage 4 Y2 [A] + K ≠ Q3 [X] r3')
put('151', 'dna', '[X] r2 C8 actC R_n(pi/2), n = (3,0,4)/5', '[W] stage 4 Y3/Z z5 [A] + K ≠ Q3 [X] r3')
put('152', 'dna', '[X] r2 C8 actC R1 (-1; -2383/5316)', '[W] stage 4 Y7 [A] + K ≠ Q3 [X] r3')
put('153', 'dna', '[X] r2 C8 actC/actT nflip (flow members; K(E0)), actC cyc3 and actC Rx(pi/2) (K(Z_F))', '[W] C5 census / D5 B1 [A] + K ≠ Q3 [X] r3')
put('155', 'dna', '[W] FC ⟺ IE1 given hgate (stage 2 [A]); hgate holds (r2 C2), IE1 fails', '[W] as for the explicit cones')
put('165', 'dna', '[X] r2 C8 (its clause "local actions compatible with the composite cone")', '[W] as I3.150', note='other K2 clauses: LT encoded, cone exists')
put('133', 'd4f', '[D] Lemma B1 (FourCopyBridge:267) + [X] r2 C9 (FCC fails, uniform)', '[D] kt4_forward_ie1 + [W] stage 4: H ⇒ IE1 ⇒ Q3')
put('135', 'd4f', '[X] r2 C9 (uniform: min -1 for K(E0), -1/2 for K(Z_F))', '[D] Lemma B1 + kt4_forward_ie1 + [W] stage 4')
put('139 140', 'd4v', '[D] (vacuous: hypothesis H fails, I3.133)')
put('187', 'd4v', '[W] KT4-PREM-1 result.md:128 (vacuous: IE1 fails, I3.137)')
put('138', 'd4s', '[W] cnot with identity locals: every twist bit false')
put('134 136 141 154 157 158', 'nr', 'no structure with three or more tokens at L (EQ5-SOURCE §1; KT4-PREM-1 Q2)', note='not a function of the pair cone')
put('145', 'nr', 'absent bridge A3 (P-STAGE2 not at L); its cone consequence hcl: I3.131')
put('146', 'nr', 'absent bridge A4 (P-ACT2 not at L); cone consequence hgate: I3.132; idle-extension reading: I3.137')
put('96 99 104 105', 'nr', 'routed through the absent P-STAGE2/P-ACT2 (I3 bridge field); single-token content shared with Q3')
put('160', 'cand', '[A] stage 3 [W + L] (surgery cones not homogeneous); stage 4 Y6', '[W + L] stage 4 Y6: H ⇒ K = Q3; K ≠ Q3 [X] r3')
put('161', 'cand', '[A] stage 4 Y6 (extreme-ray invariant c = 15 on defects, 9 on products)', 'UNDECIDED (stage 4 T: EXCLUDES-ALL open)')
put('8', 'inh', '[K] isNot_nflip CD:838; [X] r2 D1e, r6 T3')
put('18 19 21 31 45 47 125 126 128', 'inh', '[K] (d = 3 for eball 3 with nflip, cnot)')
put('37 38', 'inh', '[K] K1Bridge:128, :138 (through B1)')
put('24', 'inh', '[K] ParityNot:161; [X] r6 T3 (nflip = pi-rotation about e1)')
put('39 40', 'inh', '[K] hasTwoSharpTests_iff SharpTests:155; [X] r6 T1')
put('69 173', 'inh', '[X] r6 T5; K∞-Copy open for Q3 likewise (one N built into NativeGate)')
put('76', 'inh', '[K] boundaryTransitive_fullAut3 OG:537, _ball3Drive ON:665; [X] r6 T6')
put('87 88 89 124 186', 'inh', '[K] TRB-1 / DIM-1 single-ball statements (the token is eball 3 = ball3)')
put('164', 'inh', '[K] dim1_core instance; K1 CONDITIONAL for Q3 likewise')
put('166', 'inh', 'K∞ OPEN for Q3 likewise (pair-blind)')
put('50 57 92 94 95 101 167 168', 'inh', 'pair-blind; open/assumed for Q3 likewise (no instance for ball3 at L)')
put('52 53 78 79 80 82 83 97 98 111 127', 'inh', '[K] single-body theorems (pair-blind)')
put('169', 'inh', '[K] ball3Drive KIF:449; [X] r6 T4; operational availability open for Q3 likewise')
put('48 51 54 55 56 58 60 74 75 170 172', 'b1', '[K] B1 EffectSpace:572 / B2 DenseOrbit:243 fix maxCone (eball 3); K ⊆ maxCone [X] r2 C5', '[K] B1/B2; K ⊆ maxCone [W]')
put('73 171', 'b1', '[K] B1; [X] r6 T2 (sharp seed on the ball); K ⊆ maxCone [X] r2 C5', '[K] B1; [X] r6 T2; K ⊆ maxCone [W]')
D['I4.236'] = ('inh', '[A] kn census §4; [X] r2 C10: the pair reading of SF fails for Q3 and the cones alike', '[A] kn census §4 (token = qubit ball)', '')
D['I1.17'] = ('hmg', 'I1 bridge field: none at L (Main.md:82)', 'I1 bridge field: none at L', '')
for it in items:
    if it['bcls'] == 'HMG-dna':
        D[it['id']] = ('hmg', 'level %s; no H→P, M→P or G→P bridge at L (AUDIT-I §5.2–5.3; r5 (a))' % it['level'], '', '')
TAG = {'def': 'SATISFIES [K-indep]', 'thm': 'SATISFIES [K-indep]', 'gate': 'SATISFIES [K-indep]', 'cone': 'SATISFIES [cone]',
       'kthm': 'SATISFIES [K]', 'dna': 'FAILS [hyp]', 'd4f': 'FAILS [hyp]', 'd4v': 'SATISFIES (vacuous)', 'd4s': 'SATISFIES',
       'nr': 'NOT REACHED', 'inh': 'SATISFIES [inherit]', 'b1': 'SATISFIES [inherit]', 'cand': 'FAILS [hyp]', 'hmg': 'NOT REACHED'}
def verdict(cid, cls, col):
    if col == 'Q3':
        return 'NOT REACHED' if cls in ('nr', 'hmg') else 'SATISFIES'
    if cls == 'cand' and cid == 'I3.161' and col == 'E':
        return 'UNDECIDED'
    return TAG[cls]
COLS = ['K(E0)', 'K(Z_F)', 'E', 'Q3']
ok = {}
ok['inputs green'] = all(green.values())
ids_appl = [it['id'] for it in items]
ok['(1) every item classed'] = all(i in D for i in ids_appl) and all(k in ids_appl for k in D)
rows = []
for it in items:
    cid = it['id']; cls, ex, ee, note = D.get(cid, ('?', '', '', ''))
    v = {c: verdict(cid, cls, c) for c in COLS}
    rows.append((cid, cls, it, v, ex, ee, note))
ok['(2) Q3 column has no FAILS'] = all(not r[3]['Q3'].startswith('FAILS') for r in rows)
excl = [r[0] for r in rows if any(r[3][c].startswith('FAILS') for c in COLS[:3])
        and (r[2]['status'].startswith('proved [K]') or '(definition' in r[2]['status'])]
print('EXCLUDED-BY-L (FAILS on a proved [K] item or a definition at L):', excl if excl else 'none')
r2 = outs['r2_cones.out']
need = [('K(E0)', 'actC rot3(pi)'), ('K(E0)', 'actC R_n(pi/2)'), ('K(E0)', 'actC R1'), ('K(E0)', 'actC nflip'), ('K(E0)', 'actT nflip'),
        ('K(Z_F)', 'actC cyc3'), ('K(Z_F)', 'actC Rx(pi/2)'), ('K(Z_F)', 'actC R_n(pi/2)'), ('K(Z_F)', 'actC R1')]
ok['(4) C8 witnesses present'] = all(re.search(r'^MAP %s\s+%s: WITNESS' % (re.escape(m), re.escape(k)), r2, re.M) for k, m in need)
ok['(4b) FCC fails both'] = 'C9 FCC fails K(E0)         PASS' in r2 and 'C9 FCC fails K(Z_F)        PASS' in r2
cnt = {}
for it in items:
    if it['id'].startswith('I3.'): cnt[it['bcls']] = cnt.get(it['bcls'], 0) + 1
ok['(5) I3 bearing counts'] = cnt == {'direct': 80, 'inherits': 25, 'notread': 20, 'bridge': 17}
def cut(x, n): x = re.sub(r'\s+', ' ', x); return x if len(x) <= n else x[:n - 1] + '…'
def table(col, title, evcol):
    print('\n### %s\n' % title)
    print('| item | statement (one line) | class | verdict | evidence |')
    print('|---|---|---|---|---|')
    for cid, cls, it, v, ex, ee, note in rows:
        ev = ex if evcol == 'ex' else ee
        st = cut(it['title'], 64) + (' — ' + note if note else '')
        print('| %s | %s | %s | %s | %s |' % (cid, st.replace('|', '/'), cls, v[col], cut(ev, 120).replace('|', '/')))
table('K(E0)', 'Table A1 — K(E0) = (Q3 ∩ E0*) + R+E0, level (i)', 'ex')
table('K(Z_F)', 'Table A2 — K(Z_F) = (Q3 ∩ Z_F*) + cone Z_F, level (ii) (also the explicit cone of every subgroup of Stab_Cl(Z_F))', 'ex')
table('E', 'Table A3 — every EXOTIC-E alternative (stage-4 Y4, Y5, Z seeds; stage-5 C5 census, κ and D5 seeds; S2 and the finite groups)', 'ee')
print('\n### Table A3-seeds — the alternative-specific rows of Table A3\n')
print('| alternative | node group (level (ii)) | seed (exact) | r3 check | recomputed here | cited [A] |')
print('|---|---|---|---|---|---|')
SEEDROWS = [
 ('A3a Y4', 'S3: actC Rx with G16; the native drive on one or both tokens', 'c = 4609/4608 at φ0 = (1,2,3i,−1+i)', 'S A3a; R-a', 'X⊗X forms 1/9, 121/42', 'reduction to {φ0, CNOTφ0} (Y4)'),
 ('A3b Y5', 'S1 ⟨G16, SWAP⟩; S2 reachable set G16·SEP; the listed finite extensions', 'c = 517/512, d_min = 5/256', 'S A3b; R-b', 'G16, ⟨G16,SWAP⟩ orbit minima 5/256', 'Clifford census 23040 (Y5 F1–F5)'),
 ('A3c Z', 'S3: actC Rx with G16', 'α = 7/8 at ψ_a = (15,−1,7,7)/18', 'S A3c; R-e', 'V-coefficients, f ≤ 7/8', 'reachable-set formula (Z z3)'),
 ('A4a C5 1/2304', '{flow}@C (drive about x on the control) with G16', 'α = 499783/500000 at φ0', 'S A4a 1/2304; R-a', 'as A3a', 'reduction (C5 census)'),
 ('A4a C5 5/256', '{J}, {NOT, J} on either token; {flow}@T; native finite groups', 'α = 122509/125000 at φ0', 'S A4a 5/256; R-b', 'orbits 768 / 384, min 5/256', '—'),
 ('A4a C5 1/8704', 'ball3Drive flow on the target (Z⊗Z torus) with G16', 'c = 17409/17408 at φ0', 'S A4a 1/8704; R-c', 'Z⊗Z bound 1/8704 (sharp)', 'reduction (C5 S4)'),
 ('A4b κ / A5 S2', 'κ: Ad U(w) with G16; S2: actC Rz ∘ actT Rx with G16 (and ⟨T³, G16⟩)', 'Bell seed F = z_(−1,−1) on C1 ∪ C2', 'S A4b; R-g', 'circles invariant, maximally entangled', 'EBF (AUDIT-X)'),
 ('A4c D5', 'the substratum monomial class (with cnot, SWAP, T)', 'c = 513/512 at (1,2,3,4)/√30', 'S A4c; R-d', 'min arrangement |det| 1/15', 'σ_max arrangement bound (D5 C)'),
 ('A5 G_S', '⟨G16, Ad(S⊗I)⟩ (32)', 'Bell seed e_F, orbit of 8', 'R-h', 'orbit 8, overlaps {0, 1/2}', 'EBF'),
 ('A5 G_H', '⟨G16, Ad(I⊗H)⟩ (128)', 'α = 9/10 at ψ_a', 'S A5 G_H; R-f', 'm = 4160/6561 (32 rays)', '—'),
 ('A5 G_Cl', 'Clifford ∪ Clifford∘T (23040)', 'α = 99/100 at ψ_a', 'S A5 G_Cl', 'window given m', 'm = 6272/6561 (Z z4)'),
 ('A5 any finite group', 'every finite group ⊇ G16', 'Y5 seed (or the group\'s own)', '—', '—', 'dimension corollary [W] (Y1.5, Z claim D)')]
for r in SEEDROWS: print('| ' + ' | '.join(r) + ' |')
r3 = outs['r3_seeds.out']
ok['(6) r3 seed lines PASS'] = all(('CHECK S %s' % k) in r3 for k in ['A3a', 'A3b', 'A3c', 'A4a C5 d_low=1/2304', 'A4a C5 d_low=5/256',
                                                                        'A4a C5 d_low=1/8704', 'A4b', 'A4c', 'A5 G_H', 'A5 G_Cl']) \
    and 'FAIL' not in ''.join(l for l in r3.split('\n') if l.startswith('CHECK S '))
print('\n### Tally\n')
for c in COLS:
    t = {}
    for r in rows:
        k = r[3][c].split(' ')[0]; t[k] = t.get(k, 0) + 1
    print('TALLY %-7s %s' % (c, dict(sorted(t.items()))))
for k, v in ok.items(): print('CHECK', k, 'PASS' if v else 'FAIL')
if all(ok.values()):
    print('VERDICT R4-TABLES-EXACT: %d items x 3 alternative columns + Q3; excluded by L: %s; Q3 fails nothing; controls green'
          % (len(rows), 'none' if not excl else ', '.join(excl)))
else:
    print('NO VERDICT')
