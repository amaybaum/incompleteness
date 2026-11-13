# OA-1 (r2): can one fixed deterministic substratum supply preparation, control, measurement and complete records?

**Standing.** WIP / UNVERIFIED author report for unit OA-1 under #1169, revision r2.
- r2 applies findings 1–8 of the independent review `REVIEW-OA-1.md` (verdict ACCEPT WITH CHANGES;
  same model family, read-only), as relayed by the coordinator. r1 (`OA-1-REPORT.md`) is
  unchanged.
- Authorization: owner amaybaum, 2026-11-12, #1169 comment 6829742537, with the owner-approved
  scope addition "Fold into OA-1 (Recommended)". Paper-only.
- This file adopts no premise, promotes no claim, edits no manuscript or Lean file and runs no
  computation on any OI rule. The unit ends with an owner decision checkpoint. TUNE-1 Step 3 stays
  paused.

**Snapshots.** `main` = `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, read with `git show`.
- Citation forms: `Main:n` for `papers/Main.md`; `OB/File:n` for
  `verification/lean-mathlib/OIBridge/`; other paths relative to
  `verification/programmes/oi-qm/reconstruction/`.
- TUNE-1 is read from `research/tune-1-20261111` at `d47a6377f2d8753f88ddc4d3ab0c03ead64393dd`
  (`T1/<file>:n`). It is off `main` and is cited as research, never as an established premise
  (§A.46 item 7).

**Support labels.**
- **[K]** Lean statement on `main`; the statement was read and nothing was built.
- **[P]** manuscript statement on `main`.
- **[R]** research record stating that it is not independently established.
- **[W]** my own derivation, unreviewed except by `REVIEW-OA-1.md`, and not kernel-checked.
- **[O]** open.

**Disclosure.** Commands, r1 and r2:
- `git` (fetch, show, ls-tree, grep, log, rev-parse, status, diff --stat), `grep`, `sed`, `wc`,
  `ls`, `mkdir`, `cat -n`;
- one `curl` of comment 6829596317, with one `python3 -I` parse of its author, date and length;
- GitHub MCP reads of #1169.

For r2 I re-checked against `fb733b4a` every source the review introduced:

| Source | Checked |
|---|---|
| Main | :147, and ledger items (iv) and (vii) at :724 |
| Lean | `OB/DiscreteCompletion.lean:45` |
| `mathcon1-polc-20261108/DESIGN.md` | :578–592 |
| `round-arp1-marc-20261108/result.md` | :36–38 |
| `mechanism-2-20261108/DESIGN.md` | :66–72 |
| `apparatus-1-20261107/DESIGN.md` | :506–512 |
| `oi-pseudoentropy-20261025/README.md` | :148–151 |
| `git grep M-INACC` | over `main` |

Nothing was committed, pushed or posted. Files in this directory dated 2026-10-20 were not written
by this unit and were not used. `Main.fb733b4a.md` and `REVIEW-OA-1.md` were written by others in
this session; only the review was read, as the instruction for this revision.

***

## 0. Plain-language summary

1. The exact theorem S⇔D⇔Q_fb never fails, but it chooses the world after the target, so it is
   not a test of a given world.
2. With the corpus's linear lattice rule fixed in advance, I followed four operations in order:
   prepare, control, measure, record.
3. Preparation comes first in that order. Under OI's global maximum-entropy measure, nothing the
   observer physically holds now says anything about the hidden world now, so no hidden carrier
   can be prepared from held records. Visible carriers can be, at an exponential herald cost.
   This holds only under that measure, and classical computers share it. Under Main's per-orbit
   and record-compatible measures it is open.
4. Control fails under every measure. Under any affine rule, which is the form Main derives from
   its gauge argument, a setting stored in the world can only shift values. It cannot choose which
   operation runs or which quantity is read. An ordinary classical reversible computer can do
   this, so this gap is classical.
5. On a parallel branch, the kernel's observer interface grants full classical write access and
   external records, and is still capped: no phases and not `DerivedOI` on any carrier, no dense
   control on the two-state carrier. Changing the rule cannot lift that cap.
6. The escape the existing no-go results leave open, already named in MECH-2 and mathcon1, is a
   derived inaccessibility (M-INACC) on growing carriers. No source read here, and no hit of a
   `main`-wide search for it, constructs it.
7. This pass yields no new findings. Every result confirms or elaborates existing records.

***

## 1. Definitions in OI's own terms

**Data of one physical setup.** `𝔖 = (S, φ, (V, H), μ, A)`:
- `S` is finite (Main:60; ledger item (ii), Main:724), and `φ` is a bijection fixed **before** any
  target is named.
- `V ⊊ S` is the observer's registered configuration and `H` the hidden sector (Main:42, :48).
- `μ` is one of the three measures Main states:
  - **(μ-G)** the global counting measure, uniform on `C_V × C_H` with the uniform conditional law
    on `C_H` in each visible fibre (Main:54, :58);
  - **(μ-O)** the uniform measure on the orbit of the actual microstate, unique and invariant
    (Main:54, :60);
  - **(μ-R)** the maximal-entropy invariant measure compatible with the observer's records,
    ledger item (iv) at Main:724, a posit (Main:60).
  A structured prior declared as a realization datum (Main:58, :97, :602) is a named premise
  wherever it is used.
- `A` is the apparatus layout (carrier, setting, meter and record cells), fixed once for every
  setting.

There is no write access outside `φ`. Settings are configurations of designated cells, set as an
initial condition or written by `φ` from the observer's own records.

**Native, premise, not supplied.**
- An operation is **native** if `(φ, partition, μ, A)` supplies it, with every probability computed
  from `φ` and `μ`.
- It is **supplied under a named premise** if it needs one extra named statement and that
  statement carries no target data.
- It is **not supplied** if neither holds.

**Non-import test (§A.29, hard-to-vary form).** A construction imports its target if its supplied
elements can be re-tuned, with `φ` and the partition unchanged, to realize a non-quantum target
with equal ease. Examples of such targets: a gbit, a Born exponent `p ≠ 2`, an arbitrary finite
instrument table.

**Four operations, two tiers.** The tiers are infrastructure (target-neutral) and qubit (§4.2).

| | Operation | Infrastructure tier (what counts as supplying it) |
|---|---|---|
| N1 | Preparation | A record event `E` with `P(E) > 0` reported, and its complement recorded as failure. A designated carrier `Σ`, visible or hidden, whose conditional law `ν_E` at preparation time differs from its unconditional law. `E` is held by the observer when `Σ` is next used. `ν_E` does not depend on later settings. |
| N2 | Controllable interaction | Setting cells `s` and a duration `τ` such that the non-translational part of `φ^τ`'s action on `Σ` depends on the content of `s`, for at least two operationally distinct values. The initial law of `s` is independent of `Σ` (ledger item (xiv), Main:724). |
| N3 | Measurement | A meter whose later recorded value is correlated with a functional of `Σ`. It is *selectable* when a setting (N2) fixes which functional is read. The residual `Σ` is handed on. |
| N4 | Complete records | Every outcome, herald and failure of a protocol is physically held in `V` at the end, together with the observer's knowledge of the residual carrier. |

***

## 2. Facts derived here (paper; [W] unless cited)

**D1 (stationarity: any bijection, any φ-invariant μ).** Since `μ∘φ⁻¹ = μ`, the unconditional
law of the full state is the same at every time.
- No dynamical step prepares anything unconditionally.
- Every time-specific preparation, and every new same-time correlation between a record and a
  carrier, is conditional on a record event. ∎

**D2 (equal-time blindness, under μ-G only).** Main:58 fixes μ-G, and μ-G is φ-invariant
(Main:54). The law at every time `t` is therefore uniform on `C_V × C_H`.
- Disjoint cell sets are independent at `t`.
- In particular, `H_t` is uniform and independent of every function of `V_t`. That covers every
  physically held record, memory included. ∎

*Relation to the corpus.* D2 is Main:58 plus invariance, and Q-b1
(`observer-interface-obsmu-20261104/ANALYSIS.md:907–912`) already states it for the counting
measure on `C_V × C_H`, with no automorphism hypothesis; D2 does not extend Q-b1. What D2 adds is
an ELABORATING point:
- obsmu leaves in-`V` retention open as the route to preparation (:913–917; O-RET, O-REC, O-ACC);
- under μ-G, D2 applied at `t_0` closes that route, because a retained record is a function of
  `V_{t_0}`.

*Scope.* D2 is **not established** under μ-O or μ-R. Each of those laws is invariant but in
general not a product, so `V_t` and `H_t` can be correlated (see N1.1b).

**D3 (herald bound).** For any event `E` and carrier `Σ`,
`P(Σ_t = σ | E) ≤ μ(Σ_t = σ) / P(E)`. Under μ-G this is at most `1 / (|Σ| P(E))`.
- A preparation whose most likely value has probability `p_max` succeeds with probability
  `P(E) ≤ 1 / (|Σ| p_max)`.
- Point-preparing `M` distinct `q`-ary cells at one time costs `P(E) ≤ q^{−M}`, with equality for
  the herald "those cells show the target values". That herald is a visible herald on visible
  cells, which is how visible carriers are prepared. ∎

**D4 (complete in-`V` records under a stationary law; ELABORATING; corrected in r2).** Suppose the
observer's present configuration determines its previous one, `V_{t−1} = g(V_t)`, as complete
in-`V` records require. Suppose also that `μ` is μ-G, or any stationary law.
- *(a) The step is a permutation.* `V_t` and `V_{t−1}` have the same law, so `g` pushes that law
  onto itself. A non-injective map on a finite support leaves a point without mass, so `g` is a
  bijection on the support. Then `T(v, v′) = 1` exactly when `v = g(v′)`, so `T` is a permutation
  matrix. Since `T` is time-homogeneous, one complete step anywhere forces this.
- *(b) C1 fails.* By Main:147, `T` is a permutation matrix if and only if
  `φ(x, h) = (φ_V(x), σ_x(h))`. The visible dynamics then never depends on `h`, so (C1) fails at
  every step (Main:72), and (C4) fails with it.
- *(c) Reading.* Complete in-`V` records in an equilibrium state exclude **any** hidden influence
  on `V`. This is the blank-memory (Landauer-type) cost of D3 again, and so MP-0a. It is a
  corollary of D2 or stationarity together with Main:147.
- *(d) Scope.* Full-history records only. D4 does not cover partial records (functionals of the
  past), and it dissolves under H-LOW. r1's description of a "Markov chain of `T`" with
  "memoryless noise" was literally true but misleading: the chain is a deterministic permutation
  and the noise is trivial. ∎

**D5 (Lemma A; any affine rule; measure-independent).** Let `Φ` be affine on the configuration
group. Write the initial state as `(c, x, u)`: setting, carrier, rest. Then
`Φ^τ(c, x, u) = L_c c + L_x x + L_u u + k`, with `L_•` and `k` independent of `c`.
- The non-translational part of the carrier's map does not depend on `c`.
- Every record is `H_O r_O + H_P c + H_U u + const`. The functionals the records read do not
  depend on `c`.
- An affine exchange that writes `c` into cells changes nothing above, because its linear part
  `I − Π_C` does not involve `c`.
- Parts (i) and (ii) need only that the setting's law is independent of the rest. No uniform law
  is used, so the failure holds under every measure.
- Under μ-G the record law is also coset-uniform.

*Scope.* Ledger item (vii) (Main:724) states that amplitude-scale gauge invariance yields the
affine form, and adds linearity (A5) as a further posit. D5 therefore covers the **gauge-derived
affine class**, not only R-lin.

*Status.* One paper proof, re-derived twice at the same layer (§A.22: no added weight):
- MECH-1 Lemma A (`mechanism-1-20261107/DESIGN.md:404–430`) [R];
- TUNE-1 Lemma A-T (`T1/TUNE-1-STEP2-SESSION3.md:32–98`) [W]; its "reviewed" status is a ChatGPT
  review, ACCEPT WITH SCOPE QUALIFICATIONS, recorded at `T1/TUNE-1-STEP2-SESSION4.md:13–16`;
- this file. ∎

**D6 (point 3; [W] on [K]).** A theory generated from φ's configuration bijections by the closure
rules of `FiniteOperationalTheory` (`OB/OperationalAssembly.lean:594`ff.) is, in availability, a
sub-theory of `permTheory 𝒮.Conf`.
- That theory contains every permutation conjugation (`OB/SubstratumInterfaceAudit.lean:406`) and
  is closed under the same rules.
- `NonnegBounded` (`OB/FrozenSourcing.lean:65`) is monotone under availability inclusion. The
  ceiling therefore follows from `obsTheory_nonnegBounded` (:84).
- No kernel theorem states the sub-theory step itself, so D6 stays [W] on [K].
- `nonnegBounded_of_bijectionLevel` (:74) applies only to a `genTheory` of a bijection-level class
  with an `Architecture`. D6 does not rest on it. ∎

**D7 (post-hoc and timing selection do not supply N2).**
- If no setting changes `φ`'s action, the joint law of all records does not depend on the setting.
  "Choosing a read" then means choosing which already-made record to consult, so every such read
  is a coarse-graining of one joint record.
- Selection by preparation timing makes the setting a different preparation procedure, each with
  one available read. "The setting is the parity of the armed tick, which is available only
  through P3 and E-iso" (`apparatus-1-20261107/DESIGN.md:510–511`). The equivalence of the two
  procedures cannot be certified, and the setting is a function of the preparation record. ∎

***

## 3. The debugging ladder

The stronger target is fixed: one physical `𝔖` across all settings, with source-derived
preparation, control, readout, failures and residual state. Below R2 the ladder **forks** into two
parallel branches. R3 is the native fixed-rule branch. R4 is the kernel interface branch, which
grants more control and external records but restricts the identification. R4 is not a later rung
of R3.

### R0. `finite_horizon_equivalence` (S⇔D⇔Q_fb)

- **Holds [K]:** `OB/Equivalence.lean:462–469` (`S_imp_D` :422, `D_imp_Qfb` :294, `Qfb_imp_S`
  :245); Main:546–552 [P].
- `S_imp_D` builds a clock-and-trajectory carrier with `init := marg P ι`, so the target sits in
  the prior.
- **Target:** N1–N4 are not addressed. There are no settings, and the records are held in `H`.
  This rung cannot fail.

### R1. + embedded readback (C1–C4)

- **Holds [P/K]:** Main:68–80, :602–612, and the kernel identities cited at Main:97.
- **Target:** unchanged. C1–C4 supply no settings, preparations or records. C2 persistence by
  reversibility is global (Main:74).
- **Corrected D4:** complete in-`V` records together with a stationary law exclude C1 entirely.
  "Hidden predictive memory = unstored history" (Main:97) is the CONFIRMING restatement
  (AW-OA1-1, §7).

### R2. + one common realization for a fixed finite experiment

- **Holds [P; certified by probes, no kernel]:**
  - comb theorem (Main:480–482), with `u_c ~ P(·|c)`;
  - gluing theorem (Main:564–578);
  - single controlled dynamics (Main:580, verbatim: "Quantum mechanics enters as the instrument
    data and as the state held in the hidden register");
  - uniform continuum (Main:596).
- **Target:** realized with supplied data. It fails the non-import test by its own statement:
  "the same reversible machinery can realize non-quantum finite instrument families" (Main:582).
- **Classical control:** passes any finite target, so this rung's criteria do not discriminate.

### R3 (branch A). Sourcing from the actual substratum: the depth-first chain

The fixed rule is **R-lin**, the corpus's posited rule (items (vii) and (xiii), Main:724). Where a
result holds for the whole gauge-derived affine class, that is said.

**Node N1: preparation.**
- **N1.1a (μ-G, held records).**
  - By D2, conditioning on any function of `V_t` leaves `H_t` uniform. **No hidden carrier** is
    prepared natively from a record held at preparation time. This holds for every bijection
    under μ-G.
  - A **visible** carrier is prepared natively by a herald on `V`, at the D3 cost.
  - Under μ-G, D2 also closes obsmu's in-`V` retention route (§2).
  - The verdict is target-neutral: the classical control fails it too (§4.1).
- **N1.1b (μ-O, μ-R): open [O].** D2 is not established there.
  - μ-O is native and derived (Main:54, :60). Its law is uniform on one orbit and need not be a
    product.
  - μ-R is ledger item (iv), a posit. It is orbit-level conditioning on records, i.e. entropy
    maximization compatible with them. Whether its records count as held in `V` is the same
    question as MP-0b. This report reads μ-R as a posit, not as native supply.
  - Whether either measure supplies a held-record preparation of a hidden carrier is not
    decided here.
- **N1.2 Under μ-G, by premise.** Either of two different-type premises:
  - **MP-0a, H-LOW (resource).** Admissible form: fixed known values on designated cells, chosen
    independently of settings and carrier, with the law uniform elsewhere. It is a declared joint
    initial law on `C_V × C_H` (Main:58, :97, :602), a datum and not a supply. Apparatus-1's P2 is
    an instance (`apparatus-1-20261107/DESIGN.md:298–303`, :418). In this form it passes the
    non-import test. The general "structured prior" channel does not: that is how R2 supplies its
    target (Main:482, :522, :580).
  - **MP-0b, H-MEM (interface convention, not a resource).** The observer's visible history counts
    as its record, held outside `V`. This changes what the observer holds. It conflicts with N4 and
    with a finite-state observer over growing horizons (Main:42). The R4 kernel interface already
    grants it: `FiniteOperationalTheory` keeps outcome labels outside the carrier
    (`OB/OperationalAssembly.lean:594–643`).
  - Reading a conditional law as a laboratory preparation is H-PREP, open
    (`observer-interface-obsmu-20261104/ANALYSIS.md:892–900`; D-OB8, not adopted).
- **N1.3 Content under R-lin.**
  - Conditional laws are uniform on cosets (`T1/TUNE-1-STEP2-SESSION3.md:48–79` [W]; obsmu
    Proposition C, :546–575 [R]).
  - Qubit tier: stabilizer-type states only. At odd `q` there is none outside that class (MECH-1
    Proposition C [R]). At `q = 2` with heralds it is open (L5.4).
- **N1.4 Pressure test.**
  - "Supplied under a premise" is not native supply.
  - Main §4.6 replaces the past hypothesis only "in its role of selecting observer-compatible
    configurations" (Main:742). It does not supply ready cells.

**Node N2: controllable interaction (granting N1 by premise).**
- **N2.1.** By D5, under **any affine rule and any measure**, a setting held in the world enters
  only as a translation. D7 closes the post-hoc and timing loopholes.
- **Verdict: not supplied natively, for the gauge-derived affine class, which includes R-lin.**
  This is one paper proof, re-derived twice.
- **N2.2 Scope.**
  - A generic bijection can contain a classical controlled permutation, and a classical computer
    has one (§4.1). The gap is classical: R-lin is weaker than the classical control at N2.
  - Apparatus-1 selects only through P3 and E-iso (:510–511).
  - MECH-1 M1/CTRL-MON keeps supplied elements (a)–(e) (`mechanism-1-20261107/DESIGN.md:938–1050`).
  - R-nl, under H-nl, is open (`T1/TUNE-1-STEP2-SESSION4.md:553–628`).
  - G_SM (SM §3.1, a stated hypothesis):
    - it switches natively;
    - it breaks A5;
    - its edges are non-reciprocal **for `L ≥ 5`**;
    - its "not CP" verdict is **relative to the R1 frame**, under which joint-CP failure "holds for
      every coupling rule and does not single out `G_SM`", the linear class N included
      (`mechanism-2-20261108/DESIGN.md:44–61`, :95–96);
    - P★'s instrument fails C-CP (:82–90).
  - The Fredkin switch is not identified with the selected ring
    (`controller-preparation-1-20261108/SELECTION.md:105–121`).
- **This is the earliest failure under every measure.**

**Node N3: measurement.**
- A fixed read stream is native (`mechanism-1-20261107/DESIGN.md:815–823`).
- Backaction is native given half-known meters (`apparatus-1-20261107/DESIGN.md:311–325`).
- A selectable read is not supplied (D5(ii), D7).
- Repeatability needs P1 and E-iso.
- A passive internal observer reads existing records only (`OB/InternalObserver.lean:92`, :272,
  :290 [K]).
- **Verdict:** fixed read native; selectable read not supplied.

**Node N4: complete records, failures, residual state.**
- Under R-lin no cell is inert, so values are overwritten. Retention needs P1 and E-iso, or ledger
  blanks, which cost D3 or need MP-0a.
- O-RET, O-REC and O-ACC are open (obsmu :913–925). Under μ-G the in-`V` route is closed (D2).
- Under μ-G or any stationary law, full-history in-`V` records force C1 to fail (corrected D4).
- **Verdict:** not supplied natively. Supplied under P1, E-iso and MP-0a. MP-0b supplies only the
  convention.

### R4 (branch B). The kernel interface `obsTheory 𝒮 := permTheory 𝒮.Conf`

- **Holds [K]:**
  - `OB/SubstratumInterfaceAudit.lean:770`, with `rfl` at :775 and :780; :790
    `obs_dynamics_avail`; :816 `obs_exchangesAvailable`; :708 `permTheory_not_control`;
  - `OB/FrozenSourcing.lean:84` `obsTheory_nonnegBounded`; :99 no phases (any carrier); :111 not
    `DerivedOI` (any carrier); :295, :302 rule-independence; :318, :327 the combined verdicts, on
    `Fin 2`;
  - `OB/StructuralClosure.lean:348`.
- **Dense unitary control is defined only for `Fin 2`** (`OB/DiscreteCompletion.lean:45`). For
  `obsTheory` on `Conf`, the kernel states only no phases and not `DerivedOI`.
- **A parallel branch, not a later rung.**
  - Compared with R3, R4 grants every configuration permutation (H-write;
    `T1/TUNE-1-STEP2-PROPOSAL.md:155–167`) and external outcome labels (MP-0b).
  - It restricts the identification to the configuration basis.
  - R3's encoded-frame qubit tier (5c) lies outside R4's cap.
- **Point 3: confirmed.**
  1. Rule-independence holds by `rfl`. Its substance is maximality: every permutation is
     available, the rule's own update included (:406, :790; `OB/FrozenSourcing.lean:277`).
  2. A rule-derived, bijection-generated interface on the configuration carrier is a sub-theory,
     in availability, of `permTheory 𝒮.Conf`, and is inside `NonnegBounded` by monotonicity from
     :84 (D6, [W] on [K]). Then: no phases and not `DerivedOI` on any carrier; no dense control
     on `Fin 2`.
  3. Rule-sensitivity can only shrink availability under the ceiling. An escape must change what
     an observer operation acts on.

### R5. Candidate replacement interfaces

| Candidate | Escapes R4's ceiling? | Source of the escape | Existing no-go results | Classical control | Single-qubit target |
|---|---|---|---|---|---|
| **5a.** Rule-derived availability on configurations | No (D6) | — | `nonnegBounded_verdict` [K] | classical | fails T-C |
| **5b.** Nonlinear or state-dependent rule (R-nl, G_SM), configuration level | No (D6). G_SM addresses N2 as a proposal | a rule change; G_SM is an SM hypothesis | as 5a; encoded level: MECH-2 Lemma F, U2, NC [R] | Fredkin-type switching is classical | G_SM: P★ instrument non-CP relative to R1; no non-Clifford unitary under R1 (U2) |
| **5c.** Encoded carrier through a fixed linear frame (R1, Gross R-W, eight-sign) | Partly: an encoded Hadamard from a hidden permutation (`operational-quotient-v3/REPORT.md:11–23` [R]) | the identification, a representation choice; the frame is chosen for the comparator's covariance (MECH-1 SC-1) | finite encoded group (U2(ii), R1); nonnegative frame branches (Lemma F); noncontextual **only with spanning-read certification**, which at `q = 2` needs a non-native `Y` read (MECH-2:66–71); no exact `rot` on any finite carrier (apparatus-1 :955–1023; Main:558 [P, half imported]) | with spanning reads: a classical epistricted model | **Reachable by CP operations, relative to the frame: stabilizer/Clifford only.** U2 under R1 (covariance `A_4 ≀ S_n`, MECH-2:52–61); Proposition C at odd `q`; 24 Clifford actions under the eight-sign map; P★ is non-stabilizer but only in a non-CP instrument (MECH-2:76–86) |
| **5d.** Record level: operations on record laws; states are classes of heralded preparations | Not shown. It would need (i) access restriction derived from `φ` (M-INACC) and (ii) an unbounded carrier (Main:558; bounded `\|C\|` excluded at fixed ε, `T1/TUNE-1-STEP2-SESSION4.md:556–575`) | target-neutral by M-INACC's definition, if achieved; whether any `φ` realizes it is open | NC applies unless injectivity or H-LIFT fails, which is M-INACC's content; M-INACC is not supplied by G_SM (MECH-2 §6.2) or `G_σ` (`minacc-1-20261108/RESULT.md:37–60` [R]); ARP-1-MARC (`round-arp1-marc-20261108/result.md:36–38`) | full access is commutative (`OB/CentralObservation.lean:620` [K]); a supplied restriction is caught by the non-import test (KS sphere, Apparatus-1 P1–P3, and op-quotient v3's private-access contract) | exact needs an infinite carrier; approximate needs growing carriers and derived access [O] |
| **5e.** Emergent amplitude space | Only with E-real, E-pair and E-control supplied (`oi-qm-ext-1/two-mode-drive.md:25–40` [R]) | **imported**, resting on: those three supplied elements; `U_φ` is a permutation unitary (Main:552); reversible coherent lifts of permutations are monomial (`OB/LiftSource.lean:164` [K]); layer flows are not executable from observer access (`OB/ExecSource.lean:129` [K]); lifts are non-unique (Main:644); the wave-operator formulation is unresolved (Main:588) | native sign read with the amplitude dictionary does not factor through a density matrix (`oi-qm-ext-1/whole-model-bridge.md:14`, :242 [R]) | Koopman–von Neumann [W]: a classical real, continuous linear oscillator lattice evolves complex normal-mode amplitudes unitarily, so **passing T-C does not discriminate**. This concerns a real continuous lattice, not R-lin over `ℤ/q` | T-C only with supplied E-real, E-pair, E-control; T-M not reached |
| **5f.** Infinite substratum, quasilocal (H-∞) | No by itself (`OB/QuasilocalCharacterization.lean:792` [K]) | — | necessary for exactness (Main:558 [P, half imported]), not sufficient | — | must be combined with 5d |

**MP-2, the open escape (CONFIRMING).**
- The escape left open by U2 (under R1), Lemma F, Theorem NC, Main:558 and TUNE-1's
  bounded-`|C_n|` FAIL-CLASS, each within its hypotheses, is 5d with **M-INACC** on an unbounded
  carrier.
- It is MECH-2's named missing premise (`mechanism-2-20261108/DESIGN.md:108–117`, §6.2: "needs a
  change in the identification and access, not in the dynamics alone").
- It is also mathcon1's Shape 1 (`mathcon1-polc-20261108/DESIGN.md:585`: "non-injective
  protected-functional access rule … M-INACC").
- ARP-1-MARC refines Lemma Q's status: in its finite ring model (`L ∈ {7, 9}`, `q = 2`, `T = 4`),
  protection of `Q* = 1` functionals survives removal of coupling isolation. It stays conditional
  on supplied registration, on P2 with its support clause, and on H-PREP, and it does not adopt
  Lemma Q as an instance of M-INACC (`round-arp1-marc-20261108/result.md:36–38`). The isolation is
  not what carries the protection there; P2 and the access rule do.
- Other routes remain open:
  - over native `Z`/`X` reads, without a `Y` read, NC does not apply at `q = 2` (MECH-2:69–71);
  - mathcon1 Shapes 2 and 3 (:586–587).
- "Non-importing" holds by M-INACC's definition ("a reason not chosen to reach the target").
  Whether any `φ` realizes it is open.
- **Search scope of "not constructed".**
  - Covered: the sources read here plus `git grep M-INACC` over `main@fb733b4a`.
  - Hits: mathcon1, MECH-2, minacc-1 (DESIGN, RESULT, A1–A3), ARP-1-MARC (preregistration,
    result, controls), `substratum/a5-linear-affine-20261104/q3-a6-offsets-20261108/DESIGN.md`.
    The pseudoentropy README:150 ("up to record-equivalence") is also not a construction.
  - None constructs 5d. Records not searched by that token are outside this negative.

***

## 4. Controls

### 4.1 Classical control

Take `𝔖_F`: a classical reversible computer built from Fredkin exchanges
`(s, a, b) ↦ (s, s ? b : a, s ? a : b)` with a clock register.

| Criterion | Result | Too weak? |
|---|---|---|
| N1, hidden carrier, μ-G | fails (D2 holds for every bijection under μ-G) | no; the failure is target-neutral and shared |
| N1–N4 under MP-0a | passes (heralds, setting-selected routing, ready-meter copies, ledgers) | infrastructure is target-neutral by design and is not used as a quantumness test |
| Qubit tier, configuration identification | fails: no phases on any carrier, no dense control on `Fin 2` (`OB/FrozenSourcing.lean:99`, :327 [K]); compatible reads (`OB/CentralObservation.lean:620` [K]) | no |
| Qubit tier, restricted-access classical models (KS sphere, Spekkens toy, Main's gluing) | passes T-P to T-R | caught by the non-import test |

R-lin is weaker than this control at N2.

One qubit has classical hidden-variable models, so the qubit tier tests *sourcing*, not
quantumness.

### 4.2 Single-qubit target, at (ε, K)

- **T-P:** heralded preparations with reported `p_acc` reproducing `(1 + r·n)/2` within ε on an
  ε-net of the Bloch ball. The net includes a non-stabilizer pure state, e.g. `r = (3/5, 4/5, 0)`,
  and an equal-Z, different-X pair.
- **T-C:** a setting-selected reversible family about two axes at `cos θ = 3/5`, consistent over
  `j ≤ K` applications.
- **T-M:** selectable sharp Z and X reads (Y for spanning), chosen after and independently of the
  preparation, with Lüders repeatability and disturbance.
- **T-R:** complete records with no renormalization; the residual carrier matches the Lüders
  post-state.
- **D:** one fixed `𝔖`, no write outside `φ`, non-import test passed.

| Claimed supply | T-P | T-C | T-M | T-R | D |
|---|---|---|---|---|---|
| Main gluing and single dynamics (Main:564–582) | ε | ε | ε | pass | **fails** (data in the hidden register; realizes non-quantum families) |
| Comb theorem (Main:480) | per menu | no continuum (Main:486) | per menu | pass | **fails** (`u_c` holds the target) |
| Apparatus-1 (R-lin, `q = 2`, P1–P3, E-iso, H-PREP) | stabilizer | no encoded S, no `rot` | Z/X Lüders exact | heralded pass | **fails** (P3, P1, P2, E-iso) |
| MECH-1 (odd `q`) | stabilizer | Clifford via NNB | stabilizer instruments | under posits | **fails** (Theorem T) |
| MECH-2 (G_SM, `q = 2`) | P★ only in a non-CP instrument (R1) | no non-Clifford (U2, R1) | Z/X | — | hypothesis; C-CP fails relative to R1 |
| B1 two-mode drive | points | every angle | the sign read is not quantum | — | **fails** (E-real, E-pair, E-control) |
| KS sphere model | exact | exact | exact | exact | **fails** (all supplied) |
| Operational quotient v3 | stabilizer region | 24 Clifford; error ≥ 1/15 | — | — | supplied region and access |
| TUNE-1 R-lin, R-nl | FAIL-CLASS on subclasses, else INCONCLUSIVE | same | same | same | H-μ, H-write carried |
| `obsTheory` (R4) | readout only | no dense control on `Fin 2` [K]; no phases (any carrier) [K] | passive record reads | external labels (MP-0b) | grants write access |

***

## 5. Earliest failure and the missing premises (qualified form)

R0–R2 never fail; they meet the target only with supplied data. For the posited rule:

1. **N1 comes first in operation order, but only under μ-G.** No hidden carrier is prepared from
   held records (D2). This is target-neutral and classical: a classical computer shares it. Under
   μ-O and μ-R it is open.
2. **N2 is the earliest failure under every measure.** No native setting selection exists under
   any affine rule (D5). This is classical and paper-level: one proof, re-derived twice.
3. **The configuration-identification ceiling is the first kernel-proved failure**, on the parallel
   branch R4. That branch grants more control (write access, MP-0b) and less freedom of
   identification. R3's encoded qubit tier is capped only by frame-relative paper results (U2, NC,
   Proposition C).

**MP-0a (H-LOW; resource; for item 1).**
- *Statement:* fixed known values on designated cells, independent of the setting and of the
  carrier, with the law uniform elsewhere, declared as the joint initial law (Main:58, :97, :602).
- *Physical content:* a past-hypothesis-type supply of ready cells.
- *Why it is not supplied:* under μ-G, D2 rules it out. Main §4.6 supplies only selection.
- *Hard to vary?* No. Any such pattern works, it carries no quantum content, and classical
  computing needs it equally.

**MP-0b (H-MEM; interface convention; for item 1).** The visible history counts as the observer's
record, held outside `V`. It changes what the observer holds, so it is of the same type as MP-2.
R4 grants it.

**MP-1 (M-CTRL; for item 2).**
- *Statement:* the rule contains a setting-selective interaction. The non-translational part of
  `φ^τ|_Σ` depends on `s`; `s` is preserved or recorded and is independent of `Σ` (ledger item
  (xiv)); the timing is sourced.
- *Physical content:* conditional couplings, necessarily **non-affine**.
- *Why it is not supplied:* D5 covers every affine rule, and the affine form is **derived** from
  amplitude-scale gauge invariance (ledger item (vii)). G_SM is a stated hypothesis with the
  scope qualifiers of N2.2. The selected ring sources no Fredkin switch.
- *Hard to vary?* No in bare form: no independent prediction is known (MECH-1, CTRL-REC). Because
  it gives up a derived restriction, adopting it is a **Layer-0 revision under §A.29**. It would
  have to state in advance the results it preserves and deliver an independent prediction.
  Nothing here proposes it.

**MP-2 (for item 3; CONFIRMING).**
- *The structure to replace:* the identification of observer operations with configuration-basis
  matrices (`obsTheory 𝒮 := permTheory 𝒮.Conf`). No rule change lifts it (D6).
- *The open escape:* 5d with M-INACC on an unbounded carrier, credited to MECH-2 §6.2 and mathcon1
  Shape 1, with ARP-1-MARC as the refinement.
- Other routes remain open (§3, R5). Sufficiency, even with MP-0 to MP-2, is open [O].

***

## 6. Status table

| Item | Status | Support |
|---|---|---|
| S⇔D⇔Q_fb | proved | [K] `OB/Equivalence.lean:462` |
| Hidden predictive memory = unstored history | proved in part; partly not formalized | [P/K] Main:97 |
| Comb, gluing, uniform continuum realizations with supplied data | proved on paper with probes | [P] Main:480, :564, :596 |
| No fixed finite carrier reproduces the full qubit | proved, half imported | [P] Main:558 |
| `obsTheory`: no phases and not `DerivedOI` (any carrier); no dense control (`Fin 2` only); rule-independent | proved | [K] `OB/FrozenSourcing.lean:84–327`; `OB/DiscreteCompletion.lean:45` |
| Substratum plus elementary drives gives QM | proved, conditional | [K] `OB/StructuralClosure.lean:414` |
| D1, D3 | derived here | [W] |
| D2 | Main:58 plus invariance; Q-b1 already states it; closes the in-`V` route under μ-G | [P] + [R], ELABORATING |
| N1 under μ-O, μ-R | open | [O] |
| D4 (corrected) | corollary of D2 or stationarity plus Main:147 | [W], ELABORATING |
| D5 (Lemma A; affine class; measure-independent) | one paper proof, re-derived twice | [R] + [W] |
| D6 | derived from kernel statements | [W] on [K] |
| D7 | derived here | [W] |
| N1 under MP-0a/MP-0b; N3 fixed read; N4 under P1, E-iso, MP-0a | conditional | [R]/[W] |
| R-nl at N2; heralded `q = 2` preparation (L5.4); 5d with M-INACC | open | [O] |
| MP-0 to MP-2 jointly sufficient for the qubit target | open | [O] |

***

## 7. §A.31 classification and markers

- **D2: ELABORATING** (of obsmu Q-b1). It closes the in-`V` retention route under μ-G. It is not
  an extension of Q-b1.
- **D4: ELABORATING (r1 said NEW; corrected).** It is a corollary of D2 or stationarity together
  with Main:147. Its premise forces a permutation step and a C1 failure.
- **AW-OA1-1: CONFIRMING.** Statements that condition on `X_{<t}` use history that `V_t` does not
  hold. This restates Main:97 ("in a bijective realization run from time 0 the visible past is a
  function of `(X_t, H_t)`") and obsmu :913–917. Check MP-0b wherever C4 content is called
  observer-accessible.
- **AW-OA1-2:** Main §4.6 replaces only the selection role of the past hypothesis, not its supply
  role. A reading note, not a defect.
- **AW-OA1-3:** under the affine rule class, the first native gap is classical. A statement that
  R-lin lacks quantum control does not imply that it has classical control.
- **D5/N2: CONFIRMING.** **D6: ELABORATING.** **MP-2: CONFIRMING.** **5e Koopman–von Neumann:
  ELABORATING [W].**
- **Pressure tests on favourable branches.**
  - N1 "supplied" is "under a premise", and its native failure is measure-scoped.
  - Apparatus-1's exact Lüders law is MECH-1's countercontrol CC4 with supplied access.
  - 5c's Hadamard is inside a frame-relative Clifford cap.
  - 5e's every-angle drive is imported, and the classical control passes it too.
- **This pass: no NEW findings.** The 3–4-pass fixed-point count starts at one.

***

## 8. Check of the FH→SOURCE-1 trace (#1169 c.6829596317)

| Trace claim | Verdict |
|---|---|
| Equivalence.lean lines; per-`P` carrier; permutation unitary | confirmed |
| Rung 1: Q_fb retained, no gate | confirmed |
| Rung 2: existence for supplied data | confirmed (Main:580, :582) |
| Rung 3: `obsTheory := permTheory`, rule-independent by `rfl` | confirmed (:770, :780). The cause is maximality (D6). "First exact" omits the classical gap at R3/N2 and R4's added write access |
| Rung 4: FrozenSourcing ceilings, `substratumGen_not_control`, `rot_not_monomial` | confirmed (FrozenSourcing :295, :318; StructuralClosure :348; SubstratumInterface :155). Dense control on `Fin 2` only |
| Monomial class allows diagonal phases by stipulation | confirmed (`OB/StructuralClosure.lean:333`) |
| Rung 5: `DrivesElementary`, `QuantumArchitecture`, `substratum_plus_control_qm` | confirmed (`OB/SubstratumSource.lean:77`, :86; `OB/StructuralClosure.lean:414`). Conditional sufficiency, which imports continuous flows and phases |
| §D3: a rule-sensitive source map (B) as the ablation | **settled by D6 for configuration-level, bijection-generated source maps.** The trace's own §C allows a source map that is changed or replaced; that route is untouched |
| Verdict: the first proved loss is at the interface ceiling | qualified: it is the first kernel-proved loss, on a parallel branch. The measure-robust paper loss at R3/N2 is classical |

***

## 9. Reading inventory

**Read** (`main@fb733b4a`):
- `papers/Main.md`: :1–110, :129–150, :429–612, :644, :740–760, ledger :724 by extract.
- Lean: the statements and ranges listed in r1, plus `OB/DiscreteCompletion.lean:40–50`.
- Records:
  - apparatus-1 :1–120, :275–430, :506–512;
  - MECH-1 :1–137, :797–900, :938–1060;
  - MECH-2 :1–140;
  - CP-PREP-1 (in full);
  - physical-controller LEAD :1–50;
  - minacc-1 RESULT :1–70;
  - mathcon1 DESIGN :578–592;
  - ARP-1-MARC result :1–45;
  - obsmu ANALYSIS :1–40, :228–240, :520–575, :885–960;
  - KS model REPORT :1–60;
  - op-quotient v3 and whole-model-bridge (by grep);
  - two-mode-drive :1–40;
  - pseudoentropy review :455–475 and README :148–151.
- TUNE-1: Step 1 :1–80, :148–315; Proposal :1–230; Session 3 :1–100, :314–400; Session 4 :1–82,
  :553–630.
- GitHub: the #1169 body and its last seven comments.
- `REVIEW-OA-1.md`.

**Not read:**
- earlier #1169 comments; #866, #914, #1143, #1236, PR #1237;
- other TUNE-1 files;
- SM, Substratum, GR and Structure;
- Main §2.3–§3.3 bodies (except :129–150);
- Q-A, feedback, record-control;
- the rest of mathcon1 and ARP-1-MARC;
- the three foundations and operational audits.

Negative claims are limited to these sources and the stated grep.

***

## 10. Limits

- [W] items are reviewed once, by a same-family model, and are not kernel-checked.
- R3 verdicts are for R-lin. N2 covers the gauge-derived affine class. N2 for general bijections
  is possible in principle; R-nl is open.
- D2 is scoped to μ-G. Under μ-O and μ-R, N1's native verdict is open. Neither of those measures is
  H-LOW (r1 §10 said otherwise; corrected).
- D4 is scoped to full-history records under a stationary law.
- The qubit tier tests sourcing, not quantumness. Composite systems, Bell and the Born exponent are
  untouched.
- No candidate was constructed. 5d with M-INACC is named, and its realizability and sufficiency are
  open.
- No manuscript claim is affected. AW-OA1-2 is a reading note.

***

## 11. Changes from r1 (finding → change)

| Review finding | Change in r2 | Verdict moved? |
|---|---|---|
| 1 (C1-a) | D2 scoped to μ-G; μ-O and μ-R added as an open branch (N1.1b); "for every φ" qualified (§0.3, N1.1a, MP-0a, §5); r1's §10 "exactly what H-LOW supplies" removed | **N1 native failure: from unqualified to μ-G only; open under μ-O, μ-R** |
| 1 (C1-b) | "no **hidden** carrier"; visible carriers prepared at the D3 cost | N1 verdict narrowed to hidden carriers |
| 1 (C1-c) | D2 = Main:58 plus invariance; no longer called an extension of Q-b1; its contribution is closing obsmu's in-`V` route under μ-G | novelty reduced |
| 2 | MP-0 split into MP-0a (H-LOW, admissible target-neutral form; Main:58, :97, :602) and MP-0b (H-MEM, interface convention, granted by R4) | MP-0 retyped |
| 3 | D5 covers every affine rule (ledger (vii) derives the affine form); N2 measure-independent; "three times" → one proof re-derived twice; "reviewed" = ChatGPT review; G_SM `L ≥ 5` and R1-relative; D7 citation → apparatus-1:510 | **N2 strengthened to the gauge-derived affine class and every measure; MP-1 marked as a Layer-0 revision under §A.29** |
| 4 | "need not be a literal sub-theory" removed; ceiling via sub-theory and :84; dense control `Fin 2` only (DiscreteCompletion:45); R3 and R4 parallel | R4 failure placed on a parallel branch |
| 5 | MP-2 CONFIRMING, credited to MECH-2 §6.2, mathcon1:585 and ARP-1-MARC; "smallest" → "escape left open by … within their hypotheses"; other routes listed; non-import by definition; search scope stated | MP-2 reclassified, novelty withdrawn |
| 6 | 5c: "reachable by CP operations, relative to the frame", with sources, and NC conditional on spanning reads; op-quotient v3 also under 5d's supplied restrictions; 5e: KvN shows non-discrimination, import rests on E-real, E-pair, E-control and the kernel lift facts | 5c qubit cell narrowed; 5e rationale corrected, verdict unchanged |
| 7 | D4 reclassified ELABORATING and corrected (permutation step, C1 failure, Main:147), in §0.7, R1, N4, §7 and §6; AW-OA1-1 CONFIRMING | **NEW → none; tally: no NEW findings** |
| 8 | §8 row: "settled by D6 for configuration-level, bijection-generated source maps" | softened |
| ordering | §5 restated in the review's qualified three-point form | earliest-failure answer qualified |
