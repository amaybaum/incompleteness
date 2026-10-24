# Coordinator review: native-wave bounded resource handoff v1

> **DRAFT — research record.** The owner's read-only session produced this handoff. It is recorded here with the
> coordinator's verification and independent checks. Nothing here changes a manuscript claim or a frozen record.

## Verification

- **Archive.** The archive's sha256 is `3f46ae00b8c52080a2e9d0a88ad60f84c0ac9e333f839d1c85d04f6cbe402b7c`, as
  stated. The files in `handoff/` are its contents, unchanged. Their own `SHA256SUMS` verifies all four files.
- **Code review before running.** `native_wave_checks.py` imports only the standard library, writes no files and
  makes no network calls.
- **Replay.** Run from a separate directory with `python3 -I`, and again with `-O`, the output is byte-identical to
  `native_wave_checks.out`.

## Independent checks

**Scripts.** `coordinator_native_wave_checks.py` (separate code), with `sweep_history.py` for the sweeps. Ranks are
computed over F_q. The forms are built by a light-cone recursion, written afresh and memoized over (site, t), in
both time directions.

| Check | Result |
|---|---|
| R1 | One port, L = 9, q = 3, α = 1: conditional ranks [1, 2, 3, 4]. The frontier coefficient α^t of u_{x+te₁}(0) is present in u_x(t), and absent from every earlier reading |
| R2 | The one-port lemma for q ∈ {3, 5, 7}, every nonzero α, L = 7, K = 3 (12 cases): full conditional rank, frontier coefficient α^t |
| R3 | Eight ports built directly on the L = 18 torus, with no translation from L = 9: supports disjoint, ranks 16 and 48, matching P2 |
| R5 | The first-success call law from i.i.d. uniform symbols, for q ∈ {3, 5} and n ≤ 3: failure q^(−n), and (q − 1)/q^(k+1) for each (wait, mark) |

## Findings

### 1. Port separation is sufficient, not necessary (POSITIVE, exploratory)

- **Measured.** Two ports at axis distance 1 to 9 on L = 18, K = 4 keep full conditional rank 8 (R4).
- **Sweep.** For q ∈ {3, 5}, every nonzero α, K = 3 and L = 15, every case keeps full rank (186 cases). The sweep
  covers offsets with each coordinate in 0–3 at L1 distance 1 to 4, so it omits offsets such as (4, 0, 0). R4
  covers the axis distances 1 to 9 on L = 18.
- **What this means.** Freshness across ports holds well inside the separation 2K that the report's proof uses.
- **Scope.** This is computed evidence for these instances only. No proof is supplied.

### 2. Bounded pre-window port history preserves freshness (POSITIVE, with a proof)

- **Probe.** Give the observer the port readings u_x(−1 − s), …, u_x(0), that is, s ticks before the window. The K
  future readings keep full conditional rank in every case.
  - **R6:** L = 9, K = 4, s ≤ 6.
  - **Sweep:** 216 cases, q ∈ {3, 5, 7}, every nonzero α, K ≤ 4, s ≤ K + 2, L = 2(K + s) + 1.
- **Proof.**
  1. Φ is a bijection, so uniform counting is invariant under it.
  2. The state at time −1 − s is therefore uniform.
  3. Apply the report's one-port lemma to the window that starts there, with horizon K + s.
  4. The s history readings after the initial pair, together with the K future readings, are then jointly uniform
     and independent given that pair, whenever L > 2(K + s).
  5. So the future is independent of the whole history.
- **Extension.** This extends §5's readiness conditioning from C to s ticks of port history, provided history and
  horizon together fit the nonwrap condition.
- **Countercontrol.**
  - **On the L = 3 torus** the conditional future rank falls as 4, 3, 2, 1, 0, 0, … for s = 0, 1, 2, …. The finite
    return of N4 (Φ⁶ = −I) lets a long enough history determine the future.
  - **Neighbour access:** the six current neighbour values plus the history make the first future reading
    determined (rank 0).
  - **Duplicated port:** a duplicated port is caught (rank 3 of 6).
- **Assumption-watch marker.** The history budget s and the horizon K draw on the same nonwrap budget: L > 2(K + s)
  is sufficient for freshness. It is not shown necessary, so exceeding it does not by itself imply predictability.
  The L = 3 countercontrol shows that, under finite return, enough history can determine the future.

### 3. The report's limits are confirmed

- **Prior.** The product prior on the full Cartesian phase space is an explicit ensemble assumption. It is not the
  counting measure on a conserved-energy shell.
- **Interface.**
  - Herald and mark are two uncoupled components.
  - The call law is a sampler definition on i.i.d. field symbols.
  - Calls do not act on the field.
- **Not supplied.** The angular law μ_w, an emission/reset map, backreaction, access closure, continuous time, and
  composites. An arbitrary decoder of uniform symbols could produce any law, so the result does not select quantum
  probabilities.

## Relevance to the next target

The native wave rule supplies bounded i.i.d. resources from initial product counting. Within the nonwrap window it
also survives readiness conditioning, adaptive calls and bounded port history. What remains open is the physical
emission/readout map that turns such resources into the projected-area law, together with an account of which
records stay inaccessible. Uniform symbols alone do not select that map.
