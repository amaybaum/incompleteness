# Independent re-review: EOI gate draft r3 for #1169

**Reviewed:** `GATE-DRAFT.md` r3, sha256 `7fdef7a992ddd618656a13ba911a818a03254859a4c7b20328bf6b28193ce929` (250 lines).
It was diffed against r2 (`4b85c936…ffcf5b`). `L n` below is line `n` of r3.

**Owner text:** checked against `scratchpad/eoi-audit/BRIEF-P2.md`, sha256 `5d713b78…62aa3e`, lines 44–53.

**Sources:** as before, at the same pins.

**Mode:** read-only.

## Verdict: ACCEPT WITH CHANGES

r3 closes R2-B3. It applies R2-N1 to R2-N10 correctly. Each new citation and each quotation is accurate.

Two rules added to close R2-B1 and R2-B2 each still leave a hole, which R3-B1 and R3-B2 below describe. Both holes are
in a single sentence. The exact replacement text is given below, so applying it verbatim needs only a diff check, not
another review. Until those sentences are changed, R3-B1 and R3-B2 are blocking.

## 1. Status of the r2 blocking findings

| r2 | Status in r3 |
|---|---|
| R2-B1 | **Closed in principle, one hole (R3-B1).** A particular `μ_H` is now a departure (L69). This matches Main:56 ("a selection principle") and Main:60 ("realization datum"; "default, not a constraint"), and the owner's question 2. The escape condition, "shown for every `μ_H` in a declared class containing the counting measure and at least one correlated law", can be met trivially and can be declared after the result |
| R2-B2 | **G5 totality closed; one hole in the fixed class (R3-B2).** G5's pass and fail columns (L71) are now total. The MECH-1 row (L142) follows from G5 as written. The certification clause of the imitation class is ambiguous, and one reading produces false passes |
| R2-B3 | **Closed.** K2 (L174–181) rests on the supplied items and the named open inputs, and Theorem NC is no longer used as a reason. It is stated as "a finding about the present record", which is the right strength. See R3-N1 for one completeness point |

## 2. Findings

### Blocking until the given text is applied

**R3-B1. The prior-class escape is trivially satisfiable and can be chosen after the result.** L69, L176–177.

The pass condition for a hidden-prior assumption is "the item is shown for every `μ_H` in a declared class containing
the counting measure and at least one correlated law". This has two problems.
- *Trivial witness.* A record can add one correlated law whose correlation lies outside every dependency cone the
  protocol reaches, or between cells that the conclusion never reads. The proof then goes through unchanged, while it
  still uses product sources wherever the result depends on them. That reopens R2-B1.
- *Post hoc.* "Declared" does not say when the class is declared. A class chosen after the result is a variant
  adjusted to the outcome (§A.29).

R-I3 also names non-uniform priors ("correlated (non-uniform / non-independent)", BRIEF-P2:47), and the class
requires only a correlated one.

*Replacement for the G3 pass-column clause:*

> "a hidden-prior assumption only if the item is shown for every `μ_H` in a prior class fixed in the preregistration
> that contains the counting measure and, for each restriction on `μ_H` that the proof uses at a named step (G0's
> dependency trace), a law violating that restriction inside the protocol's dependency cone; the item's scope names
> the class"

Make the matching change in K2 (L176–177): "shown for a preregistered prior class as in G3".

**R3-B2. Which operational equivalences certify the imitation class is ambiguous, and one reading gives false
passes.** L71, L73–78.

"With operational equivalences certified by spanning reads or a tomographically complete witness" can be read in two
ways.
1. *Spanning of the encoded operator space.* This is M2D's meaning: "reachable preparations span the operator space
   and the reachable reads span its dual" (M2D:488–490), in R1 or R-W.
   - This certification is defined through the comparator's frame. It is test-only under the role test, so no
     quantum structure enters as an ingredient.
   - But it makes the verdict depend on the frame, which ties G5 to §6(d).
   - When reads do not span, the class is not certified, the question is "undecided", and a claim beyond the fragment
     fails. That holds for every construction whose nonclassicality rests on reads that are physically inaccessible.
     This is the route the owner names: "Hidden information can influence physical dynamics without being accessible
     to the embedded observer" (BRIEF-P2:51). Under this reading the gate closes it in every case.
2. *Statistical equivalence over the construction's accessible reads.* This reading is operational, with no frame and
   no leakage. But with restricted reads a classical model can appear contextual: "a law on two bits read only one bit
   at a time generates the square state space, a gbit" (M2D:521–527).
   - The noncontextual imitation then fails.
   - G5 passes an item claimed beyond the fragment, for a construction that is classical with restricted access. That
     is a false pass.
   - M2D:528–529 states the guard: "Such apparent contextuality is not a nonclassicality witness unless the missing
     reads are absent for a physical reason."

*Replacement for the certification clause in L73–75:*

> "operational equivalences are statistical equivalences over the construction's accessible preparations,
> transformations and reads. Where the accessible reads do not span the configuration-level read space (M2D:488–490,
> 521–527), a failed imitation counts toward G5 only with a proof that the missing reads are physically absent in the
> stated class and dynamics (M2D:528–529); otherwise the question is undecided. A comparator frame used to state
> spanning is test-only"

The rule then stays operational and frame-free, closes the gbit false pass, and keeps open the owner's route for
inaccessible hidden information, subject to proof. This follows the owner's symmetry: neither a limitation of the
interface nor a rescue by hidden memory is assumed.

### Non-blocking

**R3-N1. K2's list does not cover all seven units.** L178–180.
- The cited supplied items cover P-OBS, MECH-1, MECH-2 and M-INACC. MC1, P-CONTROL and P-MIX are not covered.
- *Fix:* add that MC1 is capped by A-2 (MC1:170), P-CONTROL's L-3 to L-6 are supplied (PCD:410–413), and P-MIX's
  coefficient loading, record cell and schedule are supplied (PMD:363–367). Alternatively, note that only MECH-1 has a
  positive result, while the other units are EOI-NEG or reachable set only (L136–143).

**R3-N2. Measurement independence is both a pass example and caught by the departure wording.** L69.
- Main:407 calls (iv) "a posit about the initial condition". It is therefore literally an assumption that restricts
  the joint law of settings and hidden state, which the departure column catches ("every assumption that only
  restricts it").
- r2's review allowed (iv) on the pass side because it is framework-wide (Main:406–407), whereas `μ_H` is per
  realization (Main:60). The text should state that distinction.
- *Fix:* "other than a hidden prior; a posit Main states for every realization, such as (iv), is a framework posit,
  not a hidden prior".

**R3-N2a. One owner statement is not represented.** BRIEF-P2:51 now carries a later owner statement: "A proof that
excludes such memory is valid only within that restricted model; it cannot automatically establish a limitation of OI
generally." The gate does not cite it. It is the direct source for G0's *restricted* label (L90). *Fix:* cite it there,
with the same relay caveat as L24.

**R3-N3. G2's pass column no longer mentions the schedule.** L68.
- G2's pass reads "records and known preparation information". A decision that reads the clock or schedule is
  therefore not covered on the information axis.
- G4 covers the schedule's *source*, but not reading it.
- *Fix:* "records, known preparation information and the schedule".

## 3. Quotations

Each was checked against BRIEF-P2 (lines 48, 52, 53) and is **verbatim**:
- the "main risk" passage;
- the two three-question passages ("What is proved only under …"; "What genuinely emerges from OI alone? …");
- R-I4 ("Separate representation from mechanism. …").

The attribution "verbatim as relayed" together with "to be quoted from its #1169 record … before posting" (L24–25) is
the correct standing.

Principle 2 now uses the owner's terms (BRIEF.md:16–18), with the operationalization stated separately (L51–53).
R-I1, R-I2 and R-I3 are faithful. Act 45 is now under G3's memory items, with the scope of the kernel verdict (A45:5).

## 4. Citations (new or changed in r3)

These were checked against the source and are accurate:
- Main:56 ("a selection principle"), Main:60 ("realization datum"), Main:406–410;
- A45:5 (trivial-ancilla dilations, uniform initial law) and A45:38–39;
- MID:309–311, 417, 607;
- M2D:250, 485–498, 762;
- M1D:356, 900.

All §8 line references (L24, 51, 58, 67, 69, 71, 73, 83, 88, 102, 138–143, 146, 174, 213, 232) point to the stated
changes. The §7 change for c.6714136234 (L232) is correct.

## 5. R2-N dispositions

All are adequate, namely N1 to N10. N5 is filled where the records allow ("not stated by the record" for M-INACC and
MECH-2; "census" and "definition-level" for P-CONTROL and P-OBS).

## 6. Authority

Unchanged and adequate. The alternative-prior check stays "a planning item" (L69). That is consistent with the owner's
later statement that "no manuscript corrections or new scientific investigations are authorized until the reconciled
findings are reviewed" (BRIEF-P2:51).
