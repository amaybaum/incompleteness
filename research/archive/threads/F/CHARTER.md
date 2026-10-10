# Thread F — KInf1 dependency ledger (read-only research; charter as directed by the owner, 2026-10-01)

## Deliverable
A dependency ledger for the landed hypothesis `KInf1`, not a proof attempt. Expand the landed definition
(`verification/lean-mathlib/OIBridge/KInfFoundations.lean`, `def KInf1`, at main `6d0abf6b`) into atomic
obligations and trace every conjunct backward until it reaches exactly one of:
- an already-certified kernel theorem (exact identifier, module, line at `6d0abf6b`);
- an explicitly assumed reconstruction premise (exact place it is stated in the corpus);
- a genuinely missing implication.

Ledger columns: KInf1 clause → exact Lean definition/theorem → immediate dependency → upstream source/provenance
→ status (PROVED, DERIVABLE, OPEN, OUTSIDE-KInf1) → proposed bridge theorem → countercontrol.

It must decide, with reasons, whether relative strict convexity, composition/copy structure (copy naturality), and
the gbit/rebit exclusions lie on the KInf1 path or belong to later reconstruction stages.

Finish with: a dependency graph; a recommended theorem order; and a summary of the form "Of N atomic obligations in
KInf1, X are already discharged, Y follow from these specific bridge lemmas, and Z remain genuinely open;
geometry/composition/exclusions belong at these exact positions." No formal round is proposed in this thread.

## Research limits (frozen)
1. Read-only against certified main = 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a.
2. Inspect, compute and draft only.
3. No branches, PRs, freezes, round records, receipts, ROADMAP edits or manuscript edits.
4. No new axiom or premise may be introduced to make a proof go through.
5. If a purported implication fails, produce the smallest explicit countermodel and identify the missing premise.
6. Separate logical necessity for KInf1 from later reconstruction convenience.
7. Do not promote written arguments to kernel results: a status of PROVED requires an exact kernel identifier;
   a written argument is at most DERIVABLE (with the bridge lemma named) and says so.
8. Finish with a dependency graph and a recommended theorem order before any formal round is proposed.

## Evidence levels used in the ledger
kernel (landed Lean identifier) / exact computation (script in this directory, exact arithmetic) / written argument
/ citation. They do not substitute for one another.

## Review order for the ledger (owner, 2026-10-01; applied by the reviewer, not the thread)
1. The unfolding of KInf1 is complete: no hidden conjuncts or imported assumptions.
2. Every PROVED row names an actual landed kernel theorem (identifier checked at 6d0abf6b).
3. Genuine KInf1 obligations are separated from later reconstruction premises.
4. Dependency collapse: check whether several OPEN rows follow from one missing bridge theorem.
5. Only then choose the smallest successor formal round.

## Disposition (owner, 2026-10-01)
The cheap bridge-lemma round is PARKED. B1, B5, B6, B7, B8 and B11 (LEDGER.md §B) are preserved here and are to be
bundled into the eventual substantive round once P2 has a viable definition. K∞-R (D2–D9, drivability sourcing) is a
separate research target, not mixed into Thread G. Next: Thread G, effect-family reconstruction (P2/O1).
