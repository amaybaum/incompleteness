# Introduction r7 design: register of new claims

Revision 7 applies the re-check of design r6 (`S/paper/design-r6-review/RECHECK.md`) to this register:
- C1: N-BH2 and N-BH3;
- C2: N-BH1;
- C3: N-DI1;
- O2: the Weinberg gate in §L.

The rest is r6's text.

This register lists every claim r6 makes beyond r4, under the owner's scope of 2026-10-26: quantum emergence, the
cosmological constant and black-hole information.
- r4's own results are carried at their reviewed strength, with the exact statement, status, reference and witnesses
  given in OUTLINE-r6 "Results register".
- Exact wording is in `OUTLINE-r6.md`.
- Review items are cited as R1–R19 and nits 1–9 of `S/paper/design-r5-review/REVIEW.md`.

## Key

**Status:** proved / conditional (on X) / identity / prose observation / not established / interpretation / open /
structural.

**Agreement:** none of the claims below involves an empirical number compared with data. r6 contains no numerical
agreement and no prediction.

**Literature:**
- **[abs]**: arXiv abstract read first-hand on 2026-10-26, body not read;
- **[mem]**: not read; supports no sentence.

## Register

| ID | Claim (short) | Status | Source at 687e885b | Layer | Literature |
|---|---|---|---|---|---|
| N-AB1 | Abstract: OI places the zero-point sum and the effective Λ at different levels of description; whether the sum sources curvature depends on underived covariant field equations; a proposal, not a resolution | conditional | GR:356; GR:12 | I, O | — |
| N-AB2 | Abstract: finite computations separate conservation under bijective dynamics from recovery under restricted access; GR's Page curve is not established; the problem is not resolved | proved (finite) and not established | as N-BH1 and N-BH3 | E, O | — |
| N-INT1 | One idea and two consequences; neither application is a demonstrated resolution; §6 states what would decide each | structural, scope (owner caution) | owner decision, 2026-10-26 | — | — |
| N-INT2 | Contributions: no new theorem or physical result; expository; BH results from unpublished repository research records with written proofs and exact or exhaustive checks, whose novelty has not been established | structural, scope (nit 4) | r4:32; BH package READMEs | — | — |
| N-LIT1 | 't Hooft argued that QM may be a tool for analysing a system classical at its core, and discussed reconciliation with Bell | literature report, no priority (R12) | — | L | [tH14] **[abs]** |
| N-CC0 | A Planck-cutoff zero-point density is some 120 orders of magnitude above the observed density; the exact power depends on the convention | identity plus numerical background (R9) | audit `cc.py`; review `chk/indep.py` (5.6×10¹²⁰ to 8.8×10¹²²) | A, N | Weinberg 1989 **[mem]**: to read |
| N-CC1 | The zero-point sum and the effective Λ are defined at different levels of description; a uniform shift changes no visible transition probability, so the offset has no content in the visible statistics | proved (one line, global phase) (R8, nit 7) | GR:356 | A | standard QM; the qualifier says so |
| N-CC2 | Whether the offset sources curvature is a separate coupling question; the covariant field equations are open; the no-cancellation proposal is conditional on them | conditional on the covariant field equations (Level G3 of [GR]) | GR:356; GR:12 | I, O | — |
| N-CC3 | The quantum description does not decide between completions differing by ρ_C g_μν | prose observation (GR:356), used in the weaker form; GR's "same partition and calibration" clause is not verified (R7) | GR:356 | I | — |
| N-CC4 | If the field equations take GR's target form with the substratum's classical stress-energy as source, the zero-point sum is not a source and needs no cancellation; the remaining vacuum term is not computed | conditional; the remaining term is uncomputed (R6) | GR:12; GR:360 | I, O | — |
| N-CC5 | Λ's value is an input; ρ ~ H²/G is the Friedmann normalization of the total density | identity, and a stated input | GR:360; `cc.py` | A | — |
| N-CC6 | The mismatch equals S_dS up to a factor fixed by the cutoff convention; a dimensional identity, not a prediction | identity (R9) | `cc.py`; `chk/indep.py` (8/3, or 1/(6π²)) | A | [CKN99] **[abs]**, not cited for ρ ~ M_P²H² |
| N-CC7 | The coupling of phase-transition vacuum energy is not fixed by the descriptive distinction | open | GR:581 (not repeated); AUDIT AW-3 | O | [KP14] **[abs]** |
| N-CC8 | Deriving the covariant field equations would settle the proposal; until then it reinterprets and does not resolve | open, and a scope statement (owner caution) | GR:12 | O | — |
| N-LIT2 | Trace-free EFE (Λ's value unexplained); sequestering (including phase transitions); Volovik (many-body ground states); OI differs in where it locates the source | literature report | — | L | [EvEMU11], [KP14], [Vol06] **[abs]**, VERIFY. Padmanabhan: to read |
| N-BH1 | Conservation by bijectivity neither implies nor is necessary for accessible recovery; the counts, with "accessible advantage" defined; for bijective dynamics, exact recovery under complete endpoint access and the bound P_succ ≥ 1/\|U\| (32 non-injective maps violate it); these endpoint guarantees are sufficient, not necessary (C2) | proved (finite, exhaustive) | Main:66; BH-01 REPORT:17, :21, :24, :36. Not ch19:72 (R18) | E | [Sha79] VERIFY (r4) |
| N-BH2 | The Page value enters only through H-scramble, which no bijection satisfies from a definite configuration with aligned cuts; the ensemble mean equals S_Page on the full product space and differs in general on a smaller shell (exact counterexample: the diagonal shell, H_m − 1; certified Hamming-weight shells) (C1) | C1 and C6(a) proved; C6(b) a proof reading; C6(c) exact algebra on the diagonal shell (H_m − 1) and intervals for Hamming shells (R1) | BH-02 REPORT:14, :18–20; DIFF-REVIEW §6; review `chk/shell.py` | P, E, A | Page 1993 (r4) |
| N-BH3 | GR's Page curve is not established. H-scramble is open. It requires B∪R closed, in a pure joint state, uncoupled from D and V∖R over whole cycles, which timescale ordering does not supply (≥ 10⁵⁷). The value is established only on a full-product shell (C1). The argument gives only a time average at a fixed bipartition. It is conditional on the covariant field equations in GR's ladder. The problem is not resolved | not established (R2, with #936's "pure joint state") | GR:811, :817, :841, :12; BH-01 REPORT:211–241; BH-02 REPORT:20–21; REVIEW §1 C.4; DIFF-REVIEW §6 and R1; DIFF-RECHECK §2 and §5 N1 | E, A, O | Penington 2020 (r4) |
| N-BH5 | Open steps: GSL not derived; QES agreement not established; islands–cycles conjectural | open | GR App. A.6; r4:201 | O | [Pen20] (r4) |
| N-DI1 | *If* the hypothesis holds, the fixed-basis statistics are an embedded observer's visible laws (Theorem 1), and their departures from Markov behaviour are hidden memory; the operational extension is conditional on (i)–(v), which OI does not imply (C3); vacuum energy becomes a coupling question and BH information separates into conservation and recovery | interpretation, conditional on the hypothesis | Theorem 1 (Main §3.4); r4:122; §§4–5 | I | — |
| N-DT1 | Decisive open tests: completion conditions (iii)–(v) and (C4) at the cosmological partition; no experimental discriminator or memory-witness constraint yet; the covariant field equations; H-scramble, closure and the shell for the Page value | open | GR:20, :52; Main:704; GR:12; N-BH3's sources | O | [BBS24] (r4, VERIFY) |

## Removed claims (owner scope), formerly in pre-scope r6

| Former ID | Topic | Reason |
|---|---|---|
| N-HT1, N-HT2 | horizon entropy, ħ, the 1/4 | not an application. No supporting sentence is needed: §4 uses S_dS only as a standard quantity |
| N-BH4 | Page-time fraction, β | not needed for preservation versus recovery |
| N-PE1 | PE-01 | supports none of the three |
| N-AR1 | arrow of time | supports none of the three |
| N-MR1 | measurement reading | supports none of the three |
| N-EX2, N-EX3 | Cabibbo, JUNO | removed from this paper |
| N-INT3 | status key distinguishing prediction from agreement | no numerical item remains |
| N-GC1 | gravitational-coupling paragraph | folded into N-CC2, N-CC8, N-BH3 and N-DT1 |

## L. Literature status

### Read at abstract level

Records are in `S/paper/design-r5/dl/`; the review confirmed each use.

| Key | Supports | Does not support |
|---|---|---|
| [tH14] 1405.1548v3 | a classical core analysed with quantum methods; reconciliation with Bell | priority; the D ⊆ Q direction |
| [EvEMU11] 1008.1196v2 | trace-free EFE resolve the discrepancy without explaining Λ's value | — |
| [KP14] 1309.6562v2 | sequestering, including phase transitions | — |
| [Vol06] gr-qc/0604062v4 | the many-body ground-state argument | — |
| [CKN99], [Jac95] | not cited | the AUDIT's [mem] attributions |

**Cited in r4 and kept:** [Cal26] (abstract-level, VERIFY).

### To read before any citation or claim

Coordinator's list and review O4. Nothing is claimed from any of these.

| Work | Relevance |
|---|---|
| Weinberg 1989 (*RMP* 61, 1) | the standard CC-mismatch source (N-CC0). **Landing gate (O2):** read first-hand and cited before the paper lands |
| Padmanabhan, emergent-gravity papers | the closest analogue of §4; likeliest referee comparison |
| Adler 2004 | emergent QM (§2.2, beside N-LIT1) |
| Wetterich | quantum mechanics from classical statistics (§2.2) |
| Spekkens 2007 | epistemic restriction, close to "restricted access" (§2.2) |
| Elze | cellular automata and QM (§2.2) |
| Also: Henneaux–Teitelboim, Unruh (unimodular gravity); Breuer 1995, Wolpert 2008 (embedded-observer limits) | — |

### Novelty

r6 assigns no priority and claims no new viewpoint (R12).

## Summary for the owner

r6 has three parts.
- **Quantum emergence.** Theorems 1–4 and the supporting results are machine-checked or proved on paper, each with
  its reference; the steps that are not machine-checked are named.
- **The cosmological constant.** A conditional proposal: the zero-point sum needs no cancellation *if* the covariant
  field equations take GR's target form. Those equations are not derived, and the remaining vacuum term is not
  computed.
- **Black-hole information.** A proved finite separation of conservation from accessible recovery, together with a
  Page curve that is not established.

**Neither application is a demonstrated resolution.** The paper contains no numerical agreement and no prediction.
