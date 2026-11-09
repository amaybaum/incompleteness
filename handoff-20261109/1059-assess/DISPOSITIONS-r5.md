# ASSESS-1059 r5: dispositions of REVIEW-1059-r4

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** This file maps each finding
of `review/REVIEW-1059-r4.md` (sha256
`93ae3b1743643404ddddea9e03661b39566b3623b26f167dd5a176bb8f76ea87`, REVISE, bounded) to its change
in `ASSESS-1059.md` r5 (sha256
`63d544308cafc8859c7c89a630a5bace1303e2c0c5870b0993a44b5ace52ef46`). r4 is at `r4/ASSESS-1059.md`
(`7fa70fc0c2769912ea1beddd3dd4fa05aa962e94050cd3b1428aadb6c667c085`), copied unchanged and
verified after copying.

Each finding was checked before it was applied: against its source at `fd539e15`
(`fd539e150759a6ea51ab279aeeac80fc06050ade`, present locally, read with `git show fd539e15:<path>`),
against the cited draft or script, or by a new exact check. No git fetch was needed, and
`--depth`, gc and prune were not used. No repo, git or GitHub write was made; the two #1169
comments were read with `gh api` (read only).

No finding was refused outright. One part is refused, with reasons: DISPOSITIONS-r4 is not edited
(B1(a) and B1(b), DISPOSITIONS rows). One change goes beyond the review and the brief and is
flagged for the coordinator: OQ-3 is marked resolved by owner decision 4 of the same comment.

## Blocker

| Finding | Verified against | Disposition | Change in r5 |
|---|---|---|---|
| B1(a): the every-vector (Aaronson) form holds for square (endomorphic) maps only | BORN-SRC-1 C2 as reported (`src/914-bornsrc.txt`:209–210, :317–318: "only monomial maps preserve a p-norm, p ≠ 2"), which concerns a map of a space to itself. The reviewer's counterexample re-derived independently in new r5 check S1 (symbolic $p$, moduli and phases): $K_1=2^{-1/p}\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)$, $K_2=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ gives outcome-table sum $\lvert x_1\rvert^p+\lvert x_2\rvert^p$ on every input, $K_1$ is non-monomial, complete only at $p=2$. The r3 E3 family $\{2^{-k/q}P_\sigma\}$ ($k=1,2$; $q=2,3,4$): table sum $2^{k(1-p/q)}\sum\lvert x_i\rvert^p$, so H-RF$_p$ on every vector iff $p=q$; dilation columns with $2^k$ nonzero entries; complete iff $q=2$. Square controls (S2, instances only). rv4 G3 re-run: byte-identical | **Accepted.** r4's "for $p\neq2$ every admissible operation is monomial … unitary when square" admitted non-square operations, for which the first clause is false, and §0 item 2 dropped the scope | §3 *Without posited unitarity*: "operations stay linear and square (endomorphic: maps of the amplitude space to itself)"; the Aaronson citation adds "it concerns a map of a space to itself"; "a square non-monomial admissible operation forces $p=2$"; "and, being square, unitary" replaces "unitary … when square". Added: for a non-square operation (a Kraus family read on its outcome table, or its dilation) H-RF$_p$ on every amplitude vector does not force $p=2$, with the $K_1,K_2$ pair and r3 E3's family at $p=q$ (rv4 G3; r5 S1), and "for such an operation the 2 comes only from completeness $\sum_rK_r^\dagger K_r=1$, the posited quadratic normalisation". §0 item 2: "a square (endomorphic) non-monomial linear operation", plus one sentence: for a non-square operation, such as a Kraus family's dilation, H-RF$_p$ on every vector holds at each $p>0$ for some non-monomial family, and the 2 comes only from completeness. §5 NQ-1059 clause (optional per the review; applied for consistency with §3): "the operation's linearity, as a square (endomorphic) map on complex amplitudes". Re-grep: "when square" 0 hits; "square (endomorphic)" 2 hits (§0 item 2, §5), and §3 states the scope in its own words |
| B1(b): "interference on a reachable state is needed for that route" is false | New r5 check S3 recomputes the reachable-state route two ways (intersection of each reachable state's own normalisation exponent; direct exact test at sampled exponents). $N_q=\bigl(\begin{smallmatrix}0&0&0\\a&1&0\\a&0&1\end{smallmatrix}\bigr)$, $a=2^{-1/q}$, nonnegative, non-monomial, singular: $\{q\}$ for $q=2,3$. $S=\bigl(\begin{smallmatrix}0&1&-1\\1/2&0&0\\-1/2&0&0\end{smallmatrix}\bigr)$, signed reachable states: $\{1\}$. The 45° rotation (cancellation): $\{2\}$. Signed permutation (control): every $p$. rv4 G4 and r4 H1–H2 re-run: byte-identical | **Accepted.** At $q=2$, $N_q$ forces $p=2$ with no sign and no cancellation and is not unitary; $S$ is signed and forces 1. The operative feature in r4 H2 is cancellation, not a sign | §3 *Without posited unitarity*: the clause "an instance with a sign forces $p=2$ …, but no general statement is established here, … so interference on a reachable state is needed for that route" is replaced by: on that route the readout admits exactly the exponents in which every reachable state is normalised (the column lemma applied to the reachable states), the map's own normalisation sets it, so non-monomiality does not force 2 there; r4 H1 (nonnegative, $p=1$); $N_q$ ($p=q$; at $q=2$ no sign, no cancellation, not unitary); $S$ ($p=1$) (rv4 G4(a)–(b); r5 S3); "An instance with cancellation forces $p=2$ (r4 H2; rv3 F4; r5 check S3)". Re-grep: "interference on a reachable" 0 hits |
| B1(a) and B1(b), DISPOSITIONS-r4 N1 row | `DISPOSITIONS-r4.md` (`c6e4fcd9…10ba`), N1 row: "r4 states the supported form: H-RF$_p$ on every amplitude vector gives $p\ne2$ ⇒ monomial" and "with the nonnegative counterexample showing that interference on a reachable state is needed" | **Partly refused.** DISPOSITIONS-r4 is left unchanged. Reason: it is the record of the r3 → r4 changes, paired with r4, which is kept unchanged at `r4/`; editing it would rewrite what r4 claimed. This is the same ground on which DISPOSITIONS-r3 was left unchanged in r4, which REVIEW-1059-r4 found correct (§A.27; the change record lives outside the text). The correction is recorded here instead | None to DISPOSITIONS-r4. This row supersedes two statements of its N1 row. (1) "H-RF$_p$ on every amplitude vector gives $p\ne2$ ⇒ monomial" holds for square (endomorphic) operations only; for a non-square operation, such as a Kraus family's dilation, the 2 comes only from completeness. (2) "the nonnegative counterexample showing that interference on a reachable state is needed" is withdrawn: on the reachable-state route the readout admits the normalisation exponent of the reachable states, and a nonnegative non-monomial map can set it at 2 (rv4 G4(a); r5 S3) |

## Nits

| Nit | Verified against | Disposition | Change in r5 |
|---|---|---|---|
| N1: D-label collision | `review/rv2_1059_checks.py` docstring: D1 column lemma, D2 Stinespring of $\{2^{-k/2}P_\sigma\}$, D3 the instrument $\{\lvert0\rangle\langle+\rvert,\lvert1\rangle\langle-\rvert\}$ and the unscaled $K$. r4's own D0–D2 are the dilation Gram checks of `probes/r4_dilation_gram.py` | Accepted, and applied to F4 too (`review/rv3_1059_checks.py`'s F4), since "the reviewer's check F4" has the same ambiguity across four review scripts | R3-N row "rv2 D2"; R3-C row "rv2 D3"; column lemma "rv2 D1 is the same check"; *FI-1 and R3* "rv2 D3"; §3 "rv3 F4" (×2); §8 "cited as rv2 D1–D3", "cited as rv3 F4". "r4 check D1" and "r4 D1" are unchanged. Re-grep: "reviewer check D" 0, "reviewer's D1" 0, "reviewer's check F4" 0. "the reviewer's check rv C6" and "the reviewer's rv C5" already carry the prefix and are kept |
| N2: BRIDGE r5 status | `sha256sum`: `scratchpad/bridge/BRIDGE-UNIT1.md` = `78f1098ee4310b0a190e211add27094025f95d3d1fa7d9b0fd77eaf260cf91a4`; `scratchpad/bridge/review/REVIEW-UNIT1-r5.md` = `0ef5644f2400df0c5eb300fcfcbdceb6950e7a70484e0671bab5480703a58c76`, whose header names r5 at `78f1098e…91a4` and whose l.43 reads "**Verdict: ACCEPT WITH NITS.** No blocking issue was found." | Accepted. No conclusion changes: a draft ACCEPT is not `main` (§A.46 item 7) | Header: r5 "reviewed ACCEPT WITH NITS in `scratchpad/bridge/review/REVIEW-UNIT1-r5.md` (`0ef5644f…8c76`), a draft review, not `main`; r5 was not read for this unit, and the BRIDGE citations stay pinned to r4". §8 lists REVIEW-UNIT1-r5 header and verdict as read. Re-grep: "under review" 0 hits |
| N3: cite #1169 c.6741291498 at OQ-2/OQ-3 | Read with `gh api` (read only): author amaybaum, created 2026-11-09T13:30:54Z. It quotes "Decide whether #1059 and #868 need independent follow-up experiments rather than treating success on FI-1 as solving both", and states that each matrix dependency carries "a status: proved, conditional, disproved or open; its carrier: configuration or encoded; its assumptions" | Accepted | OQ-2: the quoted question, with r5's answer on #1059's side: FI-1 is necessary under named hypotheses and not sufficient for the exponent or the law (§0 item 2, §4.4, OQ-1). OQ-3: the matrix is identified as that of c.6741291498, with the quoted status/carrier/assumptions fields. §8 lists the comment as read |
| N4: "BORN-SRC-1 C4 at $n=2$" | `src/914-bornsrc.txt`:213–216 and :325–328 (the review cites :331–333; the content is as it states): C1 is $g(x)=x+x(1-x)(1-2x)$, normalising on $n=2$; C4 normalises "every column of the 3-4-5 rotation ⊕ 1", a 3-state carrier | Accepted | §0 item 2: "BORN-SRC-1 C1 at $n=2$ and C4 at $n=3$". Re-grep: "C4 at $n=2$" 0 hits. The other C4 citations (R3-C, R4, §4.3, §4.4, F-b) do not state $n$ and are kept |

## Owner decision on record (coordinator brief)

| Item | Verified against | Disposition | Change in r5 |
|---|---|---|---|
| OQ-2 resolved by owner decision 5 | #1169 c.6742190154, read with `gh api` (read only): author amaybaum, created 2026-11-09T14:13:27Z, "Owner decisions 1–8", approved as "Approve 1–8 as listed"; item 5 verbatim: "#1059's next question is folded into #1211/#1217 NQ1." The comment adds: "None of decisions 1–8 authorizes a scientific computation, an F or E designation, a dispatch, a freeze or a merge." | Applied | OQ-2 marked resolved, with the question as asked, the verbatim decision, author and time, "NQ-1059 is therefore folded into #1211/#1217 NQ1", and the no-authorization sentence. As necessary consequences: §0 item 5 adds "By owner decision it is folded into #1211/#1217 NQ1 (§7 OQ-2)"; §5's scope guard "It must not duplicate them" becomes "by owner decision it is folded into #1211/#1217 NQ1 (#1169 c.6742190154; §7 OQ-2)". NQ-1059's content and its added conditions are unchanged |
| OQ-3 resolved by owner decision 4 (**beyond the brief; flagged**) | Same comment, item 4 verbatim: "The matrix records scoped relations: phase is independent of the layer flow only; the complex drive carries the phase; no H-Bell implication." This answers OQ-3's question ("Should the planned dependency matrix record these scoped relations rather than an unqualified independence?") in the affirmative, and agrees with §0 item 2's scoped relations | Applied, because leaving OQ-3 open beside a recorded owner answer in the comment cited at OQ-2 would be a stale status surface. The coordinator may revert it to an open question with a citation only | OQ-3 marked resolved, with the question as asked and decision 4 verbatim. No other text changes: §0 item 2 already states the same three scoped relations |

## Untraced changes (not from a review finding)

- **U1.** Header: "Revision r5"; REVIEW-1059-r4 (`93ae3b17…ea87`, REVISE, bounded) added to the
  reviews; `r4/ASSESS-1059.md` (`7fa70fc0…c085`) added to the kept texts and DISPOSITIONS-r5 to the
  change maps. "Checks run" reads "Six scripts".
- **U2.** §8 *Read*: REVIEW-1059-r4 in full with `review/rv4_1059_checks.py` (`cf6f2b38…a967`);
  #1169 c.6741291498 and c.6742190154; REVIEW-UNIT1-r5 header and verdict; BORN-SRC-1 C1 and C4
  lines; Main:218 at `fd539e15` (re-read for B1's attribution; unchanged).
- **U3.** §8 re-run line: in r5, P1, P2, `r2_fi1_scope.py`, `r3_exponent_source.py`,
  `r4_dilation_gram.py`, `rv_`, `rv2_`, `rv3_` and `rv4_1059_checks.py` were re-run under
  `python3 -I` from a scratch directory; each exits 0 and is byte-identical to its recorded `.out`.

## Probe added

`probes/r5_scope_checks.py` (sha256
`ecda6683a702bf3e1f73e4775be09ade978e5f65c1ddd1a2a00b39b60221582e`) has output
`probes/r5_scope_checks.out`
(`9459e693f750f395217469f848abc1ce95aeff7339e287d5162acabf573b79c8`). It exits 0 under
`python3 -I` from `/tmp`. Label X: exact sympy computation on generic matrices and vectors. It
imports no earlier script and computes nothing on an OI mechanism. Its checks are S1 and S2
(B1(a)) and S3 (B1(b)); S2 is a set of square instances consistent with the endomorphic form, not a
proof of it, which stays cited as literature (L, not read first-hand). Mutation-tested: ten
single-line mutants each turn the affected check to FAIL (S1 ×4, S2 ×2, S3 ×4, listed in §8 of r5;
the mutant files were not kept).
