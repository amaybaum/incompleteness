# C14 corrections — plan (proposal only; nothing is applied)

**Status: WIP / UNVERIFIED.** This plan and the packages that follow it are proposals.

**Authority.**
- Owner routing: #1169 c.7067233614, for the C1–C4 audit #1520. Round 4: #1169 c.7067281228.
- ch02:88 (with FULL:718) enters #1477's final scientific review. It is excluded here.
- The other confirmed findings of the audit at `022d750e` become separate corrections, to be
  applied after the A1 retirement, each against the refreshed `main`, with its exact
  dependencies kept.
- This branch edits no manuscript, glossary, `FULL.md`, guard or Lean file.

**Inputs.** The audit `../AUDIT.md` at `022d750e`, reviewed CONFIRMED WITH NITS (c.7066874849),
with those nits applied in `022d750e`.

**What a package is.** Each entry in `packages.json` gives:
- the file and the exact old text, unique in that file;
- the proposed new text;
- whether the same edit lands in `FULL.md` (book chapters);
- the canonical source it follows (Main:72–78, or the theorem it cites);
- the dependencies it must preserve;
- whether it is an overclaim narrowing or a wording or label fix.

`PACKAGES.md` presents them in the reviewer's impact order: F3, F5, F7, F2/F2b, F11, F4/F12,
then the rest.

**Rules.**
1. Scientific meaning is unchanged, except where a finding is an overclaim. An overclaim is
   narrowed to what Main proves, never widened.
2. Where the proved scope is itself uncertain (F9, F10), the package keeps the more conditional
   wording and records the open question. It does not decide it.
3. Paper text follows §A.32/§A.33: neutral register, no self-narration.
4. No package edits a line under #1477's frozen ledger. The ledger is read only, at `55544cc3`.

**Productivity test (fixed before writing the packages).** The packages are READY only if every
one of the following holds, as checked by `check_packages.py` at a stated commit:
- (a) every old text occurs exactly once in its file;
- (b) every book-chapter package's old text also occurs exactly once in `FULL.md`;
- (c) no old text lies on a line, or overlaps text, that a #1477 ledger edit changes;
- (d) every package names its canonical source and its dependencies.

Any failure of (a)–(c) at the refreshed post-retirement `main` makes the affected package STALE,
to be re-cut against that `main`.

**Outcome classes.**
- **READY**: (a)–(d) hold at the drafting base.
- **PARTIAL**: some packages fail.
- **INCONCLUSIVE**: the check could not be run, or the proved scope of an overclaim could not be
  fixed from the corpus. F9 and F10 carry an open scope question, but their packages are
  conservative, so they do not by themselves make the outcome INCONCLUSIVE.

**Check, and what it does not cover.**
- *What the checker is.* `check_packages.py` does text checks only: occurrence counts, mirror
  presence, ledger overlap, and a scan for guard pins. That scan reports any guard or census
  source containing a 30-character span of an old text.
- *What it does not run.* The release gate, the guards and the Lean build. They must run after
  application, in CI, on the refreshed `main`.
- *Dependencies it lists but cannot discharge.* The audit-census counts (`verification/audit-census.json`),
  the voice and claims checks, `architecture_check.py`'s forbidden-phrase families, and the
  Lean-manuscript census (§A.35).
