# A5-Q3 — amendment A2: the re-review applied (#1049)

**Standing: WIP / UNVERIFIED. Paper-only. Pre-assessment amendment.** No assessment of E1–E3 exists at
this commit or before it.

A2 applies the independent re-review of `../DESIGN.md` at `f71bdc87` together with
`A1-prereg-review.md` at `d7b6d32bb07f19a8fe0141791faa29660a75759f`. That re-review returned ACCEPT
WITH CHANGES, with should-fix items G1–G4 and nits H1–H7. It was relayed by the coordinating session,
and its text is not on `main`.

**Precedence.** A2 governs wherever it differs from `DESIGN.md` or from A1. Sections of A1 that A2
does not amend remain operative. `DESIGN.md` and A1 are unchanged.

**Pin.** `main` at `9c201475ba6fd8f341591d14dd8e88db2e2aaa90`. Every line A2 newly cites was read
there.

***

## G1 — the outcome rests on J1–J5 (amends A1 §4)

**Sets reported.**
- **J₁₋₅ — "independently justified as the extension":** the extensions meeting J1–J5. Only this set
  carries the outcome.
- **J₁₋₄ — "independently justified within its family":** the extensions meeting J1–J4. Reported
  alongside, so that a J5 failure is visible.
- **J₁₋₆ — "adoptable as a premise":** reported alongside, under §A.29 and §A.45 rule 5.

**Outcome on |J₁₋₅|.**
- **(S)** exactly one extension is independently justified as the extension.
- **(M)** more than one is, and the choice stays open. There is no tie-break, and A1 and A2 entries
  are never used to rank.
- **(N)** none is. (N) remains a valid outcome, with the meaning A1 §4 gives it.

The words "the extension" are used only of members of J₁₋₅. The outcome line states, for each
extension, whether it holds J5 and J6.

**J5, restricted motivation.** In J5, "the extension's own stated motivation" means a motivation
located and cited under C1, from a source at the pin or a specified literature item (G4). Text
composed in the assessment is not a motivation for J5. The advance decision on the ∀-quantifier
(A1 §4) is unchanged.

**C-POS.** The baseline's predicted profile (A1 §5.1) puts it in J₁₋₅ and not in J₁₋₆, subject to G4.

***

## G2 — C-CAL replaced (amends A1 §5.1)

**The C-CAL item.** E4 applied to the whole rule: F commutes with the lattice rotations of the cubic
torus, acting on site labels.

**Sources at the pin.**
- Substratum:82: "(E4) **Spatial isotropy.** Observed physics is rotationally invariant; no spatial
  direction is preferred."
- SM:238: "*Spatial isotropy is required for Lorentz invariance:* without rotational symmetry, the
  dynamics has a preferred spatial direction, breaking the isotropy that Lorentz invariance demands."

**Why it suits a calibration.** The item is a statement about the whole rule, M included, so the
functional test does not catch it. Its constraint on b's pattern is recorded in A1 and is not scored.
Its stated motivation is an observational input together with a Lorentz-invariance requirement. As
written, neither presupposes T1, T2 or ¬T.

**Pass and fail.** C2 must classify the item **independent**.
- If C2 returns another class through its definitions, C2 is miscalibrated. No outcome is rendered
  until a disclosed amendment repairs it.
- If the result instead traces to sourcing, for example a reading of the source in dispute, C-CAL is
  **not evaluable** and is replaced by amendment. That does not void C2.

The A4-based item of A1 §5.1 is withdrawn as C-CAL. Its source's grammatical referent is A4's second
sense (Substratum:98), and its exact-commutation form strengthens A4's "up to gauge".

***

## G3 — the exemption narrowed, and a law-phrased countercontrol (amends A1 §3 C2 and §5.4)

**Narrowed exemption.** The functional test exempts a law for how the offset transforms only in three
cases:
- (i) the offset is acted on by the extension's own transformation class, by g itself;
- (ii) the law is induced by the extension's stated transport of its data, as E2's link transport
  induces a law on b;
- (iii) the law is trivial.

Any other action on b alone is treated as a stipulation on the offset for the functional test. It is
target-defined if it has no stated effect outside the offset sector, whatever reason is given, and
whether it removes or keeps an effect of the offset.

The mandatory B1 rows of A1 §3 fall under (i)–(iii): E3 under (i), E2 under (ii) and E1 under (iii).
E3's other representations, listed in A1 §2, fall outside the exemption.

**Third countercontrol, E☆-law.**
- **Setting:** the lift V_K = V_3 ⊕ V_2 ⊕ V_1, with E3's data and covariance and the transformation
  class ι → G_0, the site-wise block-diagonal unitaries.
- **Added stipulation:** the offset transforms by ρ(A, B, z) = (A, B, 1). The configuration
  transforms by g itself.
- **Offered justification:** "offsets carry no singlet charge."

**Required rejection.** E☆-law must be rejected through J3 by the added stipulation:
- ρ is none of (i)–(iii);
- its statement acts on b alone and has no stated effect outside the offset sector.

If this does not happen, the rule is void and no outcome is rendered (A1 §5.5, I8). The expected C1
result, no source at the pin for the offered reason, is an expectation and not the required route.

**C-LIN for E☆-law.** C-LIN is evaluated against E3 and `A6Cov` stated on the same class ι → G_0. A
C-LIN result produced only by restricting the class is not counted, and it is not a rejection reason
for I8.

***

## G4 — literature-only support for J3 (amends A1 §3 C1 and C3, §4 and §5.1)

**Corpus first.** No [L] item may be used for C1 until the C3 search has covered the corpus for an
internal motivation, and the record lists the locations. For any A6-type covariance assumption the
search includes at least:
- SM:104, the contrast with general relativity, which that line assigns to a different principle;
- the name and wording of Substratum:102;
- Main:726 item (xii), "fixes the interface through which the gauge symmetry is read locally";
- SM:114–118.

**Specified citations.** Every [L] citation names the work and the specific claim it is cited for.
For the C-POS prediction these are:
- C. N. Yang and R. L. Mills, *Phys. Rev.* 96, 191 (1954), for the claim that invariance under
  position-dependent internal rotations requires a compensating field with an inhomogeneous
  transformation law;
- K. G. Wilson, *Phys. Rev. D* 10, 2445 (1974), for the claim that on a lattice the link variable
  transforms as U(n, μ) → g(n) U(n, μ) g(n + μ)⁻¹.

Both are [L]: from memory, not re-read.

**Labelling.** A J3 classification that rests on [L] alone is labelled "J3 ([L] only)", in the
per-candidate verdict and in the outcome line. Such a classification counts as held. The outcome line
also states the count of J₁₋₅ with [L]-only passes excluded. The same standard applies to the
baseline, to E1–E3 and to the countercontrols.

**C-POS prediction, restated.** J3 is predicted held, through a mixed classification. Its independent
component is labelled "[L] only" unless the corpus search finds an internal motivation.

***

## Nits

- **H1.** The grade "out of scope" is reserved for the D1 sentences pre-graded in A1 §3. Every other
  D1 source is graded consistent, tension or inconsistent, as `DESIGN.md` §3 defines them.
- **H2.** The E1 cell in the transformation-class row of A1 §3's B2 table reads: "quantified over all
  g; b not transported".
- **H3.** The "Boundary for the unit" sentence of #1049 c.6719886996 is attributed to the coordinating
  session's text in the owner-account comment, not to owner speech. The owner's own words in that
  comment are the blockquote. A3's boundary rests on that sentence, attributed this way, and on the
  owner's "O5 and the proposed downstream A5 record changes remain unapproved".
- **H4.** The C-TI table of A1 §5.3 gains three rows:
  - J5's advance decision that the ∀-quantifier selects E1 over E1′. It is source-based (`A6Cov`) and
    is recorded as correlating with T1 (b = 0 against no constraint). It applies the same rule to
    every extension's quantifier domain;
  - G3's narrowed exemption, applied symmetrically to laws that remove or keep an effect of the
    offset;
  - E☆-law, as a countercontrol.
- **H5.** A1 §2's "E2 ↔ E3" line, that E2 induces b ↦ g_i b_i, is labelled [D], to be re-derived in the
  assessment. The preregistration states it as no result.
- **H6.** In E☆'s expected rejection (A1 §5.4), "C1 finds no source at the pin" is an expectation, not
  the required route. A near-source on the lift is amplitude-scale gauge (Substratum:270; Substratum:163,
  "removes only the common overall phase"). The required route is the functional test.
- **H7.** In A1 §3's B2 table, `V →+ V` row: `linkSubstratum_A5` is A6Instantiation.lean:147.

***

## Invariants (amends A1 §6)

- **I1** is re-measured on this commit. It adds only `A2-rereview.md`, its parent is `d7b6d32b`, and
  no assessment file exists in its tree.
- **I2** extends to A2. At checkpoint 2, `git diff <A2> <head>` over `DESIGN.md`, A1 and A2 is empty.
- **I8** extends to E☆-law.
- **I9** reads "outcome on |J₁₋₅|", with J₁₋₄ and J₁₋₆ reported.
- **I16** reports C-CAL's E4 item.
- **New I18.** Every J3 pass that rests on [L] alone is labelled, and its C3 corpus search is recorded
  first. The reviewer checks each [L] entry for the named work and claim.

***

## §7 additions (amends A1 §7)

| Reference | Used for | Classification |
|---|---|---|
| Re-review of `d7b6d32b` | the items applied here | provenance. Each change is stated here in full |
| #1049 c.6719886996, "Boundary for the unit" | A3 | support, by quotation, attributed as in H3 |
