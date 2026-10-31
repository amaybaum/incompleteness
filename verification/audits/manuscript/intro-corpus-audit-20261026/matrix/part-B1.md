# Mapping part B1: I-001 to I-091

**Range.** Abstract, §1.1, §1.2 (with Contributions and Conventions), §2.1, §2.2 and §2.3. That is 91 claims plus 8
directional sub-claims (I-002.a–c, I-011.a–b, I-063.a–c), 99 rows in all, in `part-B1.json`.

**Objects.** The Introduction at `4a260ca9`. The corpus at `eae01647`, from the `tree939` extraction, with
`verification/programmes/**` and the probe sources read by `git show`. The OIBridge sources show an empty
`git diff 17b830bc eae01647`. #939 changes nothing these claims rest on: its edits to `Main.md:684`, `GR.md` and
`glossary.md` concern ħ wording.

**Literature.** EGGH26, Bar23, Bar25, Bar26, Sch21, LP17, BD16 and Dou26 were read from the scratch copies in `S/lit/`.
SGD19 (arXiv:1905.03018v2) was fetched and read for this audit. Milz20 was read first-hand in the earlier
introductory-paper audit and was not re-read.

## Counts

| Verdict | Rows |
|---|--:|
| FAITHFUL | 91 |
| UNDERCLAIM | 1 |
| MISCITED | 1 |
| IMPRECISE | 6 |
| OVERCLAIM | 0 |
| UNSUPPORTED | 0 |

| Proof status (weakest link) | Rows |
|---|--:|
| proved-kernel | 40 |
| proved-paper | 42 |
| open | 9 |
| conjecture | 6 |
| numerical | 2 |

## Checks the caller asked for

- **Theorem 1, one direction at a time (§A.34).** All three directions are proved in the kernel, as stated:
  - S_K ⊆ D_K: `S_imp_D`, Equivalence.lean:422.
  - D_K ⊆ Q_K: `D_imp_Qfb`, :294.
  - Q_K ⊆ S_K: `Qfb_imp_S`, :245.
  - The reverse arrows are compositions, at :466–468.
  - The wrapper `finite_horizon_equivalence`, at :462, takes only `P` as an argument.

  The class definitions match §2.1:
  - `RevReal` has a finite hidden type, a bijection and a correlated initial law.
  - `QfbReal` has a unitary `U`, diagonal initial weights, `read : Bas → V`, and Born weights `‖U‖²` chained at every
    step.

  The kernel needs only `Fintype V`. §2.1's |C_V| ≥ 2 is harmless and narrower than necessary, and Theorem 1's "every
  finite visible alphabet" is the accurate statement. The one encoding to know about: the kernel defines Q_K's
  every-step record by its Born chain formula. That formula is SGD19 Eq. (3), read first-hand.
- **The abstract against the body.** The abstract's results all match the body and the corpus. Two wordings fail:
  - I-010: "one step not machine-checked". The Corollary form has two unchecked ingredients.
  - I-015: "any test of the hypothesis" is broader than the body's sourced claims.
- **"Machine-checked" (I-053).** The definition holds:
  - Commit `17b830bc` exists.
  - Its Lean sources are identical at `eae01647`.
  - `papers/introduction_repro/` records run 40330683786 / job 121598983127, "Mathlib bridge", success, on Lean
    v4.33.0.

  "Machine-checked" certifies each declaration's formal statement. Where that statement is narrower than the prose, the
  Introduction says so: Theorem 2 for a joint law, Theorem 3 in rooted form, and readback from the routed form.
- **The scope of the correspondence (§2.3).** All ten claims are FAITHFUL and sourced to Main:534, :598 and :618, plus
  the kernel.

## Non-FAITHFUL rows, by severity

1. **I-071, UNDERCLAIM (moderate).** "For a law with rational probabilities, a realization whose hidden prior is
   independent of x_0 also exists."
   - Several sources give this form for every finite-horizon law, not only rational ones:
     - Main's Extension (response-table form, Main:498);
     - its status ledger (Main:715);
     - the Characterization theorem's quantifier.
   - The rationality restriction belongs only to the uniform-tape presentation.
   - The Introduction's own attribution, EGGH26 Prop. 16, is also unrestricted (it is not reversible).
   - What is checked where:
     - Main:500 says the independence of the prior is not formalized for the multi-time law.
     - The kernel has the independent-prior response-table construction for rooted families only
       (`RootedClassification.responseRealization`, :330), with no rationality assumption.
     - The law-level Extension is proved on paper, with one exact instance (`review4_probes.py` P-G).
   - Coordinator relay from B5: checked and confirmed.
   - Fix: "…also exists for every law [Main §3.4, Theorem (finite-horizon process dilation) and its Extension
     (response-table form)]; it is proved on paper, with exact probes."
2. **I-052, MISCITED (moderate).** "The results of §3.2–§3.3 are proved in [GR] and [Main]."
   - GR §3.3 states Theorem 4 and the qubit independence, and Main:624 states the lift results. Neither writes a
     proof.
   - The proofs are the OIBridge declarations: GeneralCarrier, RankGapTheory, CoherentLiftGauge and TrackBQfbBridge.
     The proof inventory lists GR:218 as kernel-only.
   - Fix: "…are stated in [GR §3.3] and [Main §3.4] and proved in the Lean declarations of Appendix A."
3. **I-042, IMPRECISE (moderate).** "Proofs, the status ledger and the probe code are in [Main]." The proofs are spread
   over GR §3.3, BHa/BHb, GR App. A and OIBridge, as the Introduction's own citations show. The fix is in the JSON.
4. **I-054, IMPRECISE (moderate; it affects status labels in §2.4).** The convention defines an "exact probe" as an
   *exhaustive* exact-rational computation.
   - Line 56's probes (`process_dilation_probes.py`, `review4_probes.py` P-G) are exact, but they check named instances
     rather than every law in a class.
   - Line 84's probe (`c4_backflow_probes.py`) computes the CMI and the Pinsker bound in **floating point**
     (`float(p)*log2(…)`, tolerance 1e-12), so it is not exact-rational.
   - Fix the definition ("a computation on small instances in exact rational arithmetic"). Separately, line 84 must not
     say "exact probes"; that falls to the §2.4 mapper (I-10x).
5. **I-010, IMPRECISE (low).** "Each with one step not machine-checked."
   - The count is right for Theorem 2(c), where the unchecked step is the time-t identification.
   - It is also right for readback, where the unchecked step is history-level (C4) ⇒ a non-permutation rooted map.
   - It is wrong for the Corollary form, where two steps are unchecked (line 82).
   - Fix: "(each machine-checked except for steps proved on paper)".
6. **I-015, IMPRECISE (low).** "Open are … any test of the hypothesis."
   - The sources say less: no memory-witness falsifier is established (Main:702–704; Intro line 22), and no experiment
     distinguishing OI from standard QT exists (Intro §6.3).
   - The corpus does list falsifiers for the applications (Appendix A F1, F6).
   - Fix: "…and any experiment that distinguishes OI from standard quantum theory".
7. **I-078, IMPRECISE (low).** "Coincides with the constructions of Barandes … and Schmidt."
   - Main's W equals Bar26's construction with Θ = √Γ.
   - Bar26 fn. 1 reports an apparent error in Schmidt's partial-isometry construction.
   - The symbol n is undefined in the Introduction.
   - Fix: "has the form of the dilations of …", and define n.
8. **I-025, IMPRECISE (low).** "Hidden states compatible with the same x send it to different futures" is false read
   universally: a visibly deterministic realization is a counter-case. Main:105 has the same wording. Fix: "can send …
   can evolve stochastically".

## Attention items resolved

- **I-008.** "Deterministic completion" means faithful realization. The claim needs no condition on M_t: read as
  Theorem 2(c), it is vacuous at M_t = 0, and the readout-relevant form is the Corollary.
- **I-010.** See item 5 above.
- **I-025.** Read as "can". See item 8 above.
- **I-034.** Read as "can produce". It is then proved in the kernel by `S_imp_D`.
- **I-042.** See item 3 above.
- **I-048.** Every inclusion has an attribution. Q ⊆ S is attributed to SGD19 Eq. (3), which was verified.
- **I-052.** See item 2 above.
- **I-054.** See item 4 above.
- **I-056.** The generic sense matches Main:62 and book/glossary.md:137. The cubic lattice is the matter sector's
  special case.

## Completeness: what the abstract and §1.2 omit

1. **Main's Characterization theorem** (Main:516; proof :608; no ledger row, signal S1).
   - Its statement: (ii) non-Markovian at an accessible order ⟺ (iii) a per-horizon realization with C1, C3 and C4
     at k and a fixed hidden prior. Under (T), (i) a unitarily evolving representation also holds.
   - Both directions are proved on paper only:
     - (iii)⇒(ii) by the Pinsker readback lemma;
     - (ii)⇒(iii) by process dilation and its Extension.

     Neither direction is formalized, and (i) is imported from Barandes.
   - Main itself says (ii)⇒(iii) "adds … the existence of a realization", because (C4) coincides with (ii) in every
     faithful realization.
   - **Not an understatement.** The Introduction carries every ingredient (Theorem 1, the Pinsker bound at line 84, and
     line 86's "(C4) coincides with M_t>0 … (C1) and (C3) follow"), and its internal D ⊆ Q supersedes (i).
   - Optional sentence for §2.4, if the owner wants the theorem named: "Together these give the characterization
     theorem of [Main §3.4]: a law has conditional memory at an accessible order exactly when, at every horizon
     containing that order, it has a finite reversible realization with a fixed hidden prior satisfying (C1), (C3) and
     (C4); both directions are proved on paper."
2. **Finite operational ε-realization and related results** (Main:544–578; Summary item 4 at Main:580; ledger P,
   exact probes at d = 2).
   - The results: finite operational ε-realization and gluing, uniform continuum ε-density, and one controlled dynamics.
     Every bounded d-dimensional quantum experiment of horizon K has a finite reversible ε-realization.
   - The Introduction omits these entirely. They do not make §1.2's "stop short of operational QM" false, because they
     realize quantum statistics approximately inside OI and do not derive QM from it.
   - They are the natural complement of §3.4's qubit obstruction. This is for the §3.4 mapper and the owner.
3. **GR's coherent-completion results** (GR:198, :204, :240; kernel), all absent from the Introduction:
   - the coherent-completion classification: existing OI-compatible completions with the same operational data are
     related by a unitary or an antiunitary (transpose) map;
   - the operational orientation no-go;
   - OI⁺ ⟺ exact finite endomorphic operational QM.

   These are for the §3.2–§3.3 mapper.
4. **The classical action-labelled comb** (Main:460, proved on paper) narrows the intervention gap. It is not mentioned.

## Corpus-side findings (not Introduction text; for separate correction)

- **Main:46 against Main:62 and :113.** Main:46 attributes the finiteness of S to Lemma 1. Lemma 1 gives only a finite
  C_V; the other two sites make total finiteness a posit.
- **Methodology:235 and :253 against Main:62 and :708(iii) (signal S10).** Methodology calls bijectivity a lemma; Main
  calls it a part-empirical representation choice.
- **GR:326.** The heading "Dissolution of the Cosmological Constant Problem" is unqualified, while GR's text (:28, :356)
  says the dissolution is conditional.
- **book/ch01-observation.md:261.** "quantum mechanics … is the dynamics that our specific kind of observation produces"
  asserts more than `oi_alone_not_qm` and Theorem 4 allow.
- **Main:170.** Main says "Certified exactly", but `c4_backflow_probes.py` evaluates the CMI and the bound in floating
  point with tolerance. Under the Code Review Rules' exactness clause this is evidence, not exact certification.
- **Main:706.** "Laboratory tests of the characterization theorem may be possible" contradicts :704, which says no
  experiment falsifies the theorem.
- **Main's subtitle** ("The Equivalence of Quantum Mechanics and Embedded Observation") against the Introduction's I-012
  and I-145. The claim inventory already raised this for the owner.
- **BH-01 REPORT header.** It says "unreviewed for adoption", while `review/REVIEW.md` records an independent review.
  This is a reference-list matter.

## For the owner to decide

1. Whether to name the Characterization theorem in §2.4 (completeness item 1). Recommendation: optional. Its content is
   already carried.
2. Whether the Introduction should report the ε-realization and gluing results (item 2) beside the qubit obstruction.
   Recommendation: one sentence in §3.4, marked "proved on paper".
3. The "exact probe" convention (I-054). Narrow the definition, or relabel line 84's probe. Recommendation: both; line
   84 should not claim exactness.
