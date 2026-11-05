# O-RET Phase B: native-retention design (design only)

**Status: WIP / UNVERIFIED.** A paper-only design. It is not independently reviewed, not frozen
and not authorized to run. It establishes no premise, changes no scientific status and is not a
premise of any established claim (AGENTS.md §A.46 item 7).

## Authorization and scope

- **Authorization:** the owner's grant for the Phase B design unit, recorded at
  [#1032 comment 6649418760](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6649418760)
  (amaybaum, 2026-11-05T04:08:27Z), quoting the owner: "This authorizes Phase B design only—not
  its freeze, implementation, execution or scientific promotion. Obtain independent review of the
  proposed design before requesting further authorization."
- **Designated writer:** `writer-oret`, on branch `research/o-ret-phaseb-design-20261105`, drafted
  from `main` at `f5c281ae10a913ec68fa41b3b839ad0b164979cd` (drafting snapshot `D`).
- **Accountable Issue:** #1032 (O-RET). Dependency index: #914 (master matrix revision 2,
  comment 6563412926, rows O-ACC, O-RDY, O-RET; scoped annotation, comment 6612951653).

**Not authorized, and not done.** No computation, simulation, enumeration, script, probe or Lean
build was run. Phase A was not executed, replayed or re-derived by machine. No workflow was
dispatched. Nothing was frozen or designated. No existing file in `o-ret-routes-20261103/` is
changed: Phase A's frozen inputs, `phaseA/` and `phaseA/run-1/` are read only. No physical premise
is adopted. Nothing is merged or promoted.

## Files

| File | Content |
| --- | --- |
| `README.md` | this note |
| `DESIGN-PHASE-B.md` | (a) starting point; (b) the candidate mechanism; (c) discrimination; (d) assumptions; (e) sourced versus imposed; (f) the proposed Phase B test; (g) owner decisions; review packet; off-`main` references |

## Inputs, read at `D` = `f5c281ae`

- This programme directory on `main`: `README.md`, `DEFINITIONS.md`, `DESIGN-PULSE.md` (r6),
  `SOURCES.md`, `ANNOTATION.md`, `PREREG-PHASE-A.md`, `PHASEA-TUPLES.json`, `PHASEA-EXPECTED.json`,
  `phaseA/IMPLEMENTATION-NOTES.md`, `phaseA/phasea.py` (read as a specification only, not run),
  `phaseA/run-1/RESULT.md`, `REVIEW.md`, `REPLAY.json` and `phase-a/summary.json`.
- `ROUTES.md` at `F` = `49f0bd41c5323d2191b580460c8703740dd01b30`, an ancestor of `main`, read with
  `git show 49f0bd41:verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103/ROUTES.md`.
- `../measurement-record-formation/` (MR-1, frozen): `README.md` and `amendments/MR-star.md`
  §S.1–§S.4 and §C (C-1 to C-7, C.1).
- `papers/SM.md:106–112` (copy form; the state-dependent ring rule), `papers/Main.md:726` (posit
  ledger item (vii)), and the rule-h definition in
  `../native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md` (dynamics block).
- Issues and pull requests (planning and provenance, not evidence): #1032 body and comments
  6567189236 to 6649418760; #914 body and comments 6563412926, 6562546850, 6563417740,
  6561476122, 6612951653; PR #1078 (closed, unmerged); PR #1093 (merged, `3f8d900f`).
- Off-`main` provenance: the O-OBSMU record on `research/o-obsmu-20261104` at `f67b9f0c`
  (reviewed ACCEPT on #1110, not on `main`). Every use is classified in `DESIGN-PHASE-B.md` §9.
- Literature: arXiv:0811.2690v2, abstract page read directly. Every other literature item is
  cited from memory and marked so.

## Headline

Revised after the independent review of `fdacce54` (#1115 c.6649925951, ACCEPT WITH CHANGES) and
the owner's instructions relayed with it. The revision is not re-reviewed. Every derivation is by
hand and is listed in the review packet (`DESIGN-PHASE-B.md` §8). None is an established result.

- **Starting point.** Phase A's 49/49 PASS is confirmed against `phaseA/run-1/phase-a/summary.json`
  and `RESULT.md:42–49`. It calibrates one implementation of the classifier on 49 toy controls.
  It says nothing about native dynamics, sources, access or observers, or about classification
  outside the control set.
- **Paper observations** (§1.3, unreviewed).
  - *Lemma PAD* (CONFIRMING): under `π₀`, nothing is written into a current-slice register of any
    copy-form rule.
  - *Lemma NP* (ELABORATING): a written register fails J-1 at the first hold tick unless site 0's
    neighbours pad the carrier.
  - *Observation D2-T1 and Proposition IP*: under decoder D2, a one-tick pass, and any pass whose
    later hold ticks bring no new input, is guaranteed by the decoder's construction. Such passes
    never count. DT-S13 is a concrete `T = 2` case that fails under D2 with every declared
    assumption holding.
  - *Observation W1* (ELABORATING): an instance of the Phase A classifier on a K1 wavefront, under
    D1′ and a restricted carrier.
  - *Proposition K1-NS*: the reviewer's K1 argument, re-derived. It holds under an explicit
    independence condition (A5): no K1 register reaches storage. It is not adopted. K1 stays in the
    planned tuples and controls, and adoption is gate G-14.
- **Candidate (§2): NRR-1, native ready-register retention.** A fixed declared register (both
  slices as its locus, current slice read) of an in-corpus copy-form rule, written by the step from
  a one-site carrier and held under a preregistered ready-region law `ν_r`.
  - K1 is the native step form (posit (vii)) on a 1-D toy graph.
  - The SM:112 ring rule, taken as physics, is an unadopted F2 extension, E-SDC.
  - `ν_r` (`r ≥ 0`) is imposed (H-sel). Access is declared (H-cur).
- **Discrimination (§3).**
  - Pulse: DIL∃ on the two-slice locus, an observed failure on the extension window, a locality
    gate, `T ≥ T*`, and the `IP = false` condition.
  - Recurrence: gap-free windows, the recurrence rule and a Lemma P consistency exit.
  - Re-supply: J-1 on the outside neighbours.
- **Test (§6).**
  - Instances: K1 and the SM:112 rule on rings of 5 and 8 sites, a fixed register family,
    `r ∈ {−1, 0, 1, 2, ∞}`, `T ∈ {1, 2, 3}`.
  - Rule: Phase A's classifier with amendments B-1 to B-6, each shown to change no Phase A row.
  - Hand-derived controls run first, with hash-seed determinism checked.
  - Verdict: per rule, STORAGE-ROBUST (matched local patterns at both ring sizes), STORAGE-ISOLATED
    or NO-STORAGE, computed from structured output.
- **Sourced or imposed (§5).**
  - Requirements 1 and 3 are imposed.
  - Requirements 2 and 4 are tested, not sourced.
  - Requirement 5 is avoided by labelling the ready region as a premise, not by deriving it.
- **Gate items (§7).** G-1 to G-16. Each gives the alternatives, their consequences, tautology risk,
  new assumptions and a labelled recommendation. No alternative is chosen.
