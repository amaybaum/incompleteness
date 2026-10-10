# Protocol — stage 6 (Q-EX-FULL), amendment 1: steps 2–4 (append-only; `PROTOCOL-STAGE6.md` unchanged)

Issued 2026-10-10 after the step-1 inventory threads I1–I4 reported and were audited
(`pt/audit/stage6-inputs/I-audit/AUDIT-I.md`). Base L = `9f9f8257…`, read-only. Research only; every hold of
`PROTOCOL-STAGE6.md` §0 stands (no repository change, no branch, no PR, no CI, no governed round, no publication,
no manuscript edit). Amendment-2 labels (DERIVED / CONDITIONAL / INDEPENDENT / UNRESOLVED) and the stage-6
record schema and do-not-assume list of `PROTOCOL-STAGE6.md` apply unchanged.

## A1.1 Working directories (checked absent at issue; absent from every manifest)

| step | thread | working directory | deliverables |
|---|---|---|---|
| 2 — dependency graph | G6 | `pt/G6/` | `GRAPH.md`, `graph.tsv`, `NOTES.md`, `RESULT.md`, scripts and outputs |
| 3 — countermodel reassessment | R6 | `pt/R6/` | `REASSESSMENT.md`, `NOTES.md`, `RESULT.md`, scripts and outputs |
| 4 — test of (b) against the complete applicable premises | T6 | `pt/T6/` | `TEST.md`, `NOTES.md`, `RESULT.md`, scripts and outputs |

A thread creates its directory and writes nothing else anywhere; if the directory already exists it stops and
reports without writing.

## A1.2 Inputs the step-2–4 threads read (in addition to `PROTOCOL-STAGE6.md` §2)

- The frozen step-1 records: `pt/I1/`, `pt/I2/`, `pt/I3/`, `pt/I4/` (INVENTORY.md, CENSUS.md, RESULT.md, NOTES.md
  and script outputs), and the coordinator's audit `pt/audit/stage6-inputs/I-audit/AUDIT-I.md` (§4 merge
  decisions and §5 findings are binding; the threads do not re-audit step 1).
- The audited stage-4 and stage-5 records: `pt/INTEGRATION-NOTE-STAGE4.md`, `pt/INTEGRATION-NOTE-STAGE5.md`,
  `pt/audit/Y/AUDIT-Y.md`, `pt/audit/Z/AUDIT-Z.md`, `pt/audit/D5/AUDIT-D.md`, `pt/audit/C5/AUDIT-C.md`, and the
  thread records `pt/Y/`, `pt/Z/`, `pt/D5/`, `pt/C5/` (read-only; their evidence quarantine copies under
  `pt/D5/evidence/` and `pt/C5/evidence/` are not data and are not read).
- The kernel, manuscripts and roadmap at L under `pt/base/`, read-only.

Never read: `pt/G6/`, `pt/R6/`, `pt/T6/` other than one's own; `pt/audit/stage3-inputs/OWNER-*`,
`pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, `pt/audit/stage6-inputs/OWNER-*`,
`pt/audit/reviews/`, `pt/audit/aborted-launches/`.

## A1.3 Sweeps

The start and end sweeps exclude `pt/G6/`, `pt/R6/`, `pt/T6/`, `pt/I1/`–`pt/I4/`, `pt/D5/`, `pt/C5/`, `pt/audit/`
and `pt/audit*-replay/`. The coordinator writes only under `pt/audit/` while these threads run; the files
`pt/INTEGRATION-NOTE-STAGE5.md`, `pt/audit/C5/AUDIT-C.md`, `pt/audit/D5/AUDIT-D.md` and this amendment with its
sidecar exist before the launch and are not anomalies.

## A1.4 Step 2 — the dependency graph (G6)

Nodes: every inventory record by id. Edges: `depends_on` as recorded, completed from the kernel where a record's
field is incomplete (a theorem's hypotheses are its declared arguments at L). Required outputs, in `GRAPH.md` with
the machine-readable `graph.tsv`:

1. The partition of the nodes into: (a) consequences of Axioms 1–2 alone; (b) consequences of Axioms 1–2 with
   C1–C4 (and which of C1–C4 each needs); (c) items needing an operational hypothesis (name it); (d) items needing a
   physical hypothesis (name it); (e) definitions and hypothesis-structures with no derivation at L.
2. For every do-not-assume item: its status at L and, where a theorem discharges it for a particular object, the
   object and the premises used.
3. The ancestor set of the pair-level objects (`W 3`, `K`, `cnot`, `actC`/`actT`, H1–H3, (b)) and the descendant
   set of Axioms 1–2, with the statement of where the two fail to meet (the absent bridges of AUDIT-I §5), each
   missing edge named by the obligation that would supply it (K2, P-STAGE2, P-ACT2, K∞-Act, K∞-Drive, …).
4. A check script: every edge target exists; no cycle; every proved-[K] node's recorded dependencies agree with
   its kernel signature on a sample of at least forty theorems drawn across the four inventories (list the sample
   and the rule before running).
5. No status changes; previously proved lemmas enter through their dependencies, never as independent premises.

## A1.5 Step 3 — countermodel reassessment (R6)

For each stage-4 alternative (the stage-3 cones K(E0), K(Z_F); the EXOTIC-E seeds of stage 4 Y/Z and of stage 5
C5; the torus and finite-group nodes), decide against every applicable inventory item (those with `bearing` other
than none at L, and every item whose statement reaches the pair cone through an existing bridge) whether the
alternative satisfies it, fails it, or is not reached by it (no bridge). Keep the hidden-history level (H) and the
composite-cone level (P) apart: an H-level item reaches a cone-level alternative only through a proved bridge; the
absence of a bridge is recorded as "not reached", never as "satisfied" or "failed". State explicitly for each
alternative whether any item at L excludes it, and whether a cone-level countermodel has, at L, any embedded-
observer realization claim attached (the owner's distinction: a cone-level countermodel does not by itself
establish a compatible embedded-observer realization, and the inventory is to say what L provides either way).
Exact scripts for every cone-level check; decision rules in headers before the first run.

## A1.6 Step 4 — the test of (b) (T6)

Determine whether the complete applicable premise set at L forces (b) in its weakest sufficient form ((b) for
{flow, J} on one token, or (b) for the drive with the phase flow on one token; `pt/INTEGRATION-NOTE-STAGE5.md` §2).
Outcomes: DERIVATION (a chain from inventory items at their actual status, each step [K], [W] or [X], with the
disguise test of `PROTOCOL-STAGE5.md` applied to every premise used) or INDEPENDENCE (a countermodel satisfying
every applicable inventory item at L — every item that reaches the pair cone — and violating (b), with the
missing assumption isolated and stated as the exact content that would close the gap). A failed derivation alone
is UNRESOLVED. No do-not-assume item enters as a premise. Exact scripts; decision rules in headers before the
first run.

## A1.7 Common rules

As `PROTOCOL-STAGE6.md` §3–§5: write-in-parts of at most 250 lines per write; `python3 -I -B` for every script;
`.out`/`.err` with the exit marker; failed runs kept as `.runN.*`; byte-identical replays; start and end markers
with the integrity checks; NOTES.md as a running record with UTC times from `date -u`; RESULT.md last, with the
sha256 of every file written; productivity test and decision vocabulary fixed before the first node; depth-first.
