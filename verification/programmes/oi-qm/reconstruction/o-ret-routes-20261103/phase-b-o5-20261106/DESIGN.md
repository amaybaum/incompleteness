# O-RET Phase B: one O5 register screen

**Status: BLOCKED at the physical geometry/read-access screen; independent review pending.**
Paper-only assessment for #1032, not a freeze, run or physical-retention result.
Drafting base: `f49b768709d262a05471895cec703b31aff19b57`.
Writer: `writer-oret`, this coordinating Codex session.
The candidate was fixed before outcome analysis at checkpoint
`cc2d21b36640c421d28dcca76840e97ba26e6675` of draft #1177.
The old #1115 branch and all Phase A evidence are unchanged.

## 1. Owner scope and question

Owner direction in ChatGPT Work, 6 November 2026, recorded in
[#1032 c.6692541241](https://github.com/amaybaum/incompleteness/issues/1032#issuecomment-6692541241):

> For the first candidate, I’d screen one O5 register. O5 lets you keep the preregistered preparation laws and vary the register geometry. Require a physical reason for choosing that geometry before analyzing it. The paper deliverable should identify the candidate, show which Theorem N hypotheses it escapes, and work through the second hold tick. If the geometry or its read access lacks a physical source, stop at that specific gap. Send the design for independent review before any freeze or run.

The question is whether one physically motivated register can retain a readable
classical carrier record through the second hold tick in an unresolved O5 case.
The source screen is a prerequisite, not evidence supplied by a successful
retention calculation. The two gates must not be reversed.

**Outcome of this screen.** The one geometry has a structural motivation but no
located physical implementation of its joint read access. Stop at that gap.
The static comparison with the existing Theorem N also shows that this choice
does not supply an unresolved retention tuple: PAD or NP already applies.
No second-hold calculation, new decoder, counted pass or replacement candidate
is supplied. This does not close O5 or the physical-retention obligation.

## 2. Fixed candidate and preparation laws

Use Theorem N §3.1's SMR binary copy-form model on `Lambda=Z/8`:
`x'_i=y_i`, `y'_i=y_{i-1} XOR (y_{i+1} OR y_{i+2}) XOR x_i`.
It is the binary form of the ring construction in SM §3.1.
As physics this SMR choice remains the unadopted E-SDC extension named in
Theorem N. The eight-site ring is an existing mathematical test setting;
this paper does not derive it as the physical OI substrate.

The carrier is site 0, both slices, with all four independent preparation
labels `P={(0,0),(0,1),(1,0),(1,1)}`, uniform carrier law, target
`c=y_0(t0)`. Do not restrict `x_0` or import a correlated carrier background.

The single proposed register is `A={7,1,2}`, ordered as `(1,2,7)`;
locus `R=(x_A,y_A)`; proposed read cells `rho(R)=y_A`.
The complete structural current-slice parent set of the carrier update is
`{7,1,2}`. Choosing the whole incoming stencil is motivated by the
rule's own interaction neighbourhood before considering a retention result.
It is a reason to screen the geometry; it is not a derived apparatus.

This is a fixed non-arc register of width 3 meeting `{6,7}`.
No state-selected partition, moving geometry or new value of `q` is added.

Keep precisely the preregistered law definitions of Theorem N §3.2:
`mu=mu_Sigma tensor nu_r`, `r in {-1,0,1,2,infinity}`.
Here `nu_{-1}=pi0` is uniform on all non-carrier cells; for finite
`r>=0`, both slices of every non-carrier site in
`Z_r(A)={i!=0:dist(i,A)<=r}` are fixed to zero and the remaining
non-carrier cells are independent uniform bits; `nu_infinity=delta0`.
The formula for the preparation family is unchanged; its ready set depends
on the declared register just as before. No law is selected after inspecting
a retention result. The ready supply remains physically unsourced.

## 3. Physical source screen and stopping point

The proposed physical reason is local interaction geometry: retain the full
incoming neighbourhood of site 0.
The rule establishes that dependency stencil. To make it a physical register,
however, an embedded apparatus must have a derived coupling that collects its
three current-slice values into a distinguishable accessible record at the
required ticks, with its own state, resources and effect on the carrier
accounted for. Declaring `rho(R)=y_A` does not provide that process.

| Source inspected | What it supplies | What it does not supply for this candidate |
| --- | --- | --- |
| SM §3.1, explicit ring construction | The reversible rule and its state-dependent neighbour assignment | An apparatus implementing the joint current-slice read of `{7,1,2}` |
| Theorem N §§3.1, 7.1–7.2 | The locus convention; H-cur is declared access; unresolved O5 conditions and the requirement for an independently motivated shape | A physical source for H-cur or for this particular observer geometry |
| Main §1, observer conditions; §3.4 finite-law realizations | Observer partitions, persistence requirements and existence/representation results under their stated hypotheses | Identification of this ring stencil with a prepared readable physical apparatus |
| MR-star, C-3 | The ready-region/source gap and the distinction between a wake and a usable record | A prepared ready supply for this geometry |
| Native link sourcing gate, “Actual OI reference input” and “Fully specified but non-native link/pointer model” | The distinction between a microscopic wave update and added pointer apparatus | A permitted physical read interface for the proposed ring register |
| O-RET DEFINITIONS, D-TRN | A distinct readable register and demonstrated retention are required | Permission to substitute hidden-state persistence for physical readability |

The source search covered the Markdown paper/book corpus and verification
records, with targeted searches for register geometry, physical/readable
registers, read access, SMR and non-arc registers; relevant retained source
passages above were read at the drafting base. The limitation is specific:
**no source was located that implements the proposed joint read of
`y_{1,2,7}` as an accessible physical register.**
This is not a theorem that such an apparatus cannot exist, and it makes
no claim that all register geometries or record mechanisms are absent.
The structural stencil is present; its physical apparatus interpretation
remains a declared choice.

**Stopping point:** unsourced physical register/read access, within #1032.
No retention calculation is performed to compensate for that missing source.
The first missing requirement is not silently converted into a new physical
premise. Ready-state availability would also need its own source.

## 4. Comparison with the existing obstructions

This table is a static applicability check of the existing result, not a
new retention evolution or a claim that the candidate escapes every lemma.

| Existing result | Applicability to the one fixed candidate |
| --- | --- |
| PAD | Applies to `nu_{-1}=pi0`; the previous register slice is an independent uniform pad. This is a known negative control. For `r>=0`, that slice is fixed, so this PAD hypothesis fails. |
| NP | Its hypotheses remain: product law and both `x_0` values. For every `r>=0`, all three parents of `G_0=y_7 XOR (y_1 OR y_2)` are ready zero, so its uniform-`G_0` exception is not met. The structural outside-parent set includes `y_0`. NP's known obstruction applies; no open J-1-compatible informative write is obtained. |
| AE | The global register map has state-dependent carrier entry at site 7, so its fixed-coefficient hypothesis is not available. This does not remove NP. |
| LS | The non-arc geometry fails LS's arc hypothesis. Escaping LS alone does not make a tuple unresolved. |
| U | Site 1 and site 7 have structural dependence on `y_0`, so the disjoint-parent hypothesis fails. |
| SS-2 | The width-1 hypothesis fails. No extension of SS-2 to this width is asserted. |

Thus no member of the fixed law family qualifies as the requested
“existing obstructions leave the outcome open” tuple: PAD covers `pi0`,
and NP covers the ready laws. The O5 family remains open in the wider scope
of Theorem N §7. Choosing an O5-shaped register is not itself sufficient.
No other register or preparation law is screened in this unit.

## 5. Second hold tick: the unperformed step

Use the existing `T=2` convention of Theorem N §3.1:
hold ticks `H_2={t0+1,t0+2}` and read window
`W_2={t0+1,t0+2,t0+3}`.
A passing second-hold-tick value alone would not satisfy this window.

Because the physical source screen stops the candidate, there is no
derived trajectory, error table, storage verdict or hold-tick prediction here.
The applicability check above also prevents treating the one candidate as
an unresolved tuple awaiting a numerical run. No second-tick result is
invented from the geometry.

For any separately authorized continuation, the paper would have to derive
the write, both hold ticks and the final endpoint; check J-i and J-ii
jointly at both hold ticks; and check worst-case decoding error for every
preparation and the stated storage/invariance condition on the whole window.
The existing threshold is `epsilon*=1/20`; it is not loosened.
These are unmet obligations, not an authorization to continue or execute.

## 6. Provisional counting policy, retained here for review

The owner's separate ruling was:

> Adopt the corrected counting criterion provisionally for this classical design. Keep the ambiguous D1 and D2 cases undecided. Ask the independent reviewer to check whether a counted pass could genuinely have failed, especially where the decoder may already have seen the relevant input at the write tick.

The following restates the operative definitions and criterion from historical
DPB §5 at `4b4cacc93884039afadd0069373b0ac448761a6b`.
That commit is provenance, not support on main for a new scientific claim.
The necessary working policy is stated here; no proof of a new retention
result relies on a host comment or an unlanded section.

- **D1:** among deterministic decoders minimizing worst-case write-tick
  error on all four preparations, take the lexicographically least, with
  read configurations in increasing binary order and `0<1`.
  Off write support it therefore takes zero. It reads no hold-tick data.
- **D2:** retain D1 on write support. On the full register-configuration
  space form the equivalence relation `~1` generated by
  `ell ~ f_R(ell,q)` for all `q in supp Q_{t0+1}`.
  Propagate each write-supported configuration's assigned value to read
  configurations in its class. A conflicting assignment makes D2
  undetermined and falls back to D1; otherwise remaining entries take D1.
- **Supports:** `Q=Par(R) minus R` is structural on the full state space,
  not a parent set pruned to a prepared trajectory.
  `Q_W` is the union of supported input values on the hold ticks of
  `W_T`, as in the original criterion.
- **IP:** `Q_W subseteq supp Q_{t0+1}`.
  For consistent D2, an IP pass is implied by the decoder construction.
  In particular the D2 retention test at `T=1` cannot count by itself.
- **Working count rule:** a storage row 5 or 6 with nonempty environment
  counts as use-novel if (U-1) the same storage row is reached under D1,
  or (U-2) it is reached under consistent D2 and `Q_W` contains an
  input outside `supp Q_{t0} union supp Q_{t0+1}`.
  An IP D2 pass with no D1 storage row never counts.
- **Undecided cases remain undecided:** a D2 pass whose new hold inputs
  occurred only at the write tick; and the D1 analogue in which every
  hold input already lies in `supp Q_{t0}`. The mere statement that D1
  reads no hold-tick data does not resolve its write-input caveat.

The historical comparison class `F(phi)` fixes law, carrier, locus,
structural Q and decoder rule. Its alternatives are global bijections
`phi'` agreeing with `phi` on every state whose Q value lies in
`supp Q_{t0} union supp Q_{t0+1}`, with a register map depending on
`(R,Q)`. These are logical calibration alternatives, not sourced
physical alternatives. A use-novel claim must specify this comparison
class and show that the input is genuinely unseen by the decoder's
construction; for the D2 converse the decoder must also be nonconstant
on the image of the new-input register map.

The independent reviewer must test the above policy against the exact
historical definitions, especially write-tick input leakage and the
difference between IP and the weaker class-merging flag IP-prime.
A claimed counted pass would need an explicit allowed failure alternative,
or a precise justification of the applicable criterion; unresolved cases
must not be counted by default. **This candidate supplies no storage row,
decoder table or counted pass.** No calibration model is claimed as native
physical retention, and no criterion experiment is executed.

## 7. Separate coherence and coupling obligations

The owner added cross-read ancilla coherence as a separate #1032 obligation.
Classical record persistence does not establish it. It remains open until
a coherent carrier and a read capable of preserving its coherence are
physically sourced. #1143 retains responsibility for the distinguishing
test. The S8-A assessment's two-read statistics in its assessed instance
can also be reproduced by classical memory; a match alone would not
identify the mechanism. Its record is planning provenance, not a new
scientific premise of this geometry screen.

#866 separately owns B3's physically outcome-conditioned exchange and
public access to its result. Even a future positive retention result
would supply only an ingredient; it would not settle that coupling/access
handoff or authorize another #1169 candidate assessment.
No work on #866's active branch or any #1169 source file is performed.

## 8. Review gate and source map

Request independent review of the exact pushed head for:
the physical source stopping point; the geometry's motivation before
outcome analysis; all six obstruction checks including NP; the unperformed
second hold tick and correct full window; the provisional counting rule
and its unresolved cases; and the separation of coherence and coupling.
A reviewer may accept this only as a stopped paper screen, not as a
physically sourced design or a retention demonstration.

| Reference | Role for this paper |
| --- | --- |
| `../phaseB-negative/THEOREM-N.md`, §§3–4, 7; its `REVIEW.md` | Support on main: definitions, existing scoped obstructions and open-family conditions |
| `../../../../../../papers/SM.md`, §3.1 | Support on main: the mathematical ring update and stencil, not physical read access |
| `../../../../../../papers/Main.md`, §§1, 3.4 | Support on main for the limited comparison of observer conditions and realizations |
| `../../measurement-record-formation/amendments/MR-star.md`, C-3 | Support on main for the stated ready-source gap, not a universal absence theorem |
| `../../../../substratum/continuous-substates/native-link-sourcing-gate.md`, named sections | Support on main for the microscopic-rule/apparatus distinction |
| `../DEFINITIONS.md`, D-TRN | Support on main for distinct readable-register/retention requirements |
| DPB at `4b4cacc93884039afadd0069373b0ac448761a6b`, §5; decoder definition at historical `43370576` §6.2 | Provenance of the provisional policy restated in §6; no off-main proof used for a candidate result |
| #1032 c.6692541241 | Owner authorization/provisional-policy provenance, quoted in §§1, 6 |
| #1143 c.6681999486 and #866 c.6691917468 | Planning provenance of the separate obligations in §7 |
| First checkpoint `cc2d21b36640c421d28dcca76840e97ba26e6675` | Provenance that the one geometry was fixed before its outcome screen; it must remain reachable if that ordering claim is retained at landing |

No freeze, scientific computation, enumeration, simulation, Lean build,
replay, dispatch, implementation, new physical premise adoption, merge or
scientific promotion was performed. Ordinary automatic PR CI is verification
of the draft only. The next substantive candidate requires a new bounded
owner scope; this paper does not authorize one.

