# POSIT-MIN — audit of Main's posit ledger against a preregistered minimality criterion

**Status.** Writer's paper-only research record. Source reading and paper reasoning only: no
computation, no Lean, no manuscript or registry edit, no premise adopted or dropped. The criterion,
schema, decision rule and controls were fixed in `PREREG.md` (commit `3f93b47e`, pushed before this
file). Independent non-author review is required. Every verdict below is a proposal to the owner.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 c.7033247170](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033247170),
2026-11-20T07:25:20Z. Goal link (§A.47): #1169; decides which substratum posits observation forces
and which are revisable; does not decide which the framework keeps. A1 remains OPEN/UNADOPTED;
physical measurement sourcing remains NOT PASSED.

**Source pin.** `main` at `b9168ef0408b5f55b935a4df17cb0841877e221a`. Notation as in `PREREG.md`
(`Main:n`, `SM:n`, `Sub:n`, `GR:n`; ledger items `Main:732 (k)`). Short names of inputs are those
of `PREREG.md` §1. Support labels: [K] kernel-checked on `main`; [P] manuscript statement; [R]
research record on `main`, at the review standing it states; [W] reasoning in this record,
unreviewed; [LIT] literature from memory, background only.

## 0. Summary

1. **Observation forces little at the substratum level.** Under the preregistered criterion, the
   clauses observation supports are: Axiom 2 as a presupposition of every multi-time observation
   (`PRE`); reversibility as a representation choice that excludes no finite-horizon law (`REP`);
   injectivity on registered content (`OBS`, O3); and, with settings, records and carriers read as
   configuration content, a **non-affine** update (`OBS`, O4, from MR★ S-C1 and OA-1 D5). Each
   lattice item, (viii)–(xi) and (xiii) and the lattice form of (vi), is result-needed (`RES`) or a
   stated choice of model (`CONV`); (xii) is an interface (`REP`). None is observation-forced in the
   form the ledger states it.
2. **A5 (item (vii)) is in tension** with five things the corpus itself records: Main's adopted Bell
   branch (`Main:420`: "the update of this branch lies outside ledger item (vii)"); SM's own route to
   shell sampling, which needs non-linearity (`SM:294`, `SM:1416`); item (v), whose numerical
   motivation comes from the non-linear rounded rule (`Main:732 (v)`); the configuration-level
   no-go for conditional dynamics and confined records (MR★ S-C1, S-L4, AW-MR8, AW-MR9; OA-1 D5);
   and accessible memory under Haar on `ℤ^d` (NR-1 Theorem 3.3). Each tension carries named
   hypotheses (§3). A5 is not refuted. UNIV-1 Theorem L adds no observational argument at finite
   scales: the operative constraint is affinity, not non-universality (§2).
3. **Inside Main, A5 is used only to state what it excludes** (`Main:364`, `Main:420`) and to
   describe the class of item (v). Its consumers are in the companion reconstruction (A5-LA D1–D16)
   and four kernel modules. SM already states its wave-form Lemma "at either the
   substratum-symbolic level or an observer-level linear lift" (`SM:224`) and places the
   normalization `α = 1/d` at the observer level (`SM:232`): lift-level linearity is a weaker
   alternative already present in the corpus. Its sufficiency for Theorem 23 is not traced (§4, D1).
4. **Selected classes (§4).** R_obs: reversible representatives, injective on registered content,
   with a non-affine update under the inclusion reading. R_res adds the lattice clauses as
   result-needed hypotheses: the second-order form with a general local `F`, finite read sets in
   family form, translation commutation on `ℤ^d`, cubic point-group invariance, no self-term,
   nearest-neighbour range, a declared invariant law and (EM), (xiv). A5 is outside both under the
   inclusion reading. SM's rounded rule `R_q` (`SM:294`) lies in R_res.
5. **Productivity (PREREG §4):** met. Located conflicts: (vii) against the adopted Bell branch, the
   ledger's own interdependence clause and SM §4.2 (§3); item (vi) and the first clause of (xi) are
   stated as emergent observations but consumed as lattice symmetries (§1 rows vi, xi). New
   structural fact: the scope limit of O4's affine exclusion (K5, §5).

## 1. Per-item table

Columns: (a) reason, typed; (b) consumers; (c) forced by observation?; (d) weakest known
alternative and its sufficiency; (e) standing; verdict (PREREG §3.4).

### (i) Axiom 2 — differentiation recurs

- **(a)** `Main:36`: "One thing does not follow: that the differentiation *recurs* … This is
  **Axiom 2** … non-derivability by countermodel." Type: posit of the foundation (neither `EMP` nor
  `RES`): the successor relation "uses successive moments and a locus persisting across them"
  (`Main:36`, `Main:732` rung analysis).
- **(b)** Every dynamical statement: the Definition's `φ` and its iteration (`Main:42`); C2 and C4
  (`Main:74`, `Main:78`); all of §2–§4. MAIN-ROOTS row "Finite distinguishability"
  (`a1-main-roots-20261118/AUDIT.md:18`) records Axiom 2 as an input of the roots.
- **(c)** `PRESUPPOSED`. Each requirement O1–O4 is a statement about more than one moment. No
  observation made at one moment can bear on it: the single-moment countermodel of `Main:36` contains
  apparent records and satisfies Axiom 1.
- **(d)** None traced. The countermodel is the only alternative, and it removes every dynamical
  result.
- **(e)** `open` (`PRESUPPOSED`). *Pressure (K6):* the objection that a single moment carrying
  apparent records reproduces everything registered at that moment is the countermodel itself;
  observation cannot exclude it, which is why the standing is not `forced`.
- **Verdict: KEEP (`PRE`).**

### (ii) Total finiteness of the bijective representative (A1)

- **(a)** `Main:60`: "observed near-unitarity is the empirical input motivating the choice";
  `Main:732 (ii)`: "carried as one sufficient condition and not as a premise". `Sub:92`: "A1 remains
  the finite-carrier premise for the recurrence arguments." Type: `EMP` (motivation) + `RES`.
- **(b)** Cited, not re-derived (K2): A1-REMAINDER §1 rows M1–M21, C1–C14; residues R1–R6
  (`a1-remainder-20261119/REMAINDER.md:54–167`); A1-NECESSITY five-family table
  (`a1-necessity-20261117/ASSESSMENT.md:31–39`); A1-SCOPE site map (`a1-scope-phase0-20261120/`).
- **(c)** `NOT FORCED`. Finite visible capacity is stipulated per moment (Lemma 1, `Main:46`); its
  extension to the whole representative is not implied (`Main:708`). A finite horizon entropy does
  not bound cardinality (A1-REMAINDER §4, row "Horizon-bounded finiteness", `:219`, citing DS
  Countercontrols 1.1, 1.2). A finite decoupled deep sector is unobservable at a fixed interface
  (`Main:60`).
- **(d)** Per result, A1-REMAINDER §3 hypothesis table (`REMAINDER.md:181–190`): H-F3 + H-F4 for
  the Lemma-1-only results (proved, M6, M12, M14, M15, M17, C5, C13); H-REV (R3); H-μ (R1);
  H-RIG/F11 (R2, partial); H-A4′ via O-A4 (R4; O-A4 verdict (i)); no replacement for R5. Status
  `partial`.
- **(e)** `open`. Agrees with A1-REMAINDER §3 ("posit (ii) cannot yet be replaced by
  observer-relative finiteness alone", `REMAINDER.md:171`) — K2 passes. *Cross-item coupling [R]:*
  for the selected linear update on `ℤ^d` under Haar, the A1-free recurrence routes fail (NR-1
  Prop. 2.3 and Theorem 3.3, `NR-1.md:165`, `:237–241`); on the linear branch the recurrence family
  rests on a finite torus. Whether a non-linear member behaves otherwise is open (NR-1 notes
  composite and nilpotent cases are not ruled out).
- **Verdict: WEAKEN** (per-result sufficient conditions, the A1-SCOPE programme already under way;
  no new proposal here).

### (iii) Bijectivity: record preservation and eventual image (REV as alternative)

- **(a)** `Main:732 (iii)`: "one *empirical* input — the observed statistics, in the uniform-prior
  doubly stochastic scope — and one structural principle"; REV "as the standard
  information-conservation postulate … at no cost to the downstream results". `Sub:94`: anchor
  "nanoparticle matter-wave interference at macroscopicity μ = 15.5". Type: `EMP` + `REP`.
- **(b)** Lemma 3 (`Main:54`); the permutation-unitary representation and the doubly stochastic
  marginal (`Main:60`, §3.2); RIGID, HIST, GLUE all assume REV (A1-REMAINDER M11,
  `REMAINDER.md:70`); PR1's exclusion lemma (reversible dynamics under an invariant law creates no
  net preparation supply, `prep-regress-1-20261119/RESULT.md:44–88`, item 4).
- **(c)** `PARTLY`. O3 forces injectivity on states with different registered content (`Main:36`).
  O2 (unitarity of the emergent description) constrains the effective dynamics, not ontic
  bijectivity (A1-REMAINDER M11). REV loses no finite-horizon visible law, since `S ⇔ D ⇔ Q_fb`
  (`Main:80` item (1)); that is the `REP` reason.
- **(d)** REV (bimeasurable bijection of a measurable carrier), printed at `Main:732 (iii)`; proved
  sufficient where the A1-free records use it (A1-REMAINDER R3: "No lemma").
- **(e)** `open`. *Pressure (K6):* REP covers each finite-horizon law separately; one common
  reversible carrier for all windows is a further question (A1-NECESSITY row P12(b)). That does not
  make REV observation-forced; it makes it a representation choice whose cost is nil per law.
- **Verdict: KEEP (`REP`), in the REV form**; injectivity on registered content is the `OBS` part.

### (iv) Measure selection: maximal entropy compatible with the observer's records

- **(a)** `Main:732 (iv)`: "a standard but substantive epistemic postulate, not derived";
  `Main:54`, `Main:58`. Type: `CONV` (stated as a postulate) + `RES`.
- **(b)** Baseline matrices, Lemma 3, μ-G/μ-O/μ-R (A1-REMAINDER M1–M3, R1, `REMAINDER.md:60–62`,
  `:103–113`); NR-1 and O-A4 §5 run under Haar; PR1 budgets.
- **(c)** `NOT FORCED`. Its finite-window consequences (every single-time block statistic constant
  in time) hold equally under the alternatives (A1-REMAINDER §3 relabelling test,
  `REMAINDER.md:195–209`). R1-INF: the entropy-density version "restates the uniform posit and
  delivers no independent prediction or postdiction" (`r1-inf-20261119/RESULT.md:418–420`).
- **(d)** H-μ / P-μ, a declared normalized invariant law (A1-REMAINDER R1); sufficient for the
  rooted family under RIGID/HIST/P8-M at their scopes [R]; not for selection.
- **(e)** `open`. Note [R]: under any invariant law no fixed block gains readiness (PR1 Node 1);
  observed preparation of low-entropy states then needs conditioning on records (the "compatible
  with the observer's records" clause, μ-R) or a boundary supply (PR1 Node 4, NEQ-T/NEQ-O, neither
  adopted).
- **Verdict: WEAKEN to H-μ (`RES`)**, as A1-SCOPE already proposes; no new proposal.

### (v) Hidden-sector mixing hypothesis (EM)

- **(a)** `Main:732 (v)`: "ETH-motivated … for a system class (emergent descriptions of
  linear-mod-`q` automata) on which the standard ETH evidence base is silent … numerical
  motivation comes from the rounded candidate of [SM §4.2]". Type: `EMP` (motivation, off-class) +
  `RES`.
- **(b)** The slow-bath form of C2-necessity; §4.6 theorem and both corollaries
  (`Main:750–764`); A1-REMAINDER M18–M20.
- **(c)** `NOT FORCED`. Thermalization is observed in many systems [LIT]; no observation bears on
  the effective channel of the realized hidden sector, and `Main:732 (v)` states the evidence base
  is silent for the class named.
- **(d)** P8-M's operator form with a supplied invariant law (A1-REMAINDER M18, partial); none
  traced for the full §4.6 chain.
- **(e)** `in tension` with item (vii), under the hypothesis that (EM) is to be motivated within the
  class it names: the exact linear rule "conserves further quadratic invariants" and its largest
  shell "splits into exponentially many cycles" (`SM:294`); "that rule does not satisfy linear
  dynamics and cycle ergodicity jointly" (`SM:1416`); the motivating rule `R_q` is non-linear. The
  conserved-energy question for the `d = 3` rule is G3-W1's and is not treated here.
- **Verdict: KEEP-RES (§4.6, C2-slow) + FLAG** (its stated class and its motivation differ).

### (vi) Spatial isotropy (E4)

- **(a)** `Main:732 (vi)`: "entering as empirical input E4"; `Sub:82`: "Observed physics is
  rotationally invariant"; `SM:238`: "Spatial isotropy is required for Lorentz invariance". Type:
  `EMP`.
- **(b)** The wave-form Lemma, as "cubic-isotropic" (`SM:224`, proof `SM:228`); Stage 2(b)
  (`Sub:159`); the `O_h` steps of Stage 2 (O-A4 §7.1, rows 16–18); HydroSourceAudit H2b (the axis
  stencil's fourth moment is `O_h`-invariant and not rotation-invariant [K]).
- **(c)** `PARTLY`. Observation forces isotropy of the emergent description to tested precision
  [LIT]. What the consumers use is invariance of the rule under the cubic point group (`SM:224`),
  which no observation forces: SM shows the `O(k²)` symbol is isotropic for every `α` (`SM:232`),
  and the quartic order is not (HydroSourceAudit H2b [K]).
- **(d)** `O_h` invariance of the rule, plus emergent isotropy at the order tested. Sufficient for
  the wave-form Lemma (it is the Lemma's stated hypothesis).
- **(e)** `forced` for the emergent statement E4; `open` for the lattice clause. The ledger names
  the observation, while the consumers use the lattice clause.
- **Verdict: WEAKEN** — record the consumed clause as `O_h` invariance of the rule (`RES`), with E4
  as the emergent observation it serves.

### (vii) Linearity of the substratum update (A5)

- **(a)** `Main:732 (vii)`: "a further restriction beyond the affine condition"; `Sub:100`: "The
  selected wave-equation model assumes a linear update"; `SM:240`: "Linearity (A5) is a further
  restriction imposed on the selected lattice model"; `Sub:274`: "A5 remains a stipulation for the
  selected linear branch"; H-D: "No derivation of A5 from bare OI was found on the record searched"
  (`round-h-d-a5-status-adjudication/result.md:52–56`). A5-LA R5: no selection principle among
  N1–N11 selects `b = 0` with independent justification. Type: `CONV` + `RES` (the wave-form
  Lemma).
- **(b)** In Main: `Main:364` (under (vii) `G_φ^K = G_φ` for every state class; a state-dependent
  graph "requires an update outside (vii)"); `Main:420` (the adopted Bell branch "lies outside
  ledger item (vii)"); `Main:732 (v)` (class description); the interdependence clause of
  `Main:732` ("(x) implies the bound of (ix) for `G_φ^ref`, and with (vii) for `G_φ`"). No theorem
  of §2, §3.1, §3.2, §3.4 or §4.6 uses it (A5-LA D8, D9). Companions: A5-LA §2 table D1–D16
  (`A5-LINEAR-AFFINE.md:116–162`), notably the wave-form Lemma (`SM:224`), Stage 2(b) and 2(d)
  (`Sub:159`, `Sub:163`), Theorem 23 (D16), SM §6 (D4, D5), SM:1416. Kernel [K]:
  `StochasticInterface.phi_fixes_zero` and `ensemble_underdetermined` (`:89`, `:118`),
  HydroSourceAudit H0 (`coarse_evolution_additive`, `coarseCloses_additive_on_range`, `:199–211`),
  A6Instantiation / BackgroundIndependence (`linkF` typed `V →+ V`, A5-LA D14); predicate
  `SubstratumInterfaceAudit.A5` (`:102`).
- **(c)** `NOT FORCED`. No observation in PREREG §3 implies additivity over `ℤ/q`. Linearity of
  quantum evolution is not such an observation: a permutation of configurations is a linear unitary
  on `ℂ^S` whatever its form over `ℤ/q` (`Main:274`).
- **(d)** Two weaker alternatives in the corpus. (1) Affine (base-point independence, `SM:240`):
  sufficient for D1, D2, D4, D6, D12, D13 at the scopes A5-LA states [D]; it does not escape any
  tension in §3, since OA-1 D5 and L4 hold for every affine update (SEL-SYN MM-4 (4a), (4b),
  T6). (2) Linearity of the observer-level lift only: the wave-form Lemma is stated "at either the
  substratum-symbolic level or an observer-level linear lift" (`SM:224`), the normalization belongs
  to `L_obs` (`SM:232`), and the Stage 2(d) stabilizer is computed on the lift (A5-LA D3). Its
  sufficiency for Theorem 23 is not traced (owner decision D1).
- **(e)** `in tension`, under the hypotheses listed in §3. Not `refuted`: each conflict uses at
  least one hypothesis that is itself an open posit or an interface reading.
- **Verdict: FLAG**; KEEP-RES only for the companion consumers, if the owner keeps them in the
  substratum-symbolic form (D1).

### (viii) Site factorization

- **(a)** `Main:732 (viii)`: "the configuration space is identified with a product of local
  configuration spaces … the dynamics alone has not been shown to select the identification".
  Type: `RES` (spatial results).
- **(b)** Cone and Bell ceiling (`Main:364–391`); §4.6 (`Main:752`); the companion reconstruction.
  The characterization theorem does not use it (`Main:732`).
- **(c)** `NOT FORCED` in the ontic form. O1 concerns the emergent description; Stage 2 inherits
  its graph from Stage 1, and that identification is open (O-A4 §10 item (1), citing A1-01).
- **(d)** None traced: the quasilocal completion takes an arbitrary site set but still a product
  structure (A1-REMAINDER C5).
- **(e)** `open`.
- **Verdict: KEEP-RES** (§3.3, §4.6, reconstruction).

### (ix) Bounded coupling degree (A3), family form

- **(a)** `Sub:96`: "Required for locality and the emergence of a coupling graph with well-defined
  dimension"; `Main:732 (ix)`: content "only in family form". Type: `RES`.
- **(b)** Bounded cone growth (`Main:364`); §4.6 (`Main:760`, "bounded per-step range");
  `SubstratumInterfaceAudit.A3Family` (`:131`) [K].
- **(c)** `PARTLY`. O1(b), a finite emergent signal speed, is served by bounded cone growth; bounded
  degree is the corpus's sufficient route, not an implication of O1.
- **(d)** Finite reading sets `N_i` on an arbitrary site set (`Main:364`, second half), giving the
  cone without a uniform bound; sufficient for the cone statement, not for bounded growth.
- **(e)** `open`. Compatible with Main's Bell branch, which uses "bounded-degree long edges"
  (`Main:414`).
- **Verdict: KEEP-RES** (cone growth, §4.6).

### (x) Nearest-neighbour range on the reference state class

- **(a)** `SM:226`: "an assumption beyond bounded coupling degree … Nearest-neighbor is adopted as
  the minimal local branch used by the observer-level spectral calculation". Type: `CONV` + `RES`.
- **(b)** Wave-rule form, dispersion and the coefficient `2σ/15`, the six-link carrier
  (`Main:732 (x)`, `SM:226`); the Bell–lattice Corollary (`Main:416–420`).
- **(c)** `NOT FORCED`: "center-independent families with next-nearest-neighbor couplings exist and
  tune the low-energy speed" (`SM:226`).
- **(d)** Any finite range with bounded degree (A3); sufficient for the cone (`Main:364`), not for
  the specific dispersion.
- **(e)** `open` alone; part of the conflict (vii)+(x)+(xiv) recorded in §3 T1.
- **Verdict: KEEP-RES (`CONV`)** — kept for the dispersion results only.

### (xi) Center independence (A4), two clauses

- **(a)** Clause 1, translation commutation up to gauge: "Its observational anchor is the
  homogeneity of physical law" (`Sub:98`). Clause 2, no self-term: what "the wave-equation
  derivation of Stage 2 uses"; "whether it is independently warranted by the observer architecture
  remains the question flagged" (`Sub:98`); `SM:236`: "CI remains a legitimate structural condition
  on the center-free/chiral branch". Type: clause 1 `EMP`; clause 2 `RES` + `CONV`.
- **(b)** Wave-form Lemma (`SM:224`, `SM:228`); Stage 2 (O-A4 §4 rows); `A4`, `A4Exact` predicates
  (`SubstratumInterfaceAudit.lean:94–98`) [K]; A1 through the finite periodic lattice (`Sub:98`,
  `a1_of_finite` `:109` [K]; A1-REMAINDER R4).
- **(c)** Clause 1 `PARTLY`: observation forces homogeneity of emergent law at accessible scales;
  exact translation commutation of the rule is a sufficient condition. Clause 2 `NOT FORCED`: it
  does not descend to an observer-level statement (`SM:236`, the two-bit swap).
- **(d)** Clause 1: A4∞ on `ℤ^d` without the finite periodic lattice, sufficient for Stage 2(a)–(f)
  under named hypotheses (O-A4 §10 verdict (i)). Clause 2: none traced.
- **(e)** `open`. O-A4 §7: the printed finite class fails some Stage-2 inputs on part of its range
  (`O_h` equivariance at `L = 4`; staggered steps need `Λ ⊂ 2ℤ³`).
- **Verdict: WEAKEN** clause 1 to A4∞ (`RES`, per O-A4); **KEEP-RES (`CONV`)** for clause 2 (wave
  form only).

### (xii) Background independence (A6)

- **(a)** `Main:732 (xii)`: "imposes no restriction on the rule and fixes the interface through
  which the gauge symmetry is read locally"; `Sub:102`. Type: `REP` (interface).
- **(b)** The local gauge reading (SM §3.1); A6Instantiation, BackgroundIndependence [K].
- **(c)** Not a restriction, so not a candidate for forcing (K4 passes: it is not classified as an
  observation-forced restriction).
- **(d)** Not applicable.
- **(e)** `open`, with an assumption-watch marker carried over [R]: in its formalization the link
  coupling is typed `V →+ V`, so additivity enters through the carrier's type (A5-LA D14, Q3, N9).
  If (vii) is dropped, A6's formal interface still carries additivity.
- **Verdict: KEEP (`REP`)**, with the A5-LA Q3 marker.

### (xiii) Second-order form `x(t+1) = F(x(t)) − x(t−1)`

- **(a)** `Main:732 (xiii)`: "for the continuous path of `*`-automorphisms … a posit of the
  selected lattice model, not derived and not an axiom of OI". Type: `RES` + `CONV`.
- **(b)** The continuous path (`Main:274`, `Main:594`; `SecondOrderDrive.driveQ_isContinuousPath`
  [K]); the Bell Corollary (`Main:416`); the published family (UNIV-1 §1); `SecondOrderLayer.Rule`
  [K].
- **(c)** `NOT FORCED`. [LIT] The form is the standard construction that makes a local rule
  reversible for every `F`, linear or not; this is why it carries no linearity.
- **(d)** None traced that keeps the continuous-path result for general reversible local rules.
- **(e)** `open`. It is compatible with dropping (vii): `R_q` (`SM:294`) is a non-linear member.
- **Verdict: KEEP-RES** (continuous path), with `F` general.

### (xiv) Measurement independence `p(Ω | a, b) = p(Ω)`

- **(a)** `Main:403–412`: "Measurement independence is retained as a posit about the initial
  condition, not derived". Type: `CONV` (choice between Bell branches) + `RES`.
- **(b)** Bell ceiling theorem and Corollary (`Main:366–391`, `Main:416`); the choice of branch (a)
  (`Main:414`); OA-1 D5's operational reading.
- **(c)** `NOT FORCED`. It concerns the response-relevant `Ω`, which no experiment reads; in a
  closed deterministic universe it fails for the full microstate whenever more than one setting
  pair occurs (`Main:409–410`).
- **(d)** Bounded measurement dependence: reaching the quantum value needs
  `I_ont ≥ 0.0309…` bits (`Main:429`), a necessary bound only.
- **(e)** `open`; part of conflict T1 (§3).
- **Verdict: KEEP-RES** (Bell analysis).

## 2. A5 and UNIV-1 (PREREG §3.6)

**Q1. What Main uses A5 for.** Main cites (vii) at `Main:364`, `Main:420` and `Main:732`. At
`Main:364` linearity makes the coupling graph the same on every state class; at `Main:420` the
adopted Bell branch is placed outside (vii); at `Main:732` (vii) is listed, used to describe the
class of (v), and used in the interdependence clause. No Main theorem consumes (vii) as a premise
(A5-LA D8, D9 [P]/[K]). Its consumers are the companion reconstruction and four kernel modules
(§1 row (vii)).

**Q2. What Theorem L shows.** For linear members with `q` a prime power and any coupling, every
predicate "cell `i₀` ever shows `h`" from a finitely perturbed periodic background is decidable, so
the member is not Turing-universal in Definition U (UNIV-1 §2.1, `RESULT.md:148–207`). Layer: [W]
in an author record whose latest recorded review is REVISE at `e4e6c997`, with a revision answering
it (`RESULT.md:3–7`); UNIV-1 classifies Theorem L as ELABORATING (known in the literature). Scope:
composite `q` with two distinct primes and multi-background configurations are not covered.

**Q3. What it does not imply.**
- *Universality is not measurement.* UNIV-1 Node 5: universality "would at most source apparatus …
  It would not source amplitudes or the Born rule" (`RESULT.md:359–367`). Measurement sourcing
  needs an admissible resource supply and a native mechanism (PR1 §6, item 4 of its summary); the
  non-linear `q = 2` member U₂ also fails native delivery from untuned sources at its scope (DL1
  Theorem 2.2; NP1 Corollary N3.2), and non-affine rules stay inside the kernel ceiling for the
  quantum gap (OA-1 D6). Non-universality therefore excludes no finite observer.
- *Finite observers need no undecidable halting set.* Definition U concerns unbounded resources
  from infinite configurations. A finite observer's records are finitely many states (`Main:42`).
- *The operative constraint at finite scale is affinity, which is stronger than and independent of
  non-universality.* For a linear member, every region's state is a fixed homomorphic image of the
  initial data (MR★ S-L1), the effect of a change is the same whatever the other regions hold
  (S-C1), and a stored setting acts on a carrier only by translation, for every measure (OA-1 D5,
  three derivations at the same layer). Records exist only as wakes, not as confined patterns
  (S-L4; the wake counterexample of MR★ C-2); bound states and pointers "have no carrier at the
  substratum level under A5" (AW-MR9). These facts, not Theorem L, are what bear on O3 and O4. A
  non-linear rule may also be non-universal, and still pass O4 at the configuration level.

**Q4. Contradictions with observation.** §3 T1–T5.

## 3. Located tensions for item (vii)

| Id | Conflict | Hypotheses under which it holds | Source |
|---|---|---|---|
| T1 | (vii) with Main's adopted Bell branch and observed Bell violation | (vii) and (x), so `G_φ` is the cubic graph at every state (`Main:364`; ledger interdependence clause); determinism; response-complete `Ω`; (xiv); E2 holding for wings separated beyond the graph cone, which some spacelike wings are if `c` is the wave speed `1/√3` (`Main:420`) and E2 holds in that orientation (E4). Main states the consequence: the branch "lies outside ledger item (vii)" (`Main:420`). Affine updates do not escape (SEL-SYN MM-4 (4b), L4). | `Main:416–420`; `Sub:78` |
| T2 | (vii) with SM's shell-sampling route | full-shell sampling as SM's measure reduction uses it; SM's "way out (i)" is non-linearity "from rounding rules in the bijection update" | `SM:294`; `SM:1416` |
| T3 | (vii) with item (v) | (EM) motivated within the class (v) names | `Main:732 (v)`; `SM:294` |
| T4 | (vii) with O4 and O3 at the configuration level | inclusion: settings, records and carriers are cell content; injective coupling for S-L4 | MR★ S-L1, S-C1, S-L4, AW-MR8, AW-MR9; OA-1 D5 |
| T5 | (vii) with observed accessible memory (C1/C4 anchors, `Main:72`, `Main:78`) | infinite lattice `ℤ^d`, `q` prime, `α ≠ 0`, Haar prior, lattice-convex windows: the rooted family is P-divisible at every horizon, with no C4 | NR-1 Theorem 3.3 (`NR-1.md:237–241`) |

Related, recorded but not counted as a tension with an observation: H-A's linearity gate — under
A5 no closed `ℤ/q`-linear coarse description carries a quadratic advective term [K]
(`round-h-a-source-audit/result.md:54–68`), conditional on that coarse-variable class; and O-A4 §5,
Theorem 19 is degenerate for the selected update on `ℤ^d` (`T_ij(n) = 1/q²` for `n ≥ 2`).

*Pressure (K6) on T1–T5, the branch least favourable to A5.* T1 depends on (xiv) and on which speed
is `c`, neither of which is derived (`Main:420`). T2 and T3 depend on SM's measure reduction and on
(EM), both open. T4 depends on the inclusion reading; K5 (§5) shows that an observer-level reading
with non-local coarse-graining escapes it. T5 depends on Haar and on convex windows. No tension uses
only observation and A5. Hence `in tension`, not `refuted`.

## 4. The selected classes (PREREG §3.3)

**Σ_PRE.** Axiom 2 (row (i)).

**Σ_OBS.** Finite visible capacity per moment (the Definition, `Main:42`; outside the ledger);
injectivity on registered content (O3, `Main:36`); under the inclusion reading of O4, an update
that is not affine in any abelian-group coordinatization of the cell alphabets in which settings,
records and carriers are cell content (MR★ S-C1, OA-1 D5). Emergent isotropy and homogeneity (E4,
the A4 anchor) are observations about the emergent description and impose no rule clause by
themselves.

**Σ_REP.** Reversibility of the representative (REV, row (iii)); the A6 covariant interface (row
(xii)).

**R_obs** = reversible representatives, injective on registered content, with a non-affine update
under the inclusion reading. Under the observer-level reading of O4, the non-affinity clause is not
forced (K5) and R_obs is the class of reversible representatives.

**Σ_RES, each with the results it costs.**

| Clause | Results that need it | Ledger item |
|---|---|---|
| site factorization | cone, Bell ceiling, §4.6, reconstruction | (viii) |
| finite read sets, bounded degree in family form | cone growth, §4.6 | (ix) |
| second-order form, `F` general and local | continuous path of `*`-automorphisms | (xiii) |
| translation commutation on `ℤ^d` (A4∞) | Stage 2(a)–(f) under O-A4's hypotheses | (xi) clause 1 |
| `O_h` invariance of the rule | wave-form Lemma, Stage 2 | (vi), lattice form |
| no self-term | wave-form Lemma | (xi) clause 2 |
| nearest-neighbour reference range | dispersion, `2σ/15`, six-link carrier | (x) |
| declared invariant law H-μ | R1 consumers (A1-REMAINDER) | (iv) |
| (EM) | §4.6, C2-slow | (v) |
| measurement independence | Bell ceiling, branch choice | (xiv) |
| per-result finiteness conditions | A1-REMAINDER R1, R2, R5, R6 | (ii) |

**R_res** = R_obs restricted by these clauses. Under the inclusion reading A5 is excluded from R_res
(PREREG §3.3: a clause in tension with an `OBS` clause cannot be in R_res; T4). Its consumers
(A5-LA D1–D16) are the cost. SM's rounded rule `R_q` (`SM:294`) is in R_res: second-order,
center-free, `O_h`-invariant, translation-invariant, nearest-neighbour, and not affine under any
relabelling of its pair alphabet into an abelian group (UNIV-1 Proposition 1.4 [W, EC]).

**What dropping A5 costs, from the inputs.** Uniqueness of the wave form at the substratum level
(D1; within the other clauses `F` is any symmetric function of the `2d` neighbour values); the
stabilizer computation of Stage 2(d) and Theorem 23's gauge-group output, unless lift-level
linearity carries them (D3, D16; not traced); the kernel results that take A5 as hypothesis.
**What it preserves.** Every Main theorem (A5-LA D8, D9); the continuous path (xiii); Theorem 19 on
`ℤ^d` (O-A4 §5, non-degenerate only for non-linear rules); the A1-free records, which do not use A5.

## 5. Controls

- **K1.** The unit's diff touches only `verification/audits/foundations/posit-min-20261120/`.
- **K2.** Row (ii) agrees with A1-REMAINDER §3. No disagreement between the A1 audits was found
  that bears on the ledger rows.
- **K3.** Verdicts differ across items: KEEP ×3 ((i), (iii), (xii)), WEAKEN ×4 ((ii), (iv), (vi),
  (xi) clause 1), KEEP-RES ×7 ((v), (viii), (ix), (x), (xi) clause 2, (xiii), (xiv)), FLAG ×2
  ((vii); (v) together with KEEP-RES). The criterion discriminates.
- **K4.** (xii) is classified `REP`, not as an observation-forced restriction. Axiom 1 is classified
  `PRE` (indubitable, `Main:36`), outside the fourteen items.
- **K5 (countercontrol on O4) [W].** Let `A = (ℤ/2)^n`, `n ≥ 4`, and `φ(x) = x + v` with `v ≠ 0`, a
  translation and hence affine. Partition `A` into eight blocks: `B₁, …, B₆` each a non-empty union
  of pairs `{x, x + v}`, and `B₇`, `B₈ = B₇ + v` with `B₇ ∩ B₈ = ∅`. Then `φ` maps each of `B₁, …, B₆`
  to itself and exchanges `B₇` and `B₈`. Label the blocks by three bits with `B₇ = 110`,
  `B₈ = 111`: the induced dynamics of the label is the Toffoli gate, which is not affine. An
  observer-level variable that is a non-local coarse-graining of an affine rule can therefore show
  conditional dynamics. O4's exclusion of affine rules holds at the configuration level under
  inclusion; an exclusion at the observer level would need a locality condition on the
  coarse-grained variables. With visible variables that are coordinates of the product
  `C_V × C_H`, S-C1 already applies.
- **K6.** Pressure statements are given in rows (i), (iii) and §3.

## 6. Owner decision points

- **D1 — scope of A5.** (a) Keep A5 for the whole substratum update; T1–T5 then stand, and the
  Bell-relevant sector of `Main:420` and the shell-sampling route of `SM:294` lie outside the
  ledger's own (vii). (b) Restrict A5 to the observer-level lift, the level at which `SM:224` already
  states the Lemma and `SM:232` places `α`; this needs a traced check that Stage 2(d) and Theorem 23
  use only lift-level linearity. (c) Drop A5; keep (xiii) with general local `F`; restate the
  wave-form Lemma for the linear part or the lift. Under (b) or (c), the "Theorem recovery before
  concession" rule applies to Theorem 23's uniqueness: the recovery attempt belongs in the
  Substratum paper's programme.
- **D2 — interface reading of O4.** Inclusion (configuration-level) or observer-level ("couplings
  emergent", `SM:428`). Under inclusion non-affinity is observation-forced; under the observer-level
  reading it is not (K5). The owner's 2026-11-04 decision to keep Main's absolute interface as the
  baseline (A5-LA §6 Q1, #1049 c.6624263637) concerns readout classes and does not settle this.
- **D3 — ledger forms of (vi) and (xi).** Whether the ledger should name the consumed lattice
  clauses (`O_h` invariance; translation commutation on `ℤ^d`) beside the emergent observations
  they serve. A manuscript-edit decision, not taken here.
- **D4 — (x) and (xi) clause 2.** Whether to record both as choices of model (`CONV`) needed only by
  the dispersion and wave-form results.
- **D5 — a successor unit.** If D1 (b) or (c): a paper-only unit on what, if anything, selects `F`
  within the second-order local class. Any selection principle is a Layer-0 revision under §A.29
  (A5-LA R5 found none among N1–N11 for the offset).

## 7. Classification (§A.31) and limits

- T1 as a located ledger-versus-branch conflict (`Main:732 (vii)` with the interdependence clause,
  against `Main:420`): ELABORATING (Main and SEL-SYN T6 state its parts; the ledger does not scope
  (vii)).
- K5: NEW, minor (scope of the affine exclusion; a no-go at the observer level needs a locality
  condition on coarse-grained variables).
- The criterion's result that only `PRE`, `REP` and the O3/O4 clauses are observation-supported:
  ELABORATING.
- Assumption-watch marker **AW-PM-1**: an item stated as an emergent observation (E4, homogeneity)
  may be consumed as a lattice symmetry; each use names the lattice clause.
- **Not done.** No proof of the lift-level sufficiency in D1 (b); no new computation; no reading of
  Lean beyond statements cited; the running units G3-W1, A1-PHASE2 and the UNIV-2 revision are not
  used.

## 8. Off-`main` references (§A.42 item 8)

- PR #1447, commit `7e52c8ad`: provenance (the principle's text); not used as support.
- #1049 c.6624263637 and #1169 c.7033247170: owner records, quoted as provenance for decisions; the
  claims they bear on rest on files on `main`.
- Review comments cited inside the inputs: provenance for those inputs' standing.

## 9. Verification status and remediation (§A.46 item 4)

Every row is [W] in this record over [P], [K] and [R] inputs at the standings they state. No row is
established. Missing verification: an independent non-author review of this file against the pin.
Accountable Issue: #1169. Resolving evidence: that review recorded on PR #1451.
