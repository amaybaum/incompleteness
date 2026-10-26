# PE-02 drafting notes

**Status: WIP / UNREVIEWED; planning only; no execution authorized.**

Companion to `PLAN.md`: the sources the draft rests on, how it reads Issue #934, the design-only checks made while
drafting, the points in #934 that are ambiguous, and the open owner decisions with recommendations. Nothing here is a
result.

## 1. Provenance

- **Branch:** `research/oi-pseudoentropy-20261025` at `efbfd0d7bae21de298874733df763f25c3727c18` (fetched 2026-10-26;
  remote head equal).
- **`main`:** `c967d6a931c294e456053be5e3bf5bb4f2d9ad1c`. The scoped ch18 sentence entered at `4d8ff648` (#933).
- **Owner direction (2026-10-26):** "PE-02 — Continue planning independently. No experimental authorization."
  NP-AVG-1 (#929, #935) has planning priority (§5).
- **Not committed or pushed.** Under §A.43 this draft belongs on the thread's guiding draft PR (#923) as a planning
  checkpoint once the caller or owner chooses to publish it; publishing authorizes nothing.

## 2. Sources read

| Source | Where | sha256 |
|---|---|---|
| Thread plan | `../README.md` | `27b03b22a2f2e6c841c1741c06be578bb5022c2cf4302bea16531a6917de9c2b` |
| Thread plan review | `../review/REVIEW.md` | `be943f7d5b5cce0cbfe3ee6e40d5cdc7785cb63e51ea56ea18dd5321da4e348d` |
| PE-01 plan (rev. 5) | `../pe01_bounded_tests_v1/PLAN.md` | `bf7b0cb9387eb69b8ffc925c0ed09a789911c670da2a0144408f3d473dd5e091` |
| PE-01 A1 | `amendments/A1-owner-decisions.md` | `4cb5b569533fcc25d4ef1ecf2ebd6f6b74d50af2b2ae4bdf2f2c3d73ba470ad2` |
| PE-01 A2 | `amendments/A2-open-items.md` | `aa6267bc3a909a6de814f2f4973233ae3d72f2536e3c97a18f39892bdede10e9` |
| PE-01 A3 | `amendments/A3-literature-tags.md` | `d28b374ba8ec113b801b11b9c573a25d0c526a61942a3bed3703acb3012acbfd` |
| PE-01 report | `REPORT.md` | `ae30119ba25575883a7390edc9ec06c41e6bab8e1ea920448ed5143a2dcfc0d8` |
| PE-01 results review | `review/results/REVIEW.md` | `1be39f73e5c9c904f0c357d767ca4fdd38b9765f2de399ba9f9e05d0534025ca` |
| PE-01 tag annex | `review/literature/TAGS-r2.md` | `1be54e7c56f80eecd3acb982c3d4261e237724fb15766a4786aeaf4ca94d6682` |
| PE-01 measurements | `results/measurements.json` | `f17109f10379d648fcb055c2a1868666205fae8499b35ca65ecedae7a41f067a` |
| PE-01 witness shard | `results/shards/n5-clk.json` | `3f6121e83e75ed7ed5d43817bb8fc63dc73ad5fbf7acd763c3261e11d972a963` |
| ch18 on `main` | `book/ch18-beyond.md:114`; mirror `FULL.md:4932` | `11e9948ba634ae9145b0a8894789b24a0260ee7ab4c372d98466212fdda55340` (whole file) |

Also read: `results/README.md` and `SHA256SUMS`; the witness records and `windows` of `n5-clk.json`; the
`provenance.json` timings of the `clk` shards; PE-01's `run.py`, `pe01/generators.py`, `pe01/observers.py`,
`pe01/embedded.py` (round order) and `pe01/params.py` (PIN and TH); the relevant passages of the plan, code and
literature reviews (plan review N7 and A2, code review R3, literature RECHECK-r2); `papers/Main.md:560` on `main`;
Issues #934 (with the owner's comment of 2026-10-26), #929 (with both comments), and PRs #923 and #935.

Read in part only: PE-01's plan and code reviews (grepped for charging, clock, table size and PE-02).

## 3. How the draft reads #934

1. **"A witness of PE-01's kind"** means a prediction witness meeting PE-01's (a)–(e), with (f) as restated. It is not
   restricted to $m = 2$ or to `G_clk`. The reported PE-01 witness is the calibration object (RP-01, CH-IFF).
2. **"Charged against the footprint threshold"** means the charged bits are added to PE-01's footprint
   $m + c + 1$ and compared with the same θ. The plan makes the charge physical (INT): a read-only program register in
   the visible sector, read by a fixed interpreter. That follows PE-01's plan review N7: `Main.md:560` pays for a
   program "as an initial condition", a read-only register counted as state.
3. **"Raw table size and/or fixed universal encoding, reported separately"**: both, as R and E. R is PE-01's printed
   `table_size_bits`, so its values can be checked against PE-01's records. E is a prefix-free code with one decoder for
   every $m$ and $K$.
4. **"θ, and whether it changes with what is charged"**: recommended $\theta = n + 1$ for every model, unchanged (O1).
5. **"Description-complexity variant"**: none governs; a reduced-form E-length is reported per witness (O3). The plan
   gives the reason: over an enumeration closed under reduction, the least E-charge in a behaviour class is already
   attained by an enumerated observer.
6. **"Classes … coverage complete within the enumerated class"**: complete at $n \le 8$ under U for the new generators,
   and complete in Part B for every PE-01-class observer that can meet a charged (f) at $n \le N_{\max}$, because all
   $m \ge 2$ cells are structurally empty there. $m = 0$ is added, because leaving out the cheapest observers would
   exclude exactly the candidates most likely to survive a charge.
7. **"The same tables with interventions disabled"** is $\mathrm{abl}(O) = (\rho_0, \rho_1, 0, \chi)$.
8. **"A `G_clk` variant whose clock ignores the observer's input"** needs one more hidden bit (`PLAN.md` §1.2): the
   pre-intervention visible bit already carries all earlier interventions, so no clock selector on $G_{clk}$'s own state
   space qualifies.
9. **"Controls that can fail"** are the four of `PLAN.md` §5, each with a stated failure condition. Since every PE-01
   witness is rejected under R and E, CH-IFF on PE-01's records alone would test only one direction; synthetic boundary
   witnesses and the planted witness supply the other.
10. **Outcome classes:** kept with exact definitions, and completed so that every factor combination receives exactly
    one label (`PLAN.md` §6 items 4–5). See ambiguity A2.

## 4. Design-only checks made while drafting

Both fix definitions or evaluate the plan's own formulas. Neither simulates an observer or computes an advantage, a
window or a witness. The scripts are in the drafter's scratchpad and are not committed; their outputs below are
drafting-time values, which EX4 and AR-C re-derive at run time.

**D1. The polynomial rule.** `least_primitive.py` (sha256
`7dc983fbb54016096def7a879036f269e5398730bb6d4ef336174bcc5c71df27`), run as `python3 -I least_primitive.py 24`,
output sha256 `f4c880f48bc0d0c132f226546e7d8feaa301297f57ea1e87b243949339fac5ec`.
- It finds the least primitive polynomial of each degree by integer value, testing $z^{2^n-1} = 1$ and
  $z^{(2^n-1)/q} \ne 1$ for every prime $q \mid 2^n - 1$.
- It prints `RULE_REPRODUCES_PE01 True`: the rule gives PE-01's $p_n$ and $p'_n$ for $n = 3..8$.
- Its values for $n = 9..24$ are `PLAN.md` §1.1's table. Every reciprocal is primitive.

**D2. The footprint arithmetic.** `charge_arith.py` (sha256
`45f37a47deb6b688e5dfd60ded3f83ca7f8a7a461bfbb6e45198a89979e3c256`), output sha256
`51aa19de3e0521a26fffe6890e53e41140ecd684630d54f4a0a03e6f86fe67ea`. It evaluates the §2.1 formulas.
- PE-01's witness: $F_U = 6$, $F_R = 37$, $F_E = 34$.
- Least $n$ with $n + 1 \ge F_C$ at $K = 4$: $m = 0$: R 9, E 11; $m = 1$: R 17, E 18; $m = 2$: R 36, E 31.
- Largest $K$ with $F_C \le n + 1$ (window floor ignored), $n = 3..24$:

| Model, $m$ | $n = 9$ | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R, 0 | 7 | 7 | 15 | 15 | 31 | 31 | 63 | 63 | 127 | 127 | 255 | 255 | 511 | 511 | 1023 | 1023 |
| R, 1 | – | – | – | – | 1 | 1 | 3 | 3 | 7 | 7 | 15 | 15 | 31 | 31 | 63 | 63 |
| E, 0 | 2 | 3 | 6 | 6 | 7 | 14 | 14 | 15 | 30 | 30 | 31 | 62 | 62 | 63 | 126 | 126 |
| E, 1 | – | – | – | – | – | 1 | 2 | 2 | 3 | 6 | 6 | 7 | 14 | 14 | 15 | 30 |

  Values below 4 admit no window. $m = 2$ is empty under both models throughout. At $n \le 8$ every charged entry is
  empty or below 4.

## 5. Coordination with NP-AVG-1

- NP-AVG-1 (#929) declares one background prior, i.i.d. fair on every non-source initial variable, as a named,
  supplied assumption, and owns any convention about averaging over backgrounds.
- PE-02 adopts no background-prior convention. Its priors are the stated laws of finite toy generators:
  - $\mu$ uniform on $\mathcal{C}_V \times \mathcal{C}_H$, i.e. i.i.d. fair bits, as PE-01 and consistent with NP-AVG-1;
  - `G_clkfix_u`: i.i.d. fair, consistent;
  - `G_clkfix` matched prior ($q_0 = x_0$) and `G_weak` ($x_0 = 0$): device priors for one comparison and one control,
    declared per generator. They are not proposed as conventions for any other thread. If the owner sees a conflict,
    O5's "uniform only" removes the first, and the planted control can move to a uniform prior with a different weak
    generator.
- PE-02 does not depend on any NP-AVG-1 outcome and stays meaningful if NP-AVG-1 finds no masking advantage (owner,
  #934). The owner's note that NP-AVG-1's geometry results may refine PE-02 is a refinement path only. Any change it
  prompts goes through a PE-02 amendment before freeze.
- No conflicting term is used: "background", "pad", "freshness" and "cone" do not appear in PE-02.

## 6. Open owner decisions, with recommendations

- **O1 — θ under charged models.** Recommended: $\theta = n + 1$ for U, R and E.
  - θ measures the observer against the generator's state, as A1 fixed it.
  - Option (ii), $n + 1 + D_C(\varphi)$, charges the generator's description too. It is symmetric, but its verdict
    flips with the generator encoding: the raw table of φ is $(n+1)2^{n+1}$ bits and admits everything, while a
    polynomial code is about $n$ bits and admits almost nothing. A rule that can be moved to fit either outcome fails
    the hard-to-vary test.
- **O2 — which charged models govern.** Recommended: R and E, each reported separately, as #934 allows. R ties PE-02 to
  PE-01's recorded number. E is the one universal code. Neither is privileged.
- **O3 — description-complexity proxy.** Recommended: information only (`PLAN.md` §2.2), because the existence question
  is already closed under reduction within the enumeration. A third governing model would add a third set of labels
  without new search coverage.
- **O4 — $N_{\max}$.** Recommended: 24.
  - At $N_{\max} = 8$ every charged cell is structurally empty, so the main question is answered by arithmetic alone:
    `UNCHARGED_ONLY[structural]` for every factor combination with a U-witness. That restates PE-01's REPORT and fails
    the productivity test.
  - $m = 1$ can enter the charged region only from $n = 17$ (R) or $18$ (E), and the actual onset moves up with
    $Z(\varphi)$, which is unknown at drafting. 24 leaves room for $m = 1$ under both models; 22 may not.
  - Cost: about $2^{25}$ seeds at the top $n$, 3–6 CI hours sharded (`PLAN.md` §10).
- **O5 — clock-ablated prior.** Recommended: matched primary, uniform as a reported variant. The matched prior isolates
  responsiveness: the passive record law is unchanged (CA-EQ). The uniform variant is the max-entropy, NP-AVG-1-
  consistent prior, but it also hides the clock phase, so it confounds two changes. It is cheap (Part A cost).
- **O6 — K0 status beyond $n = 8$.** Recommended: not computed. The family sizes grow (48 primitive polynomials at
  $n = 9$, 2048 at $n = 16$), K0 bears on no outcome, and PE-01 found no family-wide witness.
- **O7 — the secondary population.** Recommended: all active (a′)–(e) witnesses on `G_clk`, $n \le 8$, with (f$_U$)
  recorded per member. Restricting to admissible members leaves one cell (36 pairs), too few to separate the two
  ablations.
- **O8 — the stage name.** The thread README (and PE-01 §3, §7, §10 item 5) uses "PE-02" for a different question:
  computational versus physical observers, each direction separately (§A.34), and class-$\mathcal{Q}$ references.
  #934 uses "PE-02" for this stage. This draft follows #934 and the requested directory name. Recommended: the owner
  either renames the README's stage (for example PE-02b) or this one, and says whether the thread's first milestone
  ("PE-01 and PE-02") now refers to this stage.
- **O9 — Lemma A-SIM.** Recommended: adopt, after the plan review checks the proof. It turns PE-01's open target T2 for
  autonomous generators into a one-line statement ($m' = m + 1$ suffices). It also gives an exact control that runs the
  active and passive code paths against each other (ACT-SIM), and it shows what the clock ablation does and does not
  remove. No novelty is claimed; it is a standard simulation argument.

## 7. Ambiguities in #934

- **A1. The PE-02 label** collides with the README's PE-02 (O8).
- **A2. The outcome classes mix two kinds of label.** `SURVIVES_CHARGED`, `UNCHARGED_ONLY` and `NO_WITNESS_IN_SCOPE`
  compare accounting models within one activity level. `ACTIVE_ONLY` compares activity levels within one model. The
  four labels are also not exhaustive: a passive witness, or a missing shard, has no label. The plan keeps all four with
  exact definitions in two families (`PLAN.md` §6 items 4–5) and adds `PASSIVE_ALSO`, `PASSIVE_ONLY`, `NEITHER` and
  `INCOMPLETE`. `UNCHARGED_ONLY` gets a `structural` or `searched` sub-label, because otherwise an empty region would
  read as a search result.
- **A3. "Per factor combination."** With three binary factors, accounting is the outcome axis, not a cell axis. The plan
  reports per (activity, generator) for each charged model, and per (generator, model) for the activity contrast. Cells
  (generator, $n$, subclass, model) are never pooled for attribution, as PE-01.
- **A4. "A positive result under a charged model does not establish ch18's untested narrower claim."** "Positive" can
  mean a charged witness (positive for predictability) or the absence of one (positive for the claim). Either way
  nothing in PE-02 establishes the narrower claim, so `PLAN.md` §7 states it for every outcome.
- **A5. "The same tables with interventions disabled."** It could mean $a \equiv 0$ (the plan's reading), or actions
  that still enter the observer's record but no longer reach the generator. The second is what the clock ablation
  does on `G_clkfix`, so both readings are covered.
- **A6. "PE-02 does not re-run … it"** against "a byte-identical replay of the relevant PE-01 measurement". The plan
  reads the replay as a control on one shard (`n5-clk`), not a re-run of the study, and recomputes PE-01 cells only for
  the secondary population, cross-checked against PE-01's records (UX).
- **A7. θ for the ablated generator.** `G_clkfix` has $n + 1$ hidden bits, so $\log_2|\mathcal{C}_V \times \mathcal{C}_H|$
  is $n + 2$. The plan keeps $\theta = n + 1$, the LFSR degree rule, so that the ablation changes only responsiveness.
  This is a reading, open to the owner under O1.
- **A8. C2–C4.** #934 notes that PE-01 checked only C1 and does not ask PE-02 to check C2–C4. The plan keeps "T-level
  (C1) holds; C2–C4 not checked".

## 8. Assumption-watch markers (§A.31)

- **M1. "Bounded memory" and the program.** In finite-state prediction and bounded-memory learning (Feder–Merhav–
  Gutman; Raz), the resource is the number of states or bits of state, and the transition function is not charged.
  PE-01's uncharged convention is that standard one. `Main.md:560` charges a program register for its own construction.
  The scoped ch18 sentence says "observers of bounded memory" without fixing which convention it means; PE-02 measures
  what turns on that choice. Any wording change is a separate owner decision.
- **M2. Activity on autonomous generators.** By Lemma A-SIM, activity is worth at most one memory bit there. PE-01's
  REPORT ties its witness to "an active observer and G_clk's backaction". The lemma says the activity half of that
  attribution reduces to footprint on any autonomous generator. The clock ablation tests the backaction half.
- **M3. Structural emptiness looks like a negative.** Every charged region at $n \le 8$, and every $m \ge 2$ region in
  scope, is empty by arithmetic. The labels keep this apart from "searched, none found".
- **M4. The clock charge** may overcharge an observer whose own memory already keeps time (PE-01 plan review A2). PE-02
  keeps the fixed charge, which leans toward the favourable reading; the verdict says so wherever it reports no
  witness.
- **M5. (c) does not bind.** At θ = n + 1, (f) implies (c) for every admissible cell (PE-01 code review R3). In Part B,
  $K^{C}_{\max} \ll K_{\rm cx}$ for `G_lin` and `G_filt`, so (c) does not bind there either. AR-C still measures
  $K_{\rm cx}$.

## 9. What PE-02 would add beyond the two covered-in-kind results

The owner asked (#934) what a PE-02 plan adds beyond the 2006 clock-control fault attack and AGHP's mechanism.
- **The fault attack** reruns a separately clocked generator from one state with unbounded computation, and recovers
  state. PE-02 asks a resource question that work does not pose: does a within-trajectory prediction witness survive
  when the observer pays for its own description, and does its advantage need the clock to respond?
- **AGHP** fixes when passive linear statistics are exactly unbiased. PE-02 asks whether passive observers of any
  accounted size (`emb_m0`, `emb_m1` and their charges) gain on these generators, including on `G_clkfix`, where AGHP
  does not apply.
- Neither question is claimed new before the A3-rule reading of `PLAN.md` §11.

## 10. Not done

- No PE-02 code, no simulation, no computation of any advantage, window, $Z(\varphi)$ or $K_{\rm cx}$.
- No literature read for PE-02 beyond what PE-01's annex records.
- No independent review. The plan needs one before any owner decision is recorded or anything is frozen.
