# Review of GAMMA-1 unit G2 r1 (record laws on K1); independent, non-author, paper-only

**Object.** `GAMMA-G2-r1.md` (753 lines plus trailer), as retained on PR #1294, branch
`research/ro1-sector-c-1169-20261114` at `445b47b5`, directory
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/` (committed in
`acfdd566`); the copy read is byte-identical to the retained one. Cited as G2:N.

**Reviewer.** Claude, a session that wrote none of G2, G1 or G3. Read-only: no edits, commits or
posts; hand arithmetic only, no computation.

**Inputs checked.** G1 r4 (blob `91a5d656`), U4-CALC r2 (`bef634e2`), U1 r5 (`68983f86`), U2 r3
(`2711c168`) and r4, SIG r2 (`8d71ff13`), G3 r2 (G3-F10), and at `origin/main` `75cc5100`
`papers/Main.md` (blob `0db17597`) and MR★. Every blob id in G2's input list was re-derived with
`git rev-parse` at `6ab9515d` and at `445b47b5`: all eight agree with G2:28–41, and Main's blob agrees
with G2:43.

**Verdict: ACCEPT WITH CHANGES.** Every proof was walked step by step and none is broken: Lemma G2-1,
Theorem G2-2, Propositions G2-3, G2-4, G2-7, Theorems G2-5 and G2-6, the §3.3 and §5 instances and the
C0 and PC-wave algebra all check by hand. No counterexample was found. The changes are scope,
labelling and consistency corrections, four of them substantive (R1, R3, R5, R6 below): one false
premise sentence (§3.2 at `t = 1`), a scope claim that contradicts the source it cites (G2-6
"independently of retention" against MR★:613–615), cross-model combinations that NC-γ3 forbids, and
the A1 label missing from most K1 results. No verdict on D-1 is drawn.

***

## 1. The nine items asked

**(1) Independence and the single dark law.** Lemma G2-1 (G2:105–121) is correct: a bijection of a
finite set preserves the counting measure, the uniform law on a product is the product of uniform
laws, and (b) follows because a variable independent of itself is almost surely constant. Theorem
G2-2 (G2:130–153) follows from it. Scope: it is a theorem **for `μ-G` only**, for a bijective rule on a
finite product whose declared observers are disjoint factor sets (H-obs), with every record and every
conditioning label held at `t_c` (H-rec), and with κ-ens laws only (G2:721). Its universality is
inherited from three [P] declarations, not from any property of K1: G1 §2.1's disjoint observers, U1
G4's joint hold, and G1 §3.2's E-set incident event as the *held* record at `t_c`. Conditioning on the
use-tick setting value instead (a representation under K-4) would not be covered. So the result is a
theorem relative to modelling choices, and G2 states most of them (G2:179–188); R2 and R6 ask for the
rest. "Any rule (either reading of P-vii)" (G2:132) is wider than the hypothesis: G_SM, which the
scoped reading includes (G1:116–120), is not shown to be a bijection of a finite product with
observers as factor sets, and §7 (G2:632–634) lists only native-Y, G-ring and SIG (2.1).

**(2) G1-F3 and Proposition G2-3.** The proof (G2:242–244) is correct and matches U1 §4.3's I-sel
definition term for term (U1 r5, lines 423–427: partition of the carrier's content induced by
`s_carrier ↦ pr_Y φ^t`, every other region held at a value of positive mass). It proves U1's
factor-set reading, an [A-inf] at U1 r5 line 437, at the affine scope. That blocking needs the
induced partition to change also checks: with the screen map `F(x_L + x_R) + G(z) + N`, removing the
`x_R` dependence for one `z` is invariance of `ν` under `im F|_R`, which does not involve `z`.
"Settles it on K1" (G2:6, :69, :233) does not overreach as written, since each occurrence carries
"pending review" and the global-reading condition (G2:258–259). One qualification is missing (R7):
Proposition G2-4 shows a law-level, setting-class-dependent change of the screen's carrier
dependence through conditioning on `ζ`. The a2/a3 "not available" therefore rests on Proposition G2-3
**and** on a2's loss-booking clause, and §8 cites only the first.

**(3) H-1 masking.** Theorem G2-5's proof (G2:356–368) checks. The wrap-around bound is right: under
(NW) a translate `k ≠ 0` gives `|Δ_{c′} − k_{c′}| > L_{c′}/2 > t`. So does triangularity:
`(w − v)·e ≤ 0`, with equality only at `w = v`, and the unit diagonal from Proposition 2.6's
coefficient. For (b), ties in the key `v·e − s` give diagonal blocks, which have unit diagonal under
the distinctness hypothesis. G2-C5 and G2-C6 were recomputed: ring `u_2(0) = y_{−2} + y_0 + y_2 − x_{−1}
− x_1`, `u_1(0) = y_{−1} + y_1 − x_0`; native `(A²)_{0,−e_1} = 0` on sides `≥ 4`. "Every two-path
geometry with the source in front is carrier-independent" is **not** a finite test promoted to a
universal: it is a proof over a declared class. But the class is narrower than G2-F4 (G2:692) says,
and one premise sentence is false at `t = 1` (R3, R4).

**(4) A-cur erasure.** Theorem G2-6 (G2:463–474) checks: at `t = 1`, `u_1 = Ay − x` is a bijection in
`x` for any `D`; for `t ≥ 2` the `x_{v−(t−1)e}` coefficients form a triangular matrix with diagonal
`−1`. The consequences overreach in two places (R5): "independently of retention" (G2:485, :693)
contradicts MR★:613–615, which G2:487 itself cites, and "every later readable record" holds only for
regions inside the (NW) box.

**(5) `K_P = 1` with a masked marker.** The ring instance (G2:537–548) was recomputed over `ℤ/2`. The
non-carrier parts of `u_1(1)` and `u_2(2)` are both `y_2 − x_1`; `A′` receives `(y_2 − x_1, y_1 − x_2)`
and `D′` receives `(y_1 − x_2, y_2 − x_1)`, both uniform; under `L` detection forces `m = 1`, under `R`
`m = 0`; `K_P = 1`. It is a **witness**, labelled [instance] at G2:537 and Proposition G2-7(ii) (G2:528–529),
on a ring (not the native graph), at a tick that violates (NW), with assumed point contents. The
general content is Proposition G2-7's formula and case (i), both proved. Two defects: `c_L` and `c_R`
come from two declared `μ` (two models), and G2-F6 (G2:694) calls this "fills NC-copy's slot" with no
native-graph instance (R6, R13).

**(6) C0's `Δ = −b`, PC-wave, classical-wave type.** The algebra checks:
`Δ = −1 + (1−b)(1 + r_{12} − r_1 − r_2) = −b` when `r_{12} = r_1 + r_2`. An additive background gives
`−b` too, so the result does not depend on the noisy-OR form. It assumes the dark process does not
depend on which paths are open; G2:581 states this ("independent carrier-free"). PC-wave's
`Δ_j = (1 − b)η·2Re(f_L f̄_R) − b` checks. G2 does **not** inherit G3-F10. Its model-side normalization
is per unit of incident `μ`-mass (G2:330–332), as G1 §5.3 requires, and it uses no §5.4 coincidence
rule, so G3-F10(a) does not arise. It adds background to the model rather than subtracting it from
the data, which is G3-F10(b)'s raw-direct route, so (b) is met. The two units should be reconciled
(R8). The surrounded coset laws as "classical-wave type": the per-model and assumed-content caveats
are explicit at G2:405–407 and G2:616, but not at G2:672–673 or in §8's third column (G2:652). The
`S(PC-wave) = ∅` step also holds for *every* native result on `𝒜_10` (G1-F8: PC-wave is separated only
by X-2, which lies outside `𝒜_10`), so it says nothing specific about coset laws (R13).

**(7) The twelve controls.** C2 (countercontrol), C5, C6, C7 (non-prediction) and C12 can fail
independently of the result they test. C4 is a countercontrol by citation of SIG C-1, C-2, which was
checked against SIG r2, line 258. C9 is a weak instance check. **C3** is honestly labelled as unable to
fail. **C8** cannot fail: `f` is linear, so `f(L + R) = f(L) + f(R)` holds by construction. **C10** re-reads the
K1 step `u_1 = Ay − x`. **C11** is the instance's own calculation restated. **C1** is an instance of the
lemma's own hypothesis: a repeated image would violate bijectivity, not the lemma. These four
reproduce the claimed formula and should be relabelled as consistency checks, which is CALC's own
convention (CALC r2, lines 249–251) (R11). No control or instance checks Proposition G2-4's `τ`
construction; it was checked here by hand and holds. No verdict in G2 rests on a vacuous control
alone, since every verdict rests on a proof.

**(8) "No counted miss" against SNR-1.** It is correct under G1 §5.7 and §6: a counted miss needs an
*available* `L_a` with every input derived, and at the derived level the carrier preparation is
unsourced (PC-1 fork) and retention is unsourced (C-RET). Two weaknesses (R9). The further claim
that, with the herald retained, the outcome is "not available, not a miss" (G2:191–194, :449–452)
rests on reading R1's P-cell as the herald-retained property. G2 itself notes the screen can depend
on unprepared tick-0 carrier content (G2:174–176). Second, by Theorem G2-2, no derived-level counted
miss can arise under G1's declarations for any bijective rule, so "no counted miss" (G2:658) is
structural and carries no evidential weight. The product law's qualitative disagreement with every
fringe target should be reported beside it (§A.24: never immunizing).

**(9) D-1.** No verdict is drawn: G2:10–11, :394–395 ("bears on … by giving a sufficient geometric
condition", [A-inf]) and :674–675. Confirmed.

***

## 2. Required changes

| # | Lines | Finding | Severity | Required change |
|---|---|---|---|---|
| R1 | 18–19 against 261, 342, 463, 514, 287–297, 327–331, 397–404 | The binding (#1169 c.6893456888) requires [A1] on every result that uses a finite `S`. G2 tags Lemma G2-1, Theorem G2-2, its consequences and G2:444. Propositions G2-4 and G2-7 (uniform laws on finite cosets via CALC Theorem 1(a)), Theorems G2-5 and G2-6 (uniform content on `ℤ/q`), the E-set, E-prep and `κ_norm` masses, and the §3.3 instance all use H-K1's finite `𝐑 = ℤ/q` and carry no [A1]. Proposition G2-3 needs no finiteness and is correctly untagged | substantive | Add [A1] to each listed result. Where §7's Haar extension (G2:639–641, [A-inf]) would remove it, say so beside the result |
| R2 | 132, 170–176, 632–634, 664–666, 689 | "Any rule (either reading of P-vii)" and "for every rule" go beyond the hypothesis. The scoped reading includes G_SM, which is not shown to be a bijection of a finite product with H-obs factor sets. The theorem's universality also comes from three [P] declarations: G1 §2.1, U1 G4's joint hold, and E-set's held-record incident event | moderate | Replace "any rule" with "any bijection of a finite product in which H-obs holds". Name the three [P] declarations beside Theorem G2-2 as the source of its universality, and link them to owner question 2 |
| R3 | 377–378, 382 | "`D − (t−1)e_1` lie[s] at `k_1 < h`" is false at `t = 1`, where it is `D` itself at `k_1 = h`. Theorem G2-5(b) then needs `D`'s own current slice uniform. That holds under H-μ (`D` is not carrier), but not "relative to every declared `μ` that leaves the far side uniform" when the screen is prepared, as in G2:455–457's route 3. At `t = 1` with a prepared screen the readable pair `(y_D, (Ay)_D − x_D)` is still carrier-independent, through `y_{D−e_1}`, but it is not uniform, so "`K^D_t = R_D`" is the wrong statement there | substantive (one false premise sentence) | Restrict the sentence to `t ≥ 2`, or add "`D` uniform" for A-reg at `t = 1`, and state the prepared-screen case separately |
| R4 | 384–386, 652 (column 2), 692 | G2-F4's "every source-in-front two-path geometry has `K^D_t = R_D`" drops five hypotheses: (NW) with the box condition, so the screen's transverse extent is under half a side; a planar screen transverse to an axis; a `μ` with the far half uniform *and independent*; and the `t = 1` case of R3. The contrapositive's "non-uniform content" (G2:385) should read "content outside `U`": a carrier site can have a uniform marginal. §8 column 2 extends the screen-marginal result to a5 and a6, which are marker-sorted joint laws. That needs Proposition G2-7(iii)'s joint condition, or the marker outside the light cone of the masking variables; under A-reg, a marker at `k_1 = h + 1` in line with a cell can read `y_{D−(t−1)e}` with coefficient 1 | moderate | Carry the hypotheses into G2-F4 and §9. Add the joint condition to §8's a5/a6 entry, or declare the marker's position in §3.2 |
| R5 | 304–305, 465–466, 478–487, 499, 693 | (a) "Independently of retention": MR★:613–615, cited at G2:487, says that an access which "retains the earlier of two consecutive reads" is not single-time restricted. A herald over two consecutive ticks, which needs C-RET for its first read, conditions previous slices and lies outside G2-6's hypothesis; G2:466 already limits the example to heralds "at one tick". (b) "Every later readable record" and "every readable law at a later tick" hold only for regions inside the (NW) box. For a region spanning half a side or more, the map `x ↦ U_{t−1}(A)x` need not be surjective | substantive (contradicts its cited source) | Replace "independently of retention" with "for heralds at one tick, without retention of an earlier read". Restrict "every" to regions meeting (NW). Carry both into G2-F5 |
| R6 | 162–163, 603–606, 514–519, 537–549, 656, 694 | NC-γ3: laws of different models are never combined. (a) The derived-level `Δ_j = −p_j` and the one-path-normalizer ratio `1/2` combine a1 with a2 and a3, which on K1 are programs of other geometries (Proposition G2-3; §8 row 3). That contradicts G2:607–609 ("`Δ` is not formable"), and "the native derived-level law is a member of C0" rests on that combination. (b) Proposition G2-7 and its instance form `K_P` from `c_L` and `c_R` under two declared `μ`, which §3.3 (G2:405–407) says are two models, never combined. The identification of the program `b(π)` with "same geometry, point carrier content on path `π`" is neither G1's on K1 (other geometries, the O11 stop, G1:313–322) nor labelled. (c) §1.2's derived-level `K_P = 0` omits the O11 stop | substantive | Label every such quantity as a cross-model functional, not a within-instance result, or remove it. State and label the `b(π)` representation in Proposition G2-7. Carry the O11 stop on §1.2's `K_P` and in §8's `K_P` row, columns 1 and 2 |
| R7 | 278–286, 653, 691 | Proposition G2-4 shows the screen's carrier dependence can differ between setting classes through `ζ`: a class whose `τ`-image is a coset of `H` leaves dependence only through `c(x)` modulo `H + K_0`, which can mask one path's contribution for one class and not another. G2 correctly excludes this from a2 because nothing is booked as loss, but §8's a2/a3 row cites only Proposition G2-3. G2-F3's "can act only as a conditioning on background the setting region shares with the screen" omits G2:284–285's unmasked-`Z` case, where conditioning also selects carrier contents | moderate | Cite Proposition G2-4 and a2's loss clause in §8's a2/a3 row. Add the unmasked-`Z` case to G2-F3 |
| R8 | 578–591, 742–743 | G2 does not inherit G3-F10: its normalization is per incident `μ`-mass, and it adds background to the model, which is G3-F10(b)'s raw-direct route. But G2 calls G1's text "consistent once … read as the background-free case", where G3-F10(b) records an inconsistency in the same clause, and neither cites the other. Also: `−b_j` needs `b_j` as a value the source states (G1 §5.4); `𝒜_10` has no all-paths-blocked protocol; and G1 §7.1's void clause must then read "do not separate `Δ` from `−b_j`". With `b_j = p₀` and a background that does not depend on the openings, `−b_j` is Sinha's `I_AB = 0` | moderate | Cite G3-F10(b). Give one characterization of the G1 clause. Merge owner question 1 with G3-F10(b). State the three conditions |
| R9 | 189–194, 449–452, 658 | (a) "Not available, not a miss" for the retained-herald case rests on reading R1's P-cell (U1:514) as the herald-retained property. On a reading where the screen's dependence on unprepared tick-0 carrier content (G2:174–176) satisfies R1, the a6 product law would be a candidate miss once C-RET is sourced. (b) Under G1's declarations no derived-level counted miss can arise for any bijective rule (Theorem G2-2 with SNR-1), so "no counted miss" is structural | substantive (truth-seeking, §A.29, §A.24) | Label (a) [A-inf, a reading of U1:514] and state the alternative. Beside §8's "no counted miss", report the product law's qualitative disagreement with the fringe targets (a1 per model, a6) and give the structural reason |
| R10 | 652 (row 1, column 1) | "both instances" contradicts G2:148–149 and :201: `κ_det^rdy` is undefined at the derived level without a held screen-preparation herald | minor | "`I^part`; `I^rdy` only with a held herald (§1.3)" |
| R11 | 209, 420, 496, 566 | C1, C8, C10 and C11 cannot fail independently (§1, item 7); C8's "Could it fail? yes" is wrong | moderate (§A.29) | Relabel as consistency checks, or replace them with independent checks (for C8, a non-additive countercontrol; for C11, the dual covector computation as in CALC C1-7) |
| R12 | 292–297; G1:371–372 | G1 §3.2 makes the E-prep incident event the attempt, with the failed outcomes `(a, ¬E)` inside its mass. G2 sets `𝔄_a = {s_P ∈ B_a}` (the success event, mass `q^{−M}`) and puts the failed mass `1 − q^{−M}` outside it. "`M` cells" is also ambiguous under A-reg, where a site carries two slices | minor | Name the attempt event and the success event separately, as G1 §5.3 does (`μ(𝔈_a ∧ e = (a, E))`), and count slices |
| R13 | 610–616, 672–673, 689, 694, 696 | Classifications: G2-F1 "NEW" adds little to MR★:642 plus OA-1 D2 (G2:124–128 says as much); ELABORATING fits better. G2-F6's "fills NC-copy's slot" rests on a ring witness across two models, with no native-graph instance. "Of classical-wave type on `𝒜_10`" (G2:673) generalizes one instance with point contents, and its `S(PC-wave) = ∅` step holds for every native result on `𝒜_10` | moderate | Downgrade G2-F1. Scope G2-F6 to "a ring instance; native `d = 3` open". Carry "[assumed] point contents, per model, [instance]" into §9 and §8 column 3, and cite G1-F8 as the reason for `S(PC-wave) = ∅` |
| R14 | 620–626, 699 | AW-G2-3 names the wrong hypothesis of PC-wave's bound. Given the full field the K1 outputs are deterministic, so conditional independence given the field holds. G1 §7.2's bound uses a single split intensity `I`, with both click probabilities increasing in it, conditionally independent given `I`. The K1 outputs are not functions of one split intensity, and G2:626 says it is "not a beam-splitter geometry" | minor | Restate the marker as "PC-wave's `α ≥ 1` assumes two outputs driven by one split intensity; outputs reading shared background lie outside that construction" |
| R15 | 39, 733 | U2 r3 is cited for the SNR-1 counting condition; U2 r4 is the owner-accepted revision (#1169 c.6892563291). The counting text of §11.1 is identical in both, which was checked by diff | note | Cite r4, or state that the cited text is unchanged in r4 |

***

## 3. Checks recorded

- **Proposition G2-4** (G2:271–277): `K_0`, `τ` on `pr_Z K^W = R_Z`, and the fibre
  `M^D x + τ(z − M^Z x) + K_0` check. `Y_Z` is uniform on `R_Z` independently of `x` when `Z` is
  carrier-masked. The setting-mass formula checks.
- **Proposition G2-7(i)**: with a product background and `π_P` constant on `K^A`-cosets, `c_L` and
  `c_R` are point masses at distinct reports, so `K_P = 1` when `d_L + d_R > 0` (unstated at G2:524–526;
  add it). With a masked pair, `K_P = |d_L − d_R|/(d_L + d_R)`.
- **§3.3 instance**: over `ℤ/5`, `f(L) = −1`, `f(R) = 1`, `f(L + R) = 0`; click values `(1, 1, 0)` for
  `C_1 = ℤ/5 ∖ {0}` and `(0, 1, 0)` for `C_1 = {1}`. Correct. Under A-reg, `K^D_2 = 𝐑 ⊕ 0` checks.
- **§6.4**: under `R`, `P(both) = 0` and `α = 0`; under `L`, `α = (1/2)/(1/4) = 2`. Correct.
- **§1.2 consequences**: the pair ratio is constant, so `V_u = 0 ≤ 0.1`, the least `v_−` in `𝒮`, and
  "absent" is stable. `α = 1`. `K_P = 0` at equal detected masses, subject to R6(c).
- **Theorem G2-6 against CALC Instance 1.2**: `f` contains `−x_j`, `j ∼ 0`, so CALC's A-cur record
  needs a previous-slice carrier preparation, as G2:489–491 states.

## 4. What stands after the changes

Lemma G2-1 and Theorem G2-2 at `μ-G` for bijective finite-product rules under G1's [P] declarations;
Proposition G2-3 at affine scope, which, once reviewed, meets U2 §11.1's condition for G1-F3 under the
global reading; Proposition G2-4; Theorem G2-5 for the declared one-sided geometry under (NW), with
R3's correction at `t = 1`; Theorem G2-6 for single-tick heralds and (NW) regions; Proposition G2-7's
formula and cases (i), (iii), (iv), with (ii) as a ring witness; C0's `Δ = −b_j` as a control image.
None of these is a verdict on D-1 or on (γ), and nothing here counts under SNR-1 before the changes are
applied and confirmed.
