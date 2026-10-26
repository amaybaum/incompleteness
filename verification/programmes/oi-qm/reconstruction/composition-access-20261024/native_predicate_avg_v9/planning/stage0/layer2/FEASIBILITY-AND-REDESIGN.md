# NP-AVG-1 Stage 0, Layer 2: feasibility under the 24-hour ceiling, and revised designs (advisory)

**Status: advisory, for the owner. It sets nothing, changes no file and adopts no design.** It
answers the owner's request of 2026-10-26 (amaybaum) to "clearly distinguish: the statistically
justified κ estimate from the computationally affordable κ; the proposed survivor cap and its
scientific justification; the measured calibration costs from the unmeasured overhead assumptions;
whether the 24-hour ceiling can accommodate the scientifically justified configuration. If it cannot,
propose a revised experimental design rather than reducing κ to make the run fit."

**It reads Layer 2 r4 as pushed at `4a4d8bc1`.** Every measured number comes from the retained
design evidence of that revision: `design/kappa/calibration-repeats.json`, `design/overhead/overhead.json`,
`design/overhead/survivor-cap.json`, `design/runs/dryrun_v8_estimate.out`, `design/toyrun/dryrun.json` and
`design/RUN-MANIFEST.json`. **Nothing ran on v8's configuration class.** v8 enters only through the
dry run's combinatorics: counts and the context-size histogram, with no context and no closure.

**Labels used below:**
- **measured:** read from a retained run, with its file;
- **assumed:** a model form, an extrapolation or a stated allowance, with whose it is;
- **judged:** an explicit judgement, with whose it is;
- **unknown:** not computable without a v8 computation that is not authorized, or not yet measured.

## 1. κ: the statistically justified estimate, and the affordable κ

### 1a. The statistically justified κ (the owner's approved method)

κ = u_cal × u_model, rounded up to one decimal ("Approve the proposed method, κ = u_cal × u_model,
but not a final numerical value").

**u_cal**, *measured locally, not yet on the runner class.* It is the 99th percentile of the ratio
between two independent calibrations (`LAYER2-R3-REVIEW.md` §6). `kappa_calibration.py` computes it
over all 90 ordered pairs of 10 local calibrations (5 normal, 5 `-O`, each in a fresh process), on the
known terms of the v8 estimate.

| local repeat of the 10-calibration procedure | σ of the log estimate | normal-approximation p99, exp(2.326 · √2 · σ) | empirical p99 (= max/min) | source |
| --- | --- | --- | --- | --- |
| r3 | 0.06 | 1.22 | 1.21 | the review's re-read of `47cf942d`'s `calibration-repeats.json` |
| r4, interim run | 0.082 | 1.31 | 1.29 | not retained: overwritten by the final run |
| r4, final run | 0.091 | 1.35 | 1.37 | `design/kappa/calibration-repeats.json` at `4a4d8bc1` |

**Instability.** The same procedure on the same machine gives 1.21 to 1.37. At n = 10 the 99th
percentile of a ratio is estimated from its extreme pairs, so it moves with one slow calibration
(the final run's slowest is 1.30 × the median). **The statistic is not yet fit to fix u_cal.**

**Still to come.** The owner requires "at least 20 independent timing calibrations on the relevant CI
runner class". The workflow is proposed (`ci/`), not reviewed and not launched. Between-runner
variance, which local repeats cannot see, is unmeasured.

**u_model**, *judged* (the owner: "an explicitly judgment-based factor, subject to sensitivity
analysis"). It has no value. Its range in the sensitivity analysis is 1.0–1.5.

**What the statistics support now.** The rule cannot give κ below 1.3, since u_cal ≥ 1.21 measured
and u_model ≥ 1.0. Across u_cal ∈ {1.25, 1.35} and u_model ∈ [1.0, 1.5], κ runs from 1.3 to 2.1. At
the review's provisional pair (1.25, 1.25), κ = 1.6. None of these is proposed as the value.

### 1b. The computationally affordable κ (a diagnostic, never a candidate)

κ_aff is the largest κ for which the configuration of §2 fits the ceiling with the reserve:

κ_aff = (86,400 − reserve) / total.

It is reported only to show how far the configuration is from fitting. **It is not a candidate for
κ:** choosing it would be the "artificially smaller margin" the owner ruled out.

| inputs (C7 sets 2 and 3 taken as 0, their least possible value) | total (s) | κ_aff |
| --- | --- | --- |
| median calibration, overhead 2 (as configured), cap 16, reserve 10,800 | 76,301 | 0.99 |
| the same with cap 8 | 70,165 | 1.08 |
| median calibration, overhead 2.9 (as measured, §3), cap 16 | 102,507 | 0.74 |
| slowest of the 10 calibrations, overhead 2, cap 16 | 95,310 | 0.79 |

Every κ_aff is below the smallest κ the rule can produce (1.3), before C7's sets 2 and 3 add
|F_G| · 0.313 s and more.

## 2. The proposed survivor cap and its justification

**Proposed: 16 survivor orbits per shard** (`SURVIVOR-CAP-PROPOSAL.md`). It is a placeholder until
the owner decides it.

**What the cap is, scientifically.** It is a completeness bound, not a scientific parameter.
- No count, verdict or label depends on it, except that a run over the cap is INCOMPLETE. Its counts
  are still complete, and `survivor_gates_incomplete` is flagged (PO-L2-15).
- It cannot move a result towards collapse, and it cannot hide a survivor.
- Its scientific justification is therefore one requirement: under the cap, a run whose survivors are
  few enough to be a k ≤ 2 result must reach a label other than INCOMPLETE with high probability, and
  must stay within the time and memory each job has.

**Measured** (`design/overhead/survivor-cap.json`, 24 planted survivor orbits of the toy geometry,
contexts up to 29 quantities):
- residue detail: 3.6–4.3 kB per survivor orbit;
- memory kept: ≤ 0.55 MB per orbit;
- peak transient memory: ≤ 2.0 MB per orbit;
- P(cap exceeded) for uniform shard weights, computed exactly from the multinomial.

**Assumed** (Layer 2's model):
- survivor orbits fall independently on shards, with weights proportional to the representatives
  each shard processes;
- a concentration factor f (8 of 32 shards each carry f/32), with the toy class at about f = 2
  (shard 0 holds 53 % of the toy representatives);
- the time per survivor orbit at v8 sizes is the estimate's, 767 s per unit of cap over the run
  (planted calibration at m_max).

**Unknown:**
- X, the number of survivor orbits on v8. The Stage-0 collapse argument predicts 0 at k ≤ 2; that is
  what is being tested.
- The representatives per shard on v8. It is a v8 computation, which the owner's sequencing places
  after the cap decision.

**Justification of 16:**
- **Failure probability.** For up to 64 survivor orbits (≤ 512 survivor records, about 0.01 % of N),
  P(cap exceeded) ≤ 1e-5 with concentration up to f = 2, and about 3 % at f = 4. Above that size the
  residue calls for Stage 1 or a redesign in any case, and an INCOMPLETE run with complete counts
  says so.
- **Memory.** ≤ 9 MB kept per shard: negligible.
- **Time.** About 192 s per replica job, at a cost of 12,272 runner-seconds over the run, which
  §4 counts.

## 3. Costs: measured, assumed, and the toy over-prediction

### 3a. Measured (local machine, Python 3.13.16; timing data, not deterministic)

| quantity | value | source |
| --- | --- | --- |
| production closure time t_c(m) and full-reference time r_c(m), planted sets, m = 8–40 | per-size medians; CV 4–9 % per entry | `calibration-repeats.json` |
| per-record C7 cost at the v8 histogram mean, both copies | c7_A = 0.0715 s, c7_G = 0.313 s | the same |
| known terms of the v8 estimate (closures at overhead 2, sampled gates, S1a, allowances, C7 set 4) | median 64,029 s; CV 9.2 %; range 0.95–1.30 × the median | the same |
| survivor-gate cost per unit of cap | 767 s | the same |
| overhead, Shard.rep against the representative's four bare closures | 2.93 (every toy orbit), 2.87 (120 planted records); medians 2.9–3.0; p90 about 4 | `overhead.json` |
| `-O` copy against the normal run | median ratio 1.01: a full duplicate | `calibration-repeats.json` |
| in-process cache effect | pass 1 / passes 2–3: 0.95–1.06 | the same |
| memory per survivor orbit | ≤ 0.55 MB kept, ≤ 2.0 MB transient | `survivor-cap.json` |

### 3b. Assumed (Layer 2's cost model, `LAYER2-PLAN.md` §3.6)

| assumption | whose | status |
| --- | --- | --- |
| overhead = 2 | Layer 2's drafter, a judgement in r1 | contradicted by the measurement (about 2.9), and left at 2 pending decision |
| the model's form: closures priced per representative at the record's context size; the gates at the mean size; survivor gates at m_max | Layer 2 | unvalidated on any workload of v8 size |
| planted quantity sets stand in for records | Layer 2 | an extrapolation. Planted sets are random quantities in a displaced ball; real records are structured (whole items, port samples, many in-frame quantities under G) |
| times beyond 40 quantities scale quadratically | Layer 2 | not used at v8 sizes (m ≤ 29) |
| pre-flight 300 s, merge 300 s per run | Layer 2, stated allowances | the toy pre-flight took about 130 s locally; the v8 full-mode pre-flight is not timed |
| the reserve, 3 h | Layer 2's proposal (`KAPPA-PROPOSAL.md` §d) | a judgement; the CI calibration's job records would measure the per-job part |
| the runner class is no slower than this machine | implicit | unmeasured until the CI calibration |

### 3c. The toy over-prediction, explained

The toy dry run predicts a total of 2,197–2,453 s across runs (2,453 s in the retained
`design/toyrun/dryrun.json`). The four toy shards took about 9 s in all (`RUN-MANIFEST.json`, steps
`shard_toy_0`–`3`, normal runs).

| toy term | predicted (s) | why it is far above the measured shard time |
| --- | --- | --- |
| survivor gates | 585 | **a bound, not an estimate.** It prices 10 survivor orbits per shard at m_max; the toy class has none. On v8 this term is also a bound, spent only if survivors occur |
| merge, pre-flight | 900 | fixed allowances. They are not part of the shard time at all (the toy pre-flight is a separate step) |
| sampled gates | 721 | the toy profile samples every representative (rate 1) for C8, C11 (i), C17 and C18, priced as reference closures at a context size of at least 8. Toy contexts have at most 8 quantities, so every toy record is priced at the smallest calibrated size. The full reference on toy records measures at 2–7 % of that price (`calibration-repeats.json`, `measured_over_calibration_prediction`) |
| C7 | 229 | 608 per-record checks at planted-set prices; the same size floor and record-structure effects |
| closures, S1a | 20 | close to measured (A closures 1.03 of prediction; G closures 0.12) |
| the `-O` copy | ×2 throughout | the estimate counts both copies; the 9 s are the normal runs only |

**Which of these transfer to v8:**
- **The survivor bound:** yes. It is a priced allowance, and the launch rule must count it.
- **The allowances:** small at v8's scale.
- **The size floor:** no. v8's contexts (mean 16, max 29) lie inside the calibrated range.
- **The record-structure effect:** possibly. On toy records the G closure and both references cost
  far less than on planted sets of the same size, apparently because records under G carry many
  in-frame quantities, whose tips are ineligible. If v8's records behave the same way, the G terms are
  over-predicted, but by an unknown amount.

**The two known model errors point in opposite directions:** overhead under-stated (2 against
about 2.9), and G costs probably over-stated. **The net error is unknown.**

## 4. Can the 24-hour ceiling accommodate the scientifically justified configuration?

**The configuration:**
- κ by the rule (≥ 1.3);
- the survivor cap 16;
- the reserve 3 h;
- every Layer-1 control, including C7 per record on E1-F3's four sets with the full reference, the
  `-O` copy of every shard, and full-mode pre-flight;
- the whole record space, k ≤ 2.

**Verdict, under the cost model: no.** κ · total + reserve, with C7's sets 2 and 3 at zero:

| κ | κ · 76,301 + 10,800 (s) | h | over the ceiling by |
| --- | --- | --- | --- |
| 1.3 (smallest the rule can give) | 109,991 | 30.6 | 27 % |
| 1.6 (the review's provisional pair) | 132,882 | 36.9 | 54 % |
| 2.1 (largest in the sensitivity range) | 171,032 | 47.5 | 98 % |

C7's sets 2 and 3 only add to these: |F_G| · 0.313 s + (|I_A| / 100) · 0.0715 s + (|I_G| / 100) ·
0.313 s. At |F_G| = 1 % of N, that is about 16,000 s more.

**Sensitivity to each assumption** (all others at the line above):

| assumption | change | effect on the verdict |
| --- | --- | --- |
| overhead | 2 → 2.9, as measured | total +26,000 s: further over (κ_aff 0.74) |
| calibration | the slowest of 10 instead of the median | total +19,000 s: further over |
| survivor cap | 16 → 8 | total −6,100 s: still over at κ = 1.3 (28.3 h) |
| reserve | 3 h → 0 | still over at κ = 1.3 (27.6 h) |
| planted-to-record cost ratio ρ (unknown) | actual = ρ × model | fits only if ρ ≤ 0.76 at κ = 1.3, ρ ≤ 0.62 at κ = 1.6, ρ ≤ 0.47 at κ = 2.1, with C7's sets 2–3 at zero |
| runner class | unknown speed | a slower runner moves the verdict further over; a faster one toward fitting |

**The verdict is therefore robust under the model,** to every model input Layer 2 controls. It
turns only if the model over-predicts real v8 work by a quarter or more (ρ ≤ 0.76). The toy evidence
makes that possible for the G terms and impossible to rule out, but the measured overhead points the
other way. The verdict is not a fact about the run.

**Cheap, non-v8 measurements that would most reduce the uncertainty**, in order of value:
1. **Validate the cost model end to end on a scaled toy profile.** Same rule, n = 2, a larger region
   and slice range (for example ρ = 3, t_last = 12), so that contexts reach v8's sizes. Run the real
   shard driver over all its orbits, with the v8 gate rates, and compare the measured shard time with
   the model's prediction for that profile from the same calibration. This measures ρ, the overhead
   and the record-structure effect together. The geometry differs from v8's in n, so it is not v8's
   configuration class. It is a design-evidence step: bounded, local, minutes to an hour depending on
   the region.
2. **The planted-set CI calibration** (proposed in `ci/`, at least 20 runs): u_cal and the runner
   class's speed relative to this machine. It needs review and the owner's authorization of its
   launch.
3. **Per-job fixed overhead**, read from that calibration's structured job records: the reserve's
   main term.
4. **Re-measure the overhead factor** on the scaled toy profile of item 1, and decide whether the
   configured 2 is replaced by a measured value. That is a model correction, not a margin.

## 5. Revised designs that keep statistical validity

**Constraints on every design below:**
- the same κ rule, applied unchanged;
- the same Layer-1 acceptance criteria (the labels, the controls and their pass conditions, E1's
  rulings);
- no lowered margin.

None drops a control or narrows a criterion. Costs are under the model, at κ = 1.6, cap 16, reserve
3 h, and |F_G| = |I_c| = 0 unless stated.

### D1. Several independently launched runs, each within 24 hours

- **What.** Split the 32 shard ranges into n groups. Each group is one run with its own launch,
  pre-flight, S1a and merge, at one frozen commit and `code_digest`. A final cross-run merge checks
  the exact cover and disjointness of all ranges, equal digests and one commit, and generates the
  label from all shards.
- **Cost.** Each run carries its fixed terms (pre-flight, S1a, merge: about 1,450 s) and its reserve.
  - With 74,853 s of shardable work, n runs fit iff 1.6 · (74,853 / n + 1,450) + 10,800 ≤ 86,400,
    that is n ≥ 2.
  - At |F_G| = 1 % of N, n = 2; at 5 %, n = 4.
  - Total runner time is about 76,301 s plus 1,450 s per extra run, spread over n launches.
- **Claim.** Unchanged: the same record space, controls and labels.
- **Needs:**
  - **an owner interpretation of "24 hours maximum, including all run overhead": per run, or for the
    whole experiment.** D1 is admissible only under the per-run reading;
  - a Layer-2 amendment: the cross-run merge and certificate, commit and digest binding across runs,
    and the rule that every run uses the same frozen κ, cap and reserve;
  - a separate authorization per launch, or one authorization covering all n.
- **Risks:**
  - drift between runs (the runner class or image changing between launches). Mitigation: pin the
    image and refuse a run whose recorded runner differs;
  - a failed run makes the whole experiment INCOMPLETE until it is re-run, which is a new owner
    decision (stop rule);
  - more launches, more review surface.

### D2. A staged design: count, then the G-D decision, then the reduced reference set

- **What.**
  - Stage A: the count-only pass (`AMENDMENT-PROPOSAL-V8-COUNT.md`, unadopted) gives |F_G|, |I_c| and
    the representatives per shard.
  - Stage B: the owner decides G_D. If adopted, C7's reference under G on set 2 uses
    W(Out(R)) ∪ In(R), with the cross-check E1 §9 requires.
  - Stage C: the full run with the measured C7 term.
- **Cost.** Stage A is about one to two single-core hours, extrapolated from toy timings. G-D cuts
  the full-reference cost per F_G record (about ten times on toy records, `E1-ANALYSIS.md` §A3), so
  it shrinks only the |F_G| · 0.313 s term. **It does not touch the 76,301 s that already exceed the
  ceiling.** D2 is necessary for an affordable C7 term if |F_G| is large, but not sufficient alone.
- **Claim.** Unchanged. Lemma G-D's equivalence holds for every production output (E1 §9); the
  residual is reference-implementation faults, which fail safe.
- **Needs:** the count amendment and its review; the owner's G-D confirmation (E1 §9); the
  owner's sequencing (κ, cap and ceiling before the count) is already ruled.
- **Risks:** the G-D path is new reference code; its cross-check against the full form on the toy
  class and on sets 3 and 4 is required.

### D3. A pre-declared subset of record indices (a reduction of the claim)

- **What.** Declare before any v8 result a subset of the record space and run Stage 0 on it alone,
  with every control. Examples:
  - every single and every pair whose two sites lie within a declared sub-region;
  - a declared fraction p of orbits, chosen by a fixed hash of the representative's index.
- **Cost.** About p × the shardable work plus the fixed terms. At κ = 1.6, the run fits if
  p ≤ (47,250 − 1,450) / 74,853 ≈ 0.61, with |F_G| = 0.
- **Claim: reduced, and stated as such.**
  - COLLAPSE_ALL would read "every record of the declared subset is collapsed", not "every record of
    C_avg(4, 16, 2)". C_A's and C_G's law statements would cover the subset only.
  - A hash-sampled subset licenses a statement about the sample, not the class. Extending it to the
    class would be an inference outside Stage 0's exact-computation design, and is not proposed.
  - **It is not an equivalent test.**
- **Needs:** a Layer-1 amendment, since the search domain (§1, §12) is frozen, with its own review;
  the owner's decision that a reduced claim is worth its cost.
- **Risks:** the subset must be declared before any v8 output, and chosen on the record space's own
  structure, never on results; a geometric subset may exclude exactly the records where survivors
  would occur.

### D4. Algorithmic savings that provably preserve every value

Each saving changes how a value is computed, never which value. Each needs a proof obligation, a
Layer-2 amendment and review. Its saving is unmeasured until it is built and timed on the scaled toy
profile (§4 item 1).

| saving | proof obligation | Layer-1 effect | expected effect (unmeasured) |
| --- | --- | --- | --- |
| **(a) L3′ from L3's result.** Compute ret_L3 first, then iterate L3′ elimination starting from ret_L3 | GSS_L3′(Q) = GSS_L3′(GSS_L3(Q)). Proof sketch: L3's tips are a subset of L3′'s, so every L3′-self-supporting set is L3-self-supporting, hence GSS_L3′(Q) ⊆ GSS_L3(Q) = R; GSS_L3′(Q) is self-supporting inside R, and GSS_L3′(R) is a self-supporting subset of Q, so the two are equal | C11 (i) defines the state at an elimination as "the initial context minus the quantities logged before it, in log order". A two-phase L3′ log changes that state, so C11 (i)'s state definition for the L3′ log needs a Layer-1 amendment, or the L3′ log must be kept single-phase (no saving there) | reduces the L3′ closure's work by the share of quantities L3 already removes |
| **(b) Member processing.** Build each member's context once per convention and reuse it for L3′ and L3; precompute per-site sample sets once per shard | code identity: `post_closure` results equal; L2-POST on every toy record; C8 in-run | none | aimed at the measured overhead (about 2.9): the member contexts and attributes are most of it |
| **(c) The G closure through Lemma G-D in production.** Compute ret_G = In(R) ⊔ W(Out(R)) | Lemma G-D (proved in E1-F3, `E1-NOTE-symmetry-and-G-D.md`); C7 still compares with the full `s0ref` closure, so the independent check is unchanged | none in the specification; the production engine departs from code-r5's algorithm, so §2's provenance and the review must cover it | reduces G closures to Out(R), which is small on in-frame-heavy records |
| (d) G-D in C7's reference | D2 | none (E1 §9) | the |F_G| term |

**Excluded, because they would drop or weaken a control:**
- running the `-O` copy on a sample only (L1 §5b item 7 requires both copies of every shard);
- sampling C7's set 2 instead of checking every record (E1-F3);
- lowering the survivor cap so that a survivor-rich run becomes INCOMPLETE sooner, as a cost device;
- lowering κ.

### What the owner would need to decide, in order

1. Whether the cheap measurements of §4 (the scaled toy validation, the CI calibration) come first.
   They are recommended: they decide whether the overrun is real.
2. If it is confirmed: D4 (b) and (c), which need only Layer-2 amendments and review, then a
   re-estimate.
3. If it is still over the ceiling: the reading of "24 hours maximum" for D1 (per run or per
   experiment); or D3, a stated reduction of the claim through a Layer-1 amendment; or a declaration
   that Stage 0 at k ≤ 2 is infeasible under this budget.
4. D2 in any case, before the full run (the count and G_D), as the sequencing already provides.

**Not proposed:** lowering κ, dropping or sampling a required control, narrowing an acceptance
criterion, or reading κ_aff as a candidate.
