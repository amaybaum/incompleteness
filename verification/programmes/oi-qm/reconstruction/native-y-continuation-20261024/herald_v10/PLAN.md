# Synchronized remote Y herald and fair-z construction

Base #910: 3f440c59660d7255aa8a727ff8b5de8289004f80. Research only.
Use the unchanged P and local target deadline L=R+9. Test the retained
2,684-step predicate word with symbolic identity padding, not a claim that
P supports a 2,700-layer transport period. All source values must be affine
in five original-time fresh seed bits, with an independent sixth bit z.

Decision rule fixed before computation:
1. Verify the five-bit predicate word on all 32 seeds, the six-step identity
   on every register state, and the exact integer padding schedule at L.
2. Give all original-time source coordinates and affine values by an explicit
   finite indexed formula. Verify the native first-arrival wing recurrence
   on one bounded realization, including its final input, rather than only
   evaluating the abstract register program.
3. Place new remote herald and z receivers away from all old cones and banks.
   Check geometry with the actual parameters and a stated no-wrap torus.
   They must have blank raw prefixes and the intended complete terminal
   triples; no fresh cells may be inserted during the run.
4. Enumerate all 64 new seed assignments, retaining failure, and require
   success count 5:3:2 for (a,b)=00,10,11 and fair z jointly with (a,b).
   A shared-z source and a wrong final phase must be rejected.
5. Publish a conditional synchronized source construction only if the controls
   pass. It does not supply the local three simultaneous carrier outputs,
   prove their native connection, derive calibrated probabilities or source
   independent resources physically. Report any actual synchronization gap.

Cost: one bounded native-wing replay of about 2,700 steps plus small register,
rank, geometry and rational-law checks; no period enumeration or large search.
