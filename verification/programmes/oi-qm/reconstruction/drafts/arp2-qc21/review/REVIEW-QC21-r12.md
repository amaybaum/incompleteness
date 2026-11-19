# Confirming check: Q-C2-1 r12 (ARP-2-QC21)

**Reviewer.** The same independent model reviewer, 2026-11-09. Read-only. Inputs:
- preregistration `38c27d3a…`;
- PLAN `7560589b…`;
- DESIGN-DS `d887d839…`;
- `review/proofs/REVIEW-LEMMA-P.md` `07170453…`;
- `review/proofs/REVIEW-CONE.md` `07bc8fd7…`;
- the two certificates `e6719947…` (`K = 1`) and `f24a68d9…` (`K = 2`).

All were verified and diffed against `r11b/`.

## Verdict: **ACCEPT-WITH-NITS**

**The diff contains only the listed changes:**
- the r12 status line;
- the decisions-table row;
- hazard 7, made conditional on STAB;
- the `STAB(K)` field;
- *Proof reviews*, with the verdicts quoted and a new withholding table;
- the withdrawal of r6's `arccos(3/5)` sentence;
- the CC-NAT row;
- STAB-FALSE and STAB-TRUE, with their fixture-mode entries;
- the invariant row;
- in DESIGN-DS: LP-1's wording, the STAB-conditioned "What can be found" and R1, and Lemma P's label in §6 and §7;
- PLAN §18.

**Each change is faithful to the reviews.**
- The quoted verdicts are verbatim. That covers Lemma P's "PROVED … survives … conditional on Theorem C(ii) … and on
  the link hypotheses L1–L3", and the cone review's "PROVED UNDER STATED EXTRA HYPOTHESES … The missing hypothesis is
  STAB … it is a GAP … Not established …".
- L1–L3 are summarized correctly.
- LP-1 is stated as the review states it: `conv R(Q) = O` together with `R(πQ) ⊆ O`, with `O = conv R(L)` "neither
  needed nor sufficient".
- Hazard 7, the ENC-G sentence and R1's scope sentence are conditioned on `STAB(K)`, exactly as the cone review's fix
  asks.
- The `arccos(3/5)` withdrawal matches the review's table: refuted at `K = 1, 2` with VAL and `K = 3` without VAL, in
  the abstract class; open for gadget rounds at `K = 6, 12`.
- The "unaffected" column matches the review's §6: W-CL's computation, the C tokens, C-35 and the rational-reach
  arithmetic.

**The CC-NAT edit is justified.**
- The frozen withholding table removed CC-NAT's gating only if Lemma P's review failed.
- Lemma P's review answers "Yes" to CC-NAT's reliance (§6), and the cone argument is not involved, because Lemma P's
  O_h spectra need no STAB.
- So CC-NAT keeps its gating role, labelled conditional on Theorem C(ii) and L1–L3.

**STAB-FALSE and STAB-TRUE are well defined and have teeth.**
- STAB-FALSE uses the review's exact, pinned certificates. It expects `STAB = false` with HC, CONS and VAL holding and
  W-CL firing on `λ² − (6/5)λ + 1`, as the review states, and it expects the bound not to be printed.
- STAB-TRUE expects `STAB = true` on a map that leaves the seven QA laws fixed.
- Together they fail any STAB field stuck at one value, and any bound printed without STAB.

**STAB never gates.** `decide-c`, `decide-levels` and the token rules are unchanged. The field is declared "No token
and no Level reads it", and it affects only whether the note prints the "orders 3 or 6" bound.

## Nits (non-blocking)

- **r12-N1.** STAB-TRUE's fixture is "the idle (zero-tick) round". The idle round is also ABL's zero-tick ablation,
  which is a decisive family built through `s_decisive`, so in fixture mode the guard would refuse it.
  - Specify STAB-TRUE's input as the **supplied identity map** on the seven QA law vectors, computed outside
    `DECISIVE_BUILDERS`.
  - Similarly, state how STAB-FALSE reconstructs its orbit from each certificate: which field is the branch matrix, and
    which laws form `O_0`. The `K = 1` certificate's keys are `G`, `P`, `beta` and `q`; the `K = 2` certificate's are
    `B`, `K` and `q`.
- **r12-N2.** CC-NAT's route to failure: add "L1–L3", as Lemma P's review §6 recommends ("A red CC-NAT then points at
  Theorem C(ii), L1–L3, or …"). "A failure of Lemma P" may be dropped, though keeping it is harmless.
- **r12-N3.** Add a C-IFACE static rule that `decide-c` and `decide-levels` do not reference `STAB`. This makes "STAB
  never gates" mechanical.

## What remains before `F`

1. The nits r12-N1 to N3. They are text-level, and no further review cycle is needed beyond precondition 5's review of
   the filled control plane.
2. **The `PENDING` fields:**
   - the record-directory date and the governed-paths digest;
   - the REACHABLE path and blob;
   - the benchmark;
   - the design-run anchors and records, the stress generator and seeds, the budgets and the timeout-test count;
   - `T0`;
   - the pins of `design-run.json`, `stress.json` and `gate-tests.json`;
   - the activity API's documented retention.
3. **D9(a).** Land REACHABLE r3 and DESIGN-DS as paper records on `main` before `D`, pinned by blob. Re-confirm `D`.
4. **The scripts.** `qc21_check.py` and `controls.py` with self-tests, including STAB-FALSE and STAB-TRUE. Then the
   design and confirmation runs, and C.7's gate tests, GT-ACT on its non-recorded branch included.
5. **The owner's freeze commitments, recorded:**
   - no run, log or artifact deleted until `Q`;
   - ratification at `E`;
   - no force-move or deletion of recorded branches;
   - after `Q`, no push to, deletion of or re-creation of the round branch.
6. **The round PR.** Open it from `D` with every `PENDING` field filled. Then precondition 5's independent review of
   the filled control plane and the scripts' blobs, with no open blocking finding.
7. **The freeze.** The `F` dispatch with its approval entry and green result, then the designation request.
