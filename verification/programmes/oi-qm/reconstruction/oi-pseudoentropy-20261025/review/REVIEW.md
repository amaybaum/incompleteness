# Review of 80e44653 (OI-PE-1 plan), parent c37700ad

File: `verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/README.md` (only file changed).
Reviewer: independent, read-only. #911 package read at `bafb38d672cbc63f9bf9ef26225ad995fa02c5c9` (fetched, not checked out).

## Verdict: BLOCK

The scope matches the owner's brief, the authority limits are right, the decision rules are written as rules (no
expected numbers), and the placement is correct. But the plan has errors in a definition (HILL) and in two of its five
anchors (Main:82, Main:172). It also leaves out the corpus statements that already contain PE-01's central fact, and
leaves out the one that sets the "10^-32 level" in the book claim it tests. The OI "advantage" is also not
well-defined as written. Each of these is cheap to fix. None should be published as it stands.

## Anchor check at c37700ad

| Plan cite | Exists | Says what plan says? |
|---|---|---|
| `book/ch18-beyond.md:104–114` | yes (104 "Deterministic but inaccessible" … 114 "Practical consequences are absent") | yes. The quoted sentence is verbatim at :114. The "reduced description" point is at :106. |
| `FULL.md:4922–4932` | yes, verbatim mirror | yes |
| `papers/Main.md:78` (C3) | yes | mostly (see finding 3) |
| `papers/Main.md:82` | yes (Theorem statement) | **no** (finding 2) |
| `papers/Main.md:172` | yes (Remark: why C4 is separate) | **paraphrased incorrectly** (finding 2) |

## Findings

1. **[blocker] HILL is misattributed, and "used as stated in their sources" is false.** README.md:45–48.
   HILL 1999 defines pseudoentropy through indistinguishability from some Y of high **Shannon** entropy. The
   min-entropy form is Barak–Shaltiel–Wigderson's (BSW intro, §3.1). Yao's compression definition is Yao 1982
   (FOCS, "Theory and applications of trapdoor functions"), not BSW, which studies its min-entropy analogue. The
   plan also never states what separates the notions, which is the order of quantifiers:
   - HILL: ∃Y with H∞(Y) ≥ k such that every size-s D has |Pr[D(X)=1] − Pr[D(Y)=1]| ≤ ε;
   - metric: for every D there is a Y, which may depend on D;
   - Yao: no size-s encoder/decoder pair compresses X below k bits except with small error.

   The plan also does not specify the distinguisher model: Boolean or [0,1]-valued, deterministic or randomized,
   non-uniform circuits, one sample. BSW's HILL↔metric equivalence for circuits (their Thm 5.2) has a published
   erratum (Oct 2011, on the authors' copy): there is a gap in passing from [0,1]-valued to Boolean distinguishers,
   closed by Reingold–Trevisan–Tulsiani–Vadhan (FOCS 2008). BSW also show that HILL and metric differ sharply for
   logspace observers, which is relevant to bounded physical observers.
   *Fix:* give each definition with its quantifier order, its entropy measure and its distinguisher model, and
   attribute each correctly: "HILL (Shannon, HILL99; min-entropy form, BSW03)", "Yao (Yao82; min-entropy form,
   BSW03)". Add RTTV 2008 to the literature list. Since OI's embedded observers have a quantum emergent description,
   name classical vs quantum distinguishers, and cite Chen–Chung–Lai–Vadhan–Wu, "Computational notions of quantum
   min-entropy", arXiv:1704.07309.

2. **[blocker] Two anchors are mis-stated.**
   - README.md:30–31 says every theorem quoted at Main:82 "holds on a *fixed* finite accessible horizon". That is
     wrong on two counts. First, Main:82 layer (4) is a conditional extension, not a theorem. Second, layer (1)
     holds "on every finite accessible horizon", with the realization chosen per horizon, and layer (3) contains an
     approximation clause ("uniformly realizable to arbitrary finite accuracy"). Main:538 makes the per-horizon
     choice explicit. Fixed versus per-horizon, and exact versus ε, is exactly this thread's crux (PE-04).
   - README.md:26–27 says the fair coin is realized "on a finite horizon, from a hidden tape". Main:172 actually says
     "zero backflow throughout arbitrarily long accessible horizons… the tape influences, the ledger records, and the
     two never meet". The construction itself is at Main:496–500: C_H = ledger × Z_D^K tape × clock, with the tape
     length growing with K.

   *Fix:* restate both anchors in their own terms (layers 1, 3 and 4 separately; "per-horizon realization, tape
   Z_D^K, Main:496–500"). Record as an open question, not a finding, whether "arbitrarily long" at Main:80 and
   Main:172 is meant per horizon. On one fixed finite φ it would conflict with the entropy bound.

3. **[minor] The C3 anchor is slightly overstated.** README.md:28–29: "a data-processing bound and is saturated".
   Main:78 says necessity is the data-processing bound, and that enumeration finds the bound *attained* by some
   realizations at (2,2) and (3,2), i.e. it is tight. Also, I* = sup_t I(X_<t; X_>t | X_t) (Main:492) is a
   conditional mutual information, not a record entropy.
   *Fix:* write "a data-processing bound on I* (Main:492), attained by some realizations (tight)". Say that it bounds
   CMI, not H(X_{0:K}).

4. **[blocker, §A.19] The plan omits the anchors that already contain PE-01's fact, and so sets its productivity test
   at the wrong baseline.**
   - **`papers/Structure.md:1256`** already states the sharp form: "the visible factor of a finite reversible
     substratum has zero entropy rate under every invariant prior, so whatever randomness an embedded observer records
     is bounded by log|C_V×C_H| and is exhausted at recurrence scale". The plan's bound at README.md:43 is the
     corpus's own theorem. The productivity test at README.md:93–94 ("strictly stronger than 'a deterministic record
     has bounded entropy'") is therefore weaker than what main already says.
   - **`papers/Main.md:496–500`**: the finite-horizon process dilation, with an explicit uniform "randomness tape"
     reproducing any rational law exactly. At any fixed horizon this answers the plan's first question (README.md:12)
     with TV = 0 against *unrestricted* observers.
   - **`papers/Main.md:544–560`**: operational gluing with "K pre-loaded seeds uniform on {0,…,G−1}", an exact grid
     error of (|O|−1)/G per step, and the single controlled dynamics whose program register costs Θ(|O|^K log|F|)
     bits. This is the corpus's own "persistent hidden seed standing in for randomness" (PE-03).
   - **`papers/Main.md:576`** (mutual ε-density at horizon K) and **`:536–538`**: no fixed finite realization is
     exactly operationally equivalent to a qubit, and the fixed-representation dimension grows as (n_V|A|)^{K/4}.
     These are PE-04's exact-versus-finite-approximation boundary.
   - **`book/ch18-beyond.md:56–58`** (FULL ≈4874–4876): successive outcomes "are not exactly independent samples
     from the Born distribution… correlations… suppressed by 32 orders". This is the source of the "10^-32
     suppression level" in the very sentence at :114 that the plan tests, and it is a corpus prediction that the
     record *is* distinguishable in principle.
   - **`book/ch18-beyond.md:110`** (inside the cited range but not drawn on): measurement independence is kept and
     ontic parameter independence is dropped. Measurement independence is the assumption that makes "protocol class
     P" independent of μ.
   - **`book/appendix-c-objections.md:58–62`** (FULL:6302–6306): the book's response to Colbeck–Renner, "no extension
     of QM can have improved predictive power". This bears directly on "unpredictable by any embedded observer".
   - **`papers/Computation.md:15–17`**: the conditional BQP model for embedded observers, with "no hidden-sector-access
     operation", and the framework being "structurally silent" on asymptotic complexity without a bridging premise.
     This bears on PE-02, and on README.md:50–51's restriction to concrete (s, ε).
   - Lower priority: `papers/Main.md:708` (the posit ledger: the selection of the "maximal-entropy invariant measure"
     is a named postulate, relevant to which μ PE-01 uses), and `book/ch01-observation.md:209`.

   *Fix:* add these anchors. Restate the productivity baseline as "strictly stronger than Structure:1256 together with
   the per-horizon dilation and gluing theorems of Main §3.4". State that PE-01 is non-trivial only for a *fixed*
   (S, φ) with K or the protocol class growing, since at a fixed horizon the corpus already gives exact
   indistinguishability.

5. **[blocker] The OI advantage is not well-defined.** README.md:52–54: "max_{p∈P} TV between the record laws"
   does not say *which* two laws.
   - Is it the model's law against a fixed reference, such as i.i.d. uniform or the QM law? If so, it is a
     pseudo*randomness*-type (fixed-Y) notion and not a pseudo*entropy*-type (∃Y) one. The notion item 2 would be
     compared with has to be stated.
   - Is it one sample or n repetitions (TV of products)?
   - Do the protocols' settings form part of the record (TV of the joint settings-and-outcomes law)?
   - Which normalization is used: TV, or the success probability (1+TV)/2?
   - Does the observer know φ? This is the Kerckhoffs-type assumption that the cryptographic notions make. With φ
     known, unbounded computation and records of recurrence length, zero entropy rate means perfect prediction
     (Structure:1256). Whether ch18:114's "any embedded observer" quietly assumes φ is unknown, a bounded record or
     bounded computation is the thread's most likely hidden assumption (§A.31) and should be named as such.

   *Fix:* define Adv_P(K) = max_{p∈P} TV(P^{φ,μ}_{p,K}, R_{p,K}) with R named. State measurement independence
   (settings independent of the initial state) as a hypothesis on P. State whether φ is known.

6. **[minor] State the Shannon bound with its conditions.** README.md:43 is correct for a passive record:
   X_{0:K} = f(s_0) with s_0 ~ μ, so H(X_{0:K}) ≤ H(μ) ≤ log2|C_V×C_H|. Three precisions are missing.
   - With externally supplied inputs (the "controlled model" of Main:560), the bound is conditional:
     H(X_{0:K} | A_{0:K} = a) ≤ H(μ) for each fixed input sequence or deterministic policy. Random inputs add their
     own entropy.
   - With a prepared x_0 the relevant bound is H(X_{1:K} | X_0) ≤ log2|C_H|.
   - HILL-type comparisons need H∞ ≤ H ≤ H_0 ≤ log|supp μ|. The cheap exact negative-control bound is
     TV(X_{1:K}, U) ≥ 1 − |supp μ|/|alphabet|^K.

   *Fix:* add these qualifications, and give each claim's entropy measure.

7. **[blocker for the milestone text] The milestone prejudges the outcome.** README.md:125–126: "together with an
   explicit counterexample showing where the analogy fails" assumes the analogy fails, before any computation.
   README.md:25 ("PE-01 to PE-03 test the second sentence") also needs a scope guard. Finite instances against
   explicit classes can refute ch18:114's "any embedded observer", or support it *for those classes*, but they can
   never establish the universal claim (finite test → universal claim).
   *Fix:* phrase the milestone as a question with a stated outcome rule: "COUNTEREXAMPLE if some embedded-realizable P
   has Adv ≥ δ at K ≤ K_0; otherwise the class-restricted result, with no universal reading". Add the scope sentence
   at :25.

8. **[minor] Controls can be vacuous.** README.md:67–69: a positive control "whose advantage is provably 0" is
   trivially met by the constant test, or by the Main:496 dilation at any horizon within capacity.
   *Fix:* require the positive control to be a non-trivial class (it must contain a test that separates the
   *reference* from some nearby law), and require the negative control to fire for the stated reason (e.g. the
   support bound in 6 at K beyond capacity). Say that each stage plan carries a §A.41 invariant→checkpoint table.

9. **[minor] The #911 description is accurate but under-scoped and unpinned.** README.md:32–35. "Finite whole state,
   time-independent update, B fresh fair bits per slot, complete-record TV from QM → 1, one protocol" matches
   REPORT.md:26–35 and :66. It leaves out four things that matter for PE-03:
   - (a) REPORT.md:7 explicitly states "Nothing here concerns A1…, native availability, physical premises, access
     rules or OI".
   - (b) The obstruction is *arithmetic*: dyadic fresh bits against the 4/5 run law. It holds for any source with
     probabilities in (1/N)Z with 5 ∤ N, and fails for a base-5 source (REPORT.md:40, :100–101).
   - (c) The necessity companion: avoiding T → 1 needs an unbounded number of persistent states. A retained-seed
     reset with linearly growing private memory escapes it (T ≤ 1/(2^B−2)), and bounded private memory with
     unbounded public state is open (REPORT.md:26, :45–55).
   - (d) The "fresh fair bits" are the *independently supplied randomness* side of PE-03's comparison. A fixed finite
     bijection with no fresh input is the B = 0 bounded-state case.

   "Proves" is the author's claim on an unlanded draft branch.
   *Fix:* write "reports a proof (unlanded; internal review accept-with-nits)". Pin
   `a2_memory_v8/REPORT.md @ bafb38d6`, not a mutable branch path (§A.42). Add (a)–(d) in one line each.

10. **[nit] Literature.**
    - Verified correct:
      - HILL, SIAM J. Comput. 28(4):1364–1396 (1999). Add the issue and pages.
      - BSW, RANDOM-APPROX 2003, LNCS 2764, pp. 200–215. I could not confirm the volume number online; the pages
        and editors match.
      - Vadhan–Zheng, STOC 2012, pp. 817–836.
      - Massey, IEEE Trans. IT-15(1):122–127 (1969). It describes LFSR synthesis (Berlekamp–Massey). "Distinguisher"
        is the plan's use of it, not the paper's term.
      - Ji–Liu–Song, CRYPTO 2018, LNCS 10993, pp. 126–152, published as "Pseudorandom Quantum States". The arXiv
        title differs ("Pseudorandom States, Non-Cloning Theorems and Quantum Money", arXiv:1711.00385); add the id.
      - arXiv:2211.00747 is "Quantum Pseudoentanglement" by Aaronson, Bouland, Fefferman, Ghosh, Vazirani, Zhang,
        Zhou. "et al." is acceptable.
      - arXiv:1910.14646 is correct (Bouland–Fefferman–Vazirani).
    - Missing and relevant to ch18:114's QKD/QRNG claim:
      - Colbeck–Renner, "No extension of quantum theory can have improved predictive power", Nat. Commun. 2, 411
        (2011), arXiv:1005.5173. The corpus already engages it at appendix-c:58.
      - Pironio et al., "Random numbers certified by Bell's theorem", Nature 464, 1021 (2010), arXiv:0911.3427. The
        device-independent certification of unpredictability rests on no-signaling against the adversary. That is
        exactly where OI's ontic parameter dependence (ch18:110) has to be checked.
      - RTTV 2008 (finding 1), and Chen–Chung–Lai–Vadhan–Wu, arXiv:1704.07309.
    - Optional: Reyzin, "Some notions of entropy for cryptography" (ICITS 2011), as a survey of the definitions.

11. **[nit] Cross-references.** README.md:83 cites "requirements of #910 to #912". The #910 PR body contains none of
    the named requirements (complete-record, adaptive measurement, outgoing carrier). #911 and #912 do, the latter as
    "outgoing carrier".
    *Fix:* give each requirement with its PR and path.

## Items checked and found clean

- Placement (§A.36): under the programme's `reconstruction/`, next to the #911 audit. No root file.
- §A.28/§A.27: no manuscript edits, no internal ledger vocabulary aimed at readers. The status labels are in a
  verification file, so §A.33's caps rule does not apply.
- Authority limits (README.md:113–121) match the brief.
- The no-identification-without-a-formal-map clause (:56–57) and PE-02's separate-direction clause (:72–73, §A.34)
  are present.
- The decision rules (:86–97) are rules, not expected values.

***

## Addendum: re-check of 47d4f2b3 (parent 80e44653, one file)

### Verdict: BLOCK, narrowly

Three one-line fixes are required: R1, R2 and R3 below. Everything else is resolved or a nit. Once R1–R3 are fixed,
this is ACCEPT WITH NITS, and nothing beyond those lines needs re-review.

### 1. Status of the original eleven findings

| # | Status | Note |
|---|---|---|
| 1 HILL / metric / Yao | resolved | Entropy measure, quantifier order and distinguisher model are now named; attribution is correct. Nits N1 and N2. |
| 2 Main:82 / Main:172 | resolved | The new line 39 introduces a fresh misstatement (R2). |
| 3 C3 | resolved | Lines 49–51 are accurate. |
| 4 missing anchors | resolved | All added. Nit N3 on the description at line 34. |
| 5 OI advantage | partly | The fixed-Q form is now defined. The class form is not defined (R3). The perfect-prediction sentence is wrong as stated (R1). |
| 6 Shannon caveats | resolved | Nit N4: record length. |
| 7 milestone prejudges | resolved | Lines 222–226 are neutral, and lines 22–23 carry the scope guard. |
| 8 vacuous controls | resolved | Nit N5: feasibility. |
| 9 #911 scope | resolved | Nit N6. |
| 10 literature | resolved | All verified (section 5 below). |
| 11 #910–#912 | resolved by deferral | Lines 159–163 commit to citing each requirement by PR and path before use. That is acceptable. |

### 2. New anchors at c37700ad

All of the following exist, and the plan describes them correctly:
- FULL.md:4932;
- Structure.md:1256;
- Main.md:476 ("the per-horizon qualifier is load-bearing");
- Main.md:492, :496–500, :538, :544–560, :576, :708;
- ch18:56–58 (the 10^-32 correlations; :56 "History-dependent corrections", :58 "independence is approximate");
- ch18:110;
- appendix-c:58–62;
- Computation.md:15–17.

Exceptions:
- **R2 (required).** README.md:39 says "no fixed finite *realization* hosts generic combs as the horizon grows".
  Main:536 and Main:476 say no fixed *representation* does, meaning a horizon-independent Hilbert-space
  representation of the intervened process. The corpus states this for representations, not for finite substratum
  realizations.
  *Fix:* "no fixed representation (Hilbert space) hosts generic combs as the horizon grows (Main:476, :536)". The
  second clause, on N-state models and the qubit (Main:538), is correct.
- **N3.** README.md:33–35.
  - The "response-table extension" is Main:498. It removes the *rationality* restriction by replacing the uniform
    tape with a response coordinate under a product prior. "For arbitrary priors" should read "for arbitrary real
    finite-horizon laws, via a non-uniform product prior".
  - "Total variation is 0 against every observer" holds for the *passive* multi-time law. Intervening observers are
    covered only for a fixed finite adaptive family, by the comb theorem (Main:460, :536).
  - "One realization per horizon" (line 36) is the plan's reading of Main:172 and should be marked as such.

### 3. New definitions

- **R1 (required). README.md:121–122.** "Zero entropy rate means it can predict the record perfectly" is false as
  stated.
  - Zero entropy rate alone does not imply perfect prediction.
  - In any case, no observer predicts the opening symbols perfectly: Σ_t H(X_t | X_<t) = H(R) can be as large as
    H(μ).
  - The correct reason is periodicity. Each passive visible record π(φ^t s) is periodic, with period at most |S|. By
    Fine–Wilf, two such records that agree on 2|S|−1 consecutive symbols agree forever. So an observer who knows φ and
    π, and has seen a prefix of length 2|S|−1, predicts the rest of the record exactly. Before that, its total
    uncertainty is at most H(μ).

  *Fix:* "…then, after a prefix of length at most 2|S|−1 (Fine–Wilf, by periodicity of the passive record), every
  initial state consistent with the record has the same future, so the remainder is predicted exactly. The total
  uncertainty before that is at most H(μ)."
- **R3 (required). README.md:113–115.** The pseudoentropy-type option, where Q ranges over a high-entropy class 𝒬,
  is named but has no formula. Its quantifier order is exactly the HILL/metric distinction:
  - HILL-like: min_{Q∈𝒬} max_{p∈P} TV;
  - metric-like: max_{p∈P} min_{Q∈𝒬} TV.

  These can differ unless a minimax theorem applies (convexity in p, for example randomized protocol mixtures).
  *Fix:* display both and say which one each use takes.
- **The OI advantage, fixed-Q form** (lines 107–111): correct and well-defined.
- **The unrestricted TV bound** (lines 85–86): correct. R_K is a function of s_0, so |supp R_K| ≤ |supp μ|, and
  TV ≥ U(complement of the support) = 1 − |supp μ|/|A|^n for a uniform reference on A^n.
  - **N4.** R_K = X_{0:K} has K+1 symbols, so with an unprepared x_0, n = K+1, and |A|^K gives a true but weaker bound.
  - Name n, and say whether settings or x_0 are excluded from the reference.
- **Conditional and prepared-x_0 caveats** (lines 83–84): correct. Optional: write the prepared case as
  H(R_K | X_0 = x_0) ≤ log2|C_H|.
- **The chain at line 82** (H∞ ≤ H ≤ H(μ) ≤ log2|supp μ|): correct.
- **The PRG point** (lines 87–89): correct as hedged ("under its assumptions"). Optional addition: for one fixed
  finite generator, concrete (s, ε)-security against all size-s circuits is not provable unconditionally, beyond
  exhaustive search at tiny parameters.
- **HILL, metric and Yao statements** (lines 93–101): correct in substance.
  - **N1.** HILL 1999 states its notion asymptotically (polynomial-size families, negligible advantage). The concrete
    (s, ε) form is the later standard. "As its source states it" should say so.
  - **N2.** Yao 1982 is a Shannon-type (limit) compression notion; BSW give the min-entropy version. Name the
    measure, as is done for HILL.
  - The BSW erratum *is* verifiable. The authors' copy (boazbarak.org/Papers/compent.pdf, dated 5 Dec 2003) carries
    "Erratum (October 2011): … error in the proof of Theorem 5.2 (equivalence of HILL type and Metric type
    pseudoentropy). There is a gap … while passing from a distinguisher outputting values in [0,1] to a Boolean
    distinguisher. This gap can be overcome, as was shown by Reingold, Trevisan, Tulsiani and Vadhan (FOCS 2008)."
    The plan's neutral wording is acceptable either way.

### 4. Overclaim and prejudgement

No sentence prejudges an outcome. The milestone (lines 222–226) and the scope guard (lines 22–23) are now correct.
Minor points:
- **N5.** README.md:134–137 promises exact advantages for a circuit-size class. An exact maximum over all size-s
  circuits is feasible only at tiny s and n. State the parameters, or use the structured classes the line already
  names: Berlekamp–Massey linear tests, low-degree or k-wise tests.
- **N6.** README.md:70: per REPORT.md:26 and :53–54, the retained-seed reset escapes only *when granted the target
  cuts*. Add the qualifier.
- README.md:57–58: "certified randomness … relies on no-signalling against the adversary" is the plan's gloss, not a
  corpus statement. It is acceptable. Optionally add measurement independence, which DI certification also assumes.

### 5. New references

All verified:
- Yao, "Theory and applications of trapdoor functions", 23rd FOCS 1982, pp. 80–91.
- Reingold–Trevisan–Tulsiani–Vadhan, "Dense subsets of pseudorandom sets", FOCS 2008, pp. 76–85.
- Chen–Chung–Lai–Vadhan–Wu, "Computational notions of quantum min-entropy", arXiv:1704.07309. The authors and title
  match the arXiv record.
- Colbeck–Renner, "No extension of quantum theory can have improved predictive power", Nat. Commun. 2, 411 (2011),
  arXiv:1005.5173.
- Pironio et al., "Random numbers certified by Bell's theorem", Nature 464, 1021 (2010), arXiv:0911.3427.

The other entries are unchanged from the first review and correct. Ji–Liu–Song now carries arXiv:1711.00385.

### Update for head bd69acff (covers 47d4f2b3 and the +25/−8 on top)

**Verdict at bd69acff: BLOCK, narrowly.** The new commit resolves R1 correctly. R2 and R3 above are untouched by the
diff and still stand. Two new required points follow from the owner's risks (b) and (a): R4 and R5. Each is one to
three lines. Once R2–R5 are fixed, this is ACCEPT WITH NITS (N1–N7).

**R1 is resolved; the Fine–Wilf step checks out.** README.md:126–130 at bd69acff.
- A bijection on a finite set decomposes into cycles. So s_t = φ^t(s_0) is purely periodic with period ℓ(s_0),
  its orbit length, and x_t = π_V(s_t) is purely periodic with a period p dividing ℓ(s_0). Hence p ≤ L ≤ |C_V×C_H|.
- Take two such sequences a and b, with periods p, q ≤ L, that agree on a window W with |W| ≥ p+q−g, where
  g = gcd(p,q). The common word on W has periods p and q, so by Fine–Wilf it has period g.
- W contains p consecutive symbols of a. These have period g, and g divides p, so a's cyclic p-block has period g and
  a has global period g. The same holds for b. Since a and b agree on g consecutive symbols, a = b.
- p+q−g ≤ 2L−1, so "2L consecutive symbols" is valid, with one symbol to spare.
- So for a passive record, a K1 observer who has seen 2L−1 symbols finds that every initial state consistent with
  the record has the same future. Prediction is then exact.
- **N7 (scope):** the periodicity premise holds only for the autonomous record. Settings generated inside C_V by an
  embedded policy are part of φ and keep it. External inputs (the controlled model, Main:560) break it. Write
  "Every passive (autonomous) visible trajectory…".

**Risk (c): does knowing φ get treated as reading h? No.**
- README.md:120 says "h is never read". :122 says "Knowing the law is not knowing the seed". K1 (:124–125) is
  posterior inference from the visible record.
- The superseded 47d4f2b3:121–122 sentence also did not equate the two.
- One clarification to add: a K1 observer may *infer* the initial state up to record-equivalence from the visible
  record. If the record map is injective on supp μ, that determines s_0, and hence every h_t. This is legitimate
  inference, not K2. The K2 exclusion at :131–132 should say it excludes *a priori* knowledge of s_0, so that it is
  not later used to rule out what K1 learns.

**Risk (b): are the quantifiers stated correctly? Partly.**
- HILL (∃Y ∀D) and metric (∀D ∃Y) at :93–99 are correct. N1 and N2 still apply.
- R3 still stands at :113–115. The class-Q form of the OI advantage needs its order displayed:
  - HILL-like: min_{Q∈𝒬} max_{p∈P} TV;
  - metric-like: max_{p∈P} min_{Q∈𝒬} TV.
- **R4 (required, new).** K0 is not defined by the advantage formula at :109. TV(P^{φ,μ}_p, Q_p) is the advantage of
  the optimal test *for that P*, so it already presumes that φ and μ are known. TV is a K1 quantity.
  - The cryptographic definitions are also K1 by default, because the distinguisher is quantified after the generator
    is fixed. Non-uniform circuits may hard-wire φ (the Kerckhoffs convention); only the seed is secret.
  - So "unrestricted at K0" (:146) needs its own definition, one of:
    - (i) a prior over φ, which folds φ into the seed. K0 is then K1 on the enlarged model.
    - (ii) a test, or test class, fixed independently of φ, with its advantage stated worst-case or on average over a
      named generator family.
  - *Fix:* add one sentence giving the chosen K0 definition, and state that TV and the item-2 notions are K1-type.

**Risk (a): is the experiment new relative to Structure:1256 and Main §3.4? Partly. Expect outcome 3 for the
unrestricted part.**
- *Already covered for the unrestricted observer:* Structure:1256 (zero rate, bounded and exhausted record entropy),
  the support bound at :85–86, and the 2L Fine–Wilf horizon.
  - An exact adv(K) curve for one fixed generator at K0/K1 is a worked example of these. On its own it would fall
    under the third milestone outcome.
  - A Berlekamp–Massey negative control is textbook (an LFSR of linear complexity ℓ falls to 2ℓ symbols), which is
    right for a control and not new.
- *Not in the corpus, and therefore the possible new content:*
  - any computational-indistinguishability statement for a fixed finite realization;
  - any comparison between a physically restricted protocol class P and a distinguisher class (PE-02);
  - the dependence on knowledge level.

  Main §3.4 handles fixed finite adaptive families per horizon (Main:460, :536) and the ε-net (Main:576). It says
  nothing about bounded tests.
- *Single-instance limit:* one fixed generator supports an exact computation or a counterexample. A "new bounded
  theorem" needs a class of generators or observers. Say which class.
- **R5 (required, new): the milestone rule, README.md:238–243.**
  - (i) "Exactly one of three outcomes" is neither exclusive nor exhaustive.
    - A result can be both a counterexample and a theorem.
    - The decision rules at :182–183 also allow OPEN, and a void outcome (control failed). The milestone list omits
      both, which pressures toward closure.
    - *Fix:* "one or more of: …; or OPEN; or VOID (control failure)".
  - (ii) The counterexample outcome needs an admissibility condition. The observer must be *embedded-realizable*: its
    record memory and computation fit within C_V, and its settings are measurement-independent.
    - An unrestricted K1 observer holding about 2L symbols, with L up to |C_V×C_H| ≫ |C_V|, cannot be embedded. A
      "counterexample" built from it alone refutes nothing about ch18:114's embedded observers.
    - Such a result is also already implied by Structure:1256, so it belongs under outcome 3.
    - This embedded-memory bound is probably the main hidden assumption behind ch18:114. Record it at the
      assumption-watch item (:134–135).

**Other points carried over from 47d4f2b3:**
- R2 still stands at :39 ("realization" should be "representation", per Main:476 and :536).
- N3–N6 still stand.
- The references in section 5 above are all verified.

***

## Addendum 2: final check of e49c3b0f (parent bd69acff, +48/−23, one file)

### Verdict on head e49c3b0f: ACCEPT WITH NITS

R2–R5 and N1–N7 are resolved. Three new nits, N8–N10, are each one line. N8 should be fixed before the plan is
published, because it closes a quantifier ambiguity in the new K0 definition. N9 and N10 can wait for the PE-01 stage
plan.

### Status of R2–R5 and N1–N7

- **R2** resolved. The ":476/:536 representation" and ":538 N-state realization" lines are attributed correctly.
- **R3** resolved. Both orders are displayed: HILL-like is min over Q of max over p; metric-like is max over p of min
  over Q.
- **R4** mostly resolved. TV is stated to be K1, and the cryptographic notions K1 by default. The K0 definition leaves
  the quantifier order open (N8).
- **R5** resolved.
  - Outcomes are "one or more of".
  - A bounded theorem needs a class.
  - A counterexample needs an embedded-realizable observer.
  - OPEN and VOID are added (see N10 on their precedence).
  - The memory bound is now the assumption-watch item.
- **N1** resolved: HILL is stated asymptotically in the source; the concrete form is the later standard.
- **N2** resolved: Yao is a compression-based, Shannon-type notion.
- **N3** resolved.
  - `:498` removes the rationality restriction.
  - TV is 0 for the passive law.
  - Intervening observers are covered only for fixed finite families, `:460` and `:536`.
  - "One realization per horizon" is marked as the plan's reading.
- **N4** resolved: n = K+1, and the bound uses |A|^n.
- **N5** resolved: exact all-circuit advantages are computed only at stated tiny parameters.
- **N6** resolved: "when granted the target cuts" is added.
- **N7** resolved: the periodicity claims are scoped to the passive, autonomous record, with external inputs per
  Main:560. "Purely periodic" is stated.

### Attributions, re-verified at c37700ad

- Main:460 is the intervention-dilation (comb) theorem for a finite action-labelled family.
- Main:536 says "realizes any FIXED finite adaptive family… no fixed representation hosts generic combs".
- Main:476 says "a horizon-independent representation of the intervened process does not exist for generic combs".
- Main:538 says "no N-state model reproduces exactly… no fixed finite realization is exactly operationally equivalent
  to… a single qubit" and "the realization is chosen per finite-horizon law".
- Main:498 is the response coordinate, which lifts rationality.
- Main:560 says "intervention labels arriving as visible inputs".

All are correct.

### New sentences checked for errors and overclaims

- **The K0 definition** (README.md, K0 sub-bullets).
  - The direction is right: TV is the best test for a given P, so it is K1. At K0 the test class is fixed
    independently of φ.
  - **N8 (fix before publishing).** The order of "test" and "generator" is not stated. If the maximum over tests is
    taken per generator, the PE-01 "unrestricted observer at K0", with all tests, collapses to TV, i.e. to K1. K0 is
    then vacuous as a separate level.
  - *Fix:* state that the test is chosen once, before the generator. Use
    adv_K0 = max_{D∈𝒟} min_{φ∈𝔉} adv_D(φ) for the worst case, or max_{D∈𝒟} E_{φ∼ν} adv_D(φ) for the average case,
    and say which.
  - Note that the average-case form is not the same as folding φ into the seed. The mixture's TV is at most
    E_φ TV, not equal to it.
- **Embedded-realizability paragraph.** The criterion itself (memory and computation in C_V, measurement-independent
  settings) is sound. It is the book claim's own scope ("any embedded observer"), not an immunizing restriction.
  - **N9.** "A K1 observer holding about 2L symbols, with L up to |C_V×C_H| ≫ |C_V|, *is* not embedded-realizable" is
    stated unconditionally, but L depends on φ and can be small. The comparison should also be in bits: storing 2L
    symbols takes 2L·log2|A| bits, against log2|C_V| bits of visible memory.
  - *Fix:* "is not embedded-realizable whenever 2L·log2|A| exceeds the observer's memory share of log2|C_V| (for
    example when L is near |C_V×C_H|)".
  - "Its success is already covered by Structure:1256" is fair. Zero conditional entropy beyond recurrence scale means
    the future is a function of the past almost surely.
- **K1 inference sentence.** It is correct, given a record long enough to separate the states in supp μ. Optionally
  say "once the record separates supp μ".
- **"By default these notions are K1"** is correct for both non-uniform and uniform distinguishers, since the
  generator is public and only the seed is secret.
- **OPEN/VOID wording.**
  - **N10.** Precedence is not stated. The decision rules already make a verdict over a failed control void. Say "a
    failed control makes the milestone VOID whatever else was reached; otherwise OPEN if no outcome is reached".
- **Overclaims.** No other sentence overclaims or prejudges an outcome.
- **Process leakage.** None found (§A.28). The file is still a single README in the correct place (§A.36).

***

## Addendum 3: 66578f41 (parent e49c3b0f, +14/−5). Verdict: ACCEPT

N8, N9 and N10 are each resolved.

**N8.** The test is now chosen once, before φ. The plan gives a worst-case form,
max_{D∈𝒟} min_{φ∈𝔉} adv_D(φ), and an average-case form, max_{D∈𝒟} E_{φ∼ν} adv_D(φ), and says which one each use
reports. It also states the collapse into K1 explicitly. Both forms are correct. So is the caveat about mixtures: by
convexity of TV, TV(E_ν P_φ, Q) ≤ E_ν TV(P_φ, Q), with equality not guaranteed.

**N9.** The memory condition is now conditional and compares bits with bits. It also says that L depends on φ.

**N10.** VOID now takes precedence over every other outcome, and OPEN applies otherwise. This is consistent with the
decision rules.

The edits introduce no new error or overclaim. One optional nit: define adv_D(φ) inline, as
|Pr_{P^{φ,μ}_p}[D=1] − Pr_{Q_p}[D=1]| at the stated protocol and horizon. The meaning is clear from item 2 even
without it.
