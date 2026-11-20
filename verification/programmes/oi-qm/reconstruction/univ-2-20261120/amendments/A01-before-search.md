# UNIV-2 amendment A01 (before any search)

Committed after `PREREG.md` (`69bdc440`) and before any gadget search or invariant computation on
Q. The only computation run between the two commits is control K0's straight-line run of the W2
window (one 1D orbit, 12 ticks), which is the control's own content. Its result: the W2 signal is a
localized defect. After the signal passes, the line is back in the *same* background phase,
`N(t)`, not `−N(t)`. Within 12 ticks the configuration differs from the background on at most three
sites around the defect. U1 E2's relation `y(t+3) = −shift y(t)` holds for the background as well,
so it does not imply a phase change behind the signal.

1. **Post-transit reference (§2).** The defining clause is unchanged: "the state a straight line of
   the same type leaves behind its signal." For W2 the reference is `N(t)`, by K0. The parenthesis
   "for W2 this is `−N(t)`" in PREREG is wrong and is replaced. R5's reference after two transits is
   `N(T₂)`.
2. **R2 made explicit.** At `T₁` the difference `S(T₁) − N(T₁)` is supported in far B, within a
   window of at most 12 sites. Transplanted onto a straight line with the same background, the B
   line state is a glider moving away from the junction. The test, in the line rule of U1 Lemma 2.2:
   values in `{−1,0,1}`, and `state(t+p) = shift_s state(t)` for some `1 ≤ p ≤ 48` and some `s`
   with the outgoing sign. Any such glider counts as a signal, W2 or another type; the record
   reports which. R4's 3D continuation test is unchanged. R5 applies the same transplanted test to
   the two-signal state, with one common `(p, s)`.
3. **Line lengths.** A = `{(x,0,0) : −40 ≤ x ≤ 0}`, which leaves room for R5's second signal 12
   sites behind the first. B runs to `y = 80`, so that no signal reaches B's far end before
   `T₁ + 60`. Far B is the set of B sites at distance `≥ 8` from the junction and `≥ 8` from B's
   far end. In N3 the signal is launched 8 sites from the junction and moves away; with A to
   `x = −40` it does not reach A's far end before `T₁`.
4. **P2 outcome.** In the U1 collision turn the supplied constant particle moves without input, so
   the classifier's first failing requirement is R1. The required outcome is still "classified
   fail". The record names the first failing requirement.
5. **Prefilter and classifier.** The batched search applies R1, the radiation part of R3, and
   R2–R3 at `T₁` as a prefilter. Every survivor then goes through the canonical classifier, the
   single function of §5. Checkpoint for the prefilter being equivalent to the classifier on these
   requirements: on 100 randomly drawn candidates per family (seeded), the two verdicts must agree.
   A disagreement voids that family's search.

No other part of PREREG changes.
