## §A.37 Round lifecycle before V3 (record)

This section is a record. It governs no new round and provides for none: every round begun after
`V3-11`'s landing runs under §A.39. It keeps what is needed to read the records of the rounds that
landed before V3, each of which keeps the protocol under which it landed. The full text of this
section as it governed those rounds is `AGENTS.md` at `f9a9acaa44e4982d7814200c46bf1da222b4cbfc`,
and each round's own frozen chronology control states its shape in terms; a preregistration is not
reinterpreted after its outcome is known.

### How those rounds ran

The earliest rounds ran in three pull requests: a control plane carrying the preregistration
alone, an execution, and a separate landing. From this section's adoption they ran in two: the
control plane, then one execution pull request that, once its head was certified, carried the
landing as well. The control plane was reviewed, amended before its merge and only then, and
merged before any execution object existed; merged, it was immutable, and an execution that
diverged from it recorded the discrepancy rather than repairing the freeze. Its merge commit was
the mandated execution base, from which the execution branched and from nothing else.

Before certification an execution never absorbed later main: no merge from main, no rebase, no
amend, no force-push. Certification fixed the sealed execution commit, which never changed. The
landing merge took current green main as first parent and exactly that commit as second, with
conflicts resolved in the landing and never in the sealed commit. A **sealing** round, one whose
preregistration prospectively owned seal state, then took a pin commit that recorded its sealed
head and landing merge; a **non-sealing** round took the landing alone. Freezes written before
that wording say **guarded** and **unguarded** for the same distinction, and keep the meaning
their own chronology controls fix.

### The vocabulary of their records

- `D` — the drafting snapshot: the commit against which a control plane was written and its
  drafting-time measurements taken. Never the mandated execution base merely because the control
  plane was drafted from it.
- `B` — the mandated execution base: the certified merge commit on `main` of the latest
  control-plane artifact governing the round, the preregistration or its latest
  execution-affecting append-only amendment.
- `M` — a candidate control-plane merge, built by continuous integration to test `B`-scoped
  conditions before `B` existed; predictive test state only.
- `E` — the sealed execution commit, certified at its exact head.
- `L` — the landing merge, first parent main and second parent `E`.
- `P` — a sealing round's pin commit, after `L`.
- **execution mode** and **archive mode** — the guard's two ancestry checks for a sealing round:
  against its base while it executed, and, once pinned, against the sealed object, whose pinned
  merge's second parent had to equal the sealed head.
- **seal records** — from `SI-2`'s landing, one JSON record per round under
  `verification/seals/`: `kind: "sealed"` with `base`, `sealed_head` and `merge`, or
  `kind: "base-only"` with `base` alone. Before `SI-2` the same state was legacy constants in the
  guard file, which `SI-3` removed.
- **`control-plane-preconditions` blocks** — rows scoped at `D`, at `B` or from `D` to `B`,
  which a control plane could carry for mechanical checking.

### Their records now

The records of those rounds — their preregistrations, amendments, result notes, seal records under
`verification/seals/` and `V2` certificates under `verification/certificates/` — are listed with
their blobs in `verification/infrastructure/legacy-records.json`, and the release gate's
`legacy-records` step keeps every one unchanged and admits no new file under a closed namespace
(§A.39). The mechanisms that checked their chronology at every later head — the guard's ancestry
and seal clauses, the control-plane base check and lint, and the `V2` certificate verifier — were
retired by round `V3-13`, whose preregistration lists what each checked and what now protects it.

A question one of those rounds left open, or froze and never executed, is taken up by a new native
round, which cites the old freeze as provenance and leaves the old record as it stands.
