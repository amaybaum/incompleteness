# REVIEW-1049-r2: independent review of ASSESS-1049 r2 (linear vs affine microscopic dynamics)

**WIP / UNVERIFIED. Model-written (Claude Code reviewer subagent, 2026-11-09). This is a fresh,
independent review, not a human review.** It adopts, promotes and authorizes nothing. I made no git
or GitHub write and no manuscript edit. I wrote only this file, `rv2_gauge_audit.py` and its
`.out` (both in `review/`), and the re-run outputs in `scratchpad/rv2run/`, which is outside the
unit's directory.

- **Under review.** `ASSESS-1049.md` r2, sha256
  `1628cc7850979632da93879f5188c6df5ce5d6d55849fce5e30feac94a43a893`, re-hashed at the start and
  matching. `DISPOSITIONS-r2.md` is `ef1faa4e…b50c`. All probe and reviewer-script hashes match the
  values ASSESS §8 and REVIEW-1049 state.
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade`. I fetched it
  2026-11-09 and it did not change during the review. Every corpus read used
  `git show fd539e15:<path>`.
- **Authorization.** #1049 c.6740117832: paper-only, exact generic checks only. The owner
  direction is #1169 c.6740778880: "Check the affine counterexamples against every stated gauge
  assumption before weakening the manuscript claim."
- **Reviewer probe.** `review/rv2_gauge_audit.py`, sha256
  `2422bd131182fec7ead6069391db705e34b374f88af21ebd60cd0bb3a6faf6cd`. Its output
  `rv2_gauge_audit.out` is `372a2c1736daeffa9cfcd2317a6b58c70d46b359e767f75b7e35278fad516ab2`.
  ALL PASS, exit 0, about 24 s.
  - It uses exact integer arithmetic over ℤ/q on generic local functions and one-step identities.
  - It iterates no dynamics, computes no observable and instantiates no mechanism.
  - It imports nothing from `probes/` or from earlier review scripts. The d = 3 function is re-coded
    from its definition with a different slot order.

## Verdict: REVISE

All of r1's findings (B1–B3, N1–N11, S1) are fixed correctly (§1). The S1 paper proof is correct,
and I confirmed it with an independent witness (§2). F-7 is correct (§4).

The new §2.3 inventory is the point of the owner direction, and it is not yet adequate to support
weakening the manuscript. There are three blockers. All three are textual, and I supply the one
missing short argument:

- **R2-B1.** The inventory reads one phrase family two ways. Sub:270's "amplitude-independent
  dispersion ⟺ affine dynamics" is read as the base-point form. Sub:272's "amplitude-dependent
  emergent dispersion" is read as dependence on absolute amplitude. Read consistently, either Sub:270
  is a missed overstating site or F-8's "false" becomes "true premise, invalid inference". The
  Sub:272 proposal also leaves a parenthetical that does not support its own conclusion.
- **R2-B2.** The proposals leave contradicted clauses standing in the same passages: Sub:100,
  ch02:84 = FULL:718, Sub:274 and Sub:272. At Sub:272 the proposal's own base-point replacement
  contradicts the surviving "strictly weaker than the output".
- **R2-B3.** GA7 (A6) is mis-assessed, and the inventory is incomplete.
  - A6 has several recorded readings, and its link interface is not fixed for non-additive rules.
  - Under a link-sum extension, P1's class is excluded. Uniform shift covariance then implies
    affinity, by a one-line proof and the exhaustive check rv2 R4.
  - So, on the owner's test, P1 is a counterexample only outside that class.
  - Sub:104 and Sub:220 name A6 in the same passage, and the theorem-recovery rule of the Code
    Review Rules applies.

***

## 1. The r1 findings

I checked each finding against the r2 text and, where it applies, against the source at fd539e15.

| r1 finding | Fixed? | Where, and how checked |
|---|---|---|
| B1 (Structure:219, :259, :301; `.tex`) | **yes** | §2.1 (lines 202–246). Structure:217, :219, :259 and :301 quotes are verbatim. SM:94 and A5 N10 ("Undetermined") are verbatim. `.tex` mirrors are present (line ranges: nit N6) |
| B2 (Q-NEXT "Equivalently") | **yes** | §5 :473–477 states the exclusion as necessary, not sufficient. "Why it is small" is restated correctly in one direction (§A.34) |
| B3 (A5 D7, D12, D13, D15) | **yes** | The table rows match A5:130–138. §3.1 says "among the rows examined", and §0 items 4–5 and §3.3 are scoped. I compared these with A5 D1–D16. The remaining rows are covered or b-independent: D1 and D2 → row 1; D3 and D16 → row 5; D5 and D6 → row 12; D4 and D8–D11 are b-independent per A5. D14 (the kernel A6 typing, additive links) is a definition, not a result; it bears on R2-B3 |
| N1 | yes | :149–154. κ ≡ 2 is forced, and the κ-general form has the α = 1 witness |
| N2 | yes | The text says "d = 2, 3" throughout and notes that no d ≥ 4 construction is given |
| N3 | yes | The [O-ext] label is applied consistently |
| N4 | yes | I re-checked the d = 1 proof (:156–165). The change of variables uses 2 ∈ units. λ = −1 makes G odd, reflection makes it even, so 2G = 0. The odd-prime linear count (q rules) is correct |
| N5 | yes | §2.2 and F-1 carry centre-free, nearest-neighbour and odd q |
| N6–N9 | yes | Rows 3a and 3b, and §3.2, use r1's wording |
| N10 | yes | §0 item 5 and §3.3 |
| N11 | yes | §4 O-D |
| S1 | **yes**, proof correct | See §2 |
| Item 4 (P2(A), P2(C), P3) | yes | §8 marks them non-evidential, and rows 3a and 3b rest on [A] alone |

## 2. S1: non-affinity at every prime q ≥ 5, verified

**The writer's proof (§2.1 :174–179), checked by hand.** Let G = C·P^{q−2} on the plane
a′ + b′ + c′ = 0.

- The three points (1, 1, −2), (1, −1, 0) and (2, 0, −2) lie on the plane.
- G(1, 1, −2) = (−2)·6^{−1} = −1/3, which is nonzero for q ∤ 3. 6 is a unit for prime q ≥ 5, and
  P^{q−2} = P^{−1} on units.
- G(1, −1, 0) = G(2, 0, −2) = 0, because C = 0 at both points. Their sum is (2, 0, −2).
- So G is not additive. Since G(0) = 0, G is not affine.

The map (p_x, p_y, p_z) ↦ (a′, b′, c′) has matrix [[2,−1,−1],[−1,2,−1],[−1,−1,2]]. Its kernel is
the diagonal, its rank is 2 when char ≠ 3, and its image is the plane. x ↦ p is onto. A linear
section s of the plane therefore gives G = (G∘M)∘s, so if f were affine, G would be affine. The
proof is complete.

The covariance and isotropy steps (:169–173) are also correct.
- **Homogeneity.** λ^{2(q−2)} = λ^{−2}, and P = 0 maps to P = 0.
- **Shift invariance.** 2·2c − 2c − 2c = 0.

**Independent witness (rv2 R1).** In lattice coordinates, the mixed second difference is
f(e₊ₓ + e₊ᵧ) − f(e₊ₓ) − f(e₊ᵧ) + f(0) = (−1/3) − (1/3) − (1/3) + 0 = −1. The values are:

- at e₊ₓ, (a′, b′, c′) = (2, −1, −1) with C = 2 and P = 6;
- at e₊ᵧ the values are the same;
- at the sum, (1, 1, −2).

An affine function has a vanishing mixed difference. R1 checks D_q = −1 exactly at every prime
5 ≤ q < 1000, with the linear control giving D = 0. This is a second paper proof, and it needs no
section argument.

**Covariance at every prime (rv2 R2).**
- R2a checks exactly that a′, b′, c′ are shift-invariant.
- R2b checks that G is unit-homogeneous of degree 1 on the whole plane, exhaustively at every prime
  5 ≤ q ≤ 101.
- R2c checks covariance directly and exhaustively on (ℤ/q)⁶ at q = 5 and 7. The countercontrols
  (1/3)Σ + x₊ₓ² and (1/3)Σ + 1 both fail it.

## 3. The §2.3 gauge inventory

### 3.1 Row by row

| Row | Writer's verdict | Review |
|---|---|---|
| GA1 (R-rel) | yes | **Correct.** For P1 the stronger property also holds: the additive automorphisms carry the rule *to itself* (R2) |
| GA2 (R-uni) | yes | **Correct.** κ = 2 form and κ-general form (R2; rv_p1 B). Sources are incomplete (N8) |
| GA3 | (a) yes / (b) no | (a) is correct, and stronger than stated: P1's response about every uniform background is independent of the absolute level *and* exactly unit-homogeneous in the perturbation's amplitude (rv2 R6). Only additivity fails. (b) is correct. **The reading assignment across Sub:270 and Sub:272 is inconsistent (R2-B1)** |
| GA4 | no, by construction | Correct |
| GA5 | no, nor the linear rule | Correct (r2 G4; rv_p1 D) |
| GA6 (A4) | yes | Correct. Exact translation commutation, no centre read (rv_p1 C) |
| GA7 (A6) | not excluded | **Incomplete and reading-dependent (R2-B3)** |
| GA8 (alphabet size) | undetermined | **Correct verdict.** Its stated grounds are SM:94, Structure:217 and A5 N10, all verbatim. The framing needs care (N4) |

### 3.2 Completeness (§A.19)

The writer's search terms (§2.1 :241–246) do not include "background independence", "A6",
"gauge group", "master principle" or "amplitude-independent". My sweep of `papers/`, `book/`,
`verification/` (records and the Lean tree) at fd539e15 found these stated gauge assumptions or
gauge statements bearing on rules that the inventory omits.

1. **A6 as recorded in the kernel** (`OIBridge/BackgroundIndependence.lean`:25–60, :118–135; A5
   rows D14 and N9). There are four readings:
   - A6-inv, with a fixed coupling and site-dependent g;
   - A6-cov, defined only on `linkF`, with links typed `V →+ V`;
   - A6-glob, the global commutant;
   - A6-sd, the state-dependent graph, which is not an invariance.

   R2-B3 covers this.
2. **SM:96's "the gauge group is the additive-automorphism group, a proper subgroup of all
   permutations"**, with the master principle "observationally indistinguishable transformations are
   gauge" (Sub:270; ch05:45 = FULL:1363). This is a stated assumption about which transformations
   are gauge. Applied to P1 it holds exactly: the uniform site-wise permutations of ℤ/q that are
   exact symmetries of P1's second-order update are precisely the q(q − 1) maps x ↦ λx + c (rv2 R3,
   all q! permutations at q = 5 and 7). The linear control gives the same group. The countercontrol's
   group is trivial.

   Paper argument: σ(f(v) − y) + σ(y) is independent of y for each value of f. With f(0) = 0
   onto ℤ/q, τ = σ − σ(0) is additive. So P1 does not enlarge the gauge group.
3. **Theorem 24 generators (i), (iii) and (iv)** (Sub:251–264), hidden relabelling, decoupled
   enlargement and graph comparison. None imposes a condition on F. They should be listed as such,
   so that the inventory covers every stated assumption, as the owner asked.
4. **Book ch05:45 = FULL:1363.** This states amplitude-scale gauge, as rescalings φ ↦ λφ only. It is
   a GA1/GA2 source, and it makes no affine claim.
5. **SM:585 and SM:811.** These use additive-automorphism gauge for the gauge *map*: the induced
   connection must be a homomorphism of the additive structure. This is not a condition on F.
6. **Sub:270's "amplitude-independent dispersion ⟺ affine dynamics".** This is a stated
   equivalence, not only a source for GA3; see R2-B1.

### 3.3 R2-B1: GA3 read two ways; Sub:270 and F-8

- **GA3 row (:296).** "(b) … which Sub:270 identifies with affinity through the lemma". Here Sub:270's
  "amplitude-independent dispersion" is read as base-point independence.
- **Sub:272 row (:318).** "GA3 in reading (a), the reading its 'absolute amplitude' names". Here the
  adjacent paragraph of the same Remark/Status block, "a non-affine F induces amplitude-dependent
  emergent dispersion", is read as dependence on absolute amplitude.

The two phrases are negations of each other in one block of text, so one reading must serve both:
- **Reading (b) throughout.** Sub:272's parenthetical is *true*: by the lemma, a non-affine F has a
  base-point-dependent first difference. What fails for P1 is the inference "so 'absolute amplitude
  is unobservable' already presupposes an affine rule". Background-dependent response does not make
  absolute amplitude observable, and R6 shows that P1's response is independent of the absolute
  level. F-8 as worded ("is false") is then wrong.
- **Reading (a) throughout.** F-8 holds, and is stronger than stated: P1's response does not depend
  on amplitude *scale* either (R6, unit homogeneity). But then Sub:270's "⟺" fails in the ⟹
  direction for P1 (§A.34). Sub:270 is then an overstating site that §0 item 1, the §2.1 list, the
  per-site table and owner Q1 all omit. Its `.tex` mirror is Substratum.tex:1719–1720.

**Robust form of the finding.** Under either reading, Sub:272's circularity argument and Sub:270's
"invoke it" claim do not survive P1. The parenthetical premise and the ⟺ gloss are true or false
according to reading, and the record should say so.

**Fix.**
- Restate F-8 as the failure of Sub:272's *inference*, with the premise's truth stated relative to
  reading.
- Treat Sub:270 under the same per-site test.
- Repair the Sub:272 proposal, whose new parenthetical ("a non-affine F can induce
  background-dependent emergent dispersion, which *is* observable") does not support its new
  conclusion ("presupposes a rule for which uniform rescalings and shifts are exact symmetries"): P1
  has background-dependent dispersion and is uniformly covariant. A premise that supports the
  conclusion is, for example, "a rule for which uniform shifts or rescalings are not exact symmetries
  of the dynamics makes the absolute amplitude dynamically observable". G_SM is an instance (§2.1
  :262–264).

### 3.4 R2-B2: the proposals leave contradicted clauses

Each proposal narrows one clause. The same passage keeps another clause that P1 contradicts in the
uniform reading, which is the reading the proposal itself says the site uses:

- **Sub:100.** "pending it, non-affine alternatives are excluded precisely to the extent
  amplitude-scale gauge is assumed" survives (Substratum.tex:749–751). P1 satisfies amplitude-scale
  gauge (GA2) and is not excluded.
- **ch02:84 = FULL:718.** "non-affine alternatives are excluded exactly to the extent that input is
  assumed" survives. This is the same point.
- **Sub:274.** "The principled object that delivers the affine restriction without overshooting is
  the **additive-automorphism** group x ↦ λx + c" survives. As exact symmetries, that group does not
  deliver it (P1). The proposal qualifies only the later "certified theorem" clause.
- **Sub:272.** "the input (absolute amplitude is unobservable) is strictly weaker than the output
  (affine dynamics)" survives.
  - Under the proposal's own replacement, "excluded by the principle in its base-point form", the
    input is *equivalent* to the output (lemma), not strictly weaker.
  - Under (R-uni), input and output are incomparable. Affine rules with κ ≢ 2, or with b ≠ 0 at odd
    q, fail (R-uni) (§2.1 :151–152), and P1 satisfies (R-uni) without being affine.
  - The proposed text would therefore be internally inconsistent. This is §2.1 (R-site)'s own point
    that read with (R-site) "the principle is affinity restated".

**Fix.** Extend each proposal to the surviving clause, or state why that clause is unaffected
(§A.25 step 1, applied within the paragraph).

### 3.5 R2-B3: A6 is reading-dependent, and one reading recovers affinity

**The writer's GA7 (:300)** says "not excluded: A6 places no condition on the rule (Sub:102). P1's
rules are scalar". That is true of A6-cov as an *interface* for link-coupled rules (kernel `D3-a`,
`a6cov_all`). But the corpus fixes the link interface only for additive link couplings:
- `linkF N M c i = Σ_{j∈N i} M i j (c j)`, with `M : V →+ V`;
- SM:116–118 is stated for "the wave equation".

For a non-additive rule there are two natural extensions, and they give opposite verdicts for P1.

- **(α) Link-sum.** F_i = Σ_j m_ij(x_j), with each neighbour entering through its own link map and
  the maps not required to be additive. This is A5 N9's E2 with the additivity of the maps dropped.
  - P1's class is **excluded**: its nonlinearity is a non-separable function of several neighbours.
    rv2 R4 finds a nonzero cross difference at q = 5. The q = 2 and q = 7 constructions are likewise
    non-separable (an indicator of six equal values; y₃·χ(…)).
  - Within this class, **uniform shift covariance alone forces affinity**, at every d and q, for λ = 1
    and any κ.
  - *Proof.* Σ_j m_j(x_j + c) − Σ_j m_j(x_j) = κc for all x and c. Varying only x_k shows that
    m_k(x_k + c) − m_k(x_k) is independent of x_k. By the one-variable lemma, m_k is affine.
  - rv2 R4 checks this exhaustively over all separable rules with 2 slots at q = 2, 3, 4 and with
    3 slots at q = 3. Every solution is affine.
  - So **A6 in link-sum form, together with amplitude-scale gauge in its uniform form, yields the
    base-point form and hence affinity through the lemma.** That is the route the overstating sites
    name.
- **(β) Joint insertion.** F_i = f(M_{i,1}x_1, …, M_{i,2d}x_{2d}), with transported unit links.
  - P1's class **satisfies** this at K = 1, because f is unit-homogeneous of degree 1. rv2 R5 checks
    A6-glob exhaustively at q = 5 and 7, and the one-step covariance on a 3×3×3 torus as a
    consistency check.
  - The kernel records the K = 1 rescalings as the A5 amplitude freedom, not A6's internal-index
    freedom (`A6Instantiation`, D2-i/D2-ii). So this support is weak, and no K > 1 extension of P1
    is constructed.
- **A6-inv** fails for P1 *and* for the linear rule (rv2 R5), like GA5. It is no discriminator.

**Consequences.**
1. **GA7 is reading-dependent, and in that respect parallel to GA8.** (α) excludes P1's class, while
   (β) and the prose interface do not. Unlike GA8, it is not *undetermined*: the gap is which
   extension of the link interface the corpus intends for non-additive rules, and the corpus does
   not state one.
2. **The per-site test needs an A6 column.**
   - Sub:104 states the reconstruction's premises "A1–A6 jointly" and names A6 in the same sentence
     as A5's "partly derived".
   - Sub:220 is a bullet of the A1–A6 hypothesis-dependency remark, and the next bullet is A6.
   - Read in that context under (α), P1 is outside the class, and both sites' affine claims hold
     with a corrected justification: link-sum plus uniform gauge gives the base-point form.
   - By the writer's own conservative rule (hold where a stated assumption leaves P1's status open),
     these two sites at least need an explicit disposition before their narrowing passes.
3. **Theorem recovery before concession (Code Review Rules).** The manuscript claim "amplitude-scale
   gauge restricts the update to an affine one" is refuted by P1 in the class of all centre-free,
   nearest-neighbour rules. It is recoverable, with a one-line proof, in the link-sum class.
   - Before proposing the base-point narrowing as the correction, the record should state this
     recovered result, with its hypothesis (link-sum, not stated in the corpus for non-additive
     rules), its proof, its verification (R4), and the precise remaining gap.
   - The gap is whether link-separability is an independently justified premise (§A.29).
   - The owner can then choose between two corrections: "base-point form", which is what the lemma
     needs, or "link-sum form", which is a premise the corpus does not state.
4. **Q-NEXT (§5).** Link-separability passes the P1 screen and is *sufficient* with uniform gauge. It
   belongs in the list of principles to test, ahead of the others, as the one candidate already
   known to close the implication. Its independent justification is the whole question.

### 3.6 "Undetermined" under GA8, and the Structure holds

- **"Undetermined" is correct.** The hypothesis needs a cross-q correspondence that "is not
  constructed" (SM:94). It is "posed for linear dynamics" (Structure:217). At cycle-type level it
  excludes the linear rule too (A5 N10).
- **The holds at Structure:219 and :259 are defensible as conservative.** At clause level, however,
  the overstating sentences ("An affine rule is therefore forced *given* that operational
  principle"; "amplitude-scale gauge invariance yields the affine restriction") are conditional on
  GA2 alone, and GA8 sits in other sentences. Owner Q1 offers per-site and corpus-wide readings; it
  should also offer the clause-wise reading (N5).
- **Structure:301 makes no overstatement.** "OI's [SM §4.1] argument for an affine rule rests on
  amplitude-scale gauge" is accurate, since SM §4.1 = SM:240, which carries the base-point form. So
  no proposal is needed on any reading, and the stated reason (GA8) is not the operative one (N3).
- **No proposal is made as an edit.** The quoted source text matches fd539e15, and the working tree
  of the repository is clean (`git status` empty). The proposals exist only in the file, as required.

## 4. F-7 and F-8

- **F-7 is verified.**
  - The open form is at SM:96 ("an identified open structural question") and at Sub:100 and :104
    ("an identified open step").
  - The negative form is at Sub:274 ("resolves in the negative, and sharply") and Structure:301
    ("does not entail").
  - CONFIRMING is the right class. The record already holds this inconsistency, and ASSESS does not
    cite it: H-D D6 and H-D-SR SR-1 and SR-3 record "four in the open form and one resolved in the
    negative … the disagreement stands on the record unadjudicated", and A5 C8 cites SR-3.
  - The only addition since then is Structure:301's negative form, which is absent from the
    Structure blob H-D-SR pins (`84a7ede4`) (N1).
- **F-8 is verified only relative to reading (a), and it is stronger than stated under that reading
  (R6).** Under the reading the writer applies to Sub:270, it is not a falsehood (R2-B1).

## 5. Re-runs, register and scope

- **Re-runs.** I re-ran every probe and reviewer script with `python3 -I` into `scratchpad/rv2run/`:
  `p1`, `p2`, `p3`, `r2_gauge_inventory`, `rv_p1` and `rv_p2`. All exited 0, and all outputs are
  byte-identical to the stored `.out` hashes.
- **The r2 probe.** G1–G5 are correct as stated. G4 is a minimal witness (one slot shifted changes
  the linear update), which is adequate for the claim made. G5 matches S1.
- **Generic-check boundary.** P1, P2(B), r2 and rv2 are of the same kind. P2(A), P2(C) and P3 are
  correctly marked non-evidential, and nothing rests on them.
- **Register.** ASSESS is a verification note, so §A.32 and §A.33 do not bind its own voice. The
  proposals are paper text, and they are in a neutral register with no history voice and no caps.
  But see N7 on unsupported additions.
- **Labels.** [H], [O] and [O-ext] are used consistently, and §A.46 item 7 is respected: drafts are
  used as hypotheses, not premises.
- **Scope.** F-1 is scoped to d = 2, 3 and the uniform group, and no universal negative is stated.
  The §7 pressure test item 5 ("inventory is the corpus's stated assumptions") is accurate in kind.
  Its coverage claim needs the additions of §3.2.

## 6. Nits

- **N1.** F-7 should cite H-D D6, H-D-SR SR-1 and SR-3, and A5 C8 as the prior record of the same
  inconsistency. Structure:301 is the only site added since.
- **N2.** Line 303, "Two further statements are not assumptions on the rule", lists one item.
- **N3.** In the per-site table, give Structure:301's reason as "no overstatement", not GA8.
- **N4.** GA8 and §2.1 (:211–212) say that P1 "is defined uniformly in q", which reads as
  favourable to P1. Its nonlinearity uses P^{q−2}, whose degree grows with q, so on Structure:219's
  own heuristic P1 is if anything a q-dependence candidate. "Undetermined" stands on the
  unconstructed correspondence, and should say so.
- **N5.** Owner Q1 should add the clause-wise reading of the test (§3.6).
- **N6.** Correct the `.tex` mirror ranges. Sub:100's edited clause is at Substratum.tex:745–751, not
  :750. Sub:272's dispersion sentence is at :1736–1739; only :1732 is listed. If R2-B1 is accepted,
  Sub:270's ⟺ is at :1719–1720.
- **N7.** The Sub:100, :220 and :272 proposals insert a new negative mathematical claim into paper
  prose ("global rescalings and shifts … do not imply it for d = 2, 3"). Its proof lives off `main`
  (§2.1, P1). Under the minimal-change rule and §A.46 item 1, either offer a qualifier-only variant
  or note that the counterexample and its proof must land with any such edit.
- **N8.** Complete the GA2 sources (book ch05:45 = FULL:1363) and add the non-rule-constraining
  statements (Theorem 24 (i), (iii), (iv); the master principle; SM:585 and :811). Record SM:96's
  "gauge group is the additive-automorphism group" with P1's verdict, **yes, exactly** (rv2 R3).

## 7. Summary

| ID | Kind | One line |
|---|---|---|
| R2-B1 | blocker | GA3 is read as base-point at Sub:270 and as absolute amplitude at Sub:272. Either Sub:270's "⟺" is a missed overstating site (⟹ fails for P1) or F-8's "false" is wrong. Restate F-8 as an inference failure and fix the Sub:272 proposal's non sequitur |
| R2-B2 | blocker | The proposals leave contradicted clauses: Sub:100 and ch02:84 = FULL:718 ("excluded … to the extent … assumed"), Sub:274 ("additive-automorphism group … delivers the affine restriction"), Sub:272 ("strictly weaker than the output", which the proposal's own base-point form contradicts) |
| R2-B3 | blocker | GA7 (A6) is reading-dependent. Under a link-sum extension P1 is excluded, and uniform shift gauge then implies affinity (one-line proof; rv2 R4). Needs an A6 column for Sub:104 and :220, a theorem-recovery note before narrowing, and link-separability in Q-NEXT. The inventory also omits the kernel A6 readings, SM:96's gauge-group statement, Theorem 24 (i)/(iii)/(iv) and ch05:45 = FULL:1363 |
| N1 | nit | F-7: cite H-D D6, H-D-SR SR-1/SR-3 and A5 C8; only Structure:301 is new |
| N2 | nit | "Two further statements" lists one |
| N3 | nit | Structure:301: no overstatement, not a GA8 hold |
| N4 | nit | "defined uniformly in q" reads as favourable; P^{q−2} has q-dependent degree |
| N5 | nit | Owner Q1: add the clause-wise reading of the per-site test |
| N6 | nit | `.tex` ranges: Sub:100 → :745–751; Sub:272 → add :1736–1739; Sub:270 → :1719–1720 |
| N7 | nit | The proposals add an off-`main`-supported negative claim to paper prose; offer a qualifier-only variant |
| N8 | nit | Complete the GA sources and non-rule-constraining rows; SM:96 gauge group: P1 yes, exactly (rv2 R3) |

**What re-review needs.**
- R2-B1 to R2-B3 applied.
- The GA7 row split by reading, and a per-site A6 column.
- A recovery note for the link-sum result.
- A diff check of the changed passages.

No new computation is required beyond what `rv2_gauge_audit.py` already checks.
