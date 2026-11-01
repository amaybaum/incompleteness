# MR-1 stage 1 — amendment KS-S: substitute primary sources for the Kochen–Specker reading gate

**Status: append-only amendment.** The frozen preregistration
`../preregistration.md` at `1a236f332e8ea12b7fdb125bf8c5098ccd71d36c` is unchanged. This amendment
changes no definition, predicate, outcome, countercontrol, benchmark or decision rule. It proposes no
CC2 construction and fixes no `K★`. It is subject to independent review before use. No computation
evaluating any physical, candidate, control or algebraic quantity was run for it.

**Readings.** Entries LIT-4 (Bell 1966) and LIT-5 (Mermin 1993) of `stage1-log.json` in this
directory. Entry LIT-3 (Kochen–Specker 1967) is unchanged.

***

## 1. Authority and boundaries

Owner decision (Option 2), given in chat on 2026-11-01 and recorded on PR #1023 in comment
6553497955, replying to the stop in comment 6549290592. The boundaries, quoted from that comment:

> **Boundaries set by the owner:**
> - The substitution is recorded through an **append-only, independently reviewed amendment**. The frozen commit `1a236f33` stays unchanged.
> - Both substitute sources are **read first-hand in full**. Their exact relevant claims, limitations and provenance are recorded.
> - An **independently justified concrete CC2 model, with its OI-held constraint, is established before `K★` is frozen**.
> - **If that construction cannot be justified, the literature gate stays unresolved.** CC2 and the nonclassicality criterion are not weakened.
> - There is **no candidate screening until the reviewed `K★` is frozen**, and **no computation until the reviewed stage-1 freeze**.
> - The completed Mazurek and Catani readings remain valid. #1022 is unchanged. #1023 stays draft and unmerged, and there is **no stage-2 authorization**.

The same comment records: "The owner noted that Mermin is not a direct substitute for the original
Kochen–Specker spin-½ model. Neither reference automatically supplies the disturbing-marker extension
that CC2 requires." It names the substitute sources as J. S. Bell, *Rev. Mod. Phys.* 38, 447 (1966),
and N. D. Mermin, *Rev. Mod. Phys.* 65, 803 (1993), with "Mermin's published corrections".

## 2. What is substituted, and for what

- The Kochen–Specker 1967 gate stays **NOT-MET** as a record (LIT-3, unchanged): only pp. 59–68 of
  59–87 were obtained.
- Bell 1966 and Mermin 1993 substitute for it **in the CC2-instance role only**: the literature input
  to the CC2 row of §5.8 (frozen L569) and to its fixing constraint (frozen L561–562). They are not
  substituted for any other citation in the frozen text.

## 3. Claims consumed

**Bell 1966** (LIT-4; both full copies read, pp. 447–452):
- **(B-a)** For a two-dimensional system there is an explicit deterministic model, eq. (3), p. 448,
  reproducing every single-measurement expectation value for a pure state `ψ`. Its dispersion-free
  states have additive expectation values only for commuting operators (p. 449); it is not
  contextual in the Kochen–Specker sense. Condition: single measurements only; no measurement
  dynamics.
- **(B-b)** For state-space dimension greater than two, no dispersion-free state satisfies additivity
  of expectation values for commuting operators (§V, pp. 450–451, a corollary of Gleason's theorem;
  "it is here that we need three dimensions at least"). Condition: the argument is a continuity
  argument over all vectors, so it constrains value assignments to all rays, not to a finite set.
- **(B-c)** In any dimension there is an explicit deterministic contextual model reproducing the
  single-context statistics (p. 451): the result for a projector "depends also on the choice of the
  others", with the tacit noncontextuality assumption named in the diagnosis that the result "may
  reasonably depend … on the complete disposition of the apparatus". Bell calls it "very artificial".

**Mermin 1993** (LIT-5; arXiv:1802.10119v1 read in full, pp. 1–27):
- **(M-a)** The theorem's assumptions: value definiteness, eigenvalue values, functional composition
  (eqs. 1–3) and noncontextuality, named on p. 18 as the tacit assumption that an observable gets the
  same value whichever commuting set it is measured with.
- **(M-b)** The four-dimensional square (§V, pp. 15–16): no assignment to its nine observables
  satisfies those assumptions, for any state.
- **(M-c)** Deterministic models escape only through context or apparatus dependence (§X, p. 24); a
  necessity statement, not a construction.

## 4. Findings

- **Neither source supplies the disturbing-marker extension of CC2.** On disturbing readout, Bell is
  partial: outcomes depend on the context, but no measurement dynamics and no post-measurement state
  are given. Mermin gives none. Neither source has a marker, a record system or a sequential readout.
- **Bell's models are per-law constructions.** Their parameters and rotation are built from `ψ`'s own
  quantum expectations, so they are of the CC8 kind and agree with PC-Q on single measurements by
  construction. A CC2 instance is distinguished from CC8 only by a construction fixed by K1 (the one
  native `φ`, frozen L561–562), not by these sources.
- **Kochen–Specker-type contextuality needs dimension at least three.** On the two-dimensional carrier
  alone, Bell's model (B-a) is not contextual in that sense; a KS-type obstruction arises only on a
  larger system, for example carrier together with marker (dimension four).
- **The contextuality notion differs from U2's.** Mermin's and Bell's contextuality is measurement
  contextuality of value assignments. Corollary U2 (frozen L340) rests on Spekkens 2005 preparation
  contextuality, and neither source substitutes for that citation. Nothing conflicts.

## 5. The Mermin errata gap

The corrected arXiv text was read; the text of the two published errata (*Rev. Mod. Phys.* 88,
039902 (2016); 89, 049901 (2017)) was not obtained. The arXiv preface states that it corrects "three
small errors" without naming them. Coverage of each Mermin claim by Bell:

| Mermin claim | Covered by Bell 1966 | Status |
|---|---|---|
| M-a, the assumptions, noncontextuality named | yes: the tacit assumption named in the §V diagnosis, p. 451 | usable |
| M-c, escape only through context or apparatus dependence | yes, for value assignments to all rays: B-b gives the obstruction in dimension ≥ 3, B-c the contextual escape | usable in that form |
| M-b, the finite four-dimensional square | no: B-b concerns assignments to all rays and gives no finite set | **blocked** until the errata are read |
| M-c restricted to a finite menu of observables | no: it rests on a finite-set theorem such as M-b | **blocked** until the errata are read |

No CC2 decision rests on a Mermin claim alone until the errata text is read. A CC2 instance whose
contextuality argument needs a finite set of observables (rather than all rays) is blocked on that
point.

## 6. Status

- The literature input for the Kochen–Specker role is first-hand: Bell 1966 in full, and Mermin 1993
  in full in its corrected arXiv text, subject to §5.
- **The concrete CC2 construction is not established by these sources:** a Kochen–Specker-type
  deterministic model fixed by K1, with disturbing readout and a disturbing marker, and with its
  OI-held constraint. It is the next obligation and must be independently justified before `K★`.
- **`K★` stays blocked** until that construction is justified and reviewed. If it cannot be justified,
  the gate stays unresolved, and CC2 and the nonclassicality criterion are not weakened.
- No candidate screening precedes a reviewed `K★`; no computation precedes the reviewed stage-1
  freeze.

***

## 7. Review corrections

Source: independent review of `da558a8c`. The text above is kept as written; these corrections
supersede the passages named. The same corrections are recorded in `stage1-log.json` under
`corrections` (REV-1 to REV-7).

- **REV-1 (§6, first status line; LIT-5 gate).** Mermin 1993 is **PARTIAL**, not met: the corrected
  arXiv text is read first-hand in full, but the owner's decision requires Mermin's published
  corrections to be considered, and the errata text was not obtained. The gate stays open on that
  point, and the gap is referred to the owner. The first status line reads: the literature input for
  the Kochen–Specker role is first-hand from Bell 1966 in full; Mermin 1993 is partial, its errata
  unread.
- **REV-3 (§4, second finding).** Bell's models are **ψ-ontic**, not per-law constructions of the CC8
  kind. The spin-½ model, eq. (3), has ontic state `(ψ, λ)` with `λ` on a continuum and fixes the
  outcome of every single measurement on the system; it reproduces the quantum single-measurement
  statistics by construction. The p. 451 contextual model is also ψ-ontic and per state: its
  thresholds are cumulative quantum expectations in `ψ` of the projectors one apparatus measures, it
  is defined for every such context with an order fixed by the set of projectors, and it reproduces
  the single-context statistics by construction. Neither is a K1-fixed construction; the conclusion
  that no CC2 instance is supplied stands.
- **REV-4 (§5 table).** Two further Mermin-only items: the **product rule** of functional
  composition, Mermin eqs. (1)–(2), on which the square depends (Bell 1966 uses additivity for
  commuting operators only), **blocked** until the errata are read; and the agreement with Corollary
  U3 (Mermin p. 23), Mermin-only and not load-bearing.
- **REV-2 (literature log, LIT-1).** The PRL proof of the predictability–visibility bound assumes a
  finite ontic space. A W1 through that bound excludes only finite-`Λ` noncontextual models;
  separating CC1 or any continuum-`λ` model through it needs its own extension.
- **REV-5 to REV-7 (literature log only).** Paraphrased reader regexes are labelled; the SC-42 scan
  covers `*.md` and `*.py` only and never scanned the JSON log; the log's `readers` and
  `computation_statement` fields predate the 2026-11-01 readings of Bell and Mermin and the one
  read-only GitHub connector call.

## 8. Errata status

Sources: owner comment 6554185786 on PR #1023; `stage1-log.json`, `lit5_errata` (`LIT-5-ERRATA`)
and correction REV-8. The text above is kept as written.

- **Three errata, not two.** Crossref confirms three notices to Mermin 1993:
  - E1, *Rev. Mod. Phys.* 85, 919 (2013-06-28);
  - E2, 88, 039902 (2016-07-15);
  - E3, 89, 049901 (2017-12-28).

  §5's "the two published errata" reads "the three published errata", E1 included.
- **None was read first-hand.** Every full-text route returned a Cloudflare challenge or HTTP 403,
  or lies outside the session's allowed domains. The routes are listed in `LIT-5-ERRATA`.
- **The owner's summary (owner provenance, not a first-hand read):**
  - E1: p. 811, "contextual" corrected to "noncontextual";
  - E2: the Fig. 4 caption, "three observables in six groups" corrected to "four observables in five
    groups";
  - E3: p. 814, "noncontextuality" corrected to "contextuality".
- **Consistency of E2 with the arXiv text.** It agrees: arXiv p. 17 has "groups of four on 5
  intersecting lines". That passage concerns the eight-dimensional star, which MR-1 does not consume.
- **E1 and E3 are unmapped.** Their arXiv locations are not known without the journal layout. The
  candidates are §VII pp. 19–20 and §IX–X pp. 23–24. They may bear on the noncontextuality
  statements of pp. 18–19, the necessity statement of p. 24 (M-c) and the Bohm statement of p. 23.
- **LIT-5 stays PARTIAL.** M-b, the product rule and the finite-menu form of M-c stay blocked, as in
  §5 and REV-4.
- **What depends on them under D3:** nothing. Under amendment D3 (`D3-CC2-class-level.md` §D3.5), no
  step rests on a Mermin-only claim. M-a and the all-rays form of M-c rest on Bell 1966. The
  Kochen–Specker literature gate stays recorded as unresolved.
- **The first-hand read remains open.** The owner requires a first-hand read of the three notices
  (comment 6554185786). That requirement is not met, and LIT-5 stays PARTIAL until it is.
- **The arXiv locations above are not a mapping.** The candidate locations given for E1 and E3 are
  the errata reader's inference. Recorded as REV-9 and REV-10 in `stage1-log.json` under
  `d3_review_corrections`.
