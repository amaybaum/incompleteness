# Scientific re-check: Introduction draft, revision 2

- **Object:** `S/paper/draft/Introduction-r2.md`, sha256 `98d35eec5d4e…74fe`. It is byte-identical to
  `draft/Introduction-r2.md` on #918 at `59eb0d26`.
- **Also read:** `DRAFT-NOTES-r2.md`, `CHANGES-r2.md` and `ERRATUM-r4.md`. The erratum is
  byte-identical to `design/ERRATUM-r4.md` at `59eb0d26`.
- **Sources:** as for `REVIEW.md`, Main tree at `687e885b`.
- **Read-only.** No repository file was changed and nothing was committed. Git ran with
  `-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: BLOCK (narrow)

The draft is acceptable once the four replacements R2-1 to R2-4 below are applied. Two of them
apply AGENTS' claim/evidence-boundary blocker rule:
- **§6.4(5)** turns the framework's *adopted* Bell branch into a *necessity*, by compression. This
  is a new overclaim.
- **§6.3** now draws its "So" from a premise that was cut. That is my fault: my M3 replacement text
  produced it.

Everything else is applied correctly, and the remaining items are nits. The erratum's corrected
wording is exact, apart from two citation nits.

***

## 1. The scientific review's items, as applied

| Item | Result |
|---|---|
| RC-1 | Applied verbatim (l.160). Correct |
| RC-2 | Correctly applied (l.164–166). The text covers the uniform diagonal burn card under the [Main §3.2] embedding; the constant channel $\operatorname{tr}(\rho)I/2$, which is entanglement-breaking; the two-step identity; CP-indivisibility (Main:326); the [BBS24] definition; no decomposition for the initialized slot (Main:702, §4.5); and the Pauli instrument for the uniform card. "Record which Pauli…" is gone. D1 is left as an OWNER marker. [BBS24] is entered with a VERIFY on content, which is right |
| RC-3 | Applied verbatim (l.194), with C6(c). [PSW] is deleted and appears nowhere |
| RC-4 | All required sites are present: §5.1 (ch07:110, ch18:146, ch18:158, ch07:159–161, ch18:130), §5.2 (ch07:126 s1, GR:869, ch18:146, ch19:334), the abstract, §6.5 item 4, the conclusion, §5.4 (GR:811) and §5.3 (R12). The §5.1 marker's restatement list ("§6.5 item 4, §7, abstract") is correct for the renumbered paper. One nit: the §6.5 item-4 marker names "§5.4's decoupling sentence", which item 4 no longer restates |
| RC-5 | Applied verbatim (l.230). There is no "exactly when" left. Appendix A marks `rooted_eq_iff_slice_eq` as "(forward direction)". §A.34 is met |
| RC-6 | The abstract sentence is inserted and ends at "as one theorem". §1.2 "Contributions" cites [EGGH26; Bar23; Bar25; Bar26; SGD19]. "Machine-checked" there sits under the decision-2 / §A.42 marker (l.38). Acceptable |
| RC-7 | The six items cover CONTRIBUTION-r4 (c) 1–6 and 13. The card item carries the corrected wording, item 2 says "(iii)–(v) open", and item 4 says the reviews are internal. The decoupling non-claim now lives only in §5.4, which is acceptable because that is declarative text there |
| M1 | Applied: the non-disturbance step rests on the indicator Born weights (l.70). Cutting the `isDiag_Phi` sentence loses nothing load-bearing |
| M2 | Applied (l.32). See nit N4 |
| M3 | Applied as I wrote it, and **my text was defective**. See R2-2 |
| M4 | Applied (l.72, "coincides with" [Bar26, Thm 3.3] and [Sch21, Thm 2]) |
| M5 | Applied (l.176, l.208, §6.5 item 4) |
| M6 | Moot: the paragraph is cut |
| Bibliography | All fixes applied. I checked that every key cited in the body is defined and every defined key is cited, by script: none is missing and none is orphaned. [Sha79] is bibliographically correct on Crossref (*Commun. ACM* 22(11), 612–613, 1979), but see N7 |

## 2. Required replacements

### R2-1 — §6.4 item (5): adopted branch stated as a necessity (l.240) [new overclaim]

The draft says "… is Bell-local, $|S_{\mathrm{CHSH}}|\le2$ …, so quantum Bell correlations require
ontic parameter dependence".

Bell-locality of a completion with pointwise cones *and* a setting-independent ensemble means a
violating completion must give up **one** of the two. Main:82 and Main:396 record measurement
dependence as the alternative, "recorded, not adopted". The framework *chooses* to keep
measurement independence. r1 had this right ("the framework's adopted branch …"). The editorial
nit that removed "adopted branch" turned a choice into a theorem.

Replace from "so quantum Bell correlations require ontic parameter dependence" through the end of
item (5) with:
> so a deterministic completion reproducing quantum Bell correlations must give up one of the two; the framework keeps measurement independence and adopts ontic parameter dependence, in which one wing's microstate response depends on the remote setting without operational signalling, and the compatibility of that choice with operational no-signalling and the gravitational continuum limit of the lattice is the open hypothesis H-Bell [Main §3.3].

The H-Bell gloss follows Main:22 and Main:394, which name both no-signalling and the
metric/Ollivier–Ricci continuum condition.

### R2-2 — §6.3: the obstruction's "So" lost its premise (l.234–236)

Main:538 has two halves:
- the factorization half, $B=\Xi M$ through $N$ states, proved;
- the unboundedness half, nonnegative rank growing without bound over finite qubit experiments,
  **imported**.

r2 keeps the first half, cuts the HKLP sentence, and then infers "So no fixed finite realization
reproduces …". The unboundedness now appears only afterwards, as a separate sentence about
GH/Montina. My M3 text had the same order, and this is the correction.

Replace both paragraphs of §6.3 with:
> A fixed finite realization with $N$ ontic configurations generates only behaviour matrices that factor nonnegatively through $N$ states. Simulating a qubit's prepare-and-measure statistics needs classical memory unbounded over finite experiments: explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08], and Montina reports Hardy's result that the number of ontic states cannot be finite [Mon08; Har04]. So no fixed finite realization reproduces the full prepare-and-measure theory of a qubit exactly; the factorization is proved, and the unboundedness is imported [Main §3.4, Proposition (finite-substratum operational obstruction — classical-dimension form)]. The obstruction does not touch Theorem 1, whose realization is chosen per law.

Main's own import is Heinosaari et al. [55]. If the owner prefers that route, under D3, restore
[HKLP] in place of the GH/Mon sentence, with its content-VERIFY.

### R2-3 — §5.4 decoupling: a scope limit was dropped (l.208)

BH-01 item F lists three things it does not show. r2 keeps two and drops "that Theorem A.7 is
false within its stated scope $t\ll\tau_B^D$". Without that limit the paragraph can be read as
impugning GR Thm A.7 itself.

Replace the last sentence with:
> They do not show that information reaches $D$, that [GR, Thm A.7] fails within its stated scope $t\ll\tau_B^D$, or that no other decoupling argument exists.

### R2-4 — Status words for two steps not given as written proofs (l.94, l.276)

- **The time-$t$ identification.** Main:99 and Main:580(2) say the reading of a realization's
  time-$t$ law as the joint law is "a step not formalized". Main gives no written proof of it.
- **The CMI vanishing criterion.** Main:99 calls it "the standard vanishing criterion … not
  formalized". It is a textbook fact, not a proof in the corpus.

Under the paper's own convention ("proved on paper means a written proof without a machine
check", l.36), labelling them "proved on paper" asserts a status the sources do not give.

At l.94, replace "Their identification with a realization's time-$t$ law is proved on paper." with:
> Their identification with a realization's time-$t$ law is not machine-checked.

At l.276, replace "the time-$t$ identification and the CMI vanishing criterion are proved on paper." with:
> the time-$t$ identification and the standard vanishing criterion for conditional mutual information [CT06] are not machine-checked.

The Corollary's own label, "proved on paper" (l.96), is right: its directions are written out.

***

## 3. Checks the coordinator asked for

### 3.1 Cuts and compression

I checked every compressed paragraph against `REVIEW.md` and Main. No proved, hypothesis or open
distinction was lost, apart from R2-1 to R2-4. In detail:

- **Abstract.** The abstract keeps:
  - the hypothesis framing;
  - the coincidence of the classes, with the components attributed;
  - Markov inclusion and the unselected Born exponent;
  - "one step proved on paper only";
  - the operational layer "characterized exactly by five conditions, none implied by OI alone";
  - the three open items;
  - the black-hole sentence, which is marked.

  The parenthetical "(one step proved on paper only)" is attached only to the recurrence clause.
  The memory clause rests on the same kind of step (R2-4), so the contrast slightly overstates the
  memory clause (nit N1).
- **§2.2–§2.4.** Theorem 1, the inclusions, the independent-prior status, Theorem 2's scope and the
  Corollary's two directions are intact. The capacity bound is machine-checked and the readback
  bound is on paper with exact probes; both are correct. The per-horizon characterization was cut,
  and the conditions paragraph still states the diagnostic reading at Main:596's strength.
- **§3.1.** Theorem 3 is stated with "P-divisible on $\{0,\dots,n\}$", which matches
  `PIndivisibleWithin n`. One sentence misdescribes the kernel route (N2).
- **§5.** The access paragraph is complete at package strength: counts, sufficiency,
  $P_{\rm succ}\ge1/|\mathcal U|$, $|\mathcal U|\ge|\mathcal M|$, the 32 violators, and "sufficient,
  not necessary". The decoupling interval statement is accurate: the bounds hold over
  $\Gamma\in[1/100,1000]$ and $\tau_B^D\in[10^{16},10^{19}]$ s (BH-01 REPORT:218–235). Dropping
  "robustness" and the second sensitivity value loses no status distinction.
- **§6.1–§6.2.** Theorem 4 and its directional witnesses (§A.34), the qubit independence, "OI alone
  does not imply QM" and the open question of (iii)–(v) are intact. RC-5 is verbatim.
- **§6.4.** R2-1 is the only problem. Item (1) should also name §2.2's prior-independence step
  (N5).

### 3.2 The notation $\mathsf S_K=\mathsf D_K=\mathsf Q_K$

The notation is **faithful**. `finite_horizon_equivalence` proves, for each $P$ on
`Traj V K`, `Stochastic P ↔ RevRealizable P`, `RevRealizable P ↔ QfbRealizable P` and
`QfbRealizable P ↔ Stochastic P`. That is exactly equality of the three sets of laws at fixed
alphabet and horizon.

The definitions at l.54–56 match the kernel structures:
- `RevReal`: a correlated `init` on $V\times\mathrm{Hid}$, with finite `Hid`;
- `QfbReal`: a unitary `U`, diagonal `init` weights, every-step collapse, and a `read` function.

Main's $S\iff D\iff Q_{\mathrm{fb}}$ is noted at l.64. The alphabet dependence is suppressed in
the subscript but quantified in the theorem statement, which is acceptable.

The difference from Main is notational only, and it is correctly an owner item.

### 3.3 Inline attributions after §7's removal

Every attribution AUDIT r4 requires **for a statement the paper still makes** is at the point of
use:

| Topic | Citations |
|---|---|
| Realization | EGGH26 Props. 13 and 16; LP17 Prop. 1.5 |
| Permutation unitary and unistochastic processes | Bar25 p. 12; Bar23 §4.3; Bar26 §4 |
| Born exponent | Bar26 Thm 3.1 |
| One-step dilation | Bar26 Thm 3.3; Sch21 |
| Born rule for records | SGD19 Eq. (3), with Milz20 contrasted |
| Pinsker and DPI | CT06 |
| Divisibility | RHP14 Thm 2.4; BD16 Prop. 1 |
| Concurrent work | Dou26 Prop. 1 and App. A |
| Stochastic inverse | BB18 Problem 23 |
| XOR family | RHP14 Eq. (15) |
| Backflow witnesses | BLP09; BJA17 |
| Finite carriers | GH03; Mon08 (Har04 as reported) |
| Black holes | Pag93, Pag05 and Pag13; Pen20; Haw76 |

What is dropped:
- RHP10 (Main [4]), which was cited only in r1's related work, where no statement depends on it.
  That is fine.
- Calvo, which remains owner item D2. I recommend it more strongly now: with §7 gone, the paper
  never positions itself against the one source that claims a derivation of the textbook axioms
  (AUDIT §7, F14).

No novelty or priority sentence remains. The comb sentence is gone, and the paper makes no
packaging claim.

### 3.4 The erratum's corrected wording

**Site identification.** All four sites are correctly identified, at
`design/OUTLINE-r4.md:226`, `design/SOURCES-r4.md:135`, `design/review/RECHECK-r4.md:19` and
`design/CONTRIBUTION-r4.md:182–185`, all at `59eb0d26`.

**Hashes.** The cited probe hashes match my files:
- `card_exact.py`: `fabb115b…c642`;
- `card_exact.out`: `ad598e3c…dc1e`.

**The corrected texts are exact:**
- OUTLINE and SOURCES: uniform burn card decomposable via the Pauli instrument and
  $\mathrm{Ad}_{\sigma_o}$; initialized slot not decomposable (Main:702).
- CONTRIBUTION 13: classical on card inputs; one-step entanglement-breaking; CP-indivisible
  (Main:326) but decomposable; no Bell violation.
- RECHECK-r4: the clause is read as applying to the initialized slot only, and the row's other
  entries stand.
- The "both cases CP-indivisible" line is right: both $\Phi_1$ are constant, so
  $\Lambda\circ\Phi_1$ has rank 1.

**Nits on the erratum:**
- **E1.** For SOURCES-r4:135 the text being replaced is "and the realization has no
  classical-memory decomposition", not the OUTLINE phrase. Quote that string for SOURCES.
- **E2.** CONTRIBUTION 13's corrected text drops the citations it had: Main:286 for
  entanglement-breaking and ch01:286 for Bell. Restore them after the respective clauses.
- **E3.** "J(Φ₁) has rank 2, so every outcome-conditioned processing is measure-and-prepare"
  states the wrong reason: the rank alone does not imply it. The reason is the range. Write: "J(Φ₁)
  has rank 2 with range $|0\rangle\otimes\mathbb C^2$, so every CP map below Φ₁ is
  $|0\rangle\langle0|\operatorname{tr}(E\,\cdot)$, and every outcome-conditioned processing is
  measure-and-prepare".
- **E4 (§A.42).** The erratum cites scratch files as its check. Its claim is self-contained: the
  Pauli-twirl identity $\sum_o\sigma_o X\sigma_o=2\operatorname{tr}(X)I$ settles it by hand. Say
  that, and label the scratch probe as provenance. If the erratum lands on `main`, the probe and its
  output need to be retained beside it, or the citation dropped.

## 4. Nits (r2)

- **N1.** Abstract: "(one step proved on paper only)" → "(each with one step not machine-checked)".
  Alternatively, attach the parenthetical to both memory clauses.
- **N2.** l.116: "Steps (2)–(3) are machine-checked from a routed-readback form of (C4)". The
  kernel does not follow steps (2)–(3), which are the inverse-lemma route.
  `routed_forces_indivisible_somewhere` derives the conclusion from routed readback by the
  overlap-and-return route of Theorem 3. Write:
  > The conclusion is machine-checked from a routed-readback form of (C4), by the route of Theorem 3; the step from history-level (C4) to that form is proved on paper.
- **N3.** l.222 "for every finite carrier" → "for every nonempty finite carrier" (`[Nonempty A]`).
- **N4.** l.32: "At the level of finite-horizon observable laws the correspondence is exact and
  universal (§2)". "The correspondence" now reads as Barandes's, from the previous sentence. Write
  "the correspondence of §2 (Theorem 1)".
- **N5.** §6.4 (1): "the steps proved on paper in §2.2, §2.4 and §3.1". §2.2's prior independence
  is one of those steps.
- **N6.** The §6.5 item-4 marker mentions "§5.4's decoupling sentence", which item 4 no longer
  restates. Drop that phrase from the marker.
- **N7.** [Sha79] is correct bibliographically, but the BH-01 package names "the linear
  secret-sharing threshold" without a source, and Shamir's content is cited from memory. Either keep
  a content-VERIFY, or cite only [BHa].
