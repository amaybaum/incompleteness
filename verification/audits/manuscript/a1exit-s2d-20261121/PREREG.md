# A1-EXIT Step 2, unit S2-D — global-phase statements and the inflow endpoint: preregistration

**Status.** Writer's preregistered edit list, WIP / UNVERIFIED. Independent non-author review is
required; merge is a separate owner decision. Manuscript corrections only; no physical premise is
added, no conditional mechanism is promoted, and no §A.23 correctness band moves (bands unchanged:
consistency work).

**Authorization.** Owner `amaybaum`, 2026-11-21,
[#1169 comment 7056875845](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7056875845):
units S2-A to S2-E. Limits as recorded there: manuscript corrections only and only in this unit's
scope; A1 and Main ledger item (ii) are not deleted and the pointer sites are not rewritten; no
merge; no workflow dispatch.

**Goal link (§A.47).** The A1-exit objective (#1169). This unit decides whether the global-phase
statements of row X-63 and the inflow sentence of row X-82 (Sub:56) can be made true without A1:
as the proved region-level result W*, or as an open statement.

**Base.** `main` at `1c7eedc40`. `M:n`, `Sub:n`, `Str:n`, `Cx:n`, `ch02:n`, `ch04:n`, `FULL:n` are
line `n` of `papers/Main.md`, `papers/Substratum.md`, `papers/Structure.md`, `papers/Complexity.md`,
`book/ch02-substratum.md`, `book/ch04-methodology.md` and
`book/The-Incompleteness-of-Observation-FULL.md` at the base. The A1-EXIT ledger's line numbers
(pin `e837e3db`) coincide with the base at every site below (checked by exact-string search).

## Sources (all on `main`)

- A1-EXIT ledger, `verification/audits/foundations/a1exit-ledger-20261120/`: rows X-63, X-82, X-62
  and their sitemap entries.
- Stage 1(ii) audit, `verification/audits/foundations/r1-l8-stage1ii-20261120/AUDIT.md`: rows
  T6, T7a, T7b, T11a–T11d, T12, T14–T16, T17a, T17b, T18, T20a, T20b, T22; finding G3; §6 (W*);
  §8 (theorem-recovery note).
- Main:764 unit, `verification/audits/manuscript/a1exit-main764-20261120/LEDGER.md`: N3, N4.
- REMAINDER §5 (O-INFLOW), `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md`.

## Decision rule (fixed before editing)

For each X-63 site the audit classifies NOT FOLLOWING:

1. Where the site's content is the region-level exclusion with a phase label (G3: the label
   discriminates nothing in the iterated description), restate it as W*: (C2-slow) observers occur
   only outside regions whose effective channel satisfies (EM) at τ_mix ≪ τ_S, in the iterated
   description. Every hypothesis the site already carries ((EM), the rate condition, the iterated
   description, C2 in its timescale form, finite bijective model) is kept.
2. Where the site's content is not reducible to W* (the past-hypothesis replacement, T11c, which
   selects global configurations), state it as open.
3. Nothing is strengthened. A region-level statement retained by the audit (T7a, T11a, T11d, T17a,
   T20a) is not touched beyond moving the rate condition that already governs it (E3).

For X-82 at Sub:56: the sentence relied on finiteness to settle the replacement; the replacement is
stated open independently of finiteness, and the incoming-stream question is kept open where the
carrier is infinite.

For N4: the lead-ins become consistent with the landed typical-state statement, which is a
statement about a finite-dimensional shell (M:732 Scope: "the canonical-typicality clause … [is a
statement] about the finite representative"; X-62 exit).

## Sites located at the base

| Audit row | Site | Unit | Edit |
|---|---|---|---|
| T22 | M:748 (§4.6 heading) | S2-D | E1 |
| T6 lead-ins (N4) | M:764 | S2-D | E2, E3 |
| T7b | M:764 | S2-D | E4 |
| T11b | Sub:56 | S2-D | E5 |
| T11c; X-82 | Sub:56 | S2-D | E6 |
| T12 | Sub:401 | S2-D | E7 |
| T14 | Sub:542 (two clauses) | S2-D | E8, E9 |
| T15 | Str:718 | S2-D | E10 (E11 consequence) |
| T16 | Str:734 | S2-D | E12 |
| T17b | Cx:212 (the audit's "Comp:212") | **S2-E** (sitemap: `papers/Complexity.md:212`, row X-82, owner "Q3 propagation") | none here; wording to S2-E in RESULT |
| T18 | ch02:192 = FULL:822 | S2-D | E13–E16 |
| T20b | ch04:178 = FULL:1282 | S2-D | E17, E18 |
| T6 (the step itself) | M:764 | corrected by PR #1463 (X-62) | none |

These are the twelve NOT FOLLOWING rows (T6, T7b, T11b, T11c, T12, T14, T15, T16, T17b, T18, T20b,
T22). X-82's other sites, Cx:212 and ch18:40 = FULL:4771, are Q3 sites owned by S2-E.

The X-63 sitemap also lists ch03:58, ch04:36, Sub:407 (Phase-2 disposition N: "sufficient condition
stated") and Meth:283, Meth:441 (Q3). Each states the region-level exclusion (bounded-diameter
partitions, fast-mixing equilibria, the iterated coarse description) without a phase conclusion; no
edit from this unit. M:171 (T10) and M:750 (T9) are RETAINED pointers and are not edited.

## Edits

### E1 — `papers/Main.md:748` (X-63; source T22)

Finding: STAGE1ii T22 NOT FOLLOWING; G3.

Old (unique in its file):

````text
### 4.6 Structural Exclusion of Equilibrium-Phase Observers
````

New:

````text
### 4.6 Structural Exclusion of Observers from Fast-Mixing Regions
````

### E2 — `papers/Main.md:764` (X-63 (line mapped to X-62); source Main:764 LEDGER N4; T6)

Finding: N4: lead-in worded for the global-phase conclusion; the landed [31] statement is a finite-dimensional shell statement (M:732 Scope, finite representative; X-62 exit).

Old (unique in its file):

````text
Under $\tau_{\rm mix}\ll\tau_S$: For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies that,
````

New:

````text
For an equilibrium macrostate of a finite representative of $(S, \varphi)$, canonical typicality [31] implies that,
````

### E3 — `papers/Main.md:764` (X-63 (line mapped to X-62); source Main:764 LEDGER N4; T7a)

Finding: N4: the rate condition carried by the removed lead-in is the hypothesis of the region-level exclusion T7a (RETAINED); it moves to that sentence unchanged in content.

Old (unique in its file):

````text
No bounded-diameter partition supports (C2-slow) in that description.
````

New:

````text
Under $\tau_{\rm mix}\ll\tau_S$, no bounded-diameter partition supports (C2-slow) in that description.
````

### E4 — `papers/Main.md:764` (X-63; source T7b)

Finding: STAGE1ii T7b NOT FOLLOWING as worded; W* (§6); G3.

Old (unique in its file):

````text
In that description, with (C2) read in its timescale form, the framework's observers therefore exist only in the non-equilibrium phase of $(S, \varphi)$. Within that description, observers exist where (C1)–(C4), with (C2) read as (C2-slow), are satisfiable, and (C1)–(C4), so read, are not satisfiable in the coarse-grained description of the equilibrium phase.
````

New:

````text
In that description, with (C2) read in its timescale form, the framework's observers therefore occur only outside regions whose effective channel satisfies (EM) at $\tau_{\rm mix}\ll\tau_S$. Within that description, observers exist where (C1)–(C4), with (C2) read as (C2-slow), are satisfiable, and (C1)–(C4), so read, are not satisfiable in the coarse-grained description of such a region.
````

### E5 — `papers/Substratum.md:56` (X-63; source T11b)

Finding: STAGE1ii T11b NOT FOLLOWING as worded; W*; G3.

Old (unique in its file):

````text
are nonetheless structurally restricted to the non-equilibrium phase of $(S, \varphi)$:
````

New:

````text
are nonetheless structurally excluded from regions whose effective channel mixes in a time short compared with $\tau_S$:
````

### E6 — `papers/Substratum.md:56` (X-63; X-82; source T11c; INFLOW (C10))

Finding: STAGE1ii T11c NOT FOLLOWING (W* selects regions, not global configurations; under (LE) the replacement does not follow on a finite carrier either); X-82: the sentence relied on finiteness to settle the replacement.

Old (unique in its file):

````text
In that description, for a finite bijective $(S,\varphi)$, this replaces the low-entropy "past hypothesis", in its role of selecting observer-compatible configurations, with a structural observer-selection rule and excludes Boltzmann brains structurally rather than anthropically. Without A1 this replacement is open: on an infinite carrier
````

New:

````text
In that description, for a finite bijective $(S,\varphi)$, this excludes Boltzmann brains structurally rather than anthropically. Whether it replaces the low-entropy "past hypothesis", in its role of selecting observer-compatible configurations, with a structural observer-selection rule is open, since the rule selects regions rather than global configurations. Without A1 the question also concerns an incoming supply: on an infinite carrier
````

### E7 — `papers/Substratum.md:401` (X-63; source T12)

Finding: STAGE1ii T12 NOT FOLLOWING as worded; W*; G3 (the attribution to (EM) is accurate for W*).

Old (unique in its file):

````text
The observer's confinement to the non-equilibrium phase of $(S, \varphi)$, with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), is a structural consequence of the effective-mixing hypothesis, for sufficiently fast-mixing equilibria ($\tau_{\rm mix} \ll \tau_S$), in the coarse-grained description generated by iterating the one-step effective channel. The confinement is time-symmetric
````

New:

````text
The observer's exclusion from regions whose effective channel mixes fast ($\tau_{\rm mix} \ll \tau_S$), with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), is a structural consequence of the effective-mixing hypothesis, in the coarse-grained description generated by iterating the one-step effective channel. The exclusion is time-symmetric
````

### E8 — `papers/Substratum.md:542` (X-63; source T14)

Finding: STAGE1ii T14 NOT FOLLOWING as worded; W*: regions with fast (EM) are free of (C2-slow) observers in the iterated description; G3.

Old (unique in its file):

````text
Second, the *equilibrium phase* of $(S, \varphi)$ is, by the structural observer-selection theorem and with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), observer-free for sufficiently fast-mixing equilibria ($\tau_{\rm mix} \ll \tau_S$) in the coarse-grained
````

New:

````text
Second, *regions whose effective channel mixes fast* ($\tau_{\rm mix} \ll \tau_S$) are, by the structural observer-selection theorem and with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), observer-free in the coarse-grained
````

### E9 — `papers/Substratum.md:542` (X-63; source T14)

Finding: same sentence family as T14: the closing attribution restates the phase restriction.

Old (unique in its file):

````text
and from the observer-selection theorem's restriction of observers to the non-equilibrium phase
````

New:

````text
and from the observer-selection theorem's exclusion of observers from fast-mixing regions
````

### E10 — `papers/Structure.md:718` (X-63; source T15)

Finding: STAGE1ii T15 NOT FOLLOWING as worded; W* with the observer-relevant regions at every time; G3.

Old (unique in its file):

````text
Under the effective-mixing hypothesis and for sufficiently fast-mixing equilibria ($\tau_{\rm mix} \ll \tau_S$), substrata in perpetual equilibrium cannot satisfy
````

New:

````text
Under the effective-mixing hypothesis, substrata whose observer-relevant regions all have effective channels mixing with $\tau_{\rm mix} \ll \tau_S$ at every time cannot satisfy
````

### E11 — `papers/Structure.md:718` (X-63; source T16 (consequence))

Finding: the bullet label is the feature name Str:734 cites as 'non-equilibrium-phase'; T16 places the condition on the observer's region, not on a global phase; the label follows E12 so the reference resolves.

Old (unique in its file):

````text
- *Non-equilibrium phase:* $\varphi$ admits phases
````

New:

````text
- *Local mixing rate:* $\varphi$ admits phases
````

### E12 — `papers/Structure.md:734` (X-63; source T16)

Finding: STAGE1ii T16 NOT FOLLOWING as worded: W* gives a necessary condition on the observer's region (no fast (EM)), not on a global phase; the 'typically lack' claim is not traced and is unchanged.

Old (unique in its file):

````text
the coupled-dynamics, non-equilibrium-phase, and high-capacity features
````

New:

````text
the coupled-dynamics, slow-local-mixing, and high-capacity features
````

### E13 — `book/ch02-substratum.md:192` (X-63; source T18)

Finding: STAGE1ii T18 NOT FOLLOWING as worded; W*; G3.

Old (unique in its file):

````text
— restricts observers satisfying C1–C4, with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), to the non-equilibrium phase of $(S, \varphi)$; the restriction is time-symmetric
````

New:

````text
— excludes observers satisfying C1–C4, with C2 read in its timescale form (record persistence and readback there being suppressed, not excluded), from regions whose effective channel mixes that fast; the exclusion is time-symmetric
````

### E14 — `book/ch02-substratum.md:192` (X-63; source T18)

Finding: same sentence family as T18: the closing open statement names the phase as selected.

Old (unique in its file):

````text
That the selected non-equilibrium phase is ordered by this growth is not established.
````

New:

````text
That the regions where observers can exist are ordered by this growth is not established.
````

### E15 — `book/The-Incompleteness-of-Observation-FULL.md:822` (X-63; source T18 (FULL mirror of E13))

Finding: §A.14 mirror.

Old and new strings: identical to E13 (unique in FULL.md).

### E16 — `book/The-Incompleteness-of-Observation-FULL.md:822` (X-63; source T18 (FULL mirror of E14))

Finding: §A.14 mirror.

Old and new strings: identical to E14 (unique in FULL.md).

### E17 — `book/ch04-methodology.md:178` (X-63; source T20b)

Finding: STAGE1ii T20b NOT FOLLOWING as worded; W*; G3.

Old (unique in its file):

````text
*The equilibrium phase of $(S, \varphi)$.*
````

New:

````text
*Fast-mixing regions of $(S, \varphi)$.*
````

### E18 — `book/The-Incompleteness-of-Observation-FULL.md:1282` (X-63; source T20b (FULL mirror of E17))

Finding: §A.14 mirror.

Old and new strings: identical to E17 (unique in FULL.md).


## Mirrors (§A.14, §A.25)

- ch02:192 ↔ FULL:822 (E13/E14 ↔ E15/E16), ch04:178 ↔ FULL:1282 (E17 ↔ E18): identical lines at the
  base (checked by diff).
- The Main, Substratum and Structure sites have no book mirror of the edited wording (corpus grep
  for "non-equilibrium phase", "equilibrium phase", "Equilibrium-Phase", "past hypothesis",
  "perpetual equilibrium", "observer-free", "confinement", "restricts observers" over `papers/*.md`
  and `book/*.md`). Remaining hits outside this unit: Cx:212 (S2-E), M:171 (T10, RETAINED pointer
  "the equilibrium phase"), M:758 and M:760 ("equilibrium macrostate", T2/T3, out of scope).
- Companion restatements owned by S2-E (Cx:212; ch18:40 = FULL:4771): wording supplied in RESULT.

## Builds and checks

`sh ./build.sh Main Substratum Structure` and `sh ./build.sh --book`; no dropped glyphs; page count
and median characters per page compared with the base. `tools/coverage_check.py`; fingerprint
updates in `verification/coverage/LEDGER.json` where a changed source changes one. §A.32/§A.33 scan
of added lines. The cheap §A.40 checks that apply.

## Overlaps

None of the edited lines is in another unit's listed scope (S2-A: SM, ch05, ch06, Sub:98; S2-B: M:60,
M:328–336, :459, :473, :732, :742, Sub:92, :253–268, ch02, appB, Str:53; S2-C: M:131–224, :280, :766,
:732 (iv), SM). S2-B's scope names ch02 as a file; this unit edits only ch02:192 (an X-63 site in the
ledger's sitemap) and its FULL mirror. Main.md, Substratum.md and FULL.md are edited by other units
on other lines; text conflicts, if any, are resolved at landing by merits.
