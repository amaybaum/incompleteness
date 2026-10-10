# Addendum to the audit of thread Z (wording item found after the stage-4 archive was sealed) — 2026-10-10 16:42Z

`AUDIT-Z.md` (`4be00ec5…`) is unchanged, as is the stage-4 archive (`f99d7cc3…`) that contains it. This addendum
records one wording item found while fixing the stage-5 pre-audit (`pt/audit/stage5-inputs/preaudit_bridge.py`,
run 2 → run 3):

- Z's RESULT §1.1 writes the Bell-type states as `ψ_s = (1, s₁s₂, s₁, −s₂)/2` with `ρ(e_s) = (I − 2ψ_sψ_s*)/8`. In the
  stage-3 convention (control index first, `z_s = (E00 + s₁E13 + s₂E22 − s₁s₂E31)/4`), that vector is the state of
  `z_{−s}`: the formula labels the four states by the negated label. The set `Z_F` and every pairing Z computes are
  unaffected (the labelling is consistent inside Z's own scripts, which passed their checks and replayed
  identically); only a reader transcribing the formula to name a specific defect would be misled. No verdict,
  count or hash changes.
