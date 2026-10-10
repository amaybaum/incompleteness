# Track B act 31 — off-locus uniqueness after full product admission: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #750. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A31.json`, and on the pull request.

- **`D`** — `d61c6c5409db201e3c25abbf3ec0ecce1f530684`, act 30's receipt commit `Q`, the head of
  `main` after act 30's landing.
- **`F`** — `f5bf75e1b454ed2786fce0f689e93845f35637f6`, whose only parent is `D` and which adds the
  preregistration alone, blob `f6064e59cad2f076d8a99cd95f628973987084f5`. Its `check-run` attestation
  is run 36241183166.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A31-1-NONUNIQUE`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A31-1` | `A31-1-NONUNIQUE`, theorem `a31_nonunique` | the same, very high |

The verdict theorem has the frozen statement verbatim, compared after collapsing whitespace, and so
do the corollary `a31_c_exclusive` and the three statements required under this label:
`a31_shared_witnesses`, `a31_shared_transposition` and `a31_shared_precompose`.

***

## The frozen post-round sentence

> At the frozen product configuration, for the pair of local class bijections act 28 fixed in advance, two exhibited transition families each satisfy all eight prefix conjuncts and factorization with factor families realizing that pair, and take `GramPhaseEquiv`-inequivalent values at time zero on an exhibited tuple realizable at the product visible family whose class lies outside the product locus, at evidence level 2. This is a nonuniqueness statement about two exhibited laws at that pair and that time. It does not say that factorization is empty, has no content, or fails to restrict anything, and it reports nothing about any other pair or configuration.

***

## The two laws and the tuple

- **The tuple `W`** is act 21's product tuple `G(H₁) ⊠ G(Hᵢ)` relabelled by the carrier transposition
  exchanging `(0, 1)` and `(1, 0)`. **`W₂`** is the same with its second factor relabelled by `(2 3)`.
- **The first law** is `fun _ => RelabelTransition (Equiv.prodCongr (Equiv.swap 2 3) 1)`, act 29's
  relabelling family of `(2 3) × 1`.
- **The second law** is `fun _ => Φ₁`, where `Φ₁` is `a30_s_strictify`'s replacement of that
  relabelling precomposed by `τ`. Here `τ` is the transposition of the classes of `W` and `W₂` that
  fixes every other tuple.

At time zero the first law sends `W` to `RelabelTransition (Equiv.prodCongr (Equiv.swap 2 3) 1) W`.
The second sends it to a tuple equivalent to the same relabelling of `W₂`. The relabelling reflects
the equivalence, and `W` and `W₂` are inequivalent, so the two values are inequivalent.

***

## What was proved, and how

**`a31_shared_witnesses`.**
- **Realizability.** `W` and `W₂` are realizable at the product visible family by
  `a28_shared_product_realizable`, applied to factors realized through `sh1_necessity` and
  `realizable_relabel`, followed by `realizable_relabel` for the carrier transposition.
- **Off the locus.** Each class lies off the product locus by `a28_s_locus_first_index`, read at the
  fibres `(0, 1)` and `(1, 1)` with matrix indices `(2, 0)` and `(2, 1)`. The two entries there are
  `1/16` and `I/16`.
- **Inequivalence.** Read at the fibres `(0, 0)` and `(0, 2)` with matrix indices `(0, 0)` and
  `(0, 2)`, one phase factor would have to carry `1/16` to `1/16` and also `1/16` to `I/16`.
- **Entries.** Every entry comes from `witness_supply`'s explicit matrices, read through
  `a27_shared_fibreGram_entry`.

**`a31_shared_transposition`.**
- The map is `τ G := if G ≈ W then W₂ else if G ≈ W₂ then W else G`, under `classical`.
- Each property follows by cases, with `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and
  `gramPhaseEquiv_trans`.
- A tuple of the locus is equivalent to neither `W` nor `W₂`, since both are off the locus, so `τ`
  fixes it.

**`a31_shared_precompose`.** Each conjunct holds for `fun t G => Φ t (τ G)`:
- **Total evolution:** by the trajectory that iterates the precomposed family from the initial tuple.
- **Admissibility:** by `τ`'s and `Φ`'s.
- **Homogeneity:** by `Φ`'s constant value precomposed with `τ`.
- **Injectivity on classes:** through `τ`'s descent and involution.
- **Surjectivity:** by precomposing `Φ`'s preimage with `τ`.
- **Descent:** by `τ`'s and `Φ`'s.
- **Factorization and the pair clause:** unchanged, because `τ` fixes every product tuple.

**`a31_nonunique`** follows the freeze's route, steps 1 and 5:
- **The first law.** `a29_n_relabel_instance` at `σ₁ = (2 3)`, `σ₂ = 1` gives the first law's
  conjuncts 3 to 8, factorization and the product equation. `relabel_one` turns that equation into
  the pair clause, and `a29_p_hold` gives conjuncts 1 and 2.
- **The second law.** `a31_shared_precompose` gives the precomposed family's conjuncts 3 to 7,
  factorization and pair clause. `a30_s_strictify` gives `Φ₁` with a strict-natural lift, and
  `a30_t_transfer` carries the eligibility to `fun _ => Φ₁`. Conjunct 8 is the strict lift with the
  identities as induced maps, through `rnt1_strict_imp_twisted`. `a29_p_hold` gives conjuncts 1
  and 2.
- **The disagreement** follows from `gramPhaseEquiv_of_relabel`.

**`a31_c_exclusive`**: `P_U` applied to `P_N`'s witnesses gives the equivalence that `P_N` negates.

**Zero definitions.** The module carries five theorems, each followed by its `#print axioms` line.

### The route-authorization matrix — honoured

Every helper the proofs consume is on the freeze's provenance list, or is Mathlib:
- acts 11, 12, 17 and 18: `sh1_necessity`, `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and
  `gramPhaseEquiv_trans`;
- act 20: `RelabelTransition` and `rnt1_strict_imp_twisted`;
- act 21: `realizable_relabel`, `relabel_gramPhaseEquiv`, `relabel_symm_relabel`,
  `gramPhaseEquiv_of_relabel`, `witness_supply` and `relabel_one`;
- act 27: `a27_shared_fibreGram_entry`;
- act 28: `a28_s_locus_first_index` and `a28_shared_product_realizable`;
- act 29: `a29_p_hold` and `a29_n_relabel_instance`;
- act 30: `a30_s_strictify` and `a30_t_transfer`.

Each theorem also keeps to its row:
- `a31_shared_witnesses` consumes neither `a28_s_proper` nor any verdict of this round;
- `a31_nonunique` consumes neither `a28_s_proper` nor any off-locus value of a law it did not
  construct;
- `a31_c_exclusive` consumes neither verdict theorem.

No deviation is incurred.

### Readings of the freeze's route, recorded and not repaired

- **RD1.** Route step 2 names `product_realizable` for the realizability of `W` and `W₂`. The proof
  consumes `a28_shared_product_realizable`, which is act 28's composite of `sh1_sufficiency`,
  `product_realizable` and `sh1_necessity` and is on the provenance list.

***

## The `P0` cell

On `A31-1-NONUNIQUE`, act 29's frozen row 1 addition and the standing clause are appended once to
the `P0` cell of `verification/ROADMAP.md`, after act 30's sentence and its standing clause. The
file's blob at `E` is `4b04375e8fd88c268dd39608d1b3c145a36f07b9`, the blob rehearsed for this case
before the freeze. The guard is `D`'s, byte for byte.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `f6064e59cad2f076d8a99cd95f628973987084f5`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `78af60da95d7fb9be53bfa104da176565bdd3b5a` at stage 1.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals; 6 duality mutations fail as required`, `controls: 3 rows hold as
    frozen, 39 mutation controls fail as required` and `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on six receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A31-1-NONUNIQUE`, less this note:
  - added: the preregistration, `controls.py` and the module;
  - modified: `OIBridge.lean`, the census and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 31 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**
