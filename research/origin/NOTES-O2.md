# NOTES-O2 — candidate mechanisms for a discrete non-monomial mixer

Thread `research/origin`, node O2. Base L = `9f9f8257`. Evidence levels as in NOTES-O1. Script:
`experiments/o2_mechanisms.py` (17 checks, 4 countercontrols, classification rule fixed in the header before
run 1; green on run 1, byte-identical on replay). O1's scripts carry the exhaustive parts the mechanisms share.

**Productivity test, fixed before starting (§A.31).** A mechanism analysis counts only if it gives the smallest
exact model, the induced operation on the visible qubit, and a disguise verdict that names *where* the coherence
would enter; a list of mechanisms "that do not work" without that location is a non-gem.

## 0. Verdict

**No mechanism built from the substratum's stated resources sources a discrete coherent mixer.** Every one of
them hands the visible qubit only monomial (dephasing-covariant) operations and reads it passively, so it lies
inside the O1 envelope and its sandwich visibility is exactly 0. The four constructions that do pass the
owner's witness each receive the coherence through their input — a non-monomial operator given by hypothesis,
by postulate, by a complex one-parameter group, or by a chosen unitary dilation — and fail the disguise test.
One construction passes with monomial input only: the substratum swap acting on a knowledge-balance toy bit.
It is CONDITIONAL on a change of the observer's access (KB-D: reading the path re-randomizes the readback
memory), which the stated access does not contain and which the passive native readout contradicts.

| mechanism | smallest exact model | induced operation on the visible qubit | non-monomial? | sandwich (P_coh, P_deph) | coherence enters | verdict |
|---|---|---|---|---|---|---|
| A12 — A1–A2: finite configurations, bijective dynamics, selectable permutations | all 24 bijections of {0,1}², z visible, x hidden uniform | identity ×4, flip ×4, replace-by-uniform ×16; all DC | no | V = 0 on 24 × 24 × 2 composites | nowhere | FAILED (envelope) |
| A36 — A3–A6: bounded, centre-independent, linear, link-coupled rule | second-order rule on a ring, N = 3, K = 2, q = 2, couplings in GL(2, F₂); bijective on 4096 configurations, linear, gauge-covariant under M → G M G⁻¹ | classical stochastic; one step already uniform | no (a permutation of configurations) | (1/2, 1/2) | nowhere | FAILED (envelope) |
| PH — phase interventions | 36 diagonal phase pairs incl. Z, the quarter phase, (3+4i)/5 | identity on populations | no | V = 0 | nowhere | FAILED (envelope) |
| RW — read-write coupling | every bijection fixing all states outside {a, b}, \|S\| = 3, 4, 5 | 1 or the swap at every knob value | no | V = 0 (as A12) | nowhere | FAILED (envelope) |
| ANC — ancilla coupling with readback and feed-forward; record writing | O1 M3 (60 protocols), M4 (2304 composites); `recordInstr` on (z, r) | classical (DC) channels; the recorder into a blank register leaves populations unchanged | no | V = 0 | nowhere | FAILED (envelope) |
| TAV — coarse-graining and time averaging | uniform average over the orbit of a 4-cycle | doubly stochastic, DC | no | (1/2, 1/2) | nowhere | FAILED (envelope) |
| CLO — the completion's closure | words of length ≤ 4 in monomial generators with infinite-order phases; DC closed (O1 M7) | monomial unitaries only | no | V = 0 | nowhere | FAILED (envelope) |
| G1 — `HasAncillaQubitInterference` | `hMat` | the balanced mixer | yes | (1, 1/2) | the hypothesis `availExt … (ancMix A)` | FAILED (disguise) |
| G2 — `LayerFlowExecutable` | gate flow of the site exchange at t = 1/2 | √X = proj₊ + i·proj₋ | yes | (1, 1/2) | the complex phase on the swap's −1 eigenspace | FAILED (disguise) |
| G3 — state-mixing datum, `fixedGateTheory` | `rot(π/4)` | the real balanced rotation | yes | (1, 1/2) | the postulated datum | FAILED (disguise) |
| G4 — unistochastic lift of a balanced transition | lifts diag(1, v)·H of B = [[1/2,1/2],[1/2,1/2]] | a balanced mixer, phases free | yes | (1, 1/2); the substratum's own two-step statistic is the dephased 1/2 | the chosen dilation | FAILED (disguise) |
| G5 — knowledge balance (KB-D) | {0,1}², all permutations, reading z re-randomizes x | the swap on the toy bit's octahedron | in the operational frame yes; on configurations no | (1, 1/2) | the access change KB-D | CONDITIONAL (KB-D) |

## 1. The stated resources, one at a time

**A12 (A1–A2).** With the hidden memory fresh and uniform, the 24 bijections of {0,1}² induce on the visible
bit exactly three channels — identity, flip, replace-by-uniform — all dephasing-covariant [X A12a]. On the
matrix carrier every bijection is a permutation matrix, so O1-T3 applies; the exhaustive composite sandwich
returns V = 0 [X A12b]. The countercontrol composes (H ⊗ 1) into both mixers on the same model and finds
(1, 1/2) [X CC1]: the detector is live on this model. Kernel: `bijectiveOperator_monomial`
[K SubstratumInterface.lean:91].

**A36 (A3–A6, the link coupling).** The smallest model with every structural axiom of the substratum: a ring of
three sites, two internal components over F₂, nearest-neighbour coupling through link matrices M(n, ê) in
GL(2, F₂), the second-order update v^{t+1} = F(v^t) − v^{t−1} with no self-term (A4), linear (A5), and the A6
covariance: transforming the field by a site-dependent G(n) and the links by M → G(n) M G(n+1)⁻¹ intertwines the
dynamics. All three are checked exactly on the 4096 configurations [X A36a–c]. The update is a bijection, hence a
permutation of configurations: monomial on the carrier, O1-T3 applies; the visible bit is already uniform after
one step [X A36d]. **Where the link coupling's unitary groups come from.** The reconstruction's
U(3) × U(2) × U(1) is the unitary group of the bicommutant of the cubic-group action on the internal index space
(Substratum.md:162), a complex representation-theoretic object, and its Stage 1 takes unitary quantum mechanics
(E1) as an input (Substratum.md:122). Neither is an operation available on configurations; a route to the mixer
through them imports E1. The link coupling therefore supplies no discrete mixer: FAILED.

**PH, RW.** Phase interventions are diagonal (monomial) and leave populations unchanged; the owner's Z is here
[X PHa]. A read-write family is a bijection of the states fixing everything outside its pair, so at every knob
value it is 1 or the swap [X RWa]; the kernel says the same (`readWriteOperator_eq_perm` [K
ReadWriteControl.lean:96], `readWriteOperator_range_finite` [K CoherentContinuumSource.lean:292]). FAILED.

**ANC (ancilla coupling with readback).** Covered exhaustively by O1 (M3: attach, monomial step, Lüders readout of
either register, feed-forward, coarse-graining, discard; M4: all permutation pairs on visible ⊗ ancilla). The
canonical readback — store the visible value in the memory and swap it back — gives 1 with or without path
dephasing: memory, not coherence (O1 M4d). The kernel's record instrument `recordInstr`
[K InternalObserver.lean:249] has submonomial Kraus operators |a,a⟩⟨a,b|; its channel is DC, and written into a
blank register it leaves the visible populations unchanged [X ANCa]. Its non-passivity
(`recordInstr_not_passive` [K :290]) is the reset of its own register, which disturbs a classical state only if
the register held information — the memory-erasure case of O1-T7a, not a path dephasing. FAILED.

**TAV, CLO (coarse-graining, time averaging, closure).** A time average is a mixture of permutations, doubly
stochastic and DC [X TAVa]; coarse-graining sums DC branches; DC is a closed linear condition (O1 M7), and the
monomial unitaries form a closed group (words in generators with infinite-order phases stay monomial [X CLOa]).
Field-neutrally, passivity survives the completion by continuity (O1-T5). FAILED.

## 2. The constructions that pass, and where their coherence enters

- **G1.** `HasAncillaQubitInterference T := T.prepAvail 2 (pureAttach 2 0) ∧ T.availExt 2 Unit (fun _ =>
  conjChannel (ancMix A))` [K AncillaInterference.lean:161–163]: the second conjunct *is* the balanced mixer.
  Available by assumption; FAILED by the disguise test, as the owner's note anticipates.
- **G2.** `gateFlow σ t = unit (permMat σ) t` [K LiftAudit.lean:47] is proj₊ + e^{iπt} proj₋, where
  proj₋ = (1 − P_σ)/2 is non-monomial (on a moved pair it is the projector onto (|a⟩ − |σa⟩)/√2). The coherence
  enters through the complex phase placed on the swap's −1 eigenspace, i.e. through a frame (the ± frame) other
  than the configuration frame, joined to it by a complex one-parameter group. The substratum theory does not
  derive it (`substratumTheory_not_layerFlowExecutable` [K LiftAudit.lean:200]). FAILED (disguise). Note that
  this route is ones-fixing (O1-T4b): the disguise is invisible to the ones-fixing invariant.
- **G3.** `rot θ` and `mixImage n θ` [K StateMixingCoupling.lean:45, :50]: "the datum is a postulate, and nothing
  here derives it" (module header). At one angle the theory satisfies `DerivedOI` and `FixedGateSourced` and is
  not quantum mechanics (`fixedGateTheory_derivedOI`, `fixedGateTheory_fixedGateSourced`,
  `fixedGateTheory_not_qm` [K DiscreteCompletion.lean:1929, 1933, 1948]). FAILED (disguise).
- **G4.** A unistochastic lift [K BarandesTuple.lean:430 `IsUnistochastic`] of the balanced doubly stochastic
  matrix is always a balanced non-monomial mixer [X G4a] — but the lift is a choice: lifts with the same B give
  coherent two-step predictions ranging over at least seven values in [4/13, 1] [X G4b, CC3], while the
  substratum's own two-step statistic, B² = B, is exactly the *dephased* branch 1/2 [X G4a]. The coherent branch
  is supplied by the dilation, not by the stochastic data (the dilation-choice audit reaches the same
  conclusion for the anchored readback, `DilationChoice.lean` module header). FAILED (disguise).

## 3. G5 — the one construction with monomial input, examined to exhaustion

**What it is.** Configurations {0,1}², z visible, x a readback memory, all 24 permutations available (the
kernel's exchanges), the counting measure, and one change: the native readout of z is replaced by KB-D, "read z,
then re-randomize x". Then (O1 F8): the reachable posteriors are the uniform state and six pair states; they form
an octahedron; z is a maximal frame with singleton faces; the substratum swap maps z+ to the balanced extreme
state x+; the sandwich is (1, 1/2) with the observe-and-forget of KB-D as the path dephasing, which is the
genuine frame dephasing of this body. It is Spekkens' toy bit [L].

**Disguise test.** No operator in the input is non-monomial; no complex structure, no unitary, no `hMat`. The
non-classicality of the visible qubit is produced by KB-D together with the exchanges: without KB-D the same
swap is a vertex permutation of the classical simplex (O1 CCF1). By the owner's letter (an imported unitary, a
Hadamard by assumption, a complex structure on the carrier) G5 passes. What it carries instead is a
complementarity-type disturbance law: recording the path destroys the memory a mixer would use. That law is
the named premise; the verdict is CONDITIONAL (KB-D), not DERIVED.

**Does OI source KB-D? Branches, each closed by a check.**
1. *The kernel recorder.* Writes the record into a register; into the memory register it sets x := z, which
   makes z and x jointly known — point masses become reachable and the body is the simplex again. Not KB-D
   [X O1 F7 with W].
2. *Hidden-sector relaxation (C2, the bath hypothesis).* Re-randomizes the memory whether or not the path is
   observed, so it lowers P_coh and P_deph together; it cannot separate them [W].
3. *Incompleteness of observation (the hidden sector is not read).* Restricts what is read, not how reading
   disturbs; with the exchanges available the memory is readable by swap–read–swap without disturbing z
   (O1 F2) [X]. Not KB-D.
4. *The native readout.* Every finite operational theory of the kernel carries the Lüders readout
   (`readout_is_localLuders` [K OperationalAssembly.lean:658]), non-disturbing on configuration-diagonal states,
   and OI-STAGE's towers are passive [A oistage A5]. KB-D contradicts both: it is not an addition to the stated
   access but the replacement of its readout.
**Result:** no premise at L supplies KB-D, and the stated readout excludes it. Sourcing KB-D is OPEN; on the
present access it is ruled out.

**What G5 does and does not give.** It gives a classical construction meeting the owner's Discrete test exactly
— a concrete instance of the owner's caveat that success there "establishes neither the second nor a unique
selection of quantum theory over classical constructions". It does not give the Continuous target: its body is a
polytope and its reversible group is finite (NOTES-O3 §3).

## 4. What a genuine Discrete Origin would have to supply

From O1-T5 and the table: a reachable state on which the native path record disturbs something a later
operation reads, together with a reversible operation producing that state from a frame state. On the
configuration carrier this is coherence (non-monomial operations); field-neutrally it is invasive observation of
complementarity type. The stated substratum supplies neither: its operations are permutations and phases, its
readout is passive. **The Discrete Origin therefore needs an added premise, and the premise must change either
the operation class (a non-monomial operation — every known instance fails the disguise test) or the observation
law (KB-D-type invasiveness — not sourced).**

## 5. Classification (§A.31)

- **NEW, O2-N1.** The link coupling (A3–A6) is a permutation of configurations even with full gauge covariance
  [X A36]; the only non-monomial structure attached to it in the corpus is the reconstruction's complex
  representation theory, downstream of the input E1.
- **NEW, O2-N2.** The unistochastic lift's coherent branch is not fixed by the stochastic data, and the
  substratum's own statistics coincide with the dephased branch [X G4]: the lift supplies exactly the coherence
  the witness measures.
- **NEW, O2-N3.** The only monomial-input construction passing the witness (G5) needs an observation law that
  replaces, rather than extends, the stated readout; four candidate OI sources of it are closed.
- **CONFIRMING, O2-C1.** G1–G3 as the kernel's own module headers state them (hypothesis, flow predicate,
  postulated datum).
- **Fixed point.** After G5's four branches no new mechanism class appeared (the charter's list A1–A6, link
  coupling, ancilla readback, coarse-graining/time averaging and closure is exhausted, and the passing
  constructions are classified by where their coherence enters).
