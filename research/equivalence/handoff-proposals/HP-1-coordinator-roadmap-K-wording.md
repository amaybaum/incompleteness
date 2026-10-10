# HP-1 — to the coordinator: proposed ROADMAP wording for row K (not applied; research only)

From `research/equivalence` (base L = `9f9f8257`). Nothing below is a governed result. Under the promotion rule recorded
in `research/archive/k-infinity/K-INF-DESIGN.md` §17 (an option enters the ROADMAP only when a governed result supports
it, a governed countermodel rules it out, or it materially changes the formal statement of an open obligation), none of
these sentences should land before the corresponding governed round (NOTES-E7 skeletons S1–S4) has landed. They are
offered so that the rounds can be scoped against the exact text they would license.

| ROADMAP site at L | current text (abridged) | proposed text, if the named round lands | evidence now |
| --- | --- | --- | --- |
| :1023–1024 K∞-Seed | "a sharp seed, `SharpSeed`; on the completion it follows from SC∞ and a stage effect with values one and zero at two stage preparations (`sharpSeed_completion`)" | add: "carried to the ball along the chart and the ball's identification (`sharpSeed_eball_of_stage`), so its remaining content is the stage-level sharp test" | [D] run 38083519826 (S1) |
| :1018–1022 K∞-Trans | "K∞-Drive does not give it … and no theorem derives transitivity from `ElementaryDrivability` on a general body" | replace the last clause: "and on a general body the other single-system seams do not give it: a strictly convex, drivable, centrally symmetric body of chart dimension 4 with a sharp seed and supporting-effect completeness admits no boundary-transitive family and no dense boundary orbit" | [W] + [X] `e2_drive_trans` (S4) |
| :1027–1030 K∞-Copy | "An untested candidate weakening … if the planned exact probe confirms it, the obligation becomes type covariance of native inversion" | "Copy naturality may be weakened to type covariance of native inversion — the target copy's NOT is the conjugate of the control copy's NOT by a body automorphism fixing the corner axis, equivalently, for NOTs of the ball, equal ±1 eigenspace dimensions — under which DIM-1's selector applies (`dim_of_nativeGate2_conj`); the two-NOT countermodels at d = 5 and d = 7 violate it" | [D] (S2) + [X] `e2_copy_conj` |
| :1058–1069 Kₙ | "… take the complex matrix carriers of every finite size … No current theorem supplies the lift." | add: "Inside the K3 interfaces the carrier-general quantifier of drivability reduces to qubit-power carriers: an implementation class with `Architecture`, `ContextStable` and `LabelInvariant` that drives the elementary transitions on every `Fin (2^k)` drives them on every finite carrier (`drivesElementary_of_pow`); what remains is drivability on qubit registers from the elementary system and those closure clauses" | [W] + [X] `e3_compress` (S3) |

Two cautions for any wording: (i) the K∞-Copy weakening is not shown to admit any gate that copy naturality excludes
(`e2_copy_conj` C6); (ii) the Kₙ reduction moves the carrier generality into `ContextStable`, which is the matrix form
of the same spectator clause that K2's local-action clause (b) needs — it is not a discharge.
