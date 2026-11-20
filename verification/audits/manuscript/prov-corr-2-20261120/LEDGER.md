# PROV-CORR-2 — two-site provenance cleanup ledger

**Status.** Writer's correction ledger for manuscript correction unit PROV-CORR-2. Independent
exact-head review of `c2c3dbcc`: REVISE (small), answered in "Round 1 revision" below; review of the
revised head pending, and merge is a separate owner decision. Paper corrections only: no physical
premise is added, no conditional mechanism is promoted or dropped, `Main.md` is unchanged, and no
§A.23 correctness band moves (bands unchanged: this is consistency work).

**Authorization.** Owner `amaybaum`,
[#1169 comment 7044998279](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7044998279),
2026-11-20T16:37:21Z: "PROV-CORR-2, a two-site provenance cleanup, with standard propagation
(§A.25) and review gates: the A/4 coefficient described as 'a Level G2/G3 × Level D derivation'
(ch03:120, Str:184, and mirrors); Structure's empirical-status sentence 'all consistent with current
data' (Str:924, #1448), set against GR §7.4's tension rows. It must not grow into another broad
provenance audit. It closes #1448 on landing." Goal link (§A.47), as recorded there: a consistency
correction; not a new result.

**Base.** `main` at `800cfec6655aa5e9efaf39d6c7823bf2f40795e2` (includes PROV-CORR, #1458). Site
notation as the PROV-CORR ledger (`GR:n` is line `n` of `papers/GR.md`; `Str`, `chNN`, `FULL`
likewise); every line number is a base line number, and no edit changes a line count. Before/after
blocks quote the base and the final text.

## Coverage

| Hunk | Site | Item | Anchor | Correction |
|---|---|---|---|---|
| A.1 | ch03:120 | (A) | GR:318 ("recovered, under the conditions of the §3 calibration"; the 1/4 "fixed at 1/4 by the Hawking temperature and the first law"); GR:320; GR:689 (the count's agreement with the 1/4 "is equivalent to that calibration"); ch07:106 ("a consistency relation of the horizon calibration", "conditional at the universality-class level"); GR §8.5 Theorem, GR:672–679 (S1–S4; A2–A5 not used); ch09:48, :224; Str:180, :882 | "sits at Level G2/G3 × Level D — a conditional derivation" → the count's agreement with the factor is not class-specific: a consistency relation of the calibration (H-slope, H-count, horizon conditions) at the universality-class level, the factor fixed by the Hawking temperature and the first law; test status kept |
| A.2 | FULL:981 | (A) | mirror of A.1 | identical text |
| A.3 | Str:184 | (A) | as A.1; scope and conditions as Str:180 (S1–S4 of [GR §8.5]; H-slope and [GR §8.5(b)]) | "a Level G2/G3 × Level D derivation" → the count's agreement as a consistency relation of the calibration holding for every substratum satisfying S1–S4 of [GR §8.5], conditional on H-slope and [GR §8.5(b)], the coefficient fixed by the Hawking temperature and the first law [GR §5]; test status kept. The same line's sentence start ". the JUNO" is capitalized |
| A.4 | ch09:224 | (A), propagation | as A.1 | "The two derivations are *independent*" → "The framework's consistency relation and the string-theory count are *independent*" |
| A.5 | FULL:2639 | (A) | mirror of A.4 | identical text |
| B.1 | Str:924 | (B), #1448 | GR §7.4 table, GR:548 and :549 ("in tension"), GR:547 ("normalization comparison open"), GR:546 ("factor imported"); GR:514; GR abstract GR:12 | "all consistent with current data" → the table's measured comparisons at the levels it states; GR §7.4's two tension rows and the open Tully-Fisher normalization named, with the conditional radial law built on $a_0 = cH/6$ and its imported factor |

The audit classes behind (A) are those of `verification/audits/foundations/r1-l8-stage1i-20261120/AUDIT.md`
row R7: the coefficient ambient (X (a)), the count's equality with it calibrated (X (m)) and flagged
as equivalent to the calibration (Z). The PROV-CORR ledger lists these sites as follow-up candidates
(round-1 note N8; owner record #1169 comment 7044915211). The equivalence named at GR:689 is exact
algebra in both directions for $A \neq 0$: $\sigma A/\epsilon^2 = A/(4l_p^2) \iff \epsilon^2 = 4\sigma l_p^2$.
The new wording does not display it; it uses ch07:106's one-directional phrase.

## Before / after

**A.1** — `book/ch03-structural-realism.md:120` (A.2: `book/The-Incompleteness-of-Observation-FULL.md:981`, identical)

Before:

```text
The Bekenstein-Hawking $1/4$ factor sits at Level G2/G3 × Level D — a conditional derivation (H-count and horizon conditions, Chapter 7) with no direct empirical test (GW250114 constrains the classical area theorem, not the coefficient) — since both OI's substratum and any successful SM-reproducing framework that yields the area law would predict the same factor.
```

After:

```text
The boundary count's agreement with the Bekenstein-Hawking $1/4$ factor is not class-specific: it is a consistency relation of the horizon calibration (H-slope, H-count and the horizon conditions, Chapter 7) that holds at the universality-class level (Chapter 9), with the factor itself fixed by the Hawking temperature and the first law, and with no direct empirical test (GW250114 constrains the classical area theorem, not the coefficient); any framework that yields the area law under the same thermal calibration gives the same factor.
```

**A.3** — `papers/Structure.md:184` (final sentence)

Before:

```text
the JUNO match to $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$ is a Level G3 × Level D result (retrodictive); the $A/4$ coefficient is a Level G2/G3 × Level D derivation with no direct empirical test (GW250114 constrains the classical area theorem, not the coefficient).
```

After:

```text
The JUNO match to $\sin^2\theta_{12} = 1/3 - 1/(4\pi^2)$ is a Level G3 × Level D result (retrodictive); the boundary count's agreement with the $A/4$ coefficient is a consistency relation of the horizon calibration that holds for every substratum satisfying S1–S4 of [GR §8.5], conditional on H-slope and the further conditions of [GR §8.5(b)], with the coefficient itself fixed by the Hawking temperature and the first law [GR §5], and has no direct empirical test (GW250114 constrains the classical area theorem, not the coefficient).
```

**A.4** — `book/ch09-universality.md:224` (A.5: `book/The-Incompleteness-of-Observation-FULL.md:2639`, identical)

Before:

```text
The two derivations are *independent*, with neither producing the other;
```

After:

```text
The framework's consistency relation and the string-theory count are *independent*, with neither producing the other;
```

**B.1** — `papers/Structure.md:924` (after the paragraph's first sentence, which is unchanged)

Before:

```text
The framework's predictions are all consistent with current data; the awaiting tests (Majorana confirmation at LEGEND-1000, JUNO measurement, DESI Year 5 $\nu$ tightening, Hyper-Kamiokande proton-decay bounds) will test them further.
```

After:

```text
The measured comparisons in the table agree with current data at the levels stated there. The gravitational summary of [GR §7.4] lists the Milky Way rotation curve beyond the crossover (Jiao et al. 2023) and the high-redshift rotation curves (Genzel et al.) as in tension with the conditional radial law built on $a_0 = cH/6$, whose factor $1/6$ is imported [GR §7.3], and leaves the baryonic Tully-Fisher normalization comparison open. The awaiting tests (Majorana confirmation at LEGEND-1000, JUNO measurement, DESI Year 5 $\nu$ tightening, Hyper-Kamiokande proton-decay bounds) will test the predictions further.
```

#1448's second target, the Level 3 MOND row (Str:903 at that Issue's base), was removed by PROV-CORR
(its row F-3.2). With B.1, both of #1448's targets are at the status GR §7.4 gives them. The BTFR-z
result of #1429 is not used.

## Round 1 revision (review of `c2c3dbcc`, REVISE small)

Review record: PR #1459, comment of 2026-11-20T17:02:47Z. Item (B) accepted.

| Item | Answer |
|---|---|
| 1 (must): the "Level G2/G3 × Level D" placement is part of the overclaim; the corpus places the 1/4 at the universality-class level | A.1, A.2, A.3 restated at that level, with H-slope among the conditions |
| 2 (must, §A.25): ch09:224, FULL:2639 "The two derivations" | A.4, A.5 |
| 3: GR:516 BTFR non-evolution tension absent from GR §7.4, the abstract and ch07 | Routed to #1462 |
| 4: m_H "m_t-consistent" label (SM:1118 vs :1294) | Routed to #1462 |
| 5: Str:451, GR:32, Str:463 | Routed to #1462 |
| 6 (nit): Str:184 lowercase sentence start | Fixed in A.3 |
| 7 (nit): "conditional radial law built on $a_0 = cH/6$" | Adopted in B.1 |

### Routed (not changed here)

| Site | Finding | Issue |
|---|---|---|
| GR:516 vs GR §7.4, GR abstract, ch07:278, :300 | BTFR non-evolution recorded "in tension" in GR §7.3 but not in the summaries | #1462 |
| Str:451 | the coefficient "transports to OI from the partial-trace structure" | #1462 |
| GR:32 | "§5 derives the Bekenstein-Hawking entropy" | #1462 |
| Str:463 | garbled sentence | #1462 |
| SM:1118, :1294 | m_H inherits the "m_t-consistent" label | #1462 |

## Checked and unchanged

- **Str:439, :497** ("produces" the A/4 law). Each states the recovery conditionally (H-slope
  and [GR §8.5(b)]). Str:451 and :463 are routed above.
- **ch07:147** ("the two derivations" of the Page time) and **ch07:313** (the 1/4 relation
  "follow[s] under H-count and the named horizon conditions"): not a derivation claim for the 1/4.
- **Str:996** (the A/4 coefficient "more universal"; string theory "derives" it): a transport
  statement, not an OI derivation claim.
- **SM:1318** ("all consistent with data"): a list of SM-sector structural items, not a
  framework-wide empirical-status statement.
- The book already names both rotation-curve tensions (ch07:300, :301 "in tension"; ch07:278–280; ch18:160) and states the
  Tully-Fisher normalization comparison as open (ch07:299, ch09:149).

## Re-grep (papers/*.md, book/*.md)

| Phrase | Count |
|---|---|
| `Level G2/G3 × Level D derivation` | 0 |
| `conditional derivation (H-count` | 0 |
| `all consistent with current data` | 0 |
| `G2/G3` | 0 |
| `The two derivations` | 0 |
| `consistency relation of the horizon calibration` | 10, in Structure, Substratum, ch03, ch07, ch09, appendix C and their FULL mirrors |

## Build and checks

At the revised head: rebuilt `papers/Structure.{tex,pdf}` (94 pages) and the book `FULL.{tex,pdf}` (489 pages), both as
at the base, with no dropped glyphs. GR is not touched. The SC-42 integration result and controls
reproduce byte-identically (normal and `-O`), so no regeneration. Local checks pass: staleness,
voice, claims, duplicate, mirror, Lean-manuscript census and artifact placement. The
legacy-records self-test passes; its commit check is undecidable in the shallow local clone and runs
in CI.
§A.32/§A.33 added-line scan: no meta-commentary, reader-instruction or history phrase; the only
capitalized tokens are the acronyms DESI, JUNO and LEGEND, already present in the unchanged
parenthetical.
