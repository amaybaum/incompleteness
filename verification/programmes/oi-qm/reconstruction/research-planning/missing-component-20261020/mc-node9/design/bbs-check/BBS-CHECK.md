# BBS-CHECK: the classical-memory falsifiability claim (Main.md:702)

_Publication note: one local scratch path was replaced by "this directory". `bbs_probe.py` needs sympy (1.14.0 was used). Read-only check against `main` `af8c59d6`; no manuscript was changed; corrections need owner authorization._

This was a read-only check of `amaybaum/incompleteness` at `af8c59d6` (main), using a detached worktree that has since been removed. Nothing was committed, pushed or commented.

Files in this directory:
- `bbs_probe.py`: exact sympy probe.
- `bbs_probe.out`: its output (53 checks, 0 failed, controls C1–C6 green).

## 0. Source status of the BBS definition: [Q]

I could not read arXiv:2310.01205 or PRL 132, 060402:
- `arxiv.org` failed DNS resolution.
- `export.arxiv.org`, `journals.aps.org` and `fis.tu-dresden.de` were refused by the proxy.
- Web search returned only metadata.

Everything below therefore rests on the owner's statement of Definition 1 [rec, owner report 2]: E₂(ρ) = Σᵢ Φᵢ(Mᵢ ρ Mᵢ†).

**Read literally, that definition is vacuous.** Every channel satisfies it with one outcome, M = I and Φ = E₂ (check `B literal form`). The non-vacuous reading adds the constraint **Σᵢ Mᵢ·Mᵢ† = E₁**: the instrument carries out the first step, and its outcome is the stored memory. I use that reading. It is my reconstruction, not a quotation of the paper. Every verdict below is conditional on it.

## 1. What OI's representation implies

The setup is §3.4 and l. 532: U_φ|x,h⟩ = |φ(x,h)⟩, with a diagonal hidden prior. Eₜ(ρ) = Tr_H[Uᵗ(ρ⊗μ_H)U^{-t}]. All results are exact.

| Case | E₁ | E₂ | BBS classical memory (constrained)? | Memory variable |
|---|---|---|---|---|
| A. CNOT (S→H), μ = I/2 or \|0⟩⟨0\|, no intermediate step | Δ (dephasing) | id | **yes**: I_a = ½Z^a·Z^a, Φ_a = E₂∘Ad Z^a | Z-kick label (hidden X-basis value), **not** the hidden configuration |
| A′. Same, with a Hadamard on S between the steps | Δ | Bloch (x,y,z) → (0,−y,0) | **yes**, same instrument | same |
| B. SWAP, initialized hidden slot μ = \|0⟩⟨0\| | ρ ↦ \|0⟩⟨0\| | id | **no** | n/a |
| B′. SWAP, μ = I/2 | ρ ↦ I/2 | id | **yes**: Pauli twirl | 2-bit label, more than the hidden register's 1 bit |
| C. The paper's ledger construction of the same law as B | ρ ↦ \|0⟩⟨0\| | Δ | **yes**: I_x = ⟨x\|·\|x⟩\|0⟩⟨0\|, Φ_x = prepare \|x⟩ | recorded x₀ |

**Why case B fails.** Suppose Σᵢ Iᵢ = E₁ = (ρ ↦ Tr ρ·|0⟩⟨0|).
- Each Choi matrix then satisfies 0 ≤ Cᵢ ≤ I⊗|0⟩⟨0|. So Cᵢ = Fᵢᵀ⊗|0⟩⟨0|, and Iᵢ(ρ) = Tr(Fᵢρ)|0⟩⟨0|.
- It follows that Σᵢ Φᵢ∘Iᵢ = Σᵢ Tr(Fᵢ·)Φᵢ(|0⟩⟨0|), which is entanglement-breaking.
- The identity channel is not entanglement-breaking: the partial transpose of its Choi matrix has spectrum {−1, 1, 1, 1} (control C2).

So no classical-memory decomposition exists. B is an OI realization in the manuscript's own terms:
- φ(x,h) = (h,x) is a bijection.
- The prior is diagonal.
- Main.md:60 names "the two-state swap under … point-mass hidden priors" as a legitimate realization datum.
- Main.md:502 uses initialized (point-mass) ledger and clock sectors in the process-dilation prior.

**Same visible law, opposite verdicts.** B and C produce the same configuration law, X₁ = 0, X₂ = X₀, which is non-Markovian (C4 readback). On coherent inputs:
- In C the ledger keeps x₀, so coherence is not restored and E₂ = Δ.
- In B the swap returns the hidden slot to |0⟩, so E₂ = id.

The BBS verdict is therefore not a function of the observable law. It depends on the coherent extension, which Main.md:455 states the equivalence does not fix.

**The root cause.** Diagonal preservation (l. 322) holds only for diagonal inputs. On a coherent input, U_φ moves visible coherence into the hidden register:
- In case B the hidden marginal becomes |+⟩⟨+|.
- In case A with μ = |0⟩⟨0|, the system–hidden state is a Bell state (partial-transpose eigenvalue −½).

From then on the "classical hidden register" is no longer a classical variable. Even where a BBS decomposition does exist (A, B′), conditioning on the hidden configuration does not reproduce E₂: the instrument "read h" factors through Δ.

**Configuration inputs (OI's native interface).** For any channels E₁ and E₂, restricted to inputs diagonal in a fixed basis, take Iₓ(ρ) = ⟨x|ρ|x⟩E₁(|x⟩⟨x|) and Φₓ(σ) = Tr σ·E₂(|x⟩⟨x|). This decomposition always works (check D, which holds even for case B and for the generic quantum pair {Ad H, id}).

On native inputs, then, the claim holds for every process, quantum or not, and no outcome could falsify it.

**Uniform prior (the §3.2 / Lemma 3 scope).**
- E₁ is unital.
- For a qubit, unital channels are mixed-unitary (Landau–Streater; this is [ext], cited from memory). So every E₂ admits the decomposition.
- I have not determined whether this holds for visible dimension 3 or more under a uniform prior.

## 2. Coherent inputs and the bridge

BBS classical versus quantum memory is a property of the maps on all density matrices. Testing it requires coherent preparations or non-commuting tomography, and on configuration inputs it is empty (section 1). The claim at l. 702 is therefore conditional on the coherent-preparation and instrument bridge.

The manuscript says that bridge is open:
- l. 22: "two logically separate completion questions".
- l. 411, l. 534, l. 542, l. 562.
- l. 455: the coherent extension is not fixed by the equivalence.

**l. 702 states neither condition.** It does not mention the bridge, and it does not mention the rule separating "fundamental" processes from "engineered" ones. The project's own record lists that rule as missing: `verification/programmes/physical-realization/hidden-sector-route-selection/result.md:29` says "the eligibility rule must precede observing the witness". That file is a governed record; no edit is proposed.

**Even with the bridge in place, the inference fails.** The gluing and uniform-continuum theorems (l. 544, l. 576; abstract l. 22) give a finite reversible classical realization reproducing any finite quantum experiment to accuracy ε. That includes a physically realized swap-back process with a pure ancilla, whose BBS witness value is preserved to O(ε). A classical substratum therefore does not entail BBS-classical observed dynamics. The word "therefore" at l. 702 has no supporting derivation.

## 3. Conclusion: (iii), it does not follow

The counterexample is in OI's own representation: case B, the manuscript's swap with a point-mass prior (l. 60).

The only part of the claim that holds unconditionally is the configuration-input statement. It holds for every process and constrains nothing, so narrowing to (ii) yields no test.

### Sites needing correction (§A.25)

**BBS-sense claim:**
- `papers/Main.md:702`: the claim, plus its last sentence ("where the classical-memory simulability commitment is most stringently tested").
- `papers/Main.md:704`: "The classical-memory test above is therefore the primary falsifiability route."
- `papers/GR.md:601`: the mirror ("The framework predicts that all fundamental non-Markovian dynamics … should be classical-memory simulable, because the hidden sublattice is by construction a classical substrate … would falsify"). Its gloss "dividing line set by entanglement structure of the channel's Choi state" is a description of BBS I could not verify ([Q]).

**Adjacent claim, a different (dilation) sense, flagged for consistency review:**
- `papers/Substratum.md:476`
- `book/ch04-methodology.md:144`
- `book/The-Incompleteness-of-Observation-FULL.md:1261` (identical to ch04:144)

These state Class C "classical-memory simulability" and say a "provably supra-classical" process falsifies "at the characterization-theorem level". Two problems:
- This conflicts with Main.md:704, which says no experiment falsifies the theorem.
- In the finite-classical-realization sense, the gluing theorem gives every finite experiment a deterministic ε-shadow, so no finite-accuracy experiment can be supra-classical.

They also share the label with the BBS claim.

**Checked and needing no edit:** the Main abstract, the conclusion, the status-ledger rows (l. 714–718), `book/appendix-a-prediction-status.md` and ch19. None contains the claim. `[28]` appears only at Main.md:702 and in the reference list at 830; in GR it is `[27]`.

### Proposed replacement wording (owner authorization required)

**Main.md:702**, replacing from "Every fundamental non-Markovian…" to the end of the paragraph:

> On configuration inputs the ontology places no constraint on the classical/quantum memory distinction of Bäcker, Beyer, and Strunz [28]: restricted to inputs diagonal in a fixed basis, every two-step process admits a classical-memory decomposition. On coherent inputs the permutation unitary of §3.4 carries visible coherence into the hidden register, and the classification depends on the realization, not on the visible law: the law $X_1 = 0$, $X_2 = X_0$ has a ledger realization with classical memory and a swap realization, $\varphi(x,h) = (h,x)$ with an initialized hidden slot, whose two-step maps $\rho \mapsto |0\rangle\langle 0|$, $\rho \mapsto \rho$ admit no classical-memory decomposition. By the gluing and uniform-continuum theorems of §3.4, a finite reversible realization reproduces the statistics of any finite quantum-memory experiment to any stated accuracy. A memory-witness test of the ontology therefore requires the coherent-preparation and instrument bridge of §3.4 together with an outcome-independent rule identifying fundamental open-system processes; neither is supplied here, and the memory witnesses of [28, 29, 30] do not test the ontology without them.

**Main.md:704**, replacing the last sentence:

> What is empirically falsifiable is the framework's physical identification of nature with its deterministic finite ontology; the memory witnesses above bear on it only under the two conditions just stated.

**GR.md:601**: the same substance in GR's register. Delete "The framework predicts … should be classical-memory simulable … would falsify the framework's foundational ontology even without cosmological data. This is a near-term tractable test …", and state that the classification depends on the coherent extension and needs the same two inputs ([Main §4.5]).

**Substratum.md:476, ch04:144 and FULL:1261** (mirror pair, §A.14): state the dilation-sense content as proved, namely that every finite adaptive experiment has a finite deterministic ε-realization while the exact continuum theory at fixed carrier is excluded. Remove the clause "falsifies … at the characterization-theorem level", or tie it to an exact-continuum test. The wording is the owner's call.

## 4. Scope

- No manuscript change was made.
- The conclusions are exact for the cases computed and conditional on the owner's statement of BBS Definition 1 (with the E₁ constraint).
- I make no claim about BBS's own witness inequality, about any uniform-prior case with visible dimension 3 or more, or about which physical processes count as fundamental.
- The verdict lines in `bbs_probe.out` print only after all six controls are green.
- C6 only confirms that the rule fires. The quantum-memory verdict for case B rests on the analytic Choi-support argument plus the exact partial-transpose eigenvalue −1.
- Correctness bands are unchanged; this is a consistency finding.
