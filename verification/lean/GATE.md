# GATE — kernel-check acceptance for the LEAN-FULL layer (updated b408)

Files under gate (both core-only, zero imports):

    lean OI_B397_Pilot.lean && lean OI_L3_Core.lean

Clean exit on both = kernel certification of: the b397 closure theorems (pilot) and the L3
core set — Theorem 1a at operator level (mz_identity, kernel_equivariant), the Susskind
cancellation mechanism (susskind3, with its anticommutation/square hypotheses certified
exact on the lattice operators by l3_core_relations_probe.py), Theorem 3's chirality
algebra (center_anticommutator, mass_square), and the boost-Ward identity (boost_ward).

Risk record: authored without a local toolchain (network disabled); unchecked
kernel-targeted files = 2, held to one uniform risk class (core-only, the pilot's proven
class/calc patterns) under owner-directed continuation (b408). Statements match
L2-SPEC/L3-SPEC-1; semantic content is mirror-certified (L2M*, L3M*, R*); residual risk is
elaboration-level. On any kernel error: fix proofs, statements frozen; a wrong statement is
itself a reportable finding.
