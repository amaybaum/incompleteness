# Lean 4 pilot — compile instructions and acceptance gate (b399)

**Artifact.** `OI_B397_Pilot.lean` — self-contained Lean 4, **zero imports** (no Mathlib, no
Std): it depends only on the core prelude, so it checks with a bare invocation and is immune
to Mathlib version drift.

**Acceptance gate (owner side).**

    lean OI_B397_Pilot.lean

Clean exit = kernel acceptance of all 27 theorems. If Lean is not installed:

no toolchain: install elan (the standard Lean version manager; see the official Lean 4 install page), then:
    elan default stable
    lean OI_B397_Pilot.lean

(Any recent Lean 4 release; no project scaffolding or `lake` needed.)

**Status honesty.** The file was WRITTEN, not kernel-checked, in the b399 container (no Lean
toolchain; network disabled). Mitigations: (i) every concrete integer asserted by a `decide`
(24, 72, 288, 144, parities, chi-consistency, distinctness) is independently re-verified by
`b399_lean_pilot_probe.py` using a different construction (matrix generation vs. list
enumeration); (ii) the abstract proofs (Parts 0–2) are short calc chains reviewed line by
line, with explicit rewrite arguments everywhere an ambiguous match was possible. Residual
risk is Lean-syntax-level (a rewrite orientation, an elaboration detail), not
mathematical-content-level. If the kernel rejects anything, the fix should be local; the
round's acceptance is the owner's clean run, not this side's review.

**What is and is not proved.** T1 and T2 are complete self-contained proofs (T2 for every odd
q — stronger than the b397 census). T3 is the kernel-checked integer layer; the single
classical averaging identity |G|·dim Hom = Σχχ is documented and deferred to a Mathlib phase
(where it is `FixedPoints`/character orthogonality), as is the (3,4,5) inner split.
