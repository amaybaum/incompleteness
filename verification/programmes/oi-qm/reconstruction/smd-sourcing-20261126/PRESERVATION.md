# SMD-SRC-1: preservation record

Mutable record under §A.46 items 4 and 8. It cites the report and does not change it.

- **Evidence layers of the results:**
  - mathematical derivation on paper, labelled [A] in the report: Theorem P, Lemmas C, S, M, G and
    K, Corollary P3, identity (★), the witnesses ρ_0, ρ_D and ρ_K and their general properties;
  - conditional results: Corollary P3′ on the imported theorem [I-Stein], recalled and not
    re-checked against its source, and Corollary Pα on the stated hypothesis H-αCLT, which no
    source theorem is pinned to;
  - exhaustive finite computation in exact rational arithmetic: the checks E1–E18 and the negative
    controls N1–N5 of `controls.py`. E1–E7 spot-check, on four small tori, spatial identities the
    report proves in general by symbol calculus; E8–E18 check the internal identities. They do not
    replace the paper proofs;
  - floating point: part X of `controls-output.txt`, an illustration that certifies nothing.
- **No Lean was built.** The kernel statement `theorem_7` is cited as read, not built.

## 1. The record preserved

**Authoritative report:** `REPORT.md` at commit `0a7d653ea090ff21e4d199fe7b07a25c2995ee49`, the
head of `research/smd-sourcing-20261126` before this file. The report was revised in place; its
earlier texts are in the branch history:
- `fed502cd41f098ef5cbb62212dec8538360c5641`: the report, `controls.py` and
  `controls-output.txt` as first committed;
- `6dd8de26f73f2425567054eba5569ceb99c72d6f`: the eight nits of the first review applied, with
  negative controls N1–N5 added;
- `81d55c71f8da18e6fdbbbfef763ce60be4c4bd6b`: the four findings of the second review applied,
  with N1–N4 calling the functions of the checks they target;
- `0a7d653e`: the two wording nits of the third review applied; `controls.py` and
  `controls-output.txt` unchanged from `81d55c71`.

**Plan.** `PLAN.md` (commit `6a0a11657d55f4e847b7b53cefdd1168aec2e5a1`, committed alone before
the report) fixes the question, the clustering notions, the decision rule, the controls and the
stopping conditions. It is unchanged at `0a7d653e`. Its chronology disclosure states that, while
reading the inputs before writing the plan, the writer formed, without writing or checking them, a
candidate positive route (spreading under the dispersive linear map with a clustering bound) and
the two countercontrols later used (μ = 0 and finite Gaussian mixtures). The plan therefore fixes
the decision rule before the report; it does not certify that no part of the route was conceived
before it.

**Status in the header.** The header of `REPORT.md` records the report's status before review
("Pending independent non-author review"), and its §14 table says "unreviewed". Review is recorded
here.

**Accountable Issues:** #1049 and #1217 (programme #1169). Guiding pull request: #1612.

**Owner decisions.** Each is a #1169 comment posted from the account `amaybaum`, quoting the
owner:
- **Comment 7199704501** (created 2026-11-26T17:49:03Z; decision received 2026-11-26T17:49Z):
  activation of work package WP-2, scientific research, by the owner's decision "Proceed as
  suggested".
- **Comment 7200549806** (created 2026-11-26T18:30:55Z; decision received 2026-11-26T18:30Z),
  item 4, authorizes the investigation: "Authorize all three ranked scientific investigations —
  SMD sourcing, uniform norm control and F-slice — at paper-only level, with independent review and
  bounded stopping conditions."
- **Comment 7202075726** (created 2026-11-26T19:53:55Z; decision received 2026-11-26T19:52Z),
  item 3: "Preserve #1612, #1614 and #1611 at their reviewed landing heads, subject to their
  remaining verification and landing requirements. Preservation only; no premise adoption or
  manuscript integration." The same decision states: "All existing correctness, independent
  review, staging, freeze, trial and landing gates remain in force."

**Independent non-author reviews.** These are model reviews by reviewer agents, each recorded on
PR #1612 as reviewer text posted verbatim: evidence of review, not independent mathematical
verification.
- **Comment 7201058488, review of the plan at `6a0a1165` and the report at `fed502cd`: ACCEPT
  WITH NITS,** findings 1–8 (seven nits and one minor finding, on the labelling of Corollary Pα).
  It re-derived Theorem P line by line, Lemma G with identity (★), the three witnesses and the
  claim about unit A's Proposition B, found no mathematical error, and reproduced the controls
  byte for byte (39 PASS lines at that commit, before N1–N5 were added).
- **Comment 7201224484, confirmation review at `6dd8de26`: ACCEPT WITH NITS,** four minor nits.
  It confirmed the eight nits applied, reran `python3 -I controls.py` (exit status 0, output
  byte-identical, 56 PASS lines, no FAIL) and recomputed each negative control's target predicate.
- **Comment 7201280749, confirmation review at `81d55c71`: ACCEPT WITH NITS,** two wording nits.
  It confirmed the four findings applied and that the refactor of `controls.py` keeps every
  positive check, and reran the controls with the same result.
- **Comment 7201586635, confirmation review at `0a7d653e`: ACCEPT.** It confirmed the two wording
  nits applied, with only `REPORT.md` changed, and re-derived the statement "at least two distinct
  S_h for any nonzero t, e".
- **One reviewer wrote several reviews.** The texts of the reviews at `81d55c71` and `0a7d653e`
  refer to the reviewer's own earlier runs and proposals ("my earlier run at 6dd8de26", "as I
  proposed"), so the three confirmation reviews come from one reviewer agent. The records do not
  state whether that agent also wrote the first review.

**Reproduction of the exact controls.** In the directory of the report at `0a7d653e`, run
`python3 -I controls.py` (Python 3.8 or later; NumPy only for part X). Expected: every exact line
`PASS` (56 lines beginning `PASS`), the final line `EXACT CHECKS: ALL PASS`, exit status 0, and
output byte-identical to `controls-output.txt`. The writer of this record ran it at `0a7d653e`
with Python 3.13.18 and obtained that result. Part X is floating point and is not part of the
expected result. This local run is evidence for this record, not a `check-run` attestation.

## 2. Substantive result and its precise scope

Every result is on the carrier Z = Z^d, for the observer-level real linear offset-free lift
F = F_s ⊗ I_6 of SM:314 at M = μI_6, on configuration space X = ((R^6)²)^{Z^d}. Nothing is claimed
for the finite torus T, where unit A's Propositions A and B stand, for the Z/q level, for the
nonlinear case, for an offset b ≠ 0, or for μ = 1.

**Theorem P [A].** Let d ≥ 1 and 0 < abs(μ) < 1. A law ρ on X that is F-stationary (L-SDS), has
moments of all orders bounded uniformly in the site, and satisfies cumulant clustering K2 is a
centred Gaussian law, and hence satisfies SMD (Lemma G).
- No translation, cubic or J-invariance, no TPC and no H-PF is used.
- The dynamics enters only through the non-constancy of the dispersion relation (μ ≠ 0, Lemma
  S(b)) and the uniform gap from ±1 (abs(μ) < 1). No Hessian condition is used.

**Corollaries.**
- **P3 [A]:** the same with K2 replaced by finite-range dependence with uniformly bounded moments
  of all orders (K3), via Lemma K (K3 implies K2).
- **P3′:** K3 with only uniformly bounded fourth moments, conditional on [I-Stein].
- **Pα:** strong mixing with summable rate and uniformly bounded 2+δ moments (Kα), conditional on
  H-αCLT, for the mixing coefficient indexed by distance alone. A coefficient restricted by set
  size is not covered.

**Lemma G [A].** For abs(μ) < 1 and a centred Gaussian law with uniformly bounded second moments,
R(w) is defined almost surely and R(w)_*ρ = ρ if and only if R(w) C R(w)ᵀ = C, each direction
proved. With the TPC form and pairwise distinct block values, Stab(ρ) = U(3)×U(2)×U(1).

**Witnesses and countercontrols [A], with exact spot-checks.**
- **ρ_0 (CC-N):** a finite-range Gaussian condensate state meeting K3, L-SDS and the fixed premise
  set with distinct block values. It shows the positive results are not vacuous, and that the
  conclusion of unit A's Proposition B, proved on T, fails on Z.
- **ρ_D (CC-D), at μ = 0:** meets K3, L-SDS and the fixed set and violates SMD. The positive proof
  fails there only at Lemma S(b).
- **ρ_K (CC-K), on Z^3 with 0 < abs(μ) < 1:** an equal-weight mixture over the cubic rotation
  group meeting L-SDS and the fixed set, failing every clustering notion and violating SMD; the Z
  analogue of unit A's Proposition A. It shows the clustering hypothesis cannot be dropped.

**Outcome against the decision rule (`PLAN.md` §3), reading R1 of report §1.2, all controls
green:**
- on 0 < abs(μ) < 1: POSITIVE for K2 and K3; POSITIVE conditional on [I-Stein] for K3′ and on
  H-αCLT for Kα; OPEN for translation mixing K1 and translation ergodicity K0 (the gap of report
  §5); no obstruction found for any notion;
- at μ = 0: OBSTRUCTION for every notion, by ρ_D;
- without clustering (d = 3): stationarity with every premise of the fixed set does not force SMD
  (ρ_K).

Under reading R2 of the μ range, no notion is POSITIVE on the whole of abs(μ) < 1; the
per-range statements are the same under both readings.

**What the result does not show (report §0, §8).** None of L-SDS, K2, Kα or the moment conditions
is stated in SM. The result replaces SMD, an unstated symmetry condition on the state, by unstated
conditions of a different kind: exact stationarity under the same linear map and summable
clustering. It derives nothing from SM's stated premises. Whether to state any of these conditions
is an owner decision (§A.29, §A.50 item 6); the report proposes nothing and this record adopts
nothing.

**Productivity:** met through S1 and S3 of `PLAN.md` §5; S2 is met only under reading R2, through
the μ = 0 obstruction. NEW: Theorem P, ρ_0 with the failure of unit A's Proposition B on Z, and
ρ_K. POSITIVE: Lemma G and the finding that only non-constancy of the dispersion relation is used.

## 3. Verification status and remediation (§A.46 items 4 and 8)

Each paper result is checked only by the model reviews of §1. The exact controls are exhaustive
finite computations on the stated tori and matrices, a different layer from the paper derivations.
The remediation plan below authorizes no work (§A.45 rule 3).

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| Theorem P; Lemmas C, S, M, G, K; Corollary P3 | report §2–§3 | partially verified: paper proof, model-reviewed | independent non-model review, in particular of Lemma S(b) (the pushforward Riemann–Lebesgue step and the analytic non-degeneracy of Θ) | #1217 | a recorded independent review; optionally a Lean formalization of Lemmas C and S |
| Corollary P3′ (open node N3) | report §3, §11 | conditional on [I-Stein], recalled and not re-checked against its source; the first review matched it to the reviewer's recollection only | a check of [I-Stein] against Ross 2011, Theorem 3.5 | #1217 | a recorded source check |
| Corollary Pα (open node N3) | report §3, §11 | conditional on the stated hypothesis H-αCLT; no source theorem pinned | a specific source theorem with its indexing of α, or a proof of H-αCLT | #1217 | a pinned theorem or a written proof |
| Identity (★) and the witnesses ρ_0, ρ_D, ρ_K, including identifiability of finite Gaussian mixtures | report §4 | partially verified: paper proofs, model-reviewed; the identities spot-checked exactly on small tori | independent review of the general symbol-calculus proofs and of the identifiability step | #1217 | a recorded independent review |
| Exact controls E1–E18, N1–N5 | `controls.py`, `controls-output.txt` | reproduced, exit status 0 and output byte-identical: 39 PASS lines by the review at `fed502cd`, before N1–N5 were added; 56 PASS lines by the reviews at `6dd8de26` and `81d55c71`, and by the writer of this record at `0a7d653e`, where `controls.py` and `controls-output.txt` are unchanged from `81d55c71` | none for what they check; they certify the identities only on the tori and parameters listed in report §4 | #1217 | none; they do not stand in for the general proofs |
| K1 and K0 (open node N1) | report §5, §11 | open | a proof, or a non-Gaussian F-invariant translation-mixing law with finite moments violating SMD | #1217 | either |
| Premise audit | report §6 | partially verified: model-reviewed | independent review | #1217 | a recorded independent review |
| Unstated state conditions L-SDS, K2, moment bounds; source of K2 and L-SDS (N5) | report §6, §8, §11 | not stated in SM; not adopted | a derivation from stated premises, or an owner decision on a premise | #1217; #1049 for the offset-free branch | a written derivation, or an owner decision |
| Open nodes N2 (μ = 1), N4 (offset), N6 (torus) | report §11 | open | derivation | N2, N6: #1217; N4: #1049 | a written derivation or counterexample |
| Preregistration order (`PLAN.md` before the report) | `PLAN.md` | evidence is commit order only: `6a0a1165` at 18:40:03Z precedes `fed502cd` at 18:51:13Z (2026-11-26); with the chronology disclosure of §1 | none available from commit order alone | #1049, #1217 | none; the limitation stands as stated |

## 4. Off-`main` references (§A.42 item 8)

Each reference is classified by reading the claim it is attached to, using the three classes:
provenance, support on `main`, and support off `main` (gap).

| Reference | Where | Classification |
|---|---|---|
| #1169 comments 7199704501, 7200549806, 7202075726 (owner decisions) | `PLAN.md`, report header; §1 here | provenance: authority records quoted with author and time; no result uses them |
| #1169 comment 7191949320 (successor assessment) | `PLAN.md`, report §13 | provenance: question source |
| PR #1612 comments 7201058488, 7201224484, 7201280749, 7201586635 (reviews) | §1 here | provenance: evidence of review; no result uses them |
| commit `6a0a1165` (`PLAN.md`) | report header; §1, §3 here | support off `main` (gap), closed by the landing condition of §5: it holds the plan and the evidence of its order |
| commit `fed502cd` (first report text) | §1, §3 here | support off `main` (gap), closed by the landing condition of §5: the preregistration-order row uses its commit time. For identifying the first reviewed text it is provenance |
| commits `6dd8de26`, `81d55c71` | §1 here | provenance: cited to identify the texts the confirmation reviews read |
| commit `0a7d653e` (`REPORT.md`, `controls.py`, `controls-output.txt`) | §1 here | support off `main` (gap), closed by the landing condition of §5: the authoritative report and the exact controls with their recorded output |
| the commit adding this file | — | support off `main` (gap), closed by the landing condition of §5: this record's own content |
| pin `a8d4ab96` and the SM line citations | report header, throughout | support on `main`: `a8d4ab96` is an ancestor of `main` at `84e927b9`. `papers/SM.md` differs between them only at line 14, which the report does not cite, by a one-line replacement that leaves line numbers unchanged |
| unit A's record (`../theorem5-premise-ledger-20261126/`) and lane 2's record (`../complex-carrier-20261126/`) | throughout | support on `main`: on `main` at the pin and unchanged at `84e927b9`; used as model-reviewed inputs, named where used |
| kernel `theorem_7` | report §1.1 | support on `main`: statement read, not built; `verification/lean-mathlib/` is unchanged between the pin and `84e927b9` |
| [I-Stein] (Ross 2011), Rosiński and Żak, Dudnikova, Komech and Spohn (2003) | report §3, §5 | external literature, recalled, not repository content: Corollary P3′ is conditional on [I-Stein]; Corollary Pα rests on the stated hypothesis H-αCLT, not on a pinned source; Rosiński and Żak is used only in an unsuccessful route |
| #1049, #1217, #1169 | headers | provenance: accountability and routing |

**Support off `main` (gaps), and how they close.** Each gap below is closed when the merge commit
of §5 lands with the commit reachable from `main`. None is closed before that, and keeping the
branch does not close it.
- `6a0a1165`: `PLAN.md` and the preregistration order.
- `fed502cd`: its commit time, for the preregistration-order row.
- `0a7d653e`: the authoritative report and the exact controls.
- The commit that adds this file: this record.

## 5. Landing condition

The record is preserved only through a **merge commit, not a squash**. The merge keeps these
commits reachable from `main`:
- `6a0a1165`, `fed502cd`, `6dd8de26`, `81d55c71` and `0a7d653e`;
- the commit that adds this file, which follows the reviewed head `0a7d653e` and adds only this
  file.

That `PLAN.md`'s commit precedes every report commit is part of the record's provenance.

The owner decision of 2026-11-26T19:52Z, item 3 ("Preserve #1612, #1614 and #1611 at their
reviewed landing heads, subject to their remaining verification and landing requirements"), is the
owner's approval of this merge (§A.50 item 1), subject to the review of this file and green CI. The
same decision keeps every existing gate in force.

## 6. Preservation rationale

The investigation answers rank 1 of the successor assessment and unit A's open node O3: whether
stationarity under the linear lift together with spatial clustering forces SMD on Z. It uses a
plan committed before the report, its controls are green, and its negative statements are scoped.

It establishes, on Z^d with 0 < abs(μ) < 1 on the linear offset-free branch:
- **that P2d of unit A's ledger is derived given L-SDS and K2** (or K3; conditionally Kα or K3′),
  by Theorem P and Lemma G, with the stabilizer exactly U(3)×U(2)×U(1) under TPC and distinct
  values;
- **that the clustering hypothesis is load-bearing** (ρ_K) and that dispersion is load-bearing
  (ρ_D at μ = 0);
- **that unit A's Proposition B does not transfer to Z** (ρ_0);
- **which hypotheses the infinite-lattice route uses**, with countercontrols for two of them.

It does not source SMD from SM's stated premises: it trades SMD for named unstated state
conditions with an explicit failure mode. It is substantive and nonredundant with units A and C
and lane 2, it is independently reviewed by the model reviews of §1, its exact controls
reproduce, and its open gaps carry the remediation plans of §3. Its findings for routing (report
§12) are listed there and edit no other record.

## 7. Standing of this record

Preservation establishes no claim (§A.46 item 1). The model reviews are evidence of review, not
independent mathematical verification, and landing the record does not change any result's
evidence layer. No premise is adopted, and nothing is proposed for the manuscripts.
