# Track D report (saved by coordinator from the agent hand-back; agent could not write files)

Base 6bc2c4af (detached worktree, removed). Nothing committed/pushed. PREREG.md frozen before
computation (Amendment 1 appended before the run it governs). All Python `python3 -I -B`, exact
Fraction/integer arithmetic. All PREREG §4 + Amendment 1 controls green.

## Verdict
1. Bijective realizations: (C2-structural) holds automatically for every law, Markov included — vacuous there.
2. Non-injective/staged completions (canonical predictive quotient): whole-past retention is not automatic
   (i.i.d. coin: identical posteriors); readout-relevant retention is forced by clause (b) whenever there is a gap
   — a consequence of (C4), not an independent condition.
3. Coarse-grained physical descriptions (hidden channel between couplings not fitted to the law): (C2-structural)
   is non-vacuous; necessary for (C4), not sufficient. Only class where it constrains anything.
4. (C2) necessity splits: persistence form unconditional (observed memory forces some hidden conditional at the
   coupling time away from the reference prior); slow-bath form conditional on (EM) + uniform erosion.
5. SC-16 REFUTED: no stronger structural form of (C2) yields accessible-window P-indivisibility, alone or with
   (EM), (C2-slow), time-homogeneity; includes persistent maximal readback at every order and the kernel's
   `RoutedReadbackAtStorage`. Exact countermodels satisfy all and stay P-divisible on windows up to just before
   recurrence; two families with unbounded window/gap-order ratio. Missing assumption: in-window rooted revival,
   C4r at the window (roots a≠b, s<t in window, TV(Γ_s(a),Γ_s(b)) < TV(Γ_t(a),Γ_t(b))). C4r sufficient and
   Lean-checked (`c4r_implies_pIndivisible`, OIBridge/CausalReadback.lean:134, only hypothesis `h : C4r K Γ`);
   not necessary; implied by none of the (C2)/(C4) forms.

## Status table
| Statement | Status | Verification |
|---|---|---|
| C1 necessity; C4 necessity | unconditional | paper proof |
| C3 necessity | unconditional | Lean `c3_necessity` |
| Clause (b) distinguishability floor | unconditional, any joint law, deterministic step | Lean `distinguishability_floor` |
| (C2-structural) automatic in bijective realizations | unconditional | paper proof + exact computation |
| Gap forces readout-relevant persistence in any deterministic/Markovian hidden-state completion | unconditional | paper proof |
| Observed memory I* ⇒ max_p TV(μ_p, π_H) ≥ ε_min(I*, n_V) at coupling time (contrapositive of physical-memory theorem, Main:463) | unconditional | paper proof |
| Observed memory ⇒ τ_B ≥ τ_S/ln(1/ε_min) | conditional on (EM) + uniform erosion | paper proof |
| Fast mixing erases readback; Boltzmann-brain chain (Main:754) | conditional on (EM), uniform erosion, and K_Σ^n governing readout-relevant conditionals | last premise unproved interpretation (D6) |
| C1–C4 + any (C2) form (± EM, C2-slow, time-homogeneity) ⇒ accessible-window P-indivisibility | REFUTED | exact computation |
| C4r / C4e at window ⇒ P-indivisibility on it | proved (sufficient, not necessary) | Lean `c4r_implies_pIndivisible`, `c4e_implies_pIndivisible` |
| Physical hidden sectors show in-window rooted revival? | open | — |
| K_Σ^n governs n-step coarse conditionals P U^n P over accessible windows? | open (unstated premise) | exact check they differ in general |

## Findings
D1 (C2-structural) automatic in every bijective realization. Claims Main:76, :608, :82, also :20, :768,
Substratum:322. Proof: (X_0,H_0)=φ^{-t}(X_t,H_t) ⇒ visible past is a function of (X_t,H_t) ⇒
I(X_<t;H_t|X_t)=H(X_<t|X_t); posterior supports of distinct histories ending at x are disjoint ⇒ TV=1 ⇒ RHS of
(b) is 1 for every law. Exact: c2_bijective_checks.py, all bijections at (2,2) 24, (2,3)/(3,2) 720, (2,4) 40,320,
every t ≤ L uniform, all (2,3) correlated; 0 violations; countercontrol hidden-reset (x,h)↦(x⊕h,0) 6/6
violations. No Lean coverage (Realization takes arbitrary joint weight).

D2 Non-injective/staged: (b) proof uses only X_{t+1}=f(X_t,H_t) ⇒ posteriors ≥ δ apart. Canonical quotient t=1:
i.i.d. coin identical (2/2); XOR disjoint (2/2); X_2=X_1⊕[X_0=0] merges X_0=1,2, other 4 pairs disjoint.

D3 Candidate non-vacuous forms: C2-coarse (necessary for C4 via (b) after Σ; non-vacuous; not sufficient —
tape-and-ledger coin). Persistence lemma (Z_t Markov ⇒ TV(P(X_>s|q),P(X_>s|q')) ≤ TV(P(Z_s|q),P(Z_s|q'))).
In-window routing = (C4). Persistence with mixing = D4. Side result: under counting measure fresh-hidden kernel
K̄_x = P(X_{t+1}|X_t=x) at every t (sc16_search.py 0 mismatches at four sizes).

D4 C2 necessity has an unconditional persistence half. Main:736 ledger "Conditional on the hidden-sector mixing
hypothesis"; glossary:27 ↔ FULL:6627 "derived from observed memory by the physical-memory theorem" drops the
condition. Contrapositive of physical-memory theorem uses no hypothesis; timescale reading needs (EM)+uniform
erosion. Paper proof.

D5 SC-16 refuted. Γ_t(a,j)=μ_H{h: π_V φ^t(a,h)=j}; P-divisibility by exact LP, divisors re-verified, Farkas
certificates for infeasibility.
(a) 6-state, uniform prior, time-homogeneous: V={0,1}, H={0,1,2}, index 3x+h, permutation [0,3,4,1,5,2], L=6;
Γ_1=Γ_5=[[1/3,2/3],[2/3,1/3]], Γ_2=Γ_3=Γ_4=[[2/3,1/3],[1/3,2/3]], Γ_6=I; P-divisible on {0..5} (divisors I or
swap), not on {0..6}; gap δ=1 at every order 1..6; RoutedReadbackAtStorage at K=2 witness (0,1,1,1,2,0); C1
(Γ_1 non-permutation); C3 automatic.
(b) Exhaustive: (2,2) 16/8/2/8/2·0; (2,3) 648/576/5/288/570·552; (3,2) 672/240/4/240/540·180;
(2,4) 39,168/21,888/6/8,064/34,000·6,912 [columns: bijections with gap / C4 countermodels (P-divisible on
{0..k_min+1}) / best F2 window / F2max countermodels / F4 at some K≤L−1 · of these P-divisible on {0..K}].
Best F2 at (2,4) [1,4,5,6,2,3,7,0], L=8, P-divisible on {0..6}. Recurrence-theorem control 0 violations;
closed-form 2×2 cross-check agreed with LP on 5,664 + 267,264 pairs.
(c) LFSR: V=GF(2), H=GF(2)^m, shift of maximal-period sequence (primitive degree m+1), L=2^{m+1}−1. Paper proof:
Γ_t=J/2 for 1≤t≤L−1; P-divisible on {0..L−1} with divisor J/2; no gap below order m; gap δ=1 at every k≥m.
Exact m=1..4 (L=3,7,15,31): divisible on {0..L−1}, not on {0..L} (lfsr_family.py).
(d) F4 + (EM) + (C2-slow): hidden bit g ~ BSC(1/50) (second eigenvalue 24/25, mixing time 25), visible flips
with p_g (p_0=1/5, p_1=2/5), ledger l'=l⊕x; 80,000-state bijection. Exact (f4_routed_storage.py): λ_t = 1, 2/5,
124/625, 8552/78125, 614896/9765625; P-divisible on {0..4}; F4 at K=4 witness (0,1,1,1,2,0); gaps orders 1–3.
Paper proof every n: λ_t=E[Π_{i<t}(1−2p_{g_i})] positive strictly decreasing ⇒ divisor ratio λ_t/λ_s stochastic.
(e) Read-only (EM): x_{t+1}=g_t⊕r_t, g ~ BSC(1/50) (em_countermodel.py): shared prior ⇒ rank-one Γ_t, P-divisible
{0..6}; stationary initial law λ_t=(6/25)(24/25)^{t−1}, P-divisible {0..6}, gaps orders 1..5; exact
1,024-state bijection reproduces shared-prior model.
Revival check (revival_check.py): every pair with increasing rooted distinguishability at four sizes
(461,536 at (2,4)) has no stochastic divisor — consistent with C4r.
Provenance: extends verification/programmes/oi-qm/track-i/recurrence-tightness/result.md (tight witness
N_CR=3; "causal write/store/read does not force same-window … P-indivisibility") and recurrence-scaling/result.md
(tight witnesses N≥4, non-uniform priors). New: counting-measure countermodels incl. 6-state F4; unbounded LFSR
under counting measure (history-level C4); F4 family with (EM)+(C2-slow).
New SC-16 sites (chapter = FULL mirror): ch01:121↔FULL:465; ch01:133↔FULL:477; appendix-b:420↔FULL:6187;
ch04:178↔FULL:1297; Complexity:478/:503 already in #946. out_sc16_sitegrep.txt: 158 candidate lines (not all defects).

D6 Unstated premise in (EM) (Main:754): in exact bijective description ¬(C2-structural) impossible (D1), so the
corollary's ¬(C2-structural) is coarse-grained. (EM) at Main:744 is a property of K_Σ=PUP; chain needs PU^nP.
compression_check.py: φ(z)=z+1 on Z_5, σ=[z=0]: K=[[0,1],[1/4,3/4]], PU^nP=K for n=1..4, PU^5P=I, while K^n relaxes.
Extra premise needed: K_Σ^n governs readout-relevant conditionals over the window — owner decision.

## Recommended edits (agent's proposals; NOT reviewed)
Rebuild `sh ./build.sh Main Substratum Complexity --book`; re-grep `C2-structural` (base: 9× on 6 lines of Main,
1× Substratum, 1× ch01↔FULL, 1× appendix-c↔FULL).

E1 Main:76 replace (C2-structural) sentence with: "**(C2-structural):** a hidden record of visible history, once
written, persists to the readback that uses it. In every faithful deterministic completion of a law with a
readback gap, clause (b) of the universal hidden-memory theorem forces this retention for the readout-relevant
part of the record (§3.4); in a bijective realization the visible past is a function of the present state
$(X_t, H_t)$, so the retention holds for every law, Markov laws included. (C2-structural) is therefore a
constraint on a coarse-grained description of the hidden sector, whose effective channel between couplings can
scramble the readout-relevant record before readback; in such a description it is necessary for (C4) and does
not imply it." Plus: "(C2-slow) implies (C2-structural) under the uniform-erosion estimate" → "… in such a
description under the uniform-erosion estimate"; "satisfying (C2-structural) while violating (C2-slow)" → "so
that (C4) holds while (C2-slow) fails"; Status clause "and in the other direction it is *derived* — …
conditional on the hidden-sector mixing hypothesis, which is the physical-memory theorem of §3.4 rather than an
assumption." → "and in the other direction observed conditional memory $I^*$ forces some realized hidden
conditional at the coupling time to lie at total-variation distance at least $\varepsilon_{\min}(I^*, n_V)$ from
the reference prior — the contrapositive of the physical-memory theorem of §3.4, which uses no mixing hypothesis —
and, under the hidden-sector mixing hypothesis with uniform erosion, this bounds the bath's mixing time below by
$\tau_S/\ln(1/\varepsilon_{\min})$."
E2 Main:736 C2 necessity row: "Persistence form proved: a readback gap forces the readout-relevant hidden record
to persist to readback in every faithful deterministic completion (clause (b)), and observed memory $I^*$ places
some hidden conditional at the coupling time at least $\varepsilon_{\min}(I^*, n_V)$ from the reference prior
(physical-memory theorem); in a bijective realization the retention holds for every law. Slow-bath form
conditional on the hidden-sector mixing hypothesis; the quantitative bound $\varepsilon \geq \delta/(k-1)$ is
proved, its constant saturated in the certification suite (`c2_mixing_probes.py`); ETH is physical motivation,
not a premise"
E3 Main:82: "C2-structural, the persistence of the readout-relevant record to readback, is forced by C4 in every
faithful completion and holds for every law in a bijective one; it constrains coarse-grained descriptions of the
hidden sector, where C2-slow is one physical mechanism."
E4 Main:20: "(C2-structural), the persistence of the stored record until readback, holds in every faithful
completion of a law with memory and constrains coarse-grained descriptions of the hidden sector, where the
slow-bath inequality is one sufficient physical mechanism."
E5 Main:768: "C1 and C3 are necessary diagnostics of that mediation and its capacity; C2-structural, the
persistence of the readout-relevant record to readback, is forced in every faithful completion and constrains
coarse-grained descriptions of the hidden sector, with C2-slow one sufficient physical mechanism."
Substratum:322: "C1 and C3 diagnose the mediation and its capacity, and C2-structural, the persistence of the
readout-relevant record to readback, is forced by C4 in every faithful completion."
E6 Main:754 (owner decision on D6): replace "— and because (EM) posits genuine mixing…" through "⇒ $M_t = 0$ on
accessible windows (§3.4)" with "— and because (EM) posits genuine mixing of the coarse-grained channel rather
than mere speed, the persistence form (C2-structural) fails with it in the coarse-grained description: the
readout-relevant record is scrambled before readback, provided the iterated channel $\mathcal{K}_\Sigma^n$
governs the readout-relevant hidden conditionals over the window. In the exact bijective description the record
of visible history is retained by reversibility and is inaccessible to the readout. The chain closes in the
memory currency: $\neg$(C2-structural) $\Rightarrow$ $\neg$(C4) by clause (b) of the hidden-memory theorem, at the
rate of the fast-bath erasure lemma, $\Rightarrow$ $M_t = 0$ on accessible windows (§3.4)". Alternative in (EM)
at Main:744: "*the coarse-grained $n$-step channels $P_\Sigma\,\mathcal{U}_\varphi^n\,P_\Sigma$ of the local
region relax toward local equilibrium at the rate $1/\tau_{\rm mix}$ set by the dissipative gap of
$\mathcal{K}_\Sigma$, for $n$ up to the accessible window.*"
E7 glossary:27 ↔ FULL:6627: "**C2 (Memory persistence).** A physical-regime premise rather than one of the three
structural conditions (C1, C3, C4): the equivalence runs over those three. It is stated in two forms ([Main
§1.3]). C2-structural requires that a stored record of visible history persist to the readback that uses it; it
holds automatically in any reversible realization and is forced by C4 in every faithful completion, so it
constrains coarse-grained descriptions of the hidden sector. C2-slow requires the hidden sector's coarse-grained
mixing time to exceed the accessible window, $\tau_S \ll \tau_B$; it is one sufficient mechanism for persistence,
and fast conserved dynamics serve equally ([Main §1.3], `fastbath_probes.py`). C2 is the persistence half of what
C4 operationally needs (the other half is in-window routing). Observed memory keeps the hidden conditionals at
the coupling time away from the reference prior, and, under the hidden-sector mixing hypothesis, forces the slow
form (the physical-memory theorem). For our universe at the cosmological horizon, $\tau_S / \tau_B \sim
10^{-32}$. Under the mixing hypothesis, C2 fails when the hidden sector thermalizes between measurements,
producing classical Markovian dynamics. Discussed in Chapter 1 §1.3."
E8 appendix-c:102 ↔ FULL:6348 after "…contains ([Main §3.4])." insert: "In a reversible realization this
retention holds for every process, Markov ones included, because the present state determines the visible past;
the condition has content for a coarse-grained description of the hidden sector, in which a record can be
scrambled before readback."
E9 ch01:223 ↔ FULL:567: "this frozen-bath condition is what secures (C2-structural) — record persistence to
readback — by the most robust mechanism available." → "this frozen-bath condition is what secures
(C2-structural) in the coarse-grained description of the horizon — the readout-relevant record persisting to
readback — by the most robust mechanism available; in an exact reversible description the record is always
retained, and the frozen bath is what keeps it accessible to the readout."
E10–E13 (offered to SC-16):
E10 ch01:121↔FULL:465 last two sentences → "What the framework requires on *accessible* timescales — times short
compared to $\tau_B$, the hidden sector's intrinsic memory time — is conditional memory, and the
accessible-timescale lemma supplies it. P-indivisibility on those timescales is a further property: C1–C4 with a
slow bath admit rooted transition families that remain P-divisible on every window shorter than the recurrence
time, and P-indivisibility within a window follows when the visible distinguishability of two rooted
preparations increases within it."
E11 ch01:133↔FULL:477 new last sentence: "The recurrence-based proof establishes P-indivisibility over the
recurrence cycle; the accessible-timescale lemma establishes conditional memory in the parameter regime that
matters for actual observers in our universe."
E12 appendix-b:420↔FULL:6187: "while C2/C3 promote P-indivisibility from a formal property to an observationally
dominant one." → "while C2–C4 make conditional memory observable on accessible windows; P-indivisibility within
such a window requires in addition that rooted visible distinguishability increase within it."
E13 ch04:178↔FULL:1297 "that produces P-indivisibility" → "that sustains accessible memory"; Complexity:478 "so
their dynamics is P-indivisible." → "so their dynamics carries accessible conditional memory."; Complexity:503
"wherever C1–C4 are satisfied, P-indivisibility is mandatory." → "wherever C1–C4 are satisfied, accessible
conditional memory is mandatory."
Left unchanged: Main:608, ch02:20 accurate; "backflow" at Main:153/:174 belongs to SC-5.

## Reproduce (from trackD/)
controls.py → CONTROLS ALL GREEN; c2_bijective_checks.py → Q1 CHECKS ALL GREEN; sc16_search.py 2x2 2x3 3x2 then
2x4 → D5(b) table + INLINE CONTROLS ALL GREEN; lfsr_family.py → LFSR FAMILY ALL VERIFIED; em_countermodel.py →
EM COUNTERMODEL ALL VERIFIED; f4_routed_storage.py → F4 RUN CONTROLS GREEN; revival_check.py → REVIVAL CHECK
GREEN; compression_check.py → both lines True. Shared code trackd_lib.py.
