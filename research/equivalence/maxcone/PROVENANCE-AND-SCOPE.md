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
