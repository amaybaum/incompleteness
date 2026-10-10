# Coordinator's audit of thread U — UNIQ (stage 3, Q-SD proof attempt; launch 3)

Audited: `pt/U/RESULT.md`, sha256 `4999fef697ab086689ac39926f58d55222cce4b1b9d402e324933bf1df832f9d`; `pt/U/NOTES.md`
`40cc1e21…`; `.start_marker` `c2115cd0…` (as listed in RESULT §5). `pt/U/` holds 46 entries and no subdirectory.
Protocol: `PROTOCOL-STAGE3.md` (`1a649168…`). Launches 1 and 2 of U are recorded in `pt/audit/STAGE3-RELAUNCH-LOG.md`
(their markers under `pt/audit/aborted-launches/`); launch 3 ran with the Opus model and the write-in-parts constraint.
Thread X was audited in parallel (`pt/audit/X/AUDIT-X.md`); neither thread read the other.

## Integrity
- **Coordinator's check, 12:57Z**: six manifests OK; `pt/base` HEAD `9f9f8257…`, clean, no bytecode; six protocol
  hashes and `PROTOCOL-NS.sha256` unchanged.
- **The start marker.** Written 11:23:27Z into a freshly created `pt/U/`; this is the `pt/` directory mtime that X's
  end sweep flagged (AUDIT-X, integrity). Sha256 as listed.
- **Hashes.** The 19 distinct sha256 values quoted in RESULT §4–§5 were re-checked against the files: all 8 script
  hashes, all 8 `.out` hashes, `u5_kf.run1.py`, `u5_kf.run1.out` and the start marker match; every `.err` of a
  successful run is `exit 0` (`28d3b9e8…`).
- U's end sweep (12:52:31Z) found no file newer than its marker outside `pt/U/` (excluding `pt/X/`, `pt/audit/`,
  `pt/audit*-replay/`). Consistent with the coordinator's record: every coordinator write in that window was under
  `pt/audit/`.
- Reads: `pt/X/` never read. Writes: `pt/U/` only. No breach recorded or found.

## Replays
Run as `python3 -I -B` from `pt/audit/U/replay/` (scripts copied there; none reads argv or `pt/base`). All eight
reproduce stdout byte for byte (`cmp`); stderr differs only in my harness's exit-line format (`exit=0` against
`exit 0`):

| script | checks | replay stdout |
|---|---|---|
| `u1_struct` | 21/21 | identical |
| `u1_kstar` | 27/27 | identical |
| `u1_kstar_cc` | 11/11 | identical |
| `u2_wigner` | 10/10 | identical |
| `u3_vplus` | 8/8 | identical |
| `u4_kf2` | 5/5 | identical |
| `u5_kf` (run 2) | 15/15 | identical |
| `u5_level2_N` [N] | no verdict by rule | identical (numpy seed 12345; ran 5.5 min) |

The recorded failed run (`u5_kf.run1`, 14/15: the thread's countercontrol PLc probed the wrong eigenvector, so the
control did not register; only that line changed) was not re-executed; its record is consistent with RESULT §4 and
NOTES N10–N11.

## Independent check (no thread code)
`indep_checkQSD.py` in `pt/audit/X/` (one script for both threads, written from the landed definitions and the two
result files' claims; sections S, H1, H2, H3, W, described in AUDIT-X). The checks that bear on U's claims: the
spectral certificates and the orthonormal `f_s` (S1–S3, Theorem E's hypothesis (a)); `F = z_(−1,−1)` and `cnot`'s
action (S4); the SOS identities (H1a–b, H1 of Theorem E); the native-class computation from the landed predicates
over all 4096 dressings, the order-16 group `⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` and its permutation of `Z_F` (H2b–d, level
(ii)); `⟨E0, Ad(Z⊗I)E0⟩ = −1` (H2e, the level-(ii) exclusion of `E0` and the IE1 failure of uniform `K★`);
`ipW(q, z_s) = tr q/2 − ⟨f_s|q|f_s⟩` for symbolic Hermitian `q` (H3b, hypothesis (b)); the projection lemma on rank-one
cap batteries for `E0` and `F` by a method different from U's determinant identities (H3c–d, hypothesis (c)), with the
countercontrol `e_{3/2}` failing exactly at `t² > 3/7` (H3e); `ipW(E0,E0) = 3`, `−E0 ∉ PSD` (H3g, hypothesis (d));
the witness pairs (W1); `Y1 = E0^Γ`, `⟨Y1, cnot Y1⟩ = −1` (W4, U1(b)); `F + cnot F ⪰ 0` (W5, U4). Runs 1–3 failed
on harness errors only (five; then my own predicted countercontrol boundary; then a tuple-indexing crash in the
corrected line), all recorded in AUDIT-X with the exact derivation of the boundary; **run 4: 25/25 CONFIRMED,
`VERDICT INDEP-QSD-CONFIRMED`**, concurrent replay byte-identical (reproducibility only); script `518b4952…`, output
`cdd04849…`. For U specifically this re-establishes, by a different method and without U's code, every exact
ingredient Theorem E cites — hypotheses (a)–(d) of Theorem S for `Z_F` and `{F, cnot F}`, the projection lemma on
rank-one cap batteries, the level-(ii) group and its action — and the necessary conditions of U1(b).

**Reproducibility and correctness, kept apart.** The replays (U's own and the coordinator's) establish that U's
scripts are deterministic and that the recorded outputs are theirs. Correctness of EXOTIC rests on Theorem S and the
projection lemma as written proofs, re-derived below; on the coordinator's independently implemented checks of the
exact ingredients (a different method for the projection lemma, the native class recomputed from the landed
predicates); and on X's independent arrival at the same cones by a different proof. The one [L] dependency (the
classification of `Aut(PSD₄)`) sits in a class row, not under EXOTIC.

## Written proofs reviewed

**U1(a) consequences of H1–H3 — CONFIRMED.** Items 1–7 re-derived. Item 2 (`maxCone = dualW SEP`) is the stage-2
reading of `IsEffectOn`/`pairVal`, audited in AUDIT-S2. Item 4 (the owner's observation and the witness-pair form)
matches `qsd_owner_consequences.py` (6/6). Items 5–7 (`V±`, `Q3 ∩ V+ = PSD(3) ⊕ ℝ₊`, self-duality of `K+` within
`V+`, `|k−| ≤ |k+|`) match the same script and `qsd_owner_note2.py`.

**U1(b) necessary conditions — CONFIRMED.** `Y1 = E0^Γ ∈ K_E` with `⟨Y1, cnot Y1⟩ = −1` (independent check W4);
"`K★` misses exactly the open `E0`-cap": a pure `P = q + sE0` with `s > 0` would give `ρ(P) ⪰ s ρ(E0)`, but `ρ(E0)` is
positive definite on a 3-dimensional subspace while `ρ(P)` has rank one, so some unit vector in that subspace is
annihilated by `ρ(P)` and not by `ρ(E0)` ✓. The level-(ii) exclusion of `E0` (`⟨E0, Ad(Z⊗I)E0⟩ = −1`) is
independent check H2e.

**Theorem S (surgery) — CONFIRMED.** Self-positivity ✓; closedness and the dual formula from (d) ✓ (an element
`−Σσ_i z_i` of `Q` is excluded, so `(Q ∩ Z*) ∩ −cone Z = {0}` and `Q ∩ −cone Z = {0}`); the rewriting of
`y = q + Σσ_i z_i ∈ Z*` when `q` violates exactly one constraint ✓ (`σ_i ≥ c/|z_i|²` from orthogonality; `Π_i q ∈ Q`
by (c); `⟨Π_i q, z_j⟩ = ⟨q, z_j⟩ ≥ 0` for `j ≠ i` by (a) and (b)). Invariance and `SEP ⊆ K_Z` ✓. *Note:* X's Lemma SD2
reaches the same conclusion without hypothesis (b), by applying the projection lemma one defect at a time
(orthogonality keeps the other pairings unchanged); for `Z_F` and `{F, cnot F}` (b) holds anyway, so the two
proofs are independent routes to the same cones.

**PL reduces to pure states — CONFIRMED.** `Q3 ∩ {⟨·, z⟩ ≤ 0}` is closed, convex and pointed with a compact
trace-one base, hence generated by its extreme rays; an extreme ray strictly inside the half-space is extreme in
`Q3` (the perturbation `(1 ± ε)r₁ + (1 ∓ ε)r₂` stays in the open half-space and in `Q3`), so it is a pure state;
rays on the boundary hyperplane are fixed by `Π`; `Π` is linear. ✓ (My own route to the same reduction, through the
face dimension bound `r² ≤ 2` of Pataki, gives rank one directly; both are valid.)

**PL for pure cap states — CONFIRMED over the exact identities.** For `z = E0`: `B = 3n₁ + n₂ + n₃ − n_g`,
`ρ(Π P_ψ) = ψψ† − (B/3)ρ(E0)`, principal `(e₁,e₂,e₃)` block `cc† + k·diag(3,1,1)` with `k = −B/12 > 0` in the cap,
and the symbolic determinant `−B³(11n_g − n₁ − 11(n₂+n₃))/6912` with `11n_g − n₁ − 11(n₂+n₃) = −11B + 32n₁ > 0`
for `B < 0`; a positive-definite principal block and a positive determinant give positive definiteness (Schur
complement) ✓. For `z ∈ Z_F`: `ρ(Π P_ψ) = ψψ† + (B′/4)(I − 2ff†)`, principal block `cc† + (B′/4)I`, determinant
`3B′⁴/256` ✓. The independent check re-establishes the surgery on rank-one batteries for `E0` and `F` by a different
method (the 2×2 determinant identity on `span(f₁, g)`, H3a–d), with the countercontrol `e_{3/2}` failing.

**Theorem E — CONFIRMED.** Each hypothesis of Theorem S is matched to an exact certificate; `≠ Q3` by the
witness pairs; level (ii) for `K_F` by the group computation (H2b–d of the independent check reproduce the
order-16 group `⟨cnot, Ad(Z⊗I), Ad(I⊗Z), T⟩` from the 4096 dressings and its permutation of the orbit).

**U2(b) local Wigner theorem — CONFIRMED.** Steps 1–7 re-derived: qubit Wigner through the Bloch dictionary
(images of `e_i` orthonormal, so the ray map is the restriction of some `O ∈ O(3)`; rotations are `Ad(SU(2))`,
`reflY` is complex conjugation) ✓; slices (`ψ_ab′ ∈ H_a`, `H_a ⊥ H_a⊥`) ✓; normal form with `U₀|xy⟩ = ψ_xy`, slice maps
diagonal because they fix the basis rays ✓; the cross ratio `κ` depends on `b` only and on `a` only, hence is
constant, and `|κ| = 1` because the `D_x` are diagonal unitaries, so `diag(1,1,1,κ̄)` makes `c₀₀c₁₁ = c₀₁c₁₀` and
forces `ε₀ = ε₁` ✓; Segre step via the determinant identity [X W5] ✓; the factors are (anti)unitary by step 1 ✓;
non-generic pairs follow by continuity (a transition-probability-preserving ray map is a Fubini–Study isometry).
The countercontrol W6c shows the all-pairs hypothesis is load-bearing ✓. This is a second, independent proof of
the step S3 left [L]; X proves it through Jordan maps and a Clifford triple (AUDIT-X).

**U2(c) orthogonal images — CONFIRMED** (rests on ORTH.W, audited; the 36 axis products span `W 3` [X O1]).
**U2(a) linear images — CONFIRMED WITH NOTE**: correct given the [L] classification of `Aut(PSD₄)`; U's labelling
([W + X + L]) is right.

**U3, U4 — CONFIRMED.** `K★ ∩ V+` is self-dual in `V+` and contains `E0 ∉ PSD(3) ⊕ ℝ₊` ✓. `K_F2 ∩ V+ = Q3 ∩ V+`:
`⊆` from `P+q ∈ Q3` and `P+F ⪰ 0` (spectrum `{0, 1/8}`; independent check W5), `⊇` as written ✓; the `V−` fibre
computation (eigenvalues `(1 − xy − s(x + y))/16`) ✓. So even an exactly quantum `V+` part does not force `K = Q3`.

**§1.6 non-orthogonal orbits "route refuted"** — instance-verified at `a = 3/2` [X u5_kf CC]; the general-`a`
argument is [W] in the record and was not re-derived here; it is not load-bearing for any label.

**Downstream (§0, uniform `K★` breaks IE1 and hence FCC)** — the IE1 failure is exact (H2e); the FCC step via the
contrapositive of `kt4_general_ie1` is [D] as labelled, and X's x8 computes the FCC violation directly
(independent check W2). Consistent.

## Corrections (wording; no label changes)
1. §0 table, row "linear images of `Q3`": the evidence column says `[W + X + L]`; the text of §1.3(a) carries the
   [L] dependency only in the square-root step. Correct as labelled; the integration note states the dependency.
2. §1.6 "`K_F` is moreover invariant under every orientation-even signed-diagonal local (all 32) [W only]": X
   verified this exactly (its order-64 group `Gbig` permutes `{T_s}`, x3 C5), so the claim is [W + X] across the two
   threads.
3. The three cones are X's `K1`, `K4` and `K({F, cnot F})`; the integration note uses one name per cone.

## Verdict for integration
EXOTIC at level (i) (`K★`, `K_F2`, `K_F`) and at level (ii) (`K_F`), by Theorem S over exact certificates; the
class rows as labelled; the local Wigner theorem proved (two independent proofs across U and X); the sharpest
necessary conditions (`K ⊆ K_E ∩ Q_g`, `Y1 ∉ K`, the cap exclusions) exact; `V+`-uniqueness fails and `V+`-quantum does
not suffice. The route "pair self-duality with the pair hypotheses ⇒ Q3 / IE1 / FCC" is refuted. The independent
check (25/25, run 4, replay identical) confirms every exact ingredient Theorem E cites. **Audit verdict: U's EXOTIC
stands as stated, at levels (i) and (ii); UNIQUE is false at both.**
