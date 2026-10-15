# F2-1 correction 1 (2026-10-15): the square-root scans cover the spectral roots

Append-only correction to `../RESULT.md`, raised in owner review. `RULES.md`, the amendment,
`RESULT.md`, `review/`, `e1_exact.py` and its output are unchanged. The exact check is
`root_scope_check.py`, which imports `../e1_exact.py` by path and changes nothing in it.

## What the scans covered

Amendment A1 defines the square-root scan as "every square root of the whole-step operation modulo
a global phase (one sign choice per eigenspace)". That family is the set of **spectral** square
roots, the functions of U_0. Three passages of `RESULT.md` say "every square root modulo global
phase" for it:

- the square-root scan of C3(c2);
- the negativity scan of C4(b);
- the operator-Schmidt ranks in finding 1.

Each is to be read as "every spectral square root modulo global phase".

**Why the family is smaller [W].** A square root V of U commutes with U = V², so it preserves each
eigenspace E_λ of U and squares to λ there. Hence V restricted to E_λ is √λ R_λ, where R_λ = 2Q − 1
for any projector Q inside E_λ. The spectral roots are the cases R_λ = ±1. They exhaust the square
roots exactly when every eigenspace is one-dimensional; otherwise the square roots form a
continuum.

## Exact results

| (q, N) | eigenspace dimensions of U_0 | spectral roots exhaustive | symplectic S with S² = J′_N | stabilizer rays V\|0⟩ for some root / for a spectral root |
|---|---|---|---|---|
| (3, 1) | 1, 1, 1 | yes | 0 of 24 | 0 / 0 of 12 |
| (5, 1) | 1, 1, 2, 1 | no | 0 of 120 | 0 / 0 of 30 |
| (3, 2) | 3, 2, 2, 2 | no | 12 of 51840 | 10 / 0 of 360 |

How the columns are decided:

- **Clifford roots [W from an exact count].** A Clifford V with V² ∝ U_0 has a symplectic part S
  with S² = J′_N, the linear part of the zero-coupling leap. Conversely, such an S gives a Clifford
  square root after rephasing. Sp(2N, q) is enumerated in full.
- **Stabilizer rays.** These are the Clifford orbit of |0…0⟩. A ray is reachable when ψ ∝ V|0…0⟩
  for some square root V. On each eigenspace of dimension at least 2, R_λ v_λ ranges over the
  vectors w with ⟨w|w⟩ = ⟨v_λ|v_λ⟩ and ⟨v_λ|w⟩ real; this is reflection through the line of v_λ + w,
  with −v_λ coming from R_λ = −1.

Controls (all PASS):

- the reachability test reports each spectral root's image reachable, in both modes;
- it finds C|00⟩ below;
- every reached ray has a nonnegative Wigner function;
- the spectral-only count agrees with the explicit spectral roots.

At (3, 2), where U_0 = U ⊗ U with U the one-site image, two square roots fall outside the scanned
family:

- **V ⊗ V, with V the principal root of U.** It is not proportional to any spectral root. It is a
  product of one-site gates (operator-Schmidt rank 1). It is non-Clifford, and the Wigner function
  of V ⊗ V|00⟩ is negative.
- **C = (U ⊗ 1)·SWAP.** C² = U_0 exactly, and C is not proportional to any spectral root. It is
  Clifford (operator-Schmidt rank 9), C|00⟩ is a stabilizer state, and its Wigner function is
  nonnegative.

## The three passages, narrowed

1. **C3(c2), square-root scan.**
   - At (3, 1) and (5, 1) every square root of U_0 is non-Clifford: no S ∈ SL(2, q) squares to J′.
   - At (3, 2) the scan's result holds for the spectral roots only. C is a Clifford square root
     there.
2. **C4(b), negativity scan.**
   - At (3, 1) and (5, 1) no square root maps |0⟩ to a stabilizer state, so V|0⟩ is Wigner-negative
     for every square root (Gross's theorem at odd prime dimension [L]).
   - At (3, 2) the scan's result holds for the spectral roots only. Ten of the 360 stabilizer rays
     are V|00⟩ for some non-spectral square root V, C|00⟩ among them.
3. **Finding 1, Schmidt ranks.**
   - The ranks 2 and 3 are those of the spectral square roots. V ⊗ V is a square root of rank 1.
   - The statement about T as frozen, the principal logarithm of the composite image, is unaffected:
     T selects the principal root, which is spectral.

**Unchanged.** Every token and the verdict concern the named canonical principal root and its
global-phase scan. Both consist of spectral roots, so neither is affected. Nor is the supporting
density argument, which uses g = V·X_1 with V principal.

## Consequence for the continuity hypothesis

The uncoupled two-site update does not determine its half-period gate. Among its square roots are a
product of one-site gates and a Clifford gate. Non-locality and the non-Clifford property of the
half-period gate are therefore properties of the root a continuity rule selects, not of the update.
A statement of continuity has to fix that selection, or state results that hold for every
admissible selection.

## The literature step (Campbell–Anwar–Browne, Appendix D)

The owner read the arXiv HTML of the appendix (2026-10-15). By that reading:

- the appendix treats n qudits of odd prime local dimension d;
- it establishes density, up to a global phase, from the full n-qudit Clifford group together with
  a non-Clifford gate;
- it therefore covers (3, 2), two qutrits of total dimension 9.

This resolves the scope qualifier on C3(c3) at N = 2 and finding 4 of `RESULT.md`. The reading is
the owner's. arxiv.org does not resolve from this environment, so it was not re-checked here.

**Not settled here: whether the measured (c1) and (c2) meet the appendix's hypotheses as the
appendix states them.** As measured:

- (c1) is the full Clifford group modulo phases, of order q^{2N}·|Sp(2N, q)|;
- (c2) is a named gate that does not normalize the Weyl group.

## Provenance

| file | sha256 |
|---|---|
| `root_scope_check.py` | `7c6ed2a053ebeb85f002cb261bf2791dc84293f056d082ba9883cd68deb471f7` |
| `root-scope-check-output.txt` | `1e93218097d4604389f3ac475bab0e931462380179bf993d56a332a65efd2610` |
| `../e1_exact.py` (unchanged) | `e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6` |

`python3 -I root_scope_check.py` was run twice, about 17 s each, standard library only, and the
two outputs are byte-identical. These are local runs, not `check-run` attestations.
