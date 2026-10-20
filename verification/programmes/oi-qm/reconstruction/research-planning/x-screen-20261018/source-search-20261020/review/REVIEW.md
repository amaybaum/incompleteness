# Independent adversarial review — PR #864 source checkpoint (`a864/SOURCE-CHECKPOINT.md`)

Reviewer: independent agent; did not write the checkpoint. Research only; nothing in the repository was written,
no GitHub writes, no dispatch. Reads: `git show` of `85e949ad` (REPORT), `641ae161` (PREMISE-MEMO), `acfef447`
(F2 memo), `92de3143` (papers, kernel, audit), PR #864 body (GitHub MCP) and `a864/comments.json` (owner scope
comment 6280945976). Work dir: `rev864/` (this file's directory). `df -h`: 28 GB free.

## Verdict: **CONFIRMED WITH CORRECTIONS**

Every exact claim the parent asked about holds: the reproduction, the 8/24 count, orientation reversal on Γ(Q3),
the K(Z_F) exclusion, the W witness and the kill test. I found no PSD/CP import in EXC's statement. Two findings
must be fixed before the checkpoint is posted or cited.
- **B1:** the stated survivor K_H fails EXC-24.
- **B2:** EXC-S is defined in two different ways.

Neither changes the headline (no source found; EXC is not sufficient), and I supply a repaired survivor for B1.

***

## 1. Reproduction (task 1)

```
sha256sum a864/src_witness.py a864/src_witness.run{1,2}.out
bfce213f…78eb  src_witness.py                      (matches checkpoint)
2dfcfda3…e110  src_witness.run1.out / run2.out     (match checkpoint)
62ef2233…6f91  sdp_zf_search.py ; 82996068…69b5 sdp_zf_search.out ; 9222e9df…15f1 run1.out ; e5deb4dd…02e8 .at-run1  (all match)
a864/venv/bin/python -I -B a864/src_witness.py > rev864/rerun{1,2}.out   → rc=0, rc=0
sha256 rerun1.out = rerun2.out = 2dfcfda34ecbc735d54032d8cf2ee7e76307401e214984ac800649bf6aeee110 ; cmp vs run1.out: SAME
SUMMARY 49 PASS, 0 FAIL   (Python 3.13.16, SymPy 1.13.3)
```
I ran `diff` between the earlier script `run1-harness-error/src_witness.py.at-run1` and the current one.
- The only changed check is the nonvacuity pair: `BASIS[4]` (X⊗I, which commutes with `BASIS[1]` = I⊗X) became `BASIS[2]` (I⊗Y).
- The edit also added two Γ-conjugated controls, and E1b, E2b and E11–E13 were appended.
- The earlier output reads `38 PASS, 1 FAIL` (the nonvacuity check).

This matches §6 of the checkpoint.

## 2. Check-by-check (task 2)

**Substantive checks** (they test what the checkpoint says they test):
- E1 (both), E2 8/24 with 16 exact witnesses, E2 SWAP sign, E2 local-X sign, E2b;
- E3 (all four), E4 (all seven), E5 (all three), E7–E9, E10 trace isometry/unit/involution;
- E11 witness, E12, E13 (all three).

**Weak, tautological or duplicate checks.** None of these invalidates a conclusion; each is recorded here as notes N3 and N4:
- E2 controls "Γ∘Ad(CN(u⊗I))∘Γ sign +1" and "Γ∘T∘Γ sign −1" w.r.t. br_Γ hold by transport for *any* involution Γ. They test the
  `br_G` code path only. The checks on Ad(U) and T w.r.t. br are algebraic identities; they work as code-path controls only.
- "E2 every native permutation has sign +1 w.r.t. Q3" is automatic, since permutation matrices are unitary.
- "E2 exactly 4 of those 8 have sign −1: the SWAP-containing ones" counts 4 but does not check *which* 4. The table
  shows they are the coset S·{I, I⊗X, X⊗I, X⊗X}, and my R2 checks this.
- E1b is E1 rewritten using Γ² = id; it is not an independent fact.
- E10 "fails only positivity" checks only that Γ(B) has eigenvalue −1/2. "Only" and "keeps all data" are not computed.
- E11 control: an absence of witnesses, as the checkpoint itself says.
- **MUT block (5 items).** These are negations of facts already checked. None of them mutates the checker.
  - MUT1 is E1's second check negated, MUT2 is E2's SWAP-w.r.t.-Q3 check negated, and MUT4 is E4 negated.
  - MUT5 is weaker than E5.
  - MUT3, "Γ → full transpose", is rejected by an identity: the T-transported bracket is exactly −br.
    `rev864/mut_check.py`: `brT + br == 0 identically: True`.
  - So "mutations with Γ → id or Γ → T give no separation" is forced by algebra and is not a sensitivity test.

No check simply reproduces its own premise in a way that voids a verdict. The fixed nonvacuity check is now genuine.
`sign_wrt` is also non-vacuous on its own terms: it returns `None` when every bracket vanishes.

## 3. Independent exact verification (task 3) — `rev864/indep.py`

This is my own code; it reuses nothing from `src_witness.py`. It uses only SymPy exact arithmetic, from the same venv
library. Methods differ from the author's: E1 is checked as a combinatorial map on matrix-unit positions, and
non-membership is shown by negative 2×2 principal minors with no eigenvalue routine.
```
a864/venv/bin/python -I -B rev864/indep.py   (twice) → rc 0, rc 0; both outputs sha256 6951e8a8…63f7, SUMMARY 24 PASS, 0 FAIL
indep.py sha256 0901724c2dd9a335c597ce369f37c99d801b30e1f3def2ca55b51d2a38fe8b54
```
My first attempt (`indep.firstattempt.out`) failed R5. The error was mine: I wrote the Lagrange identity without
the conjugations. Corrected to |p0 q̄1 − p1 q̄0|²/2, the same form as the author's.

| id | result |
|---|---|
| R1 | Γ∘Ad_S∘Γ = T∘Ad_S as a position map (16/16). Kill-test form Γ∘(T∘Ad_S)∘Γ = Ad_S. |
| R2 | Exactly 8 of 24 preserve Γ(Q3). The 16 others each have an exact negative 2×2 minor of Φ_P(vv†), v = e_i + ω e_j. The 4 transpose-type ones are exactly S·{I, I⊗X, X⊗I, X⊗X}; the set agrees with the author's table. |
| R3 | Bracket sign on exact random rational Hermitian pairs: −1 on exactly those 4 and +1 on the other 4 automorphisms. Control: CNOT has no sign. |
| R4 | S z_{s,t} S = z_{−st,t}, so z_{1,1} ↦ z_{−1,1}. P_m is a rank-one projector with pairings −½ and +½. Symbolic LP identity: pairing with P_m and with the trace forces Tr y + 2Tr(P_m y) + 2D = 0, so y = 0, D = 0 and C = 1. charpoly(z) = (λ−½)³(λ+½). |
| R5 | Tr(WB) = −½ and [W,S] = 0. ⟨pq\|W\|pq⟩ = \|p0 q̄1 − p1 q̄0\|²/2 symbolically, so W is block-positive and the K_S MI-failure stands. |
| R6 | K_S, K_H and a repaired K_H\* against EXC-24 (see B1). |

The orientation claim is fine. Antiholomorphic v ↦ conj(Sv) acts on H₂(ℂP³) by −1 [L, standard], and R1/E2b supply
the exact part. The homology route needs no classification of Aut(Q3), as §3.3.1 says.

## 4. Written arguments (task 4)

- **K(Z_F) exclusion [W, new].** Sound. The extremality algebra checks out exactly (R4). Isolation follows because the
  rays coming from L are normalized PSD while each defect has λ_min = −½, and there are only finitely many defects.
  A path in a Lie group Aut(K) gives a continuous orbit of an isolated ray, so the ray is fixed. Ad_S ∈ Aut(K(Z_F)):
  it preserves Q3 and permutes Z_F, hence preserves Z_F\* and L.
- **K_B / SEP / maxCone [W, new].** Sound. Ext(C₁+C₂) ⊆ Ext(C₁) ∪ Ext(C₂) holds in general. B is isolated, since
  product fidelity with Φ⁺ is at most ½. The product component S²×S² is preserved, and the factor exchange swaps the
  H₂ generators. For maxCone, α ↦ (α\*)⁻¹ is a homeomorphic group isomorphism Aut(SEP) → Aut(SEP\*), and Ad_S is
  self-adjoint and involutive, so it is fixed. No gap found.
- **K_H dimension count.** Correct as far as it goes: the pure states lie in U(t)·Prod ∪ G_pure, of real dimension
  at most 5. An exact version exists and is better: the singlet is in neither piece (R6), and a rank-one element of K_H
  would be extreme, so P_singlet ∉ K_H. But K_H fails EXC-24 (B1).
- **"Independent exact certificate (E2)" for Γ(Q3)** (§3.2). For s(α) to be defined on *every* unit-preserving
  automorphism, Kadison's theorem is needed: unital order automorphisms of Q3 are Ad_U or T∘Ad_U. Passing from
  Aut(K) to its unit-preserving subgroup needs a retraction argument. Both are [L]/[W], and the sign of Ad_S is E1
  transported, not an independent fact (N1).

## 5. Smuggling of PSD/CP or the target (task 5)

- EXC-24 and EXC-S mention only Aut(K) (linear, GL topology), Ad_P and the identity component. No PSD or CP is
  evaluated on a competing cone. The exclusion proofs use each fixture's *definition*: Ext(Γ(Q3)) = Γ(rank one),
  L ⊆ Q3, Ext(SEP) = products. These are memberships under memo §4's convention (pmemo l.281–282).
  **"Without assuming PSD/CP for competing cones" is accurate.**
- The force comes from H-CAR (the exchange acts by Ad_S on the carrier) together with the fixed identification. This
  is a cross-token orientation datum; the checkpoint states both (§3.3.2).
- Kill test wording (N2). "Re-identify the exchange as T∘Ad_S" alone is not a consistent re-identification of the
  native permutation group. SWAP = CN₁₂·CN₂₁·CN₁₂, so re-identifying only SWAP while keeping CNOT native is not a
  homomorphism. The consistent form is the Γ-transported identification P ↦ Γ∘Ad_P∘Γ, which sends Ad_S to T∘Ad_S (E1).
  Under it Γ(Q3) satisfies EXC-24 as well as EXC-S. The conclusion stands; the wording should say this.

## 6. Citations (task 6)

The following were checked at `92de3143` / `641ae161` / `85e949ad`:
- SecondOrderCircuit.lean :356 `unit` (with `proj g = (1−g)/2` at :352, so unit S t = Π_s + e^{iπt}Π_a), :377
  `unit_one`, :469 `gate_drive`, :771 `localGate_isGate`.
- SwapLayer.lean :446 `continuous_swapQ_time`, :494 `swapQ_add_time`.
- continuous-time-audit.md :69, :129, :141 (all three read as quoted).
- GR.md :184 (operational antiunitary invariance), :198–204 (classification / orientation no-go), :268–272 (layer-flow
  box; `derivedOI_qm_iff_layerFlowExecutable'` at :270; the "not ⇒" box at :272).
- Main.md :72–80 (C1–C4), :336 (generator exactly Hamiltonian), :656 (lattice orientation, "a fixed global
  parameter"); SM.md :446–452 (H-spin′ open).
- REPORT:153 ("…local permutations are Γ-compatible [EC], so only entangling native operations can separate") and
  REPORT:123 (P2, 8 of 24); memo U1 (l.471), U3, F-β (l.80), §6(c) (l.437–443).

Defects (minor):
- `exact_of_local` is at ReachabilitySeam.lean **:251**; :249 is its docstring.
- `src_witness.py`'s E13 comment names `sdp_zf_probe.py`; the file is `sdp_zf_search.py`.
- §3.3.7's paraphrase of memo §6(c) quotes only its second clause (N5).

## 7. Claim/evidence and register (task 7)

The note is under `verification/` and is not paper prose, so §A.32/§A.33 apply only loosely. No caps emphasis beyond
status labels, and no revision-history voice. Two overclaims: B1 (EXC-S → "EXC"), and §3.3's closing sentence, which
asserts the K_B/K(Z_F) exclusions without the "[W, new], unreviewed" tag that §3.2 and §5.4 carry (N6).

***

## Blocking findings (fix before posting or citing)

**B1 — K_H is not a survivor of EXC-24, so the "EXC ⊕ MI ⊕ MEV survivor K_H" of §5.3 is unsupported.**

§3.3.5 correctly claims only EXC-S for K_H = cone(U(t)·(SEP ∪ G)). §5.3 says "EXC ⊕ MI ⊕ MEV (survivor K_H [W])",
where EXC is the headline EXC-24, and the brief repeats this. **K_H fails EXC-24.**
- Ad_{X⊗X} ∈ Aut(K_H) [EC, R6]: X⊗X commutes with S, hence with U(t), and maps products to products and G_pure to G_pure.
- Ext(K_H) = U(t)·Prod ∪ G_pure, all rank one.
- G_pure meets the closed set U(t)·Prod exactly at {|00⟩, |11⟩} [EC, R6]. There a = 0 and det C_s = αβ, using my exact
  criterion: v ∈ U(t)·Prod ⟺ |det C_s| = |a|², with controls and countercontrols in R6.
- Points of G_pure∖{|00⟩,|11⟩} have neighbourhoods homeomorphic to ℝ². Points of U(t)·Prod do not, because every
  neighbourhood contains a 4-ball.
- So every homeomorphism of Ext(K_H) preserves the pair {|00⟩,|11⟩}, and a path from the identity fixes each of them.
- Ad_{X⊗X} swaps them [EC, R6], so Ad_{X⊗X} ∉ Aut(K_H)₀ [W, reviewer; not independently reviewed].

**Repair (checked):** K_H\* = cone(𝒰·(SEP ∪ G)), with 𝒰 = {U(t)(V⊗V) : t ∈ ℝ, V ∈ U(2)}, a compact connected group.
- By Takagi, the pure set is Sym ∪ U(t)·Prod.
- The 4 S-commuting native permutations (I, S, X⊗X, S·X⊗X) lie in 𝒰.
- Each of the other 20 maps a pure state of K_H\* outside the pure set [EC, R6].
- B ∈ G gives MI; K_H\* ⊆ Q3 gives MEV.
- P_singlet ∉ K_H\* [EC + extremality], so K_H\* ≠ Q3.

So EXC-24 ∧ EXC-S ∧ MI ∧ MEV ⇏ K = Q3 still holds, with K_H\* in place of K_H. Replace K_H in §3.3.5 and §5.3, or
restrict both to EXC-S. A further result: **K_S satisfies EXC-24 as well** [EC, R6]. The 20 non-S-commuting
permutations do not preserve it, and the 4 commuting ones lie on paths via U(t) and V⊗V. So the K_S bullet can say
EXC-24 ∧ EXC-S.

**B2 — EXC-S has two definitions.**
- The §2 table reads "EXC-S: additionally S ∈ Aut(K)", i.e. EXC-24 ∧ S ∈ Aut(K).
- §3.1 reads "EXC-S: Ad_S ∈ Aut(K)₀", which does not include EXC-24.

The survivor claims differ between the readings. Under the table's reading, K_H fails EXC-S too (B1). Fix one
definition and restate every survivor cell against it: the table's "Survivors", §3.3.5 and §5.3.

## Notes (non-blocking)

- **N1.** §3.2: label the bracket-sign certificate as E1 transported plus Kadison [L] plus the unital-retraction [W],
  not "independent exact". The homology route is the one that stands alone.
- **N2.** Kill test (E1b): state it as the Γ-transported identification of all native operations; see §5.
- **N3.** MUT block: rename it (e.g. "negated restatements") or replace it with real code mutations. "Γ → T gives no
  separation" holds by the identity brT = −br.
- **N4.** E2's "SWAP-containing" identity is not checked in code; R2 checks it. E10 "fails only positivity" over-labels
  its check.
- **N5.** §A.31 class. Memo §6(c) and F-γ already record the parts of EXC's structure that matter here:
  - every examined Γ-breaker carries a cross-token orientation datum;
  - the Γ ambiguity is the relative orientation of the token frames;
  - CH uses native SWAP for the cross-token identification and already corrected REPORT:153's "only entangling" line.

  EXC is new in *form*, since it uses no test, preparation or local operation. Under maximum skepticism the class is
  NEW (scoped, form) / ELABORATING in substance. §3.3.7 should quote §6(c) in full.
- **N6.** §3.3's closing classification sentence asserts the K_B and K(Z_F) exclusions without the [W, new] tag. This
  review checked those arguments and found no gap (§4); that is one review, not a reviewed record.
- **N7.** Citation fixes: ReachabilitySeam.lean:251 (not :249); E13 comment `sdp_zf_probe.py` → `sdp_zf_search.py`.
- **N8.** K_H's "≠ Q3" can be made exact (P_singlet ∉ pure set) instead of resting on the dimension count.

## Independently verified vs only argued

| claim | status |
|---|---|
| Reproduction, 49 PASS, byte-identical, all sha256 | verified (re-run ×2) |
| 8/24 preserve Γ(Q3); the 4 in S·(local X) reverse the Γ-bracket | verified, own code (R2, R3) |
| Ad_S on Ext(Γ(Q3)) is v ↦ conj(Sv) | verified (R1 combinatorial; E2b); the H₂ = −1 step is [L] |
| K(Z_F): defects extreme and isolated; S moves z_{1,1} → z_{−1,1} | algebra verified (R4); topology step argued, sound |
| K_B, SEP, maxCone exclusion | argued only (checked by reading, no gap found) |
| W = I/2 − B: block-positive, commutes with U(t), Tr(WB) = −½ | verified (R5) |
| K_Γ satisfies EXC-24 and MI | author's E12 logic re-derived; sound |
| K_S satisfies EXC-S (and EXC-24) and fails MI | verified (R5, R6) |
| K_H satisfies EXC-S, MI, MEV | argued; true for EXC-S only. **Fails EXC-24** (B1: EC ingredients + reviewer [W]) |
| K_H\* satisfies EXC-24, EXC-S, MI, MEV and ≠ Q3 | reviewer's EC (R6) + Takagi [L] + extremality [W] |
| No PSD/CP import in EXC | confirmed by reading |
| Citations | confirmed except N7 |

***

# Re-review (focused) of the corrected checkpoint

Scope: the coordinator's four items only. Before this section was appended, REVIEW.md had sha256 `1a02839e…efd1`;
that is the hash CORRECTIONS.md cites. Nothing in the repository or on GitHub was written.

## Verdict: **CONFIRMED WITH CORRECTIONS** — B1 and B2 closed, N1–N8 applied; one non-blocking wording fix (R-1)

### Hashes and re-runs
```
SOURCE-CHECKPOINT.md            c64e39c6…ac0d   (as stated)
SOURCE-CHECKPOINT.original.md   6d2d9495…4ebb2  (22780 bytes, the size of the file reviewed above; the diff's "<" side is the text I reviewed)
src_witness.py / run{1,2}.out   bfce213f…78eb / 2dfcfda3…e110  unchanged; re-run ×2 → 2dfcfda3…e110
src_witness_v2.py               66738e27…8dcd ; re-run ×2 (venv -I -B) → rc 0, both 21a631b1…4f1f (= recorded), 51 PASS
exc_survivors.py                738f36a9…d64c ; re-run ×2 → rc 0, both 2bb0ff4d…ec3d (= recorded), 16 PASS
```

### (1) B1 — closed
- K_H no longer appears as an EXC-24 survivor anywhere: not in the table, §3.1, §3.3 item 5, §4 or §5 item 3 (grep of
  `K_H` and `EXC-S`). §3.3 item 5 says K_H satisfies EXC-S, MI and MEV and fails EXC-24. The topological step carries
  the tag "[W: the reviewer's argument, checked by reading here, not independently reviewed.]", and §5 item 4 repeats
  that. K_H\* is stated correctly in the table, in §3.3 item 5 and in §5 item 3.
- `exc_survivors.py` tests what it claims:
  - **S1.** Derives the criterion symbolically: det(C_s + μC_a) = det C_s + μ²a², and U(μ)v has coefficient matrix
    C_s + μC_a. Control: 486 vectors in U(t)·Prod are accepted. Countercontrols: the singlet and (1,2,3,5) are rejected.
  - **S2.** For generic V, V⊗V commutes with S, maps products to products and maps G_pure into Sym. U acts trivially
    on Sym. This is the inclusion "pure states ⊆ Sym ∪ U(t)·Prod" the text says it uses.
  - **S3.** The 4 S-commuting permutations, and their membership in 𝒰.
  - **S4/S5.** Exact witnesses for all 20 other permutations.
  - **S6.** The K_H ingredients.
- I checked the claim that "witnesses are taken from U(t)·Prod", so that Takagi is not load-bearing. I ran a read-only
  instrumented copy that leaves the author file untouched (`rev864/exc_survivors_witsrc.py`, sha `1e536361…75cf2`). It prints
  `S5 witness sources: ['UProd']`, so all 20 witnesses come from U(t)·Prod and the claim holds. The script itself does
  not assert this; that is acceptable, since the text states it and I have verified it.

### (2) B2 — closed
EXC-S is defined once, in §3.1, as Ad_S ∈ Aut(K)₀. The table row now points to §3.1 and gives the same form. Both
relations stated are correct:
- EXC-24 ∧ S ∈ Aut(K) ⇒ EXC-S;
- EXC-S ⇏ EXC-24, via K_H, tagged [W].

The survivor cells (table, §3.3 item 5, §5 item 3) are stated against both forms and agree with each other:
- K_Γ: EXC-24, EXC-S, MI;
- K_S: EXC-24, EXC-S, fails MI;
- K_H\*: all four;
- K_H: EXC-S only.

"Each named fixture has S ∈ Aut(K)∖Aut(K)₀, so each fails both forms" is correct.

### (3) N1–N8 — applied correctly
- **N1.** The homology route is named as the independent one. The bracket sign is labelled "E1 transported", with
  Kadison [L] and the retraction [W]. The controls are called code-path controls.
- **N2.** The kill test uses the Γ-transported identification of all native operations, with the CNOT reason given.
  The step to EXC-24 is tagged [W]; it is correct, because Γ∘Aut(Q3)₀∘Γ = Aut(Γ(Q3))₀.
- **N3.** NEG is renamed in v2, and the identity brT = −br is checked on all 256 Pauli pairs. v1 is unchanged.
- **N4.** v2 adds the coset check, which builds the reversing set from the computed table. The E10 label is narrowed.
- **N5.** The class is NEW (scoped, form) / ELABORATING (substance). Memo §6(c) is quoted verbatim: it differs from
  `641ae161` PREMISE-MEMO.md l.437–443 only by the dropped list marker and line wrapping. F-γ and CH are cited.
  AW-S1 reads "NEW in form".
- **N6.** The closing sentence tags K(Z_F) and K_B as [W, new] and states their review status.
- **N7.** ReachabilitySeam.lean:251 is fixed. The v2 E13 comment names `sdp_zf_search.py`.
- **N8.** Exact P_singlet exclusions for K_H and K_H\* (S5, S6) replace the dimension count.

### (4) Diff — nothing beyond the corrections
Every hunk maps to a CORRECTIONS.md row (1–11). I found no new overclaim, no caps emphasis beyond status labels and
no paper-register problem; §A.32/§A.33 are binding on `papers/` only. The header pointer and the provenance phrases
("re-verified here with separate code") describe the record, which suits a research note.

### Remaining finding (non-blocking)
- **R-1.** §3.3 item 5 opens: "Each survivor below is generated by pure states, so its extreme rays are exactly its
  generator rays". This does not hold for K_Γ = Q3 + ℝ₊Γ(B): Γ(B) = S/2 is not a pure state, and not even PSD. K_Γ's
  claims rest on E3 and E12, which do not use the sentence, so no conclusion is affected. Suggested wording: "Each
  survivor below other than K_Γ …".
