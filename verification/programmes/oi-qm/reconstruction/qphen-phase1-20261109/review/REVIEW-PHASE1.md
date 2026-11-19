# Independent review: QPHEN Phase 1 specifications (#1210)

**Verdict: REVISE.** Five blockers and fourteen nits. The design discipline is sound throughout:
- the programme rules are applied (one shared mechanism, A/B arms, typing, indirect access, classical alternatives);
- nothing is frozen;
- no mechanism is constructed;
- H-SDC is named only.

Three load-bearing paper claims overreach what their arguments establish. Two others misstate a requirement. The
exact probes below locate each one.

## Standing

- **Reviewer.** An independent subagent of the coordinating session. Read-only. This file and three probes are the
  only writes, all in `<session-local>/qphen/review/`. There were no repository or GitHub writes and no dispatch.
- **Authority.** #1210 c.6736966265 (owner, 2026-11-09): Phase 1 is paper-only.
- **What the probes are.** They are cheap exact checks of the paper claims, on generic objects: stabilizer states,
  `F_2` affine maps, and the affine-symplectic class. They build no OI apparatus, and they evaluate no proposed OI
  mechanism.
- **Files reviewed** (sha256 verified on read):

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `23775ceb774494cbbe06a6362945d0086d6b674d67ac6963a45572904279602c` |
  | `QX4-INCOMPATIBILITY-LG.md` | `6edcf8fa5b0e7a85e075f92c1115823cf8cf1252f86a96fff22e924ae0579899` |
  | `QX6-BELL-CHSH.md` | `1534b2c230991e7fcb5c1fedfffbfa38e9a9a05cb934a3155e8f289840fa7178` |
  | `SHARED-MECHANISM.md` | `5b07a5b9a97152d2e7aa7029c3b9bfb9135dd39657e24453b12e3e1cb4821898` |

- **Corpus.** Everything was read at `fd539e150759a6ea51ab279aeeac80fc06050ade` (`origin/main`) with `git show`.
  The local checkout's HEAD is the older `b1d782f9`. Every Main, Substratum, Methodology and book line cited by the
  specs was checked at `fd539e15`. Apart from N5 below, all cited lines match.
- **Drafts.** The cited draft hashes match the session files:
  - r13 is `arp/qc21/preregistration.draft.md`;
  - r12 is `r12/…`;
  - r11b is `r11b/…`;
  - `DESIGN-DS` r13 and `DECISIONS.md` match;
  - for OICORE-1, see N6.

## Probes

All run under `python3 -I` (3.13). The arithmetic is exact throughout: Gaussian integers, `F_2` and `Fraction`. No
floating point is used.

| probe | sha256 |
| --- | --- |
| `probes/p1_chsh_stabilizer.py` | `af34edb85fd026f0a2ef8b457d87cf5295f225693bdaeb9365ac3c657bbd0b5b` |
| `probes/p2_alpha_affine.py` | `312620b012231eb1bb48b90427be0b16047c5ca0d6c534196a8c04d64aa2cb9a` |
| `probes/p3_lg_affine.py` | `82d2099c263d8d11acf6aa2b93689076004dc50b5b66d68e400496e2ebf9e949` |

### P1: CHSH and GHZ

**Controls.**
- The enumerated stabilizer-state counts are 6, 60 and 1080 for one, two and three qubits, the known values.
- `|Φ⁺⟩` with settings `Z`, `X` against `(Z ± X)/√2` gives `√2·S = 4` exactly, so `S = 2√2`.

**Results.**
- Over all 60 two-qubit stabilizer states and all signed settings `±{I, X, Y, Z}`, the maximum `|S|` is **2**.
- Over all 1080 three-qubit states split 1+2, with every signed two-qubit Pauli on the second wing, the maximum is
  again **2**.
- On the triangle graph state `CZ₁₂CZ₁₃CZ₂₃|+++⟩`, which is local-Clifford equivalent to GHZ:
  - `⟨XZZ⟩ = ⟨ZXZ⟩ = ⟨ZZX⟩ = +1` and `⟨XXX⟩ = −1`;
  - the Mermin-type sum `XZZ + ZXZ + ZZX − XXX` is 4, against a maximum of 2 for local hidden variables (exhaustive
    over 64 assignments).
- On the standard GHZ state, the only full-weight `X/Z` stabilizer element is `XXX`.

### P2: antibunching in the affine class

**The case analysis.** Over every coset of `F_2⁴` and every pair of affine functionals (314,368 cases), `α` takes
only the values {0, 1, 2} or is undefined, and `α = 0` holds iff `f_B = f_A + 1` with `f_A` non-constant.

**The routing map.** Let `L(s, c₁, c₂) = (s, s + c₁, s + c₂)`.
- `L` is a linear bijection.
- On the ready support (`c₁ = 1`, `c₂ = 0`, `s` uniform) it maps to `(0, 1, 0)` and `(1, 0, 1)`. So `α = 0` with
  own-cell occupation reads, one excitation sits in the field cells, and the total weight is conserved on the ready
  support.
- It does not conserve weight globally.
- Fredkin is not affine, but it equals `L` on the single-excitation sector.

**Two counts.**
- 48 affine bijections of `F_2³` route the excitation on the ready support in this way.
- Exactly 6 affine bijections of `F_2³` conserve weight globally, and all 6 are coordinate permutations.

### P3: Leggett–Garg in the affine-symplectic class

**Model.** A `Z` read records `z` and adds an independent uniform kick to the carrier's `x`. Correlators come from
two-read runs: `C₁₂` from (R, G, R), `C₂₃` from (G, R, G, R) and `C₁₃` from (R, G, G, R). The scan takes the
maximum over the four `K₃` forms.

**Controls.** The QM comparators are 3/2, 4/3 and 37/25, matching QX4 A4.6.

| setting | maps scanned | correlators | max `K₃` |
| --- | --- | --- | --- |
| one mode (`|Sp(2,2)| = 6`, with translations; preparations `Z±`, `X±`) | 24 | in {−1, 0, 1} | 1 |
| two modes (`|Sp(4,2)| = 720`, with translations; second mode half-known or a both-unknown environment) | 11,520 | in {−1, 0, 1} | 1 |
| two modes, second mode sharp (both slots known) | 11,520 | in {−1, 0, 1} | **2** |

The `K₃ = 2` witness is `G: z′ = z + v, x′ = w, w′ = z, v′ = x + w`, with the carrier in `X⁺` and the mediator
`(0, 0)`:
- `C₁₂ = 1`, `C₂₃ = 1` and `C₁₃ = 0`;
- the violation comes from the `t₁` read's kick, which reaches `z₃` through `v`;
- the `t₂` kick does not reach `z₃` in the `C₂₃` runs.

## Answers to the five questions

1. **QX-6.**
   - **The stabilizer–Pauli claim is correct.** P1 confirms it. Each correlator is 0 or ±1. Anticommuting pairs on
     both wings allow at most two nonzero correlators. A commuting pair on one wing is jointly measurable, so Fine's
     theorem gives `|S| ≤ 2`. The suspicion that the Bell state with Pauli settings reaches `2√2` does not hold: it
     gives `S ∈ {0, ±2}`, and `2√2` needs the non-Pauli `(Z ± X)/√2` or a non-stabilizer pair state.
   - **The use of Main §3.3 overreaches its literal hypotheses** (B1).
   - **The GHZ row is wrong** (B3).
2. **QX-4.**
   - A4.1 is correct in its stated single-mode setting. It also holds at two modes under SA-1(c), and fails with a
     sharp mediator (P3; B5).
   - The macrorealism premise is right: `Q` read as a configuration functional is definite at every time.
   - "OI must carry null-result invasiveness" follows only when the `t₁` datum is also non-invasive (B4).
3. **QX-3.** A3.1's case analysis is correct (P2), and Fredkin is non-affine. But "`α = 0` only via L-PORT", and the
   need for a non-affine rule, hold only if number conservation is required off the ready support (B2). A3.2's
   hazard is real, but it is the existing copy-only hazard and is not specific to routing (N10).
4. **SHARED-MECHANISM.**
   - **Misstatements.** The Q-C2-1 claims (`DESIGN-DS` §§2, 5, 6; R7-B2; NR-16; the gadget rules; the `STAB` orders)
     and the M-ARC claim (receipt `ARP-1-MARC` complete at `fd539e15`; scope affine `N_1`) are not misstated. The
     Q-C2-2 claims are not misstated either: r13 does use `G_SM`, and M2D:43 and :191 confirm that `G_SM`'s edges
     are not reciprocal for `L ≥ 5`. Of the OICORE-1 claims (FIX §2; ACC_op consistency open §3.1/§3.2; §5(b);
     §8.4; §8.10; Lemma M), only Lemma M is stated without its applicability condition (N12). D18 is presented as
     decided when it is only drafted (N8).
   - **Propagation.** The matrix and the counting inherit B1, B2 and B3: the M14 typing, the count of "three distinct
     non-affine rules", T4, and M11 in QX-6.
   - **H-SDC** is kept as named only (not adopted, typed or evaluated). Its obstacles are listed first and a
     productivity test is stated. Acceptable.
5. **Programme rules.**
   - All three specs keep the programme rules (one shared mechanism, A/B, typing, indirect access through detector
     records, classical alternatives with "does not exclude" columns).
   - They freeze nothing and construct no mechanism.
   - **Off-`main` tracing is incomplete** (N7).

## Blockers

**B1. QX-6 A6.1, §3.2, §6 `B_6-loc`, §8 item 2; SHARED §3: Main §3.3 is applied beyond its literal hypotheses.**

Main:366-383 assumes four things:
- (i) the dynamics is deterministic;
- (ii) a **one-step** setting operation `u_a × u_b × id`;
- (iii) readouts at `k` iterates of **one fixed `φ`**, outside the cone (cone lemma, Main:364);
- (iv) a common ensemble, with a ±1 outcome **in every run**.

A6.1 says it applies "as stated" to:
- local coherent operations, Obligation C's included. C-SIZE-DEPENDENT needs one or two applications per run (§7
  tree);
- per-tick P3 arming as the setting switch (R6.4, M6). This is a change of which step applies per tick, a dynamics
  row (R7-B2), not a one-step state intervention followed by `φ^k`.

Neither is covered literally. The extension is standard: time-dependent local dynamics whose per-tick coupling graphs
all lie in one graph `G`, with multi-step own-wing settings and the distance condition measured from the first
setting tick. But it is a derivation of this file. It must be stated and proved as A (unreviewed), not attributed to
Main.

Three further points.
- **(b) The `⊥` outcome.** "A breach of the every-run ±1 clause, which full-mass accounting forbids" is incorrect.
  Full mass keeps `⊥` in the law. It does not make outcomes ±1. The spec must state how `S` is computed with `⊥`, for
  example a fixed local assignment `⊥ ↦ +1`. Only then does the theorem's hypothesis hold. Computing over coincidences
  is the detection loophole.
- **(c) Overbroad conclusions.** "It shows that observational incompleteness principles alone do not give Bell
  violation" (§6) is broader than the class ruled out. R6.7 (H-Bell's preparation-indexed adjacency) is itself a
  candidate OI principle. Restrict the conclusion to access restrictions, state restrictions on a setting-independent
  ensemble, own-wing local operations and local registration rules, under (ii)–(iv) and a stated `⊥` rule (Code
  Review Rules, no-go scope).
- **Propagation.** Apply the same corrections to SHARED §3's sentence "By Main §3.3's theorem, no construction made
  of … local operations, M12 included, exceeds …".

**B2. QX-3 A3.1 "Therefore", R3.6, §7 item 3; QX-4 R4.9 and A4.4's last bullets; SHARED M14, §3 counting, T4 and
§5: the non-affinity of routing is not established at the scope NCONS defines.**

The case analysis is correct (P2). The step "in a spatial setting `f_B = f_A + 1` means one detector clicks on the
absence of the field at its partner's site" is invalid:
- `f_A` and `f_B` are functionals of the supply, and affine dynamics can write complementary values into two separate
  cells, each read as its own occupation;
- P2's linear bijection `L` routes one excitation by an unknown bit, with `α = 0` and own-cell reads, and it
  conserves total weight on the ready support;
- §1 defines NCONS as conservation "on the ready support";
- `L` coincides with Fredkin on the single-excitation sector.

Non-affinity is forced only if conservation is required on the whole configuration space. There the
weight-preserving affine bijections are exactly the coordinate permutations (P2, `F_2³`; the general proof is a
one-line linearity argument). Permutations transport exclusivity but cannot generate it.

**Required.**
- Fix NCONS's domain and justify it.
- Restate A3.1's conclusion with the matching proof.
- Retype R3.6 / M14.
- Re-derive the dependants: QX-4's "INM needs QX-3's non-affine routing", SHARED's "three distinct non-affine rules"
  and T4, and §5's QX-3 row.

Whether OI's specific step admits a map like `L` is a mechanism question, and it is left unevaluated here.

**B3. QX-6 §2 GHZ row; SHARED M11 (QX-6 cell "? (GHZ option)"): "It needs Y-type reads, which the native toolkit
lacks" is false as a general statement.**

P1 gives an all-versus-nothing contradiction with `X` and `Z` reads only, on the triangle graph state. That state is
real and Clifford-prepared, and local-Clifford equivalent to GHZ. `Y` is needed only for the standard GHZ form, whose
only full-weight `X/Z` element is `XXX`.

The GHZ option's actual prerequisites are:
- a three-party entangled source (R6.5-type, absent);
- a cross-wing response (R6.7). A native `F_2` affine (toy-theory) class is itself a classical local model.

The phase-group reading of Coecke–Edwards–Spekkens concerns a fixed state presentation and does not license the
general claim. **Required:** correct the row and the M11 cell.

**B4. QX-4 A4.4 and its consequence; SHARED M16 and T2: a missing protocol hypothesis.**

The INM bound under `K_null = id` also needs a non-invasive `t₁` datum. The standard protocols fix `Q₁` by
preparation (Robens et al. 2015, Knee et al. 2016, as cited), or use INM at `t₁` as well.

Without this, an ordinary kicking read at `t₁` can produce `K₃ > 1` while the `t₂` read is ineffective on `Q₃`. P3's
witness gives `K₃ = 2` this way: the violation comes from the `t₁` kick alone.

"An OI construction matching QM under INM controls must have null-result invasiveness" follows only under these
conditions:
- `Q₁` by preparation, from a setting-independent supply;
- `K_null = id` for both detector placements;
- detector placement independent of the ontic state.

**Required:** state them, and carry them into M16 and T2.

**B5. QX-4 A4.1's scope; `A_4`, `B_4-nat`, ABL-SA1c and §7 item 2: paper expectations go beyond the setting
proved.**

A4.1 is proved for the single carrier. Its consequence "QX-4c depends on Obligation C" is sound for QM-matching
values in its general form: affine or Clifford correlators lie in {0, ±1}, so `K₃` is an integer, and the quantum
values in (1, 3/2] are non-integer. The ladder-relevant form must be stated that way.

But "no violation at native scope" (§7 item 2) and "`A_4`: `K₃ ≤ 1`" are not supported once `G` couples to a further
cell:
- with a sharp mediator, P3 gives `K₃ = 2` within the affine-symplectic class. This is above the quantum maximum of
  3/2 for projective dichotomic reads (Budroni–Emary 2014; literature, not read first-hand);
- under SA-1(c) or environment supplies, `K₃ ≤ 1` survives at two modes. This is an exhaustive finite scan, not a
  theorem.

**Required.**
- State A4.1's mode scope.
- Correct `A_4`'s expectation, or define `A_4`'s admissible supplies so that the claim holds.
- Add ABL-SA1c's 4c expectation: `K₃ = 2` is reachable, which is a supra-quantum, QM-incompatible signature.

**Classification (§A.31).** NEW, scoped to two modes and one read model. SA-1(c) appears to carry the affine-scope
`K₃ ≤ 1` bound beyond QX-0's complementarity. If it generalizes, it is a candidate consequence beyond the problem
SA-1(c) was built for (§A.29). Because this reading favours the framework, it needs an independent proof for `m` modes
before any use. Record it as an assumption-watch marker, not a result.

## Nits

- **N1. QX-6 §2.** The commuting case is not "trivial". The reason is joint measurability (Fine's theorem), and it
  covers multi-qubit wings as well. A6.2's "Necessary" needs the qualifier "with a stabilizer pair state": a
  non-stabilizer pair state with Pauli settings reaches `2√2`.
- **N2. QX-6 §1.** "Marginal-bias corrections where needed" is vague. The TLM/Landau criterion characterizes the
  correlator projection of the quantum set exactly. For full behaviours with biased marginals no closed-form exact
  criterion exists.
- **N3. QX-6 §3.** "Its source class admits PR behaviour at `η = 0`" should follow the record: an *enlarged* source
  class does, as a separate conditional countercontrol, and the fixed baseline source does not (two-system interface
  §6).
- **N4. QX-6 A6.4 and §3.2.**
  - "Predicted to produce signalling": a supply law signals iff it leaves the kernel of the balance map
    (prepared-pair-source §4), and whether ABL-SA1c or ABL-N2 do so depends on the construction.
  - "In OI the candidates for this role are N2 and SA-1(c)" should read "the only state restrictions in the present
    toolkit; none is shown to mask".
  - The "hard-to-vary corollary" wording needs the §A.31 skepticism that a favourable reading calls for.
- **N5. ROADMAP:764-769.** This is the range HB-1 quotes from an earlier ROADMAP. At `fd539e15` the quoted text is at
  ROADMAP:974-979. The citation appears in QX6 §8 item 2 and §11, and in SHARED H-SDC obstacle 5. Cite it through
  HB-1 or correct the lines.
- **N6. QX3 §0.** `9b82ecc2…` is `oicore/OICORE-1.md`. `OICORE-1-r6.md` hashes to `ec7966c9…`; the two differ by
  "ε-route" against "Route". Name the file.
- **N7. §A.42 item 8 tables are incomplete.**
  - Issue comments are not traced:
    - #1210 c.6736966265 and c.6734406842;
    - #1169 c.6734304025 and c.6734374076;
    - #1060.
  - c.6734406842 item 2 is used as *support* in QX4's witness table. Its support rests on DESIGN-DS finding 6 [D], so
    it is off `main`.
  - OICORE-1 is missing from QX4 §10 and QX6 §11.
  - `DECISIONS.md` and NR-13, NR-14 and NR-16 are missing from QX3 §10.
- **N8. QX3 §0 (IR) and SHARED M9.** "Owner-typed under D18" presents D18 as decided. `DECISIONS.md` lists it with
  option (a) drafted. It should read "pending D18".
- **N9. The type columns mix kinds.** They mix the owner's three-way types with **MC** (a dependency marker) and
  **NX** (untyped). Separate type from dependency (R3.8, R4.4, R4.5, R6.6).
- **N10. QX-3 A3.2.** The hazard is `DESIGN-DS` finding 9 / ABL-RECIP (copy-only coupling). Routing matters only
  because a non-affine rule need not be symplectic or reciprocal, as `G_SM` shows.
- **N11. SHARED T8.** "OI is a … epistemically restricted model" should say *construction B* is. SA-1(c) is CS.
  Macrorealism per se holds of `Q` as a configuration functional, which is an IR premise.
- **N12. SHARED §4 controls.**
  - "C's ABL: affine rules give no W-CL" is conditional on Theorem C [D] and on Lemma P, which is proved conditional
    on Theorem C(ii) and L1–L3.
  - Lemma M applies only where a core-realizer satisfies the restriction, and it is not used for ACC_op.
- **N13. QX-6 §3.2.** "That means … preparation-indexed long edges" leaves out three cases:
  - failure of (iii) by insufficient separation (`d ≤ k`);
  - failure of (ii) by region overlap;
  - both are excluded by the experimental design (R6.2), not by the theorem, and the spec should say so.
- **N14. QX-4 corpus search.** Main:358 also mentions Leggett–Garg ("Leggett-Garg violations included").

## What is right and should be kept

- The Main §3.3 citations, the measurement-dependence bound (Main:421) and the H-Bell anchors (Substratum:131,
  :467, :481; Methodology:393; ch01:173; ch04:124) all match `fd539e15`.
- The rational comparators are exact:
  - QX-6: `S = 5/2`, which sits on the TLM boundary;
  - QX-4: `K₃ = 3/2`, `4/3` and `37/25`.
- The separation between ontic and operational no-signalling, the complete-history requirement and the `access_only`
  discipline match the records on `main`.
- QX-3's honest ceiling is sound: W1 and W2 exclude only classical fields under square-law detection. So is QX-4's
  point that Main:486 already reaches `K₃ = 3/2` classically.
