"""Scratch: V3-13's edits to verification/infrastructure/v3/architecture.md. Never landed as is."""

SPEC = 'verification/infrastructure/v3/architecture.md'
SPEC_EDITS = [
("""five gaps round `V3-3` recorded, `G8` to `G12`. Each settlement is normative text under its
identifier. The specification is operative for every round begun after round `V3-11`'s landing that the
owner does not designate a compatibility round under `AGENTS.md` §A.37, and for the provisional
pilots `V3-10` and `V3-11` under `AGENTS.md` §A.39. A round begun earlier keeps the protocol under
which it landed, and no `V1` or `V2` state is changed or migrated by the specification.
""",
"""five gaps round `V3-3` recorded, `G8` to `G12`. Round `V3-13`, under the frozen preregistration
`verification/infrastructure/round-v3-13-retirement/preregistration.md`, restated `G12` and settled
`G13`. Each settlement is normative text under its identifier. The specification governs every
round begun after round `V3-11`'s landing, and the provisional pilots `V3-10` and `V3-11`, under
`AGENTS.md` §A.39. A round begun earlier keeps the protocol under which it landed, and no `V1` or
`V2` state is changed or migrated by the specification.
"""),
("""| `G12` | the seal record | `G12`, under `S7`; lifecycle transitions T1, T3, T6 and T7 |
""",
"""| `G12` | the seal record | `G12`, under `S7`; lifecycle transitions T1, T3, T6 and T7 |
| `G13` | a held round's records are unchanged after its receipt commit | `G13`, under `S10` |
"""),
("""No round changes another round's receipt or seal state. A change is unauthorized, whichever entry
governs it, when it is to a path under `verification/receipts/` other than the round's receipt
path, to a path under `verification/v3-seals/` other than its seal record path, or to any path
under `verification/seals/`, which holds the seal state of protocol 2 and is no V3 round's.
""",
"""No round changes another round's receipt or seal record. A change is unauthorized, whichever entry
governs it, when it is to a path under `verification/receipts/` other than the round's receipt
path, or to a path under `verification/v3-seals/` other than its seal record path. The records of
the rounds landed before V3, `verification/seals/` among them, are no V3 round's state and no V3
predicate reads them; the release gate's `legacy-records` step keeps them unchanged.
"""),
("""names, each change authorized (`G12`). The content of a superseded receipt is not read: the final
receipt is the round's durable state (`S4`), and it alone fixes which seal record any receipt
commit carries.
""",
"""names, each change authorized (`G12`). The content of a superseded receipt is not read: the final
receipt is the round's durable state (`S4`), and it alone fixes which seal record any receipt
commit carries.

### `G13` — a held round's records are unchanged after its receipt commit

Whether a round holds is decided from `Q` (T7), and nothing later changes that answer. Whether a
later commit `C` still carries the round's records is a separate question, asked of `C`'s tree by
the verifier's check of every receipt in it. For a receipt at the receipt path `P` in `C`'s tree,
let `Qc` be the commit reachable from `C` that last wrote `P`. When the round holds at `Qc`:

1. the files under the round's record directory at `C` are exactly those at `Qc`: the same paths,
   each with the same mode and object id, none added and none removed;
2. every seal record the receipt at `Qc` names has, at `C`, the object id the receipt records.

A receipt for which either fails does not hold at `C`. A correction to a held round's records is
made by a later round in its own record, never by changing the earlier round's.
"""),
]
