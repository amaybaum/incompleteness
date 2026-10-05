# Manuscript round CONSC-2 — observation terminology: registration, observation, admitted observer: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #792.

- **`D`** — `1a5752d07057895dfa7d793d11a197691bf27a0d`, the head of `main` after round DIM-1 landed, certified by push
  run 37317617636.
- **`F`** — `f34f01d227b79032bd0940387225ebbfd7ad708b`, single parent `D`; `delta(D, F)` is the preregistration alone,
  blob `46d4bfd8682d5b1d999d3c91cac16b14e940dba2`. Its exact-head `workflow_dispatch` run 37337331051 concluded
  `success` with all 32 jobs succeeded, its `check-run` attestation; the owner designated `F` (comment 5998740445).
  That run attests the control plane only.
- **Shape** — non-sealing; stages C1 and S1 and this note (S2).

**Outcome:** `CONSC-2-APPLIED`

The nineteen frozen substitutions — 34 governed instances: fifteen book substitutions B1–B9, each in its chapter source
and in `book/The-Incompleteness-of-Observation-FULL.md` (30 instances), and four paper substitutions P1–P4 (4
instances) — are applied exactly, and the built artifacts of the four edited sources that carry them are regenerated.
The edited sites now separate four notions:

- **minimal registration**, the indubitable structural floor (Axiom 1): that some tokened differentiation is
  registered, indubitable from the locus that instantiates the doubt, with no thinking subject in its content (B1, B6,
  P1);
- **physical registration / observation**: any instance of the Definition — a detector, a deck, a protein interior, a
  horizon — whose occurrence is a physical fact, not an indubitable one, and which requires no consciousness (B2, B7,
  B9, P1, and the removal of *empirical fact* from the statement of the starting point in B4, B5, B6, P3, P4);
- **admitted observer**: a partition satisfying C1–C4, the selection condition, which a momentary registering with no
  persistent record does not meet (P2); the adopted reading on which V ⊊ S follows from Axiom 1, with its alternative
  costing a further posit (B3);
- **phenomenal consciousness**: Chapter 18's conjecture, with Direction 1 labelled a conjecture and Direction 2 a
  consequence of the definition, the framework's notion of evidence stated as perspective-neutral, no categorical
  attribution or denial of experience, and no place in the cumulative case for the core framework (B8).

No theorem statement, lemma, axiom or axiom count, posit-ledger entry or count, verification tool, guard, census,
record or Lean module changed. The round changes consistency, not correctness: bands unchanged.

***

## The execution

| commit | content | exact-head run on that commit | conclusion |
| --- | --- | --- | --- |
| `F` = `f34f01d2` | the preregistration | 37337331051 | `success`, all 32 jobs; release gate PASS, the census of `D` |
| `C1` = `322ef2c18b9e4e2bd2e83adec5c98e3ea555dc63` | stage C1: `controls.py`, blob `57ec7db0` | none required | `controls.py --self-test`: `controls: OK -- 20 checks` |
| `S1` = `57889fee5ab776a1426a3ab464d29190ae1ba5ae` | stage S1: the 34 instances and the rebuilt `papers/Main`, `papers/GR`, `papers/Structure` and book `FULL` `.tex`/`.pdf` | 37340470069 | `success`, all 32 jobs |

Each commit has one parent, the row above it. `controls.py check S1 --freeze F` prints `controls: OK -- 23 checks`:
paths (exactly the sixteen governed execution paths, each modified), instances, the eight sources equal to `D`'s with
exactly their instances substituted and at their frozen blobs, the mirror and hard chapter/`FULL.md` parity, each
`.tex` stamp and frozen blob, each PDF rebuilt, the register/history/caps/scope scans, the re-grep and invariant
counts, and the freeze.

Run 37340470069 is a `workflow_dispatch` run whose `head_sha` is `S1`, attempt 1, run to completion with no job
cancelled:

- the Lean kernel check (job 111865971498), the Mathlib bridge (job 111865971933), the 29 numerical-probe shards and
  the probe aggregate (job 111873978477) each concluded `success`;
- the release gate passed every step: `staleness` 13 matched, 0 unstamped (the four rebuilt `.tex` stamps match their
  edited sources); `voice`; `claims`; `duplicate`; `mirror` 0 chapter lines absent from `FULL.md`; `citation` 112, 0
  broken; `architecture` 259 invariants, 0 violations; `dependency-label`; `coverage` 129 canonical statements;
  `lean-axioms` 5702 named results, no `sorryAx`; `lean-manuscript`; 303 legacy records intact; 33 receipts hold.

## The build

`sh ./build.sh Main GR Structure` and `sh ./build.sh --book` at S1 (pandoc 3.1.3, TeX Live 2023) succeeded with no
dropped glyph. Page counts: Main 87, GR 82, Structure 98, the book 541 (87, 82, 98, 540 at `D`). The four `.tex` files
have the frozen blobs of the predicted execution tree; the PDFs are regenerated at S1 and are not byte invariants.

## Re-grep at S1 (corpus: `papers/*.md`, `book/*.md`)

| phrase | `D` | `S1` |
|---|---|---|
| a doubting *I* | 1 | 0 |
| empirical fact that observation occurs | 5 | 0 |
| foundational empirical commitment | 2 | 0 |
| is an open question — one that bears on how the framework describes the minimality | 2 | 0 |
| nothing it is like to be the cosmological horizon | 2 | 0 |
| consciousness as structural necessary condition | 2 | 0 |
| is not speculative addition to an empirical base | 2 | 0 |
| who is a substructure of the system they are trying to describe | 2 | 0 |
| The axiom thus commits | 1 | 0 |
| without its thinking subject | 0 | 4 |
| nothing in the definition requires | 0 | 6 |
| C1–C4 selection condition | 0 | 1 |
| two-axiom | 23 | 23 |
| two axioms | 35 | 35 |
| Seven items | 1 | 1 |
| posit ledger | 8 | 8 |
| third axiom | 3 | 3 |
| cogito | 11 | 11 |

The last six rows are the invariants: no count of axioms, ledger items or primitives changes.

## Design evidence

The predicted execution tree `cd273c0949b90459ee2fdbd5c45523232fe10b55` with run 37334884651 (all 32 jobs `success`) and
the measurements recorded in the preregistration are design evidence, not attestations; the pull-request runs on this
branch are not attestations.

## What stays open

Recorded at the freeze and not carried by this round: whether a feed-forward architecture fails (C2) or (C4), as
ch18:293 and ch18:327 state for (C2); and Appendix C's engagement with whether observation needs a conscious observer.
Each belongs to a separate round.
