# RR-1: ready-resource sourcing for the native-Y public-port interface (paper-only assessment)

**Authority.** #914 comment 6556989366, item 2 (owner, 2026-11-01): a bounded, read-only, paper-only
assessment and a *proposed* preregistration. Base: the P/S/R/RR inventory, #914 comment 6556841398.
**Review provenance:** reviewed in three rounds (final: accept with changes, C-1–C-8 applied); a reviewer's empty-heredoc `python3 -` call executed no code; the files were seen reflowed after writes (cause not determined; content verified by the drafter).
**Method.** No computation, script, Lean run, re-check or arithmetic beyond what a source states. No
PR, record, grade, hold or manuscript changes. A sourcing gap is not an impossibility result; "not
found" is scoped to the sources read (§A.19). No physical premise is proposed as adopted.

**Anchors** (repo-relative, exact SHA):
- `Main:N`, `RM:N`: `papers/Main.md`, `verification/ROADMAP.md` at `5914c17c`.
- `MR-pre:N`, `MR★:N`: MR-1 `preregistration.md` and `amendments/MR-star.md` under
  `verification/programmes/oi-qm/reconstruction/measurement-record-formation/` at `af1e9be2`.
- `NY/…:N`: `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/` at `d4a80fc8`.
- `CS/…:N`: `verification/programmes/substratum/continuous-substates/` at `d4a80fc8`.
- `NC1:N`: `CS/native-coupling-nc1-preregistration.md` at `d4a80fc8`: an **unaccepted draft (REVISE,
  paused; #1009 c. 6555867706, 6556077148)**. Every NC1 citation carries this status as [draft].
- `#912:N`: `verification/programmes/oi-qm/reconstruction/composition-access-20261024/REPORT.md` at `2af1d5d5`.
- **Review status of the notes used.** These notes record their own review as pending: `CS/native-causal-interface.md:3–4`,
  `CS/native-apparatus-register.md:6` and `CS/native-packet-stochastic-kernel.md:6–7`. The kernel's
  acceptance (`923be23b`) is taken from the NC1 §2.2 table [draft]; #1009 itself was not checked.

**Grades:** LK Lean kernel; PP paper proof; PP+X paper proof with exact finite check; EB exact bounded
computation with written proof; AUD source audit; DEF definition/convention/stipulation; POS posit.
**Levels** (MR-pre:36–43): *representable* (a map exists); *available* (an executing native process
under declared access, resources booked); *derived* (available from the OI premises, no added resource).
**Classes:** DERIVED; AVAILABLE-UNDER-RETAINED-ASSUMPTIONS (assumptions named); UNRESOLVED SOURCING GAP.
**Interface:** as in inventory §3. The rule is `U_{t+1}=U_{t−1}⊕h(⊕U_t)`; the 42-bit packet is on
B1(q10); the preparation is P0_NY, the v14 fewest-seed source law (NC1:83–90 [draft]); the windows are L+1→L+3→L+5.

**Properties of a ready element E** (site set, time t_r, use time t_u ≤ t_r, ready set R_E, stated prior;
the same definitions as proposal §2):
- **(a) occurs:** P(E_{t_r} ∈ R_E) > 0 under the stated prior, at E's own site set and time. Under the counting
  measure every finite pattern has positive mass (Main:56), so "occurs naturally" needs an observer-selection
  conditioning (hypothesis H-sel).
- **(b) accessible:** some positive-mass W_{t_u}-event gives P(ready | event) = 1 under the stated prior, with
  no private read, inverse or decoder. This uses **H-law**, "the observer's knowledge of the declared
  preparation law". *W-certified*: (b) still holds deciding from W alone. Where W-certified is no, (b) holds
  **only under H-law**, and H-law is carried as a hypothesis.
- **Stipulated reads.** A read under H-access is "a candidate convention, not an adopted access rule"
  (NC1:150–152 [draft]); it is not sourced record formation (R3, MR-pre:165).
- **(c) reliably preparable:** a native procedure under declared access yields E with a stated success
  mass, and every failure branch is retained (MR-pre:162–169, R5).

## 1. The ready elements of P0_NY, as the sources state them

- **Ready balls.** These are original-time current and previous Manhattan balls, "zero except for the
  listed sources" (`NY/parallel_v3/COMBINED-REPORT.md:68`, a toy instance). For q10, "current initial
  q10-ready ball has radius L+1; the previous initial ball has radius L" (`CS/native-causal-interface.md:24–25`),
  from the extension `B_(R+10)(q10)` (`NY/native_seed_v12/REPORT.md:35`). P0_NY has 25: 24 inherited
  plus the q10 extension (`CS/native-port5-cone-reduction.md:16, 44`; NC1:85–86 [draft]).
- **Compiled sources and programs.** There are 1479 compiled sources and 17 exceptions (NC1:85–86 [draft]).
  Source programs are compiled into the initial data: `NY/herald_v10/REPORT.md:56–57` ("native compiler"),
  and `NY/parallel_v3/COMBINED-REPORT.md:110` ("a standalone prepared apparatus").
- **Banks and keys.** These are reserved original-time triples, "present initially; none is inserted
  during evolution … the required supplied resource, not its physical derivation" (`NY/history_v9/REPORT.md:61–66`).
  The 28-key prior `Pr(eta=z|C=c)=8^(-28)` is "supplied … not … physically derived" (`CS/native-packet-stochastic-kernel.md:89–96`).
- **Complement law of P0_NY.** Independent-uniform where the inherited complement and the independent
  bank are retained (kernel:94–96; NC1:142–146 [draft]).
- **Native A is kept separate.** Native A (v11/v12) has the f8/f10 fresh pool and the "fixed-zero
  complement" alternative (`NY/shared_v12/INTERFACE-CONTRACT.md:44–54`). P0_NY replaces F10 by a ready
  pin, and "their actual joint distributions must remain separate" (`CS/native-actuation-boundary.md:53–58`).
  Native A material below is labelled as such.

## 2. Q1–Q4 matrix

Q1 and Q2 assess readiness only, and Q3 assesses imprint only; neither is inferred from the other.
Single-use validity is classified first. Preparing a next trial is classified in separate rows and is
not a prerequisite.

| Q | Element | Class | Anchor; grade |
|---|---|---|---|
| Q1 | Ready balls at original time | AVAILABLE-UNDER: the P0_NY pins and H-inventory | COMBINED-REPORT:68 (EB, toy); causal-interface:24–25 (PP, review pending); herald_v10:7 "prepared at the original initial time" (DEF) |
| Q1 | Ready balls produced by the rule from less-structured data | UNRESOLVED SOURCING GAP. None in the sources read. RM:1140–1141: "calibration, readiness, clock, settings and access are supplied, not derived". For one q7 seed-copy exception: "a supplied initial correlation/readiness resource, not a constructed native initializer" | RM:1140–1141 (AUD); outward_v6/CORRECTION-REPORT:53–54 (AUD; context: that one exception); reset_v7 PROBE-PLAN:19 (DEF) |
| Q1 | Late fields free of unprepared influence (q9=(0,s,r_old) at L, q8=(0,y,0); they carry s, y) | AVAILABLE-UNDER the P0_NY pins. The rule produces them; "the earlier cones are contained in the prepared region", with the listed source exceptions as the exceptions | causal-interface:8, 79–89 (PP, review pending) |
| Q1 | Banks and the 28 keys | AVAILABLE-UNDER H-prior-NC and the independent bank. They are uniform: randomness, not readiness | kernel:89–96, 137–138 (PP); NC1:142–146 [draft] |
| Q1 | Source law (v14 fewest-seed E/N) | AVAILABLE-UNDER: one law chosen by a fewest-seed-dependence criterion; 1456 laws give q10.A=s (7464 counts readout–law pairs) | `NY/native_decode_v14/REPORT.md:23–27, 49–57` (EB) |
| Q1 | Inventory completeness | AVAILABLE-UNDER H-inventory: "a ready region missing from it would change the classification" | `NY/native_vread_v15/REPORT.md:112–113` (AUD) |
| Q1 | Any element DERIVED | none in the sources read | — |
| Q2 | q10 ball readiness window | AVAILABLE-UNDER (P0_NY, H-torus): no unprepared original cell reaches q10 or the q8/q9 chain before L+1 ("source exceptions already listed by the preparation are the exceptions", causal-interface:87–88). Boundary keys at L+4 and L+5 lie outside all 25 balls, with ready slack 4 and 5 | causal-interface:24–25, 84–87 (PP, review pending); kernel:54–58 (PP) |
| Q2 | Blank public prefixes before the deadlines a_i | AVAILABLE-UNDER (H-access, bank prior) | history_v9:51–52; `NY/history_v11/REPORT.md:46` (eight-port) (DEF/PP) |
| Q2 | Readiness persistence beyond these windows | UNRESOLVED: no other readiness window is stated in the sources read | — |
| Q3 | Imprint of the input onto prepared cells before the interface (q9 at L; q10.A=s) | AVAILABLE-UNDER (P0_NY, chosen source law). q10 is "a lattice cell, not a permitted read"; the whole-q9 record at L is a stipulated read | decode_v14:34–37 (EB); INTERFACE-CONTRACT:38–40, NC1:150–151 [draft] (DEF) |
| Q3 | Imprint of the carrier onto a ready apparatus inside the interface | UNRESOLVED SOURCING GAP. The passive kernel is "not an observer-accessible reusable measurement instrument"; Class C needs a record-forming map absent from the retained contracts | kernel:13–14 (PP); NC1:315–325 [draft] |
| Q3 | Coupling of register r=q+2e_y to the carrier | An exact one-bit apparatus→carrier coupling, but "its two states cannot both come from the specified preparation" | apparatus-register:30–33, 44–52, 72–77 (EB, review pending) |
| Q4 | Consumption per passive step | AVAILABLE-UNDER (H-prior): 6 boundary keys and 8 bank triples per step; "Randomness is supplied initially" | kernel:54–58, 77–83, 137–138 (PP) |
| Q4 | Environmental correlations | AVAILABLE-UNDER: exact joint formula `G_(L+5)(C,eta)`, "not an independent bath/reset assertion"; full pushforward, no reset | kernel:139–145 (PP); apparatus-register:116–118 |
| Q4 | Context masses and calibration | AVAILABLE-UNDER: "bookkeeping masses, not native failure probabilities"; 5:3:2 "supplied, not derived from OI" | later-access-result:112–113; herald_v10:7–8 (DEF) |
| Q4 | Cost booking | AVAILABLE-UNDER: information transfer only; no energy or temperature at D | MR-pre:177–187 (PP) |
| Q4 | Next trial (i): a fresh package prepared at original time | UNRESOLVED. No source constructs a second P0_NY package. A per-law analogue is representable ("K pre-loaded seeds", Main:566; "the protocol entering as the preparation of the program register", Main:582). Per-trial key freshness is a sufficient route, but the audit is owed | Main:566, 582 (PP); #912:57–69 (PP), #912:179 (AUD) |
| Q4 | Next trial (ii): renewal of a consumed resource | UNRESOLVED SOURCING GAP. "A reusable native reset … remain[s] open"; consumption by a later stage "is not an operational reuse result"; a reset moves information into E or L | history_v11:151–152; apparatus-register:119; MR-pre:177–182 (Lemma R); native_v11:105 (Native A, stated as a general limit) |

**Carrier/record persistence (Q3/R, not RR).**
- The sign is carried through L+3→L+5 under the passive kernel, with "No arbitrary-depth … claim"
  (kernel:130–133; `CS/native-interface-selector.md:26`).
- Later reads carry no packet or key information under the retained prior: the port-5 read at L+79
  (`CS/native-port5-cone-reduction.md:51`) and the LA reads over L+6..2L (`EMPTY`, `CS/later-access-result.md:29–33, 85–92`).
- Beyond 2L, "horizons beyond 2L need new audits" (history_v11:150–152). Stipulated reads are kept by convention (NC1:150–152 [draft]).

### Owner distinction (1): occurs / accessible / reliably preparable

| Element | (a) occurs at the interface site and time | (b) accessible; W-certified | (c) reliably preparable |
|---|---|---|---|
| q10 ready ball | Mass 1 under the stated prior (P0_NY), by stipulation. Under the counting measure the mass is positive but not distinguished from preparation | Only under H-law; W-certified: no | No sourced procedure; preparation only at original time (reset_v7 PROBE-PLAN:19); a late controller would need a new pin (causal-interface:91–95) |
| Compiled sources and programs | Mass 1 under the stated prior (P0_NY), by stipulation | Only under H-law; W-certified: no | No; "standalone prepared" (COMBINED-REPORT:110) |
| Late fields q8 and the chain (carry y, s) | Free of unprepared influence under the stated prior (P0_NY) | Only under H-law; W-certified: no (private cells) | Only through the original-time pins |
| Whole-q9 record at L | Mass 1 on each context under the stated prior, given the pins | Yes; W-certified: yes, but only through a stipulated read under H-access (NC1:150–151 [draft]), which is not sourced record formation | Only through the pins. It carries s, so it is a record, not a blank resource |
| Blank port prefixes before a_i | Mass 1 under the stated prior (bank prior and pins) | Yes; W-certified: yes, but only through stipulated port reads under H-access (history_v9:50–52; history_v11:46) | Only through the pins; each port is blank once, until its deadline |
| Banks and 28 keys | Positive mass under H-prior-NC; uniform | Not applicable: background, not ready; private by design and used as masks | Not applicable (uniform) |

## 3. Cross-cutting findings (each anchored; none is a no-go)

1. **Governing question: not shown in the sources read.** No observer-accessible ready resource
   for this interface is shown to follow without a specially imposed low-entropy initial condition. Every ready element in
   §2 traces to original-time pins of P0_NY, and RM:1140–1141 states readiness is "supplied, not derived".
2. **Pressure test, scoped.** The favourable reading is that late prepared-looking fields are produced natively.
   Two instances bound that reading, and both notes record their own review as pending:
   - the q8/q9 chain, whose cones lie inside the prepared balls (causal-interface:79–89, PP);
   - one register cell, which pulls back onto a pinned original cell (apparatus-register:58–77, EB).

   Generalizing to every late field is not sourced. The proposal (§3) records a *reviewer argument
   (round-2 review R2-3), not a sourced result*: with no pinned cell in the pullback of (E, W), the joint
   law of (E, W) under P0_NY equals that under the counting measure, so any readiness comes from
   correlation with W. That routes the case to stipulated reads (H-access), which are not sourced.
3. **The non-pinned resources are background, not readiness.** P0_NY's banks and keys are uniform and
   private (kernel:94–96), and they act as masks (cone-reduction:51; LA `EMPTY`). MR★:1347–1348 ("every
   region is uniform") is stated for the selected counting measure within K1's source set. No native-Y
   source read restates it.
4. **Entropy bookkeeping.** Under a bijection the entropy of the pushed-forward law is invariant, "so a
   ready supply of low-entropy pointer states is a resource" (MR-pre:184–187). Whether a less-structured,
   non-uniform prior builds local low entropy through correlations is not addressed in the sources read.
5. **Readiness and recording are separate.** The only native imprint in Q3 is transport, before the
   interface, into prepared cells with stipulated reads. No carrier→apparatus record is sourced inside the interface.
6. **Single-use is classifiable on its own** (readiness only; Q3 open). P0_NY supplies one single-use ready
   package under the retained assumptions. A fresh package and renewal are separate gaps (Q4).
7. **Main §4.6** (conditional on (EM)) places observers out of equilibrium but supplies no prepared
   region (MR★:1356–1357; Main:744, 758).

**Source-wording findings** (for the owner; no edit made):
- **F-1, confirmed in review.** MR★:1353, "No principle in the corpus supplies one.", is unscoped.
  C.1-1 (MR★:1527–1532) scopes only the sentences at 1358–1359 and AW-MR10 (1481–1482).
- **F-2, a wording ambiguity, not an overclaim.** NC1:25–26 [draft] "randomly selected by native dynamics"; NC1:20–22,
  142–146 [draft] name the prior. Suggested: "a function, through the native dynamics, of original variables random under the supplied prior".
- **F-3, sharpened in review.** Main:758 scopes "replaced" three ways ("within that description"; the
  role "to select observer-compatible configurations"; the rate condition τ_mix ≪ τ_S). Main:744 says
  "replaces" without the role or the rate condition (§A.25). Mirrors located by the reviewer's grep but
  not read: Substratum:56, 401, 551; Explainer:930; Complexity.

## 4. Explicit non-claims
No no-go of any scope; no claim that a ready supply cannot exist (cf. MR★:1504); no contextuality, instrument or QM
claim; no premise adopted; no row, grade, hold or token moves; NC-1 is draft, never evidence; "not found" is not corpus-wide.

## 5. Open points and owner questions
1. **The known reference state.** The authorization (#914 c. 6556989366) admits "a known reference
   state", so readiness relative to the observer's records is in scope. What remains open is how the record that
   makes the state known is sourced without assuming the resource under test (proposal gate G8). Also
   open: whether H-law, the observer's knowledge of the preparation law, is acceptable at all.
2. **Selection priors (owner question).** Should a named prior-selection class be admitted as a
   hypothesis H-sel, so that it yields RR-AVAILABLE[H-sel] and never DERIVED? Candidates are MR★:1364–1366
   route (i) and Main §4.6 under (EM). The question applies equally to non-uniform priors (finding 4).
3. **F-1 to F-3.** Correct, scope, or leave to the owning thread? (The ball count 25 = 24 + 1 is as stated, not recounted.)
