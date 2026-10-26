# PE-01 tag annex under A3 (r2)

- **Status.** Independently reviewed (A3 item 5): r1 ACCEPT WITH CHANGES (`REVIEW.md`), applied in r2; r2 ACCEPT
  WITH NITS (`RECHECK-r2.md`), its nits RN1 and RN4 applied in this file.
- **Provenance.** Prepared 2026-10-26 under `amendments/A3-literature-tags.md`, applied as written. The reviewed
  object is r1, `TAGS.md` (sha256 `ac3cdffed97efe2b7fa1b7b1279cfdaee76ba311df66ed767843bf325a93eb2e`).
- **Downloads** are not committed. Each is identified by URL and sha256.

## 1. In-scope results (A3 item 1)

- **(i) COUNTEREXAMPLE cell.** `G_clk`, n = 5, p = z⁵+z²+1, `emb_m2_all`, K = 7, window K′ ∈ [4, 7],
  |Pr − 1/2| = 1/8, 5/32, 5/32, 1/8, footprint 6 = θ (`results/verdict.txt:1621`).
  - **Generator, as coded** (`pe01/generators.py:41–51, 107–108`): the hidden register steps by L_p when the visible
    bit x = 0 and by L_p² when x = 1. Then x ← x ⊕ h₀, where h₀ is taken from the new hidden state.
  - **The clock selector** is the visible bit. Without an observer it is the running parity
    x_t = x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1} of the output stream. In the embedded protocol (`pe01/embedded.py:179–182`) the
    observer's action is added first: v ← ρ_x(v), then c ← x ⊕ a(v), h ← σ_c(h), x ← c ⊕ ℓ(h).
  - **The observer** is active. Its action bit a(v) selects the next clocking step.
- **(ii) Passive horizons listed as PROVED (exhaustive finite).** These are the K_zero / K_δ rows of
  `results/verdict.txt` section 1 (lines 8–1175) for observers that only read.
  - The classes are U, U_bayes, B1, B2, B3k, B3w, B4d1–3, `emb_m{1,2,3}_passive(_pred)` and `plin_m{1..4}(_pred)`,
    on `G_lin`, `G_lin_sib`, `G_filt` and `G_clk` and their families, for n = 3..8, at K1 and K0.
  - Rows already tagged by A2 (COVERED-corpus, COVERED-literature L1/L2, control generator) keep those tags. This
    annex addresses the rows tagged "untagged".
  - The 𝔉_lin B1 K0 rows at n ≥ 5 (`verdict.txt:1303–1304, 1352–1353, 1399–1400, 1446–1447`) are in section 1b
    (bounds and intervals, not PROVED). They are outside A3 item 1.

## 2. Works

### 2a. Read first-hand

Page numbers are the printed page numbers of each document.

| # | Work | How obtained | sha256 of the file read | Read |
|---|---|---|---|---|
| W1 | S. Agievich, O. Solovey, "On the periodic properties of self-decimated generators of pseudorandom numbers", arXiv:math/0505660v1 (2005) | https://arxiv.org/pdf/math/0505660 (HTTP 200, 5 pp.) | `8f49bbf72dc839b76735ef44f755f4e1de82628e08d1c58a794cc590d7d6b3d4` | in full |
| W2 | O. Reingold, T. Steinke, S. Vadhan, "Pseudorandomness for regular branching programs via Fourier analysis", arXiv:1306.3004v2 (RANDOM 2013) | https://arxiv.org/pdf/1306.3004 (HTTP 200, 27 pp.) | `647dcabc2cdc816ea465a8e2ef5285807eb4bc4ce066c32bed8608feb3e91d90` | §1 (pp. 1–5), §2.4–2.5 and the §3 statements (pp. 8–10). The full text was searched for adaptive / LFSR / shift-register / predict terms, with no hits. |
| W3 | N. Alon, O. Goldreich, J. Håstad, R. Peralta, "Simple constructions of almost k-wise independent random variables", Random Struct. Algorithms 3(3) (1992); author copy dated June 14, 1992 | https://www.wisdom.weizmann.ac.il/~oded/PSX/aghp.pdf (HTTP 200, 19 pp.) | `d185da1caa6d043065ac54d382ab659583baa184dd6e0d1d4867a6a93faddbbc` | §1–§3 (pp. 1–9) in full, and the §7 remarks (pp. 15–16). A second author copy (Feb 22, 2002), https://web.math.princeton.edu/~nalon/PDFS/aghp4.pdf, sha256 `70f3c766da6ac24c540cc9b9401662161df6fbabca72c38e2791bf0a6359ef31`, was fetched but not used for quotes. |
| W4 | A. Bogdanov, Z. Dvir, E. Verbin, A. Yehudayoff, "Pseudorandomness for width-2 branching programs", Theory of Computing 9(7):283–293 (2013) | https://theoryofcomputing.org/articles/v009a007/v009a007.pdf (HTTP 200, CC BY, 11 pp.) | `c47dbeb9886c677d53d79d674df357f3555b76a6d3730bb283d9d85c2511769b` | §1–§2.1 (pp. 283–287) |
| W5 | P. Caballero-Gil, A. Fúster-Sabater, "A simple attack on some clock-controlled generators", Comput. Math. Appl. 58(1):179–188 (2009); arXiv:1005.0095v1 author copy | https://arxiv.org/pdf/1005.0095 (HTTP 200, 18 pp.) | `397f2ce466f0515dc62fe9e0a0361f9567f706fb0f43e48a78442f17aad0e46a` | §1–2 and §6–7 in full, §3–5 skimmed, references |
| W6 | B. Zhang, H. Wu, D. Feng, F. Bao, "Chosen ciphertext attack on a new class of self-synchronizing stream ciphers", INDOCRYPT 2004, LNCS 3348, pp. 73–83; author copy | https://personal.ntu.edu.sg/wuhj/research/publications/2004_INDOCRYPT.pdf (HTTP 200, 11 pp.) | `89703372bb35e1701ee86b745c8dd01f9cdb272314d45544df6867b908b9c933` | §1–4 (pp. 73–79) in full |
| W7 | A. Menezes, P. van Oorschot, S. Vanstone, *Handbook of Applied Cryptography* (CRC 1996), Ch. 6; publisher-permitted copy | https://cacr.uwaterloo.ca/hac/about/chap6.pdf (HTTP 200, 33 pp.) | `e1b0bd755115d6b1797055291d31335c5a459c36e6179f426e114d501ddf6dc2` | §6.3.3 (p. 209) and the §6.5 notes on §6.3 (pp. 220–222). This is a handbook (a survey), so under A3 item 3 it supports no tag for the works it summarizes. |
| W8 | M. Gomułkiewicz, M. Kutyłowski, P. Wlaź, "Fault jumping attacks against shrinking generator", Dagstuhl Seminar Proceedings 06111 (2006), doi:10.4230/DagSemProc.06111.7, CC BY 4.0 (W5's ref. [16]) | https://drops.dagstuhl.de/storage/16dagstuhl-seminar-proceedings/dsp-vol06111/DagSemProc.06111.7/DagSemProc.06111.7.pdf (HTTP 200, 6 pp.) | `8f7a584946fa69ec6a917426ce867cb12f26b60271e18df958435a7ab1168856`, equal to the reviewer's independent copy | in full |

- **Fetched, not used.** https://cse.iitkgp.ac.in/conf/SPACE2013/Space2012/Grain02.pdf, sha256
  `f9c6d47c3677ecbe158748d3130c43cc5c205110a25333797c997ae652c1dbd2`. It is a slide deck on a bit-flip differential
  fault attack on Grain-128a. It is not a paper and is not about clocking.

### 2b. Unread (A3 item 3: supports no tag)

Where a digest is given for a failed fetch, it is the digest of the challenge page, not of the work. It records only
that the fetch failed.

| Work | Reason |
|---|---|
| R. A. Rueppel, "When shift registers clock themselves", EUROCRYPT '87, LNCS 304, pp. 53–64, doi:10.1007/3-540-39118-5_6 | Every route failed. **Springer** (chapter page and PDF URL): HTTP 200 serving a JavaScript "Client Challenge" page, 3038 bytes, sha256 `32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea` (the challenge page, not the work). **IACR cryptodb:** HTTP 403 Cloudflare challenge. **Unpaywall:** `is_oa: false`, no repository copy. **Semantic Scholar** `openAccessPdf`: CLOSED. No author or other legitimate open copy was found by search. |
| D. Gollmann, W. G. Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989), doi:10.1109/49.17716 | Paywall. **IEEE Xplore:** the document page returns HTTP 202 (bot interstitial); stamp.jsp returns HTTP 418 with purchase options. **Unpaywall:** `is_oa: false`. No author copy was found by search. |
| W. G. Chambers, D. Gollmann, "Generators for sequences with near-maximal linear equivalence", IEE Proc. E 135 (1988), p. 67 ff., doi:10.1049/ip-e.1988.0009 (Crossref title: "Technical memorandum. Generators for sequences with near-maximal linear equivalence"; W1's ref. [3], with the year printed there as 1998) | **Unpaywall:** closed. No open copy located. |
| T. Beth, F. Piper, "The stop-and-go generator", EUROCRYPT '84, doi:10.1007/3-540-39757-4_9 | Unpaywall lists a Springer open-access PDF. The URL returned the same Springer challenge page, sha256 `32ed6315…0e18ea` (the challenge page, not the work). |
| W. Meier, O. Staffelbach, "Fast correlation attacks on certain stream ciphers", J. Cryptology 1 (1989), doi:10.1007/BF02252874 | Unpaywall lists Springer open access. A fetch was not attempted; Springer served the challenge page to every other request. |
| W. Meier, O. Staffelbach, "The self-shrinking generator", EUROCRYPT '94, doi:10.1007/BFb0053436 | **Unpaywall:** closed. Springer challenge. |
| A. Kholosha, "Clock-controlled shift registers for key-stream generation", IACR ePrint 2001/061 (this is the ePrint title; the ePrint note says sections 1–3 and 5 appeared in INDOCRYPT 2001, which Crossref titles "Clock-Controlled Shift Registers and Generalized Geffe Key-Stream Generator", LNCS 2247, pp. 287–296, doi:10.1007/3-540-45311-3_27) | Only the landing page (the abstract) was read. **The PDF:** HTTP 403 Cloudflare page, sha256 `3ee223f11afcc9c1510af87d9b62482b8420bab131a60e44542dcfa84b869028` (the challenge page, not the work). **The PostScript copy** was downloaded (HTTP 200, sha256 `f01b43e7e1123b3e8e4442fbcd361bea9e943dfe7b013281c749dc09d87e13df`) but not interpreted, because rendering PostScript executes the downloaded program. |
| M. Gomułkiewicz, M. Kutyłowski, T. H. Vierhaus, P. Wlaź, "Synchronization fault cryptanalysis for breaking A5/1", WEA 2005, LNCS 3503, pp. 415–427, doi:10.1007/11427186_36 (W8's ref. [9]) | **Unpaywall:** closed. Not obtained. |
| M. Gomułkiewicz, M. Kutyłowski, P. Wlaź, "Fault cryptanalysis and the shrinking generator", WEA 2006, LNCS 4007, pp. 61–72, doi:10.1007/11764298_6 (W8's ref. [10]) | **Unpaywall:** closed. Not obtained. |
| J. Dj. Golić, L. O'Connor, "Embedding and probabilistic correlation attacks on clock-controlled shift registers", EUROCRYPT '94, LNCS 950; M. Živković, initial-state reconstruction of the clock-controlled shift register, IEEE Trans. IT (1991); A. Kanso, clock-controlled generators | Not obtained. No open copy located; these are on Springer and IEEE, as above. |

## 3. Tags

### 3(i) COUNTEREXAMPLE cell (`G_clk`, n = 5, `emb_m2_all`, K = 7)

| Work | Tag | Passage | Parameters covered |
|---|---|---|---|
| W8 Gomułkiewicz–Kutyłowski–Wlaź | **covered in kind** | p. 2: "we shall assume that one can cause exactly one bit-flip within the control register and rerun the generator … Of course, the fault injected into the control generator will propagate when the generator is working and gradually many bits are influenced by the change." p. 2: "Our aim is to discover the contents of the control register." p. 3: "We take two outputs: one from the correct computation, the other one – from a computation with exactly one bit in C flipped. We guess the position of the flipped bit and comparing the answer given by A on these outputs with (unknown) output of the LSFR we construct a system of linear equations." p. 1: "This is a report on work on progress". p. 5: "The yet unimplemented attack ideas show that …". | **The phenomenon:** an adversary's intervention enters the clock-control state, changes which base-register bits are emitted, and the effect on the output exposes the hidden state. **Not COVERED-literature:** (1) the shrinking generator is decimated by a separate control register, not self-clocked; (2) the intervention is one bit flip followed by a rerun from the same initial state, comparing two runs, not actions within one trajectory from a μ-uniform start; (3) the analysis assumes an idealized insertion/deletion detector A and unbounded computation, not a 2-bit-memory observer; (4) the goal is to recover the control register, not next-bit prediction at a stated horizon; (5) it is an unimplemented outline. No parameter of the cell is covered. |
| W1 Agievich–Solovey | **no bearing on prediction** | Abstract (p. 1): "We consider a self-decimated generator … and examine the preperiod λ and the period µ of its state sequence." On p. 2 W1 gives its general class (3), "S_{t+1} = ϕ^{d(S_t)}(S_t)", with d a function of the current state. It describes Rueppel secondhand: "R. Rueppel in the paper [4] examined the case when the word s is determined from a linear recurrence sequence … s_t = 1, σ_t = 0; 2, σ_t = 1 … Rueppel showed that if the characteristic polynomial … is primitive of degree k, then µ(s, T) = ⌊2T/3⌋, T = 2^k − 1". The floor brackets were lost in extraction. | **None.** W1 treats period and preperiod only, with no observer, prediction or intervention. **Step set:** {1, 2}, as in `G_clk`. **Selector:** in W1's class (3) the step is a function of the stepped register's current state; in `G_clk` it is the visible running parity after intervention. **Rueppel:** W1's account is secondhand and supports no tag for Rueppel 1987. |
| W2 RSV | **no bearing** | p. 2: "Oblivious branching programs choose which input bit to read depending only on the time step i, and not on the current state" (quote ends mid-sentence). The input string is fixed before the program runs. | None. Passive (oblivious) model, with no LFSR generator. |
| W3 AGHP | **no bearing** | §3, p. 7: the LFSR sample space, tested by "linear tests". | None. Passive linear tests and regular clocking. |
| W4 BDVY | **no bearing** | p. 285, Theorem 1.1: PRGs fooling degree-k polynomials fool "(k,t,n)-2BP" on a fixed input. | None. Passive. |
| W5 Caballero-Gil–Fúster-Sabater | **no bearing** | p. 4: "it is assumed that the feedback polynomial of the target LFSR is known … Y = {y_n} is an intercepted keystream segment"; "The use of these models implies that the known plaintext attack is applicable …". The generators are the shrinking and alternating-step generators (p. 3), each clocked by a separate register. | None. The adversary is passive (known plaintext), the clock control is external, and the attack is unbounded-computation state recovery. |
| W6 Zhang–Wu–Feng–Bao | **no bearing on parameters; related only** | p. 77: "if we choose a special ciphertext fed into the decryption circuits such that the corresponding decrypted message … is of finite length, then we can retrieve the secret keys". p. 79: "Since our attack only work in the chosen ciphertext scenario, the security of that generator is not influenced by our attack." | **Observer kind matches** A3's criterion: the adversary's inputs enter the device's state. **Generator does not:** it is an LFSR/FCSR divisor cascade with no clock control, attacked for key recovery, with no bounded-memory observer. It is not a class containing `G_clk`. Clocking is not involved, so the phenomenon of the cell is not treated. |
| W7 HAC Ch. 6 | **supports no tag (survey)** | p. 220: "Another variant of the stop-and-go generator is the step-1/step-2 generator due to Gollmann and Chambers [496]. … If the output of R1 is 0, then R2 is clocked once; if the output of R1 is 1, then R2 is clocked twice … Živković [1274] proposed an embedding correlation attack on R2". p. 221: "A recent survey of techniques for attacking clock-controlled generators is given by Gollmann [495]." | Its own statements cover external clock control and known-plaintext (passive) attacks. No adversary chooses the clocking. Its secondhand summaries of Gollmann–Chambers and Živković support no tag. |

- **Adversary-influenced clocking.** W8 treats an adversary whose input changes the clocking of a shrinking generator:
  one bit flip in its control register. The adversary reads the change in the output to recover the control
  register. No work read treats such an adversary for a self-clocked generator, or an adaptive bounded-memory
  observer acting within one trajectory. W6 has an adversary whose inputs enter the state, but no clock control.
- **Tag for (i): covered in kind (W8).** It is not COVERED-literature on the works read. Works that might cover it
  more closely are unread: Rueppel 1987, Gollmann–Chambers 1989, Chambers–Gollmann 1988, and Gomułkiewicz et al.,
  WEA 2005 (A5/1) and WEA 2006.

### 3(ii) Passive horizons listed as PROVED

| Work | Tag | Passage | Rows / parameters covered |
|---|---|---|---|
| W3 AGHP | **covered in kind.** First, the B1 K0-worst and K0-average rows on 𝔉_lin at n = 3, 4 (`verdict.txt:176–177, 372–373`). Second, every section-1 row on `G_lin`, `G_lin_sib` and 𝔉_lin, n = 3..8, whose statistic is linear in the record: **B3k** (K1 on `G_lin` and `G_lin_sib`, K0-worst, K0-average), **B3w** (K1 on `G_lin` and `G_lin_sib`, K0-average), **plin_m1–m4** (K1 on `G_lin` and `G_lin_sib`, K0-worst, K0-average), **plin_m1–m4_pred** (K1 on `G_lin` and `G_lin_sib`), **emb_m1_passive** (K1 on `G_lin` and `G_lin_sib`, K0-worst, K0-average) and **emb_m1_passive_pred** (K1 on `G_lin` and `G_lin_sib`). That is 222 "untagged" rows plus the 4 B1 K0 rows. | **Construction 1** (§3, p. 7): a uniform "non-degenerate" feedback rule (f(t) irreducible, f₀ = 1) and a uniform start sequence. **Proof of Proposition 1** (p. 8): "This linear combination can be either identically zero or not. The first case means that the polynomial f(t) divides the polynomial g(t) … whereas in the second case (α, r)₂ being a non constant combination of the s_i's is unbiased … Hence the bias of (α, r)₂, when r is uniformly selected in A^n_{2m} equals the probability that the polynomial f(t) divides the polynomial g(t)." **Lemma 1 (Vazirani)** (p. 5): "Let S_n ⊆ {0,1}^n be a sample space that is ε-biased with respect to linear tests of size at most k. Then the sample space S_n is ((1 − 2^{−k})ε, k)-independent (in max norm), and (2^k − 1)^{1/2}ε-away (in L1 norm) from k-wise independence." The symbols are reconstructed from the extraction, which drops the operators. Proposition 1 itself (p. 7) is only an upper bound, (n−1)/2^m·(1+O(2^{−m/2})). | **The mechanism.** For a fixed primitive p and a uniform start, each parity of the record is exactly unbiased or constant, and it is constant iff p divides its test polynomial. With Lemma 1 at ε = 0, a linear statistic of the record has its Q-law iff none of its parities is constant. Each tagged class is linear in the record: the B3 marginals; ρ_x(v) = Av ⊕ xb for plin (PLAN §3); and Sym({0,1}) = {v ↦ v ⊕ c} for m = 1 passive, so each m = 1 passive observer is an affine filter. **Not COVERED-literature,** for three reasons. (1) AGHP's feedback distribution is uniform over irreducible polynomials, ν over primitive ones. They coincide at n = 3, 5, 7, where 2ⁿ − 1 is prime, and not at n = 4, 6, 8. That observation is not in AGHP. (2) AGHP's sample is the LFSR sequence r, not PE-01's record X_{0:K}. The map X_{0:K} ↦ (x₀, Y₀, …, Y_{K−1}) is linear and invertible, and a parity with an odd number of X terms contains x₀ and is exactly unbiased. A parity with an even number of X terms is a linear test on the LFSR output (s₁, …, s_K). AGHP does not state this step. (3) The horizon values need further facts that AGHP does not state: the order of p (B3k, plin_m1, emb_m1_passive), the test polynomials a filter realizes (plin_m2–m4), or the largest number of family members dividing one test polynomial (B1 K0). **Check:** see the box below. **Excluded:** the B1 K1 rows on `G_lin` keep their A2 tag L1. Rows nonlinear in the record (B2, B4d2–3, `emb_m2/m3_passive`) and all `G_filt` and `G_clk` rows stay untagged. |
| W2 RSV | **not covered; not covered in kind** | pp. 2–3: "Permutation branching programs are a further restriction, where we require that for each setting of the input string, the mappings between layers are permutations." This is the observer model of passive 𝒫ᵉᵐᵇ(m), at width 2^m (PLAN §9). p. 9, Lemma 2.3: "Let X be a ε-biased random variable … ‖E[B[X]] − E[B[U]]‖_ρ = ‖Σ_{s≠0} B̂[s] X̂(s)‖_ρ ≤ L_ρ(B)ε". p. 10, Theorem 3.2: Fourier mass at level k ≤ (2w²)^k. | None. The observer class matches, but RSV says nothing about LFSR, filter or clock-controlled records. No measured horizon follows. At ε = 0 the bound gives only exact uniformity, K_zero(class) ≥ K_zero(U), which U's COVERED-corpus tag already carries. Beyond that point, some parity of the `G_lin` record is constant (ε = 1) and the bound is vacuous. For `G_filt` and `G_clk` the bound would give at most an upper bound on advantage, which RSV does not evaluate for these records. |
| W4 BDVY | **not covered; not covered in kind** | p. 285, Theorem 1.1: "Let G be an ε-PRG against degree-k polynomials … Then G is an ε′-PRG against … (k,t,n)-2BP, with ε′ = t·ε." p. 286: "read-once width-2 branching programs that read one bit at a time can be fooled by linear generators". | None. Width 2 is passive m = 1. With k = 1 and ε = 0 the theorem gives K_zero(m = 1 passive) ≥ K_zero(B1). That is vacuous: an input on which every linear test is exactly unbiased is uniform, so K_zero(B1) = K_zero(U) on every generator (`verdict.txt:505, 517`). |
| W5 Caballero-Gil–Fúster-Sabater | **no bearing on bounded passive rows** | p. 4 (quoted in 3(i)). | Passive, unbounded-computation state recovery for externally clocked generators (SG, ASG). In kind that corresponds to class U, which A2 already tags COVERED-corpus. It bears on no bounded-class row. It bears on no `G_clk` row either, because `G_clk` is not SG or ASG. |
| W1, W6, W7, W8 | **no bearing** | as in 3(i) | none |

> **Check of the AGHP extension (author's own).** The script `linear_rows.py` (sha256
> `82014750deaf9a8b8fd2d73419978ec3caf32f1f27d4a433484df2a5361d4fdb`) uses PLAN §1–§3 definitions only and no
> repository code. It enumerates every primitive polynomial of degree n and computes, by GF(2) rank, the first K at
> which some parity of the statistic is constant. It was run as `python3 -I linear_rows.py 7`, and its output has
> sha256 `3ac8448a395d2762c5d18f174dfcab9b4e8b583d47e5c731bf1675a5cd788671`. The output was compared against
> `verdict.txt` by reading.
>
> - **Predicted closed forms**, derived by the author, not stated in AGHP:
>   - **B3k** K1, K0-worst and K0-average: X_a ⊕ X_b = Y_a ⊕ … ⊕ Y_{b−1} has test polynomial (t^d + 1)/(t + 1),
>     with d = b − a, and p divides it iff ord(p) = 2ⁿ − 1 divides d. So K_zero = 2ⁿ − 2.
>   - **B3w** K1 and K0-average: K_zero = n, since a window of n + 2 symbols carries g = p.
>   - **plin_m1 and emb_m1_passive** K1 and K0: for K odd the parity v_K ⊕ X_K has test polynomial
>     ((t^{(K+1)/2} + 1)/(t + 1))², so K_zero = 2^{n+1} − 4.
> - **Measured** (`verdict.txt` section 1):
>   - B3k: 6, 14, 30, 62, 126 for n = 3..7. At n = 8 the row reads 127, the scope cap (2⁸ − 2 = 254 > 127).
>   - B3w: n, at every n.
>   - plin_m1 and emb_m1_passive: 12, 28, 60, 124, 252, 508. The emb_m1_passive K0 rows at n = 8 read 255, their
>     K ≤ 255 cap.
> - **Computed by the script, n = 3..7.** It agrees with every row compared:
>   - B3k K1 for every family member: all ≤ 3-subsets for n ≤ 5, pairs only for n = 6, 7, since odd subsets contain
>     x₀ an odd number of times;
>   - B3w K1 for every family member;
>   - plin_m1–m3 K1 on p_n and on p′_n (= `G_lin` and `G_lin_sib`), and their K0-average K_zero, which is the
>     minimum over the family. PLAN §3's plin K0 class uses linear prediction tests only. The two K_zero values
>     agree because a constant parity c·v_K without X_K equals (cA)·v_{K−1} ⊕ (c·b)X_{K−1}, so the same filter's
>     linear prediction fires at an earlier K′;
>   - plin_m4 for n ≤ 6.
>   - Examples: plin_m2 3/12, 4/12, 12/8, 36/60, 246/132 and plin_m3 3/3, 4/4, 7/7, 22/7, 24/32 for
>     `G_lin`/`G_lin_sib` at n = 3..7; K0-average plin_m2 3, 4, 8, 6, 12.
> - **Not computed:** K0-worst for plin_m2–m4, all `_pred` rows, the K_δ values of B3w K0-average, n = 8 (except
>   through the closed forms above), and plin_m4 at n = 7, 8.
> - **Status of the tag for those rows.** It rests on the linearity of the statistic, which holds by definition, not
>   on the computation.

**Tag for (ii).**
- **Covered in kind (AGHP, mechanism only):**
  - the B1 K0-worst and K0-average rows on 𝔉_lin, n = 3, 4;
  - the 222 linear-statistic rows on `G_lin`, `G_lin_sib` and 𝔉_lin listed above.
- **Every other "untagged" passive PROVED row:** untagged. No work read states or directly implies it.

## 4. candidate-NEW (A3 item 4)

- **(i) COUNTEREXAMPLE cell:** candidate-NEW not assignable. Unread:
  - Rueppel 1987, Gollmann–Chambers 1989, Chambers–Gollmann 1988;
  - Beth–Piper 1984, Meier–Staffelbach 1989, Meier–Staffelbach 1994;
  - Kholosha 2001, Golić–O'Connor 1994, Živković 1991, Kanso;
  - Gomułkiewicz et al. WEA 2005 and WEA 2006.
- **(ii) passive horizons:** candidate-NEW not assignable for the untagged rows. The same works are unread.
  - The "before any candidate-NEW tag" list of PLAN §9 has been read first-hand: RSV, AGHP and BDVY. None of them
    covers those rows.
  - A3 item 4 requires every listed work, and the A3 list includes Rueppel 1987 and Gollmann–Chambers 1989.
  - For the rows tagged "covered in kind" (AGHP: the B1 K0 rows at n = 3, 4 and the 222 linear-statistic rows),
    candidate-NEW is not assigned.

## 5. What this does not change

- **Unchanged:**
  - the verdict (`results/verdict.txt`, `verdict.json`) and the measurements;
  - conditions (a)–(f) and the controls;
  - the governing (`abs`) and sensitivity (`signed`) classifications.
- **The A2 mechanical tags** (L1–L4, `pe01/pending.py`) are unchanged. Tags bear on no verdict (§6 item 5).
- **`results/`** was only read, for comparison. No code was run against it.
- **One factual point for the REPORT's Literature section,** from W1 and the code:
  - **What the REPORT says:** "Rueppel's self-decimated LFSR … is essentially G_clk's clocking."
  - **The difference:** in W1's secondhand account (p. 2), Rueppel's step s_t ∈ {1, 2} is set by a bit σ_t of a
    linear recurrence sequence. By W1's eq. (3), s_t = d(S_t), a function of the register's current state.
  - **In `G_clk`:** the hidden register is stepped by 1 + x, where x is the visible bit, the running parity
    x₀ ⊕ Y₀ ⊕ … ⊕ Y_{t−1} of the output stream (`generators.py:49–51, 107–108`). Under μ, x_t is independent of h_t.
    In the embedded protocol the observer's action is added to x before each step (`embedded.py:179–182`).
