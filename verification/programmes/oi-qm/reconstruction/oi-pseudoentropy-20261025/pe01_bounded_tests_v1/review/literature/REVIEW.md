# Independent review: PE-01 literature-tag annex under A3

- **Object:** `pe01lit/TAGS.md` (draft, 2026-10-26) and its downloads `pe01lit/dl_*/`.
- **Rule:** `amendments/A3-literature-tags.md`, read before the annex.
- **Record:** `REPORT.md`, `PLAN.md` §1–§3, §6 item 5 and §9, `results/verdict.txt`, `pe01/generators.py`,
  `pe01/embedded.py`.
- **Method:** read-only. PDFs were read by `pdftotext` only. Nothing was rendered, and the PostScript file was not
  opened. Python ran with `-I` from `revlit/probe/`, outside the download directories, and imports nothing from the
  repository.

## Verdict: ACCEPT WITH CHANGES

The annex follows A3's form. The tags rest on first-hand reading, the quotes exist, the survey supports no tag,
"covered in kind" is kept apart from COVERED-literature, and candidate-NEW is correctly withheld. Two conclusions
lean in the direction favourable to novelty and need correcting before the annex is relied on (A3 item 5):

- **(ii) is under-inclusive.** The AGHP mechanism that justifies the B1 K0 tag equally covers every other passive row
  on the linear generators whose statistic is linear in the record. That covers B3k, B3w, the linear-filter
  observers, and the m = 1 passive observers.
- **(i) missed the closest kind of prior work.** W5's own reference [16] is an open-access fault attack in which the
  adversary's bit flip enters the clock-control register and changes the clocking. By the annex's own criterion,
  that covers the cell in kind.

The Rueppel point is right in substance, but it should be stated more precisely. The REPORT bullet also overstates
what W1 shows. Exact replacement texts are given below.

## Findings

### 1. A3 compliance

- **Hashes.** All 13 downloaded files match the sha256 values in TAGS.md: W1–W7, the second AGHP copy, the Grain
  slides, the two Springer challenge pages (identical, `32ed6315…e0e18ea`), the Kholosha challenge page and the
  Kholosha PostScript file. One problem is in the text, not the files: the Grain hash is printed as `f9c6d47c…dc2`,
  but the file's hash ends `…c1dbd2` (nit N1).
- **Page counts.** All match `pdfinfo`: 5, 27, 19, 11, 18, 11 and 33 pp.
- **Quotes.** I spot-checked every quote by text extraction (`probe/qcheck.py`, `probe/pages.py`).
  - Each one exists verbatim, up to the elisions marked and the extraction's line-break hyphenation ("appli-cable",
    "Goll-mann", "deter-mined").
  - Each one is on the cited printed page: W1 pp. 1–2; RSV pp. 2, 9, 10; AGHP pp. 7, 8; BDVY pp. 285, 286; W5 p. 4;
    W6 pp. 77, 79; HAC pp. 220, 221.
  - One cosmetic difference: RSV p. 2 ends "…and not on the current state" with no full stop (N2).
- **Grep claim.** The claim of no hits in RSV for adaptive / LFSR / shift-register / predict reproduces: 0 hits each.
- **Tag discipline.**
  - Every tag cites a passage, a page and the parameters covered.
  - "Covered in kind" is never conflated with COVERED-literature.
  - W7 (HAC) is a survey and supports no tag, and its secondhand summaries of Gollmann–Chambers and Živković are
    correctly given no weight.
  - W1's account of Rueppel is correctly treated as secondhand (A3 item 3).
  - Candidate-NEW is correctly not assigned. A3's list includes Rueppel 1987 and Gollmann–Chambers 1989, and both
    are unread.
- **Scope.** The restriction of the 𝔉_lin B1 K0 tag to n = 3, 4 is correct, though the annex does not say why. The
  n ≥ 5 𝔉_lin B1 K0 rows (`verdict.txt:1303–1304, 1352–1353, 1399–1400, 1446–1447`) are in section 1b, "Bounds
  and intervals (not PROVED)". That is outside A3 item 1. The annex should state this (N3).

### 2. Tag (ii): AGHP

**"Covered in kind" for the B1 K0 rows at n = 3, 4 is right.** It is neither too strong nor, on A3's wording,
clearly too weak. I checked AGHP's proof of Proposition 1 (p. 8) against PLAN's definitions:

- **The per-polynomial dichotomy.** For a fixed feedback polynomial, each linear combination of the register bits is
  either identically zero or a non-constant linear form in the uniform start vector. It is identically zero exactly
  when f | g. The argument uses only linearity in the start vector, so it holds for every primitive p in 𝔉_lin.
- **The family statement.** AGHP's "bias = Pr[f | g]" is for f uniform over irreducible polynomials. PLAN's ν is
  uniform over primitive polynomials (PLAN:69–70; `generators.py:137–139` uses `gf2.primitive_polys`). The two
  coincide at n = 3 and differ at n = 4, where z⁴+z³+z²+z+1 is irreducible but not primitive. The annex's reason (1)
  is correct.
- **Accumulated record versus raw LFSR.** The annex's reason (2) overstates this as a gap.
  - B1 tests are D_T = ⊕_{t∈T} X_t on X_{0:K} (PLAN:137), with X_t = x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1} and Y_t = ℓ(h_{t+1})
    (PLAN:26).
  - The map X_{0:K} ↦ (x₀, Y₀, …, Y_{K−1}) is linear and invertible.
  - A test with |T| odd contains x₀, which is uniform and independent of h, so it is exactly unbiased.
  - A test with |T| even is a linear test on the raw LFSR output (s₁, …, s_K) from a uniform start.
  - The gap is therefore one elementary step, not a different object. AGHP still does not state that step, so the
    tag is unaffected.
- **Counting.** The horizons need the largest number of family members dividing one g of degree < K. The annex's
  reason (3) is correct, and it is the real gap. With that count:
  - K0-average: K_zero = n, and K_1/8 = K_1/4 = n + 1 when |𝔉_lin| = 2.
  - K0-worst: K_zero = φ(2ⁿ − 1), the degree of the product of all primitive polynomials of degree n.
  - That gives 3 / 4 / 4 and 6 / 7 / 7 at n = 3, and 4 / 5 / 5 and 8 / 9 / 9 at n = 4. These are exactly the
    measured rows `verdict.txt:176–177, 372–373`.

**Control.** `probe/aghp_check.py` enumerates 𝔉_lin records from PLAN §1 alone, with no repository imports. It
computes max_T min_φ and max_T E_φ over all T exhaustively, for K ≤ 9 (n = 3) and K ≤ 11 (n = 4). It reproduces
the four rows exactly and agrees with the closed forms. At n = 3, ν equals AGHP's distribution, so one could argue
"directly implies" for the K0-average row. The remaining counting step is trivial there. A3 does not define
"directly", though, and both tags withhold candidate-NEW. The conservative reading is acceptable.

**Under-inclusive: other rows the same mechanism covers in kind.** The annex says "No other row". But the dichotomy
governs every passive statistic that is linear in the record, on G_lin, G_lin_sib and 𝔉_lin. Under G_lin the law of
any linear image of X_{0:K} is uniform on a subspace. It differs from its Q-law exactly when some parity is
constant, and that happens exactly when p divides that parity's test polynomial. AGHP Lemma 1 (Vazirani), p. 5,
with ε = 0, gives the marginal statement: a sample space unbiased on linear tests of size ≤ k is k-wise independent.
The affected section 1 rows, all "untagged", are:

- **B3k** K1, K0-worst and K0-average, n = 3..8.
  - The ≤ 3-position marginals are non-uniform only through 2-term parities. X_a ⊕ X_b has test polynomial
    t^a(t^d + 1)/(t + 1), so p divides it iff ord(p) = 2ⁿ − 1 divides d.
  - Prediction: K_zero = 2ⁿ − 2. Measured: 6, 14, 30, 62, 126, then 127 at the n = 8 scope cap of 127.
  - K0 equals K1 because all primitive p of degree n have the same order. `probe/aghp_check.py` confirms the first
    constant 2-parity at K = 2ⁿ − 1 for n = 3..6.
- **B3w** K1 and K0-average. A window of n + 2 symbols carries g = p. K1 K_zero = n, as measured at every n. The
  K0-average values follow from the per-φ hyperplane laws by a computation over sign patterns. `probe/b3w_check.py`
  gives advantages 0, 1/6 and 19/64 at K = 5, 6, 7 for n = 5, so the horizons are 5 / 6 / 7, as measured.
- **plin_m1–m4 and plin_m1–m4_pred**, K1 and K0. ρ_x(v) = Av ⊕ xb (PLAN:193), so v_K is linear in X_{0:K−1}. For
  m = 1 with b = 1, v_K ⊕ X_K has test polynomial ((t^{(K+1)/2} + 1)/(t + 1))² for K odd. That predicts
  K_zero = 2(2ⁿ − 1) − 2, which is 12 at n = 3 and 60 at n = 5, matching `verdict.txt:547`. A separate inline brute
  force confirms the first constant parity at K = 13 and 61.
- **emb_m1_passive and emb_m1_passive_pred**, K1 and K0. Sym({0,1}) = {v, v ⊕ 1}, so every m = 1 passive observer
  is an affine filter. Its rows equal plin_m1's (for example 12 / 13 / 13 at n = 3, and 60 / 61 / 61 at n = 5).

The boundary is the linearity of the statistic. emb_m2_passive, with x-dependent A_x, is nonlinear in the record.
The same is true of B2 (linear complexity) and of B4 at degree ≥ 2. The annex rightly leaves those untagged.

**RSV and BDVY are correctly untagged, but the stated reasons need repair.** No measured horizon follows from
either:

- **The exact-zero case.** Both bounds have the form L·ε. At ε = 0, an input unbiased on all parities is exactly
  uniform, so every class has advantage 0. That gives K_zero(class) ≥ K_zero(U) = K_zero(B1) on every generator,
  which is trivial and is already COVERED-corpus through U. Beyond that K, G_lin has a constant parity (ε = 1), and
  the bounds are vacuous.
- **The RSV reason.** "(2w²)^k ≥ 1, so no exact zero follows" is literally false: an exact zero does follow at ε = 0.
  The right statement is that only the trivial one follows.
- **The BDVY reason.** The "one-sided bound K_zero(m = 1 passive) ≥ K_zero(B1)" is not weaker than the measurement.
  It is vacuous: all linear tests exactly unbiased ⇔ uniform ⇔ U advantage 0, so K_zero(B1) = K_zero(U) always.
  Compare `verdict.txt:505` and `517`.

W5 is correctly limited to class U.

### 3. Tag (i): the counterexample

- **The works the annex read.** None of W1, W2, W3, W4, W6 or W7 has an adaptive or chosen-clock observer, and I
  agree with the annex on each. W1 has no observer at all. W5's adversary is passive (known-plaintext, p. 4). W6's
  adversary has inputs that enter the state of a device with no clock control (pp. 73–79). HAC §6.1 describes
  self-synchronizing ciphers, where ciphertext enters the state, but it is a survey. A grep of HAC ch. 6 finds no
  fault, chosen-clock or adaptive-clocking model.
- **The missed work.** W5's reference list (p. 18) cites [16]: M. Gomułkiewicz, M. Kutyłowski, P. Wlaź, "Fault
  Jumping Attacks against Shrinking Generator", Dagstuhl Seminar Proceedings 06111 (2006),
  doi:10.4230/DagSemProc.06111.7.
  - It is open (CC BY 4.0). I fetched it from
    https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol06111/DagSemProc.06111.7/DagSemProc.06111.7.pdf
    (HTTP 200, 6 pp., sha256 `8f7a584946fa69ec6a917426ce867cb12f26b60271e18df958435a7ab1168856`) and read it in
    full.
  - Its adversary "can cause exactly one bit-flip within the control register and rerun the generator" (p. 2), and
    "the fault injected into the control generator will propagate" (p. 2).
  - The flip changes the control sequence, and so changes which base-register bits are output. The adversary
    compares the two outputs and builds "a system of linear equations" for the control register's state (p. 3).
- **Why this is "covered in kind".** The annex itself says the phenomenon of the cell is "interventions select the
  clocking step", and on that ground it ruled W6 out. GKW 2006 treats exactly that phenomenon: an adversarial
  state intervention in clock control, read back through the output to expose hidden state. It is not
  COVERED-literature:
  - the shrinking generator is externally clocked, not self-clocked;
  - the adversary resets, reruns and compares two runs, rather than acting adaptively within one trajectory;
  - the computation is unbounded, against a 2-bit observer;
  - the goal is state recovery, not prediction at a stated horizon;
  - no parameter of the cell is covered.
- **Two related works, unread.** GKW 2006 cites two related papers, both closed according to Unpaywall:
  - [9], "Synchronization Fault Cryptanalysis for Breaking A5/1" (WEA 2005, LNCS 3503, doi:10.1007/11427186_36).
    By its title it concerns clocking faults on A5/1, a self-clocked design, which may be closer still to the cell.
  - [10], "Fault Cryptanalysis and the Shrinking Generator" (WEA 2006, LNCS 4007, doi:10.1007/11764298_6), which
    assumes the internal clocks "can be desynchronized" (p. 2 of GKW 2006).

  These belong in the unread list. The annex's conclusion "not even covered in kind" therefore does not survive.
  On the works read once GKW 2006 is added, (i) is covered in kind, and candidate-NEW stays not assignable.
- **Who must read it.** A3 requires first-hand reading by the annex's author. The reviewer's reading does not
  substitute for it. The required change R2 is written for the author to adopt after reading.

### 4. The Rueppel sentence in REPORT.md

- **REPORT.md:143–144** reads: "Rueppel's self-decimated LFSR (Eurocrypt '87), whose own output selects a clocking
  step of 1 or 2, is essentially G_clk's clocking."
- **Rueppel, as W1 describes him (p. 2).** The generator follows W1's eq. (3), S_{t+1} = ϕ^{d(S_t)}(S_t), with
  s_t = d(S_t). In Rueppel's case s_t = 1 if σ_t = 0 and s_t = 2 if σ_t = 1, where σ is a linear recurrence
  sequence. So the step is a function of the stepped register's current state. W1 does not say "output bit"; that
  reading is an inference from "self-decimated" and eq. (3).
- **G_clk, as coded.**
  - `generators.py:107–108` sets σ₀ = L, σ₁ = L∘L and f = ℓ.
  - `generators.py:49–51` sets h ← σ_x(h), then x ← x ⊕ ℓ(h), with ℓ applied to the new h.
  - In the embedded protocol, `embedded.py:179–182` does v ← ρ_x(v), then cc ← x ⊕ a(v), h ← σ_cc(h), x ← cc ⊕ ℓ(h).
  - So the hidden register is stepped by 1 + x_t. Without an observer, x_t = x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1}, the running
    parity of the output stream (PLAN:26). With an observer, x_t ⊕ a(v) selects the step.
- **The precise difference.**
  - G_clk's selector is not a function of the hidden register's state. Because φ is a bijection and μ is uniform,
    (x_t, h_t) is uniform on C_V × C_H at every t, so x_t is independent of h_t.
  - Rueppel's step (s_t = 1 + σ_t) depends on the current output bit of the register, a function of that register's
    state. G_clk's step (1 + x_t) depends on the parity of all past output bits and on x₀.
  - G_clk does share the step set {1, 2}, the polarity (0 → one step, 1 → two steps), and a clock that depends on the
    generator's own output.
  - An exact check: G_clk on (x, h) is not of the form ϕ^{1+x} with ϕ its own one-step branch. If ϕ(1, h) had x = 0,
    then ϕ²(1, h) would have x-bit ℓ(L²h) rather than 1 ⊕ ℓ(L²h). If ϕ(1, h) had x = 1 for every h, the x-bit after
    two steps would always be 1. That needs ℓ(L²h) = 0 for all h, which is false.
- **The next sub-bullet overstates W1.** REPORT.md:145–146 says W1 "confirms that construction and Rueppel's period
  result". W1 restates the period result without proof (secondhand, A3 item 3) and notes that it agrees with its own
  p = 1/2 expectation. It does not confirm it.
- **REPORT.md:150–157 is now stale.** It says RSV was read only in abstract and that AGHP and BDVY are unread.
  Once the annex is adopted, the Literature section should be corrected forward to cite the annex (§A.25, §A.27).
  That is consequential to the annex, not part of it.

### 5. The unread list

- **Rueppel 1987 and Gollmann–Chambers 1989 (A3's named works).**
  - The annex's reasons are plausible. I reproduced them: IACR cryptodb returns HTTP 403 (Cloudflare), and
    Unpaywall gives `is_oa: false` with no repository copy. OpenAlex independently gives `oa_status: closed` and
    `any_repository_has_fulltext: false` for both DOIs.
  - I could not reach an IACR open archive for EUROCRYPT '87, because iacr.org is behind the same challenge. I
    found no author copy.
  - The reader missed no legitimate open copy that I could find.
- **Chambers–Gollmann 1988.** The DOI is confirmable: Crossref gives 10.1049/ip-e.1988.0009, "Technical memorandum.
  Generators for sequences with near-maximal linear equivalence", IEE Proc. E (1988). Unpaywall reports it closed.
  W1's reference [3] misprints the year as 1998.
- **Meier–Staffelbach 1989.** "Not fetched further" should say "not attempted". A3 item 3 asks for the reason, and
  the fetch was not tried.
- **Kholosha.** Crossref gives the INDOCRYPT 2001 title as "Clock-Controlled Shift Registers and Generalized Geffe
  Key-Stream Generator" (LNCS, doi:10.1007/3-540-45311-3_27). The annex's title should be checked against the ePrint
  landing page. Leaving the PostScript file unread is correct.
- **Missing entries.** GKW WEA 2005 and GKW WEA 2006 (Finding 3). The annex lists works found while reading under
  A3's "any further" clause, so these belong in the list.
- **Out of reach here.** OpenAlex and Semantic Scholar rate-limited further searches (HTTP 429). A Kholosha thesis
  copy on research.tue.nl returned 403. Neither is required by A3.

### 6. Overstatements and suitability for a public repository

- **Overstatements.**
  - "Not even covered in kind" for (i): Finding 3.
  - "No other row" for (ii): Finding 2.
  - The RSV and BDVY rationales: Finding 2.
  - Nothing else overstates.
- **Suitability.**
  - Quotes are short and attributed. The longest is W1's four-line Rueppel passage, which is acceptable.
  - No third-party text beyond short quotes, and no personal data. Author names, public institutional URLs and DOIs
    are fine.
  - The decision to keep downloads in scratch is right for copyrighted PDFs. Digests and URLs are adequate
    provenance under §A.42, since no enduring claim rests on a retained copy.
- **Wording to fix before committing.**
  - "Nothing here changes a repository file" will be false once the annex is committed under `review/literature/`
    (N4).
  - The header "draft, not independently reviewed" must be updated once this review is resolved (N5).
  - Challenge-page digests carry no evidential weight. They can stay as the record of a failed fetch, but the line
    should say that (N6).

## Required changes (exact text)

**R1 (§3(ii), AGHP row, "Rows / parameters covered"), reason (2).** Replace the sentence beginning "(2) Its sample
is the LFSR sequence r" with:

> (2) Its sample is the LFSR sequence r, not PE-01's record X_{0:K}. The map X_{0:K} ↦ (x₀, Y₀, …, Y_{K−1}) is
> linear and invertible, and a B1 test with |T| odd contains x₀ and is exactly unbiased. A test with |T| even is a
> linear test on the LFSR output (s₁, …, s_K). AGHP does not state this step.

**R1′ (§3(ii), AGHP row, "Tag").** Replace "No other row." with:

> Also covered in kind, by the same mechanism, are the section 1 rows on `G_lin`, `G_lin_sib` and 𝔉_lin, n = 3..8,
> whose statistic is linear in the record. These are B3k (K1, K0-worst, K0-average), B3w (K1, K0-average),
> plin_m1–m4 and plin_m1–m4_pred (K1, K0), and emb_m1_passive and emb_m1_passive_pred (K1, K0). Every permutation of
> {0,1} is v ↦ v ⊕ c, so each m = 1 passive observer is a linear filter. Passage: the proof of Proposition 1 (p. 8),
> and Lemma 1 (Vazirani), p. 5 [quote it from the PDF]. At ε = 0, a marginal is uniform iff no parity on it is
> constant, and for a fixed primitive p a parity is constant iff p divides its test polynomial. The horizon values
> need, in addition, the order of p (B3k: K_zero = 2ⁿ − 2 within scope) or the test polynomials a filter realizes,
> which AGHP does not state. Rows nonlinear in the record (B2, B4 d ≥ 2, emb_m2/m3_passive) and all `G_filt` and
> `G_clk` rows stay untagged.

Mirror the change in "Tag for (ii)", first bullet, and in §4 (ii), last sub-bullet.

**R1″ (§3(ii), RSV and BDVY rows).**
- RSV: replace "No horizon value follows from the bounds: (2w²)^k ≥ 1, so no exact zero follows." with:

  > No measured horizon follows. At ε = 0 the bound gives only exact uniformity, K_zero(class) ≥ K_zero(U), which
  > U's COVERED-corpus tag already carries. Beyond it, some parity of the `G_lin` record is constant (ε = 1) and the
  > bound is vacuous.

- BDVY: replace the sentence beginning "At most, the theorem with k = 1 yields" with:

  > With k = 1 and ε = 0 the theorem gives K_zero(m = 1 passive) ≥ K_zero(B1). That is vacuous, since an input on
  > which every linear test is exactly unbiased is uniform, so K_zero(B1) = K_zero(U) on every generator.

**R2 (§2a, §3(i), §4(i)), after the author has read GKW 2006 first-hand.**
- Add to §2a:

  > | W8 | M. Gomułkiewicz, M. Kutyłowski, P. Wlaź, "Fault jumping attacks against shrinking generator", Dagstuhl
  > Seminar Proceedings 06111 (2006), doi:10.4230/DagSemProc.06111.7, CC BY 4.0 (W5's ref. [16]) |
  > https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol06111/DagSemProc.06111.7/DagSemProc.06111.7.pdf
  > (HTTP 200, 6 pp.) | `8f7a584946fa69ec6a917426ce867cb12f26b60271e18df958435a7ab1168856` | in full |

- Add to the §3(i) table:

  > | W8 GKW 2006 | **covered in kind** | p. 2: "we shall assume that one can cause exactly one bit-flip within the
  > control register and rerun the generator"; "the fault injected into the control generator will propagate when
  > the generator is working and gradually many bits are influenced by the change". p. 3: "We take two outputs: one
  > from the correct computation, the other one – from a computation with exactly one bit in C flipped … we construct
  > a system of linear equations." | The adversary's input enters the clock-control state and changes which
  > base-register bits are output, and the output difference exposes hidden state. It is not COVERED-literature:
  > the shrinking generator is clocked by a separate register, the adversary reruns from the same state and compares
  > two runs with unbounded computation, and the goal is state recovery, not bounded-memory prediction within one
  > trajectory. No parameter of the cell is covered. |

- Replace the "Chosen-clock model" and "Tag for (i)" bullets with:

  > - **Adversary-influenced clocking.** W8 treats an adversary whose input, one bit flip in the control register of
  >   a shrinking generator, changes the clocking, and who reads the change in the output to recover the control
  >   register. No work read treats such an adversary for a self-clocked generator, or an adaptive bounded-memory
  >   observer acting within one trajectory. W6 has an adversary whose inputs enter the state, and no clock control.
  > - **Tag for (i): covered in kind (W8).** It is not COVERED-literature on the works read. Works that might cover
  >   it more closely are unread: Rueppel 1987, Gollmann–Chambers 1989, Chambers–Gollmann 1988, and Gomułkiewicz et
  >   al., WEA 2005 (A5/1) and WEA 2006.

- In §4(i), append "Gomułkiewicz et al. WEA 2005, Gomułkiewicz et al. WEA 2006" to the unread list.

If the author's own reading of W8 differs, the annex must instead state why "interventions select the clocking
step", the criterion it applied to W6, is not what W8 treats.

**R3 (§2b), additions and corrections.**
- Chambers–Gollmann 1988 row: replace "No open copy located; DOI not confirmed." with:

  > doi:10.1049/ip-e.1988.0009 (Crossref: "Technical memorandum. Generators for sequences with near-maximal linear
  > equivalence"). Unpaywall: closed. No open copy located.

- Meier–Staffelbach 1989 row: replace "not fetched further" with "not attempted".
- Add:

  > | M. Gomułkiewicz, M. Kutyłowski, T. H. Vierhaus, P. Wlaź, "Synchronization fault cryptanalysis for breaking
  > A5/1", WEA 2005, LNCS 3503, pp. 415–427, doi:10.1007/11427186_36 (W8's ref. [9]) | Unpaywall: closed. Not
  > obtained. |
  > | M. Gomułkiewicz, M. Kutyłowski, P. Wlaź, "Fault cryptanalysis and the shrinking generator", WEA 2006, LNCS 4007,
  > pp. 61–72, doi:10.1007/11764298_6 (W8's ref. [10]) | Unpaywall: closed. Not obtained. |

- Kholosha row: check the title against the ePrint landing page. Crossref gives the INDOCRYPT title as
  "Clock-Controlled Shift Registers and Generalized Geffe Key-Stream Generator".

**R4 (§5, "The difference").** Replace that sub-bullet with:

> - **The difference:** in W1's secondhand account (p. 2), Rueppel's step s_t ∈ {1, 2} is set by a bit σ_t of a
>   linear recurrence sequence. By W1's eq. (3), s_t = d(S_t), so it is a function of the register's current state.
>   `G_clk`'s hidden register is stepped by 1 + x, where x is the visible bit, the running parity
>   x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1} of the output stream (`generators.py:49–51, 107–108`). Under μ, x_t is independent of h_t.
>   In the embedded protocol the observer's action is added to x before each step (`embedded.py:179–182`).

**R5 (REPORT.md, "Literature", lines 143–146).** This is proposed for the record owner and is outside the annex.
Replace the two sub-bullets with:

```
  - Rueppel's self-decimated LFSR (Eurocrypt '87, not read here) shares G_clk's step set {1, 2} and a clock that
    depends on the generator's own output, but not its clock selector. As Agievich–Solovey (arXiv math/0505660, p. 2)
    describe it, the step at time t is 1 if σ_t = 0 and 2 if σ_t = 1, where σ is a linear recurrence sequence; with
    their eq. (3) the step is a function of the register's current state. In G_clk the hidden register steps by L_p
    when the visible bit x is 0 and by L_p² when it is 1 (`pe01/generators.py:49–51, 107–108`). That bit is the
    running parity x_t = x_0 ⊕ Y_0 ⊕ … ⊕ Y_{t−1} of the output stream and, under μ, is independent of the hidden
    state. In the embedded protocol the observer's action a(v) is added to x before each step
    (`pe01/embedded.py:179–182`), so the observer selects the step.
  - Agievich–Solovey (read in full) state Rueppel's period result without proof and do not address prediction.
```

## Nits

- **N1.** Grain hash: give it in full, `f9c6d47c3677ecbe158748d3130c43cc5c205110a25333797c997ae652c1dbd2`. The
  printed "…dc2" ending is wrong.
- **N2.** RSV p. 2 quote: drop the final full stop, or mark the quote as ending mid-sentence.
- **N3.** §1(ii): add "The 𝔉_lin B1 K0 rows at n ≥ 5 are in section 1b of `verdict.txt` (bounds, not PROVED) and
  are outside A3 item 1."
  - For the record only, not as a tag: the same closed forms predict those bounds. K0-worst K_zero = φ(2ⁿ − 1) gives
    30, 36, 126 and 128. That is consistent with the reported "K_zero ≥ 23" and "K_1/8 ≤ 31, 37, 127, 129".
- **N4.** Header: replace "Nothing here changes a repository file. Downloads stay in scratch (`pe01lit/dl_*/`) and
  are not committed." with "Downloads are not committed; each is identified by URL and sha256."
- **N5.** Status line: update after this review, per A3 item 5.
- **N6.** For each challenge-page digest, add "(the challenge page, not the work)".
- **N7.** §1(i): "then x ← x ⊕ h₀" should read "then x ← x ⊕ h₀ of the new hidden state" (`generators.py:50–51`).
- **N8.** W1 row: in "with d a function of the current state", note that this is W1's general class (3). Rueppel's
  instance is W1's description, not the paper's.

## Evidence produced by this review (scratch, not for commit)

- `revlit/txt/*.txt`: my own `pdftotext -layout` extractions, including `fj.txt` for W8.
- `revlit/dl_fj/doc.pdf`: W8, sha256 `8f7a5849…68856`.
- `revlit/probe/qcheck.py`, `pages.py`: the quote and page checks.
- `revlit/probe/aghp_check.py`: the independent 𝔉_lin B1 K0 and G_lin B3k enumeration.
- `revlit/probe/b3w_check.py`: the n = 5 𝔉_lin B3w K0-average check. It reuses the generator functions of
  `aghp_check.py`.
- The m = 1 linear-filter check ran inline. It confirmed the first constant parity at K = 13 (n = 3) and K = 61
  (n = 5).
