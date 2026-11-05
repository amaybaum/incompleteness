# OI-QM-SEL M-2: the C-pers record class (preregistration draft)

**Status: DRAFT r3, NOT FROZEN. WIP / UNVERIFIED.** This file prepares definitions, controls and a decision rule
only.
- No evaluation is made. No law is computed for any pair, and nothing here states or bounds the separating power of
  C-pers. The control K-P (§6.1) is a known-answer check of the law on two single control lifts, not an evaluation.
- The test instance is a placeholder (§4). It is bound only to the M-1 instance and outcome as independently checked.
- Independent review: r1 (`f737fe0e`) received ACCEPT WITH CHANGES, recorded as PR #1149 comment 6665799329. Its
  delta review of r2 (`7ff0c180`) received ACCEPT WITH CHANGES, recorded as PR #1149 comment 6665974132. r3 applies
  its items (change log at the end). A further delta review is pending. Merge is not authorized.

**Writer:** `writer-m2`. **Issue:** #1143 (OI-QM-SEL), unit M-2 of the selection-target specification.
**Base:** `origin/main` `f051916a113c9412b3efbb1ff813ec57c2ed265d`. Every path:line below is read at this base.
**Method:** reading only, plus the hand reasoning for K-P written in §6.1. No script, CAS, numerical evaluation, search
or Lean work. No law is evaluated on any candidate instance.
**File name:** `PREREG-DRAFT.md` until the freeze, which renames it to `PREREG.md` (§7.1, §9).

**Abbreviations.**
- `R/` = `verification/programmes/oi-qm/reconstruction/`.
  - B4 = `R/bsel-2-b4prime-20261105/B4PRIME.md`; SC = `R/bsel-2-b4prime-20261105/SCOPE.md`.
  - RES = `R/bsel-2-q2a-ce-20261105/RESULT.md`; QP = `R/bsel-2-q2a-ce-20261105/PREREG.md`.
- Kernel modules under `verification/lean-mathlib/OIBridge/`: TSG `TwoSidedGauge.lean`, CLG `CoherentLiftGauge.lean`,
  DC `DilationChoice.lean`, CF `CancellationFork.lean`, RC `RootedClassification.lean`, RCAT
  `RootedClassificationAllTime.lean`.
- SPEC = the #1143 selection-target specification r3, #1143 comment 6665278924; SREV = its independent review record,
  #1143 comment 6665288579. Both are off `main`. The SPEC passages this record relies on are quoted verbatim in
  Appendix A (§10).
- REV1 = the independent review of this draft's r1, PR #1149 comment 6665799329; REV2 = its delta review of r2, PR
  #1149 comment 6665974132.
- M-1 = the separately authorized verification of the alternating-`W` candidate, tracked on PR #1151.

***

## §0. Authorization

Owner ruling, recorded at #1031 comment 6665461411 (posted 2026-11-05T18:05:55Z, edited 18:14:44Z) as amaybaum, Claude
Code session chat, 2026-11-05 (before 18:05Z), and pointed to from #1143 comment 6665466217. The M-2 item, quoted
verbatim from #1031 c.6665461411:

> **M-2.** Prepare the C-pers paper-only study in parallel: configuration-only preparation; two visible-system reads; persistent ancilla; no imposed coherence or reset. Its definitions and controls may be prepared now. Evaluate its separating power after the M-1 instance and outcome are independently checked. If M-1 fails, do not silently substitute another pair. Independent review is required for each result. This authorizes only the bounded mathematical work, not a native physical experiment.

The same comment's table reads: "#1143 M-2 | Approve preparation now and paper-only evaluation after M-1 establishes the
test instance".

**What this draft does:** fixes the C-pers definitions, its complete-record law, the target-QM comparison, the controls
and the decision rule.

**Not authorized here:** evaluating separating power; binding or computing any instance; substituting a pair; a native
physical experiment; Lean work; numerical search; theorem promotion; manuscript edits; merge.

## §1. Definitions taken from `main`

Definitions only. No [D] result of B4 or RES is used as a premise (§A.46 item 7).

- **Carrier.** `V × A`, `|V| = n ≥ 2`, fixed anchor `a₀ ∈ A`; `e_v := e_{(v,a₀)}`; `𝒜 := span{e_v}`; `C := 𝒜^⊥`;
  fibre projector `P_w := |w⟩⟨w| ⊗ 1_A` (B4 ll. 33–34; SC l. 102).
- **Lift.** `U = (U_t)_{t∈ℕ}`, each `U_t` unitary on `ℂ^{V×A}` (B4 l. 35; SC ll. 109–111).
- **Relative object.** `T_{t,s}(U) := U_tU_sᴴ` (B4 ll. 41–43; CF:123–129).
- **Readback.** `Γ_t(w,v) := ‖P_wU_te_v‖²` (DC:86, DC:134–136; B4 l. 40). Relative readback
  `𝒪₂(t,s)(w,v) := ‖P_wT_{t,s}e_v‖²` (`RelativeCandidate`, CF:123; `relativeCandidate_apply`, CF:128).
- **Gauge.** `LeftFibreGroup` (TSG:78–79); `WeakAnchorStabilizer a₀` (CLG:114–116), with `|c_j| = 1`
  (`weak_anchor_coeff_norm_one`, CLG:146); `G(U,U′)` is `TwoSidedRelated a₀ U U′` (TSG:84–87).
- **Class `PPer`.** `Γ 0 = 1`, `IsRowStochastic (Γ t)` for every `t`, and a positive finite period (RC:32–33). The
  readback is column-stochastic (`readback_isColStochastic`, DC:93). Every `PPer` statement states and checks its
  orientation (SC W9).
- **Procedures** (SC ll. 112–119, frozen there):
  - P-conf: root `|j,a₀⟩ = e_j`, each `j ∈ V` separately, laws indexed by `j`.
  - Rd: the Lüders read `P_v` with record `v`.
  - H-comp: from the root to the first read at `s`, the state evolves by `U_s`; between reads at `s < t`, by
    `T_{t,s}`.
  - Acc₂: a finite increasing read list, all records kept jointly.
- **Reading (r1)** (B4 ll. 58–60): the state at a read at `t`, from the root, is `U_t` applied to the root preparation.
- **Complete-record law and `O_C`** (SC ll. 24–25): `Λ_C` is every branch mass and every failure record `⊥`,
  unnormalized and unconditioned; `O_C(U,U′)` is `Λ_C(U) = Λ_C(U′)`.

## §2. The C-pers record class (frozen at the freeze commit; draft now)

**C-pers = (P-conf, Acc_pers, Rd, H-comp, Rst-none).**

| Element | Definition |
|---|---|
| Preparation | P-conf only: the root `e_j`, for each `j ∈ V`, separately. No P-coh, no `ρ₊`, no superposition and no mixture is prepared. No `prior` mixes the per-`j` laws (SC W5). |
| Access, Acc_pers | Exactly two reads, at times `s < t`, `s, t ∈ ℕ`. Every such pair is a procedure. Both records are kept jointly. |
| Reads | Each read is Rd, the Lüders read `P_v = \|v⟩⟨v\| ⊗ 1_A`. It acts as the identity on `A`. |
| Evolution | H-comp: `U_s` from the root to the first read; `T_{t,s} = U_tU_sᴴ` between the reads. |
| Ancilla | Persists. Between and after the reads nothing acts on `A` except `U_s` and `T_{t,s}`. |
| Reset | None, called Rst-none. No ancilla replacement (Rst-ch), no `\|a₀⟩⟨a₀\|` test (Rst-sel) and no other test is applied. |
| Imposed coherence | None. The only coherence the post-read state carries is what `U_s` and `T_{t,s}` produce from the root `e_j`. No phase reference is chosen apart from the lift. |
| Decoder | The record pair `(v₁, v₂)` itself. No other function of the records is read. |

**Readings fixed here.**
- **(p1)** The evolution clause is (r1) together with H-comp. Read as a statement about QM, it is reading (t2) of §5.
- **(p2)** "Two visible-system reads" is read as exactly two reads. Single reads and lists of length `k ≥ 3` are not
  C-pers procedures. A result for them is out of scope and is not used to rescue an outcome (§A.29). REV1 (N3) notes
  that "at most two" would give the same relation, since single-read data are the L-2 marginals; only "at least two"
  would change the class.
- **(p3)** `s = 0` is admitted. The read times range over all of `ℕ`. A claim is not restricted to a horizon.
- **(p4)** Since no test is applied, no `⊥` record exists. The record alphabet of the procedure `(j; s, t)` is
  `V × V`.

## §3. The complete-record law `Λ_C-pers`

**Branch masses.** For the procedure `(j; s, t)`, `s < t`, the record `(v₁, v₂) ∈ V × V` has the unnormalized mass

  `p_U(v₁, v₂ | j; s, t) := ‖ P_{v₂} · T_{t,s}(U) · P_{v₁} · U_s · e_j ‖²`.

Equivalently, `Σ_{a∈A} |⟨(v₂,a), U_tU_sᴴP_{v₁}U_se_j⟩|²`. The vector `P_{v₁}U_se_j` keeps every ancilla component; it is
not renormalized, reset or projected onto `a₀`.

**`⊥` masses.** None: the set of failure records is empty for every procedure (p4). This is a definitional consequence
of Rst-none, stated so that a reviewer can check it, not a computed result.

**The law.** `Λ_C-pers(U) := ( p_U(v₁, v₂ | j; s, t) )` over `j ∈ V`, `s < t` in `ℕ` and `(v₁, v₂) ∈ V × V`.
`O_C-pers(U, U′)` holds iff `Λ_C-pers(U) = Λ_C-pers(U′)` entrywise.

**The reset form.** For comparison, `r_U(v₁, v₂ | j; s, t) := Γ_s(v₁, j) · 𝒪₂(t,s)(v₂, v₁)`. By B4 W0.4 (a [D] result,
used as a cross-check only) it is the two-read C2-ch law.

**Obligations for the evaluation record** (not discharged here):
- **L-0 (law from procedures).** Re-derive the displayed mass from P-conf, H-comp and two Lüders reads, by explicit
  unnormalized branch states, as QP §3 K-b did for C0 and C2.
- **L-1 (bookkeeping).** For each `U`, `j` and `s < t`, the masses sum to 1 over `V × V`.
- **L-2 (marginal).** The marginal of `p_U(·,·|j; s,t)` over `v₂` equals `Γ_s(·, j)`. This is used by K3.
- **L-3 (`|A| = 1` reduction).** At `|A| = 1`, `p_U = r_U` for every record, the two-read case of B4 W0.4. This is used
  by K2.

L-0 to L-3 are stated before evaluation so that their failure is detectable. If any one cannot be derived, the outcome
is VOID (§7). REV1 reports that L-1 to L-3 hold symbolically. That report is provenance; the evaluation record derives
them itself.

## §4. The test instance (placeholder; not filled)

**Instance slot `I_M1`: the M-1 instance and outcome, as independently checked.**

This slot holds no pair. It is filled only by a binding amendment (§7.1), which copies verbatim from M-1's record:
- the lifts `U`, `U′`: every slice, its placement in `t`, `|V|`, `|A|`, the anchor and the basis order;
- M-1's verdict and its scope;
- M-1's reported C0, C2-ch and C2-sel laws for the pair;
- the commit on `main` that holds M-1's record, and the location of its independent review.

**Gate G-M1: what the slot requires of M-1.** M-2 is evaluated only if all of the following hold:
1. M-1's record is on `main`, and its independent review is recorded.
2. M-1's checked outcome establishes, for its frozen pair, each of:
   - (a) equal C0 laws;
   - (b) that the lifts are not `G`-related;
   - (c) that the lifts are T-V-distinct (§5);
   - (d) that the visible family `Γ` lies in `PPer`, with the orientation checked.
3. The instance bound is exactly M-1's frozen pair, character for character.

G-M1 is the single route by which (a)–(d) enter this record. They are taken from M-1's independently reviewed record
(§A.46 item 7), and K5 does not re-derive them.

**If G-M1 fails** (M-1 is VOID, does not establish any of (a)–(d), or is not independently checked): M-2 is not
evaluated, and its outcome is NOT-EVALUATED (§7). No other pair is substituted. A different instance needs a new owner
decision, recorded before any law of that instance is computed.

**Not done here.** No law of any candidate instance is computed, estimated or discussed. The spec's candidate F4 (SPEC
§0) is named only as the pair M-1 is authorized to verify; this draft depends on no property of it.

## §5. The target-QM comparison (T-V)

SPEC §1.4 is quoted verbatim in Appendix A.1. The T-V used here is that text together with two readings of this
record's own, (t1) and (t2), which SPEC §1.4 does not state.

**T-V.** QM on `V`, with `A` an inaccessible environment in `|a₀⟩` at the root.
- **Preparations:** every density matrix `ρ ⊗ |a₀⟩⟨a₀|`, `ρ` on `ℂ^V`.
- **Readouts:** every finite instrument on `V`, acting as `𝓘_r ⊗ id_A`. A Lüders read `P_v` is the instrument
  `ρ ↦ |v⟩⟨v|ρ|v⟩` on `V`.
  - **(t1), this record's reading.** Readouts include every finite sequence of such instruments at increasing times.
- **Dynamics:** the lift. Every branch mass is kept, unnormalized, and `A` persists between reads.
  - **(t2), this record's reading.** `U_t` is the cumulative propagator from the root to `t`. Between reads at `s < t`
    the state evolves by `U_tU_sᴴ`.
- **`O_T-V(U, U′)`:** equality of all T-V branch masses.
- **T-V-distinct:** `¬O_T-V(U, U′)`.

**Excluded comparators.** T-full (arbitrary QM procedures on `V ⊗ A`) does not count. T-V+R (a declared ancilla reset)
applies only to C2-ch and C2-sel, not to C-pers.

**Relation fixed in advance.**
- **D-1 (by construction, under (t1) and (t2)).** The C-pers procedure `(j; s, t)` is the T-V procedure with
  `ρ = |j⟩⟨j|` and Lüders reads at `s` and `t`. So `Λ_C-pers(U)` is a subfamily of `Λ_T-V(U)`, and
  `O_T-V ⇒ O_C-pers`. The evaluation record writes this out (K5).
- **What M-2 decides.** On the bound instance, which M-1 has shown T-V-distinct, whether C-pers is one of the T-V
  procedure classes that separate it.
- **What M-2 does not decide.** Whether native OI access supplies C-pers. Whether T-V and C-pers agree on any other pair.

## §6. Controls

Identifiers follow SPEC §4.6 where a control corresponds to one there; K2 is this record's own (see its row). All pass
criteria are fixed now. The evaluation record writes out every derivation.

| ID | Control | Pass criterion |
|---|---|---|
| K1 | Positive gauge control | For the bound `U` and `L := 1_V ⊗ H₂` on `{a₀, a₁}` (identity on further labels), constant in `t`, `Λ_C-pers(LU) = Λ_C-pers(U)` for every record. `(U, LU)` is `G`-related (TSG:84). A difference makes the outcome VOID. |
| K-B | Invariance of the law | The record derives, for every lift, that `Λ_C-pers` is unchanged by (i) any time-dependent `L_t ∈ 𝒢_L` and (ii) any constant weak `K`. It states that no step uses an `a₀` reset frame. Failure makes the outcome VOID. |
| K2 | `\|A\| = 1` countercontrol and reset-form cross-check | **This record's own; it differs from SPEC K2.** SPEC K2 asks that a statistic agree on every `\|A\| = 1` equal-`Γ` pair. Read literally it would fail for C-pers, which at `\|A\| = 1` separates WD, a `G`-related pair with equal `Γ` (B4 ll. 310–315; REV1 M4). Pass iff both hold: (i) L-3; (ii) on the instance, the record evaluates `r_U` and `r_U′` for every record `(j; s, t; v₁, v₂)` over one period of the slices (K-H), and they equal M-1's reported two-read C2-ch law for the same records. M-1's law is accepted either as masses or as the factors `Γ_s` and `𝒪₂(t,s)` (B4 W0.4); in the second case the comparison is factor by factor. A mismatch makes the outcome VOID. If M-1's record states neither form, (ii) is vacuous and the outcome is VOID. |
| K3 | Fixed-basis control | L-2 holds, and on the instance the C-pers marginals of both lifts equal the C0 laws M-1 reports. |
| K5 | Re-derivation | The record re-derives L-0 to L-3, D-1, K11's witness WD and K-P's values (§6.1). No B4 [D] or RES result is a premise. The instance facts G-M1 (a)–(d) enter through G-M1 only (§4). |
| K7 | Masses | No normalization, no conditioning and no postselection. The empty `⊥` set is stated. L-1 holds. |
| K9 | No imposed coherence | Roots are `e_j` only. No P-coh, `ρ₊` or phase is chosen apart from the lift. No reset. The ancilla's coherence enters only through `U_s` and `T_{t,s}`. |
| K10 | Adjustability | Every freedom left open (a reading, a read pair) is listed. The outcome is reported for every admissible value. An outcome that changes across them is UNDECIDED. |
| K11 | Positive sensitivity (SPEC K11, C-pers) | WD (B4 ll. 309–315): `U` = alternating `H₂`, `g` with `L ≡ 1`, `K_1 = Z`, `K_t = 1` otherwise; at the instance's `\|A\|` it is placed on `𝒜` with `⊕ 1_C`. The record computes both laws from §3 and finds some record with unequal masses. B4's stated values are not premises. |
| K-P | Retention of ancilla coherence | §6.1: exact values on the lifts `U^C` and `U^P`. |
| K12 | Device identity | Only `U ↦ U′` changes: the same roots, read pairs, projectors, anchor and decoder. |
| K13 | Joint-lift nativeness (conditional) | The instance's visible family is in `PPer`, orientation checked, as G-M1 (d) supplies. C-pers adds no preparation interaction, so the joint process is the lift itself. Reading "in `PPer`" as "native" is CONDITIONAL[F3's hypothesis that native realizations are finite `RootedRealization`s (RCAT:192–194); S-0]. Without both, K13 is a necessary check only. K13 is reported with every outcome. |
| K-D | Same `Γ` | The instance has equal `Γ_t` for every `t` (from M-1 through G-M1). |
| K-H | ℕ coverage | Every equality claim covers every `s < t` in `ℕ`, by eventual constancy or eventual periodicity of the slices `U_t` and `U′_t` (not of `Γ`), never by a horizon. |

**Not applicable at the paper level, kept for any native study.** SPEC K4 (hidden common cause), K6 (private decoder)
and K8 (carrier change) concern a physical setting variable and decoder. Here the laws are per `j`, no setting is
selected, and the decoder is the record (§2). They are re-imposed on any native realization, which is not authorized.

### 6.1 K-P: retention of ancilla coherence (fixed at the freeze)

**Purpose (REV1 M1; delta review D1).** The reset form `r_U` satisfies L-1, L-2, L-3, K2 (i), K3 and K11, and K11's WD
keeps every state in `𝒜`. A computation that dropped the ancilla after the first read would therefore pass every other
control, and DOES-NOT-SEPARATE could be reached in error with every control green. Three ways of dropping it are
distinguished:
- **(R)** reset to `|a₀⟩`, as Rst-ch does, which gives `r_U`;
- **(D)** dephasing the ancilla in the basis `{|a⟩}` after the read;
- **(A)** projecting onto `a₀` without renormalizing, as the Rst-sel ok branch does.

K-P fixes two control lifts, each with one procedure and exact known values. K-Pc separates C-pers from (R), (D) and
(A). K-Pp separates it from (R) only. Together they show that the computation retains ancilla coherence on the K-P
lift `U^C`, and ancilla populations on `U^P`. They show nothing more.

**Common notation** (`|V| = 2`, `|A| = 2`). Basis order `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`, with
`e₀ = p₀` and `e₁ = p₂`.
- `L := 1_V ⊗ H₂` on `{a₀, a₁}`, as in K1. It is real symmetric and unitary, so `Lᴴ = L`, `Lp₀ = (p₀+p₁)/√2` and
  `Lp₁ = (p₀−p₁)/√2`.
- `Q :=` the permutation matrix exchanging `p₁` and `p₂`, so `Qp₀ = p₀`, `Qp₁ = p₂` and `Qp₂ = p₁`.
- **The procedure, for both lifts:** root `j = 0`, reads `(s, t) = (0, 1)`.
- **The first read, for both lifts:** `U_0 = L` gives `U_0e₀ = (p₀+p₁)/√2`, which lies wholly in fibre 0. So
  `Γ_0(0,0) = 1`, and the unnormalized post-read state is `x := P₀U_0e₀ = (p₀+p₁)/√2`.

Neither lift is one member of a pair. No class membership is claimed for either, and neither is related to the M-1
pair. The values below are reasoned from the definitions ([D-draft], unreviewed), and K5 re-derives them.

**K-Pc: the coherence lift `U^C`.** `U^C_0 := L` and `U^C_t := Q` for every `t ≥ 1`, so `T_{1,0} = QLᴴ = QL`.
- **C-pers:** `Lx = (Lp₀ + Lp₁)/√2 = ((p₀+p₁) + (p₀−p₁))/2 = p₀` and `Qp₀ = p₀`, so `p_{U^C}(0, 0 | 0; 0, 1) = 1`.
- **(R), reset form:** the post-read state is `p₀`, with mass 1. Then `QLp₀ = Q(p₀+p₁)/√2 = (p₀+p₂)/√2`, whose fibre-0
  part has mass ½. So `r_{U^C}(0, 0 | 0; 0, 1) = 1 · ½ = ½`.
- **(D), dephased:** the state is `½|p₀⟩⟨p₀| + ½|p₁⟩⟨p₁|`. `QLp₀ = (p₀+p₂)/√2` and `QLp₁ = Q(p₀−p₁)/√2 = (p₀−p₂)/√2`
  each have fibre-0 mass ½. So the mass is `½·½ + ½·½ = ½`.
- **(A), projected onto `a₀`:** `⟨p₀, x⟩p₀ = p₀/√2`, and `QL(p₀/√2) = (p₀+p₂)/2`, whose fibre-0 part `p₀/2` has mass ¼.
- **Mechanism:** the value 1 needs the relative phase of the `p₀` and `p₁` components of `x`, which `L` recombines into
  `p₀`. (R), (D) and (A) each destroy that phase.

**K-Pp: the population lift `U^P`.** `U^P_0 := L` and `U^P_t := QL` for every `t ≥ 1`, so `T_{1,0} = QLLᴴ = Q`.
- **C-pers:** `Qx = (p₀+p₂)/√2`, whose fibre-0 and fibre-1 parts each have mass ½. So `p_{U^P}(0, 0 | 0; 0, 1) = ½` and
  `p_{U^P}(0, 1 | 0; 0, 1) = ½`.
- **(R), reset form:** `𝒪₂(1,0)(0,0) = ‖P₀Qp₀‖² = ‖p₀‖² = 1`, so `r_{U^P}(0, 0 | 0; 0, 1) = 1 · 1 = 1`.
- **(D), (A):** dephasing gives `½·‖P₀Qp₀‖² + ½·‖P₀Qp₁‖² = ½ + 0 = ½` at `(0,0)`. Projection gives `Q(p₀/√2) = p₀/√2`,
  mass ½. Both equal the C-pers value, so K-Pp does not detect (D) or (A). It detects only the loss of the ancilla's
  population that (R) causes.

**Pass criterion (fail-closed).** K-P passes iff the evaluation record derives the following exact values from §3, by
explicit branch states, using the same written procedure it uses for the instance:
- for `U^C` at `(0,0 | 0; 0,1)`: `p = 1` and `r = ½`;
- for `U^P`: `p(0,0 | 0; 0,1) = ½`, `p(0,1 | 0; 0,1) = ½` and `r(0,0 | 0; 0,1) = 1`.

Any other value, a missing derivation, or a procedure for `p_U` on the instance that differs from the one applied to
the K-P lifts makes the outcome VOID. The (D) and (A) values are stated to justify the choice of lifts; they are not
pass conditions.

**Scope of K-P, and the alternative scoping of DOES-NOT-SEPARATE.**
- REV1 recommends a pair with equal C2-ch laws that C-pers separates. **No such pair is adopted in this draft.**
  Establishing equality of a pair's C2-ch laws means computing full laws, which this preparation stage does not do.
- K-P shows only that the computation retains ancilla coherence on the K-P lift `U^C`. It does not show that C-pers
  separates any pair the reset classes identify.
- So a DOES-NOT-SEPARATE outcome carries the qualifier **"no persistence-specific pair witness"**. It then means equal
  C-pers laws on the instance, with the computation shown to retain ancilla coherence on the K-P lift. It does not mean
  that C-pers was shown able to separate reset-equal pairs.
- If such a pair `K-P′` is adopted before the freeze, by recorded reviewer or owner direction, it is fixed at `Φ`. Its
  criterion: both C2-ch laws equal and the C-pers laws unequal, each derived in the evaluation record; otherwise VOID.
  The qualifier is then dropped.

## §7. Decision rule (fixed at the freeze; draft now)

### 7.1 Order of work
1. **Definitions review.** Each review is independent. Changes it requires are made before the freeze, with a change
   log (this file's end).
2. **Freeze `Φ`.**
   - A commit that renames this file to `PREREG.md` and fixes §§1–3, 5–11 and Appendix A, with §4 still a placeholder. It may change
     only the status lines and the edits listed in the change log.
   - Precondition (REV1 N2): either SPEC lands on `main`, or Appendix A quotes verbatim every SPEC passage this record
     relies on. A delta review confirms the list.
3. **Gate.** G-M1 is checked against M-1's reviewed record on `main`.
4. **Binding amendment `B_I`.**
   - A single-parent child of `Φ`, or of a later commit that changes no frozen section. It fills §4 verbatim from M-1
     and changes nothing else.
   - If G-M1 fails, `B_I` instead writes NOT-EVALUATED and its reason inside §4, and changes nothing else.
5. **Evaluation.** `RESULT.md` in this directory, in a later commit that changes no other file.
6. **Independent review** of the result, recorded on the guiding pull request.

### 7.2 Outcomes (closed list; the first that applies is the outcome)
1. **NOT-EVALUATED.** G-M1 fails. No pair is substituted (§4).
2. **VOID.** Any of the following:
   - a control among K1, K-B, K2, K3, K5, K7, K9, K11, K-P, K12, K-D or K-H fails or is vacuous;
   - any of L-0 to L-3 cannot be derived;
   - a definition reads differently from its source line;
   - the bound instance differs from M-1's.
3. **UNDECIDED.** The controls pass, but equality over every `s < t` in `ℕ` cannot be settled by exact hand argument, or
   the outcome changes under a freedom K10 lists. The unproved step is named. A deciding computation is written as a
   proposal and not run.
4. **SEPARATES[C-pers; instance; `|V|`, `|A|`; `PPer`].** The controls pass and some `(j; s, t; v₁, v₂)` has
   `p_U ≠ p_U′`. The record writes out at least one such record with both masses in exact arithmetic. It lists every
   separating `(j; s, t)` up to the period of the slices `U_t`, `U′_t`.
5. **DOES-NOT-SEPARATE[C-pers; instance; `|V|`, `|A|`; `PPer`; no persistence-specific pair witness].** The controls
   pass and `Λ_C-pers(U) = Λ_C-pers(U′)` entrywise, for every `j`, every `s < t` in `ℕ` and every record. The last
   qualifier is dropped only under `K-P′` (§6.1).

K13 is reported with every outcome; its conditional reading does not change the outcome.

### 7.3 Consequences
SPEC §4.3 is quoted verbatim in Appendix A.2. Its "Selection, frozen now" clause reads:

> - If M-2 shows that C-pers separates the instance, the criterion selects C-pers: fewer prerequisites, no posited
>   preparation coherence.
> - Otherwise it selects `C*`.

**This record does not adopt that selection.**
- SPEC §4.4's prerequisite list, which the §4.3 criterion counts, has no row for H-comp. `C*₁` uses a single read,
  while C-pers needs a physical between-read evolution, whose supply is a SOURCING-GAP at #866 (B4 ll. 381–383).
- **This record proposes that, before any native freeze, the selection be re-checked with H-comp counted, by owner
  decision.** The proposal holds after every outcome. Its accountable Issue is #1143.

What each outcome contributes:
- **SEPARATES.** C-pers meets SPEC §4.3's qualification clause on this instance: "A candidate qualifies only after its
  separating power on the instance is established mathematically, through M-1 or M-2". The selection waits for the
  re-check.
- **DOES-NOT-SEPARATE.** C-pers does not qualify on this instance. The finding is scoped to C-pers with exactly two
  reads on this instance, with K-P's qualifier. It is not extended to other read counts, other pairs or other classes.
- **Redo rule** (SPEC §4.3, last paragraph). If M-1's checked outcome reports that C2-ch or C2-sel separates the
  instance, that class enters the comparison.
- **Persistence attribution** (reported, not a pass condition). It is compared per procedure `(j; s, t)`, not per
  record, since C2-sel has `⊥` records. For each separating `(j; s, t)` of C-pers, the result states whether M-1's
  checked C2-ch law, and its C2-sel law, for the read list `(s, t)` from root `j` also differ between the lifts. Only
  a procedure that the reset classes do not separate is attributed to the persistent ancilla.
- **Unchanged in every case.** SPEC's present verdict, UNSOURCED, for every declared interface (Appendix A.3). A
  mathematical separation without sourced access is a scoped gap.

## §8. Scope

**What a SEPARATES outcome would establish:** that, on the bound instance, the C-pers complete-record laws differ, at
the stated `|V|`, `|A|` and class. Read about OI, it is CONDITIONAL[P-conf, Acc_pers, Rd, H-comp, Rst-none with `A`
persisting, fixed `a₀`, (r1), (p1)–(p4), (t1), (t2)].

**What no outcome establishes.**
- Physical availability or native OI realizability of C-pers, or of the instance.
- Physical supply of the prerequisites, each a SOURCING-GAP:

| SPEC ID | Item | Accountable home |
|---|---|---|
| S-0 | A defined `L_native` and a native-realization→lift correspondence | #866 (P0); #914 row 12 |
| S-1 | `(Obs, μ)` and substratum realizations of the instance's `Γ` | #866 O-OBSMU |
| S-2 | Setting independent of the hidden state | #866 O-SET |
| S-4 | Accessible record for Rd | #866 O-REC |
| S-5 | Retained ticks | #914 O-ACC |
| S-8 | Retention of `A` across the two reads (O-RET) | #1032, per the owner ruling in #1031 c.6665461411 |
| — | H-comp as the physical between-read evolution (not in SPEC §4.4) | #866, a SOURCING-GAP by B4 ll. 381–383 |

- Any equivalence or inequivalence of OI and QM, physical or operational.
- Any statement about another pair, another read count or another class.
- A theorem promotion, a Lean statement or a manuscript claim.

## §9. Invariants and their checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| Definitions, controls and rule are fixed at `Φ`, before `B_I` binds the instance, and no C-pers law of the instance is stated in any repository record before `RESULT.md` | `Φ` precedes `B_I`. `git diff Φ B_I --stat` lists `PREREG.md` only, and its hunks lie inside §4, on the failure path as well. A reviewer reads every commit between `Φ` and the `RESULT.md` commit and records that none states a C-pers law of the instance |
| The freeze is the reviewed text | `git diff -M Φ^ Φ` shows the rename `PREREG-DRAFT.md → PREREG.md`, plus only the status lines and the edits the change log lists. The delta review of the last draft is recorded on the guiding pull request |
| SPEC passages relied on are quoted verbatim | Appendix A, checked by the delta review (§7.1 step 2) |
| No pair is substituted | `B_I` quotes M-1's pair verbatim, with M-1's commit and review location |
| M-1 is independently checked before evaluation | G-M1 item 1, checked in `B_I` against `main` |
| Complete-record law, `⊥` set stated | L-0, L-1, K7 |
| No imposed coherence, no reset | K9 |
| Controls green before any outcome other than NOT-EVALUATED, sensitivity included | §7.2 order: VOID, which covers K11 and K-P, precedes UNDECIDED, SEPARATES and DOES-NOT-SEPARATE |
| The computation retains ancilla coherence on the K-P lift `U^C` | K-P (§6.1): exact values on `U^C` and `U^P`, with the same written procedure as on the instance |
| Reset-form cross-check | K2 (ii) against M-1's reported C2-ch masses |
| Device identity | K12 |
| ℕ coverage, no horizon | K-H |
| Not adjustable | K10 |
| K13 reported with every outcome | `RESULT.md` has a K13 line under every outcome heading; the reviewer checks it |
| Persistence attribution reported | `RESULT.md` has a per-`(j; s, t)` attribution table whenever the outcome is SEPARATES |
| The evaluation commit adds the result only | `git show --stat` of the `RESULT.md` commit lists `RESULT.md` only |
| Independent review of the result | Recorded on the guiding pull request before any use of the outcome |
| Verdict reads structured results (§A.44) | No computation; the written decision table of §7.2, evaluated row by row in `RESULT.md` |
| Paper only | `RESULT.md` states the method; the reviewer checks that every value is a written hand computation |

**SPEC pin.** SPEC §4.7's first checkpoint asks for the sha256 of `SPEC.md` to be quoted in the comment that posts it.
c.6665278924 quotes none (finding). As a substitute this draft records the sha256 of the comment bodies as served by
the GitHub API on 2026-11-05, with `created_at = updated_at` for each:
- c.6665278924 (SPEC r3): `92510abc3913cf094bc7c34f6e6cf41c9c3b36f77c983ca9d76654979bcfca2e`;
- c.6665288579 (SREV): `865117425f87ce150f57185423ef60e3dbf3e483cf65ee472d517ea467d233c4`;
- c.6665466217 (M-1/M-2 pointer): `b057a66cd637c8d50aca539f2c791f5fc45d660db19ba15d97927e012daa3df6`.

These digests are of the comment bodies, not of a `SPEC.md` file. They pin what was read; they do not put SPEC on
`main`. REV1 (N2) accepts this substitute.

## §10. Premise ledger (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #1031 c.6665461411; #1143 c.6665466217 | Authorization (§0) | Provenance. An owner designation quoted with author and time (§A.42 item 7) |
| SPEC §1.4 (c.6665278924) | The T-V comparison (§5) | Support off `main`, closed by quotation. The text is quoted verbatim in A.1 and lands with this record. The additions (t1) and (t2) are this record's own readings |
| SPEC §4.3 (c.6665278924) | §7.3: the qualification clause, the selection rule and the redo rule | **Support off `main`.** The text is quoted verbatim in A.2 and lands with this record. Its standing as the reviewed spec rests on SREV, which is off `main`. The gap is closed by narrowing: §7.3 does not adopt the selection, which is re-checked by owner decision before any native freeze |
| SPEC §4.5 "Present state" (c.6665278924) | §7.3: UNSOURCED is unchanged | Support off `main`, closed by quotation in A.3. This record changes no verdict |
| SPEC §4.4 and §4.6 (c.6665278924) | Identifiers S-0 to S-8 and K-numbers; the absence of an H-comp row | Provenance for the identifiers. Every control used is defined in §6 as this record's own. The absence of an H-comp row is a finding about SPEC, recorded in §7.3 |
| SREV (c.6665288579) | SPEC's review status | Provenance |
| REV1 (PR #1149 c.6665799329); REV2 (PR #1149 c.6665974132) | The r2 and r3 changes; the remarks under (p2) and L-3 | Provenance. No claim rests on them |
| B4, SC, RES, QP (on `main`) | Notation, procedures, readings, WD's definition, B4 ll. 381–383 | Support on `main`, for definitions and the SOURCING-GAP assignment only. B4's WD values and every [D] result are not premises (K5, K11) |
| Kernel lines (TSG, CLG, DC, CF, RC, RCAT) | Definitions of §1; K13's conditional reading | Support on `main` |
| M-1's record (PR #1151; `RESULT.md` §3 K-b and §4.3 at `594b5128`) | G-M1 (a)–(d); the instance; K2 (ii) and K3 inputs | Not yet on `main`; PR #1151 is not merged. Its locations are cited in H7 as pointers only. It becomes support on `main` only when landed and reviewed; until then G-M1 fails |
| #866, #914, #1032 | Accountable homes in §8 | Provenance; planning records only (§A.45 rule 1) |

## §11. Hidden-assumption watch (§A.31)

- **H1 (H-comp).** C-pers reads `T_{t,s} = U_tU_sᴴ` as the physical evolution between reads. The kernel's
  `CoherentLift` (CLG:124) is admissibility slice by slice and fixes no between-read evolution. A C-pers result is
  therefore CONDITIONAL[H-comp]. H-comp's physical supply is a SOURCING-GAP at #866 (B4 ll. 381–383). SPEC §4.4 has no
  row for it, which is why §7.3 does not adopt SPEC's selection.
- **H2 (retention).** Rst-none with `A` persisting is the content of S-8. A separation that uses ancilla components of
  `P_{v₁}U_se_j` uses retention. With K-P green, the computation is shown to retain ancilla coherence on the K-P lift
  `U^C`, and populations on `U^P`; nothing beyond those lifts follows. §7.3's attribution reports where a separation
  depends on the ancilla.
- **H3 (no reset frame).** C-pers has no `a₀` reset or test after a read, so SC W3 does not arise for it. The anchor
  still enters through the P-conf roots `e_j`. K-B tests that no step uses a reset frame.
- **H4 (Lüders read).** Rd is a Lüders read that leaves `A` untouched. A read that disturbs `A` defines a different
  class and is not tested.
- **H5 (two reads).** Resolved by REV1 (N3): "exactly two" is kept (p2).
- **H6 (persistence witness).** Resolved by REV1 (M1) and REV2 (D1) through K-P (§6.1). Without a `K-P′` pair, DOES-NOT-SEPARATE
  carries the qualifier "no persistence-specific pair witness".
- **H7 (dependence on M-1's report).** K2 (ii), K3 and the attribution read M-1's reported C0, C2-ch and C2-sel
  masses. If M-1 states the two-read C2-ch law neither as masses nor as factors, K2 (ii) is vacuous and the outcome is
  VOID. M-1's form of report is not changed by this record.
  - M-1's record is PR #1151, not merged. At its head `594b5128` it states the two-read C2-ch masses in `RESULT.md`
    §4.3: the closed form at ll. 123–124 and the two-read table at ll. 126–135. These were delta-checked in #1151
    c.6665968807. `PPer` membership in both orientations is its control K-b (`RESULT.md` §3, ll. 63–82). The later
    head `9a7f9961` changes three status lines only. These are locations, not support: M-1 is not landed, so G-M1
    does not yet hold.

## §12. Review and next steps

- **A delta review of r3** is required before the freeze. It should check the K-P values (§6.1) by hand, K2 (ii), §7.1,
  §7.3, the §9 checkpoints, H7 and the change log.
- **Evaluation** waits for M-1's independently reviewed outcome on `main` (G-M1). If M-1 fails, no other pair is
  substituted without a new owner decision.
- Merge is not authorized.

## Appendix A. SPEC passages relied on, quoted verbatim from #1143 c.6665278924

### A.1 SPEC §1.4, excerpt (T-V and its excluded comparators)

The excerpt omits T-iface, the QM-side uniqueness bullet and the flagged paragraph of SPEC §1.4.

> ### 1.4 The target-QM distinction (fixed before any test)
>
> - **T-V (primary).** QM on `V`, with `A` an inaccessible environment in `|a₀⟩` at the root.
>   - Preparations: every density matrix `ρ ⊗ |a₀⟩⟨a₀|`.
>   - Readouts: every finite instrument on `V`.
>   - Dynamics: the lift. All branch masses are kept, and `A` persists between reads.
>   - C0, C1 and C-pers are T-V procedure classes by construction.
> - **T-V+R.** T-V plus a declared ancilla reset. It is used only when C2-ch or C2-sel is compared with QM (F7).
> - **T-full (excluded).** Arbitrary QM procedures on `V⊗A`. A separation that only T-full achieves does not count.

### A.2 SPEC §4.3

> ### 4.3 Candidate procedures and the criterion for "smallest"
>
> **Criterion, fixed now.** In order:
> 1. the fewest unsourced physical prerequisites in §4.4, counted per accountable obligation;
> 2. then no hidden-sector operation and no posited coherence;
> 3. then the fewest procedure elements (preparations, reads, times).
>
> A candidate qualifies only after its separating power on the instance is established mathematically, through M-1 or
> M-2.
>
> **`C*` (coherent preparation).**
> - `C*₁ = C0 + {ρ₊ = |+⟩⟨+| ⊗ |a₀⟩⟨a₀|}`, with one Lüders `V`-read at `t = 1`.
> - Fallback, frozen now: `C*₂ = C0 + {|+⟩, |+i⟩}`, with reads at every `t` in one period of the instance
>   (`t ∈ {1, 2}` for `Γ^alt`). For a general `G`-inequivalent pair the reads must cover every slice where the pair
>   differ. `C*₂` is used if and only if `C*₁` does not separate under T-V in the record's own computation.
> - *Inference (unverified):* `C*₂` separates any `G`-inequivalent pair under T-V, by B4 ll. 148–151 and l. 292. K5
>   re-derives this.
> - Prerequisites: S-0 to S-5 and S-7, plus S-6 for `C*₂`.
>
> **C-pers (no coherent preparation).**
> - P-conf, two Lüders `V`-reads, `A` persisting, no reset. It is a T-V procedure.
> - It avoids S-3, S-6 and S-7, but needs O-RET: native retention of hidden-ancilla coherence between the reads.
> - Its separating power on the instance is unknown (M-2).
>
> **Selection, frozen now.**
> - If M-2 shows that C-pers separates the instance, the criterion selects C-pers: fewer prerequisites, no posited
>   preparation coherence.
> - Otherwise it selects `C*`.
>
> **Minimality of the addition, conditional on M-1.** If M-1 confirms equal C0 laws, then C0 alone cannot separate the
> instance, so some addition is needed. If M-1 reports that C2-ch or C2-sel separates the instance, that class enters
> this comparison as a further candidate, and the selection is redone under the same criterion before any freeze.

### A.3 SPEC §4.5, "Present state"

> **Present state.**
> - For `I₀`: no reviewed closure result covers `C*₁`. FS:106 does not address `ρ₊`, and S-7 is open. So step 1 does not
>   fire, and the verdict is **UNSOURCED[I₀]**. It would become REFUTED (c)[I₀] only if a reviewed closure result settled
>   S-7 negatively.
> - For every extension: **UNSOURCED**.
>
> A mathematical separation without access stays a scoped gap.

## Change log (r1 `f737fe0e` → r2), against REV1

| Item | Change |
|---|---|
| M1 | K-P added (§6.1): lift `U^P`, record `(0,0 \| 0; 0,1)`, reasoning from the definitions, fail-closed criterion. No recommended pair adopted; DOES-NOT-SEPARATE carries "no persistence-specific pair witness" unless `K-P′` is fixed at `Φ`. K-P added to §7.2 VOID, §9 and H6 |
| M2 | H-comp's home cited as #866 (B4 ll. 381–383) in the §8 table and in H1 |
| M3 | SPEC §4.3 quoted verbatim (A.2, and its selection clause in §7.3). The §10 row reclassified as support off `main`. §7.3 does not adopt the selection: it is re-checked with H-comp counted, by owner decision, before any native freeze |
| M4 | K2 marked as differing from SPEC K2, with the reason. Its instance part is a cross-check against M-1's reported C2-ch two-read masses, and a mismatch gives VOID. Reset form `r_U` defined in §3 |
| N1 | §0 time paragraph deleted; the comment now reads "before 18:05Z" (edited 18:14:44Z) |
| N2 | Appendix A quotes SPEC §1.4, §4.3 and §4.5 "Present state"; freeze precondition in §7.1; §10 rows |
| N3 | "Exactly two" kept; REV1's remark recorded under (p2); H5 resolved |
| N4 | §9 checkpoints added: `RESULT.md`-only commit, change log and delta review before the freeze, independent review of the result, K13 with every outcome, persistence attribution, K-P. Row 1 narrowed |
| N5 | K-H and outcome 4 refer to periodicity of the slices, not of `Γ` |
| N6 | §9 aligned with §7.2: K11 and K-P gate every outcome other than NOT-EVALUATED |
| N7 | §5: (t1) instrument sequences and (t2) the between-read propagator labelled as this record's own readings |
| N8 | PPer membership enters through G-M1 (d) only; K5 no longer re-derives G-M1 facts |
| N9 | Persistence attribution compared per `(j; s, t)` |
| N10 | File name kept; rename to `PREREG.md` at `Φ`, with the `git diff -M` checkpoint in §9 |

## Change log (r2 `7ff0c180` → r3), against REV2

| Item | Change |
|---|---|
| D1 | §6.1 rewritten. The coherence lift `U^C` (`U^C_0 = L`, `U^C_t = Q`, `T = QL`) was added as K-Pc, with values re-derived by hand: C-pers 1, reset ½, dephased ½, projected onto `a₀` ¼. `U^P` was kept as K-Pp, with exact values (`p` ½ and ½; `r` 1), and noted to detect (R) only. The pass criterion requires the exact values (`U^C`: `p = 1`, `r = ½`; `U^P` as stated), obtained by the same written procedure as on the instance. The purpose sentence, the DOES-NOT-SEPARATE scoping and H2 now read "shown to retain ancilla coherence on the K-P lift". The K-P row, K5 and §9 were updated |
| D2 | §7.1 freezes §§1–3, 5–11 and Appendix A. On the failure path `B_I` writes NOT-EVALUATED inside §4. §9 row 1 is now a reviewer reading of every commit between `Φ` and the `RESULT.md` commit |
| D3 | K2 (ii) covers every record over one period of the slices, and accepts M-1's C2-ch law either as masses or as the factors `Γ_s` and `𝒪₂(t,s)` |
| D4 | A.1 headed as an excerpt of SPEC §1.4, with the omitted parts named |
| D5 | §7.3 states the owner re-check as this record's proposal, with #1143 accountable |
| H7 | M-1's locations cited (PR #1151 at `594b5128`: `RESULT.md` §4.3 ll. 123–135; K-b §3; delta check c.6665968807), as pointers only; M-1 not landed. The §10 row was updated |
