# Thread C — FOUR-COMP: running notes (research only; nothing adopted, frozen or governed)

Directory: `pt/C/` (the only place this thread writes). Protocol: `pt/PROTOCOL.md`, sha256
`239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23` (verified at start). Base: certified `main` at
L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, read-only at `pt/base/`. No Lean toolchain: any Lean text is UNBUILT.
No git write, no CI, no GitHub access, no agents.

## N0. Start (integrity)

`.start_marker` (2026-10-10T04:33:48Z), written before any other file of this thread:
- `cd pt && sha256sum -c --quiet inputs.manifest.sha256`: silent, exit 0 (41 entries).
- `git -C pt/base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`.
- `git -C pt/base status --porcelain`: empty.
- `pt/C/` was empty before the marker.

## N1. Reading log

- Protocol, whole file; Thread C section and shared rules.
- `base/.../round-kt4-prem-1-premise-audit/result.md`, whole (Q1-MAP, carrier and `H ⟺ FCC`, Q2, Q3 source map, the
  four open questions; open question 2 is this thread's target).
- Design modules (inputs/fourcopy): `FourCopyDefs.lean` (FourCopyCoherent famI/famII, ipW, dualW, PairAdm,
  transposeW, cnotTw, gateOf, EvenCycle4), `FourCopyCore.lean` (fourVal, PairLinked, flatW, pairBody, tabCoord,
  tabEff, TokenCoherent, KT4, KT4LT, KT4Core), `FourCopyBridge.lean` (KT4.toCore, core_valI/II, Lemma B1
  `fourCopyCoherent_of_kt4Core`), `FourCopyHeadline.lean` (`kt4_forward_ie1` takes `H : KT4Core`), and
  `FourCopyPackage.lean:150-170` (`chartR`, open `fourCopyCoherent_chart`).
- Landed probe `base/verification/lean/kt4_prem1_probe.py`, whole (blob 5609d96a… matches result.md); landed
  `CompositeInterface.lean` §A–§B (ProductData, PreComposite, Composite; the combo laws are affine for every
  `a + b = 1` and every chart point, CI:212–215).
- Ledgers: EQ5-SOURCE result/notes/audit, EQ5-PREM result/notes/audit, EQ3-P result and EQ3-AUDIT, EQ2-SYNTHESIS,
  EQ4-P result, EQ5-SIX result, EQ4-SIX-AUDIT, DEPGRAPH, ASSUMPTIONS, DEPENDENCY-MAP; K2-LEDGER T6 (definition of C_H);
  premise probes' outputs.

Leads taken from the ledgers, to be re-verified where used:
- KT4 minus tok is vacuous (anchor sum, every quadruple); M_ρ, M_tw, M_θ: KT4⁻ with local tomography of both
  groupings on (Q3, Q3, Q3, twin), token-3 twist; TPS ⟺ tok relative to LT(PA) (SOURCE §3.7); EQ5-PREM Theorem A:
  IP₁ᴮᴬ ∧ LT ∧ one body ∧ PairAdm ⇒ tok (TokenCoherent on the whole body); purity lemma.
- EQ3-AUDIT §4: relative to the pair premises, KT(4) ⟺ IE₁ ∧ even 4-cycles; EQ2-SYNTHESIS §5: W2 (is every
  admissible cnot-invariant K with K = T(K*) equal to Q3 or the twin?) is open.

Observation that fixes the decisive branch (to be pressure-tested): the audited theorem consumes `H : KT4Core`, whose
token clauses `tokA`, `tokB` are stated only at the product states of each grouping (FourCopyCore.lean:111–114), not on
the whole body as `KT4.tok : TokenCoherent` is. The prior routes to the token clauses (EQ5-PREM Theorem A; SOURCE §3.7)
target `TokenCoherent` and need local tomography for that. ASSUMPTIONS.md §4.2 carries this over to `KT4Core`. Whether
local tomography is needed for the clauses the headline actually reads is the first question.

## N2. Productivity test, decision rules, node plan (fixed before any script is written)

**Productivity test (protocol, fixed):** a finding is a gem iff it is (1) an exact certificate (derivation with every
step checked, or an exact countermodel) at a stated instance, (2) an exact obstruction for a stated class of routes, or
(3) an exposed hidden assumption. Otherwise record-only. Output classes NEW / POSITIVE / ELABORATING / CONFIRMING /
BORDERLINE. Fixed point: 3–4 consecutive passes with no NEW finding, or the question answered.

**Skepticism rule:** a branch favourable to the framework (a derivation of FCC or of the token clauses) is accepted only
after (a) every relevant countermodel is evaluated on the candidate, (b) each premise of the derivation has an exact
model in which it is dropped and the conclusion fails, (c) the route is checked for IE₁, IE₂, the quantum cone as a
premise, the region tower, (o)-steps and operation-level idle extension, and (d) a model shows what the premises do
not force (local tomography, body-level token coherence, a quantum four-token body).

**Nodes (depth-first; the decisive branch first):**
- A (decisive; protocol C1/C4). "Consistent composition" as regrouping invariance on a four-token carrier: does
  {each grouping a COMP-1 pre-composite of the pair bodies, one body, regrouping invariance of token-product
  preparation (TPS)} give KT4Core — hence FCC — without local tomography?
  A1 field map to KT4Core; A2 TPS ⇒ tokA ∧ tokB (spanning + combo laws); A3 posBA, posAB; A4 satisfiability;
  A5 each premise cannot be dropped; A6 what the premises do not force; A7 weakest first-order form (IP₁) and
  one-directional insufficiency; A8 independence assessment.
- B (protocol C3). The mixed assignment: both families; the {Q3, twin}⁴ characterization; which principles exclude
  it; sub-plaquette (tree) obstruction; uniformity.
- C (protocol C2). The candidate table against M_tok, M_tokC, anchor sum, M_ρ/M_tw/M_θ, the transposed-factor model,
  PN where relevant, and the new models.
- D (protocol C1). Field-by-field relation table (record).

**Script decision rules** are stated in each script header before its first run (rules, not expected numbers).

## N3. Amendment 1 (received during the run; binding)

`pt/PROTOCOL-AMENDMENT-1.md`, sha256 `b41aa0e735b3ca0bf7fb08c3629dd9a18c6d979039c6ba005fd707330831cf83` (verified; PROTOCOL.md
unchanged at `239dc123…`). For thread C: excluding M_tok and the other countermodels is necessary-condition evidence
only; a principle derives FCC only with a derivation of FCC and of the token clauses from it, with exact ingredients.
"0. Answer" must distinguish **sufficiency proved** from **survives the countermodels** for every implication. Read at
the point where c1 and c2 had run; it changes no script. It fixes how node A is reported: the route must be a
step-by-step derivation of `KT4Core` (token clauses included) and of FCC, and every other candidate is classed either
"sufficiency proved", "refuted by an exact model", or "survives the tested models; sufficiency not established".

## N4. Scripts and runs (all `python3 -I -B`, from `pt/C/`)

- `c0`: replay of the landed probe `base/verification/lean/kt4_prem1_probe.py` (read-only; no file written outside
  `pt/C/`; base status still empty afterwards): 79 PASS, 0 FAIL, `kt4_prem1_probe: OK -- 79 checks`, as landed.
- `c1_cone_level.py <OIB> <inputs/fourcopy>`: pre-run edit (before run 1): `coords` used `sp.nsimplify`; replaced by
  plain exact expansion. Run 1: 40/40, `VERDICT C1-CONE-LEVEL-EXACT`.
- `c2_carrier_models.py <OIB> <inputs/fourcopy>`: pre-run edit (before run 1): the label of G4c said "10 symmetric
  token products"; the code uses the 9 ordered products of {e_x, e_y, e_z}; label corrected. Run 1: 36/36,
  `VERDICT C2-CARRIER-MODELS-EXACT`.
- `c3_route_ingredients.py <OIB> <inputs/fourcopy>`: pre-run edits (before run 1): U1's identity rewritten as a plain
  polynomial identity (a square-root substitution was replaced); an unneeded assignment expression removed; an
  explicit bi-affinity degree check added to U4. Run 1: 17/17, `VERDICT C3-ROUTE-INGREDIENTS-EXACT`.
- `c4_supplements.py <inputs/fourcopy>`: pre-run edit (before run 1): the U.W note narrowed to the two modules the
  source checks read. Run 1: 7/7, `VERDICT C4-SUPPLEMENTS-EXACT`.
- `c0_census_L.out`: a read-only command log (git rev-parse, git log, git diff --stat, grep) at the base, saved as
  evidence that no Lean file changed between `bcbc516f` (the audited SOURCE census) and L, and that nothing with three
  or more tokens is declared at L. Not a script.
- No failed runs; no `.runN.*` files exist.

## N5. Amendment 2 (received before RESULT.md was written; binding)

`pt/PROTOCOL-AMENDMENT-2.md`, sha256 `2a2f78f374e5dfb541854677060481a0e40bda636c1649a850a132f3b27c530a` (verified). Each
target (FCC, tokA, tokB) carries exactly one label: DERIVED / CONDITIONAL / INDEPENDENT / UNRESOLVED; a model of one
route's premises is "route refuted", never INDEPENDENT; a restatement does not make a target CONDITIONAL; [K]/[D],
[W] and [X] kept apart, [X] stated for the instance it checks. Applied in RESULT.md; it changes no script.

## N6. The depth-first walk (verdicts per node)

Node A (decisive; protocol C1/C4):
- A1 field map. KT4.toCore (FourCopyBridge:221–234) reads one_body and tok at product states only; KT4Core's tokA/tokB
  are quantified over pair-body product states (FourCopyCore:111–114), TokenCoherent over the whole body (:64–68)
  [X c2 S0]. The headline consumes KT4Core [X c1 S0.head]. ELABORATING (exposes the gap between the prior target
  `tok` and the audited H).
- A2 TPS ⇒ tokA ∧ tokB with no body, no positivity, no LT: bi-affinity (landed combo laws) + the token products span
  H00 [X c2 G4, c3 E1, E2 + W]. In every model with TPS the clauses hold [X c2 M.route]. **NEW** (prior routes needed
  LT because they targeted body-level `tok`).
- A3 posBA/posAB from one body and each grouping's own prodEff_effect: KT4.toCore's argument [D source; X c2 S0.toCore].
  CONFIRMING.
- A4 satisfiability and converse: MSIG on uniform Q3 [X c2]; FCC ⇒ ∃ carrier with N0 ∧ N1 ∧ TPS [X c3 V1, V2 + W].
  ELABORATING (SOURCE §3.6 with TPS in place of tok).
- A5 skepticism, each premise cannot be dropped: one body (SEPH, cross value −1/8 [X c2 X1]); TPS (ANC [X c2]); the full
  COMP-1 effect quantifier (restricted version holds on M_tok's cones [X c2 X3 + W]); every proper sub-conjunction of
  {N0, N1, N2} is satisfiable on every quadruple. **NEW** (SEPH on the mixed assignment; the sub-conjunction statement).
- A6 what the premises do not force: PAD (TPS, one body, KT4Core, FCC; no LT of either grouping, no TokenCoherent, no
  STMC) [X c2 L1, L2]; the four-token body need not be quantum (MSIG with the hull body; PN₄) [W]. **NEW** (PAD).
- A7 weakest form: IP₁ in both directions suffices without LT (purity lemma, core [X c3 U1], countercontrols U2, U3;
  CORR shows the positivity from one body is load-bearing [X c3 U5, U6]); one direction does not suffice even with all
  pair premises (HBA on (Q3, Q3, K_c, K_c), HAB mirror) [X c2 M.HBA, M.HAB; c1 K7, K8; c4 N1–N3]. **NEW** (one-direction
  countermodels with all pair premises and ¬C; LT-free IP₁ route).
- A8 independence: N2 does not mention cones, effects or positivity; independently motivated (regrouping invariance);
  existentially equivalent to FCC with N0 ∧ N1 under hadm. Verdict: CONDITIONAL, with the existential equivalence and
  the earlier "relabelling" classification of TPS (EQ5-PREM, relative to LT and the body-level target) recorded.
Node B (protocol C3):
- B1 both families fail on (Q3, Q3, Q3, twin) at −1/8 [X c1 W2, W3]. famII failure **NEW** (only famI was recorded).
- B2 {Q3, twin}⁴: FCC exactly on coboundary patterns [X c1 T1–T3 + W]. CONFIRMING (EQ3 p2 Z).
- B3 tree obstruction: no conjunction of chart-invariant conditions on ≤ 3 pair cones (gates and locals included)
  excludes the mixed assignment [X c1 R1, R2 + W]. **NEW** as a class obstruction.
- B4 uniformity, one pair type across bipartitions, U*: exclude it, refuted as routes by uniform K_c (all pair premises;
  FCC −1 [X c1 K7]; IE₁ fails [X c4 N1–N3]); not necessary: (Q3, Q3, twin, twin). ELABORATING (C_H known; K_c simpler,
  exact).
- B5 C3's question answered: a consistency (cocycle) condition at the cone level on the classified family; at the
  carrier level token identity across groupings; one direction of first-order token identity already excludes it.
Node C (protocol C2): entangled core [X c1 E1, E2 + W] ELABORATING; candidate table assembled; link instances of FCC
are all the design proof consumes [X c4 U1, U2 + W] ELABORATING; relabelling covariance refuted (anchor sum on uniform
K_c) [X c3 L1 + W] ELABORATING.
Node D (protocol C1): field-by-field table, record only.

## N7. Passes and fixed point

- Pass 1: nodes A–D as above; NEW findings in A2, A5, A6, A7, B1, B3.
- Pass 2 (skeptical re-check of the route, after amendment 1): step-by-step re-derivation of tokA/tokB, posBA/posAB, B1;
  one body weakenable to cross membership; TPS needed only on S⁴; tokA needs neither one body nor hadm. ELABORATING.
- Pass 3 (hidden assumptions in the setting): H0 at four tokens (factor bodies are the standalone pair bodies) is in
  the typing of N0; two-copy local tomography is in W 3 (K2); the shared per-token charts (DEPGRAPH §7.4) are what TPS
  makes operational; the flattening convention is immaterial (finProdFinEquiv (a, b) = b + 4a, Mathlib
  Logic/Equiv/Fin/Basic.lean:334). CONFIRMING / ELABORATING.
- Pass 4 (missed candidates): associativity without commutativity cannot relate 01|23 to 02|13 (the regrouping
  exchanges tokens 1 and 2); sequential (process) composition closure is FCC restated (I1, I2); STMC ⇒ IP₁ both ways;
  three-token pair⊗token composites are satisfiable on every admissible quadruple (in B3's class); the design proof
  reads FCC only at link instances (c4). ELABORATING / CONFIRMING.
- Three consecutive passes (2–4) without a NEW finding: fixed point reached.

## N8. Replays

All five (`c0` landed-probe replay, `c1`–`c4`) replayed with the same arguments into `.replay.out/.replay.err`;
`cmp` identical for every `.out` and `.err`; every `.err` is `exit=0` (sha256 `19eaf438…`). Base status empty after
every run (no `__pycache__`: all runs use `-B`).

## N9. Final read of RESULT.md (before the end checks)

Edits to RESULT.md after its first writing, all to this thread's own text; no script, output or verdict changed:
- header: the UNBUILT Lean text is in §1.A7, not §1.A5 (a stale node reference); §1.A1: the "not needed / not forced"
  reference now points to A2 and A4 (PAD), not A6;
- 0. Answer, FCC: "no cone premise" narrowed to "no cone premise beyond hadm"; the assessment sentence now covers N0
  and N1 as well as N2 and states that every proper sub-conjunction holds on every quadruple of nonempty pair bodies
  (A4);
- 0. Answer, tokA: "no hadm" added (pass 2);
- 0. Answer, last bullets: the M_tok-excluding candidates are headed "Exclude M_tok, without sufficiency" (they are
  refuted as routes, so "survive the countermodels" did not fit them), with evidence tags; link-FCC is the one
  candidate that survives every tested model, in its own bullet, with its sufficiency for FCC resting on [W + L].

Node numbering: RESULT §1.A regroups this log's Node A. RESULT A1 = N6 A1 with the exposed assumption that N6 A2's
NEW grading names (prior routes needed LT because they targeted the body-level clause); RESULT A2 = N6 A2 + A3;
RESULT A3 = N6 A4; RESULT A4 = N6 A5 + A6; RESULT A5 = N6 A7; RESULT A6 = N6 A8; RESULT A7 = the UNBUILT Lean text.
Node B and C numbering is unchanged. Pass 1's NEW list in RESULT §1.E (A1, A2, A4, A5, B1, B3) is N7's list
(A2, A5, A6, A7, B1, B3) in RESULT numbering.

## N10. End (integrity)

2026-10-10T05:41:05Z: inputs manifest silent (exit 0); base HEAD 9f9f8257a980a1819fbbc1dc0019917cf8678626; base status
empty; PROTOCOL.md and both amendments hash-verified; no `__pycache__`/`.pyc` under base; `pt/C/` holds only this
thread's 28 files, no subdirectory; §6 hashes recomputed and matched; replays byte-identical. Recorded in RESULT §7.
No integrity event. RESULT.md final sha256: `1fe5af4c7e0c4dd50996b202ce32dc4ec84d9c135afe3e772391eed6ad796906`.
