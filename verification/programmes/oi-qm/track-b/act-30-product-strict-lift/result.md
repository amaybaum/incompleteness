# Track B act 30 — product-carrier strictification, its transfer, the lift, and full admission: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #747. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `E`, the reconciliation, the verdict
on the receipt commit and the gate's check of this round's own receipt are recorded in the receipt,
`verification/receipts/A30.json`, and on the pull request.

- **`D`** — `48450428f528fe489d454458e21c9394aef6a02f`, the head of `main` after `V3-14`'s landing.
- **`F`** — `3f337a95df6009102948690533d877ee1e4bf90d`, whose only parent is `D` and which adds the
  preregistration alone, blob `c637999c884328cb085cb9dbbf27a39bb44e6643`. Its `check-run` attestation
  is run 36225958085, recorded in comment 5844217779; its `owner-designation` attestation is comment
  5844220223.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

## The outcome vector

| row | vector |
| --- | --- |
| 1 | `A30-S-HOLD` · `A30-T-HOLD` · `A30-N-LIFTS` · `A30-0-ADMITS` |

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A30-S` | `A30-S-HOLD`, theorem `a30_s_strictify` | the same, high |
| `A30-T` | `A30-T-HOLD`, theorem `a30_t_transfer` | the same, high |
| `A30-N` | `A30-N-LIFTS`, theorem `a30_n_lifts` | the same, high |
| `A30-0` | `A30-0-ADMITS`, theorem `a30_0_admits` | the same, high |

Each label's theorem has the frozen statement verbatim, compared after collapsing whitespace. The
three corollary theorems are present with their frozen statements: `a30_c_lift`, `a30_c_admit` and
`a30_c_restrict`. `A30-N-LIFTS` is `a30_c_lift` applied to `a30_s_strictify` and `a30_t_transfer`;
`A30-0-ADMITS` is `a30_c_admit` applied to `a30_n_lifts`. No negative label is earned, so no
counterexample is named.

***

## The frozen post-round sentences, for the labels earned

### `A30-S-HOLD`

> At the frozen product configuration, every map preserving realizability and descending on
> realizable tuples is pointwise `GramPhaseEquiv`-equivalent, and equal off realizable tuples, to a
> map with a strictly natural representative-level lift, at evidence level 2. This is a statement at
> the exact configuration and says nothing about any other.

### `A30-T-HOLD`

> At the frozen product configuration, replacing a family by one pointwise `GramPhaseEquiv`-equivalent
> on realizable tuples and equal off them keeps every conjunct of eligibility for the same prescribed
> pair, at evidence level 2.

### `A30-N-LIFTS`

> At the frozen product configuration, for every prescribed pair of bijections of the single-carrier
> realizable class spaces there is a transition family satisfying conjuncts 3 to 7 and factorization
> with factor families realizing that pair which also satisfies representative-level gauge
> naturality at act 20's certified strength, at the product carrier, at evidence level 2. **This is
> an existence statement about some such family. It does not disturb act 23's verdict about its own
> formula**, which is a statement that one exact formula admits no lift.

### `A30-0-ADMITS`

> At the frozen product configuration, for the ordered decomposition named, every pair of bijections
> of the single-carrier realizable class spaces is the class action of the factor families of a
> single transition family satisfying all eight prefix conjuncts and factorization as act 21 froze
> it, at evidence level 2. This is a statement about the exact declarations at the exact
> configuration. It does not say that any particular formula carries those conjuncts, does not
> disturb act 23's verdict about its own formula, and reports nothing about any other configuration
> or decomposition.

***

## What was proved, and how

**`a30_s_strictify`** instantiates the shared lemma `a30_shared_strictify`, which is stated for any
carrier, any one-element ancilla and any visible matrix with no zero entry. It is instantiated at
the ancilla `Fin 1 × Fin 1` with anchor `((0 : Fin 1), (0 : Fin 1))`, the index
`((0 : Fin 4), (0 : Fin 4))` and the visible matrix `Γ 0`, every entry of which is `1 / 16`. No
verdict is stated of the shared lemma.

The construction is act 27's quotient-and-dilation route:
- a chosen admissible dilation `S ω` for each realizable class `ω`;
- the class map `f̄` of the input;
- a decomposition `U = D * S (q U) * K` from `twoSided_slice_iff`;
- the transported lift `Ψ U = D * S (f̄ (q U)) * K` on admissible `U`, and `Ψ U = U` otherwise;
- the replacement tuple `Φ₁ G = FibreGram a₀ (Ψ U_G)` on realizable `G`, and `Φ₁ G = Φ₀ G` off them.

The lift is well defined by `a30_shared_transport_eq`, which is derived from the torsor lemma
`a30_shared_torsor`. The lifting equality holds because two admissible dilations with equal fibre
Gram differ by a left gauge element, which is `a30_shared_same_gram`.

**`a30_t_transfer`** reduces to one pointwise fact: `GramPhaseEquiv (Φ₁ G) (Φ₀ G)` at **every** tuple.
On realizable tuples this is the hypothesis. Off them the two maps are equal, and `gramPhaseEquiv_refl`
gives it. Every conjunct of eligibility then transfers by transitivity of `GramPhaseEquiv`, and
realizability through `realizable_of_gramPhaseEquiv`. The factorization keeps its factor families.

**`a30_c_lift`** takes act 28's `a28_0_construction` for the prescribed pair, whose family is constant
in time. It applies `P_S` at that constant map, and `P_T` to carry eligibility to the replacement.
Conjunct 8 then holds at every time with the lift `Ψ` and the induced maps `id` and `id`, the twisted
form coming from `rnt1_strict_imp_twisted`. **`a30_c_admit`** applies act 29's `a29_p_hold` to
`P_N`'s own witness. **`a30_c_restrict`** is the projection. So `P_N` and `P_0` are equivalent, and
the vector's last two labels agree as the table requires.

**Zero definitions.** The module carries twenty-six theorems — nineteen `a30_shared_…` lemmas, the
four label theorems and the three corollaries — each followed by its `#print axioms` line.

### The route-authorization matrix — honoured

Every helper the proofs consume is on the frozen list or is one of this round's own shared lemmas:
- act 12's `sh1_sufficiency`, `sh1_necessity`, `fibreGram_apply`, `fibreGram_left_mul`,
  `left_preserves_admissible`, `one_leftFibreGroup`, `weak_mul`, `gramPhaseEquiv_of_twoSided`,
  `weak_diagonal_phase` and `twoSided_slice_iff`;
- act 11's `weak_preserves_admissible` and `weak_anchor_coeff_norm_one`;
- act 17's `gramPhaseEquiv_refl`, `gramPhaseEquiv_symm` and `gramPhaseEquiv_trans`;
- act 21's `realizable_of_gramPhaseEquiv`;
- Mathlib.

The two helpers act 27's proofs used and the list does not name, `rows_phase` and
`star_mul_self_eq_norm_sq`, are re-proved as `a30_shared_rows_phase` and `a30_shared_star_mul_self`. Each theorem also
keeps to its row:
- `P_S`'s theorem consumes no act 27 result, no `a28_0_construction` and no `a29_p_hold`;
- `P_T`'s consumes neither `P_S`'s theorem nor `a29_p_hold`;
- `a30_c_lift` consumes `a28_0_construction` and `rnt1_strict_imp_twisted` and not `a29_p_hold`;
- `a30_c_admit` consumes `a29_p_hold`.

No deviation is incurred.

### Readings of the freeze's route, recorded and not repaired

- **RD1.** Route step 3 reads the transfer as a case split on realizability at each conjunct. The proof
  makes the split once: the replacement is `GramPhaseEquiv`-equivalent to the input at every tuple,
  and each conjunct then follows by transitivity.
- **RD2.** Route step 1 names the torsor statement. It is proved as `a30_shared_torsor`, with an index
  of the carrier as an argument, and the construction consumes its consequence
  `a30_shared_transport_eq`.

***

## The assumption-watch note — constant induced maps

Conjunct 8 places no constraint on `αL` and `αR` beyond act 20's closure conjuncts. With
`αL = αR = fun _ => 1` it asks for a lift `Ψ` constant along gauge orbits. By the freeze's reading
(hand reasoning, not a result), a family that factors exactly through `GramPhaseEquiv` classes on
dilatable tuples and preserves realizability has such a lift, and every descending family is
pointwise equivalent to one that does. If so, conjunct 8 read with constant maps adds nothing, up to
law equivalence, to conjuncts 4 and 7. **This round establishes none of that**, rests no verdict on
it, and changes no declaration. It is recorded so that a later round reading conjunct 8 as a
restriction knows the reading exists.

No verdict here rests on constant induced maps: the lift of `a30_c_lift` carries the identities.

***

## The `P0` cell and the guard

On `A30-0-ADMITS` the `P0` cell of `verification/ROADMAP.md` is corrected as the freeze prescribes.
Act 28's and act 29's frozen *undecided* sentences, each with its standing clause, are replaced once
by act 29's rows 1–3 sentence with the standing clause. The file's blob at `E` is
`e6779380f858bcb905fc9877ed2f11bf5de75c95`.

Acts 28 and 29 cease to own the current status of that cell. The frozen ledger is applied to the guard
at `D`, blob `8dad60d0aac870fced7deeec44c0dbdfcb3d45de`, and gives blob
`0475fe3d8c5724a7bf918bf3fd75ae06370cef26`. It retires the live-`ROADMAP` legs by these eleven
entries:
- `pfr-road-standing` — R7-PFR's ROADMAP standing-clause constant, read only by its ROADMAP leg;
- `pfr-p0` — R7-PFR's frozen P0 sentence constant, read only by its ROADMAP leg;
- `pfr-p0-cell-and-road-ok` — the P0-cell reader (read only by R7-PFR's and R7-PRA's ROADMAP legs) and R7-PFR's ROADMAP gating predicate;
- `pfr-road-read` — R7-PFR's read of verification/ROADMAP.md;
- `pfr-road-leg` — R7-PFR's ROADMAP check entry and its seven road-mut mutation controls;
- `pfr-description` — R7-PFR's check description, less its statements that the ROADMAP cell is read;
- `pra-road-constants` — R7-PRA's frozen P0 sentence, standing-clause and anchor constants, read only by its ROADMAP leg;
- `pra-road-ok` — R7-PRA's ROADMAP gating predicate;
- `pra-road-read` — R7-PRA's read of verification/ROADMAP.md;
- `pra-road-leg` — R7-PRA's ROADMAP check entry, its nine road-mut mutation controls and its road-successor-tolerated positive control;
- `pra-description` — R7-PRA's check description, less its statements that the ROADMAP cell is read.

Every other byte of the guard is `D`'s. Both checks, `R7-PFR` and `R7-PRA`, stay in the guard, under
their tags and in their places, and keep their theorem pins, census checks and outcome-vector checks.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `c637999c884328cb085cb9dbbf27a39bb44e6643`, verified
  before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `718e33b3cde5653e277734e337f4b931a237e907` at stage 1;
    `controls.py --self-test` prints `controls: 25 rows hold as frozen, 51 mutation controls fail as
    required` and `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    findings are those that belong to later stages: the corollaries before stage 4, and at stage 3
    the vector that stage 4 completes.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on five receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 5>` lists the frozen set for
  `A30-0-ADMITS`, less this note, and no legacy record: the preregistration and `controls.py` added,
  the module added, and `OIBridge.lean`, the census, the guard and `ROADMAP.md` modified.

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

None against the freeze.

> **THE CLAUSE, carried at this mention — the result note.**
> Act 30 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**
