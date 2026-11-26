# Uniform norm control: change map r1 → r2

r1 is `REPORT.md` (commit `1a6252f41ce71a029239a82f9bea667d056f8335`) and r2 is `REPORT-r2.md`.
`REPORT.md` and `PLAN.md` are unchanged. The findings are those of the independent review of r1,
posted verbatim on PR #1614 (verdict ACCEPT WITH NITS, no mathematical error found). No result's
proof changes, and no new premise is introduced.

| Finding | Where in r2 | Change |
| --- | --- | --- |
| 1 | §0 table (Theorem U), §0 outcome U2, §3 (U-a) and Theorem 8 under (U-a) | (U-a) gives Lemma 7's map bounds for the pair (c̃, c′). The bound for the original c is not claimed, and c̃ is not claimed to have soundness term ≤ ε. Theorem 8 uses only the map bounds. The unused hypothesis φ < 1 is dropped |
| 2 | §3 "Norm control: necessary; sufficiency open at small η"; §8 Prop X2 bullet | "Not sufficient" is restricted to the case without the structure rules at small η (X2 needs η ≥ 2). In class(η) at small η it is open (UN-1) |
| 3 | §0 outcome CC-L; §3 "τ_min ≤ φ"; §5 necessary conditions | The direct bound τ_min ≤ φ(c′) (Φ is available and id is a channel) replaces the weaker bound through κ_snd; the necessary condition becomes φ(c′) ≥ τ_min |
| 4 | §0 table (Corollary G1); Corollary G1 | g < ∞ whenever ε < 1/16. The uniformity is stated over a class of theories with chosen c′, each direction separately. The consequence for unit 3's O2-a (the g = ∞ branch does not occur) is listed for routing only; unit 3 is not edited |
| 5 | §0 table (Prop S); §4; §6 | The prose equivalence is replaced by "Φ^{-1} lies within δ_S of Q_I" and two one-directional Neumann bounds, each with its condition (δ_S‖Q_I^{-1}‖ < 1; δ_S‖Φ‖ < 1) |
| 6 | §0 outcome U2 and a new void-clause bullet; §3 | φ is named as the single residual, and ‖c′(id)‖ as the part W4 isolates. One paragraph addresses PLAN §3's void clause: Theorem G (gauged) and Corollary G1 (relative) are not voided by CC-L, and no N1 bound is claimed |
| 7 | §0 table (CC-p); §5 CC-p; §8; §9 | Countercontrol CC-p added: T_S with S^{-1} = C_p, checked by hand. Laws are probability vectors, the coverage term is ≥ p/4, and norms are (1 + p(N−2)/N)/(1−p), unbounded as p → 1. It is stated as a countercontrol for Prop X1, not for Theorem G. The C0 comparison is stated as asymptotic (κ_cov = 216ε at ε = 1/48) |
| 8 | §0 outcome U1; W5 | The gauge is "the chosen correspondence's coverage partner of the identity" (not unique) |
| 9 | Label paragraph; §0 table; §5 CC-s; §9; §10 | T_s is labelled as unit 3's item D1, partially verified, [D1]; only its definition and τ_min = s are used |
| 10 (optional) | Header | States that informal exploration, including the idea behind Theorem G, preceded the plan commit and was not written down; the written derivation followed it |
