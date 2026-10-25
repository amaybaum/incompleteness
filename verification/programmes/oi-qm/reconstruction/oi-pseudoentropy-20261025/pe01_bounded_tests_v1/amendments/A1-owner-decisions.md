# PE-01 amendment A1: the three open owner decisions

This amendment fixes the three values that `../PLAN.md` leaves open: θ, $K_{\rm LP}$ and the scope of the passive
$m = 3$ sweep. It is the amendment that the TH checkpoint (§5) records. It changes nothing else in the plan. The
plan's text, controls, admissibility conditions (a)–(f), thresholds, window, classification and stopping rules stand
as reviewed.

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
   - This is the range in the §8 row "Randomized K0, dual LP": $m \le 2$, $n \le 6$, $K \le K_{\rm LP}(n)$.
3. **Passive $m = 3$ sweep: option (ii) of §10, extended through $n = 8$.**
   - Rationale (owner): "Necessary to examine m = 3 where the relaxed footprint cap makes witnesses admissible. Keep
     the sweep passive and cap it at the admissible region."
   - The sweep stays passive: $a \equiv 0$, up to simultaneous conjugacy fixing $v_0$, as in §3.
   - At $n \le 6$ it runs as already planned.
   - At $n = 7$ and $8$ it runs with $K$ capped at the top of the $\theta = n+1$ region: $K \le 15$ at $n = 7$, and
     $K \le 31$ at $n = 8$.
   - It uses the §8 row "Only under option (ii)".

## How the decisions enter the stage

- **One decision rule.** The extended sweep adds observers to the enumerated scope. It does not change the decision
  rule, the conditions (a)–(f), any threshold, or any control.
- **Separate reporting.** The passive $m = 3$ sweep, including its extension, is reported as its own cells under
  §6 item 4's per-(generator, $n$, observer subclass) rule. It is never pooled with another subclass.
- **Separate jobs.** Its CI shards are separate jobs from the primary sweeps of §8. A missing or incomplete $m = 3$
  shard is reported as "not run" for those cells. Every control and checkpoint of §5 keeps its VOID precedence.
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
blob id. A run whose parameters differ from this block, or that cannot read it, refuses to start.

```json pe01-parameters
{
  "amendment": "A1",
  "theta": "n+1",
  "K_LP": "2^(n-1)-1",
  "m3_passive_scope": "ii",
  "m3_passive_K_cap": {"7": 15, "8": 31}
}
```
