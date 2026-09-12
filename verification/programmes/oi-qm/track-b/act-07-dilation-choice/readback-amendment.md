# Track B act 7 — the READBACK AMENDMENT (append-only control plane)

**This is the append-only amendment act 7's `T3` requires by name, and it is control plane only.** It
fixes the exact map carrying a candidate on the dilated carrier back to a matrix on `V`, before any
witness or candidate is evaluated. **No `T1`–`T4` execution, no witness B, no dilation construction,
no candidate comparison, no Lean.**

**What it discharges.** Act 7's `T3` routes a negative `D4b` to three steps: record the finding,
write and merge an append-only control-plane amendment specifying the exact readback map, and only
then resume layer 2 at reduced strength. Step 1 is done — the resumption result records it. **This
file is step 2.** Step 3 waits on this file being merged.

**Governing documents, all unchanged by this one:**

| Document | Blob |
| --- | --- |
| Act 7's preregistration (governs in full) | `810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19` |
| Act 7's resumption control plane | `3bb88717267a4adb45125b6277edae4e56c5cf26` |
| Act 7's resumption result (`D4a+`/`D4b−`) | `216cb9e65cda9b2f3b9777c2ecfcdf8d8bb58df0` |

**Start state.** Merged `main` at `587d5c048d364360c62550f56d188c5814e3d5d1`.

## The frozen map

**`T3` is this one rule and no other.** Let `A` be the ancilla configuration set of an admissible
dilation, let `a₀ ∈ A` be that dilation's **distinguished ancilla input configuration** (fixed as part
of its datum — see below), and let `M` be a candidate matrix on the dilated carrier `V × A`, written
in **Source A's external (column-stochastic) orientation**. Then

    R_{a₀}(M)_{i j}  =  ∑_{a ∈ A}  M_{(i, a), (j, a₀)}

**In words: hold the INPUT ancilla at its frozen preparation `a₀`, and sum over the OUTPUT ancilla.**

**This is the direct extension of the only readback Source A supplies.** §3.4 p. 10 states

> `Γ_ij(t ← 0) = ∑_{i′=1}^{N′} Γ̃_{(i,i′)(j,j′)}(t ← 0)`

— sum over the output ancilla index `i′`, input ancilla held at `j′`. `R_{a₀}` is that same rule with
`a = i′` and `a₀ = j′`, applied at conditioning times other than `0`. **The shape is the source's;
extending it off the root is ours**, and the resumption result established that the source supplies no
such extension (its readback exists at `t′ = 0` and nowhere else).

### What the map acts on

**`R_{a₀}` acts on the (42)-type stochastic candidate**, `Γ(t ← t′)_{ik} = |U_{ik}(t ← t′)|²` in
Source A's orientation — the object `D4a` established the source forms from the dilated unitary.

**This is an adoption, and act 7 flagged that it would have to be one.** `T3`'s closing line records
that "act 3's reference points are `candidateOf` and act 5's (42) readout; **neither is adopted by
default**." This amendment adopts **act 5's (42) readout** as the object the readback acts on, and
does not adopt `candidateOf`.

**The readback is applied to the stochastic candidate, never to amplitudes and never to the unitary.**
No phase-sensitive operation is introduced anywhere in `T3`. A readback acting on `U` rather than on
`|U|²` would be a different convention with different sensitivity, and it is not this one.

## The anchor `a₀` is part of the dilation datum, not a choice made later

**§3.4's own latitude is the hazard, and it is closed here rather than inherited.** The source's
marginalization holds "**for at least some choices** of the ancilla's configuration `j′` at the initial
time `0`" (p. 10). Reading that as "pick any `j′` that works" would not remove the execution-time
freedom — **it would relocate it into the anchor**, which is exactly the move `T3` exists to prevent.

**So the distinguished `a₀` is a component of the admissible-dilation datum itself.** When a dilation
enters the comparison, its `a₀` is already fixed; it cannot be re-chosen after any candidate, witness
or divergence has been inspected. **Two dilations being compared each carry their own anchor, fixed in
advance.**

**The rooted reproduction condition certifies the anchor.** The datum's `a₀` must be one of §3.4's
reproducing choices: at the root, marginalising the dilated rooted candidate at `a₀` must return the
original rooted candidate. This is a **hypothesis on the datum**, checked before use — not a property
discovered afterwards, and not a condition adjusted to make a result come out.

**This means the round compares ANCHORED dilations, and that is our convention.** Source A does not
canonically select an anchor, and no sentence in this amendment or anywhere downstream may suggest it
does. The convention is why the strength is reduced.

### A budget note, recorded rather than left to be discovered

Act 7's frozen budget has six slots, of which slot 2 is "the dilated-family carrier or datum, **if**
the predicate cannot be stated without one". **Making `a₀` part of the datum makes that conditional
slot likely to fire.** That is within the frozen six either way, and **this amendment does not enlarge
the budget** — a seventh definition would still require its own separately frozen amendment.

## What `R_{a₀}` is NOT, and may not become

1. **No renormalization.** The sum is taken as it stands. If a row or column of the result fails to
   normalize, that is a finding about the input, not a licence to rescale.
2. **No postselection.** Nothing is conditioned on an ancilla outcome, and no branch is discarded.
3. **No averaging over anchors.** Not over `a₀`, not over a distribution on `A`, not over
   "the reproducing choices". One anchor, fixed in the datum.
4. **No §3.7 factorization.** The tensor factorization (46) p. 17 and the idealized correlation (45)
   p. 17 are **not** imported. The resumption result established that §3.7's readback consumes them
   and that Source A states neither of a generic Stinespring dilation; importing them here would be
   constructing on the source's behalf, which acts 4 and 7 declined.
5. **No phase-sensitive operation**, per the previous section.
6. **No family, and no quantification over readbacks.** See below.
7. **No alternative convention introduced during layer 2**, whether before, during or after a result
   is in view.

## One map, not a family — and why

**The "stated family of readbacks, comparison quantified over it" option is rejected for this round.**

Act 7's `T3` states that "**the readback is outcome-bearing** — different restriction or
marginalization conventions can create or erase a visible divergence". That is precisely why it
demands an exact map. **Quantifying over a family would introduce propositions that are not in the
frozen `DC1`/`DC3`/`DC4` taxonomy at all** — "all maps agree", "some map diverges", "for every
anchor", "for some anchor" — each of which is a different claim with a different quantifier, none
frozen, and each reachable by a different accident of which family was written down.

**A family would also re-open at the meta level exactly what the anchor rule closes**: the freedom to
select, after seeing a result, which member of the family the result is reported under.

**The robustness question is real, and it is deferred rather than dismissed.** Whether a layer-2
finding survives a class of reasonable readbacks is a genuine and worthwhile question — it would tell
us whether the result is an artifact of this convention. **It is a separate later round with its own
freeze**, run *after* the main layer-2 result, so that it cannot contaminate the preregistered
dilation-choice test by supplying an alternative convention while a result is in view. **It is not a
second branch inside the present layer-2 execution**, and this amendment does not preregister it.

## The structural controls layer 2 must prove

These are cheap, and they are required **because** they are cheap: a readback that failed any of them
would be the wrong object to compare candidates with, and that should be caught by proof rather than
by inspection. Each is stated here so it cannot be weakened later. **None is proved in this file.**

| # | Proposition |
| --- | --- |
| **`R-1` orientation and stochasticity** | If `M` is column-stochastic on `V × A` in Source A's orientation, then `R_{a₀}(M)` is column-stochastic on `V`: non-negativity is entrywise, and `∑_i R_{a₀}(M)_{ij} = ∑_{(i,a)} M_{(i,a),(j,a₀)} = 1`. Act 2's `RT1` is what licenses moving between orientations and is consumed, never re-proved. |
| **`R-2` agreement with §3.4 at the root** | Under the rooted reproduction hypothesis on the datum, `R_{a₀}` applied to the dilated **rooted** candidate returns the original rooted candidate — so the frozen map **agrees with the source's own readback wherever the source has one**, and departs from it only where the source supplies nothing. |
| **`R-3` equivariance under ancilla relabelling** | For a bijection `σ : A → A′` and `M′` the relabelling of `M` along `σ`, `R_{σ(a₀)}(M′) = R_{a₀}(M)`. **The anchor is carried along with the relabelling**; this says the map depends on the ancilla structure and not on the names, and it is the sense in which `R_{a₀}` is not an artifact of labelling. It does **not** say the map is independent of *which* configuration is anchored, and may not be read that way. |

**`R-2` is the load-bearing one for provenance.** It is what makes `R_{a₀}` an extension of Source A's
rule rather than a new observable: the two coincide at the root, and the only place they differ is
where the source is silent.

## Provenance and strength — carried on every downstream label

**This map is OURS, not Source A's.** The resumption result established `D4b` negative: the source
supplies no general readback. Act 7's `T3` therefore bounds every layer-2 label reached under this
amendment, and the bound is restated here so no later document has to reconstruct it:

- **`DC3`/`DC4`** would state invariance **under the frozen readback `R_{a₀}` on anchored dilations** —
  never invariance simpliciter, and never invariance of Source A's own visible prediction.
- **`DC1`** would state divergence **under the frozen readback `R_{a₀}` on anchored dilations** — never
  underdetermination of Source A's visible prediction, and never a demonstrated need for a
  candidate-selection principle.
- **A divergence found under `R_{a₀}` could still be an artifact of the map or of the anchoring
  convention** rather than of the dilation freedom. That possibility is not closed by anything here,
  and closing it is what the deferred robustness round would be for.

**All three labels are bounded, not only the negative ones** — act 7's clause, carried verbatim in
force.

## What this amendment does NOT do

- **It assigns no `DC` label** and reaches no outcome. Layer 2 remains **paused** until this file is
  merged.
- **It performs no execution**: no witness B, no `T1`–`T4`, no dilation built, no candidate computed,
  no comparison run, no Lean, no definitions introduced.
- **It does not revise act 7**, whose preregistration governs in full, nor the resumption freeze, nor
  the resumption result. It fills the slot `T3` reserved for it.
- **It does not revise `DC2a`**, which remains correct of the discrete witness it was about; nor
  `D4a`/`D4b`, which are answered; nor act 8's `CE1`, which remains **existential** — one witness, one
  extension, never restated as a classification.
- **It does not close act 7's `D3` gap** — Stinespring's pointwise existence with no coherent regular
  family derived or selected, and no stated link from the visible family's regularity to `Θ`'s or
  `U`'s. That remains **separately OPEN**, and it is **not** what this amendment is about. A frozen
  readback does not supply a coherent dilation family.
- **It adopts no candidate-selection principle**, does not adjudicate act 5's gauge-versus-empirical
  tension, and leaves `F1` versus `F2` undecided.
- **It claims nothing about Source A's applicability or inapplicability**, and nothing about whether
  the correspondence succeeds or fails. A construction that supplies no general readback is a fact
  about its reach; supplying one ourselves is a fact about our convention.
- **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2`, `DC2a` and `CE1` are cited and
  unrevised.** Acts 1 through 6 and act 8 are not reopened.
- **No manuscript edit.**

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are further append-only amendments,
  separately frozen and merged before the work they affect.
- **This PR carries this file alone.** No execution, no Lean, no probe guard, no roadmap edit.
- **Then exactly one layer-2 execution PR**, from the resulting `main`, running act 7's layer 2 at
  **reduced strength** under this map. It carries the `verification/ROADMAP.md` `P0` propagation, for
  act 8's reason: it knows the outcome and sets the row once rather than twice.
- Exact-head review after layer 2 is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head SHA.**

## Non-doings

Do not: run any part of act 7's layer 2 before this file is merged; construct a dilation, a witness B
or a candidate; compare candidates; introduce an alternative readback or a family of readbacks;
average over anchors; postselect; renormalize; import §3.7's (45)/(46); apply the readback to
amplitudes or to a unitary; adopt `candidateOf`; enlarge act 7's six-slot budget; revise `DC2a`,
`D4a`, `D4b` or `CE1`; close `D3`'s gap; adopt or propose a candidate-selection principle; name or
adopt `C5`; compare Source A with Source B or Source C on any axis; edit manuscripts.

## The restraint this amendment exists to enforce

**The observable being compared is fixed before anything is compared.** Act 7 stopped at `DC2a`
cleanly because its layer order was binding; the resumption answered `D4a`/`D4b` before touching a
construction for the same reason. This file continues that order by one more step: the map, then the
comparison — never the comparison, then the map that makes it read well.
