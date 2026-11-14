# Status note: the Bell debugging ladder r3

**Draft for the Bell landing package (`LANDING-PLAN.md` §5).** At landing this note becomes
`verification/programmes/oi-qm/reconstruction/drafts/bell-ladder-20261113/STATUS.md`. It gives the
standing of the records in that directory and changes none of them; r3 is the accepted text.

The ladder is a conditional paper result. It is not a native OI Bell mechanism, a native escape or an
OI-wide no-go.

## Accepted record and reviews

- **Record.** `BELL-LADDER-r3.md` at `d8e4f80e71b64972ee3e87a874544c8bd358d5c2` (PR #1273), blob
  `0298088d66547e0aa28b634bacae196991507a8c`, SHA-256
  `6e7708ceda86b8121dad6904cbc6c8373e819c08985a481808168a9778ebb5a6`, 304 lines. "LD:n" is line n
  of that file. The directory's twelve files and their SHA-256 are listed in `OBJECTS.md`, which
  records no substitution; every committed blob equals the reviewed bytes. Commits: `b8096c79`
  (r1, review, r2; parent `c3b5f37a`), `c4781c93` (r3, its notes and response), `d8e4f80e` (the r3
  confirmation).
- **Review trail.** r1 and r2 stay unchanged because the reviews and confirmations cite their lines.
  - `REVIEW-r1.md`: independent non-author review of r1, ACCEPT WITH CHANGES (C1–C14); dispositions
    in `RESPONSE-r1.md`, all applied in r2.
  - `CONFIRM-r2.md`: focused confirmation of r2 at `b8096c79`, ACCEPT WITH CHANGES (R1–R3, N1–N4);
    dispositions in `RESPONSE-r2.md`, all applied in r3.
  - `CONFIRM-r3.md`: focused confirmation of r3 at `c4781c93`, ACCEPT, "nothing left to change".
  - ChatGPT review 5892919040 (posted under `amaybaum`, 2026-11-13T14:39:54Z) at `d8e4f80e`: "ACCEPT
    AS A CONDITIONAL PAPER RESULT, with two integration safeguards. Not a native Bell escape, OI-wide
    no-go or merge approval."
- **Nature of the reviews.** All are model reviews; the reviewer of REVIEW-r1, CONFIRM-r2 and
  CONFIRM-r3 is not an author of the ladder or of its inputs. None is a human review, a GitHub
  approval or an owner decision, and none is verification (§A.46 item 7). REVIEW-r1 re-derived
  Proposition AL's steps 1–5 by hand; ChatGPT checked the proof "against the stated group/coset
  hypotheses". REVIEW-r1 §7 records that NOTES' `Z_3` Birkhoff remark (NOTES-r3:63–64) was not
  reviewed; nothing in the record rests on it.
- **Authority.**
  - Unit: #868 comment 6854708572 (`amaybaum`, 2026-11-13T13:44:26Z): "Full ladder as relayed".
  - Owner decisions on NOTES-r3 Q1–Q4: #1273 comment 6860580909 (`amaybaum`, 2026-11-13T17:47:30Z):
    "Adopt all four (Recommended)": "Ledger (vii) is included as a **conditional ledger posit**";
    "MI* over generator residues stays a **distinct explicit hypothesis**, unless it is shown that the
    named response-relevant pre-setting variable in (xiv) contains every residue that reaches the
    response or the full record"; "The AL review satisfies Q3 before any new preregistration depends
    on AL. AL's expected answer is **not** written into the mixed-path test"; "The full-history
    convention applies **to AL only**." It also states: "These decisions change no verdict, proof or
    classification in BELL-LADDER-r3."
  - Landing plan: #868 comment 6873193841 (`amaybaum`, 2026-11-14T06:34:07Z).

## What the record supports, and at what strength

| § | Result | Strength in the record |
|---|---|---|
| 1 | stages 0–4: NOT FORCED (designed witness); for OI's native rule undetermined | [A], designed toy maps that are not OI rules, on [K] and [P] |
| 1 | stages 5–6: OBSTRUCTION under the stated conjunction | [A] on Bell-scope Theorem N/N′ and §4 [A], SB L3 [A] and Main:362, :364–389 [P] |
| 1 | stage 7: UNDETERMINED | no selector supplied (Main:360 [P]; N4, carried by #1274) |
| 2 | hand checks 1–5 of the toy maps | [A] |
| 3 | six controls, one condition changed at a time | [A] |
| 4 | Proposition AL: affine update, coset-uniform run law, cell-valued settings, fixed regions, complete histories and complete-history NS ⇒ a Bell-local record law; NS failure ⇒ TV 1 between two remote settings at a fixed own setting | [A] on OA1 D5 and T1 Lemma A-T [W] |
| 4 | **Histories** scope limit: with NS only on a setting-selected read, a PR box is reachable inside (vii) with a coset law and MI | [A], the non-author reviewer's witness |

**Claim supported by this record:** "Starting from finite-horizon equivalence, designed toy maps on
one carrier show that one deterministic map, site factorization, separation in the actual coupling
graph and observer access do not by themselves force Bell-local behaviour; directed separation in the
actual coupling graph together with measurement independence for the response-complete pre-setting
variable forces it for the whole finite menu and complete local histories (Bell-scope Theorem N/N′,
with SB L3 for the directed form); within ledger class (vii), taken as a conditional ledger posit, for
coset-uniform run laws, cell-valued settings and complete fixed-region histories, complete-history
no-signalling alone forces a Bell-local record law, and its failure makes two remote settings
perfectly distinguishable at a fixed own setting; quantum selection is undetermined (hand
derivations [A] on manuscript [P], kernel [K] and research-record [W] inputs, with stage 5 resting on
Bell-scope [A]; model-reviewed by a non-author reviewer and by ChatGPT, not independently verified; a
conditional paper result, not a native OI Bell mechanism; not adopted; no manuscript claim
affected)."

## Hypotheses

- **Controlling condition (LD:53–62):** (D) one deterministic map; (F) finite site factorization;
  (Gen); (Rec), complete local record windows; (Sep) by directed paths in the actual `G_φ`; (MI\*)
  for λ\*, or (GI) with MI for Ω; a finite menu with every pair jointly admissible; every-run outputs
  with failures mapped by a fixed local rule; no postselection. (MI\*) is a distinct hypothesis, not
  ledger item (xiv), unless (xiv) is shown to contain every residue (owner decision Q2).
- **Proposition AL (LD:189–205):** (AL1) finite abelian site groups and an affine update (ledger
  (ii), (vii), (viii)); (AL2) a run law uniform on a coset; (AL3) settings that are affine images of
  generator cell values, every pair of positive probability; (AL4) fixed record regions independent
  of state and settings, histories complete in the sense of Bell-scope (Rec); (NS) on those complete
  histories. Ledger (vii) is a conditional ledger posit (owner decision Q1). The full-history
  convention applies to AL only (owner decision Q4).
- **For OI under the ledger (LD:78–83):** the full ledger, coset run laws and cell-valued settings.

## Limitations

- Stages 0–4 rest on designed maps; for the native rule those stages are undetermined (LD:89–93).
- No general access-only theorem; the access controls are shown in the toy only (LD:179–183).
- AL does not cover laws that satisfy NS only as a mixture, coarse-grained settings with correlated
  generators, postselection, setting-selected reads or non-affine updates (LD:242–253).
- Open items listed at LD:269–278: a selector (stage 7), NBA for non-affine branches, the record
  convention, the run law under (iv), MI\* versus (xiv), embedded setting generation, physical *c*.
- §A.31 fixed point not reached: two passes, the second with a NEW item (NOTES-r3:107–108).
- No computation on any OI rule (LD:15–16); AL's conditional dichotomy is an expectation for the
  separately authorized mixed-path unit and is not written into its preregistration (owner decision
  Q3).

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #868. Model acceptance is evidence of review, not independent mathematical
verification (#1169 comment 6865680499). This plan authorizes no work. Each gap below remains open
until the evidence or decision named for it is recorded on `main`.

Here "independently verified" means verified from `main` to the standard for its kind, for example
kernel-checked or independently verified mathematically (§A.46 item 1); "partially verified" means
reviewed by at least one separate AI-agent reviewer, or resting in part on kernel-checked statements,
without independent mathematical verification of the result; "exploratory" means a result not
reviewed by anyone but its writer, or a proposal that claims no result; "known-invalid" means refuted
on `main` by a counterexample or disproof.

- **Independently verified:** none of the record's own results. Its [K] items (`Equivalence.lean`
  :245, :294, :422, :462) are Lean statements on `main`, read, not rebuilt.
- **Known-invalid:** none in r3. In r1, kept as the review trail, `REVIEW-r1.md` C6 shows that r1:150–151
  ("The edge `λ_A0 → r_B` breaks symmetrized (Sep) but not directed (Sep)") is false as stated, C7
  that r1:170's reading of the control `R_A ∋ r_B` is wrong, and C1 that r1's "extends OA2 Corollary
  E2" misstates the relation. r2 and r3 replace them; the r1 statements are not results of the record.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Stages 0–4, designed witnesses | partially verified; designed maps, not OI rules | [A] hand checks, re-checked in REVIEW-r1; [K], [P] | independent mathematical verification | an independent mathematical verification recorded on `main` (for example a human review) |
| Stages 5–6 | partially verified; conditional on the controlling condition | [A] on Bell-scope Theorem N/N′ and §4 [A] and SB L3 [A] | as for stages 0–4, and the same for Bell-scope and SB L3 | as for stages 0–4; the Bell-scope and SB L3 remediations |
| Stage 7 | classification; undetermined | Main:360 [P]; N4 (#1274) | — | an OI-sourced selector (LD:271); remains open under #868 |
| Proposition AL | partially verified; conditional on (AL1)–(AL4), (NS) | [A]; steps re-derived in REVIEW-r1; ChatGPT check | independent mathematical verification | an independent mathematical verification recorded on `main` (for example a kernel formalization over finite abelian groups, or a human review); a further §A.31 pass on the (AL4) convention |
| **Histories** witness | partially verified | [A], reviewer's witness, re-checked by the writer | as for AL | as for AL |
| Controls §3 | partially verified | [A] | as for stages 0–4 | as for stages 0–4 |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

## Dependencies

The record's own table (LD:288–304) classifies each reference against `main` at `c3b5f37a`. At the
package landing, after #1274 has landed:

| Reference | Classification at landing |
| --- | --- |
| Bell-scope r2 at `e1534b08` (Theorem N, N′, (Rec), §4, §3.5 item 5, NBA) | Support on `main`: lands in the same merge. Lemma G, listed at LD:298, is not used. |
| SB L3 (S:167–171 at `86a413c8`) | Support on `main` in `SB-L3.md`, landed in the same merge. Its extension to Theorem N′, used by the (MI\*) branch of LD:57–60, is a marked addition there. |
| SB routes A/B/C (S:177–181), N3 (S:189), N4 (S:190) at `86a413c8` | Support on `main` in #1274's `NEW-RESULTS.md` at `fef94857`: :490–494, :508, :509, with the re-pins and wording changes stated there. |
| SB:220 | Provenance: an example of a prediction an escape would need (LD:283); no verdict uses it. |
| QH at `ffc9cda4`, QH:213–214 | Provenance. |
| QH at `ffc9cda4`, QH:68–97 | Support off `main`, closed by narrowing: see "Superseded lines". |
| RC at `9f7d2612` | Provenance (LD:301); the Q1/Q2 vocabulary is restated on `main` in #1274's `NEW-RESULTS.md` §0.1. |
| Reviews 5857227567, 5857981727, 5858000929, 5859960068, 5891666660, 5897397957, 5891524305, 5892919040 | Review provenance. |
| #868 c.6854708572, c.6794392080, c.6873193841; #1273 c.6860580909 | Governance provenance, quoted above. |
| Commits `b8096c79`, `c4781c93`, `d8e4f80e` | On `main` once the package lands by merge commit. |
| #1283 at `f57e576a` | Provenance until adopted (see Landing). |

**N4 at its carried scope.** #1274 carries N4 (OC:509) for routes A, B and C with measurement
independence kept. Two uses in the record reach beyond that scope:
- LD:104: "In the relaxed class PR (CHSH 4) is reachable (Main:360) and no selector is supplied (SB
  N4, SB:190)." The relaxed class includes the measurement-dependent branch, which N4 does not cover
  at `86a413c8` or at `fef94857`. For that branch the statement rests on Main:360 [P] ("Bare finite
  OI representability is too broad to select the quantum Bell set").
- LD:271: "an OI-sourced principle, independent of the target table, that bounds CHSH by `2√2` and
  reaches it (SB N4)". N4 requires CHSH in `(2, 2√2]`; "and reaches it" is the record's own
  settlement criterion, not part of N4.

Neither changes a classification.

## Source drift from `c3b5f37a` to `main` (`c3b5f37a`)

None at this writing: the record's pin is the `main` commit against which this note is measured. It
is re-measured when the package is assembled (`LANDING-PLAN.md` §1, G2).

## Superseded lines in the accepted text

- Lines 3–6, "WIP / UNVERIFIED … pending ChatGPT review at the exact head", and line 273, "ChatGPT
  review pending": the ChatGPT review at the exact head is 5892919040, quoted above.
- Line 104, "The native encoded U′ composite reaches the non-quantum table SWAP/2 (QH:68–97) [D]",
  and line 300's "**support off `main`: gap** for the stage-7 illustration": QH stays off `main`. The
  sentence is context, not a result of the record; stage 7's classification rests on Main:360 and N4
  and does not use it. The clause "which is Bell-local over Pauli-axis product tests [A]" is the
  record's own observation about the SWAP/2 table.
- Lines 298–299: the gaps for Bell-scope, L3 and N4 close as stated under "Dependencies".
- Line 304 lists QH's ChatGPT review 5891666660 at `acf28d3a`; the later ChatGPT recheck 5897397957
  at `ffc9cda4` is ACCEPT with no change to QH's scientific verdicts.
- `NOTES-r3.md` line 1 calls the notes "not for landing"; they land as part of the review trail,
  because LD:240 and LD:274 cite them and the confirmations cite their lines. NOTES-r3:94–104 (owner
  questions) are answered by #1273 c.6860580909, and NOTES-r3:106, "No ChatGPT review yet", is
  answered by 5892919040.

## Landing

- **Together.** In one merge with Bell-scope r2 and `SB-L3.md`, after #1274 has landed
  (`LANDING-PLAN.md` §1).
- **Mode.** Merge commit of `d8e4f80e`, so that `b8096c79`, `c4781c93` and `d8e4f80e`, which the
  reviews name, remain ancestors of `main`.
- **Basis.** The proposed basis is §A.46 item 8 as drafted in #1283 at `f57e576a`, which is not
  adopted; the basis is open until #1283 is adopted. Record-specific check of the draft's conditions:
  - substantive, nonredundant result: met (Proposition AL; no two-wing coset result with an NS
    hypothesis was found on `main`, NOTES-r3:70–74; and the ladder classification);
  - scope and limits documented: met (LD §0, §4 scope limits, §5; this note);
  - independent non-author review and ChatGPT exact-head review: met for the record (REVIEW-r1,
    CONFIRM-r2, CONFIRM-r3; ChatGPT 5892919040 at `d8e4f80e`); this note and the package head need the
    package's checks and ChatGPT exact-head review;
  - accountable Issue, verification status, remediation plan: #868, this note;
  - explicit rationale: the owner's stated preference, #868 c.6873193841: "I prefer preserving the
    complete accepted Bell ladder rather than weakening its native result or leaving valid research
    indefinitely off `main`"; owner merge decision: not recorded.

  The record is preserved, not established (§A.46 item 1). Its removal is not automatic and is
  governed by §A.46 item 6.
- **Owner record.** #868 comment 6873193841, option (1). No merge decision is recorded.
