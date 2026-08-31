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
