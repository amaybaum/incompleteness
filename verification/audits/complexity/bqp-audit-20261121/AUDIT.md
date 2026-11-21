# BQP-AUDIT: complexity statements in the corpus

**Status: WIP / UNVERIFIED.** Research and design only, under the owner decision on #1169
(comment 7063843557, stream 2). Awaiting an independent non-author review. No manuscript is
edited. Every proposed wording in §3 is a proposal; per the owner decision, narrowing waits
until the A1 retirement (#1477) lands. Entries marked **#1477** cite text that #1477's deletion
plan rewrites (§3 preamble) and are re-derived after it lands.

**Base.** `origin/main` at `df6da1c6101e811acdc7952d5748aff57028e8ed`. Line numbers below are at
that commit. `papers/` and `book/` are unchanged between `97070c98` (where the first read-only
draft was taken) and this base. Abbreviations: `Comp` = `papers/Computation.md`,
`ch14` = `book/ch14-quantum-computing.md`, `FULL` = `book/The-Incompleteness-of-Observation-FULL.md`.
Each `ch14:n` cited here is mirrored verbatim at `FULL:(n+3600)` (checked line by line for every
`ch14` line cited); other mirrors: `ch15:8` = `FULL:3885`, `ch18:28` = `FULL:4759`,
`ch18:322` = `FULL:5053`, `glossary:23` = `FULL:6514`, `glossary:65` = `FULL:6556`,
`ch12:225` = `FULL:3411`, `appendix-c:138` = `FULL:6293`, `book/README.md:82` has no `FULL`
mirror.

**Verification layers** used in the tables: **K** kernel-checked Lean; **X** exact computation;
**N** floating-point arithmetic; **P** paper argument (prose derivation); **I** imported standard
result or conjecture of complexity theory; **D** definitional: the conclusion is contained in a
stated hypothesis; **C** conjecture or interpretation.

## 1. Theorem inventory

### 1.1 Manuscript statements

| # | Statement | Sites | Stated status | Actual support | Layer |
|---|---|---|---|---|---|
| I1 | Conditional BQP characterization: under the model, the class the observer can efficiently perform is exactly BQP | Comp:15, 94, 106; ch14:12, 100 | "conditional BQP model theorem"; "Conditional BQP Characterization Theorem" | Both directions are read off the model's hypotheses (I2, I3). No step of §4.1–§4.2 or §14.3–§14.4 is stated to consume C1–C4; the representation layer they cite holds for every finite observable law (Main §3.4; Main status-ledger row (i), Main:742) | D, P |
| I2 | Lower bound: every uniform polynomial-size circuit family can be hosted | Comp:98; ch14:46–64 | "Conditional Lower Bound" | Preparation, a universal gate set, readout and fault tolerance are supplied by hypothesis (Comp:98 "§4's control hypotheses supply preparation and gating"; ch14:50, 64). The argument is the standard definition of BQP plus Solovay–Kitaev | D, I |
| I3 | Upper bound: nothing outside BQP is efficiently performed | Comp:102; ch14:80–86 | "Conditional Upper Bound Theorem" | Hypothesis: every admissible evolution admits polynomial-overhead quantum-circuit simulation (Comp:102; ch14:86). With that hypothesis the bound is composition bookkeeping plus the PostBQP = PP charging of postselection. CPTP type alone gives no efficiency (ch14:80, citing Shende–Bullock–Markov) | D, I |
| I4 | BQP-form Extended Church–Turing thesis as a "conditional theorem" | Comp:15, 112, 271; ch14:122–148; glossary:65; ch12:225 | "conditional theorem", "derived theorem" (ch14:146, 148) | Global coverage: every physically realizable computation satisfies the closure and efficiency hypotheses (Comp:112). Those hypotheses include polynomial-overhead quantum-circuit simulation (Comp:102), so the coverage premise, applied to every physical computation, contains the BQP-form thesis | D |
| I5 | BPP–BQP separation read as the cost of partial (marginal) observation | Comp:15, 114, 272; ch14:150 (heading), 156–166, 270; ch15:8 | interpretation; Comp:114 "has empirical consequences" | The separation itself is the standard conjecture. The reading adds no observable that distinguishes it from the standard reading; none is named at Comp:114 | I, C |
| I6 | Finite-substratum width ceiling, $n^* \approx 480$ (day), 520 (decades), 610 (horizon) logical qubits at $\alpha = 1$ | Comp:118–136; ch14:272 | "conditional consequence with its assumptions stated" (Comp:122); "the forced position" (Comp:122) | Premises: total finiteness (Main posit (ii), open and not adopted, Main:736; Comp:120; both rewritten by #1477, see §3), patch budget, a rate of one update per Planck time per degree of freedom, a substratum-to-classical-cost bridge, $C_{\rm cl}(n,\varepsilon) \ge 2^{\alpha n}$, non-collapse of PH (Comp:124, 134). Arithmetic reproduced: $\pi(cT)^2/l_p^2 \cdot T/t_p \approx 1.29\times10^{145}$ for $T$ = 1 day, $\log_2 \approx 482.1$, matching Comp:124, 130 | C (premises), N (arithmetic); **#1477**-dependent |
| I7 | Depth axis: a residue, no derived bound | Comp:138–146 | "the framework supplies a residue but no derived bound" | As stated; whether error correction removes a depth limit is stated open (Comp:142) | P |
| I8 | Neutrality on P vs NP; NP ⊆ BQP open | Comp:150–166, 196; ch14:168–180 | neutrality result | Standard inclusions P ⊆ BPP ⊆ BQP ⊆ PSPACE, NP ⊆ PH ⊆ PSPACE | I |
| I9 | Silence on P vs NP is "structural, not stipulative", "not a chosen agnosticism"; no principled bridging axiom is available | Comp:17, 174–182, 204, 206, 210–222; ch14:184, 188 | presented as a result ("can be sharpened", ch14:184) | Argument sketch over candidate axiom forms (Comp:210–222). Comp:17 and Comp:180 read it as a feature of the framework's axiom type ("not a chosen agnosticism"), a claim about all axiom systems of that type. §4 itself obtains an asymptotic class (BQP) from finite physical structure by adding a uniform-family premise as a model hypothesis (Comp:15, 94). That is consistent with Comp:178, which says only that the axioms do not themselves provide a bridging premise; it is not consistent with the reading at Comp:17 and Comp:180 | P (sketch) |
| I10 | Comparison with Aaronson's NP-hardness principle: "stronger" at the BQP boundary | Comp:17, 200; ch14:186 | comparison | The BQP ceiling is conditional on the §4 model (I1–I3); the comparison sets an assumed ceiling against a posited principle. Comp:202 states the ceiling neutrally | P |
| I11 | Framework-relative conjectures: lattice-local NP protocols; SU(2)-compatibility of exponential advantage (12-case survey); gauge equivalence and reductions | Comp:17, 230–262; ch14:204–240 | "conjecture", "not framework predictions" (Comp:17) | Survey fitted after the fact. The criterion admits "quantum deformations" (Comp:246) and further variants; Comp:17 says "maximized … matches the framework's gauge group", Comp:246 says "correlates … SU(2)" | C |
| I12 | Halting is decidable on an explicit finite deterministic orbit | Comp:74, 190 | stated as fact | Pigeonhole recurrence test; a computability fact, not a complexity result | P (elementary) |
| I13 | No claim that the bijection is efficiently computable | appendix-c:136, 138 | scope statement | As stated; both lines are rewritten by #1477 (D218/D219, D246/D247) | — ; **#1477**-dependent |

Other pointers restate I1 or I4 without new content: ch00:101, ch12:225, ch13:174, ch15:8,
ch16:10, ch18:28, ch18:322, book/README.md:29, appendix-a:221, glossary:23, 65,
readers-guide:63, 65 ("BQP characterization theorem"), ch09:240 ("BQP characterization" in a
list of cross-domain reach), `book/README.md`:82 (an overclaim site, O1 and O5),
`papers/Complexity.md`:15, 29, 298 (forward pointers to `Comp`). `papers/Methodology.md`:543
mentions a cross-domain audit that included computational complexity and states no complexity
result. A search of `papers/{Main,SM,GR,Substratum,Structure,Methodology,Introduction,Complexity,Juno,Medicine,Bioinformatics}.md`
for BQP, BPP, PSPACE, NP-complete, P vs NP, Church–Turing, polynomial time, complexity class,
Solovay and threshold theorem finds no further complexity statement.

### 1.2 Kernel (Lean)

Search scope: the 252 `.lean` files under `verification/lean/` (6) and
`verification/lean-mathlib/` (`OIBridge.lean` and 245 modules), and the registry
`verification/lean-manuscript-census.json`.

- No `.lean` file mentions BQP or BPP. No module imports `Mathlib.Computability.*` or
  `Mathlib.Analysis.Asymptotics.*`; the `Mathlib` imports used are from `Analysis`,
  `LinearAlgebra`, `Data`, `Tactic`, `Algebra`, `RepresentationTheory`, `MeasureTheory`,
  `Topology`, `GroupTheory`, `Logic`, `SetTheory` and `NumberTheory`. (Case-insensitive matches
  on `pSpace`/`OpSpace` in `StageCompletion`, `ParityNot` and `CompositeDimension` are not
  complexity content.)
- The census registry carries `papers/Computation.md` and `FULL` as manuscripts; none of its 127
  families names a site in `Comp` or `ch14`, and it has no entry mentioning BQP, BPP, Turing or
  Church.

Kernel results adjacent to the model's hypotheses. None concerns size, cost, uniformity or
asymptotics:

| Module (`verification/lean-mathlib/OIBridge/`) | Identifier | What it states | What it does not state |
|---|---|---|---|
| `QuantumRepresentation` | `QStar`, `qfbRealizable_rootTraj`, `rootTraj_marginal` | the representation class and finite-horizon compatibility | either inclusion of I1 |
| `QuantumRepresentationT2` | `qStar_not_subset_finiteRootedRealizable` | the Hadamard witness `pdFamily` lies in `QStar` and is not finitely rooted-realizable | anything computational |
| `QuantumRepresentationT3` | `qStar_inclusion_iff_nonempty` | every finitely rooted-realizable family is in `QStar` iff the visible carrier is inhabited | non-permutation dynamics; cost |
| `StinespringAssembly`, `IsometryExtension` | `fullInstruments_of_control`, `exact_of_sound_control_unconditional` | composite unitary control gives every finite endomorphic Kraus instrument; with `KrausSound` the theory is exact | efficiency; that the control is native |
| `KrausSoundness` | `exact_iff_sound_and_full`, `everywhereAvailable_not_sound` | exactness iff soundness and fullness; a theory with everything available is not sound | soundness from OI dynamics |
| `InstrumentAvailability` | `q3_countermodel` | frozen Level III structure with finite-support availability does not entail availability of infinite-support coherent operations, within the fixed-algebra interface | — |
| `InstrumentRealization` | `OnesNormal`, `OnesFixing`, `flow_realized_not_instrumentRealized` | an invariant preserved by instrument constructors; the transition flow is branch-realized and not instrument-realized on a carrier with a third point | the flow endpoint |
| `SecondOrderCircuit` | `depth_two_circuit`, `quasilocal_drive`, `unit`, `proj` | the native step factors as swap layer after shear, each layer an involution of commuting local gates; one-parameter unitary drives from gate lists, `unit g t = 1 + (e^{iπt} − 1)(1 − g)/2` | gate cost; physical status of the continuous flow |

## 2. Gap analysis

1. **Derived versus assumed.** Every complexity bound in the corpus is obtained from an added
   hypothesis that contains it: the lower bound from supplied control, gates, readout and fault
   tolerance (I2); the upper bound from polynomial-overhead simulation of each admissible
   evolution (I3); the BQP-form thesis from global coverage of that simulation hypothesis (I4);
   the width ceiling from total finiteness, the patch budget, a rate cap, a cost bridge and
   hardness conjectures (I6). The manuscripts state this for I1–I3 (Comp:106: "CPTP
   representability of the visible dynamics implies none of the model hypotheses"; in other
   words at Comp:15 and Comp:94); the gap is in the wording of I4, I6, I9 and I10 and in the
   hypothesis lists (§3).
2. **Nontrivial content beyond assuming efficient quantum simulation.** None was found in the
   searched corpus (§1.1, §1.2). The content that does not reduce to that assumption is standard
   complexity theory (I8; PostBQP = PP; Solovay–Kitaev; Shende–Bullock–Markov), the elementary
   I12, and the arithmetic of I6. The kernel has no complexity-theoretic statement.
   **Scope.** Items 1 and 2 concern complexity classes and time or size bounds on computation,
   in the files searched. They do not cover native resource bounds of other kinds that the
   corpus proves without an added hypothesis containing them. Examples: the per-process
   capacity bound $m \ge 2^{I^*}$ for any deterministic-bijection realization (Main:522,
   §3.4); the zero entropy rate of the visible factor of a finite reversible substratum under
   every invariant prior, which bounds recorded randomness by
   $\log|\mathcal{C}_V \times \mathcal{C}_H|$ (Structure:1231); and PE-01, a finite
   counterexample (one generator cell) to the universal form of an unpredictability statement,
   which the report cites at ch18:114 at its own base (no longer present there on this base),
   in which a bounded embedded observer predicts with positive advantage
   (`verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1/REPORT.md`).
   None is a complexity-class result.
3. **Candidates checked for a native restriction** (each a reading, not a result):
   - *Finite ⇒ periodic* (`QuantumRepresentationT2`, layer K) is a restriction on process laws
     of a finite realization, not on a complexity class.
   - *The native step is a classical reversible depth-two circuit* (`depth_two_circuit`, layer K)
     would bound per-step classical cost of the substratum. Turning it into a ceiling is the
     §4.5 route, which uses total finiteness (open, not adopted) and hardness conjectures (I6).
   - *The ones-fixing invariant* (`InstrumentRealization`). Exact computation
     (`checks/lie_closure.py`, layer X) of the real Lie algebra generated by
     $\{\, i(1-P)/2 \,\}$, the generators of the kernel's `unit` up to the factor π, for chosen
     sets of permutation involutions $P$ on $N = 2^n$ points: control (two commuting NOTs,
     $N = 4$) gives 2; NOT, CNOT, SWAP ($N = 4$) give 9; NOT, CNOT, Toffoli ($N = 8$) give 49.
     Countercontrol, non-abelian and non-saturating: CNOT₀₁ and CNOT₁₀ ($N = 4$) also fix
     $e_0$ and give $4 = (N-2)^2$, so the computation detects a second invariant. NOT and CNOT
     alone at $N = 8$, without Toffoli, already give 49, so saturation does not track classical
     universality of the gate set and the Toffoli set carries no extra significance.
     Since every generator annihilates the uniform vector, the algebra lies in $u(N-1)$ on its
     complement, of dimension $(N-1)^2$; the values 9 and 49 equal that bound. For these two
     chosen gate sets the invariant is the only obstruction to full unitary control on the
     complement. This is a finite witness at $N = 4, 8$ for gate sets chosen by hand, not the
     native step's gates; it says nothing about efficiency, and it uses fractional-time driving,
     which is supplied control. Classification: BORDERLINE. The values 2, 9 and 49 were observed
     before being written into the script, not preregistered; the countercontrol and the
     no-Toffoli value were stated by the independent review before they were run.
4. **Hypothesis-list mismatches** (prose consistency):
   - Comp:106 lists "explicit precision accounting" and omits the uniformly computable local
     descriptions, polynomial physical time and polynomial-overhead circuit simulation that
     Comp:94 and Comp:102 list and §4.2 uses.
   - ch14:100 omits efficient qubit encoding, fault tolerance (lower bound) and the clock model
     (upper bound), which ch14:12 lists among the hypotheses of §14.4.

## 3. Overclaim sites and proposed narrowed wording

Proposals only. **Every row is deferred** on the owner decision (#1169, comment 7063843557):
narrowing of overclaim sites waits until the A1 retirement lands, and ch14:184 overlaps #1477.

The **#1477** column marks dependencies on #1477's deletion plan (`edits.json` at `55544cc3`,
373 edits, read only). That plan has no edit at Comp:122, :178, :182 or any `ch14` line; its one
`Computation.md` edit, D248 (row X-01), rewrites Comp:120. Row X-55 of
`verification/audits/foundations/a1exit-ledger-20261120/rows.json` is a frozen record; its
Step-2 corrections at Comp:178, :182 and ch14:160, :164, :184, :262 are on `main` already
(`verification/audits/manuscript/a1exit-s2e-20261121/RESULT.md`, edits E01, E02, B01–B04), and
the text cited here is that corrected text. The plan does rewrite text this audit relies on:
- appendix-c:136 (D218, D219) and appendix-c:138 (D246, D247), the I13 sites;
- Main posit (ii) (D224 deletes it; Main:736 here), cited by I6, O8 and §2 item 3;
- Main:54, Lemma 3 (D260 adds "on a finite representative"), cited by O8;
- Comp:120 (D248), cited by I6.

Rows marked **#1477** are re-derived against the landed text. Every `ch14` change mirrors into
`FULL` (§1 offsets) and every `Comp` change into `papers/Computation.tex`.

| # | Site(s) | Current wording (excerpt) | Issue | Proposed wording | #1477 |
|---|---|---|---|---|---|
| O1 | Comp:15, 271; ch14:126, 136, 148; glossary:65; book/README.md:82 | "as a conditional result rather than an empirical conjecture" (Comp:15); "is a conditional theorem … not an empirical conjecture" (Comp:271); "conditional derived theorem"; "derives the BQP-form (quantum) ECT"; "is recovered as a *conditional theorem*" (README:82). Comp:112 ("rather than a theorem about unconditioned physical reality") is already narrow and needs no edit | conditional → status change: the coverage premise contains the thesis (I4) | "Under the global-coverage premise the BQP-form thesis follows from the §4 model. The premise requires polynomial-overhead quantum simulation of every physically realizable computation, which is the thesis's own content, so its empirical status is unchanged." | no |
| O2 | ch14:142, 146 | "structural foundations for the ECT that were previously absent"; "The promotion of the ECT from empirical conjecture to derived theorem" | as O1 | Delete both sentences; state: "The model makes explicit which hypotheses the BQP-form thesis requires." | no |
| O3 | ch14:40 | "The ceiling is principled rather than empirical … The framework's content closes this possibility" | as O1 | "Within the model, super-BQP computation is excluded by hypothesis. Whether physical computation satisfies the model is empirical." | no |
| O4 | Comp:106; ch14:100 | hypothesis lists | mismatch (§2 item 4) | Make both lists identical to Comp:94 / ch14:12: add uniform local descriptions, polynomial time and polynomial-overhead simulation to Comp:106; add encoding, fault tolerance and the clock model to ch14:100 | no |
| O5 | Comp:268, 286; book/README.md:82 | "*The framework establishes (theorems):*"; "a structural theorem about the computational ceiling"; "The conditional BQP model theorem is proved in two directions" | conditional → unconditional in a summary; "proved" for a definitional result (I1) | "*Conditional results (hypotheses of §4):*"; "a conditional characterization of the computational ceiling"; README:82 "Under the model's hypotheses, both bounds follow: …" | no |
| O6 | Comp:114 | "This modification has empirical consequences." | none named (I5) | "This suggests an interpretation." | no |
| O7 | Comp:15; ch14:150, 270; ch15:8 | "the cost of marginal-statistics observation"; "as cost of partial observation" | interpretation stated as content | "interpreted, under the model, as …" (ch14:150 heading: "Task-specific quantum advantage: an interpretation") | no |
| O8 | Comp:122 | "The forced position."; "in one theorem-level respect" | Lemma 3 calls the maximal-entropy measure "a selection principle, not uniqueness from invariance alone" (Main:54) | "Under a finite classical substratum …"; "under the maximal-entropy selection of [Main] Lemma 3, …" — the status of finiteness and Lemma 3's wording to be taken from the landed text, since D224 deletes posit (ii) and D260 rewrites Main:54 | **#1477** (D224, D260) |
| O9 | Comp:17, 174–182, 204; ch14:184 | "not a chosen agnosticism but a structural feature"; "the principled version of this same observation" | no-go over all axiom systems from a sketch (I9) | "No derivation of either answer to P vs NP is given; the §4 ceiling is compatible with either answer (§5.2)." Drop "not a chosen agnosticism" and "the principled version" | no (ch14:184 named in the owner decision) |
| O10 | Comp:17, 200; ch14:186 | "stronger than Aaronson's … at the BQP boundary"; "*Stronger:* the framework commits to BQP exactly" | an assumed ceiling compared with a posited principle (I10) | "Under the §4 model the ceiling is conditional; the framework adds no principle at the P vs NP boundary." | no |
| O11 | Comp:17 | "BQP advantage is maximized for problems whose hidden structure matches the framework's gauge group" | abstract stronger than body (Comp:246) | "BQP advantage correlates with SU(2)-compatibility (conjecture, §7.2)" | no |
| O12 | Comp:246, 248 | "(v5)"; "recorded in the framework's working archive (record §B.2.191)" | revision label and internal record reference (§A.27, §A.33) | Remove both | no |
| O13 | ch14:264, 270 | "The framework therefore predicts a specific limit on future quantum-computing capability" (ch14:264); "the framework's positive contribution to computational complexity theory" (ch14:270) | conditional → prediction | ch14:264: "Under the model, the BQP bound applies to future hardware."; ch14:270: "The chapter's content is therefore a conditional characterization, under §14.4's model, …". ch15:8 already conditions "established" on Chapter 14's explicit model hypotheses and is not proposed for edit | no |
| O14 | ch18:322 | "empirically engaged at near-term experimental scales" | Comp:130: nothing probes the ceiling before ~10³ logical qubits | "… exposed to any demonstrated super-BQP computation; no current experiment approaches the width ceiling." | no |

## 4. Proposed Lean formalization ladder (plan only)

Nothing below is written. Mathlib is pinned at `v4.33.0` (`verification/lean-mathlib/lakefile.toml`).
At that tag, by file and module-name inspection of the public source: `Mathlib.Computability.*`
provides Turing machines including `TM2ComputableInPolyTime`
(`Mathlib/Computability/TuringMachine/Computable.lean`), `Encoding`, `Partrec` and `Primrec`;
`Mathlib.Analysis.Asymptotics.Defs` provides `IsBigO`; `Matrix.unitaryGroup` and
`Matrix.kroneckerMap` exist. `Mathlib.lean` lists no module whose name mentions quantum
computation, BQP, BPP or probabilistic machines. Absence of Solovay–Kitaev and threshold
theorems was not checked beyond module names (**unconfirmed**).

| Level | Statement | Infrastructure | Establishes | Does not establish |
|---|---|---|---|---|
| L0 | I12 as a bound: for `f : α → α` on a `Fintype` and a halting set `H`, the orbit of `x` meets `H` iff it meets `H` within `Fintype.card α` steps (decidability itself is classically trivial; the bound is the content) | Mathlib only | the Comp:74 / Comp:190 fact | anything about complexity |
| L1 | Definitions: circuits over a fixed exact gate set (Hadamard + Toffoli, real amplitudes, so no Solovay–Kitaev); acceptance probability; uniformity as `Nonempty (TM2ComputableInPolyTime …)` for the map generating circuit descriptions (the structure is data, not a `Prop`); `BQP` as a set of languages with 2/3 vs 1/3. Sanity controls: closure under complement; a language decided by a uniform family of classical reversible circuits lies in `BQP` | new module, Mathlib `Computability` | a definition carrying uniformity as a machine, not an abstract predicate | any relation to OI; agreement with Comp:98's H/T/CNOT + Solovay–Kitaev definition, which needs the Shi / Aharonov universality theorem for Hadamard + Toffoli |
| L2 | Upper-bound schema (§A.34 direction 1): a family of `KrausSound` finite operational theories in which each admissible step is supplied with a uniform polynomial-size circuit, composed adaptively with deferred measurement and postselection charged by repetition, decides only `BQP` languages | L1 + `KrausSoundness`, `StinespringAssembly` | the composition and conditioning bookkeeping of I3 | the efficiency hypothesis; that OI dynamics supplies it |
| L3 | Lower-bound schema (§A.34 direction 2, a separate preregistered question): a family with `HasCompositeUnitaryControl` and unit cost per supplied gate realizes every L1 uniform family with linear overhead | L1 + `fullInstruments_of_control` | the realization bookkeeping of I2 | that the control or the unit cost is native |
| L4 | Research question, not a formalization target until a paper result exists: a cost statement about the native step (`depth_two_circuit`), e.g. per-step classical reversible circuit size linear in the number of sites | `SecondOrderCircuit` | a kernel statement about the substratum rule itself | any complexity class of physical computation without a coverage premise |

L2 and L3 together would certify the two directions of I1 as stated, conditional on their
hypotheses; they would not change any status in §1.1. Each new module needs a census family
with an anchor in the same commit (§A.35).

## 5. Unconfirmed items

- Mathlib content beyond the files and module names inspected (§4).
- I9: the reading that §4's model hypothesis is a bridging premise is checked against Comp:17
  and Comp:180, not Comp:178 (independent review of #1488).
- §2 item 3, third bullet, is BORDERLINE: a finite witness for chosen gate sets.

## Files

- `AUDIT.md` — this file.
- `checks/lie_closure.py` — the exact computation of §2 item 3. Run `python3 -I checks/lie_closure.py`;
  expected output ends `OK` after printing 2, 9, 49, 4 and 49. Standard library only.
