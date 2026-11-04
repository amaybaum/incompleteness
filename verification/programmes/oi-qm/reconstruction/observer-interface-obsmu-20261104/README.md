# O-OBSMU — observer-interface sourcing, paper assessment

**Status: WIP / UNVERIFIED.** A paper-only research record. Nothing here is independently
reviewed. It establishes no premise, changes no scientific status, and is not a premise of any
established claim (AGENTS.md §A.46 item 7).

## Authorization and scope

- **Authorization:** owner activation of the O-OBSMU workstream, paper-only,
  [#866 comment 6642599988](https://github.com/amaybaum/incompleteness/issues/866#issuecomment-6642599988)
  (amaybaum, 2026-11-04T21:30:05Z), quoting the owner: "Begin with paper-only research and
  independent review. No new computations, experimental runs or scientific promotion without
  separate authorization."
- **Owner guidance relayed by the coordinator, same day:** the target is the smallest missing
  ingredient needed to derive `(Obs, μ)`; every requirement is sorted into (a) already implied by
  OI's existing premises or theorems, with locator and support layer, or (b) a genuinely
  additional assumption; no new posit is adopted, and a candidate ingredient is stated only as a
  proposal awaiting the owner, with its §A.29 controls, an independent consequence and a refuting
  outcome.
- **Designated writer:** `writer-866`. Branch `research/o-obsmu-20261104`, drafted from `main` at
  `f5c281ae10a913ec68fa41b3b839ad0b164979cd` (drafting snapshot `D`).
- **Accountable Issue:** #866 (row O-OBSMU). Dependency index: #914 (master matrix revision 2,
  comment 6563412926, rows O-OBSMU, O-RDY, O-ACC, O-RET, O-REC, O-SET, O-INS).

## Question

Can OI's native dynamics physically supply what an observer interface needs — preparation,
selectable interactions, accessible outcomes, readable persistent records — and can the
stochastic interface `(Obs, μ)` be sourced from the stated architecture, or be shown irrelevant
because the claims consuming the induced law are invariant under the residual choice? If neither,
what is the smallest missing ingredient?

## Files

| File | Content |
| --- | --- |
| `README.md` | this note |
| `ANALYSIS.md` | (a) the O-OBSMU obligation by consumer; (b) the four-capacity gap map; (c) the sourcing and invariance routes, depth-first; (d) the smallest missing ingredient, as an unadopted proposal; (e) owner decisions |

## Inputs, read at `D` = `f5c281ae`

- `papers/Main.md` (Definition and Lemmas 1–3, §1.2–§1.5, §2.3, §3.2, §3.4), `papers/Substratum.md`
  (A5, amplitude-scale gauge), `papers/SM.md` §3.1.
- `verification/lean-mathlib/OIBridge/StochasticInterface.lean` and
  `verification/audits/operational/stochastic-observer-interface-audit.md`.
- `verification/audits/operational/rooted-observer-family-sourcing/result.md`.
- `verification/ROADMAP.md` (frozen; P1 stochastic observer interface section).
- `measurement-record-formation/` (MR-1 frozen preregistration, `amendments/MR-star.md` §S and §M,
  `README.md`, `LA-EQUAL-REVIEW.md`), `physical-coupling-pc1/amendments/PC-star.md` §PC★5,
  `o-ret-routes-20261103/README.md`. Read only.
- Issue comments: #866 c.6526292899, c.6541293037, c.6541615446, c.6548283392, c.6567167742,
  c.6600176951, c.6627392555, c.6631480154, c.6641545083, c.6642599988; #914 c.6563412926;
  #1007 c.6526897139, c.6527637527. These are governance, planning or provenance records, not
  evidence; `ANALYSIS.md` §7 classifies each reference individually (§A.42 item 8).
- Literature, under the owner's arXiv authorization recorded at #866 c.6643204362:
  arXiv:2309.03085v2 §3.1 read directly; the other sources are listed in `ANALYSIS.md` §3.8,
  each marked as read directly or taken from a named secondary source. External results do not
  establish that anything follows from OI's assumptions; where one supplies an ingredient, that
  ingredient is an additional assumption.

## Headline

This head has not been re-reviewed.

- The final review (#1110 c.6643749363) returned ACCEPT for `cd15123b` only.
- The extension at `478451b5` was reviewed in #1110 c.6644159894 (ACCEPT WITH CHANGES). This head
  applies those changes.

- **Consumers differ** (`ANALYSIS.md` §1).
  - The representation layer (`S ⇔ D ⇔ Q_fb`) is not a residual-choice consumer.
  - Recurrence-cycle indivisibility depends on the hidden laws only through their supports
    (Theorem SI, which elaborates Main:141).
  - C4-gap existence and window divisibility depend on the measure itself, even at fixed full
    support (CC-2). Window divisibility on the native step K1 is open.
  - Specific laws are refuted as invariant by Main:60.
- **Conditioning and preparation groups** (`ANALYSIS.md` §4.1, §4.6.4):
  - (1) orbit-level records conditioning: b-stated.
  - (2a) CR_rec, the present-value conditional and the in-realization history posterior (Main:88,
    :99, :105): a construction step, **proposed and pending owner decision D-OB7**.
  - (2b) conditioning on stipulated events beyond the records: b-new.
  - (3) preparation data, as a category: b-stated.
  - (4a) cosmic initial data:
    - gauge freedom is identified only for structural data (deep-sector cardinality, the
      representative of `φ`), not for the initial configuration (ch19:200, uninvestigated);
    - other items enter as theorem hypotheses or stated commitments, and isotropy (ch19:198) is
      speculative;
    - the microstate is unexplained, and no generating principle is identified;
    - #1112 is the accountable home.
  - (4b) laboratory preparations reduce, conditionally, to (2a), via the open identification
    H-PREP, plus retained records and (4a) for record reliability. Retained records are open and,
    on K1, tied to the unsourced ready region (O-RDY). Creating a preparation is unexplained
    (O-SET).
- **The obstacle for the μ leg and for preparation-dependent laws** is preparation content. The
  conditional answer (§4.6.3) has two parts:
  - **The condition.** H-PREP, D-OB7 and retained records must hold, and record reliability must
    be read within Lemma Q-b2's scope (time-reversal-invariant dynamics; on K1, configuration-only
    record events).
  - **The answer.** Under that condition, laboratory preparations need no observer-specific
    assumption beyond CR_rec. Their independent inputs are then the time-asymmetric data of (4a),
    O-REC/O-RDY, and O-SET.
- **Lemma D, on K1, under the native linear rule.**
  - Selectable interactions are blocked, conditional on D-SEL.
  - Marking does not destroy interference (S-L5). S-L5 is PD in a frozen record, reworded by
    MR★ C-9, and not independently reviewed here.
  - Under S-L4, no confined pattern persists over `2w + 2` slices. S-L4's review is reported in
    the frozen record and not re-verified here; it assumes `ℤ^d`, or a torus with `N ≥ 5w + 2`,
    and `a` injective.
  - This does not show that localized records are impossible (MR★ C-2), and the trace route is
    `UNDECIDED` (MR★ C-4).
- **Proposals.** P-R and P-SDC are unadopted proposals with failable controls. No independent
  consequence is identified for either.
- **Arrow of time.** This is tracked in #1112 (analysis c.6643691865, verification c.6643840329)
  and recorded here only.

## Not authorized, and not done

No computation, probe, script or Lean build was run. No workflow was dispatched. No manuscript,
ROADMAP, frozen record or Lean module is changed. No premise is adopted. O-RET, MR-1 stage 2 and
any O-SET display are not executed, and #1009's NC-1 owner questions are not answered. Nothing is
merged or marked ready for review.
