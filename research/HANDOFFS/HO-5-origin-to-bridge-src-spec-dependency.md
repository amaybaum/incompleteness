# HO-5 (v1) — origin → bridge: one shared object (J = cyc3), two open propositions (SRC, SPEC), and Lemma P

**From** `research/origin` (node O4). **To** `research/bridge`. Version 1, 2026-10-10.

## Statement

1. **A_miss restated.** The bridge's isolated missing assumption (archive `pt/INTEGRATION-NOTE-STAGE6.md` §5: (b) on one
   token for `ball3Drive`'s flow `R_z(t)` and its J-conjugate `R_x(t)`) is equivalent to (b) for `R_z(t)` for all `t`
   together with (b) for the single discrete operation `J = cyc3`, since `J = R_z(π/2)·R_x(π/2)` and
   `J R_z(t) J⁻¹ = R_x(t)` (KInfFoundations.lean:425 `cyc3`, :427 `cyc3_apply`, :449 `ball3Drive`).
   Label: CONDITIONAL ([W] proof; the group identities [X]).
2. **J is the Discrete Origin target in the bridge's vocabulary.** `J` maps the pure frame state `e_z` to the pure
   balanced state `e_x`, carries the owner's interference witness `(1, 1/2)` with `J⁻¹`, and its unitary lift is a
   non-monomial balanced mixer of order 3. Label: CONDITIONAL ([X] exact).
3. **Two propositions, two owners.** SRC(J): `J` (or any balanced mixer) is available on one token from a premise that
   passes the disguise test — Origin's, OPEN, impossible on the stated access (NOTES-O1 T3, T5, T6; every known instance
   fails the disguise test or changes the observation law, NOTES-O2). SPEC(J), SPEC(φ): (b) for `J` and for the phase
   flow on one token (matrix form: context stability / all-level availability) — the bridge's, OPEN, independent of
   everything at L (stage 6). Neither discharges the other.
4. **Matrix reduction.** If a generating class contains the substratum class and the spectator forms of one balanced
   mixer `B`, it contains the spectator forms of the drive (`substratumClass_contextStable`, StructuralClosure.lean:261,
   for the phase flow; Kronecker identity [X]). Label: CONDITIONAL ([W]).
5. **Lemma P (constraint handed over).** If single-token observation in a composite model is passive and repeatable,
   every pure state of a token is outcome-deterministic for that readout, so no balanced mixer and no drive through the
   native NOT exist on a token. A bridge construction that wants the drive cannot assume passive token-level
   observation. Label: CONDITIONAL ([W] proof, no kernel check; [X] instances; [A] oistage A5).
6. **Proposed joint statement (for the coordinator to adopt, amend or reject; not adopted).** Over the substratum class
   (monomial, with its phase continuum), exact finite QM follows from SRC(B) and SPEC_M(B) for one discrete balanced
   operation `B`; at the pair level the bridge's missing assumption is SPEC_P(φ) ∧ SPEC_P(J). Origin owns SRC; the
   bridge owns SPEC. Supporting pieces: SPEC_M of the phase flow is a theorem (StructuralClosure.lean:261); SRC(B) +
   SPEC_M(B) + the phase continuum give the drive at every level by exact conjugation (`o3_continuous` C1,
   `o4_dependency` D5) and then phase-free richness (RouteB.lean:161 `derivedOI_qm_iff_phaseFree`;
   MinimalRepertoire.lean:569 `oiPlusMin_iff_qm`).

## Evidence

| item | pointer |
|---|---|
| source | `research/origin` @ `4cec62c9ae9178b45512133abab37b2d9f59847d` |
| proposal | `research/origin/handoff-proposals/O4-origin-bridge-dependency.md`, sha256 `f9cef7aaa7a5511ad3f5d835e4d11ada4540ec952d86cf36e19fcd665a0378bd` |
| results rows | `research/origin/RESULTS.md` O4-I1, O4-J, O4-I2, O4-D, O3-T4, O3-T6 (sha256 `a3b3c17969b32fffa76946d33c1e99a4ce0d41d95f898308e812cfde23d33950`) |
| scripts, outputs | `research/origin/experiments/o4_dependency.py` (sha256 prefix `a68db000e8b3ab88`), `.out` (`8121ece52a72e03f`), 5/5 + 3 countercontrols; `o3_continuous.py` (`795cb274910d8d08`), `.out` (`b4e1e2613ccc1c9b`), 11/11 |
| coordinator audit | replays byte-identical (`research/AUDITS/2026-10-10-round1/origin/REPLAY-LOG.txt`, 6/6); `indep_checkO.py` X3 (`cyc3 = R_z(π/2)R_x(π/2)`, `cyc3 R_z(t) cyc3⁻¹ = R_x(t)`, `cyc3³ = 1`), X4 (`R_x(π/2) e_z` balanced, `R_x(π) = nflip`), X2 (visibility `2|a|²|b|²`, witness `(1, 1/2)`) CONFIRMED; kernel citations verified at L (`cite_check.out`) |

## What the receiving thread may assume

Items 1–5 at their labels; item 6 as a proposal only. In particular the bridge may take A_miss in the form
"(b) for `R_z(t)` for all `t`, and (b) for `J = cyc3`" (item 1) and may use Lemma P as a constraint on realizations
(item 5).

## What it may not assume

- that SRC(J) is available or that SPEC is discharged — both are OPEN;
- the joint statement of item 6 — it is not adopted by anyone;
- kernel status for items 1–5: the only CERTIFIED pieces are the cited declarations themselves.

## Receipt

The receiving thread copies this file into `research/bridge/inbox/` with a commit naming `HO-5 v1` and records in its
`LOG.md` whether and how it relies on it.
