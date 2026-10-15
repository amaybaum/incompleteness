# F2-2 correction 1 (2026-10-15): commuting gates can have noncommuting generators

Append-only correction to `../RESULT.md`, raised in owner review. `RULES.md`, `RESULT.md`,
`f2_2_exact.py` and its output are unchanged. The exact check is `commuting_check.py`, which
imports the frozen F2-1 module by path.

## The defect

T_loc flows a layer by the sum of its gates' generators, and the frozen text asserts that each
layer then completes its gates, so the tick ends at ρ(L_M). That holds when the generators within a
layer commute. It fails in general: two commuting gates that share a site can have noncommuting
generators.

**The owner's witness, reproduced exactly.** Take q = 3 and the pair gate δ|x, y⟩ = ω^{−xy}|x, y⟩
with principal generator G_0.

- P = |ψ⟩⟨ψ| with ψ = (|00⟩ + |01⟩ + |10⟩)/√3 lies in the eigenvalue-1 eigenspace, so G_0 P = 0.
  Since e^{2πiP} = 1, G = G_0 + P is a generator of δ supported on its pair: a member of Γ_all
  outside Γ_spec.
- On the chain 1–2–3, K = G_12 + G_23 and D = δ_12 δ_23 give [K, D] ≠ 0 (16 nonzero entries). Its
  (|011⟩, |001⟩) entry is (1 − ω²)/3.
- K commutes with e^{2πiK}, so e^{2πiK} is not proportional to D: this generator choice does not
  implement the update [W].
- [K, X_1] commutes with X_3 and Z_3, but [K, [K, X_1]] does not. The Heisenberg image of X_1 is
  analytic in the duration, with that coefficient at second order, so the strict one-edge cone
  fails for all small nonzero durations [W].

**A second witness at two sites.** Under R_self the coupling [[1, 1], [1, 0]] puts δ_1(1) and
δ_12(1) in one layer. A rank-1 projector P_s inside the degenerate eigenspace span{|1⟩, |2⟩} of
δ_1(1) commutes with its principal generator, so G_s0 + P_s generates δ_1(1). Yet the layer
generator fails to commute with the layer's gate product (4 nonzero entries).

**Controls.** The principal generator, and a diagonal non-spectral one (G_0 + |00⟩⟨00|), commute
with the layer and leave the second-order distant term at zero. The check runs twice with
byte-identical output.

## The restricted candidate

E1-L is consistent only for generator choices whose coupling-layer generators commute:

- **Γ_comm** is the set of choices in which, for every coupling of the repertoire, the generators
  of the gates in that coupling's layer pairwise commute. For these choices e^{2πis ΣG} = Π e^{2πisG}
  at every fraction s.
- **Γ_diag ⊂ Γ_comm**: coupling-gate generators diagonal in the registration basis. This contains
  Γ_spec and, for example, G_0 + |00⟩⟨00|.
- **Unrestricted parts.** The free layer's gates sit on distinct sites, so their generators commute
  for every choice. Translations flow alone. Neither needs a restriction.
- **Γ_comm = Γ_all at N = 1.** Every coupling layer there has at most one gate.
- **Γ_comm = Γ_all under R_cf at N = 2.** Each centre-free coupling's layer has one pair gate.
- **Γ_comm ⊊ Γ_all under R_self at N = 2 and on any chain at N ≥ 3**, by the two witnesses.

A choice outside Γ_comm contradicts L0, so the tick does not end at the update; it is not a
member of the candidate.

## The all-generator claims, one at a time

Each frozen [W] line is a written argument printed by the script, not a computation over the
generators it names. Replay identity is no evidence for it, so each is re-examined on its own.

| frozen claim | status |
|---|---|
| L0, "U(1) = u^{⊗N} D(M) for every member of Γ_all" | **False** for Γ_all (both witnesses). Holds on Γ_comm, since commuting exponentials multiply. The measured L0 cells use the principal member and are unaffected. |
| L1, "the flow factorizes across uncoupled blocks for every member of Γ_all" | **Survives as stated.** It uses only that no gate crosses the blocks, and needs no commutation within a block. For a member of the candidate it is read on Γ_comm. |
| L3, "the strict one-edge cone for every member of Γ_all" | **False** for Γ_all (the owner's witness, second order). Holds on Γ_comm: the layer at fraction s is a product of commuting local unitaries, so conjugating a site operator involves only the factors touching that site. |
| C3(a-self), "full for every generator choice" | **Holds on Γ_comm.** The argument needs the integer-time images inside the generated group, which is L0. At (3,1), (5,1) and (7,1), Γ_comm = Γ_all, so the token's Γ_all stands there. At (3,2) it narrows to Γ_comm. |
| C3(b-self), "[L] route over Γ_all at q = 3, 5" | **Holds on Γ_comm.** It stands as Γ_all at (3,1) and (5,1), and narrows to Γ_comm at (3,2). The free half-layer's non-Clifford property over every free-layer generator is unaffected. |
| C3(a-cf) at (3,1), "full over Γ_all" | **Survives.** N = 1, so Γ_comm = Γ_all. |
| "Every square root of u is non-Clifford (Γ_all)" at q = 3, 5; C4(b) over Γ_all | **Survives.** These concern the free layer only. |

Every [X] cell, and every count over Γ_spec members (D1, D2, the touching analysis, the listed
lattice points), concerns members of Γ_spec ⊂ Γ_comm and is unaffected. The verdict
`E1L-LOCAL-AND-SELF-CONTROLLING` was generated from those measurements and stands. Its scope tags
are read as above.

## The findings, narrowed

- **Finding 1.** Gate-wise continuity gives exact uncoupled independence and a strict one-edge
  causal cone for every generator choice in Γ_comm. That family contains Γ_spec and Γ_diag, and at
  N = 1 it is every choice. Outside Γ_comm the frozen rule does not implement the update and breaks
  the cone. The composite principal logarithm of F2-1 fails independence and the cone as reported.
- **Finding 2.** With self-couplings, the all-duration algebra is full for every choice in Γ_comm,
  which at N = 1 is every choice. One-duration density is unchanged: it was established over
  Γ_spec.
- **Findings 3 and 4** are unchanged. Finding 3 is established over Γ_spec and computed members.
  Finding 4 concerns the free layer.

**Open:** whether Γ_comm contains non-diagonal coupling generators at N ≥ 2, and the control
content of any member of Γ_comm outside Γ_spec. No such member was computed.

## Provenance

| file | sha256 |
|---|---|
| `commuting_check.py` | `6b4b0d6cfb7a1f4ac1060c217b9589302b89f5b173d79335a77c5b70a18aa489` |
| `commuting-check-output.txt` | `a70d2333f3d0737f7596d4babb1b1ca2848b8407068eacb7bf6ddb64ff6c1497` |

Local runs, standard library only, under a second each. They are not `check-run` attestations.
