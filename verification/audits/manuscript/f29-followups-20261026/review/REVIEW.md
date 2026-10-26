# Independent review: PR #938 (`fix/f29-followups-20261026`, commit `2b660c93` on main `c967d6a9`)

**Verdict: REVISE.** One line needs changing. Both corrections the owner asked for are mathematically right and mechanically clean. The one blocking item is the incidental rewording at Explainer:373: read literally, "No three-way biconditional holds" is false (Finding 1). The owner asked specifically that this sentence be correct as a mathematical statement. Everything else can be accepted as it stands. Finding 2 is a recommended same-PR edit or an owner sign-off, and the rest are nits or out-of-scope observations.

All work was read-only. Snapshots: `git archive` of `2b660c93` and `c967d6a9` in `S/f29b/{snap,base}`, and the audit directories via `git show` (they are `export-ignore`). Remote check: `fix/f29-followups-20261026` = `2b660c93` and `main` = `c967d6a9`. The PR is one commit, and `c967d6a9` is its parent.

## Item 1: witness-anchoring the every-horizon statements

**Exact match to Main.** Main:522 (iii) reads: "for some accessible order k and every finite accessible horizon K ≥ k+1 … (C1), (C3), (C4) history readback at k". The prose of all three corrected sites has the same ∃k ∀K≥k+1 structure:
- Explainer:373;
- appendix-b:454;
- FULL:6221.

Each also has the same condition set, C1, C3, C4 with C2 outside, and the same anchor, readback at k. The display at appendix-b:455 / FULL:6222 is the same formula. None of them is stronger or weaker than Main. The only thing left out is Main's parenthetical "the hidden space may grow with the horizon". That costs nothing: "on each horizon it arises from marginalizing a deterministic bijection" is already per-horizon, and the fixed-φ reading is also true (Finding 4).

**The drafter's failure claim is confirmed independently and strengthened.** My probe is `S/f29b/probe/review_probe.py`, in exact rationals. It passes, and a deliberately broken Markov control was caught, which incidentally confirms the detector fires.
- Process P is a *stationary, time-homogeneous* law, so it is inside the theorem's class: the GF(2) shift register X_{n+1} = X_{n−2} ⊕ X_n. A fixed bijection φ(x,(a,b)) = (a⊕x,(b,x)) on {0,1}³ with a uniform prior realizes it. The drafter's L is a restriction of P.
  - P has M_0 = M_1 = 0 and M_t = 1 bit for t = 2…5. The best gap has p0 = 1/8 and δ = 1, and the readback bound holds at every witness.
  - On horizons K = 1 and K = 2 there is no (C4) gap at any order ≤ K−1. The unrestricted "each finite accessible horizon" form is therefore false for this non-Markovian law.
  - For K = 3…6 the anchored form holds with k = 2.
- K = 1 fails for *every* law, because a gap needs k ≥ 1 and k+1 ≤ K. So no hypothesis at any site could have saved the literal every-horizon form. The only true strong form is the per-witness statement at Main:610, which stays in Main.
- I checked every corrected site and found no extra hypotheses. The Explainer adds only |C_V| ≥ 2. Appendix B adds only "in the form of [Main §3.4]".

**Both directions, checked independently:**
- (iii)⇒(ii). The (C4) gap is defined on visible next-step conditionals (Main:80, :167). By pushforward (a) (Main:584, Lean `pushforward_identity`) it is a gap in 𝒮's own conditionals, and the readback lemma at K = k+1 gives CMI ≥ p0δ²/ln2 > 0.
- (ii)⇒(iii). The dilation at each K ≥ k+1 (Main:500, :608) reproduces the K-law, which contains the k-witness. #932's `acceptance.py` re-ran with exit 0, and its output is byte-identical to the block in `f29-witness-quantifier/result.md` (sha256 `c04f737a…`). `c4_backflow_probes.py` Q4 also passes.
- Non-vacuity. For a Markov law both sides are false: my control M is a 6-cell coin ring with no witness and no gap at orders 0–5 through K = 6. The K-range {K ≥ k+1} is nonempty.

**Display.** The three-line `aligned` display at appendix-b:455 / FULL:6222 renders correctly. I checked FULL.pdf p. 502 by rendering it to an image: the lines are aligned on ⟺, nothing is clipped, and the content is identical to the prose.

## Item 2: history length in the readback lemma (Main:167, :170)

- **The new reading is right.** p and p′ are values of X_{<k} = (X_0…X_{k−1}), followed by the present X_k = c, with p0 bounding Pr[X_{<k}=p, X_k=c]. Every step of the proof then type-checks:
  - w_a = Pr[X_{<k}=a | X_k=c];
  - Pinsker in bits;
  - Pr[c]·w_p = Pr[p,c] ≥ p0;
  - the result 2/ln2 · p0 · δ²/2.
- **Invocations are consistent:**
  - :608 and :717 use only the conclusion I(X_{<k};X_{k+1}|X_k);
  - :163 is the lower-bound remark;
  - :582–:592 write P(·|p,x) with μ_p = P(H_t | X_{<t}=p, X_t=x);
  - :99 defines M_t;
  - the per-witness form at :610 is anchored at K ≥ t+1.
- **"Readback lemma at K = k+1"** is consistent: X_{<k}, X_k and X_{k+1} all lie in (X_0…X_{k+1}).
- **Lean (read only).** `OIBridge/HiddenMemory.lean:65–74` has `histProb p x = P(X_<t = p, X_t = x)` and `nextLaw p x = P(X_{t+1} | X_<t = p, X_t = x)`. That is the same convention. `verification/lean*` has a zero-line diff.
- **The drafter's probe** (`readback_indexing_probe.py`) passes 12/12. Its argument holds:
  - for L at k = 2, the full past X_{<2} gives δ = 1 and p0 = 1/8;
  - the 2-entry window (X_1,X_2) ending at the present gives δ = 0;
  - the controls behave correctly.
  - The probe's "suffix" past is `traj[1:k]`, which together with the present is the length-k window. That is correct.
- **Independent corroboration the drafter did not cite.** Main:165 says the fastbath shift register "supports a maximal order-2 gap". I recomputed `fastbath_probes.py`'s construction:
  - the gap first appears for 3-entry histories including the endpoint, which is order k = 2 under the X_{<k}, X_k convention;
  - under the old literal "length-k history with a common endpoint" reading it would be order 3.
  - The corrected :167 therefore makes :165 consistent.
- **The fast-bath lemma (Main:159) needs no change for item 2.** It states no history length. Under the corrected convention, a record distinguishing pasts that differ at X_0 is eroded over k steps before X_{k+1} is read, so δ_0e^{−(k−1)τ_S/τ_B} remains a valid (one-step loose) upper bound. It has a separate, pre-existing weakness (Finding 5).

## Search

I spot-checked SEARCH.md's O/C/U classes and ran my own greps:
- "each/every/per/all/any (finite)(accessible) horizon/window" near C1/C4/realiz/characteriz/⟺;
- hyphenated "finite-horizon", "each/every/all K";
- GR, Substratum, Methodology, Bioinformatics, Complexity, every book chapter, and the glossary.

I found no missed every-horizon or per-horizon characterization claim:
- GR:20 and glossary:39 are already anchored.
- Every "every finite-horizon law" hit is the representation equivalence S⟺D⟺Q_fb, which is true on every horizon. That includes Methodology:45, which SEARCH's patterns do not match because of the hyphen; it is harmless.
- The readback lemma's hypothesis has no paraphrase elsewhere. Explainer:1006 says "two histories with the same present", which is consistent.

## Mechanics

- **FULL mirror.** appendix-b:440–470 is byte-identical to FULL:6207–6237. `mirror_check.py` reports 0 lines absent.
- **Regenerated `.tex`.** Main, Explainer and FULL `.tex` regenerated with the given pandoc command are identical to the committed files, except for the build.sh `% source-sha256:` stamp line. Each stamp equals the sha256 of its committed `.md`.
- **PDFs** contain the new text. Page counts are Main 90, Explainer 69 and FULL 555, all unchanged.
- **Checks.** These all report OK:
  - `claims_check`, `voice_check`, `duplicate_check`, `staleness_check` (13 matched);
  - `lean_manuscript_census`, `artifact_placement_check`;
  - `architecture_check` (259 invariants, 0 violations);
  - `c4_backflow_probes`, `fastbath_probes`.
- **§A.32/§A.33 scan** of the 7 added manuscript lines (history phrases, meta and reader-instruction phrases, mid-sentence `[A-Z]{4,}`) has 0 hits.

## Findings

1. **Medium (blocks acceptance; one-line fix).** The sentence at Explainer:373 "No three-way biconditional holds:" is not true as an unqualified mathematical statement.
   - The same paragraph has just asserted a three-way biconditional that does hold, $S \iff D \iff Q_{\mathrm{fb}}$.
   - The old sentence pointed back to a specific retired biconditional, QM ⟺ P-indivisibility ⟺ embedded observation (Explainer at `86f64125^`, :392). The new one quantifies over all three-way biconditionals.
   - CHANGE-NOTE's claim that "the mathematical content is unchanged" is therefore inaccurate.
   - **Exact fix:** replace `No three-way biconditional holds:` with `No two of representability, memory and P-indivisibility are equivalent:`. The two counterexamples that follow, together with "P-indivisibility forces representability but not conversely", establish all three non-equivalences.
   - Then rebuild Explainer `.tex`/`.pdf` with `sh ./build.sh Explainer`, and correct the CHANGE-NOTE sentence.
   - The replacement has no §A.33 trigger words.
2. **Low (fix in this PR, or get explicit owner sign-off).** Explainer:353's "Combined:" line reads "accessible non-Markovianity ⟺ embedded observation under C1, C3, C4 (per finite accessible horizon)".
   - Its wording is essentially the old B.7.6 display, "… with C1, C3, C4, per finite accessible horizon". This PR classes that display as outdated, but classes :353 as correct.
   - :353 is a theorem statement 20 lines above the corrected :373, not a section pointer. It is not false: the horizon-local reading and the existential "per-horizon realization" reading are both true. But "per" invites the every-horizon reading the owner asked to remove.
   - **Exact fix:** `(per finite accessible horizon)` → `(for some accessible order k, on each finite accessible horizon K ≥ k+1, with the readback at k)`, then rebuild Explainer.
   - The other "⟺ C1/C3/C4 realization per accessible horizon" slogans can stay, since "per" there is used adjectivally of the realization, as in Main:614 and :616. SEARCH.md already flags them as borderline for the owner.
3. **Nit (record only).** VERIFY.md says the old hypothesis "names the wrong object, by one position". That overstates it. The corpus's own idiom of a history p "ending at x" / "sharing the endpoint x" with P(·|p,x) (Main:99, :586, :592; Lean's "weight of a history with its endpoint") admits the correct reading of the old text. More precisely, the old text was ambiguous in two places: the length and the endpoint, and whether p0 bounds Pr[p] or Pr[p,c]. The edit resolves both. No manuscript change is needed. Optionally, reword the VERIFY sentence to "admits an off-by-one reading and leaves p0's event unspecified".
4. **Nit (no change needed).** In the display, "(S, φ)" is not indexed by K. Both readings are true:
   - per-horizon realizations, by the dilation;
   - one fixed faithful φ, by the universal theorem. (C4) coincides with (ii) in every faithful realization (Main:596), and (C1) and (C3) follow from it (Main:604). P above is an instance.
5. **Out of scope (follow-up Issue recommended).** The fast-bath lemma at Main:159 defines neither δ_0 nor δ_k and gives no proof.
   - If δ_k means the maximal order-k gap (the only definition in the paper, :167), the (k−1)-exponent is unsupported under either convention. A fixed-delay register such as P has an order-k gap that is constant in k, so under uniform erosion it does not decay with k.
   - The lemma needs δ_k to be defined as the gap carried by pairs differing at the oldest entry, or the k-dependence should be dropped. The qualitative conclusion, that (C4) fails for τ_B ≪ τ_S, survives with exponent 1.
   - This predates the PR and is untouched by it.
6. **Out of scope (follow-up Issue recommended).** Two places present I(X_{<t};X_{>t}|X_t) ≥ I_0(1−kτ_S/τ_B) as following from storage and persistence alone:
   - Explainer:179–191;
   - book ch01:125–128 (and its FULL mirror).

   Main:172's coin is a counterexample if I_0 is the written information: its ledger records with a static bath, yet I = 0. Main:155 says "storage is not backflow". The bound needs I_0 to be the read-back information, which is a C4 hypothesis.
7. **Out of scope (note).** Main:163 "LOWER" and :165 "PERSISTENCE" are pre-existing §A.33 caps emphasis beside the edited lemma. They are not in this diff.

## To reach ACCEPT

1. Apply the one-line fix in Finding 1.
2. Either apply Finding 2 or record the owner's sign-off on keeping :353.
3. Rebuild Explainer `.tex`/`.pdf` and update CHANGE-NOTE (and SEARCH.md's class for :353 if it changes).
4. Re-run the added-lines scan, `voice_check`, `claims_check` and `staleness_check`.

No other changes are needed.
