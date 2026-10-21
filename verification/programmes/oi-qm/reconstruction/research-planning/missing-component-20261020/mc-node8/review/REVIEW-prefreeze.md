# Node 8 preregistration: independent pre-freeze review

- File reviewed: `mc8/PREREG.md`, 957 lines, sha256 `86d06afd17b87ef1761f7b198a5871cb68af42b902527c35c22418af76869c64`
  (hash re-verified). Line numbers below refer to this exact file.
- Corpus: worktree `mc8w`, detached at `a501b418`. `papers/`, `book/`, `FiniteEntropy.lean` and `C3Necessity.lean`
  are identical at `a501b418`, at `37e55457` and at current `origin/main` (`4546099f`). The only difference between
  the first two is the `KTokenMaxCone.lean` addition, as §0 states.
- Earlier drafts were diffed: `.PREREG.rev1.md` and `.PREREG.rev2.md`.
- Nothing was computed under any candidate. The only things run were:
  - `quotecheck.py`;
  - `git` and text searches;
  - hand checks of the lemma, the bridge algebra, the CC-dec control, the K-PR6 / RAC algebra, the TB realization,
    and the C5 ⇒ IC identity chain.

## Verdict: REVISE

The file is close. It meets most of the owner's requirements concretely. Its mathematics is right except for one
saturation sentence, which is wrong. Its controls are mostly built from their own models. Nineteen changes are
blocking:
- one is a mathematical error (1);
- one is a misattributed identity in the very place Round 3 item 4 targets (2);
- several are decision rules that are incomplete or adjustable after the fact: the H-C5 verdict table and its
  precedence, the domain 𝔇, the K-PROG variant set, V's dependence on K, the H-X verdict, and the productivity test;
- one is an underspecification of K-PR6 itself, the wing assignment of its visible preparer cells. This could
  manufacture a spurious favourable K-PR6 line.

Each blocker is small to fix. None requires a computation.

***

## Blocking changes

1. **The saturation condition in the quantum bound is wrong (l. 441–442).**
   - The text says "equality needs a pure marker and no further decoherence". That is false.
     - Counterexample: an uncoupled marker in state I/2 with path |+⟩. Both conditional marker states are I/2, so
       F_q = 1, and V = 1. Equality holds with a mixed marker.
     - In general, V = F_q holds iff the path-coherence block saturates the operator Cauchy–Schwarz (fidelity) bound.
       A pure joint path–marker state is sufficient for this, not necessary.
   - Replace the sentence with a correct sufficient condition, or delete it. Node 8 asserts no saturation anyway
     (l. 442–443, I-33).
   - l. 463 ("These are the pure-marker, no-further-decoherence points") is fine as a description of the chosen
     witnesses, provided it is not read as a necessity claim.
   - The rest of the bridge is correct:
     - B-VF is stated as an inequality;
     - the step V ≤ inf_R F_R ⇒ D² ≤ 1 − F_{R*}² ≤ 1 − V² is correct;
     - V ≤ F_q holds by positivity of the joint path–marker state;
     - the fidelity is the infimum over POVMs, and some POVM attains it.

2. **(I9) is attributed to (I1) alone; it needs (I2) (l. 260, also l. 277).**
   - (I1) conditions only the second argument.
   - Splitting X = (X_1 … X_N), the first argument, needs this identity:
     𝓘(X_≤i : BM) − 𝓘(X_<i : BM) = 𝓘(X_i : BM | X_<i).
     That is (I2) with A = X_i and C = X_<i.
   - So "from (I1) applied repeatedly" is the definitional-chain-rule fallacy that Round 3 item 4 excludes.
   - Fix (I9) to read: "from (I1) and (I2) applied repeatedly".
   - Also list, as their own checkpoints, the composite identifications that C5-S2, S3c and S4 use: X_i X_<i ≅ X_≤i,
     and BM ≅ MB.
   - In (I5) (l. 255–256), state that discarding a subsystem of a composite is an allowed local operation. C5-S2 needs
     exactly that: dropping X_<i from B M X_<i.
   - The conditional form of (I5) ("where the proof uses it") is not used by C5-S1 to C5-S4 as written. Either cite
     the step that uses it or drop it.
   - My reconstruction of the chain is otherwise correct:
     - S1 uses (I6) and (I5);
     - S2 uses (I9) [needing (I2)], (I1), (I8) for I(X_i : X_<i) = 0, and (I5) for discarding;
     - S3a uses (I8), with D-2;
     - S3b uses D-3, with (I5) and (I4) giving equality;
     - S3c uses (I1);
     - S4 uses (I1), (I2), (I4) and (I7).
   - Pawłowski's three ingredients are all present in C5-S2 and C5-S1: input independence (D-1/I8), the chain rule
     over inputs (I9), and data processing for Bob's guess (I5).

3. **IC-D4 omits input independence (l. 517).**
   - Σ_i I(a_i; Y) ≤ I(a⃗; Y) needs independent a_i.
   - IC-D4 cites only "chain rule [W]; P8 (iv), O3". Add B-2 (and D-1) to its premises column.
   - This is the owner's explicit check: "Pawłowski's proof also uses I(X_i : X_j)-independence".

4. **The H-C5 verdict table is incomplete, its rows are not mutually exclusive, and its precedence against §13 is
   unfixed (l. 332–340, 810–819, 938).**
   - (a) Rows 1–2 cover only N-ont and N-acc. There is no row for P-pq or P-ms failing, although l. 815 prints
     "construction fails" per route. Replace them with one generic per-route row.
   - (b) K-ONT's positive outcome has no row (l. 311–313, 737). The outcome is two realizations with equal accessible
     laws but different 𝓘_ont. Add a row such as "N-ont is not a quantity of the operational theory".
   - (c) Row 1's "fails C5-S3 on a model that meets the chain's assumptions" is near-contradictory. C5-S3b is D-3
     restated for the declared B. State instead: "C5-S3b fails for N-ont's hidden-cell B on a model whose
     operational B satisfies D-3".
   - (d) Scope row 3 to the preregistered routes and amendments: "no construction among N-ont, N-acc, P-pq, P-ms (and
     amended routes) …".
   - (e) Rows 4 and 5 can both fire: C5 established on a classical 𝔇, and an obstruction from K-PR6. Fix a rule for
     the joint case.
   - (f) Map every row to a §13 class.
     - Only "Undetermined → Parked" and "OI does not imply C5 → Failure" are fixed.
     - The class for "C5 established on 𝔇" is unfixed, and §13's Emergence clause (l. 792–794) names no H-C5
       target.
   - (g) Precedence puts Parked first (l. 819). Parked includes "an undecided route the class depends on" (l. 812).
     - State that an established obstruction decides the H-C5 line whatever the undecided construction routes show.
       An existence claim is refuted by one obstruction.
     - State that "C5 established on 𝔇" decides it on 𝔇 whatever the other routes show.
     - Without this, a Parked P-ms would mask a decided obstruction.
     - Node 7's precedence carried "if … prevents a decision" (MC7 PREREG l. 629). Restore that qualifier generally.
   - (h) Extend I-36 to test one mapping per row, including the joint case.

5. **The domain 𝔇 is chosen at execution, so the favourable row is adjustable (l. 340, 816–817, 872).**
   - "C5 established on domain 𝔇", with 𝔇 declared afterwards, is satisfied trivially by a classical domain. K-C5+
     (l. 739) already shows that.
   - That result then makes the correlation lines "eligible for Emergence on 𝔇" and counts as a gem.
   - Fix, now, either:
     - a minimum domain that 𝔇 must contain: at least K-PR6 (with its copies and wirings), 𝒟_LE, 𝒟_RT and the
       classical controls; or
     - the rule that any exclusion effected by the choice of 𝔇 is typed as an added axiom. The K-PR6 line then reads
       "rejected only by the added axiom (domain restriction)", which is Conditional at best.
   - Require D-1 to D-7 to be checked on 𝔇 before "IC derived on 𝔇" can print (l. 340).
   - Make "C5 established" on a domain containing no post-classical correlations a non-gem (l. 872).
   - Freeze the operational interface the measure is defined on: systems, states, allowed local operations including
     discarding, and composites (l. 240–241). The phrase "the operational theory that OI generates" is otherwise
     defined at execution.

6. **"Excluding PR boxes: yes" is stated unconditionally (l. 350–351).**
   - C5 excludes PR only where D-1 to D-7 hold. C5-0 (l. 306–309) explicitly contemplates their failing on K-PR6.
   - Write: "yes, wherever D-1 to D-7 hold". This is a conditional → unconditional boundary.

7. **B and its slices are underdefined, so IC-D5a can fail definitionally (l. 135–136, 284–287, 506–509, 518, 936).**
   - (a) IC-ont's B_{t₁} is "every cell in the backward cone of Bob's guess pointer … except M's cells and Bob's
     input".
     - Under P9 that cone contains Alice's setting cell. In K-PR6-RAC, r ^= a·b reads a = x₀ ⊕ x₁.
     - §2 makes inputs part of the visible point mass from t₀ (l. 135–136). So the same cells at t₀ already carry a⃗.
     - IC-D5a, I(a⃗; B_{t₀}) = 0, would then fail by construction. That is exactly the confusion KM-20 and I-35 forbid,
       and it conflicts with I-35's rule that IC-D5a is "evaluated from O3 and the prior alone".
   - Fix:
     - define B_{t₀} explicitly as the resource cells (hidden and Bob-side cells, excluding every input and setting
       register);
     - state that Alice's input or setting cells entering Bob's cone are recorded as mode (i) at IC-D3, or mode (ii)
       at IC-D5b, never at IC-D5a.
   - (b) The slice t₁ differs between §5.2 and §8.1. Line 285–286 has "before the message arrives"; line 506–507 adds
     "or Bob's input acts". Unify them.
   - (c) For the C5 routes, mode (i) can show at C5-S1 as well as at C5-S3b, mirroring IC-D3. This happens when
     G_i's production reads Alice's cells after t₁, so it is not a local operation on (B, M). Add C5-S1 to the failure
     sites in l. 313–316 and l. 287.
   - (d) Fix, now, the B used in K-PR6-C5 / C5-0 (l. 306–309, 741). The C5 measure lives on the operational theory,
     so the natural choice is Bob's box half as an operational system. The C5-0 outcome depends on this choice, and
     "with B … declared" at execution is adjustable.

8. **K-PR6's visible preparer cells are not assigned to wings (l. 205–208, 215, 532).**
   - p₁ and p₂ are visible, and each holds λ after the first two steps (node 7, MC7 PREREG l. 64–67).
   - If p₂ is among Bob's accessible records, Bob reads p₂ ⊕ r = ab. That is operational signalling at Bob's
     configuration.
   - σ-ons (I(a⃗; R_B) = 0) and IC-rec would then reject K-PR6 "by P10", a spurious favourable line. Under l. 884 it
     would be a gem by itself.
   - Node 7 evaluated no-signalling on the pointers q and r (MC7 NODE l. 45–46).
   - State which visible cells constitute each wing's records (pointers only; preparers at the source, not readable
     by either wing), and use the same assignment in σ-ons, IC-rec and D-3.

9. **The K-PROG variant set is open-ended, and the admission semantics are unfixed (l. 219–224, 382–383, 456–464).**
   - "Rejects K-PROG with all variants" cannot be decided while the variants are "read the path-blocking settings
     too". Enumerate them now, at least:
     - the basic V = 1, D = 1 apparatus;
     - the blocking-reading variant;
     - the three-path variant meeting I₃ = 0 by reading masks;
     - a programmed apparatus with a partial marker and programmed V = c, D = √(1 − c²), which satisfies B-VF.
   - State whether the last variant must be rejected. If it need not be, the achievability clause (l. 462–464) can be
     met by a programmed witness: response tables realize any finite law (Main.md:578), and real priors give
     irrational values (Main.md:60).
   - Require the boundary witnesses to satisfy the restriction under test and the three K-PROG discriminators.
   - In l. 382–383 and l. 462, define "admits K-Q / CC-q": there exists an O-admissible realization reproducing the
     control's record laws on the stated interventions that satisfies the restriction. CC-q is a density-matrix model
     and cannot itself be an admitted OI object (no quantum rules in the hidden sector).

10. **V depends on K, and K is not fixed for the verdict (l. 421–423, 459, 462).**
    - V is the max/min over Θ_K for four values of K. For a cos law with θ₀ ∉ Θ_K, the discrete V underestimates the
      continuous visibility, so B-VF and the boundary witnesses depend on K.
    - Fix one of: B-VF for each K separately, with every V_K printed; or V := V_K at a stated K with θ₀ ∈ Θ_K
      required.
    - State the exact field: c = 1/2 needs √3, and so do K = 6 and K = 12. ℚ(√2) (l. 114) does not suffice. Name the
      field (ℚ(√2, √3)) or the certificate.

11. **Q2's interferometer class is undefined, and rev2's fringe-law controls were dropped (l. 453–454, 456–459,
    724–755).**
    - Line 454 relies on "response-table, hidden-memory and reference-update subclasses".
      - 𝒟_IF and these subclasses are no longer defined in the file (rev2 §5.2).
      - The reference-update subclass's premise P19 (SM.md:296) was removed from §3, although `quotecheck.py` still
        checks it.
      - Either restore the definitions, or drop the reference-update subclass and state the class.
    - The three K-PROG discriminators (single-path θ-independence, Sorkin I₃ = 0 with I₂ ≠ 0, the cos law) now have no
      checker control. Rev2's K-FL+ and K-FL− supplied one: a quantum Mach–Zehnder must pass, and a triangle wave and
      a classical three-path model with I₃ ≠ 0 must be detected. Restore them. This is a regression.

12. **Several controls are not fixed at freeze, or have no model (l. 430–431, 468–470, 477, 732, 734, 736, 740).**
    - K-ERASE names no model and its expectation is "separate". Fix the model, for example CC-q at c = 0 with the
      marker read in the conjugate basis: unconditional V = 0 and conditional visibilities 1. That outcome is also
      KM-16's failing case.
    - CC-w lost rev2's definitions of V and D for the classical wave. Restore them: V from intensities, D the trace
      distance of the normalized coherency matrices.
      - The [L] expectation should be justified by the in-house Jones-vector computation.
      - The Eberly polarization-coherence relation, as I recall it, uses path predictability (intensity imbalance)
        rather than marker distinguishability. Do not let the control's expectation rest on that citation from
        memory.
    - K-I2's measure is "exhibited exactly in step 2". Fix it now. Any explicit asymmetric rescaling of Shannon
      information on composite first arguments works.
    - K-VD's "model with known laws" should be named.

13. **K-LEM, and missing tools in general, can be skipped silently (l. 117, 414, 731).**
    - sympy was absent at drafting. State that a missing dependency (sympy, python-flint or mpmath) makes the
      dependent control fail, not skip. Print the version or fail.
    - State that Q2's verdict is suppressed until K-LEM passes.
    - Fix the seed of the "random exact rational instance" (I-5 byte identity). Specify it as a rational point with
      Σ s_r² = Σ t_r² = 1, so the instance is exact.
    - Add K-LEM to an I-row; I-6 covers it only generically.

14. **Mutation controls lack named failing cases, and run before their unmodified checks (l. 757–783, 944–945).**
    - KM-1 and KM-2 ("any control", "a line"), KM-7 ("… and the checklist"; a human checklist is not a mechanical
      catch), KM-14, KM-15 and KM-16 name no failing case. Name one for each, for example:
      - KM-15 on a model where the actual readout is coarser than the optimal one;
      - KM-16 on the fixed K-ERASE model.
    - Step 2 runs "mutation controls" at item 2. Yet l. 757–758, and AGENTS §A.40, require each mutant to run only
      after every unmodified check it depends on has passed. KM-17 needs CC-dec (step 5) and KM-18 needs K-I2 (step 3).
      Move each mutant to just after its section's controls.
    - Consider using `tools/mutant_verdict.py` (present at the base) for the clean-failure judgement.

15. **P21 is stated as more than Main.md:600 supplies (l. 174, 322–325).**
    - What Main.md:600 proves:
      - it is for one finite-horizon law P on visible trajectories;
      - it quotients hidden data by the visible future-tail under that law's dynamics;
      - it has no regional or composite form.
    - P-pq describes T_B as "hidden data modulo distinctions that no accessible protocol on B reveals". That is a
      quotient across protocols, defined for a region B. P21 is neither.
    - Restate: the cross-protocol, regional quotient is a new construction (typed), and P21 is its single-law
      ingredient. Composite compatibility, which l. 324–325 already names, is then the tested step.

16. **(b5-C5) departs from Round 3 item 5, and (b4) has no amendment gate (l. 639–640, 648–650, 655–657, 929).**
    - The owner asked for full C5 tested on Pompili–Weilenmann's model "with a declared completion". The file allows
      only a completion "from the paper", and otherwise "is Parked, or gated by PC-PW …". These are two outcomes, and
      the second cannot occur if the paper fixes none.
    - Fix: if the paper fixes no completion, the PC-PW amendment declares one before execution (state space,
      transformations, composites; typed A), and the (b5-C5) verdict is scoped to it.
    - (b4) is a literature test point (Cavalcanti–Salles–Scarani, [L-s]) but has no gate. I-28 lists only (b5) and
      IC-G. Add a gate (PC-CSS), or fix an in-house search procedure now.
    - (b3)'s 3√3 is correct (2n cos(π/2n) at n = 3). Certify it in-house rather than entering it from [L].

17. **The productivity test counts restatements, and favourable branches, as gems (l. 869–887).**
    - Line 884, "any route whose K-PR6 line names an O-typed premise is a gem by itself", has no guard.
      - P8 is listed as a premise (l. 162), but its hypotheses (ii)–(iii) are exactly what branch (a) relinquishes
        (Main.md:82, :630). A route citing P8 (iii) rejects K-PR6 and TB alike.
      - Require the rejecting premise to hold on branch (a) and the same route to admit K-Q and K-C.
      - Mark P8 (ii)–(iii) in §3 as hypotheses of a no-go that branch (a) evades, not available premises. Only (i)
        and (iv) hold on branch (a).
    - Add to the baseline list (l. 869–871):
      - Main.md:356 and :407 (the unrestricted OI class includes PR);
      - book/appendix-c-objections.md:232, mirrored at FULL.md:6470 (an epistemic restriction gives complementarity
        but not Bell violation; "restricted access does not by itself single out quantum theory").
    - Without these, "OI does not imply C5" obtained from K-PR6 counts as a gem. That result is Main.md:356 plus the
      contrapositive of the cited C5 ⇒ IC theorem, so it should be a non-gem unless it identifies which interface
      property fails and why.
    - Similarly, a Q2 or H-X result that restates appendix-c:232 should be record-only.
    - The §A.19 statement at l. 186–189 should cite appendix-c:226 and :232. They are relevant corpus text, though
      they state no complementarity law.

18. **H-X has no decision rule (l. 30–35, 885).**
    - "A decision on the working hypothesis supported by the above" is adjustable.
    - Freeze the map from section verdicts to an H-X status, for example:
      - supported: every examined premise in Q1 yields "no cross-intervention restriction beyond R", with exact
        countermodels, and no route's K-PR6 line names an O-typed premise that holds on branch (a);
      - refuted: some route's K-PR6 line names such a premise, with K-Q admitted;
      - otherwise, undetermined.
    - Scope the status to the routes examined.

19. **The circularity outcomes are misclassified, I-23's exception list is incomplete, and §A.41 checkpoints are
    missing (l. 829–831, 924, 284–287, 459, 211, 913).**
    - (a) A fail on checklist items 21 (capacity standing in for IC) or 22 (independence confused with parameter
      dependence) is made "Reproduction". These are invalid steps, not quantum inputs.
      - They should leave the step unclosed: refuted, or Parked, at that step.
      - Keep Reproduction for items 1–6, 16 and 18.
    - (b) I-23's static check allows only "V-M-1 and §9.4 steps". The design also reads other sections' ledgers
      through:
      - σ-Q1, σ-C5 (l. 536–537) and ρ-Q1 (l. 571);
      - Q2's tests of Q1 restrictions and H-C5 (l. 448);
      - Q4's lines "from H-C5, Q1, 3A, 3B" (l. 668).

      As written, the check either fails or suppresses these routes. List each as a named exception with its step.
      Define "H-C5 if adopted" (l. 448, 396), presumably "as a named added axiom".
    - (c) Add checkpoints for properties the file asserts:
      - B and its slices declared and printed, with digest, before any route's computation (l. 284–287, 506–509);
      - V and θ₀ predicted from the architecture and printed before the pattern is computed (l. 459; only checklist
        item 17 covers it now);
      - every premise quoted in a step-2 ledger ("premise quoted at file:line", l. 211) passing the quote checker;
        I-12 covers only this file's fragments;
      - 𝔇 and the operational interface declared before C5 checks (see 5).

***

## Requirement-by-requirement check (owner rounds 0–3)

| requirement | status | where |
|---|---|---|
| strict prereg; plan before computation | met | l. 3–8, I-1 |
| ML and IC separately, each derived | met | §8.1, §8.2, l. 590 |
| (a) apart from (b); (b-corr) separate | met | l. 38–39, §9.2, I-10, I-27 |
| ML = NPA level 1, Q1 ⊋ Q | met; correct (needs nonzero marginals in CHSH) | l. 553, 627 |
| IC depends on Shannon choice | met | l. 494–496, B-1 |
| per-candidate derivation, ledgers, controls with PR exclusion, independent review | met | §5.2, §8, §12, §14, I-13 |
| new axiom ⇒ Conditional | met | l. 40–41, §13 |
| A1 distinct from A2 | met | §1, I-19 |
| central question (Round 1) | superseded by Round 2's governing question; carried as H-X; acceptable | l. 10–16, 30 |
| K-PR6 and RAC on every route | met, but see blocker 8 | §4.2, K-PR6-RAC algebra checked: m ⊕ b = x_y |
| GM and PW cited, unread | met; tagged [L-c]; gated | l. 497–501, 641–657 |
| Q1–Q4 structure | met | §6–§9 |
| C4 needs no write-then-read | met | V-6 (Main.md:80 verified) |
| three claims kept apart | met | §6.1 |
| K-PROG | present; variant set open (blocker 9) | §4.3 |
| Englert, operational D, concealment, eraser separate | met (D over admissible readouts; inaccessible ontic knowledge excluded) | §7.2 |
| lemma is mathematics; V := F_R circular | met | §7.1, KM-9, I-24 |
| C3 or per-record Shannon do not give IC | met | l. 33–34, σ-cap |
| GM exact selection is two-setting correlator only | met | l. 498–501 |
| complementarity ≠ Bell step | met | §9.4 |
| C5 tested first; constructions tested | met; table incomplete (blocker 4) | §5 |
| C5 settles / does not settle; classical satisfies C5 | met; "PR: yes" to be scoped (blocker 6) | l. 349–355 |
| Round 3.1 no saturation; CC-dec | met; saturation sentence wrong (blocker 1); CC-dec numbers correct | l. 438–443, 473–476 |
| Round 3.2 b(x,y,λ) ≠ initial dependence; B, slice, failing step | largely met; B_{t₀} gap (blocker 7) | l. 85–88, 523–528 |
| Round 3.3 existence claim, four verdicts, nonnegativity | met in substance; mapping incomplete (blocker 4) | l. 245–246, 332–340 |
| Round 3.4 decomposition consistency frozen | (I2) present; (I9) misattributed (blocker 2) | l. 252, 260 |
| Round 3.5 PW: full C5 with declared completion | partial (blocker 16) | l. 641–652 |
| adoption criterion | met; KM-19, I-34 | l. 342–348, 801–804 |

## Mathematics checked by hand

- **The lemma D_R² + F_R² ≤ 1 (l. 409–413)** is correct.
  - |s² − t²| = |s − t|(s + t).
  - Cauchy–Schwarz gives Σ ≤ √((2 − 2F)(2 + 2F)) = 2√(1 − F²).
  - Typo: write |p₀(r) − p₁(r)| in l. 410.
- **The bridge algebra (l. 435–437)** is correct.
- **The quantum bound and fidelity infimum (l. 438–441)** are correct, except for the saturation sentence
  (blocker 1).
- **CC-dec (l. 473–476)** is correct.
  - Both conditional states are I/2, so F_R = 1 for every readout and D = 0.
  - The coherence factor is tr[(I/2)Z] = 0, so V = 0.
- **TB (l. 602–603)** is correct. With |Φ⁺⟩ and the stated observables, E_ab = (−1)^{ab}/√2 and the marginals are
  zero.
- **Tsirelson's theorem for (b-corr) (l. 617–629)** is used correctly.
  - Unit vectors in a real space characterize the quantum binary correlator set.
  - VR ⇒ quantum is cited as [L] mathematics, and quantum ⇒ VR is in-house.
  - Q1's correlator projection also equals the quantum correlator set, so "ML and VR can at most reach (b-corr)" is
    right.
- **T1** has S_max = 14/5, matching MC7 NODE l. 107. **LE(w)** has S = 2 + 2w, matching node 6's B2b, so
  LE(√2 − 1) has S = 2√2.
- **K-PR6 and K-PR6-RAC algebra (l. 205–210)** is correct, subject to blocker 8.
  - The construction is node 7's LE(1,1) (MC7 PREREG l. 64–67). Node 6's B2 differs by the gating cell s; "after"
    node 6's B2 would be more precise.
- **The cited Lean statements** match their use: `cmi w a b c` = I(A; C | B); `cmi_le_of_deterministic` and
  `cmi_le_log_card` support IC-D3 and IC-D1/IC-D5c.

## Corpus spot-checks (§A.19, review point 7)

`quotecheck.py ../mc8w a501b418` reports 74 fragments, 0 failing (reproduced). A line-wise scan confirms that every
corpus quotation in the file is covered by the checker.

The checker carries four stale fragments that the file no longer quotes: Main.md:44, Methodology.md:393,
Structure.md:1312 and SM.md:296. Sync the list and correct I-12's count, or state that it is a superset.

I read these in full for meaning, not only for string match: Main.md:20, :78, :80, :82, :356, :358, :361–365, :392,
:405, :407, :486–488, :534, :550, :560, :578, :600, :602, :604, :630, :664, :666, :668, :674, :716; SM.md:296;
appendix-c:226–232; MC7 NODE l. 38–50, 104–111, 325–332; MC7 PREREG l. 64–67, 590–630. Findings:

- **V-1 to V-9** are supported as stated.
  - Main.md:666 does assert the slit identification without derivation, as V-7 says.
  - A word-bounded search confirms that no fringe or visibility law appears in the papers or the book.
- **P17** (Main.md:668, :674) concerns per-partition descriptions and a classical joint marginal matrix. V-W
  correctly treats a common local operator representation as Q-typed unless derived.
- **P18** (Main.md:716) is the realization's permutation unitary, as relied on.
- **P19** (SM.md:296) is quoted correctly, but it is no longer in §3, while l. 454 still relies on it (blocker 11).
- **P21** (Main.md:600) is narrower than P-pq's use (blocker 15).
- **P8** (Main.md:361–365): its hypotheses (ii)–(iii) are relinquished on branch (a) (Main.md:82, :630; blocker 17).
- **Line 76 slightly broadens node 7's record.** MC7 NODE l. 42–44 says LE(1,1) is admitted by every §3.1 reading
  "that admits the counting measure on LE(1,1)'s hidden bit", and lists those readings. That is narrower than "every
  reading of Lemma 3 it tested". Quote the narrower form.

## Literature (review point 8)

- **Load-bearing [L] items are mathematics or are re-derived in-house:**
  - Barnum et al. and Al-Safi–Short: re-derived as C5-S1 to S5;
  - Pawłowski: replayed;
  - Tsirelson and Fine: mathematics;
  - Navascués–Pironio–Acín: mathematics, and (b2) seeks an in-house witness;
  - the CLT and the binary-entropy bound: mathematics.
- **Literature cited from memory in ways that bear on a decision:**
  - (i) Eberly for CC-w's expectation (blocker 12);
  - (ii) Gallego–Dakić [L-s] for typing A-3. This is acceptable as typing, but stays flagged;
  - (iii) Wehner's 3√3 (blocker 16; the value is correct).
- **Non-load-bearing:** arXiv:2606.02416 and arXiv:2602.10206 (l. 706) and "Le et al. 2017" (l. 894) are unverified
  identifiers. Mark them [L-c], or drop them under §A.28.
- **Bibliographic data checked from my own knowledge:**
  - Barnum et al. NJP 12 033024 (author list correct), Al-Safi–Short PRA 84 042323, Short–Wehner NJP 12 033023;
  - DiVincenzo et al. PRL 92 067902, Greenberger–Yasin PLA 128 391, Englert PRL 77 2154;
  - Fuchs–van de Graaf IEEE TIT 45 1216, Oppenheim–Wehner Science 330 1072;
  - CDP PRA 84 012311 (five axioms plus purification);
  - all plausible and consistent with my knowledge.
- **Amendment gates:**
  - PC-GM blocks IC-G (l. 500–501, 655–657);
  - PC-PW blocks (b5) and the G6 three-setting scenario (l. 652, 655–657, 893);
  - both print "not run (precondition unmet)";
  - I-28 enforces this by reading only from a digest-printed amendment file;
  - (b4) needs the same treatment (blocker 16).

## Register (review point 9)

- No capitals emphasis: all-caps tokens are identifiers only (CHSH, PROG, ERASE, NODE, PLAN, PREREG, IEEE).
- No revision-history or meta-commentary phrases were found.
- Two places state claims stronger than their evidence: l. 350 (blocker 6) and l. 441–442 (blocker 1).
- The route names N-ont / N-acc ("Negative") and P-pq / P-ms ("Positive") presuppose outcomes. P-ms is labelled
  positive although l. 328 expects it may fail. Neutral identifiers would be better (non-blocking).

***

## Notes (non-blocking)

1. **Node 7's K-10.**
   - At the base, node 7's verdicts are "provisional on K-10 at n = 4" (MC7 NODE l. 82). The owner reports that K-10
     has since been confirmed in CI.
   - Record this in §0's state of knowledge, with where its evidence lives.
   - The K-10 row (l. 752, "no clause decided through it") may stay conservative, but say whether that is now a
     choice or a constraint.
2. **Feasibility.** Several clauses enumerate 𝒜_CHSH(n) up to n = 12 (l. 609, 633, 636), but node 7 needed CI for
   K-10 at n = 4. §4.1's stopping rule covers this, but a feasibility estimate in the prereg would prevent avoidable
   "incomplete" lines.
3. **Notation clashes.**
   - Sorkin's I₃ (l. 457) and the chained I₃ (l. 638) share a symbol.
   - a and b denote settings, box inputs and outputs (l. 205–210), and a_i denotes Alice's input bits (l. 494).
4. **Information–disturbance alternative (l. 357–358).** The corpus has its own result: a passive instrument learns
   only the commutative center (appendix-c:226; Main §3.4). Cite it instead of [L].
5. **Spekkens control.** Consider an epistemically restricted local model in the spirit of appendix-c:232 as a Q2/§9.4
   countercontrol: complementarity with CHSH ≤ 2. It would make the Q2 → Q4 separation measured rather than argued.
6. **Equiprobable paths (l. 406, 420).** Say how this is verified operationally, for example equal detection rates
   with each single path open.
7. **Adoption criterion (l. 342–348).** "By an exact check" admits a mathematical consequence whose truth value is
   known at freeze. Consider requiring, as G6 does, that both outcomes be possible.
8. **IC admission (l. 504–505).** IC admission of quantum boxes rests on the quantum-IC theorem, so (ii-Q) holds by
   construction for the IC line. This is legitimate mathematics. Say so in the verdict text, so that it is not read
   as OI evidence.
9. **The Explainer.md:566 overstatement** recorded in V-1 may merit an Issue for the owner. It is outside the node.
10. **An expectation in the prereg.** C5-S3a "is not expected to fail on that account" (l. 316). This is a structural
    consequence of D-2 and harmless, but it is an expectation.
