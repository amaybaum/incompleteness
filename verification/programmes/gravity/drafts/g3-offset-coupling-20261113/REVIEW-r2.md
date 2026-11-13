# REVIEW-r2: G3 unit 1 (r2), offset coupling and the covariant source

**Verdict: REVISE, with one blocking finding.** Once R2-1's text is applied, a delta check of the passages it names is enough.

r2 resolves the r1 review correctly in substance:

- R2a and R2b are split correctly, and the algebra is right.
- (SI′) and the restated O1 are correct.
- The null-flux link to SM:160–162 is correct.
- Every changed citation resolves on `main`.

B5 (Q8) is not sound as argued. "On shell, metric → origin" holds only because the completion is built so that the origin is a free coordinate whose value Λ₁ already encodes. That coupled completion has the same worlds as K_dec and carries no fine-tuning content.

The coupled completion that GR:352 contrasts fixes the offset by the emergent description's own normalization. That is a function of the reconstructed gaps and mode count, which exist only after the partition. For that completion, GR:346's loop closes, and GR:346 as argued excludes it. It survives only on the corpus's own use of (ii): GR:400 Reading 1 admits a self-consistent loop of the same form. So F8 and the "as argued" half of the verdict basis overclaim.

Whether the verdict survives depends on that distinction:

- As a statement about source maps, the verdict survives on every reading.
- As a statement about a coupled completion with physical content, it is conditional on the corpus's reading of (ii).

**Target.** Branch `research/g3-offset-873-20261113` at `1aaf87a2d34ff815b0fdb1bda73ffa0133415b5e`. Its parent `5fe230cd` adds REVIEW-r1 byte-identical to the review as issued, which I checked with `diff`. The r2 head adds G3-UNIT1-r2.md (608 lines), NOTES-r2.md (127) and RESPONSE-r1.md (195). The r1 files are unchanged. Corpus citations refer to `main` at `c3b5f37a`. "r2:n" means G3-UNIT1-r2.md line n, "N2:n" means NOTES-r2.md, and "RESP:n" means RESPONSE-r1.md.

**Checks at `1aaf87a2`.** All pass:

| Check | Result |
|---|---|
| `tools/claims_check.py` | OK |
| `tools/staleness_check.py` | OK, 13 matched |
| `tools/voice_check.py` | OK, 40 files |
| `tools/artifact_placement_check.py` | OK, self-test passed |
| `tools/legacy_records_check.py 1aaf87a2…` | 303 records intact |

None of them scans the drafts.

***

## Findings

### R2-1 (blocking): B5's "metric → origin" holds only for a free-origin coupling, which has no physical content. The contentful coupling closes GR:346's loop.

**Where.**

- r2:310–317, the on-shell paragraph;
- r2:37–39 and r2:449–450, the verdict basis "as argued and as used";
- r2:429–436, the bullet "Which reading GR:346's argument supports";
- F1 at r2:560 ("B5 included") and F8 at r2:567;
- O0 at r2:537–538;
- N2:76–78 and N2:71 ("does not depend on … the gaps");
- RESP:49–55.

**Evidence.**

1. **The completion encodes r₀.** It is defined with Λ₁ := Λ₀ − 8πGρ(r₀) (r2:275), and its field equation constrains ρ(r) only through the sum Λ₁ + 8πGρ(r). (TL) leaves the origin free (r2:432). So within K_cpl as constructed, nothing but the metric fixes ρ(r). The on-shell "selection" at r2:311–312 reads back the r₀ that Λ₁'s definition put in. Call this completion **K_cpl^free**, with e(r) = min E taken as a free coordinate on the σ-orbit.
   - The order "metric → origin" is real for K_cpl^free, and K_cpl^free does violate (SI) as a map.
   - But Λ₁ and ρ(r₀) are each undetermined, and only their sum is fixed by the metric. K_cpl^free and K_dec admit the same set of worlds (κ, g) and differ only in which constant is called vacuum energy.
   - The fine-tuning reading r2:316–317 attaches to it, "whether the observed Λ_eff is the sum Λ₁ + 8πGρ(r₀)", needs ρ(r₀) to be fixed independently of the metric. In K_cpl^free it is not.
2. **The coupled completion GR:352 contrasts.** That is the one that produces the 10^122 discrepancy (GR:352(a), GR:336). It fixes the offset by the emergent description: "The zero-point energy is the ground-state eigenvalue of Ĥ_eff" (GR:358), with "½ħω per mode with UV cutoff" (GR:332). Call this **K_cpl^conv**, with e(r) the ground eigenvalue under that normalization.
   - That value is a function of the reconstructed gaps and of the mode count.
   - Those are outputs of the transition data, which exist only after the partition is drawn.
   - Determination then runs: partition → transition data → gaps and mode count → e → metric → causal structure → partition.
   - That is GR:346's loop QM → metric → causal structure → partition → QM, closed through the uniform term.
   - B5's premise "the origin is not an output of the QM description" (r2:432) is false for K_cpl^conv. There the origin *is* an output, by the emergent description's own convention.
3. **The corpus's use of (ii) still supports survival in a modified form.**
   - GR:400 Reading 1 lets "the emergent layer's curvature response" feed back as a source. That response is defined after the partition and depends on H, and the source fixes the H that sets the horizon. GR:374 ("the emergent vacuum energy … depending on the hidden sector's volume") and GR:358 have the same form. That is a self-consistent loop of exactly GR:346's form. So the corpus does not apply GR:346 to forbid such loops.
   - Reading 1 also fixes "the constant part" by stipulation, as r2:443–445 correctly records.
   - Result: GR:346 *as argued* ("a circular dependency with no entry point") excludes K_cpl^conv, while GR:346 *as used* (fixed-point loops admitted, GR:400 Reading 1) does not.
   - GR:346's text and GR:400 Reading 1 are in tension. Neither r1 nor r2 records this.
4. **Consequences.**
   - F8's "The argument supports the weak reading only" is not established.
   - The verdict basis "as argued and as used" (r2:38–39, :449) must drop "as argued".
   - F1's "(B5 included)" inherits the gap.
   - N2:71's "does not depend on … the gaps" holds only for the free-origin parametrization.

**Fix.**

1. **The on-shell paragraph (r2:310–317).** Replace it with:

   > "**On shell, two cases [A].** (a) **K_cpl^free**: e(r) = min E as a free coordinate on the σ-orbit. With the metric in κ, the field equation fixes only Λ₁ + 8πGρ(r). K_cpl^free and K_dec admit the same worlds (κ, g) and differ only in which constant is called vacuum energy. No fine-tuning reading applies. (b) **K_cpl^conv**: e(r) is the ground eigenvalue under the emergent normalization (½ħω per mode to the cutoff; GR:332, GR:358). This is a function of the reconstructed gaps and mode count, so ρ(r₀) is fixed independently of the metric. Whether the observed Λ_eff is Λ₁ + 8πGρ(r₀) is then the fine-tuning reading at GR:352."

2. **B5 (ii).** Replace the bullet "Which reading GR:346's argument supports" (r2:429–436) with:

   > "For K_cpl^free the loop does not close: the metric fixes the origin's coordinate. For K_cpl^conv it closes through the gaps and the mode count (partition → transition data → e → metric → partition). GR:346 as argued ('no entry point') therefore excludes K_cpl^conv. The corpus admits a loop of the same form at GR:400 Reading 1 (and GR:358, GR:374), so it does not apply GR:346 to self-consistent loops. It excludes the constant emergent part only by stipulation (GR:400)."

   Then replace the node verdict (r2:449–450) with:

   > "K_cpl^free survives (ii) on every reading but is world-equivalent to K_dec. K_cpl^conv survives (ii) as the corpus uses it (self-consistent loops admitted, GR:400 Reading 1). It does not survive (ii) as argued at GR:346. Assumption-watch AW-loop: GR:346's no-entry-point argument and GR:400 Reading 1's emergent feedback are in tension."

3. **The verdict in §0 and §5.** In §0 (r2:35–58) and §5 (r2:481–482), state:

   > "Counterexample, scoped in two parts. (1) As a property of source maps, (SI) is not implied on any reading of (ii) (K_cpl^free), but this coupled completion is world-equivalent to K_dec. (2) A coupled completion with physical content (K_cpl^conv) is compatible with OI's results conditional on reading (ii) as the corpus uses it (GR:400 Reading 1). On GR:346 as argued it is excluded, and (SI) for the convention-fixed offset follows conditionally (route R0)."

   Redefine R0 accordingly: "GR:346 as argued (no self-consistent loop through post-partition data)". That reading is weaker than (ii-S), and it already suffices against K_cpl^conv.
4. **The findings.**
   - Rewrite F8 to the B5 result above, class NEW candidate (the GR:346 / GR:400 tension) or ELABORATING, flagged for review.
   - Change F1's "(B5 included)" to "(B5: K_cpl^free on every reading, K_cpl^conv on the corpus's reading)".
   - Add AW-loop to the assumption-watch markers.
   - Update O0's status (r2:537–538) and Q7/Q8 (N2:111–118) to match.
5. **NOTES and RESPONSE.**
   - Change N2:71 to "does not depend on the state; as a free coordinate on the σ-orbit it carries no gap dependence".
   - Correct N2:76–78 and RESP:49–55 to the narrowed result.

### R2-2 (should-fix): the reflection impossibility claim is broader than the algebra

**Where.** r2:305–308; N2:73; RESP:102–103.

**Evidence.** The argument is correct for the involution E ↦ −E. More generally, it is correct for any reflection E ↦ −E + c whose constant c does not depend on E: shift equivariance gives e(−(E+C) + c) = e(E) − C, while invariance gives e(E) + C.

The branch K9 actually delivers is H' = −DH̄D† + E₀ with E₀ free (PairIdentification.lean:296, :446). A reflection anchored to the spectrum admits invariant equivariant functionals. Example: E ↦ −E + 2·mean(E), under which the mean (tr Ω/m) is invariant, and under which the midrange (max E + min E)/2 is also invariant. Both are shift-equivariant. So "no functional that moves with the shift can be invariant under the reflection" is false for the branch as OI states it. How K_cpl responds "to the branch" is a convention about the origin of the reflected representative. Scoping "differ only" to the oriented branch remains harmless and can stay.

**Fix.** Replace r2:305–308 with:

> "No shift-equivariant functional is invariant under a reflection E ↦ −E + c with c independent of E [A]. Under a reflection anchored to the spectrum (E ↦ −E + 2·mean(E)), the mean tr Ω/m is invariant. Since K9 leaves E₀ free in the reflected branch, how K_cpl responds to the branch is a convention. 'Differ only' is stated on the oriented branch, where it does not arise."

Correct N2:73 and RESP:102–103 to match.

### R2-3 (should-fix): the residual freedom at fixed κ needs K9's hypotheses

**Where.** r2:300–302.

**Evidence.** "At fixed κ … the residual freedom of r is the shift, the D-gauge, the eigenframe phases and the antiunitary branch" is K9's conclusion. It holds under K9's hypotheses: 3 ≤ m, nonzero overlaps, distinct gaps, and (G4) or `BGSignedClassification` (r2:98). Outside them, for example with degenerate gaps (BohrFrequency.lean:10–11, the C₄ ring), the class can be larger.

**Fix.** Add "(under K9's hypotheses, r2:98)" after "the residual freedom of `r` is".

### R2-4 (should-fix): "E_s carries no additive constant" is imprecise

This wording came from REVIEW-r1, S-7.

**Where.** F5 at r2:564.

**Evidence.** E_s = S_dS·k_B T_cl inherits the additive constant of the entropy. GR:58 gives s_H = σA/ε² "up to an energy-independent constant", and S_dS = σA/ε² sets it to zero (GR:422). E_s carries no energy-origin constant, but it does carry the entropy's.

**Fix.** Replace "and `E_s` carries no additive constant" with "`E_s` carries no energy-origin constant; it inherits the additive constant of `s_H` (GR:58), set to zero in `S_dS = σA/ε²` (GR:422)".

### R2-5 (should-fix): relabelling T^cl inherits B2(c)'s condition

**Where.** r2:263–264, r2:353–354.

**Evidence.** The relabelling T^cl_2 = T^cl_1 + ρ_C g treats a shift of the classical origin as a vacuum-stress term. B2(c) (r2:387–389) correctly makes that conditional on a covariant continuum limit, but the relabelling cites B2(c) without carrying the condition.

**Fix.** At both places append "(conditional, as in B2(c), on a covariant continuum limit in which a uniform classical energy has vacuum stress)". Carry the same qualifier into F2 (r2:561).

### R2-6 (should-fix): O1 asserts unconditional compatibility of the λ-family

**Where.** r2:548–549.

**Evidence.** "The λ-family of §3.1 is one such completion at the level of the source map" asserts compatibility with every OI premise. That compatibility is conditional on B5, and after R2-1 it is unconditional only for K_cpl^free.

**Fix.** Append: "…compatible with every OI premise for K_cpl^free; for a convention-fixed coupling (K_cpl^conv), conditional on the corpus's reading of (ii) (B5)".

### R2-7 (nit): κ⁻ keeps the partition, which the metric determines

**Where.** r2:175, r2:199–201.

**Evidence.** κ⁻ is defined as "κ without the metric" and still contains the partition, which GR:346 fixes from the metric's causal structure. Sol(κ⁻, r) then restricts g to metrics whose horizon matches the fixed partition. For K_cpl the shifted set may then be empty. That is still a violation of (SI′), but not for the reason r2:298 gives.

**Fix.** Define "`κ⁻` denotes `κ` without the metric and without the partition, which the metric fixes (GR:346)".

### R2-8 (nit): the spacetime average needs a finite 4-volume

**Where.** r2:521–522.

**Fix.** After `ℱ = ¼⟨g^{μν}T_μν⟩` add "(defined when the spacetime 4-volume is finite, or for a normalized average)".

### R2-9 (nit): register

**Where.** r2:446.

**Evidence.** "(ii-S) would give (SI) cheaply" is an evaluative adverb.

**Fix.** Write "(ii-S) would give (SI) directly."

***

## Answers to the brief

1. **Resolution of the r1 findings.**
   - B-1 is applied, but B5's new reasoning fails as argued (R2-1).
   - B-2 is applied correctly. I checked:
     - the trace forces c = 0;
     - ∇^μ(R_μν − ¼Rg_μν) = ¼∂_νR gives ∂(R + 8πGT) = 0;
     - R2b's ∂ℱ = 0;
     - ¼⟨T⟩ is shift-equivariant.
   - S-1 is applied differently. e = min E removes the dependence on the state, which is correct. The reflection impossibility claim holds only for constant-anchored reflections (R2-2).
   - S-2 to S-9 and N-1 to N-3 are applied as RESPONSE-r1 states. The exceptions are the qualifiers in R2-4 (my own r1 wording) and R2-5.
2. **B5.** It is not sound as argued. "Metric → origin" is a relabelling for K_cpl^free, because Λ₁ encodes r₀. It hides the dependence on gaps and mode count that the physically contentful coupling (K_cpl^conv; GR:332, GR:358) carries. That dependence closes GR:346's loop. The exact gap and its fix are in R2-1. The dependence on the state ρ is correctly removed by min E.
3. **R2a, R2b, SI′, O1 and the null flux.** Correct, apart from R2-6, R2-7 and R2-8. The SM:160 input (iii) is the null flux. Since ρ g_μν k^μ k^ν = 0, the offset drops out, and Λ at SM:162 is the integration constant [L, recalled].
4. **No new overclaim or premise.**
   - The new citations resolve on `c3b5f37a`: GR:400 (Readings 1 and 2), GR:585 (recurrence φ^N = id), book/ch07-gravity.md:183 and :187, AUDIT.md:55 and :371–378, PairIdentification.lean:448 (`hW`), Introduction:157 and :161.
   - The new overclaims are F8 and the "as argued" basis (R2-1), the reflection claim (R2-2) and O1's unconditional compatibility (R2-6).
   - The cycle-average conjecture (r2:525–526) and the recalled unimodular debate (r2:509–510) are labelled correctly. No premise is adopted.
5. **Register.** The drafts contain no §A.32 or §A.33 phrase families, no capitals used for emphasis, and no local path strings. RESPONSE-r1's "now" (RESP:118, :147) is acceptable in a change record. The one evaluative adverb is covered by R2-9.

***

## Disposition

REVISE.

- **R2-1 (blocking).** It rescopes B5, F1, F8, O0 and the verdict basis. The verdict category can stay "counterexample", in the two-part scoped form given above.
- **R2-2 to R2-6 (should-fix).** Each is a local text change.
- **R2-7 to R2-9 (nits).**

No manuscript change is proposed. The new tension between GR:346 and GR:400 Reading 1 (AW-loop) and the earlier AW-G12 and AW-abs are candidates for a separately authorized manuscript unit.
