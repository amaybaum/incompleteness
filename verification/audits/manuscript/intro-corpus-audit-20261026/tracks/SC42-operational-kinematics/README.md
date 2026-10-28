# SC-42 — kinematics and structure of Theorem 4's operational theory (PR-B, part)

Base: `main` at `0d917665`. Branch: `corpus/sc42-operational-kinematics`, five commits: the
correction, the revision answering the independent review of the first, the round-3 revision
answering the delta review, and the round-4 and round-5 revisions (sections "Round 4" and "Round 5") (section "Round 3" below; it supersedes the texts quoted for GR:330,
Main:212, glossary:21, preface:5, Structure:1119 and Explainer:962 in claims 2 and 6).

## Findings corrected

| ID | Source | Finding |
|---|---|---|
| CON-15 (with R-10 stage 2) | `intro-corpus-audit-20261026/consistency.json` | No manuscript states that the operational-completion characterization (Theorem 4) assumes complex matrix kinematics. |
| B-B8 | `FULL-CORPUS-AUDIT-60c976fe-B.md`, confirmed in part by `-VERIFY.md` | Same gap, read off the kernel: `FiniteOperationalTheory` is stated over `Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ` and over `A × Fin n` at each ancilla level. |
| CON-48 | `consistency.json` | GR §3.3's setting omits structure fields of the kernel theory. |
| B-O6 | `FULL-CORPUS-AUDIT-60c976fe-B.md`, confirmed by `-VERIFY.md` | The preparation closure rule `prepAvail_post` admits only a single-outcome (deterministic) follow-on operation. |
| CON-09 | `consistency.json` | GR:330 "Part I delivers QM on a finite-dimensional Hilbert space." |
| CON-14 | `consistency.json` | The operational layer framed as an open lifting problem: Main:99, :210, :348, the conclusion (:770 here; :758 at `eae01647`), and its paraphrases corpus-wide. |
| review of the first commit | independent review, REVISE | GR's condition (i) quantified over system families, so the cited (ii)-witness `systemLoose` failed it as well; Main:210 omitted the $w<\kappa$ criterion; further CON-14 paraphrases. |

## What the kernel assumes (read first)

`FiniteOperationalTheory A` (`verification/lean-mathlib/OIBridge/OperationalAssembly.lean`), for a
finite type `A` with decidable equality, has exactly these thirteen fields:

- `avail`: availability of finite outcome families of ℂ-linear maps `Matrix A A ℂ → Matrix A A ℂ`;
- `availExt n`: the same on `Matrix (A × Fin n) (A × Fin n) ℂ`, for every `n : ℕ`;
- `avail_id`: the single-outcome identity is available on the system;
- `avail_coarse`, `availExt_coarse`: closure under coarse-graining of outcome labels, on the system and at every level;
- `availExt_bind`: feed-forward composition, an available family followed by outcome-dependent available families, at every ancilla level (not on the system);
- `prepAvail n`: availability of preparation maps `Matrix A A ℂ → Matrix (A × Fin n) (A × Fin n) ℂ`;
- `prepAvail_uniform`: `ρ ↦ ρ ⊗ I/(n+1)` is an available preparation at every level `n+1`;
- `prepAvail_post`: an available preparation followed by an available single-outcome (`Unit`) operation is an available preparation;
- `readout`, `readout_avail`, `readout_local`: at each level an available `Fin n`-outcome family whose `k`-th branch is spectator-independent over the rank-one Lüders selector, `Φ_k(X ⊗ Y) = X ⊗ P_k Y P_k`; its form on all matrices is derived (`readout_is_localLuders`);
- `prepAvail_discard`: available preparation, then an available family at that level, then the partial trace over the ancilla, gives an available family on the system.

No field imposes positivity, trace preservation or complete positivity, and no field extends a
system operation to a composite. The kinematics assumption is therefore: the system's state space is
the full complex matrix algebra `M_A(ℂ)` on its configuration index set, operations are ℂ-linear maps
on it, and the composite with an `n`-level ancilla is the matrix algebra on the product index set,
`M_A(ℂ) ⊗ M_n(ℂ)`. The typed interface (`TypedOperationalTheory`, `OIBridge/TypedCompletion.lean`)
and the OI⁺ and implementation-class forms carry the same kinematics. `verification/ROADMAP.md` P1
records its derivation from field-neutral premises as OPEN (K3 and K1 conditional, K2, K∞ and Kₙ
open).

Condition (i) in the kernel is `CompositeOperationalValidity` (`OIBridge/OperationalValidity.lean`):
for every `n`, every family available under `availExt n` is branchwise positive and trace-summing.
It does not quantify over `avail`, the system families. This matters for the independence claim:
the witness for (ii), `systemLoose` (`OIBridge/LevelOneSeam.lean`), makes every system family
available, including the trace amplifier `X ↦ 2X` (`systemLoose_amplifier_available`), so it fails a
system-level (i) and satisfies the kernel's.

## Claims, one by one

Each entry: the original claim (file:line at base `0d917665`), its defect, the correction, and the
downstream consequences.

1. **GR:216 — the setting of Theorem 4 and condition (i).**
   - *Original:* "…is settled by a characterization with no external premise. Fix a nonempty finite visible system and an operational theory on it: a specification, for the system and for every finite ancilla level, of which finite outcome families of linear maps are available, closed under coarse-graining and outcome-conditioned composition, with a spectator-independent local readout of the ancilla. … (i) *Valid probabilities*: every available family sends positive states to positive states and its outcomes' traces sum to the input trace."
   - *Defect:* the complex matrix kinematics is assumed and not stated (CON-15, B-B8). The setting omits the identity rule, the preparation predicate with uniform attachment and its single-outcome closure (B-O6), and discard, and it does not say that composition is postulated only at the ancilla levels (CON-48). GR:276 itself calls attachment and discard "already present in the finite operational framework". Condition (i) quantified over system families as well, unlike `CompositeOperationalValidity`. With that stronger (i), the cited witness `systemLoose` fails both (i) and (ii), so `five_way_minimality` does not establish (ii)'s independence as GR stated it. The first commit wrongly recorded this as not a flaw; the review's finding is correct and verified against the Lean above. "No external premise" overstated the theorem's premises once the kinematics is counted.
   - *Correction:* the kinematics is stated as an assumption whose derivation is open. The thirteen fields are stated as six rules (a)–(f), citing `FiniteOperationalTheory` and `readout_is_localLuders`, and the setting says that no rule imposes positivity or extends a system operation to a composite. Condition (i) now reads "(i) *Valid probabilities*: at every ancilla level, every available family sends positive states to positive states and its outcomes' traces sum to the input trace." "With no external premise" becomes "with no premise beyond its stated setting". `check_sc42.py` [1] checks all of this field by field and against the kernel definitions. The same check fails against the base text and against the first commit's text (the countercontrols).
   - *Downstream:* the theorem line GR:218 is unchanged (checked [2]), and the coverage fingerprint of `GR:T-operational-completion-characterization` is unchanged, K3 kept. Both directions still hold with the ancilla-level (i), which is the kernel's, and `five_way_minimality` now applies verbatim. No other manuscript glosses (i): Main, the Explainer, the book and FULL name it only ("valid probabilities"), so nothing else changes. R-10 stage 2 of the Introduction can now cite [GR §3.3] for the kinematics item. The GR:276 typed-form back-reference ("the closure rules already used above") now resolves.
2. **GR:330 — CON-09.**
   - *Original:* "Part I delivers QM on a finite-dimensional Hilbert space."
   - *Defect:* Part I establishes the fixed-basis unitary/Born representation; the operational theory is reached only under conditions (i)–(v).
   - *Correction:* "Part I delivers an exact fixed-basis unitary/Born representation of the observer's finite-horizon law on a finite-dimensional Hilbert space; the full operational theory of instruments on that space is obtained exactly when the completion conditions of §3.3 hold."
   - *Downstream:* §6.1's QFT step uses the Hilbert space and its tensor decomposition, not the instrument algebra; nothing else in GR changes.
3. **Main:352, Main:558 — Theorem 4 restated.**
   - *Original:* "…([GR §3.3], kernel-verified with no external premise): for every nonempty finite visible system, an operational theory's available outcome families on the system and on every ancilla level are exactly the normalized finite Kraus instruments…" (352); "…the operational theories whose available families on the system and on every ancilla level are exactly the finite Kraus instruments…" (558).
   - *Defect:* the kinematics is unstated. Both say "every ancilla level" where the kernel's `ExactCompositeQuantumOps` and GR say every positive level. "No external premise" has the same defect as at GR:216.
   - *Correction:* a kinematics clause with its open derivation; "every positive ancilla level"; at 352, "kernel-verified, with no premise beyond its stated setting".
4. **Main:578, Main:640, Methodology:45 — status of the characterization.**
   - *Original:* "…so what remains is orientation and the physical question of which conditions the substratum supplies, not the size of the family and not a lifting theorem." (578); "exact finite operational quantum mechanics is *characterized conditionally*, under the explicit completion principles of [GR §3.3]…" (640); "it is equivalent to the framework's core together with explicit added principles, none of which bare observation incompleteness supplies." (M:45).
   - *Defect:* the kinematics derivation is missing from what remains, and the kinematics is missing from the conditions.
   - *Correction:* each sentence adds the kinematics as given, and 578 and M:45 add its derivation to what is open.
5. **Main:99, :210, :348, :770 — CON-14.**
   - *Original:* "interventions (classical comb closed, §3.4; quantum instruments open)" (99); "…is a separate bridge, partially established by the one-step coherence theorem of §3.2 for the lattice realization and otherwise open." (210); "*Level three (open):* coherent preparation, noncommuting interventions, and the instrument algebra — the operational bridge (§3.2 checklist)." (348); "It is the remaining operational-lifting problem, not a defect in the exact stochastic–quantum equivalence proved here." (770).
   - *Defect:* the layer is characterized exactly (Main:578 says "not a lifting theorem"). What is open is which conditions the substratum supplies, and the derivation of the kinematics.
   - *Correction:* each site states the characterization: five completion conditions, within complex matrix kinematics taken as given, none supplied by bare finite OI. Each says that which conditions the substratum supplies is open. 210 keeps the lattice result with its criterion, "non-entanglement-breaking one-step coherence for the linear lattice realization under the $w<\kappa$ criterion" (as at Main:348; added on review). 770 adds the kinematics derivation as open. The negative result stays scoped as Main §3.4 scopes it.
6. **CON-14 paraphrases, corpus-wide (§A.25).** A re-grep for "lifting problem", "operational lifting", "operational-lifting", "lifting debt/result/frontier", "active-lifting", "open coherent operational lift" and "stated as open (§3.2" found these. Each is replaced by the characterization, with the substratum's supply of the conditions open:
   - Main:82 (`MAIN:T-statement`, a SUM row): "(4) Full operational extension: identifying one common *standard local quantum instrument/composite theory* … requires the additional operational-lifting and composition hypotheses stated in §3.4. Bell is a separate constraint rather than one of those lifting hypotheses". The theory is now obtained exactly under the five conditions, and Bell is "rather than one of those conditions". "local" is dropped, because the characterization concerns a carrier and its ancilla composites, not spatial locality. The ledger fingerprint was re-affirmed (`70572f0b3e1aa833` → `a7e85ca32a645bc5`), with the same ID and level SUM unchanged.
   - Main:212: "Those are the narrowly stated operational-lifting conditions of §3.4." → "Whether they do is characterized, on a finite carrier with complex matrix kinematics taken as given, by the five completion conditions of §3.4 ([GR §3.3])."
   - Main:550: "…is the residual operational-lifting problem. This residual problem is not the exponent question…" → compatibility holds exactly under the five conditions; "Which of those conditions hold is an operational question, not the exponent question of §3.1"; and "The residual operational-lifting problem is instead…" → "The operational question is instead…".
   - Main:594: "the remaining question (route (ii)) is the operational-lifting problem: which additional structure makes … a single standard local quantum operational theory." → "the additional structure that makes … a single quantum operational theory on a fixed finite carrier is characterized, within complex matrix kinematics taken as given, by the five completion conditions of [GR §3.3]."
   - Main:618: "For the operational-lifting route" → "For the operational-reconstruction route" (the name Main:352 uses for that route).
   - Main:650, Methodology:399, ch03:168 / FULL:1044: "stated as open" / "Main states as open" → "characterized conditionally and with its physical sourcing open".
   - GR:70: "touches the open coherent operational lift" → "touches the coherent operational completion, which §3.3 characterizes by completion conditions whose physical sourcing is open."
   - Structure:1119; Substratum:14, :323: "part of the operational-lifting frontier", "the narrower operational-lifting statement explicitly scoped in [Main]", "remains the narrower operational-lifting statement of [Main §3.4]" → the equality holds, on a finite carrier with the kinematics taken as given, exactly under the five conditions, and the substratum's supply of them is open.
   - Explainer:707, :916, :950, :962: "operational-lifting and composition hypotheses", "the separate coherent/composite lifting problem", "coherent/composite lifting and locality conditions", "the explicitly separated lifting problem" → the five completion conditions, within the kinematics, with the substratum's supply open.
   - preface:5 / FULL:76: "what remains to be established … is the simultaneous coherent/noncommuting instrument and composite structure", "the residual operational-lifting step … the still-open active layer" → that structure holds exactly under five completion conditions with sourcing open; "the operational completion conditions exactly where they enter … overstating what the substratum is shown to supply".
   - ch00:55 / FULL:291: "What is not yet claimed as a completed theorem is one common standard local quantum instrument/composite representation … That is the remaining operational-lifting layer" → the reviewer's text (characterized by five completion conditions; sourcing open).
   - glossary:21 / FULL:6621: "What remains is the **operational lifting** problem: prove that…" → the reviewer's text.
   - ch01:185 / FULL:529, ch01:197 / FULL:541: "do not yet prove … That residual is an active-lifting statement" and "this operational-lifting debt" → the equality holds exactly under the five conditions with sourcing open; ":197" now names the conditions where the paragraph introduces the lift, and Bell is "not one of those completion conditions".
   - ch02:12 / FULL:655, ch02:20 / FULL:663; ch03:174 / FULL:1050, ch03:186 / FULL:1062; ch04:92 / FULL:1211; ch14:76, :78 / FULL:3754, :3756: "still-conditional operational-lifting step", "narrower operational-lifting statement", "belonging to the coherent-lifting problem", "coherent/composite lifting result", "operational-lifting qualification", "the operational-lifting question" → stated through the five completion conditions. At ch03:174 the claim is sharpened: the tensor-product composite is part of the kinematics the characterization assumes, and deriving it is open.
7. **Explainer:58, :379, :381; ch01:165 / FULL:509; ch19:126 / FULL:5286 — restatements.** A kinematics clause is added at each, with the derivation open at E:379 and ch19:126.
8. **ch09:42 / FULL:2522; ch19:10 / FULL:5170; glossary:107 / FULL:6707.** "the operational instrument algebra still open", "the coherent operational extension remains open (§19.2.12)" (which contradicted ch19:126 and ch00:101), and "That residual common coherent/composite lift is the narrowly stated frontier." now state the characterization.

## Round 3 (delta review, ACCEPT WITH CHANGES)

Two errors in round-2 wording, both checked against the kernel before correcting. The theorem
(`ExactFiniteEndomorphicQuantumOps`, `OIBridge/KrausSoundness.lean`: `T.avail (Fin m) F ↔
IsFiniteEndomorphicKrausInstrument F`, and the composite form `ExactCompositeQuantumOps`) is about an
operational theory's available families on the carrier `A` and on the composites `A × Fin (k+1)`. The
composites' carrier, and so the tensor-product composite `M_A ⊗ M_n`, is fixed by the types of
`FiniteOperationalTheory` (`OperationalAssembly.lean`) and `CompositeOperationalValidity`
(`OperationalValidity.lean`); no condition of `PhysicalCompletionConditions`
(`PhysicalCharacterization.lean:295`) concerns it. Local tomography of that composite is a standard
property of complex matrix algebras (product operators span `M_A ⊗ M_n`), not a kernel theorem.

- **B1, Main:212.**
  - *Was (round 2):* "Whether they do is characterized, on a finite carrier with complex matrix kinematics taken as given, by the five completion conditions of §3.4 ([GR §3.3])."
  - *Defect:* this said that local tomography and tensor-product membership are characterized by the conditions. They are part of the assumed kinematics, as ch03:174 states.
  - *Now:* "The operational-completion characterization ([GR §3.3]) takes the complex matrix kinematics as given, the tensor-product composite and with it local tomography included, and deriving that kinematics is open; within it, whether the available interventions on a finite carrier and its composites are exactly the quantum instruments is characterized by the five completion conditions of §3.4."
- **B2, glossary:21 / FULL:6621.**
  - *Was (round 2):* "…the fixed-basis representation extends to the standard noncommuting instrument/composite algebra exactly under the five completion conditions…"
  - *Defect:* the theorem concerns an operational theory's available instruments, not the fixed-basis representation of the observer's law, which may live on a dilated carrier.
  - *Now:* "What remains is operational: on a finite carrier, within complex matrix kinematics taken as given, an operational theory's available instruments on the carrier and its composites are the standard noncommuting quantum instruments exactly when the five completion conditions of the operational-completion characterization ([GR §3.3]) hold; which of them the substratum supplies, and a derivation of that kinematics, are open."
  - §A.34 directional witnesses for this "exactly when": conditions ⇒ exact is `exactAll_of_physical_general` (`OIBridge/GeneralCarrier.lean:93`); exact ⇒ conditions is `physical_of_exactAll` (`OIBridge/PhysicalCharacterization.lean:301`); they are paired in `exactAll_iff_physical_general` (`GeneralCarrier.lean:100`). `check_sc42.py` [3b] checks both line positions.
- **The same error elsewhere.** I grepped for sites pairing the representation with "exactly under/when" the five conditions, and for sites saying the conditions characterize local tomography or the tensor-product composite.
  - Corrected the same way:
    - **GR:330** (round 1). *Was:* "; the full operational theory of instruments on that space is obtained exactly when the completion conditions of §3.3 hold." *Now:* "; whether an operational theory's available instruments on a finite carrier and its composites are the quantum instruments is a separate question, which §3.3 characterizes, within complex matrix kinematics taken as given, by its completion conditions."
    - **Explainer:962** (round 2). *Was:* "The step from that exact representation class to the full operational theory is characterized separately: …it holds exactly under five completion conditions…". *Now:* "The full operational theory is a separate question from that exact representation class: on a finite carrier with complex matrix kinematics taken as given, an operational theory's available instruments on the carrier and its composites are the standard quantum instruments exactly when five completion conditions hold, and which of them the substratum supplies is open."
    - **Structure:1119** (round 2). *Was:* "; that full coherent observable/instrument structure holds simultaneously across all interventions, … exactly under the five completion conditions…". *Now:* "; whether an operational theory's available instruments on a finite carrier and its composites are exactly the quantum instruments, simultaneously across all interventions, is a separate question, characterized within complex matrix kinematics taken as given by the five completion conditions of the operational-completion characterization [GR §3.3], and which of them the substratum supplies is open."
    - **preface:5 / FULL:76** (round 2). *Was:* "the simultaneous coherent/noncommuting instrument and composite structure of standard quantum mechanics holds, … exactly under five completion conditions". *Defect:* the composite structure is in the kinematics. *Now:* "; within complex matrix kinematics taken as given, the tensor-product composite included, an operational theory's available instruments on a finite carrier and its composites are the coherent/noncommuting instruments of standard quantum mechanics exactly when five completion conditions hold ([GR §3.3]), and which of them the substratum supplies is open."
    - **Explainer:375** (pre-existing). *Was:* "a common local tensor/composite instrument structure is part of the coherent operational lift, characterized in Main §3.4 and GR §3.3 by five operational conditions." *Now:* "but they do not supply a common local tensor/composite instrument structure: the characterization of Main §3.4 and GR §3.3 takes the tensor-product composite as part of the complex matrix kinematics it assumes, and within that kinematics characterizes by five operational conditions which instruments are available."
  - Recorded as correct, because the subject is the instruments, interventions or completion of an operational theory and not a representation or the composite kinematics:
    - Main:210, "the operational completion … holds exactly under five completion conditions";
    - Main:82, :550; Substratum:14, :323 (equality or compatibility of instrument theories, not the composite's tensor structure);
    - ch00:55, "one common standard quantum instrument/composite representation for every coherent intervention": a representation of interventions by instruments, confirmed in the delta review;
    - ch01:197, "lift the whole coherent intervention and composite hierarchy into one compatible quantum instrument theory";
    - Explainer:707; ch19:126 and the "five named conditions" status cells.
- **Optional uniformity, applied.** "within complex matrix kinematics taken as given" is added at ch02:12 / FULL:655, ch02:20 / FULL:663, ch04:92 / FULL:1211, ch14:76 / FULL:3754, ch03:186 / FULL:1062, GR:70 and Explainer:950. At Explainer:375 the clause is part of the rewrite above. I skipped none.
- **Reconciliation note (no action now).** These open-PR clauses still carry the lifting phrasing:
  - sc17's ch03:186;
  - sc33's ch00:55, ch04:92, Main:82 and Main:562;
  - sc40's Main:82 (PR #974, head `e27f7866`).

  At reconciliation, SC-42's wording wins in those clauses, `check_sc42.py` is re-run on the merged tree, and `MAIN:T-statement`'s fingerprint is recomputed.
- **Check.** `check_sc42.py` pins the new texts and lists the round-2 texts above as stale. `check_sc42.round3-countercontrol.out` is the output of the round-3 script, at commit `20da13cd`, run on the round-2 manuscripts; it fails on every pin and every old text. It is not regenerated by later scripts. Run on the head, the head script passes.

## Round 4 (review of round 3, ACCEPT WITH CHANGES)

- **Explainer:375.**
  - *Was (round 3):* "…and within that kinematics characterizes by five operational conditions which instruments are available."
  - *Defect:* the theorem characterizes when the available families are exactly the Kraus instruments (`ExactFiniteEndomorphicQuantumOps`, `ExactCompositeQuantumOps`), not which families a theory makes available in general.
  - *Now:* "…and within that kinematics characterizes by five operational conditions when the available instruments are exactly the quantum instruments."
- **Main:638.** Unchanged from base until this round; round 3 recorded it as correct, which was an error.
  - *Was:* "…the instrument algebra is reached exactly when the five operational completion conditions hold ([GR §3.3]; Remark below), none of them supplied by the fixed-basis layer, and…"
  - *Defect:* Theorem 4 restated as "exactly when" without the kinematics (CON-15).
  - *Now:* "…the instrument algebra is reached, on a finite carrier within complex matrix kinematics taken as given, exactly when the five operational completion conditions hold ([GR §3.3]; Remark below), none of them supplied by the fixed-basis layer, and…"
  - §A.34 witnesses: conditions ⇒ exact is `exactAll_of_physical_general` (`OIBridge/GeneralCarrier.lean:93`); exact ⇒ conditions is `physical_of_exactAll` (`OIBridge/PhysicalCharacterization.lean:301`).
  - Main:638 is not a canonical ledger statement; no fingerprint moved.
- **Final grep.** I searched for "exactly when", "exactly under", "if and only if", `\iff`, "precisely those", "exactly the normalized/finite Kraus" and "equivalent to", next to the five conditions or operational QM.
  - Corrected:
    - **Main:648.** *Was:* "reached exactly under the operational completion conditions (§3.4; [GR §3.3])". *Now:* "reached, on a finite carrier within complex matrix kinematics taken as given, exactly under the operational completion conditions (§3.4; [GR §3.3])".
    - **Main:580** (the OI⁺ restatement). *Was:* "On every nonempty finite carrier these three principles are respectively equivalent…". *Now:* "On every nonempty finite carrier, within the same complex matrix kinematics, these three principles are respectively equivalent…".
    - **ch19:264 / FULL:5424.** *Was:* "*conditionally*: it holds exactly when the explicit completion principles hold". *Now:* "*conditionally*: within complex matrix kinematics taken as given, it holds exactly when the explicit completion principles hold".
    - **GR:216 (setting).** Added: "The OI⁺, primitive-source, substratum-source, layer-flow and typed forms below are stated over the same kinematics, the typed form over the complex matrices of every finite carrier." This covers the restatements at GR:240, :246, :256, :260, :262, :266, :268, :276 and :278. Those forms are stated in the kernel over `FiniteOperationalTheory` (`CarrierGeneralOIPlus`, `MinimalRepertoire`, `StructuralClosure`, `DerivedQ3`) and over `Matrix S S ℂ →ₗ Matrix S' S' ℂ` (`TypedOperationalTheory`).
  - Recorded with reason:
    - **GR:218** (the theorem line) and **GR:226** (the boxed equivalence) restate Theorem 4 directly under the setting paragraph GR:216, which states the kinematics. The theorem line is kept byte-identical (checked [2]).
    - **Main:352, :558; Explainer:58, :379, :381; ch01:165, ch19:126 / FULL** carry the clause earlier in the same sentence or at the head of the paragraph that restates the forms.
    - **Main:582, :584; Explainer:381; ch01:165, ch19:126** (the OI⁺, primitive-source, substratum-source, typed and layer-flow restatements) sit in the paragraph whose opening carries the kinematics clause; Main:580 now carries it for the OI⁺ box.
    - Main:20, :586, :596, :610; Explainer:383; GR:282; Substratum:265; SM:14 and the "$S \iff D \iff Q_{\mathrm{fb}}$" and status cells concern other theorems, not Theorem 4.
- **Check.**
  - `check_sc42.py` pins the five new round-4 texts, the GR setting sentence, and the Main:648, :580 and ch19:264 texts.
  - It lists the old texts as stale.
  - `check_sc42.round4-countercontrol.out` is the output of the round-4 script, at commit `07d8b0eb`, run on the round-3 manuscripts; it fails 12 checks. Run on the head, the head script passes.

## Round 5 (review of round 4, ACCEPT; optional notes applied)

- **Main:580** (the OI⁺ paragraph).
  - *Was (round 4):* "On every nonempty finite carrier, within the same complex matrix kinematics, these three principles are respectively equivalent, on the relevant class, to inert spectators, sufficient reversible control, and iterated composition; hence".
  - *Defect:* "on the relevant class" left the side conditions of two of the three converses unstated.
  - *Now:* "Within the same complex matrix kinematics, observational independence is equivalent to inert spectators on every finite carrier; reversible richness implies sufficient reversible control, and conversely for well-formed theories on a nonempty carrier; observer recursion implies iterated composition, and conversely when the identity and the relative ancilla readout are available at every level, which sufficient reversible control and inert spectators supply. Hence, on every nonempty finite carrier," followed by the unchanged display $\mathrm{OI}^{+}\iff$ exact finite endomorphic operational QM.
  - Per-direction kernel witnesses (§A.34), read from the statements:

    | Principle | ⇒ (no side condition) | ⇐ (with its hypotheses) |
    |---|---|---|
    | observational independence ⟺ inert spectators | `observationalIndependence_iff_inert` (`CarrierGeneralOIPlus.lean:75`), an unconditional iff on every finite carrier | same theorem |
    | reversible richness / sufficient reversible control | `control_of_reversibleRichness` (`CarrierGeneralOIPlus.lean:127`), any finite carrier | `reversibleRichness_of_control` (`:148`), hypotheses `[Nonempty A]` and `WellFormed T` |
    | observer recursion / iterated composition | `closure_of_observerRecursion` (`CompletedOI.lean:332`), unconditional | `observerRecursion_of_closure` (`CompletedOI.lean:392`), hypotheses: the identity available at every level (`hid`) and the relative Lüders readout at every level pair (`hread`), supplied by `availExt_id_of_control` (`AncillaClosure.lean:174`, from control) and `availExt_relativeReadout` (`AncillaClosure.lean:231`, from inert spectators); `observerRecursion_iff_closure` (`CompletedOI.lean:401`) is the iff under `hid` and `hread` |

    "Nonempty carrier" enters only in the richness converse and in the final equivalence (`oiPlus_iff_qm`, under `variable [Nonempty A]`). It is needed there because the drift is the matrix unit at a chosen base point. The other directions hold on every finite carrier.
  - Mirrors: no other manuscript states the per-principle equivalences. GR:230–236 lists each principle with its kernel theorems and states observer recursion "under the identity and relative-readout operations used by the construction". GR:242 says "corresponds", which asserts no unconditional equivalence. Explainer:381, ch01:165 and ch19:126 state only the OI⁺ box. Nothing else changes.
- **README.** The countercontrol files above now name the script and commit that produced them.
- **Check.** `check_sc42.py` pins the new Main:580 text and lists "on the relevant class" and "these three principles are respectively equivalent" as stale. It also asserts each witness's hypotheses directly from the Lean source. `check_sc42.round5-countercontrol.out` is the head script run on the round-4 manuscripts; it fails the two stale texts and the pin. Main:580 is not a canonical ledger statement, and no fingerprint moved.

## Site table

| Site (base line) | Was | Now | Source |
|---|---|---|---|
| GR:216 | setting: linear maps, coarse-graining, composition, local readout; (i) over all families; "no external premise" | kinematics stated, derivation open; rules (a)–(f) = the 13 fields; (i) at every ancilla level; "no premise beyond its stated setting" | `FiniteOperationalTheory`; `CompositeOperationalValidity`; `systemLoose_amplifier_available`; ROADMAP P1 |
| GR:70 | "open coherent operational lift" | completion characterized in §3.3, sourcing open | GR §3.3 |
| GR:330 | "delivers QM" | fixed-basis representation; operational theory under §3.3's conditions | Main §3.4; GR §3.3 |
| Main:82 | "operational-lifting and composition hypotheses" | five completion conditions, sourcing open; ledger fingerprint re-affirmed | GR §3.3 |
| Main:99 | "quantum instruments open" | characterized by five conditions within the kinematics, sourcing open | GR §3.3 |
| Main:210 | "partially established … otherwise open" | characterized; lattice coherence under $w<\kappa$; sourcing open | GR §3.3; Main §3.2 |
| Main:212 | "operational-lifting conditions of §3.4" | characterized by the five conditions | GR §3.3 |
| Main:348 | "Level three (open)" | "Level three (characterized conditionally)" | GR §3.3 |
| Main:352 | restatement, "every ancilla level", "no external premise" | kinematics clause; "every positive ancilla level"; "no premise beyond its stated setting" | `ExactCompositeQuantumOps` |
| Main:550 | "residual operational-lifting problem" (×2) | exactly under the five conditions; "Which of those conditions hold is an operational question" | GR §3.3 |
| Main:558 | restatement, "every ancilla level" | kinematics clause; "every positive ancilla level" | as 352 |
| Main:578 | what remains: orientation, sourcing | adds the kinematics derivation | ROADMAP P1 |
| Main:594 | "the operational-lifting problem" | "the additional structure that makes … is characterized" | GR §3.3 |
| Main:618 | "operational-lifting route" | "operational-reconstruction route" | Main:352 |
| Main:640 | "characterized conditionally, under the … principles" | adds "within complex matrix kinematics taken as given" | ROADMAP P1 |
| Main:650 | "stated as open" | "characterized conditionally and with its physical sourcing open" | GR §3.3 |
| Main:770 | "remaining operational-lifting problem" | characterized; sourcing and kinematics derivation open | GR §3.3; ROADMAP P1 |
| Methodology:45, :399 | status sentence; "Main states as open" | kinematics clause; characterized conditionally, sourcing open | ROADMAP P1; GR §3.3 |
| Structure:1119; Substratum:14, :323 | "operational-lifting frontier/statement" | five completion conditions, sourcing open | GR §3.3 |
| Explainer:58, :379, :381 | restatements | kinematics clause (379: derivation open) | ROADMAP P1 |
| Explainer:707, :916, :950, :962 | lifting hypotheses/problem | five completion conditions, sourcing open | GR §3.3 |
| preface:5 / FULL:76 | "remains to be established", "still-open active layer" | characterized; sourcing open | GR §3.3 |
| ch00:55 / FULL:291 | "remaining operational-lifting layer" | reviewer's text | GR §3.3 |
| ch01:165 / FULL:509 | restatement | kinematics clause | ROADMAP P1 |
| ch01:185, :197 / FULL:529, :541 | "active-lifting statement", "lifting debt" | five conditions; Bell not one of them | GR §3.3 |
| ch02:12, :20 / FULL:655, :663 | "operational-lifting step/statement" | five completion conditions | GR §3.3 |
| ch03:168, :174, :186 / FULL:1044, :1050, :1062 | "stated as open", "coherent-lifting problem", "lifting result" | characterized conditionally; the tensor composite is in the assumed kinematics | GR §3.3; ROADMAP P1 (K2) |
| ch04:92 / FULL:1211 | "operational-lifting qualification" | "operational-completion qualification", where the five conditions hold | GR §3.3 |
| ch09:42 / FULL:2522 | "instrument algebra still open" | characterized, sourcing open | GR §3.3 |
| ch14:76, :78 / FULL:3754, :3756 | "the operational-lifting question" | characterized by the five conditions, sourcing open | GR §3.3 |
| ch19:10 / FULL:5170 | "extension remains open" | "characterized by five named conditions" | ch19:126 |
| ch19:126 / FULL:5286 | restatement | kinematics sentence, derivation open | ROADMAP P1 |
| glossary:21 / FULL:6621 | "**operational lifting** problem: prove that…" | reviewer's text | GR §3.3 |
| glossary:107 / FULL:6707 | "residual … lift … frontier" | characterization stated | GR §3.3 |

## Evidence levels

- Theorem 4 itself: kernel-proved in both directions (`physical_of_exactAll`; `exactAll_of_physical_general`; paired in `exactAll_iff_physical_general`). Its statement and strength are unchanged.
- The setting and condition (i) as transcribed: read off the Lean structure and `CompositeOperationalValidity`, checked by `check_sc42.py` (a prose/status check, not kernel certification).
- The (ii)-witness's system amplifier: kernel (`systemLoose_amplifier_available`).
- The kinematics assumption: a fact about the kernel's types (`Matrix _ _ ℂ`), recorded in ROADMAP P1.
- "Derivation of the kinematics is open": ROADMAP P1, status OPEN.
- The readout form: kernel-derived (`readout_is_localLuders`).

## Re-grep

From `check_sc42.out`:
- Stale phrasings: 0 each across the 22 maintained files. These are the eight from the first commit, plus "lifting problem", "operational lifting", "operational-lifting", "lifting debt", "lifting result", "lifting frontier", "active-lifting", "open coherent operational lift", the three "stated as open" forms, "with no external premise", and the $w<\kappa$-less lattice clause.
- Round-3 stale texts (the six round-2 wordings and the pre-existing Explainer:375 one in "Round 3" above): 0 each.
- Kinematics mentions: 0 at base, 66 at head. By file: GR 3, Main 17, Methodology 1, Explainer 8, Structure 1, Substratum 2, preface 1, ch00 1, ch01 3, ch02 2, ch03 2, ch04 1, ch09 1, ch14 1, ch19 3, glossary 2, FULL 17.
- Surviving "lifting" in papers/ and book/ outside the Introduction: 4, all legitimate. They are Main:558 "rather than as one lifting hypothesis" and Main:578 "not a lifting theorem", both negations, and Structure:599 and :1135, which say "lifting" in the mathematical sense of a unitary dilation.

## Claims made conditional or removed

- Made explicitly conditional: Theorem 4 and every restatement of it, on complex matrix kinematics taken as given. This states an assumption the kernel always had; the theorem's strength is unchanged.
- Narrowed to the kernel's form: GR's condition (i), from all available families to every ancilla level.
- Removed: GR's "Part I delivers QM"; "with no external premise" (GR:216, Main:352); and the "open lifting problem" framing at every site in claims 5, 6 and 8.

## Lean

No Lean file is changed. No correction here requires a formal change.

## Checked and left unchanged

- Sites that say the operational lift is "stated separately", or that a result is "conditional on the coherent operational lift". These are accurate scope statements and do not restate Theorem 4: Explainer:375 (second sentence), :381 (end), Main:702, Methodology:13, :385, :399 (first clause), :403, :405, SM:507, Substratum:397, :431, ch02:188, ch03:168 (first clause), ch03:230, ch04:124, readers-guide:13, appendix-c:42, :50, and their FULL mirrors.
- "the coherent operational lift still to be established" (SM:14, ch18:72, appendix-b:102 / FULL:5869) and "the common coherent operational extension remaining open" (ch18:16). They say the lift is not established for OI realizations, which is accurate. ch18:16, :72 and :76 are rewritten by open PR `corpus/sc22-n-regime`.
- Substratum:139: the finite-predictive-dimension, local-tomography and purification hypotheses belong to reconstructions beyond a fixed finite carrier (Main:558), not to Theorem 4.
- ch00:69 "the operational layer's unique selection stated as open": selection of the relating evolution is open (Main:640).
- Status cells reading "characterized by five named conditions": status idiom; they state no setting.
- `papers/Introduction.md`: left to r32. Its L114/L214 carry B-B8 and B-O6, and R-10 stage 2 now has a GR anchor.

## Rest of PR-B: out of scope here

CON-10, CON-11, CON-12, CON-13, CON-16, CON-29, CON-44, CON-45, CON-46, CON-47 (Main:624-type
directional-witness display), CMP-17 (Introduction).

## Cross-unit dependencies

Shared statements this unit changes, which other units (SC-34 … SC-41) or open PRs may rely on:

- the definition of Theorem 4's setting (GR §3.3, :216), condition (i)'s quantifier (ancilla levels), and "every positive ancilla level" at Main:352, :558;
- the kinematics clause as the canonical statement of the assumption (GR:216), its open status (ROADMAP P1), and "no premise beyond its stated setting";
- the three-status sentence (Main:640, Methodology:45, Explainer:379);
- the removal of the "operational lifting" vocabulary corpus-wide (claims 5, 6 and 8), and the name "operational-reconstruction route" at Main:618;
- `MAIN:T-statement`'s ledger fingerprint.

Same-line overlaps with open PRs. Each is a text conflict in a different clause, resolved by keeping both changes:

- `corpus/sc33-bell-main-book` (#968):
  - Main:82: sc33 changes the Bell clause and keeps "operational-lifting and composition hypotheses". Resolution: keep sc33's Bell text and this correction of the first sentence and of "one of those conditions".
  - `verification/coverage/LEDGER.json` `MAIN:T-statement`: both branches move the fingerprint (sc33 to `2748dd752bdd9f03`, here to `a7e85ca32a645bc5`). After the merge, recompute it from the merged line with `tools/proof_census.py` and re-affirm it; neither value is right for the merged text.
  - Main:558: sc33 drops "settled as"; this unit adds the kinematics clause. Keep both.
  - ch00:55 / FULL:291: sc33 rewrites "not yet claimed" to "not claimed" and keeps "remaining operational-lifting layer". Resolution: keep sc33's Bell edits earlier in the paragraph and this replacement of the last two sentences.
  - ch04:92 / FULL:1211: sc33 edits the Bell text; this unit edits the "operational-lifting qualification" sentence. Keep both.
- `corpus/sc29-kernel-scope`: ch01:165, ch19:126, Explainer:381, FULL:509 and FULL:5286. sc29 edits the infinite-region clause; keep both.
- `corpus/sc17-explainer-bell`:
  - Explainer:58: sc17 edits the Bell clause. Keep both.
  - ch03:186 / FULL:1062: sc17 rewrites the sentence and keeps "belongs to the coherent/composite lifting result". Resolution: apply this unit's phrase replacement to sc17's sentence.
- Generated `.tex`/`.pdf` for GR, Main, Methodology, Explainer, Structure, Substratum and the book also overlap. Regenerate them after merge.

## Open research question for #970

ROADMAP P1 (K): derive the complex matrix kinematics that Theorem 4 takes as given — the number
field, the matrix-algebra state space and the tensor-product composite — from operational premises
that presuppose none of them, or isolate the minimal premises from which it follows.

## Checks

- `python3 -I check_sc42.py`, run from the repository root: OK; output in `check_sc42.out`.
- Countercontrol: `--setting-from 0d917665` fails as required (`check_sc42.countercontrol.out`). The first commit's GR text fails the two new condition-(i) and premise checks.
- `tools/release_gate.py`: every step passes except `lean-axioms`, which needs the local Lean toolchain. The passing steps include `mirror`, `voice`, `claims` and `coverage`.
- `tools/coverage_check.py`: OK, 128 canonical statements; the one fingerprint moved is re-affirmed.
- `tools/lean_manuscript_census.py`: OK, 211 cited identifiers (209 at base); registry unchanged.
- `verification/lean/edge_rigidity_probe.py`: all checks pass.
- Builds, pages and median characters per page, base in parentheses:

  | Document | Pages | Median chars/page |
  |---|---|---|
  | GR | 88 (88) | 3190 (3179) |
  | Main | 97 (96) | 3283 (3273) |
  | Methodology | 54 (54) | 3094 (3094) |
  | Explainer | 70 (70) | 2941 (2909) |
  | Structure | 99 (99) | 2958 (2958) |
  | Substratum | 53 (53) | 3265 (3254) |
  | Book | 559 (558) | 3048 (3045) |
