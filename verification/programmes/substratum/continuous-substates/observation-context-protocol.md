# SUBSTATE-1 — observation context and the double-slit completion test

**Status: preregistered research protocol and exact reference controls.** This note changes no OI manuscript, premise, theorem classification or operational-quantum status. No new physical construction is asserted. Track issue #1007 and draft PR #1009.

## Question and falsifiable distinction

Can **one and the same** continuous-state OI microdynamics support visible records that are Markov/classical in a passive readout, yet exhibit reproducible interference and composable noncommuting interventions under **specified, physically executable preparations and observation settings**?

The phrase "the observation makes it quantum" is not the hypothesis. A double-slit experiment displays interference when the two alternatives remain coherent, **without** a record that reliably distinguishes them. Acquiring usable which-path information suppresses unconditional interference; an eraser-style measurement can reveal complementary **conditional** interference fringes, without restoring a fringe in the unsorted marginal or enabling signaling. Merely using a more selective readout, or postselecting a subset of runs, does not prove a quantum origin.

The same microdynamics and prior must implement each setting. No setting may be supplied by inserting a chosen abstract quantum gate, wavefunction, Kraus map or Born rule into the OI model. Otherwise a match is a representation, not emergence.

## Controls fixed before native-model construction

Work with a binary path label \(\{L,R\}\), a screen with two ports \(\{0,1\}\) (an exact toy analogue of a fringe/antifringe pair), an optional which-path marker \(\{L,R\}\), and an optional complementary marker readout \(\{+,-\}\). Use *one identical incident source*, one physical time schedule and explicit raw input counts. Record all runs and any loss/abort event; do not silently renormalize successful trials.

| Protocol | Exact coherent-reference **unconditional** counts per incident particle | What is tested |
|---|---|---|
| Both alternatives open, no marker | screen \((1,0)\) | constructive/destructive interference |
| Only left alternative transmitted | \((1/4,1/4)\), loss \(1/2\) | same incident-source baseline |
| Only right alternative transmitted | \((1/4,1/4)\), loss \(1/2\) | independent single-path baseline |
| Both open, path marker stored, not read | screen \((1/2,1/2)\) | decoherence by accessible path information |
| Both open, marker read in path basis | each screen/marker pair \((0,L),(1,L),(0,R),(1,R)\) has probability \(1/4\) | marker record and total marginal |
| Both open, marker read in complementary basis | \((screen=0,marker=+)\) and \((screen=1,marker=-)\) each have probability \(1/2\), other pairs zero | complementary *conditional* fringes; unconditioned screen remains \((1/2,1/2)\) |

These are **benchmark** Born-rule predictions for the standard path-qubit state \((|L\rangle+|R\rangle)/\sqrt2\), a balanced recombiner, and an ideal distinguishable marker. They are not predictions made by OI. Output normalization is deliberately **subnormalized** for one-open-arm settings: closing one arm discards its incoming half, keeping the incident flux fixed. Compare raw counts, not separately normalized surviving subsets.

The coherent benchmark's two-open screen minus the two **subnormalized** one-open screens is \((+1/2,-1/2)\). This nonadditivity is a useful control against a restricted positive fixed-path model in which blocking a path only removes its events; it is **not** a quantum uniqueness witness. Classical waves can interfere, and source-dependent reweighting, path-dependent blocking or uncontrolled loss can also create apparent nonadditivity.

## Competing models and decision rule

Test three different comparison classes explicitly.

**C0 — classical stochastic fixed-path/no-interference control.**
Assign each emitted run a path \(L\) or \(R\). Fix the screen response per path, independently of which other slit is open. Blocking a path merely removes its contributions. The two-open unconditioned screen distribution is the sum of the two single-path *subnormalized* screen distributions. In the balanced benchmark it is \((1/2,1/2)\), not \((1,0)\). A failure of C0 rules out only this *restricted* model, not general classical physics.

**C1 — classical coherent-wave positive control.**
A complex classical amplitude through both paths and a linear recombiner gives the same constructive/destructive port intensities as the coherent reference. Classically correlated wave/marker modes can also mimic some eraser conditional distributions. Therefore **interference alone is insufficient** to infer full operational QM or a unique ontic mechanism. This control MUST be marked PASS for the interference statistics, not incorrectly used as a no-go.

**C2 — native OI candidate.**
Specify an actual invertible (or explicitly justified) microscopic update \(T\), invariant initial measure \(\mu\), finite measurable records \(\pi\), physical setting generator and setting-dependent interventions on the *same* ontology; record their locality, causal order, stored path information and independent spectator behavior. No arbitrary quantum operations are permitted as inputs. Measure the full joint law
\(P(screen,marker,loss\mid settings,preparation)\), including attempt counts and conditioning labels. Run negative controls removing the marker, eraser selector, interference coupling, and any remote or nonlocal interaction. The native model must reproduce the benchmark *as a consequence of its implemented dynamics* and meet the independent noncommuting-control and composite tests below.

**Mandatory no-upgrade / reject rule.**
If only C0 fails while C1 and OI both fit the two-slit intensity, record "interference compatible with classical coherent waves; no quantum completion". If C2 needs freely chosen response distributions, quantum amplitudes or a Kraus-instrument menu to match the tables, label it an external-input reconstruction, NOT a native prediction. If conditioning on a marker or herald secretly changes the incident ensemble, record the selection effect explicitly and FAIL the purported native quantum witness.

## What would genuinely move the full-equivalence frontier

1. **An intervention implemented by the dynamics, not by the readout alone.** Show two independently selectable, composable controls whose effective actions fail to commute even up to a global phase. Passive changes of which column of a fixed probability table is displayed are not operations.
2. **Composition and spectators.** Execute the same controlled protocol with an independently prepared unused subsystem present. Test that the spectator's record remains unchanged and that the joint operation factors appropriately, then compose two controlled experiments without resetting hidden records by decree. Compare to \`GeneralCarrier\`'s independent inert-spectator and iterated-composition conditions.
3. **Distinctive nonclassical witness.** A two-port interference pattern is not enough. Propose a separately controlled single-excitation/correlation or contextuality/Bell experiment and account for detector loopholes and possible classical-wave analogues. Bell settings require the actual locality/measurement-independence/no-signaling controls of Main §3.3/H-Bell.
4. **The other OI commitments.** Check C4 readback and visible recurrence *separately*: a Markov passive context can coexist with a memory-bearing controlled context, but that is to be proven, not assumed. The hidden measure's finite boundary entropy and the cubic gauge-structure controls remain independent obligations.

## Implementation / release boundaries

The companion exact benchmark \`observation_context_probe.py\` tests the arithmetic in the table, its incomplete-trial bookkeeping, three-way comparison and a conditional-vs-unconditional no-signaling guard. It contains **no native OI microdynamics**. Its verdict cannot be promoted to a physical prediction, QM equivalence theorem or Lean certification.

The **first valid native run** requires an explicit realization dossier, rather than guessing a gauge-coupled map: a pinned microscopic \(d=3\) update and prior (separate from the observer-level \(\alpha=1/3\) harmonic lift), finite observer/setting interfaces, evidence of actual reversibility, baseline data, hard-to-vary prediction, and the controls above. A physically meaningful result may be negative; record that result without editing the manuscripts to protect the framework.


## Sourcing audit: why this is F2, not an unproven F1 upgrade

The maintained \`verification/programmes/oi-qm/PROGRAMME.md\`, §1, identifies
**F2 as the active endpoint**. Its existing sourcing audit concludes that
operations available to the *present observer interface* preserve
\`NonnegBounded\`, excluding the required general quantum phase control.
The bare-interface F1 endpoint is retired. Thus "specific observations"
must mean a **specific, new physically sourced observer intervention**
whose existence is independently proved, not the post hoc choice of a
different coarse-graining of the same passive record.

A possible point of contact is the bounded native instrument research in
\`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/\`,
especially \`CURRENT-HANDOFF.md\`, \`EQUIVALENCE-OBLIGATIONS.md\`, and
\`native_vread_v15/REPORT.md\`:

- A native nonlinear old-sign/new-pool product occurs in the retained
  geometry, but masks remain and no selectable gate has been isolated.
- A prepared q10.A value can carry an old sign under specified source
  laws, but q10 is private under the retained observer interface.
- The one-tick whole-V read is negative for that specific construction,
  due to unseen free complement cells; neither the access extension
  nor the required preparation changes are adopted.
- A post-Y selected raw phase has conditional statistics and terminal
  records, but it is not a reusable instrument or the noncommuting
  menu the full protocol requires.

**New native test gate (before making any benchmark comparison).**
For one immutable native-source snapshot, list the actual permitted
preparation, setting, terminal record and outgoing carrier fields.
Determine whether a putative which-path marker and an alternative
complementary read are *both* physically selectable on the same
incident preparation and whether their complete raw histories have
known joint probabilities. If either setting is only a decoder applied
afterward to inaccessible fields, return **BLOCKED: no available
intervention**. Do not compute a Born benchmark from it.

If that availability gate passes in a later construction, run the
raw-count controls above with one fixed initial prior and tracked
success/failure branches. This test specifically targets F2's
missing resource without relabeling an existing restricted passive
observer as a quantum measurement.

No manuscript change or quantum-equivalence status upgrade is
authorized by this sourcing audit.
