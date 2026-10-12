# Finite channel protocol — prospective successor to the #807 design repair

Owner authorization: ChatGPT, 2026-10-12T04:24:46Z, "Ok let's proceed as suggested";
parallel work explicitly requested at 2026-10-12T05:10:00Z.
Certified main base: f2415108601a9c36bb985b3374c56f0eb34c2962.
Measured design parent: #807, 13ad14a1ba2973245354aea7790c021d946b1ff0.
The existing #807 one-run preregistration and one-line diff remain the completed historical record.

## Scope and decision rules, before the first new computation and CI

Construct the stopped finite protocol with InstAvail's existing readout, op, bind, coarse and
discard rules, including the maximally mixed ancilla and its internal pure reset. Prove every
finite depth is available from primitive readout/reset/circuit/correction inputs. Derive the
closed form from the constructed branches. No AvailableChannelApproximation witness is assumed.

Every finite computation uses Gaussian rationals. Controls cover the actual uniformly attached
ancilla, each reset branch, normalization, the gate circuit, the corrected outcome maps and the
stopped loop. A failed control suppresses the computational verdict. Countercontrols remove the
reset, remove the correction, and continue after success; each must disagree with the intended
map on a named matrix unit. Finite computations establish only their checked cases.

The Lean module counts as built design evidence only after Build succeeds and all fourteen
declared axiom reports contain only propext, Classical.choice, Quot.sound. No sorryAx is allowed.
The CI budget is at most three sequential fresh-head design runs. Retain each tested head,
its errors and its actual result before correcting proofs and starting another run.
The new PR targets the measured disposable #807 repair branch; it is neither a main landing
nor a native F/E attestation. Its release gate is expected to stop at the manuscript census
for thirteen unadopted design modules. Establish the actual scope from the logs.

## Invariant checkpoints

| Invariant | Checkpoint |
|---|---|
| The pure seed comes from uniformly attached ancilla | reset_uniformAttach and exact physical-reset calculation |
| Availability is constructed, not supplied as an all-k witness | instAvail_attempt, instAvail_stopped, finite_protocol_available |
| Failure continues and success stops | bind/coarse definition and stop countercontrol |
| Exact O14 branch and all-k formulas | attempt_balanced_branch and balanced_stopped_formula |
| Explicit finite primitive resources | hCircuit, hReset, hCorrect and architecture projector field |
| Spectator extension names actual prerequisites | finite_protocol_spectator, ContextStable and LabelInvariant |
| All named Lean statements are genuine proofs | actual Build plus fourteen standard axiom reports |
| #807 and shared maxCone modules unchanged | prospective path allowlist and remote compare |
| Pair-cone validity is not inferred from matrix positivity | source audit I4.38/I4.66 and result review |
| Closedness enters only any later limit passage | no limit or availability closure theorem in this module |

## Premise source audit

I4.38 validity_of_implementationLocality and I4.66 CompositeOperationalValidity refer to
positive semidefinite matrices at the matrix carrier. Their definitions do not assert
preservation of an arbitrary identified pair cone. #807's channelTransfer_of_identified_stateSpace
requires its pair-validity hypothesis separately; at the kernel's PSD space identification
with that space is K = Q3. Applying that fact to an arbitrary K would assume the reconstruction
target. Context stability I4.29 and label invariance I4.30 extend availability to a spectator;
they do not identify the state cone or establish preservation of it.

The primitive circuit is the O14 balanced Hadamard/Toffoli/quarter-phase circuit on the token
and two ancilla qubits. Its rational table and exact isometry are checked. Class membership of
that circuit, reset permutations and correction remains explicit. A theorem that derives all
those memberships for MixR {pi/4}, and the channel convergence and arbitrary-cone transfer
theorems, are further obligations; they are not claimed by this constructor package.
