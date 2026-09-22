# Certificate infrastructure round CV-1 — the V2 round-certificate protocol: shadow, census and cutover: RESULT

**Non-sealing, `E` → `L`, no `P`, then `A`.** The round writes no manifest record, no prospective
declaration and no baseline change. Mandated execution base `B` =
`395d953faa5a2bd4d33c5b642e063f355453cba0`, the certified merge of the control plane (#713, push
run 35702332294, mode `B` over the 43 frozen rows); the preregistration's blob at `B` is
`45509fdf6271687034bc83c4fd86ca44098f58cd`, verified before any edit. Migration snapshot
`D` = `effd5c865dfcc207624712a6711a54b712642f48`.

## Outcomes

| target | outcome | decided by |
|---|---|---|
| `CV1-0` | `HOLD` | the locating controls of `R7-CV1` at `B`: the freeze blob, the four segments with their frozen hashes and unique anchors, `GR-2` `LANDED-UNRECORDED` with `E_GR2` and `L_GR2` recovered, the seals tree `92e0956a…`, no `verification/certificates/`, no `PRA.json`, the declarations act 28's |
| `CV1-1` | `SUPERSEDED-AS-FROZEN` | stage 1's checkpoint: the guard green at `3a631d6d79dcf49380cb27231c8dafd5be14d7c8`, 103 tags with the base's verdicts, `R7-GR1` 86 checks / 24 groups and `R7-GR2` 63 / 7, both `LANDED-UNRECORDED`; every `S1`–`S4` control in `R7-CV1` |
| `CV1-2` | `CERTIFICATES-TRANSLATED` | fifty-one certificates, all validating; the ledger's twenty-nine `landed` and six `base-only` rows |
| `CV1-3` | `CONFORMANCE-EXACT` | 89 vectors over thirteen families, executed set equal to the corpus, zero mismatches |
| `CV1-4` | `DERIVE-EXACT` | `B` derived and equal to the recorded base for every certificate with a control plane; `E`, `tree(E)` and `L` derived and equal to the recorded values for every `landed` row |
| `CV1-5` | `LIVE-RULES-SHADOWED` | 154 evidence ids resolved to their certified blobs through the empty relocation ledger; the live policy at `count: 0`; both reported by the shadow job |
| `CV1-6a` | `VERDICTS-AS-ADJUDICATED` | `census.json`, committed at the stage-4 head `92d769978921147b388a778a0f17cbd74fda213d` and recomputed equal at `E` |
| `CV1-6b` | `REPRESENTATION-AS-FROZEN` | the same census: 33 / 2 / 16 / 1 / 1 |
| `CV1-7` | `DUAL-GATING` | the release gate's `certificate-verifier` step in `--mode authoritative` at `E`; the mutation control below; the standalone job in `--mode shadow` |
| `CV1-8` | `MAP-PRESERVED`, `BUDGET-HELD`; the base emits 103 tags and `E` 104 | `cv1-tagmap.json`; `R7-CV1`'s budget contract |
| `CV1-9` | `ADDITIVE` | `R7-CV1`'s diff contracts against `B` |
| `CV1-10` | `BRIDGE-SIMULATED` | `R7-CV1`'s bridge rows, on a shared clone of this repository |

## The four supersessions

Each superseded segment was extracted from the base's own guard text at `B`, located by the
freeze's anchors, hashed and required equal to the frozen hash before anything changed; each
replacement is the freeze's own printed text.

| | superseded | sha256 | replacement |
|---|---|---|---|
| `S1` | `R7-GR2` `N12`, six lines | `3a47d54d…104cc` | the budget's subject is the lifecycle-scoped one the budget contract uses |
| `S2` | `R7-GR1` `seals-tree-integrity` | `914bbad3…5b08c` | the live tree while `EXECUTION`; `_gr1_seals_hist` at the recovered `E` and `L` afterwards |
| `S3` | `R7-GR2` `seals-tree-integrity` | `2ee51af0…9b21c` | the same split, one line |
| `S4` | `R7-GR1` fixture `F11`, six lines | `bd21c2a6…4bbac` | the positive half reads the same lifecycle-scoped subject; both negative halves and the row name unchanged |

The controls, measured by `R7-CV1` on every build:

- **`S1`.** The subject the old side reads is the guard at `E_GR2` carrying an unrelated edit
  outside the `R7-GR2` block, with `GR-2`'s history intact in this repository: the superseded
  `N12`, compiled from the base's text, fails its positive half; the replacement passes; the
  replacement on a tampered subject fails. With the state forced to `EXECUTION` on a live file
  whose budget holds, old and new return the same verdict. Post-landing the replacement reads the
  guard at `E_GR2` (the read is observed), and an unrecoverable `E` fails rather than skips.
  `R7-GR2` reports 63 checks and 7 control groups, every row passing, and every row but `N12`
  returns the same verdict when its negative suite is re-run on the successor text.
- **`S2`, `S3`, `S4`.** The old side is the base's own `_gr1_seals_ok`, compiled from the base's
  text, whose reads are the seals directory of the tree it runs on and git; the synthetic
  successor supplies exactly those reads — this tree's records plus a later round's authorized
  `base-only` record, this repository's history intact. On it each superseded statement fails and
  its replacement passes; `F11`'s superseded positive half fails and the replacement passes with
  both negative halves still failing; the superseded predicate passes on this tree's own seals
  directory, so the successor's rejection is the added record's. `EXECUTION` is unchanged on the
  live tree. Post-landing, on a `commit-tree` repository: a mutated seals tree at `E` fails, a
  mutated seals tree at `L` relative to its first parent fails, an unrecoverable `E` or `L` fails
  rather than skips. `R7-GR1` reports 86 checks and 24 control groups and `R7-GR2` 63 and 7,
  every row passing.

## The stages, each committed first and run at a fixed head

| stage | head | guard | failing contracts |
|---|---|---|---|
| 1 | `3a631d6d79dcf49380cb27231c8dafd5be14d7c8` | `ALL CHECKS PASS`, 103 tags = the base's | — |
| 2 | `c5737ad13e1ad5ee246b98dd1652ab229261dc10` | data only; the verifier in shadow: 52 certificates (51 `PASS`, `CV1` `UNATTESTED`), 35 records `PASS`, 89 / 89 vectors, exact | — |
| 3 | `1f24064a5ed7c49c8ca02598783d95773af0c115` | `FAILURE` on exactly `R7-CV1`, 104 tags; its nine red contracts are the stage-final artifacts and the stage-5 step: `census-committed`, `census-equal-to-committed`, `result-note`, `note:6a-sentence`, `note:6b-sentence`, `note:7-sentence`, `note-mut:6a-sentence-dropped`, `tag-map`, `release-gate-authoritative-step` | as listed |
| 4 | `92d769978921147b388a778a0f17cbd74fda213d` | `census.json` committed; `R7-CV1` red on exactly the seven that remain: `result-note`, the three `note:` sentences, `note-mut:6a-sentence-dropped`, `tag-map`, `release-gate-authoritative-step` | as listed |
| 5 | `7c16128682d91023e8b8f71ece61150d27807132` | the release gate's step; `R7-CV1` red on exactly the six artifact contracts: `result-note`, the three `note:` sentences, `note-mut:6a-sentence-dropped`, `tag-map`; the full release gate with the step: `PASS` | as listed |
| 6 | `the stage-6 commit` (candidate `E`) | `ALL CHECKS PASS`, 104 tags; both censuses recomputed equal to stage 4's | — |

## The `V2` objects

- **`V1`, the certificates.** Fifty-one translated (`origin: translated-v1`: 27 `sealing`, 8
  `non-sealing`, 16 `content-only`) and `CV1`'s bootstrap certificate (`protocol: 1`, `origin:
  bootstrap-v1`). Evidence pinned at `D`; control-plane entries carry the `main` merge that
  brought each artifact in, located **by blob** on `main`'s first-parent chain — act 21's
  preregistration re-froze a path act 19's freeze had added, so a path-addition search finds the
  wrong merge and a blob search finds `aeb0b91d` (#678); the same rule locates the artifacts the
  layout migration moved — and the `execution_affecting` flag; `B` derives as the merge of the
  last such entry and equals every recorded base, `GR-1`'s two amendments included.
- **`V2`, the ledger.** Thirty-five translated records under `attestations/`: 29 `landed` (the 27
  sealed rounds, `GR1`, `GR2`) with `sealed_head`, `tree` and `landing` read from git, 6
  `base-only`; every one carries `migration_snapshot` and no `ci` block. No attestation commit is
  claimed for any of them.
- **`V3`, the corpus.** 89 vectors: schema 19, ambiguity 6, visibility 8, artifact-class 8,
  dependency 4, topology 6, ledger 6, provenance 6, legacy-owned 5, live-policy 9, vacuity 2,
  historical-subject 6 (one per manifestation: declaration scope, pin scope, `N12`, the two
  seals-tree statements, `F11`), divergence 4 (`C-S1`–`C-S4`). Executed as an exact set on every
  build by the verifier and by `R7-CV1`.
- **`V4`.** No relocation record; the store is exercised by the corpus.
- **`V5`.** `live-policy.json` at `count: 0`.
- **`V6`, the verifier.** `tools/certificate_verifier.py`, standard library only, no round stem
  in its text (checked mechanically), `--mode shadow` and `--mode authoritative`, `--self-test`.
  On this repository: 52 certificates, 51 `PASS` and `CV1` `UNATTESTED` until `A`; 35 records
  `PASS`; 154 evidence ids resolved; `LEGACY-V1-OWNED PRA` reported with no validity claim.
- **`V7`.** `legacy-v1-owned.json` with exactly one entry, `PRA`, pinned to preregistration blob
  `5451a52d…` and base `0bedff07…`.

## The censuses

**`CV1-6a`, `VERDICTS-AS-ADJUDICATED`.** Over the verdicts of every pre-existing `V1` contract compared, on every one of the fifty-one certificates and on every comparable control, the `V1` guard and the `V2` verifier returned the same verdict at the same head, and they differed on exactly the four supersession controls, each in the direction this freeze named: each superseded segment, reconstructed from the base's text, fails on the successor tree named for it — a later edit to the guard for `N12`, a later round's seal record for the two seals-tree statements and for `F11` — and its replacement, which reads the round's own recovered history, passes, as does `V2`, which evaluates the round's certified subject. Representation changes are recorded separately and are not counted here. This is an agreement census with four adjudicated divergences and not a proof of correctness.

Fifty-one record rows agree on every axis compared (`evidence` for all, `topology` for the 29
`landed` rows against the `V1` tag and the keyed `U3` verdict or the repair rounds' chronology,
`base` for the 6 `base-only` rows). Of the twenty `SI-1` cases and the eleven `SI-2` cases
re-executed, 23 are comparable and agree; 8 are `no-analogue` (`SI-1` 9, 13, 14, 17, 18 and its
recorded observation; `SI-2` 8 and 12: prospective execution, `LANDED-PENDING-PIN`, seal pending,
the authorized-addition baseline and the legacy inventory are `V1` notions); `SI-2` 11 and 13 are
retired by `SI-3` and recorded as such. The corpus is exact. The four supersession controls diverge
as named: `C-S1` on the census head itself, whose guard carries `CV-1`'s edits outside `R7-GR2`;
`C-S2`, `C-S3` and `C-S4` on the synthetic successor; on the census head itself the three
seals-tree controls agree, `CV-1` adding no seal record.

**`CV1-6b`, `REPRESENTATION-AS-FROZEN`.** Thirty-three manifested rounds were transcribed with every value byte-equal; `GR-1` and `GR-2` changed representation from `LANDED-UNRECORDED` under `V1` to translated certificates and rows under `V2` with the same recovered `E`, `tree(E)` and `L` and no attestation commit claimed; sixteen content-only rounds received certificates with no `V1` lifecycle counterpart; `CV-1` is the unique bootstrap; act 29 is the one legacy-owned round, `V1`'s to certify and `V2`'s to name. No historical fact changed.

## Dual gating

From this head the release gate rejects a build the `V2` verifier rejects, alongside the `V1` guard, which gates exactly as it did at the base on every tag it carried there. `V2` can veto; `V1` is not retired and not a shadow; `V2` becomes the sole authority only in `CV-2`.

The mutation control: with the verifier made to fail — one certified evidence blob in `verification/certificates/OLT.json` altered, so its record's `certificate` blob no longer matches and the verifier reports `OLT:row:certificate-mismatch` with the dependent certificates failing by propagation — `tools/release_gate.py`
reports `FAIL  certificate-verifier` and exits 1; restored, it reports `PASS` on every step. The
standalone `Certificate verifier` job runs `--mode shadow` and never gates; `R7-CV1` checks both
readings of `verify.yml` and the gate's text.

## The act 29 bridge, simulated

On a shared clone of this repository — every real landing, both repair rounds' recovered `E` and
`L`, and the `V2` store intact — a `V1`-shaped sealing round `ZZ` was driven with `commit-tree`
through the five frozen steps. `V2` reported exactly `LEGACY-V1-OWNED` for the stem with no
certificate and no validity claim at steps 1–4 (its control plane and `V7` entry; its execution
head under a prospective declaration, checked out as the synthetic merge with the event naming the
real head; its landing merge; its pin commit, which adds exactly `verification/seals/ZZ.json`),
while the `V1` validator classified the head `EXECUTION`, the landing `LANDED-PENDING-PIN` and the
record `ARCHIVED` with pinned equal to derived; at step 4 the four replacements passed on that
repository while their superseded segments failed; at step 5 the translation's certificate and
record were accepted and the legacy-owned set reported empty, and a translation that left the
entry in place was refused. Eleven rows, all passing.

## `CV1-8` and `CV1-9`

The base's own guard file, run at `B` in a detached worktree, emits 103 tags, all `PASS`; the head
reproduces every verdict and emits exactly one tag the base does not, `R7-CV1`. The budget holds:
this file with the `R7-CV1` block removed and the four segments restored equals the base's guard
file. The diff against `B` deletes nothing; modifies exactly the guard, `verify.yml`,
`tools/release_gate.py` and `verification/README.md`; adds `tools/certificate_verifier.py`,
`verification/certificates/**` and this round's three artifacts; touches no file under
`verification/seals/`, `verification/programmes/` or `verification/audits/`, no `.lean`, no
manuscript, not `AGENTS.md` and not `ROADMAP.md`.

## Discrepancies and resolutions, recorded and not repaired

1. **The translation table's directory for `A6P`** is round 1's record directory, which the block
   reads as another round's artifacts; `A6P`'s own control plane is
   `audits/foundations/a6-covariance-propagation-audit.md`, brought in at `07ab3657` (#604), which
   is its recorded base. The certificate carries that directory and control plane.
2. **The four directory-less stems** resolve from the blocks' own artifact names: `SOI` to
   `audits/operational/stochastic-observer-interface-audit.md`; `C4R` to the causal-readback
   preregistration and amendment; `RCL` to amendment 1; `A11P` and `A12P` to their audits under
   `audits/foundations/`; `QSTAR` to no artifact, and its certificate carries an empty evidence
   list.
3. **`TSG`'s landing is not uniquely recoverable** from its `base-only` record (four candidate
   merges pass the ancestry test), so its `contributions` list is empty; the five other
   `base-only` rounds recover one landing each.
4. **The freeze's live-read census** was re-measured by the execution's own classifier, which
   resolves string literals against `D`'s tree: own 64, other 42, manuscripts 54, Lean 13,
   `ROADMAP`/`README`/`AGENTS` 27, guard 11, git 127 against the drafting-time 58 / 31 / 54 / 15 /
   33 / 12 / 132. The per-block table is carried below as data; the census is an inventory for
   `CV-2` and not a target.
5. **`SI-2`'s eleven cases** are nine executable and two retired by `SI-3`; the census records
   eleven rows with the two classified `retired`.
6. **`CV1`'s certificate** gained its three stage-final artifacts as evidence at stage 6, the
   round writing its own certificate during its execution; the record `A` will carry the
   certificate's blob at `E`.

## What no outcome of this round licenses

No deletion, weakening or bypass of an existing check, clause, region or seal record; no change to
a historical `B`, `E`, `L`, `P`, preregistration or result note; no claim that `V2` is correct, as
distinct from in agreement where it agrees, adjudicated where it differs, and now gating; no
sentence that `V1` is superseded, replaced, retired or a shadow; no change to act 29's head, no
edit to `#705`, no statement about act 29's targets; no `V1` seal record for `GR-1`, `GR-2` or
`CV-1`; no executable live-tree assertion beyond `R7-CV1`'s own contracts; no claim that `CV-2` is
safe because `CV-1` was green.

## The live-read census, per block (inventory for `CV-2`)

| stem | directory | own | other | manuscripts | Lean | `ROADMAP`/`README`/`AGENTS` | guard | git calls |
|---|---|---|---|---|---|---|---|---|
| `SOI` | `audits/operational` | 1 | 1 | 6 | 0 | 0 | 0 | 0 |
| `C4R` | `audits/physical-realization/c4-causal-readback` | 2 | 0 | 6 | 0 | 0 | 0 | 0 |
| `RCH` | `programmes/oi-qm/track-i/recurrence-tightness` | 2 | 0 | 6 | 0 | 0 | 0 | 0 |
| `SCF` | `programmes/oi-qm/track-i/recurrence-scaling` | 1 | 0 | 6 | 0 | 0 | 0 | 0 |
| `RCL` | `audits/physical-realization/c4-causal-readback` | 1 | 1 | 6 | 0 | 0 | 0 | 0 |
| `QSTAR` | `—` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `SOURCE` | `programmes/oi-qm/track-i/arc-d-operational-sourcing` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `BRIDGE` | `programmes/oi-qm/track-b/act-01-indivisibility` | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `TBRIDGE` | `programmes/oi-qm/track-b/act-02-transpose-bridge` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `CAND` | `programmes/oi-qm/track-b/act-03-candidate-selection` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `DILMAP` | `programmes/oi-qm/track-b/act-04-dilation-mapping` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `SRCA` | `programmes/oi-qm/track-b/act-05-source-a-candidate` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `TUPLE` | `programmes/oi-qm/track-b/act-06-tuple-instantiation` | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
| `DILCH` | `programmes/oi-qm/track-b/act-07-dilation-choice` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `DILL2` | `programmes/oi-qm/track-b/act-07-dilation-choice` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `RBR` | `programmes/oi-qm/track-b/act-09-readback-robustness` | 1 | 0 | 0 | 0 | 0 | 0 | 17 |
| `ABR` | `programmes/oi-qm/track-b/act-10-anchor-robustness` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `HYA` | `programmes/hydrodynamics/round-h-a-source-audit` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `CLG` | `programmes/oi-qm/track-b/act-11-coherent-lift-gauge` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `TSG` | `programmes/oi-qm/track-b/act-12-two-sided-gauge` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `SGT` | `programmes/substratum/lemma-24-1-semigroup-transfer` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `A11P` | `audits/foundations` | 0 | 0 | 9 | 0 | 0 | 0 | 0 |
| `A12P` | `audits/foundations` | 0 | 1 | 5 | 0 | 0 | 0 | 0 |
| `CTI` | `programmes/oi-qm/track-b/act-13-cross-time-invariants` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `PQT` | `programmes/oi-qm/track-b/act-14-threading-observability` | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| `HYB` | `programmes/hydrodynamics/round-h-b-reversible-fluid-substratum` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| `A6P` | `audits/foundations` | 1 | 2 | 9 | 0 | 2 | 0 | 0 |
| `WTS` | `programmes/substratum/lemma-24-1a-word-trace-sufficiency` | 1 | 1 | 0 | 0 | 2 | 0 | 2 |
| `PC4` | `programmes/physical-realization/round-c4-1-physical-discharge` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `PC4S` | `programmes/physical-realization/round-c4-2-storage-readback` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `A6D` | `programmes/substratum/a6-background-independence` | 2 | 0 | 0 | 0 | 1 | 0 | 2 |
| `A6I` | `programmes/substratum/a6-instantiation` | 2 | 1 | 1 | 0 | 2 | 0 | 2 |
| `HYE` | `programmes/hydrodynamics/round-h-e-h3-closure-bridge` | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| `TCF` | `programmes/oi-qm/track-b/act-15-pq3d-cancellation-fork` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `RNC` | `programmes/oi-qm/track-b/act-16-reanchored-channel-cancellation` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `TRJ` | `programmes/oi-qm/track-b/act-17-gram-trajectory-selection` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `XTS` | `programmes/oi-qm/track-b/act-18-intermediate-cross-time-structure` | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| `RNT` | `programmes/oi-qm/track-b/act-20-representative-naturality` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `OLT` | `programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted` | 0 | 0 | 0 | 1 | 2 | 1 | 1 |
| `OLN` | `programmes/oi-qm/track-b/act-22-orbit-law-naturality-factorization` | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| `OLG` | `programmes/oi-qm/track-b/act-23-orbit-law-gaps` | 0 | 2 | 0 | 1 | 1 | 1 | 1 |
| `OGS` | `programmes/oi-qm/track-b/act-24-orbit-geometry-selector` | 0 | 1 | 0 | 1 | 1 | 1 | 1 |
| `OGC` | `programmes/oi-qm/track-b/act-25-orbit-geometry-isometries` | 0 | 2 | 0 | 2 | 1 | 1 | 1 |
| `CGR` | `programmes/oi-qm/track-b/act-26-orbit-geometry-rigidity` | 0 | 2 | 0 | 2 | 1 | 1 | 1 |
| `NLV` | `programmes/oi-qm/track-b/act-27-strict-natural-lift` | 0 | 0 | 0 | 2 | 1 | 1 | 11 |
| `PFR` | `programmes/oi-qm/track-b/act-28-product-locus-freedom` | 0 | 1 | 0 | 2 | 1 | 0 | 7 |
| `SI1` | `infrastructure/round-si-1-shadow-seal-validator` | 4 | 1 | 0 | 0 | 0 | 1 | 7 |
| `SI2` | `infrastructure/round-si-2-authority-cutover` | 6 | 4 | 0 | 0 | 1 | 1 | 5 |
| `SI3` | `infrastructure/round-si-3-legacy-seal-retirement` | 4 | 11 | 0 | 0 | 1 | 1 | 25 |
| `GR1` | `infrastructure/round-gr-1-roadmap-entry-scoping` | 5 | 4 | 0 | 1 | 2 | 1 | 20 |
| `GR2` | `infrastructure/round-gr-2-post-landing-scoping` | 3 | 3 | 0 | 0 | 0 | 0 | 9 |
| **total** | | 64 | 42 | 54 | 13 | 27 | 11 | 127 |
