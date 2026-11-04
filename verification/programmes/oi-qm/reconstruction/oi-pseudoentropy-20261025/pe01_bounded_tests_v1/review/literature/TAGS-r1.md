# PE-01 tag annex under A3 (draft)

**Status: draft, not independently reviewed (A3 item 5).** Prepared 2026-10-26 under
`amendments/A3-literature-tags.md`, applied as written. Nothing here changes a repository file.
Downloads stay in scratch (`pe01lit/dl_*/`) and are not committed.

## 1. In-scope results (A3 item 1)

- **(i) COUNTEREXAMPLE cell.** `G_clk`, n = 5, p = z⁵+z²+1, `emb_m2_all`, K = 7, window K′ ∈ [4, 7],
  |Pr − 1/2| = 1/8, 5/32, 5/32, 1/8, footprint 6 = θ (`results/verdict.txt:1621`).
  - Generator, as coded (`pe01/generators.py:41–51, 107–108`): the hidden register steps by L_p when the
    visible bit x = 0 and by L_p² when x = 1, and then x ← x ⊕ h₀.
  - So the clock selector is the visible accumulator X_t = x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1}, after the observer's
    intervention x ← x ⊕ a(v). It is not the register's current output bit.
  - Observer: active. Its action bit a(v) enters x and so selects the next clocking step.
- **(ii) Passive horizons listed as PROVED (exhaustive finite).** These are the K_zero / K_δ rows of
  `results/verdict.txt` section 1 (lines 8–1175) for observers that only read:
  - U, U_bayes, B1, B2, B3k, B3w, B4d1–3, `emb_m{1,2,3}_passive(_pred)` and `plin_m{1..4}(_pred)`;
  - on `G_lin`, `G_filt` and `G_clk`, n = 3..8, at K1 and K0.
  - Rows already tagged by A2 (COVERED-corpus, COVERED-literature L1/L2, control generator) keep those tags.
    This annex addresses the rows tagged "untagged".

## 2. Works

### 2a. Read first-hand

Page numbers below are the printed page numbers of each document.

| # | Work | How obtained | sha256 of the file read | Read |
|---|---|---|---|---|
| W1 | S. Agievich, O. Solovey, "On the periodic properties of self-decimated generators of pseudorandom numbers", arXiv:math/0505660v1 (2005) | https://arxiv.org/pdf/math/0505660 (HTTP 200, PDF, 5 pp.) | `8f49bbf72dc839b76735ef44f755f4e1de82628e08d1c58a794cc590d7d6b3d4` | in full (re-read; earlier reading confirmed) |
| W2 | O. Reingold, T. Steinke, S. Vadhan, "Pseudorandomness for regular branching programs via Fourier analysis", arXiv:1306.3004v2 (RANDOM 2013) | https://arxiv.org/pdf/1306.3004 (HTTP 200, 27 pp.) | `647dcabc2cdc816ea465a8e2ef5285807eb4bc4ce066c32bed8608feb3e91d90` | §1 (pp. 1–5), §2.4–2.5 and §3 statements (pp. 8–11); grep of the full text for adaptive / LFSR / shift-register / prediction terms (no hits) |
| W3 | N. Alon, O. Goldreich, J. Håstad, R. Peralta, "Simple constructions of almost k-wise independent random variables" (Random Struct. Algorithms 3(3), 1992), author copy dated June 14, 1992 | https://www.wisdom.weizmann.ac.il/~oded/PSX/aghp.pdf (HTTP 200, 19 pp.) | `d185da1caa6d043065ac54d382ab659583baa184dd6e0d1d4867a6a93faddbbc` | §1–§3 (pp. 1–9) in full; §7 remarks (pp. 15–16). A second author copy (Alon, dated Feb 22, 2002), https://web.math.princeton.edu/~nalon/PDFS/aghp4.pdf, sha256 `70f3c766da6ac24c540cc9b9401662161df6fbabca72c38e2791bf0a6359ef31`, was fetched and not used for quotes. |
| W4 | A. Bogdanov, Z. Dvir, E. Verbin, A. Yehudayoff, "Pseudorandomness for width-2 branching programs", Theory of Computing 9(7):283–293 (2013) | https://theoryofcomputing.org/articles/v009a007/v009a007.pdf (HTTP 200, CC-BY, 11 pp.) | `c47dbeb9886c677d53d79d674df357f3555b76a6d3730bb283d9d85c2511769b` | §1–§2.1 (pp. 283–287) |
| W5 | P. Caballero-Gil, A. Fúster-Sabater, "A simple attack on some clock-controlled generators", Comput. Math. Appl. 58(1):179–188 (2009); arXiv:1005.0095v1 author copy | https://arxiv.org/pdf/1005.0095 (HTTP 200, 18 pp.) | `397f2ce466f0515dc62fe9e0a0361f9567f706fb0f43e48a78442f17aad0e46a` | §1–2 and §6–7 in full; §3–5 skimmed |
| W6 | B. Zhang, H. Wu, D. Feng, F. Bao, "Chosen ciphertext attack on a new class of self-synchronizing stream ciphers", INDOCRYPT 2004, LNCS 3348, pp. 73–83; author copy | https://personal.ntu.edu.sg/wuhj/research/publications/2004_INDOCRYPT.pdf (HTTP 200, 11 pp.) | `89703372bb35e1701ee86b745c8dd01f9cdb272314d45544df6867b908b9c933` | §1–4 (pp. 73–79) in full |
| W7 | A. Menezes, P. van Oorschot, S. Vanstone, *Handbook of Applied Cryptography* (CRC 1996), Ch. 6, publisher-permitted copy | https://cacr.uwaterloo.ca/hac/about/chap6.pdf (HTTP 200, 33 pp.) | `e1b0bd755115d6b1797055291d31335c5a459c36e6179f426e114d501ddf6dc2` | §6.3.3 (p. 209) and §6.5 notes on §6.3 (pp. 220–222). This is a handbook (survey). Under A3 item 3 it supports no tag for the works it summarizes. |

Fetched and not used: `dl_grain_clk/` (https://cse.iitkgp.ac.in/conf/SPACE2013/Space2012/Grain02.pdf,
sha256 `f9c6d47c…dc2`). It is a slide deck on a bit-flip differential fault attack on Grain-128a, not a paper and
not about clocking.

### 2b. Unread (A3 item 3: supports no tag)

| Work | Reason |
|---|---|
| R. A. Rueppel, "When shift registers clock themselves", EUROCRYPT '87, LNCS 304, pp. 53–64, doi:10.1007/3-540-39118-5_6 | Every route failed. Springer chapter page and PDF URL: HTTP 200 serving a JavaScript "Client Challenge" page (3038 bytes, sha256 `32ed6315…18ea`), not the paper. IACR cryptodb: HTTP 403 Cloudflare challenge. Unpaywall: `is_oa: false`, no repository copy. Semantic Scholar `openAccessPdf`: CLOSED. No author or other legitimate open copy found by search. |
| D. Gollmann, W. G. Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989), doi:10.1109/49.17716 | Paywall. IEEE Xplore document page: HTTP 202 (bot interstitial). stamp.jsp: HTTP 418 with purchase options. Unpaywall: `is_oa: false`. No author copy found by search. |
| W. G. Chambers, D. Gollmann, "Generators for sequences with near-maximal linear equivalence", IEE Proc. E 135 (1988), pp. 67–69 (W1's ref. [3] for self-decimated generators) | Not obtained. No open copy located; DOI not confirmed. |
| T. Beth, F. Piper, "The stop-and-go generator", EUROCRYPT '84, doi:10.1007/3-540-39757-4_9 | Unpaywall lists a Springer open-access PDF. The URL returned the same Springer "Client Challenge" page (sha256 `32ed6315…18ea`). |
| W. Meier, O. Staffelbach, "Fast correlation attacks on certain stream ciphers", J. Cryptology 1 (1989), doi:10.1007/BF02252874 | Unpaywall lists Springer open access. Springer is behind the same challenge; not fetched further. |
| W. Meier, O. Staffelbach, "The self-shrinking generator", EUROCRYPT '94, doi:10.1007/BFb0053436 | Unpaywall: closed. Springer challenge. |
| A. Kholosha, "Clock-controlled shift registers for key-stream generation", IACR ePrint 2001/061 (INDOCRYPT 2001) | Landing page read (abstract only). PDF: HTTP 403 Cloudflare "Just a moment" page (sha256 `3ee223f1…9028`). The PostScript copy downloaded (HTTP 200, sha256 `f01b43e7e1123b3e8e4442fbcd361bea9e943dfe7b013281c749dc09d87e13df`) was not interpreted, because rendering PostScript executes the downloaded program. Unread. |
| J. Dj. Golić and L. O'Connor, embedding/probabilistic correlation attacks on clock-controlled shift registers (EUROCRYPT '94); M. Živković, initial-state reconstruction of the clock-controlled shift register (IEEE Trans. IT, 1991); A. Kanso, clock-controlled generators | Not obtained. No open copy located (Springer and IEEE, as above). |
| AGHP | Now read (W3). |
| RSV | Now read (W2), beyond the abstract. |
| BDVY | Now read (W4). |

## 3. Tags

### 3(i) COUNTEREXAMPLE cell (`G_clk`, n = 5, `emb_m2_all`, K = 7)

| Work | Tag | Passage | Parameters covered |
|---|---|---|---|
| W1 Agievich–Solovey | **no bearing on prediction** | The abstract (p. 1): "We consider a self-decimated generator … and examine the preperiod λ and the period µ of its state sequence." On p. 2 the paper gives the class "S_{t+1} = ϕ^{d(S_t)}(S_t)" with d a function of the current state, and states, secondhand: "R. Rueppel in the paper [4] examined the case when the word s is determined from a linear recurrence sequence … s_t = 1, σ_t = 0; 2, σ_t = 1 … Rueppel showed that if the characteristic polynomial … is primitive of degree k, then µ(s, T) = ⌊2T/3⌋, T = 2^k − 1" (floor brackets lost in extraction). | None. Period and preperiod only. No observer, prediction or intervention. Step set {1, 2} as in `G_clk`. W1's d is a function of the current state; `G_clk`'s selector is the visible accumulator after intervention. W1's account of Rueppel is secondhand and supports no tag for Rueppel 1987. |
| W2 RSV | **no bearing** | p. 2: "Oblivious branching programs choose which input bit to read depending only on the time step i, and not on the current state." The input string is fixed before the program runs. | None. Passive (oblivious) model, no LFSR generator. |
| W3 AGHP | **no bearing** | §3, p. 7: the LFSR sample space, tested by "linear tests". | None. Passive linear tests, regular clocking. |
| W4 BDVY | **no bearing** | p. 285, Theorem 1.1: PRGs fooling degree-k polynomials fool "(k,t,n)-2BP" on a fixed input. | None. Passive. |
| W5 Caballero-Gil–Fúster-Sabater | **no bearing** | p. 4: "it is assumed that the feedback polynomial of the target LFSR is known … Y = {y_n} is an intercepted keystream segment"; "The use of these models implies that the known plaintext attack is applicable …". Generators are the shrinking and alternating-step generators (p. 3), clocked by a separate register. | None. Passive known-plaintext adversary. External (not self-) clock control. Unbounded-computation state recovery. |
| W6 Zhang–Wu–Feng–Bao | **no bearing on parameters; related only** | p. 77: "if we choose a special ciphertext fed into the decryption circuits such that the corresponding decrypted message … is of finite length, then we can retrieve the secret keys". p. 79: "Since our attack only work in the chosen ciphertext scenario, the security of that generator is not influenced by our attack." | Observer kind matches A3's criterion: the adversary's inputs enter the device's state. Generator does not: an LFSR/FCSR divisor cascade with no clock control, with key recovery as the goal and no bounded-memory observer. Not a class containing `G_clk`, so not COVERED-literature. The phenomenon of the cell (interventions select the clocking step) is not treated, so not "covered in kind". |
| W7 HAC Ch. 6 | **supports no tag (survey)** | p. 220: "Another variant of the stop-and-go generator is the step-1/step-2 generator due to Gollmann and Chambers [496]. … If the output of R1 is 0, then R2 is clocked once; if the output of R1 is 1, then R2 is clocked twice … Živković [1274] proposed an embedding correlation attack on R2". p. 221: "A recent survey of techniques for attacking clock-controlled generators is given by Gollmann [495]." | Its own statements cover external clock control and known-plaintext (passive) attacks. No adversary-chosen clocking. The secondhand summaries of Gollmann–Chambers and Živković support no tag. |

- **Chosen-clock model.** No work read first-hand treats an observer or adversary whose inputs influence the
  clocking of a clock-controlled or self-clocked generator: neither a clock-control-injection nor a chosen-clock
  model. W6 is the only work read with an adversary whose inputs enter the state, and it has no clock control.
- **Tag for (i): none.** It is neither COVERED-literature nor "covered in kind" on the works read. The works that
  might cover it in kind (Rueppel 1987, Gollmann–Chambers 1989, Chambers–Gollmann 1988) are unread.

### 3(ii) Passive horizons listed as PROVED

| Work | Tag | Passage | Rows / parameters covered |
|---|---|---|---|
| W3 AGHP | **covered in kind** for the B1 K0-worst and K0-average rows on 𝔉_lin at n = 3, 4 (`[n3-lin]`, `[n4-lin]` "B1 K0-… on family"). No other row. | §3, p. 7, Construction 1: feedback rule uniform over "non-degenerate" rules (f(t) irreducible, f₀ = 1), start sequence uniform. Proof of Proposition 1, p. 8: "This linear combination can be either identically zero or not. The first case means that the polynomial f(t) divides the polynomial g(t) … whereas in the second case (α, r)₂ being a non constant combination of the s_i's is unbiased … Hence the bias of (α, r)₂, when r is uniformly selected in A^n_{2m} equals the probability that the polynomial f(t) divides the polynomial g(t)." Proposition 1 itself (p. 7) is only an upper bound, (n−1)/2^m·(1+O(2^{−m/2})). | Covers the mechanism. For a fixed feedback polynomial, each linear test is exactly unbiased or constant. The family bias is the probability that the polynomial divides the test polynomial. It does not state the horizons. (1) Its feedback distribution is uniform over irreducible polynomials, while ν is uniform over primitive ones. These coincide at n = 3 (2³−1 prime), not at n = 4; that observation is not in AGHP. (2) Its sample is the LFSR sequence r, not PE-01's accumulated record X_{0:K}. (3) The horizon values need the maximum over tests of the number of family members dividing g, which AGHP does not compute. So not COVERED-literature. The B1 K1 rows on `G_lin` keep their A2 tag L1. |
| W2 RSV | **not covered; not covered in kind** | pp. 2–3: "Permutation branching programs are a further restriction, where we require that for each setting of the input string, the mappings between layers are permutations." This is the observer model of passive 𝒫ᵉᵐᵇ(m), at width 2^m (PLAN §9). p. 9, Lemma 2.3: "Let X be a ε-biased random variable … ‖E[B[X]] − E[B[U]]‖_ρ = ‖Σ_{s≠0} B̂[s] X̂(s)‖_ρ ≤ L_ρ(B)ε". p. 10, Theorem 3.2: Fourier mass at level k ≤ (2w²)^k. | None. The observer class matches. RSV states error bounds for its own generator and for small-bias inputs; it states nothing about LFSR, filter or clock-controlled records. No horizon value follows from the bounds: (2w²)^k ≥ 1, so no exact zero follows. |
| W4 BDVY | **not covered; not covered in kind** | p. 285, Theorem 1.1: "Let G be an ε-PRG against degree-k polynomials … Then G is an ε′-PRG against … (k,t,n)-2BP, with ε′ = t·ε." p. 286: "read-once width-2 branching programs that read one bit at a time can be fooled by linear generators". | None. Width 2 is passive m = 1. At most, the theorem with k = 1 yields a one-sided bound, K_zero(m = 1 passive) ≥ K_zero(B1), on generators whose records pass all linear tests. That is weaker than the measured rows (for example `[n5-lin]` emb_m1_passive K_zero = 60 against B1 K_zero = 5) and is not stated by BDVY. |
| W5 Caballero-Gil–Fúster-Sabater | **no bearing on bounded passive rows** | p. 4 (quoted in 3(i)). | Passive, unbounded-computation state recovery for externally clocked generators (SG, ASG). That corresponds in kind to class U, which A2 already tags COVERED-corpus. It bears on no bounded-class row, and on no `G_clk` row: `G_clk` is not SG or ASG. |
| W1, W6, W7 | **no bearing** | as in 3(i) | none |

**Tag for (ii).**
- **B1 K0-worst and K0-average on 𝔉_lin, n = 3, 4:** covered in kind (AGHP, mechanism only).
- **Every other "untagged" passive PROVED row:** untagged. No work read states or directly implies it.

## 4. candidate-NEW (A3 item 4)

- **(i) COUNTEREXAMPLE cell:** candidate-NEW not assignable. Unread: Rueppel 1987, Gollmann–Chambers 1989,
  Chambers–Gollmann 1988, Beth–Piper 1984, Meier–Staffelbach 1989, Meier–Staffelbach 1994, Kholosha 2001,
  Golić–O'Connor 1994, Živković 1991, Kanso.
- **(ii) passive horizons:** candidate-NEW not assignable for the untagged rows. The same works are unread.
  - The "before any candidate-NEW tag" list of PLAN §9 is now read first-hand (RSV, AGHP, BDVY), and none covers
    those rows.
  - A3 item 4 requires every listed work, and the A3 list includes Rueppel 1987 and Gollmann–Chambers 1989.
  - For the rows tagged "covered in kind" (AGHP), candidate-NEW is not assigned.

## 5. What this does not change

- The verdict (`results/verdict.txt`, `verdict.json`), the measurements, conditions (a)–(f), the controls, and the
  governing (`abs`) and sensitivity (`signed`) classifications are unchanged.
- The A2 mechanical tags (L1–L4, `pe01/pending.py`) are unchanged. Tags bear on no verdict (§6 item 5).
- No code was run against `results/`.
- One factual point for the REPORT's Literature section, from W1 and the code:
  - **What the REPORT says:** "Rueppel's self-decimated LFSR … is essentially G_clk's clocking."
  - **The difference:** W1's secondhand description has the step selected by the register's own output bit
    σ_t. `G_clk`'s step is selected by the visible accumulator x after the observer's intervention
    (`generators.py:49–51`).
