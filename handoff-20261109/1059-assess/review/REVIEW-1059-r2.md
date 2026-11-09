# Review of ASSESS-1059 r2 (BORN-SEL, #1059): fresh, independent, paper-only

**Model-written (Claude Code subagent, 2026-11-09). WIP / UNVERIFIED.** This review adopts nothing,
edits no record and authorizes nothing. It made no git or GitHub write.

- **Under review.** `ASSESS-1059.md` r2, sha256
  `f99a4c3b2196bd035295b4bbff341459abb0f0c23a802621e4b26ba10b8120d2` (verified before reading),
  with `DISPOSITIONS-r2.md`, `r1/ASSESS-1059.md` (`d5b314af…d931`), `review/REVIEW-1059.md`
  (`8cbfe227…7446`) and `probes/` (P1 `82361ef8…a3d2`, P2 `90efad3b…a94c`, r2 `3f32e79f…1091`).
- **Authorization.** #1059 c.6740117293, paper-only, exact generic checks only. Owner direction
  #1169 c.6740778880: generating state mixing does not by itself establish the Born exponent.
- **Sources.** All repository lines read with `git show fd539e15:<path>` after
  `git fetch origin main`. BORN-SRC-1 from the saved #914 text (`src/914-bornsrc.txt`). Drafts read
  as hypotheses only: BRIDGE r3 (`bridge/r3/BRIDGE-UNIT1.md`) and its review
  `REVIEW-UNIT1-r3.md`.
- **Reviewer probe.** `review/rv2_1059_checks.py` (sha256
  `a13582b236876c1e69698cba7f7316e167dd701b22a02b50c0a3898fbbffd304`), output
  `review/rv2_1059_checks.out` (`2d2be05e72c4935f796ba6facf2da44e13f07151a1056a49cb4fe976ffe13861`),
  exit 0, `python3 -I`. It imports no earlier script and computes on generic matrices and columns
  only. Checks D1–D4 are described in its docstring; the helper was mutation-tested (wrong exponent
  and monomial column both return false).

## Verdict: REVISE (bounded)

The central conclusion stands and is better separated than in r1: nothing on `main`, and no draft
read, derives exponent 2 or the Born law from independently justified OI principles, and state
mixing is presented as necessary under stated hypotheses and not sufficient. All thirteen r1
findings are fixed. The new unitary scoping (U1) is right in its result but wrong in its stated
reason, and that reason, applied consistently, changes where the exponent 2 comes from in R3-C.
Two further cells state a conditional necessity as unconditional, and two cells drop the
configuration/encoded distinction the owner asked to keep. All fixes are wording or scope; none
needs new computation beyond what D1–D4 already exhibit.

## Blockers

**B1. The value 2 in R3-C comes from H-LIN's posited unitarity, not from "the posited form"; U1's
reason for excluding Kraus families applies to unitaries verbatim.**
- Under unrenormalised H-RF$_p$, a column with at least two nonzero entries of modulus in $(0,1)$
  admits exactly one $p$: the exponent of its own normalisation. A unitary column forces $p=2$, a
  stochastic column $(1/2,1/2)$ forces $p=1$, an $\ell^3$ column forces $p=3$; a doubly stochastic
  non-monomial matrix is admissible only at $p=1$ (D1, exact). H-RF$_p$ is a power family with no
  preferred exponent, so "what forces $p=2$ under them is the posited form" (§4.4, first bullet;
  also §0 item 2, R3-C column (ii), §4.5) misattributes it. The 2 enters through H-LIN's posited
  unitary (quadratic) kinematics, which Main:218 takes as given.
- The R3-N scope note says the Kraus weights "are fixed by the quadratic completeness
  $\sum K^\dagger K=1$, which puts the exponent in by hand". Unitarity $U^\dagger U=1$ is the
  one-operator case of the same relation. A weighted monomial Kraus family is the column lemma
  applied to its Stinespring isometry, whose columns are non-monomial unit vectors (D2, exact). So
  that reason, as stated, voids R3-C too.
- What does distinguish the corpus's Kraus case is that QP:855 (on `main`) defines the amplitudes
  $2^{-k/2}$ as square roots of counting weights $2^{-k}$ ("A uniform unknown supplied by a ready
  cell enters as coarse-grained Kraus operators `2^{−k/2} P_σ`"). Normalisation at $p=2$ then
  returns the inserted counting law (D4). That is the √-insertion circularity of BORN-SRC-1 review
  9(ii), and its numbers are N2's, measure (b), as §4.3 already says.
- **Fix.** (i) State that a non-monomial column fixes $p$ at the exponent of its own normalisation,
  so in R3-C the value 2 is supplied by H-LIN's unitarity; R3-C is a consistency condition between
  two posits (H-LIN, H-RF$_p$). (ii) Replace the Kraus reason with: the family is R3-C on its
  dilation, and at QP:855 its amplitudes are square roots of counting weights, so its $p=2$ is
  circular. (iii) Optionally, NQ-1059's positive branch would bear on the exponent only if the
  exhibited operation's quadratic invariant is itself native rather than posited; say so, without
  adding a premise.

**B2. "A non-monomial admissible unitary is necessary for (a)" is stated outside the hypotheses
that make it true (conditional → unconditional).**
- R3-N proves: under H-LIN ∧ H-RF$_p$ (unitary operations), monomial operations leave every $p$
  fitting every record. Its contrapositive is a necessary condition for *record discrimination
  within H-LIN ∧ H-RF$_p$*.
- §4.4 first bullet and §4.5's (a-pow) row list "Necessary: H-LIN, H-RF$_p$ (both posited) and a
  non-monomial admissible unitary". H-LIN and H-RF$_p$ are the hypotheses under which the necessity
  holds, not necessary conditions of (a-pow). Outside H-LIN, r2's own K2 (and D2) shows monomial
  non-unitary families discriminate $p$, and QP:855 places such a family in the stated access. A
  selection of $p$ need not be record-based at all.
- OQ-1 asks the owner to record the non-monomial admissible unitary "as a *necessary* prerequisite
  of (a)", and §5's *No* branch says "(a-pow) lacks a necessary condition". Both drop the scope.
- R3-N's column (ii) adds "The antecedent itself holds for the stated interventions on the
  configuration carrier". GR:260's observable operators are "a permutation of a diagonal",
  registrations and QP:855's weighted Kraus operators included, so the stated interventions are
  monomial but not all phased permutations, and R3-N's conclusion does not cover the non-unitary
  ones.
- **Fix.** Everywhere: "Under H-LIN ∧ H-RF$_p$, a non-monomial admissible unitary in the read basis
  is necessary for any record to discriminate $p$ (R3-N)". Restate OQ-1 and §5 accordingly. In R3-N
  column (ii), say the antecedent holds for the unitary members of the stated access, and that the
  non-unitary monomial members are outside H-LIN (B1(ii) gives their status).

**B3. Two cells generalise FI-1 from the configuration carrier to every carrier.**
- R4 column (ii): "No native dense family exists, since even FI-1 is not supplied". §4.5 (a-gen):
  "A native dense family on $n\ge3$ (which needs FI-1)".
- FI-1 is posed on the configuration carrier; r2's own §1 and §3 record that non-monomial encoded
  maps arise without FI-1 (BRIDGE §5.1 [D], QP:79–98, QP:846–877). So "needs FI-1" holds on the
  configuration carrier only. On encoded carriers the records read give finite groups (stabilizer
  scope; MECH-2's $A_4\wr S_n$, cited through BRIDGE [D]), so no dense family is *recorded*, which
  is a search-scoped negative, not a consequence of FI-1.
- "No native dense family exists" is also an unscoped existence negative; §8 scopes it to the
  search, but the cell gives a logical reason that does not reach encoded carriers.
- **Fix.** R4 (ii): "No native dense family is recorded on `main` (§8): on the configuration
  carrier one would need FI-1, which the stated access does not supply; on encoded carriers the
  recorded operations form finite groups." §4.5 (a-gen): "(on the configuration carrier, which
  needs FI-1)".

## Nits

1. **BRIDGE r3 hash.** `a5d7aad1…78c1` matches no file. BRIDGE r3 is `ee1c83c0…8219`
   (`bridge/r3/`; REVIEW-UNIT1-r3 and DISPOSITIONS-UNIT1-r4 agree); its content cited here (FI-1,
   the $K$ matrix, *Position* (c)–(d), the §6 row) is present there. BRIDGE r3 is now reviewed
   REVISE and r4 exists; update "pending a fresh review". SHM r5 now lives at `qphen/r5/` (the
   path cited holds a later file, `67b3f5b5…`).
2. **R3-C's unitary scope is sufficient, not necessary.** "FI-1 would have to be supplied by a
   unitary for R3-C to apply" holds inside H-LIN only. Any operation with a visited 2-normalised
   column with two nonzero entries forces $p=2$: e.g. the instrument $\{|0\rangle\langle+|,
   |1\rangle\langle-|\}$, whose operators are non-monomial (D3). Also, K1's
   $K=\begin{pmatrix}1&1\\0&0\end{pmatrix}$ is not a contraction ($K^\dagger K$ has eigenvalue 2),
   so no instrument contains it; it shows the predicate gap and nothing about admissible
   operations.
3. **F-e verified, with its locus sharpened.** glossary:21's first sentence ("does not list a
   separate 'quadratic-exponent selector' … at that layer") matches Main:556 ("not an open choice
   … not a gap in the equivalence"). The contradiction is "What remains is operational", which
   omits the exponent-origin frontier item that Main:20, Main:226, Main:556 and ch18:34 keep, and
   which Main:556 says must not be conflated with the operational question. Add the mirror
   `book/The-Incompleteness-of-Observation-FULL.md:6604` (§A.14, §A.25). The finding is BORN-SRC-1
   F3 as sharpened by its review finding 4 ("unless 'that layer' is read narrowly"), unchanged at
   `fd539e15` (`git diff 02009693 fd539e15 -- book/glossary.md` leaves the sentence intact). Label
   it CONFIRMING, not new (DISPOSITIONS U5).
4. **Unscoped negatives.** §0 item 3, first bullet: "It is not an operation derived from OI or
   executable by the observer" → "no record read derives it as an operation the observer
   executes". §4.1: "Every other non-monomial route on `main` is two-mode (R8) or stabilizer-only"
   → "every other probability-outputting non-monomial route found (§8)"; `main` carries other
   non-monomial objects that output no probability (layer-flow intermediate points,
   `gateFlow_not_monomial`; the polarization candidate's Hadamard; the postulated coupling of
   `StateMixingCoupling.lean`).
5. **§0 item 3, second bullet.** "need weights that finite uniform resources cannot give" needs
   "exact": Main:566 and Main:584 realize quantum Bell statistics to finite accuracy with fixed
   bijections. §4.2 already says "Exact".
6. **H-Bell "independent" of FI-1** (§0 item 2, §4.2). The support shows one direction (the
   finite-accuracy realization needs no FI-1), and BRIDGE says only that "no source read derives
   either from the other". No kernel independence exists here, unlike phase/flow
   (`obligations_independent`). Say "beside FI-1, not after it; neither is derived from the other
   in the sources read".
7. **U2.** Replacing Main:580 is acceptable: Main:20, Main:226 and Main:288 carry "dictionary, not
   selected" in Main's own words. But Main:580 is not weak for what BORN-SRC-1 used it for (B10:
   the trace rule is programmed into the operational realization, $q_o={\rm Tr}\,\mathcal
   I_o(\tilde\rho)$); keep it as the operational-route instance or say why it is dropped.
   Quotation accuracy: review 9(i) reads "OI supplies it rather than sourcing it (B10; Main:580)";
   Main:218 reads "takes the complex matrix kinematics as given" (R6 quotes "taken as given").
8. **Two admissibility notions in §3 *FI-1 and R3*.** R3's "admissible" is membership of H-LIN's
   class with $p$-normalised readout; FI-1's is "made available by the stated access". The
   entailment "R3-N's condition entails FI-1" holds once R3's class is read as the operations the
   stated access makes available; say so.

## Checks performed

**r1 findings (each against its source at `fd539e15`).**
- **B1** fixed: R2 now states law-class independence of $p$, conditional on the normalisation
  restriction; "unselectable" is gone (grep); §3's closing paragraph matches.
- **B2** (i) renormalised reading excluded (K4; rv C3 re-run identical); (ii) preparation class in
  H-LIN, with the $(2^{-1/2},2^{-1/2})$ counterexample (K5); (iii) both hypotheses labelled
  *posited*, "supplied" gone from R3's column (ii) (grep), H-RF$_p$ kept in (a-pow)'s
  prerequisites; (iv) "in the read basis" throughout. The (a-pow) formulation is where B2 above
  applies.
- **B3** fixed: §0 item 3, §4.3, §0 item 5 scoped to (a-gen); the dyadic-point forcing stated.
- **B4** fixed: `484006b1` (2026-11-07) is an ancestor of `fd539e15`; Main:226 and Main:351 read as
  quoted; §3.1 is Main:208–262 and contains :226; Main:351 sits in the "Barandes route (§3.1)"
  column (Main:345).
- **B5** fixed (R9).
- **N1–N8** fixed: R3 split by antecedent; SHM r5 `a7206701…cc4d` and r4 `23ec1ef1…fd11` match;
  F-c blobs `b31d0549` / `1c077f62` differ only in the author-label line (`git diff`); P2 scoped to
  $n\le3$ with $g$ for all $n$; §4.5 (d) row restated as rv C6; "(St)" gone; F-a's per-cycle
  uniqueness (Main:56; `ensembleDetermined_of_transitive`, StochasticInterface:38); §8 names
  Main:684, ch18 §18.2 (:16, :34, :52) and glossary:21.

**Untraced changes.**
- **U1** independently verified, with B1 and nit 2 as the correction to its reasoning: $K$ is
  non-monomial with monomial columns (K1 re-run; D3); weighted monomial Kraus families normalise
  only at $p=2$ (K2 re-run; D2), equal to the column sum of their Stinespring isometry; for
  unitaries "some column has two nonzero entries" equals "non-monomial" (K3). R3-N needs the
  unitary scope; R3-C does not.
- **U2** verified (nit 7). **U3** GR:260 quote verified. **U4** Main:403–406, :566, :584 read;
  BRIDGE r3 *Position* (c) says "beside FI-1, not after it" (nit 6). **U5** see nit 3.
- Kernel identifiers verified at `fd539e15`: `exists_nonMonomial_of_layerFlowExecutable`
  (ExecSource:52), `obligations_independent` (C5Discovery:59), `polarizedTheoryC_not_qm`
  (PolarizationClosure:620), `gateFlow_not_monomial` (CoherentContinuumSource:74), `invariance_does_not_select`
  (CanonicalMeasure:242), `complete_passive_iff_commutative` (CentralObservation:620); EQ:99, 147,
  205, 227, 302, 462.

**Probes.** P1, P2, `r2_fi1_scope.py` and `rv_1059_checks.py` were re-run with `python3 -I` from
`/tmp`: all exit 0, all outputs byte-identical to the recorded `.out` files. Controls are not
vacuous (P1(c), P2(c)–(d), K4's non-root exponents, K2's phased-permutation control). K6's interval
enclosure is $[1.432495077833039546…]$, excluding 1. All are generic objects; none computes on an
OI mechanism.

**Separation and register.**
- Three columns: column (iii) is never cited for column (ii); posits are no longer column-(ii)
  "yes" (R9, F-a).
- Available vs derived: kept (§4.1 gap 1; §5 positive branch requires derivation and
  executability).
- Coherent mixing vs full rules: kept (§0 item 2, §4.4, §5).
- Configuration vs encoded carriers: kept in §1, §3, §4.3 and §5; broken at R4 (ii) and §4.5
  (B3).
- Negatives: scoped except B3 and nit 4.
- Register: no caps emphasis, reader-instruction or self-assessment found; §A.32–§A.33 bind
  `papers/` only.
