"""Scratch: V3-13's edits to verification/README.md. Never landed as is."""
README = 'verification/README.md'
README_EDITS = [
# A6P: the constants it read no longer exist
("""a derivation of the gauge group. The round is **non-sealing** under `§A.37`: it owns the guard
contracts asserting the live row and the live label cell and owns no seal state, so
`_A6P_SEALED_HEAD`, `_A6D_SEALED_HEAD`, `_A6I_SEALED_HEAD` and every `_*_MERGE` and `_*_BASE`
constant are read and never written, and the landing is `E` → `L` with no archive-pin commit.
""",
"""a derivation of the gauge group. The round is **non-sealing** under `§A.37`: it owns the guard
contracts asserting the live row and the live label cell and owns no seal state, so
`_A6P_SEALED_HEAD`, `_A6D_SEALED_HEAD`, `_A6I_SEALED_HEAD` and every `_*_MERGE` and `_*_BASE`
constant were read and never written, and the landing is `E` → `L` with no archive-pin commit.
"""),
# SI-1: the count is SI-1's
("""`verification/seals/` carries one JSON record per round: twenty-two of them, eighteen `kind:
"sealed"` and four `kind: "base-only"`. They are a **transcription** of the seal constants
`verification/lean/edge_rigidity_probe.py` already carried, and the guard machinery in that file
remains **authoritative**. `R7-SI1` runs a generic validator over the records as a SHADOW and
reports a census of its agreement with the existing per-round checks; the shadow decides nothing.
""",
"""`verification/seals/` carries one JSON record per round. `SI-1` wrote twenty-two of them,
eighteen `kind: "sealed"` and four `kind: "base-only"`, as a **transcription** of the seal
constants `verification/lean/edge_rigidity_probe.py` then carried, and the guard machinery in that
file remained **authoritative**. `R7-SI1` ran a generic validator over the records as a SHADOW and
reported a census of its agreement with the existing per-round checks; the shadow decided nothing.
"""),
# SI-2: its account of §A.37 and of the shadow, in its own time
("""The generic seal validator `SI-1` built as a shadow is now **authoritative**, and the manifest under
`verification/seals/` is the seal state it validates: twenty-three records, eighteen `sealed` and
five `base-only`, the twenty-third being the `SI1` record this round added first. The adjudicated
""",
"""The generic seal validator `SI-1` built as a shadow became **authoritative**, and the manifest under
`verification/seals/` the seal state it validated: twenty-three records, eighteen `sealed` and
five `base-only`, the twenty-third being the `SI1` record this round added first. The adjudicated
"""),
("""and archive clause in `verification/lean/edge_rigidity_probe.py` is now a call to that validator
keyed on the round's record. The old machinery still runs on every one of them, and on the
per-round seal-integrity comparisons, as a **shadow that gates nothing**: its verdicts are recorded
beside the validator's, and two dynamic controls show that forcing or flipping them changes no
verdict. Manifest integrity is data-driven, one rule over the record set fixed at the round's first
stage. Nothing was deleted: the sixty-one legacy seal-constant assignment statements are at the
head exactly as at the base, as text and in order, and `AGENTS.md` §A.37 now says in two halves
that they **cease to gate** from this landing and remain **protected historical seal state** until
the retirement round, which is sealing and writes its own manifest record.
""",
"""and archive clause in `verification/lean/edge_rigidity_probe.py` became a call to that validator
keyed on the round's record. The old machinery kept running on every one of them, and on the
per-round seal-integrity comparisons, as a **shadow that gated nothing**: its verdicts were recorded
beside the validator's, and two dynamic controls showed that forcing or flipping them changed no
verdict. Manifest integrity was data-driven, one rule over the record set fixed at the round's first
stage. Nothing was deleted: the sixty-one legacy seal-constant assignment statements were at the
head exactly as at the base, as text and in order, and `AGENTS.md` §A.37 said in two halves that
they **ceased to gate** from this landing and remained **protected historical seal state** until
the retirement round, which was sealing and wrote its own manifest record.
"""),
# SI-3: R7-SI3's contract and §A.37's text are gone
("""seal-integrity comparison (the five `_<stem>_prior_seals` comparators, their eight recordings, and
the recorder itself); every read of a round's seal state goes through one manifest accessor,
`_seal_field`, and the zero-statement count is a standing contract `R7-SI3` keeps, so a round that
writes a constant again fails it. The round was **sealing**, `E` → `L` → `P`, the first to seal
""",
"""seal-integrity comparison (the five `_<stem>_prior_seals` comparators, their eight recordings, and
the recorder itself); every read of a round's seal state goes through one manifest accessor,
`_seal_field`. The round was **sealing**, `E` → `L` → `P`, the first to seal
"""),
("""stage commits — so nothing was gating on a shadow, as `SI-2` measured. `AGENTS.md` §A.37 now states
the representation retired, the prospective declaration and its removal at `P`, the round-declared
baseline, and the closed-round rule, once for every round after.
""",
"""stage commits — so nothing was gating on a shadow, as `SI-2` measured.
"""),
# the workflow: three jobs, every change
("""`.github/workflows/verify.yml` runs the zero-import kernel check, the Mathlib build, and the
probes as three independent jobs on every change under `verification/`.
""",
"""`.github/workflows/verify.yml` runs the zero-import kernel check, the Mathlib build with the
release gate, and the probes as three independent jobs, on every pull request and every push to
`main`.
"""),
# CV-1: V2 in its own time
("""them. One generic, standard-library verifier, `tools/certificate_verifier.py`, with no round stem
in its text, derives every git-derivable fact again — the base from the control plane's last
""",
"""them. One generic, standard-library verifier, `tools/certificate_verifier.py`, with no round stem
in its text, derived every git-derivable fact again — the base from the control plane's last
"""),
("""live base-branch tip — and holds one universal live rule: every evidence id of every accepted
certificate resolves, through a relocation ledger, to exactly one current path at its certified
blob. It is held to a conformance corpus of eighty-nine vectors over thirteen families, executed as
an **exact set** on every build, six of them the permanent record of one defect: **an
""",
"""live base-branch tip — and held one universal live rule: every evidence id of every accepted
certificate resolves, through a relocation ledger, to exactly one current path at its certified
blob. It was held to a conformance corpus of eighty-nine vectors over thirteen families, executed as
an **exact set** on every build, six of them recording one defect: **an
"""),
("""**Dual gating.** From the round's fifth stage `tools/release_gate.py` — the in-repo gate the
required `Mathlib bridge` check runs — carries the verifier in authoritative mode, so `V2` can
reject a build with repository-controlled semantics; the standalone `Certificate verifier` job runs
it in shadow and gates nothing, the repository's ruleset requiring only three status contexts. `V1`
is not retired and not a shadow: every `R7` block gates at `E`, at `L` and after as at the base,
""",
"""**Dual gating.** From the round's fifth stage `tools/release_gate.py` — the in-repo gate the
required `Mathlib bridge` check runs — carried the verifier in authoritative mode, so `V2` could
reject a build with repository-controlled semantics; the standalone `Certificate verifier` job ran
it in shadow and gated nothing, the repository's ruleset requiring only three status contexts. `V1`
was not retired and not a shadow: every `R7` block gated at `E`, at `L` and after as at the base,
"""),
# V3: the verifier as it stands, and the round that retired V2
("""(`infrastructure/round-v3-11-authority-cutover/`). Its projection over the `V2` attestation rows
gates nothing, and its workflow job, `V3 verifier diagnostics`, is not a required check. `V1` and
`V2` keep running and can still fail the release gate; they do not decide whether a native round is
protocol-valid. Its conformance corpus is `infrastructure/v3/conformance/`, executed as an
exact set; its comparison with `V2` over the attestation rows is `V3-2`'s `census.json`.
""",
"""(`infrastructure/round-v3-11-authority-cutover/`), and, for each receipt that holds, requires the
round's record directory and seal record to be unchanged since that commit (`G13`,
`infrastructure/round-v3-13-retirement/`). Its conformance corpus is
`infrastructure/v3/conformance/`, executed as an exact set; the release gate runs the corpus and
the verifier's self-test as the steps `v3-corpus` and `v3-self-test`. Its comparison with `V2` over
the attestation rows is `V3-2`'s `census.json`.

Round `V3-13` (`infrastructure/round-v3-13-retirement/`) retired the checks that re-derived the
chronology of the rounds landed before V3 at every later head, as `V3-12`'s census
(`infrastructure/round-v3-12-retirement-census/`) classified them: 1,610 predicates of the guard
and fourteen of its checks, the `V2` verifier with its gate step, workflow job and conformance
corpus, the control-plane base check and lint, and the verifier's projection over the `V2` rows.
The records of those rounds are kept instead by the release gate's `legacy-records` step,
`tools/legacy_records_check.py`: every record listed in `infrastructure/legacy-records.json` keeps
its blob, no file is added under a closed namespace, and the manifest changes only as the governed
work of a native round whose receipt holds. The guard's 2,492 retained predicates, in 91 checks,
check content and read no repository history.
"""),
]
