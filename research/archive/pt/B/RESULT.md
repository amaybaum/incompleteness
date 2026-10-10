# Thread B — PAIR-ACT: gate preservation — RESULT

Research only. Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`). Design modules:
`pt/inputs/fourcopy/` (exported from `ff9c3a35`). Protocol `PROTOCOL.md` with amendments 1 and 2 (hashes in §7).
Evidence tags: [K] certified at L (file:line); [D] design-run only; UNBUILT = Lean text never compiled (not a kernel
proof); [W] written argument; [X] exact computation in this directory, replayed byte for byte; [F] floating point;
[L] literature. `CD` = `OIBridge/CompositeDimension.lean`, `CI` = `CompositeInterface.lean`, `CA` = `CompletionAction.lean`,
`K1B` = `K1Bridge.lean`, `K2G` = `K2Guard.lean`, `RSB` = `RelcSelectBlock.lean`, `PN` = `ParityNot.lean`, `ES` =
`EffectSpace.lean`, `OG` = `OrbitGeneration.lean`, `KIF` = `KInfFoundations.lean`, `TB` = `TransitiveBody.lean`, all under
`pt/base/verification/lean-mathlib/`.

## 0. Answer

Notation: `H0 = hcls ∧ hadm ∧ hcl ∧ H` at the four pairs; `C` = IE1 at every pair ∧ `EvenCycle`.

**T1 — `hgate` (each native gate maps its pair cone into itself): INDEPENDENT** of the premises certified at L as
stated. Exact countermodels at one pair, `M_max = (maxCone (eball 3), cnot)`, built from landed objects only, and
`M_D13 = (Q3, actT reflY ∘ cnot)`, satisfy every certified premise bearing on `(K, N)` — thirteen items, each checked
[K/X/W]; a text census of all 215 landed sources finds no other landed predicate over the pair carrier [X] — and
violate `hgate` [X]; the landed native-gate hypotheses even admit gates (`g_D`, `g_pre`) that preserve no admissible
cone [X]. Every principle found that implies `hgate` restates it (sufficiency proved; restatement: `JointReversible` /
`PreservesBody` of the pair slice, P-ACT2 = K∞-Act on a pair system with P-STAGE2, reversibility of the gate as an
operation on the pair state space) or is forbidden here (idle extension on the gate's local factors, which K2-GUARD-1
moreover excludes for reflection factors); every other candidate is route refuted (the K1 premises, EFF-1 /
K1-BRIDGE-1, the COMP-1 interface, OPACT-1 as landed, FCC, PRP, TBP, self-duality, product-level idle extension).

**T2 — a weaker clause in place of `hgate` (B1): sufficiency proved; the clause is INDEPENDENT** of the premises
certified at L as stated. The design proof consumes `hgate`/`hinv` only at CONS — the link tables (L), the Bell table
in `K_p` (BS), the Bell table in `dualW K_p` (BD) — and `H0 ∧ Γ ⇒ C` holds for Γ = CONS, OQ1 (open question 1's
clause), SECT (⟺ GT-COMP) and PREC: a written argument over design-run lemmas [W over D] that replaces each consuming
step (`link_mem`, `bell_mem`, Lemma R, `bell_mem_dual`, `parity_witnesses`), checked by exact text diffs, an
implicit-use scan and table identities [X], and transcribed as UNBUILT Lean (not a kernel proof). Each Γ is strictly
weaker than `hgate` under `H0` (`M_pre`, `M_DD`) and fails in `M_max` (BD) and in `M_D` (BS) [X]; no clause invariant
under the post-local reflection σ can both suffice and hold in `M_max` (Lemma O, a rigorous impossibility theorem for
that class [W with exact identities]).

**Implications.** Sufficiency proved: `H0 ∧ Γ ⇒ C` for the four Γ; under `H0`,
`hgate ⇒ PREC ⇒ SECT ⇒ OQ1 ⇒ CONS` [W; UNBUILT, except PREC ⇒ SECT: W only]; `JointReversible ⇒ hgate` and
`P-ACT2 ∧ P-STAGE2 ⇒ hgate` [K + X + W]. Survives the countermodels only: none claimed. Refuted by an exact
countermodel to the theorem with the clause in place of `hgate`: the separations SECTst, BS, PRP (hold in `M_max`,
fail in `M_D`; countermodels `M_maxD`, `M_maxT`), BD, SECTef, TBP (`M_SEPD`), SECT′ (`M_D`). Route refuted
("candidate ⇒ `hgate`"): every candidate source under T1 that is not a restatement or forbidden.

## 1. Routes and countermodels, node by node

### Objects

- Gates (all N-CLASS, `N = actC A ∘ actT B ∘ cnot ∘ actC A' ∘ actT B'`, orthogonal locals; b1_models G.*):
  `cnot` (all locals I, orient false); `g_D = actT reflY ∘ cnot` (B = reflY, orient true); `g_pre = cnot ∘ actT reflY`
  (B′ = reflY, orient false); `g_Tw = actT reflY ∘ cnot ∘ actT reflY` (B = B′ = reflY, orient true).
- Cones: `Q3`; `twin = actT reflY Q3`; `maxCone = maxCone (eball 3)` [K CD:186]; `SEP` = convex cone of the product
  states. Tables: `pxz = prodState xplus z3`, `phiW` [K CD:1220], `idW`, `chainW` [K K2G:101, 104].
- Clauses at one pair (`K = K_p`, `N = N_p`, post-locals `(A, B)`):
  `hgate`: `N K ⊆ K`. `PREC`: `∃` orthogonal `C, D`, `N ∘ actC C ∘ actT D` maps `K` into `K`.
  `SECT`: `N (prodState x y) ∈ K` for all `x, y ∈ eball 3`, and `N⁻¹ K ⊆ maxCone`; `SECTst`, `SECTef` its two halves.
  `OQ1`: `SECTst` and `bellOf A B ∈ dualW K`. `CONS`: (L) `actC (A ∘ rotWord a b) (actT B phiW) ∈ K` for all `a, b`;
  (BS) `bellOf A B ∈ K`; (BD) `bellOf A B ∈ dualW K`. `PRP`: `N^{±1}` (products) `⊆ K`. `TBP`: `N^{±1} K ⊆ maxCone`.
  `SECT′`: `N⁻¹` (products) `⊆ K` and `N K ⊆ maxCone`. `GT-COMP`: the normalized slice of `K` with the gate-transported
  product data (`N ∘ prodState`, `prodEff ∘ N⁻¹`) is a COMP-1 `PreComposite` [K CI:223].
- Models (identity locals unless stated; cones uniform unless stated; pair order 01, 23, 02, 13): `M_Q` (Q3, cnot);
  `M_D` (landed: Q3, `N_13 = g_D`); `M_D13` = pair 13 of `M_D`; `M_max` (landed: maxCone, cnot); `M_SEP` (SEP, cnot);
  `M_maxD`, `M_maxT` (maxCone, `N_13 = g_D`, resp. `g_Tw`); `M_SEPD` (SEP, `N_13 = g_D`); `M_pre` (Q3, `N_13 = g_pre`);
  `M_DD` (cones Q3, twin, Q3, twin; `N_23 = N_13 = g_D`); `TWIN` (twin, cnot); `M_int` (landed).

### B1.1 — the consumed clause (NOTES N0, N1, N11)  [verdict: CONFIRMING; exact]

On the path of `kt4_forward_ie1` [D FourCopyHeadline:120], `hgate` and `hinv` occur only in the twelve declarations of
b1_consumed's frozen list, with matching counts [X S1.uses]. `kt4_general_ie1` [D :102] produces `hinv` by Lemma R
(`inv_mem_of_orth` [D FourCopyBipolar:148]), `hbs` by `bell_mem` [D FourCopyLocal:266] and `hbe` by `bell_mem_dual`
[D :274] from `hinv`; `ie1_all` consumes `hgate` only through `link_mem` [D FourCopyIE1:286]; `parity_all` through
`parity_witnesses` [D :528], which reads `hgate` only via `bell_mem` and `hinv` only via `bell_mem_dual` [X S1.L, S1.R,
S1.BS, S1.BD, S1.PW]. The instances: `link_mem` applies `hgate` to `prodState (A'ᵀ rot3 a xplus) (B'ᵀ rotX b z3)`, whose
gate image is the link table (L) [X S1.LM, S2.L]; `bell_mem` to the product of `NClass.bell_state`, giving (BS), the
instance `a = b = 0` of (L) [X S1.BM, S2.BS]; `bell_mem_dual` reads `hinv` through `dualW_of_inv` to put the gate image
of a product of sharp effects, `(1/4) bellOf A B`, in `dualW K`, which is (BD) [X S1.BDM, S2.BE]. No tactic consumes
`hgate`/`hinv` without naming them: the only context-reading tactics in their scope (linarith, omega, positivity) read
comparison hypotheses only, and the binder types are memberships [X b1_implicit I1–I5; Mathlib
`Tactic/Linarith/Preprocessing.lean:60`, `Tactic/Positivity/Core.lean:352`, read at the source].

### B1.2 — the decisive controls for CONS and OQ1 (N2)  [verdict: CONFIRMING; exact]

Both fail in `M_max`: (BD) `phiW ∉ dualW maxCone`, witness `dg(1,−1,1,−1) ∈ maxCone` with `ipW phiW · = −2` [X W5;
landed X6]. Both fail in `M_D`: (BS) `bellOf I reflY = idW ∉ Q3` (singlet value −1) [X W13, W2]. The protocol's control
"holds in `M_max`" is not met by the consumed clause.

### B1.3 — Lemma O, the orientation obstruction (N3)  [verdict: NEW — exact obstruction for a stated class]

*Statement.* Let σ_q replace, at one pair q, `(N_q, B_q)` by `(actT reflY ∘ N_q, reflY ∘ B_q)`. Call a per-pair clause Γ
σ-invariant if, whenever `actT reflY K_q = K_q`, Γ holds before σ_q exactly when it holds after. If Γ is σ-invariant and
`H0 ∧ Γ ⇒ C`, then Γ fails on every `H0`-family having an `actT reflY`-invariant cone (in particular `M_max`, `M_SEP`).
*Proof* [W]. σ_q keeps N-CLASS (`actT reflY ∘ N(A, B, A', B') = N(A, reflY B, A', B')`) [X O1] and flips
`orient(A_q, B_q)` [X O2]. If `K_q` is `actT reflY`-invariant, σ_q changes no cone, so it keeps `hadm`, `hcl`, `H` and
IE1 (they read only the cones) and `hcls` (O1), and flips `EvenCycle` (one bit). If Γ held on such a family F, it would
hold on σ_q F, both satisfy `H0`, so C would hold on both, contradicting the flipped `EvenCycle`. `hgate`, PREC, SECT,
OQ1, CONS, SECTst, BS, BD, PRP, TBP are σ-invariant on such cones [W with X O4, Dmax, Dsep, Dadj, Dorth]. On uniform
maxCone or SEP data all 16 patterns in `{cnot, g_D}^4` satisfy `H0`, and C holds exactly for the 8 even ones [X O5,
exhaustive]. The obstruction does not reach `Q3`, which is not `actT reflY`-invariant [X O6].
*Consequence.* No σ-invariant weakening of `hgate` both suffices and holds in `M_max`. A sufficient clause that holds in
`M_max` must read the post-local orientation, and on the 16 uniform-maxCone patterns it can hold only on even ones.

### B1.4 — `hgate` constrains the pre-locals, which C never reads (N4)  [verdict: NEW — exposed hidden assumption]

`M_pre` (uniform Q3, `N_13 = g_pre`): `H0` holds, C holds, PREC/SECT/OQ1/CONS hold (post-locals I: the tables of `M_Q`),
`hgate` fails (`phiW ∈ Q3`, `g_pre phiW = chainW ∉ maxCone`); no admissible cone is invariant under `g_pre` [X W1, W12,
W4, S2.no]. `M_DD`: `H0` (FCC by the token-3 transport F.t3), C (two twisted orientations), PREC (the corrected gate
`g_D ∘ actT reflY = g_Tw` preserves twin [X W14]), `hgate` fails at 23 and 13 [X W12, W4, W2t]. On families with
`K_p = twistQ3(orient(A_p, B_p))`, `hgate` holds exactly when `orient(A'_p, B'_p) = orient(A_p, B_p)` [W N4, with X
D1, Dpt, Dtr, W2t, W12, W4: a local orthogonal map sends `Q3` to `twistQ3` of its orientation, `cnot` keeps `Q3`, and
`cnot twin` contains `chainW`]: `hgate` asks the pre-locals to match the post-locals, a condition C does not read. PREC is `hgate` up to a local orthogonal
pre-correction.

### B1.5 — sufficiency, step by step (amendment 1) (N7, N11)  [verdict: sufficiency proved at W over D; UNBUILT Lean]

| design step consuming `hgate`/`hinv` | replacement in `B1_UNBUILT.lean` | checks |
|---|---|---|
| `link_mem` in `ie1_all` [D IE1:286] | `CONS.link` and `link_target_of_ctrl` (the target-side form from the control-side form, `link_mem`'s own rewriting chain) | [X b1_steps A1, A6, D3] |
| `bell_mem` in `kt4_general_ie1` [D Local:266] | `CONS.bs` | [X A4] |
| Lemma R `inv_mem_of_orth` [D Bipolar:148] | deleted: `hinv` is never produced | [X A4: 7 lines removed, 4 added] |
| `bell_mem_dual` via `hinv` [D Local:274] | `CONS.bd` | [X A4] |
| `parity_witnesses` [D IE1:528] (`bell_mem`, `bell_mem_dual` inside) | `parity_witnesses_cons`, with the Bell state and Bell effect as hypotheses | [X A2, A3] |
| `ie1_all`, `parity_all`, `kt4_general_ie1`, `kt4_forward_ie1` [D Headline:37, 86, 102, 120] | `_cons` copies, `hcons` in place of `hgate` | [X A1, A3, A4, A5] |

[W] The modified proof is the design proof with each consumed fact supplied by CONS; every other step is a design
lemma used verbatim (59 called names, all declared [X C1–C3]); `hcl` is still used, for the bidual (`bidual_of_adm`
[D Bipolar:110]). Hence `H0 ∧ CONS ⇒ C`. The stronger clauses: OQ1 ⇒ CONS (`cons_of_oq1`: `link_mem` and `bell_mem`
with `hgate _ (hprod …)` read as the product clause [X A6, A7]); SECT ⇒ OQ1 (`oq1_of_sect`: `bell_mem_dual` with the
inverse-gate step replaced by `gate_sharp_mem_dualW_of_inv_pos`, which needs only `N⁻¹ K ⊆ maxCone` and the
ipW-orthogonality of N, `NClass.ipW_map` [D Local:221] [X A8, A9, D5]); PREC suffices directly
(`kt4_forward_ie1_prec`: `kt4_forward_ie1` applied to the corrected gates `N ∘ actC C ∘ actT D`, which are N-CLASS with
the same post-locals, `nclass_comp_loc` [X D1, D2], and C reads only the post-locals); PREC ⇒ SECT [W N7: Lemma R for
the corrected gate, and maxCone invariant under local orthogonal maps]; `hgate ⇒ PREC` (`prec_of_hgate`) and
`hgate ⇒ CONS` under `hcls ∧ hadm ∧ hcl` (`cons_of_hgate`). GT-COMP ⟺ SECT, each direction field by field [W N7]:
(⇒) the transported `prod_mem` is SECT's first half (N fixes the unit entry [X D4]) and the transported
`prodEff_effect` is its second half; (⇐) the two halves give those two fields, and convexity, the unit pairing and the
evaluation law hold for every N-CLASS gate [X D4, D6].
Pressure tests of this favourable branch: implicit consumption (B1.1, b1_implicit); exact diffs with a countercontrol
that an extra changed line is rejected [X A.cc]; no `sorry`/`axiom` [X B1]; `hgate` occurs only in the two lemmas that
start from it, `hinv` nowhere [X B2]; every Γ still fails in `M_max` (B1.2, B1.3).

### B1.6 — the model matrix: separations versus sufficiency (N5)  [verdict: NEW refutations; exact]

```
model    H0  C     hgate    PREC    SECT  SECTst  SECTef     OQ1    CONS      BS      BD     PRP     TBP   SECT'
M_Q       Y  Y       Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W
M_D       Y  n       n/X     n/W     n/X     n/X     n/X     n/X     n/X     n/X     n/X     n/X     n/X     Y/W
M_max     Y  Y       n/X     n/W     n/X     Y/K     n/X     n/X     n/X     Y/X     n/X     Y/K     n/X     n/X
M_SEP     Y  Y       n/X     n/X     n/X     n/X     Y/W     n/X     n/X     n/X     Y/X     n/X     Y/W     n/X
M_maxD    Y  n       n/X       -     n/X    Y/KW       -     n/X     n/X     Y/X     n/X    Y/KW       -       -
M_maxT    Y  n       n/X       -     n/X    Y/KW       -     n/X     n/X     Y/X     n/X    Y/KW       -       -
M_SEPD    Y  n       n/X       -     n/X     n/X     Y/W     n/X     n/X     n/X     Y/X       -     Y/W       -
M_pre     Y  Y       n/X     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     n/X     n/X     n/X
M_DD      Y  Y       n/X     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W     Y/W       -       -       -
TWIN      Y  Y       n/X     n/W     n/X     n/X       -     n/X     n/X     n/X       -       -       -       -
M_int     n  Y       n/K       -     n/X       -       -     n/X     n/X       -     n/X       -       -       -
```

(`b1_models.run1.out` S7; basis per cell: X exact witness or identity, W written reduction over listed exact checks,
K landed fact — a kernel identifier at L or the landed probe record; the cell-by-cell reasons are printed there.)
Separations that hold in `M_max` and fail in `M_D` — SECTst (= P-PROD), BS, PRP — are not sufficient: `M_maxD` and `M_maxT` satisfy `H0` and the clause and violate C
(EvenCycle fails: one twisted orientation on orientation-blind cones). BD, SECTef, TBP are refuted by `M_SEPD`, SECT′
by `M_D`. `TWIN` satisfies `H0 ∧ C` while every derived-sufficient clause fails: none is necessary, even on self-dual
cones.

### B2.1 — the K1 native-gate premises (N8)  [verdict: route refuted; NEW: no admissible invariant cone]

`IsNot (eball 3) z3 nflip` [K CD:210, isNot_nflip CD:838]; for each of `cnot, g_D, g_pre, g_Tw`: `NativeGate`'s frame
on the corners, relT and relC with `nflip`, a two-sided inverse [X K1.*], two-sided positivity of product images into
maxCone (from the landed `cnot_prodState_mem_maxCone` [K CD:1152] and the `actT reflY`-invariance of maxCone [X K1.pos,
K1.max]); `Entangling` (images of `(xplus, z3)` are `phiW` or `idW`, rank 4, extreme) [X+W K1.ent; K entangling_cnot
CD:1380]; hence `CtrlGate` [K ctrlGate_of_nativeGate RSB:53], `GateRel` [K PN:42]. Yet `g_D` and `g_pre` take `pxz` to
`chainW ∉ maxCone` in two steps, so no cone containing the products and inside maxCone is invariant under them [X S2.no;
countercontrol S2.cc]. "K1 ⇒ `hgate`" and "K1 ⇒ CONS" are refuted by `M_max` and `M_D13`.

### B2.2 — COMP-1: `JointReversible` / `PreservesBody`; the composite interface (N8)  [verdict: restatement; route refuted]

`JointReversible G := PreservesBody P.Ω G` [K CI:445; OG:69] is asserted of no pair gate at L [X S0.jr]. Asserted of
`{N_p}` on the normalized slice of `K_p`, it gives `hgate` by scaling (N-CLASS gates fix the unit entry) [X S4.jr + W]:
sufficiency proved, and it is gate preservation on the slice — a restatement. The interface alone (a `Composite` body
[K CI:243]) does not give it: the landed `ball3MinComposite` and `ball3MaxComposite` [K CI:807, 811] are not preserved
by `cnot` (`cnot pxz = phiW ∉ SEP` [X W14, W7]; `cnot idW = chainW ∉ maxCone` [X W9, W12, W4]); `M_max` is the second.

### B2.3 — OPACT-1: operation datum and completion action (N8)  [verdict: vacuous at L; as P-ACT2 a restatement]

An `OpDatum` carries each stage preparation into the completed body [K CA:46–48, `mem_body`], and a datum with an
inverse datum induces a body-preserving equivalence of the chart [K `preservesBody_inducedEquiv` CA:352]. At L the only
`DirectedStages` values are `badD`, `bitTower`, `midD` [X S0.opd]: no pair system, so OPACT-1 asserts nothing of
`(K, N)`. Instantiated as P-ACT2 (the gate as a datum with inverse on a pair system whose chart body is the normalized
slice of `K_p`, P-STAGE2), it gives `hgate` through `preservesBody_inducedEquiv` and B2.2's scaling — sufficiency
proved, restatement. On a pair system whose preparations are product states only, no datum for `cnot` exists:
`F = dg(1,−1,1,−1)` has `ipW F (prodState x y) = |x − D y|²/2 + (1 − |x|²)/2 + (1 − |y|²)/2 ≥ 0` on products and
`ipW F (cnot pxz) = ipW F phiW = −2` [X S4.pact].

### B2.4 — EFF-1 / K1-BRIDGE-1 (N8)  [verdict: route refuted]

`NativeGateOf` / `EntanglingOf` [K K1B:49, 64] for an available family whose cone equals maxCone
(`maxConeOf_avail_eq` [K ES:572]; `nativeGate_of_cone_eq` [K K1B:73]) are `NativeGate` / `Entangling`; refuted as B2.1.

### B2.5 — physical reversibility (N13)  [verdict: restatement / route refuted / not a route at L]

(a) The gate and its inverse as operations on the pair state space: `hgate ∧ hinv`, a restatement. (b) Reversibility
as two-sided positivity on products relative to maxCone (`NativeGate.posFwd/posInv`): holds for `g_D`, `g_pre` — route
refuted. (c) Substratum-level reversibility (the matrix-carrier modules, e.g. `MicroscopicReversibility`): no landed
module connects them to the pair carrier [X b2_census R5], so at L it is not a route to `(K, N)`.

### B2.6 — the certified-premise checklist and the census (N8, N10)  [verdict: INDEPENDENT established for T1, T2]

Each item, for `M_max = (maxCone, cnot)` and `M_D13 = (Q3, g_D)` [X b2_sources S3]:

| # | certified premise bearing on (K, N) | M_max | M_D13 |
|---|---|---|---|
| 1 | `IsNot (eball 3) z3 nflip` [K CD:210] | K isNot_nflip | K isNot_nflip |
| 2 | `NativeGate` (frame, posFwd, posInv into maxCone, relT, relC) [K CD:218] | K nativeGate_cnot CD:1160 | X K1.g_D, K1.pos, K1.max + K CD:1152 |
| 3 | `CtrlGate` [K RSB:45] | K ctrlGate_of_nativeGate | from 2 (K RSB:53) |
| 4 | `GateRel` [K PN:42] | K gateRel_cnot PN:418 | X K1.g_D |
| 5 | `Entangling` [K CD:229] | K entangling_cnot | X+W K1.ent |
| 6 | `NativeGateOf` / `EntanglingOf` with a family whose cone is maxCone [K K1B:49, 64; ES:572] | W: 2 + cone equality | W: same |
| 7 | one common NOT on both copies (K∞-Copy; `CopyNatural` [K KIF:284]) | nflip on both | nflip on both |
| 8 | `CandidateCone K` [K K2G:95] | K prodState_mem_maxCone K2G:165 | W: D5, D6; Q3 ⊆ maxCone |
| 9 | `K` a closed convex cone | W (landed M_max.2W) | W (PSD cone) |
| 10 | the normalized slice of `K` a COMP-1 `Composite` body [K CI:243] | K ball3MaxComposite | W: PreComposite fields from 8, 9; lt in the coordinate model |
| 11 | K2-GUARD-1: no candidate cone invariant under `cnot` and `actT reflY` [K K2G:143] | consistent | consistent |
| 12 | OPACT-1: a datum with inverse preserves the completed body [K CA:352] | vacuous (no pair system) | vacuous |
| 13 | the theorem's other hypotheses (`hcls, hadm, hcl, H`; design level) | landed M_max | landed M_D |

Violations: `idW ∈ maxCone` and `cnot idW = chainW ∉ maxCone`; `pxz ∈ Q3` and `g_D pxz = idW ∉ Q3` [X S3.vio]. CONS
fails in `M_max` for every N-CLASS decomposition of `cnot` (`bellOf A B` is a local orthogonal image of `phiW`, SEP is
invariant under local orthogonal maps, `phiW ∉ SEP = dualW maxCone`) [W with X W7, Dloc, Dsep]. Single-copy premises
(the ball, its automorphisms and sharp effects, K∞-Seed/Trans/V4, EFF-1's availability) take the same value in `M_Q`,
`M_max` and `M_D13`, which share the copies; they do not read `(K, N)`.
Census [X b2_census run 2]: the 215 landed sources at L (glob) contain 53 declarations selected by its rules, each
classified; the 8 Props over the pair carrier (`IsProduct`, `NativeGate`, `Entangling`, `NativeGateOf`,
`EntanglingOf`, `CandidateCone`, `GateRel`, `CtrlGate`) are covered by items 1–8; the 16 modules touching the pair
carrier are classified; three planted countercontrols are detected.

### B2.7 — the remaining candidates (N8, N12)  [verdict: route refuted]

`H`/FCC: holds in `M_max` and `M_SEP` where `hgate` fails. PRP: holds in `M_max`. TBP: holds in `M_SEP`. Self-duality:
`Q3` (in `M_D13`) and `twin` (in `TWIN`) are self-dual and `hgate` fails. K2 as recorded (ROADMAP, OPEN: local
tomography, the composite cone, local actions compatible with it, the composition theorem, the antiunitary / CP bridge,
the relation to K3) does not name the gate's action; its local-actions clause is operation-level idle extension
(forbidden here), a composite cone fixed to `Q3` is the forbidden `Q3` premise, and adding the gate's action restates
`hgate`.

### B3 — restricted idle extension (N8)  [verdict: route refuted / forbidden / circular]

Product-level idle extension is an identity of product data (`actC M (actT M' (prodState x y)) = prodState (M x) (M' y)`)
[X S5.prod]: it holds in every model, including `M_max` and `M_D13`, so it implies nothing about `hgate`. Idle extension
restricted to the gate's local factors (K invariant under each factor of N) implies `hgate` trivially but is
operation-level idle extension (forbidden), and for a reflection factor it leaves `Q3` (`actT reflY phiW = idW`) and,
with `cnot`-invariance, contradicts K2-GUARD-1 [X S5.gate; K K2G:143]. The commutant of `cnot` (`rot3` on the control,
`rotX` on the target) carries (BS) to the links (L) [X S5.comm; countercontrol S5.cc], but only for a K invariant under
those rotations — a fragment of IE1, the target: circular.

### B4 — survivors and independence (N7)

The survivors are CONS, OQ1, SECT (= GT-COMP) and PREC: each is sufficient (B1.5), strictly weaker than `hgate` (B1.4),
and INDEPENDENT of the certified premises (B2.6). None is independently motivated by anything found here: CONS is the
consumed clause by construction; OQ1 and SECT are its product-state forms; GT-COMP is SECT restated in COMP-1 language
(a gate-covariance reading of the composite interface, equivalent to SECT, so not a source); PREC is `hgate` with the
pre-locals freed. Fixed point: N8 was the last NEW finding; N9–N13 produced none (NOTES N14).

## 2. The ledger (certified versus added)

| premise | class | anchor | used by |
|---|---|---|---|
| `IsNot`, `NativeGate`, `Entangling`, `maxCone`, `jointStates`, `cnot`, `cnot_prodState_mem_maxCone`, `nativeGate_cnot`, `entangling_cnot`, `isNot_nflip`, `phiW` | [K] | CD:210, 218, 229, 186, 190, 775, 1152, 1160, 1380, 838, 1220 | B2.1, B2.6, models |
| `CtrlGate`, `ctrlGate_of_nativeGate` | [K] | RSB:45, 53 | B2.1, B2.6 |
| `GateRel`, `gateRel_cnot` | [K] | PN:42, 418 | B2.1, B2.6 |
| `NativeGateOf`, `EntanglingOf`, `nativeGate_of_cone_eq`; `maxConeOf_avail_eq` | [K] | K1B:49, 64, 73; ES:572 | B2.4, B2.6 |
| `CandidateCone`, `prodState_mem_maxCone`, `no_candidateCone_cnot_reflY`, `idW`, `chainW`, `cnotOrbit` | [K] | K2G:95, 165, 143, 101, 104, 182 | B2.6, B3, §4 |
| `PreComposite`, `Composite`, `minBody`, `maxBody`, `ball3MinComposite`, `ball3MaxComposite`, `JointReversible`; `PreservesBody` | [K] | CI:223, 243, 267, 271, 807, 811, 445; OG:69 | B2.2, B2.6 |
| `OpDatum` (`mem_body`), `preservesBody_inducedEquiv`, `body_isClosed` | [K] | CA:46–48, 352, 202 | B2.3 |
| `ball3`, `eball`, `CopyNatural` | [K] | KIF:311, TB:518, KIF:284 | B2.6 |
| the landed models `M_max`, `M_D`, `M_int`, `M_cl`, witness X6 | landed exact record (KT4-PREM-1 probe, blob `5609d96a…`), replayed here: 79 PASS as recorded | `round-kt4-prem-1-premise-audit/result.md` | B1.2, B1.6, B2.6, §4 |
| `kt4_forward_ie1`, `kt4_general_ie1`, `ie1_all`, `parity_all` | [D] | FourCopyHeadline:120, 102, 37, 86 | B1 |
| `link_mem`, `parity_witnesses`, `cross_rel`, `kt4_parity_of_witnesses` | [D] | FourCopyIE1:286, 528, 155, 443 | B1 |
| `bell_mem`, `bell_mem_dual`, `sharp_mem_dualW`, `NClass.ipW_map`, `.apply_prodState`, `.bell_state`, `.bell_effect` | [D] | FourCopyLocal:266, 274, 258, 221, 233, 240, 247 | B1 |
| Lemma R `inv_mem_of_orth`; `bidual_of_adm`; `dualW_of_inv`; `fourCopyCoherent_of_kt4Core` | [D] | FourCopyBipolar:148, 110; FourCopyParity:137; FourCopyBridge:269 | B1 |
| `hcls` (N-CLASS), `hadm` (`PairAdm`), `hcl`, `H` (`KT4Core`) | [D] hypotheses (thread A/C/D targets) | FourCopyCore:132, FourCopyDefs:43, —, FourCopyCore:99 | B1 (the `H0` of every sufficiency statement) |
| K1 inputs (`IsNot`, native-gate and entangling hypotheses for the native gate), K∞-Copy, K∞-Act, K2 | [A] open premises | ROADMAP P1 row (line 68), lines 995–1016 | B2.6 (satisfied by the countermodels), B2.7 |
| P-STAGE2, P-ACT2 | [A] named open premises | `result.md` (Vocabulary) | B2.3 (restatement) |
| CONS, OQ1, SECT, PREC | [N] | §1 Objects | B1.5 (sufficiency), B2.6 (INDEPENDENT) |
| GT-COMP | [N], ⟺ SECT | §1 Objects | B1.5 |
| JR for the pair gate; reversibility on the pair state space | [N], restatements of `hgate` | B2.2, B2.5 | — |

No forbidden premise is used by any route: `Q3` appears only in countermodels; IE1 is never assumed (the commutant
route that would need it is rejected as circular); operation-level idle extension appears only in B3, where it is
rejected; the complex region tower and (o) steps do not occur.

## 3. The candidate table

| candidate | statement | class | implication tested | verdict per countermodel | independence |
|---|---|---|---|---|---|
| `hgate` (target) | `N_p K_p ⊆ K_p` | [D] hypothesis | certified premises ⇒ `hgate` | `M_max` ✗, `M_D13` ✗ (all 13 items hold) | INDEPENDENT |
| JR / `PreservesBody` of the pair slice | N and N⁻¹ preserve the normalized slice | [N] (predicate [K]) | JR ⇒ `hgate` | sufficiency proved [X S4.jr + W] | restatement |
| P-ACT2 = K∞-Act on a pair system | the gate as a datum with inverse datum, inducing N on the P-STAGE2 chart | [A] | P-ACT2 ∧ P-STAGE2 ⇒ `hgate` | sufficiency proved [K CA:352 + W]; impossible on product-only preparations [X S4.pact] | restatement |
| reversibility on the pair state space | N, N⁻¹ map states to states | [N] | ⇒ `hgate` | immediate | restatement |
| two-sided positivity relative to maxCone | `NativeGate.posFwd/posInv` | [K] | ⇒ `hgate` | `M_max` ✗, `M_D13` ✗ | route refuted |
| K1: `IsNot`, `NativeGate`, `CtrlGate`, `GateRel`, `Entangling`, common NOT | as landed | [K]/[A] | ⇒ `hgate`; ⇒ CONS | `M_max` ✗, `M_D13` ✗; `g_D`, `g_pre` preserve no admissible cone | route refuted |
| EFF-1 / K1-BRIDGE-1 | `NativeGateOf`, `EntanglingOf`, cone = maxCone | [K] | ⇒ `hgate` | as K1 | route refuted |
| COMP-1 interface | the slice is a `Composite` body | [K] | ⇒ `hgate` | landed min/max composites with `cnot` ✗; `M_max` ✗ | route refuted |
| OPACT-1 as landed | datum with inverse preserves the completed body | [K] | ⇒ `hgate` | vacuous at L (no pair system) | route refuted as stated |
| `H` / FCC | the four-copy core | [D] | ⇒ `hgate` | `M_max` ✗, `M_SEP` ✗ | route refuted |
| self-duality | `dualW K = K` | [N] | ⇒ `hgate` | `M_D13` ✗, `TWIN` ✗ | route refuted |
| K2 as recorded | ROADMAP K2 obligations | [A] | ⇒ `hgate` | does not name the gate's action | not a source as recorded |
| product-level idle extension | local maps act on products factorwise | [N] | ⇒ `hgate` | an identity; `M_max` ✗, `M_D13` ✗ | route refuted |
| gate-factor idle extension | K invariant under each factor of N | forbidden | ⇒ `hgate` (trivially) | contradicts K2-GUARD-1 for reflection factors | forbidden |
| commutant extension | K invariant under `rot3` (control), `rotX` (target) | IE1 fragment | ⇒ (L) from (BS) | — | circular |
| PRP | `N^{±1}` (products) `⊆ K` | [N] | ⇒ `hgate`; sufficiency | `M_max` ✗; theorem countermodels `M_maxD`, `M_maxT` | refuted |
| TBP | `N^{±1} K ⊆ maxCone` | [N] | ⇒ `hgate`; sufficiency | `M_SEP` ✗; `M_SEPD` | refuted |
| SECTst (= P-PROD) | `N` (products) `⊆ K` | [N] | sufficiency | separation (holds `M_max`, fails `M_D`); `M_maxD`, `M_maxT` | refuted |
| BS | `bellOf A B ∈ K` | [N] | sufficiency | separation; `M_maxD`, `M_maxT` | refuted |
| BD | `bellOf A B ∈ dualW K` | [N] | sufficiency | `M_SEPD` | refuted |
| SECTef | `N⁻¹ K ⊆ maxCone` | [N] | sufficiency | `M_SEPD` | refuted |
| SECT′ | `N⁻¹` (products) `⊆ K`, `N K ⊆ maxCone` | [N] | sufficiency | `M_D` | refuted |
| CONS | (L) ∧ (BS) ∧ (BD) | [N] | sufficiency; certified ⇒ CONS | sufficiency proved [W over D]; `M_max` ✗ (BD), `M_D13` ✗ (BS); strictly weaker than `hgate` (`M_pre`, `M_DD`) | INDEPENDENT; the consumed clause, no independent motivation found |
| OQ1 | SECTst ∧ BD | [N] | same | same | INDEPENDENT |
| SECT ⟺ GT-COMP | SECTst ∧ SECTef | [N] | same | same | INDEPENDENT; GT-COMP is SECT restated |
| PREC | `hgate` after a local orthogonal pre-correction | [N] | same | same | INDEPENDENT; `hgate` with the pre-locals freed |

## 4. Cross-thread notes

- **A (PAIR-COMP).** (i) A pair system whose preparations are product states only admits no operation datum for
  `cnot` (B2.3, [X S4.pact]): a pair completion that carries the native gate must contain gate images of products.
  (ii) The cone `SEP + cnot SEP` (the cone of the landed `cnotOrbit` [K K2G:182]) is `cnot`-invariant, admissible and
  closed (both summands are closed cones over compact bases at unit entry 1, so `C₁ ∩ −C₂ = {0}`, and a sum of closed
  convex cones with that property is closed [L, unverified: Rockafellar, Convex Analysis, Cor. 9.1.3]) [W], and not IE1
  (landed M_cl.9W, M_cl.11W); by the contrapositive of the [D] theorem it is not FCC. (iii) `hcl` cannot be dropped with
  any weakening: the landed `M_cl` satisfies `hgate` and the inverse-gate clause (M_cl.3), hence PREC, SECT, OQ1 and
  CONS without using `hcl` [W], and violates C.
- **C (FOUR-COMP).** On `actT reflY`-invariant cones (maxCone, SEP) H cannot see orientation: all 16 gate patterns
  satisfy `H0` and split 8/8 on `EvenCycle` [X O5]. The chart transports F.t3 (`FCC(Q3, twin, Q3, twin) ⟺ FCC` uniform
  `Q3`) and F.t12 (uniform `twin` ⟺ uniform `Q3`) are exact identities [X b1_models S5].
- **D (NCLASS-ADM).** `cnot`, `g_D`, `g_pre`, `g_Tw` satisfy every landed native-gate hypothesis and are N-CLASS [X]; two
  of them preserve no admissible cone. On aligned families `hgate` ⟺ `orient(A', B') = orient(A, B)` (B1.4): `hgate`
  constrains the pre-locals, which C does not read. `b2_census` lists every landed Prop over the pair carrier (8) and
  every pair-touching module (16), reusable for "smallest additional assumption".
- **Coordinator (DEPGRAPH §7.6 (A2), lead only [F]).** Is a gate premise needed for IE1? Family `K01 = K23 = K_h :=
  maxCone ∩ {ipW h · ≥ 0}`, `h = diag(1, t, t, 0)`, `K02 = K13 = maxCone`, cnot gates: `K_h` is not IE1 for `t > 1/2`
  [W]; sampled positivity of `h(Q3 ∪ twin)h` holds to `t ≈ 0.707` [F `explore/e1_ie1_foil.py`]. Certifying it needs
  decomposability of qubit positive maps and the Peres–Horodecki criterion [L, unverified] or a direct proof. No claim.
- **Landed context, no formal map claimed.** `OrientationSelection` / `OrientationClosure` record that unoriented
  operational data select QM only up to the transpose. Lemma O is an orientation-blindness statement of a similar kind
  at the pair-table level (`actT reflY` is a one-copy partial transpose [X Dpt]); no map between the two is claimed.

## 5. What is not claimed

- INDEPENDENT means independent of the premises certified at L as stated — the thirteen items of B2.6, with the census
  complete relative to its text-scan rules R1–R2 (its dispositions are written judgements). It is not independence of
  every extension of the framework: a future pair system with an operation datum (P-ACT2), a substratum-to-pair bridge,
  or a K2 that fixes the composite cone or the gate's action could imply `hgate`; each would be a restatement or a new
  principle to assess.
- Sufficiency of CONS, OQ1, SECT, PREC is a written argument over design-run lemmas. `B1_UNBUILT.lean` was never
  compiled; tactic details (the `simp` sets of `locEquiv`, the `rw` chains) may need adjustment when built. The audited
  theorem is itself design-run [D], and every sufficiency statement here inherits that standing.
- PREC ⇒ SECT is written only (not in the Lean file). Whether PREC, SECT, OQ1, CONS are strictly ordered under `H0` is
  not measured: no model in the matrix separates them.
- No necessity: no clause is claimed necessary (`M_max`, `TWIN` show none is).
- Lemma O covers σ-invariant clauses. Whether an independently motivated, non-σ-invariant sufficient clause holds in
  `M_max` is not settled: such a clause must read the post-local orientation (B1.3).
- Exact computations are stated for their instances (one cell, one model). Universal statements rest on [W] liftings
  (Lemma O; the symbolic identities) or on exhaustion (the 16 patterns of O5).
- The (A2) lead is floating point only.
- Nothing is claimed about the matrix-carrier programme's premises beyond their not touching the pair carrier at L.

## 6. Evidence log

All scripts run as `python3 -I -B <script> ..` from `pt/B/` (`b1_steps`, `b1_implicit` also take `B1_UNBUILT.lean`;
`explore/e1_ie1_foil.py` takes no argument).
Decision rules are in each header, written before run 1. Timings went to `.time` files, never to stdout.

| file | sha256 (script) | runs | stdout sha256 | replay |
|---|---|---|---|---|
| `b1_consumed.py` (33 checks) | `a6843f5ecd32f81924ba8af5428b9a767977152d8740dc786eb6da97ccf366c8` | 1 (pass) | `7b76246bb1e44491481ec243ab76980780a066393a3b9ead1abab23932e809c1` | identical to run 1 |
| `b1_models.py` (53 checks) | `dd43e3061d0f229d9d319de31b1f5fa5d5e7c29392f516fdbc04cb850c120095` | 1 (pass) | `ca0fc31d6e24a150a2c00871b6f3cc367df1d6663052800febd9ce59a58b7e01` | identical to run 1 |
| `b1_steps.py` (23 checks) | `a2a79f4e909e65d5dfdee26e5d2d115a7e9ebcd5ca384ed6786495d6f6d071a4` | 2: run 1 FAILED (D.cc countercontrol logic, NOTES N7), stdout `67c5c0aa8e1c448ade343eb16f940462de77c5fa53878e2570aa1f5a3f82172a`, exit 1; run 2 pass | `d13c474db695e83154b6fde1d36dcda949cbd2b7663c8dd80a8d230a7c98b004` | identical to run 2 |
| `b1_implicit.py` (7 checks) | `2b41541ea7c27320f74c3912f741f7098be5481aa19001142afc67a2df225968` | 1 (pass) | `f83862673a8e809807348a156d10e9029c82831bbd1327b7151cdf6ce449d271` | identical to run 1 |
| `b2_sources.py` (27 checks) | `156f4a24b1ddbcb8cdf043b051f119b7787bcfb0161054603bfe56914ade78f2` | 1 (pass) | `c4e6b5394c7aed170cafa3608ff5a5d244d37b4d528c9a7de8a77307027a0ff3` | identical to run 1 |
| `b2_census.py` (7 checks) | `7f45d4188ff7d3f195c53fbb22fb666aa5537cfd40d43514167dd3dd7ed794aa` | 2: run 1 invocation error (`/usr/bin/time` absent, script not executed, exit 127, empty stdout); run 2 pass | `32362f8380990fe23a1b1d137f007cc547749986b7930167e951aa0da828ce3b` | identical to run 2 |
| `explore/e1_ie1_foil.py` [F] | `ab02a93dcf4a695d80798d2e9a3d10349c66c735f122a1064a96e5c1058a3a42` | 1 | `093d68f4258a264efa931c946b87aa8133c03492fb5819e747d18ded037b5520` | identical to run 1 |
| landed `kt4_prem1_probe.py` (blob `5609d96a9886d5d8548c0322e084849e700ba72b`, file sha256 `c2fdcaafb45bd261abf4809b60a98b1dd3a1c55a84038d72eadecef97baeeec9`) | — | replay only | `1873134134102bccaa27a12dfb9afd9ea1a8297fcf5cfe74531adc4696471d8a` | 79 PASS, 0 FAIL, ends `kt4_prem1_probe: OK -- 79 checks`, as `result.md` records |
| `B1_UNBUILT.lean` (UNBUILT) | `200e5891c61975780142eb77fab2902330fb1d70742bf900aee1e59fcb16b13f` | — | — | checked by `b1_steps`, `b1_implicit` |

Every `.err` of a passing run and replay is `exit=0`; `b1_steps.run1.err` is `exit=1`, `b2_census.run1.err` is
`exit=127`. Pre-run edits are recorded in NOTES (N1, N5, N7, N10). Other files: `NOTES.md`, `.start_marker`, the
`.time` files, `landed_replay/`.

## 7. Integrity

- Start (`.start_marker`, 2026-10-10T04:33:37Z): `sha256sum -c --quiet inputs.manifest.sha256` exit 0; `git -C base
  rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C base status --porcelain` empty;
  `PROTOCOL.md` sha256 `239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23`.
- Amendments read and verified against their `.sha256` files: amendment 1
  `b41aa0e735b3ca0bf7fb08c3629dd9a18c6d979039c6ba005fd707330831cf83`, amendment 2
  `2a2f78f374e5dfb541854677060481a0e40bda636c1649a850a132f3b27c530a`.
- End (2026-10-10T05:54:57Z, before this file was written, and again at 2026-10-10T05:59:15Z, after): manifest exit 0;
  HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`; status empty; `PROTOCOL.md` and both amendments OK. `pt/B/` holds
  54 files (the scripts of §6 with their outputs, timings and replays, `B1_UNBUILT.lean`, `NOTES.md`, this file,
  `.start_marker`), all written by this thread.
- Writes: only inside `pt/B/`. Git: read-only commands only. No PR, CI, push or network action; no agent spawned.
- Anomalies: none. Every file in `pt/B/` was written by this thread; no `INTEGRITY.md` or `quarantine/` was needed.
