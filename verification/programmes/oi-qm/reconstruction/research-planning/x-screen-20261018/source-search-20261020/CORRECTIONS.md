# Correction pass on SOURCE-CHECKPOINT.md

This pass answers the independent review `../rev864/REVIEW.md` (sha256 `1a02839e…efd1`; verdict CONFIRMED WITH
CORRECTIONS). The reviewer's code `../rev864/indep.py` (sha256 `0901724c…8b54`) was read and not reused. Research
only: nothing in the repository or on GitHub was written, and nothing was dispatched.

## Files

| file | before | after |
|---|---|---|
| `SOURCE-CHECKPOINT.md` | `6d2d94951061c115d30d61c355866a376a23b720e69b8bda149f7c3748f4ebb2` | `c64e39c6e9fe5bcff2d11feb78eedc852bdbdc76d02cf61c7d6cd2a0caa3ac0d` |
| `SOURCE-CHECKPOINT.original.md` | — | `6d2d94951061c115d30d61c355866a376a23b720e69b8bda149f7c3748f4ebb2` (byte-identical copy of the pre-review text) |
| `src_witness.py`, `src_witness.run{1,2}.out` | `bfce213f…78eb`, `2dfcfda3…e110` | unchanged |
| `src_witness_v2.py` | — | `66738e2723df9f4432acbfda8702fa55f99010ea2e9fc00e22427446d8d88dcd` |
| `src_witness_v2.run{1,2}.out` | — | `21a631b1dd93b02b73d907b603b5d231362ffc6a1550d8b2a8000c1817054f1f` (both; 51 PASS, rc 0) |
| `exc_survivors.py` | — | `738f36a936d8a22f9271fddcc075171384a61fe1b8ace42339a05938afc1d64c` |
| `exc_survivors.run{1,2}.out` | — | `2bb0ff4de4090b55332a10dd6fef4e7ea0daf73620f03624deffbc7c1c62ec3d` (both; 16 PASS, rc 0) |
| `sdp_zf_search.*`, `run1-harness-error/*` | unchanged | unchanged |

Both new scripts were run twice with `venv/bin/python -I -B` (SymPy 1.13.3, Python 3.13.16), and each pair of runs
is byte-identical.

## Changes

| # | finding | change |
|---|---|---|
| 1 | B1 | §3.3 item 5 rewritten. K_H is restated as satisfying EXC-S, MI and MEV but failing EXC-24 (Ad_{X⊗X} swaps the two junction points \|00⟩, \|11⟩). The exact ingredients are in `exc_survivors.py` S6; the topological step is labelled as the reviewer's written argument, not independently reviewed. The repaired survivor K_H\* = cone(𝒰·(SEP ∪ G)), 𝒰 = {U(t)(V⊗V)}, is added after re-verification with separate code (S1–S5): the U(t)·Prod criterion with controls; 𝒰.G_pure ⊆ Sym; the 4 S-commuting native permutations lie in 𝒰; each of the other 20 maps a pure state outside the pure set; B ∈ G (MI); K_H\* ⊆ Q3 (MEV); P_singlet ∉ K_H\*. The witnesses come from U(t)·Prod, so Takagi is not load-bearing. Added: K_S satisfies EXC-24 (S3–S4). The N1 table cell and §5 item 3 no longer carry the K_H survivor claim. The previous headline reply had stated "EXC ∧ MI ∧ MEV still has a non-Q3 survivor, K_H"; the corrected survivor is K_H\*. |
| 2 | B2 | EXC-S is defined once (§3.1) as Ad_S ∈ Aut(K)₀. The relation to EXC-24 is stated there. The table row points to §3.1. Every survivor cell (table, §3.3 item 5, §5 item 3) is restated against both forms. |
| 3 | N1 | §3.2, Γ(Q3) bullet: the homology route is named as the independent one. The bracket sign is labelled "E1 transported", needing Kadison [L] and a unital retraction [W]. The E2 controls are noted as code-path controls. |
| 4 | N2 | Kill test restated as the Γ-transported identification P ↦ Γ∘Ad_P∘Γ of all native operations (table row and §3.3 item 2), with the reason that re-identifying SWAP alone is inconsistent. |
| 5 | N3 | The MUT block is called "negated restatements" (§6). In `src_witness_v2.py` it is renamed NEG, and the identity brT = −br is checked, which shows that the "Γ → T" item is not a sensitivity test. `src_witness.py` is kept unchanged. |
| 6 | N4 | `src_witness_v2.py` adds the check that the four sign −1 automorphisms are exactly S·{I, I⊗X, X⊗I, X⊗X}. The E10 label is narrowed to what is computed, and §6 says the same. |
| 7 | N5 | The §A.31 class becomes NEW (scoped, form) / ELABORATING (substance). Memo §6(c) is quoted in full, and F-γ and CH are cited (§3.3 item 7). AW-S1 is relabelled "NEW in form". |
| 8 | N6 | §3.3 closing sentence: the K(Z_F) and K_B exclusions are tagged [W, new], with the review status stated. |
| 9 | N7 | ReachabilitySeam.lean:249 → :251. The E13 comment names `sdp_zf_search.py` in `src_witness_v2.py`. |
| 10 | N8 | K_H ≠ Q3 and K_H\* ≠ Q3 are made exact: P_singlet is outside each pure set (S5, S6), replacing the dimension count. |
| 11 | — | Header line pointing to this file and the original. §4 witness line and §6 table extended with the new files. §5 item 4 restated as review status. |

## Reviewer claims not verified in this pass

- **Topological step for K_H failing EXC-24.** Every point of U(t)·Prod has neighbourhoods containing a 4-ball;
  points of G_pure∖{|00⟩, |11⟩} have ℝ² neighbourhoods. I checked this by reading only. The exact ingredients are
  verified: X⊗X ∈ Aut(K_H), the junction is {|00⟩, |11⟩}, and X⊗X swaps them.
- **Takagi.** The claim that the pure set of K_H\* equals Sym ∪ U(t)·Prod rests on [L], and no conclusion here
  depends on it.
- **[W] steps checked by reading only:** the K_B/SEP/maxCone homology arguments, and the H₂ action of complex
  conjugation on ℂP³ [L].
- **The reviewer's own run outputs** (`indep.run{1,2}.out`) were read but not re-executed in this pass.

## Re-review R-1

- §3.3 item 5: "Each survivor below is generated by pure states" → "Each survivor below other than K_Γ is generated by pure states" (Γ(B) = S/2 is not a pure state; K_Γ rests on E3 and E12). SOURCE-CHECKPOINT.md sha256 c64e39c6e9fe5bcff2d11feb78eedc852bdbdc76d02cf61c7d6cd2a0caa3ac0d → 837e06feb246ab5b3cdb046995cf93ad900d8a7dfb2fe53a294735fb2f0d5490.
