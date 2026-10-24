# Native-Y continuation: current research handoff

24 October 2026. Active research on draft PR #910. No merge, native-round
certification, physical-premise adoption, or manuscript status change.

## Main result

A clean native Y readout has been constructed for the retained native family.
With T=185, P=12*840^185, S=T+P, d=68, R=S+d, prepare the depth-seven outward
cone about q7=(0,S,d+7). Preserve the old sources and add exactly one current
initial source:

    f=(0,S,S+2d+14),  U_0(f)=(u,0,u).

Here u is the existing apparatus seed; the source contains no copy of unknown
x or a later measurement value. The unchanged native rule gives

    U_(R+7)(q7)=(0,0,y),  y=x XOR u.

The full nonlinear two-upper-source calculation, actual giant-delay reduction,
initial source compatibility and final-update cancellation are independently
accepted in [the scoped review](outward_v6/review/REPORT.md). Details are in
[the construction report](outward_v6/CORRECTION-REPORT.md). Its positive result
supersedes the need to use the unsuccessful sidecar junction for this readout;
the earlier negative results remain valid for their own preparations.

## What is and is not transferred

Replacing qY.D at R by arbitrary diagnostic p gives

    (x(1 XOR u)(1 XOR p), (x XOR u)(1 XOR p), p).

Thus D genuinely carries that operand. The other two fields vanish on native
runs p=x XOR u, but not under every arbitrary intervention. A separate
q2.A-only replacement at R+2 still fails to transfer as a reusable input:
x=1,u=0,p2=0 gives111. The construction is a clean native readout of the
original qY wave, not a general late-input adapter or a Y reset.

## Retained findings

| Route | Result | Boundary |
| --- | --- | --- |
| Conditional five-tick extractor | Native A extraction exists | Actual late splice violates readiness |
| Unchanged sidecar junction | Free initial triple permutes the whole endpoint | Cannot be treated as a clean code |
| Six-source prepared sidecar | Exact actual-scale output computed and independently reproduced | Opposite Y supports overlap even at fixed x |
| Straight outward scan | q7=(0,u,y), with raw qY.D transfer | Retains u in B before correction |
| One seed-only boundary correction | q7=(0,0,y) on native runs | Reusable input socket and downstream reset remain open |
| Standalone native direct reset | Checked conditional tagged law and herald | Not embedded into this late phase; strict raw-carrier issue remains for that candidate |

The exact period argument is reusable: a closed strip of budget L has global
identity exponent dividing 12*840^L. The actual P permits the bounded reductions
used here. This is an analytic identity, not a numerical phase extrapolation.

## Resources and record boundary

The q7 receiver remains private until its designated read. Its earlier prefix
at R-7 is `(u,u,1)` and remains informative; the correcting pulse does not
change it. A native shutter or clock is not supplied.

The depth-seven initial ready region and one seed-correlated source are
specified resources. No extra independent fair seed is used by the correction.
Extending the seven old public records through R+7 retains the inherited
147 additional initially independent fair bits beyond R, 105 beyond the
depth-two window. No old frontier variable is pinned or repurposed.

The correction leaves old receiver histories through R+7 unchanged relative
to the uncorrected q7 preparation. Whole-record statements still depend on
the inherited joint-frontier theorem and its access assumptions. The local
construction is not a new full-protocol certification. Existing herald and
failure accounting remain unchanged; no second reset success is asserted.

## Next research task

Connect the actual clean q7 code to a subsequent native measurement/reset,
including its actual previous slice and neighboring fields. A clean endpoint
alone does not imply a cold input neighborhood. Do not reload it into the
standalone direct-reset apparatus or impose readiness at the late time.

Specify all new controls, workspace and any fresh independent seed bank at
the original initial time. Preserve the unknown operand without preloaded
copies. Then check operand interventions, every accessible prefix, and the
complete record/outgoing-carrier law with all failure branches. A post-Y
5:3:2 reset distribution must be produced and checked by that construction;
the new clean code does not itself provide it.

Exact-QM reconstruction and finite-precision OI retain their separate status.
Neither the local failures nor this local construction settles the broader
programme, initialization, access closure, arbitrary depth/menu or composites.

## Replay and checkpoint discipline

Run `python3 replay.py` from this directory; all 21 checker groups have passing
normal and optimized replay evidence. Python 3.12's standard library
and a C++17 compiler (`g++`) suffice. The driver checks retained hashes,
compiles Python, runs every scoped checker normally and with `-O`, and compares
deterministic output. It works in a temporary copy to preserve tracked bytes.

Continue this workstream on `draft/native-y-research-checkpoints-20261024`
with prompt forward checkpoints after meaningful findings, reviews and handoffs.
Preserve reviewed snapshots and state incomplete work explicitly. Keep #885
under its separate writer. No force-push, merge, special workflow dispatch,
branch deletion or F/E designation follows from this research authorization.
