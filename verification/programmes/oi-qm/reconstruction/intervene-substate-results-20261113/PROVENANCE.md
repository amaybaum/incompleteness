# Provenance of the option-(c) landing package

## 1. Source objects

| Object | PR (state at writing) | Branch @ commit | Parent / base | File (blob, sha256) |
|---|---|---|---|---|
| INTERVENE-1 unit 1, draft r2 | #1230 (open, draft) | `research/intervene-1-20261111` @ `ea12fde1bbc4b546f4690bf89817971796aeb501` (2026-11-11T10:35:27Z) | parent `592fede0` (r1); base `cac5d264` | `verification/programmes/oi-qm/reconstruction/drafts/intervene-1-20261111/INTERVENE-UNIT1.md` (blob `06f148e0b3d529659608a1bf6150a7ce6b124cb0`, sha256 `5edb4ad3c0489163af8ab2e017ec6c651611506f4f7633d411137d2de4edd7fd`) |
| SUBSTATE-BRIDGE-1 unit 1, draft r2 | #1232 (open, draft) | `research/substate-bridge-1-20261111` @ `86a413c88cd14d344aa41b6f47885aeb24da6910` (2026-11-11T11:43:47Z) | parent `b94b283a` (r1); base `cac5d264` | `verification/programmes/oi-qm/reconstruction/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md` (blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`, sha256 `662b9cbaab4237a357174b675c7ee7734c4d4512ef68d530555111230bde48fd`); `probes/generic_substate_checks.py` (blob `fa434cd4`, sha256 `d269224f…bbb99`), `.out` (blob `3861f1b0`, sha256 `9845ed1e…644ee`) |
| Reconciliation r3 with its review records | #1271 (open, draft) | `research/reconcile-1230-1232-20261113` @ `703ae20e57f9ffeb0eb458ec688883b3fc64a632` (2026-11-13T13:56:24Z) | parent `1d3c4599` (r3); ancestor `b36bba60` (r1, review, r2); base `main` `c3b5f37a` | `verification/programmes/oi-qm/reconstruction/drafts/reconcile-1230-1232-20261113/RECONCILE-r3.md` (blob `1dc565f3`, sha256 `1b68c7c5…fd839`), `REVIEW-r1.md` (blob `7f391a9d`, sha256 `4fbcf865…13373`), `CONFIRM-r2.md` (blob `11a4d663`, sha256 `bf6a3828…0277b`) |
| `main` (reference corpus) | — | `c3b5f37a354bb26437e2e0165c576a347a63c153` (merge of #1265, 2026-11-13) | — | everything cited as "on `main`" |

Each branch was fetched by name and read only. The heads above equal the heads of #1230, #1232 and
#1271 at the time of writing. Nothing was written to any of these branches.

Read for cross-checks only: APPROX r4a (#1221, `e41cf613`), BRIDGE-UNIT1 and APPROX r2
(`ccr-9c2ecca4-vkb666` @ `820519cf`), Bell-scope r2 (#1231, `e1534b08`), REC-1 r7
(`research/rec-1-1169-20261113` @ `9f7d2612`; that branch's head is `cd38655c` at writing, and
`REC-1-r7.md` is unchanged between them).

## 2. Review trail of the drafts

| Draft | Review | Object | Verdict |
|---|---|---|---|
| INTERVENE-1 r1 | ChatGPT review 5857231398 | `592fede0` | REVISE |
| INTERVENE-1 r2 | ChatGPT review 5857985732 (posted under `amaybaum`, 2026-11-11T11:25:22Z) | `ea12fde1` | ACCEPT WITH DOCUMENTATION NITS (conditional paper result); four nonblocking nits |
| SUBSTATE-BRIDGE-1 r1 | ChatGPT review 5858000929 | `b94b283a` | REVISE |
| SUBSTATE-BRIDGE-1 r2 | ChatGPT review 5859960068 (posted under `amaybaum`, 2026-11-11T14:03:54Z) | `86a413c8` | ACCEPT WITH NITS; "OI-wide verdict remains INDETERMINATE"; three nonblocking nits |

The r1 verdicts are as recorded in the reconciliation (R3:17–18); the r2 reviews were read through
the host API.

## 3. Reconciliation acceptance trail (#1271)

1. **Authority.** #1169 c.6854241002 (account `amaybaum`, 2026-11-13T13:24:47Z), as quoted in
   R3:8–11: "A read-only review and reconciliation of the existing INTERVENE-1 and SUBSTATE-BRIDGE
   paper drafts. No new derivations. No writes to those PRs' branches."
2. **RECONCILE r1** (sha256 `05ad46b2…`).
3. **REVIEW-r1**: independent non-author model review, ACCEPT WITH CHANGES, findings A–J and 20
   replacements; T5 re-checked against the Lean source (RV:47–62).
4. **RESPONSE-r1 and RECONCILE r2**: the 20 replacements applied, one in modified form, and one
   owner-guidance paragraph ("Conclusion, at its exact strength") added.
5. **CONFIRM-r2**: focused confirmation, ACCEPT WITH CHANGES (two strings in the added paragraph).
6. **RECONCILE r3**: r2 with the two replacements; nothing else changed (OBJECTS.md).
7. **ChatGPT review 5892291246** (posted under `amaybaum`, 2026-11-13T14:00:42Z) at `703ae20e`:
   "ACCEPT WITH INTEGRATION NITS (for the bounded reconciliation record only). Not a merge approval
   or physical-operation finding." Its two integration nits are answered in §5 below.

The reconciliation and its reviews are model-written and are not verification (§A.46 item 7).

## 4. Owner decisions

- **#1169 c.6854728636** (author `amaybaum`, 2026-11-13T13:45:13Z), quoted: "**INTERVENE-1 (#1230)
  and SUBSTATE-BRIDGE-1 (#1232):** "Adopt (c) (Recommended)" (amaybaum, 2026-11-13). The writer is
  this session." Step 2: "A writer pass that corrects the four inconsistencies, with no
  mathematical change". Step 3: "A minimal landing package containing only the results not already
  on `main`." It also records: "Results already on `main` are referenced, not duplicated. REC-1
  references the non-spanning results; it does not absorb their proofs. Merging is a separate
  decision." and, for the Bell ladder (#868 c.6854708572): "It takes the A/B/C classification and
  SLL as inputs, without re-deriving them."
- **#1169 c.6855167580** (author `amaybaum`, 2026-11-13T14:02:39Z), quoted: "**Owner decision**
  (amaybaum, 2026-11-13): "Corrected set (Recommended)". It replaces the landing list in
  c.6854728636, following the reconciliation r3 (#1271 at `703ae20e`) and ChatGPT review 5892291246
  (ACCEPT WITH INTEGRATION NITS)." The package "carries: INTERVENE-1 T5 part (c) only. Parts (a),
  (b) and (d) are already in APPROX r4a. SUBSTATE-BRIDGE-1 G1/E2, and E1's generality. L1/L4 for
  infinite site groups. The A/B/C Bell-route classification, with SLL kept as an open obligation.
  (NS_A), with its countercontrol S7." "**Excluded:** T7(b). It is the kernel theorem
  `realized_of_instAvail` (ImplementationLocality:530), already on `main`." Process: "The package
  records its provenance: the draft heads `ea12fde1` and `86a413c8`." "A fresh independent review at
  the exact head." "Merging is a separate owner decision. AW-OA2-1 stays stopped, and priorities are
  unchanged."

**Supersession.** c.6855167580 replaces the landing list of c.6854728636. The earlier list named
T7(b) and did not name (NS_A)/S7; the package follows the later list, which omits T7(b) and names
(NS_A) with S7. This answers the first integration nit of review 5892291246 ("The writer should
record that supersession explicitly; do not silently enlarge the landing to include (NS_A)/S7
without confirming it is inside the owner's selected file set"): (NS_A)/S7 is in the owner's set by
c.6855167580.

**Authorization of the drafts themselves.** The PR bodies of #1230 and #1232 cite owner approvals of
2026-11-11 that the reconciliation could not locate (R3:107); c.6854728636 step 5 asks for a current
owner decision to replace them. No such decision is recorded on #1169 up to c.6855167580.
c.6855167580 is the recorded authorization of this writer pass, not of those drafts, and it does
not authorize a merge.

## 5. The reconciliation's drafting-history wording

RECONCILE-r3's standing paragraph (R3:3–6) reads "Nothing was committed, pushed, posted or
dispatched. It is a working record, not yet on any branch". That wording describes the record when
it was first drafted. It is historical provenance, not current state: the record is committed on
`research/reconcile-1230-1232-20261113` at `703ae20e` and is the head of the draft PR #1271, where
review 5892291246 read it at that exact head. The same holds for the "not committed or pushed"
statements in RESPONSE-r1 and CONFIRM-r2, which describe the session in which each was written. The
original options table of RECONCILE-r3 (R3:160–170) keeps its pre-decision wording; the adoption of
option (c) is recorded on #1169 (§4).

## 6. How the package was produced

Paper-only. The drafts' scripts (`checks.py`, `generic_substate_checks.py`) were read, not run; no
computation on any OI rule was made. The arithmetic behind the [X] tags carried in `NEW-RESULTS.md`
was checked by hand there. Nothing was committed, pushed or posted in producing the package; its
landing, the fresh exact-head review and any merge are separate steps under the owner decisions
above.
