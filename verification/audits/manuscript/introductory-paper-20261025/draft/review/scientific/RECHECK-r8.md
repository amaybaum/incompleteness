# Scientific confirmation: Introduction r8

- **Object.** `draft/Introduction-r8.md`, sha256 `27d40e7b…8781` (verified), at `e217ac6c` on #918.
- **Diff.** The diff against r7 (`git -c gc.auto=0 -c maintenance.auto=false diff --no-index`) touches the abstract
  marker, §5, §6.2 item 4, §6.3, the conclusion marker and [BBS24].
- **Main.** Main at `17b830bc` (the #936 merge) was read through `S/bhfix/wt`. Its GR, ch07, ch18, ch19 and FULL
  were extracted to `sci-review/m17/`.
- **Read-only.** No repository file was changed.

## Verdict: ACCEPT WITH NITS

§5 now leads with the distinction between preservation and accessible recovery. The Page curve sits in one
subordinate, conditional paragraph, which lists every open condition at main's wording. All the R11 sites are
corrected on main and in their FULL mirrors. Nothing else changes claim strength. The three nits below are small,
and N1 is a precision fix.

## 1. §5: order and emphasis

**Order.** §5 now runs:
- the problem and the split between conservation and access;
- conservation as a premise, and claim A (conservation neither implies nor is necessary for accessible recovery);
- the counts and the endpoint guarantees;
- one closing paragraph that opens "The Page-curve calculation … addresses recovery under its own conditions and
  is a conditional result".

This meets the owner's direction: preservation versus accessible recovery is the central argument, and the Page
curve is a qualified, subordinate result.

**Each condition, against main `17b830bc`:**

| Condition | r8 | Main | Verdict |
|---|---|---|---|
| H-scramble, and its failure | "the orbit ensemble equidistributes over quantum pure states on the shell; H-scramble fails for every bijection acting on a definite initial configuration with the bipartition aligned to the configuration coordinates and is not established" | ch07:126 (the same failure clause); GR A.7 definition | Exact |
| H-decouple | "$B\cup R$ evolves with no coupling to $D$ or to … $V\setminus R$, and its joint state is pure, over whole cycles of the dynamics; timescale ordering does not supply it, and it is not established" | GR:811 at main, near-verbatim, including "over whole cycles" and "Timescale ordering does not supply it" | Exact |
| A.8 scope | "takes the whole configuration space $\mathcal C_B\times\mathcal C_R$ as a single energy shell. That requires the energy to be constant there, so that energy conservation places no constraint on the orbit, and it does not follow from the conservation of a Hamiltonian that takes more than one value there. An evaporating black hole … is in the proper-shell case …; that case is open" | GR Thm A.8 at main (shell = whole configuration space) and the paragraph after it ("a Hamiltonian that takes more than one value there…"; "An evaporating black hole whose radiation carries away its energy is in that proper-shell case") | Exact; no stronger than main |
| Time average only | "full-cycle time average …, at the bipartition of each stage held fixed"; "whether the entropy along a single trajectory follows the same curve is open" | GR Thm A.9 at main, with the remark after it | Exact |
| The covariant field equations | "In the dependency ladder of [GR] the Page curve is also conditional on the covariant field equations" | GR:12 (G4 conditional on G3) | Exact |
| GSL, QES and islands | kept | GR A.6 and GR:877 at main | Exact |

The paragraph ends: "The Page curve of [GR App. A] is therefore not established, and the black-hole information
problem is not resolved here." §6.3's update ("whether H-scramble and H-decouple hold, the Page value on a proper
energy shell and along a single trajectory") is correct. The abstract and the conclusion are unchanged and remain
consistent.

**One precision nit (N1).** "the full-cycle time average … equals the Page value" drops A.8's
"$+\mathcal O(\epsilon)$", which A.9 carries as "up to its $\mathcal O(\epsilon)$".

## 2. The drafter's departures

- **"Qualified supporting result" replaced by main's phrasing ("addresses recovery under its own conditions … is a
  conditional result" [Book §7.6, §18.5]).** Accepted.
  - The wording is main's own (ch07:110, ch18:130/:146).
  - The status is the same ("conditional"), and the result is subordinate in placement.
  - It avoids §A.32 self-assessment.
- **The $t_{\rm evap}/\tau_B^D\ge10^{57}$ clause dropped, "timescale ordering does not supply it" kept.** Accepted.
  - Main GR:811 now carries the timescale fact itself ($\sim10^{62}$ at $\Gamma\sim1$).
  - The leftover is §6.2 item 4's three non-claims ("information reaches $D$", "Thm A.7 fails within its stated
    scope", "no other decoupling argument"). They now refer to a finding §5 no longer states. They do no harm, but
    see N2.
- **The [BBS24] VERIFY can be cleared.** FINDINGS (`draft/review/references/FINDINGS.md`, sha256 `fa50caae…6ea1`)
  quotes BBS24 Def. 1 first-hand, arXiv:2310.01205v2, pp. 1–2, verdict SUPPORTED.
  - The draft's definition ("an instrument realizing the first map, followed by channels conditioned on its
    outcome") gives the same class as Def. 1's Kraus-decomposition form. Each instrument element splits into its
    Kraus operators, and each Kraus decomposition is an instrument.
  - The Pauli decomposition of Appendix B, with $M_o=\tfrac12\sigma_o$ and $\Phi_o=\mathrm{Ad}_{\sigma_o}$, is
    literally Def. 1's form.
  - Replacement comment:
    > `<!-- Read first-hand: arXiv:2310.01205v2, Def. 1, pp. 1–2 (draft/review/references/FINDINGS.md, sha256 fa50caae…6ea1): SUPPORTED. -->`
  - By the same record, the VERIFY markers on **[Cal26], [EvEMU11], [KP14], [tH14] and [Vol06]** can also be
    replaced by "read first-hand … SUPPORTED" comments citing FINDINGS.
  - **[CT06], [Har04] and [Sha79] stay**: they are UNREACHABLE. The Weinberg gate also stays open.

## 3. The R11 markers: all sites corrected on main `17b830bc`

| Site | Main now | Corrected? |
|---|---|---|
| ch07:110 / FULL:1987 | "resolves the paradox at the level of information preservation …; how much … an observer can recover … is a separate question, which bijectivity alone does not settle and which the Page-curve derivation below addresses under its own conditions" | Yes (claim A's split) |
| ch07:126 s1–2 / FULL:2003 | "does not use the gravitational path integral: the cycle structure … supplies exact time averages, and the Page value enters through a typicality condition"; Page mean plus PSW stated correctly; full-product-shell scope | Yes |
| ch07:159–161 / FULL:2036–2038 | "a measurement of the radiation alone therefore does not test the conservation claim, which rests on bijectivity as a premise" | Yes (the empty falsifier is removed) |
| ch18:130 / FULL:4950 | "framework-level interpretations and conditional results … the information account preserves information with the Page curve conditional" | Yes |
| ch18:146 / FULL:4966 | "whether the radiation carries it is a separate question …; the Page curve at the emergent level is a conditional result" | Yes |
| ch18:158 / FULL:4978 | "(the substratum preserves it, by bijectivity; whether the radiation carries it is the separate question …)" | Yes |
| ch19:334 / FULL:5510 | "Preserved; Page curve conditional" | Yes |
| GR:811 | H-decouple named and defined; "Timescale ordering does not supply it" | Yes |
| GR:869 (now GR:877) | "applies measure concentration [29, 61] … under H-scramble …, which ergodicity over configurations does not supply"; no "invokes only PSW" and no "no ergodicity" | Yes |
| R12, ch18:148 / FULL:4968 | "For a mass-independent emission coefficient …" | Yes |

**Search for the old phrases.** None of "because φ is bijective" in a resolution sense, "runs through the
*combinatorial*", "Falsification of the framework", "(which it does, through the nested partition)", "Resolved (Page
curve", "reproducing the Page curve at the emergent level", "frozen on evaporation", "invokes only Popescu", "no
ergodicity" or "mass-independent fraction" remains in GR, ch07, ch18, ch19 or FULL at main.

**FULL mirrors.** Each corrected phrase occurs equally often in the chapter and in FULL.

Removing all six markers is therefore justified.

## 4. Claim strength elsewhere

- §6.2 item 4 loses only its marker; §6.3 is updated to main's conditions; the conclusion loses only its marker.
- [BBS24] gains its arXiv identifier, which matches the PRL DOI per FINDINGS.
- No other line changed.

## 5. Nits

- **N1 (precision), §5.** Replace "equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$" with:
  > equals the Page value $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$, up to $\mathcal O(\epsilon)$
- **N2 (optional), §5.** So that §6.2 item 4's three decoupling non-claims keep their referent, cite the bound at
  "timescale ordering does not supply it":
  > timescale ordering does not supply it [GR App. A.7; BHa, item F], and it is not established

  Alternatively, drop item 4's last sentence.
- **N3.** Replace the [BBS24] VERIFY with the comment given in §2. Optionally do the same for the five other
  SUPPORTED entries.
