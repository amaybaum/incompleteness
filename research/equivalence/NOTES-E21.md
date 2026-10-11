# NOTES-E21 — E17's residual: the infinite-volume passage of the transport form

**Status: work in progress, deferred to round 6 by the owner's direction of 2026-10-11T10:38Z; unverified; no result row.**


Base L = `9f9f8257`. Node E21 of round 5 (priority 3). The residual: R-E14.2's passage, stated in round 4 as the
proposition `EqvTransport.Passage` (R-E17.1, [D] as a statement; not proved): a star automorphism `α` of a
`QuasilocalSystem` (QuasilocalCharacterization.lean:168) in **transport form** (`TransportHDyn`: every matrix unit of
every finite stage goes to a `{0,1}` matrix of some finite stage) that is `LocalityPreserving` (:475) with its inverse
is the Target A automorphism of a `ReversibleDynamics` (QuasilocalAlgebra.lean:956): `α (st Λ X) = st (hat Φ Λ)
(transported Φ Λ X)` for every stage `Λ` and every `X`. R-E17.2 proved the finite-stage case at the matrix level of
one stage ([D]). The transport form is introduced, not an OI premise (R-E17.1).

## S0 (written 2026-10-11T10:38Z, before the module is written and before its dispatch)

**What E21 is (§A.31).** Closure mode on a scoped target, with one gem-finding question attached: *which steps of
R-E14.2's written proof carry the passage, and does the written proof use anything its statement does not list?*
**Productivity test (fixed now).** A finding counts iff (a) a named step of the written proof is proved in design
([D]) and strictly reduces what stays open — the open part afterwards is a single named lemma with a precise
statement — or (b) a hypothesis the written proof uses but `Passage` does not state is exposed (a hidden assumption,
recorded as an assumption-watch marker). A restatement that the passage is open is a non-gem.

**The decomposition (fixed now).** `Passage` = (P1) ∘ (P2) ∘ (P4), with (P3) the first step of (P4):
- **(P1) uniqueness of extension** — a star automorphism of a quasilocal system is determined by its values on the
  stages: `α = β` when `α (st Λ X) = β (st Λ X)` for every `Λ`, `X`. Route: the set `{x | α x = β x}` is closed
  (`continuous_starAlgEquiv`, :483; `isClosed_eq`) and contains the union of the stage ranges, whose closure is the
  algebra (`QuasilocalSystem.dense`). Consequence: two automorphisms satisfying the Target A identity for the same
  `Φ` coincide.
- **(P2) matrix units suffice** — the Target A identity on a stage follows from its instances on the matrix units
  (`matrix_eq_sum_unitM`, linearity of `α ∘ st Λ` and of `st (hat Φ Λ) ∘ transportedHom Φ Λ`); so `Passage` follows
  from its unit form `PassageUnits` (the same hypotheses; the conclusion only on `unitM c c'`).
- **(P3) diagonal preservation at one stage** — in transport form, `α (st Λ E_cc) = st Λ' M` with `M` a *diagonal*
  `{0,1}` matrix: `M` is self-adjoint and idempotent because `st Λ'` is an injective star homomorphism and `E_cc` is a
  self-adjoint idempotent, and R-E17.2 (a) (`offDiag_eq_zero_of_zeroOne`) makes it diagonal.
- **(P4) the construction lemma (named; OPEN by design this round)** — `PassageUnits`: from the transport form and
  locality both ways, a `ReversibleDynamics Φ` exists with `α (st Λ E_cc') = st (hat Φ Λ) (transported Φ Λ E_cc')`
  for every stage and every pair of configurations. Its written route (NOTES-E14 §2): (i) by (P3) and the unit, the
  images of `{E_cc : c ∈ Conf Λ}` are orthogonal diagonal projections summing to `1` — a partition of `Conf Λ'` into
  cells; (ii) **compatibility of the stage transports under the directed system**: along `Λ ⊆ Λ₂` the partitions
  refine consistently (`compat`, `injective`), so the cells define a map `ψ` of configurations, continuous for the
  product topology; (iii) `ψ` is a bijection: the same construction for `α.symm` needs `α.symm` in transport form,
  which the statement does not assume — the written proof gets it from `α(D) ⊆ D` and the **maximal abelianness of the
  diagonal subalgebra `D`** ([L]); (iv) finite range of `ψ` and `ψ⁻¹` from `LocalityPreserving` of `α` and `α.symm`;
  (v) the off-diagonal units go to the partial isometries between cells (R-E17.2 (b)), which is
  `transported Φ Λ E_cc'` with `Φ.φ = ψ⁻¹`, the stage indices matched through `compat` (the identity is in `S.A`, not
  between stage indices).

**Design (fixed now).** A design module `lean/EqvPassage.lean` proves (P1) (`starAlgEquiv_eq_of_stages`,
`eq_of_targetA`), (P2) (`stage_eq_of_units`, `passage_of_units`, `PassageUnits`, `passage_of_passageUnits`) and (P3)
(`transport_diag`); it rides in dispatch 3 (the round's last), with the E19/E22 repairs if any are needed. No probe:
no finite computation bears on the infinite-volume steps beyond R-E17.2's exact instances (`e17_transport_finite.py`,
round 4), and the countercontrol for (P3)'s insufficiency is the kernel's own `phaseQ_ne_heisQ` (:792) — the phase
automorphism preserves every diagonal unit and is not a Target A automorphism, so diagonal preservation alone does
not determine `α` [K].

**Decision rule (fixed now).** Each of (P1), (P2), (P3) is [D] iff its theorems print standard axioms in a run whose
Build step succeeds (NOTES-E19 §2's rule); otherwise [W] (the written arguments above). (P4) is OPEN, named as
`PassageUnits` with the route (i)–(v), its steps (ii) and (iii) the load-bearing ones. The node's outcome: **gem
(ELABORATING)** if (P1)–(P3) are [D] — the open content of `Passage` is then exactly `PassageUnits`; the hidden
dependence of (iii) on the maximal abelianness of `D` (not stated in `Passage`, [L] in the written proof) is recorded
as an assumption-watch marker in either case.

**Predictions.** (P1) BUILT 0.8 (a closure argument with kernel lemmas); (P2) BUILT 0.65 (`simp only [map_sum,
map_smul]` normal forms are the risk); (P3) BUILT 0.7 (rewrites through `map_star`, `map_mul` of two bundled maps);
all three 0.5. (P4) stays OPEN (certain). The marker on (iii): CONFIRMING (it is already listed as [L] in R-E14.2's
evidence column; E21 records that `Passage`'s statement silently relies on it).
