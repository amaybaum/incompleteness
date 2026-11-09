# Review of ASSESS-1059 r4 (BORN-SEL, #1059): fresh, independent, paper-only

**Model-written (Claude Code subagent, 2026-11-09). WIP / UNVERIFIED.** This review adopts nothing,
edits no record and authorizes nothing. It made no git or GitHub write. The only GitHub access was
one read of #1169 c.6741291498.

- **Under review.** `ASSESS-1059.md` r4, sha256
  `7fa70fc0c2769912ea1beddd3dd4fa05aa962e94050cd3b1428aadb6c667c085`, verified before reading.
  Also read:
  - `DISPOSITIONS-r4.md` (`c6e4fcd9…10ba`);
  - `r3/ASSESS-1059.md` (`85fd3d4b…8465`, verified), word-diffed against r4;
  - `review/REVIEW-1059-r3.md` (`d9d8fd93…325c`, verified);
  - `probes/r4_dilation_gram.py` (`22e0fdb3…8998`, verified) and its `.out` (`d66f0b58…a34b`,
    verified);
  - `review/rv3_1059_checks.py` (`b0d99862…0151`).
- **Sources.** Read with `git show fd539e15:<path>` after `git fetch origin main`
  (`fd539e15` = `fd539e150759a6ea51ab279aeeac80fc06050ade`, an ancestor of `origin/main`).
  - GR:248–272.
  - Main:218.
  - StructuralClosure.lean:170–185 and :305–322.
  - C5Discovery.lean:1–62 and :158–166.
  - StateMixingCoupling.lean:1–40.
  - CoherentContinuumSource.lean:70–76.
  - SubstratumInterface.lean:73–95.
  - LiftAudit.lean:655–662.
  - `git diff --word-diff 02009693 fd539e15 -- book/glossary.md`; `cmp` of glossary:21 against
    FULL:6604.

  Drafts, read as hypotheses only: `bridge/r4/BRIDGE-UNIT1.md` and `bridge/BRIDGE-UNIT1.md`, hashed
  only; `bridge/review/REVIEW-UNIT1-r5.md` (`0ef5644f…8c76`, verified), header and verdict.
  BORN-SRC-1 C2 was read from `src/914-bornsrc.txt`:205–215 and :310–335.
- **Reviewer probe.** `review/rv4_1059_checks.py` (sha256
  `cf6f2b38582e1a4aec4aab891854ca307a56d40a928c0cf4455df8d03c21a967`), with output
  `review/rv4_1059_checks.out` (`f5feac5ae9132342354a24e67711339812f5531866677ee9bd8652e3b5618980`).
  - It exits 0 under `python3 -I` and imports nothing earlier.
  - It computes on generic columns, matrices and Kraus families only (G1–G4, docstring).
  - Mutation-tested: eight single-line mutants each turn the affected check to FAIL. They are: a
    wrong exponent in G1; the orthogonality filter dropped in G2; a columns-only monomial decider; a
    value set without non-monomial complete families (the non-vacuity guard); K2 rescaled in G3;
    the nonnegative map's entry set to 1/2 in G4; a sign removed from G4's signed map; and a
    non-monomial control in G4.

## Verdict: REVISE (bounded)

The r3 blocker is fixed properly. The dilation lemma is now cited as its written proof (A), and
r4 D1 is a genuine, non-vacuous computation. All seven r3 nits are applied correctly, and N7's
strengthened §4.1 negative is supported on `main` at every citation.

The writer's partial refusal of N1 is correct. The reachable-state form of the "without posited
unitarity" case is false as a general statement, and the r3 review's F4 overreaches in exactly
that way. But the new paragraph that replaces it makes two overstatements of its own (B1):
- the every-vector (Aaronson) form is stated without the restriction to square maps, which it
  needs, and which the text's own Kraus framework violates;
- its closing clause, "interference on a reachable state is needed for that route", is false.

Neither changes a column-(ii) verdict or the unit's central conclusion. Nothing on `main`, and no
draft read, derives exponent 2 or the Born law from independently justified OI principles. A delta
review of the passages named under B1 and nits 1–2 is enough.

## Blocker

**B1. The new *Without posited unitarity* case overstates in two places.**

Where: §3 *Without posited unitarity* (l.271–283); §0 item 2 (l.86–90); the §5 NQ-1059 clause
(l.528–531); the DISPOSITIONS-r4 N1 row. Rule: Code Review Rules, "Claim/evidence boundary"
(a changed mathematical claim stronger than its evidence). This is new r4 text.

- **(a) The every-vector form holds for square (endomorphic) maps only.** §3 says that with
  H-RF$_p$ on every amplitude vector, "for $p\neq2$ every admissible operation is monomial", and
  then "unitary … when square". That admits non-square operations, for which the first clause is
  false. §0 item 2 drops the scope entirely: "a non-monomial linear operation … also fixes
  $p=2$ and is then unitary".
  - *Counterexample (rv4 G3, exact, symbolic $p$).* Take $K_1=2^{-1/p}\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)$
    and $K_2=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$. $K_1$ is non-monomial. For
    every $p>0$ and every input, the outcome table has $\sum|\cdot|^p=|x_1|^p+|x_2|^p$, so
    H-RF$_p$ holds on every amplitude vector at every $p$. The family is complete only at $p=2$.
  - The text's own r3 E3 family $\{w^{1/q}P_\sigma\}$ is a second instance, at $p=q$. Its dilation
    columns have $2^k$ entries, and the family is complete only at $q=2$.
  - So for a Kraus family or dilation, which §1 brings under H-RF$_p$, the 2 comes from the
    completeness $\sum K^\dagger K=1$ (the posited quadratic normalisation), not from H-RF$_p$ on
    every vector. The Aaronson/Lamperti form, as BORN-SRC-1 C2 reports it ("only monomial maps
    preserve a p-norm"), concerns a map of a space to itself.
  - *Fix:* write "square (endomorphic)" at §0 item 2 and in §3. Add one clause: for a non-square
    operation (a Kraus family's dilation), H-RF$_p$ on every vector admits every $p$, and $p=2$
    comes only from completeness, the posited kinematics. NQ-1059's clause concerns a unitary on
    a block, so it is square already; "endomorphic" there is optional.
- **(b) "Interference on a reachable state is needed for that route" is false.**
  - *Counterexample (rv4 G4(a), exact).* $N_q=\bigl(\begin{smallmatrix}0&0&0\\a&1&0\\a&0&1\end{smallmatrix}\bigr)$
    with $a=2^{-1/q}$. It is nonnegative, non-monomial and singular. Its reachable set from the
    basis states closes on $\{e_1,e_2,e_3,(0,a,a)\}$, and H-RF$_p$ holds there iff $p=q$.
    - At $q=2$ it forces $p=2$ with no sign and no cancellation, so interference is not needed.
      The map forcing 2 is not unitary.
    - At $q=3$ it forces $p=3$.
  - *A signed map without cancellation (rv4 G4(b)).* $S=\bigl(\begin{smallmatrix}0&1&-1\\1/2&0&0\\-1/2&0&0\end{smallmatrix}\bigr)$
    has signed reachable states $\{\pm e_1,\pm(0,\tfrac12,-\tfrac12),e_2,e_3\}$ and admits only
    $p=1$.
  - On that route the forced exponent is the one in which the reachable states are normalised.
    That is the column lemma again, and the map's own normalisation sets it. H1 shows only that
    non-monomiality alone does not force 2. H2 is one instance where cancellation does.
  - *Fix:* replace the clause with that statement, for example: "so non-monomiality does not
    force 2 on that route; the readout there admits exactly the exponent in which the reachable
    states are normalised (column lemma), and a nonnegative non-monomial map can set it at 2".
    Make the same change in the DISPOSITIONS-r4 N1 row ("the nonnegative counterexample showing
    that interference on a reachable state is needed").
  - "An instance with a sign forces $p=2$" is true as an instance. "With cancellation" would
    name the operative feature, since G4(b) is signed and forces 1.

## Nits

1. **D-label collision.** The text cites "the reviewer's D1" (l.257), "reviewer check D2" (R3-N
   row) and "reviewer check D3" (R3-C row; l.326). These are `rv2_1059_checks.py`'s D1–D3. r4 now
   also has "r4 check D1" and "r4 D2", whose content differs: D1 is the dilation Gram check, not
   the column lemma. Write "rv2 D1", "rv2 D2" and "rv2 D3".
2. **BRIDGE r5 status.** The header says r5 (`78f1098e…91a4`) is "under review".
   REVIEW-UNIT1-r5 (`0ef5644f…8c76`, written before r4) gives ACCEPT WITH NITS. Its phase finding
   agrees with §0 item 2: the complex drive carries the phase, and the phase is independent of
   the layer flow only. Update the status line. The citations can stay pinned to r4, and no
   conclusion changes, since a draft ACCEPT is not `main` (§A.46 item 7).
3. **Owner record not cited (optional).** #1169 c.6741291498 (amaybaum, 2026-11-09T13:30:54Z) asks
   for a decision "whether #1059 and #868 need independent follow-up experiments rather than
   treating success on FI-1 as solving both", and for each dependency to carry its status, carrier
   and assumptions. r4 answers this in substance: FI-1 is necessary under named hypotheses and
   not sufficient (§0 item 2, §4.4, OQ-1–OQ-3). Citing it at OQ-2 or OQ-3 would connect the two.
4. **"BORN-SRC-1 C4 at $n=2$" (l.91).** C4 normalises the columns of the 3-4-5 rotation ⊕ 1, a
   3-state carrier (`src/914-bornsrc.txt`:331–333). The $n=2$ countercontrol is C1. Write "C1 at
   $n=2$; C4 at $n=3$".

## Checks performed

**1. r3 findings.**
- **B1 fixed.**
  - §3 *FI-1 and R3* now gives the dilation proof (A). The proof is correct: completeness makes
    the dilation an isometry, single-entry orthonormal columns occupy distinct (operator, row)
    positions, each block is a partial injection, and a partial injection extends to
    `permMatrix σ * diagonal d` with zeros allowed (SubstratumInterface.lean:75, read).
  - "1034" and "exhaustive over support" have 0 hits in r4. §8 describes E2(a) as vacuous and
    replaced.
  - *r4 D1 is non-vacuous.* It computes $V^\dagger V$ in exact Gaussian rationals and decides
    `IsMonomial` by search over $\sigma$. I checked the 63128-case count by hand:
    $\sum_{n,m\le3}(mn)^n4^n$.
  - I re-ran three single-line mutants, and each fails D1:
    - with the Gram test removed, the claim fails and both countercontrols drop to 0;
    - with a columns-only monomial decider, D0 fails and countercontrol (a) drops to 0;
    - with the non-unit value 1/2 removed from W, countercontrol (b) drops to 0.
  - Countercontrol (b) answers the r3 objection directly: the Gram test is not decided by
    positions.
  - *rv4 G2 checks the lemma on a wider class*: all columns over $\{0,1,i,3/5,4/5,-4/5\}$, not only
    single-entry ones, for $(n,m)\in\{(2,2),(2,3),(3,2)\}$. There are 23892 complete families
    with a non-monomial block, and each has a dilation column with $\ge2$ nonzero entries. Each
    of the 1128 single-entry complete families is blockwise monomial.
  - The DISPOSITIONS-r3 partial refusal is correct: a paired change record is provenance (§A.27).
- **N1: the writer's partial refusal is correct.** The r3 review's sentence, "linear dynamics on
  signed or complex amplitudes with H-RF$_p$ required on every reachable state also forces $p=2$,
  and unitarity then follows", is false:
  - H1 (re-run), a nonnegative map acting in a signed amplitude space, gives $p=1$;
  - rv4 G4(b) gives signed reachable states and $p=1$;
  - rv4 G4(a) at $q=2$ forces $p=2$ with a singular map, so unitarity does not follow.

  The Aaronson result cited for it is the every-vector form, not the reachable-state form. The
  "within H-LIN" scoping at §0 item 2 and in §3, "derives no exponent from OI" ("derives nothing":
  0 hits) and the NQ-1059 clause are applied. The replacement text overstates (B1).
- **Does the r3 review's F4 overreach in the same way? Yes.**
  - F4's two computations are correct; rv4 G4(c) recomputes $\sum|M_p^2e_1|^p=2^{p-2}$.
  - Its docstring's general conclusion is false: "with linear dynamics and the readout required
    on every reachable state, the exponent is fixed by the amplitude field and interference,
    unitarity being an output". G4(a) fixes 2 without interference and with a non-unitary map,
    and fixes 3 the same way. G4(b) fixes 1 with signed amplitudes.
  - r4's "interference … needed" (B1(b)) is the mirror of the same overreach.
- **N2 fixed.** The word-diff at glossary:21 matches the new F-e wording exactly: the first
  sentence and "What remains is operational:" are unchanged, and the tail was rewritten without
  the exponent item. glossary:21 and FULL:6604 are byte-identical (`cmp`).
- **N3 fixed.** GR:260 reads "is not shown sufficient", and the quotation is now verbatim.
  Non-sufficiency is cited to r3 E4 (re-run).
- **N4 fixed, with the writer's correction of the review right.** `bridge/BRIDGE-UNIT1.md` hashes
  to `78f1098e…91a4`, and its header reads "Revision r5". r4 is at `bridge/r4/` (`4e97610d…85e2`).
  The r3 review's `9d40d6f3…5c0a` is wrong.
- **N5 fixed.** QP, GR, SM, Substratum and Structure are expanded, and each path exists at
  `fd539e15`.
- **N6 fixed** (l.695).
- **N7 fixed, and supported on `main` at every citation.**
  - GR:270 contains `configurationLevel_not_layerFlowExecutable` and
    `obs_not_layerFlowExecutable`, with "the theory the read and write access generates …
    executes no layer flow".
  - GR:260 states that the substratum's interventions are monomial, and that the class "with
    nothing added, is closed under composition, coarse-graining, and ancilla blocks …".
  - In StructuralClosure.lean, `def substratumClass … IsMonomial K` is at line 180 and
    `theorem substratumClass_structurallyClosed` is at line 316.
  - C5Discovery.lean's header contains "Not claimed: that any candidate is a C5; that the
    polarization map is available to the observer".
  - StateMixingCoupling.lean's header contains "the datum is a postulate, and nothing here
    derives it", and `MixR` is the closure of the stated access and the datum.
  - `gateFlow_not_monomial` is at CoherentContinuumSource.lean:74, and `hadamard_not_monomial` is
    at C5Discovery.lean:162.
  - The inference is valid. The stated access generates within a structurally closed monomial
    class, and a unitary channel's Kraus operators are all proportional to its unitary, so no
    non-monomial unitary (Hadamard, intermediate-time layer-flow point, real rotation) is
    available from it. The draft citation is gone.

**2. Untraced changes.** The word-diff of r3 against r4 shows no change outside the dispositions
(B1, N1–N7, U1–U3). U2 is verified: P1, P2, r2, r3 and rv3 re-run byte-identically.

**3. Full re-read.**
- *Probes.* All eight earlier scripts re-run under `python3 -I` from a scratch directory: P1, P2,
  r2, r3, r4, rv, rv2 and rv3. Each exits 0 and is byte-identical to its recorded `.out`.
  rv4 G1 re-checks the column lemma independently on $\ell^1$, $\ell^2$ and $\ell^3$ columns.
- *Three columns.* No column-(iii) entry is cited for column (ii). Every column-(ii) "no" names
  its posit. The new paragraph keeps column (ii) unchanged ("posited, not derived from OI").
- *Owner distinctions.*
  - Configuration versus encoded carriers is kept: §3 *FI-1 and R3*, R4, §4.3 and §4.5.
  - Available versus derived is kept: §4.1 gap 1, now on `main`, and NQ-1059's positive branch.
  - Mixing versus the full rules is kept: §0 item 2, §4.4 and §5.
  - Generating state mixing is kept separate from deriving the exponent throughout. The 2 is
    attributed to the posited quadratic normalisation within H-LIN and, without it, to the
    posited linear kinematics. B1(a) asks that this attribution be stated for non-square
    operations too, where the 2 comes from completeness.
- *Scope.* The negatives are scoped to the search and the stated access. The No branch of
  NQ-1059 is not a no-go beyond H-LIN or beyond record-based selection.
- *Register.* No caps emphasis, reader instruction or self-assessment was found (§A.32–§A.33
  bind `papers/` only). The header states no adoption or authorization, consistent with
  #1059 c.6740117293.
