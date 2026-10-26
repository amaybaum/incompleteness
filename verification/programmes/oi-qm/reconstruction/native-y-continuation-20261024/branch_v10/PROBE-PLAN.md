# Finite branching-control audit from the actual q9 census

Source #910 at 3f440c59660d7255aa8a727ff8b5de8289004f80. Research only.

Before a spatial fork, test the smaller control family at the existing
q9 site. Its real native two-slice boundary contains q8=(0,y,0) at R+8
and q9 at R+9. This is not three same-tick ports. The q9 source census
suggests that a nonlinear seed-only J can encode two masked signs there;
no such nonlinear initial resource is adopted.

Decision rules fixed before computation:
1. Read the actual reset_v9 retained q9 tables, verify their checksum and
   native p-independence, and reconstruct all pointwise output pairs by u,J.
2. Exhaust all 8^4 affine three-bit sources J=c XOR u*cu XOR a*ca XOR b*cb.
   Demand common complete raw q9 output at fixed y,a,b over both old u values.
   For each y demand three distinct raw codes on accepted masks00,10,11;
   separately test all four masks. If none pass, exclude exactly this affine
   single-source family. Check that old selector-mask coefficients cannot help
   by testing J-to-output injectivity in every input/history row.
3. Derive the unique J tables, if present, for the explicit output
   q9=(0,y XOR a,y XOR b). Keep them as a required control truth table, not
   a physically realized nonlinear initial prior. Verify its Boolean degree
   and retain an affine one-mask positive control from reset_v9.
4. Check shallow -x/-y/+z spatial source/receiver geometry against the existing
   ready balls and frontier bank. Record any new earlier arrivals that prevent
   reusing the first-front evaluator. Do not silently erase those sources or
   treat native q8 as a cold localized input. No expensive spatial evolution
   starts without a justified coupled-background/period reduction.

A positive two-slice decoder is not observer readout access. A native compiler
for any nonlinear seed control, same-current-slice Y output, calibrated masks,
fair z and joint public/failure law remain independent obligations.
