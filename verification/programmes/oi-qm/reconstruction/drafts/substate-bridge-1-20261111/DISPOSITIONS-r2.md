# SUBSTATE-BRIDGE-1 unit 1 — dispositions for r2

**WIP / UNVERIFIED. Authorizes nothing.** Writer's dispositions of ChatGPT review 5858000929 (REVISE; PR #1232 at `b94b283aab582b33ccdfca34da6507c2bbf4a224`; posted under the owner's account), and of one further fact the coordinator asked to be incorporated. Each finding was checked against the r1 text before any change. Section numbers are those of `SUBSTATE-BRIDGE-UNIT1.md` r2.

## Findings

| # | Finding | Check against r1 | Disposition | Where |
|---|---|---|---|---|
| 1 | N1/N2 and SLL were presented as necessary for every Bell route. A non-site-fibred shared factor is a possible construction; prepared long edges between ordinary sites and within-cone propagation on the unchanged stencil are other routes. No negative verdict may extend to the O2 window. | **Correct.** r1 §3.3 gave N1's reason as "L1: site-fibred factors add no edge", which holds only for wings outside the stencil's graph cone. r1's Q4 row and SLL's exclusion branch ("leave Bell-scope's O2 and O3 as the only open points") omitted prepared long edges. r1 §3.1 did say substates "neither supply nor exclude" O2, but §0 Q2a answered "No" without that limit, and class (a)3 did not state that it is conditioned on (Sep). | **Applied.** §3.3 now distinguishes routes A (shared factor), B (prepared long edges), C (within-cone propagation). N1–N2 are scoped to route A; N3–N4 to every route. SLL is renamed "missing lemma for a substate-carried escape", stated to be neither necessary nor sufficient for an escape, and its exclusion branch lists routes B, C and O3 as left open. Class (a)3 and L2 are stated for wings that satisfy (Sep) only. Route C is recorded as not assessed, with a pointer to the mixed-path unit under #868 (comment 6794392080); no result of that unit is used. | §0 (Q2a, Q2b, Q4, "does not show"), §3.1, §3.3, §4.2, §4.3, §5 |
| 2 | §3.4's PAD condition lacks ensemble conditions: measurement independence or conditional-law balance; each preparable law; both wings; complete continuations. An unresolved fair pad is a candidate distribution, not a sourced preparation family. | **Correct.** r1 computed both history laws under one unconditional μ and required a μ-preserving σ. That is no-signalling only when the law of the hidden state does not depend on the settings. Verified by an exact instance (S7): a flip that preserves the uniform marginal of a hidden bit, equal unconditional history laws, and `P(h=0∣b)` equal to 1 and 3/4. r1 item 4 mentioned reuse, but the definition of the history did not include continuations, and "for every preparable μ" was not carried into (PAD). | **Applied.** §3.4 defines the joint law of (hidden state, settings), the conditional laws `μ_{ab}`, MI, and (NS_A) in conditional form; (PAD) is restated with `σ_* μ_{ab} = μ_{ab'}`, with its three limits (law, family and wings, complete history). The tower reading is labelled a candidate distribution with a candidate reason. The point-mass argument is marked as under MI. S7 added to the probe with a control. | §3.4, §3.3 (N3), §4.4 (G7), §5 (N3), §7.2, probe S7 |
| 3 | The heads of PR #1230 and PR #1231 are reversed in §6; recheck blobs; both are now accepted within scope; keep off-`main` status. | **Correct.** `git ls-tree` at the two heads: `INTERVENE-UNIT1.md` blob `06f148e0…` is at `ea12fde1…` (PR #1230, branch `research/intervene-1-20261111`); `BELL-SCOPE-UNIT1.md` blob `5814e479…` is at `e1534b08…` (PR #1231, branch `research/bell-scope-868-20261111`). The blobs in r1 were right; the two head ids were exchanged. Both PR heads were confirmed through the host API. | **Applied.** Full head ids corrected. Review ids added: 5857985732 (#1230 at `ea12fde1…`, accept with documentation nits) and 5857981727 (#1231 at `e1534b08…`, accept with nonblocking notes). Both classifications stay "support off `main`: gap"; a review is not verification from `main` (§A.46 item 7). No conclusion depended on which head carried which draft: every statement cites the drafts by name and section. | header, §6 |
| 4 | The record must distinguish "no native computation used or published in this unit" from "unapproved exploratory computation in the session", give the disposition of the scripts and exclude their outputs. | **Correct.** r1's header said the unit "runs no OI mechanism" and that its "only computations" were the generic checks; r1 §7 said "No OI mechanism was computed". The PR body reports three `wave_torus*.py` scripts run in that session on the linear lattice wave map. The unit's text did not record them. | **Applied.** Header and §7.1 state that the scripts were run, that the brief did not authorize them, that they were reported to the owner, that they are not in the repository and were not rerun or read for r2, and that their outputs are excluded and are not a test, a control or evidence for any route, the mixed-path unit included. §6 lists them as excluded. Dependence check: see below. | header, §6, §7.1, §7.2 |

## Dependence check for finding 4

Every statement of §§0–5 was traced to the support it names. No statement cites the scripts. The statements about the linear lattice rule rest on Main:364, the rule's definition, the kernel module `NativePadicReduction`, the records on `main`, or one line of algebra (L4).

One r1 sentence named no support: §3.1, "the long-wavelength speed is a property of the linear rule, which the per-site lifts keep". The record does not show whether the scripts informed it. It is withdrawn. Recovery note: for `R/Z`-valued fields a real-valued lift obeys the same recurrence, so the real rule's dispersion relation would apply to the lift; for `Z_p`-valued fields no real-wavenumber decomposition was defined. Neither was worked out, and no verdict used the sentence, so r2 states only that the lifts keep the rule's coefficients and that the speed for lifted fields was not examined.

## Nonblocking precision notes

| Note | Disposition |
|---|---|
| E2 concerns one shared linear encoding and input-law-independent kernels; "jointly measurable" holds under that hypothesis, not as an ontology-level claim; context-dependent, non-linear and history-dependent realizations are outside it. | **Applied.** "Scope of E2" paragraph in §2.3; wording in §0 (Q1c, favourable-reading check) and §4.3 (a)1 changed from "any linear encoding" to "one linear encoding shared by all procedures". The favourable-reading check no longer says the readings do not "survive"; it says neither is shown to be a source. |
| Saturation witness: identify the output register's decoding to the designated output carrier. | **Applied.** §2.2 names the bijection `ι`, the step `o ↦ o + ι(r(s))`, and the decoding `ι⁻¹` to output configuration and outcome. S1 already indexes the register this way; unchanged. |

## Further fact incorporated

Independent non-author review of PR #1233 (comment 6794566946, at `7f80ee6e…`), blocker B1: under ledger item (vii) the coupling graph is the same at every state, `G_φ^K = G_φ`.

- **Status.** A reviewed finding on an open PR, off `main`. Not established on `main`.
- **Check.** Re-proved here as L4 from its own definition, in one line, for arbitrary abelian site groups. The review's exhaustive ring computation was not used and not rerun.
- **Consequence for Q2.** (1) The additive per-site lifts on `main` cannot have preparation-indexed edges: no substate prior or conditioning event creates one. (2) Route B needs an update outside (vii), with or without substates. (3) A substate-carried route B needs a non-additive coupling of substates to the neighbour assignment (R3), where the no-backflow control (c4) gives no information. (4) N1 counted as a site cannot be preparation-indexed within (vii). (5) Scoping (x) alone does not open route B while (vii) stands.
- **Where.** §3.1 (L4 and consequences), §3.3 (route B, N1), §4.3, §4.4 (G8), §5 (N1), §6.

## Verdicts

| Q | r1 → r2 |
|---|---|
| Q1a, Q1b, Q1d, Q3 | unchanged |
| Q1c | unchanged in substance; E2's hypothesis is stated as one shared linear encoding |
| Q2a | narrowed. r1: "No". r2: the constructions on `main` supply neither an edge nor within-cone dependence, cannot have prepared edges under an additive rule (L4), and leave the O2 window neither supplied nor excluded and untested |
| Q2b | restated. r1: four properties N1–N4 for "a native linkage". r2: three routes; N1–N2 for route A only, N3–N4 for every route; route B outside (vii); route C not assessed |
| Q4 | unchanged: indeterminate for OI itself. SLL is scoped to a substate-carried escape and is not a necessary condition for an escape |

No verdict became stronger. Two negative statements were narrowed (Q2a, class (a)3), one sentence was withdrawn (§3.1, wave speed of the lifts), and one lemma was added (L4).

## Probe

`probes/generic_substate_checks.py` gained S7 (two lines: the correlated-setting instance and its independent-setting control). S1–S6 are unchanged. `python3 -I -B generic_substate_checks.py`: 13 lines, all PASS, exit 0; `.out` regenerated. Exact rational arithmetic; no OI rule is encoded.

## Not changed

- G1 and G2 remain observations for the reviews of PR #1230 and PR #1231. The re-reviews of those PRs record the corresponding nits (spanning frame; directed against symmetrized path), which is noted in §3.2 and §6.
- The [L] entries are still recalled, not read.
- No reading of ledger (viii), (vii) or (x) is chosen.
