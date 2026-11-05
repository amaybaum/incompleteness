# Introduction rewrite — claim map for review

**Purpose.** Reviewer aid for the reader-focused rewrite of `papers/Introduction.md`. It maps every
scientific sentence group of the rewritten text to (a) the claim-inventory id of the planning proposal
and the wording of the Introduction it replaces, and (b) the formal source that supports it. It also
lists every inventory item the rewrite moves, compresses or drops, and the disposition of the ten
separate-correction items F-1 to F-10.

**Authority.** Owner decisions on #918: c.6657998945 (editorial decisions, planning) and c.6658427740
(proposal c.6658252620 accepted with changes; rulings on the nine questions).

**Objects.** Old text: `papers/Introduction.md` at `d9f0a845` (the drafting base; identical to the
landed text at `13ced581` except for the [Main] title updated by #1130). Line numbers `old:N` refer
to that blob. New text: `papers/Introduction.md` at the head of this pull request; `new:N` are its
line numbers. Formal sources were checked at `d9f0a845`.

**Inventory ids** (I-01 … I-84) are those of the proposal posted on #918 (c.6658252620), whose full
inventory table is reproduced in the appendix below.

## 1. New text → inventory → old wording → formal source

| new | sentence group (abridged) | inventory | old wording (abridged) | formal source |
|---|---|---|---|---|
| 1–6 | title; header; date "November 2026" | — | old:1–6 (date October 2026) | owner Q7 |
| 12 | abstract: OI hypothesis with observer-relative finiteness | I-05, I-04 | old:12 "every physical observer is a proper part of a reversible deterministic system, resolves only finitely many visible configurations … the finite models below take the whole system finite, as a posit" | Main §1.2 (Definition, Lemma 1, Remark (status of the early commitments)) |
| 12 | abstract: finite-horizon correspondence, fixed measurement | I-15 | old:12 "At every finite horizon, three classes of law coincide …" | Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence) |
| 12 | abstract: memory stored, capacity | I-26, I-29, I-31 | old:12 "every faithful realization carries the law's conditional memory in its hidden state" | Main §3.4 Theorem (unavoidable hidden predictive memory), Theorem (C3 necessity); Main §1.5 |
| 12 | abstract: shared, independent preparation; non-predictable step; chaining fails somewhere in the cycle | I-42, I-39 | old:12 "In a finite reversible world whose hidden odds are shared by every visible start and drawn independently of it, … P-indivisible somewhere in the recurrence cycle whenever … a visible step is not fully predictable" | Main §2.3, Theorem (history readback + finite recurrence implies indivisibility) and Scope |
| 12 | abstract: representation, not derivation; assumed matrix structure + five conditions; Born exponent not selected | I-51, I-54, I-55–57, I-22 | old:12 "Neither that kinematics nor those conditions follow from bare OI" | GR §3.3; Main §3.4 Remarks |
| 12 | abstract: applications as finite-model results and proposals | I-67–69, I-71–74 | old:12 "OI places the zero-point sum … at different levels … separates conservation … from its accessible recovery" | GR §6.2; [BHa]; GR App. A |
| 16–18 | quantum randomness question; "God plays cards"; analogy disclaimer | I-01 | old:18 (same content) | Book §1.11 (illustration) |
| 20 | two-card swap; hidden card dealt with equal probability, independently; one shuffle = coin toss; two = certainty; memory in face-down card; classical statistics | I-02 | old:20; independence clause added per owner c.6658427740 (old:182 "a face-down burn card b, uniform and independent of x") | Book §1.11 (table; burn card uniform and independent) |
| 22 | three mathematical questions | — | old:22 | — |
| 24 | established vs open summary | I-10, I-51, I-55–58, I-22 | old:34, old:36, old:315–317 | sections 3–4 of the new text, each cited |
| 28–30 | reversible rule; visible/hidden; randomness from partial view; visible law depends on rule, partition, preparation | I-03, I-13 | old:24; old:48 "The visible law of a realization depends on the dynamics, the partition and the initial law" | Main §1.2, Remark (the measure as a realization datum) |
| 32 | OI hypothesis; observer-relative finiteness; whole world not required finite | I-05, I-04 | old:28 "Finiteness of the whole world is the model's posit, not a consequence of embedding" | Main §1.2 Definition, Lemma 1, Remark (status of the early commitments); owner c.6658427740 |
| 34 | finite models (substrata): whole finite, product of visible × hidden, reversible map; finiteness of the whole an assumption; reversible rule a representation motivated by near-unitarity | I-04 | old:26 "The bijection is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited" | Main §1.2, Remark (status of the early commitments) |
| 36 | hidden ≠ unknowable; swap: two readings identify both cards; constant-on-fibre criterion; no physical mechanism | I-06, I-27 | old:28 "a quantity is identified exactly when it is constant on the initial states compatible with the retained record"; old:111 "None of these results supplies a physical storage, preparation or intervention mechanism" | Substratum Prop. 24.5 (written proof); Substratum §4.1 "Memory and opacity are different" |
| 38 | not the uncertainty principle; fixed readout; no uncertainty relation | I-07 | old:28 | Main §3.4 ("The uncertainty relations") |
| 40 | turtles; decoupled deeper layer; coupled layer may change records; regress not shown to end; model, not final description | I-08 | old:30 | Substratum §2 and Theorem 24(iii); Book §3.8 |
| 42 | pattern; realization | I-12, I-14 | old:46 | Main §3.4 |
| 48–52 | three collections S, D, Q_fb | I-14 | old:50–56 | Main §3.4, Theorem (finite-horizon …) |
| 54–57 | S ⇔ D ⇔ Q_fb (the one display) | I-15 | old:62–66 (Theorem 1) | Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); kernel names printed there |
| 59 | scope immediately: finite stretch, one fixed measurement; not full operational QM; possibility, not fact | I-16, I-51 | old:68 "This settles a question of possibility, not of fact"; old:199 | Main §3.4, Remark (what this equivalence does and does not say) |
| 61 | tape + clock construction; [EGGH26 Prop. 13]; independent-prior realization; [EGGH26 Prop. 16]; [LP17] | I-17, I-18, I-20 | old:70, old:72, old:78 | Main §3.4 proof of the equivalence; Theorem (finite-horizon process dilation) and Extension |
| 63 | permutation unitary; Born rule converse; Barandes; Strasberg–García Díaz | I-19, I-20 | old:74, old:78 | Main §3.4 proof |
| 65 | memoryless patterns in all three collections; periodicity limit | I-21, I-23 | old:84, old:88 | Main §3.4, Remark (what this equivalence …); Main §3.4 (L640, "nonperiodic target admits no exact all-time realization") |
| 69 | definition of memory; card game | I-25 | old:94, old:96 | Main §1.5 |
| 71 | owner's register sentence; pushforward, distinguishability, capacity | I-26 | old:98–109 (Theorem 2 and "That is …") | Main §3.4, Theorem (unavoidable hidden predictive memory) |
| 73 | both directions: memory ⇔ every realization carries readout-relevant trace; one realization suffices for the converse | I-29 | old:115–117 (Corollary, "proved on paper [Main §1.5]") | Main §1.5; Main §3.4, Remark (what this strengthens) |
| 75 | keeping the past ≠ memory | I-30 | old:117 | Main §1.5 |
| 77 | capacity $2^{I}$; least memory over deterministic (non-reversible) completions | I-31 | old:119 | Main §3.4, Theorem (C3 necessity); Remark (a variational question) |
| 79 | four-item checklist; fair coin | I-35, I-36 | old:129, old:131 | Main §1.3; Main §2.3, Remark (why (C4) is a separate condition) |
| 83 | weather; card game; P-divisibility | I-38 | old:137 | Main §2.3 |
| 85 | every visible start; one preparation, independent of start; why | I-39 | old:137, old:143, old:145 | Main §2.3, Theorem (history readback …) statement |
| 87 | step-by-step forecast cannot separate forecasts; overlap + return ⇒ no chain; attributions | I-41 | old:149–151, old:167 | Main §2.3, Theorem (overlap and return); [RHP14; BD16; Dou26] |
| 89 | recurrence time; non-predictable step ⇒ failure in cycle; common-endpoint histories; full-support equivalence; zero-probability starts | I-42 | old:141, old:153–157, old:163 | Main §2.3, Theorem (history readback + finite recurrence implies indivisibility) and Scope |
| 91 | property of the rule; accessible stretches short; $X_3=X_0$ example; holds also for window-memoryless records; detectable is memory within reach | I-43, I-44, I-45 | old:159, old:161, old:165 | Main §2.3, Scope; Main §3.4, Remark (a variational question) |
| 93 | parity (XOR): memory without short-stretch failure; full-cycle failure; attributions | I-48 | old:180 | Main §2.3, Scope ("XOR control"); [RHP14 Eq. (15); Dou26 App. A] |
| 99 | representation, not derivation (frame) | I-51 | old:199 | Main §3.4 Remarks |
| 101 | Born exponent not selected | I-22 | old:86 | Main §3.4, Remark (what this equivalence …); [Bar26, Thm 3.1] |
| 103 | relating evolution not selected | I-61 | old:239–245 | Main §3.4, Remark (scope: representability, not selection of the relating evolution) |
| 105 | representation, not explanation; Calvo | I-54 | old:215 | Main §3.4, Remark (representation, not explanation); [Cal26] |
| 107 | three notions distinct; class-limited implication | I-52 | old:203–209 | Main §3.2, Remark (three notions, kept apart); Theorem (CP-indivisibility, framework scope); Remark (scope: P-indivisibility is not quantum non-Markovianity) |
| 111–113 | operational question; assumed matrix and tensor-product kinematics; derivation open; basic rules | I-55 | old:219–221 | GR §3.3 ("A derivation of this kinematics … is open"; rules (a)–(f)) |
| 113–119 | iff five conditions (plain list) | I-56 | old:223–231 (Theorem 4) | GR §3.3, Theorem (operational-completion characterization) |
| 121 | well-formedness vs substantive; independence; coherence-free qubit theory; OI alone ⇏ QM; attributions | I-57, I-60 | old:233, old:235 | GR §3.3 |
| 123 | finite bijective dynamics fails (iv) on ≥ 2 states (quarter phase); open questions | I-58, I-59 | old:233 | GR §3.3, "Substratum-source form" |
| 127 | no fixed finite world reproduces a qubit; factorization proved, unboundedness imported | I-62 | old:249–253 | Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form); [HKLP24; GH03; Mon08; Har04] |
| 131 | Bell setting; CHSH 2 vs $2\sqrt2$ | I-63 | old:257 | [Bel64; CHSH69] |
| 133 | Bell ceiling under stated assumptions; card protocol | I-63, I-50 | old:259, old:195 | Main §3.3, Theorem (Bell ceiling for a screened local completion); Book §1.11 |
| 135 | OI keeps determinism, outcome every run, measurement independence; adopts ontic parameter dependence; lattice obstruction; H-Bell open | I-64 | old:263–265 | Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape); Substratum §3.2 |
| 141 | no fixed-measurement record alone rules out a hidden deterministic account; content is memory; 't Hooft | I-24, I-10 | old:90, old:36 | Main §3.4 |
| 143 | conditional physical reading | I-81 | old:321 | Main §1.2 Remark; Substratum Prop. 24.5 |
| 147 | zero-point sum ~120 orders; cancellation if it gravitates | I-65 | old:269, old:271 | [Wei89] |
| 149 | two levels; uniform shift invisible; familiar part vs OI's addition | I-67 | old:273, old:275 | GR §6.2 ("Descriptive distinction established") |
| 151 | proposal conditional on targeted field equations; residual not computed; Λ input; two completions; G3 open; related work | I-68, I-69, I-70 | old:277–291 | GR §6.2, §8.5; [EvEMU11; KP14; Vol06] |
| 155 | conservation vs recovery; burned letter | I-71 | old:295 | GR App. A (bijectivity); [HP07] |
| 157 | qualitative toy-model separation; maps not derived from substratum; floor; secret sharing | I-72, I-73 | old:297–301 | [BHa] (unpublished finite-model research, on `main` at `verification/programmes/black-hole-information/bh01_access_v1/`); [Sha79] |
| 159 | Page curve conditional on H-scramble, H-decouple, full product shell; H-scramble has no instance for configuration states; what recovery needs | I-74, I-75 | old:303–307 | GR §8.4, App. A.7–A.9; [BHb] |
| 163–171 | open list 1–7 | I-59, I-75, I-82 | old:323–331 | Main §1.3, §3.4, §4.5; GR §2.2, §3.3, §6.2, §8.5, App. A.6, A.7; Book §7.6 |
| 175 | guide: no new theorem; where each result is proved | I-10, I-83 | old:36, old:333 | formal papers as listed |
| 177 | Lean checks named in the formal papers; census and ledger | I-83, I-84 | old:38, old:333–… (Appendix A) | `verification/lean-manuscript-census.json`; `verification/coverage/LEDGER.json` |
| 179 | BH results unpublished finite-model research; code locations; novelty not assessed | I-10, I-73 | old:36, old:335 | [BHa; BHb] |

## 2. Inventory items not carried in the new text

| inventory | content | fate | where it lives |
|---|---|---|---|
| I-11 | conventions ("machine-checked", "proved on paper", "exact probe") | replaced by the established/open paragraph (new:24) and the guide (new:175–179) | formal papers |
| I-18 (detail) | rational kernels; response-table extension | compressed to one clause (new:61) | Main §3.4 |
| I-20 (part) | [Bar26 Thm 3.3] ancilla dilation; [Milz20] omitted-measurement remark | moved | Main §3.1, §3.4 |
| I-27 (part) | $\max(1,N-1)$ stabilization; Lean status of record-fibre core | moved; Lean status F-1 | Substratum Prop. 24.5(ii); #1118 |
| I-32 | Pinsker floor | moved | Main §2.3, Lemma (accessible conditional memory from readback) |
| I-33 | actual-trajectory capacity bound | moved; F-2 | Lean `TrajectoryMemory` (kernel-only); #1118 |
| I-34 | entire-future finite-image bound | moved; F-3 | Lean `FullFutureMemory` (kernel-only); `verification/audits/manuscript/full-future-memory-20261028/`; #1118 |
| I-35 (part) | C2 structural/slow forms; process-form theorem | compressed into new:79 and open item 4 (new:168) | Main §1.3; Main §3.4, Theorem (physical memory: C2, process form) |
| I-37, I-46 | proof-and-source paragraphs | moved | Main §1.5, §2.3, §3.4 |
| I-40 | different-deck example | dropped; principle kept (new:89) | Main §2.3, Scope (general statement); F-6 |
| I-47 | six-hidden-state model | moved | Main §2.4 |
| I-49 | card table protocol table and peek | moved | Book §1.11 (table) |
| I-49 (aside) | anticorrelated cards | omitted (owner Q8) | — |
| I-53 | card table CP-indivisibility and Pauli-twirl classical memory | dropped; F-5 | Main §3.2 (CP part); twirl decomposition has no formal home |
| I-54 (part) | [BLP09; BJA17] backflow remarks | dropped | — |
| I-55 (part) | full availability rules | compressed (new:113) | GR §3.3 |
| I-61 (part) | trivial-ancilla quotient | moved | Main §3.4 |
| I-66 | mismatch ≈ de Sitter entropy (dimensional identity) | omitted (owner Q4) | GR §6.3 |
| I-73 (numbers) | 1,376 of 40,320; 60; 32 | moved (owner Q6) | [BHa] |
| I-76, I-77 | [CE], [CR] coherent constructions | omitted (owner Q5); F-8 | history at `bdcbd32`, `2624d49` |
| I-79, I-80 | established-results and "checked in Lean, not independently reviewed" lists | removed (owner Q3) | formal papers; census; #1118 |
| I-82 (item 5) | "machine checks of the steps of §§2–3 proved on paper" | moved | formal papers state which steps are proved on paper |
| I-83, I-84 | Code/data section; Appendix A Lean inventory | replaced by the guide (owner Q3) | Main and GR kernel citations; census; ledger; `papers/introduction_repro/` kept in place as historical evidence (owner Q9) |

## 3. Separate-correction items F-1 … F-10

| flag | finding | disposition in this rewrite | accountable home |
|---|---|---|---|
| F-1 | Record-fibre core called machine-checked only in the Introduction; Substratum Prop. 24.5 carries no kernel citation and its ledger row is GAP | rewrite cites Prop. 24.5 as a written result only; no machine-check claim | #1118 |
| F-2 | actual-trajectory capacity bound (`TrajectoryMemory`) stated only in the Introduction | omitted | #1118 |
| F-3 | entire-future bound (`FullFutureMemory`) stated only in the Introduction | omitted | #1118 |
| F-4 | "first sentence machine-checked on the actual realization" (`RootedRecurrenceBridge`); Main §2.3 gives a written proof, ledger P | rewrite states the result with Main §2.3's proof and hypotheses; no machine-check claim | #1118 |
| F-5 | Pauli-twirl classical-memory decomposition of the card table stated only in the Introduction | omitted | none needed unless the owner wants it landed (Main §4.5 or Book §1.11) |
| F-6 | different-deck example cited to Main §2.3, which has only the general statement | example omitted; principle kept | — |
| F-7 | conservation-versus-recovery results carried by no formal paper | kept qualitatively, labelled unpublished finite-model research, sourced to [BHa]; numbers moved to [BHa] (owner Q6) | owner decision; [BHa] on `main` |
| F-8 | [CE]/[CR] have no formal paper and are read only from history | omitted (owner Q5); evidence and review obligations stay with their records | owner Q5 |
| F-9 | Egri et al. attribution absent from Main §3.4 | rewrite keeps the attribution (new:61) | separate attribution correction to Main, not authorized here |
| F-10 | `papers/introduction_repro/` supports no statement of the rewritten text | kept in place, untouched; README describes it as historical verification evidence | owner Q9; separate disposition |

## 4. Coverage-ledger supersession

The rewritten text has no bold-headed statements, so `tools/proof_census.py` assigns it no row and the
six `INTRODUCTION:*` mirror rows are removed in the same commit as the text.

| retired row | canonical row it mirrored |
|---|---|
| `INTRODUCTION:T-1` | `MAIN:T-finite-horizon-stochastic-reversible-unitary` (K3) |
| `INTRODUCTION:T-2` | `MAIN:T-unavoidable-hidden-predictive-memory` (K3) |
| `INTRODUCTION:C-unnamed-99fe05c0` | none: Main §1.5 and Main §3.4, Remark (what this strengthens) state it in prose |
| `INTRODUCTION:T-3` | `MAIN:T-overlap-return` (K3) |
| `INTRODUCTION:C-recurrence-cycle-indivisibility` | `MAIN:T-history-readback-finite-recurrence-implies` (P) |
| `INTRODUCTION:T-4` | `GR:T-operational-completion-characterization` (K3) |

**Corollary check (`INTRODUCTION:C-unnamed-99fe05c0`).** The result — memory at a step exactly when
every faithful realization carries readout-relevant hidden memory there — keeps its written proof in
Main §1.5 and in Main §3.4, Remark (what this strengthens), with kernel support for its components
(`pushforward_identity`, `S_imp_D`). No ledger entry other than the retired mirror named it. So that
it keeps an accountable ledger entry, the same commit adds an `unattached` record for it, naming
`OIBridge/HiddenMemory.lean` (`pushforward_identity`) and stating which steps are proved on paper.

## Appendix. Claim inventory (from the planning proposal, #918 c.6658252620)

Line numbers `L…` are `papers/Introduction.md` at `13ced581`; for the body they equal `old:N` above. Columns: **Claim** (short; exact wording quoted where status is delicate) · **Status as stated** · **Formal source** (verified at `13ced581`) · **Fate** (keep = plain words; compress; move = leave to the source; drop = redundant or illustrative only) · **Flag** (F-n = separate-correction item, section D-gaps below).

#### §1.1–1.2 (L14–38)

| id | Claim | Status as stated | Formal source (verified) | Fate | Flag |
|---|---|---|---|---|---|
| I-01 | "God plays cards": deterministic deck, partial view gives uncertainty; "The picture is an analogy … it proves nothing about quantum mechanics" | heuristic | Book §1.11 | keep (opening image, with its disclaimer) | — |
| I-02 | Two-card swap: one shuffle = coin toss, two = certainty; record has memory held in face-down card; "the game's statistics are those of ordinary classical probability" | exact finite model | Book §1.11 (table: 1/2, 1, peek 1/2); Substratum §4.1, "Memory and opacity are different" (after Prop. 24.5) (swap model, $I(X_0;X_2\mid X_1)=1$ bit) | keep (running example) | — |
| I-03 | Bijection loses no information; visible marginal; visible sector evolves stochastically although the whole is deterministic | definition / elementary | Main §1.2 | keep | — |
| I-04 | Model $(S,\varphi,V)$; bijection "motivated by observed near-unitarity"; "finiteness of all of $S$ is posited" | stated posit / representation choice | Main §1.2, Remark (status of the early commitments) — verified (L62 of Main) | keep (essential limitation) | — |
| I-05 | OI = physical hypothesis: every observer is part of a reversible deterministic world, specified readout and preparation, finitely many visible configurations; finiteness of the whole is the model's posit | hypothesis | Main §1.2 | keep | — |
| I-06 | Hidden ≠ unknowable: identified exactly when constant on the initial states compatible with the record; swap game: two readings identify both cards | proved on paper (Substratum); Intro elsewhere says core "machine-checked" | Substratum Prop. 24.5 (paper proof; no kernel citation; ledger `SUBSTRATUM:P-24.5` = GAP "not formalized in Lean") | keep in plain words, cite Prop. 24.5 only; drop the machine-check claim | **F-1** |
| I-07 | Not joint unsharpness: arises for one fixed readout; "no uncertainty relation constrains fixed-readout visible laws" | proved | Main §3.4 ("The uncertainty relations", L594 of Main) | keep (one sentence) | — |
| I-08 | Turtles: an exactly decoupled deeper register adds nothing for this interface [Substratum Thm 24(iii)]; a coupled one may change records; regress not shown to end; "A finite bijection is the model being investigated, not a demonstrated ultimate ontology" | proved (fixed-interface invariance) + scope | Substratum §2 (L50, L54), Thm 24(iii); Book §3.8 | compress to 3–4 sentences, all qualifications kept | — |
| I-09 | Overview: correspondence exact and universal; discriminating content is memory and recurrence | summary | Main §3.4 Remark (what this equivalence does and does not say) | keep (folded into §3 opening) | — |
| I-10 | Contributions: "expository and claims no new theorem"; §§3.2–3.5 proved in [GR], [Main]; HKLP24 imported; §5 "in unpublished research records with exact or exhaustive checks"; "the novelty of the §§3.2–3.3 and §5 results has not been assessed"; prior work [tH14] | status statement | — (self-description) | keep, shortened ("What this paper is") | see F-7 |
| I-11 | Conventions: "machine-checked" / "proved on paper" / "exact probe"; *faithful realization* | convention | — | replace by a 4-line "how to read status words" (proved; conditional; open; proposal; exact computation), Lean named once, pointer to formal papers | — |

#### §2.1–2.3 (L40–90)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-12 | Definitions: law, realization, Markov, order $L$/recurrence, stochastic/permutation matrix, TV distance, CMI | definitions | Main §1.2, §2.3, §3.4 | keep only law, realization, memory, recurrence, in words | — |
| I-13 | Prior is part of the realization datum, not selected by invariance; counting measure is a maximal-entropy default | scope remark | Main §1.2, Remark (the measure as a realization datum) | compress: "realization = rule + how the hidden part is prepared" | — |
| I-14 | Three classes $\mathsf S_K,\mathsf D_K,\mathsf Q_K$ (fixed-basis Born records, diagonal initial state, measured every step) | definitions | Main §3.4 Theorem (finite-horizon stochastic–reversible–unitary equivalence) | keep in words; Q_fb's "same measurement at every step" kept explicit | — |
| I-15 | **Theorem 1**: $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ for every finite alphabet and horizon | machine-checked | Main §3.4 Theorem (finite-horizon …) with kernel `finite_horizon_equivalence`, `S_imp_D`; Main §1.5; ledger `MAIN:T-finite-horizon-stochastic-reversible-unitary` K3 | keep; compact display S ⇔ D ⇔ Q_fb allowed | ledger row T-1 |
| I-16 | "This settles a question of possibility, not of fact: it does not show that nature is such a world" | scope | Main §1.2 Remark; §3.4 Remark | keep verbatim in substance | — |
| I-17 | Construction: hidden register holds a pre-drawn sequence + clock | proved | Main §3.4 proof (S ⇒ D, "a clock with the complete trajectory record"); attribution [EGGH26, Prop. 13] | keep as the concrete example | **F-9** (attribution absent from Main) |
| I-18 | Independent-prior realization: rational kernels (process dilation), arbitrary kernels by response-table Extension, "proved on paper, with exact probes" | proved on paper | Main §3.4 Theorem (finite-horizon process dilation) and *Extension* (L518–520); ledger `MAIN:T-finite-horizon-process-dilation` P | compress to one clause in §3.3 (needed because the recurrence result assumes a shared hidden preparation) | — |
| I-19 | $\mathsf D\subseteq\mathsf Q$ by permutation unitary read in configuration basis; $\mathsf Q\subseteq\mathsf S$ is the Born rule | proved | Main §3.4 proof | keep in words | — |
| I-20 | Attributions: [EGGH26 Prop. 13, Prop. 16]; random-mapping [LP17 Prop. 1.5]; unistochastic [Bar25; Bar23 §4.3; Bar26 §4]; ancilla dilation [Bar26 Thm 3.3]; every-step record law [SGD19]; omitted-measurement consistency [SGD19; Milz20] does not arise | attribution | external | keep Egri et al., Barandes, Levin–Peres, Strasberg–García Díaz in one "where the pieces come from" paragraph; drop Bar26 Thm 3.3 dilation detail and Milz20 remark (move: they qualify Main §3.1/§3.4 machinery) | F-9 |
| I-21 | Markov laws lie in all three classes, so representability does not distinguish memory | proved | Main §3.4 Remark (what this equivalence does and does not say) | keep (central) | — |
| I-22 | $p=\lvert U\rvert^2$ is definitional; permutation unitaries give same table for every exponent $q>0$; "the quadratic exponent is not selected" | proved (scope) | Main §3.4 Remark (same); [Bar26, Thm 3.1] | keep (central "does not prove") | — |
| I-23 | Fixed finite realization is $L$-periodic; nonperiodic law has no exact all-time realization by one fixed finite substratum | proved | Main §3.4 (L640) | keep (one sentence) | — |
| I-24 | Possibility answered; no fixed-measurement record alone rules out a hidden deterministic account; content lies in memory | summary | as above | keep (in §5 "foundations") | — |

#### §2.4 Where the memory lives (L92–133)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-25 | Definitions $M_t$, hidden predictive memory | definitions | Main §1.5, §3.4 | keep in words; at most one symbol ($M_t$) | — |
| I-26 | **Theorem 2** (a) next step depends on past only via hidden posterior; (b) different predictions need at least as different hidden odds; (c) $M_t\le I(X_{<t};H_t\mid X_t)\le\log_2\lvert\mathcal C_H\rvert$ | (a)–(c) machine-checked for a joint law; time-$t$ reading on paper | Main §3.4 Theorem (unavoidable hidden predictive memory) and Main §1.5 ("reading a realization's time-$t$ law as that joint law is a step not formalized"); ledger `MAIN:T-unavoidable-hidden-predictive-memory` K3 | keep in plain words (owner's register example) | ledger row T-2 |
| I-27 | Predictive memory ≠ state inference; record-fibre criterion; passive stabilization after $\max(1,N-1)$ readings; parts "machine-checked for nonempty compatible-state sets"; "None of these results supplies a physical storage, preparation or intervention mechanism" | mixed: paper + kernel-only | Substratum Prop. 24.5 (paper) | compress into I-06 (one sentence + the "no physical mechanism" limit); drop Lean status and $N-1$ bound | **F-1** |
| I-28 | Memory witness ⇔ $M_t>0$ by vanishing criterion [PW25] | standard | Main §1.5 | keep in words | — |
| I-29 | **Corollary**: $M_t>0$ exactly when every faithful realization carries readout-relevant hidden memory; converse uses one realization (Theorem 1) | proved on paper | Main §1.5 (verified: both directions stated) | keep (central; both directions in words) | ledger row C-unnamed-99fe05c0 |
| I-30 | Keeping the past ≠ memory: every reversible world run from the start stores its whole visible past, Markov laws included | proved | Main §1.5 | keep (one sentence; good intuition) | — |
| I-31 | Capacity $\lvert\mathcal C_H\rvert\ge 2^{I^*}$; least hidden predictive memory over deterministic completions $=I(X_{<t};X_{>t}\mid X_t)$, $=M_t$ iff a stated CMI vanishes; bijective realizations carry $H(X_{<t}\mid X_t)$; "lower bound machine-checked for bijective realizations and proved on paper for non-injective ones" | mixed | Main §3.4 Theorem (C3 necessity) + Corollary; Remark (a variational question); ledger `MAIN:T-c3-necessity` K3 | keep the capacity bound in words; compress the variational result to one sentence ("the exact minimum is the information the past carries about the whole future, given the present") | — |
| I-32 | Pinsker floor $M_t\ge p_0\delta^2/\ln2$ | proved on paper | Main §2.3 Lemma (accessible conditional memory from readback) | move (one clause at most: "clearly different predictions force a definite minimum of memory") | — |
| I-33 | Actual finite-permutation trajectories: capacity bound uniform in time and finite future blocks, $I^*_{\rm fin}\le\log_2\lvert\mathcal C_H\rvert$; "machine-checked" | kernel-only (census), not independently reviewed | **none in a formal paper** (Lean `TrajectoryMemory`; census family `kernel-only`, no anchor; ledger delta of the C3 row names it as "unreviewed") | move — no formal home exists | **F-2** |
| I-34 | Entire visible future as a finite-image variable; $J^*\le\log_2\lvert\mathcal C_H\rvert$; equality with finite-block supremum "not certified" | kernel-only | **none in a formal paper** (Lean `FullFutureMemory`; census `kernel-only`; audit record `verification/audits/manuscript/full-future-memory-20261028/` exists on `main`) | move — no formal home exists | **F-3** |
| I-35 | (C1)–(C4) as diagnostics, not hypotheses of Thm 1; (C4) ⇔ $M_t>0$ in a faithful realization; (C1) from (C4); (C3) by capacity; (C2) structural vs slow forms; C2 necessity in coupling-step model, "with no mixing hypothesis"; slow-bath form under mixing hypothesis | mixed (paper) | Main §1.3; Main §3.4 Theorem (physical memory: C2, process form); ledger `MAIN:T-physical-memory-c2-process-form` P | compress to the four-item plain checklist (influence, persistence, capacity, readback) with one sentence on the mixing hypothesis being an assumption | — |
| I-36 | Coupling + persistence + capacity without readback give no memory: fair coin | proved | Main §2.3 Remark (why (C4) is a separate condition) | keep as one-line example | — |
| I-37 | *Proofs and sources* for Thm 2 (data-processing, joint-law vs actual-trajectory forms) | verification detail | Main §1.5, §3.4 | move | (actual-trajectory form: F-2) |

#### §2.5 Recurrence and indivisibility (L135–169)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-38 | Forecast chaining (weather); P-divisibility; card game: two identical coin-toss rows cannot become two certainties | elementary | Main §2.3 | keep (central intuition) | — |
| I-39 | Rooted family keeps rows for starts of probability zero; meaningful only with one hidden preparation shared by every start, drawn independently | hypothesis of the theorem | Main §2.3 Theorem (history readback …) and Scope ("a non-permutation row may belong to a root of visible probability zero") | keep the hypothesis in plain words (it is load-bearing) | — |
| I-40 | "Different deck" example: red start always red, black start uncertain, overlap only from the never-dealt start; forecasts return at step 2, world at step 3 | illustration, cited [Main §2.3] | general principle in Main §2.3 Scope; **the worked example itself is not in Main** | drop the example, keep the principle | **F-6** |
| I-41 | **Theorem 3** (recurrence and overlap): overlap at $s$ + return $\Gamma_n=I$ ⇒ not P-divisible on $\{0..n\}$ | machine-checked, rooted form | Main §2.3 Theorem (overlap and return), kernel `pIndivisible_of_rooted_identity_return_of_overlap`; ledger `MAIN:T-overlap-return` K3; attribution [RHP14 Thm 2.4; BD16; Dou26 Prop. 1] | keep in words ("a step-by-step forecast can never move two forecasts further apart") | ledger row T-3 |
| I-42 | **Corollary** (recurrence-cycle indivisibility): non-permutation $\Gamma_s$, $0<s<L$ ⇒ not P-divisible on the cycle; supplied by any two histories with common endpoint, any memory witness, any non-deterministic visible step (also Markov-on-windows laws); with full-support visible prior ⇔ $M_k>0$ at some $k<L$. Status: "first sentence is machine-checked on the actual finite realization"; supply and equivalence "proved on paper" | mixed | Main §2.3 Theorem (history readback + finite recurrence implies indivisibility) and Scope — paper proof using kernel lemma `isPermMatrix_of_stochastic_inverse`; ledger `MAIN:T-history-readback-finite-recurrence-implies` = P. The "actual realization" machine check is `RootedRecurrenceBridge` (kernel-only) | keep (central conditional result), every hypothesis carried: shared, independent hidden preparation; all starts counted; full support for the equivalence; drop the machine-check statement | **F-4**; ledger row C-recurrence-cycle-indivisibility |
| I-43 | Memoryless on accessible windows yet memory later; windows short vs $L$; late memory and the chaining failure may appear in no accessible record; "a property of the world's rule … not what accessible data will show" | proved / scope | Main §2.3 Scope | keep (essential limitation) | — |
| I-44 | Example $X_0,X_1,X_2$ fair bits, $X_3=X_0$: $M_1=0$, every deterministic completion keeps $X_0$, $M_2=1$ bit | proved | Main §3.4 Remark (a variational question) (L616) | keep (concrete example of late memory) | — |
| I-45 | Recurrence-cycle indivisibility does not separate Markov-on-windows laws from memory laws; discrimination is memory at an accessible order (C4) | scope | Main §2.3 Scope | keep | — |
| I-46 | *Proofs and sources*: TV contraction, [Dou26 Prop. 1] concurrent; [BB12 Problem 23] lemma machine-checked; monotone distance necessary not sufficient; routed (C4) ⇒ indivisibility at a return horizon (machine-checked) | verification detail | Main §2.3 (incl. *Routed readback*, kernel `routed_forces_indivisible_somewhere`) | move; keep Doukas attribution | — |

#### §2.6 Examples (L171–196)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-47 | Six-hidden-state model: $\Gamma_1$, $\Gamma_2=I$, divisor with negative entries; Markov comparison 5/9, 4/9; $a/(2-a)$ | exact | Main §2.4 | move (card game suffices) | — |
| I-48 | XOR: memory (1 bit) without short-window indivisibility [RHP14 Eq. 15; Dou26 App. A]; still fails somewhere in the full cycle | proved | Main §2.3 Scope ("XOR control"); Main §3.4 (L475) | keep (one paragraph; shows memory ≠ chaining failure) | — |
| I-49 | Card table exact; peek table (1/2, 1, 1/2, Markov 1/2); peek effect comes from overwriting; anticorrelated cards divisible | exact enumeration | Book §1.11 (table verified; anticorrelated case not checked there) | keep a 3-row table or prose; drop anticorrelated aside unless Book carries it | — |
| I-50 | Card protocol with wing-local operations, independent settings, outcome every run: $\lvert S_{\rm CHSH}\rvert\le2$; "changing those premises changes the claim" | proved (Bell) | Main §3.3; Book §1.11 | compress into the Bell paragraph | — |

#### §3 Quantum emergence (L197–266)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-51 | Correspondence alone does not give QM: (1) one fixed measurement only; (2) every law, so it selects neither the squared form nor the relating evolution, and represents statistics without a physical mechanism; (3) five further conditions OI does not imply | scope | Main §3.4 Remarks; GR §3.3 | keep (opening of "What it does not prove") | — |
| I-52 | Three notions (accessible memory; P-indivisibility; quantum non-Markovianity) distinct; indivisibility ⇒ CP-indivisibility for permutation unitary + diagonal hidden state; Hadamard counterexample outside that class | proved | Main §3.2 Theorem (CP-indivisibility, framework scope); Remarks (three notions, kept apart), (scope: P-indivisibility is not quantum non-Markovianity) | compress to two sentences | — |
| I-53 | Embedded card game CP-indivisible; its memory classical in the sense of [BBS24] via a Pauli-twirl decomposition; with a fixed initial hidden card the swap admits none | partly sourced | Main §3.2 (CP-indivisibility); Main §4.5 covers only the fixed-initial-slot swap; **the uniform-burn-card Pauli-twirl decomposition is stated only in the Introduction** | drop | **F-5** |
| I-54 | Backflow [BLP09], [BJA17]; "Theorem 1 states which laws admit realizations … not why"; Calvo's axiom derivation contrasted | scope/attribution | Main §3.4 Remark (representation, not explanation) | keep "representation, not explanation" (central); keep Calvo in prior work; drop BLP09/BJA17 | — |
| I-55 | Setting: complex matrix kinematics and tensor-product composites **taken as given, not derived from OI**; availability rules | assumption | GR §3.3 (verified: "A derivation of this kinematics … is open") | keep the assumption in plain words; drop the rule list (move) | — |
| I-56 | **Theorem 4**: available families are exactly normalized finite Kraus instruments iff (i)–(v) | machine-checked both directions | GR §3.3 Theorem (operational-completion characterization), kernel `exactAll_iff_physical_general`; ledger `GR:T-operational-completion-characterization` K3 | keep in words; list the five conditions in one line each in plain English | ledger row T-4 |
| I-57 | Each condition independent; a qubit theory that never creates coherence realizes the observation process and is not quantum: OI alone ⇏ QM (machine-checked) | proved | GR §3.3 (`five_way_minimality`, `oi_alone_not_qm`) | keep (central) | — |
| I-58 | (iv) fails for operations finite bijective dynamics supplies under the stated observer access, every system ≥ 2 states (one step from Lean statements: all-ones vector fixed; no quarter-phase gate) | proved | GR §3.3 "Substratum-source form" (`permClass_onesFixing`, `onesFixing_not_phasesAvailable`) | keep in words ("the reversible shuffles a finite world supplies cannot make the phase shifts quantum control requires") — wording to be checked against GR's exact access scope | — |
| I-59 | Open: which of (iii)–(v) a substratum with further intervention principles supplies; why complex matrices and tensor products | open | GR §3.3 | keep (§6) | — |
| I-60 | Sufficiency via Stinespring/Kraus/Ozawa; reconstructions [Har01; CDP11; MM11] | attribution | GR §3.3 | keep one attribution sentence | — |
| I-61 | Representability does not select the relating evolution: time-dependent right action (exhibited pair), constant deformation cancels; trivial-ancilla quotient | proved (kernel-checked) | Main §3.4 Remark (scope: representability, not selection of the relating evolution); census family "coherent-lift stabilizer no-go" (current, anchored in Main) | keep the first sentence pair in words; move the trivial-ancilla quotient | — |
| I-62 | No fixed finite realization reproduces a qubit; factorization proved, unboundedness imported [HKLP24 Thm 4; GH03; Mon08; Har04]; does not touch Thm 1 | proved + imported | Main §3.4 Proposition (finite-substratum operational obstruction — classical-dimension form) | keep (plain words, "imported" kept) | — |
| I-63 | Bell ceiling under (i) determinism, (ii) disjoint local settings, (iii) readouts outside the other's causal cone, (iv) measurement independence, outcome every run | proved | Main §3.3 Theorem (Bell ceiling for a screened local completion); [Bel64; CHSH69] | keep in words | — |
| I-64 | Framework keeps measurement independence (posit), adopts ontic parameter dependence with operational no-signalling; nearest-neighbour cubic update cannot supply it; preparation-indexed coupling graph is the open hypothesis H-Bell | posit + proved obstruction + open | Main §3.3 Corollary (Bell–lattice obstruction and state-dependent escape); Substratum §3.2 | keep (scoped; H-Bell open) | — |

#### §4 Cosmological constant (L267–291)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-65 | Zero-point sum to Planck cutoff ≈120 orders above observed; must cancel if it gravitates | external | [Wei89] | keep | — |
| I-66 | Mismatch = de Sitter entropy up to a convention factor: "a dimensional identity" | dimensional identity | GR §6.3 | keep one sentence or drop (owner Q4) | — |
| I-67 | Two levels: zero-point sum in emergent description, $\Lambda$ in substratum's; a uniform shift changes no visible probability | established (descriptive) | GR §6.2 ("Descriptive distinction established") | keep | — |
| I-68 | Proposal: if field equations take the targeted form, the zero-point sum does not source curvature; residual vacuum term not computed; observed $\Lambda$ an input | conditional proposal | GR §6.2 ("dynamical decoupling conditional on G3") | keep as proposal; one display at most (owner Q1) | — |
| I-69 | Missing link: the two completions share everything visible; deciding needs field equations (G3), open | open | GR §6.2, §8.5 | keep | — |
| I-70 | Related: trace-free Einstein [EvEMU11], sequestering [KP14], Volovik [Vol06] | attribution | external | keep one sentence | — |

#### §5 Black-hole information (L293–311)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-71 | Two questions: conservation (holds by bijectivity) vs accessible recovery [HP07]; burned-letter analogy | framing | GR App. A (conservation by bijectivity) | keep | — |
| I-72 | Toy model (registers, emissions, fixed read schedule, $P_{\rm succ}$, accessible advantage); maps range over all bijections/maps, "none is derived from the substratum's dynamics" | definition + scope | [BHa] record only | compress; keep the "not derived from the substratum" limit | **F-7** |
| I-73 | 1,376 of 40,320 bijections give zero advantage; 60 non-injective maps recover exactly; floor $P_{\rm succ}\ge1/\lvert\mathcal U\rvert$; 32 maps violate it; secret-sharing analogy [Sha79] | exhaustive enumeration + proved floor; unpublished | [BHa]: `verification/programmes/black-hole-information/bh01_access_v1/` (on `main`); **no formal paper** | keep the qualitative separation and the floor in plain words with one number; cite [BHa], status stated | **F-7** |
| I-74 | Page-curve obstruction: H-scramble has no instance for configuration states with coordinate-aligned bipartition; Thms A.8–A.9 as stated give no nonvacuous Page curve | proved | GR §8.4, App. A.7–A.9; [BHb] (`bh02_scramble_v1/`) | keep (one paragraph) | — |
| I-75 | Further limits: Thm A.7 assumes definite $D$ and short times; proper energy shell; recovery needs specified coherent preparation or different partition | scope / open | GR App. A.7–A.9 | compress into §6 open list | — |
| I-76 | [CE] coherent-subspace construction: exact $S_r=k-\dim(W\cap R_r)-\dim(W\cap B_r)$; endpoints zero; mean bounds; "not Page's Haar mean" | written finite proof + exact controls | **no formal paper**; record read from history at `bdcbd32` (owner D2; merge `4a90ac2f` makes it reachable, not in `main`'s tree) | compress to one sentence with its scope, or drop (owner Q5) | **F-8** |
| I-77 | [CR] reversible sequential release: entropy equals $S_r$ during first window; tent profile for mirror Bell pairs; "proved on paper and not independently reviewed"; "not … a black-hole evaporation model" | written proof, unreviewed | same, at `2624d49` | compress with I-76 or drop (owner Q5) | **F-8** |

#### §6, Code/data, Appendix A (L313–363)

| id | Claim | Status | Formal source | Fate | Flag |
|---|---|---|---|---|---|
| I-78 | Summary paragraph | summary | — | absorbed into §§3–6 | — |
| I-79 | "Established mathematical results" list (machine-checked vs paper) | status | per item above | replaced by the status words of §1 and by citations | — |
| I-80 | "Checked in Lean, not independently reviewed" list (owner D3 wording) | kernel-only | census `kernel-only` (#1118) | removed with the Lean inventory: the rewrite makes no statement that depends on these modules | F-1–F-4 |
| I-81 | Conditional physical interpretations (fixed-basis statistics as embedded-observer laws if OI holds; Bell trade-off; zero-point sum if field equations; Page curve not established) | conditional | as cited | keep in §5 | — |
| I-82 | Open problems 1–5 + application list | open | Main §1.3, §3.4, §4.5; GR §2.2, §6.2, §8.5, App. A.6–A.9; Book §7.6 | keep as §6 | — |
| I-83 | Code/data: Lean 4.33.0 / Mathlib pin `17b830bc`, axiom recipe in `papers/introduction_repro/`; four additional modules at checkpoints; probes and BH code (MIT), snapshot `f5c281ae` | verification detail | — | replace by the short technical-source guide | F-10 |
| I-84 | Appendix A Lean inventory | verification detail | Main/GR kernel citations; census registry | remove (owner decision) | F-1–F-4, F-10 |
