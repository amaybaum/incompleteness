# Executable finite-menu A2 envelope certificate

24 October 2026. Research source is #911 at
`f2426f16d0054943ca4937648a9ff9613d08f960`, finite-a2-v5 revised author
`dbfaa3c68003bfd5335353829c18cf6f21d300c4`. This new branch narrows the
universal-menu constants to a declared finite menu and total horizon. It
keeps the prior geometric carrier, rather than tabulating protocol answers.
No native availability, probability-selection or OI-equivalence claim follows.

## Decision rule fixed before computation

Construct the same six-face rational geometric grid and initially fair CDF
sampler as finite-a2-v5, but certify its actual finite preparation/reset rays
and all possible rotation words through h=3 directly with exact arithmetic.
The preparation menu contains both signs of X,Y,Z,a=(3/5,4/5,0), plus the
pure poles (2/3,-2/3,+/-1/3) and antipodes. Arbitrary positive mixtures of
these preparation procedures are admissible; physical mixture randomness is
a separate initial resource. Reset directions are the measured eigenstates.
Measurement axes are X,Y,Z,a. Rotation generators are H,S,R,r from the
prior report, with R a rational Z rotation with first row (3/5,-4/5,0),
and r its inverse. Every operation advances one total clock; resets clear
the current word but never restart the horizon or bit bank.

For each geometry/sampler parameter, compute a single fixed rational alpha
and decoder r=alpha E[R_word ell_i], using the same inward rational ell_i
as before. Start with alpha=3/2. If any admissible ray has decoded norm>1,
replace alpha by a rational inward value justified from a certified upper
bound on the maximum ray moment norm, before checking protocol errors.
The decoder remains identical at input/output and independent of protocols.

For every preparation/reset direction n and rotation word of length<=h,
certify positivity and a uniform upper bound chi on
||alpha R_word mean(n)-R_word n||/2. For every read axis and every
preparation/reset n and word of length<=h-1, compute exact sign probability
and its error against (1+a dot R_word n)/2; let kappa be their maximum.
Convexity then extends these finite envelope certificates to the entire
admissible mixture cone and all adaptive policies within this menu/horizon.
The complete record/outgoing-state CQ bound is min(1,h*kappa+2chi), using
initial-decoding contraction and the prior record-coupling/reset argument.
The physical controller never reads the old preparation instruction after
preparation. Enumeration is a verifier, not a table of protocol answers.

Attempt M=8,16,32,64 in ascending order, W=16 and B=24 (M even). Stop once
a fully executed geometric law has h*kappa+2chi<=1/10, or after M=64.
Do not claim success from an unexecuted alphabet or a bound clipped at one.
If no threshold is reached, retain the measured rigorous tradeoff and
identify which term blocks it. All finite ray/word/read combinations count;
no favorable protocol subset may replace this envelope.

## Independent controls and evidence

- Reconstruct rational sphere geometry, nonnegative CDF counts, complete
  normalization, antipodal mirror, and fixed decoder positivity.
- Bound square roots by rational intervals; report exact rational upper
  endpoints and squared-norm certificates, not floating certification.
- Verify finite word matrices with rational complex quantum unitaries;
  enumerate independent adaptive projector trees, including zero branches,
  stopping padding, public ticks and all flags, against the source controller.
- Retain prior controls for reused reset seed, wrong adaptive setting,
  insufficient bank and exposure of private carrier/seed/timing data.
  A detector is valid only if an actual nonzero witness is produced.
- Explain finite-menu/horizon scope and do not substitute it for the prior
  uniform all-menu theorem or practical/native implementation.

Curated files: PLAN.md, REPORT.md, checks.py, result.json, PROVENANCE.json,
SHA256SUMS. Root publishes the plan before execution and later publishes
source/evidence for separate review. Normal and optimized runs must produce
identical structured output. No dispatch, F/E designation, merge, #885 write,
private logs or broad full-suite campaign is included.
