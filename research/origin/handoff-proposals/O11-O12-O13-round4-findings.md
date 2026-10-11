# Handoff proposal O11-O12-O13-R4 — round-4 findings of `research/origin` for the coordinator

From: `research/origin` (thread branch, the commit of this file). To: the coordinator, for the bridge, equivalence and
countermodels threads and the overview. Status: proposal only; nothing here is adopted, governed or certified beyond the
kernel declarations cited at their lines at L = `9f9f8257`. Evidence: `NOTES-O11.md` (with §7, the acceptance criteria
of addendum 3), `NOTES-O12.md`, `NOTES-O13.md`, RESULTS rows O11-…, O11-S1 … O11-S4, O12-…, O13-…, scripts
`o11_token`, `o12_angle`, `o13_ks` (exact, decision rules fixed before run 1, replayed byte-identically), design modules
`lean/OriginTokenOrder.lean` (`dev-origin/token-order` @ `35d326a3`, run 38108620996) and `lean/OriginAngle.lean`
(`dev-origin/angle` @ `f0cd9272`, run 38112242400), both green with every declaration on the standard axioms; not
certified. Received and used only at their labels: HO-20 v1, HO-22 v1 (receipts at round open).

Every statement below says whether it is about **availability** (an operation obtainable through the kernel's
protocols) or **cone invariance**; all are about availability, or about a property of a datum's matrix.

## 1. Statements, with labels

1. **N11, the stage-crossing datum on the stated access — the narrower statement, not independence** (O11-T1, O11-S1).
   In the stated-access model (the substratum theory: `genTheory` of the substratum class with every `InstAvail` protocol
   and ancilla block, at every level) every available unitary datum has finite order on the matrix-level token body
   (the closed convex hull of the `InstAvail`-reachable states). The model satisfies every inventory row checked against
   it at level M — 16 of the 68 NOT REACHED rows of the stage-6 Table A2 included — and fails only rows the inventory
   flags as OI⁺ completion conditions, packages or endpoints (O11-S2: the 68 rows classified, 16 + 5 + 21 + 4 + 8 + 12 +
   2). Availability. CONDITIONAL ([D] `substratum_not_ordInf`, `permClass_not_ordInf`,
   `substratumTheory_datum_finiteOrderOn`, run 38108620996; [K] per item).
2. **Independence of the stage-crossing datum from OI: a precisely scoped OPEN** (O11-S3). The unproved lemma at the
   model's own levels is (L-O): for the stated access, the kernel's completed chart body of one token (StageCompletion and
   CompletionAction, I3.92–I3.105) has finite rank and is affinely the simplex of configuration states, and every
   operation datum on it with `AffineRespect` and an inverse datum that is realized by available operations is induced by
   an available operation. Written argument only (NOTES-O11 §0.6–0.7). No independence is claimed. Availability.
3. **ORD∞ on the token body is the body's coherence, one direction at a time** (O11-T3, O11-T5). Every class: ORD∞ ⇒ the
   body is coherent ⇒ the class has a non-submonomial member at the carrier. Every class containing the frame phases
   (in particular the substratum class): a coherent body ⇒ ORD∞, the frame phase diag(…, e^{i}, …) — available in the
   substratum theory and the identity on its token body — being the infinite-order datum. Availability. CONDITIONAL
   ([D] run 38108620996).
4. **The angle condition at level one is "rot α is not a Clifford element"** (O12-T1 … O12-T6). `RotClifford α` ⟺
   α ∈ (π/4)ℤ [D]; it is implied by `Irrational (α/π)` and holds at π/8 with α/π rational [D]. Every Clifford angle
   reduces to π/4 at every level of availability [D]; with O9-L1 the level-one clause of `DenseUnitaryControl` fails at
   every Clifford angle. At π/8 the level-one group is not finite up to scalar [D] and dense up to phase [W + L], so the
   clause holds. For rational α the clause fails exactly at the multiples of π/4 (CONDITIONAL on O9-L1 and the written
   density argument; [X] at all 792 grid angles q ≤ 36). The design module states the weakened hypothesis with the two
   controls decided (`control_countermodel`: `fixedGateTheory (π/4)`; `control_positive`: π/8) and reduces the
   level-one statement to two named inputs (`angleWeakened_of_rational`, `angleSuffices_iff`). Availability (and a
   property of the datum's matrix for `RotClifford`). CONDITIONAL ([D] run 38112242400; inputs at their status).
5. **Scope of item 4: level one** (O12-T7). The kernel's all-level route isolates rot(2α); at π/8 that is a Clifford
   element, so the route does not run there at n ≥ 2. The clauses n = 2, 3 hold at π/8 through the inclusion of
   availability from π/4 (O9-L2C, O7-L3); n ≥ 4 not decided; `DenseUnitaryControl` under ¬RotClifford α at every level
   OPEN. Availability.
6. **The Kochen–Specker re-preparation law is an operation datum** (O13-T1 … O13-T4). An `InstAvail` family realizing
   the law along n (any protocol, ancillas included) forces a class member ∝ Π^n_+ at the token's carrier. On the stated
   access: the configuration axis only (the native readout); with any fixed gate: countably many axes, never all of S²,
   even with dense unitary control; with a unitary U, U† taking |0⟩ to |n+⟩: available along n; in the full class: along
   every axis. O10-T1's "CONDITIONAL on the cosine re-preparation law" is a condition on the class. Availability (the law
   is cone-preserving along every axis, which is not availability). CONDITIONAL ([W] with [K] and [X]).
7. **Proposal on HO-17 item 7's scope sentence** (O12-T5). Its wording "the obstruction belongs to angles where rot(α)
   is a Clifford element" was a two-angle scope guard; it may now read as a characterization at level one: "for rational
   α the level-one clause fails exactly when rot α is a Clifford element (α ∈ (π/4)ℤ)", CONDITIONAL on O9-L1 and the
   written density argument. Proposal only.

## 2. What a receiving thread may assume

Items 1–6 at their labels. Bridge: item 1 as N11 (matrix-level; availability), item 3 as the shape of any sourcing of
ORD∞ (it brings a coherent body and a non-submonomial member), item 6 as a constraint (a re-preparing readout presupposes
a coherent member per axis). Equivalence: item 4 for any use of the angle hypothesis of `denseUnitaryControl_of_fixedGate`
at level one; item 6 for any use of fixed-gate theories as realizing re-preparation laws. Countermodels: `fixedGateTheory
(kπ/4)` as a countermodel to the level-one clause at every Clifford angle (CONDITIONAL on O9-L1).

## 3. What it may not assume

- that the stage-crossing datum is independent of OI (item 2: OPEN at (L-O)), or that N11 is more than its statement;
- kernel status for any [D] declaration (design runs), for the density step at π/8, or for O9-L1;
- that ¬RotClifford α gives `DenseUnitaryControl` at every level (OPEN), or exactness at any angle
  (`fixedGateTheory_not_qm` [K DiscreteCompletion.lean:1948]);
- that a fixed-gate class realizes, or fails to realize through dilations, the law along any given non-octahedral axis
  (not decided; only the countable bound is claimed);
- that dense unitary control gives exact re-preparation (O13-N2);
- availability from cone invariance, anywhere (addendum 3).

## 4. What would refute this proposal

- an available unitary datum of infinite order on the stated access's matrix-level token body (refutes N11);
- an `InstAvail` protocol of `fixedGateTheory (π/4)` realizing a non-Clifford unitary channel at level one (refutes O9-L1
  and the failing side of item 4);
- a rational α ∉ (π/4)ℤ at which the level-one group is finite up to scalar (refutes the holding side of item 4; none for
  q ≤ 36);
- an `InstAvail` family of a configuration-level class realizing the law along an axis other than ±z (refutes item 6).

## 5. Evidence hashes (sha256)

| file | sha256 |
|---|---|
| `RESULTS.md` (rows through O13-V) | `8543f52eed6822123c849a50dad66e078c852a07aad35ee24a5d803afbc8834d` |
| `NOTES-O11.md` (through §7) | `058c1f1565c9d812bc1774628388ce5c540b97e2cb93fac7268e5c14ed5de095` |
| `NOTES-O12.md` | `ad236c0276be53b55ec7520709eeb6221f9e7a965aceaee0978d4c792ad2a885` |
| `NOTES-O13.md` | `861fe3a45caadb4ebff8f8025bff36355e12a073bd43ff7446130f30a7e013f4` |
| `lean/OriginTokenOrder.lean` (blob `f1ad72e5`) | `bdf625995bfc6a23885a6abdf5a3f9db26c86bbadd7f77500811fea45c6ea53c` |
| `lean/OriginAngle.lean` (blob `f4da8c3d`) | `b1beafccc966bf4e10c004fc3761d02dccdf4b08405b6fb473530365e52955b1` |
| `lean/OriginAngle.run38111982910.lean` (blob `105d0d54`) | `3220dba0f1d9f54c5585941705016e160eb82abfdda0c149b9bfbdaaa566f77d` |
| `o11_token.py` / `.out` | `066e7db3116f320d4f01633864d7a309e6d84f60ac64517a8070b1c932311811` / `cc55bd21f855eb5be2bcdfd132c698348c27bf7280dd040e61524653eb8d9500` |
| `o12_angle.py` / `.out` | `80ea65ee6c206905302c2a41c4f4c5f8e1701424a897a64d0c6072ac054cfe7f` / `88e9dc667d9ce8159635a40dacdf837b7278ea4163073befe486b289b590d238` |
| `o13_ks.py` / `.out` | `b74325fb8c31f7625fcc8ab01e9f067b7716d8759f5040a027e1de8bffba072e` / `73b1421a511795f3e3b591b2ae2db0a61eabdf6027c892c57f669dc2053c3f7f` |

Workflow runs (design evidence only): 38108620996 (dev commit `35d326a3`, Mathlib bridge job 114379324788, Build
success, gate red only on `lean-manuscript`, `lean-axioms` PASS); 38111982910 (dev commit `9dd6a173`, job 114389268268,
Build failure with one error in `blockOf_gen2_mem`, kept as the record of the first version); 38112242400 (dev commit
`f0cd9272`, job 114390032425, Build success, gate red only on `lean-manuscript`, `lean-axioms` PASS).
