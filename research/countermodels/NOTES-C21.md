# NOTES-C21 — the round's explicit exotic cones against R6's Table A2

Round-4 node C21 (recording obligation, coordinator addenda 1–3), opened 2026-10-11T05:34Z (`date -u`), after C17–C19
closed. For each explicit exotic cone handled this round, its standing against R6's Table A2 (the 199 applicable items
at L = `9f9f8257`, as R6 decided them for `K(Z_F)` at level (ii)): which of the 13 FAILS rows it now satisfies or still
fails, whether any SATISFIES row that depends on the cone fails for it, and the 68 NOT REACHED rows listed as R6 lists
them. One table per cone, with the columns the addenda fix.

## The cones

| tag | cone | group (invariance) | seed, `c` | defects | source |
|---|---|---|---|---|---|
| `K384` | HO-24's cone | `G₃₈₄ = ⟨cnot, actT S, actT J⟩ = Stab_C(Z⊗1)` | `h* = (10, 2 − 2i, −1 − 3i, 3 − i)`, `401/400` | 192 | C11.5 |
| `KC` | HO-25 item 1's Clifford cone | `C₂ = ⟨cnot, actC J, actT J, actC S, actT S⟩` (order 11520) | `h_C = (−480 + 7i, 357 + 870i, 939 + 834i, 448 + 486i)`, `100001/100000` | 11520 | C15.2 |
| `Kk` | κ with G16 | `G_κ = closure⟨U(x), G16⟩`, `G16 = ⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` | `h = (6, 2, 1, −1)`, `103/100` | two circles `{(6, ±2, x, ∓x) : |x| = 1}` | C16.4 |
| `K768` | C19.3's cone | `G₇₆₈ = ⟨G₃₈₄, actC nflip⟩ = Stab_C(±Z⊗1)` | `h*`, `10001/10000` | 384 | C19.3 |

Every cone is `K(Z) = (Q3 ∩ Z*) + cone Z`, `Z` the group orbit of `I − cP_h`; H1 by the Schmidt bound, H3 by
Theorem S′ (finite form C17.1 [D] for `K384`, `KC`, `K768`; compact form [W] for `Kk`). C18 produced no new cone.

Hypothesis classification (standing rule 1): the cones are pure cone geometry; H1–H3 are introduced (the
composite-cone conditions of stage 3); the 13 FAILS rows are hypotheses (do-not-assume items, [D] four-token hypotheses,
PT-record candidates), none a theorem or definition at L; no OI inventory item is assumed.

## Reading of the columns (addenda 2 and 3)

- **(b)-instances: invariance under …** — rows I3.137 IE1, I3.142 IE1Drive, I3.150 (b_S4), I3.151 (b_n), I3.152 (b_R1),
  I3.153 (b_DJ), I3.155 FC, I3.165 K2's clause. Each entry is a cone-invariance statement for named operations (`K`
  mapped onto itself by `actC`/`actT` of a rotation, or by a two-token map). Invariance of a cone under a group is not
  operational availability of the group's operations; nothing here decides availability.
- **Q3-level rows** — I3.144 (`Q3`, `twin`, `pauliW`, `twistQ3`), I3.133 `H` (KT4Core), I3.135 FCC, I3.160 homogeneity,
  I3.161 T.
- One column fills the other only through a cited entailment. The ones used: a local-unitary (b)-failure gives `K ≠ Q3`
  (`Q3` is invariant under every local unitary; never the converse); FC ⟺ IE1 given hgate (R6's evidence for I3.155,
  stage 2 [A]); KT4Core ⇒ FCC (I3.140, [D]); homogeneity ⇒ `Q3` (R6 Table A3's evidence for I3.160, stage 4 Y6 [W + L]);
  H3 ⇒ closed; H1 and H3 ⇒ `K ⊆ maxCone` (`K = K*` and `maxCone` is the dual of the product effects,
  CompositeDimension.lean:186 at L; C1's C5 identity); a `cnot`-invariant `CandidateCone` is not `actT reflY`-invariant
  (K2Guard.lean:95, :143 at L); the `d4v` rows are vacuous when their hypothesis fails (I3.139, I3.140: `H`; I3.187: IE1).
- A cone that satisfies all 118 SATISFIES rows is recorded as satisfying **the transferred pair-level premises at L**
  (with the level at which I3.148 holds named), never as satisfying OI or as independent of OI. The 68 NOT REACHED rows
  stay NOT REACHED unless a theorem at L transfers one to the pair cone; R6 found none at the same L.

## S0 — predictions and decision rules, written before the first run of any C21 script (2026-10-11T05:34Z, `date -u`)

Script `experiments/c21_rows.py` (exact: Fractions and Gaussian rationals; sympy only where C1's transcription checks
use it). Inputs read-only: `research/archive/pt/R6/REASSESSMENT.md` (the blob authorized at `4dc0321c`, sha256
`1ff62ad6…`, checked by the script) and `verification/lean-mathlib/OIBridge/CompositeDimension.lean` in this branch's
tree (the blob at L) for the `cnot` transcription.

### Operations tested (each cone)
On each token `τ ∈ {C, T}`: `R_z(π)` (= `rot3(π)`), `R_z(π/2)`, `R_z(t₀)`, `R_x(π)` (= `nflip`), `R_x(π/2)`, `R_x(t₀)`,
`J` (= `cyc3`), `R_n(π/2)` (`n = (3, 0, 4)/5`), `R1` (order 3 about `(5, 1, 1)`), with `cos t₀ = 3/5` (lift
`(2I − iσ)/√5`, a non-Clifford member of each flow). Two-token: `cnot`, SWAP, `transposeW` (complex conjugation `T`),
`actT reflY` (through the kernel chain). An operation `g` is **INVARIANT** iff it maps the defect set onto itself
(finite orbits: canonical rays; `Kk`: the circle identities in the coefficients `g(A) + x g(B)`); otherwise **MOVED**
with an exact witness — a defect `d_l` and `w = g h_l` with `P_w ∈ K` (outside every cap) and `tr(g(d_l) P_w) = 1 − c < 0`,
so `g(d_l) ∉ K* = K`. An operation neither INVARIANT nor given a witness prints UNDECIDED.

### Checks
- **R0** (control) the input's sha256 is `1ff62ad6…`; Table A2 parses to 199 rows: 118 SATISFIES, 68 NOT REACHED,
  13 FAILS; classes `def, thm, gate, inh, d4s` 89 (all SATISFIES), `nr, hmg` 68 (all NOT REACHED), `cone` 12, `kthm` 1,
  `b1` 13, `d4v` 3 (all SATISFIES), `dna` 9, `d4f` 2, `cand` 2 (all FAILS).
- **D1** for every one-token unitary `U` of the list, `actC R(U)` and `actT R(U)` on the 16 basis tables equal
  `Ad(U⊗I)`, `Ad(I⊗U)` (exact; `R(U)_ij = tr(σ_i U σ_j U†)/2`), so the operations tested are the kernel's `actC`/`actT`
  (CompositeDimension.lean:198, :201) of the named rotations. **D2** `cnot = Ad(CNOT)` on the basis tables with the
  kernel's `pc`, `pt`, `sgn` transcribed and compared with the Lean text; `transposeW = T`; SWAP = table transpose.
  **D3** the chain: `cnot prodState(xplus, z3) = phiW`, `actT reflY phiW = idW`, `ipW(idW, cnot prodState(−e₁, −e₃)) = −2`.
- Per cone **k0** (data): orbit size; minimum normalised `|det Ψ|²`; minimum and maximum squared overlap between distinct
  defects; no orthogonal pair; H1 (`1 − 4 min|det Ψ|² ≤ (2/c − 1)²`) and (CC) (`c² s_min ≥ 4(c − 1)`), exact. **kB** the
  22 operations. **kQ** I3.144: `tr(d_h P_h) = 1 − c < 0` (`P_h ∈ Q3 \ K`) and the first `y` of `Φ⁺ = |00⟩ + |11⟩`,
  `Ψ⁺ = |01⟩ + |10⟩`, `Φ⁻ = |00⟩ − |11⟩`, `|00⟩ + i|11⟩` with `P_y ∈ K` (then `(P_y)^Γ` has eigenvalue `−1/2`, so
  `P_y ∉ twin = Γ(Q3)`). FCC (uniform assignment): `X = d_h`, `Y = P_y`, `F = P_χ` with `χ` the first coefficient matrix of
  `[[2, 1], [0, 1]]`, `[[1, 1], [0, 2]]`, `[[3, 1], [1, 2]]`, `[[2, i], [1, 1]]` for which the tuple lies in `K`, and `E = P_ψ`,
  `Ψ = H(ȲXᵀ)⁻¹`, so that the contraction of `Y`, `E`, `F` is the effect `P_h` on the first pair; `famI = Σ X_mn E_mk Y_kl F_nl`
  computed on the tables; cross-check `famI = 16 tr[(x⊗y)(e⊗f)]` on 16×16 operators (independent route); control: the same
  tuple with `X = P_h ∈ Q3` gives `famI > 0`. T-support (finite orbits): `(√s_max + √(1 − 1/c))² < 1/c` exactly (the whole
  null quadric of `d_h` consists of members of `K`, the hypothesis of C3.3's `c = 15`).
- **Controls** (each cone): every generator of the cone's group prints INVARIANT; the membership test rejects `P_h`; the
  known moving maps print MOVED (`K384`: `actC nflip` and `actC J`, by C19-3; `K768`: `actC J`; `KC`: `actT R1` is expected,
  not known — no control; `Kk`: `actT nflip`, whose image `(2, 6, −x, x)` is off both circles). **Q3 control** (once):
  C1's instance pool — `X ∈ {phiW, prodState(z3, z3), cnot prodState(xplus, xplus)}`, `Y, E, F` over the 72 product and
  `cnot`-product tables — has `min famI ≥ 0`.

### Row rules (fixed now)
- I3.137 IE1: FAILS iff some one-token operation is MOVED. I3.155 FC: I3.137's verdict (hgate by `cnot` INVARIANT).
  I3.165 K2's clause: FAILS iff some one-token operation is MOVED.
- I3.142 IE1Drive: on `τ`, FAILS iff one of `R_z(π)`, `R_z(π/2)`, `R_z(t₀)`, `J` on `τ` is MOVED; the row FAILS iff it fails
  on some token (C1's rule); per-token outcomes printed.
- I3.150 (b_S4): on `τ`, FAILS iff some operation on `τ` is MOVED; the row FAILS iff it fails on both tokens; a token with
  no witness is printed "not refuted by the list" (a finite list does not establish invariance under every rotation).
- I3.151 (b_n): on `τ`, FAILS iff `R_n(π/2)` on `τ` is MOVED; the row FAILS iff both tokens fail.
- I3.152 (b_R1): on `τ`, FAILS iff `R1` on `τ` is MOVED, SATISFIES iff INVARIANT (`R1` has order 3); the row FAILS iff both
  tokens fail, and is recorded SATISFIED in a token's reading where `R1` is INVARIANT.
- I3.153 (b_DJ): on `τ`, FAILS iff one of `R_z(π)`, `R_z(π/2)`, `R_z(t₀)`, `R_x(π)`, `R_x(π/2)`, `R_x(t₀)`, `J` on `τ` is
  MOVED; the row FAILS iff both tokens fail.
- I3.144: FAILS iff both kQ witnesses exist. I3.135 FCC: FAILS iff the tuple exists, lies in `K` and `famI < 0` (with the
  cross-check and control green). I3.133: FAILS iff I3.135 FAILS (I3.140). I3.160: FAILS iff `P_h ∉ K` (homogeneity ⇒
  `Q3`). I3.161 T: finite orbits FAILS by C3.3/C11.7 [W] with `c(P00) = 9` (C3.2) and [A] Y6, the T-support check
  recorded (if it fails, C3.3's covering form — finitely many caps — is what carries the row); `Kk` FAILS by C16.5, cited.
- `d4v`: I3.139, I3.140 SATISFIES (vacuous) iff I3.133 FAILS; I3.187 iff I3.137 FAILS.
- `cone` rows: SATISFIES iff H1 and (CC) hold exactly and `cnot` is INVARIANT (H3 then by S′); I3.132 and I3.148 at level
  (i) through `cnot`; I3.148 at level (ii) SATISFIES iff `cnot`, `actC R_z(π)` (= `Ad(Z⊗I)`), `actT R_z(π)` (= `Ad(I⊗Z)`)
  and `transposeW` are all INVARIANT, otherwise "level (i) only", with the moving generator: a Table-A2 SATISFIES row that
  fails for the cone at level (ii). `kthm` I3.44: SATISFIES [K] iff D3 passes and `cnot` is INVARIANT. `b1`: SATISFIES
  iff `K ⊆ maxCone` (H1 and H3). The 89 K-independent rows: Table A2's verdict, carried. The 68 NOT REACHED rows: listed
  NOT REACHED.

`VERDICT C21-EXACT` iff R0, D1–D3, every cone's k0 reproduces its source, no operation is UNDECIDED, and every control
behaves as stated; the row outcomes are recorded, not required.

### Predictions (stated before the run; medium confidence except where noted)
- R0, D1–D3, k0 as stated (high).
- Operations: `K384` — on the target `R_z(π)`, `R_z(π/2)`, `R_x(π)`, `R_x(π/2)`, `J` INVARIANT, the non-Clifford four
  MOVED; on the control `R_z(π)`, `R_z(π/2)` INVARIANT, the other seven MOVED; `cnot` INVARIANT; SWAP MOVED;
  `transposeW` MOVED (guess). `K768` — as `K384`, with the control's `R_x(π)` INVARIANT. `KC` — every Clifford one-token
  operation INVARIANT on both tokens, SWAP INVARIANT, the non-Clifford ones MOVED, `transposeW` MOVED (guess). `Kk` —
  `R_z(π)` INVARIANT on both tokens, `cnot` and `transposeW` INVARIANT, every other one-token operation MOVED, SWAP MOVED.
- Rows: the 13 FAILS rows still FAIL for all four cones, each with witnesses that differ from `K(Z_F)`'s (for `KC` only
  non-Clifford rotations move the cone); the 29 K-dependent SATISFIES rows SATISFIES, except I3.148 at level (ii) for the
  cones that are not `transposeW`-invariant (guess: `K384`, `KC`, `K768`); `Kk` satisfies I3.148 at level (ii).
- The first FCC candidates lie in `K` for every cone; `famI < 0`. T-support passes for `K384` (`s_max = 13/16`) and
  `K768`; for `KC` no prediction.

## Runs (written 2026-10-11T05:50Z, `date -u`)

- Run 1 (05:40:45Z, 2 min): 25/25, `VERDICT C21-EXACT`. Kept as `experiments/c21_rows.run1.{py,out,err}`.
- Run-2 amendment (two RECORD lines; no check, rule or decision changed; disclosed in the script's docstring): (1) the
  T-support bound fixed in S0, `√s_max + √(1 − 1/c) < √(1/c)`, rests on `cos(β − α) ≤ cos β + sin α` and is loose; run 1
  printed it False for `KC` (`s_max = 1560203344561/1566477528100`). The sharp form `s_max ≤ (2/c − 1)²` (the nearest other
  defect at Fubini–Study distance at least twice the cap radius, so the whole null quadric of `d_h` lies outside every
  other open cap) is printed as well: True for `K384`, `KC`, `K768`. The T row is decided as S0 fixed (C3.3/C11.7).
  (2) For `Kk` run 1 printed `actC R_z(π/2)` and `actC R_z(t₀)` INVARIANT, against S0's prediction; the record checks the
  identity `(I⊗Z)U(x)(I⊗Z)U(x) = diag(1, x)⊗I` (exact at `x = (3 + 4i)/5`), which puts the whole control phase flow —
  `actC R_z(t)` for every `t` — in `G_κ`.
- Run 2 (05:44:15Z): 25/25, `VERDICT C21-EXACT`; its output equals run 1's plus the four RECORD lines (`diff`). Replay at
  05:48Z byte-identical (`cmp` on `.out` and `.err`).
- Predictions against outcome: R0, D1–D3, k0 as stated. Operations as predicted for `K384`, `KC`, `K768` (including
  `transposeW` MOVED for all three, guessed); for `Kk` the prediction "every one-token operation other than `R_z(π)`
  MOVED" FAILED — the control's `R_z(π/2)` and `R_z(t₀)` are INVARIANT (the control phase flow lies in `G_κ`). Rows as
  predicted: all 13 FAILS rows still fail for all four cones, and I3.148 at level (ii) fails exactly for the three cones
  that `transposeW` moves. FCC tuples found with the first candidates; T-support as predicted for `K384`, `K768`.

## Results

### C21-0 — the K-independent checks
R0: the authorized blob (sha256 `1ff62ad6…`), Table A2 = 199 rows (118 / 68 / 13; classes as S0 states). D1: for each
of the nine one-token unitaries, `actC R(U)` and `actT R(U)` act on the 16 basis tables as `Ad(U⊗I)`, `Ad(I⊗U)`; the
families tested are the kernel's: the drive flow `rot3 t = R_z(t)` (KInfFoundations.lean:350 `rotFun`, :411 `rot3`), its
NOT `rot3 π`, `J = cyc3` (:425), assembled as `ball3Drive` (:449); `nflip = R_x(π)`; `actC`, `actT` as
CompositeDimension.lean:198, :201. D2: `cnot = Ad(CNOT)` with `pc`, `pt`, `sgn` equal to the Lean text at L;
`transposeW` = complex conjugation; SWAP = table transpose. D3: the K2Guard chain, value `−2`. Q3 control for FCC: C1's
instance pool has minimum `famI = 0`.

### C21-1 — one table per cone (generated from `c21_rows.out`, TABLE lines; in-cell separators rendered as `;`)

Each "(b)" entry is a cone-invariance statement — `K` mapped onto itself by the named operation (satisfied) or moved,
with an exact witness `tr(g(d_l) P_w) = 1 − c < 0`, `P_w ∈ K` (failed; the OP lines of `c21_rows.out` give each witness and
the largest squared overlap of `w` with the defects). It says nothing about whether the operation is operationally
available. The Q3 column of a (b)-row is filled only by the cited entailment "a local unitary moves `K` ⇒ `K ≠ Q3`";
no (b)-entry is inferred from a Q3-level entry.

#### `K384`

| item | (b)-instances: invariance under …, satisfied/failed, by operation | Q3-level rows: satisfied/failed | Table A2 (K(Z_F)) → this cone |
|---|---|---|---|
| I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | control — satisfied: R_z(π), R_z(π/2); failed: R_z(t₀), R_x(π), R_x(π/2), R_x(t₀), J, R_n(π/2), R1; target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀), R_n(π/2), R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | control — satisfied: R_z(π), R_z(π/2); failed: R_z(t₀), J; target — satisfied: R_z(π), R_z(π/2), J; failed: R_z(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.150 (b_S4) | control: failed; target: failed (operations as I3.137) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.151 (b_n) | control — failed: R_n(π/2); target — failed: R_n(π/2) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.152 (b_R1) | control — failed: R1; target — failed: R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.153 (b_DJ) | control — satisfied: R_z(π), R_z(π/2); failed: R_z(t₀), R_x(π), R_x(π/2), R_x(t₀), J; target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.155 frame covariance (FC) of the native gate | FC ⟺ IE1 given hgate (R6 I3.155 evidence; hgate: cnot INVARIANT) | — | FAILS → FAILS |
| I3.165 K2 | failed: the operations listed under I3.137 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.144 `Q3`, `twin`, `pauliW`, `twistQ3` | — | failed: P_h in Q3 \ K (1 − c = −1/400); Φ⁺ in K \ twin | FAILS → FAILS |
| I3.133 `H` | — | failed: via I3.140 (KT4Core ⇒ FCC, [D]) and I3.135 | FAILS → FAILS |
| I3.135 FCC | — | failed: famI = −4/375 at (d_h, P_y, P_ψ, P_χ) | FAILS → FAILS |
| I3.160 H | — | failed: homogeneity ⇒ Q3 (stage 4 Y6 [W + L]); K ≠ Q3 | FAILS → FAILS |
| I3.161 T | — | failed: C3.3/C11.7 (finitely many non-PSD extreme rays: c = 15 on defects), c(P00) = 9 (C3.2); T-support (S0 form) True | FAILS → FAILS |
| I3.148 H2 | cnot: invariant; level (ii): failed (moved by transposeW) | — | SATISFIES → SATISFIES at level (i) only |

Two-token maps: cnot INVARIANT, SWAP MOVED, transposeW MOVED

#### `KC`

| item | (b)-instances: invariance under …, satisfied/failed, by operation | Q3-level rows: satisfied/failed | Table A2 (K(Z_F)) → this cone |
|---|---|---|---|
| I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | control — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀), R_n(π/2), R1; target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀), R_n(π/2), R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | control — satisfied: R_z(π), R_z(π/2), J; failed: R_z(t₀); target — satisfied: R_z(π), R_z(π/2), J; failed: R_z(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.150 (b_S4) | control: failed; target: failed (operations as I3.137) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.151 (b_n) | control — failed: R_n(π/2); target — failed: R_n(π/2) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.152 (b_R1) | control — failed: R1; target — failed: R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.153 (b_DJ) | control — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀); target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.155 frame covariance (FC) of the native gate | FC ⟺ IE1 given hgate (R6 I3.155 evidence; hgate: cnot INVARIANT) | — | FAILS → FAILS |
| I3.165 K2 | failed: the operations listed under I3.137 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.144 `Q3`, `twin`, `pauliW`, `twistQ3` | — | failed: P_h in Q3 \ K (1 − c = −1/100000); Φ⁺ in K \ twin | FAILS → FAILS |
| I3.133 `H` | — | failed: via I3.140 (KT4Core ⇒ FCC, [D]) and I3.135 | FAILS → FAILS |
| I3.135 FCC | — | failed: famI = −125159/5319389250 at (d_h, P_y, P_ψ, P_χ) | FAILS → FAILS |
| I3.160 H | — | failed: homogeneity ⇒ Q3 (stage 4 Y6 [W + L]); K ≠ Q3 | FAILS → FAILS |
| I3.161 T | — | failed: C3.3/C11.7 (finitely many non-PSD extreme rays: c = 15 on defects), c(P00) = 9 (C3.2); T-support (S0 form) False; sharp form True (record T2) | FAILS → FAILS |
| I3.148 H2 | cnot: invariant; level (ii): failed (moved by transposeW) | — | SATISFIES → SATISFIES at level (i) only |

Two-token maps: cnot INVARIANT, SWAP INVARIANT, transposeW MOVED

#### `Kk`

| item | (b)-instances: invariance under …, satisfied/failed, by operation | Q3-level rows: satisfied/failed | Table A2 (K(Z_F)) → this cone |
|---|---|---|---|
| I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | control — satisfied: R_z(π), R_z(π/2), R_z(t₀); failed: R_x(π), R_x(π/2), R_x(t₀), J, R_n(π/2), R1; target — satisfied: R_z(π); failed: R_z(π/2), R_z(t₀), R_x(π), R_x(π/2), R_x(t₀), J, R_n(π/2), R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | control — satisfied: R_z(π), R_z(π/2), R_z(t₀); failed: J; target — satisfied: R_z(π); failed: R_z(π/2), R_z(t₀), J | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.150 (b_S4) | control: failed; target: failed (operations as I3.137) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.151 (b_n) | control — failed: R_n(π/2); target — failed: R_n(π/2) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.152 (b_R1) | control — failed: R1; target — failed: R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.153 (b_DJ) | control — satisfied: R_z(π), R_z(π/2), R_z(t₀); failed: R_x(π), R_x(π/2), R_x(t₀), J; target — satisfied: R_z(π); failed: R_z(π/2), R_z(t₀), R_x(π), R_x(π/2), R_x(t₀), J | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.155 frame covariance (FC) of the native gate | FC ⟺ IE1 given hgate (R6 I3.155 evidence; hgate: cnot INVARIANT) | — | FAILS → FAILS |
| I3.165 K2 | failed: the operations listed under I3.137 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.144 `Q3`, `twin`, `pauliW`, `twistQ3` | — | failed: P_h in Q3 \ K (1 − c = −3/100); Φ⁺ in K \ twin | FAILS → FAILS |
| I3.133 `H` | — | failed: via I3.140 (KT4Core ⇒ FCC, [D]) and I3.135 | FAILS → FAILS |
| I3.135 FCC | — | failed: famI = −21/125 at (d_h, P_y, P_ψ, P_χ) | FAILS → FAILS |
| I3.160 H | — | failed: homogeneity ⇒ Q3 (stage 4 Y6 [W + L]); K ≠ Q3 | FAILS → FAILS |
| I3.161 T | — | failed: C16.5 (c = 14 on defects), c(P00) = 9 (C3.2) | FAILS → FAILS |
| I3.148 H2 | cnot: invariant; level (ii): satisfied | — | SATISFIES → SATISFIES |

Two-token maps: cnot INVARIANT, SWAP MOVED, transposeW INVARIANT

#### `K768`

| item | (b)-instances: invariance under …, satisfied/failed, by operation | Q3-level rows: satisfied/failed | Table A2 (K(Z_F)) → this cone |
|---|---|---|---|
| I3.137 IE1 (`IE1`, with `IsRot3`, `IsOrth3`) | control — satisfied: R_z(π), R_z(π/2), R_x(π); failed: R_z(t₀), R_x(π/2), R_x(t₀), J, R_n(π/2), R1; target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀), R_n(π/2), R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.142 `IE1Drive`, `ie1Drive_of_ie1` (the only pair-level lift of the … | control — satisfied: R_z(π), R_z(π/2); failed: R_z(t₀), J; target — satisfied: R_z(π), R_z(π/2), J; failed: R_z(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.150 (b_S4) | control: failed; target: failed (operations as I3.137) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.151 (b_n) | control — failed: R_n(π/2); target — failed: R_n(π/2) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.152 (b_R1) | control — failed: R1; target — failed: R1 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.153 (b_DJ) | control — satisfied: R_z(π), R_z(π/2), R_x(π); failed: R_z(t₀), R_x(π/2), R_x(t₀), J; target — satisfied: R_z(π), R_z(π/2), R_x(π), R_x(π/2), J; failed: R_z(t₀), R_x(t₀) | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.155 frame covariance (FC) of the native gate | FC ⟺ IE1 given hgate (R6 I3.155 evidence; hgate: cnot INVARIANT) | — | FAILS → FAILS |
| I3.165 K2 | failed: the operations listed under I3.137 | K ≠ Q3 (entailed: a local unitary moves K; never the converse) | FAILS → FAILS |
| I3.144 `Q3`, `twin`, `pauliW`, `twistQ3` | — | failed: P_h in Q3 \ K (1 − c = −1/10000); Φ⁺ in K \ twin | FAILS → FAILS |
| I3.133 `H` | — | failed: via I3.140 (KT4Core ⇒ FCC, [D]) and I3.135 | FAILS → FAILS |
| I3.135 FCC | — | failed: famI = −4/9375 at (d_h, P_y, P_ψ, P_χ) | FAILS → FAILS |
| I3.160 H | — | failed: homogeneity ⇒ Q3 (stage 4 Y6 [W + L]); K ≠ Q3 | FAILS → FAILS |
| I3.161 T | — | failed: C3.3/C11.7 (finitely many non-PSD extreme rays: c = 15 on defects), c(P00) = 9 (C3.2); T-support (S0 form) True | FAILS → FAILS |
| I3.148 H2 | cnot: invariant; level (ii): failed (moved by transposeW) | — | SATISFIES → SATISFIES at level (i) only |

Two-token maps: cnot INVARIANT, SWAP MOVED, transposeW MOVED

### C21-2 — the other 186 rows
- **The 29 K-dependent SATISFIES rows** hold for every cone: the `cone` rows (I3.43, I3.114, I3.116, I3.118, I3.130,
  I3.131, I3.132, I3.147, I3.148, I3.149, I3.156, I3.159) by k0 (H1 and (CC) exact), H3 by Theorem S′ (finite form
  C17.1 [D]; compact form [W] for `Kk`), `cnot` INVARIANT, closedness from self-duality and the slice check (C1's C6,
  K-independent); `kthm` I3.44 by D3 with `cnot` INVARIANT (K2Guard.lean:143: a `cnot`-invariant candidate cone is not
  `actT reflY`-invariant); the 13 `b1` rows (I3.48, I3.51, I3.54, I3.55, I3.56, I3.58, I3.60, I3.73, I3.74, I3.75,
  I3.170, I3.171, I3.172) by `K ⊆ maxCone` (H1 and H3; CompositeDimension.lean:186); the `d4v` rows vacuously (I3.139,
  I3.140: `H` fails; I3.187: IE1 fails). **One difference from Table A2**: I3.148 (H2) at level (ii) — G16-invariance —
  fails for `K384`, `KC`, `K768`, which `transposeW` moves (witness `1 − c`: `−1/400`, `−1/100000`, `−1/10000`);
  they hold it at level (i) (`cnot`), as Table A1 reads it for `K(E0)`. `Kk` holds it at level (ii). I3.132 (hgate,
  preservation by the native gate) holds for all four through `cnot`.
- **The 89 K-independent rows** (classes `def`, `thm`, `gate`, `inh`, `d4s`) carry Table A2's verdict unchanged:
  their statements do not quantify over the pair cone or are single-token facts inherited by every cone on two copies of
  the ball.
- **The 68 NOT REACHED rows** are NOT REACHED for every cone, as Table A2 lists them: I3.96 I3.99 I3.104 I3.105 I3.134 I3.136 I3.141 I3.145 I3.146 I3.154 I3.157 I3.158 I1.17 I4.3 I4.4 I4.14 I4.29 I4.31 I4.42 I4.45 I4.56 I4.65 I4.66 I4.67 I4.68 I4.69 I4.70 I4.73 I4.74 I4.80 I4.82 I4.85 I4.87 I4.88 I4.96 I4.99 I4.102 I4.110 I4.115 I4.118 I4.120 I4.123 I4.124 I4.127 I4.128 I4.133 I4.137 I4.143 I4.144 I4.179 I4.187 I4.210 I4.215 I4.216 I4.241 I4.244 I4.245 I2.3 I2.29 I2.30 I2.31 I2.32 I2.33 I2.34 I2.35 I2.62 I2.63 I2.69. R6 found no theorem at
  the same L transferring any of them to the pair cone (no H→P, M→P or G→P bridge; no structure with three or more
  tokens; P-STAGE2, P-ACT2 absent); nothing at L has changed, so none is decided here.

### C21-3 — standing and the weaker alternatives
| cone | 118 SATISFIES rows | 13 FAILS rows | 68 NOT REACHED | label | weaker alternative it witnesses: with H1–H3, does not force `Q3` |
|---|---|---|---|---|---|
| `K384` | all; I3.148 at level (i) (level (ii) fails: `transposeW`) | all still fail | listed | satisfies the transferred pair-level premises at L (I3.148 at level (i)) | invariance under `Stab_C(Z⊗1) = G₃₈₄`: `cnot`, every one-token Clifford rotation of the target (`R_z(π)`, `R_z(π/2)`, `R_x(π)`, `R_x(π/2)`, `J`), the control's `R_z(π)`, `R_z(π/2)` |
| `KC` | all; I3.148 at level (i) (level (ii) fails: `transposeW`) | all still fail | listed | satisfies the transferred pair-level premises at L (I3.148 at level (i)) | invariance under the two-qubit Clifford group `C₂`: every one-token Clifford rotation on both tokens, `cnot`, SWAP |
| `Kk` | all, I3.148 at level (ii) | all still fail | listed | satisfies the transferred pair-level premises at L (level (ii)) | invariance under G16, κ's gate flow `U(x)` and the control's whole `R_z` flow — the kernel's drive flow `rot3` on the control, without its `J` |
| `K768` | all; I3.148 at level (i) (level (ii) fails: `transposeW`) | all still fail | listed | satisfies the transferred pair-level premises at L (I3.148 at level (i)) | invariance under `Stab_C(±Z⊗1) = G₇₆₈`: as `K384`, with the control's NOT `R_x(π)` |

None of the 13 FAILS rows is satisfied by any of the four cones. What changes is the operation through which a row
fails. Table A2's witnesses for `K(Z_F)` — `actC cyc3` (I3.150, I3.153, I3.142), `actC R_x(π/2)` (I3.153) — are
invariances of `KC`, so for `KC` every (b)-row fails only through the non-Clifford rotations tested (`R_z(t₀)`, `R_x(t₀)`,
`R_n(π/2)`, `R1`, on both tokens). `K384` and `K768` keep Table A2's control witnesses but are invariant under every
Clifford rotation of the target. For `Kk` the drive flow is an invariance on the control; IE1Drive fails there through
`J` alone, and (b_DJ) through the `R_x` flow and `J` (on the target every listed operation except `R_z(π)` moves it).

Each of these is a pair-level countermodel to the named invariance hypothesis with H1–H3. It is not a countermodel to
OI's quantum conclusion: the 68 NOT REACHED rows are untouched, and cone invariance is not operational availability.

## Verdict on node C21
- The four explicit exotic cones of this round stand against Table A2 as `K(Z_F)` does — 118 SATISFIES, 13 FAILS,
  68 NOT REACHED — except that `K384`, `KC` and `K768` hold I3.148 (H2) only at level (i). No FAILS row becomes
  satisfied; the operations through which the (b)-rows fail differ by cone (C21-3).
- Each cone witnesses that a named weaker alternative does not force `Q3` at the pair level: invariance under
  `Stab_C(Z⊗1)`, under `Stab_C(±Z⊗1)`, under the full two-qubit Clifford group with SWAP, and under G16 with κ's gate
  flow and the drive flow on one token (without `J`).

## Gem classification (§A.31)
- CONFIRMING: R6's classification extends to the four cones; no item at L excludes any of them.
- NEW: (i) `KC` is invariant under every one-token operation Table A2 uses to refute the (b)-rows for `K(Z_F)`; the (b)-rows
  fail for it only at non-Clifford rotations. (ii) `Kk` is invariant under the kernel's drive flow on one token (the
  control), so the flow without `J` — with G16 and κ's gate flow — does not force `Q3`; `J` (or the `R_x` flow) is
  load-bearing in R6's "{ball3Drive flow, J} forces Q3".
- Assumption-watch marker: "an exotic cone fails (b) at the operations Table A2 lists for `K(Z_F)`" is false; which
  operation moves a cone depends on the cone. A sourcing argument for (b) that reaches only finitely many Clifford
  rotations, or the drive flow without `J`, leaves an explicit exotic cone standing.
- Process: S0's T-support bound was loose; the sharp form is recorded (run-2 amendment).

## What is not claimed
No operational availability of any operation (cone invariance only); no invariance under a continuous family except the
control phase flow of `Kk` (by the group identity) — a finite list of operations refutes, it does not establish;
nothing about the 68 NOT REACHED rows beyond R6's record at L; the items `pauliW`, `twistQ3` of I3.144 not examined
separately (as R6); level-(ii) versions of `K384`, `KC`, `K768` (orbits closed under `transposeW`) not attempted;
"satisfies the transferred pair-level premises at L" is not "satisfies OI" and not "independent of OI".
