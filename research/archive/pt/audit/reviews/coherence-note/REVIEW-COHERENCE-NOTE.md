# Coordinator's review of the supplied note "the specific property OI would need to imply" (2026-10-10)

Reviewed directly by the coordinator against L = `9f9f8257` (`pt/base/`), with the stage-2 audits and the DS review as
background. Not an isolated thread: U and X are running, and a new thread directory would trip their anomaly sweeps.
The note is data; its UI line ("Worked for 2m 21s") is ignored. Exact identities: `povm_identity.py`, 4/4, replay
identical. Evidence levels as in the protocols.

## Verdict table

| id | claim (short) | verdict | anchor |
|---|---|---|---|
| N1 | the property needed is coherence between indistinguishable alternatives, preserved under reversible transformations and detectable through a change of basis | ACCURATE WITH CORRECTION | the corpus already names this as an *added* principle, not an unnamed gap: OI⁺ = OI core + well-formedness + observational independence + **reversible richness** + observer recursion, with `OI⁺ ⟺ exact finite endomorphic operational QM` (Main L564–566; [K] `carrier_general_oiPlus`, CarrierGeneralOIPlus.lean:213); minimal form "phase-free richness — one continuously driven transition and the exchanges of distinguishable states" (Main L568; [K] `oiPlusMin_iff_qm`, MinimalRepertoire.lean:569, root import OIBridge.lean:169) |
| N2 | incompleteness ≠ coherence ≠ interference | ACCURATE | Main L20, L534 (universality); [K] `S_imp_D` realizes every finite law, non-quantum ones included; DS review C53 |
| N3 | OI establishes possible incomplete access but not that it necessarily produces coherence; that is the missing connection | ACCURATE WITH CORRECTION | stronger at L: it is *settled negatively* for the stated architecture — "finite reversible read-write dynamics, even with genuine hidden-memory and readback behavior, does not itself generate quantum state mixing" (Main L568; [K] `readWriteSourced_not_qm`, ReadWriteControl.lean:174); phases and nonclassical control INDEPENDENT (ROADMAP L1399–1400, L1412–1414) |
| N4 | p(x) = ρ_LL M_LL + ρ_RR M_RR + 2 Re[ρ_LR M_RL] | ACCURATE | [X] I1: `tr(ρM)` for Hermitian ρ, M |
| N5 | if either ρ_LR or M_RL is zero the cross term disappears | ACCURATE | [X] I2 |
| N6 | not knowing the path does not make either nonzero | ACCURATE | the certified Q_fb representation has collapse at every step in a fixed basis (Equivalence.lean:207–214): effects diagonal in the record basis, so M_RL = 0 identically ([X] I3) — the stronger statement |
| N7 | a which-path record multiplies the coherence by the overlap of the record states; orthogonal records kill it; "exactly the relationship the stage-2 CNOT analysis reproduced" | ACCURATE WITH CORRECTION | [X] I4 (pure records); mixed records use γ = tr(U_L†U_Rρ₀) (DS §2 F3); the CNOT instance is AUDIT-DS F1–F2 |
| N8 | the closest existing OI principle is C4 | ACCURATE WITH CORRECTION | C4 as stated (Main L80: "two visible histories with the same current state induce different next-step laws, mediated through the hidden state") is the closest *core* condition; but the closest *existing* principle is OI⁺'s reversible richness (N1), which the corpus adds explicitly and labels as not entailed by bare OI (Main L568: "not a claim that bare OI entails the added principles") |
| N9 | C4 alone is insufficient: classical memory without interference | ACCURATE | DS's CL0m carries a C4 witness and violates the quantum two-path bound [X ds7_models B8]; Main L568 [K] |
| N10 | the ROADMAP identifies phases and nonclassical control as independent of the present architecture | ACCURATE | ROADMAP L1392–1414 (the link in the note points at `main`; the rows are identical at L) |
| N11 | the bridge diagram (embedded observation → composition/self-duality → unique cone → coherent preparation, phase evolution, recombination → double slit) | ACCURATE WITH CORRECTION | one conflation: the single-system interference term (the note's own formula) needs single-system coherence and a basis-changing effect, which the *pair* cone of stage 3 does not touch; the composite enters for the record, the eraser and Bell-type readouts (AUDIT-DS §4). The single-system ball is taken as given in the K programme, its substratum sourcing open (S2 D1; ROADMAP K∞) |
| N12 | cone uniqueness would give the state/effect geometry under its hypotheses, not the physical supply of preparations, phase transformations and screen measurements | ACCURATE | matches PROTOCOL-STAGE3's scope and DS §3(a); Origin (H3's source) is Priority 2, queued |
| N13 | the decisive missing theorem is the physical sourcing of phase-sensitive operational coherence from embedded observation; cone uniqueness is a step, not the theorem | ACCURATE | and the corpus states the minimal form of what must be sourced: one continuously driven transition (Main L568, `oiPlusMin_iff_qm`) — so the target can be posed as sourcing *that single operation*, which is sharper than "coherence" in general |

## What the owner should take from the note
- The three-way distinction (incompleteness / coherence / interference) and the two-factor structure of the cross
  term, `ρ_LR` and `M_RL`: both must be nonzero, and the certified representation supplies neither (N6).
- The record-overlap law as the exact point of contact with the certified pair data (N7).
- The ordering: cone uniqueness (stage 3) is geometry; sourcing the coherent operations is a separate theorem (N12, N13).

## What to correct
- "The missing connection" is not unnamed: the corpus already isolates it as OI⁺'s reversible richness, in minimal form
  one continuously driven transition, proved *not* to follow from read-write dynamics with hidden memory (N1, N3, N8).
  The research question is therefore the Origin question for that one operation, not the discovery of what to source.
- The diagram's single chain conflates the single-system interference (independent of stage 3) with the composite parts
  (the record, the eraser, Bell) that stage 3 governs (N11).

## Not claimed
- No label changes. Nothing here is kernel-checked beyond the cited [K] anchors. No corpus file was edited.
