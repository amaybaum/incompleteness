# Node 8 amendments

Amendments to the frozen preregistration (`PREREG.md`, sha256
`ca5f976071f3dc257c0e4abefff9b782c9eca0db9c06ddffea8df69f486bf9dd`, committed at `382fc9e4`). `PREREG.md` is not
edited. PREREG §19 requires amendments under `amendments/` with time and reason, before the computation they touch.
Each entry gives its date, its source, its reason, and the state of knowledge when it was written. No entry changes a
decision clause in a candidate's favour.

**State of knowledge when A-1 and A-2 were written (2026-10-21, 03:55 UTC).** No probe of step 2 had been run. The
quote check (I-12) had been run: 84/84 fragments pass at the drafting commit `a501b418`; at `382fc9e4` the fragment
`mc-node7/NODE.md:82` ("provisional on K-10 at n = 4") no longer matches, node 7's record having moved after K-10's
CI confirmation (§0). No operational state space, access class, pure set or purification clause had been computed for
any class. The expected shapes recorded in PREREG §0 and §6.10 were known; nothing else.

***

**A-1. Owner's interpretation rule for every purification verdict (owner, 2026-10-21; relayed by the coordinator).**
Written before any verdict line of step 1 was generated.

Owner's text, verbatim: "Interpretation rule (owner). A successful purification witness demonstrates what the
specified realization permits, not that observational incompleteness universally produces purification. Equally,
failure to reconstruct exact quantum mechanics in these small realizations does not by itself disprove OI or its
finite-precision (A2) predictions. Operational access, finite-set purification and convex-closure purification are
reported separately, and finite-model success is never classified as an exact quantum reconstruction."

Enforcement in the step-1 probe (`probe/p8s1.py`):
- every generated purification line is produced by one function that takes the class name and the reading
  ("preparable set, budget m" / "across the declared theory" / "convex closure") as mandatory arguments and prefixes
  the line with them; no purification line is printed by any other code path (a static scan of the probe source
  checks that the only `print` of a line containing "Pur-E" or "Pur-U" is inside that function);
- the access class (I-58), the finite-set reading and the convex-closure reading (I-59) are printed as three separate
  blocks per class;
- the generated text is scoped to "the class <name> under reading <r>"; a scan of every generated verdict line
  rejects the words "OI", "observational incompleteness", "in general", "universally", "quantum mechanics",
  "quantum reconstruction" and "QM" in a purification line (check `A1-SCOPE`), so no line says or implies that OI in
  general produces or fails purification, and no finite-model result is classified as an exact quantum
  reconstruction (I-59's unit test, KM-34).

**A-2. Confirmatory review of the frozen bytes (`scratchpad/mc8/review/REVIEW-confirm-frozen.md`, relayed by the
coordinator, 2026-10-21).** Written before the affected mutants ran and before any verdict line printed.

Defects, each fixing a mutant definition (PREREG §14):
- **D1, KM-31 (PREREG l. 1119).** Under the timing convention (§6.10) one waiting step already reads x₁ = h in
  K-SWAP, so a one-step-only computation still reports full access. The mutant's case is replaced by: "the access
  class computed from zero-step protocols only (readout of x₀)"; I-58 must catch it (K-SWAP's class must print full
  hidden access).
- **D2, KM-32 (l. 1120–1121).** On ℛ₁'s grid the preparable-weight rule also gives only δ₀, δ₁ as pure, so the
  mutant's output may equal the correct output. The fixture is replaced by one where the two rules provably differ:
  state set {δ₀, δ₁, (1/3, 2/3)} with mixing weights {0, ½, 1}; the correct (preparable-weight) rule gives three pure
  states, real convex combination gives two. I-54's check runs on this fixture.
- **D3, KM-33 (l. 1122–1123).** diag(1/3, 2/3) has rational entries and passes the field check; it is caught by
  I-57's closure enumeration (H ω H† is not an instance state). The closure enumeration is named as the catching
  check. (Not run in step 1: the QM instance belongs to the controls of step 3.)

Notes, same source:
- §16's non-gem rule for the full-access classes (l. 452–454; l. 1192 names ℛ₁ᵃ, ℛ₂ᵃ, K-SWAP and CL-C4) applies only
  if I-58 prints full access for that class; full access is never asserted before I-58 measures it. The probe prints
  the access class before any Lemma A instance is reported.
- I-50 (l. 1279) covers the ℛ₁, ℛ₂, K-SWAP and CL-C4 outputs; l. 1059's "QM must satisfy all" is narrowed to the QM
  row as scoped in §6.5.
- **CL-C4's inputs (l. 610–611), fixed explicitly.** Initial x: x₀ ∈ {0, 1}, each a visible point mass fixed by the
  protocol (node 6's P1 varies x₀ across histories; K-SWAP has x₀ = 0 only). Prior: the realization-datum prior on h
  with denominator ≤ 8, with the preparation bijections of the hidden cells, as K-SWAP. Composites: as ℛ₁ (two copies,
  one shared hidden counting-measure ancilla, local accessible class).
- **Shared ancilla, reading fixed.** Each copy's local preparation bijection may be *controlled by* the shared hidden
  ancilla s (it reads s) but acts on the copy's own hidden cells (h and its own hidden ancillas) only; no local
  preparation writes s. This is the reading consistent with "the joint accessible class is the local permutations and
  local coupling steps of each copy only" and with the ancilla's declared role, mixing (§2.2): s selects which local
  preparation each copy performs, so correlated composite states exist as 1/2-mixtures of two product preparations.
  The alternative reading, in which a copy's preparation may also write s (so that one copy's prior reaches the other
  through s), yields a different preparable set; the probe exhibits one exact element of the difference as a
  sensitivity row (`SHARED-ALT`), which decides nothing.
- KM-36's catching check is the mechanical 60/30/1 (and 6/1) count, and I-3 cites KM-36. (Step 3.)
- K-IF on SPK-conv: print the extreme points and the closure's description, not a size. (Step 3.)

Also fixed here, because the frozen text leaves them to the executor and they are needed before §6.10 runs:
- **I-55, the equivalence domain.** §13.1 names two options and Q-FIN (step 3) has not run, so the domain declared
  before §6.10 is the first option: a fixed finite carrier and finite horizon, the carriers being exactly the Ω of the
  §6.10 classes and the horizon the protocol depth the probe prints. It is printed with digest before §6.10.
- **Budgets.** "Up to three hidden ancilla bits" is read as the budgets m ∈ {0, 1, 2, 3}; the class's declared budget
  for the per-budget purity line is m = 3, and the mixing weights of budget m are {k/2^m : 0 < k < 2^m} (so m = 0
  admits no mixing operation and every preparable state of that budget is pure by the definition; this is printed as
  the definition's consequence, not as a finding). "Across the whole declared theory" is the union of the preparable
  sets of every class of the family at m = 3, with weights {k/8}. In a composite the shared ancilla adds the weight
  1/2, which {k/8} already contains.
- **Visible ancillas.** The probe checks statically that φ and every coupling step read and write only x (x₁, x₂) and
  hidden cells; the visible ancillas are then relabelings of a register the observer already knows, and the
  transformation list is enumerated over the permutations of the core visible cells with that certificate printed.
