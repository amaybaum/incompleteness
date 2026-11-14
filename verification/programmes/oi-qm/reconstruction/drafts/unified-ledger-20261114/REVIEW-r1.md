# Independent review of LEDGER-r1 and NOTES-r1

Read-only, paper-only, non-author review under the authorization on #914 (comment 6877420015).
Sources read at `c3b5f37a`. `git diff --stat c3b5f37a dfeec843` (after fetching `main` by name)
lists `AGENTS.md` only, so every `papers/`, `book/` and `verification/` line cited below holds at
`dfeec843`. No file was edited, no computation was run, nothing was posted.

## Verdict: REVISE

Most statuses match their sources. Four findings are blocking:

- B1. The black-hole "no instance" is stated more widely than GR Appendix A proves.
- B2. The negative claim that no extension E is stated in the corpus fails a corpus-wide search.
- B3. The paper-level results on `main` that bear most directly on QM and on A5 are missing. These
  include the OA-1, OA-2 and OA-3 records landed in `c3b5f37a` itself.
- B4. One joint-satisfiability cell is marked "undetermined" although a stated result settles it
  for one fixed finite carrier.

No branch is a unified physical derivation, and the ledger is neutral. Each correction below is a
text replacement. B2 and B3 also need the listed records read.

## Blocking

**B1. Black-hole information: "no instance" is wider than the proof.**
Location: LEDGER:31 (Status and Part 4 class cells), :280, :286, :294, :302.
Sources: `papers/GR.md`:605, 805, 815, 823–827, 839; `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:3, 14, 16, 18;
`book/appendix-a-prediction-status.md`:102, 111; #914 comment 6875046763 ("the existing
configuration-level no-go result must not be mistaken for a no-go covering every possible observer
interface").

What is proved, on paper (GR:813–823) and exactly for every bijection (BH-02 C1, C6(a)): suppose
the initial conditions counted are definite configurations of Σ_E and B|R is aligned with the
configuration coordinates. Then every state on every orbit is a product state and S(ρ_R) = 0, so
H-scramble fails in that setting and Theorems A.8–A.9 as stated have no instance. This does not
use finiteness: it holds because a bijection maps configurations to configurations.

What is not ruled out:
- an initial superposition. The aligned-cut entropy is bounded by H(p₀) (GR:825–827), and the
  source names this route as open (GR:815, 827, 839).
- a non-aligned bipartition (GR:815).
- an ensemble restatement of A.8 (GR:827, "not given here").
- the proper-shell case (GR:829).

BH-02 C3 is a scoped counterexample to "permutation dynamics cannot produce Page-like
entanglement". From a supplied superposition |−⟩|+⟩⁷, 193 of 200 random permutations give
Page-like states at every cut. This is numerical, uses an analyst-supplied state, is not an OI
mechanism and is not a derivation of H-scramble. Appendix-a:111 records G11 as an open target,
with "a non-vacuous version needs a specified initial ensemble or a non-aligned bipartition". The
ledger does not cite C3.

Replacements:
- LEDGER:31, status cell: "Conservation by premise (A2). H-scramble fails for every bijection in
  the setting Theorems A.8–A.9 count: definite initial configurations, bipartition aligned with
  the configuration coordinates (paper proof GR:813–823; exact, BH-02 C1 and C6(a)). In that
  setting the theorems as stated have no instance. Outside it (initial superposition, non-aligned
  bipartition, proper shell) the Page curve is open (GR:815, 827–829; G11 open). GSL open."
- LEDGER:31, Part 4 cell: "Open (G11 open; no instance in the counted setting)".
- LEDGER:286, replace "(refuted in its counted setting; untested otherwise)" with "(fails for every
  bijection in its counted setting; open outside it. BH-02 C3, numerical and exploratory, gives
  Page-like states from a supplied superposition under random permutations; this is not an OI
  mechanism.)"
- LEDGER:294, replace the first sentence with "H-scramble fails, for every bijection, on definite
  initial configurations at aligned bipartitions (proved). The failure comes from configurations
  being mapped to configurations, not from finiteness of the orbit. Finiteness enters only through
  A.8's cycle-average bookkeeping."
- LEDGER:280: after "(C2 there)" add "; from a supplied superposition, random permutations give
  Page-like states (C3 there, numerical, scoped). BH-02 is exploratory research, internally
  reviewed, not adopted (REPORT:3). C1's exhaustive check covers (q,n) = (2,2), (2,3), (3,2) and
  500 sampled permutations at (2,4); the general statement is the paper proof."

**B2. The negative claim "No common extension E and no sector condition C is stated anywhere in the corpus" is too wide.**
Location: LEDGER:58–60 and :84 ("Sector condition C and access closure: not stated in the corpus");
NOTES:72–73.
Sources:
- `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`:54, 69, 73. This is the
  Gate A endpoint contract on `main`: an E-indexed two-direction target, recorded as "proposed
  obligations, not proved statements".
- `.../oi-qm-ext-1/whole-model-bridge.md`:11–19, 23. Candidate extension E-AR is stated
  clause by clause. Its first state/readout bridge fails on every fixed finite-dimensional carrier.
  This is a hand proof scoped to that one added-access extension, "not a no-go for bare OI".
- `.../oi-qm-ext-1/README.md`:30–43, which gives the status of eighteen scoped records.
- `.../native-y-continuation-20261024/EQUIVALENCE-OBLIGATIONS.md`:73, which carries "composed
  observer-access closure" as an obligation label only.

The search behind the claim covered `papers/`, `book/` and one PROGRAMME file (LEDGER:59). It
did not cover `verification/programmes/oi-qm/reconstruction/` (§A.19).

Replacement for LEDGER:58–60:
"No extension E and no sector condition C is adopted. On `main`, the Gate A endpoint contract
states the E-indexed target as proposed obligations (`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`:54–69).
One candidate extension, E-AR, is stated, and its first state/readout bridge fails on every fixed
finite carrier (`.../whole-model-bridge.md`:11–19). That is a paper result scoped to that
candidate, with its scoped review recorded on PR #1173 (provenance). No sector condition C and no
access-closure condition is stated on `main`. 'Composed observer-access closure' appears only as
an obligation label (`.../EQUIVALENCE-OBLIGATIONS.md`:73)."

Make the matching change to NOTES:72–73 and add the four files to "Read".

**B3. Paper-level results on `main` that bear on QM and on A5 are missing.**
Location: §2.1 (LEDGER:63–75), §2.4 (:86), §9 row QM–SM (:312), M4 (:344), M9 (:349), §4.3 (:152).
Sources (each is a paper-level, agent-reviewed research record. None is adopted or kernel-checked,
and none is established under §A.46 items 1 and 7):
- OA-1 (`verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`:48, 58). For OI's
  gauge-derived affine rule class, a stored setting acts on a carrier only by translation, under
  every measure. Fredkin bijections supply control, so this gap is specific to the affine class.
  The configuration-level interface is capped for every rule [K]. Operations beyond it are open.
- OA-2 (`.../oa-2-20261112/STATUS.md`:56, 62). Theorem C: at a fixed finite carrier, reversible
  emergent operations form a finite group. Theorem E(b): for the affine class, under (H1), H-AR,
  (H3), (H4), (SP) and ledger item (xiv), the prepare–measure fragment is simplex-embeddable.
  Non-affine rules are open.
- OA-3 (`.../oa-3-20261112/STATUS.md`:55, 71). In SM's ring rule G_SM, under the stated observer,
  horizon and (PT) conditions, the prepare–measure fragment is a simplex. Verdict "OPEN, narrowed";
  this is not an impossibility result.
- W1-1 (`verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:48, 60, 66, 72). W1,
  the shell entropy–energy slope that H-count implies at GR:58, is an additional assumption. None
  of the tested mechanisms derives it. The one distinct route fails in the real lift of the linear
  rule. The ħ condition lists and Main's posit ledger do not carry the conserved real-valued energy
  shell (W1-0).

These records put A5 in tension with the QM branch as well as the Bell branch, under named
hypotheses and at paper level. The ledger currently lists only Bell and SM-geometry conflicts.

Replacements:
- §9 QM–SM row (LEDGER:312), reason cell: "SM uses QM as input (`papers/SM.md`:22;
  `papers/Substratum.md`:76, 123), a stated dependence, not a conflict. Separately, under A5's
  affine class and named observer hypotheses, the prepare–measure fragment is simplex-embeddable
  (OA-2 Theorem E(b)), and so is G_SM's under OA-3's conditions. A stored setting acts only by
  translation (OA-1 Gap 2). These are paper-level, not established (§A.46 item 7), and conditional
  on the listed hypotheses."
- §2.1: add the bullet "Research records on `main` (paper-level, agent-reviewed, not adopted): OA-1
  (classical-control gap specific to the affine class; configuration-level interface capped [K]),
  OA-2 (Theorem C; Theorem E(b) for the affine class under (H1), H-AR, (H3), (H4), (SP), (xiv)),
  OA-3 (G_SM simplex under its conditions; open otherwise). The Gate A records under
  `oi-qm-ext-1/` give candidate-specific obstructions and source stops (README:30–43)."
- M4 (LEDGER:344), Corpus statement column: add "affine-class results OA-1 Gap 2, OA-2 Theorem E(b)
  (paper-level)". Branches blocked: see S6.
- M9 (LEDGER:349): add "W1 an additional assumption; W1-0 not carried by the ħ condition lists
  (W1-1 STATUS:48, 72)".
- §4.3 (LEDGER:152): after "H-slope and H-count are selection conditions …" add "; W1, implied by
  H-count in GR:58's setting, is an additional assumption on the paper-level W1-1 record".

Under §A.42 item 8, the review links these records carry (PR #1173 and #1265 comments) are
provenance. The records and their proofs are on `main`.

**B4. Exact QM inclusion against A1 is settled for one fixed finite carrier, not undetermined.**
Location: §9 QM–BH (LEDGER:315); §2.5 (:90–92); M5 (:345).
Sources: `papers/Main.md`:558 (the classical-dimension Proposition: "no fixed finite realization is
exactly operationally equivalent to even a single qubit's full theory". The factorization half is
proved there and the unboundedness is imported from [55]); `papers/Substratum.md`:92 (A1 "remains
the finite-carrier premise for the recurrence arguments"); `papers/GR.md`:585 (only C_V and the
causal-cone sector need be finite on accessible timescales); #914 comment 6875046763 (the target
"cannot assume one fixed finite total carrier").

The conflict holds for exact inclusion on one finite S under the preparation → ontic → measurement
factorization interface. It is a proved conflict conditional on that interface and on the imported
unboundedness result. It is not an inference.

Replacements:
- QM–BH cell: "known not to, for exact inclusion on one fixed finite S under the factorization
  interface of `papers/Main.md`:558. Undetermined on a completion, where A.8's finite cycle
  decomposition would need a counterpart (not stated)."
- Add the §9 row "QM–A1 | exact inclusion (target) | A1 as stated | known not to, on one fixed finite
  carrier, under the factorization interface | `papers/Main.md`:558; `papers/Substratum.md`:92;
  the owner record already excludes one fixed finite total carrier".

## Should-fix

**S1. Bell–SM row: state every condition of the conflict.**
Location: LEDGER:317 and :124.
Sources: `papers/Main.md`:362, 412, 414, 724 (x); `papers/Substratum.md`:131, 171.

Exact algebra (Main:362) makes global A5 inconsistent with the adopted implementation:
preparation-indexed edges are dependences present at some states and absent at others (Main:414).
Main:412 also names "an equivalent nonlocal response map". Main:414 does not say that this
alternative leaves (vii).

Against E2 itself, the Bell–lattice Corollary excludes CHSH > 2 under global A5 together with
(viii), (x) and (xiv) and the Corollary's intervention and readout conditions, and only for wings
outside the graph cone. Wings inside the graph cone, including wings spacelike to a wave-speed
cone, are outside it (Main:414).

The nearest-neighbour premise (x) is itself scoped to the reference vacuum/uniform class (Main:724),
and Stage 2's result to the "geometric reference class" (Substratum:171). No source scopes A5 that
way.

Replacement for the Bell–SM cell: "known not to, for global A5 with the preparation-indexed
adjacency route (exact algebra, Main:362, 414). Under global A5 with (viii), (x), (xiv) and the
Corollary's conditions, CHSH ≤ 2 for wings outside the graph cone. Wings inside the graph cone are
not covered. For the 'equivalent response map' alternative the status relative to (vii) is not
stated. With A5 restricted to the reference class: undetermined. (x) and Stage 2 are scoped to the
reference class (Main:724; Substratum:171); A5 is not."

**S2. GR–SM row: the stated conflict sits within SM.**
Location: LEDGER:321.
Sources: `papers/SM.md`:104, 144, 158.

The incompatibility is between SM §3.1's dynamical-geometry principle (the graph G(v) evolves with
the state; SM:158) and global A5 (SM:104). It is not between GR's premises (geometry-first
ordering, harmonic boundary modes) and A5. SM §3.1's discrete Einstein equation is a target form
whose curvature step is open (SM:144).

Replacement: rename the row "SM §3.1 (graph geometry route to GR)–SM Stage 2(b)". Premises A: "G(x)
varying with the state (SM:104, 158; Einstein step a target form, SM:144)". Premises B: "global
A5". Status: "known not to, for global A5 (exact algebra, Main:362; SM:104)". Then add a separate
row, "GR (geometry-first)–SM | geometry-first ordering | A5 | undetermined | no shared premise in
conflict traced".

**S3. D4 omits the strongest instance.**
Location: LEDGER:356.
Sources: `papers/Substratum.md`:131–133, 171, 193.

Theorem 23 assumes A1–A6, A5 included, and states the Bell-inclusive completion "only conditional on
H-Bell" (Substratum:193). H-Bell's clauses (i)–(iii) (:133) do not mention leaving A5. Main:414
places that completion's update outside (vii).

Append to D4: "Theorem 23 (`papers/Substratum.md`:193) takes A1–A6 and makes the Bell-inclusive
completion conditional on H-Bell alone. Its preparation-indexed implementation (:131) is outside
(vii) by `papers/Main.md`:414."

**S4. The SM gauge-group classification omits the two-direction selection.**
Location: LEDGER:28 and :208.
Source: `papers/SM.md`:1424 ("the Standard Model from a cubic lattice" and "the lattice is cubic
because SU(3) is observed" are "the same fact stated in two directions"); SM:390 (Theorem 7b).

Replacement for :208, first clause: "Gauge group: C (H-link, H-cust) given the cubic-lattice
commitment. That commitment is selected by the observed gauge group (Theorem 7b; SM:1424), so as a
forward derivation from the model the gauge group is an empirical input (E). Layer 0."

**S5. QM: scope and the sharper sourcing targets.**
Location: LEDGER:25, 69, 79–88.
Sources:
- `papers/Main.md`:80 and 588: `substratumGen_not_control` is stated on the two-state carrier, and
  `verification/lean-mathlib/OIBridge/StructuralClosure.lean` states it at `Fin 2`.
- `papers/Main.md`:18 and 554: the Born exponent is not selected (a "frontier item").
- `verification/lean-manuscript-census.json`, kernel-only families at lines 643, 652, 661 and 679:
  - coherent-continuum source: a necessary condition of uncountably many non-monomial rays;
  - real pair-flow reduction: any continuous one-parameter real orthogonal pair action supplies the
    mixing datum;
  - discrete completion: one fixed gate at an irrational angle gives dense unitary control.

Replacements:
- At :69, after `substratumGen_not_control` add "(on the two-state carrier)". Make the same addition
  at :25.
- §2.3: add "Born exponent: not selected by the equivalence (Main:18, 554)."
- §2.4: append "Kernel-only reductions narrow the target. For exactness, a continuous one-parameter
  real orthogonal action on one pair suffices with the stated closure (census family 'real
  pair-flow reduction'). Uncountably many non-monomial rays are necessary (census family
  'coherent-continuum source'). For density only, one fixed gate at an irrational angle suffices
  (census family 'discrete completion'). None of these is carried by a manuscript."

**S6. Several 'Branches blocked' entries have no source.**
Location: LEDGER:342 (M2), 344 (M4), 345 (M5), 348 (M8).

No source states that BH needs tunable mixing (M2). Its stated need is a preparation or a
non-aligned partition (GR:815), which is M3. M4 blocks Bell (Main:414) and the SM §3.1 geometry
route (SM:104). For QM and BH no source makes the update outside A5 a requirement: SM:294 and
Main:724 (v) record a non-ergodicity tension, not a requirement. OA-1 and OA-2 (B3) are affine-class
obstructions, not statements that a nonlinear update is needed. M5 for GR conflates the operational
completion of Main:356 and 558 with the continuum limit of G3 (GR:12). For M8, the cosmology chain
uses horizon thermodynamics, not graph curvature (GR:422–426, 466).

Replacement: mark these entries "(inference, not stated at source)" or remove them. That is: M2 BH;
M4 QM and BH; M5 GR; M8 Cosmology.

**S7. Bell classification.**
Location: LEDGER:26 and :131.
Sources: `papers/Main.md`:360, 427; `papers/Substratum.md`:133.

In the common SM/GR model, no reconstruction of quantum CHSH values exists beyond H-Bell. H-Bell's
clause (i) is the required dependence itself. The abstract response-table construction realizes
quantum and PR-box laws alike.

Replacement for the Part 4 cell: "Open in the common model (H-Bell (i) is the required dependence).
In the abstract class, response-table realizations of quantum and supraquantum laws exist (Main:360,
427)."

**S8. A5 entry.**
Location: LEDGER:47.
Source: `papers/Substratum.md`:100; `papers/Main.md`:724 (vii).

Replace "affine part derived from amplitude-scale gauge (SM §4.1)" with "affine part necessary given
amplitude-scale gauge invariance, itself assumed (its derivation from the q-size gauge freedom is an
open step); the restriction to linear is imposed".

**S9. SM first missing step and weakest link disagree within the ledger.**
Location: LEDGER:28 compared with :188 and :198.

The table names H-link and H-χ′. §5.4 places the observer-level lift (SM:232) before them, and
§5.2 gives the weakest link in a different order. Make the table and §5.4 the same, using §5.4's
wording.

**S10. Owner questions already partly answered by recorded decisions.**
Location: LEDGER:362, 366, 368, 370.
Sources: #914 comments 6875046763, 6875548603 and 6877420015; #1169 comment 6876591512.

- Q5. "Cannot assume one fixed finite total carrier", and "arbitrarily large finite carriers" in
  #1169 answer 3. Replacement: "**Carrier.** The recorded target excludes one fixed finite total
  carrier (6875046763) and requires arbitrarily large finite carriers (#1169, answer 3). Which
  finite-carrier results (recurrence, P-indivisibility at GR:585, A.8's cycle averages) must be
  restated on the admitted carrier?"
- Q7. Exclusion of supraquantum correlations in the physical sector is decided (6875046763
  decision 3; 6875548603; #1169 answer 4 on access closure). Replacement: "**Bell sector.** Is H-Bell
  (no-signalling, continuum curvature) the route by which C's recorded exclusion of supraquantum
  correlations is to be met, or is that exclusion to be stated on C directly?"
- Q9. Part 4 states that a conditional reconstruction "does not discharge the ultimate derivation
  obligation" and is "valid scientific progress" (6877420015). Replacement: "**QM as input to SM.**
  Part 4 already treats the reverse reconstruction as progress that does not discharge the
  obligation. Is the forward SM trace (#1211) to be ordered before or after the QM sector work?"
- Q1. Add: "The recorded target already requires one compatible interface (6875046763)."

Missing question: "What standard of independent physical justification does Part 4 apply to named
hypotheses that a source records as additional assumptions (for example W1 and H-count, H-slope,
H-scramble)?" The sources are W1-1 STATUS:48 and GR:58, 74, 815.

## Nits

- N1. LEDGER:138 cites `papers/GR.md`:536–545 for "fixes only ε/√σ". The source is GR:306 and :547.
- N2. D2 (LEDGER:354): SM:14 and SM:60 also cite [Substratum §3.3]. Add them.
- N3. D3 (LEDGER:355) is not a disagreement. Both sites carry the statement, and
  `papers/Substratum.md`:373 cites both. Reclassify D3 as "dual citation, consistent", or drop it
  and update Q11's "D1–D5".
- N4. D1 (LEDGER:353): ch19:22 itself names an unresolved entry and split-status entries. The
  disagreement is the heading at :20 against the entries.
- N5. D5 (LEDGER:357): step (i)'s T_cl rests on H-count (GR:58, 422). Add it.
- N6. LEDGER:52: the census note on "manuscript axioms A1-A6" records A1 and A2 as formalization
  gaps at the substratum level as well (absent an identification map), with realized-core images.
- N7. NOTES:8–9: the diff also rewords §A.46's opening paragraph and its adoption line.
- N8. §7.7 (LEDGER:272): appendix-a:109 gives G8 (ν) Layer 2(a). §7.6: add GR:412 (iii), where a
  high-confidence phantom crossing falsifies at structural level.
- N9. §2.1 (LEDGER:71): the classical-dimension Proposition proves its factorization half and
  imports the unboundedness from [55] (Main:558). The SIC remark is certified exactly over ℚ(√3)
  (Main:560).
- N10. §6.7 (LEDGER:239): GR:352's condition is the selection between two completions that share
  substratum, partition, transition law and calibration. Stating this makes clear what the CR's
  condition carries.

## Item-by-item answers

1. **Statuses.** These match their sources: QM, GR, cosmology (Type II "a structural reading, not a
   derived law", GR:12, 26; budget "partly definitional", GR:452, 541; factor 1/6 imported, GR:466,
   474–478; first missing step GR:382–386), SM (Theorem 7 kernel `theorem_7`, H-link and H-cust
   SM:374, Theorem 7b SM:390, d = 3 SM:30 and 1424), and CC (GR:352, 356, 362). The exceptions are
   B1, B4, S1, S4, S7, S8, N6, N8 and N9. Every Lean identifier cited is declared in the named
   module.
2. **Strongest claims.** BH: see B1. Cosmology: confirmed. SM: confirmed, with S4. QM: kernel scope
   as in S5; the first missing step is right, with S5's reductions. GR and CC: G3 is the first
   missing step for both (GR:12, 162, 352).
3. **Conflicts.**
   - Bell–SM: a proved conflict for the preparation-indexed route under global A5; conditions as in
     S1.
   - GR–SM: an SM-internal proved conflict under global A5 (S2).
   - Scrambling against configurations: a failure of H-scramble in its own counted setting, not a
     conflict with finiteness (B1).
   - Exact inclusion against A1: a proved conflict on one fixed finite carrier (B4).
   - SM taking QM as input: a stated dependence (B3).
4. **"Not traced" items.**
   - No CHSH or Bell-ceiling declaration in `.lean` files. Confirmed.
   - No kernel pointer for the classical-dimension Proposition or the uniform-continuum theorem.
     Confirmed; the probe checks only (Main:560, 596).
   - The book chapters carry the preparation-indexed route (ch00:55, ch01:171, ch03:180–186,
     ch04:92, ch18:102) without the condition "outside (vii)". Confirmed.
   - No source restricts A5 to a reference class. (x) and Stage 2 are so restricted (S1).
   - C and access closure are not stated. E is stated as a slot and as candidate E-AR (B2).
5. **D1–D6.** All present at both locations. D3 is not a content disagreement (N3). D2, D4 and D5
   are incomplete (N2, S3, N5).
6. **Mechanisms.** All nine are named in the corpus as missing or open. Some blocked-branch
   assignments are inferences (S6).
7. **Classification.** No branch is a unified physical derivation. Corrections: BH (B1), Bell (S7),
   SM gauge group (S4).
8. **Owner questions.** Q5, Q7 and Q9 are largely answered by recorded decisions, and Q1 partly
   (S10). Q2, Q3, Q4, Q6, Q8, Q10 and Q11 are open and distinct. One question is missing (S10).
9. **Neutrality.** No research direction is recommended, there is no truth assessment, and no tier,
   readiness or authorization change is proposed. Passes.

## Checked by the reviewer

- **Owner records.** #914 comments 6875046763, 6875548603 and 6877420015, and #1169 comment
  6876591512, read through the API.
- **Diff.** `c3b5f37a..dfeec843`.
- **`papers/GR.md`.** Lines 12, 26, 40–60, 88, 162, 212–216, 256, 306, 328, 340–362, 374–412,
  418–486, 510, 524–547, 585, 591–605, 783–863.
- **`papers/Main.md`.** Lines 14–20, 80, 97, 356–427, 554–598, 718–726.
- **`papers/SM.md`.** Lines 12–32, 104, 140–166, 220–232, 294, 374, 390, 543, 589, 655, 669,
  1316–1322, 1422–1428.
- **`papers/Substratum.md`.** Lines 76–102, 123, 131–135, 157–171, 181, 193, and the heading lines.
- **`papers/Introduction.md`.** Lines 145, 169, 181.
- **`book/`.** `appendix-a-prediction-status.md` lines 60–120. `ch19-open-problems.md` lines 20–22,
  72, 178, 224 and the framework-status lines. The Page-curve and preparation-indexed passages
  across the chapters and FULL, by search.
- **BH records.** `black-hole-information/PROGRAMME.md` and the BH-02 REPORT in full.
- **Other verification records.**
  - The H-D A5 result, lines 640–700.
  - The C4-1 result, lines 30–45.
  - The OA-1, OA-2, OA-3 and W1-1 STATUS files.
  - `oi-qm-ext-1/README.md`, `endpoints.md` lines 1–72, and `whole-model-bridge.md` lines 1–45.
  - The H-Bell round directory, which holds a preregistration only.
- **Census.** The registry families named above.
- **Lean.** Declarations of the 17 identifiers the ledger cites. The statements of
  `substratumGen_not_control`, `substratum_plus_control_qm` and
  `qm_generated_by_substratum_extension`; the last is witnessed by the full class. Searches for
  CHSH, Bell, nonnegative rank and gluing in the `.lean` files.
- **Corpus searches.** "reference state class", "access closure", "sector condition", "extension E",
  "Type II", "Page curve" and "H-scramble".
- **Not done.** No Lean build, no script run, and no reading of PR #1289 or of other off-`main`
  drafts.
