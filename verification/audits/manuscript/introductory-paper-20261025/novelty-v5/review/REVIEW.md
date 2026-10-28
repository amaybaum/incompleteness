# Review: novelty and fidelity audit, revision 5

**Objects.** `introaudit/novelty-v5/AUDIT.md`, sha256 `ef9d475c638acf71…787a`;
`introaudit/novelty-v5/CHANGES.md`, sha256 `93f442dd88e54016…40af`.
The inputs' hashes were verified as the audit states them: v4 `34764346…f616`,
BH `c7475d09…ce0d`, LC `005cfe94…1c26`. Both review addenda (`revlitbh` and `revlitcorr`) give
ACCEPT at exactly those hashes.

**Repository.** `novelty5/repo`, fetched `origin/main` = `a411bf46` (2026-10-25 20:27 +0200,
"Merge #919"). It was read with `git show` only, and nothing in the clone was changed. Extracts
are in `revnov5/m/`. The diff `8dc36d55..a411bf46` touches only
`papers/Explainer.{md,tex,pdf}`.
- The Explainer.md blob at `a411bf46` is `a6d4cb2b`, identical to #919's head `240e31e8`, so
  the audit read exactly what landed.
- The diff is line-for-line (1064 lines both sides), so every `Explainer:NNN` citation still
  resolves.
- Main, GR, ch07 and appendix-b are byte-identical between the two commits.

## Verdict: BLOCK (wording only; no new reading is needed to clear it)

The core verdicts survive checking:
- every FT comparison that moves a candidate to KNOWN or PARTLY KNOWN;
- the C16 split;
- the F1–F20 statuses;
- the handling of C8-R and F13.

Five status claims are stronger than their evidence, which under the claim/evidence rule is a
blocker. They are findings 1–5:
- one KNOWN rests on a concurrent source;
- the proposed paper sentence says "machine-checked" of a step that Main:99 states is not
  formalized;
- §7 asserts an FT basis that several classes lack;
- the C8-R entry does not name a located construction that covers its sufficiency half;
- the audit's base is stale on #919.

Findings 6–9 are also required, because they concern fidelity or propagation. Findings 10–16
are nits.

## What was checked

**FT comparisons.** More than 30 were re-located in the reviewers' `pdftotext` files, with a
page-indexed search (`revnov5/py/pg.py`). Every cited proposition, page and equation says what
the audit says. Every FT comparison that moves a class is included:
- **C6:** B26 Thm 3.1 (p. 5), Thm 3.3 (p. 7), fn 1 (p. 8), Eq. (50) (p. 9), §4 (pp. 11–12);
  SCH Thms 1 (p. 5) and 2 (p. 10).
- **C7:** BB (PDF p. 167); B23 v2 fn 5 (p. 11); B25 v3 p. 12 and §3.5 (p. 13); PI p. 13.
- **C8:** BD Prop. 1 and Lemma 2 "trivial" (p. 5); DO3 Prop. 1 (p. 20).
- **C2:** B23 v2 §4.3 (p. 19).
- **C1 and C1′:** EG Props. 9, 11–13 and 16–18 (pp. 26–35); LPW Prop. 1.5.
- **C5:** GO Lemma 6 (p. 6), fn 8 (p. 6), App. A (p. 43).
- **C8-D and the analogues:** HHO Prop. 1 (p. 3); BCN Ex. 2 (p. 7); BI Thm 2.1 (p. 5);
  PI Fig. 4 (p. 6) and p. 17.
- **C13, C14:** SC Def. 5 (p. 9) and Thm 5 (p. 16); MO pp. 2 and 8; GH pp. 4–5.
- **XOR and C1:** DO3 App. A (pp. 36–37) and §4.1 (p. 19).
- **C16a–C16d:** Page 2013 Eq. (8) (pdf p. 11) and the t₁/₂ remark (p. 12); Page 2005
  Eqs. (5)–(10) (pp. 10–11) and (19)–(21) (p. 13); HIM fn 16 (p. 15); Penington p. 12;
  Page 1993 Eq. (10).

No FT tag rests only on an abstract or a record. Calvo's journal article, Ding–Rhee, WVB,
Pleasance and Alishahiha are all correctly tagged REC or NR.

**Manuscript lines checked at `a411bf46`:**
- **Main:** :20, :56–62, :86–94, :98–99, :121, :139, :149, :167–170, :204–220, :270–272, :332,
  :350, :409, :496–538, :544, :578–608, :624–636, :680, :690, :716, :728, :742, :748, and the
  bibliography.
- **GR:** :20, :605–611, :805, :847, :855–871.
- **ch07:** :12, :137–157.
- **Explainer:** :98–123, :287, :358, :378, :422, :1020–1026.
- **appendix-b:** :22, :406, :455.
- **glossary:** :39, :113.
- **Substratum:** :111, :126.
- **Mirrors:** ch09:127, ch18:148, ch19:72, and the FULL.md lines the audit lists.

**Lean citations checked** (all correct at `a411bf46`):
- `S_imp_D` :422, `finite_horizon_equivalence` :462–468, `D_imp_Qfb` :294, `Qfb_imp_S` :245,
  and `RevReal` :150–156;
- EquivalenceChain:110, :293, :388;
- RecurrenceHorizon:148; RootedClassification:339 and `PPer` :31; RootedClassificationAllTime
  :162 and :192;
- PhysicalC4Discharge:122; PhysicalC4StorageReadback:256; HiddenMemory:54–63 and :185;
  C3Necessity:80 and :117; CanonicalMeasure:242;
- census families 1, 34 and 40, with families 34 and 40 marked `kernel-only` and
  `manuscript: []`;
- `ARCB/result.md:113–127`, blob `05e9f35b`.

## Findings

### Required (blocking: status stronger than evidence)

**1. The XOR example is classed KNOWN on a concurrent source.**
- *Location:* §3, "Other items the literature studies touched".
- *Problem:* KNOWN rests on DO3 App. A. App. A is in v3 only: neither DO1 nor DO2 contains
  "XOR", by grep of `revlitcorr/txt`. v3 was posted 19 Oct 2026. Main:606's example is in
  `review4_probes.py` from that file's first commit, `e6c21398` (2026-08-11), lines 6–8
  ("X2 = X0 XOR X1 … T^(1) = T^(2) = J/2 … Lambda = I").
- On the audit's own dating standard, which it applies to C8, DO3 App. A is concurrent, not
  prior. KNOWN requires prior art.
- *Fix:*
  - Re-tag the example "concurrent: DO3 v3 App. A".
  - Class it KNOWN, PROVISIONAL only once a prior source is named. The classical candidate is
    Feller 1959, *Ann. Math. Stat.* 30, a non-Markov process with the semigroup
    (Chapman–Kolmogorov) property; it is NR and named from memory. The quantum analogue
    already cited by Main is Milz et al. [10], PRL 123, 040401 (2019), "CP-divisibility does
    not mean Markovianity", Main:149.
  - Add both to §5.

**2. The proposed novelty statement says "(machine-checked)" of a step that Main:99 says is
not formalized.**
- *Location:* §7, the quoted statement: "every deterministic completion carries at least the
  visible predictive information in its hidden state (machine-checked)".
- *Problem:*
  - The kernel theorem is stated for an arbitrary joint law `w` on `Hist × V × H`
    (`HiddenMemory:54–57`).
  - Main:99 says that reading a realization's time-$t$ law as that joint law "is a step not
    formalized".
  - The caveat bullet below the statement says so too, but the sentence intended for the paper
    does not. This is available → derived.
- *Fix:* put the scope in the sentence itself. For example: "…(machine-checked for the joint
  law of history, present visible state and hidden state; the identification of a
  realization's time-$t$ law with that joint law is not formalized)". Alternatively, move
  "machine-checked" to the inequality alone.

**3. §7 asserts an FT basis that several classes do not have.**
- *Location:* §7 opening ("Now every class in it rests on FT sources, except those marked
  PROVISIONAL"), together with the §0.4 rule.
- *Problem:* the following rest on NR comparators but are not marked PROVISIONAL:
  - C10 and C11 (REFRAMING): the decisive comparator is the conditional DPI, which is NR;
    SC Thm 5 is FT but a different statement;
  - C16e (subadditivity, "Textbook [NR]");
  - the "not located" remainders of C1 (Bennett 1973 and HMM realization theory, both NR) and
    of C5 (see finding 11);
  - (e), which is classed REFRAMING although its comparators, 't Hooft and Spekkens, are NR,
    and the entry itself says no novelty class applies.

  C4 and C8-D, by contrast, do mark their "not located" parts PROVISIONAL.
- *Fix:* either apply the rule uniformly, or state an explicit exemption in §0.4 ("standard
  textbook inequalities: DPI, Pinsker, subadditivity"). Mark C1's and C5's "not located" parts
  PROVISIONAL. For (e), either drop REFRAMING ("interpretation; not classified") or write
  "REFRAMING, PROVISIONAL".

**4. C8-R: the sufficiency half has a located construction, which the entry does not name.**
- *Location:* §3 C8-R, under "Literature" and "Skeptical reading", item 2.
- *Problem:*
  - EG Prop. 18 (p. 35) **[FT]** realizes every linear probability dynamics over a finite $T$
    by a time-indexed deterministic map $A : T \times C \times \Lambda \to C$, with an
    independent ancilla law. That is, every rooted family on $\{0,\dots,\tau\}$; Prop. 16 is
    used with Prop. 17.
  - Applied to one visible period $\{0,\dots,p-1\}$, plus a clock mod $p$ and a root record on
    zero-prior padding, this is C8-R's sufficiency construction. It is the same
    ledger-and-clock packaging that the audit counts as "elementary" for C1 and C1′.
  - The audit cites EG 16–18 only as "different, because time-indexed maps impose no
    periodicity". That is true of necessity, not of sufficiency.
  - On the audit's own C1 and C1′ standard, the sufficiency half is PARTLY KNOWN. Necessity is
    the finite order of a permutation, which the audit calls folklore.
- *Fix:* keep the owner-directed label, "NOVEL-CANDIDATE — novelty unverified". Scope the
  candidate in the entry to the two-sided *characterization* (PPer is exactly the realizable
  class). State that the sufficiency construction is EG Props. 16–18 restricted to one period
  plus the clock packaging [FT], and that necessity is folklore. Add this as point 4 of the
  §A.31 reading.

**5. The audit's base is stale on #919.**
- *Location:*
  - §0.1 (the PR #919 bullet, and "every citation of `Explainer:NNN` … where #919 has not
    landed");
  - the §1 table row "#919 (open)";
  - §3 (e), "#919 brings…";
  - §6, "#919 does not touch either";
  - CHANGES "Sources", "has not landed".
- *Problem:* `main` is `a411bf46`, which merges #919. Stating an open PR as open is a status
  claim that no longer holds.
- *Fix:*
  - Re-base to `a411bf46`.
  - Record that only Explainer changed, that its blob `a6d4cb2b` equals the read head
    `240e31e8`, and that the line count is unchanged (so all `Explainer:NNN` citations hold).
  - Restate (e) as landed.
  - Main, GR, ch07 and appendix-b are byte-identical, so no other citation moves.

### Required (fidelity and propagation)

**6. C12's site list is incomplete.**
- *Location:* the C12 heading, §1 "What #922 does not change", and F5.
- *Problem:* the (ii) ⟺ (iii) characterization, or its "both directions are theorems" claim,
  also appears at:
  - Main:212 ("the equivalence (ii) ⟺ (iii) is proved in-house") and Main:680 ("both
    directions in-house");
  - Explainer:378 ("Both directions are the foundational paper's own theorems"; it also carries
    the self-narration "The old three-way biconditional is retired", §A.30/§A.33);
  - Substratum:111 and :126 (:126 attaches the biconditional to "the universal hidden-memory
    theorem");
  - appendix-b:455 (displayed);
  - **GR:20**: "C1–C4 necessary as well as sufficient for accessible non-Markovianity", which
    includes C2;
  - **glossary:39 and FULL:6659**: "The framework's central result … if and only if some
    finite-horizon deterministic realization satisfies the four conditions C1–C4".

  The last two contradict Main:516 ("Condition (C2) is deliberately absent from (iii)") and
  Main:99 (the core is $S \iff D$ plus the universal statement). An introductory paper drafted
  from the glossary or the GR abstract would inherit them.
- *Fix:* add these sites to C12 and F5, and record GR:20 and glossary:39 as the strongest
  divergences.

**7. §A.19: Main already cites the C8 mechanism's literature, which F8 and C8 omit.**
- *Location:* §4 "F8, refreshed"; §3 C8 ("Breuer–Laine–Piilo 2009 and Rivas–Huelga–Plenio:
  [NR]. They are not needed for the class").
- *Problem:*
  - Main:121 already attributes the direction C8 uses ("P-divisibility ⟹ $d(p(t),q(t))$
    non-increasing … [4, 5]"). Here [4] is RHP, PRL 105, 050403 (2010), and [5] is RHP,
    Rep. Prog. Phys. 77 (2014).
  - Main:149 cites RHP [4, 5], Bylicka–Johansson–Acín [9] and Milz et al. 2019 [10]; Main:194
    cites [4, 5, 7, 9].
  - Main:332 attributes "the Breuer–Laine–Piilo criterion" to [3, 4], that is Breuer–Petruccione
    2002 and RHP 2010. BLP 2009 is not in the bibliography: "Laine" occurs only at :332.
  - The F8 grep also missed that Main cites 't Hooft [1] (Main:30, :688) and names Spekkens
    noncontextuality (Main:550). That mention is not Spekkens 2007.
- *Fix:*
  - In F8, add the "Main does cite" half, as v4 F8 had it.
  - In C8 "Needed", say that the citation at Main:121 should be to the classical source (BD,
    or the classical sources of finding 8) and not only to quantum [4, 5].
  - Carry two new F-note candidates, numbered after F20 and not renumbered:
    - (a) Main:332 cites BLP's criterion to [3, 4] with no BLP entry;
    - (b) Main:149's "divisibility failure is equivalent to information backflow [4, 5]"
      contradicts Main:121 ("The converse is *false*") and Main:332 (system backflow
      "sufficient … never necessary"). BD Prop. 1's equivalence holds only for
      general-ensemble guessing probability, which is a point the paper will need.

**8. The credit for C8 is narrower than the FT sources show.**
- *Location:* §7 novelty statement ("the data-processing direction of Buscemi and Datta") and
  CHANGES item 10.
- *Problem:* BD itself builds on the classical Blackwell–Sherman–Stein theorem (BD p. 4; ref.
  [3], Blackwell, *Ann. Math. Stat.* 24, 265 (1953)). PI p. 14 credits the classical "divisible
  iff information decreasing" result to Cohen, Iwasa, Rautu, Ruskai, Seneta and Zbăganu,
  LAA 179, 211 (1993), "presented in Buscemi and Datta". Total-variation contraction under a
  stochastic matrix is older still. Calling BD "the prior result" for a classical
  stochastic-matrix fact over-attributes.
- *Fix:* credit "the data-processing (contraction) property of stochastic maps (e.g. Cohen et
  al. 1993; in the divisibility form, Buscemi–Datta 2016)". Tag Cohen and Blackwell as
  [secondary], named in FT sources, and add them to §5 P1.3 or P3.

**9. (e)'s mirror check stops at the Explainer.**
- *Location:* §3 (e) ("#919 brings the Explainer into line").
- *Problem:* Main:86 and, since #919, Explainer:101/:422/:1008 scope partition-relativity to
  "the canonical measure". GR:20, item (ii), "the emergent description is uniquely determined
  by the partition", and ch07:46 state it without that scope. Under bidirectional §A.25
  propagation, Main and the Explainer now lead GR and ch07.
- *Fix:* note GR:20 and ch07:46 as an F-note candidate under (e).

### Nits

**10.** **Location:** C4 ("Main:98–99 now states it this way") and CHANGES item 1.
- *Problem:* Main:98–99 states $S \iff D$, with $Q_{\mathrm{fb}}$ only as the route for ⊇. The
  three-way statement is at Main:16–18, :526–530 and :580(1).
- *Fix:* cite those lines for the three-way form.

**11.** **Location:** C5, sufficiency of the exact clause ("not located elsewhere").
- *Problem:* a rational doubly stochastic $T = A/d$ gives a $d$-regular bipartite multigraph,
  and König's theorem (1916) decomposes it into $d$ perfect matchings, so $T$ is a rational
  mixture of permutations. That is a standard fact (NR, from memory).
- *Fix:* mark the "not located" part PROVISIONAL and add König 1916, or a combinatorics text,
  to §5 P3.

**12.** **Location:** C16-S against C15.
- *Problem:* C15 is left unclassified because "no literature was examined". C16-S has exactly
  that basis (Hayden–Preskill, PSW and decoupling are all NR) but is classed REFRAMING,
  PROVISIONAL.
- *Fix:* apply one rule to both.

**13.** **Location:** C12, "Since #922, it is no longer the paper's core".
- *Problem:* what #922 removed was the bare form (C4-old). (ii) ⟺ (iii) was not the
  displayed core at `c91bf5dd` either.
- *Fix:* say "Main:99 names $S \iff D$ and the universal statement as the core; glossary:39
  still calls the characterization theorem the 'central result' (finding 6)".

**14.** **Location:** C6, "predates the lemma's first appearance in the repository".
- *Problem:* LC §0.1 says its commit checks bound, and do not prove, a first appearance. The
  class does not depend on this, because SCH (2021) is prior regardless.
- *Fix:* keep LC's caveat.
- *Related positive check the audit could add:* Main at `6fc02988` (2026-02-25) and at
  `bbf28c64` (before 2026-08-01) contains no process-dilation or history-ledger text, and
  `process_dilation_probes.py` is first added at `64c95fee` (2026-08-10). So EG v1
  (26 Feb 2026) is prior for C1 and C1′. The audit does not date-check C1 against EG.

**15.** **Location:** §0.2, the FT definition ("read in full … and re-verified by that study's
independent reviewer").
- *Problem:* BI (§§1–2 only), GO (Lemma 6, its proof and the footnote) and LPW (§1.2) were not
  read in full. SC Def. 5 and EG Example 3 are not in `revlitcorr` §A's re-verified list.
  SC Def. 5 is present on p. 9 of `SC.pg`, which this review checked.
- *Fix:* define FT as "the cited passage, read in the full-text document".
- *Related:* C16a puts "half its initial entropy" in quotation marks, but Page's words are
  "when the black hole has emitted half of its initial Bekenstein-Hawking entropy … would be
  correct if β … were unity" (pdf p. 12). Mark it as a paraphrase.

**16.** **Location:** reading list §5.
- *Problem:* the P1–P4 ordering is sound, since only P1 can affect a NOVEL-CANDIDATE. Some
  items are missing, and P1.1, P1.2 and P2.1 cite works with venues and years that, unlike
  C15's, are not tagged "named from memory".
- *Fix:* tag those items and add:
  - Feller 1959 and Milz et al. 2019 [10] (finding 1);
  - Cohen et al. 1993 and Blackwell 1953 (finding 8);
  - RHP 2010 [4] and BJA [9], which Main already cites for the mechanism (finding 7);
  - König 1916 (finding 11);
  - optionally, a nonnegative-matrix text for C7 (Berman–Plemmons: a nonnegative matrix with
    nonnegative inverse is monomial);
  - optionally, for P1.3 and C8-D, the literature on the embedding and divisibility of
    stochastic matrices (Elfving 1937; Kingman 1962), named from memory.
- *Also:* book/README.md:64 ("the Page curve from nested trace-out") is the one book file
  whose summary omits the H-scramble condition. It is not one of the WITHDRAWN claims; note it
  under C16 if the mirror list is meant to be complete.

## Confirmed without change

- **C16d (WITHDRAWN).** No "QES prediction", "quantitatively matches" or GSL-proof wording
  survives in `papers/*.md` or `book/*.md`. The conditional forms hold at every listed mirror,
  including ch07:12, FULL:1887 and FULL:2605. C4-old does not survive outside Main:597's
  displayed counterexample.
- **F1, F2, F2b, F9 and the F11 header are resolved.** Main:500's caveat and the census note
  were read verbatim.
- **F6 is narrowed.** F3–F5, F7, F10, F12 and F14–F20 are unchanged at `a411bf46`.
- **F13 is kept separate.** The nine Main lines, Explainer:287 and :1020 are confirmed; no book
  file matches.
- **C8-R.** It carries no priority sentence, states the searches made and not made, and its
  §A.31 reading is apt (with finding 4 added). The census marks it `kernel-only` and
  `manuscript: []`, and no manuscript states it.
