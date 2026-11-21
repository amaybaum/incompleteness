# NOTES (r3) for C3-RLIN-r3.md

**Standing.** Working notes for the paper-only C3 check, r3. WIP / UNVERIFIED, unreviewed. Hand
reasoning only. r3 changes only the title, this paragraph and §6's first bullet (the nit of
`CONFIRM-r2.md`); the rest is NOTES-r2 unchanged.

## 0. Sources and commands

- On `main` at `c3b5f37a` (read-only worktree): `papers/Main.md` (Main:292–294, :724); OA-1 r5,
  OA-2 r4 (C-PM OA2:110–124; Claim 2 OA2:443–458), OA-3 r4; `TUNE-1-STEP2-PROPOSAL.md` (P:77–89).
- Off `main`, fetched by branch name without `--depth`:
  - `research/rec-1-1169-20261113` at `3a3aa146`. P0, P0C, P0R and P0N have the same blobs as at
    `2a9f10ba`. `REC-1-r9.md` (blob `945b7982`) was compared with `REC-1-r8.md` by `diff`: only the
    title, the revision line (r9:18–22), P5 (r9:371) and §6 provenance rows differ; the cited
    passages move by +4 lines.
  - `research/synthesis-1169-20261113` at `9eeee392`: `SYNTHESIS-r3.md`.
  - `research/c3-rlin-xiii-1169-20261113` at `a03af682`: `REVIEW-r1.md`, identical to the working
    copy (`diff` empty).
- GitHub API, read-only: #1169 c.6863414487; #1268 review 5892912758; #1268 c.6860582570 (owner L
  decision, `amaybaum`, 2026-11-13T17:47:34Z). The last also records that, at the time, the C3 check
  was "proposed and **not authorized**". The later #1169 c.6863414487 authorizes it.
- Commands: `git fetch`, `git show`, `git ls-tree`, `git log`, `git rev-parse`, `diff`, `grep`, `sed`,
  `cat -n`, `curl`. No script was written or run.
- The optional checkers were not run here. The reviewer reports `claims_check`, `staleness_check`,
  `voice_check` and `artifact_placement_check` OK at `00c84af2` (RV:31–33); their scope does not
  include these files.

## 1. 1D formulas

From `y_i(t+1) = x_i(t)`, `x_i(t+1) = x_{i−1}(t) + x_{i+1}(t) − y_i(t)`:
- `x_i(1) = X_{i−1} + X_{i+1} − Y_i`, `y_i(1) = X_i`;
- `x_i(2) = X_{i−2} + X_i + X_{i+2} − Y_{i−1} − Y_{i+1}`;
- `y_i(2) = x_i(1)`.

With `Y ≡ 0`, a single `X_j` gives `x_i(t) = X_j` for `|i−j| ≤ t`, `|i−j| ≡ t (mod 2)`, else 0.
Checked for `t = 1, 2, 3`:
- `t = 3`: `x_{±1}(3) = 2X − X`, `x_{±3}(3) = X`, `x_0(3) = 0`, `x_{±2}(3) = 0`.

On the support this is a multi-tick exact copy (C3-RLIN-r2 N1).

## 2. Precedents under R1v and R2(iii), by hand

"Fixed" means the same known value under every admitted procedure. Settings and labels are never
fixed.

**Instance II** (P0:402–411). Ring of 4. Designated: `y₀ = 0`, `x₁ = 0`, `y₁ = 0`, `x₂ = c` (setting).
Free: `x₀ = w`, `x₃ = u`, `y₂`, `y₃`. `V = {y₀, x₀, x₁}`, `t_p = 0`, `Lab(0) = {x₀}`.
- `y₀(1) ← x₀(0)`: one input, a label. A label under R1v and R2(iii).
- `x₁(1) = x₀(0) + x₂(0) − y₁(0)`: `y₁(0)` is dropped and `x₀`, `c` remain. Two inputs, so label-free
  under R1v. `c` is not a label, so label-free under R2(iii).
- `x₀(1) = x₁(0) + x₃(0) − y₀(0)`: only `u` remains, not a label. Label-free under both.

Reproduced.

**Instance I** (P0:392–400). Designated: `x₀ = x₂ = 0`, `x₁ = c`, `y₀ = p` (label), `y₂ = 0`. Free: `x₃ = u`,
`y₁`, `y₃`. `V = {x₀, x₂}`, `Lab(0) = {y₀}`.
- `x₀(1) = c + u − p`: three non-fixed inputs, not all labels. Label-free under both.
- `x₂(1) = c + u`: label-free under both.

Reproduced.

**N8.2(b)** (P0:318–349). `t_p = 3`, `Lab(3) = {r_0, r_1}` (`y`, `x`). `s0(3) = 0` is fixed (it is
`s0(0)`, designated).
- Tick 4:
  - `r_1(4) ← r_0(3)` and `r_2(4) ← r_1(3)`: labels.
  - `s0(4) ← s2(3)`, and `s2(3) ∉ Lab(3)`: label-free (`x`).
  - `r_0(4) = r_L(3) + s0(3)`: `s0(3)` is dropped; `r_L(3) = u` is not a label. Label-free (`u`).
- Tick 5:
  - `r_2(5)`, `r_3(5)`: labels.
  - `r_1(5) ← r_0(4)`: label-free.
  - `r_0(5) = r_L(4) + s0(4) = u′ + x`: two non-fixed non-label inputs. Label-free.
  - `s0(5) ← s2(4)`, not a label: label-free.

Label-free content `(x, u)` at tick 4 and `(y, u′+x, u)` at tick 5, as P0R:141–144. Reproduced under
both readings.

**R3 and settings.** R3 fails N8.2(b) under either treatment of settings. It fails Instance II only
if the measurement setting `c` counts among the values a label may depend on.

## 3. W1 label sets, every cell of `V`

Non-fixed cells at tick 0: `x_0` (`n`), `x_2` (`a`), `x_7` (`b`), `x_9` (`m`), `y_5` (`p`).

**Tick 1, R1v.**
- `y_2 ← x_2` and `y_7 ← x_7`: labels.
- `x_3(1)`: remaining inputs `{x_2}`, so a label (`a`). `x_6(1)`: `{x_7}`, a label (`b`).
- `x_1(1)`: `{x_0, x_2}`, label-free. `x_8(1)`: `{x_7, x_9}`, label-free.
- `x_5(1)`: `{y_5}`, not a label (`−p`). `x_{−1}(1)`: `{x_0}`. `x_10(1)`: `{x_9}`.
- `y_1`, `y_4` have no non-fixed input and hold 0.
- In `V`: `y_0 = n` and `x_1 = n+a` are label-free; `y_7 = b` is a label. `x_2`, `y_3`, `x_4`, `x_7`, `y_8`,
  `y_10` hold 0 with no non-fixed input.

**Tick 2, R1v.**
- `y_3 ← x_3(1)`: a label (`a`).
- `x_2(2)`: inputs `{x_1(1), x_3(1), y_2(1)}`, label-free (`n+a`).
- `x_4(2)`: `{x_3(1), x_5(1)}`, label-free (`a−p`); `y_4(1) = 0` is dropped.
- `x_7(2)`: `{x_6(1), x_8(1), y_7(1)}`, label-free (`b+m`).
- `y_8 ← x_8(1)`: label-free. `y_10 ← x_10(1)`: label-free.
- `y_0`, `x_1`, `y_7` have no non-fixed input (0).

**R2(iii).** Tick 1 as R1v. At tick 2:
- `x_2(2)` reads the non-label `x_1(1)`; `x_4(2)` reads `x_5(1)`; `x_7(2)` reads `x_8(1)`. So `Lab(2) ∩ V = {y_3}`.
- Outside `V`, `x_5(2)` (remaining input `{x_6(1)}`) is a label holding `b`.

**Comparison with the reviewer's `Lab(1)`.** The reviewer's set `{y_1, y_2, y_4, y_7, x_3, x_6}` adds
`y_1` and `y_4`. Those two have only a fixed input. Under "drop fixed inputs" they have no remaining
input. Their content is 0, so either convention leaves the analysis unchanged.

**`d = 3`, R1v and R2(iii).**
- Transverse cells: `x_{2+e⊥}(1) = a` and `x_{7+e⊥}(1) = b` are labels, with one non-fixed input each;
  they are not in `V`.
- `x_2(2) = (n+a) + a + 4a − a = n + 5a`: several inputs, label-free.
- `x_4(2) = a − p` and `x_7(2) = 5b + m`: label-free.
- `x_1(2)`: every input is fixed, so it holds 0.

**`d = 3`, R2(i), enlarged `V`.** The four transverse `x` cells of site 3 hold 0 at ticks 0 and 1.
- At tick 2, the transverse cell `3+e⊥` has neighbours with `x(1)` values: `x_3(1) = a`;
  `x_{2+e⊥}(1) = a`; `x_{4+e⊥}(1) = 0`; the others 0. Its own `y(1)` is `X_{3+e⊥} = 0`. So it holds `2a`.
- `x_{2+e⊥}` is not in `Lab(1)`: its `y` and its other `x` neighbours are not in `V`. So `2a` is
  label-free, and it is 0 at `q = 2`.
- `x_3`: all of `y_3`, `x_2`, `x_4` and the four transverse cells are in `V`, so `x_3 ∈ Lab(1)` and
  `y_3(2) ∈ Lab(2)`.
- At `q = 2`, the label-free cells at tick 2 are `(n+a, a−p, 0, b+m, b+m, m)`, the same content as in
  `d = 1`.

## 4. W2′ (ring `ℤ/24`, site level)

Free: `X_0 = n`, `X_2 = a`, `X_10 = b`, `X_12 = r`, `X_14 = m`; all `Y` = 0.

Distances from the free sites (0, 2, 10, 12, 14) to each site of `V`:
- −1: (1, 3, 11, 13, 15)
- 1: (1, 1, 9, 11, 13)
- 2: (2, 0, 8, 10, 12)
- 5: (5, 3, 5, 7, 9)
- 8: (8, 6, 2, 4, 6)
- 10: (10, 8, 0, 2, 4)
- 11: (11, 9, 1, 1, 3)
- 15: (15, 13, 5, 3, 1)

`(y, x)` by tick:

| site | t0 | t1 | t2 | t3 |
|---|---|---|---|---|
| −1 | (0,0) | (0,n) | (n,0) | (0,n+a) |
| 1 | (0,0) | (0,n+a) | (n+a,0) | (0,n+a) |
| 2 | (0,a) | (a,0) | (0,n+a) | (n+a,0) |
| 5 | (0,0) | (0,0) | (0,0) | (0,a) |
| 8 | (0,0) | (0,0) | (0,b) | (b,0) |
| 10 | (0,b) | (b,0) | (0,b+r) | (b+r,0) |
| 11 | (0,0) | (0,b+r) | (b+r,0) | (0,b+r+m) |
| 15 | (0,0) | (0,m) | (m,0) | (0,r+m) |

**R1v.** `Lab(0) = {x_2, x_10}`.
- `Lab(1) = {y_2, y_10, x_3, x_9}`. `x_11(1)` has inputs `{x_10, x_12}` and is label-free.
- Tick 2: `x_8(2)` has remaining input `{x_9(1)}` (`x_7(1)`, `y_8(1)` fixed), so it is a label. `x_4(2)` has
  `{x_3(1)}`, a label. `x_10(2)` has `{x_9(1), x_11(1), y_10(1)}` and is label-free.
- Tick 3: `x_5(3)` has `{x_4(2)}`, a label. `y_8(3) ← x_8(2)`: a label. `y_10(3) ← x_10(2)`: label-free.
  `x_11(3)` and `x_15(3)` are label-free.

**R2(iii).** The same labels in `V`. `x_9(1)`, `x_8(2)`, `x_4(2)`, `x_5(3)` have every remaining input
labelled. `x_10(2)` and `x_11(3)` each read a non-label.

**R3.** The pure-herald cells are `y_2(1)`, `y_10(1)`, `x_8(2)`, `x_5(3)`, `y_8(3)`: the same labels.

**Other readings.**
- R1s: `Lab(1) ∩ V = {y_2, y_10}`; `Lab(2) = ∅`.
- R2(i): `Lab(1)` is the `y` cells of `V`'s sites, since no `x` cell has all its inputs in `V`;
  `Lab(2) = ∅`.
- R2(ii): `Lab(1) = {y_2, y_10}`; `Lab(2) = ∅`.

**r1's W2.** Without site 8 and `r`, `x_10(2) = b` has three non-fixed inputs, so under R1v it is
label-free. With `a` label-free at tick 2, the fragment is classical under R1v. Adding `r` masks
`x_10(2)`. Adding site 8 restores retention of `b` at ticks 2 and 3 through labels.

## 5. R2(ii) attempt (unchanged from r1)

At `T = 2`, `Y_3` enters only `x_3(1)` and, through it, `y_3(2)`, `x_2(2)`, `x_4(2)`. It always appears
as part of `X_2 + X_4 − Y_3`. Nesting needs `a″` individually, hence `a` individually, through a
label-free cell whose mask is fresh. So `a` is label-free at `T`. The variants tried (masks through
`Y_5` or `X_6`; retention of `a′` through `x_6(2)` or `y_5(2)`) each exposed the mask or `a`.

## 6. Not done

- R2(i) in `d = 3` for `q ≠ 2` (at `q = 4` the label-free cell `2a` separates `a = 0` from `a = 1`); R2(i) at site level beyond W2′; R2(ii) beyond one geometry.
- R1s with use at each effect's read.
- W2′ in `d = 3`.
- No check of whether further delimitations agree with every precedent.
- No reading adopted; no record or manuscript edited; nothing committed, pushed or posted.
