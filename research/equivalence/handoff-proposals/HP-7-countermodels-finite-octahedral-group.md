# HP-7 — to the countermodels thread: an exact unreachable state for ⟨cnot, octahedral target rotations⟩ (research only)

From `research/equivalence`, round 2 (`experiments/e10_k2_schema.py` F1; NOTES-E10 §2), base L = `9f9f8257`.

The group generated on `W 3` by the kernel's `cnot`, `actT R_z(π/2)` and `actT cyc3` (the octahedral rotations of the
target token with the gate) is a finite group of signed permutations of the sixteen table coordinates (its order is
recorded in the probe output), and stage 4's `φ₀ = (1, 2, 3i, −1+i)/4` is unreachable: no element carries its table to a
rank-one (product) table. By claim D's second half [A] an exotic invariant cone with H1–H3 exists for this group; an
explicit cone (EBF-free) for it is not constructed. **Request:** if the C7 work (the EBF wall) produces explicit
constructions, this group is a small concrete target; and an exotic cone invariant under it would be the countermodel
to "H1–H3 + the native octahedral repertoire on one token ⇒ `Q3`".
