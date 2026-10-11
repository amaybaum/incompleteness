# HO-27 (v1) — origin → bridge, equivalence, countermodels: the stage-crossing datum on the stated access (N11, independence OPEN at (L-O)); ORD∞ is coherence; the level-one angle condition; the re-preparation law is an operation datum

**From** `research/origin` (round 4, nodes O11, O12, O13). **To** `research/bridge` (items 1–3, 6), `research/equivalence`
(items 4–6) and `research/countermodels` (item 4's countermodel family). Written by the coordinator from the source
thread's committed record; version 1, 2026-10-11. Every statement is about **availability** (an operation obtainable
through the kernel's protocols) or about a property of a datum's matrix; none is a cone-invariance statement.

## Statements and labels

1. **N11 — on the stated access every available unitary datum has finite order on the matrix-level token body**
   (O11-T1, O11-S1). In the stated-access model — the substratum theory, `genTheory` of the substratum class with every
   `InstAvail` protocol (step, readout, coarse-graining, feed-forward, discard) and every ancilla block, at every level —
   every reachable state is configuration-diagonal, every available unitary carries configuration states to
   configuration states, and every available unitary datum has finite order on the token body (the closed convex hull of
   the `InstAvail`-reachable states at the token's carrier, ancilla-assisted protocols included through the discard).
   The model satisfies every inventory row checked against it at level M, 16 of the 68 NOT REACHED rows of the stage-6
   Table A2 included, and fails only rows the inventory flags as OI⁺ completion conditions, packages or endpoints (the
   68 rows classified: 16 satisfied, 5 kernel theorems true in every model, 21 failed and so flagged, 4 not decided and
   not premises, 8 at level P, 12 manuscript statements, 2 at level O not shown). The same holds for the sourced class
   of scaled partial permutations and for the observer theory of every kernel substratum. Extends HO-9 item 3 from
   passive finite-rank towers to the kernel's full availability. **Form:** OI ⇒ X, with no introduced hypothesis.
   Label: CONDITIONAL ([D] `substratum_not_ordInf`, `permClass_not_ordInf`, `substratumTheory_datum_finiteOrderOn`,
   `obsTheory_obstruction`, run 38108620996, 45/45 on the standard axioms; [K] per inventory item at the lines of
   NOTES-O11 §1 and §7).
2. **Independence of the stage-crossing datum from OI is a precisely scoped OPEN** (O11-S3). N11 is not an
   independence verdict: the token body is the thread's own, and the kernel's completed chart body is reached only by a
   written argument. The unproved lemma at the model's own levels is **(L-O)**: for the stated access, the kernel's
   completed chart body of one token (StageCompletion and CompletionAction, inventory I3.92–I3.105, applied to the
   token's protocol tower) has finite rank and is affinely the simplex of configuration states, and every operation
   datum on it with `AffineRespect` and an inverse datum realized by available operations is induced by an available
   operation, so that it permutes the vertices and has finite order (NOTES-O11 §0.6–0.7, [W]; reversible data that are
   not unitary conjugations are covered by the written argument and by an exact check on every enumerated family of
   levels one and two, O11-T7). No independence is claimed. Label: OPEN.
3. **ORD∞ on the token body is the body's coherence, one direction at a time** (O11-T3, O11-T4, O11-T5). For every
   class: ORD∞ ⇒ the body holds a coherent state (an entry between two distinct configurations) ⇒ the class holds a
   non-submonomial member at the carrier. For every class containing the frame phases at the carrier, in particular
   every class containing the substratum class: a coherent body ⇒ ORD∞, the witness being the frame phase
   `diag(…, e^{i}, …)` — available in the substratum theory, the identity on its token body, of infinite order on the full
   matrix algebra and on every set holding a state with a nonzero entry at its configuration, and crossing every finite
   stage holding such a state. So on the kernel's matrix carrier the frame-axis rotation is in the stated access already;
   what the stated access lacks is a coherent state for it to act on. Without the phase continuum coherence alone does
   not give ORD∞ (`fixedGateTheory (π/4)` at level one: a coherent body, 24 channels, each of finite order), while the
   rational angle `π/8` does (O11-T6). Label: CONDITIONAL ([D] run 38108620996; [X]; O11-T6 with O9-L1 [W]).
4. **At level one the angle condition of `denseUnitaryControl_of_fixedGate` is "`rot α` is not a Clifford element"**
   (O12-T1 … O12-T6). `RotClifford α` (conjugation by `rot α` carries the sixteen-element Pauli set into itself) holds
   exactly when `α ∈ (π/4)ℤ` [D]; it is implied by `Irrational (α/π)` and fails at `π/8` with `α/π` rational [D].
   Every Clifford angle reduces to `π/4`: the class at `kβ` lies in the class at `β`, availability passes from `kβ` to
   `β` at every level, and at every Clifford angle the level-one clause implies the clause at `π/4` [D]; the level-one
   group is finite up to scalar at every Clifford angle (8 or 24 classes) [D + X]. With O9-L1 (only the 24 Clifford
   channels are available at level one at `π/4`, [W + X]) the level-one clause of `DenseUnitaryControl` fails at every
   `α ∈ (π/4)ℤ`: **`fixedGateTheory (kπ/4)` is a countermodel to "`DerivedOI ∧ FixedGateSourced α` ⇒ the level-one
   clause" at every Clifford angle.** At `π/8` the level-one group is not finite up to scalar [D] (the word
   `rot(π/8) · S rot(π/8) S†` has determinant 1 and trace `1 + √2/2`, and no power is a scalar) and is dense up to phase
   [W + L], so the clause holds. For rational `α` the clause fails exactly at the multiples of `π/4` (CONDITIONAL on
   O9-L1 and the written density argument; exact on all 792 reduced grid angles with `q ≤ 36`, and on the coordinator's
   grid `q ≤ 24`). The design module `OriginAngle` states the weakened hypothesis with the two controls decided
   (`control_countermodel` at `π/4`, `control_positive` at `π/8`) and reduces the level-one statement to two named
   inputs: `RationalDensityInput` (density at the rational non-Clifford angles, [W + L]) and `BalancedFailureInput`
   (O9-L1); with both, `AngleSufficesLevelOne α ⟺ ¬RotClifford α` (`angleSuffices_iff`). **Form:** OI + {the gate at
   `α`, `¬RotClifford α`} ⇒ the level-one clause; the gate is introduced (inventory I4.239 records it as an independent
   datum), not an OI premise. Label: CONDITIONAL ([D] run 38112242400, 52/52 on the standard axioms; the inputs at their
   status).
5. **Scope of item 4: level one** (O12-T7). The kernel's all-level route isolates `rot(2α)` on one block (the echo
   identity, DiscreteCompletion.lean:844 at L); at `π/8` that is `rot(π/4)`, a Clifford element, so the route does not
   run there for `n ≥ 2`. The clauses `n = 2, 3` hold at `π/8` through the inclusion of availability from `π/4`
   (O9-L2C, O7-L3 at their labels); `n ≥ 4` is not decided; `DenseUnitaryControl` under `¬RotClifford α` at every
   level is OPEN. Assumption-watch marker (O12-N2): a level-one weakening of the angle hypothesis does not carry to
   every level by the kernel's route, which needs the condition at `2α` as well.
6. **The Kochen–Specker re-preparation law is an operation datum** (O13-T1 … O13-T4). An `InstAvail` family of an
   architecture realizing the law along an axis `n` — `F^n_±(X) = tr(Π^n_± X) Π^n_±` — forces a nonzero multiple of
   `Π^n_+` and of `Π^n_−` into the class at the token's carrier (every Kraus operator of a map with a rank-one Choi
   matrix is a multiple of one projector; every branch of an `InstAvail` family is a finite sum of conjugations by class
   members, `realized_of_instAvail`). Hence: on the stated access the law is available along the configuration axis
   only (`Π^n_+` is submonomial exactly for `n = ±z`; along `z` it is the native readout, `readout_is_localLuders`); with
   any fixed gate, along at most countably many axes and never along all of `S²`, even where `DenseUnitaryControl`
   holds (`mixR_countable_upToScalar`); with a unitary `U, U†` taking `|0⟩` to `|n+⟩`, along `n`; in the full class,
   along every axis. O10-T1's "CONDITIONAL on the cosine re-preparation law" is a condition on the class, not on
   observation. The law is cone-preserving along every axis, which is not availability. Label: CONDITIONAL ([W] with
   [K ImplementationLocality.lean:250, :530; OperationalAssembly.lean:658; StateMixingCoupling.lean:662] and [X]).
7. **HO-17 item 7's scope sentence, sharpened** (O12-T5). "The obstruction belongs to angles where `rot(α)` is a Clifford
   element" was a two-angle scope guard; it now reads as a characterization at level one: for rational `α` the level-one
   clause fails exactly when `rot α` is a Clifford element, CONDITIONAL on O9-L1 and the written density argument. HO-17
   stays as issued (its sentence remains true); this item carries the sharper form.

## Evidence

| item | pointer |
|---|---|
| source | `research/origin` @ `7192e3b5` (round-4 commits `8709fe41` … `7192e3b5`) |
| proposal | `research/origin/handoff-proposals/O11-O12-O13-round4-findings.md`, sha256 `454c09a76254d502502d492237d2512513e8ff89517a11e6bfa664914da464a8` |
| results, notes | `research/origin/RESULTS.md` sha256 `8543f52eed6822123c849a50dad66e078c852a07aad35ee24a5d803afbc8834d` (rows O11-K … O13-V); `NOTES-O11.md` `058c1f1565c9d812bc1774628388ce5c540b97e2cb93fac7268e5c14ed5de095` (§7 the acceptance criteria); `NOTES-O12.md` `ad236c0276be53b55ec7520709eeb6221f9e7a965aceaee0978d4c792ad2a885`; `NOTES-O13.md` `861fe3a45caadb4ebff8f8025bff36355e12a073bd43ff7446130f30a7e013f4` |
| scripts, outputs | `experiments/o11_token.py` `066e7db3116f320d4f01633864d7a309e6d84f60ac64517a8070b1c932311811` / `.out` `cc55bd21f855eb5be2bcdfd132c698348c27bf7280dd040e61524653eb8d9500` (run 2; run 1 kept); `o12_angle.py` `80ea65ee6c206905302c2a41c4f4c5f8e1701424a897a64d0c6072ac054cfe7f` / `.out` `88e9dc667d9ce8159635a40dacdf837b7278ea4163073befe486b289b590d238`; `o13_ks.py` `b74325fb8c31f7625fcc8ab01e9f067b7716d8759f5040a027e1de8bffba072e` / `.out` `73b1421a511795f3e3b591b2ae2db0a61eabdf6027c892c57f669dc2053c3f7f`; all replayed byte-identically; full list `research/AUDITS/2026-10-11-round4/EVIDENCE-HASHES.txt` |
| design modules | `research/origin/lean/OriginTokenOrder.lean` sha256 `bdf625995bfc6a23885a6abdf5a3f9db26c86bbadd7f77500811fea45c6ea53c` (`dev-origin/token-order` @ `35d326a3`, run 38108620996: Build success, 45/45 standard, `lean-axioms` OK 5905, gate red only on `lean-manuscript`); `lean/OriginAngle.lean` `b1beafccc966bf4e10c004fc3761d02dccdf4b08405b6fb473530365e52955b1` (`dev-origin/angle` @ `f0cd9272`, run 38112242400: Build success, 52/52 standard, `lean-axioms` OK 5912, gate red only on `lean-manuscript`); the failed first version `OriginAngle.run38111982910.lean` `3220dba0f1d9f54c5585941705016e160eb82abfdda0c149b9bfbdaaa566f77d` (run 38111982910, one error, kept) — `research/AUDITS/2026-10-11-round4/CI-RUNS-R4.md` |
| coordinator audit | replays 3/3; `indep_checkO4.py` run 1 8/8 with every countercontrol False (the Clifford angles on two grids by two methods; the class counts 8/24; the `π/8` word's determinant, trace and non-scalar powers; the algebraic-integer test exactly at the Clifford angles; the 192-element group and its 24 channels with orders in {1, 2, 3, 4}; the minimal polynomial of `(3+4i)/5`; the Choi rank and Kraus form of the law; the submonomial axes; the row counts; monomial action on configuration projectors); the two modules and the written arguments read; the echo identity verified at L; 75/75 citations at L — `research/AUDITS/2026-10-11-round4/AUDIT-ORIGIN-R4.md` |

## What the receiving threads may assume

Items 1–7 at their labels. **Bridge:** item 1 as N11, matrix-level and availability; item 3 as the shape of any
sourcing of ORD∞ on the token (it brings a coherent body and a non-submonomial member; the frame-axis rotation itself
is available on the stated access and is not what a source must supply); item 6 as a constraint (a re-preparing readout
presupposes a coherent member per axis); item 2 as the exact location of the open transfer lemma (L-O) for the
single-token side of B14's question. **Equivalence:** item 4 for any use of the angle hypothesis of
`denseUnitaryControl_of_fixedGate` at level one, with item 5's scope; item 6 for any use of fixed-gate theories as
realizing re-preparation laws; item 7 in place of HO-17 item 7's scope sentence. **Countermodels:** `fixedGateTheory
(kπ/4)` as a countermodel to the level-one clause at every Clifford angle (CONDITIONAL on O9-L1), and
`fixedGateTheory α` at every angle as a theory in which the sphere tower's law is unavailable even with dense control.

## What they may not assume

- that the stage-crossing datum is independent of OI (item 2: OPEN at (L-O)), or that N11 says more than its
  statement — in particular nothing about the kernel's completed chart body, nothing about reversible data that are not
  unitary conjugations beyond the written argument and the enumerated levels, and nothing at level H;
- kernel status for any [D] declaration (design runs), for the density step at `π/8`, or for O9-L1;
- that `¬RotClifford α` gives `DenseUnitaryControl` at every level (OPEN), or exactness at any angle
  (`fixedGateTheory_not_qm`, DiscreteCompletion.lean:1948);
- that a fixed-gate class realizes, or fails to realize through dilations, the law along any given non-octahedral
  axis (only the countable bound is claimed);
- that dense unitary control gives exact re-preparation (O13-N2);
- availability from cone invariance, anywhere.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-27 v1` and records in its `LOG.md`
whether and how it relies on it.
