# REC-1 P0 r2: working notes (writer)

## Method
- Hand reasoning only. No script on any OI rule, no Lean, no repository edit, no commit, push or
  post.
- The r2 file was assembled from r1's unchanged sections (title, header, §1–§3, N1, N2) plus
  rewritten sections, using `cat`, `sed` and `grep` on text files only.
- Sources were re-read at the cited lines from the read-only `git show` copies made in r1, which the
  reviewer found byte-identical. The lines were:
  - OA3:101–102, :120–123, :410–416, :418–445, :466–469, :474–475;
  - OA2:502, :534;
  - OA1:131;
  - r7:254–256, :287–290, :299–300, :309–311, :319–321, :335–338.

## Re-derivation of the reviewer's countercontrol (N8.2(b))
- Shift: `s0(t+1) = s2(t)`, `s1(t+1) = s0(t)`, `s2(t+1) = s1(t)`. With `s0 = 0`, `s1 = y` and
  `s2 = x`, `s0` runs `0, x, y, 0, x, y`.
- Ring: `r_0(t+1) = r_L(t) + s0(t)`. The feeder cells `r_L`, `r_{L−1}`, `r_{L−2}` are designated 0;
  `r_{L−3} = u` and `r_{L−4} = u′` are uniform. So `r_0` runs `0, 0, x, y, u, u′+x`.
- `V(5)`: `s0 = y`, `r_0 = u′+x`, `r_1 = u`, `r_2 = y`, `r_3 = x`, then zeros.
  - It recovers `x`, `y`, `u` and `u′`, and hence every earlier `V(τ)`. So (H4) holds literally.
- Labels at tick 5: `r_2` and `r_3` (the retained herald records).
- Label-free content: tick 4 `(s0, r_0) = (x, u)`; tick 5 `(y, u′+x, u)`.
  - `u′` appears only inside `r_0(5)`, so `x` is not label-free-held at 5. `A ∼ B`, as checked on all
    single-tick and composite effects.
- Herald held at `t_p = 3`: `r_0(3) = y`, `r_1(3) = x`.
- Not R-lin: the ring rule has no second-order form and no nearest-neighbour sum.

## Reading decisions in r2
1. **Use time of a preparation herald.** Two readings are carried: the handoff `t_p` (as OA3:410–413
   uses `t_h`), or each effect's read. Composability holds under both (N3). Only reading B combined
   with use at each effect's read produces an out-of-form list.
2. **The r7 reading conflict** (clause versus r7:287–290, :299–300, :320–321) is left to the owner,
   as instructed. §6 tabulates the outcome under each reading. Under every reading the outcome is
   not a pass.
3. **(LF)** is cell-based. Its functional variant (label-free as functionals) was not pursued. Under
   a functional reading Instance II's status could change; Instance I's does not.

## Next decisive step (as recorded in §7)
- C3 for R-lin with (xiii): decide whether a second-order nearest-neighbour rule can carry
  measurement-stage retention only through herald-label cells, as the ring recorder does. Either
  realize this (an in-class contextual counterexample) or exclude it (a classicality proof for the
  class).
- Paper-only. Hand exploration of small rings is possible but was not attempted in this unit.

## Not done
- No new instance under R-lin was attempted for C3 beyond Instances I and II, which have one
  measurement tick each.
- The authorization comment and the safeguard text were taken as relayed and were not re-fetched.
