# OI → QM research programme — Amendment 2: the two-track programme

Status base: `main` at `58a7ef040869bad92daa51a80de283e48d37215a` (post-PR #554, Arc D round 1 closed at RD1).

This is a strategic roadmap amendment to `verification/programmes/oi-qm/PROGRAMME.md`. It is **not** a theorem, audit, preregistration, or execution result. Detailed mathematical status remains controlled by the Lean sources, frozen audits and results, the verification ledger, and the manuscript scope guards. No manuscript, book, bibliography or publication edit is authorized by this amendment.

## 1. What changed, and why the roadmap must change with it

Arc D round 1 is closed at outcome RD1 (`verification/programmes/oi-qm/track-i/arc-d-operational-sourcing/result.md`, merged by PR #554). What it proves, at the scope proved:

- **S1.** Padding by an arbitrary finite ancilla unitary preserves the represented rooted family **exactly**, at every root, outcome and time. Two operator properties are free in consequence — non-monomiality, and relative-phase content that moves the all-ones vector off its ray — so each is exhibited in some representation of every representable family.
- **Consequence 3 and S3a.** At the level of the criterion rather than of the family: the representation-augmented access contains every unitary on every finite carrier, so every resource whose predicate is witnessed by the availability of an admissible finite-unitary conjugation is vacuous under that augmented criterion.

Representational presence is therefore a disqualified ground for any sourcing claim — not as a discipline, but as a theorem, at the scope those results establish and not beyond it.

That result is what makes the present roadmap's strategy too narrow rather than merely incomplete. The roadmap currently treats the Barandes route as closed off by §3.5 and makes Arc D the sole active frontier. The warning in §3.5 is correct and survives this amendment intact. Its **strategic** consequence does not: "representability alone sources nothing" is a statement about representability alone. It is not a statement about a full stochastic-to-quantum correspondence carrying its own hypotheses, its own measurement structure, and its own downstream account of interference, decoherence and entanglement.

Barandes's accepted work frames its construction as an exact correspondence between indivisible stochastic processes and quantum theory, and develops measurement, interference, decoherence and entanglement downstream of that correspondence. A correspondence of that shape may supply operational content that bare representability cannot. Whether it does, and under exactly which hypotheses, is an open question of fact that the programme has never asked at definition level.

## 2. The revised spine: two tracks, neither evidence for the other

The programme's central spine becomes two-track. The tracks share their origin and their endpoint and are otherwise independent.

**Track B — the Barandes correspondence route.**

`OI → observer/hidden realization → rooted transition family Γ → the applicable causal/readback condition → P-indivisibility where applicable → the exact relation to Barandes's indivisibility/division-event definition → verification of every hypothesis of his correspondence → determination of exactly what quantum structure his theorem supplies.`

**Track I — the internal reconstruction route.**

`OI → Arc B classification → Arc C quantum representation → Arc D operational sourcing → Arc E composites/Bell → operational QM.`

The governing rule:

> **Neither track may be used as evidence for the other.** Agreement between them strengthens the result. Disagreement identifies the missing hypothesis, and identifying it is itself a result.

Track I keeps its full value and is not demoted. It is what tells the programme independently which assumptions are doing the work, and Arc D round 1 is the standing demonstration: it established a boundary that no external correspondence theorem could have established for us, because it is a theorem about our own criterion.

Track B is added because it may reach the programme's intended `OI → QM` claim sooner, and because the cost of not checking is asymmetric. If Barandes's correspondence already supplies operational and composite content under hypotheses OI can satisfy, then independently reconstructing that structure first would be strategically backwards.

## 3. Immediate consequence for sequencing

**Further Arc D research is paused** after round 1, pending the definition-level bridge audit below. This is a pause on new Arc D rounds, not a retraction: everything merged by PR #554 stands, and Arc D remains a first-class arc of Track I.

The next research act is a **narrow, definition-level audit**, not a proof attempt. The programme does not yet attempt

`PIndivisible_OI  ↔  Indivisible_Barandes`,

because it has not established what the right-hand side means in the accepted text. Attempting the equivalence before fixing the definition would be preregistering a proof of an unstated proposition.

The audit is preregistered separately as `verification/programmes/oi-qm/track-b/act-01-indivisibility/preregistration.md`, under the same split-PR freeze discipline every audit of this programme uses. Its three anticipated outcome shapes are recorded there rather than here, because which one obtains is a matter of fact and not of strategy.

One of those outcomes deserves flagging at roadmap level, because it would change how a merged claim is described: if the basic correspondence does not require actual P-indivisibility, then P-indivisibility may have been given the wrong logical role — explaining specifically nonclassical or interference behaviour rather than licensing the Hilbert-space correspondence itself. `verification/programmes/oi-qm/track-b/boundary-audit/result.md` already points that way, having found that no primary-source theorem it examined imposes a separate indivisibility hypothesis on the representation route. It is a prior indication, not a finding, and the bridge audit is what would settle it.

## 4. Sequence

1. Arc D round 1 merged. **Done — PR #554.**
2. This amendment, establishing the two-track programme.
3. Freeze the Barandes indivisibility/correspondence bridge audit.
4. Audit the accepted Barandes definition and theorem line by line against the programme's formal objects.
5. Formalize the translation layer in Lean wherever it can be formalized.
6. Only then decide whether Arc D round 2 or Arc E is on the critical path to the main theorem.

Steps 4 and 5 are execution and do not begin before step 3 is frozen and merged.

## 5. What this amendment does not do

- It does not weaken, replace or re-decide any merged result, and it re-opens nothing.
- It does not assert that the Barandes correspondence supplies operational content. That is the question, not the answer.
- It does not identify OI P-indivisibility with any external notion of stochastic indivisibility. The bridge audit exists precisely because that identification is unestablished.
- It does not restore any manuscript claim, and it authorizes no manuscript, book or bibliography edit. §7 rule 11 continues to govern: publication-facing strengthening waits until the formal chain is closed or precisely classified.
- It does not name or adopt a fifth condition.
- It does not change the disposition of any resource. The relative-phase *Additional* verdict of PR #521 and PR #515 stands as merged; the deferred resources named in the Arc D preregistration remain deferred and undecided.
- It does not decide the decisive Arc D question of whether a deeper OI condition sources continuous off-diagonal control. That question is untouched and #540 remains binding.
