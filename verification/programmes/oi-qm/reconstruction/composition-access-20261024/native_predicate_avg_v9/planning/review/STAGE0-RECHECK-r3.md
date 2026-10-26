# Re-check: NP-AVG-1 Stage 0 r3, the Layer-1 specification

**Reviewed.**
- `stage0/r3/STAGE0-PLAN-r3.md` (SHA-256 `683acdf4…c32c`, 892 lines) and
  `STAGE0-CHANGES-r3.md` (`d2083148…7e8c`), on PR #935 at `72c56ca0`.
- `stage0/code-r3/` (all eight files, read in full) and `stage0/design-r3/` with `runs/` and
  `RUN-MANIFEST`. The file hashes equal the manifest.
- Context: `STAGE0-REVIEW.md` (r1 review, R1–R9), `STAGE0-RECHECK-r2.md` (R1–R6, S11),
  `STAGE0-PLAN.md` (r1) and `r2/`, and `native_predicate_v8/REPORT.md`.

**Read-only.** Nothing was edited, committed or pushed. Nothing ran on v8's configuration class.
My re-runs and probes are in `S/npavg/review-r3/{rerun,probe}/`. I used `python3 -I -B` (and
`-O`) on Python 3.13.16, with the committed code and no modification. The probes ran on a
*copy* of the code with added mutants.

## Verdict: ACCEPT WITH CHANGES (Layer 1 not ready to freeze as written)

**What is ready.**
- The masking law, geometry, conventions, cone radii and tips are correct.
- The search domain and its counts are correct.
- The two-layer structure carries the owner's O1 faithfully.
- R1–R9 (r1 review) and R1–R6 (r2 re-check) are applied. One exception: r2 dropped r1's precise
  proof-obligation statements, and r3 inherits the loss (RC2).
- Every cheap control replays byte for byte.
- C11 is a real and useful control. My own over-elimination mutant in a single direction is caught
  by C11 (i) and by nothing else.

**What blocks a freeze as written.** Every item is a bounded text edit. None changes the rule, the
domain or the question.
- **The decision rule is ambiguous.** Several MISMATCH conditions are also failures of required
  controls, and "first match" sends those to VOID (RC1).
- **The frozen text uses objects it does not define:** P_G-dir, M_F(e) and M_B(e), "e-tip", B8,
  and the aligned direction under ties. It also cuts PO3 and PO5–PO8 down to labels (RC2).
- **C11 does not tie the closure's decisions to its tables.** One single-direction
  over-elimination mutant escapes every control in the design suite (RC6). C11 (ii) is never
  exercised on B type, under G, or on its Φ clause (RC7).

## 1. Reproduction (task 4)

| step | my result | against `runs/` |
| --- | --- | --- |
| `s0controls.py` (full), normal and `-O` | exit 0, `failed: []` | byte-identical (`a0743c03…`); `-O` identical |
| `s0s6.py`, normal and `-O` | exit 0; JSON carries `"label": "proof-check of PO8; not a result"` | byte-identical (`0f0bca68…`); `-O` identical |
| `s0symcheck.py`, normal and `-O` | 3,225 items; 5,160,000 pairs; orbits 875 and 815,175, direct = Burnside; orders 48 and 8; A001845 holds | byte-identical (`76779524…`); `-O` identical |
| `rerun.py`, `planted.py`, `radius_mutants.py`, `exact_small.py`, normal and `-O` | exit 0 | all four byte-identical; `-O` identical; `rerun.py`'s timing goes to stderr only |
| `s0mutants.py` (QUICK) | exit 0, 9 m 59 s | byte-identical (`9c793906…`) |
| `s0mutants.py --full` | not run, as instructed (§A.40) | assessed from `runs/mutants_full.out` below |

**The full campaign, from `runs/`.**
- Exit 0, and the frozen rule is clean.
- Every non-equivalent mutant hits a named catcher, and the failed-control sets equal the quick
  campaign's.
- `direction_demo` passes with 7,804 table mismatches, 3 P_A-dir violations and 0 aggregate
  violations, and no aggregate control fails.
- The equivalent mutants fail no control (parity) and only C1 (symmetric radii).
- The bracketed "observed failures" in §6's mutant table match both runs.

**The v8 guard.** I constructed contexts only and ran no closure
(`probe/guard_probe.{py,out}`).

| call | result |
| --- | --- |
| `Context(V8, A)`, `Context(V8, G)`, `num_records(V8)`, `record_at(V8, 0)`, `record_samples(V8, ())` | all five refused |
| a fresh `Setup(3, 6, 4, 23, (0, 0, −3), V8.sources)` with v8's parameters (flag unset), passed to `num_records`, `record_at` and `Context` | **not refused** |
| `s0ref.ref_context` with v8's parameters | **not refused** (no guard at all) |
| setting `V8.v8 = False` and then calling `Context(V8, …)` | **not refused** |

The guard is keyed on a mutable flag on one object, not on the configuration. That is adequate
for design evidence, where no code passes v8's parameters, but the plan's "refuses v8's setup" is
true only of that object. Layer 2 must key the refusal on content (RC9).

## 2. Freeze-readiness of Layer 1 (task 1)

### 2.1 Mathematics: checked, correct

**Cones and tips.** For x_t = x_{t−2} ⊕ H(⊕_e x_{t−1}(·+e)), with an F quantity at depth d:
- its dependence on slice L lies within d (parity d), and on slice E within d − 1;
- the near axis tips c ± d e, and the far tips c ± (d − 1) e for d ≥ 1, are bijective.

The far-tip proof in §2 is right. B type is the mirror image, and G is F type from (−1, 0). C1
and C2 confirm this natively at every depth used.

**Parity.** For even (c, t) and an even cell (u, s) on the far slice, |u − c| ≡ d − 1. So radius d
and radius d − 1 select the same even cells, and the "symmetric radii" mutant is correctly declared
equivalent.

**L3′ ⊆ L3, and C9's global bound.** A set that is self-supporting under L3′ is self-supporting
under L3. The closure equals the greatest self-supporting subset, which is monotone in the
context, because G-eligibility depends only on the frame.

**P_A and P_A-dir.** Both hold as necessary conditions. For an F element at the top reach r in
direction e, a B cover needs B reach ≥ r + 1 on slice 8 (radius d − 1). A same-type cover forces
the same tip at equal reach. Under A, the only fixed covers are Φ's seven site-times; p's cone is
exactly the six slice-7 Φ cells plus V's cell. The aligned near tip of a non-fixed quantity is
never a Φ site-time, since |c|₁ + d = 1 forces p or Φ. So P_A needs no Φ clause, and P_A-dir
does need one.

**P_G-dir as coded** (`s0ref.pa_dir_violations` with G's eligibility) is also a correct necessary
condition. An eligible e-tip of a top S_G element can be covered only by an F quantity of reach
≥ r, which then has a seed tip and lies in S_G. Ineligible tips are exempt. But **the plan never
states P_G-dir** (RC2).

**Base precondition (§3).** I checked it by hand:
- Under A: N[1]'s −z tip (0, 0, −9)₇ is free, then N[3]'s (0, 0, −7)₇. N[5]'s −z tip
  (0, 0, −5)₇ is covered by N[1] and N[3] only while they are alive.
- Under G: |c| + t ≤ 3 + 5 = 8.

The derivation is right.

**C_G's inheritance.** v8 states its negative "for every R, stream-closed or not" and on the zero
background (REPORT.md:19-21, 37), which covers truncated records.

### 2.2 The decision rule is not unambiguous (RC1)

§5 says "precedence, first match", and VOID is "a required control (§6) fails". But the
following are §6 required controls whose failure §5 also lists under MISMATCH:
- C11 (ii);
- C6 (the hand derivation at execution);
- C9 (both bullets: L3′ ⊄ L3, and outside the global bound);
- C12 (an in-frame cone leaves the frame).

Read literally, they can never produce MISMATCH. §6 C11 itself says (ii) gives MISMATCH. Two
implementers would label the same run differently.

**The C0–C18 range.** COLLAPSE_ALL also cites "controls C0–C18 green", and C4 and C5 do not exist.

### 2.3 Undefined or under-specified frozen objects (RC2–RC5)

**Propositions and proof obligations.**
- **P_A-dir:** M_F(e), M_B(e) and "e-tip" are not defined.
- **P_G-dir:** not stated anywhere, though §4, §5 and C11 use it.
- **Aligned direction:** r1 defined it, including the c = 0 case; r3 dropped the definition. Ties
  in ‖c‖_∞ give several aligned directions, and the code checks all of them.
- **The PO table:** r2 shortened r1's exact PO statements to labels, and r3 inherits them. "PO6:
  Unlinked survivors are independent" no longer says of what, or under which conditioning.
  RESIDUE_UNLINKED's G clause rests on exactly that: r1 had "independent of G given the frame".
- **B8:** used in §2, §3, C3 and C12, never defined in r3. r1 defined it as V's cone in (−1, 0):
  slice 0, even, |c| ≤ 8; slice −1, odd, |c| ≤ 7.
- **PO8's three cases:** not listed. S6 checks them, so they belong in the frozen text.

**Eligibility scope.** "A tip is eligible only if it is a seed" follows the G paragraph. It does
not say that every tip is eligible under A. It also does not say that the frame uses the G cones
on slices −1 and 0.

**L3.** "Near-only L3" does not say that the cones are unchanged. The code drops the far tips and
keeps the far cones.

**E3.** E3 says same-site pairs are "excluded", under a header that says "none excludes a record".
Same-site pairs are redundant: their context equals that of the single item (x, max t). Say so;
otherwise this reads as an exclusion.

**(b), the private dependence set.** As written, "Φ cells inside the cones of the retained public
part" is trivial, because the public part always contains p, whose cone contains all six slice-7 Φ
cells. The code means something else: the cones of the *non-fixed* public quantities, plus the Φ
cells in clear (`analyse`). Under G, "Φ cells inside cones" is empty by construction, and only
source cells are computed.

**The (q9, 9) hand instance.** C6 promises it is "derived by hand before their computed values
are read", but the plan does not contain it. Only the frozen text can show that the derivation
came first. My derivation is in RC8.

### 2.4 Search domain, coverage and outcome-independence

The search domain and coverage limits are exact:
- ball(4) has 129 sites;
- t runs over −1..23;
- k ≤ 2 at distinct sites, giving 3,225 + 5,160,000 records;
- the S1a bound is defined, with S1b and S1c deferred;
- §11 states the coverage limits.

I found no outcome-dependent acceptance choice. BASE_RESIDUE is a preregistered alternative.

**S1b and S1c.** "Taking either up depends on S1a's result" is a decision about a further search,
not about acceptance. Its trigger is still not preregistered (owner item O-b).

**The S1a axis lines.** "Each axis line's items" does not say which lines (nit N5).

### 2.5 The §A.41 table

Every row names a checkpoint. Two rows rest on design evidence that does not do what the row
claims:
- **"Every reported count" (C8).** The 44 compared counts omit observer classes among collapsed
  records and the counts of (b). §3 requires both, and §6 C8 names "the counts of (b)" (RC10).
- **"The per-direction control detects …" (C11 non-vacuity).** See §4. The demonstration is real
  but narrow (RC7).

## 3. R1–R9 and S11 (task 2)

There are two R-series, and the plan uses both without saying which (nit N2).

**r1 review R1–R9.**

| item | status |
| --- | --- |
| R1, C15 | applied (C15, with stated coverage) |
| R2, mutant list | applied |
| R3, planted families | applied at full depths |
| R4, parity re-run | applied |
| R5, C8 invariant-only | applied; source-dependent attributes are per record |
| R6, (a)–(c) | applied; (b)'s wording is defective (RC5) |
| R7, COLLAPSE_ALL wording | applied; "C0–C18" names nonexistent controls (RC1) |
| R8, base precondition | applied |
| R9, §A.41 rows and the witness order | applied (C16) |

The r1 PO statements that this review accepted were later truncated, which is a regression (RC2).

**r2 re-check R1–R6 and S11.**

| item | status |
| --- | --- |
| R1 | superseded by the owner's O1, and applied as O1 |
| R2 | applied: C1 and C2 at A F 0–15, B 0–8 and G F 0–23 plus B 0; C3 at full depths; the interior-sampling limit is stated |
| R3 | **partly** applied: 44 counts, but not observer classes among collapsed records or the (b) counts (RC10) |
| R4 | applied: C10 (ii), the docstring, the S6 label |
| R5 | applied: every stdout and stderr is retained; `rerun.py` timing goes to stderr |
| R6 | applied |
| S11 | adopted as a required control (C11) |

## 4. C11, the required per-direction control (task 3)

**Is it well defined?** Mostly, but:
- "at the same state" is not defined. The code reconstructs it as the initial context minus the
  earlier log entries, in log order.
- Nothing requires the closure's *decision* to agree with its own table.

**The authors' demonstration** (−y blind, chosen in advance). I reproduced it from QUICK: 1,672
table mismatches, 3 P_A-dir violations, 0 aggregate violations, no other control failing, and all
44 counts unchanged. It is real, but narrower than presented:
- **Part (i) is close to tautological.** The mutant overrides exactly the status field that C11 (i)
  compares.
- **Part (ii) depends on the plant direction.** It fires only because C11 (ii)'s planted sets
  include "family minus its −y tip". C3 drops only +x, which is why no other control sees it.
- **It is over-retention.** That is the direction MISMATCH already guards in principle.
- **"Aggregate counts unchanged" is near-vacuous on the toy class.** The toy class has no
  survivors under A or G. 24 of the 44 counts are identically 0 (every survivor-conditioned count,
  plus the L3/L3′ disagreements). The other 20 depend only on in-clear sets, truncated sets and
  record geometry. No over-eliminating mutant can change them on this class.

**My mutants** (chosen before running; `probe/make_mutants.py`, `probe/probe_quick.json`; QUICK
mode, toys and planted sets only):

| mutant | kind | C11 (i) | C11 (ii) | other controls failed | 44 counts |
| --- | --- | --- | --- | --- | --- |
| `rv_dir_ignore_fixed`: −y tips ignore cover by fixed quantities | single-direction **over-elimination** | **81 mismatches** | 0 | **none** | unchanged |
| `rv_dir_swap`: ±y tip labels swapped | direction swap (labelling) | 477 | 0 | none | unchanged |
| `rv_dir_wrong_far_y`: −y far tip at distance d | over-elimination | 1,464 | 0 | C2, C3, C7, C18 | changed |
| `rv_dir_cone_y`: −y boundary shell dropped from cones | under-coverage | 735 | 0 | C1, C3, C15, C18 | not compared (single run) |
| `rv_blind_B_y`: −y blind, B type only | over-retention | 1,402 | **0** | none | unchanged |
| `rv_blind_G_y`: −y blind, under G only | over-retention | 105 | **0** | none | unchanged |
| `rv_blind_plus_z`: +z blind | over-retention | 1,360 | 3 | none | unchanged |
| `rv_decide_blind_y`: decision ignores free −y tips; table truthful | over-retention | **0** | 3 | none | unchanged |
| `rv_decide_ignore_fixed_y`: decision treats Φ-only-covered −y tips as free; table truthful | single-direction **over-elimination** | **0** | 0 | **none: exit 0** | unchanged |

**What the mutants show.**
- **C11 (i) carries weight.** It alone catches a genuine single-direction over-elimination
  (`rv_dir_ignore_fixed`) that leaves every aggregate quantity intact. That satisfies the owner's
  requirement better than the authors' own demonstration.
- **C11 (ii)'s planted sets cover A F type only** (`c11_props`: depths 1–3 at (40, 0, 0)). The
  B-only and G-only blind mutants pass it, and its Φ clause is never exercised.
- **C11 (i) compares tables, not decisions.** The same gap shows in the authors' own
  `unapplied_elimination` run, where C11 (i) passes.
- **One mutant escapes every control.** `rv_decide_ignore_fixed_y` is a collapse-favourable
  decision error, and it passes the whole design suite. On the toy class its effect is always
  masked: every affected quantity also has a genuinely free tip.

**The Φ-adjacent planted family exposes it** (`probe/phi_adjacent.{py,out}`). The family is planted
at B depth 2, q = ((0, 1, 0), E − 2), so its −y near tip is a Φ cell.
- The frozen rule retains all 11 members, and P_A-dir with its Φ clause holds (0 violations).
- `rv_decide_ignore_fixed_y` and `rv_dir_ignore_fixed` eliminate all 11.

So a planted set of this kind closes the gap. Because it also exercises P_A-dir's Φ clause, it
belongs in C3 and C11 (ii).

## 5. The Layer-2 plan (task 5)

As a plan, §5b is adequate:
- it lists the driver, per-record analysis, C11, the witness, S1a, shards and merge, and labels;
- it carries the r2 re-check's fail-closed items 1–8, essentially verbatim, adding C11 (i) on a
  sample;
- it correctly defers the implementation.

Additions required: RC9.
- **The guard is flag-based.** See §1.
- **The pre-flight list omits two controls.**
  - It omits C10 (ii), which is cheap, on v8's frame. It appears neither in the pre-flight list nor
    among the in-run gates.
  - It omits C11's planted-set part and its direction mutants. "C0–C3, C6, C12–C18" skips C11.
- **The mutant campaign's kill criterion.** The plan says a mutant counts "only when it fails on
  its named case", and §A.40 says the same. But `s0mutants.py` checks control names, not cases,
  and it continues after a failed frozen run. Layer 2 must use case-level kills, gated on a clean
  frozen run.
- **§10 misreads §A.40.** It says the 33-minute full campaign and the 50-minute driver are "cheap
  enough to run locally (§A.40)". §A.40 sends mutation campaigns to CI. The local r3 runs stand as
  executor design evidence, and the Layer-2 campaign runs in CI.

## 6. Scope (task 6)

**No over-claim found.** In particular:
- no unpredictability, hardness or quantum reading of counts;
- COLLAPSE_ALL is labelled consistency-axis;
- §8 is cite-not-claim;
- v8 enumeration is stated as unauthorized throughout.

**Under-claim and exclusion.**
- **The three-way classification (a)–(c) is kept.**
- **Counterexamples are reported.**
- **E3's wording reads as an exclusion** (RC4).
- **One degeneracy is vacuous on the toy class.** The toy region ball(1) does not contain the port
  site (0, 0, −2), so "item at the port site" is identically 0 there (nit N7). It is not vacuous
  on v8, where (0, 0, −3) ∈ ball(4).

## Required changes

**RC1. Decision-rule precedence (§5).** Replace the VOID bullet with:
> **VOID:** a required control fails, other than through one of the MISMATCH conditions below.
> These are C6's execution-time hand instances, C9, C10 (ii), C11 (ii) and C12. A run in which
> both a VOID control and a MISMATCH condition fail is VOID.

In COLLAPSE_ALL, replace "controls C0–C18 green" with:
> every required control of §6 (C0–C3, C6–C18, the refusal check, the native self-test and S6)
> green

**RC2. Exact statements (§4).** Restore r1's PO table text for PO3, PO5, PO6, PO7 and PO8
(`STAGE0-PLAN.md` §4), adding the G conditioning to PO4. Insert before P_A:
> For q = (c, t) of type T and depth d, and an axis direction e, the *e-tip* of q is its near tip
> c + d e, and its *reach in e* is c·e + d. For a set S, M_T(e) is the largest reach in e among
> the elements of S of type T (−∞ if there is none). The *aligned directions* of q are the e = ±e_i
> with c_i = ±‖c‖_∞ (all six when c = 0); ρ(q) = ‖c‖_∞ + d.

In P_A and P_G, read "its aligned near tip" as "each of its aligned near tips". Add:
> **P_G-dir.** For every direction e, with S = S_G(R): if M_F(e) ≥ M_B(e), every F element of S at
> reach M_F(e) whose e-tip is eligible has its e-tip shared with another F element of S.
> Symmetrically for B type (slice −1, depth 0). When the reaches are equal, both apply.

Add to §2:
> B8 is V's cone in the pair (−1, 0): the even cells of slice 0 with |c| ≤ 8 and of slice −1 with
> |c| ≤ 7.

**RC3. Eligibility and L3 (§2).** Replace "A tip is eligible only if it is a seed…" with:
> Under A, every tip is eligible. Under G, a tip is eligible iff it is a seed, that is, outside the
> frame. The frame is the union of the G-convention cones (slices −1 and 0) of Φ, V, p and the
> even port samples; its even part is B8 (PO7).

After "Near-only L3 is reported beside L3′", add:
> L3 is L3′ with the far tips removed; cones are unchanged.

**RC4. E3.** Replace the E3 text with:
> **E3, unordered pairs at distinct sites.** A same-site pair {(x, t1), (x, t2)} has the context of
> the single item (x, max(t1, t2)), which is enumerated; it is not a separate record.

**RC5. (b), the private dependence set (§3).** Replace with:
> **(b) Private dependence set.** Under A: the Φ cells (six slice-7 cells and V) in clear, together
> with the private Φ cells inside the cones of the retained non-fixed public quantities (record
> and port samples), split into J cells (q8, q10) and others. Under G: the source cells inside the
> cones of the retained non-fixed public quantities. Computed per record where source-dependent.

**RC6. C11 (i): tie decisions to tables (§6).** Append to C11 (i):
> The state at an elimination is the initial context minus the quantities logged before it, in
> log order. The table must also agree with the decision: the logged tip's label has status
> 'free' in both the closure's and the reference's table; every retained quantity's fixed-point
> table has no 'free' entry. Either failure is **VOID**.

**RC7. C11 (ii) and its non-vacuity (§6, §7).** Replace "These are the families, and each family
minus its near tip in one direction" with:
> These are C3's families for A F, A B and G F (G outside the frame), each family minus its near
> tip in each of the six directions, and a Φ-adjacent family for each type: a family whose near
> tip in one direction is a Φ site-time, so that a fixed quantity is that tip's only other cover.
> The frozen rule must retain the Φ-adjacent families (C3).

Replace the non-vacuity paragraph's pass condition with:
> Non-vacuity is shown by two mutants fixed before the run:
> - a single-direction over-retention mutant (the −y blind);
> - a single-direction over-elimination mutant (−y tips ignore cover by fixed quantities).
>
> Each must fail C11 and leave every other control green. The demonstration also states the
> survivor counts of the class it runs on. Where these are zero, it does not claim that
> "aggregate counts appear correct" beyond those counts.

Update the §7 row to match.

**RC8. C6's (q9, 9), written down now.** Add to §3, after the base derivation:
> **Single item (q9, 9).** Its even samples are q9 at slices 0, 2, 4, 6 and 8. Slices 6 and 8 are
> p and V in clear (E1). Under A, (0, 0)₀, (0, 0)₂ and (0, 0)₄ are B type, at depths 7, 5 and 3.
> Their +x near tips (7, 0, 0)₇, (5, 0, 0)₇ and (3, 0, 0)₇ lie in no other cone once larger cones
> are gone. The port samples go as in the base. So the record is collapsed under A, with p and V
> in clear. Under G, the three samples have |c| + t ≤ 4: they are in-frame and retained, with no
> seed tip. So the record is collapsed under G, with truncated record {q9@0, q9@2, q9@4}.

**RC9. Layer-2 plan (§5b).**

(a) Certificate item 6: append
> The refusal is keyed on configuration content, not on an object flag. Any setup equal to v8's
> parameters is refused by every production, reference and native entry point. The refusal check
> includes a freshly constructed copy of v8's setup.

(b) Item 2: replace "C0–C3, C6, C12–C18" with
> C0–C3, C6, C10 (ii), C11 (planted sets and both direction mutants), C12–C18

(c) Item 3: append
> Each mutant names its case and counts as killed only when that check fails cleanly on that case
> (§A.40). Mutants run only after the unmodified suite has passed. The campaign runs in CI.

(d) §10: replace "The design-evidence checks are cheap enough to run locally (§A.40): …" with
> The r3 design evidence was run locally as executor evidence: controls about 2 minutes, the quick
> mutant campaign about 10, the full about 33. Under §A.40, the Layer-2 mutant campaign and any
> repeated suite run in CI.

**RC10. A closed list of reported counts (§3, C8).** Add to C8:
> The reported counts are exactly: <the 44 listed>, plus observer classes among collapsed records
> (A and G) and the counts of (b) (J and non-J cells, and source cells under G). Count preservation
> covers every item of this list.

Then either extend the design evidence, or state that the r3 evidence covers 44 of them.

## Nits

- **N1.** Under A, J-linked ⊂ Φ-linked. State the three classes as J-linked; Φ-linked but not
  J-linked; unlinked.
- **N2.** Disambiguate "R3", "R5" and so on: "review R3" (r1) or "re-check R3" (r2). §12's
  "R1–R9: applied" mixes the two series.
- **N3.** The paths `npavg/stage0-code-r3/` and `npavg/stage0-design-r3/` are scratch paths. The
  repository paths are `stage0/code-r3/` and `stage0/design-r3/`, and the manifest's commands
  should use them too.
- **N4.** `s0symcheck.py`'s docstring still says "carried into the frozen layer". C1 samples 1,000
  interior cells per depth on both slices, which is 2,000 perturbations; say so.
- **N5.** S1a: say which axis lines are meant, either "every axis-parallel line meeting Reg" or
  "the three coordinate axes through q9". Say what the per-line closures are used for: reported
  only, or as a C9 bound.
- **N6.** The sampling rules ("deterministic 1-in-1,000" and "1-in-100 of orbits") should be
  Layer-2 configuration constants under certificate item 1. Say so in C7 and C8.
- **N7.** The toy region does not contain the port site, so that degeneracy count is vacuous in
  the design evidence.
- **N8.** `pa_aligned_violations` accepts "ineligible" and "Φ-covered" exits, which P_A does not
  state. They are unreachable under A, by PO5, but the checker is then weaker than the
  proposition. Either drop them or state them.
- **N9.** §6's mutant table and `s0mutants.EXPECT` name different catchers, for example for
  near-only. Make one the source of the other.

## Owner decisions

- **O-a.** Accept RC1–RC10 as text edits to the Layer-1 object, and then freeze it. Re-review
  should be limited to the diff.
- **O-b.** Preregister, before S1a is read, the criterion under which S1b or S1c would be taken up.
  The other option is to state that any such search is a new preregistration.
- **O-c.** RESIDUE_UNLINKED's G clause rests on PO6-G ("independent of G given the frame"). Keep it
  with PO6-G restored, as RC2 does, or route G-unlinked survivors to RESIDUE until PO6-G's written
  proof exists. I recommend keeping it, with the PO restored.
- **O-d.** Whether RC7's extra planted sets and second direction mutant are run as design evidence
  now, which costs minutes, or first in Layer 2's pre-flight. Either keeps the v8 class untouched.
- **Unchanged:**
  - the v8 enumeration is not authorized;
  - Layer 2 follows Layer 1's independent review;
  - S2, S3, S5, S7, S8 and S10 are accepted as proposed.
