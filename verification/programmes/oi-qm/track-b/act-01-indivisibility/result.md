# Barandes indivisibility and correspondence bridge audit — result

Track B, act 1, executed against the preregistration frozen at blob
`b6727fa8df616e1a3f98e45d69b99b13554cda3e`
(`verification/programmes/oi-qm/track-b/act-01-indivisibility/preregistration.md`, merged by PR #558) as amended by
`verification/programmes/oi-qm/track-b/act-01-indivisibility/amendments/amendment-3.md`, frozen at blob
`f3f23acf7f30f941b87fa8f113699c5be0c7b87b` (merged by PR #559).

Base: `main` at `783d9edee9d63c8bbfbac8e7242a31ffd02982ae`, which carries both frozen blobs. Every
commit of this round descends from that merge, so the control-plane ordering is checkable from the
history.

This is a **definition-level audit**, not a proof round. It determines what Barandes's objects and
hypotheses are, transposed into this programme's vocabulary, and stops.

## Headline verdict

**(BD3, BR3).**

- **BD3 — definitional mismatch.** `PIndivisibleWithin` is a failure predicate. Barandes's
  *indivisible stochastic process* is a **tuple class**, membership in which neither entails nor is
  entailed by failure of divisibility. Markov chains are members (Source C §3.3, eq (54)), and a
  Markov chain is `PDivisible`. No stated transposition identifies the two predicates.
- **BR3 — required only downstream.** Source C's theorem (69) quantifies over the whole class, and
  **failure of divisibility is not among the hypotheses its proof uses**. Failure of divisibility is
  what the accepted text uses to derive interference (Source A §3.5, eq (43)).

The BR3 claim is a **negative one about divisibility specifically**, and it is stated that way
throughout. The proof of (69) does consume other structure from the tuple — non-negativity (45) for
eq (72), normalization (28) for eq (74), the trivialization condition (46) for eq (75), and the
standalone distribution and algebra of random variables in the later construction. What it never
consumes is divisibility or its failure.

The **Q4 equation comparison is recorded separately and is not folded into BD**, as Amendment 3
requires: against Source A's eq (6) the transposed factorization equation is an **exact match**.
That an exact Q4 match coexists with BD3 is precisely the situation Amendment 3 was written to keep
legible.

## Sources

| | Identity | Version and dates |
|---|---|---|
| **A** | J. A. Barandes, *The Stochastic-Quantum Correspondence* | arXiv:2302.10778**v3** [quant-ph] 30 Jul 2025; manuscript title page 30 June 2025; journal DOI `10.31389/pop.186` (*Philosophy of Physics* 3(1):8) |
| **B** | J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes* | arXiv:2507.21192**v1** [quant-ph] 27 Jul 2025; manuscript title page 30 July 2025 |
| **C** | J. A. Barandes, *The Stochastic-Quantum Theorem* | arXiv:2309.03085**v2** [quant-ph] 5 Feb 2026; manuscript title page 6 February 2026 |

Page numbers below are printed page numbers of these PDFs. Equation numbers are the papers' own.

The primary-source access precondition was met by route 1 of the freeze — lawful local copies of
the three papers supplied to the executing session. No whole paper is committed to this repository,
per Amendment 3's source-access practice; the short excerpts quoted below are the ones the answers
actually cite.

## The transposition, written out

This is the one comparison the round performs across the orientation boundary, and control 2
requires it to be explicit.

**Barandes's index order** (Source C eq (44), p. 13; Source A eq (1), p. 3):

    Γ_ij(t ← t₀) ≡ p(i, t | j, t₀)      row i = later configuration, column j = conditioning configuration

with normalization down **columns** (Source C eq (28), p. 9; Source A eq (3), p. 4):
`∑_i Γ_ij(t ← t₀) = 1`. He therefore works with **column-stochastic** matrices acting on the left
of a probability column vector: `p(t) = Γ(t ← t₀) p(t₀)` (Source C eq (47), p. 13; Source A eq (5),
p. 4).

**Our index order** (`OIBridge/CausalReadback.lean`, `rootedMap`):

    Γ t a j = probability of visible outcome j at time t, given root a

so row `a` = root, column `j` = later configuration, and `IsRowStochastic` normalizes across
**rows**. Ours is the transpose of his at the same time pair:

    Γ_ours t  =  (Γ_Barandes(t ← 0))ᵀ      with the root identified with the conditioning
                                            configuration and t₀ := 0.

**Under that transpose, the two factorizations are the same equation.** Barandes:

    Γ(t ← t₀) = Γ̃(t ← t′) Γ(t′ ← t₀),   Γ̃ column-stochastic.

Transposing both sides and reversing the product:

    Γ(t ← t₀)ᵀ = Γ(t′ ← t₀)ᵀ Γ̃(t ← t′)ᵀ,

i.e. with `s := t′`, `Λ := Γ̃(t ← t′)ᵀ`:

    Γ_ours t = Γ_ours s * Λ,   Λ row-stochastic,

which is the body of `PDivisible` verbatim. A matrix is column-stochastic exactly when its
transpose is row-stochastic, so the stochasticity requirement transports without residue.

**What does not transport** is quantifier structure, and it is reported at that granularity in Q4
and Q6 rather than absorbed here.

## The nine questions

### Q1 — the exact stochastic object

**Determination.** In the theorem-bearing source the object is a **six-component tuple**

    (C, T, T₀, Γ, p, A)

— Source C §3.1, eq (24), p. 8 — with:

- `C` the configuration space, assumed **finite** of size `N` for that paper's purposes (p. 8);
- `T` the set of target times, containing a time `0` (p. 8);
- `T₀ ⊆ T` the set of conditioning times, containing `0`, "often assumed to be a 'sparse' subset
  of `T`" (p. 9);
- `Γ : C² × T × T₀ → [0,1]` the transition map, eq (25)–(27), p. 9, with
  `Γ_ij(t ← t₀) ≡ p(i,t | j,t₀)`, subject to the **normalization condition** eq (28)
  (`∑_i Γ_ij(t ← t₀) = 1`) and the **trivialization condition** eq (29)
  (`Γ_ij(t₀ ← t₀) = δ_ij`);
- `p : C × T → [0,1]` the standalone probability distribution, eq (30)–(31), p. 9;
- `A` a commutative algebra of maps `A : C × T → ℝ`, the algebra of random variables, eq (40)–(42),
  p. 12, "always taken to be **maximal**, in the sense of containing every well-defined map" of that
  form (p. 12).

**Nomological versus contingent.** Source A §2.1, p. 3: the configuration space and the transition
maps "will constitute the *fixed* features of the model, whereas the probability distributions will
be *contingent* features". Source A p. 4 (below eq (4)): the standalone probabilities `p_j(t₀)` "are
assumed to be arbitrary and contingent, and can therefore be freely adjusted without altering the
conditional probabilities `Γ_ij(t ← t₀)`, which are regarded as fixed features of the model."
Source C makes this sharp: eq (32), p. 10 — only `p_1(0), …, p_N(0)` are "freely adjustable",
subject to summing to 1; every other `p_i(t)` is **defined** by the marginalization condition
eq (33).

**What is deliberately absent from the data.** Higher-order conditional probabilities are not part
of the tuple. Source C p. 12: "The definition of an indivisible stochastic process presented in this
paper does not assume fixed values of such higher-order conditional probabilities in the first
place, and therefore, in a sense, represents a whole equivalence class of non-Markovian models, each
of which is called a **non-Markovian realizer**. In particular, an indivisible stochastic process is
defined by fixing **less** information than any of its non-Markovian realizers." Source B §2.2,
p. 10, says the same thing and names the terminology; Source A §2.2, p. 6, gives the earlier form
("works with *equivalence classes* of non-Markovian processes … that may differ in their
higher-order conditional probabilities but share the same first-order conditional probabilities").

**Version note.** Source A §2.1, p. 3, describes the same object informally as "a model consisting
of two basic ingredients: a *configuration space* `C`; and a dynamical law in the form of a family
of *transition maps* `Γ_{t←t₀}`" — two ingredients plus contingent distributions, without the
`(C,T,T₀,Γ,p,A)` tuple presentation. The six-component tuple is Source C's. The two are not in
conflict; the tuple is the version that a formalization should transpose to, because it is the one
the theorem quantifies over.

**Evidence type.** Primary source at pinpoint locations.

### Q2 — conditioning and target times

**Determination.** `T₀` is a **distinguished component of the data**, not a derived set: it appears
in the tuple (24) itself and is the third slot. Target times `T` and conditioning times `T₀` play
asymmetric roles.

- Source C §3.1, p. 9: `T₀ ⊆ T`, contains `0`, and "in practical cases, `T₀` will often be assumed
  to be a 'sparse' subset of `T`, in the sense that `T` will contain many times not in `T₀`."
- Source B §2.2, pp. 9–10: "no assumption is made here that the transition probabilities `p(i,t|j,t₀)`
  exist as part of the laws for all real-valued choices of `t₀`. Allowed conditioning times `t₀` are
  called **division events** for the given system". And: "The target time `t`, by contrast, can be
  treated as a free variable. In particular, **no assumption is made that `t > t₀`**. One can choose
  `t < t₀` as well."
- Source C §3.1, p. 10, after eq (35): "conditioning times like `t′` will alternatively be called
  **division events**."
- Source B p. 10: "Division events are not global properties of the whole universe, but are
  system-centric".

**Does the theorem quantify over `T₀`?** **No.** Source C §5.1, p. 20, opening the proof of (69):
"one starts with a given indivisible stochastic process `(C,T,T₀,Γ,p,A)` with a finite configuration
space `C` of size `N`. **Singling out one conditioning time `t₀`**, which will be taken to be the
initial time 0 for convenience …". The construction is carried out at a single conditioning time.
Source A §3.1, p. 6, does the same: "the conditioning time `t₀` will now be taken to be the 'initial
time' 0."

**Bearing on our side.** Our `Γ : ℕ → Matrix V V ℝ` carries one time index and a fixed root, so it
is by construction the `t₀ = 0` slice — hazard 1 of the freeze. The audit's finding is that this is
not a defect of our object relative to his theorem, because his theorem also works at a single
conditioning time. It **is** a difference relative to his *tuple*, which carries the whole set `T₀`,
and Q8 records what that costs.

**Evidence type.** Primary source at pinpoint locations.

### Q3 — the divisibility predicate

**Determination.** The primary sources carry **two distinct formulations**, and they are not
interchangeable. Control 3 requires both to be reported rather than one projected onto the other.

**(a) The diagnostic formulation — Source A §2.1, p. 4, eq (6), and Source B §2.2, p. 10,
eqs (22)–(23).** Source A, verbatim:

> "Crucially, the transition matrix `Γ(t ← t₀)` will *not* be assumed to be 'divisible,' … That is,
> `Γ(t ← t₀)` will generically be *indivisible*, meaning that for intermediate times `t′` satisfying
> `t > t′ > t₀`, **there will not generally exist** a genuinely stochastic matrix `Γ̃(t ← t′)`
> satisfying the composition law or *divisibility condition*
> `Γ(t ← t₀) = Γ̃(t ← t′) Γ(t′ ← t₀)`."

Here the intermediate object is **existentially quantified** and **required to be stochastic**.
Source A p. 5 sharpens it for the explicit 2×2 examples of eq (7): those are "provably indivisible,
because **any** matrix `Γ̃(t ← t′)` satisfying the divisibility condition above would need to have
negative entries for at least some pairs of times `t` and `t′`, and would therefore not be a genuine
stochastic matrix." Source B pp. 9–10 gives the mechanism for the natural candidate:
`Γ̃(t ← t′) ≡ Γ(t ← t₀) Γ⁻¹(t′ ← t₀)` (eq (22)) "will generically fail to be a column stochastic
matrix, and, indeed, will typically have negative entries", with footnote 7 proving that the inverse
of a stochastic matrix is stochastic only for permutation matrices.

**(b) The axiom formulation — Source C §3.1, p. 10, eq (35).** Verbatim:

> "The transition map `Γ` **will be assumed to satisfy** the following divisibility condition for any
> target time `t ∈ T` and any pair of conditioning times `t₀, t′ ∈ T₀ ⊂ T`:
> `Γ_ij(t ← t₀) = ∑_k Γ_ik(t ← t′) Γ_kj(t′ ← t₀)`."

In this formulation there is **no existential quantifier**: the intermediate factor is the *given*
`Γ(t ← t′)`, which exists precisely because `t′ ∈ T₀`. Divisibility is an **axiom of the tuple**,
holding throughout `T₀`. Indivisibility is then a matter of **definedness off `T₀`** — Source C
p. 11:

> "If `t′` is a target time but *not* a conditioning time, then the values `Γ_ik(t ← t′)` appearing
> in the divisibility condition (35) will not be well-defined, and the divisibility condition will
> not hold. The process described here is therefore indivisible for generic target times `t′` …"

Source C footnote 5, p. 11, adds the same inverse-matrix observation as Source B: "It follows that
one cannot safely define the non-negative quantities `Γ_ik(t ← t′)` by invoking inverse matrices."

**The divergence, stated.** (a) says *no stochastic intermediate exists*. (b) says *the intermediate
is not part of the model's data off `T₀`, and the composition law is imposed on `T₀`*. A process can
satisfy (b)'s axiom everywhere on `T₀` and be indivisible in sense (a) at target times outside `T₀`;
conversely, a process whose `T₀ = T` and which satisfies (b) at every pair is divisible in sense (a)
throughout. The later source (C, Feb 2026) is the axiom formulation; the accepted correspondence
paper (A, June/July 2025) is the diagnostic formulation. **The later terminology is not projected
backward** onto Source A, per control 3.

**Evidence type.** Primary source at pinpoint locations.

### Q4 — literal comparison after transposition

**Recorded separately from BD, per Amendment 3 repair 1. This answer is not a BD verdict.**

**Determination against formulation (a) — Source A eq (6): an exact match.** Applying the
transposition of the section above to eq (6) yields, term for term,

    Γ_ours t = Γ_ours s * Λ  with  Λ  row-stochastic,

which is the body of `PDivisible` with `s := t′`, `t := t`, `t₀ := 0`. The orientation hazard named
in the freeze is real — his propagator is on the left of a column-stochastic action, ours on the
right of a row-stochastic one — and it resolves: the two are the same content under transpose, and
the transpose carries the stochasticity requirement onto the same factor. There is no mismatch in
**which** factor is required stochastic: in both, it is the newly introduced intermediate, not the
given earlier-time map.

**Against Source A eq (6), exactly two quantifier differences remain, and they are findings, not
formatting.**

1. **Horizon.** Ours bounds `t ≤ K`. Source A bounds nothing; the intermediate times range over
   `t > t′ > t₀` without a horizon. Our `K` has no counterpart on his side.
2. **Endpoint of the intermediate range.** Source A requires `t′ > t₀` strictly; ours admits `s = 0`.
   At `s = 0` our condition is discharged by `Λ := Γ_ours t`, since `rootedMap R 0 = 1`, so the extra
   case is vacuous rather than stronger.

**Direction is not one of them, and is recorded separately as a Source B scope observation.**
Source A eq (6) restricts to `t > t′ > t₀`, which is the same forward orientation as our `s < t`, so
against eq (6) there is no direction difference to report. Source B p. 10 nonetheless broadens the
convention at the level of the framework rather than of the divisibility equation: "The target time
`t` … can be treated as a free variable. In particular, no assumption is made that `t > t₀`. One can
choose `t < t₀` as well." That widens the domain on which his `Γ` is defined; it is not a difference
between the two factorization equations, and the audit does not report it as one.

**Determination against formulation (b) — Source C eq (35): not a match.** Eq (35) is universally
quantified and **asserted**, with the intermediate supplied by the data rather than existentially
quantified. Our `PDivisible` has no assertion form and no `T₀`; it is an existence claim at every
admissible pair. Under `T₀ = {0}` eq (35) becomes vacuous (only `t₀ = t′ = 0` is available) while
`PDivisible` remains a substantive claim at every `s < t ≤ K`.

**Evidence type.** Primary source at pinpoint locations, plus a prose transposition. The transposed
predicate is **not** formalized in Lean this round; the freeze defers that to the next round, and
the evidence hierarchy prefers a Lean equivalence for the this-side half when that round runs.

### Q5 — required or merely unassumed

**Determination: merely unassumed.** "Indivisible stochastic process" names the **framework**, not
a hypothesis. Six independent primary-source locations settle it:

1. **The class contains Markov chains, by name.** Source C §3.3, p. 14, eq (54): "In particular, one
   can regard **any Markov chain as a special case of an indivisible stochastic process**." The
   construction given there sets `T = T₀ ≅ ℤ` and `Γ(n δt ← 0) = [Γ(δt)]ⁿ` — which is divisible in
   our sense, with `Λ := [Γ(δt)]^{t−s}` stochastic. Source C p. 14 concludes: "More broadly, an
   indivisible stochastic process can therefore be understood as a kind of non-Markovian
   generalization of a Markov chain."
2. **The abstract says so.** Source C, abstract, p. 1: "The most general of these structures, called
   indivisible stochastic processes, collectively **encompass many important kinds of stochastic
   processes, including Markov chains and random dynamical systems**."
3. **The naming convention is explicitly permissive.** Source C §2.1, p. 3, on the deterministic
   analogue: "A dynamical system is usually assumed to be divisible … The more general case would be
   an indivisible dynamical system that **might lack** this feature."
4. **The wording of the assumption.** Source A §2.1, p. 4: the transition matrix "will *not* be
   assumed to be 'divisible'". This is "not assumed divisible", not "assumed not divisible" — the
   distinction the freeze required the audit to resolve, resolved in favour of the former.
5. **Divisibility is affirmatively assumed on `T₀`.** Source C §3.1, p. 10, eq (35), as quoted in Q3:
   "The transition map `Γ` will be assumed to satisfy the following divisibility condition …". Far
   from requiring failure, the later source **imposes** the composition law where it is defined.
6. **A fully divisible worked example is admitted by the theorem.** Source C §4.3, p. 19: a discrete
   Markovian-homogeneous dynamical system whose evolution is the `n`-th power of a fixed permutation
   matrix `Σ` "is already a unistochastic process, and therefore **trivially satisfies the
   stochastic-quantum theorem (69)**."

**And the proof does not use it.** The claim here is narrow and negative: **divisibility and its
failure are not among the hypotheses the proof of (69) uses.** Source C §5.1, p. 20, opens the
construction from the non-negativity condition (45) — "the non-negativity (45) of the system's
conditional transition probabilities, `Γ_ij(t ← 0) ≥ 0`, means that each transition probability can
be written as the modulus-square of a non-unique complex number" — giving eq (72), of which the text
says: "It is worth emphasizing that this formula is an **identity, not a postulate**." The
normalization condition (28) then gives the summation condition (74).

**What the proof does use is more than those two, and the audit does not claim otherwise.** Source C
§5.1, p. 21, invokes the **trivialization** condition (46) to set `Θ(0 ← 0) = 1` at eq (75); §5.2
builds `H ≡ ℂ^N` from `C`; and the later construction — the density matrix of §5.4, the dilation of
§5.7, and the dilated process of §5.8 — draws on the standalone distribution `p` and the algebra `A`
of the tuple. Enumerating the proof's inputs is not this round's question. What settles the role
axis is that **no version of divisibility, and no failure of it, appears among them.**

**Evidence type.** Primary source at pinpoint locations.

### Q6 — the shape of the failure, if it is required

**Determination: not required, so it has no shape as a hypothesis.** Q5 settles that no source
imposes failure of divisibility as a condition of entry to the class or as a hypothesis of the
theorem. The question is therefore answered in its conditional's antecedent.

Where the sources describe failure as a **fact about generic members** rather than a hypothesis, the
shapes differ across sources, and the freeze requires reporting at that granularity:

| Source | Location | Shape asserted |
|---|---|---|
| A | §2.1, p. 4, eq (6) | **Generic**: "will *generically* be indivisible … there will not *generally* exist a genuinely stochastic matrix" |
| A | §2.1, p. 5, on eq (7) | **Existential, provable, for named examples**: "provably indivisible, because any matrix `Γ̃(t ← t′)` … would need to have negative entries **for at least some pairs of times** `t` and `t′`" |
| B | §2.2, p. 10, eqs (22)–(23) | **Generic failure of one named candidate**: `Γ(t ← t₀)Γ⁻¹(t′ ← t₀)` "will generically fail to be a column stochastic matrix" |
| C | §3.1, p. 11 | **Undefinedness off `T₀`**: "indivisible for generic target times `t′`", because `Γ_ik(t ← t′)` "will not be well-defined" |
| **ours** | `PIndivisibleWithin K Γ` | **Existential failure at one pair below a horizon**: `¬ ∀ s t, s < t → t ≤ K → ∃ Λ, …` |

Two of these are strictly weaker than ours as claims about a fixed process. Source B's is a claim
about a **particular** candidate intermediate obtained by inversion; that this candidate fails to be
stochastic does not by itself establish that **no** stochastic `Λ` exists, which is what
`PIndivisibleWithin` asserts. Source C's is a claim about **definedness** of the model's own data,
which is not a claim about existence of a stochastic matrix at all. Only Source A's statement about
the eq (7) examples is of our kind, and it is asserted of those examples rather than of the class.

**Evidence type.** Primary source at pinpoint locations.

### Q7 — time domain

**Determination: our finite discrete-time rooted process satisfies the tuple's time-domain
assumptions. No embedding or interpolation theorem is needed for Source C's theorem.**

- Source C §3.1, p. 8, requires only that `T` be a set containing a time `0`, with `T₀ ⊆ T`
  containing `0`. No ordering, cardinality, topology or algebraic structure is imposed on `T` in the
  definition.
- Source C §3.3, p. 14, eq (54), explicitly instantiates `T = T₀ ≅ ℤ`, a discrete domain.
- Source C §4.3, p. 19, works a discrete example with `T ≅ ℤ` under addition.
- Source C §4.1, p. 18, restricts the theorem's domain in the **configuration** direction only:
  "Focusing on the case of indivisible stochastic processes with **finite configuration spaces**
  (leaving the more general case to future work)". Our `V` is a `Fintype`.

Two differences are worth recording, neither of them an obstacle:

1. **The real-line default is a default, not a requirement.** Source A §2.1, p. 3, says target times
   will "usually be assumed to be isomorphic to the real line `ℝ`". Source C does not carry that
   assumption into the tuple, and its own worked examples are discrete.
2. **Continuity has no discrete counterpart, and is not needed.** Source A p. 4 assumes that
   "in the limit `t → t₀`" the transition matrix approaches `Γ(t₀ ← t₀) = 1`. In a discrete `T` the
   limit clause is empty; what survives is the **trivialization** condition, Source C eq (29),
   `Γ(t₀ ← t₀) = δ`. That holds on our side: `rootedMap R 0 = 1`, since `step^[0]` is the identity.

**Evidence type.** Primary source at pinpoint locations, plus the this-side reading of `rootedMap`
at `t = 0` from the merged Lean source.

### Q8 — sufficiency of our data

**Determination: the merged rooted-realization datum supplies the transition half of the tuple
outright, and two of the six components must be supplied alongside it. Nothing is missing in the
sense of being unavailable; two things are missing in the sense of being undetermined by the
datum.**

The merged datum is `RootedRealization V H` (`OIBridge/CausalReadback.lean`): a reversible total
update `step : V × H ≃ V × H`, together with **one hidden prior** `prior : H → ℝ`, nonnegative and
normalized, **shared by every visible root**. The rooted map is
`rootedMap R t a j = ∑_h [((step)^[t] (a,h)).1 = j] · prior h`, proved row-stochastic by
`rootedMap_isRowStochastic`.

Component by component against Source C eq (24):

| Barandes component | Supplied by our datum? |
|---|---|
| `C` (finite configuration space) | **Yes** — `V`, a `Fintype`. |
| `T` (target times containing 0) | **Yes** — `{0, …, K}`, or `ℕ`. |
| `T₀` (conditioning times containing 0) | **Not carried.** Must be **declared**; the natural choice is `T₀ = {0}`, which is the slice our `Γ` represents. |
| `Γ` (transition map, normalized, trivializing) | **Yes** — `Γ_ij(t ← 0) := (rootedMap R t)ᵀ`. Column-normalization is `rootedMap_isRowStochastic` after transpose; trivialization (29) is `rootedMap R 0 = 1`. |
| `p` (standalone distribution) | **Not determined.** Our prior lives on the hidden carrier `H`, not on `C = V`. Barandes's `p(·,0)` is a distribution on `C`. |
| `A` (algebra of random variables) | **Yes, automatically** — Source C p. 12 takes `A` maximal, containing every well-defined map `C × T → ℝ`. |

**On `p`.** This is not a gap in the theorem's direction. Source C eq (32), p. 10, makes `p(0)`
freely adjustable subject only to normalization, and Source A p. 4 calls the standalone
probabilities "arbitrary and contingent"; the transition map is defined independently of them
(Source C p. 10: "the definition of the transition map `Γ` is independent of the choice of standalone
probabilities"). So **any** normalized choice instantiates the tuple, and the theorem's construction
in §5.1 does not consume `p` at all. What is true is that our datum does not **select** one.

**On `T₀`.** Declaring `T₀ = {0}` makes Source C's divisibility axiom eq (35) vacuous, since the only
available pair is `t₀ = t′ = 0`. That is a legitimate instantiation and it is worth stating plainly:
under it, the axiom carries no content, and the process is "indivisible for generic target times" in
Source C's sense (p. 11) purely because no intermediate propagator is part of the data.

**Provenance language, per Q8's own constraint and control 9.** The prior is a **fixed ingredient of
the merged datum**. It is not claimed to be sourced from bare OI; #537 settled that. Nothing in this
answer describes it as sourced, and the sufficiency determination above is about the data, not about
where the data comes from.

**Evidence type.** Primary source at pinpoint locations for the tuple's requirements; the merged
Lean source for what our datum carries.

### Q9 — what the correspondence delivers

Itemized, each marked **theorem-level** or **interpretive**, in point 4 below.

**Determination in summary.** Across the three sources, exactly **one** theorem environment exists:
Source C's boxed eq (69), p. 18. Source A contains no theorem of its own — its five occurrences of
the word name **other people's** theorems (Stinespring, the spectral theorem, an elementary theorem
of linear algebra, Bell–Kochen–Specker, Pusey–Barrett–Rudolph). Source B likewise states none of its
own; it attributes the result: "This statement is called the stochastic-quantum theorem (Barandes
2023)" (p. 18). Everything else in the three papers is developed by construction, derivation and
worked example within the framework, or is interpretive.

**Evidence type.** Primary source at pinpoint locations.

## 4. What the correspondence delivers, itemized

**Theorem-level.**

1. **Every indivisible stochastic process can be regarded as a subsystem of a unistochastic
   process.** Source C §4.1, p. 18, boxed eq (69), proved in §5, pp. 20 ff. Domain: finite
   configuration spaces (p. 18). This is the whole of the stochastic-quantum theorem.
2. **The `Γ = |Θ|²` representation exists.** Source C §5.1, eq (72), p. 20; Source A §3.1, eq (12),
   p. 6. Marked by both texts as an **identity, not a postulate**, following from non-negativity
   alone. Non-unique — Source A p. 7, fn 6, calls the freedom a form of gauge invariance.
3. **The dictionary.** `Γ_ij(t ← 0) = tr(Θ†(t ← 0) P_i Θ(t ← 0) P_j)`, Source A §3.2, eq (15), p. 7,
   boxed and called "a new result".
4. **A Kraus decomposition exists**, Source A §3.3, eqs (25)–(27), p. 10; and hence, **by the
   Stinespring dilation theorem**, one may take `Θ = U` unitary after dilating `C` to `C̃` of size
   `Ñ ≤ N³` — Source A §3.4, p. 10. The dilated transition matrix marginalizes over the ancilla back
   to `Γ`. Source A calls this "the inevitability of unitary time evolution in quantum theory";
   Source B §3.5, p. 17, restates it and notes the argument "establishes the existence but not the
   uniqueness of Kraus operators".
5. **Born-rule form on the dilated system.** `Γ_ij(t ← 0) = |U_ij(t ← 0)|²`, Source A eq (30), p. 11;
   equivalently the unistochastic property, Source C §3.5, eq (68), p. 17.
6. **Hilbert space, complex numbers, linear-unitary evolution and the Born rule as outputs.**
   Source C §4.2, p. 18: the proof "will show that every indivisible stochastic process corresponds
   to a unitarily evolving quantum system in a Hilbert space. One thereby turns some of the puzzling
   axiomatic ingredients of quantum theory — the complex numbers, Hilbert spaces, linear-unitary time
   evolution, and the Born rule in particular — into the output of a theorem."
7. **Hamiltonian, von Neumann, Schrödinger and Ehrenfest equations**, Source A §3.4, eqs (33)–(36),
   pp. 12–13 — **conditional on** `U(t ← 0)` being a differentiable function of `t` (stated as a
   hypothesis at eq (33); Source B eq (69), p. 18, repeats the differentiability condition). Not
   available for a purely discrete `T` without that added structure.

**Interpretive, or developed by construction rather than proved.**

8. **Interference.** Source A §3.5, eq (43), p. 14: the discrepancy between `Γ(t ← 0)` and its
   "would-be division" `Γ(t ← t′)Γ(t′ ← 0)` is computed, and the text concludes: "the right-hand side
   of (43) gives the general mathematical formula for quantum interference … interference is a direct
   consequence of the stochastic dynamics not generally being divisible." This is a derivation
   within the framework, not a theorem statement, and it is the **sole** place where failure of
   divisibility does load-bearing work. It is what makes the role axis **BR3** rather than BR2.
9. **Division events and the Markov approximation.** Source A §3.7, pp. 16 ff. Explicitly
   approximate — fn 18, p. 19: "Although generically always approximate, division events will become
   nearly exact when the environment is sufficiently macroscopic".
10. **Decoherence.** Source A §3.8, eqs (59)–(60), p. 19. Constructed from the §3.7 division-event
    model.
11. **Entanglement.** Source A §3.9, eqs (63)–(66), pp. 19–20: loss of tensor-factorization of
    `Γ^{AB}(t ← 0)` under interaction, and its restoration relative to a later division event. A
    model-independent **definition** of interaction is offered here, not a theorem.
12. **Measurement, emergeables, wave-function collapse, the measurement problem, the uncertainty
    principle.** Source A §4, §§4.1–4.5, pp. 21 ff. No theorem environments.
13. **Empirical equivalence to textbook quantum theory.** Announced, not proved, in the sources
    examined: Source A §2.2, p. 6 — "these first-order conditional probabilities will be enough to
    give agreement with all the empirical predictions of quantum theory".
14. **The converse direction (quantum → indivisible stochastic).** Source C §4.2, p. 19, states it
    **by citation to other work**: "As shown in other work (Barandes 2025), one can go in the other
    logical direction and show that any quantum system that includes measuring devices and observers
    as part of the system can be modeled as an indivisible stochastic process." Within the three
    sources examined, this direction is asserted rather than proved; Source B, which is the cited
    2025 paper, presents §3 as a **review** of the correspondence and states no theorem of its own.
15. **Composite systems and subsystems.** Source C §3.4, eqs (65)–(66), p. 17: subsystems of a
    composite generically **lack** well-defined transition maps of their own and so are not
    themselves indivisible stochastic processes in the sense of (24). This is a structural
    observation and is worth flagging for Track I's Arc E, which asks about composites.

## 5. Effect on merged descriptions in this corpus

**One surface is destabilized; one is confirmed.**

**Confirmed — `papers/Main.md` §3.1.** The merged text already states the finding this round
reached, and states it correctly: "the source's membership conditions are the tuple's own — a finite
configuration space, transition maps normalized and trivializing at the conditioning time, a prior,
and the observable algebra — not a divisibility property. Divisibility failure is generic in the
class rather than a condition of entry, so P-indivisibility is not what admits the framework's
processes to it." Line 204 of the same section calls the class "its term of art for the tuple class,
which includes Markov chains". Both are exactly right against Source C §3.1 eq (24) and §3.3
eq (54). No change is called for, and none is made.

**Destabilized — `papers/Explainer.md` line 287** (and its built artifact `papers/Explainer.tex`,
line 833), in the section "The Stochastic-Quantum Correspondence (§3.1 and Appendix A)":

> "**The core statement.** Any P-indivisible stochastic process on a finite configuration space of
> size n can be embedded into a unitarily evolving quantum system."

The source theorem is Source C eq (69): "**Every indivisible stochastic process** can be regarded as
a subsystem of a unistochastic process", where "indivisible stochastic process" is the tuple-class
name of eq (24), not a failure predicate. The sentence as merged is not false — every process
satisfying our `PIndivisibleWithin` and instantiating the tuple is in the class, so the stated
instance holds — but it places a failure predicate in the slot the source fills with a class name,
which is precisely the BD3 conflation. Two nearby lines in the same file already carry the correct
breadth ("a broad one, including Markov chains", line 293; "every process in the source's class
embeds in a unistochastic one; P-indivisibility makes it nontrivial", line 1011), so the file is
internally uneven rather than uniformly wrong.

**This round performs no manuscript edit**, per control 4 and the freeze's non-doings. The item is
recorded as backlog with its surface named, for a later round to carry under the corpus's own
propagation discipline (`§A.25`), together with the rebuild of `papers/Explainer.tex`.

**The role finding.** The freeze states that BR2 or BR3 means P-indivisibility has a different
logical role from the one the manuscript gives it. Against `Main.md` §3.1 that is already the role
the manuscript gives it, so the finding lands as confirmation there and as a backlog item only at
the Explainer surface above. Nothing else in the corpus is touched.

## 6. What the next Track B round can begin from

Stated, not executed.

1. **The Lean transpose bridge**, which is step 5 of the Amendment 2 sequence and which this round's
   freeze deferred. The statement it should prove is now fixed by the transposition above: for
   `Γ : ℕ → Matrix V V ℝ`,

       Γ t = Γ s * Λ ∧ IsRowStochastic Λ  ↔  (Γ t)ᵀ = Λᵀ * (Γ s)ᵀ ∧ IsColStochastic Λᵀ,

   with `IsColStochastic` defined as the transpose-dual of `IsRowStochastic`, plus the
   `PDivisible` restatement over the transposed family. This needs no primary source and no new
   hypothesis; it converts the prose transposition of this round into evidence of hierarchy level 2.

2. **A tuple-instantiation lemma.** Q8 shows the merged datum supplies four of six components
   outright and leaves `T₀` and `p` to be declared. A formal `BarandesTuple` structure carrying
   `(C, T, T₀, Γ, p, A)` with the normalization (28) and trivialization (29) conditions, together
   with an instance built from `RootedRealization`, would make "our processes are in his class" a
   checkable statement rather than a prose one. Note what it would **not** be: it would not be a
   proof of any indivisibility relation, and BD3 means no such relation is available.

3. **The question BD3 leaves open.** Since the class predicate and `PIndivisibleWithin` are
   predicates of different kinds, the useful next question is not equivalence but **what our
   `PIndivisibleWithin` adds on top of class membership**. Source A §3.5 eq (43) says what it adds
   in his framework: the interference term. Whether the OI processes of §2.3 make that term nonzero,
   and at what horizon, is a well-posed question that this round does not answer and does not
   prejudge.

4. **Source C §3.4's subsystem observation** (item 15 above) bears on Arc E's composite question and
   should be read before Arc E is scoped. Track separation applies: it is a Track B observation and
   is not evidence for any Track I result.

## 7. Evidence type and what remains undetermined

**Evidence type by question.** Q1, Q2, Q3, Q5, Q6, Q9 — primary source at pinpoint locations only.
Q4 — primary source at pinpoint locations plus a prose transposition, the transposition itself
carrying hierarchy level 3 until the Lean bridge of §6.1 is proved. Q7 — primary source plus the
this-side reading of `rootedMap` at `t = 0` from merged Lean. Q8 — primary source for the tuple's
requirements, merged Lean source for what our datum carries.

**Kernel status.** No Lean was written or built this round, so there is no kernel status to report
beyond the merged corpus's existing one. The round adds no `#print axioms` line and changes no
proof.

**Mathematical status.** No theorem is proved or claimed. Every determination above is about what a
text says.

**What remains undetermined.**

- **Whether the class-name divergence between Source A and Source C is a change of position or of
  presentation.** Q3 records two formulations of divisibility across two versions dated eight months
  apart. Which one Barandes would call authoritative is not fixed by the texts examined, and the
  audit does not guess. Both are reported; neither is projected onto the other.
- **Whether Source A's generic-indivisibility claim is ever established at our strength for a class
  rather than for examples.** Source A p. 5 proves existential failure for the eq (7) family. No
  location examined proves it for a general member of the class, and none is claimed.
- **The converse direction's proof.** Item 14 above: asserted by citation within the three sources
  examined, not proved in any of them. A later round wanting it must locate the proof rather than
  inherit the assertion.
- **Everything about the operational layer.** Q9 items 8–13 are interpretive or constructed. Whether
  any of them can be strengthened to theorem level, and under what hypotheses, is untouched here.

**On the recorded prediction.** The freeze predicted **BR2** on the role axis at roughly two-to-one
against BR1, and recorded no prediction on the definition axis. The outcome is **BR3**. The
prediction's substance — that failure of divisibility is not a hypothesis of the basic
correspondence — is confirmed at six primary-source locations (Q5). Its **label** is not: BR3 is the
label that fits, because Source A §3.5 eq (43) puts failure of divisibility to work downstream, for
interference specifically, and the prediction did not name that use. Recorded as a miss at label
level and a hit on the underlying proposition, with no retrofitting of either.

## 8. This is not a sourcing claim

Explicitly, and as control 9 requires: **nothing determined in this round is a claim that OI sources
anything.**

What a correspondence theorem supplies under its own hypotheses is a different claim from what OI
sources. Source C's theorem (69) supplies a unistochastic dilation to every finite-configuration
member of its tuple class, under its own hypotheses, from transition data given to it. That says
nothing about which resources embedded observation makes available, and Arc D round 1's boundary is
untouched: representational presence remains a disqualified ground for any sourcing claim, exactly
as `verification/programmes/oi-qm/track-i/arc-d-operational-sourcing/result.md` establishes at RD1.

Track separation is likewise binding and observed: nothing determined here is used as evidence for
any Track I result, and no Track I result was used as evidence for a determination here.

No resource deferred by the Arc D preregistration is adjudicated. No fifth condition is named or
adopted. No merged Arc B, C or D result is reopened, restated or re-proved. No Arc D round 2 or
Arc E work is begun.
