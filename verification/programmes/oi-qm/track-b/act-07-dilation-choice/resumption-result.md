# Track B act 7 — resumption result: the `D4a`/`D4b` adjudication

## Outcome: **`D4a` POSITIVE, `D4b` NEGATIVE → the round PAUSES for the readback amendment**

**No `DC` outcome label is assigned by this adjudication, and none may be inferred.** `DC2b` is
**not reached**, because `D4a` is positive. `DC1`, `DC3` and `DC4` are layer-2 labels and layer 2 is
**paused**, not executed — a different status from both *not reached* and *unresolved*.

**The next artifact is the append-only readback amendment**, written, reviewed and merged **before**
any layer-2 work. That is the routing act 7's frozen stop table fixes for this pair of answers, and
the resumption freeze restated it in advance.

Executed under the resumption control plane, `resumption-preregistration.md` in this directory, blob
`3bb88717267a4adb45125b6277edae4e56c5cf26`, merged by PR #580. From `main` at
`a8f97531eb993feeaa79cc692ca7c3a9fe25d15a`. Act 7's governing preregistration is blob
`810bb2f11d88a0872f764e1e32e2aa2f1e2c9b19`, unchanged.

**Evidence level 3** — a reading of the accepted text. **No Lean, no definitions, no dilation built,
no readback chosen, no witness B, no `T1`–`T4`.**

## The authoritative surface, verified before reading

Source A is *The Stochastic-Quantum Correspondence*, Jacob A. Barandes, **arXiv:2302.10778v3**. The
surface read is the PDF whose p. 1 stamp reads `arXiv:2302.10778v3 [quant-ph] 30 Jul 2025`, 38 pages,
dated June 30, 2025. The arXiv HTML rendering is non-admissible and was not consulted. **Only Source
A was read**; Sources B and C were not consulted and are not compared with it on any axis.

## `D4a` — POSITIVE. The source forms the relative candidate from the dilated unitary

Act 7 asks whether "any equation form[s] the relative operator (39), or any readout of (42)'s shape,
from the **dilated** unitary — on the dilated carrier or anywhere".

**It does. The chain, with coordinates:**

| Step | Coordinate | Text |
| --- | --- | --- |
| The dilation produces a unitary on the enlarged carrier | §3.4 p. 10 | Stinespring "implies the existence of an `Ñ × Ñ` unitary time-evolution operator `Θ̃(t ← 0) = Ũ(t ← 0)`" |
| The tildes are dropped and the unitary case becomes the working case | **(28) p. 11** | "**Without any real loss of generality, the preceding arguments imply** that one can focus on the case in which the time-evolution operator is unitary, `Θ(t ← 0) = U(t ← 0)`" |
| The relative operator is formed from that unitary | **(39) p. 13** | "suppose that `Γ(t ← 0)` is unistochastic, with unitary time-evolution operator `U(t ← 0)`. Then, for any two times `t` and `t′`, one can define a relative time-evolution operator `U(t ← t′) ≡ U(t ← 0)U†(t′ ← 0)`" |
| The visible readout of (42)'s shape is taken from it | **(42) p. 14** | `Γ_ik(t ← t′) ≡ \|U_ik(t ← t′)\|²`, "which is manifestly unistochastic" |

**The mechanism is a RENAMING, and that is recorded rather than smoothed over.** No equation in §3.5
carries a tilde. The source does not write "form the relative operator from `Ũ`"; it writes (28)'s
reduction, which licenses working with *a* unitary `U(t ← 0)` on the strength of "the preceding
arguments" — and for a process that was not already unistochastic, the unitary those arguments supply
is the **dilated** one. So `D4a`'s positive answer is inherited through (28)'s tilde-dropping, not
through an explicitly dilated instance of (39).

**An independent instance confirms the source will form a relative operator on an enlarged carrier**,
with explicit labels rather than by renaming: §3.7 posits a composite `SE` with unistochastic
dynamics at **(44) p. 17** and forms the composite's **relative** time-evolution operator
`U^SE(t ← t′)` at **(46) p. 17**; **(52) p. 18** then takes a readout of exactly (42)'s shape,
`Γ^S_{ii′}(t ← t′) ≡ |U^S_{ii′}(t ← t′)|²`.

### The trap this adjudication had to avoid, recorded because it is easy to fall into

**Source A uses the tilde for TWO different objects, and only one of them is the dilation's.**

- **`Γ̃(t ← t′)` at (37) p. 13** is an `N × N` matrix on the **original** carrier, defined as
  `Γ(t ← 0)Γ⁻¹(t′ ← 0)` — the *would-be division*, which the source immediately shows is "not
  generically stochastic".
- **`Γ̃`, `Θ̃`, `Ũ` in §3.4 p. 10** are `Ñ × Ñ` objects on the **dilated** carrier `C̃`.

**`D4a`'s answer does not rest on (37), and may not be read as resting on it.** (37) forms no
candidate from the dilated unitary; it is a counterexample the source uses to motivate indivisibility.
Mistaking the two tildes would have produced a positive `D4a` for the wrong reason.

**`D4a` positive means `DC2b` is NOT reached.** The round does not stop here.

## `D4b` — NEGATIVE. No general map returns the relative candidate to `V`

Act 7 asks whether, given that a candidate is formed on the dilated carrier, "the source suppl[ies] a
map returning it to `V`".

**It does not, for the relative candidate. What it does supply is narrower, and the boundary is
exact.**

### What the source DOES supply: the ROOTED readback, at the root only

**§3.4 p. 10** supplies marginalization back to the original carrier for the **rooted** object alone:

> `Γ̃(t ← 0)` "yields the original `N × N` transition matrix `Γ(t ← 0)` by marginalization over the
> ancilla's configuration `i′` at time `t`, **for at least some choices** of the ancilla's
> configuration `j′` at the initial time `0`: `Γ_ij(t ← 0) = Σ_{i′=1}^{N′} Γ̃_{(i,i′)(j,j′)}(t ← 0)`"

Two limits are on the face of it. The map is given for `(t ← 0)` and for no other conditioning time;
and even there it holds "for **at least some** choices" of `j′`, not for all.

**So the readback exists exactly at `t′ = 0` and nowhere else.** That is a sharper statement than
"no readback", and it bounds what an amendment has to supply: the gap is at `t′ ≠ 0`, which is
precisely where the relative candidate (39)/(42) lives and therefore where the dilation-choice test
would be run.

### What the source does NOT supply, and the conditions its near-misses consume

Every place Source A carries a **relative** object back to a subsystem carrier does so under posited
conditions that §3.4 does not state of a generic Stinespring dilation. All of them were checked:

| Location | What it gives | The conditions it consumes |
| --- | --- | --- |
| **§3.7 (50) p. 18**, landing on **(52) p. 18** | marginalization of the composite's relative object to the subject carrier | **(45) p. 17**, the *idealized statistical correlation* `p^SE_{i′e′}(t′) = p^S_{i′}(t′) δ_{e′e(i′)}` — the source's own word is "idealized"; and **(46) p. 17**, the **tensor factorization** `U^SE(t ← t′) = U^S(t ← t′) ⊗ U^E(t ← t′)`, introduced as "**If** there is to be any possibility of the two subsystems evolving independently … **then it should be possible to factorize**". (50) then explicitly proceeds by "invoking the **unitarity of the environment's relative time-evolution operator** `U^E(t ← t′)`" — an object that exists only because (46) posits the factorization. |
| **§3.8 (66)** | tensor factorization of a relative transition matrix between two subsystems | conditioned on the subsystems "**not interact[ing] with each other after `t′`**". It is a factorization statement, not a marginalization of a dilated relative candidate. |
| **§4 (74)**, and the later marginalization over `D` and `E` | the three-subsystem analogue | stated as "**Mirroring the analogous formula (46)** in Subsection 3.7" — the same posited factorization, now threefold, plus the same idealized correlation at (73). |

**None of these is stated of §3.4's dilation.** §3.4's ancilla "need not be regarded as physical",
and Stinespring there supplies **existence only** — act 7's `D3`, cited and unrevised. Nothing in
§3.4 factorizes the dilated relative operator into a system part and an ancilla part, and nothing
posits a correlation condition of §3.7's shape for it.

**Importing (45)/(46) into §3.4's setting would be constructing on the source's behalf**, which act 4
declined and act 7 declined. This adjudication declines likewise.

### The asymmetry has a single cause, and naming it is the finding

**(28) p. 11 drops the tildes, which makes every downstream formula available on the dilated carrier —
and nothing re-attaches them to carry a result back.** The dilation is used one-directionally in the
source's exposition: it licenses the unitary case going forward, and the only return path it supplies
is the rooted marginalization of §3.4 p. 10. `D4a` is positive and `D4b` is negative **for the same
reason**, and that reason is a feature of the text rather than of our witness.

## The prediction HELD — and that is not the finding

Act 7's result recorded, as a counterfactual and explicitly "settl[ing] nothing in this round", the
reading **`D4a` positive / `D4b` negative**. The resumption freeze carried it as a preregistered
prediction and forbade it from becoming the default answer.

**Both questions were asked on the authoritative surface and answered from it.** The prediction held.
**That is reported as the prediction holding, not as the prediction having been the finding**, and the
answers stand on the coordinates above rather than on act 7's note.

**What this adjudication adds beyond act 7's recorded reading**, stated so the round's contribution is
legible rather than inflated:

1. **The mechanism of `D4a`'s positivity** — that it runs through (28)'s renaming rather than through
   a tilde-carrying instance of (39), with (42) p. 14 named as the readout.
2. **The two-tildes trap** — (37) p. 13's `Γ̃` is on the original carrier and is *not* the dilation's
   object, so `D4a` may not be argued from it.
3. **The exact boundary of the rooted readback** — it exists at `t′ = 0`, and only "for at least some
   choices" of `j′`; the gap is at `t′ ≠ 0`, which is where the relative candidate lives.
4. **How §3.7's readback actually works** — (50) does not merely sit alongside (45)/(46); it
   **consumes** (46) by invoking the unitarity of the `U^E` factor that (46) posits.
5. **A completed sweep** — §3.8's (66) and §4's (74) were checked and are the same posited
   factorization, so the negative answer rests on the whole paper rather than on §3.4 and §3.7 alone.

## Routing, and what happens next

Act 7's frozen stop table, fourth row:

> Contract met; a candidate is formed on the dilated carrier; the source supplies **no** map back to
> `V` → layer 2 **paused** until an append-only amendment freezing the readback map is merged, then
> executed at **reduced strength**; `DC1`, `DC3` or `DC4`, each marked reduced-strength.

**The round is at that row.** The next artifact is the readback amendment. **No witness computation,
no witness B, no `T1`–`T4` formalization, no Lean and no candidate comparison may be performed before
it is merged.**

**And the strength bound is inherited now, before anything is built**, so that no later result can be
read past it. Under a readback fixed by our own amendment:

- `DC3`/`DC4` would state invariance **under that readback**, never invariance simpliciter;
- `DC1` would state divergence **under that readback**, never underdetermination of Source A's own
  visible prediction, and never a demonstrated need for a selection principle;
- a difference produced under such a map could still be an artifact of the extra map rather than of
  the dilation freedom, which is why the strength is reduced.

## What this adjudication does NOT establish

- **No `DC` label.** `DC2b` is not reached; `DC1`, `DC3` and `DC4` are layer-2 labels and layer 2 is
  **paused**.
- **`DC2a` is NOT revised.** It remains correct of the `ℕ`-indexed discrete witness it was about.
  Act 8 substituted the object under test; it did not re-answer `D2`.
- **`D1`, `D2` and `D3` were not re-adjudicated**, and **`D3`'s gap remains separately OPEN** —
  Stinespring's pointwise existence with no coherent time-indexed family derived or selected, and no
  stated link from regularity of the visible family to regularity of `Θ` or `U`. **Nothing here
  closes it**, and it is not what the readback amendment is about.
- **`D5a` and `D5b` remain *not reached*.** Act 3's padding theorem bears on layer 2's witness
  comparison, which is not performed. No shape condition and no quantity-identification condition is
  determined or relied on anywhere here.
- **Act 8 is not revisited**, and **`CE1` remains existential** — one witness, one extension, never
  restated as a classification. Everything above concerns Source A's text, not that witness.
- **Nothing about whether the dilation moves the visible candidate.** That is layer 2's question and
  it is untouched. This adjudication establishes only *where the source's construction stops*.
- **No claim that Source A is applicable or inapplicable**, and none that the correspondence succeeds
  or fails. A construction that supplies no general readback is a fact about the construction's
  reach, not a verdict on the theory.
- **No candidate-selection principle** is adopted or proposed; act 5's gauge-versus-empirical tension
  is not adjudicated and `F1` versus `F2` is undecided.
- **`BD3`, `BR3`, `RT1`, `CU1a`, `MP4`, `SA2`, `TI1`, `UB2`, `DC2a` and `CE1` are cited and
  unrevised.** Acts 1 through 6 and act 8 are not reopened.
- **No manuscript edit**, and no Lean of any kind.

## What would settle what remains

1. **The readback amendment** — an explicit map carrying a candidate on the dilated carrier back to
   `V`, fixed in advance, with its provenance reported as **ours** rather than the source's. That is
   the immediate next artifact, and every layer-2 label it enables is bounded by it.
2. **Act 7's `D3` gap**, separately: a derivation or selection of a coherent, suitably regular
   dilation family, or a countermodel. Unaffected by anything here.
3. **Layer 2 itself**, at reduced strength, once the amendment is merged.
