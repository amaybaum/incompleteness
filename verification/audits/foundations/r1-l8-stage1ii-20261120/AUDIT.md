# R1-L8 Stage 1(ii) — global canonical typicality replaced by a declared local-equilibrium condition

**Status.** Writer's paper-only audit, WIP / UNVERIFIED. Revised after the independent review of
`a7eb5916` ([PR #1460 comment 7045557506](https://github.com/amaybaum/incompleteness/pull/1460#issuecomment-7045557506),
round 1, REVISE; answered in §13). A delta review is required. Conditions, consumer list, decision
rule and controls were fixed in `PREREG.md` (commit `08f63c9d`, pushed before this file, unchanged
since). Existing evidence only: no new measure construction, no replacement law, no manuscript,
Lean or registry edit. The local-equilibrium conditions below are declared hypotheses; this audit
derives none of them and does not present any of them as derived. A1 (Main posit ledger item (ii))
remains open and unadopted. Independent non-author review is required before any use.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7044998279](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7044998279),
2026-11-20T16:37:21Z, item 1. Goal link (§A.47): "Stage 1(ii) bears on removing A1 (the R1/R5
residue)."

**Source pin.** `main` at `800cfec6655aa5e9efaf39d6c7823bf2f40795e2`; site and record abbreviations
as PREREG, plus `Meth:n` for line `n` of `papers/Methodology.md` (D3). [W] marks the writer's own
elementary reasoning; everything else is cited.

## 1. Verdict (generated from the table in §3)

**44 rows.** They are the 21 preregistered consumers, with T7, T11, T17 and T20 split into
separately worded claims (D1), plus 16 consumers added after review (†, D3).

| Verdict | Count | Rows |
|---|---|---|
| **RETAINED** | 21 | T1, T4, T5, T7a, T10, T11a, T11d, T13, T17a, T19, T20a, T21, T24b, T30–T37 |
| **RETAINED-WITH-(LE)** | 11 | T2, T3, T8, T9, T23, T24a, T25–T29 |
| **NOT FOLLOWING** | 12 | T6, T7b, T11b, T11c, T12, T14, T15, T16, T17b, T18, T20b, T22 |
| **UNDETERMINED** | 0 | — |

- **Retained.** None of these uses the typicality step, and all are unchanged (K1 passed):
  - the τ_B bound;
  - the anti-Boltzmann-brain corollary;
  - the rate-condition analysis;
  - the region-level exclusion of (C2-slow) ("No bounded-diameter partition supports (C2-slow) in
    that description"), with its companion and book restatements;
  - the time-symmetry statements.
- **Retained with (LE).** Each holds with the condition named:
  - the thermal "in particular" clause, with (LE-T);
  - the proof's division of labour: (LE) supplies the state, (EM) the mixing;
  - the scope lists (M:664, M:732, M:766);
  - the statements that the observer-selection rule "selects where observers can exist" (M:750,
    Sub:14, :26, :371, :407, :413).
- **Not following as worded.** Every statement worded about the global equilibrium macrostate or
  phase of (S, φ):
  - the global-to-local step itself (T6);
  - "observers exist only in the non-equilibrium phase of (S, φ)" (T7b) and the §4.6 heading (T22);
  - their restatements at Sub:56, :401, :542, Str:718, :734, Comp:212, ch02:192 and ch04:178;
  - the past-hypothesis replacement (Sub:56, Comp:212).

  The verdicts follow Q2. The underlying reason is G3: in the iterated description the phase has no
  purchase, so these statements are not supported even with T6. What does follow is the region
  form W* (§6).
- **G2 [W] — local equilibrium enters no proof step.** In the iterated description, the τ_B bound
  and the failure of (C2-slow) use only (EM) at a fast rate on the region; neither canonical
  typicality nor (LE) enters. Local equilibrium does three other jobs:
  - it labels the regions where the fast-(EM) posit is asserted;
  - it supplies a temperature for the thermal reading;
  - in its (LE-ref) part, it is the state link that the existing transfer gap (REMAINDER M18) needs.
- **G3 (review M1; NEW under §A.31) — the phase cannot be discriminated.** K_Σ = P_Σ U P_Σ depends
  only on (φ, μ, Σ). So in the iterated description the equilibrium/non-equilibrium distinction
  cannot discriminate where observers are, and T6 does no logical work in T7's chain.
  Phase-discriminating content can exist only at the level of actual laws, which is the transfer
  gap. That gap is open with or without T6, L8, or A1 + [31].
- **(LE) is weaker as a premise but has no source.**
  - It needs no total finiteness, no global law and no typical-set quantifier.
  - (LE-eq) is satisfiable on an infinite carrier at β = 0.
  - No finite-temperature equilibrium family exists on `main` for the selected update.
  - Nothing on `main` sources the link from the actual law to the equilibrium state (§5, §7).

## 2. The condition used

From PREREG §2, unchanged. The setting:

- Ω is a configuration space of any cardinality, and μ is the reference law of (IL)/(EM).
- 𝓡 is a declared family of bounded-diameter finite regions.
- ν is the actual law: the declared preparation, conditioned on the declared macro-data.
- δ_LE is a declared tolerance.

The conditions:

> **(LE-eq)** For every Σ ∈ 𝓡: ‖ν|_Σ − ω_Σ‖_TV ≤ δ_LE, where ω_Σ = μ|_Σ is the Σ-marginal of a law
> in a declared equilibrium family 𝓔 (translation-invariant, update-invariant Gibbs/DLR states of a
> declared local interaction, β = 0 included), specified independently of the conclusion.
>
> **(LE-T)** (LE-eq) with 𝓔 at finite inverse temperature β = 1/(k_B T_local) > 0 for a declared
> real-valued conserved local energy of the update.
>
> **(LE-ref)**, used only in K3, G2 and I1: ‖ν|_Σ − μ|_Σ‖_TV ≤ δ_LE for an arbitrary invariant μ.
> It is the first clause of (LE-eq).

These conditions are region-wise over 𝓡 and say nothing about regions outside D(𝓡), a global
macrostate, or a typical set. They are hypotheses to be declared, not results.

## 3. Per-consumer table

**Q1:** does the result use the typicality step (M:764's global-to-local inference, or [31])? Q1 is
answered by logical use in the result's argument, not by phase words in a premise (D4).

**Q2:** is the result's conclusion worded about a global macrostate or phase of (S, φ), or about a
typical set? (PREREG §4.)

† marks a consumer added after review (D3).

| Id | Site | Result (quoted or paraphrased) | Q1 | Q2 | Verdict | Condition carried / why not / strongest weaker result |
|---|---|---|---|---|---|---|
| T1 | M:754–756, :760 | τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε) for the iterated description | No: the decay step is "under (EM) its dissipative gap … bounds the decay … exponentially at rate 1/τ_mix" with the causal cone | — | **RETAINED** | Unchanged: (EM), bounded diameter, finite S or (IL). "Typical-set corrections" in ε name no proof step; ε is unquantified on `main` either way (REMAINDER M18; A1-05 :21) |
| T2 | M:758 | "if Σ_loc(V) is in its local equilibrium macrostate in the sense of canonical typicality [31], τ_B(V) is bounded by the local thermal decorrelation time" | Yes ([31]) | No: an "if" about one region | **RETAINED-WITH-(LE)** | (LE-T) on {Σ_loc(V)} governs the clause. With μ\|_Σ the Gibbs marginal at T_local, the correlations K_Σ controls are equilibrium correlations, so τ_mix is the local thermal decorrelation time [W]. (Outside the clause, for comparison only: under (LE-eq) at β = 0 the bound holds but has no thermal scale.) |
| T3 | M:760 | "canonical typicality [31] supplies the local-equilibrium *state*, not the temporal mixing, which is exactly what (EM) posits" | Yes | No | **RETAINED-WITH-(LE)** | (LE-eq) supplies the state, and (EM) is still needed separately; the two are logically independent (I1). By G3, M:760's "dissipative gap — which on an equilibrium macrostate sets the local thermal decorrelation rate" names the gap's value thermally under (LE-T); the gap itself is the same on every macrostate |
| T4 | M:762 | Anti-Boltzmann-brain corollary; (GT) illustration | No: local thermal equilibrium of Σ_BB is stipulated ("that is what 'fluctuation from equilibrium' means"); [31] not cited (STAGE0 M19.b; REMAINDER M20) | — | **RETAINED** | Unchanged: (EM), τ_mix(Σ_BB) ≪ τ_S, uniform erosion; the (GT) illustration adds T_local. The stipulation is an instance of (LE-T) on {Σ_BB}; naming it changes nothing |
| T5 | M:764 to "remains open." | The theorem and (C2-slow) do not compose without τ_mix ≪ τ_S; "a sufficiently fast-mixing equilibrium supports no observer satisfying … (C2-slow)"; dS thermal scale | No | — | **RETAINED** | Unchanged. "Equilibrium" here is a region's stipulated state |
| T6 | M:764 | "For (S, φ) in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its local equilibrium" | Yes | Yes | **NOT FOLLOWING** | It is the replaced step: (LE) asserts local equilibrium only on declared regions and implies nothing from a global macrostate. Weaker results and recovery: §8 |
| T7a | M:764 | "By the theorem — under (EM) for each region's effective channel … — τ_B(V) is bounded by the local τ_mix for every bounded-diameter partition V. No bounded-diameter partition supports (C2-slow) in that description." | No: (EM) is stated per region and the rate condition outright; T6 does no logical work here (G3) | — | **RETAINED** | Unchanged: (EM) for each region with τ_mix ≪ τ_S, finite S or (IL). Its matching book sentence is T20a |
| T7b | M:764 | "That every relevant equilibrium region satisfies (EM) at the required rate is itself a physical hypothesis … observers therefore exist only in the non-equilibrium phase of (S, φ)"; C1–C4 "not satisfiable in the coarse-grained description of the equilibrium phase" | Yes (via T6) | Yes | **NOT FOLLOWING** as worded | W* (§6). By G3, the phase restriction is not supported in the iterated description even with T6. Its content is T7a over every region for which the fast-(EM) posit holds, plus a label |
| T8 | M:766 | Inputs include "the canonical-typicality result [31]"; "the canonical-typicality clause" is a finite-representative statement | Yes | No | **RETAINED-WITH-(LE)** | Input list with (LE-eq)/(LE-T) in place of [31]. The finite-representative restriction belonged to [31]'s finite shell; (LE-eq) is stated on region marginals and is satisfiable on an infinite carrier (§7). O(ε) and exact recurrence stay finite-representative. O1(b): "the theorem uses [31]", but T1's bound does not; only T2's clause and T6 do |
| T9 | M:750 | "the rule" (the selection rule of the §4.6 heading, M:748) "on where in a finite bijective (S, φ) observers can exist … conditional on (EM) … and on the rate condition" | Yes (the rule is T5–T7) | No: "where … observers can exist" is met by W* | **RETAINED-WITH-(LE)** | Conditions: (EM), rate condition, (LE-eq) as the domain label. O1(b) (weak): the printed list omits [31]; by G3 the region-level exclusion needs only (EM) and the rate |
| T10 | M:171 | The erasure lemma bounds the readback left by fast mixing "in the exclusion arguments below — the equilibrium phase, and the anti-Boltzmann-brain corollary" | No | — | **RETAINED** | The remark's content is the erasure lemma; its pointer to "the equilibrium phase" inherits T7a/T7b |
| T11a | Sub:56 | "τ_B(V) is bounded by the local mixing time on equilibrium microstates, so C2 fails there in its timescale form, … wherever that mixing time is short compared with τ_S" | No: the rate condition is per region ("wherever …"), and T1's bound holds on every microstate (G2, G3); restricting to equilibrium microstates only weakens it (D4) | — | **RETAINED** | Unchanged: (EM) and the per-region rate condition |
| T11b | Sub:56 | Observers "structurally restricted to the non-equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W*; G3 |
| T11c | Sub:56 | "this replaces the low-entropy 'past hypothesis', in its role of selecting observer-compatible configurations, with a structural observer-selection rule" | Yes | Yes (global configurations) | **NOT FOLLOWING** | W* selects regions, not global configurations. Whether a configuration of a globally equilibrated (S, φ) has every observer-relevant region in (LE) is the dropped step. By G3, a phase-discriminating selection would in any case need actual laws. Sub:56 already records the infinite-carrier form as open; under (LE) the replacement does not follow on a finite carrier either |
| T11d | Sub:56 | "excludes Boltzmann brains structurally rather than anthropically"; "The rule is time-symmetric" | No (T4; T13) | — | **RETAINED** | As T4. Sub:56 attributes the BB exclusion to the phase restriction; T4 supplies it without that restriction |
| T12 | Sub:401 | "The observer's confinement to the non-equilibrium phase of (S, φ) … is a structural consequence of the effective-mixing hypothesis" | Yes | Yes | **NOT FOLLOWING** as worded | W*; G3. O1(b): the attribution to (EM) is accurate for W*; the phase wording is the defect |
| T13 | Sub:409 | The spectral-gap bound "applies equally in both directions" | No | — | **RETAINED** | Unchanged (K1) |
| T14 | Sub:542 | "the *equilibrium phase* of (S, φ) is … observer-free for sufficiently fast-mixing equilibria" | Yes | Yes | **NOT FOLLOWING** as worded | W*: regions with fast (EM) are free of (C2-slow) observers in the iterated description; G3 |
| T15 | Str:718 | "substrata in perpetual equilibrium cannot satisfy C2's slow-bath route" | Yes | Yes | **NOT FOLLOWING** as worded | W* with 𝓡 the observer-relevant regions at every time; G3. The first sentence of Str:718 (phases with mixing faster than recurrence) does not use the step and is not classified (D2) |
| T16 | Str:734 | "non-equilibrium-phase … features required for C1–C4" | Yes (via T7b) | Yes | **NOT FOLLOWING** as worded | W* gives a necessary condition on the observer's region (no fast (EM)), not on a global phase. The claim that random permutations "typically lack" these features is a separate claim, not traced here |
| T17a | Comp:212 | Boltzmann brains have τ_B bounded by local thermal decorrelation; "not observers in the sense of C1–C4 with C2 read in its timescale form" | No (T4) | — | **RETAINED** | As T4, with its (GT) estimate |
| T17b | Comp:212 | Observers "cannot exist in the equilibrium phase of (S, φ)"; past hypothesis "replaced … by the same theorem" | Yes | Yes | **NOT FOLLOWING** as worded | W*; G3; past-hypothesis replacement as T11c. Its sub-clause "τ_B is bounded by the local mixing time on equilibrium microstates, so C2 fails there in its timescale form" follows, as T11a |
| T18 | ch02:192 = FULL:822 | The theorem "restricts observers … to the non-equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W*; G3 |
| T19 | ch03:58 = FULL:919 | Conditional Boltzmann-brain exclusion for bounded-diameter partitions under effective mixing and τ_mix ≪ τ_S | No | — | **RETAINED** | Unchanged |
| T20a | ch04:178 = FULL:1282 | "bounded-diameter partitions fail C2-slow" under effective mixing and τ_mix ≪ τ_S; suppression under uniform erosion | No | — | **RETAINED** | Unchanged (the book counterpart of T7a) |
| T20b | ch04:178 = FULL:1282 | The heading attributes T20a to "The equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W*; G3 |
| T21 | LEDGER :1367, :1381, :1395; `verification/lean*/` | Kernel status of the theorem and both corollaries | No kernel statement | — | **RETAINED** | All three entries are kernel `GAP`, "not formalized". No Lean module states a §4.6 result; `OIBridge/ThermalOrientation.lean` uses Boltzmann ratios for orientation, not typicality |
| T22 † | M:748 | §4.6 heading "Structural Exclusion of Equilibrium-Phase Observers" | Yes (via T7b) | Yes | **NOT FOLLOWING** as worded | Counterpart of T20b. W*; G3 |
| T23 † | M:664 | "canonical typicality [31], which the structural observer-selection theorem of §4.6 uses" | Yes | No | **RETAINED-WITH-(LE)** | As T8: (LE-eq)/(LE-T) in place of the import. O1(b): T1's bound does not use [31] |
| T24a † | M:732 | Posit ledger: "the canonical-typicality step of §4.6 [is a statement] about finite representatives" | Yes | No | **RETAINED-WITH-(LE)** | As T8: the replacing (LE) clause is not finite-only (§7) |
| T24b † | M:732 | Other §4.6 mentions in the ledger: (IL) "for the decay estimate of §4.6"; §4.6 "consumed" by the deep-sector enlargement; posits (viii), (ix) used by §4.6; the mixing hypothesis and "the typicality selection in (iv)" (the measure selection of posit (iv), not [31]) | No | — | **RETAINED** | Unchanged |
| T25 † | Sub:14 | "a third projection that supplies a time-symmetric observer-selection rule" | Yes (the rule) | No | **RETAINED-WITH-(LE)** | As T9 |
| T26 † | Sub:26 | "the C1–C4 observer-selection theorem of [Main, §4.6], which is time-symmetric and selects where observers can exist" | Yes | No | **RETAINED-WITH-(LE)** | As T9 |
| T27 † | Sub:371 | The arrow-of-time projection "supplies the time-symmetric C1–C4 observer-selection theorem of [Main, §4.6]" | Yes | No | **RETAINED-WITH-(LE)** | As T9 |
| T28 † | Sub:407 | "C1–C4 observer selection via Main §4.6 for a finite bijective (S,φ), conditional on its effective-mixing hypothesis …, which fixes where observers exist, not a direction" | Yes | No | **RETAINED-WITH-(LE)** | As T9; O1(b) |
| T29 † | Sub:413 | "the observer selection on the effective-mixing hypothesis and the iterated-channel description" | Yes | No | **RETAINED-WITH-(LE)** | As T9; O1(b) |
| T30 † | Str:532 | Compactifications whose cosmological structure "mixes fast compared with τ_S in the coarse-grained description of [Main §4.6], fail C2's slow-bath route" | No | — | **RETAINED** | Unchanged (region-level, fast mixing) |
| T31 † | Meth:162 | "effective mixing at the stated rate excludes C2-slow for the specified fast equilibria [Main §4.6]" | No | — | **RETAINED** | Unchanged |
| T32 † | Meth:283 | "(EM) and the rate condition of [Main §4.6] exclude bounded-diameter partitions satisfying C2-slow in the fast-equilibrium coarse model" | No | — | **RETAINED** | Unchanged |
| T33 † | Meth:441 | "The proved exclusion uses a finite bijective model, a chosen effective channel and the mixing and rate hypotheses of [Main §4.6]" | No | — | **RETAINED** | Unchanged; by G3 this list is complete for the exclusion |
| T34 † | ch04:36 = FULL:1140 | (EM) and its rate condition "exclude C2-slow for bounded-diameter partitions at fast-mixing equilibrium in the finite bijective model's iterated coarse description" | No | — | **RETAINED** | Unchanged |
| T35 † | ch02:194 = FULL:824 | Observer selection "conditional on the effective-mixing hypothesis … which excludes C2-slow for bounded-diameter partitions in sufficiently fast-mixing equilibria of that coarse model" | No | — | **RETAINED** | Unchanged |
| T36 † | ch01:221 = FULL:554 | Under effective mixing and uniform erosion the iterated coarse dynamics suppresses the readback gap when τ_mix ≪ τ_S | No | — | **RETAINED** | Unchanged |
| T37 † | ch03:26 = FULL:887 | "Even an exact short orbit can give a gapped compressed channel ([Main §4.6])" | No | — | **RETAINED** | Unchanged |

## 4. Findings

**G1 [W] — the typicality step and OI's microstates.**

1. *What [31] covers.* [31] concerns pure states ψ drawn from the normalized unitarily invariant
   measure on a shell subspace. For most such ψ, the reduced state of a fixed subsystem is close to
   the shell's marginal.
2. *What an OI microstate is.* A configuration. In the fixed-basis representation it is a basis
   vector |s⟩ = |s_Σ⟩ ⊗ |s_rest⟩, under the site factorization (M:732, posit (viii)). Its reduced
   state on Σ is the pure state |s_Σ⟩⟨s_Σ|.
3. *Distance from the shell marginal.* For the projector P = |s_Σ⟩⟨s_Σ|, the trace distance obeys
   D(|s_Σ⟩⟨s_Σ|, Ω_Σ) ≥ tr P(|s_Σ⟩⟨s_Σ| − Ω_Σ) = 1 − ⟨s_Σ|Ω_Σ|s_Σ⟩ ≥ 1 − λ_max(Ω_Σ). For a diagonal
   Ω_Σ this holds with equality at 1 − Ω_Σ(s_Σ). The distance is close to 1 whenever Ω_Σ is spread
   over many configurations, so configuration microstates lie outside the typical set.
4. *Two readings, neither typicality.* For superposition states the step is not a statement about
   OI's microstates. For an ensemble (the uniform law on the shell), its conclusion is the exact
   marginal of that law. That needs no typicality, and it is the selected counting law, class (c) in
   STAGE0 M19.a.
5. *Relation to earlier records.* This sharpens MAIN-ROOTS :95, which notes that [31] does not
   "guarantee the desired marginal for every microstate and every cut".
6. *Consequence for (LE).* It supports stating (LE) for laws (PREREG §2) and not for single
   configurations: the configuration on one region is a point, with no local-equilibrium content of
   its own. A classical substratum analogue exists as an average over translates or over time along
   the orbit, for typical configurations of an ergodic law (R1-INF :389: spatial frequencies by the
   strong law, temporal averages by the ergodic theorem; §8 L8-typ).

**G2 [W] — what local equilibrium does in the §4.6 chain.** In the iterated description, K_Σ =
P_Σ U P_Σ is fixed by the reference law μ, and the bound of T1 is a property of K_Σ under (EM). It
does not refer to the region's actual state. The failure of (C2-slow) (T5, T7a) follows from that
bound and τ_mix ≪ τ_S for the region.

The global corollary's chain (M:764) runs:

1. global equilibrium;
2. ⇒ (T6) every region in local equilibrium;
3. ⇒ fast (EM) on every such region, by the posit "That every relevant equilibrium region satisfies
   (EM) at the required rate is itself a physical hypothesis";
4. ⇒ (T1) no (C2-slow).

Local equilibrium therefore enters only

- (i) as the label of the regions on which the fast-(EM) posit is asserted;
- (ii) for the thermal reading of τ_mix and (GT), through (LE-T);
- (iii) as the link between the actual law and the reference law, ‖ν|_Σ − μ|_Σ‖ ≤ δ_LE. The
  transfer from the iterated description to actual record laws requires this link. That transfer
  is the existing A1-independent gap of REMAINDER M18 and A1-05 P8-M ("relation of P_Σ U^n P_Σ to
  K^n", "comparison to actual history-conditioned observables").

Replacing the typicality step by (LE) changes no proof step of the bound or of the (C2-slow) failure.

*Pressure test of this favourable reading.* The physical exclusion, as distinct from the statement
in the iterated description, needs (iii). Nothing on `main` sources (iii). So the physical reach of
the observer-selection rule is not improved: the need moves from typicality to the actual-state link,
which was already open.

**G3 — the phase has no purchase in the iterated description.** Raised by the independent review
(round 1, M1); checked here [W]. NEW under §A.31: it is stronger than restating G2 and constrains
every phase-worded row.

1. *K_Σ ignores the state.* K_Σ = P_Σ U P_Σ depends only on (φ, μ, Σ), not on the actual state or
   macrostate. The same region at two times has the same K_Σ. When φ commutes with translations and
   μ is translation invariant (the counting law on a torus, or β_A), translates of a region have
   conjugate K_Σ, with the same spectrum and decay.
2. *Neither result can be phase-specific.* (EM) at a given rate on a region is therefore a property
   of the region's shape, not of its phase. Consider T7a's chain, (EM) per region plus the rate
   condition. If that holds for the regions observers would occupy, it excludes (C2-slow) observers
   in the non-equilibrium phase as well. If it fails there, it fails for equilibrium regions of the
   same shape too.
3. *What the phase statements reduce to.* Within the iterated description, the phase-worded
   statements (T7b, T11b, T12, T14–T16, T17b, T18, T20b, T22) reduce to T7a, i.e. W* over every region
   for which the fast-(EM) posit holds, plus a label that discriminates nothing. T6 does no logical
   work in T7's chain.
4. *Where phase content could come from.* Only from statements about actual laws: that the actual
   record law of an equilibrium region has decaying history contrasts, and an observer region's does
   not. That is G2 (iii), the transfer gap, which is open with or without T6.
5. *Bearing on M:760.* "Its dissipative gap — which on an equilibrium macrostate sets the local
   thermal decorrelation rate": the gap is a property of K_Σ and is the same on every macrostate. The
   parenthetical can name its value thermally under (LE-T) compatibility (T2). It does not make the
   gap phase-dependent.

**I1 [W] — (LE) and (EM) are logically independent.** (EM) is a property of (φ, μ, P_Σ) and does not
involve ν, whereas (LE) does, so the independence is immediate. Two witnesses:

- *(LE) without (EM).* Take φ = id on Ω = A^{Z^d} with μ = ν = β_A. β_A is the zero-interaction DLR
  state, translation invariant and invariant under the identity, so (LE-eq) holds with δ_LE = 0 on
  every region. But U is the identity, so K_Σ = P_Σ: centred local observables do not decay, and
  (EM) fails.
- *(EM) without (LE).* Main's own four-state example (M:766): cells {0,1} and {2,3}, φ the
  transposition (0 2), μ uniform. Its K_Σ has eigenvalues 1 and 0, so centred observables are
  annihilated in one step and (EM) holds. With ν = δ_0, the cell marginal is (1, 0) against (½, ½),
  at TV distance ½. So the (LE-ref) clause contained in (LE-eq) fails for δ_LE < ½. The example lies
  outside (LE-eq)'s lattice setting, and it refutes only that clause.

Hence (EM) is still needed separately, as M:760 states for canonical typicality.

**O1 — routing to a separate correction unit (observations only).**

- **(a) Genuine, low to moderate.** M:764 states that [31] "implies every local subsystem is also in
  its local equilibrium". [31] gives this only for typical ψ and a fixed subsystem, and the
  typical-state quantifier, with its measure, is dropped from the corollary. G1 sharpens this: the
  typical set excludes configuration microstates, so as worded about the microstates of (S, φ) the
  step does not apply.
- **(b) Weak.** The condition lists at M:750, Sub:401, Sub:407 and Sub:413 omit [31]. An imported
  theorem need not be listed as a hypothesis, and by G3 the region-level exclusion uses (EM) and the
  rate condition alone, so these attributions are accurate for W*; where there is a defect, it is in
  the phase wording (the NOT FOLLOWING rows). Conversely, M:664 and M:766 say the theorem "uses"
  [31], while T1's bound does not; only T2's clause and T6 do. This is a minor imprecision.

This audit edits nothing; under §A.25 any correction would be propagated in its own authorized unit.

## 5. What still needs physical sourcing

| Item | Needed by | Source on `main` |
|---|---|---|
| The equilibrium family 𝓔 and its states ω_Σ | (LE-eq), (LE-T); T2, T3, T8, T9, T23–T29, W* | **β = 0:** β_A, the zero-interaction DLR state (R1-INF Prop. 6 (a)), invariant under every injective CA (R1-INF Lemma 1 (c)). It is selected by P-ED, i.e. by the posited (G3) + (G4) (R1-INF Prop. 3), or by a declared law (H-μ). It is not derived (R1-INF §6.4). **β > 0:** none. (LE-T) needs a real-valued conserved local energy. SM:292 records that the exact linear rule conserves its quadratic energy only modulo q and that neither it nor the rounded rule supplies "the required real positive-definite conserved energy". R1-INF Prop. 6 leaves d ≥ 2 undetermined, and in d = 1, α² = 1 the conserved mover densities give a family with free parameters. A measured local temperature would enter as an explicit empirical input (class E), not a derivation |
| Reference compatibility μ\|_Σ = ω_Σ | (LE-eq); G2 (iii) | None: A1-05 P8-M first stop, "No existing source in the trace selects the normalized invariant probability for the physical readout" |
| The actual-law link ‖ν\|_Σ − ω_Σ‖ ≤ δ_LE (a preparation or relaxation account) | (LE-eq); transfer to actual records; any phase-discriminating statement (G3) | None: A1-05 P8-S first stop, "no normalized equilibrium state for a specified encompassing region, selected by the physical update or preparation" |
| (EM) on each region, at τ_mix + O(ε) ≪ τ_S | T1–T9, W* | None: an explicit physical hypothesis (M:752), established "model by model" (M:766). Still needed separately (I1). On the infinite full product, β_A is mixing of all orders for the selected update with α a unit (R1-INF Prop. 5). That is exact-dynamics mixing without a rate; it is not (EM) for K_Σ |
| The posit that the regions of 𝓡 mix fast | T7a, T7b and their restatements | Posited (M:764) |
| Uniform erosion; O(ε); transfer of the τ_B bound | T4, T7a, readback suppression | Existing A1-independent gaps (REMAINDER M18, M20; A1-05), carried unchanged |

## 6. What no longer follows, and the strongest weaker result

**What fails.** Each NOT FOLLOWING row asserts something about the global equilibrium macrostate or
phase of (S, φ). The verdict comes from Q2, and there are two reasons behind it:

- Under (LE) nothing connects a global property to the regions, because (LE) replaces the connecting
  step T6 without deriving it.
- More basically (G3), in the iterated description the phase cannot be discriminated at all. So the
  phase wording would not be supported there even with T6.

The rows fall into two groups:

- **The global-phase statements** (T6, T7b, T11b, T12, T14, T15, T16, T17b, T18, T20b, T22):
  "observers exist only in the non-equilibrium phase of (S, φ)", its restatements and the §4.6
  heading.
- **The past-hypothesis replacement** (T11c, T17b): it selects observer-compatible global
  configurations. That needs the global-to-local step and, by G3, a phase-discriminating statement
  about actual laws.

**Strongest weaker result W\*.** It follows under the stated hypotheses; it is not presented as
physically established. Let 𝓡 be a declared family of bounded-diameter regions, and assume:

- (EM) for K_{Σ_loc(V)}, for every V with Σ_loc(V) ∈ 𝓡, with τ_mix + O(ε) ≪ τ_S;
- finite S, or (IL) for the decay estimate, as M:766 states.

Then, in the coarse-grained description generated by iterating K_{Σ_loc(V)}, no such V supports
(C2-slow). Under uniform erosion, its order-k readback gap is bounded by δ_0 e^{−(k−1)τ_S/τ_B} for
k ≥ 2. This is T7a.

- With (LE-eq) on 𝓡, D(𝓡) is a domain of local equilibrium, and the statement reads: (C2-slow)
  observers occur only outside the fast-mixing local-equilibrium domain.
- With (LE-T), τ_mix is a thermal decorrelation time.

By G2 and G3, W* holds with fast (EM) on 𝓡 alone. (LE) only labels the domain, and the label
discriminates nothing within the iterated description. W* says nothing about a global phase, about
which global configurations host observers, or about regions outside D(𝓡).

For the anti-Boltzmann-brain corollary nothing is lost: its neighbourhood equilibrium was always
stipulated (T4). The corollary still covers only fluctuations inside a neighbourhood stipulated to be
in local equilibrium; that scope is unchanged and not addressed here.

## 7. Is (LE) weaker than A1 + canonical typicality? (PREREG §5 item 4)

1. **Logical comparison [W].**
   - *What the A1 route gives.* A1 with the selected spherical shell measure, bath size and weak
     coupling gives, by [31], the region condition for typical superposition states, per subsystem,
     with δ_LE set by [31]'s bound. On that typical set the route implies (LE) in the
     quantum-representation reading (PREREG §2).
   - *Why (LE) is weaker as a premise.* (LE) implies neither A1 (item 2) nor any global macrostate or
     law selection. It drops total finiteness, the shell, the spherical measure and the typical-set
     quantifier.
   - *What the A1 route does not give.* (LE) is not inherited from that route by OI's configuration
     microstates (G1). At the level of laws, the A1 route reaches (LE) only through a selected law
     (class (c)), not through typicality:
     - at β = 0 the torus counting law μ_L has uniform marginals on boxes smaller than the torus
       (R1-INF Lemma 1 (b)), which are β_A's;
     - for an energy shell, its marginal approximates a Gibbs marginal only through equivalence of
       ensembles, which needs a real conserved energy that `main` lacks for the selected update (§5).
2. **Infinite carriers.** (LE-eq) at β = 0 holds with δ_LE = 0 on every finite region of
   Ω = A^{Z^d}, for every injective CA, with μ = ν = β_A. β_A is invariant (R1-INF Lemma 1 (c)) and is
   the zero-interaction DLR state (Prop. 6 (a)), and its finite marginals are uniform by its product
   form [W]. So (LE) is consistent without A1. This holds only at β = 0 and only with β_A declared;
   it is not derived (§5). Finite-β (LE-T) on an infinite carrier is undetermined on `main` for the
   selected update.
3. **The m_H countermodel (control K3).** For the selected update (d ≥ 2, q prime, α ≠ 0), m_H is
   update-invariant with h̄(m_H) = log|A| (R1-INF Prop. 9 (b); STAGE0 F3). H requires x_t(0) = 0 for
   all t, including x_0(0) = u(0) and x_{−1}(0) = v(0), so the one-site marginal of m_H at the origin is
   δ_{(0,0)} [W]. Against each condition:
   - **(LE-ref) admits m_H** (flagged). With μ = ν = m_H it holds with δ_LE = 0 on every region.
     (LE-ref) only ties the actual law to whatever invariant reference is chosen, so it does not
     certify equilibrium marginals.
   - **(LE-eq) excludes m_H**, on every region containing its special site.
     - As a reference: m_H is not translation invariant (Prop. 9 (b)), so it is not admissible in 𝓔.
     - As an actual law: its TV distance from ω_Σ is at least 1 − ω_0((0,0)), where ω_0 is the
       one-site marginal of the reference; TV does not increase under marginalization.
     - That bound is 1 − q^{−2} at β = 0. It is positive for any Gibbs state of a finite-range,
       finite-valued potential, whose single-site marginals have full support [W]; hard constraints
       (infinite energies) are excluded from that statement.
     - So m_H is excluded whenever δ_LE is below that distance.
   - **Regions avoiding the special site:** not determined here (flagged).

   The exclusion is carried by the translation invariance required of 𝓔. That is the homogeneity
   premise (G3), which STAGE0 F3 and R1-INF §6.1 identify as load-bearing. (LE) does not remove the
   homogeneity question; it moves it into the declared choice of 𝓔. (The premise (G3) of R1-INF is
   unrelated to finding G3 of this audit.)
4. **Observational checkability.**
   - Σ_loc(V) contains hidden sites, so (LE) is not directly verifiable.
   - Its visible consequences are checkable in principle: the visible marginal of ω_Σ on V's labels,
     stationarity of visible statistics and, for (LE-T), consistency with a measured local
     temperature. A mismatch above δ_LE in any of these falsifies the declared instance.
   - The global-to-local inference it replaces has no observable content of its own (REMAINDER M19).
   - So (LE) is falsifiable through its visible consequences, but not verifiable on the hidden part.

## 8. Theorem-recovery note (Code Review Rules)

The twelve NOT FOLLOWING rows share two missing ingredients:

1. the global-to-local step T6, at the level of laws or of typical configurations;
2. by G3, a phase-discriminating statement about actual laws, the transfer G2 (iii). Without it, the
   phase wording is not supported in the iterated description even when T6 holds.

The second is decisive for every phase-worded row. The first matters only to the extent that the
phase statements are read at the level of laws. The past-hypothesis rows add one further gap.

- **Strongest existing results.**
  - (a) *Finite representative.* The imported theorem [31]: per subsystem, for typical ψ under the
    spherical measure on a finite-dimensional shell, with bath size and weak coupling for the
    canonical form. Hypotheses: A1, the shell, the selected measure (STAGE0 M19.a, class (c)), and the
    caveats G1 and O1 (a).
  - (b) *Infinite full product, β = 0, under the posited P-ED.* If the global law is β_A, every finite
    region is in (LE-eq) with δ_LE = 0 [W, product form]. For β_A-almost every configuration:
    - spatial frequencies of patterns converge to the uniform marginals;
    - for α a unit, where β_A is mixing of all orders for the selected update (R1-INF Prop. 5), time
      averages of local observables along the orbit converge to their β_A expectations.

    Source: R1-INF :389 ("spatial frequencies by the strong law …; temporal averages by the ergodic
    theorem"). Hypotheses: the injective-CA class and the posited (G3) + (G4).
  - (c) *Counterexample without (G3).* m_H shows that "update-invariant with maximal centred entropy
    density" does not imply equilibrium local marginals in d ≥ 2 (R1-INF Prop. 9 (b); STAGE0 F3).
    A version of L8 with that premise is false.
- **Proposed repair for T6: L8** (REMAINDER :163, "Local-equilibrium marginals of a supplied invariant
  law on an infinite carrier"). Decomposition [W]:
  - **L8-sel.** At the level of laws, the step is immediate once the global law is declared in 𝓔:
    ω_Σ is by definition its marginal (item (b)). The content is the selection of that law, which is
    R1 and open. It is restored at β = 0 by P-ED with (G3) (R1-INF Prop. 3), and blocked without (G3)
    by (c).
  - **L8-typ.** At the level of configurations, a single region carries no equilibrium content (G1).
    The meaningful forms are averages for typical configurations of an ergodic law in 𝓔: over
    translates (spatial), or along the orbit (temporal). At β = 0 both hold by item (b).
- **What the attempt checked.** Items (a)–(c) were read at their sources. The decomposition and the
  β = 0 marginal statement are [W] and elementary. No new law was constructed.
- **Remaining gap.**
  - **For the phase statements.** L8 alone, or A1 + [31], does not support them in the iterated
    description (G3). They would need a statement about actual record laws that distinguishes
    equilibrium regions from observer regions (G2 (iii); REMAINDER M18; A1-05 P8-M, P8-S), and that
    statement is open with or without T6.
  - **For T6 itself.**
    - a finite-temperature family 𝓔 for the selected update (a real conserved local energy; SM:292;
      R1-INF Prop. 6);
    - selection of the global law in 𝓔 without (G3), or a physical source for (G3);
    - the link from the actual law to that law (§5);
    - a decision whether the global statements are meant at the level of laws or of averages.
      Per-region statements about single configurations are not available (G1).
  - **For T11c and T17b in addition:** the infinite-carrier low-entropy inflow that Sub:56 itself
    records as open (REMAINDER O-INFLOW).
- **Status.**
  - Failure to recover is not a disproof.
  - On the finite representative, the global-to-local step holds only at the level of laws for the
    selected shell law (class (c)), and for [31]-typical superposition states, which are not
    configuration microstates (G1).
  - The global-phase statements are conditional on those, on (EM), on the rate condition, and on the
    posit that every equilibrium region mixes fast (M:764). They are open beyond them. Within the
    iterated description they carry no phase-discriminating content in any case (G3).
  - This unit edits no manuscript text. Any narrowing would need its own authorized unit.

## 9. Controls (PREREG §6)

| Id | Result |
|---|---|
| K1 | T1, T4 and T13 are RETAINED. Passed |
| K2 | T6 is NOT FOLLOWING. Passed |
| K3 | (LE-ref) admits m_H (flagged). (LE-eq) and (LE-T) exclude it on regions containing its special site whenever δ_LE < 1 − ω_0((0,0)) (1 − q^{−2} at β = 0). Regions avoiding the site are flagged as not determined (§7.3). Passed: each condition either excludes m_H or is flagged |
| K4 | Every row using (LE-eq) or (LE-T) names it as a hypothesis. The occurrences of "derive", "follows", "implies" and "holds" near "(LE" were read. Each is one of three kinds: a statement that (LE) is not derived; a conditional ("under (LE) …", "(LE) implies neither …"); or the [W] fact that the β = 0 marginal holds for the declared β_A. Passed |
| K5 | GR Thm A.8 (GR:801–867), ch07:126–151, ch18:140 and ch18:200 = FULL:4931 contain no citation of Main §4.6 or of [31]'s use there. Passed |
| K6 | The diff touches only this directory. Passed (checked at each commit) |

## 10. Deviations from PREREG

- **D1 (splits).** T7, T11, T17 and T20 each contain separately worded claims that the rule
  classifies differently. They are split into sub-rows (T7a–b, T11a–d, T17a–b, T20a–b), and each
  sub-row is classified by the unchanged rule. Without the split, each would be NOT FOLLOWING as a
  whole, which would hide the retained parts:
  - the region-level exclusion (T7a, and its book counterpart T20a);
  - the Boltzmann-brain parts (T11d, T17a).

  The first version split ch04:178 (T20) but not Main's matching sentence in T7, which classified
  the same statement differently at its two sites. T7 is now split for consistency (review, round 1).
- **D2.** T15's first sentence does not use the step and is left unclassified (noted in the row).
- **D3 (census extension).** The first version's claim that no consumer existed beyond the
  preregistered list was false. Sixteen consumers are added (†, T22–T37), with the reason each was
  missed:
  - M:748: the heading's hyphenated "Equilibrium-Phase" escaped the search term "equilibrium phase".
  - M:664 and M:732: hits for "canonical typicality", "canonical-typicality" and "§4.6" that were
    not carried into the table.
  - Sub:14, :26, :371, :407, :413, Str:532, ch04:36, ch02:194 and ch01:221: "observer-selection" or
    "§4.6" hits not carried into the table.
  - Meth:162, :283, :441: `papers/Methodology.md` was outside PREREG's file abbreviations and was
    not searched.
  - ch03:26: found by the added search below.

  The added search covered all of `papers/*.md`, using the preregistered terms plus citations of
  Main §4.6 in the forms "Main §4.6", "[Main, §4.6]", "[Main §§2.3, 4.6]" and "[1, §4.6]". It covered
  Introduction, Computation, Juno, Medicine, Bioinformatics and Methodology, and all `book/*.md`
  files including appendices, glossary, preface and readers' guide. Hits that are not consumers:
  - Meth:253's "§4.6" is Methodology's own section;
  - Juno's "§4.6" cites SM (its reference [18]);
  - Bioinformatics' "[31]" is a different reference;
  - SM's "§4.6" hits are SM's own section;
  - ch10:204 concerns chemistry's observer selection under supplied measures, not Main §4.6.
- **D4 (rule interpretation, T11a).** Q2's list includes "equilibrium microstates". In T11a that
  phrase appears in a premise, while the conclusion is per region ("wherever that mixing time is
  short compared with τ_S"), and T1's bound holds on every microstate. Q1 is therefore read as
  logical use, not as the presence of a phase word in a premise. On that reading T11a does not use
  the step and is RETAINED, consistently with T5, T7a and T20a.

## 11. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7044998279 | Authorization and scope | Provenance; quoted with author and time |
| PR #1460 comment 7045557506 | The review this revision answers; G3 is credited to it | Provenance; G3's content is stated and checked here, on this record |
| #1456, #1457 | Stage 0 and Stage 1(i), whose records are on `main` | Provenance; STAGE0 is cited from its file on `main` at the pin |
| R1-INF's credit to #1431 comment 7025214238 for Prop. 9's argument | Inside a cited record | Provenance; the proof is written out on `main` (R1-INF :280–320) |
| [31] (arXiv:cond-mat/0511091) | G1, §7, §8 | External published theorem, cited as Main does |

## 12. What an independent reviewer must check (delta)

1. The round-1 items, against §13.
2. The 16 added rows (T22–T37) and their Q1/Q2 answers, and that D3's search and its non-consumer
   list are complete.
3. The T7a/T7b split and D4's reading of Q1, and that the split leaves no site classified two ways.
4. G3 as stated, in particular the claim about translates (φ commuting with translations, μ
   translation invariant) and its bearing on M:760.
5. The restated §6 rationale and the §8 framing, especially the remaining-gap entry for the phase
   statements, and the §8 status sentence (B2).
6. G1's revised trace-distance bound and the temporal-average form in L8-typ.
7. The counts in §1 against the table, and that no other count statement in this file is stale.
8. That (LE) is nowhere presented as derived (K4), and that no manuscript, Lean or registry file
   changed (K6).

## 13. Answer to the independent review of `a7eb5916` (round 1, REVISE)

PREREG is unchanged. Each item and where it is answered:

| Item | Change |
|---|---|
| B1 | T11a is RETAINED (rule reading recorded as D4); T17b notes that its matching sub-clause follows; counts updated (§1, §6, §8) |
| B2 | §8 status sentence restated: the step holds on the finite representative only for the selected shell law at the level of laws and for [31]-typical superposition states; the global-phase statements are conditional on those, on (EM), on the rate condition and on the fast-mixing posit, and are open beyond them |
| B3 | Rows T22–T37 added (†); the false "no new consumer" claim withdrawn; D3 records the extended search, including Methodology and the other papers |
| M1 | Recorded as G3, credited to the review and checked. The NOT FOLLOWING rationale is restated in §6, the §8 framing is restated (two ingredients; the actual-law link decisive), and §8's remaining gap is restated for the phase statements. The bearing on M:760 is noted in G3 and T3. The T7 split (T7a/T7b) is made and explained in D1 |
| M2 | G1 and L8-typ include temporal averages for α a unit (R1-INF :389; Prop. 5) |
| M3 | O1 split into (a), genuine and low to moderate, sharpened by G1; and (b), weak, extended to M:664, M:766, Sub:407 and Sub:413 |
| N1 | T2: (LE-T) governs; the β = 0 remark is marked as outside the clause |
| N2 | I1: the four-state example refutes the (LE-ref) clause of (LE-eq) and lies outside (LE-eq)'s setting; the cell marginal is (1, 0); independence is noted as immediate |
| N3 | G1: elementary bound D ≥ 1 − ⟨s_Σ\|Ω_Σ\|s_Σ⟩ ≥ 1 − λ_max, with equality 1 − Ω_Σ(s_Σ) for diagonal Ω_Σ |
| N4 | §7.3: full support stated for finite-range, finite-valued potentials |
| N5 | §8 (b): "under the posited P-ED" |
| N6 | T9: "the rule" refers to the §4.6 heading at M:748 |
| N7 | Every count in this file re-checked: 44 rows; 21 / 11 / 12 / 0 |
