# Diff-only confirmation: PR #937, 4fe0ebff..f0cc2e94

- **Mode:** read-only, run on `git show` / `git archive` snapshots (`S/cc2/review2/regen3`). No worktree was created and
  nothing was committed. Git ran with `-c gc.auto=0 -c maintenance.auto=false`; Python with `python3 -I`.
- **Ancestry:** `f0cc2e94`'s parent is `4fe0ebff`.

## Verdict: ACCEPT WITH NITS

F1–F7 are applied as specified, and both departures are acceptable. The mirrors, artifacts and checks pass. Two
optional nits are listed at the end.

## F1–F7

| Fix | Status |
|---|---|
| F1 appendix-a:225 | ✓ verbatim: "four consistency or descriptive relations" |
| F2 ch09 Tier 1 | ✓ verbatim: both rows deleted; "Five universality-class entries … are not tabulated."; "Tier 1 has five entries"; "twenty entries" |
| F3 Koide Q figure | ✓ all seven sites (appendix-a:79, :98, :211, :215; ch09:167 (was :169); Structure:56, :940) |
| F4 ch06:196 | ✓ verbatim |
| F5 Substratum B-S clause | ✓ verbatim (SM:865's window) |
| F6 Substratum sin²θ₁₃ | ✓, with an acceptable departure (below) |
| F7 | ch06:205 was fixed here rather than deferred (below). The θ₀ table disagreement remains deferred (CHANGE-NOTE §9). |

## The two departures

**F6.** Dropping "as in Chapter 4" is acceptable. The papers do not cite book chapters, and the count statement stands
without it: "(class C in [SM §7.6]; not counted separately in Class B)".

**ch06:205.** Acceptable, and it improves the text.
- "Q from $C_2(T_1)/d^2$" is now "Q = 1/3 + A²/6 = 2/3 through A² = C₂(T₁) = 2". This is correct per SM:895 and
  consistent with F4.
- "are all derived from cubic-group representation theory" overstated the four relations. "take their forms from …
  with no free parameters" is accurate.

## Recounts and figure sites

**ch09 tier tables, recounted from the tables:**
- Tier 1 = 5;
- Tier 2 = 7;
- Tier 3 = 8;
- total 20.

These match ch09:130, :177 and :179.

**Koide Q.** No site labelled Q still reads 0.02%.

**θ₀ sites are unchanged.**
- SM.md, Juno.md and ch04 are byte-unchanged in this range.
- The ch06 table θ₀ row (ch06:303) and ch06:171 are unchanged.
- The remaining 0.02% hits are all θ₀ sites: SM:14, :1318, :1329, :1572; Juno:401; ch05:196 ("Koide relation 2/9");
  ch08:177, :210 ("Koide angle"); README:62.

## Mechanical checks

- **FULL mirror:** the FULL diff equals the union of the chapter diffs as multisets (11 added, 13 removed).
  `mirror_check`: 0 absent.
- **.tex:** the stamps match their sources for Structure, Substratum and FULL. Regenerated with pandoc 3.1.3 and the
  shared header, all three are byte-identical to the committed files.
- **.pdf:** rebuilt. Pages unchanged: Structure 98, Substratum 52, FULL 555.
- **Repo checks:** `claims_check` OK, `voice_check` OK (40 files), `duplicate_check` OK.
- **Text added in this range:** no history voice, no assert-then-qualify.

## Nits (optional)

1. **ch06:205 [FULL]:** "their classifications are those given above". Above that line, ch06 gives classes only for Q
   and θ₀ (ch06:196). m_d/m_s and m_u/m_d are classified in the §6.8 table, which comes later. Suggested: "their
   classifications are those of the Section 6.8 table — $m_d/m_s$ and $m_u/m_d$ layered, Koide $Q$ and $\theta_0$
   conditional on the dynamical closure of the Koide amplitude."
2. **ch08:68 [FULL]:** "Koide at $0.02\%$" is unlabelled, and the figure is θ₀'s. Suggested: "the Koide angle at
   $0.02\%$", as at ch08:177 and :210.
