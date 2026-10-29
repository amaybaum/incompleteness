# Minimisation of PR #982 to its necessary manuscript changes

PR #982 merged as `dffe1945`; the main branch before it was `0d917665`. It rewrote about 860 hunks in 30
manuscript files. This round keeps only the changes the corpus needs. It restores every other hunk to its
`0d917665` text.

## What counts as necessary

A hunk is necessary only when the `0d917665` text is false, or asserts more than its support, and the
change is the minimal edit that fixes it. Three further kinds count as necessary: the minimal dependent edit
at a site that cites a refuted result, the exact attribution of a retained classical result, and a factual
error found in a #982 hunk. Everything else returns to the old text. That covers rewording, hedges on
claims that were already correct or already conditional, new propositions and discussion, reorganisation,
and overcorrections. Uncertain hunks keep the old text.

The verified corrections the classification rests on:

| id | correction | evidence |
|---|---|---|
| G1 | Substratum Lemma 24.1 (semigroup transfer) is false; the completeness of Theorem 24's generator families is open | Lean `ST3_pairC` (equal visible channel families, traces 2 and 0) |
| G2 | Theorem 24(i) holds for one hidden permutation applied in every visible fibre; a fibre-dependent relabelling preserves $T_{ij}(t)$ only | exact 4-state counterexample to the all-bijection form |
| G3 | the cubic reconstruction (Theorem 23, Lemma 23.0, SM Theorem 7b) needs the nearest-neighbour premise of Stage 2(b); the $d=3$ filter of Stage 2(a) stays derived | Stage 2(b) text |
| G4 | SM Theorem 3 holds as a restricted biconditional: no additive 2-torsion, both parity sectors, site-independent coefficients | Lean `scalar_center_chiral_iff` |
| G5 | anomaly cancellation fixes the one-family hypercharges up to normalisation and quark-singlet interchange, apart from the branch $Y_Q=Y_L=Y_e=0$, $Y_u=-Y_d$ | SM Theorem 15 |
| G6 | the Main abstract and §1.1 statements about embedded observers are correct (records inside the carrier) | Main §1.1; Breuer 1995 |
| G7 | Theorem 24(iii) (decoupled deep-sector enlargement) is sound; only claims resting on completeness change | Substratum §4 |

## Decisions

- Proposition 24.2 (block-word rigidity, Lean `WT3_spanning_iff`) stays as the proved remainder in
  Substratum §4, with the Specht–Wiegmann attribution [Specht 1940; Wiegmann 1961; Futorny–Horn–Sergeichuk 2017].
  Propositions 24.3–24.5, 9.7c, 14a and 15a and Corollary 15b are reverted, together with their architecture
  guards. Theorem 24(iv) keeps its old text.
- The amplitude-scale invariance removes only the common phase. The reduction of the block-algebra unitary
  group $U(3)\times U(2)\times U(1)$ to $SU(3)\times SU(2)\times U(1)$ also uses a specified charged matter
  action and anomaly cancellation (SM §4.9, Theorem 15). The strict commutant of the cubic-group action is
  $U(1)^3$. Substratum Stage 2(d) and Level 2, Structure (two sites), ch02, ch03, ch05 and ch06 state the
  reduction this way.
- The factual fixes in #982 hunks that are kept: the commutant naming above, the K=6 minimisation
  statements that contradict SM §4.5, the draft fragment in the appendix-b Corollary, the README's
  Grassmann wording, GR's E1–E7 and line 446, the Explainer's "only possible reconstruction",
  Computation lines 80 and 120, and the E6 citation numbers in Substratum.
- Kept old as uncertain: the equivalence-class "representative" wording, the $\alpha B+\beta L+\gamma S$ form
  of the hypercharge, the Juno "Gauge group (commutant)" table row, the Structure "classifies" sites, the
  appendix-b B.6c per-generation anomaly step, and ch19:224.
- `papers/Main.md` is identical to `0d917665` (G6).
- After independent review, the following edits were made.
  - Propagation completed:
    - the subsumed-candidate sentence in Methodology;
    - the nearest-neighbour premise at Juno and wherever SU(3) is said to select simple cubic (Explainer, Substratum, ch19);
    - "from the commutant" at the remaining Substratum and Structure sites;
    - the nonzero-$Y_Q$ branch in ch00 and ch05;
    - the Stage-2 uniqueness qualifiers in ch02;
    - the generator-(i) proof in ch02;
    - Complexity §5.2, which rests on the definition of $\mathcal{G}_{\text{sub}}$ rather than on completeness;
    - SM Theorem 3's opposite-parity hopping premise and its two directional kernel witnesses (§A.34);
    - a numbered reference for Breuer 1995 in Computation.
  - Two added clauses were corrected:
    - Substratum §3, where $\mathcal{G}_{\text{sub}}$ relates equivalent realizations by definition;
    - Structure, where the completeness converse is stated for generators (i)–(iv).
  - Reverted to the old text:
    - the GR §2 premise;
    - the ch12 theorem name;
    - an appendix-b parenthesis;
    - the Methodology "classified" wording at five sites.

## Files

`reports/` holds the per-group hunk classifications: substratum, structure, sm (with ch05 and ch06),
companions and book. Each gives the old and minimal text of every necessary edit and lists the statements
whose text differs. The decisions above were applied after those reports. The manuscripts at this commit
are the authoritative text.

Infrastructure aligned with the minimal text:
- `papers/oi_lattice_code/architecture_check.py`: back to `0d917665`; guards b173 and b174 require the open
  completeness status.
- `verification/lean-manuscript-census.json`: the chirality-recovery family is anchored at SM Theorem 3's
  citation of `scalar_center_chiral_iff`.
- `verification/coverage/LEDGER.json`: entries for the changed statements are refreshed and L-24.1 is
  removed.
- `verification/audit-census.json`, `verification/lean/edge_rigidity_probe.py` and
  `verification/lean/stinespring_scope_probe.py`: back to `0d917665`, with the scope probe requiring that the
  refuted Lemma 24.1 remark is absent.

The Lean module `OIBridge/ChiralCenterRecovery.lean`, the CI step that checks it, and the audit records #982
added all stay unchanged.

## Checks

On this commit: `sh ./build.sh` succeeds for every changed paper and for the book. The release gate passes
every step except lean-axioms, legacy-records, v3-corpus, v3-receipts and citation-roles. Those steps need
the Lean toolchain or full history and run in CI.

## Owner review at `ee007c89`: revise

The owner did not approve `ee007c89`. The review named three regressions and asked that the reviewed recovery
results be kept. The revision makes these changes.

- **Hidden-state identifiability.** The claims that the observer provably cannot determine $h$, that multiple
  hidden states are compatible with any visible history, and that $h$ is undecidable are false: for
  $\varphi(v,h)=(h,v)$, two readings determine $h_0$. They are narrowed to the degrees of freedom beyond causal
  reach (Main §1.1) and to the complete state. Substratum §2 cites the record-fibre criterion of
  Proposition 24.5. #982's five lexical guards and its record-fibre controls run are restored in
  `architecture_check.py`.
- **Gauge hierarchy.** No inclusion Level 1 ⊂ Level 2 ⊂ Level 3 (G1 ⊂ G2 ⊂ G3) and no map from
  $\mathcal{G}_{\text{sub}}$ onto the Standard Model gauge group is established. The "image" and "shadow" assertions
  are replaced by that statement, or by "follows from the substratum construction (Stage 2)".
- **Theorem 24(iv).** $\mathcal{G}_{\text{sub}}$ is defined by equal $T_{ij}(t)$. Graphs with equal growth
  dimension, mode count and isotropy share the structural outputs of Theorems 1–6, not $T_{ij}(t)$ at a fixed
  interface. (iv) is therefore a structural graph comparison outside $\mathcal{G}_{\text{sub}}$. The
  "four families" counts become three, and the completeness question concerns (i)–(iii).
- **Recovery results kept.** Propositions 24.3–24.5 (Substratum §4.1) and Propositions 14a and 15a with
  Corollary 15b (SM §4.9) are restored from #982 with their proofs and scope notes, and their ledger entries are
  restored. Corollary 15b replaces the unconditional corollary $|q_p|=|q_e|$, which fails on the exceptional branch.
  The book and README state the identity on the nonzero-$Y_Q$ branch. Proposition 9.7c is not restored: Structure's
  Proposition 9.7b already states the general minimal Stinespring uniqueness with its citation.

## Follow-up: the "Theorems 1–6" citations (#995)

SM Theorems 1–6 are the conditional Klein–Gordon branch, the Susskind factorization, chirality, the mass spectrum, the condensate stabilizer and the link-carrier count. All six are specific to the cubic lattice, so they do not support claims about general bounded-degree graphs. The citations are replaced as follows:
- Main §3.4 for the graph-independent finite-law representation;
- SM §3.2 for dimensional selection;
- SM §3.1 for the conditional continuum-curvature construction.

GR is cited only for the horizon and thermodynamic arguments.

Graphs with the same growth exponent, mode count and isotropy admit the same finite-law representation and share the growth exponent, a hypothesis of Theorem 24(iv). They need not give the same $T_{ij}(t)$, and no gravitational equivalence is claimed without the continuum conditions. The same correction reaches Structure, Methodology, Explainer and book Chapter 2, with FULL.md mirrored. No Gromov-type quasi-isometry classification of general bounded-degree graphs is asserted.

The same PR corrects the integer-dimension argument. Not every bounded-degree graph falls into an exponential, fractal or integer-polynomial growth class: intermediate (Grigorchuk) and irregular growth occur. Gromov's theorem concerns finitely generated groups and their Cayley graphs, and statistical isotropy does not make a general graph quasi-isometric to $\mathbb{Z}^d$. The integer degree is an input through A4, which is stated explicitly: the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice. The three filters select $d = 3$ when applied to the continuum description, conditional on SM §3.1's continuum step. The corollary says that $d \neq 3$ fails one of the filters E5–E7, not that it produces internal contradictions. The Explainer's minimal-structure summary now states which observer conditions are generic (C1, the C3 floor) and which are hypotheses (C2, C4), per SM §2.1.
