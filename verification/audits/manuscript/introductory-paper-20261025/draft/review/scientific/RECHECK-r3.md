# Scientific re-check: Introduction draft, revision 3

- **Object.** `draft/Introduction-r3.md` at `270728cb` on #918, sha256 `83313e2c…6a68`, which is
  byte-identical to `S/paper/draft/Introduction-r3.md`.
- **Also read.** `draft/CHANGES-r3.md` and the updated `design/ERRATUM-r4.md`, which is identical
  to the scratch copy.
- **Sources.** The same as before, with Main at `687e885b`. I also read
  `verification/programmes/physical-realization/round-c4-1-physical-discharge/result.md` and the
  kernel module `PhysicalC4Discharge.lean`.
- **Read-only.** I changed no repository file. Git ran with `-c gc.auto=0 -c maintenance.auto=false`.
- **Scope of the r3 commit.** The diff `29e078a0..270728cb` touches only the audit directory. No
  book or GR file was edited, which is what the owner decision requires.

## Verdict: ACCEPT WITH NITS

R2-1 to R2-4 are applied verbatim, and §6.3 now has the right order and premises. The drafter's
two departures from my nits are correct, and N2's departure fixes an error in my own suggestion.
The owner decisions are applied without changing any claim. The erratum is exact.

The nits below are small. Two of them (T1 and T2) should be applied before landing.

***

## 1. R2-1 to R2-4

| Item | Result |
|---|---|
| R2-1 (§6.4(5), l.234) | Verbatim. The text now reads "must give up one of the two; the framework keeps measurement independence and adopts ontic parameter dependence". The overclaim is gone. The "lattice" wording is addressed in T1 |
| R2-2 (§6.3, l.230) | Verbatim, in the right order. The factorization comes first, then the unboundedness with its sources [GH03; Mon08] and Hardy as reported, then "So …", then "the factorization is proved, and the unboundedness is imported". This now matches Main:538's two-part structure |
| R2-3 (§5.4, l.204) | Verbatim. All three limits of BH-01 item F are present |
| R2-4 (l.92, l.275) | Verbatim at both sites. The Corollary keeps "(proved on paper)", which is correct |

## 2. The drafter's departure from N2: correct

My N2 text said: "the step from history-level (C4) to that form is proved on paper". That asserts
history-level (C4) ⇒ routed readback. The sources say the opposite.

- **C4-1 `result.md`:129–136.** The discovery round's T1 "says routed implies history-level".
- **C4-1 `result.md`:211–218, RD3.** On the tape-ledger carrier there is "history-level memory
  within the window — and **no routed readback within the window `K = 3`**". The record calls this
  "the converse's failure on one carrier".

So no written step from history-level (C4) to routed readback exists, and my wording would have
asserted one.

**r3's wording is correct.** It reads: "The conclusion is machine-checked, by the route of
Theorem 3, from a routed-readback form of (C4) …; from history-level (C4) it is proved on paper."
- The machine-checked route is `routed_forces_indivisible_somewhere`. It goes through
  `routedReadback_overlap`, then a periodic return, then `horizon_verdict`, which is Theorem 3's
  route.
- The history-level conclusion is Main:139's written proof, by the inverse-lemma route. That route
  is steps (1)–(3) in l.114.

Appendix A (l.278) is aligned: "for routed readback; on paper for (C4)". This is accepted.

**The gloss of routed readback** is "a visible-history record written into the hidden state is
read back later [Main §1.3]". It is faithful to `RoutedReadback`, which has write, store, causal
read and rooted reappearance clauses, and whose recorded item is the root $x_0$. Main never uses
the word "routed", though. The cited text is the realization clause of (C4) in §1.3, "a causal
read-write cycle". See nit N1.

## 3. The departure from N5: correct

l.234 reads "machine checks of the steps of §2.2, §2.4 and §3.1 that lack one". Since R2-4, the
time-$t$ identification and the CMI vanishing criterion are "not machine-checked" and are not
claimed as proved on paper. "The steps that lack one" therefore covers them without mislabelling
them. My N5 phrase, "proved on paper", would have mislabelled them. Accepted.

## 4. The Calvo sentence and [Cal26]

I checked the sentence against the arXiv API record for arXiv:2601.18720v2, by Sami Calvo, titled
"On the Stochastic-Quantum Correspondence" and updated 2026-07-30. The abstract says: "we prove the
six axioms of textbook quantum mechanics from a single axiom: every physical system evolves
according to a, generally indivisible, stochastic law".

**l.72 is accurate**, and it is at the right strength.
- "Calvo states a proof of …" attributes the claim to Calvo and does not endorse it.
- "Theorem 1 is a correspondence between classes of law and derives no such axioms" is exactly
  AUDIT r4's required positioning (§3 (e) and §7, F14). It does not describe Calvo as a
  dimension extension.

**The VERIFY marker is over-conservative.** AUDIT r4 C4 records Calvo v1 and v2 as **[FT]** from
the literature study (LC §3), with the claim located at Thm 1, p. 4. See nit N2.

## 5. "The lattice" in R2-1: replace (T1)

This paper never introduces a lattice, and its "substratum" is defined only as the finite
reversible system $(S,\varphi)$.

H-Bell, per Main:22 and Main:394, concerns two things:
- whether preparation-indexed Bell adjacency in the state-dependent cubic coupling graph preserves
  operational no-signalling;
- whether it preserves the metric and Ollivier–Ricci continuum limit that the gravitational
  reconstruction needs.

The object is the substratum's spatial coupling graph. Main:22 says: "the coupling graph defined
by one-step dynamical dependence".

Replace "and the gravitational continuum limit of the lattice" with:
> and the gravitational continuum limit of the substratum's spatial coupling graph

## 6. The Contributions paragraph (l.32): no overclaim

- "Claims no new theorem or physical result; its contribution is expository" is consistent with
  AUDIT r4. No class above REFRAMING or PARTLY KNOWN is claimed, and nothing is presented as
  novel.
- Each listed item is presentation or synthesis. The component attributions are correct:
  - EGGH26, Bar23, Bar25, Bar26 and SGD19 for Theorem 1;
  - the DPI and Pinsker inequalities for §2.4;
  - RHP14 and BD16 for §3, with Dou26 as concurrent work;
  - [GR] and [Main] for §6.1–§6.2.
- "Machine-checked theorem" became "one theorem", which removes the decision-2 dependency from
  this paragraph.
- **§4.3's Pauli decomposition** is the paper's only statement not found in the corpus. It is a
  one-line consequence of the Pauli-twirl identity, used to illustrate, and it is not presented
  as a theorem. So "claims no new theorem" stands.
- **"Established mathematical results of OI"** must read as covering §5's results only within
  "the scope stated in §5". The [BHa] and [BHb] packages are internally reviewed research records
  that the owner has not adopted. With the review-status clause removed from §6.5 item 4, the paper
  no longer says this anywhere. See T2.

## 7. The erratum

- **E1.** Applied. The SOURCES-r4 string is quoted exactly ("and the realization has no
  classical-memory decomposition") and has its own replacement (l.49–51).
- **E2.** Applied. Main:286 and ch01:286 are restored in non-claim 13 (l.55).
- **E3.** Applied, and correct: "$J(\Phi_1)$ … has rank 2 with range $|0\rangle\otimes\mathbb C^2$.
  So every CP map below $\Phi_1$ is $|0\rangle\langle0|\operatorname{tr}(E\,\cdot)$ for some
  $0\le E\le I$".
- **"(output factor first)"** is correct. My probe's convention is
  $J(E)=\sum_{ij}E(|i\rangle\langle j|)\otimes|i\rangle\langle j|$, so the output factor is first.
  It gives $J(\Phi_1)=|0\rangle\langle0|\otimes I$, whose range is $|0\rangle\otimes\mathbb C^2$ as
  stated. With the input factor first, the range would read $\mathbb C^2\otimes|0\rangle$, so the
  qualifier is needed.
- **E4.** Applied. The claim now rests on the Pauli-twirl identity
  $\sum_o\sigma_oX\sigma_o=2\operatorname{tr}(X)I$, which is correct for every $2\times2$ $X$.
  The decomposition step $\sum_o\tfrac14\sigma_o^2\rho\,\sigma_o^2=\rho$ is correct. The probe is
  labelled provenance and is retained at `draft/review/scientific/probe/`. Its sha256 values match:
  `card_exact.py` is `fabb115b…c642` and `card_exact.out` is `ad598e3c…dc1e`.
- **The rest.** The CP-indivisibility argument for both cases is unchanged and correct.

## 8. Other changes in r3

The following were all checked and are correct:
- **The title**, as the owner chose it.
- **The abstract.** "(each with one step not machine-checked)" now covers both memory clauses.
  "characterized by" still names an iff, given Theorem 4.
- **§1.2.** "The correspondence of §2 (Theorem 1)".
- **§3.1 definitions.** "Rooted (rows indexed by $x_0$)" matches `rootedMap`. The forward-order
  sketch uses $\Gamma_L$ and $\Gamma_n$ consistently.
- **The BJA17 gloss.** "On a $d$-dimensional system" matches Main:332, "bijective (invertible)
  dynamical maps on $\mathbb C^d$".
- **The coherent-lift gloss.** It reads "unitary dilations that reproduce the visible law at every
  time and compose exactly across times", which matches Main:624.
- **The $S_{\rm Page}$ gloss.** "Page's average for factor dimensions" [Pag93] is consistent with
  BH-02, which compares C6(c) against the exact Page average.
- **Theorem 4.** "Nonempty" is in place.
- **The §5.1 compression.** "The endpoint guarantees above are sufficient, not necessary" matches
  BH-01 REPORT:24.
- **The §6.2 identifiers.** With the `File:line` references moved to Appendix A, the identifiers
  and "forward direction" still sit beside the claims, so §A.34 is unaffected.
- **Appendix A line numbers.** These are unchanged from r2, which I verified against the kernel.
  The drafter's direct resolution found 0 mismatches.
- **Owner D1–D3.** D1 adds no sentence and drops its marker; §4.3 keeps CP-indivisibility at
  Main:326. D2 is the Calvo sentence (§4). D3 is met by R2-2. No new physical assumption is made,
  and full OI–QM equivalence is not claimed. Non-claims 1 and 2 stand.
- **R11 and R12 markers.** All are kept, at l.14, 178, 187, 194, 203, 241 and 251.

## 9. Nits

**T1 (apply).** §6.4(5): replace "the lattice" as given in §5 above.

**T2 (apply, or owner).** §6.5 item 4 lost CONTRIBUTION-r4 non-claim 6's last clause, that the
black-hole reviews are internal and not external validation. The editorial rule against
review-process prose in the paper conflicts with stating the evidential status. Both are satisfied
by putting the status in the two bibliography entries. Append to [BHa] and [BHb]:
> unpublished research record, internally reviewed

**N1.** l.114: the cite "[Main §1.3]" could name its object, as "[Main §1.3, the realization
clause of (C4)]", since the term "routed readback" is the kernel's and does not appear in Main.

**N2.** [Cal26]: the claim was read in full text in the literature study (AUDIT r4 C4: "Thm 1,
p. 4", [FT]). Change the VERIFY to cite that record, or cite "[Cal26, Thm 1]". The journal
version is a Crossref record only: *Quantum Stud. Math. Found.* 14, 2 (2026),
doi 10.1007/s40509-026-00415-9. The arXiv entry is fine as it is.

**N3.** §6.5 item 4: "the results of §5 are finite toy-model computations". §5.2's C6(a) and
C6(b) are written proofs, not computations. Write "the results of §5 concern finite toy models,
proved on paper and checked exhaustively at small size or by exact arithmetic".
