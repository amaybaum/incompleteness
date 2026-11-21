# NOTES (r1) for C3-RLIN-r1.md

**Standing.** Working notes for the paper-only C3 check. WIP / UNVERIFIED, unreviewed. Hand
reasoning only.

## Sources read

- On `main` at `c3b5f37a` (read-only worktree of branch `research/c3-rlin-xiii-1169-20261113`):
  `papers/Main.md` (ledger, Main:724; §3.2 rule, Main:292–294); OA-1 r5, OA-2 r4, OA-3 r4 (definitions
  cited in C3-RLIN-r1 §1); `TUNE-1-STEP2-PROPOSAL.md` (rule class, P:77–89).
- Off `main`, fetched by branch name without `--depth`:
  - `research/rec-1-1169-20261113` at `2a9f10ba`: `REC-1-P0-r3.md`, `REC-1-P0-CONFIRM-r3.md`,
    `REC-1-r8.md`, `REC-1-P0-REVIEW-r1.md`, `REC-1-P0-NOTES-r2.md`, and grep hits in the other REC-1
    responses and confirmations.
  - `research/synthesis-1169-20261113` at `9eeee392`: `SYNTHESIS-r3.md` (MM-2, T5, SQ3),
    `CONFIRM-r2.md`, `CONFIRM-r3.md` (grep only).
- GitHub API: #1169 comment 6863414487 (owner decision), #1268 review 5892912758.
- Commands: `git fetch`, `git show`, `git ls-tree`, `git rev-parse`, `grep`, `sed`, `cat -n`, `curl`
  (GitHub API, read-only). No script was written or run; the optional checkers were not run (their
  scope is the manuscripts).

## Reading decisions

1. **Rule class.** R-lin with (xiii), as P0 (P0:350–352) and review 5892912758 read OBL-SP's class.
   Owner question 4 records the alternative (all of ledger (vii)).
2. **Carrier and dimension.** P0's instances and OA-2's N₁ use rings; TUNE-1 and ledger (x) name the
   simple cubic lattice. The proof (N2) is dimension-free. W1 is checked in `d = 1` and lifted to
   `d = 3`; W2 is `d = 1`.
3. **Cells.** Slots, as in P0's instances. Site-level observers (Main:292–294) are covered by N2 and,
   for R3 only, by W2.
4. **Label delimitation after the use time.** Not defined by C-PM, OA3:101–102 or the herald typing.
   Four readings are carried (R1, R2(i), R2(ii), R3), and R0 is excluded by the precedents. None is
   adopted. Choosing one is an owner decision (owner question 1); doing it here would be a rule
   change.
5. **Full retention** is checked at every tick (nesting of `V(τ)` in `V(τ′)`), which is at least
   what (H4) and retention-type (V-ii-H) require.

## Hand computations

### 1D formulas (all `Y` used below are 0 except where stated)

From `y_i(t+1) = x_i(t)`, `x_i(t+1) = x_{i−1}(t) + x_{i+1}(t) − y_i(t)`:
- `x_i(1) = X_{i−1} + X_{i+1} − Y_i`, `y_i(1) = X_i`;
- `x_i(2) = x_{i−1}(1) + x_{i+1}(1) − X_i = X_{i−2} + X_i + X_{i+2} − Y_{i−1} − Y_{i+1}`;
- `y_i(2) = x_i(1)`.
With `Y ≡ 0`, a single `X_j` gives `x_i(t) = X_j` for `|i−j| ≤ t`, `|i−j| ≡ t (mod 2)`, else 0. This
was checked step by step for `t = 1, 2, 3` (t = 3: `x_{±1}(3) = 2X − X`, `x_{±3}(3) = X`,
`x_0(3) = 0`, `x_{±2}(3) = 0`).

### W1 (ring `ℤ/16`)

Free: `X_0 = n`, `X_2 = a`, `X_7 = b`, `X_9 = m`, `Y_5 = p`. Row by row:
- `y_0`: `Y_0 = 0`; `X_0 = n`; `x_0(1) = X_{−1} + X_1 − Y_0 = 0`.
- `x_1`: `X_1 = 0`; `X_0 + X_2 − Y_1 = n + a`; `X_{−1} + X_1 + X_3 − Y_0 − Y_2 = 0`.
- `x_2`: `a`; `X_1 + X_3 − Y_2 = 0`; `X_0 + X_2 + X_4 − Y_1 − Y_3 = n + a`.
- `y_3`: `0`; `X_3 = 0`; `x_3(1) = X_2 + X_4 − Y_3 = a`.
- `x_4`: `0`; `X_3 + X_5 − Y_4 = 0`; `X_2 + X_4 + X_6 − Y_3 − Y_5 = a − p`.
- `x_7`: `b`; `X_6 + X_8 − Y_7 = 0`; `X_5 + X_7 + X_9 − Y_6 − Y_8 = b + m`.
- `y_7`: `0`; `b`; `x_7(1) = 0`.
- `y_8`: `0`; `0`; `x_8(1) = X_7 + X_9 − Y_8 = b + m`.
- `y_10`: `0`; `0`; `x_10(1) = X_9 + X_11 − Y_10 = m`.
- Where the hidden variables go: `p` reaches `x_5(1)`, `x_4(2)`, `x_6(2)`, `y_5(2)`, of which only
  `x_4 ∈ V`. `m` reaches `x_8(1)`, `x_10(1)`, `y_9(1)` (none in `V` at tick 1). `n` is outside `V(0)`.

Label sets:
- R2(i): `Lab(0) = V`; `Lab(1) = {y_1, y_2, y_4, y_7, x_3}`; `Lab(2) ∩ V = {y_3}`.
- R2(ii): `Lab(0) = {x_2, x_7}`, `Lab(1) = {y_2, y_7}`, `Lab(2) = ∅`.
- R1 as R2(ii) here.
- R3: `{y_7}` at tick 1 and `{y_3}` at tick 2.

### W1 in `d = 3`

Transverse neighbours of a chain site `i` have `x(1) = X_i`, so each chain `x` cell at tick 2 gains
`4X_i`:
- `x_1(2) = 0`;
- `x_2(2) = (n+a) + a + 4a − a = n + 5a`;
- `x_4(2) = a − p` (`X_4 = 0`);
- `x_7(2) = (b) + (b+m) + 4b − b = 5b + m`.
Tick-1 cells and `y` cells are unchanged. Composites: `n + a = x_2(2) − 4a` is label-free-held only if
`4 ≡ 0 (mod q)`; either way every composite law depends on `b` only.

### W2 (ring `ℤ/24`, site level)

Distances `(d to 0, d to 2)` and `(d to 10, d to 14)` give the `(y, x)` table:

| site | t0 | t1 | t2 | t3 |
|---|---|---|---|---|
| −1 | (0,0) | (0,n) | (n,0) | (0,n+a) |
| 1 | (0,0) | (0,n+a) | (n+a,0) | (0,n+a) |
| 2 | (0,a) | (a,0) | (0,n+a) | (n+a,0) |
| 5 | (0,0) | (0,0) | (0,0) | (0,a) |
| 10 | (0,b) | (b,0) | (0,b) | (b,0) |
| 11 | (0,0) | (0,b) | (b,0) | (0,b+m) |
| 15 | (0,0) | (0,m) | (m,0) | (0,m) |

- R3 labels: tick 1 `y_2`, `y_10`, `x_11`; tick 2 `x_10`, `y_11`; tick 3 `x_5`, `y_10`.
- R2(i): `Lab(1)` is the `y` cells of `V`'s sites and `Lab(2) = ∅`.
- Cones reach sites −4…18 by `t = 3`, so a ring of 24 avoids wrap-around.

### R2(ii) attempt (N6)

At `T = 2`, `Y_3` enters only `x_3(1)` and, through it, `y_3(2)`, `x_2(2)`, `x_4(2)`, always as
`X_2 + X_4 − Y_3`. With `X_2 = a`, `X_4 = a′`, `Y_3 = a″` as herald cells, nesting needs `a″`
individually at tick 2, hence `a` individually. `a`'s other tick-2 occurrences (`x_0(2)`, `y_1(2)`,
`x_2(2)`, `x_4(2)`) carry fresh masks, which appear only in label-free cells. So `a` is label-free at
`T`. Variants tried: masks on `x_4(2)` through `Y_5` or `X_6`, and retention of `a′` through `x_6(2)`
or `y_5(2)`. Each exposed the mask or `a` once the herald fixed `a′`, `a″`.

## Not done

- R2(i) in `d = 3` and at site level; R2(ii) beyond the one geometry.
- No check of whether a delimitation other than R0–R3 agrees with every precedent.
- No reading adopted; no record or manuscript edited; nothing committed, pushed or posted.
