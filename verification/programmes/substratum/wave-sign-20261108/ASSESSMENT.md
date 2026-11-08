# WAVE-SIGN-1: binary notation, the selected second-order rule, and sign-sensitive claims

**Standing:** paper-only source and hand-algebra assessment for #1193, by Codex
`/root`, 2026-11-08. First author checkpoint; independent review is pending.
This assessment changes no manuscript, physical premise, implementation or
verification lifecycle.

**Source snapshot:** main `120b3ca40d94fdab8db1ad271db299ff44360f2c`.
[Authorization and writer scope](https://github.com/amaybaum/incompleteness/issues/1193#issuecomment-6717097561)
are provenance. The claims below use the source texts and calculations stated here.

## 1. Question, decision rule and result

The question is whether Main's displayed `+v` update conflicts with the
`−v` second-order rule used by Substratum, SM and MECH-1 at odd characteristic.

The decision rule is:

1. Read the alphabet and coordinate definitions attached to each formula.
2. Check Main's own general-model premises before inferring a cross-paper conflict.
3. Keep invertibility, a specified time-reversal symmetry, and preservation of
   the canonical alternating form separate.
4. Attribute a theorem only to the sign, representation and access assumptions
   used in its proof. Do not choose the sign because it gives a desired quantum result.
5. If the formulas agree at their stated scopes, recommend correcting the
   discrepancy record rather than changing the physical model.

**Author finding:** Main's binary display is consistent with the general
minus-memory model that Main itself explicitly posits. Main:294 specifies
`q = 2`; Main:726, item (xiii), gives the general second-order rule with
`−x(t−1)` and explicitly calls the display its binary instance. Thus
Main:296 supplies no conflicting odd-`q` native rule.

There is a genuine mathematical distinction between plus and minus at odd
characteristic. MECH-1's sign-sensitive conclusions require the minus rule.
This distinction remains useful, but it does not by itself establish a
contradiction in the cited Main display.

The recommended disposition is a scope clarification, subject to independent
review. No new sign choice is necessary to interpret Main's currently selected
model. Deriving that model from OI's foundations remains a separate physical
question; the ledger calls its second-order form a posit.

## 2. Source map

All line references and links in this section use the source snapshot.

| Source | What the source actually supplies |
| --- | --- |
| [Main:294–296](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L294) | State `(u,v)` over `F_2`; the displayed update is `(Ku+v,u)`. The field is declared immediately before the formula. |
| [Main:304](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L304) | The cross-block support factorization holds over `Z_q`. This statement does not choose a general memory sign. |
| [Main:318 and :326](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L318) | The corollary repeats the binary scope. The later prime-`q` Weyl/Clifford extension concerns the configuration-basis channel, not MECH-1's smaller encoded carrier. |
| [Main:726, item (xiii)](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L726) | One step is `x(t+1)=F(x(t))−x(t−1)` on previous/current values in a finite abelian group. The text calls the second-order form a posit, not an OI axiom or a derivation, and identifies the §3.2 display as its `q=2` nearest-neighbour instance. |
| [Substratum:98](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Substratum.md#L98) | A4's examples explicitly lie in the minus-memory second-order class over `Z_q`. |
| [SM:106 and :224–228](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L106) | The explicit inverse and the form-lemma proof use the minus-memory ansatz. The proof does not independently derive the memory sign from bijectivity. |
| [SM:296](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L296) | The exact linear rule is `(p,c)↦(c,Ac−p)`, with its conserved quadratic form and stated finite-cycle hypotheses. |
| [SecondOrderCircuit:47–68](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean#L47) | `prevOf` is the first slot, `curOf` the second; `leap F` is `(p,c)↦(c,F(c)−p)`. Its inverse/factorization are about this specified class. |
| [OI_Time_Reversal:99–138](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean/OI_Time_Reversal.lean#L99) | `WaveS` has the minus-memory form. The theorem proves invariance under the specified `t↦−t` transformation, not that every bijective update has this form. |
| [MECH-1:439–446](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L439) | Node 2 already acknowledges that Main's display is binary and the two signs then agree. |
| [MECH-1:1095–1105](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L1095) | The assumption-watch marker treats Main's odd-`q` native sign as divergent. That interpretation omits Main's explicit item (xiii); it needs the scope qualification above. |

The papers, book sources, Lean definitions and relevant retained research
records were searched for the recurrence, phase-space form and sign statements.
The release archive excludes `verification/programmes` by `.gitattributes`;
the relevant research records were therefore read separately from GitHub at the
same immutable commit. This is a targeted sign assessment, not a fresh audit of
every theorem in those records.

## 3. Hand derivation with an explicit sign convention

Let `u` mean the current slice and `v` the previous slice. Set

```text
T_ε(u,v) = (Ku + εv, u),       ε ∈ {+1,−1}.
```

Here `ε` is the actual coefficient of the previous slice: `ε=−1` is the
selected minus-memory rule. This convention avoids using a positive sign
parameter to mean subtraction.

### 3.1 Both signs are bijections

For either unit `ε`,

```text
T_ε⁻¹(a,b) = (b, ε⁻¹(a−Kb)).
```

Substitution in both orders gives the identity. More generally, replacing
`Ku` by any fixed function `F(u)` leaves this inverse valid.
Invertibility therefore does not select the minus sign.

This is a countercontrol to inferring the sign from the word “reversible”
when that word means only bijective evolution.

### 3.2 Ordinary reversal of the two time slots

Let `R(u,v)=(v,u)`. Then

```text
R T_ε R(u,v) = (v, Kv+εu),
T_ε⁻¹(u,v)   = (v, ε⁻¹u−ε⁻¹Kv).
```

By direct substitution `R(T_ε(R(u,v)))=(v,Kv+εu)`. Since `ε²=1`, equality with the inverse
requires `(1+ε)K=0`. The minus rule satisfies this for every `K`.
For the plus rule over an odd-prime field it requires `K=0`.
Thus for nonzero coupling the specified slot-swap reversal distinguishes the
two signs. This is a statement about this reversal map, not every possible
notion of time reversal.

### 3.3 The canonical alternating form

Over a field, use the current/previous ordering and

```text
M_ε = [ K   εI ],         Ω = [ 0   I ].
      [ I    0 ]             [−I   0 ]
```

Block multiplication gives

```text
M_εᵀ Ω M_ε = [ Kᵀ−K   −εI ].
             [  εI      0  ]
```

For `Kᵀ=K` this equals `−εΩ`. Hence the minus-memory step is
symplectic and the plus-memory step anti-symplectic. In characteristic two
these coincide. Affine constant offsets do not change this bilinear calculation.

A passive coordinate change transforms both the update and its alternating
form; it preserves the multiplier. Negating one slot alone changes the other
update equation too. It does not turn `(Ku+v,u)` into `(Ku−v,u)` with
the same declared slot meanings and form.

### 3.4 Boundary factorization is insensitive to this sign

The memory term is on-site. It contributes no entry to either cross-region
block. Only the neighbour coupling contributes across the visible/hidden cut.
Consequently Main's Lemma 1 support factorization is the same for both signs,
over the same coefficient ring. Rank statements additionally retain their
field/module qualifications. Nothing here repairs or challenges that lemma.

## 4. Which conclusions transfer

| Claim | Assessment |
| --- | --- |
| Main's binary display and the general minus rule disagree | Refuted as a reading of the cited scopes: `−v=v` in `F_2`, and Main names that display as the general rule's binary instance. |
| A literal plus-memory extension at odd prime `q` has the same symplectic multiplier as the minus rule | Refuted by §3.3, for symmetric coupling and the declared canonical form. |
| Bijectivity alone derives the minus sign | Refuted by the inverse in §3.1. |
| Main already posits the minus-memory second-order model outside its binary display | Directly stated by its own item (xiii), independently of importing SM's conclusions into Main. |
| MECH-1's odd-`q` symplectic argument applies to the selected minus model | The sign prerequisite is supported. This does not re-review the whole of Theorem W or Proposition AS. |
| MECH-1 proves an OI-native physical controller, a qubit quarter phase or full equivalence | Not supplied by this assessment; MECH-1's recorded stop and missing premises remain unchanged. |

The word “symplectic” must also be attached to its carrier. Any finite
configuration permutation has a unitary permutation lift on the Hilbert space
whose basis is all configurations, irrespective of this sign. MECH-1's fixed
odd-`q` phase-space frame instead identifies laws on `2n` classical
coordinates with operators on `n` qudits. A failure of symplecticity in the
latter frame is not a failure of unitarity of the former configuration-basis
lift. This assessment does not reprove either operational correspondence.

## 5. Recommended disposition and remaining gate

1. **Preserve Main:296 and :304.** Their stated scopes do not establish a sign
   contradiction. A cosmetic sign change is unnecessary to interpret the
   existing model.
2. **Qualify the discrepancy record.** Cite Main:294 and item (xiii) alongside
   MECH-1's marker. Proposed wording for a later owner-approved correction:
   “The minus-memory form is a posit of Main's selected lattice model, item
   (xiii). Main's displayed plus sign is its binary instance, where the signs
   coincide. A different plus-memory extension at odd characteristic would be
   anti-symplectic in this frame and is not covered by this selection argument.”
3. **Keep derivation and assumption separate.** SM:312 says “Reversibility
   requires `D=−I_K`”. If read as bijectivity alone, that inference is too
   strong: any invertible `D` gives an invertible second-order linear map.
   Within the already selected minus-memory ansatz `D=−I_K` is the stipulated
   coefficient. Clarifying that wording is a separate propagation item, not
   permission to alter SM or its artifacts here.
4. **Do not reopen the quantum-mechanism search under a new sign by default.**
   A genuinely different odd-`q` update would be a different proposal, with
   independently motivated premises and the full access/composition controls.

Independent exact-head review is needed before treating this assessment as an
accepted correction or deciding #1193's closure. Native-rule adoption,
manuscript edits, integration and closure have not occurred.

## 6. Verification limits

The algebra above is given in full and was checked by hand. No scientific
program, enumeration, simulation, Lean build or native V3 stage was run.
Repository CI, if green, checks repository compatibility; it does not establish
the physical realization. Source reading is not a new kernel certificate.

The earlier MECH-1, Q-A, feedback, controller and retention studies retain their
respective scopes and review histories.
