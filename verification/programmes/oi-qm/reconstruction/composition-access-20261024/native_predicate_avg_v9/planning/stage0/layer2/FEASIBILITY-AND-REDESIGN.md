# NP-AVG-1 Stage 0, Layer 2: feasibility under the 24-hour ceiling, and revised designs (advisory; r5)

**Status: advisory, for the owner. It sets nothing and adopts no design.** It answers the owner's
request of 2026-10-26 (amaybaum) to "clearly distinguish: the statistically justified κ estimate from
the computationally affordable κ; the proposed survivor cap and its scientific justification; the
measured calibration costs from the unmeasured overhead assumptions; whether the 24-hour ceiling can
accommodate the scientifically justified configuration. If it cannot, propose a revised experimental
design rather than reducing κ to make the run fit."

**r5.** The r4 version (committed at `b6da326b`, outside LAYER2-R4-REVIEW's scope) is revised for:
- the owner's decisions of 2026-10-26: the ceiling is per complete campaign and includes calibration,
  count pass, primary run, mutant campaign, retries and execution overhead; the shard imbalance is a
  design blocker, to be met by deterministic subdivision, "Do not compensate by lowering κ or simply
  increasing job timeouts";
- LAYER2-R4-REVIEW K1: a second infeasibility, the per-job inequality, which does not depend on κ;
- the review's validation step, run on a mid-size analogue (§3);
- the review's redesign levers (§5).

**Sources.** The retained r5 design evidence: `design/kappa/calibration-repeats.json`,
`design/overhead/`, `design/subdivision/bounds.json`, `design/midsize/validation.json`,
`design/runs/dryrun_v8_estimate.out` and `design/RUN-MANIFEST.json`. **Nothing ran on v8's configuration
class.** v8 enters only through the dry run's combinatorics.

**Labels:** **measured** (from a retained run, with its file); **modelled** (the cost model or an
extrapolation, with whose); **judged** (an explicit judgement, with whose); **unknown** (not computable
without an unauthorized v8 computation, or not yet measured).

## 1. κ: the statistically justified estimate, and the affordable κ

**The justified κ** is u_cal × u_model, rounded up to one decimal (the owner's method).
- **u_cal, measured locally, not yet on the runner class.** Four repeats of the 10-calibration local
  procedure give 1.21, 1.29, 1.37 and 1.19 (r5) for the 99th percentile of the ratio of two
  independent calibrations (`KAPPA-PROPOSAL.md` §b). It is preregistered for the CI calibration as an
  upper confidence bound (one-sided 95 % on the spread), which at n = 20 is about 1.37 × the point
  estimate's σ.
- **u_model, judged**, range 1.0–1.5 in the sensitivity analysis. The mid-size validation (§3) shows a
  per-shard model error from 0.08 to 0.90, so the range is not generous.
- **So κ ≥ 1.3 by the method,** and 1.3–2.1 across the sensitivity range. None is proposed as the value.

**The affordable κ, a diagnostic and never a candidate:** κ_aff = (86,400 − reserve) / total, the
largest κ for which the configuration fits under the model. Choosing it would be the "artificially
smaller margin" the owner ruled out.

| configuration (C7 sets 2 and 3 at 0, their least possible value) | κ_aff |
| --- | --- |
| primary run only, reserve 10,800 (r4's form; LAYER2-R4-REVIEW K3 on r4's calibration: 1.08 at cap 8, 0.99 at cap 16) | 1.07 at cap 8, 0.98 at cap 16 |
| the campaign's known terms (§4), reserve 0, no execution overhead or retries | 1.11 at cap 8, 1.03 at cap 16 |
| the campaign with the judged execution overhead, the proposed retry allowance and reserve | 0.90 at cap 16 |

Every κ_aff is below 1.3, the smallest κ the method can give.

## 2. The per-job inequality: an infeasibility that does not depend on κ (K1)

**The inequality.** Both copies of a shard (normal and `-O`) run within its 40-minute timeout, as one job
or two 20-minute replica jobs. The heaviest shard decides (r5, PO-L2-24).

**Under r4's index-even plan** it fails by about a factor of 4 at any κ: representatives concentrate in
low-index shards (heaviest/mean 2.9, 3.7 and 5.0 on ball(1), ball(2) and ball(3); LAYER2-R4-REVIEW K1).

**Under r5's deterministic subdivision** (`LAYER2-PLAN.md` §3.5; measured in
`design/subdivision/bounds.json`):
- representatives are balanced exactly (heaviest/mean 1.00 on ball(2) and ball(3));
- the modelled closure cost is nearly balanced (heaviest/mean 1.49, 1.09 and 1.04 on ball(1), ball(2)
  and ball(3)).

**It still fails, under the model, at 32 shards:**

| survivor cap | heaviest shard, both copies (model, s) | largest κ for which it fits |
| --- | --- | --- |
| no allowance | about 2,050 | 1.17 |
| 8 | about 2,240 | 1.07 |
| 16 | about 2,435 | below 1 |

(The mean shard's closures and sampled gates are 1,916 s, C7's set 4 adds about 63 s, the ball(3)
spread 1.04, and the survivor allowance c × 24 s. C7's sets 2 and 3 are not included.) **No κ the rule
can give (≥ 1.3) satisfies it, whatever the cap.** This failure does not depend on the campaign total.

**The measured spread is larger than the modelled one.** On the mid-size analogue (§3) four shards of
exactly 325 representatives each took 7.9, 8.5, 18.5 and 131.6 s: the heaviest is 3.2 × the mean of the
four, where the model predicts 1.34 for the heaviest over the mean of all 128. Representative balance
does not give cost balance. The dominant per-record cost there is C7 on set 2 (F_G, 40 % of the
analogue's records), whose placement across shards the site-pair counts cannot see.

**What it would take.** Not κ, and not the timeouts (owner). Either less work per shard (§5 levers
(ii)–(iv)), or more shards (lever (vi), a Layer-1 amendment of S7's "at most 32 shards"), or a
cost-balanced subdivision with a validated per-record cost proxy (lever (i′)).

## 3. Costs: measured, modelled, judged; the mid-size validation

### 3a. Measured (local machine, Python 3.13.16; timing data, not deterministic)

| quantity | value | source |
| --- | --- | --- |
| production closure t_c(m) and full-reference r_c(m), planted sets, m = 8–40 | per-size medians; median CV 4–12 % per entry | `calibration-repeats.json` |
| the v8 estimate's known primary terms | median 64,784 s; CV 5.7 %; 0.95–1.13 × the median | the same |
| the ratio of two independent calibrations, p99 | 1.19 (r5); 1.21–1.37 in earlier repeats | the same; `KAPPA-PROPOSAL.md` §b |
| overhead, Shard.rep against four bare closures | toy geometry: 2.87 (every toy orbit), 2.89 (120 planted records); **mid-size analogue, contexts 12–27: median 2.24, p90 3.46** | `overhead.json`; `midsize/validation.json` |
| `-O` copy against the normal run | median ratio 1.01: a full duplicate | `calibration-repeats.json` |
| memory per survivor orbit | ≤ 0.55 MB kept, ≤ 2.0 MB transient | `survivor-cap.json` |
| population count (the amendment's pass) on the analogue | about 115 s for 188,125 records | `midsize/validation.json` |
| site-pair count | ≤ 0.01 s, about 22 MB, on ball(1)–(3) | `subdivision/bounds.json` |
| four mid-size shards against the model (single copy) | actual 7.9, 131.6, 18.5, 8.5 s; predicted 60.4, 145.5, 62.3, 110.8 s; actual/predicted 0.13, 0.90, 0.30, 0.08 | `midsize/validation.json` |
| C7 populations on the analogue | F_G 40.1 %, I_A 41.9 %, I_G 40.1 %, E_G 8.3 % of N | the same |

### 3b. Modelled and judged

| assumption | whose | status |
| --- | --- | --- |
| the cost model's form: closures per representative at its context size; gates at the mean size; survivor gates at m_max; C7 per record at the record-weighted mean | Layer 2 | **tested on the analogue (§3c): not validated per shard; it over-predicts three of four shards and is near on the heaviest** |
| overhead = 2 | Layer 2's drafter (r1), judged | measured 2.24 (median) at v8-like sizes on the analogue, 2.87 on toy geometry; left at 2 |
| planted quantity sets stand in for records | Layer 2 | an extrapolation; the analogue shows record costs both well below and near the planted prices |
| the population count scales linearly in records to v8 | Layer 2 | modelled (A4's measurement is on the analogue) |
| pre-flight 300 s, merge 300 s per run | Layer 2, stated allowances | the toy pre-flight took about 140 s; v8's full mode is not timed |
| per-job fixed overhead 90 s | Layer 2, judged | to be measured by the CI calibration (CI-5) |
| retry allowance 2,400 s, reserve 3,600 s | Layer 2's proposal, judged | `KAPPA-PROPOSAL.md` §d |
| the runner class is no slower than this machine | implicit | unmeasured until the CI calibration |

### 3c. What the mid-size validation shows, and does not

- The four shards were chosen by the model's own ranking (the first, the heaviest, the lightest and the
  median), not at random. Their actual total is 0.44 of the predicted, but this is not an estimate of
  the total's error.
- The model is near on the heaviest shard (actual/predicted 0.90) and over-predicts the other three, by
  3 to 13 ×.
- The spread between equally balanced shards is far larger than modelled (§2).
- r4's statement that the toy over-prediction "does not transfer to v8" was an untested explanation. On
  the analogue the model over-predicts most shards but not the heaviest, which is the one that binds the
  per-job inequality.

## 4. Can the 24-hour ceiling accommodate the scientifically justified configuration?

**The configuration:** κ by the rule (≥ 1.3); the survivor cap derived in `SURVIVOR-CAP-PROPOSAL.md`
(16); the reserve; every Layer-1 control, including C7 per record on E1-F3's four sets with the full
reference, the `-O` copy of every shard and full-mode pre-flight; the whole record space, k ≤ 2.

**The campaign's known terms** (the ledger, `LAYER2-PLAN.md` §3.5): primary run 64,784 s + survivor term
12,224 s + calibration 220 s + count pass about 3,161 s + mutant campaign 3,872 s = **84,261 s**, before
C7's sets 2 and 3, execution overhead and retries.

**Verdict, under the cost model: no, on two independent counts.**
1. **The campaign** (κ · 84,261 + the proposed reserve 3,600):

   | κ | κ · campaign + reserve (s) | h | over the ceiling by |
   | --- | --- | --- | --- |
   | 1.3 (smallest the rule can give) | 113,139 | 31.4 | 31 % |
   | 1.6 (the review's provisional pair) | 138,417 | 38.4 | 60 % |
   | 2.1 (largest in the sensitivity range) | 180,547 | 50.2 | 109 % |

   Execution overhead (judged about 5,600 s) and retries only add.
2. **The per-job inequality** fails at every κ the rule can give (§2), whatever the campaign total.

**C7's sets 2 and 3** add |F_G| · 0.303 s + (|I_A| / 100) · 0.0715 s + (|I_G| / 100) · 0.303 s, which is
unknown on v8. **An analogue indication, not a v8 figure:** if v8's F_G were 40 % of N, as on the toy and
the mid-size analogue, set 2 alone would be about 627,000 s under the model, seven times the ceiling.
The model over-predicts some record classes by large factors (§3c); even a 13-fold over-prediction
leaves about 48,000 s.

**Sensitivity** (each change alone, from the κ = 1.3 line):

| assumption | change | effect |
| --- | --- | --- |
| overhead | 2 → 2.24 (measured at mid sizes) / 2.9 (toy geometry) | +7,100 s / +26,500 s: further over |
| calibration | the slowest of 10 instead of the median | +8,500 s: further over |
| survivor cap | 16 → 8 | −6,112 s: still over (29.2 h) |
| reserve | → 0 | still over (30.4 h) |
| actual = ρ × model, all terms | ρ unknown | the campaign fits only if ρ ≤ 0.76 at κ = 1.3, 0.61 at 1.6, 0.47 at 2.1, with C7's sets 2–3 at 0 |

**The verdict is robust under the model to every input Layer 2 controls,** but it is a statement about
the model. The mid-size validation makes ρ well below 1 plausible for cheap shards and about 0.9 for the heaviest; it
does not make either verdict turn.

## 5. Revised designs and levers

**Constraints on every design:** the same κ rule, applied unchanged; the same Layer-1 acceptance criteria
(the labels, the controls and their pass conditions, E1's rulings); no lowered margin; no raised timeout
to fit. None below drops a control or narrows a criterion except D3, which reduces the claim and says so.

### The review's levers (LAYER2-R4-REVIEW §5), with r5's status

| lever | what it changes | status in r5 | what it needs |
| --- | --- | --- | --- |
| **(i) representative-balanced shards** | the per-job inequality's concentration | **done:** the deterministic subdivision (exact accounting, L2-SHARDPLAN, L2-SPLIT). Necessary, not sufficient: cost is not balanced (§2) | on v8, the site-pair count (conditionally approved; review, then the owner's authorization) |
| **(i′) cost-balanced subdivision** (new) | cuts at equal modelled or measured cost instead of equal representatives, still a pure function of frozen inputs | not implemented. The modelled weights (`shard_context_weights`) are computable from the site-pair counts and the dry run's per-site item sets; they do not capture the measured spread, which follows C7's set 2 | a per-record cost proxy validated on the analogues; on v8 it would likely need F_G per site pair, an extension of the population count (owner) |
| **(ii) the `-O` full duplicate** | a factor of about 2 on almost every primary term (L1 §5b item 7) | not changed | a Layer-1 amendment, e.g. `-O` on a preregistered sample of shards, with its own review of what it then certifies |
| **(iii) C7 set 2 on F_G through Lemma G-D** | the reference cost of the largest unknown term | not implemented (the owner: conditionally approved, non-executing until the proof is confirmed) | the owner's confirmation; then a reviewed implementation with the cross-check E1 §9 requires |
| **(iv) engineering the gate overhead** | the overhead factor (2.2 at mid sizes) | not implemented (D4 (b) below) | a Layer-2 amendment and review; each saving measured on the analogue |
| **(v) the budget itself** | the ceiling | the owner's | — |
| **(vi) the shard count** (new) | the per-job inequality only: more, smaller shards | not changed | a Layer-1 amendment of S7's "at most 32 shards". It does not reduce the campaign: the survivor allowance grows with the shard count (c × S × 24 s), and each job adds execution overhead |

### D1. Several independently launched runs — no longer an escape

The owner's ruling makes the ceiling per complete campaign and an aggregate compute-runtime budget, not a
wall-clock deadline. Splitting the run into several launches only spreads wall-clock time: every launch's
compute time is in the one ledger, and each launch adds its fixed terms (pre-flight, S1a, merge, about
1,450 s) and execution overhead. **D1 no longer helps fit the ceiling,** and is withdrawn as a lever.

### D2. A staged design: count, then G-D, then the full run

- Stage A: the site-pair count (shard cut points) and the population count (|F_G|, |I_c|).
- Stage B: the owner decides G_D. If adopted, C7's reference under G on set 2 uses W(Out(R)) ∪ In(R),
  with the cross-check E1 §9 requires.
- Stage C: the full run with the measured C7 term.

Both counts are in the campaign ledger (the population count about 3,200 s modelled). G-D shrinks only
C7's set-2 term; **it does not touch the 84,261 s of known terms that already exceed the ceiling at
κ ≥ 1.3, nor the per-job inequality.** Necessary for an affordable C7 term if |F_G| is large; not
sufficient alone.

### D3. A pre-declared subset of record indices (a reduction of the claim)

Declare, before any v8 result and on the record space's own structure, a subset (a sub-region, or a
hash-chosen fraction of orbits) and run Stage 0 on it alone with every control. **The claim is reduced
and stated as such:** COLLAPSE_ALL would cover the subset, not C_avg(4, 16, 2); a hash-sampled subset
licenses a statement about the sample, not the class. Needs a Layer-1 amendment (the search domain is
frozen), with its own review. A geometric subset may exclude exactly the records where survivors would
occur.

### D4. Algorithmic savings that provably preserve every value

Each changes how a value is computed, never which value; each needs a proof obligation, a Layer-2
amendment and review, and is unmeasured until built and timed on the mid-size analogue.

| saving | proof obligation | Layer-1 effect | aimed at |
| --- | --- | --- | --- |
| (a) L3′ from L3's result | GSS_L3′(Q) = GSS_L3′(GSS_L3(Q)) (sketch in the r4 version) | C11 (i)'s state definition for a two-phase L3′ log needs a Layer-1 amendment, or no saving | the L3′ closures |
| (b) member processing: contexts built once per convention, per-site samples once per shard | code identity (L2-POST; C8 in-run) | none | the overhead factor (lever (iv)) |
| (c) the G closure through Lemma G-D in production | Lemma G-D (proved in E1-F3); C7 still compares with the full `s0ref` closure | none in the specification; provenance and review | the G closures |
| (d) G-D in C7's reference | D2 | none (E1 §9) | the \|F_G\| term (lever (iii)) |

**Excluded, because they would drop or weaken a control:** running the `-O` copy on a sample without a
Layer-1 amendment; sampling C7's set 2; lowering the survivor cap as a cost device; lowering κ; raising a
timeout to fit.

## 6. What the owner would need to decide, in order

1. **The cheap measurements first** (they decide whether the overruns are real): the CI calibration
   (u_cal and the per-job overhead; two launches proposed), and a bounded extension of the mid-size
   validation (all 128 shards in CI, or more shards locally) to measure the cost spread and the total's
   model error. Neither touches v8.
2. **The site-pair count's dispatch,** after its independent review (`SITE-PAIR-COUNT.md`): it fixes v8's
   cut points and the cap's shard weights, but not the cost balance.
3. **If the overruns are confirmed:** D4 (b) and (c), which need only Layer-2 amendments and review, then
   a re-estimate; and lever (i′) if a validated cost proxy exists.
4. **If still over:** Layer-1 amendments for lever (ii) (the `-O` copy) or (vi) (the shard count), or D3
   (a stated reduction of the claim), or lever (v), or a declaration that Stage 0 at k ≤ 2 is infeasible
   under this budget.
5. **D2 in any case before the full run** (the population count and G_D), as the sequencing provides.

**Not proposed:** lowering κ, raising a timeout to fit, dropping or sampling a required control,
narrowing an acceptance criterion, or reading κ_aff as a candidate.
