# Review of FOUND-ASSESS-r1 (foundational assessment, candidates C0–C5)

**Reviewer.** Independent, non-author. Paper-only and read-only: no repository file edited, nothing committed or posted, no Lean build, no computation. Sources were read at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`, in the papers, the Lean sources under `verification/lean-mathlib/OIBridge/`, the A1 impact audit r9, and Issues #914, #866, #1169, #1147 and #1007. The Issues were read through `gh api`. Their extent is listed in §4.

**Verdict: REVISE.** The inventory in §1.1 is mostly accurate, and so are most kernel citations. The register is balanced, and the stop rule is respected: no premise is adopted and no model is built beyond small illustrations. But one blocking finding and several required ones change parts the brief asked for directly:

- the Bell elimination (§3) is missing a live option that Main:418 states explicitly;
- three of the six ranked questions (Q-A, Q-B, Q-C) rest on framings that the record or the owner's adopted rules contradict, and Q-D asks a question that GR:132 already partly answers;
- C5's prediction is stated more strongly than Main:562 and Main:566 allow, and C5 conflicts with the owner-adopted exact target, which the assessment does not mention.

A revision followed by a focused confirmation should be enough. Nothing here calls for restructuring the document.

Counts: **blocking 1** (F1), **required 16** (F2–F17), **recommended 12** (F18–F29).

***

## 1. Findings

### F1 — blocking — §0 summary, §3 intro and table, "two of the eight rows remain live"

**Evidence.** Main:418: "Wings separated by less than the graph cone over the experiment's duration fall outside the Corollary, including any that are spacelike with respect to an emergent light cone lying strictly inside the graph cone in some direction. If $c$ is the wave speed, these include wings that are spacelike with respect to $c$ … with $\Delta t/\sqrt3 < d \le \Delta t/\lVert\hat n\rVert_1$." Sub:131 says the same: which of the graph cone and the wave speed $1/\sqrt3$ is the physical $c$ "is not derived".

Loophole-free tests establish spacelike separation with respect to the physical light cone, not with respect to the reference graph cone. Two things follow:

1. The experiments contradict the conjunction of Main:414's hypotheses with a bridging premise: that the experimental wings satisfy (iii), lying outside the graph cone. That premise holds if the physical $c$ equals the graph speed in the relevant direction, or if the separation margin exceeds the graph cone. The record establishes neither.
2. The table omits an option. Hypothesis (iii) can fail *for the experiment* with no preparation-indexed edges at all: the wings lie inside the reference graph cone off the body diagonals. So "two of the eight rows remain live" is incomplete.

**Fix.**

- In §0 and the §3 intro, state what exactly is contradicted: Main:414's hypotheses *together with* the premise that the experimental wings lie outside the reference graph cone, which Main:418 does not derive.
- Add a row: "(iii) fails for the performed experiments: wings inside the reference graph cone (physical $c$ below the graph speed in that direction)."
  - **Mechanism:** influence through the reference rule at speeds between $c$ and the graph speed.
  - **No-signalling:** under item (vii) the remote effect of a setting change is a fixed linear image of the setting difference, so operational signalling is expected unless the readout averages it away. Nothing on record checks this.
  - **Assessment:** open. A short paper check would probably eliminate it; if it survived, it would predict anisotropic influence faster than $c$.
- Recount the live rows.

### F2 — required — §3 row "Graph locality …", C2 "Excluded by", Q-B

**Evidence.** Wood and Spekkens 2015 (to be checked first-hand; this is the reviewer's recollection) treat superluminal, superdeterministic (measurement-dependent) and retrocausal causal structures alike. Their conclusion is that every classical causal explanation of Bell violation compatible with no-signalling requires fine-tuning.

The assessment applies the result only to C2. Q-B then "separates C2 vs C3, C0". If the theorem covers measurement dependence, the fine-tuning question does not separate C2 from C3. §3's last paragraph half-recognizes this ("both reduce … to the same missing item").

**Fix.**

- State the fine-tuning obstacle for C3 as well: in its §3 row, in its "Excluded by", and in the C3 obligation "derived (untuned) initial law".
- Rewrite Q-B's "Separates" column as "C2, C3 jointly vs C0". Move the C2/C3 discrimination to the cost comparison: linearity and the SM/GR side for C2, initial conditions for C3.
- Keep the literature check as the first step and mark the scope "to be checked first-hand".

### F3 — required — Q-C, §3 last paragraph, §1.3 "Native preparation"

**Evidence.** The O-RDY plan r5 (#1147 c.6894144708) carries the owner's answers, confirmed at #1169 c.6894115930:

- **Q8 — no:** a departure of `R`'s unconditional marginal from `ρ_R` without an executed herald is "not native"; it is "*relative to `μ`*". Under rule N-8, "readiness carried by a measure, declared or derived, is not a source".
- **Q9 — no:** a use read conditionally on a held herald without gating by φ is "*representable only*". Only a herald-sourced conditional with gating by φ (R1a) can be native.
- **#866 c.6649267203:** D-OB7 stands, and D-OB8 records H-PREP, the identification of a laboratory preparation with conditioning on the observer's own records, as an open hypothesis.

Q-C(a) asks for a measure principle that "permits native preparation". §3 says native preparation "needs a non-invariant initial or boundary law". Under the adopted classification, a measure principle cannot by itself supply native preparation.

**Fix.**

- Replace Q-C(a) with: "is compatible with herald-sourced, φ-gated readiness (R1a) and does not itself carry readiness (N-8)".
- In §3, rewrite the third demand: native preparation needs an executed, φ-gated herald, and a non-invariant law yields readiness "relative to μ", which is not native.
- Name H-PREP (D-OB8) in §1.3.

### F4 — required — C5 (premises, obligations, standing), §1.4, summary table

**Evidence.** The owner's target decision #914 c.6875046763 (2026-11-14) adopts "Exact as the ultimate target", says "the target cannot assume one fixed finite total carrier", and says "Finite access by an embedded observer must remain distinct from finiteness of the underlying dynamics". The amendment c.6875548603 keeps "no assumption of one fixed finite total carrier; … exact as the ultimate target". The owner's foundational decision in the #1007 body (2026-10-30) reads: "The general formulation must **not require `|S|<∞`**. A finite `S` remains a valid *restricted model and proof premise*."

C5 predicts that exact quantum statistics fail. It is therefore incompatible with the adopted exact target (decision 2), in both its total and its per-patch form, because E8 applies to the configurations of the patch. The assessment does not say so. This does not count against C5 as a candidate; the owner's 2026-11-15 guidance admits it. But adopting C5 would require revising decision 2, and in its total form it would reverse #1007's framework choice.

**Fix.** Add to C5's obligations: "revision of #914 decision 2 (exact target), and for the total form of #1007's decision, by the owner". Add the same point to the standing column.

### F5 — required — §0, §2.1, C0 "Excluded by", Q-A

**Evidence.** By the amended target (#914 c.6875548603), OI is a superset of QM: inclusion, a sector condition C, and gravity. That amendment "removes the obligation that the OI side as a class imply QM". D-CQ (#1169 c.6891338304) defines C by the limits of embedded observation and leaves the relation between C and Q open.

§2.1's "OI → QM … refuted at three scopes" is accurate as mathematics. But the assessment never says that the adopted target does not require that direction. C0's exclusion criterion and Q-A are framed as excluding a finite law from OI as a class.

**Fix.**

- State the three-part target and D-CQ in §2.1.
- Restate C0's "Excluded by" and Q-A relative to the sector: "a sector C, defined from limits of embedded observation without reference to quantum outcomes, that excludes some consistent finite law or operational theory while covering the perceived quantum phenomena and agreeing with performed experiments".

### F6 — required — C5 "Independent prediction" and "Excluded by", §0, §1.4 "Observational constraint", C4 "Independent prediction"

**Evidence.** Main:562 is an exact statement: "no fixed finite realization is exactly operationally equivalent to even a single qubit's full theory", with "the unboundedness imported". Main:566: what no fixed finite carrier can do is reproduce the theory "at all preparations/effects and all precisions". The ε-form theorem (Main:568) and Main:566 show that bounded instrument envelopes are reproduced to any requested accuracy by finite carriers.

The observable content of a finiteness principle therefore needs two things the record does not contain:

1. an estimate of N;
2. a lower bound on the ε-approximate nonnegative rank of qubit behaviours as a function of menu size and ε.

"Sharp in principle", "derivable from results already on `main`" and "the only candidate with a sharp prediction" overstate this. The unboundedness is an import, not a proof on `main`. The assessment also contradicts itself: C4's prediction is called "the most concrete of any candidate" even though no principle P is proposed.

**Fix.**

- Restate C5's prediction as "an exact-limit consequence (Main:562, unboundedness imported) whose finite-precision content needs an estimate of N and an approximate-rank growth bound, neither on record".
- Restate "Excluded by" as "agreement, within ε, for a behaviour whose ε-approximate nonnegative rank exceeds a credible N".
- Rewrite C4's entry as "none in view; conditional on an unproposed P".
- Drop "only" and "most concrete".

### F7 — required — §1.4 "Motivation", C5 premises

**Evidence.** Holographic and de Sitter bounds limit entropy, that is, the logarithm of the Hilbert-space dimension of a patch. They do not limit the number of classical ontic configurations. A finite-dimensional quantum patch has a continuum of states and evades E8. Main:703: holographic bounds "are compatible with the finiteness assumed here and are not premises of it".

**Fix.** Say that these bounds motivate finitely many *ontic configurations* per patch only together with OI's premise that the patch's ontic description is a classical configuration space. They motivate the finite Hilbert dimension that an infinite-carrier route (#1007) can also meet.

### F8 — required — §0 ("derivable per horizon from locality premises"), §1.4 items 2–3 and "Derivation", Q-D(1)

**Evidence.**

- **What GR App. B derives.** It derives the finiteness of the patch's *site count* from (D1)–(D3), via Lemma B.2(a). It does not derive finite alphabets: "(D4) the alphabets on $V\cup B_n$ are finite" is a hypothesis. The owner separated finiteness premises from probability premises (#1169 c.6897254631). "Per-patch finiteness is the derivable kind" contradicts C5's own obligation text ("finite patch alphabets, hypotheses not derived").
- **The coupled deep sector.** GR:132 under (D1)–(D5) already covers a *coupled* deep sector of any cardinality beyond the n-cone, per horizon. That is the question §1.4 item 3 and Q-D(1) treat as open from Main:60.
- **A missing third kind of statement.** The derivation bullet's dichotomy ("all-time or all-horizon statements … choices of completion") leaves out statements about all experiments, that is, about unbounded operational complexity. E8 is one, and it is not a choice of completion.

**Fix.**

- Write: "per-horizon finiteness is a derived lemma from (D1)–(D4), of which (D4) is a finiteness hypothesis on the patch alphabets".
- Cite GR:132 under (D1)–(D5) as answering the coupled-sector question for transition data at horizon n.
- Restate Q-D(1) as the residual: non-product priors (D5 fails), infinite alphabets inside the cone (D4 fails; cf. NATIVE-PADIC-1, off `main`, #914 body), and E8-type statements.
- Scope the "strong indication" sentence to transition data at a fixed interface.

### F9 — required — C0 "Consequences"

**Evidence.** The assessment cites "No observational constraint (audit r9 headline: none of 57 A1-dependent results currently establishes one)". The headline covers only the 57 A1-dependent rows and continues: "that does not mean none can be recovered" (audit r9, line 24). E16 and E17 together with the loophole-free data are an observational constraint, a negative one, carried by results that do not depend on A1. C0's own list (b) includes E16.

**Fix.** Write: "no positive observational constraint established; the A1-free Bell results constrain the reference architecture negatively (subject to F1)". Quote the audit's qualifier.

### F10 — required — Q-A, "Cheapest decisive next step"

**Evidence.** "The present record suggests only the conjunction locality + MI + determinism excludes anything (E16)" contradicts §1.1's own reading: E8, E9, E13 and E14 each exclude something.

**Fix.** State the pattern the record actually shows. Every exclusion on record excludes observed quantum behaviour or the exact quantum theory:

- E8: finiteness excludes exact continuum QM;
- E13 and E14: bijection-level access excludes phases and full control;
- E16 and E17: locality with MI excludes Bell violation.

None excludes a non-quantum law while keeping QM. Name that as the gap Q-A tests.

### F11 — required — summary table, row C1

**Evidence.** The table gives "Excluded by: — (law-level unfalsifiable by S⇒D)" and "consistent". The C1 body says: "at the Bell level, its own conditional ceiling plus experiment excludes C1 read with MI and the reference graph". C1's premises list "MI for Bell".

**Fix.** Make the table match the body, with F1's scope.

### F12 — required — C3 "Preserves"

**Evidence.** C3 claims that Theorem 23's local reconstruction is preserved without H-Bell (Sub:193). But Theorem 23 assumes M1-B (Sub:193), and Sub:123 defines M1-B as: "Bell-violating composites take [Main §3.3]'s measurement-independent, ontically parameter-dependent branch". Under C3, M1-B fails. Sub:129 and :171 suggest that M1-B enters separately from the local sector, but nothing on record traces this.

**Fix.** Write: "Theorem 23 as stated is not available under C3; a restatement with M1-B replaced by a measurement-dependent clause, and a trace showing that the local sector does not consume M1-B, are obligations".

### F13 — required — §3 row "Measurement independence", C3 "Physical consequences", §5 final paragraph

**Evidence.** Meth:389: "OI does not postulate unconditional preparation independence". Meth:405: "OI does not impose that postulate". The assessment says "denies" and "OI's denial of PBR preparation independence".

**Fix.** Say "does not impose". The asymmetry question stands: why posit one independence and not the other.

### F14 — required — C4 "Obligations" (literature obstacles)

**Evidence.** The assessment says "continuous reversibility conflicts with a finite carrier (E13's dense-control ceiling)". The ceiling applies to nonnegativity-bounded theories: `nonnegBounded_verdict`, FrozenSourcing.lean:327. `fixedGateTheory_outside_ceiling` (same file) exhibits a theory on `Fin 2` with dense unitary control, and QM itself lives on finite carriers (E10).

**Fix.** Write: "conflicts with the bijection-level sourced class (E13), and with a fixed finite *ontic* carrier through E8; not with a finite operational carrier".

### F15 — required — C1 "Preserves" and "Obligations"

**Evidence.** Two items are listed as preserved before their proofs exist:

- E6 is listed as preserved "via P5a". P5a is an unwritten proof unit, and AM-21.1 is in class NEW.
- E16 for an infinite Ω is CONTINGENT until P4 is written (AM-7.2; owner, #1169 c.6901193492).

The owner's rule (c.6896940222) is no recovery credit until each theorem's requirements are checked. C1's obligations list P1, P3, P5a and P15 but omit P4.

**Fix.**

- Write E6 as "recoverable through P5a (not written; no recovery credit)".
- Write E16 as "finite Ω; infinite Ω contingent on P4".
- Add P4 to the obligations. Main:414 part (2) can stay as preserved, as a checked proof of the restricted statement.

### F16 — required — header and §1.4 (owner guidance)

**Evidence.** The guidance is on record at #1169 c.6901670978. It asks what further analysis of finiteness would involve: "whether total or effective finiteness could be derived, motivated or constrained by observation, and the cheapest decisive step for each". §1.4 gives one bullet each for derivation, motivation and observation. It does not separate total from effective finiteness in each bullet, and it gives a cheapest step only through Q-D.

**Fix.**

- Cite c.6901670978 in the header.
- Add a 2×3 grid: total and effective finiteness against derived, motivated and constrained by observation. Give each cell its current standing and one paper or literature step. These can draw on F7 and F8, for example: GR App. B for the effective/derived cell; the approximate-rank bound and N for the observational cells; entropy bounds plus the classical-ontology premise for the motivation cells.

### F17 — required — §4 candidates (completeness)

**Evidence.** The continuum or infinite-alphabet carrier route has three entries on record:

- #1007 records it as an owner framework decision of 2026-10-30, at the top of the research backlog;
- #914 §4 calls it "Candidate under study … A hidden continuum removes the finite-carrier obstruction M:560, but that is the problem it was built for, not a prediction … measure-preserving dynamics plausibly stays inside the nonnegativity invariant";
- #866 c.6707774417: "continuum material removes a finite-carrier restriction without supplying the missing operational map".

It appears in the assessment only as "the route #1007 opens". It is the direct counterpart of C5.

**Fix.** Add a short C1 variant, or a C5 counterpart, under the same §A.29 headings, and carry #914 §4's own assessment.

***

### F18 — recommended — §2.2 scope

The "no phase information" claim holds for Q_fb as defined (Main:554): laws depend on U only through |U|², with time-inhomogeneous kernels if U varies. In the compressed (T) representation, unmeasured two-time data $T(t)$ fix the generator up to gauge (phase-locking, Main:228–242; Main:650 (iv)). Phases are then determined by classical data, but operational interference still needs the bridge. Add one sentence.

### F19 — recommended — §2.2, Spekkens comparison

In Spekkens' toy theory, measurement disturbance is *derived* from the knowledge-balance principle. OI's intervention dilation *supplies* it (Main:686). Say that an epistemic restriction would derive what OI supplies, which is itself a C4-type route.

### F20 — recommended — §3 row "Single-world readout"

Exclusion follows from φ being a map, a single trajectory (Sub:465; Meth:144). Axiom 1 does not exclude it: Everettian accounts accept that registered differentiation occurs. Change the stated reason.

### F21 — recommended — §3 row "Retrocausality"

This is correct with stated scope (see §2c). Add that Hall and Branciard's causal (≈0.080 bits) and retrocausal (≈0.046 bits) optima (Main:427) show the two model classes differ. The reduction is statistical, and the explanatory difference matters for the fine-tuning question (F2).

### F22 — recommended — §3 row "Finite regions"

"Only non-measurable response tables could evade the bound (Pitowsky-type)" is plausible but unsupported. A reviewer's sketch, not checked: if each wing's outcome is measurable, which is needed for $P(q\mid a,b)$ to be defined, then with finite reading sets each coordinate of $\varphi^k$ depends on finitely many sites, so the table is measurable. That suggests the finite-region condition may be removable. The owner has said a focused check is warranted only if a classification relies on such an argument (c.6901193492). Mark the sentence as unchecked and rely on it for nothing.

### F23 — recommended — Q-E next step

Simplex-embeddability is a property of the operational theory. Every theory has some classical ontic model obtained by restricted access, in general a contextual one; OI's own realizations under D are examples. So "restricted access … yields a simplex-embeddable theory unless the access itself is contextual" is close to a tautology. Replace it with the decisive and cheap question: is every `NonnegBounded` theory (the E13 class) simplex-embeddable? A yes would show that the sourced class is noncontextual and would locate where phases must enter.

### F24 — recommended — citation precision

| Claim in the assessment | What the source shows |
|---|---|
| E13 at FrozenSourcing.lean:106, :318 | :106 is `permTheory_phase_ceiling`; `frozen_sourcing_verdict` is at :318 and `nonnegBounded_verdict` at :327; all on `Fin 2` |
| E12 located at "#914 §1" | Lean locations are RouteB.lean:228 (`derivedOI_of_qm`) and CompletedOI.lean:549 (`qm_implies_oiCore`) |
| §2.1 `target_not_qm` | Conditional on `RouteBTarget`; cite `routeB_target` (RouteB.lean:389) as well |
| E10 "each condition independent" | Independence is witnessed on the qubit (`main_result`, Main:566, Main:592) |
| Main:702, Meth:150 | Both are headings; the content is at Main:703 and Meth:152 |
| Meth:146 for "injectivity does not give surjectivity on an infinite carrier" | Meth:146 does not say it; mark it as the assessment's own observation, true by the shift map, and cite Main:60 ("no construction is given for an infinite $S$") |
| E20 at Main:298–318 | The statement is Corollary 1, Main:316 |

### F25 — recommended — §1.2 "Determinism"

The observation that Main:44's composition argument does not select determinism ("Markov semigroups also compose") is a finding about Main. Record it for routing to an accountable Issue; no manuscript change is authorized.

### F26 — recommended — C2 (off-`main` provenance, §A.42 item 8)

Two #866 results bear on C2. Both are unmerged and off `main`, so they are provenance only:

- #866 c.6704691492: SM §3.1's ring rule "gives a genuine program-dependent local response under one common structured hidden prior", but it is "not a complete physical Bell interface", and the Bell ceiling applies to screened, separated implementations.
- c.6704448653: the no-signalling screen stopped at the physical preparation, setting and access map, with neither PASS nor FAIL.

### F27 — recommended — §3 intro

"This is the corpus's sharpest contact with data" is a judgement. Narrow it to the QM-emergence results reviewed, or drop it.

### F28 — recommended — literature

Add Hardy 2004 (ontological excess baggage: an exact qubit model needs infinitely many ontic states) and Galvão–Hardy 2003. Both bear directly on E8 and C5; mark them "to be checked first-hand".

### F29 — recommended — candidate count

The brief asked for 3–5 candidates. Six are listed. Say explicitly that C1 is the common core, not a separate physical theory; the body already says so in C1's "Standing".

***

## 2. The writer's own arguments

**(a) Phase invisibility of Q_fb: correct with stated scope.** After each projective measurement in the fixed basis the state is a basis vector, so a Q_fb law is a function of a Markov chain whose kernels are $|U_t|^2$. This is consistent with Main:554–557, and with Main:557's remark that the recovered table is the same for every $|U|^p$. The scope limit is F18: the compressed (T) representation, unmeasured two-time data and phase-locking.

**(b) One-bit Mach–Zehnder example: correct.** For $\varphi(v,h)=(v\oplus h,h)$ with h uniform, $T^{(1)}=\tfrac12J$ and $T^{(2)}=I$, as at Main:445. A passive read of v at step one does not disturb h, so step two returns to $v_0$, while QM gives a uniform law. The disturbance is supplied by the intervention dilation (Main:686). The example is illustrative and is not a theorem that no classical model derives disturbance (F19).

**(c) Retrocausality reduced to measurement dependence: correct with stated scope.** In a deterministic bijection, a future boundary constraint pulls back to a constraint on the initial law. With internal setting generators, that makes Ω correlate with the settings, and the bound of E18 then applies. The reduction is statistical. Causal and retrocausal model classes differ in Hall and Branciard's costs and in explanation (F21). A pulled-back boundary law is also a non-invariant initial law, which bears on F3.

**(d1) "Total finiteness has no observational effect within any finite horizon in the finite-reading-set class": correct with stated scope, overstated as written.**

- At the class level it is nearly immediate. S⇒D realizes every per-horizon law finitely, and GR:132 under (D1)–(D5) shows that the deep-sector cardinality beyond $B_n$ does not enter the transition data on $[0,n\Delta t]$.
- The scope is: transition data, finite alphabets (D4), and a product prior with a uniform part on $B_n$ (D5).
- It does not cover E8-type statements about unbounded operational complexity, where carrier cardinality does have consequences in the exact limit (F8).

**(d2) "Finiteness per horizon is derivable from locality premises": correct for the site count, wrong for finiteness as a whole.** The site count follows from (D1)–(D3). Finite alphabets are hypothesis (D4) (F8). Main:362's any-cardinality induction is consistent with this. Main:414 part (2) uses finite regions and the finite group alphabet of item (xiii).

***

## 3. Checked and confirmed accurate (spot list)

**Kernel identifiers.** All are present and say what is claimed, apart from the location and scope notes in F14 and F24:

- `finite_horizon_equivalence` (Equivalence.lean:462), with S⇒D, D⇒Q_fb and Q_fb⇒S as cited at Main:97 and Main:554;
- `oi_alone_not_qm` (GeneralCarrier.lean:160): the diagonal theory on `Fin 2` realizes the sealed OI core and is not exact QM;
- `exactAll_iff_physical_general` (GeneralCarrier.lean:100), with necessity and sufficiency separately witnessed (`physical_of_exactAll`, `exactAll_of_physical_general`), so §A.34 is satisfied;
- `five_way_minimality`, `derivedOI_of_qm`, `qm_implies_oiCore`, `substratumGen_not_control` (StructuralClosure.lean:348; two-state carrier), `oiPlusMin_iff_qm`, `c3_necessity`, `pIndivisible_of_rooted_identity_return_of_overlap`, `iterate_dependsOnlyOn_ball`, `twoBranch_of_triangleGeneric`, `ensemble_underdetermined`.

**Manuscript and record citations.**

- Condition (iv) is "full reversible control" in Main:566's numbering, as the assessment says.
- Main:414 parts (1) and (2), its hypotheses, and part (2)'s finite-region condition match Main:414–416. The owner's AM-7.3 decision (c.6901193492) is quoted correctly.
- E18's bound, 0.0309 bits, and the Hall–Branciard figure match Main:420–427.
- Main:60's decoupled finite factor, and its explicit non-claim for coupled or infinite sectors, are quoted correctly.
- Ledger items (ii), (vii), (xiii) and (xiv) are at Main:728.
- O-RDY D1 and Lemma R (I-1, I-2) are quoted correctly from #1147 c.6894144708.
- H-Bell (i)–(iii) are quoted correctly from Sub:133.
- The adopted branch is ontic parameter dependence: Main:404, :412, :418; Meth:389, :393; Sub:123 (M1-B).

**External attributions.** Fine 1982; Kochen–Specker 1967 and Bell 1966 qubit models; Pawłowski et al. 2009 (information causality gives Tsirelson); Navascués et al. 2015 (almost-quantum set); Schmid et al. 2021 (noncontextual model iff simplex-embeddable); the three 2015 loophole-free tests; and the cosmic Bell tests (Handsteiner 2017, Rauch 2018) are correctly attributed as far as the reviewer knows.

**Balance and the stop rule.** C0 is consistently "not concluded"; F9 and F10 are the two places where wording slants toward it. Finiteness is treated as open throughout. No premise is adopted, and no recovery credit is claimed except in F15.

***

## 4. What was read of #866, #914 and the other Issues, and what it changes

**#914** (body and 93 comments). All 93 were indexed by date and opening text. Every comment was searched for: Bell, measurement independence, parameter dependence, no-signalling, PR box, Tsirelson, finiteness, total finiteness, BSEL, probability law, prior, selection principle, contextual, Spekkens, preparation independence.

Read in full or in the relevant passages:

- the body (§1 endpoints F1/F2, the matrix rows 14–18, §4 including "Candidate under study: a continuum");
- c.6875046763 and c.6875548603 (target decisions);
- c.6594910654 (A1-NECESSITY);
- c.6893722503 (target-impact triage: D-CQ, linearity Q2, total finiteness);
- c.6556841398 (P/S/R/RR inventory: linearity K1, settings as state functions, measurement independence as a posit, no `do(σ)`);
- c.6776048388 and c.6883931412 (PR box and soundness wording, later superseded by D-CQ);
- c.6558834119 (BSEL-1, opening).

**Changes:** F4, F5 and F17. Nothing contradicts the inventory.

**#866** (body and 73 comments). Indexed and searched the same way. D-OB7 is not in the body but appears in six comments. There were no hits for measurement independence, parameter dependence or finiteness.

Read in full:

- c.6649267203 (D-OB7, D-OB8 / H-PREP);
- c.6704318875 and c.6704448653 (no-signalling screen: STOP at the preparation, setting and access map);
- c.6704542441 and c.6704691492 (common interface: a conditional local component, not a Bell interface);
- c.6707774417 (observer-interface source: a negative deliverable at its scope; continuum without an operational map);
- the passages of c.6540829854 and c.6567167742 on preparation and setting independence (joint setting independence against common causes).

**Changes:** F3 (H-PREP), F17 and F26. Nothing contradicts §3's account of the adopted branch.

**#1169.** All 282 comments indexed. Read in full: the owner records of 2026-11-15 cited in the findings (c.6891338304, 6893456888, 6894697123, 6896940222, 6897254631, 6901193492, 6901612904 and 6901670978), plus the relevant passages of c.6899443112 and 6900274688. These are the sources for F4, F8, F15 and F16.

**#1147.** Body and three comments; c.6894144708 read in its D1, Q8, Q9, routes and inventory passages. Source for F3.

**#1007.** Body read (the owner's 2026-10-30 decision). Source for F4 and F17.

***

## 5. Not checked

- External literature was not fetched. The scopes of Wood–Spekkens, Hardy 2004, Galvão–Hardy, HKLP's growth rate, Hossenfelder–Palmer and Pitowsky are from memory and are marked "to be checked first-hand".
- Other readings were partial:
  - the A1 audit r9 (§0 headline, §13, §14 proof-unit table and owner records);
  - Main §3.5 and §4.6 proofs;
  - `papers/Structure.md`;
  - GR beyond 128–134 and Appendix B;
  - SM beyond lines 14, 48 and 150.
- EF-1 drafts and the #1173 papers are off `main` and were not read.
- No Lean build was run; identifiers were checked by reading the source.
- The measurability sketch in F22 and the no-signalling expectation in F1 are the reviewer's own and are unchecked.
