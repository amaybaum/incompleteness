# PE-05 drafting notes (revision 3)

**Status: decisions recorded; frozen pending independent confirmation.** Planning only; no execution authorized.

Companion to `PLAN.md`. It records:
- the sources the draft rests on;
- how the draft reads Issue #934;
- the design-only checks;
- the points in #934 that are ambiguous;
- the open owner decisions, with the drafter's and the review's recommendations.

Nothing here is a result. Revision 2's edits are mapped item by item in `CHANGES-r2.md`, and revision 3's in
`CHANGES-r3.md`.

## 1. Provenance

- **Revision 1** (`PLAN.md`, this file and `design/`) was committed on `research/oi-pseudoentropy-20261025` at
  `902c4c0d5a7d870e84cf60494955d3ebf3bccd4f`, on the thread's guiding draft PR #923.
- **Its independent review** was committed at `2bb45e0b2d641046f5c50b7b511ce5ac3983c02a` as `review/` (`REVIEW.md`
  sha256 `00995749368f5d60de2086d4c6f0b88c070ac8a106724dada9c0043bafb70521`). The verdict is ACCEPT WITH CHANGES,
  R1–R15, with no freeze until re-reviewed.
- **Revision 2** (`PLAN.md`, this file and `CHANGES-r2.md`) was committed at `58441eb2`.
- **Its diff-only re-review** was committed at `5b2ae247` as `review/RECHECK-r2.md`, with `r2_checks.py` and its
  output. The verdict is REVISE, narrowly: every R item is confirmed except R15, N1–N3 are required, and N4–N7 are
  nits.
- **Revision 3** (`PLAN.md`, this file, `CHANGES-r3.md`, and the new `design/charge_ranges.*` and
  `design/linear_class_code.*`) is drafted on `5b2ae247`. It is uncommitted at the time of writing. Committing it is the
  caller's or the owner's choice, and authorizes nothing (§A.43).
- **Revision 3** was committed at `b339c4b2`, and its diff-only re-check at `7a283d39` (`review/RECHECK-r3.md`: ACCEPT
  WITH NITS, P1–P3). P1–P3 are applied in place as part of revision 3 (`CHANGES-r3.md`, last section).
- **`main`:** `c967d6a931c294e456053be5e3bf5bb4f2d9ad1c`. The scoped ch18 sentence entered at `4d8ff648` (#933).
- **Owner direction (2026-10-26):** "PE-02 — Continue planning independently. No experimental authorization."
  NP-AVG-1 (#929, #935) has planning priority (§5).

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
| PE-05 review (r1) | `review/REVIEW.md`, with `toy_checks.*` and `tightness.*` | as in §1 and `review/REVIEW.md` |
| PE-05 re-review (r2) | `review/RECHECK-r2.md`, with `r2_checks.*` | committed at `5b2ae247` |

Also read:
- `results/README.md` and `SHA256SUMS`;
- the witness records of `n5-clk.json`, and the `windows` entries of every `n*-clk*.json` shard (revision 2, §4.3);
- the `provenance.json` timings of the `clk` shards;
- PE-01's `run.py`, `pe01/generators.py`, `pe01/observers.py`, `pe01/embedded.py` (round order) and `pe01/params.py`
  (PIN and TH);
- the `PYTHON_VERSION` and `NUMPY_VERSION` pins of `.github/workflows/pe01-bounded-tests.yml` (3.12, 2.2.6);
- the relevant passages of PE-01's plan, code and literature reviews (plan review N7 and A2, code review R3,
  literature RECHECK-r2);
- `papers/Main.md:560` on `main`;
- Issues #934 (with the owner's comment of 2026-10-26) and #929 (with both comments), and PRs #923 and #935.

Read in part only: PE-01's plan and code reviews, grepped for charging, clock, table size and PE-02.

**PE-01 data read for revision 2.** The §4.3 statements about the secondary population come from reading the
`windows` entries of PE-01's retained `G_clk` shards for $K \le K_{\rm cx}$. No PE-01 cell was recomputed. They agree
with the review's §9:
- `emb_m1_all` has no window at any $n$;
- `emb_m2_all` has windows at $n = 4$ ($K = 7, 8, 9$) and $n = 5$ ($K = 7, 10$) only;
- `emb_m2_passive` has none;
- `emb_m3_passive` has windows at $n = 4$ ($K = 7$–$9$), $n = 5$ ($K = 7$–$20$) and $n = 6$, and none within its caps at
  $n = 7, 8$.

## 3. How the draft reads #934

1. **"A witness of PE-01's kind"** is a prediction witness meeting PE-01's (a)–(e), with (f) as restated. It is not
   restricted to $m = 2$ or to `G_clk`. The reported PE-01 witness is the calibration object (RP-01, CH-IFF).
2. **"Charged against the footprint threshold"** means the charged bits are added to PE-01's footprint $m + c + 1$
   and compared with θ.
   - The plan makes the charge physical (INT): the charged bits sit in a read-only program register in the visible
     sector, read by a fixed interpreter.
   - That follows PE-01's plan review N7: `Main.md:560` pays for a program "as an initial condition".
3. **"Its transition and action tables, or a fixed encoding of them".** Revision 1 charged the full description: the
   transition and action tables, the readout and the trigger constant. The review notes that this goes beyond the
   literal wording, in the favourable direction. Revision 2 states the choice as owner decision O10 (new ambiguity A9)
   and reports per-witness components, so that either charge can be read.
4. **"Raw table size and/or fixed universal encoding, reported separately"** is read as both: R and E.
   - R is PE-01's printed `table_size_bits`.
   - E is a prefix-free code with one decoder for every $m$ and $K$. Revision 2 fixes its bit order and labelling (R14).
   - In scope, E's region lies inside R's (INC-RE), so E adds no E-only witness.
5. **"θ, and whether it changes with what is charged".** The drafter's and the review's recommendation is option (i),
   $\theta = n + 1$ under every model (O1). The corrected rationale is in §6.
6. **"Description-complexity variant".** None governs; a reduced-form E-length is reported per witness (O3).
7. **"Coverage complete within the enumerated class".**
   - At $n \le 8$ coverage is complete under U for the new generators.
   - In Part B it is complete for every PE-01-class observer that can meet a charged (f) at $n \le N_{\max}$:
     $m \ge 2$ is structurally empty, $m = 0$ is zero by M0, and $m = 1$ is enumerated in full.
   - Revision 1 gave a false reason for adding $m = 0$ ("the candidates most likely to survive"). Revision 2 proves
     $m = 0$ identically zero on every (a′) generator and keeps it as an exact-zero control (R4).
8. **"The same tables with interventions disabled"** is $\mathrm{abl}(O) = (\rho_0, \rho_1, 0, \chi)$.
9. **"A `G_clk` variant whose clock ignores the observer's input"** needs one more hidden bit (`PLAN.md` §1.2). The
   pre-intervention visible bit already carries all earlier interventions.
10. **"Controls that can fail"** are the four of `PLAN.md` §5. Revision 2 restates CH-IFF relative to each record's
    other conditions and specifies its synthetic boundary records (R2). It also restricts the PL countercontrol to
    $1 \le K \le 13$ (R1).
11. **Outcome classes.** They are kept with exact definitions, completed so that every case receives exactly one label,
    and, from revision 2, computed per $n$ (R8; ambiguities A2 and A3).

## 4. Design-only checks

Every script fixes a definition or evaluates the plan's own formulas. None simulates an observer or computes an
advantage, a window or a witness.
- `least_primitive` and `charge_arith` were committed under `design/` at `902c4c0d`, with their outputs.
- `charge_ranges` and `linear_class_code` are new in revision 3. Their outputs are written beside them, so that they
  replay once committed.
- EX4, AR-C and TH re-derive the values at run time.

**Rename.** The scripts' header docstrings changed from "PE-02" to "PE-05" with the rename (O8), so the `.py` digests
below are the renamed files. Their outputs are unchanged, and replay byte-identically from the new path.

**Replay for revision 3.** All four were run with `python3 -I` (local Python 3.13; standard library only). The two
committed outputs are byte-identical on rerun (`cmp`). The two new scripts were run twice, and each output is
byte-identical to the first run.

| File | sha256 |
|---|---|
| `design/least_primitive.py` | `202787c91d849a15f5648ecfd4c40a3b2622f515cbc2365d9882eac9e162b2b6` |
| `design/least_primitive.out` | `f4c880f48bc0d0c132f226546e7d8feaa301297f57ea1e87b243949339fac5ec` |
| `design/charge_arith.py` | `33422c019a3d7e297d21f7d4b99e2c7e06e298620522b16f89349de03befd997` |
| `design/charge_arith.out` | `51aa19de3e0521a26fffe6890e53e41140ecd684630d54f4a0a03e6f86fe67ea` |
| `design/charge_ranges.py` | `895c197d885e82831a7644ba1982f00ac87f642269ab51c983111ea4b8991c87` |
| `design/charge_ranges.out` | `e2359f73fb8ca987180a645590e4601bbc8b6ab12e5204d55b29a03e75f13ff6` |
| `design/linear_class_code.py` | `b70cf1d6518cf1e1102af30fbbe10d41046b3149d08c59cdae191851c7db8c0a` |
| `design/linear_class_code.out` | `895da4bc4a78f5e26fe3b1f5c28a4cda43073c4c8b316e55975a8da97769e795` |

**D1. The polynomial rule.** `least_primitive.py 24` finds the least primitive polynomial of each degree by integer
value. It tests $z^{2^n-1} = 1$ and $z^{(2^n-1)/q} \ne 1$ for every prime $q \mid 2^n - 1$.
- It prints `RULE_REPRODUCES_PE01 True`: the rule gives PE-01's $p_n$ and $p'_n$ for $n = 3..8$.
- Its values for $n = 9..24$ are `PLAN.md` §1.1's table. Every reciprocal is primitive.

**D2. The footprint arithmetic.** `charge_arith.py` evaluates the §2.1 formulas.
- PE-01's witness: $F_U = 6$, $F_R = 37$, $F_E = 34$.
- Least $n$ with $n + 1 \ge F_C$ at $K = 4$: for $m = 0$, R 9 and E 11; for $m = 1$, R 17 and E 18; for $m = 2$,
  R 36 and E 31.
- Largest $K$ with $F_C \le n + 1$ (window floor ignored), for $n = 9..24$:

| Model, $m$ | $n = 9$ | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R, 0 | 7 | 7 | 15 | 15 | 31 | 31 | 63 | 63 | 127 | 127 | 255 | 255 | 511 | 511 | 1023 | 1023 |
| R, 1 | – | – | – | – | 1 | 1 | 3 | 3 | 7 | 7 | 15 | 15 | 31 | 31 | 63 | 63 |
| E, 0 | 2 | 3 | 6 | 6 | 7 | 14 | 14 | 15 | 30 | 30 | 31 | 62 | 62 | 63 | 126 | 126 |
| E, 1 | – | – | – | – | – | 1 | 2 | 2 | 3 | 6 | 6 | 7 | 14 | 14 | 15 | 30 |

Values below 4 admit no window. $m = 2$ is empty under both models throughout. At $n \le 8$ every charged entry is
empty or below 4. The $m = 1$ rows are the per-$n$ values of the `pe02-parameters` block.

**D3. Ranges per n, both θ values, both charge scopes (N1, N3).** `charge_ranges.py` evaluates §2.1's footprints at
θ = n+1 and n+2, for the full description and for the transition-and-action component sums, under R and E, for
m = 0..4 and n = 3..24. It prints the largest admissible K per n, the least n with a K ≥ 4 range, the per-n m = 1
values the parameters block carries, and every cell at n ≤ 8 with a non-empty range.
- **Full description at θ = n+2** (`G_clkfix_u`): m = 1 R from n = 16 (K ≤ 7), E from n = 17 (K ≤ 6); K ≤ 127 (R) and
  ≤ 30 (E) at n = 24. These agree with the re-review's `r2_checks.out`.
- **At n ≤ 8 with the full description,** the only non-empty range is `G_clkfix_u` at θ = n+2, n = 8, m = 0, R,
  K = 4..7 (N1).
- **Transition and action only (O10's alternative)** at θ = n+1: m = 1 from n = 8 (E sum) and n = 10 (R); m = 2 from
  n = 19 (E sum). At θ = n+2, m = 1 from n = 7 (E sum) and m = 2 from n = 18 (E sum) and n = 24 (R).

**D4. The linear-filter class code (O3).** `linear_class_code.py` counts $|\mathrm{GL}(m,2)|$ by enumeration (1, 6,
168, 20160, each matching the product formula) and evaluates the code of `PLAN.md` §2.2.
- At θ = n+1, `plin_m2` is admissible at n = 22, 23 (K = 4..6) and n = 24 (K = 4..7). This agrees with the
  re-review.
- `plin_m1` is admissible from n = 16 (K = 4..6), up to K ≤ 31 at n = 24.
- `plin_m3` and `plin_m4` are empty for n ≤ 24.
- The drafter's addition to the re-review's statement: under a class-code model, `plin_m1` at n = 16 would also need
  searching, one n below `emb_m1_all`'s R onset.

## 5. Coordination with NP-AVG-1

- NP-AVG-1 (#929) declares one background prior, i.i.d. fair on every non-source initial variable, as a named,
  supplied assumption. It owns any convention about averaging over backgrounds.
- PE-05 adopts no background-prior convention. Its priors are the stated laws of finite toy generators:
  - $\mu$ uniform on $\mathcal{C}_V \times \mathcal{C}_H$, i.e. i.i.d. fair bits, as in PE-01 and consistent with
    NP-AVG-1;
  - `G_clkfix_u`: i.i.d. fair, also consistent;
  - device priors, each declared for one generator and not proposed as conventions for any other thread: the
    `G_clkfix` matched prior ($q_0 = x_0$), used for one comparison, and the `G_weak` prior ($x_0 = 0$), used for one
    control.
  - If the owner sees a conflict, O5's "uniform only" removes the first. The planted control can move to a uniform
    prior with a different weak generator.
- PE-05 does not depend on any NP-AVG-1 outcome, and it stays meaningful if NP-AVG-1 finds no masking advantage
  (owner, #934). NP-AVG-1's geometry results may refine PE-05 only through a PE-05 amendment before freeze.
- PE-05 uses none of NP-AVG-1's terms: no "background", "pad", "freshness" or "cone".

## 6. Owner decisions, with recommendations

**Decided.** The owner (amaybaum, 2026-10-26) approved all eleven decisions as recommended: "I approve all eleven PE-02
decisions (O1–O10, including O4b) as recommended, subject to the final nit confirmation and exact-version checks before
freezing the plan." The rulings are recorded in `PLAN.md` §9 and in the parameters block's `decisions`. The approval
"authorizes specification freeze, not experimental execution".

**O8 applied: PE-05.** The owner (amaybaum, 2026-10-26): "Approved: rename the new stage to PE-05. PE-04 remains reserved for quantum reconstruction." The stage was
renamed from its working name PE-02, and its directory moved from `pe02_charged_tables_v1/` to
`pe05_charged_tables_v1/`. PE-04 had been found taken by the README's quantum-reconstruction stage.

The record below keeps each item's recommendation as it was put to the owner; the drafter agrees unless stated.

- **O1, θ under charged models.** Recommended: option (i), $\theta = n + 1$ for U, R and E.
  - **Correction of revision 1.** Revision 1 said that option (ii), $\theta = n + 1 + D_C(\varphi)$, "admits almost
    nothing" under a polynomial code. That was wrong. Any $D_C \ge 0$ makes (ii) admit a superset of what (i) admits.
    Option (i) is the most stringent rule considered, and so the most favourable to the claim under audit.
  - Its hard-to-vary property comes from fixing θ independently of the charge, not from any defect of (ii). Under (ii)
    the verdict moves with the choice of generator encoding, which is the remaining reason to prefer (i).
  - Revision 2 reports each witness's $F_C$ components and each cell's minimum $F_C$, so that a reader can apply
    another θ without a re-run (R6).
- **O2, which charged models govern.** Recommended: R and E, each reported separately. In scope, E ⊆ R (INC-RE), so E
  can only make a verdict stricter, and no E-only witness can arise.
- **O3, description-complexity proxy.** Recommended: information only. The review adds that this rests on E alone. Its
  linear-filter class-code arithmetic is now a checked design fact (D4). Under a class-code model, `plin_m2` would
  need searching at n = 22..24, K = 4..7, and `plin_m1` at n = 16.
- **O4, $N_{\max}$.** Recommended: 24, with the no-extension clause (`PLAN.md` §3.4).
  - At $N_{\max} = 8$ the main question is answered by arithmetic alone, which restates PE-01's REPORT.
  - $m = 1$ enters the charged region only from $n = 17$ (R) or $18$ (E).
  - The $m = 0$ cut is a separate decision, O4b.
- **O4b (new), $m = 0$ in Part B.** Recommended (review and drafter): option (a), the M0 control only, with
  $1 \le K \le 63$ at each Part B $n$, and coverage beyond resting on the M0 proof, which the verdict states. Revision
  2's body applied this as a default while labelling it "done in revision 2". Revision 3 makes it an `OPEN` placeholder
  like the others; the body keeps option (a) as drafted, and the dependent value `M0_K_max_partB` is tagged
  `O4b:a`.
- **O5, clock-ablated prior and θ for `G_clkfix_u`.** Recommended: the matched prior as primary, with the uniform prior
  as a reported variant.
  - θ for `G_clkfix_u`: the review recommends $n + 2$ as governing, which is PE-01's $\log_2|\mathcal{C}|$ and
    $\log_2|\mathrm{supp}\,\mu|$, with $n + 1$ also reported. Revision 1 used $n + 1$, in the favourable direction.
    Revisions 2 and 3 report both and leave the governing value to the owner. From revision 3, `G_clkfix_u` is
    searched over its region at n+2 whichever value governs (N1).
- **O6, K0 status beyond $n = 8$.** Recommended: not computed.
- **O7, the secondary population.** Recommended: all active (a′)–(e) members, with their known extent ($m = 2$,
  $n \in \{4, 5\}$) stated in advance (`PLAN.md` §4.3).
- **O8, the stage name.** The review recommends renaming this stage to PE-04 and retitling #934 and this directory
  before freeze. PE-01's frozen PLAN binds "PE-02" to the computational-versus-physical stage, and frozen text cannot
  change. Revision 2 keeps "PE-02" with a placeholder note, at the coordinator's instruction. The drafter agrees that
  renaming is cleaner while nothing is frozen. **Ruling:** PE-05 (above); PE-04 was found taken.
- **O9, Lemma A-SIM.** Recommended: adopt, with the review's added bijectivity step (applied in revision 2).
  - It gives PE-01's target T2 an upper bound, $m' \le m + 1$, on autonomous generators.
  - Minimality is open, and the review's toy cases show $m' = m$ does not suffice in general. Revision 1's NOTES said
    the lemma "turns T2 into a one-line statement", which overstated it.
- **O10, charge scope.** Recommended by the review: the full description ($\rho$, $a$, readout, $K$) governs, with
  the reason stated: an interpreter needs the readout and the trigger. Every witness reports components and the
  component sum $F_C^{\rm TA}$, so that #934's literal transition-and-action charge can be read.
  - Choosing transition and action only would change every charged range (D3), add `emb_m2_all` to Part B from
    n = 19, make Part A's charged cells non-empty, and break INC-RE.
  - Every dependent value would then have to be restated (`PLAN.md` §9, TH).

## 7. Ambiguities in #934

- **A1. The stage label.** #934's working label PE-02 collided with the README's PE-02 (computational versus
  physical observers). Resolved by O8: this stage is PE-05.
- **A2. The outcome classes mix two kinds of label and are not exhaustive.**
  - `SURVIVES_CHARGED`, `UNCHARGED_ONLY` and `NO_WITNESS_IN_SCOPE` compare accounting models within one activity
    level. `ACTIVE_ONLY` compares activity levels within one model.
  - The plan keeps all four in two families and adds `PASSIVE_ALSO`, `PASSIVE_ONLY`, `NEITHER` and `INCOMPLETE`, plus
    a `structural`/`searched` sub-label on `UNCHARGED_ONLY`. The review agrees.
- **A3. "Per factor combination."** Accounting is the outcome axis. Revision 2 computes every factor outcome per $n$,
  so that U-witnesses and C-cells are never compared across different $n$ (R8).
- **A4. "A positive result under a charged model does not establish ch18's untested narrower claim."** "Positive"
  could mean either outcome. Nothing in PE-05 establishes the narrower claim under either reading (`PLAN.md` §7).
- **A5. "The same tables with interventions disabled."** It could mean $a \equiv 0$, or actions that still enter the
  record but no longer reach the generator. The second is the `G_clkfix` comparison, so both readings are covered.
- **A6. "PE-05 does not re-run" PE-01, against "a byte-identical replay".** The replay is read as a one-shard control.
  PE-01 cells are recomputed only for the secondary population and UX.
- **A7. θ for the ablated generators.** It is settled by the support rule (§1.2): $n + 1$ for `G_clkfix`, and both
  values for `G_clkfix_u` (O5).
- **A8. C2–C4** are not asked for and stay unchecked.
- **A9 (new). "Transition and action tables"** against the full description (O10).

## 8. Assumption-watch markers (§A.31)

- **M1. "Bounded memory" and the program.**
  - In finite-state prediction and bounded-memory learning (Feder–Merhav–Gutman; Raz), the resource is states or bits
    of state, and the transition function is not charged. PE-01's uncharged convention is that standard one.
  - `Main.md:560` charges a program register for its own construction.
  - The scoped ch18 sentence says "observers of bounded memory" without fixing which convention it means. PE-05
    measures what turns on that choice. Any wording change is a separate owner decision.
- **M2. Activity on autonomous generators** is worth at most one memory bit (A-SIM, an upper bound). PE-01's REPORT ties
  its witness to "an active observer and G_clk's backaction". On autonomous generators the activity half of that
  attribution reduces to footprint; the clock ablation tests the backaction half.
- **M3. Structural emptiness and proved zeros look like negatives.** Every charged region at $n \le 8$, every $m \ge 2$
  region in scope, and every $m = 0$ cell are empty or zero by arithmetic or proof. The labels keep these apart from
  "searched, none found".
- **M4. Choices that lean toward the favourable reading** are printed beside the outcomes they affect (`PLAN.md` §6
  item 9):
  - θ option (i);
  - the full-description charge (O10);
  - the fixed clock charge, which may overcharge an observer whose memory already keeps time (PE-01 plan review A2);
  - for `G_clkfix_u`, θ = n + 1 if the owner chooses it.
- **M5. (c) does not bind in Part B.** At θ = n + 1, (f) implies (c) for every admissible cell (PE-01 code review R3).
  In Part B, $K^{C}_{\max} \ll K_{\rm cx}$ for `G_lin` and `G_filt`. AR-C still measures $K_{\rm cx}$.
- **M7 (new in revision 3). A reported parameter can silently narrow a search.**
  - Revision 2 reported `G_clkfix_u` at θ = n+2 but computed its search range at n+1 (N1).
  - Its dependent values were also computed under the recommended options with nothing tying them to those options
    (N3).
  - The marker: every reported θ needs its own searched range, and every computed value names the decisions it
    assumes.
  - In the same pass the drafter found one more instance and fixed it: `emb_m3_passive`'s Part A caps for
    `G_clkfix_u`, raised to the θ = n+2 region (31 at n = 7, 63 at n = 8).
- **M6. Z was load-bearing in revision 1.** Revision 1's Part B started at $Z + 4$ and computed Z by a method that
  is invalid for `G_clkfix`. Revision 2 starts at $K = 4$, from the $K' = 0$ zero alone, and uses Z only as a
  cross-check. The general marker: a search bound derived from a quantity is only as sound as that quantity's
  computation.

## 9. What PE-05 would add beyond the two covered-in-kind results

The owner asked (#934) what a PE-05 plan adds beyond the 2006 clock-control fault attack and AGHP's mechanism.
- **The fault attack** reruns a separately clocked generator from one state, with unbounded computation, and recovers
  state. PE-05 asks a resource question that work does not pose: does a within-trajectory prediction witness survive
  when the observer pays for its own description, and does its advantage need the clock to respond?
- **AGHP** fixes when passive linear statistics are exactly unbiased. PE-05 asks whether passive observers of any
  accounted size gain on these generators, including on `G_clkfix`, where AGHP does not apply.
- Neither question is claimed new before the A3-rule reading of `PLAN.md` §11.

## 10. Not done

- No PE-05 code. No simulation. No computation of any advantage, window, $Z(\varphi)$ or $K_{\rm cx}$. No PE-01 cell
  recomputed.
- No literature read for PE-05 beyond what PE-01's annex records.
- The owner's decisions are recorded. Freeze still needs: the identifier for O8 confirmed and the rename applied; the
  owner's other freeze conditions (nit confirmation, coverage of every option-dependent control by TH, exact-version
  checks); and an independent confirmation, with the freeze SHA recorded by the coordinator.
