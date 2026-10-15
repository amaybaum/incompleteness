# P0 locality sources — which locality properties follow from OI's adopted premises: result

This is a research result on a local branch cut from #834's head `55450d57`. It is not a native round and adopts
nothing. It is not for merge without separate review, and it does not change #834.

## Provenance

- **Rules.** `RULES.md` was committed at `fccd7008` (blob `d0b286ea`), before the script existed.
- **Amendment.** `amendments/amendment-1.md` was committed at `4c6a0fbc`, after one development run and before the
  recorded runs.
  - The development run used script sha256 `01d3581f…` and gave output sha256 `556c4a01…`. It printed `LS-SPLIT` with
    every control green.
  - A skeptical pass over that favourable reading (§A.31) found that the rules modelled Lemma 3's "maximal entropy
    compatible with the observer's records" only with orbit-level records.
  - The amendment adds the cell HI-rec, in which records are registered values. The development run's tokens are not
    used.
- **Files.**
  - `p0_ls_exact.py`, sha256 `904e242e…`. It uses the standard library only, with exact integer and `Fraction`
    arithmetic.
  - `p0-ls-exact-output.txt`, sha256 `880c2904…`.
- **Replay.** Two parallel runs under `python3 -I`, each about 70 s, are byte-identical (K0). These are local runs, not
  `check-run` attestations.

## Verdict, as printed

```
TOKEN LS-TC
TOKEN LS-FAC
TOKEN LS-INS-ALL-PRIORS
TOKEN LS-HI-DEFAULT
TOKEN LS-HI-REC
TOKEN LS-HI-ORBIT-FAILS
TOKEN LS-HI-PRIOR-FAILS
TOKEN LS-SEL-SPLIT
VERDICT LS-SPLIT
checks: 8, failures: 0
```

The following controls passed: K-leap, K-free, K-prod, K-cone-neg, K-INS-neg, K-orbit and K-prod-agree. The two product
tests disagreed on no law. The reading the verdict licenses, as amended:

> Across an uncoupled cut of a finite-range substratum, intervention no-signalling follows from the rule's dependency
> structure for every hidden prior. Hidden-sector independence follows from the counting measure, or from Lemma 3's
> maximal-entropy selection conditioned on regional records. It does not follow from Lemma 3's law on the actual orbit
> when the regional periods share a factor, nor from structured realization priors.

## 1. Measurements

| cell | what was measured |
| --- | --- |
| TC | On `C-chain`, every point mass (531441) and every one of 10 site interventions at site 5 leave site 0's `(p, c)` unchanged for `t < 5`. Some intervention changes `c₀` at `t = 5`. Mutating the rule so that site 0 reads site 3 breaks the check (K-cone-neg) |
| FAC | `φ = φ₁ × φ₂` exhaustively on `U-free(3,5)`, on the four `U-edge(3, α, β)` and on every ordered pair of `FAM(3)` and `FAM(5)`, up to 390625 configurations per pair. On `C-cut`, each region's next state depends on the other region |
| INS | No change in region 1's visible laws at `t = 0..8`, or in its two-time laws, under any tested intervention. This covers every ensemble: E-cnt, all E-reg, all E-orb, E-pri, and every point mass. The counts are 32, 208 and 4 × 1500 ensembles, and 81, 625 and 4 × 6561 point masses. `C-cut` signals at `t = 1` (K-INS-neg) |
| HI-default | Under E-cnt and every E-reg, every joint visible law and one-step kernel is a product |
| HI-rec | For every registered-value record, 9, 25 or 81 per configuration, the record-conditioned law gives product visible laws and kernels and no selection dependence |
| HI-orbit | W4 holds with no exception on 4909 joint orbits at `q = 3` and 549317 at `q = 5`. 589 and 18101 of these, respectively, have a product law. On `U-free` and `U-edge`, 4240 orbit laws have a non-product visible law or kernel while INS holds |
| HI-prior | E-pri gives a non-product one-step kernel with INS on every model |
| SEL | No selection dependence under E-cnt or E-reg. 4092 correlated laws, orbit or prior, show it |

**Supplementary, deciding nothing.** For every registered record on every model, the unconditioned maximal-entropy
invariant law `μ_R` is not a product on `Conf`. That is 9/9, 25/25 and 81/81 records. So the invariant law that the
records select is correlated across the uncoupled cut. Only its record-conditioned slice, the law that predicts from the
records, is a product.

## 2. Written statements [W]

These are W1–W6 of `RULES.md` §5, and each was checked on the frozen configurations. Two notes:

- **W2 holds for every prior.** Region 1's marginal at tick `t` is the push-forward of `μ`'s region-1 marginal by
  `φ₁ᵗ`. A region-2 permutation does not touch that marginal. So no countermodel separates factorization from
  intervention no-signalling across a cut.
- **The conditioned law under HI-rec.** `μ_R(· | R)` is uniform on the rectangle `R`, because `R` lies inside the union
  of the orbits that meet it. A uniform law on a rectangle is a product, and so are its images under `φ₁ × φ₂` at every
  tick.

## 3. Findings

Each finding was pressure-tested against the reading least favourable to the framework.

**L1. Locality of the dynamics is adopted, not derived.**
- *Where it enters.* The tick cone rests on the rule's dependency structure (`Rule.dep`), together with A3 and the
  nearest-neighbour stipulation (Substratum.md:96; SM.md:226). The kernel proves it (`iterate_dependsOnlyOn_ball`,
  RegionTower.lean:283). TC confirms it on `C-chain` with a non-vacuous control.
- *What the OI core sees.* The observer theory consumes nothing of A3–A6 (`obsTheory_rule_independent`,
  SubstratumInterfaceAudit.lean:779). The OI core therefore does not see locality. Locality enters only through the
  spatial constitution.
- *The posit ledger.* Main.md:708's ledger lists seven posits, and A3, the nearest-neighbour range and site
  factorization are not among them. Each is stated as an assumption elsewhere: Substratum.md:96; SM.md:226; SM.md:66–70,
  where the uniqueness of the factorization is a LEDGER **GAP**.
- **Classification:** CONFIRMING. The ledger omission is recorded as a consistency observation for review, and no text
  is changed here.

**L2. Given the spatial constitution, factorization and intervention no-signalling across an uncoupled cut follow for
every hidden prior.**
- *Derived.* FAC and INS hold exhaustively, with W1 and W2 as the written arguments. P0's no-signalling (`NS`, P0 RESULT
  §1) is therefore OI-derived on uncoupled cuts, once the cut is a cut of the rule.
- *Coupled cuts.* There, no-signalling holds below the graph distance (TC) and fails at it.
- **Classification:** POSITIVE. It validates the inheritance P0's F4 relies on, for `|A| = 1`-type exclusions across a
  rule cut.

**L3. Hidden-sector independence, `SL-U`'s surplus at `|A| ≥ 2` (P0 F5), is a property of the ensemble reading, not of
the dynamics.**
- *Where it holds.* It holds under the counting measure, which is Lemma 3's default (Main.md:60). It also holds under
  Lemma 3's maximal-entropy selection conditioned on regional records (HI-default, HI-rec).
- *Where it fails.* Two readings that the corpus also admits break it:
  - **The actual-orbit law** (Main.md:62: "on the orbit of the actual microstate, the uniform measure is the unique
    φ-invariant measure"). It is a product iff the regional periods are coprime (W4, exhaustive on FAM). Identical
    uncoupled copies with period above 1 are always correlated (W6).
  - **Structured realization priors** (Main.md:60: "a realization … carries its own fixed hidden prior μ_H").
- *No-signalling is unaffected.* In both failing cases INS still holds. The correlation is visible as correlated
  one-step kernels and selection dependence. This is the `𝒪₀`-level counterpart of P0's `Ucv`, realized here by a
  deterministic finite-range substratum with uncoupled parts.
- **The answer to P0's sourcing obligation (ii).** The product hidden sector is supplied by OI's default measure and by
  record-conditioned maximal entropy. It is not supplied by the actual-orbit reading or by structured priors. Which of
  these OI's statistics are is an interpretive choice that Lemma 3's text leaves open:
  - an ensemble over orbits selected by maximal entropy, or
  - frequencies along the one actual orbit.
- **Classification:** NEW.
- **Assumption-watch marker.** A claim that uses product hidden statistics across uncoupled subsystems is conditional on
  the counting or maximal-entropy reading of Lemma 3. It fails under the actual-orbit reading whenever the subsystems'
  periods share a factor.

**L4. The maximal-entropy invariant law compatible with registered records is itself correlated across an uncoupled
cut.**
- *The measurement.* This is the supplementary count above.
- *What it means.* Independence is a property of the predictive, record-conditioned law, not of the selected invariant
  law. A claim stated for "the selected measure" without conditioning would be false at every tested record.
- **Classification:** ELABORATING on L3.

**L5. Sub-tick locality is independent of tick-level locality.** This study did not compute it. The corpus already
records it:
- F2-1 RESULT.md:304–315, where two uncoupled sites interact at sub-period times under the composite logarithm [X];
- ROADMAP.md:1522, "Executable intermediate layer flow" **INDEPENDENT**.

Any continuous extension that requires a sub-tick cone adds a principle beyond the tick cone.
- **Classification:** CONFIRMING, by citation.

## 4. Separations, collected

| separation | witness | evidence |
| --- | --- | --- |
| factorization and INS, but not hidden-sector independence (so not `SL-U` at the visible-law level) | `U-free(3)`, E-orb on a joint orbit of two period-4 sites; E-pri | [X] |
| tick cone, but not factorization | `C-cut` (one crossing edge): signalling at `t = 1` | [X] |
| INS below the graph distance; signalling at it | `C-chain`, distance 5 | [X] with [K] |
| tick cone, but not the sub-tick cone | F2-1's uncoupled pair under the composite logarithm | [X], corpus |
| factorization without INS | impossible across a rule cut, for every prior (W2) | [W] |

## 5. What this answers, and what remains open

**The central question.** Can locality be derived from OI's existing principles, or must it be introduced?

- **Locality of the dynamics** is introduced, as part of the spatial constitution (A3, nearest-neighbour range, site
  factorization). It is not derived from Axioms 1–2 or C1–C4 (L1).
- **Factorization and intervention no-signalling** across an uncoupled cut are derived from that constitution, for
  every prior (L2).
- **Hidden-sector independence**, and with it `SL-U` beyond no-signalling, is derived under the counting or
  record-conditioned maximal-entropy reading of Lemma 3. It is independent of the dynamics and fails under the
  actual-orbit and structured-prior readings (L3, L4).
- **The sub-tick cone** must be added to any continuous extension (L5).

**Open.**
- **Obligation (i), the decomposition.** Here the visible datum of each region was fixed as that region's current
  components. A visible map that does not respect the rule cut was not tested.
- **Obligation (iii), the uncoupled premise.** The dependency test reads the rule at configuration level, which the
  observer does not see. When `Γ` is a product, `𝒪₀` still cannot check the premise (P0 F1).
- **Obligation (iv), the carriers.** Untouched. The relation of these visible laws to P0's pure-anchor dilation
  carriers `𝒪₁`–`𝒪₃` is stated, not tested.
- **The size of the actual-orbit correlation** for observer-scale periods is not measured. Main.md:62 places short
  orbits outside every theorem's scope; whether coprimality fails generically among long periods, and with what visible
  strength, is open.
- **Coupled cuts beyond the cone, and Bell preparations.** Main.md:392 and SM.md:110 allow preparation-indexed non-local
  edges, and H-Bell is open.

**Non-claims.**
- No locality principle or ensemble reading is adopted.
- Nothing says which reading of Lemma 3 is correct, or whether nature satisfies `SL-U`.
- The results are exact on the frozen finite configurations. W1–W6 are written arguments that the configurations check,
  not kernel proofs.
- Correctness bands are unchanged; this is on the consistency axis (§A.23).
