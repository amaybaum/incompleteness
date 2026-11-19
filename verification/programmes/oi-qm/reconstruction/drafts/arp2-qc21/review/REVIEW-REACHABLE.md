# Review of REACHABLE.md (ARP-2 / Q-C2-1, reachable law set on U′)

**Reviewed object.** `REACHABLE.md` (Q-C2-1 working file, not published), sha256
`c65a9d37a7123e01bfa3d7a0b664fb436fb880fbe029a3d08fa7f48246aed2c0` (378 lines). Line numbers below refer to it.

**Reviewer standing.** Independent model reviewer, read-only, 2026-11-08. This review is not human verification. It
changes no record, and nothing in it adopts or promotes a claim.

**Sources checked against `origin/main` = `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`.** The copies in `qc21/src/`
match the blobs on `main` byte for byte (`git hash-object`): QA `fb21999b`, QA-PR `fea582d7`, FB `a00b3b7f`, M2D
`9352d9da`, MINACC RESULT `5adf76eb`. AP1 (`51c24aeb`) was read from `main` (no copy in `src/`). Substratum A2–A5
(SUB:94-100) is identical at `b1d782f9` and `2cd49dc0`. Owner records #1169 c.6723277401, c.6723329527,
c.6723491138 and c.6723571280 were read through the API. AUDIT-C2 §17 (Q-C2-1) and AUDIT-C3 §§0, 3, 6, 9, 10 were
read in scratch.

**Controls run by the reviewer** (`review/controls_review.py`, exact F₂/integer/Fraction arithmetic, `python3 -I -B`,
12/12 PASS). These are controls, not evidence:
- RC1: random protocols in the class "affine symplectic steps + P2 supplies + P1-terminal registration, forward
  conditioning". This class is a superset of class N on U′. In 3,000 trials every fully conditioned carrier law has
  at most one `f_a` determined, and its determined carrier set is `Q*`-totally singular. Five countercontrols break
  as they must: retrodictive conditioning, re-coupling a registered cell, a non-symmetric `K`, a supplied sharp
  cell, and centre terms. Centre terms keep `V₀` and break only `Q* = 0`.
- RC2: over all of AGL(4,2), 768 affine carrier bijections induce a map on all laws. They give exactly 48 distinct
  signed permutations, 24 with det +1 and 24 with det −1, each realized 16 times. This matches AUDIT-C2's 384 + 384.
- RC3 (static only): the four non-affine triangle rules change `Q = Σ u_i v_i` on 8, 24, 8 and 24 of 64
  configurations (AND, NAND, OR, NOR). The linear rules 0 and XOR conserve `Q`. The offset rules 1 and XNOR change it
  through their constant. **No reachable set was computed under any non-affine rule.** That is the decisive
  computation of a round not yet frozen, and running it here would expose its outcome before `F`.
- RC4: a 3/4 herald applied to `V₀` branches gives `ℓ1 ≤ 1`.
- The writer's `controls/sanity.py` (sha256 `2077db9d…`) was re-run: 27/27 PASS. Its checks were read and are
  faithful to the statements they test.

## Verdict: **REVISE**

The mathematical core survives review. Theorem C (ii)–(iii) — confinement to `O` and signed-permutation induced
maps — is correct at paper level under hypotheses that can be stated exactly. The re-derivation below and RC1–RC2
agree with it.

Five findings block. Three are scope or labelling defects:
- B1: the headline says "any record conditioning", but retrodictive conditioning is a counterexample on `main`;
- B2: the extension of AP1 Lemma 3 beyond SA-1 is mis-attributed;
- B3: the NE "consequence" claims more than Theorem C and Prop D give.

Two concern the decided object of ARP-2:
- B4: NE-1 is broader than the native class, and leaves room for discretion;
- B5: the narrowing says the non-affine family "keeps isotropy", which is false for this family, and it omits the
  two corpus results that bear directly on route S-5.

All five fixes are textual or definitional. None needs a new derivation, except restricting the NE consequence to
its proved scope.

**The witness-principle question.** Theorem C is the kind of theorem the principle asks for: it is not a failed
search. With the B1–B3 corrections it is a stated impossibility within the following scope:
- `q = 2`;
- U′ with the linear identification R, and exactly encoded-induced maps;
- affine symplectic dynamics. Class N, with or without NNB, is an instance. Centre terms are harmless for
  (ii)–(iii);
- P1 terminal registration, with registered cells decoupled from every cell, hidden sector included (that is,
  P3/E-iso as implemented);
- P2 supplies with N2, and H-INF-μ read as the uniform product;
- conditioning on events of record values registered no later than the time of the carrier law;
- bounded finite protocols, for the `Q³` refinement only.

It is conditional on three WIP records: AP1 Lemma 3, QA Lemma Q(iii)'s per-branch extension, and MINACC's C-LIN
re-derivation. It is reviewed only by this model review. It must not be cited as established (§A.46 item 1).

## Reconciliation with AUDIT-C2's (2/3, 2/3, −1/3) remark

Neither document is wrong. AUDIT-C2 (§17, "Still open") makes an **arithmetic** remark: once heralds are allowed,
denominators other than powers of 2 occur, so the 2-adic descent no longer forces axis vectors, and rational
orthogonal rows such as `(2/3, 2/3, −1/3)` become arithmetically admissible. The audit exhibits no reachable law
with that image, and it says no runnable check exists until L is characterized. Theorem C supplies that
characterization. It replaces the dyadic argument with a convexity argument that does not depend on denominators:
- every fully conditioned branch lies in `V₀`;
- every reachable law is a convex combination of branches, so `ℓ1 ≤ 1`;
- the row has `ℓ1 = 5/3`.

The audit's "a 3/4 herald gives denominator 3" is correct, and it agrees with Theorem C(ii)'s `Q³` (RC4). REACHABLE
says this correctly at :264-266.

The audit's own protocol class is wider than the native class. It is Lemma F's class: "cells attached in **any
fixed law**", and conditioning on configuration records (AUDIT-C2 §17; M2D:313-318). A protocol in that class that
puts this row in the image of a law must break one of the posits:
- S-1: N2 or P2;
- S-2: a conditioning predicate that is not a registered record;
- S-3: unrecorded mixtures of non-isotropic components;
- S-4: P1, including retrodiction (B1);
- S-5: affinity.

So the row is non-native whenever it is the image of a reachable law under affine dynamics. The posit it breaks is
whichever of S-1 to S-4 the construction uses. The audit's "still open" stands for supplies outside `conv S_nat`
and for non-affine dynamics, as REACHABLE's §2.5 rows 7-8 record.

## Blocking findings

**B1. "Any record conditioning" is wider than the proof (:35-36, :96-101, :127-129, :173-175).**
The proof chain proves confinement only for the carrier law at time `t` given records registered by `t`. It needs
two things for that:
- AP1 Lemma 3 bounds "functionals on the active cells … at every tick" (AP1:535-538);
- QA Lemma Q(iii) bounds what is determined about cells active at the time of determination (AUDIT-C3 §3).

MINACC RESULT §6.3 ("PROT-R fails", on `main`) gives a one-tick counterexample in both linear limits. A ready cell
with known `u = 0` has its unknown `v` read through `u_0(1)`, and its `t = 0` state, `Q* = 1` functional included,
is then determined. On U′ the same thing happens: a carrier in `Λ_{z,0}`, conditioned on a later `X` read, has
`f_z` and `f_x` both determined, so its `t`-law has an image outside the ball (RC1(a)).

The headline also leaves out a hypothesis the proof uses. P1's terminality ("not coupled to any cell afterwards",
AP1:294-295) is implemented only through P3/E-iso, and it is not native (AP1:338-343; AUDIT-C3 §10). In the native
world a registered meter would stay coupled to the hidden sector, and that is the RC1(b) countercase.

*Fix.*
- Define L as the set of carrier laws at a time `t`, conditioned on events of values of slots registered at or
  before `t`.
- State in §0 and §2.2 that pre- and post-selected (retrodicted) carrier laws lie outside Theorem C, and can leave
  the ball.
- Add to the hypothesis list "registered cells are decoupled from every cell, hidden sector included (P1 as
  implemented by P3/E-iso)".
- Replace "any record conditioning, any herald" at :35-36 with "conditioning on any event of earlier registered
  record values, including heralds whose probability depends on the input".

**B2. Lemma 4's layer and Theorem C's dependence statement are mis-attributed (:162-165, :188-189).**
AP1 Lemma 3 is scoped "Under SA-1" (AP1:533). SA-1 covers:
- a one-cell carrier;
- carrier–meter–record couplings;
- P1;
- P2 with its support condition.

AUDIT-C3 §6 says this, and AUDIT-C3 §6 also requires downstream citations to carry "under SA-1". Theorem C applies
the lemma to more than SA-1:
- a two-cell carrier;
- hidden-sector couplings;
- NNB;
- adaptive armings and translations;
- reuse.

That extension is not in AP1. It is QA Lemma Q(iii)'s per-branch argument (QA:476-492: "Condition on all of the
observer's records. Each branch is then a fixed sequence of symplectic … steps and constant translations"). MINACC
§6.3 (C-LIN) re-derives it independently, with reserve cells, refills and archives. Both are WIP.

So the statement at :189, "(ii) and (iii) need only isotropy (Lemma 4's AP1 part)", is wrong: (ii) and (iii) need
the isotropy half of QA's extension.

Prop E and NE-1 extend further, to `S_nat` supplies whose known set is any isotropic set. That includes multi-cell
known functionals, and a single-cell known `u + v`, which has `Q* = 1` and which P2 excludes (QA:780). No record
states this. It is valid, because AP1's proof uses only "`I` is isotropic" (AP1:539-541), but it is "paper here".

The extension to state-dependent heralds and adaptivity is **not** a silent extension of Lemma 3:
- a native herald is a registered record value;
- given the full record, an adaptive protocol coincides with the fixed protocol `σ(r)` on the event `{records = r}`.

The causal argument is in Lemma 1 (:149-150) and QA:484-486. It is sound.

*Fix.*
- Re-label Lemma 4: "record: AP1 Lemma 3 (under SA-1); extended to class N, NNB and adaptive processes by QA Lemma
  Q(iii)'s per-branch argument (QA:476-492) and MINACC §6.3; to `S_nat` supplies: paper here".
- Correct :189 to match.
- Cite MINACC in the Sources table.

**B3. The NE "consequence" claims more than Theorem C and Prop D give (:300-302, also :292-293).**
"If `G` is affine and NE-1, NE-2 hold, Theorem C (or Prop D) excludes a witness … This is a theorem." That sentence
is not proved as stated, for four reasons.

- (a) Prop D does not exclude a witness. Its second branch reaches a law outside the ball. Coarse conditioning on
  **recorded** labels then gives laws in `ball \ O`, which is exactly :221-222's S6 pattern. The witness tuple
  `(Σ, C, G, B, β)` carries no E-BALL requirement on L.
- (b) Prop D needs pure supplies (:216), while NE-1 admits declared mixtures. Under non-symplectic affine dynamics,
  mixtures under unrecorded labels can give `ball \ O` with valid observed laws. Prop D's own caveat (:220-221)
  says so.
- (c) NE-2 says "registered record slots" and requires neither P1 terminality nor time order (B1).
- (d) The same defect affects NE-3's gloss "(or Prop D's for non-symplectic affine members)" (:292-293). A
  non-symplectic affine member could fail NE-3 legitimately, through the Prop D pattern, without anything being
  embedded.

*Fix.*
- State the consequence for affine **symplectic** `G` only. Class N, every affine member of the triangle family, and
  NNB all qualify; RC3 and the linear part `K = k·A_triangle` confirm that the triangle family's affine members are
  symmetric.
- Make NE-2 require P1 terminality (B1) and forward-time conditioning.
- Either drop "(or Prop D)", or add a witness condition NE-0: E-BALL holds on all of L. With E-BALL on L and pure
  supplies, Prop D does give `R(L) ⊆ O`.
- Phrase the conclusion as "under affine symplectic dynamics, a witness that meets NE-1 and NE-2 does not exist
  (Theorem C, conditional on its WIP inputs)".

**B4. NE-1 is broader than the native supply class and leaves discretion (:286-287; table :109-117).**
NE-1 admits every `S_nat` law and every "declared mixture" of `S_nat` laws. `S_nat` (:105-106) includes supplies
that are not native:
- a cell with known `u + v` (`Q* = 1`), which P2 excludes (QA:780);
- supplies with known multi-cell functionals;
- real-weight mixtures, which need a supplied biased coin (:113).

Three features of NE-1 leave room for judgement:
- "Declared" makes membership depend on what the witness declares.
- The parenthetical "(and `Q* = 0` on it, for P2-type supplies)" leaves open which supplies count as P2-type.
- Prop E calls real-weight mixtures harmless, and that holds only under affine dynamics. Under a non-affine `g`, a
  `Q* = 1`-known supply that passes NE-1 is precisely a candidate carrier of non-stabilizer content "embedded in the
  definitions", the case the owner's Q-C2-1 safeguard excludes (c.6723571280).

*Fix.*
- Make NE-1 the native class exactly: P2 ready cells, meaning one known **slot** with value 0, or 1 through
  H-PREP, and the other slot uniform under N2; products of these; H-PREP preparations of the QA family; and uniform
  hidden cells under H-INF-μ. Test membership structurally.
- Admit mixtures only with recorded labels, which native record conditioning provides with rational weights.
- If a wider tier (`S_nat`, or `conv S_nat` with real weights) is kept, label it as a separate, non-native tier,
  and decide membership in `conv S_nat` by exact LP rather than by declaration.

**B5. The narrowing of ARP-2's decided object states a false property and omits the corpus data on S-5 (:313-318,
:346-348).**
- O-1 says the round "tests the smallest family that keeps A2, A4 (both senses) and isotropy and drops only
  affinity". Isotropy is a property of linear transport of determined functionals (AP1 Lemma 3; QA Lemma Q(ii)),
  and it is undefined for non-affine transport. M2D Lemma Qσ and MINACC node 1 say so.
- Two results on `main` show the property fails for rules of this kind:
  - MINACC's `G_σ` is symmetric, centre-free, `Q`-conserving and non-affine. Under P1 and P2 it **breaks** AP1
    Lemma 3's isotropy: `E_A` and `E_B` make an active cell sharp in every branch (MINACC RESULT :37-69, C-L3).
  - All four non-affine triangle rules fail even Lemma Q(i), since they do not conserve `Q` (RC3). By Lemma Qσ the
    change is `Σ_i u_i g(u_{i−1}, u_{i+1})`: that is `u_0 u_1 u_2` for AND and OR, and `Σ_i u_i + u_0 u_1 u_2` for
    NAND and NOR.
- So "isotropy" is an outcome to measure, not a kept property of the family.
- The S-5 row (:276) and O-1 omit M2D's P★ (M2D:630-703). Under the non-affine `G_SM`, with P2 and H-PREP and P1
  not implemented, P★ already reaches a **valid** branch with `r = (3/5, 1/5, 3/5)` (`ℓ1 = 7/5`, inside the ball,
  outside `O`) together with a non-PSD companion branch, `(1/3, −1/3, −1)`.
- P★ and MINACC are the existing corpus data on S-5. §A.19 requires citing them before stating O-1 as a gap.
- O-1 stays open as scoped: symmetric `g`, P1 terminal, U′ and an induced rotation. But the document should say how
  ARP-2 differs from P★ and from MINACC, and that both point to a Prop D-like pattern: non-stabilizer validity
  appears together with invalid branches.

*Fix.*
- Delete "and isotropy" from :317 and the matching clause in PLAN:53.
- Add P★ and the MINACC exposure to §3.2 S-5 and to O-1, with how ARP-2's object differs from each.
- State that whether determined sets remain isotropic is among the measured quantities.

## Non-blocking findings

**N1. `Q³` depends on bounded protocols, contrary to :187-188 ("finiteness of the number of steps" not used).**
An adaptive repeat-until-success protocol terminates almost surely but is unbounded. It gives countable mixtures,
and their weights can be irrational: comparing record coins with the binary expansion of any `p` samples
`Bern(p)`. `⊆ O` survives because `O` is closed. `⊆ Q³` and Prop L's equality do not.
*Fix:* define a protocol as a bounded finite composite and remove "finiteness" from the not-used list. Or state
`R(L) ⊆ O` for a.s.-terminating protocols, and `= O ∩ Q³` (under NNB) for bounded ones.

**N2. Assumption-watch: exactness plus rational reach allows only rational rotations, for any dynamics.**
With N2, H-INF-μ and bounded protocols, every reachable law has rational probabilities, for **any** dynamics, affine
or not. So every exactly encoded-induced rotation on L is a rational orthogonal matrix. The `T` gate (π/4), and
every rotation with an irrational entry, is excluded by arithmetic, not by dynamics.

ARP-2's positive outcome can therefore only be a rational non-octahedral rotation, such as the 60° rotation of S3.
A null result says nothing about irrational or approximate gates. State this in §3.1 and §5, and carry it into the
preregistration's scope and its assumption-dependence analysis (ADA).

**N3. Theorem C(iii) without NNB (:131-133, :184-185).** The proof uses `β e_a ∈ R(L)` for all three axes. The
justification at :132 ("`Λ_{a,0} ∈ L`") rests on QA node 8, which is under NNB. Without NNB, `Λ_{y,·}` need not be
reachable.
*Repair:* two columns in `R(L) ∩ S²` suffice. They are `±e_b`, and orthogonality makes the third column `±` their
cross product. State also that an orthogonal `β` forces `α = 0` on `R(L) ⊇ V₀`, because `βO = O` and `O + α ⊆ O`
only for `α = 0`. Prop M's "exactly 48" needs this.

**N4. The induced-map definition with state-dependent heralds and reuse (:125-131; NE-4 :294-296).**
- For an input-dependent `q`, the map `μ ↦ Bμ/q(μ)` is not affine on mixtures. Agreement on `Λ_0` and `Λ_{a,0}`
  therefore does not imply agreement on L. The decision predicate must check the identity on a stated finite
  generating set of L **and** the herald condition: `q` constant on that set, or the full nonlinear identity.
- With reuse of retained cells or correlated hidden cells, the branch is a fixed carrier-level matrix only under
  H-LIFT (M2D Lemma F, :316-341).
- Theorem C(ii) does not need H-LIFT, and :191-192 is right about that. Defining `β` in (iii) for such protocols
  does need either H-LIFT or a definition at the level of joint laws. State which one.

**N5. Prop K (:224-232).**
- `K = conv R(L)` need not be closed. Write `cl K`, and take the volume argument on `cl K` (it is full-dimensional
  because `O ⊆ K`).
- "Non-Clifford rotation" should read "non-octahedral rotation".
- The group-theoretic step is correct. A5 has no subgroup of order 24, so the only finite subgroup containing the
  octahedral group is that group. An `O(2)`-type group preserves an axis pair, and the octahedral group does not.
- The step that compositions of induced maps are induced needs L to be closed under protocols. That holds by
  definition (:128).

**N6. Prop D (:215-222) and the §2.5 row "octahedral when E-BALL holds".** Both are correct only with E-BALL on all
of L, including fine branches, and with full-record conditioning available. Say so; the point is linked to B3(a).

**N7. Prop L (:196-200).**
- The `⊇` direction uses adaptive per-branch preparation, and uniform bits from native minimal reads of fresh
  unknown slots, since P1 registers meter slots, not "registered unknown slots".
- It rests on QA node 8 (NNB, WIP) and on bounded protocols (N1).
- The `⊆` direction and the arithmetic are correct.

**N8. Prop M (:202-206).**
- Correct given QA. The reflection `Y ↦ −Y` (`z_2 += 1`) is available **without** NNB (QA:729-731), and with the 24
  rotations it gives all 24 reflections. The separate availability of `L` is needed only for the attribution, and
  QA states it for `N_na` realizations only (QA:695-697).
- RC2 confirms the 48 maps among affine carrier bijections.
- "Exactly" also inherits the PROOF-RECOVERY §4 realizability of `H` (WIP).

**N9. Citations and provenance.**
- QA:240 is Lemma G1. The two-complementary-reads bound is QA node 2 (:323-338).
- SUB is cited "read at `b1d782f9`" while the file is pinned to `2cd49dc0`. The A2–A5 text is identical; cite
  `2cd49dc0`.
- Line 9 says the owner direction's #1169 record is "PENDING". It is recorded at c.6723571280
  (amaybaum, 2026-11-08T15:47:58Z).
- Specify that H-INF-μ is used as the **uniform** product: QA:788 says only "normalized product law".
- QA C-ROT's "dyadic, conditional on herald success" (QA:647-648) is false for herald probabilities that are not
  powers of 2. REACHABLE uses the correct ratio-of-dyadics (:112). Note the conflicting record statement as a
  finding, not as support.

**N10. Assumption-dependence analysis (owner direction c.6723491138).**
RC1 and the proof separate the essential posits from the inessential ones.

Essential posits, each with the countercontrol that breaks it:
- affinity (A5's affine part, partly derived);
- symplecticity, that is, symmetric (reciprocal) couplings: RC1(c);
- P1 terminality, including isolation: RC1(b);
- P2's one-known-slot clause: RC1(d);
- N2 uniformity: the `Bern(1/5)` example at :119-121;
- forward-time conditioning: RC1(a).

Inessential for (ii)–(iii):
- centre-freeness (A4, centre sense), which RC1(e) shows matters only for `Q* = 0`;
- linearity beyond affinity.

Classification: P1, P2, H-PREP and N2-through-H-PREP are supplied or imported; symmetry and affinity are native,
with affinity partly derived. Recording this table would strengthen §3.2.

**N11. NE-3 and NE-5 operational details.**
- "`G` replaced by the identity" (:290) is ambiguous. The zero rule `g ≡ 0` is the free swap, not the identity, and
  a closed ring cannot hold still. Name the ablated rule exactly.
- NE-5's bounded enumeration (PLAN: depth 2, `k ≤ 6`) makes a null result a scoped finite search. Under the
  witness principle it is not an impossibility. §5 should say so beside the §4 paragraph.
- On the triangle, Theorem C covers the affine countercontrols only as class N **with** an NNB-type coupling, since
  the triangle is not bipartite. The offset members 1 and XNOR are covered through the constant-translation clause,
  not as class-N steps (RC3). `Λ_{y,b}` is an H-PREP supply obtained under NNB (PLAN:64-65). State all three in §5.

**N12. Literature (from reviewer knowledge, not fetched).**
- Theorem C(i)–(ii) is the single-qubit case of the knowledge-balance and stabilizer structure of Spekkens' toy
  theory: Spekkens, PRA 75, 032110 (2007); Pusey, Found. Phys. 42, 688 (2012), stabilizer notation, with epistemic
  states uniform on cosets of isotropic subspaces of a symplectic `F_2^{2n}`; Catani and Browne, NJP 19, 073035
  (2017).
- The general epistemically restricted framework is Bartlett, Rudolph and Spekkens, PRA 86, 012103 (2012).
- Its operational counterpart is the Gottesman–Knill fact that stabilizer operations (Clifford unitaries, Pauli
  measurements, adaptive feed-forward, postselection on Pauli outcomes) map stabilizer mixtures to stabilizer
  mixtures.
- `O` is the single-qubit stabilizer polytope. See the magic-state literature: Bravyi and Kitaev, PRA 71, 022316
  (2005); Veitch et al. and Howard–Campbell on magic monotones. In resource-theory language, the S-1 row is "magic
  supplied by the input".
- Prop K is the standard universality fact that the Clifford group together with any non-Clifford single-qubit
  gate is dense. The octahedral group is a maximal finite subgroup of `SO(3)`.
- Lemma R's encoded reflections correspond to the toy theory's transformations that have antiunitary analogues
  (reviewer's recollection of Spekkens 2007). The single-qubit transformation-contextuality context is
  Lillystone–Wallman–Emerson, PRL 122, 140405 (2019), already the QA comparator.
- **What is new beyond that literature.** It is not the confinement theorem. It is the identification of OI's
  supplied interface (P1, P2, H-PREP, N2) and its native symplectic step as the source of the knowledge balance.
  :376-378 says this, and it should stay worded that modestly.
- The pointers were not read first-hand by the writer. A first-hand check should precede any manuscript use.

## Checked and found correct

- Lemmas 1–3 (:141-160).
- The 307 / 43 counts. For the 43: one subspace of dimension 0, nine singular points × 2, six totally singular
  lines × 4.
- `ω(f_a, f_b) = 1`.
- The `Bern(1/5)` example `(3/5, 0, 3/5)`.
- S6's decomposition.
- `rot(Z_+)` `ℓ1 = 31/25` (AP1:911).
- Lemma 5.
- Prop E's mixture argument: the protocol is linear on laws and conditioning reweights components.
- The planted control S4. Two-point supports are cosets with 3-dimensional determined sets, so they are
  non-isotropic and fail NE-1.
- The S7 family facts: eight symmetric `g`, four affine, all bijective.
