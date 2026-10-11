# HO-47 — stopped-channel protocol and cone controls
Version 1. From round7-channel to bridge, countermodels, origin and equivalence.

## Statements and evidence levels

[X]: the saved Gaussian-rational circuit checker passes 17 groups, including the stopped
protocol at depths 0,...,6 on 140 matrix-unit cases, 112 Pauli dictionary cases, 16 mixer
cases and five discriminating countercontrols. Its stdout replays byte for byte.

[W]: the branch recurrence Phi_0=id, Phi_(k+1)=(5/8)Ad(D)+Phi_k composed with ((3/8)id)
gives Phi_k=(1-(3/8)^k)Ad(D)+(3/8)^k id for every k>=0. This is a written induction,
not a general-k Lean InstAvail witness. Exact availability of D is not inferred.

CONDITIONAL [W]: a closed cone preserved by every transferred Phi_k is preserved by the
limit Ad(D). For a convex cone preserved by Ad(D), the displayed convex mixtures Phi_k
also preserve it. These are the two written directions; no kernel-certified equivalence
is claimed. The broader clause for every available channel still needs an independent source.

[X]+[W], scoped controls:
- OCT: a closed product-containing cone preserved by all 24 proper signed-permutation
  target actions is moved by Phi_1 (failing test -1/4). This is the stated finite-action
  comparison, not a classification of arbitrary dilation-generated reversible operations.
- OPEN: the nonclosed cone over the open disc plus one boundary ray is preserved by the
  sequence Phi_k but not by its limit. This does not assert preservation under every
  available channel.
- KAPPA: the expanded block cone at kappa=3/2 has H1, H2 and target CPTP-channel
  invariance [W]; two exact members pair to -5/4, and a product-vector PSD test is -1/2.
  It fails maxCone product-effect positivity and is not a full OI countermodel.
  A maxCone-based replacement of H3, given cone structure, H2 and A_miss, remains a
  separate proof question.

## Evidence and provenance

Committed source e7d380fcb9881e3063243aaa149e85be3cd0a914, research/round7-channel/:
- channel_check.py SHA256 9937b6ffca6cf570cf7e1c3267ba1525ead48ada4d5f1e92959ec0f603baebff.
- channel_check.run1.out and replay.out SHA256 ec73839a23e1c2e051140ff9b56d47bbda4f9b55e37963ca1256500b36642da5.
- ARGUMENT.md SHA256 04f251a9f5ead08f834745debc063fdfd367aff59f0b35b2ce46e1186235ece6.
- PREREGISTRATION.md, LOG.md and MANIFEST.sha256 fix scope and record provenance.

This issues the deferred controls of HP-round6-transfer-2, adding the scoped evidence.
The original proposal at 694219a4 remains unchanged; SHA256
b07610bee5b2eb8664771d35970d2cf6bc54bf5b61da203f71728d181519ca3e.

## Receiving-thread limits

After a v1 inbox receipt and logged use, threads may rely on these exact finite
identities, witnesses and separately labelled written arguments.
They may not assume a formal availability witness, exact availability of a channel
limit, a source of Tch or H3, a full-model counterexample, or main certification.
