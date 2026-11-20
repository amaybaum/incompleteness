# R1-L8 Stage 1(ii) — global canonical typicality replaced by a declared local-equilibrium condition

**Status.** Writer's paper-only audit, WIP / UNVERIFIED. Conditions, consumer list, decision rule
and controls were fixed in `PREREG.md` (commit `08f63c9d`, pushed before this file). Existing
evidence only: no new measure construction, no replacement law, no manuscript, Lean or registry
edit. The local-equilibrium conditions below are declared hypotheses; this audit derives none of
them and does not present any of them as derived. A1 (Main posit ledger item (ii)) remains open and
unadopted. Independent non-author review is required before any use.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7044998279](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7044998279),
2026-11-20T16:37:21Z, item 1. Goal link (§A.47): "Stage 1(ii) bears on removing A1 (the R1/R5
residue)."

**Source pin.** `main` at `800cfec6655aa5e9efaf39d6c7823bf2f40795e2`; site and record abbreviations
as PREREG. [W] marks the writer's own elementary reasoning; everything else is cited.

## 1. Verdict (generated from the table in §3)

26 rows (21 preregistered consumers; T11, T17 and T20 split into the separately worded claims they
contain, §10): **RETAINED 10** (T1, T4, T5, T10, T11d, T13, T17a, T19, T20a, T21); **RETAINED-WITH-(LE)
4** (T2, T3, T8, T9); **NOT FOLLOWING 12** (T6, T7, T11a, T11b, T11c, T12, T14, T15, T16, T17b,
T18, T20b); **UNDETERMINED 0**.

- **Retained.** The τ_B bound, the anti-Boltzmann-brain corollary, the rate-condition analysis and
  the time-symmetry statements do not use the typicality step and are unchanged (K1 passed).
- **Retained with (LE).** The thermal "in particular" clause (with (LE-T)), the proof's division of
  labour ((LE) supplies the state, (EM) the mixing), the scope list and the §4.6 opening, each with
  the condition named.
- **Not following.** Every statement worded about the global equilibrium macrostate or phase of
  (S, φ): the global-to-local step itself, "observers exist only in the non-equilibrium phase of
  (S, φ)" and its seven companion and book restatements, and the past-hypothesis replacement (Sub:56,
  Comp:212). The strongest weaker result that does follow is the region form W* (§6).
- **Structural finding G2 [W].** In the iterated description, the τ_B bound and the failure of
  (C2-slow) use only (EM) at a fast rate on the region; neither canonical typicality nor (LE) enters
  the proof. Local equilibrium does three other jobs: it labels the regions where the fast-(EM)
  posit is asserted as equilibrium regions, it supplies a temperature for the thermal reading, and
  (in its (LE-ref) part) it is the state link that the existing transfer gap (REMAINDER M18) needs.
- **(LE) is weaker as a premise but has no source.** It needs no total finiteness, no global law and
  no typical-set quantifier, and (LE-eq) is satisfiable on an infinite carrier at β = 0. No
  finite-temperature equilibrium family exists on `main` for the selected update, and nothing on
  `main` sources the link from the actual law to the equilibrium state (§5, §7).

## 2. The condition used

From PREREG §2, unchanged. On a configuration space Ω of any cardinality, with reference law μ of
(IL)/(EM), a declared family 𝓡 of bounded-diameter finite regions, the actual law ν (declared
preparation, conditioned on the declared macro-data), and a declared tolerance δ_LE:

> **(LE-eq)** For every Σ ∈ 𝓡: ‖ν|_Σ − ω_Σ‖_TV ≤ δ_LE, where ω_Σ = μ|_Σ is the Σ-marginal of a law
> in a declared equilibrium family 𝓔 (translation-invariant, update-invariant Gibbs/DLR states of a
> declared local interaction, β = 0 included), specified independently of the conclusion.
>
> **(LE-T)** (LE-eq) with 𝓔 at finite inverse temperature β = 1/(k_B T_local) > 0 for a declared
> real-valued conserved local energy of the update.
>
> **(LE-ref)**, used only in K3 and G2: ‖ν|_Σ − μ|_Σ‖_TV ≤ δ_LE for an arbitrary invariant μ.

These conditions are region-wise over 𝓡 and say nothing about regions outside D(𝓡), a global
macrostate, or a typical set. They are hypotheses to be declared, not results.

## 3. Per-consumer table

Q1: does the result use the typicality step (M:764's global-to-local inference, or [31])? Q2: is its
conclusion worded about a global macrostate or phase of (S, φ), or a typical set? (PREREG §4.)

| Id | Site | Result (quoted or paraphrased) | Q1 | Q2 | Verdict | Condition carried / why not / strongest weaker result |
|---|---|---|---|---|---|---|
| T1 | M:754–756, :760 | τ_B(V) ≤ τ_mix(Σ_loc(V)) + O(ε) for the iterated description | No: the decay step is "under (EM) its dissipative gap … bounds the decay … exponentially at rate 1/τ_mix" with the causal cone | — | **RETAINED** | Unchanged: (EM), bounded diameter, finite S or (IL). "Typical-set corrections" in ε name no proof step; ε is unquantified on `main` either way (REMAINDER M18; A1-05 :21) |
| T2 | M:758 | "if Σ_loc(V) is in its local equilibrium macrostate in the sense of canonical typicality [31], τ_B(V) is bounded by the local thermal decorrelation time" | Yes ([31]) | No: an "if" about one region | **RETAINED-WITH-(LE)** | (LE-T) on {Σ_loc(V)}: with μ|_Σ the Gibbs marginal at T_local, the correlations K_Σ controls are equilibrium correlations, so τ_mix is the local thermal decorrelation time [W]. Under (LE-eq) at β = 0 the bound holds but has no thermal scale |
| T3 | M:760 | "canonical typicality [31] supplies the local-equilibrium *state*, not the temporal mixing, which is exactly what (EM) posits" | Yes | No | **RETAINED-WITH-(LE)** | (LE-eq) supplies the state; (EM) is still needed separately; the two are logically independent (I1, §4) |
| T4 | M:762 | Anti-Boltzmann-brain corollary; (GT) illustration | No: local thermal equilibrium of Σ_BB is stipulated ("that is what 'fluctuation from equilibrium' means"); [31] not cited (STAGE0 M19.b; REMAINDER M20) | — | **RETAINED** | Unchanged: (EM), τ_mix(Σ_BB) ≪ τ_S, uniform erosion; the (GT) illustration adds T_local. The stipulation is an instance of (LE-T) on {Σ_BB}; naming it changes nothing |
| T5 | M:764 to "remains open." | The theorem and (C2-slow) do not compose without τ_mix ≪ τ_S; "a sufficiently fast-mixing equilibrium supports no observer satisfying … (C2-slow)"; dS thermal scale | No | — | **RETAINED** | Unchanged. "Equilibrium" here is a region's stipulated state |
| T6 | M:764 | "For (S, φ) in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its local equilibrium" | Yes | Yes | **NOT FOLLOWING** | It is the replaced step: (LE) asserts local equilibrium only on declared regions and implies nothing from a global macrostate. Weaker results and recovery: §8 |
| T7 | M:764, remainder | "No bounded-diameter partition supports (C2-slow) in that description … observers therefore exist only in the non-equilibrium phase of (S, φ)"; C1–C4 "not satisfiable in the coarse-grained description of the equilibrium phase" | Yes (via T6) | Yes | **NOT FOLLOWING** as worded | W* (§6): no V with Σ_loc(V) ∈ 𝓡 supports (C2-slow), under (EM) fast on 𝓡; D(𝓡) is labelled the equilibrium domain by (LE-eq). Its relation to a global equilibrium phase is not established |
| T8 | M:766 | Inputs include "the canonical-typicality result [31]"; "the canonical-typicality clause" is a finite-representative statement | Yes | No | **RETAINED-WITH-(LE)** | Input list with (LE-eq)/(LE-T) in place of [31]. The finite-representative restriction belonged to [31]'s finite shell; (LE-eq) is stated on region marginals and is satisfiable on an infinite carrier (§7). O(ε) and exact recurrence stay finite-representative |
| T9 | M:750 | Selection rule "on where in a finite bijective (S, φ) observers can exist … conditional on (EM) … and on the rate condition" | Yes (the rule is T5–T7) | No: "where … observers can exist" is met by W* | **RETAINED-WITH-(LE)** | Conditions: (EM), rate condition, (LE-eq). Observation O1 (§4): the printed list omits the typicality step that M:764 uses and M:766 lists |
| T10 | M:171 | The erasure lemma bounds the readback left by fast mixing "in the exclusion arguments below — the equilibrium phase, and the anti-Boltzmann-brain corollary" | No | — | **RETAINED** | The remark's content is the erasure lemma; its pointer to "the equilibrium phase" inherits T7 |
| T11a | Sub:56 | "τ_B(V) is bounded by the local mixing time on equilibrium microstates, so C2 fails there in its timescale form" | Yes | Yes ("equilibrium microstates") | **NOT FOLLOWING** as worded | W* on 𝓡 |
| T11b | Sub:56 | Observers "structurally restricted to the non-equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W* |
| T11c | Sub:56 | "this replaces the low-entropy 'past hypothesis', in its role of selecting observer-compatible configurations, with a structural observer-selection rule" | Yes | Yes (global configurations) | **NOT FOLLOWING** | W* selects regions, not global configurations: whether a configuration of a globally equilibrated (S, φ) has every observer-relevant region in (LE) is the dropped step. Sub:56 already records the infinite-carrier form as open; under (LE) the replacement does not follow on a finite carrier either |
| T11d | Sub:56 | "excludes Boltzmann brains structurally rather than anthropically"; "The rule is time-symmetric" | No (T4; T13) | — | **RETAINED** | As T4. Sub:56 attributes the BB exclusion to the phase restriction; T4 supplies it without that restriction |
| T12 | Sub:401 | "The observer's confinement to the non-equilibrium phase of (S, φ) … is a structural consequence of the effective-mixing hypothesis" | Yes | Yes | **NOT FOLLOWING** as worded | W*. As O1, the attribution to (EM) alone omits the typicality step |
| T13 | Sub:409 | The spectral-gap bound "applies equally in both directions" | No | — | **RETAINED** | Unchanged (K1) |
| T14 | Sub:542 | "the *equilibrium phase* of (S, φ) is … observer-free for sufficiently fast-mixing equilibria" | Yes | Yes | **NOT FOLLOWING** as worded | W*: D(𝓡), with (EM) fast, is free of (C2-slow) observers in the iterated description |
| T15 | Str:718 | "substrata in perpetual equilibrium cannot satisfy C2's slow-bath route" | Yes | Yes | **NOT FOLLOWING** as worded | W* with 𝓡 the observer-relevant regions at every time. The first sentence of Str:718 (phases with mixing faster than recurrence) does not use the step and is not classified |
| T16 | Str:734 | "non-equilibrium-phase … features required for C1–C4" | Yes (via T7) | Yes | **NOT FOLLOWING** as worded | W* gives a necessary condition on the observer's region (not in 𝓡 with fast (EM)), not on a global phase. The claim that random permutations "typically lack" these features is a separate claim, not traced here |
| T17a | Comp:212 | Boltzmann brains have τ_B bounded by local thermal decorrelation; "not observers in the sense of C1–C4 with C2 read in its timescale form" | No (T4) | — | **RETAINED** | As T4, with its (GT) estimate |
| T17b | Comp:212 | Observers "cannot exist in the equilibrium phase of (S, φ)"; τ_B bounded "on equilibrium microstates"; past hypothesis "replaced … by the same theorem" | Yes | Yes | **NOT FOLLOWING** as worded | W*; past-hypothesis replacement as T11c |
| T18 | ch02:192 = FULL:822 | The theorem "restricts observers … to the non-equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W* |
| T19 | ch03:58 = FULL:919 | Conditional Boltzmann-brain exclusion for bounded-diameter partitions under effective mixing and τ_mix ≪ τ_S | No | — | **RETAINED** | Unchanged |
| T20a | ch04:178 = FULL:1282 | "bounded-diameter partitions fail C2-slow" under effective mixing and τ_mix ≪ τ_S; suppression under uniform erosion | No | — | **RETAINED** | Unchanged |
| T20b | ch04:178 = FULL:1282 | The heading attributes T20a to "The equilibrium phase of (S, φ)" | Yes | Yes | **NOT FOLLOWING** as worded | W* |
| T21 | LEDGER :1367, :1381, :1395; `verification/lean*/` | Kernel status of the theorem and both corollaries | No kernel statement | — | **RETAINED** | All three entries are kernel `GAP`, "not formalized". No Lean module states a §4.6 result; `OIBridge/ThermalOrientation.lean` uses Boltzmann ratios for orientation, not typicality |

## 4. Findings

**G1 [W] — the typicality step and OI's microstates.** [31] concerns pure states ψ drawn from the
normalized unitarily invariant measure on a shell subspace: for most such ψ the reduced state of a
fixed subsystem is close to the shell's marginal. An OI microstate is a configuration. In the
fixed-basis representation it is a basis vector |s⟩ = |s_Σ⟩ ⊗ |s_rest⟩, under the site
factorization (M:732, posit (viii)), and its reduced state on Σ is the pure |s_Σ⟩⟨s_Σ|. The trace distance
from a pure state to the shell marginal Ω_Σ is at least 1 − √λ_max(Ω_Σ) (Fuchs–van de Graaf), which
is close to 1 whenever Ω_Σ is spread over many configurations. Configuration microstates therefore
lie outside the typical set. The step can be read in only two ways. For superposition states it is
not a statement about OI's microstates. For an ensemble (the uniform law on the shell) its
conclusion is the exact marginal of that law, which needs no typicality and is the selected
counting law, class (c) in STAGE0 M19.a. This sharpens MAIN-ROOTS :95, which notes that [31] does
not "guarantee the desired marginal for every microstate and every cut". It also supports stating
(LE) for laws (PREREG §2) and not for single configurations: the configuration on one region is a
point, so it has no local-equilibrium content of its own. A classical substratum analogue exists
only as a spatial average (§8).

**G2 [W] — what local equilibrium does in the §4.6 chain.** In the iterated description the
operator K_Σ = P_Σ U P_Σ is fixed by the reference law μ, and the bound of T1 is a property of K_Σ
under (EM). It does not refer to the region's actual state. The failure of (C2-slow) (T5, T7) follows
from that bound and τ_mix ≪ τ_S for the region. The global corollary's own chain (M:764) is: global
equilibrium ⇒ (T6) every region in local equilibrium ⇒ (posit: "That every relevant equilibrium
region satisfies (EM) at the required rate is itself a physical hypothesis") fast (EM) on every
region ⇒ (T1) no (C2-slow). Local equilibrium therefore enters only

(i) as the label of the regions on which the fast-(EM) posit is asserted;
(ii) for the thermal reading of τ_mix and (GT) ((LE-T));
(iii) as the link between the actual law and the reference law, ‖ν|_Σ − μ|_Σ‖ ≤ δ_LE, which the
transfer from the iterated description to actual record laws requires. That transfer is the existing
A1-independent gap of REMAINDER M18 and A1-05 P8-M ("relation of P_Σ U^n P_Σ to K^n", "comparison to
actual history-conditioned observables").

Consequence: replacing the typicality step by (LE) changes no proof step of the bound or of the
(C2-slow) failure. It changes only the set of regions to which the conclusion is attached, from
"every region of an equilibrium (S, φ)" to the declared D(𝓡). Pressure test of this favourable
reading: the physical exclusion, as distinct from the statement in the iterated description, needs
(iii). Nothing on `main` sources (iii), so the observer-selection rule's physical reach is not
improved; the need is relocated from typicality to the actual-state link, which was already open.

**I1 [W] — (LE) and (EM) are logically independent.** (LE) without (EM): take φ = id on
Ω = A^{Z^d} with μ = ν = β_A. β_A is the zero-interaction DLR state, translation invariant and
invariant under the identity, so (LE-eq) holds with δ_LE = 0 on every region. But U is the identity,
so K_Σ = P_Σ: centred local observables do not decay and (EM) fails. (EM) without (LE): (EM) is a property of (φ, μ, P_Σ) and does not involve ν, whereas (LE) does. Main's
own example (M:766), four states with cells {0,1}, {2,3}, φ = the transposition (0 2) and μ uniform, gives K_Σ with eigenvalues 1 and 0, so centred observables
are annihilated in one step: (EM) holds. With ν = δ_0 the cell marginal is δ_{0,1} against (½, ½), at TV
distance ½, so (LE) fails for δ_LE < ½. Hence (EM) is still needed separately, as M:760 states for
canonical typicality.

**O1 — dropped quantifier (observation, for a separate correction unit).** M:764 states that [31]
"implies every local subsystem is also in its local equilibrium". [31] gives this for typical ψ and
for a fixed subsystem; the typical-state quantifier, and with it the measure, is not carried into
the corollary's conclusion. M:750 ("conditional on (EM) … and on the rate condition") and Sub:401
("a structural consequence of the effective-mixing hypothesis") omit the step that M:766 lists. This
audit edits nothing; under §A.25 any correction would be propagated in its own authorized unit.

## 5. What still needs physical sourcing

| Item | Needed by | Source on `main` |
|---|---|---|
| The equilibrium family 𝓔 and its states ω_Σ | (LE-eq), (LE-T); T2, T3, T8, T9, W* | **β = 0:** β_A, the zero-interaction DLR state (R1-INF Prop. 6 (a)), invariant under every injective CA (R1-INF Lemma 1 (c)). It is selected by P-ED, i.e. by the posited (G3) + (G4) (R1-INF Prop. 3), or by a declared law (H-μ). It is not derived (R1-INF §6.4). **β > 0:** none. (LE-T) needs a real-valued conserved local energy. SM:292 records that the exact linear rule conserves its quadratic energy only modulo q and that neither it nor the rounded rule supplies "the required real positive-definite conserved energy". R1-INF Prop. 6 leaves d ≥ 2 undetermined, and in d = 1, α² = 1 the conserved mover densities give a family with free parameters. A measured local temperature would enter as an explicit empirical input (class E), not a derivation |
| Reference compatibility μ|_Σ = ω_Σ | (LE-eq); G2 (iii) | None: A1-05 P8-M first stop, "No existing source in the trace selects the normalized invariant probability for the physical readout" |
| The actual-law link ‖ν|_Σ − ω_Σ‖ ≤ δ_LE (a preparation or relaxation account) | (LE-eq); transfer to actual records | None: A1-05 P8-S first stop, "no normalized equilibrium state for a specified encompassing region, selected by the physical update or preparation" |
| (EM) on each region, at τ_mix + O(ε) ≪ τ_S | T1–T9, W* | None: an explicit physical hypothesis (M:750–752), established "model by model" (M:766). Still needed separately (I1). On the infinite full product, β_A is mixing of all orders for the selected update with α a unit (R1-INF Prop. 5). That is exact-dynamics mixing without a rate; it is not (EM) for K_Σ |
| The posit that the regions of 𝓡 mix fast | T7 and its restatements | Posited (M:764) |
| Uniform erosion; O(ε); transfer of the τ_B bound | T4, T7, readback suppression | Existing A1-independent gaps (REMAINDER M18, M20; A1-05), carried unchanged |

## 6. What no longer follows, and the strongest weaker result

**What fails.** Each NOT FOLLOWING row asserts something about the global equilibrium macrostate or
phase of (S, φ). Under (LE) nothing connects that global property to the regions, because (LE)
replaces the connecting step without deriving it. Two groups:

- **The global-phase statements** (T6, T7, T11a–b, T12, T14, T15, T16, T17b, T18, T20b): "observers
  exist only in the non-equilibrium phase of (S, φ)" and its restatements.
- **The past-hypothesis replacement** (T11c, T17b): it selects observer-compatible global
  configurations, and that needs the global-to-local step.

**Strongest weaker result W\*** (follows under the stated hypotheses; it is not presented as
physically established). Let 𝓡 be a declared family of bounded-diameter regions. Assume:

- (EM) for K_{Σ_loc(V)}, for every V with Σ_loc(V) ∈ 𝓡, with τ_mix + O(ε) ≪ τ_S;
- finite S, or (IL) for the decay estimate, as M:766 states.

Then, in the coarse-grained description generated by iterating K_{Σ_loc(V)}, no such V supports
(C2-slow). Under uniform erosion, its order-k readback gap is bounded by δ_0 e^{−(k−1)τ_S/τ_B} for
k ≥ 2. With (LE-eq) on 𝓡, D(𝓡) is a domain of local equilibrium, and the statement reads: (C2-slow)
observers occur only outside the fast-mixing local-equilibrium domain. With (LE-T), τ_mix is a
thermal decorrelation time. By G2, W* holds with fast (EM) on 𝓡 alone, and (LE) only labels the
domain. W* says nothing about a global phase, about which global configurations host observers, or
about regions outside D(𝓡).

For the anti-Boltzmann-brain corollary nothing is lost: its neighbourhood equilibrium was always
stipulated (T4). The corollary still covers only fluctuations inside a neighbourhood stipulated to
be in local equilibrium; that scope is unchanged and not addressed here.

## 7. Is (LE) weaker than A1 + canonical typicality? (PREREG §5 item 4)

1. **Logical comparison [W].** A1 with the selected spherical shell measure, bath size and weak
   coupling gives, by [31], the region condition for typical superposition states, per subsystem,
   with δ_LE set by [31]'s bound. On that typical set the route implies (LE) in the
   quantum-representation reading (PREREG §2). (LE) implies neither A1 (item 2) nor any global
   macrostate or law selection. As a premise it is therefore weaker: it drops total finiteness, the
   shell, the spherical measure and the typical-set quantifier. It is not inherited from that route
   by OI's configuration microstates (G1). At the level of laws the A1 route reaches (LE) only
   through a selected law (class (c)), not through typicality. At β = 0 the torus counting law μ_L has
   uniform marginals on boxes smaller than the torus (R1-INF Lemma 1 (b)), which are β_A's. For an
   energy shell, its marginal approximates a Gibbs marginal only through equivalence of ensembles,
   which needs a real conserved energy that `main` lacks for the selected update (§5).
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
   - **(LE-eq) excludes m_H**, on every region containing its special site. m_H is not translation
     invariant (Prop. 9 (b)), so it is not admissible as a reference in 𝓔. As an actual law it has TV
     distance at least 1 − ω_0((0,0)) from ω_Σ, where ω_0 is the one-site marginal of the reference.
     That is 1 − q^{−2} at β = 0, and positive for any finite-range Gibbs state, whose single-site
     marginals have full support [W]. So it is excluded whenever δ_LE is below that distance.
   - **Regions avoiding the special site:** not determined here (flagged). The exclusion is carried by
     the translation invariance required of 𝓔. This is the homogeneity premise (G3), which STAGE0 F3
     and R1-INF §6.1 identify as load-bearing. (LE) does not remove the homogeneity question; it moves
     it into the declared choice of 𝓔.
4. **Observational checkability.** Σ_loc(V) contains hidden sites, so (LE) is not directly verifiable.
   Its visible consequences are checkable in principle: the visible marginal of ω_Σ on V's labels,
   stationarity of visible statistics and, for (LE-T), consistency with a measured local temperature.
   A mismatch above δ_LE in any of these falsifies the declared instance. The global-to-local
   inference it replaces has no observable content of its own (REMAINDER M19). So (LE) is falsifiable
   through its visible consequences but not verifiable on the hidden part.

## 8. Theorem-recovery note (Code Review Rules; one shared gap)

All twelve NOT FOLLOWING rows fail at one link, the global-to-local step T6. One note covers them;
the past-hypothesis rows add one further gap.

- **Strongest existing results.**
  - (a) *Finite representative.* The imported theorem [31]: per subsystem, for typical ψ under the
    spherical measure on a finite-dimensional shell, with bath size and weak coupling for the
    canonical form. Hypotheses: A1, the shell, the selected measure (STAGE0 M19.a, class (c)), and the
    caveats G1 and O1.
  - (b) *Infinite full product, β = 0, under P-ED.* If the global law is β_A, every finite region is
    in (LE-eq) with δ_LE = 0 [W, product form]. For β_A-almost every configuration, spatial
    frequencies of patterns converge to the uniform marginals (R1-INF :389, "spatial frequencies by
    the strong law"). Hypotheses: the injective-CA class and the posited (G3) + (G4).
  - (c) *Counterexample without (G3).* m_H shows that "update-invariant with maximal centred entropy
    density" does not imply equilibrium local marginals in d ≥ 2 (R1-INF Prop. 9 (b); STAGE0 F3).
    A version of L8 with that premise is false.
- **Proposed repair: L8** (REMAINDER :163, "Local-equilibrium marginals of a supplied invariant law
  on an infinite carrier"). Decomposition [W]:
  - **L8-sel.** At the level of laws, the step is immediate once the global law is declared in 𝓔:
    ω_Σ is by definition its marginal (item (b)). The content is the selection of that law: R1, open.
    It is restored at β = 0 by P-ED with (G3) (R1-INF Prop. 3), and blocked without (G3) by (c).
  - **L8-typ.** At the level of configurations, a single region carries no equilibrium content (G1).
    The meaningful form is a spatial-average statement for typical configurations of an ergodic
    translation-invariant law in 𝓔. At β = 0 it holds by the strong law (item (b)).
- **What the attempt checked.** Items (a)–(c) were read at their sources. The decomposition and the
  β = 0 marginal statement are [W] and elementary. No new law was constructed.
- **Remaining gap.**
  - A finite-temperature family 𝓔 for the selected update (a real conserved local energy; SM:292;
    R1-INF Prop. 6).
  - Selection of the global law in 𝓔 without (G3), or a physical source for (G3).
  - The link from the actual law to that law (§5).
  - A decision whether the global-phase statements are meant at the level of laws or of spatial
    averages. Per-region statements about single configurations are not available (G1).
  - For T11c and T17b in addition: the infinite-carrier low-entropy inflow that Sub:56 itself records
    as open (REMAINDER O-INFLOW).
- **Status.** Failure to recover the global-to-local step is not a disproof. The global-phase
  statements remain established on the finite representative within (a)'s scope and class (c), and
  are open beyond it. This unit edits no manuscript text. Any narrowing would need its own
  authorized unit.

## 9. Controls (PREREG §6)

| Id | Result |
|---|---|
| K1 | T1, T4 and T13 are RETAINED. Passed |
| K2 | T6 is NOT FOLLOWING. Passed |
| K3 | (LE-ref) admits m_H (flagged). (LE-eq) and (LE-T) exclude it on regions containing its special site whenever δ_LE < 1 − ω_0((0,0)) (1 − q^{−2} at β = 0). Regions avoiding the site are flagged as not determined (§7.3). Passed: each condition either excludes m_H or is flagged |
| K4 | Every row using (LE-eq) or (LE-T) names it as a hypothesis. The occurrences of "derive", "follows", "implies" and "holds" near "(LE" were read. Each states either that (LE) is not derived, or a conditional ("under (LE) …", "(LE) implies neither …"), or the [W] fact that the β = 0 marginal holds for the declared β_A. Passed |
| K5 | GR Thm A.8 (GR:801–867), ch07:126–151, ch18:140 and ch18:200 = FULL:4931 contain no citation of Main §4.6 or [31]'s §4.6 use. Passed |
| K6 | The diff touches only this directory. Passed (checked at commit) |

## 10. Deviations from PREREG

- **D1.** T11, T17 and T20 each contain separately worded claims that the rule classifies
  differently. They are split into sub-rows (T11a–d, T17a–b, T20a–b), and each sub-row is classified
  by the unchanged rule. Without the split, each would be NOT FOLLOWING as a whole, which would hide
  that the Boltzmann-brain parts (T11d, T17a) and ch04's partition sentence (T20a) are retained.
- **D2.** T15's first sentence does not use the step and is left unclassified (noted in the row).

No other deviation. No new consumer was found by the trace beyond the preregistered list.

## 11. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7044998279 | Authorization and scope | Provenance; quoted with author and time |
| #1456, #1457 | Stage 0 and Stage 1(i), whose records are on `main` | Provenance; STAGE0 is cited from its file on `main` at the pin |
| R1-INF's credit to #1431 comment 7025214238 for Prop. 9's argument | Inside a cited record | Provenance; the proof is written out on `main` (R1-INF :280–320) |
| [31] (arXiv:cond-mat/0511091) | G1, §7, §8 | External published theorem, cited as Main does |

## 12. What an independent reviewer must check

1. Each Q1/Q2 answer in §3 against the quoted site, in particular:
   - T2 and T9 (Q2 = no);
   - T11a and T17b ("equilibrium microstates" read as global);
   - T20a/T20b (the split);
   - T4 (local equilibrium stipulated, not via [31]).
2. G1: that configuration microstates are basis vectors with pure reduced states, the trace-distance
   bound, and that the ensemble reading reduces to the selected law's marginal.
3. G2: that the T1 bound and the (C2-slow) failure use no state beyond the reference law of K_Σ, and
   that (LE)'s three roles are exhaustive. In particular, that the transfer gap (iii) is the existing
   M18/A1-05 gap and not a new one.
4. I1: that K_Σ = P_Σ for φ = id under β_A, and Main's four-state transposition example with ν = δ_0.
5. §5: SM:292's statement, R1-INF Prop. 6's scope, and that no finite-temperature family 𝓔 exists on
   `main` for the selected update.
6. §7.3: m_H's origin marginal δ_{(0,0)} (u(0) = x_0(0), v(0) = x_{−1}(0) ∈ Γ), the TV values, the
   full-support claim for finite-range Gibbs single-site marginals, and the flag for regions avoiding
   the site.
7. §8: the L8-sel/L8-typ decomposition, and that no item is presented as a derivation of (LE).
8. That no row reports mathematical sufficiency as physical justification, that (LE) is nowhere
   presented as derived (K4), and that no manuscript, Lean or registry file changed (K6).
9. O1, as a candidate for a separate correction unit only.
