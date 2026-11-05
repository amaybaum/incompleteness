# K1-RDY pre-freeze proofs (#1031)

**Status: written proofs, not independently reviewed. WIP / UNVERIFIED.** This directory decides no gate, token,
readiness result or owner question, and changes no statement of the K1-RDY text. It authorizes nothing.

## Purpose

`verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md` (on `main` at `4f016afd`) proves the
blindness lemma, the P1 lemma and L-O(i)/(ii), and its §5 item 3 lists what the K1-RDY text uses without proof there.
The owner's direction, #1031 comment 6653233009 (amaybaum, Claude Code session chat, 2026-11-05): "There is one
important additional point: #1119 does not prove that the complete decision procedure in #1031 is correct. In
particular, the rule for classifying all invariant probability measures still needs separate justification or
validation. That should be explicitly checked before the next research round is frozen." `PROOFS.md` treats each item,
and the ledger bounds (c1)/(c2):

| Item | Text lines | `PROOFS.md` |
|---|---|---|
| `E` at the instance | 198 | §1, proved |
| cycle decomposition of `φ` at the instance | 191, 270 | §2, proved (156 cycles) |
| P3's image at `t_0` | 86–90 | §3, proved |
| TA (c4) | 206, 234, 243 | §4, proved |
| ℰ conservation and shell count | 74, 209 | §5, proved |
| ledger bounds (c1)/(c2) | 60–62, 142, 244 | §7, proved |
| §5.3's class rule (Q4) | 156–163 | §6: the positive clause is sufficient and the ABSENT clause exact; the converse of the positive clause is not established; at the instance the clause is unreachable, so no token depends on it |

The gates that precede G4 are not premises; they are decided by the round's own procedure at execution.

## Limits

- Hand derivations only. No enumeration, model computation, Lean run or workflow dispatch was used; enumeration before
  `F` is not authorized (#1031 comment 6651204512).
- Until an independent review of these proofs is recorded on `main`, no result here is established (`AGENTS.md` §A.46
  items 1 and 7).
- The statements are reproduced from the text, which is not on `main`; that they are the text's is checkable against
  its recorded sha256 once lines 1–313 are on `main`.
- §6 identifies a gap in the class rule's claimed equivalence (CR-5) and proposes no change to the text. Whether the
  rule is restated is an owner decision.
