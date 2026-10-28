# Introduction design r7: changes from r6

**Applies:**
- the re-check of design r6, `S/paper/design-r6-review/RECHECK.md` (ACCEPT WITH CHANGES), at #918 `f256c5f4`:
  required changes C1–C6, nits 1–9 (nit 9 from its §7, the #937 sites) and owner item O2 (the Weinberg landing gate).

The r6 files in `S/paper/design-r6/` are unchanged. r7 = r6 plus the items below; the structure and scope are r6's.

## Required changes

| Item | Status | Where in r7 |
|---|---|---|
| **C1** A.8 scope: holds on the full product space, fails in general on a proper shell | Applied with the re-check's exact text at every site. **OUTLINE:** N-BH2 sentence 2; N-BH3 "is established only for a full-product shell"; §6.2 item 4 ("needs H-scramble and the closure … in a pure joint state, over whole cycles; its stated value is established only for a full-product energy shell; and it gives …"). **CLAIMS:** N-BH2 (with the diagonal-shell and Hamming counterexamples); N-BH3 ("established only on a full-product shell"; DIFF-RECHECK §5 N1 added to its sources). **DEPENDENCIES §C**, the Thm A.8 bullet ("holds when … full product space and fails in general on a proper shell") | OUTLINE §5 items 3–4, §6.2; CLAIMS; DEPENDENCIES §C |
| **C2** N-BH1 counts sentence | Applied: the re-check's text (definition of accessible advantage; the bijectivity condition on exact recovery and on P_succ ≥ 1/\|U\|; "these endpoint guarantees"), plus the 32-map clause the coordinator asked for (Departures 1). CLAIMS N-BH1 updated, with BH-01 REPORT:21 and :24 added to its sources | OUTLINE §5 item 2; CLAIMS |
| **C3** N-DI1 limited to fixed-basis statistics | Applied verbatim. Bell correlations are not attributed to memory: the planning note points to H-Bell (§3.2). CLAIMS N-DI1 updated | OUTLINE §6.1; CLAIMS |
| **C4** Process dilation: Main:496's rationality; source label | Applied verbatim: PD row ("r4:66 s4 … rational multi-time probabilities … \|C_V\| ≥ 2 (Main:496)") and S-1's second sentence ("For a law with rational probabilities, …"). This **restores a hypothesis**; it is not a sketch | OUTLINE register PD; §2 S-1 |
| **C5** Stochastic-inverse lemma: "finite square" | Applied verbatim: SI row "(= Main:133)"; r4:114 sentence 1 now reads "A finite square stochastic matrix …". This **restores a hypothesis**. Counterexample without "square": (1 0)·(1 1)ᵀ = I₁ | OUTLINE register SI; §2 sketches table |
| **C6** Page budget | Applied: the re-check's measurement (`chk/budget.py`, ±5%). Abstract 260, §1 550, §2 1,240, §3 870, §4 460, §5 480, §6 570; total ≈ 4,430 words ≈ **11.2 pp**; applications ≈ 940 words ≈ **2.4 pp**. The sketch saving is ≈ 140 words net, ≈ 0.35 pp (310 removed, 169 added), correcting r6's "275 words, 0.7 pp". Slack to 12 pp ≈ 0.8 pp. Appendix B adds ≈ 550 words outside the count | OUTLINE "Page budget" and "Fit" |

## Nits

| Nit | Status |
|---|---|
| 1. r4:164, not :162 | Applied (OUTLINE §2, "exception") |
| 2. Doukas referent | Applied verbatim: "Theorem 3 is machine-checked in its rooted form, and Doukas states the same overlap-and-return argument concurrently [Dou26, Prop. 1]" |
| 3. N-DT1 BH clause adds the covariant field equations | Applied verbatim. CHANGES-r6's R14 claim is now true |
| 4. "a minimal model with six hidden states" | Applied verbatim (Appendix B pointer) |
| 5. Pre-scope path | Applied: `S/paper/design-r6/pre-scope/` (scratch; not in the repository) |
| 6. DEPENDENCIES SM:849 wording | Applied verbatim: "AUDIT cites 'emergent dressing pending' at SM:851; both phrases are at SM:849" |
| 7. N-LIT2 in full | Applied: r5's exact text written out in OUTLINE §4 item 7 |
| 8. Pinsker in bits | Applied: the draft adds "(in bits)" (Main:166–170) |
| 9. #937 sites (re-check §7) | Applied. **§A** gains ch07:207, ch07:258, ch09:90, GR:32, Substratum:324, SM:132 and appendix-c:273. **§R** ("Handled only by PR #937") gains GR:164 and ch07:65. All are sourced "#937 REVIEW.md at `5221b53e`". Each site's text was read at `687e885b` |

**The #937 check (re-check §7) reached RECHECK.md.** It finds that r6 neither cites nor leans on any #937 site, so it
requires no change to the paper design; only nit 9 applies.

## Landing gate added (O2)

**Weinberg 1989 read first-hand.** N-CC0 states a standard number (the Planck-cutoff mismatch) that is otherwise
uncited. The paper does not land until Weinberg, *Rev. Mod. Phys.* 61, 1 (1989), is read and cited there.
- Recorded in OUTLINE §4 item 1, CLAIMS §L and DEPENDENCIES §H.
- Padmanabhan stays first on the reading list for §4.

## Departures from the reviewer's exact text

1. **C2: one clause added.** After $P_{\rm succ}\ge1/|\mathcal U|$ r7 adds "32 non-injective maps of $\{0,1\}^2$
   violate this bound", as the coordinator asked.
   - Its source is BH-01 REPORT:21 ("without bijectivity 32 maps violate the bound"), and r4:181 carried it.
   - The re-check's final clause becomes its own sentence: "These endpoint guarantees are sufficient, not necessary."
     The meaning is the same.
2. **C1, wording per site.** The coordinator's summary form is "holds on the full product space and fails in general
   on a proper shell".
   - r7 uses the re-check's exact text at each site. N-BH3 and §6.2 item 4 therefore say the value "is established
     only for a full-product shell", a statement about the evidence, not a necessity. N-BH2 and DEPENDENCIES say
     "holds … on the full product space; … differs/fails in general on a smaller/proper shell".
   - Both forms are DIFF-RECHECK N1's.
3. **C3: a planning note, not paper text.** Beside N-DI1 I added a note that Bell correlations need H-Bell. The quoted
   sentence is verbatim.

## Owner items (unchanged from r6, plus O1)

- **O1.** DIFF-RECHECK N1's correction, the one applied as C1, should also reach #936's README and CHANGE-NOTE. The
  r5 REVIEW's R1, R2 and R5 text is superseded on this point and stays as a frozen record.
- **Carried:**
  - the "H-decouple" label once #936 lands;
  - the A.8 remedy (r7 holds either way after C1);
  - the §A.42 Lean retention;
  - the R11 gates;
  - 9 VERIFY markers;
  - the title (hyphenation; "from … to");
  - Main's title.
