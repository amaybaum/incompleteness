> **Superseded.** This revision of the #1245 H-BD report is superseded. The authoritative report is `REPORT-r5.md` in this directory; its change map is `CHANGES-r5.md`.

# #1245 H-BD: origin and derivation of the deep-to-boundary influence bound (resumed paper-only round)

## Status, pin, sources

- **Status.** Paper-only, read-only research under the existing authorization (owner, 2026-11-12, "Let's open an issue to investigate its origins, and try to find a proper derivation."), resumed by owner decision 2026-11-25 (#1245 comment 7163939634). Nothing is adopted and no manuscript, Lean or premise change is made. No computation was run. The new results below are hand derivations: they are not independently reviewed and not machine-checked. Items marked [W] are the writer's own unverified steps; [background] marks external literature I cite but did not retrieve.
- **Pin.** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`.
- **Sources read.**
  - AGENTS.md at the pin.
  - #1245 body and all 11 comments.
  - #1244 comments 6817631738 (item 3 audit), 6818164393 (posit record), 6818792755, 6820568979, 6821450454, 6824919310, 6880017798, 6880703935.
  - `papers/GR.md` sec. 3.1-3.2, App. A (A.5, A.7) and App. B.
  - `papers/Main.md` sec. 1.4, 3.2, 3.3, 4.5 (posit ledger) and 4.6.
  - `papers/Substratum.md`:54, 60, 80, 92, 262, 268.
  - `papers/Methodology.md`:353.
  - Book mirrors: ch02:44/144, ch03:220, ch07:46, ch18:170/178, appendix-b:169-210.
  - Verification records on `main` that cite H-BD (listed in sec. 1).

***

## 1. What has already been done (do not repeat)

| # | Work | Where (commit / record) | Result | Support class |
|---|---|---|---|---|
| P1 | #1244 item 3 audit of GR sec. 3.2 step (ii) | #1244 c.6817631738, at `1b273698` | Step (ii) inferred small influence from small motion; a frozen D still drives B (C0 = (v+b, b+d, d)). Explicit counterexamples C0, C1', C2, C3 under 5 of 7 readings of tau_B, none under R5 (D-to-B influence) or R6. GR:813's measure form does not recover the lemma. The A.5 step-(i) display is refuted (R2 form). A.7 is valid only on its own hypothesis. | Hand-checked examples; two internal reviews |
| P2 | Posit record | #1244 c.6818164393 | H-BD is a named posited hypothesis; tau_BD is not fixed | Owner decision |
| P3 | sec. A.29 check of H-BD | #1245 c.6818702013; the full check is session material, not on `main` | (a) eps = Delta t/tau_BD per step, and bijectivity suffices. (b) **Linear dichotomy:** for affine phi on a finite abelian group, eps is in {0} or [1/2, 1], at every B thickness and every power; under ledger (vii), H-BD with tau_BD > 2 Delta t holds iff L = 0. (c) 1D ring: eps = 1/2. (d) Local nonlinear rules need sigma >~ 1.4-4 x 10^2 for tau_BD ~ 1/H, assuming sigma = ln q_c. (e) C-4: H-BD does not bound A.5's channel terms. (f) The cone form is the parameter-free baseline. Verdict: ad hoc at 1/H; otherwise a conditional placeholder. | Paper derivations; internal review |
| P4 | Owner record | #1245 c.6818793241 | Recorded "conditional, not explanatory, A.5 not recovered, cone baseline" | Decision |
| P5 | Manuscript correction | PR #1248, merged as `0cf85e21` (commits `42115ca2`, `501dba1c`, `9483f4f9`, `ccf73468`) | GR sec. 3.2 now carries (a) the exact cone form, (b) H-BD as posited with the linear dichotomy (GR:112-138), A.5 narrowed with its order open (GR:757-769), App. B for any deep cardinality. Substratum, Methodology, book and FULL carry H-BD. | On `main` |
| P6 | W1 entropy-slope investigation and W1-1 | #1245 c.6818970549, c.6828106610 (L current, C alternative), c.6831591590, c.6835701280, c.6841976574; `verification/programmes/physical-realization/w1-1-20261112/` (r4 accepted; merged via #1265 as `c3b5f37a`) | W1 is an additional physical assumption. Counterexample for reading L. An extensive deep sector gives C_D/2s_B ~ 7e59. H-inert, H-eq and W1' remain unadopted. | Paper; reviewed (r4) |
| P7 | A1-programme audits that touch H-BD | `verification/audits/foundations/r1-l8-stage0-20261120/AUDIT.md` (F2; the C4 trace); `a1-remainder-20261119/REMAINDER.md` C4/L10; `a1-09-dependency-census/CENSUS.md` D25/C08; `p7-shell-calibration-20261116`:84; `a1-free-p7-coupled/DECISION.md` row 4; `a1exit-ledger-20261120` X-73/X-74 | (i) The counting step of GR:126 uses \|f^-1(S)\| <= \|S\| for injections. A measure-theoretic H-BD (L10) needs fibrewise non-expansion of the deep law and is open. (ii) H-BD controls absolute row error only, so it is insufficient for P7's log-ratio and energy-derivative needs. (iii) **None of H-BD's consumers reaches an ACC consequence; every one concerns invisibility of deep-sector cardinality.** | Paper audits on `main`; WIP status as stated there |
| P8 | M9 assignment | #1245 c.6880025217; LEDGER-r5 sec. 10 | M9 is the energy-shell mechanism (W1), not H-BD itself | Planning |

**Routes in the Issue body already closed:**
- Route 1 (causal) yields the cone form (P3, P5).
- Route 5 found no independent fix of tau_BD (P3).

**Routes in the Issue body not yet tested:**
- Route 2 (typicality).
- Route 3 (observer-relative partition).
- Route 4 (a restated (C2)).
- The general nonlinear and inhomogeneous case beyond the q-threshold.
- The weaker-bound question (Q4).

These are the subject of this round.

***

## 2. Record assessment

- **The lemma.** GR sec. 3.2 (a), the cone form, is a paper derivation from Main sec. 3.3 (the coupling-graph cone) and App. B. It is exact and parameter-free. I did not check its Lean status.
- **H-BD.** GR:122 is posited. Its proof of (b) given H-BD (GR:126) is a correct counting argument for finite C_D under counting measure (P7 F2 limits it to that measure).
- **The linear dichotomy (GR:128).** Correct as stated. It agrees with P3.
- **Negative findings that stand.**
  - Small motion does not bound influence (C0).
  - H-BD does not bound channel or purity terms (C-4).
  - H-BD fails under the selected linear rule at every cut with a deep neighbour.
  - The 10^-32 figure needs tau_BD >~ 1/H, and nothing derives that value.
  - H-BD gives no relative-error control (P7).

***

## 3. The four questions

### Q1. Does the needed bound follow from existing OI principles?

**The bound that is needed.** H-BD is a per-step statement about in-cone coupling *magnitude*: for every fixed (v, b), at most a fraction Delta t/tau_BD of deep configurations alters the one-step V x B output. Its consumers use it for one thing only: a *fixed, one-layer* B such that T(t) = T^(B)(t) + O(t/tau_BD), uniformly in t << tau_BD.

**Locality, Lieb-Robinson bounds and the cone.** For a site-local bijective update, the Lieb-Robinson-type bound is the exact graph cone (Main sec. 3.3), with no tail. Every causality statement constrains only influence *outside* the cone. D is adjacent to B, so D-to-B influence is inside the cone after one step. Hence no locality or propagation-speed principle bears on H-BD. These principles give exactly the cone form.
- Conclusion: H-BD does not follow from them.
- Support: logical (paper).

**New result R1 (exact threshold, observer-uniform form).**
- *Setting.* phi is site-local with bounded read sets (A3, ledger (ix)) and nearest-neighbour range (x). The read component has alphabet size q. The cut is the cosmological ball of fixed radius R_H with B its 1-neighbourhood. H-BD with fraction eps_f = Delta t/tau_BD is required at the horizon cut of *every* observer position. Partition-relativity (Main sec. 1.4: phi is partition-independent) and de Sitter / cosmological homogeneity (E4) motivate that requirement.
- *Claim.* If eps_f < 1/q, then phi has no inter-site dependence: G_phi is empty, every partition is closed, and T(t) is a permutation for all t, so (C1) fails everywhere.
- *Proof sketch.*
  1. Take a B-site i whose only deep read-neighbour is i+e (a terrace-interior site).
  2. At any fiber (v, b), the component of the output at i varies with d only through x_{i+e}, which is uniform over q values.
  3. If f_i(a, .) is non-constant at the assignment a realized by (v, b), the fraction is at least 1/q. So eps_f < 1/q forces f_i to be independent of x_{i+e} at every a, because every a is realized by some fiber.
  4. Every site i and every direction e occur in this role for some observer position. The cubic-symmetric digitized ball of radius ~1e60 has terrace-interior B-sites facing each of the 6 directions [W, geometry], and translation moves them to i.
  5. So no site reads any neighbour.
- *Scope.* No translation invariance is used. The linear dichotomy is the special case q prime with L != 0, which gives eps_f >= 1/2.

**New result R2 (transfer; translation invariance (xi) added).**
- (a) For each direction e, the worst-case per-link dependence fraction satisfies eps*(e) <= -ln(1 - eps_f)/N'_e, where N'_e is the number of terrace sites facing e in an independent set at one cut. This is rigorous given the independent-set choice: the deep neighbours are disjoint, so the deviations are independent under uniform d. With N'_e ~ c A/eps_lat^2 [W, constant c = O(1)] and tau_BD ~ 1/H, eps* <~ 1e-183. Either the rule reads no neighbour, or q >~ 1e182. This reproduces P3(d)'s upper threshold and is not new.
- (b) **The new part.** Every link that is D-to-B for one observer is B-to-V for another. So the *same* per-link bound holds for V-sites reading B-sites.
- (c) At t = Delta t, with hidden values uniform:

  sum_j |T_ij(Delta t) - delta_{j, pi(i)}| <= 4 sum_{V-B read links} eps*(e) = O(N_VB eps_f / N') = O(Delta t/tau_BD),

  for some deterministic reference map pi. This step is rigorous on paper, by a hybrid argument over hidden arguments.
- (d) Over many steps the same order holds [W, sketch]. The argument needs approximate uniformity of the evolved B values, which holds because each site's update is eps*-close to a single-site update.

**Consequence.** Under (viii) + (xi), or under observer-uniform H-BD, a bound on D-to-B influence is a bound on all hidden-to-visible influence at the cut. At tau_BD ~ 1/H the visible law at the cosmological cut is within O(t/tau_BD) of a hidden-independent deterministic law. So the one-layer law T^(B) carries no boundary-specific content beyond the order of the H-BD correction itself.

Above the q-threshold, the only rules compatible with H-BD are "passive-majority" rules. Their uniform (maximal-entropy) states are dynamically inert per link at ~1e-183. Those rules lie outside (vii), on which SM's dispersion and Main sec. 3.2's channel results rest.

There is no formal conflict with the h-bar calibration: GR:130, :144 and :679 state that sec. 8.5(b) and the Step 4 matching do not use Step 2. What conflicts is Step 2/Step 4's narrative identification of boundary modes "across which H_int couples" as the dynamically relevant sector.

**Route 2 (typicality).** The H-BD fraction is a property of the rule under counting, not of states, so typicality over states cannot lower it. Where it is small, R2 shows the uniform state is inert on every link.
- Conclusion: closed.
- Support: paper (R2).

**Route 3 (observer-relative partition).** Defining B as everything that influences V within the window gives B = B_n, which is the cone form. It is not circular, but it is not thin. Requiring B to be thin is then the whole of H-BD.
- Conclusion: closed.
- Support: logical.

**Route 4 (restated (C2)).**
- (C2-slow) is a statement about motion or mixing. Item 3 shows that motion does not give influence (C0).
- A (C2) that bounds influence is H-BD under another name, a relabelling with no gem content.
- Adding it to Main would put a downstream-motivated premise into Main, which the Main-independence rule bars.
- Conclusion: closed.
- Support: logical.

**Q1 conclusion.** H-BD does not follow from OI's principles. Under partition-relativity plus homogeneity it is contradicted below q-threshold (R1). Above it, H-BD reduces to an inert hidden sector (R2).
- Support: paper derivation (R1 exact except [W] geometry; R2 first step rigorous, multi-step [W]).
- Conditions: counting measure; site-local bounded-range rule; observer-uniformity or (xi).

### Q2. Does it follow from independently justified physics?

- **Finite propagation speed, microcausality, LR bounds** [background: Lieb-Robinson 1972; strict cones for reversible cellular automata]. These give only the cone form; see Q1. Not sufficient.
- **Horizon causal structure and static-patch holography** [background: membrane paradigm, Thorne-Price-Macdonald 1986; de Sitter complementarity and stretched horizon, Susskind and co-workers; Banks].
  - In GR, the region beyond the event horizon never influences the static patch. That is exact one-way decoupling (tau_BD = infinity), not a 1/H law.
  - In the static symmetric lattice the cut is not an event horizon. Realizing one-wayness at an observer-relative cut is excluded by R1 for homogeneous rules.
  - The only open escape is state-dependent directional coupling (SM sec. 3.1's G(x), outside (vii)) that realizes an emergent event horizon. No corpus result supports it, and SM's area-law proof is for uniform initial conditions.
  - Static-patch holography is itself a conjecture, so importing it would be a new premise. As a candidate it has no free parameter, which is good. But it conflicts with (vii), (x) and (xi) at Layer 0, and I found no independent prediction. It fails sec. A.29.
- **Cosmological principle and de Sitter homogeneity.** These cut *against* H-BD. Any intrinsic property, of rule or state, that makes D inert holds for every observer's D, and our own interior is D for distant observers. A dynamically or thermally inert deep sector therefore contradicts our observed active interior (sketch).
  - Cross-propagation: this gives a principled reason why W1-1's extensive, thermally active deep sector (CE-RL, r ~ 7e59) is the physically relevant case rather than one possible case. It bears against H-inert in the same way. Marked ELABORATING for W1.
- **Q2 conclusion.** No independently justified physics yields H-BD. Homogeneity plus partition-relativity obstructs it.
- Support: paper argument plus [background] literature.

### Q3. Can the 1/H scaling be obtained non-ad hoc, or must it be replaced?

- **Thermal or mixing time 2 pi/H.** This is a hidden *mixing* time (tau_B), not an influence time. Using it for tau_BD repeats the R1-R4 versus R5 conflation found by item 3.
- **Gibbons-Hawking emission rate.** Total emission is O(1) quanta per Hubble time across the horizon, about 1e-183 per Planck-area mode per step. This matches R2(a)'s per-link figure.
  - Pressure-tested and rejected as support. Any rate of order H produces the same powers, so the match is dimensional, not independent.
  - The map from a counting fraction to emitted quanta is undefined.
  - It is not a sec. A.29 prediction.
  - Classification: BORDERLINE.
- **A parameter-free 1/H exists in the cone form.** The collar B_n has thickness n lattice steps, which is ct. Its thickness relative to the horizon radius is ct/R_H = tH, about 2e-33 at t ~ 1e-15 s (GR:48's tau_S). That is the "10^-32" order, up to the O(1) graph-cone versus wave-speed factor (1 versus 1/sqrt 3) that Main:424 leaves open.
  - It controls geometric thinness: the collar's outer link count equals the horizon count to relative O(tH), and curvature or near-horizon corrections are O(tH).
  - It does **not** control deviation of T from a one-layer law, or the collar's configuration count, which is n times the one-layer count (~1e28 layers at tau_S).
- **Q3 conclusion.** The 1/H in H-BD cannot be obtained non-ad hoc. It should be replaced by the geometric statement tH in the cone form, which is derivable apart from the c-calibration factor.
- Support: paper and dimensional analysis.

### Q4. Does a weaker, derivable bound suffice for the manuscript's gravitational uses?

| Use (site) | What it needs | Cone form / App. B suffices? |
|---|---|---|
| GR sec. 3.2 Step 2 (b), Step 4 "same degrees of freedom" (GR:116-130, :144) | One-layer law; stated as a consistency check, not used by sec. 8.5(b) or by the matching | Yes for "data independent of the deep volume beyond the collar". No thin-layer statement is needed by any derivation. |
| Deep-cardinality gauge corollary (GR:132-138) | Invisibility of \|C_D\| | Yes, and exactly (beyond B_n, any cardinality, App. B). H-BD adds only time-uniformity with a fixed B. |
| GR:589 theorem, finiteness clause | Finiteness of the relevant sector | Yes: C_V x C_{B_n} is finite for a finite window without any holographic bound. The H-BD clause is superfluous. |
| Sub:54, :60, :262, :268(ii)-(iii); Meth:353; ch02, ch03, ch18 | Transfer across coupled enlargements | Yes in exact finite-window form: an enlargement attached beyond B_n leaves the window data unchanged. "Leading order for all t << tau_BD" is not derivable. |
| Sub:92, Sub:268(i) (E3 cutoff \|C_V x C_B\| <= e^{A/4}) | A thin, area-scaling relevant sector | No. Neither H-BD nor the cone supplies it, and see the new marker below. |
| A.7 (GR:791-797), tau_B^D ~ 1/H | D frozen for about 1/H | Not an H-BD use. Same unsupported 1/H; the R2-type transfer also bears on it (marker below). |

**Q4 conclusion.** Every load-bearing gravitational use is carried by the cone form plus App. B, in exact, window-dependent form. H-BD's only non-replaceable content is time-uniformity with a fixed one-layer B, which no load-bearing derivation uses (consistent with P7(iii)). The E3 thin-layer cardinality reading is unsupported with or without H-BD.

**New assumption-watch marker E3-VOL.** In the selected lattice model, the visible sector of the Hubble interior has about 1e182-1e183 sites (Main:224's (L_H/eps)^3), with q >= 2 and K = 6 components per site. So log\|C_V\| is about 1e183, far above S_boundary ~ 1e122. E3 read as a dimension cutoff on C_V x C_B (Sub:92, :268(i); GR:589; ch18:178 / FULL:4909) is therefore not satisfied by the model's own visible configuration space, independently of B's thickness. My grep of papers, book and verification found no record addressing this. Novelty needs reviewer confirmation.

***

## 4. Classification

| Item | Result | Support class | Conditions | Output class (sec. A.31) |
|---|---|---|---|---|
| H-BD from OI premises | Not derivable | Paper | — | CONFIRMING (extends P3) |
| R1 exact threshold | eps_f < 1/q forces a trivial rule (observer-uniform H-BD) | Paper derivation; geometry [W] | Counting measure; (viii), (ix), (x); observer-uniformity | NEW |
| R2 transfer | H-BD implies hidden influence at the cut is O(t/tau_BD); the boundary channel is not separated | Paper (step 1); multi-step [W] | Adds (xi) and the terrace count N' ~ cA | NEW |
| Routes 2, 3, 4 | Closed | Paper / logical | — | NEW (2), CONFIRMING (3, 4) |
| Causality / LR / holography | Give the cone form or exact one-way decoupling, not H-BD | Logical + [background] | — | CONFIRMING |
| Homogeneity versus an inert D | Obstructs; supports W1-1's extensive case | Paper sketch | E4 / de Sitter homogeneity | ELABORATING (W1) |
| 1/H via the GH rate | Dimensional coincidence | Dimensional | — | BORDERLINE |
| tH geometric thinness in the cone form | Parameter-free replacement for 1/H (geometry only) | Paper; O(1) calibration open (Main:424) | c = graph or wave speed | POSITIVE |
| Weaker bound sufficiency | Cone + App. B suffice for every load-bearing use | Paper trace | E3 reading excluded | POSITIVE |
| E3-VOL | E3 cutoff conflicts with the lattice visible count | Arithmetic | — | NEW (marker) |

S/C/L layer: H-BD stays a named posited conditional (C at best), ad hoc at 1/H. Correctness bands are unchanged; this is a consistency-axis result.

***

## 5. Earliest unsupported step

In the thin-boundary chain, the earliest unsupported step is the assumption that per-link deep-to-boundary influence can be small while boundary-to-visible influence is not. That assumption is H-BD's content beyond the cone. Under partition-relativity plus homogeneity it is not merely unsupported: it is contradicted below threshold (R1) and reduces to an inert hidden sector above it (R2).

For the E3 chain, the earliest unsupported step is "E3, read as a dimension cutoff, bounds \|C_V x C_B\|". It conflicts with the lattice count of C_V (E3-VOL).

***

## 6. Smallest discriminating next step (proposed only; needs separate authorization)

**Computation.** An exact, exhaustive integer enumeration testing R1 and R2.
- *Rules.* Translation-invariant second-order rules x_i(t+1) = F(x_{i-1}, x_{i+1}) - x_i(t-1) mod q, which are bijective for every F, on 1D rings (q = 2: 16 rules; q = 3: 19683 rules). Then symmetric nearest-neighbour F on small 2D tori (q = 2).
- *Quantities, at several cuts.* The H-BD fraction eps_f (maximum over fibers), the per-link eps*(e), and the one-step hidden-influence distance.
- *Decision rule (fixed in advance).* R1 is refuted if some rule has eps_f < 1/q and a non-empty G_phi. R2 is refuted if the one-step inequality fails.
- *Controls.*
  - Linear F reproduces GR:128's eps in {0} or [1/2, 1].
  - C0 gives eps_f = 1/2.
  - Countercontrol: a rule switched off only across the cut must satisfy H-BD and violate the transfer inequality. This shows the inequality is not vacuous.

The run is cheap and local. The exact threshold lemma is also elementary enough to be a kernel candidate.

**Paper step.** Decide whether a measure-form H-BD (L10) with a non-uniform deep law can coexist with maximal-entropy B and homogeneity. That is the only escape R2 leaves open.

***

## 7. Limitations

- None of the new results is independently reviewed.
- The terrace geometry and N' ~ cA are [W]. The multi-step part of R2 is a sketch.
- The analysis is limited to counting-measure H-BD and site-local bounded-range rules.
- R1 assumes H-BD is meant as an observer-uniform law. If the owner intends one privileged partition, only the (xi) version (R2) applies.
- Literature is [background] and was not retrieved.
- GR App. A's link-variable and H-link component readings are covered only by remark: the dependence argument is invariant under site-wise relabelling.

***

## 8. Manuscript inaccuracies found (listed, not edited)

1. **The 10^-32 figure.** GR:130, ch07:46, appendix-b:192, their FULL mirrors and GR.tex:892 say the correction is "10^-32 for laboratory processes". That holds only for t ~ 1e-15 s (GR:48's tau_S). In general the correction is 2tH, about 1e-18 at t = 1 s.
2. **Finiteness attributed to holographic bounds.** GR:589 says C_V and C_B are "finite by holographic entropy bounds". In the lattice model, finiteness for a finite window needs no holographic bound, and the holographic bound read as a cutoff is exceeded by the lattice's \|C_V\| (E3-VOL). The same tension appears at Sub:92, Sub:268(i) and ch18:178 / FULL:4909.
3. **Main:224.** It equates "the number of distinguishable positions" with \|C_V\| ~ 1e183. For the site-factorized lattice, log\|C_V\| is about 1e183, so positions and configuration-space cardinality are conflated. Owner or reviewer check advised.
4. **tau_B^D in App. A.** GR:763-769 and :791 leave tau_B^D undefined ("D-sector timescale") and assert tau_B^D ~ 1/H ~ 1e17 s without derivation; GR:791 attributes it to sec. A.5, where it is only an order-of-magnitude assignment. Under the motion reading, item 3's R2 map (deviation 1/M as t/tau_B^D goes to 0) bears on the displayed open order \|\|D_V^(D)\|\| = O(tau_S/tau_B^D). A reviewer should check whether "open" understates it. Under the influence reading, it inherits H-BD's status.
5. **Minor.** GR:116 defines B as "within the interaction range of H_int", a Hamiltonian notion, while the lemma concerns a bijective update. The 1-neighbourhood in G_phi is the operative definition.

Scratch directory created but unused: no files were written.
