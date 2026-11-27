# P2-MIN changes r1 → r2

Review: #1629 comment 7213507725 (REVISE). r1, `PLAN.md` and Amendment 1 are unchanged. The outcome
changes from **B** to **C overall, with B under the current-slice access** (x5-TS, finding 2).

| Finding | Change |
|---|---|
| 1 (x4 circular) | r1's derivation of R-READ withdrawn. x4 rerun through steps 3–5: Q0 fails (no mechanism or selector), so NC and SET/M are ASSUMES. Named step: a sourced READ (#1501) |
| 2 (time reversal) | x5 split into x5-gen and x5-TS. Fix(T) verified as a translation-invariant Lagrangian that F does not preserve. Q0 (S) weighed both ways: UNDECIDED. Lemma U added (the current slice is uniform at every time for every reversal class), confirming the reviewer's readability check and extending it to all t. Cells: BLOCKED under current-slice access; SET/M and O-RET OPEN under two-slice access. Outcome stated as C overall. AW-P2-1 added |
| 3 (controls) | Q0 run on K6: ASSUMES. K6 narrowed to the clause and tuning branches, its preregistered defect disclosed, and K6′ added (Haar → F-invariant law: RESOLVES with Q0 active). K7 relabelled CONDITIONAL, with LIFT, linearity, abs(αμ) ≤ 1/d, H-ZM and taming carried; H-PF open. Strength-of-controls note added |
| 4 (LIFT) | Restated as the open dependency of CS only, under lane 2's conditions with H-PF open. C-ENV Theorem 1 narrowed to Haar subgroup laws |
| 5 (x6 (G)) | Lemma N argument replaced by phase averaging of second moments (P-here; the limit is thermal for white noise); DKS cited as context only; "conserves every quadratic density's mean" corrected |
| 6 (Lemma P / AS scope) | AS restated as a full-space statement; NC cells now rest on nonnegativity plus W3/W1/W6, which also covers x7; the C-NL remark marked P-here and outside the covered class; KIN clarified |
| 7 (Bartlett) | Replaced by Mari–Eisert (Wigner-positive simulability) and the classical-sampler argument |
| 8 (Amendment 1) | Owner steer cited (#1169 c.7213508490, quoted). Commit-order limitation stated; additions marked post-hoc in evidential weight; SET cells under the original SET reported (BLOCKED) |
| 9 (status; landing) | Input-status column (§1, §6); landing after #1627 (done); the Gross claim re-sourced to MECH-1 W1/W3/W6; Bartlett replaced |
| 10 (scope of §4) | §4 kept to the covered class; the excluded remark labelled; Lemma A's setting-independence hypothesis (AP1 C1) named |
| 11 (OBS) | "only route C-NL" withdrawn; G4 narrowed to its scope; N/A justified by the absence of a criterion |
| 12 (K3) | Reading stated: no readable write at t₀ means D-RET cannot be met |
| 13 (x7) | Q0 reason given directly |
| 14 (orientation) | Lane 2's taming and coordinate convention stated |
| 15 (count) | Controls listed explicitly (K1–K7, K6′) |
| 16 (q = 2) | x4 and x6 added to the q = 2 paragraph |
| 17 (x6 CS) | Reason changed to the Q0 failure |
| 18 (S-L7) | Added to the inputs and the tracing |
| 19 (Lemma A transfers) | The ℤ^d transfer (P1-11, P-here) and the further real-lift transfer for x6 noted as unwritten |
| C-ENV landed | Reclassified as support on `main` (#1627, merge `69d4d1c2`; the REPORT text is identical) |
