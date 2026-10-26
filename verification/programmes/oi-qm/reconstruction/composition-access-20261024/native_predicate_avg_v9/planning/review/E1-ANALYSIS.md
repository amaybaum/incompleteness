# E1 analysis: C7 set 2, orbit reduction, the G decomposition, count semantics

**For:** the owner's rulings of 2026-10-26 and their refinements, on erratum E1
(`stage0/amendments/E1-LAYER1-ERRATUM.md`, `c00b4486…12ab`, at `21d25752`) and on my review
(`review/E1-REVIEW.md`, at `47e16576`).

**Read-only. Toy and planted instances only.**
- Nothing was edited or committed.
- Nothing touched v8's configuration class: the script asserts that the setup is not v8's.

**Evidence**, in `S/npavg/review-e1/analysis/`:
- `e1_analysis.py` (`059739e4…a4a3`) runs on the Layer 2 r2 code at `4a51c675`, toy profile.
- Its output is `e1_analysis.out` (`c9822a43…31c6`). It exits 0, all 27 checks pass, and the
  output is byte-identical under `-O`.
- `timing_toy.py` and `timing_toy.out` hold timings. They are not deterministic.

**How to read this document:**
- **Proved** means a written argument from r5's definitions. Each such argument is checked on the
  toy class.
- **Observed (toy)** means a toy number. It says nothing about v8.

## Summary of conclusions

1. **C7 set 2 gives distinct coverage information, not distinct tie information.**
   - Under A, set 2 is always contained in the survivors: it is redundant there (proved).
   - Under G, set 2 is (T_G ∩ Surv_G) ∪ F_G. Here F_G is the set of records whose *in-frame*
     quantities have a shared near tip, and it can be computed without any closure (proved).
   - These in-frame ties are inert. They never affect a survivor, linkage, rule-T input or label
     (proved).
   - What C7 on set 2 adds is verification of the whole closure on every such record. No other
     in-run check covers that population in full. Two planted faults show this, one of them a
     fault on an orbit member alone.
2. **Orbit reduction preserves C7's verdicts and multiplicities, but not failure detection**
   (proved, then shown with a planted fault).
   - Verdicts and multiplicities: for the results the run reports, which are carried from the
     representative, the verdict on a member equals the representative's.
   - Failure detection: a fault that shows only on a non-representative member is invisible in
     the carried results. Only a direct computation on that member detects it.
   - Under the owner's refined criterion, sets 1 and 2 therefore keep the full record population,
     with a direct production closure and a reference closure for every member.
   - The *reference* computation may use Lemma G-D below. It is a proved, equivalent optimization
     of the reference, not of the population, and it is about ten times faster on the toy class.
3. **E1-F3's set 2, as drafted, hides a class of faults.** It is defined by the *computed*
   closure, so a fault that destroys a tie removes its record from the set. The planted fault F1
   is caught on 0 of 595 records. Defining set 2 by the closure-free F_G gives the same population
   under the specification and catches F1 on all 595 records.
4. **The structural property (Lemma G-D) is proved, but it is not NEW.** The G closure splits into
   the in-frame part, which is always retained and inert, and the greatest self-supporting subset
   of the seed part, where covers come only from the seed part itself. The lemma is a corollary of
   PO7 and r5's definitions, so the §A.31 class is ELABORATING. It is useful as a cost reduction.
   The "595 of 1,400" is a toy frequency.
5. **Counts: 58 is complete.**
   - The two added degeneracies are well defined, C4v-invariant record predicates, and they are
     counted by exactly the convention of the other eight.
   - Their survivor cells (E1's 4) are not redundant. Their non-survivor cells are determined
     (plain count minus survivor cell).
   - 62 and 60 carry the same information as 58 (equal rank). Under the owner's instruction, 58
     stands. Masking equivalence (D9) differs from the other nine in one respect: it is relative to
     the record space, not intrinsic to a record. It is well defined all the same.

## A. The C7 question

### A1. Definitions and facts (proved)

Write Q⁰(R) for the non-fixed quantities of Ctx(R).
- Under G, split Q⁰(R) into **In(R)**, the quantities with no seed tip, and **Out(R)**, those with
  a seed tip.
- By PO7, q = (c, t) is in Out(R) iff |c| + t > 8 when t ≥ 0, or |c| > 7 when t = −1.

**Lemma G-D** (the G decomposition). For every record R and both rules L3′ and L3:

ret_G(R) = In(R) ⊔ W(Out(R)).

Here W(X) is the greatest subset Y ⊆ X such that every eligible tip of every y ∈ Y lies in the
cone of some y′ ∈ Y with y′ ≠ y. Fixed quantities and In(R) take no part in the covering.

*Proof.*
1. **Eligible tips lie outside the frame** (L1 §2).
2. **Cones of fixed quantities lie inside the frame.** The frame is the union of the G cones of Φ,
   V, p and the even port samples. Each fixed quantity's cone is therefore inside the frame by
   definition.
3. **Cones of In(R) lie inside the frame.**
   - For t ≥ 0, by PO7: |c| + t ≤ 8.
   - For t = −1 the quantity is B type at depth 0, so its cone is itself, which lies at |c| ≤ 7 on
     slice −1. That is inside the frame.
4. **Hence no fixed or in-frame quantity covers an eligible tip.**
5. **Quantities of In(R) are never eliminated:** they have no eligible tip, and elimination
   requires a free eligible tip.
6. **Conclusion.** The elimination dynamics of Out(R) are therefore exactly the computation of
   W(Out(R)), and In(R) is retained in full. The same holds for L3, whose tips are a subset of
   L3′'s and whose cones are the same. ∎

*Toy check.* On all 1,400 records, ret_G equals In ∪ W(Out) computed by `s0ref`. The cones of
fixed and in-frame quantities contain no eligible cell (A3, three checks).

**Corollaries** (proved):
- **(i) G-survival comes from Out(R) alone.** S_G(R) = W(Out(R)), so G-survival and G-linkage
  depend only on Out(R).
- **(ii) Set 2 under A is redundant.** T_A ⊆ Surv_A, because ret_A contains non-fixed quantities
  only. Any shared tip among them makes S_A non-empty.
- **(iii) Eligible ties are survivors.** A retained shared near tip that is eligible is a seed tip
  of a retained quantity, so it lies in S_G. Hence T_G^elig ⊆ Surv_G.
- **(iv) Set 2 under G.** T_G = (T_G ∩ Surv_G) ∪ F_G, where
  F_G = {R : In(R) has a shared near tip}.
  - For a non-survivor, ret_G = In(R), by Lemma G-D and (i).
  - Conversely, In(R) ⊆ ret_G(R) always.
  - F_G needs no closure.
- **(v) In-frame ties are inert.** They lie in In(R), which covers no eligible tip. So they affect
  no survivor, no linkage, no L_A or L_G input and no label.

**Observed (toy).**

| quantity | A | G |
| --- | --- | --- |
| Surv | 0 | 0 |
| T (set 2, any tip) | 0 | 595 (283 orbits) |
| T with eligible tips only | 0 | 0 |
| F_G (in-frame tie, closure-free) | — | 595 |
| I (initial-context tie) | 1,071 | 667 |
| I ∖ (Surv ∪ T) | 1,071 | 72 |
| I ∩ H₁₀₀ (record index) | 12 | 6 |
| H₁₀₀₀ (record index) | 1 | 1 |

Every set is a union of C4v orbits (A2). The identity T_G = (T_G ∩ Surv_G) ∪ F_G holds, 595 = 595.

### A2. Does set 2 give information distinct from the survivors and the samples?

**Ties: no.** By (v) the ties themselves carry no masking information: under G they are inert.

**Coverage: yes.** C7 on a record of set 2 checks that the production closure equals the reference
closure of that whole record. Under G this means that Out(R) is reduced to W(Out(R)) correctly and
that In(R) is retained. The population F_G is disjoint from Surv on non-survivors. It meets the
sampled sets only at their sampling rates. So C7 on set 2 is the only in-run check that verifies
every record of F_G.

**Per-record capability: redundant with C17 ∧ C18, documented, not removed.**
- *Proved.* On a record where C0, C17 and C18 all pass, together with the code invariant
  "retained ∪ logged = Q⁰":
  - C17 shows that ret is self-supporting, so ret ⊆ the greatest self-supporting subset (GSS);
  - C18 shows that no logged elimination removed a GSS member, so GSS ⊆ ret;
  - hence C7 passes. C7 is implied by C17 ∧ C18 on the same record. The converse fails: a correct
    final set with an unjustified logged reason fails C18 but passes C7.
- C7's distinct value is therefore a second, independent algorithm, not detection power beyond
  C17 ∧ C18. In-run, however, C17 and C18 run only on survivors and at 1 in 1,000. That is why
  C7 on set 2 does detect what the other in-run checks miss.

**Planted faults** (toy G, with the v8 in-run rates applied to toy indices; `planted_faults_G`):

| fault | wrong reported results | wrong direct results | set 2, as drafted (computed closure, orbit-reduced) | set 2, recommended (F_G ∪ (T ∩ Surv), direct per member) | I ∩ H₁₀₀ | H₁₀₀₀ | C11 (i), C17, C18 at 1 in 1,000 | C8, 1-in-100 orbits |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **F1:** equivariant; drops every retained in-frame quantity with a shared near tip | 595 | 595 | **0** | **595** | 6 | 1 | 0 | 0 |
| **F2:** F1 on non-representative members only | 0 | 312 | 0 | **312** | 0 | 0 | 0 | 0 (none of the affected orbits sampled) |

- **F1** shows the self-masking of the drafted definition. The fault destroys the tie, so the
  computed closure no longer has one, and the record leaves set 2.
- **F2** is invisible in every reported result, because reported results are carried from correct
  representatives. Only a direct computation of the member detects it.
- **Caveat** (§A.31, skepticism). On the toy class, the *pre-flight* already runs full C7, C11 (i)
  and C18 on every toy record, so F1 and F2 would be caught before any v8 run. What set 2 adds
  in-run is detection of faults whose trigger geometry occurs on v8 but not on the toy class.
  That cannot be demonstrated without v8; F1 and F2 stand in for such faults.

### A3. Orbit reduction: what it preserves

**Theorem** (C7 verdict equivalence; proved). Let R′ = gR, and let the reported production result
of R′ be prod_rep(R′) = g · prod(R), carried from the representative R. The specification's GSS
is C4v-equivariant: contexts, cones, tips and the frame are mapped by g (PO-L2-3), and the GSS is
a set function of them. Then:
- prod_rep(R′) = GSS(R′) ⇔ prod(R) = GSS(R);
- set membership in Surv, T, F and I is orbit-invariant, because g maps e-tips to (g·e)-tips;
- multiplicities are therefore orbit sizes.

The reference code implements the GSS with set operations that commute with g, both by brute force
and by synchronous deletion. Toy check: the reference and the production are equivariant on all
1,400 records, and the member verdict equals the representative verdict on all of them (A1).

**What the theorem does not give: failure detection.**
- A non-equivariant fault in the production engine changes no carried result, so it is not
  detected by checking representatives. F2 is an example.
- The same holds for a non-equivariant fault in the reference.

Under the owner's refined criterion ("including … failure detection; a fault that shows up on one
orbit member and not on the representative must still be caught"), the reduction is **not**
admissible for C7's populations.

**Recommended computational unit.** The population is every record, by record index. For each
record R in sets 1 and 2, and for each sampled record of sets 3 and 4:
- R's production closure is computed directly, and R's reference closure is computed in R's own
  reference context;
- C7 fails if the direct production closure ≠ the reference closure;
- C7 also fails if the carried result ≠ the direct production closure, which is C8's comparison
  applied to R.

Both failures are VOID. Report both raw-record coverage (records checked, by set) and orbit-level
coverage (orbits touched, with the sum of orbit sizes).

**The permitted optimization is in the reference, not the population.** Under G, the reference
may compute W(Out(R)) and add In(R), by Lemma G-D. Conditions:
- Layer 2 states it as a proof obligation;
- on the toy class, and on every record of sets 3 and 4, it is checked against the full `s0ref`
  closure.

Toy timing: 2.46 ms for the full reference against 0.25 ms via G-D (1,400 records, 1,400 equal).
The production engine is not changed.

**Cost.**

cost(set 2) = 2 · |F_G ∪ (T_G ∩ Surv_G)| · (t_prod,G + t_ref,G)

The factor 2 is the `-O` run. In this formula:
- t_prod,G is measured at about 4.3 ms on 16-quantity planted sets (Layer 2 F9);
- t_ref,G is 90–280 ms in full form, much less via G-D;
- |F_G| can be computed in the dry run **without any closure**, by Corollary (iv). I did not
  compute it for v8.

On the toy class, set 2 is 595 of 1,400 records. If v8's fraction were similar, full-form
reference cost alone would be far beyond S7's budget, which is why G-D matters. The dry run must
report |F_G| before κ is decided.

## B. Count semantics

**Notation.** ℛ is the k ≤ 2 record space. s_c(R) is "R is a survivor under c", with L3′
(L1 §3). For a record predicate D:
- n(D) = #{R ∈ ℛ : D(R)};
- n(D, c, v) = #{R ∈ ℛ : D(R) ∧ s_c(R) = v}.

The identity n(D, c, True) + n(D, c, False) = n(D) holds for c = A and c = G.

**The ten degeneracies** of §3, as record predicates, are those of code-r5 and Layer 2
(`l2analysis.degeneracies`):

| # | predicate D(R) | kind |
| --- | --- | --- |
| 1 | some item's site is q9 | intrinsic |
| 2 | some item's site is a Φ site | intrinsic |
| 3 | some item's site is the port site | intrinsic |
| 4 | some item's site lies on the z-axis | intrinsic |
| 5 | k = 2 and the two sites differ in exactly one coordinate | intrinsic |
| 6 | the stabilizer {g ∈ C4v : gR = R} is not {1} | intrinsic |
| 7 | some item has t ≤ 0 | intrinsic |
| 8 | some item has t = −1 | intrinsic |
| 9 | some R′ ≠ R in ℛ has Ctx(R′) = Ctx(R), with odd-class samples dropped (equivalence E2) and identity merges applied (equivalence E1) | **relative to ℛ** |
| 10 | some item (x, t) has \|x\| + t odd | intrinsic |

All ten are well defined. All are C4v-invariant (toy check for 6 and 9: B.both_predicates…). So
all are orbit-reducible.

**The counting convention of the existing eight** (D = 1–5, 7, 8, 10). The listed counts are
n(D, c, True) and n(D, c, False) for c ∈ {A, G}: four cells per D, 32 in all. n(D) is **not**
listed. It is implied, twice.

**Under the same convention, the candidates for D = 6 and D = 9** are n(D, c, True) and
n(D, c, False), for c ∈ {A, G}: 8 cells. The frozen list already contains n(6) and n(9).

**Reconciliation table** (per D ∈ {6, 9}):

| list | listed for D | determined, not listed | independent numbers (rank) | redundant listed |
| --- | --- | --- | --- | --- |
| r5, 54 | n(D) | — | 1 | 0 |
| **E1, 58** | n(D), n(D, A, T), n(D, G, T) | n(D, A, F), n(D, G, F) | **3** | 0 |
| 62 | n(D), all four cells | — | 3 | 2 |
| 60 | the four cells | n(D) | 3 | 1 (A-sum = G-sum) |
| the existing eight (for comparison) | the four cells | n(D) | 3 | 1 |

**Totals:**
- 54 = 52 non-degeneracy-plain counts + 2 plain counts.
- 58 = 54 + 4 survivor cells.
- 62 = 58 + 4 determined cells.
- 60 = 62 − 2 frozen plain counts.

**Decision: 58.**
- **Well defined.** All cells of D6 and D9 are counts of records under the same predicate-and-status
  convention as the other eight.
- **Required and not redundant.** The 4 survivor cells E1 adds cannot be derived from the 54.
  E1-check part D shows them nonzero on planted records.
- **Determined.** The remaining 4 non-survivor cells follow as n(D) − n(D, c, T).
- **Complete.** 58 therefore reaches the maximal rank (3 per D), and no additional nonredundant
  cell exists.
- **The asymmetry with the eight** is one of presentation only: the plain marginal is listed in
  place of the two non-survivor cells. It is explained by the frozen list's prior inclusion of
  n(6) and n(9). Under the owner's instruction, symmetry alone does not justify 62.
- **Toy check.** The marginal identities hold for D6 and D9 under A and G (all survivor cells are 0
  on the toy class). Survivor status is constant on masking-equivalence classes, since equal
  contexts give equal closures (B).

**The note on D9.** Masking equivalence is relative to ℛ, which makes it the one non-intrinsic
degeneracy. That is not an obstacle to well-definedness or invariance: C4v maps ℛ onto itself and
contexts equivariantly. But D9's value on a record depends on the whole domain, and it should be
said so in the definition.

## C. S1a status: wording consistent with the owner's precedence ruling

> **S1a's status σ is a diagnostic status of the S1a computation, not a run label.** It is
> computed as in E1-T2 (cases 1–4), with the reference check of L_A and L_G added (E1-T2,
> case 2 (d)). Rule T is evaluated iff σ = OK. σ never overrides the run's label: the label is
> generated by L1 §5 from every mandatory check. A failure of S1a's own checks enters that label
> through §5 like any other failed control (VOID for case 2, MISMATCH for case 3, INCOMPLETE for
> case 1). A run with σ = OK carries VOID, MISMATCH or INCOMPLETE whenever another mandatory check
> fails. When rule T is evaluated in a run whose label is VOID, MISMATCH or INCOMPLETE, its outcome
> is recorded with that label beside it, as a geometric property of the certified bound; no
> proposal under rule T is made from such a run without the owner's separate decision.

## D. Exact replacement text for E1

The edits below are to `E1-LAYER1-ERRATUM.md` (sections as numbered there). They apply my review's
R1–R5, the owner's rulings and refinements, and §A–C above.

**D0. Naming (R5).** In §0, after "**How E1 governs.**" add:
> Tags of the form E1-T1, E1-F3 … name items of this erratum. The equivalences of r5 §1 are
> written "equivalence E1" … "equivalence E4".

In §8, replace "with odd-class samples dropped (E2) and identity merges applied (E1)" with "with
odd-class samples dropped (equivalence E2) and identity merges applied (equivalence E1)".

**D1. Rule T qualification** (a new §6a, after "Not governed by E1", which it replaces):
> **E1-T6, the standing of rule T's consequence.** Ruling: "geometric fact only": "Approved, with
> qualification. Rule T may be used as a geometric property of the specified closure. It must not
> be presented as a probabilistic result, empirical observation, or independent theorem about the
> full model" (amaybaum, 2026-10-26). The pending-owner marks at L1 lines 1001–1004 and 1033–1035
> are resolved accordingly. The L_A = L_G = 0 branch reads: "No record whose items lie in
> Reg × {−1, …, 23}, of any size, has a linked survivor under the specified closure (L3′, the
> declared conventions and frame). This is a geometric property of that closure. It is not a
> probabilistic result, an empirical observation, or an independent theorem about the full model,
> and no law statement is made beyond k ≤ 2." `result.json` records this text under
> `rule_T.statement_scope`.

**D2. E1-T2, replace the "Added definition" through "Consequences" with:**
> **Added definition.** S1a's status σ ∈ {OK, VOID, MISMATCH, INCOMPLETE} is a diagnostic status
> of the S1a computation (the owner, 2026-10-26: "Give S1a its own diagnostic status, not an
> overriding success label"). It transcribes Layer 2 r2 (`4a51c675`, `l2s1a.run` and
> `l2merge.merge`), including the reference checks of the L3 bound that L2-R8 added; those only add
> non-OK cases. The first matching case applies:
>
> 1. **INCOMPLETE** if (a) S1a's structured output is missing, which includes every case in which
>    S1a refused to start for want of certificate items 1, 2, 3, 6 or the dry run (item 7); or
>    (b) its normal and `-O` outputs are not byte-identical, or one is missing; or (c) its code or
>    configuration digest differs from the frozen Layer-2 manifest.
> 2. **VOID** if, on any of the four bound closures ret^ρ_c(U) (c ∈ {A, G}, ρ ∈ {L3′, L3}):
>    - (a) C0 fails: the production context of U differs from `s0ref`'s;
>    - (b) C17 fails: by `s0ref`'s cones and tips, a quantity of the bound has a free eligible tip;
>    - (c) C18 fails: a logged elimination is not justified by `s0ref`;
>
>    or if (d) L_A or L_G, recomputed from the L3′ bounds with `s0ref`'s explicit cones and tips,
>    differs from the production value (ruling: "Add it"). The L3 values are recomputed the same
>    way and any difference is reported; it is not a σ condition, since the ruling names L_A and
>    L_G. For the L3 closures,
>    (b) and (c) use near tips only.
> 3. **MISMATCH** if (a) a fixed quantity appears in the elimination log of a bound closure; or
>    (b) ret^{L3′}_c(U) ⊄ ret^{L3}_c(U); or (c) the in-run C9 gate fails on a record R of an
>    accepted shard. In (c), ret_c(R) is the run's computed closure of R (E1-F3), and the gate fails
>    if ret^{L3′}_c(R) ⊄ ret^{L3}_c(R), or ret^{L3′}_c(R) ⊄ ret^{L3′}_c(U), or
>    ret^{L3}_c(R) ⊄ ret^{L3}_c(U).
> 4. **OK** otherwise.
>
> σ reads C9 only on accepted shards. Shard completeness is not an input of σ; it determines the
> run's INCOMPLETE label under L1 §5. The order of cases 1–3 fixes only the recorded name.
>
> **Precedence.** Rule T is evaluated iff σ = OK. σ never overrides the run's label, which L1 §5
> generates from every mandatory check. A failure in case 1, 2 or 3 enters that label as an
> INCOMPLETE, VOID or MISMATCH reason respectively. A run cannot pass because σ = OK if any other
> mandatory check fails (the owner, 2026-10-26). When rule T is evaluated in a run whose label is
> VOID, MISMATCH or INCOMPLETE, its outcome is recorded with that label beside it. No S1b proposal
> is made from such a run without the owner's separate decision.
>
> **Why σ = OK certifies the bound** (the argument the precedence rests on). C0 gives
> Ctx_prod(U) = Ctx_ref(U). The closure code partitions Q⁰ into the retained and the logged (a
> code invariant). C18 then gives that no logged elimination removed a member of the greatest
> self-supporting subset (GSS), so GSS ⊆ computed. C17 gives that the computed bound is
> self-supporting, so computed ⊆ GSS. With 2 (d), the inputs of rule T are certified by `s0ref`
> independently of the production code and of the records' closures.

**D3. E1-T5:** no change.

**D4. E1-F3, replace "Definitions" through "Checkpoint" with:**
> **Definitions.**
> - *Shared near tip*: as drafted, for a set Q of non-fixed quantities, a convention c and an axis
>   direction e. Eligibility plays no part.
> - *Q⁰(R)*: as drafted.
> - *In(R), Out(R)* (convention G): the quantities of Q⁰(R) without, respectively with, a seed tip.
>   By PO7, q = (c, t) is in Out(R) iff |c| + t > 8 for t ≥ 0, or |c| > 7 for t = −1.
> - *Lemma G-D* (proved here; a proof obligation of this erratum): for every R and both rules,
>   ret_G(R) = In(R) ⊔ W(Out(R)), where W(X) is the greatest subset of X whose every eligible tip
>   lies in the cone of another of its elements. *Proof:* eligible tips lie outside the frame
>   (L1 §2); the cones of the fixed quantities lie inside it by its definition, and those of In(R)
>   by PO7 (t ≥ 0) or because a slice −1 quantity's cone is itself at |c| ≤ 7; so neither covers an
>   eligible tip; quantities of In(R) have no eligible tip and are never eliminated; hence Out(R)
>   is reduced exactly to W(Out(R)). The same holds for L3. ∎
> - *Computed closure*: as drafted.
>
> **The scope.** For each convention c, C7 runs on every record of the following sets. The
> population is the record space ℛ, indexed by `record_at`, with every record counted:
> 1. **Surv_c:** every record that the run computes to be a survivor under c.
> 2. **Set 2:**
>    - under A: T_A, the records whose computed closure has a shared near tip. T_A ⊆ Surv_A,
>      because ret_A contains non-fixed quantities only (proved), so set 2 adds no record under A;
>    - under G: (T_G ∩ Surv_G) ∪ F_G, where F_G = {R : In(R) has a shared near tip}. By Lemma G-D
>      this equals T_G under the specification. F_G is computed from Q⁰(R) without any closure,
>      so a fault that destroys a tie cannot remove its record from the set. The ruling retains
>      these records ("Retain the approved shared-tip closure scope, including G's 595 records"),
>      although their ties are inert by Lemma G-D.
> 3. **I_c ∩ H₁₀₀:** every record whose initial context Q⁰(R) has a shared near tip under c and
>    whose record index lies in the 1-in-100 sample H₁₀₀.
> 4. **H₁₀₀₀:** every record whose record index lies in the 1-in-1,000 sample H₁₀₀₀.
>
> **The samples** (R1; the owner: "Every record index"). H₁₀₀ and H₁₀₀₀ are drawn over every record
> index i ∈ [0, N). Record i is in the sample of stream X at rate r iff the first eight bytes of
> SHA-256(salt | X | i), read as a big-endian integer, are 0 mod r. The salt and the stream names
> are configuration constants under certificate item 1, frozen before any v8 output; the two
> streams are distinct.
>
> **The check on each record R of the scope.**
> - R's production closure is computed directly on R.
> - R's reference closure is computed in R's own reference context.
> - C7 fails on R if they differ, or if the run's reported (carried) result for R differs from R's
>   direct closure.
> - Under G, the reference may compute W(Out(R)) ∪ In(R) by Lemma G-D. Layer 2 then checks this
>   form against the full `s0ref` closure on the whole toy class and on every record of sets 3
>   and 4; a difference is a C7 failure.
> - A C7 failure is VOID under L1 §5. C7 may run on further records.
>
> **Orbit reduction.** Orbit representatives may replace records only where an equivalence is
> proved for every required result. For C7 verdicts on reported results, multiplicities and
> set membership it is proved (C4v-equivariance of the specification; sets are unions of orbits).
> For failure detection it is not: a fault confined to a non-representative member changes no
> carried result. C7 on its scope is therefore computed per record, as above.
>
> **Coverage reporting.** Each shard writes, and `result.json` sums, per set 1–4 and per
> convention:
> - records checked and failed;
> - orbits touched;
> - the sum of the touched orbits' sizes.
>
> **What changes.** C7's pass condition changes: it now applies on the scope above. The masking
> law, the domain and the labels do not change. Since T_c ⊆ I_c, the scope is the frozen literal
> scope except that the records of I_c outside sets 1 and 2 are checked at 1 in 100. C11 (i) and
> C18 still re-check eliminations on their samples and on every survivor, and C17 the fixed point.
> On a record where C0, C17 and C18 all run, C7 is implied by them (proved). C7's distinct
> contribution is its independent algorithm and its coverage of sets 1–4. This redundancy is
> recorded, not grounds for removal.
>
> **Checkpoint (§A.41).**
> - The per-set tallies above.
> - The configuration digest covers the salt, the streams and the rates (certificate item 1).
> - The dry run computes |F_G|, records and orbits, without any closure, and the C7 cost term from
>   it (L2-R6).
> - Layer-2 self-tests:
>   - the samples are deterministic over record indices;
>   - Lemma G-D's form equals the full reference on the toy class;
>   - a planted fault that removes in-frame tied quantities (F1) is caught on every affected record
>     of set 2;
>   - a fault on non-representative members only (F2) is caught by the direct per-record check;
>   - a mutant that defines set 2 by the computed closure is killed by F1's case.
>
> **Consequential replacements.**
> - L1 line 1041 (S5) reads: "C7 sampling: every survivor; set 2 of E1-F3 (under G, every record
>   with an in-frame shared near tip, or a survivor whose computed closure has a shared near tip);
>   a deterministic 1-in-100 sample, over record indices, of the records whose initial context has
>   a shared near tip; and the deterministic 1-in-1,000 sample over record indices (E1-F3)".
> - L1 line 475 reads: "C7 on its scope (E1-F3), per record;".

**D5. E1-F6.** Keep 58. Add after "**The added counts.**":
> **Count convention** (the owner: "explicit count definitions and a reconciliation table"). For a
> record predicate D on ℛ:
> - n(D) = #{R ∈ ℛ : D(R)};
> - n(D, c, v) = #{R ∈ ℛ : D(R) ∧ s_c(R) = v}, with s_c the survivor status under c (L1 §3, L3′).
>
> The eight degeneracies of C8's list are reported as n(D, c, True) and n(D, c, False), with n(D)
> implied. For D = nontrivial stabilizer and D = masking-equivalent, the list reports n(D) (frozen)
> and n(D, A, True), n(D, G, True) (added). n(D, c, False) = n(D) − n(D, c, True) is determined.
> Every list carries rank 3 per degeneracy, so 58 is complete and the four non-survivor cells
> would be redundant.
>
> | list | for D ∈ {6, 9} | rank per D | redundant listed |
> | --- | --- | --- | --- |
> | r5 (54) | n(D) | 1 | 0 |
> | E1 (58) | n(D), n(D, A, T), n(D, G, T) | 3 | 0 |
> | 62 (not adopted) | n(D) and four cells | 3 | 2 |
>
> Masking equivalence is defined relative to ℛ (some R′ ≠ R in ℛ has an equal context); the other
> nine degeneracies are intrinsic to R.

**D6. §10 table.** Add one row per new invariant:

| invariant | checkpoint |
| --- | --- |
| Lemma G-D | the toy whole-class check; the per-record check of sets 3–4 |
| set 2 is closure-free under G | F1 self-test and the computed-closure mutant |
| per-record C7 detects member-only faults | F2 self-test |
| σ is diagnostic and never overrides the run label | Layer-2 label self-test: σ = OK with another failing check gives that check's label |
| L_A and L_G reference recomputation | case 2 (d) self-test with a perturbed production count |
| rule T's statement scope | `result.json` `rule_T.statement_scope` |
| record-index sampling | sampling self-test |
| coverage reporting, raw and orbit-level | shard and `result.json` fields |

## E. Does the C7 investigation reveal a new structural property of the G convention?

**Answer: no NEW property in the §A.31 sense.** It does yield one proved structural lemma, which is
ELABORATING, and one observation, which is toy-only.

**Proved** (from r5's definitions and PO7; §A1):
- **Lemma G-D.** Under G, every record's closure is In(R) ⊔ W(Out(R)). The frame, consisting of
  the fixed quantities, the port samples and every in-frame record sample, neither masks nor
  supports any seed quantity. It is transparent to the elimination dynamics.
- **G-survival is internal to Out(R).** A G-survivor's tips are covered only by other seed
  quantities. In particular Φ, V and p play no part in G-survival; they enter only through the
  frame.
- **Retained in-frame ties are inert.** They are geometric coincidences: aligned sites whose
  distance equals their depth difference. They affect no survivor, no linkage, no rule-T input and
  no label. Under A there is no analogue, since every retained non-fixed quantity is already a
  survivor.

**Why this is not NEW.** Each part is a short consequence of statements Layer 1 already contains:
- PO7 (in-frame cones lie inside the frame);
- the frame's definition as the union of the fixed and port cones;
- the "truncated record" (§3: the retained in-frame record samples);
- P_G and P_G-dir, which already exclude any Φ clause under G.

It is the light-cone structure of the initial pair stated as a decomposition. That is useful
(cost, the closure-free definition of set 2, and the self-masking fault it exposes), but it is not
a new fact about the dynamics.

**Observed on toy instances only** (no claim about v8):
- 595 of 1,400 records, in 283 orbits, have retained in-frame ties under G.
- None of those ties is eligible.
- The toy class has no survivors at all.

The frequency reflects the toy geometry: region ball(1) inside a frame of radius 4, and port
(0, 0, −2). v8's frequency of F_G is unknown. It can be computed without closures in the dry run;
I did not compute it.

**Skeptical check of the favourable-looking part.** The decomposition could have been an artifact
of the toy frame, which contains the whole region. The proof does not use the region's size; it
uses only PO7 and the frame's definition. The toy check (1,400 of 1,400 records, both rules)
confirms the implementation, not the generality. What remains open is only the v8 frequency of
F_G, not the lemma.

## Owner decisions remaining

1. **Lemma G-D in the reference** (cost). The options are to allow the G-D form of the reference
   computation as a proved, checked optimization (recommended), or to require the full `s0ref`
   form on every set-2 record. The latter's cost depends on |F_G| for v8, which the dry run can
   compute without any closure. Decide after seeing it, together with κ.
2. **κ and S7:** still open, as the owner directed. The C7 term now includes per-record production
   closures on set 2, and the dry run must report it before any launch decision.
3. **No further decision is needed on counts.** 58 is complete.
