# Review of OI-SM-QM-BRIDGE unit 1 (BRIDGE-UNIT1.md)

**Reviewer.** Fresh independent reviewer (Claude Code subagent, 2026-11-09). Paper-only, read-only.
No git or GitHub writes, no Lean build, no manuscript change. This review authorizes nothing
(#1211 c.6738806776: a review ACCEPT does not authorize freeze, implementation, manuscript change
or merge).

**Object.** `scratchpad/bridge/BRIDGE-UNIT1.md`, sha256
`00cd6fad1e326aaa21badcf70e6c78784ec17baaf54bc669a5725668fc28453c` (verified before reading).
Whole text read (618 lines). Sources read with `git show fd539e15:<path>` after `git fetch origin
main`; copies in `review/src/`.

**Verdict: REVISE.** Five blockers (B1–B5), fifteen nits (N1–N15). Most citations check out
and most findings are confirmed. The blockers come from three places. Two negative or novelty
claims are contradicted by records on `main` that the writer did not read, or read without using.
One cross-level claim is stronger than its evidence. One wording claim about SM:130 is
mathematically wrong.

***

## 1. Blockers

### B1. §10 / Q6 and §0 item 6: "NNB breaks {D, ε} = 0 on which SM Theorems 3, 12, 13 rest" overreaches across levels, and the "NEW" label is contradicted

*Evidence.*
- **QP already states the connection.** QP:298–305, in node 1, which the writer reports reading:
  "SM's exact chiral (sublattice) symmetry of the observer-level staggered operator (Theorem 3 …;
  §4.8 …) is the same bipartite structure at another level. That correspondence is an analogy
  across levels, which SM itself says needs a bridge. Lemma G1 uses only the finite update."
  So §10's classification, "NEW … a structural tension not previously stated", is contradicted.
- **SM names the bridge.** SM:306: "Theorem 3 classifies first-order onsite terms within a fixed
  opposite-parity hopping family; identifying those terms with center dependence of the
  second-order substratum update requires a separate bridge." The same remark gives a
  same-site term of the second-order operator, the self-term $C=2(1-d)$. That term is the
  diagonal of the massless 4D Laplacian, "whose standard 4D staggered factorization has exact
  chiral symmetry".
- **NNB is an armed coupling, not a change to the reference graph.** QP:805–806: "P3 may arm a
  symmetric, center-free, linear coupling between two cells of the same sublattice." The
  writer's algebra, $\{D+h,\varepsilon\}=2h\varepsilon$, adds $h$ to the first-order operator
  $D$. The writer's Check B adds it to a scalar nearest-neighbour adjacency, not to
  $D_{\rm st}$.
- **Reviewer probe R2 (exact) is a countercontrol.** On a 16-site ring take
  $D'=\tfrac12(T-T^{-1})+\tfrac13\cdot\tfrac12(T^3-T^{-3})$. It satisfies
  $\{D',\varepsilon\}=0$ exactly. Its square $\Box'=-4D'^2$ is $\varepsilon$-even. On each
  scalar sublattice, $\Box'$ has **same-sublattice (NNB-type) couplings**: row 0 is
  `[20/9, -1/3, -2/3, -1/9, 0, -1/9, -2/3, -1/3]`, with the hop-2 entry nonzero. The
  $\mu=0$ control has none. So same-sublattice couplings in the second-order scalar operator are
  compatible with an exactly chiral, local first-order factor. Whether such couplings break
  $\{D,\varepsilon\}=0$ depends on the scalar→staggered bridge, not on bipartiteness alone.

*What the evidence supports.* NNB removes the bipartiteness of the scalar dynamics. SM:539 cites
that bipartiteness as the ground for Theorem 12's identification ("the wave equation is
nearest-neighbor, so the cubic lattice is bipartite"). It is also the premise $\Gamma A\Gamma=-A$
of SM:569's identity $\Gamma_VK_{\rm eff}(E)\Gamma_V=-K_{\rm eff}(-E)$.

*Required.*
- Restate the tension at that level: the scalar-update bipartiteness and SM:539/SM:569.
- State that its transfer to $D_{\rm st}$ (Theorems 3, 12, 13) is the bridge that SM:306 and
  QP:298–305 name.
- Note that NNB is an armable P3 coupling, local to a protocol.
- Change the §A.31 label from NEW to ELABORATING. The added content is that SM:539 and SM:569
  rest on the scalar-update bipartiteness.
- Correct §0 item 6 and §11's scoped conclusion to match.

### B2. NQ2 and §10's third bullet: the corpus already examines SM:112's rule as an NNB source

The writer says: "Whether this yields an encoded phase, and at what cost to the grading, is not
established anywhere read." NQ2's *First check* is "whether the SM:112 rule … is reversible
with symmetric armable couplings at all (its reads are directed)". Three records on `main` at
`fd539e15` already treat this:

- **MECH-1** (`oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md:877–893`, "SM §3.1 as a
  candidate source"). The SM:112 rule "couples `i` to `i + 2`, a same-sublattice (NNB-type)
  edge". At odd $q$ it is non-affine, so its joint encoded action is not CP. "The adjacency is
  not symmetric, so the branch map is not symplectic … and not CP." Its controlling cells are
  ordinary dynamical cells, which Proposition T′(i) does not permit.
- **MECH-2** (`mechanism-2-20261108/DESIGN.md` §0). It treats $G_{\rm SM}$, the SM:112 rule at
  $q=2$, whose edges are not reciprocal for $L\ge5$. Theorem U2: for every fixed bijection,
  under $R1^{\otimes n}$ and H-LIFT, there is "no encoded `S`, `T`, CNOT …". Lemma Q's
  conservation fails for $G_{\rm SM}$.
- **M-INACC-1** (`minacc-1-20261108/DESIGN.md`, RESULT §0). For the symmetrized switched graph
  $G_\sigma$ at $q=2$, Lemma Q(iii)'s protection fails. The $N_0$ limit, with all
  $\{i,i+2\}$ edges, is QA's NNB-type linear class.

*Required.*
- Replace the negative with these results.
- Rescope NQ2 to what they leave open: preparation-class confinement; an armable *symmetric* NNB
  coupling under P1–P3; exact coexistence with the reference grading (after B1's correction);
  and the link to H-Bell.
- Drop or replace the "first check".
- §0's coverage list should state that these records were not read.

### B3. F4, §0 item 4, §11 and NQ1: the complex-structure finding is partly contradicted and partly refuted

The core computation stands. Probe R1 (exact sympy, independent of the writer's script):

- A generic $O$-equivariant symmetric $\Sigma$ on the six signed links has eigenvalue
  multiplicities (1, 2, 3).
- Its stabilizer has dimension **4** in $\mathfrak{so}(6)$ and **14** in $\mathfrak u(6)$.
- $T_1$, $E$ and $A_1$ are of real type.

So Theorem 5's $\mathrm U(3)\times\mathrm U(2)\times\mathrm U(1)$ needs a complex structure, and
SM:340–342 does not list one among its premises. Three parts of F4 do not survive:

- **(a) "It is not named or justified separately."** The corpus names it twice.
  - SM:505: the carrier is "equipped after-the-fact with the complex inner-product structure
    $V_K=\mathbb C^6$".
  - SM:809 (§6.5): the explicit map $\phi\mapsto M\in\mathrm{SU}(N)$ "is under-determined at
    several enumerable joints (the real-to-complex step, the unitarization prescription)".

  Restate as: "not listed among Theorem 5's premises; named as an open joint at SM:809 and as
  after-the-fact equipment at SM:505".
- **(b) "SM:130 refers to 'the custodial U(6) of the real lift'; a real lift carries O(6), not
  U(6)."** This is refuted for the real lift's dynamics. Probes R1 and R1b, exact:
  - For one non-null mode ($a=1/2$) of $F(u,v)=(v,av-u)$ on $\mathbb R^6\oplus\mathbb R^6$,
    the commutant of $F$ in $\mathfrak{sp}(12,\mathbb R)$ has dimension **36**.
  - Every element commutes with the positive-frequency complex structure
    $J=\big((f-\cos\omega)/\sin\omega\big)\otimes I_6$. This $J$ satisfies $J^2=-1$, commutes
    with $F$, is symplectic, and commutes with the $O$ action. So the algebra is $\mathfrak u(6)$.
  - The stationary $O$-equivariant covariance $C=K\otimes\Sigma$ has stabilizer dimension
    **14** inside it, against **4** for configuration-space $\mathfrak o(6)$.

  This is the isotropic-oscillator $\mathrm U(n)$, which is nonlocal in space. A "custodial
  U(6) of the real lift" is therefore defensible on its non-null sector. The exception is the
  null modes at $\alpha=1/d$ (SM:292). There $f$ is unipotent: its commutant is
  $\{tI+r(f-I)\}$, and no $O$-commuting $J$ exists, because the block-scalar commutant of the
  $O$ action has no square root of $-1$.
- **(c) "Supplied, not generated" (§0 item 4, §11).** This is premature. Narrow it to: "not
  derived in SM. A canonical candidate (positive-frequency $J$) exists on the real lift's
  non-null sector. Open: the null modes, whether $\Sigma$ is $J$-linear, and the lift itself
  (B12)."
  - NQ1 must be reframed. Its parts (a) and (b) have the standard positive answer off the null
    modes. The discriminating content is the null-mode sector and the identification of
    $\Sigma=\langle\phi\phi^\dagger\rangle$ with the $J$-Hermitian covariance.
  - The "no ⟹ SU(3) not reachable from a real carrier" branch needs restating to match.
  - Cite `oi-qm-ext-1/two-mode-drive.md` §3. It builds a complex structure on the second-order
    phase space ($J=T_0$, "Multiplication by i is exactly the zero-coupling quarter-turn J") and
    shows $T_kJ-JT_k\neq0$ for coupled steps.
  - Change F4's §A.31 label from NEW to ELABORATING, keeping the stabilizer computation as the
    elaboration.

### B4. Continuous state mixing and interference: Main:590's qualifier is dropped

Main:590 states the observer-level lift negative only "in every formulation stated that lands in
the operational interface …, **the site-space wave-operator formulation being unresolved rather
than excluded**". The document drops this qualifier in three places:

- the §6 "Interference" row: "Main:590 shows the substratum and the observer-level lift supply
  neither";
- B23's lift clause;
- §11's "not generated: … continuous state mixing".

This states a no-go beyond the class ruled out (Code Review Rules, "Bridge and no-go scope").
Restore the qualifier at each site.

### B5. The authorization is misquoted

The header says: "Paper-only: no computation beyond tiny sanity checks of algebraic claims being
traced", and attributes this to #1211 c.6738806776. That record says only "no computation;", with
no exception. Quote the owner record exactly. If the sanity checks rest on a separate instruction
from the coordinating session, cite that instruction separately. Otherwise state that they fall
outside the owner record.

***

## 2. Nits

- **N1 (F9, §12 Q2).** The vacuity is already tracked as **#1188** (KERNEL-VAC-1, open). Its owner
  decision of 2026-11-07 reads "Do not use it as scientific evidence". It is also noted at
  minacc-1 DESIGN:585. Owner question 2 is therefore already decided: cite #1188 and drop the
  question.
  - `MonoidalCompletion.lean:360` is the *definition* of `conjChannel`. The identity
    $\mathrm{conjChannel}(i\cdot1)=\mathrm{id}$ follows from it.
  - Other sites cite `readWriteSourced_not_qm` and belong in the propagation list: GR:260,
    `verification/README.md:298`, `audits/operational/completion-assumption-audit.md:95`,
    `programmes/substratum/route-b-audit.md:29`, `source-audit.md:100,121`, and
    `RouteB.lean:13`.
- **N2 (F11).** The SM:112 defect is already recorded at M-INACC-1 DESIGN:274–278. The diagnosis
  "interval reversed" is wrong. The undirected degree takes the values 2, 3 and 4. Hand check:
  the neighbours are {i−1, R(i), i+1}, plus i−2 when $x_{i-1}=0$, so the correct range is
  [2, 4]. F11's SM:106 clause is correct.
- **N3 (F8).** Address the corpus's stronger claims:
  - book ch06:28 and FULL:1541: "follows from the lattice representation theory … not from a
    separate spin-statistics postulate";
  - book ch10:36: the spin–statistics theorem as a consequence of the emergent QFT's Lorentz
    invariance.

  F8 stands. Representation labels give spin under H-spin', not statistics, and the fermionic
  measure is open (SM:290–292). The book statements become findings in their own right.
- **N4 (F7).** The same "exact change of variables" wording appears in book ch05:91 and
  FULL:1409.
- **N5 (F4, F5 site lists).** The unitary stabilizer is presented without a complex structure
  at Sub:163, Structure:152, Structure:1153, FULL:736, FULL:939 and FULL:1226. For F5, cite
  Sub:393–395, which places the SM gauge group at Level 2, the emergent QFT: this is the
  competing anchor. Also cite SM:511, which places the commutant at the bijection level.
- **N6 (§4 counts).** The counts are wrong (§A.30).
  - St rows: 9 (B1, B6, B8, B10, B11, B21, B23, B25, B26), not 6.
  - Rows with a "none identified" clause: 14 (B4, B7, B12–B17, B20–B25), not 12.
  - Op rows: 7 (B1, B3, B5, B7, B8, B20, B27), not 5.
- **N7 (labels).** Slash labels (E/QS on B6, B20, F2 and §9; E/Op on B7) blur empirical
  selection with QS.
  - Bell violation is observed (E2), so label it E, plus St for which hypothesis is dropped.
  - The Bravais type is selected by the observed gauge group, so label it E.
  - Keep QS for target-defined items such as premise I.
- **N8 (F6 / §3.2 E6).** SM:176 also cites the classical Ehrenfest and Tangherlini orbit
  instability. Narrow the finding to "the atomic-stability filter as stated includes a quantum
  statement".
- **N9 (complex-phases row).** Add the kernel negative at GR:260: `onesFixing_not_phasesAvailable`
  and `substratumClass_not_onesFixing` in `PhaseSource.lean`. It is scoped to level one on the
  physical carrier.
- **N10 (§3.1 and ingredients).** Main:274 and Main:590 derive an exact strongly continuous path
  of $*$-automorphisms (`driveQ_isContinuousPath`). Mention it, with its status: derived, but
  not an executable operation.
- **N11 (§3.1, Bell row).** "Reached only by adopting ontic parameter dependence" omits the
  measurement-dependent alternative, $I_{\rm ont}\ge0.0309$ bits (Main:22, Main:404–406). The
  framework chose parameter dependence.
- **N12 (F3).** Main:66's "standard postulate" alternative is itself motivated by QM unitarity,
  so "removes the circularity" overstates. Main:62 and Sub:94 already state the empirical anchor
  openly, so F3 is CONFIRMING.
- **N13 (F1).** Note Sub's own scoped statements at Sub:14, Sub:193 and Sub:373. Sub:68 is a
  sentence-level overstatement, inconsistent with them.
- **N14 (F10).** Sub:44's own paragraph names the unresolved coherent-instrument extension. The
  finding concerns the word "interference" only.
- **N15 (B8).** Cite A5-LINEAR-AFFINE R5 (`programmes/substratum/a5-linear-affine-20261104`):
  "none selects b = 0 with an independent justification". It is a corpus-wide confirmation of
  "St".

***

## 3. Per-finding table

| Item | Verdict | Basis |
|---|---|---|
| F1 Sub:68 overstates forward direction | **Confirmed** | Main:20, Main:22, Main:82, Main:99, Main:218, Main:556; SM:22–24, SM:232, SM:290–292 all read as quoted. Nit N13. |
| F2 Bell branch is a selection | **Confirmed** | Main:362, Main:403–407, Main:414, Main:429; Sub:131–133. Label nits N7, N11. |
| F3 bijectivity uses unistochastic input | **Confirmed** (mitigation overstated) | Main:62 quote exact; Main:726 (iii); Sub:94. N12. |
| F4 SU(3) needs complex structure | **Narrowed** | 4 vs 14 confirmed (R1). "Not named" is contradicted by SM:505 and SM:809. The SM:130 O(6) claim is refuted (R1/R1b: $\mathfrak u(6)$ symmetry of the real lift off the null modes). B3. |
| F5 gauge group placed at substratum | **Confirmed** | SM:312, SM:316, SM:344 vs SM:428, SM:515 (also SM:511). Sub:395 supports. N5. |
| F6 QM imported at dimension filter and gravity lemmas | **Confirmed, narrowed at E6** | SM:122–124, SM:140–142 confirmed; SM:176 also classical. N8. |
| F7 "exact change of variables" | **Confirmed** | SM:288 vs SM:290–292. Mirrors in N4. |
| F8 spin–statistics imported | **Confirmed** (book counterclaims to address) | SM:454, SM:452; book ch06:28, ch10:36. N3. |
| F9 `readWriteSourced_not_qm` vacuous | **Confirmed** | Read in Lean: `ReadWriteSourced` (RWC:158–160); `readout_avail`, `readout_is_localLuders`, `availExt_coarse` (OperationalAssembly:594–660); `localLuders` (:191); `conjChannel` (MonoidalCompletion:360). With $i\cdot1\ne$ `permMatrix σ` on nonempty `Fin 2 × Fin 1`, the hypothesis has no instance. QP:865 says the same. Tracked as #1188. N1. |
| F10 interference language | **Confirmed** (wording-level) | Sub:44, Sub:463. N14. |
| F11 SM:112 / SM:106 | **Narrowed** | The typo is real but the diagnosis is wrong (degree {2, 3, 4}); already recorded at M-INACC-1:274. The SM:106 clause is right. N2. |
| Q6 native obstruction vs SM chirality | **Narrowed** (cross-level claim refuted as stated; NEW contradicted) | QP:298–305, SM:306, R2. Supported residue: SM:539, SM:569. B1. |
| NQ1 canonical J | **Narrowed** | Standard positive answer off the null modes (R1b). Remaining content: null modes, $J$-linearity of $\Sigma$, B12. two-mode-drive.md §3. B3. |
| NQ2 state-dependent NNB | **Narrowed** | First check answered: MECH-1:877–893 (odd $q$), MECH-2 Theorem U2 and Lemma Q failure ($q=2$), M-INACC-1. Residual coexistence question open. B2. |

Ledger rows not listed above were spot-checked against their sources and match, apart from the
counts (N6). Spot-checked rows: B1–B3, B5–B8, B10–B14, B16–B19, B21, B22, B24, B26 and B27, and
S1–S29.

***

## 4. Citation check (summary)

Opened and quoted at `fd539e15`. These match the document's quotations:

- Sub:26, 44, 68, 76, 78, 92–102, 123–137, 145, 161, 163, 181–185, 193, 203, 225–227, 270–274,
  348–361, 459, 463, 518–523;
- Main:20, 22, 44, 48, 56, 62, 66, 82, 86, 99, 117, 137, 145, 173, 186–202, 218, 226, 268–274,
  288, 306, 326, 362, 364, 403–407, 414, 416, 429, 548, 556, 564, 566, 584, 590, 600, 654, 726;
- SM:12, 22, 24, 68, 106–118, 122–124, 130, 136, 140–142, 150, 176, 196, 222–240, 264–276,
  286–316, 326, 328–380, 428, 434, 448–468, 485, 499–515, 527–571, 579, 585, 589, 611, 625–647,
  681, 683, 809, 1422, 1424;
- QP:1–98, 120–176, 236–262, 286–345, 440–470, 744–770, 803–880, 895–916, 948–960;
- QPR:15–30;
- OperationalAssembly.lean:185–200 and 540–680; ReadWriteControl.lean (whole file);
  BranchSelector.lean:55–75; MonoidalCompletion.lean:350–368.

Minor inaccuracies:

- MonoidalCompletion:360 is a definition (N1).
- QP:955's marker spans QP:954–956.
- Main:99's quote appears with a non-ASCII hyphen. The text is present.

No misquotation found.

## 5. Corpus-wide search for negative claims (§A.19)

Searched at `fd539e15`: all `papers/*.md`, `book/*.md`, FULL.md, `verification/programmes/oi-qm/**`,
`verification/programmes/substratum/**`, `verification/audits/**` and
`verification/lean-mathlib/OIBridge/*.lean`, using `git grep` on the claim's terms and
paraphrases.

**The corpus contradicts or adds to these claims:**

- Q6 "NEW": QP:298–305; SM:306. → B1.
- NQ2 "not established anywhere read": MECH-1 DESIGN:877–893; MECH-2 DESIGN §0; M-INACC-1 DESIGN
  and RESULT. → B2.
- F4 "not named": SM:505, SM:809. On a complex structure on the second-order phase space:
  `oi-qm-ext-1/two-mode-drive.md` §3, plus the reviewer's probes R1 and R1b. → B3.
- Lift no-go scope: Main:590's "site-space wave-operator formulation … unresolved". → B4.
- F8: book ch06:28 / FULL:1541 and ch10:36 assert a derivation that their own support does not
  reach. This is a finding to add; the negative stands. → N3.
- F9 owner question: #1188 and minacc-1:585. → N1.
- F11: M-INACC-1:274–278. → N2.
- F5: Sub:393–395 and SM:511 (supporting). → N5.
- Complex phases: GR:260, `PhaseSource.lean` kernel negatives (supporting). → N9.

**The corpus confirms these claims:**

- Born exponent open: `born-sel-b-measure-20261104/QB3-EVIDENCE.md` Status, "OI has not yet
  been shown to derive the Born rule or select the physical probability measure".
- Fermionic measure open: no derivation in `verification/`; SM:290–292.
- H-Bell open: only `h-bell/round-hb-1-obligation-shape/preregistration.md` exists.
- Linearity beyond affine has no independent justification: A5-LINEAR-AFFINE R5.
- Bare adaptive S open: `quarter-phase-feedback-20261107/RESULT.md` §1; QP:897–915.
- Complex matrix kinematics open: Main:218, Main:564.
- Site factorization open: SM:68; Main:726 (viii). No record found that selects it.
- Observer-level CI open: SM:276. No record found.
- φ → L_obs open: SM:232; Main:590.

## 6. Independent checks on items 5–8 of the review brief

- **{D, ε} and NNB.** Covered under B1. The writer's algebra is correct for a term added to $D$.
  It is not established for the NNB coupling as QP defines it. Probe R2 is the countercontrol.
- **The three questions kept apart.** Column (iii) is never used as support for column (ii) in
  the ledger. Mixed E/QS labels blur empirical selection with QS (N7). Consistency is labelled
  C correctly (B17, H-χ').
- **§A.34.** §2 correctly excludes the QM → (S, φ, V) direction: Sub §3.1–§3.2, Theorem 23, and
  Main's gluing and uniform-continuum theorems. Displayed equivalences cite two-direction
  support:
  - Theorem 3: both kernel directions named at SM:304.
  - Operational completion: necessity and sufficiency named at Main:564.
  - $S\iff D\iff Q_{\rm fb}$: kernel directions named at Main:99.

  No QM → substratum result is counted toward the forward bridge.
- **Register and authorization.** "Recorded only" disclaimers are present on F1 and §12. The one
  defect is the misquoted authorization (B5). The F4 statement "SM:130 … should say O(6)" is a
  manuscript-correction claim that is also wrong (B3(b)). No new physical assumption is adopted.

## 7. Reviewer probes

All are in `scratchpad/bridge/review/probes/`, use exact sympy, and import nothing from the
writer. They are controls on algebra, not evidence for new results.

- `r1_carrier_stabilizer.py`
  - (a) Multiplicities (1, 2, 3). Stabilizer dimension 4 in $\mathfrak{so}(6)$, 14 in
    $\mathfrak u(6)$.
  - (b) For a one-mode real lift ($a=1/2$), the commutant of $F$ in $\mathfrak{sp}(12)$ has
    dimension 36. The stationary $O$-equivariant $C$ has stabilizer 14 inside it, against 4
    inside configuration-space $\mathfrak o(6)$.
  - (c) At the null mode ($a=2$), the commutant dimension is also 36, but non-compact (see R1b).
- `r1b_positive_frequency_J.py`. The positive-frequency $J$ satisfies $J^2=-1$, commutes with
  $F$, and is symplectic. Every element of the commutant commutes with $J$, so the commutant is
  $\mathfrak u(6)$. At the null mode the commutant of $f$ is $\{tI+r(f-I)\}$ with $(f-I)^2=0$,
  so there is no complex structure.
- `r2_grading_levels.py`. The countercontrol of B1, with the $\mu=0$ control and the writer-style
  control ($\{D_0+h,\varepsilon\}\ne0$).

## 8. What a revision needs for ACCEPT

1. Fix B1–B5.
2. Apply N1, N2, N3 and N6, which are factual.
3. Rerun the novelty labels (§A.31) after B1–B3.

A delta review of the changed passages is sufficient if nothing else changes.
