# TUNE-1, Step 2, session 4: the R-nl branch (L5/M3 under H-nl)

**WIP / UNVERIFIED research record.** Paper derivation only; no interpreter or numerical
computation was run. No manuscript or Lean file is changed, no premise is adopted, and nothing is
frozen, dispatched or merged. The results go to independent review and then ChatGPT review.

**Authorization.** The owner authorized this work on PR #1237, comment 6824440978 (`amaybaum`,
author association `OWNER`, 2026-11-12T13:06:41Z): "R-nl branch: 'Start after review
(Recommended)'. R-nl (choice 1(b), under H-nl) starts as paper-only work once ChatGPT has reviewed
Session 3." The same comment records L5.4 and L5.5 as "Record and leave (Recommended)"; this
session does not work on them. The review gate is met: ChatGPT review 5875006206 of Session 3 at
`53ec4898` (ACCEPT WITH SCOPE QUALIFICATIONS) states that "that independent review gate is now
met, subject to the existing named H-nl and all governance limits."

**Governing text:**
- the proposal at `e676c42a` (sha256 `2a081101…7499fd5`, checked at the start of this session);
- `TUNE-1-STEP2-AMENDMENT-1-final.md`;
- addenda 1 and 2.

Q-conditions are Q1, Q2, Q3′, Q4, Q5′ and Q6′; `F(ε; 𝒯′)`, credited assignments, admissibility,
the separation length `L` and constant `c₀` are as in the final amendment (B1). Labels are [K],
[P], [R] and [W]. Every derivation here is [W] unless tagged otherwise.

**R-nl and H-nl, as frozen** (proposal §1.1, choice 1(b) recorded at M0 in Session 1):
- **R-nl** is the rounded bijection of SM:294,
  `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q`, evaluated on the representatives `0, …, q − 1`.
  In the second-order form of proposal §1.1 it is `Φ(y, x) = (x, g(x) − y)` with
  `g(x)_i = h(s_i(x)) mod q`, `s_i(x) = Σ_{j ∈ nn(i)} x_j` (integer sum of representatives over the
  six nearest neighbours) and `h(s) = ⌊(s + 1)/3⌋`. The formula was checked against SM:294 at the
  Step 1 pin `cac5d264`.
- **H-nl** is the named hypothesis "the world's rule is R-nl". It replaces ledger item (vii) for
  this subclass, is carried into every conclusion that uses it, and is not adopted (proposal
  §1.1, §6).

**Controls.** All seventeen M1 controls are green under the governing text (Session 2, and its
C-POS-2 rerun with G1 closed), and the L5 proves-too-much row is green (Session 3 §4). Any new
negative argument of this session gets its own proves-too-much row (§4).

**Effort bound.** Choice 10(a) fixed three writer sessions with reviews. This is the fourth. It
runs under the owner's decision above, which authorized the R-nl branch after Session 3; the
relation of that decision to choice 10(a) is listed for the owner in §7.

***

## 0. Productivity test (§A.31), fixed before the node derivations

The R-nl branch is a **gem** iff it yields a fact that is strictly stronger than the restatement

> "Lemma A-T's proof uses R-lin's linearity, so FC-1 and FC-2 do not cover R-nl"

and that fact either
- (a) constrains R-nl families: a `FAIL-CLASS` for a stated subclass, or an explicit necessary
  condition on any family that meets Q3′, Q5′ and Q6′; or
- (b) exposes a hidden assumption in the governing text or in Sessions 1–3.

Otherwise the branch is a non-gem, and its results are recorded only. The propagation bar is
better-than-coherence: a relabelling of an existing statement is recorded and not propagated.

**Node plan (depth-first).**
- NL.1: transfer of Session 3 to R-nl, item by item, with the exact step at which nonlinearity
  breaks Lemma A-T, and whether the conclusion (not only the proof) fails.
- NL.2: the decisive branch. Is there an obstruction for R-nl families? First the R-lin route (an
  exact dichotomy), then its weakenings, then obstructions that do not use the rule at all.
- NL.3: the constructive side (Route P): what a `PASS-DERIVED` on R-nl would need.
- NL.4: the child splits of Session 3 (heralds, adaptivity, laws), read for R-nl.
- Tokens by proposal §2.2, over green controls.
