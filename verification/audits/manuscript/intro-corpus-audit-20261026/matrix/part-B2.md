# Mapping part B2: I-092–I-171 (§2.4, §2.5, §3.1–§3.5)

Introduction at `4a260ca9`; corpus at `eae01647`, read from the `git archive` extraction. The Lean sources at
`eae01647` are identical to those at `17b830bc`, and every Appendix A `module:line` in this range was checked against
them. The range has 80 claims and 10 directional sub-claims, so 90 rows in `part-B2.json`. #939 changed no site in
this range: its edits to Main, GR, ch00 and ch01 concern only ħ.

## Counts

| Verdict | Rows |
|---|--:|
| FAITHFUL | 75 |
| IMPRECISE | 11 |
| MISCITED | 1 |
| UNSUPPORTED | 1 |
| OVERCLAIM | 1 |
| UNDERCLAIM | 1 |

Proof status of the 90 rows:

| Proof status | Rows |
|---|--:|
| proved-kernel | 36 |
| proved-paper | 46 |
| open | 4: I-146, I-158, I-167, I-171 |
| conditional | 1: I-109, the necessity direction, conditional on the mixing hypothesis |
| conjecture | 1: I-170, a posit conditional on H-Bell |
| unsupported | 2: I-124, I-127 |

Literature attributions that their source proves are counted as proved-paper.

## Non-FAITHFUL rows, most severe first

1. **I-127, OVERCLAIM (moderate).** Line 106 reads "no unconditional implication holds among" accessible memory,
   P-indivisibility and quantum non-Markovianity. Its source, Main:334, says only that "no unconditional implication
   … is asserted". One direction does hold. A Markov law is rooted-P-divisible (RHP14 Cor. 2.1), so P-indivisibility
   of the population law forces $M_t>0$ at some $t$. A replacement is in the row.
2. **I-146, UNDERCLAIM (moderate; central quantum-equivalence status).** Line 120 reads "Which of (iii)–(v) a
   physical substratum supplies is open." The corpus partly answers this, and part of the answer is machine-checked:
   - GR §3.3 (GR:260), ch01:165 and ch19:126 state that the concrete substratum, with a phase intervention assumed,
     supplies the structural closures but not continuously tunable state mixing.
   - `readWriteSourced_not_control` (ReadWriteControl:169) shows that a read-write-sourced theory fails (iv).
   - `substratum_residual` (StructuralClosure:383) records the substratum class's residual.
   - `substratum_plus_control_qm` (StructuralClosure:414) shows that QM follows exactly when the controllability
     resource is added.
   - ROADMAP:1521 records "Dense/nonclassical operational control from the presently stated architecture" as
     INDEPENDENT, which retires the equivalence endpoint F1 for that architecture; F2 stays open.

   Only the physical source of the resource is open. The same sentence recurs in the abstract (line 12) and in §6.3
   (line 183), so any fix must propagate there.
3. **I-114, IMPRECISE (citation scope).** Theorem 3 matches `pIndivisible_of_rooted_identity_return_of_overlap`
   (RecurrenceHorizon:148) exactly, but the citation does not cover it:
   - [Main §2.3] (Main:115) proves only the special case $s=1$ under the uniform prior.
   - The census lists the general form as kernel-only, with no manuscript carrying it (family 34).
   - "Fixed hidden prior" means a prior shared by every root (CausalReadback:181); I-114's attention item is resolved
     on that reading.
4. **I-121, MISCITED.** The machine-checked routed-readback conclusion is cited as `routed_forces_indivisible_somewhere`
   (round C4-1).
   - That module itself records that its predicate conditions on the initial hidden seed, not on the hidden state at
     storage time, and that the predicate fails on the sealed C1–C4 core.
   - The Introduction's gloss, "record written into the hidden state is read back later", matches round C4-2's
     `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256).
   - Both readings are proved, incomparable with each other, and kernel-only.
5. **I-103, IMPRECISE.** The claim is labelled "(proved on paper, with exact probes)". `c4_backflow_probes.py`
   computes the conditional mutual information in floating point on hand-picked families, so it does not meet the
   Introduction's own definition of an exact probe (line 30). The bound and its written proof are correct. Main:170
   says "certified exactly" in the same way.
6. **I-116, IMPRECISE.** The Introduction says Doukas states "the same overlap-and-return argument". Doukas Prop. 1 is
   the general no-revival obstruction, applied to a Rabi example where two rows coincide and then separate. It has no
   overlap, return or recurrence; Theorem 3 is an instance of it. The same attribution recurs at line 28.
7. **I-113, IMPRECISE.** The text reads "This is the divisibility criterion of [RHP14, Thm 2.4]", but only the "only
   if" half is used. RHP14's "if" half needs contraction of every vector and invertible rooted maps. BD16 Prop. 1 is
   the semiclassical case; its classical statement is Cor. 1. This resolves I-111's attention item:
   - BD16's divisibility is rooted at $t_0$, so its attribution applies.
   - RHP14's divisibility is also rooted (Eq. 14), but assumes invertibility.
8. **Low severity.**
   - I-102: $I^*$ is undefined. It is $\sup_t I(X_{<t};X_{>t}\mid X_t)$ (Main:492), and the sentence has no
     manuscript locator.
   - I-105 and I-105.a: the time index and positive probability are missing from "(C4) coincides with $M_t>0$".
   - I-123: "minimal model" beside "smallest realization".
   - I-124, UNSUPPORTED: "smallest realization" has no proof anywhere. It is true by a two-line argument, given in
     the fix.
   - I-147: the §3.3 heading drops "by representability".
   - I-159: the §3.4 heading is broader than its body, and "carrier" clashes with Theorem 4's "carrier".
   - I-162: Mon08 bounds ontological dimension; it gives no explicit task. HKLP24 is the source of the explicit
     tasks.

## Other attention items resolved, all FAITHFUL

- I-100: Main §1.5 (Main:97) carries the Corollary. Both directions are traced; each rests on kernel (a) plus the
  vanishing criterion and the time-$t$ identification, neither machine-checked.
- I-109: "(C2) is a physical-regime premise" (Main:76) and §6.3 item (4) agree. The latter concerns the necessity
  direction, which Main proves on paper conditional on the mixing hypothesis (Main:433, :447). §6.3 calling it "open"
  understates it; that is outside this range.
- I-139 and I-140: `physical_of_exactAll` is carrier-general, with [Nonempty A] in its section (PhysicalCharacterization:224).
  Theorem 4's "positive ancilla level" matches `ExactAll`, and line 114's "every ancilla level" matches the
  structure's `availExt n`.
- I-153: the converse pair has different middle terms but is sound. Equal trajectory laws imply equal rooted families
  (an unformalized marginal), and equal rooted families imply equal one-step matrices (the forward direction). No iff
  is claimed. Main:624 does claim an iff on trajectory laws, which slightly exceeds its kernel anchor.
- I-154: `realData_traj_stochastic` proves both `QfbRealizable` and `Stochastic`.
- §3.5: the Bell ceiling (Main:360, written proof), the choice of ontic parameter dependence (Main:392) and H-Bell
  open (ROADMAP P1) are all stated faithfully.

## Quantum-equivalence status across the corpus

| Class | Results | Sources |
|---|---|---|
| Proved (kernel) | $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ | `finite_horizon_equivalence` |
| | Theorem 4 | `exactAll_iff_physical_general` |
| | OI ⇏ QM | `oi_alone_not_qm`, `five_way_minimality` |
| | OI⁺ ⟺ exact finite endomorphic operational QM (a characterization of an extension) | `carrier_general_oiPlus` |
| | Substratum + continuous controllability ⟺ QM | `substratum_plus_control_qm` |
| | The typed form | `typed_determined_iff` |
| | The relating evolution is not fixed | GL2/GL3 |
| Conditional | Exact operational QM, on (i)–(v) or on the OI⁺ principles | |
| | Coherent-completion uniqueness up to gauge and one antiunitary | GR:198, conditional on existence |
| Open | The physical source of the controllability resource | ROADMAP F2 |
| | Selection of the relating evolution | P0 |
| | H-Bell | P1 |
| | Pre-quantum kinematics K | P1 |
| | H-∞ | P1 |
| | Physical C4 discharge | P1 |
| | Origin of the Born exponent | Main:534 |
| Settled negatively | Phases and dense control are not sourced by the presently stated architecture | ROADMAP:1521 |

The Introduction says what is proved and what is open, and denies that OI implies QM. It omits two things:
- the negative sourcing results (I-146);
- the OI⁺ and substratum-source characterizations and the coherent-completion classification.

## For the owner to decide

1. Whether §3.2, the abstract and §6.3 report the substratum-source result and the INDEPENDENT findings (I-146), and
   whether the Introduction should mention OI⁺ and the coherent-completion classification. Both are completeness
   findings.
2. How to source Theorem 3 (I-114). The options are to cite the kernel module alone, or to have Main §2.3 state the
   general overlap form, which would be a corpus correction to census family 34.
3. Which routed-readback reading to cite (I-121): round C4-2, or both.
4. Corpus findings for separate correction:
   - Main's title, "The Equivalence of Quantum Mechanics and Embedded Observation", is unscoped.
   - ch00:39 calls QM "an exact observer-level representation of the incomplete finite law" without the fixed-basis
     scope.
   - Main:624 claims an iff on trajectory laws, which exceeds `rooted_eq_iff_slice_eq`.
   - Main:170 calls a floating-point probe "exact".
   - H-Bell has three clauses in Substratum:132 and two in Main:394.
   - GR:216's prose omits the preparation and discard fields of the operational structure.
   - The ch18:34 and ch19:126 framing of the exponent differs from Main:534's "frontier item".
