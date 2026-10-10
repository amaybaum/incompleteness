# c1_rows.py -- research/countermodels node C1: the row-by-row reassessment of K_F2 = K({F, cnot F}) and K(e_c),
# c in (1/2, 1], against the 199 applicable items of stage 6 (R6's Tables A1/A2 as the template; the reference rows
# pt/audit/stage6-inputs/T-audit/r6_rows.tsv), generated from the exact checks of c1_cones.out.
# DECISION RULE (fixed before the first run, 2026-10-10T20:16:07Z by date -u):
#  Inputs (read-only): ../../archive/pt/audit/stage6-inputs/T-audit/r6_rows.tsv (597 rows: table, id, class, verdict);
#  ../../archive/pt/R6/REASSESSMENT.md (Table A1 and A2 lines: statement, class, verdict, evidence);
#  ../../archive/pt/R6/r1_inventory.out (APPL lines: status at L); c1_cones.out (must carry VERDICT C1-CONES-EXACT).
#  Class rules (R6's, NOTES N3 of R6, unchanged): def/thm/gate SATISFIES [K-indep]; inh/b1 SATISFIES [inherit] (b1 through
#  the maxCone bound, checked per cone); cone SATISFIES [cone]; kthm SATISFIES [K]; dna/d4f/cand FAILS [hyp]; d4v
#  SATISFIES (vacuous); d4s SATISFIES [W]; nr/hmg NOT REACHED. A K-dependent verdict is assigned only if every check id it
#  cites is a PASS line of c1_cones.out (otherwise the row prints UNSUPPORTED and the rule below fails).
#  CONTROLS: (1) the A1 and A2 reference rows agree id by id (class and verdict) and number 199; (2) every row of the two
#  new columns has a verdict and every cited check id is PASS; (3) any FAILS row whose status at L begins "proved" or is a
#  definition is listed as EXCLUDED-BY-L (none expected; listed, not hidden); (4) the tallies are printed per column.
#  OUTCOME: COVERING-CONFIRMED iff every row's verdict for both cones equals the reference verdict, no EXCLUDED-BY-L row
#  exists, and the K-dependent rows are all backed by PASS lines; COVERING-REFUTED if some item at L (status proved or a
#  definition) is FAILED by either cone, or some reference SATISFIES row fails; otherwise (a hypothesis row differs)
#  COVERING-CONFIRMED-WITH-DIFFERENCES, the differing rows listed. Separately, the rows the covering argument of AUDIT-R §4
#  does not decide by itself (the cone-specific computations: cand T, the dna witnesses, d4f) are listed with the check that
#  decides them.
import re

ARC = '../../archive/pt/'
def rd(p):
    with open(p, encoding='utf-8') as f: return f.read()
ref = {}
for l in rd(ARC + 'audit/stage6-inputs/T-audit/r6_rows.tsv').strip().split('\n')[1:]:
    t, i, c, v = l.split('\t'); ref.setdefault(t, {})[i] = (c, v)
status = {}
for l in rd(ARC + 'R6/r1_inventory.out').split('\n'):
    if l.startswith('APPL '):
        f = [x.strip() for x in l[5:].split(' | ')]; status[f[0]] = f[3]
rea = rd(ARC + 'R6/REASSESSMENT.md')
def table_rows(title):
    blk = rea.split(title, 1)[1].split('\n### ', 1)[0]
    rows = {}
    for l in blk.split('\n'):
        if l.startswith('| I'):
            f = [x.strip() for x in l.strip('|').split(' | ')]
            rows[f[0]] = dict(stmt=f[1], cls=f[2], verdict=f[3], ev=f[4])
    return rows
A1 = table_rows('### Table A1'); A2 = table_rows('### Table A2')
out = rd('c1_cones.out')
PASS = set(re.findall(r'^CHECK (.+?)\s+PASS', out, re.M))
FAILL = set(re.findall(r'^CHECK (.+?)\s+FAIL', out, re.M))
green = bool(re.search(r'^VERDICT C1-CONES-EXACT', out, re.M))
maplines = re.findall(r'^MAP (.+?)\s+(F2|EC): (\S+)(.*)$', out, re.M)

ctl = {}
ctl['1 references agree'] = (set(ref['A1']) == set(ref['A2']) and len(ref['A1']) == 199 and
                             all(ref['A1'][i] == ref['A2'][i] for i in ref['A1']) and set(A1) == set(ref['A1']) == set(A2))
ctl['0 c1_cones green'] = green
ids = sorted(ref['A1'], key=lambda x: (x.split('.')[0], int(x.split('.')[1])))
ORDER = [i for i in A1]          # R6's printed order

R6MAP = {'D0a': 'D0a', 'D0b': 'D0b', 'D0c': 'D0b', 'D0e': 'D0c', 'D1a': 'D1a', 'D1b': 'D1b', 'D1d': 'D1c', 'D1e': 'D1d',
         'D1f': 'D1e', 'D1g': 'D1f', 'D1h': 'D1g'}
MYD = {'D0a': 'D0a cnot=Ad(CNOT)', 'D0b': 'D0b actC/actT=Ad', 'D0c': 'D0c transposeW=T', 'D1a': 'D1a cnot invol/sym',
       'D1b': 'D1b relT,relC nflip', 'D1c': 'D1c frame', 'D1d': 'D1d IsNot nflip', 'D1e': 'D1e entangling image',
       'D1f': 'D1f posFwd identity', 'D1g': 'D1g pW(prod)=rho(x)rho(y)'}
def kindep_ev(i):
    ev = A1[i]['ev']; cites = []
    for m in re.findall(r'r2 (D\d[a-h])', ev):
        if m in R6MAP: cites.append(MYD[R6MAP[m]])
    for m in re.findall(r', (D\d[a-h])', ev):
        if m in R6MAP: cites.append(MYD[R6MAP[m]])
    return 'R6 A1/A2: ' + ev + ('; re-checked: c1 ' + ', '.join(sorted(set(cites))) if cites else ''), sorted(set(cites))

def cone_rule(i, tag):
    # returns (verdict, evidence, [check ids])
    T = tag
    c = lambda *k: ['%s-%s' % (T, x) for x in k]
    rules = {
        'I3.43': ('SATISFIES [cone]', 'H1 and the maxCone bound', c('C1 H1', 'C5 maxCone')),
        'I3.114': ('SATISFIES [cone]', '[W] over the slice checks (convex, compact, products inside, effects valid, unit pairing)', c('C1 H1', 'C5 maxCone', 'C6 slice')),
        'I3.116': ('SATISFIES [cone]', '[W] over the slice checks', c('C1 H1', 'C5 maxCone', 'C6 slice')),
        'I3.159': ('SATISFIES [cone]', '[W] over the slice checks', c('C1 H1', 'C5 maxCone', 'C6 slice')),
        'I3.118': ('SATISFIES [cone]', 'cnot preserves the body, involutive', c('C2 cnot permutes Z', 'C6 slice') + ['D1a cnot invol/sym']),
        'I3.156': ('SATISFIES [cone]', 'cnot preserves the body, involutive', c('C2 cnot permutes Z', 'C6 slice') + ['D1a cnot invol/sym']),
        'I3.130': ('SATISFIES [cone]', 'convex cone by construction; H1; maxCone bound', c('C1 H1', 'C5 maxCone')),
        'I3.131': ('SATISFIES [cone]', '[A] SD1/SD2 closedness (AUDIT-X); [W] a self-dual cone is closed', c('C3 H3 certificate')),
        'I3.132': ('SATISFIES [cone]', 'level (i) (level (ii) fails, record)', c('C2 cnot permutes Z', 'C2 record level (ii) fails')),
        'I3.148': ('SATISFIES [cone]', 'level (i) (level (ii) fails, record)', c('C2 cnot permutes Z', 'C2 record level (ii) fails')),
        'I3.147': ('SATISFIES [cone]', 'symbolic SOS over the whole ball', c('C1 H1')),
        'I3.149': ('SATISFIES [cone]', 'certificates of SD1/SD2 and Theorem S + [A] their proofs (AUDIT-X, AUDIT-U)'
                   + ('; T6 §3.3 proof applies verbatim to a subset of Z_F' if T == 'F2' else '; X characterization (c in (1/2, 1])'),
                   c('C3 H3 certificate') + (c('C3 one-violation identity') if T == 'F2' else [])),
        'I3.44': ('SATISFIES [K]', '[K] K2Guard:143; actT reflY moves the cone', c('C7 actT reflY moves K')),
        'I3.137': ('FAILS [hyp]', 'local rotation witnesses (MAP lines)', c('C8 IE1 (I3.137)')),
        'I3.142': ('FAILS [hyp]', 'drive-word witness on some token', c('C8 IE1Drive (I3.142)')),
        'I3.144': ('FAILS [hyp]', 'a pure state outside K; K != twin (cnot-invariant; twin is not, CC5)', c('C4 K != Q3') + ['CC5 twin fails H2; Q3 not reflY-invariant']),
        'I3.150': ('FAILS [hyp]', 'witnesses on the control and on the target', c('C8 b_S4 control (I3.150)', 'C8 b_S4 target (I3.150)')),
        'I3.151': ('FAILS [hyp]', 'actC R_n(pi/2), n = (3,0,4)/5', c('C8 b_n actC (I3.151)')),
        'I3.152': ('FAILS [hyp]', 'actC R1 (order 3 about (5,1,1))', c('C8 b_R1 actC (I3.152)')),
        'I3.153': ('FAILS [hyp]', 'drive/J witnesses on the control and on the target', c('C8 b_DJ control (I3.153)', 'C8 b_DJ target (I3.153)')),
        'I3.155': ('FAILS [hyp]', '[W] FC <=> IE1 given hgate (stage 2 [A]); hgate holds, IE1 fails', c('C2 cnot permutes Z', 'C8 IE1 (I3.137)')),
        'I3.165': ('FAILS [hyp]', 'its clause "local actions compatible with the composite cone"', c('C8 K2 clause (I3.165)')),
        'I3.133': ('FAILS [hyp]', '[D] Lemma B1 (FourCopyBridge:267): H => FCC; FCC fails', c('C9 FCC fails') if T == 'F2' else ['EC-C9 FCC fails for all c']),
        'I3.135': ('FAILS [hyp]', ('uniform assignment, exact (min -1/2)' if T == 'F2' else
                                   'uniform assignment, exact for every c: famI = 1 - 2c at one tuple of e_c and (cnot-)products'),
                   c('C9 FCC fails') if T == 'F2' else ['EC-C9 FCC fails at c = 1', 'EC-C9 FCC fails for all c']),
        'I3.160': ('FAILS [hyp]', '[A] stage 3 X1 / stage 4 Y6 [W + L]: a homogeneous cone with H1-H3 is Q3; K != Q3', c('C4 K != Q3')),
        'I3.161': ('FAILS [hyp]', 'c = 15 on the defect, 9 on P00; automorphisms of a self-dual cone preserve c on extreme rays ([A] Y6)',
                   c('T c(F) = 15', 'T c(P00) = 9') if T == 'F2' else
                   ['EC-T c(e_c) = 15 at c = %s' % x for x in ('5/8', '3/4', '1')] + ['EC-T c(P00) = 9 at c = %s' % x for x in ('5/8', '3/4', '1')]),
    }
    return rules.get(i)

def assign(i, tag):
    cls = ref['A1'][i][0]
    if cls in ('def', 'thm', 'gate'):
        ev, cites = kindep_ev(i); return ('SATISFIES [K-indep]', ev, cites)
    if cls == 'inh':
        return ('SATISFIES [inherit]', 'R6 A1/A2: ' + A1[i]['ev'] + ' (single-token; the tokens are those of Q3)', [])
    if cls == 'b1':
        return ('SATISFIES [inherit]', 'B1/B2 fix maxCone (eball 3); K ⊆ maxCone', ['%s-C5 maxCone' % tag])
    if cls in ('nr', 'hmg'):
        return ('NOT REACHED', 'R6 A1/A2: ' + A1[i]['ev'] + ' (K-independent)', [])
    if cls == 'd4s':
        return ('SATISFIES', '[W] cnot with identity locals: every twist bit false (K-blind)', [])
    if cls == 'd4v':
        if i == 'I3.187':
            return ('SATISFIES (vacuous)', '[W] KT4-PREM-1 result.md:128 (vacuous: IE1 fails, I3.137)', ['%s-C8 IE1 (I3.137)' % tag])
        return ('SATISFIES (vacuous)', '[D] (vacuous: hypothesis H fails, I3.133)', (['%s-C9 FCC fails' % tag] if tag == 'F2'
                else ['EC-C9 FCC fails for all c']))
    r = cone_rule(i, tag)
    if r is None: return ('UNASSIGNED', '', [])
    return r

def norm(v): return v.split(' [')[0].split(' (')[0]
cols = {'F2': {}, 'EC': {}}
unsupported = []
for tag in cols:
    for i in ORDER:
        v, ev, cites = assign(i, tag)
        bad = [x for x in cites if x not in PASS]
        if bad or v == 'UNASSIGNED':
            unsupported.append((tag, i, bad)); v = 'UNSUPPORTED'
        cols[tag][i] = (v, ev, cites)
ctl['2 every row assigned and backed'] = not unsupported
excl = [(tag, i) for tag in cols for i in ORDER if cols[tag][i][0].startswith('FAILS') and
        (status[i].startswith('proved') or '(definition)' in status[i] or status[i].startswith('definition'))]
ctl['3 EXCLUDED-BY-L listed (none expected)'] = not excl
diff = [(tag, i, cols[tag][i][0], ref['A1'][i][1]) for tag in cols for i in ORDER if norm(cols[tag][i][0]) != norm(ref['A1'][i][1])]

# ---- print the tables
names = {'F2': 'K_F2 = K({F, cnot F}) = (Q3 ∩ {F, cnot F}*) + cone{F, cnot F}, F = z_(-1,-1), level (i)',
         'EC': 'K(e_c) = (Q3 ∩ e_c*) + R+ e_c, e_c = E00 + c(E13 - E22), every c in (1/2, 1], level (i)'}
for tag in cols:
    print('### Table C1-%s — %s' % (tag, names[tag]))
    print('| item | statement (R6) | class | verdict | evidence | reference (R6 A1 = A2) |')
    print('|---|---|---|---|---|---|')
    for i in ORDER:
        v, ev, cites = cols[tag][i]
        cit = ('; [X] c1_cones.out: ' + ', '.join(cites)) if cites else ''
        print('| %s | %s | %s | %s | %s%s | %s |' % (i, A1[i]['stmt'], ref['A1'][i][0], v, ev, cit, ref['A1'][i][1]))
    print()
for tag in cols:
    tally = {}
    for i in ORDER: tally[norm(cols[tag][i][0])] = tally.get(norm(cols[tag][i][0]), 0) + 1
    print('TALLY %s: %s' % (tag, ', '.join('%s %d' % (k, tally[k]) for k in sorted(tally))))
tr = {}
for i in ORDER: tr[norm(ref['A1'][i][1])] = tr.get(norm(ref['A1'][i][1]), 0) + 1
print('TALLY reference A1 = A2: %s' % ', '.join('%s %d' % (k, tr[k]) for k in sorted(tr)))
print('MAP lines read from c1_cones.out: %d' % len(maplines))
for k in sorted(ctl): print('CONTROL %-40s %s' % (k, 'OK' if ctl[k] else 'FAILED'))
for tag, i, bad in unsupported: print('UNSUPPORTED %s %s: %s' % (tag, i, bad))
for tag, i in excl: print('EXCLUDED-BY-L %s %s' % (tag, i))
for d in diff: print('DIFFERS %s %s: %s vs reference %s' % d)
cone_specific = [(i, ref['A1'][i][0]) for i in ORDER if ref['A1'][i][0] in ('cand', 'dna', 'd4f', 'cone', 'kthm', 'b1', 'd4v')]
print('ROWS DECIDED BY CONE-SPECIFIC CHECKS (not by the covering argument alone): %d -- %s' %
      (len(cone_specific), ', '.join('%s(%s)' % x for x in cone_specific)))
if not all(ctl.values()):
    print('NO OUTCOME (a control failed)')
elif excl or any(norm(r) == 'SATISFIES' and norm(v) != 'SATISFIES' for _, _, v, r in diff):
    print('OUTCOME COVERING-REFUTED')
elif diff:
    print('OUTCOME COVERING-CONFIRMED-WITH-DIFFERENCES')
else:
    print('OUTCOME COVERING-CONFIRMED: K_F2 and K(e_c) (every c in (1/2, 1]) receive the reference verdict on all 199 rows; '
          'no item at L excludes either cone; every FAILS row is a hypothesis')
