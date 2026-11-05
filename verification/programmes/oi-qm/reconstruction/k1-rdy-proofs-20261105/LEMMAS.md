# K1-RDY: paper proofs of the P1 lemma, the blindness lemma and L-O(i)/(ii)

**Status of every proof in this file: written proof, not independently reviewed.** Each is a hand derivation. No
enumeration, model computation, Lean run or workflow was used. The file changes no statement of the K1-RDY text and
decides no gate, token or owner question.

## 0. Sources, conventions and definitions

### 0.1 The text and its locators

"The text" is the K1-RDY preregistration accepted on 2026-11-02: 313 lines, recorded sha256
`a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`. "Line N" is line N of the text. The text is posted
as body lines 5–317 of #1031 comment 6567522034 and is held, byte for byte, as `PREREG-RECOVERED.md` on the branch of
PR #1114 (`research/k1-rdy-reconstruction-20261105`, head `e18b36e3`). Neither location is on `main`; both are
locators only (§A.42 item 2). Every statement proved below is quoted verbatim from the text, except the P1 lemma, whose
statement is assembled in §1.1, so the statement and its proof are readable from this file alone. The proofs establish
the statements as reproduced here; that they are the text's is checkable against the recorded sha256 once lines 1–313
are on `main`.

Earlier arguments, cited as provenance only; each row below is provenance: no proof here uses its content.

| Key | Record | Body lines used | Recorded digest prefix |
|---|---|---|---|
| r3 | #914 comment 6564008455, proposal K1-RDY r3 | 73–87 (blindness), 76–77 and 96 (P1 lemma), 104–124 (L-O) | `6ef06b1695d02a14` (body lines 5–325) |
| REV-r3 | #914 comment 6564018307, independent review of the proposal | 33–41 (F2), 106–107 (P1 lemma), 119–120 and 127–128 (blindness, L-O) | `74e4ead9793c6870` (body lines 5–151) |
| REV-pre | #1031 comment 6567537517, independent review of the text | 26 ("correct as stated and scoped") | `fa6c9e0430d4adf2` (body lines 5–182) |
| PROP | #1114 comment 6650931698, proposal for owner review, §3 "Draft proofs" | — | — |

The owner's ruling that calls for this package is #1031 comment 6651204512 (amaybaum, 2026-11-05T06:15:48Z), "Off-`main`
proofs: Option 1b": "Prepare self-contained paper proofs of the blindness lemma, the P1 invariant-measure lemma and
L-O(i)/(ii). Have them independently reviewed. [...] If a lemma fails review, return with a scoped correction rather
than silently changing the accepted text."

The text states that "the blindness lemma and L-O(ii) were checked in the proposal's review, and L-O(i) restates r3's
L-O(a) argument without the strict-form definition" (line 95). r3's L-O(a) (r3 lines 106–112) derives the inclusion
from sharp readiness under the further assumption that `π_0` is not sharply ready on `w`, and states no converse.
No earlier written proof of L-O(i) as stated was found. The P1 lemma's only earlier argument is one sentence of
REV-r3 (lines 106–107).

### 0.2 Definitions

The definitions are the text's, quoted or restated with their lines. Where a word is read in a particular way, the
reading is marked **(reading)**.

- **D1. Instance** (lines 31–33). `Λ = ℤ/5`, `𝐑 = ℤ/2`, `S = 𝐑^Λ × 𝐑^Λ`, `|S| = 1024`, `φ(x, y) = (y, Ay − x)` with
  `(Ay)_i = y_{i−1} + y_{i+1}`, and `φ^{−1}(x, y) = (Ax − y, x)`. Check of the inverse:
  `φ(Ax − y, x) = (x, Ax − (Ax − y)) = (x, y)` and `φ^{−1}(y, Ay − x) = (Ay − (Ay − x), y) = (x, y)`. So `φ` is a
  bijection of `S`. `A` is additive, so `φ(s + s′) = φ(s) + φ(s′)`: `φ` is an automorphism of the finite abelian group
  `S` (cellwise addition mod 2). In particular `φ(0) = 0`.
- **D2. Cells, states, ticks.** A cell is one coordinate `x_i` or `y_i`. For a set `X` of cells, `pr_X : S → 𝐑^X` is
  the restriction, a group homomorphism. The state at tick `t ∈ ℤ` is `s(t) = φ^{t − t_0}(s(t_0))` (line 31's `φ`
  is the one-tick update). `μ` is the joint law of the whole state at `t_0`, `Σ` included (line 35). For a set `X` of
  cells, `X_t := pr_X(s(t))`; it is a function of `s(t_0)`. An event is a subset of `S`, read as a condition on
  `s(t_0)`; an event stated at other ticks is "transported to `t_0`" by writing it as such a subset (lines 102–103).
- **D3.** `Σ = {x_0, y_0}`, `V` = site 1, current slice, `V_t = y_1(t)`, `T = 1`, `V ∩ Σ = ∅` (lines 33–34).
- **D4. Region `E`** (lines 36–37): "Every cell outside `Σ` that enters `V_t` with a nonzero coefficient, as a linear
  function of the state at `t_0`, for some `0 ≤ t ≤ T`." Here `t` is the offset from `t_0` **(reading;** line 34 uses
  the same symbol for the tick. Lines 37–38 compute `E` from `(V, Σ, T)`, `V`'s readout class and `φ` alone, without
  `t_0`, so the tick reading agrees with this one only when ticks are counted from `t_0`. Only the offset `0`, the tick
  `t_0`, is used below).
- **D5. Ready set** (line 39). `R_E = {0}`; the ready event is `Z := {E_{t_0} = 0} = {s : pr_E(s) = 0}`.
- **D6. Measures.** `π_0` is the uniform (counting) probability measure on `S`. For a measure `ν` and an event `B`
  with `ν(B) > 0`, `ν(· | B) = ν(· ∩ B)/ν(B)`. `μ_O = π_0(· | O)` for an event `O ≠ ∅` (line 103). For a map
  `ψ : S → S` and a measure `ν`, `ψ_*ν(A) = ν(ψ^{−1}A)`; the law of `s(t)` is `(φ^{t − t_0})_*μ`.
- **D7. Sharp readiness on `w`** (line 50): "`μ(W_{t_u} = w) > 0` and `μ(E_{t_0} = 0 | W_{t_u} = w) = 1`", and in B-pl
  "`μ(E_{t_0} = 0) = 1`". Write `B_w := {W_{t_u} = w}`.
- **D8. Non-blindness** (lines 53–54): "`NB(ν)`. There exist `σ ≠ σ′` with `ν(s_Σ(t_0) = σ), ν(s_Σ(t_0) = σ′) > 0`
  such that the law under `ν` of `(V_{t_0}, …, V_{t_0+T})` given `s_Σ(t_0) = σ` differs from that given `σ′` [...]"
  (the omitted words are the text's citation, "(R1, MR-pre:162)").
- **D9. Invariance and cycles.** `μ` is φ-invariant if `μ(φ^{−1}A) = μ(A)` for every `A ⊆ S`, that is `φ_*μ = μ`. A
  cycle of `φ` is an orbit `{φ^k(s) : k ∈ ℤ}`; `u_c` is the uniform probability measure on the cycle `c`.
- **D10. "Determines", "fixes"** **(reading)**. A nonempty event `B` determines (fixes) a function `f` on `S` if `f` is
  constant on `B`. This is the sense of L-O (lines 105–106, 110) and of G2(b) ("the function [...] that
  `Im ∩ {W_{t_u} = w}` fixes and `{W_{t_u} = w}` does not", lines 133–134). Since `π_0(· | B_w)` and `μ_O(· | B_w)`
  have full support on `B_w` and on `O ∩ B_w` respectively, "constant on the event" coincides there with "almost surely
  constant under the conditioned law", so L-O holds under either reading.

***

## 1. The P1 invariant-measure lemma

**Status: written proof, not independently reviewed.**

### 1.1 Statement and its source

The text names the P1 lemma without stating it: "The P1 lemma and the blindness lemma (CC-SCOPE)" (lines 244–245). It
uses its content at four places:

- lines 72–73: "`𝓘` = all φ-invariant probability measures on `S`, i.e. the mixtures of the uniform measures `u_c` on
  the cycles `c` of φ, `π_0` included";
- lines 74–75: "P2's energy-shell measures (SM:294–296) are members";
- lines 75–76: "each member's support is φ-invariant, so its image at `t_0` is itself";
- through the blindness lemma's proof (r3 lines 76–77: "Invariance makes the law of the state `μ` at every tick, so
  `P_μ(E_t = 0) = 1` for every `t` (the P1 lemma, confirmed by REV)").

r3 line 96 states a further consequence: "for invariant `μ`, sharp quiet `E` holds iff `μ` lives on orbits vanishing on
`E` at every tick (P1 lemma, confirmed by REV)". REV-r3 lines 106–107 state the lemma as: "invariance makes `P(E_t=0)`
constant, and invariant measures on a finite S are mixtures of cycle-uniform measures".

The statement below assembles these into one lemma. **The assembly is the writer's**; no accepted text states the P1
lemma, and the reviewer of this file should check that (a)–(c) carry what lines 72–76 and 244 use and nothing more.
Part (d) is not used by the text (source: r3 line 96); it is proved here as a corollary.

**Lemma P1.** Let `S` be a finite set, `φ` a bijection of `S`, and `𝒞` the set of cycles of `φ`.

- **(a)** A probability measure `μ` on `S` is φ-invariant if and only if `μ = Σ_{c ∈ 𝒞} λ_c u_c` for some `λ_c ≥ 0`
  with `Σ_c λ_c = 1`. The weights are unique: `λ_c = μ(c)`. In particular `π_0` and every `u_c` are φ-invariant.
- **(b)** If `μ` is φ-invariant, then `(φ^k)_*μ = μ` for every `k ∈ ℤ`. Hence, for every set `X` of cells, every
  `r ∈ 𝐑^X` and every tick `t`, `μ(X_t = r) = μ(X_{t_0} = r)`.
- **(c)** If `μ` is φ-invariant, its support is a union of cycles, and `φ(supp μ) = supp μ`; hence
  `φ^k(supp μ) = supp μ` for all `k ∈ ℤ`.
- **(d)** If `μ` is φ-invariant and `E` is a set of cells, then `μ(E_{t_0} = 0) = 1` if and only if `μ(c) = 0` for
  every cycle `c` that contains a state `s` with `pr_E(s) ≠ 0`; that is, if and only if `μ` is carried by the union of
  the cycles along which `E` vanishes at every tick. In that case `μ(E_t = 0) = 1` for every tick `t`.

### 1.2 Proof of Lemma P1

*Cycles.* For `s ∈ S` the states `s, φ(s), φ²(s), …` lie in the finite set `S`, so `φ^i(s) = φ^j(s)` for some
`0 ≤ i < j`; applying the bijection `φ^{−i}` gives `φ^{j−i}(s) = s`, so the orbit of `s` is
`{φ^k(s) : 0 ≤ k < j − i}`. The relation "`s′ = φ^k(s)` for some `k ∈ ℤ`" is
an equivalence relation (reflexive with `k = 0`, symmetric with `−k`, transitive by adding exponents), so the cycles
partition `S`. Each cycle `c` satisfies `φ(c) = c` and `φ^{−1}(c) = c`.

*(a), "only if".* Let `μ` be φ-invariant and `s ∈ S`. Since `φ` is injective, `φ^{−1}({φ(s)}) = {s}`, so
`μ({s}) = μ(φ^{−1}{φ(s)}) = μ({φ(s)})`. By induction `μ({φ^k(s)}) = μ({s})` for all `k ≥ 0`, so `μ` is constant on each
cycle: `μ({s}) = μ(c)/|c|` for `s ∈ c`. For any `A ⊆ S`, summing over the partition into cycles,
`μ(A) = Σ_c Σ_{s ∈ A ∩ c} μ(c)/|c| = Σ_c μ(c) u_c(A)`. The weights `μ(c)` are nonnegative and sum to `μ(S) = 1`.

*(a), "if".* Fix a cycle `c` and `A ⊆ S`. Since `φ^{−1}(c) = c`,
`φ^{−1}(A) ∩ c = φ^{−1}(A) ∩ φ^{−1}(c) = φ^{−1}(A ∩ c)`, and `φ^{−1}` is a bijection, so `|φ^{−1}(A) ∩ c| = |A ∩ c|`.
Hence `u_c(φ^{−1}A) = u_c(A)`: each `u_c` is invariant. The condition `μ(φ^{−1}A) = μ(A)` for all `A` is linear in
`μ`, so every convex combination of the `u_c` is invariant.

*(a), uniqueness and the named members.* If `μ = Σ_c λ_c u_c`, then for a cycle `c′`, `μ(c′) = Σ_c λ_c u_c(c′) = λ_{c′}`,
because distinct cycles are disjoint. For `π_0`: `π_0(A) = |A|/|S| = Σ_c |A ∩ c|/|S| = Σ_c (|c|/|S|) u_c(A)`, a
convex combination. At the instance, `φ(0) = 0` (D1), so `{0}` is a cycle and `δ_0 = u_{{0}}`.

*(b).* `φ_*μ = μ` is the definition of invariance. For `φ^{−1}`: `(φ^{−1})_*μ(A) = μ(φ(A))`, and invariance applied to
`φ(A)` gives `μ(φ(A)) = μ(φ^{−1}(φ(A))) = μ(A)`. By induction `(φ^k)_*μ = μ` for all `k ∈ ℤ`. Then
`μ(X_t = r) = μ({s : pr_X(φ^{t−t_0}(s)) = r}) = (φ^{t−t_0})_*μ({pr_X = r}) = μ({pr_X = r}) = μ(X_{t_0} = r)`.

*(c).* By (a), `μ({s}) = μ(c)/|c|` for `s ∈ c`, so `supp μ = {s : μ({s}) > 0}` is the union of the cycles `c` with
`μ(c) > 0`. `φ` maps each cycle onto itself, hence maps the union onto itself, and so does each `φ^k`, `k ∈ ℤ`.

*(d), "only if".* Suppose `μ(E_{t_0} = 0) = 1`, so `μ({s : pr_E(s) ≠ 0}) = 0`. If a cycle `c` contains `s` with
`pr_E(s) ≠ 0`, then `μ(c)/|c| = μ({s}) ≤ μ({pr_E ≠ 0}) = 0`, so `μ(c) = 0`.

*(d), "if".* Suppose `μ(c) = 0` for every cycle `c` that meets `{pr_E ≠ 0}`. That set is contained in the union of
those cycles, so `μ(pr_E ≠ 0) ≤ Σ μ(c) = 0`, and `μ(E_{t_0} = 0) = 1`.

*(d), the restatement and the last sentence.* A cycle `c` contains no `s` with `pr_E(s) ≠ 0` exactly when, for each
`s ∈ c`, `pr_E(φ^k(s)) = 0` for every `k ∈ ℤ`, that is, `E` vanishes along the orbit at every tick. The last sentence
is (b) with `X = E`, `r = 0`. ∎

### 1.3 Scope of Lemma P1

- Proved for any bijection of any finite set; at the instance it applies to `S` and `φ` of D1. Additivity of `φ` is not
  used.
- It does not compute the cycle decomposition of `φ` at the instance. (REV-pre line 31 reports 156 cycles from a hand
  check; that report is not used here, and line 191 assigns the decomposition to execution.)
- It does not establish §5.3's class rule (lines 156–163): that evaluating `π_0` and the cycle-uniform members, together
  with the union-of-cycles condition, decides the class (review question Q4). Part (a) supplies the description of the
  class that rule ranges over; the rule's sufficiency is a separate claim and is not proved here.
- Relation to the uses: lines 72–73's "i.e." is (a), both directions. Lines 75–76's image statement is (c). The
  blindness lemma uses (b). `δ_0` as a member of `𝓘` (line 236, CC-SCOPE) is (a). Lines 74–75's "P2's energy-shell
  measures (SM:294–296) are members" uses (a)'s "if" direction together with the conservation of ℰ (SM:294–296), which
  is not proved here. (d) is not used by the text (source: r3 line 96); it is proved here as a corollary.

***

## 2. The blindness lemma

**Status: written proof, not independently reviewed.**

### 2.1 Statement and its source

Lines 97–100, verbatim:

> **Blindness lemma.** Let `μ` be φ-invariant as the joint law of the whole state, `V ∩ Σ = ∅`, `E` given by §2, and
> `μ(E_{t_0} = 0) = 1`. Then `V_t = 0` μ-a.s. for every `t`, and `NB(μ)` fails. Not covered: non-invariant laws,
> W-relative branches, weak readiness, `V ∩ Σ ≠ ∅`, and ready sets with more than one element. It is not extended beyond
> these premises (K-14).

Definitions: D1–D5, D8, D9. "`μ`-a.s." means with `μ`-probability 1. "For every `t`" is read over all ticks `t ∈ ℤ`;
the proof gives that, which contains the readout window `[t_0, t_0 + T]` used by `NB`.

### 2.2 Proof of the blindness lemma

*Step 1: `y_1 ∈ E`.* Take the offset `0` in D4. `V_{t_0} = y_1(t_0)` is the linear function of the state at `t_0`
with coefficient `1` on the cell `y_1` and `0` on every other cell, and `1 ≠ 0` in `ℤ/2`. The cell `y_1` is `V`'s cell,
and `V ∩ Σ = ∅`, so `y_1 ∉ Σ`. By D4, `y_1 ∈ E`.

*Step 2: `V_t = 0` a.s.* `μ` is φ-invariant, so by Lemma P1(b) with `X = E` and `r = 0`,
`μ(E_t = 0) = μ(E_{t_0} = 0) = 1` for every tick `t`. By Step 1, `{E_t = 0} ⊆ {y_1(t) = 0} = {V_t = 0}`. Hence
`μ(V_t = 0) = 1` for every `t`.

*Step 3: `NB(μ)` fails.* Let `ρ := (V_{t_0}, …, V_{t_0+T})` and `N := {ρ ≠ (0, …, 0)}`. `N` is the union of the
`T + 1` events `{V_t ≠ 0}`, each of `μ`-probability 0 by Step 2, so `μ(N) = 0`. Let `σ` have `μ(s_Σ(t_0) = σ) > 0` and
let `v` be a value of `ρ`. Then
`μ(ρ = v | s_Σ(t_0) = σ) = μ({ρ = v} ∩ {s_Σ(t_0) = σ}) / μ(s_Σ(t_0) = σ)`. For `v ≠ 0` the numerator is at most
`μ(N) = 0`. For `v = 0` the numerator is `μ(s_Σ(t_0) = σ) − μ(N ∩ {s_Σ(t_0) = σ}) = μ(s_Σ(t_0) = σ)`. So the
conditional law of `ρ` given `s_Σ(t_0) = σ` is the point mass at `(0, …, 0)` for every positive-mass `σ`. No two
positive-mass values `σ ≠ σ′` give different laws, so `NB(μ)` fails (D8). If fewer than two values of `s_Σ(t_0)` have
positive mass, `NB(μ)` fails because its existential has no witness. ∎

### 2.3 Scope of the blindness lemma

- Premises used: `S` finite and `φ` a bijection with the evolution of D2; `μ` φ-invariant as the joint law of the whole
  state at `t_0`; `μ(E_{t_0} = 0) = 1` with `R_E = {0}`; and `V`'s cell in `E`, which follows from D4 and `V ∩ Σ = ∅`.
  This matches the premises of lines 97–98 and REV-r3's final check (lines 119–120). No other property of the instance
  is used.
- Not covered, as stated at lines 98–100: non-invariant laws, W-relative branches, weak readiness, `V ∩ Σ ≠ ∅`, ready
  sets with more than one element. The lemma is not extended here.
- Relation to line 163 ("In B-pl a member row [...] BLIND by the blindness lemma if it is" sharply ready). A member of
  `𝓘` is φ-invariant (Lemma P1(a)). In B-pl, `W` is trivial, sharp readiness is `μ(E_{t_0} = 0) = 1`, and G4 decides
  `NB` under `μ` (line 141). The lemma gives that `NB` fails at the only `w`, which is the BLIND row of line 174. The
  lemma does not decide the gates before that row: a G2 flag gives Z1-VOID, which supersedes it (lines 136–138, 182),
  and G4's VOID[row] precedes BLIND (lines 142–143). On the second point only, an observation outside this package's
  four results: a B-pl row that is sharply ready under `μ` satisfies (c1), because `supp μ ⊆ Z`, `|Z| = |S| q^{−|E|}`,
  and `H(μ) ≤ log|supp μ|`, so `D(μ) = log|S| − H(μ) ≥ |E| log q`.
- Relation to CC-SCOPE (line 208: `δ_0` BLIND in B-pl, B-eq and B-ct; line 244). In B-pl the lemma applies to
  `μ = δ_0`, which is invariant (Lemma P1(a)) with `δ_0(E_{t_0} = 0) = 1`. In B-eq and B-ct, G4 decides `NB` under
  `δ_0(· | W_{t_u} = w)` (line 141). Under `δ_0` the state is `0` at every tick (`φ(0) = 0`), so the only
  positive-mass `w` is `0`, `δ_0(E_{t_0} = 0 | W_{t_u} = 0) = 1`, and `δ_0(· | W_{t_u} = 0) = δ_0`. That conditioned law
  is itself φ-invariant and meets the lemma's premises, so the lemma applies to it as stated. This is an application to
  a law that satisfies the premises, not an extension to W-relative branches, where conditioning in general breaks
  invariance.

***

## 3. Lemma L-O(i)

**Status: written proof, not independently reviewed.**

### 3.1 Statement and its source

Lines 102–106, verbatim:

> **Lemma L-O** (quantifiers fixed; review nit 2). Let `O` be an event on `W`'s cells over a window, transported to `t_0`,
> `μ_O = π_0(· | O)`, and `w` of positive `μ_O`-mass.
> - *(i) Sharp readiness, any event.* `μ_O` is sharply ready on `w` iff `O ∩ {W_{t_u} = w} ⊆ {E_{t_0} = 0}`. If, in
>   addition, `π_0` is not sharply ready on `w`, then `O ∩ {W_{t_u} = w}` determines the nonconstant function
>   `1[E_{t_0} = 0]`, which `{W_{t_u} = w}` alone does not.

Definitions: D2, D5–D7, D10. `μ_O` is defined only for `O ≠ ∅`, which the hypothesis "`w` of positive `μ_O`-mass"
presupposes. "Sharply ready on `w`" is D7 for the single value `w`. "If, in addition" is read as adding the hypothesis
that `π_0` is not sharply ready on `w` to sharp readiness of `μ_O` on `w` **(reading)**; without sharp readiness of
`μ_O` the clause fails, for example for `O = S`.

### 3.2 Proof of L-O(i)

For `A ⊆ S`, `μ_O(A) = |A ∩ O|/|O|`. Hence `μ_O(B_w) = |O ∩ B_w|/|O|`, and positive `μ_O`-mass of `w` means
`O ∩ B_w ≠ ∅`. For such `w`,

`μ_O(Z | B_w) = μ_O(Z ∩ B_w)/μ_O(B_w) = |O ∩ B_w ∩ Z| / |O ∩ B_w|`. (∗)

*First clause, "only if".* Suppose `μ_O` is sharply ready on `w`, so (∗) equals 1. Then the finite set
`O ∩ B_w ∩ Z` has the same number of elements as the set `O ∩ B_w` that contains it, so the two are equal, and
`O ∩ B_w ⊆ Z`.

*First clause, "if".* Suppose `O ∩ B_w ⊆ Z`. Then `O ∩ B_w ∩ Z = O ∩ B_w`, and (∗) equals 1. With `μ_O(B_w) > 0` this
is sharp readiness on `w` (D7).

*Second clause.* Suppose `μ_O` is sharply ready on `w`, so `O ∩ B_w ⊆ Z` by the first clause, and `π_0` is not
sharply ready on `w`. `B_w ⊇ O ∩ B_w ≠ ∅`, so `π_0(B_w) > 0`, and "not sharply ready" means
`π_0(Z | B_w) = |B_w ∩ Z|/|B_w| < 1`: there is `s′ ∈ B_w` with `s′ ∉ Z`. Pick `s ∈ O ∩ B_w`; then `s ∈ Z`. So
`1[E_{t_0} = 0]` takes the value 1 at `s` and 0 at `s′`, both in `B_w`: it is nonconstant on `B_w`, so `B_w` does not
determine it (D10), and it is nonconstant on `S`. On `O ∩ B_w ⊆ Z` it is identically 1, so `O ∩ B_w` determines it.
It depends on the state only through `E_{t_0}`. ∎

### 3.3 Scope of L-O(i)

- Premises used: `S` finite, `π_0` uniform (so every nonempty event has positive `π_0`-mass), `O ≠ ∅` and
  `O ∩ B_w ≠ ∅`. The proof does not use that `O` is an event on `W`'s cells over a window, that `φ` is additive, or
  any property of the instance; the statement holds for every nonempty event `O` and every `w` of positive
  `μ_O`-mass. The text's narrower preamble is kept as stated.
- The second clause reads "determines" as in D10. The text's scope sentence calls this "a dynamical determination of
  `E`" (line 111). The lemma proves the set statement. The word "dynamical" describes how `O` reaches `E_{t_0}` (an
  event on `W`'s cells at window ticks, transported to `t_0` through `φ`) and is not a further mathematical claim.
- At equal time `W` may share cells with `E` (B-eq: `W_eq = {x_1, y_1}`, line 198). The lemma concerns the event
  `{E_{t_0} = 0}` of line 39 over all of `E`; the overlap rule (lines 48–49) governs counting and reporting and does not
  enter the statement or the proof.

***

## 4. Lemma L-O(ii)

**Status: written proof, not independently reviewed.**

### 4.1 Statement and its source

Lines 102–103 (the preamble quoted in §3.1) and 107–110, verbatim:

> - *(ii) Affine events, sharp or weak.* If `O` is a coset of a subgroup (equations on `W`'s window cells), then under
>   `μ_O(· | W_{t_u} = w)` the variable `E_{t_0}` is uniform on a coset `C_O(w)` contained in the coset `C(w)` it fills under
>   `π_0(· | W_{t_u} = w)`. Its law differs from `π_0`'s on the same `w` iff `C_O(w) ⊊ C(w)`, and then the class of
>   `E_{t_0}` modulo the smaller subgroup is a nonconstant function that `O ∩ {W_{t_u} = w}` fixes.

Definitions: D1, D2, D5–D7, D10. Notation for the proof: `L := (s ↦ W_{t_u}(s)) = pr_W ∘ φ^{t_u − t_0}` and
`p := pr_E`, so `B_w = L^{−1}(w)` and `E_{t_0} = p(s)`. Both are group homomorphisms, because `φ` is an automorphism
(D1) and projections are homomorphisms. "`O` is a coset of a subgroup" is read with `O` as a subset of `S`, the state at
`t_0`: `O = a_O + K_O` for a subgroup `K_O ≤ S`. "The smaller subgroup" is `p(K_O ∩ ker L)`, the subgroup of which
`C_O(w)` is a coset **(reading)**.

*On the parenthetical "equations on `W`'s window cells".* An event given by equations
`Σ_j c_j · (cell_j at tick t_j) = b_j` on `W`'s cells is, transported to `t_0`, the set `{s : M(s) = b}` for the
homomorphism `M(s) = (Σ_j c_j · pr_{cell_j}(φ^{t_j − t_0}(s)))_{equations}`. If nonempty it is `a + ker M` for any of its
elements `a`, hence a coset. A value-free event such as P3's "`W`'s configuration is identical at each tick of
`[t_u − 2, t_u]`" (line 79) is the kernel of `s ↦ (W_{t_u−1} − W_{t_u−2}, W_{t_u} − W_{t_u−1})`, hence a subgroup.
This is the content of line 113's "P3's `O` is a subgroup (§3), so (ii) applies to it", and it does not use the
explicit equations of line 89, which are not checked here.

### 4.2 Proof of L-O(ii)

*Step 1: the two conditioning events are cosets.* `w` has positive `μ_O`-mass, so `O ∩ B_w ≠ ∅`; fix `a` in it. Since
`L(a) = w`, `L(s) = w ⇔ L(s − a) = 0`, so `B_w = a + ker L`. Since `a ∈ a_O + K_O`, `a + K_O = a_O + K_O = O`. Hence
`s ∈ O ∩ B_w ⇔ s − a ∈ K_O ∩ ker L`, that is `O ∩ B_w = a + K` with `K := K_O ∩ ker L`, a subgroup of `ker L`.

*Step 2: uniform pushforward.* **Claim U.** If `H ≤ S` is a subgroup, `b ∈ S`, and `ν` is uniform on `b + H`, then
`p_*ν` is uniform on the coset `p(b) + p(H)` of the subgroup `p(H)`. *Proof.* `p(b + h) = p(b) + p(h)`, so `p` maps
`b + H` onto `p(b) + p(H)`. For `e = p(b) + p(h_0)` with `h_0 ∈ H`, the fibre is
`{b + h : h ∈ H, p(h) = p(h_0)} = {b + h_0 + k : k ∈ H ∩ ker p}`, of size `|H ∩ ker p|`, the same for every `e`. So each
point of `p(b) + p(H)` has `ν`-mass `|H ∩ ker p|/|H|`. ∎

*Step 3: the two laws.* For `A ⊆ S`, `μ_O(A | B_w) = π_0(A ∩ O ∩ B_w)/π_0(O ∩ B_w) = |A ∩ (a + K)|/|K|`: the law
`μ_O(· | B_w)` is uniform on `a + K`. Likewise `π_0(· | B_w)` is uniform on `B_w = a + ker L`. By Claim U, under
`μ_O(· | B_w)` the variable `E_{t_0} = p(s)` is uniform on `C_O(w) := p(a) + p(K)`, a coset of `p(K)`, and under
`π_0(· | B_w)` it is uniform on `C(w) := p(a) + p(ker L)`, a coset of `p(ker L)`. Since `K ⊆ ker L`,
`p(K) ⊆ p(ker L)`, and so `C_O(w) ⊆ C(w)`. This is the first sentence of (ii).

*Step 4: "differs iff `C_O(w) ⊊ C(w)`".* "If" direction: if `C_O(w) ⊊ C(w)`, the two laws have different supports
(the support of the uniform law on a nonempty finite set is that set), so they differ. "Only if" direction: if
`C_O(w) = C(w)`, both laws are uniform on the same finite set and so are equal; contrapositively, if they differ then
`C_O(w) ≠ C(w)`, and with `C_O(w) ⊆ C(w)` from Step 3, `C_O(w) ⊊ C(w)`.

*Step 5: the class modulo the smaller subgroup.* Suppose `C_O(w) ⊊ C(w)`. Two cosets with the common point `p(a)` are
equal exactly when their subgroups are equal, so `p(K) ⊊ p(ker L)`. Let `g(s) := p(s) + p(K) ∈ 𝐑^E / p(K)`, the class
of `E_{t_0}` modulo `p(K)`; it depends on `s` only through `E_{t_0}`. On `O ∩ B_w = a + K`,
`g(a + k) = p(a) + p(k) + p(K) = p(a) + p(K)`: `g` is constant, so `O ∩ B_w` fixes it (D10). Choose `k ∈ ker L` with
`p(k) ∉ p(K)`. Then `a + k ∈ B_w` and `g(a + k) = p(a) + p(k) + p(K) ≠ p(a) + p(K) = g(a)`, so `g` is nonconstant on
`B_w`, and hence on `S`. ∎

### 4.3 Scope of L-O(ii)

- Premises used: `S` a finite abelian group, `φ` an automorphism, `π_0` uniform, `O` a nonempty coset in `S`, `w` of
  positive `μ_O`-mass. The proof uses no other property of the instance. It covers B-pl as the case `W` trivial
  (`L = 0`, `B_w = S`, `C(w) = 𝐑^E`).
- Weak readiness. Under the premises, `μ_O(Z | B_w) = 1/|C_O(w)|` if `0 ∈ C_O(w)` and `0` otherwise, and likewise for
  `π_0` with `C(w)` (Step 3). Any difference between `r(w)` and `π_0(E_{t_0} = 0 | W_{t_u} = w)` is a difference of the
  two laws, so Step 4 gives `C_O(w) ⊊ C(w)` and Step 5 gives the function `g`. This is what the scope sentence of lines
  111–112 uses for "affine events (any departure)".
- Not covered, as stated at line 112: weak readiness from an event that is not a coset.

***

## 5. Outcome

All four results are proved as stated, on the definitions of §0.2. No counterexample or gap was found, and no
correction to the text is proposed. Points for the reviewer:

1. **The P1 lemma has no accepted statement.** §1.1 assembles one from lines 72–76 and 244 and from r3 and REV-r3. The
   reviewer should confirm that the assembly carries what the text uses.
2. **Readings.** D4 (offset), D10 ("determines"/"fixes"), the reading of "the smaller subgroup" in §4.1 and the
   reading of "If, in addition" in §3.1 are the writer's. Each is the reading under which the text's uses are stated; none changes a statement.
3. **Uses not proved here.** §5.3's class rule (Q4); the cycle decomposition of `φ` at the instance; P3's explicit image
   (line 89); the gates that precede G4 for a P1 member row; TA (c4); the conservation of ℰ (SM:294–296) behind lines
   74–75's membership of P2's energy-shell measures. Each is outside the four results.
4. **Generality noted, not adopted.** L-O(i) holds for any nonempty event, and the P1 lemma for any bijection of a finite
   set (§1.3, §3.3). The text's statements are not widened by this file.
