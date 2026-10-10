# Coordinator's audit of thread B — PAIR-ACT

Audited: `pt/B/RESULT.md` sha256 `acd8b8a164ca148f772cfcff4ef5796e21ca65e1eb3d0be578ede6b1e8c26ac5` (54 files in `pt/B/`,
including `explore/` and `landed_replay/`).

## Integrity
- `inputs.manifest.sha256`: OK. `pt/base` HEAD `9f9f8257…`, status clean. The protocol and both amendments are
  unchanged.
- The thread wrote only in `pt/B/`. No foreign file is present.

## Replays (coordinator, `pt/auditB-replay/`, `python3 -I -B <script> ..`)
All seven reproduce the recorded stdout and `.err` (`exit=0`) byte for byte:
- `b1_consumed` 33;
- `b1_models` 53;
- `b1_steps` 23 (against run 2);
- `b1_implicit` 7;
- `b2_sources` 27;
- `b2_census` 7 (against run 2);
- `explore/e1_ie1_foil` [F].

The thread's two recorded failed first runs were not re-executed: `b1_steps` run 1, a countercontrol logic error, and
`b2_census` run 1, which was never executed because `/usr/bin/time` is absent.

## Independent checks (no thread code)
- **`census_scan.py`** (sha256 `97cadf51…`, output `50af7930…`).
  - It is a multi-line declaration scan of all 215 landed Lean sources.
  - The Prop-valued declarations over the pair carrier are exactly the thread's eight: `CandidateCone`, `CtrlGate`,
    `Entangling`, `EntanglingOf`, `GateRel`, `IsProduct`, `NativeGate`, `NativeGateOf`.
- **`indep_checkB.py`** (sha256 `1fe957ce…`; output `e05cdf4c…`, replay identical). All 16 checks are CONFIRMED.
  - **Runs 1 and 2 failed on my own harness errors.** Both are kept (`indep_checkB.run1.*`, `indep_checkB.run2.*`).
    - Run 1: an argument-order error in my pairing helper, which raised an exception.
    - Run 2: I passed the wrong sign to the sharp effects in M2, which printed MISMATCH.

    Each fix touched only the faulty call or signature. No claim of the thread was in question: the landed
    `cnot_idW` and the −1/2 value, which run 3 confirms, are as recorded.
  - **Source scan (S1–S3, S1c).**
    - The design declarations naming `hgate`/`hinv` outside the package module are exactly the twelve of the thread's
      list.
    - `link_mem` and `bell_mem` apply `hgate` only to a product state, and `bell_mem_dual` reads `hinv` only through
      `dualW_of_inv`.
    - Lemma R uses `hgate` on general cone elements.
    - The scanner detects a planted use.

    So the consumed instances are (L), (BS) and (BD), as the thread states.
  - **Countermodels to `hgate` (M1–M4, M4c).**
    - M_max: `idW ∈ maxCone`, by the Lorentz pairing; `cnot idW = chainW`; and chainW has value −1/2 at the sharp
      effects of −e₁ and −e₃.
    - M_D13: `pxz ∈ Q3`, and `g_D pxz = idW ∉ Q3`.
    - `g_D` meets NativeGate's frame, relT and relC with `nflip`, and has a two-sided inverse. Its two-sided
      positivity follows from `cnot`'s, because maxCone is `actT reflY`-invariant.
    - A frame countercontrol rejects the identity map.
  - **CONS separations (C1–C4).**
    - M_pre: `hgate` fails (`g_pre phiW = chainW`), while the post-local Bell data are those of M_Q.
    - M_DD: `g_D` breaks twin, while the pre-corrected `g_Tw` preserves it.
    - F = diag(1,−1,1,−1): the identity `|x − Dy|²/2 + …` holds, F lies in maxCone, and `ipW F phiW = −2`. So (BD)
      fails in M_max, and a product-only pair system cannot carry `cnot`.
    - (BS) fails in M_D (`bellOf I reflY = idW`).
  - **Lemma O ingredients (O1–O3).**
    - σ_q keeps N-CLASS form and flips the orientation.
    - `homMap reflY` preserves the Lorentz form, so maxCone and SEP are σ-blind.
    - The 16 gate patterns on uniform maxCone split 8/8 on EvenCycle.

## Written steps reviewed
- **T1 (`hgate` INDEPENDENT).** The thirteen-item checklist is sound, and the census confirms there is no other landed
  pair-carrier predicate. K2-GUARD-1 (item 11) is consistent with both models: each breaks a different one of its two
  invariances.
  - The sources found for `hgate` are restatements: `JointReversible`/`PreservesBody` of the pair slice, P-ACT2, and
    reversibility on the pair state space.
  - The one other source is forbidden: gate-factor idle extension.
  - The classification is fair.
- **T2 (CONS, OQ1, SECT, PREC suffice).** The written replacement of each consuming step is consistent with the source
  scan: the proof reads `hgate` and `hinv` only at (L), (BS) and Lemma R → (BD). The Lean is UNBUILT, and the audited
  theorem itself is [D].
- **Lemma O** (no σ-invariant weakening both suffices and holds in M_max). The argument is a rigorous impossibility for
  its class, and its ingredients are confirmed.
- **B1.4** (`hgate` constrains the pre-locals, which C never reads). Confirmed by M_pre and M_DD. It agrees with my
  derivation in the C audit: an NClass gate preserves Q3 only when the pre- and post-orientation are both even.
- **GT-COMP ⟺ SECT, classed a restatement.** The fields of GT-COMP are SECT's two halves, so the classification is
  consistent with the protocol. Contrast thread C's N2, which is stated without cones or inequalities.

## Verdict for integration
- **`hgate`.**
  - Relative to certified L: INDEPENDENT, by two valid countermodels (M_max and M_D13).
  - Sufficient principles: none independently motivated. Those found are restatements or forbidden.
- **Weaker consumed clauses (CONS, OQ1, SECT ⟺ GT-COMP, PREC).**
  - Sufficient relative to H0 [W over D; UNBUILT], and strictly weaker than `hgate`.
  - INDEPENDENT of certified L.
  - No independent motivation found.
  - Lemma O: any sufficient clause that holds in M_max must read the post-local orientation.
- **Hidden assumption exposed:** `hgate` constrains the pre-locals, which the conclusion never reads. So `hgate` as
  stated is stronger than the theorem needs (M_pre: `hgate` fails, H0 and C hold).
- **Not established:** a physically motivated, non-restating source for the gate's action on the pair cone. On the
  certified record this is a K2 item: the composite cone together with local and gate actions compatible with it.
