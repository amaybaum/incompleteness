# SC-42 — kinematics and structure of Theorem 4's operational theory (PR-B, part)

Base: `main` at `0d917665`. Branch: `corpus/sc42-operational-kinematics`.

## Findings corrected

| ID | Source | Finding |
|---|---|---|
| CON-15 (with R-10 stage 2) | `intro-corpus-audit-20261026/consistency.json` | No manuscript states that the operational-completion characterization (Theorem 4) assumes complex matrix kinematics. |
| B-B8 | `FULL-CORPUS-AUDIT-60c976fe-B.md`, confirmed in part by `-VERIFY.md` | Same gap, read off the kernel: `FiniteOperationalTheory` is stated over `Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ` and over `A × Fin n` at each ancilla level. |
| CON-48 | `consistency.json` | GR §3.3's setting omits structure fields of the kernel theory. |
| B-O6 | `FULL-CORPUS-AUDIT-60c976fe-B.md`, confirmed by `-VERIFY.md` | The preparation closure rule `prepAvail_post` admits only a single-outcome (deterministic) follow-on operation. |
| CON-09 | `consistency.json` | GR:330 "Part I delivers QM on a finite-dimensional Hilbert space." |
| CON-14 | `consistency.json` | Main frames the operational layer as an open lifting problem at :99, :210, :348 and the conclusion (:770 here; :758 at `eae01647`). |

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

No field imposes positivity, trace preservation or complete positivity (condition (i) supplies
validity), and no field extends a system operation to a composite (condition (iii) supplies that).
The kinematics assumption is therefore: the system's state space is the full complex matrix algebra
`M_A(ℂ)` on its configuration index set, operations are ℂ-linear maps on it, and the composite with an
`n`-level ancilla is the matrix algebra on the product index set, `M_A(ℂ) ⊗ M_n(ℂ)`. The typed
interface (`TypedOperationalTheory`, `OIBridge/TypedCompletion.lean`) and the OI⁺ and
implementation-class forms carry the same kinematics. `verification/ROADMAP.md` P1 records its
derivation from field-neutral premises as OPEN (K3 and K1 conditional, K2, K∞ and Kₙ open).

## Claims, one by one

Each entry: the original claim (file:line at base `0d917665`), its defect, the correction, and the
downstream consequences.

1. **GR:216 — the setting of Theorem 4.**
   - *Original:* "Fix a nonempty finite visible system and an operational theory on it: a specification, for the system and for every finite ancilla level, of which finite outcome families of linear maps are available, closed under coarse-graining and outcome-conditioned composition, with a spectator-independent local readout of the ancilla."
   - *Defect:* the complex matrix kinematics is assumed and not stated (CON-15, B-B8); the identity rule, the preparation predicate with uniform attachment and its single-outcome closure (B-O6), discard, and the restriction of composition to the ancilla levels are not stated (CON-48), although GR:276 calls attachment and discard "already present in the finite operational framework".
   - *Correction:* the kinematics is stated as an assumption, with its derivation open; the thirteen fields are stated as six rules (a)–(f), with `FiniteOperationalTheory` and `readout_is_localLuders` cited; absence of positivity and of system-to-composite extension among the rules is stated. Checked field by field by `check_sc42.py` [1]; against the base text the same check fails (countercontrol, `check_sc42.countercontrol.out`, 18 failures).
   - *Downstream:* the theorem line GR:218 is unchanged (checked [2]; coverage fingerprint of `GR:T-operational-completion-characterization` unchanged, K3 kept). R-10 stage 2 of the Introduction can now cite [GR §3.3] for the kinematics item. The GR:276 typed-form back-reference ("the closure rules already used above") now resolves.
2. **GR:330 — CON-09.**
   - *Original:* "Part I delivers QM on a finite-dimensional Hilbert space."
   - *Defect:* Part I establishes the fixed-basis unitary/Born representation ($S\iff D\iff Q_{\mathrm{fb}}$); the operational theory is reached only under conditions (i)–(v).
   - *Correction:* "Part I delivers an exact fixed-basis unitary/Born representation of the observer's finite-horizon law on a finite-dimensional Hilbert space; the full operational theory of instruments on that space is obtained exactly when the completion conditions of §3.3 hold."
   - *Downstream:* §6.1's QFT step uses the Hilbert space and its tensor decomposition, not the instrument algebra; no further GR change.
3. **Main:352, Main:558 — Theorem 4 restated.**
   - *Original:* "…an operational theory's available outcome families on the system and on every ancilla level are exactly the normalized finite Kraus instruments…" (352); "…the operational theories whose available families on the system and on every ancilla level are exactly the finite Kraus instruments…" (558).
   - *Defect:* kinematics unstated; "every ancilla level" where the kernel's `ExactCompositeQuantumOps` and GR state every positive level.
   - *Correction:* kinematics clause with its open derivation; "every positive ancilla level".
   - *Downstream:* none beyond the mirrors below.
4. **Main:578, Main:640 — status of the characterization.**
   - *Original:* "…so what remains is orientation and the physical question of which conditions the substratum supplies, not the size of the family and not a lifting theorem." (578); "exact finite operational quantum mechanics is *characterized conditionally*, under the explicit completion principles of [GR §3.3]…" (640).
   - *Defect:* the list of what remains omits the kinematics derivation; the conditional characterization omits the kinematics among its conditions.
   - *Correction:* "within the complex matrix kinematics it takes as given …; what remains is orientation, the physical question of which conditions the substratum supplies, and a derivation of that kinematics"; 640 adds "within complex matrix kinematics taken as given".
   - *Downstream:* same sentence pattern at Methodology:45 and Explainer:379, corrected below.
5. **Main:99, :210, :348, :770 — CON-14.**
   - *Original:* "interventions (classical comb closed, §3.4; quantum instruments open)" (99); "…is a separate bridge, partially established by the one-step coherence theorem of §3.2 for the lattice realization and otherwise open." (210); "*Level three (open):* coherent preparation, noncommuting interventions, and the instrument algebra — the operational bridge (§3.2 checklist)." (348); "It is the remaining operational-lifting problem, not a defect in the exact stochastic–quantum equivalence proved here." (770).
   - *Defect:* the layer is characterized exactly (§3.4 Remark at 578 says "not a lifting theorem"); what is open is which conditions the substratum supplies and the kinematics derivation.
   - *Correction:* each site states the characterization (five completion conditions, within complex matrix kinematics taken as given, none supplied by bare finite OI) and that the substratum's supply of the conditions is open; 770 adds the kinematics derivation as open. The negative result stays scoped as Main §3.4 scopes it (finite reversible read-write dynamics does not itself generate state mixing); no site extends it.
   - *Downstream:* Main:550 and :594 used the same "operational-lifting problem" framing and are corrected (claim 6); book mirrors in claim 8.
6. **Main:550, :594 — paraphrases of CON-14.**
   - *Original:* "exact coherent/composite compatibility is the residual operational-lifting problem" and "The residual operational-lifting problem is instead a question about…" (550); "the remaining question (route (ii)) is the operational-lifting problem: which additional structure makes one controlled family … a single standard local quantum operational theory." (594).
   - *Defect:* contradicts 578 ("not a lifting theorem"); the question at 594 is answered on a fixed finite carrier by the characterization.
   - *Correction:* 550 states that compatibility holds exactly under the five conditions, within the kinematics; 594 states that the question is characterized on a fixed finite carrier by the five conditions. "local" is dropped at 594: the characterization concerns one carrier and its ancilla composites, not spatial locality.
   - *Downstream:* 594's dangling "route (ii)" pointer is removed; Main:596 ("What remains is selection — route (ii).") is untouched.
7. **Methodology:45; Explainer:58, :379, :381 — restatements.**
   - *Original:* "it is equivalent to the framework's core together with explicit added principles, none of which bare observation incompleteness supplies." (M:45); "on a finite carrier it follows exactly when five further operational conditions hold" (E:58); "it holds exactly when the five completion conditions hold, none of them supplied by embedded observation alone." (E:379); "the coherent preparations, noncommuting instruments, and composites of one OI system form one standard quantum operational theory exactly when five operational conditions hold" (E:381).
   - *Defect:* kinematics unstated.
   - *Correction:* a kinematics clause at each; M:45 and E:379 also state that its derivation is open.
8. **Book: ch01:165, ch09:42, ch19:10, ch19:126, glossary:107, with FULL:509, :2522, :5170, :5286, :6707.**
   - *Original:* "the coherent preparations, transformations, and measurements of one OI system and its composites form one standard quantum instrument algebra exactly when five operational conditions hold" (ch01:165); "and the operational instrument algebra still open ([Main §3.4])" (ch09:42); "while the coherent operational extension remains open (§19.2.12)" (ch19:10); "…the physical question is which of those conditions the substratum supplies." (ch19:126); "That residual common coherent/composite lift is the narrowly stated frontier." (glossary:107).
   - *Defect:* kinematics unstated (ch01, ch19:126); CON-14 framing (ch09, glossary); ch19:10 contradicts the chapter's own status line at ch19:126 and ch00:101 ("characterized by five named conditions").
   - *Correction:* kinematics clause at ch01:165 and ch19:126 (the latter with its open derivation); ch09:42 and glossary:107 state the characterization; ch19:10 states the split status as ch19:126 does. FULL carries each line verbatim (checked [4]).

## Site table

| Site (base line) | Was | Now | Source |
|---|---|---|---|
| GR:216 | setting: linear maps, coarse-graining, composition, local readout | kinematics stated as assumption, derivation open; six rules (a)–(f) = the 13 fields | `FiniteOperationalTheory`; ROADMAP P1 |
| GR:330 | "delivers QM" | fixed-basis representation; operational theory under §3.3's conditions | Main §3.4; GR §3.3 |
| Main:99 | "quantum instruments open" | characterized by five conditions within the kinematics, sourcing open | GR §3.3 |
| Main:210 | "partially established … otherwise open" | characterized; one-step coherence for the lattice realization; sourcing open | GR §3.3; Main §3.2 |
| Main:348 | "Level three (open)" | "Level three (characterized conditionally)" | GR §3.3 |
| Main:352 | restatement, "every ancilla level" | kinematics clause; "every positive ancilla level" | `ExactCompositeQuantumOps` |
| Main:550 | "residual operational-lifting problem" (×2) | compatibility exactly under the five conditions; "operational question" | GR §3.3 |
| Main:558 | restatement, "every ancilla level" | kinematics clause; "every positive ancilla level" | as 352 |
| Main:578 | what remains: orientation, sourcing | adds the kinematics derivation | ROADMAP P1 |
| Main:594 | "the operational-lifting problem" | characterized on a fixed finite carrier | GR §3.3 |
| Main:640 | "characterized conditionally, under the … principles" | adds "within complex matrix kinematics taken as given" | ROADMAP P1 |
| Main:770 | "remaining operational-lifting problem" | characterized; sourcing and kinematics derivation open | GR §3.3; ROADMAP P1 |
| Methodology:45 | status sentence | kinematics clause, derivation open | ROADMAP P1 |
| Explainer:58, :379, :381 | restatements | kinematics clause (379: derivation open) | ROADMAP P1 |
| ch01:165 / FULL:509 | restatement | kinematics clause | ROADMAP P1 |
| ch09:42 / FULL:2522 | "instrument algebra still open" | characterized, sourcing open | GR §3.3 |
| ch19:10 / FULL:5170 | "extension remains open" | "characterized by five named conditions" | ch19:126 |
| ch19:126 / FULL:5286 | restatement | kinematics sentence, derivation open | ROADMAP P1 |
| glossary:107 / FULL:6707 | "residual … lift … frontier" | characterization stated | GR §3.3 |

## Evidence levels

- Theorem 4 itself: kernel-proved in both directions (`physical_of_exactAll`; `exactAll_of_physical_general`; paired in `exactAll_iff_physical_general`), unchanged in statement and strength.
- The setting's transcription: read off the Lean structure, checked field by field by `check_sc42.py` (prose/status check, not kernel certification).
- The kinematics assumption: a fact about the kernel's types (`Matrix _ _ ℂ`), recorded in ROADMAP P1.
- "Derivation of the kinematics is open": ROADMAP P1, status OPEN (K3, K1 conditional; K2, K∞, Kₙ open).
- The readout form: kernel-derived (`readout_is_localLuders`).

## Re-grep

`check_sc42.out`: stale phrasings ("delivers QM on a finite-dimensional", "quantum instruments open)",
"Level three (open)", "operational-lifting problem", "remains open (§19.2.12)", "instrument algebra
still open", "residual common coherent/composite lift", "on every ancilla level are exactly") 0 each
across the nine files; kinematics mentions 0 at base, 27 at head (GR 1, Main 12, Methodology 1,
Explainer 3, ch01 1, ch09 1, ch19 2, glossary 1, FULL 5).

## Claims made conditional or removed

- Made explicitly conditional: Theorem 4 and every restatement of it, on complex matrix kinematics taken as given. This states an assumption the kernel always had; the theorem's strength is unchanged.
- Removed: GR:330 "delivers QM"; the "open lifting problem" framing at Main:99, :210, :348, :550, :594, :770, ch09:42, ch19:10, glossary:107.

## Lean

No Lean file is changed. No correction here requires a formal change.

## Checked and left unchanged

- GR (i) "every available family sends positive states to positive states…" quantifies over system families too, while `CompositeOperationalValidity` quantifies over the ancilla levels only. Not a flaw: exactness implies validity on the system, and GR's (i) implies the kernel's, so the displayed equivalence holds as stated in both directions.
- "open" for the operational instrument algebra where the sentence says the framework or a route does not deliver it for OI realizations: ch03:168, ch18:16, ch18:72, ch18:76, appendix-b:102, appendix-c:72, appendix-c:80, Explainer:290, Main:650, Methodology:399. These state that sourcing is not established, which is accurate; none restates Theorem 4 or calls it an unsolved lifting theorem. ch18:16, :72, :76 are also rewritten by open PR `corpus/sc22-n-regime`.
- Status cells "characterized by five named conditions" (ch00:101, ch18:52, ch18:333, ch19:64, ch19:340, ch19:341 and mirrors): status idiom, no setting stated.
- ch01:16 ("the one boundary not folded into the theorem…"): accurate, concerns $S\iff D\iff Q_{\mathrm{fb}}$.
- ch03:174 ("coherent-lifting problem", PBR composites): a different claim class (composite product law); not changed.
- `papers/Introduction.md`: left to r32 (its L114/L214 carry B-B8 and B-O6; R-10 stage 2 now has a GR anchor).

## Rest of PR-B: out of scope here

CON-10, CON-11, CON-12, CON-13, CON-16, CON-29, CON-44, CON-45, CON-46, CON-47 (Main:624-type
directional-witness display), CMP-17 (Introduction).

## Cross-unit dependencies

Shared statements this unit changes, which other units (SC-34 … SC-41) or open PRs may rely on:

- The definition of Theorem 4's setting (GR §3.3, :216) and the phrase "every positive ancilla level" at Main:352, :558.
- The kinematics clause as the canonical statement of the assumption (GR:216), and its open status (ROADMAP P1).
- The three-status sentence (Main:640, Methodology:45, Explainer:379).
- The removal of "operational-lifting problem" from Main (:550, :594, :770) and of "open" framing at Main:99, :210, :348, ch09:42, ch19:10, glossary:107.
- Same-line overlaps with open PRs (text conflicts, different clauses): `corpus/sc33-bell-main-book` at Main:558; `corpus/sc29-kernel-scope` at ch01:165, ch19:126, Explainer:381, FULL:509, FULL:5286; `corpus/sc17-explainer-bell` at Explainer:58. Each is resolved by keeping both changes. Generated `.tex`/`.pdf` for GR, Main, Methodology, Explainer and the book also overlap and are regenerated after merge.

## Open research question for #970

ROADMAP P1 (K): derive the complex matrix kinematics that Theorem 4 takes as given — the number
field, the matrix-algebra state space and the tensor-product composite — from operational premises
that presuppose none of them, or isolate the minimal premises from which it follows.

## Checks

- `python3 -I check_sc42.py` (from the repository root): OK, output in `check_sc42.out`; countercontrol `--setting-from 0d917665` fails as required (`check_sc42.countercontrol.out`).
- `tools/release_gate.py`: every step passes except `lean-axioms` (needs the local Lean toolchain).
- `tools/coverage_check.py`: OK, 128 canonical statements; no fingerprint moved.
- `tools/lean_manuscript_census.py`: OK, 211 cited identifiers (209 at base; `FiniteOperationalTheory` and `readout_is_localLuders` added and resolved); registry unchanged.
- `verification/lean/edge_rigidity_probe.py`: all checks pass.
- Builds: GR 88, Main 97 (96 at base), Methodology 54, Explainer 70, book 558 pages; median characters per page 3177, 3291, 3094, 2941, 3045 (base 3179, 3273, 3094, 2909, 3045).
