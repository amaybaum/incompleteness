# Response to the focused review of RO1-DEPS-r3

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-DEPS-r3.md` (ACCEPT WITH CHANGES at
`4fc3f4aa`). The changes are in `RO1-DEPS-r4.md`. `RO1-DEPS-r3.md` is left unchanged (SHA-256
`aee284f2d9f51df8a698aff0f08c64f5db922f9495f39fdb31c4bcc76d65451d`).

Each finding was checked at source before it was applied. No finding was found to be wrong.

Unchanged: the verdict UNDETERMINED (C2 does not change it; see below); no new premise, no
computation, no manuscript edit; and the separations between defined and executable, conditional and
established, and first missing step and ultimate goal.

## Required changes

| Finding | Check at source | Disposition | Where in r4 |
|---|---|---|---|
| **C1.** The interface ceilings and D-A8 exclude quantum operations only, not PR | **Confirmed.** The PR gate `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-EXCL-1 l. 33) is a bijection of configurations. Its conjugation is a permutation, which is monomial and preserves nonnegative entries, so it passes D-iv's obstruction (diagonal preservation, `StructuralClosure.lean`:344–345) and D-nonneg's (`NonnegBounded`). D-A8 bounds entanglement from definite configurations (GR:823). RO1-SPEC-r3 §7.4: on one carrier a PR table is "an ordinary classical channel" | **Applied.** §5.1 now has four classes: *excludes both* (only D-ceil, under global P-vii and P-xiv, separated wings on F); *excludes quantum only* (D-iv, D-nonneg, D-A8), with the reason; *excludes neither*; *partial discriminator*. It adds the consequence that this is the worst case, since the restriction soundness needs falls on settings and renewal. Inherited statements are corrected too: the closing paragraph of §5; R7's "Excludes PR?" cell (Interface B: no; affine class: the stated gate is outside it, but no general exclusion is shown); and §6's grouping (R7 moved out of "sound against PR"). X4 is sharpened to match | §§4 (R7), 5, 5.1, 6, 7.7 (X4) |
| **C2.** Track (c) omits what holds under global P-vii | **Confirmed.** Main:20: such a completion "is a local hidden-variable model, so `|S_CHSH| ≤ 2`". The hypotheses (i)–(iv) are at Main:364–376, with the ±1-in-every-run condition. Main:414: wings inside the cone are not covered | **Applied.** Track (c)'s evidence status is indexed by the P-vii reading. Under the global reading, the separated-wing Bell experiments on F are sound, at the cost of Bell coverage, with the exact hypotheses and the out-of-scope cases (inside the cone, messages, other experiments, I). Under the scoped reading, not shown. The §7.6 row and the header summary match. **First step and verdict:** an added paragraph explains why neither changes. The target needs soundness *with* Bell coverage, so C-1 is still step 1. The global-reading result is partial and coexists with a coverage failure, so it is not SUFFICIENT. It shows no executable supraquantum experiment, so it is not INSUFFICIENT | §7.4; §7.6; header |

## Recommended changes

| Finding | Disposition | Where in r4 |
|---|---|---|
| **X5.** Track (b)'s remote-setting dependence is the PR mechanism | **Applied** as a flagged conflict. Checked: H-Bell (i) (Substratum:133); the adopted branch (:80); D-PR (:360). Effect: tracks (b) and (c) must be settled on one interface. Track (b)'s completion cannot count toward SUFFICIENT without track (c) on the same interface. The verdict does not change. The §7.7 lead and the header count now say five conflicts | §7.7; header |
| **X3 clause** (nonblocking note) | **Applied.** X3 now states that the same holds for the phases (P-phase), since a complex diagonal is not a bijection of configurations | §7.7 |
| **m1.** The carrier is first on (a) and last on (b) | **Applied.** One sentence in track (a) step 1 gives the reason: on F₂ track (a) is already refuted, while C-1 can be settled on F and then transferred | §7.2 |
| **m2.** Track (d)'s step 3 depends on the reading of P-vii | **Applied.** Step 2 now fixes both the reading of "one model" (S6) and the reading of P-vii (OB-b0, OB-b1) | §7.5 |
| **m3.** Stale labels | **Applied.** "Scope of r2" → "Scope"; "Not inventoried in r2" → "Not inventoried" | Header; §10 |
| **m4.** "Under `Θ`" stated as if adopted | **Applied.** It now reads "Under `Θ`, if adopted (S8)" | §5.1 |

## Verdict

**UNDETERMINED**, unchanged, for the reason given under C2.
