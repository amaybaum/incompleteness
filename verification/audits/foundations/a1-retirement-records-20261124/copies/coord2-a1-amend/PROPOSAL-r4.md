# A1 plan amendment proposal, revision 4

## 0. Status

**Paper-only, provisional.** Nothing is authorized. PROPOSAL-r2 §0 and PROPOSAL-r3 §0 still apply: the inputs, the
owner's instructions of 2026-11-24, the dependency on tool design v6.0e, the adoption decision O-13 and the
boundaries.

**What r4 answers.**

- **Review r3.** `review-r3/review.md`, sha256 `ab30b1a79d0376c44eb5e6532e3d7054db5c6a440a27abbf3f8ae79261f43ff9`,
  rejected one clause of D402 (R3-B1) and confirmed everything else.
- **The owner's O-13 request of 2026-11-24.** It is quoted in `O13-INVENTORY-r4.md`. It asks for an inventory and the
  decision wording.

Each change is mapped in `CHANGES-r3-to-r4.md`. The r1–r3 files are unchanged.

**Still pending.** An independent review of r4, including `O13-INVENTORY-r4.md` and `O13-DECISION-DRAFT-r4.md`.

## 1. Changes from r3

| Item | r4 |
|---|---|
| D402, the 1/α₀ clause (R3-B1) | "…and $1/\alpha_0$ is the Brillouin-zone integral over $\mathbb{Z}^3$ of §6.1, whose…" becomes "…and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose…". This is the reviewer's wording. SM:683–685 and :689 show that 1/α₀ = 6 × Π_s(0) × 4π, computed from a loop integral ∫d⁴q over four directions. |
| Correction of r3's stated reason | P's infinity scan matches "infinite lattice", but not "infinite-lattice" (review r3). r3's reason for avoiding that phrasing was mistaken; r4 uses the reviewer's wording. |
| §32.9 | The 1/α₀ table row and open-dependency item 4 are corrected in the same way. The A1 column now reads "No use of A1 found in the cited derivation(s)", with a sentence that this is not a statement of independence from A1 (owner, O-13 request). |
| D403 | "H-slope" becomes "H-slope on identified transitions", verbatim from GR:88 at H and at T1′ (optional review nit, applied). |
| Item 7 negative controls | Extended to NC1–NC5: the SM:1394 phrase; ch09:137's count; "Fourteen items, …"; a bare "(finite under A1)" pointer; "sixth of". |
| Configuration | `adapters.ledger` and its `edits` companion pin the r4 digests |
| O-13 | `O13-INVENTORY-r4.md` (new) and `O13-DECISION-DRAFT-r4.md` (new) |
| Counts and pins | 412 edit records; 410 splices in 44 files. `edits.json` `19eb79bd478275110b4ff1cd3ae2271c37574e849d45be272f53b8e75e726b4b`; `ledger.json` `d20495f0084f29ac5c58c5a0480be5f0ed342334381e6680e9cca58952940976` |

## 2. Final D402 and D403

**D402** (`papers/SM.md:1394`, part 1).

Old:

> they hold for every bijection satisfying the six structural properties.

New:

> they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry
> under the further conditions of the theorems cited for it; whether an entry requires finiteness of the substratum
> is not established where those theorems use the measure conditions of Lemma 1c or Proposition 4b or the continuum
> conditions of the $d = 3$ selection (§3.2), and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1
> over the whole Brillouin zone, whose counterpart for a finite substratum and whose normalization of the vertex
> coupling are not established.

**D403** (part 2). New:

> hold for the same class as consistency relations conditional on H-count, which includes finiteness of the total
> system and a conserved energy shell, and on H-slope on identified transitions, H-frame, the H-Hawking horizon and
> frame conditions, local boost structure and the symmetric detailed-balance rate ratio, with selection of the
> physical slope an additional condition ([GR §2.3, §3.2, §4–§5, §8.5])

D404–D412 are unchanged from r3; the texts are in `O13-INVENTORY-r4.md` Appendix A.

## 3. Checks (re-run for r4)

The sandbox and scripts are in `work-r4/`.

| Check | Result |
|---|---|
| `preserve_check --build-ledger` | 410 splices in 44 files. The 399 P splices are byte-equal, and the 401 P records are unchanged. |
| `edits_check --static` | PASS (the infinity scan on the new texts finds 0 hits; register, capitals and identifier 0; mirror parity 0; sitemap 194/194) |
| `--commit H --simulate` | PASS (412 unique; residual 5, all allowed; criterion-5 0; identifier and count 0) |
| `--pins` | PASS |
| `--repo-scan --simulate --final` | PASS (0 unexplained) |
| `edits_check --self-test`; `preserve_check --self-test` | PASS; PASS |
| `preserve_check --verify-ledger` | re-derived identically |
| `preserve_check --verify-pins` with the r4 PREREG | PASS (0 pin findings) |
| Item 7 as frozen, on H with the r4 ledger | count grep 0 lines; pointer grep only the 4 ledger false positives; PASS |
| NC1–NC5 | each FAIL, as required (NC4 through the pointer clause) |
| `duplicate_check` on the 4 edited sources and on the r4 PREREG | OK; OK |
| Gate tools (coverage, claims, voice, citation_roles, dependency_label, baseline_label) on H and on H with only D402–D412 | identical output and exit status; coverage reports 132 statements |
| `staleness_check` | STALE for SM and the book, as expected |
| TeX (base control reproduces H) | SM.tex sha256 `96176b436d188baf2276d2551baa6c0c4e614a40350d571cc47e401b7970efdb`. FULL.tex is unchanged (`5d37cafc…`). Each differs from T1′ only in the edited paragraphs and the stamp. |
| PREREG r4 | pure append; the last of 13 `Record pins` headings is §32.10; both parsers read 6 rows |

**Not run.** `guards_check` and SC-42, which belong to the gate; PDFs; CI.

## 4. The O-13 inventory and decision draft

- **`O13-INVENTORY-r4.md`.** It covers each edit and each prediction it touches: verbatim old and new text, the
  splice hashes, the categories (E/N/H/A1/U), the supporting lines at H, and whether the claim is strengthened. Every
  answer is "no", with its evidence. The only conclusions whose existing derivations require A1 are the action scale
  and the Bekenstein-Hawking 1/4, through H-count.
- **`O13-DECISION-DRAFT-r4.md`.** It adopts exactly D402–D412 by their byte hashes and the r4 digests. It supersedes
  c.7093128173's "or any scientific conclusion" for those exact edits only. It keeps H, the 399 splices and every other
  conclusion protected. It authorizes nothing else.
