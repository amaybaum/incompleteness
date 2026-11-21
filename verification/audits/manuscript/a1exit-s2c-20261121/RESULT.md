# A1-EXIT Step 2, unit S2-C — R1/R2 scoping and criterion-3 qualifications: result

**Status.** Writer's result, WIP / UNVERIFIED. Independent non-author review is required; merge is a
separate owner decision. Bands unchanged (consistency work, §A.23).

**Authorization and goal link.** As in `PREREG.md` (owner `amaybaum`, #1169 comment 7056875845,
2026-11-21T03:51:25Z; goal: the A1-exit objective, #1169).

**Commits.** PREREG `e9ebf3ab8`; edits, rebuilt artifacts and coverage ledger `5cf892c69`; RESULT
`05d2ab4f3`. After review round 1 (§8): amendment A1 `0d17087b2`, then its edits and this revision of
the record. Base `main` at `1c7eedc4`. No edit adds or removes a line, so every site keeps its base line
number on this branch.

## 1. Edits as applied

All 27 splices of `PREREG.md` §5 were applied verbatim, with no deviation. After applying, each new string
occurs exactly once in its file and each replaced old string is gone.

| ID | Site (line on this branch) | Ledger row | Kind |
|---|---|---|---|
| C1 | `papers/Main.md:131` | X-20 | return form, introduction |
| C2 | `papers/Main.md:141` | X-23 (X-20) | return form |
| C3 | `papers/Main.md:180` | X-20 | return form |
| C4 | `papers/Main.md:224` | X-20, X-23 | "assumed as hypotheses and not adopted" and the return form |
| C5 | `papers/Main.md:724` | X-20 | return form |
| C6 | `papers/Main.md:280` | X-15 | law form, (IP) |
| C7 | `papers/Main.md:766` | X-60, X-61 | law form, (IL) |
| C8 | `papers/Main.md:159` | X-20 (sitemap) | finite-representative scope |
| C9 | `papers/Main.md:732`, clause (iv) only | X-12 | "on a finite representative" |
| C10 | `papers/SM.md:122` | X-41 | "assumed … not adopted" and the law form, H-μ(φ,Θ) |
| C11 | `papers/SM.md:252` | X-41 | the same, at the selected invariant measure, on ℤ^d |
| C12 | `papers/SM.md:334` | X-17 | the same, H-μ(sp) |
| C13 | `papers/SM.md:44` | X-20 (Phase 2 S1) | return form |
| C14 | `papers/GR.md:138` | X-20 (Phase 2 G1) | return form |
| C15 | `papers/GR.md:589` | X-20 (Phase 2 G2) | return form |
| C16 | `papers/Substratum.md:92` | X-20 (Phase 2 B1) | return form |
| C17 | `papers/Structure.md:1224` | X-20 (review B1) | finite-representative scope |
| C18 | `book/ch01-observation.md:121` = FULL:454 | X-20 (mirror of M:131) | return form |
| C19 | `book/ch01-observation.md:161` = FULL:494 | X-20 (review B1) | finite-representative scope |
| C20 | `book/ch01-observation.md:179` = FULL:512 | X-20 | "assumed … not adopted" and the return form |
| C21 | `book/appendix-c-objections.md:104` = FULL:6259 | X-20 | return form |
| C22 | `book/appendix-b-derivations.md:46` = FULL:5723 | X-15 (mirror of M:280) | law form, (IP) |

**Not edited, as decided in PREREG §2.**

| Item | Outcome | Reason |
|---|---|---|
| X-25 (M:147) | option (a), F as printed | LEDGER §12 N1. The finite scope is visible at the site through "instances of the overlap-and-return theorem" (finite sets, a bijection; M:145) and "$(\Gamma_t)$ is periodic" |
| X-50 | handled by S2-B | S2-B (#1473) prints the X-50 wording at its Main:336 (its E2); confirmed from the PR body and diff |
| X-13 | no site | criterion 3 met (LEDGER §3.1) |
| M:356 | no edit | it states the role of P-indivisibility, not that it holds |
| Cx:474, ch15:113 = FULL:3990 | no edit | each sentence opens "On a fixed finite reversible representative" |
| R1 (X-11) | check found nothing | No site in Main, SM, GR, Substratum or the book states a selected law on an infinite carrier unconditionally. Main's (iv) keeps "a standard but substantive epistemic postulate, not derived". M:58 calls the counting measure "the default, not a constraint on representations". Each A1-free result names its law hypothesis: ρ is any root-shared probability (M:131), (IP) (M:280), (IL) (M:766), H-μ(φ,Θ) and H-μ(sp) (SM:122, :252, :334). With (iv) scoped to a finite representative (X-12), R1 is named through these per-result law hypotheses: no result uses a selected law on an infinite carrier without naming its law condition as assumed and not adopted |
| C1 (X-71) | check found nothing | GR:58 is stated "Under A1" for a finite total system with the boundary interaction negligible at the shell scale. No text in `papers/` or `book/` claims a normalized invariant shell law for coupled bijections |

## 2. Wording for S2-E (exact final text)

**Return form, at a site that introduces (NR) or opens a sentence with it (Main):**

> (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected
> update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to
> satisfy it.

**Return form, as a parenthesis after "assumed … not adopted" at a restatement (Main):**

> (it concerns a time that need not be accessible and then has no finite-window test; for the selected
> update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to
> satisfy it)

- In the companions write "of [Main §3.2]".
- In the book write "of Main §3.2". The book's restatements, which say "the near-return condition of
  Chapter 1 §1.5", take the parenthesis form (appC:104; ch01:179 after amendment A1).
- Where "assumed … not adopted" is missing, it is added as ", assumed as a hypothesis and not adopted,"
  (ch01:179), or, for several conditions, "assumed as hypotheses and not adopted" (M:224).

**Law form** (sentence after the statement of the condition, with X its label):

> X is a condition on a law on the whole carrier; finite-window data can test some of its consequences
> but cannot establish it, and do not distinguish it from a finite carrier's counting law.

Inside a clause (SM:122, :252) the same text stands in parentheses after "assumed as a hypothesis and not
adopted". For an extension with several clauses (SM:334) it reads "assumed as a hypothesis of this
extension and not adopted; the measure clause is a condition on a law … counting law".

At SM:252 the lemma opens "Let $\mu$ be the invariant measure — the selected counting measure of [Main]
Lemma 3, or a stated structured prior, or, on $\mathbb{Z}^d$, a law …", so that the assumed law is not
called "selected" (amendment A1-2).

**Finite-only scope** of a recurrence-cycle statement: "on a finite representative" (C8, C17, C19).

## 3. Propagation (§A.25, §A.14)

Re-grep on this branch:

- **Return form** ("has no finite-window test"): 15 occurrences.
  - Main 5 (:131, :141, :180, :224, :724).
  - SM 1 (:44), GR 2 (:138, :589), Substratum 1 (:92).
  - ch01 2 (:121, :179), appC 1 (:104), FULL 3 (:454, :512, :6259).
- **Law form** ("do not distinguish it from a finite carrier's counting law"): 7 occurrences.
  - Main 2 (:280, :766), SM 3 (:122, :252, :334).
  - appB 1 (:46), FULL 1 (:5723).
- **Lines with "(NR)" or "near-return" and no return form.** Four remain:
  - M:60 and M:732 item (ii), which are S2-B sites;
  - ch01:284 = FULL:617, the NR-1 citation, a negative result that uses no (NR) hypothesis.

  Meth, ch18 and glossary:105 carry their own wording and are S2-E's Q3 sites.
- **Book mirrors.** ch01:121/161/179, appC:104 and appB:46 are byte-identical to FULL:454/494/512/6259/5723.
- **No book mirror** for the edited M:141, :180, :224, :724, :766, :159 and :732 (iv), SM:122, :252,
  :334, or Str:1224. The distinctive-phrase grep at the base found one occurrence of each.
- **Not edited.** M:224's mention of (IP) is a pointer to §3.2's remark, which carries both parts, and
  LEDGER §3.1 does not list it.

## 4. Build, coverage and checks

- `sh ./build.sh Main SM GR Substratum Structure` and `sh ./build.sh --book`: build OK, no dropped glyphs.

  | Artifact | Pages (base → branch) | Median characters per page (base → branch) |
  |---|---|---|
  | Main | 106 → 107 | 3338 → 3317 |
  | SM | 148 → 148 | 3153 → 3144 |
  | GR | 84 → 84 | 3178 → 3185 |
  | Substratum | 53 → 54 | 3240 → 3190 |
  | Structure | 94 → 94 | 2908 → 2914 |
  | book | 489 → 489 | 2998 → 2997 |

- `python3 tools/coverage_check.py`: OK (132 canonical statements) after three re-affirmations in
  `verification/coverage/LEDGER.json`:
  - the area-law lemma, `SM:L-unnamed-ff7b7d06` → `SM:L-unnamed-675607a6` (its id is derived from its
    fingerprint), fingerprint `675607a6c305eeb8`;
  - Lemma 1c, fingerprint `242ff16786e66342` (after amendment A1-2), with its assumptions field naming the H-μ(φ,Θ) law on
    ℤ^d;
  - Proposition 4b, fingerprint `e7cb872ef111a22a`.

  Levels and deltas are unchanged.
- `tools/lean_manuscript_census.py` OK; `tools/artifact_placement_check.py` OK.
- `tools/legacy_records_check.py`: the self-test passed. The check itself was undecidable because the
  local clone is shallow, so it is left to CI.
- Register scan of the added text (§A.32, §A.33): no revision-history words, no reader instructions, no
  capitals for emphasis.
- `ledger_check.py check` (for information; the ledger is reconciled after Step 2): PIN MISMATCH, as
  expected. The rebuilt map has one site that the committed map lacks, `papers/SM.md:122`. The law form's
  phrase "a finite carrier's counting law" matches the extended criterion-5 scan there. The other
  sites where the law form was added were already mapped. The reconciliation maps SM:122 to X-41.

## 5. Overlaps with parallel units (for landing)

- **M:732.** S2-B (#1473) edits item (ii) of the same line; this unit edits clause (iv) only (C9). A
  line conflict is expected and is resolved by keeping both.
- **Sub:92.** S2-B rewrites this line but keeps its (NR) sentence. When it lands, C16's appended
  sentence goes after S2-B's text.
- **M:766.** S2-D edits Main §4.6. This unit appends one sentence after the statement of (IL).
- **appB.** S2-B edits appB:92 = FULL:5769; this unit edits appB:46 = FULL:5723.
- **Main line numbers.** S2-B shifts the Main lines after 334 by +4.
- **Wording difference with S2-B.**
  - S2-B's X-50 sentence at its Main:336 reads "for the selected update on $\mathbb{Z}^d$" without
    "of §3.2".
  - Its appB Theorem B.2.5 carries only the first clause of the return form.

  Harmonizing these is for the coordinator. The pointer "of §3.2" is needed for accuracy, not only for
  grammar: under NR-1 Prop. 5.1, a nilpotent coupling coefficient α makes the Bernoulli law satisfy (NR),
  so the sentence would be false for "the selected update on ℤ^d" without a pin. Main §3.2's instance
  (q = 2, α = 1) is covered by NR-1 Prop. 2.3, where (NR) fails under the Haar product law. The ledger's
  queued X-20 wordings carry the same unpinned phrase and the superseded "the only laws known …" clause;
  both are for the reconciliation.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| PR #1473 (S2-B) and its diff | "X-50 is handled by S2-B"; the overlap notes | provenance: no manuscript claim of this unit uses its content |
| #1169 comment 7056875845 | authorization | provenance (owner record, quoted) |

All support (the A1-EXIT ledger, O-A4, NR-1, Phase 2) is on `main` at the base.

## 7. Verification status (§A.46 item 4)

- **Verified by the writer.**
  - The splices match the preregistration byte for byte.
  - The builds, coverage and census pass.
  - The mirrors are identical.
- **Missing.** A delta review of the amendment A1 edits at this head.
- **Accountable Issue.** #1169. The regression audit is #1468.
- **What resolves it.** An accepting review on PR #1474, then the ledger reconciliation after Step 2,
  then a separate owner merge decision.

## 8. Review round 1 (`05d2ab4f`, ACCEPT-WITH-NITS)

The record is on #1474. As directed by the coordinator, this unit applied N1, N2, N3, N5 and N7 by
amendment A1 (`amendments/A1.md`, pushed before the edits), skipped N4, N6 and N8, and records N6 and N8
here.

- **N1 (applied, A1-1).** Every one of the 15 return-form sites reads "no law that is not supported on
  periodic configurations is known to satisfy it", and the superseded phrase has no occurrences. The
  sites are:
  - Main 5;
  - SM 1, GR 2, Substratum 1;
  - ch01 2, appC 1, FULL 3.

  The wording rests on NR-1 Prop. 2.3. No law satisfying the root-shared (NR) is on record.
- **N2 (applied).** The accuracy reason for "of §3.2" is in §5.
- **N3 (applied).** The naming of R1 is in §1, in the R1 row.
- **N4 (skipped).** M:224's "(IP)" stays a pointer to §3.2's remark.
- **N5 (applied, A1-2).** At SM:252, "the invariant measure — the selected counting measure …".
- **N6 (recorded for reconciliation).** SM:122 and SM:252 write H-$\mu(\varphi,\Theta)$, and Θ also
  denotes time reversal at SM:647. The reconciliation, or a later unit, may rename the reversal symbol
  in the hypothesis label.
- **N7 (applied, A1-3).** At ch01:179 = FULL:512 the return form is in parentheses, as at appC:104.
- **N8 (recorded for reconciliation).** SM:150 is a pointer to the area law. It is out of scope for
  this unit.

**After A1.**
- **Builds.** All builds pass with no dropped glyphs:

  | Artifact | Pages | Median characters per page |
  |---|---|---|
  | Main | 107 | 3317 |
  | SM | 148 | 3144 |
  | GR | 84 | 3185 |
  | Substratum | 54 | 3190 |
  | book | 489 | 2997 |

- **Coverage.** `coverage_check` reports OK after the Lemma 1c fingerprint was re-affirmed
  (`711478cf44840d32` → `242ff16786e66342`).
- **Mirrors.** ch01:121/179 and appC:104 are byte-identical to FULL:454/512/6259.

## 9. Catch-up with `main` at `a1f38284`

The merge brings in S2-A (#1470, `0cd5d5bf`), #1476 (`f1c8c6b1`) and S2-B (#1473, `a1f38284`).

- **Merge commit:** `3addf4acd`.
  - First parent: `cb6d1b87e`, this branch.
  - Second parent: `a1f38284`.
  - It was made with `git merge`; no rebase.

**Conflicts in `.md` files.**

- **Files.** Two files conflicted: `papers/Main.md` and `papers/Substratum.md`.
- **How they were resolved.**
  - Each was taken from `main`, which holds S2-A and S2-B.
  - This unit's final splices were then applied to it: PREREG §5 with amendment A1.
  - Each old string occurred once in `main`'s text except C4's. S2-B changed M:224's list connective from
    ", and the remark" to ", the remark", so C4's insertion was placed after "(NR)," in S2-B's text,
    unchanged in content.
- **Other conflicts.** The generated `.tex` and `.pdf` files also conflicted; they were rebuilt.
- **Line shifts.** S2-B adds four lines before Main:724, so M:724, :732 and :766 of this unit are now
  M:728, :736 and :770. No other site of this unit moved.

**S2-B's return-form sites.** Main:336 (X-50) and appB:92 = FULL:5769 read, character for character,
"concerns a time that need not be accessible and then has no finite-window test; for the selected update
of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it".
AppB and FULL write "of Main §3.2". This matches this unit's wording.

### 9.1 The resolved lines

#### M:224

S2-A/S2-B change (base `1c7eedc4` → `main` `a1f38284`), word diff:

  - delete: "and" → ""
  - replace: "(IP)" → "(IP), the measurable-carrier corollary of §3.2 and the two coupling-step theorems of §3.4 (the quantitative C2 theorem and the physical-memory theorem)"

S2-C change (`main` → this merge), word diff:

  - insert: "assumed as hypotheses and not adopted (the condition (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it),"

Resolved line `papers/Main.md:224`, in full:

> **Continuous spectra and the finite-substratum commitment.** Lemma 1 fixes the visible configuration space as finite, and the Barandes correspondence as applied here produces an emergent Hilbert space of finite dimension. Standard quantum mechanics makes heavy use of continuous-spectrum observables — position on $\mathbb{R}^3$, momentum, continuous-spectrum scattering — which strictly require infinite-dimensional Hilbert spaces and unbounded self-adjoint operators. The framework's position on this is that continuous spectra are the infrared limit of the discrete spectrum produced by Lemma 1, not a deeper reality that the framework fails to capture. The quantitative separation is extreme: for a visible sector bounded by the cosmological horizon, of radius $L_H$, and an assumed discreteness scale $\epsilon$ of the order of the Planck length $l_p$, the number of distinguishable positions is $|\mathcal{C}_V| \sim (L_H/\epsilon)^3 \sim 10^{183}$, and no independent continuous-spectrum prediction is needed or claimed. Calvo [13] extends the Barandes correspondence to countable-infinite dimensions for completeness, but the finite-dim correspondence is the load-bearing one for the framework — every result in §2–§3 other than the infinite-region completion (§3.2, §3.4), which is assembled from finite-region stages, runs on finite configuration spaces: Lemma 1 for the visible sector, with the total-finiteness posit (§1.2 Remark, §4.5) where a result also needs the hidden sector finite; the near-return corollary of §2.3, the index-free form of §2.3 under (FS) and (NR), assumed as hypotheses and not adopted (the condition (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it), the remark of §3.2 under the condition (IP), the measurable-carrier corollary of §3.2 and the two coupling-step theorems of §3.4 (the quantitative C2 theorem and the physical-memory theorem) take a measurable hidden space.

#### M:732 (now M:736)

S2-A/S2-B change (base `1c7eedc4` → `main` `a1f38284`), word diff:

  - replace: "§2.3," → "§2.3 and for the P-indivisibility input of the CP-indivisibility theorem of §3.2 on a measurable hidden carrier,"
  - replace: "capacity, the CP-indivisibility theorem of §3.2, the physical-memory theorem of §3.4" → "capacity"
  - delete: "finite" → ""
  - insert: "of any cardinality"
  - insert: "or law"
  - replace: "permutation," → "dynamics (a unitary or isometry, or a measurable map),"
  - delete: "finite" → ""

S2-C change (`main` → this merge), word diff:

  - insert: "on a finite representative"

Resolved line `papers/Main.md:736`, in full:

> **The posit ledger.** The two-axiom presentation of §1.2 names the foundation's primitives; the full argument consumes more inputs than two, and they are collected here so they are countable in one place. The list is complete in one specified sense: it is the audited inventory of the explicit premises that the derivations of this paper consume, including those it takes from the companion substratum construction, as these texts stand in the same revision of the repository. It does not enumerate every physical assumption one might make; the named hypotheses of the matter, gauge and gravity sectors are carried where they enter; and the empirical motivation recorded for an item does not make that item logically necessary. The framework's substantive posits, beyond Axiom 1 (tokened differentiation, indubitable), are: (i) Axiom 2 — recurrence — owned as a posit with a non-derivability countermodel; (ii) total finiteness of the bijective representative of the status Remark of §1.2 (an open hypothesis, not adopted), carried as one sufficient condition and not as a premise of the framework: each result that uses it names the hypotheses it consumes, and a weaker sufficient condition, where its sufficiency is proved, is stated with the result — the near-return condition (NR) for the P-indivisibility conclusion of §2.3 and for the P-indivisibility input of the CP-indivisibility theorem of §3.2 on a measurable hidden carrier, the invariant-product condition (IP) for the doubly stochastic marginal of §3.2 and the invariant-law condition (IL) for the decay estimate of §4.6, each assumed as a hypothesis of that result and not adopted, and reversibility (REV), item (iii), an alternative sufficient condition for bijectivity — while the counting-measure selection of Lemma 3, the exact return and its index $L$, the orbit capacity and the canonical-typicality step of §4.6 are statements about finite representatives — Lemma 1 delivers finiteness of the observer's distinguishable states from the finite-capacity clause of the Definition, and the extension to the whole representative is A1 of the companion substratum construction — there scoped as the gauge choice of the minimal finite representative, the cardinality of a deep sector being unobservable at the fixed visible/hidden interface when that sector is a factor of any cardinality prepared independently in a normalized state or law and evolved by its own dynamics (a unitary or isometry, or a measurable map), with product dynamics, which leaves every reduced visible channel, and hence every transition probability, unchanged (deep-sector enlargement, developed there) — consumed here by the recurrence step of §2.3 and by §4.6, whose conclusions hold on the finite representative; their transfer, where expressible through the transition probabilities, to every representative reached from it by relabelling the hidden states, by such a decoupled enlargement or, under the alphabet-size hypothesis that systems with the same coupling structure and dynamics class differing only in alphabet size have the same emergent transition probabilities, by a change of alphabet that keeps the coupling structure and dynamics class is stated and proved in the companion substratum construction, while the recurrence-scale conclusion of §2.3 is a statement about finite representatives, the remaining uses of the posit being listed in the status Remark of §1.2; (iii) the record-preservation and eventual-image arguments that ground injectivity (Lemma 3) close the hidden-sector margin on a finite representative (item (ii)) using one *empirical* input — the observed statistics, in the uniform-prior doubly stochastic scope — and one structural principle, the restriction of a finite map to its eventual image, which covers registered histories whose states lie in that image, so bijectivity is part-empirical rather than a pure lemma (a reader who declines the recovery may instead adopt reversibility (REV), $\varphi$ a bimeasurable bijection of a measurable carrier, as the standard information-conservation postulate of unitary quantum mechanics and classical Hamiltonian flow [42, 43], at no cost to the downstream results — see the remark following Lemma 3); (iv) the measure selection for constructed realizations (§1.2 Remark) is a maximal-entropy principle ("the maximal-entropy invariant measure compatible with the observer's records") on a finite representative — a standard but substantive epistemic postulate, not derived; (v) the hidden-sector mixing hypothesis (ETH-motivated) conditioning the slow-bath form of the C2-necessity direction, for a system class (emergent descriptions of linear-mod-$q$ automata) on which the standard ETH evidence base is silent, and whose exact linear rule conserves a quadratic invariant for every symmetric translation-invariant coupling and, at prime $q$ not dividing the lattice size, for $d\ge2$ splits its largest energy shell into exponentially many cycles [SM §4.2], so that numerical motivation comes from the rounded candidate of [SM §4.2], which behaves chaotically at the sizes measured, while whether the realized hidden sector satisfies the mixing hypothesis remains open — this is the same open dynamical question as the typicality selection in (iv), one conditional wearing two hats; (vi) spatial isotropy, entering as empirical input E4 of the reconstruction; (vii) linearity of the substratum update (A5), a further restriction beyond the affine condition. The affine step uses base-point-independent first differences, which telescope to a constant plus an additive map; and, for the spatial results — the causal cone and Bell ceiling of §3.3, the observer selection of §4.6 and the companion reconstruction — the spatial constitution, which the characterization theorem of §3.4 does not use: (viii) site factorization — the configuration space is identified with a product of local configuration spaces over a set of sites; given that identification the dynamics determines its coupling graph, the dynamics alone has not been shown to select the identification, and the coupling graph, its causal cone and the regions of §3.3 and §4.6 are read relative to it; (ix) bounded coupling degree (A3), as one degree bound across the family of finite representatives — at a single finite lattice the bound holds automatically, so the item has content only in family form, where it gives the cone of §3.3 bounded growth and is used by §4.6; (x) the nearest-neighbour range — on the reference vacuum/uniform state class the coupling graph $G_\varphi^{\rm ref}$ of §3.3 is the simple-cubic graph — on which the form of the wave rule, its dispersion and the six-link carrier of the companion construction rest, and which the cone of §3.3 does not require; (xi) center independence (A4), in two clauses: the update commutes with lattice translations up to gauge, and the update at a site contains no explicit copy of that site's present value; (xii) background independence (A6), covariance of the dynamics under site-dependent internal-index transformations with the link coupling transformed alongside, which in the form formalized imposes no restriction on the rule and fixes the interface through which the gauge symmetry is read locally; and, for the continuous path of $*$-automorphisms from the identity to the update in §3.2 and §3.4, (xiii) the second-order form of the update, a posit of the selected lattice model, not derived and not an axiom of OI: each site of (viii) carries a previous and a current value in a finite abelian group, and one step is $x(t+1) = F(x(t)) - x(t-1)$, in phase-space form $(x(t-1), x(t)) \mapsto (x(t), F(x(t)) - x(t-1))$, with each $F_i$ reading the current values at finitely many sites and each site read by finitely many $F_i$ (kernel: `ruleDynamics` in `OIBridge/SecondOrderDrive.lean`), the update displayed in §3.2 being its instance with $q = 2$ and $F$ the nearest-neighbour sum; and, for the Bell analysis of §3.3, (xiv) measurement independence, $p(\Omega\mid a,b)=p(\Omega)$ — the response-relevant pre-setting variable $\Omega$ is uncorrelated with the setting generators' outputs — a posit about the initial condition, not derived. Fourteen items, of unequal weight, and not fourteen independent physical assumptions: (viii) is foundational and (ix)–(xi) and (xiii) are stated relative to it; (x) implies the bound of (ix) for $G_\varphi^{\rm ref}$, and with (vii) for $G_\varphi$; the second clause of (xi) depends on the identification of (viii) as well as on the rule; (xii) restricts no rule; and (xiv) enters only the Bell analysis of §3.3. Part I of the companion methodology paper gives the complementary view: an eight-rung analysis of observational structure. The perspectival reading gives the proper-part locus. A successor map uses successive moments and a persisting locus, and preservation of registered distinctions implies injectivity on states with different registered content. The analysis takes per-moment finiteness of the visible configuration space from the finite-capacity clause of the Definition, and isolates recurrence (Axiom 2) as the one rung requiring a further axiom; the total finiteness of item (ii) and items (iv)–(xiv) lie outside the layer it treats. The two accounts describe one structure — the rung analysis counts what is *recovered*, this ledger counts what is *assumed* — and agree on the substance, including that the injectivity recovery closes its hidden-sector margin on a finite representative with an empirical input and that visible finiteness is stipulated per moment rather than derived. The two-axiom statement remains correct about what is *primitive*; this ledger states what is *assumed* or, for item (ii), hypothesized, and the framework's claims are conditional on the full list, item (ii) entering only as one of the sufficient conditions named at each use.

#### Sub:92

S2-A/S2-B change (base `1c7eedc4` → `main` `a1f38284`), word diff:

  - delete: "finite" → ""
  - insert: "of any cardinality"
  - replace: "interface. Infinite extensions require specified" → "interface, each in a"
  - replace: "measures" → "state"
  - replace: "states and well-defined" → "law with its own unitary, isometric or measurable"
  - replace: "the finite identity does" → "an unnormalizable factor is"
  - replace: "supply that construction." → "covered."

S2-C change (`main` → this merge), word diff:

  - insert: "(NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it."

Resolved line `papers/Substratum.md:92`, in full:

> (A1) **Finiteness.** The configuration space $S$ is finite. E3, read as a Hilbert-space dimension cutoff $\dim\mathcal H\le e^{A/4}$, bounds the observationally relevant visible sector and boundary layer $\mathcal C_V\times\mathcal C_B$ under the deep-sector influence bound H-BD of [GR §3.2]. This bound alone does not establish finiteness of every underlying sector. Theorem 24(iii) gives an exact freedom to adjoin independently prepared decoupled factors of any cardinality at a fixed interface, each in a normalized state or law with its own unitary, isometric or measurable dynamics; an unnormalizable factor is not covered. A deep sector coupled under H-BD changes the transition law by at most $2t/\tau_{BD}$ ([GR §3.2]), so its comparison is only at leading order on accessible timescales. A1 is an open hypothesis, not adopted ([Main §4.5], item (ii)), and one sufficient condition among those each result names: it remains the finite-carrier premise for the recurrence arguments, and for their P-indivisibility conclusion the near-return condition (NR) of [Main §2.3], assumed in its place and not adopted, is a weaker sufficient condition. (NR) concerns a time that need not be accessible and then has no finite-window test; for the selected update of [Main §3.2] on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it.

### 9.2 Union check

The scratch script `s2c-union.py` (recipe below) checks every tracked `.md` file in the merged tree:

- each file this unit edits equals `main`'s version plus this unit's final splices, each old string
  occurring exactly once;
- the same splices applied to base `1c7eedc4` reproduce this branch's pre-merge head `cb6d1b87e`
  exactly, so the splice list is this unit's whole change;
- every other `.md` file equals `main`'s version.

Since `main` is base plus S2-A, #1476 and S2-B, the merged tree is their union with this unit's change
and nothing more. Result: `union check: PASS`, all nine edited files OK.

The recipe is to replay `PREREG.md` §5 with amendment A1 on `git show a1f38284:<file>`, with C4's old
string read as ", the remark of §3.2", and compare with the merged file.

### 9.3 Rebuild and coverage

- **Builds.** `sh ./build.sh Main SM GR Substratum Structure` and `sh ./build.sh --book` succeeded with
  no dropped glyphs.

  | Artifact | Pages | Median characters per page |
  |---|---|---|
  | Main | 109 | 3326 |
  | SM | 149 | 3158 |
  | GR | 84 | 3185 |
  | Substratum | 54 | 3196 |
  | Structure | 94 | 2914 |
  | book | 490 | 2980 |

- **Coverage.** `coverage_check` reports OK (132 canonical statements) on the auto-merged
  `verification/coverage/LEDGER.json`. No fingerprint moved, so none was re-affirmed.

### 9.4 SC-42

The result file was regenerated under the owner's authorization (#1169 comment 7057674976), on the
conditions set for S2-D. From the repository root, with
`R=verification/audits/manuscript/bell-operational-reconciliation-20261029`:

    python3 -I -B $R/check_sc42_integration.py --verbose > $R/sc42-integration-result.json

| Check | Result |
|---|---|
| exit status, normal and `-O` | 0 and 0; verdict PASS; the two stdout outputs are byte-identical |
| `ok: false` entries | none |
| added-text scan | `added-text scan: 0 hit(s)` |
| `--self-test`, normal and `-O` | exit 0; output byte-identical to the committed `sc42-integration-controls.json`, which is unchanged |
| diff of the result file | +4 lines: one added `ok: true` entry, nothing removed or changed |

**The added entry** is "chapter line mirrored in FULL: The second route is the stochastic–quantum
correspondence of...". It comes from ch01:161 = FULL:494 (C19), a chapter line that this unit's edit
makes new relative to the checker's base `ca3a5bb2`.

**This unit's other book lines** (ch01:121 and :179, appC:104, appB:46) add no entry. Their first 60
characters already occur among the predicates, because those lines already differ from `ca3a5bb2`.

### 9.5 Register and duplicate checks

Words added against `main` in the nine edited sources were scanned for history words, reader
instructions and capitals for emphasis: 0 hits. No non-empty line in those files occurs more often than
it does on `main`.

### 9.6 Off-`main` references

None added. PR #1473 and the S2-B commit are on `main` (`a1f38284`).
