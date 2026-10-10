# Coordinator's audit of EQ4-SOURCE (research only)

Thread result: `scratchpad/eq5/SOURCE/RESULT.md`. Protocol: `scratchpad/eq5/PROTOCOL.md` (EQ4-SOURCE).

## Verdict

The result **stands as written**. The four replays are byte-identical. An independent exact audit (own code) confirms
every load-bearing exact claim. Integrity is clean.

There is one scope note (§3, item 1), recorded as a precision rather than an error, and one route difference with
EQ4-F (§3, item 4).

## 1. Replays

Run from a separate directory (`eqreview/replaySOURCE/`) on copies of the scripts, with the recorded arguments:

| script | script sha (matches record) | output | checks / verdict |
|---|---|---|---|
| `s0_census.py` | `a1c366ce4e47a0da` | identical | 12/12, `S0-CENSUS-NO-MULTICOPY-STRUCTURE` |
| `s1_kt4_models.py` | `3c7b3c993b7d5527` | identical | 35/35, `S1-KT4-WITHOUT-TOK-MODELS-EXACT` |
| `s2_pair_premises.py` | `fcf2c56b103ed2cc` | identical | 11/11, `S2-PAIR-PREMISE-CORES-EXACT` |
| `e1_stmc_twist.py` (lead) | `8f7ed449ccbbd674` | identical | 3 controls, `LEAD STMC-TWIST-EXCLUDED` |

## 2. Independent exact audit

`audit_source.py`:
- sha `95b0f2477977b104`; output `b3d5ff9382e6d1f6`.
- 4/4, `SOURCE-AUDIT-EXACT`, on the first run; replay identical; `.err` empty.
- The decision rule was fixed before the run. The code imports nothing from the thread and parses `cnot` from the base.

| id | what was checked | result |
|---|---|---|
| K0 | `sgn`, `pc`, `pt` transcription; `chainW` parsed from K2Guard equals `cnot idW` computed independently | pass |
| AS | anchor sum, on 17×17 coordinate arrays with random rational data (4 draws). Checked: the evaluation laws; the cross values `e(x0)·f(y0)` and `E(L0)·F(L0′)`; unit pairing 1 at both kinds of product. `tok` fails at three indices (−31/8, −35/4, −1). Control: a zero anchor gives unit pairing 0. | pass |
| MR | M_ρ. Checked: Q3 ≠ twin (`pauliW phiW = v vᴴ/2`; singlet value of `pauliW idW` is −1); the witnesses X = Y = phiW ∈ Q3, E = phiW/4 ∈ Q3* and F = dg(1,−1,1,−1)/4, with `actT reflY F = dg(1,−1,−1,−1)/4` PSD, so F ∈ twin*; the pairing identity at the witnesses; family (i) value **−1/8**; ρ an involution and PB's evaluation law; `tok` difference 2 at index (0,0,0,2), the same magnitude as the thread's −2 | pass |
| G | landed gate countermodels: `idW` nonnegative on 200 random Lorentz pairs; `chainW = cnot idW` takes **−1/2** at sharp b = −eₓ, c = −e_z; F(ω) = ω₀₀ − ω₁₁ + ω₂₂ − ω₃₃ satisfies `F(prodState x y) = ½|x − Dy|² + ½(1 − |x|²) + ½(1 − |y|²)` symbolically, and `F(cnot(prodState xplus z3)) = −2` | pass |

Written assembly checked by hand:
- **Anchor sum.** On V = C × C, the bi-affinity, `prodEff_apply`, `prodEff_effect` (values at the other grouping's
  products are e(x0)·f(y0) ∈ [0, 1], extended over the convex hull), `prodEff_unit`, `convex` and `one_body` hold for
  every quadruple of nonempty pair bodies. Confirmed.
- **M_ρ.**
  - `PB.prodState L L′ = pState L (ρL′)` lies in PA's minimal body, because ρ maps `pairBody twin` onto `pairBody Q3`.
  - `PB.prodEff E F = pEff E (F∘ρ)` takes values `E(x)·F(ρy) ∈ [0, 1]` on PA's products.
  - Unit: `unitEff ∘ ρ = unitEff`.
  - PB's product effects are PA's, through `F ↦ F∘ρ`, so local tomography transfers.
  - The pair premises hold for (Q3, Q3, Q3, twin) with (cnot, cnot, cnot, cnotTw).

  Confirmed.

## 3. Wording and scope (P/A/C, §A.34)

1. **Scope of M_ρ and M_tw.**
   - They refute the **parity** part of `kt4_forward`'s conclusion only. Their cones are classified (each is Q3 or the
     twin) and IE₁, so the conclusion fails through `EvenCycle τ`.
   - Refutations of the classification and IE₁ parts without `tok` come from the anchor sum with C_H:
     - C_H violates KT(4) at −1/200 [X EQ3 p6 H3];
     - C_H is not IE₁, because `phiW ∈ C_H` while `actT R_H phiW ∉ C_H` [X EQ4-F precheck_core F2 + W].

   The thread's §0 says "the conclusion fails", which is accurate. This precision feeds EQ4-F's per-conclusion foil
   table.
2. **"`tok` is not necessary relative to the other premises"** (M_id, M_T). These are models of P_rest ∧ C ∧ ¬tok. That
   is the correct form of a non-necessity claim under the P/A/C rule. No necessity claim is made anywhere. **Correct.**
3. **Equivalences.** `FourCopyCoherent ⟺ ∃ KT4` and `TokenCoherent ⟺ TokProdState` each name a separate witness per
   direction, and both are marked [W] with exact endpoints. This satisfies §A.34.
   - The (⇐) of the first is Lemma B1. Its unbuilt Lean draft is `eq5/F/drafts/FourCopyBridge.lean`.
4. **Route difference with EQ4-F.**
   - Row 1 lists `chart_rule` among `hcls`'s consumers, following FORMAL's skeleton.
   - Under EQ4-F's IE₁-first route (`eq5/F/DEPGRAPH.md`), `chart_rule` is not on the headline. Orientation enters
     through the witness reduction (N8) instead.
   - This changes no SUPPLIES class.
5. **Correction to EQ4-F's FORMAL §2, accepted.**
   - H-gate, H-inv and H-NCLASS were labelled "transported". At the base no stated premise implies body-level gate
     preservation: the landed `ball3MaxComposite` and `ball3MinComposite` with `cnot` are exact countermodels.
   - N-CLASS is a derivation route (EQ2-B, unbuilt) from K1-level premises, which are themselves unsourced.
   - EQ4-F's minimal-assumption table records each hypothesis's SUPPLIES class from this ledger.

## 4. Integrity

- Base manifest (1317 entries): silent, exit 0, checked from the base directory. No base file is newer than the
  manifest.
- Inputs manifest (6 entries): OK.
- Repository: HEAD `f0d37906`, working tree clean, no reflog movement.
- No file newer than the thread's start marker exists outside `eq5/SOURCE/`, `eq5/SIX/`, `eq5/F/` and `eqreview/` (the
  concurrent thread's, the coordinator's and this audit's directories).

Consistency-axis work only; bands unchanged.
