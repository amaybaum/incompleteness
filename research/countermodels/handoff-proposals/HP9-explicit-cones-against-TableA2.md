# HP9 — countermodels → overview, equivalence, bridge, origin, via the coordinator: the round's explicit exotic cones against R6's Table A2, by operation

**From** `research/countermodels` (round 4, node C21, the recording obligation of addenda 1–3). **Proposed recipients**
the coordinator (overview: the eliminated-alternatives record and the stage-6 reassessment), `research/equivalence`,
`research/bridge` and `research/origin` (whoever sources (b) or its instances). Proposal only; the coordinator routes.
Written 2026-10-11T06:00Z (`date -u`).

## Statements, each with its label

1. **Standing.** `K384` (HO-24's cone, C11.5), `KC` (HO-25 item 1, C15.2), `Kk` (κ with G16, C16.4) and `K768` (C19.3)
   each receive, row by row against R6's Table A2 (the 199 items at L as R6 decided them for `K(Z_F)`), 118 SATISFIES,
   13 FAILS, 68 NOT REACHED. One difference from `K(Z_F)`: I3.148 (H2) at level (ii) holds for `Kk` only; `transposeW` moves
   the other three, which hold it at level (i). The 68 NOT REACHED rows are listed as R6 lists them; no theorem at L
   transfers one. Each cone satisfies the transferred pair-level premises at L (level (ii) for `Kk`, level (i) for the
   others). CONDITIONAL (H3 by Theorem S′: finite form C17.1 [D], compact form [W] for `Kk`; the entailments cited in
   NOTES-C21 for I3.133, I3.155, I3.160, I3.161; `pauliW` [D] as the table dictionary).
2. **By operation.** No FAILS row is satisfied by any of the four cones, but the operations through which the (b)-rows
   fail differ by cone. `KC` is invariant under `actC` and `actT` of every one-token Clifford rotation (`R_z(π)`, `R_z(π/2)`,
   `R_x(π)`, `R_x(π/2)`, `J`), under `cnot` and under SWAP: Table A2's witnesses for `K(Z_F)` (`actC cyc3`, `actC R_x(π/2)`)
   are invariances of `KC`, which fails IE1, IE1Drive, (b_S4), (b_n), (b_R1), (b_DJ) and K2's clause only at the
   non-Clifford rotations tested (`R_z(t₀)`, `R_x(t₀)` with `cos t₀ = 3/5`, `R_n(π/2)` with `n = (3, 0, 4)/5`, `R1`), on both
   tokens. `K384` and `K768` are invariant under every Clifford rotation of the target and keep Table A2's control witnesses.
   `Kk` is invariant under the kernel's drive flow `rot3 t` on the control for every `t` (KInfFoundations.lean:411, :449;
   the control phase flow lies in `G_κ`); IE1Drive fails there through `J` alone, (b_DJ) through the `R_x` flow and `J`.
   Every entry is cone invariance, decided exactly (INVARIANT, or MOVED with a witness `tr(g(d) P_w) = 1 − c < 0`,
   `P_w ∈ K`). CONDITIONAL (exact computation; the kernel's `actC`, `actT`, `cnot` re-checked against `Ad` on the basis
   tables).
3. **Weaker alternatives that do not force `Q3`** (with H1–H3, at the pair level): invariance under `Stab_C(Z⊗1)` (`K384`),
   under `Stab_C(±Z⊗1)` (`K768`), under the two-qubit Clifford group with SWAP (`KC`), under G16 with κ's gate flow and the
   drive flow on one token without `J` (`Kk`). These are countermodels to the named invariance hypotheses, not to OI's
   quantum conclusion: the NOT REACHED rows are untouched, and invariance is not availability. CONDITIONAL (as 1).
4. **Uniform FCC fails on all four through one mechanism.** With `Y = P_{Φ⁺}`, `F = P_χ` and `E = P_ψ`, `Ψ = H(ȲXᵀ)⁻¹` (`H`, `Ȳ`,
   `X` the coefficient matrices of the defect's state, of `y`, of `χ`), the contraction of `(Y, E, F)` is the effect `P_h`
   on the first pair, and `famI(d_h, Y, E, F) = 16 tr[(d_h⊗y)(e⊗f)] = 16|v|²(1 − c)/(|y|²|ψ|²|χ|²) < 0`; the only condition is
   that `y`, `ψ`, `χ` lie outside every cap. Exact on the four cones (`famI = −4/375`, `−125159/5319389250`, `−21/125`,
   `−4/9375`), with the operator route and the control `X = P_h` (`famI > 0`). CONDITIONAL ([W] identity; [X] instances).

## Assumption-watch marker proposed
- **"An exotic cone fails (b) at the operations Table A2 lists for `K(Z_F)`"** — false. Which operation moves a cone depends
  on the cone; the explicit cones of this round are invariant under every finite Clifford witness of Table A2 (`KC`) or
  under the drive flow on one token (`Kk`). A sourcing argument for (b) that reaches only finitely many Clifford rotations,
  or the drive flow without `J`, leaves an explicit exotic cone standing.

## What the recipients may not assume
Operational availability of any operation; that any cone "satisfies OI" or is "independent of OI"; anything about the 68
NOT REACHED rows beyond R6's record at L; that the items `pauliW` and `twistQ3` of I3.144 were examined separately; level-
(ii) versions of `K384`, `KC`, `K768` (not attempted); invariance under any continuous family other than `Kk`'s control
phase flow (a finite list refutes, it does not establish).

## Evidence
`NOTES-C21.md` (`f0d72871…`; S0, runs, one table per cone, the other 186 rows, standing), `experiments/c21_rows.py`
(`c4621d1e…`) / `.out` (`80d4d660…`): run 2 25/25 `VERDICT C21-EXACT` (run 1 25/25 kept; the run-2 amendment adds two
RECORD lines), replay identical; RESULTS rows C21.1, C21.1f. Inputs: R6's `REASSESSMENT.md` at `research/archive`
`4dc0321c` (sha256 `1ff62ad6…`, checked by the script); kernel lines at L as cited.
