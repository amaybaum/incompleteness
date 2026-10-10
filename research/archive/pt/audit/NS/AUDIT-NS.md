# Coordinator's audit of review thread NS — the supplied Navier–Stokes / horizon / OI analysis

Audited: `pt/audit/reviews/NS/RESULT.md`, sha256 `8485f4f77ecb5485bc110e2d8ee59174de312b5ce42ab7423cddc031eb5f190e`
(572 lines); `NOTES.md` `f34b4314…`; `.start_marker` `31fcb2d4…`. The directory holds 24 entries, as RESULT §7 lists.
Protocol: `pt/audit/stage3-inputs/PROTOCOL-NS.md` (`4f61891f…`). Input: `NS-INPUT.md` (`d8c5a1b3…`, manifest OK from
its own directory). The thread ran 12:36:14Z–13:23:37Z, in parallel with the end of U and X and with their audits; it
read none of them.

## Integrity
- **Coordinator's check, 13:25Z**: six `pt/` manifests OK; `ns.manifest.sha256` OK; `pt/base` HEAD `9f9f8257…`, clean,
  no bytecode; the seven protocol hashes unchanged (`239dc123 b41aa0e7 2a2f78f3 38603692 086a4cb8 1a649168 4f61891f`).
- **Hashes.** All 10 script/output hashes of RESULT §6 match the files; every `.err` is `exit 0`.
- **The start marker** was written first into an empty directory (12:36:14Z). NS's end sweep (13:22:23Z, rerun
  13:23:37Z) found nothing newer than the marker outside `pt/U/`, `pt/X/`, `pt/audit/`; `pt/` itself unchanged since
  11:23:27Z (U's `mkdir`). Consistent with the coordinator's record.
- **Observation NS recorded**: `pt/audit/U`, `pt/audit/NS`, `pt/audit/X` appeared during its run. All three are the
  coordinator's audit directories (U's replay directory 12:59Z then AUDIT-U 13:14Z; `pt/audit/NS/indep_checkNS.py`
  13:21Z; AUDIT-X 13:22Z). Accounted; not read by NS; not an anomaly.
- Reads and writes as the protocol requires; no breach found or recorded.

## Replays
Run as `python3 -I -B` from `pt/audit/NS/replay/` (scripts copied; none reads argv or `pt/base`):

| script | checks | replay stdout |
|---|---|---|
| `ns2_hb3_recheck` | 12/12 | identical |
| `ns4_scaling` (run 2) | 14/14 | identical |
| `ns5_null_model` (run 2) | 19/19 | identical (ran 3.6 min) |

The two kept failed runs (`ns4_scaling.run1`: a sympy simplification left `erf + erfc` unreduced, verdict withheld;
`ns5_null_model.run1`: the thread's own preregistered Liouville claim was false on the odd subspace, verdict withheld,
amendment written into the run-2 header) were not re-executed; their records are consistent with RESULT §6 and
NOTES. The second is a genuine preregistration error caught by the thread's own rule, not a harness defect; the
withheld verdict and the explicit amendment are the correct handling.

## Independent check (no thread code)
`indep_checkNS.py` (`756d5e5f…`), written from the protocol's questions and the input before NS's result was read:
**24/24 CONFIRMED**, `INDEP-NS-CONFIRMED`; replay byte-identical. Run 1 (kept as `indep_checkNS.run1.*`, 23/24) failed
at my own A5: the profile's `|f|²` depends on `z`, and the supremum over `z` had not been taken (harness); the fix
evaluates at `z = 0`, where `e^{−2z²}` is maximal. Every other line of runs 1 and 2 is identical.

- **A, the scaling family** (profile `f = curl(0,0,e^{−|x|²})`, the same as NS's): divergence-free preserved;
  `‖u_ε‖₂² = ‖f‖₂² = √2π^{3/2}/2` exactly for symbolic `ε`; `a = 3/2` is the unique `L²`-preserving exponent
  (`‖ε^{−a}f(·/ε)‖₂² = ε^{3−2a}‖f‖₂²`); `‖f‖_∞ = √(2/e)`; `‖u_ε‖_∞ → ∞`; `‖∇u_ε‖₂² = ε^{−2}‖∇f‖₂²`; countercontrol: the
  Navier–Stokes exponent `a = 1` sends the energy to 0. Agrees with NS §2.1–2.2 (S0–S6, CC1–CC3).
- **B, finiteness**: at each `ε = 1/n` the observed values form a finite set with an exact bound growing like
  `ε^{−3/2}`; countercontrol: with an `ε`-independent normalisation the same finite systems are bounded by 1
  uniformly. So the boxed non-uniformity is a property of the continuum normalisation `P_ε`, not of finiteness or
  reversibility — the same conclusion as NS's F1/F2 (§2.3), reached from the other side.
- **C, the Burgers null model**: the characteristic solution satisfies the PDE symbolically; `u_x(0,t) = −1/(1−t)`;
  the characteristic map is a diffeomorphism for `t < 1`; energy `π` conserved; the `N = 1` truncation is frozen; the
  `N = 2` and `N = 3` odd Galerkin truncations conserve energy exactly (`b₁′ = b₁b₂/2`, `b₂′ = −b₁²/2`, the ODE NS
  solves in closed form); the slope bound `√(N(N+1)(2N+1)/6)‖b‖` diverges with `N`; countercontrol: energy does flow
  into mode 2 from the data `−sin x`. Agrees with NS §3.1 (B1–B5, G1, G4, G5, [W] for general `N`). NS's exact `N = 2`
  solution `a₁ = −sech(t/2)`, `a₂ = −tanh(t/2)` was checked by hand against this ODE: it satisfies both equations, the
  energy `sech² + tanh² = 1`, and the gradient `a₁ + 2a₂ ∈ [−√5, −1]` (the maximum of `sech + 2 tanh` is `√5`).
- **D, HB3-a**: from the configurations recorded in `hb3a_gas_values` (HexLatticeGas.lean:875–889), the block charges
  of `c` and `c′` agree on every block at `t` (`w₀ + w₃` on block `(0,0)`) and at `t − 1` (`w₃` on `(0,0)`, `w₀` on
  `(1,0)`) for symbolic channel weights, and at `t + 1` the momentum `P₁` on block `(0,0)` is `1` versus `0`; the mass
  on block `(1,0)` differs too; countercontrol: the mass on block `(0,0)` agrees; the recorded images conserve mass
  and momentum (HB1). This recomputes the arithmetic of the kernel theorem from its recorded data; it does not
  replace the [K] status (no Lean was rebuilt), and it agrees with NS's `ns2` A1–A5.

## Anchors spot-checked at L
- Literature: `git grep -il` for Burgers, Galerkin, Bredberg, "cosmic censorship", "membrane paradigm",
  "fluid/gravity", Minwalla, Damour: 0 files each. Strominger: only Structure.md:1456 (dS/CFT) and :1458
  (Strominger–Vafa). Mori–Zwanzig: SM.md:246 only. As NS reports.
- Kernel: `mz_identity` OI_Structural_Core.lean:276 and `kernel_equivariant` :292 (NS cites :275 and :291, the
  docstring lines; one-line offset, harmless); `h3a_no_closure` HydroSourceAudit.lean:863 and `h3a_control_L4_closes`
  :875; `hexSubstratum_not_A5` HexLatticeGas.lean:685; `hb3a_block_state_not_closed` :942 and `hb3a_no_closure` :989
  (read in full). PROGRAMME.md:51 and :218 are the only "OpenAI" mentions. GR.md:40 and :597 as quoted.
- The gate (hypothesis L9), the target (L55), control 5 (L75) and PROGRAMME L231 quoted verbatim: match the files.

## Written arguments reviewed
- **The null model's conclusion (§3.1–3.2) — CONFIRMED.** The S1 shape (regular finite approximants, a singular
  continuum limit, a uniform energy bound) is exhibited with nothing hidden, twice: by closed energy-conserving
  Galerkin truncations of a PDE that blows up, and by a fully observed finite bijective family. "Route refuted" is the
  right label under amendment 2; NS is right that it is not INDEPENDENT, since L defines no OI continuum map whose
  certified premises a countermodel could satisfy.
- **Two notions of "hidden" (§3.2, NEW) — CONFIRMED.** The note's S2a defines its hidden sector relative to the map
  (hypothesis L34, L38), which is the Mori–Zwanzig complement; OI's observer-level hidden sector is a different object
  (GR L40–52); the input asserts the second with computations about the first. This is the review's central finding
  and it is correctly placed as an assumption-watch marker on the corpus's own note.
- **Generic non-closure (§1.1(c)) — CONFIRMED.** H-A's `h3a_no_closure` proves exact non-closure for the linear wave
  rule; HB3-a is an instance of the H3 closure gap, as H-E reads it. The input's "pointing in this direction" is
  therefore not supported by the record.
- **Independence from the quantum branch (§1.3) — CONFIRMED.** Results are separable (PROGRAMME L9, L216); the
  shared premise is A5, quoted from H-D's own labels; the only fluid witness fails A5 (kernel anchor verified).
- **Horizons (§1.4) — CONFIRMED.** The input avoids the horizon/singularity conflation and makes the softer one
  (black-hole interior as an OI hidden sector); GR L597 keeps the external observer's partition at the cosmological
  horizon.
- **The decision rule (§3.4) — CONFIRMED as a sound preregistration shape**; it is a proposal for a future round,
  not a result, and NS labels it so. Its CC1–CC3 are exactly what the null model shows to be necessary.
- **Dimensional bookkeeping (§2.4) — CONFIRMED** ([W]; the 2D global regularity remark correctly [L, unverified]).
- **§2.2's energy budget** is standard and correctly scoped to smooth solutions.

## Corrections (wording; no verdict changes)
1. Kernel line numbers for `mz_identity` and `kernel_equivariant` are off by one (docstring versus `theorem` line).
2. §1.6 marker 5 (Structure.md:496 status cell) is a §A.25/§A.30 item for the owner; NS correctly made no edit. It is
   outside this review's question and is passed on as a record-only observation.
3. The verdict table's count (25 / 24 / 2 / 2 / 0 / 13 = 66) tallies.

## Verdict for integration
NS's bottom line stands: the input's corpus paraphrases are faithful but drop the gate; its "precise OI mechanism"
is generic to finite truncations (route refuted, exactly); HB3-a is the generic closure gap, not hidden-sector
evidence; Mori–Zwanzig is already a certified corpus theorem; the September 2026 claims are not checkable at L and
nothing depends on them; the framework-specific target T-NS is UNRESOLVED and not statable at L (no continuum map);
the proposed test is not executable at L (four missing objects); nothing in the input changes any corpus label.
What to keep: the forcing and dimension caveats, and the attribution-or-not shape run under §3.4's controls.
