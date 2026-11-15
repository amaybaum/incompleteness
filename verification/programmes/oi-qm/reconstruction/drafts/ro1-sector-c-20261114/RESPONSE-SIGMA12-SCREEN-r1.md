# Response to the review of SIGMA12-SCREEN r1

Review: `REVIEW-SIGMA12-SCREEN-r1.md`, blob `4280293a`, at `c0e3dcf5`, ACCEPT WITH CHANGES. Object:
r1, blob `c32d54c8`, left unchanged. Revision: `SIGMA12-SCREEN-r2.md`. Paper-only; the hand checks are
as stated in r2. The verdict ("partly done; no negative on recording for route M") is unchanged, and
nothing new counts under SNR-1.

| Finding | Disposition | Where in r2 |
|---|---|---|
| R1, G-2 not general | Accepted. G-2 now states the coupling condition (CC) it needs, checked for Y and G-ring only. The review's countercontrol is included: `F` vanishing on `X`, with `X^c` a separate component, makes `φ` a block swap and a time shift. G-1 is split into (a) for every rule (2.1), (b) for `F ≢ 0`, and (d) for every bijection. G-6's extra hypotheses are named: `H` bijective; the unit, non-selector left read. SG-1, §3's closing paragraph, AW-σ1 and blocker 2 are narrowed to match | §2 G-1, G-2, G-6; §3; §5 item 2; §6 |
| R2, Y on a side-2 torus | Accepted, and hand-checked. With every side 2 under the six-offset reading, `F ≡ H(0) = 0` and `φ = σ`. The scope is now "some side `≥ 3`" for G-1(b) and "every side `≥ 3`" for G-2, or the set reading of `∼` in either case. With a side 2, neighbours along that axis cancel, so (CC) can fail even when other sides are `≥ 3`; hence "every side" for G-2. Native-Y's own side is odd and large | §1 table; G-1; G-2; §3 rows (a), (b) |
| R3, G-6 is a second negative | Accepted. G-6 is listed as a proved negative that does not count under SNR-1, because it rests on an assumed carrier preparation (an assumed apparatus), and as one that concerns transport and return rather than recording. §4 splits the reversal into three rows: the global inverse (not available, by criterion clauses); the J-return form (excluded at G-6's scope, uncounted); weaker forms (unsourced, not disproved) | §2 G-6 "Standing"; §4; §5; SG-5 |
| R4, "would need blank cells" | Accepted. It is now [A-inf] "may need", stated as open: a reversible conditional gate can uncompute without an ancilla, and no source shows a blank is necessary. The Lemma R / G-7 consequence is made conditional ("if one is needed"). Added as AW-σ2 | §4 weaker-forms row; §6 |
| R5, blocker list | Accepted. Added: C-PREP (item 3); R4 amplification beside R3 and R5, and R1 on G-ring beyond C-5's instance (item 4); SUBSTATE-1's scoped results (item 5). SUBSTATE-1 is cited in §1 with MR★'s provenance standing, and §4 refers to it. It is not used as a premise, since MR★ gives it provenance standing and r2 did not re-read SUBSTATE-1 | §1; §4; §5 items 3–5 |
| Coordinator, member L | Accepted. SM:811 states a candidate map from matter data to links. No update rule in which the links act back on the matter is stated, and that rule is what blocker 1 names as missing | §1 table; §5 item 1 |
| O1, rule names | Accepted, at SG-3, SG-4, SG-5, AW-σ1 and §5 | §5; §6 |
| O2, C-3 wording | Accepted. "Records" is S-L5's structural hypothesis, and G-4 masks it at `t = 1`. Y: `Σ = {v, w}`, `D = v ⊂ Σ`; `w₂` depends on `y_v` while its effect on `D` depends on `y_w`. G-ring: effect `(m − c)[m ≠ 0]`; the qualifier "for `c ≠ 0`" is dropped (rechecked at `c = 0`: `R(i+1) = i+3` reads `0`) | §2 C-3 |
| O3 | Applied with the coordinator's point (member L above) | §5 item 1 |
| O4 | Accepted: G-5 is the partition-independence clause | §2 G-5; §3 |
| O5 | Accepted: "an additive observer" | §1; §4 |
| O6 | Accepted: C-5's carriers are point-prepared, [assumed] (C-PREP) | §3; §4 |
| O7 | Accepted: "at VER's narrower scope", with VER §1.5's note on MR★'s wording | §4 |
| O8 | Accepted: "within the SM class" | §5 item 2 |
| N1 | Fixed: CURRENT-HANDOFF.md is in the native-Y programme directory, not `shared_v12/` | Inputs |
| N2 | Fixed: CALC is cited as r2 (blob `bef634e2`), reviewed ACCEPT (`REVIEW-U4-CALC-r2.md`, blob `70eddf2d`), and r1 is recorded as ACCEPT WITH CHANGES. The statements compared are unchanged. Theorem 2(c)'s new S-L2 [NP] is not used. "Label dependence" is updated | Inputs; §3 |

Text rules: no banned word or machine-local path in r2 or in this note. The MR★ σ12 quotation keeps its
marked paraphrase.
