# Independent review: native selected-sign readout by opposite-front masking

**Reviewed:** `oi_native_selector_v1/`, which contains:
- `REPORT.md`, `INVESTIGATION.md` and `README.md`;
- `checks.py`, `selector.py`, `native_checks.py` and `law_checks.py`;
- `relay.py`, `compiler.py`, `layout.py` and `transport_layout.py`;
- `checks.out` and `SHA256SUMS`;
- `dependencies/OI_selector_session_handoff_v1.zip`.

**Not reviewed:**
- The transport (extrusion) theorem of `OI_native_transfer_handoff_v1`, which gives `U_S(Q_i)=(0,0,c_i)` at `P=12*840^185`. It is imported as a premise and was not re-derived here.
- The other four nested dependency archives.
- The selector-record note, which was already reviewed separately.

**Repository:** untouched. No commits, pushes, comments or dispatches were made. All work is under `.../scratchpad/native-selector-review/`.

## Verdict

**HOLDS WITH CORRECTIONS.** The corrections are to the claim text only; the mathematics stands.

Every mathematical claim I could test reproduces under independent code:
- the update algebra;
- the Lucas parity and the X compensation;
- the meeting lemma, for all admissible exteriors in the tested cases;
- the general D-toggle identity, including nonlinear lower computations;
- the 2S separation on the actual 1479-entry T=185 layout at the astronomical P;
- the §5 frontier ordering and bijections;
- the exact record laws L1–L3.

No must-fix error was found. Three should-fix items concern framing:
- F1 and F2: what the "selection" is;
- F3: the review status of the imported transport premise.

There are also three nits.

The result is internal consistency work (§A.23): a native interface construction under supplied resources and access. It moves no correctness band.

## 1. What was run

### Integrity

- `sha256sum -c SHA256SUMS`: all 13 entries OK.
- The embedded prior archive has sha256 `3d18fe9c…1d33`, as expected. I extracted it, after a path-traversal check, into `ext/prior/`; its own `SHA256SUMS` passes for all 10 entries.
- The nested `OI_native_transfer_handoff_v1.zip` has sha256 `4a232a48…9098`, as expected. I extracted it into `ext/transfer/`; its `SHA256SUMS` passes for all 12 entries.
- `relay.py`, `compiler.py`, `layout.py` and `transport_layout.py` are byte-identical (`cmp`) to the transfer handoff's copies:

  | File | sha256 |
  |---|---|
  | `relay.py` | `05ebed2d…` |
  | `compiler.py` | `c0057e95…` |
  | `layout.py` | `b8286cb1…` |
  | `transport_layout.py` | `1eb4eb4e…` |

  The claim holds.

### Replay

- I read all eight Python files first. They use only the standard library and numpy-free packed integers, write nothing, and make no network calls.
- Under `python3 -I` the script directory is not on `sys.path`. I therefore ran `checks.py` through `mine/run_bundle.py`, which *appends* the bundle directory to `sys.path` so the standard library cannot be shadowed, and then uses `runpy`.
- Both modes were run from `run/` on Python 3.13.16:

  | Mode | Output | Runtime |
  |---|---|---|
  | `python3 -I -B` | byte-identical to `checks.out` (sha256 `0efc7df3…25dd1`) | 4.7 s |
  | `python3 -I -B -O` | byte-identical to `checks.out` | 4.9 s |

### Mutations of the author checker

Each mutation was applied to a copy in `mut/`; the bundle itself was not edited.

| # | Mutation | Result |
|---|---|---|
| m1 | always compensate, ignoring parity | killed at N2 (T=1, P=1) |
| m2 | control exponent `-S` instead of `1-S` | killed at N2 |
| m3 | `parity` forced to 1 | killed at N1 |
| m4 | selected pad not zeroed | killed in L1 |
| m5 | N4 expects an A-toggle instead of a D-toggle | killed at N4 |

m6, which dropped one of the two exteriors, still passes, as expected. It is a coverage reduction, not a defect.

### Independent re-derivation

The scripts are in `mine/`. None imports bundle code. `dump_sources.py` runs the bundle's `transport_layout.build()`, already read, only to export the actual T=185 source list as JSON data (`t185_sources.json`, sha256 `39c47fe8…5e3e`).

| Script | Content | Runtime |
|---|---|---|
| `algebra.py` | H, its inverse, order, Lucas parity, deadline-meeting algebra | <1 s |
| `sim.py` | own numpy packed-lane torus simulator: meeting lemma, record statistics, countercontrols | 46 s |
| `frontier_sim.py` | §5 subsequent-record structure on the actual masked apparatus | 4 min 16 s |
| `geometry.py` | actual T=185 source geometry at astronomical P; general §5 ordering | <1 s |
| `laws.py` | exact Fraction record laws | <1 s |
| `xplane.py` | admissible lower-source region at Q_X | <1 s |

Outputs are saved beside each script as `*.out`. Total local compute was about 6 minutes.

## 2. Independent results

| Item | My check | Result |
|---|---|---|
| 3a: H | Permutation of F2^3. The stated inverse `(d^ab,a,b)` is correct. Order 12. 3-cycle on single-field triples. `H^(1-S)(l,0,0)` arrives as `(l,0,0)` at the final input, for S=0..39; reduction mod 3 is valid on basis triples. | PASS |
| 3b: Lucas | `binom(T+P,T)` mod 2 = `[T&P==0]` for all 34,191 pairs with T+P≤260, via an own lattice-path recursion and `math.comb`. v2(12·840^185) = 557 > bit length of 185, and P has 543 digits, so b=1; b=1 for every T<2000. | PASS |
| 3c: algebra | `H(L^(m,0,0)) = H(L)^(0,0,m)` for all L and m. B- and D-field arrivals are *not* D-toggles, which is a countercontrol. | PASS |
| 3c: meeting lemma (S0, M1) | Own simulator, checked against a naive per-site loop and its inverse. Cases: (T,P) = (1,0), (1,1), (1,2), (2,1), (2,3), (3,4), (3,6), (4,3), covering both b=0 and b=1. The lower computation is my own: one single-site pulse per unknown input, each at a randomly chosen admissible point at distance S from its port with odd path parity. Each input occurs at exactly one site, and cross-port terms come from exact multinomial path parity. All 1024 assignments (4 inputs, 4 raw pads, 2 setting bits). Dense exteriors outside the radius-S current and radius-(S-1) previous cones, both lane-constant and lane-varying, so every lane has a different exterior. Outcome: blank prefix; endpoint `(0,0,c^m)`; the selected bit is exact; the 3 unselected bits are fair and independent. | PASS |
| 3c: general nonlinear lower (M2) | 16–60 random multi-field lower sources (nonlinear interactions), lane-varying, at admissible boundary points; lane-varying exterior; 512 lanes; (T,P) = (1,0), (1,2), (2,1), (2,3), (3,6). The masked run equals the unmasked run before S and equals unmasked ^ (0,0,m) at S, while the unmasked endpoint is *not* D-only. This confirms the "any compatible lower output" generalization. | PASS |
| CC1 | Dropping the X compensation at b=1 [(1,2), (2,1), (3,4)] | DETECTED |
| CC2 | At b=0 [(1,1), (2,2), (3,3)] no compensation is needed, and compensating anyway fails | DETECTED |
| CC3 | Controls one site closer (distance S−1) | DETECTED |
| CC4 | Lower sources on Q_X's boundary at dy=+1, which lie 2S−2 from a control, break the toggle. The 2S bound is load-bearing. | DETECTED |
| 3c: actual layout (G1) | All 1479 actual T=185 source entries are ≥2S from every control for P ∈ {1, 2, 3, 12·840^185}. The minimum margin is **exactly 0**, attained by the input, Y, R and Z sources. No source lies strictly inside a transported current cone. Controls are >S from the old X and H ports. The old input's previous triple lies outside every previous cone. | PASS |
| 3d: R1 | All 12 hidden states × 4 settings × 16 records satisfy `P(r|a,c) = (1/8)[r_a=c_a]` | PASS |
| 3d: R2 | 512 menu cells. Each record effect was solved by exact elimination from the 8 preparations (consistent, rank 4) and equals `P_(a,s(r))/8`. | PASS |
| 3d: R4 | Masked I/2 mixtures are identical for all 6 pairs and all settings. X vs Z with every key exposed gives TV=7/30 at every setting. A shared pad gives 7/30 at settings Y and Z, but **1/15 at X and 1/6 at R** (see N2). | PASS |
| 3d: R5 | 2048 joint cells (prep, setting, x, herald, record) for the X reset plus masked read match the reference. Success mass is 5/8 on every input, failure mass 3/8, total 1, with no postselection. | PASS |
| 3e: G2 | For all 400 (T,P,B) with 1≤T,P≤10 and 1≤B≤4: every frontier block lies outside all ready cones; its own path is axial and unique; there is one block per window record; the order old-X, H, Y, R, Z, X is triangular, with exactly the F_Y→Q_X and F_R→Q_X same-tick edges; the bit count is 6P+18B. G3 samples the same at T=185, P=12·840^185. | PASS |
| 3e: F1 | On the *actual masked apparatus* (lower sources, controls, masks and dense exterior): (T,P,B) = (1,2,2), (2,1,2), (1,1,3); every one of 14–20 blocks; 64 dense backgrounds per block. In each case, every earlier-ordered record at all six ports over ticks 1..S+B is independent of the block, and the block's own record is a permutation of it. | PASS |
| 3e: F2 | Exhaustive 4096-lane joint bijections: {F_Y1, F_R1, F_Z1, F_X1}; {F_Y1, F_R1, F_X1, F_X2} across two ticks; {M, N, F_Y1, F_X1} across old and new ports. Countercontrol: F_Y1 really changes Q_X(S+1). | PASS |
| R3 (equivalence) | On every menu preparation and setting, the full masked record law equals the law of port a alone × three fair coins (exact). | PASS (see F1) |

### Proof check by hand (§4)

In the backward cone of (Q,S), every point at tick t is at distance ≥t from every source at distance ≥S from Q, so only first arrivals occur there.

A cross term between the lower and upper computations needs both in one neighbour sum at a tick t≤S−1. That forces dist(p,C) ≤ 2t ≤ 2S−2. At tick S the meeting is exactly the final H at Q.

The report's identity dist(C_i,p) − 2S = σ_{q_i}(p) − T is correct, so the condition is exactly the transfer layout's one-sided σ ≥ T. Points on two radius-S spheres are at even distance, so the margin 2S−1 cannot occur and the bound is tight.

Exteriors outside the radius-S current and radius-(S−1) previous balls cannot reach (Q,S). The universal "all admissible exteriors" claim therefore rests correctly on finite speed, not on the witnesses.

## 3. Findings (§A.31 classification; severity for the claim text)

**F1 (should-fix). The "selection" is a one-time pad.**

Classification: NEW, scoped to deadline-meeting selectors with the four Q ports public. This is an assumption-watch marker.

At a D-only first-arrival endpoint the incoming lower sum is necessarily `(c,0,0)`; the preimage is unique. For *any* upper arrival `u` at the deadline, the port triple is `(u_B, u_D, c ^ u_A ^ u_B·u_D)`, which is affine and injective in c (`algebra.py` A3). Consequences:
- No deadline-meeting construction with all four Q ports public can remove an unselected sign from its port record.
- Such a construction can only randomize that record with control data that must stay private.
- The masked construction is therefore the generic form of this class, not one choice among several.
- Its whole hiding power is the privacy of the control payloads and their propagating copies, which is an access assumption.

R3 states the same thing operationally: the masked record law is identical to "observe port Q_a only" plus three independent coins.

What the construction adds over that trivial readout is real but specific:
- a setting-independent public port set;
- a native XOR into D at the deadline, with no input adapter and no clean neighbourhood.

It adds no physical selection. The report says privacy is "supplied" and "revealing a mask key defeats the intended restriction". Even so, the Result paragraph ("can be read selectively"; "closes a readout interface") should say explicitly that the unselected signs remain in the public record, one-time-pad encrypted under private keys, and that the record law equals single-port access with independent noise.

The scope of this finding is the deadline-meeting class only. It is not a statement about selectors acting after S, or about OI.

**F2 (should-fix). The setting is preparation data, not dynamics.**

Classification: ELABORATING.

The dynamics is identical for all settings. The setting is solely which pad is pinned to zero, together with the X compensation relation. The report states this in §6 ("compiled into the initial mask correlations"). The §9 sentence "The immediate clean-neighborhood obstacle has an explicit route around it" should be scoped: by F1, the route works for operations that enter the endpoint's A-slot affinely. A nonlinear or information-discarding selector, such as a setting-register-controlled AND, cannot be done by a deadline meeting. It must act after S, where the neighbourhood problem returns.

**F3 (should-fix). The transport premise's review status is not stated.**

Classification: ELABORATING.

At T=185 the record-law claim is conditional on the transfer handoff's extrusion theorem (D-only endpoints with a blank prefix at `P=12*840^185`). The readout's own use of that premise is correct:
- b=1 is verified, and holds for every T;
- the 2S separation holds on the real layout at symbolic P;
- the meeting lemma does not need D-only outputs.

However, the report calls the premise only "conditional and expensive". In the chain supplied, that theorem has been hash-checked only; the prior review did not open the dependency archives. The report should say that the T=185 instance rests on an imported author theorem not covered by this or the previous review.

**F4 (nit). The Q_X layout has zero slack.**

Classification: ELABORATING, with a CONFIRMING component.

The 2S separation at the actual layout has margin exactly 0 (G1), and CC4 shows the bound is load-bearing. Moreover, because C_Y and C_R also arrive at Q_X at tick S, the admissible lower sources on Q_X's boundary sphere are exactly the x=0 lower semicircle: 2S+1 of the boundary points (`xplane.py`).

The present reset satisfies this, because X is a pure echo of the input at the origin. A future layout in which the X port carries a computed function would need relocation or a different control geometry. This is worth recording as a constraint on reuse.

**N1 (nit). N4 uses literal programs.**

Classification: CONFIRMING.

N4 is described as the "actual small compiled reset layout at T=9". It uses the actual compiler and layout code with *literal* programs (u0, u1, u2), not the calibrated formulas, as the code comment says; I confirmed T=9 with 38 sources. Suggest wording such as "compiled layout with literal programs".

**N2 (nit). The shared-pad TV depends on the setting.**

Classification: CONFIRMING.

The L2 line "exposed keys or a shared unselected pad restore TV=7/30" is general in form, but the shared-pad check is run only at setting Z. The shared-pad TV is 7/30 at Y and Z, 1/15 at X and 1/6 at R. The countercontrol's point, TV>0, holds at every setting. State the setting, or say "TV>0 (7/30 at Z)".

**N3 (nit). Process narration if ported.**

Classification: CONFIRMING.

§1's "has now received independent review, according to the review supplied in the conversation" is acceptable in a handoff note. If any of this text is ported into `papers/` or `book/`, it must drop process narration and internal labels (§A.27, §A.30, §A.32–33).

**Positive confirmations.** Classification: POSITIVE / CONFIRMING.

- **No copies of unknown inputs.** Control payloads depend only on the setting and the private masks. In both the author's and my lower circuits each input occupies one site.
- **No clean neighbourhood assumed.** Only the transport's already-prepared radius-S/(S−1) cones are used, and the controls *replace* 12 zero pins on their boundary. My tests had dense, lane-varying fields immediately outside the cones, so the endpoints' tick-S neighbours were dirty.
- **Quantifiers.** The finite checks are witnesses, labelled as such; the universal claims rest on the finite-speed proof, which I re-derived and found tight.
- **Supplied menu.** L1 and L2 are channel tests on supplied preparations, as the report says. Only L3 composes with the native post-X family, and even there the reset kernel's law is the earlier supplied calibration.
- **Codimension.** The −3 change (8 pins for unused fields plus one relation; rank 3) is correct.
- **§5.** The joint, not marginal, uniformity argument is correct, and P>0 is correctly required.

## 4. What I could not verify

- **The transport/extrusion theorem itself** (F3): the period bound `12*840^R`, the staggered-front recurrence, and the D-only, blank-prefix endpoints at T=185. It was imported and not re-derived or reviewed.
- **The 12-state calibration's provenance** from the carrier-record closure handoff. It was transcribed from SELECTOR-RECORD.md and not re-derived.
- **The reset kernel** (`c_Y = x^[U≥5]`, etc.) at T=185. It was taken from REPORT §7 and the transfer report, and not re-derived from the compiled programs.
- **Large (T,P) and long windows.** Simulation covered T≤4, P≤9 and B≤3. The general statements rest on the proofs; for the §5 ordering I checked the geometry symbolically over 400 parameter triples and on samples at the huge P.
- **Privacy and access closure.** They are assumptions of the construction, not derived, and remain open obligations in the report's own terms.

## 5. Suggested replacement text (Result paragraph, minimal)

> The four transported signs can be read for a preprogrammed setting under the unchanged native update by one-time-pad masking at the first-arrival deadline: independent control pulses arriving from the opposite side XOR private fair pads into the D fields of the unselected ports. The unselected signs remain in the public record, encrypted under the private control data; the record law equals that of observing the selected port alone together with three independent fair bits. No copies of the unknown signs and no clean neighbourhood beyond the transport's prepared cones are used. At T=185 the result is conditional on the imported transport theorem (not independently reviewed).
