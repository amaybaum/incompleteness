*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran `controls.py` and `probe_sensitivity.py` under `python3 -I -B` (both reproduce their `.out` files byte for byte) and two of the eleven `search.py` modes (`full1 10`, `full2 5`), which reproduce their blocks of the reviewer's `search.out` apart from timings.*

# Review: Pinsker lower bound on the conditional past–future information

Object: Introduction (4a260ca9) L84, "If two values of $X_{<k}$ followed by a common present state
$X_k$, each of joint probability at least $p_0$, induce next-step laws at total-variation distance at
least $\delta$, then $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln2$ (in bits)…"; source
`papers/Main.md` L167–170 (corpus eae01647), Lemma (accessible backflow from readback), and the probe
`papers/oi_lattice_code/foundations/c4_backflow_probes.py`.

## Verdict: ACCEPT WITH CHANGES

The inequality is true, the constant is the best possible for a bound of the form $c\,p_0\delta^2$,
and the corpus proof is correct in every step and constant. None of the changes below touches the
mathematics of the bound. They concern (i) what the probe is said to establish ("certified exactly";
"exact probes"), (ii) two missing hypotheses for the strict "$>0$", (iii) the TV convention, which
the Introduction does not state although the constant depends on it by a factor 4, and (iv) the
sentence introducing the lemma, Main.md:153, and the lemma's name. Both say more than the lemma
proves.

## 1. Statement as proved, with the best constant

Let $A=X_{<k}$, $C=X_k$, $B=X_{k+1}$ be finite-valued. Let $a\neq a'$ be two values of $A$ and $c$ a
value of $C$ with joint masses $w=\Pr[A=a,C=c]$ and $w'=\Pr[A=a',C=c]$, both $>0$. Write
$P_a=\Pr[B\in\cdot\mid A=a,C=c]$, define $P_{a'}$ the same way, and let
$\mathrm{TV}(P,Q)=\tfrac12\|P-Q\|_1$. Then

$$I(A;B\mid C)\ \ge\ \frac{2\,w\,w'}{w+w'}\,\mathrm{TV}(P_a,P_{a'})^2\ \text{nats}\ \ge\ \min(w,w')\,\mathrm{TV}(P_a,P_{a'})^2\ \text{nats}.$$

So with $p_0\le\min(w,w')$ and $\delta\le\mathrm{TV}$ we get $I\ge p_0\delta^2$ nats $=p_0\delta^2/\ln 2$ bits.
That is exactly the stated bound, with no factor of 2 or 4 lost or gained.

- **With $\|\cdot\|_1$:** if $\delta_1:=\|P_a-P_{a'}\|_1\,(=2\,\mathrm{TV})$, the same bound reads
  $I\ge p_0\delta_1^2/4$ nats $=p_0\delta_1^2/(4\ln2)$ bits. Reading the Introduction's $\delta$ as an
  $\ell_1$ distance would overstate the bound fourfold, and that reading is false: the search below
  finds hundreds of thousands of violations of it.
- **Best constant.** For the family "two pasts of joint mass $p_0$ each, $P(c)=2p_0$, laws
  $((1\pm\delta)/2,(1\mp\delta)/2)$", $I=2p_0\,[\ln2-h((1+\delta)/2)]$ nats $=p_0\delta^2(1+\delta^2/6+O(\delta^4))$
  nats. So $\text{bound}/I\to1$ as $\delta\to0$. Any constant $c>1$ in $I\ge c\,p_0\delta^2$ nats is
  false, and $1/\ln2$ in bits is optimal. Interval checks: ratio $0.998329$ at $\delta=1/10$,
  $0.9999833$ at $1/100$, $0.99999983$ at $1/1000$; $1.0001\,p_0\delta^2$ is violated at $\delta=1/100$.
- **Individual, not joint, weights.** The bound needs each weight to be at least $p_0$. The sharp
  Pinsker-route quantity is the harmonic form $2ww'/(w+w')$. A version with the average weight
  $(w+w')/2$ is false: take $w=10^{-3}$, $w'=0.999$ with disjoint laws, where $I=h(10^{-3})\approx0.0114$
  bits.
- **Joint, not conditional, $p_0$.** $p_0$ must be the joint probability $\Pr[A=a,C=c]$, as the
  Introduction and Main both say. With the conditional $\Pr[A=a\mid C=c]$ the bound is false: take
  $P(c)=10^{-3}$, conditional weights $\tfrac12,\tfrac12$ and disjoint laws, where $I=10^{-3}$ bits
  but $0.5/\ln2$ would be required.
- **Conditioning in the KL terms.** $I(A;B\mid C)=\sum_c P(c)\sum_a P(a\mid c)\,D(P_{a,c}\,\|\,\bar P_c)$,
  where $\bar P_c=\sum_a P(a\mid c)P_{a,c}=P(B\mid C=c)$ is the mixture over **all** pasts at $c$,
  not only over the two specific values. The bound drops every other $c$ and every other $a$, since
  those terms are nonnegative. It then uses Pinsker against the common reference $\bar P_c$ and the
  triangle inequality $\mathrm{TV}(P_a,\bar P_c)+\mathrm{TV}(P_{a'},\bar P_c)\ge\mathrm{TV}(P_a,P_{a'})$.
  Pasts other than $a,a'$ move $\bar P_c$ but cannot break the argument, because the triangle step
  holds for any reference.

My derivation, done before reading the corpus proof:
$I\ge P(c)\,[w_aD(P_a\|\bar P)+w_{a'}D(P_{a'}\|\bar P)]$ (conditional weights)
$=wD(P_a\|\bar P)+w'D(P_{a'}\|\bar P)\ge 2wt^2+2w't'^2$, with $t,t'$ the TVs to $\bar P$ and
$t+t'\ge\delta$. Minimising $2wt^2+2w't'^2$ subject to $t+t'=\delta$ gives $t=\delta w'/(w+w')$ and the
value $2ww'\delta^2/(w+w')\ge\min(w,w')\delta^2$.

## 2. The corpus proof (Main.md:170): step-by-step check

| Step | Check |
|---|---|
| $w_a=\Pr[X_{<k}=a\mid X_k=c]$, $\bar P=\sum_a w_aP_a$ | correct: the mixture over all pasts at $c$ |
| CMI given $X_k=c$ is $\sum_a w_aD(P_a\|\bar P)$ | correct (the standard mixture or "radius" identity) |
| Pinsker: $D\ge\frac{2}{\ln2}\mathrm{TV}^2$ in bits | correct with $\mathrm{TV}=\tfrac12\|\cdot\|_1$, the convention Main fixes at L121 and the probe uses (`/2`) |
| triangle: $\mathrm{TV}(P,\bar P)+\mathrm{TV}(P',\bar P)\ge\delta$ | correct |
| $x^2+y^2\ge (x+y)^2/2\ \Rightarrow\ \ge\delta^2/2$ | correct |
| "Multiplying by $\Pr[X_k=c]$ converts conditional weights to path probabilities, each at least $p_0$" | correct: $P(c)w_p=\Pr[p,c]\ge p_0$. This uses $I=\sum_{c'}P(c')I_{c'}\ge P(c)I_c$ and drops the $a\notin\{p,p'\}$ terms, both silently. Both drops are valid. |
| final constant $\frac{2}{\ln2}\cdot p_0\cdot\frac{\delta^2}{2}=p_0\delta^2/\ln2$ | correct |

The weights that enter are the two configurations' **joint** masses, each bounded below by $p_0$.
The statement says joint ($\Pr[X_{<k}=p,X_k=c]\ge p_0$), and the proof's conditional weights are
converted to joint ones correctly. The probe also takes $p_0=\min$ of the joint masses.

## 3. Gaps and errors, each with location and fix

1. **"Certified exactly" (Main.md:170, the closing parenthetical; probe header L3 and final print
   "readback lemma certified").** This overclaims, in (a) and (b), and the instance set is weak, in (c) and (d).
   - (a) The probe computes $I$ in **floating point** (`I += float(p)*log2(float(...))`) and the bound
     as `float(best)/LN2`. It compares them in floats with tolerances of 1e-12 or 1e-9. Only $(p_0,\delta)$
     are exact rationals.
   - (b) Checking three instances is not certification of a universally quantified lemma.
   - (c) The probe's instances are not discriminating. Each one has a margin of at least about 2×, so
     the **false** bound $2p_0\delta^2/\ln2$ passes Q1, Q2 and Q5 alike. Interval re-evaluation is in
     `probe_sensitivity.py`: $c=2$ "holds" on Q1, Q2 and Q5, and is violated only on a near-tight
     instance that the probe lacks. The probe would catch an $\ell_1$ slip (factor 4), but not a
     factor-2 error in the constant.
   - (d) Q3 (the coin) is vacuous as a control for the inequality: its hypothesis never holds. It
     controls the gap detector, and its $I$ is the whole-future $I(X_{<k};X_{>k}\mid X_k)$, not the
     next-step quantity.

   **Fix.** Replace "(Certified exactly on …)" with wording such as "Instances checked in
   `c4_backflow_probes.py`, with exact laws and gaps and floating-point $I$". Make the same change at
   Intro L84, "(proved on paper, with exact probes)" → "(proved on paper; instances checked
   numerically)". Optionally upgrade the probe to interval arithmetic and add a near-tight instance,
   such as the tightness family at $\delta=1/10$, together with a countercontrol showing that $2p_0\delta^2$
   fails there. Then the probe actually pins the constant.
2. **Strict "$>0$" needs $p_0>0$ and $\delta>0$ (Main.md:167–168).** The statement does not require
   $p_0>0$, and "$\ge p_0$" with $p_0=0$ leaves the next-step laws undefined. At $\delta=0$ or $p_0=0$ the
   bound is $0$ and "$>0$" fails: the $\delta=0$ edge case gives $I=0$ exactly. A "gap" implicitly means
   $\delta>0$. **Fix:** "… for some $p_0>0$ and $\delta>0$ …".
3. **The TV convention is undefined in the Introduction (L77, L84, L90).** The Introduction writes
   $\|\cdot\|_{\mathrm{TV}}$ and "total-variation distance" without stating the ½. The constant in L84
   holds only for $\mathrm{TV}=\tfrac12\|\cdot\|_1$; under the $\ell_1$ reading it is false by a factor
   of 4. Main fixes the ½ only locally, inside a proof at L121. **Fix:** at first use in the
   Introduction, add "$\|P-Q\|_{\mathrm{TV}}=\tfrac12\sum|P-Q|$".
4. **The proof is compressed, though not wrong (Main.md:170).** It leaves unstated the drop of other
   presents and other pasts, $I\ge P(c)I_c$ with only the two terms kept, and it switches notation
   $P_a\to P,P'$ without introducing $P:=P_p$ and $P':=P_{p'}$. **Fix:** one clause, e.g. "keeping
   only the terms $a\in\{p,p'\}$ at $c$ (all terms are nonnegative), with $P:=P_p$, $P':=P_{p'}$".
5. **Optional strengthening.** The same proof gives the harmonic form
   $I\ge\frac{2}{\ln2}\frac{ww'}{w+w'}\delta^2$ bits, which reduces to the stated form when $w=w'$.
   The search confirms it: zero violations. It is not needed.

## 4. The search: outcomes and scripts

Scripts are in `S/proofrev/pinsker/`:

- `cmi_iv.py`: rigorous CMI in `mpmath.iv` (80-bit, outward rounding).
- `controls.py` (output `controls.out`): controls, edge cases and the tightness family.
- `search.py` (output `search.out`): the exhaustive grids.
- `probe_sensitivity.py` (output `probe_sensitivity.out`).

Everything ran with `python3 -I -B`.

**Decision method.** $I_{\text{bits}}\ge p_0\delta^2/\ln2 \iff I_{\text{nats}}\ge p_0\delta^2$. The
right-hand side is therefore an exact rational, and $I_{\text{nats}}$ is an outward-rounded interval.
A case is decided "holds" if $\inf I>\sup(\text{bound})$ and "violation" if $\sup I<\inf(\text{bound})$;
otherwise it is "undecided" and would need refinement. No case came out undecided. Exact ties with a
positive bound are impossible: $I_{\text{nats}}=\ln(\text{algebraic})$, which is never a nonzero
rational, by Lindemann. Every admissible pair at a common present is tested, with $p_0$ the minimum
of the two joint masses (the largest admissible $p_0$) and $\delta$ their exact ½-ℓ1 TV.

**Controls (all PASS).**
- An independent second CMI formula, $H(AC)+H(CB)-H(C)-H(ACB)$, must overlap formula 1 on every
  instance. The search aborts otherwise, and it never aborted.
- The probe's Q1, Q2 and Q5 are reproduced: $I=1$, $2/3$ and $0.0455660$ bits, with $(p_0,\delta)=(1/4,1)$,
  $(1/6,1)$ and $(1/4,1/4)$.
- The tightness family matches the closed form.
- **Countercontrols (must fire)** are evaluated on the same instances: $1.01\,p_0\delta^2$, the
  $\ell_1$ reading $p_0(2\delta)^2$, conditional $p_0$, and average weight. All four fire on every
  sufficiently fine grid.

| grid (all probabilities in $\frac1N\mathbb Z$) | pairs tested | stated bound violated | harmonic violated | CC 1.01× | CC ℓ1 | CC conditional | CC average | max bound/$I$ |
|---|---|---|---|---|---|---|---|---|
| k=1, full joint $\{0,1\}^3$, N=4,6,8,10,12,14,16 | 605,124 (N≥8) + 1,360 | **0** | 0 | 252 | 366,812 | 121,856 | 93,400 | 0.99658 |
| k=2, full joint $\{0,1\}^4$, N=4,5,6,7 | 470,256 | **0** | 0 | 0 (grid too coarse) | 301,200 | 57,024 | 12,384 | 0.98097 |
| k=1 slice (2 pasts × 2 futures + slack), N=48 | 264,652 | **0** | 0 | 152 | 242,924 | 42,394 | 108,932 | 0.99968 |
| k=2 slice (4 pasts × 2 futures + slack), N=13 | 741,264 | **0** | 0 | 36 | 306,072 | 4,572 | 31,944 | 0.99327 |
| ternary future slice (2 × 3 + slack), N=20 | 225,486 | **0** | 0 | 30 | 203,130 | 11,226 | 49,722 | 0.99794 |

A slice instance is a full joint law: the slack mass sits on a single cell at another present and
contributes 0 to $I$. Slices are therefore sufficient for a counterexample search, since $I\ge I_c$.
In total about 2.3 million (instance, pair) cases were tested: **zero violations and zero undecided**.
The maximising instances are always the tightness configuration (equal weights, $P(c)\approx2p_0$,
laws symmetric about ½, small $\delta$), and the ratio approaches 1 from below as the grid refines.
In every case the bound was also certified to be at most $H(X_{k+1}\mid X_k)$, which never failed.

**Edge cases.**
- $\delta=0$: the bound is 0, $I\ge0$ holds trivially, and the strict "$>0$" fails (item 3.2).
- $\delta=1$ (disjoint supports): the bound is $p_0/\ln2\approx1.443p_0$ bits. On the extremal
  family $I=2p_0$ bits, a ratio of $1/(2\ln2)=0.7213$. The bound holds but is not tight there; the
  sharp $\delta$-dependence is $2p_0(1-h_2((1+\delta)/2))$ on that family. KL terms stay finite
  because $P_a\ll\bar P$ whenever $w_a>0$.
- $p_0$ at its maximum: two disjoint events force $p_0\le\tfrac12$. Then the bound is at most
  $1/(2\ln2)=0.7213$ bits, while $I$ can be 1 bit (X0 uniform, X1 constant, X2 = X0). Generally the
  bound is at most $P(c)/(2\ln2)$.
- Tiny $P(c)$: $p_0\le P(c)/2$, so the bound scales down correctly. ($P(c)=10^{-3}$: $I=10^{-3}$ bits
  against a bound of $0.72\times10^{-3}$.)
- More than two pasts: covered by the k=2 grids and by an explicit three-past control.
- Comparison with the trivial bounds: the bound is $\le I\le H(X_{k+1}\mid X_k)\le\log_2|\mathcal C_V|$.
  Because it is proved, it cannot exceed them, and $\le H(B\mid C)$ was certified on every grid case.

## 5. Proof correctness versus physical interpretation

**What is proved.** The bound is a fact about any finite joint law of
$(X_{<k},X_k,X_{k+1})$: a TV gap between two positive-mass next-step conditionals at a common present
forces $I(X_{<k};X_{k+1}\mid X_k)\ge p_0\delta^2/\ln2$. It is a quantitative form of one direction of
the standard vanishing criterion. The hidden sector, bijectivity, (C1)–(C3), timescales and
"accessible windows" play no role in it. It holds for every stochastic process, realized or not.

**The reading attached to it.**
- *(C4) connection: supported.* (C4)'s operational clause, "two histories with the same present
  induce different next-step laws", is exactly the lemma's hypothesis. The lemma gives (C4)-gap ⇒
  $M_k\ge p_0\delta^2/\ln2>0$. That is the direction Main.md:608 and :717 use for (iii)⇒(ii), and it is
  correctly cited there. The "mediated through the hidden state" part of (C4) plays no role.
- *"Backflow": unsupported as a separate claim; a terminology hazard.* Main's own "three notions"
  remark (L334) defines "information backflow in the visible law" as equivalent to accessible memory
  $M_t>0$. Under that definition the lemma's name is a relabelling of "positive conditional memory".
  But Main.md:149, four lines earlier in the same §2.3, uses "information backflow" in the standard
  Breuer–Laine–Piilo sense, as a witness of divisibility failure. The corpus's own XOR example
  (Intro L232, Main L334) has $I=1$ bit and is P-divisible. So the lemma gives nothing about
  BLP-backflow or P-indivisibility, and a reader of §2.3, which is titled P-Indivisibility, can take
  "accessible backflow" in that sense. **Fix:** rename it, e.g. "Lemma (conditional memory from a
  readback gap)", or say at the lemma that "backflow" here means $M_k>0$ in the sense of the L334
  remark.
- *Main.md:153, "The following lemma shows that under (C2), information backflow occurs on
  observable timescales": stronger than what is proved.* (C2) is not a hypothesis of the lemma. And
  "on observable timescales" is assumed, because the gap is posited in the accessible window, not
  derived. The lemma converts a posited gap into an information bound. Whether (C2) makes such a gap
  occur is the separate content of the fast-bath lemma's contrapositive and the C2-necessity theorem,
  and it is not established by this lemma. **Fix:** "The following lemma converts a readback gap
  in the accessible window into a lower bound on conditional memory at that order."
- *Intro L84, "Two further bounds tie memory to the hidden sector".* The Pinsker bound itself
  mentions only the visible law. It ties memory to the hidden sector only when combined with Theorem
  2(c), giving $\log_2|\mathcal C_H|\ge p_0\delta^2/\ln2$. That is a valid one-line corollary and is
  worth stating if the "hidden sector" framing is kept.

## 6. Bearing on the broader framework

- The (iii)⇒(ii) direction of the characterization theorem (Main.md:608, :717) rests on this lemma.
  The lemma is sound, so that direction is unaffected. Only the qualitative consequence ($>0$) is
  used there, which needs the hypotheses $p_0,\delta>0$ (item 3.2).
- Assumption-watch marker: the same "instances certified exactly" phrasing, with float-computed
  entropic quantities, may recur at other "(Certified exactly … in `*_probes.py`)" parentheticals in
  Main (L208, L324, L330, L451, L462, L500, L512, L590). I did not audit them. Each should be checked
  for whether "exactly" refers to exact rational arithmetic throughout or only to the laws, and for
  whether its instance set discriminates the constant it is said to certify.
- The two senses of "backflow" (memory versus BLP divisibility) recur corpus-wide: Main L80, 149,
  153, 167, 172, 174, 492, 722. That is a propagation item (§A.25) if the naming is changed.

## 7. Comparison with the audit (matrix row I-103; evidence E2-09, E2-10)

I wrote this section after the verdict above. The audit directory is not in the eae01647 checkout, so
I read it at `a44003a02` (latest audit commit) via `git show`, read-only.

**What the audit records.**
- I-103 is classed as proved-paper and **IMPRECISE**, with scope "two positive-probability histories
  with a common present".
- Its load-bearing links are: (1) the probe, described as floating-point CMI on chosen families; (2)
  Pinsker [CT06]; (3) the paper proof at Main.md:167.
- E2-09 (pass, reproduced): the probe's instance values Q1–Q5 are re-certified exactly or by interval
  in the audit's own script.
- E2-10 (fail): "with exact probes" (L84) and "Certified exactly" (Main.md:170) describe a
  floating-point probe on named instances. The fix proposed is R-03 (drop "with exact probes" at L84
  and narrow L30), with CON-25 covering Main.md:170.

**Agreement.**
- I agree with all of it. My item 3.1(a)–(b) is E2-10 found independently.
- My controls reproduce E2-09's values: Q1 $I=1$, Q2 $2/3$, Q5 $I\in[0.045566]$ against $0.022542$.
- The audit's conclusion that "the bound itself stands" is confirmed here by an independent
  derivation, by the optimal-constant analysis, and by an exhaustive interval-arithmetic grid search
  of about 2.3 million cases with zero violations.
- The IMPRECISE (not WRONG) classification matches ACCEPT WITH CHANGES.

**What this review adds that the audit items do not record.**
- (a) **The probe's instance set does not discriminate the constant.** The false bound
  $2p_0\delta^2/\ln2$ passes Q1, Q2 and Q5. So even an exact re-run of those instances (E2-09) is no
  check on the factor, and E2-09's "pass" should be read as "instance values", which its own `limits`
  field says.
- (b) The constant $1/\ln2$ is **optimal**. The bound/$I$ ratio tends to 1 on an explicit family.
- (c) The strict "$>0$" in Main.md:168 needs $p_0>0$ and $\delta>0$, which the audit row's scope
  ("positive-probability histories") supplies but the Main statement does not.
- (d) The Introduction never defines TV as $\tfrac12\|\cdot\|_1$, and the $\ell_1$ reading makes
  L84 false by a factor of 4.
- (e) Main.md:153 ("under (C2) … on observable timescales") and the lemma's name "accessible
  backflow" claim more than the lemma proves, and "backflow" is used in two senses within §2.3.

**R-03's proposed L84 text.** "(proved on paper) [Main §2.3; CT06]" is adequate and consistent with
this review. I would add the TV convention at first use (item 3.3).
