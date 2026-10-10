# Manuscript round CONSC-2 — observation terminology: registration, observation, admitted observer: PREREGISTRATION

**Status: candidate freeze.** This file is the control plane of a native round under `AGENTS.md` §A.39. It is drafted
on its pull request from `D` and is final only at the commit `F` the owner designates; no commit after `F` changes it.
The frozen substitutions, the controls, the stages and the outcomes below are fixed; the predicted execution tree is
recorded before `F`.

```v3-round
round CONSC-2
kind non-sealing
record-directory verification/audits/manuscript/round-consc-2-observation-terminology/
```

```v3-governed-paths
record AM verification/audits/manuscript/round-consc-2-observation-terminology/
record AM verification/receipts/CONSC-2.json
execution M papers/Main.md
execution M papers/Main.tex
execution M papers/Main.pdf
execution M papers/GR.md
execution M papers/GR.tex
execution M papers/GR.pdf
execution M papers/Structure.md
execution M papers/Structure.tex
execution M papers/Structure.pdf
execution M book/ch01-observation.md
execution M book/ch03-structural-realism.md
execution M book/ch18-beyond.md
execution M book/glossary.md
execution M book/The-Incompleteness-of-Observation-FULL.md
execution M book/The-Incompleteness-of-Observation-FULL.tex
execution M book/The-Incompleteness-of-Observation-FULL.pdf
```

The record directory holds this preregistration, the round's frozen controls `controls.py` (stage C1) and the
result note. The receipt path is `verification/receipts/CONSC-2.json`. Every other path the round changes is an
execution path listed above: eight manuscript sources and the eight built artifacts regenerated from four of them.
**No Lean module, no theorem statement, no axiom count, no posit-ledger entry or count, no verification tool or
record, no other manuscript, `verification/ROADMAP.md`, the workflow, and no other round's record change under any
outcome.**

## The objects

- **`D`** = `1a5752d07057895dfa7d793d11a197691bf27a0d`, the head of `main` after round DIM-1 landed (push run
  37317617636, every job green; the act 42 exclusion matrix skipped on push). Every `papers/` and `book/` file is
  byte-identical at `D` to its state at `00ee70a60cf59d421c0056619709459d704fae99`, the base of the advisory audit
  below.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation and the receipt commit, as §A.39 defines them.

## 1. Provenance and scope

**Provenance.** The advisory audit CONSC-1 (charter at pull request #790, head
`0cefaecbf52a22f865e4415617d9e12935f3402d`, an ordinary advisory audit and not a native round; its charter and head are
not changed by this round) was executed read-only from `D` and returned the verdict **TERMINOLOGY-SPLIT**: the
mathematics, the two-axiom count, the lemma set and the posit ledger are unchanged, and the prose uses *observation
occurs* for distinct contents. Its findings, each verified at `D`:

- the companion papers disagree on whether the primitive contains a subject: Methodology §2.1, §2.3 and §6.3 exclude
  one ("**not** 'I exist'"; "It does not deliver a subject"), while Main §1.2 grounds the floor in "a doubting *I*"
  and the book's ch01 and ch03 in the Cartesian *cogito*; Methodology derives the same axioms and lemmas without the
  subject;
- no passage relates the indubitable floor to registrations by systems no one is aware of: ch01 states the floor
  indubitable and, six lines on, that a deck of cards satisfies the definition;
- *observation occurs* carries a content neither axiom yields: Main §1.2 attributes to "the axiom" the commitment
  that our universe admits a C1–C4 partition, while a momentary registering with no persistent record satisfies the
  first axiom and fails (C2) (Main's anti-Boltzmann-brain corollary); Methodology §4.6 and §6.1 already classify C1–C4
  as a selection condition; the book's ch03 and the papers GR and Structure call the starting point an *empirical
  fact* while ch01, ch03 and ch04 call it indubitable;
- the status of V ⊊ S is labelled open in ch01 and settled as an adopted reading (with its cost disclosed) in Main,
  Methodology and Substratum; every source agrees it changes no prediction;
- Chapter 18 contradicts its own status note: the note states a conjecture carrying no evidential weight, while
  §18.10's account is said to make "empirical predictions" and is listed in the chapter's "cumulative case"; ch18:287
  denies consciousness to horizons and proteins outright while ch18:297 states the framework allows panpsychism.

**The editorial principle.** The round separates four notions rather than replacing one word everywhere:

| notion | what it names | consciousness | standing |
|---|---|---|---|
| **minimal registration** (the indubitable structural floor) | that some tokened differentiation is registered — Axiom 1 | not part of its content | indubitable: it cannot coherently be denied from the locus that instantiates the doubt |
| **physical registration / observation** | a particular interaction leaving a record — a detector, a deck, a protein interior, a horizon; any instance of the Definition (S, φ, V) | not required | a physical fact, not indubitable |
| **admitted observer** | a partition satisfying C1–C4 | not required | the C1–C4 selection condition; satisfied in our universe as an empirical matter; not a consequence of Axiom 1 |
| **phenomenal consciousness** | what it is like to be a system | — | not derived; the Chapter 18 conjecture |

The frozen texts of §3 implement this separation at the sites they edit. The round edits no other site; the principle
is recorded so that later edits use the same separation.

**Owner decisions recorded at the freeze.** (1) Disposition TERMINOLOGY-SPLIT; this round carries exactly the pairs
of §3. (2) B3 takes the adopted-reading direction: ch01 is brought into agreement with the papers. (3) P2 places
observer admission under the C1–C4 selection condition; no posit-ledger item is added and no ledger count changes.
(4) Chapter 18 keeps its conjectural status (B8): the consciousness material is labelled conjecture and removed from
the cumulative case, and the categorical denial is reconciled with the stated compatibility. (5) The two companion
paper sites P3 (Structure) and P4 (GR), found while building the predicted tree, are added so that no companion paper
keeps the *empirical fact* statement (§A.25 step 3). They are included because they instantiate the same
already-approved defect with the same correction as B4–B6; their discovery does not reopen the corpus census, and
nothing in this round authorizes a further search-and-expand step after `F`. A site found later is recorded in the
result note for a separate round, not added.

**Frozen out.** Any mathematical file; any theorem statement, lemma, axiom or axiom count; the posit ledger and its
"seven items"; any verification tool, guard, census or record; Methodology and Substratum (the anchors, unchanged);
the Explainer (frozen and superseded, with its standing notice); ch04, ch00, ch02, ch12; Appendix C. Two findings of
the audit are recorded here and not carried: (i) whether a feed-forward architecture fails (C2) or (C4), as
ch18:293 and ch18:327 state for (C2) — a separate physics and cognitive-architecture audit; (ii) Appendix C promises
engagement with cognitive-science objections and carries no objection on whether observation needs a conscious
observer — a separate completeness question. Any wording beyond §3's frozen texts is out of scope; a substitution
that fails to apply halts the round and is not repaired in text.

## 2. The rule of the round

The file at `E` equals the file at `D` with exactly the substitutions of §3: each `old` occurs exactly once in its
file at `D` and its `new` does not occur there (verified before this freeze for all 34 instances). Every book pair is
applied to its chapter source and to `book/The-Incompleteness-of-Observation-FULL.md` with byte-identical `old` and
`new`; a pair applied to one side only is incomplete and fails the round (hard parity). The built artifacts of the
four edited sources that carry them are regenerated in the same commit with `sh ./build.sh Main GR Structure` and
`sh ./build.sh --book`.

## 3. The frozen substitutions

**Scope arithmetic.** Fifteen book substitutions, labelled B1–B9 (B6 carries two and B8 six), each instantiated twice
— once in its chapter source and once in `book/The-Incompleteness-of-Observation-FULL.md` — give 30 instances; four
paper substitutions, P1–P4, give 4 instances. Total: **19 substitutions, 34 governed instances.** Each entry below is
one substitution; its file list names every instance. Old and new are verbatim.

@@TABLE@@

## 4. Re-grep (corpus: `papers/*.md`, `book/*.md`)

Measured at `D` and on the predicted execution tree; the controls require exactly these counts at `E`. The last six
rows are invariants: the round changes no count of axioms, ledger items or primitives.

| phrase | `D` | `E` |
|---|---|---|
@@REGREP@@

## 5. Controls

`controls.py` (stage C1) embeds the 34 instances, the frozen blobs of the eight sources and of the four rebuilt
`.tex` files at `E`, the re-grep table and the scan lists, and implements these checks on a commit:

| code | check |
|---|---|
| P | `delta(D, commit)` is exactly the sixteen governed execution paths, each modified, plus files of the record directory |
| I | at `D` every instance's `old` occurs exactly once in its file and its `new` does not occur |
| S | each source equals `D`'s with exactly its instances substituted, and has its frozen blob |
| M | every non-blank line of each edited chapter occurs in `FULL.md`; each book pair's `new` occurs exactly once in its chapter and exactly once in `FULL.md` |
| T | each rebuilt `.tex` carries the `% source-sha256:` stamp of its source and has its frozen blob |
| B | each rebuilt `.pdf` is a PDF (`%PDF-` header) and differs from `D`'s, i.e. it was regenerated at the commit rather than carried over; PDF bytes are not an invariant, because a rebuild from an identical source differs only in embedded timestamps — the byte-level invariant of a build is its `.tex` (T), and the page counts are recorded in the result note, not frozen |
| R | §A.32/§A.33 register scan of the paper pairs' `new` text; revision-history and caps scans of every `new` text; none of the out-of-scope terms (feed-forward, Appendix C, ledger, Lean, kernel, item and axiom counts) in any `new` text |
| G | the re-grep counts of §4 at `D` and at the commit; the invariant rows unchanged |
| F | with `--freeze F`: the preregistration at the commit equals `F`'s, and `delta(D, F)` is the preregistration |

Its self-test drives each check through the predicted tree built in memory from `D` and through mutations that must
fail: `D` itself (countercontrol), a chapter edit without its `FULL.md` pair, an extra edit in a governed source, a
chapter line absent from `FULL.md`, revision-history voice, meta-commentary in a paper, caps emphasis, an
out-of-scope term, a stale `.tex` stamp, a delta touching a non-governed path, a delta missing a rebuilt artifact, and
an injected invariant phrase.

### Invariants and their checkpoints (§A.41)

| invariant asserted | checkpoint |
|---|---|
| exactly the frozen substitutions, nothing else, in each source | S (both forms), P |
| hard chapter/`FULL.md` parity | M (parity), M (mirror) |
| built artifacts regenerated, not carried over or stale | T, B; release gate `staleness` |
| no axiom count, ledger count or primitive count changes | G (invariant rows) |
| no history voice, no meta-commentary in papers, no caps emphasis | R; release gate `voice` |
| no out-of-scope content added | R (scope terms), P |
| no verification tool, Lean module or record changed | P; the exact-head run's guard and release gate |
| every manuscript-reading check still passes | the exact-head runs at S1 and `E` (release gate: staleness, voice, claims, duplicate, mirror, citation, architecture, dependency-label, coverage, lean-manuscript; the edge-rigidity guard) |
| the control plane is frozen | F |

## 6. Stages

1. **C1** adds `controls.py`, blob `@@CONTROLS_BLOB@@`, to the record directory. Acceptance: the blob is the frozen
   blob and `controls.py --self-test` prints `controls: OK`.
2. **S1** applies the 34 instances of §3 to the eight sources and regenerates `papers/Main.{tex,pdf}`,
   `papers/GR.{tex,pdf}`, `papers/Structure.{tex,pdf}` and the book's `FULL.{tex,pdf}` with `sh ./build.sh Main GR
   Structure` and `sh ./build.sh --book`, in one commit. Acceptance: `controls.py check S1 --freeze F` prints
   `controls: OK`; the build reports no dropped glyph; the exact-head run at S1 has every job green, the release gate
   passing every step.
3. **Repairs**, if needed, touch only the built artifacts (a rebuild); each passes `controls.py check` at its commit.
   A failure a rebuild cannot fix halts the round.
4. **S2** adds the result note `result.md`; this is candidate `E`. Acceptance: `controls.py check E --freeze F`
   passes and the exact-head run at `E` has every job green.

## 7. Outcomes

- **`CONSC-2-APPLIED`** — `controls.py check E --freeze F` prints `controls: OK` and the exact-head run at `E` is green
  on every job. The result note records the substitutions applied, the build report (page counts, dropped glyphs),
  the re-grep table at `E`, and states that the round changes consistency, not correctness: bands unchanged.
- **`CONSC-2-HALTED`** — anything else; the round halts under the specification's `S12`, and the result note names the
  failing check or job.

No outcome changes a theorem, an axiom count, the posit ledger or a verification surface, or asserts anything about
consciousness beyond the conjectural status the frozen texts give it.

## 8. Design evidence (measured before this freeze)

- **Toolchain.** `sh ./build.sh Main GR Structure` and `sh ./build.sh --book` at `D` reproduce all four `.tex` files
  byte for byte (pandoc 3.1.3, TeX Live 2023); the PDFs differ only in embedded timestamps. On the predicted tree the
  builds succeed with no dropped glyph: Main 87 pages (87 at `D`), GR 82 (82), Structure 98 (98), the book 541 (540).
- **Every manuscript-reading check, on the predicted tree.** `toolchain`, `staleness` (13 matched, 0 unstamped),
  `voice`, `voice-scope`, `claims`, `duplicate`, `mirror` (0 chapter lines absent from `FULL.md`), `citation` (112, 0
  broken), `architecture` (259 invariants, 0 violations), `dependency-label --strict`, `coverage` (129 canonical
  statements), `lean-manuscript`, `artifact-placement`; `verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS
  PASS`.
- **`controls.py`** at its frozen blob: `--self-test` OK; `check` on the predicted tree OK on every check but `F`.
@@PREDICTED@@

## 9. Interpretation limits

- The round changes consistency, not correctness: bands unchanged (AGENTS.md honesty conventions).
- The working draft is corrected forward (§A.27, §A.30): no dated notes, no "formerly", no history voice.
- The round introduces no claim: each new text states a distinction the corpus already draws at its anchor
  (Methodology Part I for the primitive and for C1–C4; Chapter 18's own status note for the consciousness
  conjecture).
