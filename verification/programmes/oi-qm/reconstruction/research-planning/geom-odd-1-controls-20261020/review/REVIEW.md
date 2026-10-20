# Review: GEOM-ODD-1 design note (PR #830), failed control searches

I reviewed `scratchpad/a830/DESIGN-NOTE.md`, its scripts and outputs, adversarially and independently. I did not write any of it.
Objects: PR head `f8e75086`, D `dee3b5ae`, revised prereg `8a4587c9`, preflight `e8ac54b5`, wrapper `cf9ddc11`, run `39192591924`.
All my work is in `scratchpad/rev830/`: scripts in `scripts/`, outputs in `out/`, `slp/`, `omegah/` and `cand/`. I used the
venv's numpy 2.4.6 and scipy 1.17.1. I made no repo edits, no GitHub writes and no dispatches.

## Verdict: **CONFIRMED WITH CORRECTIONS**

Every load-bearing measurement I re-ran reproduces: F1, F2's start 0, the exact vertex and Stiemke certificate, the
verifier's PASS and sha256s, and F3's violation counts. The proposed decision rule P0–P4 is neither vacuous nor circular.
Three groups of corrections block posting the note as the design checkpoint, or using it for the owner's open questions:

- B1: the SLP "new gate" is a local relabelling of `cnot`.
- B2: F3's throughput diagnosis rests on a contention-inflated timing and an invalid lower bound.
- B3: several claims are stronger than their evidence.

None of them voids a verdict, because the note renders none.

***

## Blocking findings

### B1. The SLP candidate is `cnot` relabelled by local ball automorphisms, not a new gate (§2.2, §2.3 item 4, §5 Q5, N1.1)

`scripts/x2_equiv.py` uses exact integer arithmetic. Its output is in `out/x2.out`:

```
R^-1 G diagonal: True signs [[1,-1,-1,1],[-1,1,-1,1],[-1,1,-1,1],[1,-1,-1,1]]
decompositions G = (A(x)B) R (C(x)D) with local signed permutations: 128
 first: A = 1, B = diag(1,1,-1), C = diag(-1,-1,1), D = -1_3
 of which pure conjugations: 0
 local maps of first hit: z-line kept / commute with N: all (True, True)
sign twists R o diag(s) in F passing posFwd and posInv exactly on pools A u B: 32
 candidate among them: True
 of these, local relabellings (A(x)B) R (C(x)D) of R: 32
```

So `G = (1 ⊗ diag(1,1,−1)) · R · (Zπ ⊗ (−1₃))`. Each local factor is an orthogonal automorphism of the ball that keeps the
`z` line and commutes with `N = nflip = diag(1,−1,−1)`. The "non-product sign pattern" comes from moving local maps through `R`.
It does not show a new gate.

Consequences:
- **§2.2 wording.** "`G ≠ R`, `G ≠ R∘(Zπ⊗1)`, `G² ≠ 1`" is true but implies novelty. The note should state the decomposition.
- **§2.3 item 4 and open question 5 rest on a false premise.** The involutive ansatz excludes this representative, but not
  its class: the class contains the involution `R`. §2.2 gives no evidence that the ansatz loses a gate class.
- **The float diagnostic is no longer needed.** Whole-body `posFwd` and `posInv` of the candidate follow exactly from
  `R`'s, since `(e⊗f)((A⊗B)R(C⊗D)(x⊗y)) = (Aᵀe ⊗ Bᵀf)(R(Cx ⊗ Dy))`. The off-pool float diagnostic (`a13`) should give way to
  that exact argument.
- **The target is a finite set, not one point.** "Its target is an isolated point" (F2) should read: on pools A ∪ B the
  verifier accepts at least 32 isolated points of the form `R∘diag(s)`, all local relabellings of `cnot`. Recovery probabilities
  such as SLP's 1 in 5 are hit rates against that orbit.
- **The favourable branch missed the obvious test.** N1.1 was the branch due maximum skepticism (§A.31). "Is the hit
  trivially equivalent to the reference?" is the obvious pressure test of it, and it was not run.

This does not change the meaning of the search: the prereg defines recovery as acceptance by the verifier, and a
relabelled `cnot` is accepted. It does change how the repair evidence reads. SLP recovered `cnot` up to local relabelling
in 1 of 5 starts. It did not find a second gate.

Positive side-check (`out/x4.out`): every one of the 32 orbit members has the same commutation counts as `R` against
`g⊗1`, `1⊗g` and `g⊗g`. So §2.3 item 5's claim, that the full-stabiliser ansatz excludes `cnot`, holds for the whole class,
not only for `R`.

### B2. F3's throughput diagnosis: the row-construction timing does not reproduce, and the 29-round bound is invalid

I re-ran `a6_omegah_vertex.py` on the frozen code, 300 s budget, on this host at load about 1.5 (`omegah/run.out`). Its
pool is byte-identical to the author's (sha256 `a5b5c8d5…`).

```
initial cuts 3000 built in 0.4 s
LP 0: 44.1 s, rows 4500, min value -5.630e+00, violated 43305, ..., separation 8.5 s
LP 1: 68.2 s, rows 6000, min value -4.574e+00, violated 16770, ..., separation 0.1 s
LP 2: 101.6 s, rows 7500, min value -2.138e+00, violated 16472, ..., separation 0.2 s
LP 3: no solution within budget (76.9 s)
```

- The violation counts 43 305 and 16 770 replay exactly. That part of F3 is confirmed.
- **"Building the initial 3000 cut rows takes 74 s" does not reproduce: it takes 0.4 s.** Separation takes 8.5 s here,
  against 50.4 s in the note. The note's own environment line says the host was at load 9–10 with 4 cores, so the 74 s
  measured contention. It did not measure the code. F3 names unvectorised row construction as a root cause, and §2.3
  item 1 ranks vectorising it first. Both rest on that timing. The cost is the LPs, which grow from 44 to 68 to 102 s.
- **"LP 0 takes 72 s on 4500 rows; LP 1 takes 135 s on 6000 rows" misreads the script.** `a6` prints `len(cuts.C)` after
  separation. LP 0 was solved on 3000 rows and LP 1 on 4500.
- **"At the measured rates a single vertex needs at least about 29 rounds" is not a lower bound.** 43 305 / 1500 ≈ 29
  assumes every violated row must be added. The note's own data refutes that: round 1 added 1500 rows and removed 26 535
  violations. My LP 2 shows a plateau instead (16 770 → 16 472), which points to slow convergence, but no bound follows.
  §3.5's "over an hour" is labelled speculative and inherits this. Restate it as an LP-time trajectory, measured on an
  unloaded host.
- CI arithmetic: `13 500 = 3000 + 7 × 1500` is right (log of job 117868433431: `rounds 0, best residual inf, cuts 13500,
  944 s`). It shows at least 7 separation calls, and exactly 7 if each added the full 1500. "No pool-feasible vertex for
  `G`" cannot be read from the CI log. The cut set is shared, so the `H` vertex could have been in progress. The replay
  makes the reading plausible but does not establish it.

### B3. Claims stronger than their evidence (Code Review Rules: finite test → universal; float → exact; first-order → isolation)

1. **F2 heading and conclusion overstate.** "The alternating L1 coupling cannot converge to the control's gate" and "its
   target is an isolated point that the method cannot converge to" rest on 9 local basin trials and 36 CI starts. Say
   "did not converge in any tested start". The step from isolation to stalling is not shown: SLP converges to the same
   isolated points. Isolation is a property of the target and the stall is a property of block-coordinate descent; the
   note links them causally without a test. N1's "cannot converge to it from any tested start" should read "did not".
2. **N2 says Ω_h's target is "on a face of the relaxation, not isolated".** Only `rank_ℚ ≥ 768` is exact (from the
   modular rank), which gives a face of dimension ≤ 192. `rank_ℚ ≤ 768`, and hence non-isolation even in `P_A`, is a float
   measurement. F3 labels this correctly; the N2 row drops the label. For the coupled relaxation `K`, a 192-dimensional
   first-order-flat space does not give non-isolation: second-order `H` terms can still cut every direction. To settle it
   exactly: find a mod-p nullspace of the tight rows, rational-reconstruct it, and check it on all 57 456 rows in integer
   arithmetic. Then either exhibit a curve in `K` or state "first-order flat".
3. **N4, "`HIT` reachable only for gates rational in `F`", is too general.** The argument (no slack, so a rounded point
   fails VP) holds for gates isolated in `K_A`. A positive-dimensional face can contain rational gates near an irrational
   one. `exactify` also limits denominators to `2²⁰`. Correct scope: a returned candidate is always rational, and an
   irrational gate isolated in `K_A` yields no `HIT` near it. The §3.6 wording ("cannot be returned as a HIT") is fine.

***

## Independent verifications (commands and outputs)

### Pins
- `git archive e8ac54b5 …` gives `controls_verify.py` `e6f3fcbc…0763`, `controls_gen.py` `df7e640c…b855` and
  `run_control.py` `3faa0fdf…06b9`. These equal the pins at `8a4587c9`, preregistration lines 116–120.
- `CompositeDimension.lean` is blob `377f0b25` at `424aa33b`, `dee3b5ae` and `e8ac54b5`.
- E20 `run2.py` is blob `34485203` at `424aa33b`, sha256 `ec95a697…93c3`.

### F1: confirmed
- Command: `cd rev830/e20/research/equivalence/experiments && venv/python -I -B e20_odd_bodies.run2.py` (2 min 31 s).
- Stdout is identical to the recorded `e20_odd_bodies.run2.out`, 20 lines each. The recorded file has no comment lines.
  It reads `FAIL C4 -- eball 3: UNDECIDED(iterations) (18639 constraints)` and `VERDICT NOT RENDERED -- failing: ['C4']`;
  exit code 1 is the harness's own.
- The 40-round cap is confirmed: `lp_relaxation(body, max_iter=40, …)` (run2.py:705) sets
  `status = 'UNDECIDED(iterations)'`.
- "posFwd only" is read from the harness docstring (line 4), not independently tested.

### F2: confirmed with the frozen generator itself, which is stronger than the author's re-implementation
- I emitted the pool with the frozen verifier: `pool-eball3.json` sha256 `e1e04e70…`, byte-identical to the author's.
- I ran `controls_gen.py pool out 150` unmodified (`out/` console, 2 min 26 s):
  `start 0: rounds 26, best residual 0.020604249432947475, cuts 8867`. Starts 1–3 also match the CI log lines exactly
  (`0.9622796916655078/9507`, `0.9418638113617409/10205`, `0.9864502287807035/8822`). Start 4 was truncated by my deadline.
- The CI summary is confirmed: 36 starts, best residual `0.006731313064325839` (start 25), and the generator stopped at its
  deadline at 937 s.

### Exact vertex and Stiemke certificate: confirmed by my own code (`scripts/x1_exact.py`, `out/x1.out`)
- I built `F₀` from the matrix identities relT, relC and the homogeneous frame, not from the generator's free pattern:
  dim 48. Its span equals the generator's `build_F` span (rank of the union is 48), and `G0 − R ∈ F₀`.
- `R² = 1` exactly. In int64 on positive rescalings, which is exact, the pool A values of `R` are: min 0, 0 negatives, and
  exactly 200 zeros out of 331 776.
- The exact rank over ℚ (Fraction elimination) of the 200 `G`-tight rows is **48 = dim F**, so `R` is a vertex of `P_A`.
  The rank of the 400 `G`+`H` rows (`H`-side rows `L_q(−RδR)`) is 48, and `R F₀ R ⊆ F₀`.
- **Exact Stiemke certificate.** Rational `y` with `Σ yᵢ rowᵢ = 0` exactly and every `yᵢ > 0`: min 0.4747 when
  normalised to `Σy = 400`; the vector is in `out/stiemke-y.json`, sha256 `ed80ac21…`. The author's "min 0.177" is the same
  fact under an unstated normalisation; state it.
- **Countercontrol** (`x1b_gonly.py`, `out/x1b.out`, float LP). The `G`-side rows alone admit no positive certificate (LP
  infeasible) and do admit a direction with all rows ≥ 0, as at a vertex. The same holds for the `H` side alone. So
  isolation needs the coupling, and the certificate is not vacuous.
- **The argument is valid for the generator's relaxation.** The frozen code defines
  `K = {G ∈ F : G and G⁻¹ posFwd on pool A}` (box 8; `H` sought in `F`, which is closed under inversion). Stiemke plus full
  rank gives `φ(u) = minᵢ cᵢ·u < 0` on the unit sphere, so `φ ≤ −κ`. `G`-side values are exactly linear and `H`-side values
  are linear plus `O(t²)` uniformly. So for small `t > 0` some tight value is at most `−κt + Ct² < 0`. Hence `R` is isolated
  in `K`, and therefore in the A ∪ B version. This is a written argument, as the note says.

### Exact verifier on the PASS candidate: confirmed
- I reproduced the candidate by replaying `A10_ONLY=3 a10_slp.py … random 1 120` (`slp/run.out`, 2 min): residual
  `1.304e-12`. The output is **byte-identical** to the author's `slp-candidate-eball3-s3.json`, sha256 `5dc9fa9b…b393`.
- Random mode reads `lamR` only for printing. The update never uses `R`.
- The frozen verifier (sha256 equals the pin) gives `--verify eball3 …`: `verdict PASS`, `VP posFwd_negative 0`,
  `posInv_negative 0`, pools A and B of `[24, 24]` each, `equals_reference false`. The report is byte-identical to the
  author's, sha256 `80a367f8…ba1f`.
- So "PASS on pools A and B" means what the note says: exact pool-relative VS, VE, VL, VI and VP. B1 identifies what the
  candidate is.

### Verifier self-test (P0): confirmed
- `controls_verify.py --self-test` prints `self-test: OK` for both bodies (55 s, `out/selftest.out`).

### §1 precision note on comment 6255285218: confirmed, and provable
- `R∘(Rθ⊗1) ∈ F` iff `Rθ` commutes with `1⊕nflip = diag(1,1,−1,−1)`, since `CRC = TR` and `Rθ⊗1` commutes with `T`. That
  holds iff `sin θ = 0`. So "π only" (besides the identity) is a two-line exact fact. State that argument; the single
  counter-angle `3/5` is a witness, not a proof.

***

## Decision rule P0–P4 (checked for vacuity and circularity)

- **P0 and P1** are well-formed. P1 has real bite: the author's `a10_slp.py` reads `lam-eball3.json`, a reference table,
  so a repaired generator derived from it must drop that read or P1 voids the run.
- **P2** accepts any verified candidate, which matches the prereg's definition of recovery. Two notes:
  - On `eball3`, acceptance covers the 32-member local orbit (B1).
  - On Ω_h, a PASS can land on a pool-blind non-gate of the ≤ 192-dimensional face. This is consistent with a pool-relative
    `HIT`, but the claim that P2 calibrates the face regime should carry open question 7.
- **P3** is non-circular: it voids nothing and only withholds credit from the repair. The run from CI `39192591924` already
  is XP1 at cap 1200.
- **P4, the `eball 7` countercontrol, is not trivially vacuous.** With the family's pair, the frame is consistent and
  dim F = 960, the same as Ω_h (`out/x3.out`). Kernel `ne_seven_of_nativeGate` (CompositeDimension.lean:2741) excludes
  whole-body gates. The countercontrol is asymmetric: an accepted candidate is decisive and voids `HIT`, while "no
  candidate" is weak because the generator is local. Gating on P2(Ω_h) PASS, which shows capability at D = 7, is the right
  mitigation. Add a checkpoint that the `eball 7` run reached the same stage, with pool-feasible vertices and a residual
  trajectory recorded, so that a throughput stall is not read as pool discrimination (§A.41).
- **Design-overfitting (note).** SLP was chosen after observing it on the `eball3` control. A later P2 PASS on `eball3`
  is therefore not held-out calibration. Prefer crediting the held-out family-parametrised control `Ω_R(1,1;2)` from open
  question 2, or record that `eball3` informed the design.

## Other notes (non-blocking)

- **The basin comparison is not like-for-like.** The alternation was tested with `G = R` and only `H` perturbed. SLP was
  tested with both perturbed. Both setups are non-trivial for their method, because the alternation's first step re-solves
  `G`. Still, "where the alternation stalls in 9 of 9" compares different starts.
- **Register.** The design note is not `papers/` prose, so §A.32 and §A.33 do not bind it. I found no caps emphasis
  outside verdict tokens. "S0-b's tolerance diagnosis was withdrawn there" is history narration, acceptable in a design note.
- **Gem-finding (§A.31).** The note itself says the fixed point is not reached. B1 is a NEW finding on the N1.1 branch.
  Add it as an assumption-watch marker: "is the hit equivalent to the reference under the body's local automorphisms?",
  checked before reading any control or search hit as new.

## Verified independently vs only read

**Independently verified (re-run or own code):**
- pins and sha256s;
- F1 replay and the 40-round cap;
- F2 starts 0–3 with the frozen generator, and the CI summary;
- dim F, R²=1, the tight set, exact rank 48, and the exact Stiemke certificate, plus its countercontrol and the isolation
  argument;
- SLP start 3 reproduction, the candidate sha256, the frozen verifier's PASS and the report sha256;
- the candidate's identity as a local relabelling, and the 32-gate orbit;
- the symmetry claim over the orbit;
- the self-test;
- F3 violation counts and timings (contradicting the 74 s and the "on 4500 rows" reading);
- F3 CI arithmetic;
- `eball 7` dim F;
- the π-rotation claim (by argument).

**Only read (not re-run):**
- Ω_h modular rank 768 and float ranks 768/776/784 (`a8`, `a9`);
- the random-vertex distances (F2 item 5);
- the alternation basin runs (`a2-basin`);
- SLP basin runs and starts 0, 1, 2 and 4;
- `a7`;
- E20's posFwd-only relaxation beyond the docstring;
- LOG.md, which is not in the material.

***

## Re-review of the corrected note (DESIGN-NOTE.md `26eed555…091e`)

Inputs checked:

| file | sha256 |
| --- | --- |
| `DESIGN-NOTE.original.md` | `9b5ffea6…af15` |
| `CORRECTIONS.md` | `47d90d4d…966b` |
| `a14_orbit.py` | `2ee802c8…5639` |
| `a15_members.py` | `a616b7e6…55e1` |
| `a3_rigidity.py` | `8b12dc02…0b40d2df` |

`DESIGN-NOTE.original.md` matches the note I reviewed: 284 lines, and it contains the text I cited ("74 s", "29 rounds",
"cannot converge"). New reviewer outputs are in `rev830/rr/` and `rev830/out/x5.out` and `rev830/out/x6.out`.

### Verdict: **CONFIRMED WITH CORRECTIONS** (one wording overclaim left; everything else closed)

**R1, remaining correction (claim stronger than evidence; the diff introduced it).**
- Line 54 reads "**What the target is.** The verifier accepts a finite set of 32 points of this form, all one class", and
  N1's verdict reads "the `eball3` target is a set of 32 points isolated in …". Both state that the whole accepted set
  of `F` is these 32 points.
- What was enumerated is narrower:
  - the 4096 sign twists `R∘diag(s)` in `F` (a14: exactly 32 pass);
  - the Γ-class, and in my `x6_class48.py` the larger class under all 16 local signed permutations that keep the z3 line
    (also 32 members in `F`, `out/x6.out`).
- Nothing excludes accepted points of `F` that are not sign twists. That includes non-permutation matrices, and members
  of other classes.
- Fix: "Among the 4096 sign twists in `F`, the verifier accepts exactly 32, which form one local-relabelling class.
  Whether other points of `F` are accepted is not determined."
- Correspondingly, "the hit rate is a rate against the 32-point class" should read "against at least that class". N1.2's
  wording ("class of 32; no other sign twist passes") is already correctly scoped.

### (1) B1: closed, except R1
- **Novelty wording is gone.** A grep for `non-product`, `G ≠ R`, `G² ≠ 1`, `new gate`, `second gate` finds nothing. The
  remaining "distinct from" hits (§3.3 row; N1.2) are the test and the marker.
- **The decomposition, the 32-member class, the 4096/4064 split and "8 involutions incl. R" are confirmed:**
  - a14 re-run (`rr/a14.out`, 9 min 58 s) matches the recorded `work/a14-orbit.out` byte for byte. The recorded file
    also carries the shell `time` lines, which my capture does not, so its sha256 differs. Recorded files should hold
    deterministic output only.
  - `R ∈` class holds trivially (A=B=C=D=1). R is an involution, so it is among the 8.
- **a15 reproduces:**
  - a15 regenerated the 32 member files in `rr/orbit/`; their sha256 lists are identical to `work/orbit/`.
  - I re-ran the §6 loop, `A3_REF=… A3_STIEMKE=1 a3_rigidity.py`, for all 32 members (`rr/a15-raw.out`).
  - Filtered by `^## |^== |exact tightness|rank mod 2147483647|exact Stiemke|^LP status`, it is **byte-identical** to
    `work/a15-orbit-isolation.out` (sha256 `4ed4183b…a4d`). The recorded file is a filtered log of that loop: the raw
    loop also prints the float lines and a second prime. §6 should state the filter.
  - Raw output: all 32 members have rank 48 modulo both primes, all 32 Stiemke certificates have every `yᵢ > 0`, and
    every single-row LP gives 0. Tight counts are 122–217 per side; min `yᵢ` is 0.096–0.383. Both match the note.
- **a15 does test isolation in `K_A`.** With `A3_REF`, the script:
  - evaluates the `G`-tight set at the member `M`;
  - evaluates the `H`-tight set at `M⁻¹`;
  - builds the exact `H` rows as `−(efᵀM⁻¹) δ (M⁻¹w)` (`exrow` with `M = Ri`);
  - confirms every selected quadruple exactly tight before using it;
  - computes the rank modulo p of the integer-rescaled exact rows (`rank_p = 48` forces `rank_ℚ = 48`);
  - builds an exact Fraction certificate.

  Tight rows are selected in float (`|v| < 1e-12`), but each is confirmed exactly zero, and missing a tight row can only
  weaken the certificate, not falsify it. The isolation argument therefore holds per member.
- **Independent cross-check with my own code** (`scripts/x5_member_exact.py`, the generalisation of `x1_exact.py` to
  non-involutions; `out/x5.out`):
  - SLP candidate, `M² ≠ 1`: 192 + 192 tight, exact rank over ℚ 48, exact Stiemke certificate with all `yᵢ > 0`.
  - member-29, an involution: 200 + 200 tight, rank 48, certificate holds.

### (2) B2: closed
- The root cause is now LP cost.
- The row counts are corrected ("solved on `3000 + 1500k`"), and the table matches both quiet-host replays.
- "29 rounds", "over an hour", and vectorisation as the top repair are gone. The contended figures appear only as "not
  used".
- The `G`/`H` shared-cut-set wording is correct: "the log does not say which vertex step was in progress".
- §3.5 now says no time-to-vertex estimate is supported.

### (3) B3: closed
- "Did not converge to any member of the class in any start tried" is supported: no CI residual is below 6.7·10⁻³.
- The isolation⇒stall causation is removed explicitly.
- Ω_h: only `rank_ℚ ≥ 768` is exact; flatness is float; non-isolation is "not shown" (lines 118–124, §2.3 closing, N2).
- N4 is restricted to gates isolated in `K_A`, with the `2²⁰` cap noted; §3.6 is aligned.

### (4) Notes: applied
- Stiemke normalisations are stated.
- The basin comparison is marked not like-for-like.
- **π rotation.** The two-line argument is correct: `Zθ` rotates homogeneous coordinates 1 and 2, whose `H`-eigenvalues
  are +1 and −1, so it commutes with `H` iff `sin θ = 0`.
- **P4 stage checkpoint** is in §3.1(d), §3.2 and §3.4. A stalled `eball 7` run leaves `HIT` unread.
- **P1's bite** (`lam-eball3.json`) is recorded.
- **Held-out `Ω_R(1,1;2)` control** is in P2 and Q2.
- **Ω_h PASS caveat** and the exact check for Q7 are present.
- **N1.2 marker** is in §3.3 and §3.4.
- **Kernel citation:** `nativeGate_cnot` is at CompositeDimension.lean:1160 at `e8ac54b5`, as cited.

### (5) Diff: no new overclaim except R1
- I read all added lines of `diff DESIGN-NOTE.original.md DESIGN-NOTE.md`.
- R1 is the only strengthening beyond the evidence.
- The header line "This revision incorporates the independent review … (verdict: confirmed with corrections)" should,
  when posted, cite this re-review's verdict for the revised text rather than the first-pass verdict.

### (6) `a3_rigidity.py` edit
- **A literal diff is impossible.** No copy of the pre-edit file (sha256 `2e42a30b…`) exists anywhere on disk; only its
  hash is recorded in CORRECTIONS.md. The only `A3_REF` code is lines 40–41, an override of `R` placed before `Ri`, `Rf`
  and `Rif` are computed.
- **Default behaviour is verified by reproduction.** Run without `A3_REF`:
  - with `A3_STIEMKE=1`, the output is **byte-identical** to `work/a3-eball3-A-stiemke.out`;
  - without it, the output is **byte-identical** to `work/a3-eball3-A.out` (`rr/a3-stiemke-noref.out`, `rr/a3-noref.out`).
- **Recommendation.** Editing a script in place after its outputs were recorded loses the exact recipe. Keep a copy of
  the pre-edit version, or add a new script, next time.

### Commands (re-review)
```sh
R=…/rev830; A=…/a830; P=$R/src/verification/programmes/oi-qm/reconstruction/round-geom-odd-1/preflight
$A/venv/bin/python -I -B $A/scripts/a14_orbit.py $P $A/work/slp-candidate-eball3-s3.json > $R/rr/a14.out
python3 -I -B $A/scripts/a15_members.py $P $R/rr/orbit
for i in 00..31; do echo "## work/orbit/member-$i.json"; A3_REF=$R/rr/orbit/member-$i.json A3_STIEMKE=1 \
  $A/venv/bin/python -I -B $A/scripts/a3_rigidity.py $P $R/rr eball3 A; done > $R/rr/a15-raw.out
grep -E "^## |^== |exact tightness|rank mod 2147483647|exact Stiemke|^LP status" rr/a15-raw.out | cmp - $A/work/a15-orbit-isolation.out
$A/venv/bin/python -I -B scripts/x5_member_exact.py $P /dev/null <member.json>
$A/venv/bin/python -I -B scripts/x6_class48.py $P
env -u A3_REF A3_STIEMKE=1 $A/venv/bin/python -I -B $A/scripts/a3_rigidity.py $P $R/rr eball3 A | cmp - $A/work/a3-eball3-A-stiemke.out
```
