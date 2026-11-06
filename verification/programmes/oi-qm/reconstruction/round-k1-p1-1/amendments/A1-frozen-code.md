# A1. Code freeze: rulings, fixture interface and synthetic fixtures (draft)

**Status.** Draft amendment to the K1-P1-1 control plane, before `F`. WIP / UNVERIFIED. It freezes no code: §14's freeze
table is completed by a revision of this file before `F`, under the owner's authorization (b) of preregistration §13,
which has not been given. It authorizes nothing listed in §19.

**Governs:** preregistration §4 (PR-CR6's pass condition, Q26), §6 (R9 and CLASS, output conventions only), §8.1
(declared inputs), §8.4 item 3, §9 (CC-PART's sub-tests and CT-INC), §10.1 to §10.4, §11.1 (S0 failure, Q5), §11.2,
§11.3, §13 (X5's command), §15, and §19 ("Text and scope"; Finding 10's categories). It
settles the open questions Q1 to Q31 of the stage-2 independent static review and the synthetic-fixture review's
requirements (§17). Under preregistration §2 ("Precedence") it governs procedure and outputs only. It changes no gate,
token, control, hypothesis or decision of `K`, and no member, member order, row set or count. Where this amendment and
the preregistration differ, this amendment governs.

**Companion files**, part of this amendment: `A1-fixtures.md` (fixture definitions and hand derivations) and
`A1-fixtures.json` (the same fixtures in machine-readable form). `A1-fixtures.json` has SHA-256
`691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85` at this revision.

## 0. Authority

Quoted with author and time, as preregistration §19, Finding 12, requires for authorization (a).

**Authorization (a), code drafting.** amaybaum, Claude Code session chat, 2026-11-06, recorded in #1031 comment
6677496553 (2026-11-06T05:11:18Z), item 1:

> **1. #1031 — Stage 2 approved.** Authorize Stage 2: pre-F code drafting, under these boundaries: Three independent
> writers prepare implementation A, implementation B and `controls.py`, using the reviewed control plane and separate
> staging branch. Only static analysis and predeclared synthetic-fixture tests are permitted. No computation on the K1
> instance, its dynamics or its states. Preserve implementation independence, distinct methods, exact arithmetic,
> complete member enumeration and the fixed decision rules. Record all code provenance, hashes, hand-offs and permitted
> test commands. Obtain independent static and synthetic-fixture reviews before proposing a code-freeze amendment. The
> review's nonblocking checkpoint clarification concerning Finding 12 should be included in the next permitted
> documentation revision. Not authorized: `F` designation, K1-instance enumeration, scientific execution, workflow
> dispatch, `E`, merge or theorem promotion. Each retains its separate gate.

**Rulings for this amendment.** amaybaum's 6 November 2026 session handoff, as summarized in #1031 comment 6678956167
(2026-11-06T06:44:11Z), which describes itself as "a summary of the decisions in the handoff"; section "K1-P1-1 pre-F
amendment (#1031, #1135)":

> - The proposed Q1–Q29 readings are the working basis for amendment drafting. This handoff records the following
>   specific readings. The full Q1–Q29 table still needs to be recovered from the prior session for an exact amendment.
> - Q4: use JSON `null` for the union-clause field where the frozen schema requires an absent token, retaining the
>   distinct union-reached stop.
> - Q6: option (i), explicit frozen `--fixture` subprocess entry points for A and B. B's earlier SF-1/SF-2 harness run is
>   exploratory synthetic-fixture evidence. Repeat using the approved interface to qualify.
> - Q18: the amendment drafter proposes deterministic rendering, a schema, structured exit statuses and negative
>   fixtures.
> - Q26: strict PR-CR6. A `δ₀` row passing G5 fails the preserved-result control.
> - Independent agent contexts under one coordinator are acceptable as internal model-independent replication, with
>   inputs, shared dependencies and hand-offs disclosed. These are model reviews.
> - Preserve the three writers' separate staging branches. Consolidate byte-pinned reviewed deliveries on one
>   integration staging branch before proposing `F`.
> - Authorized here: amendment drafting and independent review, and rechecking the three revised code files under the
>   Stage 2 limits. The final code freeze, `F` designation, computation on K1 states, workflow dispatch, `E` designation
>   and merge each remain outside this authorization.

**Writer.** amaybaum, Claude Code session chat, recorded in #1031 comment 6680770304 (2026-11-06T08:37:17Z): "Yes take
over as writer for everything now". The same record states: "It grants no merge, F or E designation, dispatch,
scientific execution or theorem promotion."

**Authorization (b)**, approval of this amendment and of any revision of the preregistration before `F`, has not been
given. The revision that completes §14 quotes it with author and time (§15).

**The Q1–Q29 readings.** The handoff names them as the working basis and notes that the full table had to be recovered.
They are the proposals of §4 of the independent static review (§17, `STATIC-REVIEW.md`). That review and the
synthetic-fixture review (`FIXTURE-REVIEW.md`) are held off-repository by the coordinator and are not on `main` or on
GitHub. This amendment states each reading in full in §2, so no ruling here depends on either file's text, and the
owner's approval under (b) adopts this amendment's text itself; the two reviews remain provenance (§A.42 item 8). Where the owner gave a specific reading (Q4, Q6, Q18, Q26),
it is applied as given. A ruling below marked **drafter's proposal** goes beyond the static review's proposal. It is
offered under the Q18 ruling or as the means of carrying out an adopted reading, and it needs the owner's approval with
authorization (b) (§16 lists them).

## 1. Classification used below

- **Owner ruling**: the owner's specific reading, quoted in §0.
- **Working basis**: the static review's proposal, adopted under the owner's ruling that the Q1–Q29 readings are the
  working basis.
- **Already determined**: the preregistration settles it; the determining text is quoted.
- **Drafter's proposal**: specified by this amendment, for the owner's approval with (b).

## 2. Rulings on Q1 to Q31

### Q1. G7 of a row that passes G5 at `rows` (working basis)

Preregistration R9: "Without the adversarial record the row's G6 and token are "pending"." §10.2: "Each value is
"pass", "not-reached", "pending" or a row token." RD-8: "Once G2 has been evaluated and an earlier gate determines the
outcome (R5a), G3 to G7 are recorded `not-reached`."

**Normative text (adds to R9).** At stage `rows`, a row that passes G5 records `gates.G6 = "pending"`,
`gates.G7 = "pending"` and `token = "pending"`, and carries its `usefulness` object (§10.2: "For a row that passes G5, it
is an object…"). RD-8's `"not-reached"` does not apply: no earlier gate has determined the outcome, and G7, the gate that
writes the token, is waiting on G6.

### Q2. G7 of a row whose G6 issues UNDECIDED(G6) (working basis)

`K` line 183: "a row takes the token of the first gate that issues one." RD-8: "These are RD-2's grounds applied to G1
and G2."

**Normative text (adds to R9).** At stage `final`, a row that passes G5 and whose adversarial token differs from A's and
B's agreed token records `gates.G6 = "UNDECIDED(G6)"`, `gates.G7 = "not-reached"`, `token = "UNDECIDED(G6)"`,
`usefulness = null` (not a positive, §10.2), and `hypotheses = Λ` (the row reached G5). This applies RD-2's and RD-8's
grounds to G6; it changes no token value.

### Q3. `union_clause_reached` while a branch is pending (working basis)

CLASS: "computed only when the row set is complete … and no row of the branch is pending; "pending" otherwise."

**Normative text.** For a branch whose class token is `"pending"`, `union_clause_reached` is `false`: the union clause is
reached only by the class computation, which does not run while a row is pending.

### Q4. The class token when the union clause is reached (owner ruling)

CLASS: "If every member row is a positive: emit union_clause_reached = true and no class token (stop condition H3,
against PR-CR6)." §10.2: "an absent value `null`."

**Normative text.** When every member row of a branch is a positive, `class_tokens[b]` is JSON `null` (the key present)
and `union_clause_reached[b]` is `true`. This is stop condition H3; PR-CR6 fails. `null` occurs in `class_tokens` in this
case only, and a `true` union flag occurs only with a `null` class token.

### Q5. S0 failure at `rows` or `final` (working basis)

§11.1: "A computed S0 part that fails gives VOID[stage] under `K`'s §5.4: no row or class token is issued." §10.1: "2 for
a refusal (a stage precondition, or CT-INC)".

**Normative text.** At `members` (**drafter's proposal**, §16; neither the static review's proposal, which concerns
`rows` and `final`, nor the reconstructed table's unqualified "S0 failure exits 2"), A and B write the gate table with
the failing control's `outcome` `"fail"` and exit 0, so that the failure is kept as structured data; `controls.py run`
records PR-S0 `fail`, exits 1, and writes only the checks file (H10). At `rows` and `final` (working basis),
an S0 control that A or B computes as failing is a stage-precondition refusal: exit 2, nothing written. All of A's and
B's refusals exit 2 and write nothing, so their order among themselves does not affect any output. `controls.py`'s
refusal order is §6's.

### Q6. Synthetic fixtures (owner ruling: option (i))

§11.2: "Fixed, with hand-derived answers, in the code-freeze amendment. … `controls.py self-test --synthetic` runs them."
§11.3: "the implementations carry no test hooks." §8.1: "`controls.py` imports neither implementation: it runs each with
`python3 -I` as a subprocess and reads its output file."

**Normative text.** A and B each carry the frozen `--fixture` entry point of §5. `controls.py self-test --synthetic`
runs it as a subprocess (§5.6), which keeps §8.1's subprocess clause. The fixtures are those of `A1-fixtures.md` and
`A1-fixtures.json`. B's earlier run of SF-1 and SF-2 through an uncommitted by-path harness is exploratory
synthetic-fixture evidence; it qualifies nothing and is repeated through `--fixture` (§13).

### Q7. `hypotheses` of rows stopped at G1, G2 or VOID[row] (already determined)

§10.2: "`Λ` for a row that reaches G5 (R8), and the set of RD-3 (i) otherwise". RD-3 (i): "the declaration's hypotheses
(here H-inv[K-17(a)]) and the §2 access labels its token names". Z1-VOID, UNDECIDED and VOID[row] name no access label,
so the value is `["H-inv[K-17(a)]"]`.

### Q8. Measured fields of rows stopped by R5a (already determined)

R5a: "Every measured field of the row is still computed and reported." §10.2 `usefulness`: "It is `null` for every other
row."

### Q9. `hsel_content` when T1 is `"undecided"` (already determined)

§10.2: "`hsel_content` is `[]` when T1 or T2 fires"; "`a` and `t1` are true exactly when `class-decisions.json` records
`"flag"`". T1 fires only on `"flag"`; with `"undecided"`, the content is computed.

### Q10. Strictness of `adversarial.json` (working basis; absent and extra entries already determined)

§13 X4: "adds `adversarial.json` … when any row passes G5". §10.1: "refuses unless it lists every row that passes G5".

**Normative text.** At `final`, A and B each:
- accept an absent `adversarial.json` exactly when no row passes G5, and refuse (2) otherwise;
- refuse (2) unless the top level has exactly the keys `schema` (`"k1p1-adversarial"`), `version` and `rows`, with
  `version` of JSON integer type equal to 1 (`true` is refused), and `rows` a list;
- refuse (2) unless every entry has exactly the keys `branch`, `member`, `token` and `note`, all strings;
- refuse (2) on two entries with the same (`branch`, `member`) (**drafter's proposal**, §16);
- ignore an entry naming a row that does not pass G5, and read entries by key, not by position (**drafter's proposal**,
  §16; it makes A's and B's behaviour on such entries identical). ADV-INDEX (§10) fails on such an entry and on entries
  out of row order.

### Q11. Strictness of `class-decisions.json` (working basis)

**Normative text.** A and B refuse (2) unless the file has exactly the keys `schema`
(`"k1p1-class-decisions"`), `version` (JSON integer 1, not `true`), `derivations` (exactly §10.2's list), `g1`
(`"pass"` or `"undecided"`), `class_rule` and `support_restriction` (each exactly `{"a", "t1"}` with values `"pass"`,
`"flag"` or `"undecided"`) and `s0_paper` (exactly the six keys of §10.2, values `"pass"`, `"fail"` or `"undecided"`).
`controls.py` applies the same rule.

### Q12. `--out` and usage errors (working basis; `--out` already determined)

§10.1: "`<out>` a fresh empty directory".

**Normative text.** A and B refuse (2) when `<out>` is absent, not a directory or not empty, and exit 2 on every usage
error: an unknown or repeated flag, a missing value, a missing required flag, an unknown stage, or `--fixture` combined
with `--stage`, `--record` or `--members-sha256`. `controls.py` exits 2 on usage errors.

### Q13. CC-SCOPE's `nb_all_false` with no sharp `w` (already determined)

§10.2's CC-SCOPE row requires `"sharp": true` with `nb_all_false`, so a vacuous `nb_all_false` (no sharp `w`) fails the
control through `sharp`.

### Q14. §10.3's worked example (working basis; documentation)

The list after "The `π_0` member row in B-pl differs in these fields:" is completed to read: `"branch":"B-pl"`;
`"bound_ok":false`; `"gates"` with `"G4":"ABSENT[π_0; B-pl; H-cur (declared)]"`; `"hypotheses":["H-cur (declared)",
"H-inv[K-17(a)]"]`; `"ledger":"D=log(1/1); (c1) |E|=3: breaks"`; `"mass":{"":"1/1"}`; `"nb_g1":false`;
`"pi0_ref":{"":"1/8"}`; `"token":"ABSENT[π_0; B-pl; H-cur (declared)]"`; `"w_inputs":[]`;
`"w_rule":"W trivial; t_u = t_0"`; `"weak":{"":"1/8"}`. No code reads the example.

### Q15. Writer names, hand-off record and disclosures (working basis)

Carried out in §13.

### Q16. Check ids for MU-5 and MU-9 (working basis; ids and order a drafter's proposal)

§10.2 names only §9, §4, §11, `AB-*`, `IMPORTS` and `ADV-INDEX`. **Normative text.** `EXACT` is `controls.py`'s own
application of §7's guard to every file A and B wrote at the stage (MU-5 must fail it). `TOKENS` is `controls.py`'s
recomputation, from each row's measured fields and `class-decisions.json`, of every row's gates, `hypotheses`, `ledger`,
`bound_ok`, `g2`, `usefulness` form and token, and of each branch's class token and union flag (MU-9 must fail it). The
full roster and order are §6.

### Q17. MU-C1 to MU-C3: patch format and tool (working basis)

Carried out in §8.

### Q18. Rendering (owner ruling: drafter's proposal)

Carried out in §9.

### Q19. ADV-INDEX note index (working basis)

Carried out in §10.

### Q20. MU-11 when no row passes G5 (working basis; the mutation token a drafter's proposal)

Carried out in §10.

### Q21. Command-log categories (working basis)

Carried out in §12.

### Q22 to Q29. Readings (a) to (m) of `controls.py` (working basis)

The controls writer's readings, as recorded in its checkpoint (#1135 comment 6677738699):
- **Q22, reading (a)**, `controls.py` implements `φ` itself for CC-PART's closure and single-orbit test, PR-P1c and the
  T2 recomputation: **accepted**. MU-3 becomes an exchange (§11, C-1) so that the closure test is shown able to fail.
- **Q23, readings (b) and (c)**: (b), each content check runs on A's and on B's outputs and passes only if both pass:
  **accepted**. (c), if A or B exits nonzero, `AB-members` and `AB-gate-table` are recorded `fail` and no content check
  is performed: **accepted, amended** so that both exit statuses are recorded as structured data (§6, C-4).
- **Q24, readings (d) and (e)**: (d), a check runs from the first stage whose outputs carry its inputs; (e), CT-INC is
  `refused` when that implementation's CC-PART or CC-ROWS fails: **accepted**.
- **Q25, reading (f)**, CC-MASS re-sums `mass` and relies on the self-reported `completeness.mass_sums` for the `ν` and
  `L_σ` sums: **accepted**, with this statement: the `ν` and `L_σ` part of CC-MASS is not a check independent of the
  implementations; only the `mass` re-sum is.
- **Q26, reading (g)**, a pending `δ_0` row at `rows` counted as not positive: **replaced by the owner's strict
  ruling**. Normative text for PR-CR6's pass condition (§4): at `rows` and `final`, PR-CR6 fails if any `δ_0` row
  (member `"0000000000"`) passes G5, whatever its later gates or token, or if any branch's
  `union_clause_reached` is `true`. Grounds: CR-6's proof (`PROOFS.md` §6.3, on `main`) states that under `δ_0` "G4, if
  reached, issues VOID[row] or BLIND", so a `δ_0` row that passes G5 contradicts the proof whatever its later token.
  This is H3 (§14).
- **Q27, reading (i)**, `check` applies none of `run`'s git preconditions and, without `--stage`, checks the last stage
  whose files exist: **accepted**. The CI job uses `check --stage final` (§9.5). `run`'s preconditions gain
  `PRE-INPUTS` (§6, C-6).
- **Q28, reading (j)**, `members_sha256` is the digest of A's `members.json`, or `null` when A wrote none: **accepted**,
  `null` occurring only in the checks file of a failed or refused `run` (§10.2's absent-value convention).
- **Q29, readings (k), (l) and (m)**: (k), `run` exits 0, 1 or 2 (§4); (l), the implementations are invoked as
  `sys.executable -I`; (m), PR-LEDGER is read from G4 and the token: **accepted**.
- **Reading (h)** is Q7.

### Q30 and Q31 (no action)

Q30: POS-X's `W_ct` is a literal in A and derived from `E` in B; the sets agree at the instance, and a wrong `E` fails
PR-E. Q31: POS-X's `g3_void` is `false` by rule, since B-ct has no `D` bound (R6); A and B may write it as a constant.

## 3. The A/B divergences, resolved

Every case where A and B, as drafted, would give different bytes or exit statuses on the same input is fixed. A and B
must give byte-identical shared outputs and equal exit statuses on every input of §10.1 and §5.

| Case | Resolution |
|---|---|
| D-1: `rows`, a row passes G5 | Q1: both write `"pending"` for G6, G7 and the token, with `usefulness`. No implementation exits on this case |
| D-2: `final`, the adversarial token differs | Q2: UNDECIDED(G6); G7 `"not-reached"`; `usefulness` `null`; `hypotheses` `Λ` |
| D-3: union clause reached | Q4: `class_tokens[b]` `null`, `union_clause_reached[b]` `true` |
| D-4: `class-decisions.json` with an extra key or `"version": true` | Q11: both refuse (2) |
| D-5: `adversarial.json` entry without `note`, extra keys, or `"version": true` | Q10: both refuse (2) |
| D-6: usage error | Q12: both exit 2 |
| D-7: a pending branch's union flag | Q3: `false` |
| D-8: S0 failure at `rows` or `final` | Q5: both exit 2, nothing written |
| D-9: POS-X's `W_ct` | Q30: no action |

The static review's defects follow: A-1 (dead pending-class branch) and A-5 (exit on a G5 row) are removed by Q1 and Q3;
A-2's redundant refusal may stay; A-3 by Q12; A-4 by Q10 and Q11; B-2 by Q5. The lint items (B-1 and the style findings) are optional.

## 4. Exit statuses

**A and B (both routes).** 0: the files are written. 2: a refusal (usage, an `--out` that is not a fresh empty
directory, a stage precondition, a malformed input, CT-INC, an S0 failure at `rows` or `final`, or, on the fixture route,
an unknown id or an input whose bytes differ from the frozen digest). 3: the exactness guard (§7). 1: any other failure,
including an unexpected exception. No other status occurs; in particular no status marks an open question, since none
remains. Nothing is written on a nonzero exit.

**`controls.py`.** `run`: 0 when every check passes and the stage's files are written; 1 when a check fails; 2 on a
refusal or usage error. In all three cases it writes the stage's checks file (§10.1's "in every case"), recording the
checks performed up to and including the refused precondition. `check`: 0 when everything holds, 1 otherwise, 2 on a
usage error. `self-test`: 0 when every case holds; 1 when a case fails, including a patch whose hunks do not apply; 2 on
a usage error, or when a self-test input (`A1-fixtures.json` or a patch file) is absent or its SHA-256 differs from the
constant frozen in `controls.py`. `render`: §9.

## 5. The fixture interface (Q6, option (i))

### 5.1 Command line

```text
python3 -I verification/lean/k1p1_enum_a.py --fixture <id> --input <file> --out <out>
python3 -I verification/lean/k1p1_enum_b.py --fixture <id> --input <file> --out <out>
```

`--fixture`, `--input` and `--out` are required together and exclude `--stage`, `--record` and `--members-sha256`
(Q12). `<out>` is a fresh empty directory. This amends §10.1's command lines and §11.3's sentence "the implementations
carry no test hooks", which now reads: "Apart from the frozen `--fixture` entry point of A1 §5, the implementations carry
no test hooks."

### 5.2 Admission

Each program carries the frozen table of the fixture ids it accepts, each with the SHA-256 of that fixture's canonical
input bytes (the input object serialized as §10.2 serializes outputs, encoded UTF-8, with one final LF):

| Id | A | B | Canonical input SHA-256 |
|---|---|---|---|
| SF-1a | yes | yes | `0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1` |
| SF-1b | yes | yes | `c15b30da87758d7d7d762f6cf3b282c0490f9243e7f88d7b97db800811689dc9` |
| SF-1c | yes | yes | `d44e2700ddb8e50e1061c8846d6a8ee82092583af59ac44df0bbac361448643c` |
| SF-2a | — | yes | `521a0ca03cb42f4d81a93f6cd9bbcc1124fb2f8de6491738e7d4e4f7a8f07bc6` |
| SF-2b | — | yes | `fa77757342a23c1eef2d6d187ec68b4d90d0d395c19b94541cae04c61f74ccbe` |
| SF-2c | — | yes | `199029401c2707d8af887341846226e3c952dc28323bcc1731a1be9d0e9ac594` |
| SF-2d | — | yes | `d93b96d2b626410c2662c5844ab692a64b864a93f31be3743e1c7942cedf402b` |
| SF-2e | — | yes | `c6822bf4650178b6ccab88a20a1ecf088b7522c0c27ac1184abb0fe69e8bcef6` |
| SF-2f | — | yes | `6420ebd896642128865e250bb82da5780c9694a196a6a5a9df791bcc5ec46f65` |
| SF-2p | yes | yes | `f7d444061e8c2bfa427f66e5df7ff43ae80bf7b22548391ee340b67b66b845a7` |
| SF-2pb | yes | yes | `b8048192ccffc506f9e18981045048633ce9af1ceba1ac5f29c76fc1add20630` |
| SF-3 | yes | yes | `9f6fd0a2bb09127350b1b4a8edc323c3989f95fc1097064ecfe96d31740af36a` |
| SF-3f | yes | yes | `80319c62df77dc8a95a16d4e640fc0c44cf4a2c9aafa6f30006ba39b2271a8af` |
| SF-3g | yes | yes | `03dae8724f09cbbe68e983a6dd1717f370ddf4bf2ea194c4a7716f1ca02c8064` |

A program refuses (2) an id outside its table, and an input file whose bytes' SHA-256 differs from the id's entry. It
checks both before parsing the input further. So the fixture route accepts exactly the frozen synthetic inputs, and no
input naming the K1 instance, its dynamics or its states can reach any computation through it.

### 5.3 Inputs (all fields required, no others)

- `perm`: `id`, `kind`, `cells` (the state width and names), `image` (each state string to its image). For `perm`,
  `completeness.bijection` is true exactly when the image of every state is a state and the sixteen images are distinct,
  i.e. the image is a permutation of `S`; there is no `phi_inv`.
- `rank` (B only): `id`, `kind`, `rows` (a list of equal-length lists of 0 and 1).
- `linear`: `id`, `kind`, `q` (2), `kmax`, `cells`, `phi` and `phi_inv` (each cell to the sorted list of input cells
  summed mod 2).
- `system`: the `linear` fields, and `T`, `stage` (`"rows"` or `"final"`), `sigma`, `readout`, `class_decisions` (the
  three decision fields of §10.2, `g1`, `class_rule` and `support_restriction`), and `adversarial` (entries
  `{branch, member, token}`; `[]` at `rows`). Cells are `x_0, …, x_{n−1}, y_0, …, y_{n−1}`, and the site and slice
  structure used by `W_eq`'s rule is read from those names, as at the instance.

### 5.4 What the route computes, and with which code

The fixture route calls the same functions as the instance route, with a map supplied as data in place of the
instance's map and constants, for: M1 (all `2^n` strings, `linear` and `system`), M2 (both composites; the result is recorded in
`completeness.bijection`, and a failure is recorded, not refused), M3 to M5, R0 to R10, CLASS, serialization and §7's
guard. §8.2's method diversity holds on the route: A applies `φ` and `φ^{−1}` from the cell-by-cell formulas and finds
`E` by propagating symbolic 𝔽₂ forms; B builds the matrices, applies them by matrix-vector products, finds `E` from the
rows of `M^t`, and computes the rank chain from ranks of `M^k − I` with Möbius inversion. The route reads no file other
than `--input`, no instance constant (`N`, `q`, `a`, `T`, `Σ`, `V`, the K1 formulas) and no record-directory file, and
computes no S0 control and no preserved-result block. At `final`, adversarial entries follow Q10's coverage and duplicate
rules (without `note`). On the route, M2's failure is recorded and the route continues; at the instance the same holds,
so that MU-C2 fails CC-BIJ rather than an exit status.

**How A meets "the same functions".** At the instance, A builds `φ` and `φ^{−1}` from the K1 coordinate formulas, as
cell-by-cell linear forms, and passes them to its orbit walk, its symbolic propagation for `E` and its row functions. On
the fixture route the same functions receive the cell-by-cell forms read from the input. B likewise passes either its
instance-built matrices or matrices built from the input to the same matrix and rank functions. The two methods stay
distinct on both routes.

**What the fixture route does not exercise** (claim/evidence boundary). A passing synthetic self-test establishes the
behaviour of the shared functions on the fixtures, and nothing about the following, which only the instance route
reaches: A's K1 coordinate formulas and B's construction of the K1 matrices; the instance constants (`N`, `q`, `a`, `T`,
`Σ`, `V`); the S0 controls; the preserved-result block; record-directory input and output (the `members.json` pin and
its refusals, `class-decisions.json`, `adversarial.json` with `note`, and their strict validation); the gate-table-only
fields (`instance`, `preserved`, `controls`). Before `F` these are covered by the static re-review only; after `F` by the
S0 controls, the CC and PR checks, and MU-C1, MU-C2, MU-14 and MU-16.

### 5.5 Outputs

Written to `<out>` with §10.2's serialization, only on exit 0:
- `fixture.json`, by A and B, byte-identical between them: `schema` `"k1p1-fixture-output"`, `version` 1, `fixture`
  (the id), `kind`, and
  - `perm` and `linear`: `cell_order`, `members` and `histogram` in `members.json`'s form, and `completeness`
    (§10.2's keys; `mass_sums` `null`);
  - `rank`: `rank`;
  - `system`: also `stage`, `region` (with §10.2's `region` keys; the gate table's `instance`, `preserved` and
    `controls` are absent), `rows` (§10.2's row objects),
    `class_tokens` and `union_clause_reached`, and `completeness.mass_sums` a boolean.
- `fixture-cyc2.json`, by B only, for `linear` and `system`: `schema` `"k1p1-fixture-cyc2"`, `version` 1, `fixture`,
  `kmax`, and objects `ranks`, `fix`, `period_states` and `cycles` from each `k = 1, …, kmax` as a decimal string, and
  `identity_at_kmax`.

The expected bytes are the canonical serialization of `A1-fixtures.json`'s `expected` and `expected_cyc2`. Where an
entry gives `expected_from` and `expected_set`, the expected object is the named fixture's, with `fixture` set to the
entry's id and each listed path set to its value; `expected_cyc2_from` copies the named `expected_cyc2` with `fixture`
set likewise. These are substitutions of listed values; nothing is derived.

### 5.6 `controls.py self-test --synthetic`

It reads `<rec>/amendments/A1-fixtures.json` and refuses (2) unless the file's SHA-256 equals the constant frozen in
`controls.py`; it reads the patches from `<rec>/amendments/A1-patches/` likewise. `<rec>` is the record directory of
the tree it runs in: on the round branch, the control plane's own files; on the integration branch, their byte-identical
copies (§14). Then, in this order:
1. **Fixtures.** For each entry of `fixtures`, for each program it lists: write the canonical input to a fresh temporary
   file, run the program with `--fixture`, `--input` and a fresh empty `--out`, as `sys.executable -I`, and require the
   entry's exit status, `fixture.json`'s bytes equal to the expected bytes (EXPECTED′), A's and B's `fixture.json`
   equal (AB′), and B's `fixture-cyc2.json` equal to its expected bytes.
2. **Own checks on the outputs** (§11.2): each applicable primed check passes on every unmutated output.
3. **Analogues** (`analogues`; `A1-fixtures.md` §6): each must make its named checks fail, or report refused.
4. **Interface negatives** NF-1 to NF-7, each after its paired control. Each must exit 2 and leave `<out>` exactly as
   it was before the run (empty, or, for NF-4, holding only the file placed there).
5. **MU-C3′**: the frozen MU-C3 patch applied to a temporary copy of A (§8); `--fixture SF-3` must exit 3. The
   unpatched run of step 1 is its control.
6. **Render, marker and adversarial-index fixtures** (§9, §10).

It exits as §4 states: 0 exactly when every step holds, 1 when a step fails, 2 on a usage error or an absent or
mis-pinned self-test input. It never passes `--stage` to A or B, and it reads no record-directory file other than
`A1-fixtures.json` and the patches.

This amends §11.2: SF-1, SF-2 and SF-3 are those of `A1-fixtures.md`, with SF-2′ added; the "two-cell toy system" of
§11.2 is replaced by SF-3's four-cell system, because `W_eq`'s rule (site set of `V`, both slices) and a `Σ` disjoint from
`V` need two sites in two slices.

## 6. The checks files: roster, order and new fields

**Roster and order** (Q16; C-3; C-6; drafter's proposal for the `PRE-*` ids). `run --stage s` performs, and records in
this order, the checks of its stage:

| Stage | Checks, in order |
|---|---|
| `members` | `PRE-INPUTS`, `IMPORTS`, `AB-members`, `AB-gate-table`, `EXACT`, `CC-ABS`, `CC-EXACT`, `CC-SCOPE`, `CC-LEDGER`, `CC-IMP`, `CC-IMP′`, `CC-IMP″`, `CC-PASS`, `CC-T2`, `POS-X`, `CC-BLIND`, `PR-S0`, `CC-COUNT`, `CC-BIJ`, `CC-PART`, `CC-CYC2`, `CT-INC`, `PR-E`, `PR-CYC`, `PR-EN`, `PR-P1c` |
| `rows` | `PRE-INPUTS`, `PRE-PREV`, `PRE-CHECK`, then the `members` list from `IMPORTS` to `CC-CYC2`, then `CC-ROWS`, `CC-MASS`, `CT-INC`, `PR-E`, `PR-CYC`, `PR-EN`, `PR-P1c`, `PR-IND`, `PR-BLIND`, `PR-LEDGER`, `PR-CR6`, `PR-P0`, `TOKENS` |
| `final` | `PRE-INPUTS`, `PRE-PREV`, `PRE-ADV`, `PRE-CHECK`, then the `rows` list from `IMPORTS` to `TOKENS`, then `ADV-INDEX` |

- `PRE-INPUTS`: `class-decisions.json`, `derivations/P1-class-paper.md` and `derivations/S0-paper.md` are tracked and
  unmodified at `HEAD` (C-6).
- `PRE-PREV`: every file of the previous stages is tracked and unmodified at `HEAD`.
- `PRE-ADV` (`final`): when a row of the committed `gate-table.rows.json` passes G5, `adversarial.json` and each note file
  are tracked and unmodified; otherwise it passes.
- `PRE-CHECK`: `check --stage <previous>` exits 0.

A `PRE-*` check that does not hold is recorded `"refused"`, `run` stops there and exits 2. When A or B exits nonzero,
`AB-members` and `AB-gate-table` are recorded `"fail"` and no later check is performed (Q23). A check is recorded once,
having run on both A's and B's outputs.

**New fields** (§10.2's checks files):
- `exit_status`: `{"A": <int or null>, "B": <int or null>}`, the exit status of each implementation run at the stage,
  `null` when it was not run (C-4). H1 (both 0, outputs differ), refusals (status 2), the exactness guard (status 3,
  a defect of the frozen code, H6) and any other failure (status 1, H6) are told apart from this field and the `AB-*`
  outcomes.
- `gate_table_sha256` (`checks.json` only): the SHA-256 of A's final `gate-table.json` bytes when every final check
  passes, `null` otherwise (Q18).
- `members_sha256` (`checks.members.json`): as §10.2, `null` only in a failed or refused `run` (Q28).

`check` regenerates the same files, these fields included, and compares them with the committed bytes (`REPLAY-*`).

## 7. Requirements on `controls.py`

- **C-1, MU-3.** MU-3 exchanges one state each way between two 10-cycles of `members.json`, neither state the least
  state of its cycle, and re-sorts both state lists, so that sizes, histogram, keys, sortedness and coverage stay valid
  and only CC-PART's closure or single-orbit test can detect it.
- **CC-PART's sub-tests** (drafter's proposal, §16, enumerating what §9's "every state in exactly one cycle; lengths sum
  to `|S|`; each cycle closed under `φ` and a single orbit" requires of `members.json`'s form). On `members.json`, with
  `controls.py`'s own `φ`: (p1) every state of `S` occurs in exactly one member's `states`; (p2) each `size` equals its
  list's length, the sizes sum to `|S|`, and `histogram` equals the size counts; (p3) each member's states are closed
  under `φ`; (p4) each is a single orbit; (p5) each `states` list is sorted; (p6) each `key` is the least of its states;
  (p7) the cycle members are in strictly increasing order of `key`, after `pi0`. At the instance, (p7) is also checked
  on the rows by CC-ROWS. CC-PART′ applies (p1) to (p7) to a fixture's `members` with the fixture's map; on the `perm` and
  `linear` routes, which have no rows, member order is checked by CC-PART′ (p7) alone.
- **C-2, MU-12.** MU-12 changes CC-EXACT's `computed.weak[""]` to `"1/1"` and its `outcome` to `"fail"`, identically in
  A's and B's outputs, so that the control genuinely fails: CC-EXACT and PR-S0 are recorded `fail`, `run` exits 1, and no
  row file is written.
- **C-3, MU-14.** The `controls.py` leg of MU-14a to MU-14c, and of MU-14d (§11), passes only when the sandbox's checks
  file records the named `PRE-*` check as `"refused"` and `run` exits 2, after a paired run of the unmutated sandbox
  records that check `"pass"`.
- **C-4.** §6's `exit_status`.
- **C-5.** G7 `"not-reached"` after UNDECIDED(G6) is Q2, now declared.
- **C-6.** §6's `PRE-INPUTS`.
- **C-8, negative fixtures.** §5.6 and `A1-fixtures.md` §6: every primed check is shown able to fail.
- **C-9.** No refusal on an open question remains; every `run` path writes the checks file.
- **C-10.** Sandbox `git` runs with `-c core.hooksPath=/dev/null`, `GIT_CONFIG_GLOBAL=/dev/null` and
  `GIT_CONFIG_NOSYSTEM=1` (drafter's proposal; cheap mitigation under §A.41).
- **C-11.** Q28.
- **Mutation detection reads structured data** (§A.44): exit statuses, checks-file outcomes, and the fields of the
  outputs, never printed text. A mutation aimed at a content check is applied identically to A's and B's outputs, so that
  `AB-*` pass and the content check is reached; a mutation aimed at `AB-*` is applied to one output only.

## 8. Mutation patches (Q17)

- **Files.** `amendments/A1-patches/MU-C1.patch`, `MU-C2.patch` and `MU-C3.patch`, added by the freeze revision (§14),
  made against the frozen blobs on the integration branch. Their SHA-256 values are recorded in §14 and frozen in
  `controls.py`.
- **Format.** Unified diff of one file: one `--- a/<path>` and one `+++ b/<path>` header naming the frozen file's
  repository path, then hunks `@@ -l,s +l,s @@` whose lines begin with a space, `-` or `+`. No `\ No newline at end of
  file` marker (frozen files end with LF), no fuzz, no offset.
- **Applier.** A stdlib-only line splice in `controls.py`: it verifies the patch's SHA-256, reads the frozen file as
  lines, and for each hunk in order requires the old lines (context and `-`) to equal the file's lines at the stated old
  start exactly, then replaces them by the new lines (context and `+`). The patched copy is written to a temporary directory and run from there with `sys.executable -I`.
- **Content.** MU-C1 sets A's `T` to 2; MU-C2 makes B's `φ^{−1}` matrix wrong in one entry; MU-C3 replaces A's exact
  division by floating division at its single division helper.
- **Exit statuses.** A patch file that is absent or whose SHA-256 differs is a refusal of the self-test (2); a hunk
  that does not apply fails it (1). Neither passes it.
- **Pass criteria.** Only one program is patched in each case, so the checks file's single outcome per check suffices.
  MU-C1: the sandbox checks file records PR-E `fail`. MU-C2: it records CC-BIJ `fail`. MU-C3: A's `exit_status` is 3
  (instance, after `F`), and A exits 3 on `--fixture SF-3` (MU-C3′, before `F`).

## 9. Rendering (Q18: drafter's proposal)

The proposal of #1135 comment 6679002642, reviewed there as WIP, completed here.

### 9.1 Command and inputs

`python3 -I <rec>/controls.py render --out <dir>`, `<dir>` a fresh empty directory. This amends §10.1's `render` line.
It reads `<rec>/gate-table.json`, `members.json`, `checks.members.json` and `checks.json`. It runs neither A nor B and
derives no token: the row and class token strings come from `gate-table.json`.

### 9.2 Validation, in order; the first that fails is the reason

1. `MISSING_INPUT`: an input absent or not UTF-8 JSON.
2. `BAD_SCHEMA`: an input fails §10.2's schema or is not byte-equal to its own canonical re-serialization; the gate
   table's `stage` is not `"final"`; its rows are not, branch by branch in the order B-pl, B-eq, B-ct, exactly the
   member keys of `members.json` in M5 order; a token fails the grammar of §9.3, or a row token does not name its own
   row's member and branch; or a union flag and its class token disagree with Q4.
3. `INPUT_MISMATCH`: `members.json`'s SHA-256 differs from `checks.members.json`'s `members_sha256`, or
   `gate-table.json`'s SHA-256 differs from `checks.json`'s `gate_table_sha256` (including `null`).
4. `UNION_REACHED`: some `union_clause_reached` is `true`. The table is kept as stop evidence; no fragment is produced.
5. `CONTROL_NOT_GREEN`: an S0 control's `outcome` is not `"pass"`, or `checks.json`'s `checks` is not exactly §6's
   `final` roster with every outcome `"pass"`.
6. `INCOMPLETE_TOKENS`: a row or class token is `"pending"`.

Valid tokens such as `VOID[row]` or `UNDECIDED(G6)` render over green controls; the halt rules of §14 govern what follows.

### 9.3 Token grammar

Row tokens: `ABSENT[<m>; <b>; <acc>]` and `BLIND[<m>; <b>; <acc>]` with `<m>` the row's member name, `<b>` its branch and
`<acc>` §10.2's access labels of `<b>`; `VOID[row]`; `Z1-VOID[IMPORTED]`, `Z1-VOID[DYN]`; `UNDECIDED(G<k>)`, `k` in
1 to 7; `CONDITIONAL[<Λ>]` and `AVAILABLE[H-sel](<Λ>)`, `<Λ>` a nonempty list of distinct labels among §10.2's six,
in code-point order, joined by `", "`; and `"pending"`. Class tokens: `ABSENT[𝓘; <b>; <acc>]`, `BLIND[𝓘; <b>; <acc>]`,
`UNDECIDED(G<k>, …)` (distinct, ascending), `Z1-VOID[IMPORTED]`, `Z1-VOID[DYN]`, `Z1-VOID[IMPORTED, DYN]`,
`VOID[row](<member names in M5 order>)`, `"pending"`, and `null` with a `true` union flag only. Nothing else is a token.

### 9.4 The fragment

UTF-8, LF line ends, no BOM, no trailing spaces, one final LF. Lines, in order:
1. `<!-- k1p1-token-tables:v1:begin -->`, then an empty line;
2. `| Branch | Member | Token |` and `| --- | --- | --- |`;
3. one line per row, branches B-pl, B-eq, B-ct and members in M5 order: `` | <b> | `<member name>` | `<token>` | ``,
   with member name `π_0` for `pi0` and `u_c[<key>]` otherwise;
4. an empty line, `| Branch | Class token |`, `| --- | --- |`, and one line `` | <b> | `<class token>` | `` per
   branch in the same order;
5. an empty line, then `<!-- k1p1-token-tables:v1:end -->`.

No escaping, sorting or normalization is applied; the grammar excludes backticks and `|`. RF-1's expected fragment
(`A1-fixtures.json`) is an instance of this layout.

### 9.5 Status, outputs, and the check at `E`

- `render-status.json`, §10.2's serialization: `schema` `"k1p1-render-status"`, `version` 1, `stage` `"final"`,
  `outcome` (`"pass"`, `"refused"` or `"fail"`), `reason` (`"OK"`, a reason of §9.2, or `"IO_ERROR"`),
  `gate_table_sha256` (the SHA-256 of the gate-table bytes read, `null` if none were read) and `fragment_sha256` (`null`
  unless `outcome` is `"pass"`). No path, time or verdict text.
- Exit 0, `pass`: `token-tables.md` and the status are written. Exit 2, `refused`: only the status. Exit 1, `fail`,
  `IO_ERROR`: the status is attempted; if it cannot be written, nothing is. Each file is written to a temporary name in
  `<dir>` and renamed; temporary files are removed on every exit. A consumer accepts a fragment only with exit 0 and a
  status whose `outcome` is `"pass"` and whose `fragment_sha256` matches it.
- At X5 the executor embeds the fragment bytes in `result.md`. `check --stage final` (RENDER), after every replay and
  control comparison holds, regenerates the fragment in memory and compares it with the bytes of `result.md` from the
  start of the unique begin-marker line through the LF ending the unique end-marker line. A missing, repeated or
  reversed marker, a changed byte or a changed line end fails RENDER, through `check`'s exit status only.
- §13 X5's job command and §10.4's recipe become `python3 -I controls.py check --stage final`, so that missing final
  files cannot fall back to an earlier stage.

### 9.6 Fixtures

Before `F` (synthetic profile): `self-test --synthetic` calls `controls.py`'s own projection and validation functions, the
ones `render` uses, on fixture outputs in place of files. Steps 2, 4 and 6 of §9.2 apply; steps 1, 3 and 5 need files
and run after `F` (MU-15, §11). In this profile step 2 reads "§10.2's schema" as §5.5's `system` fixture-output schema,
requires `stage` `"final"`, and takes the member keys from the fixture output's own `members` in place of
`members.json`; the token grammar and the union rule are as in §9.2 and §9.3. Fixtures RF-1, RF-2, RN-1 to RN-9 and RM-0 to RM-5 (`A1-fixtures.md` §7).

## 10. Adversarial note index (Q19) and MU-11 (Q20)

**Q19, normative text.** A note file `derivations/adversarial-<b>.md` exists exactly for each branch `b` with a row that
passes G5. Its first lines are its index, one row key per line (`pi0` or the least state), with nothing else on the line,
in M5 order, ended by the first empty line. ADV-INDEX passes exactly when, for each branch: the note file exists if and
only if the branch has a row that passes G5; its index lists exactly those rows' keys in M5 order; and the entries of
`adversarial.json` for that branch list the same keys in `gate-table.rows.json`'s row order, each with `note` equal to
that file's path. Fixtures AI-0 to AI-7.

**Q20, normative text.** MU-11 is required at `final` exactly when a row of `gate-table.rows.json` passes G5. Its mutation
replaces that row's adversarial token by `BLIND[<member name>; <b>; <acc>]`, a well-formed token different from any
positive. It passes when both A's and B's final outputs give that row `gates.G6 = "UNDECIDED(G6)"` and
`token = "UNDECIDED(G6)"`. When no row passes G5, the condition is read from the committed `gate-table.rows.json`, and
`result.md`'s execution log records MU-11 as not applicable with that reason. Its synthetic analogue, SF-3g, exercises
the G6 path before `F` in either case.

## 11. Mutations: amended and added

### 11.1 Changes to §11.3

| Id | Mutation | Must fail | Stage |
|---|---|---|---|
| MU-3 (amended) | exchange one state each way between two 10-cycles of `members.json` (C-1) | CC-PART | `members` |
| MU-12 (amended) | CC-EXACT's `computed` and `outcome` made a genuine failure, in both outputs (C-2) | CC-EXACT and PR-S0; no row file written | `rows` |
| MU-14a–c (amended) | as §11.3; the `controls.py` leg reads `PRE-PREV` `"refused"` (C-3) | as §11.3 | `rows` |
| MU-14d (new) | `class-decisions.json` modified and not committed, in the sandbox | `PRE-INPUTS` `"refused"`; `run` exits 2 | `rows` |
| MU-15a (new) | `checks.members.json`'s `members_sha256` set to 64 zeros | `render` refused, `INPUT_MISMATCH` | `final` |
| MU-15b (new) | one entry of `checks.json` set to `"fail"`, `gate_table_sha256` kept | `render` refused, `CONTROL_NOT_GREEN` | `final` |
| MU-15c (new) | `gate-table.json` removed | `render` refused, `MISSING_INPUT` | `final` |
| MU-15d (new) | one byte inside `result.md`'s fragment changed | `check` exits 1 (RENDER) | `final` |
| MU-16a (new) | an extra top-level key in `class-decisions.json` | A and B exit 2 (`exit_status`) | `rows` |
| MU-16b (new) | `"version": true` in `class-decisions.json` | A and B exit 2 | `rows` |
| MU-16c (new) | an `adversarial.json` entry without `note`, when a row passes G5; otherwise not applicable, as for MU-11 | A and B exit 2 | `final` |
| MU-17 (new) | a `δ_0` row recorded as passing G5 and pending, in both outputs (Q26) | PR-CR6 | `rows` |

Each new or amended mutation is preceded by a paired run without the mutation, which must hold; a mutation detected only
because its control also fails fails the self-test. §11.3's timing lists gain MU-14d, MU-16a, MU-16b and MU-17 at `rows`,
and MU-15a to MU-15d and MU-16c at `final`. MU-16a to MU-16c have no synthetic analogue (`A1-fixtures.md` §6).

### 11.2 Primed checks on fixture outputs

`AB′` (A's and B's `fixture.json` byte-equal), `EXPECTED′` (each equal to the expected bytes), `EXACT′`, `CC-PART′`
(with the fixture's map, built by `controls.py` from the input), `CC-BIJ′`, `CC-CYC2′` (B's rank chain against the
member histogram, with Möbius consistency), `CC-ROWS′`, `CC-MASS′`, `CT-INC′`, `PR-E′` (the region's `E` and `W_eq`
against the hand-derived values), `PR-CR6′` (strict, on the toy's zero state `0000`) and `TOKENS′`. Each is the
instance check's function applied to fixture data, or, for `PR-E′`, a comparison with the fixture's frozen values as
PR-E compares with literals. They are reported only through `self-test`'s exit status and are recorded in no checks file.

## 12. Command-log categories (Q21) and the drafting log

§19's Finding 10 lists "read, static check, synthetic-fixture run, or, under authorization (e), run on the instance".
**Normative text.** A fifth category, **edit**, covers file and `git` writes, commits, pushes and posts; it computes
nothing. Every command of a writer or reviewer of this round before `F` is listed under one of these five in the
drafting log (the commits from `D` and the checkpoint comments on #1135), fixture runs included, with any harness quoted
with its digest. The staging-only log files `verification/lean/k1p1_enum_{a,b}.drafting-log.md` are not carried onto the
integration branch or into X1; before `F` each writer's command table, A's per-command table included, is posted as or
quoted in a checkpoint comment. This amendment's own commands are in its checkpoint comment.

## 13. Provenance and independence (Q15)

**Writers.**

| Dispatched as | Preregistration §8.1 | Staging branch, head reported |
|---|---|---|
| `writer-k1p1-implA` | `writer-k1p1-impl-a` | `staging/k1-p1-1-impl-a-20261106`, `caea695c875179fb9b310739c4aa2a9196332fe4` |
| `writer-k1p1-implB` | `writer-k1p1-impl-b` | `staging/k1-p1-1-impl-b-20261106`, `e32fe4eea312b1a468ea19ed1f1559d768c5dbda` |
| `writer-k1p1-controls` | `writer-k1p1-ctl` | `staging/k1-p1-1-controls-20261106`, `e4ee843c87005b2f48e9e2081ed7dc12e41c0f0e` |

The dispatch times and the SHA-256 of each brief are in the coordinator's hand-off record, #1135 comment 6677963479. A
dispatched name and its §8.1 name denote the same writer; file headers record both.

**Disclosures**, under the owner's ruling that independent agent contexts under one coordinator are acceptable as
internal model-independent replication, with inputs, shared dependencies and hand-offs disclosed, and that these are
model reviews:
1. **Shared session.** The three writers, the two reviewers and this amendment's writer are separate agent contexts
   launched from one coordinating Claude Code session, which is why every file header names the same session.
   Independence here means separate contexts with no access to another writer's code, output or checkpoint at the time
   of writing; it does not mean separate sessions or operators. Shared dependencies: the preregistration at `4ca431af`,
   `K` at `d9b3de01`, `AGENTS.md`, the Stage 2 authorization and the coordinator's briefs.
2. **The controls writer's reads.** Besides its brief, the `controls.py` writer read #1135's comment list and #1031's
   comments since 04:50Z. A's checkpoint (05:25:55Z) predates the `controls.py` commit (05:27:58Z), and the controls log
   has no times, so whether that writer saw A's checkpoint is not established. The checkpoint holds A's readings, open
   questions and digests, not A's code.
3. **B's harness run.** B's writer ran SF-1 and SF-2 through an uncommitted harness `sf_b.py` (SHA-256
   `977d30c9ef494aea438713c5a45b097eb98888d5a5732028593450359d94ece6`, text in B's drafting log) that loads B by path and
   calls two generic functions. The static review found that B's top level computes nothing, so nothing ran on the
   instance. Under the owner's Q6 ruling the run is exploratory synthetic-fixture evidence; it is repeated through
   `--fixture` to qualify. B's writer also resolved several ambiguities in code against its brief's instruction to stop
   and report; those readings are superseded by this amendment's rulings.
4. **Earlier `self-test --synthetic` runs.** The controls writer and the synthetic-fixture reviewer each ran the drafted
   `controls.py self-test --synthetic` once (SF-1, positive only; exit 2 on an open question). These are exploratory
   runs of a superseded fixture specification.
5. **This amendment.** Written by `writer-k1p1-amend`, a separate agent context of the same coordinating session,
   acting under the writer designation of c.6680770304. It is not one of §8.1's five designated sessions and writes no
   code. It read the preregistration, `K`'s cited lines, both reviews, the writers' checkpoints and the
   coordinator's record, and read the drafted code statically to confirm its interfaces. It ran none of A, B and
   `controls.py`, and no fixture.
6. **A cross-writer channel.** This amendment describes behaviour and defects of each implementation and of
   `controls.py` (§3's D-1 to D-9 and A-1 to B-2; Q30's POS-X note; Q22 to Q29's readings) and is delivered to every
   writer for the revision. It carries no code; it is a disclosed channel between writers, limited to the behaviour the
   rulings fix.

## 14. Integration branch and the freeze revision

- The three writers' staging branches are kept, never rebased, force-pushed or deleted.
- Each writer revises its own file under this amendment, without access to the other writers' revised code. A static
  re-review of each revised blob at its exact head and a synthetic-fixture review through `--fixture` follow, both
  independent of the writers.
- The reviewed blobs are consolidated on one integration staging branch, cut from a commit of `main`, by single-parent
  commits each adding one reviewed file byte for byte and naming its source branch, commit and blob. Besides the three
  code files, the integration branch carries, at the same repository paths as on the round branch and byte-identical to
  the round branch's blobs, `amendments/A1-fixtures.json` (at this revision blob `b785d728d86a7f5a970cd89c32ce1c45621bae11`,
  SHA-256 `691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85`) and the three patch files of §8, once the
  freeze revision has added them to the round branch. Nothing else is committed there. The writers' drafting logs are not
  carried.
- `controls.py self-test --synthetic` exits 0 at the integration head before `F` is proposed. It runs there against the
  integration branch's own tree (§5.6), so the gate needs only that branch: the code files, `A1-fixtures.json` and the
  patches. `controls.py`'s frozen constants for `A1-fixtures.json` and the patches equal the round branch's blobs'
  SHA-256, so a later revision of `A1-fixtures.json` requires a new `controls.py` constant and a new review.
- The freeze revision of this file, under authorization (b), fills this table and quotes (b):

| File | Blob | SHA-256 |
|---|---|---|
| `verification/lean/k1p1_enum_a.py` | (to be recorded) | (to be recorded) |
| `verification/lean/k1p1_enum_b.py` | (to be recorded) | (to be recorded) |
| `verification/programmes/oi-qm/reconstruction/round-k1-p1-1/controls.py` | (to be recorded) | (to be recorded) |
| `amendments/A1-patches/MU-C1.patch`, `MU-C2.patch`, `MU-C3.patch` | (to be recorded) | (to be recorded) |
| `amendments/A1-fixtures.json` (copy on the integration branch) | (to be recorded; equal to the round branch's) | (to be recorded) |

and records the integration branch's head and the `verify.yml` edit of §13 X5 (with §9.5's command).

## 15. RR-1 Finding 12

**The D sentence.** Preregistration §19, "Text and scope", reads: "The checkpoints of the entries for Findings 10 and 12
are checked, with those of §15, by the reviewer of each candidate head before `F` is proposed for designation and before
`E` is designated (§13)." It is amended to read: "The checkpoints of the entries for Findings 10 and 12 are checked, with
those of §15, by the reviewer of each candidate head before `F` is proposed for designation and before `E` is designated
(§13), and the receipt checkpoint of Finding 12 at `Q`." (Delta review of `4ca431af`, #1135 comment 6677168694, nit; the
Stage 2 authorization asks for it in the next permitted documentation revision.)

**Finding 12's quotations.** Authorization (a) is quoted in §0. Authorization (b) is quoted by the freeze revision.

## 16. Owner approval needed with (b)

These parts are drafter's proposals (§1) and take effect only with the owner's approval of this amendment:
1. the `PRE-*` check ids and the full check roster and order (§6);
2. the `exit_status` and `gate_table_sha256` fields (§6);
3. the fixture admission table by input digest (§5.2), and the fixture kinds, schemas and output files (§5.3 to §5.5);
4. the rendering design (§9), proposed under the Q18 ruling, including `check --stage final` at X5;
5. MU-14d, MU-15a to MU-15d, MU-16a to MU-16c and MU-17 (§11);
6. the sandbox `git` isolation (C-10);
7. the replacement of §11.2's two-cell toy by SF-3's four-cell system, and the fixture contents of `A1-fixtures.md`;
8. Q5's `members`-stage behaviour: exit 0 with the failing control recorded, and `run` exit 1 (§2, Q5);
9. Q10's refusal of duplicate entries and its ignore-and-read-by-key rule (§2, Q10);
10. Q20's MU-11 mutation token `BLIND[<member name>; <b>; <acc>]` (§10);
11. CC-PART's sub-tests (p1) to (p7) (§7).

Two further questions for the owner, which this amendment does not decide:
- whether the fixture set pinned at a reviewed head of this amendment counts as "predeclared" for the Stage 2
  `--fixture` and `self-test --synthetic` runs that §14 schedules before (b) is given;
- whether the following coverage, static-only before `F`, is acceptable: strict input validation (Q10, Q11; MU-16 after
  `F`), D-3 (the union reached), D-8 (an S0 failure at `rows`), and the instance-only code of §5.4.

## 17. References to content not on `main` (§A.42 item 8)

| Reference | Claim | Class |
|---|---|---|
| Independent static review, `STATIC-REVIEW.md`, held off-repository by the coordinator; not on `main` | the source of the Q1–Q31 readings and defects C-1 to C-11, D-1 to D-9 | provenance: every reading adopted is stated in full in §2, §3 and §7 |
| Independent synthetic-fixture review, `FIXTURE-REVIEW.md`, held off-repository by the coordinator; not on `main` | the fixture requirements carried out in §5 and `A1-fixtures.md` | provenance: the fixtures and their derivations are stated in full here |
| The three staging branches and heads (§13) | the drafted code these rulings address | provenance until the freeze revision; the frozen blobs reach `main` through X1 and the round's landing |
| Independent review of this amendment at `0a17e814` (`A1-REVIEW.md`), held off-repository by the coordinator; not on `main` | the revisions of this amendment's second draft | provenance; each revision is stated here |
| #1135 comments 6677692354, 6677725670, 6677738699 (writers' checkpoints), 6677963479 (hand-off record), 6679002642 (Q18 proposal), 6679215729 and 6679364571 (reconstructed Q-table and its check), 6677168694 (Finding 12 nit) | the disclosures of §13, the rendering basis of §9, the D sentence of §15 | provenance; the content used is stated here |
| #1031 comments 6677496553, 6678956167, 6680770304 | authority | quoted in §0 with author and time |
| `PROOFS.md` §6.3, blob `b50e23e47e107934fb5637158cd9148433d62bc9` | Q26's grounds | support on `main` |

## 18. Invariants and checkpoints (§A.41)

| Invariant (new in this amendment) | Checkpoint |
|---|---|
| A and B agree on every formerly divergent case (§3) | `AB-members` and `AB-gate-table` at each stage; on the fixture route, AB′ and EXPECTED′ on SF-3 (pending row), SF-3f (positive) and SF-3g (UNDECIDED(G6)); NF-3 and NF-4 for usage refusals; the static re-review of the revised blobs |
| Exit statuses are only 0, 1, 2 and 3, and nothing is written on a nonzero exit (§4) | static re-review; NF-1 to NF-7, each requiring exit 2 and `<out>` unchanged; `exit_status` in every checks file |
| D-3 (union reached: `null` class token) and D-8 (S0 failure at `rows`: exit 2) | static-only: the static re-review before `F`; no fixture or mutation reaches them (D-3 is excluded at the instance by CR-6; D-8 is stopped at X2 by PR-S0). RN-2 and RN-8 test render's handling of D-3's output form |
| Q5's `members`-stage behaviour (failing control recorded, `run` exit 1) | static re-review; MU-12's paired runs at `rows` show the recorded failure path of the S0 checks |
| Q19's note-index form | AI-0 to AI-7 before `F`; ADV-INDEX at `final` |
| Q28: `members_sha256` `null` only in a failed or refused `run` | static re-review; at X2 `check --stage members` regenerates `checks.members.json` and REPLAY compares it, including the digest |
| C-10: sandbox `git` isolated from global configuration and hooks | static re-review of the self-test's `git` invocations |
| CC-PART's sub-tests (p1) to (p7) | AN-3, AN-4, AN-7m, AN-MO, AN-KL, AN-US and AN-DS before `F`; MU-3, MU-4 after |
| The integration branch can run the pre-`F` gate (§14) | the reviewer of candidate `F` checks that the integration head holds `A1-fixtures.json` and the patches byte-identical to the round branch's blobs, and that `self-test --synthetic` exits 0 there |
| The fixture route computes nothing on the K1 instance (§5.2, §5.4) | the digest admission table, tested by NF-2, NF-5 and NF-6; the static re-review finds no instance constant or record file read on the route; the drafting log lists every fixture run |
| Fixture answers are hand-derived (`A1-fixtures.md`) | the written derivations; the synthetic-fixture reviewer re-derives them independently before `F` |
| Every primed check can fail (C-8) | `self-test --synthetic`: each analogue after its paired control; exit 0 required at the integration head |
| The G6 path is exercised before `F` (Q20) | SF-3g's expected output |
| Strict PR-CR6 (Q26) | AN-17 before `F`; MU-17 after |
| Strict inputs (Q10, Q11) | static re-review before `F`; MU-16a to MU-16c after |
| Exit statuses and refusals are structured (C-3, C-4) | `exit_status` and `PRE-*` in the checks files; MU-14a to MU-14d and MU-C3 read them |
| Inputs fixed at X1 are not altered before a stage runs (C-6) | `PRE-INPUTS`; MU-14d |
| The check roster is fixed (§6) | `render`'s CONTROL_NOT_GREEN compares `checks.json` with §6's final roster; MU-15b |
| Rendering is deterministic and refuses incomplete or stop-state tables (§9) | RF-1, RF-2, RN-1 to RN-9, RM-0 to RM-5 before `F`; MU-15a to MU-15d after; RENDER in `check --stage final` |
| Patches are the frozen ones and apply exactly (§8) | `controls.py` checks each patch's SHA-256 against §14's table; a patch that does not apply fails the self-test; MU-C3′ |
| The integration branch carries exactly the reviewed bytes (§14) | the reviewer of candidate `F` compares each integration blob with the reviewed staging blob and with §14's table, and checks that the integration commits add nothing else |
| Disclosures are complete (§13) | the reviewer of candidate `F` compares §13 with #1135 comment 6677963479 and the writers' logs |
| Command logs use five categories (§12) | the reviewer of each candidate head compares the drafting log with the commits from `D` and the checkpoint comments |
| Finding 12: (a) and (b) quoted; the D sentence (§15) | the reviewer of candidate `F` checks §0's quotes and the freeze revision's quote of (b) against their sources; the reviewer of `Q` checks the receipt's owner-designation records |
| No computation on the K1 instance before `F` | the drafting log lists only reads, static checks, synthetic-fixture runs and edits; `self-test --synthetic` passes no `--stage` |

## 19. Not authorized

This amendment, and its drafting, authorize none of the following, each of which keeps its own gate: the final code
freeze (§14's table) and authorization (b); designation of `F`; any computation on the K1 instance, its dynamics or its
states, including any run of A or B with `--stage`; any workflow dispatch; execution under authorization (e); designation
of `E`; reconciliation, receipt or merge; and any theorem or claim promotion. Before `F`, the only runs permitted remain
static checks and the predeclared synthetic fixtures of this amendment, run through `--fixture` and
`controls.py self-test --synthetic`.
