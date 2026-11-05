# BORN-SEL (b): recommended answers to the C-1 owner questions OQ-1 to OQ-15 (#1059)

**Status.** WIP / UNVERIFIED. Paper only. Recommendations only: **the owner decides every item**, and nothing here is a
decision, an adopted premise or a change to `PREREG-C1.md` r6, which is left as it stands at `cde5ecbc`. Not
independently reviewed.
- **Authorization.** #1059 c.6649420231 (owner, chat 2026-11-05): paper-only, part (b). Order of work set by the owner
  (relayed by the coordinator, 2026-11-05): "present #1059's OQ-1–OQ-15 recommendations for owner decisions before
  proceeding with the dependent measure analysis."
- **Writer.** `writer-born`.
- **Inputs.** `PREREG-C1.md` r6 §8.2 (the questions and the reviewers' recommendations) and §2–§4, §7, §9;
  `BORNSEL-B-MEASURE.md` r3 (`BSB:N`); QB-1 and QB-2 (#1059 c.6624262539). Corpus lines are at `origin/main`
  `1609dc440f5a12d05b750f6d894bb91d09a099a3`.
- **Labels.** [P] a citation at the base; [D] a derivation in this file, unreviewed; [O] an owner decision;
  **Rev** the recommendation recorded in PREREG §8.2 from the C-1 reviews.

**Two facts that apply to every row.**
- **Every OQ blocks `F` procedurally.** PREREG §7 step 1 and §8.1 require all fifteen answers, written into the text and
  reviewed, before the owner can designate `F`. The column "Blocks `F`" below therefore says *yes* for every row, and
  says separately whether the answer is **substantive** (it changes what C-1 tests, its scope or its verdict) or
  **confirmatory** (the corpus or a proof leaves one reasonable answer).
- **No answer changes part (b)'s accepted paper result** (BSB §4: no branch is selected; the Born form is
  branch-invariant; the numbers are κ-functionals). The answers fix what C-1 would test. The column "(b) analysis
  depends" marks the OQs on which the remaining measure analysis depends (summary at the end).

***

## The table

### OQ-1, `ℓ_min`
- **Question.** "The draft uses `ℓ_min = n + 1` (§2.5). The corpus leaves 'small p' unquantified (Main:62)."
- **Options.** (A) `n + 1`; (B) `2` (fixed points only); (C) one number common to all instances.
- **Recommended: (A)**, as Rev.
  - It is the least length at which some root is guaranteed two hidden states on the orbit (pigeonhole, PREREG §2.5),
    so it is the weakest instance-scaled reading of Main:62's C3 argument.
  - (C) ignores that `n` ranges over 4–16 across the instances. (B) admits orbits on which every visited root has one
    hidden state, whose `T^{α,O}` is then 0/1 by construction.
  - Caveat [D]: a non-permutation `T^{α,O}` already forces `max_a n_a(O) ≥ 2`. So under 13b/13d (OQ-13) the threshold
    is partly redundant with `Long′`, and it also drops non-permutation orbits of length `≤ n` that visit fewer than
    `n` rows. Every orbit's `|O|` and `eq` are recorded (PREREG §2.5), so this is visible after a run, but no verdict
    is issued on it.
- **Consequences.** For (b): none; `ℓ_min` is a scope parameter of the test, not a premise about μ. For C-1: (B)
  enlarges `Long`, and short deterministic orbits then give R0 and S2 NOT by mechanism (ii) of PREREG §9; (C) makes
  the threshold arbitrary for some instances.
- **Blocks `F`:** yes; substantive, but low risk. **(b) analysis depends:** no.

### OQ-2, the visible content of a site
- **Question.** "The draft uses the full `(prev, cur)` pair at each site of `R`, following `cutRealization` … The
  alternative is the current value only."
- **Options.** (A) `(prev, cur)` only; (B) `cur` only; (C) both, as two frozen readouts of the same instances.
- **Recommended: (C)**, or (A) with its stated support corrected. **This differs from Rev.**
  - Rev records "corpus answers — forced" by `cutRealization` (`PhysicalC4Discharge.lean:578–582`). The corpus has a
    second, competing statement: Main:222, "The transition probabilities `T_ij` are projections of the full
    phase-space flow onto the configuration sector of `Γ_V`, with momenta and hidden-sector degrees of freedom absorbed
    into the Liouville marginalization" [P]. Read on the second-order rule, the configuration is `cur` and `prev` is
    absorbed into the hidden side [D]. The kernel's cut and Main:222's readout therefore differ, and which one is
    native is the open planning item O-ACC (#914 row O-ACC; also recorded in the O-OBSMU note, below). The choice is
    not forced.
  - Main:288's theorem is stated for Main:117's `T_ij`, which Main:222 places in the configuration sector. So (B) is
    at least as faithful to "the numbers the representation carries" as (A).
  - (C) costs little [D]: `φ`, `S` and the orbits are unchanged; only `π_V` and the word of each orbit change. Under
    (B), `n = q^r` (2, 3 or 4), so `ℓ_min = 3, 4, 5`.
- **Consequences.** For (b): the C-1 verdict is a statement about one declared cut. Under (A) alone it says nothing
  about the configuration-sector readout of Main:222, and the reverse. For C-1: (C) adds a readout family, its own
  WF control (OQ-10) and a selection row; OQ-4 changes with it (W-q2-L7-r2 is non-void under (B) [D]: `ord(φ) = 14` by
  SM:1606, so some orbit has length 7 or 14, at least `ℓ_min = 5`). (A) needs the support sentence corrected from "forced" to "the kernel's `cutRealization`
  reading; Main:222's configuration readout is not tested".
- **Blocks `F`:** yes; substantive. **(b) analysis depends:** yes, for which cut the numbers belong to.

### OQ-3, the coupling
- **Question.** "The draft uses `a = 1` only … At `q = 3`, `a = 2 ≡ −1` is not covered."
- **Options.** (A) `a = 1`; (B) add `a = 2` at `q = 3`.
- **Recommended: (A)**, as Rev (SM:1602 writes the `d = 1` ring with coefficient 1).
  - Sharpening [D]: on a ring with `L` even, the staggered negation `g(p, c)_i = (−1)^i (p_i, c_i)` satisfies
    `g ∘ φ_a = φ_{−a} ∘ g`, because `(−1)^i (−1)^{i±1} = −1`. `g` relabels `𝒞_V` and `𝒞_H` bijectively and keeps the
    product split, so every C-1 field is relabelled and every verdict is unchanged. At `q = 3`, `a = 2` would
    therefore add information only at odd `L` (N3, N9), not at N7.
- **Consequences.** For (b): none. For C-1: scope stays `a = 1` (PREREG §9).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.

### OQ-4, the instance list
- **Question.** "The draft has eleven instances … and excludes W-q2-L7-r2 … The question is also which instances
  count toward the overall verdicts."
- **Options.** (A) eleven, all counting (draft); (B) as (A), plus W-q2-L7-r2 recorded; (C) count only N10 and N11,
  where Theorem 22's diameter hypothesis holds.
- **Recommended: (B)**, as Rev, with every non-void instance counting.
  - C-1 asserts nothing about (C1) (PREREG §2.2), so Theorem 22's diameter hypothesis does not bear on C-1's question
    and should not gate counting. A recorded N10/N11 secondary is harmless.
  - W-q2-L7-r2 costs nothing and adds an RX-ORD point at `r = 2`. Under OQ-2 (B)/(C) it is also non-void.
- **Consequences.** For (b): the instance list is the whole scope of any C-1 statement (`d = 1`, outside posit (v)'s
  `d ≥ 2` splitting clause and the `d = 3` manuscript instance; PREREG §2.1, §9). For C-1: (C) leaves two instances.
- **Blocks `F`:** yes; substantive (scope). **(b) analysis depends:** no.

### OQ-5, the α-rooted family's row set
- **Question.** "The draft uses `V_O` only, with horizon `{0, …, |O|}` (§2.4)."
- **Options.** (A) `V_O`; (B) all of `𝒞_V`, with a convention on unvisited roots.
- **Recommended: (A)**, as Rev. α defines no hidden conditional on an unvisited root, so (B) would add an arbitrary
  datum (BSB:147).
- **Consequences.** None for (b); by Lemma PD the record is a function of the comparison data (PREREG §2.4).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.

### OQ-6, β's P-divisibility on native instances
- **Question.** "The draft records it."
- **Options.** (A) record; (B) omit.
- **Recommended: (A)**, as Rev. By Lemma PD it equals "`T^β` is a permutation matrix", which `beta_is_permutation`
  already records, so it is redundant but free.
- **Consequences.** None for (b) or the verdict.
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.

### OQ-7, RX-ORD
- **Question.** "The draft records it only." Rev: make it gating, because "a cycle-detection bug that fragments orbits
  while still partitioning `S`" is otherwise uncaught.
- **Options.** (A) recorded only; (B) gating on `ord(φ) = qL` (SM:1606), with a new exit code; (C) **a gating
  closure check** under the existing exit 4 — every recorded orbit is a list of distinct states with
  `φ(s_k) = s_{k+1}` and `φ(s_last) = s_0` — plus a mutation that fragments one cycle and must be caught, with RX-ORD
  kept as a record.
- **Recommended: (C).** [D] A partition of `S` into closed `φ`-cycles is exactly the cycle decomposition, so (C)
  catches the fragmenting bug directly. The mixture identity does not (it is a partition identity), and nor does
  `Σ|O| = |S|`. (B) catches only bugs that change `ord(φ)`, needs a new exit code, and makes a companion-paper theorem
  a gate on a part (b) verdict: a fault in either the tool or SM Appendix A would halt the run without saying which.
- **Consequences.** For (b): none. For C-1: (A) leaves the fragmentation hazard open (PREREG §9 says so); (C) adds one
  invariant and one mutation (OQ-10).
- **Blocks `F`:** yes; substantive (control validity, §A.29). **(b) analysis depends:** no.

### OQ-8, the aggregation
- **Question.** "The draft applies §4.2's map, in which void instances do not count, to each variant."
- **Options.** (A) accept; (B) another map.
- **Recommended: (A)**, as Rev. The five cases are exhaustive and exclusive, and FREQ_VACUOUS and VOID are listed
  separately, so a FREQ_ALL resting on few instances is visible in the verdict text.
- **Consequences.** None for (b).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.

### OQ-9, Lemma PD
- **Question.** "The draft adopts the reduction to '`Γ₁` is a permutation matrix', with the certified definitional
  method on toys (§2.4)."
- **Options.** (A) accept; (B) compute P-divisibility by the definition on natives too.
- **Recommended: (A)**, as Rev. It is a proof, checked in both directions by the reviewer; the certified method on
  toys is its countercontrol.
- **Consequences.** None for (b).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.

### OQ-10, the controls
- **Question.** "The draft has the 21 gating controls of §3."
- **Options.** (A) accept 21; (B) accept and add Rev's two unadded items (an `n = 3` toy for `first_mismatch` order; a
  WF step at `r = 2`); (C) as (B) plus the controls the other answers require.
- **Recommended: (C)**, with this content:
  - a WF step at N6's parameters (`r = 2`). [D] No hand-derived value currently checks the `r = 2` visible projection;
    the two implementations of `φ` agree with each other but share `π_V`;
  - the fragmentation mutation, if OQ-7 (C);
  - a WF step for the `cur`-only projection, if OQ-2 (B) or (C);
  - the `n = 3` `first_mismatch` toy is optional: `first_mismatch` is diagnostic and enters no verdict.
- **Consequences.** None for (b). For C-1: the new expected values must be hand-derived and reviewed before `F`.
- **Blocks `F`:** yes; substantive for the added items. **(b) analysis depends:** no.

### OQ-11, the QB readings
- **Question.** "The draft identifies the variant's credence as the QB-2 credence, and `T^{α,O}` as the QB-1 target at
  the cycle horizon (§2.6)."
- **Options.** (A) accept; (B) reject either identification.
- **Recommended: (A)**, as Rev, with both limits stated where C-1's verdict is reported:
  - **frequencies versus credences** [O, QB-1]: `T^{α,O}` is the operational target *at the cycle horizon only*
    (Lemma A, BSB:239–243); accessible-window frequencies are C-3 and untested;
  - **prior versus conditioning** [O, QB-2]: the credence is an invariant prior conditioned on the present-visible
    record (γ-c, BSB:206–208); which orbits the prior ranges over is OQ-13 (ii).
- **Consequences.** For (b): under (A), a FREQ coincidence would make the one-step numbers the same whether read as
  frequencies or as credences on those instances; it would not supply a source for either (BSB:181). Under (B), C-1
  answers a question the owner has not posed and should be redrafted.
- **Blocks `F`:** yes; substantive. **(b) analysis depends:** yes.

### OQ-13, the candidates and the support of the credence prior
(Placed before OQ-12 because OQ-12 depends on it.)
- **Question.** "(i) Are the candidates for `O*` the long orbits, or the long orbits that carry history readback
  (`Long′`)? (ii) Does QB-2's invariant prior range over all orbits, or over the candidate orbits only?"
- **Options.** 13a (Long, all), 13b (Long′, all), 13c (Long, candidates), 13d (Long′, candidates), or a new variant
  written in before `F`.
- **Recommended: 13b** (variant S1). Rev left it to the owner.
  - **(ii), all orbits.** [D, from BSB N3] Under QB-2 with the present-visible record `x₀ = a`, the record-compatible
    orbits are all orbits that visit `a`, short ones included, and the prior conditioned on the record is
    `unif({a} × 𝒞_H)`, whose one-step numbers are row `a` of `T^β`. These are exactly the numbers the representation
    carries: Main:282 sets `ρ_H = I_m/m` and Main:288–290 outputs `T_ij` [P]. Restricting the prior to candidate orbits
    would condition on "the actual orbit is observer-bearing", which is not a visible record. It would also replace
    the representation's numbers by `T^{β|C}`, so the selected verdict would no longer test them.
  - **Against (ii) = candidates.** Main:62 places "the atypical short orbits" "outside the scope of every theorem
    below" in the same clause as the records selection [P]. The O-OBSMU note reads this as excluding observer-lacking
    orbits from the measure (its H-OC_orb). If the owner adopts that reading, Main:62 and Main:282 then disagree on
    the prior, and that disagreement belongs to O3/QB-2, not to C-1. Choose 13d in that case, knowing that by Lemma V′
    it tests whether the candidate orbits agree with one another, not whether they agree with Main:288's numbers.
  - **(i), `Long′`.** Under QB-1 the target is the frequencies along the actual trajectory. If `T^{α,O*}` were a
    permutation matrix, the visible process on `O*` would be deterministic at every horizon (PREREG §2.4,
    Lemma PD), contradicting the non-deterministic record any observer of stochastic outcomes holds. So `Long′` uses
    an operational record, not a new premise.
    - Skepticism (§A.31): 13b removes NOT-mechanism (ii), so it is the variant more favourable to FREQ. Removing (ii)
      is justified only by that record; R0 is recorded beside it, so the cost of the exclusion stays visible.
- **Consequences.**
  - For (b): under 13a/13b a FREQ_ALL says that on those instances the Born-form numbers equal the cycle frequencies
    of every admissible actual orbit, so α and β agree on one-step numbers there. A NOT_ALL or MIXED extends B3's
    non-invariance (CE-8, generic bijections) to the native rule at those sizes. Under 13c/13d C-1 bears on whether the
    identity of the actual orbit matters, not on Main:288's numbers.
  - For C-1: sets `oq13_answer` and the selected variant (PREREG §4.2).
- **Blocks `F`:** yes; substantive (it selects the verdict). **(b) analysis depends:** yes, both parts.

### OQ-12, the governance form
- **Question.** "One option is a research run on a disposable branch, not a §A.39 native V3 round … The other is a
  native V3 round."
- **Options.** (A) research run; (B) native V3 round.
- **Recommended: (A)**, unless the owner intends C-1 to support a status record (QB-3, the μ-number record on
  O-OBSMU), in which case (B) now.
  - C-1 is on the consistency axis and moves no band (§A.23). Under (A) the tool, command and `summary.json` still
    land on `main` with the result note (PREREG §7), which makes the result reproducible from `main` (§A.42 item 1)
    but not §A.39-protocol-valid.
  - Choosing (A) now and needing (B) later would mean a second freeze and run.
- **Consequences.** For (b): under (A) no status change rests on C-1 by itself. For C-1: (B) rewrites PREREG §7 to
  the §A.39 lifecycle before review.
- **Blocks `F`:** yes; substantive (governance). **(b) analysis depends:** only through QB-3.

### OQ-14, rerun after a runner failure before step (a)
- **Question.** "`run_attempt = 1`, with no exception, would let such a failure spend the freeze."
- **Options.** (A) no rerun; the freeze is spent; (B) one further dispatch under a new recorded owner approval, citing
  the failed run's id.
- **Recommended: (B)**, as Rev, admissible only when the host's step records (§A.44) show that step (a) never started.
  Restate the invariant as "the check step ran in exactly one attempt".
- **Consequences.** None for (b). Under (A) an infrastructure fault spends the freeze and yields no information.
- **Blocks `F`:** yes; substantive (run validity). **(b) analysis depends:** no.

### OQ-15, the twin relation and the cross-check groups
- **Question.** "The draft defines twin classes intrinsically: orbits with the same primitive cyclic visible word …
  The draft keeps frozen generators as a cross-check only."
- **Options.** (A) word relation, with the group cross-check; (B) word relation, no cross-check; (C) group-defined
  classes.
- **Recommended: (A)**, as Rev. The word relation contains every twin pair a visible-fixing symmetry commuting with `φ`
  can produce (PREREG §2.7), and (C) is provably incomplete (the hidden-supported translations at N2, N3, N5, N10).
  The cross-check costs nothing and tests the tool.
- **Consequences.** None for (b). For C-1: (C) would make `shared_rows` miscount, which is how review findings N6 and
  N7 arose.
- **Blocks `F`:** yes; confirmatory once (A) is taken. **(b) analysis depends:** no.

***

## Which answers must be decided together

1. **OQ-2, OQ-1, OQ-4 and OQ-10.** The readout fixes `n`, hence `ℓ_min = n + 1`, hence which instances are void
   (W-q2-L7-r2) and which WF controls are needed.
2. **OQ-11 and OQ-13.** OQ-11 fixes what the two sides of the comparison are; OQ-13 (ii) fixes the prior inside the
   credence side. The OQ-13 (ii) answer should be consistent with the owner's reading of Main:62 against Main:282
   (O3/QB-2).
3. **OQ-7 and OQ-10.** A gating closure check (OQ-7 (C)) needs its mutation control.
4. **OQ-12 with QB-3, and OQ-14 with OQ-12.** Governance depends on whether C-1 is to support a status record. The
   rerun policy is written into whichever lifecycle is chosen.
5. OQ-3, OQ-5, OQ-6, OQ-8, OQ-9 and OQ-15 can be decided independently.

## Dependence of the remaining part (b) measure analysis on these answers

Paused at this checkpoint by the owner's order of work. No analysis text is written here.
- **Independent of every OQ** (the C-1 questions fix only the test): which branch, if any, a current premise selects
  (BSB N2: none); that under QB-2 with present-visible records the credence numbers are β-conditioning (γ-c, BSB N3)
  and under QB-1 the cycle-horizon frequencies are α (Lemma A); the three distinctions (Born form versus numerical
  source, frequencies versus credences, invariant prior versus conditioning); and the classification against the
  O-OBSMU groups (orbit-level records conditioning b-stated, CR_rec a construction step under D-OB7, slice
  conditioning on stipulated events b-new, the measure posited).
- **Dependent:** whether the representation's numbers coincide with operational frequencies on the native rule
  (OQ-11, OQ-13, OQ-2, and the C-1 run itself, which is not authorized); which cut the numbers belong to (OQ-2); which
  orbits the invariant prior ranges over (OQ-13 (ii)); and whether any C-1 outcome may support a μ-number record
  (OQ-12, QB-3).

## Other findings
- **OQ-2's recorded reviewer note.** PREREG §8.2 item 2 records "corpus answers — forced" by `cutRealization`. Main:222
  is a competing corpus statement (OQ-2 above). PREREG is not edited here; the owner's answer would be written in at
  §7 step 2.
- **A dangling reference.** PREREG line 19 cites "review `REVIEW-7b46d36c.md`: ACCEPT". No such file is on this branch
  or in its history. The review is recorded in #1082 c.6622587957. The citation should name that comment when the
  text is next revised (§A.42 item 8: provenance).

## Off-`main` references (§A.42 item 8)

| Reference | Used where | Classification |
|---|---|---|
| #1059 c.6649420231, c.6624262539 | authorization; QB-1, QB-2 | governance records, quoted |
| #1082 comments (reviews of the assessment and of C-1 r1–r6), and Rev in PREREG §8.2 | the recommendations compared with | provenance; no recommendation here rests on a review's authority |
| `PREREG-C1.md`, `BORNSEL-B-MEASURE.md` (this branch, off `main`) | throughout | the objects under decision; their derivations are [D] and unreviewed as evidence |
| O-OBSMU note, branch `research/o-obsmu-20261104` at `f67b9f0c` (#1110, off `main`) | OQ-13 (ii), the H-OC_orb reading; OQ-2, O-ACC | provenance. The recommendations rest on Main:62, :222, :282–290, which are on `main` |
| #914 row O-ACC | OQ-2 | planning record; no claim rests on it |

***
_Recommendations only. The owner decides OQ-1 to OQ-15. Running or freezing C-1 is not authorized._
