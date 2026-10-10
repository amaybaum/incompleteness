# Pre-audit for stage-6 steps 3–4 (R6, T6) — coordinator, fixed before either thread reports

Base L = `9f9f8257…`. Written 2026-10-10, 18:05Z, after launching G6 and R6 (17:57Z) and before any of their
output exists. Purpose: fix exact facts and the audit decision rules in advance, so that the audits of R6 and T6
compare their claims against predictions written down beforehand (§A.21, §A.29).

## 1. Exact facts (`preaudit_r6t6.py`, run 2: 11/11 CONFIRMED, replay identical; run 1 kept, 6/11, four
transcription errors of mine recorded in the script)

| id | fact |
|---|---|
| P1a | the K2-guard chain recomputed: `cnot p(xplus, z3) = phiW`, `actT reflY phiW = idW`, `cnot idW = chainW`, `chainW` pairs −1/2 with the sharp effects of −e₁, −e₃. Hence `no_candidateCone_cnot_reflY` (K2Guard.lean:143): no candidate cone is invariant under both `cnot` and `actT reflY`. |
| P1b | K(Z_F) is not `actT reflY`-invariant: `phiW` ∈ K(Z_F) and its reflection `idW` pairs −2 with the singlet, a pure state of K(Z_F). Every reflected defect is PSD (eigenvalues 0, 1/4), so the witness is not a defect. |
| P1c | K(E0) is not `actT reflY`-invariant: `actT reflY E0 = E00 + E13 + E22`; the joint (−1)-eigenvector of X⊗Z and Y⊗Y pairs +1 with E0 and −1 with the reflection. |
| P1d | Q3 is not `actT reflY`-invariant (the Bell table is PSD, its partial transpose is not). So the K2-guard no-go excludes none of the alternatives: it constrains the operation, not the cone. |
| P2 | local tomography on `W 3` holds for every K: products of the four ball effects {unit, sharp +x, +y, +z} span the dual of `W 3` (rank 16). |
| P3 | `4 prodEffVal(e, f, z_s) = e₀f₀ + eᵀM_s f` with `M_s` orthogonal, and `prodEffVal(e, f, E0) = e₀f₀ + eᵀM_E f` with `‖M_E‖ = 1`; an effect on the ball has `|e_vec| ≤ e₀`, so both cones lie in `maxCone (eball 3)` (the CandidateCone upper clause). P3c: `chainW ∉ maxCone`. |
| P4 | `cnot` carries pure products into `maxCone` on an exact grid (posFwd) and is an involution (posInv). |
| P5a | K(Z_F): a defect has eigenvalue −1/8 (not inside Q3); `phiW ∈ K(Z_F)` reflects to `idW` with eigenvalue −1/2 (not inside twin); `actC J` moves `z_(1,1)` out (pairing −1/2). So IE₁'s conclusion and (b_DJ) fail for K(Z_F) — as hypotheses, not theorems. |
| P5b | K(E0): not `actC nflip`-invariant (pure witness); not SWAP-invariant (3/13, −5/13). |
| P6 | every product state pairs ≥ 0 with every defect of Z_F (`1 + aᵀM_s b`) and with E0 (`1 + a₁b₃ − a₂b₂`): products lie in both cones; the single-token slices are the ball (H1). |

Mechanical (AUDIT-I §2): no module at L reaches both the pair-level modules and the matrix carrier except the root;
so no statement at L attaches a `FiniteOperationalTheory` realization to any `W 3` cone.

## 2. Predictions for R6 (written before its output)

- Every pair-level kernel theorem at L (I3's B1–B7 and the DIM-1 / K2-GUARD / COMP-1 / NB-1 / EFF-1 items) is
  SATISFIED by K(Z_F), K(E0) and Q3 alike, or NOT REACHED: they constrain the gate on products, the effects, the
  single ball, or are no-gos about operations (P1–P4). None excludes either cone.
- Every H-, M- and G-level item is NOT REACHED (no bridge at L).
- The items each alternative FAILS are exactly hypotheses on the do-not-assume list: (b) in every form, IE₁,
  IE₂ where it reaches, `Q3`/PSD reachability, pair-level T (extreme-ray transitivity); K(E0) additionally fails
  the NOT-only and SWAP forms; K(Z_F) fails κ.
- No statement at L attaches an embedded-observer realization to any cone-level object; R6 must say so with the
  mechanical ground, for every alternative.
- The single-token structure of every alternative is Q3's (P6), so every single-token item holds as for Q3.

## 3. Audit decision rules for R6 and T6 (fixed now)

- **R6** is accepted iff: every SATISFIES/FAILS verdict for K(Z_F) and K(E0) is backed by an exact script line
  with a countercontrol (Q3 satisfies every pair-level item; a known failing object fails); every NOT REACHED
  verdict names the absent bridge (an I3 A-item or AUDIT-I §5); no H-level item is marked satisfied or failed for a
  cone-level alternative; the three explicit statements (i)–(iii) are present per alternative; and the FAILS set
  for each alternative consists of do-not-assume hypotheses only (any FAILS against a proved-[K] item would mean an
  item at L excludes the alternative — that would be a NEW finding and is audited first, by my own exact check).
- **T6** is accepted as INDEPENDENCE iff its countermodel satisfies every item reaching the pair cone at L
  (SATISFIES or NOT REACHED for every non-hypothesis item, per R6's audited table), violates (b) in the weakest
  sufficient form by an exact witness, and the isolated missing assumption is stated as exact content (expected:
  the spectator clause for the drive and one off-frame partner on one token, the instance of OI⁺-1 for those
  operations). T6 is accepted as DERIVATION iff every step is [K], [W] or [X], no do-not-assume item enters as a
  premise, every premise passes the stage-5 disguise test, and I can reproduce the chain's exact steps
  independently. A DERIVATION verdict would contradict stage 5 and the predictions above; it is audited with
  maximum skepticism (§A.31) before acceptance. UNRESOLVED is accepted only with the failed derivation and the
  failed countermodel both recorded.

## 4. Files

`preaudit_r6t6.py` (run 2, sha256 `591b88fe…`), `.out` (`4f9e24db…`), `.err` (`exit 0`), replay pair identical;
run 1 kept as `preaudit_r6t6.run1.{py,out,err}`.

## 5. Added after R6's audit and T6's launch (18:50Z), before T6 reports: the expected witnesses, recomputed

`T-audit/preaudit_t6.py` (run 1, 6/6 `PREAUDIT-T6-FIXED`, replay identical; table-level code, rational rotations,
no unitaries): W0 the maps `nflip`, `rot3 π`, `cyc3`, `R_x(π/2)`, `R_n(π/2)` (n = (3,0,4)/5) and the order-3 `R1`
about (5,1,1) are exact rational rotations; W1 K(Z_F) is invariant under both NOTs, `rot3 π`, the phase flips
and SWAP (the defects are permuted; Q3 control green); W2 `actC cyc3`, `actT cyc3`, `actC R_x(π/2)`,
`actC R_n(π/2)` move a defect out of K(Z_F) with the witness pairing −1/2 (the image of the defect's own
(−1/8)-eigenstate, which stays in K(Z_F)); W3 `actC R1` moves a defect out (best witness in my finite candidate
set −7/18; AUDIT-Y R7 and R6 −2383/5316 with their witnesses — sign is what matters); W4 K(E0) leaves itself
under every listed map and under SWAP (−5/13); W5 **K(Z_F) violates (b) in both weakest sufficient forms on the
control token** ({flow about x, J} and {flow about x, phase flow about z}: the quarter-turn of the flow alone
suffices, pairing −1/2) and satisfies the NOT-only, phase-only and SWAP forms. So the expected INDEPENDENCE
countermodel for T6 is K(Z_F) with the witness `actC R_x(π/2)` (or `actC cyc3`), and the expected missing
assumption is the spectator clause for the drive (with its off-frame partner) on one token — the instance of
OI⁺-1 for those operations (I3.150–I3.153's weakest member; K2's local-action clause I3.165). A T6 verdict of
INDEPENDENCE with another countermodel, or of DERIVATION / CONDITIONAL on a new item, is audited against this
table first.
