# Coordinator's pre-audit record for stage 4 (Q-EX), written 2026-10-10 14:47Z, before reading Y's or Z's results

Purpose: fix, before the threads report, what the coordinator has established independently about the leading
candidate, so that the later audit compares the threads' claims against checks made without their code or
conclusions. Script `indep_checkQEX.py` (`d7dec152…`), run 2: 15/15 CONFIRMED, `INDEP-QEX-CONFIRMED`; replay
byte-identical. Run 1 (kept as `.run1.*`, 12/15) failed on three harness choices of my own: a simplification form
sympy left unreduced (B5), and a control rotation `Ry(π/4)` that left one orbit overlap at `1/2 + √2/4` and the rotated
`E0` eigenvector inside its cap (D1, D2); run 2 uses the order-3 rotation `(I + i(X + Y + Z))/2`, Gaussian-rational,
which spreads a defect's state evenly (overlap `1/4`) over the orbit basis. The other twelve lines are identical.

## What is established [X], with the written argument [W] it supports
- **A.** `CNOT = I⊗P₊ + Z⊗P₋` in the target `X`-eigenbasis (the owner's decomposition); `I⊗P₊ + X⊗P₋`, the
  protocol sketch's form, is not CNOT (erratum recorded in `pt/audit/stage4-inputs/OWNER-NOTE5-STAGE4-PROVENANCE.md`).
- **B.** `Ad(CNOT)(U⊗I) = U⊗P₊ + ZUZ⊗P₋` for generic `U ∈ SU(2)`; the CNOT-conjugates of `X⊗I, Y⊗I, Z⊗I` are
  `X⊗X, Y⊗X, Z⊗I`; the Lie algebra generated is `span{σ⊗I, σ⊗X}`, closed under all 36 brackets, equal to
  `su(2)⊗P₊ ⊕ su(2)⊗P₋`; `V⁻¹ZVZ` for a real rotation `V` by `a` is the rotation by `2a`, so the second factor is all of
  `SU(2)`; `CNOT = [I⊗P₊ + (−iZ)⊗P₋]·[I⊗(P₊ + iP₋)]` with the second factor `(1+i)/2·(I − iX)`, a target `X`-rotation by
  `−π/2` up to phase, whose sector blocks have determinants `1` and `−1`, so it is not in `Ad(SU(2)×SU(2))`: the
  generated group is the connected product extended by a discrete target rotation (the owner's precision).
- **C.** Six exact pure states (a Bell state, Gaussian-rational states, stage 3's `(1,1,1,−1)/2`) are each the image
  of a product state under an explicit `U⊗P₊ + V⊗P₋` with `U, V ∈ SU(2)` — the reachability construction
  `ψ = u′⊗|+⟩ + v′⊗|−⟩`, product `|0⟩⊗(|u′| |+⟩ + |v′| |−⟩)`, `U|0⟩ = u′/|u′|`, `V|0⟩ = v′/|v′|`. Countercontrol:
  `Z⊗X` commutes with CNOT, with `Z` on the control and with `X` on the target, so `⟨Z⊗X⟩` is invariant under the
  commuting torus with `cnot`; states with `⟨Z⊗X⟩ = 1` are unreachable from `|0⟩|0⟩` there. (This is a reachability
  obstruction for the commuting torus; whether the torus-invariant class is EXOTIC is Z's question, settled at
  stage 3 by EBF as existence.)
- **D.** With `g` the order-3 control rotation: `φ = gψ_s` has overlap `1/4` with each `ψ_t`, so `P_φ ∈ K(Z_F)` and
  `ipW(P_φ, g e_s) = −1/2 < 0`: `g e_s ∉ K(Z_F)`; the rotated negative eigenvector `χ` of `E0` has `ipW(P_χ, E0) = 1 ≥ 0`
  (outside the cap, so `P_χ ∈ K(E0)`) and `ipW(P_χ, g E0) = −1`: `g E0 ∉ K(E0)`. So one control rotation already breaks
  the invariance of every stage-3 countermodel; the exclusion at S4 is witnessed exactly, not only by the
  reachability argument. Countercontrol: `ipW(e_t, g e_s) = |⟨ψ_t|gψ_s⟩|²/4 ≥ 0` for all `s, t`, so the defect orbit
  never certifies exclusion by itself; the witness must be a pure state.
- **E.** Pure states pair nonnegatively and are PSD, so a cone containing every pure state contains `Q3`; with
  `K = K*` and `Q3 = Q3*`, `K ⊆ Q3* = Q3` and `K = Q3`.

## What this does not establish (for the audit to hold the threads to)
- Reachability of *every* pure state is a [W] construction verified on instances [X]; Y must give it as a theorem
  with the generic case handled (`u′ = 0` or `v′ = 0`: the state is a product, already in `K`).
- Nothing here bears on the provenance question: whether the operation `U⊗P₊ + V⊗P₋` — or even `U⊗I` acting on
  an entangled composite — is available from observer-native premises at L. The owner's requirement (note 5) is
  that Y classify this: derived at L (file:line), or an added extension-of-operations principle, with every UNIQUE
  verdict then CONDITIONAL on it.
- Nothing here decides the weaker nodes S1–S3 or the finite extensions; those are Z's, with Y's exact group
  statements.
- No claim about carriers other than the certified two-qubit pair carrier `W 3`.
