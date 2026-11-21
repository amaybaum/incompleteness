# C14 correction packages (proposals only; nothing is applied)

**Status: WIP / UNVERIFIED.** These are proposed corrections for the findings of `../AUDIT.md` (reviewed CONFIRMED WITH NITS, c.7066874849; nits applied at `022d750e`).

**Application.**
- Each package is to be applied only after the A1 retirement, separately reviewed, and re-cut against the refreshed `main`.
- Before application, `check_packages.py <refreshed main>` must report READY. Any package it reports STALE is re-cut first.
- After application, the release gate, the guards and the Lean build run in CI. They were not run here.

**What is authoritative.** `packages.json` is authoritative for the exact old and new texts. The texts are reproduced below for review.

**Term.** A *faithful realization* of a visible process is a deterministic realization of it: a bijection $\varphi$ on $\mathcal{C}_V \times \mathcal{C}_H$ with an initial law under which the visible trajectory has the process's law. This is Main:614, the hypothesis of the theorem on unavoidable hidden predictive memory. The packages' necessity wordings ("C1, C3 and C4 hold in every faithful realization") are stated relative to that notion. C2's persistence form is stated for bijective realizations (Main:74).

**Canonical source.** Every package follows `papers/Main.md` §1.3 (Main:72 C1, :74 C2, :76 C3, :78 C4) or the theorem named in its row.

**Ledger.**
- No package touches a line that #1477's ledger (`edits.json` at `55544cc3`) edits.
- Checked by `check_packages.py`, column c.
- **ch02:88 / FULL:718 is excluded.** Its F9 "C2-mixing" is routed to #1477's final scientific review (#1169 c.7067233614).

**Drafting-base check (`022d750e`).** `python3 -I verification/audits/foundations/c14-audit-20261121/corrections/check_packages.py 022d750e` reports:
- 53 packages, 0 failing: verdict READY;
- every old text unique in its file;
- every book package's old text also unique in `FULL.md`;
- no ledger line or overlap.

**Guard pins found by the 30-character span scan.**
- *A real pin.* `verification/lean/edge_rigidity_probe.py:1180–1189`, the canonical C-numbering guard, pins the IndependenceCensus docstrings. The F14 packages were shaped to keep it: a static replay of the guard's substring tests on the patched text holds.
- *Phrase-family matches.* The other spans are shared-phrase matches with `architecture_check.py`'s forbidden-phrase examples, `memory_probes.py` and `bohr_frequency_probe.py` comments.
- *Kernel identifiers.* `edge_rigidity_probe.py:3143` requires the three kernel identifiers in Main:524's paragraph, which P-F15-1 keeps.
- *All of these* must still be re-run in CI after application.

**Dependencies common to every package.**
- §A.25 propagation: the book chapter, `FULL.md` and companion papers change together.
- §A.25 step 5: the `.tex` and `.pdf` are regenerated, or flagged stale, in the same commit.
- `verification/audit-census.json` hit counts are re-derived (`verification/lean/audit_census_probe.py`) for any edited phrase it counts.
- §A.32/§A.33 voice checks run on the added paper lines.
- The Lean-manuscript census (§A.35) is unaffected: no cited kernel identifier changes.

**Line numbers.** Line numbers are at the drafting base and will move after the retirement. Packages anchor on their exact old text, not on line numbers.

**Order.** Packages are listed in the reviewer's impact order: F3, F5, F7, F2/F2b, F11, F4/F12, then the rest.

## F3 — necessity claims narrowed to what Main proves

### P-F3-1 — `papers/Structure.md:110`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism).
- **Preserve:** the (C1)-(C4) list at Structure:112-118 that follows; Level B's role in Structure's level hierarchy; the citation [Main §3].
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
The framework identifies four conditions on a substratum's bijection $\varphi$ that are necessary for an embedded observer to exist [Main §3]:
```

New:

```text
The framework identifies four conditions on a partition of a substratum's dynamics that diagnose when an embedded observer's reduced description carries the memory-bearing sector [Main §1.3]. C1, C3 and C4 hold in every faithful realization of accessible non-Markovian visible statistics; C2 is a physical-regime premise [Main §3.4]:
```

### P-F3-2 — `papers/Structure.md:734`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism); Main:153 (bijections failing C1 are an exponentially vanishing fraction as n_H grows).
- **Preserve:** the paragraph's structural-anthropic reading that follows; the observer-admitting/observer-lacking distinction of Structure:518 and :711.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.
- **Note:** The removed typicality clause also conflicts with Main:153, where bijections failing C1 are an exponentially vanishing fraction as n_H grows. This conflict was confirmed in review (#1529, c.7067421634).

Old:

```text
Most arbitrary $(S, \varphi)$ pairs do not admit observers — random permutations on finite sets typically lack the coupled-dynamics, slow-local-mixing, and high-capacity features required for C1–C4.
```

New:

```text
Not every $(S, \varphi)$ pair admits observers: admission requires a partition satisfying C1–C4.
```

### P-F3-3 — `book/ch18-beyond.md:276`; FULL.md:5007

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism).
- **Preserve:** Direction 1's conditional framing (consciousness requires non-Markovian processing is the direction's hypothesis, not a result).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
The C1–C4 architecture is necessary for the non-Markovian information processing that conscious systems must exhibit.
```

New:

```text
In every faithful realization of the non-Markovian information processing that conscious systems must exhibit, C1, C3 and C4 hold, and C2's persistence form holds in every bijective realization; C2's slow-bath form is not necessary ([Main §3.4]).
```

### P-F3-4 — `book/ch18-beyond.md:286`; FULL.md:5017

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism).
- **Preserve:** the paragraph body (Strict feed-forward accounts face this constraint).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
*C1–C4 architecture is necessary for non-Markovian information processing.*
```

New:

```text
*C1, C3 and C4 hold wherever non-Markovian information processing is faithfully realized.*
```

## F3 with F2 — ch18 necessity sentences that also type C1–C4 as structural

### P-F3-5 — `book/ch18-beyond.md:24`; FULL.md:4755

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism); Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the surrounding enumeration of constraints in ch18:24.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
the C1–C4 architecture provides necessary structural conditions for the non-Markovian information processing conscious systems must exhibit;
```

New:

```text
C1, C3 and C4 hold in every faithful realization of the non-Markovian information processing conscious systems must exhibit;
```

### P-F3-6 — `book/ch18-beyond.md:296`; FULL.md:5027

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:70 (diagnostics, not hypotheses); Main:546-552 (characterization theorem: (iii) lists C1, C3, C4; C2 absent); Main:74 (C2-structural by reversibility in bijective realizations; C2-slow one sufficient mechanism); Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the IIT comparison at ch18:294 (C1-C3 as necessary for Phi is a separate application, unchanged).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
the C1–C4 architecture provides the necessary structural conditions for the framework, and IIT's $\Phi$ provides the additional sufficient content for consciousness within that architecture.
```

New:

```text
the C1–C4 architecture supplies the framework's conditions, with C1, C3 and C4 holding in every faithful realization of memory-bearing statistics, and IIT's $\Phi$ provides the additional sufficient content for consciousness within that architecture.
```

## F5 — C4 stated operationally

### P-F5-1 — `papers/Structure.md:118`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:78.
- **Preserve:** Structure:536 (C4 witness for compactifications, unchanged); the cosmological realization clause GR:52 / Main:78 (read-write cycle to be demonstrated).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
(C4) **History readback.** The interaction must read back what was written — the load-bearing memory condition.
```

New:

```text
(C4) **History readback.** At some accessible order, two visible histories with the same present state induce different next-step laws through the hidden state — the load-bearing memory condition. The condition is operational and does not by itself assert a causal write-then-read cycle [Main §1.3].
```

### P-F5-2 — `book/ch09-universality.md:116`; FULL.md:2531

- **Kind:** wording.
- **Canonical source:** Main:78.
- **Preserve:** the capacity inequality in the same item.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
to store the correlations the read-write cycle generates
```

New:

```text
to hold the correlations that readback uses
```

### P-F5-3 — `papers/Introduction.md:85`

- **Kind:** wording.
- **Canonical source:** Main:78.
- **Preserve:** the fair-coin counterexample sentence that follows (Main §2.3 Remark, why (C4) is a separate condition).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.
- **Note:** Optional: Introduction is a non-technical paper.

Old:

```text
and feed the record back into what is seen
```

New:

```text
and make what is seen next depend on what it holds
```

## F7 — C3 as the I* capacity bound

### P-F7-1 — `papers/Structure.md:116`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:76; Main:522 (cumulative reading needs a no-reuse hypothesis).
- **Preserve:** Structure:140 (A1 related to but distinct from C3; a #1477 ledger line, not touched).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
(C3) **Sufficient capacity.** The hidden sector must have information capacity enough to store the interaction history.
```

New:

```text
(C3) **Sufficient capacity.** The hidden sector must have enough distinguishable states to encode the observed conditional past–future information, $\log_2|\mathcal{C}_H| \geq I^*$ [Main §1.3].
```

### P-F7-2 — `papers/Structure.md:534`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:76; Main:522.
- **Preserve:** the holographic-bound translation that follows in the same item.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
- *C3 (sufficient capacity)* requires the hidden sector to have sufficient information capacity to store the interaction history.
```

New:

```text
- *C3 (sufficient capacity)* requires the hidden sector to have enough distinguishable states to encode the observed conditional past–future information, $\log_2|\mathcal{C}_H| \geq I^*$.
```

## F2 — 'structural conditions C1–C4' relabelled

### P-F2-1 — `papers/GR.md:617`

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the universality claim's three parts at GR:617-623 and their conditions.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
satisfying [Main]'s structural conditions C1 (non-trivial coupling)
```

New:

```text
satisfying [Main]'s conditions C1 (non-trivial coupling)
```

### P-F2-2 — `papers/Structure.md:528`

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the translation list Structure:530-536.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
The structural conditions for observer admission [Main §3] are formulated
```

New:

```text
The observer-admission conditions [Main §3] are formulated
```

### P-F2-3 — `papers/Structure.md:711`

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the observer-admitting definition and its use at Structure:734.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
satisfying the framework's structural conditions C1–C4 (coupling, record persistence, sufficient capacity, history readback)
```

New:

```text
satisfying the framework's conditions C1–C4 (coupling, record persistence, sufficient capacity, history readback)
```

### P-F2-4 — `book/ch09-universality.md:88`; FULL.md:2503

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the conditional chain (H-slope, GR §8.5(b)) stated in the same paragraph.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
any substratum with the framework's structural conditions at its horizon
```

New:

```text
any substratum with the framework's observer-admission conditions at its horizon
```

### P-F2-5 — `book/appendix-c-objections.md:172`; FULL.md:6327

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the enumeration of distinctive content.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
the C1–C4 structural conditions, the specific
```

New:

```text
the C1–C4 observer-admission conditions, the specific
```

### P-F2-6 — `book/appendix-c-objections.md:291`; FULL.md:6446

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the interconnection response.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
(C1–C4 structural conditions operating at different scales)
```

New:

```text
(C1–C4 conditions operating at different scales)
```

### P-F2-7 — `book/ch11-origin-of-life.md:10`; FULL.md:2973

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the replicator realization claim (Complexity:286 parallel).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
the framework's structural conditions C1, C2, C3, C4 at the molecular scale
```

New:

```text
the framework's conditions C1, C2, C3, C4 at the molecular scale
```

### P-F2-8 — `book/ch14-quantum-computing.md:107`; FULL.md:3707

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** the clause 'through the readback gap of C4' (C4 carries the memory).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
- The framework's structural conditions C1–C4 guarantee accessible conditional memory
```

New:

```text
- The framework's conditions C1–C4 guarantee accessible conditional memory
```

## F2b — the canonical paper's own slip (Main:326) and its mirror

### P-F2b-1 — `papers/Main.md:326`

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636; Main:74 (persistence, not slowness).
- **Preserve:** the swap-example clause that follows (entanglement-breaking channel satisfying (C1)); appendix-b:90 mirrors this sentence.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
not an additional structural condition: (C1)–(C4) constrain coupling, timescales, and capacity
```

New:

```text
not an additional condition: (C1)–(C4) constrain coupling, record persistence, capacity and readback
```

### P-F2b-2 — `book/appendix-b-derivations.md:90`; FULL.md:5767

- **Kind:** label.
- **Canonical source:** Main:74 ('a physical-regime premise, not a structural condition'; 'C1, C3 and C4 are the structural conditions'); Main:636.
- **Preserve:** mirror of Main:326 (P-F2b-1); apply together.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
not an additional structural condition: (C1)–(C4) constrain coupling, timescales, and capacity
```

New:

```text
not an additional condition: (C1)–(C4) constrain coupling, record persistence, capacity and readback
```

## F11 — the missing C4 item in ch09

### P-F11-1 — `book/ch09-universality.md:118`; FULL.md:2533

- **Kind:** wording.
- **Canonical source:** Main:78.
- **Preserve:** ch09:84 ('C1–C4 specify the admission criterion'); the italic run-in format of ch09:112-116.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.
- **Note:** Inserts the missing C4 item before ch09:118; the item becomes a new copy in FIN-SCOPE's C4 node group.

Old:

```text
These conditions specify the observer-admission criterion on the stated finite representative.
```

New:

```text
*C4 (history readback).* At some accessible order, two visible histories with the same present state induce different next-step laws through the hidden state ([Main §1.3]). The condition is operational; it does not by itself assert a causal write-then-read cycle.

These conditions specify the observer-admission criterion on the stated finite representative.
```

## F4 — C1 without a magnitude requirement

### P-F4-1 — `papers/Structure.md:112`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72.
- **Preserve:** none beyond the list.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
(C1) **Coupling.** The interaction between the observer's degrees of freedom and the rest must be substantial.
```

New:

```text
(C1) **Coupling.** The hidden degrees of freedom must affect the observer's visible evolution at some accessible step: the conditional law of some visible transition depends on the hidden state [Main §1.3].
```

### P-F4-2 — `papers/Structure.md:530`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72.
- **Preserve:** the EFT translation and 'Compactifications with completely decoupled hidden sectors fail C1' (unchanged, still correct).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
- *C1 (coupling)* requires substantial coupling between visible-sector and hidden-sector dynamics.
```

New:

```text
- *C1 (coupling)* requires that hidden-sector dynamics affect some accessible visible transition.
```

### P-F4-3 — `book/ch18-beyond.md:276`; FULL.md:5007

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72.
- **Preserve:** Direction 1's conditional framing.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
Any conscious system must implement a partition with substantial C1–C4 structure.
```

New:

```text
Any conscious system must implement a partition with C1–C4 structure.
```

## F12 — application paragraphs held to C1's requirement

### P-F12-1 — `book/ch13-quantum-biology.md:50`; FULL.md:3471

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72; ch01:53.
- **Preserve:** the mechanisms listed earlier in ch13:50.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
C1 is satisfied with substantial coupling strength.
```

New:

```text
These mechanisms motivate C1; establishing it requires showing that scaffold variation affects an accessible active-site conditional under a specified preparation (Chapter 1 §1.3).
```

### P-F12-2 — `book/ch11-origin-of-life.md:152`; FULL.md:3115

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72; Main:72 status ('One-way influence can suffice'); Medicine:88.
- **Preserve:** the autocatalytic-network sentence that follows.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
The template must direct synthesis of new molecules (catalyzing the reaction), and the synthesis must maintain the template (either by producing copies of the template or by producing molecules that contribute to template stability).
```

New:

```text
The template must direct synthesis of new molecules (catalyzing the reaction); C1 requires only this influence. In the proposed replicator the synthesis also maintains the template (either by producing copies of the template or by producing molecules that contribute to template stability), a feedback that belongs to the realization rather than to C1.
```

## F1 — C2 named and stated by persistence; the ch01 C2 table row

### P-F1-1 — `book/ch13-quantum-biology.md:52`; FULL.md:3473

- **Kind:** label.
- **Canonical source:** Main:74.
- **Preserve:** the tau ratios in the paragraph (C2-slow application, unchanged).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
**C2: conformational timescale separation.**
```

New:

```text
**C2: conformational record persistence (timescale separation as the route).**
```

### P-F1-2 — `book/ch18-beyond.md:68`; FULL.md:4799

- **Kind:** wording.
- **Canonical source:** Main:74.
- **Preserve:** ch18:64 and :72 (failure of C2 in its timescale form suppresses, not empties).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
- C2 (memory persistence): the hidden sector must retain a record of the subsystem's past across the accessible window, $\tau_B \gg \tau_S$ with $\tau_B$ the coarse-grained mixing time — slow hidden dynamics is one sufficient mechanism, not the condition itself ([Main §1.3]);
```

New:

```text
- C2 (memory persistence): the hidden sector must retain a record of the subsystem's past until the readback that uses it ([Main §1.3]); the slow-bath form $\tau_B \gg \tau_S$, with $\tau_B$ the coarse-grained mixing time, is one sufficient mechanism, not the condition itself;
```

### P-F1-3 — `book/ch01-observation.md:252`; FULL.md:585

- **Kind:** wording.
- **Canonical source:** Main:74; Main:768 (suppression, not exclusion, short of complete erasure); ch01:215.
- **Preserve:** the column 'What fails'; the sentence after the table (full erasure gives a Markov law).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.
- **Note:** Low priority: the sentence after the table already states the full-erasure limit.

Old:

```text
| C2 | Timescale separation | Markovian stochastic | Thermalized observer |
```

New:

```text
| C2 | Timescale separation, to complete erasure ($\tau_B \to 0$) | Markovian stochastic | Thermalized observer |
```

## F6 — the ch01 C3 table row

### P-F6-1 — `book/ch01-observation.md:253`; FULL.md:586

- **Kind:** wording.
- **Canonical source:** Main:76; ch01:229.
- **Preserve:** the sentence after the table (a shortfall bounds accessible memory; coextensive is the zero-capacity extreme).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.
- **Note:** Low priority, as P-F1-3.

Old:

```text
| C3 | Capacity hierarchy | No observation | Coextensive with system |
```

New:

```text
| C3 | Capacity hierarchy, to zero hidden capacity | No observation | Coextensive with system |
```

## F8 — SM Theorem 22's C1 stated in its coupling form

### P-F8-1 — `papers/SM.md:1376`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72 ('A C1 witness requires influence on an accessible visible conditional under the specified preparation').
- **Preserve:** Theorem 22's proof (unchanged; it proves exactly the coupling form); citers ch01:61, SM:52; Theorem 22's C2/C4 hypotheses.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
the partition (V, H) satisfies C1, with
```

New:

```text
the partition (V, H) satisfies C1 in its coupling form — a dynamical coupling edge across ∂V, $H_{\text{int}} \neq 0$ — with
```

### P-F8-2 — `papers/SM.md:52`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72.
- **Preserve:** the C2/C4-hypothesis sentence that follows.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
C1 holds structurally for any connected coupling graph and proper visible subgraph
```

New:

```text
C1 holds structurally, as a dynamical coupling edge across the cut, for any connected coupling graph and proper visible subgraph (influence on an accessible visible conditional depends in addition on the preparation)
```

### P-F8-3 — `book/ch01-observation.md:61`; FULL.md:394

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:72; SM Theorem 22.
- **Preserve:** the C3 floor and C2/C4-hypothesis clauses in the same paragraph.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
At the lattice cut of [SM §8], C1 is verified structurally under the stated update and cut
```

New:

```text
At the lattice cut of [SM §8], C1 is verified structurally, as a coupling edge across the cut, under the stated update and cut
```

## F9 — 'C2-mixing' replaced by the defined hypothesis (ch02:88 excluded)

### P-F9-1 — `papers/Structure.md:138`

- **Kind:** label.
- **Canonical source:** Main:74 (C2-structural, C2-slow only); Substratum Theorem 23 (:193, 'The slow-bath form of C2 additionally uses the stated mixing hypothesis').
- **Preserve:** the condition stays listed (keeps the citation at least as conditional as now); whether the reconstruction itself uses the mixing hypothesis is an open scope question for review, not decided here.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.
- **Note:** ch02:88 / FULL:718 is excluded: it is routed to #1477's review.

Old:

```text
conditional on C2-mixing
```

New:

```text
conditional on the mixing hypothesis of C2's slow-bath form
```

### P-F9-2 — `papers/Substratum.md:24`

- **Kind:** label.
- **Canonical source:** Main:74 (C2-structural, C2-slow only); Substratum Theorem 23 (:193, 'The slow-bath form of C2 additionally uses the stated mixing hypothesis').
- **Preserve:** the condition stays listed (keeps the citation at least as conditional as now); whether the reconstruction itself uses the mixing hypothesis is an open scope question for review, not decided here.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
(M1-T; C2-mixing; the Stage-2 structural inputs
```

New:

```text
(M1-T; the mixing hypothesis of C2's slow-bath form; the Stage-2 structural inputs
```

### P-F9-3 — `papers/Substratum.md:195`

- **Kind:** label.
- **Canonical source:** Main:74 (C2-structural, C2-slow only); Substratum Theorem 23 (:193, 'The slow-bath form of C2 additionally uses the stated mixing hypothesis').
- **Preserve:** the condition stays listed (keeps the citation at least as conditional as now); whether the reconstruction itself uses the mixing hypothesis is an open scope question for review, not decided here.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
the C2-mixing condition
```

New:

```text
the mixing hypothesis of C2's slow-bath form
```

### P-F9-4 — `papers/Substratum.md:367`

- **Kind:** label.
- **Canonical source:** Main:74 (C2-structural, C2-slow only); Substratum Theorem 23 (:193, 'The slow-bath form of C2 additionally uses the stated mixing hypothesis').
- **Preserve:** the condition stays listed (keeps the citation at least as conditional as now); whether the reconstruction itself uses the mixing hypothesis is an open scope question for review, not decided here.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
together with M1-T, C2-mixing and the nearest-neighbor premise
```

New:

```text
together with M1-T, the mixing hypothesis of C2's slow-bath form and the nearest-neighbor premise
```

### P-F9-5 — `papers/oi_lattice_code/architecture_check.py:1086`

- **Kind:** label.
- **Canonical source:** Main:74 (C2-structural, C2-slow only); Substratum Theorem 23 (:193, 'The slow-bath form of C2 additionally uses the stated mixing hypothesis').
- **Preserve:** the condition stays listed (keeps the citation at least as conditional as now); whether the reconstruction itself uses the mixing hypothesis is an open scope question for review, not decided here.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.
- **Note:** Guard message string only; the guard's pattern and exception list are unchanged.

Old:

```text
reconstruction uniqueness is conditional: C2-mixing, M1,
```

New:

```text
reconstruction uniqueness is conditional: the mixing hypothesis of C2's slow-bath form, M1,
```

## F10 — characterization theorem cited with its hypothesis and name

### P-F10-1 — `papers/Substratum.md:112`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:546 ('Let S be a time-homogeneous stochastic process ... Then (ii) iff (iii)'); Main:614 (unavoidable hidden predictive memory).
- **Preserve:** §A.34: both directions are proved in prose at Main:640, not in the kernel; the equivalence is not strengthened.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.
- **Note:** Whether the proof uses time-homogeneity is open; the qualifier follows the theorem as stated.

Old:

```text
[Main §3.4] Characterization theorem (accessible non-Markovianity
```

New:

```text
[Main §3.4] Characterization theorem (for a time-homogeneous visible process: accessible non-Markovianity
```

### P-F10-2 — `papers/Substratum.md:127`

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:546 ('Let S be a time-homogeneous stochastic process ... Then (ii) iff (iii)'); Main:614 (unavoidable hidden predictive memory).
- **Preserve:** the clause 'with $M_t > 0$ forcing unavoidable hidden predictive memory' that follows.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
[Main §3.4]'s universal hidden-memory theorem — accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon,
```

New:

```text
[Main §3.4]'s characterization theorem — for a time-homogeneous visible process, accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon — and its universal hidden-memory theorem,
```

### P-F10-3 — `book/appendix-b-derivations.md:22`; FULL.md:5699

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:546 ('Let S be a time-homogeneous stochastic process ... Then (ii) iff (iii)'); Main:614 (unavoidable hidden predictive memory).
- **Preserve:** the lemma-chain description.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
The framework's characterization theorem — accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon, with the quantum
```

New:

```text
The framework's characterization theorem — for a time-homogeneous visible process, accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon, with the quantum
```

### P-F10-4 — `book/appendix-b-derivations.md:405`; FULL.md:6082

- **Kind:** overclaim-narrowing.
- **Canonical source:** Main:546 ('Let S be a time-homogeneous stochastic process ... Then (ii) iff (iii)'); Main:614 (unavoidable hidden predictive memory).
- **Preserve:** the appendix's lemma collection.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** the same edit in `FULL.md`.

Old:

```text
The framework's characterization theorem — accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon, the quantum
```

New:

```text
The framework's characterization theorem — for a time-homogeneous visible process, accessible non-Markovianity ⟺ C1/C3/C4 realization per accessible horizon, the quantum
```

## F13 — README present-tense status (forward only)

### P-F13-1 — `verification/README.md:683`

- **Kind:** wording.
- **Canonical source:** GR:46-52; ch07:24-30.
- **Preserve:** forward only: the historical description of the earlier audit's repair is kept, and that audit's own records are not edited (§A.42 item 4).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
The `R7-AUDB` guard holds all of it.
```

New:

```text
The `R7-AUDB` guard holds all of it. The current cosmological-cut status is that of `[GR]` §2.2: C1 motivated by the constraint correlations and not established, C2's timescale a physical input, C3 a mode-count estimate, and C4 not presently discharged.
```

## F14 — Lean CoreC1C4 docstrings (comments only)

### P-F14-1 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:21`

- **Kind:** wording.
- **Canonical source:** Main:74, Main:76.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
All four OI conditions are kernel-named, and bundled as
```

New:

```text
All four OI condition slots are kernel-named (C1 and C4 as instances, C2 and C3 as surrogates; see below), and bundled as
```

### P-F14-2 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:27`

- **Kind:** wording.
- **Canonical source:** Main:74.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
    C2 (memory persistence) is structural, not merely statistical: `v_{t+2} = v_t`
       (`core_visible_period_two`), so the visible stream carries a real one-bit memory.
```

New:

```text
    C2 slot: `v_{t+2} = v_t` (`core_visible_period_two`), a consequence about the visible stream.
       It is not [Main]'s C2, the persistence of a hidden record to the readback that uses it.
```

### P-F14-3 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:29`

- **Kind:** wording.
- **Canonical source:** Main:76.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
    C3 (sufficient hidden memory capacity): every visible readout is carried by exactly
```

New:

```text
    C3 (sufficient hidden memory capacity), as a fibre-count slot stating no law or I*: every visible readout is carried by exactly
```

### P-F14-4 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:141`

- **Kind:** wording.
- **Canonical source:** Main:74.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
/-- **C2, structurally.** The visible stream carries a genuine one-bit memory:
```

New:

```text
/-- **C2 slot — a visible-stream consequence, not [Main]'s hidden persistence.** The visible stream carries a genuine one-bit memory:
```

### P-F14-5 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:152`

- **Kind:** wording.
- **Canonical source:** Main:76.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
/-- **C3 — sufficient hidden memory capacity.** For every current visible readout there
```

New:

```text
/-- **C3 slot — a fibre count; no law or `I*` is stated.** For every current visible readout there
```

### P-F14-6 — `verification/lean-mathlib/OIBridge/IndependenceCensus.lean:182`

- **Kind:** wording.
- **Canonical source:** Main:74, Main:76.
- **Preserve:** edge_rigidity_probe.py:1180-1189 canonical C-numbering guard: the docstring before core_capacity_saturates keeps '**C3 ', before core_history_readback keeps '**C4 ', and the file keeps 'C3 (sufficient hidden memory capacity)' and 'C4 (history readback)'; docstring/comment only: no theorem statement, definition or proof changes; #print axioms output unchanged; Lean-manuscript census registry unaffected (no cited identifier changes).
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
C2 (memory
persistence — the visible stream carries structural memory), C3 (sufficient hidden memory
capacity — exactly saturated here)
```

New:

```text
a C2 slot (the visible stream carries structural memory; not [Main]'s hidden
persistence), a C3 slot (a fibre count, exactly saturated here; no law or `I*` is stated)
```

### P-F14-7 — `verification/lean/bohr_frequency_probe.py:4094`

- **Kind:** wording.
- **Canonical source:** Main:74.
- **Preserve:** comment only: no executed statement changes; the probe's checks and printed output are unchanged.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
# C2: the visible stream carries a genuine one-bit memory, v_{t+2} = v_t
```

New:

```text
# C2 slot (a visible-stream consequence, not [Main]'s hidden persistence): v_{t+2} = v_t
```

### P-F14-8 — `verification/lean/bohr_frequency_probe.py:4108`

- **Kind:** wording.
- **Canonical source:** Main:76.
- **Preserve:** comment only: no executed statement changes; the probe's checks and printed output are unchanged.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
# C3 -- sufficient hidden memory capacity: every visible readout is carried by two states,
```

New:

```text
# C3 slot (a fibre count; no law or I* is stated): every visible readout is carried by two states,
```

## F15 — kernel scope of C3 necessity at Main:524

### P-F15-1 — `papers/Main.md:524`

- **Kind:** wording.
- **Canonical source:** Main:626 (kernel stated for bijective realizations; non-injective case on paper).
- **Preserve:** Lean-manuscript census parsing of '(kernel: ...)' citations (identifiers unchanged); §A.35 registry.
- **#1477 ledger:** not on a ledger line.
- **Mirror:** none.

Old:

```text
(kernel: `c3_necessity`, `card_hidden_ge_two_pow_Istar`, `c3_necessity_and_capacity` in `OIBridge/C3Necessity.lean`)
```

New:

```text
(kernel: `c3_necessity`, `card_hidden_ge_two_pow_Istar`, `c3_necessity_and_capacity` in `OIBridge/C3Necessity.lean`, for bijective realizations)
```

## Not packaged

- **ch02:88 / FULL:718 (F9).** Routed to #1477's final scientific review.
- **Main:439's heading,** "The Characterization Theorem: Necessity of the Conditions". It is accurate for the necessity directions §3.4 proves. It is noted at F3 as a plausible source of the overclaimed wording, not as an error.
- **The open scope questions are not decided by any package.**
  - F9: whether the reconstruction itself uses the mixing hypothesis.
  - F10: whether the characterization theorem needs time-homogeneity.
  - In both cases the packages keep the more conditional wording.
- **Confirmed in review (#1529, c.7067421634; P-F3-2).** Structure:734's typicality clause, "random permutations on finite sets typically lack the coupled-dynamics … features", conflicts with Main:153, where bijections failing C1 are an exponentially vanishing fraction as $n_H$ grows. P-F3-2 removes the clause.
- **Noted, not packaged: `verification/lean/bohr_frequency_probe.py:4307–4308`.** This is a printed message string: "C2 is structural (v_{t+2} = v_t, a genuine one-bit memory), C3 is sufficient hidden memory capacity …". It repeats the old Lean labels in the probe's output. Changing it changes the probe's printed output, which may be compared or retained elsewhere, so it is left to the F14 application round to change together with any consumer of that output. The probe's comment labels are packaged as P-F14-7 and P-F14-8.
