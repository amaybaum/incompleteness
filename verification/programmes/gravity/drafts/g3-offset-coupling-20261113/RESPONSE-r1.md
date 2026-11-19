# RESPONSE-r1: disposition of REVIEW-r1 for G3 unit 1

**Review.** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/REVIEW-r1.md`, on branch
`research/g3-offset-873-20261113` at `5fe230cd`. It reviews r1 at `e64b9a3c` and gives the verdict
REVISE: two blocking findings, nine should-fix findings and three nits.

**Response files.** `G3-UNIT1-r2.md` and `NOTES-r2.md`. The r1 files are unchanged.

**Line references.**

- "r2:n" is a line of G3-UNIT1-r2.md.
- "N2:n" is a line of NOTES-r2.md.
- Corpus lines refer to `main` at `c3b5f37a`. NOTES-r2.md §3 records that every changed citation was
  re-checked there.

## Summary of dispositions

| Finding | Disposition | Where in r2 |
|---|---|---|
| B-1 | Applied | r2:35–58, r2:328, r2:378–380, r2:409–452, r2:486–489, r2:535–542, F8 r2:567 |
| B-2 | Applied | r2:187–202, r2:493–526, r2:543–550, F6 r2:565, F9 r2:568, AW-G12 r2:585 |
| S-1 | Applied differently | r2:267–273, r2:300–308, r2:50 |
| S-2 | Applied | r2:46–47, r2:334–341, F3 r2:562 |
| S-3 | Applied | r2:353–357, r2:263–264 |
| S-4 | Applied | r2:310–317, B1 r2:362–372 |
| S-5 | Applied | r2:387–389 |
| S-6 | Applied | r2:247–254, F4 r2:563 |
| S-7 | Applied | F5 r2:564, r2:570–575, AW-abs r2:581–584, Q3 N2 |
| S-8 | Applied | r2:196–197, P4 in the table at r2:110 onward |
| S-9 | Applied | r2:275–281, r2:549 |
| N-1 | Applied | r2:106–108, r2:155–158, F7 r2:566, N2 §2 |
| N-2 | Applied | K9 r2:98 |
| N-3 | Applied | r2:366–367, r2:516, r2:523, §7 r2:591 onward |
| Review answer 7: smaller obligation O0 | Assessed as correct and adopted as the first obligation. It is addressed on paper in B5. | r2:535–542 |
| Review answer 8: register | Applied ("the non-implication at GR:352 holds") | r2:357, F1 r2:560 |

## Per finding

### B-1. Requirement (ii) is an omitted OI datum. Applied.

- **Node B5** is added at r2:409–452.
  - (i) is satisfied: ρ(r) is definite on shell.
  - (iii) is satisfied, by GR:751.
  - For (ii) the node states a strong reading (ii-S) and a weak reading (ii-W). It shows that (ii-S)
    excludes K_cpl and every λ ≠ 0, and that (ii-W) does not.
  - The node gives the support class: GR:342–348 is a paper argument, not kernel-checked, and
    book/ch07-gravity.md:187 is the book's mirror.
  - The node cites GR:358 and GR:400 (Reading 1) as the reading the corpus uses.
- **A further step beyond the review.** B5 also examines which reading GR:346's own argument supports.
  - For the uniform term, the origin is not an output of the QM description: (TL) leaves it free (K1,
    K5–K7).
  - On shell, K_cpl determines the origin from the metric (§3.1, r2:310–317). That is the order
    metric → origin.
  - So the QM → metric loop that GR:346 excludes does not close through the uniform term, and the
    argument supports only (ii-W).
  - B5 also records that GR:400 itself names "Reading 2 (strict geometry-first)", which corresponds to
    (ii-S) for the source, and does not adjudicate it.
  - Adopting (ii-S) would also remove the corpus's Reading 1 and the feedback stated at GR:358. That is
    recorded as the §A.31 pressure test of the branch that favours decoupling (r2:446–448).
- **B2(a)** is replaced as the review proposes (r2:378–380).
- **§3.2** has the new row (r2:328).
- **§0** makes the verdict conditional on B5 (r2:35–58). B5 finds that (ii), as argued and as used, does
  not exclude K_cpl, so "counterexample" stands. (ii-S) is named as route R0 (r2:486–489). The branch
  in which (ii-S) is read in, giving "conditional on requirement (ii) read strongly", is stated at
  r2:53–58.
- **Difference from the review.** None in substance. The added step, that GR:346's argument does not
  reach the uniform term, is a reason for B5's verdict. The review asked for the strong and weak
  readings, and that reason is offered as the basis for choosing between them. It is new reasoning
  and needs review (owner question Q8, N2).

### B-2. R2 and O1 misstate the admissible trace sector. Applied.

- **R2 is rewritten** as R2a and R2b (r2:493–526).
  - **R2a: trace-free left side.**
    - The trace of the equation forces the additive constant to be zero.
    - Bianchi and conservation give `∂(R + 8πG T) = 0`, which supplies the integration constant Λ_int.
      The algebra is at r2:498–503.
    - R2a lies outside the class 𝒞_div. A separate class, 𝒞_tf, is defined in §2 (r2:187–188).
  - **R2b: divergence-free left side.**
    - (Adm2) forces `∂ℱ = 0`, so `ℱ = ¼T` violates conservation.
    - The equivariant, conserved choices are spacetime constants such as `¼⟨T⟩`. This is the
      sequestering structure.
    - R3 of r1 (sequestering) is merged into R2b. The old R4 (substratum phase) is renumbered R3.
- **"ℱ = const fails" is kept** (r2:495).
- **(SI′) is added** at r2:199–202. R2a shows that in an integration-constant theory, SI′ holds over
  the whole solution set. At fixed data, SI′ holds if and only if the datum that selects the solution is
  a function of κ alone (r2:504–510).
- **The Jacobson null-flux route is connected** (SM:160–162; r2:511–514). The null flux does not see
  `−ρg`, and the Λ displayed at SM:162 is the integration constant.
- **O1 is restated** in the review's words, carrying the left-side form and conservation (r2:543–550).
- **The GR:12 clause is conditional** on an equivariant (E, ℱ) pair. This is recorded as AW-G12
  (r2:585) and in F6. No manuscript change is made.
- **Difference from the review.** One sentence is added: whether unimodular gravity removes the
  vacuum-energy problem is debated on exactly the question of the selecting datum. It is labelled
  [L, recalled], and no verdict rests on it. A one-line conjecture is also recorded: a cycle average
  over OI's finite recurrence (GR:585) is one candidate for a spacetime-global ℱ (r2:525–526). It is
  labelled conjecture, it is not examined, and it is not adopted.

### S-1. "Differ only" does not hold for `e = tr(ρΩ)`. Applied differently.

- r2 adopts the review's first option, `e(r) = min_a E_a` (r2:267).
- **Change from the review.** `min_a E_a` also responds to the antiunitary branch. A short argument
  shows that no shift-equivariant functional can be invariant under the reflection (r2:305–308).
- "Differ only" is therefore scoped to the oriented branch, which a passive non-uniform state selects
  (K11). Within the class [r] fixed by κ, the remaining freedom is the shift, the D-gauge, the
  eigenframe phases and the branch (r2:300–303).
- The verdict line at r2:50 says "On the oriented branch". The correction to NOTES-r1:104–105 is
  recorded in N2 §4.

### S-2. Generalization from a finite list. Applied.

- The claim is narrowed to "the operational content of the emergent generator" (r2:46–47, F3).
- r2:334–341 adds that the corpus's absolute emergent quantities (GR:332, GR:336, GR:358) depend on the
  representative, and that K_cpl couples to such a quantity.

### S-3. The justification for relabelling `T^cl`. Applied.

- The relabelling is now justified by the classical-origin freedom (B2(c), GR:58) (r2:353–354 and the
  data list at r2:263–264).
- The third reading, ρ_C = 0, is marked as giving an empty claim (r2:355–357).

### S-4. The countermodel is off shell. Applied.

- The on-shell paragraph is added (r2:310–317): K_cpl's field equation fixes the origin from the
  metric, the worlds are identical at r₀, and the counterfactual difference is stated.
- B1 is amended: K_cpl needs no outside structure to select a representative (r2:369–370).

### S-5. Per-cell vacuum stress labelled [A]. Applied.

The claim is relabelled: [A], conditional on a covariant continuum limit in which a uniform per-cell
energy has vacuum stress. That limit is open: GR:12, GR:697(ii) (r2:387–389).

### S-6. F4 classed NEW. Applied.

- F4 is reclassified ELABORATING (mechanism and target form).
- It cites GR:579 and AUDIT.md:55 and :371–378 (item 2.9) (r2:252–254, F4, and P17 and P30).

### S-7. F5 and Q3. Applied.

- F5 is rewritten in the review's terms (r2:564). "E_D" is dropped.
- The algebra block includes the 2ρ_crit check (r2:570–575).
- AW-abs names the GR:426 attribution sentence (r2:581–584).
- Q3 is restated in N2.

### S-8. Wrong support label. Applied.

The converse is now labelled "[K] for each step (K7, K5–K6), [P] for their composition (GR:747)"
(r2:196–197, and P4).

### S-9. Undefined λ-family. Applied.

The λ-family is defined at r2:275–281, with λ = 0 as K_dec and λ = 1 as K_cpl. It is referenced in O1
(r2:549).

### N-1. Inventory lines and the Λ claim. Applied.

- The docstring line numbers are corrected, to :8 for `shift_normSq` and :9 for `reflect_normSq`
  (r2:106–108, F7).
- The Λ sentence is replaced (r2:155–158). The new sentence cites SecondOrderDrive.lean:59 and :361 and
  MinimalRepertoire.lean:21, each re-checked.
- OrientationClosure.lean (:135–141, :256–265, reflection form only) is added to the hit list in N2 §2.

### N-2. Hypotheses of K9. Applied.

"`W W† = 1` at :446" is added (r2:98). This was re-checked: PairIdentification.lean:448 carries
`hW : W * Wᴴ = 1`.

### N-3. Literature line references. Applied.

- Weinberg: listed at Introduction:288 and cited at :157.
- EvEMU11: listed at :244 and cited at :161.
- KP14: listed at :258 and cited at :161.
- The Wald entry gives the book, with the section number marked as recalled and not verified (r2:604).

### Review answer 7: the smaller obligation O0

**Assessment: correct.** O0 is logically prior to O1, because a strong reading of (ii) would settle
(SI) for the uniform term without O1. It is smaller, because it is a reading of a paper argument
rather than a G3 derivation.

**Adopted as the first obligation** (r2:535–542). Its status is "addressed on paper in B5, pending
review".

**What remains is not a proof obligation.** It is an owner decision about a premise: whether to adopt
(ii-S), which corresponds to GR:400's Reading 2, under §A.29. That decision is Q7 in N2.

### Review answer 8: register. Applied.

"The substance of GR:352 stands" is replaced by "the non-implication at GR:352 holds" (r2:357, F1).

## Findings not applied

None. S-1 is applied differently, and the reason is given above. Two items in B-1 and B-2 go beyond the
review, and both are marked for review. B-1 adds the argument that GR:346 does not reach the uniform
term. B-2 adds the recalled unimodular debate and the conjecture about a recurrence average.
