# Focused confirmation of FOUND-ASSESS-r2

**Reviewer:** the independent, non-author reviewer of r1.

**Scope.** Paper-only and read-only. I checked r2 against my review of r1 (`REVIEW-FOUND-ASSESS-r1.md`, findings F1–F29) and against the same sources at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. I also read for this check:
- Meth:146–158;
- GR:875–879;
- FrozenSourcing.lean:103–190 and :336;
- Main:46;
- the #914 §4 continuum paragraph;
- the #1007 body (preregistered controls and payoff);
- #866 c.6704691492 and c.6704448653, first-hand;
- the A1 audit's premise table (L1–L8 and its F1–F5 group).

No computation and no Lean build.

**Verdict: CONFIRMED WITH NITS.**

All 29 findings are applied and correct. F24's correction is right, and the reviewer's original location was wrong. F26 is confirmed first-hand.

The new material is mostly well scoped. Four one-sentence corrections are still required:
- R1: C5′ is described as the owner's framework choice;
- R2: C5′ omits #1007's own preserved-results list, and its "route R4" label is unsourced;
- R3: C5's "Excluded by" has a logic slip;
- R4: Q-G's thermodynamic route says it "avoids the circularity".

These can be applied without another review. There are seven nits (N1–N7).

***

## 1. Findings F1–F29, as applied in r2

| F | In r2 | Confirmed? |
|---|---|---|
| F1 | §0 (lines 34–41); §3 intro (252); new table row (259); "Live rows" (266); C1 "Excluded by" | Yes. The bridging premise is stated, and Main:418's arithmetic is correctly paraphrased (the graph reach equals 1/√3 only along body diagonals; up to √3 *c* along the axes). New row: see §2.1 |
| F2 | §0 (41); §3 rows MI and long edges; C2, C3; Q-B | Yes. Fine-tuning is applied to both routes, Q-B separates "C2 and C3 jointly vs C0", and the costs discriminate between C2 and C3 |
| F3 | §1.3 preparation row; §3 "One shared gap"; retrocausality row; Q-C | Yes. Q8, Q9, N-8, R1a and H-PREP are all quoted correctly from #1147 c.6894144708 and #866 c.6649267203. The preparation demand is removed from the measure question |
| F4 | header; §0 (54); table C5; C5 obligations and standing | Yes |
| F5 | header; §2.1; C0 "Excluded by"; Q-A | Yes. See N6 on the supersession wording in C2 |
| F6 | §0 (53); §1.4 grid; C4; C5 | Yes. "Only" and "most concrete" are gone, and the C5 prediction is exact-limit with two missing estimates |
| F7 | §1.4 grid (Motivated); C5 obligations | Yes |
| F8 | §0 (51–52); §1.4 items 2–3; Q-D | Yes. (D4) is at GR:878. The site count follows from (D1)–(D3) via Lemma B.2(a), and GR:132 covers the deep sector beyond B_n under (D5). The three residual cases are named |
| F9 | C0 "Consequences" | Yes; the audit's qualifier is quoted exactly |
| F10 | Q-A | Yes |
| F11 | §0 table, C1 | Yes |
| F12 | C3 "Preserves" | Yes (Sub:123, :193) |
| F13 | §3 MI row; C3 | Yes |
| F14 | E13′; §2.4; C4 | Yes. `fixedGateTheory_outside_ceiling` is at FrozenSourcing.lean:336. E13's split of scope is accurate: `permTheory_phase_ceiling` holds on any nonempty carrier (:106), `permTheory_dense_ceiling` on `Fin 2` (:187). See N4 |
| F15 | E6, E16; C1 | Yes; P4 is added |
| F16 | header; §1.4 grid | Yes. Every cell has a standing and a step. See N3 on the wording of the Total/Derived cell |
| F17 | table; C5′ | Partly. C5′ exists under the §A.29 headings, but see R1 and R2 |
| F18 | §2.2 Scope | Yes |
| F19 | §2.2 | Yes |
| F20 | §3 single-world row | Yes |
| F21 | §3 retrocausality row | Yes |
| F22 | §3 finite-regions row | Yes |
| F23 | §2.4; Q-E | Yes. See N4 for one wording point in §2.4 |
| F24 | §1.1, §1.2, §2.1 | Yes, and the writer's correction is right. Meth:148 reads: "Injectivity yields bijectivity only on a finite set; on an infinite set an injective map need not be surjective." My r1 statement that Methodology does not say this was wrong; I had read only to :146. The other locations are fixed. See N1 for one remaining location |
| F25 | §1.2 | Yes |
| F26 | C2 provenance; §6 | Yes. I have now read both comments first-hand. c.6704691492: "SM §3.1's existing … ring rule gives a genuine program-dependent local response under one common structured hidden prior … a conditional source-based local component, **not a complete physical Bell interface**". c.6704448653: "STOP at the physical preparation/setting/access map; no physical no-signalling PASS or FAIL". r2's paraphrases are faithful, apart from "one common prior", which should read "one common structured hidden prior". Both rest on draft #1173, off `main`, so "provenance only" is the right classification. §6's sentence "cited from the review, not read first-hand" can now cite this confirmation |
| F27 | §3 intro | Yes |
| F28 | §1.4 grid; Q-D | Yes |
| F29 | §0; C1 | Yes |

***

## 2. New material

### 2.1 Bell row: wings inside the reference graph cone

**Correct.**
- The speeds lie between *c* and at most √3 *c*, which holds if *c* is the wave speed (Main:418).
- Under (vii) the remote contribution is a linear image of the setting write. The write itself can be any function of the setting and of local data, under hypothesis (ii) of Main:414.
- Toner–Bacon 2003: one bit plus shared randomness reproduces singlet correlations for projective measurements, with uniform marginals. A one-bit influence of this kind is therefore not excluded on paper from giving CHSH > 2 with operational no-signalling.

**Status and scope.** The row's status is right: "this assessment's sketch, unchecked", "not excluded on paper", "probably excluded by data". It does not overreach.

**Exclusion by data.** The comparison with speed-of-influence data is sound, provided the lattice rest frame moves slowly relative to the Earth. For a frame moving at speed β, a Salart-type test with near-simultaneous detections over a distance *d* leaves a time window of about β*d*/*c* in that frame. The bound on the influence speed is then of order *c*/β, which is far above √3 *c* unless β is a sizeable fraction of 1. Bancal et al. 2012 is the right reference: finite-speed influence models of multipartite correlations allow signalling, and that argument does not depend on the frame. Both remain "to be checked first-hand".

**Prediction.** The prediction (violation fails for spacelike wings separated near the body diagonals of the lattice frame, beyond the graph cone) follows from Main:414 applying there.

Nits on this row are N2.

### 2.2 C5′ (infinite or continuum carrier) under §A.29

**Correct.** The obligations (i)–(iv), the controls listed, the predictions (Wilson action selection, p = 2, a definite composite cone) and the rejection test all match #914 §4. "Evading E8 is the problem it was built for" matches #914 §4 and #1007.

**R1 (required).** C5′ "Premises" says: "This is the owner's framework choice of 2026-10-30". The decision recorded in the #1007 body is narrower: "finiteness belongs to the observational interface … The general formulation must not require |S|<∞. A finite S remains a valid restricted model and proof premise". That is C1's premise, finiteness not assumed. The positive commitment to an infinite or continuum carrier is the research question #1007 tracks: "physical extensions remain research-only".

As written, the sentence presents a candidate as owner-adopted. That slants against C5 and contradicts the owner's guidance that finiteness stays open.

*Fix:* "#1007's 2026-10-30 decision makes finiteness of S not required (C1's premise); C5′'s positive commitment to an infinite or continuum carrier is the research route #1007 tracks, not an adopted choice".

**R2 (required).** C5′ "Preserves" says its list was "named in advance by #914 §4 and #1007". The list reproduces only #914 §4. The #1007 body has its own "Preregistered controls (§A.29)":
- Lemma 1 with a finite discreteness scale ε;
- S⇔D⇔Q_fb with measure-preserving maps;
- P-indivisibility, where "the finite-recurrence route (Main:139) … must be replaced or dropped" and the readback route must survive;
- gauge-group selection (Theorem 23, Lemma 23.0);
- the area law and the ħ gap equation with finite σ ("sub-states must stay decoupled from the boundary count, or σ diverges").

The last two are where C5′ is most at risk, so they belong in the list. "#1007 route R4" has no source in the #1007 body. The only "R4" I found is a list label in #1007 c.6719401889.

*Fix:* add the #1007 controls and drop the "R4" label, or source it.

### 2.3 §1.4 finiteness grid

The grid is accurate and complete in form: two kinds of finiteness, three routes, a standing and a step in each cell. The classical-ontology caveat is correctly carried into both Motivated cells. "A total bound implies a patch bound" is right. Wording nit: N3.

**R3 (required).** C5 "Excluded by" ends: "or a demonstration that cardinality beyond the cone is observable at a fixed interface under some admissible prior". Showing that something is observable does not exclude finiteness; it makes finiteness testable.

*Fix:* "… or an observed consequence of infinite cardinality beyond the cone, once such a consequence is shown to exist under an admissible prior".

### 2.4 Q-G: justifying finite visible capacity

**The three statements kept apart.** They are kept apart correctly:
- (a) Lemma 1's conclusion from the Definition's clause (Main:42 → :46);
- (b) the unestablished claim about physical observers;
- (c) hidden and total finiteness, which do not follow from (b).

The point that (b) would not select QM (E1) is right. So is the fixed-horizon premise list: it matches the audit's group F1–F5 (site factorization, determinism, L1, L8, L2), and the audit (L8 row) agrees that Lemma 1 "gives ∣C_V∣ < ∞, not a readout depending on finitely many sites". See N5 for the settings premises.

**The circularity obligation.** It is right in substance. Main:46's two supports (a finite-area mode count, holographic bounds) yield finiteness only with quantum premises: finitely many classical field modes still have a continuum of amplitudes. Main:703 calls the foundational use circular for a related but different reason: the bounds are downstream physical results. Both reasons should be named; see N1.

**R4 (required).** The thermodynamic route says: "The premises are classical, so this route avoids the circularity." That overreaches. In OI, energy and the noise floor are not foundational quantities. The Hamiltonian and its scale are emergent (§2.3 calibration; GR:130), and Main:703's objection (downstream physical results) applies to any energy bound imported at the foundational layer. The bullet does say, correctly, that the route gives a capacity bound rather than a finite configuration set. In addition, Landauer and Bennett bound the thermodynamic cost of erasure and of reversible computation, not the number of distinguishable states.

*Fix:* "The premises need not be quantum, which avoids the first circularity; whether an energy-like constraint and a noise floor can be defined from the substratum itself (for example a conserved quantity of φ, with the trace-out as the noise), rather than imported, is a further obligation (Main:703)". Cite Landauer and Bennett for record cost only.

The named routes, and the cheapest step (a literature sort of capacity bounds by whether their premises are quantum, then a paper statement about a register coupled through a fixed bijection), are reasonable and within scope. Ranking Q-G fifth is defensible: it bears on every candidate's foundation but separates none of them directly.

***

## 3. New errors and balance

**Errors.** No new error beyond R1–R4 and the nits.

**Nits.**
- **N1.** Location and reasons. In §1.4 item 1 and Q-G(b), the "bound on each occurrence is not a uniform capacity bound" point is at Meth:154, with Main:703, not Meth:152; Meth:152 states the circularity. In the circularity obligation, name both reasons: quantum premises, and downstream results (Main:703).
- **N2.** Bell row wording.
  - "As a one-time pad does": in Toner–Bacon no pad is needed, because the receiver's marginal is uniform by the symmetry of the shared randomness. "Symmetric shared randomness, as in Toner–Bacon" is more accurate.
  - State the frame assumption for the exclusion by data: a lattice rest frame moving slowly relative to the Earth. Note that the Bancal et al. argument does not depend on the frame.
  - For balance, note that this route would keep item (vii) and need no long edges, so it would leave the SM/GR linear derivations intact. It also needs the physical *c* to be the wave speed, which Main:418 leaves open.
- **N3.** In the grid's Total/Derived cell, "excluded" should read "not derivable from transition data at horizon n (GR:132); not derivable from the axioms for a decoupled factor (Main:60)".
- **N4.** §2.4 item 2 says that E13′ shows theories leaving "the nonnegativity and ones-fixing invariants" exist. E13′ shows only that a theory lies outside the nonnegativity ceiling. QM itself (E10) witnesses both invariants being left.
- **N5.** The fixed-horizon premise list in Q-G omits the settings and policies premises that apply with interventions (FS-all, or finite reads per run; the audit's F6 and F7).
- **N6.** C2 says "the earlier PR-exclusion wording of #914 c.6875548603 is superseded by D-CQ for C". D-CQ (titled "target amended") makes soundness open and says excluding PR is no longer a goal. But it leaves the #1060 BELL-QSET text pending a separate owner decision. "Superseded for the soundness requirement; related planning text pending an owner decision" is more exact. The same applies to §2.1's "must be exactly QM, or at least …".
- **N7.** F26: replace "one common prior" with "one common structured hidden prior". §6 can cite this confirmation for the first-hand reading.

**Balance (owner guidance of #1169 c.6901670978).**
- C0 is a candidate throughout ("not concluded"; "consistent … not established").
- Finiteness is open throughout (§0, §1.4, C5, Q-D, Q-G).
- C5's conflict with the exact target is stated as a fact about the adopted target, with the owner's admission of C5 recorded.
- The one slant is R1: C5′ presented as owner-adopted.

***

## 4. Not checked

- The external literature was not fetched: Salart et al. 2008, Cocciaro et al., Bancal et al. 2012, Toner–Bacon 2003, Bekenstein, Bousso, Lloyd, Shannon–Hartley, Landauer and Bennett, and Hardy 2004. Attributions and scopes are from memory and stay "to be checked first-hand".
- The Toner–Bacon embedding into the linear rule is not verified; it is the writer's sketch, correctly marked unchecked.
- r2's other new citations were spot-checked only where named above.
- No Lean build.
