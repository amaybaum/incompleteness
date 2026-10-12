# OI-PAIR-MAXCONE-1 — conditional pair-cone proof package

Status: candidate freeze, native V3 draft. Owner direction to prepare this work: ChatGPT,
2026-10-12T04:24:46Z, “Ok let's proceed as suggested”. Parallel design work was authorized
at 2026-10-12T05:10:00Z, “Can we work on both PR's in parallel?” This control plane is
prepared on one PR from D. An instruction to proceed is not an exact-object F or E designation.
The owner designates F only after an all-green workflow_dispatch run held on that exact head.

```v3-round
round OI-PAIR-MAXCONE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-oi-pair-maxcone-1/
record AM verification/receipts/OI-PAIR-MAXCONE-1.json
execution A verification/lean-mathlib/OIBridge/EqvK2Schema.lean
execution A verification/lean-mathlib/OIBridge/EqvK2Converse.lean
execution A verification/lean-mathlib/OIBridge/EqvK2Block.lean
execution A verification/lean-mathlib/OIBridge/EqvK2Generation.lean
execution A verification/lean-mathlib/OIBridge/BridgeDictionary.lean
execution A verification/lean-mathlib/OIBridge/BridgeConverge.lean
execution A verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean
execution M verification/lean-mathlib/OIBridge.lean
execution A verification/lean/oi_maxcone_check.py
execution A verification/lean/oi_maxcone_gaussian.py
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
execution M verification/ROADMAP.md
```

D: f2415108601a9c36bb985b3374c56f0eb34c2962.
D tree: 31b2cd14bdc9e20ec12d153b56718db6294d607c.
D to F changes this preregistration alone. S1 and S2 are linear children after F;
unrelated history enters only in the prescribed reconciliation after E. This non-sealing
round promotes conditional mathematics; it changes no manuscript or other round's record.

## Productivity test and questions

The original design protocol was fixed before its first build. This is stronger mathematics
only if the forcing theorem removes self-duality H3, closedness and assumed ReachPure,
while exposing addition and nonnegative scaling explicitly, and the named kernel reports
contain only standard axioms, with no sorryAx. The actual OI sources remain separately
open. A failed frozen control halts execution under S12; neither a threshold nor an earned
reading is revised after F.

| Question | Named witnesses / checkpoint | Earned scope |
|---|---|---|
| Upper inclusion without H3 or cone closure | subset_Q3_of_maxCone_block | K⊆maxCone and block invariance give K⊆Q3 |
| Lower inclusion without H3 | Q3_subset_of_products_cone_block | Products, addition, nonnegative scaling and block invariance give Q3⊆K |
| Generator form | blockInvariant_of_drive; pairCone_eq_Q3_of_drive_maxCone | CNOT plus every-angle rotation and cyclic invariance derive the required block action |
| Block equivalence | blockInvariant_of_eq_Q3 / pairCone_eq_Q3_of_block_maxCone | Separate directions under stated cone and positivity premises |
| Generator equivalence | driveInvariant_of_eq_Q3 / pairCone_eq_Q3_of_drive_maxCone | Separate directions, retaining the full-flow/cyclic datum |
| Available sharp tests suffice | maxCone_bound_of_sharp_available; subset_Q3_of_sharp_products_block; pairCone_eq_Q3_of_sharp_available | Validity on an available family containing sharpFamily 3 gives the upper bound, without EffectsOn in this direction |
| Actual pair sourcing | Complete I3/I4 review and conditional result template | No source of an actual observer's cone, state/test identification or pair-preserving action is upgraded |

The sufficient subgroup is SU(2)×SU(2). No claim that the resources generate every pair
of arbitrary U(2) blocks is made. A prior one-angle/channel-limit route retains its own
closure assumptions. Six E19 dependencies retain their proof bodies; EqvOneDictionary
is not part of this package and no unneeded design module is imported.

## Frozen S1 files and independent reconstruction

| Destination | SHA256 | Git blob |
|---|---|---|
| verification/lean-mathlib/OIBridge/EqvK2Schema.lean | c76991ba337ac3ac58a41eaa88c46af62e59a374117b31edecabaec9309f6a3e | c634beb82193eb7372ccaf498dba56dd2ec8538c |
| verification/lean-mathlib/OIBridge/EqvK2Converse.lean | 58f97ca9a371b3d14148328a2816f953e6adc0d1067ea383cc802460aae26d56 | f01fc607eab88d8d8ffe24b48d164830e2dad3e6 |
| verification/lean-mathlib/OIBridge/EqvK2Block.lean | 081b99696c104d6e3c4d50d6b9f1b7d5133976f89c9d5410ae5d3067a5b1d0ac | 23c74144073ef001d69c718f1fa3c0be5b8c1896 |
| verification/lean-mathlib/OIBridge/EqvK2Generation.lean | 42c9e313ee35d7f5ee16cf0bee2abde2ad17867d6eaf65a76e5abb2be469c6d3 | 1251afd7aa8667cf73fb8b19a669e6a3d7bb026e |
| verification/lean-mathlib/OIBridge/BridgeDictionary.lean | f32304db1803ee31141f3a805ac9c15c7ea7c02042e6e2234c77f3863850e065 | f997b33ec7ff8402246c7250d38f3e935e4f92df |
| verification/lean-mathlib/OIBridge/BridgeConverge.lean | f1c43d1ca223c8a924a1afee55ee97a661e49079ec757c80df53aa5637de7c42 | e1647b1dc6585073b5b27be2b5e7e13ac803eb0c |
| verification/lean-mathlib/OIBridge/EqvK2MaxCone.lean | 9222038440f742856480706c27569611bed15b82f650b3eab76c9c61e258169f | 5b4b98c8e81e21eb002de25383eada381b65e3dd |
| verification/lean-mathlib/OIBridge.lean | a031136f6c7eddc7c9d5cc0162119dfcd9bb5fa2ec8be996628a99cc94a400c8 | 281b6a52412ea3e51cb412997c9984d5806bad82 |
| verification/lean/oi_maxcone_check.py | d322c9139666c00821fbf85bb2c63dbf5b977ce329dca180bbf652b55c7ca72a | 09d2abcd66f0e230b1a1895e015cb3183297f900 |
| verification/lean/oi_maxcone_gaussian.py | 8e4573f6f5a916202cc5770809809bbbbabd682cc2aefd5d3e4567d2b0282df1 | eff710c93f2211b90472eec8f6d3d5884e3c9421 |
| verification/lean-manuscript-census.json | d23abaf21d73f2410d932f47ff6f29e68fe3d12f482714c462c6276d807eb547 | dd59b8938c12d87be9d3a007900eca2c3020518a |
| .github/workflows/verify.yml | 62fb29a5348e02828044c4e34d8a1281b00c20d4c7e0a5de9aefc5ab43d1535d | 7c85970db08f8326ff3bca86c62cebab1e3159db |

Controls SHA256: c5a13a2f7ae09f705e653a101d48210ac6be018a46dece35bc0ff66c2b85bedd

The seven new module headers describe conditional infrastructure truthfully. The six E19
proof bodies are from dev-equivalence/r5-design f0c36cf9fa8395ac4349d944dc21dda80e4c2658
(design run 38134245361); the MaxCone proof body is from bbcdbab531af5c6ce14d43625e6dc1df16e2063f.
Each body here means every byte after the first header-closing -/, including imports and
axiom-report commands. Only the new headers differ from those measured design sources.

| Module | Preserved body SHA256 |
|---|---|
| EqvK2Schema | 89d4b787eed4a118b19ca5f10778f35b8e35bca64ac10545cf72fef0de6d401d |
| EqvK2Converse | a3781383974dbf7b48d474395d99f7ad110400c41496157febc959adee61777a |
| EqvK2Block | 7117ea8ac51b5a14ff4d9420298469890b74bbd94da82f5901da7767f76bbe08 |
| EqvK2Generation | 2a1b833d13e9acd679748ceba8a0b1e0c1daf3c917b6ea695f911fc942bf9da4 |
| BridgeDictionary | e06a491f0ce1a0c866214b89ebaca1d8cd9a3145727b68a20e6aeb1dc46bd68a |
| BridgeConverge | 7ac67b54b4271e545fd3fa7b9fb6d203d708dcdaa7f25aed8d4b99bcc4321f71 |
| EqvK2MaxCone | 4f12fb1693b6b13843f58f9c562a4c1143e2b2027e730b6350877b0e2d78866a |

The aggregate import has one insertion after import OIBridge.RelcSelectC5:
import OIBridge.EqvK2MaxCone. The registry keeps every original family and supersession
and appends one kernel-only family covering exactly the seven new modules, with manuscript=[]
and explicit conditional scope. No current manuscript family or publication-facing theorem
is strengthened. Kernel-only is the actual disposition, not a claim that a paper carries it.

The workflow changes only five declared splices: the new OI pair maxCone shard, one needs
entry, one result environment variable, one echo and one required-success test. The shard
uses Python 3.11, checkout with fetch-depth 0, the standard-library exact checker and
controls --self-test. Existing jobs and source modules retain their bytes. The controls
reconstruct all five splices, the import and the semantic registry append from D.

| D anchor | SHA256 |
|---|---|
| .github/workflows/verify.yml | bd71bdc270753be8296c4a5c9723e23673c2f8acdaa9417fb70a6ddd6cbe2443 |
| verification/lean-mathlib/OIBridge.lean | e5af9614009889dab616d7f02f75bb395f1ae1fb01307f46ef82d3b282b4c313 |
| verification/lean-manuscript-census.json | cdadb02e0463366c036834f2ca58ae904ad70e05dfe981fd1f37d9bc928e0bbf |
| verification/ROADMAP.md | a64835c2107131530f2396311b3e8fa291bc690462ffbbde225f3479d89a2c2c |
| verification/lean-mathlib/OIBridge/OperationalValidity.lean | ba316747d23820f75f4bbd25105d87a85febb3bd1d0eaa123913b629b34f05f0 |
| verification/lean-mathlib/OIBridge/ImplementationLocality.lean | 4e5b4b22298dfba7b0ee7ba26109ef3090eb48b23227734bb26bbf6834a545ac |

The frozen execution controls compare all twelve output files to their SHA256s and these
anchors to D; bound every changed path; require the preregistration to remain exactly F;
require exact record population; enforce linear ancestry from F; and run the actual checker.
At later heads, CI self-test reconstructs a virtual fixture from the immutable Git blobs
above instead of pinning the live shared workflow, registry, aggregator or kernel. The
owned checker/support and actual checker output remain live regression inputs. A separate
local replay changed every shared fixture file and still passed; actual execution controls
continue to reject every changed frozen output. This is essential for later native rounds
and the parallel transfer successor.

## Execution invariants and checkpoints

| Execution invariant | Checkpoint that measures it |
|---|---|
| The twelve S1 files and controls retain their frozen bytes | Content controls P and C; SHA256 and blob table above |
| The workflow has exactly five splices, the aggregator one import, and the registry one kernel-only family | Independent reconstruction W, H and J |
| Existing jobs and source modules retain their bytes; no unrelated path changes | Changed-path bound G and retained-anchor check L |
| The control plane stays exactly F; execution is linear from F | Freeze check F and ancestry check T; native receipt verifier G7 and S3 |
| The round records are exactly preregistration and controls at S1, with result added at S2 | Record-population check R |
| The exact checker reproduces all 2743 checks with byte-identical stdout, empty stderr and zero exit | Output control V against OUTPUT_SHA |
| Broken trace normalization, adjoint transport and product-test sign are rejected | Checker --self-test: three mutations |
| Content controls accept S1/S2 and reject altered frozen files, scope and output | Controls --self-test: two positive fixtures and 25 mutations |
| The result preserves the conditional earned scope and actual F/S1 identifiers | Exact-template check S and source-audit table |
| Only the specified K2 paragraph changes; K2 stays OPEN and other obligations retain D | Roadmap reconstruction M and changed-path bound G |
| All sixteen named MaxCone axiom reports are standard; no sorryAx occurs | S1/E Mathlib Build axiom-report audit, before E designation |
| Every required host job is green on the exact F and E objects | Held-head workflow_dispatch attestations, checked from host metadata |
| Reconciliation preserves other rounds' shared changes and the round's own execution delta | S9 per-path merits review and native receipt verifier |
| The receipt is valid before landing | v3_verifier --verify-round Q: VERDICT HOLDS |

## Exact controls and their limits

The independent checker reads no research or Lean source, computes in Q(i) with the
standard library, and prints 2743 finite exact checks. Its SHA256 stdout is
492bfc19254a39193222a90e828dc16c4ae58bc434bb00c90f03931c6a0adeee, stderr empty, exit zero. Final line:
MAXCONE-EXACT: PASS; 2743 finite exact checks

Its checks include all 16 scaled Pauli-tensor basis elements and 256 trace pairings;
81 products and 1296 product identities; 169 pure-state block reductions including
zero blocks and complex phases, 338 SU checks and 169 adjoint checks; exact PSD/minor/rank witnesses. Mutations
of the trace factor, omitted adjoint and product-test sign must be rejected. The checker
has an independent Gaussian-rational helper; changing the support file also trips P.
Finite computations are controls, not universal proofs or a full OI model.

The frozen content controls pass two positive fixtures (S1 and S2) and reject 25 mutations:
each of twelve S1 files, workflow reconstruction, import, registry, roadmap, preregistration,
controls, extra record, result overclaim, wrong F, source anchor, stdout, stderr and exit code.
The result check uses the full exact earned template below with four bounded attestation
fields; negated sentences containing kernel-certified, sources H3 or OI implies QM pass.
Appending an affirmative overclaim fails. No context-blind forbidden-word list is used.

## Source audit and family controls

# MaxCone theorem: premise provenance and scope

Certified snapshot: main f2415108601a9c36bb985b3374c56f0eb34c2962. It adds OI-CHANNEL-1 records to the inventory's base 9f9f8257 and changes no kernel definition used below. Reference inventory: research/archive 4dc0321ca2aac6f6aca6f55efc90b7f51330334a, I3 and I4.

## Premises in the new theorem

| Premise | Inventory / current source | Standing for an observer's actual pair cone |
|---|---|---|
| Carrier W 3 and two elementary eball 3 factors | I3.1-I3.3; K1/K2 roadmap; CompositeDimension | Conditional coordinate realization. Local tomography, the elementary ball and its dimension have their own source obligations. |
| Products in K (H1) | I3.43 CandidateCone; I3.147 | Assumed for K. The theorem placing products in maxCone does not place them in arbitrary K. |
| Addition and nonnegative scaling | I3.130 IsConvexCone / PairAdm, design hypothesis | Explicit. These properties were consequences of H3 in the previous proof. Convexity of a normalized body alone is not closure under nonnegative scaling. |
| K subset maxCone | I3.3 definition; I3.43 CandidateCone | Assumed for K. The definition of maxCone is not a source of pair validity. |
| CNOT preserves K (H2) | I3.148; kernel cnot and NativeGate positivity on product inputs | Pair invariance remains additional. Availability of the permutation gate and its product-input positivity do not prove invariance on K. |
| Full rotation flow and cyclic datum preserve K (A_miss) | I3.66, I3.165; E23 source table; E19 exact generator form | Pair invariance remains additional. The full-flow statement includes the cyclic datum and does not follow merely from having a drive on one token. |
| Block invariance | E19 blockInvariant_of_drive, measured design source f0c36cf9 | Derived mathematically from H2 and the stated A_miss. The needed group is SU(2) x SU(2); arbitrary U(2) block pairs are not asserted to be generated. |
| Pure-state reachability | E19 reach_block | Derived in the existing design proof; no ReachPure premise appears in the replacement. |

Self-duality and closedness are absent from the new forcing theorem. In a route that first upgrades a one-angle or channel sequence to the full flow, its own closure assumptions still need to be sourced: absence from this theorem does not remove them from that earlier route.

## The test-side reduction

EFF-1's kernel theorem EffectSpace.maxConeOf_sharp_subset_maxCone proves that sharp product tests suffice for the full maxCone upper bound. The contravariance theorem maxConeOf_anti then gives:

- K subset maxConeOf avail, together with sharpFamily 3 subset avail, implies K subset maxCone.
- This direction does not need EffectsOn avail: that predicate enters EFF-1's reverse inclusion when equality of test cones is asserted.
- It does not assume availability of every affine effect. OG-1/EFF-1 derive sharpFamily subset avail under body preservation, a sharp seed, boundary transitivity and seed-orbit availability (I3.51). Those premises retain their inventory statuses.
- DenseOrbit supplies an alternative involving a dense seed orbit. Availability of limits is a separate issue; positivity of a continuous evaluation extends along a dense family mathematically. No derivation of such an orbit for the observer is supplied here.

Two concrete source obligations remain: validity of the product tests on the actual pair body, and enough available tests to determine the upper bound. They must be traced separately. A possible common principle connecting test validity to operation transfer is a research question, not a proved identification.

## Existing composite and operational validity interfaces

COMP-1's PreComposite.prodEff_effect makes product effects valid on its composite body as a field of an assumed structure. Its Composite.lt is a local-tomography field. These give a precise place to state the requisite test soundness, but neither constructs the observer's composite from the hidden-history inventory.

I4.38 validity_of_implementationLocality derives I4.66 CompositeOperationalValidity on the complex matrix carriers of FiniteOperationalTheory. I4.66 assumes PSD input matrices. To apply this result to dict '' K as the whole physical state space needs an independently justified identification and validity on that space. Identifying it with the PSD cone would already assert K=Q3. It also does not by itself supply the operational context and label premises used to transport a local protocol to a pair.

Repository-wide default-branch searches for maxCone, product effects and implementation locality located EffectSpace, K1Bridge, DenseOrbit, CompositeInterface, K2Guard, the current roadmap, OperationalValidity/ImplementationLocality, and the GR source discussion. The inventory's level and status distinctions are preserved; no unseen source is claimed absent merely because a search returned no hit.

## Exact countercontrols and written family scope

The saved checker measures finite instances and witnesses. The following family statements are separate written arguments:

1. Normalized density matrices contain all normalized product states, obey maxCone, are convex and are invariant under unitary conjugation. They fail nonnegative scaling: a trace-one state doubled has trace two. Hence normalized convexity cannot substitute for the cone assumptions.
2. The PSD matrices with rank in {0,1,2,4} contain all products of two PSD 2x2 states (product ranks are 1,2 or 4), are closed under nonnegative scaling and all unitary conjugations, and obey maxCone. They fail addition: diag(1,1,0,0) plus diag(0,0,1,0) has rank three and is excluded. These properties do not assert topological closedness or convexity.
3. The expanded kappa family of OI-CHANNEL-1 is closed and convex, contains products and is preserved by CNOT and every target channel, as proved in that record's written argument. Its X+ at kappa=3/2 fails a product test: the unnormalized vector (1,0,-1,0) gives -1/2, and the normalized sharp product effect gives -1/4. It is excluded by the replacement bound and is not a full OI model.
4. The zero cone fails H1. The separable cone satisfies product positivity and all local unitary invariances but its |+0> product is mapped by CNOT to a Bell state with a negative partial-transpose minor (-1/4), so it fails H2.

These are controls for the named pair-level premises. They do not establish independence from the full OI inventory. The 68 NOT REACHED rows remain unresolved; B24 needs a model satisfying every applicable row or a precisely scoped OPEN.

## Next decisive fork

The theorem replaces the self-duality obligation in this route with explicit cone structure and test validity. The source audit does not convert these into adopted OI axioms. The next research target is the realization of the pair's test positivity and operation preservation under a single, independently sourced state/test identification. If that cannot be derived, B24's full-model construction must check the entire applicable inventory. Subsequent work retains the K-infinity/K1 origin, arbitrary finite-carrier K_n, and operation/instrument K3 obligations.


## S2 roadmap and exact result note

The sole roadmap splice replaces the K2 paragraph, retaining K2 OPEN, and states the new
conditional theorem and all remaining sources. Every byte outside that uniquely identified
paragraph is D. Its complete predicted SHA256 is a6a4e9e7f5d1e3e363c9abef34e1123002fb1a9494c65bef690450f833b3e160.
The controls reconstruct that one replacement from D; the precise old/new paragraphs are
literal ROADMAP_SPLICE values in the frozen controls. No K∞, K1, K_n, K3 or H-Bell status changes.

The result has exactly this template. Only F and S1 may be replaced by lowercase 40-hex
commit IDs and F_RUN/S1_RUN by positive workflow IDs; the former must equal the actual
freeze and first execution commit. Host metadata separately establishes event, head SHA,
conclusion and job results. Template matching cannot establish host attestations.

```text
# OI-PAIR-MAXCONE-1 — conditional pair-cone theorem

Outcome: OI-PAIR-MAXCONE-1-PROVED

For a set of two-token tables containing every product state of eball 3 and closed under addition and nonnegative scaling, the maxCone upper bound together with CNOT and full rotation/cyclic invariance implies K=Q3. The upper inclusion uses maxCone and block invariance; the lower uses products and cone closure. Available sharp product tests suffice for the upper bound. These conditional statements use neither self-duality nor closedness nor an assumed ReachPure witness.

The block and generator equivalences have separate witnesses: blockInvariant_of_eq_Q3 / pairCone_eq_Q3_of_block_maxCone, and driveInvariant_of_eq_Q3 / pairCone_eq_Q3_of_drive_maxCone. The physical state/test identification, product preparation and cone realization, validity of product tests on the actual pair, enough available tests, and preservation by the gate and full rotation/cyclic actions retain their source obligations. A one-angle or channel-limit route retains its own closure assumptions.

The finite controls do not show that OI implies QM. Nothing here sources H3; neither physical sourcing nor full-model independence is labelled kernel-certified. The 118 reached rows and 68 NOT REACHED rows remain distinct; the latter are unresolved. Arbitrary finite-carrier reconstruction and the full operation/instrument correspondence remain open.

Exact controls: MAXCONE-EXACT: PASS; 2743 finite exact checks
The checker uses Q(i), replay is byte-identical, and its three mutations are rejected. Finite witnesses are not universal proofs. Density states fail scaling; the rank-three-excluded PSD family fails addition; the expanded kappa family fails a product test; the zero cone fails product inclusion; the separable family fails CNOT invariance. Whole-family statements have written proofs in the preregistration at their stated scope.

Design evidence: core 4d7d71d6, run 38205087980, 13 standard axiom reports; sharp-test refinement bbcdbab5, run 38205760341, 16 standard axiom reports. Both Build steps succeeded and their release gates failed only the seven unregistered design modules' census. Predictive execution evidence is recorded in the preregistration. The execution includes the matching proof bodies, truthful conditional headers, the kernel-only registry family, the exact checker and control shard. Six E19 dependency bodies are unchanged; the new MaxCone proof body is unchanged from the measured refinement.

F: {F}
F workflow run: {F_RUN}
S1: {S1}
S1 workflow run: {S1_RUN}

The execution's sixteen named MaxCone axiom reports must be standard, with no sorryAx, and all required host checks must be green before E designation. The owner's E designation and its exact-head workflow attestation are recorded outside this result note and in the receipt. The proof is conditional mathematics; this package supplies no unconditional reconstruction or full-model independence result.
```

## Design evidence and bounded execution

Original design registration and controls were recorded at research/equivalence
a163b9246a98ef100cbf256e51b00e39a1fc564a before the first design run.
Core head 4d7d71d6b1c771e2f6c578b4cdead45d3a63ff96, run 38205087980:
Build succeeded, thirteen standard named reports; the release gate failed only on seven
unregistered design modules at lean-manuscript. Refinement registration at research/equivalence
9430c4635c34ef8f252176925201737a6966235d preceded the next design run.
Refinement bbcdbab531af5c6ce14d43625e6dc1df16e2063f, run 38205760341:
Build succeeded, sixteen standard named reports, 5967 named global axiom reports and no
sorryAx; release gate failed only the same seven-module census. The other eighteen jobs
passed, with the dispatch-only Act42 matrix job intentionally skipped. All44 existing
native receipts held in both runs. These are design evidence, not F/E attestations.

Predictive S1 execution evidence: head 6543cb2f9700ada87cb66384e1049006ae3ad072,
tree 0173c309f02c998d36220d7354b51a880ff1ab3a, run 38208044012, pull_request,
attempt 1, Mathlib job 114675816616. Build succeeded with sixteen named standard MaxCone
reports, 5967 global reports and no sorryAx. The manuscript census and complete release
gate passed; all 44 receipts held. Entire workflow: twenty successful jobs, one intentional
dispatch-only Act42 skip. The maxCone shard passed its 2743-check output and controls'
two positive fixtures / 25 rejected mutations. This completes the three-run design budget.

The predictive tree contains the twelve exact S1 files and controls, D's roadmap and no
result note. The seven proof bodies are the measured ones. Its draft preregistration differs
from this final draft by this evidence entry; all executable file blobs are identical to
the frozen table above. The legitimate kernel-only family resolves the earlier expected
census failure; no manuscript disposition is fabricated. Prospective research checkpoint
8508d17278ea11b90fd37d137172e18a25b3835f preceded this predictive publication.
These are disclosed design results, not a blind prediction or an F/E host attestation.

1. Before F: complete the predictive check, hold the control-plane PR at its proposed exact
   F and dispatch verify.yml on that head. Every job must be green before owner F designation.
2. S1 after F: add the twelve frozen files plus controls.py in one single-parent commit,
   retaining D's roadmap. Run controls HEAD --freeze F, mutation tests and CI; the Build must
   emit all sixteen named standard reports with no sorryAx and the release gate must pass.
3. S2: add the exact result note and only the roadmap splice. Run the frozen controls;
   hold E for an all-green exact-head workflow_dispatch run and owner E designation.
4. Reconcile under S9 even if the current base has not advanced; resolve any differing
   shared rows by merits. Build a receipt-only single-parent Q, require v3_verifier
   --verify-round Q to print VERDICT HOLDS and obtain exact-object landing authorization
   before ordinary review and merge. No native validity is inferred from a green PR badge.

Any failed frozen check halts the round under S12; it does not license editing the control
plane. A halt also requires the governed record, reconciliation, valid receipt and normal
landing review. The theorem and source audit leave bare OI reconstruction and full-model
independence open. The transfer successor has its own design and adoption scope and is
not assumed to be part of this round.
