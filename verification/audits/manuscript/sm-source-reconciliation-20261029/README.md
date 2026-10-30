# SM, recurrence and stationary-law source reconciliation

Base: main `ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf`. Successor source reconciliation for #962, #967 and #971 under #946. Original branches and their evidence remain intact; forward timing-tail normalization is recorded below. Source corrections are applied forward and FULL is propagated. The prior canonical publication verification and scoped source acceptance are recorded below; the integration-review follow-up is a new candidate. No merge authorization is claimed.

Applied scope: common-time return versus Poincaré recurrence; C2 conditional-memory versus P-divisibility; state/representation and type-II/de-Sitter limitations; finite-cycle invariant distributions; exact modular-linear versus rounded versus geometry-dependent maps; open stationary-law and pseudofermion measure hypotheses; lcm/Landau/uniform-random period distinctions and map-specific bounds. The written finite class theorem and finite controls are not Lean certificates or physical ergodicity proofs.

Current main's restricted onsite Theorem 3 and its K3 directional witnesses are preserved. SC-32 #969 remains a separate publication dependency: its normalized second-order update-center theorem differs from that first-order onsite theorem. Its Lemma 3a/Theorem 3/Proposition 3b require distinct identifiers and the recorded K1/K1/P evidence boundaries. Reusing the onsite certificate or its ID for that different statement is not permitted here.

SC-17 #963's non-Bell selector/chirality/Higgs summaries remain open: Explainer dynamics selection/Higgs-from-one-condition and book ch05's center-independence equivalence need that theorem-scope reconciliation. The Bell workstream owns Bell/entanglement corrections. This PR does not close #963/#969 or modify Introduction #918. Exact-current-source review, final propagation sweep, bounded replay, canonical builds, rendered-page inspection and fresh ordinary PR CI remain required. No merge, release, F/E designation, special dispatch or old-PR closure.

Independent source review of `fc058b2a4d38b2f7647bd7328a528f5b78295a33` found a retained covariance error in the measure argument. The follow-up separates a Gaussian action kernel from its covariance: for positive-definite regulated M, det M is proportional to the complex Gaussian integral with action chi* M^-1 chi, whose covariance is M. The scalar-to-determinant measure and observable map therefore remains open independently of stationary-law/Gaussian sampling. The same correction reaches §6.5 and gaps (i)/(ii)B. The uniform invariant shell ensemble is distinguished from an occupied orbit's empirical law; fragmentation refutes the single-cycle sampling claim, not existence of the invariant ensemble. Primary-source provenance: Albergo et al., Phys. Rev. D 104, 114507 (2021), §II.B Eq. (9), DOI 10.1103/PhysRevD.104.114507; the finite Gaussian identity also follows by diagonalizing M.

The b60d5c6c source recheck accepted the covariance/ensemble repairs and identified one further conclusion beyond the Part A algebra: time-swap invariance establishes equal slice expectations, not temporal factorization or the 3D/4D measure bridge. The follow-up states that exact symmetry and keeps the further measure identification open. No canonical statement or proof grade changes.

## Prior canonical publication checkpoint at ce03041c

Scientific source acceptance is recorded on #999 at `987e7d449f1951b93e7a788fe254fbc8af7ee744`, review 5697813064. This acceptance covers the declared source correction, including the complete modified measure argument and its dependents. It does not close the explicitly retained SC-32/SC-17 dependencies or authorize publication/merge. The artifact follow-up changes publication TeX/PDF and this verification record only; manuscript and ledger source blobs remain those of the accepted source.

Canonical commands: `sh ./build.sh Explainer GR Juno Main SM Structure Substratum` and `sh ./build.sh --book`. SM was rebuilt after the final scoped amendments using `sh ./build.sh SM`. All completed successfully with no dropped glyphs. Final pages: Explainer 70, GR 88, Juno 22, Main 96, SM 150, Structure 98, Substratum 55, book 559. Median nonspace characters per page are respectively 2446, 2588, 2054, 2711, 2514, 2477, 2657 and 2561. Representative rendered pages SM 31/33/112 and book 396/411 were inspected; no clipping or layout fault was found.

`python3 tools/staleness_check.py` passes with all 13 stamps matched. `python3 tools/coverage_check.py` passes with all 133 canonical statements. `python3 tools/voice_check.py` and `git diff --check` pass. The full restricted onsite Theorem 3/proof/scope block is byte-identical to pinned main; ledger comparison confirms identical IDs, grades, evidence mappings and deltas, with only the stated past-hypothesis GAP fingerprint reaffirmed. The added-line credential/email/local-path scan is clear.

Bounded smoke only, not full retained-output replay: SC-31's Landau dynamic program agrees with its partition maximum through n=20, every cycle type through n=12 divides the universal lcm bound, and all 81 states of the q=3, L=2 exact linear rule satisfy bijectivity, modular-energy invariance and the finite order bound. Heavy retained enumerations and Lean suites remain for ordinary CI. Fresh final-head CI, independent source-identity reanchoring of this artifact follow-up, final integration with the other correction workstreams and owner approval remain separate gates. No source unit is closed by these local checks.

## Integration-review follow-up and supersession crosswalk

Requirements: #999 comment 6497991912 on `ce03041cd13d46315e2b48f67aad5b33efab4848`. The SHOULD-FIX findings are publication blockers until the revised candidate passes review. Prior acceptance and green CI apply to ce03041c, not automatically to this follow-up. The source-only checkpoint ddf4aae5 flagged canonical TeX/PDF as STALE; rebuilt-candidate verification is recorded below. No grade promotion or closure follows from these corrections.

The SC28/SC34 source tables retained from the old PRs are historical records of those candidates. Their rows below are explicitly superseded as statements of the current source. Those historical rows are preserved; this mutable crosswalk and the maintained manuscripts supply the current interpretation.

| Historical record / row | Current disposition and authoritative source |
|---|---|
| SC34 README, site table SM :290 and :292; gap (i) at :1221 | Superseded where the row reduces measure equivalence to stationary-law/Gaussian sampling alone. SM §4.2 and gap (i) separately leave the scalar stationary law/Gaussian limit and scalar-to-determinant measure/observable map open. Action kernel M^-1 gives covariance M. Uniform invariant ensembles need no single-cycle ergodicity; an occupied orbit sampling the whole shell does. |
| SC34 README, SM :805 | Superseded: the free-sector correspondence is not established at Level 2 even given the stationary-law hypothesis. SM §6.5 retains the independent measure/observable-map obligation. |
| SC34 README, SM :807 | Superseded where its two-condition summary omits the scalar-to-determinant measure/observable map. The scalar law, that map and the proposed gauge-map principle carry separate obligations in SM §6.5. |
| SC34 README, SM :1223 / gap (ii) | Superseded where symmetry is read as temporal factorization or full 3D/4D measure identification. Part A proves time-swap invariance/equal slice expectations on a T-invariant uniform shell; identifying a realized orbit with that ensemble and Part B's measure/observable bridge remain separate. |
| SC28 README, SM §7.5 bridge gap (ii) row | Superseded: Part A's shell symmetry needs no cycle ergodicity. Orbit-to-ensemble identification and Part B's stationary-law and determinant-measure/observable-map obligations are open as stated in SM §7.5. |
| SC34 README, reproducer/docstring/README row | The claimed code propagation did not hold at ce03041c. This follow-up changes `lyapunov_v3.py`'s documentation, output and exit-status criterion to finite separation to saturation, independently of fitted slopes, and aligns the expected-output table. No positive Lyapunov-exponent theorem or realized-hidden-sector mixing is claimed. |
| SC34 README, rows equating measured rounded-map diagnostics with the realized hidden sector; SM :298/:1412 constraints | The rounded candidate and exact A5 rule are distinct. Main's ETH remark/posit (v), Substratum's mixing discussion, SM §8.3 and Juno retain the open physical identification and mixing hypothesis. Tested quadratic-energy sets of the rounded map are not invariant; the existence/sampling of a suitable shell is open. |
| SC34 replay notes concerning trailing `real/user/sys` durations | Those shell-timing tails are removed from the current forward copies of s1/s2/s3 outputs. All nonblank scientific result lines are unchanged; original timed bytes remain at ce03041c and the original PR heads. No heavy replay or new scientific result is claimed by this normalization. |
| SC31/ch18 global-cycle wording and finite-recurrence headings | The no-global-cycle consequence is scoped to nontrivial rules fixing zero. §18.7 and its run-in/summary headings say exact finite recurrence; genuine Poincaré-theorem references remain. |

Per-finding disposition: (1) separation script and expected output corrected; (2) verification README names the stationary law and separation dynamics; (3) measured rounded diagnostics no longer establish realized-hidden-sector mixing; (4) exact A5 versus rounded candidate and shell noninvariance are explicit; (5) this crosswalk supersedes stale audit rows and the obsolete pending sentences are removed; (6) the exactly-linear period implication is one-way; (7) zero-fixed cycle scope is explicit; (8) finite-recurrence headings aligned; (9) redundant rho phrase removed; (10) numerical diagnostics indicate non-integrability rather than proving it; (11) nondeterministic timing tails removed forward; (12) normalized prime-field alpha=1/d requires p not dividing d. The restricted onsite K3 statement, Lean sources and every proof grade remain unchanged. #969 and #963 non-Bell residuals stay open.

The review's three explicitly pre-existing out-of-scope items (cubic dispersion shorthand, uncited standard-interpretation sentence and Main's exponential-time wording) are not claimed fixed by this bounded follow-up. The rebuilt-candidate verification is recorded below; independent exact-candidate review is requested after publication.

The default separation reproducer and its bounded identical-twin countercontrol are
added to the existing ordinary `Numerical probes / core B` step sequence, with
exit-status verdicts and no new workflow event. The default L=20/q=2^16/400-step
replay remains for CI. The new `--no-perturbation-control` mode runs the actual map at
L=4/q=256/80 steps and succeeds only when separation is zero and saturation fails on
every seed. Fitted slopes remain diagnostic only. This is an explicit workflow/code
follow-up; the prior artifact-only/no-workflow-change descriptions apply only to
ce03041c and not this candidate.

A same-claim recheck also found stale Lyapunov/SM-target labels in
`mixing_battery.py`. Its B1 console labels now describe window-dependent fitted
log-separation slopes; the withdrawn SM 241 target is removed and an empty window
is reported without inferring slow growth. The actual numerical map, diagnostics,
fit calculation and data are unchanged. The reproducer README scopes the battery
to the rounded candidate. This completes finding (1)'s evidence-surface propagation.

## Rebuilt integration-review candidate

Canonical commands `sh ./build.sh Explainer Juno Main SM Substratum` and
`sh ./build.sh --book` completed with exit status zero and no dropped glyphs.
Page counts remain Explainer 70, Juno 22, Main 96, SM 150, Substratum 55 and book
559. Their median nonspace characters per page are 2446, 2067, 2725, 2514, 2635
and 2557 respectively. Rendered Main 47, Substratum 14, SM 34 and book 413 were
inspected with no layout faults. All 13 source stamps match. Coverage retains
133 statements; audit-census, voice and whitespace checks pass.

The new saturation criterion passed a scaled actual-map perturbed run and rejected
an identical unperturbed twin. After the explicit countercontrol mode was added,
the scaled positive run and the bounded control command both returned their
expected success status: the latter confirms zero separation and failure of the
saturation predicate on every seed. Full default replay is delegated to the new
ordinary CI step, not claimed from the scaled run. The battery's numerical AST is
unchanged modulo console string constants. The onsite K3 block, full ledger and
Lean sources are byte-identical to ce03041c; historical SC28/SC34 README files are
also byte-identical. The three normalized output files preserve every nonblank
scientific result line.

This rebuilt candidate still needs independent exact-candidate acceptance and
fresh ordinary CI. The new workflow step is the only workflow change; its event
modes are unchanged. No merge, publication release, special dispatch, F/E
designation or old-unit closure is authorized.
