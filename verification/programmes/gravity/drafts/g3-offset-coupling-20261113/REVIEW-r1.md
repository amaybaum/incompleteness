# REVIEW-r1: G3 unit 1 (r1), offset coupling and the covariant source

**Verdict: REVISE.**

The explicit pair K_dec/K_cpl is algebraically correct. Both completions are natural and conserved, and they coincide at r₀. As a statement about source maps, the non-implication from the operational data (K1–K14, channels) holds.

Two blocking defects remain:

- **B-1.** The verdict "counterexample to implication from OI's existing results" does not check an OI datum the corpus presents as forced: requirement (ii) of the geometry-first ordering (GR:346, "forced" at GR:342, "not a stipulation but a structural consequence" at book/ch07-gravity.md:187). The draft dismisses it on a scope ground (GR:350) that does not apply to a uniform term.
- **B-2.** Route R2 and the proposed next obligation O1 rest on the claim that ℱ = ¼T is an admissible, shift-equivariant trace sector. That holds only for a trace-free left side. With the divergence-free left side that GR:12's "Bianchi structure" names, it violates conservation.

Both can be fixed on paper, and the verdict category may survive. Neither fix can be skipped.

**Target.** Branch `research/g3-offset-873-20261113` at `e64b9a3c219c8f2676885964b26c29dd78d83c6b`, a single commit on `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`. It adds only `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/G3-UNIT1-r1.md` (460 lines) and `NOTES-r1.md` (149 lines). Every corpus `file:line` below refers to `c3b5f37a`, which is byte-identical to the target for `papers/`, `book/` and `verification/lean*`. "UNIT1:n" means G3-UNIT1-r1.md line n, and "NOTES:n" means NOTES-r1.md line n.

**Authority checked.** I read both comments through the REST API:

- #873 c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z), the planning record, items 1–5;
- c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z), unit 1 authorized paper-only with Claude as writer, followed by an independent non-author review.

The draft stays inside that scope. It changes no manuscript and builds no Lean, adopts no premise and makes no Λ-magnitude claim.

**Checks run** (all at the target head, all passing):

| Check | Result |
|---|---|
| `tools/claims_check.py` | OK |
| `tools/staleness_check.py` | OK, 13 matched |
| `tools/voice_check.py` | OK, 40 files |
| `tools/artifact_placement_check.py` | OK, self-test passed |
| `tools/legacy_records_check.py e64b9a3c…` | 303 records intact, self-test OK |

NOTES:115–117 records that these checks were not run. They now have been, and they pass. They do not scan the drafts.

***

## Findings

### B-1 (blocking): requirement (ii) of the geometry-first ordering is an omitted OI datum, and B2(a)'s dismissal is wrong for the uniform term

**Where.** UNIT1:308–309 (B2(a)), UNIT1:256–266 (the §3.2 table), UNIT1:35–36 and :270–271 (the shared-data claim).

**Evidence.**

- GR:342 says the geometry-first ordering "is forced by the logical structure of the derivation through three independent requirements". GR:346, (ii) Non-circularity, reads: "If the metric were derived from QM, then the derivation would require: QM → metric → causal structure → partition → QM — a circular dependency with no entry point. The circle breaks only if the metric exists prior to the partition." The book mirror calls the ordering "not a stipulation but a structural consequence" (book/ch07-gravity.md:183, :187).
- K_cpl's source contains ρ(r) = ħ·tr(ρΩ_r)/v. Here Ω_r is the reconstructed visible generator and ρ is the emergent state, and both exist only after the partition is drawn. Under K_cpl the de Sitter radius, and with it the horizon that defines the partition (GR:40, GR:346), therefore depends on post-partition emergent data. The draft's own §3.3 (UNIT1:277–279) shows that a uniform term moves H² by 8πGρ/3 and so moves the partition. On its face, that is the QM → metric → partition loop that (ii) excludes.
- B2(a) answers that "(i)–(iii) fix the metric at the partition boundary only" and cites GR:350's three laboratory completions. That scope limit concerns laboratory near fields. A uniform term acts on the cosmological horizon, which *is* the partition boundary. So the scope argument does not remove (ii) from the uniform-offset question. It points the other way.
- The §3.2 table lists substratum, partition, reduced law, fixed-basis class, calibration, channels and K10–K14. It has no row for the ordering requirements (i)–(iii), although these are the OI statements most directly about what may source the boundary metric.

**Why it matters.** If (ii) is read as the corpus states it, a boundary metric that depends on the emergent representative is excluded. That would give (SI) for the uniform term, and the verdict would become "conditional on (ii)" or even "derived". If (ii) is read more weakly, as a statement about derivation order that does not exclude self-consistent fixed points, K_cpl survives. In that case the draft must say so and give the reason. The corpus supplies one: GR:358 states that "the emergent quantum description does feed back into gravitational dynamics through state-level quantities" (the §7.1 running-vacuum bookkeeping, "the emergent vacuum energy depending on H"). So the corpus itself does not read (ii) as forbidding every emergent input to the cosmological metric. Either way, the verdict as written rests on an unchecked datum.

A secondary point: (iii) (GR:348) does not exclude K_cpl. ħ = τ_K/β_E is independent of κ (GR:751), so an H that depends on the state leaves ħ state-independent. The draft should record this too.

**Fix.**

1. Add a §3.4 node, "B5. The ordering requirements (i)–(iii) exclude a boundary metric that depends on the emergent offset". Check each requirement against K_cpl:
   - (i) is satisfied, because ρ(r) is a definite real number;
   - (iii) is satisfied, by GR:751;
   - for (ii), state the strongest reading and the weakest reading, show which one excludes K_cpl, give the support class of GR:342–346 (a paper argument, not kernel-checked), and cite GR:358's admitted emergent→metric feedback as evidence of the reading the corpus actually uses.
2. Replace B2(a) with: "Requirements (i)–(iii) concern the metric at the partition boundary. For a uniform term that is the cosmological horizon itself, so the GR:350 laboratory scope does not apply; see B5."
3. Add a row to §3.2: "Ordering requirements (i)–(iii) (GR:342–348) | shared at r₀; whether (ii) excludes K_cpl's counterfactual dependence is B5's verdict."
4. Make §0 depend on B5:
   - if B5 finds that (ii) as the corpus uses it does not exclude K_cpl, keep "counterexample" and name (ii)'s strong reading among the routes that would yield (SI), as R0;
   - if B5 finds that it does, change the verdict to "conditional on requirement (ii), read as …".

### B-2 (blocking): R2 and O1 misstate the admissible shift-equivariant trace sector

**Where.** UNIT1:378–386 (R2), UNIT1:397–407 (O1), UNIT1:422 (F6).

**Evidence.**

- GR:12 states the target as E_μν[g, OI] = 8πG(T_μν − ℱ[g,T] g_μν). G3 is "covariant field equations with conservation/Bianchi structure", and under this form "the distinct-descriptions argument becomes a theorem of the dynamics".
- The shift condition ℱ[g, T−ρg] = ℱ[g,T] − ρ is correctly derived at UNIT1:379–380. ℱ = ¼g^{μν}T_μν + c satisfies it, since g^{μν}g_μν = 4. That much is correct.
- Admissibility is where it fails. If E_μν is identically divergence-free (G_μν, the "Bianchi structure" GR:12 names) and ∇^μT_μν = 0, the equation requires ∂_ν ℱ = 0 on solutions. ℱ = ¼T is then constant only when the trace of T is constant, so for generic matter it violates conservation. The draft's own (Adm2) (UNIT1:145) excludes it.
- The trace-free/unimodular reading UNIT1:381–384 invokes needs a trace-free left side, E_μν = R_μν − ¼Rg_μν. In that case:
  - the trace of the equation forces c = 0;
  - Bianchi gives ∂(R + 8πG T) = 0, which is where the integration constant Λ comes from.
  
  That left side is not divergence-free, and its source T − ¼Tg is not conserved. It therefore lies outside the completion class of §2, "G[g] + Λg = 8πG𝒮" with conserved 𝒮. The draft uses one class for the countermodel and a different class for R2 without saying so.
- With a divergence-free E_μν, the shift-equivariant and conserved choices of ℱ are spacetime constants, for example a spacetime average ℱ = ¼⟨g^{μν}T_μν⟩. That is the structure of sequestering [L, recalled: Kaloper–Padilla 2014, Λ = ¼⟨T⟩]. In this formalism R2 and R3 are therefore the same route, not two separate ones.
- The corpus already contains the trace-free structure on its own conditional field-equation route, and the draft does not connect it. Jacobson's argument as the corpus uses it (SM:160, input (iii): "the energy flux δQ = ∫T_μν k^μ dΣ^ν" with null k) constrains only the null–null components. Those are blind to −ρg, and Λ enters as an integration constant (SM:162 displays a free Λ). The draft uses this blindness in its own §3.2 calibration row (UNIT1:264) but not in R2 or O1. On that route the offset question becomes a different one: is the integration constant fixed by classical data κ (the metric is substratum data, GR:340)? A solution-level version of (SI) would then hold at fixed κ. The source-map version of (SI) is not the right object for it.

**Fix.**

1. Rewrite R2 as follows:

   > "With a trace-free left side (E_μν = R_μν − ¼Rg_μν), ℱ = ¼g^{μν}T_μν, and the trace equation forces the additive constant to vanish. Bianchi and conservation then return Λ as an integration constant. This is outside the §2 class, whose left side is divergence-free and whose source is conserved. With a divergence-free left side, (Adm2) requires ∂ℱ = 0 on solutions, so a shift-equivariant ℱ must be a spacetime constant such as ¼⟨T⟩ [L, recalled: sequestering]. The corpus's conditional Jacobson route (SM:160–162) has the trace-free structure: its null-flux input does not see −ρg."
   
   Keep "ℱ = const does not satisfy the condition", which is correct.
2. Merge R3 into R2, or cross-reference them.
3. Add a solution-level variant of the target, (SI′): for every κ and C, the solution set {g} for (κ, σ_C r) equals the solution set for (κ, r). State that in an integration-constant theory (SI′) is the meaningful form. Whether it holds then depends on whether the constant is fixed by κ alone.
4. Restate O1 as:

   > "Decide whether OI's premises force the G3 equation's dependence on T, with its Λ-sector, to be invariant under T ↦ T − ρg for constant ρ on its solution set, with conservation carried. Known admissible realizations are (a) a trace-free left side with Λ an integration constant fixed by classical data, and (b) a divergence-free left side with ℱ a spacetime-global functional. A non-equivariant admissible completion compatible with every OI premise is a G3-level countermodel."
5. Note in F6 or §5 that GR:12's sentence "under which the distinct-descriptions argument becomes a theorem of the dynamics" holds only for an equivariant (E, ℱ) pair. The printed target form does not supply that pair, so the sentence is conditional on it. Record this as an assumption-watch on GR:12, with no manuscript change in this unit.

### S-1 (should-fix): "differ only in how the source responds to the shift" is false for the chosen e(r)

**Where.** UNIT1:36, UNIT1:268; NOTES:103–105.

**Evidence.** The draft defines e(r) = tr(ρΩ_r), which depends on the emergent state ρ. K_cpl's effective Λ therefore moves under any change of ρ at fixed (V, E), for example an excitation or a preparation, and also under changes of the gaps. K_dec does not move under either. So the two completions differ in more than their response to the shift. In addition, by GR:573 relative energy differences are already in T^cl, so K_cpl counts them twice, once with a vacuum equation of state. NOTES:104–105 says the alternatives "behave the same way". That holds for the shift only, not for these other variations.

**Fix.** Use e(r) = min_a E_a, the ground eigenvalue (the zero-point offset), which does not depend on the state. Alternatively, keep tr(ρΩ_r) and replace "differ only in" with "differ in". If you keep it, add: "With e = tr(ρΩ_r), K_cpl also responds to changes of the emergent state and of the gaps. The non-implication needs only the shift response." Correct NOTES:104–105 to match.

### S-2 (should-fix): the "every further datum" claim generalizes from a finite list

**Where.** UNIT1:32–33, UNIT1:270–271, F3 at UNIT1:419.

**Evidence.** The support is K1, K6, K7, K10–K14 and the Ad argument: a finite list of structures, each of which reads only gaps, channels or energy order. The corpus also derives absolute, representative-dependent quantities from the emergent description:

- ρ_QFT from ½ħω per mode (GR:336, GR:332);
- the emergent "zero-point energy … the ground-state eigenvalue of Ĥ_eff" (GR:358);
- the emergent vacuum energy of the §7.1 running-vacuum reading (GR:358, GR:374).

These are not shift-invariant. They are exactly what K_cpl couples to.

**Fix.** Narrow UNIT1:32 and F3 to: "every datum the corpus derives from the operational content of the emergent generator (transition probabilities, channels, gaps, and the thermal, passivity and stationarity structures K10–K14)". Add one sentence noting that the corpus's absolute emergent quantities (GR:332–336, :358) depend on the representative, and that a coupled completion reads them.

### S-3 (should-fix): §3.3's justification for relabelling T^cl

**Where.** UNIT1:284–286.

**Evidence.** GR:340 defines T^cl as "the classical stress-energy of the total microstate". With a shared substratum, T^cl is a function of the shared microstate even though no explicit map is on `main`. The absence of a map therefore does not permit two values. What does permit relabelling a uniform part of T^cl is the classical-origin freedom the draft establishes itself in B2(c) (UNIT1:311–314; GR:58 "by the choice of energy zero"). Separately, the third reading, ρ_C = 0, makes the two completions identical, so the claim at GR:352 loses its content under it.

**Fix.**

- Replace "which the corpus permits because it supplies no map from the substratum to `T^cl`" with "which the classical-origin freedom of B2(c) permits: a uniform part of `T^cl` is fixed only by the convention of GR:58".
- After "`ρ_C = 0`" add: "under which the pair coincides and the claim is empty. Only the first two readings preserve the content of GR:352."

### S-4 (should-fix): the off-shell character of the countermodel is not stated

**Where.** UNIT1:249–254, B1 at UNIT1:300–301.

**Evidence.** (SI) is a property of the map 𝒮 at a fixed g, which is fine. On shell, however:

- κ contains the partition, and per GR:340 the metric as substratum data;
- under K_cpl, σ_C r₀ at fixed κ no longer solves the field equation for that g.

K_cpl's field equation together with κ therefore *selects* the representative: in K_cpl the origin is a physical quantity fixed by gravity. At r₀ the two completions' worlds are identical in every observable. Their difference is counterfactual: whether the origin is physical, which carries the fine-tuning reading of GR:352. B1 says that K_cpl needs a representative "physically selected, by any structure outside the OI data listed". In fact K_cpl selects it itself, given the metric.

**Fix.** After UNIT1:254, add:

> "On shell, with the metric and partition in κ (GR:340, GR:346), K_cpl's field equation fixes e(r), so it fixes the origin. K_dec leaves the origin free. At r₀ the two give identical worlds. What OI's data do not decide is whether the origin is a physical quantity, and with it whether the observed Λ_eff is the sum Λ₁ + 8πGρ(r₀)."

Amend B1 to match.

### S-5 (should-fix): the per-cell-constant stress tensor is labelled [A] but assumes a covariant vacuum equation of state

**Where.** UNIT1:313–314.

**Evidence.** The statement "A per-cell constant moves T^cl by −(b/ε³) g" assigns pressure −b/ε³ to a lattice energy constant. On a lattice with a preferred foliation (H-frame, GR:88), a per-cell constant fixes an energy density. Its pressure, and so its tensor form, depends on the continuum limit and on Lorentz invariance, and both are open (GR:12, GR:697(ii)).

**Fix.** Relabel it: "[A], conditional on a covariant continuum limit in which a uniform per-cell energy has vacuum stress −(b/ε³)g (open: GR:12, GR:697(ii))."

### S-6 (should-fix): F4 is classed NEW without checking GR:579 and AUDIT item 2.9

**Where.** F4 at UNIT1:420; NOTES:62–66, :147.

**Evidence.**

- GR:579, last sentence: "How the energy released in the electroweak and QCD transitions couples to gravity is not fixed by the relative/absolute distinction and requires the same open coupling step."
- `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md:55` (item 2.9): the relative/absolute rule "does not decide a transition between two configurations".

So the corpus already records that changes in absolute level caused by physical processes are not decided by the rule. F4 adds a concrete mechanism: the scalar part of the bath-averaged coupling Tr_H[V_int(1⊗ρ_H)] (Main:340) shifts Ĥ_eff invisibly under a change of hidden state. It also sharpens the target into (SI) at fixed κ. That is useful, but it elaborates a recorded point rather than exposing a blind spot that was never characterized.

My algebra check is consistent with the draft's: the scalar drops out of −i[Ĥ_eff,·] and out of each U_h ρ U_h†.

**Fix.** Cite GR:579 and AUDIT item 2.9 in F4. Reclassify it as "ELABORATING (mechanism and target form; extends GR:579 / AUDIT 2.9)", or give an explicit argument for why the frozen-bath mechanism is not covered by them.

### S-7 (should-fix): F5 and Q3 should state that the two horizon energies differ by definition, and point at the sentence that needs checking

**Where.** F5 at UNIT1:421, UNIT1:425–434; NOTES:128–130 (Q3).

**Evidence.** I checked the algebra and it is correct:

- S_dS·k_B T_cl = (σ·4πc²/(H²ε²))·(c³ε²H/(8πGσ)) = c⁵/(2GH) = c⁴R/(2G);
- with κ = cH and dA = 8πR dR, the first law gives dE = c⁴dR/G, hence c⁴R/G;
- ρ_s = E_s/V_H = 3c²H²/(8πG), matching GR:424.

The two quantities are distinct by definition. GR:58 defines E as "the energy of the horizon first law" (the H-count shell energy). GR:422 defines E_s := S_dS·k_B T_cl as "the total thermal energy". So the factor 2 is not an inconsistency between two values of one quantity, and the draft does not claim it is. Q3 asks "Which is W1-0's 'energy of the horizon first law'?", but GR:58 answers that: it is E. Note that W1-1-REPORT-r4.md:301 also says "the energy H receives in the horizon first law".

The live item that F5 exposes is narrower. GR:426 says "The identity ρ_s = ρ_crit is a consequence of Jacobson's Clausius relation". Integrating the Clausius relation from R = 0 gives 2ρ_crit. ρ_crit follows only from the product definition E_s = TS: the Clausius relation supplies T, and the area law supplies S. Also, "the first law integrated with zero constant" (UNIT1:421) is the draft's reconstruction, not GR:58's wording, and "E_D" is undefined.

**Fix.**

- Rewrite F5 as: "GR:58's E is by definition the first-law energy. Its de Sitter value c⁴R/G is the first law integrated from R = 0 with zero constant [A]. GR:422's E_s := S_dS k_B T_cl = c⁴R/(2G) is a different quantity by definition. The factor 2 is the Euler relation for S ∝ E². Under P11 the origin of E is a convention (GR:58), and E_s carries no additive constant. Assumption-watch: GR:426's attribution of ρ_s = ρ_crit to the Clausius relation; the integrated Clausius energy gives 2ρ_crit."
- Define E_D or drop it.
- Restate Q3 as: "Should GR:426's attribution sentence be reviewed in a separately authorized manuscript unit?"

### S-8 (should-fix): one support label is wrong

**Where.** UNIT1:154.

**Evidence.** The converse of (TL) is labelled [K]. `ad_eq_scalar` (AntiunitaryInvariance.lean:201) gives U(t) = c(t)·W(t) at each t. `phase_families_shift` (:244) assumes a common scalar between *phase families* on one index set. The step from the matrix identity to the hypothesis on the phase family is not a kernel declaration. It is the prose step at GR:747 ("the resulting identity of spectral phase families"). No Lean file composes the two declarations; the only uses are the docstring at :154–156 and :291.

**Fix.** Change "[K]" to "[K] for each step, [P] for their composition (GR:747)".

### S-9 (should-fix): an undefined "λ-family"

**Where.** UNIT1:349, UNIT1:406.

**Evidence.** §3 defines no λ-family, and both lines refer to one.

**Fix.** Define it in §3.1, for example as "the one-parameter family 𝒮_λ(κ, r, g) = T^cl − λρ(r)g with Λ_λ = Λ₀ − 8πGλρ(r₀), λ ∈ ℝ; λ = 0 is K_dec and λ = 1 is K_cpl". Alternatively, rephrase both lines.

### N-1 (nit): inventory line references and the Λ claim

**Where.** UNIT1:78, UNIT1:123, F7 at UNIT1:423; NOTES:35–36.

**Evidence.**

- The `shift_normSq` docstring is at BohrFrequency.lean:**8**, not :7.
- The same header (:9) names `reflect_normSq`, but the declaration is `reflect_modsq` (:279). That is a second mismatch, which F7 misses.
- "The only appearance of `Λ` … is the exterior power `Λ²ℝ⁴`" is false. `Λ` appears in 22 Lean files: for example as a region `Finset` (SecondOrderDrive.lean:59, :361) and as a matrix (MinimalRepertoire.lean:21). None of these denotes a cosmological constant.
- `OrientationClosure.lean` carries `E₀` in the reflection form (:135–141, :256–265) and is missing from NOTES:35–36's hit list.

**Fix.**

- UNIT1:78 and F7: change ":7" to ":8". Add "and names `reflect_normSq` (:9) for `reflect_modsq` (:279)".
- UNIT1:123: replace the sentence with "No occurrence of `Λ` denotes a cosmological constant. It appears as the exterior power `Λ²ℝ⁴` (OI_Regulator_Symmetry.lean) and as a region or matrix name elsewhere."
- Add OrientationClosure to NOTES:35–36, with "reflection form only".

### N-2 (nit): hypotheses of K9

**Where.** UNIT1:70.

**Evidence.** `twoBranch_of_BGSignedClassification` (:446) also requires `W * Wᴴ = 1`. `twoBranch_of_triangleGeneric` (:296) does not.

**Fix.** Add "and `W W† = 1` for :446".

### N-3 (nit): literature line references

**Where.** UNIT1:299, :383–384, :388, §7.

**Evidence.**

- Introduction:244, :258 and :288 are bibliography entries. The citing sentence is Introduction:161, which cites EvEMU11 and KP14. Wei89 is cited at Introduction:157.
- The Wald entry (UNIT1:459–460) has no reference.

**Fix.**

- Write "listed at Introduction:244, cited at :161", and the same for the other two.
- Give the Wald reference (for example, *QFT in Curved Spacetime and Black Hole Thermodynamics*, 1994, §4.6), keeping the [L, recalled] label. Otherwise drop the entry.

***

## Answers to the brief

1. **Countermodel.**
   - Valid as algebra and as a non-implication about source maps from the operational data.
   - The shared-data rows are correct at r₀, with the provisos in S-3 and S-4.
   - It is not circular: §2's refusal to factor 𝒮 through Op(r) (UNIT1:163–166) is correct and is respected.
   - The omitted datum is the geometry-first ordering requirement (ii) (B-1). The partition row should also note that, on shell, K_cpl pins the origin (S-4).
2. **The GR:352 reading.**
   - Confirmed: with one T^cl and one geometric side, H² moves by 8πGρ_C/3 and the partition moves with it.
   - GR:340, which puts the metric among the substratum data, makes the point stronger.
   - Only the free-constant reading and the classical-origin relabelling (S-3) preserve the content of GR:352; ρ_C = 0 makes the claim empty.
3. **Inventory.**
   - I checked 15 declarations against `c3b5f37a`: K1 :235, K2 :215, K3 :146 and :291, K4 :265 and :279, K5 :244, K6 :285, K7 :201, K8 :251, K9 :296 and :446, K10 :66 and :76, K11 :192, :195 and :239, K12 :318, :336 and :356, K13 :256, K14 :403 and :472, K15 :69 and :104.
   - Statements and hypotheses match, except N-2.
   - Imports are confirmed at OIBridge.lean:86, :93, :95–97 and :284.
   - Negative claim: my case-insensitive grep over all 247 `.lean` files outside `.lake` covered stress-energy, Einstein, Bianchi, cosmolog, metric tensor, Lorentzian, Ricci, Clausius, Unruh, Raychaudhuri, Jacobson, Bekenstein, Hawking, first law, area law, gravit, Friedmann, de Sitter, vacuum energy, zero-point, ħ/hbar and gap equation. Its only hits are HexLatticeGas.lean:102, HydroClosureBridge.lean:69 and HydroSourceAudit.lean:90, each disclaiming gravity, plus one unrelated match in HomometricKill.lean:340.
   - The negative claim therefore holds as stated, apart from the `Λ` sentence (N-1).
4. **Dependency trace.** All cited lines resolve to the stated content:
   - GR:12, :40, :52, :58, :62–66, :70, :74, :78, :84, :86, :88, :162, :172, :292, :334, :340, :344–352, :356, :358, :362, :374, :422–426, :466, :573–579, :633, :655, :693–697, :745–751;
   - Main:62, :228, :242, :340;
   - Introduction:159–161;
   - SM:144–148, :160–162, :292;
   - W1-1-REPORT-r4.md:140, :298, :301, :346–351;
   - ROADMAP.md:85, :1194, :1214–1219;
   - the exceptions are BohrFrequency.lean:7, which should be :8 (N-1), and the literature lines in N-3.
5. **Claim/evidence boundary.**
   - Finite list → universal: S-2.
   - Wrong support label: S-8; the [A] label conditional on an open premise: S-5.
   - Negative results are scoped to the class ruled out, except the R2 admissibility claim: B-2.
   - §A.34 is kept: only (TL) ⇒ (SI) is posed, and the converse is marked trivial.
   - Literature is marked [L, recalled], and no verdict rests on it, except that R2's "Λ returns as an integration constant" and the sequestering identification should keep that label (B-2).
6. **The new findings.**
   - The distinction about where an offset comes from is partly in the corpus already (GR:579, AUDIT 2.9). It is an elaboration, not NEW (S-6).
   - The factor 2 is arithmetically real. The two quantities differ by definition and are not inconsistent. The item worth recording is GR:426's attribution sentence (S-7).
7. **The proposed next obligation.**
   - ℱ = ¼T satisfies the shift condition, and ℱ = const does not; both are correct as algebra.
   - ℱ = ¼T is admissible only with a trace-free left side. Under the Bianchi structure GR:12 names, it violates conservation (B-2).
   - O1 is not the smallest obligation. A smaller, paper-only O0 comes before it: settle what requirement (ii) of the geometry-first ordering (GR:346), on the GR:350 scope, implies for a boundary metric that depends on the emergent origin. If it excludes such a metric, (SI) for the uniform term follows conditionally on (ii), and O1 becomes secondary.
8. **Register.**
   - The added lines show no §A.32 or §A.33 phrase families, no capitals used for emphasis, no revision-history voice, and no local path strings.
   - "The substance of GR:352 stands" (UNIT1:288) is evaluative, but it is a review statement in a draft record, not paper prose. Optionally rephrase it as "The non-implication at GR:352 holds".

***

## Disposition

REVISE.

- **Blocking: B-1 and B-2.** Before r2 can be accepted, add the B5 node with the corresponding verdict conditioning, and correct R2, O1 and (SI′).
- **Should-fix: S-1 to S-9.** They are small and local.
- **Nits: N-1 to N-3.**

No manuscript change is proposed. The assumption-watch items on GR:12 (B-2, item 5) and GR:426 (S-7) are candidates for a separately authorized manuscript unit.
