# Independent review of S3-U4 r1 (route M and the parked-record case)

**Object.** `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/S3-U4-r1.md`,
blob `e6d8101a2e8017c9b1d09a0909e66c1faae52df7`, at PR #1294 head
`3a08a4463b64bde2fa1cd09e2c415b7a65972180`.

**Reviewer.** A separate, non-author Claude reviewer. Read-only: no repository edit, commit, push,
computation, Lean or Issue change. All checks below are by reading and hand algebra.

**Governing documents read.** S3-PLAN-r9 (blob `46ebc72d`; §§8.1–8.6, §9 U4 row, gating), S3-U1-r5
(blob `68983f86`; AD-1(b), C-RET and its parked-record clause, §7), U4-SOURCES-r1 (blob `2e75b886`),
VERIFY-SL3-CC-r1 (blob `4baa0283`), VERIFY-SL3-CC-r2 (blob `9f81ad0e`) and its response
`RESPONSE-VERIFY-SL3-CC-r1.md`. Corpus at `origin/main` = `75cc51009aebcfb17c1bbf76d149760c540aac3b`:
MR★ (blob `45af1678`), PREREG (blob `c36fb14b`), Main, GR, Substratum, SM:252, ch15, ch18, OAC,
AP1, CWR, NIS2 STATUS and SOURCE-SCREEN, `composition-access-20261024/REPORT.md`. Owner records on
#1169: c.6890079967, c.6891230989, c.6891241282, c.6891338304, c.6891511297 (all `amaybaum`). The
owner refinement on compatibility and support is taken as relayed in the brief and in U4's header; no
#1169 comment carrying it was located (finding 13).

## Verdict: REVISE

The note's central outcome stands: **D-1 undecided at (γ)**, with (β)–(δ) unsourced for the native
marker where masking is complete, and nothing counting toward a negative closure under SNR-1. Route M
is not closed. U4-F1, the conclusion of U4-F2, PK-1 (with a scope fix), PK-2, PK-3, PK-5, PK-6 and
U4-F7 check out by hand at their stated status. Three things need a revision before acceptance:

- PK-4 and U4-F4 are false as stated (finding 1);
- QM-4's "exclude each other" overstates the complementarity bound (finding 2);
- the "explanatory compatibility" label is applied to a native mechanism whose compatibility is not
  shown (finding 3).

The note also predates two owner records it must now reflect: VER r2 was accepted (c.6891511297), and
r2's Sup-3 bears directly on U4 §2.2 and on PK-1 (finding 4).

## Findings

### Required

**1. PK-4 and U4-F4 are false: parking is neither necessary nor sufficient for losing S-L7's
restriction.** PK-4 says S-L7's epistemic restriction "holds exactly while the one-tick parked value is
**not** recovered" and that "a parked value that becomes accessible again removes that restriction".
Hand check on the K1 step `φ(x, y) = (y, A y − x)`, with S-L7's bracket
`cJc′ᵀ = c₁·c₂′ − c₂·c₁′` (MR★:606–608):
- Write `u_{t+k} = U_k(A) u_t − U_{k−1}(A) u_{t−1}`, with `U_{−1} = 0`, `U_0 = I`,
  `U_k = A U_{k−1} − U_{k−2}`. The current-slice read of site `w` at `t+k`, in time-`t` coordinates, is
  `(−U_{k−1} e_w, U_k e_w)`. Its bracket with the read of `v` at `t`, `(0, e_v)`, is `(U_{k−1}(A))_{vw}`.
  At `k = 1` this is `δ_{vw}`: S-L7's second pair, reproduced.
- *Recovery without losing the restriction.* Under A-cur, `V` recovers the parked value `u_t(v)` at
  `t+2` from `u_t(v) = (A u_{t+1})_v − u_{t+2}(v)`, holding its retained reads `u_{t+1}(w)` for `w ∼ v`
  and its read `u_{t+2}(v)`. Every pair in that set has bracket `0`: equal-time reads commute, and
  consecutive-tick reads of distinct sites give `δ_{wv} = 0` (the stencil is centre-free). The set is
  isotropic, its span contains the recovered parked value, and it also holds the neighbours' parked
  values `u_{t+1}(w)` at `t+2`. So the restriction survives recovery.
- *Losing the restriction needs a conjugate partner, not parking.* What breaks isotropy is a retained
  pair with nonzero `(U_{k−1}(A))_{vw}`: the same site at consecutive ticks (S-L7's pair, which under
  A-cur is a parked value held with that site's current value), and also a site and a neighbour two
  ticks apart (bracket `a ≠ 0`).
- S-L7's own wording "retains the earlier of two consecutive reads, is not" is literally broader than
  its computed pair, which is site-specific. U4 should use the computed content, not the wording.

*Required change:* restate PK-4 as follows. Under A-cur, S-L7's single-tick restriction fails when `V`
holds a parked value together with its conjugate partner. Recovery or retention of parked values does
not by itself remove the restriction. Reclassify U4-F4 and restate its assumption-watch marker in that
form, since the marker propagates to every K1 account of complementarity by epistemic restriction.
"Tested against both slice forms" (§8) did not catch this.

**2. QM-4 overstates the complementarity bound.** `D² + V² ≤ 1` (Englert 1996; PREREG:232–233 derives
equality for pure marker states) is a trade-off, not an exclusion.
- With `D` taken over the whole complement and a pure joint state, `D = √(1 − V²)`. An intact return,
  a unitary transfer inside the complement, changes neither quantity (QM-1), so in those terms a
  "return" is not a change of `D` at all.
- A record's return is an increase of the *accessible* distinguishability `D_acc ≤ D_whole`. Then
  `D_acc² + V² ≤ 1`, and a partial revival of `V` can coincide with a partial rise of `D_acc`. For
  example, `(V, D_acc)` can move from `(0.3, 0.1)` to `(0.5, 0.8)`.
- Exclusion holds only at the extremes: full return (`D_acc = 1`) forces `V = 0`, and full revival
  (`V = 1`) forces `D = 0`.

*Required change:* replace "exclude each other" with the trade-off. Keep the two
distinguishabilities apart, `D_whole` for the bound and `D_acc` for "return". Note that the §6.3
accessibility argument compares `V` at the parking tick with `D` at the retrieval tick, so it needs QM-1's
invariance: only the complement evolves between the two ticks. Say so explicitly. The same correction
applies to §6.3's phrase "lowers path distinguishability in the whole complement" and to §10's
summary. Englert 1996 is [EXT], read in abstract only (INV 5.3), and should be labelled that way at
QM-4.

**3. "Explanatory compatibility" is applied where compatibility is not shown.** The owner refinement
applies the label when no observable distinguishes the account from ordinary erasure, revivals or
memory effects. That presupposes an account that agrees with the data. §6.3 says that, by PK-2, OI's
native mechanism "predicts neither QM's record-tied visibility loss nor any alternative to it". Only
the first half is accurate:
- if (γ) were supplied, PK-2 with a quiet marker predicts fringes intact under a stored, unread record.
  That is an alternative, and it disagrees with E-1 as attributed. It is D-1's quiet-marker branch: an
  assumed apparatus, not counted toward (a′), but not compatibility either;
- for the native marker, a noise-driven drop that tracks `D` is not shown (PLAN §8.4, native-marker
  miss branch).

§6.3 presents PK-2 only as protective ("on K1 PK-2 excludes" the accessibility reading). It omits PK-2's
tension with E-1. That is the favourable-branch reading §A.31 asks to pressure-test.

*Required change:* report U4-F8 and §10 as follows: no distinguishing observable is derived; no
independent experimental support; explanatory compatibility is **not shown** for the native K1
mechanism, since PK-2 against E-1 is a potential raw-direct conflict, undecided at (γ) and confined to
an assumed quiet marker. "Explanatory compatibility, not independent experimental support" can then
apply only to the class-(ii) reading (QM-1 to QM-5), which is standard QM and adds nothing native.

**4. Status propagation: VER r2 and its acceptance supersede the inputs U4 cites.** U4 cites
VERIFY-SL3-CC-r1 at `4ce925ad` and treats S-L3 and CC4/CC5/CC7 as named premises throughout
(§§2.2, 6.4, 9, 10). The brief also describes r2 as unreviewed. On the record, r2 (`9f81ad0e`) was
committed before U4 (`d195a29f`, 08:05:10Z), and the owner accepted it at `25207fae` in c.6891511297
(08:11Z):
- S-L3 is verified for its four bullets;
- the gloss "erasure unavailable on K1" is verified at the narrower scope;
- the supplements are credited to the record;
- CC4, CC5 and CC7 are verified at narrower scopes;
- outside those scopes all four remain named premises.

Required consequences in U4:
- **§2.2 attribution.** "S-L3 excludes executing `σ`, a block swap `σ_X ⊕ g`, or the inverse of a
  marking evolution within a budget below recurrence." Under r2 only the first is S-L3's. The block
  swap is the record's Sup-1, and the marking inverse within the budget is its Sup-2.
- **§2.2 μ-assumed-inputs bullet.** It reads "no datum of μ makes `σ`, a block swap or the inverse of a
  marking evolution executable". This is contradicted in the marginal sense by r2's Sup-3, now accepted.
  One native tick applies `σ_X` to a one-site region (and to any independent set of sites) whose
  neighbours' current slice is `0`, a condition a μ-assumed datum can supply. Sup-3 gives no erasure,
  since reversal needs the inverse on the record's whole support (S-C4a). The bullet must say so rather
  than deny it.
- **PK-1 and Sup-3 are one phenomenon.** Sup-3's marginal swap is exactly one-tick parking at a
  one-site region. Cross-reference it.
- **SNR-1 standing of the S-L3 branch.** The independent-verification condition of PLAN §8.4 is now met
  at S-L3's scope. Only the U1 re-check (author-side in §2.2) and U4-F2's T3-sense obstacle remain. That
  makes U4-F2 the operative reason the branch does not count; see finding 5.
- **CC scopes in §6.4.** Use r2's scopes: CC5's T4 match needs uniform `e` and readings G-CC5-1 to
  G-CC5-3; CC4's needs G-CC4-1 and G-CC4-2; CC7's `V = 0` needs uniform `f`.
- **Owner questions 2 and 3.** Both are answered by c.6891511297, items (2a) and (2b): the
  first-hand literature unit and the two calculations are authorized. Update §10 and the routing list.

**5. U4-F2's conclusion holds; its mechanism sentence conflates two kinds of restoration.** The
conclusion is correct and is consistent with VER r2 §6. On K1 the visibility loss is a carrier-free
offset (S-L5), so restoring visibility needs no inverse of the coupling. Whether an available `φ^n`
restores it is a T3-sense question outside S-L3, and the branch does not reach the raw-direct
observable. But §4.2 supports the removal with "a region holding a correlated copy of the offending
content has a matching transfer to `D` (the recovery identity OAC:132–134 has this form)". The OAC
identity `S = R − K` is an observer-side decoding of two retained readouts. That is a conditional
recovery of the sorting (T4/CC5) kind, which PLAN §8.4 explicitly sets outside the S-L3 branch. An
unconditional restoration at `D` is a property of the fixed transfers: whether, at some tick `n`, the
noise term `Σ_{X≠Σ} Φ^n_{DX} s_X` stops masking the carrier's image `Φ^n_{DΣ} s_Σ`. This is the same
coset question as §3.2, posed at `D`.

*Required change:* state the two routes separately. Unconditional restoration is the T3-sense calculation
now authorized in (2b). Conditional recovery through a retained copy is the T4 question. Also state
that F2's "does not count toward (a′) even after S-L3 is accepted" is a U4 finding against PLAN
§8.6's counting conditions, which stay as written pending owner question 4.

**6. The "accessibility reading" is defined inconsistently with its own prediction (§6.3).** It is
defined as visibility depending on "whether `V` holds or can retrieve the record". A parked record that
later returns *can* be retrieved, so under the stated definition this reading predicts **no** fringes
while the record is parked, the opposite of the prediction §6.3 derives. The derived prediction
follows only from a time-indexed reading: whether `V` holds the record at the recombination tick.

*Required change:* fix the definition, with its time index, before testing it against E-2. With the
heuristic "in principle retrievable" the reading coincides with QM's prediction in E-2 and is not
distinguishable.

**7. §6.4 generalizes from two toy controls to "any eraser phenomenology".** "Any eraser phenomenology a
parked record produces is therefore of a kind classical models reproduce" is a finite-witness-to-
universal step. CC5 reproduces PC-Q's T4 conditional-fringe law, CC4 reproduces T1–T4 under its
readings, and both are at VER r2's narrower scopes. Neither bears on W1-type behaviour, which (e′)
itself reserves.

*Required change:* restrict the sentence to T4-type conditional-fringe recovery at r2's scopes. State that
whether a parked record could produce W1-type behaviour is not addressed.

**8. §5's "performed experiments" table mixes performed experiments with proposals and theory.**
- In E-1, Scully–Englert–Walther 1991 is a proposal. PREREG's own table says they "propose marking by a
  cavity photon". Englert 1996 is theory. Of E-1's sources, only Dürr–Nonn–Rempe 1998 is a performed
  experiment.
- In E-2, Kwiat–Steinberg–Chiao 1992 and Herzog et al. 1995 are erasers but not delayed-choice ones,
  so their parking interval is trivial; Ma–Kofler–Zeilinger 2016 is a review.

*Required change:* mark each source as performed, proposal, theory or review. Restrict "delayed-choice
erasers are performed parked-record experiments" to Kim et al. 2000 and Walborn et al. 2002, pending
first-hand reads.

Also carry into the (2a) unit two raw-direct (§A.24) checks the note's summary does not flag:
- whether the unsorted signal pattern was **measured** as singles or is inferred from summed
  coincidence channels;
- that sorted channels sum to the unsorted pattern only with full branch masses (R5, K-6). Finite
  idler detection efficiency and coincidence windows break that sum in the raw data.

The literature-dependence labelling itself is adequate: §5's header, the parentheticals in §6.3,
U4-F6's "pending first-hand reads" and AC-1's "as attributed" all carry it.

**9. The C/Q sentence needs the agreement requirement.** "If fresh-cell renewal were sourced, a C fixed
by these limits alone would contain PR, which would be a prediction about unperformed experiments ...
not a defect" (§7). Under c.6891338304 this holds only if C's predictions for *performed* Bell
experiments still match the observed data, which respect the quantum bound. A C that yields PR
statistics for the configurations already performed is a raw-direct miss, not a prediction.

*Required change:* add that condition. "C ⊆ Q undetermined" itself is correct.

**10. The tier claim is stated favourably.** §10 says "the weaker tier, in part". PLAN §8.6's weaker tier
is a class-(i) result: recording explains memory and some measurement behaviour. U4 states that record
formation on K1 stays unsourced, and what it supplies is definitional ([P]) or conditional.

*Required change:* report "weaker tier not reached; definitional and conditional groundwork recorded"
(§A.22: a valence move needs a new result).

### Minor

**11. Wording of S-L5 per C-9.** PK-2 and §4.2 say the offset comes from "carrier-independent content".
C-9 (MR★:1433–1440) replaces that with "content that is not a function of the carrier's content", and
adds that under `μ` it may be correlated with the carrier. §2.1 uses the C-9 wording; PK-2, §4.2 and
U4-F3 should match it. A μ correlated with the carrier is not covered by PK-2's "no record-tied
consequence" without a check.

**12. U4-F1 can be sharpened at one tick.** U4-F1 is correct: under μ-G, conditional on `s_Σ`, the
marker's content is uniform on `Φ^t_{AΣ} s_Σ + K^t_A`, and complete masking holds iff
`im Φ^t_{AΣ} ⊆ K^t_A`. Hand check: `Φ^1_{AA}(x, y) = (y, A_{AA} y − x)` is an automorphism of `S_A`,
with inverse `(x′, y′) ↦ (A_{AA} x′ − y′, x′)`. So `K^1_A = S_A` for every marker region, and masking is
complete at `t = 1`; the plan's sentence is exact there. Whether masking is incomplete is open only for
`t ≥ 2`. A sufficient condition for complete masking is surjectivity of
`s_{Σ^c} ↦ pr_A φ^t ι_{Σ^c} s_{Σ^c}`. Recording this narrows the (2b) calculation. U4-F1's NEW
classification is justified.

**13. Provenance.** The owner refinement is quoted as relayed, with no comment id. Under §A.42 item 7
the record should quote the comment that carries it, once there is one, with author and time.
- The header gives the PR head as `4ce925ad`, but U4 is at `3a08a446`, and r2 of VER and U2 r1 were
  added in between.
- R-c and R-b in §6.3 are undefined in U4.
- QM-5's second sentence ("Visibility depends on the existence of distinguishable path-correlated
  content ...") is an inference, class (ii), and should not carry GR:350's [M].
- In §6.3 the D–V observable is a joint statistic over runs at one tick, not "per-run": `V` is a
  contrast.
- ch18:78 is quoted only for "standard open-systems phenomenology". The same sentence continues "what is
  distinctive here is the proposed capacity-controlled origin and the specific scaling law", and ch15
  (:156, :214) claims `𝓕(r) = 2r − r²` as a proposed, not derived, discriminator against the
  alternatives considered. U4's conclusion is unaffected, because that proposal concerns visible-law
  revival and is not tied to which-path coherence. The quotation should include the continuation.
- PK-1's "and only there" should be scoped to same-site slice parking. Transport of content out of `V`
  into hidden sites and back is not excluded under A-reg (S-C4a), and it is undecided as retention.

## The writer's claims, item by item

| Claim | Review |
|---|---|
| D-1 undecided at (γ) (Main:682); (α) per reading; (δ) only the native noisy marker sourced; carrier preparation and T0 unsourced | Confirmed (Main:682; Substratum:463; MR★:642, :651; PREREG:471–477) |
| U4-F1 | Confirmed and correctly NEW; sharpened at `t = 1` (finding 12) |
| U4-F2 | Conclusion confirmed and consistent with VER r2 §6; mechanism sentence to be split (finding 5) |
| PK-1 | Confirmed for same-site one-tick parking under A-cur (SM:252, Lemma 1c (iii)); scope fix (finding 13); identical to Sup-3 (finding 4) |
| PK-2 | Confirmed at fixed geometry under S-L1 and S-L5 [NP], global reading; C-9 wording (finding 11); its tension with E-1 omitted (finding 3) |
| PK-3 | Confirmed (OAC:132–134) |
| PK-4 | **False as stated** (finding 1) |
| PK-5 and Lemma R | Confirmed: Lemma R (PREREG:177–182) is injectivity; the freshness link matches REPORT.md:57–69 |
| PK-6 | Confirmed: Main:200 is a diagonal, visible-law readback; `𝒩` (ch18:74) is a total-variation distance; CWR is a research candidate with a 27-site readout. U4-F7 is a sound [A-inf], given that identifying the visible configuration with "path" is itself a (γ)-type step |
| QM-1, QM-3 | Correct as class (ii) |
| QM-4 | Overstated (finding 2) |
| No discriminating prediction, hence explanatory compatibility | First half confirmed; the label is misapplied to the native mechanism (finding 3) |
| Delayed-choice erasers as parked-record experiments; the accessibility reading disagrees | The attributed standard content is right (unsorted pattern without fringes; fringes and antifringes summing to it; none under a path readout). Labelled as unread. Definition inconsistent (finding 6); source typing (finding 8) |
| C ⊆ Q undetermined; records, retention and parking do not exclude PR; fresh-cell PR executability unsourced | Confirmed at [OFF] support (SEL-EXCL-1, reviewed); agreement caveat needed (finding 9) |

## Brief items 1–8

1. PK claims and Lemma R checked by hand: findings 1, 11 to 13, and the table above.
2. U4-F1 and U4-F2 are correct at their status, with the changes in findings 5 and 12.
3. `D² + V² ≤ 1` is correct, but "exclude each other" is overstated, because the bound allows partial
   values of both (finding 2).
4. Delayed-choice erasers: the performed data, as standardly reported, show conditional fringes with the
   unconditional pattern unchanged. The accessibility reading disagrees only under a time-indexed
   definition (finding 6). The claim rests on unread literature and is labelled so; source typing needs
   fixing (finding 8).
5. The owner's compatibility-versus-support rule is applied to agreement with eraser data ("not
   evidence"). Its compatibility half is misapplied (finding 3).
6. SNR-1 and gating are applied: nothing counts toward (a′) to (e′) as a negative, and route M stays
   open. The tier claim needs tempering (finding 10).
7. S-L3 and CC* are treated as named premises, but this status is now out of date (finding 4).
8. No new physical premise is adopted. The three return kinds of §6 are [P] refinements of C-RET and are
   put to the owner (owner question 1). Conditional statements presented as established: §6.4's "any
   eraser phenomenology" (finding 7) and the tier claim (finding 10). Soundness is not treated as
   required: AC-1 and the C/Q finding follow c.6891338304.

## Checked and not checked

**Checked:**
- every Main, GR, Substratum, SM:252, ch15 and ch18 quotation U4 relies on;
- MR★ S.1–S.3, S-L1 to S-L3, S-L5, S-L7, S-C1, C-4, C-9, :640–:651 and σ12;
- PREREG:162–233, 471–491 and 519;
- OAC:100–140, REPORT.md:55–69, CWR in full, AP1's header and §4.5 lines, NIS2 STATUS:25–33 and its
  rule (non-additive, OR term);
- U1's AD-1(b), C-RET and its parked-record clause;
- PLAN §8 in full and the U4 row;
- VER r1 to r2 differences, r2 §§1.3, 1.5, 6 and 7;
- the owner comments listed above;
- the cited blobs at `3a08a446` and at `4ce925ad`;
- hand algebra for the S-L7 bracket of multi-tick reads, `Φ^1_{AA}`, and the coset statement of §3.2.

**Not checked:**
- the external literature, which U4 also did not read first-hand;
- S-L5's proof beyond restating it from S-L1;
- U1's G4 and AW items beyond what U4 cites;
- SEL-EXCL-1 at `0ecfddeb`, which is off `main`;
- whether `K^t_A = S_A` for `t ≥ 2` and the T3-sense question, both calculations now authorized under
  (2b);
- U2 r1;
- the INV entries beyond the items cited.
