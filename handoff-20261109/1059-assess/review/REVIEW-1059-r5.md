# Review of ASSESS-1059 r5 (BORN-SEL, #1059): fresh, independent, paper-only delta review

**Model-written (Claude Code subagent, 2026-11-09). WIP / UNVERIFIED.** This review adopts nothing,
edits no record and authorizes nothing. It made no git or GitHub write. GitHub access was two
reads with `gh api`: #1169 c.6741291498 and c.6742190154.

- **Under review.** `ASSESS-1059.md` r5, sha256
  `63d544308cafc8859c7c89a630a5bace1303e2c0c5870b0993a44b5ace52ef46`, verified before reading.
  Also read:
  - `DISPOSITIONS-r5.md` (`086b9f49…2668`), in full;
  - `r4/ASSESS-1059.md` (`7fa70fc0…c085`, verified); the full `diff` r4 → r5;
  - `review/REVIEW-1059-r4.md` (`93ae3b17…ea87`, verified);
  - `DISPOSITIONS-r4.md` (`c6e4fcd9…10ba`, verified; unchanged);
  - `probes/r5_scope_checks.py` (`ecda6683…582e`, verified) and its `.out` (`9459e693…79c8`,
    verified); `probes/r4_dilation_gram.py` docstring (H1–H3).
- **Sources.** `fd539e15` is present locally (`git cat-file -t`: commit). Read with
  `git show fd539e15:<path>`: Main:218. BORN-SRC-1 C1, C2 and C4 from `src/914-bornsrc.txt`:205–216
  and :317–335. Drafts hashed only: `bridge/BRIDGE-UNIT1.md` (`78f1098e…91a4`) and
  `bridge/review/REVIEW-UNIT1-r5.md` (`0ef5644f…8c76`, l.43 "Verdict: ACCEPT WITH NITS").
- **Reviewer probe.** `review/rv5_1059_checks.py` (sha256
  `10aa30d5083f3db92bfe9ef12e08be7ac3db7a4fda4d6952008526236089ae44`), with output
  `review/rv5_1059_checks.out`
  (`47b6aa3f7f60df22dca477c412381c8b9e7910c8dcde8b9f8f7dd12c42d04684`).
  - It exits 0 under `python3 -I` and imports nothing earlier. It uses exact `Fraction` and sympy
    arithmetic on generic matrices and vectors only (T1–T4, docstring).
  - Mutation-tested: seven single-line mutants (argument `m1`–`m7`) each turn the affected check to
    FAIL:
    - `m1` drops the $e_i-e_j$ probe (T1);
    - `m2` replaces the second Kraus operator (T2);
    - `m3` makes $K_2$'s columns overlap (T3);
    - `m4` zeroes $N_q$'s entry (2,1) (T4);
    - `m5` fixes $M_p$'s scale at $2^{-1/2}$ (T4);
    - `m6` makes the disjointness decider constant (T1, the countercontrol);
    - `m7` removes $-1/2$ from the alphabet (T1, the non-vacuity guard).

## Verdict: REVISE (bounded)

The square half of B1(a) is fixed correctly, and so is B1(b). Nits 1–4 are applied correctly. The
partial refusal to edit DISPOSITIONS-r4 is correct. Both owner decisions are quoted accurately
and applied within scope. Every diff hunk is accounted for, and no column-(ii) verdict or
conclusion changed.

One new overstatement blocks acceptance (B1). It is in the non-square clause that r5 added for
B1(a). That clause follows the fix wording of REVIEW-1059-r4, and the wording overreached. The
clause holds for the two families it exhibits. As a statement about every non-square operation
it is false. Column (ii) does not change: in every case the 2 comes from a posit.

A delta review of the B1 sentences, the matching DISPOSITIONS-r5 supersession row and nits 1–3 is
enough.

## Blocker

**B1. The non-square clause is stated for every non-square operation; it holds only when the
dilation columns have disjoint supports.**

- *Where.* All three sites are new r5 text:
  - §0 item 2 (l.93–96): "For a non-square operation, such as a Kraus family's dilation, H-RF$_p$
    on every amplitude vector holds at each $p>0$ for some non-monomial family, and the 2 comes
    only from completeness, the posited quadratic normalisation";
  - §3 *Without posited unitarity* (l.287–296): "For a non-square operation, such as a Kraus family
    read on its outcome table (§1) or its dilation, H-RF$_p$ on every amplitude vector does not
    force $p=2$ … For such an operation the 2 comes only from completeness";
  - DISPOSITIONS-r5, supersession row, statement (1).
- *Rule.* Code Review Rules, "Claim/evidence boundary": witness → universal claim. The evidence,
  rv4 G3 and r5 S1, is two families. Both have disjointly supported dilation columns (rv5 T3).
- *Counterexample (rv5 T2, exact, symbolic $p$ and scale $c>0$).*
  - Take the Kraus family $\{cH,cH\}$ with $H=\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)$.
    It is a non-square operation with a $4\times2$ dilation and a non-monomial $K$, and its two
    dilation columns overlap in support.
  - H-RF$_p$ on $e_1$ gives $4c^p=1$. On $e_1+e_2$ it gives $2(2c)^p=2$.
  - The unique solution is $p=2$, $c=1/2$.
  - Completeness $\sum_rK_r^\dagger K_r=1$ then follows; it is not posited. H-RF$_2$ holds on every
    complex vector (symbolic moduli and phases).
  - So for this non-square operation, H-RF$_p$ on every vector does force $p=2$. The 2 then comes
    from the linear kinematics together with H-RF$_p$, exactly as in the square case, and not
    "only from completeness".
- *The general picture (rv5 T1, exhaustive over the alphabet $\{0,\pm\tfrac12,\pm1\}$).*
  - Square $2\times2$ and $3\times3$ maps passing H-RF$_1$'s necessary conditions are all
    monomial.
  - Of the 336 non-square $4\times2$ maps that pass at $p=1$:
    - each has disjointly supported columns;
    - 256 have a non-monomial $2\times2$ block.
  - Of the 144 that pass at $p=2$:
    - each has $V^{\mathsf T}V=1$;
    - 96 have overlapping column supports.
  - Countercontrol: with the signed probe dropped, 320 overlapping maps pass at $p=1$. This is the
    reachable-state situation.
  - This is the finite-dimensional case of Lamperti's disjointness result. For $p\neq2$, a
    $p$-norm-preserving linear map has disjointly supported columns, each $p$-normalised.
  - The operative split is therefore by disjointness of the column supports, not square versus
    non-square. For a square map, disjointness is the same as monomiality.
- *What is right.* For the exhibited families, $K_1,K_2$ and r3 E3's $\{w^{1/q}P_\sigma\}$, the
  dilation columns are disjoint (rv5 T3). There H-RF$_p$ on every vector admits the exponent of
  the columns' own normalisation, and the 2 comes only from completeness. This also covers the
  configuration carrier's monomial Kraus families $\{2^{-k/2}P_\sigma\}$ (R3-N).
- *Fix.* Two options; either is enough:
  - narrow the clause to its witnesses: "need not force $p=2$", "for these families the 2 comes
    only from completeness", and add one sentence: "a non-square operation whose dilation columns
    overlap in support, such as $\{H/\sqrt2,H/\sqrt2\}$, is forced to $p=2$ as in the square case
    (rv5 T2)";
  - or state the split: for $p\neq2$, H-RF$_p$ on every vector requires disjointly supported,
    $p$-normalised dilation columns (Lamperti; computation-supported here on the T1 alphabet). So
    overlapping supports force $p=2$, with completeness following. Disjoint supports admit the
    columns' own exponent, and there the 2 comes only from completeness.

  Make the same change in §0 item 2 and in DISPOSITIONS-r5's supersession statement (1). §3's
  "does not force" becomes "need not force". The other passages that depend on these sentences
  are unaffected; each was checked:
  - *FI-1 and R3*: a 2-normalised dilation column forces $p=2$ through the posited normalisation.
    This is the column reading, and it is correct.
  - R3-N's last column: $\{2^{-k/2}P_\sigma\}$ has disjoint dilation columns.
  - NQ-1059's square clause: a unitary on a block is square.

## Nits

1. **"A non-monomial nonnegative map satisfies H-RF$_1$ on every reachable state" (§3, l.299–300).**
   - In r4 this was a subordinate clause. In r5 it stands as a sentence of its own, so it reads
     as universal.
   - Read that way it is false. $N_2$, introduced two lines later, is nonnegative and
     non-monomial and fails H-RF$_1$ (rv5 T4).
   - Write "A non-monomial doubly stochastic map (r4 H1's DS) satisfies …".
2. **"An instance with cancellation forces $p=2$ (r4 H2; rv3 F4; r5 check S3)" (l.306–307).**
   - r4 H2's $M_p=2^{-1/p}\bigl(\begin{smallmatrix}1&-1\\1&1\end{smallmatrix}\bigr)$ isolates
     cancellation. Its first reachable state is $p$-normalised at every $p$, and only the
     cancelled state $M_p^2e_1$ forces 2.
   - r5 S3's rotation has the fixed scale $2^{-1/2}$. Its first reachable state, $(1,1)/\sqrt2$,
     has no cancellation and already forces $p=2$ (rv5 T4).
   - So S3 is not evidence that cancellation forces 2. Drop "r5 check S3" there, or relabel S3's
     "(cancellation)" in §8 and in the probe's docstring.
3. **§5's *Alternative, if the owner prefers to stay within (b)* (l.589) is stale.** Decision 5
   fixes #1059's next question as NQ-1059, folded into #1211/#1217 NQ1. The writer's reason for
   resolving OQ-3 applies here too: an open offer beside a recorded owner answer is a stale status
   surface. Mark the alternative "not selected (owner decision 5; §7 OQ-2)", or remove it.
4. **OQ-3 (optional).** Decision 4's "no H-Bell implication" corresponds to §0 item 2's "none
   derived from another in the sources read". It is not a refutation, and the OQ-3 preface says
   only that "no independence theorem involving H-Bell is stated". One clause would keep the
   matrix entry's status explicit: in c.6741291498's terms, "open, none derived in the sources
   read". An owner planning decision confers no scientific status (§A.45 rule 1).

## Checks performed

**1. B1(a) and B1(b).**
- *Square form: correct.*
  - §3 now restricts to "linear and square (endomorphic: maps of the amplitude space to itself)".
    It notes that the Aaronson result concerns a self-map, and it reads "being square, unitary".
    §0 item 2 and §5 carry "square (endomorphic)".
  - "when square" has 0 hits.
  - This is the Banach–Lamperti statement for $\ell^p_n$, $p\neq2$. rv5 T1 is consistent with it:
    every square passer at $p=1$ is monomial.
- *Dilation case: correct for the exhibited families only.* See B1.
- *B1(b): fixed correctly.* "The readout admits exactly the exponents in which every reachable
  state is normalised … so non-monomiality does not force 2 on that route" is true.
  - Basis states are normalised at every $p$. A reachable state with at least two nonzero entries
    of modulus in $(0,1)$ has at most one exponent (column lemma). The admissible set is the
    intersection, possibly empty.
  - rv5 T4 recomputes these values independently:
    - $N_q$ for symbolic $q$: the reachable set closes on four states, and the admissible set is
      $\{q\}$;
    - $S$: $\{1\}$;
    - $M_p$: cancellation forces 2.
  - "interference on a reachable" has 0 hits.
- *r5's probe.* `probes/r5_scope_checks.py` re-runs byte-identically. S3's "two ways" both sample
  the exponent set {1/2, 1, 3/2, 2, 3, 4}. Method A's uniqueness rests on the strict-decrease
  argument, which the probe checks, so it is exact. Method B is a sampled test, and the docstring
  says so.

**2. Nits 1–4 of REVIEW-1059-r4.**
- **N1: applied.** "reviewer check D", "reviewer's D1" and "reviewer's check F4" have 0 hits.
  rv2 D1–D3 and rv3 F4 are used throughout. Extending the change to F4 is a correct reading of the
  same ambiguity.
- **N2: applied.** Both hashes match. REVIEW-UNIT1-r5 l.43 reads ACCEPT WITH NITS. "under review"
  has 0 hits. The citations stay pinned to r4, and §A.46.7 is respected.
- **N3: applied.** The quotation from c.6741291498 is verbatim. The field list "a status: proved,
  conditional, disproved or open; its carrier: configuration or encoded; its assumptions" is
  verbatim from the comment's "How this is applied" section. It is attributed to the comment, not
  to the owner's own words, and that attribution is correct.
- **N4: applied.** "C1 at $n=2$ and C4 at $n=3$" matches `src/914-bornsrc.txt`:205–216 (C1
  normalises on $n=2$; C4 normalises "every column of the 3-4-5 rotation ⊕ 1"). "C4 at $n=2$" has
  0 hits.

**3. Refusal to edit DISPOSITIONS-r4: correct.**
- DISPOSITIONS-r4 is the change record paired with the r4 text kept at `r4/`. Rewriting it would
  falsify what r4 claimed (§A.27: the change record lives outside the text; provenance is
  preserved).
- REVIEW-1059-r4 accepted the same ground for DISPOSITIONS-r3.
- The supersession row in DISPOSITIONS-r5 names both N1-row statements it supersedes. That is the
  right mechanism. Its statement (1) carries B1's overstatement and needs the same fix.
- DISPOSITIONS-r4 hashes unchanged.

**4. Owner decisions.**
- **Source.** c.6742190154: author amaybaum, created 2026-11-09T14:13:27Z, "Approve 1–8 as
  listed". Decisions 4 and 5 are quoted verbatim in OQ-3 and OQ-2, character for character. The
  no-authorization sentence is reproduced accurately at OQ-2.
- **OQ-2 / decision 5: within scope.**
  - The decision is a planning act. r5 applies it only to:
    - OQ-2's status;
    - a pointer in §0 item 5;
    - §5's overlap guard, "must not duplicate" → "folded into".
  - NQ-1059's content and conditions are unchanged. Nothing is presented as authorized or as
    scientifically established.
  - One consequence was missed: §5's alternative (nit 3).
- **OQ-3 / decision 4: within scope.** The decision answers OQ-3's question ("should the planned
  dependency matrix record these scoped relations?") in the affirmative. Its three relations agree
  with §0 item 2:
  - layer-flow-only independence;
  - the drive carries the phase;
  - no H-Bell implication.

  No other text changed. The writer flagged it as beyond the brief, and the present brief covers
  it. Nit 4 is optional.

**5. Probes and diff accounting.**
- *Re-runs.* All ten earlier scripts were re-run under `python3 -I` from a scratch directory: P1,
  P2, r2, r3, r4, r5, rv, rv2, rv3 and rv4. Each exits 0 and is byte-identical to its recorded
  `.out`. "Six scripts" is correct: P1, P2, r2, r3, r4 and r5.
- *Diff accounting.* Every hunk of `diff r4 r5` maps to a disposition:

  | Hunk | Disposition |
  |---|---|
  | header and "Six scripts" | U1 |
  | BRIDGE status | N2 |
  | §0 item 2 | B1(a), N4 |
  | §0 item 5 | OQ-2 |
  | R3-N, R3-C, the column lemma, l.350 | N1 |
  | §3 paragraph | B1(a), B1(b), N1 |
  | §5 clause | B1(a) |
  | §5 guard | OQ-2 |
  | OQ-2 and OQ-3 | owner decisions, N3 |
  | §8 | U2, U3 and the probe entry |

  No hunk is untraced.
- *Verdicts unchanged.*
  - The R3-N and R3-C rows differ only in "rv2 D2/D3". No column-(ii) entry changed.
  - The central conclusion stands: nothing on `main`, and no draft read, derives exponent 2 or
    the Born law from independently justified OI principles.

**6. Scope, columns and register.**
- *Columns.* No column-(iii) result is cited for column (ii). The new text keeps "posited, not
  derived from OI".
- *Scope.* The new reachable-state and non-square statements are scoped to H-RF$_p$ variants, not
  to OI, except for the overreach in B1.
- *Register.* No caps emphasis, reader instruction or self-assessment appears in the added lines.
  "(resolved)" and "Asked:" are status idiom in a working assessment, not manuscript prose
  (§A.32–§A.33 bind `papers/`).
- *Header.* It states no adoption or authorization.
