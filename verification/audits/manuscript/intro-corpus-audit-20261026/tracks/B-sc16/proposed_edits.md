# SC-16 proposed edit list (corpus at 6bc2c4af10863c2cdfd9f5c1b88abdc8b64f9ed0)

Each entry: site, mirrors, verdict, exact old text (the span to replace), exact new text.
Book chapter edits must land identically in `book/The-Incompleteness-of-Observation-FULL.md`
(mirrors verified byte-identical at the lines listed). Regenerate or flag stale the `.tex/.pdf`
of every touched file (AGENTS §A.25 step 5).

Notation: "C4 => accessible P-indivisibility" is refuted (REPORT.md F1). What C4 does deliver on an
accessible window is positive conditional memory (Main §2.3 readback lemma); P-indivisibility of the
rooted family is delivered across the recurrence cycle (Main §2.3 theorem).

---------------------------------------------------------------------------------------------------
## E1  papers/Complexity.md:418   (no book mirror; companion: papers/Computation.md:144 = E12)
Verdict: asserts that P-indivisible memory (grade iii) is "the framework's specific claim" for
device noise; C1–C4 deliver grade (ii)-or-(iii) only. Unsupported as stated.

OLD:
**A decoder-level test on existing data.** P-indivisibility has a syndrome-level signature. Three grades of temporal structure must be distinguished: (i) non-stationarity (parameter drift — classical and divisible), (ii) classically correlated noise (leakage, cosmic-ray events — non-Markovian but divisible), and (iii) P-indivisible memory, the framework's specific claim, whose fingerprint is information backflow — non-monotonic conditional error-rate relaxation and negative canonical decay rates in the per-round channel reconstructed from syndrome history. The prediction is directional and falsifiable at device level:

NEW:
**A decoder-level test on existing data.** Accessible conditional memory has a syndrome-level signature. Three grades of temporal structure are distinguished: (i) non-stationarity (parameter drift — classical and divisible), (ii) correlated noise that is non-Markovian while its population law stays divisible (leakage, cosmic-ray events), and (iii) P-indivisible noise, whose fingerprint is information backflow in the population law — non-monotonic conditional error-rate relaxation and negative canonical decay rates in the per-round channel reconstructed from syndrome history. Readback (C4) at an accessible order places the noise in grade (ii) or (iii); it does not select grade (iii), since a readback gap is compatible with a population law that is P-divisible on every window short of recurrence [1, §2.3]. Grade (iii) is a further property, testable on the same records by a divisibility witness. The prediction is directional and falsifiable at device level:

(The remainder of the paragraph is unchanged.)

---------------------------------------------------------------------------------------------------
## E2  papers/Complexity.md:461   mirror book/ch15-quantum-engineering.md:112 = FULL:4073
Verdict: labels the long-chain regime "P-indivisible"; C2-slow plus C3 give neither C4 nor
P-indivisibility on accessible windows. Unsupported. (The ch15 and FULL lines are identical to
Complexity apart from `\tau_B / \tau_S` spacing; apply the same text in each file's own spelling.)

OLD (Complexity):
- Long chain ($L \gtrsim 20$, $\tau_B \gg \tau_S$): P-indivisible regime. Information backflow. Correlations from gate $k$ return at gate $k + \tau_B / \tau_S$, partially restoring coherence.
OLD (ch15:112, FULL:4073):
- Long chain ($L \gtrsim 20$, $\tau_B \gg \tau_S$): P-indivisible regime. Information backflow. Correlations from gate $k$ return at gate $k + \tau_B/\tau_S$, partially restoring coherence.

NEW (all three):
- Long chain ($L \gtrsim 20$, $\tau_B \gg \tau_S$): memory-bearing regime when the chain reads back its record (C4). Correlations written at gate $k$ can return at later gates within the retention time of $\tau_B/\tau_S$ gates, partially restoring coherence. P-indivisibility of the qubit's population law on such windows is a further property, certified only by a divisibility witness.

---------------------------------------------------------------------------------------------------
## E3  papers/Complexity.md:462   companion book/ch15-quantum-engineering.md:114 = FULL:4075
Verdict (found in the corpus grep): "once tau_B/tau_S exceeds the C2 threshold the visible law
carries accessible finite-horizon memory" — persistence does not supply C4 (Main :76, :80);
the Complexity version also omits the recurrence-cycle scope that ch15 states.

OLD (Complexity):
- The transition is sharp: once $\tau_B / \tau_S$ exceeds the C2 threshold the visible law carries accessible finite-horizon memory rather than acquiring it gradually, and on a fixed finite reversible representative that memory also appears as stochastic indivisibility of the visible population law [1, §2.3]. Neither is a claim about generic open-system non-Markovianity of a quantum channel.
NEW (Complexity):
- Once $\tau_B / \tau_S$ exceeds the C2 threshold the record survives to readback; where the chain also reads it back (C4), the visible law carries accessible finite-horizon memory. On a fixed finite reversible representative, where recurrence returns the visible map to the identity and a readback gap forces a non-permutation rooted map, that memory also shows up as stochastic indivisibility of the visible population law across the recurrence cycle [1, §2.3]. Neither is a claim about generic open-system non-Markovianity of a quantum channel.

OLD (ch15:114 = FULL:4075, first sentence only):
The transition is sharp: once $\tau_B/\tau_S$ exceeds the C2 threshold the record survives to readback, and the visible law carries accessible finite-horizon memory rather than acquiring it gradually.
NEW:
Once $\tau_B/\tau_S$ exceeds the C2 threshold the record survives to readback; where the chain also reads it back (C4), the visible law carries accessible finite-horizon memory.
(The ch15 sentence on the recurrence-cycle representative is correct as it stands; add "across the recurrence cycle" after "visible population law" for parity with Complexity.)
(The "sharp transition" claim is removed because nothing in the corpus derives a threshold sharpness.)

---------------------------------------------------------------------------------------------------
## E4  papers/Complexity.md:478   (no book mirror)
Verdict: "satisfy C1–C4 ..., so their dynamics is P-indivisible" — the inference C1–C4 =>
P-indivisible is refuted; the C1–C4 identification for these compounds is itself unestablished.

OLD:
**Heavy-fermion materials as natural P-indivisible systems.**
NEW:
**Heavy-fermion materials as candidate memory-bearing systems.**

OLD:
The OI framework provides a structural reframing: the conduction electrons satisfy C1–C4 with the f-electron bath, so their dynamics is P-indivisible. The anomalous transport is a *consequence* of non-Markovian electronic dynamics, not a deviation from normal behavior requiring a special mechanism.
NEW:
The OI framework provides a structural reframing: if the conduction electrons satisfy C1–C4 with the f-electron bath, their dynamics is non-Markovian on accessible windows — the readback gap forces positive conditional memory [1, §2.3] — and the anomalous transport is then a consequence of non-Markovian electronic dynamics rather than a deviation from normal behavior requiring a special mechanism. P-indivisibility of the electronic population law is a further property, not implied by C1–C4 on those windows.

---------------------------------------------------------------------------------------------------
## E5  papers/Complexity.md:503   (no book mirror)
Verdict: "wherever C1–C4 are satisfied, P-indivisibility is mandatory" — refuted (F1).

OLD:
The OI framework provides one: wherever C1–C4 are satisfied, P-indivisibility is mandatory.
NEW:
The OI framework provides one: wherever C1–C4 are satisfied, accessible non-Markovianity is mandatory — the readback gap forces positive conditional mutual information on the accessible window [1, §2.3].

---------------------------------------------------------------------------------------------------
## E6  papers/Explainer.md:294   (no book mirror found)
Verdict: "nontrivially so where the dynamics is P-indivisible by C1–C4" — attributes
P-indivisibility to C1–C4. Unsupported on accessible windows.

OLD:
— nontrivially so where the dynamics is P-indivisible by C1–C4.
NEW:
— nontrivially so where the dynamics is P-indivisible, which on a fixed finite reversible representative holds across its recurrence cycle whenever a rooted visible map is not a permutation.

---------------------------------------------------------------------------------------------------
## E7  papers/Explainer.md:767   (no book mirror found; papers/Explainer.tex:2758 is the derived artifact)
Verdict: three claims contradicted by SM: "select exactly one" (SM :226 fixes the form up to one
coefficient alpha, nearest-neighbour assumed, SM :228 Remark); "center independence is necessary
... proven analytically ... information-screening" (SM :236 says CI does not imply statistical
independence after projection; no information-screening result exists anywhere in the corpus);
"maximum propagation speed" and "uniquely maximizes P-indivisibility" as selectors (SM :240: "do not
hold as selectors"); Unruh as selector (SM :240: a downstream test of the observer-level operator).

OLD (whole paragraph):
**The dynamics is unique.** Among all second-order reversible nearest-neighbor dynamics on a lattice, the requirements of center independence (necessary for emergent QM), spatial isotropy, and linearity select exactly one: the discrete wave equation. This holds for any alphabet size and any dimension. Center independence is necessary because center-dependent rules allow the visible sector to partially predict itself, suppressing the information backflow that produces the quantum phenomenology — an effect proven analytically on the full lattice via an information-screening mechanism. Linearity is selected by three independent criteria: it gives maximum propagation speed, it uniquely maximizes P-indivisibility among linear rules, and it is the only choice for which horizons are in thermal equilibrium (nonlinear dispersion breaks the Unruh effect).
NEW:
**The form of the dynamics is fixed up to one coefficient.** Among second-order reversible nearest-neighbor rules on a cubic lattice, center independence, cubic isotropy and linearity fix the form $x_i(t+1)=\alpha\sum_{j\sim i}x_j(t)-x_i(t-1)$ — the discrete wave equation — for one coefficient $\alpha$, at the substratum-symbolic level or an observer-level linear lift; the nearest-neighbor range is an assumption beyond bounded coupling degree. Linearity rests on the amplitude-scale-gauge lemma: with no access to an absolute amplitude scale, base-point-independent first differences force an affine rule, which the center-free branch reduces to a linear one. Center independence is a condition on the microscopic update; it does not by itself make successive visible variables statistically independent once the hidden sector is traced out, and whether it descends to a zero observer-level self-weight is an open coarse-graining condition. The normalization $\alpha=1/d$ is where the real harmonic lift is stable and its leading symbol isotropic. The map from the finite bijection to that observer-level operator is not derived, so Lorentz invariance and the Unruh property are tests of the observer-level operator, not selectors of the substratum rule [SM §4.1–§4.3].

---------------------------------------------------------------------------------------------------
## E8  book/ch15-quantum-engineering.md:112 = FULL:4073   — see E2.

---------------------------------------------------------------------------------------------------
## E9  book/ch17-bioinformatics.md:178 = FULL:4757   (status row: book/appendix-a-prediction-status.md:151 = FULL:5688, B7)
Verdict: premise "P-indivisibility" is attributed to C1–C4 ("because C1–C4 are universally
satisfied"); C1–C4 give accessible conditional memory, not P-indivisibility. The step from memory
to rate autocorrelation is a modeling interpretation; "universally satisfied" is not established.

OLD:
**Universal rate autocorrelation.** P-indivisibility implies that the substitution rate along a single lineage is temporally autocorrelated — the rate at one time correlates with the rate at neighboring times, because both are modulated by the slowly evolving hidden sector (the conformational landscape, the epigenome). The correlation should decay on the timescale $\tau_B$ of the hidden sector, and should be detectable across all taxa because C1–C4 are universally satisfied.
NEW:
**Universal rate autocorrelation.** History readback (C4) makes the substitution process along a single lineage memory-bearing: the slowly evolving hidden sector (the conformational landscape, the epigenome) carries information about the lineage's past into its future rates, so the rate at one time is expected to correlate with the rate at neighboring times. The correlation should decay on the timescale $\tau_B$ of the hidden sector, and should be detectable in every taxon in which C1–C4 are realized.
Propagation flag: B7 is classified S (strictly parameter-free structural); its chain now contains a
modeling step (memory => rate autocorrelation) and an unestablished universality premise. Re-audit
the B7 classification (appendix-a:151 and FULL:5688) under Steps 1–3.

---------------------------------------------------------------------------------------------------
## E10 book/ch01-observation.md:121 = FULL:465
Verdict: "The framework requires P-indivisibility on accessible timescales ... The
accessible-timescale lemma supplies this." Refuted: the lemma supplies conditional memory.

OLD:
The framework requires P-indivisibility on *accessible* timescales — times short compared to $\tau_B$, the hidden sector's intrinsic memory time — not at recurrence. The accessible-timescale lemma supplies this.
NEW:
What an observer can measure is memory on *accessible* timescales — times short compared to $\tau_B$, the hidden sector's intrinsic memory time — not at recurrence. The accessible-timescale lemma supplies that memory, as conditional mutual information, wherever the stored record is read back (C4). It does not supply P-indivisibility on those windows: a readback gap is compatible with a population law that is divisible on every window short of recurrence ([Main §2.3]).

## E11 book/ch01-observation.md:127–129 = FULL:471–473
Verdict: (a) the lower bound is stated from storage alone; Main §2.3 (:155, :172) shows storage
without readback gives zero conditional memory; (b) "distinguishability has rebounded by an amount
of order I_0 at every step" equates conditional memory with one-time distinguishability revival;
refuted by the XOR model (1 bit of memory, no revival).

OLD (:127):
Quantitatively, the non-Markovian mutual information between the visible sector's past and future, conditioned on its present, is bounded below by
NEW (:127):
Quantitatively, when the stored record is read back (C4), the non-Markovian mutual information between the visible sector's past and future, conditioned on its present, is bounded below by

OLD (:129):
which is order $I_0$ for any $k \tau_S \ll \tau_B$. The information backflow that the proof established at recurrence times is therefore present continuously throughout the accessible-timescale regime: the visible sector's distinguishability has rebounded by an amount of order $I_0$ at every step until enough cycles have accumulated to deplete the stored memory.
NEW (:129):
which is order $I_0$ for any $k \tau_S \ll \tau_B$. Conditional memory of order $I_0$ is therefore present throughout the accessible-timescale regime, until enough cycles have accumulated to deplete the stored record. It is memory in the multi-time law, distinct from the distinguishability revival that the recurrence proof establishes for the one-time population law, and it does not imply that revival.

## E12 book/ch01-observation.md:133 = FULL:477
Verdict: "the accessible-timescale lemma establishes that the same property [P-indivisibility]
holds in the parameter regime that matters for actual observers" — refuted.

OLD:
The recurrence-based proof of the theorem establishes the existence of P-indivisibility; the accessible-timescale lemma establishes that the same property holds in the parameter regime that matters for actual observers in our universe.
NEW:
The recurrence-based proof establishes P-indivisibility across the recurrence cycle; the accessible-timescale lemma establishes conditional memory in the parameter regime that matters for actual observers in our universe. The second does not imply the first on accessible windows.

---------------------------------------------------------------------------------------------------
## E13 book/appendix-b-derivations.md:420 = FULL:6187
Verdict: "C2/C3 promote P-indivisibility from a formal property to an observationally dominant
one" — unsupported; also attributes observable-timescale "backflow" to C2 and C3.

OLD:
Conditions C2 (memory persistence) and C3 (sufficient capacity) are what make the information backflow occur on *observable* timescales $k\tau_S \ll \tau_B$ rather than only at recurrence — with C4 (history readback) the load-bearing condition for the memory witness itself (`review4_probes.py`); this is the content of Lemma B.7.4 and Chapter 1 §1.7. This division of labor follows [Main]: the recurrence argument uses C1 and finiteness alone, while C2/C3 promote P-indivisibility from a formal property to an observationally dominant one. $\square$
NEW:
On *observable* timescales $k\tau_S \ll \tau_B$ the relevant property is conditional memory: C4 (history readback) is the load-bearing condition for it (`review4_probes.py`), with C2 (memory persistence) keeping the record alive to readback and C3 (sufficient capacity) giving it room; this is the content of Lemma B.7.4 and Chapter 1 §1.7. This division of labor follows [Main]: the recurrence argument uses C1 and finiteness alone and delivers P-indivisibility across the recurrence cycle, while readback delivers conditional memory on observable timescales, which does not by itself make the population law P-indivisible on those windows. $\square$

## E14 book/appendix-b-derivations.md:92 = FULL:5859
Verdict: "(under C1–C4)" misattributes the hypothesis of the P-indivisibility it consumes.
OLD:
*The P-indivisibility of the substratum dynamics (under C1–C4) implies CP-indivisibility of $\{\Phi_t\}$:
NEW:
*The P-indivisibility of the substratum dynamics across its recurrence cycle (from C1 and finiteness) implies CP-indivisibility of $\{\Phi_t\}$:
(The theorem's own scope — diagonal-preserving realizations, glossary :119 — is a separate question, not audited here.)

## E15 book/ch18-beyond.md:72 = FULL:4890
OLD:
— the memory effects that produce P-indivisibility are washed out.
NEW:
— the accessible memory effects are washed out.

## E16 book/ch15-quantum-engineering.md:83 = FULL:4044
OLD:
The framework's prediction of P-indivisible noise in superconducting qubits
NEW:
The framework's prediction of memory-bearing (accessibly non-Markovian) noise in superconducting qubits

## E17 papers/Computation.md:144 (companion of E1)
OLD:
The same partition machinery predicts P-indivisible device noise at the engineered-bath level ([Complexity §8.2]); its syndrome-level signature — an exploitable temporal kernel in detection-event time series, distinguishable from classical drift by divisibility tests — is testable on already-public fault-tolerance datasets, and the sharpened prediction is stated there.
NEW:
The same partition machinery predicts memory-bearing device noise at the engineered-bath level ([Complexity §8.2]); its syndrome-level signature — an exploitable temporal kernel in detection-event time series, retained after conditioning on drift — is testable on already-public fault-tolerance datasets, with P-indivisibility of the reconstructed per-round channel a further property that a divisibility test certifies. The sharpened prediction is stated there.

## E18 papers/Explainer.md:892
Verdict: "the accessible-timescale backflow lemma (Main, §2.3) establishes P-indivisibility without
recurrence" — refuted.
OLD:
because the accessible-timescale backflow lemma (Main, §2.3) establishes P-indivisibility without recurrence, and
NEW:
because the accessible-timescale readback lemma (Main, §2.3) establishes conditional memory without recurrence (P-indivisibility, which the recurrence theorem supplies, uses the finiteness of the whole state space), and

## E19 papers/Explainer.md:581
OLD:
and persistent through P-indivisibility (condition C2).
NEW:
and persistent (condition C2).

## E20 papers/Explainer.md:619
OLD:
the trace-out produces the reduced law — P-indivisible in the memory-bearing sector the conditions characterize — and
NEW:
the trace-out produces the reduced law — memory-bearing in the sector the conditions characterize — and

## E21 papers/SM.md:306   (and :236)
Verdict: borderline; "C4/readback theorem supplies the memory/P-indivisibility content" can be read
as crediting P-indivisibility to C4.
OLD (:306):
Main's C4/readback theorem supplies the memory/P-indivisibility content independently.
NEW (:306):
Main's readback lemma supplies the memory content, and its recurrence-cycle theorem the P-indivisibility content, independently of center independence.
OLD (:236):
Main's C4/readback and finite-recurrence theorems establish the memory/P-indivisibility content without that inference.
NEW (:236):
Main's readback lemma establishes the memory content, and its finite-recurrence theorem the recurrence-cycle P-indivisibility content, without that inference.

## E22 papers/Explainer.md:352 (and heading :346; table rows :1009, :1018–:1020 use the same §3.3 numbering)
Verdict: the direction stated (accessible P-indivisibility => C4) is true but needs a full-support
visible prior; the cited section is Main §3.4, not §3.3 (Main §3.3 is Bell).
OLD (:346):
## The Characterization Theorem (§3.3)
NEW:
## The Characterization Theorem (§3.4)
OLD (:352):
- Section 3.3 proves: accessible-window P-indivisibility ⟹ C1, C3, C4 (necessity, unconditional); C2's slow form within the mixing class (the conditional physical-memory theorem)
NEW:
- Sections 2.3 and 3.4 prove: accessible-window P-indivisibility under a full-support visible prior ⟹ accessible non-Markovianity ⟹ C1, C3, C4 (necessity); C2's slow form within the mixing class (the conditional physical-memory theorem)
(Check whether "Section 3.3" elsewhere in the Explainer means Main §3.4 before changing.)

## E23 papers/Main.md:153 and the lemma title at :167 (terminology; see REPORT F6)
OLD (:153):
The recurrence argument establishes P-indivisibility in principle. The following lemma shows that under (C2), information backflow occurs on observable timescales — not merely at Poincaré recurrence times.
NEW (:153):
The recurrence argument establishes P-indivisibility across the recurrence cycle. The readback lemma below shows that a readback gap at an accessible order produces conditional memory on observable timescales; that is a property of the multi-time law and does not make the population law P-indivisible on those windows (Scope, above).
OLD (:167):
**Lemma (accessible backflow from readback).**
NEW:
**Lemma (accessible conditional memory from readback).**
(If adopted, rename every citation of "accessible-timescale backflow lemma" — Main :716, Complexity :474, Explainer :892, book ch01 §1.7 — and reserve "information backflow" for the trace-distance sense used at Main :121 and :149.)
