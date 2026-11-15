# Response to the review of GAMMA-1 unit G1, r1

**Object.** `REVIEW-GAMMA-G1-r1.md` (blob `17431953280e20618d484f48fe87b65dd8ba48ea`, at PR #1294
commit `20cdb9e5d`), verdict REVISE. The revision is `GAMMA-G1-r2.md` (cited r2 §N); r1 is unchanged.
One disposition per finding: **applied**, **partly** or **not**, with the reason. Paper-only; no
computation, Lean, manuscript or Issue change.

## Required

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| 1 | Per-phenomenon credit-set clause makes (γ←) unsatisfiable, QM included | **applied** | The clause is removed from (γ←) (r2 §6). Owner Q6 is stated as a condition on the coverage result as a whole: it counts toward AC-1 only if its credit set is nonempty (r2 §6, §7.2). Satisfiability countercontrol NC-γ6 added with a checkpoint and its hand evaluation at G1 (r2 §7.4): no clause fails for the OCP benchmark by construction; whether QM meets the global condition on the declared list turns on X-2 and X-3 (G1-F8). §7.2 now admits an observable only when every member of a declared ceiling set `𝒦(o)` is **established** to disagree through the same `κ`; an unknown result blocks entry. The ceiling is C0 and PC-wave always, and CC4 and CC5 where VER2's scopes give them a law; a member that agrees removes the observable, C0 included |
| 2 | `K_P` is not Schwindt's `K`; it can be 0 for a perfect marker | **applied** | `K_P` is the sum over `m` of the absolute difference `c_L(m) − c_R(m)`, divided by `Σ_{π,m} c_π(m)`, with `c_π(m)` the detected mass (screen detection and `m ≠ ∅`) per incident particle in the one-path run, the priors from the detected masses at equal incident flux, efficiency entering only as ratios (r2 §2.4). Shown equal to `2L − 1` under Wootters–Zurek betting, and to include predictability. Hand checks shown in r2 §2.4: a perfect marker gives `K_P = 1` for every `d_L, d_R > 0`; the block's position no longer matters (r1 gave `1/2` and `0`); an uninformative marker gives `P`; an inefficient perfect marker gives 1 with `f_∅` reported; NC-copy reaches `K_P = 1`. Full laws are kept; `K_P` is a ratio of masses (NC-γ4). Advisory part: `K_C = P` is stated as necessary, not sufficient, with the trivial partition as the counterexample |
| 3 | Masses undefined under E-read and E-prep | **applied** | Each protocol has a declared incident event `𝔈_a`, distinct events disjoint (r2 §3.2). E-set: `μ(z = a)`. E-prep: the attempt `𝔄_a`, herald outcome `(a, E)` or `(a, ¬E)` as a record component, total mass `μ(𝔄_a)` with the failed mass inside. E-read: one event `𝔈_*` shared by the protocols it encodes, total mass `μ(𝔈_*)` each, the shared runs entered once in `L^full`. `κ_norm`'s denominator per encoding (r2 §5.3). NC-γ4's checkpoint restated per encoding (r2 §7.4). Minor part: `L_a^full` is now defined once on `𝓡^full` with `V_A`'s full configuration, and every `L_a` is its projection `ρ_a` (r2 §3.1). The sum rule and the equal marginals were re-checked by hand per encoding (r2 §3.3) |
| 4 | NC-rep identified with the accessibility reading, contrary to G1 §2.1 | **applied** | Identification deleted (r2 §7.1). Stated: under G1's held-and-omitted marker AV-t predicts no fringes for a4; NC-rep's a4 would match AV-t only for a marker held by no observer, a parked protocol G1 does not define (PROVISIONAL). U4 r2 §6.3 classifies Schwindt's unanalysed polarization as unheld; which convention a physical unread marker takes is left open (LIT C5). The disagreement with Schwindt is kept for NC-rep as a law family, with the background condition: raw `V` is at or below the subtracted value, and the raw-level comparison is not made in G1, since the signal rate needed to add the background is not in LIT |
| 5 | Visible-herald route for the ready screen omitted | **applied** | New row in r2 §4.2: preparation native at the D3 cost (OA1:328, :156–160 via U1:284–285 [M-r]), with the herald held at `t_c` unsourced at C-RET (U1:300–304, :590–599). MR★:639 and OA1:328 reconciled: one concerns process-produced marks in `φ`, the other a read of a held visible configuration. G1-F4's location restated: C-PREP on the counting-measure route, the herald's C-RET on the visible-herald route |
| 6 | "No protocol reaches available" needs its `μ` scope and conditions | **applied** | The per-protocol summary is now under μ-G, with the factor-set condition (U2 §11.1) on every *not available* and the PROVISIONAL tags where they apply (r2 §4.2). The coupling-switch verdict is stated to rest on D5 and the factor-set reading alone; U4 §2.1 bears on the O11 stop only. Added: under a declared `μ` with ready cells or a register as `μ`-data, C-PREP, C-REC and C-RET are available relative to `μ` (U1:275, :524–525, :576–577), and the screen's remaining blocker is R1's persistence, undecided (C-4) |
| 7 | O11 stop also covers a1 vs a4 and the auxiliary protocols | **applied** | r2 §9 extends the conditional O11 stop to a1 against a4, to `𝒜_10 ∖ 𝒜_6` and to the Deletion control (PROVISIONAL where on U4 §2.1). r2 §4.2: E-prep realizes a4 with another marker preparation, not a1. Owner question 1 now says the auxiliary protocols are comparable within `I` on K1 only through that stop. Minor part: blocking by a prepared content correlated with the carrier under `μ` is listed as **not classified**, with the reason that no ground on record excludes it without reference to outcomes (r2 §4.2, §9) |
| 8 | `κ_cmp` withholds counted misses on qualitative raw-direct features | **applied** | A qualitative miss is defined and counted, reported separately from quantitative misses: fringes present/absent classified by the image's `V` against fixed `v_+ = 0.5`, `v_− = 0.2`, with a no-count band; a π-shift by the sign of the channels' covariance (r2 §5.7). Advisory part applied: the interval multiple is fixed at `k = 3σ`, every deviation reported in `σ` units, with the trial count. The constants are flagged as explicit choices (owner question 5) |
| 9 | κ-orb's weight; κ-ens's hidden premise | **applied** | (a) κ-orb reports the agreeing set as all, some or none of the orbits in the support, with its `μ`-mass beside it and no weight fixed; the weight is G4's (r2 §5.6; owner question 3). (b) H-ens named as κ-ens's hypothesis (independent draws across the runs of one history), recorded as AW-ens; G1-F5 restated: κ-ens needs no renewal action only because of H-ens |

## Minor

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| 10 | `κ_det`'s ground, standing, partition and tick | **applied** | Ground recited to U1:519 and MR★ C-3; R1 (U1:514) quoted for what it does and does not require (r2 §5.2). `κ_det` is flagged as an explicit choice (AW-det). The alternative `κ_det^part` (declared click class, no ready reference) is stated and carried as a separate instance, since no target-neutral ground on record excludes it; its consequence for a uniform screen law is stated (owner question 2). The partitions and click classes are listed under NC-γ1. The tick is tied: the readout held at `t_c`; an earlier departure enters only if retained (C-RET) |
| 11 | E-decl's ground needs the record map fixed | **applied** | Record map stated as fixed; a declaration that changes the reported cells is E-read, one that changes `Obs` is §2.1 and O11 (r2 §2.2) |
| 12 | Two PROVISIONAL tags missing | **applied** | T0 row (r2 §4.2, now citing U4 r2 §3.2) and NC-noise (r2 §7.1) tagged |
| 13 | C0 and NC-rep equalities hold on the screen part only | **applied** | C0's full laws carry the blocked mass `δ_blk`; the sum holds on the screen part per incident particle, and the full laws are stated not to add (r2 §7.1). NC-rep's equalities stated on the screen part |
| 14 | Loss ledger held by no observer | **applied** | `V_E ⊇ H_e ∪ L` (r2 §2.1) |
| 15 | "D is not measured" overstates LIT §3 | **applied** | Restated: `D` is defined as a maximum of `K`; the FULL-read sources report `K` for a chosen measurement, which can be below `D`; Dürr's PRL abstract states that `D` and `V` were measured independently (ABSTRACT; method NOT READ) (r2 §2.4, §5.5, §10) |
| 16 | OCP:45 is the wrong citation for an outcome-chosen partition | **applied** | Cited as an outcome-based choice (K-2, NC-γ1), with OCP:45 kept only for the case where the sorted subset is treated as the incident ensemble (r2 §2.3) |

## Advisory

| # | Finding | Disposition | Where and how |
|---|---|---|---|
| A1 | Without `𝒜_10`, `π_P`, `π_C` have no operational test | **applied** | Added to r2 §2.4, to G1-F1 and its cross-propagation (r2 §10), and to owner question 1 |
| A2 | E-read places a5, a6 in the classical-eraser class | **applied** | Recorded as an unchecked candidate for G5 (r2 §10, cross-propagation; §12) |
| A3 | Hashed instance declaration and trial counts | **applied** | NC-γ1's checkpoint requires a committed, hashed declaration preceding every evaluation in commit order; NC-γ5's requires the count of instances declared after the first evaluation (r2 §7.4) |
| A4 | "Every input derived or disproved" cannot occur with *available* | **applied** | Restated as "every input derived" in r2 §5.7 and §6; a disagreement at the level *available relative to `μ`* is reported relative to that `μ` |

## NEW finding G1-F1, re-verified

After the `K_P` fix, G1-F1 **stands** (r2 §10). Schwindt's `K` needs per-path conditional marker laws
and priors from detected masses in one-path runs. On a4–a6 the records carry no path label, and a2,
a3 specify no marker and keep none in the compared record (OCP:15, :20–21). So `K` is not a functional
of any law on `𝒜_6`. Refinements: the omission is the marker-engaged one-path program; under E-read
the extension is two programs, not four; and the finding concerns `K`, which is what the FULL-read
sources report, with `D` defined as its maximum.

## Changes beyond the findings

- Inputs updated to `20cdb9e5`: U4 r2 (unreviewed there; PROVISIONAL throughout) in place of U4 r1;
  U4-CALC r2 (reviewed ACCEPT), used for two table rows in r2 §4.2 (the marker's masking condition, and
  the screen's coset law under μ-G), for a remark on E-prep (Theorem 1′) and for a G2 slot on NC-copy.
  These are needed because r1's rows cited the earlier undecided state that CALC r2 replaced. The
  later review of U4 r2 on the branch (`fbde6485`) is not used.
- G1-F8 (CONFIRMING) records NC-γ6's hand evaluation.
- Owner question 5 (`κ_cmp`'s constants) is new, from finding 8; owner questions 1–4 are updated.
