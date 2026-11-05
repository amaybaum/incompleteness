# OI-QM-SEL M-2: the C-pers record class (preregistration draft)

**Status: DRAFT, NOT FROZEN. WIP / UNVERIFIED.** This file prepares definitions, controls and a decision rule only.
- No evaluation is made. No law is computed for any specific pair, and nothing here states or bounds the separating
  power of C-pers.
- The test instance is a placeholder (§4). It is bound only to the M-1 instance and outcome as independently checked.
- Independent review of these definitions is pending. Merge is not authorized.

**Writer:** `writer-m2`. **Issue:** #1143 (OI-QM-SEL), unit M-2 of the selection-target specification.
**Base:** `origin/main` `f051916a113c9412b3efbb1ff813ec57c2ed265d`. Every path:line below is read at this base.
**Method:** reading only. No script, CAS, numerical evaluation, search, Lean work or hand evaluation of any law on any
instance.

**Abbreviations.**
- `R/` = `verification/programmes/oi-qm/reconstruction/`.
  - B4 = `R/bsel-2-b4prime-20261105/B4PRIME.md`; SC = `R/bsel-2-b4prime-20261105/SCOPE.md`.
  - RES = `R/bsel-2-q2a-ce-20261105/RESULT.md`; QP = `R/bsel-2-q2a-ce-20261105/PREREG.md`.
- Kernel modules under `verification/lean-mathlib/OIBridge/`: TSG `TwoSidedGauge.lean`, CLG `CoherentLiftGauge.lean`,
  DC `DilationChoice.lean`, CF `CancellationFork.lean`, RC `RootedClassification.lean`, RCAT
  `RootedClassificationAllTime.lean`.
- SPEC = the #1143 selection-target specification r3, #1143 comment 6665278924; SREV = its independent review record,
  #1143 comment 6665288579. Both are off `main` (§10).

***

## §0. Authorization

Owner ruling, recorded at #1031 comment 6665461411 (posted 2026-11-05T18:05:55Z) as amaybaum, Claude Code session chat,
2026-11-05, and pointed to from #1143 comment 6665466217. The M-2 item, quoted verbatim from #1031 c.6665461411:

> **M-2.** Prepare the C-pers paper-only study in parallel: configuration-only preparation; two visible-system reads; persistent ancilla; no imposed coherence or reset. Its definitions and controls may be prepared now. Evaluate its separating power after the M-1 instance and outcome are independently checked. If M-1 fails, do not silently substitute another pair. Independent review is required for each result. This authorizes only the bounded mathematical work, not a native physical experiment.

The same comment's table reads: "#1143 M-2 | Approve preparation now and paper-only evaluation after M-1 establishes the
test instance".

**Recorded discrepancy (provenance only).** The comment dates the session-chat ruling "about 18:45Z", which is later
than the comment's own posting time, 18:05:55Z. No claim here depends on the time.

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
- **(p1)** The evolution clause is (r1) together with H-comp. Read as a statement about QM, it is (r-TV) of §5.
- **(p2)** "Two visible-system reads" is read as exactly two reads. Single reads and lists of length `k ≥ 3` are not
  C-pers procedures. A result for them is out of scope and is not used to rescue an outcome (§A.29).
- **(p3)** `s = 0` is admitted. The read times range over all of `ℕ`. A claim is not restricted to a horizon.
- **(p4)** Since no test is applied, no `⊥` record exists. The record alphabet of the procedure `(j; s, t)` is
  `V × V`.

## §3. The complete-record law `Λ_C-pers`

**Branch masses.** For the procedure `(j; s, t)`, `s < t`, the record `(v₁, v₂) ∈ V × V` has the unnormalized mass

  `p_U(v₁, v₂ | j; s, t) := ‖ P_{v₂} · T_{t,s}(U) · P_{v₁} · U_s · e_j ‖²`.

Equivalently, `Σ_{a∈A} |⟨(v₂,a), U_tU_sᴴP_{v₁}U_se_j⟩|²`. The vector `P_{v₁}U_se_j` keeps every ancilla component; it is
not renormalized, reset or projected onto `a₀`.

**`⊥` masses.** None: the set of failure records is empty for every procedure (p4). This is a definitional consequence
of Rst-none, stated here so that a reviewer can check it, not a computed result.

**The law.** `Λ_C-pers(U) := ( p_U(v₁, v₂ | j; s, t) )` over `j ∈ V`, `s < t` in `ℕ` and `(v₁, v₂) ∈ V × V`.
`O_C-pers(U, U′)` holds iff `Λ_C-pers(U) = Λ_C-pers(U′)` entrywise.

**Obligations for the evaluation record** (not discharged here):
- **L-0 (law from procedures).** Re-derive the displayed mass from P-conf, H-comp and two Lüders reads, by explicit
  unnormalized branch states, as QP §3 K-b did for C0 and C2. B4 W0 is a cross-check only.
- **L-1 (bookkeeping).** For each `U`, `j` and `s < t`, the masses sum to 1 over `V × V`.
- **L-2 (marginal).** The marginal of `p_U(·,·|j; s,t)` over `v₂` equals `Γ_s(·, j)`. This is used by K3.
- **L-3 (`|A| = 1` reduction).** At `|A| = 1`, `p_U(v₁, v₂ | j; s, t) = Γ_s(v₁, j) · 𝒪₂(t,s)(v₂, v₁)`, the
  two-read case of B4 W0.4. This is used by K2.

L-0 to L-3 are stated before evaluation so that their failure is detectable. If any one cannot be derived, the outcome
is VOID (§7).

## §4. The test instance (placeholder; not filled)

**Instance slot `I_M1`: the M-1 instance and outcome, as independently checked.**

This slot holds no pair. It is filled only by a binding amendment (§7.1), which copies verbatim from M-1's record:
- the lifts `U`, `U′`: every slice, its placement in `t`, `|V|`, `|A|`, the anchor and the basis order;
- M-1's verdict and its scope;
- M-1's reported C0, C2-ch and C2-sel laws for the pair;
- the commit on `main` that holds M-1's record, and the location of its independent review.

**What the slot requires of M-1 (gate G-M1).** M-2 is evaluated only if all of the following hold:
1. M-1's record is on `main`, and its independent review is recorded.
2. M-1's checked outcome establishes, for its frozen pair, each of:
   - (a) equal C0 laws;
   - (b) that the lifts are not `G`-related;
   - (c) that the lifts are T-V-distinct (§5), re-derived;
   - (d) that the visible family `Γ` lies in `PPer`, with the orientation checked.
3. The instance bound is exactly M-1's frozen pair, character for character.

**If G-M1 fails** (M-1 is VOID, does not establish any of (a)–(d), or is not independently checked): M-2 is not
evaluated, and its outcome is NOT-EVALUATED (§7). No other pair is substituted. A different instance needs a new owner
decision, recorded before any law of that instance is computed.

**Not done here.** No law of any candidate instance is computed, estimated or discussed. The spec's candidate F4 (SPEC
§0) is named only as the pair M-1 is authorized to verify; this draft depends on no property of it.

## §5. The target-QM comparison (T-V)

Restated from SPEC §1.4 so that the record is self-contained. The restatement is this record's own definition.

**T-V.** QM on `V`, with `A` an inaccessible environment in `|a₀⟩` at the root.
- **Preparations:** every density matrix `ρ ⊗ |a₀⟩⟨a₀|`, `ρ` on `ℂ^V`.
- **Readouts:** every finite sequence, at increasing times, of finite instruments on `V`, each acting as
  `𝓘_r ⊗ id_A`. A Lüders read `P_v` is the instrument `ρ ↦ |v⟩⟨v|ρ|v⟩` on `V`.
- **Dynamics (r-TV):** `U_t` is the cumulative propagator from the root to `t`. Between reads at `s < t` the state
  evolves by `U_tU_sᴴ`. `A` persists between reads. Every branch mass is kept, unnormalized.
- **`O_T-V(U, U′)`:** equality of all T-V branch masses.
- **T-V-distinct:** `¬O_T-V(U, U′)`.

**Excluded comparators.** T-full (arbitrary QM procedures on `V ⊗ A`) does not count. T-V+R (a declared ancilla reset)
applies only to C2-ch and C2-sel, not to C-pers.

**Relation fixed in advance.**
- **D-1 (by construction).** The C-pers procedure `(j; s, t)` is the T-V procedure with `ρ = |j⟩⟨j|` and Lüders reads at
  `s` and `t`. So `Λ_C-pers(U)` is a subfamily of `Λ_T-V(U)`, and `O_T-V ⇒ O_C-pers`. The evaluation record writes this
  out (K5).
- **What M-2 decides.** On the bound instance, which M-1 has shown T-V-distinct, whether C-pers is one of the T-V
  procedure classes that separate it.
- **What M-2 does not decide.** Whether native OI access supplies C-pers. Whether T-V and C-pers agree on any other pair.

## §6. Controls

Identifiers follow SPEC §4.6 where a control corresponds to one there. All pass criteria are fixed now. The evaluation
record writes out every derivation.

| ID | Control | Pass criterion |
|---|---|---|
| K1 | Positive gauge control | For the bound `U` and `L := 1_V ⊗ H₂` on `{a₀, a₁}` (identity on further labels), constant in `t`, `Λ_C-pers(LU) = Λ_C-pers(U)` for every record. `(U, LU)` is `G`-related (TSG:84). A difference makes the outcome VOID. |
| K-B | Invariance of the law | The record derives, for every lift, that `Λ_C-pers` is unchanged by (i) any time-dependent `L_t ∈ 𝒢_L` and (ii) any constant weak `K`. It states whether the derivation used the `a₀` reset frame (it must not, since there is none). Failure makes the outcome VOID. |
| K2 | `\|A\| = 1` countercontrol | L-3 holds, so at `\|A\| = 1` the law is the two-read C2-auto form in `(Γ_s, 𝒪₂)`. On the instance, the record also evaluates that reduced form for both lifts and reports whether it separates them; this feeds the attribution of §7.3 and is not a pass condition. |
| K3 | Fixed-basis control | L-2 holds, and on the bound instance the C-pers marginals of both lifts equal the C0 laws M-1 checked. |
| K5 | Re-derivation | The record re-derives L-0 to L-3, D-1, K11's witness WD, and the facts of G-M1 (a)–(d) that it uses, from `main` and M-1's reviewed record. No B4 [D] or RES result is a premise. |
| K7 | Masses | No normalization, no conditioning and no postselection. The empty `⊥` set is stated. L-1 holds. |
| K9 | No imposed coherence | Roots are `e_j` only. No P-coh, `ρ₊` or phase is chosen apart from the lift. No reset. The ancilla's coherence enters only through `U_s` and `T_{t,s}`. |
| K10 | Adjustability | Every freedom left open (a reading, a read pair) is listed. The outcome is reported for every admissible value. An outcome that changes across them is UNDECIDED. |
| K11 | Positive sensitivity (SPEC K11, C-pers) | WD (B4 ll. 309–315): `U` = alternating `H₂`, `g` with `L ≡ 1`, `K_1 = Z`, `K_t = 1` otherwise; at the instance's `\|A\|` it is placed on `𝒜` with `⊕ 1_C`. The record computes both laws from §3 and finds some record with unequal masses. B4's stated values are not premises. |
| K12 | Device identity | Only `U ↦ U′` changes: the same roots, read pairs, projectors, anchor and decoder. |
| K13 | Joint-lift nativeness (conditional) | The instance's visible family is in `PPer`, orientation checked (G-M1 (d)). C-pers adds no preparation interaction, so the joint process is the lift itself. Reading "in `PPer`" as "native" is CONDITIONAL[F3's hypothesis that native realizations are finite `RootedRealization`s (RCAT:192–194); S-0]. Without both, K13 is a necessary check only. |
| K-D | Same `Γ` | The instance has equal `Γ_t` for every `t` (from M-1). |
| K-H | ℕ coverage | Every equality claim covers every `s < t` in `ℕ`, by eventual constancy or periodicity of the instance, not by a horizon. |

**Not applicable at the paper level, kept for any native study.** SPEC K4 (hidden common cause), K6 (private decoder)
and K8 (carrier change) concern a physical setting variable and decoder. Here the laws are per `j`, no setting is
selected, and the decoder is the record (§2). They are re-imposed on any native realization, which is not authorized.

## §7. Decision rule (fixed at the freeze; draft now)

### 7.1 Order of work
1. **Definitions review.** This draft is independently reviewed. Changes required by that review are made, with a change
   log, before the freeze.
2. **Freeze `Φ`.** A commit that fixes §§1–3 and 5–9, with §4 still a placeholder. It precedes any knowledge of a
   C-pers law of the instance.
3. **Gate.** G-M1 is checked against M-1's reviewed record on `main`.
4. **Binding amendment `B_I`.** A single-parent child of `Φ` (or of a later commit that changes no frozen section) that
   fills §4 verbatim from M-1 and changes nothing else. If G-M1 fails, `B_I` instead records NOT-EVALUATED and its
   reason.
5. **Evaluation.** `RESULT.md` in this directory, in a later commit that changes no other file.
6. **Independent review** of the result.

### 7.2 Outcomes (closed list; the first that applies is the outcome)
1. **NOT-EVALUATED.** G-M1 fails. No pair is substituted (§4).
2. **VOID.** A control among K1, K-B, K2, K3, K5, K7, K9, K11, K12, K-D or K-H fails or is vacuous; any of L-0 to L-3
   cannot be derived; a definition reads differently from its source line; or the bound instance differs from M-1's.
3. **UNDECIDED.** The controls pass, but equality over every `s < t` in `ℕ` cannot be settled by exact hand argument, or
   the outcome changes under a freedom K10 lists. The unproved step is named. A deciding computation is written as a
   proposal and not run.
4. **SEPARATES[C-pers; instance; `|V|`, `|A|`; `PPer`].** The controls pass and some `(j; s, t; v₁, v₂)` has
   `p_U ≠ p_U′`. The record writes out at least one such record with both masses in exact arithmetic, and lists every
   separating `(j; s, t)` up to the instance's period.
5. **DOES-NOT-SEPARATE[C-pers; instance; `|V|`, `|A|`; `PPer`].** The controls pass and `Λ_C-pers(U) = Λ_C-pers(U′)`
   entrywise, for every `j`, every `s < t` in `ℕ` and every record.

K13 is reported with every outcome; its conditional reading does not change the outcome.

### 7.3 Consequences, fixed now (SPEC §4.3)
- **SEPARATES.** M-2's mathematical prerequisite is met for C-pers. Under SPEC §4.3 the selection criterion selects
  C-pers, subject to the redo rule below.
- **DOES-NOT-SEPARATE.** Under SPEC §4.3 the selection is `C*`. The finding is scoped to C-pers with exactly two reads
  on this instance. It is not extended to other read counts, other pairs or other classes.
- **Redo rule.** If M-1's checked outcome reports that C2-ch or C2-sel separates the instance, that class enters the
  comparison, and the selection is redone under SPEC §4.3's criterion before any freeze of a native test.
- **Persistence attribution (reported, not a pass condition).** The result states whether every separating record of
  C-pers is also separated by C2-ch or C2-sel, from M-1's checked laws. Only a separation that the reset classes do not
  reproduce is attributed to the persistent ancilla.
- **Unchanged in every case.** SPEC's present verdict, UNSOURCED, for every declared interface. A mathematical
  separation without sourced access is a scoped gap (SPEC §4.5).

## §8. Scope

**What a SEPARATES outcome would establish:** that, on the bound instance, the C-pers complete-record laws differ, at
the stated `|V|`, `|A|` and class. Read about OI, it is CONDITIONAL[P-conf, Acc_pers, Rd, H-comp, Rst-none with `A`
persisting, fixed `a₀`, (r1), (p1)–(p4)].

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
| — | H-comp as the physical between-read evolution | no accountable Issue is identified; finding for the reviewer |

- Any equivalence or inequivalence of OI and QM, physical or operational.
- Any statement about another pair, another read count or another class.
- A theorem promotion, a Lean statement or a manuscript claim.

## §9. Invariants and their checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| Definitions, controls and rule are fixed before any C-pers law of the instance is known | `Φ` precedes `B_I`. `git diff Φ B_I --stat` lists this file only, and its hunks lie inside §4 |
| No pair is substituted | `B_I` quotes M-1's pair verbatim, with M-1's commit and review location. K5 compares character for character |
| M-1 is independently checked before evaluation | G-M1 item 1, checked in `B_I` against `main` |
| The SPEC definitions used are the reviewed r3 | This file cites SPEC by comment id and the digest below. `updated_at` equal to `created_at` at the time of reading |
| Complete-record law, `⊥` set stated | L-0, L-1, K7 |
| No imposed coherence, no reset | K9 |
| Controls green before any SEPARATES or DOES-NOT-SEPARATE | §7.2 order: VOID precedes them |
| Sensitivity before DOES-NOT-SEPARATE | K11 |
| Device identity | K12 |
| ℕ coverage, no horizon | K-H |
| Not adjustable | K10 |
| Verdict reads structured results (§A.44) | No computation; the written decision table of §7.2, evaluated row by row in `RESULT.md` |
| Paper only | `RESULT.md` states the method; the reviewer checks that every value is a written hand computation |

**SPEC pin.** SPEC §4.7's first checkpoint asks for the sha256 of `SPEC.md` to be quoted in the comment that posts it.
c.6665278924 quotes none (finding). As a substitute this draft records the sha256 of the comment bodies as served by
the GitHub API on 2026-11-05, `created_at = updated_at` for each:
- c.6665278924 (SPEC r3): `92510abc3913cf094bc7c34f6e6cf41c9c3b36f77c983ca9d76654979bcfca2e`;
- c.6665288579 (SREV): `865117425f87ce150f57185423ef60e3dbf3e483cf65ee472d517ea467d233c4`;
- c.6665466217 (M-1/M-2 pointer): `b057a66cd637c8d50aca539f2c791f5fc45d660db19ba15d97927e012daa3df6`.

These digests are of the comment bodies, not of a `SPEC.md` file. They pin what was read; they do not put SPEC on
`main`.

## §10. Premise ledger (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| #1031 c.6665461411; #1143 c.6665466217 | Authorization (§0) | Provenance. An owner designation quoted with author and time (§A.42 item 7) |
| SPEC (c.6665278924) | Origin of T-V, the K-list, the §4.3 criterion and the S-list | Provenance. Every definition this record uses is restated in §§2–6 as its own. SPEC §4.3's selection rule is quoted in §7.3 as a consequence, not used as a premise of any mathematical claim |
| SREV (c.6665288579) | SPEC's review status | Provenance |
| B4, SC, RES, QP (on `main`) | Notation, procedures, readings, WD's definition | Support on `main`, for definitions only. B4's WD values and every [D] result are not premises (K5, K11) |
| Kernel lines (TSG, CLG, DC, CF, RC, RCAT) | Definitions of §1; K13's conditional reading | Support on `main` |
| M-1's record | G-M1 (a)–(d); the instance | Not yet existing. Becomes support on `main` only when landed and reviewed; until then G-M1 fails |
| #866, #914, #1032 | Accountable homes in §8 | Provenance; planning records only (§A.45 rule 1) |

## §11. Hidden-assumption watch (§A.31)

- **H1 (H-comp).** C-pers reads `T_{t,s} = U_tU_sᴴ` as the physical evolution between reads. The kernel's
  `CoherentLift` (CLG:124) is admissibility slice by slice and fixes no between-read evolution. A C-pers result is
  therefore CONDITIONAL[H-comp]. No accountable Issue for H-comp's physical supply is identified (§8).
- **H2 (retention).** Rst-none with `A` persisting is the content of S-8. A separation that uses ancilla components of
  `P_{v₁}U_se_j` uses retention. That is the attribution §7.3 reports.
- **H3 (no reset frame).** C-pers has no `a₀` reset or test after a read, so SC W3 does not arise for it. The anchor
  still enters through the P-conf roots `e_j`. K-B tests that no step uses a reset frame.
- **H4 (Lüders read).** Rd is a Lüders read that leaves `A` untouched. A read that disturbs `A` defines a different
  class and is not tested.
- **H5 (two reads).** "Two visible-system reads" is read as exactly two (p2). A reviewer who reads it as "at most two"
  or "at least two" should say so before the freeze. After the freeze the class is not widened (§A.29).
- **H6 (sensitivity witness).** K11's WD tests sensitivity to a time-dependent right gauge, which already shows at
  `|A| = 1`. No preregistered witness tests sensitivity to the persistent ancilla specifically. Whether one is required
  before a DOES-NOT-SEPARATE outcome is left to the definitions review.

## §12. Review and next steps

- **Independent review of these definitions** is required before the freeze. It should check §§1–3 against their
  sources, the T-V restatement against SPEC §1.4, the controls and their pass criteria, the decision order and the
  watch items H5 and H6.
- **Evaluation** waits for M-1's independently reviewed outcome on `main` (G-M1). If M-1 fails, no other pair is
  substituted without a new owner decision.
- Merge is not authorized.
