# Independent re-review: QPHEN Phase 1 r2 (#1210)

**Verdict: REVISE.** The scope of the remaining fixes is narrow.

- **r1 findings.** All r1 blockers and nits are fixed in substance, with one exception: the new A6.1 proof (B1's fix)
  is unsound as worded.
- **Proofs.**
  - A3.1(c) is sound.
  - A6.1 has an exact counterexample under its literal hypotheses. Under one tightened hypothesis, given below, its
    proof sketch is sound.
- **AW-QX4-1** stays a marker in QX4. SHARED cites it in a way that reads as support for SA-1(c).
- **The owner's four added requirements** are not yet met.
  - (1) The GHZ formulations are not named precisely enough.
  - (2) The Leggett–Garg wording calls `K₃ = 2` "supra-quantum" and "QM-incompatible" without naming the protocol
    class. This error came from my r1 review (B5), and I correct it here.
  - (3) There is no explicit proved / disproved / open ledger.
  - (4) T9 and the M3 cell lean on agreement with QM to support SA-1(c).
- **New in r2.** One new false statement appears in R4.9, and two stated hypotheses were dropped without a
  corresponding finding.

**Blockers** R2-B1 to R2-B6 and **nits** R2-N1 to R2-N7 are given at the end. Each owner requirement has its own
section, as the coordinator asked.

## Standing

- **Reviewer.** The same independent subagent as r1. Read-only. The writes are this file and probe P4. There were no
  repository or GitHub writes and no dispatch; reads used `gh api` only.
- **Files reviewed** (sha256 verified on read):

  | file | r2 sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `26ba2167813887e9d6cca63e90667659a88a56365ce21f3ac319b638c8bfe615` |
  | `QX4-INCOMPATIBILITY-LG.md` | `47fb4202049efb49a8cd9c471632d06aba74866e4b80f895ab0512c1cd45f975` |
  | `QX6-BELL-CHSH.md` | `9d68526ce41cd8fedf249fd3d4e377ef54f6de4679a6b884fcd6a9fe1805a875` |
  | `SHARED-MECHANISM.md` | `7d10092a5c860123ab6902feeed1857ec07e8613b3b5e714478e0d959f408553` |
  | `DISPOSITIONS-r2.md` | `064df364a51fda7f2256705cd9f1978b1eec44152f1c09587d7104bfddf3cb53` |

- **The r1 copies** under `r1/` are byte-identical to the files reviewed in r1 (`23775ceb…`, `6edcf8fa…`,
  `1534b2c2…`, `5b07a5b9…`).
- **The D18 decision is verified at its source.** #1169 c.6735014875 is by amaybaum, created 2026-11-09T07:52:50Z.
  The D18, D15 and D4 quotes in r2 match it verbatim. As directed, N8's "decided" is treated as correct.
- **Probe P4**, `review/probes/p4_r2_checks.py`, sha256
  `2e7c2de93b9a9919091acde1ee1c7b0555d5f713df0466474e47eb78ec15eff8`. It runs under `python3 -I` with exact integer
  arithmetic. It checks generic objects only and builds no OI apparatus. Its output:
  - **(1)** A one-tick composite map `op_A ∘ φ ∘ op_B` that is bijective for every setting. In the dependency graph
    `G`, `R_A` is at distance 1 from B's region, and the correlators are `(1, 1, 1, −1)`, so `S = 4`. The map's
    components outside B's region depend on `b`.
  - **(2)** The copy coupling `m ← m + c` and the reciprocal CNOT are affine. The occupation-conditional kick
    `x ← x + c·m′` is not.
  - **(3)** On `(|000⟩ + |111⟩)/√2`, `⟨XXX⟩ = +1` and `⟨XYY⟩ = ⟨YXY⟩ = ⟨YYX⟩ = −1`, so Mermin's
    `XXX − XYY − YXY − YYX = 4`. Also `⟨ZZZ⟩ = 0`.
- **The r1 probes P1–P3** are unchanged (`af34edb8…`, `312620b0…`, `82d2099c…`).

## 1. Were the r1 findings fixed in substance?

| finding | status in r2 | note |
| --- | --- | --- |
| B1 (Main §3.3's reach) | **partly** | Main's literal hypotheses are now quoted, the `⊥ ↦ +1` rule is declared, and the conclusion is narrowed. But the new A6.1 fails as worded (R2-B1) |
| B2 (routing) | fixed | `NCONS_ready` and `NCONS_global` are separated, and A3.1(b)–(d) are correct. R4.9 adds a new false sentence (R2-B6) |
| B3 (GHZ) | fixed in substance | the conventional state is not named precisely (owner requirement 1, R2-B4) |
| B4 (A4.4's hypotheses) | fixed | (H1)–(H4) are stated, and ABL-T1 is added |
| B5 (A4.1's scope) | fixed in scope | the wording "supra-quantum" and "QM-incompatible" must be corrected (owner requirement 2, R2-B2). It came from my r1 text |
| N1–N6, N8–N14 | fixed | N8 was verified against c.6735014875 |
| N7 | fixed | the tables trace Issue comments, OICORE-1, `DECISIONS.md`, the NR items and the reviewer probes, each with a classification |

**Changes beyond the findings.** `DISPOSITIONS-r2.md` states that nothing else changed. That is not accurate:
- QX4 R4.9 gains a new claim, which is false (R2-B6).
- QX6 §3 drops two hypotheses from the records it summarizes (R2-N2, R2-N3).
- QX6's old Q6-4 is renumbered Q6-5 (R2-N4).
- Much of the prose is restyled into bullets, with no change of content that I found.
- Two additions are accurate and acceptable: SHARED M8 (D15(a) typed CS) and M11 (D4(a)'s quote). Both come from
  c.6735014875.

## 2. Soundness of the new paper proofs

**QX3 A3.1(c): sound.**
- If `T(y) = My + b` preserves Hamming weight everywhere, then `T(0) = 0`, so `b = 0`.
- Each `Me_i` has weight 1, and `M` is invertible, so `M` is a permutation matrix.
- A coordinate permutation sends the excitation's cell to a fixed cell, whatever the unknown bit, so it cannot route.
  P2's count, 6 such bijections on `F_2³`, agrees.
- The same conclusion holds if only the field cells' weight is required to be conserved on all inputs. With `c = 0`,
  the term `s·u` must vanish for both values of `s`. The writer may add this, but need not.

**QX6 A6.1: the proof sketch is sound only under a tighter hypothesis. It is false as worded (R2-B1).**
- **The counterexample (P4(1)).** A tick map `op_A ∘ φ ∘ op_B` satisfies every stated hypothesis:
  - (D): it is a bijection with its dependency graph in `G`;
  - (L): each wing's setting acts only through an operation that reads and writes only its own region;
  - (R): `d_G(B's region, R_A) = 1 > T_A − t_B = 0`;
  - (MI).

  Yet B's setting reaches A's record within the same tick, and the result is the PR box, `S = 4`.
- **Why the proof fails.** Step 2, "after that, B's operations act within B's region", is used as if the tick map's
  components outside B's region were independent of `b`. (L) does not say that.
- **The fix.** Add:
  - (L′) for every tick `t`, the maps `φ_t` for different values of `b` agree on every component outside B's region,
    and symmetrically for A;
  - `t_B` is the earliest tick at which any value of `b` acts (R2-N7).

  Under (D), (L′), (R) and (MI), the induction is correct:
  - after tick `t_B`, the runs differ only within B's region;
  - each later tick spreads the difference by at most one `G`-edge;
  - `d_G > T_A − t_B` keeps `R_A` outside the difference set;
  - the pointwise CHSH bound finishes the proof.

  Main's own one-step form `u_a × u_b × id` satisfies (L′). The alternative is to keep (L) and require
  `d_G > T_A − t_B + 1`, with the tick map restricted to one own-wing operation composed with one step.

## 3. Owner requirement 1: the GHZ state and the measurement bases

**Not yet met (R2-B4).**

The QX6 §2 GHZ row names the rotated formulation precisely:
- the state `CZ₁₂CZ₁₃CZ₂₃|+++⟩`;
- per-qubit `X` or `Z` reads, with the operator set `XZZ`, `ZXZ`, `ZZX`, `XXX`;
- the values `+1, +1, +1, −1`;
- the sum `XZZ + ZXZ + ZZX − XXX = 4`, against a local maximum of 2 (P1).

The conventional formulation, however, is named only as "Mermin's standard GHZ presentation". It should give:
- **the state:** `|GHZ⟩ = (|000⟩ + |111⟩)/√2`;
- **the operator set:** `XXX`, `XYY`, `YXY`, `YYX`, with values `+1, −1, −1, −1` (P4(3));
- **the inequality:** Mermin's `XXX − XYY − YXY − YYX = 4`, against a local maximum of 2;
- **the bases:** per-qubit `X` or `Y`;
- **the scope note:** on this state `X/Z` reads give no all-versus-nothing contradiction, because the only
  full-weight `X/Z` stabilizer element is `XXX` (P1).

The two formulations should be stated as two distinct protocols, each with its state and bases. Nothing should say
"`X/Z` suffices" without the state attached. SHARED M11's QX-6 cell ("the GHZ-type option uses `X/Z` reads") needs
the same qualifier: "on the triangle graph state". Optionally, name the local-Clifford map between the two states.

## 4. Owner requirement 2: the Leggett–Garg bound and its protocol class

**Not met (R2-B2). I correct my own r1 B5 here.**

`3/2` is the Lüders bound: the maximum of `K₃` for projective dichotomic reads **with the Lüders state update**, in
any dimension (Budroni and Emary, PRL 113, 050401 (2014); L, not read first-hand). It is not an unconditional
quantum bound. Two points from that literature:
- With non-Lüders (von Neumann) projective reads of a degenerate `Q`, `K₃` exceeds `3/2`, approaching 3 with many
  levels.
- General instruments exceed it in an elementary way. A measure-and-prepare instrument that reprepares a diagonal
  state depending on the outcome implements any classical invasive model, so `K₃ = 2`, and even 3, is
  quantum-realizable.

So `K₃ = 2` exceeds the Lüders bound of the **declared QM comparator class** for QX-4c: Lüders reads of the carrier's
`Z`, with unitary `G` on the carrier and mediator. It is not "supra-quantum" or "QM-incompatible" in general.

**The sites to correct:**
- QX4 line 76: "For projective dichotomic reads, `3/2` is the quantum maximum";
- line 129: "exceeds the quantum maximum … QM-incompatible signature";
- line 251 (ABL-SA1c): "supra-quantum, QM-incompatible";
- line 301 (§7 item 2): "supra-quantum";
- line 322 (§8): "A value above `3/2` is QM-incompatible";
- SHARED T9: "supra-quantum", "QM-incompatible".

**Suggested wording:** "exceeds the Lüders bound `3/2` that holds for the declared comparator protocol (Lüders reads of
`Q`, unitary `G`). Values up to 3 are reachable in QM with non-Lüders or general instruments."

§8's crediting rule, that only values in `(1, 3/2]` are credited, can stand. It should be phrased as "outside the
comparator class", not "QM-incompatible".

The Tsirelson row in QX6 (`|S| ≤ 2√2`, "supra-quantum correlator quadruples") is fine. Tsirelson's bound holds for
every quantum bipartite strategy in the tensor-product model, whatever the measurement.

## 5. Owner requirement 3: separating proved, disproved and open claims

**Not met (R2-B5).** The status layers are labelled in place: A, D-scan, W, P, and MECH-OPEN. But no file separates
proved, disproved and open claims, and the refutations appear only implicitly as corrected text. Add one ledger, in
SHARED or per spec, stated timelessly, with explicit counterexamples. The content should be:

- **Proved** (layer in brackets):
  - QX3 A3.1(a) [A, with P2 exhaustive over `F_2⁴`] and A3.1(c) [A; sound, §2 above];
  - QX4 A4.1(a) [A, with P3 at one mode];
  - QX6 §2's stabilizer–Pauli bound `|S| ≤ 2` [A, with P1; Fine's theorem for the commuting case];
  - QX6 A6.1 [A], **only once (L′) is added**;
  - Main §3.3 [P].
- **Supported by a finite scan only:**
  - QX4 A4.1(b) (two modes; P3);
  - AW-QX4-1 (a marker).
- **Refuted, each with its counterexample:**
  - "Routing with own-cell reads and conservation on the ready support needs a non-affine map." Counterexample: P2's
    `L(s, c₁, c₂) = (s, s + c₁, s + c₂)`.
  - "A GHZ-type contradiction needs `Y` reads." Counterexample: the triangle graph state with `X/Z` reads, P1.
  - "INM agreement with QM forces null-result invasiveness" without (H2). Counterexample: P3's sharp-mediator
    witness, with `K₃ = 2` from the `t₁` kick alone.
  - "`A_4`: `K₃ ≤ 1`" with sharp supplies admitted. Counterexample: the same witness.
  - A6.1 under (D), (L), (R) and (MI) as now worded. Counterexample: P4(1), `S = 4`.
  - R4.9's "a detector that interacts only when its cell is occupied lies outside the affine class". Counterexample:
    the copy coupling `m ← m + c` is affine (P4(2)).
- **Open:**
  - every MECH-OPEN row;
  - H-Bell (R6.7);
  - R6.9's masking;
  - AW-QX4-1 for `m > 2` modes;
  - A4.1(c)'s integrality with non-stabilizer ancillas (R2-N1);
  - W3's classical status;
  - L-CLICK's typing.

## 6. Owner requirement 4: no restriction chosen to force agreement with QM

**Mostly met. Three places need fixing (R2-B3).**

These pass:
- **The `⊥ ↦ +1` rule** (QX6). It is the standard local assignment. It preserves A6.1's hypothesis and makes an excess
  over 2 harder, not easier, so it cannot force agreement with QM. ABL-BOT reports the alternatives, and Q6-4 is
  neutral.
- **NCONS** (QX3). Neither domain is selected: Q3-2 is neutral. On the ready support the two domains give the same `α`
  and `V` (ABL-NCONS), so the choice cannot force QM-like antibunching. It decides only whether a non-affine element
  enters.
- **Access** (D15(a)). It is owner-typed CS, and `access_only` is reported. It is not credited with dynamics.
- **(H2) of A4.4.** It is a protocol hypothesis taken from the cited INM experiments, not a restriction on OI.

These need fixing:
- **SHARED T9.** "Admitting sharp supplies (dropping SA-1(c)) can therefore make a construction QM-incompatible in
  QX-4" argues for SA-1(c) from agreement with QM. Owner D-sheet c.6735014875: "Passing a consistency check must not
  be presented as a new derivation." Restate T9 as the fact and nothing more: with a sharp mediator the affine class
  reaches `K₃ = 2`, above the comparator's Lüders bound. Add: "this is not a justification of SA-1(c), whose status
  remains posited, not derived (AP1:347)".
- **The M3 cell for QX-4 in the SHARED matrix** reads "R (backaction; AW-QX4-1)". It makes AW-QX4-1 a reason SA-1(c)
  is required. Remove AW-QX4-1 from that cell; QX-4 needs M3 for backaction only. SHARED §3's "possibly the
  affine-scope Leggett–Garg bound … not a result" can stay.
- **AW-QX4-1's "a candidate §A.29 consequence"** (QX4). Add: agreement with QM's Clifford-scope value is a
  consistency result (§A.23). It counts as an independent §A.29 consequence only if it is shown that SA-1(c), a
  restriction modelled on quantum uncertainty, was not fitted to it. Q4-4 should note that a proof would establish a
  property of SA-1(c), not justify it (R2-N6).
- **QX6 R6.9.** It is defined by its function ("a restricted preparation class under which R6.7 balances"). The row
  should say that a class fixed only by the balance equations is fitted to no-signalling. It would be creditable only
  if fixed in advance by an independent principle with its own consequence (§A.29). §9 Level 3 already says "fixed in
  advance (§A.29)"; carry that into R6.9 and A6.4.

**AW-QX4-1 in QX4 itself** is correctly kept as "record only; not a result", with §A.31 skepticism. Nothing in QX3,
QX4 or QX6 presents SA-1(c) as justified by it. Only SHARED T9 and the M3 cell do, as above.

## 7. The new owner questions

- **Q3-2** (`NCONS` domain): neutral. It is an owner decision with no recommended option.
- **Q3-3** (L-CLICK typing): neutral.
- **Q4-4** (should AW-QX4-1 become a paper-proof item): neutral. Add the caveat in R2-N6.
- **Q6-4** (the `⊥` rule): neutral. But r2 reassigns the identifier: r1's Q6-4 (HB-1) is now Q6-5 (R2-N4).

## Blockers

- **R2-B1. QX6 A6.1 is false as worded** (P4(1): `S = 4` under (D), (L), (R) and (MI)). Add (L′) and the definition
  of `t_B`, or adjust (R). Carry the change to SHARED §3 and §4, and to QX6 §§3, 6 and 8.
- **R2-B2. The Leggett–Garg protocol class** (owner requirement 2). Correct QX4 lines 76, 129, 251, 301 and 322, and
  SHARED T9, as in §4 above.
- **R2-B3. Agreement with QM must not support SA-1(c)** (owner requirement 4). Fix SHARED T9, the QX-4 M3 cell,
  AW-QX4-1's §A.29 wording and R6.9's justification, as in §6 above.
- **R2-B4. Name both GHZ protocols precisely** (owner requirement 1), as in §3 above, including SHARED M11.
- **R2-B5. Add the claim-status ledger** (owner requirement 3), as in §5 above.
- **R2-B6. QX4 R4.9's new sentence is false.** It says "a detector that interacts only when its cell is occupied is
  a controlled coupling and lies outside the affine class". But the copy coupling `m ← m + c` is affine (P4(2)). What
  is non-affine is an **occupation-conditional backaction**, `x ← x + c·m′`. The affine reciprocal coupling kicks on
  both branches, which is null-result invasiveness, as A4.4 already notes. Restate the sentence. Do not add a
  non-affinity requirement the argument does not need.

## Nits

- **R2-N1. QX4 A4.1(c).** The integrality claim (correlators in {0, ±1} "at any number of modes") needs its
  hypotheses: N2 uniform-coset laws in the affine class, and stabilizer preparations, ancillas included, in the
  Clifford class. With a non-stabilizer ancilla, a Clifford coupling can give non-integer correlators. For example,
  `CNOT` from an ancilla `cos θ|0⟩ + sin θ|1⟩` gives `C₁₂ = cos 2θ`. Whether a QM-matching violation then needs a
  non-Clifford `G` is open.
- **R2-N2. QX6 §3, two-system interface.** "Signals … at every `η`" dropped r1's "and at `h > 0`". Per the record (eq.
  (11) and below), signalling holds for every herald rate `h > 0`. Restore it.
- **R2-N3. QX6 §3, M2D.** Theorem NC dropped r1's "under an injective identification". Restore the hypothesis
  (M2D:483-497).
- **R2-N4. Identifiers.** Keep r1's Q6-4 (HB-1) under its identifier, and give the `⊥`-rule question a new one. This
  follows the spirit of §A.30 on identifiers.
- **R2-N5. `DISPOSITIONS-r2.md`.** Its "nothing else was changed" statement understates the diff:
  - the R4.9 sentence;
  - the two dropped hypotheses;
  - the renumbering;
  - widespread restyling.

  Either list them or revert the restyling. Keep each edit tied to a finding.
- **R2-N6. Q4-4 and AW-QX4-1.** State that an `m`-mode proof would establish a property of SA-1(c), not justify SA-1(c).
- **R2-N7. A6.1's `t_B`.** Define it as the earliest tick at which any value of `b` acts. Settings may differ in timing.
