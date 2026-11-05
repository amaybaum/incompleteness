# K1-RDY-1: proposed V3 supersession and amendments (for independent review)

**Status: proposal for independent review. WIP / UNVERIFIED. Nothing here is adopted, frozen or designated.** The
files under `proposed-k1-rdy-1/` are drafts of the round's control-plane files. They are not a round's record and no
pull request carries them as one. `PREREG-RECOVERED.md` is unchanged (sha256 `a93f3f33…`, 313 lines), and lines 1–313
of `proposed-k1-rdy-1/preregistration.md` are byte-identical to it.

**Authorization.** Owner, #1031 comment 6651204512 (amaybaum, 2026-11-05T06:15:48Z): "Prepare the proposed V3
supersession and amendments for independent review." The same record adopts K-1 to K-18, D-07(a), O-1(b), O-2 KEEP and
O-3 CONFIRM prospectively, rules A4 option (a), and does not authorize enumeration before `F`. Not authorized: `F`
designation, dispatch, freeze, execution, merge.

## 1. File map

| Path (under `verification/programmes/oi-qm/reconstruction/`) | Branch | Content |
|---|---|---|
| `k1-rdy-20261105/proposed-k1-rdy-1/preregistration.md` | this branch (#1114) | lines 1–313: the accepted text, byte for byte; §12: base, standing, precedence, the owner record in force, support on `main`, governed paths, the `v3-round` and `v3-governed-paths` blocks |
| `k1-rdy-20261105/proposed-k1-rdy-1/amendments/A1`–`A9` | this branch | the amendments of §3 |
| `k1-rdy-20261105/SUPERSESSION.md` | this branch | this file |
| `k1-rdy-pref-proofs-20261105/PROOFS.md`, `README.md` | `evidence/k1-rdy-pref-proofs-20261105`, from `main` `4f016afd` | written proofs of the pre-freeze items (§4), for review and a narrowly scoped landing before `D` |
| `k1-rdy-proofs-20261105/LEMMAS.md` | `main` at `4f016afd` (#1119) | the four lemma proofs |

## 2. What the supersession replaces, and why

- **The base's standing.** Lines 3–5 state "Not frozen, not an `F` candidate", the standing on 2026-11-02. A native
  freeze needs a new round from a fresh `D` with an explicit supersession of that standing (owner interim ruling, #1031
  comment 6650824861: "A native V3 freeze requires a new compliant round from a fresh `D`, with an explicit amendment or
  supersession of the recovered draft's historical non-freeze status"). §12 records the standing as historical and makes
  lines 1–313, §12 and the amendments the round's preregistration at the owner-designated `F`.
- **The attribution of decisions.** Lines 6, 44, 84, 123–124, 130, 144 and 288 call coordinating-session decisions
  "owner decisions". The owner adopted them prospectively without retroactive attribution. A1 gives the reading and
  quotes every adopted decision verbatim, so their text is on `main` once the round lands.
- **The hold mechanism.** Lines 229 and 263 rest on formal holds that `AGENTS.md` §A.45 rule 7 retired; A4 applies
  the owner's option (a).
- **Off-`main` support.** The lemmas, TA (c4), HC-1 and the anchors are traced under §A.42 item 8 (A5, A3, A6, A7), with
  the support moved to `main` (`LEMMAS.md`, and `PROOFS.md` once landed).
- **Rules the text leaves underdetermined.** The P1 class token's fields (A2, as the owner directed), the union clause's
  scope (A8) and the gate table's schema (A9, which §A.44 requires of a control plane not yet at `F`).

No line of 1–313 is edited; each change is an amendment that names the lines it governs.

## 3. Amendments

| File | Governs (base lines) | Content | Source |
|---|---|---|---|
| `A1-attribution.md` | 6, 44, 84, 123–124, 130, 144, 286, 288 | "owner decision" reads as the prospective adoption of 2026-11-05; the adopted form of D-07(a) and O-3; the adopted decisions and the documented owner decisions the base cites, quoted verbatim | #1031 comment 6651204512; #1114 SOURCES C-2, C-3 |
| `A2-class-token-fields.md` | 156–159 | list-order "first"; the class token's fields; member order reporting-only, with a cell order | owner direction #1031 comment 6649717044; #1114 review ruling on A-1 (PF-1) |
| `A3-equal-time-independence.md` | 206, 234, 243 | TA (c4) replaced by Proposition IND, proved in `PROOFS.md` §4 | PF-2 |
| `A4-historical-heads.md` | 229, 263 | holds retired by §A.45 rule 7; heads recorded, a mismatch recorded and not VOID[stage], with the material-change stop | owner, #1031 comment 6651204512 (A4 option (a)) |
| `A5-lemmas.md` | 95, 97–114, 163, 244–245 | support in `LEMMAS.md`; line 163 subject to precedence; CC-SCOPE in all branches | #1119; option 1b |
| `A6-disclosure.md` | 252, 303–313 | evaluations before acceptance disclosed; HC-1 and HC-A–HC-D provenance; control values derived on paper | P-5; P-3 |
| `A7-reference-trace.md` | none (adds a table) | §A.42 item 8 classification of every off-`main` reference, with the stated differences of `main` from the anchors | §A.42 item 8; §A.46 item 7 |
| `A8-class-rule-scope.md` | 159–162 | reading of "every weighting supported on `C`"; the clause unreachable at the instance; what its outcomes establish | `PROOFS.md` §6 |
| `A9-gate-table-schema.md` | 192–194 | `gate-table.json` and its fields | §A.44 |

None carries a `v3-round` or `v3-governed-paths` block or a near miss of one (`K2`, `G10`).

## 4. Pre-freeze justification of each premise

`LEMMAS.md` §5 item 3 lists what the text uses and #1119 does not prove. The owner's direction, #1031 comment
6653233009 (amaybaum, Claude Code session chat, 2026-11-05), requires the check: "#1119 does not prove that the complete
decision procedure in #1031 is correct. In particular, the rule for classifying all invariant probability measures
still needs separate justification or validation. That should be explicitly checked before the next research round is
frozen." Each item, and each other premise that rests
on off-`main` content, is justified before `F` in one of three ways: a written paper proof to be reviewed, an on-`main`
result cited, or a named hypothesis or control carried by the round. None is resolved by computation.

| Premise | Used at (base lines) | Justification before `F` | Kind | Where |
|---|---|---|---|---|
| blindness lemma, P1 lemma, L-O(i), L-O(ii) | 95–114, 163, 208, 244 | `LEMMAS.md` §1–§4 at `4f016afd`; its review is PR #1119 comment 6651717259 and the delta check, not yet recorded on `main` (decision OD-2) | on-`main` result | A5 |
| the classification of all invariant probability measures | 72–73 (K-17(a)) | Lemma P1(a), `LEMMAS.md` §1 | on-`main` result | A5 |
| §5.3's class rule (Q4) | 156–163, 236 | `PROOFS.md` §6: the positive clause is sufficient (CR-3), the ABSENT clause exact (CR-4), the converse not established (CR-5), the clause unreachable at the instance because `δ_0`'s member row is non-positive in every branch (CR-6) | written proof, to be reviewed; scope carried by A8 | A8 |
| the cycle decomposition of `φ` at the instance | 191, 270 | `PROOFS.md` §2: 156 cycles; also carried as line 270's checkpoint | written proof, to be reviewed; named checkpoint | — |
| P3's explicit image | 86–90, 131–133, 235 | `PROOFS.md` §3; G2(b) recomputes it from the rule at execution (T2) | written proof, to be reviewed; control | — |
| the gates before G4 for a member row | 163, 232–236 | not a premise: decided at execution by G1–G3 and recorded per row in the gate table (A9), under the precedence of lines 136–138 and 182–183 (A5). The non-positivity of `δ_0`'s row needs no G1–G3 outcome (`PROOFS.md` CR-6) | carried by the round | A5, A9 |
| TA (c4) | 206, 234, 243 | `PROOFS.md` §4, Proposition IND | written proof, to be reviewed | A3 |
| the conservation of ℰ and its shells | 74, 209, 244 | `PROOFS.md` §5; SM:294–296 at `07d94f2c` states the conservation | written proof, to be reviewed; on-`main` statement | A7 |
| `E` at the instance | 198 | `PROOFS.md` §1 | written proof, to be reviewed | A6 |
| the ledger bounds (c1)/(c2) | 60–62, 139–142, 243–244 | `PROOFS.md` §7, Proposition LEDGER; MR-pre:184–187 (on `main`) states only the entropy invariance I1 | written proof, to be reviewed | A7 |
| the anchors Main:56, Main:62, Main §4.6, Main:760, MR★:462–483, MR-pre:137–165 | 10–12 and throughout | `07d94f2c`, `af1e9be2`, both reachable from `main`; differences on `main` stated in A7 | on-`main` result | A7 |
| H-μ, H-sel, H-inv, H-law, H-ret, H-2s (declared), H-cur (declared), (EM), the finite-`S` posit | §3, §5 | named hypotheses listed in each row's `Λ` (G5) | named hypotheses | base §2, §3, §5.2 |
| HC-1 | 201, 206, 209, 303–310 | provenance only; its values are derived in `PROOFS.md` §1, §4, §5 | — | A6 |

## 5. What remains before `F`

1. Independent review of this proposal, of `PROOFS.md` and of the §12 wording.
2. Landing of `PROOFS.md` on `main` through a separately approved, narrowly scoped pull request, and of a record of the
   #1119 proof review (OD-1, OD-2). Then the placeholders marked `‹to be filled before F: …›` (§12; A5) are filled, and A4's heads are re-read and
   entered in the last control-plane commit before `F`.
3. The round's guiding draft pull request from a fresh `D`, at or after those landings. Its first commit copies
   `proposed-k1-rdy-1/` byte for byte, as revised by review, into `round-k1-rdy-1/`; every later commit before `F` is
   single-parent and changes only those control-plane files (`AGENTS.md` §A.39, §A.43 item 1; architecture `G9`).
4. The exact-head `check-run` on the candidate `F` and the owner's designation (§A.39). Each needs owner approval.

These drafts are kept on #1114's branch, a linked research branch, because §A.43 item 1 admits only control-plane
commits on a round's pull request before `F`, and because the round's `D` should postdate the landings of item 2.

## 6. Owner decisions needed

| Id | Question | Recommendation |
|---|---|---|
| OD-1 | Land `PROOFS.md` (pre-freeze proofs) on `main` before `D`, after its independent review, through a narrowly scoped pull request like #1119? | Yes. Several premises of §4 then rest on `main`, and the round's `D` can postdate the landing |
| OD-2 | Record the #1119 proof review on `main`? `LEMMAS.md` still marks every proof "written proof, not independently reviewed", and the review (#1119 comment 6651717259) and its delta check are off `main` | Yes: a verbatim review record with author and time in `k1-rdy-proofs-20261105/`, and the status lines corrected in place, in the same pull request as OD-1. Without it the lemmas are not established under §A.46 items 1 and 7, and the owner's "remain conditional until those proofs pass review" stays open on `main` |
| OD-3 | §5.3's union clause: keep it with A8's scope statement, or restate it in the `∀λ ∃w` form? | Keep it with A8. The clause is unreachable at this instance (CR-6), so no token depends on the choice; a restatement would edit accepted text for no effect here |
| OD-4 | Execution mode: paper-only, as drafted, or reserve an enumeration tool's path as an `execution` entry at `F` (paths are fixed at `F`, `G7`; an execution path cannot lie in the record directory, `G6`)? | Paper-only for K1-RDY-1, with this cost. Any P1 member row (`π_0` and 156 cycle-uniform members per branch) that the paper derivations do not decide makes that branch's class token UNDECIDED(Gk), because UNDECIDED precedes ABSENT and BLIND in A2's order; that removes the content line 238 calls informative. Any S0 control left undecided gives VOID[stage] for the whole round. The alternative is to reserve an execution path at `F`: the reservation authorizes nothing, since execution still needs the #1031 gate-3 authorization naming the exact tools, inputs and scope (#1031 comment 6651204512), but the tool would have to exist and be reviewed before `F`. The recommendation stands because it matches K-10 and the owner's ruling, and because the cycle decomposition (`PROOFS.md` §2) gives the member list on paper; the trade-off is the owner's |
| OD-5 | Adopt A2's field definitions and cell order? | Yes. The owner directed that "first" be resolved before freeze; A2 also fixes the fields the #1114 review found undefined |
| OD-6 | Adopt A9's schema? | Yes. §A.44 requires a stated schema for a control plane not yet at `F` |
| OD-7 | #1114's disposition once the round's pull request opens | Keep #1114 as the research record until the round lands, then close it without merge, keeping its branch (§A.43 item 6); the round's record carries lines 1–313 |

The coordinating session is told before any pull request is opened.
