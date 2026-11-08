# A5-Q3 — assessment of E1–E3 under the preregistered rule (#1049)

**Standing: WIP / UNVERIFIED. Paper-only. Checkpoint 2.** No code, enumeration or Lean was written or
run. Every algebraic step below was done by hand; this is the writer's self-report (I4). Nothing is
adopted, A5's status is unchanged, and no manuscript, ROADMAP or kernel file is touched.

**Governing rule.** The rule is `DESIGN.md` at `f71bdc8706300a743c03346a7b2d1d0bee4f9a49`, as amended by
`amendments/A1-prereg-review.md` at `d7b6d32bb07f19a8fe0141791faa29660a75759f` and by
`amendments/A2-rereview.md` at `ab0e1dac4a7288bf72df90d9caf337eb00dee3fc`. Where they conflict, the
later amendment governs. None of the three was edited.

**Review record.** The preregistration was accepted for assessment ("ACCEPT FOR ASSESSMENT") in the
review posted on #1202 as comment 6720120379. That comment was posted from the owner's account
(amaybaum) at 2026-11-08T10:02:09Z, before any assessment text existed. It states that the review is
by an independent model reviewer, not a human. The coordinating session verified that the comment
was posted at 10:02:09Z and that its text matches the review file byte for byte.

**Readings of the review's non-blocking nits.** These are the coordinating session's readings, and
neither can change a verdict.
- **K1.** E☆-law means covariance in E3's form, with b transported by ρ. It is therefore a constraint
  on b, recorded under A1.
- **K2.** Exemption (ii) of A2 G3 means transport under g itself, as in `DESIGN.md` §2.3. A transport
  chosen in order to induce some other law is not exempt.

**Pin.** Paper references `File:N` are `papers/File.md` line N at `main`
`9c201475ba6fd8f341591d14dd8e88db2e2aaa90`. Book references are `book/<file>:N`, and Lean references
are under `verification/lean-mathlib/OIBridge/`, both at the same commit.

**Owner records.** These are quoted in `DESIGN.md` and in A1 §0: #1049 c.6719806528, c.6719886996 and
c.6624263637, and #1169 c.6719386464.

**Conditionality (N6, I17).** Every entry, verdict and outcome below is conditional on amplitude-scale
gauge. The affine rule class F = linkF + b rests on it, and Substratum:272 records it as
"*Status (open, referee-grade).* Amplitude-scale gauge is adjoined as an explicit operational
principle".

***

## 1. Corpus search record (C3), and the [L] gate (A2 G4)

The search covered `papers/*.md` and `book/*.md` at the pin, using `git grep -i` for each term below.
The terms are: offset, tadpole, spurion, external source, constant term, plus a constant, link-valued,
background field, gauge principle, Yang, Wilson, locally U(6), affine map, affine link. The
results review of `118fd9c2` found that this search missed the corpus's relabelling notion of gauge.
The terms relabel, conjugat, fixed-background, frame, background and "gauge freedom" were therefore
added (n1), and their hits appear in the second table below.

Every A6 site named in A1 §3 D1 and A2 G4 was then read, together with the hits. The pattern
"locally U(6)" returned nothing because the source spells it in LaTeX (`\mathrm{U}(6)`). SM:493 was
found by reading it directly.

| Location | What it says that bears on a motivation |
|---|---|
| Substratum:102; book/ch02-substratum.md:86; book/glossary.md:13 | A6 is defined: "a site-dependent transformation G(n) … is a symmetry of the dynamics provided the coupling data carried on the links are transformed with it. The content of the assumption is this covariant interface — the coupling is link-valued data on which the transformations act". No reason is given beyond the interface. Offsets and site constants are not mentioned. |
| Substratum:104 | "A4 … and A6 … overlap in physical content (A6 promotes the symmetry that A4 constrains)". This is a relation between assumptions, not a motivation. |
| SM:104 | The contrast with general relativity is assigned to "the state-dependent-geometry principle", and "This principle is not the structural assumption (A6)". So it is not a motivation for A6. |
| SM:114 | A6 "is then the premise carrying the surviving global stabilizer to the local gauge reading". This is a T2-directed role. |
| SM:116–118 | The transformation law covers φ and M only. "This is local gauge invariance." |
| Main:726 item (xii) | A6 "fixes the interface through which the gauge symmetry is read locally". This is a T2-directed role. |
| book/ch05-gauge-structure.md:137 | "The Standard Model is, of course, a local gauge theory … The step from global to local is what background independence (A6) supplies". This motivates A6 by T2. |
| SM:493 | "The substratum dynamics is locally U(6) invariant". This states a local group, in the context of the condensate route of Theorem 5 (H-cust, SM:342). |
| SM:382 | The argument for a scalar M is withdrawn: "Any physical use of that decomposition now cites H-link, and any stabilizer use also cites H-cust." |
| SM:523 | The link variable "lives in V_K^{(n)} ⊗ V_K^{(n+ê_j)*}". The space is inferred from the transformation law, in a step of the T2 construction. |
| SM:681 | The gauge field is "the state-dependent coupling matrix M(n, ê_j) of §3.1, determined by the matter field". §3.1 contains both the state-dependent-graph principle (SM:104) and A6 (SM:114). Reading this passage as concerning the state-dependent-graph principle is this assessment's reading (n3). It is not used as a motivation for any law. |
| SM:240; Substratum:274 | The constant is placed in the site update: "an additive map plus a constant"; "F(x)=F(0)+\sum_i c_i x_i". This locates b at sites. It gives no transformation law. |
| SM:96; Substratum:270 | Amplitude-scale gauge: rescalings and uniform shifts of the field value, read as relabellings. See the relabelling-gauge rows below. The earlier entry here dismissed these as "the alphabet's relabellings, not … internal-index transformations". That dismissal is withdrawn: BackgroundIndependence.lean:26–30 states that "the internal index enters only through the alphabet", with `V := K → ZMod q`. For the K-component alphabet, the alphabet's additive automorphisms are A6's class (R1). |
| BackgroundIndependence.lean:30, :127–129; A6Instantiation.lean:70, :408, :455 | The formal class: "over the finite alphabet there is no unitary group and none is introduced"; "the coupling is transported and nothing needs preserving"; "`AddAut (Fin 6 → ℂ)` is not `U(6)`"; and "strictly larger" than the unitary group, so `A6Cov` "contains the manuscripts' law as a specialization". |
| SM:1082, :1312, :1410 ("spurion"); SM:756–1221 ("tadpole") | Yukawa spurions and loop tadpoles. These are unrelated to A6 or to offsets. |
| SM:954 ("affine map") | An affine map on mass eigenvalues. This is unrelated to link couplings. |

**Relabelling-gauge sources (R1, n1).**

| Location | What it says | What it bears on |
|---|---|---|
| Substratum:270 | "These affine relabellings are exactly the site-wise relabellings that preserve not only the coupling graph but the field-amplitude dispersion ω(k) …, so amplitude-scale gauge is one instance of the framework's master principle that *observationally indistinguishable transformations are gauge*" | Gauge read as relabelling. Under conjugation by the global unit rescaling λ, a rule constant is re-expressed as b ↦ λb. That is the E2/E3 law, on the global scalar subgroup only |
| Substratum:163 | "the field-value-scale freedom — the additive-automorphism relabellings of the alphabet"; it "removes only the common overall phase", acting on the field and the offset together | The same freedom, in the K = 6 setting |
| BackgroundIndependence.lean:26–30 | the internal index enters "only through the alphabet"; `V := K → ZMod q`; the class is `g : ι → AddAut V` | Identifies the alphabet's additive automorphisms with A6's class |
| Substratum:98 | A4 holds "up to gauge", "with gauge acting by site-wise bijections of each site's (previous, current) pair" | A site-dependent gauge in the corpus, acting on the rule by conjugation |
| Methodology:463 | "Gauge freedom is descriptive redundancy: two representations, no observable difference" | Observational indistinguishability is the criterion for gauge status |
| Substratum:272; Theorem 24's generators (Substratum:251–262) | "generator (i) relabels hidden states only" | The corpus's conjugation gauge does not cover visible data |
| Substratum:102; book/ch02-substratum.md:86; A6Instantiation.lean:359–365 | A6 is "not the stronger fixed-background condition"; as the definition, that condition "would refute the manuscripts' own rule for exactly the site-dependent transformations the gauge reading needs" | The corpus's reason for transporting data rather than holding them fixed. The reason is directed at the gauge reading (T2/O5) |

**Search result.**
- No location at the pin states a transformation law for a site offset under A6, a reason to place an
  offset on links, or a reason to hold a non-singlet constant fixed.
- The relabelling sources support the E2/E3 law on the global scalar subgroup of A6's class. Extending
  that law to the site-dependent class needs A6's transformations to be gauge in the relabelling sense
  (Methodology:463; Substratum:270). The routes to that are either observationally excluded at Main's
  absolute interface, or directed at T2/O5 (§4).
- The corpus's stated motivations for A6 itself are T2-directed: SM:114, Main:726 item (xii) and
  book/ch05:137.

**[L] items, used only after this search, from memory and not re-read.**
- **[L1]** C. N. Yang and R. L. Mills, *Phys. Rev.* 96, 191 (1954). Cited for two claims:
  - (a) requiring invariance of the interactions under position-dependent rotations of the isotopic
    frame needs a compensating field with an inhomogeneous transformation law;
  - (b) its premise, that the orientation of the isotopic frame has no physical significance. This
    premise concerns frames for dynamical fields. It is neutral between holding a non-dynamical
    constant fixed and re-expressing it under a frame change. It is therefore credited as motivation
    to neither offset law (R2).
- **[L2]** K. G. Wilson, *Phys. Rev. D* 10, 2445 (1974). Cited for two claims:
  - (a) the link variable transforms as U(n, μ) → g(n) U(n, μ) g(n + μ)⁻¹;
  - (b) the lattice action is built only from gauge-invariant terms (plaquettes, and link-matter-link
    products), so no term linear in a non-singlet site field appears. Judged on its own (A1 C2), (b)
    states, in the literature's setting, that non-singlet constants are absent. That is T1's content,
    so (b) is **target-adjacent** (R2).
- **[L3]** H. Georgi, *Weak Interactions and Modern Particle Theory* (1984). Cited for the spurion
  method: a symmetry-breaking parameter is treated *as if* it transformed under the symmetry, which
  makes the Lagrangian formally invariant and constrains how the parameter can appear. The method is
  presented as a calculational device for an explicitly broken symmetry.
- **[L4]** S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry* I (1963), chapter III.
  Cited for the claim that affine connections are connections in the bundle of affine frames, whose
  structure group is the affine group, translations included.

***

## 2. Block A — mathematical consequences (recorded, not scored)

### A1. What each candidate forces on b [D]

**E1.** By `a6cov_all` (BackgroundIndependence.lean:161),
linkF N (gaugeLink g M) (siteAct g c) = siteAct g (linkF N M c).

So Cov_E1 ⇔ ∀ g, b = siteAct g b. Since g is site-dependent and arbitrary, this is
b_i ∈ Fix(AddAut V) at every site. By cases:
- **K = 1, q odd:** the unit −1 gives 2b = 0, so b = 0.
- **K = 1, q even > 2:** −1 gives b ∈ {0, q/2}. Every unit u is odd, so (u − 1)·q/2 ≡ 0, and both
  values are fixed.
- **K = 1, q = 2:** AddAut(ℤ/2) is trivial, so b is unconstrained.
- **K ≥ 2, any q:** a transvection I + E_lk adds b_k to component l. Some b_k ≠ 0 for b ≠ 0, so b = 0.
- **The lift ℂ^6, with the class AddAut or U(6):** −I gives b = 0.
- **Uniform or non-uniform b:** the condition is site-wise, so the result is the same.
- **S1** (K = 1, q = 5): 2·1 ≠ 1, so S1 is excluded.

These reproduce the core file's N9 list.

**E1′** (the class is the site-wise stabilizer of b): Cov holds for every b. It forces nothing.

**E2.** Since g_j⁻¹(0) = 0 and g_i is additive,
F_{g·A}(g·c)_i = Σ_j g_i(A_ij(g_j⁻¹ g_j c_j)) = g_i(Σ_j A_ij(c_j)).
So Cov_E2 holds identically, and no b is excluded. The induced law is
(g·A)_ij(0) = g_i(a_ij), hence b_i ↦ g_i b_i. This re-derives the A1 §2 "E2 ↔ E3" line (H5).

**E3.** linkF N (gaugeLink g M)(g·c) + g·b = g·linkF N M c + g·b = g·(linkF N M c + b). So Cov_E3 holds
identically, and no b is excluded. The law is b_i ↦ g_i b_i.

### A2. The Q4 stabilizer [D]

Glob is the set of constant g carrying the rule to itself with the candidate's data unchanged. It is
evaluated on the lift, with generic block-scalar M (the M-route) and 𝒢 = U(K) or G_0.

- **E1:**
  - On admissible rules b = 0 (A1). Constant g must commute with M, and the commutant of M in U(6) is
    G_0. This coincides with reading (L).
  - At rule level, g must also fix b. That condition is vacuous at b = 0.
  - The Stage 2(d) object is the coupling, since b is not data. The constraint on b is rule-level
    (`A6Glob`-type).
- **E1′:** Glob = {g ∈ G_0 : g b = b}. For b = v𝟙 with v ∈ V_1 \ {0}, this is G_v = U(3)×U(2)×{1},
  the (A-lin) result. It needs H-b to place v in V_1. Without H-b, a T₁ component reduces U(3) to
  U(2) (Q4 N4b).
- **E3:** the data (M, b) are unchanged iff [g, M] = 0 and g b = b. So Glob = G_v under H-b, which is
  the (A-lin) result again. Data level and rule level coincide, so the coupling-level reading
  (Substratum:102) includes the offset.
- **E2:** the data are unchanged iff [g, M] = 0 and g a_ij = a_ij for every link. So Glob = ∩ Stab(a_ij)
  ⊆ G_v.
  - Equality holds when every a_ij ∈ V_1.
  - A zero-sum split with components outside V_1 gives a smaller group, even at b = 0.
- **(A-aff):** no candidate's class contains affine internal maps, so none realizes (A-aff).
  Resonance (μ_{A₁} = 1) is not used.

### A3. The local class, read from each definition (c.6719886996 boundary)

| Candidate | Local class | Data transported |
|---|---|---|
| E1 | ι → AddAut V | M by `gaugeLink`; b not transformed |
| E1′ | site-wise Stab(b_i) ⊆ AddAut V | M by `gaugeLink`; b fixed by construction |
| E2 | ι → AddAut V | affine link maps A_ij ↦ g_i ∘ A_ij ∘ g_j⁻¹ |
| E3 | ι → AddAut V | M by `gaugeLink`; b by `siteAct` |

No promotion to local gauge invariance, link action or plaquette statement is derived.

### A4. Relations among the candidates [D]

- E2 and E3 induce the same law on b.
- E1 is E3 with the trivial law.
- On E1's admissible set, b ∈ Fix(AddAut V), every g fixes b. So E1 and E3 coincide there at rule
  level, and E2 agrees with them for any split of such a b.
- E3 embeds equivariantly into E2 by placing b_i on one chosen link of each site. The choice of link
  breaks the cubic symmetry of the data.

***

## 3. Block B — imported assumptions

**B1, the mandatory offset-law rows (A1 §3), plus E1′'s class.**

| Candidate | Import | At the pin | Status |
|---|---|---|---|
| E1 | the offset is not transformed | not in the corpus (§1) | none |
| E1′ | the local class is the site-wise stabilizer of b | Q4 note N7 remark only (a record, not a source with a motivation) | none |
| E2 | link couplings are affine maps; the offset is link data transported by g_i ∘ A_ij ∘ g_j⁻¹ | not in the corpus. Links are matrices in V⊗V* (SM:116, SM:523), and the constant sits in the site update (SM:240, Substratum:274) | none |
| E3 | the offset is site data, transformed as the field is | not in the corpus. H-b (the Q4 note) is a global O-action hypothesis, open (Q4a), and does not supply a site-dependent law | none |

**B2, baseline elements used outside their stated role.** The cells are filled from the A1 §3 table,
as amended by A2 H2 and H7.

| 𝔅 element: stated role (source) | E1 | E2 | E3 |
|---|---|---|---|
| Class ι → AddAut V: the class over which an identity holds with all named data transported; not the manuscripts' group (BackgroundIndependence.lean:30, :127–129; A6Instantiation.lean:70, :408) | quantified over all g with b not transported: **outside the role**. The class's breadth constrains a datum that is not transported, whereas the stated role is containment for an identity in which "nothing needs preserving" | acts on transported link data: inside | acts on transported data: inside |
| `gaugeLink`: the transformation law of SM:116 (:121–123) | M only: inside | applied to affine maps: **outside** (pattern 2) | M only: inside |
| `siteAct`: the action "on configurations" (:87–91) | appears on F's value: inside | not used on b directly | applied to b, which is not a configuration: **outside** (pattern 3) |
| `V →+ V` typing (`linkF` :118; A6Instantiation.lean:147) | kept: inside | relaxed: **outside** | kept: inside |
| E4, H-link | not in the statement | not in the statement | not in the statement |

E4 and H-link on the offset enter only through H-b, in the A2 entries. They are recorded as imports
there, and are not in any candidate's statement.

***

## 4. Block C — classification of each import

The classification is judged on the import alone (A1 §3 C2). What an import yields together with 𝔅
is in A1 above, and is not used here.

**E1, B1 (b not transformed).**
- Corpus: none (§1).
- The strongest corpus candidate is the literal clause of Substratum:102, "provided the coupling data
  carried on the links are transformed". It names only link data, and read literally for an affine
  rule it would leave b untransformed. It is not counted as a motivation, for two reasons:
  - it is a definition stated where the rule class has no site constant. This is the same scope
    reason A1 §3 D1 applies to Substratum:102's "imposes no further condition", and it is applied
    here identically to E1, E2 and E3;
  - it gives no reason; it only does not mention offsets.
- [L1](b) is neutral between the two offset laws and is credited to neither (R2).
- [L2](b) is target-adjacent: on its own it states that non-singlet constants are absent, which is
  T1's content.
- The relabelling sources (§1) move a rule constant under the global scalar elements, b ↦ λb. They
  do not support holding b fixed.
- **Class: target-adjacent.** No independent component was located (R2). This is the first ground
  on which E1 fails J3. The literature involved is the same gauge-principle literature as the
  baseline's J3 (§7).

**E1, B2 (the AddAut class constraining an untransported b).**
- Corpus: the class's stated role is formal (containment for an identity), and the sources say it is
  not the manuscripts' group.
- [L1] and [L2] concern invariance under the **physical** gauge group. They give no reason to require
  invariance under the formal class AddAut V.
- Taking the physical group instead, two classes were located at the pin.
  - **Site-wise U(6)** (SM:493, "The substratum dynamics is locally U(6) invariant"). After the C3
    search, no stated motivation of its own was found:
    - its scalar-M basis (SM:376, "Remark below") is withdrawn at SM:382;
    - its stabilizer use rests on H-cust (SM:342);
    - its local character is the A6 promotion itself (Substratum:163, "promotes … to local gauge
      invariance").

    **Class: none found** (R3). Adopting local U(6) as A6's physical class would itself be an
    O5-type promotion, which the boundary in c.6719886996 excludes from this unit.
  - **G_0, or SU(3)×SU(2)×U(1)** (Substratum:163; SM:114). This is T2 itself. **Class:
    target-adjacent.**
- **Class: none found** for the formal class; none found for site-wise U(6); target-adjacent for
  G_0. This is the second ground on which E1 fails J3. Even if a physical class were granted, the
  motivation for holding b fixed would be [L2](b), which is target-adjacent (R2).
- Pressure test (§A.31). This branch is the one favourable to T1 and T2.
  - Could the gauge principle be applied to a class with an independently stated physical gauge
    status? None was located: the internal index's physical group is, in the corpus, an output of
    Stage 2(d) or an input of the H-cust route. The class's specification decides E1's content (A1
    depends on it), so the class cannot be left unspecified.
  - The verdict does not depend on what E1 yields: the same role test, applied to E2 and E3, finds
    their uses of the class inside its role.

**E1′, B1 (class = Stab(b)).**
- Corpus: none.
- [L]: the exact residual symmetry of a fixed symmetry-breaking parameter is its stabilizer. That is
  a fact about explicit breaking, not a reason for A6's class to be defined by b.
- The functional test does not catch it: it restricts the class, not b's values.
- **Class: none found.**

**E2, B1 and B2 (affine link maps; `gaugeLink` on affine maps; typing relaxed).**
- Corpus: none. The corpus links are matrices (SM:116, SM:523), and the constant sits in the site
  update (SM:240; Substratum:274).
- [L4] describes affine connections with the affine structure group, translations included. E2 keeps
  AddAut V as its local class, so [L4] does not describe E2. In any case [L4] is mathematics, not a
  physical motivation.
- **Class: none found.**

**E3, B1 and B2 (b transformed as the field; `siteAct` on b).**
- Corpus: none (§1).
- SM:523 infers the link variable's space from its transformation law; it does not state that a
  datum's type fixes its law. Using it that way would compose a motivation, which A2 G1 excludes.
- [L3] spurion: a calculational device that assigns a law *as if*; it makes no physical claim that b
  transforms.
- [L1](a) and [L2](a) motivate transporting the connection, not a non-dynamical site constant.
- [L1](b) is neutral and is credited to neither law (R2).
- **Relabelling route (R1).** This is the strongest corpus route, and it supplies one independent
  component and one target-adjacent component.
  - **Independent component.** Amplitude-scale gauge treats the global unit rescaling λ as a
    relabelling. Its motivation is operational (Substratum:270), and it is the principle on which this
    whole outcome is already conditional. Under conjugation it transforms a rule constant as the
    field, b ↦ λb. That is E3's law, but **only on the global scalar subgroup** of A6's class.
  - **Extending it to the site-dependent class.** That requires A6's transformations to be gauge in
    the relabelling sense: observationally indistinguishable (Methodology:463; Substratum:270). Three
    things stand against that:
    - at Main's absolute interface (Q1), visible site-wise relabellings are distinguishable (core
      file §3.3.8 item 6; Proposition 2.6(b), [D] there);
    - the conjugation gauge of 𝒢_sub is hidden-only (Substratum:272);
    - the #1049 safeguard requires the gauge status of site-dependent transformations to be
      established separately.
  - **Target-adjacent component.** What remains is the identification of A6's transformations as
    gauge (SM:118; Substratum:163; Main:726 item (xii)), together with Substratum:102's reason for
    transport over a fixed background (A6Instantiation.lean:359–365). Both are directed at T2 and O5.
- [L3], the spurion method, is a representation device and is recorded as such.
- **Class: mixed, with an insufficient independent component.** The independent part motivates the
  law on the global scalar subgroup only, not on the class (`DESIGN.md` J3).
- Pressure test (§A.31). Rejecting E3 protects T1 and T2, since E3 admits offsets and gives G_v under
  H-b, so this branch is pressure-tested too.
  - The strongest case for E3 is the **passive reading**, H-passive: A6's transformations are changes
    of description, so every internal-index-valued datum transforms with them.
  - Its corpus route is the relabelling route above, so H-passive has the same classification:
    **mixed, with an insufficient independent component**.
  - The sources' own wording for A6 is active: "symmetry of the dynamics" (Substratum:102) and "local
    gauge invariance" (SM:118).

**Hypotheses offered for J_c (F10).**
- **H-b.** It is motivated by E4 (Substratum:82) applied to the whole rule under H-link (posited).
  It is independent given H-link, but it is global and does not supply any candidate's site-dependent
  law. So it places no candidate in J_c.
- **H-passive.** Mixed, with an insufficient independent component (above). F10 admits only
  independent hypotheses, or mixed ones whose independent component suffices on its own, so it
  cannot place E3 in J_c.
- **H-active** ("A6's transformations, under a stated physical group, are exact invariances with
  untransported constants"). The located physical groups are none found (U(6)) or target-adjacent
  (G_0), and its motivation for holding b fixed is [L2](b), which is target-adjacent. So it cannot
  place E1 in J_c.

**Countercontrol imports.** These are classified in §7.

***

## 5. Block D — consistency

The grades are consistent, tension or inconsistent. "Out of scope" is reserved for the D1 sentences
pre-graded in A1 (A2 H1), and those are graded identically for every candidate: out of scope on
b ≠ 0, and consistent on the linear class.

| | D1 (other A6 sources) | D2 (Q1) | D3 (Q2, scoped) | D4 (P1–P6) | J4 |
|---|---|---|---|---|---|
| E1 | **tension.** It holds one datum fixed, the pattern Substratum:102 declines for the coupling ("not the stronger fixed-background condition"). It uses the formal class as a physical constraint, whereas A6Instantiation.lean:70 says the class is not the manuscripts' group. For the constant scalar elements λ of A6's class, amplitude-scale relabelling transforms a rule constant by conjugation (b ↦ λb; Substratum:270, :163), while E1 holds b fixed under the same elements and so requires λb = b (R4). These are two principles, not a contradiction. No kernel statement is contradicted | consistent (rule-level, absolute interface) | consistent (no identification) | preserved: P1 by C-LIN; P2 on the linear class; P3 C2 (S1 keeps its properties; only its A6 status under E1 changes); P5 (vii) still true; P6 unchanged | held |
| E1′ | **tension.** The local class depends on the rule's data, which no A6 source has | consistent | consistent | preserved | held |
| E2 | **tension.** Link data are affine maps, not elements of V⊗V* (SM:523, SM:116). Plaquette and trace statements (SM:118) are not examined (O5 boundary). Zero-sum splits are redundant data with no gauge status claimed, so D3 is not triggered | consistent | consistent | preserved | held |
| E3 | **tension.** It transports a site datum that SM:116 and Substratum:102 do not list | consistent | consistent: the covariance relation is not an identification (A1 §3 D3) | preserved | held |

***

## 6. J1–J6 for each candidate and variant

Each J5 entry compares only with variants that the candidate's own C1-cited motivation supports
equally (A2 G1). Variants differing only in the domain of the quantifier are decided by `A6Cov`'s
∀ g (A1 §4).

| | J1 | J2 (C-LIN) | J3 | J4 | J5 | J6 |
|---|---|---|---|---|---|---|
| **E1** | held | held | **not held**, on two grounds: B1 is target-adjacent ([L2](b)); B2 is none found (formal class; site-wise U(6)) or target-adjacent (G_0) | held (tensions) | held: E1′ is excluded by the ∀ decision; the class variants are settled by the same decision; [L2](b) distinguishes E1 from E3, but [L2](b) is a target-adjacent item (R2) | **not held**: no consequence beyond A1 and A2. Shared with the baseline |
| **E1′** | held | held | **not held**: none found | held (tension) | **not held**: the ∀ decision selects E1 over it | not held |
| **E2** | held | held (its data space is larger at b = 0) | **not held**: none found | held (tension) | **not held**: no C1 motivation distinguishes splits, and splits change A2 (§2). Scope finding: an Aff(V) reading is equally supported by "link couplings may be affine maps" (not counted) | **not evaluable within the authorized scope**: candidate consequences are translation parts of link holonomies, beyond the O5 boundary |
| **E3** | held | held | **not held**: mixed, with an insufficient independent component. Amplitude-scale relabelling reaches only the global scalar subgroup | held (tension) | **not held**: with no C1-cited motivation, the trivial law (E1) and other representations are equally supported, and they change A1 | **not held**: covariance is an identity; nothing beyond A2. Shared with the baseline |

**Variants found beyond A1 §2 (I14).**
- E1's class variants on the lift: site-wise U(6) (SM:493), and G_0. These fall under "transformation
  class: … or a subgroup", and all give b = 0.
- The active and passive readings of A6 for data the sources do not name (H-active, H-passive). They
  are recorded as readings, not as candidates.

***

## 7. Controls

**C-LIN** (A1 §5.2; A2 G3):
- E1, E1′, E2, E3, E★ and E☆ each reduce to `A6Cov` on `A6Cov`'s own data, with the same class and
  `gaugeLink`. **Pass.**
- E☆-law is compared on the same class, ι → G_0, and reduces at b = 0. **Pass.**
- **E-inv** reduces to `A6Inv` (:104): the coupling is held fixed and preserved pointwise, not
  transported by `gaugeLink`. **Fails, as required.** So C-LIN is not vacuous.
- Recorded: E2's data space is strictly larger at b = 0 (zero-sum splits).

**C-POS** (the baseline `A6Cov` on the linear class; A1 §5.1 and A2 G4):

| Clause | Observed | Predicted | Basis |
|---|---|---|---|
| J1 | held | held | |
| J2 | held | held | |
| J3 | **held, [L] only** | held, [L] only | Mixed. The corpus motivations are T2-directed (SM:114; Main:726 item (xii); book/ch05:137). The independent component is [L1](a) and [L2](a) |
| J4 | held | held | |
| J5 | held | held | `A6-inv`, `A6-glob` and `A6-sd` are distinguished by Substratum:102 and SM:104 |
| J6 | not held | not held | The interface's consequences are identities (SM:118). The further ones are T2 or beyond O5 |

There is no deviation from the prediction. The baseline is in J₁₋₅ and not in J₁₋₆. Its J3 rests on
[L] alone.

**C-CAL** (A2 G2): E4 on the whole rule, "F commutes with the lattice rotations acting on site
labels".
- Sources: Substratum:82, an observational input, and SM:238, a Lorentz-invariance requirement.
- On its own it presupposes no T and is not designed to exclude a construction.
- Its statement concerns the whole rule, so the functional test does not apply.
- **Classified independent. Pass.**

**C-TI** (A1 §5.3; A2 H4):
- No verdict above cites an A1 or A2 entry as its reason.
- E1's J3 failure rests on the role of the class and on the target-adjacency of the located physical
  classes. That is a penalty for dependence on T2, which the table permits. It does not rest on b = 0.
- The same role test was applied to E2 and E3, and found inside the role.
- J5 entries compare variants as worded.
- The results review (R2) found that [L1](b) had been credited to E1's offset law and refused to
  E3's. That asymmetry favoured the law that produces T1, and it was not decisive. It is corrected
  here: [L1](b) is credited to neither law. The correction removes a T1-leaning credit and adds no
  T1 penalty.
- **Pass.**

**Countercontrols** (A1 §5.4; A2 G3; I8):
- **E★** (E3 data, with all offsets identified, for a stated T2 reason):
  - J3 is not held. The import is target-defined by its stated reason, and the functional test catches
    the identification, which has no effect outside the offset sector. The rejection comes from the
    stipulation.
  - J4 is also not held: D3 is inconsistent (a declared physical identification beyond covariance,
    contrary to Q2), and so is D2 (core file, Proposition 2.6(a), itself [D] in the core file).
  - **Rejected through J3. Pass.**
- **E☆** (identification modulo the A₁ phase):
  - The functional test catches it, so it is target-defined. **Rejected through J3. Pass.**
  - The C1 expectation is confirmed: the near-source, the common-phase removal of Substratum:163 and
    :270, acts on the field and the offset together, not on the offset's A₁ phase alone.
  - J4 is also not held (D3).
- **E☆-law** (read as K1, with ρ(A, B, z) = (A, B, 1) on b):
  - Under K2, ρ is none of the exemptions (i)–(iii).
  - Its statement acts on b alone and has no effect outside the offset sector, so it is target-defined.
    **Rejected through J3. Pass.**
  - The constraint it imposes (A1, not scored): ρ(g_i) b_i = g_i b_i for all g ∈ G_0 gives
    (z − 1) b_{i,1} = 0, so the A₁ component vanishes.

**Void conditions** (A1 §5.5): none fired. Every control is green, so the outcome below is rendered.

***

## 8. Outcome, generated from the rule

**Sets.**
- J₁₋₅ = ∅
- J₁₋₄ = ∅
- J₁₋₆ = ∅
- J_c = ∅

**Outcome: (N).** None of E1–E3 is independently justified as the extension of A6 to affine rules on
the record at `9c201475`. Conditional on amplitude-scale gauge (Substratum:272).

**Count.**
- With [L]-only J3 passes excluded, |J₁₋₅| = 0.
- No candidate passes J3, so no [L]-only pass enters the count.
- The one [L]-only J3 pass is the baseline's (C-POS).
- E1's B1 entry is classified target-adjacent ([L2](b)). It is not an [L]-only pass. E1 fails J3 on
  both B1 and B2.

**Per candidate.**

| | J1 | J2 | J3 | J4 | J5 | J6 |
|---|---|---|---|---|---|---|
| E1 | held | held | not held | held | held | not held |
| E1′ | held | held | not held | held | not held | not held |
| E2 | held | held | not held | held | not held | not evaluable |
| E3 | held | held | not held | held | not held | not held |

**What (N) states, and what it does not.**
- It states that the A6 sources at the pin, written for additive link-coupled rules, fix no
  transformation law for a site offset. For none of the three laws was an independent physical
  motivation located that suffices on its own for A6's class. Specifically:
  - E1, the offset untransformed: its motivation is target-adjacent ([L2](b)), and its constraint
    comes from the formal class or from a physical class that is none found (U(6)) or T2 (G_0);
  - E2, the offset carried on affine links: none found;
  - E3, the offset transported as the field: amplitude-scale relabelling supports this law on the
    global scalar subgroup only.
- It does not state that any candidate is false, that no extension of A6 to offsets exists, or
  anything about A5.
- Restated by the reading of A6 for data the sources do not name:
  - E1 corresponds to an active-invariance reading, under which the offset is a fixed parameter and
    the content depends on a physical gauge group that the corpus supplies only through T2;
  - E3 corresponds to a passive, relabelling reading, under which it restricts nothing. The corpus
    supports that reading for the global scalar subgroup. For the site-dependent class it supports it
    only through identifications directed at T2 and O5.

**Status.** A5's status is unchanged. A6 remains `A6Cov` on `main`. The core file's Q3 marker
("carries A5 in relocated form") is consistent with E1's J3 entry: E1 restricts b only through the
choice of class. O5 is not examined.

***

## 9. Sensitivities, with the results review's rulings

The writer named three sensitivities at `118fd9c2`. The results review ruled on each, and its rulings
are recorded here.

1. **E3 and H-passive.** At `118fd9c2` the writer noted that crediting [L1](b)'s frame-convention
   premise to H-passive would move E3 into J_c or J₁₋₅, giving an (S) outcome resting on [L] alone.
   **Ruling: the scenario does not arise.**
   - Under C1, [L1](b) is not a passage that motivates transporting a non-dynamical rule constant.
     Reading it that way is the assessor's own extension.
   - [L1](b) is credited to neither law (R2). Crediting it to both would also credit E1, and E1
     still fails J3 on B2.
   - H-passive's corpus route, relabelling gauge, is mixed with an insufficient independent
     component (R1), so F10 bars it from J_c.
2. **E1 and the class role.** **Ruling: robust.**
   - The formal role of AddAut V is stated in the sources, and E1's use of it to constrain an
     untransported datum lies outside that role.
   - SM:493's local U(6) has no stated motivation of its own (none found), and adopting it would be
     an O5-type promotion (R3).
   - Even if a physical class were granted, the motivation for holding b fixed would be [L2](b),
     which is target-adjacent (R2).
   - So E1 fails J3 on two independent grounds.
3. **[L] items.** **Ruling: no set membership rests on [L].**
   - [L1]–[L4] are from memory and were not re-read (§A.46 item 7), by the writer or the reviewer.
   - They enter C-POS's J3 (the baseline's [L]-only pass) and the classification of E1's B1
     ([L2](b), target-adjacent).
   - The outcome (N) and the empty sets do not rest on them.

***

## 10. References not on `main` (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1202 c.6720120379 | review record; ACCEPT FOR ASSESSMENT; K1 and K2 | provenance, by quotation of its verdict. Posting time (10:02:09Z) and byte-identity with the review file verified by the coordinating session (n4) |
| The results review of `118fd9c2` (R1–R4, n1–n4, and the rulings on the sensitivities) | corrections applied in §1, §4–§9 | provenance. Each change is stated in this file |
| #1049 c.6719806528, c.6719886996, c.6624263637; #1169 c.6719386464; #1049 Issue body | as in `DESIGN.md` and A1 §0 and §7 | support, by quotation (in those files) |
| [L1]–[L4] | §1, §4 | literature from memory, not re-read. The outcome (N) and the set memberships do not rest on them. C-POS's J3 pass and the classification of E1's B1 do (n2) |
