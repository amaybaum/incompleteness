# OI-SM-QM-BRIDGE unit 1: dispositions of the r1 review (r2)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Paper-only. No git or
GitHub write, no Lean, no manuscript change.

- **Object revised:** `BRIDGE-UNIT1.md`. r1 sha256
  `00cd6fad1e326aaa21badcf70e6c78784ec17baaf54bc669a5725668fc28453c`, kept unchanged as
  `r1/BRIDGE-UNIT1.md`; r2 revised in place. Line numbers below are r2 lines.
- **Review:** `review/REVIEW-UNIT1.md`, sha256
  `e242a794d2941826fb3f38fea019a37ce960ceb05182b5f007d58b71549a1ef7`, verdict REVISE.
- **Sources:** read with `git show fd539e15:<path>` after `git fetch origin main`. Every review
  claim below was checked against its source before it was applied; "verified" names what was
  read.
- **Checks:** `probes/r2_generic_checks.py` (sha256 `579533e3cc20d7f720e017ad08c7cafc1ae41f100edb5392ad1fd64de5e21f00`),
  output `probes/r2_generic_checks.out` (sha256 `fba1e5618dca9954ae7c16df8edc68d4f4f72d1cd2e2368a0cb370e918e4b685`, all PASS).
  Exact sympy on generic mathematical objects, under the owner's permission in #1211
  c.6739843458 ("Allow generic checks (as #1210)"); imports no earlier script; no OI mechanism.

## Blockers

| Finding | Verified | Change in r2 |
|---|---|---|
| **B1** NNB / $\{D,\varepsilon\}$ cross-level claim; "NEW" | QP:296–306 (the "Relation to SM" bullet: "an analogy across levels, which SM itself says needs a bridge"); SM:306 (separate bridge; $C=2(1-d)$ remark); QP:803–806 (NNB is a P3-armable symmetric, center-free, linear same-sublattice coupling); SM:539; SM:569 (premise $\Gamma A\Gamma=-A$); r1 Check B used a symmetric adjacency, not $D_{\rm st}$. Countercontrol re-derived by hand ($T^{\pm4}$ terms of $D'^2$ give $-2\mu$) and by exact check C3 (symbolic $\mu$, 12-site ring, with control). | §0 item 6 (l.87–95) restated at the scalar-dynamics level, NNB as P3-armable and protocol-local, transfer to $D_{\rm st}$ named as the SM:306 / QP:298–305 bridge. §10 "Connection to the SM chain" (l.640–662) rewritten: quotes QP:298–305 and SM:306, states what SM:539 and SM:569 use, "where armed" scope, what is not derived, C3 countercontrol; heading "(new in this unit; scoped)" → "(scoped)". §10 second consequence (l.668–675) restated likewise. §10 classification: NEW → ELABORATING (l.699–701). §11 NQ2 (c) uses the scalar-bipartiteness form (l.755–756). r1's Check B is no longer cited in support (§13). |
| **B2** NQ2 "first check" already answered | MECH-1 DESIGN:877–893 (non-affine at odd $q$, not CP; asymmetric adjacency for $L\ge5$, not symplectic; controlling cells vs Proposition T′(i)); MECH-2 DESIGN §0 items 1–3 (edges not reciprocal for $L\ge5$; Theorem U2 under $R1^{\otimes n}$ and H-LIFT; Lemma Q conservation fails for $G_{\rm SM}$); M-INACC-1 DESIGN §2.4 table (:268–282) and RESULT §0 ($G_\sigma$: $Q$ conserved, Lemma Q(iii) protection fails; $N_0$ = NNB-type linear class). Standing read from each head: MECH-1/MECH-2 "promote no claim"; M-INACC-1 WIP / UNVERIFIED, model-reviewed. | §10 third consequence (l.676–694): the "not established anywhere read" negative replaced by the three records, with their standing, cited as record and not as established premises (§A.46 item 7). §11 NQ2 (l.747–763) rescoped to what they leave open: preparation-class confinement, armable *symmetric* NNB under P1–P3, coexistence with the reference class's scalar bipartiteness, link to H-Bell; the "First check" bullet replaced by "Records to start from". §0 item 7 (l.96–101), B25 (l.278) and §9 NNB row (l.608) cite them. Header coverage (l.35–42) states these records were not read in r1 and lists what r2 read. |
| **B3** F4 complex structure: "not named"; SM:130 O(6); "supplied, not generated"; NQ1 | SM:505, SM:809 ("the real-to-complex step"); SM:130 quoted; SM:292 (null modes); SM:340–342 (premise list); `two-mode-drive.md` §3 (J = T_0; $T_kJ-JT_k\neq0$). Hand: $f^2=af-1\Rightarrow J^2=-1$; null modes $(f\mp I)^2=0$ at $a=\pm2$ (constant and staggered), joint commutant $\mathbb R[N]/(N^2)\otimes\mathbb R^3$ has no square root of $-1$. Exact checks C1 (real commutant dim 3; 4 vs 14), C2(a)–(b) (J; commutant dim 36 = $\mathfrak u(6)$), C2(c) (no J at $a=2$, countercontrol at $a=1$), C2(d) (stationary $K\otimes\Sigma$: 14 vs 4). | F4 (l.464–504) rewritten: heading "that the real substratum does not supply" → "that Theorem 5 does not list among its premises"; "not named or justified separately" → named at SM:505 and SM:809, not listed in SM:340–342; the SM:130 O(6) sentence replaced by the off-null-mode $\mathrm U(6)$ via positive-frequency $J$ (nonlocal) and the null-mode obstruction; `two-mode-drive.md` §3 cited; status "not derived; a candidate exists off the null modes", open items listed. §0 item 4 (l.78–81), §3.2 stabilizer row (l.207), B13 (l.266), §6 complex-phases row (l.400), §11 scoped conclusion (new "not derived" bullet, l.778–779) narrowed the same way. NQ1 (l.723–745) reframed to (a) null modes at $\alpha=1/d$, (b) $J$-Hermiticity of $\Sigma$ beyond one mode, (c) the lift; the "no ⟹ SU(3) not reachable from a real carrier" branch restated. §0 item 7 matches. Label NEW → ELABORATING (l.702–705). §12 Q2 no longer lists SM:130. |
| **B4** Main:590 qualifier dropped | Main:590 read in full ("the site-space wave-operator formulation being unresolved rather than excluded"); GR:270 (same, plus "no operational map from it to the configuration carrier being stated"). | Qualifier restored in §6 Interference row (l.405), §6 "Missing" tally (l.416–418), B23 (l.276, also cites GR:260/GR:270 and adds `coherentLiftClass_eq_substratumClass`), §11 scoped conclusion (l.772–777, 783–787). Also applied at two further sites carrying the same unqualified claim: §0 item 4 (l.73–76) and S7 (l.304). |
| **B5** authorization misquoted | c.6738806776 read via `gh api`: "no computation;" with no exception. c.6739843458 read: "Allow generic checks (as #1210)", and "The checks already run were run before this permission, and are recorded as such." | Header Authorization bullet (l.9–18) quotes c.6738806776 exactly, quotes c.6739843458, states the r1 script ran before the permission and outside the authorization then in force, and that r2 checks ran under it. §13 (l.814–833) records the r1 script that way, states no r2 statement rests on it, and describes the r2 checks. The one statement supported only by a check, the stationary-covariance stabilizer count, is marked computation-supported (F4, l.495–497; §13). |

## Nits

| Finding | Verified | Change in r2 |
|---|---|---|
| **N1** F9 tracked in #1188; owner question decided | #1188 body read (owner decision 2026-11-07 "Do not use it as scientific evidence"; citation list); MonoidalCompletion.lean:359–360 is `def conjChannel`; M-INACC-1 DESIGN:585. | F9 heading "appears vacuous" → "is vacuous; already tracked as #1188" (l.545–568); #1188, its owner decision, M-INACC-1:585 and #1188's citation-site list added; `:360` stated to be the definition. §12 r1 Q2 removed; a closing line cites #1188's decision (l.805). Extra sites found by `git grep` that #1188 does not list are inventories, not support citations (`intro-corpus-audit-20261026/unit5-evidence/REVIEW.md`:687, `u5_reports.tsv`, a results JSON, two `verification/lean/*.py` probe scripts); not added to r2. |
| **N2** F11 diagnosis | SM:112 read; neighbours $\{i-1,i+1\}\cup\{i+2: x_{i+1}=0\}\cup\{i-2: x_{i-1}=0\}$ by hand, degree 2, 3, 4; M-INACC-1 DESIGN:274–278. | F11 (l.576–580): "(interval reversed)" replaced by the degree set and the M-INACC-1 citation; SM:106 clause kept. |
| **N3** book spin–statistics claims | ch06:28 = FULL:1541 ("follows from the lattice representation theory … not from a separate spin-statistics postulate"); ch10:36 (spin–statistics theorem from the emergent QFT's Lorentz invariance); SM:130 (iii) radiative stability open. | F8 (l.534–544) adds both book statements as findings, with why they exceed support. §12 Q2 lists them. |
| **N4** F7 mirrors | ch05:91 = FULL:1409 ("under an exact change of variables on the lattice"). | F7 (l.531–533) names both. §12 Q2 lists them. |
| **N5** F4/F5 site lists | Sub:163, Structure:152, Structure:1153, FULL:736, FULL:939, FULL:1226 read; Sub:393–395 (Level 2, emergent QFT); SM:511 ("At the bijection level … the commutant … acts"). FULL:1226 is stated "Conditionally on H-link", whose $\otimes\mathbb C^m$ carries the complex structure, so it is the weakest of the six sites; kept in the list because it too does not state the dependence. | F4 site list (l.477–480); F5 (l.513–517) adds SM:511 and Sub:393–395 as the competing anchor. §12 Q2 lists them. |
| **N6** §4 counts | Recounted row by row after N7's relabels. Reviewer's St 9, Op 7, "none identified" 14 confirmed for r1's labels. | Counts paragraph (l.282–287) replaced: D in part 3, Op 6, E 7, QS 1, St 10, C 1, none identified 14, with row lists. (St 10 and Op 6 differ from the reviewer's 9 and 7 only through N7: B20 gains St, B7 A4 moves from E/Op to E.) |
| **N7** slash labels | SM:1424 (Bravais selected because the gauge group is observed); Main:403–407 and Main:22 (Bell: one of two hypotheses dropped; framework drops parameter independence); Sub:98 (A4's "observational anchor is the homogeneity of physical law"; observer-architecture warrant open). | B6 E/QS → E (l.259); B7 A4 E/Op → E with Sub:98's wording (l.260); B20 QS/E → E + St (l.273); F2 (l.448–456); §9 rows (l.590, 591, 603). §1 QS definition (l.140–142) clarified: QS is a theory-defined target, an observed quantity is E. QS kept for premise I. |
| **N8** E6 also classical | SM:176 (Ehrenfest; quantum statement "the corresponding"; classical orbit instability). | §3.2 row (l.205) and F6 (l.518–521) narrowed to "the atomic-stability filter as stated includes a quantum statement". |
| **N9** GR:260 phase negative | GR:260 read; `onesFixing_not_phasesAvailable` (:55), `substratumClass_not_onesFixing` (:200) in PhaseSource.lean; scope "exhibited at level one, with no claim … at each composite level". | §6 complex-phases row (l.400) adds it with that scope; §5.1 (b) uses it. |
| **N10** `driveQ_isContinuousPath` | Main:274 and Main:590 (path of $*$-automorphisms, no one-parameter-group law, no generator; Hamiltonian law additional structure). | §3.1 operational-completion row (l.185), B26 (l.279), §6 Interference row (l.405): derived, not an available operation. |
| **N11** measurement-dependent alternative | Main:22 ($I_{\rm ont}\ge0.0309$ bits); Main:403–406. | §3.1 Bell row (l.186), B20 (l.273), F2 (l.448–456), §9 H-Bell row (l.603). |
| **N12** F3 mitigation; CONFIRMING | Main:66 ("Unitary evolution in quantum mechanics *is* information conservation"); Main:62; Sub:94. | F3 (l.457–463): "removes the circularity" → relocates the quantum anchor; Main:62/Sub:94 state it openly. Labelled CONFIRMING (l.715–717). |
| **N13** Sub's own scoped statements | Sub:14, Sub:193 (Theorem 23), Sub:373. | §3.3 (l.237–240): Sub:68 is a sentence-level overstatement inconsistent with them. |
| **N14** F10 wording-level | Sub:44 ("The unresolved step is … its simultaneous extension to the full coherent local instrument/composite algebra"). | F10 (l.569–575) narrowed to the word "interference" and the Sub:463 statement. |
| **N15** A5-LINEAR-AFFINE R5 | `A5-LINEAR-AFFINE.md`:543 (R5: "none selects b = 0 with an independent justification"); standing WIP / UNVERIFIED. | B8 (l.261) and §9 linearity row (l.594) cite it, with its standing. |

## Review §8 item 3: §A.31 novelty labels

Redone after B1–B3 against `main` at `fd539e15` (`git grep` over `papers/`, `book/`,
`verification/` excluding JSON/TSV/Python, for each finding's terms). r2 §10 classification
(l.696–717). No finding is NEW.

| Item | r1 | r2 | Basis on `main` |
|---|---|---|---|
| Q6 NNB vs SM chirality | NEW | ELABORATING | QP:298–305; SM:306 |
| F4 complex carrier | NEW | ELABORATING | Substratum §4 "no complex structure" (quoted at `audits/foundations/phase-source-audit.md`:74); SM:505; SM:809 |
| FI-1 (new in r2) | — | CONFIRMING | Main:590; GR:270 |
| F1 | ELABORATING | ELABORATING | #1211 c.6738806776 anchor correction; no record found flagging Sub:68 |
| F5 | — | ELABORATING | Sub:393–395, SM:312, SM:316; inconsistency not found recorded |
| F8 | — | ELABORATING | `audits/manuscript/dimension-dependency-reconciliation-20261029/README.md`:8 |
| F2, F3, F6, F7, F9, F10, F11 | F9 CONFIRMING; others unlabelled | CONFIRMING | Main:403–406; Main:62, Sub:94; SM:150 (i), SM:176; SM:290–292; #1188, QP:865; Sub:44; M-INACC-1:274–278 |

## Other review items

- Review §4 "QP:955's marker spans QP:954–956": verified (QP:952–957); §10 citation changed to
  QP:954–956 (l.675).
- Review §4 "MonoidalCompletion:360 is a definition": applied under N1.
- Review §4 "Main:99's quote appears with a non-ASCII hyphen": no change; the text matches.

## Refusals

None. Each blocker and nit was verified against its source and found correct. Two
applications differ from the review's wording, with reasons:
- **N6 counts.** The review's St 9 and Op 7 are correct for r1's labels; r2's St 10 and Op 6
  follow from applying N7 (B20 gains St; B7 A4 loses Op).
- **B2 standing.** The review says the first check is "already answered". r2 cites the three
  records as the record on `main`, with their stated standing (paper-only, "promote no claim";
  M-INACC-1 WIP / UNVERIFIED), not as established results (§A.46 item 7).

## Changes not traced to a review finding

1. **FI-1, the earliest unsupported forward implication** (§0 item 8, l.102–113; new §5.1,
   l.336–389; §11 scoped conclusion l.783). From the coordinator's instruction, quoting the
   owner's stated purpose for the next step. FI-1's statement is limited to one direction:
   it is a necessary condition of layer-flow executability, by GR:270 and
   `exists_nonMonomial_of_layerFlowExecutable`, and no equivalence is claimed (§A.34).
2. **§12 reviewer question removed** (r1 Q5). It is answered by c.6738806776 ("Its reviewer is
   a fresh, independent reviewer"). §12 is renumbered 1–3 (l.792–803), and a closing line cites both
   decisions (l.805–806).
3. **Header standing line** (l.3–4) names the revision r2 and the review it answers.
4. **§9 search-scope sentence** (l.611–612) and the §13 limits bullet (l.834–839) now refer
   to the header's coverage list, which includes the r2 additions.
5. **Exact check C2(d)** was added so that F4's stationary-covariance stabilizer count rests
   on this unit's own check rather than only on the reviewer's probe R1. It is marked
   computation-supported.
6. **§5.1 (e)** names S12 (the observer-level CI descent, SM:276) beside S13 as the open
   implications on the spatial route.

7. **Repair of an editing artefact** introduced during r2 drafting (a control character in
   §5.1's `\varphi`), fixed before hashing.

No other text was changed. The diff r1 → r2 (`git diff --no-index -U0`) has 48 hunks, and each
falls under one of the rows above.
