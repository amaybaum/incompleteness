# Minimal-#982 report — papers/Substratum.md (group: substratum)

Output: `minimal/papers/Substratum.md` = OLD (`0d917665`) + the N edits below. Built by
a replacement script (each replacement asserted to match exactly once in OLD).

Hunks are counted per changed OLD paragraph (word-diff granularity): 75 paragraphs touched by #982.
**N = 26, U = 45, UNCERTAIN = 4 (kept OLD).** Plus 1 consistency edit outside #982's hunks (E6 citation numbers).

## N edits (old → minimal)

| old line | reason | old → minimal |
|---|---|---|
| 16 (abstract) | G1, G3 | "conditional on the named modeling and completeness premises" → "…modeling and nearest-neighbor premises"; "Theorem 24 identifies the observables-preserving kernel …, conditional on Lemma 24.1's semigroup-transfer completeness step." → "Theorem 24 identifies generators of the observables-preserving kernel …; their completeness is open." |
| 24 (intro) | G1, G3 | "(M1-T; C2-mixing; Lemma 24.1's completeness step, together with the Stage-2 structural inputs) — … fixes the residue up to the stated gauge freedoms." → "(M1-T; C2-mixing; the Stage-2 structural inputs, including the nearest-neighbor premise) — … fixes the residue."; "The substratum gauge group identifies the kernel of this inverse map — four families …, that exhaust — conditional on Lemma 24.1's completeness step — all observables-preserving operations … (§4) — and shows" → "The substratum gauge group is the kernel of this inverse map; §4 identifies four families … in it, …, whose exhaustion of all observables-preserving operations of the dilation-datum substratum is open, and shows" |
| 32 (§1.1) | G1 cross-ref | "neither Theorem 23 nor Lemma 24.1 proves" → "Theorem 23 does not prove" |
| 104 | G3 | "holds under E1–E7 **and** A1–A6 jointly;" → "…jointly, with the nearest-neighbor premise of Stage 2(b);"; "The set A1–A6 is sufficient" → "The set A1–A6, with that premise, is sufficient" |
| 139 Stage-1 gauge statement | G1 (Pair C: equal Φ_t, not conjugate) | "dilation freedoms are absorbed into the stated substratum-gauge directions: …enlargement." → "…include the stated substratum-gauge directions: …enlargement; equal channel families need not have unitarily conjugate dilations (§4)." |
| 165 Stage 2(e) | G5 | "Anomaly cancellation (Theorems 14–15) uniquely fixes the hypercharges." → "…fixes the hypercharges up to normalization and quark-singlet interchange, apart from the exceptional branch $Y_Q=0$." |
| 169 Uniqueness at Stage 2 | G3, G5, G1 | "…unique consistent choice given the inputs. … so the output is unique up to $\mathcal G_{\rm sub}$." → "…given the inputs, step (b) within the nearest-neighbor class and step (e) apart from its exceptional branch. … so the output is unique." |
| 189 Lemma 23.0 | G1, G3, G5 | drop "Conditional on Lemma 24.1's semigroup-transfer/completeness step," and "up to the local action of $\mathcal G_{\rm sub}$"; add "and both lie in the nearest-neighbor class of Stage 2(b). Then"; "associated local representation data" → "… (hypercharges apart from the exceptional branch of Stage 2(e))" |
| 191 Lemma 23.0 proof | G1 | delete "Stage 1 fixes the finite channel/dilation datum … only up to its stated dilation/gauge freedoms and the explicit operational-lift conditions." (false by Pair C, not needed); "Stage 2 then selects … from E4–E7 and A3–A6;" → "Stage 2 selects … from E4–E7, A3–A6 and the nearest-neighbor premise;"; "because neither Lemma 24.1 nor the Stage-2 uniqueness argument acts" → "because the Stage-2 uniqueness argument does not act" |
| 193 Theorem 23 | G1, G3, G5 | "and Lemma 24.1's semigroup-transfer/completeness step hold. Then the reconstruction uniquely fixes, up to the stated substratum-gauge freedoms, the" → "and the nearest-neighbor premise of Stage 2(b) hold. Then the reconstruction fixes the"; qualification list adds "the exceptional hypercharge branch $Y_Q=0$," |
| 195 Theorem 23 proof | G1 cross-ref | delete ", and Lemma 24.1 controls the visible channel-semigroup dilation datum rather than such Bell-composite structure" |
| 199 Remark (Evidential weight) | G3, G5 | "The reconstruction uniquely derives" → "Within the nearest-neighbor class of Stage 2(b), the reconstruction uniquely derives"; "and unique hypercharges." → "and hypercharges unique up to normalization and quark-singlet interchange apart from the exceptional branch $Y_Q=0$." |
| 201 Remark (Substantive content) | G2, G5 | "(state relabeling," → "(hidden-sector relabeling,"; "the anomaly-free hypercharge assignment." → "… assignment (apart from the exceptional branch $Y_Q=0$)." |
| 203 Refinement | G5, G3 (Theorem 7b) | "the hypercharges —" → "the hypercharges (apart from the exceptional branch $Y_Q=0$) —"; "the simple-cubic Bravais structure is selected because" → "…is selected, within the nearest-neighbor class, because" |
| 212 | G3 | "within the stated structural class the **local reconstructed residue**" → "within the stated structural class, with the nearest-neighbor premise of Stage 2(b), the **local reconstructed residue**" |
| 253 Theorem 24(i) | G2 | whole clause "*(i) State relabeling.* For any bijection π: S→S … $|S|!$-element subgroup … *(Scope.)* … amplitude-scale subgroup (Remark below)." → "*(i) Hidden-sector relabeling.* For any bijection σ: C_H→C_H, applied identically in every visible fibre, π(v,h)=(v,σ(h)), the conjugate (S,πφπ⁻¹) ∼ (S,φ): with uniform hidden prior ω_H=𝟙/|C_H|, every visible channel Φ_t(ρ_V)=Tr_H[φ̂^t(ρ_V⊗ω_H)φ̂^{-t}], with φ̂ the permutation unitary of φ, is unchanged. A fibre-dependent hidden relabelling (v,h)↦(v,σ_v(h)) preserves the transition probabilities T_ij(t) but not, in general, the coherent channels Φ_t." (Φ_t definition carried over from the removed Lemma 24.1; the dropped Scope note described all-bijection (i); its affine-relabelling fact remains in the amplitude-scale Remark.) |
| 261 Theorem 24 proof (i) | G2 | "(i): conjugation preserves the coupling graph … eigenvalue multiplicities)." → "(i): conjugation by 𝟙_V⊗P_σ leaves ω_H invariant and cancels under the partial trace, so every Φ_t is unchanged; for a fibre-dependent σ_v the visible coordinate is fixed and each rooted fibre's uniform hidden prior is permuted bijectively, so every T_ij(t) is unchanged." |
| 267 Remark Status | G2 | "generator (i) over-counts (its full $|S|!$ includes dispersion-altering nonlinear relabellings, …)" → "generator (i) relabels hidden states only" |
| 271–298 Completeness / Lemma 24.1 / Steps 1–3 / Conclusion / Scope / fifth families | G1, G2 | Heading "(conditional)"→"(open)"; first sentences → "Whether the four families exhaust G_sub, family (ii) entering under the alphabet-size hypothesis, is open. The question has two logical parts … — is not established." + Pair C (ST3_pairC) sentences taken verbatim from #982. Lemma 24.1, its proof, the specialist note, Steps 1–3, Conclusion and Scope paragraph removed (their conclusion rests on Lemma 24.1). Inserted: #982's Specht–Wiegmann attribution sentence ([7–9]→[5–7]), Proposition 24.2 and its proof verbatim, and "The ST3_pairC pair has unequal block-word traces (pairC_wordTraces), so it does not meet Proposition 24.2's premises." Fifth-family list: "Three candidate … are explicitly subsumed" → "A candidate fifth family is explicitly subsumed:"; time-reversal bullet removed (T is not hidden-only, G2); hidden-reparametrization bullet removed (false, G1/Pair C); global-phase bullet kept verbatim. |
| 317 (§5 intro) | G1, G3 | "and Lemma 24.1's completeness step, uniquely fix the residue modulo the stated substratum-gauge freedoms." → "and the nearest-neighbor premise of Stage 2(b), fix the residue." |
| 345 | G2 | "(state relabeling," → "(hidden-sector relabeling," |
| 383 (§6) | G1/G3 consistency with Thm 23 | "residue modulo the stated substratum-gauge freedoms**: Theorem 23 uniquely fixes" → "residue**: Theorem 23 fixes" |
| 393 | G1 | "determinate modulo the stated gauge freedoms, while" → "determinate, while" |
| 498 (§7) | G1, G3, G5 | "Under M1-T, C2-mixing and Lemma 24.1's completeness step, the reconstruction uniquely fixes the residue modulo the stated gauge freedoms;" → "Under M1-T, C2-mixing and the nearest-neighbor premise of Stage 2(b), the reconstruction fixes the residue;"; "forced once the observed family pattern is given" + ", apart from the exceptional branch $Y_Q=0$"; "identifies the kernel of this inverse map and shows" → "identifies generators of the kernel of this inverse map, whose completeness is open, and shows"; "what the reconstruction fixes, modulo the stated gauge freedoms." → "what the reconstruction fixes." |
| 502 | G1 | "residue modulo its stated gauge freedoms, while" → "residue, while" |
| 517 references | needed by retained Prop 24.2 | add #982's Specht [7], Wiegmann [8], Futorny–Horn–Sergeichuk [9], renumbered [5]–[7] (only these are cited). |
| 86 (E6; not a #982 hunk) | dangling citation | OLD cites "Ehrenfest [10]", "Tangherlini [11]", absent from OLD's list (in NEW they resolve to Schützenberger/Carlyle–Paz — wrong). Changed to [8], [9] and added the two entries (text copied from Complexity.md). Coordinator may veto. |

Principle applied: "modulo the *stated* (substratum-)gauge freedoms" names the four families, so it needs completeness → removed; "modulo $\mathcal G_{\rm sub}$ / up to gauge" (G_sub defined as the full observational-equivalence group) is near-tautological and kept, as are statements of invariant uniqueness (d, K, multiplicities, gauge group), which Stage 2 gives without Lemma 24.1.

## UNCERTAIN (OLD kept)

- **163 Stage 2(d)** U(3)×U(2)×U(1) → SU(3)×SU(2)×U(1) "because the overall U(1) phase of each block is gauge under amplitude-scale invariance". One global scalar circle cannot remove two independent block phases; the theorem-recovery audit row "SM gauge reduction" says only the common scalar circle is in the kernel. Not a G-item, and fixing it cascades through the Stage 2 output, Thm 23, Level 2, §5.1 and the SM mirror. **Coordinator decision.**
- **259 Theorem 24(iv)** The header puts (iv) in G_sub, whose ∼ means identical T_ij(t). But (iv) itself claims only the same "content", "for this content", and Z³ vs a random graph do not have equal T_ij(t). I kept OLD because the text qualifies itself; a fix would cascade to A3, line 345 and Lemma 23.0's proof.
- **303 Level 2** "image of G_sub restricted to transformations that permute internal components": these act on visible sites, so membership relied on all-bijection (i). Same issue at 323 (§5.1 "SM gauge group … commutant", tied to 163).
- (ii) kept OLD (U): it is explicitly conditional on the alphabet-size hypothesis.

## U (reverted to OLD), one line each

26, 28 (rewordings); 36, 38 (realism framing, not false); 50 (substrate objection); 58, 60 (G6: embedded-observer opacity correct); 62, 68 (residue up to gauge); 92 A1, 257 (iii), 263 Corollary (G7); 96 A3 (matches the qualified (iv)); 119; 141 Stage-1 status; 161 (c) (already H-link/H-spin' conditional); 173; 223; 229, 231–235 (bidirectional arrow modulo G_sub, near-tautological; the finite-data remark); 246 (new §3.7 companion-family section, not required); 249 ∼ definition; 251 Theorem 24 header; 255 (ii); 265 amplitude Remark; 301, 305–311 hierarchy and Remark (restored); 323 visible projection (see UNCERTAIN); 327, 343, 371, 373, 379, 387 (soundness only), 389 ("modulo gauge" = G_sub), 391, 399–405, 488 ("within the equivalence class", by definition). Props 24.3–24.5, Pair C operator certificate, "Limits"/"Open scope" paragraphs, §4.1 and references [5],[6],[10]–[12] dropped.

## Statements whose text differs OLD → MINIMAL (ledger updates)

- **Theorem 23**: hypotheses (Lemma 24.1 → nearest-neighbor premise); conclusion ("uniquely fixes, up to the stated substratum-gauge freedoms" → "fixes"); added the $Y_Q=0$ qualification.
- **Lemma 23.0**: Lemma 24.1 condition removed; nearest-neighbor hypothesis added; "up to the local action of G_sub" removed; hypercharge qualification added. Proof also changed.
- **Theorem 24**: clause (i) restated (hidden-only σ; fibre-dependent σ_v preserves T_ij only); header, (ii), (iii), (iv) unchanged. Proof (i) changed.
- **Lemma 24.1**: removed.
- **Proposition 24.2**: added (verbatim from #982).
- Non-numbered but status-bearing: "Completeness of the generators" (conditional → open); "Uniqueness at Stage 2"; "Stage-1 gauge statement"; Remark (Evidential weight); Remark (Substantive content) and its Refinement; Stage 2(e); the Status note of the amplitude-scale Remark.

## Checks

No remaining "Lemma 24.1", "Proposition 24.3/24.4/24.5", "$|S|!$", "state relabeling", "stated (substratum-)gauge freedoms" or "completeness step". Every numeric citation [1]–[9] resolves ([100]/[110]/[111] are Miller indices). No `---` rules were added, and lines 1–15 are byte-identical to OLD. I did not run the PDF build.
