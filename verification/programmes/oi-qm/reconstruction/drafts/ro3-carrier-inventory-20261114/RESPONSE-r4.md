# RO-3: response to the independent review of inventory r4

**UNREVIEWED.** This file gives the writer's disposition of each finding F1–F17 of the independent
review of r4 (`REVIEW-r4.md`, ACCEPT WITH CHANGES, at PR head
`78089e5e7540f116f69933efca898a8b86d5f36d`; SHA-256 of the review as delivered
`f06d9f16b0ba3e5bdb928166d4a9b57278810aeb78b35726eecaf7c2a7d14e20`). r4 is left unchanged. The
changes are in `RO3-INVENTORY-r5.md`. Each finding was checked at `main`
`7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac` with `git show 7ac74a4b:<path>`, and the governance
comments were read through the GitHub API, before it was applied. Paper-only: nothing was built or
run, and no repository, Issue or PR was written.

Authorization: #1169 comment 6893687398 (`amaybaum`, 2026-11-15), the #1303 row: "Write inventory
r5, applying the 17 findings of the independent inventory review (ACCEPT WITH CHANGES), followed by
an independent review. No #1055 recovery target is chosen before then."

Dispositions:
- **accepted**: applied as the review proposes;
- **accepted, modified**: applied with a stated difference;
- **noted**: no change needed.

Section numbers below refer to r5.

## 1. Labels

### F1. 1.7 F: "refuted within" rests on an imported half

**Disposition: accepted.**
- **Checked.** Main:558 proves the factorization half and imports the unbounded nonnegative rank
  from [55]; Main:600 item (3) says "the unbounded-dimension half imported [55]"; the reference is
  Main:901. r4's own label required "a result on `main`".
- **Applied.** 1.7 F now reads "refuted within one fixed finite realization ..., conditional on the
  imported unboundedness theorem [55] (external, cited input ...)". The "refuted within" label now
  says that a cell resting in part on an imported theorem names it. 2.1 and AM-9 carry the same
  condition.

### F2. 2.7: a sufficient condition stated as a necessary one

**Disposition: accepted.**
- **Checked.** r4:440–441. The source of the wording is the #1055 body's test-case line: "infinite
  measure-preserving systems, where Poincaré recurrence needs a finite invariant measure and fails
  without one". Conservative infinite-measure systems recur. This is addendum nit n4.
- **Applied.** 2.7 uses the addendum's wording, "is not available without a finite invariant measure
  or conservativity", and attributes the original sentence to the #1055 body. Q9 notes it for the
  owner. The Issue body is not edited.

### F3. 2.6: Main:155 attached to 1.1 and 1.2

**Disposition: accepted.**
- **Checked.** Main:155 concerns near-total common visible return of rooted laws for continuous-time
  flows; it says nothing about microscopic return. This is addendum nit n3.
- **Applied.** 2.6 now splits the item. Main:155 is attached to 1.2 only. The non-inheritance of 1.1
  stands without it, and the OBL class refutation of 1.1 is cited separately.

### F4. SM:296 and SM:1606 hypotheses

**Disposition: accepted.**
- **Checked.** SM:296: "Let q=p be prime with p∤L, let L≥2, let A be any translation-invariant
  coupling over F_p". SM:1602–1606: the ring with phase space `(Z/q)^{2L}`, `A` the circulant
  adjacency matrix (unit coefficients), "For q prime with gcd(L, q) = 1 — q = 2 included:
  ord(F mod q) = qL".
- **Applied.** 1.1 G-fam states `L ≥ 2`, "any translation-invariant coupling over `F_p`" for SM:296,
  and "the unit-coefficient circulant adjacency" for SM:1606.

### Review §1, 1.4: the forward direction cited through a docstring

**Disposition: accepted.** Not numbered as a finding, applied with F1–F4.
- **Checked.** `pper_of_finiteRootedRealizable` is at `RootedClassification.lean:339`;
  `pper_has_responseRealization` is at `RootedClassificationAllTime.lean:162`.
- **Applied.** 1.4 F names both directions with their witnesses (§A.34). The I-classes cell cites the
  theorem and quotes the docstring at AllTime:182 as the docstring.

## 2. Use of OBL-RO3-2

### F5. Stale passages on OBL-RO3-2

**Disposition: accepted.**
- **Checked.** #914 comment 6883931412 item 2 and #1055 comment 6883932722 record the acceptance of
  the direct proofs "in place of the Halmos/Rokhlin primary-source check that was not completed".
  OBL Step 4 (lines 145–158) proves the two implications from S1–S3, and the correction note (lines
  205–207) says that (R) is not needed.
- **Applied.** §3 is rewritten:
  - OBL-RO3-2 is recorded as accepted at its scope, with the owner's words;
  - the route through Halmos and Rokhlin is removed, and Step 4 is cited;
  - the primary-source check is recorded as not completed and replaced by owner decision;
  - the first branch of r4's decision rule is quoted and recorded as fired.

### F6. Cells to move, at the OBL class only

**Disposition: accepted, modified.** Applied at the class the review names: this rule, prime `p`,
`α ≠ 0`, uniform Haar `μ`. The class is added as a row of the §0 table, the "OBL class", so that
every moved cell names it. Differences from the review's text:
- **1.1 I-qloc.** The review says `heisQ^n ≠ id` "follows by hand". It is not in OBL. r5 records it as
  [IR], a reading of the review checked by the writer on paper: on diagonal stage elements
  `heisQ^n` acts as `f ↦ f ∘ F^n` through 2.5 (ii-b), and cylinder functions separate points. The
  cell's status rests on OBL 3.2 for the configuration map only.
- **1.1 I-meas.** The row states both facts, as asked: `φ^L = id` refuted within the class, and
  Poincaré recurrence `μ`-almost everywhere. It adds the addendum's point that neither is exact
  common visible return.
- **1.2.** Refuted within the class in the cell-conditioned convention for every readout with at
  least two positive cells, with `V` restricted to its positive cells (addendum nit n2). In Main's
  root-shared convention it covers restriction readouts only (OBL lines 221–228). For I-qloc the
  cell names (ii-a) and (ii-b) as the bridge.
- **1.3.** Recurrence route unavailable; P-indivisibility itself open. Added from OBL 3.3: near-total
  common return excluded at late times and open at bounded times.
- **2.3 G-fact.** The [IR] conditional is replaced by OBL 3.4, with its one-line argument.
- **2.5.** (i), (ii-a), (ii-b) carry the support-off-`main` label; (ii-c) and (iii) stay open; the
  first missing step is (ii-c), and separately (iii).
- **Q6** is updated.
- **§3 secondary candidates.** r4's "[IR] `φ^L ≠ id` for the linear rule" is dropped as a candidate,
  since OBL 3.2 now covers it. The others are kept, unchosen (F5 and the r5 authorization).
- **Also moved, as consequences of the same proof and not as new cells.** The context paragraph after
  1.2, which r4 marked as on no record, now cites OBL 3.1 for the OBL class and stays [IR] in
  general. The null-measure remarks in §0 and 2.3 cite OBL §4.1.
- **Not moved.** 1.4 and 1.5 are unchanged. The review proposes no move there, and §7 of OBL proposes
  none.

### F7. Evidence layer of the moved cells

**Disposition: accepted.** Option 1: cite OBL-RO3-2 r2 at its exact SHA as support off `main`.
- **Checked.** `OBL-RO3-2-r2.md` is blob `b1edb95f9ed0f331c06f5ecbc69a806dc6631562`, added at
  `ef8d353e4c05e6e4de2f813478bc279f3fa00eb4` and unchanged at head `78089e5e`. It is not on `main`.
- **Applied.**
  - A label, "established for that rule and measure, support off `main` (PR #1303)", with the
    matching "refuted within the OBL class, support off `main` (PR #1303)". Its definition cites
    §A.42 item 8 and §A.46 item 1 and confines both labels to the OBL class.
  - Every moved cell uses it. No moved cell is recorded as established on `main`.
  - §6 classifies the reference as support off `main`, a gap, and states what would shut the gap.
- Landing OBL-RO3-2 r2 first is outside this authorization.

## 3. The map of A1-dependent results

### F8. Consumers listed at Main:60 with no row

**Disposition: accepted.** r5 §7 adds a corpus-wide map. Rows AM-1 to AM-10 take Main:60's list in
order, and AM-11 to AM-19 cover the companions, the book, Lean and the records. Each row gives where
A1 enters, what survives without A1 and the status at proved scope.
- **(a) Bijectivity: AM-3, AM-15.**
  - Checked: Main:60, "On a finite set, injectivity implies surjectivity"; Meth:158, :166, :253,
    :261; `injective_imp_bijective` (`CanonicalMeasure.lean:63`, `[Fintype S]` at :54).
  - §0 now says that every infinite class takes bijectivity as a hypothesis.
- **(b) Lemma 3 and the uniform prior: AM-4.**
  - Checked: `orbit_invariant_unique` (:178) and `counting_maximal_entropy` (:227) under
    `[Fintype S]`; DEPENDENCY-AUDIT.md:291.
  - At this base Lemma 3 is Main:54, with its Remarks at :56 (the continuum analogue) and :58 (the
    measure as a realization datum). The review's Main:56 is the continuum-analogue remark. r5 cites
    :54 and :58.
- **(c) The §3.2 setup: AM-5, with CP-indivisibility as AM-2.**
  - AM-2 gives CP-indivisibility a per-class row, and 1.3 points to it.
  - Checked: Main:266, :268–270, :280–288, :326–332; `permMatrix_mem_unitaryGroup`
    (`EquivalenceChain.lean:179`) and `isDiag_Phi` (:253) under `[Fintype V]` and `[Fintype H]`.
  - The Born-form theorem has no kernel pointer at Main:288; r5 labels it P.
- **(d) Corner occupancy: AM-6.** Checked: Main:216. No book mirror was found; there is no hit for
  "Doukas" in `book/`.
- **(e) The causal cone: AM-7.** Checked at source, with a result the review did not state.
  - The kernel proves the cone for an arbitrary site type: `iterate_dependsOnlyOn_ball`
    (`RegionTower.lean:283`) and `readout_unaffected_outside_ball` (:304). There is no finiteness of
    the site set (section variables at :246).
  - The kernel assumes the `CouplingGraph` hypothesis (:254): finite neighbourhoods on which each
    site's next value depends. Main:362 derives that hypothesis from one-step insensitivity using
    finite `V`.
  - So the cone survives without A1 under a stated hypothesis that the finite-range rules satisfy
    by definition. GR:132–134 states the same for an infinite deep sector.
  - The Bell ceiling's infinite form is recorded as [IR].
- **(f) §4.6: AM-8.** Added as [IR] context: Main:758 (ii)'s reason for placing the gap in the
  coarse-grained channel ("the exact Koopman operator of a finite permutation ... cannot mix") is
  specific to finite permutations, because on the OBL class the Koopman operator mixes. No cell
  moves.
- **Also cited.** Main:486 and Main:718 are in AM-9 and AM-10.

### F9. Companions and records

**Disposition: accepted.**
- **Theorem 23: AM-11.** Checked: Sub:123 lists A1 among the inputs; Sub:125 makes "S finite" an
  output; Sub:110 lists the §3.2 forward dilation; Sub:189 is Lemma 23.0; DEPENDENCY-AUDIT.md:287.
  Which stages beyond Stage 1 consume A1 is marked not traced.
- **Theorem 24 beyond (iii): AM-12.** (i) uses the uniform prior `1/|C_H|`. (ii) is under the
  alphabet-size hypothesis, and its use of A1 is not traced. (iv) is not a consumer. Structure's
  Proposition 9.5 (Struct:646) is added.
- **Computation:118: AM-13.**
- **The audit's proof-dependency matrix: AM-18.** It covers rows :281–291 and notes control 3 of row
  :285, which r4 did not cite.
- **Structure's A1–A6 comparisons** are listed in §7.2 as classifications, not consumers, as the
  review says. `book/ch09-universality.md:194` is added there.
- **Added by the writer.**
  - `book/ch18-beyond.md:168` (AM-17).
  - SM's counting-measure results SM:252, :334 and :641 (AM-4, AM-16).
  - `waveSubstratum_A1` (`SubstratumInterfaceAudit.lean:185`, census 15) (AM-16).
  - GR:669, under which A1 is sufficient for S3 and not a premise of (U1)–(U3) (§7.2).

### F10. Scope statement; Q9's framing

**Disposition: accepted.**
- **Checked.** Main:724 posit (ii): "consumed here by the recurrence step of §2.3 and by §4.6 ... the
  remaining uses of the posit being listed in the status Remark of §1.2". The #1055 body: "Main
  names exactly two consumers of A1", with §4.6 at "Main:760". At this base §4.6's scope is Main:758.
- **Applied.**
  - Standing states that §1–§6 cover the Q5 family and §7 maps A1's consumers.
  - Q9 is rewritten. It no longer repeats "second consumer"; it records the two Main sites, the
    narrower #1055 wording and the line drift, and asks the owner whether #1055's list is to be read
    as §7's map.

### F11. The "main equivalence" reading in #1169 comment 6893456888

**Disposition: accepted. Recorded as a finding, not settled.**
- **Checked.** The comment cites "the per-horizon equivalence's finite hidden configuration space
  (Main.md:111, :266)" and says "the main equivalence stays conditional on that posit".
  - Main:111 is the §2.3 setup and Main:266 the §3.2 setup.
  - Main:546 states the §3.4 equivalence, and Main:60 says it uses only Lemma 1.
  - Main:716 names two routes to the transition-statistics layer.
- **Applied.** §7.3 sets out the comment, the source and what does consume A1 at the cited lines. It
  asks the owner which of the two readings the decision text means. 1.6 points to §7.3. The source
  governs (§A.45 rule 1), and r5 follows Main:60 without settling the owner's question.

## 4. Stale cross-references

### F12. Gate A answers 3 and 4, Q10, D-CQ

**Disposition: accepted.**
- **Checked.** Q10 is decided (#914 comment 6883249235); r4:590–592 quotes the adoption. r4:337–338
  still called Q10 an owner question.
- **The D-CQ record.** D-CQ is #1169 comment 6891338304 (`amaybaum`, 2026-11-15T07:54:33Z), the C/Q
  target decision, read first-hand. #914 comment 6893722503 §3 cites it under that label. It states
  that it "amends the soundness requirement in the Gate A answers (c.6876591512). Soundness is now
  an open question, subject to the agreement-with-data requirement." It also says that C "is
  defined independently, by the limits of embedded observation" and that "Excluding PR is no
  longer a goal."
- **Applied.**
  - 2.3 quotes the Q10 decision in place of the stale cross-reference. It notes that D-CQ leaves the
    decision unchanged: the decision concerns coverage, which stays required. Under D-CQ's
    definition of C, whether sector confinement is a limit of embedded observation is part of S-J.
  - Standing quotes D-CQ by comment id. Answer 4 is quoted in full as adopted and then read as
    amended in its soundness sentence. That reading is marked [IR], because D-CQ does not number
    the answers it amends. Answer 3 is recorded as unaffected.
  - Q10 notes the amendment. Q13 asks the owner to confirm the reading and whether answer 4's
    access-closure clause survives.
  - §5 and §6 cite the decision and the #914 record.
  - **Also corrected.** r4 quoted answer 4 without its last sentence ("Access closure must prevent a
    model from qualifying through selected quantum experiments while also permitting
    stronger-than-quantum experiments.") and did not mark the omission. r5 quotes it in full.
- **What changed after the first draft of r5.** The first draft said that no D-CQ record was found.
  Its search matched the string "D-CQ". That string does not occur in the decision, so the search
  found only #1169 comment 6893687398. The coordinator identified c.6891338304. The draft's "not
  found" statements in Standing, Q13, §5 and §6 are replaced as above, and the reference to answer
  4 is updated.

### F13. Q2 and RO-1

**Disposition: accepted.**
- **Checked.** #1169 comment 6883250792 (`amaybaum`, 2026-11-14T19:48:20Z): "RO-1 owns sector-C
  membership, physical confinement grounds (S-J), closure under permitted operations and
  compositions (S-A), and non-circularity."
- **Applied.** Q2 now records the assignment, quoted verbatim, and leaves admissibility of sector
  confinement to RO-1 and S-J. 2.3 cites the split.

### F14. Ledger references

**Disposition: accepted.**
- **Checked.**
  - `LEDGER-r8.md` on `main` is blob `d6ceba53…`, the same blob as at `9ff3b8d9`.
  - `LEDGER-r9.md` is on `main`, blob `7c69662a…`, retained through #1304 (#1169 comment
    6891337868).
  - A diff of r8 and r9 restricted to rows quoting the cited identifiers finds four added rows and
    no changed cited row. One uncited row (A-QM) changes a count.
- **Applied.** Standing and §6 are updated.
  - The identifiers are provenance.
  - The one attributed reading (§8.5) is support on `main` for the statement that the ledger makes
    it.
  - The branch copy at `9ff3b8d9` is provenance.

### F15. Status lines

**Disposition: accepted.**
- **Applied.**
  - The header states r4's review status: confirmed against r3 in `REVIEW-OBL-r2.md`, with the
    addendum, and reviewed as an inventory in `REVIEW-r4.md`.
  - 2.3 reads "so this inventory does not recommend it".
  - The base is `7ac74a4b`. Standing records the files that changed since `dfeec843`, none of them
    cited by r4.

## 5. The ChatGPT nits

### F16. `patch_glob`

**Disposition: accepted, modified.**
- **Checked.** `patch_glob` (`QuasilocalAlgebra.lean:136`) states `patch Λ s (glob Λ s) = s`.
- **Applied, as text, in the restatement of (ii-b) in r5 2.5.** The review's R5 places it in an
  OBL-RO3-2 r3. That revision is outside this authorization, so `OBL-RO3-2-r2.md` is unchanged.

### F17. The diagonal identification in `heisQ`

**Disposition: accepted, modified.** As F16: applied as text in r5 2.5 (ii-b), step 3. The
calculation was checked by reading the definitions; nothing was run.
- `target Φ Λ s f = glob (hat Φ Λ) (φ^{-1} (patch Λ (φ s) f))` (:1054).
- At `f₀ = glob Λ (φ s)`, `patch_glob` gives `patch Λ (φ s) f₀ = φ s`. So the target is
  `glob (hat Φ Λ) s`, which is `h` for `s = ext (hat Φ Λ) h` by `glob_ext` (:1071).
- `transported` (:1109), `heis_emb` (:1127), `glob_map_of_glob_eq` (:1074) and `heisQ_stage`
  (:1274) are as the review cites them. The review's ":1073" for `glob_map_of_glob_eq` is its
  docstring line; the theorem is at :1074.

## Not applied

- **The review's §6 recommendation of a first recovery target.** It is listed among the r5
  candidates, with the review's second candidate, and neither is chosen. #1169 comment 6893687398:
  "No #1055 recovery target is chosen before then."
- **An OBL-RO3-2 r3.** It is not written (F16, F17).

## Off-`main` references in this response

These are the same as in r5 §6. The review of r4 and this response are review records and support no
claim. The moved cells' support, `OBL-RO3-2-r2.md`, is off `main` and labelled so in r5.
