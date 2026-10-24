# Independent review: "Read-and-reset investigation: an X relay and two construction boundaries"

24 October 2026. Reviewer: independent, skeptical (AGENTS.md "Code Review Rules", §A.31).

**Reviewed:**
- `OI-READ-RESET-INVESTIGATION-2026-10-23.md`, byte-identical to the bundle's `REPORT.md`.
- The author bundle `OI_read_reset_boundary_handoff_v1.zip` (sha256 `15af0674…b7a5`), extracted at `pkg/oi_read_reset_boundary_v1/`. The coordinator supplied it after my independent work was done. §1.4 covers it.

**Prior material used as data:**
- The native-selector bundle's actual T=185 source list. It was dumped earlier by the prior reviewer's `dump_sources.py` to `native-selector-review/mine/t185_sources.json`, and I read it here as JSON.
- The 12-state calibration in `SELECTOR-RECORD.md`.
- `NEXT-TARGET-READ-RESET.md`.

**Repository and GitHub:** untouched. All work is under `scratchpad/read-reset-review/`. Reviewer code is in `mine/`, replay output in `run/`, mutants in `mut/`, and the dependency extraction in `dep/`.

## Verdicts

| Result | Verdict |
|---|---|
| §2 mask-reset bound (2/5; 9/10 under validity) | **HOLDS.** It is exact and correctly scoped to endpoint XOR with input-independent masks. One scope elaboration is recommended (SF1). |
| §3 X relay (with the §4 record statements) | **HOLDS WITH CORRECTIONS.** The mathematics and the actual-geometry claims all reproduce. The corrections are to wording: the §4 shared-pad claim (SF3), the reading of the register diagnostic (SF4), and verdict lines in the checker that are not computed (SF5). |
| §5 shell collapse | **HOLDS.** The derivation is exact, and it is correctly scoped as a sufficient condition of one method, not a no-go. Its *significance* rests on an unstated resource assumption (SF2). |
| §6 joint countercontrol | **HOLDS.** 1/2 conditional, 5/16 unconditioned, with normalization exact and discrimination confirmed. |

No must-fix error was found.

The report's own verdict, PARTIAL with no read-and-reset instrument constructed, is accurate. Under §A.23 everything here is consistency-axis work and moves no correctness band.

## 1. What was run

All scripts are reviewer code: Python 3.13.16, `python3 -I -B`, run from the review directory.

| Script | Content | Runtime |
|---|---|---|
| `mine/exactlp.py` | Exact Fraction two-phase simplex. `certify()` also solves the explicitly built dual and checks primal feasibility, dual feasibility and equal objectives exactly. | — |
| `mine/masks.py` → `masks.out` | §2 bound by exact LP; menu witnesses; validity restriction; random-permutation extension; §4 key and pad controls; §6 countercontrol | 10 s |
| `mine/relay_geom.py` → `relay_geom.out` | §3 coefficients with exact integers; actual 1,479-entry geometry at the 543-digit P; §4 frontier distances for all indices; readiness-bound identity; §5 shell enumeration | 2 s |
| `mine/relay_sim.py` → `relay_sim.out` | Full 3-D periodic dynamics of the relay, with countercontrols and a witness | 3 min 46 s |

`relay_sim.py`'s `Lat` stepper is **adapted from the prior native-selector reviewer's simulator** (`native-selector-review/mine/sim.py`), which is reviewer code, not author code. It is re-validated here against a naive per-site loop. The relay geometry, the tests and the countercontrols are new.

### 1.1 §2 mask bound (`masks.out`)

- **A1.** The target post-X+ law has plane (00,10,11,01) = (1/2, 2/5, 1/10, 0) with independent fair z. It equals the earlier native success family (U uniform on 0..9, z fair).
- **A2.**
  - TV(μ, τ_YR μ) = 4/5.
  - The uniform output has TV 2/5 and puts 1/4 on the forbidden plane 01.
- **A3.** The triangle bound is an exact linear certificate. With A = planes {00,10}, the sum (μ(A) − Q_000(A)) + (μ(A) − Q_110(A)) is identically 4/5 for *every* mask law ν: every ν coefficient is −1. The report's triangle-inequality argument is therefore correct.
- **L1.** The exact LP over *all* laws ν on (y,r,z), with arbitrary bias and correlation, against the 6 X+ hidden states has a dual-certified minimax of **2/5**. The uniform ν attains it. The optimum is not unique: the solver returned a non-uniform optimal ν.
- **L2.** The two inputs {000, 110} alone already force 2/5.
- **L3.** The menu witnesses check out:
  - Y+ | X+ has plane 00, fair z, and Pr 1/2.
  - R− | X+ has plane 11, fair z, and Pr 1/10.
  - These two are τ_YR translates.
  - The LP minimax over all seven menu preparations conditioned on X+ is **2/5**. X− has read probability 0.
- **L4.** Validity restriction:
  - The masks that preserve the X+ hemisphere are exactly {identity, Z flip}.
  - Over all of F₂⁴, the support-preserving translations are {0, Z, XYR, XYR+Z}; the last two flip X, so the "keeps X fixed" scope excludes them.
  - The dual-certified minimax is **9/10**, attained by a fair Z flip.
- **E1–E3 (elaboration, SF1).** Input-independent random **permutations** of the 8 triples are all doubly stochastic maps (Birkhoff), with XOR masks as a subset. Their certified minimax is:
  - **7/30** over the 6 hidden inputs;
  - **7/30** when every X+ input must stay valid;
  - **7/30** against the menu-conditional inputs.

  The column-capacity argument gives the matching lower bound of 7/30. A non-reversible map (discard and resample) reaches 0 trivially.

### 1.2 §3–§5 exact geometry and algebra (`relay_geom.out`)

- **R1.** For all 21,300 triples (T,P,d) with T+P+d ≤ 60:
  - α = binom(S+d,S) mod 2 = [S&d=0], by Lucas and by an independent 3-D lattice-path recursion;
  - the side coefficient binom(S+d,T)·binom(P+d,P) = multinom(T,P,d) = α·b mod 2.
- **R2.** At T=185, P=12·840^185:
  - P has 543 digits, v₂(P)=557 and 3|P, so b=1;
  - the d<T with S&d=0 are {2,4,6,64,66,68,70};
  - with 3|d as well they are exactly **{6, 66}**.
- **R3.** The origin source has field echo_field(185) = B. Every control H^(1−S)(ℓ,0,0) also starts in field B, because 3|P. H^d fixes (0,0,x) for d ∈ {6,66}. The mask terms α(x⊕ℓ_X) ⊕ αb(ℓ_Y⊕ℓ_R) = αx cancel exactly for every bit pattern.
- **G1.** For the actual 1,479 entries, both signs and every d = 1..184 at the exact P:
  - the only entry at distance ≤ R is the origin input `((0,0,0), field 1, 'input')`, and it sits at exactly R;
  - C_X, C_Y and C_R are exactly on the boundary, and C_Z is outside;
  - the origin's previous-slice fields are at distance R, outside the (R−1) previous ball;
  - the minimum margin of any non-input source is 2;
  - at d = 185, 186 and 187, Y- and R-owned entries reach the boundary. This confirms the report's d<T limit.
- **G2.** Section 4 frontier families against both new ports, for all d<T. Every distance minus R is (index) + offset, with slope +1 in the index, so the statement holds for *all* indices. The minimum offsets are:

  | Frontier | Minimum offset |
  |---|---|
  | M_j | 1 |
  | N_j (H) | 1298 |
  | F_X,k / F_Y,k / F_R,k | 1 |
  | F_Z,k | 556 |

  For the H frontier against q₋ the margin is 9T + j − 2d, so d<T is sufficient but not necessary; d ≤ 4T would do.
- **G3.** |B_r| = (4r³+6r²+8r+3)/3 (enumerated for r<30). The report's bound 16[(S+d)³−S³]+32d is *exactly* 2 ports × 3 fields × [(|B_R|−|B_S|)+(|B_{R−1}|−|B_{S−1}|)], which uses B_S(q) ⊂ B_R(q±). It is a valid over-count.
- **S1.** In 1,024 geometries (1≤T≤8, 0≤P≤7, 1≤d≤8, both signs; these include d ≥ T), the 2R-admissible shell set is exactly {(0,S,±(S+2d))}.

  As a countercontrol, dropping the origin, C_Y or C_R as an old source enlarges the set to 8 points. Dropping C_X leaves 1 point, so C_X is not needed for uniqueness in that instance.
- **S2.** At the actual T=185, d ∈ {6,66}, the in-cone set is exactly {input}, and the unique point is ≥2R from it and from C_Z.

  For q₋, the reflected point (0,S,−S−2d) lies within 2R of the actual H-owned entries and the N_j frontier. These are outside the radius-R cone, so by finite speed they are irrelevant to (q₋,R). This is consistent with the report, but see SF2 on public-record effects.

### 1.3 Full dynamics (`relay_sim.out`)

**S0:** the stepper equals a naive site loop on a dense 5×6×7 torus.

**Mirror.** It reproduces the actual parity conditions with:
- an origin X source H^(1−T)(x,0,0) in the echo field;
- selector controls at C_i = Q_i + S e_y, with setting X, fair m_Y,m_R,m_Z and the X compensation;
- lower Y/R/Z single pulses at (±T,−T,0) and (4T,−T,0), each exactly S from its own port and 2S from every control;
- a lane-varying random previous-slice triple at the origin;
- a dense exterior outside the old radius-S/(S−1) balls and the new radius-R/(R−1) balls, both lane-constant and lane-varying.

There are 512 lanes, exhaustive over (x, c_Y, c_R, c_Z, m_Y, m_R, m_Z, p, f). Torus images are checked so that no relevant pair at ≤ 2R+2 is affected by wrap-around.

| (T,P,d) | b | α | 3\|d | Result (both exteriors) |
|---|---|---|---|---|
| (4,24,3): full mirror of the actual b=1, α=1, 3\|d | 1 | 1 | yes | PASS |
| (5,3,3) | 0 | 1 | yes | PASS |
| (8,3,4) | 1 | 1 | no | PASS (H^d rotation) |
| (4,9,2) | 1 | 1 | no | PASS |
| (4,9,1), (4,9,3), (8,3,3) | 1 | 0 | – | PASS (terminal zero) |

Each PASS covers five checks:
1. The selected X port is (0,0,x) at S.
2. Both q± ports are blank in all three fields for every tick before R.
3. The terminal triple equals H^d(0,0,αx).
4. Replacing D at (q,S) by p gives H^d(0,0,αx⊕p⊕x).
5. Replacing D at the *other* wavefront sites (0,S−k,k) moves the port by binom(d,k)·δ, exactly as predicted (SF4).

Countercontrols, each of which must fail and does:
- no readiness enlargement: dense exterior inside the new balls;
- X compensation dropped at b=1;
- a read at R−1 or R+1 disagrees with x on some lanes.

**W (witness for SF2):** one private pulse at the unique admissible shell point (0,S,S+2d), in the same initial phase as the origin source, gives q₊ = H^d(0,0,αx⊕f), with the prefix blank and q₋ unchanged. This holds at (4,24,3) and (5,3,3).

### 1.4 Author bundle (supplied after the independent work)

**Integrity.**
- `sha256sum -c SHA256SUMS`: all 11 entries OK. `REPORT.md` is byte-identical to the reviewed report.
- The embedded `dependencies/OI_native_selector_handoff_v1.zip` has sha256 `c204e6f6…8664`, as stated. It is byte-identical to the archive the prior native-selector review checked (`native-selector-review/in.zip`).
- The zip entries contain no path traversal. I extracted them to `dep/`.
- `relay.py`, `selector.py`, `compiler.py`, `layout.py` and `transport_layout.py` are byte-identical (`cmp`) to the dependency's copies and to the extracted native-selector package.

**Replay.**
- I read `checks.py`, `relay.py` and `selector.py` first. They use only the standard library, write nothing and make no network calls.
- I ran through `mine/run_bundle.py`, which *appends* the bundle directory to `sys.path` and runs from `run/`.

| Mode | Output | Runtime |
|---|---|---|
| `python3 -I -B` | byte-identical to `checks.out` (sha256 `c3a9771d…c30d`) | 71 s |
| `python3 -I -B -O` | byte-identical to `checks.out` | 72 s |

**Mutations of the author checker.** Each was applied to a copy under `mut/`; the bundle itself was not edited.

| # | Mutation | Result |
|---|---|---|
| m1 | relay factor forced to α=1 | killed: "native private relay / full triple", in the T=9 compiled case |
| m2 | X compensation dropped | killed: "actual selected X prefix and deadline" |
| m3 | readiness enlargement removed | killed: "private port premature blank" |
| m4 | C_Y dropped from the shell test | killed: G3 |
| m5 | intervention expectation ignored | killed: "actual-register transfer diagnostic" |
| m7 | relay moved to the x-direction (±d,S,0) | killed: "control cone compatibility" |
| m8 | J1 mutant replaced by the correct product law | killed: the control discriminates |
| m9 | shared pad moved to the Y/R pair at setting Z | killed: TV ≠ 7/30, in fact 1/15 (see SF3) |
| m11 | wrong target plane weights | killed: J0 |
| **m6** | control phase H^(−S) instead of H^(1−S) | **survives** |
| **m10** | the only α=0 simulation case (T=9) removed | **survives** |

m6 survives because origin and control waves coexist only on the line x=0, y=S. There the net control payload ℓ_X ⊕ bℓ_Y ⊕ bℓ_R is zero at every site, so the X relay and the selected X port are insensitive to the control encoding. This is expected, and it means the mask cancellation holds for any common control phase. These checks do not test the unselected ports, and the report does not claim they do.

m10 survives and still prints "N-controls: … bad-delay erased X bit … detected" (SF5).

**What checks.py checks, compared with what REPORT.md says** (all four gaps are covered by my independent checks, which pass):
- (a) G1 checks controls only at distance ≥ R. It does not check that C_X, C_Y and C_R are *on* the boundary or that C_Z is outside, which §3 states as verified. My G1 confirms both.
- (b) The "N-controls" line comes from a constant arithmetic assertion `(12&3)==0 and (12&4)!=0`, not from a measured countercontrol. The α=0 erasure *is* measured inside the compiled T=9 simulation (d=4..8, where 12&d ≠ 0), but the printed "detected" does not depend on it.
- (c) J0 prints "mask-only reset minimax TV exactly 2/5 … 9/10". What it computes is the ingredients: TV(μ,τμ)=4/5 and attainment by the uniform mask and the fair Z flip. The lower bounds rest on the prose proofs. My dual-certified LPs establish them.
- (d) J2's "shared X/R pad TV 7/30" is computed at setting Z, with Z unmasked and X/R sharing one pad. §4 states "A shared unselected pad also gives 7/30" in the setting-X relay context without naming the setting (SF3).

Smaller differences:
- The simulations use lane-constant exteriors only ("SAME environment for every input"), and wrap-around is not separately checked. My lane-varying exteriors and wrap checks cover both.
- G4 samples frontier indices, as the report itself says. My G2 covers all indices.
- J3 is stated as a theorem consequence, not a simulation, and is labelled as such.

## 2. Independent results

| Report claim | My check | Result |
|---|---|---|
| §2 2/5 minimax for input-independent masks (any bias or correlation), attained by the uniform mask | exact certificate A3 + dual-certified LP L1/L2 | CONFIRMED |
| §2 menu witnesses (Y+\|X+: 00, 1/2; R−\|X+: 11, 1/10) | L3; menu-conditional LP = 2/5 | CONFIRMED |
| §2 only identity and Z flip preserve the X hemisphere; 9/10 minimax, attained | L4 enumeration + certified LP | CONFIRMED |
| §2 scope: endpoint XOR only | E1–E3: random permutations reach 7/30, also with validity kept | CONFIRMED; class-specific (SF1) |
| §3 α=[S&d=0]; side coefficient α·b; d ∈ {6,66} | R1, R2 exact integers | CONFIRMED |
| §3 mask cancellation; terminal H^d(0,0,αx) | R3 algebra; 7 full-dynamics cases × 2 exteriors | CONFIRMED |
| §3 actual geometry, both signs, d=1..184 | G1 on 1,479 entries at exact P | CONFIRMED (stronger than the author checker, gap a) |
| §3 d=T limit | G1: Y/R entries reach the boundary at d ≥ 185 | CONFIRMED |
| §3 register-replacement diagnostic | sim: exact; also responds at other blank wavefront sites | CONFIRMED; wording (SF4) |
| §3 α=0, early-read and wrong-deadline countercontrols | sim CC; author T=9 sim | CONFIRMED (author print gap b) |
| §3 ΔJ upper bound | G3 identity | CONFIRMED (exact nested-ball count) |
| §4 frontier exclusion for all indices | G2 symbolic slope | CONFIRMED |
| §4 joint uniformity 2^(−6P−18d) after the extra pins | geometry: no reserved triple is in a new current or previous ball, and relay outputs depend only on in-cone initial data. The bijection theorem was re-derived in the prior review. | CONFIRMED (conditional on that theorem) |
| §4 existing public ports cannot carry outgoing X | consequence of the bijection; scoped "under this prior" | CONFIRMED |
| §4 keys exposed 7/30; shared pad 7/30 | K1/K2 | keys CONFIRMED at all settings; shared pad **setting-dependent** (SF3) |
| §5 unique point (0,S,±(S+2d)) | S1: 1,024 geometries + proof re-derived; S2 actual | CONFIRMED |
| §6 1/2, 5/16, normalization, discrimination | C6; author m8 | CONFIRMED |
| Author replay, normal and -O | byte-identical | CONFIRMED |
| Dependency hash and five byte-identical copies | sha256 + cmp | CONFIRMED |

### §5 proof check by hand

For a point p on the shell, being 2R from the origin forces the triangle inequality to be tight, so p_y ≥ S and p_z ≥ d. Write a = |p_x|, u = p_y − S and w = p_z − d, with a + u + w = R.

- The C_X condition becomes |u−S| ≥ S+u, so u = 0.
- The C_Y condition becomes |p_x−T| − |p_x| ≥ T, so p_x ≤ 0.
- C_R gives p_x ≥ 0 by the same argument.

So p = (0, S, S+2d).

On the shell, "≥ 2R apart" is also *equivalent* to "no meeting of the two waves inside the backward cone before R" in the L1 metric:
- two shell points are at even distance;
- if that distance is < 2R, some coordinate offset is shared with the same sign;
- a step along that coordinate gives a common neighbour of q at tick R−1.

So the condition is necessary and sufficient for *no early meeting*. It is not necessary for a *correct output*, because a meeting may be harmless. The report's "sufficient, not necessary" refers to the latter, which is correct.

## 3. Findings

Severity applies to the claim text. Classification follows §A.31.

**SF1 (should-fix). The 2/5 and 9/10 values are specific to XOR masks; the robust obstruction is reversibility without an entropy sink.**

Classification: NEW, with a POSITIVE component.

Input-independent random permutations of the carrier are still reversible, carrier-only and input-independent, and XOR masks are a subset of them. They achieve a certified minimax of **7/30**, and 7/30 even when every output must stay a valid 12-state carrier (E1–E3). The column-capacity bound shows that no doubly-stochastic map does better.

Consequences:
- The "9/10 if validity is required" figure in the Verdict is an artifact of translations. Under the same validity requirement, a validity-preserving permutation of the six X+ states gives 7/30.
- The report's scope paragraph already excludes "data-dependent processing", and a permutation arguably falls under it. So nothing stated is false.
- However, the Verdict's juxtaposition invites the reading that validity itself costs 9/10.

Suggested addition: *"Input-independent reversible maps of the carrier alone (random permutations, which include all XOR masks) have exact minimax 7/30 > 0. A zero-error reset needs data-dependent processing or an ancilla that absorbs the old carrier."* This supports the report's conclusion that encryption is not replacement, and it gives the class boundary its natural form.

**SF2 (should-fix). §5's significance depends on an unstated resource assumption.**

Classification: BORDERLINE, with an assumption-watch marker.

The target outgoing state is affine in x: (x, x⊕f(U), x⊕g(U), z) with (f,g) drawn from the calibrated plane law. The single admissible shell point per relay port can hold one isolated private pulse. Witness W shows such a pulse XORs its payload into the relay port natively, with a blank prefix.

If supplied *biased, correlated* private payloads are admissible initial resources, then pulses at (0,S,±(S+2d)) with joint law (f,g) would deliver the Y/R plane law without any multi-source compiler. The brief puts "derivation of the calibrated probabilities from OI" out of scope and requires initialization to be counted, not absent. In that case the §5 collapse would not obstruct this component at all.

If only fair independent seeds are admissible, so that the law must be *computed* natively, the collapse binds as stated.

The report should state which resource class "fresh private apparatus resources" means. Even in the permissive case, the following would still be missing:
- a third x copy for the X slot;
- a fresh Z port;
- an outgoing carrier geometry readable by the next selector;
- the joint law with the public frontier records. The pulse at (0,S,S+2d) reaches Q_X at tick S+2d, inside any window with B ≥ 2d. The reflected pulse reaches the old H port at about 2S+2d−8T.

This is not a claim that a reset exists. It is a hidden assumption that decides whether §5 is the binding obstacle.

**SF3 (should-fix). The §4 shared-pad statement is setting-dependent.**

Classification: CONFIRMING. This is the prior review's N2, and it was not propagated.

"A shared unselected pad also gives 7/30" is computed by J2 at setting Z with X/R sharing one pad. The X- versus Z-mixture TVs with one pad shared by a pair of unselected ports (K2):

| Setting | Pair sharing a pad: TV |
|---|---|
| X | YR: 1/15; YZ: 0; RZ: 0 |
| Y | XR: 7/30; XZ: 0; RZ: 0 |
| R | XY: 1/6; XZ: 0; YZ: 0 |
| Z | XY: 1/6; XR: 7/30; YR: 1/15 |

With all three unselected ports sharing one pad (K1), the TVs are X: 1/15, Y: 7/30, R: 1/6, Z: 7/30.

At the relay's own setting X, a shared pad gives 1/15, or **0** for any pair that includes Z. So this particular X/Z-mixture discriminator can miss a shared-pad defect at setting X. Suggested wording: "(7/30 at setting Z with a shared X/R pad; the value depends on the setting and on which pads are shared, and is 0 for some pairs)". Any shared-pad countercontrol carried into an X-reset acceptance test should use a discriminator that is nonzero for every pairing.

**SF4 (should-fix). The register diagnostic shows dependence, not exclusive routing.**

Classification: ELABORATING.

At α=1 the relay output equals the D register at (q,S), with every other slice-S datum contributing zero net. That is the precise content. But the port also responds, with coefficient binom(d,k), to replacing other (blank) wavefront sites (0,S−k,k): k ∈ {2,4,6} for d=6 and k ∈ {2,64,66} for d=66. The simulation confirms this exactly.

Physically, the relay is the free continuation of the origin's echo wave. It works without the selector, since the controls cancel identically on y=S (m6), and it does not use the transport theorem. Suggested wording: "the port value is the XOR of slice-S registers weighted by path parity; at α=1 the actual register enters with coefficient one and all other slice-S data cancel."

Related point, also ELABORATING: the relayed bit is already public at q. The relay adds physical routing, not information. Privacy of q± is irrelevant for x, and matters only for bits later added there. That is acceptable for the X slot, because μ_(X,s) has deterministic X = s. It does nothing toward the hard part, the fresh (y,r,z) independent of input and record. The report says as much in §7 ("not just more encrypted copies").

**SF5 (should-fix). Some checker verdict lines are not generated from measurements.**

Classification: CONFIRMING. AGENTS: "generate verdict text from the measurements".

- The "N-controls … detected" line is printed after a constant arithmetic assertion (gap b). Mutant m10, which removes the only α=0 simulation, still prints it.
- J0 prints a minimax over computed ingredients only (gap c).
- §3's "the three listed control points lie on the boundary; the Z control is outside" is described as verified by exact enumeration, but the checker tests only ≥ R (gap a).

All three underlying statements are true by my independent checks, so this is evidence presentation, not a mathematical error. Generate each such line from a measured countercontrol, or reword it as "by proof (§2)".

**N1 (nit).** "The choices are exactly 6 and 66" is correct under the D-field requirement. Without it, d ∈ {2,4,64,68,70} also relay x, in a rotated field, as the H^d formula already says. The d<T condition for the H frontier against q₋ is sufficient, not tight (d ≤ 4T suffices).

**N2 (nit).** ΔJ's upper bound is exactly the nested-ball difference identity (G3), which is worth stating as such. It over-counts the overlap of the two ports' balls and the overlap with C.

**N3 (nit).** Process narration ("according to the review supplied in the conversation", "The other session's /tmp brief was not available here") is fine in a handoff. It must be dropped if any of this is ported into `papers/` or `book/` (§A.27, §A.30, §A.32–33).

**Positive confirmations.** Classification: POSITIVE / CONFIRMING.
- The mask-bound scope paragraph is accurate. It covers masks chosen after learning X and heralded branches, and it gives the conditional-law versus unconditioned distinction. The record-weighted values at the uniform mask are 1/5 and 1/25.
- No copies of the unknown input are used: x occurs once, at the origin.
- The readiness enlargement is load-bearing, as the countercontrol shows. It is correctly declared an *additional input-independent resource*, not a property of the old apparatus.
- The relay claim is correctly scoped as X-specific, under enlarged readiness, with d<T.
- The §5 result is stated as a method boundary, not a no-go, and the d ≥ T caveat is accurate.
- The §6 mutant passes both marginals exactly and fails the joint test, as intended.

## 4. Formerly unverified, now replayed

The author bundle was supplied after the independent work. The replay (§1.4) reproduces `checks.out` byte for byte in normal and -O modes. The dependency hash and the five copied files are verified, and 9 of 11 mutations are killed. The two survivors are explained: m6 is an expected insensitivity, and m10 is SF5.

What remains unverified:
- **The imported transport (extrusion) theorem.** It is not needed for the X relay, which is a direct first-arrival computation from the origin. It is needed for the full transported-carrier interpretation of the other three signs, as the report says.
- **The §4 frontier-bijection theorem at the actual P.** The prior review re-derived it and simulated it at small (T,P,B). Here only its geometric preconditions under the new zero pins were checked, symbolically for all indices.
- **The nested dependency archives inside `OI_native_selector_handoff_v1.zip`** (the selector-session handoff and its five archives). Only the outer hash was checked.
- **Large-parameter dynamics.** Simulations used R ≤ 31. The T=185 statements rest on the exact geometry (G1) plus the first-arrival linearity proof, which I re-derived.
