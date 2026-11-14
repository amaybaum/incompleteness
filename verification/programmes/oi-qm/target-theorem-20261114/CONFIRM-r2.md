# Confirmation review of TARGET-THEOREM-r2

**Verdict: ACCEPT WITH CHANGES.** B1–B3 and S1–S12 are resolved as `RESPONSE-r1.md` reports, and
the modified and declined dispositions are correct on their merits. Six changes remain (C1–C6),
none blocking: one hypothesis cell understates and mis-cites its source (an error carried from my
own S2), one sentence attaches #1216 to the wrong candidate, and four questions still lack a
pointer to a recorded position. Exact replacement text is given for each.

**Method.** Read-only, paper-only, as in `REVIEW-r1.md`. New r2 text was checked at
`wt-mainread` (`c3b5f37a`), `wt-bellplan` (`a0fa2502`) and the Issue bodies of #1236, #1169, #875,
#1216, #899, #1060, #914. No Lean build, no computation. "Reading" marks hand composition.

***

## 1. Dispositions checked

| # | RESPONSE disposition | r2 does it | Correct at source |
|---|---|---|---|
| B1 | applied | yes: T3 statement restricted to (a)–(c); (d⇒), (d⇐) stated on their own predicates; D2 added | yes. D2's GR:274 is a real boxed `⟺` with the same left side; see C6 for wording |
| B2 | applied, modified | yes | yes, and the modification is right: `D_imp_Qfb` (OB/Equivalence.lean:294) concludes `QfbRealizable` with basis `V × Hid`, not membership in Q^(d,m)_K. My r1 wording was too strong |
| B3 | applied, mapping modified | yes: §1.3, §3 R1–R9, questions rephrased | yes. Declining to file T2 under PG's notion B as sourced is right (PG:216 quoted correctly). Residue: C3 |
| S1 | applied | yes, T0 | yes, except the hypothesis cell: C1 |
| S2 | applied | yes | partly: C1 |
| S3 | applied | yes: O1 narrowed, O5, O7–O9 | yes; quotations at M:486, :492, :496, :638, :644 and RM:73 match |
| S4 | applied | yes | yes; #1061, #1032, #913, #1147, #945, #1059, #872, #1007, #1055 titles match; "#914 (O-CTX)" and "#866 (O-OBSMU)" match the #914 block and `observer-interface-source.md`:4 |
| S5 | applied | yes | yes |
| S6 | applied | yes | yes |
| S7 | applied | yes | yes; one addition available, C4 |
| S8 | applied | yes: "posited" | yes |
| S9 | applied | yes | yes |
| S10 | applied, modified | yes | yes: "bare" does not occur at M:562; M:356 and GR:240 are the right cites |
| S11 | applied | yes | yes, except one verb: C5 |
| S12 | applied, modified | yes | yes, and the modification is right: M:381 does not say which of (ii)–(iv) fails, and my accuracy remark had no source. (iv) is at M:372–373, as cited |
| N1–N12, N14 | applied | yes | yes: `permTheory_dense_ceiling` :187, `qm_iff_derivedOI_pairFlowSourced` :199 (statement `ExactAll T ↔ DerivedOI T ∧ PairFlowSourced T`), Sub:145 (A3–A6), S4:3 all match |
| N13 | declined | — | correct: neither r1 nor r2 takes a Main line from #914 |

## 2. New text checked (§A.34, one direction at a time)

- **T0.** (iii) ⇒ (ii) and (ii) ⇒ (iii) each have their own [P] witness (M:628); the status "neither
  is formalized in the kernel" is quoted exactly; (i) is correctly kept out of the biconditional
  and M:632 is correctly placed against (i) ⇒ (ii). The companion's [K] scope and its two
  unformalized steps match M:600 (2) and M:608.
- **§3 records.** Every quotation in R1–R9 was found verbatim: PG:40, :515–517, :521, :634; #914 §1;
  #875 (a)–(d) and "These decisions fix the screening criteria only"; #1216; #1169 ("construct-
  then-reduce", the Gate A sentence, the 2026-11-07 clarification); #1236's owner decision of
  2026-11-11 (both sentences); M:402–404 and M:416 for R7; BL/STATUS-LADDER.md:37–44 for R8; #899
  for R9. The limits stated (memo unread; #1273 not read at source; no owner comment traced for
  Level B) are accurate.
- **T2, T4, T5 rows.** Completeness/soundness labels are consistent across T2, T4b and T5c. T5a's
  split of the phase ceiling (every nonempty carrier) from the control ceilings (two-state) is
  as the kernel states it.
- **Neutrality.** No candidate is recommended; no assessment of OI.

***

## 3. Remaining changes

### C1 (should-fix). T1 (⇐) and T0 (ii) ⇒ (iii): the independent-prior form is proved for arbitrary real kernels, at M:518

*Source.* M:518, "*Extension (arbitrary kernels — the response-table form).* The rationality
restriction is a property of the uniform-tape presentation, not of realizability. … with product
prior $\mu(u) = \prod_c \mathrm{kern}_c(u_c)$ … the prior is a product and independent of $X_0$ …
The chain rule then reproduces the full multi-time joint for arbitrary real kernels … The
characterization below therefore quantifies over general finite-horizon laws." M:520: the
rational case uses a prior "uniform on" the tape. r2 gives "[P] for rational conditional kernels
(M:516)" as the scope of the independent-prior form and cites the status table M:731 for the
extension. That understates the [P] result; I proposed the wording in S2 without having read
M:518.

*Replace* the T1 (⇐) Hypotheses cell with:

> with a hidden prior independent of the visible initial state: [P] for arbitrary real kernels,
> by the response-table form, whose product prior carries the kernels' values (M:518; "a product
> prior carrying the quantum conditionals", M:600); with the uniform-tape prior, for rational
> conditional kernels (M:516, M:520). "The rationality restriction is a property of the
> uniform-tape presentation, not of realizability" (M:518). With the uniform hidden prior of
> ledger (iv) (M:58) the kernels are rational ("Rationality tracks the prior", M:516), so (⇐)
> then covers rational-kernel laws only (reading)

*Replace* the T0 (ii) ⇒ (iii) Hypotheses cell with:

> rational conditional kernels with the uniform-tape prior (M:516); arbitrary real kernels by the
> response-table form with a product prior (M:518: "The characterization below therefore
> quantifies over general finite-horizon laws"; M:731)

### C2 (should-fix). T2 header: #1216 is not "the programme of this target"

*Source.* #1216 [I]: "Can one mechanism **derived from OI** approximate the complete accessible
predictions of quantum mechanics to arbitrary finite precision? The mechanism uses finite
deterministic dynamics and **independently justified observer access**"; Unit 1 question 1: "Do
Main's existing approximation results meet Level A?"; "A preloaded table of quantum predictions
could satisfy Level A without explaining anything." M:580: in R, "Quantum mechanics enters as the
instrument data and as the state held in the hidden register".

*Replace* the second sentence of the T2 header with:

> #1216 [I] holds the approximate question, for "one mechanism derived from OI" with
> "independently justified observer access"; its Unit 1 asks whether Main's results, this T2, meet
> its Level A (any specified finite experiment within ε), and its Level B asks for one reusable
> mechanism and rule family. T2's R is a constructed realization that runs quantum instruments
> (M:580); whether it is a mechanism in #1216's sense is that Issue's question, and the native form
> is T5c.

### C3 (should-fix). Four questions lack a pointer to a recorded position

*Sources.* #1236 [I], owner decision of 2026-11-11, verbatim: "The third possibility is especially
important. I do not want us to assume that finite observational access necessarily means finite
underlying dynamics." and "The goal is not simply to add continuous mixing to OI. It is to
determine whether continuously tunable quantum behavior can arise from OI's existing principles …
without introducing an independently postulated quantum rule." #1169 [I]: "a proof that assumes
Hilbert spaces, arbitrary unitaries, quantum instruments or the Born rule from the outset is a
**conditional reconstruction/embedding**, not a physical derivation of them from OI"; Gate B,
Meas-1: "**Born frequencies derived from the stated extension**, not silently inserted"; "Both
directions matter: cover the quantum target and account for every operation the proposed physical
OI interface admits."

*Edits.*
- R6, "What it fixes": append `; "I do not want us to assume that finite observational access
  necessarily means finite underlying dynamics"; the question is whether tunable behaviour can
  arise "without introducing an independently postulated quantum rule"`. "Bears on": append
  `; questions 2 and 8`.
- R5, "What it fixes": append `; "a proof that assumes Hilbert spaces, arbitrary unitaries,
  quantum instruments or the Born rule from the outset is a conditional reconstruction/embedding,
  not a physical derivation"; candidate requirement Meas-1 asks for "Born frequencies derived from
  the stated extension"`. "Bears on": append `; questions 7, 9 and 13`.
- §7, first line: replace with `Questions 1, 2, 4, 6, 7, 8, 9, 10, 12, 13 and 14 have recorded
  partial answers or positions (§3); for those the choice is to keep, narrow or supersede the
  record.`
- Question 2: append `(R6 records the owner's position on finite access against finite underlying
  dynamics; #1007 and #1055 [I] carry the question.)`
- Question 7: append `(R5: with the kinematics assumed, #1169 labels the result a conditional
  reconstruction/embedding.)`
- Question 9: append `(R5: "account for every operation the proposed physical OI interface
  admits".)`
- Question 13: append `(R5 and R6 list Born probabilities and Kochen–Specker contextuality as
  obligations of #1169 and TUNE-1.)`

### C4 (nit). T5c, soundness at interface level: the hypothesis follows from the row's other hypothesis

*Source.* `krausSoundExt_of_implementationGenerated`, OB/ImplementationLocality.lean:963:
`ImplementationGenerated T 𝓘 → KrausSoundExt T` on a nonempty carrier. `DerivedOI`'s first
conjunct is `ReversibleImplementationLocality T` (OB/RouteB.lean:146), which is
`∃ 𝓘, ImplementationGenerated T 𝓘 ∧ …` (OB/MicroscopicReversibility.lean:223). `KrausSoundExt`
(OB/CompositeSoundness.lean:123) is stated at positive ancilla levels.

*Replace* the Status cell with:

> a hypothesis (`KrausSoundExt`) of `denseFiniteQM_of_denseControl`, OB/DenseInstrumentBridge.lean:496,
> not a conclusion of it; under that theorem's other hypothesis `DerivedOI` it follows at positive
> ancilla levels from `krausSoundExt_of_implementationGenerated`, OB/ImplementationLocality.lean:963,
> through the first conjunct (reading; not a named theorem)

### C5 (nit). D1: M:588 says "structural architecture", not the conditions

*Replace* "M:588, GR:260 (…) and RD:320–322 state that it supplies them, and the kernel proves"
with:

> M:588 ("the concrete OI substratum supplies the structural architecture"), GR:260 ("the concrete
> substratum supplies every structural requirement of quantum mechanics but not continuous
> state-mixing controllability") and RD:320–322 state that it supplies the structural part, and
> the kernel proves

### C6 (nit). D2: GR:274 cites typed theorems; its gap is inherited

*Replace* D2's last sentence with:

> The two kernel statements cited at GR:258 are on different predicates (T3 (d)), so that display
> is stronger than its cited witnesses (§A.34); GR:274 has the same left side and cites the typed
> determination theorems, which relate the endomorphic shadow to the typed theory and do not
> supply the missing direction.

***

## 4. Is r2 safe to choose a target from

- **No status stronger than its support:** yes. The only status found off its source is weaker
  than the source (C1, C4).
- **No recorded decision presented as open:** yes for decisions on the target (R1–R9). Four
  questions touch recorded positions without saying so (C3); with C3 applied this holds throughout.
- **No candidate recommended:** yes.

## 5. Limits

As in `REVIEW-r1.md` §5. In addition: #875's memo, #1273 and the comments of every Issue were not
read; C4 is a hand composition of three kernel statements.
