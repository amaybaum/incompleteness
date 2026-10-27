*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran them under `python3 -I -B`, and the re-run outputs are the `.out` files.*

# Review: Bell ceiling for a screened local completion (Main §3.3, corpus at eae01647)

## Verdict: ACCEPT WITH CHANGES

The theorem is Bell's theorem (Bell 1964, CHSH 1969) applied to a deterministic completion. Its
ingredients are a coupling-graph cone that supplies ontic parameter independence, determinism that
supplies outcome determinism, and hypothesis (iv), which states measurement independence directly.
Under the strong readings of its hypotheses given below, the proof is correct. The cone lemma is
correct for a finite site set, which is the framework's standing setting (SM L44, L60: "a
deterministic bijection on a finite set").

No change is needed to the mathematics. The changes concern the statement and its scope:

- The title's key term, "screened", is undefined.
- Hypotheses (ii) and (iii) are each loose enough as written that models satisfying the literal
  wording reach CHSH = 4. Exact counterexamples are given below.
- Hypothesis (iii), read literally ("before the post-setting cones meet"), is stronger than the
  proof needs. It is also stronger than the condition the Corollary invokes, so the Corollary does
  not follow from the theorem as literally stated.
- The binary-outcome and no-post-selection premises are implicit.
- The "Certified in check 11" attribution overstates what that check computes.
- "Exactly two hypotheses remain … must choose between them" needs to be phrased as an inclusive
  disjunction over stated premises.
- Separately, the Corollary's identification of the graph-cone speed with $c$ is in tension with
  SM's own dispersion. That bears on the claim that the reference graph cannot supply option (a).

## 1. The statement as proved

**Setting.** Site set $V$ is finite. Each $S_i$ is finite. $S=\prod_{i\in V}S_i$, and $\varphi:S\to S$
(a bijection in the framework, though bijectivity is not used). $D(i)=\{j:\exists s,s'$ differing
only at $j$ with $\varphi(s)_i\neq\varphi(s')_i\}$. $G_\varphi$ is the symmetrization of
$i\to D(i)$, and $d$ is its graph distance.

**Lemma (cone), as proved.** For finite $V$, every $k\ge0$ and every $i$, $(\varphi^k(s))_i$ is a
function of $s|_{B(i,k)}$.

*Proof check.* For finite $V$, single-coordinate insensitivity outside $D(i)$ implies that
$\varphi_i$ factors through $s|_{D(i)}$: change the coordinates outside $D(i)$ one at a time. The
induction is then
$\varphi^{k+1}_i(s)=\varphi_i\big((\varphi^k(s))_{D(i)}\big)$, with each $(\varphi^k(s))_j$ a
function of $s|_{B(j,k)}$ and $\bigcup_{j\in D(i)}B(j,k)\subseteq B(i,k+1)$. This is correct.
Symmetrization only enlarges the balls, which is harmless. Nearest-neighbour structure is not used.
"Finite propagation" here means only that the propagation is one edge of $G_\varphi$ per step;
there is no bound in any metric other than $d$.

I checked the lemma independently and exhaustively on an actual reversible local map (an 8-site
ring with a two-sublattice Toffoli-type rule, $2^8$ states, $k\le3$): it holds (probe C0). The
corpus's own cone check (`coupling_graph_exact_causal_cone`) does not run a map. It composes the
declared dependency sets, which is the induction itself, so it reproduces the claimed formula and
does not test it.

**Theorem, as proved.** The hypotheses that make the proof go through are these.

- (i′) **Determinism.** The pre-setting state $s\in S$, the deterministic interventions and the
  dynamics fix the outcomes.
- (ii′) **Interventions local in both reading and writing.** At step $t_0$ the setting operation is
  $\iota_{a,b}=u^A_a\times u^B_b\times\mathrm{id}$ on $S_{A}\times S_{B}\times S_{V\setminus(A\cup B)}$,
  with $u^A_a:S_A\to S_A$ and $u^B_b:S_B\to S_B$. Equivalently, both interventions read only their
  own region of the pre-setting state.
- (iii′) **Local readouts outside the remote setting's cone.** Wing $A$'s outcome is
  $q=f_A\big((\varphi^{k_A}\iota_{a,b}s)|_{R_A}\big)\in\{\pm1\}$, and similarly for $B$, with
  $d(B,R_A)>k_A$ and $d(A,R_B)>k_B$.
- (iv) **Measurement independence.** $\Omega$, taken as $s$ or as any response-complete function of
  it, satisfies $p(\Omega\mid a,b)=p(\Omega)$ for all $a,b$.
- **Unconditioned correlators.** $E(a,b)=\sum_\Omega p(\Omega)\,q_a(\Omega)r_b(\Omega)$, with no
  post-selection on detection or coincidence.

Then $q=q_a(\Omega)$ and $r=r_b(\Omega)$, and $|S_{\rm CHSH}|\le2$. The proof is the stated one:
the lemma gives $\partial q/\partial b=0$ and $\partial r/\partial a=0$ pointwise in $\Omega$;
determinism gives point masses; (iv) gives one weight; and
$q_0(r_0+r_1)+q_1(r_0-r_1)\in\{\pm2\}$ pointwise. Every step checks.

**What each hypothesis contributes.**
- (i) makes outcome independence automatic. It is also implicit in "$\Omega$ fixes each wing's
  response to every setting", so (i) and the definition of $\Omega$ overlap.
- (ii) and (iii) give ontic parameter independence, through the lemma.
- (iv) *is* measurement independence. It is assumed, not derived.

The theorem therefore does not replace any Bell hypothesis with something weaker. Its one piece of
added content is that the dynamics' own dependency graph certifies parameter independence. The text
says as much ("Bell's theorem applied to the framework's own hypotheses"), and that framing is
accurate.

## 2. Gaps, with locations and fixes

**G1. "Screened local completion" is undefined (Main:360, title).** The preceding sentence
introduces "operational setting screening" only by contrast, and no definition follows. The
evident intent is that a completion is *screened* iff (iv) holds, with $\Omega$ response-complete.
*Fix:* define it in one clause, or retitle the theorem "Bell ceiling for a measurement-independent
graph-local deterministic completion". The Explainer (L1017) uses "screened graph-local". Use one
term corpus-wide.

**G2. (ii) "supported in the respective regions" is ambiguous (Main:360, hypothesis ii).** If
"supported" means only "writes only in its region", the theorem fails when the interventions are
applied in sequence.

*Counterexample CE2 (exact).* Take $V=\{1,2,3,4\}$, $A=\{1,2\}$, $B=\{3,4\}$ and
$\varphi=\mathrm{id}$, so $G_\varphi$ is edgeless and no cones ever meet. Use the pre-setting state
$s_2=s_3=\lambda$ with $\lambda$ uniform, independent of the settings. Apply
$\iota_a: s_1\leftarrow a$, then $\iota_b: s_4\leftarrow b,\ s_3\leftarrow s_3\oplus(b\wedge s_1)$.
The readouts are $q=s_2$ and $r=s_3$. Then $r=\lambda\oplus ab$: this is a PR box, with CHSH = 4
exactly. Hypotheses (i), (iii) and (iv) hold, and $\iota_b$ writes only in $B$. If the interventions
read the *pre-setting* state simultaneously instead (CE2′), CHSH = 2.

*Fix:* state (ii′). Each intervention is of the form $u_a\times\mathrm{id}$ and reads only its own
region, or both act simultaneously on the pre-setting state. The proof's "the cone statement makes
the A-readout independent of the B-intervention" silently uses this.

**G3. (iii) does not localize the readout, and its cone condition is the wrong one (Main:360,
hypothesis iii; Main:358, last sentences).**

(a) *Readout locality.* Nothing says the $B$ outcome is a function of a region $R_B$ alone.
*Counterexample CE3:* the same 4-site model with a $B$ readout map $r=s_3\oplus(s_1\wedge s_4)$
gives CHSH = 4 at $k=0$.

(b) *The condition.* "Readout occurs before the post-setting cones meet", read as the forward cones
$B(A,k)$ and $B(B,k)$ meeting, requires $d(A,B)>2k$ when the readout regions lie inside the setting
regions. The proof needs only $d(A,R_B)>k_B$ and $d(B,R_A)>k_A$: each remote setting's forward cone
must not reach the local readout region. That is the relativistic Bell condition (setting at A
spacelike to outcome at B), and it is weaker by a factor of 2 in time. The literal (iii) therefore
excludes valid configurations, including tests whose outcomes are registered after half the
light-travel time.

The Corollary (Main:394) and Substratum L130 invoke "spacelike-separated" wings, which is (iii′),
not (iii). So "the theorem above applies" does not follow from the theorem as literally stated. The
lemma paragraph's "the corresponding causal cones" (Main:358) can be read correctly, which makes
the mismatch a wording defect.

*Fix:* replace (iii) with (iii′) as displayed in §1.

**G4. Outcome alphabet and post-selection are implicit (Main:360 statement, "$|S_{\rm CHSH}|\le2$").**
The bound needs $q,r\in\{\pm1\}$ (or $[-1,1]$) and unconditioned correlators. *Exact control CE4:*
local deterministic tables with outcomes in $\{-1,0,+1\}$ (0 meaning no detection), weights
independent of the settings, and correlators conditioned on coincidences reach CHSH = 4. Without
conditioning the pointwise maximum is 2. *Fix:* add "with $\pm1$-valued outcomes recorded in every
run". This is a precision point. It matters only where the corpus maps the theorem onto
experiments, where the detection loophole is closed empirically, not by the theorem.

**G5. The lemma's finiteness should be stated (Main:358).** The induction's first step needs
$\varphi_i$ to factor through $s|_{D(i)}$, which single-coordinate insensitivity gives only for
finite $V$.

*Counterexample CE1 (analytic, infinite $V=\mathbb Z$).* Let
$\varphi(s)_1=s_1\oplus\big(s_2\wedge g(s_{\le-2})\big)$, with $g=1$ iff $s_{\le-2}$ is not
eventually zero, and let $\varphi$ be the identity elsewhere. This $\varphi$ is a bijection, and
$D(1)=\{1,2\}$, because $g$ is insensitive to any finite change. The interventions are
$\iota_a:s_{\le-2}\leftarrow(a,a,a,\dots)$ in $A=\{j\le-1\}$ and $\iota_b:s_2\leftarrow b$. With
$q=s_{-1}=\lambda=s_1$ and $r=\varphi(s)_1=\lambda\oplus ab$, CHSH = 4, while $A$ is isolated in
$G_\varphi$. A hub variant with unbounded degree defeats finite-region interventions as well.

This is out of scope for the framework's finite substratum. It matters only if the lemma is cited
for $\mathbb Z^3$ or continuum-limit analyses. *Fix:* add "$V$ finite (or: each $\varphi_i$ factors
through a finite $D(i)$, $G_\varphi$ is locally finite, and interventions have finite support)".

**G6. Certification overstated (Main:377, "Certified in … check 11").** Check
`bell_ceiling_screened_deterministic_local_completion_is_2` does three things:

- It verifies exhaustively the pointwise CHSH value of the 16 deterministic tables. This is exact
  and correct.
- It samples 4000 floating-point mixtures, which is redundant by convexity.
- Its controls (b) to (d) are vacuous or hard-coded:
  - (b) is a hand-typed correlator dictionary, not a setting-dependent ensemble of local tables.
  - (c) sets `I_lambda = 0.0` by assignment, so `coarse_defect` equals `dep_reaches_4`.
  - `withdrawn_would_allow = (2*sqrt(2) > 2.0)` is a constant truth.

  No part of the check exercises the theorem's actual content: the reduction from cone, locality
  and the common ensemble to factorized response functions. Under the repo's own rule, a control
  that "merely reproduces the claimed formula" or is vacuous does not license a verdict.

*Fix:* say "the pointwise CHSH bound over the 16 deterministic tables is checked exhaustively in
check 11". Replace (b) with an explicit ensemble. For example, two response tables chosen by
setting give CHSH = 4 at $I(\Omega;Z)=0.811$ bits exactly; my probe derives this rather than
asserting it. Compute $I(\lambda;Z)$ from the model in (c). Optionally, add a run of an actual
$\varphi$ with local interventions as a positive control, plus CE2 and CE3 as countercontrols for
(ii′) and (iii′).

**G7. "Exactly two hypotheses remain available and the framework must choose between them"
(Main:389).** The logic is the contrapositive: CHSH > 2 implies that at least one of
(ii′)/(iii′) and (iv) fails. With (ii′) and (iii′) together read as ontic parameter
independence, that yields (a) or (b). Three corrections are needed:

1. The disjunction is inclusive. A completion can fail both, so "must choose between" overstates
   the exclusivity. "At least one must be given up; the framework gives up (a)" is accurate.
2. "Exactly two" is exact only relative to the theorem's stated premises. The implicit premises
   from G2 to G4 are read-local and simultaneous interventions, local readout, $\pm1$ outcomes
   without post-selection, and one classical probability space over single outcomes. Failure of
   the first two is a form of (a). The third is closed experimentally, not by the theorem. The last
   is constitutional, with determinism. Saying so turns "exactly two" into a correct statement.
3. "Determinism is constitutional" is correct as a premise (the bijective substratum) and does the
   stated work: it removes outcome-independence as a third option.

**G8. Corollary (Main:394): the cone speed is identified with $c$ (bears on "the reference
nearest-neighbor graph alone cannot supply option (a)").** The Corollary assumes "maximum lattice
propagation speed identified with $c$". The graph cone moves at 1 edge per step, and the exact
dependency front is attained for the linear second-order update with unit $\alpha$: one shortest
path along an axis gives the coefficient $\alpha^k\ne0$.

SM:230 itself states that the stable, isotropic observer-level lift ($\alpha=1/d$) has
long-wavelength speed $1/\sqrt d$ edges per step, and that converting the cone into a physical $c$
"belongs to the emergent clock/length calibration". My probe samples the Brillouin zone and finds
the maximum group velocity of $\cos\omega=\tfrac13\sum\cos k_j$ to be $1/\sqrt3$ to sampling
precision. If $c$ is the emergent wave speed, the graph cone moves at $\sqrt3\,c$. Wings spacelike
with respect to $c$ but separated by less than $\sqrt3\,c\,\Delta t$ are then *inside* $G_\varphi$'s
cone, the theorem does not apply to them, and the reference graph's exact dependency already
reaches the remote readout.

So the Corollary is correct as a conditional, but its antecedent conflicts with SM's dispersion
unless the cone speed and the emergent light speed coincide, which SM's formula says they do not.
*Fix:* either state the Corollary with "wings separated by more than the graph-cone speed (1 edge
per step) times the setting-to-readout interval", and note that this is $\sqrt d$ times the
emergent $c$ under SM's calibration; or supply the calibration argument that identifies them.
Substratum L130 ("pointwise causal cone with maximum propagation speed $c$") and Main abstract
L22/L630 ("not by itself a Bell-violating completion") inherit this.

## 3. Counterexample attempts

The probes are in `bell_review_probes.py`, beside this review. They were run with
`python3 -I -B` and use exact `Fraction` arithmetic for the Bell values.

| Attempt | Exploits | Satisfies (i)–(iv) as written? | CHSH |
|---|---|---|---|
| C0: actual reversible local ring map, exhaustive | (positive control, lemma) | yes, strong reading | lemma holds |
| CE1: tail-dependent $\varphi$ on $\mathbb Z$ | "depends … for some state" with infinite $V$ | yes; outside the finite-substratum scope | 4 (analytic) |
| CE2: write-local, read-nonlocal sequential intervention | (ii) "supported" | yes, weak reading of (ii) | **4** |
| CE2′: same, simultaneous pre-setting reads | (control) | yes | 2 |
| CE3: readout map reading the remote register | (iii) has no readout region | yes | **4** |
| CE4: no-click outcomes, coincidence post-selection | implicit $\pm1$, unconditioned | MI holds; $S$ redefined | 4 (conditioned); 2 unconditioned |
| Setting-dependent ensemble of 2 local tables | (iv) fails (control) | no | 4 at $I=0.811$ bits |
| Stronger-than-needed (iii) | factor 2 in time | — | (iii) excludes valid tests |

No model satisfying the strong readings (ii′), (iii′), (iv) and $\pm1$ outcomes with finite $V$
exceeds 2. That cannot happen, because under those readings the statement is Bell's theorem. Every
violation found exploits definitional looseness, not a flaw in the argument.

I also checked the measurement-dependence bound (Main:398). The steps
$S\le2+\sum_z2\,\mathrm{TV}_z\le2+8\sqrt{\ln2\,I/2}=2+4\sqrt{2\ln2\,I}$ (Pinsker, then Jensen),
with $I=\mathrm{avg}_zD(p_{\cdot|z}\|p)$, are correct, and so is the threshold
$(3-2\sqrt2)/(8\ln2)=0.030941$ bits. "Not claimed tight" is appropriate: my explicit 4-valued
example needs 0.811 bits.

## 4. Correctness versus interpretation

**Proof correctness.** Under (ii′), (iii′), (iv), finite $V$ and $\pm1$ unconditioned outcomes,
the theorem and the lemma are correct. The (b) information bound is correct. The PR-box negative
control (dropping the intervention/locality structure) is correct.

**Interpretation, which the proof does not establish.**

- *Measurement independence in a closed deterministic universe.* If $\Omega$ is the full
  pre-setting microstate, the settings are functions of $\Omega$, so $I(\Omega;Z)=H(Z)$ and (iv)
  fails automatically. The information bound is then vacuous: at 2 bits it is $\min\{4,\dots\}=4$.
  The theorem is meaningful only with $\Omega$ the response-relevant part (the coarsest
  response-complete variable, the response table), counterfactual responses defined by
  intervention on the setting generators' outputs, and (ii) as an idealization of the generators.
  "The framework keeps measurement independence" is therefore a posit about the initial
  condition and the dynamics: the response tables decorrelate from the generators' outputs. Nothing
  in the corpus derives it. It should be labelled a posit, as "the option taken" implicitly does,
  not presented as a consequence. Whether the option is "superdeterminism" in the pejorative sense
  is a matter of interpretation; the mathematics only prices it ($I_{\rm ont}\ge0.031$ bits).
- *Ontic parameter dependence with operational no-signalling.* This is a fine-tuning condition in
  the sense of Wood and Spekkens (New J. Phys. 17, 033002, 2015): any causal model that reproduces
  Bell violations through parameter dependence must tune $p(\Omega)$ so that the marginals hide the
  dependence. H-Bell's "preserve operational no-signaling" is exactly that tuning requirement, and
  the corpus does not cite the result. Calling (a) "not an operational signal" (Main:391) is a
  requirement, not a property shown for any SM/GR construction.
- *"Locality".* The theorem's locality is $G_\varphi$-locality. Its relation to relativistic
  locality is the cone-speed calibration in G8. "The cone is kept" (Intro L134) and "spacelike"
  (Corollary) coincide only under that calibration.

## 5. Bearing on the broader framework

1. **The cone speed versus $c$ (G8)** is the substantive cross-paper finding. Under SM's own
   observer-level dispersion, the reference NN graph's dependency cone is $\sqrt3$ times faster than
   emergent light. The blanket claim that the reference graph "cannot supply option (a)" (Main:394,
   abstract L22, L630; Substratum L130) is then conditional on an unproved calibration. In the
   window between $c$ and $\sqrt3\,c$ the reference graph supplies ontic dependence as it stands,
   along with a risk of operational signalling faster than $c$ at the substratum level.
   Experimental timing margins in loophole-free tests are, as I recall them (unverified), well
   below a factor of $\sqrt3$. Which way this cuts, for or against the framework, is undetermined.
   It needs to be stated either way.
2. **Option (a) relocates the burden to H-Bell plus fine-tuning.** Preparation-indexed long edges
   are, by the definition of $G_\varphi$ ("for some state"), already edges of $G_\varphi$. So under
   (a) the global coupling graph is non-local, and "the reference vacuum graph remains local" is a
   statement about a sub-ensemble of states, not about $G_\varphi$. This is consistent with the
   theorem but worth saying, since §3.3 also asserts that "the graph read from the actual dynamics"
   is the locality witness.
3. **Assumption-watch marker.** Several corpus sentences treat "keeps measurement independence" as
   free. In a closed finite deterministic universe it is a property of the initial condition that
   needs a mixing or decorrelation posit, for which C2 mixing is the natural candidate. It is not
   derived anywhere I could find.
4. **Intro §3.5 (L134–136).** "A deterministic completion that keeps pointwise causal cones and a
   setting-independent pre-setting ensemble is Bell-local … must give up one of the two." This is
   correct given G2 to G4, and "pointwise causal cones" must carry (ii′) and (iii′). "Adopts
   ontic parameter dependence, in which one wing's microstate response depends on the remote
   setting without operational signalling" defines (a) with no-signalling built in, and the next
   clause says compatibility with no-signalling is open. That borders on assert-then-qualify.
   Better: "… adopts ontic parameter dependence; whether it can be realized without operational
   signalling and with the continuum limit is the open hypothesis H-Bell".
   **Intro §6.1 (L175).** "With measurement independence kept, they need ontic parameter
   dependence" is correct given determinism and the implicit premises. "Not accounted for by memory
   alone" is correct: hidden memory is part of $\Omega$ and does not change the bound.

## 6. Comparison with the audit matrix (read after the verdict above was written)

Source: `origin/audit/intro-corpus-20261026`, `MATRIX.md` L446–447 and L603–604, and
`matrix/part-B2.json` and `part-B4.json`. That directory is absent from the eae01647 corpus copy.
All four rows are rated FAITHFUL, proved-paper, traced-only.

| Row | Audit | This review | Agreement |
|---|---|---|---|
| I-168 (L136: cones + setting-independent ensemble ⇒ Bell-local) | FAITHFUL; hypotheses "determinism; pointwise causal cones (interventions local, readout before cones meet); setting-independent ensemble"; chain link "certified in … check 11" | Faithful to Main, and true under (ii′)/(iii′)/$\pm1$/finite $V$. The source theorem's literal (ii) and (iii) admit CHSH = 4 (CE2, CE3), and its literal (iii) is stronger than needed (G3b). Check 11 does not test the reduction (G6). | **Agree on FAITHFUL and proved-paper.** Disagree with two details. (1) The audit's note "response-fixing microstate, automatic for a deterministic completion's full state" is true for response-fixing, but with $\Omega$ the full state, (iv) fails automatically whenever the settings are dynamically generated. $\Omega$ must be the response-relevant part, with counterfactuals defined by intervention (§4). (2) The chain link repeats "certified in check 11" without qualification; it should read "pointwise bound checked; reduction proved on paper". |
| I-169 (L136: must give up one of the two) | FAITHFUL; rests on Main:379/389 "exactly two hypotheses remain", link proved | Correct as an inclusive disjunction relative to the theorem's premises. "Exactly two" and "must choose between them" need the G7 qualifications. The Intro's "give up one of the two" is the better wording. | **Agree** that the Intro sentence is faithful and correct. The audit should not cite Main:389's "exactly two … choose between" as a proved link without the implicit-premise list. |
| I-249 (L175: not accounted for by memory alone) | FAITHFUL, with the note on the locality qualifier | Same reading: hidden memory is part of $\Omega$. | **Agree.** |
| I-250 (L175: with MI kept, need ontic parameter dependence) | FAITHFUL; assumptions "deterministic completion; MI" | Correct given determinism and the implicit premises. Under G8, "parameter dependence" relative to $G_arphi$ may already hold for the reference NN graph if the cone speed exceeds the emergent $c$. That bears on Main's claim that the reference graph cannot supply (a), not on this Intro sentence. | **Agree.** |

**Not in the audit rows.** The audit records no counterpart to these findings:

- the definitional gaps in Main's theorem (G1–G5);
- the vacuity of check 11's controls (G6);
- the cone-speed versus $c$ tension in the Corollary and in Substratum L130 (G8);
- the fine-tuning (Wood–Spekkens) character of H-Bell's no-signalling requirement (§4).

The audit's row I-008 independently notes that "deterministic completion" is undefined in the
Intro's Bell sense. That matches G1, and the fix belongs at the source, Main:360.
