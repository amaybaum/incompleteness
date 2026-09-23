# Certificate infrastructure round CV-2 — V1 retired: act 29 translated, standing invariants migrated, V2 the sole authority: RESULT

**Halted at the stage-3 boundary by owner ruling. Nothing of the round's execution landed.** `main`
carries the round's control plane only: the preregistration (blob
`61de8904ac4bc98eb2ae608f42d526faa1f5dcb7`) and Amendment 1 (blob
`b0187a44c6df12acce7368e9a7cc05c138bf41f5`), whose certified merge
`f9a99fdf4b3bfeb2d3e830c8d6980ced74d52d23` is the mandated execution base. No certificate, record,
verifier change, guard change or protocol-text change of this round is on `main`; `V1` is not
retired, `legacy-v1-owned.json` still names `PRA`, and `PRA` is certified by `V1` alone.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `CV2-0` | `HOLD` | the amended start state at `B`: every start-state row, the frozen pinned blobs and the two store trees, the three superseded `T1` segments at their frozen hashes with unique anchors, nothing between the preregistration's drafting snapshot and `B` but the two control-plane files |
| `CV2-1` | `SUPERSEDED-AS-FROZEN` | the stage-1 checkpoint and all five `T1` controls, decided there as Amendment 1 requires, with the four cells of the amended control 2 exactly as frozen |
| `CV2-2` | `TRANSLATED-AS-FROZEN` | the stage-2 checkpoint: the translation at the `F7` blobs, `V6` authoritative OK with `PRA` and its record `PASS`, `legacy-owned 0`, the round's own certificate `UNATTESTED`, 163 evidence ids, the guard `ALL CHECKS PASS` with the base's 105 verdicts |
| `CV2-3` – `CV2-11` | not reached | the round halted before stage 3 was committed |

The execution that produced these outcomes is not on `main` and is not evidence of anything beyond
this note; the facts above are recorded as measured.

## The finding that halted the round

Stage 3 adds seventeen frozen vectors to the conformance corpus. Its checkpoint requires `CV2-4`(a)
`CONFORMANCE-EXACT` and the guard's verdict map unchanged. The two cannot hold together.

`R7-CV1`'s census section `6a.corpus` records the corpus summary — `executed`, `mismatches`,
`exact` and the per-family counts — from a live run of the verifier over the live corpus, and the
contract `census-equal-to-committed` requires the whole census to equal `CV-1`'s committed
`census.json`, which carries `executed: 89` and `live-policy: 9`. Any legitimate extension of the
corpus therefore fails that contract and turns the guard red. This is a fifth live read of `CV-1`'s
own state, beside the four `T1` superseded: a statement fixed at `CV-1`'s certified subject, asked
of whatever tree the guard runs on.

Measured at the stage-2 tree with one additional passing vector and nothing else changed:
`census-equal-to-committed` goes from `true` to `false`, the only one of `R7-CV1`'s contracts that
changes.

## Disposition

The finding is not repaired within this round. Repairing it would extend the reconstruction of a
historical git subject that the next verifier architecture is designed to remove, so the retirement
of `V1`, and the safety properties this round was to establish — execution-time chronology for
native rounds, a verifier that checks its own text is stem-free, the standing invariants carried by
the live policy, and the verifier as sole authority — are carried as migration requirements of that
architecture rather than completed here.
