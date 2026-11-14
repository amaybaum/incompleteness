# Review of `L54-r1.md` (TUNE-1 gap L5.4, paper derivation r1)

**Reviewer standing.** Independent, non-author, read-only, paper-only AI-agent review. Hand reasoning
only: no computation was made on any OI rule or model (commands are listed in §9). Nothing in the
repository or either worktree was edited, committed, pushed or posted. This is one hand review of a
[W] derivation. It is not a kernel check, an owner decision or a token.

**Objects.** `l54/L54-r1.md` (362 lines) and `l54/NOTES-r1.md` (71 lines). Sources: `main` at
`c3b5f37a` (worktree `wt-mainread`), Step 3A r3 off `main` (worktree `wt-3a`).

**Citation forms.** `L54:n` is the document under review. `P`, `AF`, `S2`, `S3`, `S4`, `3A`, `OA2`,
`M1`, `Main` are as in `L54:11–17`. In addition: `OA1:n` = `oa-1-20261112/OA-1-REPORT-r5.md`;
`HA5:n` = `states-dynamics-audit-20261024/history-architecture-v5/REPORT.md` (both under
`verification/programmes/oi-qm/reconstruction/` on `main`).

***

## 0. Verdict

**ACCEPT WITH CHANGES.**

Theorem 1 is correct. It is not a misreading of a definition. Lemmas 1–3, Theorem 1, Corollary 1a,
Proposition 2 and Lemma 5 were each re-derived by hand, including all three constants (`1/96`,
`1/48`, `1/128`), and no error was found in the mathematics. Every definition the proof of
Theorem 1 uses was opened at its source and the restatement in `L54:44–66` is exact.

The result is strong because of three things the schema fixes, and not because of any property of
heralds, laws or witnesses:
- the record is the complete history of `O` (D4, P:272–277);
- the Lüders target has conditional record laws that depend on label and class only (AF:88–91), so
  the target law of two reads is a product given the two classes;
- under an additive rule every label acts on the complete record by a fixed translation
  (Lemma A-T (a), (b), S3:62–68).

It is less of a jump from prior work than the task framing suggests. Its qualitative content is
already on `main` (§5 below): M1 Corollary A′ (M1:424–427), OA-1 nodes N2 and N3 (OA1:369–392) and
the C-MEAS control (S2:238–244). What is new is the quantitative form against `F(ε; 𝒯_R)` and the
observation that it decides the L5.4, L5.5 and L5.6 rows whatever the Q6′ witnesses are.

The changes required are to the control K1, to several statements of scope, and to one false
comparison with FC-1. None touches the proof of Theorem 1. Findings are in §7; the statement I am
willing to sign is in §8.

***

## 1. Definitions at source (task item 1)

| Object | Source read | Restatement in L54 |
|---|---|---|
| R-lin, additivity | P:72–89; S3:58, :79–80 | exact |
| Interface, H-μ, labels | P:137–148; D3 at P:242–271 | exact |
| Exchange mode; record contains `c_j`; protocols adaptive | P:155–176 | exact |
| Initial-condition mode; non-adaptive; every block labelled; compared on first `K` rounds | P:184–199 | exact |
| Causal layout is an option, not a requirement | P:206–209 | exact (hypothesis (C), `L54:239–240`) |
| D4, D5 | P:272–280 | exact |
| Target reads | AF:88–91 | exact |
| `𝔔*(σ · T)` | AF:107 | exact; gives the product-given-classes form of Lemma 3 |
| Identified tests; `𝒯_R` | AF:98–105 | exact. A test's labels "may depend on its own records" (AF:99); the constant policies are members |
| Admissible preparations; credit; `F` | AF:116–135, :274 | exact |
| Q5′, Q3′, Q6′ | AF:153–175, :269 | exact |
| T1 | 3A:783–809 | exact |

**The `ℓ = 0` reading.** The source's requirement does include the empty preparation, and the
document understates its support. Beyond AF:116, :134–135 and :389, the reviewed control rerun uses
it twice: "The empty preparation gives `TV(L_∅, p(0)) ≤ ε`" (S2:195) and "`F(ε; 𝒯_R)` at the empty
preparation gives one credited `σ` for both reads" (S2:200). Session 2 is the record S3:9–10 reports
as clean and accepted. So `ℓ = 0` is the record's own reading in a green control (C-ISO-2), not the
author's. It is still true that no sentence states it as a definition. This is not the weakest
point of the document (finding F8).

**The fallback, Corollary 1a.** It is sound independently of `ℓ = 0`. I re-derived:
- `D(Q) = TV(Q, Q̃)` with `Q̃(r, h_1, h_2) = Q(r) Q(h_1|r) Q(h_2|r)`;
- `TV(Q̃, Q̃′) ≤ 3 TV(Q, Q′)`, a second way, by the direct `ℓ¹` split
  `ab/c − a′b′/c′ = (a − a′)b/c + a′(b/c − b′/c′)`: the first term sums to at most `2t` and the
  second to at most `2t + 2t`, with `t = TV(Q, Q′)`, so the `ℓ¹` distance is at most `6t`;
- hence `|D(Q) − D(Q′)| ≤ 4t`, `Σ_r w_r(1 − α_r²) ≤ 32ε`, likewise for `β_r`, and `½ ≤ 64ε`.

The constant `1/128` is confirmed. Two conditions on its statement are in finding F4. It needs
`K ≥ 3`; T1 is posed at `K ≥ L + 1 ≥ 3`, so T1 is unaffected by which reading is taken.

***

## 2. The key lemma (task item 2)

**Re-derivation.** `Φ_F(y, x) = (x, Ax − y)` is additive on `(V × V)^Λ`. In initial-condition mode
the time-zero configuration is `r_O ⊕ c ⊕ u`, so the configuration of `O` at every tick is
`H_O r_O + H_P c + H_U u`. In exchange mode a round is `x ↦ (I − Π_C)x + ι(c_j)` followed by `τ`
additive ticks, and the record also carries `c_j`. For two label sequences fixed in advance,
`h(c′, u) − h(c, u) = H_P(c′ − c)` for every `u`. No property of the law of `u` is used. Lemma 1 is
confirmed as stated, with its hypotheses (h1)–(h4).

**(a) Adaptive labels.** For a policy whose later label is a function of an earlier record, the
record is still a bijective image of the label-free variable `z`, but the bijection is triangular:
`h_2 = z_2 + δ_2(c_1, π_2(h_1))`. The shift of round 2 depends on `h_1`. The complete-record laws of
two policies are then not coordinatewise shifts of one another, and the invariant does not survive.
Example: `z_1 = z_2` one fair bit, so `dep = ½`; the policy that shifts round 2 by `h_1` gives
`h_2 = 0` and `dep = 0`. Theorem 1 does not need the adaptive case: its four tests are constant
policies, which are in `𝒯_R` in both modes. `L54:360–362` is true as worded but should say that
Lemma 2 (i) does not extend to it (finding F7).

**(b) Heralds and postselection.** Theorem 1 uses none, and the schema leaves no way to impose one.
The empty preparation has no record to condition on. "An unheralded preparation is always
admissible" (AF:121). `F` quantifies over every `T ∈ 𝒯′` that fits (AF:127), so a family cannot
remove the four constant tests or attach a herald to them. Proposition 2 conditions on a herald on
the prefix records, and its step 2 is correct: under (C) the prefix records are unchanged pointwise
in `u`, so the accepted event is the same event and conditioning commutes with the shift of the
last round.

**(c) Laws and modes.** The proof uses H-μ and nothing else about the law. The level-set law is
offered in exchange mode only (P:255–258), where it is fixed at time zero before any exchange, so
it does not depend on the labels. Exchange mode under H-write is covered for label sequences fixed
in advance.

**What the proof closes.**

| Class (3A) | What Theorem 1 proves | Wider than the proof |
|---|---|---|
| A (R-lin, coset-uniform, init) | every member fails Q5′, hence T1, at `ε < 1/96`, `K ≥ 2` | "Proposition 2 answers the heralded-witness form directly" (`L54:312`) holds only under (C) |
| B (R-lin, exch, H-write) | the same, because the four tests are non-adaptive. Adaptive and heralded witnesses are never reached | nothing in the row, but see F4 for Corollary 1a with adaptive prefixes |
| C (level-set, non-uniform product) | the same, by H-μ alone | nothing in the row |
| D (R-nl) | nothing | nothing claimed |

For A, B and C the gap questions L5.4, L5.5 and L5.6 are answered NO because Q5′ alone fails. That
is the whole content of "closed". It is not a statement that label translations cannot supply the
gate family: `L54:152–155` (N8) records that as not derived, and it stays open. See finding F2.

***

## 3. The invariant and the target values (task item 3)

**Invariance.** The map is `T(h_1, h_2) = (h_1 + δ_1, h_2 + δ_2)` with `(δ_1, δ_2) = H_P(c′ − c)`
fixed. It is a product bijection of `G_1 × G_2`. The marginals of `T_*P` are the shifted marginals,
`T_*(P_1 ⊗ P_2)` is the product of the marginals of `T_*P`, and total variation is invariant under
a bijection. So `dep(W_ab) = dep(W_aa)` exactly. In exchange mode `δ_1 = 0`; in initial-condition
mode with a non-causal layout `δ_1` may be nonzero, which changes nothing. The content of the
blocks beyond the test may differ between the four tests: the identity holds for any two complete
assignments (`L54:168–169`), which is stronger than what FC-1 needed (S3:166–167).

**Target values.** With `𝓘*_{c_u,h}(σ) = q_u(h|k) P^u_k σ P^u_k`, the law of `(c_u, c_v)` on `σ` is
`Σ π(k_1, k_2) q_u(·|k_1) ⊗ q_v(·|k_2)`, with `π(k_2|k_1) = Tr(P^v_{k_2} P^u_{k_1})` because `P^u_k`
has rank one. The four products have disjoint supports, so `dep = ½ Σ |π(k_1,k_2) − π(k_1)π(k_2)|`
and the four deviations of a 2×2 table share one modulus `d`: `dep = 2d`.
- `aa`: `d = p_a − p_a²`, `dep = 2p_a(1 − p_a)`.
- `ab`: `d = p_a(1 − p_a)[(1 + c)/2 − (1 − c)/2] = p_a(1 − p_a)c`, `dep = 2p_a(1 − p_a)|c|`.

Sanity check at `p_a = ½`, `c = 0`: equal fair bits give `dep = ½`, independent bits give 0.

**Constants.**
- Theorem 1: `|dep(L_aa) − dep(L_ab)| ≤ 3ε + 3ε`; `2p_a(1 − p_a)(1 − |c|) ≥ (1 − α²)/4`; so
  `1 − α² ≤ 24ε`, likewise `β`; `α² + β² ≤ (1 + |c|)|x|² ≤ 3/2`; `½ ≤ 48ε`. **`1/96` confirmed.**
- Proposition 2: step 1 gives `|u·x_i − u·ψ_i| ≤ 10ε` (the chain `ε + ε`, `2ε`, `ε` on class
  probabilities, doubled); step 3 gives `| |a·Δ| − |b·Δ| | ≤ 8ε`; `2 − 20ε − (1 + 20ε) ≤ 8ε`.
  **`1/48` confirmed.**
- Corollary 1a: §1 above. **`1/128` confirmed.**
- Lemma 5: `min(α², β²) ≤ ¾` gives `p_u(1 − p_u) ≥ 1/16` and a gap of at least `1/16`. Confirmed.

***

## 4. Counterexample search and controls (task item 4)

**Attempts to violate the conclusion.**
1. *Coset-uniform world.* `(z_1, z_2)` uniform on a subgroup `S ≤ G_1 × G_2`, so
   `dep = 1 − |S|/(|S_1||S_2|)`, the same for every label sequence. The target needs `½` for `aa`
   and `0` for `ab` at `p_a = ½`, `c = 0`. No choice of `S` gives both.
2. *Records that are class bits and nothing else* (`q_u` point masses). Then `(z_1, z_2)` takes at
   most four values with one fixed joint law, which must be perfectly correlated under `aa` and
   `c`-correlated under `ab`. Impossible.
3. *Hiding the first class from the second record.* Take `z_1 = (s, t)`, `z_2 = (s, t′)` with
   independent fair bits, class of `a` equal to `s` in both rounds, class of `b` equal to `t′`. The
   class statistics are right for `c = 0`. The complete record of round 2 still contains `s`, and
   the target for `ab` requires `h_2` to be independent of `h_1` given the classes. The world has
   `dep = ½` and the target has `dep = 0`, so by Lemma 2 (ii) the total variation from the target
   is at least `1/6`. This is the
   mechanism of the theorem, and it is why the document's control K4 is right that D4 is
   load-bearing: with class-only records the `ℤ/4` example passes this two-round test.
4. *Eigenstate escape.* `p_a ∈ {0, 1}` makes `dep(L_aa) = dep(L_ab) = 0`. Then
   `p_b(1 − p_b) = (1 − c²)/4 ≥ 3/16` and the `b`-pair fails. The proof handles this by using both.
5. *A law that depends on the labels.* This would break Lemma 1 and is excluded by H-μ.

No counterexample was found, and the search did not suggest one is available inside the schema.

**Why the argument does not exclude Main's constructions (control K2).** Confirmed. In the gluing
realization the label selects the step map `φ_a`, the outcome is an integer threshold comparison of
a seed with `Tr 𝓘_o(ρ̃)`, and the hidden register is updated to `𝓘_o(ρ̃)` (Main:578); in the single
dynamics `Φ(x) = φ_{π(x_vis)}(x)` (Main:580). The record is not an additive function of
(label, rest), so Lemma 1 has no input. Directly: Main:578 certifies exact `Z`-repeatability and
total variation `½` between the `XZ` and `ZX` outcome-string laws, so the dependence between
successive outcomes changes with the label and property (T) fails. The construction is also not an
interface of the schema (C-SUP-1 fails D1, D2, D6 and D7, AF:308–309).

**Control K1 is not independent as written** (finding F1). Direct checks that make it green:
- *C-POS-1.* Its round record is one public sign pointer (HA5:135, :308) and its record laws equal
  the quantum instrument branches (HA5:201–202). For "read `a`, read `a`" and "read `a`, read `b`"
  the pointer pairs have `dep` equal to `2p_a(1 − p_a)` and `2p_a(1 − p_a)|c|`. By Lemma 2 (i)
  alone they are not coordinatewise shifts, so (T) fails. I read only the HA5 lines cited.
- *Third case.* For R-nl at `q = 3`, in the interface of W-nl-2, the round-1 record laws of two
  label sequences are `(27, 90, 126)/243` and `(51, 51, 141)/243` up to a common shift (S4:181–185,
  table T3 at S4:145–151). I recomputed both rows of T3 by hand from the coefficients of
  `(1 + z + z²)^5`; they are right. Their probability multisets differ, so they are not translates,
  and (T) fails for a member of the class.
- *C-POS-2.* Not checked here; its source record was not opened.

**A second, rule-free constraint under D4 (reviewer's observation; one derivation, unreviewed; not
needed for the verdict).** A configuration of `O` is a pair (previous, current) and the record
lists it at every tick (P:167–168). So `X := x_O(τ)` is a coordinate of `h_1` (current component at
the last tick of round 1) and of `h_2` (previous component at the first tick of round 2); in
exchange mode this holds on `O ∖ C`. The proposal names the copy mechanism itself at P:200–203. In
the world `X` read from `h_1` equals `X` read from `h_2` with probability 1. Under the target law
the same event has probability at most `Σ_{k_1} π(k_1) max_x q_u(X = x | k_1)`. With one-round
credit this gives: **if `F(ε; 𝒯_R)` holds for the empty preparation, there are two configurations
that carry probability at least `1 − 2ε` of the law of `x_O(τ)`** (of `x_{O∖C}(τ)` in exchange
mode). This holds for every second-order rule, R-nl included, and uses no label. It does not
weaken Theorem 1. It bears on two things: for class D, Lemma 5 is not the only rule-free necessary
condition; and whether Q5′ on complete records was meant to force the observer region back to a
class-determined configuration at every round boundary is a question about the schema that the
owner may wish to see, since the proposal changed a definition for the same copy effect
(P:200–205). I did not derive what it implies for R-lin under the uniform law.

***

## 5. Consistency with prior results (task item 5)

**FC-1, FC-2.** Consistent. Both rest on part (d) of Lemma A-T, the 0-or-1 dichotomy for the
*marginal* continuation laws of two preparations under one continuation, which needs a
coset-uniform law and is lost under a herald. Theorem 1 rests on part (a), which is about values.
Proposition 2 implies FC-1 and FC-2 at `ε < 1/48` (unheralded witnesses need no (C)). Theorem 1
does not imply them on `1/96 ≤ ε < 1/48`, nor at the tokens' `ε₀ = 1/50` (finding F3).

**Lemma I.** Consistent. It is a necessary condition on one pair of preparations under one read.
For R-lin its hypothesis (Q3′, Q5′, Q6′ together) is not met at `ε < 1/96`.

**NL-C.** Independent: it bounds `|C|` and uses the gate family. No conflict.

**OA-2 Theorem E (b), (SP), Corollary E1.** Consistent and logically separate. Theorem E (b) is a
simplex embedding of the prepare–measure fragment. A simplex model can reproduce a qubit's
sequential reads (C-POS-1 does), so Theorem 1 does not follow from simplex-embeddability. It
follows from the translation form with complete records. Lemma 4 (c) agrees with the remark at
3A:613–617 and is conditional on the identification the document flags.

**The simplex remark** (S3:198–211; 3A:546–551). It is correct as far as it goes: a heralded
preparation's continuation law is a mixture of pairwise equal-or-disjoint coset laws, and one pair
of such mixtures under one read can sit at any total variation, so Lemma I does not exclude them.

**What the earlier analysis missed.** Two things, both available from Lemma A-T (a), which Session
3 proved and then used only through (d):
1. It never compared *one pair of preparations under two different reads*. Changing the read
   translates both continuation laws by the same element, so the pair is equally far apart under
   read `a` and under read `b`, mixture or not. The target needs about 1 for `±a` under `a` and at
   most about `½` under `b`. This is Proposition 2.
2. It never tested Q5′'s own two-round tests. The dependence between the complete records of two
   rounds does not depend on the labels in the world, and does in the target. This is Theorem 1.

The node tree was organized by where part (d) holds, so heralds, adaptivity and other laws became
child nodes, and the three survivors were then carried through review as complements of FC-1
without the base requirement being re-tested. The proposal had pointed at the right place: record
laws as "a family of translates ... bears directly on Q1, Q2 and Q5" (P:859–861).

**Prior statements of the same mechanism on `main`.**
- M1 Corollary A′: "The physical joint law of all records does not depend on the setting. The
  comparator's `(r0, r2)` marginal does depend on it: AP1 §4.4 gives independence at
  `(s, s′) = (0, 1)` and equality at `(1, 1)`" (M1:424–427).
- OA-1: under any affine rule "a setting held in the world acts only by translation ...
  measure-free"; "Not supplied natively for the gauge-derived affine class, R-lin included"
  (OA1:369–375); "Selectable read: not supplied (D5(ii), D7)" (OA1:392). OA-1 left open only the
  preparation tier: "At `q = 2` with heralds it is open (L5.4)" (OA1:365–367).
- C-MEAS: Q5′ fails on the two-read test: "The world's repeated reads are independent
  Bernoulli(`p`)" (S2:238–244).

Theorem 1 is the quantitative form of these for TUNE-1's `F(ε; 𝒯_R)`. Nothing in the earlier
record asserts that an R-lin interface meets Q5′, so no earlier result has to be withdrawn. The
`INCONCLUSIVE` rows were correct statements that no argument had been found.

***

## 6. Scope statements (task item 6)

- **Class D.** `L54:315` claims nothing beyond the proof. Its citation shows that the proof of
  Lemma 1 fails for R-nl, which is what the row says.
- **Main:588.** The paragraph is cautious but its last clause implies support inside the additive
  class. Main:588 concerns the continuously tunable state-mixing operation, with kernel support at
  configuration level. Theorem 1 uses no gate and concerns the sequential-read condition. It
  neither supports nor conflicts with Main:588 (finding F5).
- **"The linear rule is closed for control."** The document does not use these words, and it
  should not be summarized by them. What is proved is that R-lin fails the read-pair condition Q5′
  of TUNE-1 under D4 and the Lüders product target. Whether label translations can supply the gate
  family is recorded as not derived (N8). With a record convention coarser than D4 the invariant is
  unavailable (K4; open item 3). The measure-free statement about control for the affine class is
  OA-1's (OA1:369–385), at the level of the map.

***

## 7. Findings

Severity: **major** = must change before the result is relied on; **minor** = statement is wider or
weaker than the proof; **nit** = wording or citation.

**F1 (major; control). K1 is not an independent control.** Location: `L54:285`.
- For C-POS-1 and C-POS-2 the entry infers that (T) fails from Lemma 5 and the stated
  classification. That uses the argument under test to certify its own control ("merely reproduces
  the claimed formula", AGENTS.md, Exactness and controls).
- For the third case it cites Lemma NA (S4:86–92), which shows that the *proof* of Lemma 1 fails
  for R-nl, not that (T) fails. Session 4 keeps that distinction (S4:126, "The conclusion fails,
  not only the proof").
- Replacement text: "C-POS-1: the round record is one public sign pointer (HA5:135, :308) with
  record laws equal to the quantum branches (HA5:201–202), so the pointer pairs of 'read `a`, read
  `a`' and 'read `a`, read `b`' have `dep = 2p_a(1 − p_a)` and `2p_a(1 − p_a)|c|`; by Lemma 2 (i)
  they are not coordinatewise shifts and (T) fails. C-POS-2: [direct check from
  `finite-a2-v5/REPORT.md`, to be supplied]. Reversible rules with an unread uniform environment:
  (T) fails for R-nl at `q = 3`, where two label sequences give round-1 record laws
  `(27, 90, 126)/243` and `(51, 51, 141)/243` (S4:145–151, :181–185), which are not translates."
- Until the C-POS-2 entry is supplied, K1 is green for two of its three cases.

**F2 (major; scope). The headline statements omit load-bearing hypotheses, and "closed" is wider
than "fails Q5′".** Locations: `L54:23–29`, `:304–308`, `:310–314`.
- The blockquote names the rule, carrier, mode and H-μ. It omits D4, the Lüders product form of the
  target, the `ℓ = 0` reading, and the carried hypotheses H-∞ and H-write. The full list is at
  `L54:295–302`, but the blockquote is what will be quoted.
- Replacement for `L54:27–29`: "**Theorem 1.** In the TUNE-1 schema (complete-history records, D4;
  Lüders reads with conditional record laws fixed by label and class, AF:88–91), under R-lin, on
  `𝓛_fin` or on `ℤ^3` under H-∞, in initial-condition mode or in exchange mode under H-write, under
  any law of the unread world that is the same for every label sequence (H-μ): `F(ε; 𝒯_R)` fails
  at every `ε < 1/96` and every `K ≥ 2` when it is posed for the empty preparation (AF:116,
  :134–135, :389; S2:195, :200), and at every `ε < 1/128` and every `K ≥ 3` otherwise
  (Corollary 1a), for every interface and every declared target."
- Replacement for `L54:23`: "**Outcome label: NO.** No R-lin family meets Q5′ at any `ε < 1/96`,
  hence none meets Q3′, Q5′ and Q6′ together at every `ε`, whatever its Q6′ witnesses."
- Replacement for the heading `L54:304`: "**What fails, and for which class.**" and add after
  `L54:308`: "This is failure of the read-pair condition Q5′, and so of T1. It is not a statement
  that label translations cannot supply the gate family (N8, not derived), and it does not hold
  for a record convention other than D4 (control K4)."
- `L54:34–35` and `:312`: add "under (C) in initial-condition mode" to the statements about
  Proposition 2.

**F3 (minor; false comparison). Theorem 1 does not imply FC-1 and FC-2.** Location: `L54:289`.
FC-1 and FC-2 hold at `ε < 1/48` and their tokens are stated at `ε₀ = 1/50` (S3:331–334;
S4:328–335). Theorem 1 is silent on `1/96 ≤ ε < 1/48`. Replacement: "Proposition 2 implies the
conclusions of FC-1 and FC-2 at `ε < 1/48`. Theorem 1 gives failure of Q5′ alone at `ε < 1/96` for
the whole family class and says nothing on `1/96 ≤ ε < 1/48`; it does not reproduce the tokens at
`ε₀ = 1/50`. Lemma I's hypothesis is not met by any R-lin interface at `ε < 1/96`. NL-C is
independent."

**F4 (minor; statement of Corollary 1a).** Location: `L54:226–235`.
- "Any unheralded preparation" includes adaptive prefixes in exchange mode (AF:116; P:172–173),
  which (h2) excludes. The corollary is true for them, by one more line: in exchange mode the two
  test labels are written after the prefix, so replacing `c_a` by `c_b` in the second test round
  leaves `(r, h_1)` unchanged and shifts `h_2` by the fixed element given by `ι(c_b − c_a)`,
  whatever the prefix policy. Add that line, or restrict the statement to non-adaptive prefixes.
  The same line extends Proposition 2 to adaptive witnesses in exchange mode, which the document
  does not claim.
- The proof takes one weight vector `w_r` and one assignment for the four tests. That is AF:125–127
  ("world weights `w_r` on its prefix records"). In a non-causal layout the world's prefix-record
  law shifts with the test labels, so say explicitly that `w` is the preparation's, the same for
  every test.
- The constant is now cross-checked a second way (§1); `L54:233–234` can say so after its own
  check.

**F5 (minor; Main:588).** Location: `L54:326–331`. Replacement for the last two sentences: "The
present result does not bear on that statement: it concerns the sequential-read condition Q5′ on
record laws, uses no gate and none of the kernel theorems, and neither supports nor conflicts with
it. It is a consistency-axis result (§A.23)."

**F6 (minor; classification and prior art).** Location: `L54:333–340`; `NOTES-r1.md:56–59`.
"NEW for TUNE-1" is defensible only relative to the TUNE-1 directory. Add: "The mechanism is
stated on `main` in M1 Corollary A′ (M1:424–427), in OA-1 N2 and N3 (OA1:369–392) and in control
C-MEAS (S2:238–244); Theorem 1 is its quantitative form for `F(ε; 𝒯_R)`." Classify Theorem 1 as
ELABORATING with a new quantitative consequence for the L5 rows, or keep NEW with that sentence.

**F7 (minor; adaptivity).** Location: `L54:360–362`. Add: "The relabelling is triangular, not
coordinatewise: the shift of a later round depends on earlier records. `dep` and `D` are not
invariant under it, so Lemma 2 (i) does not extend to adaptive tests. Theorem 1 does not need it."

**F8 (nit; `ℓ = 0`).** Locations: `L54:73–75`, `:346–348`; `NOTES-r1.md:39–41`. Add S2:195 and
S2:200 to the support and state that the reading is the one used in the reviewed C-ISO-2 rerun.

**F9 (nit).**
- `L54:148–149` (N7 verdict): add "under the identification of Lemma 4 (c)".
- `L54:272–277` (Lemma 5): "for any rule, law and mode" should add "in the schema, with D4, the
  Lüders target of AF:88–91 and `F` posed for the empty preparation".
- `L54:304`, `:312–314`: a result marked WIP / UNVERIFIED should not carry the word "closed" in a
  table that may be copied; "fails Q5′ [W]" states the same thing.

No blocker was found. No finding concerns Lemmas 1–3 or the proof of Theorem 1.

***

## 8. The statement I am willing to sign

> **Theorem 1 (reviewed form).** Let `I` be one interface of the TUNE-1 schema (P:137–209) and
> assume:
> 1. **Rule.** The tick map is an additive map of `(V × V)^Λ`: R-lin at any fixed `q ≥ 2`.
> 2. **Carrier.** `Λ` is a finite torus, or `Λ = ℤ^3` under H-∞.
> 3. **Labels.** They enter as the time-zero content of program blocks disjoint from `O`
>    (initial-condition mode; any layout; any content in the blocks beyond the test), or by the
>    per-round exchange under H-write along label sequences fixed in advance.
> 4. **H-μ.** The law of the unread configuration is the same for every label sequence. Nothing
>    else is assumed of it.
> 5. **One interface.** `O`, `C`, `τ`, `r_O` and the layout are the same for the four tests (D1,
>    D2).
> 6. **Records.** The record of a round is the complete history of `O` over that round, with `c_j`
>    in exchange mode (D4), and a test's law is the law of these records.
> 7. **Target.** Two read labels `c_a, c_b` carry the instruments of AF:88–91: a two-class split of
>    the round records, conditional record laws that depend on label and class only, and
>    `a·b ∈ [−½, ½]`.
> 8. **Credit.** `K ≥ 2`, and one qubit state `σ` satisfies `TV(W_uv, 𝔔*(σ · (c_u, c_v))) ≤ ε` for
>    the four tests `(u, v) ∈ {a, b}²`. This is `F(ε; 𝒯_R)` for the empty preparation.
>
> Then `ε ≥ 1/96`.
>
> **Corollary 1a (reviewed form).** Replace 8 by: `K ≥ 3`, and some unheralded preparation of
> length `1 ≤ ℓ ≤ K − 2` whose labels are fixed in advance has one weight vector `w` and one
> assignment `r ↦ σ_r` credited at error `ε` on the same four tests. Then `ε ≥ 1/128`.
>
> **Consequence.** Under 1–7, no interface satisfies Q5′, hence none satisfies Q3′ or T1, at any
> `ε < 1/96` and `K ≥ 2` (at any `ε < 1/128` and `K ≥ 3` without the empty preparation). The
> conclusion carries H-μ, and H-∞ or H-write where they are used. It holds for every law, every
> control-region size and every kind of Q6′ witness, because none of them enters.
>
> **Proposition 2 (reviewed form).** Under 1–7, Q3′ and Q5′ at `(ε, K)` with `K ≥ L + 1`, and
> admissible Q6′(i) witnesses for `a` and `−a` whose labels are fixed in advance: if both are
> unheralded, or if no record of rounds before `j` depends on the label of block `j` (C), then
> `ε ≥ 1/48`.

**Not covered by anything I sign.** Rules that are not additive. Record conventions other than D4.
Targets whose reads are not of the form of AF:88–91. Labels that act other than as additive cell
content. Whether label translations can supply the gate family. Any statement about Main:588 or
about OI beyond the additive rule in this schema. The status of all of the above is one hand
review of a [W] derivation; whether the S3 §5 rows and 3A §§3.1–3.3 are restated is the owner's
decision (`L54:349–351`).

***

## 9. What was and was not checked

**Read.**
- `L54-r1.md` and `NOTES-r1.md`, whole.
- `TUNE-1-STEP2-AMENDMENT-1-final.md`, whole.
- `TUNE-1-STEP2-PROPOSAL.md`: 55–300, 424–520, 660–720, 825–900.
- `TUNE-1-STEP2-SESSION2.md`: 1–40, 150–300.
- `TUNE-1-STEP2-SESSION3.md`, whole.
- `TUNE-1-STEP2-SESSION4.md`: 60–200, 236–530.
- `TUNE-1-STEP3A-r3.md`: 462–900.
- `OA-2-REPORT-r4.md`: 492–612. `OA-1-REPORT-r5.md`: 168–210, 352–392.
- `mechanism-1-20261107/DESIGN.md`: 84–104, 398–452.
- `papers/Main.md`: 556–588, 596–600 (long paragraphs read to about 3,000–6,500 characters).
- `history-architecture-v5/REPORT.md`: 295–320 and the lines matching "pointer" or "record".

**Not read.** `TUNE-1-STEP1.md`; Session 1; the amendment drafts; `OA-3-REPORT-r4.md` beyond a
search; the OA reviews; `finite-a2-v5/REPORT.md` (so C-POS-2 in K1 is unchecked); any Lean module;
the owner's authorization comment.

**Not checked.** N9 (the superseded route) beyond its one inequality. Lemma 4 (c)'s identification
of OA-2's objects with TUNE-1's. The reviewer's observation in §4 has one derivation and no second
reader.

**Commands.** `ls`, `wc`, `sed -n`, `cat -n`, `cut`, `fold`, `grep`, `awk` (line lengths), `find`,
and one short Python text substitution applied to this review file itself (three wording
corrections). No interpreter was run on any OI rule, model or record law. All arithmetic was done
by hand, including the two rows of table T3.
