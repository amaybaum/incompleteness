# Track B act 45 — the fixed-basis image of a single-time lift: RESULT

**Outcome:** `A45-BRIDGE-PROVED`

For a trivial-ancilla admissible dilation `pad U` of a visible slice `G`, the fixed-basis datum `realData U` — evolution `U`, uniform initial law, identity readout — has root-conditioned trajectory laws determined by `G` alone, also after `permClass` interventions on either side of `U`; its rooted families agree with those of a second such datum exactly when the two slices are equal; and each of its trajectory laws is `Q_fb`-realizable and stochastic, so it lies in the class the landed equivalence `S ⇔ D ⇔ Q_fb` describes. At the product configuration every flat 16 × 16 Hadamard `H` gives the unitary `U_H = H/4`, whose Born weights are `1/16`, the entries of `Γ₀ ⊗ Γ₀`. These are kernel theorems at evidence level 2. The round's probe computes, in exact arithmetic and not in the kernel, that an ancilla carried between steps as hidden basis states separates two dilations of one slice that share every column entering the slice, at two steps, while an ancilla attached as a tensor factor leaves the rooted family equal to `Gᵗ`. This is a statement about the frozen mathematical objects; it recovers no realization's class from its data, adopts no relation, carrier or intervention class as the physical one, and leaves `P0`'s cross-time parts open.

**THE CLAUSE, carried at this mention — the result.**

> Act 45 proves statements about the fixed-basis data that a single-time trivial-ancilla lift instantiates, and adopts none of them as anything but mathematics. A `BRIDGE-PROVED` verdict settles, for trivial-ancilla admissible dilations and the fixed-basis datum with the dilation's unitary as its evolution, a uniform initial law and the identity readout, that the root-conditioned trajectory laws are determined by the visible slice, also after `permClass` interventions on either side, that the rooted families agree exactly when the slices are equal, and that each trajectory law is fixed-basis realizable and stochastic. It recovers no realization's class from its data, proves nothing in the kernel about a nontrivial ancilla, adopts no relation, carrier or intervention class as the physical one, and leaves `P0`'s cross-time parts open; no principle gains physical status by appearing here, and nothing here names, endorses or excludes a selection principle.

## The kernel layer

The module `verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean` at `E` is the reference implementation: reference
blob `9d6086bbe3af28e576adf2fb51784b02a5d66e5f`, module blob at `E` `9d6086bbe3af28e576adf2fb51784b02a5d66e5f`. The two are identical, so no proof departs from the
reference.

It carries the four frozen definitions (`realData`, `pad`, `IsFlatHadamard`, `UH`) and the 27 frozen statements, each
followed by its `#print axioms` line. In the run at `E`'s predecessor, the `Mathlib bridge` built the module (job
109580668417). All 27 of its axiom lines read `[propext, Classical.choice, Quot.sound]`, with no `sorryAx`. They include:

- the verdict `a45_bridge_kernel`, `P_R`;
- the statements the label requires:
  - `bridge_traj`, the trajectory laws after `permClass` interventions on either side;
  - `rooted_eq_iff_slice_eq`, with its forward witness `slice_eq_of_rooted_eq` and its backward witness `visible_congr`;
  - `realData_traj_stochastic`, through the landed `qfbRealizable_rootTraj` and `Qfb_imp_S`;
  - the flat 16 × 16 instance: `UH_unitary`, `UH_norm`, `UH_born_eq_slice`, `UH_admissible` and `flat_bridge`.

The release gate's `lean-axioms` step reports 5278 named results and no sorry: 5251 at `D`, plus these 27.

## The exact-computation layer

The frozen probe `verification/lean/fixed_basis_ancilla_probe.py`, blob `8419549b598131a4bdef36e8c9ce82690cdaac6c`, ran in its own shard,
`Numerical probes / A45 ancilla` (job 109580668489, run 36619408800 at `E`'s predecessor). It reported 16 `PASS`, no
`FAIL`, and the line:

`fixed_basis_ancilla_probe: OK -- 16 checks: six flat realizations of one slice give equal rooted families before and after monomial interventions; carried ancilla separates at two steps; tensor-factor ancilla does not`

The carried-ancilla separation and the tensor-factor invisibility are the probe's exact arithmetic replayed in CI. They
are not kernel statements, and the verdict does not contain them.

## The execution

| stage | commit | run | outcome |
| --- | --- | --- | --- |
| `F` | `524e16ad74f378b5903e30514f95c218668b6709` | 36615421546 | the `check-run` attestation at `F`: twelve jobs green, gate 21 of 21 |
| 1 — controls, probe and shard, module without the verdict, import | `6d18c07e4722122dc3b877ecb891ae58da1d2d37` | 36619165282 | build green; `lean-axioms` 5277, no sorry; the A45 shard green with its `OK` line; the gate red only at `lean-manuscript`, the module being unclassified until stage 3, as frozen |
| 2 — the verdict | `fa55937d63917956446a18acf06be7f93c3f309d` | 36619224682 | build green; `lean-axioms` 5278, no sorry; the A45 shard green; the gate red only at `lean-manuscript`, as at stage 1 |
| 3 — the surfaces | `90f582ea166d43cad9a9cf5a9a4c168a88e68099` | 36619408800 | all thirteen jobs green; the release gate passing all 21 steps — `lean-manuscript`, `staleness` (13 matched, 0 unstamped), `voice`, `claims`, `mirror`, `citation` among them — seventeen receipts holding, the 303 legacy records intact |

At stage 3 the census, the six manuscript insertions and the `P0` sentence were written from `controls.py`'s own
expected-tree functions. Main, the Explainer and the book were rebuilt by `sh ./build.sh Main Explainer` and
`sh ./build.sh --book`, to 87, 67 and 540 pages, with no dropped glyph. The three rebuilt `.tex` are byte-identical to
those of the predicted tree carried by the pre-freeze run 36612901341.

`controls.py --self-test` held at every stage commit, and `legacy_records_check.py` and `v3_verifier.py --receipts` held
locally at each (`C6`). `controls.py check E --freeze F` is `C9`, run on the commit carrying this note.
