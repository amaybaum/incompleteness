# Scalar rule census and multi-field escape

Read REPORT.md for assumptions, exact probabilities, proofs and limitations.
This is an exploratory independent read-only handoff, not an apparatus pass.

Python 3.10+; standard library only:

```sh
sha256sum -c SHA256SUMS
python3 rule_census_checks.py > replay.out
cmp rule_census_checks.out replay.out
python3 -O rule_census_checks.py > optimized.out
cmp rule_census_checks.out optimized.out
```

Independent exhaustive integer enumeration (C++17, standard library only):

```sh
g++ -O2 -std=c++17 exhaustive.cpp -o exhaustive
./exhaustive > exhaustive-replay.out
cmp exhaustive.out exhaustive-replay.out
```

The C++ lines give rule code, four counts in (h1,h3) order 00,01,10,11,
and denominator 2^24. Dividing reproduces the Python fractions.
The checkers themselves have no file writes, randomness or network calls;
the shell commands above create output files and the executable. Python
checks stay enabled under -O. The archive contains no compiled executable.
SHA256SUMS covers every payload except itself and the enclosing ZIP.

No repository edits, commits, comments, pushes or workflow launches were made.
