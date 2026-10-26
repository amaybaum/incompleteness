# NP-AVG-1 Stage 0, Layer 2: a proposal for the v8 survivor cap (advisory)

**Status: advisory. It sets nothing.** The v8 survivor cap is an `OWNER-PLACEHOLDER`
(`l2config` `profiles.v8.survivor_cap_per_shard`), with no default. The toy profile's 10 is design
evidence only.

**The owner's request** (amaybaum, 2026-10-26): "Request a reasoned proposal based on shard
distribution, memory consumption, and failure probability; do not use the placeholder 10." The
cap is fixed before any v8 count ("Fix κ, the survivor cap, and budget ceiling before any v8
count").

**Nothing here ran on v8.** The measurements are on planted records of the toy geometry
(`design/survivor_cap_measure.py`, retained output `design/overhead/survivor-cap.json`; timing and
memory data). The per-cap cost is the v8 estimate's, from the local calibration
(`design/kappa/calibration-repeats.json`).

## 1. What the cap does

Per shard, the first c survivor orbits get their survivor gates (C0, C7 on set 1, C11 (i), C17, C18
on every member, both conventions) and their residue detail. A shard that meets more survivor orbits:
- still computes and counts every record;
- sets `survivor_cap_exceeded`.

The run is then INCOMPLETE, with its 58 counts complete and `survivor_gates_incomplete` flagged
(LAYER2-R3-REVIEW R2; PO-L2-15).

The cap therefore decides one thing only: whether a survivor-rich outcome can reach a label other
than INCOMPLETE. It never changes a count, never moves a verdict towards collapse, and never drops a
counterexample silently. Its cost is the survivor-gate term of the estimate.

## 2. Memory and time per retained survivor (measured)

**Measurement.** 24 planted survivor orbits of the toy setup: constraint blocks at eight centres,
some with extra items, with contexts of up to 29 non-fixed quantities, v8's maximum.

| quantity | median | max |
| --- | --- | --- |
| residue detail per survivor orbit (canonical JSON) | 3.6 kB | 4.3 kB |
| memory the shard keeps after one gated orbit (tracemalloc; includes the engine's caches, so an upper bound for the detail) | 0.36 MB | 0.55 MB |
| peak transient memory while one orbit is gated | 1.75 MB | 2.0 MB |
| time of one gated survivor orbit, toy geometry, under tracemalloc | 1.9 s | 2.4 s |

**At v8 sizes.** The estimate prices one survivor orbit at m_max as 767 s / 32 ≈ 24 s per shard, both
copies, from the planted calibration (`survivor_gates_seconds_per_cap_unit`, median of 10). That is
about 12 s per replica job.

**Memory.** At any cap below 100 the shard keeps at most 100 × 0.55 MB = 55 MB. That is negligible
against a hosted runner's memory, which the CI review states for the runner class. **Memory does not
bind the cap.**

## 3. The shard distribution

Survivor orbits are processed in the shard of their representative's index. The shard plan splits the
index range evenly, but representatives are not spread evenly. A representative is the minimal image
of its orbit, and the index order runs singles first, then pairs by site pair, so representatives
cluster at low indices.
- **On the toy class**, the four shards hold 260, 36, 162 and 30 of the 488 representatives: shard 0
  holds 53 %, against 25 % if they were uniform.
- **On v8** the representatives per shard are not computed here. They are part of the count-only
  pass (`AMENDMENT-PROPOSAL-V8-COUNT.md` §1), which by the owner's sequencing comes after the cap is
  fixed.

The model therefore uses a concentration factor f. A quarter of the shards (8 of 32) each carry f/32
of the representatives, and the rest share what remains. f = 1 is uniform; the toy class corresponds
to roughly f = 2.

**The failure probability** is P(cap exceeded): the probability that some shard receives more than c
of X survivor orbits, the orbits placed independently with the shard weights. It is computed exactly
for uniform weights (`survivor-cap.json`), and by an independent-Poisson approximation for f = 2 and 4.

| c | X = 32 survivor orbits (f = 1 / 2 / 4) | X = 64 (f = 1 / 2 / 4) | X = 128 (f = 1 / 2 / 4) | survivor term (s; h) | per replica job (s) |
| --- | --- | --- | --- | --- | --- |
| 8 | 1.3e-5 / 1.9e-3 / 0.16 | 5.3e-3 / 0.16 / 0.98 | 0.50 / 0.99 / 1 | 6,136 (1.7) | 96 |
| 12 | 1.7e-10 / 1.7e-6 / 2.2e-3 | 2.6e-6 / 2.2e-3 / 0.41 | 6.4e-3 / 0.41 / 1 | 9,204 (2.6) | 144 |
| 16 | ≈ 0 / 4.5e-10 / 9.1e-6 | 2.8e-10 / 9.1e-6 / 0.029 | 1.9e-5 / 0.029 / 0.99 | 12,272 (3.4) | 192 |
| 24 | ≈ 0 / ≈ 0 / 1.3e-11 | ≈ 0 / 1.3e-11 / 9.4e-6 | 8.2e-12 / 9.4e-6 / 0.17 | 18,408 (5.1) | 288 |

**How large X might be.**
- The Stage-0 collapse argument (`RECHECK-r2.md` §1) predicts X = 0 at k ≤ 2. The cap matters only if
  that prediction fails.
- 64 survivor orbits are at most 512 survivor records, about 0.01 % of N. Beyond that, the residue is
  large enough to call for Stage 1 or a redesign in any case. An INCOMPLETE run that reports complete
  counts and the flag is then an informative outcome, not a lost one.

## 4. Proposal

**c = 16 survivor orbits per shard**, reasoned as follows:
- **Failure probability.** For up to 64 survivor orbits, P(cap exceeded) is at most about 1e-5 with
  concentration up to twice the uniform share (about the toy class's), and about 3 % at four times.
  For up to 32 orbits it is below 1e-5 even at f = 4. c = 12 reaches 41 % at X = 64 under f = 4; c = 8
  reaches 16 % at f = 2.
- **Memory.** About 9 MB kept and 2 MB transient per shard: negligible.
- **Time per job.** About 192 s per replica job at m_max. That fits the job inequality: about 1,138 s
  per replica job before C7, × κ = 1.6, gives 1,821 s against 2,400 s.
- **Cost.** 12,272 runner-seconds (3.4 h) of the 24-hour ceiling under the cost model. Under the
  model the full run does not fit the ceiling at any cap (`KAPPA-PROPOSAL.md` §c). The cap's share of
  the overrun is c × 767 s, so the owner may prefer a smaller cap and accept a higher INCOMPLETE
  probability under concentration. c = 8 saves 6,136 s.

**Recommended review step.** If the owner allows a site-pair-level combinatorial count of
representatives per shard before the cap is fixed, the concentration factor would be measured rather
than assumed. That count needs no record, no context and no closure, but it is still a computation
on v8's geometry, and it is not authorized here. Otherwise c = 16 holds under f ≤ 2 with a wide
margin.
