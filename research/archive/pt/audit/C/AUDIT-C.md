# Coordinator's audit of thread C — FOUR-COMP

Audited: `pt/C/RESULT.md` sha256 `1fe5af4c7e0c4dd50996b202ce32dc4ec84d9c135afe3e772391eed6ad796906` (28 files in `pt/C/`,
counting `.start_marker`).

## Integrity
- `inputs.manifest.sha256`: OK. `pt/base` HEAD `9f9f8257…`, status clean, no `__pycache__`/`.pyc` under `base/`.
  The protocol and both amendments are unchanged.
- The thread wrote only in `pt/C/`. No foreign file is present, which agrees with its §7.

## Replays (coordinator, `pt/auditC-replay/`, `python3 -I -B`)
All five reproduce their recorded stdout byte for byte. Each has empty stderr and exit 0.
- landed `kt4_prem1_probe.py` (c0): 79 checks, `1873134…`;
- `c1_cone_level`: 40/40, `37053fb7…`;
- `c2_carrier_models`: 36/36, `40376431…`;
- `c3_route_ingredients`: 17/17, `ccb06b06…`;
- `c4_supplements`: 7/7, `a0466c6c…`.

## Independent check (`indep_checkC.py`, sha256 `d7327447…`; output `da34f58a…`, replay identical)
The check was written from the landed and design definitions, re-read for this audit. It uses no thread code. The
K_c tables `E0`, `G` and the rotation `R` were transcribed from the thread's printed output. The MSIG maps were
implemented from the thread's prose description. All 33 checks are CONFIRMED, with countercontrols green.
- **Primitives (P1–P4).**
  - The landed `cnot` is exactly conjugation by CNOT (symbolic), so `cnot Q3 = Q3`.
  - The trace pairing gives `dualW Q3 = {opW ≥ 0}`.
  - `actT reflY` and `actC reflY` are the two partial transposes, so `actC reflY Q3 = twin` and
    `dualW twin = actT reflY (dualW Q3)`.
- **M_tok (M1–M3).** Every membership was checked directly, including that the dual tables are effects.
  - famI = −1/8 and famII = −1/8.
  - Countercontrols give +1/4.
- **B2 classification (T1–T3).**
  - Per-token transport invariance of both families holds for all 16 charts (symbolic, 64 variables).
  - The coboundaries are exactly the 8 even patterns.
  - For each of the 8 odd patterns, the transported witnesses were checked as members of that pattern's cones and
    duals, with values (−1/8, −1/8).
  - Even patterns: [W] via uniform-Q3 FCC (landed F2/F3).
- **Uniform K_c (K1–K6).**
  - `E0 ∈ dualW K_c`: the exact reduction `1 + x1y3 − x2y2` with the Lagrange identity, and `cnot E0 = E0`.
  - `E0 ∉ dualW Q3`.
  - `K_c ⊆ Q3`: products are `ρ_x ⊗ ρ_y`, and P1.
  - `phiW ∈ K_c`.
  - famI = −1 for uniform K_c and for (Q3, Q3, K_c, K_c); famII = −1 for (K_c, K_c, Q3, Q3).
  - `actC R phiW = G ∉ K_c`, so IE1(K_c) fails.
  - The four pair hypotheses hold [W].
- **A2 route, step 3 (A1–A3).**
  - The 16 token products have det 256, and each lies in H00, so they form a basis of ℝ¹⁶.
  - A general bi-affine map, with 289 coefficients, is a bilinear form on H00 × H00.
  - Under N2 and `prodEff_apply`, the two bi-affine maps agree at all 256 points.

  Together with the landed `ProductData` fields, which are stated at every chart point (`prodEff_apply` and the
  combination laws, CompositeInterface:210–218, read), this makes the token clauses follow from N2 with no one-body
  premise, no hadm and no local tomography. That is as the thread states.
- **Converse via MSIG (S1–S4).**
  - σ is an involution, and `σι = ιR`.
  - TPS holds in MSIG for all token vectors (symbolic).
  - The cross values are exactly famI and famII of the homogenized effect tables.
  - The unit pairing is 1.

  With hadm, an effect's homogenized table lies in the dual cone [W]. FCC and the complement identity then bound every
  cross value in [0, 1], so the hull body carries N0 ∧ N1 ∧ N2. Both directions of `∃V.(N0 ∧ N1 ∧ N2) ⟺ FCC` (relative
  to hadm) are confirmed. The ⇒ direction uses Lemma B1, which is [D].

## Finding (audit; NEW): the tree obstruction B3 holds only for conditions on cones and gate maps
B3's header admits conditions "reading the cones, gates and locals of at most three of the four pairs", each
invariant under per-token reflection charts. As stated, this is false:
- **The chart action.** The chart action that preserves NClass sends `(A, B, A′, B′)` to
  `(D^{g_i}A, D^{g_j}B, A′D^{g_i}, B′D^{g_j})`.
  - Under it, the quantum locals (identity) are carried onto M_tok's locals (`B_13 = B′_13 = reflY`) on only two of the
    four 3-pair subsets.
  - On `{01, 23, 13}` and `{23, 02, 13}`, no chart does it (B3, enumeration).
- **A conjunction of two conditions forces EvenCycle.** Let `Π_S` say: "on the 3-pair subset S, the determinant
  pattern of the post-locals is a chart image of the quantum one". Each `Π_S` reads three pairs, is chart-invariant
  and holds at the quantum data. `Π_{01,23,02} ∧ Π_{01,23,13}` implies EvenCycle of the orientation bits. It fails at
  every NClass decomposition of M_tok's gates (B4, exhaustive over Z₂⁸; orientation is a gate invariant by thread D's
  T2).
- **Orientation equals twist** (B5 + [W]). An NClass gate preserves Q3 only with even orientation, and twin only with
  odd orientation. The exact ingredients:
  - `twin ⊄ Q3`;
  - `cnotTw(prodState xplus z3) = idW ∉ Q3`, so `cnot twin ⊄ twin`.

  So on cones in {Q3, twin} under hcls ∧ hgate, the orientation bits equal the twist bits.
- **A class member that implies FCC.** Combine "each cone is Q3 or twin" (one-pair conditions, chart-invariant) with
  the two `Π` conditions. Under the pair hypotheses this forces an even twist pattern, and hence FCC (by B2).

So the class as stated contains a principle that implies FCC. B3 holds for conditions that read cones and gate
*maps*, or read the supplied locals only through the gate. That is exactly the wording of the thread's own B5,
"intrinsic condition on at most three pair cones", and the argument (R1, I4W, R2) is sound there; B1 confirms the gate
transport. The correction narrows B3's scope and leaves its use in B5 intact. A side observation, not a composition
principle: the supplied locals carry a chart trivialization, so 3-pair conditions on them can glue to the 4-pair
parity.

## Written steps reviewed
- **A2.** Sound step by step:
  - posBA/posAB from N1, `prod_mem` and `prodEff_effect` [K CI:227–229];
  - the token clauses from N2 by bi-affine extension (checked above);
  - FCC by Lemma B1, which is [D] and not certified.
- **A5** (IP₁ variant). The vanishing step uses `exists_effect_rescale` and bilinearity. The positivity step needs
  `t(g, g′)` to be an effect, which follows from K ⊆ maxCone and the complement identity. The purity lemma is the
  standard first-order argument: a positive multilinear readout with a pure marginal factors. The extension step is
  as in A2. The argument is sound. Its exact ingredients (c3 U1–U3) are replay-confirmed, not recomputed.
- **Not independently recomputed (replay-confirmed only):**
  - the carriers ANC, MTW/MTH, SEPH, PAD, CORR and HBA/HAB;
  - the entangled-core identities E1/E2;
  - the link-instance source checks c4 U1/U2.

## Verdict for integration
- **FCC.**
  - Relative to certified L: **INDEPENDENT**, by a valid countermodel. M_tok's data satisfy hcls, hadm, hcl and hgate;
    L certifies nothing with three or more tokens; and both families fail at −1/8 (confirmed above).
  - Sufficiency: **CONDITIONAL** on N0 ∧ N1 ∧ N2. This is sound. Over carriers it is equivalent to FCC relative to
    hadm, with both directions confirmed.
  - Assessment: the principle **explains without reducing**. It identifies FCC with the existence of one
    regrouping-invariant four-token composite, with no cone, inequality, operation or local tomography in its
    statement. But it carries exactly FCC's strength.
- **tokA, tokB.** CONDITIONAL on N2, with N0's data form. Sound. The principle is strictly stronger than the clauses,
  relative to N0.
- **Routes refuted (confirmed):**
  - uniformity, one-pair-type matchings and U* (uniform K_c, −1);
  - cone-level 3-pair principles (M_tok, B3 restricted).
- **B2:** confirmed. On {Q3, twin}⁴, FCC holds exactly at the 8 even patterns.
- **Not kernel-checked:** the route's Lean (A7 UNBUILT); Lemma B1 and the headline are [D]; the classification step
  `P ∧ C ⇒ FCC` is [W + L].
