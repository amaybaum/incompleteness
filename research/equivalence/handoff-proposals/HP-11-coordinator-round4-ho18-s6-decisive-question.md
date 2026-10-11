# HP-11 — to the coordinator: correct HO-18 item 2; S6 as an equivalence of cone-level statements with §G built in design; the answer to the owner's decisive question; E17–E18 in design (research only)

From `research/equivalence`, round 4 (E15–E18, under addenda 1–3), base L = `9f9f8257`. Nothing here is certified; no
preregistration became a round; nothing was placed under `verification/` on the thread branch.

1. **Correction requested — HO-18 v1, item 2.** It describes LOWER as "every product of `eball 3` states has a positive
   semidefinite dictionary image" and UPPER as bounding "a cone containing the products". The built module proves
   something else: LOWER `Q3_subset_of_pure` (EqvK2Schema.lean:308) — a set closed under addition that contains a table
   of every rank-one positive matrix contains `Q3`; UPPER `subset_Q3_of_pure_dual` (EqvK2Schema.lean:297) — a set that
   contains a table of every rank-one positive matrix and lies in its own dual lies in `Q3` (R-E11.2). The hypothesis of
   both is every pure state, not the products; with products alone UPPER would make A_miss and `ReachPure` superfluous,
   which K(Z_F) and HO-24's cone refute. Requested: HO-18 v2 with item 2 in these words.
2. **Draft S6 (`K2-SCHEMA-1`) is ready for owner review** (E15; R-E15.1–R-E15.4;
   `preregistration-drafts/S6-k2-schema-pair-cone.md`). Native V3 format, one `v3-round` and one `v3-governed-paths`
   block, non-sealing. It states: **given H1–H3 and `ReachPure`, `K = Q3` iff A_miss, where A_miss is the invariance of
   `K` under the flow and `cycEquiv`** — sufficiency witnessed by the schema (`pairCone_eq_Q3_of_drive`), necessity by the
   invariance lemma (`Q3_aMiss`). Its scope section: the equivalence is between cone-level statements; the availability
   of the operations ((A)/H-OI_g) is a separate H-level question S6 does not decide; A_miss (invariance form) is an
   introduced hypothesis, not a premise at L. Its hypothesis table classifies H2 (I3.148), H3 (I3.149), A_miss
   (invariance form; I3.165, I3.150/I3.153) and `ReachPure` (I3.144) as introduced, not OI premises, and lists
   (A)/H-OI_g (availability, H-level) as not in S6. Countercontrol: HO-24's cone, recomputed exactly and shown not
   invariant under the rotation with cosine 3/5 by an explicit witness (R-E15.2) — the finite clause is the weaker
   alternative that fails (R-E15.3, given Theorem S′). Checkpoint `C0′` (§G built before `F`): see item 6.
3. **The owner's decisive question** (E16; R-E16.1–R-E16.5). *Positive, below chart dimension 5*: the gate's control
   relation counts dimensions for every body (no body of even chart dimension carries a native gate), so with a drive
   **OI ⇒ (d = 3 ∧ Ω an ellipsoid) ∨ (d odd ∧ d ≥ 5)** with every hypothesis an inventory item (I3.8, I3.9's `relC` and
   invertibility, I3.66, the token body of K∞-Stage I3.167), i.e. OI + {chart dimension at most 4} ⇒ ellipsoid. The
   chart-4 separation countermodels (Ω₄, Ω⋆, Ω_cs) are excluded by dimension, not by shape. *Negative, in odd chart
   dimension*: the hybrid token Ω_h (a qubit with a two-sector superselection rule, chart dimension 7) meets every
   pair-level clause in the kernel's form and is no ellipsoid — {the listed inventory items} + {gate invariance of K,
   product-form self-duality, drive invariance of K} ⇏ ellipsoid, independent of those premises at L and not claimed
   independent of OI. The missing assumption is K∞-Geom (I3.174), or an elementary-scope predicate (I3.177) bounding the
   number of perfectly distinguishable states by two. Weaker alternatives that fail without the gate: self-duality
   alone, central symmetry alone. Residual (OPEN): with K∞-Geom, a drivable non-ellipsoidal body of odd chart dimension
   `≥ 5` with a native gate.
4. **E17** (R-E17.1–R-E17.2): the transport form of H-DYN as a predicate on the kernel's `QuasilocalSystem`, the passage
   stated as a proposition (not proved; R-E14.2's status), the positive control that every Target A system satisfies the
   predicate, and the finite-stage case — a star-algebra automorphism of a stage's matrix algebra mapping every matrix
   unit to a `{0,1}` matrix is the transport along a configuration permutation. The transport form is introduced (H-DYN's
   form), not an OI premise; the stage-6 inventory has no item for it.
5. **E18** (R-E18.1): the power cone of Ω⋆, in polynomial form, equals its dual for the self-dualizing form
   (R-E13.1's self-duality step).
6. **Design runs** (two of the round's three dispatches; the third unused). Run 38112803530 on `20c207f1`
   (`dev-equivalence/r4-design`, based on L), Mathlib bridge job 114391691368: `Build completed successfully (3647
   jobs)`; prints all `[propext, Classical.choice, Quot.sound]` — `EqvK2Schema` 22/22, `EqvK2Converse` (S6's §G) 9/9,
   `EqvTransport` (E17) 9/9, `EqvPowerCone` (E18) 7/7; release gate red only at `lean-manuscript` (the four unregistered
   design modules), `lean-axioms` 5907, no sorry, 303 legacy records intact, 43 receipts hold. Readings BUILT for all
   three new modules; S6's checkpoint `C0′` is met. The first run (38112020014) read PARTIAL: its Build step failed on
   `EqvTransport` (the `Matrix`-scoped notation `ᴴ` not opened), while `EqvK2Converse` already elaborated cleanly.
7. **Addendum 3 applied to older surfaces.** The LEDGER's K2 row (clause (c)) and RESULTS R-E4.1 said (b) was
   "independent of every item at L"; both now say "independent of the transferred pair-level premises at L" (the 68 rows
   not reached at stage 6 not shown irrelevant). Request: the same wording in any coordinator record that quotes them.

**ROADMAP-relevant wording (not applied; for the owner).** Row K2: as draft S6's licensed sentence, conditional on a
governed round. Row K∞ (Trans): "the pair level does not supply K∞-Trans without a further single-system premise: a
superselection token meets every pair-level clause in the kernel's form and is no ellipsoid (research record)" —
research-only wording, for the owner's decision.

**May not be assumed:** that S6 or any draft is a round; that the design modules are certified or carry census
dispositions; that A_miss, H2, H3, `ReachPure`, the transport form, K∞-Geom or the elementary scope is an OI premise or
sourced; that the negative answer of item 3 concerns OI as a whole.
