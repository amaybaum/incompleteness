# Changes from r2 to r3, with the source of each

## Sources

- Review r2 (sha256 `901787327ba80afaee661c0f12e6f66854a163dae3859820ac8db1caa547c522`): the blocking finding R2-B1
  and its nits.
- The coordinator's r3 instructions.
- One correction the writer found while re-running the checks.

The r1 and r2 files are unchanged.

## Changes

| # | Change | Where | Source |
|---|---|---|---|
| 1 | D402's new text is replaced (both texts below). It no longer asserts one common sufficient condition. It states, in SM:1394, where it is not established whether an entry requires finiteness of the substratum. | `diffs-r3/new-edit-records-D402-D412.json`; §32.9; PROPOSAL-r3 §2 | R2-B1 |
| 2 | D410 is added: the generations entry names its spin-1/2 sectors under H-spin′ (Theorems 9–10) and light-spectrum selection (Theorem 10, SM:460). O-12 is resolved. | same | R2-B1; requirements 2, 5 and 7 |
| 3 | D411 is added: the hypercharges entry names the observed family pattern, the five representations per family, family-universal charges and H-χ′ (Theorem 15; SM:460, SM:555) | same | R2-B1 |
| 4 | D412 is added: the gauge entry names the premises and matter action of the Standard-Model reduction and the further physical input of Proposition 14a (SM:344, :374, :585). It is necessary, because the entry claims the SM group while Theorem 5 gives U(3)×U(2)×U(1). | same | R2-B1 (optional item, included) |
| 5 | The false §32.9 sentence ("does not replace the earlier count by any list of assumptions") is removed. "The wording" states what D402 does. | §32.9 | R2-B1 point 4 |
| 6 | The open-dependency list is the same in §32.9 and the proposal. It adds Lemma 1c's H-μ(φ,Θ) alternative on ℤ^d, Proposition 4b's H-blind route and the normalization of 1/α₀'s vertex coupling. Lemma 1c is not used for the generation count; that row is corrected. | §32.9; PROPOSAL-r3 §2 | R2-B1; review nits |
| 7 | D403 names H-Hawking and "selection of the physical slope remains an additional condition" (GR:88 at T1′) | D403; §32.9 | nit |
| 8 | Item-7 row: one clause that the FULL mirrors are false positives by the ledger's mirror convention (LEDGER.md:304) | §32.4 row 7; §32.9 | nit |
| 9 | The side-change records pin today's `main` blobs. A later change to those paths before `L` needs a post-F record or a re-freeze. | §32.7 | nit |
| 10 | The adoption decision must expressly supersede c.7093128173's clause for these edits. The placeholder is in §32.9, the §32 preamble is reworded, and O-13 is added. | §32 preamble; §32.9; PROPOSAL-r3 §0 | nit (authorization) |
| 11 | The configuration's `adapters.ledger` and `edits` companion pin the new `ledger.json` and `edits.json` digests. r2 left P's digests there. | `diffs-r3/CONFIG-r2-to-r3.diff` | writer, found on re-run |
| 12 | Counts and pins are recomputed: 412 records, 410 splices; `edits.json` `1adaadb9…1778`, `ledger.json` `afbd4d00…bfd` | §32.1, §32.9, §32.10 | consequence |
| 13 | Re-run: P's checkers, item 7 and its controls, duplicate_check, the gate tools (coverage with `.github`), and the TeX rebuild | PROPOSAL-r3 §3; `work-r3/*.out` | coordinator |

## D402, reviewer's text and r3's

**The reviewer's proposed wording (review r2, R2-B1), quoted:**

> they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry
> under the further conditions of the theorem cited for it; whether an entry requires finiteness of the substratum is
> not established where that theorem uses the measure conditions of Lemma 1c or Proposition 4b, the continuum
> conditions of the d = 3 selection (§3.2) or, for $1/\alpha_0$, the infinite-lattice Brillouin-zone integral of §6.1.

**r3's D402:**

> they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry
> under the further conditions of the theorems cited for it; whether an entry requires finiteness of the substratum
> is not established where those theorems use the measure conditions of Lemma 1c or Proposition 4b or the continuum
> conditions of the $d = 3$ selection (§3.2), and $1/\alpha_0$ is the Brillouin-zone integral over $\mathbb{Z}^3$ of
> §6.1, whose counterpart for a finite substratum and whose normalization of the vertex coupling are not established.

**Adjustments, each for accuracy:**

- "theorem" becomes "theorems", because entries rest on several theorems.
- For 1/α₀, the open point is the finite-substratum counterpart of a ℤ³ integral, together with the normalization of
  the vertex coupling.
- "infinite-lattice" becomes "over $\mathbb{Z}^3$", which avoids P's infinity-scan pattern and has the same meaning.
