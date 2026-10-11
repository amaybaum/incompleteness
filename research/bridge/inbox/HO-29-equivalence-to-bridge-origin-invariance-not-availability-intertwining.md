# HO-29 (v1) — equivalence → bridge, origin: S6's necessity direction proves invariance, not availability; the intertwining for every rotation angle in design; the admissible wording for (b)

**From** `research/equivalence` (round 4, node E15, under the owner's two distinctions). **To** `research/bridge`
(B14–B15: what a sufficient bridge `A + H ⇒ (b)` must deliver at the pair level) and `research/origin` (O11: the same,
from the availability side). Written by the coordinator from the source thread's committed record; version 1,
2026-10-11.

## Statements and labels

1. **What the necessity direction of S6 proves** (R-E15.4; draft S6 §G). Given H1 (every product of `eball 3`
   states in `K`), H2 (`cnot`-invariance), H3 (`K = dualW K`) and `ReachPure`: **`K = Q3` iff A_miss**, where A_miss
   is the invariance of `K` under `actT (rotLin t)` for every `t` and under `actT cycEquiv` — cone-preserving
   admissibility. Sufficiency (`←`) is the schema `pairCone_eq_Q3_of_drive` (HO-18 item 3); necessity (`→`) is
   `Q3_aMiss`: `Q3` is invariant under one copy's local unitary conjugations, because the dictionary carries the two
   operations to conjugation by `1 ⊗ diag(1, cos t + i sin t)` and `1 ⊗ (I − i(X + Y + Z))/2` and unitary conjugation
   preserves positive semidefiniteness. The two directions are witnessed by different declarations (§A.34), assembled
   in `pairCone_eq_Q3_iff_drive`. **This is `Q3 ⇒ A_miss` in the invariance reading only.** It gives no operational
   availability of those operations through the kernel's protocols — the H-level premise (A)/H-OI_g, for this
   repertoire H-OI_g at `{R_z(θ₀), J}` (HO-20 item 4, CONDITIONAL) — and S6 does not decide availability: a quantum
   cone with a restricted set of available transformations has the invariance without the availability. For B14–B15
   and O11: a sufficient bridge `A + H ⇒ (b)` must deliver the invariance form at the pair level; the equivalence says
   that, given H1–H3 and `ReachPure`, that is exactly what `K = Q3` requires, and says nothing about the transfer.
   Form: OI + {H2, H3, `ReachPure`} ⇒ (`K = Q3` ↔ A_miss), H2 (I3.148), H3 (I3.149) and `ReachPure` (I3.144)
   introduced, not OI premises; A_miss (I3.165; a form of (b), I3.150/I3.153) the open bridge on one side of the
   equivalence, introduced, not a premise at L. Label: CONJECTURE ([D] `EqvK2Converse`, 9/9 prints standard in design
   run 38112803530, Mathlib bridge job 114391691368; the sufficiency direction [D] run 38101580750; not certified).
2. **The intertwining for every angle, in design** (`EqvK2Converse`, on `EqvK2Schema`'s dictionary, which is the
   bridge draft's `pauli`, `tokMat`, `dict` verbatim). `dict_actT_rotLin`: for every real `t`,
   `dict (actT (rotLin t) ω) = (1 ⊗ diag(1, cos t + i sin t)) · dict ω · (1 ⊗ diag(1, cos t + i sin t))ᴴ`;
   `dict_actT_cyc`: `dict (actT cycEquiv ω) = (1 ⊗ V) · dict ω · (1 ⊗ V)ᴴ` with `V = (I − i(X + Y + Z))/2`; through
   the split `dict ω = Σ_μ (½ σ_μ) ⊗ tokMat (ω μ)` (`dict_eq_sum_tensorOf`) and the one-token laws `tokMat_rot`,
   `tokMat_cyc`. This is the angle-general form of the bridge thread's monomial images (HO-21 item 1, stated on the
   unit circle `c² + s² = 1`); a converged dictionary module would be a separate round's surface. Label: CONJECTURE
   ([D] the same run; the same blob elaborated cleanly in run 38112020014, whose Build step failed on another module).
   **Coordinator's check (X6, exact in `ℚ(i)`):** both identities on all 16 basis tables of `W 3` at `cos t = 3/5`, at
   `t = π/2` and for `cycEquiv`, with the module's `cycMat` and `cycMatᴴ = cycMatH`.
3. **Admissible wording** (the owner's first distinction, applied by the source thread). Stage 6 established
   `A_reached ⊭ (b)` for the 118 transferred pair-level rows; the 68 rows not reached have not been shown irrelevant.
   The source thread writes "(b) is independent of the transferred pair-level premises at L", never "independent of
   OI", for (b), A_miss and every pair-level hypothesis; its LEDGER K2 row and R-E4.1 were reworded in place to this
   form (old text recorded in its LOG). The coordinator's records use the same wording from this handoff on.

## Evidence

| item | pointer |
|---|---|
| source | `research/equivalence` @ `ab6788b9` (round-4 commits; §G built at `d3432cc3`) |
| proposal | `research/equivalence/handoff-proposals/HP-13-bridge-origin-invariance-not-availability.md`, sha256 `6ff14f4a6e7baaf6b87bee1a920bf5254b6151e8dabc74b06d077c07f6e72659` |
| results, draft | `research/equivalence/RESULTS.md` sha256 `2a53ffac8272a93ec0a1aac626cb5f6fbcbd65fab09e7aac02de7bc283ef98b4` (row R-E15.4; R-E15.1 for the draft); `preregistration-drafts/S6-k2-schema-pair-cone.md` `91873058d8ceb39f1ae2a55e45ac4a77f3fae1187a2bb112872998ce0319773d` (§G; the scope section; the hypothesis table) |
| design module | `research/equivalence/lean/EqvK2Converse.lean` sha256 `240abaf6c445112e1b2d5aa39932b51004e6b21cb93b9999ca6aacb5201b0554` (dev blob `4add9b8d`), equal to the blob on `dev-equivalence/r4-design` @ `20c207f1` and @ `2d978412` (both cut from L); run 38112803530, job 114391691368: `Build completed successfully (3647 jobs)`, `EqvK2Converse` 9/9 prints `[propext, Classical.choice, Quot.sound]` (the coordinator's count over the saved job log), gate red only at `lean-manuscript` — `research/AUDITS/2026-10-11-round4/CI-RUNS-R4.md` |
| coordinator audit | `research/AUDITS/2026-10-11-round4/AUDIT-EQUIVALENCE-R4.md`; `equivalence/indep_checkE4.py` run 2 (8/8; X6 the intertwining, X1/X7 the countercontrol cone of HO-24 recomputed with the non-invariance witness at `cos t = 3/5`; replay identical); the module's nine declarations read (`Q3_aMiss` is a statement about the set `Q3`; `pairCone_eq_Q3_iff_drive`'s `→` is `Q3_aMiss` after `rintro rfl`, its `←` is `pairCone_eq_Q3_of_drive`) |

## What the receiving threads may assume

Items 1–3 at their labels. **Bridge:** item 1 as the exact target shape of a pair-level bridge — the invariance of the
pair cone under the full flow and `cycEquiv` is, given H1–H3 and `ReachPure`, equivalent to `K = Q3`; item 2 as Lean
text that builds against Mathlib `v4.33.0` and the kernel at L with the standard axiom footprint, on the same
definitions as `BridgeDictionary`. **Origin:** item 1 as the statement that a derivation of availability (H-OI_g at
`{R_z(θ₀), J}`, or any availability principle) is what would turn the invariance form into (b) at the pair level, and
that nothing in S6 supplies it; item 3 as the wording rule.

## What they may not assume

- that S6 or any preregistration became a round, or that the design modules are certified or carry census
  dispositions;
- that A_miss, H2, H3 or `ReachPure` is an OI premise or is sourced;
- that the invariance form implies availability, or that `Q3_aMiss` says anything about the kernel's protocols;
- that the module formalizes HO-13 item 2's two-rotation clause (it formalizes the full-flow form), or that
  `ReachPure` is proved in the kernel (it is a hypothesis, proved in writing in NOTES-E10 L4).

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-29 v1` and records in its `LOG.md`
whether and how it relies on it.
