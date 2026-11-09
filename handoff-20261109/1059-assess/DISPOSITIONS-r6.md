# ASSESS-1059 r6: dispositions of REVIEW-1059-r5

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** This file maps each finding
of `review/REVIEW-1059-r5.md` (sha256
`4e343e555f3b73f7b066cf742c8b80a380b0e2f64eb5f82ebc19804fd0eb42b7`, REVISE, bounded) to its change
in `ASSESS-1059.md` r6 (sha256
`ccedea2f66bb567689cba161f9a9ae0818008e4822b4143d4ad63377be63d50c`). r5 is at `r5/ASSESS-1059.md`
(`63d544308cafc8859c7c89a630a5bace1303e2c0c5870b0993a44b5ace52ef46`), copied unchanged and
verified after copying. `DISPOSITIONS-r5.md` (`086b9f494e47811e7c626052194337327d95ba3291f631e988e2638185412668`)
is not edited.

Each finding was checked before it was applied: by a paper argument, by a new exact check
(`probes/r6_column_support.py`, below), against the cited script, or by reading the cited comment.
No repo, git or GitHub write was made; #1169 c.6742190154 was read with `gh api` (read only). No
computation was run on an OI mechanism.

No finding was refused. Nit 4 (optional) was applied.

## Blocker

| Finding | Verified against | Disposition | Change in r6 |
|---|---|---|---|
| B1: the non-square clause holds only when the dilation columns have disjoint supports | Paper argument (A): for complex $a,b$ and $p>0$, with $u=\lvert a+b\rvert^2$, $v=\lvert a-b\rvert^2$, $u+v=2(\lvert a\rvert^2+\lvert b\rvert^2)$; for $p>2$, convexity of $x^{p/2}$ and superadditivity give $u^{p/2}+v^{p/2}\ge2(\lvert a\rvert^2+\lvert b\rvert^2)^{p/2}\ge2(\lvert a\rvert^p+\lvert b\rvert^p)$, the last with equality only if $ab=0$; for $0<p<2$ both inequalities reverse. If H-RF$_p$ holds on $e_i$, $e_j$, $e_i\pm e_j$, the row-sum of these terms over columns $i,j$ is $2+2-2(1+1)=0$, so each term is 0 and the columns are disjointly supported. Conversely disjoint $p$-normalised columns give H-RF$_p$ on every vector. New r6 checks Q1–Q5 (exact): Q1 the pointwise sign and equality case; Q2 every $4\times2$ map over one alphabet per exponent: at $p=1$ (1616 passers) and $p=3$ (816) none has overlapping supports and every disjoint pair of unit columns passes; at $p=2$, 192 of 1008 passers overlap and all have $V^{\mathsf T}V=1$; countercontrol: without $e_1-e_2$, 4384 overlapping passers at $p=1$; Q3 the disjoint case symbolically; Q4 $\{cH,cH\}$: $p=2$, $c=1/2$ unique (by `solve` and by hand: $c^p=1/4$, then $2^p/4=1$), completeness follows, H-RF$_2$ on every complex vector; Q5 $K_1,K_2$ and $\{2^{-k/q}P_\sigma\}$ have disjoint dilation columns. rv5 T1–T4 re-run: byte-identical | **Accepted.** r5 stated the non-square clause for every non-square operation; it holds for the disjoint case only. The reviewer's second fix option (state the split) is applied, with the paper proof added so that the split is not supported by a finite alphabet alone. Lamperti is cited only as literature not read first-hand. Column (ii) does not change: in both cases the 2 comes from a posit | §0 item 2: the sentence "For a non-square operation … the 2 comes only from completeness, the posited quadratic normalisation (§3)" is replaced by: the split is by the supports of the dilation columns (§3); overlapping supports force $p=2$ under H-RF$_p$ on every vector, and completeness follows, as in the square case; disjoint supports require only $p$-normalised columns, so H-RF$_p$ holds at each $p>0$ for some non-monomial family and the 2 comes only from completeness. §3 *Without posited unitarity*: "does not force $p=2$" is replaced by the split with its proof (A; r6 Q1–Q2; Lamperti, L, not read first-hand); the overlapping case: $p=2$ forced, $V^\dagger V=1$ by polarization, completeness not posited, the 2 fixed by the posited linear kinematics with posited H-RF$_p$, instance $\{cH,cH\}$ (rv5 T2; r6 Q4); the disjoint case: H-RF$_p$ iff columns $p$-normalised, completeness iff 2-normalised (r6 Q3), "need not force $p=2$"; the $K_1,K_2$ pair and r3 E3's family keep their text, with "r6 check Q5" added; "For such an operation" becomes "For an operation with disjointly supported dilation columns, such as these and $\{2^{-k/2}P_\sigma\}$ (R3-N)". Re-grep: "does not force $p=2$" 0 hits; "only from completeness" 2 hits (§0 item 2, §3), both in the disjoint case. Checked and unchanged, as the review states: *FI-1 and R3* (a posited complete family; the column lemma on a 2-normalised column); R3-N's last column ($\{2^{-k/2}P_\sigma\}$ has disjoint dilation columns, r6 Q5); §5's NQ-1059 square clause; §8's r5 S1 entry, which describes the two disjoint families it checks |
| B1, DISPOSITIONS-r5 supersession row, statement (1) | `DISPOSITIONS-r5.md` (`086b9f49…2668`), row "B1(a) and B1(b), DISPOSITIONS-r4 N1 row", statement (1): "holds for square (endomorphic) operations only; for a non-square operation, such as a Kraus family's dilation, the 2 comes only from completeness" | **Accepted; DISPOSITIONS-r5 is not edited.** It is the change record paired with r5, kept unchanged at `r5/`; rewriting it would falsify what r5 claimed. This is the ground on which DISPOSITIONS-r3 and DISPOSITIONS-r4 were left unchanged, found correct in REVIEW-1059-r4 and REVIEW-1059-r5 (§A.27) | None to DISPOSITIONS-r5. This row supersedes its statement (1), second clause, with: "For a non-square operation the split is by the supports of the dilation columns. If two columns overlap in support, H-RF$_p$ on every amplitude vector forces $p=2$ and completeness $\sum_rK_r^\dagger K_r=1$ follows (e.g. $\{H/2,H/2\}$; rv5 T2; r6 Q4). If the columns are disjointly supported, H-RF$_p$ on every vector requires only that each column be $p$-normalised, and the 2 comes only from completeness, the posited quadratic normalisation ($K_1,K_2$; r3 E3's family; $\{2^{-k/2}P_\sigma\}$; r6 Q5)." Its first clause (the square case) and its statement (2) stand |

## Nits

| Nit | Verified against | Disposition | Change in r6 |
|---|---|---|---|
| N1: "A non-monomial nonnegative map satisfies H-RF$_1$ on every reachable state" reads as universal | rv5 T4: $N_2$ is nonnegative, non-monomial and fails H-RF$_1$ (re-run, byte-identical). Paper check: a nonnegative column-stochastic map sends nonnegative vectors of entry sum 1 to the same, and basis states are such, so every doubly stochastic map satisfies H-RF$_1$ on every reachable state; `probes/r4_dilation_gram.py` H1 names its matrix DS | Accepted | §3: "A non-monomial doubly stochastic map (r4 H1's DS) satisfies H-RF$_1$ on every reachable state". Re-grep: "nonnegative map satisfies" 0 hits |
| N2: r5 S3 cited as cancellation evidence | r5 S3's rotation $2^{-1/2}\bigl(\begin{smallmatrix}1&-1\\1&1\end{smallmatrix}\bigr)$: its first reachable state $(1,1)/\sqrt2$ has no cancellation and is 2-normalised only, so it forces $p=2$ before any cancellation. r4 H2's $M_p$ and rv3 F4 (docstring: "$M_p^2e_1$ forces $p=2$ (interference)") isolate cancellation | Accepted (drop, the first option) | §3: "(r4 H2; rv3 F4; r5 check S3)" → "(r4 H2; rv3 F4)". The other "r5 check S3" citation (for $N_q$ and $S$) is kept: S3 does check those. §8's description of r5's probe, "(cancellation)" for the rotation, is kept: it describes what that probe contains (the rotation's reachable set does include the cancelled state $R^2e_1=(0,1)$), and it is no longer cited as isolating cancellation; r5's probe is a frozen script and is not edited. Re-grep: "r5 check S3" 1 hit (§3, $N_q$ and $S$) |
| N3: §5's alternative is stale | #1169 c.6742190154, read with `gh api` (read only): author amaybaum, created 2026-11-09T14:13:27Z, item 5 "#1059's next question is folded into #1211/#1217 NQ1." | Accepted | §5: "*Alternative, if the owner prefers to stay within (b):*" → "*Alternative within (b), not selected (owner decision 5, #1169 c.6742190154; §7 OQ-2):*". The paragraph's content is unchanged. Re-grep: "prefers to stay" 0 hits |
| N4 (optional): OQ-3's "no H-Bell implication" is an open status, not a refutation | §0 item 2 ("none derived from another in the sources read"); OQ-3's preface ("no independence theorem involving H-Bell is stated"); c.6741291498's status vocabulary "proved, conditional, disproved or open" (as quoted in OQ-3) | Accepted | OQ-3, after decision 4's quotation: 'In that status field, "no H-Bell implication" is open (none derived in the sources read, §0 item 2), not disproved.' |

## Untraced changes (not from a review finding)

- **U1.** Header: "Revision r6"; REVIEW-1059-r5 (`4e343e55…42b7`, REVISE, bounded) added to the
  reviews; `r5/ASSESS-1059.md` (`63d54430…ef46`) added to the kept texts and DISPOSITIONS-r6 to the
  change maps; "Checks run" reads "Seven scripts".
- **U2.** §8 *Read*: REVIEW-1059-r5 in full with `review/rv5_1059_checks.py` (`10aa30d5…ae44`);
  #1169 c.6742190154 again (r6).
- **U3.** §8 *Probes*: the r6 probe entry; the re-run line: `r5_scope_checks.py` and
  `review/rv5_1059_checks.py` re-run from a scratch directory under `python3 -I`, both exit 0 and
  byte-identical to their recorded `.out` files.
- **U4.** §8 *Not done*: Lamperti added to the literature not read first-hand.

## Probe added

`probes/r6_column_support.py` (sha256
`386b2ef5a651511a5db035e0ae1472ff1b16faea1c42713b2e4f5faf7b353822`) has output
`probes/r6_column_support.out`
(`c362171f5d564ec76d7e645c3c63399efe23f830c384cc4a31adf870d30918d3`). It exits 0 under
`python3 -I` from `/tmp`, and a re-run is byte-identical. Label X: exact `Fraction` and sympy
computation on generic matrices and vectors. It imports no earlier script and computes nothing on
an OI mechanism. Its checks are Q1–Q5 (B1). Q1–Q2 are instances of the paper proof's step and of
its conclusion over finite alphabets, not a proof; the general statement rests on the paper
argument (A), with Lamperti cited as literature (L, not read first-hand). Mutation-tested: six
single-line mutants (`n1`–`n6`, listed in the script's docstring and in §8 of r6) each turn the
affected check to FAIL; the mutants are argument-selected in the script, so no mutant file exists.
