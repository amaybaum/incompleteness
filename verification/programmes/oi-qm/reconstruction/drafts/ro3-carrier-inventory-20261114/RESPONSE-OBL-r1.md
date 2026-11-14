# OBL-RO3-2: response to the review of r1

**UNREVIEWED.** This file gives the writer's disposition of each finding in `REVIEW-OBL-r1.md`
(ACCEPT WITH CHANGES, at `76ca4c3d`).

- The changes are in `OBL-RO3-2-r2.md` and, for m8 only, in `RO3-INVENTORY-r4.md`.
- `OBL-RO3-2-r1.md` and `RO3-INVENTORY-r3.md` are left unchanged.
- Each finding was checked at `main` `dfeec843` with `git show origin/main:<path>` before it was
  applied, or by a paper check where the finding is mathematical.
- Paper-only: nothing was built or run.

## R1 (required). §3.2 overstated the recurrence consequence

**Disposition: accepted. §3.2 is rewritten, and every place that rests on it is updated.**

**Checked.**
- **The fixed-point example.** For `d = 2`, `F(u, v) = (u, v)` gives `v = u` and `Av − u = u`, that
  is `Au = 2u`. Solving for `u(n_1 + 1, n_2)` gives a recursion that runs uniquely forward and
  backward from the columns `n_1 = 0, 1`. So `Fix(F) ≅ (F_p^Z)^2` is uncountable, and an aperiodic
  column 0 gives a fixed point that is not spatially periodic. At `p = 2` the recursion still holds,
  with coefficient `2α^{-1} = 0`.
- **`d = 1`.** The same recursion has two initial values, so `Fix(F^n)` is finite and
  shift-invariant, and each of its points is spatially periodic.
- **Null set.** `Fix(F^n)` is closed and `F`-invariant. Ergodicity, which follows from Step 8, gives
  measure 0 or 1. Measure 1 would make the set all of `X`, because `μ` has full support, and that
  contradicts `F^n ≠ id`.
- **Poincaré recurrence.** It holds `μ`-almost everywhere: a measure-preserving map of a compact
  metric probability space.
- **r1's error.** "They form a countable set" covered only the spatially periodic points, and the
  heading "Refuted on `X`" was stronger than what was proved.

**Applied.**
- §3.2 is retitled "`F` has infinite order; periodic points are `μ`-null". It states that Poincaré
  recurrence holds almost everywhere, gives the example and the `d = 1` case, proves that periodic
  points are null, and says what 3.2 does not claim.
- The summary row in §6 is updated to match.
- §4.1 now gets the torus's null measure from its finiteness, and cites 3.2 only for the null set of
  periodic points.

**Consequences elsewhere.**
- The other places that use 3.2 were checked: §3.4, §3.5 and §7. None rests on the overstatement.
- In the inventory, the only related statement is r3 §1.1 I-qloc, "`φ^L ≠ id` for every `L ≥ 1`",
  which remains true. r3 therefore needs no change for R1. r4 exists only for m8 and says so.

## Minor

- **m1. Order of the constant-`a` map.** Accepted. Checked: at `p = 2`, `−u = u`, so the map is the
  swap, of order 2. Row corrected.
- **m2. SM:296's hypothesis.** Accepted.
  - Checked at `papers/SM.md:296`: "Let `q=p` be prime with `p∤L`, let `L≥2`".
  - §4.1 now states the `p ∤ L` case from SM and the `p | L` case by finiteness of the group.
  - The countercontrol row cites both cases.
- **m3. Step 4(b) applied beyond `X`.** Accepted. A scope note after Step 4 says that the proof uses
  only two facts: Haar orthonormality of characters, and characters mapping to characters under a
  continuous automorphism. It therefore holds on every compact abelian group. The countercontrol rows
  and §4.1 refer to that note.
- **m4. Rooted conventions.** Accepted.
  - §3.1 now says that its argument is in the cell-conditioned convention.
  - It says that Main's convention coincides with it for `π = res_Λ`.
  - It says that a coarse-grained readout with unequal fibres has no root-shared prior in Main's
    product form.
- **m5. "Refuted" and the near-return variant.** Accepted.
  - §3.3 says "unavailable": the route's hypothesis fails, and the route itself is not refuted.
  - It adds the continuous-time near-total return of `papers/Main.md:155`. Checked: Main:155 requires
    a common time at which every root's return set has measure `> 1 − δ`.
  - Mixing excludes such a return at every sufficiently late time, since `Γ_t(a, a) → μ(C_a) < 1`. A
    return at a bounded time is left open.
  - The status of P-indivisibility itself is unchanged: open.
- **m6. (ii-b) can be checked.** Accepted. (ii-b) is upgraded to "proved on paper from the
  definitions on `main`; not kernel-checked".
  - Checked: `heis Φ T = permOpInv Φ * T * permOp Φ` (`QuasilocalAlgebra.lean:999`); `permOp` is
    `Finsupp.lmapDomain` along `φ` (:966); `permOpInv_apply` gives `(permOpInv f)(t) = f(φ t)` (:981).
    Hence `heis Φ D_f = D_{f ∘ φ}`.
  - Also checked: `emb Λ X` (:242–245) sends `δ_s` to `Σ_f X f (glob Λ s) δ_{patch Λ s f}`, which for
    a diagonal `X` is a multiplication operator. This assumes `patch Λ s (glob Λ s) = s`, an identity
    named and not looked up.
  - With `heisQ_stage` (:1274) and (ii-a), the diagonal case reduces to Step 2.
  - §5's closing note and §7 now say that the rooted laws need (ii-a) and (ii-b), and that only
    full-state statements need (ii-c), which stays open.
- **m7. The unmet mandate item.** Accepted. §1 now tells the owner plainly that the requirement to
  verify the Halmos and Rokhlin criteria from primary sources is not met. It gives the reason, says
  why the result does not depend on them, and names the textbook treatments the reviewer mentions.
  The writer did not consult those either.
- **m8. Inventory wording.** Accepted.
  - Checked: r3 2.5 names one route after the N3 rewrite and then says "Neither route is checked
    here".
  - `RO3-INVENTORY-r4.md` changes that sentence to "This route is not checked here" and adds a header.
    Nothing else differs from r3, and r3 is unchanged.

## Unchanged

- The review confirms Steps 1–8, §3.1, §3.4, §4.1 apart from m2, the countercontrols apart from m1,
  and (i), (ii-a), (ii-c) and (iii) of §5. These are not altered.
- The mixing theorem is restated with the same scope: prime `p`, `α ≠ 0`, `d ≥ 1`, Haar measure.
- It is not a quantum realization, and EXACT stays open.
