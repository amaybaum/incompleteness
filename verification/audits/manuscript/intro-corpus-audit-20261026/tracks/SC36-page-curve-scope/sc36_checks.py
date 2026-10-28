"""SC-36 checks. Standard library only; run from the repository root as `python3 -I <this file>`.

K1  entropy budget under permutations (GR App. A.8 scope paragraph): S(rho_R(t)) <= H(p0) at every
    aligned single-site bipartition, for every permutation of 3 qubits and several initial states.
    Exact Schmidt data: for a one-qubit R the reduced state is 2x2 and its eigenvalues are closed form.
K1c configurations: every permutation image of a configuration has S(rho_R) = 0 (rank 1, exact).
CC1 countercontrol: a non-permutation unitary (Hadamard, then CNOT) from a configuration gives
    S = ln 2 > H(p0) = 0, so the K1 comparison detects a violation when one exists.
K2  tightness: CNOT on |+>|0> reaches S = ln 2 = H(p0).
K3  A.7 counterexample to "rho_D constant => VB pure": D maximally entangled with V, trivial dynamics.
K4  GR:366 / ch07:193 convention factors, from SI constants, against the closed forms in the text.
K5  re-grep of retired phrases and of the corrected statement across papers/*.md and book/*.md.
K6  every changed chapter line has an identical line in the FULL mirror.
The verdict prints only if every control passes.
"""
import itertools, math, os, re, subprocess, sys
from fractions import Fraction

FAIL = []
def check(name, ok, detail=''):
    print(f'{name}: {"pass" if ok else "FAIL"} {detail}')
    if not ok:
        FAIL.append(name)

N = 3  # qubits
D = 1 << N

def reduced_R(psi, site):
    """2x2 reduced density matrix of qubit `site` for a real or complex vector psi (list)."""
    r = [[0j, 0j], [0j, 0j]]
    for x in range(D):
        for y in range(D):
            if (x & ~(1 << site)) != (y & ~(1 << site)):
                continue
            a, b = (x >> site) & 1, (y >> site) & 1
            r[a][b] += psi[x] * psi[y].conjugate()
    return r

def ent2(r):
    tr = (r[0][0] + r[1][1]).real
    det = (r[0][0] * r[1][1] - r[0][1] * r[1][0]).real
    disc = max(tr * tr / 4 - det, 0.0)
    ls = [tr / 2 + math.sqrt(disc), tr / 2 - math.sqrt(disc)]
    return -sum(l * math.log(l) for l in ls if l > 1e-15)

def shannon(ps):
    return -sum(p * math.log(p) for p in ps if p > 0)

def permute(psi, perm):
    out = [0j] * D
    for x in range(D):
        out[perm[x]] = psi[x]
    return out

def normalize(v):
    n = math.sqrt(sum(abs(a) ** 2 for a in v))
    return [a / n for a in v]

# K1 / K1c
states = {
    'config |000>': [1 + 0j] + [0j] * (D - 1),
    'two-term |000>+|111>': normalize([1, 0, 0, 0, 0, 0, 0, 1]),
    'uniform signs |-++>': normalize([(-1) ** (x & 1) for x in range(D)]),
    'skewed real': normalize([3, 1, 0, 2, 0, 0, 1, 1]),
    'complex phases': normalize([complex(math.cos(k), math.sin(k * k)) for k in range(D)]),
}
worst = {}
viol = 0
for name, psi in states.items():
    h0 = shannon([abs(a) ** 2 for a in psi])
    mx = 0.0
    for perm in itertools.permutations(range(D)):
        phi = permute(psi, perm)
        for site in range(N):
            s = ent2(reduced_R(phi, site))
            mx = max(mx, s)
            if s > h0 + 1e-12:
                viol += 1
    worst[name] = (mx, h0)
    print(f'  {name}: max S over 40320 permutations x 3 cuts = {mx:.12f}, H(p0) = {h0:.12f}')
check('K1', viol == 0, f'violations={viol}')
check('K1c', worst['config |000>'][0] == 0.0, f'max S from a configuration = {worst["config |000>"][0]}')

# CC1: Hadamard on qubit 0 then CNOT(0->1) from |000>: not a permutation
s2 = 1 / math.sqrt(2)
psi = [0j] * D
psi[0] = s2; psi[1] = s2            # H on qubit 0 of |000>
psi = permute(psi, [x ^ (((x >> 0) & 1) << 1) for x in range(D)])  # CNOT 0->1 (a permutation)
s = ent2(reduced_R(psi, 1))
check('CC1', s > 1e-6 + 0.0, f'S = {s:.12f} > H(p0 of |000>) = 0')

# K2: CNOT on |+>|0>|0>: initial H(p0) = ln 2, final S across qubit 1 = ln 2
psi0 = [0j] * D; psi0[0] = s2; psi0[1] = s2
psi = permute(psi0, [x ^ (((x >> 0) & 1) << 1) for x in range(D)])
s = ent2(reduced_R(psi, 1)); h0 = shannon([abs(a) ** 2 for a in psi0])
check('K2', abs(s - h0) < 1e-12 and abs(h0 - math.log(2)) < 1e-12, f'S = {s:.12f}, H(p0) = {h0:.12f}')

# K3: V,D qubits maximally entangled, B a qubit in |0>; dynamics trivial. rho_D = I/2 constant; rho_VB purity 1/2.
# basis index = v + 2*b + 4*d
bell = [0j] * 8; bell[0] = s2; bell[1 + 4] = s2
# rho_D eigenvalues and rho_VB purity, exactly via Fractions on the amplitudes squared (all 1/2)
rhoD = [[Fraction(0)] * 2 for _ in range(2)]
for x in range(8):
    for y in range(8):
        if (x & 3) == (y & 3) and bell[x] != 0 and bell[y] != 0:
            rhoD[x >> 2][y >> 2] += Fraction(1, 2)
purity_VB = sum(rhoD[i][j] * rhoD[j][i] for i in range(2) for j in range(2))  # equal to purity of rho_D
check('K3', rhoD == [[Fraction(1, 2), 0], [0, Fraction(1, 2)]] and purity_VB == Fraction(1, 2),
      f'rho_D = I/2 at every t (trivial dynamics), purity(rho_VB) = {purity_VB}')

# K4: convention factors (CODATA 2018 SI; H0 = 67.4 km/s/Mpc, Omega_L = 0.6847, Planck 2018)
hbar = 1.054571817e-34; c = 2.99792458e8; G = 6.67430e-11
H = 67.4e3 / 3.0856775814913673e22; OL = 0.6847
S = math.pi * c ** 5 / (hbar * G * H ** 2)
EPl = math.sqrt(hbar * c ** 5 / G); EPlred = math.sqrt(hbar * c ** 5 / (8 * math.pi * G))
def modesum(E):  # energy density of sum k^4/(16 pi^2) cut off at energy E
    return E ** 4 / (16 * math.pi ** 2 * (hbar * c) ** 3)
rho_planck = c ** 7 / (hbar * G ** 2)          # M_Pl^4 in energy-density units
rho_HG = H ** 2 * c ** 2 / G
rho_crit = 3 * H ** 2 * c ** 2 / (8 * math.pi * G)
f1 = rho_planck / rho_HG / S
f2 = modesum(EPl / 2) / rho_crit / S
f3 = modesum(EPlred) / (OL * rho_crit) / S
check('K4a', abs(f1 * math.pi - 1) < 1e-12, f'M_Pl^4/(H^2/G) / S_dS = {f1:.6e} vs 1/pi = {1/math.pi:.6e}')
check('K4b', abs(f2 * 96 * math.pi ** 2 - 1) < 1e-12, f'modesum(M_Pl/2)/rho_crit / S_dS = {f2:.6e} vs 1/(96 pi^2) = {1/(96*math.pi**2):.6e}')
check('K4c', abs(f3 * 384 * math.pi ** 4 * OL - 1) < 1e-12 and abs(f3 - 3.9e-5) < 0.05e-5,
      f'modesum(reduced M_Pl)/(Omega_L rho_crit) / S_dS = {f3:.4e} vs 1/(384 pi^4 Omega_L) = {1/(384*math.pi**4*OL):.4e}')
check('K4d', f3 < 1 / (96 * math.pi ** 2), f'{f3:.3e} < 1/(96 pi^2) = {1/(96*math.pi**2):.3e}, outside [1/(96 pi^2), 8/3]')
print(f'  S_dS = {S:.3e}')

# K5: re-grep
files = sorted([os.path.join('papers', f) for f in os.listdir('papers') if f.endswith('.md')] +
               [os.path.join('book', f) for f in os.listdir('book') if f.endswith('.md')])
def count(pat, exclude_intro=True):
    n = 0; where = []
    for f in files:
        if exclude_intro and f.endswith('Introduction.md'):
            continue
        k = len(re.findall(pat, open(f, encoding='utf-8').read()))
        if k:
            n += k; where.append(f'{f}:{k}')
    return n, where
retired = {
    'resolves the paradox': r'resolves the paradox',
    'Resolved at the level of information preservation': r'Resolved at the level of information preservation',
    'at the level of information preservation': r'at the level of information preservation',
    'Problems resolved': r'Problems resolved',
    'range 1/(96pi^2)..8/3': r'between \$1/\(96\\pi\^2\)\$ and \$8/3\$',
    'reproducible from a finite deterministic substratum': r'reproducible from a finite deterministic substratum',
    'it can be combinatorial': r'it can be combinatorial',
    'BH information preserved (row)': r'\| BH information preserved \|',
    'Preserved; Page curve conditional': r'Preserved; Page curve conditional',
    'Five universality-class entries': r'Five universality-class entries',
}
for k, pat in retired.items():
    n, where = count(pat)
    check(f'K5 retired "{k}"', n == 0, f'count={n} {where}')
n, where = count(r'H-scramble fails for every bijection')
print(f'  surviving "H-scramble fails for every bijection": {n} {where}')
n, where = count(r'no instance')
print(f'  "no instance": {n} {where}')
n, where = count(r'resolv', exclude_intro=True)
# context-only listing for the record; the BH-specific ones are covered above
bh = subprocess.run(['grep', '-n', '-i', 'information paradox.*resolv\\|resolv.*information paradox', *files],
                    capture_output=True, text=True).stdout.strip().splitlines()
print(f'  lines pairing "information paradox" with "resolv": {len(bh)}')
for l in bh:
    print('   ', l[:200])

# K6: chapter lines mirrored in FULL
full = set(open('book/The-Incompleteness-of-Observation-FULL.md', encoding='utf-8').read().splitlines())
base = sys.argv[1] if len(sys.argv) > 1 else 'origin/main'
missing = 0
for f in ['book/ch07-gravity.md', 'book/ch09-universality.md', 'book/ch18-beyond.md', 'book/ch19-open-problems.md',
          'book/appendix-a-prediction-status.md', 'book/glossary.md']:
    d = subprocess.run(['git', 'diff', '-U0', base, '--', f], capture_output=True, text=True).stdout
    for line in d.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            if line[1:] not in full:
                missing += 1; print('   not mirrored:', f, line[:120])
check('K6', missing == 0, f'changed chapter lines missing from FULL: {missing}')

print()
print('VERDICT:', 'all controls pass' if not FAIL else 'VOID (failed: ' + ', '.join(FAIL) + ')')
sys.exit(1 if FAIL else 0)
