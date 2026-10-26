BLOCK (wording only) — 587d419657404411cc662112829bcf50a32abd9f (PR #917, research/oi-bh-information-audit, package verification/programmes/black-hole-information/bh01_access_v1/)

The computations reproduce exactly, and so do the replay, the -O determinism, the checksums and the 10 of 10 mutants. The written proofs of Lemma 0, C1, C2, C3 (sufficiency), Lemma L and D1 are correct. Item F is confirmed independently: GR A.7's stated support for D-decoupling, τ_evap ≪ τ_B^D with τ_B^D ~ 1/H, is reversed at 30 M_⊙ by at least 10^57. The block is for one category of prose: necessary-versus-sufficient overclaims in REPORT.md, which MANUSCRIPT-AUDIT.md inherits. The package's own enumeration refutes them (AGENTS.md "Claim/evidence boundary: necessary → sufficient"). Further issues: the L155 falsifier proposal over-reaches, and the propagation list is incomplete. All fixes are textual. No computation has to change, except regenerating `verdict_text` if the overall label is reworded.

Reviewer: independent, read-only. Scratch outputs are in this directory: `indep.py`/`indep-output.json` (own exact enumeration), `itemf.py`/`itemf-output.txt` (own interval arithmetic), `revmut.py`/`revmut-output.json` (own mutants), `c3extra.py`/`c3extra-output.txt`, and `replay/` (recipe replay, logs). The clone worktree was not modified: `git status` is empty and HEAD is 587d4196 before and after.

***

## Ranked findings and fixes

### F1 — blocker (necessary vs sufficient). "Only under R1–R4" and "D can be removed from K only when the dynamics factorizes"

REPORT.md makes two necessity claims:

- "Recovery from the emitted records follows, in the tested class, **only under** (R1)…(R4)".
- "`D` can be removed from `K` **only when** the dynamics factorizes as `W x D`". The pressure-test paragraph repeats the claim: "the endpoint condition requires reading or decoupling `D`".

C1–C3 prove sufficiency only, and the package's own enumeration refutes the necessity claims:

- **Nested layout, W read at the endpoint, D never read.** 36416 of 40320 bijections recover exactly. Only 48 of these are product maps, so 36368 are not.
  - 36032 of the recovering bijections have explicit D→W back-action: the W-update depends on d (`c3extra-output.txt`). Example, encoding (V,B,D) → 4V+2B+D: the permutation [0,1,2,3,4,6,5,7].
  - The W-only reduction of C3 also holds whenever W is autonomous (G independent of d) with H arbitrary. Factorization is therefore not even necessary for C3's own conclusion. Example: [0,1,2,3,4,5,7,6], where D flips iff V∧B.
- **Moving-partition layout, one mode unread after two emissions.** 14496 bijections have δ = 1, so exact recovery occurs with an inaccessible remnant. R1 as worded ("no remnant, or a remnant … with C2 as the only guarantee") is always satisfied, so it is not a condition at all.
- **R3 and R4.** Neither is necessary in general. In the swap cascades, the shares need not be read jointly.

MANUSCRIPT-AUDIT.md defines its **conditions** class as "holds only under endpoint conditions R1–R4", so the overclaim propagates to every sentence classified "conditions".

**Fix:**
- Restate R1–R4 as **sufficient guarantees**: "under R1–R4, C1–C3 guarantee recovery. Without them, recovery is not guaranteed, and the enumeration exhibits failures (claim A, the C3 leak countercontrol)."
- State the necessary-side fact that is proved: the contrapositive of C2. No bijective instance has P_succ < 1/|K|.
- Rewrite R1 so it is not vacuous.
- Replace "only when the dynamics factorizes" with "when the W-dynamics does not depend on D (in particular, when it factorizes)". Optionally state C3 under that weaker hypothesis, since the proof is unchanged.
- Re-key the audit's **conditions** class as "holds under conditions the sentence does not state".

### F2 — moderate (§A.25 completeness). MANUSCRIPT-AUDIT.md omits sites that draw the same inference

Line numbers are at 809fac52:

- `book/ch09-universality.md` L108 [FULL L2580]: "Bijectivity is load-bearing because it preserves information at the substratum level (resolving the BH information paradox in Chapter 7 §7.6)". This is the most direct bijectivity ⇒ resolution inference in the corpus, and it is missing.
- `book/ch18-beyond.md` L158 [FULL L4970]: "…as if it should preserve substratum information (which it does, through the nested partition)". This attributes radiation-level preservation to the nested partition, which claim E shows carries no recovery content.
- `book/ch19-open-problems.md` L334 [FULL L5502], status table: "Resolved (Page curve from typicality)". It is a status surface and omits the H-scramble conditionality that ch19 L72 states.
- `book/ch18-beyond.md` L130 [FULL L4942]: "receive the *same* structural resolution". Minor.
- `book/ch09-universality.md` L127 is listed, but its FULL mirror (L2599) is not.

**Fix:** add these sites, with their FULL mirrors, to the propagation list.

### F3 — moderate (over-reach). The L155 falsifier proposal

The proposal reads: "Given complete evaporation with no remnant and the trans-cosmological sector decoupled, bijectivity requires the joint radiation record to determine the initial state…". Four problems:

- **(a) It misstates C1.** C1 needs every register read at the endpoint, which here means all of V. The joint radiation record alone is not enough: R4 is dropped. C1 also gives recovery of the message, not "the initial state" from the radiation.
- **(b) It moves a classical finite toy result into a physical falsifier** about quantum radiation.
- **(c) Its antecedent is the very premise item F shows to be unsupported.** That premise ("D decoupled") fails for every black hole above ~5×10^12 kg. Below the crossover, the only candidates are hypothetical light primordial holes. L153 itself says astrophysical evaporation is unobservable. The proposed falsifier therefore restores no testable content.
- **(d) It is presented as "derived from C1"**, which the report itself calls near-tautological.

**Fix:** do not offer it as a falsifier. Either:

- state that the section has no empirical falsifier for recoverability at present, or
- give the purely conditional logical statement with all four conditions. Those are full endpoint access to V, no remnant (or the C2 bound), D decoupled, and the joint record. Add an explicit note that the decoupling premise is presently unsupported (item F).

The diagnosis that the current sentence "can absorb any outcome" (§A.29) is right. Classifying it "unfalsifiable as stated" is more accurate than "contradicts".

### F4 — minor (finite → universal). "Zero accessible advantage exists whenever some register is inaccessible"

This statement appears in the PLAN claim A wording and in MANUSCRIPT-AUDIT.md's L12 entry. It is false in the P_succ = 1/|M| sense whenever |K| < |M|. By C2, P_succ ≥ 1/|K| > 1/|M|, and the package's own MP2 run finds 0 of 40320 bijections at the blind value 1/4.

**Fix:** say "whenever the inaccessible endpoint set has at least |M| joint values (for a binary message: whenever any register is inaccessible)", or "in the tested classes".

### F5 — minor (clarity). The overall verdict label

"Overall: HOLDS_WITHIN_SCOPE (each claim is the plan's hypothesis)" is technically correct, but it invites the reading "the framework's resolution holds". Claim A, the headline, is a non-implication.

**Fix:** generate an overall line such as: "All preregistered hypotheses A–E confirmed in the tested finite classes. Headline: bijectivity does not imply accessible recovery (counterexamples), nor is it necessary for it." Tag each claim in the programme's own vocabulary (PROGRAMME.md acceptance criteria):

| claim | tag |
|---|---|
| A | COUNTEREXAMPLE (to "bijective ⇒ recoverable" and to its converse) |
| B | demonstrated examples |
| C1, C2, C4, D1 | PROVED (written proof, exhaustive finite check) |
| C3 | PROVED for sufficiency only |
| D2 | COUNTEREXAMPLE |
| E | PROVED (an identity) |
| F | audit observation |

### F6 — minor (classification strength). L12 and L139 are marked "contradicts"

Both sentences rest on bijectivity *jointly* with the Page curve, H-scramble or mode counting, and the audit itself places those outside BH-01.

**Fix:** "not supported by the bijectivity clause alone". L110 sentence 2 ("resolves … because φ is bijective") is fairly marked.

### F7 — minor (§A.21/§A.41). Item F has no control and no mutant

My mutants:

| mutant | effect on the verdict |
|---|---|
| M³ → M² dimension error | unchanged, "contradicted" |
| swapped G bounds | unchanged, "contradicted" |
| t_evap divided by M³ | caught: status becomes "undecided" |
| τ read as 10^80 s | caught: status becomes "undecided" |

The verdict survives by ≥ 57 orders of magnitude, and my independent recomputation agrees, so the conclusion stands. But the NEW finding that bears on a published paper rests on unguarded arithmetic. Two further points:

- The intervals Γ ∈ [1/100, 1000] and τ ∈ [10^16, 10^19] were fixed after the plan. This is immaterial given the margin.
- `sci()` truncates the *upper* bounds downward, so the printed upper bounds are not rigorous. The lower bound and the crossover bounds are conservative.

**Fix:** add a reference-value control. With Γ = 1 at 1 M_⊙, the formula gives 2.10×10^67 yr, the textbook value (reproduced in `itemf-output.txt`). Add a dimension check, and round printed upper bounds up.

### F8 — nit. The C1 "dropping complete access gives 5280 failures" count is a mixture

5280 = 1376 MP1 instances with δ = 0 at t = 2, plus 3904 nested instances not recovered with W read. The MP1 instances failing exact recovery at t = 2 number 25824.

**Fix:** label the two parts, or count failures of exact recovery consistently.

### F9 — nit. "49 transport models"

These are three parametric families plus one aggregate: swap with 30 settings, wide-alphabet swap with 8, CNOT with 10, and the GL(4,2) B3 item, which is implied by C1.

**Fix:** say "three families, 49 parameter settings".

### F10 — nit. Claim E is an identity for every map, not only bijections

The `nested_assoc` check sums the same terms in two orders, which is close to "merely reproduces the claimed formula" (AGENTS.md). The CONFIRMING classification and "carries no recovery content" are right.

**Fix:** say "holds for every map (Fubini); the enumeration only exhibits it on the zero-advantage instances".

### F11 — nit. The D1 control and the claim check share `nondecreasing()`

A vacuous `nondecreasing()` survives every package control (my RM4). It would, however, flip D2 to NEGATIVE in a full run, so the overall verdict would expose it. No change is needed. Optionally, give the D1 control its own comparison.

### F12 — reviewer observations on GR, outside the package's claims, for the Page/gravity lane

- **Error term.** The proof of Theorem A.7 bounds the error by O(τ_S/τ_B^D), independent of t. A.5(i) derives the frozen-D correction as O(t/τ_B^D), which accumulates. Inside A.7's own window, t ≪ τ_B^D ≤ 10^19 s, the black hole has lost at most t/t_evap ≲ 6×10^-58 of its mass (Γ ≤ 1000), so the Page curve's turnover lies wholly outside that window. My bound: t_P/τ_B^D ≥ 1.15×10^57.
- **Coupling chain.** A.5's chain V↔B↔D ("no direct V–D coupling") matches the boundary-layer/deep-sector notation used elsewhere: FULL L785 has C_B as the boundary layer and C_D as the deep sector, with τ_B^D the deep sector's coupling time. A.1, and A.5's own numbers (τ_B^B ~ τ_scr of the black hole), make B the black-hole interior. With that geometry, locality gives B↔V↔D. The audit's question is well posed. My reading is that the two meanings of B are conflated, which is an assumption-watch marker.

***

## Evidence per check

### 1. Preregistration — pass, with F5

- **Commit order.** faf90280 is PLAN.md alone, parent 809fac52, committed 08:23. The results commit 436be700 follows at 08:59. The PLAN blob d8326165 is unchanged through 587d4196.
- **Decision rule.** `decide()` implements PLAN §4 as written:
  - A adds one extra conjunct (`swap_into_remnant` δ = 0), which is stricter, not weaker.
  - Every required countercontrol finds a violation: C1 172/5280, C2 32, C3 leak δ = 0, D2 21632.
  - The item F rule (lower bound > 1 ⇒ contradicted) is exact.
- **Deviations.** All are declared and none weakens a control:
  - K6 is measured outside `checks.py`. My replay confirms it: byte-identical under -B and -B -O.
  - The K5 mutant changed. The justification is correct: a uniform +1 cancels in rank G_t − rank C_t.
  - The GL(4,2) analytic counts are labelled post-run. I verified the formulas: 1344, 10752, 576 and 9216.
- **Not determinable from git.** Whether the deviations predate the verdict cannot be read from history, because the deviations and the verdict arrive in one commit. The intervals for item F are post-plan (F7).
- **Exit-144 incident.** It is recorded nowhere in the package. It is immaterial because the full replay matches. Note it on the PR checkpoint.
- **Verdict wording.** See F5.

### 2. Proofs

- **Lemma 0.** Correct, and definitional, as the report says.
- **C1.** Correct, and near-tautological; the report says so honestly ("Pressure test"). It is the |K| = 1 case of C2.
- **C2.**
  - The proof is correct: s has fibres of exactly |K| points, ρ_T refines s, ρ_T takes at least |I|/|K| values on I, and each value contributes at least 1.
  - The entropy corollary is correct.
  - Tightness is correctly reported as attained (2368 instances at 1/2).
  - It is a known fact: guessing probability rises by at most a factor |K| with |K|-valued side information, the min-entropy chain rule, which is the remnant-capacity argument. The report identifies it correctly ("known information-theoretic facts", ELABORATING).
- **C3.** Correct as a sufficiency statement. The hypothesis is stronger than needed (W-autonomy suffices). "Only if" is not proved and is false (F1).
- **Lemma L / C4.** Correct. y is uniform on the coset A_t m + Im C_t, so r_t = t − rank C_t and the bounds follow. It is the linear secret-sharing / wiretap threshold, correctly identified as known.
- **D1.** Correct: a refinement inequality for P_succ, and data processing for TV. Cumulative records alone suffice; the plan's nondecreasing-access hypothesis is not used.

### 3. Exact re-derivation

`indep.py` uses its own code and a different bit encoding (invariant by conjugation). It runs on exact integers/Fractions. Every number matches result.json exactly:

- **MP1 δ at t = 2:** 0/½/¾/1 = 1376 / 12672 / 11776 / 14496.
- **Nested δ at t = 3:** 2688 / 10944 / 26688.
- **All 256 maps of {0,1}²:**
  - Complete access: 24 bijective and recovering / 60 non-injective and recovering / 172 non-injective and failing. Analytic check: 84 maps recover in total.
  - C2 countercontrol: 0 bijective / 32 non-injective violations. Analytic: 2·2⁴.
- **MP2 P_succ at t = 2:** minimum ½, attained by 2368; none at ¼. Histogram {½: 2368, 5/8: 768, ¾: 21120, 7/8: 5888, 1: 10176}. C2 violations: 0.
- **GL(4,2):** 20160 matrices. Full profile histograms for k = 1 and k = 2 identical, including 10752 / 1344 and 9216 / 576.
- **D2:** 21632 bijections with decreasing snapshot δ. Example [0,1,2,4,3,5,6,7], δ = 0, ½, 0, ½. Swap-in/swap-out: snapshot 0, 1, 0; cumulative 0, 1, 1.

### 4. Item F — confirmed; this is the highest-priority result

**What GR A.7 says.** It reads (GR.md L817): "The trans-cosmological sector D is frozen on evaporation timescales (τ_evap ≪ τ_B^D), so by Theorem A.5 … D decoupled". A.5 (L787) gives τ_B^D ~ 1/H ~ 10^17 s for the 30 M_⊙ case. FULL L565 gives τ_B ~ H^-1 ~ 10^18 s.

**Is this the right comparison?** Yes. A.5(i)'s own frozen-D correction is O(t/τ_B^D), so the frozen-D approximation needs t ≪ τ_B^D over the whole evolution. Reading A.7 against any other timescale would mean redefining τ_B^D against A.5's explicit value. In pure de Sitter one could argue the horizon is static; that would be a new, unstated premise.

**My recomputation.** I used `itemf.py` with exact rationals, independent constants (h exact, so ħ from π ∈ [333/106, 355/113]; G ∈ [6.6740, 6.6746]×10^-11; M_⊙ ∈ [1.9884, 1.9890]×10^30 kg), and t_evap = 5120πG²M³/(ħc⁴Γ), which matches A.7's α.

| quantity | result |
|---|---|
| Γ = 1, 1 M_⊙ (reference) | 2.10×10^67 yr, the textbook value |
| t_evap, 30 M_⊙, Γ = 1 | 1.785×10^79 s |
| ratio, τ = 10^17 s, Γ = 1 | 1.79×10^62 |
| ratio, Γ ∈ [1/100, 1000], τ ∈ [10^16, 10^19] | [1.785×10^57, 1.787×10^65] (package: [1.70×10^57, 1.78×10^65]; its looser π gives the smaller lower bound) |
| crossover mass, same ranges | [1.059×10^10, 4.92×10^12] kg (package: [1.05×10^10, 4.99×10^12], conservative) |
| crossover mass, Γ ∈ [1, 20], τ ∈ [10^17, 10^18] | [1.06×10^11, 6.2×10^11] kg |

Standard greybody/species factors for stellar masses, of order 1–10, lie well inside Γ ∈ [1/100, 1000].

**What item F shows.** It removes the stated support for treating D as decoupled over the evaporation. It therefore removes the support for applying Theorem A.7, and through it A.9, out to t_P = 0.646 t_evap, and for the recovery premise R2.

**What it does not show:**
- that information reaches D;
- that Theorem A.7 is false within its stated scope t ≪ τ_B^D;
- that no other decoupling argument exists.

The report says this correctly ("it does not show that information reaches D").

**Coupling chain.** See F12.

### 5. Faithfulness and scope — fair, with additions

The moving-partition layout (modes read one at a time as they become R) and the nested V/B/D layout with a hidden-uniform prior are fair finite formalizations of A.7, A.1 and A.2, and of PROGRAMME lane 1. The stated limitations are present: classical messages, no back-action, no black-hole physics, maps not derived from the OI wave equation, quantum/Page material out of scope.

Limitations to add:
- The generic maps impose neither A.5's locality chain nor A.8's energy-shell conservation.
- Access means full-register reads on fixed schedules. Coarse-grained or adaptive measurement protocols, which PROGRAMME lane 1 mentions, are not covered.
- Short horizons (T ≤ 3–4) with time-homogeneous maps in the S_8 classes.
- A uniform message prior with equal-size supports.

### 6. MANUSCRIPT-AUDIT.md

**Quotes and lines.** Every quoted sentence was checked at 809fac52 and is verbatim at the stated line:

- ch07 L12, L110, L112, L118, L124, L139, L151, L153, L155;
- ch18 L146, ch19 L72, ch09 L127;
- GR L761, L811, L817, L819.

Each ch07 line, and ch18 L146 and ch19 L72, is byte-identical to its FULL mirror at the stated line (1887, 1985, 1987, 1993, 1999, 2014, 2026, 2028, 2030, 4958, 5240).

**Classifications.**
- The "supports" items are right.
- The "conditions" class is mis-keyed (F1).
- L12 and L139 are marked "contradicts" too strongly (F6).
- L155's diagnosis is right, but its proposal over-reaches (F3).
- Missing sites: see F2.
- The GR dependencies are correctly flagged as outside scope, with the right item F statement.

### 7. Controls and mutants

The package's 10 of 10 mutants are each caught on their named case (replayed). My mutants, in `revmut.py`:

| mutant | result |
|---|---|
| C2 bound ½ → ¾ on all 2-bit maps | detected: 24 bijective violations |
| GL(4,2) C2 bound ×2 | detected: 76416 violations |
| snapshot records on the all-maps D1 enumeration (not only the named example) | detected: 36 violations |
| `nondecreasing()` made vacuous | survives the controls (F11) |
| item F mutants | see F7 |

The C2 and D1 checks are therefore not vacuous. Item F is unguarded but robust.

### 8. Replay and hygiene — pass

- **Recipe.** Run as written from an empty directory, using `git show` per file. `sha256sum -c` gives OK for all 8 files.
- **`checks.py` (-B).** Exit 0. result.json is byte-identical to the committed file.
- **`checks.py --out o` (-B -O).** Byte-identical (`cmp`).
- **`mutants.py`.** Caught 10 of 10, exit 0. mutants-output.json and the checksums still verify afterwards.
- **Timing.** Wall times were 3.6 min under load from my parallel runs (65 s user).
- **Scan.** No absolute paths, secrets, e-mail addresses or session paths in the package. The commits touch only the package directory and carry the attribution trailers.
- **Repository tools.** `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py`, run read-only from the clone root, all print OK. Placement under `verification/programmes/` conforms to §A.36.
- **Worktree.** Unchanged before and after: `git status` is empty and HEAD is 587d4196.
