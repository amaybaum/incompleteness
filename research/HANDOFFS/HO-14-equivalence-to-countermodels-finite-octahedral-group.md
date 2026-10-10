# HO-14 (v1) — equivalence → countermodels: an exact unreachable state for ⟨cnot, octahedral target rotations⟩, order 384

**From** `research/equivalence` (round 2, node E10, probe F1). **To** `research/countermodels` (explicit exotic cones;
the EBF wall of C7). Written by the coordinator from the source thread's committed record; version 1, 2026-10-10.

## Statement and label

The group generated on `W 3` by the kernel's `cnot` (`Ad(P₀⊗1 + P₁⊗X)`, control the first token), `actT R_z(π/2)` and
`actT cyc3` — the octahedral rotations of the target token with the gate — is a finite group of signed permutations of
the sixteen table coordinates, of **order 384**, and stage 4's `φ₀ = (1, 2, 3i, −1+i)/4` is unreachable: no element
carries its table to a rank-one (product) table (the Bell state is carried to one by 192 elements). By claim D's second
half [A] an exotic invariant self-dual cone with H1–H3 exists for this group; no explicit (EBF-free) cone for it is
known. Label: the order and the unreachability CONJECTURE (exact exhaustive computation, independently reproduced by
the coordinator's `indep_checkE2.py` X2); the exotic cone's existence CONDITIONAL on claim D [A].

**Request carried from the source thread.** This group is a small concrete target for explicit constructions: an exotic
cone invariant under it would be the countermodel to "H1–H3 + the native octahedral repertoire on one token ⇒ `Q3`".
Note the round-1 fact (C2.1) that the local stabilizer of K(Z_F) with `cnot` has order 1536 and contains the octahedral
rotations only as `V4` on each token (HO-11): K(Z_F) itself is **not** invariant under this group (`cyc3` moves it,
witness `−1/8`), so a new construction is needed — the orbit of a defect set under the group, or a non-surgery cone.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `5d266133` |
| proposal | `research/equivalence/handoff-proposals/HP-7-countermodels-finite-octahedral-group.md`, sha256 `08f01ad24acca50890a7b595229f75cffbe2b226c0b6a3491f7c608001388d7f` |
| results | `research/equivalence/RESULTS.md` sha256 `1570731e…` row R-E10.3; `NOTES-E10.md` `ab45c208…` §2 |
| script, output | `experiments/e10_k2_schema.py` `e480cea9…` / `.out` `dce83bbe…` (F1, F3) |
| coordinator audit | `research/AUDITS/2026-10-10-round2/equivalence/indep_checkE2.py` X2 (own signed-permutation closure: 384; `φ₀` reachable by 0 elements) |

## What the receiving thread may assume

The group's order and generators as exact facts; the unreachability of `φ₀`; the existence of an exotic invariant cone
only at CONDITIONAL on claim D [A].

## What it may not assume

That any explicit cone for this group exists; that claim D is certified; anything about groups containing a continuous
local rotation (there the K2 schema forces `Q3`, HO-13).

## Receipt

The receiving thread copies this file into its `inbox/` with a commit naming `HO-14 v1` and records in its `LOG.md`
whether and how it relies on it.
