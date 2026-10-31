# F2-1 stage 2, run-2 — proof repairs in `OIBridge/F2CoherenceControls.lean`

Authorization: PR #1011 comment 6546214912 (owner), step 2, under amendment A★-1 (accepted at
`fdeeb2d5`). The earlier attempt at `05ecc873` (CI run 41220197866, `INCONCLUSIVE (void)`) is
preserved unchanged.

Its `Build` log listed errors at lines 52, 79/80, 103, 109, 181, 194/195, 204, 295 and 349 of
the module. Two of these are the genuine errors the authorization names (L194/195 and L295). The
rest are parse and elaboration failures of the `ᴴ` and `*ᵥ` notations, which `open Matrix` supplies
(A★-1), together with their cascades: unknown constant `rot_moves_ones`, the type mismatch of
`onesBounded_of_onesFixing` against an unelaborated `OnesBounded`, and unsolved goals after the
parse error.

No statement, definition, hypothesis or declaration meaning changed. The 19 A★ statements remain
byte-identical, which `run-2/controls.py` checks. There is no `sorry`, no `admit` and no new axiom.

| Line (run-2) | Change | Traced defect | Why it is necessary |
|---|---|---|---|
| 30 | `open Matrix` added to the context | notation context (A★-1) | `ᴴ` and `*ᵥ` are scoped notations of `Matrix`. Without them, `OnesBounded`, `rot_moves_ones`, the `hgram` step of `nonnegClass_onesFixing` and `fullTheory_rotDagger` do not parse. |
| 193–198 (old 192–195) | `ext i j; apply Complex.ext; · simp; · simp [← …]` replaced by `refine Matrix.ext fun i j => ?_`, then `show M i j = (((M i j).re : ℝ) : ℂ)`, then `Complex.ext`, with `rw [Complex.ofReal_re]` and `rw [Complex.ofReal_im]; exact (Complex.nonneg_iff.mp (hM i j)).2.symm` | (ii) the `simp` that made no progress (old L194), with its sibling bullet (old L195), which left the unreduced goal `0 = (Matrix.map … i j).im` | Both `simp` calls failed to unfold the `Matrix.map` application. The `show` states the entry by definitional unfolding, and each component then closes by one rewrite. The statement proved (`M = N.map ofReal` for the real parts) is unchanged. |
| 298 (old 295) | `AncillaClosure.ancBlock M f e` replaced by `Matrix.of fun s t => M (s, f) (t, e)` in `realClass_arch.block` | (i) the complex block construction applied to a real matrix | `ancBlock` is defined for complex matrices only. The replacement is the same block taken entrywise on the real matrix. Its complexification is `ancBlock` of the complexified matrix, so `ext i j; rfl` closes as before. |

No other line changed. The cascaded declarations keep their proofs. A failure in them after this
repair, not caused by the two defects or the notation context, is a new substantive defect: under
the authorization, it stops the work pending fresh owner authorization, and it is not repaired here.
