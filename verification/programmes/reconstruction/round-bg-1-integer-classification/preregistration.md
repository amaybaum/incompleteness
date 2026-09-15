# Reconstruction round BG-1 — the Bekir–Golomb integer classification: CONTROL PLANE

Owner-called. This file is the whole of round BG-1's control plane and is merged **alone**, before
any execution object exists. It takes up the `P2` queue row *Bekir–Golomb integer classification*,
status `EXTERNAL`, and nothing else.

**Blob identity is authoritative.** The execution guard pins this file by content.

## What kind of round this is, said first

**This round is unusual for the programme: it is a formalization job with a known target, not an
open research question.** Every other live round in this repository asks something whose answer is
not known in advance and whose preregistered targets are propositions that may come back either way.
This one does not. The proposition to be formalized is a published classification theorem; the
repository consumes it as a cited premise, has audited its primary text, has kernel-proved the
passage from it to the statements that use it, and records it as the sole remaining `K3` backlog
item. **Nothing in this round is a prediction about whether the classification is true.**

What that changes, stated plainly: **the uncertainty here is feasibility and cost, not truth.** The
preregistered targets are therefore about what can be *proved in the kernel within a stated budget*,
and every prediction below is a prediction about reachability within that budget and about nothing
else. Accordingly:

> **UNDECIDED is live on every target of this round, and on the main target it means exactly one
> thing: the statement was not formalized within this round's budget. That is a legitimate outcome
> and is not a failure, not a finding about the statement, not a finding about its difficulty, and
> not a bound on what a later round can do.**

The freeze rates UNDECIDED the most likely outcome of the main target and says so in the prediction
table, with its reason. A round that ends there still lands its locating controls, its anti-drift
bridge, its consistency controls and its small-mark case, and it lands a narrowed statement of what
the repository is assuming — which is a result and is reported as one.

## The round's shape, declared in `§A.37`'s terms

**This is a SEALING round.** Under `AGENTS.md` `§A.37` a sealing round is one whose preregistration
prospectively owns seal state — it creates new seal and pin state, or explicitly takes ownership of
changing existing seal state. Quoted verbatim from `AGENTS.md`, **lines 775–784**:

> 1. **A sealing round — a round whose preregistration prospectively owns seal
>    state: either it creates new seal and pin state, or it explicitly takes
>    ownership of changing existing seal state — takes a pin commit `P`, and `P`
>    is mandatory.** `P` sets the constants it owns to `E` and to `L`. Mandatory
>    is not a stylistic preference: in execution mode the guard requires every
>    commit of `git rev-list HEAD ^base` to descend from the base, and once `L`
>    is on the head, that set reaches the sibling rounds merged into main since
>    the freeze, which do not descend from it. Without `P` the guard fails closed
>    on the landing and the round cannot land at all. `P` is what moves the guard
>    to archive mode, where the landing is certifiable.

This freeze creates new seal state. The execution writes a new Lean module with its own guard clause
in `verification/lean/edge_rigidity_probe.py` under the reserved tag **`R7-BGC`**, and that clause
carries the archive-mode seal constants this round fills:

| constant | what it holds | state at execution |
| --- | --- | --- |
| `_BGC_BASE` | the mandated execution base — the merge commit of this control-plane pull request | set by the execution, from the base it is built on |
| `_BGC_SEALED_HEAD` | the sealed execution commit `E` | **present and unset** at execution; set by `P` |
| `_BGC_MERGE` | the landing merge `L` that carries `E` as its second parent | **present and unset** at execution; set by `P` |

So the round lands **`E` → `L` → `P`, and `P` is mandatory.** `P` is the one pin-only commit that
sets `_BGC_SEALED_HEAD` to `E` and `_BGC_MERGE` to `L`, moving the `R7-BGC` clause from execution
mode to archive mode. Without `P` the execution-mode ancestry check fails closed on the landing,
because `git rev-list HEAD ^_BGC_BASE` at `L` reaches the sibling rounds merged into `main` since
this freeze, which do not descend from the base.

**The shape does not depend on the outcome.** The `R7-BGC` clause and its three constants are
created by the execution in **every** outcome of every target, UNDECIDED on the main target
included. `§A.37` fixes this at **line 801**: "So the freeze names the shape, and the diff does not.
Read the freeze before building a landing rather than inferring a shape from which files moved."

**What this round does NOT own.** It alters **no existing seal constant**. Every `_*_BASE`,
`_*_SEALED_HEAD` and `_*_MERGE` already present in `verification/lean/edge_rigidity_probe.py` — the
seals of every earlier round, without exception — is **read and never written**. The governing
sentence, quoted verbatim from `AGENTS.md`, **lines 793–799**:

> **An archive seal belongs to the round that set it, and stays immutable
> afterwards.** A later round does not re-pin it, and does not acquire a pin
> commit merely by touching the guard file that carries it. An existing seal
> constant changes only in a round whose own preregistration says in advance
> that it changes it — and such a round is *sealing*, because it has taken
> ownership of that state prospectively rather than as a side effect of its
> diff.

The execution's diff against `verification/lean/edge_rigidity_probe.py` **adds** the `R7-BGC` clause
and changes nothing else in that file.

## Locating controls — the governing passages at the base, each with a coordinate

The base is `main` at **`b78eac870ba3ee9ef9e98659ac933bf97dc62226`**. Every quotation in this
section is verbatim from a blob pinned in the start-state table below.

### L1 — the queue row, `verification/ROADMAP.md` line 68

> | **P2** | Bekir–Golomb integer classification | Reconstruction | **EXTERNAL** | removes the last reconstruction premise |

### L2 — what `EXTERNAL` means, `verification/ROADMAP.md` line 27

> | **EXTERNAL** | A published result consumed as a cited premise. Formalizing it is an independent job; until then it is an assumption, and every result above it says so. |

**This is the label the round is working against, and the label it leaves in place unless the
premise-removal gate below is passed in full.**

### L3 — the `P2` section, `verification/ROADMAP.md` lines 774–781

> ### P2 — Bekir–Golomb integer classification
>
> `TurnpikeScopeTransfer.lean` consumes `BGIntegerClassification` as a cited premise. Everything around
> it is kernel-proved — the integer-to-real passage and the final assembly included — and the probe's
> own scope block names it the sole remaining K3 backlog item. Formalizing the 2007 classification is
> an excellent independent job and can run in parallel with everything above it.
>
> → [`lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean`](lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean)

### L4 — the probe's scope block, `verification/lean/edge_rigidity_probe.py` lines 20037–20043

The block is printed narrative. Quoted as the strings the file carries, in order:

> `'     hyperbola IS the reflection branch). twoBranch_of_spectral_classification now needs'`
> `'     only equal probabilities + distinct gaps + a purely SPECTRAL classification. NOT'`
> `'     settled in the kernel: the integer Piccard/Bekir-Golomb classification itself,'`
> `'     consumed as the cited premise BGIntegerClassification -- the manuscript two-branch'`
> `'     THEOREM is graded K2 on it, with the integer-to-real passage kernel-proved'`
> `'     (TurnpikeScopeTransfer.lean); formalizing the 2007 classification is the sole'`
> `'     remaining K3 backlog item.'`

**This is the passage the `P2` row means by "the probe's own scope block names it the sole remaining
K3 backlog item", located and confirmed at the base.**

### L5 — the manuscript's own consumption, `papers/GR.md` line 178, first sentence

The line is one long paragraph; the quotation is its opening sentence, verbatim and complete.

> The proof is kernel-verified end to end (`verification/lean-mathlib/OIBridge/`, composed statement `twoBranch_of_BGClassification`), with a single exception consumed as a cited external theorem: the integer classification of Bekir–Golomb, stated in the kernel as the explicit premise `BGIntegerClassification` — in the integer scope the cited text uses, the passage from integer to real spectra being proved, not assumed.

### L6 — the programme file, `verification/programmes/oi-qm/PROGRAMME.md` line 597

> The reconstruction programme's two-branch theorem is graded K2 rather than K3 on a single unformalized input: the integer Piccard/Bekir–Golomb classification, carried in the kernel as the `Prop` `BGIntegerClassification` in `OIBridge/TurnpikeScopeTransfer.lean` and consumed as a cited external premise. That module records it as the only unproved input of the reconstruction programme. Every other step is kernel-proved, including the integer-to-real passage and the assembly `twoBranch_of_BGClassification`, and three probes record formalizing the 2007 classification as the sole remaining K3 backlog item.

## The exact statement of `BGIntegerClassification`, as the tree has it and as it is consumed

**This section is the anti-drift anchor of the round.** The formalization target is the `Prop` below
and no paraphrase of it. Quoted verbatim from
`verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean`, **lines 534–552** — the docstring
and the definition together, because the docstring is where the tree records what the `Prop` is for:

```lean
open HomometricSix in
/-- **THE EXTERNAL INTEGER PREMISE — Bekir–Golomb 2007, in the spectral form this repository
consumes.** Any two strictly increasing INTEGER rulers with distinct internal differences and
equal difference sets that are neither translates nor reflections of one another exist only at
six marks, with gap data realizing the exceptional correspondence μ through explicit
relabelings (the equivalences force `n = 6` with no casts). The μ-form of the exceptional
clause is backed by `PiccardBridge`: the paper's own two-parameter family is kernel-proved to
realize μ this way. This `Prop` is the ONLY unproved input of the reconstruction programme. -/
def BGIntegerClassification : Prop :=
  ∀ (n : ℕ) (F F' : Fin n → ℤ),
    StrictMono F → StrictMono F' →
    (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d) →
    (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d) →
    (Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ) →
    (¬ ∃ c : ℤ, ∀ i, F' i = F i + c) →
    (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) →
    ∃ eS eT : Fin 6 ≃ Fin n, ∀ a b : Fin 6, a < b →
      F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS b) - F (eS a)
```

with `AscPair` from the same file, **line 309**:

```lean
abbrev AscPair (n : ℕ) := {p : Fin n × Fin n // p.1 < p.2}
```

and `mu` from `verification/lean-mathlib/OIBridge/HomometricSix.lean`, **lines 58–66**:

```lean
/-- The forced correspondence on ascending pairs: `mu a b` is the R₂-pair with the same gap. -/
def mu : Fin 6 → Fin 6 → Fin 6 × Fin 6
  | 0, 1 => (0,1) | 0, 2 => (4,5) | 0, 3 => (1,3) | 0, 4 => (1,4) | 0, 5 => (0,5)
  | 1, 2 => (2,3) | 1, 3 => (2,5) | 1, 4 => (0,3) | 1, 5 => (1,5)
  | 2, 3 => (3,5) | 2, 4 => (0,2) | 2, 5 => (0,4)
  | 3, 4 => (3,4) | 3, 5 => (1,2)
  | 4, 5 => (2,4)
  | _, _ => (0,0)
```

### How the premise is consumed, quoted with coordinates

It is consumed at exactly two places in the tree, both in
`verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean`, and in both it enters as a named
hypothesis `hBG` of that `Prop` and is not unfolded:

**Line 563**, the head of `spectral_classification_of_BG`:

```lean
theorem spectral_classification_of_BG (hBG : BGIntegerClassification)
```

**Line 826**, the head of `twoBranch_of_BGClassification`:

```lean
theorem twoBranch_of_BGClassification (hBG : BGIntegerClassification) {m : ℕ} (hm : 3 ≤ m)
```

and the closing line of that theorem's docstring, **line 825**:

> `Every step other than `BGIntegerClassification` is kernel-proved. -/`

**Consequence, frozen.** A round that proves anything other than the displayed `Prop` — including a
statement that is provably equivalent to it but not definitionally it — does **not** discharge those
two hypotheses by name. The premise-removal gate below turns on this and on nothing softer.

## What the surrounding kernel already proves — the round does not re-prove any of it

The following are merged, named, and axiom-clean at the base, and are **consumed unmodified, at
their own strengths**. **No target of this round re-proves any of them, and no artifact of this
round restates one as its own result.**

| result | file | what it gives |
| --- | --- | --- |
| `rational_point` | `OIBridge/TurnpikeScopeTransfer.lean` line 57 | a rational point near a real one preserving finitely many rational strict and nonzero linear conditions |
| `rational_solutions` | same, line 156 | the same with equality constraints added, through a ℚ-basis of the span of the real solution's entries |
| `exists_int_scaling` | same, line 255 | denominators cleared, every constraint being homogeneous |
| `integer_realization_of_real_realization` | same, line 316 | a real ruler pair realizing a fixed ascending-pair correspondence yields an **integer** pair realizing the same one, with strict ordering, Golombness and both nontriviality witnesses preserved |
| `spectral_classification_of_BG` | same, line 563 | the **real** spectral trichotomy, *derived* from the integer premise |
| `gaps_eq_of_equal_probabilities` | same, line 759 | equal transition probabilities give equal gap sets |
| `twoBranch_of_BGClassification` | same, line 826 | the composed two-branch theorem over arbitrary real spectra, conditional on the integer premise alone |
| `twoBranch_of_spectral_classification` | `OIBridge/CongruentReconstruction.lean` line 752 | the two branches from equal probabilities, distinct gaps and a purely **spectral** classification premise |
| `twoBranch_of_PiccardClassification` | same, line 713 | the same at the coefficient level, with `ExceptionalMatch` as the third alternative |
| `coefficient_line_extraction`, `coefficients_by_frequency_determined` | `OIBridge/FrequencyMatching.lean` | probabilities determine every frequency amplitude; distinct gaps extract each coefficient line |
| `homometricSix_unrealizable` | `OIBridge/HomometricKill.lean` | the forced non-two-branch six-mode correspondence admits no pair of unitary eigenbases with all overlaps nonzero |
| `golomb_r1`, `golomb_r2`, `mu_gap`, `mu_forced`, `mu_muInv`, `muInv_mu`, `mu_not_vertex_induced`, `flat_locus`, `no_six_orthogonal`, `three_clique` | `OIBridge/HomometricSix.lean` | the printed pair's Golombness, μ's forcedness and bijectivity, and the two finite endpoints of the six-mark kill chain |
| `piccard_mu_bridge`, `piccard_realizes_mu`, `piccard_factor_r`, `piccard_factor_s`, `piccardX_at_printed`, `piccardY_at_printed` | `OIBridge/PiccardBridge.lean` | the cited two-parameter family realizes μ as a polynomial identity over any commutative ring, and the printed factorization expands to the quoted mark lists |
| `k4_rigidity`, `exceptional_relation`, `orientation_coherence` | `OIBridge/EdgeRigidity.lean` | `K4`-rigidity for `n ≥ 5` with the `n = 4` exception sharp, and the two directed lifts of an induced correspondence |

**What this table is for.** The `P2` row's sentence "Everything around it is kernel-proved — the
integer-to-real passage and the final assembly included" is located here, item by item, so that the
round's scope is the premise and only the premise. **The integer-to-real passage is not this round's
work and is not restated as this round's work**; neither is the six-mark kill chain, neither is the
Fourier layer, and neither is the congruent-case assembly.

## What "the 2007 classification" is, as the record cites it — and in how many forms the tree states it

### The citation, with coordinates

From `verification/lean-mathlib/OIBridge/PiccardBridge.lean`, **lines 4–6**:

> `PROVENANCE, NOW AT PRIMARY-SOURCE LEVEL. Bekir–Golomb, "There Are No Further Counterexamples`
> `to S. Piccard's Theorem", IEEE Trans. Inform. Theory 53(8) (2007) 2864–2867 (p. 2865, family`
> `attributed to Yovanof–Golomb, ARS Combinatoria 48 (1998) 43–48), represents the unique`

From `papers/GR.md`, **line 176** — one long proof paragraph — the sentence that names the classical
input, quoted verbatim and complete:

> For integer spectra the classification is the completed Piccard theorem: two rulers with all internal differences distinct and the same difference set are identical or mirror images, except for a single two-parameter six-mark family [A. Bekir and S. W. Golomb, IEEE Trans. Inform. Theory 53 (2007) 2864–2867].

From `verification/coverage/LEDGER.json`, the `delta` field of entry
`GR:T-d-gauge-completeness-two-branch`:

> K2, not K3, for exactly one named external step: the integer Piccard classification (Bekir-Golomb, IEEE Trans. Inform. Theory 53 (2007) 2864-2867) is consumed as a cited theorem, stated in the kernel as the explicit premise BGIntegerClassification (TurnpikeScopeTransfer.lean) in the integer scope the primary text unambiguously uses.

### The audit caveat the tree carries about the cited text's scope

From `verification/lean-mathlib/OIBridge/PiccardBridge.lean`, **lines 23–28**, beginning at the
point on line 23 where the caveat starts:

> `AUDIT CAVEAT THAT REMAINS: the 2007`
> `text presents its polynomial model with integer marks-as-exponents and never explicitly`
> `quantifies over real configurations; its Section III argument manipulates symbolic exponents`
> `through linear relations only (hence is domain-agnostic), but the real-scope reading is an`
> `interpretation, recorded in the ledger, not a sentence of the paper. This bridge already`
> `delivers the third alternative of `twoBranch_of_spectral_classification` in its verbatim shape.`

**This caveat is why the premise is stated in the integer scope, and it is why this round's target is
the integer statement and not a real-scope one.** The round does not reopen the scope question: it
is closed mathematically by `integer_realization_of_real_realization`, which is merged.

### In how many forms the tree states the classification: several, and exactly one is the premise

**The answer is: several, and the difference between them is the round's principal hazard.** The
forms present at the base, enumerated with coordinates:

| # | form | where | status in the tree |
| --- | --- | --- | --- |
| 1 | `BGIntegerClassification`, the integer premise quoted above | `OIBridge/TurnpikeScopeTransfer.lean` line 542 | **a `def … : Prop`, consumed as a cited premise. This is the round's target.** |
| 2 | the **real** spectral trichotomy | `OIBridge/TurnpikeScopeTransfer.lean` lines 569–572, as the *conclusion* of `spectral_classification_of_BG` | kernel-proved **from** form 1; it is a theorem, not a premise |
| 3 | the same real spectral trichotomy as the `hclass` hypothesis | `OIBridge/CongruentReconstruction.lean` lines 761–765 | a hypothesis of a merged theorem, discharged by form 2 |
| 4 | the coefficient-level trichotomy with `ExceptionalMatch` | `OIBridge/CongruentReconstruction.lean` lines 717–726 | a hypothesis of `twoBranch_of_PiccardClassification`, manufactured from form 3 by `coefficient_line_extraction` |
| 5 | the exceptional family realizing μ | `OIBridge/PiccardBridge.lean` `piccard_realizes_mu` | kernel-proved; it backs form 1's μ-shaped exceptional clause and is **not** a statement of the classification |
| 6 | the prose statement | `papers/GR.md` line 176; `verification/coverage/LEDGER.json` entry `GR:T-d-gauge-completeness-two-branch`; `OIBridge/PiccardBridge.lean` lines 4–6 | citation prose, carrying no Lean object |

**Forms 2, 3 and 4 are not the premise.** They are real-scope or coefficient-scope statements, and
they are consequences of form 1 rather than restatements of it. **Form 5 is not the premise either**:
it says the cited family *realizes* μ, which is the exceptional clause's witness direction and not
the classification's universal direction. `BG0` below makes this enumeration a target of the round,
settled by locating and quoting, so that the execution has it on its own search rather than on this
freeze's word.

## The evidence rule for type-P components, FROZEN

`BG0` and `BG1` are settled by **locating and quoting**, not by proving a theorem. The rule below
binds the execution:

1. Evidence is a **verbatim quotation** from a pinned blob, with its file path and line coordinate;
   or
2. a **verbatim quotation** from a merged result note, preregistration or ledger field, with its
   coordinate; or
3. an explicit, recorded statement that **the passage sought does not exist** on the record
   searched, with the search **named and bounded** — the file set enumerated, the search terms
   listed, and the result recorded for each term.

**Reconstructive inference is forbidden as a finding.** A determination of the form "the record must
contain X, because otherwise Y would not have been written" may appear only in a clearly labelled
analysis paragraph that states it is not evidence and that no target rests on it. **Where the record
is silent, the finding is that it is silent** — not that the thing sought is false, and not that it
is true.

**The bounded search is fixed now**, so that its boundary cannot be chosen after its result is
known:

- **The file set**: every `*.lean` file under `verification/lean-mathlib/`; every `*.py` file under
  `verification/lean/`; `verification/coverage/LEDGER.json`; `verification/ROADMAP.md`;
  `verification/programmes/oi-qm/PROGRAMME.md`; and `papers/GR.md`, `papers/Main.md`, `papers/SM.md`,
  `papers/Explainer.md`.
- **The search terms**: `BGIntegerClassification`, `Bekir`, `Golomb`, `Piccard`, `turnpike`,
  `homometric`, `spanning ruler`, `difference set`, `mu_forced`, `ExceptionalMatch`,
  `twoBranch_of_`, `classification`.
- **The question asked of each hit**: does this passage state the integer classification — for
  **every** mark count and **every** pair of integer rulers satisfying the hypotheses — or does it
  state a consequence, a witness, a real-scope variant, or citation prose?
- **The recorded answer per hit** is one of: *is the premise* (quoted, with coordinate); *is a form
  of the classification other than the premise, and which* (quoted, with coordinate); or *not a
  statement of the classification*.

The execution records the search in the result note in full. **A search that finds a further form is
a finding, and a search that finds none beyond the six enumerated above is equally a finding.**

**`BG1` adds no external reading.** This lane is blind and this round performs **no** re-audit of the
primary 2007 text, no literature search and no external fetch. `BG1` is settled from pinned blobs
only. Where the record's description of the cited argument is all the round has, the round says that
is all it has.

## Start state, pinned by blob

Pinned **by blob** at this freeze's base, `main` at `b78eac870ba3ee9ef9e98659ac933bf97dc62226`.
Blob identity is authoritative: the commit locates the tree, the blob is what is compared.

| path | blob |
| --- | --- |
| `AGENTS.md` | `c51e4fb7b101e6907e23c0ca0c0ccd6e16ec2d08` |
| `papers/GR.md` | `0258ccb7a5ef02877a01638428ae7ab8ba91bf71` |
| `verification/coverage/LEDGER.json` | `7fd6a369c473520832223fa746cb2b8295d6ae9d` |
| `verification/programmes/oi-qm/PROGRAMME.md` | `56b399443d19c65c315a935647147e6749356add` |
| `verification/lean/gap_correspondence_probe.py` | `7a951f2238ef3c7b0c2474f2efb855429d4b5e7b` |
| `verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean` | `79f5bd95d07a154caf09fcf04d5e26edcb064206` |
| `verification/lean-mathlib/OIBridge/CongruentReconstruction.lean` | `9e17bf4e78afb46055f922afd2e7cc7632d63247` |
| `verification/lean-mathlib/OIBridge/HomometricSix.lean` | `eb387471d927960f8de43254a3614d78ba2648c5` |
| `verification/lean-mathlib/OIBridge/HomometricKill.lean` | `2b7736dcb4eae27ae5c2dc2cadb99aec0a019853` |
| `verification/lean-mathlib/OIBridge/PiccardBridge.lean` | `1d73ab92825cb87e528242be51f5aa3139245577` |
| `verification/lean-mathlib/OIBridge/FrequencyMatching.lean` | `efd828d5913bba3b37195a07b77d1a32200a993b` |
| `verification/lean-mathlib/OIBridge/EdgeRigidity.lean` | `51ac26c42e695583175ee8d934cf82e72283e85a` |
| `verification/lean-mathlib/OIBridge/BohrFrequency.lean` | `295dcacc4b3a31bafbd10d290a1c2f4d98ae85cc` |

Every one of these is read and never written by this round. If any blob differs at the base, the
execution records the discrepancy and does not repair the freeze.

**The files this round writes are named separately and are not in the table above**, because the
clause just given does not apply to them. Each is pinned by blob at this base all the same, so that
a discrepancy in what the round writes onto is as visible as a discrepancy in what it reads:

| path | blob at this base | what the round does to it |
| --- | --- | --- |
| `verification/ROADMAP.md` | `5ee35552fbfb41bd3172d3e3053c1a6d860a16d1` | **read** as the pinned statement of the `P2` row, the `P2` section and the status vocabulary, and **written** only by appending the frozen post-round sentence for the case reached; the row's label changes only if the premise-removal gate is passed in full |
| `verification/lean/edge_rigidity_probe.py` | `6e334e832d99851e7a275842c1bdd856cbeb09f7` | the `R7-BGC` clause **added**; **no existing seal constant altered**; the scope block at lines 20037–20043 amended only if the premise-removal gate is passed in full |
| `verification/lean-mathlib/OIBridge.lean` | `0bff51eb9cc3c22859da2ac0efc622910e77d7b4` | one import line added for the round's module |
| `verification/coverage/LEDGER.json` | `7fd6a369c473520832223fa746cb2b8295d6ae9d` | the `checks` list of entry `GR:T-d-gauge-completeness-two-branch` gains the round's module; its `kernel` grade changes **only** if the premise-removal gate is passed in full |
| `verification/lean-mathlib/OIBridge/TurnpikeClassification.lean` | — | created by the execution |
| `verification/programmes/reconstruction/round-bg-1-integer-classification/result.md` | — | created by the execution |

`verification/coverage/LEDGER.json` and `verification/ROADMAP.md` are the two files this round both
reads and writes, and they are listed here rather than above for exactly that reason: the verbatim
clause governs the read-only table without qualification, and each file's treatment is stated in its
own row. If either blob differs at the base, the execution records the discrepancy and does not
repair the freeze.

### The anti-contamination invariant, verbatim

> A start-state discrepancy does not license the execution to consume the newer sibling result
> merely because it happens to be present at its mandated base. The round consumes only what its
> freeze says it consumes.

**Its `§A.37` justification.** `§A.37` makes the control plane's merge commit the mandated execution
base and requires the execution to branch "from exactly that commit and from nothing else", with its
first act the verification that the preregistration at that base carries the blob the freeze names.
That base is a commit on `main`, so it carries whatever sibling rounds merged between this freeze
and it. `§A.37` also makes the preregistration **immutable** once merged, and requires an execution
that diverges from it to **record the discrepancy** rather than repair the freeze. The two clauses
together are what the invariant states: the base fixes *ancestry*, the freeze fixes *inputs*, and a
sibling result reachable from the base is not thereby an input. Reading one as the other would make
a freeze's meaning depend on what merged after it was reviewed — which is exactly the property
`§A.37` says a freeze must not have.

**Why it matters here.** Several sibling lanes are drafting and executing concurrently with this
freeze, and some will merge into `main` before this round's execution begins, so this round's
mandated base will carry results this freeze does not consume.

## The definition budget

The execution introduces **at most three** top-level Lean definitions, and these are the three:

1. **`BGClassificationAt (n : ℕ) : Prop`** — the mark-count slice of the premise: the body of
   `BGIntegerClassification` with `n` fixed, quantified over `F F' : Fin n → ℤ` and carrying the same
   seven hypotheses and the same conclusion, **written from the quoted text and not from memory**.
   Needed because `BG4` and the narrowing report are statements about particular `n`, which the
   monolithic `Prop` cannot express, and because `BG2`'s bridge is what keeps every later target
   anchored to the premise actually consumed. *Needed.*
2. **`BGResidual : Prop`** — `∀ n, 6 ≤ n → BGClassificationAt n`, the narrowed premise the split
   report cites. *Conditional: fires only if `BG4` lands and the main target does not reach
   `BG5-full`.*
3. **A 0/1 polynomial ruler model** — one definition carrying a ruler as the exponent set of a
   0/1-coefficient integer polynomial, in the shape `PiccardBridge`'s `piccard_factor_r` and
   `piccard_factor_s` already work in. *Conditional: fires only if the main target is attempted at
   `BG5-normal-form`.*

**A fourth definition requires its own append-only amendment**, separately frozen and merged before
the work it affects. **No ruler, mark list, correspondence, witness pair or parameter value is a
top-level definition** — each is a bound variable pinned by an equation in the statement that needs
it. `HomometricSix`'s `r1`, `r2`, `mu`, `muInv` and `PiccardBridge`'s `piccardX`, `piccardY`,
`alignT`, `alignEquiv` are **reused, not redefined**, and `AscPair` is reused from
`TurnpikeScopeTransfer.lean`.

## The proof-effort scope, FROZEN — this is the budget UNDECIDED is measured against

**The record's own cost estimate, quoted with its coordinate.** From
`verification/coverage/LEDGER.json`, the `note` field of entry
`GR:T-d-gauge-completeness-two-branch`:

> CASE-COMPLETENESS RIGOR: the classification argument is a narrative geometric construction (negative-term placement in the Phi1 x Phi2 term matrix; nonsingular Ax=b forces the trivial mirror case, singular forces repeated row/column distances or an infinite regress of compensating terms), at correspondence-level rigor with acknowledged informal steps ('It can be proved that...'); a K3 formalization would be a reconstruction, not a transcription -- estimated comparable to or larger than the entire six-mode kill chain (factorization completeness over Laurent rings, the finite two-negative-term case analysis, and a well-founded version of the infinite-regress counting argument).

**The comparison unit, measured at the base.** The six-mode kill chain that estimate names is
`OIBridge/HomometricKill.lean` (871 lines) together with `OIBridge/HomometricSix.lean` (297 lines):
**1168 source lines**, carrying 26 `#print axioms` lines between them.

**The budget, frozen.** One new Lean module,
`verification/lean-mathlib/OIBridge/TurnpikeClassification.lean`, of **at most 1200 source lines**
and **at most 24 named results**, each carrying a `#print axioms` line.

**The budget is deliberately set at the floor of the record's own estimate, and the freeze says so.**
The estimate is "comparable to or larger than" 1168 lines; the budget is 1200. A round whose budget
sits at the floor of the estimate for the full job is a round whose main target is more likely to end
UNDECIDED than to land, and the prediction table below rates it that way rather than pretending
otherwise. **Setting the budget higher would not make the estimate smaller**; it would make the
round's boundary unfalsifiable, which is what a preregistered budget exists to prevent.

**Exceeding either limit requires an append-only amendment**, separately frozen and merged before
the work it affects. **An execution that reaches the limit stops and reports UNDECIDED on whatever
is unfinished** — it does not spend past the budget and report the result as within it.

## The targets, FROZEN

Six targets, `BG0` through `BG5`. Each names what settles it and what evidence counts.

### `BG0` — the premise as consumed, and every form the tree states the classification in

**What is asked.** Locate the `Prop` the two consumers take as a hypothesis; record its text
verbatim with its coordinate; and enumerate, on the bounded search frozen above, every other form in
which the tree states the classification, saying of each whether it is the premise, a consequence, a
witness, a scope variant or citation prose.

**What settles it.** The bounded search, executed and recorded in full.

**What evidence counts.** Rule 1 or 2 of the evidence rule for each located form; rule 3 for a form
sought and not found.

**This is a type-P target.** It is settled by locating and quoting, or by a recorded bounded-search
negative, and by nothing else. **No Lean is written for `BG0`**, and no outcome of `BG0` is a
theorem of this round.

**What `BG0` is not.** It is not a claim that the enumeration in this freeze is complete — that is
what the search is for — and it is not a claim about which form *ought* to be the premise.

### `BG1` — what the record says the 2007 argument is, and what a kernel reconstruction would cost

**What is asked.** Record, from pinned blobs only, what the merged record says the cited
classification is, in what shape its argument runs, and what the record already estimates about the
cost of formalizing it.

**What settles it.** Quotation from the pinned blobs, with coordinates: the `PiccardBridge`
provenance and audit-caveat paragraphs, the `GR.md` citation sentence, and the ledger entry's
`delta` and `note` fields.

**What evidence counts.** Rule 1 or 2 only. **Rule 3 applies if a passage this freeze expects is
absent at the base**, in which case the absence is the finding.

**This is a type-P target**, and it carries no evidence level. **It performs no re-audit of the
primary text.** The record's description of the cited argument is recorded as the record's
description, attributed to the record, and never as this round's own reading of the paper.

### `BG2` — the anti-drift bridge

**The statement.** `BGIntegerClassification ↔ ∀ n : ℕ, BGClassificationAt n`, with
`BGClassificationAt` as budgeted above.

**What settles it.** A Lean theorem at **evidence level 2**, proved by `Iff.rfl` or by one
`constructor`/`intro` pair, consuming `BGIntegerClassification` **by name** from
`OIBridge.ScopeTransfer` and not restating it.

**Why the round has it.** Every later target is a statement about particular mark counts. Without
this bridge those statements would be about a `Prop` this round wrote, and the round's relation to
the premise the tree actually consumes would be an argument rather than a theorem. **With it, the
drift hazard is a kernel obligation instead of a reading.**

**Bounded reading, frozen.** `BG2` is a restatement of quantifier order. **It proves nothing about
rulers**, establishes no case of the classification, and is not progress toward one.

### `BG3` — the premise is consistent and its conclusion is attained at six marks

Two conjuncts, predicted separately and reported separately.

**(a) The printed pair satisfies every hypothesis of `BGClassificationAt 6`.** With `F = r1` and
`F' = r2` from `OIBridge/HomometricSix.lean`: both strictly increasing; both Golomb, by the merged
`golomb_r1` and `golomb_r2`; equal ascending-pair difference-set images; not a translate; not a
reflection.

**(b) The printed pair satisfies the conclusion.** There are `eS eT : Fin 6 ≃ Fin 6` with
`r2 (eT (mu a b).2) - r2 (eT (mu a b).1) = r1 (eS b) - r1 (eS a)` for every ascending `a < b`,
through the merged `mu_gap`.

**What settles each.** A Lean theorem at **evidence level 2**, stated as conjuncts of one theorem.

**Why the round has it.** This is the round's guard against the second-named hazard below. A
statement whose hypotheses are unsatisfiable is provable and worthless; `BG3` (a) exhibits a pair
meeting every hypothesis of the target as stated, so a later weakening that makes the hypotheses
contradictory is visible as a contradiction with `BG3`. **`BG3` (b) does the same for the
conclusion**: it shows the conclusion is attained rather than vacuous at the one mark count where the
classification says it must be.

**Bounded reading, frozen.** `BG3` is about **one exhibited pair**. It is **not** the six-mark case
of the classification, which is the universal statement that every nontrivial homometric Golomb pair
at six marks realizes μ up to relabeling. `BG3` does not establish that, does not bound it, and is
not a step toward it. `golomb_r1`, `golomb_r2` and `mu_gap` **stand as `HomometricSix.lean` states
them** and are consumed, not extended.

### `BG4` — the small-mark case

Two conjuncts, predicted separately and reported separately.

**(a) `BGClassificationAt n` for every `n ≤ 2`.** At `n ≤ 1` any two rulers are translates, so the
sixth hypothesis is contradicted; at `n = 2` equal difference-set images force
`F' 1 - F' 0 = F 1 - F 0`, hence a translate, contradicting the same hypothesis.

**(b) `BGClassificationAt n` for `n = 3`, `n = 4` and `n = 5`.** The hypotheses are jointly
unsatisfiable at each: no pair of strictly increasing integer rulers with distinct internal
differences and equal difference sets at three, four or five marks is neither a translate nor a
reflection of the other.

**Why both conjuncts have that shape, stated so the target is not misread.** The premise's conclusion
asserts the existence of `eS eT : Fin 6 ≃ Fin n`, and such an equivalence forces `n = 6`. So at every
mark count below six the conclusion is uninhabited, and `BGClassificationAt n` there **is** the
statement that the seven hypotheses cannot all hold. That is what `BG4` proves and the only thing it
proves.

**What settles each.** A Lean theorem at **evidence level 2**, stated as conjuncts of one theorem,
by a kernel argument. **No `native_decide`, and no `decide` over an unbounded integer range.**

**Why the round has it.** The cited text records the sub-six-mark case as easily shown and the record
carries that; **this round does not consume "easily shown" as evidence** and either proves it in the
kernel or reports it UNDECIDED.

**Bounded reading, frozen.** `BG4` settles mark counts at most five and nothing above five. **It is
not evidence about six marks or about seven and above**, in either direction.

**The narrowing report, frozen here so that it is not invented later.** If `BG4` (a) and (b) both
land and the main target does not reach `BG5-full`, the execution additionally proves
`BGResidual → BGIntegerClassification` at evidence level 2 and reports **exactly** this:

> The repository's cited premise is narrowed: what stands as assumed is `BGResidual` — the
> classification at six marks and above — with `BGIntegerClassification` kernel-derived from it.
> **The premise stands**, the `P2` row stays `EXTERNAL`, and the ledger entry stays at its grade.
> What changed is the size of what is assumed and not whether something is assumed.

### `BG5` — THE MAIN TARGET: the classification itself, under a strict four-line status hierarchy

**The question, restated over the quoted `Prop` and over nothing else.** Is
`BGIntegerClassification`, as quoted above from `OIBridge/TurnpikeScopeTransfer.lean` line 542,
proved in the kernel within this round's budget — and if not, which of the frozen fallbacks is
reached?

**`BG5` is attempted in this round**, and it is attempted in the frozen order below. The owner's
scope decision is recorded here: the round attempts the main target rather than stopping at
`BG0`–`BG4`, and UNDECIDED is priced accordingly rather than standing in for the attempt.

**The attempt order is frozen** so that a fallback cannot be chosen after its result is known: the
execution attempts line 1; if the budget is not exhausted and line 1 is not reached, it attempts line
2; if the budget is not exhausted and line 2 is not reached, it attempts line 3, taking restriction
**F3a before F3b**. It stops at the budget wherever it is.

**The hierarchy is strict and exhaustive, and the outcome reported is the highest line the kernel
actually carries** — never a higher one:

| # | outcome | statement | earned only by |
| --- | --- | --- | --- |
| 1 | **`BG5-full`** | `BGIntegerClassification` holds | a kernel proof of the quoted `Prop` itself, axiom-clean, with the two consumers re-derived by discharging `hBG` by name. **This is the only line that passes the premise-removal gate.** |
| 2 | **`BG5-normal-form`** | `BGIntegerClassification` follows from a frozen polynomial-model `Prop` | a kernel-proved implication from a `Prop` stated in the 0/1-polynomial model of budget slot 3 to the quoted `Prop`, axiom-clean, with the polynomial-model `Prop` written out in the result note in full. **The premise stands, restated in the cited argument's own shape, and the round says so.** |
| 3 | **`BG5-restricted`** | one of the two frozen restrictions is proved | a kernel proof, axiom-clean, of **F3a** — the classification under the nonsingular branch of the case split the ledger's `note` records, stated as an explicit hypothesis on the ruler pair — or of **F3b** — `BGClassificationAt 7`, the single mark count seven and no other. **No other restriction qualifies**, and any other requires an append-only amendment frozen and merged before the work. **The premise stands and the round says so.** |
| 4 | **UNDECIDED** | none of the above was reached within the budget | the recorded statement that none was reached, with the point at which the budget was reached named, and with `BG0`'s and `BG1`'s findings recorded alongside it |

**A preregistered fallback is a result; one invented mid-execution is not.** Lines 2 and 3 are
written out here, before the round runs, with their statements bounded and their restrictions named.
The execution may report one of them; it may not report a fallback this file does not name.

**What `BG5` may not do.**

- It may not report an outcome at a strength the kernel does not carry.
- It may not report line 1 on the strength of a proof of a statement that is not the quoted `Prop`,
  however close. **The premise-removal gate below is the only route to line 1.**
- It may not report line 2 or line 3 as a removal of the premise, or as a change to the `P2` row's
  label, or as a change to the ledger entry's grade.
- It may not report line 3 under a restriction other than F3a or F3b.
- It may not report line 1, 2 or 3 on the strength of `BG2`, `BG3` and `BG4` together, which are a
  bridge, a consistency control and a case at most five marks.
- **Reporting a settling outcome because the round ran out of budget is the specific error this
  target's status rule exists to prevent.** Running out of budget is line 4.

## The premise-removal gate

**The round removes a cited premise only if the formalized statement is the one
`TurnpikeScopeTransfer.lean` consumes.** Three conditions, all required, checked in the result note
one by one:

1. **Identity.** The statement proved is `OIBridge.ScopeTransfer.BGIntegerClassification` itself —
   the `def` at `OIBridge/TurnpikeScopeTransfer.lean` line 542, referred to **by name** — and not a
   restatement, not a variant with different hypotheses, and not a statement proved equivalent to it
   by a separate argument.
2. **Discharge, not edit.** `spectral_classification_of_BG` and `twoBranch_of_BGClassification` are
   re-derived with `hBG` **discharged** from the round's theorem. **Their statements are not edited
   to remove the hypothesis**, and the round does not alter either theorem's existing text.
3. **Axiom cleanliness.** Every named result of the round, and the two re-derived consumers, print
   exactly `[propext, Classical.choice, Quot.sound]`.

**If any condition fails, the premise stands and the round says so.** In that case: the `P2` row
stays `EXTERNAL` with the label unchanged; the ledger entry
`GR:T-d-gauge-completeness-two-branch` keeps its grade; the probe's scope block at lines 20037–20043
is left as the base has it; and the result note states, in terms, that the premise stands and which
condition was not met.

**A partial pass is a fail.** Two of three conditions met is the premise standing, not the premise
half-removed.

## The preregistered predictions, with their signs, strengths and recorded reasons

| target | prediction (sign) | strength | recorded reason |
| --- | --- | --- | --- |
| `BG0` | **positive** — the search finds the six enumerated forms and confirms exactly one is the premise | **high** | A pre-freeze reading of the file set found forms 1–6 above and no seventh; the two consumers take the premise by name at lines 563 and 826 and nowhere else in the tree. The reading is the freeze's **reason**, not a finding: `BG0`'s finding is whatever the execution's own bounded search records. |
| `BG1` | **positive** — the record carries the citation, the scope caveat and a cost estimate, all quotable | **high** | The `PiccardBridge` provenance and caveat paragraphs, the `GR.md` citation sentence and the ledger `delta`/`note` fields are present at the base and were read at this freeze. |
| `BG2` | positive | **high** | Quantifier reordering over a `def`; the bridge is `Iff.rfl` or one `constructor`. |
| `BG3` (a) | positive | **high** | `golomb_r1` and `golomb_r2` are merged and supply two of the five hypotheses outright; the ordering and image-equality conjuncts are finite checks over `Fin 6` with `ℤ` values; the two nontriviality conjuncts each reduce to evaluating the candidate constant at one index and contradicting it at a second. |
| `BG3` (b) | positive | **high** | The merged `mu_gap` gives the fifteen identities with `eS = eT = Equiv.refl _`. |
| `BG4` (a) | positive | **high** | At `n ≤ 1` the translate witness is `F' 0 - F 0` or is vacuous; at `n = 2` the single difference on each side forces it. |
| `BG4` (b) | positive | **medium** | Three separate finite arguments over unbounded integers, each of the form "the largest difference matches, then the next, then the case split closes". The route is standard and the freeze can see it; what the freeze cannot price is how much Mathlib support the `Finset.image` equality needs before the case split starts. **Reporting `BG4` (b) UNDECIDED with the obstruction named is an allowed outcome**, and it does not move `BG4` (a). |
| `BG5` | **UNDECIDED** — the classification is not formalized within this round's budget | **medium** | The budget is set at the floor of the record's own estimate for the full job, and that estimate describes a **reconstruction** rather than a transcription: factorization completeness over Laurent rings, a finite two-negative-term case analysis, and a well-founded form of an infinite-regress counting argument. Any one of the three is a research step this round's budget funds at most partly. The freeze names no route that fits inside 1200 lines. |
| `BG5` → line 1, `BG5-full` | not predicted | **low** | The full statement is the whole of the 2007 classification. The freeze does not rate reaching it inside the budget better than low, and rates it at or below every fallback line for the reason the hierarchy is ordered: line 1 implies the content of lines 2 and 3, so a freeze rating it above them would be incoherent. |
| `BG5` → line 2, `BG5-normal-form` | not predicted | **low** | The polynomial model is the shape `piccard_factor_r` and `piccard_factor_s` already work in, so the model itself is cheap; the implication from a polynomial-model `Prop` back to the quoted `Prop` is the expensive half, since it must handle every mark count and every ruler rather than the cited family. |
| `BG5` → line 3, `BG5-restricted` | not predicted | **low** | F3a's hypothesis is stated from the ledger's recorded description of the argument's case split, which is a paraphrase and not the paper; the execution must write the hypothesis out exactly and record a discrepancy if the recorded description does not support a precise statement. F3b is one mark count and is rated low because seven marks is where the argument's counting content begins rather than a case the small-mark route reaches. |

**No target has a numerical fallback**, and none is offered for a universal statement. **UNDECIDED
remains a permitted label for every target**, reported with the obstruction named.

**The four `BG5` rows are the freeze's whole position on the main target.** No sentence of this file
predicts the classification's formalization at medium or high, on any line of the hierarchy.

## The status rule: the outcomes per target, each with its FROZEN post-round sentence

The execution reports each target with exactly the sentence frozen here for the outcome reached. The
wording is fixed before the round runs so that no outcome can choose its own wording.

### `BG0` outcomes

- **Outcome `BG0`-enumerated** — the search confirms the enumeration:
  > On the search this freeze bounds, the tree states the Bekir–Golomb classification in the forms
  > recorded above, and exactly one of them — the `Prop` `BGIntegerClassification` at
  > `OIBridge/TurnpikeScopeTransfer.lean` line 542 — is consumed as a cited premise, at the two
  > coordinates recorded. Every other located form is a consequence of it, a witness for its
  > exceptional clause, a scope variant, or citation prose, and each is recorded as such with its
  > coordinate. **This is a statement about the tree at the base and about nothing else.**
- **Outcome `BG0`-further-form** — the search locates a form this freeze does not enumerate:
  > The search locates a further form of the classification in the tree, quoted above with its
  > coordinate and classified as premise, consequence, witness, scope variant or prose. **This
  > freeze's enumeration is recorded as incomplete against this round's own search and is not
  > repaired**: a preregistration is a statement about what was frozen, and the execution records the
  > discrepancy. Whether the further form changes the round's target is settled by the
  > premise-removal gate's identity condition and by nothing else.
- **Outcome `BG0`-UNDECIDED:**
  > The bounded search was not completed, and every later target that depends on knowing which `Prop`
  > is the premise is reported UNDECIDED with this recorded as the obstruction.

### `BG1` outcomes

- **Outcome `BG1`-recorded:**
  > The record's citation of the 2007 classification, its standing scope caveat about the cited
  > text's ambient domain, and its own estimate of what a kernel reconstruction would cost are
  > quoted above with their coordinates. **These are the record's statements, attributed to the
  > record.** This round performed no re-audit of the primary text, no literature search and no
  > external reading, and asserts nothing about the paper beyond what the pinned blobs say.
- **Outcome `BG1`-partial:**
  > The passages located are quoted with their coordinates and the passages sought and not found are
  > recorded as absent on the named and bounded search. **Where the record is silent the finding is
  > that it is silent**, and no description of the cited argument is reconstructed from what the
  > record does carry.

### `BG2` outcomes

- **Outcome `BG2`-positive:**
  > The premise is equivalent, definitionally, to its mark-count slice quantified over all mark
  > counts, at evidence level 2, with `BGIntegerClassification` consumed by name. **Every later
  > target of this round is stated over that slice and is therefore stated over the premise
  > `TurnpikeScopeTransfer.lean` consumes.** The bridge is a restatement of quantifier order and
  > establishes no case of the classification.
- **Outcome `BG2`-UNDECIDED:**
  > The bridge was not reached in the kernel, and every later Lean target of this round is reported
  > UNDECIDED with this recorded as the obstruction, because without it those targets would be
  > statements about a `Prop` this round wrote rather than about the premise the tree consumes.

### `BG3` outcomes

- **Outcome `BG3`-both:**
  > The printed six-mark pair satisfies every hypothesis of the premise's six-mark slice and
  > satisfies its conclusion, both at evidence level 2. **The premise as stated is therefore not
  > vacuous and its conclusion is attained**, so a weakening of either that made the target easier
  > would contradict a theorem of this round. **This is a statement about one exhibited pair**: it is
  > not the six-mark case of the classification, which is universal over pairs, and it is not a step
  > toward it. `golomb_r1`, `golomb_r2` and `mu_gap` are consumed as `HomometricSix.lean` states
  > them and are not extended.
- **Outcome `BG3`-(a)-only:**
  > The printed pair satisfies every hypothesis of the six-mark slice, at evidence level 2. Whether
  > it satisfies the conclusion is undecided in this round, with the obstruction named, and the
  > hypothesis conjunct does not cover it.
- **Outcome `BG3`-(b)-only:**
  > The printed pair satisfies the conclusion of the six-mark slice, at evidence level 2. Whether it
  > satisfies every hypothesis is undecided in this round, with the obstruction named; in particular
  > the non-vacuity control is **not** established, and no sentence of this round may say the
  > premise's hypotheses are satisfiable.
- **Outcome `BG3`-UNDECIDED:**
  > Neither conjunct was reached, with the obstruction named, and the non-vacuity control is not
  > established.

### `BG4` outcomes

- **Outcome `BG4`-both:**
  > The premise's mark-count slice holds at every mark count at most five, at evidence level 2, by a
  > kernel argument with no kernel-bypassing decision procedure. **This settles mark counts at most
  > five and nothing above five**, and is not evidence about six marks or about seven and above in
  > either direction. The narrowing report frozen for this target is issued.
- **Outcome `BG4`-(a)-only:**
  > The slice holds at every mark count at most two, at evidence level 2. Whether it holds at three,
  > four or five is undecided in this round, with the obstruction named, and the narrowing report is
  > **not** issued, because the residual it would cite is not established.
- **Outcome `BG4`-UNDECIDED:**
  > No mark count was settled, with the obstruction named, and the narrowing report is not issued.

### `BG5` outcomes — the main target, with a frozen sentence for each of the four lines

- **Outcome line 1, `BG5-full`:**
  > `BGIntegerClassification`, the `Prop` at `OIBridge/TurnpikeScopeTransfer.lean` line 542, is
  > proved in the kernel at evidence level 2, printing exactly
  > `[propext, Classical.choice, Quot.sound]`. The premise-removal gate is passed in all three
  > conditions: the statement proved is that `Prop` by name; `spectral_classification_of_BG` and
  > `twoBranch_of_BGClassification` are re-derived with `hBG` discharged rather than by editing
  > their statements; and every named result is axiom-clean. **The cited premise is thereby
  > removed.** What this establishes is the integer classification and the results that consume it;
  > it establishes nothing about any other queue row, and the reconstruction theorem's remaining
  > hypotheses — distinct gaps and non-vanishing overlaps — stand exactly as the manuscript states
  > them.
- **Outcome line 2, `BG5-normal-form`:**
  > `BGIntegerClassification` is kernel-derived at evidence level 2 from a polynomial-model `Prop`
  > written out in full in this note, in the 0/1-polynomial shape the cited argument uses. **The
  > premise stands**: what the repository assumes is now that polynomial-model `Prop` rather than the
  > classification in ruler form, and the `P2` row stays `EXTERNAL` with its label unchanged, the
  > ledger entry keeping its grade. **This is a change in the shape of what is assumed and not in
  > whether something is assumed**, and no sentence of this round may report it as a removal of the
  > premise. The premise-removal gate is not passed and the note says which condition is not met.
- **Outcome line 3, `BG5-restricted`:**
  > The restriction reached — F3a, the nonsingular branch stated as an explicit hypothesis on the
  > ruler pair, or F3b, the single mark count seven — is proved in the kernel at evidence level 2,
  > and the note names which. **The premise stands**, the `P2` row stays `EXTERNAL` with its label
  > unchanged, and the ledger entry keeps its grade. **The restricted statement is a result about
  > its own restriction and about nothing else**: it is not evidence about the unrestricted
  > classification, it does not bound it, and no sentence of this round may report it as partial
  > progress toward a number, a fraction or a proportion of the classification. The premise-removal
  > gate is not passed and the note says which condition is not met.
- **Outcome line 4, `BG5`-UNDECIDED — its post-round sentence frozen in full:**
  > **The Bekir–Golomb integer classification is not formalized within this round's budget, and that
  > is the whole of the finding.** None of the three settling lines was reached and **none is
  > claimed**: the quoted `Prop` is not proved, no polynomial-model reduction to it is proved, and
  > neither frozen restriction is proved. The point at which the budget was reached is named above.
  > **The premise stands**, the `P2` row stays `EXTERNAL` with its label unchanged, the ledger entry
  > keeps its grade, and the probe's scope block is left as the base has it. **What this round adds
  > is the target pinned and the ground around it prepared, not the target reached**: the premise's
  > exact text is recorded with its coordinate and every other form the tree states the
  > classification in is enumerated and classified; the premise is kernel-bridged to its mark-count
  > slice, so a later round's statements are anchored to the `Prop` actually consumed; the printed
  > six-mark pair is proved to satisfy every hypothesis and the conclusion, so the statement cannot
  > be weakened into vacuity unnoticed; and the small-mark case is settled where it was settled.
  > **UNDECIDED here is a statement about this round's budget and about nothing else.** It is
  > **not** a finding that the classification is false, **not** a finding that formalizing it is
  > infeasible, **not** a finding that it is hard beyond the estimate the record already carries,
  > **not** a bound on what a later round with a different budget can do, and **not** a finding
  > against any merged result of the reconstruction programme — every result in the kernel-proved
  > table above stands exactly as its own file states it.

## The frozen post-round sentence for the `P2` row, per case

**Case A — `BG0` enumerated, `BG1` recorded, `BG2`, `BG3` (a) and (b), `BG4` (a) and (b) land, and
`BG5` is UNDECIDED.** This is the case the freeze predicts. The row stays **EXTERNAL** and its label
does not change. The sentence appended:

> The premise `BGIntegerClassification` stands as a cited external theorem and is not formalized.
> Round BG-1 pinned the target and prepared the ground around it: the premise's exact text is
> recorded with its coordinate, every form in which the tree states the classification is enumerated
> and classified, the premise is kernel-bridged to its mark-count slice so that later statements are
> anchored to the `Prop` the tree consumes, the printed six-mark pair is kernel-proved to satisfy
> every hypothesis of that slice and its conclusion, and the slice is kernel-proved at every mark
> count at most five — so what stands as assumed is the classification at six marks and above, with
> the full premise kernel-derived from it. The classification itself was not formalized within the
> round's budget, which is a statement about the round's budget and not about the classification:
> the row's `EXTERNAL` label, the ledger entry's grade and the probe's scope block are unchanged.

**Case B — as A, but `BG5` reaches line 1, `BG5-full`.** The row's label changes to **DERIVED** and
the sentence appended is:

> `BGIntegerClassification` is kernel-proved and the cited premise is removed: the two consumers in
> `TurnpikeScopeTransfer.lean` are re-derived with the hypothesis discharged by name, and every
> named result prints exactly `[propext, Classical.choice, Quot.sound]`. The reconstruction
> theorem's remaining hypotheses — distinct gaps and non-vanishing overlaps — stand exactly as the
> manuscript states them, and this row's closure establishes nothing about any other queue row.

**Case C — as A, but `BG5` reaches line 2, `BG5-normal-form`.** The row stays **EXTERNAL**, and Case
A's first sentence is replaced by:

> The premise stands, restated: what the repository assumes is a polynomial-model `Prop` in the
> shape the cited argument uses, from which `BGIntegerClassification` is kernel-derived. This is a
> change in the shape of what is assumed and not in whether something is assumed.

Every other clause of Case A stands, with its final clause's phrase "was not formalized within the
round's budget" reading "was not formalized in ruler form within the round's budget".

**Case D — as A, but `BG5` reaches line 3, `BG5-restricted`.** The row stays **EXTERNAL**, and Case
A's final sentence is replaced by:

> The classification was kernel-proved under one frozen restriction, named in the round's result
> note, and under no other; that is a result about its own restriction and is not evidence about the
> unrestricted classification and does not bound it. The row's `EXTERNAL` label, the ledger entry's
> grade and the probe's scope block are unchanged.

**Case E — `BG2` UNDECIDED.** Every clause of Case A stated over the mark-count slice is omitted, the
targets that land are reported at their own strengths, and `BG4`'s narrowing report and `BG5` are
UNDECIDED.

**No case other than B changes the `P2` row's label**, and no case reports the reconstruction
programme's other obligations moved.

## What no outcome licenses

These are the forbidden sentences, in terms. None of them may be written in any artifact of this
round, in any paraphrase, in a summary line, an abstract, a table cell or a propagation line.

1. **"The classification is unformalizable", or "the classification is out of reach."** An UNDECIDED
   here is the recorded fact that the statement was not formalized within this round's budget. It is
   not a finding about feasibility, not a finding about difficulty beyond the estimate the record
   already carries, and not a bound on a later round.
2. **"The premise is removed", asserted on anything short of the premise-removal gate passed in all
   three conditions.** Lines 2 and 3 of the hierarchy leave the premise standing, and every artifact
   of this round says so where it reports them.
3. **"The formalized statement is the premise", asserted of a statement that is not the `Prop` at
   `OIBridge/TurnpikeScopeTransfer.lean` line 542.** Equivalence proved by a separate argument is not
   identity, and the gate's identity condition is not met by it.
4. **Any sentence that weakens the target's hypotheses and reports the weakened statement under the
   target's name.** Dropping the Golomb hypothesis on either side, dropping either nontriviality
   hypothesis, replacing difference-set equality by multiset equality, or bounding the mark count
   without saying so, each produce a different statement. **A different statement is reported under
   its own name, with the difference from the quoted `Prop` written out.**
5. **"The small-mark case is progress toward the classification."** `BG4` settles mark counts at most
   five. It is not evidence about six marks or about seven and above, and no fraction, proportion or
   percentage of the classification is claimed by it or by anything else in this round.
6. **"The printed pair shows the six-mark case."** `BG3` is about one exhibited pair. The six-mark
   case of the classification is universal over pairs and is not established by exhibiting one.
7. **"The record's cost estimate is this round's finding."** The estimate is the ledger's, quoted
   with its coordinate and attributed to it. This round neither confirms nor revises it.
8. **Any sentence about the primary 2007 text that is not a quotation from a pinned blob.** This lane
   is blind, this round performs no re-audit, and no sentence of this round reports what the paper
   says on this round's own authority.
9. **"The scope caveat is reopened", or any sentence treating the integer-versus-real question as
   live.** `integer_realization_of_real_realization` is merged and closes it mathematically; this
   round consumes that and adds nothing to it.
10. **Any sentence carrying an outcome of this round to another queue row.** `P0`, the substratum
    Lemma 24.1 rows, `A6`, physical `C4`, `H-Bell`, `H-link`, `H-state`/`H-frame`/`H-slope`, the
    covariant matter→boundary coupling and the Level-III row are untouched in every outcome, and a
    shared word is not a bridge.
11. **"The two-branch theorem is unconditional", in any outcome other than line 1 with the gate
    passed.** The manuscript's own hypotheses stand in every outcome, and in every outcome other than
    line 1 the cited premise stands too.
12. **Any sentence that reports a sibling lane's result.** The anti-contamination invariant governs.

## Named hazards

1. **Drift between the formalized statement and the premise actually consumed.** **This is the
   strongest hazard in the round.** The tree states the classification in six forms and only one of
   them is the premise; two of the others are real-scope or coefficient-scope statements that read
   like it and are consequences of it. The specific failure guarded against is a round that proves
   form 2, form 3 or form 5 — or a hand-written restatement of form 1 that differs in a hypothesis —
   and reports it as the classification, leaving the two `hBG` hypotheses undischarged while the
   record says the premise is gone. **`BG0` enumerates the forms, `BG2` bridges the premise by name
   to everything later, and the premise-removal gate's identity condition is the check.** A round
   that cannot discharge `hBG` by name has not removed the premise, whatever it proved.
2. **Silently weakening the statement to make it provable.** **This is the second strongest hazard,
   and it is what makes a formalization round with a known target different from a research round.**
   The target's hypotheses are seven and its conclusion is one; weakening any hypothesis, or
   strengthening any, produces a statement that may be far easier and is not the premise. The
   specific failures guarded against are: adding a bound on the mark count without saying so;
   adding a bound on the marks; replacing `Finset.image` equality by a multiset or a list equality;
   dropping either nontriviality hypothesis, each of which alone makes the conclusion false at six
   marks; and stating the conclusion with the equivalences replaced by functions, which loses the
   forcing of `n = 6`. **`BG3` is the standing control**: it proves the hypotheses are jointly
   satisfiable and the conclusion attained on an exhibited pair, so a weakening into vacuity
   contradicts a theorem of this round rather than passing unnoticed.
3. **Proving a statement whose hypotheses are contradictory and reporting it as the classification.**
   The premise is a universally quantified implication; making its antecedent unsatisfiable makes it
   trivially true. The specific failure guarded against is a definition of the mark-count slice whose
   hypotheses cannot be met at six marks, which would make `BG4` easy and `BG3` (a) unprovable.
   **The two targets are stated together for that reason**, and an execution that lands `BG4` while
   `BG3` (a) is UNDECIDED reports the combination as the obstruction it is.
4. **Supplying a step from background knowledge the record does not contain.** The specific failure
   guarded against is a step of the form "the classical result gives this" or "this is standard for
   Golomb rulers" — plausible-sounding, absent from the record, and licensed by nothing in it. Every
   step of every proof in this round is discharged from a merged result cited by name or from an
   argument written out in the kernel. Nothing is discharged from what "is well known", and nothing
   is discharged from the cited paper, which is the premise this round exists to replace.
5. **Treating the record's paraphrase of the cited argument as the argument.** The ledger's `note`
   describes the 2007 construction in a sentence and flags acknowledged informal steps in it. The
   specific failure guarded against is an execution that formalizes the ledger's sentence and reports
   the paper's theorem. F3a's frozen restriction is where this bites hardest, and its own wording
   requires the execution to write the hypothesis out exactly and to record a discrepancy if the
   record's description does not support a precise statement.
6. **Reporting a fallback the freeze does not name.** A fallback invented mid-execution is chosen
   with its result in view, which is what a freeze exists to prevent. Lines 2 and 3 name the only
   fallbacks this round may report, F3a and F3b the only restrictions, and any other requires an
   append-only amendment frozen and merged before the work it affects.
7. **Spending past the budget and reporting the result as within it.** The budget is 1200 source
   lines and 24 named results in one module, set at the floor of the record's own estimate. The
   specific failure guarded against is an execution that reaches the limit, keeps going, and reports
   a settling line; the correct behaviour is to stop and report UNDECIDED on what is unfinished.
8. **Reporting UNDECIDED as a finding about the classification rather than about this round.** The
   specific failure guarded against is the sentence "the classification is out of reach", and every
   paraphrase of it, including "no progress is possible" and "this is beyond formalization".
9. **Reporting `BG4` as a fraction of the job.** Mark counts at most five are where the cited text
   itself records the case as easily shown; settling them settles them and measures nothing. The
   specific failure guarded against is a percentage, a proportion, or "most of the cases".
10. **Reporting the narrowing as a removal.** The narrowing report says what stands as assumed is
    smaller. The specific failure guarded against is a summary line reading "the premise is reduced
    away" or "the assumption is nearly gone".
11. **Editing a merged theorem's statement to make a hypothesis disappear.** The premise-removal
    gate's second condition forbids it. The specific failure guarded against is deleting `hBG` from
    `spectral_classification_of_BG` or `twoBranch_of_BGClassification` and reporting the premise
    removed, which changes what those theorems say rather than what they need.
12. **Re-proving the surrounding kernel.** The integer-to-real passage, the six-mark kill chain, the
    Fourier layer and the congruent-case assembly are merged and axiom-clean. The specific failure
    guarded against is a module that restates one of them and reports it as this round's result.
13. **Using a kernel-bypassing decision procedure.** `native_decide` is forbidden outright, and
    `decide` may be used only where the domain is genuinely finite — over `Fin 6`, over `AscPair 6`,
    over `ZMod` — never over an unbounded integer range. The specific failure guarded against is a
    `decide` that appears to settle a case at seven marks by silently instantiating a bounded model.
14. **Consuming a sibling round's result because it is present at the mandated base.** The
    anti-contamination invariant governs; the specific failure guarded against is an execution that
    reads a lane that merged between this freeze and its base.
15. **A landing without `P`.** This is a sealing round. The specific failure guarded against is
    treating `L` as the end of it: in execution mode the ancestry check enumerates
    `git rev-list HEAD ^_BGC_BASE`, which at `L` reaches sibling rounds that do not descend from the
    base, and fails closed. `P` is what moves the clause to archive mode.
16. **A chronology guard that certifies only the head, or that certifies `HEAD` on `main` after the
    merge.** See the chronology control's clauses 5 and 7.
17. **Editing this freeze after an outcome is known.** The preregistration is immutable once merged.
    An execution that diverges **records the discrepancy** and does not repair the freeze.

## Non-doings

The round does not: re-audit the primary 2007 text, or read anything outside the pinned blobs; assert
anything about that text on its own authority; reopen the integer-versus-real scope question, which
`integer_realization_of_real_realization` closes; re-prove any merged result of the reconstruction
programme; edit `spectral_classification_of_BG`, `twoBranch_of_BGClassification`,
`twoBranch_of_spectral_classification` or `twoBranch_of_PiccardClassification`; redefine `r1`, `r2`,
`mu`, `muInv`, `piccardX`, `piccardY`, `alignT`, `alignEquiv` or `AscPair`; edit any manuscript;
alter any existing archive seal constant; change the `P2` row's label except in Case B; change the
ledger entry's grade except in Case B; touch any other queue row; consume or compare anything from
the Track B, substratum, physical-realization or hydrodynamics programmes; or report a fallback this
file does not name.

## Evidence levels

**Evidence level 2** — kernel-checked, every named result printing only
`[propext, Classical.choice, Quot.sound]`, with **no unproved declaration, no added axiom and no
kernel-bypassing decision procedure** — for `BG2`, `BG3`, `BG4`, the narrowing report, and, if any of
lines 1, 2 or 3 of its hierarchy is reached, `BG5`.

**`BG0` and `BG1` are type P and carry no evidence level.** Each is settled by the frozen evidence
rule — verbatim quotation with a coordinate, or the recorded statement that the passage sought does
not exist on the named and bounded search — and by nothing else. **Reconstructive inference is
forbidden as a finding**, and where the record is silent the finding is that it is silent.

## The axiom discipline

**No `sorry`. No `axiom`. No `native_decide`.** No unproved declaration of any kind, and no
declaration whose proof is deferred to a later round.

**Every named result of the round's module carries a `#print axioms` line**, printing **exactly**
`[propext, Classical.choice, Quot.sound]` and nothing else. The result note carries the axiom table
with one line per named result, and the module's `#print axioms` block carries one line per named
result with no omissions — the module's result count and its `#print axioms` count are equal, and the
result note states both numbers.

**`BGIntegerClassification` is a `def … : Prop` and not an `axiom`**, and this round does not change
that. Its status as an unproved *input* is carried by its appearing as a hypothesis, which is why
`#print axioms twoBranch_of_BGClassification` is already clean at the base while the theorem is
conditional. **A clean axiom print is therefore not evidence that the premise is discharged**, and no
artifact of this round may present one as such.

**The premise-removal rule, stated with the axiom discipline it depends on.** The round removes a
cited premise **only if** the formalized statement is the one `TurnpikeScopeTransfer.lean` consumes —
the `Prop` at line 542, discharged by name into `spectral_classification_of_BG` and
`twoBranch_of_BGClassification`, with every named result axiom-clean. **Otherwise the premise stands
and the round says so**, in the result note, in the `P2` row's appended sentence, and in the ledger
entry, each in the frozen wording above.

## The chronology control

The execution's guard tag is **`R7-BGC`**, reserved here and created by the execution pull request.
The seal constants this round owns and fills are **`_BGC_SEALED_HEAD`** and **`_BGC_MERGE`**, with
the base held in **`_BGC_BASE`**.

1. **This preregistration blob is merged into `main` before any execution-specific BG-1 object enters
   the repository tree** — any Lean definition or proof about integer rulers, difference sets, the
   mark-count slice or the classification; any search artifact; any probe clause; any result
   artifact. **The single permitted exception is the analysis recorded inside this control-plane blob
   itself**, merged *as* the freeze, including the frozen evidence rule, the quoted statements, the
   cost estimate quoted from the ledger and the pre-freeze reading recorded as the reason for `BG0`'s
   prediction.
2. **The execution pull request's base must be exactly the merge commit of this control-plane pull
   request**, and `_BGC_BASE` is set to that commit.
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from the
   Actions event payload, **never** the synthetic merge commit. An unresolvable head **fails
   closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B = _BGC_BASE` and `H` the real execution
   head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B` itself a descendant of `B`**,
   fail-closed.
6. **The guard recovers whatever history it needs itself** and **fails** if recovery fails — for `B`,
   for `H`, and for every enumerated commit alike.
7. **Archive mode.** `_BGC_SEALED_HEAD` and `_BGC_MERGE` are present and **unset** at execution.
   After `L`, the mandatory pin commit `P` sets them to `E` and to `L`, and the guard re-runs the
   same strong check against the sealed object: the pinned merge's second parent must equal the
   sealed head; the sealed head must pass clause 5 against `B` exactly as in its own run; and both
   must be reachable from the current target — the real `pull_request.head.sha` in pull-request
   continuous integration, `HEAD` otherwise — each **fail-closed**. `P` is a pin-only change
   recording the two SHAs and nothing else.

### Preconditions checkable mechanically at the execution's base

An auditor checks each of the following at the execution's base commit `B`, with the commands given.

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 1 | This control plane is merged, and `B` is its merge commit | `git rev-list --parents -n 1 B` shows two parents; `git cat-file -p B:verification/programmes/reconstruction/round-bg-1-integer-classification/preregistration.md \| git hash-object --stdin` equals the blob the `R7-BGC` clause pins |
| 2 | The premise and its two consumers are in the tree | `git show B:verification/lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean` contains `def BGIntegerClassification : Prop :=`, `theorem spectral_classification_of_BG (hBG : BGIntegerClassification)` and `theorem twoBranch_of_BGClassification (hBG : BGIntegerClassification)` |
| 3 | The merged results the round consumes are in the tree | `git cat-file -e B:verification/lean-mathlib/OIBridge/HomometricSix.lean`, `…/HomometricKill.lean`, `…/PiccardBridge.lean`, `…/CongruentReconstruction.lean` and `…/FrequencyMatching.lean` all succeed |
| 4 | The `P2` row is still `EXTERNAL` | `git show B:verification/ROADMAP.md` contains `| **P2** | Bekir–Golomb integer classification | Reconstruction | **EXTERNAL** |` as a prefix of the row |
| 5 | No BG-1 execution object precedes the freeze | `git ls-tree -r B --name-only` contains no path under `verification/programmes/reconstruction/round-bg-1-integer-classification/` other than `preregistration.md`, and no `verification/lean-mathlib/OIBridge/TurnpikeClassification.lean` |
| 6 | The tag is unused | `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-BGC`, `_BGC_BASE`, `_BGC_SEALED_HEAD` or `_BGC_MERGE` |

**No sibling lane's merge is a precondition of this round**, and the execution does not wait for one.
Sibling results present at `B` are **not** inputs: the anti-contamination invariant governs, and the
round consumes only what this freeze's start-state table names.

**The claim is scoped to the repository record.**

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This pull request carries this file alone.**
- **Then exactly one execution pull request**, based on the merge commit of this one, carrying the
  Lean module, the result note, the `R7-BGC` guard clause with `_BGC_SEALED_HEAD` and `_BGC_MERGE`
  present and unset, the `OIBridge.lean` import line, the `ROADMAP` propagation and the ledger
  `checks` entry. **No manuscript changes.**
- `python3 verification/lean/edge_rigidity_probe.py` prints `ALL CHECKS PASS` on the execution head,
  and the full release gate is green.
- **Before certification the execution never absorbs later `main`**: no merge from `main`, no rebase,
  no amend, no force-push. A red badge caused solely by an archive clause that entered `main` after
  the base is not a research failure; the certification of record is the run whose `head_sha` is `E`.
- Exact-head review after execution is complete, with full continuous integration green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **The landing is `E` → `L` → `P`, on the execution pull request, in that order**, with `P`
  mandatory. Landing conflicts are resolved **in `L`, never in `E`**, and by merits rather than by
  side. Full continuous integration must pass again on `P` before the pull request merges, and the
  resulting `main` build must be green before the next round's landing is constructed.

## Allowed final report

1. **The round's shape**, restated: sealing, `E` → `L` → `P`, with the seal constants it filled named
   and no existing seal constant altered;
2. **`BG0`** — the bounded search recorded in full, the premise quoted with its coordinate, and every
   other form of the classification enumerated and classified;
3. **`BG1`** — the record's citation, scope caveat and cost estimate, quoted with coordinates and
   attributed to the record, with no external reading;
4. **`BG2`** — the bridge, with its bounded reading;
5. **`BG3`** — the two conjuncts of the consistency control, each reported separately, with the
   exhibited-pair boundary stated;
6. **`BG4`** — the small-mark case, each conjunct reported separately, and the narrowing report if
   both land and line 1 is not reached;
7. **`BG5`** — the outcome as the highest line of the four-line hierarchy the kernel actually
   carries, in the status rule's frozen wording for the outcome reached, with the budget point named
   in the UNDECIDED case;
8. **the premise-removal gate** — each of its three conditions checked and reported, and the
   statement that the premise stands where it is not passed in full;
9. the frozen `P2` sentence for the case reached, verbatim, with the row's label unchanged except in
   Case B;
10. what no outcome licenses, in this file's wording, and the status rule as honoured;
11. the relation to the merged reconstruction programme — every consumed result named, none revised,
    none re-proved;
12. the definition count against the three-slot budget, with each conditional slot marked fired or
    unused, and the module's line count and named-result count against the frozen budget;
13. the chronology certification, naming the property certified, the preconditions checked at `B`,
    and the archive-mode pins as unset at execution;
14. the axiom table with one line per named result, and the equality of the module's result count and
    its `#print axioms` count;
15. the discrepancies, if any, recorded and not repaired.
