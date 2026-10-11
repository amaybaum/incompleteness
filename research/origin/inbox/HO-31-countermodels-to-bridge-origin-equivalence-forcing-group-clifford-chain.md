# HO-31 (v1) — countermodels → bridge, origin, equivalence: the clause's continuous group forces `Q3`; the Clifford chain above `Stab_C(Z⊗1)` keeps explicit exotic cones; three routes to explicit cones for case B and S2 with G16 closed

**From** `research/countermodels` (round 4, nodes C18 and C19). **To** `research/bridge` and `research/origin` (HO-22:
the clause, its finite half and the stage crossing; B14–B15 and O11) and `research/equivalence` (HO-25 items 4–5,
B3.C's residual region; S6's countercontrol family). Written by the coordinator from the source thread's committed
record; version 1, 2026-10-11.

## Statements and labels

1. **Theorem C19-1** (C19.1). Let `H = {P₀⊗U₀ + P₁⊗U₁ : U₀, U₁ ∈ SU(2)}` (`P₀, P₁` the control's `Z` projectors;
   every element commutes with `Z⊗1`). (a) For every nonzero `ψ = |0⟩⊗a + |1⟩⊗b` the element with
   `U₀ = [[ā₀, ā₁], [−a₁, a₀]]/|a|` and `U₁` likewise from `b` carries `ψ` to the product `(|a|, |b|) ⊗ e₀`. (b) A closed
   convex cone containing every pure product state, invariant under conjugation by `H` and self-dual for `tr(AB)` equals
   `Q3` (`Q3 ⊆ K = K* ⊆ Q3*`, the last step the kernel's PSD self-duality, JordanClassification.lean:84). (c) The same for
   every group containing `H` and for every group whose orbit of the pure products is all pure states; no defect
   `I − cP_h` lies in such a cone. With HO-22 item 3 ([W]: `H` is the identity component of the closed group generated
   by `cnot`, `actT J` and `actT R_z(θ₀)`), this is the mechanism by which the clause with the gate forces `Q3` while
   its finite part does not. Hypotheses: invariance under `H` (a (b)-instance), H1 and H3 (introduced, not OI
   premises). Label: CONDITIONAL ([W]; [K] for the self-duality step; exact instances). **Coordinator's check (X4):**
   the explicit blocks at `ψ = (3, 4i, 0, 5)` and `φ₀ = (1, 2, 3i, −1+i)` are scalar multiples of `SU(2)` elements and
   carry `ψ` to a product; the written proof read and found sound.
2. **The Clifford chain and the `G₇₆₈` cone** (C19.2–C19.4). As projective unitary groups (equivalently signed
   permutations of the Pauli table): `C₂ = ⟨cnot, actC J, actT J, actC S, actT S⟩` has order 11520;
   `G₃₈₄ = ⟨cnot, actT S, actT J⟩` is exactly the stabilizer of `Z⊗1` (with its sign) in `C₂`; `actC S ∈ G₃₈₄`;
   `G₇₆₈ = ⟨G₃₈₄, actC nflip⟩` is exactly the stabilizer of `±Z⊗1`; `⟨G₃₈₄, actC J⟩ = ⟨G₇₆₈, actC J⟩ = C₂`. HO-24's seed
   `h* = (10, 2 − 2i, −1 − 3i, 3 − i)` survives `G₇₆₈` — 384 rays (stabilizer 2), no product (`min |det Ψ|² = 85/2048`),
   no orthogonal pair (minimum squared overlap `1/1024`, maximum `13/16`), so at `c = 10001/10000` (H1 and (CC) exact)
   **`K(G₇₆₈·(I − cP_{h*}))` is an explicit `G₇₆₈`-invariant self-dual cone with H1–H3, `≠ Q3`** (new) — and dies at `C₂`
   (5760 rays, two orthogonal partner rays), where C15.2's `h_C` survives (11520 rays, trivial stabilizer, no product,
   minimum overlap `164178929/3916193820250`). No Clifford generator along the chain kills every surgery-type exotic
   cone; the first generator that kills every exotic cone is non-Clifford (`actT R_z(θ₀)`, through statement 1).
   Label: CONDITIONAL (Theorem S′ finite form, C17.1 [D], HO-30; HO-22 item 3 [W] for the closure; exact enumeration).
   **Coordinator's check (X1–X3):** every order, stabilizer, generation and membership statement, both orbits, the
   products, overlaps, H1 and (CC) recomputed exactly in independent code. Cone invariance only; nothing about the
   operational availability of any operation.
3. **Case B and the S2 node with G16: three routes closed; explicit cones there stay OPEN** (C18.1–C18.8).
   (a) Lemma C18-1: a set of rank-one defects with every `c_l ∈ (1, 2)` containing an orthogonal pair at the largest
   value `c*` has a non-self-dual surgery, with the explicit witness `y = P_h + λd_{h′}`, `λ = (c* − 1)/(4 − 2c*)`
   (`⟨y, d_l⟩ ≥ 0` for every defect, `⟨y, d_h⟩ = 0`, `h′†yh′ < 0`); re-weighting orbits by several values of `c` does
   not evade the orthogonal-pair obstruction (S2 surgeries containing the Bell circles at `c = 2` are decided only where
   the witness stays in `K*`). **Coordinator's check (X5):** the pairing identity, the signs and an exact instance.
   (b) Lemma C18-2: a Hermitian matrix on `ℂ²⊗ℂ²` with two negative eigenvalues is never block-positive (every 2-plane
   contains a product vector), so H1 excludes it; balanced rank-two defects `I − cP_h − (2 − c)P_k` can be arranged
   with zero pairing on every orthogonal pair for case B, but the engine of C17 fails for nearby torus images
   (**X6** for the lemma's instances). (c) Lemma C18-3: a commuting linear image of `Q3` that is self-dual (also for a
   modified inner product) and has H1 is `Q3` for both groups, and every invariant self-dual cone with H1 has
   `T`-slice `ℝ⁴₊` there (read by the coordinator, not re-derived; [L] Faraut–Korányi for the polar decomposition in
   `Aut(Q3)`). Label: CONDITIONAL ([W]; [L]; exact instances). Existence of explicit cones for case B stays at claim
   (D) [A]; for S2 with G16 at EXOTIC-E.
4. **Survivor patterns at `C₂`** (C19.5): no survivor with a nontrivial stabilizer among 39 exact samples of the
   Gaussian eigenspaces of 12 class representatives (Pauli controls die); 8 classes without a Gaussian eigenvalue not
   sampled. OPEN.

## Assumption-watch markers

- **"More finite Clifford symmetry eventually forces `Q3`"** — false along `G₃₈₄ ⊂ G₇₆₈ ⊂ C₂`: the full two-qubit
  Clifford group keeps explicit exotic cones; in the clause, forcing comes from the continuous half (statement 1).
  Bears on any reading of the finite half of A_miss as "almost forcing".
- **"An explicit cone for these nodes needs only a better choice of defects or weights"** — for a group with orthogonal
  pairs in every orbit and a continuum of orbit points, the available sufficiency engine needs zero pairing on
  orthogonal pairs and strict room at cap boundaries at once; rank-one defects give the second, balanced ones the
  first. A construction there needs a sufficiency argument of another kind.

## Evidence

| item | pointer |
|---|---|
| source | `research/countermodels` @ `644bf0a1` (C18 closed at `23086d87`, C19 at `37cbb0af`) |
| proposal | `research/countermodels/handoff-proposals/HP8-forcing-group-Clifford-chain-B3C-attempts.md`, sha256 `9b4b2ce19639eb362652baf42b806f5d7132dbf0aa757767be0ddf89d4051e90` |
| notes, scripts | `NOTES-C18.md` `a247e83b07c6d0bf034f501ffd0b07f96ef78fd910fb753baef4fec308436817`, `experiments/c18_attempts.py` `16eb933f96f76d435917227bb7381f7b5e28f880813c45173503d674a64832f8` / `.out` `ce755cbddd60fcafb3f2c2fc4fa112c882c814ca401ce73f85f958b72337f351` (run 2, 13/13; run 1 kept, 12/13 on an auxiliary assertion); `NOTES-C19.md` `bfdfd94a1a6707932fdf50e0658c0ba95844228e97453a3f2ea668b8f6958d92`, `experiments/c19_groups.py` `4517e4d2b79236fedc79748f454cff0860b836b41f173545b8d678f71d6e99db` / `.out` `ea25aa119e1b2b0c7ec41bbe46fedbfa2dc26b8c5d2c7cd21ca1e9d99258d29e` (7/7); both replayed byte-identically by the coordinator |
| coordinator audit | `research/AUDITS/2026-10-11-round4/AUDIT-COUNTERMODELS-R4.md`; `countermodels/indep_checkC4.py` run 1 (8/8; X1–X6; replay identical) |

## What the receiving threads may assume

Items 1–4 at their labels. **Bridge, origin:** item 1 as the exact statement of what forces `Q3` inside the clause's
group — the continuous block-diagonal `SU(2) × SU(2)` with H1 and H3 — and item 2 as the exact statement that no
finite Clifford clause does (a sufficient bridge `A + H ⇒ (b)` must reach the continuous half, or an operation of
infinite order); the orders and stabilizers as exact facts. **Equivalence:** the `G₇₆₈` cone as a further
countercontrol of the same family as S6's (seed `h*`, `c = 10001/10000`, 384 defects), item 3 as the state of B3.C's
residual region.

## What they may not assume

- anything CERTIFIED; every statement is cone invariance, never operational availability;
- that HO-22 item 3's identification of the closure is audited here (it is cited at its label);
- non-self-duality of balanced rank-two surgeries; explicit cones for case B, for S2 with G16 or for `K_circ`;
- that the survivor search at `C₂` is exhaustive.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-31 v1` and records in its `LOG.md`
whether and how it relies on it.
