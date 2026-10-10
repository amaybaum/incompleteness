# Premise ledger — consolidated architecture and obligations (checkpoint 2)

Read-only audit of the corpus at base `0f2687b7`. No repository change; no act, freeze or manuscript implication.
Checkpoint 1 (`SUMMARY.md` `19f4bfad`) is frozen and unchanged; this checkpoint extends it with the three families
audited since — the general interface G, R4-MEASURED-EFFECT, and the empirical inputs E1–E7 — and adds no claim that
is not in a frozen entry. Source of every statement: the frozen entry named in brackets.

Frozen entries added this round: L-G `64804253` · L-R4ME `1db9a3ce` · L-E `e2904486` (= current LEDGER.md).
Everything in checkpoint 1 §§2–3 (representation core; realization table for A1–A6) stands as written there.

***

## 1. The architecture, both tracks

```
                         E1(op) + M1-T            E4                 E4 (quadratic order)       E3a · E3b · E5–E7 · E2 + M1-B
                               │                    │                      │                             │
 corpus:   [R] observable-law representation ──► [B1] H-T1 ──► [B2] H-T2 ──► [Z] realization / selection ──► SM ; GR*
                               │
                               │ G-OBL-1 (not constructed)
                               ▼
 Track I:  [G] operational interface ──► [R4(r_I; G_I)] ──► [Q] QM-selecting premises
                                                                                    * GR via GR/SUBSTRATE BRIDGE (held; Track II)
```

The corpus line is checkpoint 1's. The Track I line is the program's three-layer split: its G and R4 layers are
program premises, not corpus premises, and the corpus's own substrate constructions do not reach G (below).

Beside each arrow, only what is unresolved. Rows marked ¹ are checkpoint 1's and carry over unchanged.

| Arrow | Unresolved obligations |
|---|---|
| R → B1 ¹ | OBS-1 (OBS-M → OBS-C map) |
| B1 ¹ | O-a/b, O-d, O-f, O-g |
| B1 → B2 ¹ | none beyond B1 for OBS-C; the OBS-M route to isotropy is a candidate |
| B2 ¹ | T2-1 … T2-6 |
| B2 → Z ¹ | identification of g with spacetime geometry (realization) |
| Z → SM/GR/Q ¹ | the realization premises, each with its replacement obligation |
| **R → G** | **G-OBL-1**: the corpus realizes passive readout (MM-P) and action-labelled interventions without outcomes (MM-A); a substrate-level, field-neutral realization with **selective outcomes and a record** is not constructed (Main.md:458, :468). Until it is, G-BR and G-REC are stipulated of the interface, not realized by the substrate. [L-G] |
| **G** | **G-OBL-2**: G-INV (operational invasiveness) is a property of rule × interface × observer, and every use must name all three. **G-OBL-3**: any theorem proved in the matrix-carrier model MM-K is a matrix-setting theorem (G-MATRIX). [L-G] |
| **G → R4** | R4-MEASURED-EFFECT (r_I ∈ E) is **chosen**, at level R4. Invariance is required only under non-selective generators (selective-branch lemma), which are defined by G-FS, so R4(r; G) depends on that identity. R4 is a family indexed by interface; an exclusion proved for one index does not transfer to another. [L-R4ME] |
| **R4 → Q** | the Q-layer premises are not audited here. The corpus's own placement agrees with the layering and is proved: MM-K (iii) inert spectators, (iv) full reversible control and (v) iterated composition are substantive selection principles, and bare finite OI ⇏ QM (`oi_alone_not_qm`, `five_way_minimality`; GR.md:224). [L-G] |
| **E → corpus** | as in the table of §3, column "consumed by". |

***

## 2. The interface layer G and the R4 premise

**Four measurement models, not one** [L-G]:

| Model | Outcomes / record | Setting |
|---|---|---|
| MM-P Main passive readout | the configuration is the outcome; nothing is disturbed | field-neutral |
| MM-A Main intervention dilation | action labels, no outcomes | field-neutral, classical comb |
| MM-K operational completion | instruments with outcomes | matrix carrier |
| MM-R RECORD | one-bit record, pair map, leap | field-neutral |

**Clause kinds** [L-G]:

| Kind | Clauses | Consequence |
|---|---|---|
| definitional | G-BR selective branches · G-REC separate record · G-SPLIT system/record · G-DIST disturbance permitted | they define the interface class |
| exact identity | G-FS non-selective = forgetful sum · G-UNIT normalization · G-COMP consistent composition | RECORD's checks of these tested the simulator's faithfulness, not nature. G-FS's *test power* is interface-dependent |
| **substantive** | **G-INV** operational invasiveness | interface-relative: for the linear rule under MM-R it is false at Level 1 (proved, all 143 interfaces) and true at Level 2 for 76/143; for the nonlinear and majority rules it is true for all |

Under MM-K, (i) valid probabilities and (ii) trivial-ancilla consistency are well-formedness conditions, and (iii)–(v)
are the selecting work. All are stated inside a setting that already contains the matrix carrier (**G-MATRIX**). The
field-neutral G is the program's own and does not appear in the papers.

**Not G in general** (specific to RECORD): the one-bit record copying v₀, the pair map κ_b, the leap after
observation, the single-site visible pair, the seed r = (o, 1), and the Level-1 and Level-2 letter sets.

**R4-MEASURED-EFFECT** [L-R4ME]:
- **Statement:** r_I ∈ E. **Level:** R4. **Status:** chosen.
- **Its only consumer** is the orbit-span exclusion: r ∈ E gives C(r; G) ⊆ E, so a certified lower bound > 4 excludes R4(r; G).
- **No corpus counterpart.** The papers fix no elementary-system dimension.
- **No circularity found.** The clause encodes no linearity, dimension, convexity, complex structure or composite.

**Observer applicability** [L-G; OBS-1]:
- **OBS-R:** RECORD's observer, an OBS-M-type spatial partition with an invasive interface.
- **G-BR, G-REC and G-INV are present only for OBS-R and MM-K.** They are absent from OBS-M's passive theorems and undefined for OBS-C.
- **No G result transfers** between these without a stated map.

***

## 3. Empirical inputs: anchors versus theory with an empirical label

| Input | What is observed, at what level | Bundled theory | Consumed by | If weakened or removed |
|---|---|---|---|---|
| E1 | finite-precision quantum statistics, operational; interference at μ = 15.5 | the Hilbert-space formalism | Stage 1 (with M1-T); A2b's empirical anchor | representation survives under "observed statistics are finite-horizon laws"; only A2b's anchor is lost |
| E2 | Bell violations, operational, composite | none | M1-B; Bell completion; H-Bell | local completions suffice; the representation core is unaffected |
| E3a | **not directly observed**: holographic bound applied to the finite cosmological horizon area | finiteness as a dimension cutoff dim ℋ ≤ e^{A/4} | A1-F2, its single interpretive premise | A1-F2 loses its premise; L-A1's infinite-deep-sector replacements apply (recurrence-scale results → accessible-window statements) |
| E3b | **not observed**: holographic and Bekenstein bounds | area scaling | the gravity calibration only (ħ, ε, 1/4) | with E3a alone, A1-F2 and every accessible-time result survive; the calibration loses its input |
| E4 | continuous rotation invariance, observer level | none | form lemma; H-T1 clause b; Corollary 1a | matched by discrete O_h at quadratic order only (quartic O(a²)) |
| E5 | gravitational-wave detections, operational | d ≥ 3 is Einstein-gravity-specific | Stage 2(a) d-selection | leaves d ≤ 3 |
| E6 | existence of atoms, operational | Gauss-law and Schrödinger scaling | Stage 2(a) | d = 3 then rests on E5 + E7 |
| E7 | **inferred** ΛCDM flatness parameter (§A.24) | derived ratio 2/(d−1) | Stage 2(a) consistency check | removable without losing d = 3 (SM.md:196) |

[L-E]

**Findings** [L-E]:
- **Genuine operational anchors:** E2, E4, the statistics behind E1, the detections behind E5, and the atoms behind E6.
- **E1 is stronger than its consumers need.** Its Hilbert-space clauses are not consumed.
- **E3 is split.** The corpus's internal graph area law does not discharge E3b (T-A3-1, T-A3-2).
- **E5 forms a loop for Track II.** It selects d using a property of the theory then reconstructed; this is recorded for the GR/SUBSTRATE BRIDGE.
- **E4 is where an empirical input meets H-T2's one-geometry requirement.**

**Named but not audited:**
- **M1-T:** observed temporal data lie in the accessible sector.
- **M1-B:** Bell composites take the measurement-independent, ontically parameter-dependent branch.

These map E1 and E2 onto C1–C4 and the Bell completion. They are selection premises, neither empirical nor structural.

***

## 4. Level map of the whole ledger

| Entry | Level | Kind of premise |
|---|---|---|
| A1, A2, A3, A4, A5, A6 | SUBSTRATE (A3-OBS and the observer parts of A4 are observer-side) | posits / sharpened stipulations; split per checkpoint 1 §3 |
| H-T1, H-T2 | bridges: SUBSTRATE → observer → continuum | conditional theorems with named obligations |
| G clauses | INTERFACE (G) | definitional / exact identity, except G-INV (substantive, interface-relative) |
| R4-MEASURED-EFFECT | R4 | chosen |
| MM-K (iii)–(v) | Q (corpus placement) | substantive selection principles |
| E1–E7 | inputs: OBSERVATION (operational or inferred), with bundled theory per §3 | empirical / theory-laden |
| M1-T, M1-B | selection (unaudited) | — |

***

## 5. Control axes for a later level (updated; nothing run)

These are the axes checkpoint 1 knew:
- A5 (linearity);
- A4-S (self-coupling);
- the hidden-law class (product vs correlated preparations);
- the observer notion.

This round adds:
- **Interface I** (alphabet, letter set, record map). G-INV and R4(r_I; G_I) are both indexed by it, so any rule
  comparison must hold I fixed, and any interface comparison must hold the rule fixed.
- **Measured effect r_I.** It is part of the R4 index; changing it changes the premise tested.
- **Setting** (field-neutral vs matrix carrier). RECORD's runs are field-neutral, while the corpus's operational
  characterization is matrix-setting (G-MATRIX). A result in one setting is not evidence in the other.

RECORD's three rules differ from one another in A5 **and** A4-S together. They all satisfy A2, A3-NN (d = 1) and A6,
and all share one field-neutral setting. The candidate orthogonal rules recorded in L-A4 remain held.

***

## 6. Drift and claim/evidence items (record only; none harmonized)

Checkpoint 1's 23 items are left untouched, as directed. This round adds four:

| ID | Site(s) | Item | Kind |
|---|---|---|---|
| T-E-1 | Substratum.md:76 | E1 states the Hilbert-space formalism as an observation; consumers use finite-horizon statistics (+ A2b anchor) | claim/evidence |
| T-E-2 | Substratum.md:80 | E3 (holographic bounds) listed among "facts about the observed universe" | claim/evidence |
| T-E-3 | Substratum.md:84; SM.md:170 | E5's d ≥ 3 is Einstein-gravity-specific, used to select d for a reconstruction of Einstein gravity | circularity (Track II) |
| T-E-4 | Substratum.md:88 | E7 compares a derived ratio with an inferred ΛCDM parameter, not a raw observable (§A.24) | external-comparison level |

G-MATRIX is a setting classification, not a drift item: the corpus describes its own theorem as "an axiomatic
completion theorem, not a derivation" (GR.md:240).

Total recorded: 27 items, all inputs for a future §A.25 propagation round under owner direction.

***

## 7. Not yet audited

- The Q-layer premises themselves: strict convexity, continuous reversible transitivity, and MM-K (iii)–(v) beyond
  the corpus's own classification.
- M1-T and M1-B.
- The GR/SUBSTRATE BRIDGE (Track II; the E5 loop is recorded for it).
- G1's A5-freedom, which is declared but not line-checked; and the book mirror beyond the premises audited.
- **Level 3 design**, which is held for owner direction. The extension proposed in `record/PROPOSAL-LEVEL3.md`
  predates checkpoint 2. Read against §5, a CNOT on the visible pair changes the interface I with the rule fixed, so
  it is an interface-axis move. It does not separate A5 from A4-S.
