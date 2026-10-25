# PE-01 amendment A1: the three open owner decisions

This amendment fixes the three values that `../PLAN.md` leaves open: θ, $K_{\rm LP}$ and the scope of the passive
$m = 3$ sweep. It is the amendment that the TH checkpoint (§5) records. It also adds reporting rules for the extended
sweep (below). The plan's text, controls, admissibility conditions (a)–(f), thresholds, window, classification and
stopping rules stand as reviewed.

- **Plan amended:** `../PLAN.md` at commit `af38dc2dde0fbdd190a67debf700ab5c370f92d9`, sha256
  `bf7b0cb9387eb69b8ffc925c0ed09a789911c670da2a0144408f3d473dd5e091`.
- **Decided by:** the owner (amaybaum), 2026-10-25, on revision 5 (`af38dc2d`). The decisions and rationale below
  quote that decision.

## Decisions

1. **Footprint cap: $\theta = n + 1$.**
   - Rationale (owner): "Opens the m = 3 and m = 4 witness regions, giving the experiment substantially greater
     discriminatory power for the cost of one additional bit."
   - Condition (f) of §6 reads: footprint $m + \lceil \log_2(K+1) \rceil + 1 \le n + 1$.
   - The admissible region is the §7 table for $\theta = n+1$, as recomputed by AR.
   - The horizon bound of the resource model is $K < 2^{\,n-m}$.
2. **LP horizon: $K_{\rm LP}(n) = 2^{n-1} - 1$.**
   - Rationale (owner): "Accept the proposed range. Retain it as the preregistered horizon, with no post-result
     adjustment."
   - This is the range in the §8 row "Randomized K0, dual LP": $m \le 2$, $n \le 6$, $K \le K_{\rm LP}(n)$. It applies
     only at $n \le 6$, the LP's range.
3. **Passive $m = 3$ sweep: option (ii) of §10, extended through $n = 8$.**
   - Rationale (owner): "Necessary to examine m = 3 where the relaxed footprint cap makes witnesses admissible. Keep
     the sweep passive and cap it at the admissible region."
   - The sweep stays passive: $a \equiv 0$, up to simultaneous conjugacy fixing $v_0$, as in §3.
   - At $n \le 6$ it runs as already planned.
   - At $n = 7$ and $8$ it runs with $K$ capped at the top of the $\theta = n+1$ region: $K \le 15$ at $n = 7$, and
     $K \le 31$ at $n = 8$.
   - It uses the §8 row "Only under option (ii)".

## How the decisions enter the stage

- **Owner clarification of "separate".** The owner's safeguard reads: "Keep the passive sweep separate from the primary
  acceptance criterion". Asked to choose among three readings, the owner selected, on 2026-10-25, "(a) Same rule": "One
  decision rule for all observers. An m = 3 witness meeting (a)–(f) counts as a counterexample. The sweep is reported
  as its own cells and runs in its own CI jobs. Any control failure voids the whole stage."
- **One decision rule.** The extended sweep adds observers to the enumerated scope. It does not change the decision
  rule, the conditions (a)–(f), any threshold, or any control.
- **Separate reporting.** The passive $m = 3$ sweep, including its extension, is reported as its own cells under
  §6 item 4's per-(generator, $n$, observer subclass) rule. It is never pooled with another subclass.
- **Separate jobs.** Its CI shards are separate jobs from the primary sweeps of §8.
  - A shard that was never started is reported as "not run" for its cells.
  - A shard that started and did not finish is reported as "incomplete", with its reason and with the results of
    every cell it completed. Its partial output is committed (§8).
  - Neither status is a verdict.
  - A checkpoint failure inside an $m = 3$ shard makes the whole stage VOID (§6 item 1), as for any other shard.
- **Results are stated under $\theta = n + 1$ only.**
  - The verdict prints each witness's measured footprint (FP).
  - Whether an individual witness also has footprint $\le n$ is therefore a recorded measurement.
  - No conclusion is drawn at $\theta = n$. In particular, the absence of an admissible witness at $\theta = n+1$ is
    not reported as a result at $\theta = n$.
  - $\theta = n$ remains an alternative resource model that PE-01 does not test as a decision rule.
- **No post-result changes.** No threshold, admissibility rule, cap, horizon or stopping criterion is changed after
  any result is seen, except by a further amendment in this directory, committed and recorded before the run it
  governs.

## Parameters read by the checker

The TH checkpoint reads the values below from this file, and records them in the measurement JSON with this file's
blob id. The checker evaluates each formula at every $n$ and compares the result with the explicit per-$n$ values.
A run refuses to start if:
- any formula and its per-$n$ values disagree;
- its parameters differ from this block;
- it cannot read the block.

```json pe01-parameters
{
  "amendment": "A1",
  "theta": "n+1",
  "theta_by_n": {"3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9},
  "K_LP": "2^(n-1)-1",
  "K_LP_by_n": {"3": 3, "4": 7, "5": 15, "6": 31},
  "m3_passive_scope": "ii",
  "m3_passive_K_cap": {"7": 15, "8": 31}
}
```
