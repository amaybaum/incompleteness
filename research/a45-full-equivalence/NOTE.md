# A45 — full-equivalence closure (disposable research, L41-based)

Base: L41 = `fa6ddf77703a8ce7f9eaf573ef48355194d72541`. Branch `claude/a45-full-equivalence-closure-research`. Not a
native round: no `F`, no receipt, no pull request, no claim about any landed verdict. Sections 0–2 are written before any
result of this thread and are not edited afterwards; results go in later sections, deviations are recorded there.

## 0. Goal and dependencies

**Goal.** Determine whether all admissible static realizations identified by the current Track-B geometry induce the
same operational object, or exhibit the first certified operational obstruction.

**Dependencies, fixed at the outset.**

- **A44 (operational bridge) is the primary dependency.** Closure needs either a certified map from static realizations
  to the operational object, or a theorem that the operational construction factors through a quotient already known to
  identify the realizations.
- **A43 (family generalization) is potentially helpful, not blocking.** It bears on the shape of the full static quotient
  and on whether Diţă status is intrinsic under all isometries of the normalized set; an abstract invariance argument can
  bypass a complete classification.
- **A42 (support minimality) is non-blocking unless it reveals a new equivalence invariant.** The least support of a
  non-Diţă straight line does not bear on whether operational data collapse the static distinctions.
- **A41 is the foundation**: its corrected semantics (partition structure, alignment, factorization class, partition
  orbit) are the static vocabulary here. Pre-L41 threads (A42–A44) are sources of candidates and algorithms, not evidence.

## 1. What the corpus already fixes (read at L41; K = kernel, P = prose)

- **The open target is definitional.** `ROADMAP.md` (programme interpretation boundary) states the fork: the residual
  lift freedom is physically redundant, or additional structure selects one quantum history, or observational
  incompleteness determines only an equivalence class of quantum histories; a physics-beyond-QM claim needs a residual
  "not removed by the physically appropriate equivalence relation". Act 14's preregistration (P) records that until that
  relation "is written down as an object, 'the freedom is gauge' and 'the freedom is physical' are not statements with
  truth values"; act 14 freezes four carriers `𝒪₀`–`𝒪₃` and adopts none.
- **The Q_fb operational datum depends on visible data only, by definition** (K, `QuantumRepresentation.lean`):
  `QfbData.born b b' := ‖U b' b‖²`, and `bornPow`, `jointMass`, `rooted` and `QStar` are built from `born`, `init`
  and `read` alone. No congruence lemma is stated.
- **Every admissible static realization has the same visible slice.** At the product configuration every flat unitary
  `H` gives an admissible dilation `pad H` of `Γ₀ ⊗ Γ₀ = J/16` (K, `a35_shared_gram_realizable`), and every act-9
  admissible readback returns that slice (K, `rb3_of_admissible`; A44's I4).
- **The lift-level classes are separated by a frozen carrier.** `twoSided_slice_iff` (K, `TwoSidedGauge.lean:826`)
  identifies the two-sided relation with `GramPhaseEquiv`; A44 (pre-L41) found `𝒪₁` (`AnchoredChannel`) and the Gram
  class detect Diţă status on act 39's family only by completeness (they resolve the whole two-sided class), and every
  coarser named invariant blind.
- **No certified static→operational functor.** No kernel theorem builds `QfbData`, a rooted realization, a Q\* family or
  a `FiniteOperationalTheory` from a Track-B `H`, `pad H`, admissible dilation or coherent lift (A44's Finding N;
  confirmed at L41 by inventory). The operational uniqueness theorems (`quasilocal_characterization`,
  `sameData_unitary_or_transpose`) take operational data or quasilocal systems as input, not Track-B realizations.

## 2. The three questions, with decision rules fixed in advance

**Q1 — the target relation.** Write down, for each certified operational object `𝒪` defined in the corpus, (a) its
input type, (b) whether a certified map sends an admissible static realization into that input type, (c) the relation
`~_𝒪` it induces on static realizations. Classify each as:
- *visible*: `𝒪` is a function of the visible data (slice, Born weights, `init`, `read`);
- *lift-level*: `𝒪` is defined on the realization or its dilation and depends on more than the visible data;
- *not applicable*: its input type receives no certified map from a static realization.
The target of Q2/Q3 is stated per class, never as one unqualified "operational equivalence". The strongest statement the
thread could need is the relation of the strongest *applicable* `𝒪` the corpus certifies as operational; if the corpus
certifies none as the physical observable (act 14), that absence is the Q1 finding.

**Q2 — factorization.** For a class of `𝒪`, `FACTORS` iff there is a proof (kernel, written, or exact over the whole
domain) that `𝒪 ∘ (realization ↦ input)` is constant on a quotient that identifies every admissible static
realization of the Track-B geometry (all flat unitaries at the product configuration, and the families through SIG
studied by acts 34–41). Any map into `𝒪`'s input type that the corpus does not certify is named and every verdict is
conditional on it (assumption-watch **AW-static**, carried from A44).

**Q3 — obstruction.** For a class where Q2 does not close, `OBSTRUCTION` iff two admissible static realizations,
statically distinct in A41's semantics (different Diţă status, factorization class or two-sided class), are exhibited
with exactly different values of an applicable, certified `𝒪`. `COLLISION` evidence (equal values across a static
distinction) supports equivalence for that `𝒪` only. Non-constancy is not separation of the relevant classes; one
exhibited pair decides, never a proof of existence alone.

**Interpretation, fixed in advance.** An obstruction for a lift-level carrier is a statement about that carrier, not a
physical distinction, unless the corpus certifies the carrier as observable. A factorization for visible carriers is a
statement that those carriers cannot see the static geometry, not that the geometry is unphysical.

**Controls.** Every Q2/Q3 verdict is void unless: a visible carrier (`𝒪₀`) comes out FACTORS on the full domain; a
carrier known to resolve the two-sided class (`FibreGram`) comes out OBSTRUCTION with an exhibited pair; a toy carrier
that varies but is not class-determined (a single matrix entry) is not mistaken for either; A41's census classifier
reproduces its landed values on any point it is applied to.

**Working hypothesis (to be tested, not assumed).** Because every admissible static realization shares its visible
slice, every *visible* `𝒪` factors trivially; the full-equivalence question then reduces exactly to act 14's open
choice of relation among the *lift-level* carriers, where A44 found separation by completeness. If so, A44's missing
static→multi-time map is load-bearing only for the *not-applicable* carriers, and the shortest closure route is a
certified argument that the physically appropriate relation is visible-level — or else a certified reason it is not.
