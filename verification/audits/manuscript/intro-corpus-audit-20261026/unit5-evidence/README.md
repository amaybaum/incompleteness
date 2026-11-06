# unit5-evidence — independent evidence review for OD-15 and EV-28 (#941 Unit 5)

**Standing.** `REVIEW.md` is the independent Unit 5 evidence review of #941. Its reviewer did not write
the closure ledger or the evidence it reviews. It was carried out under the owner rulings of #941
comment 6677500012 (amaybaum, 2026-11-06T05:11:33Z), items 11, 12, 13 and 17, and it applies, in its §7,
the verification standard of #1031 comment 6678672357 (amaybaum, 2026-11-06T06:26:04Z), section 3:
"Choose CI plus independent re-comparison, not a new full Lean build at this stage." Its §7 governs
wherever its §§0–2 are worded differently, and the §A.42 item 8 table at the end of this README governs
wherever its §6 classifies a reference differently.

**Result, as the standard requires it to be described.** For OD-15 (the three declarations
`OIBridge.PhaseSource.permClass_onesFixing`, `OIBridge.PhaseSource.onesFixing_not_phasesAvailable` and
`OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere`) and for EV-28 (the
248 `#print axioms` reports of the 14 modules that
`../introduction-repro-ext/results-121598983127-28.json` adds), the review finds **independently
audited historical evidence**, with no correspondence missing and no mismatch. No fresh reproduction is
claimed: no Lean build was run for this review. The scientific claims these declarations support keep
their existing proof-status qualifications.

**What this record does not do.** The review's acceptance is the owner's step, on #941, which remains
accountable for EV-28 until then ("#941 remains open until that review is accepted", #1031 comment
6678672357, section 3). This record changes no outcome in `../CLOSURE-LEDGER.md`; the closure audit
(Unit 6) records outcomes.

## Contents

| file | sha256 | what it is |
| --- | --- | --- |
| `REVIEW.md` | `a92d266ba2a93594818939183ebd237c01287b03aea06c3c5afc239fb5aab020` | the review, with Appendix A, its per-report table of all 248 reports |
| `u5_reextract.py` | `105e7e342e082b5479ad1d94656c81fa83483660d8e0cbd5ad1597bca3ed57f0` | the reviewer's own log parser and source resolver (§7); imports nothing from the evidence-retention archive, the release gate or `u5_check.py` |
| `u5_check.py` | `d71bce27256a626f3084c323e5171b2886f7bf9c37fca95f58c6512b4b36efbc` | the reviewer's static check of the two expected results and the Lean sources (§§0–2), with an optional artifact layer |
| `u5_reports.tsv` | `2f4610d54620d67ac9bcab3419ddf377f907827b14db4084622a7c8997f898f2` | the per-report table written by `u5_reextract.py`: 248 rows keyed by (module, fully qualified name), with the source line at `17b830bc` and on `main`, and the line and axiom list in H, F and J (below) |

The three files besides `REVIEW.md` are byte-identical to the reviewer's (the digests are those the
review states). `REVIEW.md` is the review as delivered (sha256
`78227551e04699eb391099de700f21a3599edc0dda95e20aa3683c66295bc114`) with one redaction: two mentions of
the reviewer's local working path (its lines 30 and 314) are replaced by the file's place in this
directory. Nothing else differs. Every file here was scanned for tokens, keys, signed-URL parameters,
IPv4 and e-mail addresses and local paths: no matches.

## The objects compared (review §7.1)

- **J** — the retained 28-module result on `main`, blob `97a2377dbfc30987887dffea2b72e423feed079d`,
  pinned by `EXPECTED_28` (`2714278a`) in `.github/workflows/evidence-replay.yml`.
- **S** — the `#print axioms` commands of each module at the source commit
  `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86`, resolved to fully qualified names, and on `main`.
- **H** — the pinned historical log: job 121598983127 ("Mathlib bridge") of run 40330683786
  (`verify.yml`, `push`, at `17b830bc`). 43064 lines, sha256
  `bc2291bc57d952779f27282211b588321618bf503d39d192840c777074cd0c81`; its lines 1–38918 hash to
  `1a83921fb967dad82785ce79b06013f184f4a82e377e39cad21ab4df453e09df`, J's `source.served_sha256`.
- **F** — the archived fresh-build log: `build-and-gate.log` in artifact 12714762314
  (`lean-fresh-build-40457712855-1`) of run 40457712855, sha256
  `31e5045bc9c4d563566a7600dd9e747d658e2ac44b083de232f4d71d37ad8979`. The artifact zip has sha256
  `d5b8256bc7a19db34629a8ddfaba0824f078ee77f30a5ddfa867b580c0a1a0f8`, equal to the host's recorded
  digest, and its `SHA256SUMS` covers the log.

H and F are not committed (AGENTS.md §A.42 items 2 and 4). They are provenance, pinned by the digests
above. The content the review uses from them, the line and axiom list of each of the 248 reports in
each log, is landed here in `u5_reports.tsv`.

## Recipe (AGENTS.md §A.42 item 1)

Run from the root of a full-history clone of the repository, with `<rec>` =
`verification/audits/manuscript/intro-corpus-audit-20261026/unit5-evidence`. Outputs go outside the tree.

**1. From `main` alone (no network).**

```
python3 -I <rec>/u5_check.py . 424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b > <out>/static-424f.json
python3 -I <rec>/u5_check.py . 374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0 > <out>/static-374b.json
python3 -I tools/lean_manuscript_census.py
```

Expected: each `u5_check.py` run exits 0 with `"verdict": "PASS"` and `"failures": []`, and its output
has sha256 `d21449aae2c9d596e89cb589601a8ae12c183bbb397c5334ce3c2ca797a06ae4` (at `424f28b1`, the
commit the review's §§0–2 ran on) and `6bbbb1d7496fe56b953ff9ef1bc797ae760533e6374fe492a2abf36b23d2ce2e`
(at `374b2ef3`, the `main` of §7). The census exits 0 with
`lean_manuscript_census: OK (… 25 current families; complete relative to the maintained registry)`.
This layer checks, for the 14 added entries and the three OD-15 declarations, everything that can be
checked without a Lean build: S against J, line by line and name by name; the modules' presence in the
gated build; byte identity from `17b830bc` through `2714278a` to `main`; and the absence of
axiom-introducing constructs in each module's import closure. Its mutation controls are part of the
output.

**2. The re-comparison against H and F (needs the two logs).**

```
gh api repos/amaybaum/incompleteness/actions/jobs/121598983127/logs > <H>
gh api repos/amaybaum/incompleteness/actions/artifacts/12714762314/zip > <zip>
sha256sum <H> <zip>        # bc2291bc… and d5b8256b… (above)
# unpack <zip> into a new directory <art> with Python's zipfile; in <art>: sha256sum -c SHA256SUMS
python3 -I <rec>/u5_reextract.py . 374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0 <H> <art>/build-and-gate.log <out>/reports.tsv > <out>/reextract.json
cmp <out>/reports.tsv <rec>/u5_reports.tsv
python3 -I <rec>/u5_check.py . 424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b <art> > <out>/artifact-424f.json
```

Expected: `u5_reextract.py` exits 0 with `"verdict": "PASS"`, `"mismatches": []` and 0 mismatches in
each of the 14 modules; its output has sha256
`5c905fcaa4027c114eaf4891bc2e5331bfc2ae38feb0e01e562419052f028fa3`, and the table it writes is
byte-identical to `u5_reports.tsv`. The script itself fails unless H's full digest and the digest of its
lines 1–38918 are those above; F's digest is part of its output, so a different F changes the output
digest. The artifact-layer `u5_check.py` run exits 0 with `"verdict": "PASS"` and output sha256
`731c12a70439432fbdc5d852f9dd4a70ce6b279b37f18ca717e26dbce03dae08`.

All outputs are deterministic; a second run is byte-identical. Every commit named here
(`17b830bc`, `2714278a`, `f5efa7a0`, `14804075`, `424f28b1`, `374b2ef3`) is reachable from `main`.
Step 2 depends on the host's retention of the job log and the artifact (the artifact expires
2027-01-25); once they expire, `u5_reports.tsv`, compared with S and J by step 1, is the remaining
record of what the logs contained.

## Limits (review §7.6)

- No Lean elaboration was performed by the review or for this record. The kernel's axiom output rests on
  CI: H, a cached build whose reports are replays of an earlier elaboration of the same sources, and F,
  a CI build from an empty `.lake/build` dispatched by the evidence's author, not by the reviewer.
- H is a CI job log held by GitHub, not on `main`, and pinned only by the digests above.
- The comparison parses log text, which AGENTS.md §A.44 otherwise excludes from verdicts about what a
  CI run showed, because the owner's standard names the pinned historical log as the object compared.
  H is read whole through the API, not as a served tail, and F's reports are corroborated by the
  artifact's structured `reproduced.json` (the artifact layer of `u5_check.py`).
- Current-source CI on `main` (table below) checks only that each reported axiom lies within the
  permitted set, not the exact list; the gate's checker reads names by short name and only ASCII names.
  Those gaps are tracked in #1162. All three OD-15 declarations and all 248 EV-28 reports have ASCII,
  unique short names, and the review checks every report individually by fully qualified name.
- The current-source CI does not record its resolved Mathlib revision (no `lake-manifest.json` is
  committed).

## CI identities (structured host records; review §7.5)

| run | workflow, event | head | job and step conclusions | kind |
| --- | --- | --- | --- | --- |
| 40330683786 | `verify.yml`, `push` | `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86` | job 121598983127 "Mathlib bridge" `success`; "Build", "Release gate" `success` | historical; source of J and H |
| 40457712855 | `evidence-replay.yml` at `14804075f8f98588ec25c61fe8908b871fb74231`, `workflow_dispatch` | checks out `17b830bc` | job 122034819227 "Lean fresh build at 17b830bc" `success`, every step `success` | historical; source of F |
| 42164140276 | `verify.yml`, `push` | `424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b` | job 127716522424 "Mathlib bridge" `success`; "Build", "Release gate" `success` | current-source CI |
| 42174428450 | `verify.yml`, `push` | `374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0` | job 127749493708 "Mathlib bridge" `success`; "Build", "Release gate" `success` | current-source CI |

The run and job ids are provenance (AGENTS.md §A.42 item 2).

## References to content off `main` (AGENTS.md §A.42 item 8)

| reference | classification |
| --- | --- |
| job 121598983127 / run 40330683786 (H) | support on `main`: the per-report content the claims use (module, fully qualified name, line and axiom list of each of the 248 reports, the three OD-15 declarations among them) is in `u5_reports.tsv`. The log itself is provenance, pinned by the digests above and re-checkable against the TSV while the host retains it |
| run 40457712855, artifact 12714762314 (F and the artifact layer) | support on `main`, as above, for F; the artifact itself is provenance, pinned by its zip digest and `SHA256SUMS` |
| runs 42164140276, 42174428450 (step conclusions) | provenance; the claim that the current sources pass the gate's subset check regenerates from `main` through the release gate (step `lean-axioms`) at `374b2ef3` |
| #941 comment 6677500012; #1031 comment 6678672357 | the owner rulings governing the review and its standard |
| the review's own §6 table | the review's classification of the further references it makes, for EV-CI-1, EV-CI-3 and EV-L |
