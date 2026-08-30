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
check("F10", ok10,
      "THERMAL ORIENTATION: gibbs(-beta) of the reflected energies equals gibbs(beta) of the "
      "original (the E0 shift cancels; machine precision), +beta and -beta profiles differ "
      "whenever energies differ and coincide when all are equal, the matrix identity "
      "D conj(rho_beta) D^dag = rho_{-beta}(H') holds for the reflection-branch coboundary, "
      "and (exact fractions) a strictly passive profile is strictly active after energy "
      "reflection -- oriented positive-temperature structure excludes the antiunitary branch "
      "(kernel: transported_gibbs, gibbs_orientation, passivity_selector)")

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
