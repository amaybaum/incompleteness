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

## Headline (revised after the review at #1110 c.6643202940; not re-reviewed)

- **Consumers differ** (`ANALYSIS.md` §1).
  - The representation layer (`S ⇔ D ⇔ Q_fb`) is not a residual-choice consumer.
  - The recurrence-cycle indivisibility verdict depends on the hidden laws only through their
    supports (Theorem SI, which elaborates Main:141).
  - C4-gap existence and window divisibility depend on the measure itself, even at fixed full
    support (countercontrol CC-2). Window divisibility on the native step K1 is open.
  - Specific laws are refuted as invariant by Main:60.
- **Lemma D (conditional).** On K1, provided offsets do not count as selectable interactions
  (D-SEL) and S-L4 holds, no `(Obs, μ)` supplies selectable interactions or confined records.
- **Additional premises.**
  - Main §4.6 is "structural, not measure-theoretic". Conditioning the measure on observer
    presence (H-OC) and the conditioning rule (CR) are therefore new premises, not Main's.
  - The corpus states a low-entropy initial condition (book) and treats initial data as
    solution-specific. No source specifies a state-level preparation event (Q11′).
  - Q11′, conditional on H-OC and CR, is a scoped candidate for consumers L3 and L5 only. It is
    not shown to be minimal.
- **Proposals.** P-R and P-SDC are written out as unadopted proposals with failable controls. No
  independent consequence is identified for either.

## Not authorized, and not done

No computation, probe, script or Lean build was run. No workflow was dispatched. No manuscript,
ROADMAP, frozen record or Lean module is changed. No premise is adopted. O-RET, MR-1 stage 2 and
any O-SET display are not executed, and #1009's NC-1 owner questions are not answered. Nothing is
merged or marked ready for review.
