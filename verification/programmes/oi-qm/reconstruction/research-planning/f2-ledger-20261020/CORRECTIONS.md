# Corrections to LEDGER.md after independent review (`revf2/REVIEW.md`, CONFIRMED WITH CORRECTIONS)

Research only. No repository or GitHub write. `LEDGER.original.md` is a byte copy of the ledger as it stood before
this pass.

## Digests

| file | before | after |
|---|---|---|
| LEDGER.md | `77b50b909541912c6875e726f855fdba9f0c241095e0bab6b4f5440716887840` (= LEDGER.original.md) | `ccbe1f91b426ad8b9f206488dddd7519b9002b8d8ae440b1ba4654c625e7dc32` |
| monomial_branch.py | `b12b5e453b72b6bf56889e16a1da0c5a335c18c9c8c85bd528cd3d71c674b338` | `93b5858fb20d228f8a9ff0af6dd77c57e94ee6c002f7e9a2b96f878d3e10b185` |
| monomial_branch.run{1,2}.out | `bd7ad5f4e4b6cc9ecbec3173fbb3e5b01af6d7bb561ba48bcad3053a92c2a598` | `ffc67f36d26da2858f9180fa8c61ca3c74a488804466da3d6d2e83732a76602c` (5 PASS, byte-identical) |
| kh_pc24.py | (new) | `7d3d866d48392818f7d021e239c3f06e828ee02ba76a7a9a6841013fd85e622d` |
| kh_pc24.run{1,2}.out | (new) | `d9b29aae1191e67281c4c4999ff0760750da8b407e6e3b24a3b23f1b3aca05cd` (10 PASS, byte-identical) |
| reg3_exclusion.*, indep_check.* | unchanged | unchanged (digests in SHA256SUMS) |

The earlier hand-off quoted LEDGER.md digest `8db3efb9…` for an intermediate state. One wording edit was made after
that digest was taken, which produced `77b50b90…`. That later file is the one preserved as `LEDGER.original.md`.

## Changes

**B1 (blocking): Σ3 is equivalent at the pair, not weaker.**
- Finding accepted. Given the domain, the existence of a K₃ satisfying Σ3 is equivalent to K₂ = Q3: one direction is
  §4, and the converse takes K₃ = QK₃. By `pairCone_eq_Q3_iff_drive_maxCone`, it is therefore also equivalent to
  hH2 ∧ hA.
- Changed in the ledger:
  - §3 O-B. "The weakest known sufficient form of O-B is Σ3" becomes: Σ3 re-expresses hH2 ∧ hA in native-operation
    vocabulary. Its states and tests come from O-A, it adds an unsourced K₃, and in the fixed 8×8 Ad_P carrier it is
    pair PSD restated.
  - §2.2. The row "new route" is renamed "re-expression", with the equivalence noted.
  - §4.5 item 1 now states the PSD equivalence.
  - §4.6. "Not a converse" is dropped. The existence-form equivalence is stated, and its converse is called trivial.
  - §5 is re-derived:
    - Attacking O-B in the Σ3 form instead of hH2 ∧ hA gains only a change of vocabulary in logical content.
    - The one substantive lesson is the two-token control (AW-F1).
    - The recommended first premise changes from O-B (native form) to O-A, with new derivation requirements.

**B2 (blocking): most fixtures are already excluded at Σ2.**
- Finding accepted:
  - Γ(Q3), K_Γ, K_B and K_H\* fail PC24/hH2 at the pair;
  - K_S fails MI.
- Checked here: K_H\* fails hH2. `kh_pc24.py` K3c: CNOT maps the pure state (V⊗V)(|00⟩+2|11⟩) of K_H\*, with
  V = [[3,4i],[4i,3]]/5, outside Sym ∪ U(μ)Prod. 20 of 24 native pair permutations fail (K4). Inferring
  non-membership from this uses the extreme-ray argument [W].
- Changed in the ledger:
  - §4.2. A Σ2 row now lists these exclusions.
  - The Σ3 verdict names K(Z_F) as the only listed fixture that needs Σ3.
  - "Fixtures excluded at each level" is rewritten.
  - §4.5 item 5 is restricted to K(Z_F), and its classification is lowered from NEW to ELABORATING.
  - AW-F1 is restated as a two-token control on derivations.

**C1.** σ⁻¹ reaches only u with u₀₀ ≠ 0. For u₀₀ = 0 a native pair transposition is applied first, under PC24.
Stated in §4.2, both routes.

**C2.**
- Closure is needed only for the lower route under CNOT-only NC₃, since (0,1,1,1) is unreachable there.
- The S₈ variant with PC24 needs no closure.
- The upper route uses continuity of u ↦ ⟨u|X|u⟩, so it needs no closure either.
- The variants are named in §4.1, and §4.2 states which one uses closure.

**C3.** The scope of claim (3) is stated in full in §4.2: the 4×4 and 8×8 Hermitian carriers, the fixed Ad_P, the
Lüders branch, and complex Bloch tests. Real tests are not sufficient in general (review R5e/R5f), and the
Γ-transported identification is out of scope. §4.3 is amended accordingly.

**C4.** The monomial control was vacuous. `monomial_branch.py` now computes each branch matrix explicitly, using
distinct prime ancilla amplitudes, with both the scan and the control going through the same `branch` function. The
control applies a Hadamard post-map and flags 4 full-support non-monomial branches. The scan results are unchanged:
0 failures, 92160 and 18432 full-support branches, all monomial. The lemma is also restated as "at most one nonzero
entry per row", following the review's §(e).

**C5.** Citation details:
- OI-7: `PhaseFreeRichness` also requires every swap, and that conjunct is supplied under `SourcedOI`.
- "Ball and effects": `hU` and `hM` are added.
- `maxCone_bound_of_sharp_available` is located at :194.
- Σ0: the classical countermodel is the kernel's operation-class result plus a short [W] cone-level reading. It is no
  longer tagged (a) at the cone level.

**C6.** The O-B countermodel is extended to three tokens. With K₃ = cone{X⊗τ : X ∈ K(Z_F)} ∪ products₃, the clauses
H1₃, MAX₃, RO₃, ATT and DIS hold and NC₃ fails [W] (§3, §4.4). Beyond three tokens it is unchecked, and the ledger
says so.

**C7.** In §3, "minimal" becomes "irredundant". It now states that O-B's native form depends on O-A, so the two are
not independent.

**Register note (§A.32/§A.33).** Not applied. The ledger is a research note, not `papers/` prose. If any of it is
propagated into a manuscript, the process vocabulary and the internal tags should be dropped.

## Re-review R1 and minor notes (applied by the session lead)

- R1: AW-F1 (§4.5 item 5), §5 and the last-recommendation sentence scoped to non-circular derivations yielding only Σ2-type clauses (no reachable-closure definition, MEMO R4); "every pair-level native clause" read as "every clause of Σ2".
- "Every form of O-B depends on O-A" → "Every known form".
- "A countable family can reach at most the dense endpoint" → "cannot reach the exact endpoint" (the cited theorems rule out exactness only).
- LEDGER.md sha256 ccbe1f91b426ad8b9f206488dddd7519b9002b8d8ae440b1ba4654c625e7dc32 → 751155b1f772a4e82b69fbca6dabb020b8355d4cdf6e6d0cc963427fe701a0fb.

## Monomial-lemma scope (from the missing-component node, PR #885)

- §5, "What an OI-native derivation of O-A would have to show", item 2: the must-fail control said that a construction
  adding "only preparations, or any other non-operation resource" does not qualify. The second clause overreached. The
  lemma covers protocols whose instruments are configuration readouts. Sharp Lüders tests in non-configuration bases are
  a non-operation resource that makes the layer flow executable exactly, though they break no uniform ray (`mc-node1`,
  independently reviewed). The item now states that scope.
- LEDGER.md sha256 751155b1f772a4e82b69fbca6dabb020b8355d4cdf6e6d0cc963427fe701a0fb → a04f0e79b3d8dc6fb6779617db7161ac3067858e56f9840dde48b908ddcd704c.
