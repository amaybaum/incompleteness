# #868 Bell-scope unit 1: native Bell factorization, its proved class, and the line between OI and an interface

**WIP / UNVERIFIED, paper-only writer draft r1, pending independent review; authorizes nothing.**

- **Accountable home:** #868. Coordination #1169. Cross-references #1060 (H-Bell, frozen record untouched),
  #1210 (QX-6, frozen r7c untouched), #914 row 16, #866, #1216.
- **Authorization:** contract #868 c.6791565399 (owner account, 2026-11-11T08:56:50Z); coordination #1169
  c.6791556736 (08:56:22Z); writer assignment #868 c.6791606126 (08:59:01Z), quoting the owner's answer "Confirm:
  Claude writes (Recommended)": "Paper-only writer unit under #868 following that contract (paths A obstruction / B
  escape / C indeterminate). No OI-mechanism computation, no new premise, no runs." ChatGPT is the independent
  reviewer.
- **Done in this unit:** source reading, hand proofs, and one probe file of exact checks on generic mathematical
  objects (§3.6). No OI rule, carrier, coupling, preparation, ring or simulator is encoded or run. No Lean run, git
  write, push or GitHub write. No frozen record or manuscript was edited.
- **Corpus pin:** `main` = `cac5d26441dd33e9348151487e4df7b547195481` (2026-11-09 16:04 +0200), which equals
  `origin/main` when read. Every `main` citation below is `git show cac5d264:<path>`. Line numbers `Main:N` are
  lines of `papers/Main.md` at that commit (blob `5b73da57…`).

**Evidence-layer tags.** **K** kernel; **P** paper proof on `main`; **W** research record on `main`, model-reviewed
(an author-posted or model acceptance is not verification, §A.46 item 7); **D** draft off `main`; **A** derivation
in this file, unreviewed; **X** exact generic check in this unit's probe (computation-supported only, not a proof);
**L** literature, recalled or abstract-level (none read first-hand in this unit).

***

## 0. Verdict and scope

**Verdict for OI itself: (C) INDETERMINATE.** The sources neither prove that every intervention/observer interface
admissible under Main's posits and the substratum dynamics is Bell-factorizable, nor exhibit a native operation that
violates factorization. Neither an unconditional obstruction nor a native Bell escape is established.

**Verdict for a stated interface class: (A) obstruction, restricted.** For the *closed native screened class*
𝒞_sep of §3.1 — one fixed deterministic map, site factorization, setting generators inside the system, every
record region of each wing outside the actual coupling-graph cone of the other wing's generator for the whole record
window, generator isolation, every-run outputs with failures mapped by a fixed local rule, and measurement
independence (posited as in Main, or obtained under the conditioning-factorization condition of Lemma G) — there is
a single pre-setting, response-complete λ with one setting-independent μ(λ) that factorizes **for the whole finite
setting menu at once**, including complete local histories, heralds, controller records and continuations inside
the window (Theorem N, [A] on Main's cone lemma [P]). Hence CHSH ≤ 2 and, against the four Tsirelson contexts,
mean (so also worst-setting) joint-output TV error ε ≥ (√2−1)/4 ≈ 0.1036, also when the error is measured on full
histories (§4). **This is an interface-scoped result, not a no-go for OI.** It is labelled restricted: it covers
only wings separated beyond the actual coupling-graph cone.

**Where the line between the two lies, and the open posits it depends on (§3.4).**
- **O1 — the actual coupling graph.** Main defines `G_φ` by one-step dependence "for some state" (Main:364). Main's
  adopted Bell branch (Main §3.3(a)) and H-Bell (Substratum:131–133) need preparation-indexed long edges, which, by
  that definition, are edges of `G_φ`. Ledger posit (x) states "the coupling graph is the simple-cubic graph"
  (Main:726) without restricting it to the reference class. Read globally, (x) excludes the long edges and puts
  every graph-separated protocol in 𝒞_sep's geometry; read as SM §3.1's reference-class constraint (SM:108), it
  leaves H-Bell (i) open. The text does not settle which reading holds (finding F1).
- **O2 — the physical light cone.** Main states that which of the graph cone (Euclidean reach `1/‖n̂‖₁` per update,
  from 1 to 1/√3) and the long-wavelength wave speed (1/√3) is the physical *c* "is not derived" (Main:416). If
  *c* is the wave speed, wings that are spacelike in physical terms can still lie inside the graph cone, by a factor
  up to √3 off the body diagonals, even on the nearest-neighbour graph. Such protocols are outside 𝒞_sep; whether
  the native rule yields Bell-relevant dependence there is unexamined.
- **O3 — measurement independence.** It is hypothesis (iv) of Main's theorem, "retained as a posit about the
  initial condition, not derived" (Main:406–407). It is **not** ledger item (iv) (the maximal-entropy measure
  selection) and is not separately itemized in the ledger (finding F2). Lemma G reduces it, under the uniform
  counting measure, to a condition on the conditioning events (CF) and generator isolation; CF is unsourced for an
  observer's actual record conditioning.

**Decisive missing lemma (C).** *Native Bell-availability lemma (NBA):* every Bell protocol admissible under Main's
posits and the substratum dynamics whose wings are separated in the physical sense satisfies (Sep) in the actual
`G_φ` for its generator and record regions, and its response-complete pre-setting variable satisfies (MI). NBA
would give (A) for OI; its failure through a sourced native coupling with complete-history no-signalling would give
(B). NBA requires O1 and O2 to be resolved and O3 to be sourced or posited explicitly (§3.4).

**Escape (B): not established.** No native operation, coupling or preparation violating factorization is supplied
by the sources. Main's PR realization is the abstract finite response construction with globally coupled
setting-dependent hidden dynamics (Main:362) — a negative control, excluded by the contract. The shared-parity
candidate (`two-system-interface.md`, W) is built from explicit abstract apparatus assumptions with a cross-wing
controlled interaction, is "not a compiled extension" of a native rule, and its record reports reuse signalling.
If an escape exists while (MI) and every-run outputs are kept, the Bell hypothesis that fails is **parameter
independence** (§2): outcome independence is automatic under determinism, and the pre-setting λ always exists.

**Favourable-reading check (§A.31).** Theorem N and Lemma G favour an obstruction. Their pressure test is in §3.5:
neither reaches OI itself, because Sep, GI and CF are hypotheses about a protocol, not consequences of the posits.

***

## 1. Claim / scope table

Status: *proved* (layer), *conditional* (named hypotheses, each justified / posited / open), *open*, *not established*.

| # | Statement | Protocol class | Hypotheses (status) | Layer | Source | On `main`? |
|---|---|---|---|---|---|---|
| C1 | Cone lemma: `(φ^k(s))_i` depends only on `B_{G_φ}(i,k)` | any finite site-factorized deterministic map | finite `V`, `S=∏S_i` (ledger (ii), (viii): posited) | P | Main:364 | yes |
| C2 | Bell ceiling for a screened local completion, CHSH ≤ 2 | exogenous one-step own-wing interventions, readouts outside the other wing's cone, every-run ±1, common ensemble | (i) determinism (justified: Lemma 3, ledger (iii) part-empirical); (ii)–(iii) protocol design (posited per protocol); (iv) MI (posited) | P (+ exhaustive check 11) | Main:366–393 | yes |
| C3 | **Theorem N:** closed native form of C2 with generators inside the system; one λ = Ω for the whole finite menu and complete local histories | 𝒞_sep (§3.1) | D, (ii), (viii) (posited); Sep, GI, ⊥-rule (protocol design, posited per protocol); MI (posited, or Lemma G) | A on C1 | §3.2 here | no (this file) |
| C4 | **Lemma G:** under the uniform counting measure conditioned on an event that factorizes across generator / non-generator coordinates at the setting slice, MI holds for Ω | 𝒞_sep with measure semantics M | M (ledger (iv) with Lemma 3's uniform-prior scope: posited); CF (open, unsourced); GI | A (+X G6) | §3.3 here | no |
| C5 | CHSH-variant pointwise identity over the 16 deterministic tables | generic | none | X (G1); standard (L) | probe | no |
| C6 | ε ≥ (√2−1)/4 for mean and worst-setting TV to the Tsirelson box, any MI Bell-local family; tight | generic Bell-local families | Bell locality + MI | A (+X G2–G4) | §4 | no |
| C7 | Full-history contraction: TV on full histories ≥ TV on extracted outputs | any local extractor applied to both laws | same extractor on both; target pushes forward to the Tsirelson box | A (+X G5) | §4.2 | no |
| C8 | MI-relaxed ceiling `S ≤ min{4, 2+4√(2 ln2 I_ont)}`, hence ε ≥ (2√2−2−4√(2ln2·I_ont))/8 when positive | response-complete Ω with setting dependence | response-completeness (Main:427) | P (bound, not re-proved here); A (corollary) | Main:418–425; §4.3 | bound yes |
| C9 | Complete-history no-signalling over a preparation family with full affine span forces pointwise locality, so CHSH ≤ 2 | fixed deterministic realization, fixed policy menu | (S) full span (unsourced); every-run binary first outputs | W | prepared-pair-source §§4–5 | yes |
| C10 | Bare finite OI representability realizes PR behaviour | unrestricted global coupling | none | P (construction) | Main:362, :429 | yes |
| C11 | Native Bell escape (B) | any native preparation/operation | needs O1 or O2 positively, complete-history NS for a sourced preparation family | **not established** | — | — |
| C12 | NBA: every admissible physically-separated protocol is in 𝒞_sep | OI itself | O1, O2, O3 | **open** | §3.4 | — |
| C13 | Reference nearest-neighbour graph alone cannot give option (a) for graph-separated wings | nearest-neighbour cubic, graph-separated | C2's hypotheses | P | Main:416 (Corollary) | yes |

***

## 2. Bell hypotheses mapped to OI objects

Fix a finite setting menu `X × Y`, every pair jointly admissible (positive probability). Write `x_t` for the
substratum configuration at tick `t` and `t_s` for the setting slice.

| Bell hypothesis | OI object | Status in the sources |
|---|---|---|
| **Pre-setting λ exists** | `x_{t_s}` itself, or a coarse-graining Ω of it. Determinism (Main Lemma 3) makes every later record a function of `x_{t_s}`. | Always available. No retrocausal or future-input escape inside a deterministic one-way map: a pre-setting variable fixing all responses exists (L: Wharton–Argaman classify such escapes as MI failures). |
| **Response-completeness** | Ω must fix each wing's complete record for every setting value. `x_{t_s}` is complete; a coarse Ω is complete only if responses depend on discarded coordinates only through the settings (GI, §3.1). | Main: Ω "fixes each wing's response to every setting" (hypothesis of C2); Main:427 requires it for the information bound. |
| **Outcome independence** | At fixed `x_{t_s}` and settings, every record is a point mass. | Automatic under determinism. Not an escape route. |
| **Parameter independence (PI)** | Wing A's record window `{R_A^t}` lies outside the `G_φ`-cone of the B-generator region `G_B` (Sep). Exogenous form: Main's (ii)+(iii). | Proved from Sep via C1. Sep is a protocol property. Its failure by a `G_φ` path is Main's adopted branch (a): preparation-indexed long edges (H-Bell (i), open) or within-cone dependence (O2). |
| **Measurement / setting independence (MI)** | `p(Ω \| a,b) = p(Ω)`. The settings are functions of `x_{t_s}|_{G_A}, x_{t_s}|_{G_B}`; for the full microstate MI fails whenever two setting pairs occur (Main:406–410). | Posited (Main:406–407). Lemma G: implied by CF + GI under the uniform measure. Main records the MI-dependent alternative with `I_ont ≥ 0.0309` bits and does not adopt it. |
| **Every-run outputs** | Each run records an output; a failure `⊥` is a record, mapped by a fixed local rule (`⊥ ↦ +1`). Heralds before `t_s` are part of Ω; heralds after `t_s` are local records. | Main's C2 assumes every-run ±1. Coincidence-only (postselected) statistics are outside every result here. |
| **Operational no-signalling** | Each wing's complete accessible history law is independent of the remote policy (prepared-pair-source §4, balance equations (B)). | A separate, weaker property: PR satisfies it with CHSH 4 (composition-source-map §5.2, W). Not Bell locality. |
| **Determinism** | Main Lemma 3; ledger (iii). | Neither proves nor refutes factorization: C10 (PR realizable) and C2 (ceiling) both hold for deterministic maps. |

***

## 3. Proof, missing lemma, and pressure test

### 3.1 The closed native screened class 𝒞_sep

Main's C2 models a setting as an exogenous map `u^A_a × u^B_b × id`. In a closed deterministic universe there is no
exogenous map: the setting is carried by part of the state. 𝒞_sep restates the protocol without one.

- **(D)** One deterministic map `φ : S → S` for every run and every setting value. Bijectivity is not used.
- **(F)** `S = ∏_{i∈V} S_i`, `V` and each `S_i` finite (ledger (ii), (viii)). `G_φ` is Main's coupling graph
  (Main:364), read from the actual `φ`, state-dependent edges included.
- **(Gen)** Disjoint generator regions `G_A, G_B ⊂ V`; the settings are `a = g_A(x_{t_s}|_{G_A})`,
  `b = g_B(x_{t_s}|_{G_B})`. A generator that acts over several ticks is handled by taking `t_s` as its first tick
  and `G_A` as the region whose content then fixes the setting. Put `W = V ∖ (G_A ∪ G_B)` and
  `Ω = x_{t_s}|_W`.
- **(Rec)** Wing A's complete record is `h_A = H_A( (x_t|_{R_A^t})_{t_s ≤ t ≤ T_A} )` for regions `R_A^t`. It
  includes the outcome, heralds, failure flags, controller and preparer information that reaches A, timing, and
  any continuation records in the window. The output is `o_A = π_A(h_A) ∈ {±1}`, with any failure mapped by a fixed
  local rule. Symmetrically for B.
- **(Sep)** For every `t ∈ [t_s, T_A]`: `d_{G_φ}(G_B, R_A^t) > t − t_s`. Symmetrically for B.
- **(GI) generator isolation.** Each `x_t|_{R_A^t}` depends on `x_{t_s}|_{G_A}` only through `a`: if `x, x'` agree
  outside `G_A` and `g_A(x|_{G_A}) = g_A(x'|_{G_A})`, they give the same A-record. Symmetrically for B.
- **(MI)** `p(Ω | a,b) = p(Ω)` for every jointly admissible `(a,b)` — posited, as in Main, or via Lemma G.

(D), (F) are posits of the framework. (Gen), (Rec), (Sep), (GI) and the ⊥-rule are properties of a protocol: they
define the class and are not derived from OI.

### 3.2 Theorem N (closed native screened ceiling) [A, on C1]

*Under (D), (F), (Gen), (Rec), (Sep), (GI) there are functions `Ĥ_A(Ω,a)`, `Ĥ_B(Ω,b)` with `h_A = Ĥ_A(Ω,a)`,
`h_B = Ĥ_B(Ω,b)` for every run. If also (MI), then for every jointly admissible `(a,b)` in the whole menu*
`P(h_A, h_B | a, b) = Σ_Ω p(Ω) 1[h_A = Ĥ_A(Ω,a)] 1[h_B = Ĥ_B(Ω,b)]`,
*so the complete local histories, and every local function of them, are Bell-local with one λ = Ω and one
setting-independent μ. For binary outputs and any two settings per side, `|S_CHSH| ≤ 2`.*

*Proof.*
1. *Parameter independence.* Fix `t ∈ [t_s, T_A]`. By C1 applied to `φ^{t−t_s}`, `x_t|_{R_A^t}` depends only on
   `x_{t_s}` restricted to `B_{G_φ}(R_A^t, t−t_s)`. By (Sep) that ball is disjoint from `G_B`. So `h_A` does not
   depend on `x_{t_s}|_{G_B}`.
2. *Response-completeness.* By (GI), `h_A` depends on `x_{t_s}|_{G_A}` only through `a`. With step 1, `h_A` is a
   function of `(x_{t_s}|_W, a) = (Ω, a)`; call it `Ĥ_A`. Symmetrically `h_B = Ĥ_B(Ω, b)`. This holds for every
   `x_{t_s}`, so conditional on `(Ω, a, b)` both records are point masses whatever the law of the generator
   residues.
3. *Mixture.* `P(h_A,h_B | a,b) = Σ_Ω p(Ω|a,b) 1[·]1[·]`; (MI) replaces `p(Ω|a,b)` by `p(Ω)`. The same Ω and μ
   serve every pair in the menu, not each 2×2 sub-menu separately.
4. *CHSH.* For outputs `q_x(Ω) = π_A(Ĥ_A(Ω,x))`, `r_y(Ω) = π_B(Ĥ_B(Ω,y))` in `{±1}`, pointwise
   `q_0(r_0+r_1) + q_1(r_0−r_1) ∈ {−2, 2}` (X: G1 checks all eight CHSH functionals over the 16 tables). Average. ∎

*Relation to Main's theorem.* Main's C2 is the exogenous case. Theorem N removes the exogenous map: the setting
enters as generator content, Sep is measured from `G_B` rather than from an intervention region, and the records
are the whole local history window rather than one readout. A parallel derivation for time-dependent local maps,
A6.1 in #1210's frozen QX-6 r7c (D, off `main`), is provenance only; Theorem N does not use it.

*Remark (generator residue).* Without (GI), enlarge Ω to `(x|_W, ρ_A, ρ_B)`, where `x|_{G_A} ↔ (a, ρ_A)` is any
chart. Steps 1–4 go through, and (MI) then also requires the residues to be independent of the setting values.
This is the setting-generator accounting the contract asks for: MI concerns the response-relevant variable, which
includes whatever part of the generator reaches a record.

### 3.3 Lemma G (setting-generator accounting under the uniform measure) [A; X G6]

*Measure semantics (M), posited:* the run law of `x_{t_s}` is the uniform counting measure on `S` conditioned on an
event `E` of positive measure (ledger (iv) in Lemma 3's uniform-prior scope; an event at an earlier tick transports
to `t_s` through the bijection `φ` without changing the counting measure).

*(CF) conditioning factorization:* with `S = S_G × S_W`, `G = G_A ∪ G_B`, the transported event is a product
`E = E_G × E_W`.

*Lemma G.* *Under (M) and (CF), `x_{t_s}|_G` and `x_{t_s}|_W` are independent. Hence `(a, b)` is independent of
`Ω = x_{t_s}|_W`, and (MI) holds. With (GI) failing, (MI) for the enlarged Ω of §3.2 holds when, in addition, the
conditioned law on each `S_{G_A}` makes `a` independent of `ρ_A`.*

*Proof.* The uniform law on a product set is the product of the uniform laws on its factors. ∎ (X: G6a; the
countercontrol G6b shows a coupling event breaks independence.)

*What Lemma G does and does not give.* It replaces a posit about an ensemble by a checkable condition on what is
conditioned on. It does not source CF. Under (M) a single time slice carries no correlation at all; every
generator–response correlation enters through conditioning on events whose transported dependence sets meet both
`G` and `W`. An observer's actual conditioning — the visible history, the preparation and heralding record, earlier
runs' records — is a long history whose transported dependence sets generically meet both. Whether it factorizes
across generators and sources in a physical Bell test is open. Main's MI-dependent bound (C8) quantifies the cost of
its failure.

### 3.4 The missing lemma for OI itself

*NBA (native Bell-availability).* For every Bell protocol admissible under Main's posits (i)–(xiii) and the
substratum dynamics whose wings are separated in the physical sense: (Sep) holds in the actual `G_φ` for its
generator and record regions, and its response-complete pre-setting variable satisfies (MI).

NBA ⇒ (A) for OI on physically separated protocols, by Theorem N and §4. Each of its parts is open:

- **O1 (long edges vs ledger (x)).** A preparation-indexed long edge between the wings is, under Main's
  "for some state" definition (Main:364), an edge of `G_φ`; so is a path wing–mode–wing through a shared
  non-localized hidden mode, such as Book §18.4's candidate boundary modes (`book/ch18-beyond.md`:104, a candidate
  "not an established Bell mechanism"). Either breaks (Sep) at graph distance ≤ 2. SM §3.1 restricts local
  graph-dependence to "the reference vacuum/uniform state class" and allows "additional bounded-degree,
  preparation-indexed edges" in prepared states (SM:108–110). Ledger (x) states the simple-cubic coupling graph with
  no such restriction (Main:726). Under (x) read globally, H-Bell (i) is excluded and graph-separated protocols meet
  (Sep). Under (x) read as the reference-class constraint, H-Bell (i) is open (Substratum:133).
- **O2 (physical c).** The nearest-neighbour graph cone reaches `1/‖n̂‖₁` per update, from 1 along the axes to
  1/√3 along the body diagonals; the wave speed is 1/√3 in every direction; which is *c* "is not derived"
  (Main:416). With *c* the wave speed, the ratio cone/light is `√3/‖n̂‖₁ ∈ [1, √3]`, so physically spacelike
  wings lie inside the graph cone except along the body diagonals. Main's Corollary already excludes "wings
  separated by less than the graph cone" (Main:416). Whether the native rule produces setting dependence in that
  region, and whether it violates CHSH with complete-history no-signalling, needs computation on the native rule,
  which this unit is not authorized to do.
- **O3 (MI).** Posited in Main; reduced by Lemma G to (M) + (CF) + (GI); CF unsourced.

*The missing lemma for (B).* A sourced native operation, coupling or preparation — not chosen to fit a Bell table —
with a `G_φ` path inside the run (O1) or within-cone dependence (O2), giving CHSH > 2 under (MI) and every-run
outputs, together with complete-history no-signalling for a sourced preparation family. By C9 (W), that family
cannot have full affine span over the response-complete states: it must be restricted, and the restriction needs
a reason independent of no-signalling and of agreement with QM (§6). The failed Bell hypothesis would then be
parameter independence.

*Preserved conditional result.* Main's C2 (P) and Theorem N (A) stand at their stated scopes; neither is weakened
by this indeterminate verdict.

### 3.5 Pressure test of the favourable reading (§A.31)

Theorem N and Lemma G favour the obstruction. Checks against over-reading:

1. *Is 𝒞_sep native OI?* No. (Sep), (GI), the ⊥-rule and (CF) are design or conditioning properties. The
   theorem is native in form (no exogenous map) but not in coverage.
2. *Does the cone lemma use only posits?* It uses (F) and the definition of `G_φ`. The cone is the cone of the
   *actual* map, including every state-dependent edge. A protocol cannot be shown to meet (Sep) without knowing
   `G_φ` near the experiment, which is O1.
3. *Does Lemma G derive MI?* No. It shows MI is equivalent, under (M) and (GI), to a factorization of the
   conditioning; that condition is not derived. Under (M) the reliability of records itself needs conditioning on
   past events, which is exactly what threatens CF.
4. *Could the TV bound be evaded inside 𝒞_sep?* Only by changing a hypothesis: postselection (coincidence-only
   counts), dropping a record from the full mass, or setting-dependent heralds after `t_s` that remove runs. The
   ⊥-rule and full-mass accounting exclude these.
5. *Does the multi-run trajectory matter?* For run `n`, Ω_n includes the records of earlier runs. Theorem N applies
   per run when the run-`n` settings satisfy (MI) given Ω_n — fresh generators. The two-sided memory effect
   (L: Barrett–Collins–Hardy–Kent–Popescu 2002) concerns estimators, not this per-run law.
6. *Is the LIT-SURVEY synthesis "V-L under posits" right?* Only at interface scope: it presumes a local rule and
   physical separation equal to graph separation. O1 and O2 show the posits do not fix either (§7 note).

### 3.6 Generic probe

`bell868/probes/generic_bell_checks.py` (sha256 `a6cf97c8b68a3fe929cab03dab3f1b5dbac2d60d3bcdb22a77e9e08c8f8b71ed`),
run with `python3 -I`, exit 0, all twelve checks PASS. It encodes no OI object. G1: the eight CHSH functionals over
the 16 deterministic tables take values ±2. G2: the Tsirelson box is a family of probability laws with CHSH 2√2
(the ceiling is not vacuous). G3: an explicit local witness — the uniform mixture of the 8 deterministic tables with
S = +2 — has correlators (½, ½, ½, −½), equals the isotropic mixture at v = 1/√2, and has TV (√2−1)/4 to the
Tsirelson box in every context, exactly. G4: `|E_P − E_Q| ≤ 2 TV` on a rational grid. G5: TV contraction under the
local map `⊥ ↦ +1` on 400 exact rational cases. G6: independence under a product conditioning event, and its failure
under a coupling event (countercontrol). These checks support the proofs; they do not replace them.

***

## 4. The ε bound and its scope

### 4.1 Statement and proof [A; X G2–G4]

Let `P_Q(a,b|x,y) = (1 + ab·c_{xy}/√2)/4`, `a,b ∈ {±1}`, `c_{xy} = −1` iff `x = y = 1`. Its correlators are
`E^Q_{xy} = c_{xy}/√2`, so `S_Q = E_00 + E_01 + E_10 − E_11 = 2√2`. Let `P_L` be any MI Bell-local family on the
same four contexts and `ε_{xy} = TV(P_L(·|xy), P_Q(·|xy))`.

*Claim.* `(1/4)Σ_{xy} ε_{xy} ≥ (√2−1)/4`; hence `max_{xy} ε_{xy} ≥ (√2−1)/4`. Equivalently, `2√2 − 2 ≤ 8ε` for the
worst-setting ε (and for the mean).

*Proof.* `|E^L_{xy} − E^Q_{xy}| = |Σ_{ab} ab (P_L − P_Q)| ≤ Σ_{ab}|P_L − P_Q| = 2ε_{xy}`. So
`2√2 − S_L ≤ |S_Q − S_L| ≤ Σ_{xy} 2ε_{xy}`. With `S_L ≤ 2`, `Σ ε_{xy} ≥ √2 − 1`. ∎

*Tightness.* The local witness G3 attains `ε_{xy} = (√2−1)/4` in every context (exact). The bound is optimal for
both the mean and the worst setting.

*General target.* For a quantum target with CHSH value `S_Q > 2`: `ε ≥ (S_Q − 2)/8`.

### 4.2 Full-history marginal contraction [A; X G5]

Suppose the error is measured on full joint histories, `ε^hist = max_{xy} TV(P_L(h_A,h_B|xy), P_Q(h_A,h_B|xy))`,
and the outputs are extracted by one product map `f = π_A × π_B` applied to both laws, with the target's pushforward
equal to `P_Q` (a target that never emits ⊥ is unchanged by the ⊥-rule). Then for every `(x,y)`

`TV(f_# P_L, f_# P_Q) ≤ TV(P_L, P_Q)`,

because for each output set `U`, `|P_L(f^{-1}U) − P_Q(f^{-1}U)| ≤ TV(P_L, P_Q)`. Under Theorem N, `f_# P_L` is MI
Bell-local (step 3 applies to local functions of the histories). So `ε^hist ≥ ε^out ≥ (√2−1)/4`. A failure symbol
in the raw alphabet only adds mass to the TV.

### 4.3 MI-relaxed corollary [A on Main's bound, P]

If (MI) fails with `I_ont = I(Ω; Z)` bits, Z uniform on the four pairs and Ω response-complete, Main's boxed bound
(Main:418–425, not re-proved here) gives `S_L ≤ 2 + 4√(2 ln 2 · I_ont)`, so
`ε ≥ (2√2 − 2 − 4√(2 ln 2 · I_ont))/8` whenever the right side is positive, i.e. `I_ont < (3−2√2)/(8 ln 2)`.

### 4.4 Scope

- The bound forbids **arbitrarily small uniform error** for the Tsirelson CHSH target by any member of 𝒞_sep (or any
  MI Bell-local family). It does not forbid finite-precision reproduction of Bell-local quantum fragments, nor exact
  reproduction of a quantum table with CHSH ≤ 2.
- It does not cover coincidence-only statistics, setting-dependent postselection, or wings inside each other's
  `G_φ`-cone.
- It applies to OI itself only through NBA (§3.4).
- Exact `2√2` is in any case unreachable by rational laws; the bound is about approach, not attainment.

***

## 5. Consequences for #1216 Level B and #1169

**#1216 Level A (one fixed experiment within ε).** Main's abstract states that, for fixed dimension, instrument
menu, horizon and accuracy ε, one finite OI construction reproduces the quantum experimental envelope (Main:22).
By §4 any construction within ε < (√2−1)/4 of the Tsirelson box on a two-wing CHSH experiment is **outside
𝒞_sep**: it has a `G_φ` path from a generator to a remote record inside the window, or fails (GI), (MI), or every-run
accounting. This is consistent with Main (C10), but it means such a Level-A realization is not a native spatial
realization of separated wings unless O1 or O2 is resolved positively.

**#1216 Level B (one reusable mechanism, uniform over a class with composition).**
1. If the mechanism's separated two-wing composites lie in 𝒞_sep, Level B fails for any class containing the
   separated CHSH Tsirelson experiment: the uniform error is at least (√2−1)/4, mean and worst-setting, full
   histories included (§4). [A, conditional on 𝒞_sep membership]
2. A Level-B mechanism that keeps (MI), every-run outputs and complete-history no-signalling, and admits a preparation
   family whose affine span is the whole simplex over its response-complete states, is pointwise local by C9 (W),
   hence also fails at (√2−1)/4. So Level B with Bell coverage requires a **restricted preparation class** with an
   independent reason (§6, P-c). [A on W]
3. Hence #1216's accepted approximation mathematics stays at its proved scope; Level B is not promoted without NBA's
   negation through a sourced native route, as #1169 c.6791556736 already requires.

**#1169 (exact equivalence).** The finite-law equivalence `S ⇔ D ⇔ Q_fb` (Main §3.4) is untouched: it is a
global-law representation, and Bell selection is a spatial-composite question (Main:362, :698). Gate A's endpoint
includes composites and ancillas, so exact operational equivalence with separated composites needs C11 — a native
escape with complete-history no-signalling — which is not established. This is an open dependency, not a no-go for
#1169: OI's verdict is (C).

***

## 6. §A.29 disposition of candidate principles (none adopted)

| Candidate | What it would do | §A.29 check | Disposition |
|---|---|---|---|
| **P-a.** Ledger (x) read globally ("no long edge in `G_φ`") | puts graph-separated protocols in 𝒞_sep's geometry; with NBA's other parts, obstruction for those | preserves SM's local derivations; its independent consequence is CHSH ≤ 2 for graph-separated wings under MI, a raw-direct confrontation with loophole-free Bell tests whose force depends on O2 | not adopted; contradicts Main §3.3(a)'s adopted branch; owner reading of (x) needed (F1) |
| **P-b.** Preparation-indexed long edges (H-Bell) | ontic PI across wings | existing open hypothesis (Substratum:133), not new; still needs no-signalling for a sourced preparation family and a consequence beyond the Bell table (curvature stability is a required compatibility, not a prediction) | not adopted; remains open; not evaluated |
| **P-c.** Restricted preparation class masking cross-wing response (R6.9-type) | complete-history NS with PI failure | defined by the balance equations it is fitted (C9; QX-6 A6.4, D); creditable only with an independent reason and an own consequence (e.g. signalling of non-equilibrium preparations, as in de Broglie–Bohm — L) | rejected as fitted; open only with an independent reason |
| **P-d.** CF as a principle (MI from conditioning factorization) | derives MI under (M) | would need a reason why an observer's conditioning factorizes across generators and sources; none supplied | not adopted; Lemma G is a reduction, not a principle |
| **P-e.** Measurement dependence (Main option (b)) | MI failure with `I_ont ≥ 0.0309` bits | recorded by Main, not adopted; Hall–Branciard benchmark ≈ 0.080 bits (causal) (Main:418–425) | not adopted |
| **P-f.** Within-cone super-wave dependence (O2) as a Bell route | PI failure on the nearest-neighbour rule where cone exceeds the wave speed | would need *c* = wave speed (not derived), a native response violating CHSH with complete-history NS, and preserved dispersion/isotropy controls; its shape is falsifiable — violation only within the graph cone, which is direction-dependent | candidate raised here; not adopted, not evaluated (needs OI-mechanism computation, not authorized) |

***

## 7. §A.42 item 8 reference table

Each reference is classified by what the claim it is attached to uses. Nothing in this file lands; if it ever does,
the gaps marked here must close first.

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md` @ cac5d264 (blob `5b73da57…`), §§3.3–3.4, ledger Main:726 | C1, C2, C8, C10, C13, O1–O3, F1, F2 | support on `main` |
| `papers/Substratum.md` @ cac5d264 (`e5c6f217…`), :131–133, :171, :467 | O1, P-b | support on `main` |
| `papers/SM.md` @ cac5d264 (`7d805ac8…`), :104–110 | O1 | support on `main` |
| `book/ch18-beyond.md` @ cac5d264 (`ace0bad4…`), :104 | O1 (example of a shared mode) | support on `main` |
| composition-source-map.md @ `017ae88ee4f2…` (blob `98470461…`) | §2 rows (NS ≠ Bell locality, PR control), §3.4 | commit **not** an ancestor of `main` (on `origin/research/oi-qm-composition-source-20261107`). The file is on `main` at cac5d264 (blob `c4eeb467…`); the only difference is the author label in line 5; §§4–5 identical. **Support on `main`**, difference stated. |
| prepared-pair-source.md @ cac5d264 (`9123157c…`) §§4–5 | C9, §5 item 2, (B) lemma | support on `main` (W) |
| two-system-interface.md @ cac5d264 (`65db5a7c…`) | §0 (not native; reuse signalling) | support on `main` (W, its review status as recorded there) |
| correlation-recombination-20261107/NO-SIGNALLING.md @ cac5d264 (`25294da4…`) | §2 (NS source stop) | support on `main` (W) |
| h-bell/round-hb-1-obligation-shape/preregistration.md @ cac5d264 (`b27851ea…`) | #1060 frozen record located, untouched | provenance |
| #1210 QX-6 r7c, `QX6-BELL-CHSH.md` (blob `2b525318…`), `SHARED-MECHANISM.md` (`86490d5d…`), commit `4c7f3f86…` on `research/qphen-phase1-frozen-20261109` | A6.1, A6.4 compared with Theorem N and P-c | off `main`. **Provenance**: Theorem N is proved here from C1 alone and does not use A6.1; P-c's rejection rests on C9 (W), A6.4 only cited as parallel |
| session file `reassess/868/ASSESS-868.md` r3a (sha256 `d97c4b6b…788e1b`) | context for J14 | off `main`; provenance |
| session file `q868h/Q868H-UNIT1.md` r2 (`1e128f28…179e6`), under review | its (V) claim (native Pauli product tables are deterministic-local) | off `main`, **unverified**; provenance only, not a premise (§A.46 item 7) |
| session file `LIT-SURVEY.md` (not published) | L entries | off `main`; provenance; no primary read first-hand |
| `probes/generic_bell_checks.py` (this directory) (`a6cf97c8…71ed`) | X tags (G1–G6) | off `main`: **gap** if this record lands; the probe must land with it |
| #868 c.6791565399, c.6791606126; #1169 c.6791556736; #914 row 16; #866; #1216 body | authority, scope, Level definitions | planning records; provenance |

*Cross-check with LIT-SURVEY (present when this file was finished).* Agreements: the ε bound, its tightness witness
and constant; PI and MI as the only levers under determinism; postselection excluded on full-mass accounting.
Differences: (1) the survey's "Main posit (iv)" is Main theorem hypothesis (iv); ledger item (iv) is the
maximal-entropy measure (F2). (2) Its synthesis item 1 ("V-L") assumes a local rule and physical separation equal to
graph separation; O1 and O2 show the posits fix neither, so its V-L is interface-scoped (§3.5 item 6). (3) This
unit adds the mean-TV form of the bound and full-history contraction.

### Findings for the corpus (reported, not corrected; no manuscript edit authorized)

- **F1.** Ledger (x) ("the coupling graph is the simple-cubic graph", Main:726) is stated without the
  reference-class restriction that SM:108 attaches to local graph-dependence, while Main §3.3(a) adopts
  preparation-indexed long edges, which are edges of `G_φ` under Main:364's definition. Either (x) is restricted
  to the reference class or the adopted branch is excluded by a posit.
- **F2.** Main §3.4(iii) (Main:654) and ledger (v) (Main:726) cite §3.3 for a chaotic-mixing motivation of
  setting-generator decorrelation; §3.3 at cac5d264 contains no such passage (no "mixing", "chaotic" or
  "decorrel" in Main:360–430). MI is called a posit in §3.3 but is not a separately itemized ledger posit.

***

## 8. Not done

- No computation on any OI rule: in particular, whether the native nearest-neighbour rule's dependence fills the
  graph cone in the O2 region, and whether any native coupling violates CHSH, were not examined.
- No primary literature read first-hand; L entries rest on recall or abstract-level checks (LIT-SURVEY access note).
- Main's MI-dependent bound (C8) and check 11 were cited, not re-proved or re-run. No Lean run.
- F1 and F2 are not corrected; that needs an authorized manuscript unit.
- No reading of ledger (x) or of MI's status is chosen; both are owner questions.
- No independent review yet. Nothing here is adopted, promoted, or proposed for the manuscripts.
