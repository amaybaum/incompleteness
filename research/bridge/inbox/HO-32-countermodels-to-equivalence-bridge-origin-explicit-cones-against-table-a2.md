# HO-32 (v1) — countermodels → equivalence, bridge, origin: the round's four explicit exotic cones against the stage-6 Table A2, by operation; what each refutes and what it leaves open

**From** `research/countermodels` (round 4, node C21, the recording obligation of the coordinator's round-4 addenda).
**To** `research/equivalence`, `research/bridge` and `research/origin` (whoever sources (b) or its instances). Written
by the coordinator from the source thread's committed record; version 1, 2026-10-11. Inventory ids are the stage-6
inventory's (`research/archive/pt/I3/INVENTORY.md` at `4dc0321c`); Table A2 is `pt/R6/REASSESSMENT.md` (sha256
`1ff62ad6…`) at the same commit.

## Statements and labels

1. **Standing** (C21.1). `K384` (HO-24's cone, C11.5), `KC` (HO-25 item 1, C15.2), `Kk` (κ with G16, C16.4) and `K768`
   (C19.3, HO-31) each receive, row by row against Table A2's 199 items at L as R6 decided them for `K(Z_F)`:
   **118 SATISFIES, 13 FAILS, 68 NOT REACHED**. One difference from `K(Z_F)`: I3.148 (H2) at level (ii) holds for `Kk`
   only; `transposeW` moves the other three, which hold it at level (i). Each cone **satisfies the transferred
   pair-level premises at L** (level (ii) for `Kk`, level (i) for the others) — never "satisfies OI", never
   "independent of OI". Label: CONDITIONAL (H3 by Theorem S′: finite form C17.1 [D] (HO-30) for `K384`, `KC`, `K768`,
   compact form [W] for `Kk`; the entailments cited in NOTES-C21 for I3.133, I3.155, I3.160, I3.161; `pauliW` [D] as the
   table dictionary).
2. **The premises, in three kinds** (the coordinator's reading of the C21 tables, at the owner's request). *Satisfied
   directly at the cone's level:* the 29 K-dependent SATISFIES rows — the twelve `cone` rows by exact computation (H1
   by the Schmidt bound, (CC) on every pair) with S′ for H3 and `cnot` invariance; I3.148 at level (i) or (ii) as above;
   the `d4v` rows vacuously. *Transferred by a proved bridge:* the 13 `b1` rows through `K ⊆ maxCone` (H1 and H3;
   `maxCone` the dual of the product effects, CompositeDimension.lean:186 [K]); the `kthm` row I3.44 through
   `no_candidateCone_cnot_reflY` (K2Guard.lean:143 [K]); the 89 K-independent rows carry Table A2's verdict unchanged.
   *Never reaching the model's level:* the 68 NOT REACHED rows (M-level and H-level items); R6 found no theorem at L
   transferring any of them to the pair cone and nothing at L has changed. *Failed:* the 13 FAILS rows, each a
   hypothesis (do-not-assume items, [D] four-token hypotheses, PT-record candidates), none a theorem at L.
3. **By operation** (C21.1, C21-3). No FAILS row is satisfied by any of the four cones, but the operations through
   which the (b)-rows fail differ by cone. `KC` is invariant under `actC` and `actT` of every one-token Clifford
   rotation (`R_z(π)`, `R_z(π/2)`, `R_x(π)`, `R_x(π/2)`, `J`), under `cnot` and under SWAP: Table A2's witnesses for
   `K(Z_F)` (`actC cyc3`, `actC R_x(π/2)`) are invariances of `KC`, which fails IE1, IE1Drive, (b_S4), (b_n), (b_R1),
   (b_DJ) and K2's clause only at non-Clifford rotations (`R_z(t₀)`, `R_x(t₀)` with `cos t₀ = 3/5`, `R_n(π/2)` with
   `n = (3, 0, 4)/5`, `R1`), on both tokens. `K384` and `K768` are invariant under every Clifford rotation of the
   target and keep Table A2's control witnesses. `Kk` is invariant under the kernel's drive flow `rot3 t` on the
   control for every `t` (the control phase flow lies in `G_κ`); IE1Drive fails there through `J` alone, (b_DJ) through
   the `R_x` flow and `J`. Every entry is cone invariance, decided exactly (INVARIANT by group membership, or MOVED
   with a witness `tr(g(d) P_w) = 1 − c < 0`, `P_w ∈ K`). **Coordinator's check (X7):** the memberships, and MOVED
   witnesses for `K384` (the target `R_z(t₀)`; the control `R_x(π)`, `J`, `R_x(t₀)`) and for `KC` (the target `R_z(t₀)`,
   the control `R_x(t₀)`) recomputed exactly; `Kk` not re-derived.
4. **What each cone refutes** (C21-3; the coordinator's wording under the owner's third question). With H1 and H3
   as introduced hypotheses, at the pair level: *invariance under `Stab_C(Z⊗1)` ⇒ `Q3`* (`K384`); *under
   `Stab_C(±Z⊗1)` ⇒ `Q3`* (`K768`); *under the two-qubit Clifford group with SWAP ⇒ `Q3`* (`KC`); *under G16 with κ's
   gate flow and the drive flow on one token without `J` ⇒ `Q3`* (`Kk`). These refute particular bridge candidates —
   every finite Clifford clause, and the drive flow without its cyclic permutation — and nothing more: the
   implications refuted have introduced hypotheses, the 68 items never reaching the cone are untouched, and cone
   invariance is not operational availability. They are not countermodels to OI's quantum conclusion. In the other
   direction the continuous block-diagonal group forces `Q3` (HO-31 item 1).
5. **Uniform FCC fails on all four through one mechanism** (C21-1, I3.135): with `Y = P_{Φ⁺}`, `F = P_χ`, `E = P_ψ`,
   `Ψ = H(ȲXᵀ)⁻¹`, the contraction of `(Y, E, F)` is the effect `P_h` on the first pair and
   `famI(d_h, Y, E, F) = 16 tr[(d_h⊗y)(e⊗f)] = 16|v|²(1 − c)/(|y|²|ψ|²|χ|²) < 0`, the only condition being that `y`,
   `ψ`, `χ` lie outside every cap. Exact on the four cones (`famI = −4/375`, `−125159/5319389250`, `−21/125`, `−4/9375`),
   with the operator route and the control `X = P_h`. Label: CONDITIONAL ([W] identity; [X] instances; not re-derived by
   the coordinator).

**Assumption-watch marker.** "An exotic cone fails (b) at the operations Table A2 lists for `K(Z_F)`" — false. Which
operation moves a cone depends on the cone; the explicit cones of this round are invariant under every finite Clifford
witness of Table A2 (`KC`) or under the drive flow on one token (`Kk`). A sourcing argument for (b) that reaches only
finitely many Clifford rotations, or the drive flow without `J`, leaves an explicit exotic cone standing.

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `644bf0a1` (C21 closed at `c9dcc18e`) |
| proposal | `research/countermodels/handoff-proposals/HP9-explicit-cones-against-TableA2.md`, sha256 `fee41dc2797cbc431e7eaed605906ecc7c3c60678ef7b34b5f88704a304bcb37` |
| notes, script | `NOTES-C21.md` `f0d72871ae25493023a1afc4026f42544702bc097e83c1e103c2c59f934e8adc` (S0, runs, one table per cone, the other 186 rows, standing); `experiments/c21_rows.py` `c4621d1e20d9ddaad07cd7d2a134ad19d385352682aa598bf1782b2632ee1fb4` / `.out` `80d4d660cd04ad66bd15d1867d650ca606b087699a9169939094d2c1d5529001` (run 2, 25/25; run 1 kept, 25/25; the run-2 amendment adds two RECORD lines, disclosed in the script); replayed byte-identically by the coordinator (120 s) |
| inputs | Table A2 at `research/archive` `4dc0321c` (sha256 `1ff62ad6…`, checked by the script and by the coordinator's X8: 199 rows, 118/68/13); kernel lines at L as cited (CompositeDimension.lean:161, :186, :198, :201, :775; K2Guard.lean:95, :101, :143; KInfFoundations.lean:350, :411, :425, :449), verified by the coordinator |
| coordinator audit | `research/AUDITS/2026-10-11-round4/AUDIT-COUNTERMODELS-R4.md` (§"The three questions"); `countermodels/indep_checkC4.py` run 1 (8/8; X7, X8; replay identical) |

## What the receiving threads may assume

Items 1–5 at their labels, each as the exact proposition stated; item 2 as the reading of which premises the cones
meet and at which level; item 4 as the exact list of refuted implications. **Equivalence (S6):** the finite clause and
the Clifford group are refuted as sufficient invariances with H1–H3; the full-flow form of A_miss is not refuted by
any cone of the record. **Bridge, origin:** a candidate bridge that delivers only finitely many Clifford rotations, or
the drive flow without `J`, is refuted at the pair level by an explicit cone; one that delivers the continuous
block-diagonal group is sufficient with H1 and H3 (HO-31 item 1).

## What they may not assume

Operational availability of any operation; that any cone "satisfies OI" or is "independent of OI"; anything about the
68 NOT REACHED rows beyond R6's record at L; that `pauliW` and `twistQ3` of I3.144 were examined separately;
level-(ii) versions of `K384`, `KC`, `K768` (not attempted); invariance under any continuous family other than `Kk`'s
control phase flow (a finite list refutes, it does not establish); that the coordinator re-derived `Kk` or the FCC
mechanism.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-32 v1` and records in its `LOG.md`
whether and how it relies on it.
