# QPHEN Phase 1 r3: independent full-text review

## Standing

- **Reviewer.** A fresh, independent, model-written review. It is read-only on the repository, git and GitHub. It writes
  only this file and the probes `review/probes/p6_r3rev_*.py`.
- **Independence.** Findings B1 to B3 and N1 to N17 were formed and written before any earlier review was opened.
  `DISPOSITIONS-r3.md` was read afterwards, only for the traceability check below. `review/REVIEW-PHASE1.md`,
  `review/REVIEW-PHASE1-r2.md`, `r1/` and `r2/` were not read.
- **Files reviewed** (sha256 verified):
  - `QX3-ANTIBUNCHING.md` `4ea39322ec363331…`
  - `QX4-INCOMPATIBILITY-LG.md` `866a6f2aeae4e394…`
  - `QX6-BELL-CHSH.md` `04882cc25af13476…`
  - `SHARED-MECHANISM.md` `6537031aa8299652…`
  - `DISPOSITIONS-r3.md` `711bfda011a1bd9c…`
- **Corpus.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`, fetched on 2026-11-09. It equals the specs'
  snapshot. Every cited Main, Substratum, AP1, M2D, ROADMAP, Methodology, book and COMP-1 line was read there.
- **Owner records read** (read-only): #1210 c.6736966265, c.6737891756, c.6738031707, c.6738145827, c.6738337450 and
  c.6738866690.

## Verdict: **REVISE (narrow)**

The mathematical core of r3 holds. Each item below was re-derived or re-computed exactly:
- Lemma A6.1's proof is complete and correct, and Main §3.3's setting satisfies every hypothesis of A6.1.
- Both GHZ protocols, and the local-Clifford map between them.
- Every Leggett–Garg value.
- Every QX-3 count.
- The CHSH stabilizer bound.

Three blockers remain. Each is a classification or specification error, not an error in a derivation. Each needs a
one-line fix:
- B1 is a misread source in §9.
- B2 is a disproof stated beyond the scope of its counterexample.
- B3 is an under-specified counterexample: under one natural reading of its notation, the stated value is false.

The owner's gate requires a full ACCEPT with no unresolved mathematical blockers. r3 does not meet that gate yet. An r4
that applies B1 to B3 and the must-fix nits N1 and N2 should need only a check of those items.

***

## Blockers

### B1. SHARED §9, row "(L′) and (R) of A6.1": column (ii) answers "yes", and Main says the opposite

**The text.** Column (ii) reads: "yes as design conditions: they state causal locality in the coupling-graph sense,
'The selector in a Bell experiment is therefore causal locality' (Main:362-364)".

**Why it is wrong.**
- **Main gives these conditions up.** (L′) and (R) generalize Main's hypotheses (ii) and (iii). Main:403-406 says a
  completion reproducing quantum Bell correlations "gives up at least one of two remaining hypotheses: (ii) and (iii),
  … or measurement independence, (iv). **The framework gives up the first.**" Main:414 then takes branch (a), ontic
  parameter dependence. Substratum:467 says the same.
- **So OI's principles do not imply (L′) and (R).** OI's chosen branch, H-Bell's preparation-indexed long edges, is a
  failure of (R) by design. QX-6 §3.2 itself lists it as the third way to escape A6.1.
- **The quoted sentence is misread.** Main:362 says that causal locality is what *selects* the Bell class. It does not
  say that OI's dynamics obeys causal locality.
- **The row breaks §9's own rule.** QX-6 §3.2 says (L′) and (R) are "excluded by the experimental design (R6.2, R6.4),
  not by any theorem". §9 says a protocol or design declaration "answers no and records the reason it is adopted".

**Required fix.**
- Column (ii): "no. These are design conditions of the Bell test: own-wing settings and separation. OI's chosen branch
  (a) gives up Main's (ii) and (iii) (Main:403-406, :414), and H-Bell is a failure of (R)."
- Standing: "design conditions (protocol)".

**Why this is a blocker.** It is the error the owner's three-questions rule targets: a source-supported "yes" in (ii)
where the source says the framework does not hold the condition. It is a status claim stronger than its evidence
(Code Review Rules, claim/evidence boundary).

### B2. SHARED §8 Q4-D2: the counterexample does not lie within the refuted claim's scope

**The text.** Q4-D2 lists as disproved "`A_4`, with sharp supplies admitted, gives `K₃ ≤ 1`". The counterexample is
A4.1(b)'s sharp-mediator witness.

**Why it is wrong.** QX-4 §5 itself says: "Whether `A_4`'s admissible `G` includes such a map is construction-specific."
The witness refutes the statement for the generic affine-symplectic class with sharp supplies. It does not refute it
for `A_4`, because it is not shown to belong to `A_4`. The review rule "State negative results only for the
construction or class actually ruled out" applies.

**Required fix.**
- Restate the refuted claim as: "every affine-symplectic `G` (with translations) on two modes, with sharp supplies
  admitted, gives `K₃ ≤ 1`." The counterexample is the witness (exact; reproduced in p6 (5b)).
- Classify `A_4`'s own value as open. Q4-O6 already covers `A_4`'s paper expectations.

This is one of the six owner-required disproved items, so its counterexample must be valid as stated.

### B3. QX-4 A4.1(c) and SHARED Q4-P4: the counterexample `G = (I ⊗ H)·CNOT_{m→c}` does not fix the tensor order

**The problem.** The text fixes the operator order ("the rightmost factor acts first") and the control direction. It
does not say which tensor factor is the carrier. Probe p6_r3rev_lg (1) computes the value exactly under both readings:

| tensor order | `H` acts on | `(C₁₂, C₂₃, C₁₃)` | `K₃` |
| --- | --- | --- | --- |
| carrier ⊗ mediator (the writer's probe convention) | mediator | `(cos β, sin β, 0)` | `cos β + sin β` ✓ |
| mediator ⊗ carrier (the order of the subscript `m→c`) | carrier | `(0, 0, cos β)` | `−cos β` ✗ |

The SWAP variant has the same dependence. With `H` on the carrier, `K₃ = 0`.

The claimed values `√2` and `7/5`, and with them Q4-D6, hold only under the first reading.

**Required fix.** State "tensor order carrier ⊗ mediator, so `H` acts on the mediator" in QX-4 A4.1(c) and in SHARED
Q4-P4, for both constructions. With that fix the claim is proved exactly.

***

## Nits

**Must fix before freeze consideration**

- **N1. Q6-P2's status.**
  - The sentence "The status depends on the r3 review. If that review finds a gap …" is process narration, and so is
    the "[… unreviewed]" tag.
  - This review checked A6.1 line by line and probed it exhaustively and adversarially. It found no gap in the proof and
    none in the Main check.
  - Under the owner's rule (c.6738337450), Q6-P2 may now read "proved [A: complete paper proof, independently reviewed
    r3; exact checks P5-A61, p6_r3rev_a61]". Remove the conditional sentence.
  - The same "unreviewed" tag appears in SHARED §3 and QX-6 A6.1's header.
  - Q6-P2 remains a paper derivation in these files (A). It is not on `main` and not kernel-checked.
- **N2. Standing: "no computation is run" against the cited writer's probes.**
  - All four specs say "no computation is run". QX-3 §0 lists "any computation" as not done.
  - Yet r3 cites the writer's own probes P5 as support (X) for ledger entries.
  - The owner's authorization (c.6736966265) bars "computation, including probes that evaluate any proposed OI
    mechanism". The P5 probes evaluate generic mathematical objects, not an OI mechanism. That appears to be the
    tolerated practice, since the reviewers' probes P1 to P4 are cited in owner-facing comments.
  - The standing sentences are nevertheless literally false. Reword them, for example: "no computation on any proposed
    OI mechanism; exact checks on generic mathematical objects (P1–P6) only".
  - **Flag for the owner.** Confirm that generic exact checks fall within Phase 1.
- **N3. SHARED §8 rules and the X layer.**
  - The rule "A claim whose only support is a W or D record is open" conflicts with listing as proved [X] entries whose
    only computation is an off-`main` probe: Q3-P4, Q4-P2, Q4-P4, Q4-P7, Q4-P9, Q4-P15 and Q6-P6. QX-3 §0 classes the
    probes as D.
  - Add an explicit rule: an exact finite computation on generic objects, re-runnable and independently reproduced,
    counts as X at its stated scope.
  - This review reproduced every such entry independently, so each stands as proved.

**Precision and scope**

- **N4. Q4-P8: the Lüders bound has a two-line proof. Include it rather than resting on L.**
  - For Lüders dichotomic reads, `C_ij = ½⟨{Q_i, Q_j}⟩`, with Heisenberg operators `Q_i² = I`. The identity
    `P₊QP₊ − P₋QP₋ = ½{Q_i, Q}` was checked symbolically (p6 (3)).
  - Then `0 ≤ ⟨(Q₁ − Q₂ + Q₃)²⟩ = 3 − 2(C₁₂ + C₂₃ − C₁₃)` (checked symbolically, p6 (3)), so `K₃ ≤ 3/2` in any
    dimension, with degenerate `Q` included.
  - Q4-P3's consequence and Q4-D4 then rest on A, not L.
- **N5. A4.1(c), the Clifford integrality argument.** The values `{0, ±1}` hold for pure stabilizer states and stabilizer
  codes. They fail for convex mixtures of stabilizer states. `K₃ ≤ 1` still holds for mixtures, by linearity. Say "pure
  stabilizer preparations", or add the mixture remark.
- **N6. Q4-D1's counterexample** reaches `K₃ = 2`, not a comparator value, and it uses ordinary reads, not an INM
  detector.
  - It can be tightened. In the witness `G`, the `t₂` kick never enters `z₃` (p6 (6)). The same `G` with an
    environment mediator gives `K₃ = 0`. The mixture with weight `3/4` on the sharp mediator gives exactly
    `K₃ = 3/2`, with the `t₂` read ineffective on `Q₃` in every branch.
  - State the INM detector, `K_null = id`, explicitly, and either give this mixture or restate the refuted claim as
    "an INM-controlled violation forces …".
- **N7. Q4-D6's wording.** "C-NONSTABILIZER gives no QM-matching value" is refuted as a statement about the QM
  comparator protocol, by the two-qubit computation. It is not refuted as a statement about OI's value, which stays
  open (Q4-O2). Say "the comparator protocol reaches `√2` …".
- **N8. Dyadic.**
  - **Q6-P9, T6, A6.3, M2.** "N2 laws are dyadic" holds for uniform laws on `F_2` cosets without conditioning. It fails
    for `Z_q` with `q` odd (AP1 works over `Z_q`), and after conditioning on an event whose count is not a power of 2.
    The conclusion, that irrational targets are unreachable, needs only "rational". Use "rational (dyadic at `q = 2`,
    unconditioned)".
  - **QX-3 §7 item 5.** It gives the wrong reason. `α = 0.18 = 9/50` is reachable with dyadic probabilities:
    `P_A = P_B = 5/8`, `P_AB = 9/128`. What excludes it is A3.1(a), the affine case analysis, not dyadicity.
- **N9. QX-6 §2, first witness row.** "Measurement-dependent models with `I_ont ≥ 0.0309` bits" is the threshold for
  `S = 2√2` only. For an observed `S`, Main:421 gives the unexcluded class as `I_ont ≥ (S − 2)²/(32 ln 2)`.
- **N10. Q6-P7 and QX-6 §1, TLM sufficiency.** The (⇐) direction is usually credited to Landau, Found. Phys. 18, 449
  (1988), and to Masanes (2003). Landau PLA 120, 54 (1987) is usually cited for the necessary condition. Literature
  only; check the source before relying on the (⇐) attribution.
- **N11. SHARED §9, SA-1(a), column (ii).** "Native for the wave branch" rests on Substratum (A4) and (A5). (A5)'s
  restriction to linear is "imposed" and only "partly derived" (Substratum:100). Write "yes, conditional on Substratum
  (A4)–(A5), with (A5)'s linear restriction imposed".
  - The M15 row's "yes" rests on AP1 §3.2 [W]. It inherits that condition, and its support is a W record. Either state
    the elementary identity behind it, or mark it conditional.
- **N12. SHARED §2, cell M16 × QX-4 marked R.**
  - The legend defines R as "required for the experiment's discriminating form".
  - M16 is required only for agreement with the comparator protocol, as §1 and §9 say, which label it QM-only.
  - An INM run without M16 is still discriminating: it gives `K₃ ≤ 1`.
  - Mark the cell "? (tested; QM-only, §9)", and treat M20's Tsirelson half the same way.
- **N13. Ledger completeness.** These are not in §8:
  - "classical mixing of sharp reads reaches only `η_Z + η_X ≤ 1`" (QX-4 §2);
  - "a classical wave … reaches `V² + D² = 1`" (QX-4 §2 table);
  - A4.5, two applications of `G`, together with its claim about C-SIZE-DEPENDENT, which is D-sourced;
  - QX-3 §3's statement that W1 and W2 need only stabilizer or classical-reversible operations.
- **N14. QX-3 A3.1(c), `NCONS_global`.** The text does not declare whether the supply or control cell `s` counts toward
  the excitation number.
  - The conclusion holds either way. With field-only weight there are 64 globally field-weight-preserving routing
    bijections of `F_2³`, and none is affine (p6_r3rev_qx3 (c)).
  - Analytically: an affine field map that preserves field weight for each `s` is the identity or the swap, independent
    of `s`.
  - State the convention. This answers DISPOSITIONS' "optional item not taken" (POSITIVE).

**Register and self-narration** (spec bodies; §A.27, §A.30, §A.33 voice)

- **N15. Revision narration in spec bodies:**
  - QX-6 §11, last row: "it is no longer cited for the GHZ claim";
  - QX-3 §0: "(review N9)";
  - SHARED §8 Q6-P2's conditional sentence (N1).

  Move each to DISPOSITIONS. No §A.32 or §A.33 caps-emphasis hits were found: every all-caps token is an identifier,
  token or file name.
- **N16. Owner records now exist.**
  - The r3 requirements are recorded at #1210 c.6738145827 and c.6738337450.
  - O1 and O2 were approved at c.6738866690.
  - DISPOSITIONS O3 and its "not on a recorded Issue comment" are stale. The specs' §0 should quote these with author
    and time (§A.42 item 7).
- **N17. DISPOSITIONS line references are stale.** R2-B2 cites QX-4 "line 76, 129, 251, 301, 322". In r3 these sites
  are at about 75-86, 140, 289, 339-342 and 363. The content is present (traceability below).

***

## Owner acceptance criteria

| criterion | status | basis |
| --- | --- | --- |
| **Bell locality:** tighter condition, proved lemma, Main checked, counterexample kept | **met in substance; status line to fix (N1)** | (L′) is stated precisely (QX-6:241-248). The proof was checked line by line: step 1 uses finiteness of `V` and the union-over-settings `G_t`; step 4's induction needs `t > t_B` for `G_t ⊆ G_B`, which holds; step 6 uses (MI). No gap was found. Each hypothesis was checked against Main:364-391, quoted: (ii) "`u^A_a × u^B_b × id` … at one step" gives `t_A = t_B = 1`; (iii) "`k_A` updates after the setting, with `d(B, R_A) > k_A`" gives `G_B = G_φ`; (iv) and "±1 in every run" also hold. Exhaustive and adversarial probes found 0 violations in 2,787 random (R) cases plus 397 cases at the (R) boundary. (R) is not vacuous: 56 of 213 non-(R) cases depend on the remote setting. The counterexample to the weaker form is kept as Q6-D1 and was re-built: `S = 4`, single-graph `d = 1 > 0`, (L′) fails. The single-graph distinction (P5-A61(5)) was re-built. B1 is a §9 table error, not a lemma error |
| **GHZ:** both formulations with exact states and predictions | **met** | GHZ-1, X/Y: `(|000⟩+|111⟩)/√2` gives `+1, −1, −1, −1`, Mermin value 4 against a local maximum of 2. Its nonzero `X/Z` strings are exactly `XXX`, `ZZI`, `IZZ`, `ZIZ`, all `+1`, so there is no X/Z contradiction (Q6-D3 holds). GHZ-2, X/Z: the triangle graph state gives `+1, +1, +1, −1`, value 4 against a local maximum of 2, with real amplitudes. `(SH⊗SH⊗SHS)|GHZ⟩ = e^{iπ/4}|tri⟩` holds exactly with right-to-left action. With `HS` in place of `SH` the map fails, so the stated convention is necessary and correct |
| **Leggett–Garg:** every comparison qualified by protocol; no "supra-quantum" from exceeding 1.5 | **met, subject to B3 and N4** | The comparator protocol is declared (QX-4 §2). Every site that mentions `3/2`, `2` or `3` names it, and "supra-quantum" survives only as the quoted refuted claim Q4-D4. Measure-and-reprepare values were checked exactly: `K₃ = 3`, and `6w − 3` with `w = 5/6` giving 2. The 11,520-map two-mode scan was reproduced: maximum 1 with half-known or environment mediators, 2 with a sharp one. The witness is symplectic. B3 is the tensor-order specification of the Clifford counterexample |
| **Evidence ledger:** every substantive claim classified; six disproved claims linked to counterexamples | **not met (B2); otherwise largely met** | All 11 disproved entries carry explicit counterexamples, and 10 are valid as stated. Q4-D2's counterexample is outside the claim's scope (B2). The six owner-required items are Q3-D1, Q6-D2, Q4-D1 (N6), Q4-D2 (B2), Q6-D1 and Q4-D3. §A.34 directions are kept separate wherever an equivalence is displayed: A3.1(a), A3.1(c), Busch, TLM, Spekkens (one direction, with Q4-O7 for the converse), and A6.4's "iff" (open). Gaps in completeness: N13. Rule inconsistency: N3 |
| **Independent physical justification:** a reason independent of QM for every restriction | **not met (B1); otherwise met** | §9 keeps (i), (ii) and (iii) separate, and (iii) is never cited for (ii). SA-1(c), null-result invasiveness (M16, R4.10) and Tsirelson soundness (R6.10) are hypotheses under test marked "none identified (open)", as owner decision O1 (c.6738866690) requires. The quoted reasons for SA-1(c) were checked: AP1:347-349 "Clause (c) is not derived", the E-AR obstruction (AP1:221, :677), and closure (AP1:344-347). These sources do not establish SA-1(c), and §9 is right not to count them. No "yes" in (ii) is supported only by (iii). One "yes" is a misread source (B1), and one is conditional (N11). No restriction was found that was introduced to force QM agreement while left unlabelled. The three such restrictions are labelled QM-only. M16's matrix cell is inconsistent with that label (N12) |

**The owner's further points.**
- **Antibunching.** It is framed as a question:
  - A3.1(d): "Which additional physical constraints, if any, make non-affinity necessary is open";
  - Q3-O2 and Q3-2.

  Non-affine dynamics is stated as not established. **Met.**
- **D19–D23, freeze, dispatch.** No text implies their authorization, or a freeze, a dispatch or an implementation
  approval. The specs mark rules as outlines, not frozen. **Met.** N2 is the one standing inconsistency.

***

## Other verified content (POSITIVE)

**QX-3**
- 307 cosets of `F_2⁴` and 314,368 cases, with `α ∈ {0, 1, 2}` or undefined.
- Both directions of "`α = 0` ⇔ `f_B = f_A + 1` with `f_A` non-constant" hold.
- `L` routes, is bijective, and equals Fredkin on `c₁ + c₂ = 1`.
- 48 affine bijections route on the ready support with weight conserved there.
- Exactly 6 affine bijections preserve weight globally, all coordinate permutations.
- All 8 globally weight-preserving routers are non-affine.
- A3.1(c)'s proof is correct.

**QX-4**
- A4.1(a): 24 one-mode maps, maximum 1, with a correct case table.
- A4.2: correct, since a single-qubit Pauli other than `±Z` anticommutes with `Z`.
- A4.6: `3/2`, `37/25`, `4/3` and `−3/2` hold exactly.
- `C₁₂ = cos 2θ` holds.
- Q4-P11 and Q4-D7 hold. Q4-D7: the maximally mixed state gives `1/2` both ways.
- Q4-P12's `3/4` bound holds by the octahedron argument, `|⟨Z⟩| + |⟨X⟩| ≤ 1` on the hull of stabilizer states.

**QX-6**
- `|Φ⁺⟩` gives `E = (−1)^{xy}/√2` and `S = 2√2`.
- The `π/3` comparator gives `S = 5/2`, exactly on the TLM boundary (`3/4 = 3/4`).
- Max `|S| = 2` over all 60 two-qubit stabilizer states with signed Pauli settings.
- The analytic anticommutation and Fine argument holds for multi-qubit wings.
- `I_ont ≥ (3 − 2√2)/(8 ln 2)` holds.

**Source lines** checked at `fd539e15`:
- Main:22, :44, :50, :56, :362-427, :486, :488, :652, :654, and ref. [26];
- Substratum:48, :98, :100, :131, :467, :481;
- Methodology:393; book ch01:173 and ch04:124;
- ROADMAP:974-979; M2D:59-69, :483, :509-515;
- AP1:282-361, :416-417, :221, :677;
- COMP-1 `result.md`, a kernel round with receipt `verification/receipts/COMP-1.json`.

All are as quoted, except the B1 reading.

**AW-QX4-1 at three modes** (§A.16 cheap probe; record only).
- A random sample of 20,000 affine-symplectic maps on three `F_2` modes with translations, every mode half-known or the
  extra modes environment, gives maximum `K₃ = 1`.
- The sharp-supply countercontrol in the same sample gives 2.
- This is consistent with AW-QX4-1 at `m = 3`. It is a finite sample, not a proof, so Q4-O1 stays open.

## DISPOSITIONS-r3 traceability

| claimed change | present in r3? |
| --- | --- |
| R2-B1: A6.1 rewritten as a complete proof; Main table; P4 kept as Q6-D1; propagation to QX-6 §1, §3.2, R6.4, consequence, §8 items 2 and 7, §11, SHARED §3, §4, §8 | yes, all sites |
| R2-B2: Lüders heading; `3/2` as the Lüders bound; measure-and-reprepare 3 and 2; von Neumann case; comparator declared; the five sites; T9 and T2; Tsirelson row reworded; "supra-quantum" only in Q4-D4 | yes. Line numbers are stale (N17); a grep confirms "supra-quantum" and "QM-incompatible" occur only at SHARED:408-409 |
| R2-B3: T9 disclaimer; M3 × QX-4 "R (backaction)"; AW-QX4-1 consistency sentence; Q4-4 caveat; R6.9 and A6.4 fitted-class sentence | yes |
| R2-B4: GHZ-1 and GHZ-2 block; X/Z note; "only GHZ-2"; SHARED M11 qualified | yes |
| R2-B5: SHARED §8 ledger; §0 "Claim status" pointers in each spec | yes (B2, N3, N13) |
| R2-B6: R4.9 rewritten; Q4-D3 | yes |
| R2-N1: A4.1(c) hypotheses, `cos 2θ`, two-qubit Clifford examples; propagation to A4.2, ABL-G, §6, §7 item 2, M12, §5, Q4-P3/P4/D5/D6/O2 | yes (B3) |
| R2-N2 (`h > 0`), R2-N3 (injective identification; M2D lines), R2-N4 (Q6-4 and Q6-5), R2-N7 (`t_B`) | yes. M2D lines verified |
| Owner 2a (antibunching as a question) | yes |
| QX-4 §1 Spekkens direction; §2 NSIT "for some preparation" | yes (QX-4:33-34, :67) |
| SHARED §9 with 22 restrictions | yes (22 rows counted; B1, N11) |
| Writer's probe hashes | all four match. `p5_r3_a61.py`, `p5_r3_ghz.py` and `p5_r3_qx3.py` were re-run (exit 0) as scripts, not imported |
| "None refused"; open items listed | consistent with SHARED §8 |

## Probes (`review/probes/`; none imports P1–P5)

| probe | sha256 | method | result |
| --- | --- | --- | --- |
| `p6_r3rev_a61.py` | `8dea32b916e020d2…` | exhaustive over `x₀` and settings for each model; `G_t` computed exactly from the maps | 1,500 random models satisfying (L′), 0 to 25% long-range reads, non-bijective maps allowed: 2,787 (R) cases with 0 remote dependence; 213 non-(R) cases with 56 dependent. 397 boundary-targeted (R) cases with 0 dependent. P4(1) rebuilt: `S = 4`, single-graph `d = 1`, (L′) false. Three-tick split: `S = 4`, `d_{G_B} = 2 = T_A − t_B`. Main instance: `d_φ = ∞`, single-graph `d = 2 ≤ k`, readout independent of `b` |
| `p6_r3rev_lg.py` | `fbdd53cbba218e98…` | sympy, exact; `F_2` exhaustive | B3 table; measure-and-reprepare `6w − 3`; Lüders identity; `cos 2θ`; one mode 24 maps max 1; two modes 720 × 16 = 11,520 maps: half-known 1, environment 1, sharp 2; witness symplectic, `(1, 1, 0)`; N6 mixture `p = 3/4`; A4.6 values; Q4-D7 |
| `p6_r3rev_ghz_chsh.py` | `390b8d9371d10b47…` | sympy, exact | GHZ-1 and GHZ-2 values and local maxima; GHZ-1's X/Z content; LC map exact (HS variant fails); `|Φ⁺⟩` `S = 2√2`; `5/2` on the TLM boundary; 60 stabilizer states, max `|S| = 2` |
| `p6_r3rev_qx3.py` | `99917656469304d7…` | exhaustive, `Fraction` | 307 cosets, 314,368 cases, `α ∈ {0, 1, 2, undefined}`, both directions; `L` = Fredkin on the sector; 48; 6, all permutations; 8, 0 affine; field-only weight: 64, 0 affine (N14) |
| `p6_r3rev_aw3.py` | `097da07bd8e522c0…` | random sample of `Sp(6, F_2)` (transvection products) with translations, exact correlators | half-known and environment: max 1; sharp countercontrol: 2. A sample, not a proof |
