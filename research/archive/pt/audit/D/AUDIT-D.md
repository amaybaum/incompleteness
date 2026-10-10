# Coordinator's audit of thread D — NCLASS-ADM

Audited: `pt/D/RESULT.md` sha256 `0207e2647646ef3f7b4477083bf6e47ab1ab199665161403b7d2ad9bd67da53f` (51 entries in
`pt/D/`).

## Integrity
- `inputs.manifest.sha256`: OK. `pt/base` HEAD `9f9f8257…`, status clean, no `__pycache__`/`.pyc`. The protocol and
  both amendments are unchanged.
- The thread wrote only in `pt/D/`, with one recorded exception: the temporary `D_listing.txt` at the scratchpad root.
  It is confirmed absent, and no file newer than the protocol exists at the scratchpad root. No foreign file is in
  `pt/D/`.

## Replays (coordinator, `pt/auditD-replay/`, `python3 -I -B`)
All nine scripts reproduce their recorded stdout and (empty) stderr byte for byte, each with exit 0:
- `d1a_zeroset` (20/20);
- `d1b_classify` (57/57, about 10 min);
- `d1c_bookkeeping` (15/15);
- `d2_adm` (37/37);
- `d3_deps` (29/29, run 2);
- `d4_models` (7/7);
- the leads `e1`–`e3`.

## Independent check (`indep_checkD.py`, sha256 `ec2262ae…`; output `d16cba58…`, replay identical)
The check was written from the landed definitions and from the family G(a, b) as RESULT.md defines it in prose. It
uses no thread code. All 16 checks are CONFIRMED.

**Run 1 failed on my own harness error.** Two checks (C1, C2) printed MISMATCH: my control-dephasing projector kept
basis coordinates (0, 3) instead of (0, 1) of the basis (hom z3, hom −z3, e₁, e₂). The fix was that one line, recorded
in the script, and nothing else changed. Run 1 is kept (`indep_checkD.run1.{out,err}`, out sha256 `a2cd523b…`). The
thread's claim was never in question: its identity C10.h.posFwd has the form my corrected check confirms.
- **Family (F1–F3).**
  - `G(I, J′) = cnot`, and `G(a⁻¹, −b⁻¹)∘G(a, b) = id` (symbolic).
  - `G(a, ±aJ′) = actC(diag(a,1))∘G(I, ±J′)`, and `G(I, −J′) = actC reflY∘cnot∘actC reflY`.
- **Bounds and mixing (P1–P3).**
  - The equatorial pairings are `2 + 2u′ᵀax′` and `1 − u′ᵀbx′`, so a and b are orthogonal (with posInv via F2).
  - The null identity is `⟨b,Y⟩⟨b,HN Y⟩ − σ² − τ² = N(b)(Y₀² − Y₁²) + (b₂² + b₃²)N(Y)`.
  - The O(2) norm identity holds, and U + Uᵀ = 0 forces U = ±J′.
- **T2 and M_refl (T1–T4).**
  - `det cnot(prodState x y) = −(x₀²+x₁²)(1−x₂²)(1−y₀²)(y₁²+y₂²)`. For unit x, y this equals
    `−(1−x₂²)²(1−y₀²)² ∈ [−1, 0]`, which is the step that closes T2: |det| = 1 on both sides forces d = −1.
  - `det(actC A (actT B w)) = det A det B det w`, and `det phiW = −1`.
  - M_refl's post-local `reflY` would give `actC reflY phiW = idW`, with det +1 > 0, which no decomposition of `cnot`
    attains.
- **Deletion countermodel (C1–C3).**
  - `G(I/2, J′/2) = ½cnot + ½cnot∘(control dephasing)`, and the dephased part maps products to positive combinations
    of products, so posFwd holds.
  - posInv fails: the value is −1.
  - The gate is not ipW-orthogonal, so not N-CLASS: `ipW(Ge₁₀, Ge₁₀) = 1/4`.
- **hadm (c) (A1).** `E00 + phiW` has rank 4 and its `cnot` image rank 2. So the sum of a product and a `cnot` image
  of a product lies in neither branch of the scaled `cnot` orbit, and additivity fails.

## Written steps reviewed
- **T1, steps 10–13:** sound; their exact ingredients are confirmed above.
- **T1, steps 1–9:**
  - the frame change;
  - the corner slices through the landed `corner_form`;
  - the Lorentz step (a cone automorphism of L fixing e₀ is `homMap` of an O(3) element, a standard fact);
  - the tangent and zero-set steps, whose exact parts are replay-confirmed in d1a and d1b;
  - the exclusion of the improper case.

  These are coherent written steps on landed lemmas and are not recomputed. The Lean is UNBUILT.
- **T3** (hadm ⟺ product-test cone of a COMP-1 pre-composite of two balls, no `lt`). Both directions are sound. The
  upper bound uses the bilinear decomposition `pEff(e,f) = pEff(1,1) − pEff(1−e,f) − pEff(1,1−f)`, checked by hand.
  `paddedBall3` shows local tomography is not consumed.
- **INDEPENDENT labels for hadm (a), (b), (c).** Valid under amendment 2. Each countermodel meets every certified
  statement bearing on a pair cone. At L these are definitions or theorems true in every model: no certified statement
  identifies the pair system with anything. The countermodels also meet the theorem's other hypotheses, and for (a)
  and (b) H as well. The independence is therefore inexpensive. Its content is in T3: hadm is exactly the assertion
  that the pair is a COMP-1 pre-composite of two balls.

## Verdict for integration
- **hcls.** CONDITIONAL on the recorded, unsourced K1 gate premises: unit corner axis, CNOT frame, and two-sided
  product positivity. Sufficiency: T1 [W + K + X; Lean UNBUILT].
  - The characterization `N-CLASS ⟺ posFwd ∧ posInv ∧ frame` (up to local frames) has both directions witnessed. The
    principle **explains** the property: N-CLASS adds to two-sided positivity exactly a classical CNOT frame.
  - Hidden assumption exposed: the supplied locals must form a decomposition (M_refl). This is harmless, because
    orientation is a gate invariant (T2, confirmed).
- **hadm (a), (b), (c).** INDEPENDENT of the premises certified at L as stated. Sufficiency holds only by restatement
  (T3), and each clause's operational source is the clause in other words.
- **Local tomography.** hadm does not consume it.
