# Gate 1 (scientific accuracy): PR #918 r20 at `10c629ea`

**Verdict: ACCEPT WITH CHANGES.** One change is required: the abstract's Theorem 4 sentence (F1). All three r19 findings and all four gate-2 explanation changes are correct against their sources. Every exact statement is unchanged, and no ledger ID is retired.

The review was read-only, against r19 `2afb5b6a`. I used a detached worktree at `10c629ea`, which is now removed. Line numbers are at `10c629ea`.

## 1. The three required r19 findings: all fixed
- **§3.4 quantifier (L238).** It now reads "for any single finite pattern some finite hidden world reproduces it, but no one fixed finite hidden world reproduces everything one qubit can do". This matches the realization being chosen per law (L236; Main §3.4 Proposition).
- **H-Bell (L250).** It now names all three open items: that a coupling graph can supply the remote dependence at all, without signalling, and while keeping the continuum limit. This matches L248 and Main §3.3's Corollary and H-Bell.
- **§2.5 opener (L130).** It now carries the shared hidden odds, the step "not fully predictable from the current observation", and "for the forecasts from every starting point". This matches Main §2.3 Theorem and Scope.

## 2. The gate-2 explanation changes
- **Why the hidden odds are shared (L134): correct.**
  - Main §2.3's proof uses this independence. If every Γ_s were a permutation, then "the visible configuration at each time t ≤ k would be σ_t of the root, μ_H-almost surely", so two positive-probability histories with the same endpoint would coincide.
  - That inference needs the hidden state to have law μ_H given every root. So "the step from two histories with a common endpoint to an overlap rests on this independence" is right. So is "a hidden start correlated with the visible one would make the rows forecasts of different preparations".
- **Why rows for starting points that never occur are kept (L134): correct, with one wording issue.**
  - Main §2.3's proof says: "some Γ_s … is not a permutation, possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix, which is why every row is kept". The writer's reason matches this, and "the argument needs the full square table" is right.
  - The wording issue is that an overlap always involves two rows, so it cannot "sit in such a row alone". See F2.
- **Memoryless windows against memory before the return (L144): correct.**
  - The precise sentence carries every hypothesis: the rooted family, the shared prior drawn independently of the root, and a full-support visible prior.
  - The direction from late memory to the failure of chaining holds without full support. A memory witness gives a non-permutation Γ_s, and Theorem 3 does the rest. The closing step is also right: a law Markov on every accessible window has M_k=0 at every accessible order, so k lies beyond those windows.
- **Both directions of the memory result (L118, L296): correct.**
  - Converse: if any one faithful realization has posteriors with different pushforwards, Theorem 2(a) gives different next-step laws for positive-probability histories ending at x. That is a memory witness, so M_t>0.
- **Keeping the past versus memory (L118): correct.**
  - "Every reversible world run from the start stores its whole visible past, even for a memoryless record" is I(X<t;H_t|X_t)=H(X<t|X_t) for bijective realizations (Main §3.4, Remark "a variational question"; L120).

## 3. Theorem 4 at every site
| Site | Line | Verdict |
|---|---|---|
| §3.2 question | L200 | Correct; it carries "for a theory with the structure described below". |
| Plain reading | L214 | Correct; it has every hypothesis: any nonempty finite system, any finite helper, the normalized finite Kraus instruments, and the §3.2 structure. |
| §6 Summary | L296 | Correct; it is the proved iff with the §3.2 structure and a nonempty finite system. |
| §1.2 roadmap | L37 | Contains no Theorem 4 formulation, so nothing to check. |
| Abstract | L17 | Too broad; see F1. |

L180 and L218 are also consistent with the theorem.

## 4. Unchanged statements: confirmed
- **Word for word as in r19:**
  - Theorems 1–4 and Theorem 2(a)–(c);
  - the recurrence Corollary and the Γ_t definition;
  - the Bell theorem paragraph and §4's three labelled paragraphs;
  - §5's "Toy model", "Results" and "Page curve";
  - §6's "Established" and "Conditional" paragraphs;
  - Realization, Quantum representation, Attribution and the independence paragraph;
  - (C1)–(C4) and the capacity paragraph, the three-notions paragraph and the card-CP paragraph.
- **§3.3 (L226).** The remainder after the moved gloss is verbatim.
- **Abstract.** After the new bridging sentence it is byte-identical to r19, so the recurrence scope is unchanged in the abstract, the Corollary (L140) and §6 (L298).
- **§2.4 Corollary.** Byte-identical.
- **Ledger.** Only `line` fields changed, with no fingerprint changes and no ID retired. `coverage_check` reports OK (134 statements).
- **"Proofs and sources" moves.** I recomputed the six SHA-256 digests in CHANGES-r20 §5 and all six match. The labels added are run-in only, and "Part" is prefixed to "(b) and the first inequality". The §2.2 picture and r19 L27 are verbatim apart from the stated opening words.

## 5. New text: checked against its sources
**Correct:**
- the abstract bridging sentence (Theorem 1 and the Corollary);
- §1.2 (L37);
- the definitions of law, realization, Markov and recurrence (L49), and of amplitude (L59);
- L85;
- L93: "no record of one repeated measurement can by itself rule out a partly hidden deterministic account, and the memory results … apply to every such quantum record" (Theorem 1 with Theorem 2);
- the rewritten L112: "what the past reveals about the hidden state", and "at least as different odds";
- L124, the persistence form in the coupling-step model;
- the openers at L130, L154 and L161;
- the definitions at L184 (completely positive, tracing out, diagonal, populations);
- L190 and L194 (classical in the sense of BBS24);
- L200, L224 (lift; right action, which acts first) and L234;
- the Bell definitions at L242;
- L254 (emergent, Hubble-scale density, de Sitter entropy);
- L286, with the counts "1,376 of the 40,320 toy maps";
- the Page definitions at L288;
- the Page-curve reading at L292:
  - it gives a cycle average under the three conditions;
  - it says when H-scramble fails, exactly as in BH-02 C6(a) and GR A.7;
  - it says H-decouple is not established;
  - it identifies the proper-shell case, as GR A.7 does.

**Not overstated anywhere.** The card analogy, the memory-without-readback gloss and the G3 conditional are unchanged from r19.

## Findings
**F1 — L17, abstract. Required.**
- *Problem.* "Exact finite operational quantum mechanics is characterized by five completion conditions that OI alone does not imply" drops Theorem 4's hypotheses. Those are an operational theory with the §3.2 structure (identity, coarse-graining, outcome-conditioned composition at every ancilla level, uniform-ancilla preparation, spectator-independent readout, ancilla discard) on a nonempty finite system. Stated without them, the sentence is broader than the theorem, which the owner's Theorem 4 rule forbids. CHANGES-r20 G3-2 left it unchanged.
- *Anchor.* GR §3.3, Theorem (operational-completion characterization) and its setup; `exactAll_iff_physical_general` (GeneralCarrier:100).
- *Replacement.* "For an operational theory with a stated minimal structure on a nonempty finite system, the available operations on the system and with every finite ancilla are exactly the finite Kraus instruments if and only if five completion conditions hold, and OI alone does not imply them."

**F2 — L134. Optional (precision).**
- *Problem.* "the overlap that breaks the chain can sit in such a row alone" — an overlap is between two rows.
- *Anchor.* Main §2.3, proof of Theorem (history readback + finite recurrence implies indivisibility): "possibly only through a row of a root of visible probability zero".
- *Replacement.* "…kept because the table can fail to be a permutation only through such a row, and the argument needs the full square table of forecasts".

**F3 — L49. Optional.**
- *Problem.* "its order L is the number of steps after which every configuration has returned to itself" should say the *least* such number. The Corollary's "0<s<L" depends on it.
- *Anchor.* Main §2.3 (order L, Γ_L=I).

**F4 — L230. Optional.**
- *Problem.* "the fixed-basis records identify every two quantum descriptions that agree on everything visible" is meant for lifts with trivial ancilla read in a fixed basis. Main notes that an ancilla carried between steps as hidden basis states can separate such lifts already in the two-step law.
- *Anchor.* Main §3.4, Remark (scope: representability, not selection of the relating evolution); `rooted_eq_iff_slice_eq` (trivial ancilla).
- *Replacement.* Add "with trivial ancilla" after "quantum descriptions".

## 6. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes, except the abstract's Theorem 4 sentence (F1).
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. Theorems 1–4, the memory equivalence in both directions, the recurrence Corollary with its full-support equivalence, the persistence form of (C2), the 1/|𝒰| floor and the descriptive cosmological-constant distinction are all stated at proved strength. The new glosses explain them without narrowing them.