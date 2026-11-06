# O-RET Phase B: one O5 geometry screen

**Status: WIP / UNVERIFIED. Paper-only design, not a freeze or a run.**
Accountable Issue: #1032. Owner rulings: [6 November 2026 decision record](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6692541241).
Drafting base: `f49b768709d262a05471895cec703b31aff19b57`.
Writer: `writer-oret`, this coordinating Codex session.
The earlier #1115 draft and Phase A freezes are preserved.

## 1. Question and stopping rule

Can one physically motivated register retain a readable classical carrier record
through the second hold tick, in an O5 case not already decided by Theorem N?

Check the geometry and read access before retention calculations. A dependency
stencil supplies a mathematical neighbourhood; it does not by itself supply a
physical detector or a jointly readable register. If no source establishes that
connection for the one candidate, stop there. Do not replace it or tune a
preparation law to obtain a favourable retention outcome.

## 2. One candidate, fixed before outcome analysis

Use the SMR binary copy-form rule on the eight-site ring in Theorem N §3.1:
`x'_i = y_i`, `y'_i = y_{i-1} XOR (y_{i+1} OR y_{i+2}) XOR x_i`.
Carrier: site 0, both slices, all four preparations
`P = {(0,0),(0,1),(1,0),(1,1)}`; target `c = y_0(t0)`.

The single proposed register has sites `A = {7,1,2}`, locus `R=(x_A,y_A)`.
The proposed read cells are the current slice `y_A`.
This shape is the complete structural current-slice parent set of the carrier's
update, chosen from the rule's incoming coupling stencil rather than a computed
retention outcome. That is a motivation to screen it, not a claim of physical sourcing.
It is a fixed non-arc set meeting `{6,7}`, with width 3.

Keep exactly the preregistered preparation laws `nu_r`,
`r in {-1,0,1,2,infinity}`, of Theorem N §3.2; do not introduce a
slice-level, correlated, restricted-carrier or nonzero-ready preparation.
No member is selected on the basis of a retention result.
The `nu_{-1}=pi0` pad obstruction remains a negative control.

## 3. Window and conditional analysis obligations

Use the existing `T=2` convention: hold ticks `t0+1,t0+2`,
window `W_2={t0+1,t0+2,t0+3}`.
If the physical geometry/access screen passes, derive the write, both hold
ticks and the final endpoint. Check J-i and J-ii at each hold tick, worst-case
decoding error on every preparation at every window tick, and the applicable
storage/invariance requirement. A second-hold-tick read alone is insufficient.

Theorem N §7 identifies O5 as unresolved under the named hypotheses.
Being outside the original family is not itself a positive retention result.
The exact escape checks and the source audit are pending in this checkpoint.

## 4. Counting and separate coherence obligation

The owner provisionally adopted the corrected criterion in historical
DESIGN-PHASE-B.md §5.6 for this classical design only. Its precise content and
support must be retained with this design before any enduring claim uses it.
Ambiguous D1 and D2 cases remain undecided, including inputs available to the
decoder only through the write tick. No pass or counted result is asserted.

Independent review must ask whether any proposed counted pass could genuinely
have failed with the declared construction data fixed. Reproducing a decoder's
construction is insufficient.

Cross-read ancilla coherence is a separate open #1032 obligation, blocked on a
sourced coherent carrier and a read capable of preserving it. #1143 owns its
distinguishing test; the assessed two-read match alone does not identify the
mechanism. This classical paper does not supply coherence.

## 5. Next gate and separate coupling work

Complete the source screen, stop if the geometry/read access is unsourced, and
send the exact pushed paper head for independent review before a freeze or run.
#866 keeps B3's outcome-conditioned physical exchange and public access.
A classical retention ingredient would not discharge that handoff or authorize
another #1169 candidate assessment.

No scientific computation, simulation, enumeration, Lean build, replay, workflow
dispatch, new physical premise adoption, implementation, freeze, merge or
scientific promotion is authorized by this paper. Ordinary automatic PR CI is
verification only.
