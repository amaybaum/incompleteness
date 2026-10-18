# Hidden-sector route selection: bounded design check

Research/design record, 2026-10-13. This is not a native round, F designation,
execution receipt, or empirical analysis. Planning base:
`9b5b53eea5cd03b93b22b4812362fb40e2eea234`; manuscript snapshot:
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

## Fixed scope and decision rule

Select the route with the cheapest currently specified derivation gate, not the
route with an assumed signal. Compare all four routes against their missing
physical inputs. A route-selection success must name a derived obstruction or
conditional observable, a null/comparison model, and the next precise derivation.
No observational data, fitted parameter, or significance calculation is used.

Productivity test: an output is useful only if it removes a candidate inference
or exposes an additional required input beyond the roadmap's existing list.
Inventorying the four routes alone does not meet that test.

H-NEQ's first gate is whether the stated premises determine a relaxation law
for a *named projected distribution* and a nonzero visible moment response.
Fine-grained relaxation, projected relaxation, and an outcome response must not
be identified. A chosen scalar relaxation model is a conditional comparison,
not a derivation from the substratum.

## Exact check requirements fixed before the check

The stdlib-only `exact_check.py` must establish all of the following before
printing a design verdict:

1. Permutation pushforward preserves total variation from the uniform prior
   for all sampled rational distributions and all permutations, including a
   nonuniform positive case. A nonbijective map must break the inference.
2. A four-cycle has a recurrent projected deviation, including a return after
   a zero projected deviation. Two distributions with the same current
   projection must have different next projections: no autonomous projected
   update is licensed for this example.
3. The specified reset kernels are stochastic, preserve the reference measure,
   and contract the specified perturbation. The identity kernel and a
   nonstochastic matrix are countercontrols.
4. A symmetric perturbation changes the second moment while the third moment
   remains zero; zero perturbation must recover the reference law.
5. Two rates of order H have different exact exit-scale powers. A chosen
   scale-dependent initial perturbation must cancel the exit-scale trend.
   Continued relaxation to a common end must cancel that trend as well.
6. Deliberately corrupted outputs or premises must be rejected by the relevant
   checks. A script exception or any failed check invalidates its design verdict.

These finite checks exercise examples. The universal statements and their scope
are proved separately in `result.md`; replay is not an independent proof.

## Next-derivation decision

Proceed toward an empirical preregistration only if a specific substratum
update, observer partition, measure reading, and mode readout yield (a) a
projected/conditional propagator, (b) its deviation decay, (c) an observable
response, and (d) a restricted initial-condition family. If any remains free,
record underdetermination and the added premise required. Do not fit an
unrestricted function of wavenumber to the data and call that a test.
