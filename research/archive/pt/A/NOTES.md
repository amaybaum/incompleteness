# Thread A (PAIR-COMP) — working notes and node log

Research only. Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only).
Brief: `pt/PROTOCOL.md` (sha256 `239dc123…fa9b23`) and amendment 1 `pt/PROTOCOL-AMENDMENT-1.md`
(sha256 `b41aa0e7…31cf83`, received mid-run; it requires the (A-i)/(A-ii) split and the "sufficiency proved" versus
"survives the countermodels" marking). Nothing here is adopted; no git write, PR, CI or agent was used.

Evidence tags as in the protocol: [K] kernel identifier at L; [D] design-run module at `ff9c3a35`; [X] exact script in
this directory; [W] written; [E] exploration lead; [L] literature not read at the source. "Landed X" means an exact check
of the certified round KT4-PREM-1 (`kt4_prem1_probe.py`), cited by its check id.

## Reading log (before any node)

- Read in full: `round-kt4-prem-1-premise-audit/result.md` and `preregistration.md`; `StageCompletion.lean`,
  `CompletionAction.lean`, `CompositeInterface.lean`, `K2Guard.lean`, the §A–§B and §K–§L parts of
  `CompositeDimension.lean`; the design modules `FourCopyDefs`, `FourCopyCore`, `FourCopyHeadline`, `FourCopyBipolar`,
  `FourCopyBridge`, `FourCopyPackage` (and the declaration lists of the others); `kt4_prem1_probe.py` in full.
- Ledgers read as leads: `OISTAGE-RESULT.md`, `K2-LEDGER.md` (D1–D6, T1–T10), `ASSUMPTIONS.md`, `DEPGRAPH.md` §4.3,
  §5–§7, and the parts of `EQ2-SYNTHESIS.md`, `INTEGRATION-DESIGN.md`, `DRIVE-RESULT.md` that mention finite rank.
- Where `hcl` is consumed in the design proof ([D], read from the code): `kt4_general_ie1`
  (`FourCopyHeadline.lean:102`) uses it twice — `inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)` (Lemma R,
  `FourCopyBipolar.lean:148`) and `bidual_of_adm (hadm p) (hcl p)` (`FourCopyBipolar.lean:110`), whose output `hbi`
  feeds `cross_rel`, the four `inv_*` lemmas and `ie1_of_dualW` in `ie1_all`. No other use (grep of `IsClosed`, `hcl`,
  `closure`, `hbi` over the design modules).
- Leads that matter here: DEPGRAPH §7.2 ("closedness is redundant for the parity conclusion; every hypothesis passes to
  closures"); EQ3-AUDIT ("cl K01 = Θ(K23*) with no closedness"); K2-LEDGER D6 ("LT is test locality of a joint tower");
  DRIVE-RESULT X-FR (finite rank essential for the drive); the design package's open `kt4_closure`
  (`FourCopyPackage.lean:318`, `sorry`).

## Productivity test (fixed before node 1, as the protocol fixes it)

A finding is a gem iff it is (1) an exact certificate at a stated instance, (2) an exact obstruction for a stated class of
routes, or (3) an exposed hidden assumption. Otherwise record-only. Fixed point: 3–4 consecutive passes without a NEW
finding, or the question answered.

## Pass 1 — the decisive branch (depth-first)

**N0 (A0). What does `hcl` do in the theorem?** Read [D]: only `hbi` and `hinv` (above). Then: every other hypothesis
passes to closures — products and the maxCone bound (maxCone is an intersection of closed half-spaces), the convex-cone
property, `hgate` (gates are continuous), FCC (dual cones are unchanged by closure; the famI/famII values are continuous in
the state slots). So `kt4_general_ie1` applied to `closure (K p)` gives IE1 for every closure and `EvenCycle`
(written W-A0; UNBUILT Lean `lean/PairComp.lean` §2). Check: on `M_cl`, `cl K_cl = Q3` and the conclusion holds for `Q3`
(landed M_cl.4, M_Q); on `M_int` the closure passage does not apply (`hgate` fails for `K_int`). Pressure test (favourable
reading "hcl is inessential"): rejected — IE1 for `K_p` itself fails in `M_cl`; the corollary only locates `hcl`'s role:
transferring IE1 from `cl K_p` to `K_p`. Verdict: POSITIVE/CONFIRMING (DEPGRAPH §7.2, EQ3-AUDIT had the parity and cross
relation parts). Consequence for the search: any source of `hcl` must identify `K_p` with a closed object; no other
content is consumed.

**N1 (A1). The stage-level product.** Defined the narrow product (product preparations, product labels, multiplicative
table, product stage maps; UNBUILT §1) and listed the choices: preparations (products / + mixtures / + native-gate images
/ + (o)-step images [forbidden] / a dense subset of a given cone [P-STAGE2 in disguise]); labels (product only / + joint);
tables (product rule; gate images through the gate's action on `W 3`, which presupposes that the gate acts on
product-test tables). Exact (`a1_stage_product.py`, 25 checks, first run): laws, SC∞ (with a countercontrol), TAB, cnot
closure valid (1444 gate images), `actT reflY ∘ cnot` closure invalid (value −1/2; countercontrol on the cnot orbit ≥ 0),
read-out rank 16 (countercontrol rank 4), table span 16. Verdict: CONFIRMING (COMP-1-DESIGN §2.1 anticipated the narrow
product) + ELABORATING (validity of gate closure is gate-dependent: an exact certificate at two instances).

**N2 (A2). The completions.** Narrow product: completed body = Ψ(normalized SEP), closed, compact, finite rank; not
cnot-invariant (landed I2, value −2). cnot closure: `K_gen = SEP + cnot SEP`, closed, cnot-invariant, admissible.
Exploration (`explore/e1_objects.py` [E]) suggested a PSD-free witness `F = E00/2 − T_ψ/4`; then
`a2_native_closures.py` (rules fixed first). Run 1: 21/21 PASS. Pre-run-2 edit: the run-1 verdict line summarized
`K_gen ⊆ Q3 ⊆ K_E` although the inclusions rest on written steps; added R6 (the symbolic identities behind them, A2.16) and
reworded the verdict to separate exact strictness from written inclusions; run 1 kept as `.run1.*`. Run 2: 22/22 PASS.
Results: `T_ψ ∉ K_gen` by the linear witness `F` with exact SOS certificates (independent of the landed rank/extremality
and NPT routes); IE1 fails for `K_gen`; FCC fails for uniform `K_gen` at −1/8, so H fails by Lemma B1 [D]. The maximal
native closure `K_E = dualW(K_gen) = maxCone ∩ cnot(maxCone)` (the largest admissible cnot-invariant cone): closed,
admissible, cnot-invariant, contains `F ∉ Q3`; IE1 fails (−2/5); FCC fails at −1/2 (witness found by exploration
`explore/e2_fcc_KE.py`, `explore/e3_fcc_KE_witness.py` [E], certified in A2.14). Every admissible cnot-invariant convex
cone lies in `[K_gen, K_E]`; `Q3` and `K_cl` lie strictly inside. Verdict: NEW — exact obstruction for the class "the pair
cone is the closure selected by native generation (minimal) or by native no-restriction (maximal)" at the instance
(cnot, identity locals, uniform cones). Pressure test: the endpoints are certified members of the candidate family and
the FCC values are exact; the obstruction is stated for this instance only.

**N3 (A3). Passage from the completion to `W 3`.**
- N3.1 The read-out `T` exists once 16 spanning product labels are labels (A1.10); it is continuous (finitely many
  coordinates). Injectivity of `T` on the completed body is local tomography of the completed pair system.
- N3.2 Under finite rank, the completed body is compact and `T(body)` is compact, so the cone over it is closed (W-A3.1,
  [K] ingredients). Injectivity is not used. `D_pad` (`a4_identification.py` A4.4–A4.7): finite rank, LT fails, closed
  shadow — the closedness argument does not consume LT.
- N3.3 Without finite rank the closedness does not reach `W 3`: the system `D_cl` (product labels with bi-affine tables,
  plus joint labels `b_S` making a dense family of interior preparations ℓ¹-separated) has the landed foil `K_cl` as the
  cone over its shadow (written W-A3; exact skeleton `a3_shadow_countermodel.py`). Run 1: 14/14 PASS; pre-run-2 edit: the
  run-1 verdict said "rank grows without bound" while the exact check covers n ≤ 4 — added the written one-line
  generalization A3.W3 and reworded; run 1 kept. Run 2: 14/14 PASS, PASS/FAIL lines identical to run 1. Verdict: NEW —
  exposed hidden assumption: the closedness content of P-STAGE2 is finite rank (compactness) of the pair completion, not
  completion per se and not LT. The same construction realizes `M_int`'s cone (A3.11 + written A3.W2).
- N3.4 K2 does not give `hcl`: the slice of `K_cl` is an LT COMP-1 Composite (landed Q2/I1W; I1 re-checked, A4.8).
  CONFIRMING.

**N4 (A4). Identification.**
- N4.1 Which feature excludes `K_cl`: finite rank of the completion together with the identification; the completion's
  closure in ℓ^∞ alone does not (N3.3). For countably indexed systems the finitely preparable cone cannot contain all pure
  product rays (uncountably many extreme rays of maxCone), so `hadm` already forces limit points (W-A4.1); with an
  uncountable index preorder every convex set, `K_cl` included, is a finitely preparable set. ELABORATING.
- N4.2 ID (the theorem's cone is the cone over the read-out of a finite-rank pair completion): (⇒) `hcl` by W-A3.1; (⇐)
  for a closed admissible cone the per-cone system `D_K` (product labels, dense preparations) realizes it (W-A4.2; exact
  instances A4.1–A4.3). So, as a condition on the theorem's `K_p`, ID ⟺ `hcl` relative to `hadm`: a restatement.
  Since `D_K` is injective (LT), the same holds for P-STAGE2 itself: as a condition on `K_p`, P-STAGE2 ⟺ `hcl` relative to
  `hadm`; its LT clause constrains the witnessing system, not `K_p`. NEW (sharpens the landed record's "P-STAGE2
  presupposes … K2": for `hcl`, the LT clause is satisfiable for every closed admissible cone; LT is a substantive premise
  only for a given pair system).
- N4.3 Instance characterization (cnot, identity locals, uniform): the models of `hcls ∧ hadm ∧ hgate ∧ H` are exactly
  the cnot-invariant convex cones between `K_cl` and `Q3` (W-A4.4, using W-A0, the landed written classification with its
  one Lie-theory input, and `int cl K = int K` for convex sets [L]). `K_cl` is the smallest model; `hcl` ⟺ `K = Q3` ⟺ every
  rank-deficient state of `Q3` lies in `K`. ELABORATING (sharpened gap), conditional on the written classification.

**N5 (A5).** Ledger and independence in RESULT.md §2–§3.

## Pass 2 — other closure principles (no NEW finding)

- N6 Twisted self-duality `K01 = Θ(K23*)`: implies closedness (dual cones are closed, Θ is a linear isomorphism); relative
  to the other hypotheses the closure form gives `cl K01 = Θ(K23*)` [D + W], so self-duality ⟺ `hcl` at the pair:
  restatement relative to H.
- N7 No-restriction `K = dualW(dualW K)`: ⟺ `hcl` for nonempty convex cones (`dualW_dualW` [D]). Restatement.
- N8 Minimal / maximal gate-invariant admissible cone: `K_gen` / `K_E` (N2). Independent, inconsistent with H at the
  instance.
- N9 "The pair cone is the closure of what is preparable at finite stages": this is ID (N4.2); with the closure taken in
  ℓ^∞ it needs finite rank to reach `W 3` (N3.3).

## Pass 3 — sources of finite rank and of richer generation (no NEW finding)

- N10 Product labels only (with TAB) give finite rank and LT together (W-A3.3) — this is K2-LEDGER D6's relocation of LT:
  using it is a use of K2, named.
- N11 Finite rank of the two factors does not give finite rank of the pair: `D_cl`'s factor marginals are ball states and
  its completion has infinite rank (N3.3).
- N12 (open lead, not settled) Native closure under an N-CLASS gate of infinite order: by Milman's converse of
  Krein–Milman [L], a pure state lies in the closed convex hull of the orbit of the pure products only if it is itself in
  the closed orbit; a pure eigenvector of the gate that is entangled is then never reached. Not pursued to a certificate;
  recorded as open.

Three consecutive passes (2, 3 and the pressure tests of pass 1's favourable readings) produced no NEW finding beyond
pass 1; the question is answered (GAP with sharpened statement). Stopped.

## Pressure tests of favourable readings (§A.31)

- N0 "hcl is inessential": rejected (above).
- N3.2 "LT is not needed": holds for closedness only; for the correspondence of the completed state space itself to
  `K_p` (P-STAGE2's injective chart) LT is exactly what is used. Both uses are stated in RESULT.md.
- N4.2 "P-STAGE2 is just hcl": holds as a condition on `K_p` (existential over systems). For a given (OI-constructed)
  pair system, LT and finite rank are substantive and unsourced.

## Runs and pre-run edits

| script | runs | pre-run edits |
|---|---|---|
| `a1_stage_product.py` | 1 | none |
| `a2_native_closures.py` | 2 (run 1 kept as `.run1.*`, 21/21 PASS) | before run 2: R6 and A2.16 added; verdict reworded (inclusions written, strictness exact) |
| `a3_shadow_countermodel.py` | 2 (run 1 kept as `.run1.*`, 14/14 PASS) | before run 1: countercontrol C4 changed from a vacuous rank bound to "rank < 8"; before run 2: note A3.W3 added, verdict reworded (n ≤ 4 exact, generalization written) |
| `a4_identification.py` | 1 | none |
| `explore/e1–e3` | 1 each | exploration [E]; e2 ran in the background (slow sympy search) |

## Addendum — amendments 1 and 2 (received mid-run; applied in RESULT.md)

- Amendment 1 (sha256 `b41aa0e7…31cf83`): RESULT.md separates (A-i) completion from (A-ii) correspondence, names every use
  of local tomography, and marks each implication "sufficiency proved" or "survives the countermodels" (none of mine rests
  on the latter).
- Amendment 2 (sha256 `2a2f78f3…c530a`): per-target labels. The pass-1 summary above says "GAP with sharpened statement";
  in amendment-2 vocabulary:
  - (A-i) completion: DERIVED (constructed systems; `body_isClosed` [K]; [W] laws; [X] instance);
  - (A-ii) correspondence, and `hcl` for the theorem's `K_p`: INDEPENDENT of the premises certified at L as stated. The
    countermodel is `M_cl` realized as `D_cl`; every certified premise bearing on the target is listed with its check in
    RESULT.md §0.1. It is not independent of `FiniteRank ∧ ID` or P-STAGE2, which imply it but restate it relative to
    `hadm`.
  The models of single routes (`D_cl` for the finite-rank-free route, `K_cl`'s slice for K2, `K_gen`/`K_E`/`SEP` for
  native identification) are recorded as "route refuted", not as independence results in their own right. The scope of
  every [X] statement is the instance it checks; universal statements rest on symbolic identities or on [W].
