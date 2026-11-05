# O-RET Phase B: the NRR-1 obstruction (paper record)

**Status: WIP / UNVERIFIED.** A paper-only negative record. Every derivation in it is by hand and is
not independently reviewed. It establishes no result, changes no scientific status and is not a
premise of any claim (AGENTS.md §A.46 items 1, 3 and 7). **No Phase B run is planned.**

## Authorization and scope

- **Owner ruling** ([#1032 comment 6651202161](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6651202161),
  amaybaum, 2026-11-05T06:15:39Z): "Option 1, a paper-only negative analysis. … Phase B is revised to
  document this obstruction, rather than to run a test whose outcome its assumptions already
  determine." "**Not authorized:** Phase B freeze, enumeration, execution, any new physical premise,
  or scientific promotion." The ruling also requires independent review of the derivations and of
  the negative conclusion.
- **Earlier grant** ([#1032 comment 6649418760](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6649418760),
  amaybaum, 2026-11-05T04:08:27Z): Phase B design only.
- **Writer:** `writer-oret`, on branch `research/o-ret-phaseb-design-20261105`, drafted from `main` at
  `f5c281ae10a913ec68fa41b3b839ad0b164979cd` (drafting snapshot `D`). The design draft at `43370576`
  is provenance for the definitions restated in the record.
- **Accountable Issue:** #1032 (O-RET). Dependency index: #914.

**Not done.** No computation, simulation, enumeration, script, probe or Lean build. No workflow
dispatch. Nothing frozen, designated, merged or promoted. No physical premise adopted. No file outside
`phase-b-design/` is changed: Phase A's frozen inputs, `phaseA/` and `phaseA/run-1/` are read only.

## Files

| File | Content |
| --- | --- |
| `README.md` | this note |
| `DESIGN-PHASE-B.md` | the record: starting point; the family `𝔉`; the paper derivations and Theorem N; the counting criterion; the scope of the negative; open families and the missing ingredient; no run planned; review packet; references |

## Headline [all unreviewed]

- **Theorem N** (`DESIGN-PHASE-B.md` §4.10). On the NRR-1 family `𝔉` (K1 and the SM:112 ring rule SMR,
  rings `N ∈ {5, 7, 8}`, the declared registers, product laws `ν_r` and the one-sided site-level
  laws, all four carrier preparations, every fixed decoder, any `T ≥ 1`), no tuple takes a storage
  row of the Phase A classifier. A run of `𝔉` therefore cannot distinguish retained information
  from information passing through.
- **Its parts** (§4): Lemma PAD; Lemma NP; Proposition AE (additive carrier entry: K1, and SMR
  registers right of the carrier, any product law); Proposition LS (SMR registers left of the carrier,
  site-level laws); Observation U; the `N = 5` cases; Lemma SS-2 (a ready one-site register of any
  copy-form centre-free rule loses the record at `t₀+2` under J-1); the slice-level shape, which fails
  at `t₀+2`.
- **Scope** (§6). Only the rules, registers, preparations, decoder class, readiness laws and
  classifier stated there. It is not a universal no-go theorem for OI retention.
- **Counting criterion** (§5). Relative to the free-map comparison class, a D2 pass is a strict
  tautology exactly when the window's inputs all occurred at the first hold tick (the syntactic flag
  `IP`, with caveats). `IP′` is not such a flag. DT-S1q, DT-S2s and the control DT-SX are informative
  passes; DT-S2s with `R = (r)` and every `T = 1` D2 pass are strict tautologies. The criterion acts
  on no tuple of `𝔉`.
- **Open** (§7). Families not decided by §4, and the smallest unresolved ingredient a discriminating
  test would need: a readiness law outside the site-level product class on a width-`≥ 2` register
  with non-additive carrier entry, a paper analysis of its second hold tick, and a reason for the law
  independent of this analysis.
