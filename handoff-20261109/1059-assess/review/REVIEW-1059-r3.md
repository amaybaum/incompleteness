# Review of ASSESS-1059 r3 (BORN-SEL, #1059): fresh, independent, paper-only

**Model-written (Claude Code subagent, 2026-11-09). WIP / UNVERIFIED.** This review adopts nothing,
edits no record and authorizes nothing. It made no git or GitHub write; the only GitHub access was
a read of #1169 c.6740778880.

- **Under review.** `ASSESS-1059.md` r3, sha256
  `85fd3d4b1d39e4addb63edac11761908f6001286ec34e8a276b6b2999d328465` (verified before reading),
  with `DISPOSITIONS-r3.md` (`beef3bd3…de68c`), `r2/ASSESS-1059.md` (`f99a4c3b…20d2`, verified),
  `review/REVIEW-1059-r2.md` (`a262ad4f…9710`, verified) and `probes/` (P1 `82361ef8…a3d2`, P2
  `90efad3b…a94c`, r2 `3f32e79f…1091`, r3 `34db77f2…e758`, all verified).
- **Sources.** Repository lines read with `git show fd539e15:<path>` after `git fetch origin main`
  (`fd539e15` = `fd539e150759a6ea51ab279aeeac80fc06050ade`). Drafts read as hypotheses only:
  BRIDGE r4 (`bridge/r4/BRIDGE-UNIT1.md`, `4e97610d…85e2`, verified) and REVIEW-UNIT1-r4
  (`e489fc19…2bc7`, verified). BORN-SRC-1 from `src/914-bornsrc.txt`.
- **Reviewer probe.** `review/rv3_1059_checks.py` (sha256
  `b0d99862690439f7d081ce4e70b188d47a406943e8597b185066e476663d0151`), output
  `review/rv3_1059_checks.out`
  (`d5895d993b79684717f6fc393840d86fbc2719f9641c97ecbc8f93c03861165a`), exit 0 under
  `python3 -I`, run from `/tmp`. It imports nothing earlier and computes on generic columns,
  matrices, Kraus families and Lie algebras only (checks F1–F5, docstring). Mutation-tested: six
  single-line mutants (wrong exponent in F1; completeness dropped in F2; the phase factor dropped
  and the real Lie dimension set to 8 in F3; the sign removed in F4; a cube root in F5) each turn
  the affected check to FAIL.

## Verdict: REVISE (bounded)

The central conclusion stands, and r3's new material is mathematically correct: nothing on `main`,
and no draft read, derives exponent 2 or the Born law from independently justified OI principles.
The column lemma, the Kraus/dilation lemma, the instrument instances and the phase/drive identities
all check exactly and independently (F1–F3, F5). All three r2 blockers and all eight r2 nits are
fixed. One blocker remains, of the verification-layer kind: the dilation lemma is cited as
supported by an "exhaustive" computation that is vacuous. The lemma is true and the text already
contains its proof, so the fix is relabelling or replacing the check. A delta review of the
passages named under B1 and nits N1–N3 is enough.

## Blocker

**B1. E2(a), cited as an exhaustive check of the dilation lemma, is vacuous.**
- *Where.* §3 *FI-1 and R3*, second bullet ("r3 E2, exhaustive over support patterns,
  $n,m\le3$"); §0 item 2 ("r3 check E2"); §8 probe entry ("exhaustive over 1034 support
  patterns"); DISPOSITIONS nit-2 row and U1.
- *What the code does.* In `r3_exponent_source.py`, E2(a) defines
  `orthonormal = all(assign[j] != assign[jj] …)` and `injective = len(set(assign)) == n` and
  asserts they are equal. These are the same predicate. Its per-block row check
  (`len(rows) == len(set(rows))`) follows from distinct positions. No inner product, Gram matrix
  or monomiality test is computed, so e2a is true on every branch. The only non-trivial line is
  the pattern count. The "inverted orthogonality" mutant fails only because it negates one copy of
  the predicate.
- *Rule.* Code Review Rules, "Exactness and controls": a computational verdict is invalid if its
  control is vacuous or reproduces the claimed formula. "Keep verification layers distinct."
- *Status of the lemma.* It is true. The text's own sentence is a complete proof (A): orthonormal
  single-entry columns sit at distinct (operator, row) positions, so each Kraus block has at most
  one nonzero per row and per column, which is the kernel's `IsMonomial` shape
  (`permMatrix σ * diagonal d`, zeros allowed; SubstratumInterface.lean:75). A non-vacuous check
  confirms it: F2 builds every single-entry dilation pattern for $n\le3$, $m\le2$ (266 patterns)
  with phase values, *computes* the Gram matrix, decides `IsMonomial` of each block by brute force
  over $(\sigma,d)$, and finds Gram $=1$ ⇒ every block monomial. Its countercontrol finds
  single-entry patterns with Gram $\ne1$ that have non-monomial blocks, so completeness carries the
  argument. Exact Cayley isometries cut into non-monomial blocks have a dilation column with
  $\ge2$ nonzero entries.
- *Fix.* Cite the dilation lemma as A (the written argument). Either describe E2(a) as encoding
  the argument's case split and not as a verification, or replace it with a computed check of
  F2's kind. Drop "exhaustive over 1034 support patterns" as support in §3, §8 and the
  dispositions. E2(b) (the instruments) and E2(c) (the non-contraction control) are genuine and
  can stay as X.

## Nits

1. **The attribution of the 2 holds relative to H-LIN.** R3-C is correctly a consistency
   condition between two posits *as formulated*: H-LIN posits unitarity, so every visited column
   is already $\ell^2$-normalised, and H-RF$_p$ can only agree at $p=2$ (F1: such a column has
   exactly one exponent, existence and uniqueness). The general sentences go further: "the 2 is
   the exponent of the unitary (quadratic) invariant posited in H-LIN, not of H-RF$_p$" (§3),
   "H-RF$_p$ supplies only the power form" and "derives nothing" (§0 item 2). If unitarity is not
   posited, linear dynamics on signed or complex amplitudes with H-RF$_p$ required on every
   reachable state also forces $p=2$, and unitarity then follows. F4 checks this exactly:
   $M_p=2^{-1/p}\bigl(\begin{smallmatrix}1&-1\\1&1\end{smallmatrix}\bigr)$ has $\ell^p$ columns for
   every $p$, while $M_p^2e_1$ is normalised only at $p=2$; the nonnegative analogue forces $p=1$.
   This is the Aaronson $p$-norm result the unit already cites (BORN-SRC-1 C2). The column-(ii)
   verdicts do not change: the 2 is then fixed by the complex linear kinematics that Main:218
   takes as given. Fixes:
   - write "within H-LIN" at those three sites, with one sentence on this alternative;
   - replace "derives nothing" with "derives no exponent from OI";
   - in NQ-1059's clause, add the case where unitarity is forced by the operation's linearity
     together with H-RF$_p$; it falls under "taken with the complex matrix kinematics".
2. **F-e edit history (the writer's correction of the r2 review).** The line was edited between
   `02009693` and `fd539e15`, as r3 says. But "both sentences are unchanged" is not right. The first
   sentence and the opening clause "What remains is operational" are unchanged. The second
   sentence's tail was rewritten: "which of them the substratum supplies" became "the substratum's
   stated interventions do not supply one of them, full reversible control; whether an extended OI
   mechanism can supply it, which of the others …". The r2 review's "leaves the sentence intact"
   referred to the first sentence and was correct. F-e's finding stands, since the rewritten
   sentence still omits the exponent item. Glossary:21 and FULL:6604 are byte-identical at
   `fd539e15`. Fix: "the first sentence and the clause 'What remains is operational' are
   unchanged; the second sentence's tail was rewritten, still without the exponent item" (§6 F-e
   and DISPOSITIONS).
3. **GR:260 says "not shown sufficient".** §0 item 2 cites "(GR:260)" for "necessary for the phase
   and not sufficient". GR:260 supports necessity and says only "is not shown sufficient". Non-sufficiency is
   established by r3 E4's real rotation (also F3; REVIEW-UNIT1-r4 R2(e)). Cite E4 for that half.
4. **BRIDGE path.** `scratchpad/bridge/BRIDGE-UNIT1.md` now holds r5 (`9d40d6f3…5c0a`). r4
   (`4e97610d…85e2`) is at `bridge/r4/BRIDGE-UNIT1.md`. The hash pin is right; the path should name
   `bridge/r4/`.
5. **QP is undefined.** r3 reads QP first-hand and cites it on seven lines, but the source-snapshot
   list does not expand it. QP is
   `verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md`
   (BRIDGE's definition, checked at `fd539e15`). GR, SM, Substratum and Structure could be expanded
   in the same line.
6. **§8 stale sentence.** "Lean files were read only at EQ's lines" contradicts the r3 kernel
   reads listed a few lines above it (SubstratumInterface:75, CoherentContinuumSource:74,
   C5Discovery:59/:162, LiftAudit:660, the StateMixingCoupling header). Restate it as "Lean files
   were read only at the lines listed".
7. **§4.1 negative rests on a draft alone.** "In the records read, none is an available operation
   of the stated access (BRIDGE §5.1 [D])" contradicts the header's rule that no conclusion rests
   on drafts alone. `main` supports it directly:
   - GR:270 (`configurationLevel_not_layerFlowExecutable`, `obs_not_layerFlowExecutable`) for the
     intermediate-time layer flows;
   - C5Discovery.lean's header ("Not claimed: … that the polarization map is available to the
     observer") for the Hadamard;
   - the StateMixingCoupling header for the postulated coupling.

   Cite these.

## Checks performed

**1. r2 findings, each against its source at `fd539e15`.**
- **B1 fixed.**
  - (i) The column lemma is restated for columns with $\ge2$ entries of modulus in $(0,1)$, with
    the $\ell^2/\ell^1/\ell^3$ cases. The 2 is attributed to H-LIN's posited unitarity at every
    site named in the dispositions. A grep for "posited form" and "by hand" finds 0 hits.
  - (ii) R3-N's last column now gives the dilation reason and the √-insertion reason.
  - (iii) The condition paragraph in §3, §5 and §0 item 5 is present.
- **QP correction verified.** "A uniform unknown supplied by a ready cell enters as coarse-grained
  Kraus operators `2^{−k/2} P_σ`" spans QP:856–857. QP:855 is "configuration basis." The writer is
  right. BRIDGE r4 §5.1 *Position* (d) cites "QP:855's", as U6 says. F5 confirms the
  outcome-table identity: amplitudes $2^{-k/2}$ give the uniform table $2^{-k}$ and are admissible
  only at $p=2$.
- **B2 fixed.**
  - The scoped form appears at all seven sites.
  - Grep for "necessary prerequisite" and "lacks a necessary" finds 0 hits.
  - R3-N column (ii) separates the unitary members from registrations and the weighted Kraus
    operators.
  - GR:260 ("monomial observable operators, a permutation of a diagonal") and `IsMonomial` read as
    cited.
- **B3 fixed.** R4 column (ii) and §4.5 (a-gen) use the reviewer's wording. Grep for "dense family
  exists" finds 0 hits.
- **Nits 1–8 fixed.**
  - Nit 1: the hashes are right, but the path has gone stale again with BRIDGE r5 (N4).
  - Nit 2: verified below.
  - Nit 3: fixed, with the edit-history correction half right (N2).
  - Nits 4–6: verified at Main:566, Main:584, CoherentContinuumSource:74, C5Discovery:162 and the
    StateMixingCoupling header (line 7).
  - Nit 7: verified. Main:218 and review 9(i) (`src/914-bornsrc.txt`:331–333) are quoted
    verbatim, and Main:580 is kept for the B10 role.
  - Nit 8: verified. BRIDGE r4:470 reads "'Supplies' in FI-1 means 'makes available …'".

**2. New material.**
- **Column lemma.** Correct. Every column with $\ge2$ nonzero entries of modulus in $(0,1)$ has
  exactly one exponent $p^*\in(0,\infty)$, since $h(0^+)=\#\text{nonzero}-1>0$, $h\to-1$ and
  $h'<0$. Under unrenormalised H-RF$_p$ it admits only $p^*$. F1 checks this exactly on $\ell^1$,
  $\ell^2$, $\ell^3$ and $\ell^{1/2}$ columns, and on $(1/2,1/3)$, whose root lies in $(1/2,1)$.
  The doubly stochastic case is right.
- **Dilation lemma (E2).** True, with a valid written proof in the text. The computational support
  cited for it is vacuous (B1).
- **Kraus-family lemma (nit 2).** Verified.
  - $\{|0\rangle\langle+|,|1\rangle\langle-|\}$ and $\{|0\rangle\langle+|,|0\rangle\langle-|\}$ are
    complete and non-monomial, and their outcome tables are admissible only at $p=2$.
  - The second instance is the row case: $|0\rangle\langle+|$ has monomial columns, yet its
    dilation column has two entries.
  - Unscaled $K$ has $K^\dagger K$ eigenvalue 2, so it is not a contraction.
- **R3-C as a consistency condition between two posits.** Correct as formulated. The general
  attribution needs "within H-LIN" (N1).

**3. Untraced changes.**
- U1 verified (B1 for its support).
- U2: the probe re-runs byte-identically; E1, E2(b), E2(c), E3 and E4 are genuine.
- U3: OQ-3's quotation matches #1169 c.6740778880 (amaybaum, 2026-11-09T13:05:46Z), as does the
  header's verbatim text.
- U4: the clause is correct and adds no premise; see N1 for the third case.
- U5 verified (N7).
- U6 verified (QP:846–877 read).
- U7 verified (N6).

A word-diff of r2 against r3 shows no change outside the dispositions.

**4. Phase/drive correction.**
- §0 item 2 and OQ-3 state the correction as directed. The complex drive carries the phase. The
  phase is kernel-independent of the layer flow only (`obligations_independent`, C5Discovery:59,
  `Fin 2`, both directions). The driven-transition form folds the phase obligation into mixing,
  to be met by the complex drive and not by a real rotation.
- Grep for "for free", "no phase input", "dispens" and "supplied together" finds 0 hits.
- `gateFlow` (LiftAudit:47) is `unit (permMat σ) t` = $1+(e^{i\pi t}-1)(1-P)/2$
  (SecondOrderCircuit:356). `gateFlow_isolation` (LiftAudit:660) is a diagonal phase times gate
  flows equal to the transition flow at angle $\pi t$.
- F3, built independently from that definition, confirms the following:
  - $e^{-i\theta X}=e^{-i\theta}G(2\theta/\pi)\,{\rm diag}(1,1,e^{i\theta})$;
  - $e^{-i\pi X/2}\,{\rm swap}=-i\,{\rm diag}(1,1,i)$;
  - $G(t)$ fixes the all-ones ray at every $t$, while the drive moves it at $\theta=\pi/3,\pi/2,\pi$
    and not at $2\pi$;
  - the real rotation moves the ray, and the Lie algebras have dimension 3 against 8.
- GR:250's "No phase operation enters" reads as a statement about the repertoire.

**5. Full re-read.**
- All six earlier scripts (P1, P2, r2, r3, rv, rv2) re-run under `python3 -I` from `/tmp`: exit 0,
  outputs byte-identical to the recorded `.out` files.
- Kernel identifiers confirmed at `fd539e15`: `exists_nonMonomial_of_layerFlowExecutable`
  (ExecSource:52), `polarizedTheoryC_not_qm` (PolarizationClosure:620),
  `bijectiveOperator_monomial`/`phaseOperator_monomial` (SubstratumInterface:91/:94),
  `invariance_does_not_select` (CanonicalMeasure:242), `complete_passive_iff_commutative`
  (CentralObservation:620), `ensembleDetermined_of_transitive` (StochasticInterface:38).
- `git grep -iE 'frame.?function|gleason|busch'` over the Lean trees finds nothing, which is
  consistent with R5.
- Main:20, 56, 218, 226, 288, 351, 362, 552–556, 566, 580, 584, 590, 648 and 726 read as quoted.
- **Three columns.** Column (iii) is never cited for column (ii), and no posit is a column-(ii)
  "yes".
- **Three distinctions.** Configuration vs encoded carriers is kept, including R4 and §4.5.
  Available vs derived is kept (§4.1 gap 1; NQ-1059's positive branch). Coherent mixing vs the full
  rules is kept (§0 item 2, §4.4, §5).
- **Scope.** The negatives are scoped to the search (N7 aside). The No branch is not a no-go
  beyond H-LIN or beyond record-based selection.
- **Register.** No caps emphasis, reader instruction or self-assessment found (§A.32–§A.33 bind
  `papers/` only).
