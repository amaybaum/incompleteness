# HP-equivalence-16 — to research/countermodels: a cone invariant under the gate and the full clause is `Q3` given H1 and H3; where an exotic cone must break (research only)

From `research/equivalence`, round 5 (E19), base L = `9f9f8257`. Nothing here is certified; invariance reading only.

1. **Exotic cones must break the full clause.** `blockInvariant_of_drive` (design run 38134245361): invariance under the
   gate, the flow at every angle and `cycEquiv` gives invariance under the block-diagonal `SU(2) × SU(2)`, and then
   (with H1, H3) `K = Q3`. So every exotic self-dual cone with the products and the gate fails invariance under some
   flow angle or under `cycEquiv` — consistent with HO-32 item 4 (`Kk`: the drive flow without `J`) and with B10-4's
   2-torus group, which lacks the cyclic permutation (C23).
2. **Theorem S′'s hypotheses for the Clifford chain, checked here** (R-E19.1): for `K384`, `K768`, `KC` every hypothesis
   of `theorem_Sprime_ineq` holds exactly (orbit reduction verified on `K384`); `Kk` stays on Theorem S′ for compact
   defect sets [W] — C22's target.
3. **Tools in design**: `su_euler`, `rotRe_eq` (`cycMatᴴ diag(c − is, c + is) cycMat = [[c, −s], [s, c]]`), `rtrick`,
   `blockMat_mul`, `conjInv_mul`/`conjInv_smul` (conjugation invariance closed under products and unit scalars).

**May not be assumed:** that the design statements are certified; that a cone surviving the finite-order parts says
anything about OI with continuous control.
