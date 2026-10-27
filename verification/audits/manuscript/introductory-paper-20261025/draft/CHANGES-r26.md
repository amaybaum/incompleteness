# Introduction r26: the r25 confirmations, on base `d831fb83`

r26 applies `review/editorial/GATE3-papers-366da4bb.md` (gate 3, ACCEPT WITH CHANGES; should-fixes 1–7 and optional 8)
and the two optional findings of `review/scientific/GATE1-papers-366da4bb.md` (gate 1, ACCEPT; O1 and O2), with the
owner's three r26 decisions.

**Unchanged:**
- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical to r25.
- Every census fingerprint is unchanged. Only the ledger `line` fields moved, because the L130 split adds four lines:
  T-1 65, T-2 101, C-unnamed-b596be8a 116, T-3 140 (was 136), C-recurrence-cycle-indivisibility 146 (was 142), T-4 220
  (was 214).
- No ID was retired, and main was not merged.

Line numbers below are r25 → r26.

## 1. Finding → change

| # | Finding | Line | Change |
|---|---|---|---|
| G3-1 | D's first sentence repeats the one before | L130 → L130 | The fixed-rule sentence is merged into the contrast sentence: "The comparison is about one fixed rule, the same hidden preparation tried from every visible start the world could have, not about the starts a sample happens to contain, and it means something only because the face-down card is dealt the same way whichever card is face up: …". "Letting the hidden odds change with the start would compare different rules" is dropped, since the face-down-colour contrast already says it. The example opens "Why keep a start that never occurs? A different deck and shuffle shows." "After the first shuffle" is dropped from the rule's description |
| G3-2 | L130 is one block | L130 → L130–L134 | Split into three paragraphs: the P-divisibility explanation with the fixed-rule comparison; the never-occurring-start example; the one-sentence statement of the result |
| G3-3, O1 | "Overlap" and "rooted family" before definition | L132 | "The rooted family, the table of forecasts from every start, still asks …" (O1's gloss). "It overlaps the red one" becomes "After the first shuffle both forecasts give red a positive chance, an overlap that comes only from the start that is never dealt [Main §2.3]", which says what overlaps and defines the word where it is used |
| G3-4 | The closing "so" names the wrong cause; "return horizon" before its definition | L132 | "A return horizon" is removed; the return is described as "Both forecasts return to certainty at step 2, earlier than the whole world, which returns to its starting configuration only at its recurrence time, step 3." The causal chain is stated, per the owner's decision 2: "The failure of chaining comes from the step-1 overlap together with this step-2 return, not from the step-3 recurrence: no step-by-step forecast can carry the overlapping forecasts of step 1 to the two certainties of step 2, so the forecasts fail to chain over the first two steps, although no dealt game ever looks uncertain." The mechanism is the one Theorem 3 uses with s = 1 and n = 2, checked exactly at r25 (Γ₁ = [[1, 0], [½, ½]], Γ₂ = I, L = 3) |
| G3-5 | The "sees neither" sentence and case 2 duplicate each other | L146 → L150 | "An observer confined to accessible windows therefore sees neither …" is removed, and case 2 carries it. Of the two wordings offered, "neither appears in any accessible record" was chosen, per the owner's decision 1. Case 2 names both objects and keeps the hypotheses: "If it first affects what is seen only beyond every accessible window, an observer confined to accessible windows sees neither the late conditional memory nor the failure of chaining it implies across the cycle: both remain established in the dynamics under the theorem's hypotheses, but neither appears in any accessible record." The (C4) clause is dropped from case 2, because the paragraph's subject is what a window can see; (C4) stays at L122 and L156. The example stays a separate paragraph, with its end unchanged |
| G3-6 | Redundant clause after D | L136 → L138 | Removed "; a preparation that depended on the start would give rows for different setups, as in the card comparison above". The sentence ends "… computed from the same preparation." |
| G3-7, O2 | R3's label and its first item | L206 → L212 | "In plain terms," becomes "That is,", so no label remains. "Do nothing" becomes "always leave the system alone". O2 is included: "prepare an evenly mixed helper and act after preparing it". The full gloss is "That is, the experimenter can always leave the system alone, combine operations, lump outcomes together, prepare an evenly mixed helper and act after preparing it, read the helper without disturbing the system, and discard it." Each item still maps to one element of the §3.2 structure (GR §3.3) |
| G3-8 (optional) | R2 could lose one clause | L300 → L306 | "Bell's theorem leaves two options," is removed: "Given determinism and an outcome in every run, quantum Bell correlations require giving up ontic parameter independence or measurement independence; with measurement independence retained, they require ontic parameter dependence, whose realization … is the open hypothesis H-Bell (§3.5);". The hypotheses and the H-Bell scope are unchanged |

## 2. The owner's decision 3: definitions at or before first use

- **Overlap:** first used at L132, where the sentence says what overlaps; the formal definition is at L138.
- **Rooted family:** first used at L132, with the gloss "the table of forecasts from every start"; formal at L136.
- **Return horizon:** first used at its definition, L144 ("A *return horizon* is a time n with Γ_n = I …"). L130–L134
  do not use the term.

## 3. Terms

The six terms keep their meaning: conditional memory, hidden predictive memory, accessible memory, P-divisibility,
recurrence time and return horizon.

## 4. Not applied

- **G3-9 (optional, L150 → L154, "Precisely: …").** Not applied. The owner requires the Corollary's scope to be stated
  explicitly wherever the result is restated, and the shortened form would point to the Corollary instead of stating
  it.

## 5. Build and checks

- **Build:** `sh ./build.sh Introduction` gives 22 pages, the same as r25; the owner accepted 22 pages. Median about
  3,236 non-space characters per page.
- **Typesetting:** 0 overfull, 0 underfull and 0 missing characters. Theorem 2 still breaks after (b), as accepted at
  r23.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake` and cannot run locally; it passes in CI.
- **Other checks:** `duplicate`, `voice`, `claims`, `coverage` (134), `staleness` and `mirror` pass.
  `edge_rigidity_probe`: ALL CHECKS PASS.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families, caps emphasis, history voice, markers, secrets,
  scratch paths or model identifiers.
