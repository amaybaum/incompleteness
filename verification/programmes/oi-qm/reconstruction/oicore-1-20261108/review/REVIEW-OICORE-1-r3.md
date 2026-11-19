# REVIEW-OICORE-1-r3: independent re-review of OICORE-1 r3

**Reviewed file**

- `OICORE-1.md` (r3), sha256 `93156b287c3349be7e3fead75726609224ea3fdd3cf9f61fcec9aab34e585d78`. I re-hashed it
  before the review. It has 663 lines.
- r1 (`ed828f16…88da6`) and the final r2 (`dbeca5b4…6477d`) hashes were confirmed. Line numbers below refer to r3.

**Snapshot.** `origin/main` = `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`. Every Lean, record and paper citation used below was
re-read at that commit. No Lean build was run, and nothing beyond trivial arithmetic was computed.

**Governing text.** I read these from GitHub and checked them against DIR4-1169.md and the quotes in r3:

- #1169 c.6724721208 (the four distinctions; amaybaum, 17:31:47Z);
- c.6724620166 (the strengthened hierarchy; 17:22:38Z);
- c.6724668737 (the backward dependency map; 17:27:00Z);
- c.6723277401 (the M-ARC quote).

Every verbatim owner quote in r3 matches its source: §0 lines 29-36, §5(f) lines 359-361 and §4 line 301.

**Standing.** This is a model-written, read-only review. It is not human verification.

## Verdict: **REVISE**

r3 is a substantial improvement.

- Lemma I and the recast Lemma M are correct.
- The universal/existential split, the ACC-U/M-INACC separation, the F3 recast, the V cell, the hierarchy table and the dependency map
  are sound in substance.
- All twelve r1 nits are fixed.

Six blockers remain:

- four concern the owner's new requirement to separate "proved unable" from "not shown" and to keep exact apart from approximate (R3-B1
  to R3-B4);
- one concerns the synthesis (R3-B5);
- one concerns §A.42 item 8 (R3-B6).

All six can be fixed in the text.

## Verified (no change needed)

1. **Lemma I** (lines 197-205) **is correct.**
   - Every field of `FiniteOperationalTheory` apart from the readout (OperationalAssembly.lean:594-653) is a Horn-type closure rule:
     - the two existence axioms: `avail_id`, `prepAvail_uniform`;
     - the five closure rules: `avail_coarse`, `availExt_coarse`, `availExt_bind`, `prepAvail_post`, `prepAvail_discard`.
   - So the pointwise intersection satisfies each of them.
   - `readout_is_localLuders` makes all readouts equal, so `readout_avail` and `readout_local` transfer.
2. **Lemma M** (lines 207-219) **is correct, with its hypothesis stated and used.**
   - Downward closure is stated as closure under shrinking `avail`, `availExt` and `prepAvail`. It is used exactly once, at step 3
     (`T₀ ⊆ T₁`).
   - Intersecting with `permTheory (Fin 2)` preserves realization of the core. `σ̂` and `τ̂` are available in `permTheory`
     (`permTheory_relabel`, SubstratumInterfaceAudit.lean:730; `permTheory_realizesSealedOICore`, :741) and in `T₁`. F1 then supplies
     the other four conjuncts for every theory.
   - `DenseUnitaryControl` (DiscreteCompletion.lean:45-48) is upward-closed, as `HasCompositeUnitaryControl` is.
   - `permTheory_dense_ceiling` (FrozenSourcing.lean:187-188) and `permTheory_not_control` (:708) give the conclusion.
   - The applicability notes are correct. Lemma M is withheld from ACC (line 232). The FIN_op witness is sound: by `NonnegBounded`
     (FrozenSourcing.lean:65-67, 79), an available unitary conjugation must preserve nonnegative entries, which forces `V` to be a unit
     scalar times a permutation, and these are countable up to scalar [A].
3. **The FIX_op ⇒ V cell is EI and correct.**
   - `permTheory_sourcedOI` gives reversible implementation locality.
   - `implementationLocality_of_reversible` (MicroscopicReversibility.lean:227-230) and `validity_of_implementationLocality`
     (ImplementationLocality.lean:971-974) give validity.
   - `CompositeOperationalValidity` is a ∀-available predicate, so it is inherited downward.
   - I is a ∀∃ predicate (SpectatorBridge.lean:223), so NS is right.
4. **The dense route** (lines 412-421, 477) **is sufficiency-only and `Fin 2`-only, as claimed.**
   - `DenseUnitaryControl`, `FixedGateSourced`, `KrausDense` and `DenseFiniteQM` are all stated on `FiniteOperationalTheory (Fin 2)`.
   - `denseUnitaryControl_of_fixedGate` (:1522) takes `DerivedOI`, `Irrational (α/π)` and `FixedGateSourced α`.
   - `denseFiniteQM_of_denseControl` (DenseInstrumentBridge.lean:496-498) keeps soundness as its own hypothesis.
   - No converse exists. `fixedGateTheory` is dense and not QM (:1940-1947).
   - `DerivedOI`'s phases are "stipulated, not derived from the stated access" (RouteB.lean:141-145).
5. **The cos α = 3/5 / Niven claim** (lines 537-539) **is correct.**
   - By Niven's theorem, the only rational values of cos at rational multiples of π are 0, ±1/2 and ±1. So α/π is irrational.
   - Equivalently, `(3+4i)/5` is not a root of unity (control RC-1: its minimal polynomial `5x²−6x+5` is not monic).
   - The sign convention does not matter: irrationality holds for ±α. See nit R3-n2 on the citation.
6. **The hierarchy facts check out.**
   - `oiPlusMin_iff_qm` holds in both directions on every nonempty carrier (MinimalRepertoire.lean:544-570).
   - `PhaseFreeRichness` drives one pair per level and makes every exchange available (:423-428).
   - `flow H t = exp(−itH)` (ReachabilitySeam.lean:95-96), so §8.2's `diag(−i, −i, 1, …)` computation is right.
   - `ElementaryTransitionRichness` is a conjunction of availabilities, including `phaseGate` (LieRankSource.lean:436-441). So the R-1
     discrepancy with completion-assumption-audit.md:64-66 is real.
   - The idle `DaggerStable` (MicroscopicReversibility.lean:227-230) is confirmed.
   - `git grep` finds no "OI†", `OIDagger` or `OI^†`.
   - `substratum_residual` (StructuralClosure.lean:383-386) and `substratumClass_not_drivesElementary` (:370) are as stated.
   - `driveQ_isContinuousPath` asserts no group law (SecondOrderDrive.lean:37, 221-225).
   - `monomialSource_not_control` is not vacuous. `IsMonomial` (SubstratumInterface.lean:75-76) absorbs unit scalars, so the #1188
     pattern does not arise.
7. **§A.34.** Every displayed ⟺ has a kernel witness for each direction:
   - F1;
   - the `general_characterization` / `exactAll_iff_substantive` line of §8.4;
   - `oiPlusMin_iff_qm`;
   - `qm_iff_derivedOI_pairFlowSourced`.

   The dependency map uses one-way ⟸ arrows and labels the dense row sufficiency-only.
8. **The r1 findings.**
   - B2, B3 and B5 are fixed in substance.
   - B1 is fixed apart from R3-B1 below.
   - B4 is partly fixed (R3-B4).
   - B6 is partly fixed (R3-B6).
   - N1-N12 are all fixed.

## Blockers

**R3-B1. The access exclusion is presented as "proved unable", but its hypothesis may be unsatisfiable and its dense form is not a defined
predicate.** Lines 177, 244, 299, 324, 328, 513.

- *Satisfiability.* No core-realizer satisfying ACC_op is exhibited. The draft itself says so (line 232: "no witness is exhibited";
  OICORE-F2, line 374). If no core-realizer satisfies ACC_op, then "ACC_op excludes control" holds only vacuously, and the real finding
  would be that the core and ACC_op are inconsistent.
  - This is #1188's own assumption-watch ("a no-go whose hypothesis quantifies over … needs a satisfiability control").
  - The owner asked for the access negative to be kept "with its exact hypotheses". Its non-vacuity is one of those hypotheses.
- *Definition.* "Any non-law relabelling moving `h` into `V`" (line 177) is imprecise. `τ` is the observer's control, not the law, and
  `τσ` moves `h` into `V`. A precise downward-closed form: *every relabelling `g` of `Core` whose transported channel is available at
  level 4 lies in ⟨σ, τ⟩*.
- *Dense form.* ACC_op^δ ("no available instrument *not containing `σ̂`* identifies `h`…", line 177) is not a predicate on `T`.
  Availability is a set of families, and "containing `σ̂`" names a protocol, not a family. The dense CX in line 244 ("A, sketch"), line
  328 ("Excluded for … ACC_op") and line 513 ("dense (A sketch)") therefore has no well-defined hypothesis.
- *Fix.*
  - State ACC_op precisely.
  - Keep "CX, exact", with the hypotheses (i) `coreIdx`, (ii) the R2 reading, and (iii) *consistency of ACC_op with `OICore` not
    exhibited (open, OICORE-F2)*.
  - Note that the implication is definitional: control makes every unitary available, so it makes `g_hb` available.
  - Reclassify the dense cell as NS until a predicate-level ACC^δ is stated.

**R3-B2. "CX" is used for existence principles that are merely not shown to give control. This is the owner's "not shown" versus "proved
unable" distinction.** Lines 252, 518.

- EMB is an existence principle that QM also satisfies (`embeddedObservation_of_qm`, EmbeddedObservation.lean:327). The two witnesses —
  `permTheory` (EMB, no control) and `lieRank_not_redundant` (LieRankSource.lean:156-162: reversible implementation locality and EMB
  without `LieRankRichness`) — show only that EMB does **not imply** control.
- EMB does not *exclude* control. That fails line 78's own definition of CX ("excluded within a stated class"). §8.6 line 518 repeats the
  error ("CX as a source (exact)"), as does its dense entry.
- *Fix.* Add a class **NI-W** (not implied: witness exhibited) and use it for EMB in both places. Keep CX for class-confinement results:
  FIX_op ⊆ `permTheory`, the monomial read-write class, and CERT inside Theorem NC's scope.

**R3-B3. A `Fin 2` kernel result is stated without its carrier, and its kernel label is attached to a statement it does not make.** Lines
366-367, 495, 545, 631.

- *Carrier.* `DenseUnitaryControl`, `nonnegBounded_not_denseUnitaryControl` and `permTheory_dense_ceiling` exist only on
  `FiniteOperationalTheory (Fin 2)` (DiscreteCompletion.lean:45; FrozenSourcing.lean:173, 187). §3.3 tags them "K, `Fin 2`" (line 261).
  But four other places say "on the physical carrier … (K)" without the carrier. #1188's owner decision forbids broadening a two-state
  result into a general one without further proof.
  - A carrier-general form is available at the paper level: `NonnegBounded` is carrier-general (FrozenSourcing.lean:65-86), and the
    limit argument does not depend on the carrier. That form is A, not K.
- *Label.* The kernel proof refutes dense control through the quarter phase (`phaseGate_not_preservesNonneg`, FrozenSourcing.lean:177). So
  "approximate coherent **mixing** is proved unable (K: …)" (lines 366-367) is not what the kernel states. The mixing statement — no real
  rotation is approximable — is a one-step corollary through `preservesNonneg_of_approx`, and it is A.
- *Fix.* Write "K on the `Fin 2` system carrier, every ancilla level; carrier-general and mixing-specific forms A" at each of the four
  places.

**R3-B4. The "open part is narrower than stated" claim (§5(f) item 2) is not accurate as stated.** Lines 366-368.

- It uses results from two levels the owner's distinction keeps apart, and it presents unverified results as proved.
- *Cross-level.* The owner's open statement concerns "genuinely nonclassical, **approximately** quantum operations". Two of the three
  narrowing items are about something else:
  - "The exact form is proved unable for every countable mechanism" is an exact result. Using it to narrow an approximate question is what
    DIR4 forbids: "We must not use an exact-control obstruction to dismiss an ε-level construction."
  - The physical-carrier dense ceiling concerns configuration-level operations. The owner's question concerns effective (encoded)
    operations; c.6724668737 speaks of "effective" operations reached "through discrete microscopic dynamics, hidden-state interactions
    or an observer-dependent protocol". So the ceiling removes a case nobody proposed.
- *Status.* The one exclusion that bears on encoded approximate operations rests on U2 [W] and Theorem C [D]. Under §A.46 item 7, a W
  record cannot convert an open question into "proved unable". A D draft off `main` cannot either. The same over-promotion appears in
  lines 495 and 632 ("*proved unable* on encoded carriers within U2 [W] and Theorem C's affine scope [D]").
- *Neutrality.* "Narrower than stated" reads as a correction of the owner. The evidence supports a locating statement, not a correction.
- *Fix.* Replace item 2 with: "Within the open question, these sub-cases are already excluded:
  - exact control, for every countable mechanism (K on `Fin 2`; A in general);
  - dense control on the configuration-level carrier (K on `Fin 2`);
  - encoded gates within U2's scope (W) and Theorem C's (D), conditionally on those unverified records.

  Beyond these, the question stands as the owner stated it."

  Make the matching change at lines 495 and 632: "excluded, conditional on W / D".

**R3-B5. The synthesis headline is contradicted by its own list.** Lines 563-586.

- *The headline.* "Every ε-route shifts the missing assumption rather than discharging it" (line 569) generalizes a four-item list to all
  ε-routes, which is a finite-to-universal step.
- *The contradicting item.* The list's third route, the horizon-limited gate (lines 575-576), is called "compatible with OI". It needs
  only:
  - a mathematical bridge theorem (OICORE-F6), which is a missing theorem, not an assumption about nature;
  - the existence of a native mechanism, which is open, not assumed.

  Read as an exactly available gate of finite order larger than the accessible horizon, it is not excluded by §8.7(c) row 2, which
  excludes only exact *infinite-order* gates. It is also the second disjunct of ENC-G (line 593). A route that is consistent with the
  axioms and open on both counts is an open route, not a shifted assumption.
- *The prior sentence.* "It does not remove the requirement … infinite-order coherent gate" (lines 566-567) holds only relative to the
  existing dense theorem. Under an F6-type bridge the infinite-order requirement would change. The sentence should say "under the
  existing theorems".
- *Fix.* Answer the owner's question by route:
  - Growing systems or an ε-indexed rule family, an infinite world or open supplies, and a free ε each move the gap into a new hypothesis.
    That is a shift.
  - The horizon-limited finite-order gate in one fixed finite world is compatible with the axioms. It is not shown to be a shift, and it
    is open on two named counts: F6 and a native mechanism.
  - So, as far as these routes go, the approximate-versus-exact distinction does expose one route that is consistent with OI and not yet
    closed, alongside three that shift the assumption.

  The gap table (lines 582-586) should split the "ε / horizon-limited / growing" row to match. This is the fair classification of the
  horizon-limited route.

**R3-B6. Residual §A.42 item 8 gaps.** Lines 395-400.

- **Theorem C [D].** Line 395 says "No conclusion here depends on it beyond that label; the same cells stand on U2 [W]". That is not
  accurate:
  - §8.7(c) row 4 (line 548) stands on Theorem C alone. Its hypotheses (affine rules, P1, P2/N2) differ from U2's (`q = 2`, R1^⊗n,
    H-LIFT).
  - The boundary of the open region in §5(f) item 2 and §8.10 depends on it.

  "Kept by coordinator direction" does not close a gap. Under item 8 only a recorded owner decision can land an unclosed gap, and the
  record must quote it with author and time.
- **ACCESS Prop. F0 [D].** Line 396 says it "carries no general conclusion". But §5(c) (lines 341-342) concludes from it: "So ACC-U is not
  sufficient by itself." A counterexample does support that conclusion logically, but the support is off `main`.
- **Relayed directions** (line 400: "no comment id yet"). They are now recorded as c.6724620166, c.6724668737 and c.6724721208. Cite them
  in §0 (lines 31-36, 45) and §7.
- *Fix.*
  - For Theorem C and F0, land the drafts first, or mark both conclusions "draft-conditional" and state the gap.
  - Alternatively, cite a recorded owner decision.

## Nits

- **R3-n1. §8.7(c) row 2's argument** (line 546) does not support its conclusion.
  - The argument is: "Iterating one protocol is periodic, so the induced gate has finite order". But repeated runs act on different
    apparatus states, so the periodicity of φ does not give `G^L = id` for the map one run induces.
  - A sound route to the same conclusion is spectral. If the identification `E` is a linear surjection with `E S = G E` on an
    `S`-invariant preparable span, then `spec G ⊆ spec S`. The unit-modulus eigenvalues of a (sub)stochastic `S` are roots of unity, by
    Perron–Frobenius.
  - State these hypotheses: linearity, invariance, and one fixed induced map.
- **R3-n2. Citation for the gate** (line 538). `mixImage n α` uses `StateMixingCoupling.rot θ` (StateMixingCoupling.lean:45-51), not
  `DiagonalTheory.rot` (:368-371). The latter is the fixed matrix at −α in that convention. Cite the former, with α = arccos(3/5).
- **R3-n3. CTRL is an exception** (line 332). CTRL is a candidate row, and it yields QM (EI, line 251). So "No quantum-selecting property
  … follows from any candidate in the search" needs "other than CTRL (rejected as the target's own resource)".
- **R3-n4. FIN_op exact cell** (line 247) is about control, but `pairFlowSourced_of_qm` is stated from QM, not from control. Its proof
  uses only control, and the cell is trivially A by cardinality. Label it "A over K".
- **R3-n5. The `five_way_minimality` / `oiPlus_independence` row** (line 280). For the control-lacking clause, write "not assessed"
  rather than implying it survives. Its witness was not checked against FIX_op or ACC_op.
- **R3-n6. Interpretation marks.** Two places need *interp.*:
  - "`ImplementationLocality` is FIX with the class left existential" (line 486);
  - "outside OI's axioms" for a continuous coupling (line 519).

  Also scope §8.5's "OI's finite bijective picture does not contain [coherent blending]" (lines 506-507) to the configuration level. Main
  shows ε-level blending in encoded descriptions (with imports, Main:582), so the D1/D4 levels must not merge.
- **R3-n7. Lemma M's dense conclusion is `Fin 2`.** Lemma M's statement already assumes `FiniteOperationalTheory (Fin 2)` through
  `DenseUnitaryControl`. Say so in its statement (line 207).
- **R3-n8. Controls** (line 539). RC-1 is a control, off `main`. Like `c1_core_access.py`, it lands with the record or is dropped.

## Answers to the coordinator's checks

1. **B1-B6 and N1-N12.** All are fixed in substance, except as R3-B1 (B1), R3-B4 (B4) and R3-B6 (B6) describe. N1-N12 are all fixed.
2. **Lemma I and Lemma M.** Both are correct.
   - Intersecting with `permTheory` preserves realization of the core, by F1 and `permTheory_relabel`.
   - The downward-closure hypothesis is stated and used once, correctly.
3. **"Proved unable" traceability.**
   - Exact, countable: sound. It is K on `Fin 2`, and A (cardinality) in general.
   - Dense on the physical carrier: K on `Fin 2` only, proved through the phase (R3-B3).
   - The access exclusion: definitional, with satisfiability open and the dense form undefined (R3-B1).
   - EMB: misclassified as CX (R3-B2).
   - §A.34: fine.
4. **The cos α = 3/5 / Niven claim** is correct. The dense route is sufficiency-only and `Fin 2`-only.
5. **The four distinctions.**
   - D2, D3 and D4 are kept.
   - D1 is breached at §5(f) (R3-B4).
   - The physical and effective levels merge at §8.5 (R3-n6).
6. **The synthesis** is partly rhetorical. The horizon-limited route is unfairly folded into "shifts the assumption" (R3-B5).
7. **§A.42 item 8.** Theorem C, F0 and the relayed ids remain open (R3-B6). The owner quotes match #1169 verbatim.
8. **"The open part is narrower than the owner stated"** is inaccurate and not neutral. It needs restating as a locating statement
   (R3-B4).
