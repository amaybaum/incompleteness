# A1-EXIT Step 2, unit S2-D — global-phase statements and the inflow endpoint: result

**Status.** WIP / UNVERIFIED. This is the writer's record. Independent non-author review is
required, and merge is a separate owner decision. The work is consistency work only: no premise is
added, no claim is strengthened, and the §A.23 bands are unchanged.

**Authorization and Goal link.** The same as `PREREG.md` (owner `amaybaum`, #1169 comment 7056875845;
A1-exit objective #1169).

**Base.** `1c7eedc40`. PREREG was committed at `fdcca6ea` before any manuscript edit. No edit changes a
line count, so every site keeps its base line number.

## 1. Edits as applied

All 18 preregistered edits were applied verbatim, from the same exact-string list. The apply script
checks that each old string occurs exactly once, on the preregistered line, before it replaces anything.

| Edit | Site (base = new line) | Ledger row | Source | Form |
|---|---|---|---|---|
| E1 | M:748 (§4.6 heading) | X-63 | T22 | W* |
| E2 | M:764, lead-in "For $(S,\varphi)$ in its equilibrium macrostate" | X-63 (line mapped to X-62) | N4 | finite scope (finite representative) |
| E3 | M:764, the rate lead-in moved onto the T7a sentence | X-63 (line mapped to X-62) | N4; T7a | unchanged content |
| E4 | M:764, the phase sentences | X-63 | T7b | W* |
| E5 | Sub:56 | X-63 | T11b | W* |
| E6 | Sub:56, past-hypothesis replacement and incoming stream | X-63; X-82 | T11c; INFLOW | open |
| E7 | Sub:401 | X-63 | T12 | W* |
| E8, E9 | Sub:542 (two clauses) | X-63 | T14 | W* |
| E10 | Str:718 | X-63 | T15 | W* (observer-relevant regions at every time) |
| E11 | Str:718, bullet label | X-63 | T16 (consequence) | label follows E12 |
| E12 | Str:734 | X-63 | T16 | W* (necessary condition on the observer's region) |
| E13, E14 | ch02:192 | X-63 | T18 | W* |
| E15, E16 | FULL:822 | X-63 | T18 mirror | W* |
| E17 | ch04:178 | X-63 | T20b | W* |
| E18 | FULL:1282 | X-63 | T20b mirror | W* |

The old and new strings are in `PREREG.md`.

### Notes on the readings

- **E2/E3 (N4).**
  - The landed [31] statement concerns a finite-dimensional shell. Main's own Scope paragraph (M:732)
    already lists "the canonical-typicality clause" among the statements about the finite
    representative. E2 therefore names the finite representative and drops the presupposition that
    $(S,\varphi)$ is in a global equilibrium macrostate.
  - The rate condition was carried by the lead-in "Under $\tau_{\rm mix}\ll\tau_S$:". E3 attaches it
    to the region-level sentence, the only one that uses it (T7a, RETAINED). What that sentence asserts
    does not change.
- **E4.** The posit sentence "That every relevant equilibrium region satisfies (EM) at the required rate
  is itself a physical hypothesis …" is kept unchanged (Main:764 LEDGER, "Scope kept out"). Only the
  conclusion is restated as W*.
- **E6.**
  - Following T11c, the replacement of the past hypothesis is stated open on every carrier. The reason
    is the audit's own: the rule selects regions, not global configurations.
  - The Boltzmann-brain exclusion (T11d, RETAINED) keeps its finite-bijective scope.
  - The incoming-stream sentence of the Phase-2 B4 splice is kept. It is reattached as a further part
    of the open question on an infinite carrier, so the sentence no longer relies on finiteness to
    settle the replacement (X-82).
- **E11/E12.**
  - The audit does not trace the claim at Str:734 that random permutations "typically lack" these
    features, and it is unchanged.
  - The label of the bullet at Str:718 is the feature name that Str:734 cites. It is renamed so that
    the reference still resolves. The first sentence of Str:718 (D2, not classified) is unchanged.
- **Main independence.** E1–E4 use only Main's own theorem, (EM), the rate condition and [31]'s
  finite-shell scope (M:732). No downstream reference is added.

## 2. Propagation (§A.25, §A.14)

I re-grepped `papers/*.md` and `book/*.md` (FULL included) after the edits:

| Phrase | Remaining | Where |
|---|---|---|
| "non-equilibrium phase" | 1 | Cx:212 (S2-E) |
| "equilibrium phase" | 3 | Cx:212 ×2 (S2-E); M:171 (T10, RETAINED pointer) |
| "Equilibrium-Phase", "non-equilibrium-phase", "perpetual equilibrium", "confinement to", "restricts observers", "in its equilibrium macrostate" | 0 | — |
| "past hypothesis" | 2 | Sub:56 (E6, stated open); Cx:212 (S2-E) |
| "observer-free" | 1 | Sub:542 (E8, region form) |
| "fast-mixing regions" (any case) | 4 | M:748, Sub:542, ch04:178, FULL:1282 (new) |

- **Book mirrors.** ch02:192 ↔ FULL:822 and ch04:178 ↔ FULL:1282 are byte-identical after the edits.
- **Other books, appendices and glossary.** The Main, Substratum and Structure sites have no restatement
  in any other book file, appendix or the glossary.

## 3. Wording for S2-E (Q3-owned sites; not edited here)

**Cx:212 (T17b; X-82).** Both old strings are unique in `papers/Complexity.md`.

1. Old: `that C1–C4-satisfying observers, with C2 read in its timescale form, cannot exist in the
   equilibrium phase of $(S, \varphi)$:`

   New: `that C1–C4-satisfying observers, with C2 read in its timescale form, cannot exist in
   regions whose effective channel mixes in a time short compared with $\tau_S$:`
2. Old: `The "past hypothesis" of low initial entropy — usually imported as a separate axiom to
   explain why we observe a low-entropy universe — is replaced, in its role of selecting
   observer-compatible configurations, by the same theorem, since, in that description and with C2
   read in its timescale form, observers exist only in the non-equilibrium phase.`

   New: `Whether the same theorem replaces the "past hypothesis" of low initial entropy — usually
   imported as a separate axiom to explain why we observe a low-entropy universe — in its role of
   selecting observer-compatible configurations is open, since the theorem selects regions rather
   than global configurations; on an infinite carrier an invariant law can also carry a low-entropy
   stream entering from spatial infinity, and whether such an incoming supply is excluded is not
   settled.`

The Boltzmann-brain sentences of Cx:212 (T17a, RETAINED) and its clause "τ_B is bounded by the local
mixing time on equilibrium microstates" (T11a-type, RETAINED) need no change.

**ch18:40 = FULL:4771 (X-82).**

- **Reliance on finiteness.** The sentence ("… follows from the finite reversible substratum dynamics,
  which is recurrent under A1 (§18.7)") concerns recurrence versus effective relaxation. It does not
  use finiteness to exclude an incoming stream. Whether X-82's correction applies to it is S2-E's
  call.
- **Suggested insertion, if it applies.** After `which is recurrent under A1 (§18.7);` insert `on an
  infinite carrier an invariant law can carry a low-entropy stream entering from spatial infinity,
  and whether such an incoming supply is excluded is open;`
- **Uniqueness.** The anchor string is unique in each of the two files.

**Meth:283, Meth:441 (X-63 Q3 sites).** Both state the region-level exclusion without a phase
conclusion. The same holds for ch03:58, ch04:36 and Sub:407. No change is proposed.

## 4. Builds

| Source | Pages (base → new) | Median chars/page (base → new) | Dropped glyphs |
|---|---|---|---|
| Main | 106 → 106 | 3338 → 3338 | none |
| Substratum | 53 → 54 | 3240 → 3189 | none |
| Structure | 94 → 94 | 2908 → 2908 | none |
| book (FULL) | 489 → 489 | 2998 → 2998 | none |

The papers were built with `sh ./build.sh Main Substratum Structure` and the book with
`sh ./build.sh --book`. Both builds printed `build: OK`. The regenerated `.tex` and `.pdf` files are
committed with the source.

## 5. Coverage

- **Stale entry.** `tools/coverage_check.py` reported one stale entry,
  `MAIN:C-observer-selection-rule-rate-condition`, with fingerprint `9830ad9513ecc4f8` →
  `375f3d287641e4a7`.
- **Re-affirmed.** The kernel status stays `GAP` and the delta stays "not formalized". The assumptions
  ("the observer-selection theorem plus its rate condition … stated for the coarse-grained description
  generated by iterating the effective channel") are still accurate, since E3 keeps the rate condition
  explicit.
- **Result.** After the fingerprint update the check reports `coverage_check: OK (132 canonical
  statements, 20 unattached checkers)`.

## 6. Other checks (§A.40)

- **Exit 0.** staleness, voice, voice-scope, artifact-placement, manifest-drift `--check`, claims,
  duplicate, mirror, citation, architecture, dependency-label `--strict`, coverage, the lean-manuscript
  census, the legacy-records self-test and the v3 verifier self-test.
- **Not decided locally.** `tools/v3_verifier.py --corpus` reports `UNDECIDABLE
  undecidable:shallow-repository` for the s8-landed vectors in this shallow worktree. This change does
  not touch it, and CI runs it with full history.
- **§A.32/§A.33 scan of the added manuscript text.** No register, reader-instruction, self-assessment,
  revision-history or caps-emphasis hit.

## 7. Deviations from PREREG

- **Manuscript.** None: every edit was applied as preregistered.
- **PREREG.** After `fdcca6ea`, PREREG's mirror entries E15, E16 and E18 were re-rendered as "identical
  to E13/E14/E17", because `tools/duplicate_check.py` rejects repeated paragraphs within a file. No old
  or new string changed.

## 8. Overlaps

- **Other units.** No edited line lies in another unit's listed scope.
- **ch02.** S2-B's scope names the whole of ch02. This unit edits only ch02:192 (an X-63 site in the
  ledger's sitemap) and its FULL mirror. S2-B should confirm that it does not edit ch02:192.

## 9. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Class |
|---|---|---|
| #1169 comment 7056875845 | authorization | provenance |
| PR #1472 (this unit's draft PR) | tracking | provenance |
| PR #1463 | X-62 landing (merged; content on `main`) | support on `main` |
| PREREG commit `fdcca6ea` | chronology of this record | provenance (on this branch; lands with it) |

Every support this record uses is on `main`: the Stage 1(ii) audit, the A1-EXIT ledger, the Main:764
ledger and REMAINDER §5.

## 10. Verification status (§A.46 item 4)

- **Independently verified.** Nothing yet. This is the writer's record and awaits non-author review.
- **What the edits rest on.** The Stage 1(ii) audit's classification (an independently reviewed
  record on `main`) and its W* (§6), which is conditional on (EM) and the rate condition on declared
  regions.
- **What stays open.** The phase statements themselves, which are not restated here; the replacement
  of the past hypothesis; and O-INFLOW. All are tracked under #1169 (X-63, X-82). O-INFLOW is also
  tracked under #866.
- **What would resolve them.** A statement about actual record laws that distinguishes equilibrium
  regions from observer regions (AUDIT §8, "Remaining gap").
