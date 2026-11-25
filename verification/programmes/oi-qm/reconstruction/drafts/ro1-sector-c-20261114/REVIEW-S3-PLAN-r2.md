ACCEPT WITH CHANGES — `S3-PLAN-r2.md` at `413af128f21c7bce788a720ddd712e945940a6fd` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused check of the S3 plan, r2

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r2.md` and `RESPONSE-S3-PLAN-r1.md`. The copies supplied to me are identical to the
  committed files.
- `S3-PLAN-r1.md` is unchanged, and `REVIEW-S3-PLAN-r1.md` is preserved as delivered.
- The full diff from r1 to r2.
- At source on `main`:
  - S-L5, S-L7 and σ12 in `amendments/MR-star.md` (ll. 584–594, 603–618, 667, 680);
  - MR-1 W1 (`preregistration.md`:519);
  - the GAP comment, #1023 c.6555169983.

## Summary

- F1(b)–(d) and F2–F9 are resolved. F3 is partly resolved.
- The owner's requirements A, B1–B3 and C are met.
- No authorization is changed, no #913 work is activated, and no new premise is introduced.
- **Two required changes.** Both are local.
  - **R1.** D-1 is not yet decisive in both directions. One reading it presupposes, a fourth one it
    omits, and one open derivation each need stating.
  - **R2.** U2's classification of the closure rules reaches into #913/#914 loci.

## 1. Disposition of F1–F9

| Finding | Status | Where in r2 |
|---|---|---|
| F1(a), condition (a) holds by definition; the lift is open | **Resolved** | Point 1 says the configuration-level conclusion "holds by the definition of *available* together with P-L3, so it is not a finding". Check 3 records the Main:588 lift as open and homes it at OB-a1. The definitional condition is gone from the closure conditions, replaced by (b′) |
| F1(b), condition (c) false on the record | **Resolved** | (e′) restricts the class-(ii) requirement to interference beyond generalized-noncontextual models (W1, `preregistration.md`:519). Point 1 records S-L1's native interference |
| F1(c), decisive test missing | **Partly resolved** | D-1 is named and made the first check. Its decisiveness needs R1 |
| F1(d), the GAP's scope and caveats | **Resolved** | §8.6 carries `K★ = {K1}`, σ1–σ13, the budget, σ12 unscreened, both caveats and the provisional token. Check 2 is indexed by P-vii (C-1; X2) |
| F1, overall: open, not closable by U4 alone | **Resolved** | §8.6: "U4 alone cannot close route M negatively". A configuration-level copy is kept apart from the full process |
| F2, negative controls need construction | **Resolved** | M-7 and M-8 are on record. M-8 is PC-1's rules on `main`; the obstruction is G★ item 3, which MR-1's README leaves unaffected. M-1 to M-3 are at class level, behind MR-1 stage 2, and their full specification is a stop |
| F3, overlap with other work | **Partly resolved** | #914 O-INS and the Codex screen are added, with a demarcation. U2 waits on owner question 4. U3 is definitional and routed. U2's scope still includes S-A1 to S-A7 (R2) |
| F4, setting independence in the criterion | **Resolved** | Dropped. It is decided per record as a property of `μ`, conditional on S5 |
| F5, the access declaration | **Resolved** | Frozen in U1 with its source re-pinned (the S-L7 → SM:252 drift is noted); K-2 and M-6 cover it |
| F6, AW-MR8 wording | **Resolved** | C-6's text is quoted, with ll. 1401–1412 checked |
| F7, tiers misapplied | **Resolved** | Tiers are route M's only. U1–U3 give an output type |
| F8, offsets | **Resolved** | Offsets are recorded as setting-dependent outputs, not interventions |
| F9, premise labels | **Resolved** | |

## 2. Is D-1 decisive in both directions?

The conditions are stated as conditional, and S-L5 is quoted accurately. Checked at
`MR-star.md`:584–594, its text reads:
- the marker "affects any later test of the carrier only through the offset `Φ_{DA} s_A`, which comes
  from its own initial content and does not depend on `s_Σ`";
- "(ii), loss of observed interference, can arise only by additive injection from regions whose
  content does not depend on the carrier".

D-1 is not decisive as written, for three reasons.

**R1(a). A fourth condition is missing: how the marker is prepared.**
- S-L5 does not say that a coupled marker leaves fringes intact. It says that the *record* causes no
  loss, and that the *marker's own initial content* can.
- Under P-iv's counting measure, "every region's marginal is uniform, so there is no ready region"
  (MR-star σ1, μ leg). The GAP's named missing element is exactly a sourced quiet, ready region.
- So, with the natively sourced marker:
  - whenever `Φ_{DA} ≠ 0`, it injects uniform, carrier-independent noise into the recombination
    region;
  - visibility can drop when the marker is coupled, by M-3's mechanism, without the record causing
    it;
  - the "no loss" behaviour holds only for a quiet marker, and a quiet marker is unsourced (an
    assumed apparatus).
- Without this condition, "If (α)–(γ) hold, native K1 recording misses observed complementarity" does
  not follow. Add (δ): the marker's preparation, either quiet (assumed) or native (noisy), and the
  geometry `Φ_{DA}`.
- The miss branch then needs a further check. With the native marker, does the noise-induced drop
  reproduce observed complementarity quantitatively? That is, does visibility fall with the marker's
  path distinguishability, and does it return under erasure as MR-1 §3.5 / T4 bookkeeping requires?
  Only a negative answer is a raw-direct miss.
- With a quiet marker, the conflict is real. But it then concerns an assumed apparatus, and should be
  reported as such.

**R1(b). (γ) cannot be decided from the corpus.**
- (γ) asks whether "the additive-field interference of S-L1 corresponds to the observed detection
  statistics".
- The corpus says this derivation is open:
  - Main:682: "a derivation of the two-slit interference pattern from the substratum dynamics is
    open";
  - Substratum:463 says the same.
- Deciding (γ) either way is a derivation, which is beyond "from the corpus only" and a §9 stop.
- So D-1 has a third outcome, "undecided at (γ)", and on the record it is the likeliest. State it,
  and stop U4 there rather than deriving.

**R1(c). (α) is not U4's to decide.**
- (α) is "P-vii read globally". The plan says that "depends on C-1". C-1 stays under #1234, and its
  test is not authorized.
- Yet §8.4 says each identification is "decided from the sources", and §8.6 says "U4 can settle
  (a′)". Deciding (α) would resolve C-1 inside U4.
- U4 must *condition* on (α), reporting D-1 per reading of P-vii, as check 2 already does. On the
  scoped reading, S-L5's K1 linearity applies only on the reference class, and a which-path marker is
  not a reference-class state.

**Fix.**
- Restate D-1 with four conditions: (α) as a conditioning reading, (β), (γ) and (δ).
- Give three outcomes, with an explicit stop at (γ): miss, empty on K1, and undecided at (γ).
- Change "U4 can settle (a′)" to "U4 can decide (β) and (δ) on paper, conditional on (α), and stops at
  (γ)".

## 3. New issues

**R2. U2 still reaches into #913/#914 loci (§9, U2 row).**
- U2 classifies "the closure rules S-A1 to S-A7" against the executability criterion. That is
  sequence, adaptivity, parallel composition, reuse, renewal, classical communication and joint
  readout.
- Whether these are natively executable is the content of #913's gates "Native preparation, settings
  and clock", "Observer-access closure" and "Composites and Bell structure". Their accountable home is
  #914 O-INS (c.6628909432).
- That sits awkwardly with §2.3's demarcation, which makes U3's closure definitional only.
- **Fix:** either remove S-A1 to S-A7 from U2, leaving their definitions to U1/U3, or limit U2 to
  reading existing records on them and routing any verdict to #913/#914 without classifying anew.

**No other new error found.**
- **No hidden authorization or activation.** Questions 1–7 ask openly. U3 routes "without
  discharging". O-REUSE and O-INS keep their status (question 5).
- **No new premise.** None is introduced. The non-functional-record stop stays (§A.29).
- **No conditional result stated as established.**
  - D-1 and the check-3 lift claim are [P] and [A-inf].
  - The check-3 sentence "the native linear step acts on field amplitudes by a non-monomial matrix"
    is correctly [A-inf]. Main:588 (`coherentLiftClass_eq_substratumClass`, `obs_not_layerFlowExecutable`)
    states the lift's operational status as open, and r2 does not go beyond that.
- **No duplication of the Codex screen.** U2 waits for it and reads its result. U3 reads its item (iv)
  and does not repeat it.
- **Question 6, the new D-1 question, is appropriate.** It asks where D-1's consequence for P-vii is reported, and it keeps
  C-1 under #1234.

## 4. The owner's requirements

| Requirement | Status | Evidence in r2 |
|---|---|---|
| **A.** Four-way separation | **Met** | (i) native mechanism; (ii) conditional interpretation; (iii) discriminating prediction (D-1 as a candidate); (iv) negative controls, fully specified on record (M-7, M-8) |
| **B1.** Acquiring coherent operations is separate from losing interference | **Met** | Point 1, with the class-(i) form of (b) noted |
| **B2.** Erasure as physical uncomputation | **Met** | R, U, I and P, the preparation included, in check 5 |
| **B3.** Fresh-cell PR and restrictions | **Met** | Point 3 with K-3 |
| **C.** Two tiers and a negative closure | **Met** | Both tiers; negative closure via (a′)–(e′), with U4's limits stated. (a′)'s wording needs R1 |

## 5. Verdict

**ACCEPT WITH CHANGES.**
- **Required:** R1 (D-1's conditions (α) and (δ), its third outcome, and its stop at (γ)) and R2 (U2's
  scope).
- Both are local to §8.4 check 1, §8.6 (a′) and §9's U2 row.
- A focused confirmation of those passages suffices.
