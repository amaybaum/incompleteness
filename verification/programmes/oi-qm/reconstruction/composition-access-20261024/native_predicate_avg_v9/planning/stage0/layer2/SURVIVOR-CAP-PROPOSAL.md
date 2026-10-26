# NP-AVG-1 Stage 0, Layer 2: the v8 survivor cap, derived (advisory; r5)

**Status: advisory. It sets nothing.** The v8 survivor cap is an `OWNER-PLACEHOLDER`
(`l2config` `profiles.v8.survivor_cap_per_shard`), with no default. The toy profile's 10 is design
evidence only.

**The owner's requests** (amaybaum, 2026-10-26): "Request a reasoned proposal based on shard
distribution, memory consumption, and failure probability; do not use the placeholder 10." and, after
the r4 review, "The survivor cap should likewise follow from a justified resource and completeness
analysis, not a convenient placeholder." The cap is fixed before any v8 count.

**r5 (LAYER2-R4-REVIEW K1, K2).** r4's justification used a concentration factor f ≈ 2 for the shard
distribution, which the analogues showed to be understated (heaviest shard 2.9–5.0 × the mean under
the index-even plan), assumed survivors independent, and stated that the cap fitted the job inequality,
which was wrong. r5 replaces the index-even plan by the deterministic subdivision, which makes the
representatives per shard exactly equal (to within one), derives the cap from the resulting model with
the clustering of survivors as an explicit parameter, and states the job inequality correctly.

**Nothing here ran on v8.** Sources: `design/overhead/survivor-cap.json` (step `survivor_cap_measure`:
memory and time on planted toy-geometry survivor orbits; the v8 survivor term per unit of cap from the
planted calibration), `design/overhead/survivor-cap-derivation.json` (step `survivor_cap_derive`,
deterministic given its input), `design/subdivision/bounds.json` and `design/midsize/validation.json`.

## 1. What the cap does (unchanged; the scientific justification)

Per shard, the first c survivor orbits get their survivor gates (C0, C7 on set 1, C11 (i), C17, C18 on
every member, both conventions) and their residue detail. A shard that meets more survivor orbits still
computes and counts every record and sets `survivor_cap_exceeded`; the run is then INCOMPLETE, with its
58 counts complete and `survivor_gates_incomplete` flagged (PO-L2-15).

The cap never changes a count, never moves a verdict towards collapse and never drops a counterexample
silently. It decides one thing: whether a survivor-rich outcome can reach a label other than
INCOMPLETE. **It is a resource and completeness parameter, not a scientific one,** and this holds
without any v8 count (LAYER2-R4-REVIEW K2).

## 2. Resources per survivor orbit

| quantity | value | status |
| --- | --- | --- |
| residue detail per orbit | 3.6–4.3 kB | measured, planted toy-geometry orbits, contexts up to 29 (v8's maximum) |
| memory kept per gated orbit (an upper bound: includes the engine's caches) | ≤ 0.55 MB | measured, the same |
| peak transient memory per orbit | ≤ 2.0 MB | measured, the same |
| time per gated orbit per shard, both copies, at v8 sizes | about 24 s (the survivor term per cap unit, 764 s, over 32 shards) | **modelled**: the planted calibration at m_max |

**Memory does not bind:** at c = 64 a shard keeps at most about 35 MB. **Time** adds c × 24 s to a
shard's job and c × 764 s to the campaign.

## 3. The shard distribution under the deterministic subdivision

Every shard holds ⌊R/32⌋ or ⌈R/32⌉ representatives (`LAYER2-PLAN.md` §3.5; on v8, R/32 ≈ 25,500, once
the site-pair count gives the cut points). So if survivor orbits are spread over representatives
independently of their index, each orbit's shard is uniform over the 32 shards: the review's "uniform
row" applies exactly.

**The clustering of survivors is not measured.** Survivors come from geometric constraint blocks, and
the planted ones clustered; neither the toy class nor the four mid-size shards run in r5 has a survivor,
so no available class measures it. The derivation therefore takes it as a parameter: X survivor orbits
arrive as X/b clusters of b orbits, each cluster wholly in one shard (a site pair holds at most 625
representatives, under 3 % of a v8 shard, so a cluster inside one site pair falls in one shard or
straddles two; one shard is the conservative case), the clusters uniform and independent.

## 4. P(INCOMPLETE by the cap)

Exact (rational arithmetic over the 32 shards), from `survivor-cap-derivation.json`:

| X survivor orbits, cluster size b | c = 8 | c = 12 | c = 16 | c = 24 | c = 32 |
| --- | --- | --- | --- | --- | --- |
| X = 32, b = 1 | 1.3e-5 | 1.7e-10 | ≈ 0 | ≈ 0 | ≈ 0 |
| X = 32, b = 4 | 0.048 | 1.9e-3 | 4.9e-5 | 7.2e-9 | 0 |
| X = 32, b = 8 | 0.18 | 0.18 | 3.8e-3 | 3.1e-5 | 0 |
| X = 64, b = 1 | 5.3e-3 | 2.6e-6 | 2.8e-10 | ≈ 0 | ≈ 0 |
| X = 64, b = 4 | 0.36 | 0.041 | 3.1e-3 | 8.3e-6 | 8.5e-9 |
| X = 64, b = 8 | 0.61 | 0.61 | 0.048 | 1.9e-3 | 4.9e-5 |
| X = 128, b = 4 | 0.97 | 0.45 | 0.093 | 1.6e-3 | 1.3e-5 |
| X = 128, b = 8 | 0.99 | 0.99 | 0.36 | 0.041 | 3.1e-3 |

**The derived cap** c*(X, b, α), the smallest c with P ≤ α:

| α | X = 32: b = 1 / 4 / 8 | X = 64: b = 1 / 4 / 8 | X = 128: b = 1 / 4 / 8 |
| --- | --- | --- | --- |
| 1 % | 6 / 12 / 16 | 8 / 16 / 24 | 12 / 24 / 32 |
| 5 % | 5 / 8 / 16 | 7 / 12 / 16 | 11 / 20 / 24 |

**The judgements this rests on**, each the owner's to accept or change:
- **α**, the acceptable probability that a survivor-rich run ends INCOMPLETE because of the cap. Such a
  run still reports complete counts and the flag, so a cap failure is benign: it costs a re-run with a
  larger cap, not a wrong result.
- **X, the reference number of survivor orbits.** The Stage-0 collapse argument predicts X = 0 at
  k ≤ 2; the cap matters only if that fails. 64 orbits are at most 512 survivor records, about 0.01 %
  of N; beyond that the residue calls for Stage 1 or a redesign whatever the label.
- **b, the cluster size.** Not measured (§3).

## 5. Proposal

**c = 16 survivor orbits per shard,** derived as the smallest cap with P(INCOMPLETE by the cap) ≤ 5 % at
X = 64 survivor orbits in clusters of up to 8, and ≤ 1 % at X = 64 with clusters of up to 4 or at
X = 32 with clusters of up to 8. **At α = 1 %, X = 64, b = 8 the derived cap is 24.** The owner chooses
the envelope; the numbers above give the cap for each.

**Its resources:** about 8 MB kept and 2 MB transient per shard; about 380 s per shard job (both copies)
and 12,224 runner-seconds in the campaign (c = 24: about 570 s and 18,336 s). Memory measured; time
modelled, from the planted calibration.

**The job inequality, correctly stated** (LAYER2-R4-REVIEW K1). A shard job runs both copies against its
40 minutes. Under the cost model, the mean shard's known terms (closures and sampled gates, both copies)
are already about 1,900 s; with the subdivision's modelled cost spread (heaviest about 1.04 × the mean
on the ball(3) analogue) and C7's set 4, about 2,050 s before any survivor allowance. **c = 16 adds about
380 s: about 2,435 s, over 2,400 s at κ = 1.** Above κ = 1.17 the job inequality fails with no survivor
allowance at all. So under the model no cap value satisfies the job inequality at 32 shards and any κ
the rule can give; the cap is not the binding term. The levers are the shard count (S7's "at most 32
shards", a Layer-1 amendment), the per-shard work (`FEASIBILITY-AND-REDESIGN.md`), or the model's error
(the mid-size validation finds it over-predicts every shard measured, the heaviest by about 10 %); never κ or the timeouts (owner).
With more shards the per-shard cap can stay at the derived value, but the survivor term grows with the
shard count (c × S × 24 s).

**Cost in the campaign:** c × 764 s of the 24-hour campaign ceiling, under the model. The campaign does
not fit at any cap under the model (`FEASIBILITY-AND-REDESIGN.md`); the cap's share of the overrun is that
term.

## 6. What would replace the judgements with measurements

- **b:** any class with survivors. A planted survivor population on the mid-size analogue (constraint
  blocks placed at several centres, as `planted_shard.py` does on the toy geometry) would measure how
  survivor orbits cluster in representative rank. Proposed as a bounded design step; not run in r5.
- **The time per orbit at v8 sizes:** the mid-size analogue's real shards measure per-representative
  cost at v8-like contexts, but not per survivor orbit (no survivors there).
- **The representatives per shard on v8:** the site-pair count (`SITE-PAIR-COUNT.md`), conditionally
  approved and not dispatched. It makes §3's uniform weights exact for v8.
