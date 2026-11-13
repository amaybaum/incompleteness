# WAVE-SIGN-1: downstream wording disposition

Paper-only source audit by Codex, 2026-11-09; submitted for separate
independent review. Planning home: #1193. The
[bounded continuation](https://github.com/amaybaum/incompleteness/issues/1193#issuecomment-6739175078)
is authorization provenance, not mathematical evidence. This packet proposes
wording; it edits no manuscript, Lean definition, proof, probe or prior record.

Source snapshot: main `fd539e150759a6ea51ab279aeeac80fc06050ade`.
The accepted source assessment is `ASSESSMENT.md` in this directory, available
at that snapshot. Its calculations are restated below where needed.

## 1. Disposition

Preserve Main's binary display and general minus-memory rule. Main:294 fixes
`q=2`, where the two signs agree; Main:726 item (xiii) explicitly posits the
general minus-memory update and identifies the display as its binary instance.
No new odd-characteristic rule needs to be chosen to interpret those passages.

The four downstream surfaces in the review's propagation note do need a
documentary correction: they infer a necessary memory coefficient from
bijectivity. That inference is false. The existing minus-memory construction
and its proved properties can be preserved. Recommend a separately scoped
minimum correction and keep #1193 open pending owner disposition. No source
correction or closure is authorized by this audit.

## 2. Hand check of the necessity claim

For previous/current coordinates `(p,c)` and an invertible linear map `D`, set

```text
T_D(p,c) = (c, F(c) + Dp),
T_D^-1(a,b) = (D^-1(b - F(a)), a).
```

Substitution in either order gives the identity, for any fixed `F`.
In particular `D=+I` gives a bijection over any additive abelian group;
over odd characteristic it differs from `D=-I`. Hence the word
"bijective" cannot force `D=-I`. For the selected minus-memory class the
inverse is `(F(a)-b,a)`, exactly the class used by `leap`.

A proposed replacement must not silently substitute "time-reversal symmetry
forces" for "reversibility forces". With linear `F(c)=Ac`, slot reversal
`R(p,c)=(c,p)` yields

```text
R T_D R(p,c) = (Ap + Dc, p),
T_D^-1(p,c)  = (D^-1 c - D^-1 Ap, p).
```

Equality requires `D^2=I` and `(D+I)A=0`. Minus memory suffices for every
`A`, but plus memory also satisfies this reversal when `A=0`.
Neither this calculation nor a conditional wave-equation theorem is a
physical derivation selecting a native rule. The safest minimal wording
states the branch's existing assumption directly.

## 3. Checked anchors and proposed minimum wording

All line positions below are at the source snapshot. Each proposal replaces
only the offending inference, preserving the displayed update and its scope.

| Surface and source blob | Classification and evidence | Proposed wording |
| --- | --- | --- |
| `papers/SM.md:312`, blob `611305ab172c8d7e9a42b88a015b744fd8e97e1b` | Genuinely inconsistent as a necessity claim from bijectivity: "Reversibility requires D=-I_K" is contradicted by section 2. The surrounding paragraph explicitly concerns the observer-level branch. | Replace "Reversibility requires $D = -I_K$" with "The selected minus-memory branch sets $D = -I_K$". |
| `book/ch05-gauge-structure.md:99`, blob `400b00393c5ee625daa75a479fd00cfe232952c7`; exact FULL mirror at `:1417`, blob `9eda7811100df71a661a0bbe7e819e35e1e103df` | Same false necessity claim: "reversibility forces the previous-step coefficient to be -I_K". The two paragraphs are byte-identical. This is one source passage and its required mirror. | Replace that clause with "the selected minus-memory branch has previous-step coefficient $-I_K$" in both sources. |
| `verification/lean-mathlib/OIBridge/SecondOrderCircuit.lean:6-10`, blob `4eacbb0910dd7b9002640847a7bb4929ca7b92b9` | Genuinely inconsistent prose: "only the value -1 makes the phase-space map a bijection" is explicitly false. The definitions at :47-68 instead assume the minus class, and the involution/factorization results concern that specified class. | Replace the two explanatory sentences beginning "Reversibility is what forces" with "This file takes the minus-memory second-order form as given and shows what it implies about the one-step map as an automorphism." Preserve definitions and proofs. |
| `verification/lean/bohr_frequency_probe.py:10008-10009`, blob `c6b592eb3b0bbc188ea4d78b875417919abea70d` | Misleading explanatory comment: it repeats the false necessity assertion. The displayed `leap` at :10011 is the selected minus rule. This audit inspects text, not probe behavior. | Replace the two comment lines with "The selected minus-memory second-order branch has D = -I_K, so its phase-space map on per-site state (prev, cur) is". Preserve executable bytes. |

Main's anchor blob is `5b73da5743f39aef080d02cc0a06bcaab4704f9f`.
`OI_Time_Reversal.lean` (blob `ded1b50bbd58ec2dc090c7a79dcf39bd7749fe37`),
especially :99-138, correctly states and proves a reversal property of the
specified minus-memory equation. It needs no correction for this finding.
SM:224-228 already begins with the minus-memory ansatz; that is not an
independent derivation of the sign and does not need a sign change.

## 4. Consequences and correction boundary

Phrase/paraphrase searches across papers, book and verification sources also
find these retained records:

- `verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md:1095-1105`,
  blob `7f8a142be31222b1aee74b05990bb58648387cae`: the discrepancy marker
  overlooks Main's binary scope and its general posit. The existing assessment's
  section 5 supplies the minimal proposed qualification. Its sign-dependent
  algebra remains scoped to the chosen minus-memory model.
- `verification/audits/physical-realization/continuous-time-audit.md:40`,
  blob `720db0dde09c77eb90e766445384a6bb645a2c0b`: repeats the false
  "reversibility forces" inference; any corrective unit must address its status.
- `verification/programmes/substratum/a6-instantiation/result.md:76`,
  blob `3d2b4b9ebc24a3a65172ad9384b8da7d8ca03634`: quotes the old SM
  sentence while describing the selected second-order term. The legacy manifest
  freezes this file. Keep it unchanged; a correction of its interpretation must
  follow the applicable forward process and preserve the valid branch result.

These are propagation findings, not permission to edit records or adopt a new
scientific premise. A future correction must check native-record immutability,
incoming citations and exact-text guards before editing; absence from the
legacy manifest alone does not establish mutability. The independently proved
properties of the specified minus-memory map are not refuted by this finding.

The manuscript correction, if separately authorized, would require the SM and
book publication artifacts, book/FULL parity and affected mechanical guards.
No generated publication artifact changes are needed for this packet itself.
Physical sourcing of the minus-memory model remains separate.

## 5. Verification and next gate

Source inspection, blob/line checks, exact book/FULL paragraph comparison,
corpus phrase searches and the explicit hand substitutions above support this
audit. No scientific program, enumeration, simulation, Lean build, workflow
dispatch or native stage was run. Ordinary repository CI is compatibility
evidence only. Independent exact-head review precedes the owner decision on
the proposed documentary correction and retained-record disposition.
