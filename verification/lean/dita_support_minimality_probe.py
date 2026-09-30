"""dita_support_minimality_probe.py -- act 42's exact-computation layer.

Runs the frozen tools in verification/lean/a42/ (exact arithmetic throughout, SAT verdicts from CaDiCaL through
python-sat) and asserts every value the preregistration freezes. One part per CI shard:

  every run          witness     R1 via class support, R2 path B(i), R3 exact class supports, C6, lemmas L1-L4, ctrl16
                     d01span     the {0,1} census below 48 (dfs01), Lemma P on its leaves, the zero-row span lemma at 77
  dispatch only      paths       R2 path A (landed production machinery) and path B(ii) (landed independent census)
                     r5          act 38's families xA+yB+zC and xP+yQ+zT
                     n18:K       K in 0..2: the N18 subspaces STRUCTS[K::3] against A41's corrected triples
                     dfs:K       K in 0..5: the <= 39 zero-row DFS on the row sets Rle13_39[K::6]
                     sathr       the <= 39 zero-row, r >= 14 SAT case
                     cubes:K     K in 0..2: the <= 39 no-zero-line SAT cubes [K::3]

Usage: python3 dita_support_minimality_probe.py --part <part>   (run from any directory)
Exit 1 on any mismatch. Ends with `dita_support_minimality_probe <part>: OK -- ...` or `... FAILED ...`.
"""
import hashlib, itertools, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, 'a42')
FAILS, COUNT = [], [0]


def check(name, cond):
    COUNT[0] += 1
    print(('PASS ' if cond else 'FAIL ') + name, flush=True)
    if not cond:
        FAILS.append(name)


def run(*args):
    t0 = time.time()
    r = subprocess.run([sys.executable] + list(args), cwd=TOOLS, capture_output=True, text=True)
    print('  [%s: exit %d, %.0fs]' % (' '.join(args), r.returncode, time.time() - t0), flush=True)
    if r.returncode != 0:
        print(r.stdout[-2000:], r.stderr[-2000:])
    return r


def jload(name):
    return json.load(open(os.path.join(TOOLS, name)))


def ensure_msize():
    if not os.path.exists(os.path.join(TOOLS, 'msize.npy')):
        run('cvsize.py')
    f = os.path.join(TOOLS, 'msize.npy')
    check('msize tables (cvsize.py) replay: sha256 %s' % MSIZE_SHA256[:12],
          os.path.exists(f) and hashlib.sha256(open(f, 'rb').read()).hexdigest() == MSIZE_SHA256)


# ---- every run ----------------------------------------------------------------------------------------------------
def part_witness():
    r = run('r3_run.py')
    d = jload('r3.json')
    check('R3 exact class support: E40 40, act 38 witness 44, A 16',
          r.returncode == 0 and (d['E40']['class_support'], d['act38_E']['class_support'], d['A']['class_support']) == (40, 44, 16))
    check('R3 representatives: E40 entries {-1,0,1} support 40; act 38 entries {-2..1} support 44',
          d['E40']['rep_support'] == 40 and d['E40']['rep_entries'] == [-1, 0, 1]
          and d['act38_E']['rep_support'] == 44 and d['act38_E']['rep_entries'] == [-2, -1, 0, 1])
    r = run('r2b_independent.py')
    d = jload('r2b.json')
    check('C1c independent enumeration: 20 partition structures, 976 triples, equal to L41 strict and relaxed',
          r.returncode == 0 and d['partitions'] == 20 and d['triples'] == 976
          and d['C1c_equals_L41_strict_census'] and d['C1c_equals_L41_relaxed_census'])
    check('C5 sorted alignment: 18', d['C5_sorted_partitions'] == 18)
    check('C3 gauge annihilated; zero in every triple', d['C3_gauge_annihilated'] and d['zero_in_all'])
    m = d['members']
    check('R2 B(i): E40, gauged E40 and act 38 witness in 0 triples',
          m['E40']['count'] == 0 and m['E40_gauge']['count'] == 0 and m['act38_E']['count'] == 0)
    check('C2 B(i): A 596, B 272, C 576, P 272, Q 596, T 596, -P+Q 128, -P-T 128, Q-T 256 triples',
          [m[k]['count'] for k in ('A', 'B', 'C', 'P', 'Q', 'T', '-P+Q', '-P-T', 'Q-T')]
          == [596, 272, 576, 272, 596, 596, 128, 128, 256])
    r = run('c6_control.py')
    check('C6: 150 instances, 146 equal at box 4, 4 gaps all closed at box 8, exact never above brute force',
          'C6: 150 instances; 146 equal at box 4; 4 gaps, 4 closed at box 8; exact above brute: 0' in r.stdout)
    ensure_msize()
    r = run('lemmas42.py')
    check('lemmas L1-L4 on A, B, C and the act 38 witness: ALL PASS', r.returncode == 0 and 'ALL PASS' in r.stdout
          and 'FAIL' not in r.stdout)
    r = run('ctrl16.py')
    check('ctrl16: 896 leaves at budget 16, all in N18; A, B, C, -A present',
          'leaves 896 all in N18 True' in r.stdout and all('%s present True' % x in r.stdout for x in ('A', 'B', 'C', '-A')))


def part_d01span():
    ensure_msize()
    r = run('dfs01.py', '47', 'zero', 'd01_zero.pkl')
    check('D01 zero, budget 47: 12520 leaves, supports 16 (176) and 32 (12344), all in N18',
          'zero budget 47 leaves 12520 hist (support, in some census subspace): [((16, True), 176), ((32, True), 12344)]' in r.stdout)
    r = run('dfs01.py', '32', 'two', 'd01_two.pkl')
    check('D01 two, budget 32: 288 leaves, support 32, all in N18',
          'two budget 32 leaves 288 hist (support, in some census subspace): [((32, True), 288)]' in r.stdout)
    r = run('lemmas42.py', 'd01_two.pkl', 'd01_zero.pkl')
    check('Lemma P on all 12808 D01 leaves (288 + 12520): ALL PASS',
          'PASS L4 Lemma P on all 288 leaves of d01_two.pkl: 288' in r.stdout
          and 'PASS L4 Lemma P on all 12520 leaves of d01_zero.pkl: 12520' in r.stdout and 'ALL PASS' in r.stdout)
    r = run('spanAll.py', '77')
    check('spanAll 77: 65390 row sets, 13922 dead, least live LB 24',
          'R sets 65390 dead 13922 alive 51468' in r.stdout and 'min LB among alive: 24' in r.stdout)
    check('spanAll 77: every row set with LB < 24 dead (dead by LB starts (16, 50); alive by LB starts (24, 140))',
          'dead by LB: [(16, 50),' in r.stdout and 'alive by LB: [(24, 140),' in r.stdout)


def part_wlog():
    ensure_msize()
    sys.path.insert(0, TOOLS)
    os.chdir(TOOLS)
    import random
    import numpy as np
    import lib42 as L
    from pysat.solvers import Cadical153
    from sat42 import Enc
    FULL = (1 << 16) - 1
    msize = np.load('msize.npy')
    lb = {}
    for R in range(1, FULL + 1):
        Z = FULL ^ R
        lb[R] = sum(int(msize[i, Z]) for i in range(16) if (R >> i) & 1)
    low = sorted(R for R in lb if 2 <= bin(R).count('1') <= 13 and lb[R] <= 39)
    high = [R for R in lb if bin(R).count('1') in (14, 15) and lb[R] <= 39]
    Rall = [int(x) for x in open('Rle13_39.txt').read().split()]
    check('W1 the DFS row sets are exactly the %d sets R with 2 <= |R| <= 13 and LB(R) <= 39' % len(low),
          sorted(Rall) == low and len(low) == 5494 and len(set(Rall)) == len(Rall))
    check('W1 row sets with a zero row, |R| >= 14 and LB(R) <= 39, left to sat_hr: %d' % len(high), len(high) == WLOG_HIGH)
    check('W2 one nonzero row against fifteen zero rows: least vanishing column set 16 for every row',
          all(int(msize[i, FULL ^ (1 << i)]) == 16 for i in range(16)))
    lines = trans = 0
    for p_, s_ in L.elems:
        rho = [p_[16 * i] // 16 for i in range(16)]; gam = [p_[j] % 16 for j in range(16)]
        if all(p_[16 * i + j] == 16 * rho[i] + gam[j] for i in range(16) for j in range(16)):
            lines += 1
        else:
            rho = [p_[16 * i] % 16 for i in range(16)]; gam = [p_[j] // 16 for j in range(16)]
            if all(p_[16 * i + j] == 16 * gam[j] + rho[i] for i in range(16) for j in range(16)):
                lines += 1; trans += 1
    check('W3 every one of the %d stabilizer elements maps lines to lines; %d transpose' % (len(L.elems), trans),
          len(L.elems) == 1024 and lines == 1024 and trans == 512)
    orbit = {p_[0] // 16 for p_, s_ in L.elems if all(p_[j] // 16 == p_[0] // 16 for j in range(16))}
    fix0 = [e for e in L.elems if all(e[0][j] // 16 == 0 for j in range(16))]
    check('W4 the row-preserving elements act transitively on the 16 rows; row-0 stabilizer 32',
          orbit == set(range(16)) and len(fix0) == 32)
    check('W5 SIG is symmetric, exactly', all(L.SIG[i][j] == L.SIG[j][i] for i in range(16) for j in range(16)))

    def e40(i, j):
        a, b, c, d = i // 4, i % 4, j // 4, j % 4
        return -(b == 0 and c == 0) + (a == 2 and b % 2 == 1 and d % 2 == 0) - (a % 2 == 0 and c % 2 == 1 and d == 0)
    E40 = L.mat(e40)
    neg = lambda E: [[-x for x in r] for r in E]
    pos = [E40, neg(E40), L.A38, L.B38, L.C38, neg(L.A38), L.WIT38]
    rng = random.Random(42)
    pos += [L.stab_apply(L.elems[rng.randrange(1024)], E40) for _ in range(16)]
    tests = []
    for E in pos:
        tests.append(E)
        for _ in range(3):
            F = [r[:] for r in E]; i, j = rng.randrange(16), rng.randrange(16)
            F[i][j] = rng.choice([x for x in (-1, 0, 1) if x != F[i][j]]); tests.append(F)
    enc = Enc(); enc.straight()
    sol = Cadical153(bootstrap_with=enc.cnf.clauses)
    agree = npos = nneg = 0
    for E in tests:
        a = [enc.p[i][j] if E[i][j] == 1 else (enc.n[i][j] if E[i][j] == -1 else enc.z[i][j]) for i in range(16) for j in range(16)]
        sat, ex = sol.solve(assumptions=a), L.straight_direct(E)
        agree += (sat == ex); npos += ex; nneg += (not ex)
    sol.delete()
    check('W6 the SAT straightness encoding agrees with the exact test on %d matrices (%d straight, %d not)'
          % (len(tests), npos, nneg), agree == len(tests) and npos >= 23 and nneg >= 40)
    check('W7 E40 has entries {-1,0,1}, support 40, 0 a most frequent value of every line',
          L.support(E40) == 40 and {x for r in E40 for x in r} == {-1, 0, 1}
          and all(max((-1, 0, 1), key=lambda v: (line.count(v), v == 0)) == 0
                  for line in [r for r in E40] + [list(c) for c in zip(*E40)]))


# ---- dispatch only ------------------------------------------------------------------------------------------------
def part_paths():
    r = run('r2a_landed.py')
    d = jload('r2a.json')
    check('C0 path A: the landed production probe replayed OK', r.returncode == 0 and d['C0'])
    R1 = d['R1']
    check('R1: E40 = -P+Q-T, entries {-1,0,1}, support 40, straight by levels and at exact points',
          R1['formula_equals_-P+Q-T'] and R1['entries'] == [-1, 0, 1] and R1['support'] == 40
          and R1['straight_levels'] and R1['straight_points'])
    check('C5: one entry changed fails both straightness methods',
          not d['C5_one_entry_changed']['straight_levels'] and not d['C5_one_entry_changed']['straight_points'])
    s, rl = d['R2A_E40']['strict'], d['R2A_E40']['relaxed']
    check('R2 A: 28 candidates; no structure holds identically; exceptional sets {1} strict, {1, -1} relaxed',
          d['R2A_E40']['candidates'] == 28 and s['identically'] == [] and rl['identically'] == []
          and s['exceptional'] == ['u1 = 1'] and rl['exceptional'] == ['u1 = -1', 'u1 = 1'])
    check('R2 A: at u = 1, 20 structures and 976 alignments (strict and relaxed); at u = -1, relaxed only, 4 structures, 272',
          s['at1'] == [20, 976] and rl['at1'] == [20, 976] and s['atm1'] == []
          and len(rl['atm1']) == 4 and sum(x[4] for x in rl['atm1']) == 272)
    check('C1b: act 38 arc reproduces L41', d['C1b'])
    check('C3: gauged E40 straight with the same exceptional sets', d['C3_gauge']['same'] and d['C3_gauge']['straight'])
    r = run('r2b2_census.py')
    d = jload('r2b2.json')
    check('C0 path B(ii): the landed independent probe replayed OK', r.returncode == 0 and d['C0'])
    want = {'u = 1': (20, 976, 20, 976), 'u = -1': (0, 0, 4, 272), 'u = (3+4i)/5': (0, 0, 0, 0),
            'u = (5+12i)/13': (0, 0, 0, 0), 'u = (8+15i)/17': (0, 0, 0, 0), 'u = i': (0, 0, 0, 0)}
    got = {k: (v['strict']['partitions'], v['strict']['alignments'], v['relaxed']['partitions'], v['relaxed']['alignments'])
           for k, v in d['points'].items()}
    check('R2 B(ii): census empty at the four generic points, nonempty exactly at u = 1 (20/976) and u = -1 (relaxed 4/272)',
          got == want)


def part_r5():
    r = run('r5_family.py')
    d = jload('r5.json')
    fam = {}
    for v in d.values():
        fam.setdefault((v['family'], v['class_support']), 0)
        fam[(v['family'], v['class_support'])] += 1
    check('R5: 128 members, all straight, all exact, all in 0 triples',
          r.returncode == 0 and len(d) == 128 and all(v['straight'] and v['exact'] and v['triples_member'] == 0 for v in d.values()))
    check('R5: class supports 40 for 16 and 44 for 48 members of each family',
          fam == {('ABC', 40): 16, ('ABC', 44): 48, ('PQT', 40): 16, ('PQT', 44): 48})


def part_n18(k):
    sys.path.insert(0, TOOLS)
    from fractions import Fraction as Fr
    import lib42 as L
    import triples as T

    def rank(rows):
        M = [[Fr(x) for x in r] for r in rows if any(r)]; r = 0; ncol = len(M[0]) if M else 0
        for c in range(ncol):
            p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
            if p is None: continue
            M[r], M[p] = M[p], M[r]; pv = M[r][c]
            for i in range(len(M)):
                if i != r and M[i][c] != 0:
                    f = M[i][c] / pv; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
            r += 1
        return r

    def vec(eq):
        v = [0] * 256
        for kk, (i, j) in eq: v[i * 16 + j] += kk
        return v
    CEN = T.census()
    mine = L.STRUCTS[k::3]
    check('n18:%d covers %d of the 18 subspaces' % (k, len(mine)), len(L.STRUCTS) == 18 and len(mine) == 6)
    for nm, tr, s in mine:
        mn, cp, rows = s
        old = [list(r) for r in L.SMAT[(nm, tr, True)]]
        ro = rank(old); matches = []
        for key, ths in CEN.items():
            form, mn2, blocks, classes = key
            if form != ('row' if tr else 'column') or mn2 != mn: continue
            if sorted(map(sorted, blocks)) != sorted(map(sorted, cp)) or sorted(map(sorted, classes)) != sorted(map(sorted, rows)): continue
            for th in ths:
                new = [vec(e) for e in T.identity_eqs(key, th)]
                if rank(new) == ro and rank(old + new) == ro: matches.append(th)
        sorted_th = tuple(tuple([sorted(cl)[a] for cl in sorted(map(tuple, map(sorted, rows)))]) for a in range(mn[0]))
        at_sorted = any(sorted(map(tuple, th)) == sorted(sorted_th) for th in matches)
        check('N18 %s %s: rank %d, equal to exactly one realizing triple, at its sorted alignment'
              % (nm, 'row' if tr else 'column', ro), len(matches) == 1 and at_sorted)


def part_dfs(k):
    ensure_msize()
    sys.path.insert(0, TOOLS)
    os.chdir(TOOLS)
    sys.argv[1:] = ['39']   # dfsR.py reads its argv at import; the rerun ran `dfsR2.py 39 ...`
    import numpy as np
    from dfsR2 import RSearch2, to_flat
    from classify42 import member_masks
    Rall = [int(x) for x in open('Rle13_39.txt').read().split()]
    mine = Rall[k::6]
    check('dfs:%d: %d of the 5494 row sets' % (k, len(mine)), len(Rall) == 5494 and len(mine) == (916 if k < 4 else 915))
    leaves = nond = nodes = pruned = 0
    for R in mine:
        S = RSearch2(R, 39, True); S.run()
        nodes += S.nodes; pruned += S.pruned
        if S.leaves:
            X = np.array([to_flat(a) for a in S.leaves]); ms, mr = member_masks(X)
            leaves += len(X); nond += int((mr == 0).sum())
    print('  nodes %d pruned %d leaves %d nonDita %d' % (nodes, pruned, leaves, nond), flush=True)
    check('dfs:%d: 0 leaves outside N18 (leaves %d, non-Dita %d)' % (k, leaves, nond), nond == 0)
    check('dfs:%d: node and pruning counts as frozen' % k, (nodes, pruned) == DFS_COUNTS[k])


def part_sathr():
    r = run('sat_hr.py', '39')
    check('sat_hr 39: 270792 clauses, UNSAT', 'B 39 clauses 270792' in r.stdout and '\nUNSAT' in '\n' + r.stdout
          and 'SAT ' not in r.stdout.replace('UNSAT', ''))


def part_cubes(k):
    sys.path.insert(0, TOOLS)
    from pysat.solvers import Cadical153
    from sat42 import Enc
    from lib42 import elems
    fix0 = [(p, s_) for p, s_ in elems if all(p[j] // 16 == 0 for j in range(16))]

    def act(e, y):
        p, s_ = e; out = [0] * 16
        for j in range(16): out[p[j] % 16] = s_ * y[j]
        return tuple(out)
    cubes = []
    for m in (1, 2):
        reps = []; seen = set()
        for supp in itertools.combinations(range(16), m):
            for signs in itertools.product((1, -1), repeat=m):
                y = [0] * 16
                for kk, s in zip(supp, signs): y[kk] = s
                y = tuple(y)
                if y in seen: continue
                orb = set()
                for e in fix0:
                    a = act(e, y); orb.add(a); orb.add(tuple(-x for x in a))
                seen |= orb; reps.append(y)
        cubes += [(m, y) for y in reps]
    check('cubes: row-0 stabilizer 32; 26 cubes (m = 1: 2, m = 2: 24)',
          len(fix0) == 32 and len(cubes) == 26 and sum(1 for c in cubes if c[0] == 1) == 2)
    for idx, (m, y) in enumerate(cubes):
        if idx % 3 != k: continue
        e = Enc(); e.straight(); e.mode0(); e.lines_ge(m); e.support_le(39)
        for j in range(16):
            e.cnf.append([e.p[0][j] if y[j] == 1 else (e.n[0][j] if y[j] == -1 else e.z[0][j])])
        s = Cadical153(bootstrap_with=e.cnf.clauses); ok = s.solve(); s.delete()
        check('cube %d (m %d, y0 %s): UNSAT' % (idx, m, y), not ok)


# (nodes, subtrees pruned by Lemma NS) per shard, from the rerun at L41 of the two halves; totals 2333206 and 228374
MSIZE_SHA256 = '5ac7c84aa7506a2741fe8a81cba28a607472cc9357344216c2f6eaa56ce0787d'
WLOG_HIGH = 104
DFS_COUNTS = {0: (151625, 18685), 1: (471631, 46227), 2: (281624, 24040), 3: (428775, 44974), 4: (722178, 72305),
              5: (277373, 22143)}

PARTS = {'witness': part_witness, 'd01span': part_d01span, 'wlog': part_wlog, 'paths': part_paths, 'r5': part_r5, 'sathr': part_sathr}
if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != '--part':
        print(__doc__); sys.exit(2)
    part = sys.argv[2]; t0 = time.time()
    name, _, arg = part.partition(':')
    if name in PARTS and not arg: PARTS[name]()
    elif name == 'n18' and arg in ('0', '1', '2'): part_n18(int(arg))
    elif name == 'dfs' and arg in ('0', '1', '2', '3', '4', '5'): part_dfs(int(arg))
    elif name == 'cubes' and arg in ('0', '1', '2'): part_cubes(int(arg))
    else:
        print('unknown part', part); sys.exit(2)
    if FAILS:
        print('dita_support_minimality_probe %s: FAILED (%d of %d checks): %s' % (part, len(FAILS), COUNT[0], '; '.join(FAILS)))
        sys.exit(1)
    print('dita_support_minimality_probe %s: OK -- %d checks (%.0fs)' % (part, COUNT[0], time.time() - t0))
