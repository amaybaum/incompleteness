# Mapping part B4: I-246 to I-312 (§6.1–§6.4, Code, data and formal verification)

**Rows:** 71 (67 claims plus the sub-claims I-296.a/b and I-297.a/b).

**Read at:** corpus `eae01647` (S/tree939, plus `git show` for `papers/oi_lattice_code/` and
`verification/programmes/`). The Introduction is read at `4a260ca9`. #939 changed none of the sites this range
depends on: its edits to Main, GR, ch07 and appendix C concern only the ħ framing.

## Counts

| Verdict | Rows |
|---|--:|
| FAITHFUL | 60 |
| IMPRECISE | 8 |
| UNDERCLAIM | 3 |
| OVERCLAIM, MISCITED, UNSUPPORTED | 0 |

## Non-FAITHFUL rows, ranked by severity

1. **I-258 (§6.2 item 2) and I-281 (§6.3): UNDERCLAIM, medium.** Both say that "which of (iii)–(v) a physical
   substratum supplies" is open. The corpus has a kernel-checked negative result for the presently stated
   architecture:
   - Finite bijective read-write dynamics with the observer's stated access generates only monomial operators. It
     sources no phases and no dense unitary control: `frozen_sourcing_verdict`, `readWriteSourced_not_qm`,
     `substratum_residual`. ROADMAP lists this under "Settled negatively — INDEPENDENT" (ROADMAP:1529, :1538).
   - Adding one continuous off-diagonal controllability resource, with the phase intervention assumed, gives exact
     finite operational QM: `substratum_extension_quantum_iff_drives`, `substratum_plus_control_qm`, and the
     layer-flow form (GR:260, :266).

   What remains open is ROADMAP F2: whether a physical substratum supplies that resource. The Introduction cites
   GR:228's framing sentence. GR's later paragraphs narrow that sentence, and the Introduction does not follow them.
   The abstract (I-0xx) and §3.2 (line 120) carry the same wording, so the fix must reach them too (§A.25). Fixes
   are in the JSON.
2. **I-292 (§6.3 item 3): UNDERCLAIM, medium-low. Owner decision.** "Exact gluing for recurrent target families" is
   listed as open. The kernel settles the rooted-family version: `finiteRootedRealizable_iff_pper`
   (RootedClassificationAllTime:192). A rooted family is realizable at every time by one finite reversible system
   exactly when it is periodic, row-stochastic and the identity at the root, and the construction is explicit. The
   census registry has this result as kernel-only, and no manuscript carries it. The full multi-time-law version
   remains open. Main:618 and ROADMAP:1569 also omit the rooted result.
3. **I-294 (§6.3 item 4): IMPRECISE, low.** The Introduction lists "(C2) necessity" as an open problem. Main proves
   it on paper under the mixing hypothesis (Main:433, :447), and Main's ledger (Main:720) and GR:565 both say
   "conditional". The open item is the mixing hypothesis itself, which ROADMAP:1591 lists as a declared input.
4. **I-246 (§6.1): IMPRECISE, low.** "the fixed-basis statistics of quantum theory are the visible laws of an
   embedded observer" has no horizon qualifier. The kernel shows that the all-time reading fails:
   `qStar_not_subset_finiteRootedRealizable`. A non-permutation fixed-basis family is nonperiodic, so one fixed
   finite system cannot record it at all times. Fix: add "at every finite horizon".
5. **I-300 (§6.4): IMPRECISE, low.** "Exact operational quantum mechanics is reached only under …" drops "finite".
   Theorem 4 is proved for finite carriers only, and H-∞ is open (ROADMAP:71).
6. **I-299 (§6.4): IMPRECISE, low. Attention item resolved.** "Deterministic completion" is undefined in the
   Introduction; the defined term is "faithful realization", which matches Main's "faithful deterministic
   completion". The content is Theorem 2(c) together with the Corollary. Because the antecedent is "memory", no
   M_t>0 qualifier is missing. The fix is to the term only.
7. **I-289 (§6.3 item 1): IMPRECISE, low.**
   - Every step it lists is indeed unformalized; a grep of OIBridge found no CMI vanishing criterion, Pinsker bound,
     prior-independent dilation or history-level (C4) proof.
   - The list omits other paper-only steps: §3.1's Hadamard example and §3.4's factorization half.
8. **I-265 (§6.2 item 4): IMPRECISE, low.** §5 cites BHa item F and BHb C6(b)–(d). Item F is timescale arithmetic on
   GR's formulas, and C6(b)–(d) are textual analyses of GR's theorems. Neither is a "finite toy model".
9. **I-277 (§6.2 item 7): IMPRECISE, low.** The sentence says "§4 is conditional". Only §4's proposal is conditional;
   its descriptive distinction is established (GR:356).
10. **I-280 (§6.2 item 8): IMPRECISE, low.** "What the paper states are the cited theorems" is too narrow. The paper
    also states a hypothesis, a proposal, computations, open problems and uncited examples.

## Requested checks

- **§6.2/§6.3 against ROADMAP:**
  - The items listed as open are open. The exceptions are the partially settled items above: (iii)–(v), gluing at
    the rooted level, and the (C2) mislabel.
  - Open items missing from §6.3:
    - P0, the selection of the relating evolution. The abstract and §3.3 carry it; §6.3 does not.
    - H-∞, finite to continuum. It is not mentioned anywhere in the Introduction.
    - The (Obs, μ) observer interface (ROADMAP:70).
    - The Born-exponent origin. §3.5 carries it.
    - Physical (C4) at the lattice cut. Only the cosmological cut is listed.
  - Partial negatives the Introduction omits:
    - The hop-metric obstruction upstream of H-Bell (ROADMAP:963).
    - The canonical predictive quotient (Main:600), which is proved.
  - Positive confirmations: H-scramble, H-decouple, the proper shell, the single trajectory and G3 are open in GR
    and ROADMAP exactly as stated.
- **§6.4 I-299:** resolved above (IMPRECISE, terminology only).
- **Code section:**
  - **I-308.** Toolchain confirmed. At `17b830bc`, `lean-toolchain` is `leanprover/lean4:v4.33.0`, and the lakefile
    pins mathlib at the tag `v4.33.0`.
    - No `lake-manifest.json` is committed. The README records what the job resolved: mathlib `db584cd6` and its
      dependency SHAs.
    - The attested job replayed all 226 modules from cache, which the README discloses. The recipe, starting from
      an empty `.lake`, re-elaborates.
  - **I-309.** The `git diff` of both Lean trees, from `17b830bc` to `b64919cd` and to `eae01647`, is empty.
  - **I-310.** `PERMITTED = {propext, Classical.choice, Quot.sound}` (`tools/lean_axiom_check.py:47`).
  - **I-311.**
    - I checked all 28 Appendix A declarations in `results-121598983127.json`. Each has exactly one report, and
      every report is exactly the three axioms.
    - Each module:line matches the declaration's `theorem` line.
    - The only report using fewer axioms is `levelOne_eq` (propext only). Appendix A does not cite it.
    - **Correction to the brief:** `papers/introduction_repro/` exists only at #918's head `4a260ca9`. It is not at
      `eae01647` or at `b64919cd`.
    - This checks the retained record, not a rebuild.
  - **I-312.** The recipe's tools exist at `48b18ac5` on main, and the extractor blob matches. The compare step reads
    `papers/introduction_repro/…` by relative path, so the recipe implicitly needs a clone at #918 or its landing.

## For the owner

1. **[Main]'s title** is "The Equivalence of Quantum Mechanics and Embedded Observation" (Main:2). The Introduction
   cites it verbatim at line 261. Main itself scopes the phrase:
   - Main:20: "the exact equivalence claim is at the finite observable-law level; universal Hilbert-space
     representability is not promoted into a uniqueness theorem for operational quantum mechanics entire".
   - Main:758: the phrase "has a precise theorem-level meaning: exact bidirectional equivalence of finite observable
     stochastic laws and their quantum representations".

   GR §3.3 proves that bare finite OI does not imply QM, which matches the Introduction's I-145 and I-252. The title
   is therefore stronger than Main's own scoped claim. The Introduction must cite the actual title, so the remedy
   lies in Main. One option is to retitle Main to name the finite-law equivalence. Methodology:585 and
   Structure:1416 carry the same title.
2. **Report the stated-substratum negative result?** Recommended: yes (I-258, I-281, the abstract, §3.2).
3. **Mention the kernel-only all-time results?** These are `finiteRootedRealizable_iff_pper` and
   `qStar_not_subset_finiteRootedRealizable` / `qStar_inclusion_iff_nonempty` (I-246, I-292).
4. **Empirical record.** The Introduction says "No claim that the physical hypothesis is … tested" (I-269), and the
   abstract lists "any test of the hypothesis" as open. Appendix A reports empirical comparisons for S-class rows.
   Those rows test OI together with a specific substratum and named hypotheses, not OI as stated in §1.1. Decide
   whether the Introduction should say so.

## Corpus findings, recorded and not fixed

- **"Dissolution" headings.** GR §6 (GR:326), Book §7.7 (ch07:163) and ch18:142/146 use the word in their headings.
  Their bodies qualify it as conditional.
- **Appendix C:317** says "the derivations are explicit and the proofs are complete", although GR's G3 is open.
- **Main:758** treats the operational residual as "the remaining operational-lifting problem". That leaves out the
  INDEPENDENT verdict for the present architecture.
- **Main:594.** The probe (`memory_probes.py`) minimizes over uniform priors only, and its "1 of 15" count groups
  processes by their t=2 conditionals. My countercheck over arbitrary priors, grouped by full law, gives 2 of 16
  attaining M_t and 14 failing, with residuals of 1/3 or 2/3 bit. The countercheck is
  `/tmp/claude-0/-home-user-incompleteness/57e93868-2ccb-5ebd-afb7-d31826198729/scratchpad/b4probe/fixeddim.py`,
  convex in the split and solved with Nelder–Mead restarts. Main's "FALSE" stands; its evidence sentence overstates
  what the probe covers.
- **BHa REPORT:3** says "unreviewed for adoption", while the Introduction's reference entry says "internally
  reviewed". This is outside my range.
- **GR:545** lists a predicted dark-sector fraction (Ω_CDM+Ω_Λ ≈ 95%). This does not contradict I-275, which is
  about Λ or Ω_Λ alone.

## Notes on the fields

- **Code-section `proof_status`.** For I-308 to I-312, `proof_status` means "the repository or infrastructure fact is
  verified". It is not a mathematical status.
- **Scope disclaimers.** For I-266 and I-268, `proof_status` is `open`: the disclaimed proposition is not established
  anywhere.
- **Generator.** The JSON is generated by
  `/tmp/claude-0/-home-user-incompleteness/57e93868-2ccb-5ebd-afb7-d31826198729/scratchpad/b4probe/gen_b4.py`.
