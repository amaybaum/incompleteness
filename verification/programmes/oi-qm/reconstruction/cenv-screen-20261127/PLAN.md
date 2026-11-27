# C-ENV screen: plan

**Status.** Plan, committed before any derivation. Paper only. WIP / UNVERIFIED.

**Authorization.** #1169 comment 7212372089, posted 2026-11-27T07:20:10Z through the owner's
account by the coordinating session, quotes the owner's approval (amaybaum, 2026-11-27) verbatim:
"Authorize the bounded paper-only C-ENV screen as the first Phase 2 investigation. Determine
whether the proposed invariant background is independently physically justified and whether it
permits an initially readable encoding at one registered parameter tuple." "Stop the C-ENV
investigation if either requirement fails. Do not initiate T-ENV computation without further
authorization." "SMD and C-NL remain suspended under their existing holds."

**Drafting snapshot D.** `main` at `69786da24`. Branch `research/cenv-screen-20261127`.

**Source of the question.** Phase 1 report r3 (PR #1625, accepted at
`95d7c225b2135f3393d3e421cc9329a0d185c2bc`), §3.1, and the Phase 2 preview on #1625 (comment
7210194622). The proposed background is restated in full below, so this unit's results rest on
its own text and not on r3's proofs.

## Goal link (§A.47)

Item served: the #914 central bottleneck under A1 retirement (#1169), through the first Phase 2
investigation. What this unit decides for it: whether C-ENV's proposed invariant background is
independently physically justified and whether it admits an initially readable encoding at the
registered tuple. That decides whether C-ENV stops or is eligible for an owner decision on T-ENV.
It does not decide whether dispersal, terminality or any physical mechanism exists.

## Pre-plan disclosure

Before committing this plan the writer read r3, NR-1 and Main's posit ledger. While fixing the class
definitions below, the writer noticed that a translation- and F-invariant closed subgroup whose
annihilator has rank one would give an eigenline of the update's symbol over the fraction field of
the Laurent polynomial ring. The writer conjectured that none exists for d ≥ 2. Nothing was
derived or written. The tuple below is fixed by a criterion that does not depend on that
conjecture: if the conjecture holds, it covers every d ≥ 2 equally.

## 1. Setting

- **Rule.** NR-1 §2 (U), on `main`: each site z ∈ ℤ^d carries a current value u(z) and a previous
  value v(z) in F_q, and F(u, v) = (αSu − v, u), with (Sf)(z) = Σ_j (f(z+e_j) + f(z−e_j)). This is
  the second-order form of ledger item (xiii) with the nearest-neighbour F_i of item (x).
- **Phase space.** Ω = (F_q²)^{ℤ^d}, product topology. Ω_fin is its finitely supported part.
- **Characters.** Ω̂ ≅ R² with R = F_q[x_1^{±1}, …, x_d^{±1}]. (Φ, Ψ) acts by
  χ(u, v) = Σ_z Φ(z)u(z) + Ψ(z)v(z). The dual of F is F̂(Φ, Ψ) = (XΦ + Ψ, −Φ), with
  X = α Σ_j (x_j + x_j^{−1}) (NR-1, proof of Theorem 3.3).
- **Symplectic form** on Ω_fin: ω((u,v),(u′,v′)) = Σ_z [u(z)v′(z) − v(z)u′(z)]. Its
  translation-covariant polynomial form on R² is λ(a, b) = a_1 b̄_2 − a_2 b̄_1, where the bar is
  x_j ↦ x_j^{−1}.
- **Registered tuple: (q, α, d) = (2, 1, 3).** Criterion: this is the instance the corpus makes
  explicit. It is Main §3.2's displayed update over F_2 (Main.md:296), NR-1 node 1 ("the instance
  q = 2, α = 1, d = 3 is explicit") and SM §4's d = 3 cubic substratum. It lies inside r3's T-ENV
  range (q ∈ {2, 3}, α = 1, d ∈ {1, 3}). Results proved for wider ranges are stated with their
  range. Only the registered tuple enters a verdict.

## 2. The proposed background (object under test)

r3 §3.1 (E2L) proposes "a random translation-invariant law, uniform on a Lagrangian subgroup of the
two-slice phase space", with "a closed, translation-invariant and rule-invariant Lagrangian subgroup
L" nominated "by a criterion fixed before outcomes". The class is fixed here as:

**𝒜_L** = the Haar (uniform) probability measures μ_{ξ₀+L} on cosets ξ₀ + L, where L ⊂ Ω is a
closed subgroup with
- (L1) σ_z L = L for every lattice translation σ_z;
- (L2) F(L) = L;
- (L3) Lagrangian: L = M^⊥ for an R-submodule M ⊂ R² with M = M^{⊥λ} (the translation-invariant
  stabilizer-group condition of the polynomial formalism).

A secondary reading, (L3′), replaces (L3) by "the Haar measure of L has entropy density exactly
log q", half the maximum 2 log q. Every result on 𝒜_L states which reading it uses. S1 is decided
under (L3).

For the diagnostic D1 only, **𝒜** is the wider class of probability laws on Ω that are invariant
under F and under all translations, with mean entropy density h(μ) < 2 log q. This is the
"low-entropy far field" of r3's (E2) without the Lagrangian clause.

## 3. Questions

- **S1.** At the registered tuple, is there a law in 𝒜_L that is independently physically
  justified by the criterion J of §4? J is fixed here and is not the C-ENV target.
- **S2.** At the registered tuple, is an initially readable encoding of a signal possible over such
  a background, by the criterion of §5?

## 4. Justification criterion J (fixed in advance)

A law μ is independently physically justified for this screen iff J1–J5 all hold.

- **J1 (native stationarity).** μ is a Borel probability on Ω invariant under F and under every
  lattice translation.
- **J2 (source).** μ is delivered by at least one route:
  - (R1) a principle of Main's posit ledger, applied as stated there, or in an A1-free form already
    recorded on `main`, such as NR-1's (Haar) posit and Proposition 4.3;
  - (R2) an observational input recorded on `main`, with the chain from the input to μ written out;
  - (R3) dynamical generation: μ is a limit, in a stated topology, of F^t_*μ₀ or of its Cesàro
    averages, with μ₀ itself delivered by R1 or R2;
  - (R4) a new principle stated in this unit that passes §A.29's Layer-0 test as written. It must
    be stated before outcomes, name the existing results it preserves as controls, deliver at
    least one independent prediction or postdiction beyond C-ENV, and admit no variant adjustable
    to any outcome. An R4 principle is a candidate only and is not adopted.
- **J3 (determinacy).** The route fixes μ uniquely, or fixes a family every member of which is
  carried into S2. No member is chosen after an outcome is known.
- **J4 (target independence, CC-RECON).** No premise of the route mentions a C-ENV deliverable or is
  equivalent to one. The deliverables are:
  - entropy-sink capacity, or terminality of exported content;
  - readability of an encoding;
  - supply of fresh or ready meters;
  - independence of inflowing resources (#885's acceptance rule);
  - correspondence with quantum stabilizer or Gaussian states, including "maximal knowledge" in the
    stabilizer sense;
  - success of any T-ENV or T-MON test.

  A route with such a premise is rejected, whatever μ it yields.
- **J5 (status).** Every step is proved on paper. Arguments written here are labelled P-here and
  are unreviewed. Every cited record is traced under §A.42 item 8.

## 5. Readability criterion (fixed in advance)

- **Encoding E0** (r3's single-site current-slice encoding). At the encoding time the configuration
  is ξ + a·e₀, with ξ ~ μ, a uniform on F_q and independent of ξ, and e₀ = (δ₀, 0): one unit in the
  current slice at site 0. This is r3's x(1) = aδ over the background, with r3's (x(0), x(1)) as
  this plan's (v, u).
- **Readout.** w = π_W(ξ + a·e₀), the current-slice values on a finite window W ⊂ ℤ^d, read at the
  encoding time. No time evolution enters S2.
- **Readable over μ:** some finite W gives I(a; w) = log q, so that a is recovered with probability
  1. **Weakly readable:** some finite W gives I(a; w) > 0. Both are reported.

## 6. Decision rule (outcome-neutral)

**S1.**
- **PASS:** 𝒜_L ≠ ∅ at the tuple, and some μ ∈ 𝒜_L meets J1–J5.
- **FAIL:** either
  - (F1) 𝒜_L = ∅ at the tuple, proved; or
  - (F2) 𝒜_L ≠ ∅, and every μ ∈ 𝒜_L is shown to fail J. For R1–R3 this needs a proof that the
    route does not deliver μ. For R4 it needs that no principle in the corpus delivers μ and that
    every R4 principle proposed in this unit fails §A.29's test as written. A FAIL by (F2) is
    limited to principles available in the corpus or proposed here, and the report says so.
- **OPEN:** otherwise. The undecided step is named, with the proof or computation that would decide
  it.

**S2.**
- **NOT REACHED:** S1 is FAIL by (F1): there is no background to encode over.
- **PASS:** some background μ ∈ 𝒜_L is readable over μ. If S1 is PASS, μ must be one that meets J.
  If S1 is OPEN, μ ranges over 𝒜_L, and the result is stated as conditional on S1.
- **FAIL:** no background in that range is weakly readable for any finite W.
- **OPEN:** otherwise, with the step named.

**C-ENV disposition.**
- **STOP** if S1 is FAIL, or S2 is FAIL or NOT REACHED.
- **ELIGIBLE FOR AN OWNER DECISION ON T-ENV** (not initiated) if S1 and S2 are both PASS.
- **HOLD, OPEN** otherwise, with the named steps.

**Generation.** The report's verdict lines are produced by applying this table to the recorded node
results. A verdict rendered while any control of §7 has failed is void, and the report says which
control failed.

## 7. Controls and countercontrols (each able to fail)

| ID | Object | Required outcome | Fails if |
|---|---|---|---|
| K1a | r1 §3.1's stated reason for (E2L): "the infinite analogue of a stabilizer state, compatible with S-L7" | J4 rejects the route | J classes it as justified |
| K1b | The vacuum point mass δ₀ chosen "because it makes every single-site encoding readable and supplies known ready states" (a deliberately target-motivated background) | J4 rejects the route | J classes it as justified |
| K2 | Product Haar on Ω via R1: ledger item (iv) in its A1-free form, NR-1 (Haar) and Proposition 4.3 | J1–J5 accept it (it is then outside 𝒜 and 𝒜_L, since h is maximal) | J rejects it. J would then be too strict to accept anything |
| K3 | Vacuum background δ₀ = Haar of {0} (trivially readable case) | readable with W = {0} | criterion reports unreadable |
| K4 | Product Haar background (L = Ω) | not weakly readable for any finite W | criterion reports any information |
| K5 | Outside the native class: q = 5, α = 0, any d. A candidate invariant Lagrangian subgroup is to be exhibited by direct check | the existence method used for S1 finds an element of 𝒜_L here, in agreement with the direct check | the method reports none, or the direct check fails |
| K6 | Native rule at q = 2, α = 1, d = 1: the chiral subgroup {(u, v) : u(z) = v(z − 1)} | direct check: closed, translation- and F-invariant, entropy density log q, not isotropic. The existence method detects it and rejects (L3) | the method misses it, or calls it Lagrangian |
| K7 | Orientation of F̂ and λ | F̂ agrees with NR-1, and F preserves ω by direct computation | either check fails |

## 8. Stopping bounds

- Paper only. No scripts, enumeration or numerical evaluation. A step that needs one is recorded as
  OPEN, with the computation named.
- At most ten depth-first nodes (§A.31), each closed by an explicit check with its verdict. Maximum
  skepticism goes to any branch favourable to C-ENV.
- No T-ENV content. No time-evolved window statistic g_t (t ≥ 1), no terminality and no revival is
  evaluated for any background. A node that would need one stops and is recorded as OPEN (T-ENV).
- SMD, C-NL and D-BV are not touched. No manuscript, Lean, registry or Issue edits. No premise is
  adopted.
- Stop after the S1 and S2 verdicts, or at the first failed control, which voids the verdicts.

## 9. Diagnostic D1 (non-gating, for P2-MIN)

If S1 is FAIL or OPEN, the report records, for the wider class 𝒜, which routes R1–R4 could deliver
an element, with proofs where they are standard and cheap. It then states, as precisely as the
records allow, the minimal missing ingredient. D1 never changes the S1 or S2 verdict.

## 10. Deliverables

`REPORT.md` in this directory, containing:
- the nodes;
- the verdicts generated by §6;
- the outcomes of the controls;
- D1;
- a §A.46 item 4 verification-status table;
- §A.42 item 8 tracing of every off-`main` reference.

No push and no GitHub write is made by this unit.
