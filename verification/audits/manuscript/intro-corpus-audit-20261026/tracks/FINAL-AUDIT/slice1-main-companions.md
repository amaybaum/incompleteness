# Final consolidated audit, slice 1: Main and the companion papers (main `55e3217b`)

Independent, read-only check, in a detached worktree since removed. It covers Main and nine companions: Substratum, GR, SM,
Structure, Complexity, Computation, Medicine, Bioinformatics and Methodology. Line numbers are at `55e3217b`.

The coordinator re-read D-0 and D-1 at `55e3217b` and confirms both.

## A. Main's claims
- All 61 Lean identifiers cited in Main resolve in `verification/lean-mathlib/OIBridge/`.
- `fiber_freedom` (:616) is a probe check name, not a Lean identifier.
- Every cited probe exists. Six were re-run (memory, primitive, translation, review4, sdq, equivalence_recovery); each
  passes and reproduces the counts quoted in the text.

**Supported at the stated scope:**

| Area | Sites |
|---|---|
| Finite-horizon S⇔D⇔Q_fb, with both directions witnessed | :16–18, :98, :542–548 |
| Hidden-memory theorem, with the joint-law and vanishing-criterion steps disclosed | :20, :596–608 |
| Stochastic-inverse lemma and the recurrence theorem; Scope equivalence | :133–141 |
| §2.3 non-permutation theorem; readback lemma; one-step dilation | — |
| Phase-locking lemma (conditional on H-BG) | — |
| Reverse one-step lemma (SC-18 scope intact) | — |
| Lemma 2, separability threshold and corollaries, with both directions in Lean | — |
| CP-indivisibility scope | — |
| Bell ceiling (SC-4 intact) and graph-cone corollary | :360–419 |
| C2 quantitative bound; physical-memory theorem in two forms | :449–467 |
| Comb dilation | — |
| C3 necessity and capacity bound, unconditional | :500–510 |
| Process dilation (SC-2 intact) | — |
| Fixed-Ĥ form | — |
| Characterization theorem, (C2) outside (iii) | :532–538, :624 |
| ε-gluing (SC-1 intact) | :560–594 |
| OI⁺ ⇔ finite operational QM | :582 |
| Quasilocal uniqueness | :584 |
| Passive observation | — |
| Predictive quotient | :616 |
| Variational infimum (SC-3 intact) | :99, :610 |
| §4.6, as scoped by SC-21 | :742–758 |

**Overstated or unsupported:** :86–92, :151, :660–670. See D-1, D-2 and D-14 below.

## B. Regression sweep, classes corrected by #947–#955
- **No surviving instance in Main or the companions:** SC-1, SC-2, SC-3, SC-4, SC-18.
- **SC-16: surviving instances** at Structure :31, :90, :752, :836, :903, :1306; Complexity :484, :490, :492; Substratum :129;
  Main :696, :730; Bioinformatics :138. All are listed under D.
- **SC-20: stale sites** at Main :99, :652 and Substratum :129. GR :20 says ETH "holds".
- **SC-21:** scoped everywhere. Main :165 belongs to SC-23.

## C. Known open items, current text confirmed
| Item | Current state |
|---|---|
| SC-23 | Main :159–161, :165, :439, :445 and :754 are unchanged |
| SC-17 | Bell summaries at Main :22, :646, :770; Substratum :417; Methodology :385, :389, :391; Structure :1149 |
| SC-19 | Main :72, :78, :620; also Substratum :137, where C3 sits under the mixing conditional |
| SC-22 | absent from the papers; it is book-only |
| Main :74/:143 vs appendix-b :418 | now consistent |
| ch04 :178 | the rate condition is still missing |
| appendix-c :102 | still "is lost" |

## D. New findings, ranked by severity

### High
- **D-0, Medicine :25.** The text says OI "proves that the description of any embedded observer with partial access to a
  deterministic system is necessarily non-Markovian — quantum … under (T)". This contradicts Main :172 (C1–C3 without readback
  give noise), :612–614 (Markov laws are realizable) and :548/:652 (the representation is internal and universal, not
  conditional on (T)).
  - Proposed: "proves that an embedded observer's finite observable law has an exact fixed-basis unitary/Born
    representation, and that this law is non-Markovian exactly when history readback (C4) holds at an accessible order".
- **D-1, Main §3.5 :660–670.** The rest-frame "iff" proves only one direction.
  - The proof's step "spatial rotations fix n and so are [invariances]" treats a necessary condition as sufficient. What
    follows is only that the invariance group is contained in Stab(n) ≅ O(3).
  - :670, "rotational invariance … and rest-frame selection are the same fact", conflicts with :658 and :674, where
    isotropy is an input.
  - Substratum :329 mirrors the claim.
  - Proposed:
    - state the lemma as "the invariance group of T within O(3,1) is contained in Stab(n) ≅ O(3); boosts are excluded;
      which rotations are invariances is fixed by the substratum";
    - keep the converse as a one-way statement;
    - drop the boxed biconditional and the "same fact" sentence;
    - at Substratum :329, write "are not excluded by the partition; spatial isotropy enters as an empirical input".

### Medium
- **D-2, Main :151.** "By Poincaré recurrence … measure > 1−δ for any δ" is false for general Hamiltonian flows. Recurrence
  gives positive-measure return, and a mixing flow gives μ(A∩φ₋ₜA) → μ(A)².
  - Proposed: the discrete §2.3 theorem applies to a finite discretization. For a continuous flow, near-identity return in
    measure must be assumed; it holds for quasi-periodic flows and fails for mixing ones.
- **D-3, Substratum :129 and :137.**
  - :129 calls C2 conditional on mixing, with the "divisibility deficit (k−1)ε" and "P-indivisibility on accessible
    timescales forces τ_S ≪ τ_B". This contradicts Main :461, :465 and :736.
  - :137 places C3 under the mixing conditional (SC-19 class).
  - Proposed :129: "C2's persistence form holds without further hypothesis (Main §3.4); its slow-bath form is conditional
    on the quantitative mixing hypothesis, under which departure from the homogeneous Markov benchmark obeys (k−1)ε;
    without it, accessible conditional memory does not bound the bath's mixing time."
  - Proposed :137: state C3 separately, as unconditional.
- **D-4, Structure :31, :90, :752, :836, :903, :1306.** These say "P-indivisibility transports directly", "confirmed" by
  Mehl–Gröblacher, or a "holographic analog of P-indivisibility". The paper's own §14.3 says P-indivisibility is not
  established across frameworks.
  - Proposed: "hidden memory (non-Markovianity); P-indivisibility not established cross-framework".
- **D-5, Main :696.** "observed Bell-class dynamics — indivisible, hence non-Markovian a fortiori — certify (ii) directly"
  contradicts :74, :628 and Substratum :109/:123.
  - Proposed: (ii) is certified by directly observed memory effects; Bell data constrain the spatial-composite branch.
  - Scope :620 to the adopted ontic-parameter-dependent branch.
- **D-6, Main :176.** "The §3.4 necessity proof for (C2) establishes this formally", applied to the P-divisibility of
  Jaynes–Cummings and Davies–Merkli. Those theorems bound conditional memory in the classical coupling-step model, not
  P-divisibility. Proposed: "consistent with … does not by itself establish P-divisibility".
- **D-7, Complexity :484, :492, :490, :394, :370.**
  - :484 and :492 assert P-indivisible design and dynamics, contradicting the paper's :478.
  - :490 states unconditional "backflow".
  - :394 says the application "follows from the same characterization theorem", contradicting :362.
  - :370 reads the readback lemma's lower bound as a magnitude.
- **D-8, Bioinformatics :138.** "no method using only scRNA-seq data can recover the true causal GRN … This is the
  structural content of P-indivisibility". The claim is misattributed, and it strengthens a prediction into an impossibility.
  - Proposed: attribute it to the hidden-memory theorem, as an expectation.
- **D-9, Main :99 and :652.** Both give C2 as one form: "conditional on mixing" and "ETH-conditional C2 bound". Proposed:
  the two-form statement.
- **D-10, GR :20.** ETH "holds for the horizon complement" → "is the standard assumption for".
- **D-11, SM :1211.**
  - "by P-indivisibility (Main Theorem 4), the stationary distribution is unique" is false: for a bijection, the uniform
    measure on every orbit is invariant, so uniqueness needs a single cycle (cycle ergodicity, gap (i)).
  - Main has no "Theorem 4".
  - Proposed: make the step conditional on cycle ergodicity.
- **D-12, Main :710 (§4.4).**
  - The paragraph claims the type II structure "as a consequence rather than a postulate", "structurally forced"
    cancellation, and an AAIL formula match. None of this is derived anywhere in the corpus.
  - It also contains evidential-weight sentences (§A.32, §A.23).
  - Proposed: restate as parallels only, saying that type II is not derived here, and delete the weight sentences.

### Low
- **D-13, Main :109.** "By (C1) … imprints on the hidden sector": C1 is hidden-to-visible influence. Unqualified "(C2)"
  there means C2-slow.
- **D-14, Main :86 and GR :20(ii).** The partition-relativity lemma claims dependence "only on the geometric and
  thermodynamic properties of the partition boundary". The proof gives dependence on (φ, partition, μ).
- **D-15, Main :730.** "(ii) ⟹ (i): P-indivisible ⟹ …": clause (ii) is non-Markovianity.
- **D-16, Main :131.** The §2.3 theorem is said to "require only … (C1)"; its hypothesis is a non-permutation T. Proposed:
  scope it "(C1), under the uniform hidden prior that defines T", as Main :151 now has. Check whether SC-16 left a residual
  here.
- **D-17, Main :716 and GR :589.** The characterization theorem is said to require the stochastic–quantum bridge and
  genericity conditions. It uses neither.
- **D-18, Main :584.** The equivalence cites only the forward witness. Add `qm_generated_by_substratum_extension`
  (`StructuralClosure.lean:423`).
- **D-19, Main :250 vs :246/:254.** Contradictory certification status for the (3,3) and (4,2) shapes. Check against
  `phaselock_probes`.
- **D-20, Main :640.** "(exact computation)" with no named probe or kernel.
- **D-21, Main :48/:62 vs :700.** Lemma 1 is called "a theorem" though its justification is the argument §4.3 calls
  circular.
- **D-22, Main :336.** "conditions (C2)–(C3)" for frozen-bath → "(C2-slow)".
- **D-23, Methodology :13.** "derives the Standard Model gauge structure … from a single starting point" omits the E1–E7
  inputs and named hypotheses.
- **D-24, SM :112.** P-indivisibility "for any L and q" without a non-permutation rooted map shown.
- **D-25, GR :591.** "restoring P-divisibility would require decoupling the sectors entirely" holds only over the
  recurrence cycle with a full-support prior.
- **A-5, Main :20.** The abstract's "as late as one step before recurrence" has no in-text witness. An exhaustive probe at
  (2,2), (2,3) and (3,2) found only L = 2 instances.
- **A-12, Main :242–244.** The ancilla-marginal "iff" has no displayed proof. It is verified algebraically, but §A.34
  needs one line.

**Mirror risks for slice 2:** D-1 (ch19 :240 and FULL :5400), D-0, and the D-12 paragraph.
