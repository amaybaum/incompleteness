# SC-41: the Pauli-twirl classical-memory decomposition in Main §4.5

Base `main` at `0d917665`. Branch `corpus/sc41-pauli-twirl`.

## Finding

The Introduction (draft `9dc2b069`, L204) cites [Main §4.5] for a decomposition of the uniform-burn card game: the one-step channel is realized as the Pauli twirl, followed by $\sigma_o$ conditioned on the outcome. Main §4.5 contains only the fixed-card clause.

The finding is recorded in three places on `draft/oi-introductory-paper-20261025` at `9dc2b069`:
- `FULL-CORPUS-AUDIT-CONSOLIDATED-60c976fe.md`, row "Main §4.5";
- `FULL-CORPUS-AUDIT-60c976fe-B.md` O5;
- `FULL-CORPUS-AUDIT-60c976fe-VERIFY.md`, item 8.

The audit checked the mathematics; this unit re-verified it independently.

## Per-claim record

**Original claim.** It is in the Introduction (draft, not on `main`), at `papers/Introduction.md`:204 (`9dc2b069`):
> its memory is still classical in the sense of [BBS24], since the two-step identity is obtained by realizing the one-step channel as the Pauli twirl $\rho\mapsto\tfrac14\sigma_o\rho\sigma_o$, $o\in\{0,x,y,z\}$, and applying $\sigma_o$ conditioned on $o$, a decomposition a fixed initial hidden card does not admit [Main §4.5].

Main.md:714 at `0d917665` contains only the fixed-card clause. That clause reads "a swap realization, $\varphi(x,h) = (h,x)$ with an initialized hidden slot (§1.2), whose two-step maps are $\rho \mapsto |0\rangle\langle 0|$ and $\rho \mapsto \rho$ … this swap realization admits no classical-memory decomposition."

**Defect.** The Introduction cited Main for a result that Main does not state. The result itself is correct.

**Correction.** The result is added to Main §4.5 (Falsifiability), directly after the fixed-card clause, as a stated result with its proof. The added text:

> The same bijection with the hidden slot in the uniform diagonal state $I/2$ has two-step maps $\rho \mapsto \operatorname{tr}(\rho)\, I/2$ and $\rho \mapsto \rho$, and admits one: the instrument $\{\rho \mapsto \tfrac{1}{4}\sigma_o \rho\, \sigma_o\}_{o \in \{0,x,y,z\}}$, with $\sigma_0 = I$ and $\sigma_x, \sigma_y, \sigma_z$ the Pauli matrices, realizes the first map, since the qubit Pauli twirl satisfies $\tfrac{1}{4}\sum_o \sigma_o \rho\, \sigma_o = \operatorname{tr}(\rho)\, I/2$, and applying the unitary channel $\rho \mapsto \sigma_o \rho\, \sigma_o$ conditioned on outcome $o$ gives $\sum_o \sigma_o \big(\tfrac{1}{4}\sigma_o \rho\, \sigma_o\big) \sigma_o = \rho$, since $\sigma_o^2 = I$. The classification is therefore not fixed by the bijection; it depends on the hidden prior as well.

**Downstream consequences.**
- The Introduction's citation [Main §4.5] at L204 is now supported for both clauses: the decomposition, and that a fixed initial card admits none. No change to the Introduction is needed, and it was not touched (r32).
- Main §4.5's surrounding claims are unchanged. The classification still depends on the realization rather than on the visible law, and no memory-witness outcome falsifies the ontology at present.
- The new sentence makes one further point: one bijection gives opposite classifications under two hidden priors.
  - The two priors give different visible laws: $X_1=0$ under the fixed card, against $X_1$ uniform.
  - So this is a statement about the bijection, not a same-law comparison. The text says "not fixed by the bijection", not "by the law".
- GR :599 restates Main §4.5's classification ("a swap into an initialized hidden slot admits none"). It remains accurate and is not changed. Mirroring the uniform-slot case there is optional.
- No book chapter, glossary entry or the FULL mirror states the memory classification of the card game, so there is nothing to propagate there:
  - book ch01 :271–:281 gives the card game's matching odds only;
  - a grep for `twirl`, `classical-memory`, `Bäcker` and `memory-witness` over papers and book finds only Main §4.5 and GR :599.

## Verification against Main's definitions

Main §4.5 paraphrases [28] (Bäcker, Beyer and Strunz): a two-step process is classical-memory when its second map can be written as an instrument realizing the first map, followed by channels conditioned on the instrument's classical outcome. In symbols: $\Lambda_2=\sum_o\Phi_o\circ\mathcal I_o$, with $\{\mathcal I_o\}$ completely positive, $\sum_o\mathcal I_o=\Lambda_1$, and each $\Phi_o$ CPTP. The uniform-burn game is the swap $\varphi(x,b)=(b,x)$ with the burn card uniform: Introduction §2.6, which is Main §3.2's Remark example $\varphi(x,h)=(h,x)$, $\Phi(\rho)=I/2$.

The exact check `pauli_twirl_check.py` (sympy, Gaussian rationals, no floating point; output in `pauli_twirl_check.out`, ALL PASS) compares every map through its Choi matrix.

- **(A) The process.** With $U$ the permutation unitary of the swap and the hidden slot $I/2$, $\Lambda_1(\rho)=\operatorname{tr}_H[U(\rho\otimes I/2)U^\dagger]=\operatorname{tr}(\rho)I/2$ and $\Lambda_2=\mathrm{id}$, exactly.
- **(B) The decomposition.**
  - Each $\mathcal I_o=\tfrac14\sigma_o\cdot\sigma_o$ is CP: its Choi eigenvalues are $\{0,1/2\}$.
  - Each $\Phi_o=\mathrm{Ad}\,\sigma_o$ is unitary, hence CPTP.
  - $\sum_o\mathcal I_o=\Lambda_1$ and $\sum_o\Phi_o\circ\mathcal I_o=\Lambda_2$, exactly.
- **Controls.**
  - *Non-vacuity.* Without the conditioned correction, the composite is $\Lambda_1\ne\Lambda_2$.
  - *Countercontrol.* With the fixed card $|0\rangle\langle0|$:
    - $J(\Lambda_1)=I\otimes|0\rangle\langle0|$, so every CP $\mathcal I_o\le\Lambda_1$ has Choi matrix $A_o\otimes|0\rangle\langle0|$ and is measure-and-prepare;
    - $\Lambda_2=\mathrm{id}$, whose Choi matrix has partial-transpose eigenvalue $-1$, so it is entangled;
    - hence no decomposition exists. This is Main's existing clause, reproduced.
  - *Definition sensitivity.* The Pauli instrument does not realize the fixed-card $\Lambda_1$.

**Evidence level.**
- **Proof:** complete and elementary. The qubit Pauli-twirl identity and $\sigma_o^2=I$ appear in the added sentence.
- **Exact check:** the exact symbolic check above, retained here.
- **Not machine-checked:** there is no Lean statement and no coverage-ledger entry. The edited paragraph is not a canonical statement, and `coverage_check` reports no change.
- **Not a probe in `papers/oi_lattice_code`:** the manuscript sentence carries its own proof, so no probe was added (§A.28).

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| Main :714 (§4.5 Falsifiability) | fixed-card swap admits no classical-memory decomposition; the uniform-slot case is absent | adds: the uniform-slot swap admits the Pauli-twirl decomposition, with proof; the classification depends on the hidden prior as well as the bijection | this unit's proof; exact check |

Rebuilt: `papers/Main.{tex,pdf}`, 96 → 96 pages, median characters per page 3273.5 → 3273.5.

## Re-grep (papers/*.md, book/*.md)

| Pattern | Count | Where |
|---|---|---|
| `Pauli twirl` | 1 | Main :714 |
| `admits no classical-memory decomposition` | 1 | Main :714 |
| `admits none` | 1 | GR :599, unchanged and consistent |
| `classical-memory` | 2 | Main :714 (×2, counted once per line); GR :599 |

## Claims made conditional or removed

None. One result is added, with proof.

## Lean

No Lean change is needed; nothing **requires formal change**.

## Overlap with open PRs

None. No open PR (#961, #962, #963, #964, #967, #968, #969, #971) changes Main :710–:718 at `0d917665`.

## Cross-unit dependencies (shared definitions, scopes, sentences)

1. **Main §4.5's Falsifiability paragraph, :714.** It now has one added sentence. A unit editing the [28] classification text, or the swap example there, must keep both clauses. SC-33 (#968) and SC-34 (#971) edit nearby Main lines (:700, :706, :720) but not :714.
2. **The scope "the classification depends on the realization rather than on the visible law".** This is unchanged. The added sentence adds "and on the hidden prior" for a fixed bijection. GR :599 mirrors the unchanged part.
3. **The Introduction (r32), L204.** Its citation [Main §4.5] is now supported for both clauses. If r32 changes the wording, the object must stay the swap with hidden slot $I/2$ and the instrument $\tfrac14\sigma_o\cdot\sigma_o$.
4. **SC-40** (`corpus/sc40-c2-c3-statements`) does not touch Main §4.5. The two units are independent.

## Open research questions (for #970)

- **Coherent bridge.** Whether the instrument $\{\tfrac14\sigma_o\cdot\sigma_o\}$ is implementable from the substratum is part of the open coherent-preparation and instrument bridge (§3.4). The classification is a property of the process maps only.

## Checks

- `python3 tools/release_gate.py`: all steps pass except `lean-axioms`, which needs the local toolchain.
- `python3 tools/coverage_check.py`: OK (128 canonical statements).
- `python3 verification/lean/edge_rigidity_probe.py`: ALL CHECKS PASS.
- Scan of added lines: no §A.32/§A.33 phrase, caps, revision voice, local path or secret.
- `sh ./build.sh Main`: OK, with no dropped glyphs.

## Review findings applied

- Main §4.5 now names the initialized-slot swap where it says the bridge alone does not supply a constraint. The
  paragraph describes two swap realizations, and only the initialized-slot one admits no classical-memory
  decomposition.
- The prior-dependence sentence now notes that the two priors give different visible laws ($X_1=0$ against $X_1$
  uniform).

## Stronger result recorded, not added to Main

The independent reviewer gave a stronger statement with a proof; it is recorded here for #970. With hidden prior
$\mathrm{diag}(p,1-p)$, the swap admits a classical-memory decomposition if and only if $p=\tfrac12$. The proof:
- the identity has Kraus rank 1, so each $\Phi_o\circ\mathcal I_o=q_o\,\mathrm{id}$;
- a qubit channel with a CPTP left inverse is $\mathrm{Ad}\,V$;
- so $\Lambda_1=\sum_o q_o\,\mathrm{Ad}\,V_o$ is unital, which forces the slot state to be $I/2$.

This also gives a second proof of the fixed-card clause. It has not been checked against the primary text of [28].
The source was not reachable from the review session, so the decomposition was checked against Main's paraphrase of
the definition.
