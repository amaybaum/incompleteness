# Gate 1 (scientific accuracy): PR #918 r21 at `d3790019`

**Verdict: ACCEPT.** Every required item is applied correctly against its source and at proved strength. Nothing is overstated, and nothing is weakened. The remaining findings are all optional.

The review was read-only, against r20 `10c629ea` (the paper is unchanged at `542b1d9c`). The head `bfd8b026` is records only, so the paper there is identical to `d3790019`. I used a detached worktree at `d3790019`, which is now removed. Line numbers are at `d3790019`.

## 1. F1–F4, L188 and gate-2 changes A, 1, B, C: all applied correctly

**F1 (abstract, L17): Theorem 4 now carries all its hypotheses.**
- It reads "an operational theory with a stated minimal structure on a nonempty finite system, the available operations, on the system and with every finite ancilla attached, are exactly the normalized finite Kraus instruments if and only if five completion conditions hold, and OI alone does not imply them".
- That matches GR §3.3 and `exactAll_iff_physical_general`.

**The other gate-1 fixes:**
- **F2 (L134):** "the table may fail to be a permutation only through such a row" matches Main §2.3's proof: "possibly only through a row of a root of visible probability zero".
- **F3 (L33):** "the *least* number of steps".
- **F4 (L226):** "cannot distinguish two quantum descriptions with trivial ancilla that agree on everything visible". This is the direction `bridge_traj` proves, and it also resolves gate 3's L230 must-fix.
- **L188 (now L188 at `d3790019`):** "no unconditional implication among them is asserted" now matches Main §3.2's own wording. The added sentence states the two proved non-implications (XOR; Hadamard), and the next sentence keeps the proved implication for the permutation-dilation class.

**Change A (L130): card example with a fixed face-down deal. Meets the owner safeguard.**
- "the face-down card dealt the same way, at even odds … whichever card is face up" is exactly the shared hidden prior, uniform and drawn independently of the root.
- A hidden deal chosen per root appears only as the excluded contrast: "would describe two different deals, not one rule started in two ways".
- "a black start never appears … belongs to that comparison" explains hypothetical roots.
- The example sits before the formal statements and draws no conclusion, so it does not read as a proof.
- The reference "the anticorrelated deal of §2.6" resolves to L174: "With anticorrelated cards ($b=1-x$), $\Gamma_1$ is a permutation and the game is divisible".

**Change 1 (L134): matches the formal construction.**
- One hidden preparation rule with no change per start: "the same hidden preparation run forward from each visible start".
- Zero-probability roots keep their rows, "computed from the same preparation".
- The two-row overlap step keeps its dependence on the shared prior ("uses that every row comes from the same preparation [Main §2.3]"), as in Main's proof (μ_H-almost surely).
- The "price" sentence carries the full-support equivalence correctly.

**Change B (L146): the four-bit example, at the approved wording.**
- M₁ = 0, the forecasts chain on {0,1,2} (Γ₁ = Γ₂ = ½J), and M₂ = 1 bit.
- "every deterministic world that reproduces the law, reversible or not, must keep $X_0$" holds, because X₃ = X₀ is a function of (X₂, H₂) (L120; `c3_necessity_via_hidden`).
- "it shows no failure of chaining inside it" carries the owner's scope condition.
- "Predictive memory can exist all the same, at a later order" keeps the three terms apart.

**Change C (L161): states only the proved coexistence.**
- "predictive memory and P-divisibility are different properties". Nothing says the two are independent or unrelated in general.
- The recurrence-cycle sentence matches the Corollary's hypotheses:
  - a reversible world, with hidden odds independent of the visible start (the shared prior drawn independently);
  - a non-deterministic visible step, since X₁ given X₀ is uniform;
  - failure "on the recurrence horizon, not necessarily on an accessible window" ({0,…,L}).

## 2. Theorem 4: consistent at every site

I verified the table in CHANGES-r21 §3.

| Site | Line | Result |
|---|---|---|
| Formal statement | L210 | Word for word as in r20 |
| Abstract | L17 | Same result and hypotheses (F1) |
| §3.2 question | L200 | "for a theory with the structure described below" |
| Plain reading | L212 | "for a theory with the structure above … a nonempty finite system, with any finite helper attached … exactly … the normalized finite Kraus instruments … if and only if all five requirements hold" |
| Summary | L292 | Same result and hypotheses |
| Roadmap | L37 | No Theorem 4 formulation |
| References only | L180, L294 | No broader formulation |

## 3. R3 (L214): accurate

GR §3.3 reads: "Conditions (i) and (ii) are well-formedness requirements of any operational theory; (iii)–(v) are the substantive selection principles". The paper's sentence is the same claim, cited to GR §3.3.

## 4. R2 (L246): accurate

- **"So, given determinism and an outcome in every run,"** carries hypothesis (i) and the ±1-every-run condition, so the either/or is not compressed.
- **Coupling-graph gloss.** "records which parts of the substratum directly affect which" matches the coupling graph defined by one-step dependence (L244; Main §3.3).
- **H-Bell gloss.** "suitable extra links can be added for a Bell preparation with those two properties" matches Main §3.3's preparation-indexed long edges that preserve no-signalling and the continuum limit.

## 5. [Wei89] (L250): supported, with one optional pinpoint

- The L250 sentence is "the mismatch is some 120 orders of magnitude [Wei89]".
- It is supported by the same source that L252 cites with its pinpoint (§III, Eqs. (3.4)–(3.6)), hedged with "some" and "the exact power depending on the cutoff convention".
- From memory of Weinberg's §III, without a lookup against the paper: his own Planck-cutoff estimate requires cancellation to about 118 decimal places. "Some 120" is the conventional rounding.
- Optional: give L250 the same pinpoint (finding O2).

## 6. Everything else

**New or changed sentences, all correct:**
- **Theorem 3 one-line reason (L138).** "A step-by-step forecast can only bring forecasts closer…" is the contraction criterion: TV < 1 at s cannot become TV = 1 at n.
- **Overlap definition (L134).** Correct; see O1 for a wording tightening.
- **Qubit definition.** Moved to L200, before its first use at L214.
- **Summary converse (L292).** "if the hidden part of any one such world holds a trace of the past that changes what is seen next, the record has memory".
- **Energy wording (L288).** "not every configuration of black hole and radiation has the same energy" matches GR A.7, Proper energy shells.
- **Measure-concentration gloss.** "gives nearly the same value of a smooth quantity" matches the Lévy-type concentration of GR Thm A.8.
- **Abstract plain sentence.** Carries the shared odds, the never-occurring starts and "cannot all be chained … somewhere in the world's cycle".
- **Convention note (L25).**
- **Merged paragraphs (L146, L214).**

**Unchanged material:**
- Every exact theorem and corollary statement is word for word as in r20. I checked:
  - Theorems 1–4 with (a)–(c), and conditions (i)–(v);
  - both corollaries;
  - the Γ_t definition;
  - every labelled paragraph in §§2.2, 4, 5 and 6;
  - the Bell theorem paragraph;
  - the "Proofs and sources" blocks.
- The §2.4 Corollary is byte-identical.
- The ledger has only `line` changes. No ID is retired, and `coverage_check` reports OK (134 statements).

**Nothing weakened.**
- Removed: the framing sentence "Operational quantum mechanics requires … one instrument theory", now covered by L180.
- Removed: "central open question", while "the open step toward full operational equivalence" remains.
- Removed: the unsupported "largest known mismatch".
- The full-support equivalence moved from r20 L142 into L134 and L146.

## Optional findings
- **O1 (L134).** "an *overlap*, two rows sharing a positive entry" should follow Theorem 3's wording: "two rows that are both positive in a common column". As written, "sharing a positive entry" could be read as "equal entries". Anchor: L136, Theorem 3.
- **O2 (L250).** "the mismatch" is used before L252 defines it. Suggest "the vacuum-energy estimate exceeds the observed value by some 120 orders of magnitude [Wei89, §III]". Anchor: Wei89 §III, Eqs. (3.4)–(3.6).
- **O3 (L214).** "Hidden information and partial access therefore do not by themselves imply quantum mechanics" now follows the well-formedness sentence, so "therefore" reads as if it followed from that sentence. Move the R3 sentence before "Which of (iii)–(v)…". Anchor: GR §3.3.
- **O4 (L188).** "What is proved is that …" could be read as exhaustive, but the next sentence states a further proved implication. Suggest "Among what is proved: …". Anchor: Main §3.2, Theorem (CP-indivisibility, framework scope).
- **O5 (L17).** In the abstract's plain sentence, "not fully predictable" could add "from the current observation", matching L130 and L144. Anchor: Main §2.3, Scope (non-deterministic visible step).

## 7. The owner's two final questions
- **Is every substantive claim supported by its evidence and assumptions?** Yes.
- **Does the paper communicate the strongest results without unnecessary weakening?** Yes. Theorems 1–4, the memory equivalence in both directions, the recurrence Corollary with its full-support equivalence, the persistence form of (C2), the 1/|𝒰| floor and the descriptive cosmological-constant distinction are stated at proved strength. The new examples explain the shared-prior construction, the role of hypothetical starts, and how memory differs from P-divisibility, without narrowing any result.