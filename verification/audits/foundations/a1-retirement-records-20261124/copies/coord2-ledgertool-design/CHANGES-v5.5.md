# DESIGN-v5.5: changes against DESIGN-v5.4

## Inputs and scope

Inputs, each sha256 verified before use:

| File | sha256 |
|---|---|
| `DESIGN-v5.4.md` | a980251709485e7c1b26c91c32a18d8fdf412adb6f6d8058c382892bc29b9cb3 |
| `review-v5.4/review-v5.4.md` (verdict REVISE, V1-V5) | bc0921e37a1d941f3845b200dd90e744dcf0fdd635f8cac7fb2b6ca9d67af854 |
| `review-v5.4/review-v5.4-addendum.md` (C1-C4, draft authority-record shape) | 8559e4336e293a5b879a5154c928fcad209be8e1a1aa37d15ddab459b1059ef3 |

The scope was exactly: V1-V5, C1-C4, and the residual-trust list. The owner decisions of 2026-11-23
applied are numbered 1-5 below and are called R-D1 to R-D5 in the design. Nothing outside that
scope was changed.

The work was paper-only:

- no repository, git or GitHub write, no workflow run, and no host call;
- the Stage 1 worktree was not touched;
- the one new script is `work-v55/parity55.py` (sha256
  06b6f0515ca07e1cd39f2841468af977d11f1e0bf1062d12a55f7b0a58ffd40d), which reads git objects and
  imports P's blob after verifying its hash.

**Correction to my v5.4 report.** In that report I gave the sha256 of `CHANGES-v5.4.md` as
`2c1a3e3c...`. That value was wrong. The file's actual sha256, as `sha256sum` prints it and as
`MANIFEST.sha256` records it, is d1e5c04858050d61a30b3b9135a6a729c4186d3878ffe3b91d129cbac15033a5.
The v5.4 review used the correct value. The values reported for v5.5 are copied from `sha256sum`
output.

## 1. Mapping

| Item | DESIGN-v5.5 sections | What changed | How verified |
|---|---|---|---|
| V1: P's count; offset mapping; chained edits; overlap control | 6.1 (counting, offsets back to `H`, binding); 10.4 S11-58i-k; 14 | See "V1" below the table | `parity55.py`: see "V1" below the table |
| V2 and R-D3: the run's commit | 5 (acceptance); 6.3 (trust root point 3; snapshot); TR29, TR30 | The run's `head_sha` must be on `main`'s first-parent chain of the attested repository, and must contain `A`, the reviewed tool and the pinned workflow. `X`, `C`, `L`, `M`, `H` and `E` are explicit, recorded inputs. They are never the run's `head_sha`, because `X` does not contain the tool. The consumer compares them with the landing record | textual; controls |
| V3 and R-D3: executed code | 6.3 (`engine_pins`, `workflow` requirement, trust root point 3); 5; TR28 | `A.engine_pins` pins every tool file the run executes. The tool and the consumer each read those blobs and the workflow content at the run's `head_sha` through the host API, never from `result.json`. The workflow's reviewed content must check out `head_sha`, verify the pins before executing, and run only that tree | textual; control |
| V4 and R-D2: withdrawal integrity | 6.3 (admission point 3; the freeze ledger; reconciliation; snapshot); 5 (events appended at landing); TR31-TR36 | See "V4" below the table | textual; controls |
| V5: the first line | 6.3 (forms) | The body's bytes up to the first LF, with at most one trailing CR removed and no other normalization | TR37 (CRLF recognized), TR38 (trailing space refused) |
| C1 and R-D4: authority changes | 6.3 ("Authority changes") | See "C1" below the table | TR40-TR44 |
| C2 and R-D4: versioned forms | 6.3 ("The forms") | `oi-freeze/1 designate plan= round= commit=`, `... withdraw ...`, `... supersede ... by=`, and `oi-authority/1 approve from= to=`. Single spaces and lowercase hex. Any owner comment beginning `oi-freeze/` or `oi-authority/` that is not an exact form refuses, unknown versions included. Path `tools/ledger_coverage/authority.json`; schema `oi-tool-authority/2`, with fields as the addendum's draft plus `freeze_ledger_path` | TR38, TR39 |
| C3 and R-D5: durable evidence | 5 ("Durable evidence", "Offline replay"); 6.3 ("The admission snapshot") | See "C3" below the table | TR45, TR46 |
| C4 and R-D1: stricter refusals | 6.1 ("Where the tool is stricter than P") | See "C4" below the table | `parity55.py`, as V1 |
| Residual-trust list | 6.3 ("Residual trust assumptions") | See "Residual trust" below the table | textual |

**V1.**

- "Occurs exactly once" is defined as P's non-overlapping, left-to-right `str.count` on the decoded
  text. A byte-level count over the UTF-8 gives the same result.
- The running copy is defined as segments of original `H` text and inserted images. An occurrence
  must lie inside one original segment. Its `H` byte offset is the segment's `H` start plus the
  in-segment offset, converted by UTF-8 length.
- Chained edits are named as the third stricter refusal and given control S11-58j, plus S11-58k
  for a chain across an image boundary.
- The overlap control is S11-58i: `"aa"` in `"xaaay"`.

Verified with `parity55.py`, against P's own `variant`, a `check`-style application and
`static_new`:

- A1: 401 of 401 edits accepted, and the splices reproduce P's text.
- Crafted cases: the overlap is selected as P does; two chained cases that P applies are refused as
  chained; case (i) and case (ii) are refused.
- 20000 random cases (60% with two variants):
  - 2822 that P applies and that disjoint splices can represent are all accepted, and their splices
    reproduce P's text;
  - 16905 that P refuses are all refused;
  - the only extra refusals are the 273 chained cases.
- In the chained control, with edit 1's splice supplied, the refusal names edit 2 as chained.

**V4.** Admission now reads the edit status and hidden state of **every** owner comment in the
thread. It refuses when any of the following holds:

- an owner comment carrying a form was ever edited;
- an owner comment's edit history ever contained a form's first line;
- an owner comment is hidden;
- an owner comment's edit status is unreadable.

So an edited withdrawal or supersession fails closed. A new freeze ledger, `oi-freeze-ledger/1`,
is an append-only, owner-approved record on `main`; every acceptance landing appends the events its
admission observed. Every admission reconciles the thread with the ledger and with every admission
snapshot committed on `main`:

- a withdrawal or supersession recorded there binds even after its comment is deleted, hidden or
  edited;
- a designation must be present and verifiable now;
- a conflict, or an unavailable or unverifiable ledger, refuses.

What remains is stated as a residual: a withdrawal posted and deleted before any admission
observed it cannot be detected unless the host reports deletion events, in which case any deletion
refuses.

**C1.**

- An authority change takes effect only with an owner approval comment. It must be in
  `A.authority_thread`, read `oi-authority/1 approve from=<old sha256> to=<new sha256>`, be authored
  by the previous `A`'s numeric owner id, and be created before the merge. It is verified like a
  designation: unedited, not hidden, the thread read completely.
- An independent review record must name both blobs.
- An owner-id change also needs approval from the new id.
- The merge is provenance only.
- The first `A` is approved with `from=none` by the id it pins. That is a consistency check, and
  the circular residual is named.

**C3.**

- The landing record commits `result.json.gz`, made with deterministic gzip settings (mtime 0, no
  name, level 9, OS 255). The sha256 of the uncompressed bytes decides; the compressed sha256 is
  recorded too.
- It also commits the full admission snapshot and its sha256, and the reproducibility recipe:
  commits, blobs, command and tool version.
- The events the admission observed are appended to the freeze ledger.
- An offline `replay --snapshot` mode recomputes the result from git objects and the snapshot. Its
  output equals the committed result except `config.admission.mode = "replay"`, and it is never
  acceptable as a new run.
- The design states plainly that only the snapshot's authenticity at acceptance time remains
  host-attested.

**C4.** The design states, per kind, why the input is invalid or ambiguous:

- (i) a splice for the unselected variant writes bytes P's application does not;
- (ii) one splice covering two edits is malformed under the ledger schema's one-edit `id`;
- (iii) chained edits cannot be expressed by disjoint splices at `H`, so such a frozen plan's ledger
  is necessarily inconsistent with its edit list.

The design also states that P's items 5 and 6 are computed and recorded in every case, and that
there is no claim of complete behavioural equivalence. The demonstration that no valid,
unambiguous operation is rejected is the measurement under V1.

**Residual trust.** Added to the list:

- the host runner executing the pinned workflow faithfully;
- who can delete, hide or edit comments in the authorized threads, and what that means for
  undetected deletions;
- the authenticity of the admission snapshot at acceptance time.

Kept:

- the host API and its attestations;
- the access control on `main`;
- the first `A`'s landing;
- the owner's account.

## 2. Consequential edits inside the scope

Each of these follows from a scoped change:

- TR4 now names `A.owner.id`.
- TR11 and TR19 refer to admission point 3, renumbered by V4.
- TR17's near-form example uses the C2 syntax.
- Sec. 0.2 gains the mapping rows.
- Sec. 14 gains the v5.5 measurement paragraph.
- Sec. 15 item 0a is updated for `A`, the freeze ledger and the approval comment.
- Sec. 16.8's control list is updated.
- The durable-evidence bullet of sec. 5 is rewritten. This also repairs a sentence in v5.4 where the
  X11 clause had been run into the evidence paragraph.

Nothing else changed. `diff DESIGN-v5.4.md DESIGN-v5.5.md` has 25 hunks, and the document grows from
2759 to 2929 lines.

## 3. Not adopted, by scope

The v5.4 review's optional O1 and O2 were not adopted. O1 is one plan per thread. O2, about
compression, is replaced by C3.

## 4. What I could not follow or verify

- **The host's semantics were not exercised; no host call was made.** That includes:
  - whether edit history (`userContentEdits` with content) reveals every edit and every earlier
    first line;
  - how hidden comments are reported;
  - whether deletion events are exposed;
  - comment counts, `merged_by` and fork status;
  - whether the run record's `head_sha` and the file contents at it are what the runner executed.

  Each is specified fail-closed, and each is named as a residual where it cannot be.
- **Deterministic gzip output depends on the compressor.** The design therefore makes the sha256 of
  the uncompressed bytes decisive.
- **The freeze ledger and its procedure are my construction under R-D2.** The owner gave one as an
  example, and the owner may want another form.
- **No v5.5 implementation exists.** The controls are specified, not run.
- **Comment ids are held for none of the owner decisions.**
