# Introduction r25: the run-3 comprehension evaluation, on base `72e41201`

r25 applies `review/accessibility/RUN3-EVALUATION.md` (gate 2, NOT MET): two required explanation changes, D and E,
and the recommended R2 and R3.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical.
- Every census fingerprint is unchanged. Only the ledger `line` fields were rewritten, and they have the same values as at r24 (65, 101, 116, 136, 142, 214).
- No ID was retired, and main was not merged.

Line numbers are the same at r24 and r25 for each paragraph changed.

## 1. Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| D | Required: one fixed rule, never-occurring starts | L130 | Inserted after "…not one rule started in two ways.": "So the comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain; letting the hidden odds change with the start would compare different rules. A start that never occurs stays in the comparison for the same reason. A different deck and shuffle could, for instance, make a red start always show red after the first shuffle while a black start may show either colour, with the face-down odds still the same for both starts: a dealer who always deals red then never sees uncertainty, yet under that rule the forecasts from the two starts overlap, and they overlap only because of the start that is never dealt [Main §2.3]. In that rule the forecasts from the start return to certainty at step 2, before the whole world returns at step 3, so the chain breaks there although no dealt game ever looks uncertain." The added wording "A different deck and shuffle" marks it as a different rule from the two-card swap game. "With the face-down odds still the same for both starts" keeps the shared hidden prior explicit. The optional return-horizon clause is included. It is offered as an instance ("for instance"), not as a proof |
| E | Required: two cases of late memory | L146 | Inserted before "For example,": "Two cases differ. If the memory first affects a later step that some accessible window still reaches, an observer who watches that long detects it, as in the example below. If it first affects what is seen only beyond every accessible window, no observer detects it; the failure of chaining across the cycle is then a structural consequence of finite reversibility and partial access, not something any accessible window records, and what an observer can test is memory at an accessible order, which (C4) asserts." The evaluator's "should be kept apart" is replaced by "differ", because §A.32 excludes reader instruction. The example's end now reads: "Here the window ends at time 2: an observer whose window reaches time 3 detects the memory, while one whose windows all end at time 2 never does. The example shows memory beyond the window; it shows no failure of chaining inside it." "Which (C4) asserts" matches the paper's (C4) at L122, "a memory witness at some accessible order", which "in a faithful realization … coincides with M_t>0". The same clause already appears at L152 |
| R2 | Recommended: the Bell either/or | L300 | The labelled paragraph "Conditional physical interpretations" was changed only in its Bell clause. **Old:** "With measurement independence retained, quantum Bell correlations then require ontic parameter dependence, subject to H-Bell (§3.5);". **New:** "Given determinism and an outcome in every run, Bell's theorem leaves two options, giving up ontic parameter independence or measurement independence; with measurement independence retained, quantum Bell correlations then require ontic parameter dependence, whose realization on the substratum without usable signalling and with the gravitational continuum limit is the open hypothesis H-Bell (§3.5);". The scope is that of §3.5 (L242–L246) and Main §3.3. L246 already states the either/or, so it is unchanged. The Summary (L296) does not summarize Bell, so it is unchanged |
| R3 | Recommended: a plain gloss of the §3.2 structure | L206 | Inserted before "The five completion conditions are:": "In plain terms, the experimenter can do nothing, combine operations and lump outcomes together, prepare an evenly mixed helper, read the helper without disturbing the system, and discard it." Each item maps to the structure in L206 and GR §3.3: identity; outcome-conditioned composition; coarse-graining; a uniformly mixed ancilla preparation; a spectator-independent readout (acting as the identity on the system for product inputs); ancilla discard. Six items, none added or dropped |

## 2. The change-D rule, checked exactly

The coordinator's realization was re-run with exact rationals (Python `fractions`):

- **The rule.** Visible states {R, B} and hidden states {0, 1, 2}. φ(R,0)=(R,0), φ(R,1)=(R,1), φ(R,2)=(B,2), φ(B,0)=(R,2), φ(B,1)=(B,1), φ(B,2)=(B,0).
- **The prior.** μ_H is uniform on {0, 1} and the same for both starts, so the hidden prior is shared by every root and drawn independently of it.
- **Checks:**
  - φ is a bijection, of order L = 3.
  - Γ₁ = [[1, 0], [½, ½]]. The rows overlap in column R, and the R row alone is a point mass.
  - Γ₂ = Γ₃ = I, so Γ₂ = I is a return horizon before the recurrence time L = 3.
  - From the R start, both hidden states give R at every step, so a dealer who always deals red never sees uncertainty.
- **Consequence.** Theorem 3 with s = 1 and n = 2 gives failure of P-divisibility on {0,1,2}. The failure comes only through the row of the never-dealt black start, the case Main §2.3 names: "possibly only through a row of a root of visible probability zero".

## 3. Terms

The six terms are unchanged in meaning: conditional memory, hidden predictive memory, accessible memory,
P-divisibility, recurrence time and return horizon. The new text uses "return to certainty" for the return horizon, the
"whole world returns" for the recurrence time, and "memory at an accessible order" for accessible memory.

## 4. Not applied

None.

## 5. Build and checks

- **Build:** `sh ./build.sh Introduction` gives 22 pages, one more than r24 and over the 21-page flag. The extra page holds about ten lines of the reference list. The main text ends on p. 19. Median 3,156 non-space characters per page.
- **Typesetting:** a direct compile shows 0 overfull, 0 underfull and 0 missing characters. Theorem 2 still breaks after (b), as accepted at r23.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake` and cannot run locally; it passes in CI.
- **Other checks:** `duplicate`, `voice`, `claims`, `coverage` (134), `staleness` and `mirror` all pass. `edge_rigidity_probe`: ALL CHECKS PASS.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families ("should be kept" included), caps emphasis, markers, secrets, scratch paths or model identifiers.
