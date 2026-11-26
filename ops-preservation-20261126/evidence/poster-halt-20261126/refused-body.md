**Independent review of PR #1583 at `c96cff1d`: reviewer text, verbatim.**

Reviewer: a Claude reviewer agent started with a fresh context, given only the PR, the approved lane 1 scope, the owner's activation and the owner's added review requirements at #1169 comment 7184920234 and the commit; it wrote none of the reviewed work and made no GitHub or repository writes (owner decision at #1169 comment 7166418469). Redaction: no redaction. SHA-256 of the unredacted review text: `80afa3372cd1d49887dcefe2869301fca8c831dd504bab85b0204c9513379f84`. Writer responses, if any, are posted separately; acceptance is the owner's decision.

---- reviewer text begins ----

**Independent review of PR #1583 at `c96cff1d`**

**Verdict: ACCEPT WITH NITS.** The mathematics of the new steps holds, with one control that claims too much (F3). The decision rule was applied as written. The second-branch outcome holds even under the narrowest reading of the conventions. Six of the findings below are minor and should be fixed before landing: F1, F2, F3, F5, F8 and F9. None of them changes the branch outcome or the productivity verdict. F4, F6 and F7 are nits.

Reviewer setup: a read-only, fresh worktree at `c96cff1d`; manuscripts and Lean read at main `b6c6b80b`. Free disk was 33 GB. No pushes, no GitHub writes, no dispatch, no Lean build. I ran small exact sanity checks in scratch Python, listed under "Checks that passed". They are controls, not evidence.

### Per-step status

| Step | Status | Note |
|---|---|---|
| PLAN: rule verbatim, committed before REPORT | correct | The rule matches the scope record word for word (#1169 comment 7184602960). Commit order: `1fdd0907` at 06:43:40Z, then `c96cff1d` at 06:49:46Z. |
| §1 countercontrol S1 | correct | The linear part gives readout 0; S1 gives readout 𝟙. This matches A5-LA Prop. 2.6(a). |
| §2.1 p(n), period, q = 2 | correct | p(n) = (b·n(n−1)/2, b·n(n+1)/2). At q = 2 p(n) vanishes iff 4 divides n, so ord Φ = lcm(ord L, 4). |
| §2.2 Theorem A.1 with an offset; controls L = 1, 3 | correct | The orbits and orders in the controls all check. |
| §2.3 Q′ conservation; shell-splitting transfer | correct | m = ord_L(p) ≤ L−1 (SM:296), so N ≥ m+2 holds when d ≥ 2. The p = 2 bound 2^{2N−1} > 4(2^{2m}−1) holds. |
| §2.4 Q′(σ_c z) = Q′(z) − 2bNc; the proposition | correct | Each Δ-orbit meets each Q′-shell exactly once. |
| §2.4 controls (b = 0, one site over 𝔽₃, S1) | correct | |
| §2.4 control p ∣ N | gap, needs a fix | F3 |
| §2.4 real lift ([W] regularization) | correct as labelled | Write \|b\|N for bN. Its bearing on SM:811 is discussed at F2. |
| §2.4 alternative energies over 𝔽_p | gap (nit) | F4 |
| §2.5 one site, q = 2 | correct | The kernel hypotheses `[NeZero L] [NeZero q] [Fact (1 < q)]` admit L = 1 and q = 2 (and also d = 0). |
| §2.6 hydrodynamic gate | correct | On the range, Φ_c(sum) = Φ_c(x) + Φ_c(y) − C(b). This gives degree at most one for any offset. |
| §2.7 quotes Sub:102, Sub:163, SM:340, SM:493, SM:130 | correct, with a fix | All quoted text is present at the pin. The "proof reads" quotes are at SM:342, not SM:340 (F7). |
| §2.7 SM:130 and the offset; the rounded floor identity | correct | Checked residue by residue mod 3. |
| §3 classification table and pins | correct, with fixes | F1, F2, F6 |
| §3 ledger rows | correct | Site map: SM:222/:232 → X-41; SM:334/:336 → X-10; SM:811 → X-11; Sub:189/:193/:195 → X-45. No entries at Sub:159, Sub:163, SM:92, SM:130, SM:1416. Row homes for X-17, X-18, X-56 and X-81 as stated. |
| Kernel re-enumeration: six modules | correct | Under H-D's criterion (i), which counts unfolded forms: SubstratumInterfaceAudit, HydroSourceAudit, StochasticInterface, HexLatticeGas, A6Instantiation (:147, :306, :484) and WaveSubstratumUnbounded (:58). |
| §4 decision rule | correct | Applied verbatim; the second branch is reported. Residual bookkeeping: F5. |
| §5 productivity verdict | correct | The test is met. |

### Findings

**F1 (minor). Location: REPORT header, "Pin".** The header says every change between `e837e3db` and the pin "is an in-place line edit". That is true for SM.md and Substratum.md but false for Main.md. The diff `e837e3db..b6c6b80b` has a hunk `@@ -336 +336,5 @@`, so site-map lines in Main after 336 are offset by +4: the site map's M:732 is the pin's Main:736, and M:766 is Main:770. The table itself already uses the correct pin lines. Fix: correct the header sentence.

**F2 (minor). Location: §3 D5; §4 bullet 1 and the residual sentence; §7.** SM:811 specifies "a real-valued conserved energy" and says the exact rule conserves its energy "only modulo q". SM:291 asks for "a specified real positive-definite quadratic shell". So the 𝔽_p form of §2.4 is not a reading SM:811 states. It is a correct [A] fact about the exact rule.
- The stated-reading placement therefore rests on the real-lift form, which is conditional on SM:232. That form is also not the six-link A₁/H-b locus that Q4c is about.
- D5's (c) placement still stands, on firmer ground than the [W] regularization. On the real lift with b ≠ 0, Q′ is unbounded below along s, so SM:291's positive-definite precondition fails and the candidate is "not established". That meets PLAN §4's (c).
- Fix: rest D5's stated-reading (c) placement on the real-lift form. Remove "the exact form of D5" from the list of (c) placements under the stated reading and from the residual sentence, or label it as outside SM:811's stated reading. Keep §2.4's 𝔽_p proposition as an [A] result.

**F3 (minor). Location: §2.4 controls, p ∣ N.** The control says that if p ∣ N "then 𝟙 ∈ Im(A − 2I) and a fixed point exists". This is false for general symmetric, translation-invariant A with κ ≡ 2: for A = 2I, Im(A − 2I) = 0. The claim holds in C3's class (A − 2I = Δ on a ring; B0.3(e)). So "the trivialization occurs exactly on the no-fixed-point branch" claims too much. The direction that is shown is: p ∤ N implies no fixed point. Fix: restrict the control to C3's class, or state only the proved direction.

**F4 (nit). Location: §2.4, "Alternative energies".** "Over 𝔽_p, E_⊥ and E_⊥ + f(Q′_0) have non-uniform relational shells" is given without an argument. It is false at N = 1: there E_⊥ ≡ 0, and E_⊥ + f(Q′_0) = f(Q′) has shells that are unions of relationally uniform Q′-shells. For S1 my scratch check found both shell families non-uniform. Fix: add N ≥ 2, and either an argument or the named case.

**F5 (minor; honesty of the residual). Location: §4, last sentence; §7.** §4 says "the residual it leaves is stated in §7". §7 does not list D7 or D12/K3. D7 appears only in §8 item 3, and D12/K3 appears in no open or routing item. Fix: add both to §7 as residuals that do not involve Q4c.

**F6 (nit). Location: PLAN §4 class (a); REPORT D6, D12 (N ≥ 2), D13, D15.** Class (a) is defined as "by an argument that uses only the linear part L". These rows hold for every offset, but their arguments use the offset: Q′, p(n), the affine closure, and the invariant W. The placement is harmless for the rule. Fix: say that (a) is used here as "holds for every offset".

**F7 (nit). Location: §2.7, §6, §2.5.**
- The SM:340 "proof" quotes are at SM:342.
- §2.5 lists the kernel hypotheses without `[NeZero q]`. Immaterial.

**F8 (minor; §A.42 item 8). Location: REPORT §9, off-`main` table.**
- The PLAN-before-REPORT order is carried by `1fdd0907`. The table says it "lands with this record", which holds only if the PR lands with a merge commit. A squash merge would leave the order claim depending on a commit not reachable from `main`. Fix: state the merge-mode requirement, or drop any reliance on the order (PLAN already disclaims chronological weight).
- The scope record #1169 comment 7184602960, which supplies the rule's wording and the class definitions, is cited in neither file. Fix: list it as provenance.

**F9 (minor; materiality).** The D7 and D12/K3 placements are correct but degenerate.
- D7 is only at q = 2, which is not the physical alphabet. At odd prime q the period at resonance does not change with an offset (§2.1–2.2).
- D12/K3 is only on the one-site torus, where the centre-free wave rule becomes a self-term.
- The kernel theorem itself is correct. What fails is its affine analogue.
- §6 says much of this. The owner's summary table ("an affine offset changes the recurrence period at resonance"; "a concrete failure of the kernel ensemble gap") should be read with these limits.

**F10 (observation; preregistration).** PLAN discloses that the writer read the sources before committing it. The decision rule is not affected, because it was fixed by the owner beforehand. The PLAN §4 conventions were written after that reading:
- each stated reading is classified separately;
- "fails, or is not established" counts as (c);
- placements conditional on Q4c count as (c);
- the single-component uniform sector is treated as "A₁".

The outcome does not depend on these conventions. Under the narrowest reading — only the six-link A₁ sector, conditional placements counting as the rule's own wording requires — D3/D16 under R-dyn (SM:493) still give the second branch. The disclosure is adequate. The preregistration is not compromised for the verdict, but its chronology carries no weight.

### Owner review requirements (#1169 comment 7184920234, item 2)

**(i) Was the original decision rule applied correctly? Yes.**
- The text is verbatim from the scope record.
- The first branch fails, and the second branch is reported.
- The branch is robust: D3/D16 under R-dyn alone give it, and so do D7 or D12/K3 under PLAN's conventions.
- No re-scoping: the report applies the rule's text and states plainly that the text does not describe D7, D12/K3 or the exact form of D5. F5 is a bookkeeping gap in that disclosure, not a re-scoping.

**(ii) Do the findings expose limits of the rule? Yes.** The rule is binary, and its second branch assumes every (c) placement goes through Q4c, conditional on SM:232. The trace finds (c) placements that do not:
- D7 (q = 2) and D12/K3 (N = 1, q = 2) are unconditional and have nothing to do with Q4c.
- D5 under the stated reading is conditional on SM:232 and on resonance of the single-component lift (the massless operator of SM:811), not on Q4c's six-link A₁/H-b resonance. Its 𝔽_p form also does not involve Q4c, but it is not under SM:811's stated reading (F2).

So, as a scientific characterization, the rule is incomplete in two ways. The physically marginal q = 2 and one-site edge cases alone defeat its first branch. And its second-branch text misdescribes part of the residual. A characterization that fits the findings would sort (c) placements into three kinds: (α) through Q4c (D3/D16 under R-dyn); (β) through lift resonance and SM:232 (D5); (γ) edge cases at the scope boundary (D7, D12/K3). Any change to the rule needs owner approval.

**(iii) Necessity for existing results versus physical necessity.** The findings establish the first and not the second.
- What they do show: within affine rules with a uniform offset, specific statements as currently written fail or are not established when b ≠ 0 on the resonant sector. Those statements are Theorem A.1 as cited at SM:92 (q = 2); the kernel ensemble gap, through its affine analogue on one site at q = 2; SM:811's energy-shell candidate; and Stage 2(d)/Theorem 23 under R-dyn.
- What they do not show: they do not derive b = 0 or linearity from OI or from observation.
  - D5 concerns a measure that SM:811 offers only as a candidate, resting on the open stationary-law hypothesis of §4.2. The alternative-energy branch (E_⊥, or E_⊥ + f(Q′_0)) escapes it for b ≠ 0.
  - D7 and D12/K3 have no physical content at the physical alphabet and lattice size.
  - D3/D16 depend on Q4b and Q4c.
- What they do: they name what a physical-selection investigation (Q-γ) would have to explain — why the resonant uniform sector carries no offset, or why the total quadratic invariant is the energy in question — together with the conditions each placement carries. The report seeks no selection principle, and A5 remains a posit.

**U(6) (SM:493 against SM:130 and SM:340): yes, a genuine inconsistency in the manuscript text.**
- SM:493 says flatly: "The substratum dynamics is locally U(6) invariant".
- SM:130 says the custodial U(6) belongs to the real lift and that "the substratum dynamics, the threshold nonlinearity … commute with the signed permutations", with the U(6) "broken by the threshold only down to this signed-permutation group".
- SM:340/342 hold U(6) invariance only as the hypothesis H-cust, about the observer-level kinetic term.
- No exact U(6) can act on the ℤ/q alphabet at all.

The two statements cannot both hold as written. SM:493's sentence states as exact fact what SM:130 denies at substratum level and SM:340 only assumes at observer level. The inconsistency is in the status and level of the claim. It does not by itself refute Theorem 5, which is conditional on H-cust. It bears on Q4b because it decides which ambient group R-dyn refers to. It is independent of A5 and should stay a separate candidate obligation (suggested route #1029). No manuscript edit is proposed.

### Checks that passed

- **PLAN rule:** it is verbatim from the scope record, and PLAN's commit precedes REPORT's.
- **Pins:** Main, SM and Substratum are identical at `e2e2a623` and at the pin.
- **Hand checks:**
  - §2.1: p(n), N_C² = 0, and the period conditions.
  - §2.3: Q′ conservation, E(v, Av − u) = E(u, v), and the m ≤ L−1 and p = 2 bounds.
  - §2.4: σ_c's effect on E and on Q′; the one-site 𝔽₃ case.
  - §2.6: the closure algebra.
  - §2.7: sign-flip commutation iff 2b = 0; the floor identity.
- **Scratch exact controls (Python):**
  - ring orders, linear and affine: (L, q) = (1,2) → 2 and 4; (1,3) → 3 and 3; (3,2) → 6 and 12; (5,2) → 10 and 20; (3,5) → 15 and 15; (5,3) → 15 and 15;
  - S1, all 5^8 states: every Q′-shell projects onto all 78125 Δ-classes with multiplicity 1; with b = 0, every E-shell covers about a fifth of them;
  - the one-site q = 2 orbit is a 4-cycle;
  - for S1, E_⊥ and Q′_0 are conserved (on a sample), and both alternative-energy shell families are non-uniform.
- **Lean, read only:** `EnsembleDetermined` (:32) and the statements at :89, :118, :182, :191 in StochasticInterface; HydroSourceAudit :126, :137, :156; the six-module enumeration; HexLatticeGas :641, :685.
- **Q4:** "11 = 36 − 25" generators at Q4 N6(a) is confirmed.
- **Other quotes:** GR:673 and Str:308 quotes are confirmed, and `driveQ_isContinuousPath` is at SecondOrderDrive :225.
- **REPORT-r5:** the trace fills the gap that REPORT-r5 §1.4 marks as "not traced" and that §7.6 V-2 calls for.
- **Scope:** no selection principle is sought, and A5's status is unchanged. §8 lists routing items and edits nothing. The record makes no use of Q4 G1 or #1226. The commits it names as on `main` (`b6c6b80b`, `e2e2a623`, `e837e3db`) are.
- **Productivity:** consumers moved to pinned classes; (c) placements made; unrecorded uses of b = 0 exposed (SM:130's sign flips, Theorem A.1 at q = 2, SM:811 at resonance). Gem, with §2.4 as the substantive NEW finding and §2.1–2.2 and §2.5 as edge-case NEW findings.

### Limitations

- The [D] inputs (A5-LA B0.3 and Prop. 2.5; Q4 N0–N6 and outcome (iii)) were not re-derived. Only B0.1's orbit and N4's Q′ were re-derived.
- I did not audit D9, D10, D11 and D14 beyond their quoted lines.
- I did not establish whether H-D's four-module list was stale or missed entries at its own base.
- Ledger membership was checked for the listed lines only.
- Nothing was built.
- The scratch computations are controls on named small cases, not evidence for the general claims.

---- reviewer text ends ----

---
_Generated by [Claude Code](https://claude.ai/code)_