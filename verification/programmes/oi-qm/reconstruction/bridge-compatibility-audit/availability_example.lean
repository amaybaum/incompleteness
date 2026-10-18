/- Research-only design check: instantiate the adopted spectator theorem.
   No new axiom, named theorem, or import into the adopted OIBridge library. -/
import OIBridge.BridgeFiniteProtocol

open OIBridge InterventionLocality BridgeFiniteProtocol ReferenceExtension

noncomputable section

example (k : ℕ) :
    InstAvail fullClass (Fin 2 × Token) Unit
      (fun _ => amplRefL (Fin 2) (stopped (attempt balancedCircuit) k)) :=
  finite_protocol_spectator
    fullClass_arch
    fullClass_contextStable
    fullClass_labelInvariant
    (Fin 2)
    balancedCircuit (by trivial)
    balancedCircuit_isometry
    (fun _ => by trivial) (fun _ => by trivial) k
