# Focused confirmation: RO-3 inventory r6 (PR #1303), with RESPONSE-r5

**Verdict: REVISE.** The narrow scope of the revision: complete the A1 map and update the authority
record.

r6 applies every item of the r5 review correctly, and no label is refuted. The owner's acceptance
condition is not yet met. That condition (#1169 c.6894115930, #1303 row) reads: "The A1 map must be
complete before it is accepted."

- r6 says of its own map that it "is not a complete corpus closure" (r6:114, :903–904).
- AM-16 leaves SM "not traced".
- My sweep found further consumers that the manuscripts carry: Main:588 with GR:266, Main:145, and
  SM Theorems 19 and 22.

The remaining work is editorial. It needs no new mathematics and no change of status.

## Object, base and limits

- **Reviewed.** `RO3-INVENTORY-r6.md` (SHA-256 `7318dafe…7037`) and `RESPONSE-r5.md`, against my
  review of r5. That review's digest `16b5d919…a8d1` matches the one r6 cites.
- **Base.** `main` `7ac74a4bbb2a9f62c76052def3e9da1e67ea70ac`; PR head `78089e5e`.
- **Authority comment.** I read #1169 c.6894115930 first-hand (`amaybaum`, 2026-11-15T12:11:24Z).
- **Limits.** Paper-only and read-only. Nothing was built or run, and nothing was posted.

## 1. The six items asked about

| Item | Status | Checked |
|---|---|---|
| Main:716 reading | **Applied** | AM-5 (r6:913) and §7.3 (r6:983–987) say that the two routes are §3.1 and §3.2, citing Main:352 and :356. The route that avoids A1 now rests on Main:354, :60 and :208. The "§3.4 route" citation is gone. |
| §7.3 with both halves of Main:60 | **Applied** | Both halves are quoted verbatim (r6:974–981), together with DEPENDENCY-AUDIT.md:282 and three readings. r6:866 is narrowed to the equivalence at the level of laws. |
| Seven new consumer rows | **Applied** | AM-20 to AM-26 (r6:932–938). I checked each against its source. Comp:100 is AM-23 and is quoted correctly. AM-25's lines (`SubstratumInterfaceAudit.lean` :764–800 and `obsTheory` at :770; `FrozenSourcing.lean:84`) are correct. |
| D-CQ quotation in Q13 | **Applied** | Q13 (r6:802–809) quotes answer 4's last sentence verbatim. The Standing reading (r6:111–135) covers the exclusion purpose and keeps it [IR]. The "same point" sentence is gone. |
| Causal cone traced to posits (xiii) and (viii) | **Applied** | AM-7 (r6:915) gives the full sourcing and the countercontrol. Its status reads "conditional[the coupling-graph hypothesis, from posits (xiii) and (viii), or GR:132]", which meets the owner's requirement. |
| AM-3 as a recommendation only | **Applied** | §3 (r6:676–724) records it as "a recommendation only", and no candidate is marked chosen. |

Also confirmed:
- H5: the label is applied at r6:251, :285, the §3 bullets and AM-16, and §6's "Use here" cell is
  extended (r6:868).
- H6: AM-3 records the hidden-sector prong.
- §5's correction about the trailing-space search.

## 2. Required changes

### K1 (required): the authority record is stale

r6 Standing (r6:46–49) says that no owner comment authorizing r6 was found. That was written in the
same minute as #1169 c.6894115930, which now records the decision. Its #1303 row, verbatim:

> "After the r6 review, propose bijectivity (AM-3) as the first recovery unit. The question: can
> bijectivity be established from observational structure and a weaker, independently justified
> premise, without total finiteness? Recovery needs a complete proof and at least one independent
> consequence. A negative names the weaker-premise class it excludes. The A1 map must be complete
> before it is accepted. The causal cone is classified as depending on its coupling-graph
> assumptions."

Its "Not authorized" line is "merges …, CI dispatch, new physical premises, or promotion of any
unresolved claim".

**Change:**
- Cite this comment in Standing, quoting it.
- Restate §3's AM-3 entry in the owner's terms. That means a weaker premise, independently
  justified, together with an independent consequence, and a negative that names the class it
  excludes.
- Keep the entry a proposal until after this review.

### K2 (required): consumers still missing

Each item below was read at the base.

- **(a) Main:588 and GR:266, the result that observer access does not source a layer flow.** "The
  stated substratum dynamics with the observer's read and write access do not source that
  executability … (kernel: `obs_not_layerFlowExecutable` in `OIBridge/ExecSource.lean`,
  `coherentLiftClass_eq_substratumClass` in `OIBridge/LiftSource.lean`)."
  - `obs_not_layerFlowExecutable` sits under `variable (𝒮 : Substratum) [Fintype 𝒮.ι]
    [Fintype 𝒮.V]` (ExecSource.lean:125) and is stated of `obsTheory 𝒮`. LiftSource.lean:196 and
    :296 have the same context.
  - These are census 21 and 22, both current. AM-25 lists only census 15 and 31, as kernel-only.
  - Both papers carry these negatives on the operational carrier, so they bear on EXACT.
  - *Status:* established (K) when the configuration space is finite. Without A1 the negative is not
    stated.
- **(b) Main:145, routed readback (the realization clause of C4).** The P-divisibility failure
  "for some `n`, because `(Γ_t)` is periodic and `Γ_0 = I`" rests on `rootedMap_periodic`. Kernel:
  `PhysicalC4Discharge.lean` (:103, finite `V`, `H`; census 35, current) and
  `PhysicalC4StorageReadback.lean` (census 36, current).
  - This line belongs in AM-1, which stops at Main:143.
  - The `Cut` section of `PhysicalC4Discharge.lean` (:576, `cutRealization` with finite sites)
    names "the lattice residual", which is SM Theorem 22's readback genericity lemma (item c).
- **(c) SM.** AM-16's "not traced" leaves gaps that the manuscript carries:
  - **Theorem 22 (SM:1376–1384; also SM:52 and :92).** It works on a finite graph of `N` sites,
    with `|V| ≤ N/3` and the C3 floor read through `log₂|C_H| = |H| log₂ q`.
  - **Theorem 19, reciprocity (SM:643).** "Dividing by `|C_H|` gives `T_ij = T_{θj,θi}`". Kernel:
    `theorem_19` (`Reciprocity.lean:129`, `[Fintype H]` at :40, census 1). It uses the uniform
    prior, as in AM-4.
  - **SM:44.** "requires a bijection on a finite set: bijectivity guarantees recurrence". It mirrors
    AM-1 and AM-3.
  - **SM:112.** Recurrence-cycle P-indivisibility on the ring, a G-fam member of AM-1.
  - **SM:22** (C3 via `|C_H|`) and **SM:1654** (the uniform prior `q^{-2(L-1)}`).
- **(d) Census 32, `StochasticInterface.lean`** (:111 and :182, kernel-only). The ensemble gap is
  stated under finite sites and alphabet. Trace whether the finiteness is used, or list it under
  §7.2 with the reason.
- **(e) Minor: posit (ix).** Posit (ix) is "one degree bound across the family of finite
  representatives", and Main:724 says it gives the cone bounded growth. Note it in AM-7.

### K3 (required): define "complete" by a recipe that can be rerun

A search bounded by phrases cannot certify completeness. Items (a) to (c) above carry no word
"A1" at all. To meet the owner's condition, r7 should state a structural recipe and its result,
in the form of §A.42 item 1:

1. **Lean.** Every `OIBridge` declaration whose context puts `Fintype` or `Finite` on a substratum's
   sites, configuration space or hidden carrier. Search for `𝒮 : Substratum` with `Fintype 𝒮.ι`,
   for `RootedRealization` at substratum cuts, and for `[Fintype S]`/`[Fintype H]` applied to the
   substratum. Map each such declaration to its census family.
2. **Manuscripts.** Every manuscript line that cites a declaration found in step 1.
3. **Hidden and total finiteness in prose.** Every manuscript use of `|C_H|`, of the uniform or
   counting hidden prior, of recurrence or the period of `φ`, of a finite `N` or `L` that is
   load-bearing, and of the phrases r6 already uses.

The map is then "complete relative to that recipe". That is the closure the owner can accept.
Rows found by the recipe that do not consume A1 go to §7.2, each with its reason.

## 3. Corpus sweep (what I ran)

**At the base:**
- whole-word `A1` and the phrase families of r6 §5 over `papers/*.md` and `book/*.md`;
- `|\mathcal{C}_H|`, "recurrence", "counting measure", "uniform prior" and "total system" over SM;
- `𝒮 : Substratum` together with `Fintype 𝒮.ι` over `OIBridge/*.lean`, mapped to census families;
- the manuscript citations of the modules found;
- "total-finiteness", "total finiteness", `A1_finite` and "finiteness posit" over the verification
  records.

**Results:**
- Items K2 (a) to (e) are new.
- The records found besides AM-18 and AM-26 do not consume A1: the OA-1 and OA-2 STATUS files, the
  TUNE-1 step 1, the intro-corpus closure ledger, and ledger r9 row QM–A1. They restate the posit or
  its scope.
- The remaining `papers/*.md` hold no hits outside the seven papers already covered.

**Is the map complete?** No. With K2 and K3 applied, I found nothing further.

## 4. AM-3 as a unit under the owner's question

**The owner's question.** Bijectivity from observational structure plus a weaker, independently
justified premise, without A1. Success needs a complete proof and at least one independent
consequence. A negative names the class it excludes.

### Observations made for this review ([IR], checked by hand; not on `main`)

- **O1: surjectivity needs no normalization.**
  - *Setting.* `φ` is injective and nonsingular on a standard Borel space with a σ-finite measure,
    and is conservative (no wandering set of positive measure).
  - *Argument.*
    - Let `W = X \ φX`. Then `φ⁻¹W = ∅`, so `W` is wandering, and conservativity gives `μ(W) = 0`.
    - By injectivity, `X \ φⁿX = ⋃_{k<n} φᵏW`. Each `φᵏW` is null, by nonsingularity.
    - So `X∞ = ⋂φⁿX` has full measure and `φ(X∞) = X∞`.
    - The images are measurable by Lusin–Souslin.
  - *Comparison with r6.* This is weaker than r6 §3's invariant probability, and it covers I-nonorm.
    Conservativity is the measure form of recurrence. Whether it is the content of Axiom 2, which
    "asserts that differentiation recurs, not that every microstate returns" (Main:60), is a reading
    still to be argued. It is the natural candidate premise with independent justification, but it
    is not adopted here.
  - *Direction (§A.34).* Conservativity is sufficient, not necessary. `n ↦ n+1` on `Z` with counting
    measure is bijective and dissipative.
- **O2: without A1, the empirical prong cannot detect hidden merges.**
  - *The finite case.* A non-injective map does not preserve the uniform prior, and Main:60's test of
    double stochasticity catches it.
  - *The infinite case.* A non-injective map can preserve a probability, and its visible marginal is
    then stationary.
  - *Example.* On `{0,1} × {0,1}^N`, with the uniform measure times Bernoulli(1/2), let
    `T(v, h) = (v ⊕ h₂, σh)`.
    - `T` preserves the measure and is conservative.
    - (C1) holds: the hidden `h₂` moves `v`.
    - Its one-step visible matrix is `[[1/2,1/2],[1/2,1/2]]`, which is doubly stochastic.
    - `T` is 2-to-1. The two preimages of each point share `v` and differ only in `h₁`, so the merge
      is hidden-only and leaves the registered content unchanged.
  - *Comparison with r6.* This is a cleaner countercontrol than the doubling map that r6 cites. With
    the doubling map, it has to be argued that the merged states agree in registered content.

### First missing step of the unit

The first step comes before any proof. Preregister three things:
- **(i) The observational inputs.** Lemma 1; injectivity on registered content (the record prong);
  Axiom 2.
- **(ii) The candidate class `P_w` of weaker premises, with the independent justification for each,**
  for example:
  - conservativity of a σ-finite quasi-invariant measure, as the measure form of Axiom 2;
  - an invariant probability, as the normalized prior that every rooted law needs.
- **(iii) The target statement.**
  - `φ` is a bijection of a full-measure invariant set.
  - `φ` is injective on states that differ only in the hidden sector.

The first mathematical step is then O1 written as a full paper proof. The open step that no route
yet covers is hidden-sector injectivity without A1. O2 shows that neither member of `P_w` above
supplies it.

### Controls, fixed in advance

**Finite control.**
- On a finite `X` with counting measure, conservativity is automatic and `X∞ = E`.
- The result reproduces Main:60 and `injective_imp_bijective` (CanonicalMeasure.lean:63).
- It reproduces Main:60's three-state example. There, counting measure on `E` is not doubly
  stochastic.

**Preservation.**
- Every F cell is unchanged.
- `S ⟺ D ⟺ Q_fb`, the readback lemma and Theorem 24(iii) are unchanged.
- AM-4 stays dependent on A1. Lemma 3's selection gains no counterpart.
- On the OBL class, where `F` is already bijective, the result gives `X∞ = X`.

**Countercontrols, each of which must fail at a named step.**
- `n ↦ n+1` on `N`: dissipative. It fails at conservativity.
- O2's `T`, the doubling map and the one-sided shift: they fail at injectivity on the hidden sector.
- A non-Borel map, or a non-standard space: it fails at the measurability step.
- The `Z` shift: it shows that conservativity is not necessary.

**Independent consequence.**
- At least one consequence is to be named before the proof. It must lie outside the bijectivity
  statement, and it must not be a restatement of it (§A.29).
- One candidate: almost every point returns to its positive-measure visible cell on I-meas and
  I-nonorm carriers (Halmos). This would bear on the 1.1 and 1.2 cells, but it is not exact return.

**Decision rule.**
- **Recovery.** A complete paper proof of both halves from (i) and one member of `P_w`, with every
  hypothesis labelled, plus the preregistered consequence.
- **Negative.** An explicit map that satisfies (i) and the chosen `P_w` member and is not injective.
  The record names that class as excluded. O2 is the expected candidate for the two classes above.
- **Partial.** Surjectivity alone is recorded as partial, with bijectivity open.
- No outcome is expected in advance.
- The premise is not chosen because it delivers bijectivity.

**Skepticism.** O1 is standard ergodic theory. Its value is the premise and the map, not the
argument. A negative on hidden-sector injectivity would show that A1 carries injectivity as well as
surjectivity. Neither outcome removes the posit, and neither moves correctness.

## Summary of required changes

- **K1.** Cite #1169 c.6894115930 in Standing, and restate §3's AM-3 entry in the owner's terms.
- **K2.** Add the consumers:
  - Main:588 and GR:266, census 21 and 22;
  - Main:145, census 35 and 36, together with the `Cut` section;
  - SM Theorem 22 (SM:1376, :52, :92), Theorem 19 (SM:643, `theorem_19`), and SM:44, :112, :22 and
    :1654;
  - census 32;
  - posit (ix) in AM-7.
- **K3.** State a structural recipe that can be rerun, and the map's completeness relative to it.

The six items that were asked about are applied. No result is withdrawn, and no status changes.
