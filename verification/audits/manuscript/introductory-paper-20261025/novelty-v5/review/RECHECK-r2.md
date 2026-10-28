# Re-check: novelty audit, revision 5, r2

**Objects read** (sha256 verified):
- `introaudit/novelty-v5/AUDIT.md`:
  `df39e2f93dd52456d0833c9a1a792762903945e6ffc891b9028681e7027e4b93`;
- `AUDIT-r1.md`: `ef9d475c…787a`, unchanged;
- `CHANGES.md`:
  `73e53c6f5285e09e52a5c8786c71ce95923c4f0d2b895269acf0be9bc1771e36`.

The r1→r2 diff was read in full.

**Repository.** `origin/main` = `ebf98d83` ("Merge #917"). It was read with `git show` only;
nothing was committed, pushed or posted. `a411bf46..ebf98d83` touches only
`verification/programmes/{oi-qm,black-hole-information}/` (260 files). No path under
`papers/`, `book/`, `verification/lean-mathlib/` or the census changed, and the blob ids were
confirmed for Explainer, ch01, ch18, FULL, bibliography and glossary. Every manuscript citation
in r2 therefore resolves at `ebf98d83`.

## Verdict: ACCEPT WITH NITS

All 16 findings of `REVIEW.md` are resolved. The five blocking items were checked against the
repository and the extracted texts, not against the change note. No novelty claim exceeds its
full-text basis. The new F21–F27 are correct at `ebf98d83`. Eight nits remain, none of them
required.

## 1. The 16 findings

| Rv5 | Resolution in r2 | Verified against |
|---|---|---|
| 1 XOR | "concurrent: DO3 v3 App. A"; KNOWN, PROVISIONAL; Feller 1959 and Milz 2019 = Main [10] as NR candidates; §5 P3.6 | "XOR" absent from `DO1.txt` and `DO2.txt`, present in DO3 pp. 36–37; `review4_probes.py` at `e6c21398` (2026-08-11), lines 6–8 |
| 2 machine-checked | §7 sentence now scopes the claim to the joint law and says the time-$t$ identification is not formalized | Main:99; `HiddenMemory:54–57` |
| 3 PROVISIONAL rule | §0.4 uniform rule with no textbook exemption; PROVISIONAL now on C9, C10, C11, C16e and on the not-located parts of C1 and C5; (e) not classified; §7 evidence paragraph | class lines at AUDIT:757, :780, :816, :986, :1039; C1's and C5's parts. One gap remains: N4 |
| 4 C8-R | candidate scoped to the biconditional; EG Props. 16–18 named as the sufficiency construction; point 4 added to the §A.31 reading; §7 credits EG | EG Prop. 18, PDF p. 35: "Let P be a linear probability dynamics with T = {0, 1, ..., τ} finite. Then there exists … A : T × C × Λ → C, and … λ⃗0", with the independence condition (114). The one-period, clock and padding argument holds: A(0, a, λ) = a gives Γ_M = 1 |
| 5 re-base | base `a411bf46`; ebf98d83 noted; no "(open)" or "not landed" remains | Explainer blob `a6d4cb2b` = `240e31e8`; 1064 lines on both sides; the `ebf98d83` path check above |
| 6 C12 sites | sites added; F24, F25, F26 | GR:20, glossary:39, FULL:6659, Explainer:378 and the others, re-read |
| 7 F8 / §A.19 | "What Main does cite" added; F21, F22; C8 "Needed" | Main:121, :149, :194, :332; bibliography (BLP absent) |
| 8 C8 credit | Blackwell and Cohen et al. as [secondary]; BD for the divisibility form | BD p. 4, ref. [3]; PI p. 14, ref. [26] |
| 9 (e) mirrors | F23 | GR:20(ii), ch07:46; #919's PR body (read by REST) lists them under "Not in this PR". See N6 |
| 10 | three-way form cited at Main:16–18, :526–530, :580(1) | ✓ |
| 11 | König 1916 [from memory]; C5's part PROVISIONAL; §5 P3.5 | ✓ |
| 12 | C16-S not classified; #917 records named as pending | ✓ |
| 13 | C12 core wording | ✓ |
| 14 | C6 caveat kept; C1 dated against EG | See N1. r2 also corrects an error of mine: my Rv5:14 check read `6fc02988:papers/Main.md`, a path that did not exist then. At `6fc02988`, Main.md was at the root. It has 0 hits, confirmed |
| 15 | FT redefined; partial reads disclosed; Page quote marked as paraphrase | ✓ |
| 16 | [from memory] and [secondary] tags; additions to §5; F27 | ✓, apart from N8 |

## 2. New notes F21–F27 and the extra sites, at `ebf98d83`

- **F21.**
  - Main:332 attributes the BLP criterion to [3, 4]. "Laine" occurs only at :332.
  - The book also names BLP at ch01:101 / FULL:445, ch18:78 / FULL:4896 and Explainer:148.
    `book/bibliography.md`'s only Breuer entry is T. Breuer 1995 (line 17). ✓
  - Additional sites: N5.
- **F22.** ✓
  - Explainer:148: "Breuer, Laine, and Piilo proved that P-indivisibility is equivalent to
    'information backflow'".
  - ch01:101 / FULL:445: "showed that P-indivisibility is equivalent to … *information
    backflow*".
  - Both contradict Main:121 and Main:332, as stated.
- **F23.** GR:20(ii) and ch07:46. ✓ (incomplete; see N6)
- **F24.** GR:20, "C1–C4 necessary as well as sufficient". ✓
- **F25.** glossary:39 / FULL:6659. ✓
- **F26.** Explainer:378, "The old three-way biconditional is retired". ✓
- **F27.** book/README.md:64. ✓

## 3. Novelty claims against their full-text basis

- **C8-R.** It is scoped to the biconditional. Both halves are located or folklore, and it
  carries no priority sentence. Its "Needed" item keeps P1.1–P1.3 as the precondition for any
  wording that presents it as new.
- **C4 packaging and C8-D.** Both "not located" parts are PROVISIONAL.
- **The §7 statement** carries no priority claim, and its "machine-checked" phrases are
  scoped. Two wording nits (N2, N3) make it cite an unread source and imply a provenance. Both
  are fixable in the sentence.

## 4. Nits (none required)

**N1.** **Location:** C1 dating (AUDIT:342–349) and CHANGES item 14.
- *Problem:* "Main.md … at `bbf28c64` contains neither 'process dilation' nor 'ledger'" is
  false. `bbf28c64:papers/Main.md:394` contains "this ledger counts what is *assumed*", which
  is the posit ledger. The conclusion is unaffected, since no history-ledger or
  process-dilation text is present.
- *Fix:* say "no process-dilation or history-ledger text".

**N2.** **Location:** §7 statement.
- *Problem:* the sentence cites "e.g. Cohen et al. 1993", while the bullet below it says
  Cohen et al. must not be cited until read.
- *Fix:* write the sentence with Buscemi–Datta "in the divisibility form" alone, and keep
  Cohen et al. and Blackwell in the pending list.

**N3.** **Location:** §7 statement, "the realization half adapts the time-indexed construction
of Egri et al.".
- *Problem:* "adapts" asserts a provenance. The kernel proof
  (`RootedClassificationAllTime:162`, response tables on embedded cycles, September 2026) was
  not shown to derive from EG. Separately, "the realizable rooted families" does not say
  realizable by what.
- *Fix:* write "is an instance of the time-indexed construction of Egri et al. (Props. 16–18),
  packaged as one bijection", and "the rooted families realizable by one finite permutation
  with a hidden prior shared by all roots".

**N4.** **Location:** C1′ (AUDIT:378) and the §7 evidence paragraph.
- *Problem:* under the uniform rule, C1′'s unlocated remainder (the reversibility packaging)
  rests on the same unread search areas as C1's: Fine 1982, Kallenberg, Bennett 1973 and HMM
  realization theory. C1′ is not marked PROVISIONAL, and §7's list omits it.
- *Fix:* mark it, as C1 is marked.

**N5.** **Location:** F21 and F8.
- *Problem:* BLP is also named at appendix-b:96 / FULL:5883, which is consistent with Main:332,
  and at Explainer:624. Separately, ch01 uses numeric citations ([2] at :32, [8] at :85, [9] at
  :101) against the author-year `book/bibliography.md`. Under Main's numbering, [9] is
  Bylicka–Johansson–Acín, not BLP, so ch01:101's "[9]" dangles.
- *Fix:* add these sites to F21 for the owner.

**N6.** **Location:** F23.
- *Problem:* #919's "Not in this PR" names ch01:79 and :83, and their FULL.md mirrors, beside
  GR.md:20 and ch07:46. r2 mentions this in (e), but F23's own site list omits them. ch01:79,
  "*The emergent description is uniquely determined by the partition*", is confirmed unscoped.
  #919 also flags Main:86's "(§1.3 Remark)" pointer, which should name §1.2.
- *Fix:* list all of these in F23.

**N7.** **Location:** §0.1, and the Explainer sites in C12, F13, F22 and F26.
- *Problem:* Explainer:3–8 carries a standing note: it is superseded by the book and frozen,
  and the book is authoritative where the two disagree. #919 edited it anyway, and its PR body
  defers the status note as a separate decision.
- *Fix:* record this standing, so that the owner can decide whether Explainer sites are
  correction targets. The introductory paper should not be drafted from the Explainer.

**N8.** **Location:** C3 (AUDIT:413).
- *Problem:* "Milz et al., PRX 10, 041049 (2020)" and "Strasberg–García Díaz, PRA 100, 022120
  (2019)" are not tagged [from memory] there, though §5 P2.1 tags them.
- *Fix:* tag them in C3 too.
