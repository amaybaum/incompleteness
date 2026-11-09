# Review of ASSESS-1059 r6 (BORN-SEL, #1059): fresh, independent, paper-only delta review

**Model-written (Claude Code subagent, 2026-11-09). WIP / UNVERIFIED.** This review adopts nothing,
edits no record and authorizes nothing. It made no git or GitHub write and no GitHub read.

- **Under review.** `ASSESS-1059.md` r6, sha256
  `ccedea2f66bb567689cba161f9a9ae0818008e4822b4143d4ad63377be63d50c`, verified before reading.
  Also read:
  - `DISPOSITIONS-r6.md` (`528cd5c3…48fd`), in full;
  - `r5/ASSESS-1059.md` (`63d54430…ef46`, verified) and the full `diff` r5 → r6;
  - `review/REVIEW-1059-r5.md` (`4e343e55…42b7`, verified);
  - `DISPOSITIONS-r5.md` (`086b9f49…2668`, verified; unchanged);
  - `probes/r6_column_support.py` (`386b2ef5…3822`, verified) and its `.out` (`c362171f…18d3`,
    verified); `probes/r4_dilation_gram.py` H1 (the DS matrix).
- **Sources.** `fd539e15`, read with `git show`: Main:218 ("takes the complex matrix kinematics as
  given, … and deriving that kinematics is open"), unchanged in use. Lamperti was not read (as
  the unit states); the finite-dimensional statement it is cited for is proved independently
  below.
- **Reviewer probe.** `review/rv6_1059_checks.py` (sha256
  `c81045126f8d3e335a45dfa4549d12c877f9a2dbc6a6ed069efd1d7f6a847d96`), output
  `review/rv6_1059_checks.out`
  (`bcda76a486cb3fca70ce8eec03be5edb75b644ffbfc34afa123c40d1f347285f`). Exit 0 under
  `python3 -I`; imports nothing earlier; exact `Fraction`, integer-root enclosures and sympy on
  generic numbers and matrices only (V1–V7, docstring). Mutation-tested: six single-line mutants
  `m1`–`m6` each turn the affected check to FAIL (V3, V4, V6, V1, V2, V7 respectively).

## Verdict: ACCEPT WITH NITS

B1 of REVIEW-1059-r5 is fixed correctly at all three sites, with the reviewer's second option
(state the split) and a paper proof that I verified independently, including for complex
entries. Nits 1–4 are applied correctly. U1–U4 are accurate. Every diff hunk is traced. All
twelve scripts re-run byte-identically. No conclusion and no column-(ii) verdict changed. The
two nits below are non-blocking.

**The unit is ready to be used as an input to the dependency matrix** (#1169 c.6741291498), on
the scope it states: a paper-only, WIP assessment whose conclusions are conditional on the named
posited hypotheses (H-LIN, H-RF$_p$) and whose drafts are cited as hypotheses only (§A.46.7).
This readiness is a review finding; it adopts nothing and authorizes nothing (§A.45 rule 3).

## Blockers

None.

## Nits

1. **Put the pointwise inequality's proof in §3, not only in DISPOSITIONS-r6.** §3 (l.295–297)
   labels the statement "$|a+b|^p+|a-b|^p-2(|a|^p+|b|^p)$ is $\le0$ for $0<p<2$ and $\ge0$ for
   $p>2$, with equality only when $ab=0$" as A, but the argument is given only in the change
   record. One clause would make the unit self-contained: "by the parallelogram identity
   $|a+b|^2+|a-b|^2=2(|a|^2+|b|^2)$, Jensen for $x^{p/2}$ and strict super- (sub-)additivity of
   $x^{p/2}$ for $p>2$ ($p<2$) when $ab\ne0$". Q1–Q2 are instances, and Lamperti is not read, so
   without the clause the A label points outside the unit.
2. **(Optional) Homogeneity.** H-RF$_p$ is stated on $\ell^p$-unit vectors (§1, §3), while §3 and
   r6 Q2/Q4 apply it to $e_i\pm e_j$ and $e_1+e_2$ with target sum 2. This is equivalent by
   degree-$p$ homogeneity; "on $e_i$, $e_j$ and $(e_i\pm e_j)/2^{1/p}$" or "(by homogeneity)"
   would make it explicit.

## Checks performed

**1. B1, the disjoint/overlapping split.**
- *Statement at the three sites: correct.*
  - §0 item 2 (l.94–100): the split is by the supports of the dilation columns; overlapping →
    $p=2$ forced and completeness follows, "as in the square case"; disjoint → only
    $p$-normalised columns required, so H-RF$_p$ holds at each $p>0$ for some non-monomial
    family, and the 2 comes only from completeness.
  - §3 (l.291–317): the same, with the proof, the polarization step $V^\dagger V=1$, the
    instance $\{cH,cH\}$, "need not force $p=2$", and "For an operation with disjointly supported
    dilation columns, such as these and $\{2^{-k/2}P_\sigma\}$ (R3-N)". The added remark that a
    square map with nonzero, disjointly supported columns is monomial is correct (rv6 V7; nonzero
    columns follow from H-RF$_p$ on $e_i$).
  - DISPOSITIONS-r6, supersession row: supersedes DISPOSITIONS-r5 statement (1), second clause,
    with the same split; first clause and statement (2) stand. DISPOSITIONS-r5 is left unedited,
    on the ground accepted in REVIEW-1059-r4 and -r5 (§A.27). Correct.
  - The row's example is $\{H/2,H/2\}$. That is right: $\sum_r K_r^\dagger K_r=2c^2H^\dagger H
    =4c^2\cdot1$, so $c=1/2$. REVIEW-1059-r5's fix text had $\{H/\sqrt2,H/\sqrt2\}$, which gives
    $2\cdot1$ (rv6 V6); the writer did not propagate that slip. "H/\sqrt2" has 0 hits in r6.
- *Overlapping columns force $p=2$, and completeness follows: verified.* For $p\ne2$, the
  pointwise lemma plus the row sum (below) makes every pair of columns disjointly supported, so
  an overlapping pair leaves only $p=2$. At $p=2$, H-RF$_2$ on every complex vector gives
  $V^\dagger V=1$ by polarization, which is completeness. rv6 V5 confirms that the complex probes
  are needed for that step: $v_1=e_1$, $v_2=ie_1$ passes the four real probes at $p=2$ and has
  $v_1^\dagger v_2=i$. The text requires H-RF$_p$ "on every amplitude vector", complex ones
  included, so the step is covered.
- *Disjoint columns: the 2 comes only from completeness: verified.* With disjoint supports,
  $\sum_i|(Vx)_i|^p=\sum_j|x_j|^p\lVert v_j\rVert_p^p$ (r6 Q3), so H-RF$_p$ on every vector holds
  iff each column is $p$-normalised. A column with two or more nonzero entries is normalised at
  one exponent only (column lemma), and completeness requires 2-normalised columns; so the 2 is
  completeness's. Column (ii) is unchanged: in both cases the 2 comes from a posit (the linear
  kinematics with H-RF$_p$, or completeness).
- *The writer's paper proof: correct, and it extends to complex $a,b$.* Independently:
  - With $s=|a|^2$, $t=|b|^2$, $w={\rm Re}(a\bar b)$: $u=|a+b|^2=s+t+2w$, $v=|a-b|^2=s+t-2w$,
    $u+v=2(s+t)$, and $st-w^2=({\rm Im}\,a\bar b)^2\ge0$ (rv6 V1, symbolic complex).
  - $p>2$: Jensen for convex $x^{p/2}$ gives $u^{p/2}+v^{p/2}\ge2(s+t)^{p/2}$; strict
    superadditivity of $x^{p/2}$ gives $(s+t)^{p/2}\ge s^{p/2}+t^{p/2}$ with equality iff $st=0$.
    $0<p<2$: both reverse (concavity; strict subadditivity when $st>0$). If $ab=0$, then $u=v=s+t$
    with $st=0$, and the expression is 0. So it has a fixed sign and vanishes iff $ab=0$, for
    complex as well as real entries.
  - Row sum: H-RF$_p$ on $e_i$, $e_j$, $(e_i\pm e_j)/2^{1/p}$ gives
    $\sum_k[\,|a_k+b_k|^p+|a_k-b_k|^p-2|a_k|^p-2|b_k|^p\,]=2+2-2-2=0$; each term has the same
    sign, so each is 0 and $a_kb_k=0$ for every row $k$. Conversely disjoint $p$-normalised
    columns satisfy H-RF$_p$ on every vector.
  - Exact checks: V2, for $p=4,6,8$ symbolically in $s,t,w$: every monomial has a positive
    coefficient and contains $st$ or $w^2$, so the expression is $\ge0$ and vanishes only at
    $st=0$ (e.g. $D_4=4st+8w^2$); control $D_2\equiv0$. V3, rigorous rational enclosures at
    $p\in\{1/2,1,3/2,5/2,3,7/2\}$ over 100 ordered Gaussian-rational pairs: strict sign whenever
    $ab\ne0$, exact zero whenever $ab=0$. V4, exhaustive complex $4\times2$ maps at $p=4$ over
    $\{0,\pm1,\pm i,(\pm1\pm i)/2\}$: 272 unit columns, 73 792 overlapping unit pairs, 192 passers,
    none overlapping, no disjoint pair failing; countercontrol at $p=2$: 3 680 overlapping
    passers.
- *Lamperti is labelled "not read first-hand"*: at §3 (l.299–300, "L, not read first-hand") and
  in §8 *Not done* (l.868, "Lamperti as REVIEW-1059-r5 reports it"). It is cited as literature
  beside the paper argument, not as the sole support. Its characterisation as "the
  finite-dimensional case of Lamperti's theorem on $L^p$ isometries" is accurate.

**2. Nits 1–4 of REVIEW-1059-r5.**
- **N1: applied.** "A non-monomial doubly stochastic map (r4 H1's DS)". r4 H1's DS is
  $\bigl(\begin{smallmatrix}1/3&2/3\\2/3&1/3\end{smallmatrix}\bigr)$, doubly stochastic; any
  column-stochastic nonnegative map keeps nonnegative entry-sum-1 vectors so, which gives
  H-RF$_1$ on every reachable state. "nonnegative map satisfies" has 0 hits.
- **N2: applied** (drop option). "An instance with cancellation forces $p=2$ (r4 H2; rv3 F4)".
  The remaining "r5 check S3" (1 hit) cites S3 for $N_q$ and $S$, which S3 does compute. §8's
  "(cancellation)" for r5's rotation describes the frozen probe correctly ($R^2e_1=(0,1)$ is in
  its reachable set) and is no longer cited as isolating cancellation. Acceptable.
- **N3: applied.** "*Alternative within (b), not selected (owner decision 5, #1169
  c.6742190154; §7 OQ-2):*". Content unchanged. "prefers to stay" has 0 hits.
- **N4: applied.** OQ-3: "In that status field, 'no H-Bell implication' is open (none derived in
  the sources read, §0 item 2), not disproved." "That status field" refers to the quoted
  c.6741291498 vocabulary immediately before; the sentence is the writer's, not attributed to the
  owner. Correct (§A.45 rule 1).

**3. Untraced changes U1–U4: accurate.**
- U1: header "Revision r6", REVIEW-1059-r5 with its hash and verdict, `r5/` kept text,
  DISPOSITIONS-r6, "Seven scripts" (P1, P2, r2–r6: seven). Correct.
- U2: §8 *Read* adds REVIEW-1059-r5 with `rv5_1059_checks.py` (`10aa30d5…ae44`, verified) and
  c.6742190154. Correct.
- U3: the r6 probe entry matches the script (Q1–Q5, alphabets, counts 1616/816/1008/192/4384,
  the six mutants); the re-run line is true (below).
- U4: Lamperti added to *Not done*. Correct.
- *Diff accounting.* Every hunk of `diff r5 r6` maps to a disposition: header and "Seven
  scripts" (U1); §0 item 2 and the §3 paragraph (B1); §3 DS sentence (N1); §3 cancellation
  sentence (N2); §5 alternative (N3); OQ-3 (N4); §8 *Read* (U2); §8 probe entry and re-run line
  (U3); §8 *Not done* (U4). No hunk is untraced.

**4. Probes and conclusions.**
- *Re-runs.* All twelve scripts (P1, P2, r2–r6, rv, rv2–rv5) re-run under `python3 -I` from a
  scratch directory: each exits 0 and is byte-identical to its recorded `.out`.
- *r6 mutants.* `n1`–`n6` each exit 1 with the named check FAIL (Q2, Q2, Q4, Q5, Q1, Q2).
- *Verdicts unchanged.* No table row (R2, R3-N, R3-C, R4, §4 rows) changed. §0 item 1 is
  unchanged: nothing on `main`, and no draft read, derives exponent 2 or the Born law from
  independently justified OI principles.
- *Dependent passages, checked and consistent with the split.* FI-1 and R3 (a posited complete
  family; the column lemma on a 2-normalised dilation column); R3-C's last column ("any operation
  with a visited 2-normalised column, or dilation column … forces $p=2$"); R3-N's last column
  ($\{2^{-k/2}P_\sigma\}$, disjoint dilation columns, r6 Q5); §0 item 2's FI-1 paragraph ("in
  either case the 2 is the posited quadratic normalisation", which reads completeness as posited
  by FI-1's complete family); NQ-1059's square clause (§5, l.573); §8's r5 S1 entry (two disjoint
  families).

**5. Scope, columns and register.**
- *Columns.* Column (iii) results are not cited for column (ii); the new text keeps the 2 as a
  posit in both cases ("the posited linear kinematics together with posited H-RF$_p$";
  "completeness …, the posited quadratic normalisation").
- *Scope.* The split is stated for H-RF$_p$ on every amplitude vector, and r6's checks are
  described as instances "not a proof"; nothing is promoted beyond the paper argument.
- *Register.* Added lines contain no caps emphasis, reader instruction, self-assessment or
  revision narration in the assessment's own claims; "not selected" and "(resolved)" are status
  idiom of a working assessment (§A.32–§A.33 bind `papers/`).
- *Header.* States no adoption or authorization.
