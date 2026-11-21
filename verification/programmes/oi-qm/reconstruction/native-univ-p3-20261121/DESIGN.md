# NATIVE-UNIV, phase 3: candidate tests compared, and the choice

**Standing.** Writer's design record, under `PLAN.md` (committed first, `56a02e25`). It is design
only: nothing is run. Base and notation are as in `PLAN.md`. Cited records:
- `P2N`: NU3–NU7, confirmed in review at `ef25e3bf` on #1499, with the NU8 classification at
  `92cb2350`; not on `main`;
- F1: NU1, NU2, reviewed on #1489, not on `main`;
- MQ: MEAS-Q, on `main`;
- U1 and U2: UNIV-1 and UNIV-2, on `main`.

## 1. The hypotheses the test must separate

For Q at a uniform background `c = 2^15`, with W2 signals on designed axis lines (U1 §3):
- **H1:** some gadget realizes a *controlled transfer*: a signal entering on line A leaves as a
  signal on a non-parallel line B, the line sector is restored, and the transit is *leak-free*: no
  site outside `lines ∪ K_r` ever leaves `c`. That is U2's region, with `R⁺` replaced by `K_r`.
  The closed hull of a bent junction fills an infinite planar sector (§6), so confinement in that
  hull would be a much weaker requirement. It is not used;
- **H0 (for a stated class):** no gadget in the class does.

Why this is the decisive pair: U1 identifies off-line transfer as the missing block that turn,
gate and fan-out all require. NU5 shows that, relative to the allowed region, "bounded breach that
heals" is not a separate route. A test that can return H1 with an exact certificate, or H0 exactly
for a stated class, is decision-relevant in the sense of
[#1169 c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480)
item 6.

## 2. Candidates

| Candidate | What it would decide | Can it separate H0 and H1? | Cost class (§A.40) | Controls |
|---|---|---|---|---|
| (a) Bounded breach: F1 P2, periodic finite orbits with excursions | whether small finite configurations have non-spreading excursions | No. By NU3 and NU5 such an orbit is a transient inside a confined set, not a transfer; at most it supplies a candidate ingredient | CI | P2-K1–K7 (F1 `plans/P2-PREREG.md`) |
| (b) P3 stage S1: spreading of single-site seeds (paper) | whether every excursion of a single-site seed grows without bound | No. A transfer uses infinite lines inside a confined region, so S1 bears on neither hypothesis directly | local, paper | P3-K1–K5 (F1 `plans/P3-PREREG.md`) |
| (c) Controlled interaction in a Q gadget: **PLANAR-TURN** (chosen) | H1 with an exact certificate, or H0 exactly for the narrow class "leak-free planar ternary gadgets of radius ≤ 2 at J1/J2, W2 signal, every no-input period and arrival phase" (PREREG §8) | Yes: an exact positive certificate; an exact negative per gadget (breach); undetermined cases are reported as INCONCLUSIVE | first stage bounded local; full search CI | positive control on Q itself (collinear transfer) and the bent-line oracle; plain-corner, dead-end, linear-rule and signal-away countercontrols; an NU4 consistency check (`PREREG.md` §4) |

## 3. Why (c), in planar form

1. **Ternary is a theorem, not a restriction.** A leak-free run stays in `lines ∪ K_r`, which lies
   inside its planar closed hull `D`. So `D` is never breached, and by NU6(c) every value is in
   `{−1, 0, 1}` (relative to `c`) at every tick. Enumerating ternary gadgets on a planar `K_r`
   therefore covers every leak-free planar junction of that size. It is not a value cut-off like
   U2's `{±1, ±2}`.
2. **Exact outcomes.**
   - A leak is detected exactly at its tick. Only `lines ∪ K_r` and its neighbourhood are
     simulated, and lines are long enough that no line end reaches a checked site (PREREG §3).
   - A turn is certified exactly at a finite tick. The configuration then equals the post-transit
     reference everywhere except a W2 glider on far B, moving away. The future is that
     superposition for all time: by MQ2(a), and U1's induction for the glider on an infinite line.
   - Neither is horizon-limited. Only a case that neither breaches nor certifies by the cap is
     undetermined.
3. **One component suffices.** The search places the gadget in the signal component only. This
   loses no generality for the transfer requirements (U2 A1; F1 NU1).
4. **What U2 already covered.** U2 F1 covered J1 with the 6 in-plane sites of radius 1, values
   `{−2,…,2}`, at one launch phase, to horizon 120. The planar ternary radius-1 J1 class is a
   subset of it. It is rerun here as a replication control, with every launch phase. New coverage:
   - J2, radius 1: 10 sites, all `3^10` ternary values;
   - J1, radius 2: 20 sites. Its quiescent gadgets are enumerated exactly by constraint
     propagation rather than over all `3^20` configurations.

## 4. (N)/(I) and Established / Assumed / Missing

| Item | Label | Status | Established | Assumed (where it enters) | Missing |
|---|---|---|---|---|---|
| The choice of PLANAR-TURN | (N) | design, unreviewed | the comparison in §2 and the reasons in §3 (no measurement) | NU4, NU5, NU6(c) [P2N, confirmed in review, not on `main`]; NU1 [F1, reviewed]; U2 A1, U1 Lemmas 2.1–2.2, the W2 glider (U1 E2, U2 K0) [`main`] | the run (needs separate authorization) |
| A PLANAR-TURN outcome, if run | (N) | not run | — | as above; the W2 lines and gadgets are a designed initial pattern on a uniform background. This is a scope condition, not a claim about native preparation (Goal C, #866) | if H1: gate, fan-out and composition, then an encoding and correctness proof under Definition U (mathematics); native preparation of the pattern (physical mechanism). If H0: the next class (radius, non-planar regions, other signal types) |

## 5. Relation to the Phase-3 inputs

- **No quantum assumptions.** PLANAR-TURN concerns classical signal transfer in Q. It does not
  use or bear on OPRES Theorem C (non-MIO and non-DIO elements), the I3-SOURCE criteria or
  GATE-A D5/D6, and it imports no quantum or operational assumption.
- **R-READ is not assumed either way.** The test reads configuration values of Q only.
- **No BQP claim.** A positive PLANAR-TURN result would be one block toward native Turing
  universality. As the owner states (#1169 c.7066630306), native Turing universality would not
  by itself prove BQP capability.

## 6. Effect on #1499's NU5 (read-only check at `92cb2350`; #1499 not edited)

The review of #1515 (c.7066725317, R1) points out that `cl₂` of a bent junction is infinite. The
check against `P2N` NOTE at `92cb2350`:
- **The theorems stand.** NU4, NU4′, NU5(a) and NU5(b) are stated for any closed `D`, finite or
  infinite, and are unaffected. NU6(c) is also unaffected: the closure of a planar set is planar.
- **The reading "finite junction region" is wrong for bent junctions.** NU5 and §0 item 1 restate
  the decisive question as a transit confined in `D = cl₂(L ∪ R)`, "with `R` finite". `R` is finite,
  but `D` is not a finite neighbourhood of the junction. For J1 it contains the planar quadrant
  `{x ≤ −1, y ≥ 1, z = 0}`, and for any two non-collinear coplanar lines it contains the sector
  between them. "Confined in `D`" therefore allows ternary disturbance throughout that sector, a
  weaker requirement than U2's R3.
- **One sentence is incorrect as stated.** P2N NOTE line 149 reads: "The breach mechanism of U2 D1
  (AW-UNIV-3) is exactly a breach of `∂D` for `D` the junction's closed set." U2 D1's
  inner-corner kick puts a ternary value at `(−1,1,0)`, which lies *inside* the sector `D`. It is a
  leak out of U2's non-closed region `lines ∪ R⁺`, not a breach of `∂D`. Whether that disturbance
  later breaches `D` is not established.
- **Consequence for the decisive question.** "Confined in `cl₂(lines ∪ R)`" is not the right
  criterion for a controlled transfer at a bent junction. The criterion is leak-freeness relative
  to a finite, non-closed allowed region, as U2 used and PLANAR-TURN now uses. NU5 still shows
  that a breach of the closed hull is radiation out of that hull, but that hull is a sector.
- **AW-NU-4 (assumption-watch).** In Q, closure under `cl₂` of a set containing two non-collinear
  lines is infinite. Any statement that uses `cl₂(lines ∪ R)` as a junction region must say so.
- **Flagged for the owner.** Correcting the P2N wording (NOTE §0 item 1, §1 "decisive question,
  restated" and line 149) would be a change to #1499, which stays as reviewed. It is left to a
  separate, authorized correction.
