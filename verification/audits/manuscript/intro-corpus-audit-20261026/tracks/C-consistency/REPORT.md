# Track C: global consistency audit after SC-1 to SC-4 (main 6bc2c4af; Introduction at 4a260ca9)

The coordinator recorded this file verbatim from the auditor's hand-back. The harness blocked the auditor's own write. Scripts and run outputs are in this directory (`tools/`, `out_*.txt`, `diff_*.txt`, `FINDINGS_intro.md`). The auditor removed both worktrees and committed, pushed and commented nothing.

**Counts:**

| Category | Count |
|---|---|
| False statement | 1 (at 5 sites) |
| Overstatements | 4 |
| Stale mirrors | 3 (19 sites) |
| Understatements | 3 |
| Documentation items | 8 |
| Introduction items | 12 |

The #946 items already recorded are excluded. The SC-16 and SC-17 entries below list new sites only.

**C3-conditional-on-(EM) sweep.** Nothing beyond Substratum :136. Main :496 and :630, appendix-b :459, appendix-c :98/:106/:110 and glossary :39 all keep (C3) unconditional.

**Mirrors.** Every chapter/FULL pair agrees, on main and on #951. `mirror_check` reports 0, and the auditor's two-way check found nothing. For book sites, FULL is only one more place to edit.

**Lean.** Statuses are read from the source in `OIBridge/`. There is no Lean toolchain in this container, so nothing was rebuilt.

## Tool runs at 6bc2c4af

- **coverage_check:** OK.
  - 128 statements; kernel 30/116, machine 58/116.
  - 29 named probes are not run by CI. They include every probe behind the theorems that SC-1 to SC-4 edited.
- **lean_manuscript_census:** OK. 227 modules, 20 current families. The recurrence-horizon and physical-C4-discharge families are kernel-only.
- **edge_rigidity_probe:** ALL CHECKS PASS. Its scope is GR reconstruction, which SC-1 to SC-4 did not touch.
- **mirror_check:** 0 lines absent.
- **Uncited probes, run locally:** all pass.
  - opglue 25/25
  - process_dilation, memory, primitive, review4, equivalence_recovery
  - the three `verification/lean` source probes
- **`tools/scope_equiv.py`:** the auditor's own exact check of the SC-3 Scope equivalence, over every bijection with uniform priors. "Gap below L ⇔ some Γ_s (0<s<L) non-permutation" holds with no violations:
  - (2,2): 16 cases where both hold, 8 where neither does
  - (2,3): 648 both, 72 neither
  - (3,2): 672 both, 48 neither

## FALSE

### F-1 (new SC-16 sites): the accessible-window backflow lemma is said to give P-indivisibility

1. **Claims.**
   - GR:589: "The accessible-timescale backflow lemma ([Main, §2.3]) provides a second route to P-indivisibility that is independent of |C_H|."
   - Explainer:892: "…establishes P-indivisibility without recurrence"
   - ch01:121 (FULL:465): "The framework requires P-indivisibility on *accessible* timescales … The accessible-timescale lemma supplies this."
   - ch01:129 (FULL:473): "distinguishability has rebounded by an amount of order I_0 at every step"
   - ch01:133 (FULL:477): "…the accessible-timescale lemma establishes that the same property holds…"
2. **Assumptions.** A C4 gap at an accessible order, with mass p_0 and gap δ (Main:167).
3. **Counterexample.** The lemma gives only CMI ≥ p_0δ²/ln2. The XOR family (Main:622) has 1 bit of memory and is P-divisible through Λ=I. Main:141 Scope says the same.
4. **Status.** Exact computation and a paper proof.
   - Computation: `python3 -I -B papers/oi_lattice_code/foundations/review4_probes.py`, expected output COMPLETE.
   - Paper proof: Main:622.
5. **Affected.** The five sites above; #951 does not touch them.
6. **Replacements.**
   - GR:589: "The accessible-timescale backflow lemma ([Main, §2.3]) gives, independently of |C_H|, positive conditional memory on accessible windows; it does not give P-indivisibility there, which memory does not force (the XOR family, [Main, §3.4])."
   - Explainer:892, two changes:
     - "…establishes accessible conditional memory without recurrence, though not P-indivisibility…"
     - replace "recurrence produces P-indivisibility … nontrivially indivisible" with "recurrence together with any non-permutation rooted map produces P-indivisibility; the quantum representation exists for every finite law."
   - ch01:121: "The framework requires memory on *accessible* timescales … not only indivisibility at recurrence. The accessible-timescale lemma supplies that memory; it does not supply P-indivisibility on those timescales ([Main §2.3])."
   - ch01:129: "Conditional memory of order I_0 is therefore present at every step of the accessible-timescale regime until enough cycles have accumulated to deplete the stored record; this is memory, not a revival of distinguishability, which it does not force."
   - ch01:133, second sentence: "…the accessible-timescale lemma establishes positive conditional memory in the parameter regime that matters for actual observers in our universe, a different and weaker property."

## OVERSTATEMENT

- **O-1. SM:296.** It says "the chaotic mixing underlying operational measurement independence ([Main] §3.3)".
  - Measurement independence is a posit under SC-4 (Main:398–405), and §3.3 contains no mixing argument.
  - Status: unproved interpretation.
  - Replacement: "the chaotic mixing that may motivate, but does not derive, the measurement-independence posit of [Main] §3.3".
- **O-2. glossary:107 (FULL:6707), the gluing theorem.** It says "…within the stated O(K/G) bound … explicit hidden-capacity bounds … Certified in exact arithmetic (`opglue_probes.py`)".
  - The bound is proved only in exact arithmetic, and the fixed-point capacity depends on the open finite-b bound (Main:562/570).
  - The probe computes exact laws on qubit instances but compares total variation in floats (lines 161, 193).
  - Replacements:
    - insert "with exact-arithmetic registers," before "a finite reversible…";
    - "an explicit exact-arithmetic hidden-capacity bound (the fixed-point form depends on a finite-precision accuracy bound that is open)";
    - "Checked on qubit instances with exact laws (`opglue_probes.py`)."
- **O-3. Main:560, the ε-form statement.** It says "the unnormalized digitized branch matrix (a density register)", but the proved clause (1) is for exact-ring registers (R-40).
  - Replacement: "the unnormalized branch matrix (a density register), held exactly over the instruments' entry ring, or digitized to b fractional bits in the fixed-point variant of clauses (1) and (5)".
- **O-4. Main:610.** It says "At (2,3) the two agree for one of fifteen…" (`memory_probes.py`). The probe uses the uniform prior and floats, and under arbitrary priors the audit found 2 of 16 (R-33).
  - Replacement: "At (n_V,|C_H|)=(2,3), under the uniform prior, the two agree…".

## STALE MIRROR

### S-1. "C3 follows from C4" survives, although (C3) is unconditional after SC-3

- **Sites:**
  - Main:72, :78, :620
  - ch00:37 (FULL:273)
  - ch01:133 (FULL:477)
  - ch01:201 (FULL:545)
  - ch07:30 (FULL:1909)
  - Intro L86, the same class (R-36)
- **Proof.** Main:608 bounds (C3) by data processing over the whole future, in every faithful realization, Markov ones included. The R-36 example (X3=X0, rest i.i.d.) shows Theorem 2(c) does not give it.
- **Status.** Lean-checked: `c3_necessity` (C3Necessity.lean:80).
  - Hypotheses: `[Nonempty H] (R : Realization Hist V H) (L : ℕ)`, with `step : V×H ≃ V×H` and `w` an arbitrary normalized law.
  - No C4, mixing or Markov hypothesis appears.
  - The time-t identification is on paper.
- **Replacements.**
  - Main:78: "Dependency — C3 holds in every faithful realization, with or without C4: the whole visible future is a function of (X_t, H_t), so data processing gives log₂|C_H| ≥ I* (kernel: `c3_necessity` in `OIBridge/C3Necessity.lean`)."
  - Main:72: "(C1) follows from (C4) in any faithful realization, (C3) holds in every faithful realization, and (C2) is a physical-regime premise."
  - Main:620: "and (C3) holds in every faithful realization by data processing applied to the whole visible future, with…"
  - ch00:37: "C1 follows from C4, C3 holds in every faithful realization, and C2 is…"
  - ch01:133: "with C1 its consequence and C3 a capacity bound that holds in every faithful realization, and C2…"
  - ch01:201: "C4 coincides with the non-Markovianity clause, C1 follows from it and C3 holds in every faithful realization"
  - ch07:30: "since C1 follows from C4 and C3 holds in every faithful realization, verifying those two does not supply it either."

### S-2. New SC-17 sites: Bell summaries that omit read/write locality, readout distance or "±1 in every run"

- **Sites:**
  - Main:22 ("…keeps the pointwise cone and a setting-independent pre-setting ensemble is a local hidden-variable model"), :558, :646, :770
  - ch00:55 (FULL:291; SC-4 edited it but omitted two conditions)
  - ch03:162 (FULL:1038)
  - ch18:110 (FULL:4928)
  - ch04:92 (FULL:1211)
  - Methodology:411
  - Intro L136 (R-39)
- **Status.** Paper proof. The 16-table check 11 is an exact computation, but its controls are vacuous (SC-13).
- **Replacement pattern:** "setting interventions that each read and write only their own wing, ±1 outcomes recorded in every run from readout regions outside the remote setting's graph cone, and a setting-independent response-relevant pre-setting variable".
- **ch00:55.** Insert before "and the wings lie outside…": "the interventions each read and write only their own wing, a ±1 outcome is recorded in every run,".

### S-3. Structure :1180, :1190, :1256 credit recurrence-scale P-indivisibility to C4

SC-3 fixed :1141 and :1147 but missed these three, and #951 does not touch Structure.

- **:1190:** "OI proves the latter at recurrence scale for a fixed finite reversible representative with a non-permutation rooted map, which C4 supplies and every non-deterministic visible step also supplies;"
- **:1256:** "…is proved in OI here only at recurrence scale, for a fixed finite reversible representative with a non-permutation rooted map (which C4 supplies)."
- **:1180:** "OI supplies those extra ingredients for a fixed representative: C4 for the retained correlations, and, for indivisibility, finite recurrence with a non-permutation rooted map, which C4 supplies and every non-deterministic visible step also supplies;"

## UNDERSTATEMENT

### U-1. Main:139: a composition step cited as on paper is Lean-checked

Main:139 says "its composition with P-divisibility … proved on paper", and the LEDGER row reads "P / no Lean statement".

- **Lean-checked:** `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon.lean:148).
  - Hypotheses: `(R : RootedRealization V H) (hsn : s < n) (hI : rootedMap R n = 1) (hab : a ≠ b) (hax : 0 < rootedMap R s a x) (hbx : 0 < rootedMap R s b x)`.
  - Conclusion: `PIndivisibleWithin n (rootedMap R)`.
  - Its definitions match Main's: one prior shared by every root, rows for every root, and `PDivisible` stated as Γ t = Γ s * Λ with Λ stochastic.
- **On paper:** non-permutation ⇔ overlapping rows, and the step from trajectories to a non-permutation rooted map.
- **Proposed parenthesis:** "(kernel: the lemma is `isPermMatrix_of_stochastic_inverse` in `OIBridge/EquivalenceChain.lean`; the composition with P-divisibility, in overlap form — two distinct roots with positive mass in a common column of Γ_s and Γ_n = I with s < n give failure of P-divisibility on {0,…,n} — is `pIndivisible_of_rooted_identity_return_of_overlap` in `OIBridge/RecurrenceHorizon.lean`, for a bijection with one prior shared by every root; that a non-permutation stochastic matrix has two such rows, and the step from two positive-probability histories with a common endpoint to a non-permutation rooted map, are proved on paper)".
- **In the same commit:** set the LEDGER row to K2 with these names and add a census anchor for the recurrence-horizon family (§A.35).
- **Coordinator's note.** The R7-RCH guard in `verification/lean/edge_rigidity_probe.py` currently forbids citing RecurrenceHorizon in any manuscript (the family is registered kernel-only). U-1 therefore requires a governed change to that guard and to the census registry, not a manuscript edit alone.

### U-2. A LEDGER note on the intervention dilation contradicts its probe

The note says `lg_comb_probes` shows the comb "does not by itself reach quantum instrument statistics". The probe reproduces the Leggett–Garg statistics exactly (K=3/2), and what remains is the instrument algebra.

- **Command:** `python3 -I -B papers/oi_lattice_code/foundations/lg_comb_probes.py`
- **Proposed note:** "…shows the comb reproduces quantum instrument outcome statistics exactly, Leggett-Garg violation included; what it does not supply is the instrument algebra, which repconsistency names as the remainder."

### U-3. Main:624: "neither is formalized in the kernel"

The (C3) leg is formalized, as `c3_necessity_and_capacity`.

- **Fix:** append "; the (C3) leg is the kernel's `c3_necessity_and_capacity` in `OIBridge/C3Necessity.lean`".

## DOCUMENTATION

- **D-1.** The LEDGER marks hidden memory and C3 as K3, while Main:604 says the time-t identification is not formalized. Use K2 with that delta, or drop the caveat.
- **D-2.** 21 LEDGER `line` fields for Main are 16 lines stale after #950 (matching is by fingerprint, so the checker passes).
- **D-3.** CI runs none of the probes cited as "certified" for the edited theorems. All of them pass locally.
- **D-4.** Main:648 and :724 cite "(§3.3)" for a chaotic-mixing decorrelation argument that §3.3 does not contain.
  - :648: "(§3.3 retains measurement independence as a posit)"
  - :724: "that may motivate the laboratory setting/preparation decorrelation §3.3 posits"
- **D-5.** Main:578: add "in exact arithmetic" after "closed at the stated accuracy".
- **D-6.** Main:212: "before two cones meet" should take the SC-4 form: an intervention reading and writing only A cannot alter, k updates later, a region R with d(A,R)>k.
- **D-7.** The LEDGER ε-form assumptions should add "exact-arithmetic registers over the instruments' entry ring (the finite-b form is open)".
- **D-8.** The LEDGER process-dilation row lists no Lean check, although Main cites `S_imp_D` and `exists_perm_extending`. `S_imp_D` covers only the correlated-initial-law form. Suggest K1 with "independence of μ_H on paper".

## No finding

- SC-2 propagation.
- The SC-4 cone and speed text: "spacelike" no longer occurs in papers/ or book/.
- Kernel citations near the edited theorems: every identifier is cited no more broadly than its hypotheses allow (`c3_necessity_via_hidden` is correctly marked "for bijective realizations").
- The ε-form checks 14–16 are described accurately.

## Introduction (4a260ca9), by audit item

### R-08 (SC-2)

- **I-1, L56.** "For every law, a realization whose hidden prior is independent of x₀ also exists [Main §3.4, Theorem (finite-horizon process dilation), for rational conditional kernels, and its Extension (arbitrary kernels — the response-table form)]; it is proved on paper, with an exact probe on one rational instance." R-08's proposed citation uses the old label "(arbitrary priors …)".

### R-36 (SC-3)

- **I-2, L12.** "(each with steps not machine-checked)"
- **I-3, L82.** "a pair of posteriors, of positive-probability histories ending at the same x_t, with different pushforwards"
- **I-4, L86.** "(C1) follows from it, (C3) holds in every faithful realization by the capacity bound above, whether or not (C4) holds, and (C2) is a physical-regime premise"

### R-37 (SC-3)

- **I-5, L12.** "…finite recurrence forces stochastic indivisibility somewhere in the recurrence cycle whenever some rooted map is not a permutation, which history readback ensures and every non-deterministic visible step also ensures"
- **I-6, L90.** Define Γ_t "with a row for every x₀ ∈ C_V, roots of visible probability zero included, under one hidden prior shared by every root".
- **I-7, L92.** "with a hidden prior shared by every root"
- **I-8, L96.** R-37's text, plus: "With a full-support visible prior, indivisibility somewhere in the cycle holds exactly when M_k>0 at some order k below the recurrence time, and every law with a non-deterministic step meets it, including laws that are Markov on every accessible window; an observer sees the memory only at an accessible order, which is what (C4) asserts [Main §2.3]."
- **I-9, L185 (FALSE; new, supersedes R-33/O-4).** Open problem (2), "whether the minimal hidden predictive memory equals M_t once … quotiented", is answered by SC-3 claim 3. Delete it, and add after L84: "Over deterministic completions the least hidden predictive information I(X<t;H_t|X_t) is I(X<t;X>t|X_t), attained by the canonical predictive quotient, and it equals M_t exactly when I(X<t;X>t+1|X_t,X_t+1)=0; over bijective realizations it is H(X<t|X_t) for every law, Markov laws included (proved on paper; the lower bound machine-checked for bijective realizations as `c3_necessity_via_hidden`) [Main §3.4, Remark (a variational question)]."
- **I-10, L189 and L12 (overlaps R-24).** "…the discriminating content lies in readout-relevant memory, which every faithful realization carries in its hidden state exactly when the visible law has memory"

### R-39 (SC-4)

- **I-11, L136.** "A deterministic completion is Bell-local, |S_CHSH|≤2, when each setting intervention reads and writes only its own wing, each wing's ±1 outcome is recorded in every run from a readout region outside the other wing's setting cone, and the response-relevant pre-setting variable is independent of the settings [Bel64; CHSH69; Main §3.3]; a deterministic completion reproducing quantum Bell correlations must give up the first two conditions or the third. The framework retains measurement independence as a posit about the initial condition and adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting; whether this is compatible with operational no-signalling and with the gravitational continuum limit of the substratum's spatial coupling graph is the open hypothesis H-Bell [Main §3.3]."
- **I-11, L168.** "with measurement independence kept as a posit". R-39's "(settings and readouts local)" omits d(B,R_A)>k_A.

### R-40 (SC-1)

- **I-12.** The Introduction has no ε-realization text yet. R-40's three replacements agree with Main after SC-1. Also amend R-07's "needs a program register that grows exponentially with K", since Main:576 gives only an upper bound: "uses a program register of up to Θ(|O_max|^K log₂|F|) bits for an arbitrary adaptive policy".
