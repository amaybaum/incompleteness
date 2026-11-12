# Focused re-check of OA-1 r2 (`OA-1-REPORT-r2.md`)

**Reviewer standing.** The same independent reviewer as `REVIEW-OA-1.md`. Read-only and paper-only, with sources at
`fb733b4a` and TUNE-1 at `d47a6377`. No computation on any OI rule and no commits, pushes or GitHub writes. r1
(`OA-1-REPORT.md`, mtime 17:00:43) is unchanged.
- The derivations marked **[W-rev]** below are my own paper checks. They are unreviewed and are offered for OA-1 to
  adopt or refute, not as results.

## Verdict: REVISE (one bounded revision)

r2 applies findings 1–8 accurately, with four residual defects. The owner's two new points expose a conflation that
r1 and r2 share and my first review missed:
- **N1, as defined, tests correlation between a held record and the carrier ("knowing"), not selectable
  preparation.**

Fixing it changes the meaning of gap 1 but not its classical character. The required changes are R1–R7 (§5). None
reverses a verdict on N2, R4 or MP-2.

***

## 1. Findings 1–8: application check

| Finding | Applied? | Residual |
|---|---|---|
| C1-a measure scope | yes (§1, D2 scope, N1.1a/b, §0.3, §5, §10) | **R2**: μ-G and μ-R are typed inconsistently (§3 below) |
| C1-b hidden carrier | yes (N1.1a, D3, §0.3) | superseded by R1 (selectable preparation) |
| C1-c novelty | yes (D2 relation, §6, §7) | — |
| 2 MP-0 split | yes (N1.2, §5) | nit: MP-0a's "why not supplied: under μ-G, D2 rules it out" (:469). D2 does not rule out H-LOW; μ-G is simply not that law, and ready cells under μ-G cost D3 |
| 3 D5 / G_SM / D7 | yes (D5 scope and status; N2.2; :510–511 verified) | **R4**: the "every measure" justification (§4 below) |
| 4 R4 / D6 / Fin 2 / branches | yes (D6, R4, §0.5, the tables) | nit: §5 item 3 should add that R3 under the configuration identification inherits R4's ceiling, being a sub-theory by D6 |
| 5 MP-2 credit / scope | yes (§3 MP-2; citations verified: mathcon1 :584–587, MECH-2 :64–71, :104–118, ARP-1-MARC :36–38) | **R6**: the routes list (§5 below) |
| 6 5c / 5e | yes | — |
| 7 D4 | partly | **R5**: D4(b) extends Main:147 beyond μ-G; the partial-record content was dropped (§2.2 below) |
| 8 trace row | yes | — |

***

## 2. The owner's two points

### 2.1 Knowing versus preparing (owner example: the swap `(V, H) → (H, V)`)

**Where the memory of `V_t` lives.** Under μ-G, D2 makes `V_{t+1} ⊥ H_{t+1}`.
- In the swap, the remembered bit `V_t` *is* `H_{t+1}`. It cannot also sit in `V_{t+1}`.
- A larger observer does not help. By D2 applied to the enlarged `V`, no function of the present configuration
  determines or biases `H_{t+1}`.
- Copying `V_t` into another visible cell needs a blank cell. Under μ-G cells are not blank, so a CNOT into a uniform
  cell yields a one-time pad.

So under μ-G the memory is physically either in the hidden sector itself or outside the configuration, which is
MP-0b (H-MEM, the law-level conditioning on `X_{<t}`). The owner's example therefore does not contradict D2. It is
exactly the case D2 assigns to MP-0b.
- **Per-orbit measure μ-O.** The swap's orbits are `{00}`, `{11}` and `{01, 10}`. On the 2-cycle, `V_{t+1}` determines
  `H_{t+1} = 1 − V_{t+1}`. So under μ-O the observer knows the hidden bit from its *present* configuration, with no
  memory at all.
- **Record-compatible measure μ-R.** Once the records exclude the fixed points, μ-R gives the same result. Under μ-O
  and μ-R, "knowing" can be native. r2 already marks this as open (N1.1b); the swap shows it is not vacuous.

**Knowing is not preparing.** r2's N1 row (:115) requires a record event `E` and a carrier `Σ` whose conditional law
`ν_E` differs from its unconditional law, with `E` still held when `Σ` is used. That is heralded correlation: what
the observer *knows* about `Σ`. Nothing in N1 asks the observer to *select* which state is prepared.
- §0.3 and §5 item 1 then read the failure as "no hidden carrier can be prepared", which conflates the two.
- The qubit tier's T-P (an ε-net of preparations) assumes selectability, but the infrastructure tier does not test
  it.

**Selectable preparation, evaluated [W-rev].**
- **The definition needed.** Call it N1-S. A setting `s` whose law is independent of the carrier (ledger (xiv)) is
  chosen and recorded. For at least two values of `s`, the carrier's law at use time, conditional on everything the
  observer holds there (`s` included), differs. Heralds are allowed and failures are recorded.
- **Dynamical selection is native under affine rules.** A cell permutation is linear. `(s, Σ) ↦ (Σ, s)` writes the
  chosen value into a hidden `Σ` exactly. A translation `Σ ↦ Σ + s` selects too, but only if `Σ` starts at a known
  value.
- **Retaining the choice together with the selected carrier fails under μ-G, for every bijection.**
  - If `s` is still held in `V_{t′}` at use time, then by D2 `Σ_{t′} ⊥ s` given everything held, so the carrier's held
    conditional law does not depend on the choice.
  - Later outcomes can depend on `s` only through visible cells.
  - Operationally, the hidden carrier carries no selected state relative to the observer's records.
- **Diagnosis.** This is the blank-memory cost (D3; MP-0a), not a missing selection mechanism in the rule. MP-0a
  (blank copy cells) resolves it classically, and so does MP-0b. Under μ-O and μ-R, N1-S also needs (xiv) to hold on
  the actual orbit or orbit union, where cells are correlated. Open.

**Verdict on point 1.**
- r2 does **not** keep "cannot know the hidden state" apart from "cannot prepare a selected state". **Required (R1):**
  split N1 into N1-K (held correlation) and N1-S (selectable, as above), and evaluate each.
- Under μ-G, both fail for hidden carriers and every bijection. N1-S's failure is a failure to retain the record, not
  a dynamical one: selection itself is native under affine rules. MP-0a or MP-0b resolves it classically.
- Under μ-O and μ-R, N1-K can hold natively (the swap). N1-S is open.
- "Uniformity alone cannot give a preparation no-go" is correct. D2's no-go needs uniformity **and** the definition
  "held = a function of the present `V`". Say this explicitly in N1.

### 2.2 Complete history and hidden memory

- **D4 is not bookkeeping.** D4 does not define the observer's state as its history. Its premise is that the
  *physical* visible configuration determines its predecessor, `V_{t−1} = g(V_t)`.
  - Under μ-G that forces `T` to be a permutation and, by Main:147, `φ(x, h) = (φ_V(x), σ_x(h))`: no hidden influence
    on `V` at all.
  - That is a physical constraint on which records can coexist with hidden influence. It is not a claim that hidden
    memory disappeared.
  - r2 states the demotion in those terms (D4(a)–(c), :158–167). ✓
- **Overreach (R5).** D4's header and (b) also cover "any stationary law" (:157) and invoke Main:147 there. Main:147's
  `T` is the uniform-prior kernel (Main:88, :129: "under the uniform hidden prior that defines `T`").
  - Under another stationary law, (a) gives only a deterministic visible process on the support. (C1) and (C4) fail
    *for that law*, but `φ` need not be visibly autonomous.
  - Restrict (b) to μ-G and restate the stationary case as "deterministic on the support". The R1 bullet (:239) and
    the N4 bullet (:336) need the same edit.
- **The owner's physical test, and what r2 dropped [W-rev].** The test asks whether two histories with the same
  current readout predict different futures, which can be checked when the observer keeps both. Write `V = (Y, R)`,
  with readout `Y` and record cells `R`, where `R_t` faithfully holds `Y_{t−k..t−1}`.
  - Suppose `R` is **inert** for the readout update, `Y_{t+1} = f(Y_t, H_t)`, as a good record is. Under μ-G,
    `H_t ⊥ (Y_t, R_t)` (D2), so `I(Y_{t−k..t−1}; Y_{t+1} | Y_t) = 0`.
  - Hence the observer measures **zero** memory at every order its records cover. Hidden readback appears only
    beyond the record window, carried by the history the window has dropped (Main:97).
  - Example: `(y, r, h) ↦ (h, y, r)` is a bijection with faithful window-1 records and `y_{t+1} = y_{t−2}`. The memory
    sits at order 2. Widening the window moves it to order 3.
  - If `R` is not inert, any history dependence the observer sees is mediated by visible cells, not by hidden memory.

  This is the physical, non-bookkeeping form of r1's "records versus readback" candidate. It needs no completeness,
  holds under μ-G only, and dissolves under MP-0a (non-stationary) or μ-O/μ-R (D2 fails). r2's "D4 does not cover
  partial records" (:168) follows my first review and undersells this.
  - **Recommended (R5′):** add it as a [W] item (classification ELABORATING of Main:97; status: candidate,
    unreviewed) and run the owner's test in it.
- **AW-OA1-1** (:528–531) is a check marker and claims no more than allowed. Scope it to `X = V`, Main's convention.
  With a coarser readout `Y` and records held in `R ⊂ V`, the observer does hold the history, and the item above
  applies.

**Verdict on point 2.** r2 does not equate history-as-state with the absence of hidden memory, and its D4 demotion
via Main:147 is correct under μ-G. The extension to "any stationary law" must be corrected (R5). The owner's
same-present / different-future test is not run in r2, and under μ-G it gives a stronger, physical result (R5′).

***

## 3. Pressure test: MP-0's split

- **MP-0a (H-LOW) is a resource.** Its admissible form (:466–467) is target-neutral and passes the non-import test. ✓
- **MP-0b (H-MEM) is an interface convention.** R4's `FiniteOperationalTheory` keeps outcome labels outside the
  carrier, so R4 grants it. ✓ The swap analysis (§2.1) confirms MP-0b is exactly where the owner's remembered `V_t`
  lives under μ-G.
- **Typing defect (R2).** r2 counts all three measures as native inputs (§1, :84–101). Yet N1.1b reads μ-R "as a posit,
  not as native supply" (:271–273), while μ-G is treated as native. Main makes the global counting measure itself a
  selection principle: "a selection principle, not uniqueness from invariance alone" (Main:54). Ledger item (iv)
  posits maximal entropy "compatible with the observer's records" (Main:724), and μ-G is the case of (iv) in which
  the records exclude no orbit. Only μ-O is derived (Main:54, :60). Fixes:
  - type μ-G and μ-R alike (both rest on (iv)) and μ-O as derived;
  - say the N1 native failure holds "under the posited global selection μ-G".
- **What the split shows.** Both branches are classical. Neither carries quantum content: MP-0a supplies blanks, MP-0b
  relocates records. ✓

## 4. Pressure test: "N2 holds under every measure"

- **True, for the right reason.** D5 is a statement about the map. `Φ^τ` is affine, so the carrier's linear part and
  the functionals the records read do not depend on `c`, *for every state*. No measure enters at all.
- **The justification is misstated.** D5's last bullet says parts (i)–(ii) "need only that the setting's law is
  independent of the rest" (:181–182). That wording came from my first review and is imprecise. Independence (xiv) is
  not used by (i)–(ii). It matters only for the *operational* reading.
  - Under μ-O and μ-R, cells on an orbit are correlated, so (xiv) can fail for the actual setting cells.
  - Then the record law conditional on `c` can change beyond a translation through `c`–`u` correlation. That is
    preparation correlation (D7), not control, and N2 excludes it through (xiv).
- **Required (R4):** state that N2's failure is measure-free as a property of `φ^τ`. Under μ-O and μ-R, (xiv) is a
  posit that may fail on the actual orbit, and any setting effect that remains is correlation, not control.
- **§5 item 2 wording.** "N2 is the earliest failure under every measure" (:321, :458) reads as if N2 were earliest
  under each measure. Under μ-G, N1 comes earlier. Write "the earliest failure that holds under every measure".

## 5. Pressure test: the routes listed under MP-2

The list (:390–392) is correctly scoped as open, and every citation is verified. Required precisions (R6):
- "Over native `Z`/`X` reads … NC does not apply" is not an escape route. It marks undecided ground: MECH-2 records A6
  as "undecided" at the native read level (:107–108). Say "NC's hypotheses are not met; contextuality there is
  undecided".
- mathcon1 Shape 2 (a changed identification under which P★-type conditioning is CP) overlaps R5 rows 5b and 5c.
- Shape 3 (B1's coherent-mixing template with a phase-congruent readout quotient, :587) overlaps 5e, and mathcon1
  counts E-real, E-pair and isolation against it.
- Cross-reference both shapes to their R5 rows, so that a route is not listed as open in one place and imported in
  another.
- Shape 0 (:584) is mathcon1's own preregistration routes, not an observer-interface escape. Its omission is correct.
- **Necessity (R7).** The 5d row says the escape "would need (i) … M-INACC and (ii) an unbounded carrier". M-INACC is
  necessary only within NC's hypotheses (injectivity, H-LIFT, spanning reads). Carrier growth is necessary for exact
  reproduction by Main:558 [P, half imported], and at fixed ε for TUNE-1's bounded-`|C_n|` family classes [W]. State
  both as **possible ingredients**, necessary only within those hypotheses, with sufficiency open. MP-2's "on an
  unbounded carrier" (:379–380, :493) should read "on growing carriers" to match 5d.

***

## 6. The three gaps, each on its own target

| Gap | Target | What r2 supports (with R1–R7) | Layer | Verdict |
|---|---|---|---|---|
| **1. Preparation** | a genuine inability to make selectable preparations, not just an absence of correlation | Under μ-G: for hidden carriers and every bijection, a selection cannot be retained alongside the selected carrier (D2 applied to N1-S). Writing the chosen value is native under affine rules. The failure is the blank-memory cost and is resolved classically by MP-0a or MP-0b. Under μ-O and μ-R: N1-K can be native (swap); N1-S is open. | paper [W] on [P] Main:54/58 | **Classical gap, measure-relative.** The no-go needs μ-G *and* "held = function of present `V`". r2 must restate N1 accordingly (R1). |
| **2. Classical control** | a restriction of the actual affine rule and its admissible apparatus, not of all deterministic systems | D5/D7: under one affine `φ` acting on every cell, apparatus included, a setting acts only by translation. The verdict is measure-free as a map property. Fredkin-type bijections supply control (§4.1), so the restriction is specific to the affine class that Main derives from gauge invariance. Lifting it is a Layer-0 revision (MP-1). | paper [R]+[W]; one proof re-derived twice | **Classical gap of the actual rule, correctly scoped**, after R4. |
| **3. Quantum operations** | a sourced operation beyond the configuration-level ceiling, without assumed quantum structure | Configuration identification: capped for every rule [K]: no phases and not `DerivedOI` on any carrier, no dense control on `Fin 2`. Rule-derived interfaces stay inside (D6, [W] on [K]). Encoded frames: capped by frame-relative paper results (U2 under R1, Proposition C, eight-sign 1/15). Emergent amplitudes: imported. 5d with M-INACC: not constructed, open. | [K] for configuration level; [R] for encoded frames; [O] for 5d | **Remains open. Not shown impossible.** |

**The owner's key test.** Can gaps 1–2 be resolved entirely classically while gap 3 remains? **Yes, OA-1 r2
supports this, at paper level, with these qualifiers:**
- Gap 1 is resolved by a classical resource (MP-0a) or a classical convention (MP-0b), shared by a reversible
  computer (§4.1).
- Gap 2 is resolved by a classical non-affine switch, which for OI means giving up the gauge-derived affine form (a
  Layer-0 revision under §A.29).
- The classical control `𝔖_F` with MP-0a passes N1–N4 [W] and still fails the qubit tier under the configuration
  identification [K]. It passes the qubit tier only with a supplied access restriction, which the non-import test
  catches.

"Gap 3 remains" means no route on `main` closes it; it does not mean an impossibility. M-INACC and growing carriers
are **possible ingredients only**. Their necessity holds only within the stated hypotheses (NC; Main:558 [P, half
imported]; TUNE-1 FAIL-CLASS [W]), and sufficiency is not established.

***

## 7. Required changes for r3

- **R1.** Split N1 into N1-K and N1-S as in §2.1 and evaluate both. State that the μ-G no-go needs "held = function
  of present `V`", that selection is native under affine rules, and that the N1-S failure is a retention (blank
  memory) failure resolved classically by MP-0a or MP-0b. Propagate to §0.3, N1.1a, §4.1 row 1, §5 item 1, §6 and
  §11.
- **R2.** Type μ-G and μ-R alike (both rest on ledger (iv); Main:54 calls the global selection a selection principle)
  and μ-O as derived. Reconcile §1's "native" with N1.1b.
- **R3 (nits).** MP-0a's "D2 rules it out" (:469) → "μ-G is not that law; ready cells under μ-G cost D3". In §5 item
  3, add that R3 under the configuration identification inherits R4's ceiling.
- **R4.** Say that N2's failure is measure-free as a property of `φ^τ`; (xiv) is used only for the operational reading
  and may fail under μ-O and μ-R, where a residual setting effect is correlation (D7), not control. Reword "earliest
  failure under every measure" (:321, :458) as "the earliest failure that holds under every measure".
- **R5.** Restrict D4(b)'s Main:147 step to μ-G (Main:88, :129). Under any other stationary law, only "deterministic
  on the support". Edit :155–171, :239, :336 and :607.
- **R5′ (recommended).** Add the partial-window form (§2.2) as an unreviewed [W] candidate. Under μ-G, inert faithful
  window-`k` records give zero observed memory at orders ≤ `k`. Run the owner's same-present / different-future test
  in it, and scope AW-OA1-1 to `X = V`.
- **R6.** Reword the MP-2 routes: the native `Z`/`X` case is "undecided", not an escape route; cross-reference
  mathcon1 Shapes 2 and 3 to R5 rows 5b/5c and 5e.
- **R7.** State M-INACC and growing carriers as possible ingredients, necessary only within NC's hypotheses, Main:558
  [half imported] and TUNE-1 FAIL-CLASS [W], with sufficiency open. Use "growing carriers" in MP-2.
