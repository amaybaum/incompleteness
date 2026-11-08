# Canonical axiom identity channel — design only (#1162)

This is the normative D-AX companion to [HARDENING-DESIGN.md](HARDENING-DESIGN.md).
It applies the owner's canonical-kernel-identity choice in
[#1031 c.6691759997](https://github.com/amaybaum/incompleteness/issues/1031#issuecomment-6691759997)
and the independent review's R1–R3 at
[#1172 c.6691575360](https://github.com/amaybaum/incompleteness/pull/1172#issuecomment-6691575360).
Writer: ChatGPT Work `/root`, scope checkpoint #1162 c.6709997368. The prior writer's
fixtures and results remain intact at `2b08dbe0ee4b82bb60019f9cb97af492dd892bd6`.

No reporter, checker, workflow, fixture execution or migration is implemented here.
The controls below are hand-derived specifications, not Lean experiments or observed output.
Independent review of an immutable pushed revision precedes any implementation decision.

## 1. Source basis and decision

Sources were read at Lean v4.33.0 commit
`d8b18978322de05a8f3dba51ef03cf5461676c17`:

- [`Lean/Elab/Print.lean:240`](https://github.com/leanprover/lean4/blob/d8b18978322de05a8f3dba51ef03cf5461676c17/src/Lean/Elab/Print.lean#L240):
  `elabPrintAxioms` resolves the source identifier with `realizeGlobalConstWithInfos` in its
  command context, then calls `printAxiomsOf` for each result. `printAxiomsOf` obtains the
  actual axiom Names with `collectAxioms` before formatting any message.
- [`Lean/Message.lean:276`](https://github.com/leanprover/lean4/blob/d8b18978322de05a8f3dba51ef03cf5461676c17/src/Lean/Message.lean#L276):
  raw Name formatting differs from `MessageData.ofConstName`; the latter is used for each
  listed axiom. Pretty-printing is not an injective kernel-identity channel.
- [`Lean/PrivateName.lean:18`](https://github.com/leanprover/lean4/blob/d8b18978322de05a8f3dba51ef03cf5461676c17/src/Lean/PrivateName.lean#L18):
  private Names retain a `_private` prefix, module components and a numeric component.
- [`Init/Meta/Defs.lean:101`](https://github.com/leanprover/lean4/blob/d8b18978322de05a8f3dba51ef03cf5461676c17/src/Init/Meta/Defs.lean#L101):
  identifier and escaping rules are display rules. `_inaccessible` satisfies the character
  grammar and is also recognized by `Name.isInaccessibleUserName` at lines 151–154.
- [`Lean/Util/CollectAxioms.lean`](https://github.com/leanprover/lean4/blob/d8b18978322de05a8f3dba51ef03cf5461676c17/src/Lean/Util/CollectAxioms.lean):
  collection uses precomputed axiom entries from imported modules and does not cross module
  boundaries. Trusting a stale intermediate imported artifact can therefore preserve stale
  axiom information. This motivates the full transitive cache-validity contract below; no
  failure of an actual build is asserted.

**Decision:** the authoritative input is the actual resolved declaration Name and the actual
Names returned by `collectAxioms`, before any pretty-printer, alias or display conversion.
Namespace opens, aliases and local `pp.fullNames` options may change how a message looks;
they cannot change the accepted identity by changing that message. The existing conservative
source/diagnostic parser remains an additional check, not the origin of canonical records.

The threat model is accidental or adversarially selected source names, missing/misattributed
reports and stale artifacts, under a trusted pinned Lean/compiler, reviewed reporter and
reviewed build wrapper. It is not a sandbox against arbitrary malicious native code inside
that toolchain, dependencies or elaboration plugins. Hashes bind artifacts to inputs; they
are not signatures and do not make an untrusted producer trustworthy. A future implementation
must name and review this producer/dependency boundary before claiming a production guarantee.

## 2. Where the channel comes from

The proposed implementation target is a separately reviewed instrumentation of the pinned
Lean command reporter at the source points above. This is a proposed mechanism, not a claim
that stock Lean already supplies the bundle. It preserves the command's original resolution
and `collectAxioms` calls and exports their results before generating the ordinary message.
It does not reconstruct a Name from a diagnostic, parse a final name component, or re-resolve
the identifier later in a different namespace/environment.

For each elaborated `#print axioms` command, the producer emits one command record containing:

1. Module identity/path, source-byte digest, command byte span, and line/column at `#print`.
2. The complete ordered array of resolved declaration Names. The normal case has exactly one;
   zero is an error, and multiple distinct resolutions give AMBIGUOUS even if all are allowed.
3. For each resolved declaration, its complete set of collected axiom Names. An empty axiom
   set is explicit; absence of a command record is never interpreted as an empty set.
4. Protocol version, reporter/toolchain identity, and module environment/import binding.

Records go to a dedicated structured module artifact produced by the instrumented reporter,
not a recognizable line in stdout. Ordinary `logInfo` text cannot create or replace a record.
The build wrapper accepts artifacts only from the pinned reporter invocation/cache protocol,
validates their manifests and supplies their directory to the checker as `--identity-bundle`.
Any implementation that cannot maintain this producer boundary must stop for design review;
accepting arbitrary JSON text found in a log is not an allowed substitute.

The wrapper inventories every scoped source module and binds the artifact manifest to exact
source bytes, the **complete transitive imported-artifact and compilation-input closure**,
Lean and reporter binaries, dependency lockfile, build options, and schema version. This closure
includes dependency modules outside the print inventory. For each imported module it validates
the compiled artifact against its current source/build inputs and recursively validated imports,
anchored in the current resolved dependencies and trusted toolchain, not just a cache's own old
manifest. An unchanged direct-import hash does not certify that the imported artifact is current.
Unknown or unverifiable closure inputs fail; they require rebuilding under the authorized wrapper
or a reviewed equivalent validity proof. A trusted immutable prebuilt toolchain/dependency bundle
must bind its whole included closure. Each scoped module has one manifest entry, including a
module with zero print commands. Deleted or extra modules, stale source digests, incomplete
commands or unexpected artifacts fail. The output is finalized only after successful module
compilation; partial output from a failed compilation cannot certify the module.

**Cold and warm builds.** The cold comparison requires each scoped module to be compiled with
the reporter and its artifact finalized; an existing uninstrumented `.olean` is insufficient.
For the warm comparison a module may be rebuilt or its *complete artifact plus compilation
product* reused, only after all the binding inputs above agree. Otherwise it must be rebuilt
under the separately authorized wrapper or the gate fails. A top-level manifest records the
current invocation, the complete inventory, and whether each artifact was produced or reused.
It must not copy a successful status from an earlier invocation. Cold and warm build exit
statuses are captured independently by the outer runner and both must be zero (R1).

The source census, diagnostic messages and canonical command records are cross-checked by
module/position. No command record may serve two prints. Every parsed print needs one canonical
command record; every canonical command in scope needs one parsed print. The conservative
source parser can therefore cause safe false failures for unsupported source forms. This design
does not claim to discover every theorem that ought to have a print. Dependency modules are
outside the scoped print inventory, but imported axioms collected for an in-scope declaration
are included and checked regardless of which dependency declared them.

**Invocation.** In the existing no-log `--require-lake` mode, the future checker invokes this
trusted wrapper and receives its bundle and actual status internally. If the wrapper is absent
or fails to supply a valid bundle, the checker fails. For an external `--log`, the caller must
also supply `--identity-bundle` containing its validated build-status manifest; the checker must
not fabricate a zero status or obtain records from a different invocation. Each normal invocation
checks its own build; the migration comparison separately requires successful cold and warm runs.

## 3. Lossless Name representation and exact allowlist

A Name is an array of constructor-tagged components from the anonymous root:

- `[]` represents `Name.anonymous`.
- Appending `["str", s]` represents `Name.str parent s`, with the exact Unicode scalar sequence
  in `s`. JSON escaping is decoded once. No NFC/NFKC, case folding or alias expansion occurs.
- Appending `["num", n]` represents `Name.num parent n`, where `n` is a canonical decimal
  string for a natural number: `"0"` or a nonzero digit followed by digits. JSON floating-point
  numbers, signs, leading zeros and exponent notation are rejected.

Thus a numeric component `[["num","0"]]` differs from a string component
`[["str","0"]]`; one component `[["str","Classical.choice"]]` differs from
`[["str","Classical"],["str","choice"]]`. Private, inaccessible and macro-scope components
are retained exactly; none are stripped. The tagged representation covers all three Name
constructors, even when display text cannot be round-tripped. Empty Names cannot be declaration
or axiom identities: those are malformed records. A diagnostic that fails its conservative
grammar still fails the combined gate; lossless identity does not waive that check.

The only permitted axiom identities are exactly:

```json
[
  [["str", "propext"]],
  [["str", "Classical"], ["str", "choice"]],
  [["str", "Quot"], ["str", "sound"]]
]
```

Identity equality is constructor-by-constructor equality, never equality of a dotted rendering.
The serialization is injective: the outer list length and each tag determine the constructor
chain; each string or natural component is preserved, so equal encodings reconstruct equal Names.
Conversely, reconstructing then serializing every accepted encoding yields the same tagged
value. Ordinary JSON whitespace is irrelevant; duplicate object keys, unknown schema versions,
extra fields in fixed records, unknown tags and malformed component values fail closed.

The producer emits axiom Names as a set without duplicates; duplicated entries are a channel
error rather than silently deduplicated input. Sorting for deterministic JSON uses a documented
lexicographic order of tagged values and exact scalar sequences; it never affects identity.
Byte-identical checker output is required for identical complete inputs, including provenance.

## 4. Checker consumption and failure rules

The checker validates the bundle schema and all source/build bindings before authorizing any
axiom result. It attaches canonical records by module/command position, checks the source span
and diagnostic declaration consistency, and records the full canonical Name of every matched
declaration and axiom. The diagnostic declaration Name must agree component-wise with the
canonical declaration (numeric and escaped components distinguished); agreement with the
written source remains the companion design's conservative suffix guard. The axiom strings
in the pretty-printed message are not compared to the allowlist and cannot substitute for or
override the canonical axiom set.

| Finding | Trigger |
| --- | --- |
| IDENTITY_MISSING | No bundle, module artifact, finalization marker or canonical record for a required print |
| IDENTITY_FORMAT | Invalid schema, duplicate keys/axioms, unknown fields/tags or invalid/empty identity |
| IDENTITY_BINDING | Source, import, toolchain, reporter, option, inventory or current-build binding differs or is absent |
| IDENTITY_MISMATCH | Canonical declaration/position disagrees with the attached diagnostic/source record |
| DUPLICATE / AMBIGUOUS | Repeated command records or multiple resolutions, as in the companion matching policy |
| ORPHAN | An in-scope canonical command cannot attach to a parsed print |
| AXIOM | Any collected canonical axiom Name is outside the exact three-element allowlist |
| BUILD | The outer runner records any missing/nonzero cold or warm build exit status |

All earlier source/diagnostic failures remain, including SORRY and EMPTY. A complete revised
PASS requires both layers, successful build statuses, and successful self-tests. The production
path has no text-only compatibility mode. Old fixtures remain useful for the diagnostic layer;
their absence of canonical artifacts would correctly fail the complete checker.

Private declaration policy (R2): a target such as `_private.M.0.OIBridge.A.foo` can pass when it
is exactly the reporter's kernel Name and its suffix matches the written `foo`. The full Name
is stored. Printing it does not make its axioms private or permitted; each axiom is separately
checked. Neither this policy nor source inspection establishes a real pretty-printer exploit.

## 5. Predeclared paper controls

Each row gives a controlled mutation of an otherwise valid bundle/source/diagnostic fixture.
“Pass” assumes the stated genuine Names came from the trusted producer; it is a hand-derived
checker expectation, not a claim that a synthetic record proves those premises. Before any
implementation tests, exact fixture bytes and full expected findings must be committed and
independently reviewed, including canonical companions for the historical 34 fixtures.

| ID | Pair or mutation | Required outcome and reason |
| --- | --- | --- |
| K01 | Genuine `Classical.choice`; display `Classical.choice` versus `choice` under namespace/open/alias presentation | Both pass canonical AXIOM; identical Name. The print target still obeys the source guard. |
| K02 | Replace K01's axiom with `Other.choice` while retaining display `choice` | Fail AXIOM; final/display spelling cannot mask the different kernel identity. |
| K03 | Genuine `propext` versus `Other.propext`, with identical allowed display text | First passes, second fails AXIOM. |
| K04 | Genuine `Quot.sound` versus the one-component Name `«Quot.sound»` | First passes, second fails AXIOM; escaped dots do not create namespace components. |
| K05 | Toggle a local `pp.fullNames` option or permitted axiom display alias while keeping genuine kernel Names | Canonical verdict unchanged; never infer this from a source-wide default. |
| K06 | Private declaration `_private.M.0.OIBridge.A.foo`, written `foo`, empty axiom set, exact diagnostic and canonical Name | Pass; retain prefix and numeric component in the result. |
| K07 | Change only K06's diagnostic numeric component `0` to `1` | Fail IDENTITY_MISMATCH; suffix agreement alone cannot establish identity. |
| K08 | Change K06's written name to `OIBridge.B.foo` | Fail MISMATCH despite same final component and otherwise valid canonical record. |
| K09 | Add private axiom `_private.M.0.propext` to K06 | Fail AXIOM, whatever display is supplied. This is a synthetic identity test, not an observed exploit. |
| K10 | Change K06's canonical numeric component to a string component `"0"` with the original diagnostic unchanged | Fail IDENTITY_MISMATCH; string and numeric constructors are distinct. |
| K11 | Source/diagnostic `_inaccessible`, matching canonical declaration Name, empty axiom set | Pass these identity/grammar rules; the grammar makes no false semantic exclusion claim. |
| K12 | Two distinct Unicode scalar sequences or macro-scope component chains are substituted for one another | Fail identity equality/matching; no normalization or erasure is allowed. Valid identical pairs pass where the diagnostic grammar accepts them. |
| K13 | Remove a canonical record but retain clean diagnostic text | Fail IDENTITY_MISSING. Remove the entire bundle: same failure. |
| K14 | Change a source digest, import binding, reporter identity or options; retain all clean diagnostics | Fail IDENTITY_BINDING. Exact bound positive must pass. |
| K15 | Zero, two distinct or two identical resolutions/records at one print | Zero fails; distinct resolutions AMBIGUOUS; duplicate command record DUPLICATE. Single resolution is the positive. |
| K16 | An explicit empty axiom set versus an absent set/finalization marker | Empty set passes; absence fails format/missing. |
| K17 | Warm build exits nonzero but reproduces identical clean records and cold exit is zero | Fail BUILD; both-zero pair passes. Missing status also fails. |
| K18 | Warm cache artifact has changed source/import input or comes from an uninstrumented module | Fail binding/missing; exact finalized artifact reuse with successful current status passes. |
| K19 | Put a valid-looking JSON record only in stdout | Fail IDENTITY_MISSING; the trusted artifact channel remains absent. |
| K20 | Unsupported schema/tag, duplicate object key/axiom, noncanonical numeric value, empty declaration Name | Fail IDENTITY_FORMAT; canonical corresponding inputs pass. |
| K21 | A imports B, B imports C; C's current source/build inputs change while cached A and B bytes/manifests retain the old closure | Fail IDENTITY_BINDING even if A's direct-import B hash is unchanged. A fully validated current A→B→C closure is the positive; replaying the whole old closure against current inputs also fails. |
| K22 | No-log mode receives a valid bundle/status from the trusted wrapper; external-log mode omits its bundle | No-log case passes with the other controls satisfied; external-log case fails IDENTITY_MISSING. Missing wrapper or status also fails; neither mode has a text-only fallback. |

Required future channel mutant D01 replaces only the canonical AXIOM allowlist comparison with
exact equality of displayed strings against `propext`, `Classical.choice`, `Quot.sound`, keeping
all other checks. K03's forbidden Name displayed as `propext` kills it by changing FAIL to PASS;
K01's genuine `Classical.choice` displayed as `choice` kills it by changing PASS to FAIL. K02
does not kill D01: its display `choice` also fails that mutant's exact display allowlist.

Other required future channel mutants: split rendered
dots (K04); strip private prefixes (K09); conflate numeric/string components (K10); normalize
Unicode or erase macro scopes (K12); trust text fallback (K13/K19); ignore binding/cache
identity (K14/K18/K21); validate only direct-import hashes while trusting stale intermediate
manifests (K21); borrow cold status for warm (K17); waive missing external-log bundles (K22).
A reject-all mutant is killed by the
positive members. These are paper expectations; no actual mutant has been run. M01's separate
two-part historical text-layer semantics are specified in HARDENING-DESIGN §7.2 (R3).

## 6. Next gate and stopping rule

The revised design and hand-derived controls need independent exact-head review. Before
implementation is authorized, the reviewer must find a complete, feasible producer-to-checker
contract and no identity fallback. Implementation authorization must explicitly cover the
reporter instrumentation and build/cache wrapper, not just a Python parser. An alternative
transport requires the same reviewed contract; it cannot be substituted without review.

Any implementation proposal that cannot preserve actual kernel Names, bind every scoped
command to its source/environment, distinguish both build statuses, or maintain the trusted
producer boundary stops at that precise gap. Fixture execution, real-build comparison,
replacement and integration each remain at their recorded authorization boundaries. Passing
ordinary PR CI would not execute or validate this unimplemented design.
