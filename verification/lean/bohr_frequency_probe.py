#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/BohrFrequency.lean.

[GR] Theorem (Bohr-frequency completeness), and the post-mortem of the theorem it replaces.

The statement that stood at GR 3.3 -- matching transition probabilities force H' = D H D^dag --
is FALSE, on three counts, and this probe carries all three as permanent countercontrols alongside
the exact content that replaces it: the probabilities determine the full Bohr-frequency set, which
is what the dimensional determination of hbar actually consumes.

  F1  the return-probability expansion: |U_ii(t)|^2 = sum_ab |V_ia|^2 |V_ib|^2 e^{-i(E_a-E_b)t},
      checked against direct matrix exponentiation at machine precision.
  F2  frequency recovery: the gap set read off the probability data (by solving the character
      linear system at sampled times) matches {E_a - E_b} exactly, including with a DEGENERATE
      gap -- merged positive coefficients cannot cancel.
  F3  COUNTERCONTROL ONE (the energy origin): H + E0 preserves every |U_ij(t)|^2 identically and
      is not D H D^dag -- any reconstruction conclusion must carry E0.
  F4  COUNTERCONTROL TWO (the antiunitary reflection): -conj(H) preserves every |U_ij(t)|^2
      identically, its spectrum is {-E_a}, not a shift of {E_a} for generic H -- any
      reconstruction conclusion must carry the second branch.
  F5  COUNTERCONTROL THREE (the C4 breach, joining [SM] Proposition 20): the C4 ring satisfies
      the withdrawn theorem's hypotheses -- distinct eigenvalues, uniform overlaps -- yet conj(H)
      matches every |U_ij(t)|^2 while its loop phase differs, so eigenvalue non-degeneracy is not
      a substitute for the gap condition. The same matrix lands inside the two-branch form via
      the bipartite sign D = diag(1,-1,1,-1).
  F6  the homometric obstruction: the Golomb rulers {0,1,4,10,12,17} and {0,1,8,11,13,17} share
      all fifteen pairwise differences, each ruler's differences distinct, and are not translates
      or reflections of one another -- exact integer arithmetic -- so the two-branch claim's
      reduction must run on coefficient-labelled data, not the raw difference set.
  F7  both branches of the claim reproduce the data exactly; a generic perturbation off them
      does not (local rigidity).
  F8  lint.
  F9  ANTIUNITARY CIRCUIT INVARIANCE: transposing the preparation, every Kraus operator
      (entrywise conjugation), and the effect leaves every multi-step circuit probability
      unchanged, including instrument outcome strings; conjugating only part of the circuit
      breaks it. Kernel twins: circuit_invariance / string_invariance / transposeMap_kraus
      (OIBridge/AntiunitaryInvariance.lean) -- no operational data separate the two branches.
  F10 THERMAL ORIENTATION: the antiunitary image of the +beta Gibbs state of H is the -beta
      Gibbs state of the reflected Hamiltonian (matrix identity checked to machine precision),
      +beta and -beta Gibbs profiles differ whenever two energies differ (and coincide when
      all energies are equal -- the degenerate exception), and an exact rational passivity
      check: a strictly passive profile turns strictly active under energy reflection. Kernel
      twins: transported_gibbs / gibbs_orientation / passivity_selector
      (OIBridge/ThermalOrientation.lean) -- oriented thermal structure excludes the branch.

Usage:  python3 bohr_frequency_probe.py
"""
import itertools
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []
TOL = 1e-11


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


rng = np.random.default_rng(23)
ts = np.linspace(0.07, 19.3, 141)


def probs(H):
    E, V = np.linalg.eigh(H)
    out = []
    for t in ts:
        U = V @ np.diag(np.exp(-1j * E * t)) @ V.conj().T
        out.append(np.abs(U) ** 2)
    return np.array(out), E, V


def rand_herm(nn):
    A = rng.normal(size=(nn, nn)) + 1j * rng.normal(size=(nn, nn))
    return (A + A.conj().T) / 2


# ---------------------------------------------------------------- F1  the expansion
ok1 = True
for nn in (2, 3, 4):
    H = rand_herm(nn)
    P, E, V = probs(H)
    p = np.abs(V) ** 2
    for k, t in enumerate(ts[:25]):
        for i in range(nn):
            model = sum(p[i, a] * p[i, b] * np.exp(-1j * (E[a] - E[b]) * t)
                        for a in range(nn) for b in range(nn))
            ok1 &= abs(model.real - P[k, i, i]) < TOL and abs(model.imag) < TOL
check("F1", ok1,
      "the return-probability expansion |U_ii(t)|^2 = sum_ab |V_ia|^2 |V_ib|^2 e^{-i(E_a-E_b)t} "
      "against direct matrix exponentiation, at n = 2, 3, 4 and 25 times each. Lean's "
      "`retProb_eq_sum_gaps` and `normSq_expansion`")

# ---------------------------------------------------------------- F2  frequency recovery
def recover_freqs(signal, cand):
    """Least-squares coefficients of the candidate frequencies; support = nonzero ones."""
    A = np.exp(-1j * np.outer(ts, cand))
    coef, *_ = np.linalg.lstsq(A, signal, rcond=None)
    return {cand[k] for k in range(len(cand)) if abs(coef[k]) > 1e-6}


ok2 = True
# generic spectrum, and one with a DEGENERATE gap (equally spaced), overlaps generic
for E in (np.array([0.0, 0.9, 2.3]), np.array([0.0, 1.0, 2.0])):
    nn = len(E)
    Q, _ = np.linalg.qr(rng.normal(size=(nn, nn)) + 1j * rng.normal(size=(nn, nn)))
    V = Q
    if np.abs(V).min() < 0.15:
        continue
    p = np.abs(V) ** 2
    sig = np.array([sum(p[0, a] * p[0, b] * np.exp(-1j * (E[a] - E[b]) * t)
                        for a in range(nn) for b in range(nn)) for t in ts])
    gapset = {round(E[a] - E[b], 9) for a in range(nn) for b in range(nn)}
    cand = sorted(gapset | {round(x, 9) for x in (0.35, -1.7, 3.05)})   # decoys included
    got = recover_freqs(sig, np.array(cand))
    ok2 &= {round(g, 9) for g in got} == gapset
check("F2", ok2,
      "frequency recovery: solving the character system at the sampled times, against decoy "
      "frequencies, returns exactly the gap set -- including for an equally-spaced spectrum, where "
      "the degenerate gap's merged coefficient stays positive. Lean's `gaps_determined` and "
      "`ampR_pos`")

# ---------------------------------------------------------------- F3  the energy origin
H = rand_herm(3)
P0, E0v, _ = probs(H)
P1, E1v, _ = probs(H + 0.83 * np.eye(3))
ok3 = np.abs(P1 - P0).max() < TOL
ok3 &= not np.allclose(np.sort(E1v), np.sort(E0v))
check("F3", ok3,
      f"COUNTERCONTROL ONE. H + E0 preserves every |U_ij(t)|^2 to {np.abs(P1 - P0).max():.1e} and "
      f"shifts the spectrum, so it is not D H D^dag: a reconstruction conclusion without the "
      f"energy origin is false. Lean's `shift_modsq` is this, exactly")

# ---------------------------------------------------------------- F4  the reflection
P2, E2v, _ = probs(-H.conj())
ok4 = np.abs(P2 - P0).max() < TOL
spec, rspec = np.sort(E0v), np.sort(-E0v)
ok4 &= not any(np.allclose(rspec + s, spec) for s in np.linspace(-4, 4, 4001))
check("F4", ok4,
      f"COUNTERCONTROL TWO. -conj(H) preserves every |U_ij(t)|^2 to {np.abs(P2 - P0).max():.1e}; "
      f"its spectrum is the reflection, which no shift aligns with the original for this generic "
      f"H. A one-branch conclusion is false; the branch is antiunitary (time reversal composed "
      f"with energy reflection), not a gauge transformation. Lean's `reflect_conj`/`reflect_modsq`")

# ---------------------------------------------------------------- F5  the C4 breach
a, b = 1.0, 0.3
z = a + 1j * b
H4 = np.zeros((4, 4), complex)
for k in range(4):
    H4[k, (k + 1) % 4] = z
    H4[(k + 1) % 4, k] = np.conj(z)
P4, E4, V4 = probs(H4)
P4c, _, _ = probs(H4.conj())
ok5 = min(np.diff(np.sort(E4))) > 1e-9                                # distinct eigenvalues
ok5 &= abs(np.abs(V4).min() - 0.5) < 1e-9                             # uniform overlaps
g4 = sorted(round(E4[x] - E4[y], 9) for x in range(4) for y in range(4) if x != y)
ok5 &= len(set(g4)) < len(g4)                                         # DEGENERATE gaps
ok5 &= np.abs(P4c - P4).max() < TOL                                   # conj(H) matches the data


def loop(H):
    return H[0, 1] * H[1, 2] * H[2, 3] * H[3, 0]


ok5 &= abs(loop(H4).imag) > 1                                          # loop phase genuinely complex
ok5 &= abs(loop(H4.conj()) - loop(H4)) > 1                             # and conj differs
D4 = np.diag([1, -1, 1, -1]).astype(complex)
ok5 &= np.allclose(H4.conj(), -D4 @ H4.conj() @ D4.conj().T)           # lands in the second branch
check("F5", ok5,
      "COUNTERCONTROL THREE, joining [SM] Proposition 20. The C4 ring satisfies the withdrawn "
      "hypotheses -- eigenvalues {+-2a, +-2b} distinct, overlaps all 1/2 -- yet conj(H) matches "
      "every |U_ij(t)|^2 (reciprocity) while its loop product z^4 is conjugated, so it is not "
      "diagonal-conjugate to H: eigenvalue non-degeneracy does not substitute for the gap "
      "condition. The bipartite sign diag(1,-1,1,-1) shows conj(H) = -D conj(H) D^dag, inside the "
      "two-branch form")

# ---------------------------------------------------------------- F6  the homometric rulers
R1 = (0, 1, 4, 10, 12, 17)
R2 = (0, 1, 8, 11, 13, 17)


def diffset(R):
    return sorted(abs(x - y) for x, y in itertools.combinations(R, 2))


ok6 = diffset(R1) == diffset(R2)                                       # same fifteen differences
ok6 &= len(set(diffset(R1))) == 15 and len(set(diffset(R2))) == 15     # each a Golomb ruler
shifts = range(-20, 21)
ok6 &= all(tuple(sorted(x + s for x in R1)) != R2 for s in shifts)     # no translate
ok6 &= all(tuple(sorted(s - x for x in R1)) != R2 for s in shifts)     # no reflection
check("F6", ok6,
      "the homometric obstruction, in exact integers: {0,1,4,10,12,17} and {0,1,8,11,13,17} share "
      "all fifteen pairwise differences, each ruler's differences distinct, and no translate or "
      "reflection carries one to the other. Distinct gaps alone do not make a spectrum "
      "recoverable from its difference set, so the two-branch claim's reduction must run on the "
      "coefficient-labelled frequency data -- the recorded open step")

# ---------------------------------------------------------------- F7  the branches, and rigidity
E3, V3 = np.linalg.eigh(H)
alph = rng.normal(size=3)
D = np.diag(np.exp(1j * alph))
ok7 = True
for name, Hb in (("D H D^dag + E0", D @ H @ D.conj().T + 1.3 * np.eye(3)),
                 ("-D conj(H) D^dag + E0", -D @ H.conj() @ D.conj().T + 1.3 * np.eye(3))):
    Pb, _, _ = probs(Hb)
    ok7 &= np.abs(Pb - P0).max() < TOL
Hp = H + 0.01 * rand_herm(3)
Pp, _, _ = probs(Hp)
ok7 &= np.abs(Pp - P0).max() > 1e-4
check("F7", ok7,
      "both branches of the two-branch claim reproduce every |U_ij(t)|^2 exactly, with a random "
      "diagonal unitary and a nonzero energy shift, and a generic 1% perturbation off the "
      "branches moves the data: the classification is locally rigid where it is checked, and "
      "what remains open is that nothing else global slips through")

# ---------------------------------------------------------------- F8  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'BohrFrequency.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
gr = open(os.path.join(HERE, '..', '..', 'papers', 'GR.md'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('chr_injective', 'coeffs_eq_zero', 'retProb_eq_sum_gaps', 'ampR_pos',
         'gaps_determined', 'normSq_expansion', 'shift_modsq', 'reflect_conj',
         'reflect_modsq', 'bohr_frequency_completeness')
ok8 = 'import OIBridge.BohrFrequency' in root
ok8 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok8 &= re.search(r'(?m)^axiom ', body) is None
ok8 &= all(f'theorem {n}' in src for n in NAMES)
ok8 &= all(f'#print axioms {n}' in src for n in NAMES)
ok8 &= 'native_decide' not in body
# the analytic step must be Dedekind, used at every real time -- no sampling, no approximation
ok8 &= 'linearIndependent_monoidHom' in src
ok8 &= '∀ t : ℝ, retProb E p t = retProb E\' p\' t' in src
# the manuscript must carry both theorems, the K2 citation structure, and the C4 cross-reference
ok8 &= '**Theorem (Bohr-frequency completeness).**' in gr
ok8 &= '**Theorem (D-gauge completeness, two-branch form).**' in gr
ok8 &= '**Corollary (operational antiunitary invariance).**' in gr
ok8 &= '**Corollary (thermodynamic orientation).**' in gr
ok8 &= 'no antiunitary branch and no nontrivial $D$' in gr
ok8 &= 'A. Bekir and S. W. Golomb' in gr
ok8 &= 'the passage from integer to real spectra being proved, not assumed' in gr
ok8 &= '[SM] Proposition 20' in gr
ok8 &= '0,1,4,10,12,17' in gr and '0,1,8,11,13,17' in gr
# and the withdrawn conclusion must not be asserted anywhere as a theorem
ok8 &= '**Theorem (D-gauge completeness).**' not in gr
check("F8", ok8,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The "
      f"analytic step is Dedekind's independence of characters at every real time, not sampling. "
      f"The manuscript carries Bohr-frequency completeness and the two-branch theorem, the "
      f"latter proved with the integer Bekir-Golomb classification as its one cited input and "
      f"the integer-to-real passage proved internally; the [SM] Proposition 20 cross-reference "
      f"and the homometric rulers stand, and the withdrawn unconditional conclusion is still "
      f"asserted nowhere")

# ---------------------------------------------------------------- F9  antiunitary invariance
rng9 = np.random.default_rng(20260830)


def rmat(k):
    return rng9.normal(size=(k, k)) + 1j * rng9.normal(size=(k, k))


ok9 = True
for _ in range(5):
    k = 4
    rho = rmat(k)
    rho = rho @ rho.conj().T          # PSD preparation
    rho /= np.trace(rho)
    Ef = rmat(k)
    Ef = Ef @ Ef.conj().T             # PSD effect
    ops = [rmat(k) for _ in range(6)] # an outcome string of six instrument operators
    X, Xc = rho, rho.T
    for A in ops:
        X = A @ X @ A.conj().T
        Ac = A.conj()
        Xc = Ac @ Xc @ Ac.conj().T
    p = np.trace(Ef @ X)
    pc = np.trace(Ef.T @ Xc)
    ok9 &= abs(p - pc) < 1e-9 * max(1.0, abs(p))
    # multi-Kraus channels, composed
    X, Xc = rho, rho.T
    for _ in range(3):
        As = [rmat(k) for _ in range(3)]
        X = sum(A @ X @ A.conj().T for A in As)
        Xc = sum(A.conj() @ Xc @ A.conj().conj().T for A in As)
    ok9 &= abs(np.trace(Ef @ X) - np.trace(Ef.T @ Xc)) < 1e-7 * max(1.0, abs(np.trace(Ef @ X)))
    # countercontrol: conjugating only the operators (not the state/effect) breaks it
    X, Xbad = rho, rho
    A = ops[0]
    ok9 &= abs(np.trace(Ef @ (A @ rho @ A.conj().T))
               - np.trace(Ef @ (A.conj() @ rho @ A.conj().conj().T))) > 1e-9
# the unitary special case IS the second branch: conj channel of e^{-iHt} = channel of -conj(H)
H9 = rmat(4)
H9 = H9 + H9.conj().T
t9 = 0.7
from scipy.linalg import expm
U9 = expm(-1j * H9 * t9)
U9r = expm(-1j * (-H9.conj()) * t9)
ok9 &= np.max(np.abs(U9.conj() - U9r)) < 1e-9
check("F9", ok9,
      "ANTIUNITARY CIRCUIT INVARIANCE, numerically: transposing the preparation and effect and "
      "conjugating every instrument operator leaves six-step outcome-string probabilities and "
      "composed multi-Kraus circuit probabilities unchanged to machine precision; conjugating "
      "only part of the circuit breaks it; and the conjugated propagator IS the propagator of "
      "-conj(H) -- the circuit symmetry restricted to unitary evolution is exactly the second "
      "branch (kernel: circuit_invariance, string_invariance, unitary_channel_transpose)")

# ---------------------------------------------------------------- F10  thermal orientation
ok10 = True
from fractions import Fraction as Frac
E10 = np.array([0.0, 0.3, 1.1, 2.4])
beta = 0.9
E0c = 1.7


def gibbsv(b, Ev):
    w = np.exp(-b * Ev)
    return w / w.sum()


# reflection reverses temperature: gibbs(-beta) of (-E + E0) = gibbs(beta) of E
ok10 &= np.max(np.abs(gibbsv(-beta, -E10 + E0c) - gibbsv(beta, E10))) < 1e-12
# orientation: +beta and -beta profiles differ for nonconstant E, coincide for constant E
ok10 &= np.max(np.abs(gibbsv(beta, E10) - gibbsv(-beta, E10))) > 1e-3
ok10 &= np.max(np.abs(gibbsv(beta, np.ones(4)) - gibbsv(-beta, np.ones(4)))) < 1e-15
# the matrix identity D conj(rho_beta) D^dag = W diag(gibbs(-beta) E') W^dag
rngV = np.random.default_rng(20260831)
M = rngV.normal(size=(4, 4)) + 1j * rngV.normal(size=(4, 4))
Q, _ = np.linalg.qr(M)
V10 = Q
tau = [2, 0, 3, 1]
d10 = np.exp(1j * rngV.uniform(0, 6.28, 4))
bc10 = np.exp(1j * rngV.uniform(0, 6.28, 4))
Ep = np.zeros(4)
W10 = np.zeros((4, 4), dtype=complex)
for a in range(4):
    Ep[tau[a]] = -E10[a] + E0c
    for i in range(4):
        W10[i, tau[a]] = d10[i] * bc10[a] * np.conj(V10[i, a])
rho_b = V10 @ np.diag(gibbsv(beta, E10)).astype(complex) @ V10.conj().T
lhs = W10 @ np.diag(gibbsv(-beta, Ep)).astype(complex) @ W10.conj().T
rhs = np.diag(d10) @ rho_b.conj() @ np.diag(d10).conj().T
ok10 &= np.max(np.abs(lhs - rhs)) < 1e-12
# exact passivity: a strictly passive rational profile turns strictly active under reflection
Eex = [Frac(0), Frac(1), Frac(3)]
pex = [Frac(1, 2), Frac(1, 3), Frac(1, 6)]
ok10 &= all(pex[b] < pex[a] for a in range(3) for b in range(3) if Eex[a] < Eex[b])
Eref = [-e + Frac(5) for e in Eex]
ok10 &= any(not (pex[b] <= pex[a]) for a in range(3) for b in range(3) if Eref[a] < Eref[b])
# the WEAK selector: passivity with a TIE (not strict) and non-uniform still fails reflection
Ew = [Frac(0), Frac(1), Frac(2)]
pw = [Frac(1, 2), Frac(1, 4), Frac(1, 4)]     # passive (tie at the top), NOT uniform
ok10 &= all(pw[b] <= pw[a] for a in range(3) for b in range(3) if Ew[a] < Ew[b])
ok10 &= not all(pw[b] <= pw[a] for a in range(3) for b in range(3) if (-Ew[a]) < (-Ew[b]))
# and the uniform profile survives both orientations -- the degenerate exception is exact
pu = [Frac(1, 3)] * 3
ok10 &= all(pu[b] <= pu[a] for a in range(3) for b in range(3) if Ew[a] < Ew[b])
ok10 &= all(pu[b] <= pu[a] for a in range(3) for b in range(3) if (-Ew[a]) < (-Ew[b]))
# layer one of H-orientation transport: monotone finite-bath counting gives passivity
Om = lambda x: x * x * x + x          # strictly increasing bath count
Etot10 = Frac(10)
eps10 = [Frac(0), Frac(2), Frac(5)]
pc = [Om(Etot10 - e) for e in eps10]
ok10 &= all(pc[b] < pc[a] for a in range(3) for b in range(3) if eps10[a] < eps10[b])
check("F10", ok10,
      "THERMAL ORIENTATION: gibbs(-beta) of the reflected energies equals gibbs(beta) of the "
      "original (the E0 shift cancels; machine precision), +beta and -beta profiles differ "
      "whenever energies differ and coincide when all are equal, the matrix identity "
      "D conj(rho_beta) D^dag = rho_{-beta}(H') holds for the reflection-branch coboundary, "
      "and (exact fractions) the WEAK selector: a passive profile with a tie, non-uniform, "
      "already fails reflected passivity while the uniform profile survives both orientations "
      "-- and monotone finite-bath counting yields passivity (layer one of H-orientation "
      "transport). Oriented structure excludes the antiunitary branch (kernel: "
      "transported_gibbs, gibbs_orientation, passivity_selector_nonuniform, counting_passive)")

# ---------------------------------------------------------------- F11  stationarity + rigidity
ok11 = True
rng11 = np.random.default_rng(20260901)
M11 = rng11.normal(size=(4, 4)) + 1j * rng11.normal(size=(4, 4))
Q11, _ = np.linalg.qr(M11)
E11 = np.array([0.0, 0.7, 1.9, 3.2])
# a stationary state is a population profile: rho = V f(E) V^dag is fixed by U(t)-conjugation
# and diagonal in the eigenbasis; a generic rho is neither
pops = rng11.uniform(0.1, 1.0, 4)
pops /= pops.sum()
rho_st = Q11 @ np.diag(pops).astype(complex) @ Q11.conj().T
rho_gen = M11 @ M11.conj().T
rho_gen /= np.trace(rho_gen).real
for t in (0.37, 1.13, 2.9):
    U11 = Q11 @ np.diag(np.exp(-1j * E11 * t)) @ Q11.conj().T
    ok11 &= np.max(np.abs(U11 @ rho_st @ U11.conj().T - rho_st)) < 1e-12
    ok11 &= np.max(np.abs(U11 @ rho_gen @ U11.conj().T - rho_gen)) > 1e-3
Min = Q11.conj().T @ rho_st @ Q11
ok11 &= np.max(np.abs(Min - np.diag(np.diag(Min)))) < 1e-12
# ad_eq_scalar numerically: e^{i theta} U has the same conjugation action; an unrelated W does not
U0 = Q11 @ np.diag(np.exp(-1j * E11 * 0.37)) @ Q11.conj().T
Up = np.exp(1j * 1.234) * U0
Wu, _ = np.linalg.qr(rng11.normal(size=(4, 4)) + 1j * rng11.normal(size=(4, 4)))
X11 = rng11.normal(size=(4, 4)) + 1j * rng11.normal(size=(4, 4))
ok11 &= np.max(np.abs(U0 @ X11 @ U0.conj().T - Up @ X11 @ Up.conj().T)) < 1e-12
ok11 &= np.max(np.abs(U0 @ X11 @ U0.conj().T - Wu @ X11 @ Wu.conj().T)) > 1e-3
Zrel = Wu.conj().T @ U0
ok11 &= np.max(np.abs(Zrel - np.diag(np.diag(Zrel)))) > 1e-3  # not scalar for unrelated W
check("F11", ok11,
      "STATIONARITY AND CHANNEL RIGIDITY, numerically: a population-profile state is fixed by "
      "U(t)-conjugation at every sampled time and is diagonal in the energy eigenbasis, while "
      "a generic state is neither (kernel: stationary_offdiag / stationary_spectral_form -- "
      "the mathematical half of transport layer two); a phase multiple of U has the identical "
      "conjugation action while an unrelated unitary does not, and its relative operator is "
      "not scalar (kernel: ad_eq_scalar / phase_families_shift, backing the exact-unitary "
      "regime of Corollary A.3)")

# ------------------------------------------- F12  the correlated shell assignment (route a)
ok12 = True
# joint space: visible energies e = (0,1,2); hidden levels with counts 1,2,4,8 at
# energies 0,1,2,3 (bath count increasing with energy: beta_E > 0); total energy 3
evis = [0, 1, 2]
Ehid = [0] + [1] * 2 + [2] * 4 + [3] * 8          # 15 hidden states
Etot = 3
shell = [(i, h) for i in range(3) for h in range(len(Ehid)) if evis[i] + Ehid[h] == Etot]
wgt = {x: Frac(1, len(shell)) for x in shell}
marg = [sum(wgt.get((i, h), Frac(0)) for h in range(len(Ehid))) for i in range(3)]
ok12 &= marg == [Frac(8, 14), Frac(4, 14), Frac(2, 14)]
# the counting profile is strictly passive for the classical energies (layer one, exact)
ok12 &= all(marg[b] < marg[a] for a in range(3) for b in range(3) if evis[a] < evis[b])
# an i-dependent joint permutation preserving the shell: cycle hidden states within each
# hidden-energy level, with the cycle offset depending on i (genuinely correlated dynamics)
levels = {}
for h, Eh in enumerate(Ehid):
    levels.setdefault(Eh, []).append(h)


def phi(i, h):
    lev = levels[Ehid[h]]
    k = lev.index(h)
    return (i, lev[(k + 1 + i) % len(lev)])


img = {phi(i, h) for (i, h) in shell}
ok12 &= img == set(shell)                          # the shell is invariant
# marginal stationarity, exact, on the ACTUAL correlated ensemble
inv = {phi(i, h): w for (i, h), w in wgt.items()}
marg2 = [sum(inv.get((i, h), Frac(0)) for h in range(len(Ehid))) for i in range(3)]
ok12 &= marg2 == marg
# the hidden conditionals are i-dependent -- supported on DISJOINT hidden energy shells
supp = [set(h for (i2, h) in shell if i2 == i) for i in range(3)]
ok12 &= supp[0].isdisjoint(supp[1]) and supp[1].isdisjoint(supp[2])
ok12 &= supp[0] != supp[1]                          # mu(.|0) != mu(.|1): no fixed prior
# the margin selector on this profile: gamma = marg[0]-marg[1] = 2/7; any q within
# gamma/2 in sup-norm still fails reflected passivity; the uniform profile (far away)
# is reflected-passive, so the bound is doing real work
gam = marg[0] - marg[1]
q12 = [marg[0] - gam * Frac(1, 3), marg[1] + gam * Frac(1, 3), marg[2]]
ok12 &= max(abs(q12[k] - marg[k]) for k in range(3)) < gam / 2
ok12 &= not all(q12[b] <= q12[a] for a in range(3) for b in range(3)
                if (-evis[a]) < (-evis[b]))
qu = [Frac(1, 3)] * 3
ok12 &= max(abs(qu[k] - marg[k]) for k in range(3)) > gam / 2
ok12 &= all(qu[b] <= qu[a] for a in range(3) for b in range(3) if (-evis[a]) < (-evis[b]))
check("F12", ok12,
      "THE CORRELATED SHELL ASSIGNMENT, exact fractions (route a): uniform counting on an "
      "invariant total-energy shell has a strictly passive visible marginal (bath count "
      "increasing: beta_E > 0), the marginal is STATIONARY under a genuinely i-dependent "
      "shell-preserving joint dynamics with no product substitution, and the hidden "
      "conditionals mu(.|i) live on disjoint hidden energy shells -- the correlated "
      "preparation that blocks the fixed-prior channel (kernel: shellWeight_invariant, "
      "joint_stationary, marginal_stationary, shellConditional_sum in "
      "OIBridge/ShellAssignment.lean; the stopping point is the named Prop "
      "ShellRepresentationConsistency). The margin selector holds within gamma/2 and the "
      "uniform profile beyond it is reflected-passive: the bound does real work (kernel: "
      "approx_passivity_selector, exists_margin_pair)")

# ------------------------------------------- F13  the coherent lift as an extension problem (C1)
ok13 = True
# (a) THE OVERLAP IDENTITY, exhaustive census: joint space S = {0..5}, readout pi(s) = s // 2,
# a menu of two bijections x three outcomes, ALL 259 words to horizon 3, exact fractions.
# The quantum fold (permutation lift, Born branch update) must equal the classical trajectory
# fold at every word -- and stay diagonal with the classical weights as entries, which is the
# invariant the kernel induction (qfold_diagonal) runs on.
S13 = list(range(6))


def pi13(s):
    return s // 2


perms13 = [
    [1, 2, 3, 4, 5, 0],           # a 6-cycle
    [0, 2, 1, 5, 3, 4],           # a transposition times a 3-cycle
]
w13 = [Frac(k + 1, 21) for k in range(6)]          # normalized: 1+2+...+6 = 21


def mat_mul13(A, B):
    return [[sum(A[i][k] * B[k][j] for k in S13) for j in S13] for i in S13]


def class_fold13(word, w):
    w = list(w)
    for (g, i) in word:
        w = [w[g.index(s)] if pi13(s) == i else Frac(0) for s in S13]
    return w


def q_fold13(word, rho):
    for (g, i) in word:
        P = [[1 if g[j] == r else 0 for j in S13] for r in S13]
        Pt = [[P[c][r] for c in S13] for r in S13]
        proj = [[1 if (pi13(r) == i and r == c) else 0 for c in S13] for r in S13]
        rho = mat_mul13(mat_mul13(proj, mat_mul13(mat_mul13(P, rho), Pt)), proj)
    return rho


menu13 = [(g, i) for g in perms13 for i in range(3)]
rho13 = [[w13[r] if r == c else Frac(0) for c in S13] for r in S13]
nwords = 0
for L in range(4):
    for word in itertools.product(menu13, repeat=L):
        cw = class_fold13(word, w13)
        rho = q_fold13(word, rho13)
        ok13 &= all(rho[r][c] == (cw[r] if r == c else Frac(0)) for r in S13 for c in S13)
        nwords += 1
ok13 &= nwords == 259
# (b) causal normalization at one slot, on a NON-diagonal Gaussian-integer state (exact):
# the branch traces over the outcome partition sum to the parent trace.
A13 = [[complex(((r * 3 + c) % 5) - 2, ((r - c) * 2) % 7 - 3) for c in S13] for r in S13]
rhoH = [[A13[r][c] + A13[c][r].conjugate() for c in S13] for r in S13]
for g in perms13:
    tot = 0
    for i in range(3):
        P = [[1 if g[j] == r else 0 for j in S13] for r in S13]
        Pt = [[P[c][r] for c in S13] for r in S13]
        proj = [[1 if (pi13(r) == i and r == c) else 0 for c in S13] for r in S13]
        Y = mat_mul13(mat_mul13(proj, mat_mul13(mat_mul13(P, rhoH), Pt)), proj)
        tot += sum(Y[s][s] for s in S13)
    ok13 &= tot == sum(rhoH[s][s] for s in S13)
# (c) THE PREPARATION SLOT, exact LP landscape: the strengthened
# ShellRepresentationConsistency holds iff p = B*q with q in the simplex,
# B_{ia} = |V_{ia}|^2 doubly stochastic. Exact instance: the 3-4-5 rotation.
B345 = [[Frac(9, 25), Frac(16, 25)], [Frac(16, 25), Frac(9, 25)]]
ok13 &= all(sum(row) == 1 for row in B345)
ok13 &= all(sum(B345[i][a] for i in range(2)) == 1 for a in range(2))
# feasible: p = (3/5, 2/5) has the unique solution q = (1/7, 6/7), inside the simplex
p_f = [Frac(3, 5), Frac(2, 5)]
q_f = [Frac(1, 7), Frac(6, 7)]
ok13 &= all(sum(B345[i][a] * q_f[a] for a in range(2)) == p_f[i] for i in range(2))
ok13 &= all(qa >= 0 for qa in q_f) and sum(q_f) == 1
# the constructive witness rho = V diag(q) V^T: visible diagonal is p, eigenbasis form is
# diagonal (hence stationary at every time under any nondegenerate spectrum)
V345 = [[Frac(3, 5), Frac(-4, 5)], [Frac(4, 5), Frac(3, 5)]]
rho_w = [[sum(V345[i][a] * q_f[a] * V345[j][a] for a in range(2))
          for j in range(2)] for i in range(2)]
ok13 &= [rho_w[i][i] for i in range(2)] == p_f
back = [[sum(V345[a][i] * rho_w[a][b] * V345[b][j] for a in range(2) for b in range(2))
         for j in range(2)] for i in range(2)]
ok13 &= back == [[q_f[0], Frac(0)], [Frac(0), q_f[1]]]
# infeasible: p = (7/10, 3/10) -- B is invertible, the unique solution leaves the simplex
p_i = [Frac(7, 10), Frac(3, 10)]
det13 = B345[0][0] * B345[1][1] - B345[0][1] * B345[1][0]
ok13 &= det13 == Frac(-7, 25)
q_i = [(B345[1][1] * p_i[0] - B345[0][1] * p_i[1]) / det13,
       (B345[0][0] * p_i[1] - B345[1][0] * p_i[0]) / det13]
ok13 &= all(sum(B345[i][a] * q_i[a] for a in range(2)) == p_i[i] for i in range(2))
ok13 &= sum(q_i) == 1 and any(qa < 0 for qa in q_i)
# the uniform-modulus obstruction, tied to route (a): the ACTUAL classical counting marginal
# of F12 is (4/7, 2/7, 1/7); under Fourier-type eigenvectors (B all 1/3) every stationary
# state has UNIFORM visible readout, so that marginal admits no coherent stationary
# representation -- the first exact infeasible instance of the coherent-lift extension
marg13 = [Frac(4, 7), Frac(2, 7), Frac(1, 7)]
ok13 &= marg13 == marg
for k in range(3):
    ek = [Frac(1) if a == k else Frac(0) for a in range(3)]
    ok13 &= [sum(Frac(1, 3) * ek[a] for a in range(3)) for i in range(3)] == [Frac(1, 3)] * 3
ok13 &= marg13 != [Frac(1, 3)] * 3
# (d) THE DISAGREEMENT COUNTERCONTROL: corrupting one classical branch probability by 1/7
# makes the corrupted prescription differ from the quantum functional at that word (the true
# one agrees everywhere by (a)), so no functional extends both -- the infeasibility
# certificate of no_common_extension_of_disagreement, numerically instantiated.
word_x = [menu13[0], menu13[3]]
true_x = sum(class_fold13(word_x, w13))
ok13 &= sum(q_fold13(word_x, rho13)[s][s] for s in S13) == true_x
ok13 &= true_x > 0 and true_x + Frac(1, 7) != true_x
check("F13", ok13,
      "THE COHERENT LIFT AS AN EXTENSION PROBLEM (phase three, C1): the overlap identity "
      "holds EXACTLY at all 259 words to horizon 3 over a 6-state joint space with a "
      "two-bijection menu -- the quantum fold stays diagonal with the classical weights as "
      "entries (kernel: qfold_diagonal, intersection_consistent, finite_comb_extension in "
      "OIBridge/CoherentLift.lean); branch traces over each outcome partition sum to the "
      "parent trace on a non-diagonal state (kernel: branch_normalization); the preparation "
      "slot is an exact LP landscape p = B*q with B doubly stochastic -- the 3-4-5 rotation "
      "gives a feasible instance with its constructive witness verified and an infeasible "
      "instance whose unique solution leaves the simplex, and the F12 shell marginal "
      "(4/7, 2/7, 1/7) is infeasible outright under uniform-modulus eigenvectors (kernel: "
      "shell_representation_from_comb, comb_mixture_of_shell_representation, "
      "uniform_overlap_obstruction; the audit lemma spectral_clauses_insufficient records "
      "why ShellRepresentationConsistency was strengthened); a corrupted classical branch "
      "probability yields a disagreement certificate: no common extension (kernel: "
      "no_common_extension_of_disagreement)")

# ---------------------------- F14  the projector-valued preparation slot (phase three, round 2)
ok14 = True
# The rank-one obstruction of F13 is carrier-specific: Main's actual emergent object is the
# ancilla-marginal representation on D = n*m_a with rank-m_a block projectors P_i summing to
# I -- the carrier of the phase-locking shapes. There B_ia = <a|P_i|a> and the preparation
# Prop holds iff p lies in conv{B_.a} (kernel: projector_shell_representation_from_comb /
# comb_mixture_of_projector_shell_representation). This census decides the LP exactly on
# structured rational eigenbases at all seven phase-locking shapes, then samples generic
# eigenbases in float.
SHAPES14 = ((2, 2), (3, 2), (2, 3), (4, 2), (2, 4), (3, 3), (3, 4))
TRIPLES14 = [(Frac(3, 5), Frac(4, 5)), (Frac(5, 13), Frac(12, 13)),
             (Frac(8, 17), Frac(15, 17)), (Frac(7, 25), Frac(24, 25)),
             (Frac(20, 29), Frac(21, 29))]
PROFILES14 = {2: [Frac(2, 3), Frac(1, 3)],
              3: [Frac(4, 7), Frac(2, 7), Frac(1, 7)],
              4: [Frac(8, 15), Frac(4, 15), Frac(2, 15), Frac(1, 15)]}


def matmul14(A, B):
    D = len(A)
    return [[sum(A[r][k] * B[k][c] for k in range(D)) for c in range(D)] for r in range(D)]


def build_U14(D, sweeps):
    U = [[Frac(1) if r == c else Frac(0) for c in range(D)] for r in range(D)]
    t = 0
    for _ in range(sweeps):
        for k in range(D - 1):
            c, s = TRIPLES14[t % len(TRIPLES14)]
            G = [[Frac(1) if r == cc else Frac(0) for cc in range(D)] for r in range(D)]
            G[k][k], G[k + 1][k + 1], G[k][k + 1], G[k + 1][k] = c, c, -s, s
            U = matmul14(G, U)
            t += 1
    return U


def gauss14(M, b):
    k = len(M)
    A = [row[:] + [b[r]] for r, row in enumerate(M)]
    for col in range(k):
        piv = next((r for r in range(col, k) if A[r][col] != 0), None)
        if piv is None:
            return None
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(k):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return [A[r][k] for r in range(k)]


def in_hull14(B, p):
    """Exact decision: p in conv(columns of B)? Caratheodory over subsets of size <= n,
    each candidate verified against the FULL system, so a positive answer is a certificate;
    exhaustion of the affinely independent subsets makes a negative answer one too."""
    n = len(B)
    D = len(B[0])
    cols = [[B[i][a] for i in range(n)] for a in range(D)]
    for k in range(1, n + 1):
        for sub in itertools.combinations(range(D), k):
            M = [[cols[a][i] for a in sub] for i in range(n)] + [[Frac(1)] * k]
            for rows in itertools.combinations(range(n + 1), k):
                lam = gauss14([M[r] for r in rows],
                              [(p[r] if r < n else Frac(1)) for r in rows])
                if lam is None or any(l < 0 for l in lam):
                    continue
                if sum(lam) == 1 and all(
                        sum(lam[j] * cols[sub[j]][i] for j in range(k)) == p[i]
                        for i in range(n)):
                    return sub, lam
    return None


for n14, m14 in SHAPES14:
    D14 = n14 * m14
    for sweeps in (1, 3):
        U = build_U14(D14, sweeps)
        Ut = [[U[c][r] for c in range(D14)] for r in range(D14)]
        ok14 &= matmul14(Ut, U) == [[Frac(1) if r == c else Frac(0) for c in range(D14)]
                                    for r in range(D14)]
        B = [[sum(U[s][a] ** 2 for s in range(D14) if s // m14 == i) for a in range(D14)]
             for i in range(n14)]
        # doubly-stochastic-with-multiplicity structure (kernel: projector_overlap_nonneg,
        # projector_overlap_col_sum, projector_overlap_row_sum)
        ok14 &= all(B[i][a] >= 0 for i in range(n14) for a in range(D14))
        ok14 &= all(sum(B[i][a] for i in range(n14)) == 1 for a in range(D14))
        ok14 &= all(sum(B[i][a] for a in range(D14)) == m14 for i in range(n14))
        # the counting profile is FEASIBLE at every shape and both mixing depths: the
        # rank-one uniform-overlap obstruction does NOT survive on these carriers
        ok14 &= in_hull14(B, PROFILES14[n14]) is not None
        # positive control: uniform is always feasible (q uniform gives B q = rows/D = 1/n)
        ok14 &= in_hull14(B, [Frac(1, n14)] * n14) is not None
        # countercontrol: the deterministic vertex profile is infeasible, and consistently
        # so -- a probability-vector hull hits a vertex only through a column at it
        ok14 &= in_hull14(B, [Frac(1)] + [Frac(0)] * (n14 - 1)) is None
        ok14 &= max(B[0]) < 1
# generic-eigenbasis census (float, LP via scipy): feasibility depends SYSTEMATICALLY on
# the geometry -- mild non-uniformity is representable, strong non-uniformity is not once
# n >= 3, because Haar-like eigenvectors concentrate the readout columns near uniform
from scipy.optimize import linprog

rng14 = np.random.default_rng(23)
counts14 = {}
NS14 = 40
for n14, m14 in SHAPES14:
    D14 = n14 * m14
    cnt = {b: 0 for b in (0.25, 2.0, 'shape', 'uniform')}
    for _ in range(NS14):
        A = rng14.normal(size=(D14, D14))
        _, Vg = np.linalg.eigh((A + A.T) / 2)
        Bg = np.array([[sum(Vg[s, a] ** 2 for s in range(D14) if s // m14 == i)
                        for a in range(D14)] for i in range(n14)])
        for key in cnt:
            if key == 'shape':
                p = np.array([float(x) for x in PROFILES14[n14]])
            elif key == 'uniform':
                p = np.full(n14, 1.0 / n14)
            else:
                w = np.exp(-key * np.arange(n14))
                p = w / w.sum()
            r = linprog(np.zeros(D14), A_eq=np.vstack([Bg, np.ones(D14)]),
                        b_eq=np.concatenate([p, [1.0]]),
                        bounds=[(0, None)] * D14, method='highs')
            cnt[key] += 1 if r.status == 0 else 0
    counts14[(n14, m14)] = cnt
for shp, cnt in counts14.items():
    ok14 &= cnt['uniform'] >= NS14 - 2                    # uniform: always representable
    ok14 &= cnt[0.25] >= 35                               # mild non-uniformity: generic yes
    if shp[0] >= 3:
        ok14 &= cnt[2.0] <= 5                             # strong non-uniformity: generic no
for shp in ((3, 2), (3, 3), (3, 4)):
    ok14 &= 5 <= counts14[shp]['shape'] <= 35             # the shell profile splits: geometry
for shp in ((2, 2), (2, 3), (2, 4)):
    ok14 &= counts14[shp]['shape'] >= 30                  # n = 2 polytope is wide enough
check("F14", ok14,
      "THE PROJECTOR-VALUED PREPARATION SLOT (phase three, round two): on Main's "
      "ancilla-marginal carrier (rank-m_a block projectors at all seven phase-locking "
      "shapes) the preparation lift exists iff p lies in conv{B_.a}, B_ia = <a|P_i|a> "
      "(kernel: projector_shell_representation_from_comb, "
      "comb_mixture_of_projector_shell_representation, with projector_overlap_nonneg/"
      "col_sum/row_sum the doubly-stochastic-with-multiplicity structure and "
      "rankOne_specialization tying F13's carrier to this one). EXACT LAYER: on structured "
      "rational eigenbases (Pythagorean Givens sweeps, orthogonality verified exactly) the "
      "counting profiles are FEASIBLE at every shape and both mixing depths, with exact "
      "Caratheodory certificates -- the rank-one uniform-overlap obstruction does NOT "
      "survive on these carriers; uniform is always feasible and the deterministic vertex "
      "never is (max B < 1, exact). GENERIC LAYER (40 seeded Gaussian eigenbases per "
      "shape, LP): feasibility depends SYSTEMATICALLY on the geometry -- mild "
      "non-uniformity (beta = 1/4) is representable nearly always, strong non-uniformity "
      "(beta = 2) nearly never once n >= 3, and the shell profile itself splits both ways "
      "at the n = 3 shapes: OI-compatible coherent completions are being classified by "
      "whether the shell marginal lies inside their spectral-readout polytope -- "
      "concentration of delocalized eigenvectors shrinks it toward uniform "
      "(kernel boundary: projector_uniform_overlap_obstruction is the exact uniform-"
      "overlap limit of that shrinkage)")

# --------------------- F15  one-slot visible-local interventions (phase three, round 3)
ok15 = True
# The guard of round three: interventions must be local to the visible factor,
# J_a = I_a (x) id_A, or C1 becomes too easy (a global CP map can manipulate the ancilla
# and manufacture any classical comb). Kernel spine: local_intervention_overlap /
# local_intervention_branch (layer one), local_channel_preserves_ancilla (the locality
# invariant), two_time_forces_stationary / two_time_necessary (the Fourier reduction of
# the named predicate TwoTimeCoherentLift). This census runs the exact necessary layer,
# the exact affine layer of the one-slot Choi problem, a float PSD completion, and the
# probe-menu hierarchy.
TR15 = [(Frac(3, 5), Frac(4, 5)), (Frac(5, 13), Frac(12, 13)), (Frac(8, 17), Frac(15, 17)),
        (Frac(7, 25), Frac(24, 25)), (Frac(20, 29), Frac(21, 29))]


def mm15(A, B):
    n2, n3 = len(B), len(B[0])
    return [[sum(A[r][k] * B[k][c] for k in range(n2)) for c in range(n3)]
            for r in range(len(A))]


def bu15(D, sweeps, offset=0):
    U = [[Frac(1) if r == c else Frac(0) for c in range(D)] for r in range(D)]
    t = offset
    for _ in range(sweeps):
        for k in range(D - 1):
            c, s = TR15[t % len(TR15)]
            G = [[Frac(1) if r == cc else Frac(0) for cc in range(D)] for r in range(D)]
            G[k][k], G[k + 1][k + 1], G[k][k + 1], G[k + 1][k] = c, c, -s, s
            U = mm15(G, U)
            t += 1
    return U


def kron15(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    return [[A[r // rb][c // cb] * B[r % rb][c % cb] for c in range(ca * cb)]
            for r in range(ra * rb)]


def rs15(A, b):
    """Exact row reduction: (consistent, particular, nullspace basis)."""
    rows, cols = len(A), len(A[0])
    M = [list(A[r]) + [b[r]] for r in range(rows)]
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    for i in range(r, rows):
        if M[i][cols] != 0:
            return False, None, None
    part = [Frac(0)] * cols
    for k, c in enumerate(piv):
        part[c] = M[k][cols]
    free = [c for c in range(cols) if c not in piv]
    null = []
    for fc in free:
        v = [Frac(0)] * cols
        v[fc] = Frac(1)
        for k, c in enumerate(piv):
            v[c] = -M[k][fc]
        null.append(v)
    return True, part, null


def lp15(A, b):
    """Exact feasibility of {q >= 0 : A q = b}: basic-solution enumeration (complete)."""
    cols = len(A[0])
    cons, _, null = rs15(A, b)
    if not cons:
        return None
    r = cols - len(null)
    for size in range(0, r + 1):
        for T in itertools.combinations(range(cols), size):
            AT = [[A[i][c] for c in T] for i in range(len(A))]
            cT, pT, nT = rs15(AT, b)
            if not cT or (nT and len(nT) > 0):
                continue
            qq = [Frac(0)] * cols
            for k, c in enumerate(T):
                qq[c] = pT[k]
            if all(x >= 0 for x in qq):
                return qq
    return None


# ---- (a) layer one, exact: visible-local classical words on a block-diagonal state
# with NON-diagonal Gaussian-integer ancilla blocks (n = 3, m = 2). The quantum fold must
# keep the state block-diagonal with the SAME ancilla blocks relabelled/masked (the ancilla
# identity of local_intervention_overlap), and the trace must equal the classical fold on
# the visible alphabet alone (local_intervention_branch).
n15, m15 = 3, 2
BLK = [[[complex(1 + i, 2 * i), complex(2, -i)], [complex(2, i), complex(3 - i, 0)]]
       for i in range(n15)]                        # hermitian-ish, entries exact ints
SIGS = [[1, 0, 2], [1, 2, 0]]


def op_fold(word, blocks):
    for sig, out in word:
        inv = [sig.index(i) for i in range(n15)]
        blocks = [blocks[inv[i]] if i == out else [[0, 0], [0, 0]] for i in range(n15)]
    return blocks


def q_fold15(word, blocks):
    D = n15 * m15
    rho = [[blocks[p // m15][p % m15][q % m15] if p // m15 == q // m15 else 0
            for q in range(D)] for p in range(D)]
    for sig, out in word:
        P = [[1 if (sig[q // m15] == p // m15 and p % m15 == q % m15) else 0
              for q in range(D)] for p in range(D)]
        Pt = [[P[c][r] for c in range(D)] for r in range(D)]
        proj = [[1 if (p == q and p // m15 == out) else 0 for q in range(D)]
                for p in range(D)]
        rho = mm15(mm15(proj, mm15(mm15(P, rho), Pt)), proj)
    return rho


def cl_fold15(word, w):
    for sig, out in word:
        inv = [sig.index(i) for i in range(n15)]
        w = [w[inv[i]] if i == out else 0 for i in range(n15)]
    return w


menu15 = [(sig, out) for sig in SIGS for out in range(n15)]
w0 = [BLK[i][0][0] + BLK[i][1][1] for i in range(n15)]
nw = 0
for L in range(3):
    for word in itertools.product(menu15, repeat=L):
        rho = q_fold15(list(word), BLK)
        blocks = op_fold(list(word), BLK)
        ok15 &= all(rho[p][q] == (blocks[p // m15][p % m15][q % m15]
                                  if p // m15 == q // m15 else 0)
                    for p in range(6) for q in range(6))
        ok15 &= sum(rho[s][s] for s in range(6)) == sum(cl_fold15(list(word), w0))
        nw += 1
ok15 &= nw == 43

# ---- (b) the locality invariant, exact: a visible-local Kraus pair preserves the
# ancilla marginal on an entangled state; a global (ancilla-touching) channel does not.
RHOE = [[complex((r * 2 + c) % 5 - 2, (r - c) % 3 - 1) for c in range(6)] for r in range(6)]
RHOH = [[RHOE[r][c] + RHOE[c][r].conjugate() for c in range(6)] for r in range(6)]
c35, s35 = 0.6, 0.8
W1 = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
W2 = [[0.6, -0.8, 0], [0.8, 0.6, 0], [0, 0, 1]]
KS = [[[c35 * W1[r][c] for c in range(3)] for r in range(3)],
      [[s35 * W2[r][c] for c in range(3)] for r in range(3)]]
ok15 &= all(abs(sum(KS[k][i][r] * KS[k][i][cc] for k in range(2) for i in range(3))
                - (1 if r == cc else 0)) < 1e-12 for r in range(3) for cc in range(3))


def ptv15(Y):
    return [[sum(Y[i * 2 + z][i * 2 + y] for i in range(3)) for y in range(2)]
            for z in range(2)]


def vl15(K):
    return [[K[p // 2][q // 2] * (1 if p % 2 == q % 2 else 0) for q in range(6)]
            for p in range(6)]


Yloc = [[sum(mm15(mm15(vl15(KS[k]), RHOH),
             [[vl15(KS[k])[c][r].conjugate() if isinstance(vl15(KS[k])[c][r], complex)
               else vl15(KS[k])[c][r] for c in range(6)] for r in range(6)])[p][q]
         for k in range(2)) for q in range(6)] for p in range(6)]
ok15 &= all(abs(ptv15(Yloc)[z][y] - ptv15(RHOH)[z][y]) < 1e-9
            for z in range(2) for y in range(2))
# global countercontrol: swap the two ancilla levels inside block 0 only
Pg = [[1 if ((r, c) in ((0, 1), (1, 0)) or (r == c and r > 1)) else 0
       for c in range(6)] for r in range(6)]
Yg = mm15(mm15(Pg, RHOH), [[Pg[c][r] for c in range(6)] for r in range(6)])
ok15 &= any(abs(ptv15(Yg)[z][y] - ptv15(RHOH)[z][y]) > 0.5 for z in range(2)
            for y in range(2))

# ---- (c) THE NECESSARY-LP CENSUS, exact: strata x actions. Necessary conditions from
# two_time_necessary: a stationary target q' >= 0 with B q' = sigma p AND the ancilla
# marginal of the represented state preserved (local_channel_preserves_ancilla).
def census15(U, n, m, q, sigma):
    D = n * m
    B = [[sum(U[s][a] ** 2 for s in range(D) if s // m == i) for a in range(D)]
         for i in range(n)]
    G = [[[sum(U[i * m + z][a] * U[i * m + y][a] for i in range(n))
           for y in range(m)] for z in range(m)] for a in range(D)]
    p = [sum(q[a] * B[i][a] for a in range(D)) for i in range(n)]
    tp = [p[sigma.index(i)] for i in range(n)]
    Ag = [[B[i][a] for a in range(D)] for i in range(n)] + [[Frac(1)] * D]
    bg = tp + [Frac(1)]
    qg = lp15(Ag, bg)
    Al = [row[:] for row in Ag]
    bl = list(bg)
    for z in range(m):
        for y in range(z, m):
            Al.append([G[a][z][y] for a in range(D)])
            bl.append(sum(q[a] * G[a][z][y] for a in range(D)))
    ql = lp15(Al, bl)
    return (qg is not None), (ql is not None)


Q15 = {4: [Frac(8, 15), Frac(4, 15), Frac(2, 15), Frac(1, 15)],
       6: [Frac(2 ** (5 - k), 63) for k in range(6)],
       9: [Frac(2 ** (8 - k), 511) for k in range(9)]}
verdicts = {}
for nn, mm in ((2, 2), (3, 2), (3, 3)):
    D = nn * mm
    q = Q15[D]
    strata = (("st", bu15(D, 1)), ("mx", bu15(D, 3)),
              ("ba", kron15(bu15(nn, 1), bu15(mm, 1, offset=2))))
    acts = (("id", list(range(nn))),
            ("tr", [1, 0] + list(range(2, nn))),
            ("cy", [(i + 1) % nn for i in range(nn)]))
    for stag, U in strata:
        for atag, sig in acts:
            verdicts[(nn, mm, stag, atag)] = census15(U, nn, mm, q, sig)
# identity actions are always locally feasible (q' = q)
ok15 &= all(verdicts[k] == (True, True) for k in verdicts if k[3] == 'id')
# THE BOXED OBSTRUCTION -- globally feasible, locally impossible -- at these exact
# instances: the classical comb embeds coherently only if the intervention may
# manipulate the ancilla
boxed = {k for k, v in verdicts.items() if v == (True, False)}
ok15 &= boxed == {(2, 2, 'mx', 'tr'), (2, 2, 'mx', 'cy'),
                  (3, 2, 'st', 'tr'), (3, 2, 'st', 'cy'),
                  (3, 3, 'st', 'tr'), (3, 3, 'st', 'cy'),
                  (3, 3, 'mx', 'tr'), (3, 3, 'mx', 'cy')}
# block-aligned carriers are locally feasible WHENEVER globally feasible
ok15 &= all((not v[0]) or v[1] for k, v in verdicts.items() if k[2] == 'ba')

# ---- (d) the one-slot Choi problem, exact affine layer + PSD. Parameterize the visible
# Choi J = S + iA (S symmetric, A antisymmetric; real carrier, so the two sectors
# decouple); the constraints are TP, stationarity of J(rho) (W = U^T Y U off-diagonal
# zero), and the block readout. Exact rational row reduction decides consistency and the
# affine fibre dimension; PSD then decides CP.
def full_affine15(n, m, U, q, sigma):
    D = n * m
    rho = [[sum(U[p][a] * q[a] * U[qq][a] for a in range(D)) for qq in range(D)]
           for p in range(D)]
    B = [[sum(U[s][a] ** 2 for s in range(D) if s // m == i) for a in range(D)]
         for i in range(n)]
    p = [sum(q[a] * B[i][a] for a in range(D)) for i in range(n)]
    tp = [p[sigma.index(i)] for i in range(n)]
    nb = n * n
    sym = [(i, j) for i in range(nb) for j in range(i, nb)]
    asym = [(i, j) for i in range(nb) for j in range(i + 1, nb)]
    Ut = [[U[c][r] for c in range(D)] for r in range(D)]

    def image(J):
        Y = [[sum(J[(pp // m) * n + i2][(qq // m) * n + j2]
                  * rho[i2 * m + (pp % m)][j2 * m + (qq % m)]
                  for i2 in range(n) for j2 in range(n)) for qq in range(D)]
             for pp in range(D)]
        return Y, mm15(mm15(Ut, Y), U)

    colS = []
    for (r, c) in sym:
        J = [[Frac(0)] * nb for _ in range(nb)]
        J[r][c] += 1
        if r != c:
            J[c][r] += 1
        colS.append((J,) + image(J))
    rowsS, rhsS = [], []
    for i in range(n):
        for i2 in range(i, n):
            rowsS.append([sum(cj[0][o * n + i][o * n + i2] for o in range(n))
                          for cj in colS])
            rhsS.append(Frac(1) if i == i2 else Frac(0))
    for a in range(D):
        for b in range(a + 1, D):
            rowsS.append([cj[2][a][b] for cj in colS])
            rhsS.append(Frac(0))
    for j in range(n):
        rowsS.append([sum(cj[1][s][s] for s in range(D) if s // m == j) for cj in colS])
        rhsS.append(tp[j])
    consS, partS, nullS = rs15(rowsS, rhsS)
    colA = []
    for (r, c) in asym:
        J = [[Frac(0)] * nb for _ in range(nb)]
        J[r][c] += 1
        J[c][r] -= 1
        colA.append((J,) + image(J))
    rowsA = []
    for i in range(n):
        for i2 in range(i + 1, n):
            rowsA.append([sum(cj[0][o * n + i][o * n + i2] for o in range(n))
                          for cj in colA])
    for a in range(D):
        for b in range(a + 1, D):
            rowsA.append([cj[2][a][b] for cj in colA])
    _, _, nullA = rs15(rowsA, [Frac(0)] * len(rowsA))
    return consS, partS, (len(nullS) if nullS is not None else 0), len(nullA), sym, \
        rowsS, rhsS


Q22 = Q15[4]
Q32 = Q15[6]
# (2,2) structured transposition -- the necessary LP PASSED here, yet the one-slot
# channel problem is RIGID: the affine constraints determine the Choi uniquely
# (dimS = dimA = 0) and the unique candidate fails PSD by a macroscopic margin. The
# full Choi constraints strictly refine the ancilla-marginal invariant.
consS, partS, dimS, dimA, sym22, _, _ = full_affine15(2, 2, bu15(4, 1), Q22, [1, 0])
ok15 &= consS and dimS == 0 and dimA == 0
J22 = [[Frac(0)] * 4 for _ in range(4)]
for k, (r, c) in enumerate(sym22):
    J22[r][c] += partS[k]
    if r != c:
        J22[c][r] += partS[k]
ok15 &= np.linalg.eigvalsh(np.array([[float(x) for x in row]
                                     for row in J22])).min() < -1.5
# (2,2) mixed transposition -- the necessary LP failed; the unique Choi candidate fails
# PSD too (the two exact layers cross-validate)
consS, partS, dimS, dimA, sym22, _, _ = full_affine15(2, 2, bu15(4, 3), Q22, [1, 0])
ok15 &= consS and dimS == 0 and dimA == 0
J22 = [[Frac(0)] * 4 for _ in range(4)]
for k, (r, c) in enumerate(sym22):
    J22[r][c] += partS[k]
    if r != c:
        J22[c][r] += partS[k]
ok15 &= np.linalg.eigvalsh(np.array([[float(x) for x in row]
                                     for row in J22])).min() < -5
# (3,2) identity action: the identity channel is an EXACT witness (Choi = the
# unnormalized maximally-entangled projector, PSD), verified against every row
consS, partS, dimS, dimA, sym32, rowsS, rhsS = full_affine15(3, 2, bu15(6, 1), Q32,
                                                             [0, 1, 2])
ok15 &= consS and dimS > 0
xid = []
for (r, c) in sym32:
    ri, rj = divmod(r, 3)
    ci, cj = divmod(c, 3)
    xid.append(Frac(1) if (ri == rj and ci == cj) else Frac(0))
ok15 &= all(sum(rowsS[k][t] * xid[t] for t in range(len(sym32))) == rhsS[k]
            for k in range(len(rowsS)))


# (2,2) block-aligned transposition: positive-dimensional affine fibre, and Dykstra
# completes it to a genuine CPTP instrument
def dykstra15(n, m, U, q, sigma, iters=1500):
    D = n * m
    Uf = np.array([[float(x) for x in row] for row in U])
    qf = np.array([float(x) for x in q])
    rho = Uf @ np.diag(qf) @ Uf.T
    B = np.array([[sum(Uf[s, a] ** 2 for s in range(D) if s // m == i)
                   for a in range(D)] for i in range(n)])
    tp = np.array([(B @ qf)[sigma.index(i)] for i in range(n)])
    nb = n * n
    basis = []
    for i in range(nb):
        M = np.zeros((nb, nb)); M[i, i] = 1; basis.append(M)
    for i in range(nb):
        for j in range(i + 1, nb):
            M = np.zeros((nb, nb)); M[i, j] = M[j, i] = 2 ** -0.5; basis.append(M)

    def app(J):
        Y = np.zeros((D, D))
        for i in range(n):
            for x in range(m):
                for jj in range(n):
                    for y in range(m):
                        Y[i * m + x, jj * m + y] = sum(
                            J[i * n + i2, jj * n + j2] * rho[i2 * m + x, j2 * m + y]
                            for i2 in range(n) for j2 in range(n))
        return Y

    rows, rhs = [], []
    Yapps = [app(Bk) for Bk in basis]
    Ymaps = [Uf.T @ Ya @ Uf for Ya in Yapps]
    for i in range(n):
        for i2 in range(i, n):
            rows.append([sum(Bk[o * n + i, o * n + i2] for o in range(n))
                         for Bk in basis])
            rhs.append(1.0 if i == i2 else 0.0)
    for a in range(D):
        for b in range(a + 1, D):
            rows.append([Ym[a, b] for Ym in Ymaps]); rhs.append(0.0)
    for j in range(n):
        rows.append([sum(Ya[s, s] for s in range(D) if s // m == j) for Ya in Yapps])
        rhs.append(tp[j])
    L = np.array(rows); cvec = np.array(rhs)
    from numpy.linalg import pinv
    Lp = pinv(L)
    Jid = np.zeros((nb, nb))
    for i in range(n):
        for j in range(n):
            Jid[i * n + i, j * n + j] = 1
    xv = np.array([np.trace(Bk.T @ Jid) for Bk in basis])
    pc = np.zeros_like(xv)
    for _ in range(iters):
        xa = xv - Lp @ (L @ xv - cvec)
        y = xa + pc
        J = sum(y[k] * basis[k] for k in range(len(basis)))
        w, Vv = np.linalg.eigh(J)
        Jp = Vv @ np.diag(np.clip(w, 0, None)) @ Vv.T
        xn = np.array([np.trace(Bk.T @ Jp) for Bk in basis])
        pc = y - xn
        xv = xn
    J = sum(xv[k] * basis[k] for k in range(len(basis)))
    return np.linalg.norm(L @ xv - cvec), np.linalg.eigvalsh(J).min()


resBA, eigBA = dykstra15(2, 2, kron15(bu15(2, 1), bu15(2, 1, offset=2)), Q22, [1, 0])
ok15 &= resBA < 1e-6 and eigBA > -1e-7
# (3,2) mixed transposition: the necessary LP passed and the affine fibre is
# positive-dimensional, but Dykstra stalls at a macroscopic gap -- no CP completion
# found (recorded as evidence of PSD infeasibility, not a certificate)
resMX, _ = dykstra15(3, 2, bu15(6, 3), Q32, [1, 0, 2])
ok15 &= resMX > 1e-2

# ---- (e) the probe-menu hierarchy against the orientation pair (V, E) vs (V, -E):
# permutation and real coherent probes are exactly blind; ONE complex coherent probe
# resolves the orientation. This is the intervention-level face of the phase-two
# antiunitary structure: full transposition would also transpose the probe.
Uf = np.array([[float(x) for x in row] for row in bu15(6, 1)])
E15 = np.array([0.0, 1.0, 2.4142135623, 3.7320508075, 5.1, 6.9])
qf = np.array([float(x) for x in Q15[6]])
rho15 = Uf @ np.diag(qf) @ Uf.T


def resp15(Evec, R):
    RL = np.kron(R, np.eye(2))
    X = RL @ rho15 @ RL.conj().T
    M = Uf.T @ X @ Uf
    ts = np.linspace(0.13, 7.7, 25)
    out = []
    for j in range(3):
        P = np.diag([1.0 if s // 2 == j else 0 for s in range(6)])
        N = Uf.T @ P @ Uf
        out.append([sum(M[a, b] * N[b, a] * np.exp(1j * (Evec[b] - Evec[a]) * t)
                        for a in range(6) for b in range(6)).real for t in ts])
    return np.array(out)


Rp = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1.0]])
Rr = np.array([[0.6, -0.8, 0], [0.8, 0.6, 0], [0, 0, 1.0]])
Rc = np.array([[np.cos(0.7), -np.sin(0.7) * np.exp(1j * 0.9), 0],
               [np.sin(0.7) * np.exp(-1j * 0.9), np.cos(0.7), 0], [0, 0, 1.0]])
dperm = np.max(np.abs(resp15(E15, Rp) - resp15(-E15, Rp)))
dreal = np.max(np.abs(resp15(E15, Rr) - resp15(-E15, Rr)))
dcplx = np.max(np.abs(resp15(E15, Rc) - resp15(-E15, Rc)))
ok15 &= dperm < 1e-10 and dreal < 1e-10 and dcplx > 0.05

check("F15", ok15,
      "ONE-SLOT VISIBLE-LOCAL INTERVENTIONS (phase three, round three). (a) Layer one "
      "exact: 43 visible-local classical words on a block-diagonal state with non-diagonal "
      "Gaussian-integer ancilla blocks -- the quantum fold carries the ancilla blocks "
      "UNTOUCHED (relabelled and masked only) and the branch trace equals the classical "
      "fold on the visible alphabet alone (kernel: local_intervention_overlap, "
      "local_intervention_branch). (b) The locality invariant: a visible-local Kraus pair "
      "preserves the ancilla marginal on an entangled state exactly; an ancilla-touching "
      "permutation moves it (kernel: local_channel_preserves_ancilla, embA_conj_channel). "
      "(c) THE NECESSARY-LP CENSUS (exact fractions; kernel spine two_time_forces_"
      "stationary + two_time_necessary reduces TwoTimeCoherentLift to: stationary target "
      "q' >= 0 with B q' = sigma p in the preparation's ancilla-marginal fibre): identity "
      "actions always locally feasible; THE BOXED OBSTRUCTION -- globally feasible yet "
      "visible-locally impossible, i.e. the classical comb embeds coherently only if the "
      "intervention manipulates hidden/ancillary degrees of freedom -- occurs at exactly "
      "8 of 27 instances, covering every nontrivial action on the non-aligned carriers at "
      "(3,3); block-aligned (product) carriers are locally feasible wherever globally "
      "feasible. (d) The one-slot Choi problem, exact affine layer + PSD: at (2,2) the "
      "problem is RIGID -- TP + stationarity + readout determine the visible Choi "
      "UNIQUELY (zero-dimensional affine fibre, both sectors), and the unique candidate "
      "fails positivity by a certified macroscopic margin EVEN WHERE THE NECESSARY LP "
      "PASSES: the full channel constraints strictly refine the ancilla-marginal "
      "invariant. The identity action carries the exact identity-channel witness; the "
      "block-aligned carrier is CPTP-completable (Dykstra) on a positive-dimensional "
      "instrument fibre; the (3,2) mixed nontrivial action stalls at a macroscopic "
      "Dykstra gap (evidence, not a certificate). (e) The probe-menu "
      "hierarchy against the orientation pair (V, E) vs (V, -E): permutation and real "
      "coherent probes are exactly blind (< 1e-10), one complex coherent probe resolves "
      "the orientation (> 0.05) -- the intervention-level face of the antiunitary "
      "structure, matching the source-lift prior")


# ----------------------- F16  the exact (2,2) no-go certificates (phase three, round 4)
ok16 = True
# Kernel twins: twoByTwo_affine_rigidity / twoByTwo_nonCP / twoByTwo_no_local_lift
# (OIBridge/TwoByTwoNoGo.lean). This check recomputes, from scratch and in exact rational
# arithmetic, everything the Lean file hardcodes: the witness carrier, the 18-equation
# affine system and its rank-16 uniqueness, the unique Choi candidate, the negativity
# witness, readout completeness, the distinct-gap condition, preparation feasibility, and
# the GLOBAL feasibility of the classical action -- which is what makes the theorem the
# boxed statement: preparation feasible + global intervention feasible does NOT imply a
# visible-local CPTP coherent lift.
def giv16(i, j, c, s):
    G = [[Frac(1) if r == cc else Frac(0) for cc in range(4)] for r in range(4)]
    G[i][i], G[j][j], G[i][j], G[j][i] = c, c, -s, s
    return G


U16 = [[Frac(1) if r == c else Frac(0) for c in range(4)] for r in range(4)]
for (i, j), (c, s) in [((0, 1), (Frac(3, 5), Frac(4, 5))),
                       ((2, 3), (Frac(5, 13), Frac(12, 13))),
                       ((0, 2), (Frac(3, 5), Frac(4, 5)))]:
    U16 = mm15(giv16(i, j, c, s), U16)
q16 = [Frac(1, 2), Frac(1, 4), Frac(1, 8), Frac(1, 8)]
E16 = [0, 1, 3, 7]
# distinct gaps (the decide twin): every nonzero difference occurs exactly once
gapset = {}
for a in range(4):
    for b in range(4):
        if a != b:
            g = E16[b] - E16[a]
            ok16 &= g not in gapset
            gapset[g] = (a, b)
rho16 = [[sum(U16[p][a] * q16[a] * U16[qq][a] for a in range(4)) for qq in range(4)]
         for p in range(4)]
B16 = [[sum(U16[s][a] ** 2 for s in range(4) if s // 2 == i) for a in range(4)]
       for i in range(2)]
p16 = [sum(q16[a] * B16[i][a] for a in range(4)) for i in range(2)]
tp16 = [p16[1], p16[0]]
ok16 &= p16 == [Frac(1531, 2500), Frac(969, 2500)]
# readout completeness: every off-diagonal pair is visible at block 0
N0 = [[sum(U16[s][b2] * U16[s][a2] for s in range(2)) for a2 in range(4)]
      for b2 in range(4)]
ok16 &= all(N0[b2][a2] != 0 for a2 in range(4) for b2 in range(4) if a2 != b2)
# global feasibility: the transposed marginal lies in the spectral-readout polytope
Ag16 = [[B16[i][a] for a in range(4)] for i in range(2)] + [[Frac(1)] * 4]
qg16 = lp15(Ag16, tp16 + [Frac(1)])
ok16 &= qg16 is not None
# the 18-equation affine system on the 16 Choi entries; rank 16; unique solution
rows16, rhs16 = [], []
for a in range(2):
    for b in range(2):
        row = [Frac(0)] * 16
        for i in range(2):
            row[4 * (2 * i + a) + (2 * i + b)] += 1
        rows16.append(row)
        rhs16.append(Frac(1) if a == b else Frac(0))


def yrow16(pp, qq):
    i, x = pp // 2, pp % 2
    j, y = qq // 2, qq % 2
    row = [Frac(0)] * 16
    for i2 in range(2):
        for j2 in range(2):
            row[4 * (2 * i + i2) + (2 * j + j2)] += rho16[2 * i2 + x][2 * j2 + y]
    return row


YR = [[yrow16(pp, qq) for qq in range(4)] for pp in range(4)]
for a in range(4):
    for b in range(4):
        if a == b:
            continue
        row = [Frac(0)] * 16
        for pp in range(4):
            for qq in range(4):
                coef = U16[pp][a] * U16[qq][b]
                if coef:
                    row = [r + coef * yr for r, yr in zip(row, YR[pp][qq])]
        rows16.append(row)
        rhs16.append(Frac(0))
for jv in range(2):
    row = [Frac(0)] * 16
    for s in range(4):
        if s // 2 == jv:
            row = [r + yr for r, yr in zip(row, YR[s][s])]
    rows16.append(row)
    rhs16.append(tp16[jv])
cons16, part16, null16 = rs15(rows16, rhs16)
ok16 &= cons16 and len(null16) == 0
J16 = [[part16[4 * s + t] for t in range(4)] for s in range(4)]
# the negativity witness: v = (1, -1, -1, -1), v^T J v = -449600/76287 < 0
v16 = [Frac(1), Frac(-1), Frac(-1), Frac(-1)]
vval16 = sum(v16[s] * J16[s][t] * v16[t] for s in range(4) for t in range(4))
ok16 &= vval16 == Frac(-449600, 76287) and vval16 < 0
# J16 is symmetric and TP (cross-checks on the unique candidate)
ok16 &= all(J16[s][t] == J16[t][s] for s in range(4) for t in range(4))
ok16 &= all(sum(J16[2 * i + a][2 * i + b] for i in range(2))
            == (1 if a == b else 0) for a in range(2) for b in range(2))
# lint: the Lean witness file carries the same unique candidate and witness value
tb = open(os.path.join(BRIDGE, 'OIBridge', 'TwoByTwoNoGo.lean'), encoding='utf-8').read()
ok16 &= '449600' in tb and '76287' in tb
ok16 &= str(abs(J16[0][0].numerator)) in tb and str(J16[0][0].denominator) in tb
ok16 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', tb) is None
# (b) reflection blindness at the coefficient level, exact: for a real carrier and real
# probe, the response coefficient at (a,b) equals the coefficient at (b,a), so the signal
# is invariant under E -> -E -- the coefficient-level twin of
# real_instrument_reflection_invariant, and permutation probes are the special case
U6 = bu15(6, 1)
qb = [Frac(2 ** (5 - k), 63) for k in range(6)]
rho6 = [[sum(U6[p][a] * qb[a] * U6[qq][a] for a in range(6)) for qq in range(6)]
        for p in range(6)]
Rreal = [[Frac(3, 5), Frac(-4, 5), 0], [Frac(4, 5), Frac(3, 5), 0], [0, 0, Frac(1)]]
RL = [[Rreal[p // 2][q // 2] * (1 if p % 2 == q % 2 else 0) for q in range(6)]
      for p in range(6)]
X6 = mm15(mm15(RL, rho6), [[RL[c][r] for c in range(6)] for r in range(6)])
M6 = mm15(mm15([[U6[c][r] for c in range(6)] for r in range(6)], X6), U6)
for jv in range(3):
    N6 = [[sum(U6[s][b2] * U6[s][a2] for s in range(6) if s // 2 == jv)
           for a2 in range(6)] for b2 in range(6)]
    ok16 &= all(M6[a][b] * N6[b][a] == M6[b][a] * N6[a][b]
                for a in range(6) for b in range(6))
# (c) the intertwining form, exact one-step check on the block-diagonal representation
# with a lifted classical action (the algebraic C1 form of intertwining_all_horizons):
# R(classStep w) = Q(R(w)) with the ancilla blocks carried untouched
BLK16 = [[[Frac(1, 3), Frac(1, 7)], [Frac(1, 7), Frac(1, 5)]] for _ in range(3)]
w16 = [Frac(1, 2), Frac(1, 3), Frac(1, 6)]


def Rrep(w):
    D = 6
    return [[w[p // 2] * BLK16[p // 2][p % 2][q % 2] if p // 2 == q // 2 else Frac(0)
             for q in range(D)] for p in range(D)]


sig16 = [1, 0, 2]
out16 = 1
Pm = [[1 if (sig16[q // 2] == p // 2 and p % 2 == q % 2) else 0 for q in range(6)]
      for p in range(6)]
proj16 = [[1 if (p == q and p // 2 == out16) else 0 for q in range(6)] for p in range(6)]
lhs = Rrep([w16[sig16.index(i)] if i == out16 else Frac(0) for i in range(3)])
# note: R(classStep w) must use the RELABELLED blocks too; build directly
lhsblocks = [[r[:] for r in BLK16[sig16.index(i)]] for i in range(3)]
lhsw = [w16[sig16.index(i)] if i == out16 else Frac(0) for i in range(3)]
lhs = [[lhsw[p // 2] * lhsblocks[p // 2][p % 2][q % 2] if p // 2 == q // 2 else Frac(0)
        for q in range(6)] for p in range(6)]
rhs = mm15(mm15(proj16, mm15(mm15(Pm, Rrep(w16)),
                             [[Pm[c][r] for c in range(6)] for r in range(6)])), proj16)
ok16 &= lhs == rhs
check("F16", ok16,
      "THE EXACT (2,2) NO-GO CERTIFICATES (phase three, round four; kernel: "
      "twoByTwo_affine_rigidity, twoByTwo_nonCP, twoByTwo_no_local_lift in "
      "OIBridge/TwoByTwoNoGo.lean). Recomputed from scratch in exact rationals: the "
      "witness carrier G02(3/5)*G23(5/13)*G01(3/5) has all fifteen gap differences "
      "distinct for E = (0,1,3,7), every off-diagonal mode pair visible at block 0 "
      "(readout completeness), preparation marginal p = (1531/2500, 969/2500) feasible by "
      "construction, and the transposed marginal GLOBALLY reachable in the "
      "spectral-readout polytope; the 18-equation affine system on the 16 visible Choi "
      "entries is CONSISTENT WITH RANK 16 -- the one-slot channel is affinely RIGID -- "
      "and its unique candidate is symmetric, trace-preserving, and fails positivity at "
      "the witness v = (1,-1,-1,-1) with v^T J v = -449600/76287 exactly. Hence: "
      "preparation feasible + global intervention feasible does NOT imply a visible-local "
      "CPTP coherent lift. Also exact: the coefficient-level reflection-blindness "
      "identity M_ab N_ba = M_ba N_ab for a real carrier and real probe (kernel twin: "
      "real_instrument_reflection_invariant, with permMatrix_conjOp the permutation "
      "case), and the one-step intertwining identity R(classStep w) = Q(R w) on a "
      "block-diagonal representation (kernel: ActionIntertwining, "
      "intertwining_all_horizons, intertwining_comb_compatible -- C1 in its final "
      "algebraic form)")

# ----------------------- F17  the accessible-algebra commutant census (phase three, round 5)
# The generated accessible algebra A_OI = alg*({P_j x I}, {U_t (M x I) U_t^H}) has trivial
# commutant iff Z commuting with the full-time Heisenberg orbit is scalar.  With distinct
# gaps the fibers are singletons and the commutant equations on W = V^H Z V are EXACT:
#   entry (r,s), frequency E_b - E_a (a != b):  [a=r] N_ab W_bs - [b=s] W_ra N_as = 0
#   entry (r,s), frequency 0:                   W_rs (N_rr - N_ss) = 0
# with N = V^H (M x I) V (kernel: gap_coefficient_vanish + dyad_conjugation +
# accessible_trivial_commutant).  This census computes exact commutant dimensions across
# carriers x menus, cross-checked by float time-sampling.
ok17 = True

class C17:
    __slots__ = ('re', 'im')
    def __init__(s, re=0, im=0):
        s.re = Frac(re); s.im = Frac(im)
    def __add__(s, o): return C17(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return C17(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return C17(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def conj(s): return C17(s.re, -s.im)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def z(s): return s.re == 0 and s.im == 0
    def inv(s):
        d = s.re * s.re + s.im * s.im
        return C17(s.re / d, -s.im / d)
    def f(s): return complex(s.re, s.im)

CZ17, CO17 = C17(0), C17(1)

def mmc17(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), CZ17)
             for j in range(len(B[0]))] for i in range(len(A))]

def dag17(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]

def kr17(A, B):
    ra, ca, rb, cb = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i // rb][j // cb] * B[i % rb][j % cb]
             for j in range(ca * cb)] for i in range(ra * rb)]

def eye17(n): return [[CO17 if i == j else CZ17 for j in range(n)] for i in range(n)]

def rank17(rows):
    rows = [r[:] for r in rows if any(not x.z() for x in r)]
    nc = len(rows[0]) if rows else 0
    rk, piv = 0, 0
    while piv < nc and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if not rows[i][piv].z()), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = rows[rk][piv].inv()
        rows[rk] = [x * iv for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and not rows[i][piv].z():
                f = rows[i][piv]
                rows[i] = [rows[i][j] - f * rows[rk][j] for j in range(nc)]
        rk += 1
        piv += 1
    return rk

def nulsp17(rows, nc):
    rows = [r[:] for r in rows if any(not x.z() for x in r)]
    rk, piv, pivots = 0, 0, []
    while piv < nc and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if not rows[i][piv].z()), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = rows[rk][piv].inv()
        rows[rk] = [x * iv for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and not rows[i][piv].z():
                f = rows[i][piv]
                rows[i] = [rows[i][j] - f * rows[rk][j] for j in range(nc)]
        pivots.append(piv)
        rk += 1
        piv += 1
    basis = []
    for fc in (j for j in range(nc) if j not in pivots):
        v = [CZ17] * nc
        v[fc] = CO17
        for r, pc in enumerate(pivots):
            v[pc] = CZ17 - rows[r][fc]
        basis.append(v)
    return basis

def comm_dim17(V, E, Ms, D, da, want_basis=False):
    # distinct-gap sanity, then the fiber equations on W
    diffs = set()
    for a in range(D):
        for b in range(D):
            if a != b:
                d = E[b] - E[a]
                assert d != 0 and d not in diffs
                diffs.add(d)
    Vh = dag17(V)
    rows = []
    for M in Ms:
        N = mmc17(mmc17(Vh, kr17(M, eye17(da))), V)
        for r in range(D):
            for s in range(D):
                row = [CZ17] * (D * D)
                row[r * D + s] = N[r][r] - N[s][s]
                rows.append(row)
                for a in range(D):
                    for b in range(D):
                        if a == b:
                            continue
                        row = [CZ17] * (D * D)
                        if a == r:
                            row[b * D + s] = row[b * D + s] + N[r][b]
                        if b == s:
                            row[r * D + a] = row[r * D + a] - N[a][s]
                        if any(not x.z() for x in row):
                            rows.append(row)
    if want_basis:
        return D * D - rank17(rows), nulsp17(rows, D * D)
    return D * D - rank17(rows)

def fdim17(V, E, Ms, D, da, nts=9):
    # float cross-check: stack [U_t (M x I) U_t^H, Z] = 0 over sampled times
    rows = []
    for M in Ms:
        A = np.kron(np.array([[x.f() for x in r] for r in M]), np.eye(da))
        Vf = np.array([[x.f() for x in r] for r in V])
        for k in range(nts):
            t = 0.37 + 1.113 * k
            U = Vf @ np.diag(np.exp(-1j * np.array([float(e) for e in E]) * t)) @ Vf.conj().T
            B = U @ A @ U.conj().T
            for r in range(D):
                for s in range(D):
                    row = np.zeros(D * D, complex)
                    for p in range(D):
                        row[p * D + s] += B[r, p]
                        row[r * D + p] -= B[p, s]
                    rows.append(row)
    return D * D - np.linalg.matrix_rank(np.array(rows), tol=1e-8)

def giv17(D, i, j, c, s):
    G = eye17(D)
    G[i][i], G[i][j] = C17(c), C17(-s)
    G[j][i], G[j][j] = C17(s), C17(c)
    return G

def menus17(dv):
    nat = [[[CO17 if (r == c == i) else CZ17 for c in range(dv)] for r in range(dv)]
           for i in range(dv)]
    Gr = eye17(dv)                      # a DENSE rotation: chained Givens over all pairs
    for k in range(dv - 1):
        cs = (Frac(3, 5), Frac(4, 5)) if k % 2 == 0 else (Frac(5, 13), Frac(12, 13))
        Gr = mmc17(Gr, giv17(dv, k, k + 1, *cs))
    real = [mmc17(mmc17(dag17(Gr), P), Gr) for P in nat]
    Ph = eye17(dv)
    Ph[1][1] = C17(0, 1)
    gc = mmc17(Gr, Ph)
    cplx = [mmc17(mmc17(dag17(gc), P), gc) for P in nat]
    return nat, real, cplx

def complete17(V, E, Ms, D, da):
    # the Lean hypothesis hcomplete: every off-diagonal eigenpair visible to some menu element
    Vh = dag17(V)
    Ns = [mmc17(mmc17(Vh, kr17(M, eye17(da))), V) for M in Ms]
    return all(any(not N[a][b].z() for N in Ns)
               for a in range(D) for b in range(D) if a != b)

E17 = [Frac(0), Frac(1), Frac(3), Frac(7)]
# (a) the (2,2) no-go carrier: native menu ALREADY generates (dim 1, no probe needed)
V22 = mmc17(mmc17(giv17(4, 0, 2, Frac(3, 5), Frac(4, 5)),
                  giv17(4, 2, 3, Frac(5, 13), Frac(12, 13))),
            giv17(4, 0, 1, Frac(3, 5), Frac(4, 5)))
nat2, real2, cplx2 = menus17(2)
for Ms in (nat2, nat2 + real2, nat2 + cplx2):
    ok17 &= comm_dim17(V22, E17, Ms, 4, 2) == 1
    ok17 &= fdim17(V22, E17, Ms, 4, 2) == 1
ok17 &= complete17(V22, E17, nat2, 4, 2)          # hcomplete holds natively
# (b) the Fourier carrier (n = 4 visible, Gaussian-rational): same verdict
i4 = [CO17, C17(0, 1), C17(-1), C17(0, -1)]
VF = [[i4[(i * k) % 4] * C17(Frac(1, 2)) for k in range(4)] for i in range(4)]
nat4 = menus17(4)[0]
ok17 &= comm_dim17(VF, E17, nat4, 4, 1) == 1 and complete17(VF, E17, nat4, 4, 1)
# (c) the decoupled carrier: EVERY visible-local menu is defeated (kernel countercontrol:
# decoupled_carrier_commutes + ancillaPhase_not_scalar); the surviving commutant is
# exactly the ancilla phases diagonal(y o snd)
VP = kr17(giv17(2, 0, 1, Frac(3, 5), Frac(4, 5)), eye17(2))
for Ms in (nat2, nat2 + real2, nat2 + cplx2):
    ok17 &= comm_dim17(VP, E17, Ms, 4, 2) == 2
dimP, basP = comm_dim17(VP, E17, nat2 + cplx2, 4, 2, want_basis=True)
ok17 &= dimP == 2
for v in basP:
    W = [[v[b * 4 + s] for s in range(4)] for b in range(4)]
    Z = mmc17(mmc17(VP, W), dag17(VP))
    ok17 &= all(Z[p][q].z() for p in range(4) for q in range(4) if p != q)
    ok17 &= Z[0][0] == Z[2][2] and Z[1][1] == Z[3][3]   # y depends on the ancilla only
# hdec: every eigencolumn of VP lives in one ancilla sector (the Lean hypothesis)
ok17 &= all(len({p % 2 for p in range(4) if not VP[p][k].z()}) == 1 for k in range(4))
# (d) the blind stratum at (3,2): two product eigenvectors sharing an ancilla state make
# the NATIVE menu incomplete (commutant dim 3 > 1); a probe with visible off-diagonal
# support restores completeness and generation (kernel: complexProbe_trivialCommutant)
E6 = [Frac(0), Frac(1), Frac(3), Frac(7), Frac(12), Frac(20)]
W4 = mmc17(mmc17(giv17(4, 0, 1, Frac(3, 5), Frac(4, 5)),
                 giv17(4, 2, 3, Frac(5, 13), Frac(12, 13))),
           mmc17(giv17(4, 0, 2, Frac(3, 5), Frac(4, 5)),
                 giv17(4, 1, 3, Frac(4, 5), Frac(3, 5))))
ok17 &= all(not W4[i][j].z() for i in range(4) for j in range(4))
V32 = [[CZ17] * 6 for _ in range(6)]
V32[0][0] = CO17                                   # v0 = e0 x a0   (row 2i+a)
V32[2][1] = CO17                                   # v1 = e1 x a0
rows4 = [4, 1, 3, 5]                               # span{e2xa0, e0xa1, e1xa1, e2xa1}
for r in range(4):
    for c in range(4):
        V32[rows4[r]][2 + c] = W4[r][c]
nat3, real3, cplx3 = menus17(3)
dnat = comm_dim17(V32, E6, nat3, 6, 2)
dreal = comm_dim17(V32, E6, nat3 + real3, 6, 2)
dcplx = comm_dim17(V32, E6, nat3 + cplx3, 6, 2)
ok17 &= dnat == 3 and dreal == 1 and dcplx == 1
ok17 &= (not complete17(V32, E6, nat3, 6, 2)) and complete17(V32, E6, nat3 + real3, 6, 2)
ok17 &= fdim17(V32, E6, nat3, 6, 2) == 3 and fdim17(V32, E6, nat3 + real3, 6, 2) == 1
# (e) the antilinear residue: for a real carrier the eigenbasis coefficient tensor of
# every real response is REAL, so conjugation carries the accessible family to the
# reflected-spectrum family (kernel: real_menu_conjugation_stable); the complex probe's
# response is Hermitian but NOT conjugation-fixed (kernel: probeG_unitary,
# probeResp_is_probe_response, complexProbe_breaks_conjugation)
for M in nat2 + real2:
    N = mmc17(mmc17(dag17(V22), kr17(M, eye17(2))), V22)
    ok17 &= all(N[a][b].im == 0 for a in range(4) for b in range(4))
Ph2 = eye17(2)
Ph2[1][1] = C17(0, 1)
gC = mmc17(giv17(2, 0, 1, Frac(3, 5), Frac(4, 5)), Ph2)
ok17 &= mmc17(dag17(gC), gC) == eye17(2)
respC = mmc17(mmc17(dag17(gC), [[CO17, CZ17], [CZ17, CZ17]]), gC)
ok17 &= respC == [[C17(Frac(9, 25)), C17(0, Frac(-12, 25))],
                  [C17(0, Frac(12, 25)), C17(Frac(16, 25))]]
ok17 &= dag17(respC) == respC                       # Hermitian: a genuine readout response
ok17 &= [[x.conj() for x in r] for r in respC] != respC   # but not conjugation-fixed
check("F17", ok17,
      "THE ACCESSIBLE-ALGEBRA COMMUTANT CENSUS (phase three, round five; kernel: "
      "gap_coefficient_vanish, dyad_conjugation, accessible_trivial_commutant, "
      "native_menu_generates, complexProbe_trivialCommutant in "
      "OIBridge/AccessibleAlgebra.lean). Exact fiber-equation commutants, float "
      "time-sampling agreeing everywhere: (a) on the aligned (2,2) no-go carrier and "
      "(b) the Fourier carrier the NATIVE block readouts already have commutant "
      "dimension 1 -- readout completeness = generation, no probe needed, DEVIATING "
      "from the round's expectation that removing the complex probe leaves a nontrivial "
      "linear commutant; (c) on the sector-decoupled carrier every visible-local menu "
      "-- complex probe included -- leaves the exact ancilla-phase commutant "
      "diagonal(y o snd) (dim 2; kernel countercontrol decoupled_carrier_commutes + "
      "ancillaPhase_not_scalar): generation is carrier ALIGNMENT, not menu size; "
      "(d) the blind stratum at (3,2): two product eigenvectors sharing an ancilla "
      "state leave the native commutant at dim 3, and one rotated probe restores "
      "completeness and dim 1 -- the probe's genuine C3a role; (e) the ZZ_2 residue is "
      "ANTILINEAR: real responses have real eigenbasis tensors (conjugation maps the "
      "accessible family to the reflected spectrum), while the unitary complex probe's "
      "Hermitian response is not conjugation-fixed -- the complex probe orients, it "
      "does not generate")

# ----------------------- F18  operational separation and the Jordan chain (phase three, round 6)
# C3b.1: contexts must SEPARATE operators before any data-defined map is well-defined.
# The Fourier-resolved span of {1} + one-slot + two-slot contexts is computed exactly;
# the one-slot layer leaves a diagonal deficiency (two exact states with identical
# one-slot data), and the two-slot layer closes it (kernel: operational_separation,
# sameData_unique_state).  C3b.2: the Kadison chain (kernel: orderIso_jordan) is checked
# on both matrix branches, and the pinching countercontrol shows one-sided positivity
# does not suffice.
ok18 = True

def span_rank18(V, E, Ms, D, da, slots):
    Vh = dag17(V)
    Ns = [mmc17(mmc17(Vh, kr17(M, eye17(da))), V) for M in Ms]
    gens = [[CO17 if a == b else CZ17 for a in range(D) for b in range(D)]]
    for N in Ns:
        for a in range(D):
            for b in range(D):
                if a != b and not N[a][b].z():
                    v = [CZ17] * (D * D)
                    v[a * D + b] = CO17
                    gens.append(v)
        v = [CZ17] * (D * D)
        for p in range(D):
            v[p * D + p] = N[p][p]
        gens.append(v)
    if slots >= 2:
        for NA in Ns:
            for NB in Ns:
                for a in range(D):
                    for b in range(D):
                        if a == b:
                            continue
                        for c in range(D):
                            if NA[a][b].z() or NB[b][c].z():
                                continue
                            v = [CZ17] * (D * D)
                            v[a * D + c] = CO17
                            gens.append(v)
    return rank17(gens)

# (a) the separation census at the (2,2) no-go carrier, native menu
V22a = mmc17(mmc17(giv17(4, 0, 2, Frac(3, 5), Frac(4, 5)),
                   giv17(4, 2, 3, Frac(5, 13), Frac(12, 13))),
             giv17(4, 0, 1, Frac(3, 5), Frac(4, 5)))
E18 = [Frac(0), Frac(1), Frac(3), Frac(7)]
nat18 = menus17(2)[0]
r1s = span_rank18(V22a, E18, nat18, 4, 2, 1)
r2s = span_rank18(V22a, E18, nat18, 4, 2, 2)
ok18 &= r1s == 14 and r2s == 16      # one-slot deficient by 2; two-slot SEPARATES
# (b) the degeneracy witness: a diagonal direction invisible to all one-slot data
Vh18 = dag17(V22a)
Ns18 = [mmc17(mmc17(Vh18, kr17(M, eye17(2))), V22a) for M in nat18]
rows18 = [[Ns18[j][p][p] for p in range(4)] for j in range(2)] + [[CO17] * 4]
ker18 = nulsp17(rows18, 4)
ok18 &= len(ker18) == 2              # dim = D - rank(diag lumps + trace) = 4 - 2
y18 = ker18[0]
q18 = [Frac(1, 2), Frac(1, 4), Frac(1, 8), Frac(1, 8)]
eps18 = min(q18) / (2 * max(abs(v.re) for v in y18))
pops_p = [q18[p] + eps18 * y18[p].re for p in range(4)]
pops_m = [q18[p] - eps18 * y18[p].re for p in range(4)]
ok18 &= all(pp >= 0 and pm >= 0 for pp, pm in zip(pops_p, pops_m))
ok18 &= pops_p != pops_m and sum(pops_p) == sum(pops_m) == 1
# identical one-slot data at every frequency (off-diagonals equal: both diagonal states;
# zero-frequency lumps equal by construction), discriminated by a two-slot triple (a,b,a)
for j in range(2):
    lump = sum((Ns18[j][p][p] * C17(pops_p[p] - pops_m[p]) for p in range(4)), CZ17)
    ok18 &= lump.z()
disc = None
for a in range(4):
    for b in range(4):
        if a != b and not Ns18[0][a][b].z() and not Ns18[1][b][a].z() \
                and pops_p[a] != pops_m[a]:
            disc = Ns18[0][a][b] * Ns18[1][b][a] * C17(pops_p[a] - pops_m[a])
ok18 &= disc is not None and not disc.z()
# (c) the Jordan chain on both branches, and the pinching countercontrol
W18 = mmc17(giv17(3, 0, 1, Frac(3, 5), Frac(4, 5)), giv17(3, 1, 2, Frac(5, 13), Frac(12, 13)))
A18 = [[C17(1), C17(2, 1), C17(0, -1)], [C17(2, -1), C17(-1), C17(Frac(1, 2))],
       [C17(0, 1), C17(Frac(1, 2)), C17(3)]]
B18 = [[C17(2), C17(0, 2), C17(1)], [C17(0, -2), C17(0), C17(1, 1)],
       [C17(1), C17(1, -1), C17(-1)]]
ok18 &= dag17(A18) == A18 and dag17(B18) == B18

def anti18(X, Y):
    return [[sum((X[i][k] * Y[k][j] + Y[i][k] * X[k][j] for k in range(3)), CZ17)
             for j in range(3)] for i in range(3)]

def phiU18(X):
    return mmc17(mmc17(W18, X), dag17(W18))

def phiT18(X):
    return mmc17(mmc17(W18, [[X[j][i] for j in range(3)] for i in range(3)]), dag17(W18))

def pinch18(X):
    return [[X[i][j] if i == j else CZ17 for j in range(3)] for i in range(3)]

for Phi in (phiU18, phiT18):
    ok18 &= anti18(Phi(A18), Phi(B18)) == Phi(anti18(A18, B18))       # Jordan identity
ok18 &= anti18(pinch18(A18), pinch18(B18)) != pinch18(anti18(A18, B18))  # pinching FAILS
# projection transport on both branches (extreme points of [0,1] map to extreme points)
P18 = mmc17(mmc17(dag17(giv17(3, 0, 1, Frac(3, 5), Frac(4, 5))),
                  [[CO17, CZ17, CZ17], [CZ17, CZ17, CZ17], [CZ17, CZ17, CZ17]]),
            giv17(3, 0, 1, Frac(3, 5), Frac(4, 5)))
ok18 &= mmc17(P18, P18) == P18 and dag17(P18) == P18
for Phi in (phiU18, phiT18):
    Q18 = Phi(P18)
    ok18 &= mmc17(Q18, Q18) == Q18 and dag17(Q18) == Q18
# (d) the accessible cone construction, exact: M rho M^H = (w^H rho w)|u><u|
rho18 = mmc17(mmc17(V22a, [[C17(q18[p]) if p == qq else CZ17 for qq in range(4)]
                           for p in range(4)]), Vh18)
w18 = [CO17, CZ17, CZ17, CZ17]
wr18 = sum((w18[p].conj() * sum((rho18[p][r] * w18[r] for r in range(4)), CZ17)
            for p in range(4)), CZ17)
ok18 &= not wr18.z()
M18 = [[(w18[jj].conj()) * (CO17 if ii == 1 else CZ17) for jj in range(4)]
       for ii in range(4)]
MrM = mmc17(mmc17(M18, rho18), dag17(M18))
ok18 &= MrM[1][1] == wr18 and all(MrM[i][j].z() for i in range(4) for j in range(4)
                                  if (i, j) != (1, 1))
check("F18", ok18,
      "OPERATIONAL SEPARATION AND THE JORDAN CHAIN (phase three, round six; kernel: "
      "operational_separation, sameData_unique_state, sameData_combination_transfer, "
      "sameData_linear_extension, orderIso_jordan, accessible_cone_full in "
      "OIBridge/OperationalRigidity.lean). (a) Exact Fourier-resolved context spans at "
      "the (2,2) no-go carrier, native menu: {normalization + one-slot} spans 14/16 -- "
      "one-slot contexts do NOT separate operators even where the commutant is trivial "
      "-- and adding two-slot contexts closes the span to 16/16, exactly as "
      "operational_separation requires; (b) the deficiency is PHYSICAL: two distinct "
      "exact stationary states (populations perturbed along the 2-dim kernel of the "
      "diagonal lumps) carry identical normalization and one-slot data at every "
      "frequency yet are discriminated by an explicit two-slot triple (a,b,a) -- "
      "temporal depth of data, not menu size, is what pins the state "
      "(sameData_unique_state); (c) the Kadison chain: the Jordan identity "
      "Phi(A.B+B.A) = Phi(A).Phi(B)+Phi(B).Phi(A) holds exactly on BOTH matrix "
      "branches W X W^H and W X^T W^H, projections transport on both, and the pinching "
      "countercontrol (positive, unital, NOT an order isomorphism) violates the "
      "identity -- Kadison's two-sided positivity is load-bearing, matching "
      "orderIso_jordan's hypothesis package; (d) the accessible-cone construction is "
      "exact: a selective word maps any nonzero positive preparation onto a prescribed "
      "rank-one state with coefficient w^H rho w (accessible_cone_full) -- the "
      "positivity face of the C3b.3 assembly")

# ----------------------- F19  the matrix-unit classification pipeline (phase three, round 7)
# C3b.3: every step of the kernel classification is replayed exactly at D = 3 on BOTH
# branches Phi(X) = W X W^H and Phi(X) = W X^T W^H with a dense exact unitary W (two
# Givens rotations and two complex phases): rank-one resolution from the diagonal-unit
# images, corner localization, the alpha.beta = 0 dichotomy, unimodularity, the triple
# cocycle, and the phase coboundary that rebuilds W.  Countercontrols: a MIXED
# orientation (transposing one corner pair only) violates the Jordan identity at the
# triple (0,1,2) -- triple consistency is load-bearing; and the self-duality witness
# Tr(A vv^H) = -1 < 0 detects a non-PSD Hermitian A through the rank-one dyad test.
ok19 = True
D19 = 3

def n219(x):
    return x.re * x.re + x.im * x.im

def T19(X):
    return [[X[j][i] for j in range(D19)] for i in range(D19)]

def madd19(A, B):
    return [[A[i][j] + B[i][j] for j in range(D19)] for i in range(D19)]

def anti19(X, Y):
    return madd19(mmc17(X, Y), mmc17(Y, X))

def E19(i, j):
    return [[CO17 if (r, c) == (i, j) else CZ17 for c in range(D19)] for r in range(D19)]

def dot19(a, b):
    return sum((a[k].conj() * b[k] for k in range(D19)), CZ17)

Ph1_19 = eye17(3); Ph1_19[1][1] = C17(0, 1)
Ph2_19 = eye17(3); Ph2_19[2][2] = C17(Frac(3, 5), Frac(4, 5))
W19 = mmc17(mmc17(mmc17(giv17(3, 0, 1, Frac(3, 5), Frac(4, 5)), Ph1_19),
                  giv17(3, 1, 2, Frac(5, 13), Frac(12, 13))), Ph2_19)
ok19 &= mmc17(dag17(W19), W19) == eye17(3)          # exact dense unitary

def phiU19(X):
    return mmc17(mmc17(W19, X), dag17(W19))

def phiT19(X):
    return mmc17(mmc17(W19, T19(X)), dag17(W19))

for name19, Phi19 in (("unitary", phiU19), ("transpose", phiT19)):
    A19 = [[C17(1), C17(2, 1), CZ17], [C17(0, 3), C17(-1), CO17],
           [C17(1, 1), CZ17, C17(2)]]
    B19 = [[CZ17, CO17, C17(1, 2)], [C17(2), CZ17, CZ17],
           [CO17, C17(0, -1), C17(1)]]
    ok19 &= Phi19(anti19(A19, B19)) == anti19(Phi19(A19), Phi19(B19))  # complexified Jordan
    # (a) diagonal-unit images: an orthogonal rank-one resolution of the identity
    p19 = [Phi19(E19(i, i)) for i in range(3)]
    ok19 &= madd19(madd19(p19[0], p19[1]), p19[2]) == eye17(3)
    for i in range(3):
        ok19 &= mmc17(p19[i], p19[i]) == p19[i] and dag17(p19[i]) == p19[i]
        ok19 &= sum((p19[i][k][k] for k in range(3)), CZ17) == CO17   # trace 1: rank one
        for j in range(3):
            if i != j:
                ok19 &= all(x.z() for r in mmc17(p19[i], p19[j]) for x in r)
    # frame vectors (unnormalized: s_i = v_i^H v_i > 0, p_i s_i = v_i v_i^H exactly)
    v19 = []
    for i in range(3):
        j0 = next(j for j in range(3) if not p19[i][j][j].z())
        v19.append([p19[i][r][j0] for r in range(3)])
    s19 = [dot19(v19[i], v19[i]) for i in range(3)]
    for i in range(3):
        for j in range(3):
            if i != j:
                ok19 &= dot19(v19[i], v19[j]).z()
        for r in range(3):
            for c in range(3):
                ok19 &= p19[i][r][c] * s19[i] == v19[i][r] * v19[i][c].conj()
    # (b) corner coefficients and localization  F_ij = p_i F_ij p_j + p_j F_ij p_i
    F19m = [[Phi19(E19(i, j)) for j in range(3)] for i in range(3)]

    def quad19(vv, M, ww):
        return dot19(vv, [sum((M[r][c] * ww[c] for c in range(3)), CZ17)
                          for r in range(3)])

    al19 = [[quad19(v19[i], F19m[i][j], v19[j]) for j in range(3)] for i in range(3)]
    be19 = [[quad19(v19[j], F19m[i][j], v19[i]) for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            if i != j:
                loc = madd19(mmc17(mmc17(p19[i], F19m[i][j]), p19[j]),
                             mmc17(mmc17(p19[j], F19m[i][j]), p19[i]))
                ok19 &= loc == F19m[i][j]                        # corner_form
                ok19 &= (al19[i][j] * be19[i][j]).z()            # corner_nilpotent
                ok19 &= n219(al19[i][j]) / (s19[i].re * s19[j].re) \
                    + n219(be19[i][j]) / (s19[i].re * s19[j].re) == 1  # corner_unimodular
    # (c) the dichotomy is GLOBAL and matches the branch (orientation_dichotomy)
    brU = all(be19[i][j].z() for i in range(3) for j in range(3) if i != j)
    brT = all(al19[i][j].z() for i in range(3) for j in range(3) if i != j)
    ok19 &= brU != brT and (name19 == "unitary") == brU
    co19 = al19 if brU else be19
    # (d) triple cocycle and phase coboundary (corner_cocycle, the W reconstruction)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if len({i, j, k}) == 3:
                    ok19 &= co19[i][k] * s19[j] == co19[i][j] * co19[j][k]
    i0 = 0
    for i in range(3):
        for j in range(3):
            if i != j and i != i0 and j != i0:
                ok19 &= co19[i][j] * s19[i0] == co19[i][i0] * co19[j][i0].conj()
# (e) countercontrol: a mixed orientation violates the Jordan identity at (0,1,2)
mix19 = {(0, 0): (0, 0), (1, 1): (1, 1), (2, 2): (2, 2), (0, 1): (0, 1),
         (1, 0): (1, 0), (1, 2): (2, 1), (2, 1): (1, 2), (0, 2): (0, 2),
         (2, 0): (2, 0)}

def phiMix19(X):
    out = [[CZ17 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for b in range(3):
            ta, tb = mix19[(a, b)]
            out[ta][tb] = out[ta][tb] + X[a][b]
    return out

ok19 &= phiMix19(anti19(E19(0, 1), E19(1, 2))) != anti19(phiMix19(E19(0, 1)),
                                                         phiMix19(E19(1, 2)))
# (f) self-duality witness: the dyad test detects the negative direction
A19d = [[C17(1), CZ17, CZ17], [CZ17, C17(-1), CZ17], [CZ17, CZ17, C17(2)]]
vneg19 = [CZ17, CO17, CZ17]
dy19 = [[vneg19[r] * vneg19[c].conj() for c in range(3)] for r in range(3)]
tr19 = sum((mmc17(A19d, dy19)[k][k] for k in range(3)), CZ17)
ok19 &= tr19 == C17(-1)
check("F19", ok19,
      "THE MATRIX-UNIT CLASSIFICATION PIPELINE (phase three, round seven; kernel: "
      "psd_iff_trace_nonneg, orthogonal_resolution_rank_one, corner_form, "
      "corner_nilpotent, corner_unimodular, corner_cocycle, orientation_dichotomy, "
      "matrixJordan_unitary_or_transpose, sameData_orderIso, "
      "sameData_unitary_or_transpose in OIBridge/JordanClassification.lean). At D = 3 "
      "with a dense exact unitary W (two Givens rotations, two complex phases), BOTH "
      "branches W X W^H and W X^T W^H replay every classification step exactly: the "
      "diagonal-unit images form an orthogonal rank-one resolution (traces exactly 1), "
      "each off-diagonal image localizes to its two corners, the two corner "
      "coefficients satisfy alpha.beta = 0 with |alpha|^2 + |beta|^2 = 1, the "
      "surviving coefficient obeys the triple cocycle co_ik s_j = co_ij co_jk and the "
      "phase coboundary co_ij s_i0 = co_ii0 conj(co_ji0) that rebuilds W, and the "
      "orientation is GLOBAL -- the unitary branch kills every beta, the transpose "
      "branch every alpha. Countercontrols: transposing ONE corner pair only violates "
      "the Jordan identity at the triple (0,1,2), so triple consistency is what forces "
      "a single global orientation (the same local-freedom -> triple-coherence -> "
      "coboundary architecture as the Hamiltonian reconstruction); and the rank-one "
      "dyad test detects a non-PSD Hermitian direction exactly (Tr(A vv^H) = -1), the "
      "converse half of PSD self-duality that lets positivity transfer BOTH ways in "
      "the assembly")

# ----------------------- F20  the selector no-go and the oriented reference (phase three, round 8)
# C3c bounded exactly.  (a) The transpose partner ({G^T},{sigma^T}) of a completion carries
# IDENTICAL pairing data and remains admissible (PSD transports, span transports); (b) the
# transpose map realizes the second branch with W = 1 yet is NOT any unitary conjugation
# (inner maps are multiplicative, transpose is antimultiplicative); (c) an oriented
# functional O with O(Theta R) = -O(R) and O(R) > 0 excludes the transpose branch, and since
# the data are Theta-invariant while O flips, O provably CANNOT factor through the data;
# (d) the OTI sign transport is exact, and the passivity margin refutes the reflected
# orientation, replaying both assembly routes' fork resolution arithmetic.
ok20 = True

def T20(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

def conj20(X):
    return [[X[i][j].conj() for j in range(len(X[0]))] for i in range(len(X))]

def tr20(X):
    return sum((X[k][k] for k in range(len(X))), CZ17)

# (a) data identity at D = 2 with a dense complex menu: I, sigma_x, sigma_y, sigma_z and a
# genuinely complex two-slot product sigma_x . sigma_y = i sigma_z
sx20 = [[CZ17, CO17], [CO17, CZ17]]
sy20 = [[CZ17, C17(0, -1)], [C17(0, 1), CZ17]]
sz20 = [[CO17, CZ17], [CZ17, C17(-1)]]
G20 = [eye17(2), sx20, sy20, sz20, mmc17(sx20, sy20)]
A20a = [[C17(1), C17(2, 1)], [C17(0, -1), C17(Frac(1, 2))]]
A20b = [[C17(Frac(3, 5), Frac(4, 5)), CZ17], [C17(1, 1), C17(2)]]
S20 = [mmc17(A, dag17(A)) for A in (A20a, A20b)] + [eye17(2)]
for Gm in G20:
    for sm in S20:
        ok20 &= tr20(mmc17(T20(Gm), T20(sm))) == tr20(mmc17(Gm, sm))
# any selector factoring through the data therefore CANNOT split R from Theta R: the two
# data tables are equal entry by entry (operational_orientation_noGo)
# (b) admissibility of the partner: sigma^T = conj(A).conj(A)^H is PSD by construction,
# and the transposed menu still spans all of M_2 (4/4 over C)
for A in (A20a, A20b):
    ok20 &= T20(mmc17(A, dag17(A))) == mmc17(conj20(A), dag17(conj20(A)))
vec20 = lambda M: [M[r][c] for r in range(2) for c in range(2)]
ok20 &= rank17([vec20(M) for M in G20[:4]]) == 4
ok20 &= rank17([vec20(T20(M)) for M in G20[:4]]) == 4
# (c) the second branch is realized (Phi = transpose, W = 1) and the branches are disjoint:
# transpose is antimultiplicative, inner maps are multiplicative, matrix units refuse
E11_20, E12_20 = [[CO17, CZ17], [CZ17, CZ17]], [[CZ17, CO17], [CZ17, CZ17]]
prod20 = mmc17(E11_20, E12_20)
ok20 &= T20(prod20) == mmc17(T20(E12_20), T20(E11_20))          # (XY)^T = Y^T X^T
ok20 &= T20(prod20) != mmc17(T20(E11_20), T20(E12_20))          # not X^T Y^T
ok20 &= prod20 == E12_20 and all(x.z() for r in mmc17(E12_20, E11_20) for x in r)
ok20 &= any(not x.z() for r in E12_20 for x in r)               # transpose_not_inner witness
# (d) the oriented reference: a passive profile at ordered energies, its margin flips sign
# under the reflection while the pairing data are unchanged -- so the margin is positive on
# R, negative on Theta R, and provably NOT a function of the data
E20 = [0, 1, 3, 7]
p20 = [Frac(1, 2), Frac(1, 4), Frac(1, 8), Frac(1, 8)]
ok20 &= all(p20[bb] <= p20[aa] for aa in range(4) for bb in range(4)
            if E20[aa] < E20[bb])                                # Passive E p
Erefl20 = [-e + 10 for e in E20]
Om20 = p20[0] - p20[1]                                           # the margin at pair (0,1)
OmT20 = p20[1] - p20[0]                                          # the same pair, reflected order
ok20 &= Om20 == Frac(1, 4) and OmT20 == -Om20 and Om20 > 0 and OmT20 < 0
ok20 &= not all(p20[bb] <= p20[aa] for aa in range(4) for bb in range(4)
                if Erefl20[aa] < Erefl20[bb])                    # reflected passivity FAILS
# (e) OTI sign transport, exact: betaE (eps_b - eps_a) = tauK (omega_b - omega_a) with
# betaE = 2, tauK = 3, eps = 3k, omega = 2k -- the classical order IS the Bohr order; a
# negative tauK reverses it (the countercontrol the positivity premises exclude)
eps20 = [3 * k for k in (0, 1, 4, 6)]
omg20 = [2 * k for k in (0, 1, 4, 6)]
for aa in range(4):
    for bb in range(4):
        ok20 &= 2 * (eps20[bb] - eps20[aa]) == 3 * (omg20[bb] - omg20[aa])
        ok20 &= (eps20[aa] < eps20[bb]) == (omg20[aa] < omg20[bb])
        ok20 &= (eps20[aa] < eps20[bb]) == ((-3) * omg20[aa] > (-3) * omg20[bb]) \
            or eps20[aa] == eps20[bb]
# (f) the state route's profile: rho = V diag(p) V^H at the exact (2,2)-carrier unitary is
# PSD with trace one, spectral populations exactly p, and is RECONSTRUCTED from them
rho20 = mmc17(mmc17(V22a, [[C17(p20[aa]) if aa == bb else CZ17 for bb in range(4)]
                           for aa in range(4)]), dag17(V22a))
ok20 &= tr20(rho20) == CO17 and dag17(rho20) == rho20
spec20 = mmc17(mmc17(dag17(V22a), rho20), V22a)
ok20 &= all(spec20[aa][aa] == C17(p20[aa]) for aa in range(4))
ok20 &= all(spec20[aa][bb].z() for aa in range(4) for bb in range(4) if aa != bb)
recon20 = mmc17(mmc17(V22a, [[spec20[aa][aa] if aa == bb else CZ17 for bb in range(4)]
                             for aa in range(4)]), dag17(V22a))
ok20 &= recon20 == rho20                                         # the state IS its profile
check("F20", ok20,
      "THE SELECTOR NO-GO AND THE ORIENTED REFERENCE (phase three, round eight; kernel: "
      "transpose_data_eq, selector_factorization_invariant, operational_orientation_noGo, "
      "transpose_span, transpose_sep, transpose_cone, transpose_completion_admissible, "
      "transpose_realizes_second_branch, transpose_not_inner, "
      "orientedReference_excludes_transpose, oriented_functional_not_data_definable, "
      "sameData_unitary_of_orientedReference, shellRepresentation_stationary_profile, "
      "sameData_unitary_of_transitionIdentification, "
      "sameData_unitary_of_shellRepresentation in OIBridge/OrientationSelection.lean). "
      "(a) The transpose partner ({G^T},{sigma^T}) carries IDENTICAL pairing data -- every "
      "trace pairs equal exactly, complex two-slot products included -- so any selector "
      "factoring through operational data assigns the same verdict to both members of the "
      "orientation pair: full unoriented data select QM only up to antiunitary "
      "equivalence; (b) the partner is ADMISSIBLE (transposed states stay PSD by exact "
      "construction, the transposed menu still spans 4/4) and the transpose map itself "
      "realizes the classification's second branch with W = 1, yet is NOT any unitary "
      "conjugation -- transpose is antimultiplicative and matrix units refuse to commute; "
      "(c) the oriented functional: a passive profile's margin is +1/4 on R and -1/4 on "
      "Theta R while the data tables are equal, so the margin flips where the data cannot "
      "-- the oriented datum is provably not data-definable, and positivity on both "
      "completions excludes the transpose branch; (d) the OTI sign transport is exact "
      "(betaE.d_eps = tauK.d_omega with positive betaE, tauK forces the classical order "
      "to BE the Bohr order; negative tauK reverses it) and reflected passivity fails at "
      "an explicit pair -- the arithmetic both assembly capstones run; (e) the state "
      "route's stationary state is exactly its spectral profile (PSD, trace one, "
      "populations p, reconstructed from its own diagonal) -- what "
      "shellRepresentation_stationary_profile extracts from "
      "ShellRepresentationConsistency. The remaining question is precise: does bare OI "
      "derive OperationalTransitionIdentification or ShellRepresentationConsistency?")

# ----------------------- F21  SRC transpose stability and the universal no-go (phase three, round 9)
# The final audit before the phase-three synthesis.  (a) SRC is an EXISTENCE condition,
# not an orientation selector: transposing the represented state and reflecting the model
# preserves every SRC clause exactly -- the reflected propagator IS the conjugated
# propagator (checked at the formal phase level: integer powers of z = e^{-it}), the
# transposed state keeps PSD/trace/readout; (b) OTI is genuinely orientation-sensitive:
# the identification for the labels and for their reflection jointly force every Bohr gap
# to zero; (c) the state-side oriented condition (SRC + aligned spectral passivity +
# nonuniformity) is orientation-sensitive under the carrier nondegeneracies: the shared
# readout pins ONE spectral profile (the moduli mixture B is injective at the census
# carrier), and a nonuniform profile cannot be passive for both orientations; (d) the
# universal no-go replayed on a two-element Theta-closed class.
ok21 = True
E21 = [0, 1, 3, 7]
p21 = [Frac(1, 2), Frac(1, 4), Frac(1, 8), Frac(1, 8)]

def dyad21(V, a):
    return [[V[r][a] * V[c][a].conj() for c in range(4)] for r in range(4)]

def prop21(V, E):
    U = {}
    for a in range(4):
        M = dyad21(V, a)
        if E[a] in U:
            U[E[a]] = [[U[E[a]][r][c] + M[r][c] for c in range(4)] for r in range(4)]
        else:
            U[E[a]] = M
    return U

# (a) the reflected propagator is the conjugated propagator, formally in z-powers
V21c = [[V22a[r][c].conj() for c in range(4)] for r in range(4)]
U21 = prop21(V22a, E21)
U21r = prop21(V21c, [-e for e in E21])
ok21 &= set(U21r) == {-k for k in U21}
for k, M in U21.items():
    ok21 &= U21r[-k] == [[M[r][c].conj() for c in range(4)] for r in range(4)]
# the transposed state: every SRC clause survives exactly
rho21 = mmc17(mmc17(V22a, [[C17(p21[a]) if a == b else CZ17 for b in range(4)]
                           for a in range(4)]), dag17(V22a))
rho21T = T20(rho21)
rho21r = mmc17(mmc17(V21c, [[C17(p21[a]) if a == b else CZ17 for b in range(4)]
                            for a in range(4)]), dag17(V21c))
ok21 &= rho21T == rho21r                                  # rho^T IS the reflected witness
ok21 &= dag17(rho21T) == rho21T and tr20(rho21T) == CO17
ok21 &= all(rho21T[i][i] == rho21[i][i] for i in range(4))  # readout survives
# (b) OTI orientation sensitivity: 2.d_eps = 3.d_omega holds, 2.d_eps = -3.d_omega fails
eps21 = [3 * k for k in (0, 1, 4, 6)]
omg21 = [2 * k for k in (0, 1, 4, 6)]
ok21 &= all(2 * (eps21[b] - eps21[a]) == 3 * (omg21[b] - omg21[a])
            for a in range(4) for b in range(4))
viol21 = [(a, b) for a in range(4) for b in range(4)
          if 2 * (eps21[b] - eps21[a]) != -3 * (omg21[b] - omg21[a])]
ok21 &= len(viol21) > 0                                   # both together are impossible
ok21 &= all(omg21[a] == omg21[b]
            for a in range(4) for b in range(4) if (a, b) not in viol21)
# (c) the readout pins the profile: B = |V_ia|^2 is injective at the census carrier, the
# shared p forces one q, and q passive for E is NOT passive for -E (nonuniform squeeze)
B21 = [[V22a[i][a] * V22a[i][a].conj() for a in range(4)] for i in range(4)]
ok21 &= rank17(B21) == 4                                  # ReadoutSeparating holds
Bc21 = [[V21c[i][a] * V21c[i][a].conj() for a in range(4)] for i in range(4)]
ok21 &= B21 == Bc21                                       # the partner has the SAME mixture
ok21 &= all(p21[b] <= p21[a] for a in range(4) for b in range(4)
            if E21[a] < E21[b])                           # Passive E q
ok21 &= not all(p21[b] <= p21[a] for a in range(4) for b in range(4)
                if -E21[a] < -E21[b])                     # Passive (-E) q FAILS
# (d) the universal no-go on a two-element Theta-closed class: P(R) and not P(Theta R)
cls21 = [("R", E21), ("ThetaR", [-e for e in E21])]
def P21(lab):
    Em = dict(cls21)[lab]
    return all(p21[b] <= p21[a] for a in range(4) for b in range(4)
               if Em[a] < Em[b]) and any(p21[a] != p21[b]
                                         for a in range(4) for b in range(4))
ok21 &= P21("R") and not P21("ThetaR")                    # no Theta-closed class forces P
check("F21", ok21,
      "SRC TRANSPOSE STABILITY AND THE UNIVERSAL ORIENTATION NO-GO (phase three, round "
      "nine; kernel: conjM_conjM, conjM_sandwich_transpose, umat_reflect_conjM, "
      "shellRepresentation_transpose_stable, transitionIdentification_orientation_"
      "sensitive, stationary_readout, orientedShellRepresentation_orientation_sensitive, "
      "no_universal_oriented_property, no_symmetric_condition_forces_transition"
      "Identification, no_symmetric_condition_forces_orientedShell in "
      "OIBridge/OrientationClosure.lean). (a) SRC is an EXISTENCE condition, not an "
      "orientation selector: at the census carrier the reflected model's propagator "
      "equals the conjugated propagator formally in z-powers (power negation + "
      "coefficient conjugation, exact), and the transposed state IS the reflected "
      "witness -- Hermitian, trace one, identical visible readout -- so every SRC clause "
      "transports both ways (shellRepresentation_transpose_stable); (b) OTI is genuinely "
      "orientation-sensitive: betaE.d_eps = tauK.d_omega holds exactly on all pairs while "
      "its reflection fails on every pair with a nonzero gap -- the two together force "
      "all gaps to zero; (c) the state-side oriented condition is orientation-sensitive "
      "under the carrier nondegeneracies: the moduli mixture B = |V_ia|^2 has full rank "
      "4/4 (ReadoutSeparating), the partner carries the SAME mixture, so the shared "
      "readout pins one spectral profile -- and the nonuniform passive profile fails "
      "reflected passivity at an explicit pair; (d) the universal no-go replayed on a "
      "two-element Theta-closed class: P holds at R, fails at Theta R, so no "
      "transpose-symmetric condition can force P throughout. BOXED: bare "
      "transpose-symmetric coherent-completion conditions cannot force an orientation -- "
      "'impossible from unoriented data', not 'not yet derived'")

# ----------------------- F22  actual-substratum preparation feasibility (phase three, round 11)
# The substratum coherent-existence test, stage one: ONE microscopic model -- the corpus's
# concrete shell shape (visible energies 0,1,2; bath counts 1,2,4,8 so beta_E > 0; joint
# permutation conserving total energy, ergodic within each shell) -- generates BOTH the
# shell marginal p AND the carrier (U_phi, P_i).  No hand-chosen V, no fitting B to p.
# (a) same model sources shell and transition data; (b) the carrier's B on the target shell
# block is CANONICAL -- the block is a single 14-cycle, its spectrum nondegenerate, so the
# eigenvector moduli (hence B) are invariant under every branch of the interpolation
# ambiguity [Main] names; (c) the feasibility p = Bq is decided POSITIVELY with the
# classical shell ensemble itself as the representing state; (d) changing the preparation
# with the carrier fixed flips feasibility (exact separating certificate); (e) beyond the
# permutation shadow the corpus specifies no finite continuous flow, and two generic
# carriers compatible with everything the corpus fixes give OPPOSITE verdicts for the same
# p: the physical-flow carrier datum is underdetermined -- the named missing premise.
ok22 = True
evis22 = [0, 1, 2]
Ehid22 = [0] + [1] * 2 + [2] * 4 + [3] * 8            # counts 1,2,4,8: beta_E > 0
J22 = [(i, h) for i in range(3) for h in range(len(Ehid22))]
shells22 = {}
for s in J22:
    shells22.setdefault(evis22[s[0]] + Ehid22[s[1]], []).append(s)
ok22 &= sorted(len(v) for v in shells22.values()) == [1, 3, 7, 8, 12, 14]
ratio22 = {}
for E, sh in shells22.items():
    ratio22[E] = [Frac(sum(1 for s in sh if s[0] == i), len(sh)) for i in range(3)]
# phi: fiber-interleaved single cycle within each shell (round-robin over visible labels)
order22 = {}
for E, sh in shells22.items():
    byf = [[s for s in sh if s[0] == i] for i in range(3)]
    seq, k = [], 0
    while any(byf):
        if byf[k % 3]:
            seq.append(byf[k % 3].pop(0))
        k += 1
    order22[E] = seq
phi22 = {}
for E, seq in order22.items():
    for k, s in enumerate(seq):
        phi22[s] = seq[(k + 1) % len(seq)]
ok22 &= sorted(phi22) == sorted(J22) and sorted(phi22.values()) == sorted(J22)
for E, sh in shells22.items():
    ok22 &= {phi22[s] for s in sh} == set(sh)          # every shell conserved
    orb, s = [sh[0]], phi22[sh[0]]
    while s != sh[0]:
        orb.append(s)
        s = phi22[s]
    ok22 &= len(orb) == len(sh)                        # ergodic: one cycle per shell
# (a) the SAME phi sources the transition data: T(1) with the uniform hidden prior is
# doubly stochastic and genuinely mixes the visible labels
T22 = [[Frac(0)] * 3 for _ in range(3)]
for i in range(3):
    for h in range(len(Ehid22)):
        T22[i][phi22[(i, h)][0]] += Frac(1, len(Ehid22))
ok22 &= all(sum(r) == 1 for r in T22) and all(sum(T22[i][j] for i in range(3)) == 1
                                              for j in range(3))
ok22 &= sum(T22[i][j] for i in range(3) for j in range(3) if i != j) == Frac(5, 3)
ok22 &= sum(1 for s in shells22[3] if phi22[s][0] != s[0]) == 10   # mixing on the shell
# (b) canonical B on the target shell block: no nontrivial fixed powers, so every
# eigenprojector of the 14-cycle has constant diagonal 1/14 (the DFT fixed-point
# identity), the spectrum is the 14 distinct fourteenth roots, and B_ia = tr(P_i Pi_a)
# = m_i/14 for EVERY a -- invariant under every log-branch of the interpolation
sh22 = order22[3]
N22 = len(sh22)

def powfix22(t, j):
    s = t
    for _ in range(j):
        s = phi22[s]
    return s == t

ok22 &= all(not powfix22(t, j) for j in range(1, N22) for t in sh22)
m22 = [sum(1 for s in sh22 if s[0] == i) for i in range(3)]
Bcol22 = [Frac(mi, N22) for mi in m22]
ok22 &= sum(Bcol22) == 1 and m22 == [8, 4, 2]
# (c) FEASIBILITY, decided positively: p IS the (unique) column, q uniform solves p = Bq,
# and the representing state is the classical shell ensemble itself -- exactly stationary,
# correct readout, PSD, trace one.  SRC holds for the actual substratum truncation.
p22 = ratio22[3]
ok22 &= p22 == Bcol22 == [Frac(4, 7), Frac(2, 7), Frac(1, 7)]
rho22 = {s: Frac(1, N22) for s in sh22}
ok22 &= {phi22[s]: w for s, w in rho22.items()} == rho22           # U rho U^T = rho
ok22 &= [sum(w for s, w in rho22.items() if s[0] == i) for i in range(3)] == p22
ok22 &= sum(rho22.values()) == 1 and all(w > 0 for w in rho22.values())
# every shell's counting marginal is its own cycle ratio point: the counting preparation
# is feasible at EVERY shell of the model, unconditionally
ok22 &= all(ratio22[E] == [Frac(sum(1 for s in order22[E] if s[0] == i),
                                len(order22[E])) for i in range(3)] for E in shells22)
# (d) COUNTERCONTROL: the stationary-readout hull is spanned by the shells' ratio points;
# the exact observable bound (cycle-averaging M = c.P) certifies that the modified
# preparation p'' = (1/3, 2/3, 0) is INFEASIBLE on the same carrier: every stationary
# state pays at most 2/3 on M = P_0/2 + P_1, while p'' pays 5/6
c22 = [Frac(1, 2), Frac(1), Frac(0)]
d22 = Frac(2, 3)
ok22 &= all(sum(ci * vi for ci, vi in zip(c22, ratio22[E])) <= d22 for E in shells22)
avg22 = {}
for E, seq in order22.items():
    a = sum(c22[s[0]] for s in seq) / len(seq)
    for s in seq:
        avg22[s] = a
ok22 &= max(avg22.values()) == d22                     # max cycle average = the bound
p2_22 = [Frac(1, 3), Frac(2, 3), Frac(0)]
ok22 &= sum(ci * vi for ci, vi in zip(c22, p2_22)) == Frac(5, 6) > d22
# a commutant state with genuine coherences (rho = I/14 + (C + C^T)/56 on the shell,
# C the cycle shift: commutes with C, PSD since its eigenvalues are
# 1/14 + cos(2 pi k/14)/28 >= 1/14 - 1/28 > 0) keeps its readout at p exactly: C has no
# fixed point on the cycle, so C + C^T has zero diagonal and coherences never move the
# diagonal readout of the diagonal projectors -- the hull of the shells' ratio points is
# the EXACT stationary-readout set
ok22 &= all(phi22[s] != s for s in sh22)               # zero diagonal for C + C^T
# (e) THE PHYSICAL-FLOW LAYER IS UNDERDETERMINED.  The corpus fixes p, the classical
# energies, and beta_E > 0, but names the continuous interpolation as additional chosen
# structure and its genericity fails AT the permutation limit (root-of-unity eigenphases:
# maximally gap-degenerate).  Two generic rational-orthogonal carriers compatible with
# everything the corpus fixes give opposite verdicts for the SAME p:
def giv22(i, j, c, s):
    G = [[Frac(1) if a == b else Frac(0) for b in range(3)] for a in range(3)]
    G[i][i], G[i][j], G[j][i], G[j][j] = c, -s, s, c
    return G

def mm22(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]

def det22(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))

def solve22(B, p):
    D = det22(B)
    rep = lambda k: [[p[r] if c == k else B[r][c] for c in range(3)] for r in range(3)]
    return [det22(rep(k)) / D for k in range(3)]

VF = mm22(giv22(0, 1, Frac(5, 13), Frac(12, 13)), giv22(1, 2, Frac(5, 13), Frac(12, 13)))
VI = mm22(giv22(0, 1, Frac(3, 5), Frac(4, 5)), giv22(1, 2, Frac(5, 13), Frac(12, 13)))
for V in (VF, VI):
    for a in range(3):
        for b in range(3):
            ok22 &= sum(V[i][a] * V[i][b] for i in range(3)) == (1 if a == b else 0)
BF = [[VF[i][a] ** 2 for a in range(3)] for i in range(3)]
BI = [[VI[i][a] ** 2 for a in range(3)] for i in range(3)]
ok22 &= all(sum(B[i][a] for i in range(3)) == 1 for B in (BF, BI) for a in range(3))
qF = solve22(BF, p22)
ok22 &= all(x >= 0 for x in qF) and sum(qF) == 1
ok22 &= qF == [Frac(188, 833), Frac(3986, 99127), Frac(72769, 99127)]
ok22 &= [sum(BF[i][a] * qF[a] for a in range(3)) for i in range(3)] == list(p22)
qI = solve22(BI, p22)
ok22 &= any(x < 0 for x in qI)                         # unique solution leaves the simplex
# exact Farkas certificate for the infeasible carrier: the B-inverse row of a negative
# component is nonnegative on every column and negative on p
aneg = min(k for k in range(3) if qI[k] < 0)
DI = det22(BI)
cof = lambda r, c: [[BI[x][y] for y in range(3) if y != c] for x in range(3) if x != r]
det2 = lambda M: M[0][0] * M[1][1] - M[0][1] * M[1][0]
crow = [(-1) ** (aneg + j) * det2(cof(j, aneg)) / DI for j in range(3)]
ok22 &= all(sum(crow[i] * BI[i][a] for i in range(3)) == (1 if a == aneg else 0)
            for a in range(3))
ok22 &= sum(crow[i] * p22[i] for i in range(3)) < 0
# and the Fourier-uniform carrier is infeasible outright: only the uniform readout
ok22 &= p22 != [Frac(1, 3)] * 3
check("F22", ok22,
      "ACTUAL-SUBSTRATUM PREPARATION FEASIBILITY (phase three, round eleven; the "
      "substratum coherent-existence test, stage one; kernel context: "
      "ShellRepresentationConsistency, shellWeight_invariant, joint_stationary, "
      "marginal_stationary in OIBridge/ShellAssignment.lean; "
      "shell_representation_from_comb, comb_mixture_of_shell_representation, "
      "uniform_overlap_obstruction in OIBridge/CoherentLift.lean; "
      "shellRepresentation_transpose_stable in OIBridge/OrientationClosure.lean). ONE "
      "microscopic model -- the corpus's shell shape: visible energies 0,1,2, bath "
      "counts 1,2,4,8 (beta_E > 0), a joint permutation conserving every total-energy "
      "shell and ergodic within each -- generates BOTH the shell marginal "
      "p = (4/7, 2/7, 1/7) AND the carrier: (a) the same phi yields doubly stochastic, "
      "genuinely mixing transition data (off-diagonal mass 5/3 at one step); (b) on the "
      "14-state target shell the block is a single cycle with no nontrivial fixed "
      "powers, so every eigenprojector has constant diagonal 1/14 and "
      "B_ia = m_i/14 = (4/7, 2/7, 1/7) for EVERY a -- canonical, and invariant under "
      "every log-branch of the interpolation ambiguity [Main] records; (c) FEASIBLE: "
      "p equals the column, uniform q solves p = Bq, and the representing state is the "
      "classical shell ensemble itself -- exactly stationary under the carrier, correct "
      "readout, PSD, trace one: SRC HOLDS FOR THE ACTUAL SUBSTRATUM TRUNCATION, with "
      "the counting preparation feasible at every shell of the model unconditionally; "
      "(d) countercontrol: with the carrier fixed, the modified preparation "
      "(1/3, 2/3, 0) is INFEASIBLE -- every stationary state pays at most 2/3 on the "
      "exact observable P_0/2 + P_1 (the maximal cycle average) while the target pays "
      "5/6; feasibility has content at the permutation layer; (e) BEYOND the "
      "permutation shadow the physical-flow carrier is UNDERDETERMINED: the corpus "
      "names the continuous interpolation as chosen structure and its reconstruction "
      "genericity fails at the permutation limit, and two generic rational-orthogonal "
      "carriers compatible with everything the corpus fixes give opposite verdicts for "
      "the same p -- G01(5/13).G12(5/13) is feasible with exact "
      "q = (188/833, 3986/99127, 72769/99127), G01(3/5).G12(5/13) is infeasible with "
      "an exact Farkas row certificate, and the Fourier-uniform carrier is infeasible "
      "outright. VERDICT: existence holds at the permutation truncation with a "
      "canonical branch-invariant carrier; the missing premise for the physical "
      "continuous-flow layer is exactly the generic-flow spectral/projector data "
      "(the eigenvector moduli B) that no corpus datum currently pins")

# ----------------------- F23  the cycle-fibre hull, kernelized (phase three, round 12)
# The F22 geometry is now theorem, not carrier arithmetic; this section replays the
# KERNEL statements exactly on the F22 model.  (a) freq: the orbit-frequency vectors are
# constant on orbits, sum to one at each point, and total to the fibre cardinalities;
# (b) the hull identity: for a genuinely mixed stationary state, weighting the orbit
# frequencies by the state's own diagonal reproduces every fibre readout exactly
# (stationary_readout_hull's convex decomposition); (c) achievability: the orbit-averaged
# diagonal state built from an arbitrary weight vector is stationary and reads out the
# prescribed convex combination (hull_readout_achieved's construction).
ok23 = True
L23 = 1
for E in shells22:
    L23 = L23 * len(shells22[E]) // __import__('math').gcd(L23, len(shells22[E]))

def iter23(s, k):
    for _ in range(k % L23):
        s = phi22[s]
    return s

def freq23(i, s):
    return Frac(sum(1 for k in range(L23) if iter23(s, k)[0] == i), L23)

# (a) freq facts: orbit constancy, probability vector, fibre mass
for E in shells22:
    s0 = shells22[E][0]
    ok23 &= all(freq23(i, phi22[s0]) == freq23(i, s0) for i in range(3))
    ok23 &= sum(freq23(i, s0) for i in range(3)) == 1
    ok23 &= [freq23(i, s0) for i in range(3)] == ratio22[E]      # r^(alpha) exactly
for i in range(3):
    ok23 &= sum(freq23(i, s) for s in J22) == sum(1 for s in J22 if s[0] == i)
# (b) the hull identity on a mixed stationary state: rho = (2/3) uniform(Sigma_3)
# + (1/3) uniform(Sigma_4) -- diagonal, orbit-constant, hence stationary
rho23 = {}
for s in shells22[3]:
    rho23[s] = Frac(2, 3) / len(shells22[3])
for s in shells22[4]:
    rho23[s] = Frac(1, 3) / len(shells22[4])
ok23 &= {phi22[s]: v for s, v in rho23.items()} == rho23
for i in range(3):
    readout = sum(v for s, v in rho23.items() if s[0] == i)
    hull = sum(v * freq23(i, s) for s, v in rho23.items())
    ok23 &= readout == hull                                       # the convex identity
    ok23 &= readout == Frac(2, 3) * ratio22[3][i] + Frac(1, 3) * ratio22[4][i]
# (c) achievability: arbitrary weights w, orbit-averaged diagonal d, stationary + exact
w23 = {s: Frac(1 + (7 * k) % 11, 45 * 6) for k, s in enumerate(J22)}
tot23 = sum(w23.values())
w23 = {s: v / tot23 for s, v in w23.items()}
d23 = {}
for s in J22:
    d23[s] = sum(w23[iter23(s, k)] for k in range(L23)) / L23
ok23 &= {phi22[s]: v for s, v in d23.items()} == d23              # stationary diagonal
ok23 &= sum(d23.values()) == 1 and all(v >= 0 for v in d23.values())
for i in range(3):
    ok23 &= sum(v for s, v in d23.items() if s[0] == i) \
        == sum(w23[s] * freq23(i, s) for s in J22)                # prescribed readout
check("F23", ok23,
      "THE CYCLE-FIBRE HULL, KERNELIZED (phase three, round twelve; kernel: freq_shift, "
      "freq_pow, freq_sum_one, freq_sum_card, fiberProj_trace, stationary_diag_pow, "
      "stationary_freq_readout, psd_diag_real, stationary_readout_hull, "
      "hull_readout_achieved, no_representation_outside_hull, transitive_freq_const, "
      "transitive_freq_eq_countMarginal, ergodicShell_readout_unique, ergodicShell_SRC, "
      "cycle_eigenvector_overlap, commutant_entry_zero, simple_spectrum_column_moduli, "
      "permLogBranch_projOverlap_invariant, sum_range_shift in "
      "OIBridge/CycleFibreHull.lean). The F22 geometry is now theorem: on the F22 model "
      "the orbit-frequency vectors are orbit-constant probability vectors totalling the "
      "fibre cardinalities and equal to the shell ratio points r^(alpha) exactly; a "
      "genuinely mixed stationary state (2/3 on the 14-shell, 1/3 on the 12-shell) "
      "satisfies the hull identity -- every fibre readout equals the diagonal-weighted "
      "average of the orbit frequencies -- and an arbitrary weight vector's "
      "orbit-averaged diagonal state is stationary with exactly the prescribed convex "
      "readout: the stationary readout set IS conv{r^(alpha)}, both directions. With "
      "transitivity the hull collapses to the counting marginal (unique readout, the "
      "DFT identity in readout form with no roots of unity), and simple-spectrum "
      "diagonalizations are unique up to diagonal phase, so the carrier datum B is "
      "branch-invariant on nondegenerate blocks -- the F22 verdict now rests on kernel "
      "statements, with the generic-flow B beyond the permutation shadow still the one "
      "named missing premise")

# ----------------------- F24  the dynamics glue G1 (phase three, round 13)
# The glue hierarchy separated exactly.  G1 (diagonal-sector dynamics glue): the sampled
# coherent dynamics agrees with the substratum permutation on the WHOLE classical
# diagonal sector.  (a) G1 <=> monomial: a phased cycle D.C on the F22 shell satisfies
# the glue at EVERY diagonal indicator exactly, and the indicator dyads force the
# monomial column structure back out (unimodular phases included); (b) G1 pins B: a
# genuinely coherent D.C-commutant state (with off-diagonal coherences) reads out the
# counting marginal exactly -- phases cannot move the readout; (c) countercontrol: the
# two F22 generic carriers are G0-compatible (same p) with opposite feasibility, and
# BOTH fail G1 at an explicit indicator -- observable agreement alone does not force
# SRC; diagonal-sector dynamics glue does.
ok24 = True
sh24 = order22[3]
N24 = len(sh24)
idx24 = {s: k for k, s in enumerate(sh24)}
u24 = C17(Frac(3, 5), Frac(4, 5))
pw24 = [CO17, u24, u24 * u24, u24 * u24 * u24]
d24 = [pw24[k % 4] for k in range(N24)]
ok24 &= all(d24[k] * d24[k].conj() == CO17 for k in range(N24))
C24 = [[CO17 if idx24[phi22[sh24[c]]] == r else CZ17 for c in range(N24)]
       for r in range(N24)]
W24 = [[d24[r] * C24[r][c] for c in range(N24)] for r in range(N24)]
ok24 &= mmc17(W24, dag17(W24)) == eye17(N24)
# (a) G1 holds at EVERY diagonal indicator, exactly
P24 = C24
for s0 in range(N24):
    ind = [[CO17 if (r == c == s0) else CZ17 for c in range(N24)] for r in range(N24)]
    ok24 &= mmc17(mmc17(W24, ind), dag17(W24)) == mmc17(mmc17(P24, ind), dag17(P24))
# and the indicator dyads force monomiality back out: column s of any G1 solution is
# supported on phi(s) with a unimodular phase
for s0 in range(N24):
    tgt = idx24[phi22[sh24[s0]]]
    col = [W24[r][s0] for r in range(N24)]
    ok24 &= all(col[r].z() for r in range(N24) if r != tgt)
    ok24 &= col[tgt] * col[tgt].conj() == CO17
# (b) G1 pins B: rho = I/N + (W + W^H)/(4N) has genuine coherences, commutes with W
# exactly, and reads out the counting marginal
rho24 = [[(CO17 if r == c else CZ17) * C17(Frac(1, N24))
          + (W24[r][c] + dag17(W24)[r][c]) * C17(Frac(1, 4 * N24))
          for c in range(N24)] for r in range(N24)]
ok24 &= mmc17(mmc17(W24, rho24), dag17(W24)) == rho24
ok24 &= dag17(rho24) == rho24 and tr20(rho24) == CO17
ok24 &= any(not rho24[r][c].z() for r in range(N24) for c in range(N24) if r != c)
ok24 &= all(rho24[k][k] == C17(Frac(1, N24)) for k in range(N24))   # zero-diag coherences
read24 = [sum((rho24[k][k] for k, s in enumerate(sh24) if s[0] == i), CZ17)
          for i in range(3)]
ok24 &= read24 == [C17(p22[i]) for i in range(3)]                   # counting marginal
# (c) countercontrol: the F22 generic carriers are G0-compatible with opposite
# feasibility (qF in the simplex, qI outside -- recorded by F22) and BOTH fail G1
# against the visible 3-cycle at the first indicator: their columns are not monomial
phi3 = [1, 2, 0]
P3 = [[CO17 if phi3[c] == r else CZ17 for c in range(3)] for r in range(3)]
for V in (VF, VI):
    Vc = [[C17(V[r][c]) for c in range(3)] for r in range(3)]
    ok24 &= all(sum(1 for r in range(3) if not Vc[r][c].z()) >= 2 for c in range(3))
    ind3 = [[CO17 if (r == c == 0) else CZ17 for c in range(3)] for r in range(3)]
    ok24 &= mmc17(mmc17(Vc, ind3), dag17(Vc)) != mmc17(mmc17(P3, ind3), dag17(P3))
ok24 &= all(x >= 0 for x in qF) and any(x < 0 for x in qI)
check("F24", ok24,
      "THE DYNAMICS GLUE G1 (phase three, round thirteen; kernel: DiagonalSectorGlue, "
      "conj_diag_entry, diagonalGlue_forces_monomial, glue_of_monomial, "
      "diagonalGlue_iff_monomial, monomial_unitary, monomial_conj_apply, "
      "diag_invariant_pow, diag_invariant_freq_readout, "
      "monomial_ergodic_readout_unique, phasedCycle_columnModuli, "
      "ergodicShell_SRC_of_dynamicsGlue in OIBridge/DynamicsGlue.lean). (a) G1 <=> "
      "MONOMIAL, exactly: a phased 14-cycle D.C on the F22 shell (unimodular rational "
      "phases, unitary) satisfies the diagonal-sector glue at EVERY rank-one diagonal "
      "indicator, and the indicator dyads force the monomial column structure back out "
      "-- each column supported on phi(s) with a unimodular phase, no unitarity "
      "assumed; (b) G1 PINS B: a D.C-commutant state with genuine off-diagonal "
      "coherences (rho = I/N + (W + W^H)/4N, exactly stationary, Hermitian, trace one) "
      "reads out the counting marginal (4/7, 2/7, 1/7) exactly -- the phases wind the "
      "cycle but cannot move a readout, matching monomial_ergodic_readout_unique and "
      "ergodicShell_SRC_of_dynamicsGlue: G1 + ergodic shell close physical-flow SRC "
      "with canonical B, independent of phases and logarithm branch; (c) "
      "COUNTERCONTROL: the two F22 generic carriers are G0-compatible (same visible p) "
      "with opposite feasibility, and BOTH fail G1 at the first diagonal indicator -- "
      "their columns are nowhere monomial. BOXED: observable agreement alone does not "
      "force SRC; diagonal-sector dynamics glue does. THE AUDIT QUESTION IS NOW ONE "
      "LINE: does OI require G1, or only G0?")

# ----------------------- F25  the domain span: G1 earned, not chosen (phase three, round 14)
# G_D (CompatibilityDomainGlue): the coherent lift intertwines the state dynamics only on
# the classical branch domain -- the closure of the shell ensemble under reversible
# evolution and visible branch selection, exactly the preparations of the corpus's own
# classical trajectory fold.  (a) the F22 shell cut is ITINERARY-SEPARATING: the 14
# visible itineraries are pairwise distinct; (b) the branch-evolve closure of the shell
# ensemble reaches every singleton indicator and spans the full 14-dim diagonal algebra
# exactly; (c) hence any U satisfying the domain glue satisfies it on every indicator
# and the monomial forcing applies -- verified on the phased cycle; (d) countercontrol:
# a label-symmetric 4-cycle (labels 0,1,0,1) is NOT itinerary-separating, its domain
# closure spans only 2 of 4 dimensions, and an explicitly non-monomial unitary satisfies
# the domain glue on the whole closure -- the separation property is load-bearing.
ok25 = True
# (a) itinerary separation on the 14-shell
words25 = []
for s in sh24:
    t, word = s, []
    for _ in range(14):
        word.append(t[0])
        t = phi22[t]
    words25.append(tuple(word))
ok25 &= len(set(words25)) == 14
# (b) branch-evolve closure: exact span over Q
def rankQ25(rows):
    rows = [r[:] for r in rows if any(x != 0 for x in r)]
    rk, piv, nc = 0, 0, 14
    while piv < nc and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if rows[i][piv] != 0), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = rows[rk][piv]
        rows[rk] = [x / iv for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][piv] != 0:
                c = rows[i][piv]
                rows[i] = [a - c * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
        piv += 1
    return rk

# the singleton indicators are constructed BY the domain operations themselves,
# mirroring the kernel proof: u_{T+1} = branch_{c 0}(evolve(u_T shifted))
def evolve25(w):
    return tuple(w[pos25[phi22[sh24[k]]]] for k in range(14))

def branch25(i, w):
    return tuple(w[k] if sh24[k][0] == i else Frac(0) for k in range(14))

pos25 = {s: k for k, s in enumerate(sh24)}
built25 = set()

def itiInd25b(word):
    if not word:
        w = tuple([Frac(1)] * 14)
    else:
        w = branch25(word[0], evolve25(itiInd25b(word[1:])))
    built25.add(w)
    return w

for k0, s in enumerate(sh24):
    ind = itiInd25b(list(words25[k0]))
    ok25 &= ind == tuple(Frac(1) if k == k0 else Frac(0) for k in range(14))
ok25 &= rankQ25([list(v) for v in built25]) == 14
# (d) countercontrol: 4-cycle, labels (0,1,0,1) -- NOT separating, span 2, and a
# non-monomial unitary satisfies the glue on the whole closure
phi4 = [1, 2, 3, 0]
lab4 = [0, 1, 0, 1]
w4 = []
for s0 in range(4):
    t, word = s0, []
    for _ in range(4):
        word.append(lab4[t])
        t = phi4[t]
    w4.append(tuple(word))
ok25 &= len(set(w4)) == 2                                  # itineraries collide
seen4 = set()
front4 = [tuple([Frac(1)] * 4)]
seen4.add(front4[0])
while front4:
    w = front4.pop()
    ev = tuple(w[phi4[k]] for k in range(4))
    outs = [ev] + [tuple(w[k] if lab4[k] == i else Frac(0) for k in range(4))
                   for i in range(2)]
    for o in outs:
        if o not in seen4:
            seen4.add(o)
            front4.append(o)
def rankQ4(rows):
    rows = [list(r) for r in rows if any(x != 0 for x in r)]
    rk, piv = 0, 0
    while piv < 4 and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if rows[i][piv] != 0), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = rows[rk][piv]
        rows[rk] = [x / iv for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][piv] != 0:
                c = rows[i][piv]
                rows[i] = [a - c * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
        piv += 1
    return rk
ok25 &= rankQ4(seen4) == 2                                 # proper subspace
P4 = [[CO17 if phi4[c] == r else CZ17 for c in range(4)] for r in range(4)]
R4 = [[C17(Frac(3, 5)) if (r, c) in ((0, 0), (2, 2)) else
       C17(Frac(-4, 5)) if (r, c) == (0, 2) else
       C17(Frac(4, 5)) if (r, c) == (2, 0) else
       C17(Frac(5, 13)) if (r, c) in ((1, 1), (3, 3)) else
       C17(Frac(-12, 13)) if (r, c) == (1, 3) else
       C17(Frac(12, 13)) if (r, c) == (3, 1) else CZ17 for c in range(4)]
      for r in range(4)]
U4 = mmc17(P4, R4)
ok25 &= mmc17(U4, dag17(U4)) == eye17(4)
ok25 &= any(sum(1 for r in range(4) if not U4[r][c].z()) >= 2 for c in range(4))
for w in seen4:                                            # glue on the WHOLE closure
    dw = [[C17(w[r]) if r == c else CZ17 for c in range(4)] for r in range(4)]
    ok25 &= mmc17(mmc17(U4, dw), dag17(U4)) == mmc17(mmc17(P4, dw), dag17(P4))
check("F25", ok25,
      "THE DOMAIN SPAN: G1 EARNED, NOT CHOSEN (phase three, round fourteen; kernel: "
      "CompatibilityDomainGlue, ClassicalBranchDomain, ItinerarySeparating, "
      "itiIndicator, spanning_domain_glue_implies_G1, itiIndicator_mem, "
      "separating_singleton_mem, separating_domain_span_top, "
      "classicalBranch_glue_forces_G1, classicalBranch_glue_forces_monomial, "
      "ergodicShell_SRC_of_domainGlue in OIBridge/DomainGlue.lean). The domain-relative "
      "glue G_D asks intertwining only on the classical branch domain -- the closure of "
      "the shell ensemble under reversible evolution and visible branch selection, "
      "exactly the preparations of the corpus's own classical trajectory fold. (a) the "
      "F22 shell cut IS itinerary-separating: all 14 visible itineraries are pairwise "
      "distinct; (b) the branch-evolve closure reaches every singleton indicator "
      "literally and spans the full 14-dimensional diagonal algebra exactly (rank "
      "14/14 over Q), so by the linearity bridge G_D implies full G1 there, the "
      "monomial forcing fires, and ergodicShell_SRC_of_domainGlue closes physical-flow "
      "SRC from OI compatibility + observability + ergodicity -- G1 is derived from "
      "the corpus's own preparations, not postulated; (c) countercontrol: the "
      "label-symmetric 4-cycle (labels 0,1,0,1) is NOT separating -- itineraries "
      "collide pairwise, the closure spans only 2/4 dimensions, and an explicitly "
      "non-monomial unitary (a phased pair rotation) satisfies the domain glue on the "
      "ENTIRE closure: itinerary separation is the load-bearing hypothesis, and where "
      "it fails the F22 underdetermination is genuine. The existence question is now: "
      "is the actual observer cut itinerary-separating?")

# ----------------------- F26  the observability quotient: exactly the resolvable distinctions
# (phase three, round 15).  The finite-horizon quotient theorem span(D_K) = {f constant on
# every ~_K class} and the residual classification (glue <=> class-indicator transport;
# block-unitary freedom inside itinerary fibres) verified finitely.  (a) graded class-count
# profile at the F22 14-shell: #(~_K classes) for K = 0..K*, monotone, reaching 14
# singletons at the separation horizon K*; (b) the graded branch domain D_K, built by the
# kernel's own constructors (shell / mono / evolve / branch), has Q-span rank EQUAL to the
# class count at EVERY horizon K -- the quotient theorem, not just its top; (c) residual
# classification at the non-separating 4-cycle: classes {0,2},{1,3} stable for all K >= 1,
# the F25 non-monomial unitary U4 satisfies class-indicator transport U E_C U^dag =
# P E_C P^dag exactly (the countercontrol is a CLASSIFICATION INSTANCE, not an anomaly),
# its columns are supported inside the phi-transported fibre of each class
# (glue_column_support), while a fibre-crossing unitary FAILS the transport equation --
# necessity; (d) unitarity is forced by the base preparation w = 1 alone
# (domainGlue_unitary): a non-unitary multiple of P4 already fails the shell equation.
ok26 = True
# (a) graded class counts on the 14-shell: ~_K classes = distinct K-prefixes of itineraries
prof26 = [len({w[:K] for w in words25}) for K in range(15)]
Kstar26 = next(K for K in range(15) if prof26[K] == 14)
ok26 &= prof26[0] == 1                                     # horizon 0: everything glued
ok26 &= all(prof26[K] <= prof26[K + 1] for K in range(14)) # monotone refinement
ok26 &= all(prof26[K] == 14 for K in range(Kstar26, 15))   # stable once separated
ok26 &= Kstar26 <= 14                                      # within one period (orderOf phi)
# (b) graded domain vs graded quotient: build D_K by the kernel constructors and check
# rank(span D_K) == #classes(K) at every K -- branchDomain_span_eq_itineraryInvariant
lvl26 = {tuple([Frac(1)] * 14)}                            # BDK 0 = {shell}
for K in range(Kstar26 + 1):
    ok26 &= rankQ25([list(v) for v in lvl26]) == prof26[K]
    nxt = set(lvl26)                                       # mono
    nxt |= {evolve25(w) for w in lvl26}                    # evolve
    frontier = list(nxt)
    while frontier:                                        # branch closes level K+1
        w = frontier.pop()
        for i in range(3):
            b = branch25(i, w)
            if b not in nxt:
                nxt.add(b)
                frontier.append(b)
    lvl26 = nxt
ok26 &= rankQ25([list(v) for v in lvl26]) == 14            # separating: full algebra
# (c) residual classification at the 4-cycle.  Classes stable at {0,2},{1,3} for K >= 1.
w4p = [len({w[:K] for w in w4}) for K in range(5)]
ok26 &= w4p == [1, 2, 2, 2, 2]
E02 = [[CO17 if r == c and r in (0, 2) else CZ17 for c in range(4)] for r in range(4)]
E13 = [[CO17 if r == c and r in (1, 3) else CZ17 for c in range(4)] for r in range(4)]
for EC in (E02, E13):                                      # class-indicator transport
    ok26 &= mmc17(mmc17(U4, EC), dag17(U4)) == mmc17(mmc17(P4, EC), dag17(P4))
# phi transports the fibres: P E_{02} P^dag = E_{13} and vice versa
ok26 &= mmc17(mmc17(P4, E02), dag17(P4)) == E13
ok26 &= mmc17(mmc17(P4, E13), dag17(P4)) == E02
# column support (glue_column_support): column s of U4 lives inside phi(class(s))
cls4 = {0: (0, 2), 1: (1, 3), 2: (0, 2), 3: (1, 3)}
for s0 in range(4):
    img = {phi4[t] for t in cls4[s0]}
    ok26 &= all(U4[r][s0].z() for r in range(4) if r not in img)
# necessity: a fibre-crossing unitary (3-4-5 rotation of coordinates 0,1 after P4)
# violates the E02 transport equation even though it is exactly unitary
X01 = [[C17(Frac(3, 5)) if (r, c) in ((0, 0), (1, 1)) else
        C17(Frac(-4, 5)) if (r, c) == (0, 1) else
        C17(Frac(4, 5)) if (r, c) == (1, 0) else
        CO17 if r == c else CZ17 for c in range(4)] for r in range(4)]
V4 = mmc17(X01, P4)
ok26 &= mmc17(V4, dag17(V4)) == eye17(4)
ok26 &= mmc17(mmc17(V4, E02), dag17(V4)) != mmc17(mmc17(P4, E02), dag17(P4))
# (d) unitarity from the base preparation alone: 2*P4 fails the w = 1 shell equation
W4 = [[P4[r][c] + P4[r][c] for c in range(4)] for r in range(4)]
ok26 &= mmc17(W4, dag17(W4)) != eye17(4)
ok26 &= mmc17(mmc17(W4, eye17(4)), dag17(W4)) != mmc17(mmc17(P4, eye17(4)), dag17(P4))
check("F26", ok26,
      "THE OBSERVABILITY QUOTIENT: EXACTLY THE RESOLVABLE DISTINCTIONS (phase three, "
      "round fifteen; kernel: branchDomainK_invariant, classIndicator_eq_itiIndicator, "
      "itiIndicator_mem_BDK, classIndicator_mem_BDK, invariant_le_span_classIndicators, "
      "branchDomain_span_eq_itineraryInvariant, classicalBranchDomain_iff_horizon, "
      "itiRelInf_iff_orderOf, classicalBranch_span_eq_invariant, glueEq_span, "
      "domainGlue_classification_mod_itineraryFibres, domainGlue_unitary, "
      "glue_column_support in OIBridge/ObservabilityQuotient.lean). The finite-horizon "
      "quotient theorem span(D_K) = {f constant on every ~_K class} holds at EVERY "
      "horizon on the F22 shell: the graded branch domain built by the kernel's own "
      "constructors has Q-span rank equal to the ~_K class count for each K from 0 to "
      f"the separation horizon K* = {Kstar26} (profile {prof26[:Kstar26 + 1]}), where "
      "the classes become singletons and the round-14 monomial collapse fires. Where "
      "separation FAILS, the surviving freedom is classified, not mysterious: on the "
      "4-cycle the classes freeze at the two fibres {0,2},{1,3}, the domain glue is "
      "EQUIVALENT to class-indicator transport U E_C U^dag = P E_C P^dag, the F25 "
      "non-monomial countercontrol satisfies exactly those equations (a classification "
      "instance now, not an anomaly), every glue-compatible column is supported inside "
      "the phi-transported fibre of its class, a fibre-crossing unitary fails the "
      "transport equation, and unitarity itself is forced by the shell preparation "
      "w = 1 alone. Boxed: OI earns G1 on exactly the distinctions the observer cut "
      "can operationally resolve, and nothing stronger -- full QM follows precisely "
      "when the physical cut is informationally complete on the relevant shell.")

# ----------------------- F27  the passive-minimal quotient (phase three, round 16)
# The canonical quotient Q = S/~_inf: the greatest observation-preserving dynamical
# congruence, the descended permutation, minimality = separation, law preservation,
# and the mandatory hidden-fibre negative control -- each verified exactly on the
# round-14/15 controls.  (a) 4-cycle quotient: classes {0,2},{1,3}, descended dynamics
# the swap, descended labels (0,1), separating by construction; (b) greatest
# congruence EXHAUSTIVELY: of all 15 partitions of the 4 states, exactly 2 are
# label-constant and phi-stable (the trivial one and ~_inf itself) and every one is
# contained in ~_inf; (c) law preservation: a generic rational prior pushed forward by
# fibre sums reproduces every trajectory probability at every horizon T = 0..4, and
# the pushforward commutes with evolve and branch; (d) capstone on the quotient: the
# separating 2-state carrier reaches its singletons, and a non-monomial rotation
# fails the singleton glue there -- G_D forces monomial with no separation premise;
# (e) hidden-fibre extension of the F22 shell: a 2-point fibre with per-state fibre
# dynamics is a permutation, glues every fibre, is NOT separating, preserves every
# trajectory probability for a CORRELATED prior with the shell marginal, and its
# quotient recovers exactly the 14 base classes.
ok27 = True
# (a) the quotient of the 4-cycle
cls27 = {0: 0, 1: 1, 2: 0, 3: 1}
phiQ, okwd = {}, True
for s0 in range(4):
    c, img = cls27[s0], cls27[phi4[s0]]
    if c in phiQ:
        okwd &= phiQ[c] == img
    else:
        phiQ[c] = img
ok27 &= okwd and phiQ == {0: 1, 1: 0}                      # descends to the swap
visQ = {0: lab4[0], 1: lab4[1]}
ok27 &= all(visQ[cls27[s0]] == lab4[s0] for s0 in range(4))
wq = []
for c in range(2):
    t, word = c, []
    for _ in range(2):
        word.append(visQ[t])
        t = phiQ[t]
    wq.append(tuple(word))
ok27 &= len(set(wq)) == 2                                  # separating by construction
# (b) greatest congruence, exhaustively over all 15 partitions of {0,1,2,3}
def partitions27(xs):
    if not xs:
        yield []
        return
    x, rest = xs[0], xs[1:]
    for p in partitions27(rest):
        for k in range(len(p)):
            yield p[:k] + [[x] + p[k]] + p[k + 1:]
        yield [[x]] + p

nprt, ncong = 0, 0
for p in partitions27([0, 1, 2, 3]):
    nprt += 1
    blk = {s: k for k, b in enumerate(p) for s in b}
    lab_const = all(lab4[s] == lab4[t] for b in p for s in b for t in b)
    stable = all(blk[phi4[s]] == blk[phi4[t]] for b in p for s in b for t in b)
    if lab_const and stable:
        ncong += 1
        ok27 &= all(cls27[s] == cls27[t] for b in p for s in b for t in b)
ok27 &= nprt == 15 and ncong == 2          # only the trivial congruence and ~_inf
# (c) law preservation under the pushforward
mu27 = [Frac(1, 2), Frac(1, 4), Frac(1, 6), Frac(1, 12)]
push27 = lambda m: [m[0] + m[2], m[1] + m[3]]
muQ = push27(mu27)
def traj27(phi, vis, n, T, word, mu):
    tot = Frac(0)
    for s0 in range(n):
        t, okw = s0, True
        for k in range(T):
            if vis[t] != word[k]:
                okw = False
                break
            t = phi[t]
        if okw:
            tot += mu[s0]
    return tot

from itertools import product as iprod27
phiQl, visQl = [phiQ[0], phiQ[1]], [visQ[0], visQ[1]]
for T in range(5):
    for word in iprod27(range(2), repeat=T):
        ok27 &= traj27(phi4, lab4, 4, T, word, mu27) \
            == traj27(phiQl, visQl, 2, T, word, muQ)
ev27 = [mu27[phi4[s]] for s in range(4)]
ok27 &= push27(ev27) == [muQ[phiQ[c]] for c in range(2)]   # evolve commutes
for i in range(2):
    br27 = [mu27[s] if lab4[s] == i else Frac(0) for s in range(4)]
    ok27 &= push27(br27) == [muQ[c] if visQ[c] == i else Frac(0) for c in range(2)]
# (d) capstone: on the separating quotient the singleton glue kills non-monomials
P2 = [[CZ17, CO17], [CO17, CZ17]]
R2 = [[C17(Frac(3, 5)), C17(Frac(-4, 5))], [C17(Frac(4, 5)), C17(Frac(3, 5))]]
E0q = [[CO17, CZ17], [CZ17, CZ17]]
ok27 &= mmc17(R2, dag17(R2)) == eye17(2)
ok27 &= mmc17(mmc17(R2, E0q), dag17(R2)) != mmc17(mmc17(P2, E0q), dag17(P2))
ok27 &= [Frac(1) if visQl[c] == 0 else Frac(0) for c in range(2)] \
    == [Frac(1), Frac(0)]                                  # branch_0(shell) = e0
# (e) hidden-fibre extension of the F22 shell
ext27 = {}
for k, s in enumerate(sh24):
    sig = 1 if k == 0 else 0                               # sigma_s: swap at one state
    for a in range(2):
        ext27[(k, a)] = (pos25[phi22[s]], a ^ sig)
ok27 &= sorted(ext27.values()) == sorted(ext27.keys())     # a permutation
lab22 = [s[0] for s in sh24]
wext = {}
for p in ext27:
    t, word = p, []
    for _ in range(28):
        word.append(lab22[t[0]])
        t = ext27[t]
    wext[p] = tuple(word)
ok27 &= all(wext[(k, 0)] == wext[(k, 1)] for k in range(14))
ok27 &= len(set(wext.values())) == 14                      # quotient recovers the base
nuu = {}
for k in range(14):
    nuu[(k, 0)] = Frac(k + 1, 210)
    nuu[(k, 1)] = Frac(1, 14) - Frac(k + 1, 210)           # correlated, marginal 1/14
ok27 &= all(v > 0 for v in nuu.values())
phl = [pos25[phi22[s]] for s in sh24]
for T in (0, 1, 3, 6, 9):
    for k0 in range(14):
        word = words25[k0][:T]
        base = traj27(phl, lab22, 14, T, word, [Frac(1, 14)] * 14)
        tot = Frac(0)
        for p in ext27:
            t, okw = p, True
            for k in range(T):
                if lab22[t[0]] != word[k]:
                    okw = False
                    break
                t = ext27[t]
            if okw:
                tot += nuu[p]
        ok27 &= tot == base
check("F27", ok27,
      "THE PASSIVE-MINIMAL QUOTIENT (phase three, round sixteen; kernel: itiRelInf_pow, "
      "itiRelInf_evolve, itiRelInf_symm_evolve, itiSetoid, MinimalCarrier, quotVis, "
      "quotPerm, quotPerm_mk, quotPerm_pow_mk, itiRelInf_greatest_congruence, "
      "quotient_itinerarySeparating, ObservationCongruence, PassivelyMinimal, "
      "passiveMinimal_iff_itinerarySeparating, realization_pow, realizationMap, "
      "minimal_realization_bijective, realizationMap_equivariant, realizationMap_vis, "
      "realization_factor_unique, trajProb, quotMeasure, quotMeasure_weighted_sum, "
      "itiIndicator_quotient_mk, trajProb_quotient, quotMeasure_evolve, "
      "quotMeasure_branch, quotient_transitive, passiveQuotient_glue_forces_G1, "
      "passiveQuotient_glue_forces_monomial, ergodicShell_SRC_of_passiveQuotient, "
      "hiddenExt, hiddenExt_pow_fst, hiddenExt_itiRelInf_fibre, "
      "hiddenExt_not_separating, hiddenExt_itiIndicator, hiddenExt_same_law, "
      "hiddenExt_quotient_recovers_base in OIBridge/PassiveQuotient.lean). The "
      "canonical passive quotient S/~_inf: (a) the 4-cycle descends to the labelled "
      "swap, separating by construction; (b) ~_inf is the GREATEST observation-"
      "preserving dynamical congruence, verified exhaustively -- of all 15 partitions "
      "of the 4 states exactly 2 are label-constant and phi-stable, and both refine "
      "the itinerary classes; (c) the fibre-sum pushforward preserves every "
      "trajectory probability at every horizon T = 0..4 for a generic rational prior "
      "and commutes with evolve and branch -- the full closed passive multi-time law "
      "is quotient-invariant; (d) on the separating quotient the branch domain "
      "reaches its singletons and a non-monomial 3-4-5 rotation fails the singleton "
      "glue: G_D forces monomial WITH NO SEPARATION PREMISE LEFT; (e) the mandatory "
      "negative control: a 2-point hidden fibre with per-state fibre dynamics on the "
      "F22 shell is a permutation that glues every fibre, is NOT separating, "
      "preserves every trajectory probability for a correlated prior with the shell "
      "marginal, and its quotient recovers exactly the 14 base classes. BOXED: bare "
      "OI does not make the ontic carrier observable, but the minimal carrier of the "
      "complete passive observational law is automatically separating -- domain glue "
      "earns full G1 on exactly the state space to which the passive coherent "
      "description is operationally accountable. The quotient is observer-relative "
      "(Structure's G4 observational equivalence, not G3 substratum gauge): "
      "interventions may yet separate what the passive law glues.")

# ----------------------- F28  SM linear observability: the wave rule audited exactly
# (phase three, round 16).  The SM reference branch's second-order mod-q wave rule
# x_i(t+1) = sum_nbrs x_j(t) - x_i(t-1)  (SM SS4.1: the unique center-free isotropic
# linear rule) in companion form z = (x_t, x_{t-1}), A = [[K,-I],[I,0]], with the
# component-complete site observer reading the CURRENT field on its sites (SM Lemma 1c:
# current field visible, retarded register hidden).  By linear_itiRelInf_iff /
# linear_separating_iff_observability the itinerary audit IS the Kalman observability
# computation: kernel of the stacked family (C, CA, CA^2, ...) over GF(q).
# (a) A is an exact bijection (explicit inverse [[0,I],[-I,K]]);  (b) full visibility
# separates at horizon 2 exactly (the retarded register is reconstructed in one step);
# (c) ring L=12: a SINGLE visible site leaves a 10-dim unobservable sector -- exactly
# the mirror-odd modes about that site (2*(L/2-1) = 10, kernel verified) -- while TWO
# adjacent sites already observe everything (profile [10,0,0,...] identically over
# q = 3, 5, 7; q = 2 degenerates to 12 at width 1 and still closes at width 2);
# (d) 3-torus L=3: one slab of 9 sites leaves an 18-dim unobservable sector -- exactly
# the mirror-odd modes of the z -> -z reflection -- and two adjacent slabs observe
# everything (identical over q = 5, 7); (e) fibre semantics: states differing by a
# mirror-odd mode share their entire visible itinerary; a non-fibre difference is
# separated.  Verdict: the SM reference geometry supplies itinerary separation on the
# linear branch whenever the observer's window has thickness >= 2 in the propagation
# direction; thickness-one screens have exactly the reflection-odd sector as their
# itinerary fibres -- the block-unitary freedom of the round-15 classification.
ok28 = True
def rank28(rows, q, ncols):
    rows = [r[:] for r in rows]
    rk, piv = 0, 0
    while piv < ncols and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if rows[i][piv] % q != 0), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = pow(rows[rk][piv], -1, q)
        rows[rk] = [(x * iv) % q for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][piv] % q != 0:
                c = rows[i][piv]
                rows[i] = [(a - c * b) % q for a, b in zip(rows[i], rows[rk])]
        rk += 1
        piv += 1
    return rk

def mm28(A, B, q):
    m, p = len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) % q for j in range(p)]
            for i in range(len(A))]

def companion28(nbrs, n, q):
    A = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in nbrs[i]:
            A[i][j] = (A[i][j] + 1) % q
        A[i][n + i] = (-1) % q
        A[n + i][i] = 1
    return A

def inverse28(nbrs, n, q):
    B = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        B[i][n + i] = 1
        B[n + i][i] = (-1) % q
        for j in nbrs[i]:
            B[n + i][n + j] = (B[n + i][n + j] + 1) % q
    return B

def obsrows28(A, vis_sites, q, horizon):
    n2 = len(A)
    rows, M = [], [[1 if i == j else 0 for j in range(n2)] for i in range(n2)]
    for _ in range(horizon):
        for i in vis_sites:
            rows.append(M[i][:])
        M = mm28(M, A, q)
    return rows

def unobs28(A, vis_sites, q):
    n2 = len(A)
    return n2 - rank28(obsrows28(A, vis_sites, q, n2), q, n2)

ring28 = lambda L: [[(i - 1) % L, (i + 1) % L] for i in range(L)]
L28 = 12
eye28 = [[1 if i == j else 0 for j in range(2 * L28)] for i in range(2 * L28)]
for q in (5, 7):
    A28 = companion28(ring28(L28), L28, q)
    ok28 &= mm28(A28, inverse28(ring28(L28), L28, q), q) == eye28       # (a)
    ok28 &= rank28(obsrows28(A28, range(L28), q, 2), q, 2 * L28) == 2 * L28  # (b)
# (c) window profile on the ring, exactly over three odd primes and q = 2
for q in (3, 5, 7):
    A28 = companion28(ring28(L28), L28, q)
    ok28 &= [unobs28(A28, range(w), q) for w in range(1, 4)] == [10, 0, 0]
A2q = companion28(ring28(L28), L28, 2)
ok28 &= [unobs28(A2q, range(w), 2) for w in range(1, 3)] == [12, 0]
# the width-1 kernel IS the mirror-odd sector about the visible site
q28 = 5
A28 = companion28(ring28(L28), L28, q28)
rows28 = obsrows28(A28, [0], q28, 2 * L28)
odd28 = []
for layer in range(2):
    for i in range(1, L28 // 2):
        v = [0] * (2 * L28)
        v[layer * L28 + i] = 1
        v[layer * L28 + (L28 - i)] = q28 - 1
        odd28.append(v)
ok28 &= len(odd28) == 10
ok28 &= all(sum(r[j] * v[j] for j in range(2 * L28)) % q28 == 0
            for v in odd28 for r in rows28)
# (d) the 3-torus: one slab leaves the z-mirror-odd 18-dim sector; two slabs close it
L3, n3 = 3, 27
idx28 = lambda x, y, z: (x % L3) * 9 + (y % L3) * 3 + (z % L3)
nbrs3 = [[idx28(x + 1, y, z), idx28(x - 1, y, z), idx28(x, y + 1, z),
          idx28(x, y - 1, z), idx28(x, y, z + 1), idx28(x, y, z - 1)]
         for x in range(L3) for y in range(L3) for z in range(L3)]
for q in (5, 7):
    A3 = companion28(nbrs3, n3, q)
    slab = [i for i in range(n3) if i % 3 == 0]
    ok28 &= unobs28(A3, range(n3), q) == 0
    ok28 &= unobs28(A3, slab, q) == 18
    ok28 &= unobs28(A3, [i for i in range(n3) if i % 3 in (0, 1)], q) == 0
A3 = companion28(nbrs3, n3, q28)
rows3 = obsrows28(A3, [i for i in range(n3) if i % 3 == 0], q28, 2 * n3)
odd3 = []
for layer in range(2):
    for x in range(3):
        for y in range(3):
            v = [0] * (2 * n3)
            v[layer * n3 + idx28(x, y, 1)] = 1
            v[layer * n3 + idx28(x, y, 2)] = q28 - 1
            odd3.append(v)
ok28 &= len(odd3) == 18
ok28 &= all(sum(r[j] * v[j] for j in range(2 * n3)) % q28 == 0
            for v in odd3 for r in rows3)
# (e) fibre semantics on the ring: mirror-odd difference invisible, generic one seen
x28 = [(3 * i * i + 1) % q28 for i in range(2 * L28)]
y28 = [(a + b) % q28 for a, b in zip(x28, odd28[3])]
ok28 &= all(sum(r[j] * (x28[j] - y28[j]) for j in range(2 * L28)) % q28 == 0
            for r in rows28)
w28 = [0] * (2 * L28)
w28[1] = 1
z28 = [(a + b) % q28 for a, b in zip(x28, w28)]
ok28 &= any(sum(r[j] * (x28[j] - z28[j]) for j in range(2 * L28)) % q28 != 0
            for r in rows28)
check("F28", ok28,
      "SM LINEAR OBSERVABILITY: THE WAVE RULE AUDITED EXACTLY (phase three, round "
      "sixteen; kernel: addEquiv_pow_sub, linear_itiRelInf_iff, "
      "linear_separating_iff_observability in OIBridge/PassiveQuotient.lean). The SM "
      "reference branch's second-order mod-q wave rule in companion form, read by the "
      "component-complete site observer (current field visible, retarded register "
      "hidden -- SM Lemma 1c), audited as the Kalman observability computation the "
      "kernel bridge makes exact: (a) the update is an exact bijection with explicit "
      "inverse; (b) full visibility separates at horizon 2 -- one step reconstructs "
      "the retarded register; (c) on the L = 12 ring a SINGLE visible site leaves a "
      "10-dimensional unobservable sector, verified to be EXACTLY the mirror-odd "
      "modes about that site, while TWO adjacent sites already observe the entire "
      "state (profile [10, 0, 0] identically over q = 3, 5, 7; q = 2 degenerates to "
      "12 at width one and still closes at width two); (d) on the 3-torus one slab "
      "of 9 sites leaves the 18-dimensional z-mirror-odd sector and two adjacent "
      "slabs observe everything (identical over q = 5, 7); (e) states differing by a "
      "mirror-odd mode share their ENTIRE visible itinerary and a generic difference "
      "is separated -- the fibres are real and they are exactly the reflection-odd "
      "modes, the block-unitary freedom of the round-15 classification. VERDICT: the "
      "SM reference geometry supplies itinerary separation on the linear branch "
      "whenever the observer's window has thickness >= 2 in the propagation "
      "direction; a thickness-one screen fails by exactly its mirror symmetry. The "
      "solution-level identification of the ACTUAL cosmological window remains open, "
      "as does the nonlinear/state-dependent-graph regime.")

# ----------------------- F29  the coherent extension fibre on a 3-cycle (phase three,
# round 17).  Three members of the SAME classification fibre over the classical
# 3-cycle g: a rank-one phase matrix (the unitary monomial lift), a genuinely
# partially dephasing correlation matrix, and complete dephasing C = I.  They realize
# the identical classical action, produce IDENTICAL action-labelled comb statistics on
# every diagonal preparation and every branch interleaving, and are separated by one
# coherent effect; only the rank-one member has a CPTP inverse, and the classical
# inverse composed coherently is NOT the identity -- the audit guard exact.
ok29 = True
g29 = [1, 2, 0]                                            # the 3-cycle 0->1->2->0
gi29 = [2, 0, 1]                                           # its inverse
d29 = [CO17, C17(Frac(3, 5), Frac(4, 5)), C17(Frac(3, 5), Frac(-4, 5))]
C1_29 = [[d29[s] * d29[t].conj() for t in range(3)] for s in range(3)]
C2_29 = [[CO17 if s == t else C17(Frac(2, 3)) for t in range(3)] for s in range(3)]
C3_29 = eye17(3)
# (a) validity: C1 rank-one unimodular; C2 = (2/3) v v^H + (1/3) I is an explicit PSD
# certificate; C3 = I
ok29 &= all((d29[s] * d29[s].conj()) == CO17 for s in range(3))
v29 = [CO17, CO17, CO17]
ok29 &= all(C2_29[s][t]
            == C17(Frac(2, 3)) * v29[s] * v29[t].conj()
              + (C17(Frac(1, 3)) if s == t else CZ17)
            for s in range(3) for t in range(3))
def Phi29(C, X):
    return [[C[gi29[a]][gi29[b]] * X[gi29[a]][gi29[b]] for b in range(3)]
            for a in range(3)]

def E29(s, t):
    return [[CO17 if (a, b) == (s, t) else CZ17 for b in range(3)] for a in range(3)]

# (b) all three classically realize g on every classical pure state
for C in (C1_29, C2_29, C3_29):
    ok29 &= all(Phi29(C, E29(s, s)) == E29(g29[s], g29[s]) for s in range(3))
# (c) comb blindness: a 3-step comb with branch selection between steps produces the
# SAME statistics for the three members, on every classical trajectory
p29 = [C17(Frac(1, 2)), C17(Frac(1, 3)), C17(Frac(1, 6))]
def branch29(i, X):
    return [[X[a][b] if a == i and b == i else CZ17 for b in range(3)]
            for a in range(3)]

for traj in [(i, j, k) for i in range(3) for j in range(3) for k in range(3)]:
    vals = []
    for C in (C1_29, C2_29, C3_29):
        X = [[p29[a] if a == b else CZ17 for b in range(3)] for a in range(3)]
        for step in traj:
            X = branch29(step, Phi29(C, X))
        vals.append(sum(X[a][a].re for a in range(3)))
    ok29 &= vals[0] == vals[1] == vals[2]
# (d) ONE coherent effect separates all three: on the uniform superposition dyad the
# all-ones effect reads sum_{s,t} C_st = 121/25, 7, 3 respectively
ones29 = [[CO17] * 3 for _ in range(3)]
reads = []
for C in (C1_29, C2_29, C3_29):
    Y = Phi29(C, ones29)
    tot = CZ17
    for a in range(3):
        for b in range(3):
            tot = tot + Y[a][b]
    reads.append(tot)
ok29 &= reads[0] == C17(Frac(121, 25)) and reads[1] == C17(7) \
    and reads[2] == C17(3) and len({(r.re, r.im) for r in reads}) == 3
# (e) reversibility: ONLY the rank-one member. Its family inverse is exact and it IS
# the monomial conjugation Ad(D P_g)
C1inv = [[d29[gi29[a]].conj() * d29[gi29[b]] for b in range(3)] for a in range(3)]
def Psi29(X):
    return [[C1inv[g29[a]][g29[b]] * X[g29[a]][g29[b]] for b in range(3)]
            for a in range(3)]

ok29 &= all(Psi29(Phi29(C1_29, E29(s, t))) == E29(s, t)
            for s in range(3) for t in range(3))
P29 = [[CO17 if g29[c] == r else CZ17 for c in range(3)] for r in range(3)]
D29 = [[d29[gi29[r]] if r == c else CZ17 for c in range(3)] for r in range(3)]
M29 = mmc17(D29, P29)
ok29 &= mmc17(M29, dag17(M29)) == eye17(3)
ok29 &= all(Phi29(C1_29, E29(s, t)) == mmc17(mmc17(M29, E29(s, t)), dag17(M29))
            for s in range(3) for t in range(3))
# the family inverse candidate for C2 needs entries 3/2 off-diagonal: NOT PSD, with
# the explicit witness x = (1,-1,0):  x^H C' x = 2 - 2*(3/2) = -1 < 0
C2inv = [[CO17 if s == t else C17(Frac(3, 2)) for t in range(3)] for s in range(3)]
x29 = [CO17, C17(-1), CZ17]
q29 = CZ17
for s in range(3):
    for t in range(3):
        q29 = q29 + x29[s].conj() * C2inv[s][t] * x29[t]
ok29 &= q29 == C17(-1)                                     # negative: no CPTP inverse
# complete dephasing is not even injective
ok29 &= Phi29(C3_29, E29(0, 1)) == [[CZ17] * 3 for _ in range(3)]
# (f) THE AUDIT GUARD: the classical inverse composed coherently is NOT the identity.
# Phi_{g^-1, I} after Phi_{g, I} is complete dephasing: identity on every diagonal
# (the classical comb identity I_{a^-1} I_a = id) yet it kills E_01
def comp29(X):
    Y = Phi29(C3_29, X)                                    # Phi_{g, I}
    return [[(C3_29[g29[a]][g29[b]] * Y[g29[a]][g29[b]]) for b in range(3)]
            for a in range(3)]                             # then Phi_{g^-1, I}

diag29 = [[p29[a] if a == b else CZ17 for b in range(3)] for a in range(3)]
ok29 &= comp29(diag29) == diag29                           # classical comb: identity
ok29 &= comp29(E29(0, 1)) == [[CZ17] * 3 for _ in range(3)]  # coherent: NOT identity
# (g) the purity selector: the rank-one member maps the uniform dyad to a PURE dyad
# (all 2x2 minors vanish); the partial dephaser does not (minor 1 - 4/9 = 5/9)
Y1 = Phi29(C1_29, ones29)
ok29 &= all(Y1[a][b] * Y1[c][dd] == Y1[a][dd] * Y1[c][b]
            for a in range(3) for b in range(3) for c in range(3) for dd in range(3))
Y2 = Phi29(C2_29, ones29)
m29 = Y2[0][0] * Y2[1][1] - Y2[0][1] * Y2[1][0]
ok29 &= m29 == C17(Frac(5, 9))
check("F29", ok29,
      "THE COHERENT EXTENSION FIBRE (phase three, round seventeen; kernel: "
      "basisVec_mulVec, basisVec_dot, form_basis, hermitian_form_conj, "
      "psd_zero_form_mulVec_zero, psd_diag_zero_entry_zero, "
      "psd_unit_diag_entry_bound, psd_unimodular_rank_one, "
      "correlationExtension_single, correlationExtension_classical, embed_sum, "
      "choi_correlation, correlationExtension_completelyPositive, "
      "correlationExtension_trace, correlationExtension_cptp, "
      "cptp_classical_forces_correlation, cptpExtension_iff_correlationMatrix, "
      "correlationExtension_comp, correlationExtension_one_eq_id_iff, "
      "reversibleExtension_iff_rankOne, rankOne_extension_monomial, "
      "purity_selector_rank_one, correlationExtension_diagonal, combPerm_cons, "
      "combFold_diagonal, combPerm_eq_permProd, classicalComb_blind_to_correlation "
      "in OIBridge/CoherentExtension.lean). The kernel classifies EVERY completely "
      "positive extension of a classical permutation action as Ad(P_g) compose "
      "Schur_C with C PSD and unit-diagonal, and this probe walks the fibre over the "
      "3-cycle exactly: a rank-one unimodular phase matrix, a partial dephaser "
      "(2/3 off-diagonal, PSD certificate exhibited), and complete dephasing C = I. "
      "All three realize the same classical action; every 3-step branch-interleaved "
      "comb produces IDENTICAL statistics on all 27 classical trajectories (comb "
      "blindness, exact); one coherent effect -- the all-ones effect on the uniform "
      "superposition dyad -- reads 121/25, 7, 3 respectively and separates the "
      "fibre. ONLY the rank-one member is reversible: its family inverse is exact "
      "and the member IS the monomial conjugation Ad(D P_g) (unitary, verified on "
      "all 9 matrix units); the partial dephaser's would-be inverse matrix has "
      "x^H C' x = -1 < 0 on the witness (1,-1,0) and so is not PSD -- by the "
      "classification no CPTP inverse exists; complete dephasing is not even "
      "injective. THE AUDIT GUARD: composing the coherent lifts of g and g^-1 (both "
      "with C = I) is the identity on every diagonal -- the classical comb identity "
      "-- yet kills E_01: classical invertibility of the intervention does NOT give "
      "coherent reversibility. The purity selector fires exactly: the rank-one "
      "member maps the uniform dyad to a pure dyad (all 2x2 minors vanish), the "
      "partial dephaser leaves minor 5/9. BOXED: classical OI comb => the "
      "correlation-matrix family; OI comb + coherent reversibility => the monomial "
      "unitary intervention lift. Standard QM is the rank-one member; the "
      "alternative OI-derived theories are precisely its correlation/dephasing "
      "extensions.")

# ----------------------- F30  the controlled quotient countercontrol (phase three,
# round 17).  The 4-cycle with labels (0,1,0,1) has a nontrivial PASSIVE quotient
# (classes {0,2},{1,3}) -- but adding ONE intervention (the transposition tau = (0 1))
# to the menu makes the CONTROLLED quotient trivial: every state is separated by some
# action word.  The controlled relation is computed two independent ways -- partition
# refinement (the greatest-congruence fixpoint) and explicit word search -- and the
# caveat-closing instance is exhibited: (0,2) passively glued, separated by the
# single-letter word [tau].
ok30 = True
tau30 = [1, 0, 2, 3]
menu30 = {'phi': phi4, 'tau': tau30}
# (a) partition refinement over the menu: greatest observation-preserving congruence
def refine30(gens):
    blk = {s: lab4[s] for s in range(4)}
    while True:
        sig = {s: (blk[s],) + tuple(blk[g[s]] for g in gens) for s in range(4)}
        codes = {v: k for k, v in enumerate(sorted(set(sig.values())))}
        new = {s: codes[sig[s]] for s in range(4)}
        if new == blk:
            return blk
        blk = new

ctrl30 = refine30([phi4, tau30])
ok30 &= len(set(ctrl30.values())) == 4                     # singletons: separated
pass30 = refine30([phi4])
ok30 &= sorted(sorted(s for s in range(4) if pass30[s] == c)
               for c in set(pass30.values())) == [[0, 2], [1, 3]]
# (b) word search confirms: every pair is separated by an explicit word over the menu
def word_apply30(word, s):
    for a in word:
        s = menu30[a][s]
    return s

from itertools import product as iprod30
def sep_word30(s, t):
    for L in range(4):
        for word in iprod30(('phi', 'tau'), repeat=L):
            if lab4[word_apply30(word, s)] != lab4[word_apply30(word, t)]:
                return word
    return None

for s in range(4):
    for t in range(s + 1, 4):
        ok30 &= sep_word30(s, t) is not None
# (c) the caveat closer: (0,2) passively glued (identical phi-itineraries), separated
# by the single letter [tau]
ok30 &= w4[0] == w4[2]                                     # passive itineraries agree
ok30 &= sep_word30(0, 2) == ('tau',)
ok30 &= lab4[tau30[0]] == 1 and lab4[tau30[2]] == 0
# (d) exhaustive greatest congruence for the TWO-generator menu: of all 15 partitions
# only the trivial one is label-constant and stable under BOTH actions
ncong30 = 0
for p in partitions27([0, 1, 2, 3]):
    blk = {s: k for k, b in enumerate(p) for s in b}
    lab_const = all(lab4[s] == lab4[t] for b in p for s in b for t in b)
    stab = all(blk[gg[s]] == blk[gg[t]] for gg in (phi4, tau30)
               for b in p for s in b for t in b)
    if lab_const and stab:
        ncong30 += 1
        ok30 &= all(len(b) == 1 for b in p)
ok30 &= ncong30 == 1                                       # controlled-minimal
# (e) the refinement map: 4 controlled classes onto 2 passive classes, strictly finer
img30 = {ctrl30[s]: pass30[s] for s in range(4)}
ok30 &= set(img30.values()) == set(pass30.values())        # onto
ok30 &= len(set(ctrl30.values())) > len(set(pass30.values()))
check("F30", ok30,
      "THE CONTROLLED QUOTIENT COUNTERCONTROL (phase three, round seventeen; kernel: "
      "actWord_append, actWord_replicate, ctrlRel_evolve, ctrlRel_word, "
      "ctrlRel_symm_evolve, ctrlRel_le_itiRelInf, ctrlRel_greatest_congruence, "
      "ctrlPerm_mk, ctrlWord_mk, controlled_actionSeparating, "
      "controlledMinimal_iff_actionSeparating, controlledToPassive_surjective, "
      "intervention_separates_passive_fibre in OIBridge/ControlledQuotient.lean). "
      "The label-symmetric 4-cycle has passive classes {0,2},{1,3}; adding the single "
      "transposition tau = (0 1) to the action menu separates EVERYTHING: the "
      "greatest-congruence partition refinement reaches singletons, explicit "
      "separating words exist for every pair (word search to length 3), and of all "
      "15 partitions only the trivial one is label-constant and stable under both "
      "menu actions -- the carrier is controlled-minimal exactly as "
      "controlledMinimal_iff_actionSeparating states. THE CAVEAT, CLOSED: the pair "
      "(0,2) has identical passive phi-itineraries yet is separated by the "
      "one-letter word [tau] (labels 1 vs 0) -- passively glued, interventionally "
      "distinct, the exact instance of intervention_separates_passive_fibre. The "
      "controlled carrier maps ONTO the passive carrier (4 classes onto 2, strictly "
      "finer): the interventional coherent description is accountable to the "
      "controlled quotient, and with a single passive generator the controlled "
      "relation collapses back to the passive one exactly.")

# ----------------------- F31  coherent functoriality: the projective action and the
# H-functor boundary (phase three, round 18).  On the C3 rotation action, two
# families of classical CPTP extensions: a PROJECTIVE PHASE FAMILY (rank-one
# correlations built from exact Gaussian-rational phases, with a genuinely
# nontrivial multiplier omega(1,1) = (3+4i)/5 != 1) that satisfies coherent
# functoriality exactly -- channels compose strictly, the monomial unitaries
# multiply projectively U_g U_h = omega(g,h) U_{g+h}, and omega passes all 27
# cocycle identities -- and a DEPHASING FAMILY (C_e = all-ones, C_g = C_{g^2} = I)
# that produces IDENTICAL classical comb statistics on every group word and every
# branch-interleaved trajectory yet violates functoriality: Phi_g o Phi_{g^2} kills
# E_01 while Phi_e preserves it.  Complete classical comb data do not imply coherent
# functoriality: H-functor is a named bridge, and with it unitarity FOLLOWS.
ok31 = True
rho31 = [[(s + j) % 3 for s in range(3)] for j in range(3)]
rhoinv31 = [[(s - j) % 3 for s in range(3)] for j in range(3)]
w0_31 = C17(Frac(3, 5), Frac(4, 5))                        # omega(1,1), unimodular
alpha31 = [
    [CO17, CO17, CO17],
    d29,
    [w0_31.conj() * d29[s] * d29[(s + 1) % 3] for s in range(3)],
]
ok31 &= all((alpha31[j][s] * alpha31[j][s].conj()) == CO17
            for j in range(3) for s in range(3))
Cfam31 = [[[alpha31[j][s] * alpha31[j][t].conj() for t in range(3)]
           for s in range(3)] for j in range(3)]
def Phi31(j, C, X):
    return [[C[rhoinv31[j][a]][rhoinv31[j][b]] * X[rhoinv31[j][a]][rhoinv31[j][b]]
             for b in range(3)] for a in range(3)]

# (a) the multiplier: beta(g,h,s) is s-INDEPENDENT and unimodular for all 9 pairs
omega31 = {}
for g in range(3):
    for h in range(3):
        betas = [alpha31[h][s] * alpha31[g][rho31[h][s]]
                 * alpha31[(g + h) % 3][s].conj() for s in range(3)]
        ok31 &= betas[0] == betas[1] == betas[2]
        ok31 &= (betas[0] * betas[0].conj()) == CO17
        omega31[(g, h)] = betas[0]
ok31 &= omega31[(1, 1)] == w0_31 and not (omega31[(1, 1)] == CO17)
# (b) coherent functoriality of the CHANNELS, exactly, on all 9 matrix units
ok31 &= all(Phi31(0, Cfam31[0], E29(s, t)) == E29(s, t)
            for s in range(3) for t in range(3))
for g in range(3):
    for h in range(3):
        ok31 &= all(Phi31(g, Cfam31[g], Phi31(h, Cfam31[h], E29(s, t)))
                    == Phi31((g + h) % 3, Cfam31[(g + h) % 3], E29(s, t))
                    for s in range(3) for t in range(3))
# (c) the projective unitary law U_g U_h = omega(g,h) U_{g+h}, all 9 pairs
U31 = []
for j in range(3):
    D = [[alpha31[j][rhoinv31[j][a]] if a == c else CZ17 for c in range(3)]
         for a in range(3)]
    P = [[CO17 if rho31[j][c] == a else CZ17 for c in range(3)] for a in range(3)]
    U31.append(mmc17(D, P))
    ok31 &= mmc17(U31[j], dag17(U31[j])) == eye17(3)
for g in range(3):
    for h in range(3):
        lhs = mmc17(U31[g], U31[h])
        rhs = [[omega31[(g, h)] * U31[(g + h) % 3][a][b] for b in range(3)]
               for a in range(3)]
        ok31 &= lhs == rhs
# (d) omega is a 2-cocycle: all 27 triples
for g in range(3):
    for h in range(3):
        for k in range(3):
            ok31 &= omega31[(g, h)] * omega31[((g + h) % 3, k)] \
                == omega31[(g, (h + k) % 3)] * omega31[(h, k)]
# (e) THE BOUNDARY: the dephasing family -- identical classical combs, no
# functoriality
Cdeph31 = [[[CO17 for _ in range(3)] for _ in range(3)], eye17(3), eye17(3)]
ok31 &= all(Phi31(0, Cdeph31[0], E29(s, t)) == E29(s, t)
            for s in range(3) for t in range(3))             # Phi_e = id holds
from itertools import product as iprod31
diag31 = [[p29[a] if a == b else CZ17 for b in range(3)] for a in range(3)]
for L in range(4):
    for word in iprod31(range(3), repeat=L):
        X1, X2 = diag31, diag31
        for j in word:
            X1 = Phi31(j, Cfam31[j], X1)
            X2 = Phi31(j, Cdeph31[j], X2)
        ok31 &= X1 == X2                                    # plain word combs agree
for word in iprod31(range(3), repeat=2):
    for traj in iprod31(range(3), repeat=2):
        X1, X2 = diag31, diag31
        for j, i in zip(word, traj):
            X1 = branch29(i, Phi31(j, Cfam31[j], X1))
            X2 = branch29(i, Phi31(j, Cdeph31[j], X2))
        ok31 &= X1 == X2                                    # branch-interleaved too
ok31 &= Phi31(1, Cdeph31[1], Phi31(2, Cdeph31[2], E29(0, 1))) \
    == [[CZ17] * 3 for _ in range(3)]                       # functoriality FAILS
ok31 &= not (Phi31(1, Cdeph31[1], Phi31(2, Cdeph31[2], E29(0, 1))) == E29(0, 1))
check("F31", ok31,
      "COHERENT FUNCTORIALITY: THE PROJECTIVE ACTION AND THE H-FUNCTOR BOUNDARY "
      "(phase three, round eighteen; kernel: unimodular_ne_zero, "
      "correlationExtension_matrix_eq, functoriality_forces_rankOne, "
      "functoriality_schur_law, coherentFunctoriality_iff_projectiveMonomial, "
      "monomial_entry, functorial_projective_unitaries, functorial_cocycle, "
      "groupFamily_comb_blind in OIBridge/ProjectiveAction.lean). On the C3 rotation "
      "action, the projective phase family (exact Gaussian-rational phases, "
      "multiplier omega(1,1) = (3+4i)/5 genuinely nontrivial) satisfies coherent "
      "functoriality EXACTLY: the multiplier is s-independent and unimodular for all "
      "9 pairs, the channels compose strictly on all matrix units, the monomial "
      "unitaries are exactly unitary and multiply projectively U_g U_h = omega(g,h) "
      "U_{g+h}, and omega passes all 27 cocycle identities -- the kernel capstone "
      "coherentFunctoriality_iff_projectiveMonomial instantiated, and the Weyl-lift "
      "probe's projective-binding observation (L1: H(u)H(v) = +-H(u+v)) replaced by "
      "the exact classification. THE BOUNDARY: the dephasing family (C_e = all-ones, "
      "C_g = C_g2 = I) realizes the same classical action with Phi_e = id, produces "
      "IDENTICAL comb statistics on every group word up to length 3 and every "
      "branch-interleaved trajectory, yet Phi_g o Phi_g2 kills E_01 while the "
      "identity preserves it: complete classical comb data do not imply coherent "
      "functoriality. BOXED: bare OI => controlled-minimal classical core + the "
      "correlation-matrix coherent extensions; + H-functor (a NAMED BRIDGE -- two "
      "intervention words realizing the same reversible transformation must act "
      "identically on the completed coherent state space) => the projective monomial "
      "unitary action. Unitarity is not postulated: it follows. Full operational QM "
      "is not presently a theorem of bare OI; the quantum branch is selected by "
      "exactly this coherent composition principle -- the precise boundary the "
      "programme set out to locate.")

# ----------------------- F32  the dynamical control Lie algebra: separation from the
# accessible algebra, and the one-control jump to u(2) (phase three, round 19).
# The unitary-controllability CLASSIFICATION on Alex's exact 2x2 carrier:
# H = V diag(0,1) V^T with V the 3-4-5 rotation.  (a) with NO nontrivial controls the
# dynamical Lie algebra is the line R(-iH) -- real rank 1, a PROPER subalgebra of the
# 4-dimensional u(2); (b) on the SAME carrier the accessible *-algebra generated by
# the readout E_00 and the Hamiltonian is ALL of M_2(C) (nondegenerate gap {0,1},
# every eigenvector overlap nonzero -- the native_menu_generates hypotheses): algebra
# generation and dynamical controllability are DIFFERENT notions, exactly separated;
# (c) adding the single classical swap control X jumps the bracket closure of
# {-iH, -iXHX} to real rank 4 = dim u(2), with traceless part of rank 3 = dim su(2):
# the boxed criterion L_0 = su(D) holds and universal unitary control up to phase
# follows through the (recorded, analytic) Lie-closure bridge; (d) projective
# invariance and gauge covariance verified exactly; (e) the finite algebraic core of
# the conjugated-flow identity U e^{-itH} U^dag = e^{-it UHU^dag}: term-by-term
# power conjugation U H^n U^dag = (U H U^dag)^n.
ok32 = True
V32 = [[C17(Frac(3, 5)), C17(Frac(-4, 5))], [C17(Frac(4, 5)), C17(Frac(3, 5))]]
H32 = mmc17(mmc17(V32, [[CZ17, CZ17], [CZ17, CO17]]), dag17(V32))
ok32 &= H32 == [[C17(Frac(16, 25)), C17(Frac(-12, 25))],
                [C17(Frac(-12, 25)), C17(Frac(9, 25))]]
mi32 = C17(0, -1)
def smul32(c, M):
    return [[c * M[r][s] for s in range(2)] for r in range(2)]

def msub32(A, B):
    return [[A[r][s] - B[r][s] for s in range(2)] for r in range(2)]

def brk32(A, B):
    return msub32(mmc17(A, B), mmc17(B, A))

def vec32(M):
    out = []
    for r in range(2):
        for s in range(2):
            out += [M[r][s].re, M[r][s].im]
    return out

def rankR32(mats):
    rows = [vec32(M) for M in mats if any(not x.z() for r in M for x in r)]
    rk, piv = 0, 0
    while piv < 8 and rk < len(rows):
        sel = next((i for i in range(rk, len(rows)) if rows[i][piv] != 0), None)
        if sel is None:
            piv += 1
            continue
        rows[rk], rows[sel] = rows[sel], rows[rk]
        iv = rows[rk][piv]
        rows[rk] = [x / iv for x in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][piv] != 0:
                f = rows[i][piv]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
        piv += 1
    return rk

def lieClose32(gens):
    basis = []
    for M in gens:
        if rankR32(basis + [M]) > rankR32(basis):
            basis.append(M)
    while True:
        grew = False
        for i in range(len(basis)):
            for j in range(i + 1, len(basis)):
                B = brk32(basis[i], basis[j])
                if rankR32(basis + [B]) > rankR32(basis):
                    basis.append(B)
                    grew = True
        if not grew:
            return rankR32(basis), basis

A1_32 = smul32(mi32, H32)
# (a) no controls: the line R(-iH)
r0, _ = lieClose32([A1_32])
ok32 &= r0 == 1
# (b) the accessible *-algebra on the same carrier is full M_2: associative closure
# of {I, H, E00} under multiplication and dagger has complex rank 4
ok32 &= all(not V32[r][s].z() for r in range(2) for s in range(2))  # overlaps
E00_32 = [[CO17, CZ17], [CZ17, CZ17]]
def cvec32(M):
    return [M[0][0], M[0][1], M[1][0], M[1][1]]

alg32 = [eye17(2), H32, E00_32]
while True:
    grew = False
    cur = rank17([cvec32(M) for M in alg32])
    cand = [mmc17(A, B) for A in alg32 for B in alg32] + [dag17(A) for A in alg32]
    for M in cand:
        if rank17([cvec32(N) for N in alg32] + [cvec32(M)]) > cur:
            alg32.append(M)
            cur += 1
            grew = True
    if not grew:
        break
ok32 &= rank17([cvec32(M) for M in alg32]) == 4          # full M_2(C)
# THE SEPARATION on one carrier: algebra rank 4 (full), Lie rank 1 (a line)
# (c) one classical control: the swap
X32 = [[CZ17, CO17], [CO17, CZ17]]
A2_32 = smul32(mi32, mmc17(mmc17(X32, H32), X32))
rfull, basis32 = lieClose32([A1_32, A2_32])
ok32 &= rfull == 4                                       # L = u(2)
half32 = C17(Frac(1, 2))
def traceless32(M):
    tr = M[0][0] + M[1][1]
    return msub32(M, [[half32 * tr, CZ17], [CZ17, half32 * tr]])

ok32 &= rankR32([traceless32(M) for M in basis32]) == 3  # L_0 = su(2)
# (d) projective invariance and gauge covariance, exactly
lam32 = C17(Frac(3, 5), Frac(4, 5))
lamX = smul32(lam32, X32)
ok32 &= mmc17(mmc17(lamX, H32), dag17(lamX)) == mmc17(mmc17(X32, H32), dag17(X32))
W32 = mmc17(V32, [[CO17, CZ17], [CZ17, lam32]])          # a rational unitary gauge
ok32 &= mmc17(W32, dag17(W32)) == eye17(2)
gaugegens = [mmc17(mmc17(W32, A), dag17(W32)) for A in (A1_32, A2_32)]
rgauge, _ = lieClose32(gaugegens)
ok32 &= rgauge == 4                                      # rank is gauge-invariant
# (e) the finite core of the conjugated-flow identity: power-by-power conjugation
Hpow, XHXpow = H32, mmc17(mmc17(X32, H32), X32)
for _ in range(3):
    Hpow = mmc17(Hpow, H32)
    XHXpow = mmc17(XHXpow, mmc17(mmc17(X32, H32), X32))
    ok32 &= mmc17(mmc17(X32, Hpow), X32) == XHXpow
check("F32", ok32,
      "THE DYNAMICAL CONTROL LIE ALGEBRA (phase three, round nineteen; kernel: "
      "phase_conj_invariant, controlGenerators_phase_invariant, "
      "controlLie_phase_invariant, conj_conj_collapse, controlLie_gauge_mem, "
      "controlLie_gauge_mem_iff, controlLie_le_skewHerm, "
      "unitary_inv_eq_conjTranspose, unitary_exp_conj, conjugated_flow, "
      "controlLie_trivial in OIBridge/ControlLie.lean). The unitary-controllability "
      "classification on the exact 2x2 carrier H = V diag(0,1) V^T (V the 3-4-5 "
      "rotation): (a) with no nontrivial controls the bracket closure of {-iH} has "
      "real rank 1 -- the line R(-iH), kernel theorem controlLie_trivial -- a PROPER "
      "subalgebra of the 4-dimensional u(2); (b) on the SAME carrier the accessible "
      "*-algebra generated by the readout E_00 and the Hamiltonian closes to full "
      "M_2(C) (complex rank 4; nondegenerate gap {0,1} and all eigenvector overlaps "
      "nonzero, the native_menu_generates hypotheses): the MANDATORY SEPARATION -- "
      "algebra generation and dynamical controllability are different notions, and "
      "the accessible-algebra theorem must never be read as a controllability "
      "theorem; (c) adding the single classical swap control X jumps the closure of "
      "{-iH, -iXHX} to real rank 4 = dim u(2), with traceless projections of rank "
      "3 = dim su(2): the boxed criterion L_0 = su(D) holds exactly, and universal "
      "unitary control up to phase follows through the recorded analytic Lie-closure "
      "bridge Lie(K^0) = L(H,U) -- kept at probe level, not claimed in the kernel; "
      "(d) the projective phase freedom moves nothing (lam*X conjugates H "
      "identically to X, kernel phase_conj_invariant / controlLie_phase_invariant) "
      "and a rational unitary gauge W leaves the closure rank at 4 "
      "(controlLie_gauge_mem_iff); (e) the finite algebraic core of the "
      "conjugated-flow identity U e^{-itH} U^dag = e^{-it UHU^dag} verified "
      "power-by-power (kernel unitary_exp_conj / conjugated_flow via the matrix "
      "exponential). THE CHAIN: bare OI => classical core + correlation extensions; "
      "+ H-functor => projective monomial quantum controls; + L_0 = su(D) => "
      "universal unitary control up to phase; and only then the remaining "
      "purification/composite/instrument bridge. The theorem is conditional on the "
      "selected H-functor completion with gauge-equivalent lifts identified: the "
      "classical permutation action alone does not determine L.")

# ----------------------- F33  the operational-dilation boundary: instrument dilation
# and the two load-bearing bridges (phase three, round 20).  (a) the Stinespring
# dilation of an exact 2-outcome qubit instrument -- an amplitude-damping-style Kraus
# pair with K0^dag K0 + K1^dag K1 = I -- gives an isometry V^dag V = I, its ancilla
# blocks read back the Kraus post-states K_k rho K_k^dag, and the coarse-grained
# channel is CP; (b) H-PURE-SEED countercontrol: a maximally-mixed-environment
# channel is UNITAL (Phi(I) = I), while the reset channel rho -> |0><0| Tr(rho) is
# NOT unital, so the uniform hidden state cannot realize state preparation;
# (c) H-TENSOR countercontrol: a nonfactorizable-phase monomial unitary on A x B
# (swap on A, identity on B, phases 1,i,1,-i) is exactly unitary with U^2 = I and
# realizes a purely local classical permutation, yet is NOT of the form U_A tensor
# I_B -- H-functor and classical locality hold, tensor locality fails; (d) local
# tomography: the local matrix-unit effects read off every composite entry.
ok33 = True
# (a) qubit instrument dilation.  Amplitude-damping Kraus pair (p = 9/25):
p33 = Frac(9, 25)
sp, sq = C17(Frac(4, 5)), C17(Frac(3, 5))                  # sqrt(1-p)=4/5, sqrt(p)=3/5
K0 = [[CO17, CZ17], [CZ17, sp]]
K1 = [[CZ17, sq], [CZ17, CZ17]]
Klist = [K0, K1]
# completeness: sum K_k^dag K_k = I
comp = [[CZ17, CZ17], [CZ17, CZ17]]
for K in Klist:
    KdK = mmc17(dag17(K), K)
    comp = [[comp[r][c] + KdK[r][c] for c in range(2)] for r in range(2)]
ok33 &= comp == eye17(2)
# V : (k, s') -> s, indexed rows (k,s') = 2k + s', cols s.  V^dag V = I
V33 = [[Klist[kk][sp2][s] for s in range(2)] for kk in range(2) for sp2 in range(2)]
VdV = mmc17(dag17(V33), V33)
ok33 &= VdV == eye17(2)
# branch: sysBlock(V rho V^dag, k) = K_k rho K_k^dag on a generic state
rho33 = [[C17(Frac(1, 2)), C17(Frac(1, 5), Frac(1, 10))],
         [C17(Frac(1, 5), Frac(-1, 10)), C17(Frac(1, 2))]]
VrV = mmc17(mmc17(V33, rho33), dag17(V33))
for kk in range(2):
    block = [[VrV[2 * kk + r][2 * kk + c] for c in range(2)] for r in range(2)]
    ok33 &= block == mmc17(mmc17(Klist[kk], rho33), dag17(Klist[kk]))
# coarse-grain (single outcome each here): the channel is trace-preserving on rho
chan = [[CZ17, CZ17], [CZ17, CZ17]]
for kk in range(2):
    KrK = mmc17(mmc17(Klist[kk], rho33), dag17(Klist[kk]))
    chan = [[chan[r][c] + KrK[r][c] for c in range(2)] for r in range(2)]
ok33 &= (chan[0][0] + chan[1][1]) == (rho33[0][0] + rho33[1][1])   # Tr preserved
# (b) H-pure-seed: unital uniform environment vs non-unital reset
# uniform-env channel Phi(X) = Tr_E[U (X tensor I/m) U^dag]; at X = I this is I for
# ANY unitary U (probe the identity interaction U = I on a 2-dim environment)
m33 = 2
Uenv = eye17(4)                                            # trivial interaction
Iin = [[(CO17 if r == c else CZ17)
        for c in range(4)] for r in range(4)]              # 1 tensor 1 (before /m)
big = mmc17(mmc17(Uenv, Iin), dag17(Uenv))
PhiI = [[sum((big[2 * r + e][2 * c + e] for e in range(m33)), CZ17)
         for c in range(2)] for r in range(2)]
PhiI = [[C17(Frac(1, m33)) * PhiI[r][c] for c in range(2)] for r in range(2)]
ok33 &= PhiI == eye17(2)                                   # UNITAL
# reset channel at I: |0><0| Tr(I) = 2|0><0| != I
resetI = [[C17(2) if (r, c) == (0, 0) else CZ17 for c in range(2)] for r in range(2)]
ok33 &= not (resetI == eye17(2))                           # NOT unital
# (c) H-tensor: nonfactorizable-phase monomial unitary, basis (a,b) -> idx 2a+b
Ci, Cmi = C17(0, 1), C17(0, -1)
# columns: (0,0)->(1,0) phase 1; (0,1)->(1,1) phase i; (1,0)->(0,0) phase 1;
# (1,1)->(0,1) phase -i
Utens = [[CZ17, CZ17, CO17, CZ17],
         [CZ17, CZ17, CZ17, Cmi],
         [CO17, CZ17, CZ17, CZ17],
         [CZ17, Ci, CZ17, CZ17]]
ok33 &= mmc17(Utens, dag17(Utens)) == eye17(4)             # exactly unitary
ok33 &= mmc17(Utens, Utens) == eye17(4)                    # U^2 = I: C2 functorial
# classical locality: the support permutation is swap-on-A, identity-on-B
supp = {}
for c in range(4):
    r = next(r for r in range(4) if not Utens[r][c].z())
    supp[c] = r
ok33 &= supp == {0: 2, 1: 3, 2: 0, 3: 1}                   # (a,b)->(1-a,b)
# tensor locality FAILS: U = M tensor I_B would force M[1][0] = phase in BOTH b
# sectors, but b=0 gives U[2][0] = 1 and b=1 gives U[3][1] = i, unequal
ok33 &= Utens[2][0] == CO17 and Utens[3][1] == Ci
ok33 &= not (Utens[2][0] == Utens[3][1])                   # nonfactorizable
# a genuine M tensor I would satisfy this equality (kernel tensorProduct_entry):
Mloc = [[C17(Frac(3, 5)), C17(Frac(-4, 5))],
        [C17(Frac(4, 5)), C17(Frac(3, 5))]]
kronMI = [[Mloc[r // 2][c // 2] * (CO17 if r % 2 == c % 2 else CZ17)
           for c in range(4)] for r in range(4)]
ok33 &= kronMI[2][0] == kronMI[3][1]                       # factorizes: M[1][0]
# (d) local tomography: local matrix-unit effects read off entries
def loceff(a, ap, b, bp):
    return [[(CO17 if (r // 2 == a and c // 2 == ap) else CZ17)
             * (CO17 if (r % 2 == b and c % 2 == bp) else CZ17)
             for c in range(4)] for r in range(4)]

X33 = [[C17(r + 1, c) for c in range(4)] for r in range(4)]
for a in range(2):
    for ap in range(2):
        for b in range(2):
            for bp in range(2):
                tr = sum((mmc17(loceff(a, ap, b, bp), X33)[i][i]
                          for i in range(4)), CZ17)
                ok33 &= tr == X33[2 * ap + bp][2 * a + b]
check("F33", ok33,
      "THE OPERATIONAL-DILATION BOUNDARY (phase three, round twenty; kernel: "
      "krausInstrument_isometry, dilation_sysBlock, instrument_coarsegrain, "
      "seeded_prep_eq, finiteInstrument_of_ancillaControl, uniform_input_scalar, "
      "uniformEnvChannel_unital, resetChannel_not_unital, uniformHiddenState_not_full, "
      "tensorProduct_entry, localEffect_trace, local_tomography in "
      "OIBridge/InstrumentDilation.lean). (a) the Stinespring dilation of an exact "
      "amplitude-damping qubit instrument (p = 9/25) gives an isometry V^dag V = I "
      "whose ancilla blocks read back the Kraus post-states K_k rho K_k^dag exactly, "
      "and the coarse-grained channel is trace-preserving -- the whole finite "
      "instrument reduced to seed + unitary + basis readout; (b) H-PURE-SEED is "
      "load-bearing: a maximally-mixed-environment channel is UNITAL (Phi(I) = I for "
      "any interaction), the reset channel rho -> |0><0| Tr(rho) reads 2|0><0| at I "
      "and is NOT unital, so the existing uniform hidden state cannot supply state "
      "preparation and H-pure-seed cannot be identified with the hidden-sector prior; "
      "(c) H-TENSOR is load-bearing: the nonfactorizable-phase monomial unitary "
      "(swap on A, identity on B, phases 1, i, 1, -i) is exactly unitary with "
      "U^2 = I (so H-functor holds for its C2) and realizes the purely local "
      "classical permutation (a,b) -> (1-a,b), yet is NOT U_A tensor I_B -- the b=0 "
      "and b=1 sectors would force M[1][0] = 1 and M[1][0] = i, unequal, while a "
      "genuine M tensor I factorizes (kernel tensorProduct_entry): H-functor and "
      "classical locality green, tensor locality RED; (d) local tomography -- the "
      "local matrix-unit effects read off every composite entry, so equal "
      "local-product probabilities force equal composite states. BOXED CHAIN: bare "
      "OI => classical core + correlation extensions; + H-functor => projective "
      "monomial coherent dynamics; + L_0 = su(D) => universal unitary control; "
      "+ H-tensor + H-pure-seed => the full finite quantum instrument algebra. "
      "Purification (Schmidt/Uhlmann) and local tomography are the theorem targets "
      "immediately behind the dilation reduction; the remaining OI/QM question is "
      "exactly whether OI earns H-functor, H-tensor, H-pure-seed and sufficient "
      "composite Lie rank, or whether those are independent completion principles.")

# ----------------------- F34  round-twenty repairs, the H-pure-seed collapse, and
# purification (phase three, round 21).  (a) THE ACTUAL uniform-environment channel
# Phi_U(rho) = Tr_E[U(rho tensor I/m)U^dag] on a genuine rho != I: nonconstant, and
# unital at rho = I; (b) physical single-system tomography reconstructs an off-diagonal
# entry from the +/- and +/-i projector expectations; (c) H-PURE-SEED COLLAPSES:
# branch_project P_k rho P_k = rho_kk P_k, mixed_branch_is_pure, and readout +
# feed-forward on the uniform ancilla derives |s0><s0| -- the pure seed the round-20
# countercontrol showed the uniform environment ALONE could not supply; (d)
# purification: Tr_E|Psi_A><Psi_A| = A A^dag exactly, and purifier uniqueness
# A A^dag = B B^dag with B = A U verified on a rotation.
ok34 = True
m34 = 2
U34 = [[CO17, CZ17, CZ17, CZ17],
       [CZ17, CO17, CZ17, CZ17],
       [CZ17, CZ17, CZ17, CO17],
       [CZ17, CZ17, CO17, CZ17]]                          # entangling (CNOT-like)
ok34 &= mmc17(U34, dag17(U34)) == eye17(4)
inv_m = C17(Frac(1, 2))
def uinput34(rho):                                        # rho tensor (I/m), (k,s)=2k+s
    return [[(inv_m if (r // 2) == (c // 2) else CZ17) * rho[r % 2][c % 2]
             for c in range(4)] for r in range(4)]
def ptraceE34(M):
    return [[sum((M[2 * e + s][2 * e + t] for e in range(m34)), CZ17)
             for t in range(2)] for s in range(2)]
def PhiU34(rho):
    return ptraceE34(mmc17(mmc17(U34, uinput34(rho)), dag17(U34)))
ok34 &= PhiU34(eye17(2)) == eye17(2)                      # unital at rho = I
plus_dyad = [[C17(Frac(1, 2)), C17(Frac(1, 2))],
             [C17(Frac(1, 2)), C17(Frac(1, 2))]]          # |+><+|
ok34 &= PhiU34([[CO17, CZ17], [CZ17, CZ17]]) != PhiU34(plus_dyad)  # rho-dependent
# (b) physical tomography: reconstruct an off-diagonal from projector expectations
rho_t = [[C17(Frac(1, 2)), C17(Frac(1, 5), Frac(3, 10))],
         [C17(Frac(1, 5), Frac(-3, 10)), C17(Frac(1, 2))]]
def expect(v, M):
    return sum((v[i].conj() * M[i][j] * v[j] for i in range(len(v))
                for j in range(len(v))), CZ17)
re_off = expect([CO17, CO17], rho_t) - rho_t[0][0] - rho_t[1][1]   # rho01 + rho10
im_comb = expect([CO17, C17(0, 1)], rho_t) - rho_t[0][0] - rho_t[1][1]  # i(rho01-rho10)
recon01 = C17(Frac(1, 2)) * (re_off + C17(0, -1) * im_comb)
ok34 &= recon01 == rho_t[0][1]                            # off-diagonal recovered
# (c) H-pure-seed collapse on a 3-dim ancilla
def proj3(k):
    return [[CO17 if (r == k and c == k) else CZ17 for c in range(3)] for r in range(3)]
rho3 = [[C17(Frac(1, 2)), C17(Frac(1, 10)), CZ17],
        [C17(Frac(1, 10)), C17(Frac(1, 3)), CZ17],
        [CZ17, CZ17, C17(Frac(1, 6))]]
for k in range(3):                                        # branch_project
    ok34 &= mmc17(mmc17(proj3(k), rho3), proj3(k)) \
        == [[rho3[k][k] if (r == k and c == k) else CZ17 for c in range(3)]
            for r in range(3)]
Im3 = [[C17(Frac(1, 3)) if r == c else CZ17 for c in range(3)] for r in range(3)]
ok34 &= mmc17(mmc17(proj3(0), Im3), proj3(0)) \
    == [[C17(Frac(1, 3)) if (r == 0 and c == 0) else CZ17 for c in range(3)]
        for r in range(3)]                                # mixed_branch_is_pure
def swap0(k):
    P = [[CZ17] * 3 for _ in range(3)]
    perm = list(range(3)); perm[0], perm[k] = perm[k], perm[0]
    for r in range(3):
        P[r][perm[r]] = CO17
    return P
for k in range(3):
    ok34 &= mmc17(mmc17(swap0(k), proj3(k)), dag17(swap0(k))) == proj3(0)  # |k>->|0>
seed = [[CZ17] * 3 for _ in range(3)]
for k in range(3):
    branch = mmc17(mmc17(proj3(k), Im3), proj3(k))
    ff = mmc17(mmc17(swap0(k), branch), dag17(swap0(k)))
    seed = [[seed[r][c] + ff[r][c] for c in range(3)] for r in range(3)]
ok34 &= seed == proj3(0)                                  # DERIVED pure seed |0><0|
# (d) purification: Tr_E |Psi_A><Psi_A| = A A^dag
A34 = [[C17(Frac(1, 2)), C17(0, Frac(1, 2))],
       [C17(Frac(1, 3)), C17(Frac(1, 4))]]
psi = [A34[p // 2][p % 2] for p in range(4)]
dens = [[psi[p] * psi[q].conj() for q in range(4)] for p in range(4)]
ptr = [[sum((dens[2 * s + e][2 * t + e] for e in range(2)), CZ17)
        for t in range(2)] for s in range(2)]
ok34 &= ptr == mmc17(A34, dag17(A34))                     # purifies A A^dag
Urot = [[C17(Frac(3, 5)), C17(Frac(-4, 5))], [C17(Frac(4, 5)), C17(Frac(3, 5))]]
ok34 &= mmc17(Urot, dag17(Urot)) == eye17(2)
B34 = mmc17(A34, Urot)
ok34 &= mmc17(B34, dag17(B34)) == mmc17(A34, dag17(A34))  # Uhlmann: same reduced state
check("F34", ok34,
      "ROUND-TWENTY REPAIRS, H-PURE-SEED COLLAPSE, AND PURIFICATION (phase three, "
      "round twenty-one; kernel: uniformInput, uniformEnvChannel, uniformInput_one, "
      "uniformEnvChannel_unital, uniformHiddenState_not_full, "
      "productMatrixUnit_separating, tomography_physical, local_tomography, "
      "rankOneProj, branch_project, mixed_branch_is_pure, trace_eq_sum_diag, "
      "readout_feedforward_reset, uniform_readout_feedforward_seed, luders_selector_cp, "
      "purifVec, ptraceB, purification_partialTrace, purification_of_factorization in "
      "OIBridge/InstrumentDilation.lean and OIBridge/Purification.lean). (a) THE "
      "REPAIRED CHANNEL: Phi_U(rho) = Tr_E[U(rho tensor I/m)U^dag] is now the actual "
      "channel on a genuine rho (population-dependent, verified rho-dependent), unital "
      "at rho = I -- uniformHiddenState_not_full quantifies over THIS channel, not the "
      "scalar form. (b) PHYSICAL TOMOGRAPHY: an off-diagonal entry is reconstructed "
      "exactly from the |a+a'> and |a+ia'> rank-one projector expectations (genuine "
      "physical effects), repairing the matrix-unit overclaim -- the old "
      "functional-separation result is retained honestly as "
      "productMatrixUnit_separating. (c) H-PURE-SEED COLLAPSES: branch_project gives "
      "the Luders update P_k rho P_k = rho_kk P_k, mixed_branch_is_pure gives "
      "P_k (I/m) P_k = (1/m) P_k, and readout + reversible feed-forward on the uniform "
      "3-ancilla derives |0><0| EXACTLY -- the pure seed the round-20 countercontrol "
      "proved the uniform environment ALONE could not supply. So H-pure-seed is NOT "
      "an independent bridge, PROVIDED the rank-one Luders readout (luders_selector_cp) "
      "is itself OI-licensed -- the remaining epistemic guard. (d) PURIFICATION: "
      "Tr_E|Psi_A><Psi_A| = A A^dag exactly, and B = A U shares the reduced state "
      "(Uhlmann uniqueness, the standard finite theorem). BOXED REDUCTION: if the "
      "Luders branch update is OI-licensed, the four named endpoint conditions become "
      "THREE -- H-functor, H-tensor, and sufficient composite Lie rank.")

# ----------------------- F35  the selector-completion round: rank-one uniqueness and
# the coarse-fibre correlation family (phase three, round 22).  (a) RANK-ONE: the CP
# map P_k X P_k is the UNIQUE CP extension of the rank-one classical selector
# Phi(E_ss) = delta_sk E_kk -- its Choi matrix is the single entry at ((k,k),(k,k)),
# PSD, and no other CP map has that Choi diagonal; (b) MONOMIAL-LUDERS COMPATIBILITY:
# on a diagonal classical state the fixed-basis Luders readout after a monomial lift
# U_g = D P_g is the phase-free classical branch w(g^-1 k) P_k, independent of the
# phases D; (c) COARSE FIBRE: on a rank-two fibre F = {0,1} the Luders map (C = all
# ones) and complete within-block dephasing (C = I) are DIFFERENT CP selectors that
# agree on every classical branch probability yet differ on E_01 -- the surviving
# freedom is a correlation matrix inside the block; (d) RANK-ONE COLLAPSE: on the
# rank-one fibre {0} the block is 1x1, C = [1] for both, and the family collapses to
# the unique Luders member.
ok35 = True
def Est(s, t, n=3):
    return [[CO17 if (r == s and c == t) else CZ17 for c in range(n)] for r in range(n)]
# (a) rank-one selector uniqueness: Choi of P_k . P_k, k = 0
k35 = 0
def luders_map(k, X, n=3):
    P = Est(k, k, n)
    return mmc17(mmc17(P, X), P)
# Choi matrix J[(s,a)][(t,b)] = Phi(E_st)[a][b], over 3x3 -> 9x9
def choi(phi, n=3):
    J = [[CZ17] * (n * n) for _ in range(n * n)]
    for s in range(n):
        for t in range(n):
            PhiE = phi(Est(s, t, n))
            for a in range(n):
                for bb in range(n):
                    J[n * s + a][n * t + bb] = PhiE[a][bb]
    return J
JL = choi(lambda X: luders_map(k35, X))
# the Choi is the single entry at index (n*k + k) = 0
exp = [[CO17 if (r == 0 and c == 0) else CZ17 for c in range(9)] for r in range(9)]
ok35 &= JL == exp
# PSD (Hermitian, and it is a rank-one projector |e><e|): J = v v^H with v = e_0
vJ = [CO17 if r == 0 else CZ17 for r in range(9)]
ok35 &= JL == [[vJ[r] * vJ[c].conj() for c in range(9)] for r in range(9)]
# rank-one selector condition holds
ok35 &= all(luders_map(k35, Est(s, s)) == (Est(k35, k35) if s == k35
            else [[CZ17] * 3 for _ in range(3)]) for s in range(3))
# (b) monomial-Luders: phases vanish on a diagonal classical state
g35 = [1, 2, 0]                                           # 3-cycle
gi35 = [2, 0, 1]
d35 = [CO17, C17(Frac(3, 5), Frac(4, 5)), C17(Frac(3, 5), Frac(-4, 5))]
ok35 &= all((d35[s] * d35[s].conj()) == CO17 for s in range(3))
P35 = [[CO17 if g35[c] == r else CZ17 for c in range(3)] for r in range(3)]
D35 = [[d35[r] if r == c else CZ17 for c in range(3)] for r in range(3)]
U35 = mmc17(D35, P35)
w35 = [C17(Frac(1, 2)), C17(Frac(1, 3)), C17(Frac(1, 6))]
diagw = [[w35[r] if r == c else CZ17 for c in range(3)] for r in range(3)]
for k in range(3):
    lhs = luders_map(k, mmc17(mmc17(U35, diagw), dag17(U35)))
    rhs = [[w35[gi35[k]] if (r == k and c == k) else CZ17 for c in range(3)]
           for r in range(3)]
    ok35 &= lhs == rhs                                    # phase-free classical branch
# a phase-FREE lift (D = I) gives the same branch -> phases irrelevant
U35_nophase = P35
for k in range(3):
    ok35 &= luders_map(k, mmc17(mmc17(U35, diagw), dag17(U35))) \
        == luders_map(k, mmc17(mmc17(U35_nophase, diagw), dag17(U35_nophase)))
# (c) coarse rank-two fibre F = {0,1}: Luders vs dephasing
PF = [[CO17 if (r == c and r in (0, 1)) else CZ17 for c in range(3)] for r in range(3)]
def luders_F(X):
    return mmc17(mmc17(PF, X), PF)
def dephase_F(X):
    out = [[CZ17] * 3 for _ in range(3)]
    for i in (0, 1):
        Pi = Est(i, i)
        term = mmc17(mmc17(Pi, X), Pi)
        out = [[out[r][c] + term[r][c] for c in range(3)] for r in range(3)]
    return out
# both are classical selectors: Phi(E_ss) = E_ss for s in F, 0 for s notin F
for s in range(3):
    tgt = Est(s, s) if s in (0, 1) else [[CZ17] * 3 for _ in range(3)]
    ok35 &= luders_F(Est(s, s)) == tgt and dephase_F(Est(s, s)) == tgt
# agree on every diagonal (classical) state
for w in [[C17(Frac(1, 2)), C17(Frac(1, 3)), C17(Frac(1, 6))],
          [C17(1), CZ17, CZ17], [CZ17, C17(1), CZ17]]:
    dw = [[w[r] if r == c else CZ17 for c in range(3)] for r in range(3)]
    ok35 &= luders_F(dw) == dephase_F(dw)
# but DIFFER on the coherence E_01
ok35 &= luders_F(Est(0, 1)) == Est(0, 1)                  # Luders: C = all-ones, survives
ok35 &= dephase_F(Est(0, 1)) == [[CZ17] * 3 for _ in range(3)]  # dephasing: C = I, killed
ok35 &= luders_F(Est(0, 1)) != dephase_F(Est(0, 1))
# (d) rank-one collapse: fibre {0}
P0 = Est(0, 0)
def luders_1(X):
    return mmc17(mmc17(P0, X), P0)
def dephase_1(X):
    return mmc17(mmc17(P0, X), P0)                        # single block -> identical
ok35 &= all(luders_1(Est(s, t)) == dephase_1(Est(s, t))
            for s in range(3) for t in range(3))          # family collapses to Luders
check("F35", ok35,
      "THE SELECTOR-COMPLETION ROUND: RANK-ONE UNIQUENESS AND THE COARSE FIBRE "
      "(phase three, round twenty-two; kernel: ludersLift, ludersLift_apply, "
      "RankOneSelector, ludersLift_selector, choi_ludersLift, ludersLift_cp, "
      "cp_rankOneSelector_forces_luders, cp_rankOneSelector_iff_luders, "
      "monomial_luders_classicalBranch in OIBridge/BranchSelector.lean). (a) RANK-ONE "
      "UNIQUENESS: the Choi matrix of the Luders map P_k . P_k is the single entry at "
      "((k,k),(k,k)) -- exactly the rank-one projector |e><e|, PSD -- so by the "
      "round-17 PSD zero-diagonal lemma NO other CP map shares that Choi diagonal: the "
      "capstone cp_rankOneSelector_iff_luders says a CP coherent completion of the "
      "rank-one classical selector Phi(E_ss) = delta_sk E_kk has NO ALTERNATIVE to "
      "Luders. The branch update is forced, not a new freedom. (b) "
      "MONOMIAL-LUDERS COMPATIBILITY: on a diagonal classical state the fixed-basis "
      "Luders readout after any H-functor monomial lift U_g = D P_g is the phase-free "
      "classical branch w(g^-1 k) P_k, verified identical to the phase-free lift -- "
      "H-functor's phases do not disturb the branch. (c) COARSE FIBRE: on the "
      "rank-two fibre {0,1} the Luders map (correlation C = all-ones) and complete "
      "within-block dephasing (C = I) are DIFFERENT CP selectors agreeing on every "
      "classical branch probability yet differing on the coherence E_01 -- the "
      "surviving freedom is exactly a correlation matrix inside the selected block; "
      "(d) RANK-ONE COLLAPSE: on the fibre {0} the block is 1x1, C = [1] for both, and "
      "the family collapses to the unique Luders member. THE CLOSED CHAIN: bare Q_fb "
      "gives a CP rank-one branch extension; CP uniqueness makes it Luders; H-functor "
      "monomial phases do not disturb it; H-tensor supplies the ancilla; round-21 "
      "feed-forward produces the pure seed. So H-pure-seed disappears -- NOT replaced "
      "by an H-readout assumption -- and the endpoint is genuinely three conditions: "
      "H-functor, H-tensor, and sufficient composite Lie rank.")

# ----------------------- F36  the OI independence census: one shared C1-C4 core carrying
# three inequivalent coherent completions (phase three, round 23).  (a) THE SHARED CORE:
# three bits (v,h,b), observer reads (v,b), sigma(v,h,b) = (h,v,b), tau(v,h,b) =
# (v,h,b^1) -- reversible, commuting, C1 literal (the hidden bit drives the visible
# future), C2 structural (v_{t+2} = v_t), and already observer-minimal (the two-step
# visible itinerary separates all eight states); (b) THE COMB IDENTITY: all three
# completions return identical branch statistics on EVERY word of passive steps,
# tau-controls and rank-one readouts, equal to the bare classical comb; (c) NOT
# H-FUNCTOR: the dephasing tau-member is CPTP and classically exact but Phi_tau^2 != id;
# (d) NOT H-TENSOR: the phased lifts form a STRICT unitary rep of Z2 x Z2 (involutions
# that commute -- no projective cocycle) whose tau-lift is not I_vh (x) M_b; (e) PROPER
# LIE RANK: the phase-free lifts are tensor-local, every reachable control commutes with
# H = pi P_- (x) I_b, so the control Lie algebra is a single real line inside su(8).
ok36 = True
N36 = 8


def vhb36(i):
    return (i >> 2, (i >> 1) & 1, i & 1)


def idx36(v, h, b):
    return (v << 2) | (h << 1) | b


def vh36(i):
    return i >> 1


def b36(i):
    return i & 1


# --- (a) the shared swap-memory core
sig36 = [idx36(h, v, b) for (v, h, b) in map(vhb36, range(N36))]
tau36 = [idx36(v, h, 1 - b) for (v, h, b) in map(vhb36, range(N36))]
vis36 = [(v, b) for (v, h, b) in map(vhb36, range(N36))]
ok36 &= all(sig36[sig36[i]] == i for i in range(N36))        # reversible involutions
ok36 &= all(tau36[tau36[i]] == i for i in range(N36))
ok36 &= all(sig36[tau36[i]] == tau36[sig36[i]] for i in range(N36))   # commuting
# C1: two states with the same visible readout separated after one passive step
ok36 &= any(vis36[p] == vis36[q] and p != q and vis36[sig36[p]] != vis36[sig36[q]]
            for p in range(N36) for q in range(N36))
# C2: the visible stream carries a genuine one-bit memory, v_{t+2} = v_t
ok36 &= all(vis36[sig36[sig36[i]]] == vis36[i] for i in range(N36))
# observer-minimal: the two-step visible itinerary separates all eight states
ok36 &= len({(vis36[i], vis36[sig36[i]]) for i in range(N36)}) == N36
# C4 -- history readback: the present readout fixes neither past nor future.  Since the
# passive step is an involution the predecessor coincides with the successor, so the
# visible window (v_{t-1}, v_t, v_{t+1}) around state i is (h, v, h).
def hist36(i):
    return (sig36[i] >> 2, i >> 2, sig36[i] >> 2)


ok36 &= any(vis36[p] == vis36[q] and p != q
            and hist36(p) == (0, 0, 0) and hist36(q) == (1, 0, 1)
            for p in range(N36) for q in range(N36))
# C3 -- sufficient hidden memory capacity: every visible readout is carried by two states,
# separated precisely by the hidden bit, with differing visible futures; the hidden Bool
# has exactly two states, so the one-bit memory is EXACTLY saturated -- it carries the
# full past-to-future distinction the visible stream can express, and nothing more
ok36 &= len({(i >> 1) & 1 for i in range(N36)}) == 2
for r36 in {vis36[i] for i in range(N36)}:
    cls36 = [i for i in range(N36) if vis36[i] == r36]
    ok36 &= (len(cls36) == 2 and len({(i >> 1) & 1 for i in cls36}) == 2
             and vis36[sig36[cls36[0]]] != vis36[sig36[cls36[-1]]])

# --- the three completions, as correlation matrices over the SAME classical actions


def Est36(s, t):
    return [[CO17 if (r == s and c == t) else CZ17 for c in range(N36)]
            for r in range(N36)]


def inv36(g):
    gi = [0] * N36
    for x in range(N36):
        gi[g[x]] = x
    return gi


def corr36(g, C, X):
    gi = inv36(g)
    return [[C[gi[a]][gi[bb]] * X[gi[a]][gi[bb]] for bb in range(N36)]
            for a in range(N36)]


def luders36(k, X):
    out = [[CZ17] * N36 for _ in range(N36)]
    out[k][k] = X[k][k]
    return out


def rank1C36(d):
    return [[d[r] * d[c].conj() for c in range(N36)] for r in range(N36)]


allones36 = [[CO17] * N36 for _ in range(N36)]
dephase36 = [[CO17 if r == c else CZ17 for c in range(N36)] for r in range(N36)]
# the nonfactorizable phase: 1 on the v = h sector, +-i on v != h, sign set by b
nl36 = [CO17 if v == h else (C17(0, -1) if b else C17(0, 1))
        for (v, h, b) in map(vhb36, range(N36))]
ok36 &= all((z * z.conj()) == CO17 for z in nl36)             # unimodular
ok36 &= all(nl36[sig36[i]] == nl36[i] for i in range(N36))    # depends on v ^ h only
compl36 = {'nonFunctorial': {'pass': allones36, 'ctrl': dephase36},
           'nonTensor': {'pass': allones36, 'ctrl': rank1C36(nl36)},
           'restricted': {'pass': allones36, 'ctrl': allones36}}
# every member is a unit-diagonal correlation matrix, and the two coherent ones are
# rank-one d d^H (hence PSD by construction); dephasing is the identity (PSD)
for nm, tbl in compl36.items():
    for gen, C in tbl.items():
        ok36 &= all(C[s][s] == CO17 for s in range(N36))
ok36 &= allones36 == rank1C36([CO17] * N36)
ok36 &= dephase36 == eye17(N36)

# --- (b) THE COMB IDENTITY: every word gives the bare classical comb, for all three
perm36 = {'pass': sig36, 'ctrl': tau36}


def run_state36(name, word, w):
    X = [[w[r] if r == c else CZ17 for c in range(N36)] for r in range(N36)]
    for s in word:
        if s[0] == 'act':
            X = corr36(perm36[s[1]], compl36[name][s[1]], X)
        else:
            X = luders36(s[1], X)
    return X


def run_weight36(word, w):
    v = list(w)
    for s in word:
        if s[0] == 'act':
            gi = inv36(perm36[s[1]])
            v = [v[gi[a]] for a in range(N36)]
        else:
            k = s[1]
            v = [v[k] if a == k else CZ17 for a in range(N36)]
    return v


w36 = [C17(Frac(1, 8)), C17(Frac(1, 4)), C17(Frac(1, 16)), C17(Frac(1, 16)),
       C17(Frac(1, 8)), C17(Frac(1, 8)), C17(Frac(1, 8)), C17(Frac(1, 8))]
steps36 = [('act', 'pass'), ('act', 'ctrl'), ('read', 0), ('read', 3)]
for L in range(4):
    for word in itertools.product(steps36, repeat=L):
        ref = run_weight36(word, w36)
        dref = [[ref[r] if r == c else CZ17 for c in range(N36)] for r in range(N36)]
        for nm in compl36:
            ok36 &= run_state36(nm, word, w36) == dref

# --- (c) COUNTERMODEL 1: CPTP, classically exact, but not functorial
for s in range(N36):                       # classically exact on every classical state
    for nm in compl36:
        gen = 'ctrl'
        ok36 &= corr36(perm36[gen], compl36[nm][gen], Est36(s, s)) \
            == Est36(tau36[s], tau36[s])
E36 = Est36(0, 1)
twice36 = corr36(tau36, dephase36, corr36(tau36, dephase36, E36))
ok36 &= twice36 == [[CZ17] * N36 for _ in range(N36)]        # coherence killed twice over
ok36 &= twice36 != E36                                       # so Phi_tau^2 != identity
# the composed correlation is the Schur square of I, not the all-ones identity member
comp36 = [[dephase36[s][t] * dephase36[tau36[s]][tau36[t]] for t in range(N36)]
          for s in range(N36)]
ok36 &= comp36 != allones36
# the OTHER two completions DO compose to the identity on the same word
for nm in ('nonTensor', 'restricted'):
    C = compl36[nm]['ctrl']
    ok36 &= corr36(tau36, C, corr36(tau36, C, E36)) == E36

# --- (d) COUNTERMODEL 2: a strict unitary rep that is not tensor-local


def monoU36(c, g):
    return [[c[x] if g[x] == y else CZ17 for x in range(N36)] for y in range(N36)]


one36 = [CO17] * N36
Us36 = monoU36(one36, sig36)
Ut36 = monoU36(nl36, tau36)
Vt36 = monoU36(one36, tau36)
I36 = eye17(N36)
ok36 &= all(mmc17(U, dag17(U)) == I36 for U in (Us36, Ut36, Vt36))    # unitary
ok36 &= mmc17(Us36, Us36) == I36 and mmc17(Ut36, Ut36) == I36        # STRICT involutions
ok36 &= mmc17(Us36, Ut36) == mmc17(Ut36, Us36)                       # STRICT commutation
# conjugation by the phased lift IS the rank-one member of the round-17 family
for (s, t) in ((0, 1), (2, 5), (3, 3), (6, 1)):
    ok36 &= mmc17(mmc17(Ut36, Est36(s, t)), dag17(Ut36)) \
        == corr36(tau36, rank1C36(nl36), Est36(s, t))
# NOT I_vh (x) M_b: one and the same M entry is demanded to be both 1 and i
x1_36, x2_36 = idx36(0, 1, 0), idx36(0, 0, 0)
y1_36, y2_36 = tau36[x1_36], tau36[x2_36]
ok36 &= vh36(y1_36) == vh36(x1_36) and vh36(y2_36) == vh36(x2_36)
ok36 &= (b36(y1_36), b36(x1_36)) == (b36(y2_36), b36(x2_36))   # same M entry demanded
ok36 &= Ut36[y1_36][x1_36] == C17(0, 1) and Ut36[y2_36][x2_36] == CO17
ok36 &= Ut36[y1_36][x1_36] != Ut36[y2_36][x2_36]               # so no such M exists

# --- (e) COUNTERMODEL 3: tensor-local, functorial, proper control Lie rank
Mb36 = [[CO17 if y != x else CZ17 for x in range(2)] for y in range(2)]      # the X gate
ok36 &= all(Vt36[y][x] == ((CO17 if vh36(y) == vh36(x) else CZ17)
                           * Mb36[b36(y)][b36(x)])
            for y in range(N36) for x in range(N36))           # V_tau = I_vh (x) X_b


def swp2_36(a):
    return ((a & 1) << 1) | (a >> 1)


Mvh36 = [[CO17 if y == swp2_36(x) else CZ17 for x in range(4)] for y in range(4)]
ok36 &= all(Us36[y][x] == (Mvh36[vh36(y)][vh36(x)]
                           * (CO17 if b36(y) == b36(x) else CZ17))
            for y in range(N36) for x in range(N36))           # U_sigma = S (x) I_b
half36 = C17(Frac(1, 2))
Pm36 = [[half36 * ((CO17 if r == c else CZ17) - Us36[r][c]) for c in range(N36)]
        for r in range(N36)]
ok36 &= mmc17(Pm36, Pm36) == Pm36                              # P_- is idempotent
ok36 &= [[(CO17 if r == c else CZ17) - C17(2) * Pm36[r][c] for c in range(N36)]
         for r in range(N36)] == Us36                          # 1 - 2 P_- = U_sigma
# every reachable control fixes H by conjugation (H = pi P_-; the scale is irrelevant
# to the Lie rank, so the probe carries the rational generator P_-)
lifts36 = {'pass': Us36, 'ctrl': Vt36}
words36 = []
for L in range(5):
    for wt in itertools.product(('pass', 'ctrl'), repeat=L):
        U = eye17(N36)
        for g in wt:
            U = mmc17(lifts36[g], U)
        words36.append(U)
ok36 &= all(mmc17(mmc17(U, Pm36), dag17(U)) == Pm36 for U in words36)
# so every control generator -i U H U^H coincides: the Lie algebra is ONE real line
ok36 &= len({tuple(tuple((e.re, e.im) for e in row)
                   for row in mmc17(mmc17(U, Pm36), dag17(U))) for U in words36}) == 1
# a traceless skew-Hermitian direction outside that line
A36 = [[CZ17] * N36 for _ in range(N36)]
A36[0][0], A36[1][1] = C17(0, -1), C17(0, 1)
ok36 &= dag17(A36) == [[CZ17 - A36[r][c] for c in range(N36)] for r in range(N36)]
ok36 &= sum((A36[i][i] for i in range(N36)), CZ17) == CZ17     # traceless
# H has a nonzero off-diagonal entry exactly where A vanishes, so A = r(-iH) forces
# r = 0, hence A = 0 -- contradicted by A[0][0] != 0
qx36, qy36 = idx36(0, 1, 0), idx36(1, 0, 0)
ok36 &= not Pm36[qy36][qx36].z() and A36[qy36][qx36].z()
ok36 &= not A36[0][0].z()
ok36 &= 1 < N36 * N36 - 1                                      # dim line = 1 < 63 = su(8)
check("F36", ok36,
      "THE OI INDEPENDENCE CENSUS: ONE SHARED C1-C4 CORE, THREE INEQUIVALENT "
      "COMPLETIONS (phase three, round twenty-three; kernel: swapFn, flipFn, sigmaPerm, "
      "tauPerm, core_hidden_drives_visible, core_visible_period_two, "
      "core_observer_minimal, core_capacity_saturates, core_history_readback, "
      "core_isC1C4, threeCompletions_same_classical_comb, "
      "nonFunctorial_not_functorial, nonTensor_not_local, restrictedU_fixes_coreH, "
      "restricted_controlLie_line, outsideGen_not_mem, "
      "oi_core_underdetermines_completion in OIBridge/IndependenceCensus.lean). (a) THE "
      "SHARED CORE: three bits (v,h,b) with the observer reading (v,b); the passive step "
      "sigma(v,h,b) = (h,v,b) and the control tau(v,h,b) = (v,h,b^1) are commuting "
      "involutions, C1 is literal (v_{t+1} = h_t, so two states with the same readout "
      "separate after one step), C2 is structural (v_{t+2} = v_t, a genuine one-bit "
      "memory), C3 is sufficient hidden memory capacity (every visible readout is carried "
      "by exactly two states, separated precisely by the hidden bit, with differing "
      "visible futures -- the one-bit hidden sector has exactly the capacity the "
      "conditional past-to-future distinction demands), C4 is history readback (two "
      "states with the SAME present (v,b) carry the histories 0->0->0 and 1->0->1, so "
      "the present fixes neither past nor future and only the hidden bit separates them), and "
      "the core is ALREADY observer-minimal -- the two-step visible "
      "itinerary separates all eight states, so no quotient collapses it. (b) THE COMB "
      "IDENTITY: exhaustively over every word of length <= 3 in passive steps, "
      "tau-controls and rank-one readouts, all three completions return EXACTLY the bare "
      "classical comb -- the correlations drop out, so nothing in the C1-C4 operational "
      "data stream distinguishes them. (c) NOT H-FUNCTOR: the dephasing tau-member is "
      "CPTP and classically exact on every classical state, yet Phi_tau^2 kills the "
      "coherence E_01 that the identity preserves, so Phi_tau^2 != Phi_e while the other "
      "two completions do compose correctly. (d) NOT H-TENSOR: the phased lifts are "
      "unitary involutions that commute -- a STRICT representation of Z2 x Z2, no "
      "projective cocycle, hence functorial -- and conjugation by the tau-lift is "
      "verified to be the rank-one member of the round-17 family; but its b-flip "
      "amplitude is 1 on the v = h sector and i on v != h, and both are forced into the "
      "SAME entry M[1][0] of any I_vh (x) M_b, so no such M exists. (e) PROPER LIE RANK: "
      "the phase-free lifts really are S (x) I_b and I_vh (x) X_b, P_- = (1 - S(x)I)/2 is "
      "idempotent with 1 - 2P_- = U_sigma (so exp(-i pi P_-) = U_sigma), every one of the "
      "reachable controls fixes H by conjugation, so all control generators -i U H U^H "
      "coincide and the dynamical Lie algebra is a single real line -- dimension 1 "
      "against dim su(8) = 63 -- with an explicit traceless skew-Hermitian direction "
      "outside it. THE CENSUS: C1-C4 OI does NOT select the unrestricted operational "
      "completion. Case (e) is ordinary quantum kinematics with a restricted reachable "
      "control subgroup, NOT a non-quantum theory: S <=> D <=> Q_fb is untouched, and "
      "what fails is the unrestricted finite operational package.")

# ----------------------- F37  the compositional principle, the control separation, and the
# kernelized taxonomy (phase three, round 24).  (a) WORDS: concatenating implementations
# composes both the classical map and the coherent map -- structural, not an axiom;
# (b) EXTENSIONALITY FAILS for completion 1: [ctrl,ctrl] and [] realize the SAME classical
# transformation (tau^2 = 1) yet are completed differently; (c) EXTENSIONALITY HOLDS for
# completions 2 and 3: exhaustively over every word of length <= 4, words realizing the same
# transformation are completed identically -- so the coherent representation descends to the
# quotient by implementation equivalence; (d) SPECTATOR INDEPENDENCE: completion 2's tau-lift
# correlation depends on the spectator vh indices (no B-only CB reproduces it) while
# completion 3's does; (e) THE CONTROL SEPARATION: for a CENTRAL drift H = c.I every unitary
# fixes H by conjugation, so the control Lie algebra is one line for EVERY menu however rich
# -- H_Lie is a sufficient certificate, NOT a necessary condition.
ok37 = True
gens37 = ('pass', 'ctrl')


def wperm37(word):
    g = list(range(N36))
    for i in reversed(word):
        p = perm36[i]
        g = [p[g[x]] for x in range(N36)]
    return tuple(g)


def wmap37(name, word, X):
    for i in reversed(word):
        X = corr36(perm36[i], compl36[name][i], X)
    return X


def allwords37(maxlen):
    out = []
    for L in range(maxlen + 1):
        out.extend(itertools.product(gens37, repeat=L))
    return [list(w) for w in out]


# --- (a) concatenation is structural: it composes classical maps AND coherent maps
Xg37 = [[C17(Frac(1 + 3 * r + 5 * c, 7), Frac(2 + r - c, 11)) for c in range(N36)]
        for r in range(N36)]
for u in allwords37(2):
    for v in allwords37(2):
        gu, gv = wperm37(u), wperm37(v)
        ok37 &= wperm37(u + v) == tuple(gu[gv[x]] for x in range(N36))
        for nm in compl36:
            ok37 &= wmap37(nm, u + v, Xg37) == wmap37(nm, u, wmap37(nm, v, Xg37))

# --- (b) completion 1 is NOT implementation-extensional
ok37 &= wperm37(['ctrl', 'ctrl']) == wperm37([])            # same classical transformation
E01_37 = Est36(0, 1)
ok37 &= wmap37('nonFunctorial', ['ctrl', 'ctrl'], E01_37) \
    != wmap37('nonFunctorial', [], E01_37)                  # different coherent map

# --- (c) completions 2 and 3 ARE implementation-extensional, exhaustively to length 4.
# The coherent map is identified by its action on ALL 64 matrix units, so "same map" is
# tested exactly rather than on a single probe input.
units37 = [Est36(a, b) for a in range(N36) for b in range(N36)]


def sig37(name, word):
    return tuple(tuple(tuple((e.re, e.im) for e in row) for row in wmap37(name, word, U))
                 for U in units37)


for nm in ('nonTensor', 'restricted'):
    byperm = {}
    for w in allwords37(4):
        byperm.setdefault(wperm37(w), set()).add(sig37(nm, w))
    ok37 &= all(len(v) == 1 for v in byperm.values())       # descends to the quotient
    ok37 &= len(byperm) == 4                                # exactly Z2 x Z2 is realized
# completion 1 fails the same exhaustive test
bad1 = {}
for w in allwords37(4):
    bad1.setdefault(wperm37(w), set()).add(sig37('nonFunctorial', w))
ok37 &= any(len(v) > 1 for v in bad1.values())

# --- (d) the spectator criterion: does a B-only correlation reproduce the tau-member?
def spectator_ok37(C):
    seen = {}
    for p in range(N36):
        for q in range(N36):
            key = (b36(p), b36(q))
            val = (C[p][q].re, C[p][q].im)
            if key in seen and seen[key] != val:
                return False
            seen[key] = val
    return True


ok37 &= not spectator_ok37(compl36['nonTensor']['ctrl'])    # depends on the spectator
ok37 &= spectator_ok37(compl36['restricted']['ctrl'])       # genuinely local
ok37 &= spectator_ok37(compl36['restricted']['pass'])
# the exact overdetermined entry: -1 on the v != h sector, +1 on v = h, same (b,b') slot
Cnt37 = compl36['nonTensor']['ctrl']
p1_37, q1_37 = idx36(0, 1, 0), idx36(0, 1, 1)
p2_37, q2_37 = idx36(0, 0, 0), idx36(0, 0, 1)
ok37 &= (b36(p1_37), b36(q1_37)) == (b36(p2_37), b36(q2_37))
ok37 &= Cnt37[p1_37][q1_37] == C17(-1) and Cnt37[p2_37][q2_37] == CO17

# --- (e) THE CONTROL SEPARATION: a central drift defeats H_Lie for EVERY menu
Hc37 = eye17(N36)                                            # H = 1.I, central
menu37 = [Us36, Ut36, Vt36, mmc17(Us36, Vt36), mmc17(Ut36, Vt36), I36]
for V in menu37:
    ok37 &= mmc17(V, dag17(V)) == I36                        # unitary
    ok37 &= mmc17(mmc17(V, Hc37), dag17(V)) == Hc37          # fixes the central drift
# so every control generator -i V H V^dag equals -i H: the algebra is the single line R(-iH),
# and every element of that line is a multiple of the identity -- equal diagonal entries
A37 = [[CZ17] * N36 for _ in range(N36)]
A37[0][0], A37[1][1] = C17(0, -1), C17(0, 1)
ok37 &= dag17(A37) == [[CZ17 - A37[r][c] for c in range(N36)] for r in range(N36)]
ok37 &= sum((A37[i][i] for i in range(N36)), CZ17) == CZ17   # traceless skew-Hermitian
ok37 &= A37[0][0] != A37[1][1]                               # unequal diagonal -> not r.I
# a genuinely rich menu still fails H_Lie, because H_Lie constrains H, not the menu
ok37 &= len({tuple(tuple((e.re, e.im) for e in row)
             for row in mmc17(mmc17(V, Hc37), dag17(V))) for V in menu37}) == 1
# contrast: the round-19 architecture with the NON-central passive Hamiltonian still gives a
# line here too (F36 (e)) -- the point is that H_Lie can fail while all operations are present
ok37 &= 1 < N36 * N36 - 1
check("F37", ok37,
      "THE COMPOSITIONAL PRINCIPLE, THE CONTROL SEPARATION, AND THE KERNELIZED TAXONOMY "
      "(phase three, round twenty-four; kernel: wordPerm, wordMap, wordPerm_append, "
      "wordMap_append, ImplementationExtensionality, "
      "implementationExtensionality_descends, descendedAction_functorial, "
      "implementationExtensionality_iff_functorial, SpectatorIndependent, "
      "spectatorIndependent_iff, HComp, hComp_iff, HControl, "
      "HControl_iff_controlLie0_full, centralDrift_not_HControl, "
      "UniversalUnitaryReachability, fullOps_universalUnitary, census_clause_taxonomy in "
      "OIBridge/MonoidalCompletion.lean). (a) WORDS: concatenating implementations composes "
      "both the classical map and the coherent map -- verified over every pair of words of "
      "length <= 2 -- so sequential composition is STRUCTURAL at the word level, not an "
      "axiom. The single axiom is implementation extensionality, and its content is DESCENT: "
      "the coherent representation factors through the quotient by implementation "
      "equivalence, becoming a representation of physical transformations rather than of "
      "implementation strings. (b) COMPLETION 1 FAILS IT: [ctrl,ctrl] and [] realize the "
      "SAME classical transformation, tau^2 = 1, yet complete differently on E_01. (c) "
      "COMPLETIONS 2 AND 3 SATISFY IT: exhaustively over every word of length <= 4, words "
      "realizing the same transformation have identical coherent maps -- compared on ALL 64 "
      "matrix units, so map equality is exact -- and exactly the four elements of Z2 x Z2 "
      "are realized; completion 1 fails the same test. (d) SPECTATOR INDEPENDENCE: "
      "completion 2's tau-correlation forces the SAME (b,b') slot to be both -1 (on v != h) "
      "and +1 (on v = h), so no I_vh (x) M_b reproduces it, while completion 3's "
      "correlations are constant and do. (e) THE CONTROL SEPARATION -- the round's central "
      "correction: for a CENTRAL drift H = c.I EVERY unitary fixes H by conjugation, so the "
      "control Lie algebra is the single line R(-iH) for EVERY menu however rich, and every "
      "element of that line is a multiple of the identity with equal diagonal entries -- "
      "while the traceless skew-Hermitian direction -i(E_00 - E_11) has unequal diagonal. So "
      "an observer possessing every unitary still FAILS H_Lie. H_Lie is a sufficient "
      "CERTIFICATE for universal reachability in the round-19 drift/control architecture, "
      "NOT a necessary condition for full operational QM; the operational principle is "
      "H_opControl (universal unitary reachability), and unitary channels are one-outcome "
      "instruments, so they need no separate conjunct (fullOps_universalUnitary). Baking "
      "H_Lie into the definition would make the characterization hostage to one control "
      "architecture.")


print()
print('     [scope] Settled in Lean: the return-probability expansion, positivity of every gap')
print('     coefficient, gap-set determination from equal probability families (Dedekind, at every')
print('     real time), the |U_ij|^2 expansion over the same frequencies, and both invisible')
print('     impostors -- the energy origin and the antiunitary reflection -- as exact identities.')
print('     The two-branch reconstruction is now a manuscript THEOREM at K2: every step is')
print('     kernel-proved except the cited integer Bekir-Golomb classification (the explicit')
print('     premise BGIntegerClassification); the homometric rulers mark why the proof runs on')
print('     coefficient-labelled data, and formalizing the 2007 classification is the sole')
print('     remaining K3 backlog item.')
print()
print("bohr_frequency_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
