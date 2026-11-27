# FSLICE-PS-1: changes from REPORT.md (r1) to REPORT-r2.md (r2)

r1 is `REPORT.md` at `b3500e3194e4db04372c6ed2bf9b4ab4962c3dc8`, kept unchanged. The review is the
independent review of r1, PR #1624 comment 7209242260 (posted from the account amaybaum, created
2026-11-27T03:45:08Z; verdict REVISE, minor to moderate, no class changes). Findings 1–11 are
applied as the coordinator directed.

| Finding | Change in r2 |
| --- | --- |
| 1 (Medium): R2.2 is false as stated | R2.2 is restated in two parts. (a) Naturality under the stated symmetry types (F, the translations, O, the custodial action) does not force LI; the O-equivariant transport is marked [W]. (b) Naturality under the whole linear commutant of F does force LI, through R_π = 1 − 2P_π. That requirement is not stated, so it is recorded as the new premise NAT-C, not adopted (stopping condition 3). Added in §0, §6, §7 and §8 (O-3) |
| 2 (Medium): reflection-invariance route for N-9 | New route R9.6. R_π-invariance is not stated. With the label-sector reading it would turn ρ_P's class I into class R. ρ_T is unaffected, and R_0-invariance does not rescue N-9 (witness ρ_T′, [A]). The qualification is carried into §0, §4.3, §7, O-2 and §9 item 2 |
| 3 (Medium): carrier ranges | §0 and §4.3 state the ranges. ρ_T holds for L ≥ 7, any parity. ρ_P holds for every even L ≥ 2. The class is O for odd L ∈ {3, 5} without the label-sector reading (O-6). The rule is applied per carrier, labelled as a refinement of PLAN §4; for odd L it falls to its third branch |
| 4 (Low–medium): O-5, the L bound for ρ_P | The reviewer's hand argument was checked. A term of q_2 is nonzero on y_0 only if hk_0 ∈ {k_0, π − k_0}, and every such term equals z_{k_0}ᵀz_{π−k_0}. So q_2(y_0) = N cos ψ and q_2′(y_0) = N cos(ψ − 2φ), and the same holds for y_1. ρ_P therefore holds for every even L ≥ 2 and every k_0 ∉ {0, π}, written as [A]. The condition "a(k_0) ∉ {±2}" is shown automatic. The old O-5 is removed |
| 5 (Low): "under any translation-commuting extension" | The test now uses φ = 2π/3. Then w_φ ∈ SU(6), so it acts trivially on the labels under every translation-commuting extension (Lemma L) and lies in Stab(C), with e^{2iφ} ≠ 1. For ρ_T, the stabilizer statements are stated under R_ext |
| 6 (Low–medium): N-c incomplete | The §4.2 table adds rows for lane 2's Theorem 1, H-link, H-cust (kinetic and condensate clauses) and N-1. It covers ρ_T, ρ_P and ρ_T′ |
| 7 (Low–medium): one owner question for two readings | O-1 is split into O-1a (N-2: the clause on V_rest; dropping it weakens H-PF) and O-1b (N-8: the clause extended to the support, citing [FS] §4.2). §2.2 step 3 is strengthened to every function of 𝒢_+. §3.2 states the equivalence in both directions (§A.34), with a reason for offering the trajectory reading. "Its own" is dropped from §0 |
| 8 (Low): §2.2 step 2 garbled | Restated: J_t = iS_t with S_t ≠ diag(1, −1), so J_t ≠ J_F, and J_F is the unique F-positive-frequency structure |
| 9 (Low): the mirror case of Lemma PF | Dropped, with a sentence noting that it would be inconsistent with φ = Φ_n unless Φ_n = 0 |
| 10 (Low): §11 table | Rows added for R8.2, R9.1 (relying on Proposition C), §2.2 step 4, ρ_T on odd L, and the new r2 items. §A.46 item 4 categories are used, and §1 uses PLAN §8's status words ("open" for unstated premises) |
| 11 (Low): §10 tracing | Added Issues #1217, #1169, #1049, #1216 and PR #1624 as provenance, and the owner ruling (#1169 comment 7202075726, item 4) as support on `main` through [FS] PRESERVATION.md. "Merge without squash" is stated as a landing condition |
