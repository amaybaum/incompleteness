# FSLICE-PS-1: can N-2, N-8 and N-9 be sourced from native OI dynamics? Plan

**WIP / UNVERIFIED. Model-written research record, paper-only. Committed on its own before any
derivation is recorded. Recorded, not frozen. No premise is adopted, weakened or changed (§A.29,
§A.50 item 6). Nothing here is proposed for the manuscripts.**

The writer is the author of the F-SLICE-HZM record, from which N-2, N-8 and N-9 come, and read the
inputs of §1 before writing this plan. The writer had begun considering the question while reading.
No derivation is recorded before this commit. The decision rule of §4 names classes and the rule
that maps them to an outcome, not expected results.

- **Accountable Issue:** #1217; programme #1169.
- **Work package:** WP-2, scientific research (#1169 comment 7199704501).
- **Authorization:** #1169 comment 7208939261 (author amaybaum, created 2026-11-27T03:22:49Z;
  owner decision "Proceed as suggested", received 2026-11-27, coordinating session). The approved
  proposal reads: "Approved: under WP-2, paper-only investigations UN-1 (#1216), F-slice premise
  sourcing (#1217), and SMD clustering (#1049/#1217), each with preregistration, bounded stopping
  conditions and independent review." Unit 2 is described as: "Whether N-2 (label independence),
  N-8 (the centred field reading) and N-9 (SMD on the full state) can be derived from native OI
  dynamics, or whether at least one remains an independent premise."
- **Goal link (§A.47):** #1217. For each of N-2, N-8 and N-9, the unit decides one class of §4:
  derivable from the stated premises, reducible to a premise Theorem 5 already carries,
  independent, or open. This decides whether the candidate-premise set of the preserved F-slice
  outcome R2 can be reduced. It does not decide the outcome in advance, and it changes no status.
- **Scope boundary.** The SMD clustering unit (#1049/#1217) runs in parallel. It concerns cumulant
  clustering on Z with 0 < abs(μ) < 1. Here SMD on the fluctuation law is carried, and only the
  extension of SMD to the joint law of labels and fluctuations (N-9) is in scope. Carrier Z, the
  nonlinear lift and consumers outside Theorem 5 are out of scope.
- **Pinned main commit [P]:** `13c05b4fe666c2e128eed1213874be9b8208982d`. Between the F-slice pin
  `a8d4ab96` and [P], `papers/SM.md` differs only at line 14, and `papers/Main.md` only at lines 360,
  544, 686, 718 and 732. No line cited here changed.
- **Writer:** the designated writer of `research/fslice-premise-sourcing-20261127`. No push and no
  GitHub write.

## 1. Inputs (on `main` at [P])

| Label | Source | Used for |
| --- | --- | --- |
| FS | `verification/programmes/substratum/f-slice-hzm-20261126/` (REPORT-r5.md, PRESERVATION.md) | N-1, N-2, N-8 and N-9 as defined; Proposition P; Lemma L; §4.2; witnesses ρ_S, ρ_T, ρ_W; the owner's ruling (R2; N-2, N-8, N-9 candidate premises) |
| L2 | `verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md` | Lemma 0; Theorem 1; positive-frequency J_F; the H-PF definition; Propositions 3, 4, 7, 11 |
| A-rec | `verification/programmes/oi-qm/reconstruction/theorem5-premise-ledger-20261126/REPORT-r3.md` | the Theorem 5 ledger; Lemma 1; §2.3 covariance; Propositions A, B, C |
| C3 | `verification/programmes/substratum/hzm-energy-sourcing-20261126/REPORT-r3.md` | the register at Main's specified partitions; the amplitude-scale gauge; staggered shift τ_c |
| SMD-SRC | `verification/programmes/oi-qm/reconstruction/smd-sourcing-20261126/` | Theorem P and its scope (Z, 0 < abs(μ) < 1); ρ_K |
| Papers | Main:44, Main:60, the Main §4.5 ledger; SM:96, 136, 290, 292, 312–316, 340–344, 811; Substratum:270–272, 288 | the stated premises |

The records are model-reviewed paper derivations. They are used as named conditional inputs
(§A.46 item 7), never as established premises.

## 2. Questions

The setting is that of FS: carrier T at the massless point (αμ = 1/d, M = μI_6), b_A1 = 0, an
F-stationary law with finite second moments, on the linear lift. The carried conditions C* are
LIN, LIFT, b_A1 = 0, L-SDS, lane 2's Theorem 1, and the Theorem 5 premises unit A carries (H-link,
H-cust, H5, H-PF, TPC, and SMD on the fluctuation law P_rest∗ρ).

- **Q2.** Can N-2 (LI: J commutes with the deviation dynamics, independent of the label) be derived
  from the stated premises with C*, or does it reduce to a premise in C*?
- **Q8.** The same for N-8 (the centred reading φ = Φ_n ∘ P_rest on the stationary support).
- **Q9.** The same for N-9 (SMD read on the full law ρ, labels included).

Each question is answered separately, by its own trace.

## 3. Method

1. For each Nk, list the candidate routes: from Main's interface (registers, records, measure
   selection), from SM's stated structure (the amplitude-scale gauge, the observer-level branch),
   from the dynamics (symmetries of F, spectral structure), and from the premises in C*.
2. Close each route by an explicit check: algebra [A], a stated reasoning step [W], or a citation.
3. For an independence claim, construct or reuse a witness. The witness must satisfy every premise
   of the stated set and of C* named in the claim, and must violate Nk. Each premise is checked on
   the witness one by one.
4. Apply maximum skepticism to any favourable route (§A.31). A route that uses a step only Theorem
   5 itself needs (for example P2a's covariance) is not a derivation (§A.29).
5. Go depth-first, one Nk at a time (§A.12).

## 4. Decision rule

Each Nk receives exactly one class:

- **D (derived):** Nk follows from the stated premises of Main and SM together with C*, by a stated
  argument, and without using a premise of C* that is itself unstated in the papers. (H-PF, L-SDS,
  TPC and SMD are unstated; a route through them is class R, not D.)
- **R (reduces to a carried premise):** Nk follows from a named premise in C* that the papers do not
  state, by a stated argument, under a stated reading of that premise. Nk is then not additional to
  C*, but it is not native.
- **I (independent):** a witness satisfies the stated premises and every premise of C* named in the
  claim, together with every other premise under study that is admitted (for example N-2 and N-8
  for Q9), and violates Nk.
- **O (open):** none of the above within the effort bound. The remaining gap is stated.

Where an Nk is class R under one reading of the carried premise and class I under another, both are
reported, with the reading.

**Outcome (generated from the classes):**
- Answer "derivable" for an Nk only in class D.
- Answer "at least one remains an independent premise" iff some Nk is class I under every reading
  admitted in its trace.
- Otherwise report each Nk's class and the readings that decide it.

## 5. Controls and countercontrols

| Id | Kind | Requirement | Fails if |
| --- | --- | --- | --- |
| P-1 | positive | At abs(μ) < 1 there is no null sector (L_0 = 0, P_rest = I). N-2, N-8 and N-9 must reduce to J_F, Φ_n and SMD on ρ | the method finds any of them non-trivial there |
| P-2 | positive | Under H-ZM, N-2, N-8 and N-9 must be supplied (FS C+2) | they are not |
| N-a | countercontrol | Proposition P's family (J_t, J_{−t}) is tamed and intertwined by F and the translations. It must not be counted as excluded by the native structure alone | the family is declared excluded without naming the premise that excludes it |
| N-b | countercontrol | The uncentred field H-PF_u of FS §6 (ρ_W) must be checked against every premise used for Q8, not dismissed by assertion | it is excluded without an explicit check |
| N-c | countercontrol | Any independence witness for N-9 (ρ_T-type) must be checked against each admitted premise individually | a premise is not checked |
| N-d | countercontrol | No step that only Theorem 5 itself needs (P2a's covariance, the U(6) stabilizer reading) counts as a derivation | such a step is used for class D or R |
| N-e | countercontrol | A candidate native route that would give Nk must be tested for whether it also forces a conclusion the framework cannot use (for example extremality against [A-rec] Proposition B) | the test is omitted |
| X-1 | extraction | Every quote is re-read at [P] by fixed-string match | a quote does not match |

A class is printed only over green controls. A failed control voids the class it bears on.

## 6. Stopping conditions

1. Each of Q2, Q8 and Q9 has a class, with all controls green.
2. Bounded effort: at most three depth-first passes per question. After that the remaining gap is
   stated (class O).
3. If a new premise would be needed to class an Nk, it is recorded, the class is O, and the unit
   ends there for that Nk (§A.29, §A.50 item 6).

## 7. Productivity test (§A.31)

**Gem** iff the unit yields, for at least one Nk, a class strictly more informative than "candidate
premise", and either reduces or confirms the candidate-premise set by a checked argument or witness.
Otherwise it is a non-gem (record only).

## 8. Outputs

`REPORT.md` in this directory, committed separately. It contains:
- the routes and traces;
- every premise labelled proved, conditional, posited or open;
- the classes and the controls;
- the scope;
- the open nodes;
- a §A.46 item 4 verification table;
- §A.42 item 8 tracing of every off-`main` reference.
