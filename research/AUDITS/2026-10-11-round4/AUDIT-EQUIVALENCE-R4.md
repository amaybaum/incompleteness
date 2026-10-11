# Coordinator audit — `research/equivalence`, round 4

Thread head `ab6788b9` (2026-10-11; round-4 commits `46d5aea0` … `ab6788b9`). Base L = `9f9f8257`. Audited: the
round-4 rows of `RESULTS.md` (R-E15.1 … R-E15.4; R-E16.1 … R-E16.5; R-E17.1, R-E17.2; R-E18.1; R-CITE.4), the
reworded rows R-E4.1 and the LEDGER's K2 row, `NOTES-E15.md` … `NOTES-E18.md`, the draft
`preregistration-drafts/S6-k2-schema-pair-cone.md`, `experiments/e15_k2s6_probe`, `e16a_tokens_pair`, `e16b_hybrid`,
`e17_transport_finite`, `e18_powercone`, `e8_cite_check` (run 5), the design modules `lean/EqvK2Converse.lean`,
`lean/EqvTransport.lean` (with the failed dispatch's copy `EqvTransport.run38112020014.lean`) and
`lean/EqvPowerCone.lean`, the nine receipts in `inbox/`, the handoff proposals HP-11, HP-12, HP-13, `LOG.md` and
`LEDGER.md`. Audited under the owner's round-4 acceptance criteria (the premise-inventory rule, the pair-level/full-OI
distinction, the invariance/availability distinction); the checks added for them are in method 8.

## Method

1. **Receipts.** HO-9 v2, HO-17, HO-20, HO-21, HO-22, HO-23, HO-24, HO-25 and HO-26 (v1) copied verbatim at
   `46d5aea0` (sha256 `bd62649d…`, `65d2f79a…`, `f36b2448…`, `5b8599be…`, `3a6440f0…`, `3c1e126d…`, `27175857…`,
   `9341f3f3…`, `4ee56f58…`, each equal to the overview file at `742c6b2f`, re-checked by the coordinator), with the
   reliance recorded in `LOG.md` item by item before any research step (HO-9 v2 item 3 only; HO-17 items 4–8 at their
   labels, items 6–7 unused; HO-20 item 4 beside the two-rotation clause S6 does not formalize; HO-21 as the
   convergence target, not part of S6's surface; HO-22 items 1 and 3 as context, the order 384 recomputed; HO-23 as a
   comparator only; HO-24's cone as S6's countercontrol with every exact item recomputed; HO-25 and HO-26 at their
   labels). The thread read its own HO-18 v1 and HO-19 v1 as issued and found **HO-18 item 2 not what it meant** (the
   coordinator's error; corrected by HO-18 v2, below). The three coordinator addenda arrived mid-round and were met by
   in-place amendments of the round's own unaudited rows, notes and draft, recorded in the LOG with the time of each.
   Cross-branch reads (`research/overview` @ `742c6b2f`; `research/archive` @ `4dc0321c`, the stage-6 inventory under
   addendum 1) are logged with hashes. Protocol satisfied.
2. **Replay.** Six scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 6/6
   (`equivalence/REPLAY-LOG.txt`; `e8_cite_check` at the head, its run commit).
3. **Independent check.** `equivalence/indep_checkE4.py` (own code: Gaussian rationals over Fractions, exact
   principal minors, a BFS closure of the projective group and of the orbit, exhaustive enumerations; reads nothing
   from the thread; decision rule fixed before run 1): run 1 **7/8** — X2 failed on the harness's own expectation that
   `relC` holds for `Ad(CNOT)` with `N = diag(−1, 1, −1)` as well as with `diag(1, −1, −1)`; the exact computation was
   right and the hand expectation wrong (`(Y ⊗ 1) CNOT (Y ⊗ 1) = CNOT (1 ⊗ X)` while `(1 ⊗ Y) CNOT = CNOT (Z ⊗ Y)`); run
   1 kept (`indep_checkE4.run1.out`), expectation corrected, no thread claim touched; run 2 **8/8**, countercontrols
   5/5 failing as stated, `INDEP-E4-FIXED`; replay identical.
   - X1 (R-E15.2, HO-24's cone): the projective group `⟨CNOT, 1 ⊗ diag(1, i), 1 ⊗ U_J⟩` has order 384; the orbit of
     `h* = (10, 2−2i, −1−3i, 3−i)` has 192 rays (BFS, and the same set under all 384 elements); the 18336 squared
     overlaps lie in `[25/2048, 13/16]`; (CC) `c²s ≥ 4(c−1)` holds on every pair at `c = 401/400`; `R h*` for
     `R = 1 ⊗ diag(1, (3+4i)/5)` has squared overlap exactly `1949/2048 < 400/401` with every ray; `⟨Rh*|R d* R†|Rh*⟩ =
     −1/400` — so `P_{Rh*}` lies in `PSD ∩ Z*`, pairs negatively with `R d* R†`, and `R d* R†` is outside `K*`
     although `d*` is in it (no use of Theorem S′, as R-E15.3 says).
   - X2 (R-E16.1): for `d = 1 … 7` and every non-identity diagonal sign involution, `(d+1) tr H = (tr H)²` holds
     exactly when `tr N = −1`; on built matrices `tr(H ⊗ 1) = (d+1) tr H` and `tr(H ⊗ H) = (tr H)²`; the instances
     `(d, #+1 of H) = (1,1), (3,2), (5,3), (7,4)`; `relC` and the derived identity `G actC G⁻¹ = actC actT` hold
     exactly for `G = Ad(CNOT)` on `W 3` with `N = diag(1, −1, −1)` and fail for `diag(−1, 1, −1)` and
     `diag(−1, −1, 1)`, which meet the count (**the count is necessary, not sufficient** — consistent with the row,
     which claims only the exclusion of even chart dimension).
   - X3 (R-E16.3, Ω_h): the chart transport `Φ` of the two-sector qubit; `G = Ad(CNOT on the qubit factors)` is a
     linear map of `W 7` intertwined by the composite transport, an involution, and satisfies `relC` on all 64 basis
     tables with `N = 1 ⊕ nflip ⊕ nflip`, `tr H = 0`; a product (sector 0, `|+⟩`) ⊗ (sector 0, `|0⟩`) goes to a table
     of rank 4; the four states `|s,q⟩⟨s,q|` lie in Ω_h and are perfectly distinguished by four projector effects; the
     effect `t₁` is zero on two distinct states; the midpoint of `|0,0⟩⟨0,0|` and `|1,0⟩⟨1,0|` is a boundary point
     (a non-zero effect vanishes on it, both ball constraints tight), so Ω_h is not strictly convex; an exact element
     of the composite `K` (sector-blockwise PSD) is preserved by `G` and by the drive rotation at `cos t = 3/5` on one
     token, each intertwined by the transport on basis tables.
   - X4 (R-E17.2): lemma (a) exhaustively for `n = 2, 3, 4` (`2ⁿ` symmetric idempotent `{0,1}` matrices, all
     diagonal); lemma (b) exhaustively for `n = 2, 3, 4` (7, 34, 209 matrices with `(VᵀV)² = VᵀV`, none with two ones
     in a column); (c) for `n = 2, 3`, every monomial unitary with phases in `{1, i, −1, −i}` (32 and 384): `Ad(U)`
     maps all units to `{0,1}` iff the phases are equal, and then transports along the permutation; the non-monomial
     `[[3,4],[−4,3]]/5` maps `E_00` outside `{0,1}`.
   - X5 (R-E18.1): the three identities (AM–GM, Bernoulli at exponent six, `form_eq`) by exact evaluation on
     determining grids; `B ≥ 0` on all pairs of 137 exact `PC` points with minimum `0`; the tight pair
     `(1, 1/8, (1/4,0,0))`, `(1/8, 1, (−1/2,0,0))`; the converse witnesses of the module in all three cases
     (`u′,v′ > 0` at two points with `B = (θ−1)S′ < 0`; `u′ = 0`: `B = −2/3`; `v′ = 0`: `B = −5/6`), each `z` in `PC`.
   - X6 (R-E15.4, §G): `dict (actT ω) = U dict(ω) U†` on all 16 basis tables for `rotLin` at `cos t = 3/5`, at
     `t = π/2` and for `cycEquiv` with the module's `cycMat` (`cycMatᴴ = cycMatH`; `U_J` unitary).
   - X7 (R-E15.2): the minimum normalized `|det Ψ_z|²` over the 192 rays is `85/2048 ≥ (1/c)(1 − 1/c) = 400/160801`,
     so `c λ_max ≤ 1` and every defect admits every product (H1); `⟨h*|d*|h*⟩/‖h*‖² = −1/400`, `d*` not PSD;
     `dict(z*) = d*/8` for `z* = E00/2 − (c*/8) T_{h*}`.
   - X8 (R-E16.4): `y = (5/6, 0, 0, 5/6)` lies in Ω₄ (`(x·x)² + s⁴ = 1250/1296`) and `(1,y)·(1,−y) = −7/18`; the
     support of Ω₄ in `e₀` and `e₃` is 1; the scaled point in the 4-ball pairs `1/2 ≥ 0` with its negative.
   - Countercontrols (all failing as stated): (CC) at `c′ = 301/300` on the minimal pair (`90601/7372800 < 1/75`);
     `(1 ⊗ diag(1, i)) h*` has overlap `1` with a ray of `Z`; the chart-4 tokens' NOT gives `5` against `1`;
     `Ad(diag(1, i))(E_01) = −i E_01`; with the exponents swapped, two points of `PC′` pair `−679/6144`.
4. **Modules read.** `lean/EqvK2Converse.lean` (sha256 `240abaf6…`, dev blob `4add9b8d`, 9 declarations printed):
   `dict_eq_sum_tensorOf` (the split along the control index), `tensorOf_conj`, `tokMat_eq`, `tokMat_rot`,
   `tokMat_cyc` (entrywise, by `Complex.ext` and `linarith` over `sin² + cos² = 1`), the intertwining lemmas
   `dict_actT_rotLin` for every real `t` and `dict_actT_cyc`, `Q3_aMiss` (`PosSemidef.mul_mul_conjTranspose_same`),
   and `pairCone_eq_Q3_iff_drive` whose `→` is `Q3_aMiss` after `rintro rfl` and whose `←` is
   `EqvK2Schema.pairCone_eq_Q3_of_drive` — two witnesses, as §A.34 asks; **`Q3_aMiss` is a statement about the set
   `Q3`, nothing in the module names a protocol.** `lean/EqvTransport.lean` (sha256 `0f8aa17a…`, dev blob
   `fadf980e`, 9 printed): the unit algebra (§A), lemma (a) through the row sum `Σ_j P_ij = P_ii` and nonnegativity of
   real parts, lemma (b) through `|G_jj|² ≤ Σ_k |G_jk|² = Re G_jj` against `G_jj ≥ 2`, (c) by choosing one support
   point per configuration (`choose`), injectivity from disjoint supports, surjectivity by finiteness, and the sandwich
   `α(E_cc′) = α(E_cc) α(E_cc′) α(E_c′c′)`; `TransportHDyn` and `Passage` are `def … : Prop` (the passage is **stated,
   not proved**, as R-E17.1 says); `oiSystem_transportHDyn` uses the kernel's `hat`, `transported` and `α_stage`
   (QuasilocalAlgebra / QuasilocalCharacterization at L). The failed copy differs from the built module by the opened
   `Matrix` notation and typed lambdas only (the thread's reading: proof-only repair; the statements compared).
   `lean/EqvPowerCone.lean` (sha256 `477a9f1f…`, dev blob `e7d7a286`, 7 printed): `PC`, `B`, `form_eq`, `amgm` by the
   factorization `(a−b)²(a+8b)`, `B_nonneg` by the chain `(X·X′)⁶ ≤ (S S′)³ ≤ (u u′ (v v′)²)² ≤ ((u u′ + 2 v v′)/3)⁶`,
   `bernoulli6`, `mem_PC_of_dual` by the three explicit witnesses, `PC_selfDual`. The module has no OI content, as its
   header says.
5. **Written arguments read.** Draft S6: the statement "given H1–H3 and `ReachPure`, `K = Q3` iff A_miss" with both
   directions named, the scope section (cone-level equivalence; availability (A)/H-OI_g a separate H-level question;
   A_miss introduced; (b) independent of the transferred pair-level premises at L, not shown independent of OI), the
   hypothesis table against the inventory, the evidence-layer table, the exact layer, the decision rules (no rule reads
   another cell), the earned reading and the non-inference rule, the invariant→checkpoint table with `C0` and `C0′`
   met — a research draft, not a control plane, as it says; the design-evidence table matches the CI records (method
   7). NOTES-E16 §3 (G1) the count: sound, X2; (G2) the dichotomy: `d = 1` by `not_drivable_Icc` after an affine
   transfer of drivability, `d = 3` by R-E2.6 ([W] + [L], not re-derived here); (G3) Ω_h: the blockwise argument from
   `nativeGate_cnot`, `entangling_cnot` and `Q3_selfDual`, instances by X3; (G4) product-form pair self-duality
   reduces to token self-duality (the written step not re-derived; the Ω₄ witness by X8); (G5) the residual stated
   as a question. NOTES-E17 §2: the reading rules fixed before dispatch. NOTES-E18: the two proof devices departing from
   S0 recorded.
6. **Kernel citations.** The coordinator's sweep (`cite_check_r4.py`, lines added since `c10dbaee`) finds 93 distinct
   `File.lean:NNN` strings; nine are module-internal lines of the thread's own design modules (EqvK2Schema.lean:297,
   :308, :453; EqvK2Converse.lean:226; EqvTransport.lean:439; EqvPowerCone.lean:313; EqvOmega4.lean:157, :530) and one
   is the thread's own checker's countercontrol string (`NoSuchModule.lean:1`); the remaining **84/84 resolve at L**
   (`cite_check_r4_equivalence.out`): 29 with the named identifier in the window, 51 naming no identifier, and four
   window misses inspected by hand — CompositionOrder.lean:348 is `finiteOrderOn_of_stagePreserving` (the name in the
   same sentence, `psd_iff_trace_nonneg`, belongs to the neighbouring citation JordanClassification.lean:84, verified),
   CompositeDimension.lean:97 is `W` (the names `actT_reflY_phiW`, `cnot_idW`, `chain_value` belong to K2Guard.lean:106,
   :110, :134, each verified), DiscreteCompletion.lean:1929 is `fixedGateTheory_derivedOI` (HO-17's inbox copy),
   TransitiveBody.lean:109 is `chartBody_isCompact` (HO-9's inbox copy; `not_infiniteOrderOn_chartBody_of_binary` is a
   dev-branch name, as that handoff says). The module-internal lines were read against the `lean/` copies: :297 is
   `subset_Q3_of_pure_dual`, :308 `Q3_subset_of_pure`, :226/:439/:313 the first `#print axioms` line of each module.
   The thread's own `e8_cite_check` run 5 (74 distinct citations, 153 occurrences, 69 named pairs, `CITATIONS-RESOLVE`)
   replays identically. All correct.
7. **Design runs** (`CI-RUNS-R4.md`). 38112020014 (`dev-equivalence/r4-design` @ `2d978412`): Build **failure** at
   `EqvTransport` only (the `Matrix`-scoped notation `ᴴ` not opened at four sites, an untyped-lambda projection, the
   consequent unknown constant), `EqvK2Schema` 22/22 and `EqvK2Converse` 9/9 standard, `EqvTransport` 4 standard, 3
   `sorryAx`, 2 not printed; gate skipped; run completed 32 success, 1 failure. 38112803530 (@ `20c207f1`): Build
   success (3647 jobs), `EqvK2Schema` 22/22, `EqvK2Converse` 9/9, `EqvTransport` 9/9, `EqvPowerCone` 7/7, all on
   `[propext, Classical.choice, Quot.sound]` (134 prints counted over the saved job log, none wrapped), `lean-axioms`
   OK 5907, gate red only at `lean-manuscript` (4 problems, the four unregistered modules), `legacy-records` 303,
   `v3-receipts` 43; at the time of this audit the run was still in progress (30 success, 1 failure, one A42 shard
   running). Nothing cancelled; the third dispatch unused. The dev branch is cut from L and differs from it by the four
   modules and three aggregator import lines (verified); the thread's `lean/` copies equal the dev-branch blobs at
   `20c207f1`, the failed copy equals the blob at `2d978412` (verified). Design evidence only; nothing certified.
8. **Acceptance-criteria checks (owner, 2026-10-11).**
   - *Hypothesis classification against the inventory.* Every round-4 row states its form with each hypothesis
     either an inventory item by id or flagged introduced. The records cited were read at `research/archive` @
     `4dc0321c` (`pt/I3/INVENTORY.md`, sha256 `51eff9af…`): I3.8, I3.9, I3.10, I3.43 assumed; I3.66 assumed/open;
     I3.89 proved [K]; I3.144 not at L ([D] preflight); I3.148, I3.149 PT-record assumed; I3.150, I3.153 PT-record
     open; I3.165, I3.167, I3.168, I3.172, I3.173, I3.174, I3.177 open — the kinds and statuses the S6 table and the
     E16 rows assign. S6's form OI + {H2, H3, A_miss, `ReachPure`} ⇒ `K = Q3` and OI + {H2, H3, `ReachPure`} ⇒
     (`K = Q3` ↔ A_miss) are stated with the braces filled; E16.1–E16.2 are the round's only results of the form
     "OI ⇒ X", every hypothesis of kind (i); E16.3 names its three introduced hypotheses; E17's transport form is
     introduced and the inventory has no item for it; E18 has none. No introduced hypothesis is used as an OI premise.
   - *Pair-level versus full-OI insufficiency.* No row claims independence of OI: R-E16.3 says "independent of these
     premises at L, not of OI"; S6's scope section says (b) is independent of the transferred pair-level premises at
     L and the 68 rows not reached have not been shown irrelevant; the reworded R-E4.1 and LEDGER K2 row carry the
     admissible wording. **Deviation recorded:** these two older surfaces were reworded in place under addendum 3
     (old text in the LOG entry of 04:33Z), and NOTES-E3 §4's round-1 sentence "found independent of everything at L"
     stands as a node record with the LEDGER and RESULTS rows as the reading; accepted, since the surfaces the
     corpus reads are the rows. The coordinator's own records quoting the old wording: none found (`OVERVIEW.md`
     and the handoffs grepped); HP-11 item 7 is met by HO-29 item 3 from here on.
   - *Cone invariance versus operational availability.* R-E15.4, S6 §G and the scope section, HP-13 and now HO-29
     name the invariance reading explicitly; `Q3_aMiss` is a property of the set `Q3` (method 4); no round-4 row
     derives availability from invariance; (A)/H-OI_g is listed as not in S6.
   - *Decisive result forms.* E16 delivers the owner's third form, a precisely scoped OPEN (R-E16.5), together with
     a negative answer for the listed premises (Ω_h) that is not labelled an independent bridge; E15 delivers a
     draft, no bridge is claimed derived or independent; the C21 safeguard is kept in R-E15.3 (`K* ≠ Q3` alone would
     show only that some instance of A_miss fails; the non-invariance at `θ₀` is exhibited directly).
   - *Defeated alternatives named.* R-E15.3 (the finite clause), R-E16.3 (the pair-level hypotheses without K∞-Geom),
     R-E16.4 (self-duality alone; central symmetry alone) each name the alternative in the owner's words.

## Findings by row

| row | thread label | audit |
|---|---|---|
| R-E15.1 | OPEN (draft for owner review) | accepted; the draft read in full (method 5); its design-evidence table matches the CI records; `C0′` met in run 38112803530 |
| R-E15.2 | CONJECTURE ([X]) | accepted; X1, X7 (group 384, orbit 192, overlaps, (CC), `1949/2048`, `85/2048`, `dict(z*) = d*/8`) |
| R-E15.3 | CONDITIONAL on Theorem S′ for H3 of `K*` | accepted; the non-invariance witness needs neither S′ nor `ReachPure` (X1's dual argument); S′ read by the coordinator in round 3 (HO-24), not re-checked |
| R-E15.4 | CONJECTURE ([D] run 38112803530) | accepted; the module read (method 4), X6, the run verified (method 7); invariance reading only, as labelled |
| R-E16.1 | CONJECTURE ([W] + [X]) | accepted with the precision that the count is necessary, not sufficient (X2); RelcSelectParity.lean:354 and CompositeDimension.lean:2888 verified at L |
| R-E16.2 | CONJECTURE ([W]; `d = 3` step [W] + [L]) | accepted; KInfFoundations.lean:529 verified; the `d = 3` step rests on R-E2.6 as the row says |
| R-E16.3 | CONJECTURE ([X] + [W]) | accepted; X3 for `relC`, the involution, `Entangling`, the four states, the K∞-Geom failure, the boundary segment and the composite `K` instance; the remaining kernel-form clauses rest on the thread's probe and written proof; wording "not of OI" as required |
| R-E16.4 | CONJECTURE ([W] + [X]) | accepted; X8 for the Ω₄ witness; the reduction to token self-duality is a written step, not re-derived |
| R-E16.5 | OPEN | accepted; correctly scoped; the assumption-watch marker carried to HO-28 |
| R-E17.1 | CONJECTURE ([D]; `Passage` [W] as R-E14.2) | accepted; `TransportHDyn` and `Passage` are definitions, `Passage` unproved, as the row says; the kernel references (QuasilocalCharacterization.lean:168, :463, :475; QuasilocalAlgebra.lean:1109) verified |
| R-E17.2 | CONJECTURE ([D] + [X]) | accepted; X4; the three proofs read |
| R-E18.1 | CONJECTURE ([D] + [X]) | accepted; X5; the module read |
| R-CITE.4 | [X] exact text check | accepted; replay identical; the coordinator's independent sweep agrees (method 6) |
| R-E4.1, LEDGER K2 (reworded) | CONDITIONAL (unchanged labels) | accepted as the admissible wording; the in-place rewording recorded as a deviation (method 8) |

No label changes. The thread's recorded deviations (dev-branch writes under `verification/`; in-place amendments of the
round's rows, notes and draft under addenda 1–3 and of two older surfaces under addendum 3; NOTES-E16's body-hypothesis
classification corrected before its closing commit; dispatch 1's `EqvTransport` blob differing from NOTES-E17 §2's text
by one `first` fallback; `EqvK2Converse` read PARTIAL in dispatch 1 by the rule's letter; E18's two proof devices; two
LOG time corrections; the scratch check and the dry run of the citation checker, uncommitted; NOTES-E17's `OISystem`
reference made a full citation before run 5; no local Lean toolchain) are each in the LOG and change nothing audited
here.

## Handoff items

- HP-11 item 1 → **HO-18 v2** (item 2 corrected: LOWER `Q3_subset_of_pure`, UPPER `subset_Q3_of_pure_dual`, the
  hypothesis of both every pure state, not the products; v1 stays in place). HP-11 items 2–7 are addressed to the
  coordinator and recorded in `OVERVIEW.md` (S6 ready for owner review; the answer to the decisive question; E17–E18
  in design; the two design runs; the admissible wording).
- HP-12 → **HO-28** to the countermodels thread (cc bridge): the count with the coordinator's necessary-not-sufficient
  precision, the dichotomy, Ω_h with the coordinator's X3 scope, the failing weaker alternatives, the residual target,
  the refined assumption-watch marker.
- HP-13 → **HO-29** to the bridge and origin threads: the necessity direction as invariance only, the intertwining
  for every angle in design, the admissible wording for (b).
