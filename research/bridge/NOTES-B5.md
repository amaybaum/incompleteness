# NOTES-B5 — the exact content: the weakest H-level principle that supplies A_miss

Node B5 of `research/bridge`. It synthesizes B1–B4. No new computation; evidence pointers are to `b1`–`b4`, [A]
records and [K] at L. Base L = `9f9f8257`.

## 1. What the hidden level provides and what it does not

| H-level item | supplies (b)? | evidence |
|---|---|---|
| the constraints of the realization theorem and branch (a), as listed in NOTES-B4 §1: Lemmas 1–3, Axioms 1–2, context-independent implementation (Main.md:550 (3)), operational no-signalling, branch (a) parameter dependence (Main.md:392), the native gate and NOTs as hidden permutations | **no**: K(Z_F) is realized exactly with all of them | B4 R1–R13 |
| `EmbeddedObservation` and `ObserverRecursion`, transcribed | **no**: K(Z_F) satisfies them with a fully drivable token | B2 E1–E2 |
| locality of registers (product registers, local readout, `π × id`, measurement independence) | yes, (b_H) is a theorem | B1.1 |
| ↳ but it is Bell-local and realizes no candidate cone, `Q3` included | — | B1.2: `S(phiW) = 14/5` |
| every operation realized with `cnot` on a fixed finite pair substratum, or on a directed tower of them, with (b) granted for all | **never sufficient** (finite group: exotic cone survives) and **never contains** `R1`, an off-frame circle, or two non-commuting circles | B3.1, B3.2 [W + A + L + X] |
| availability in context (A) of a token operation `g`, with RESPECT and product behaviour | **yes**, exactly (b) for `g` | B1.1; violated by the K(Z_F) realization exactly here (B4 R11) |

## 2. The weakest H-level principle

**Statement (H-OI_g).** For the single token operation `g`, the hidden intervention that realizes `g` on an isolated
token remains available when the token is embedded in a pair with the native gate present. "Available" means applied
in the pair context by one fixed map, the same in every context. Its realized pair statistics are those of the idle
extension: (W) RESPECT and (P) product behaviour, which hold in branch (a) by no-signalling and local tomography.

**It supplies A_miss** with H1–H3 for each of the following choices of `g`. Each is a single generator, or a single
generator together with its J-conjugate.

| `g` | why it suffices | evidence |
|---|---|---|
| `R1`, order 3 about (5,1,1), `(1/9)[[8,1,4],[4,−4,−7],[1,8,−4]]` | `(b_R1)` forces `Q3` with `cnot` | stage 4 Y7 [A]. The weakest found: one operation of **finite** order |
| one rational rotation of infinite order about an off-frame axis, e.g. axis `(3/5, 0, 4/5)` with `cos θ = 3/5` (rational by Rodrigues, `tr = 11/5`) | by closure, (b) for one rotation equals (b) for its circle (B3 §3); one off-frame circle forces `Q3` at level (ii), i.e. with G16 invariance | stage 4 S3[n] [A]; at level (i) the axis must also be neither parallel nor perpendicular to the gate axis [A] |
| `{R_z(θ), R_x(θ)}` with `cos θ = 3/5` | this is A_miss as two rational matrices | B3 X5 [W + X] |

**Status.** Assumed. It is OI⁺-1 (GR.md:228; `HasParallelReferenceExtension`, ReferenceExtension.lean:447) restricted
to one operation and read at the hidden level.
- **Not derived** from anything at L. The kernel at level M has `redundancy_fails` (ImplementationLocality.lean:207)
  and `oiPlus_independence` (CompletedOI.lean:506).
- **Not derivable** from the framework's stated H-level constraints: B4 gives an exact realization satisfying all of
  them and violating H-OI_g.
- **Not realizable** for `R1` or an off-frame circle on any finite or locally finite pair substratum carrying `cnot`
  (B3). The principle can therefore hold only at a non-locally-finite level: the completed pair, with stage-crossing
  operations. That level is exactly where F-D3 places the drive's generator.

**Disguise test: FAILS.** At level H it is the spectator clause for `g`. Through Theorem B1.1 its transcription to `W 3`
is (b) for `g`, which restates I3.150–I3.153 and I3.165's clause "local actions compatible with the composite cone".
Tested against K(Z_F): K(Z_F) violates it for every `g` above, by exact witnesses:
- `S`: `−1/8`;
- `cyc3`: `−1/8`;
- `R_z(θ)`: `−1/10`;
- `R1`: `−79/720` (new);
- every axis: the flow law `−sin t/8` [A, T6 t5].

**Candidates that pass the disguise test, all P-level and none at L.**
- λ, four-token coherence with `tok`: [D].
- Pair homogeneity H, I3.160.
- Extreme-ray transitivity T, I3.161.

B4 §4(d) shows that preparation reachability belongs to the T/H family. At the finite level it is self-defeating.
L-REG passes the disguise test but excludes the target.

## 3. The theorem at L that would close the gap

**(i) The bridge, provable: an H→P lemma.** Formalized at L, Theorem B1.1 would be the first H→P bridge declaration:

> for a finite hidden pair model `(Λ, 𝒫, R)` with `R(𝒫) ∋` all products, and a hidden bijection `Π` that satisfies
> RESPECT on `𝒫`, maps products as `actC O`, and preserves `𝒫`: `actC O (cone R(𝒫)) ⊆ cone R(𝒫)`.

- Level: H→P.
- Proof: elementary (B1 §2).
- It discharges no obligation by itself. It **relocates** K2's local-action clause (I3.165; ROADMAP.md:1001–1005) to
  the hidden-level premise (A).
- Its value is to make the relocation a theorem rather than a reading.

**(ii) The premise, not provable at L.** With (A) for one sufficient `g` the gap closes:

> **K2-local (discrete form).** For every closed `K ⊆ W 3` with `CandidateCone K` (K2Guard.lean:95), `cnot K ⊆ K` and
> `K = K*` (H3), `actC R1 K ⊆ K`.

Equivalent single-generator forms use `{R_z(θ), R_x(θ)}`, or one rational off-frame rotation.

- Level: P.
- It discharges K2's clause "local actions compatible with the composite cone". Together with K∞-Act and K∞-Drive
  (I3.168, I3.169: availability of `g` on the token), it gives `K = Q3` [A, stage 4].
- **As a universal statement it is false at L's premises.** K(Z_F) satisfies every premise at L that reaches the pair
  cone (T6 §4) and violates it, with witness `−79/720` for `R1` (b3 X7).
- It can enter L only as an adopted premise, which fails the disguise test, or as a consequence of a premise that passes
  it (λ, H, T; none at L).
- The hidden level adds no third way. Its only route is (i) together with (A) = H-OI_g.

## 4. Reading

The question was what embedded observation adds, at the hidden-history level, that L lacks at the pair level.

**Answer: one thing, and it is the missing clause itself.** The availability, in the pair context, of a token's
intervention. Every other H-level structure falls into one of three groups:
- satisfied by the exotic pair (B2, B4);
- incompatible with every candidate pair, `Q3` included (B1, L-REG; B4 §4(d), finite-level PR);
- unable to carry the needed operation at all on finite or locally finite substrata (B3).

The composite action (b) is **independent of every embedded-observation principle stated in the corpus**:
CONDITIONAL on H-OI_g, which is OI⁺-1 at level H for one off-frame operation, and unsourced.
