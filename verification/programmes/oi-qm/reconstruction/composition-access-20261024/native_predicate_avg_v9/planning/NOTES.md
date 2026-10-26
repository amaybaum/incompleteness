# Notes on the NP-AVG-1 draft plan

## Files read

Worktree of #912 at `2af1d5d5b5fff4375e9fe9460f892c680ae99f0c`, under
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/`
(blob ids at that head):

| file | blob | used for |
| --- | --- | --- |
| `README.md` | `0c0d8b25` | package table, replay commands, v8 pinned at `fc452ea8` |
| `REPORT.md` | `2f77fe2f` | contract (1); "Fresh resources" lines 57-69 (the G9 condition); fair-after-heralding toy lines 151-157 |
| `CURRENT-HANDOFF.md` | `ddc11410` | v6/v7/v8 summaries; v8 open branch lines 129-134 |
| `native_predicate_v8/PLAN.md` | `9f5e5bd1` (same at `631bec0c`, `fc452ea8`) | house structure; reduction lines 48-58; decision rule 111-122; controls 124-153 |
| `native_predicate_v8/REPORT.md` | `adcd75c9` | result and scope; pad/mixture branch lines 62-65 |
| `native_predicate_v8/checks.py` | `0a53c776` | geometry (69-84), backgrounds (171-182), J and A (314-325), law test (338-351), families (254-264) |
| `native_predicate_v8/result.json` | `9ef92ae4` | zero-background diagnostic, controls |
| `native_predicate_v8/mutants/run_mutants.py` | `91779b22` | mutant style |
| `native_predicate_v8/review/README.md` | `852dab8b` | review rounds |
| `composition_flag_v6/PLAN.md`, `REPORT.md` | `d0b569f2`, `b94a93a2` | phase map, law (REPORT lines 131-145), wrong-flag TV 1/8 (180-183), pad reuse (184-190) |
| `delayed_history_v7/PLAN.md`, `REPORT.md`, `checks.py` | `927fba6a`, `48bf6923`, `bfe91693` | factorization conditional on C0; exposed pre-tail bank (REPORT line 74); scaled port (checks.py 172-216) |
| `AGENTS.md` | `0fe9a4c5` (equals `main` at `52e2db40`) | rules |

v8 verification: `sha256sum -c SHA256SUMS` passes; the files listed there have
the same blobs at `fc452ea8` and at head; `python3 -I -B checks.py` (57 s)
reproduces `result.json` byte for byte. `fc452ea8` is an ancestor of
`2af1d5d5` but not of `main` (`52e2db40`).

On `main` (`52e2db40`):
- `native-y-continuation-20261024/transport_audit_v1/REPORT.md` (`4a5c2761`),
  lines 10-14 and 186-206: the cyclic counterexample, eight joint outputs of 64.
- `native-y-continuation-20261024/history_v11/REPORT.md` (`ed3a7131`), line
  141-142, and `review/REPORT.md` (`97f5ecb7`), lines 102-104: support 8 of 64
  for a read of a reserved bank triple with its later output.
- `verification/programmes/oi-qm/PROGRAMME.md` (`6590e274`), lines 40 and 634.
- `AGENTS.md` (`0fe9a4c5`): §A.31, §A.40-§A.44 and the Code Review Rules. The
  local checkout's copy (`9b83ff7c`, 2026-10-19) carries an older §A.42 and an
  extra §A.40 paragraph on `retention-tests`; the plan follows `main`'s copy.

PE-01: `.../ppe/repo/verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/PLAN.md`,
blob `3ca81a06` at `47a1f19b` (branch `research/oi-pseudoentropy-20261025`):
priors at lines 45-46, 56-57 and 70; observer memory fixed at 0 (lines
160-170); tables charged as state (181-183); relation to the B classes deferred
to PE-02 (210-212).

Issue #929: `ISSUE-929.md` was absent when work began. The body was read
through the GitHub API, and the file written later (sha256 `74a05798…`, 87
lines) agrees with it on the spot-checked lines (K2, K4, dependencies).

No new computation was run for this question; the only execution was v8's
replay.

## Places where #929 was interpreted

1. **"Averaged over π_bg".** This could mean the full Bayesian average (A) or
   averaging only over seeds licensed by the G9 condition (G). The plan
   computes the law in A and uses G, on seventeen frames, as F1b. The G9 text
   requires independence from "all non-seed variables used by the stage", so
   averaging over background in the carrier's own cones is not itself
   licensed.
2. **"Conditional-freshness certificate".** Split into F1a (against the
   carrier, exact), F1b (against every stage input, sampled frames) and F2
   (against later ports, exact).
3. **"Every later public port".** Taken as the declared ports of the contract
   (a scaled port, plus R's stream closure). Unrestricted later native reads
   would make every pad non-fresh by reversibility.
4. **Old ports.** #929 does not mention them, but v8's public record includes
   the eight old ports. v8 drops them only because N_L is constant given C0.
   Under averaging they must be modelled, so the plan adds v7's scaled port.
5. **"Support cap".** Read as a cap on the residual binary support enumerated
   after the exact reductions (27 bits). Read sets larger than k are outside
   the class.
6. **k, horizon, frames, port, budget.** These are proposed and listed as open
   items.
7. **K1 "byte for byte".** Split into a precondition replay (K1a) and a
   field-equality control on the new engine (K1b).
8. **K2's "·".** Set to 0.
9. **K3 "must fail freshness".** Realized as an F2 failure. K3b (a pad
   correlated with a hidden input) and K3c (fair after heralding) are added so
   the "against the carrier" half and the heralding hazard can each fail.
10. **K4 "bias 1/4".** Pr(1) = 1/4 on every non-source bit; open whether to bias
    c alone.
11. **K6 "8-versus-64".** Instantiated from the transport audit's exact
    construction. history_v11 is the other source of the phrase.
12. **"Zero-background countercontrol".** Read as π_bg replaced by the point
    mass on zero: A must equal P there, and K2 must fail.
13. **Stream closure.** v8's positive rule required stream-closed R. With at
    most two site-times that leaves only trivial sets, so closure moves into F2.
14. **NEG_BOTH.** Read as "pointwise: every R (v8); cone form: every R with
    |R| ≤ k". It requires every read set to be decided, as does
    PADS_NOT_FRESH. Otherwise the outcome is NOT_DECIDED.
15. **"G9".** `REPORT.md:57-69` carries no "G9" label; it is the "Fresh
    resources" section.

## Method additions not in #929

L1 (space-time parity decoupling), L2 (uniform slice pairs under the fair
product prior) and L3 (free-extreme bijection elimination) are written lemmas
the checker relies on. Each is gated by a control (L1c-L3c). They follow from
the rule's form, x_t = x_{t−2} ⊕ H(Σ x_{t−1}) with H a permutation, and from
the first-front arguments already used in Native A, `history_v11` and the
transport audit. The plan states them as methods, not as results.
