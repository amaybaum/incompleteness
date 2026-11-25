> **Superseded.** This revision of the #1245 H-BD report is superseded. The authoritative report is `REPORT-r5.md` in this directory; its change map is `CHANGES-r5.md`.

# #1245 H-BD: origin and derivation of the deep-to-boundary influence bound (resumed paper-only round), revision r3

## Status, pin, sources

- **Status.** Paper-only, read-only research under the existing authorization (owner, 2026-11-12, "Let's open an issue to investigate its origins, and try to find a proper derivation."), resumed by owner decision 2026-11-25 (#1245 comment 7163939634). Nothing is adopted and no manuscript, Lean or premise change is made. No computation was run for this report. The new results below are hand derivations and are not machine-checked.
- **Review status.** Revision r1 (commit `e9872d62`) was independently reviewed at PR #1564 comment 7166704115 (verdict REVISE). This revision r2 applies the owner's bounded revision decision (amaybaum, #1245 comment 7166798992, 2026-11-25T15:24:39Z: "Proceed with a bounded revision addressing the review findings. [...] Return the corrected report for independent review before acceptance."). The r2 corrections are not yet independently reviewed. The multi-step argument of R2(d) is the reviewer's derivation; the writer checked it step by step (sec. 3, R2(d)). The terrace-geometry proof of R1 is the reviewer's; the writer checked it (sec. 3, R1). Items marked [W] are the writer's own unverified steps; [background] marks external literature cited but not retrieved.
- **Revision r3.** Revision r2 (commit `a00e1dd6`) was independently delta-reviewed at PR #1564 comment 7167216051 (verdict ACCEPT-WITH-NITS); the statements in this section and in sec. 7 that the r2 corrections are not yet independently reviewed describe r2 before that review. r3 applies the owner's decision (amaybaum, 2026-11-25, coordinating session), quoted: "Preserve the exact P3 evidence in the version-controlled research package, with its provenance and original reference. Verify that the two classifications genuinely follow from that evidence. If either classification cannot be independently supported, narrow it or mark it unresolved. Ensure that all evidence supporting the final report will be present on `main` when the package lands. Obtain a bounded independent delta review and complete CI on the corrected head. Do not reopen the accepted mathematical results or expand the H-BD investigation." The P3 comment is preserved verbatim in P3-EVIDENCE.md. r3 changes only the passages that rest on P3 (sec. 1 P3 row and off-`main` references; sec. 2 C-4; sec. 3 R1 contribution and R2(a) comparison; sec. 4 R1 output class), restores r1's qualifier in sec. 8 item 4 and applies citation nit 6 of the delta review; no mathematical result is changed. The r3 changes are not yet independently reviewed.
- **Pin.** `main` at `e2e2a623265187a28ebec604ab8bcc672742888f`.
- **Sources read.**
  - AGENTS.md at the pin.
  - #1245 body and all 11 comments (as read for r1); comment 7166798992 (owner decision on r2); comment 6818702013 re-read in full for r3 (P3-EVIDENCE.md).
  - #1244 comments 6817631738 (item 3 audit), 6818164393 (posit record), 6818792755, 6820568979, 6821450454, 6824919310, 6880017798, 6880703935.
  - `papers/GR.md` sec. 2.1, 3.1-3.2, App. A (A.5, A.7) and App. B.
  - `papers/Main.md` sec. 1.4, 3.2, 3.3, 4.5 (posit ledger) and 4.6.
  - `papers/Substratum.md`:54, 60, 80, 92, 262, 268.
  - `papers/Methodology.md`:353.
  - Book mirrors: ch02:44/144, ch03:220, ch07:46, ch18:170/178, appendix-b:169-210, appendix-c:106; FULL:4909, FULL:6261.
  - Verification records on `main` that cite H-BD (listed in sec. 1), and `verification/audits/foundations/a1exit-ledger-20261120/LEDGER.md` row X-74.
  - The independent review of r1 (PR #1564 comment 7166704115).

***

## 1. What has already been done (do not repeat)

| # | Work | Where (commit / record) | Result | Support class |
|---|---|---|---|---|
| P1 | #1244 item 3 audit of GR sec. 3.2 step (ii) | #1244 c.6817631738, at `1b273698` | Step (ii) inferred small influence from small motion; a frozen D still drives B (C0 = (v+b, b+d, d)). Explicit counterexamples C0, C1', C2, C3 under 5 of 7 readings of tau_B, none under R5 (D-to-B influence) or R6. GR:813's measure form does not recover the lemma. The A.5 step-(i) display is refuted (R2 form). A.7 is valid only on its own hypothesis. | Hand-checked examples; two internal reviews |
| P2 | Posit record | #1244 c.6818164393 | H-BD is a named posited hypothesis; tau_BD is not fixed | Owner decision |
| P3 | sec. A.29 check of H-BD | #1245 c.6818702013, preserved verbatim in P3-EVIDENCE.md; the full check it mentions is session material and is not in the repository | (a) eps = Delta t/tau_BD per step, and bijectivity suffices. (b) **Linear dichotomy:** for affine phi on a finite abelian group, eps is in {0} or [1/2, 1], at every B thickness and every power; under ledger (vii), H-BD with tau_BD > 2 Delta t holds iff L = 0. (c) 1D ring: eps = 1/2. (d) Local nonlinear rules need sigma >~ 1.4-4 x 10^2 for tau_BD ~ 1/H, assuming sigma = ln q_c. (e) C-4: H-BD does not bound A.5's channel terms. (f) The cone form is the parameter-free baseline. It records that H-BD "conflicts with Main ledger items (vii), (x), (xi) and (xiii) at site-local cuts with D→B dependence". Verdict: ad hoc at 1/H; otherwise a conditional placeholder. | Paper derivations; internal review |
| P4 | Owner record | #1245 c.6818793241 | Recorded "conditional, not explanatory, A.5 not recovered, cone baseline" | Decision |
| P5 | Manuscript correction | PR #1248, merged as `0cf85e21` (commits `42115ca2`, `501dba1c`, `9483f4f9`, `ccf73468`) | GR sec. 3.2 now carries (a) the exact cone form, (b) H-BD as posited with the linear dichotomy (GR:112-138), A.5 narrowed with its order open (GR:757-769), App. B for any deep cardinality. Substratum, Methodology, book and FULL carry H-BD. | On `main` |
| P6 | W1 entropy-slope investigation and W1-1 | #1245 c.6818970549, c.6828106610 (L current, C alternative), c.6831591590, c.6835701280, c.6841976574; `verification/programmes/physical-realization/w1-1-20261112/` (r4 accepted; merged via #1265 as `c3b5f37a`) | W1 is an additional physical assumption. Counterexample for reading L. An extensive deep sector gives C_D/2s_B ~ 7e59. H-inert, H-eq and W1' remain unadopted. | Paper; reviewed (r4) |
| P7 | A1-programme audits that touch H-BD | `verification/audits/foundations/r1-l8-stage0-20261120/AUDIT.md` (F2; the C4 trace); `a1-remainder-20261119/REMAINDER.md` C4/L10; `a1-09-dependency-census/CENSUS.md` D25/C08; `p7-shell-calibration-20261116`:84; `a1-free-p7-coupled/DECISION.md` row 4; `a1exit-ledger-20261120` X-73/X-74 | (i) The counting step of GR:126 uses \|f^-1(S)\| <= \|S\| for injections. A measure-theoretic H-BD (L10) needs fibrewise non-expansion of the deep law and is open. (ii) H-BD controls absolute row error only, so it is insufficient for P7's log-ratio and energy-derivative needs. (iii) **None of H-BD's consumers reaches an ACC consequence; every one concerns invisibility of deep-sector cardinality.** (iv) X-74 queues deletion of Sub:268(i)'s sentence "This reading is the interpretive premise of A1." | Paper audits on `main`; WIP status as stated there |
| P8 | M9 assignment | #1245 c.6880025217; LEDGER-r5 sec. 10 | M9 is the energy-shell mechanism (W1), not H-BD itself | Planning |

**Off-`main` references (sec. A.42 item 8).** Each reference above to an Issue comment, a pull request or session material is classified by the claim it is attached to.
- P1, P2, P4, P6 (Issue comments), P8: **provenance** for this report's results. No result of sec. 3 uses their content as a premise. The C0 example used in sec. 2 is on `main` at GR:128 (**support on `main`**).
- P3 (#1245 c.6818702013): **support** for the statements of this report about what P3 records, carried in this package as P3-EVIDENCE.md (the exact comment body, its SHA-256 and its provenance), so that it is on `main` no later than this report. These statements are limited to what that text records: R1's contribution relative to P3 and its output class (sec. 3, R1; sec. 4), narrowed in r3; R2(a)'s comparison with P3(d) (sec. 3, R2(a)), whose novelty relative to P3 is unresolved in r3; C-4, which sec. 2 reports as P3's finding and this report does not re-derive; and the P3 row, Routes 1 and 5, the agreement of GR:128 with P3 (sec. 2) and "extends P3" (sec. 4), each checked against the preserved text. For the mathematics P3 is **provenance**: R1 and R2 are derived in full below and use no P3 content as a premise. The full check that the comment calls session working material was not found in the repository (all branches and their history searched); no claim of this report uses it, so it is **provenance** only.
- P5: on `main` (`0cf85e21`); **support on `main`** for every GR/Substratum line cited.
- PR #1564 comment 7166704115 (the independent review): **provenance** (credit) for R2(d) and the terrace-geometry proof. Both arguments are reproduced in full in this report and checked by the writer, so the claims rest on the text below, not on the comment. The review's exhaustive enumeration (q = 2, 1D ring, one cut; a scratch script, not on `main`) is provenance only; R1 does not rest on it.

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
  - Small motion does not bound influence (C0, GR:128).
  - P3 reports that H-BD does not bound channel or purity terms (C-4: an update with eps = 0 whose two-step V-channel fully dephases under Main:280's rho_H = I/m; P3(e), preserved in P3-EVIDENCE.md, not re-derived here).
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

**Result R1 (exact threshold at the single GR cut, under ledger (xi)).**
- *Setting.* phi is site-local with bounded read sets (A3, ledger (ix)), nearest-neighbour range (x), site factorization (viii), and center independence (xi): the update commutes with lattice translations up to site-wise gauge. The cut is the single horizon cut that GR posits for the observer's worldline (GR:122, GR sec. 2.1): V is the cosmological ball of radius R_H and B its 1-neighbourhood. H-BD holds at that cut with fraction eps_f = Delta t/tau_BD.
- *Hypotheses.* q is the number of values of the neighbour data that the site function reads (the size of the read component's range, not of the full site alphabet). With read range r > 1, the threshold below becomes 1/q^k for a site whose read set contains k deep sites.
- *Claim.* If eps_f < 1/q, then phi has no inter-site dependence: G_phi is empty, every partition is closed, and T(t) is a permutation for all t, so (C1) fails everywhere.
- *Proof.*
  1. Take a B-site i whose only deep read-neighbour is i+e (a terrace-interior site).
  2. At any fiber (v, b), the component of the output at i varies with d only through x_{i+e}, which is uniform over q values.
  3. If f_i(a, .) is non-constant at the local assignment a realized by (v, b), its most frequent value occurs on at most q-1 of the q values, so the V x B output differs from phi^VB(v, b) on at least a fraction 1/q of C_D. Every local assignment a is realized by some fiber, because C_V x C_B is a full product. So eps_f < 1/q forces f_i to be independent of x_{i+e} at every a.
  4. *Terrace geometry* (proof from the independent review, checked by the writer). Locally approximate the ball's surface by a half-space V = {x : n.x <= 0} with outward normal n, components ordered so that n3 >= n1, n2 >= 0 (other octants by symmetry). Then B = {x : 0 < n.x <= n3}, and a B-site's deep neighbours are the x+e_j with n.x + n_j > n3. The site has +e3 as its only deep neighbour iff 0 < n.x <= n3 - max(n1, n2). For normals in the open cap where n3 > max(n1, n2), the values n.x are equidistributed over the layer, so these sites make up a fraction (n3 - max(n1, n2))/n3 > 0 of the B-sites under that part of the surface. The cap has positive solid angle about each of the six axis directions, and the curvature correction for a ball of radius R_H is O(1/R_H) in lattice units. So terrace-interior B-sites facing each of the six directions exist, with N'_e ~ c A/eps_lat^2 and c = O(1).
  5. Under (xi), the site function at every site is the same up to a site-wise gauge, and a gauge relabelling preserves both the dependence on x_{i+e} and the fraction in step 3. So step 3 applied at a terrace site facing e shows that no site reads its neighbour in direction e. By step 4 this holds for all six directions, so no site reads any neighbour.
  6. Under (xiii) with (xi)'s second clause (no explicit copy of the site's present value), F is then constant, F = k, so the update is (p, c) -> (c, k - p) and T(t) is a permutation.
- *Scope.* The argument uses one site at one cut (steps 1-3) and the translation covariance of the rule (step 5); it uses no quantifier over observers. The linear dichotomy of GR:128 is the special case q prime with L != 0, which gives eps_f >= 1/2.
- *Contribution relative to P3.* The preserved P3 text (P3-EVIDENCE.md) records, in its verdict on the preserved-list criterion for H-BD, "It conflicts with Main ledger items (vii), (x), (xi) and (xiii) at site-local cuts with D→B dependence": a conflict with the four items jointly. The derivations it records are the linear dichotomy for affine phi under (vii) ("Under (vii), H-BD with τ_BD > 2Δt therefore holds iff L = 0") and the 1D-ring example; for local nonlinear rules it records only a required size, "σ ≳ 1.4–4×10² for τ_BD ~ 1/H", under the assumptions σ = ln q_c, H-link and one cell per step. It does not record a conflict with (xi) for nonlinear rules without (vii). R2(a) below gives a far stronger quantitative threshold. What R1 adds is the exact 1/q threshold for general nonlinear site-local rules at the single GR cut, under (xi) without (vii), together with the non-translation-invariant case below. Output class: ELABORATING (P3) for the linear special case (q prime, L != 0), which P3 records; for general nonlinear rules the class relative to P3 is unresolved, because the preserved text does not record that case and P3's full check is not available.

**R1 for rules without (xi) (observer-uniform case; conditional, outside GR's reading).**
- *Hypothesis.* H-BD holds, with the same eps_f, at the horizon cut of every lattice site taken as an observer position.
- *Claim.* If eps_f < 1/q, no site reads any neighbour, with no translation covariance of the rule. Proof: steps 1-3 and 6 as above; every pair (i, e) occurs as a terrace-interior site facing e for the cut centred at a suitably translated observer position (step 4 applied to that cut).
- *Status of the hypothesis.* It is not a reading of H-BD as GR states it. GR:122 posits H-BD for "the" boundary modes of the horizon cut of "the observer's worldline", with no quantifier over observers. GR sec. 2.1 and A.4 extend the h-bar calibration to every calibrated horizon, but Step 2 is a consistency check that sec. 8.5(b) does not use (GR:130, :144, :679), so no derivation requires H-BD at every observer's cut. The case further needs every lattice site to be an observer position, while Main sec. 4.6 excludes observers from fast-mixing regions. Main sec. 1.4 fixes phi and varies T with the partition; it does not require H-BD at every partition. The hypothesis is therefore an extension introduced in this report, and this case applies only to rules without (xi) under that extension. In the selected model, which carries (xi), it is not needed.
- Output class: NEW, narrowed to rules without (xi) under the observer-uniform hypothesis.

**New result R2 (transfer; under (viii), (ix), (x), (xi)).**
- (a) For each direction e, the worst-case per-link dependence fraction satisfies eps*(e) <= -ln(1 - eps_f)/N'_e, where N'_e is the number of terrace sites facing e in an independent set at the cut. Here "independent set" means that the chosen sites have pairwise disjoint V u B read sets, so that the worst-case local assignment a* can be imposed at every chosen site in one fiber. Proof: in that fiber, each chosen site's output depends on d only through its own deep neighbour; these are disjoint and independent under uniform d, and each matches any fixed value with probability at most 1 - eps*(e); H-BD gives (1 - eps*(e))^{N'_e} >= 1 - eps_f, and ln(1 - eps*) <= -eps*. This step is rigorous. An independent set is obtained from the terrace sites of R1 step 4 by thinning to a sublattice of spacing 3, so N'_e ~ c A/eps_lat^2 with c = O(1). With tau_BD ~ 1/H: eps_f = t_P H ~ 1.2e-61, N' ~ (A/4)/6, eps* <~ 3e-183. Either the rule reads no neighbour, or q >~ 3e182 (ln q ~ 420). The value ln q ~ 420 agrees with the upper end of the threshold that P3 records for local nonlinear rules ("σ ≳ 1.4–4×10² for τ_BD ~ 1/H", assuming σ = ln q_c, H-link and one cell per step; P3-EVIDENCE.md). The preserved text does not give P3's derivation, so whether R2(a) reproduces P3's result under the same hypotheses, and hence whether it is new relative to P3, is unresolved; R2(a) is derived in full here and does not rest on P3.
- (b) **The new part.** Under (xi), the per-link dependence fraction eps*(e) is a property of the rule and the direction, not of the site. So the *same* per-link bound holds for V-sites reading B-sites.
- (c) At t = Delta t, with hidden values uniform:

  sum_j |T_ij(Delta t) - delta_{j, pi(i)}| <= 4 sum_{V-B read links} eps*(e) = O(N_VB eps_f / N') = O(Delta t/tau_BD),

  for a deterministic reference map pi of C_V. Proof (hybrid argument): for a V-site reading k hidden components, draw the hidden arguments h and h' independently and swap them one at a time; each swap changes the site's output with probability at most 2 eps*, so P[f(h) != f(h')] <= 2k eps*, and since P[f(h) != f(h')] >= 1 - max_c P[f = c], there is a value c with P[f != c] <= 2k eps*. A union bound over V-sites and l1 = 2P give the display. This step is rigorous.
- (d) **Multi-step bound** (derivation from the independent review, PR #1564 comment 7166704115, adapting GR:126's injectivity argument; checked by the writer). Let C_H = C_B x C_D be finite with counting measure, and let

  delta = max over v in C_V of |{h in C_H : pi_V phi(v, h) != pi(v)}| / |C_H|.

  - Step d1. By (c), for every v the fraction is at most 2 sum_{V-B read links} eps*, because eps* is a worst case over all other arguments, V values included. So delta <= 2 sum eps*. *Writer's check:* holds; the bound in (c) does not depend on v.
  - Step d2. Fix x_i and the reference path v_s = pi^s(x_i). Let S_s be the set of initial h in C_H whose trajectory under phi has V component v_{s'} at every step s' <= s. *Writer's check:* well defined; S_0 = C_H.
  - Step d3. Elements of S_s share their V components at step s, and phi^s is injective, so their hidden components at step s are distinct: the map h -> pi_H phi^s(x_i, h) is injective on S_s. *Writer's check:* holds; two elements with equal V and equal H components at step s would have equal images under the injective phi^s.
  - Step d4. An element h of S_s leaves at step s+1 iff its hidden component g at step s satisfies pi_V phi(v_s, g) != pi(v_s). At most delta |C_H| configurations g do so, and by d3 each is the step-s hidden component of at most one element of S_s. So |S_s \ S_{s+1}| <= delta |C_H|. *Writer's check:* holds; no assumption on the distribution of the evolved hidden values is used, which removes the uniformity step of r1.
  - Step d5. After n steps |C_H \ S_n| <= n delta |C_H|, and on S_n the V component is v_n. Averaging over uniform h, sum_j |T_ij(n Delta t) - delta_{j, v_n}| <= 2 n delta <= 4 n sum eps* = O(t/tau_BD). *Writer's check:* holds, with t = n Delta t and sum eps* = O(N_VB eps_f/N') from (a).
  - *Writer's verdict:* no gap found. The argument requires finite C_H, counting measure (uniform hidden prior at t = 0) and the injectivity of phi; it inherits P7 F2's restriction to that measure.

**Consequence.** Under (viii) + (xi), a bound on D-to-B influence is a bound on all hidden-to-visible influence at the cut. At tau_BD ~ 1/H the visible law at the cosmological cut is within O(t/tau_BD) of a hidden-independent deterministic law. So the one-layer law T^(B) carries no boundary-specific content beyond the order of the H-BD correction itself.

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

**Q1 conclusion.** H-BD does not follow from OI's principles. Under ledger (xi), at the single GR cut, it is contradicted below the q-threshold (R1) and reduces to an inert hidden sector above it (R2).
- Support: paper derivation (R1 exact, terrace geometry checked; R2 one-step and multi-step steps rigorous on paper, the multi-step argument being the reviewer's, checked by the writer).
- Conditions: counting measure on finite C_H; site-local bounded-range rule; (viii), (ix), (x), (xi). Without (xi), R1 holds only under the observer-uniform hypothesis, which is not GR's reading.

### Q2. Does it follow from independently justified physics?

- **Finite propagation speed, microcausality, LR bounds** [background: Lieb-Robinson 1972; strict cones for reversible cellular automata]. These give only the cone form; see Q1. Not sufficient.
- **Horizon causal structure and static-patch holography** [background: membrane paradigm, Thorne-Price-Macdonald 1986; de Sitter complementarity and stretched horizon, Susskind and co-workers; Banks].
  - In GR, the region beyond the event horizon never influences the static patch. That is exact one-way decoupling (tau_BD = infinity), not a 1/H law.
  - In the static symmetric lattice the cut is not an event horizon. Realizing one-wayness at an observer-relative cut is excluded by R1 for homogeneous rules.
  - The only open escape is state-dependent directional coupling (SM sec. 3.1's G(x), outside (vii)) that realizes an emergent event horizon. No corpus result supports it, and SM's area-law proof is for uniform initial conditions.
  - Static-patch holography is itself a conjecture, so importing it would be a new premise. As a candidate it has no free parameter, which is good. But it conflicts with (vii), (x) and (xi) at Layer 0, and I found no independent prediction. It fails sec. A.29.
- **Cosmological principle and de Sitter homogeneity.** These cut *against* H-BD. Any intrinsic property, of rule or state, that makes D inert holds for every observer's D, and our own interior is D for distant observers. A dynamically or thermally inert deep sector therefore contradicts our observed active interior (sketch).
  - Cross-propagation: this gives a principled reason why W1-1's extensive, thermally active deep sector (CE-RL, r ~ 7e59) is the physically relevant case rather than one possible case. It bears against H-inert in the same way. Marked ELABORATING for W1.
- **Q2 conclusion.** No independently justified physics yields H-BD. Homogeneity of the rule (ledger (xi)) obstructs it (R1, R2); the state-homogeneity argument above is a sketch.
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

The trace covers every identified use of H-BD or of Step 2 in `papers/` and `book/` (GR:116-144, 589, 679, 873, 901; Sub:54, 60, 92, 262, 268; Meth:353; ch02:44, 144; ch03:220; ch07:46; ch18:170; appendix-b:169-210; FULL mirrors).

| Use (site) | What it needs | Cone form / App. B suffices? |
|---|---|---|
| GR sec. 3.2 Step 2 (b), Step 4 "same degrees of freedom" (GR:116-130, :144) | One-layer law; stated as a consistency check, not used by sec. 8.5(b) or by the matching | Yes for "data independent of the deep volume beyond the collar". No thin-layer statement is needed by any derivation. |
| Deep-cardinality gauge corollary (GR:132-138) | Invisibility of \|C_D\| | Yes, and exactly (beyond B_n, any cardinality, App. B). H-BD adds only time-uniformity with a fixed B. |
| GR:589 theorem, finiteness clause | Finiteness of the relevant sector | Yes: C_V x C_{B_n} is finite for a finite window without any holographic bound. The H-BD clause is superfluous. |
| Sub:54, :60, :262, :268(ii)-(iii); Meth:353; ch02, ch03, ch18 | Transfer across coupled enlargements | Yes in exact finite-window form: an enlargement attached beyond B_n leaves the window data unchanged. "Leading order for all t << tau_BD" is not derivable. |
| Sub:92, Sub:268(i) (E3 cutoff \|C_V x C_B\| <= e^{A/4}) | A thin, area-scaling relevant sector | No. Neither H-BD nor the cone supplies it; see E3-VOL below. |
| A.7 (GR:791-797), tau_B^D ~ 1/H | D frozen for about 1/H | Not an H-BD use. Same unsupported 1/H; the R2-type transfer also bears on it (sec. 8 item 4). |

**Outside the sufficiency claim.**
- The E3 row: neither form carries it. The E3 bound motivates A1, which is not adopted, so it is not consumed by a derivation; it is excluded from the claim, not carried by it.
- The physical picture behind H-count and H-slope, that the dynamically relevant modes are the A/eps^2 boundary modes (GR:98-104, Step 4). It rests on those named hypotheses, not on H-BD, and the cone form (a collar of about 1.9e28 layers at tau_S) does not support it either.

**Q4 conclusion.** Every identified use of H-BD or Step 2 is carried by the cone form plus App. B, in exact, window-dependent form. H-BD's only non-replaceable content is time-uniformity with a fixed one-layer B, which none of these uses consumes (consistent with P7(iii)). The E3 thin-layer cardinality reading and the H-count/H-slope boundary-mode picture lie outside this claim; the E3 reading is unsupported with or without H-BD.

**Assumption-watch marker E3-VOL (existing cross-corpus inconsistency).**
- *Arithmetic.* In the selected lattice model, the visible sector of the Hubble interior (R_H = c/H0 ~ 1.37e26 m) has about 2.6e183 sites at eps = l_p (about 1.7e182 at eps = sqrt 6 l_p; Main:224's (L_H/eps)^3), with q >= 2 and two values per site under (xiii). So log\|C_V\| is about 1e183 (about 3.6e183 at q = 2, eps = l_p), against S_boundary = A/4 ~ 2.3e122, a ratio of about 1.6e61.
- *The cardinality reading.* E3 is read as a dimension or cardinality cutoff on C_V x C_B at Sub:92 (dim H <= e^{A/4} bounds C_V x C_B), Sub:268(i) (\|C_V x C_B\| <= e^{S_partial}), ch18:178 / FULL:4909 (<= e^{10^122}, with the recurrence illustration \|S\| ~ e^{10^122}) and, implicitly, GR:589 ("finite by holographic entropy bounds"). Under ledger (viii), that reading is contradicted by the model's own visible configuration space, independently of B's thickness.
- *The entropy reading.* Book appendix-c:106 and its mirror FULL:6261 already state that the E3 bound is "an entropy-based bound [...] not a count of microscopic configurations", limiting the sector to e^{S_dS} *effectively distinguishable* states; Sub:80 states E3 as entropy scaling with area.
- *Classification.* The corpus disagrees with itself: appendix-c reads E3 as entropy, while Sub:92, Sub:268(i), ch18:178 / FULL:4909 and GR:589 read it as cardinality. Main:224, which equates "the number of distinguishable positions" with \|C_V\| ~ 1e183, conflates the count of positions with the cardinality of the configuration space and so feeds the confusion. The related ledger item a1exit-ledger X-74 already queues deletion of Sub:268(i)'s "interpretive premise" sentence. As physics, the tension is the standard volume-versus-area overcounting of local lattice field theories [background: Cohen-Kaplan-Nelson infrared-ultraviolet bound]. E3-VOL is therefore an existing cross-corpus inconsistency, partly resolved by appendix-c:106, not a novel discovery.

***

## 4. Classification

| Item | Result | Support class | Conditions | Output class (sec. A.31) |
|---|---|---|---|---|
| H-BD from OI premises | Not derivable | Paper | — | CONFIRMING (extends P3) |
| R1 exact threshold at the single GR cut | eps_f < 1/q forces a trivial rule | Paper derivation; terrace geometry proved (review, checked) | Counting measure; (viii), (ix), (x), (xi); q = size of the read neighbour data; 1/q^k for k deep sites read at range r > 1 | ELABORATING (P3) for the linear case (q prime, L != 0); relative to P3 unresolved for general nonlinear rules (sec. 3, R1) |
| R1 without (xi) | Same conclusion for rules that are not translation-covariant | Paper derivation | Observer-uniform H-BD at every lattice site: an extension, not GR's reading | NEW, narrowed to this case |
| R2 transfer | H-BD implies hidden influence at the cut is O(t/tau_BD); the boundary channel is not separated | Paper: one-step rigorous; multi-step rigorous (reviewer's injectivity argument, checked by the writer) | (viii), (ix), (x), (xi); finite C_H, counting measure; independent set = disjoint V u B read sets; N' ~ cA | NEW |
| Routes 2, 3, 4 | Closed | Paper / logical | — | NEW (2), CONFIRMING (3, 4) |
| Causality / LR / holography | Give the cone form or exact one-way decoupling, not H-BD | Logical + [background] | — | CONFIRMING |
| Homogeneity versus an inert D | Obstructs; supports W1-1's extensive case | Paper sketch | E4 / de Sitter homogeneity | ELABORATING (W1) |
| 1/H via the GH rate | Dimensional coincidence | Dimensional | — | BORDERLINE |
| tH geometric thinness in the cone form | Parameter-free replacement for 1/H (geometry only) | Paper; O(1) calibration open (Main:424) | c = graph or wave speed | POSITIVE |
| Weaker bound sufficiency | Cone + App. B suffice for every identified use of H-BD or Step 2 | Paper trace | E3 row and the H-count/H-slope boundary-mode picture outside the claim | POSITIVE |
| E3-VOL | E3 read as a cardinality cutoff conflicts with the lattice visible count; the corpus also carries the entropy reading (appendix-c:106) | Arithmetic; corpus trace | Ledger (viii) | ELABORATING (existing cross-corpus inconsistency) |

S/C/L layer: H-BD stays a named posited conditional (C at best), ad hoc at 1/H. Correctness bands are unchanged; this is a consistency-axis result.

***

## 5. Earliest unsupported step

In the thin-boundary chain, the earliest unsupported step is the assumption that per-link deep-to-boundary influence can be small while boundary-to-visible influence is not. That assumption is H-BD's content beyond the cone. Under ledger (xi), at the single GR cut, it is not merely unsupported: it is contradicted below threshold (R1) and reduces to an inert hidden sector above it (R2).

For the E3 chain, the earliest unsupported step is "E3, read as a dimension cutoff, bounds \|C_V x C_B\|". It conflicts with the lattice count of C_V, and the corpus already carries the competing entropy reading (E3-VOL).

***

## 6. Smallest discriminating next step (proposed only; needs separate authorization)

**Computation.** An exact, exhaustive integer enumeration testing R1 and R2.
- *Rules.* Translation-invariant second-order rules x_i(t+1) = F(x_{i-1}, x_{i+1}) - x_i(t-1) mod q, which are bijective for every F, on 1D rings (q = 2: 16 rules; q = 3: 19683 rules). Then symmetric nearest-neighbour F on small 2D tori (q = 2).
- *Quantities, at several cuts.* The H-BD fraction eps_f (maximum over fibers), the per-link eps*(e), and the one-step and multi-step hidden-influence distances.
- *Decision rule (fixed in advance).* R1 is refuted if some rule has eps_f < 1/q at a single cut and a non-empty G_phi. R2 is refuted if the one-step or the multi-step inequality fails.
- *Controls.*
  - Linear F reproduces GR:128's eps in {0} or [1/2, 1].
  - C0 gives eps_f = 1/2.
  - Countercontrol: a rule switched off only across the cut must satisfy H-BD and violate the transfer inequality. This shows the inequality is not vacuous.

The independent review ran the q = 2, 1D-ring case at one cut as a sanity check of R1 step 3 (no rule reading a neighbour had a fraction below 1/2); that run is provenance only and does not replace the controlled enumeration. The run is cheap and local. The exact threshold lemma is also elementary enough to be a kernel candidate.

**Paper step.** Decide whether a measure-form H-BD (L10) with a non-uniform deep law can coexist with maximal-entropy B and homogeneity. That is the only escape R2 leaves open.

***

## 7. Limitations

- R1 (r1 form), R2(a) and R2(c) were independently reviewed (PR #1564 comment 7166704115). The r2 corrections, including the restated R1 and the incorporated R2(d) and terrace proofs, are not yet independently reviewed.
- R2(d) and the terrace-geometry proof are the reviewer's derivations, checked by the writer; neither is machine-checked.
- The analysis is limited to counting-measure H-BD on finite C_H and site-local bounded-range rules.
- R1 in the selected model uses (xi) at the single GR cut. The case for rules without (xi) needs the observer-uniform hypothesis, which GR does not state.
- Literature is [background] and was not retrieved.
- GR App. A's link-variable and H-link component readings are covered only by remark: the dependence argument is invariant under site-wise relabelling.

***

## 8. Manuscript inaccuracies found (listed, not edited)

1. **The 10^-32 figure (clarity).** GR:130, ch07:46, appendix-b:192, their FULL mirrors and GR.tex:892 say the correction is "10^-32 for laboratory processes". GR:48 fixes the laboratory timescale at tau_S ~ 1e-15 s, where 2t/tau_BD is about 4e-33, so the figure is valid; it is a clarity issue, not an inaccuracy. Naming tau_S at those sites would fix it. At t = 1 s the correction is about 4.4e-18.
2. **Finiteness attributed to holographic bounds.** GR:589 says C_V and C_B are "finite by holographic entropy bounds". In the lattice model, finiteness for a finite window needs no holographic bound (C_V from Lemma 1; C_{B_n} a finite set of sites with finite alphabets), and the holographic bound read as a cutoff is exceeded by the lattice's \|C_V\| (E3-VOL). The same tension appears at Sub:92, Sub:268(i) and ch18:178 / FULL:4909; a correction would be reconciled with appendix-c:106 / FULL:6261, which already carries the entropy reading.
3. **Main:224.** It equates "the number of distinguishable positions" with \|C_V\| ~ 1e183. For the site-factorized lattice, log\|C_V\| is about 1e183, so positions and configuration-space cardinality are conflated. Owner or reviewer check advised.
4. **tau_B^D in App. A (partly valid).** GR:763 glosses tau_B^D as the "D-sector timescale" with the coupling chain V <-> B <-> D, so the symbol is not undefined. The value tau_B^D ~ 1/H ~ 1e17 s is only an order-of-magnitude assignment at GR:769, which GR:791 cites as sec. A.5. Under the motion reading, whether item 3's R2 map (deviation 1/M as t/tau_B^D goes to 0) bears on the displayed open order \|\|D_V^(D)\|\| = O(tau_S/tau_B^D) is a check for a reviewer, not a manuscript candidate. Under the influence reading, it inherits H-BD's status.
5. **Minor.** GR:116 defines B as "within the interaction range of H_int", a Hamiltonian notion, while the lemma concerns a bijective update. The 1-neighbourhood in G_phi is the operative definition.
