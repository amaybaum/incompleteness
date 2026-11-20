# R1-L8 Stage 1(ii) — preregistration: global canonical typicality replaced by a declared local-equilibrium condition

**Status.** Writer's paper-only preregistration, committed and pushed before any consumer is
classified. The classification is `AUDIT.md` in this directory, in a later commit. Existing
evidence only: no new measure construction, no replacement probability law, no new physical
assumption beyond the declared condition under study, no manuscript, Lean or registry edit. The
local-equilibrium condition studied here is a declared hypothesis; nothing in this unit derives it.
A1 (Main posit ledger item (ii)) remains open and unadopted. Independent non-author review is
required before any use of the audit.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7044998279](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7044998279),
2026-11-20T16:37:21Z, "Owner decision record: research emphasis and next units", item 1. Quoted:
"**R1-L8 Stage 1(ii)** (paper-only, existing evidence only). Replace global canonical typicality
(M19.a) with a declared local-equilibrium condition, and determine: exactly what can be retained;
what still needs physical sourcing; which results no longer follow. Narrowing to local equilibrium
is not deriving equilibrium. The unit must not present the replacement condition as derived. No new
measure constructions and no manuscript edits."

**Goal link (§A.47), from the authorization.** "Stage 1(ii) bears on removing A1 (the R1/R5
residue)." This unit decides, consumer by consumer, which of Main §4.6's equilibrium-phase
conclusions survive when the finite-dimensional typicality step is replaced by a declared local
condition, and which need that step (or a lemma L8) to stand. It does not decide whether the
declared condition is physically true.

**Source pin.** `main` at `800cfec6655aa5e9efaf39d6c7823bf2f40795e2`. `M:n`, `Sub:n`, `Str:n`,
`Comp:n`, `GR:n`, `SM:n` are line `n` of `papers/Main.md`, `Substratum.md`, `Structure.md`,
`Complexity.md`, `GR.md`, `SM.md`; `chNN:n` and `FULL:n` are lines of the `book/` chapter files and
`book/The-Incompleteness-of-Observation-FULL.md`, all at the pin.

**Reused records** (cited with their own line numbers; their investigations are not repeated):
STAGE0 = `verification/audits/foundations/r1-l8-stage0-20261120/AUDIT.md` (rows M19.a, M19.b at
:129–130; F3 at :79; note at :213); REMAINDER = `…/a1-remainder-20261119/REMAINDER.md` (M18–M20 at
:77–79, C10 at :95, R5 at :141, L8 at :163); A1-05 = `…/a1-05-p8-observer-selection/SOURCE-MATRIX.md`
(P8-M :13–28, P8-S :30–43); FCLASS = `…/a1-finiteness-classes-20261117/CLASSIFICATION.md` (rows 23–24);
R1-INF = `…/r1-inf-20261119/RESULT.md` (Lemmas 1–2 :83, :101; Prop. 3 :114; Prop. 6 :212; Prop. 9
:280; C4, C6 :351–353; §6 note :389); MAIN-ROOTS = `…/a1-main-roots-20261118/AUDIT.md` (:95);
LEDGER = `verification/coverage/LEDGER.json` (:1367, :1381, :1395).

## 1. The step being replaced

M:764: "For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies every
local subsystem is also in its local equilibrium." Together with M:758's "in the sense of canonical
typicality [31]", M:760's "canonical typicality [31] supplies the local-equilibrium *state*, not the
temporal mixing" and M:766's listing of "the canonical-typicality result [31]" among the theorem's
inputs, this is **the typicality step** for this unit. STAGE0 classes the global-to-local inference
(M19.a) as (c) c2: it needs the normalized unitarily invariant measure on a finite-dimensional energy
shell and a "typical" quantifier.

## 2. The declared conditions considered (fixed before tracing)

**Setting.** As A1-05 P8-M: a measurable update φ on a configuration space Ω of sites of any
cardinality; a reference probability μ, normalized and φ-invariant ((IL), M:766, assumed, not
adopted); P_Σ = E_μ[· | F_Σ] the projection onto the observables of a finite region Σ; K_Σ =
P_Σ U P_Σ; (EM) stated on the μ-centred observables of L²(μ). A declared family 𝓡 of finite regions
of bounded diameter (each of the form Σ_loc(V), or a candidate neighbourhood Σ_BB); D(𝓡) is their
union. ν denotes the **actual law** whose region marginals the conclusion concerns: the declared
preparation law, conditioned on the declared macro-data of the situation (for the anti-Boltzmann-brain
case, the stipulated neighbourhood law). TV is total-variation distance.

Three statements, from weakest to strongest. Each is a declared hypothesis with a declared tolerance
δ_LE ≥ 0; none is asserted, and none is derived here.

- **(LE-ref)** For every Σ ∈ 𝓡: ‖ν|_Σ − μ|_Σ‖_TV ≤ δ_LE. (The actual region law is close to the
  marginal of the reference law of (IL)/(EM), whatever that law is.)
- **(LE-eq)** (LE-ref), and in addition μ|_Σ = ω_Σ for every Σ ∈ 𝓡, where ω_Σ is the Σ-marginal of
  a law from a **declared equilibrium family 𝓔**, specified independently of the conclusion: a
  translation-invariant law that is a Gibbs/DLR state for a declared local interaction and is
  invariant under the update (the zero interaction, β = 0, included).
- **(LE-T)** (LE-eq) with 𝓔 the Gibbs/DLR states at a finite inverse temperature β = 1/(k_B T_local)
  > 0 for a declared real-valued conserved local energy of the update.

**Quantifier.** Region-wise, over the declared 𝓡 only. None of the three asserts anything about
regions outside D(𝓡), about a global macrostate of (S, φ), or about a typical set of any measure.

**Quantum-representation reading.** In the fixed-basis representation a law ν on configurations is a
diagonal density operator, and for diagonal operators trace distance equals TV, so each statement
has the same content when stated for reduced density operators of diagonal states. Non-diagonal
states are outside OI's microstate class and are not used.

**Which statement a consumer receives.** (LE-T) where the consumer's statement involves a temperature
or a thermal timescale (a "local thermal decorrelation time", T_local, (GT)); otherwise (LE-eq). (LE-ref)
is recorded for the control K3 and for the question of what "equilibrium" adds.

## 3. Consumers (fixed before tracing)

From STAGE0 M19.a–b, REMAINDER M18–M20 and C10, and a search of `papers/*.md`, `book/ch*.md` and
`FULL.md` at the pin for `canonical typicality`, `typicality`, `equilibrium phase`, `non-equilibrium
phase`, `equilibrium macrostate`, `local equilibrium`, `perpetual equilibrium`, `Boltzmann`, `past
hypothesis`, `observer-selection`, `§4.6`, `[31]`; and of `verification/lean*/` and the LEDGER for the
§4.6 results. A further consumer found during the trace is added to the table with a marker and the
reason it was missed.

| Id | Result | Site |
|---|---|---|
| T1 | Theorem bound τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε), with its proof's decay step | M:754–756, :760 |
| T2 | "In particular" clause: Σ_loc in local equilibrium "in the sense of canonical typicality" ⇒ τ_B bounded by the local thermal decorrelation time | M:758 |
| T3 | Proof sentence: canonical typicality supplies the state, (EM) the mixing | M:760 |
| T4 | Anti-Boltzmann-brain corollary, with its (GT) numerical illustration | M:762 |
| T5 | Observer-selection corollary, rate-condition part: the bounds do not compose; a sufficiently fast-mixing equilibrium supports no C2-slow observer | M:764 (to "remains open.") |
| T6 | Global-to-local step (§1) | M:764 |
| T7 | Equilibrium-phase conclusion: no bounded-diameter partition supports C2-slow; observers exist only in the non-equilibrium phase of (S, φ) | M:764 (remainder) |
| T8 | Scope: inputs include [31]; the canonical-typicality clause is a finite-representative statement | M:766 |
| T9 | §4.6 opening: the selection rule "on where in a finite bijective (S, φ) observers can exist" is a theorem conditional on (EM) and the rate condition | M:750 |
| T10 | Remark pointing to "the equilibrium phase" and the anti-BB corollary | M:171 |
| T11 | Arrow of time: τ_B bounded "on equilibrium microstates"; restriction to the non-equilibrium phase of (S, φ); past-hypothesis replacement; Boltzmann brains excluded | Sub:56 |
| T12 | Third projection: confinement to the non-equilibrium phase of (S, φ) | Sub:401 |
| T13 | Time-symmetric spectral-gap bound | Sub:409 |
| T14 | Regimes of silence: the equilibrium phase of (S, φ) is observer-free | Sub:542 |
| T15 | "Substrata in perpetual equilibrium cannot satisfy C2's slow-bath route" | Str:718 |
| T16 | Anthropic implication: non-equilibrium-phase features "required for C1–C4" | Str:734 |
| T17 | Boltzmann-brain problem dissolved; observers cannot exist in the equilibrium phase of (S, φ); past-hypothesis replacement | Comp:212 |
| T18 | Horizon-clock projection: observers restricted to the non-equilibrium phase of (S, φ) | ch02:192 = FULL:822 |
| T19 | Conditional Boltzmann-brain exclusion for bounded-diameter partitions | ch03:58 = FULL:919 |
| T20 | "The equilibrium phase of (S, φ)": bounded-diameter partitions fail C2-slow | ch04:178 = FULL:1282 |
| T21 | Lean and the coverage ledger | LEDGER :1367, :1381, :1395; `verification/lean*/` |

**Boundary (listed, not classified).** Separate uses of typicality that do not consume M:764's step:
GR Theorem A.8 (cycle typicality under H-scramble) and its book mirrors (ch07:126–151, ch18:140), and
the trace-out arrow of ch18:200 = FULL:4931. They are checked only for whether they cite the §4.6
step (control K5).

## 4. Decision rule (fixed before tracing)

For each consumer R, read its printed statement and proof at the pin and answer:

- **Q1.** Does R use the typicality step — the global-to-local inference of M:764, or [31] by
  citation or by "in the sense of canonical typicality"? A stipulated local equilibrium that R
  introduces itself (by definition or as an "if") is not a use.
- **Q2** (only if Q1 = yes). Does R's conclusion, as worded, quantify over a global macrostate or
  phase of (S, φ) — "(S, φ) in its equilibrium macrostate", "the (non-)equilibrium phase of (S, φ)",
  "substrata in (perpetual) equilibrium", "equilibrium microstates", "every local subsystem" of a
  globally specified state — or over a typical set of a measure?

Verdicts, generated from the answers:

| Q1 | Q2 | Verdict |
|---|---|---|
| no | — | **RETAINED** (unchanged). If R stipulates its own local equilibrium, that stipulation is recorded as an instance of (LE-eq)/(LE-T), with no change to R |
| yes | no | **RETAINED-WITH-(LE)**: R holds with (LE-eq) or (LE-T) (per §2) as a named hypothesis added to all of R's printed hypotheses ((EM), rate condition, uniform erosion, bounded diameter, finite S or (IL), as printed), and with no other change of quantifier or scope |
| yes | yes | **NOT FOLLOWING** as worded. The audit records why, and the strongest weaker result that does follow, which is its D(𝓡) form under the condition (LE-eq) or (LE-T), with every printed hypothesis carried |
| cannot be answered from the cited text | | **UNDETERMINED**, with what is missing |

A verdict is about the consumer's logical dependence only. RETAINED or RETAINED-WITH-(LE) does not
make R established beyond its printed status; every existing condition and source gap (REMAINDER
M18, M20; A1-05) is carried unchanged.

## 5. What the audit reports for each consumer, and overall

1. Verdict, with Q1/Q2 answers quoted from the site; the condition the consumer carries.
2. What still needs physical sourcing: the equilibrium state ω_Σ and family 𝓔; the link from the
   actual law to ω_Σ (δ_LE); whether (EM) is still needed separately (M:760 says typicality supplies
   the state, not the mixing).
3. For NOT FOLLOWING: why, and the strongest weaker result.
4. Whether (LE-eq)/(LE-T) is weaker than A1 + canonical typicality: logical comparison; satisfiability
   on an infinite carrier from existing results (R1-INF Lemma 1, Prop. 3, Prop. 6); the m_H
   countermodel (STAGE0 F3; R1-INF Prop. 9 (b)); observational checkability in principle.
5. A theorem-recovery note (Code Review Rules, "Theorem recovery before concession") for each
   NOT FOLLOWING result: the strongest existing result, its hypotheses and dependencies, the proposed
   repair (L8, REMAINDER :163), what existing evidence supplies toward it, and the remaining gap.
   Failure to recover is recorded as open, not as disproof.

Writer's own algebra or elementary reasoning is marked [W]; everything else is cited.

## 6. Controls

| Id | Control | Pass condition |
|---|---|---|
| K1 | Non-consumers come out unchanged | T1, T4 and T13 — which STAGE0 (M19.b, :130, :219–222) and REMAINDER (M18, M20) record as not using the global-to-local inference — are RETAINED. A different verdict voids the classification until the rule or the trace is re-examined, and is recorded as a deviation |
| K2 | The rule is not vacuous | T6, the replaced step itself, is NOT FOLLOWING |
| K3 | The m_H countermodel | For the selected update (d ≥ 2, q prime, α ≠ 0), Haar measure m_H on H = {x : x_t(0) = 0 ∀t} is invariant with full centred entropy density (R1-INF Prop. 9 (b)). Each of (LE-ref), (LE-eq), (LE-T) either excludes m_H as a local-equilibrium law (on a stated class of regions, with the TV distance computed) or is flagged as admitting it |
| K4 | (LE) is not presented as derived | Every row that uses (LE-eq) or (LE-T) names it as a hypothesis; no sentence in `AUDIT.md` states that OI derives, selects or explains it. Checked by reading every occurrence of "derive", "follows", "implies" near "(LE" |
| K5 | Boundary uses are not consumers | GR Thm A.8, ch07:126–151, ch18:140, ch18:200 do not cite M:764's step |
| K6 | Scope | The unit's diff touches only this directory |

## 7. Limits

No new law, measure or selection principle is constructed; existing laws (β_A, m_H, Gibbs/DLR
states named in R1-INF) are cited only. No proof of L8 is attempted beyond reporting what existing
results give toward it. The O(ε) error, the transfer of the iterated-channel bound to actual record
laws, uniform erosion and the fluctuation-conditioned law are existing source gaps (REMAINDER M18,
M20; A1-05) and are carried, not addressed. No manuscript, Lean, ledger or census change; any
correction suggested by a finding needs its own unit and owner authorization.
