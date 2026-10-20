# Node 5: the precise additional postulate, its compatibility with OI, and its predictions

Research only, consistency axis (§A.23). F2 stays A1 (exact finite operational QM on qubit-power registers). No
premise adopted, no status changed, nothing written to `main`, nothing pushed.

**Base.** Thread records at `research/missing-component-20261020` = `b0481e08` (N1 = `../oa-node1/NODE.md`, MC1 =
`../mc-node1/NODE.md` with node 1b, MC2, MC3, MC4 = `../mc-node{2,3,4}/NODE.md`, PLAN = `../PLAN.md`, each with its
review outcome). `main` = `55a0e80a`; `papers/` and `verification/lean-mathlib/` are identical to `df9e601e`
(`git diff --quiet`), so paper and Lean lines hold at both. Every [AT] name was confirmed by `git grep` of its
declaration at `55a0e80a`; Lean paths are under `verification/lean-mathlib/OIBridge/`. LG =
`f2-ledger-20261020/LEDGER.md` at `3ecdefe9`. MEMO = `f2-decision-memo.md` at `acfef447`. I = thread I
(`f2-research-threads/I-f2-sufficiency-target.md`) at `804843f1`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (`probe/p5.py`, SymPy
1.14.0, Python 3.13.16, `-I -B`, two runs byte-identical); [UP] unsourced premise; [L] literature; [rec] recorded in
the cited record, not re-derived.

**Productivity test (fixed before the node, from the brief).** The node is a gem iff it gives a postulate statement
strictly sharper than PLAN's current form clauses (PLAN:141–154), and either proves the necessity of each clause (each
shown needed by a cited node result or a new check) or exposes a hidden assumption. The owner's requirements of
2026-10-20 (minimal postulate, compatibility, the (i)/(ii)/(iii) classification, a distinguishing prediction, negative
results permitted) arrived during the node. They are answered in §1, §4, §5 and §7; the test was not changed.

***

## 0. Headline

1. **Minimal postulate.** The weakest content that delivers O-A is fixed by an adopted kernel equivalence:
   relative to `SourcedOI`, which the sourced theory satisfies, exact QM holds iff phase-free richness (PFR) holds,
   one continuously driven pair per level [AT, both directions]. This is GR's controllability resource
   (GR.md:250, :256–264). Under Origin_K, the weakest content that adds O-B on top of it is state–operation
   compatibility and test validity (X-4, X-5) for the available operations under the Ad identification [W; AT at the
   pair]. Each minimal content coincides with a reading the gates exclude: PFR stated as a premise is E0 (MEMO:200),
   and X-4 stated as a premise is the bare transfer clause (MEMO:155, :202). **No acceptable single postulate is
   found.** An admissible postulate has to entail these contents and carry its own sourcing argument (G2 (ii)), and no
   source exists in OI for the constructions examined.
2. **Primitive-level form.** Over the native class, with finite protocols (A1, `InstAvail`), any generating set for
   PFR must satisfy four mutually irredundant clauses: U (an uncountable alphabet), M (some primitive outside the
   row-monomial class and some outside the column-monomial class), O (a primitive outside `OnesNormal`) and R (a
   primitive with no real Kraus form). This is sharper than PLAN's clauses in three places: R is missing from PLAN;
   PLAN's "non-classical kind" is satisfied by destructive non-configuration tests, which do not suffice (an exact
   countermodel meets every PLAN clause and stays monomial); and PLAN's "uncountable non-monomial family" need not be
   one family (MC4's M\*). The four clauses are necessary. Their joint sufficiency is not shown.
3. **Classification of the missing ingredient: (iii) for the framework as stated, scoped to the constructions
   below.** (i) is ruled out for every construction the thread examined. Its core (M, R) needs a process of
   non-classical kind, which contradicts Lemma 3's classical bijective form (Main.md:56) as the realizer of available
   operations, or else the closure of the observation triple (Main.md:44). Main.md:62 labels that form a
   representation choice, not a theorem. Its A1 increment (U, O) also conflicts with Lemma 1 (Main.md:48) for
   operations the observer selects, and with E3 and the boundary-layer reading (Substratum.md:92; GR.md:112, :134) for
   any continuum that carries them. The ingredient becomes (ii) only after an explicit change of the substratum class.
   GR.md:260–264 already describes exactly that change ("an assumption on the substratum class", "an empirical
   extension of the current substratum").
4. **G6.** None found. The postulate as stated has no distinguishing regime. By construction it reproduces QMfin on
   its domain. Its A1-specific clauses (U, O) are inert at every finite precision, because the A2 theory of MC2
   reproduces every finite-precision statistic [W from the definitions; EC instance G3]. Each regime examined either
   needs extra structure with a free scale, which §A.29 rejects, or reproduces a known QM result.

***

## 1. Q1: the candidate postulate P\*

### 1.1 Theory level: the content is pinned [AT]

- `sourcedOI_qm_iff_phaseFree` (SubstratumInterfaceAudit.lean:654): `SourcedOI T → (ExactAllFiniteEndomorphicQuantumOps
  T ↔ PhaseFreeRichness T)`.
- `sourcedOI_of_qm` (:636): QM implies `SourcedOI`. `permTheory_sourcedOI` (:660): the sourced theory satisfies it.
- So, for every theory T: QM(T) ⟺ `SourcedOI T` ∧ PFR(T). PFR (MinimalRepertoire.lean:423) asks, at every level with
  at least two states, for one pair (a, b) with conj(exp(−it(|a⟩⟨b| + |b⟩⟨a|))) available as a one-outcome family for
  every real t, and for every exchange.
- **Necessity is universal, not scoped:** any extension of OI that reaches A1 satisfies PFR (`.mp`). **Sufficiency is
  relative to `SourcedOI`** (`.mpr`). The two directions have separate kernel witnesses (§A.34).
- The corpus already states this content: GR.md:250 (phase-free richness), the box GR.md:256, and GR.md:258 ("the
  nonclassical repertoire the equivalence consumes is one continuously driven transition together with the exchanges
  ... the quarter phase is dispensable"); GR.md:262–264 (the controllability resource "is not entailed by A1–A6").
  LG OI-7 records it (LEDGER.md:46). This part is CONFIRMING.

**One family carries all four primitive clauses [EC P0–P5].** At level two (four states), the transition flow F(t) on
a pair, with a third point present, is:
- non-monomial at t = π/4 (P1);
- off the all-ones ray at t = π/2: F(π/2)·1 = (−i, −i, 1, 1) (P2; the kernel's `onesTheory_no_quarter_flow`
  FlowEndpoint.lean:119);
- not real up to a scalar (P3);
- a distinct ray for each t (P4).

At level one the same flow fixes the all-ones ray (P5). This is why PFR is stated at every level, and why the TU flows
of MC1 T1, which are level-one flows on a token, stay inside `onesTheory`.

### 1.2 Primitive level: four necessary clauses

Setting: the native class N (every permutation of every carrier, CNOT included; configuration readout; configuration
or uniform attach; discard; feed-forward; coarse-graining) plus an added alphabet A of primitive instruments.
Availability is generated by finite `InstAvail` protocols, with no completion rule (A1 as adopted, MC1 §9.3). RM and
CM denote the classes of matrices with at most one nonzero entry per row, respectively per column. Every Kraus
operator of N lies in RM ∩ CM.

| clause | statement | necessary because (the result that fails without it) |
|---|---|---|
| **U** | A is uncountable up to scalars | Kraus-word lemma (MC2 §2.1) and CR (N1 §2.1): over a countable alphabet the available level-one conjugations lie in countably many rays, so `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218) excludes QM. PFR needs uncountably many rays (P4) |
| **M** | A ⊄ RM and A ⊄ CM | [W, EC M1]: RM and CM are each closed under products and under tensoring with the identity (M1a–c, exhaustive at the pattern level for 3×3), and an invertible matrix in either class is monomial (M1d). If A ⊆ RM or A ⊆ CM, every Kraus word is in that class, a one-outcome conj(V) has V ∝ a word (Choi rank one, MC2 §2.1), so V is monomial and the Hadamard channel is unavailable. This refines MC3's κ-drop (κ1 mixed to κ4 keep A ⊆ RM ∩ CM), MC4's monomial no-go (a coherent prior is RM) and LG's monomial-branch lemma (LEDGER.md:116–123) |
| **O** | some primitive family {K_j} has 1 ∉ span{K_jᴴ1} | MC1 T2: `instAvail_onesNormal` (InstrumentRealization.lean:313) with the readout case widened, then `instAvail_unitary_fixes_ones` (:398). PFR's quarter flow at level two moves the all-ones ray (P2) |
| **R** | some primitive has no real Kraus decomposition | [W, EC R2]: real Kraus forms are closed under products, tensoring, readout, attach and discard, so every available family has real Kraus operators; S is not real up to a scalar (R3), so `PhasesAvailable` and QM fail. G4's reality clause (MEMO:187), absent from PLAN's form clauses |

The source clause **S** (N1 CR; MC3 §7): for U, some available primitive is not a function of a substratum process and
a countable context, or the substratum is infinite and of non-classical kind. This clause concerns the source, not
the theory. §4 shows what it costs.

**Drop-one countermodels: each satisfies the other three clauses and is not QM.**

| dropped | countermodel | why not QM |
|---|---|---|
| U | {H, T = diag(1, e^{iπ/4})} | countable: `countable_not_pairFlowSourced` [AT]; the kernel's own instance is `fixedGateTheory_not_qm` (DiscreteCompletion.lean:1948) |
| M | {diag(1, e^{iθ}) : θ ∈ ℝ}, or that family with destructive non-configuration tests in every real basis | A ⊆ CM, so every unitary channel is monomial (M2c–d: 2 992 words, 1 286 of them unitary up to a scalar, all monomial); the first is inside `substratum_residual` (StructuralClosure.lean:383) |
| O | MC1's TU (Lüders tests in the Y basis and every real basis) | `OnesNormal` (O1; MC1 T2) |
| R | {R_y(θ)} with real Lüders tests and Z | real (R2: 584 words, all real); R_y meets M and O (R1, O3) |

**PLAN's clauses do not suffice [EC M2].** The second M countermodel meets every PLAN clause:
- non-configuration tests are present (κ4 dropped);
- Z = diag(1, −1) is outside `OnesNormal`;
- the destructive test Kraus operators ⟨w(φ)| ⊗ I form an uncountable non-monomial family;
- diag(1, (3+4i)/5) breaks reality.

Yet all its primitives are CM (M2a), and no Hadamard-type channel arises (M2d). MC1 T5 already records that destructive
tests give column-monomial branches. What is added here is that PLAN's form statement does not carry that lesson, and
clause M does.

**The criterion bites in both directions [EC M3].** A coherent preparation of |+⟩ (RM, not CM) and a destructive
Y-basis test (CM, not RM), with the native CNOT, give branches ∝ exp(∓iπ/4 X) (M3b). A native X on one outcome makes
the channel deterministic (M3c, M3d). So a Lüders update is not required. Separate RM-breaking and CM-breaking
primitives suffice for a non-monomial deterministic unitary. This corrects the wording of AW-MC4 ("Only their
combination, the Lüders update, gives coherent control"): the combination need not sit in one primitive. In
coherence-theory terms, CM is the Kraus class of incoherent operations (IO), RM is its adjoint class, and RM ∩ CM is
the Kraus class of strictly incoherent operations (SIO). M3 is the qubit instance of "IO plus a maximally coherent
resource implement unitaries" [L, §6].

**U and M may sit in different primitives.** In MC4's M\* the uncountable family {R_z(θ)} is monomial, and
non-monomiality comes from one fixed X-basis test (MC4 §2.2, review O1–O3 [rec]). So PLAN clause 3's "an uncountable
non-monomial family", read as one primitive family, is not necessary. Read as a property of the generated theory it is
the conclusion, not a constraint. This is ELABORATING (MC4 already implies it).

### 1.3 Necessary versus only possible

- *Necessary given the gates.* The theory-level content (PFR) is necessary for every extension that reaches A1
  [AT `.mp`]. The four primitive clauses are necessary for every extension whose availability is generated by finite
  protocols over a fixed alphabet with the native class.
- *Not the only possible postulate.* Other routes replace clauses:
  - a completion rule admitting almost-surely terminating protocols replaces O (MC2 F1);
  - the dense-endpoint relabellings F6–F8 replace U (MC2 §2.3), and the gates bar them;
  - a change of identification (κ3) is barred by G3.
  The clauses say nothing about extensions that change the availability notion itself.

### 1.4 Sufficiency, as its own question (§A.34)

- **Shown sufficient:**
  - PFR with `SourcedOI` [AT `.mpr`];
  - TU with a deterministic Z [MC1 T4: EC, L Barenco et al., W];
  - M\*: a continuum of phases, one X-basis test and the native class [MC4: W, L].
- **Not shown:** that U ∧ M ∧ O ∧ R suffices. Two steps are missing. U at the alphabet level does not force
  uncountably many unitary rays: MC3 B3's unsharp configuration tests are uncountable and add only mixtures. And M
  gives a non-monomial word, which is not shown to always yield a non-monomial deterministic unitary. No countermodel
  to sufficiency was found. **No equivalence is claimed at the primitive level.**

***

## 2. Q2 (owner item 2): compatibility of each clause with OI

| clause | E3 and the boundary layer (Substratum.md:92; GR.md:112, :134) | κ1–κ4 (MC3 §2) | CR (N1 §2.1) | G2 / G3 | verdict |
|---|---|---|---|---|---|
| M | leaves E3 intact: a finite non-classical boundary is allowed by the dimension cutoff | contradicts κ2 ∧ κ4 as the realizer. By MC3's cone lemma, a classical substratum realizes only diagonal effects at any cardinality, so an available non-configuration test realized by substratum dynamics needs κ2 dropped. Otherwise it is a non-supervenient primitive. Dropping κ1 alone is RM and fails (MC4). It extends the readout of Main.md:632, which itself assigns non-commuting interventions to the instrument algebra, but that extension needs a realizer | not engaged (M is not a counting clause) | G3 intact. G2 open: no source | contradicts Lemma 3's classical bijective form (Main.md:56), or the closure of Main.md:44 if non-supervenient |
| R | intact | as M: a configuration bijection has a real Kraus form (`permTheory_no_sign` SubstratumInterfaceAudit.lean:680; MC3 C1) | — | — | as M |
| O | intact | contradicts realizability by bijections. The native class is ones-fixing (`permClass_onesFixing` PhaseSource.lean:79). GR.md:260 states the phase intervention "enters as an assumption on the substratum class, not as a consequence of the finite states with the bijective read-write dynamics" | — | E0 if posited (MEMO:200) | needs a changed substratum class |
| U | **the substantive issue.** E3 bounds the visible sector and boundary layer to dim ≤ e^{A/4} (Substratum.md:92). An infinite coherent sector coupled at leading order, MC4's M\*, contradicts it. An infinite deep sector is licensed only when decoupled (no effect) or coupled slowly. Its effect is then O(t/τ_B) (Substratum.md:92), about 10^{−32} for laboratory processes (GR.md:134, boundary-only dependence lemma GR.md:112). That is too slow by that factor to carry O(1) exact operations on accessible timescales [W] | with κ2 kept, real data give only convex weights (MC3 B1–B3) | needs an uncountable context or an infinite substratum | G7: a real datum must be fixed in X's statement | see the two readings below |

**The two readings of U.**
- *(a) Within one realization, the operations are ones the observer selects.* Lemma 1 (Main.md:48) gives the observer
  finitely many distinguishable internal states, and Main.md:44 couples it to the rest only through φ. A setting
  recorded in the observer, or in a boundary apparatus under E3, takes finitely many values per experiment and
  countably many over growing experiments. Under this reading, exact A1 availability contradicts Lemma 1 together
  with E3, for every construction, classical or not, whose settings are physical records [W]. This is CR's P2 with
  Lemma 1 as the reason the contexts are countable.
- *(b) Across realizations, a real coupling is a realization datum*, as the prior is (Main.md:60). With κ2 kept, such
  data give mixtures (MC3). With κ2 dropped, a finite non-classical boundary with real couplings gives uncountably many
  unitaries. This is compatible with E3 and Lemma 1, but it is again the κ2 change of row M. F2's Origin is stated per
  realization (I:308, H0), so reading (a) is the one the target uses.

**The boundary-layer conflict is not specific to M\*.** Every route to an A1 continuum found in the thread has to put
the continuum in one of three places:
- the boundary layer at leading order, which E3 as read bars;
- the deep sector, which acts only at O(t/τ_B);
- non-physical (non-supervenient) settings, which go against Main.md:44.

This is a tension between OI's foundations and the A1 target, not a presentation problem. It does not touch A2: MC2's
three fixed bases give `DenseFiniteQM` with a countable alphabet, so at A2, U and O are not needed. M and R still are.

***

## 3. Q3: O-B

**What P\* must add (Origin_K) [W; AT at the pair].** Given P\*_A (full control under the Ad identification), take
the domain of LG §2.2: products of configuration states, a convex cone, and hmax (K ⊆ maxCone). Then K = Q3 iff X-4
(every available operation preserves K) and X-5 (every available test is valid on K).
- *⟸.* For X ∈ K and any pure ψ, choose an available U with Uψ = |00⟩. X-4 puts UXU† in K ⊆ maxCone, so
  ⟨ψ|X|ψ⟩ = ⟨00|UXU†|00⟩ ≥ 0, and K ⊆ PSD. X-4 applied to |00⟩⟨00| reaches every pure state, so K ⊇ PSD.
- *⟹.* Unitary conjugation preserves PSD, and effects are positive.

At the pair, `pairCone_eq_Q3_iff_drive_maxCone` (EqvK2MaxCone.lean:174) gives the same with only CNOT, the drive and
the cyclic map [AT].

Exact instances [EC B1, B2]:
- each non-PSD fixture element (Γ(Bell) ∈ Γ(Q3), z₁,₁ ∈ K(Z_F), SWAP ∈ maxCone) is carried by an exact unitary to an
  element with product test |00⟩⟨00| equal to −1/2, −1/2 and −1;
- the PSD controls stay nonnegative under the same unitaries.

So with P\*_A and X-4, every listed fixture is excluded at the pair. Γ(Q3) is excluded already by X-4 for the native
CNOT (B5; MEMO Fact B).

**Correction to PLAN clause 4.** PLAN:153 says the component "includes the G3 identification and multi-token
compatibility clauses". LG's AW-F1 (LEDGER.md:300–303) says a source for O-B needs multi-token native protocols (Σ3)
*or* non-native operations (hA). With P\*_A the non-native drive is available, so the pair-level hA route is open, and
multi-token clauses are one route, not a necessary one. This is CONFIRMING: the ledger had it right, and PLAN
overstated it.

**Does O-A imply any of O-B? No, in either direction [W; EC B3, B4].**
- (P\*_A, K = maxCone) has full control and fails X-4: CNOT carries SWAP ∈ maxCone outside it (B3). Availability does
  not imply preservation (MEMO:139, BCR).
- (`permTheory`, K = Q3) satisfies X-4 and X-5 under the Ad identification (B4) and fails O-A (`permTheory_not_qm`
  :716).

Within a source, O-A can carry part of O-B. For TU, pair-level compatibility is automatic, because a local Lüders
filter maps maxCone into SEP (MC1 §3 item 5 [rec]). P\*_A as stated carries none.

**What OI already supplies [corpus check, §A.19].**
- *The Ad identification, at representation level.* Main.md:280 gives the unitary realization (U_φ, Kraus
  K_kl = m^{−1/2}⟨l|U_φ|k⟩), Main.md:532 sets U_φ|x, h⟩ = |φ(x, h)⟩, and GR.md:282 says the substratum update extends
  to the quasilocal algebra. This fixes Ad_P for native operations as the framework's representation. G3 asks for an
  exclusion *relative to* that identification (MEMO:186), so the identification is framing and is supplied. LG lists
  it as (d) (LEDGER.md:93) because it is not operationally determined: GR.md:204's operational orientation no-go shows
  that operational data cannot select a completion over its transpose, and Γ is the token-local analogue.
- *The diagonal shadow.* Configuration tests are valid on configuration states, and native permutations preserve the
  diagonal. The classical register family satisfies every sourced premise (Σ0, LEDGER.md:179).
- *Nothing off-diagonal.* The purification uniqueness that would give O-B is a posit (Main.md:602; MC2 §3).
- *Under Origin_M, O-B collapses.* X-4, X-5 and G3 follow from the inherited complex carrier (I:482, R14), with the
  kinematics inherited, not derived (I:524, AW-I4). The single postulate is then PFR.

**Gate status of the O-B content.** Stated as a premise, X-4 for the available operations is the bare transfer clause
(MEMO:155) or LO (MEMO:202), which G2 rejects. Fact A permits a principle that is equivalent to cone selection, but not
one that renames it.

***

## 4. Q4 (owner item 3): the strategic classification

**(i) Can it emerge from OI? Ruled out for these constructions:**
- supervenient realizations on the finite bijective substratum: CR (N1);
- classical enlargements of any cardinality, time model, coupling or setting, and their channel limits: the cone lemma
  (MC3);
- a coherent hidden prior with κ2–κ4: monomial unitaries only (MC4);
- every `OnesNormal` measurement extension, sharp or unsharp Lüders: MC1 T2;
- word-type completion rules: MC2 §2;
- logarithm-branch interpolation: N1 §3, a G7 knob;
- the global antiunitary: MC3 §5;
- the canonical purification with bijective purifier maps: MC4 E7.

This is not a claim about every observer-level extension.

**(ii) or (iii)?** Each clause either changes a stated foundation or is a gate-excluded posit (§2):
- M and R need a non-classical process (against Main.md:56 as realizer, a representation choice per Main.md:62) or a
  non-supervenient primitive (against Main.md:44);
- O needs a changed substratum class (GR.md:260);
- U needs, under the target's per-realization reading, more than Lemma 1 and E3 allow (§2 (a)), or a continuum that E3
  places too slowly coupled to act (§2).

None of the constructions examined adds the ingredient while leaving all of Main.md:44–62 and Substratum.md:92
intact. So the classification is **(iii) incompatible with the current framework as stated**.

**Where the conflict sits.**
- For M, R and O it sits at a declared representation choice (the classical bijective substratum, Main.md:62), not at a
  theorem. GR.md:260–264 already presents the controllability resource as a change of the substratum class. Making
  that change explicitly turns the ingredient into a (ii)-type principle, at the price that OI's substratum is no
  longer classical in the boundary layer.
- For U it also involves Lemma 1, a theorem, under the per-realization reading (§2 (a)).

**What is empirically at stake.** The conflict carried only by U and O is a conflict with the A1 target definition.
At A2 those clauses are not needed (MC2), and no finite-precision experiment separates the two endpoints (§5). The
conflict carried by M and R is substantive at every precision, since it concerns the kind of process.

***

## 5. Q5 (owner item 4): an independent prediction (G6)

**The owner's observation, made exact.** P\* is designed so that the extended theory is QMfin on qubit-power
registers, with M1 keeping every native law (§7 control 2). On that domain its statistics are QM's, so no experiment
within the domain distinguishes it from QM. A distinguishing prediction needs a regime outside the domain or extra
structure.

**A1-specific clauses are inert at finite precision [W from definitions; EC G3].** `KrausDense` (DiscreteCompletion.lean:52)
asks for every instrument to be approximated outcome by outcome in operator norm. Finite experiments are finite
compositions of instruments, so their probabilities are continuous in the instruments [W]. So a theory meeting A2 (for
instance MC2's `TU_fin`: countable, `OnesNormal`) reproduces every finite-precision statistic of QM. The instance: a
|+⟩ preparation and an X test separate Φ_n from Ad Z by exactly 2^{−n} (G3). So no finite-precision prediction can
attach to U or O. G6 for P\* would have to come from M or R (A2 content) or from structure outside the operational
target.

**Regimes examined.**

| regime | does P\* as stated differ from QM there? | verdict |
|---|---|---|
| A1 versus A2 | no at finite precision (above) | not testable |
| E3 cutoff (a finite boundary of dimension D ≤ e^{A/4}) | a finite-boundary variant has countably many exact operations, so it fails A1. It can still be dense, so it forces no finite-precision deviation. E3 bounds D only from above | adjustable from below: rejected (§A.29). Refines MC4 §5, where the scale was called free: E3 fixes an upper bound, not a scale |
| a slowly coupled deep continuum | operations would need times ~τ_B (GR.md:134) | contradicted by laboratory gates. A failed variant, not a prediction |
| native versus non-native split | P\* as stated assigns no statistical difference. A variant in which non-native operations consume a finite reference (a phase reference, [L] Bartlett–Rudolph–Spekkens) predicts degradation of non-native operations only, in a preferred configuration basis | needs extra structure with a free size and degradation law: rejected as stated; recorded as the one direction with a possible regime |
| reality (R) | complex QM is distinguishable from real QM in network tests [L: Renou et al. 2021] | reproduces a known QM result, and R was built in to meet G4. Does not qualify |
| local dimensions other than 2^k (B2) | P\* is silent | outside the domain |
| native statistics | identical by M1 and control 2 | none |

**Verdict: no distinguishing prediction found. The postulate as stated has none.** Any G6 needs added structure, and
the one candidate (consumable reference, native/non-native asymmetry) has a free scale.

***

## 6. Literature (Step 4)

Bibliographic data below are from memory and were not re-verified in this node; no full text was read here.
- Reconstructions: L. Hardy, quant-ph/0101012 (2001); G. Chiribella, G. M. D'Ariano, P. Perinotti, Phys. Rev. A 84,
  012311 (2011); Ll. Masanes, M. P. Müller, New J. Phys. 13, 063001 (2011). Each posits continuous reversibility or
  purification with uniqueness. In this node's terms, each posits the theory-level content (PFR, transitivity) rather
  than a primitive source (MC3 §6 [rec]).
- Coherence resource theory: T. Baumgratz, M. Cramer, M. B. Plenio, Phys. Rev. Lett. 113, 140401 (2014) (IO, Kraus
  operators mapping incoherent to incoherent states, i.e. CM); A. Winter, D. Yang, Phys. Rev. Lett. 116, 120404 (2016)
  (SIO, i.e. RM ∩ CM); B. Yadin et al., Phys. Rev. X 6, 041028 (2016); K. Ben Dana et al., Phys. Rev. A 95, 062327
  (2017) (implementing unitaries under IO with coherent resources); E. Chitambar, G. Gour, Phys. Rev. Lett. 117,
  030401 (2016). Clause M is "leave IO and its adjoint class". The native OI class lies in SIO. MC3's cone is the
  nonnegative part of the partial-permutation (PIO-type) class.
- Imaginarity: A. Hickey, G. Gour, J. Phys. A 51, 414009 (2018); K.-D. Wu et al., Phys. Rev. Lett. 126, 090401 (2021).
  Clause R is "leave the real (free) operations".
- Real versus complex QM: W. K. Wootters and L. Hardy, Found. Phys. 42, 454 (2012); M.-O. Renou et al., Nature 600,
  625 (2021).
- Gadgets and universality: X. Zhou, D. W. Leung, I. L. Chuang, Phys. Rev. A 62, 052316 (2000); A. Barenco et al.,
  Phys. Rev. A 52, 3457 (1995).
- Reference frames: S. D. Bartlett, T. Rudolph, R. W. Spekkens, Rev. Mod. Phys. 79, 555 (2007).

The resource-theoretic reading puts the native class inside the intersection of three free classes: incoherent (SIO),
real, and ones-fixing. It puts O-A at leaving all three plus countability. That reading is standard in kind; only its
application to OI's native class is particular to this thread.

***

## 7. Controls fixed in advance (§A.29), from PLAN:47–53, with outcomes

| # | control | outcome |
|---|---|---|
| 1 | `permTheory` and the monomial class stay non-QM with the addition removed | holds: removing A returns `permTheory` (`permTheory_not_qm`). Must-fail instances: the CM countermodel stays monomial (M2c–d). Can-fail countercontrol: separate RM- and CM-breakers produce a non-monomial unitary (M3) |
| 2 | rooted law and M1 on retained protocols | holds by construction for an additive P\* that keeps configuration readout [W]: the native protocols are the same Kraus words. Not a computed check; a computation would only reproduce. Can-fail negative control: replacing the configuration readout by an X-basis Lüders test changes P(x₀, x₂) from (½, 0, 0, ½) to uniform (G1), while configuration readout is non-disturbing (G2). This is the E1-L failure mode M1 excludes |
| 3 | K_B, K(Z_F) and Γ(Q3) excluded by the candidate itself | holds only through the O-B content X-4 with P\*_A (B1, B5). K_B was not computed; it falls under the K ⊆ PSD argument if K_B ⊄ PSD, which LG records (witness −1/4) [rec]. Without X-4, P\*_A excludes nothing (B3) |
| 4 | no E0 positing; representability not standing in for availability | **fails** for the minimal P\*_A: PFR as a premise is E0. It can be met only by a source, and none is found |
| 5 | an independent prediction with a preregistered rule | fails: none found (§5). Decision rule fixed before §5: a candidate counts iff it gives a finite-precision statistic that differs from QMfin on some protocol, its size is fixed by the postulate or by an OI quantity without free parameters, and both outcomes are possible. No candidate met all three |
| 6 | `fixedGateTheory_not_qm` survives (MC2 §2.2) | holds: no completion rule is added |

***

## 8. Hidden assumptions and assumption-watch markers

| # | assumption | where | finding | class |
|---|---|---|---|---|
| HA-P1 | "non-classical kind (κ2 or κ4 dropped)" is enough for (a) | PLAN:142 | **exposed as insufficient.** Destructive non-configuration tests drop κ4 and stay CM. With phases, every PLAN clause holds and the theory stays monomial (M2). Clause M is the sharp form. The row/column split is MC1 T5's; the RM/CM classes are the IO classes of coherence theory [L] | BORDERLINE (the countermodel to PLAN's form statement), ELABORATING (the criterion) |
| HA-P2 | the form clauses carry G4 | PLAN:141–154 against MEMO:187 | reality is missing. A real rotation continuum meets U, M and O and is not QM (R1–R2) | ELABORATING (G4 lists reality; PLAN:13 too) |
| HA-P3 | "uncountable non-monomial family" is one primitive family | PLAN:152 | not necessary: M\* splits it (MC4) | ELABORATING |
| HA-P4 | AW-MC4: only the Lüders update gives coherent control | MC1 §5 | separate RM- and CM-breaking primitives with CNOT give a deterministic non-monomial unitary (M3) | ELABORATING (wording correction; standard gadget [L]) |
| HA-P5 | a weaker postulate than the controllability resource might deliver O-A | PLAN question | no: PFR is necessary for any A1 extension [AT]. The minimal content is E0, and the O-B minimal content is the bare transfer clause. The gates demand an explanans, not more content | CONFIRMING (LEDGER.md:46, GR.md:258–264) |
| HA-P6 | O-B needs multi-token clauses | PLAN:153 | not with non-native operations (AW-F1's own disjunction) | CONFIRMING |
| HA-P7 | the A1 target is compatible with OI's finite observer | MEMO §1.1 | under the per-realization reading, exact availability of an uncountable family conflicts with Lemma 1 and E3 (§2 (a)), and the only E3-licensed continuum acts at O(t/τ_B). The A1 increment is empirically inert (§5). Partly recorded: CR's P2 counts finite contexts, and MC4 places M\* against E3 | BORDERLINE |
| HA-P8 | a G6 for P\* could live in the A1 increment | brief | no: U and O are inert at finite precision | ELABORATING (immediate from `KrausDense`) |

Assumption-watch markers:
- **AW-MC5-1.** A claimed source for O-A at A1 states which of U, M, O, R it supplies. M is "outside RM and outside
  CM", not "κ4 dropped": destructive tests do not count.
- **AW-MC5-2.** Relative to `SourcedOI`, O-A's content is PFR exactly [AT]. Any admissible postulate entails it, and
  stating it is E0.
- **AW-MC5-3.** Under Origin_K with P\*_A, O-B's content is X-4 ∧ X-5. Stating it is the bare transfer clause.
  Multi-token clauses are needed only for sources limited to native operations.
- **AW-MC5-4.** The A1 increment (U, O) is empirically inert. A G6 must come from M, R or the source.
- **AW-MC5-5.** Under E3 as read (Substratum.md:92) and the boundary-only dependence lemma (GR.md:112), an A1
  continuum must sit in the boundary layer (barred), in the deep sector (O(t/τ_B)), or in non-physical settings
  (against Main.md:44).

***

## 9. Not verified

- The RM/CM closure and the real-Kraus closure are [W]. The exact checks cover pattern closure at 3×3 (exhaustive),
  words of depth ≤ 3 on one and two tokens, and finitely many rational instances of each uncountable family. The
  families are represented by instances; the CM property itself is structural.
- The necessity of M uses the Choi rank-one step of MC2 §2.1 [rec] and assumes the native class is RM ∩ CM. The uniform
  attach and discard are, by inspection; this was not machine-checked for every constructor.
- §3's ⟸ direction is [W] for general registers; it is exact only on the three fixture elements and at the pair through
  the [AT] theorem. K_B was not computed.
- §2's reading (a) and the O(t/τ_B) placement argument are [W]. They rely on Substratum.md:92 and GR.md:112, :134 as
  written. Whether a coherently coupled continuum could act at leading order through a finite boundary without counting
  as boundary layer is not settled.
- §5's continuity step (finite-precision statistics are continuous in the instruments under `ChanWithin`) is [W].
- Joint sufficiency of U ∧ M ∧ O ∧ R is open (§1.4).
- The (iii) classification is scoped to the constructions listed in §4. It is not a no-go for observer-level extensions
  outside them.
- The literature in §6 is cited from memory: bibliographic data not re-verified, texts not read here.
- [rec] rows (N1, MC1–MC4, LG, MEMO, I) were taken as recorded.
- No independent review has been run on this node.

***

## 10. Files (`probe/`)

| file | role |
|---|---|
| `p5.py` | blocks P (PFR flow), M (RM/CM criterion, CM countermodel, RM+CM countercontrol), R (reality), O (`OnesNormal`), B (O-B under full control, independence), G (M1 negative control, A1/A2 instance); 37 checks |
| `p5.run1.out`, `p5.run2.out` | 37 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | `p5.py` `4dad948f…ad4a`; both outputs `7191bbcb…025b` |

***

## 11. Productivity verdict

**Gem: yes, narrow,** under the fixed test.
- *A postulate statement strictly sharper than PLAN's form clauses:* the theory-level content PFR with both directions
  [AT]; the four primitive clauses U, M, O, R, with R added, M replacing the κ-drop, and U split from M; and the O-B
  content X-4 ∧ X-5 under Origin_K.
- *The necessity of each clause:* each is tied to a cited result or a new check (§1.2), with exact drop-one
  countermodels.
- *Hidden assumptions exposed:* HA-P1 (PLAN's clauses are jointly satisfiable by a non-QM theory) and HA-P7 (the A1
  target against Lemma 1 and E3).

**Classification: ELABORATING overall, with two BORDERLINE items** (HA-P1's countermodel to PLAN's form statement,
HA-P7's target–foundation tension). No item is claimed NEW:
- the theory-level content is in GR.md:250–264 and LEDGER.md:46;
- the RM/CM criterion is coherence-theory standard [L];
- R is in G4;
- the U/M split follows from MC4;
- the O-B reduction follows from the pair theorem and MC2 §3.

**Answers to the owner's items.**
1. Minimal content: PFR (and, under Origin_K, X-4 ∧ X-5). Both are gate-excluded as premises. No acceptable single
   postulate is found.
2. Compatibility: §2. M, R and O contradict the classical bijective realizer (a declared representation choice). U
   also conflicts with Lemma 1 and E3 under the target's reading. The boundary-layer conflict is general, not specific
   to M\*.
3. Classification: (iii) for the framework as stated, for the listed constructions. It becomes (ii) only by an explicit
   change of the substratum class, which GR.md:260–264 already describes.
4. G6: none. The postulate as stated cannot have one on its domain, and the A1 increment is inert.
5. Both negative results are stated as such.

***

## 12. Proposed PLAN text (not applied)

**Status bullet (after `mc-node4/`):**

> - **`mc-node5/`, the precise additional postulate: ELABORATING, two BORDERLINE items, [W/EC].**
>   - Relative to `SourcedOI`, which the sourced theory satisfies, exact QM holds iff phase-free richness holds, one
>     continuously driven pair per level (`sourcedOI_qm_iff_phaseFree`, both directions). This is GR's controllability
>     resource. Under Origin_K, O-B then adds exactly X-4 ∧ X-5 for the available operations. Stated as premises,
>     these are E0 and the bare transfer clause, so no acceptable single postulate is found. An admissible one must
>     entail them and carry a source.
>   - With finite protocols over the native class, a generating set needs: an uncountable alphabet (U); a primitive
>     outside the row-monomial class and one outside the column-monomial class (M); a primitive outside `OnesNormal`
>     (O); and a primitive with no real Kraus form (R). Each is necessary and the four are irredundant. Joint
>     sufficiency is not shown. Destructive non-configuration tests with phases meet every earlier form clause and
>     stay monomial.
>   - Classification: (iii), incompatible with the framework as stated, for the constructions examined. M, R and O
>     need a non-classical realizer (against Main.md:56, a representation choice per Main.md:62). U also conflicts
>     with Lemma 1 and E3 for selected operations, and E3 leaves a continuum only the deep sector, at O(t/τ_B). The
>     ingredient becomes (ii) only by an explicit change of the substratum class.
>   - G6: none. The postulate reproduces QMfin on its domain, and its A1 increment (U, O) is inert at finite precision.

**Form clauses (replacing PLAN:141–154):**

> **Form the missing component must take under A1, as the reviewed nodes have narrowed it:**
> - Theory level: it entails phase-free richness (necessary for every A1 extension; sufficient with `SourcedOI`).
>   Stated directly, that is E0.
> - Primitive level, with finite protocols over the native class (necessary, irredundant, not shown jointly
>   sufficient):
>   - U: an uncountable alphabet;
>   - M: a primitive outside the row-monomial class and one outside the column-monomial class. Destructive
>     non-configuration tests alone do not qualify, nor does a coherent prior with κ2–κ4;
>   - O: a primitive outside `OnesNormal`, or else a rule admitting almost-surely terminating protocols;
>   - R: a primitive with no real Kraus form.
>   U and M may sit in different primitives (`mc-node4`'s M\*).
> - Source: for U, non-supervenience or an infinite substratum of non-classical kind. Under E3 as read, a continuum
>   coupled at leading order is barred, and the deep sector acts only at O(t/τ_B).
> - O-B, under Origin_K: X-4 ∧ X-5 for the available operations under the Ad identification. Multi-token clauses
>   are needed only for sources limited to native operations (AW-F1). Under Origin_M, O-B is inherited.
> - G6: none. The A1 increment (U, O) is inert at finite precision, so a G6 must come from M, R or the source.
