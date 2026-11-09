# OI-SM-QM-BRIDGE unit 1: dispositions of the r2 review (r3)

**WIP / UNVERIFIED. Model-written (Claude Code subagent, 2026-11-09).** Paper-only. No git or
GitHub write, no Lean work, no manuscript change, no computation on an OI mechanism.

- **Object revised:** `BRIDGE-UNIT1.md`. r2 sha256
  `3905569bd8d47e3d3797e66f5d3c68b2fbf054e8859191b7cf3777db0412103a`, kept unchanged as
  `r2/BRIDGE-UNIT1.md`; r3 revised in place. Line numbers below are r3 lines.
- **Review:** `review/REVIEW-UNIT1-r2.md`, sha256
  `3cdf7dc294e27701737e0c605b8a63bd958983d0debad127e3d3a525b1164eb3`, verdict REVISE (RB1–RB3,
  n1–n10).
- **Sources:** read by the writer with `git show fd539e15:<path>` after `git fetch origin main`
  (copies in `src3/`; the five papers and QP are byte-identical to the reviewer's `review/src2/`).
  Lean statements were read at their declarations; nothing was built.
- **Checks:** `probes/r3_generic_checks.py` (sha256
  `6489694cf51aebb6a0bb5b805d81c30b97d97364addd176fd0c2c6627c3890fc`), output
  `probes/r3_generic_checks.out` (sha256
  `d85a1a9fbfffb4e6aeec3c67e5ae543dcf5df692ea0814890262d0e9d479a9d5`, 14 PASS, ALL PASS).
  Exact arithmetic on generic objects under #1211 c.6739843458; imports no earlier script; no OI
  mechanism (the K1 graph is a fixed six-vertex bipartite graph, not a ring or cubic lattice of
  the corpus).

## Blockers

| Finding | Verified (writer's own reading at `fd539e15`) | Change in r3 |
|---|---|---|
| **RB1** "earliest" / "weakest … therefore" contradicted | `C5Discovery.lean:59` `obligations_independent`: substratum theory has `PhasesAvailable` and ¬`LayerFlowExecutable`; ones-fixing theory the reverse. `FlowEndpoint.lean:89, :208` (`onesTheory_layerFlowExecutable`, `onesTheory_not_qm`). `exec-source-audit.md` outcome: the frontier "is two named assumptions, the phase intervention and the executability", necessary condition "a non-monomial admissible operator at level one"; no ranking. `CoherentContinuumSource.lean:163` and `PolarizationClosure.lean:135` (uncountable rays); `polarizedTheoryC_derivedOI` (:606), `polarizedTheoryC_not_layerFlowExecutable` (:389), `polarizedTheoryC_not_qm` (:620); `coherent-continuum-source-audit.md` outcome 2 "no current source". Main:590 and GR:268 state the equivalence "with the phase intervention stated". Main:403–406, Main:414, Main:566, Main:584 for Bell. | §0 item 8 (l.120–146) rewritten as "Frontier of the forward chain": phase, flow (FI-1 as its necessary condition) and H-Bell as separate unsupported implications; FI-1 first only with the phase taken as stated. §5.1 heading (l.369) and Statement (l.375–376); "weakest coherent requirement … therefore" deleted; *Scope of necessity* (l.398–425) cites `PolC` as countermodel to sufficiency and the strengthened condition; *Position* (l.479–506) replaces "Why it is the earliest": (b) phase independent, kernel-cited, (c) H-Bell beside FI-1. §10 FI-1 label (l.899–902) cites the three audits; the "added: first unsupported step" clause dropped. §11 conclusion (l.983–986) restated. *Deviation:* H-Bell's independence is stated as "not after FI-1; no source read derives either from the other", not as kernel-proved independence, because only the phase/flow independence is kernel-proved. |
| **RB2** qualifier dropped; carrier ambiguous | Main:590 and GR:268 ("exact finite endomorphic operational QM"), GR:262. Main:566 (fixed injective step maps extended to bijections), Main:584 ("finite resolution … incompatible measurements, adaptive interventions"), Main:600 (two-sided ε-density). `ExecSource.lean:52`: the witness is `K : Matrix (S × Fin 1) …`, level one of the configuration carrier. QP:79–98, QP:846–877; MECH-2 §0 item 2 (U2: $A_4\wr S_n$; NC). | FI-1 restated on "the configuration carrier at level one" (§5.1 l.378–382, §0 item 8). "Exact finite endomorphic operational QM within the structural architecture" restored in §0 item 8, §5.1 *Scope of necessity*, §11 (l.983–986). Encoded-carrier and finite-accuracy sentence added (§5.1 l.414–425). *Partial refusal:* the review asks for "with the phase stated" wherever FI-1's *necessity* is stated. The necessity does not use the phase: `exists_nonMonomial_of_layerFlowExecutable` has no phase hypothesis, exact QM executes every layer flow (GR:270, `layerFlowExecutable_of_control`), and `uncountableNonMonomialRays_of_qm` (CoherentContinuumSource.lean:195) derives the stronger condition from QM alone. r3 attaches the phase qualifier to the equivalence and to FI-1's position as first, and says so (l.402–405). |
| **RB3** wrong direction of support; "adaptive"; "only" | `SubstratumInterfaceAudit.lean:770` (`obsTheory := permTheory 𝒮.Conf`), :837 (`obs_availExt_le_substratum`); `StructuralClosure.lean:180` (`substratumClass := … IsMonomial K`); `exec-source-audit.md` scope amendment (quoted); GR:260 (`bijectiveOperator_monomial`), `ReadWriteControl.lean:100` (`readWriteOperator_monomial`). `OperationalAssembly.lean:617` (`availExt_bind`); QP:851–863 (adaptive processes covered "by the `availExt_bind` field"). QP:897–915 (open item: adaptive native `S`, encoded). C5 audit candidate 2, T4, T6 (test 8), verdict C. Main:590 cites only ¬executability for read/write. | §5.1 *Status* (l.441–478): read/write negative re-cited to `obsTheory`, `obs_availExt_le_substratum`, `substratumClass`, the monomial theorems and the scope amendment; the layer-flow negatives stated not to be cited for ¬FI-1; "adaptive" removed from the open list with `availExt_bind` and QP:851–863; the open adaptive item placed at encoded $S$. "Only unresolved candidate source" replaced by four numbered candidates, including C5 candidate 2 (verdict C) and extended access. NQ1 cross-reference (l.941–945). §6 Interference row (l.577) gains the read/write citation. |

## Nits

| Finding | Verified | Change in r3 |
|---|---|---|
| **n1** non-monomial ≠ state-mixing | Exact check K2 (independent of reviewer's G1); `LiftAudit.lean:155` `gateFlow_half_not_preservesDiag`. | FI-1 uses "admissible operator" (GR:270's term); the two predicates are stated separately (l.384–388). |
| **n2** exponent: permutation unitaries only | Main:556 ("entries are 0 or 1"); QP:855 ($2^{-k/2}P_\sigma$); exact check K3. | §5.1 *Position* (d) (l.493–497) scoped to permutation unitaries; the weighted family normalizes only at $p=2$, stated as a consequence of the quadratic Kraus normalization, not a selection. |
| **n3** §6 Born row "equivalently" | The second item is a precondition, not an equivalent. | "equivalently a source of …" → "which presupposes a source of non-monomial admissible operators (FI-1, §5.1)"; the layer-flow citation removed (l.574). Same as point (b). |
| **n4** two gaps merged | SM:232; GR:270 ("no operational map from it to the configuration carrier being stated"). | Both stated: §0 item 8 (l.141–143); §5.1 candidate 1 (l.463–467). |
| **n5** closest derived objects | `SecondOrderCircuit.lean`, `SwapLayer.lean` (gate one-parameter groups), `SecondOrderLayer.lean` (all-sites layer as an automorphism); `gateFlow_not_monomial`; coherent-continuum route S5; exec-source X2, X5; Main:274. | New *Closest derived objects* bullet (l.426–433). Wording differs slightly from the review's: the one-parameter groups are of the gates, carried to the layer by `SecondOrderLayer`. |
| **n6** §9 scope vs header | Header coverage (SM §§1–5, SM:677–690, §8.3; Main §§1–2, §3.1–§3.3, lines cited). | §9 search-scope sentence aligned (l.786–788). |
| **n7** F8 ellipsis | ch06:28 read: "at the level of the algebraic labels … — with the physical spin identification riding H-spin' (SM §4.7) — not from a separate spin-statistics postulate"; FULL:1541 carries the same qualifier. | F8 (l.710–713) quotes the qualifiers and states why the finding stands (spin, not statistics; fermionic measure open). |
| **n8** B9's D clause | B9 column (ii). | D-partial count 3 → 4, B9 listed (l.316–317). |
| **n9** coverage | — | Header (l.44–59) lists the foundations audits and the Lean statements read, with lines. §13 (l.1055–1067) records what was read at declarations and what was not read. |
| **n10** "downstream of FI-1" | — | §5.1 *Position* (e) (l.497–501): restricted to H-spin', H-χ' and the fermionic measure; the carrier's complex structure (NQ1) stated not to presuppose FI-1. |

## Brief items beyond the review

| Item | Verified | Change in r3 |
|---|---|---|
| **FI-1's conditionality** | Kernel `Substratum` is site-factorized (`SubstratumInterfaceAudit` docstring Q1); `obsTheory_rule_independent` (:780); QP:846–877; B4, B10, B25. | *Conditionality* bullet (l.390–397): FI-1 posed on site factorization, P1–P3 with E-iso, and the second-order form; the negative uses only the configuration carrier; H-PREP not used. §0 item 8 states it. |
| **(a) #1049 re-assessment** | Confirmed in part. QP:254–257: G1's induction uses only which sites the update reads; re-derived by hand with "a function of" in place of "a linear combination of"; exact check K1 (nonlinear bipartite-read rule passes; linear control; self-term and same-colour-read countercontrols fail). G2's step 3 (QP:362–369) uses linearity of the O-sector map, which affinity suffices for. SM:569's $\Gamma A\Gamma=-A$ excludes same-sublattice and diagonal entries. MECH-2:530–534 reads "whose nonlinearity breaks the grading"; MECH-2 §0 item 1 gives $f_i(u)=u_{i-1}\oplus(u_{i+1}\vee u_{i+2})$, whose only same-colour read (even ring) is $u_{i+2}$. Not confirmed, and not claimed: that G1's Lagrangian/commutation consequences, or apparatus-1's full exclusion of a $Y$ read, survive nonlinearity (they use linearity). | §0 item 6 (l.104–109): shared premise is the bipartite, center-free read pattern, not linearity. §10 Connection (l.826–834) states it with K1. §10 MECH-2 bullet (l.871–877): the attribution names a feature that does not by itself break the grading; the record's conclusion unaffected. Classification line added (l.892–894), ELABORATING. §12 Q4 (l.1011–1013). |
| **(b) #1059 re-assessment** | Same as n3. | Applied under n3. |

## Owner instruction relayed during the revision (2026-11-09, chat, via the coordinating session)

| Requirement | Change in r3 |
|---|---|
| Section near §5.1 answering five questions with sources and status | New §5.2 table (l.511–522): site factorization **assumed**; read/write access **assumed**, its sufficiency **excluded under stated conditions**; non-monomial mixing **excluded under stated conditions**, **open** for four candidates; existing results **open**; wave-operator route **open**, excluded only for formulations that land. |
| Two "earliest" notions kept apart | §5.2 (l.524–540): earliest unproved assumption (B1–B3 as OI's foundation; beyond the finite-law level, site factorization, then the access posits and the stated phase, all upstream of FI-1); earliest missing mechanism (FI-1 with the phase stated; otherwise phase, flow/FI-1 and H-Bell side by side; S13 on the spatial route). |
| Necessity scope | §5.1 *Scope of necessity*; §5.2 one-sentence summary (l.542–544). |
| Proposed dependency chain, arrow by arrow | §5.2 table (l.546–555) and summary (l.556–559): arrow 1 not supported (only converse necessary conditions); arrow 2 supported as a requirement, not an identification; arrow 3 not supported as consequences (phase independent, complex kinematics given, exponent unselected), replaced by the conditional (mixing ∧ phase, within the closure) ⟹ QM; arrow 4 supported conditionally. The sources give a branching structure. |
| Do not select NQ1 or NQ2 | §12 Q3 (l.1004–1010) rewritten: records the deferral and the owner's criterion; selects neither. |

## Refusals

- **RB2, in part:** the phase qualifier is not attached to FI-1's necessity, with the evidence
  given in the RB2 row. It is attached to the equivalence and to FI-1's position as first.
- No other finding is refused. RB1's H-Bell clause is applied in a narrower form (RB1 row).

## Changes not traced to a review finding

1. Header standing line (l.3–5) names r3 and both reviews; authorization bullet says r2 and r3
   checks (l.18).
2. §5.2, §12 Q3 and §12 Q4: from the relayed owner instruction and point (a) (tables above).
3. §13 (l.1042–1067): r3 checks recorded; kernel statements read at declarations listed; limits
   extended to the unread foundations audits.
4. §5.1 heading renamed (l.369) to match the content after RB1.

No other text was changed. The diff r2 → r3 (`git diff --no-index -U0`) has 23 hunks, each under
one of the rows above.
