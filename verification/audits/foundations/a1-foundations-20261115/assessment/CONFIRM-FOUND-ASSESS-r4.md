# Focused confirmation of FOUND-ASSESS-r4

**Reviewer.** The independent, non-author reviewer of r1, r2 and r3.

**Scope.** Paper-only and read-only. The check runs against `REVIEW-FOUND-ASSESS-r3.md` (G1–G14) and the sources at `main` `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6` already read for that review. No computation and no Lean build.

**Verdict: CONFIRMED WITH NITS.**

All fourteen G items are applied at the locations §7 gives. Three of the four re-derived arguments are correct as written, and the fourth (G5) is correct for its qubit example. Two one-clause corrections are needed:

- **H1.** G5's general sentence is stated too broadly, and the same breadth reaches §0 and C5.
- **H2.** A cut in C5 dropped the "total finiteness" qualifier from the periodicity consequence.

Neither needs another review. Nits H3–H7 follow.

***

## 1. G items in r4

| G | Location in r4 | Confirmed? |
|---|---|---|
| G1 | §0 ("Classicality, not finiteness …"); §2b.2 ("One further constraint, at L-C per window"); §2b.4 FR(L-C) row | Yes. "Constrains nothing per window" is restricted to L-T, L-H and finite L-I tables. The L-C constraint is attributed to classicality (Main:326–334, `isDiag_Phi`; E13, E14). The infinite or continuum carrier case is marked "plausible, not proved (#914 §4)" in §2b.2. The FR(L-C) row omits that qualifier; see H3 |
| G2 | §0 ("three places"); §2b.1 L-H row; §2b.2; §2b.4 FR(L-H, all time) row | Yes. Main:642 is cited in one direction only, and "converse not on record" is stated. The entropy-rate argument is §2 below; its status tag is H4 |
| G3 | §2b.1, "Relations between the levels" | Yes. The argument is correct and tagged "reviewer's argument, re-derived" |
| G4 | §2b.2, invariance criterion | Yes. The class-invariant reading is stated, Sub:268 (iii) is cited for the transfer direction only, and statements true of every finite representative are separated out |
| G5 | §0; §2b.4 FR(L-T, all time) row; C5; §2b.4 "Standing" | Applied, with the generality slip H1. The point about compatibility with #1007's decision is correctly placed in §2b.4 and C5 |
| G6 | §2b.1, L-W row; "L-C does not imply L-W"; §2b.5 step 2 | Yes. The argument is correct. On "(kernel)" see H5 |
| G7 | §2b.1, L-H row | Yes |
| G8 | §2b.1 | Yes (Sub:249) |
| G9 | §2b.3, every-q row | Yes |
| G10 | §5, Q-R "Separates" | Yes |
| G11 | C5′ heading | Yes |
| G12 | C2 | Yes (#1169 c.6876591512) |
| G13 | §1.4, thermodynamic route | Yes |
| G14 | §2b.1, L-H row | Yes |

***

## 2. Second reading of the four re-derived arguments

### G2 — entropy rate 0 under FR(L-H, all time): correct

In a fixed finite representative with deterministic dynamics and a fixed prior, every passive visible block $X_0\ldots X_{n-1}$ is a function of the initial microstate. So $H(X_0^{n-1})\le H(S_0)\le\log\lvert S\rvert$ for every n, and the rate $\lim H/n$ is 0. The same holds conditionally on each root.

**Status.** The sentence in §2b.2 carries no tag (H4).

### G3 — fibre-dependent relabelling preserves every passive multi-time law: correct as written

We have $\pi_V(\pi\varphi^t\pi^{-1})(x_0,h_0)=\pi_V\varphi^t(x_0,\sigma_{x_0}^{-1}h_0)$. The map $(x_0,h_0)\mapsto(x_0,\sigma_{x_0}^{-1}h_0)$ preserves every root law times the uniform hidden prior, so all passive multi-time laws agree. The scope is correct: under the uniform prior, more generally under a prior invariant under each $\sigma_v$, with passive reads only. Interventions that change v break the correspondence, and r4 says so.

**Status.** Tagged "reviewer's argument, re-derived". Correct.

### G5 — the qubit example is correct; the general sentence overreaches (H1)

**The example.** $\sin^2(\omega t/2)=(1-\cos\omega t)/2$. If $\cos\omega t$ has period M in integer t, then the value at t = 0 gives $\cos\omega M=1$, so $\omega M\in2\pi\mathbb Z$ and ω/2π is rational. The converse is immediate. Correct.

**The general sentence.** "FR(L-T, all time) … excludes exact unitary dynamics whose eigenphase differences are not all rational multiples of 2π" is false as written. A frequency can be absent from every $T_{ij}$. For example, take $U=\mathrm{diag}(1,e^{i\theta})$ in the configuration basis with θ/2π irrational: then $T(t)=I$ for all t, which is periodic. More generally, a term $e^{-i(E_k-E_l)t}$ drops out of $T_{ij}(t)$ when the overlaps $V_{ik}V_{jk}V_{il}V_{jl}$ vanish, or when degenerate gaps cancel.

**Status.** Tagged as re-derived; the generality is the problem, not the status.

### G6 — `ST3_pairC` agrees at L-H: correct as written

Both permutations satisfy $\varphi^2=1$, so $X_{t+2}=X_t$ pointwise. The rooted passive law is then fixed by the root law and $T(1)$, and equality of Φ_1 gives equal $T(1)$. This uses the uniform hidden prior of `familyAt`.

**Status.** Tagged "re-derived". Correct.

***

## 3. Consistency of §0, §2b, §5 and C5

**Agree:**
- §0's five levels match the §2b.1 menu.
- §0's "three places" plus the classicality constraint match §2b.2.
- §0's statement of FR's relation to #1007's decision and to the exact target matches §2b.4 and C5.
- Q-R's "Separates" matches §2b.4's statement that window-level FR cannot separate C5 from C5′.

**Disagree:** C5's "Physical consequences" against §2b.4 (H2).

***

## 4. New errors from the cuts

**H2 — C5 "Physical consequences".** r3 read: "Under total finiteness exact recurrence follows". r4 reads: "Rooted maps and passive laws are exactly periodic (§2b.4), which excludes exact dynamics with incommensurate spectra". The qualifier was lost in the cut.

C5 includes a per-patch form. There N depends on the experiment's duration, and no single finite representative serves all time. So per-patch finiteness does not imply all-time periodicity. §2b.4 ties periodicity to FR at the all-time level, which is the total form.

*Fix:* "Under total finiteness (or FR at the all-time level), rooted maps and passive laws are exactly periodic …", plus H1's qualifier.

**Other cuts.** I found no further error in §1.4 (grid, Q-G block), §3, §5 (Q-D and Q-G shortened, with their content kept in §1.4) or §7.

***

## 5. Nits and required fixes

| Id | Kind | Where in r4 | Change |
|---|---|---|---|
| H1 | required | §2b.4 FR(L-T, all time) row; §0 "excludes exact dynamics with incommensurate spectra"; C5 "Physical consequences" | Qualify as "dynamics in which an irrational eigenphase difference appears in some $T_{ij}$ (for example, generically, or under (G2)–(G3))". Keep the qubit example |
| H2 | required | C5 "Physical consequences" | Restore "under total finiteness (or FR at the all-time level)" |
| H3 | nit | §2b.4 FR(L-C) row | Add "proved for finite classical representatives; plausible, not proved, for infinite ones (#914 §4)", matching §2b.2 |
| H4 | nit | §2b.2 entropy-rate sentence | Tag it "reviewer's argument, re-derived" |
| H5 | nit | §2b.1 L-W row ("involutions (kernel)"); §7 G6 | `hC` and `hC'` are local facts inside the kernel-checked proof of `ST3_pairC`, not exported theorems. Write "established inside the kernel proof of `ST3_pairC`" |
| H6 | nit | §6 "Lean statements read" | Add SemigroupTransfer.lean:749 (`ST3_pairC`, `pairC_wordTraces`) and RootedClassification.lean (`PPer`, `FiniteRootedRealizable`), which r4 relies on |
| H7 | nit | §6 "Unreviewed arguments" | Add the four reviewer arguments re-derived by the writer (G2, G3, G5, G6). After this confirmation each has had two readers, with H1 applied to G5's general sentence |

***

## 6. Balance

- The null option remains a candidate, not a verdict (§0, C0, Q-A).
- Finiteness remains open.
- §2b adopts no premise and gives no recovery credit.
- The classicality point (G1) is stated as a constraint that applies to every classical representative. It is not a verdict against C5 or for C0.

***

## 7. Not checked

- EF-1 r7, off `main`.
- The Theorem 23 trace, which is under separate review.
- External literature.
- No Lean build; Lean statements were read from source in the previous review.
