# Changed-lines check: ARP-2 preregistration r4 and PLAN r4, against REVIEW-REACHABLE-r3.md

**Objects (sha256).**
- `qc21/preregistration.draft.md` r4: `b157a6b1852af1092000db29ad312478a4dfb4571134b77b0bde0d4517fbb852`
- `qc21/PLAN.md` r4: `a48274202a32b63f6e1f8f3b6d56a8bfe98affcca6ae56550be2dc4821e7abdc`
- `qc21/controls/rank_fixture.py`: `3fbc3e8d094c570b9e7c76774a80e19a4e25d83562924559dde341cae24e690b`
- r3 baselines: `preregistration-r3.draft.md` `7f0d5983…`, `PLAN-r3.md` `74afe74e…`. REACHABLE is unchanged (r3, `718e7dbc…`, ACCEPT).
- Measured against `review/REVIEW-REACHABLE-r3.md` (`daf48a35…`).

**Standing.** Independent model check, read-only, 2026-11-08. Not human verification. Scope: the r3 → r4 diff. Line references are to prereg r4 (`P:`).

**Reviewer control** (`review/controls_r4.py`, sha256 `e8558a7cfa03263095283632ad230bfe7c94a0d0e72da0aeae50f0409b78c1a2`, exact, `python3 -I -B`). It is a control, not evidence, and it does static algebra only. It checks four things: rule `0`'s single tick on `S_0`; the `u ↔ v` closure of the supply sets; the determinant identity on random integer matrices; and the rank of the C-AFFB (b) fixture together with greedy basis selection from it. **No reachable set is computed under any rule.** `controls/rank_fixture.py` was also re-run and prints `S_0` rank 10 and rank 14 for its 31-law static set, which matches PLAN §11.

## Verdict: **ACCEPT WITH CHANGES**

R3-B1 and R3-B2 are closed, and so are the three non-blocking notes. No new blocking hole was found. The three changes below are non-blocking. The first two are text fixes; the third is optional. All three are best made before `F`:
- R4-N1: freeze `B_P`'s extension for C-AFFB (b).
- R4-N2: state the time-covariant reading of "induced" as a definition.
- R4-N3 (optional): add an encoded-identity check to C-FRAME.

## 1. Each fix

| item | closed? | check |
| --- | --- | --- |
| **R3-B1** NNB in the common clause | **yes** | P:330 now reads "conditional on P2, N2, H-PREP, NNB (for the supplied `Λ_{y,b}`), the supplied registration and the refilled mediator". |
| **R3-B2** frame / determinant | **yes** (§2) | Covered by four parts of the prereg. The frozen frame convention is at P:209-219. "Unitary" is defined as `det_enc β = (−1)^k det_fix β = 1` at P:246-247, with `k = 0` for PC-PLANT, whose planted map is not a dynamics. The schema reports `k`, `det_fix` and `det_enc` (P:480). C-FRAME is at P:300. |
| N: PC-NONSTAB separation | **yes** | P:294: two separate runs, and the planted laws enter no countercontrol's or test rule's set. |
| N: basis-selection cost | **yes** | P:538-543: fraction-free integer elimination in the frozen order from `Λ_0, Λ_{a,0}`, stopping early at 16. Linear independence of law vectors is the same as affine independence, because every law lies on the hyperplane `Σμ = 1`, which misses the origin. So stopping at 16 correctly means the affine hull is the whole simplex plane. The estimate of ≲ 30 min against a 60-min timeout is consistent. |
| N: C-AFFB on a full-rank set | **yes** (§4), with R4-N1 | P:296. |

The S4 phrase screen still passes: the frozen texts changed only at P:330, and that line adds no screened phrase.

## 2. Is option 2 equivalent to evaluating in the encoded frame for every round?

Let `P` be the transposition `x ↔ z`, so `P² = I` and `det P = −1`. A law whose total tick count has parity `p` satisfies `R_enc = P^p R_fix`. A round with `k` ticks takes parity `p` to `p + k`.

**Equivalent quantities, for every round and for both input parities.**
- `outside_ball`, `nonstab_valid`, `offaxis_unit` and octahedrality are invariant under `P`, since `P` is a signed permutation.
- Herald constancy does not involve R.
- `α = 0` is the same condition in both frames, since `α_enc = P^{p+k} α`.
- **The determinant.** For even-parity inputs the encoded linear part is `P^k β`. For odd-parity inputs it is `P^{k+1} β P`. Both have determinant `(−1)^k det β`. The correction `(−1)^k` is therefore right whatever the input's parity. The control confirmed this on 1,400 random cases.

**Where the frames are not interchangeable: whether a map is induced at all.**
- In fixed slots, "π induces `(α, β)` on `L_scope(g)`" means one affine map on a set that mixes parities.
- In the encoded frame the same statement reads: π induces `β′₀ = P^k β` on the even-parity laws and `P β′₀ P` on the odd-parity laws. The two encoded maps are `P`-conjugate, and they differ in general (1,393 of 1,400 random cases).
- This is the **time-covariant** reading: a fixed, time-invariant physical action, described at each time in that time's encoded frame. It is the natural definition for a fixed rule.
- It is stronger than requiring an induced map on one parity class only. If the even and odd parity classes of `L_scope(g)` have different affine hulls, a round could induce a non-octahedral encoded rotation on one class and fail the fixed-slot test. That would be a conservative miss against CANDIDATE. It cannot produce a false CANDIDATE, and it does not affect NONSTAB or NO-VALID-ESCAPE, which do not depend on induced maps.
- The rationale for rejecting option 1 is correct. With parity carried, `R_enc` is not one affine function of `μ` on a mixed-parity set, and the affine-basis equivalence at P:229-235 needs one.

**R4-N2 (non-blocking).** Add one sentence to P:209-219: "Induced means one fixed-slot affine map on all of `L_scope(g)`. In the encoded frame this is the time-covariant notion, with encoded action `P^k β` on even-parity inputs and its `P`-conjugate on odd-parity inputs. It is not a per-parity notion." Optionally, report as a diagnostic field, not a decision input, any round that induces a map on the parity-0 subset of `L_scope(g)` only.

## 3. Are the supplies closed under `u ↔ v`?

**Yes.**
- `M`: `ready(u_2 = b) ↔ ready(v_2 = b)`, and `source ↔ source`.
- `S_0`, checked exactly on all 23 laws: `Λ_{x,b} ↔ Λ_{z,b}`; `Λ_{y,b}` and `Λ_0` are fixed; the 16 P2 products map among themselves.
- CC-MIX's mixtures are listed for both `u_2` and `v_2`.

So the supply sets do not depend on the frame, as P:217-219 claims.

**C-FRAME's expectation is right.**
- Rule `0`'s tick acts on every `S_0` law as `R ↦ (r_z, r_y, r_x)`. The mediator is decoupled, so every round with positive herald has a constant herald.
- `det_fix = −1` and `det_enc = +1`, so the map is classified unitary and octahedral.

**R4-N3 (optional).** In the encoded frame this map is the identity (`P^1 · P = I`). C-FRAME could also require `P^k β = I`, which tests the full frame correction and not only its determinant.

## 4. Does C-AFFB (b) reach full rank?

**Yes.**
- The fixture has 23 + 7 + 2 + 16 = **48** laws.
- The 16 point laws alone are the standard basis, so the linear rank is 16.
- Greedy selection reaches 16. It starts with `Λ_0, Λ_{x,0}, Λ_{y,0}, Λ_{z,0}`, which are affinely independent because their images `0, e_x, e_y, e_z` are, and then scans the fixture.
- Without the point laws the static set has rank 14 (`rank_fixture.py`), so including them is necessary.

**R4-N1 (non-blocking; fix before `F`).** C-AFFB (b) applies "PC-PLANT's `B_P`" to all 48 fixture laws. `B_P` is defined only on the 12 points of the six planted supports (sanity S4 builds it column by column on those points). Four points are uncovered, and so are the point laws and most `S_0` laws supported on them.
- As frozen, the control is underspecified, and an implementation could crash in the self-test, before `F`.
- Any linear extension serves the control's purpose, because the full-versus-basis equivalence holds for every linear `B`.
- So freeze one, for example: "`B_P` acts as the identity on the four uncovered configurations".

**Formatting.** The C-AFFB row at P:296 has a fifth cell that duplicates the route-to-failure text. Delete it, so that a table parser or note generator reading the controls table sees four columns.

## 5. Summary

| item | status |
| --- | --- |
| R3-B1 | closed |
| R3-B2 (option 2) | closed. The determinant correction is exact for both input parities. Counts, octahedrality, herald and `α` are frame-independent. "Induced" is the time-covariant notion; state it (R4-N2) |
| `u ↔ v` closure | holds for `M`, `S_0` and the CC-MIX mixtures |
| C-FRAME | expectation correct; optional encoded-identity check (R4-N3) |
| C-AFFB (b) | full rank 16 reached (48 laws; the point laws are necessary); freeze `B_P`'s extension (R4-N1); fix the duplicated cell |
| PC-NONSTAB separation, basis cost | closed |
| preregistration r4 | **ACCEPT WITH CHANGES** (R4-N1, R4-N2, optional R4-N3; none blocking) |
