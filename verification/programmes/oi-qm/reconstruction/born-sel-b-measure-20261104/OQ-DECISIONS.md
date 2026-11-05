# BORN-SEL (b): recommended answers to the C-1 owner questions OQ-1 to OQ-15 (#1059)

**Status.** WIP / UNVERIFIED. Paper only. Recommendations only: **the owner decides every item**, and nothing here is a
decision, an adopted premise or a change to `PREREG-C1.md` r6, which is left as it stands at `cde5ecbc`.
- **Review.** Both reviews are model-authored, and both returned ACCEPT WITH CHANGES.
  - r1 (`16bde823`) was reviewed in #1082 c.6649637586.
  - r2 (`cfdcb83e`) was delta-reviewed in #1082 c.6649769429.
  - This revision (r3) applies the delta review's required revisions 1–9 and has not been re-reviewed.
  - Each item gives the delta review's endorsement of r2 as **Review r2**.
- **Authorization.** #1059 c.6649420231: paper-only, part (b).
- **Writer.** `writer-born`.
- **Inputs.**
  - `PREREG-C1.md` r6: §8.2, with the questions and the C-1 reviewers' recommendations, and §2–§4, §7, §9;
  - `BORNSEL-B-MEASURE.md` r3 (`BSB:N`);
  - QB-1 and QB-2 (#1059 c.6624262539).

  Corpus lines are at `origin/main` `1609dc440f5a12d05b750f6d894bb91d09a099a3`.
- **Labels.**
  - [P] a citation at the base;
  - [D] a derivation in this file, unreviewed unless stated;
  - [O] an owner decision;
  - **Rev** the recommendation recorded in PREREG §8.2 from the C-1 reviews. The individual C-1 review texts are not
    posted on #1082, so Rev is checked against PREREG §8.2 only.

**Two facts that apply to every row.**
- **Every OQ blocks `F` procedurally.** PREREG §7 step 1 and §8.1 require all fifteen answers before the owner can
  designate `F`. The answers must be written into the text and reviewed. Each row says whether its answer is
  **substantive** (it changes what C-1 tests, its scope, its controls or its governance) or **confirmatory** (the
  corpus or a proof leaves one reasonable answer).
- **No answer changes part (b)'s accepted paper result** (BSB §4):
  - no branch is selected;
  - the Born form is branch-invariant;
  - the numbers are κ-functionals.

  The answers fix what C-1 would test. "(b) analysis depends" marks the OQs on which the remaining measure analysis
  depends.

***

## The table

### OQ-1, `ℓ_min`
- **Question.** "The draft uses `ℓ_min = n + 1` (§2.5). The corpus leaves 'small p' unquantified (Main:62)."
- **Options.**
  - (A) `n + 1`;
  - (B) `2`, which excludes fixed points only;
  - (C) one number common to all instances;
  - (D) the direct capacity predicate `max_a n_a(O) ≥ 2`, with no length threshold.
- **Recommended: (A)**, as Rev.
  - It is the least length at which some root is guaranteed two hidden states on the orbit (pigeonhole, PREREG §2.5).
    So it is the weakest instance-scaled reading of Main:62's C3 argument.
  - (D) is the intrinsic form of the same capacity condition. It admits short orbits that happen to repeat a visible
    value.
  - (C) ignores that `n` ranges over 4–16 across the instances.
  - (B) admits orbits on which every visited root has one hidden state. Their `T^{α,O}` is then 0/1 by construction.
  - **Caveat [D].**
    - A non-permutation `T^{α,O}` forces `max_a n_a(O) ≥ 2`. So under `Long′`, (A) and (D) differ only on
      non-permutation orbits with `|V_O| < |O| ≤ n`, which (A) drops.
    - Every orbit's `|O|` and `eq` are recorded (PREREG §2.5), so this shows after a run. No verdict is issued on it.
- **Consequences.**
  - For (b): none. `ℓ_min` is a scope parameter of the test, not a premise about μ.
  - For C-1:
    - (B) enlarges `Long`, and short deterministic orbits then give R0 and S2 NOT by mechanism (ii) of PREREG §9;
    - (D) can change `Long` on any instance;
    - (C) makes the threshold arbitrary for some instances.
- **Blocks `F`:** yes; substantive (scope). **(b) analysis depends:** no.
- **Review r2:** YES WITH CHANGE (wording, applied).

### OQ-2, the visible content of a site
- **Question.** "The draft uses the full `(prev, cur)` pair at each site of `R`, following `cutRealization` … The
  alternative is the current value only."
- **Options.**
  - (A) `(prev, cur)` only;
  - (B) `cur` only;
  - (C) both, as two frozen readouts of the same instances.
- **Recommended: (C)**, or (A) with its stated support corrected. **This differs from Rev.**
  - **Not forced.** Rev records "corpus answers — forced" by `cutRealization` (`PhysicalC4Discharge.lean:578–590`).
    That is a kernel *definition*: it encodes one modelling choice and rules out no other split.
  - **What the corpus says.**
    - Main:288 is a representation identity that holds for every product split, so it does not choose between the
      readouts.
    - Only Main:222 bears on the choice: "The transition probabilities `T_ij` are projections of the full
      phase-space flow onto the configuration sector of `Γ_V`, with momenta and hidden-sector degrees of freedom
      absorbed into the Liouville marginalization" [P].
    - Read on the second-order rule, the configuration is `cur`, and `prev` is absorbed into the hidden side [D].
    - Whether the retained tick is native is the open planning item O-ACC (#914 row O-ACC).
    - Any C-1 verdict holds only for the declared cut.
  - **Cost of (C)** [D]. `φ`, `S` and the orbits are unchanged; only `π_V` and each orbit's word change. Under (B),
    `n = q^r` (2, 3 or 4), so `ℓ_min = 3, 4, 5`.
  - **How the verdict is defined under (C)** (to be frozen before `F`). Recommended:
    - **(i) One `oq13_answer` for both readouts.** The same variant is selected for each. The OQ-13 question concerns
      the prior and the candidates, not the cut.
    - **(ii) One run, one halt.** The controls (§3) run once and gate both readouts. A failure of any control, or of
      any invariant under either readout, halts the whole run. Neither readout's verdict is then printed.
    - **(iii) Per-readout aggregation.** Each readout gets its own §4.1–§4.2 evaluation over its own instance list.
      W-q2-L7-r2 counts in the `cur` aggregation on every variant where it is non-void. In the `(prev, cur)`
      aggregation it is VOID and is listed only.
    - **(iv) A pair of verdicts.** `c1_verdict` is replaced throughout by the pair `c1_verdict_pc` and
      `c1_verdict_cur`, and each `c1_*_verdict` likewise:
      - in `summary.json` and the schema;
      - in step (b)'s recomputation;
      - in step (c)'s verdict text;
      - in PREREG §4.3, §5 and §6.
    - There is no combined verdict across readouts. Each verdict is stated for its own readout only.
- **Consequences.**
  - For (b): the C-1 verdict is a statement about one declared cut. Under (A) alone it says nothing about Main:222's
    configuration-sector readout, and the reverse.
  - For C-1, under (C):
    - a second readout family, with its own WF control (OQ-10) and selection rows;
    - the word classes and `shared_rows` are recomputed per readout (OQ-15);
    - the aggregation map applies per readout (OQ-8).
  - **W-q2-L7-r2 under (B)** [D, reviewed in c.6649637586]. `ord(φ) = 14` (SM:1606) forces a cycle of length at least
    7, which is at least `ℓ_min = 5`. So `Long ≠ ∅`, and the instance is non-void under R0 and S2. This is
    conditional on SM Theorem A.1, which C-1 only records. `Long′ ≠ ∅` is not shown.
  - (A) needs its support sentence corrected from "forced" to "the kernel's `cutRealization` reading; Main:222's
    configuration readout is not tested".
- **Blocks `F`:** yes; substantive. **(b) analysis depends:** yes, for which cut the numbers belong to.
- **Review r2:** YES WITH CHANGE (the per-readout definition is completed above, (i)–(iv)).

### OQ-3, the coupling
- **Question.** "The draft uses `a = 1` only … At `q = 3`, `a = 2 ≡ −1` is not covered."
- **Options.** (A) `a = 1`; (B) add `a = 2` at `q = 3`.
- **Recommended: (A)**, as Rev (SM:1602 writes the `d = 1` ring with coefficient 1).
- **Sharpening** [D, checked by hand in c.6649637586].
  - On a ring with `L` even, the staggered negation `g(p, c)_i = (−1)^i (p_i, c_i)` satisfies `g ∘ φ_a = φ_{−a} ∘ g`,
    since `(−1)^i (−1)^{i±1} = −1`.
  - `g` relabels `𝒞_V` and `𝒞_H` bijectively and keeps the product split. At `r = 1` it fixes the visible values.
  - So at even `L`, `a = 2` is isomorphic to `a = 1`, and every verdict is unchanged. Order-dependent fields (`rep`,
    `first_mismatch`, `primitive_word`, `class_rep`, `orbits_sha256`) would be recomputed, not merely relabelled.
  - At `q = 3`, `a = 2` could add information only at odd `L` (N3, N9), not at N7.
- **Consequences.** For (b): none. For C-1: the scope stays `a = 1` (PREREG §9).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-4, the instance list
- **Question.** "The draft has eleven instances … and excludes W-q2-L7-r2 … The question is also which instances
  count toward the overall verdicts."
- **Options.**
  - (A) eleven, all counting (the draft);
  - (B) as (A), plus W-q2-L7-r2 recorded;
  - (C) count only N10 and N11, where Theorem 22's diameter hypothesis holds.
- **Recommended: (B)**, as Rev. Every non-void instance counts.
  - **Rev's N10/N11 secondary: recommended**, as a recorded secondary that carries no verdict. C-1 asserts nothing
    about (C1) (PREREG §2.2), so Theorem 22's diameter hypothesis does not bear on C-1's question and should not gate
    counting.
  - **W-q2-L7-r2 costs nothing and adds an RX-ORD point at `r = 2`.**
    - Under `(prev, cur)` it is void by the statement of SM Theorem A.1 (PREREG §2.2).
    - Under OQ-2 (B) or (C), the `cur` readout has `Long ≠ ∅`. This is conditional on SM Theorem A.1, and
      `Long′ ≠ ∅` is not shown (OQ-2).
- **Consequences.**
  - For (b): the instance list is the whole scope of any C-1 statement (PREREG §2.1, §9):
    - `d = 1`;
    - outside posit (v)'s `d ≥ 2` splitting clause;
    - not the `d = 3` manuscript instance.
  - For C-1: (C) leaves two instances.
- **Blocks `F`:** yes; substantive (scope). **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-5, the α-rooted family's row set
- **Question.** "The draft uses `V_O` only, with horizon `{0, …, |O|}` (§2.4)."
- **Options.** (A) `V_O`; (B) all of `𝒞_V`, with a convention on unvisited roots.
- **Recommended: (A)**, as Rev. α defines no hidden conditional on an unvisited root, so (B) would add an arbitrary
  datum (BSB:147).
- **Consequences.** None for (b). By Lemma PD, the record is a function of the comparison data (PREREG §2.4).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-6, β's P-divisibility on native instances
- **Question.** "The draft records it."
- **Options.** (A) record; (B) omit.
- **Recommended: (A)**, as Rev. By Lemma PD (OQ-9) it equals "`T^β` is a permutation matrix", which
  `beta_is_permutation` already records. It is redundant, but free.
- **Consequences.** None for (b) or for the verdict.
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-7, RX-ORD
- **Question.** "The draft records it only." Rev recommends making it gating, because "a cycle-detection bug that
  fragments orbits while still partitioning `S`" is otherwise uncaught.
- **Options.**
  - (A) recorded only;
  - (B) gating on `ord(φ) = qL` (SM:1606), with a new exit code;
  - (C) a gating closure check with a mutation, and RX-ORD kept as a record.
- **What (C) contains.**
  - On every native instance, every recorded orbit must be a list of distinct states with `φ(s_k) = s_{k+1}` and
    `φ(s_last) = s_0`. A failure exits 4, as the existing invariants do.
  - A new mutation, M-FRAG, splits one toy cycle into two non-closed lists. As with M-INJ (PREREG §3.3), its detection
    is a compared field: `closure_ok = false` must match the frozen expected value. It is not detected by an exit-4
    halt.
  - The toys already compare their `cycle` field against frozen values, which checks closure there.
  - **After detection.** As with M-INJ's `evaluated_beyond_injectivity = false`, the fragmented toy is not evaluated
    further. Recommended: a field `evaluated_beyond_closure = false`, compared.
  - **Every place the change touches.** M-FRAG alone raises the control count from 21 to 22. The change touches:
    - PREREG §3's execution-order paragraph: controls at orders 1–22, natives after them;
    - PREREG §3.3, which gets the M-FRAG entry;
    - PREREG §4.3, which adds closure to step (a)'s invariants;
    - PREREG §5's `summary.json` row, `controls_frozen` (21 → 22);
    - PREREG §6, which gets the closure invariant and its checkpoint;
    - `C1-INSTANCES.json`, which gets the entry and renumbered orders;
    - `C1-CONTROLS-EXPECTED.json`, which gets M-FRAG's expected values;
    - `C1-OUTPUT-SCHEMA.json`:
      - `controls_frozen` const and the `controls_matched` maximum;
      - the `order` maximum (32);
      - a `closure_ok` field, in the unit record for M-FRAG and in the native per-instance record;
      - the `evaluated_beyond_closure` field.

    The totals under the combined answers are in OQ-10.
- **Recommended: (C).**
  - [D, confirmed in c.6649637586] A partition of `S` into closed `φ`-cycles is exactly the cycle decomposition, so (C)
    catches the fragmenting bug directly.
  - The mixture identity is a partition identity and does not catch it, and nor does `Σ|O| = |S|`. r6 has no native
    closure check.
  - (B) catches only bugs that change `ord(φ)`, and it needs a new exit code. It also makes a companion-paper theorem
    a gate on a part (b) verdict: a fault in either the tool or SM Appendix A would halt the run without saying which.
- **Consequences.**
  - For (b): none.
  - For C-1:
    - (A) leaves the fragmentation hazard open, which PREREG §9 states;
    - (C) adds one native invariant and one mutation (OQ-10).
- **Blocks `F`:** yes; substantive (control validity, §A.29). **(b) analysis depends:** no.
- **Review r2:** YES WITH CHANGE (the full list of places touched is given above).

### OQ-8, the aggregation
- **Question.** "The draft applies §4.2's map, in which void instances do not count, to each variant."
- **Options.** (A) accept; (B) another map.
- **Recommended: (A)**, as Rev.
  - The five cases are exhaustive and mutually exclusive.
  - FREQ_VACUOUS and VOID are listed separately, so a FREQ_ALL resting on few instances shows in the verdict text.
  - Under OQ-2 (C) the map applies per readout.
- **Consequences.** None for (b).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-9, Lemma PD
- **Question.** "The draft adopts the reduction to '`Γ₁` is a permutation matrix', with the certified definitional
  method on toys (§2.4)."
- **Options.** (A) accept; (B) compute P-divisibility by the definition on natives too.
- **Recommended: (A)**, as Rev.
  - It is a proof (PREREG §2.4), which the C-1 reviewer checked in both directions (PREREG §8.2 item 9).
  - The certified method on toys is its countercontrol.
- **Consequences.** None for (b).
- **Blocks `F`:** yes; confirmatory. **(b) analysis depends:** no.
- **Review r2:** YES.

### OQ-10, the controls
- **Question.** "The draft has the 21 gating controls of §3."
- **Options.**
  - (A) accept the 21;
  - (B) accept, and add Rev's two unadded items: an `n = 3` toy for the order of `first_mismatch`, and a WF step at
    `r = 2`;
  - (C) as (B), plus the controls the other answers require.
- **Recommended: (C)**, with this content:
  - **A WF step at N6's parameters (`r = 2`).** [D, confirmed in c.6649637586] No hand-derived value checks the `r = 2`
    visible projection.
  - **M-FRAG**, if OQ-7 (C).
  - **A WF step for the `cur`-only projection**, if OQ-2 (B) or (C).
  - **The S4 obligation, if OQ-13 admits 13e.** PREREG §3.1 and §6 require every variant to be computed and compared
    on the toys, and each pair of variants to be separated by a control. For S4 that means:
    - S4's fields (`s4_verdict`, `s4_first_mismatch`, `s4_shared_rows`, `T_beta_np`, and per orbit `np`,
      `eq_beta_np` and `first_mismatch_beta_np`) are added to all eleven toys' expected values, derived by hand;
    - S4 is separated from R0, S1, S2 and S3. S4 and S3 differ only through a short non-permutation orbit, which needs
      `n ≥ 3` (OQ-13). So at least one new toy with `n ≥ 3` and such an orbit is required, for example CC-S4;
    - whether the existing toys separate S4 from R0, S1 and S2 has to be checked by hand. The OQ-13 witness separates
      S1 from S4 and could serve as a further toy.
  - **The `n = 3` `first_mismatch` toy is optional.** `first_mismatch` is diagnostic and enters no verdict.
- **Counts under the combined recommended answers** [D]. The answers are OQ-2 (C), OQ-4 (B), OQ-7 (C) and OQ-10 (C).
  - **Controls.** 21 + M-FRAG + WF at `r = 2` + WF for the `cur` readout = **24**.
    - Choosing 13e adds CC-S4, giving 25, and the witness toy if it is used, giving 26.
    - The optional `first_mismatch` toy adds one more.
  - **Native instances.** 12 (eleven plus W-q2-L7-r2), each evaluated under both readouts within one run.
  - **Orders.** The schema's `order` maximum becomes controls + 12, for example 36 at 24 controls, if each instance
    carries both readouts in one record. A per-readout record design would need its own count.
- **Consequences.** None for (b). For C-1: the new expected values must be hand-derived and reviewed before `F`.
- **Blocks `F`:** yes; substantive for the added items. **(b) analysis depends:** no.
- **Review r2:** YES WITH CHANGE (the S4 obligation and the counts are given above).

### OQ-11, the QB readings
- **Question.** "The draft identifies the variant's credence as the QB-2 credence, and `T^{α,O}` as the QB-1 target at
  the cycle horizon (§2.6)."
- **Options.** (A) accept; (B) reject either identification.
- **Recommended: (A)**, as Rev. Both limits are stated wherever C-1's verdict is reported:
  - **Frequencies versus credences** [O, QB-1]. `T^{α,O}` is the operational target *at the cycle horizon only*
    (Lemma A, BSB:239–243). Accessible-window frequencies are C-3 and are untested.
  - **Prior versus conditioning** [O, QB-2]. The credence is an invariant prior conditioned on a record. In r6 the
    record is the present visible value (γ-c, BSB:206–208). Which orbits the prior ranges over, and on which record
    it is conditioned, are OQ-13.
- **Consequences.**
  - For (b), under (A): a FREQ coincidence would make the one-step numbers the same whether they are read as
    frequencies or as credences on those instances. It would not supply a source for either (BSB:181).
  - Under (B), C-1 answers a question the owner has not posed and should be redrafted.
- **Blocks `F`:** yes; substantive. **(b) analysis depends:** yes.
- **Review r2:** YES.

### OQ-13, the candidates and the support of the credence prior
(Placed before OQ-12, which depends on it.)
- **Question.** "(i) Are the candidates for `O*` the long orbits, or the long orbits that carry history readback
  (`Long′`)? (ii) Does QB-2's invariant prior range over all orbits, or over the candidate orbits only?"
- **Options.**
  - 13a: candidates `Long`, prior over all orbits;
  - 13b: candidates `Long′`, prior over all orbits;
  - 13c: candidates `Long`, prior over the candidates;
  - 13d: candidates `Long′`, prior over the candidates;
  - **13e, a record-consistent fifth variant (new)**, written in as a frozen variant S4 before `F` (PREREG §4.2):
    - the candidates are `Long′`;
    - the prior is the invariant prior conditioned on the nondeterminism record, then on `x₀ = a`. That record is the
      part of `Long′`'s admission that is a record; `ℓ_min` is a C3 proxy, not a record;
    - in orbit terms, the prior ranges over `NP := {O : T^{α,O} not a permutation matrix on V_O}`, with no length
      threshold, and the credence is `T^{β|NP}`.
  - **How 13e relates to 13d** [D, consistent with c.6649769429].
    - `Long′ = Long ∩ NP`. So S4 differs from S3 only through short non-permutation orbits, those with
      `|V_O| < |O| < ℓ_min`.
    - Such an orbit needs `n ≥ 3`:
      - with `|V_O| = 1`, the 1×1 row is a permutation;
      - so `|V_O| ≥ 2`, and then `|O| ≥ |V_O| + 1 ≥ 3`;
      - with `|O| ≤ n`, this gives `n ≥ 3`.
    - **S4 ≡ S3 when `n = 2`.** This covers every `n = 2` toy and the `q = 2`, `r = 1` instances under the `cur`
      readout.
    - **S4 ≡ S3 under OQ-1 (D).** There, a non-permutation orbit has `max_a n_a ≥ 2`, so `NP ⊆ Long` and
      `Long′ = NP`.
    - **13e keeps the `ℓ_min` asymmetry.** Candidates are admitted by the record and by `ℓ_min`; the prior uses the
      record only. 13e is record-consistent for nondeterminism, not for the length threshold.
- **The C-1 reviewers' corpus leanings** (PREREG §8.2 item 13).
  - On (ii): Main:56 (Lemma 3, clause 2) and posit (iv) state the global counting prior, which favours 13a or 13b.
  - On (i): Main:74 makes (C1) the hidden-influence diagnostic, which supports `Long′`. Nothing in the corpus excludes
    permutation orbits outright.
- **Three facts the choice turns on.**
  1. **The record asymmetry.** 13b admits candidates by a visible-*history* record, but conditions the credence on
     the present value only.
     - The bridge [D]: an observer whose records show nondeterministic outcomes excludes every orbit whose `T^{α,O}`
       is a permutation matrix. On such an orbit the visible process is deterministic at every horizon (Lemma PD
       (⇐), PREREG §2.4).
     - Conditioning the prior on that same record leads outside 13a–13d, to 13e. 13b therefore uses a record on the
       candidate side that its credence side ignores.
     - This sits uneasily with an argument this table gave against restricting the prior to candidate orbits: that
       the restriction would condition on "the actual orbit is observer-bearing", which is not a visible record. The
       nondeterminism record *is* a visible-history record, so that argument does not exclude conditioning on it.
     - **The orbit-level coarsening is [D].** 13e conditions on the invariant event "some nondeterministic history
       occurs on the orbit", which is `NP`. Conditioning on one specific finite history `r` instead gives BSB A3's
       history-conditioned credence. That depends on `r`, so it cannot be frozen as one per-instance verdict, and it
       is not proposed.
  2. **What each variant compares** [D, from PREREG §2.3, §4.1].
     - **13a/13b** compare candidates with `T^β`, the numbers Main:288's representation carries. Main:282 sets
       `ρ_H = I_m/m`, and under QB-2 with the present-visible record the conditioned prior is `unif({a} × 𝒞_H)`
       (BSB N3, Lemma G).
     - **13c/13d** test whether the candidates agree with one another (Lemma V′).
     - **13e** compares candidates with the credence conditioned on the nondeterminism record. That credence is a
       mixture of `NP` orbits' rows, so 13e is partly a mutual-agreement test, and its credence is not `T^β`.
  3. **Favourability (§A.31)** [D, the first two items confirmed in c.6649637586].
     - S3 NOT ⇒ S1 NOT ⇒ R0 NOT:
       - `Long′ ⊆ Long` with the same credence gives the second implication;
       - by Lemma V′, two disagreeing candidates cannot both equal `T^β`, which gives the first.
     - So 13d is weakly the most favourable to FREQ, and 13b is more favourable only relative to 13a.
     - `Long′ ⊆ Long` can also turn an R0 NOT into an S1 VOID.
     - For 13e: S3 NOT ⇒ S4 NOT, since a mixture cannot equal two different rows.
     - **S1 NOT ⇏ S4 NOT.** Witness [D, checked by hand here; the reviewer's in c.6649769429]:
       - **The map.** `n = 2`, `m = 3`. One 4-cycle `(0,0) → (0,1) → (1,0) → (1,1) → (0,0)`, and fixed points
         `(0,2)` and `(1,2)`. `ℓ_min = 3`.
       - **The orbits.** The cycle's word is `0011`, so `T^{α}` has both rows `(1/2, 1/2)`; it is not a permutation,
         and it is long. The fixed points have length 1 and permutation rows.
       - **The sets.** `Long = Long′ = NP = {cycle}`.
       - **The credences.** `T^β` has row 0 `= (2/3, 1/3)` and row 1 `= (1/3, 2/3)`. `T^{β|NP}` is the cycle's own
         rows.
       - **S1.** The cycle does not match `T^β`. Rows 0 and 1 each pool the cycle with a fixed point, two word classes,
         so `shared_rows = 2`, and the verdict is NOT.
       - **S4.** The cycle matches its own rows. Each row's pool is the cycle alone, so `shared_rows = 0`, and the
         verdict is FREQ_VACUOUS.
     - **S4 NOT ⇏ S1 NOT is not shown.** A witness would need a short non-permutation orbit, hence `n ≥ 3`. None is
       given, so no further ordering between S4 and S1 is claimed.
- **The Main:62 / Main:282 reading.**
  - Read literally, Main:62's exclusion of short orbits is a scope statement, and Main:288 is a representation
    identity, so they do not contradict each other.
  - A tension arises only if Main:62 is read as excluding observer-lacking orbits from the prior itself (the O-OBSMU
    note's H-OC_orb reading). That question belongs to O3/QB-2, not to C-1.
- **Recommendation: a genuine choice among 13b, 13d and 13e**, decided by which question C-1 is meant to answer.
  - **13b,** if the question is "are the numbers Main:288's representation carries (`T^β`) the cycle frequencies of
    every admissible actual orbit?" This is part (b)'s own question: "which branch … fixes the probabilities the
    representation carries". The writer leans to 13b on that ground.
    - On this reading, the credence side is the representation's fixed object, not the observer's best credence, so
      the record asymmetry does not create an inconsistency.
    - The cost is that the candidate restriction rests on the [D] bridge, and R0 is recorded beside it.
  - **13e,** if the question is "is the credence conditioned on the observer's own record the operational frequency?"
    It applies QB-2 to the same record on both sides. It needs a new frozen variant, a separating toy (OQ-10) and
    review.
  - **13d,** if the owner reads Main:62 as excluding observer-lacking orbits from the prior. It then tests mutual
    agreement among candidates (Lemma V′) and is weakly the most favourable to FREQ.
  - **13a, not recommended.** It admits long permutation orbits as candidates, which the nondeterminism record
    excludes. Such an orbit mismatches `T^β` automatically (PREREG §9, mechanism (ii)), so an R0 NOT can reflect only
    that. R0 is recorded under every answer.
  - **13c, not recommended.** It restricts the prior to `Long`, a length-based C3 proxy and not a record, while still
    admitting permutation orbits as candidates. By Lemma V′, it then tests whether all long orbits agree with one
    another, deterministic ones included. A disagreement can therefore come from mechanism (ii) alone. It carries
    both asymmetries and resolves neither. S2 is recorded under
    every answer.
- **Consequences.**
  - For (b):
    - **Under 13b**, a FREQ_ALL would show that on those instances `T^β` equals the cycle frequencies of every
      admissible actual orbit, so α and β agree on one-step numbers there. A NOT_ALL or MIXED would extend B3's
      non-invariance (CE-8, generic bijections) to the native rule at those sizes.
    - **Under 13d or 13e**, C-1 bears on whether the identity of the actual orbit matters, or on the record-conditioned
      credence, and not directly on `T^β`.
  - For C-1: the answer sets `oq13_answer` and the selected variant (PREREG §4.2). 13e adds variant S4, its fields,
    its row in the selection table, its `shared_rows` pool (the `NP` orbits visiting `a`) and its control.
- **Blocks `F`:** yes; substantive (it selects the verdict). **(b) analysis depends:** yes, on both parts.
- **Review r2:** YES WITH CHANGE (applied above: the 13e precision, the S1/S4 witness and the narrowed claim, the 13a
  and 13c standing, and the argument restated in place).

### OQ-12, the governance form
- **Question.** "One option is a research run on a disposable branch, not a §A.39 native V3 round … The other is a
  native V3 round."
- **Options.** (A) research run; (B) native V3 round.
- **Recommended: (A).**
  - **This differs from Rev.** Rev's recommendation is conditional: (A) if the result is for the record only, and (B)
    if it is to support the O-OBSMU μ-number proposal. Here (A) is recommended in both cases. Using (B) for a
    status-supporting result is left to the owner as a policy choice.
  - C-1 is on the consistency axis and moves no band (§A.23).
  - Using (B) for a result meant to support a status record (QB-3, the μ-number record on O-OBSMU) is a policy choice
    the owner may make. It is not mandated.
  - Choosing (A) now and needing (B) later would mean a second freeze and run.
- **What either form needs** [P, §A.42 items 1, 2 and 8]. Before C-1's result is an enduring claim, `F` and the run
  commit must be reachable from `main`.
  - A verdict that depends on commits uses them. Copying the tool's files to `main` does not make `F` reachable.
  - PREREG §7 currently lands the tool, the command and `summary.json` with the result note. It does not provide for
    `F`'s ancestry, and should be revised to do so (for example, by landing the branch that contains `F`).
- **Consequences.**
  - For (b): under (A), no status change rests on C-1 by itself.
  - For C-1: (B) rewrites PREREG §7 to the §A.39 lifecycle before review. Either form needs the `F`-reachability
    provision.
- **Blocks `F`:** yes; substantive (governance). **(b) analysis depends:** only through QB-3.
- **Review r2:** YES WITH CHANGE (the difference from Rev is marked).

### OQ-14, rerun after a runner failure before step (a)
- **Question.** "`run_attempt = 1`, with no exception, would let such a failure spend the freeze."
- **Options.**
  - (A) no rerun; the freeze is spent;
  - (B) one further dispatch, under a new recorded owner approval citing the failed run's id.
- **Recommended: (B)**, as Rev, with two additions (§A.41, §A.44):
  - **The predicate.** The failed run qualifies only if the host's API job record shows step (a)'s step entry either
    absent, or with `started_at` null and conclusion `skipped` or null. It is read from the API, not from logs.
    - **These field semantics are to be verified against a real job record before `F`.** The predicate frozen at
      `F` must name the fields as the host actually returns them.
  - **The checkpoint.** Add to PREREG §6: "the check step ran in exactly one attempt". The result reviewer measures it
    from the API job records of every dispatch on `F`. Exactly one record must show step (a) started.
- **Consequences.** None for (b). Under (A), an infrastructure fault spends the freeze and yields no information.
- **Blocks `F`:** yes; substantive (run validity). **(b) analysis depends:** no.
- **Review r2:** YES WITH CHANGE (the field semantics are marked as to be verified; "must").

### OQ-15, the twin relation and the cross-check groups
- **Question.** "The draft defines twin classes intrinsically: orbits with the same primitive cyclic visible word …
  The draft keeps frozen generators as a cross-check only."
- **Options.**
  - (A) the word relation, with the group cross-check;
  - (B) the word relation, with no cross-check;
  - (C) classes defined by the group.
- **Recommended: (A)**, as Rev.
  - The word relation contains every twin pair that a visible-fixing symmetry commuting with `φ` can produce (PREREG
    §2.7).
  - (C) is incomplete: it misses the hidden-supported translations at N2, N3, N5 and N10. This rests on review
    findings N6 and N7 and on PREREG §2.7's derivation.
  - The cross-check costs nothing and tests the tool.
  - The visible word depends on `π_V`, so under OQ-2 (C) the classes are computed per readout.
- **Consequences.** None for (b). For C-1: (C) would make `shared_rows` miscount.
- **Blocks `F`:** yes; confirmatory once (A) is taken. **(b) analysis depends:** no.
- **Review r2:** YES.

***

## Which answers must be decided together

1. **OQ-2, OQ-1, OQ-4 and OQ-10.** The readout fixes `n`, hence `ℓ_min = n + 1`, hence which instances are void
   (W-q2-L7-r2) and which WF controls are needed.
2. **OQ-1 and OQ-13.** `ℓ_min` defines `Long` and `Long′`, and 13e's prior `NP` drops the length threshold.
3. **OQ-2 with OQ-13, OQ-8 and OQ-15.**
   - A second readout doubles the variant evaluations and the selection.
   - The aggregation applies per readout.
   - The word classes depend on `π_V`.
4. **OQ-11 and OQ-13.** OQ-11 fixes what the two sides of the comparison are. OQ-13 fixes the candidates, the prior's
   support and the conditioning record. The OQ-13 answer should be consistent with the owner's reading of Main:62
   against Main:282 (O3/QB-2).
5. **OQ-7 and OQ-10.** A gating closure check needs M-FRAG. OQ-13's 13e needs its own toy.
6. **OQ-6 and OQ-9.** Under Lemma PD, OQ-6's record is a function of `T^β`.
7. **OQ-12 with QB-3, and OQ-14 with OQ-12.** Governance depends on whether C-1 is to support a status record. The
   rerun policy is written into whichever lifecycle is chosen.
8. **Independent:** OQ-3 and OQ-5 only.

## Dependence of the remaining part (b) measure analysis on these answers

Paused at this checkpoint by the owner's order of work. No analysis text is written here.

**Independent of every OQ.** The C-1 questions fix only the test, so the following do not depend on them:
- which branch, if any, a current premise selects (BSB N2: none);
- that under QB-2 with present-visible records the credence numbers are β-conditioning (γ-c, BSB N3), and that under
  QB-1 the cycle-horizon frequencies are α (Lemma A);
- the three distinctions: Born form versus the source of the numbers; frequencies versus credences; invariant prior
  versus conditioning;
- the classification against the O-OBSMU groups:
  - orbit-level records conditioning is b-stated;
  - CR_rec is a construction step under D-OB7;
  - slice conditioning on stipulated events is b-new;
  - the measure is posited.

**Dependent on the OQ answers:**
- whether the numbers the representation carries coincide with operational frequencies on the native rule. This
  depends on OQ-11, OQ-13 and OQ-2, and on a C-1 run, which is not authorized;
- which cut the numbers belong to (OQ-2);
- which orbits the invariant prior ranges over, and on which record it is conditioned (OQ-13);
- whether any C-1 outcome may support a μ-number record (OQ-12, QB-3).

## Other findings
- **OQ-2's recorded reviewer note.** PREREG §8.2 item 2 records "corpus answers — forced" by `cutRealization`. That is
  an overstatement, and Main:222 is the discriminating corpus statement (OQ-2). PREREG is not edited here. The owner's
  answer would be written in at §7 step 2.
- **A dangling reference.** PREREG line 19 cites "review `REVIEW-7b46d36c.md`: ACCEPT". The file is in no tree or
  history (confirmed in c.6649637586). The ACCEPT is #1082 c.6622587957, and the citation should name that comment
  when the text is next revised.

## References not on `main` (§A.42 item 8)

Each reference is classified by reading the claim it is attached to: **provenance** (the claim does not use the
content), **support on `main`**, or **support off `main`** (a gap). This file is a mutable WIP record on a research
branch and is not landing. Every gap below must be closed before any record that relies on it lands. A gap is closed
by landing the content, or by narrowing the claim.

| Reference | Used where | Classification |
|---|---|---|
| Main:56, :62, :74, :117, :222, :282–290; SM:1602, :1606; `PhysicalC4Discharge.lean:578–590` | throughout | support on `main` |
| #1059 c.6649420231 (the activation record; it quotes amaybaum, Claude Code session chat, 2026-11-05, posted 2026-11-05T04:08:33Z) | the authorization | provenance |
| QB-1 and QB-2, #1059 c.6624262539 (amaybaum, chat 2026-11-04; posted 2026-11-04T06:28:41Z). QB-1: "Choose operational frequencies as the eventual physical meaning that OI must explain. Observer credences can describe predictions conditional on preparations, but cannot by themselves establish a Born probability law." QB-2: "Interpret the maximum-entropy branch as an invariant prior followed by conditioning, while leaving the physical source of that prior open." | OQ-11, OQ-13 | **support off `main`: a gap.** The recommendations use these decisions as premises of the comparison |
| Owner's order of work: #1059 c.6649688361 (2026-11-05T04:28:25Z), quoting amaybaum, Claude Code session chat, 2026-11-05: "For #1032 and #1059, continue within the already authorized scopes. In particular, present #1059's OQ-1–OQ-15 recommendations for owner decisions before proceeding with the dependent measure analysis." | the pause of the dependent analysis | provenance |
| `BORNSEL-B-MEASURE.md` r3 (this branch; reviewed ACCEPT, #1082 c.6622587957) | OQ-5, OQ-11, OQ-13; the dependence section | **support off `main`: a gap** (Lemmas A, A3, G, γ-c) |
| `PREREG-C1.md` r6 (this branch; accepted as a draft, #1082 c.6625738542) | every row (the questions, Lemma PD, Lemma V′, §2.7) | **support off `main`: a gap.** It is the object under decision |
| The C-1 review findings N6 and N7, and the C-1 reviewer's check of Lemma PD, as recorded in PREREG §2.7 and §8.2 | OQ-9, OQ-15 | **support off `main`: a gap.** The review texts are not posted (#1082 c.6625738542 summarizes them) |
| #1082 c.6649637586 (model-authored review of r1) and c.6649769429 (model-authored delta review of r2) | the [D] items marked as confirmed by them; the Review r2 column | provenance for the endorsement column. The [D] items stand on the derivations stated here, not on the reviews' authority |
| The O-OBSMU note, branch `research/o-obsmu-20261104` at `f67b9f0c` (#1110) | OQ-13, the H-OC_orb reading | provenance. The tension is stated from Main:62 and :282, which are on `main` |
| #914 row O-ACC | OQ-2 | provenance |

***
_Recommendations only. The owner decides OQ-1 to OQ-15. Running or freezing C-1 is not authorized._
