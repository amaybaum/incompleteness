# HP-14 — HO-24's explicit cone along B10-5's tower: the first failing stage is n = 3

From `research/bridge`, node B17 (round 4). Proposed for the countermodels thread (author of HO-24) and the
equivalence thread (the `G₃₈₄` cone theorem). The coordinator routes.

## Statements and labels

Every statement is an invariance statement.

1. **The tower facts** (B17-1). HO-24's explicit exotic cone `K = (Q3 ∩ Z*) + cone Z` (`Z` the `G₃₈₄`-orbit of
   `d* = I − c*P_{h*}`, `c* = 401/400`) is invariant under B10-5's stages `G_1` and `G_2` — their generators lie in
   `G₃₈₄` modulo phases — and under no `G_n` with `n ≥ 3`. At `n = 3`, under `V = 1 ⊗ diag(1, e^{iπ/4})`, every one of
   the 192 orbit defects `d_j` is certified out of `K`: `P_{V h_j}` has squared overlap at most `400/401` with every
   orbit ray, so lies in `K*`, and pairs to `1 − c* = −1/400` with `V d_j V*`. Only the definition of the dual cone is
   used; no Theorem S′. Label: CONJECTURE (exact computation with controls, not kernel-checked).
2. **"A finite stage" defeated** (B17-1). Each finite stage has an explicit exotic invariant cone (HO-24 item 6), so no
   finite stage forces `Q3`, and the explicit Clifford cone does not persist along the tower. The tower's closure (B10-4's
   group) leaves a different exotic cone. Label: FAILED (kept with evidence) as a sufficient bridge; CONDITIONAL (on
   HO-24 items 4 and 6 and, for the closure, claim (D) through B7-2).
3. **Re-derived from HO-24** (controls): the Gaussian-rational lift of `G₃₈₄` has order 384 modulo `{±1, ±i}`; the orbit
   of `h*` has 192 rays; pairwise squared overlaps lie in `[25/2048, 13/16]` over 18336 pairs.

## Evidence

| item | pointer |
|---|---|
| script | `experiments/b17_tower.py` / `.out`, checks K1, K1b, S0-2, S0-3, K2 (no certificate at `n = 2`), K3 (none for `V = 1`), replay byte-identical; exact arithmetic over `ℚ(i)`, with `√2` only through integer comparisons of `p + q√2` |
| notes, results | `NOTES-B17.md`; `RESULTS.md` row B17-1 |

## What the recipient may assume

Items 1–3 at their labels: `n = 3` is the first stage of B10-5's tower under which HO-24's explicit cone is not
invariant, with an explicit exact certificate for every orbit defect.

## What the recipient may not assume

- that `K` is exotic or self-dual beyond HO-24 item 4's own label;
- anything about an exotic cone invariant under the whole tower other than through B10-4 and claim (D);
- a kernel check.
