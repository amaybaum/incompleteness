# DESIGN-v5.5.1: changes against DESIGN-v5.5

## Inputs

I verified both inputs by sha256 before use:

- `DESIGN-v5.5.md`: 74db584a5bdb861519f9703e3b5d102ba07a60dfd0e8f89ea183bd89a80b52a4.
- `review-v5.5/review-v5.5.md`: 8c77254a7291e75fe8caff01185e3f9896ace2a18a881497241fc4c51cc5f9ac.
  Its verdict is ACCEPT WITH REQUIRED CORRECTIONS.

## Scope

Exactly F2, F1 and N1, and nothing else. N2, N3, N4, the review's optional points and every pending
owner decision are not applied.

The work was paper-only: nothing was written to the repository, git or GitHub, no workflow ran, and
no host was called. One new script, `work-v551/f1.py`, reuses `work-v55/parity55.py` and P's
verified blob.

## 1. Mapping

| Item | DESIGN-v5.5.1 sections | What changed | How verified |
|---|---|---|---|
| F2 (blocking): delegated evidence for replay | 6.3 ("The admission snapshot"); 5 ("Offline replay"); TR45 | See "F2" below the table | Textual. The replay rule now names, for every class, the inputs it uses, and each of them is in the snapshot's new field list |
| F1: control S11-58k completed | 10.4, row S11-58k | Edit 2 is now fully specified: `{old: "qc", new: "Q", old_step2: "yc", new_step2: "Q"}` at `H` = `"ab qc"`. Expected: ERROR naming edit 2 as chained, while P applies the list with result `"xQ"` | `work-v551/f1.py` (see below). P's own application gives `{'f': 'xQ'}`, and the v5.5 rule, with edit 1's splice supplied, refuses as `chained`. This reproduces the reviewer's verified example |
| N1: chained-edit wording | 6.1, item (iii) | The definition now also covers an occurrence that "spans the point where an earlier edit's image, possibly empty (a deletion), was inserted", that is, one that crosses more than one segment. The rule is unchanged | Wording only; the binding rule already refuses an occurrence that crosses segments |

**F2.** The admission snapshot now carries the delegated evidence. This applies for every
delegated and native class, at `X` and, where `C` differs from `X`, at `C`. It comprises:

- the host run, job and artifact records the tool read, kept as returned;
- the sha256 of every artifact and result file the class used;
- the full outputs of every checker the tool ran natively, with the checker blob, command, working
  directory and exit status;
- the class's own re-derivations.

Replay of an op-C result decides every class from this evidence and the git objects alone. It
makes no host call, no clone, no PDF build and no checker run. It re-applies the rules of sec. 7.2
and 7.3, checks every recorded file against its recorded hash, and must equal the committed result
byte for byte apart from the admission field. TR45 now covers an op-B result and an op-C result. It
also refuses a snapshot whose evidence is missing or whose hashes do not match.

## 2. Nothing else changed

`diff DESIGN-v5.5.md DESIGN-v5.5.1.md` has 7 hunks, and the document grows from 2929 to 2963 lines.
The hunks are:

- the title;
- one status bullet naming this revision and its inputs;
- the N1 wording;
- the snapshot field list (F2);
- the replay bullet (F2);
- TR45 (F2);
- S11-58k (F1).

## 3. What I could not follow or verify

- No implementation exists, so F2's replay is specified, not run.
- Whether every native checker's output is small enough to commit was not measured. The SC-42
  output, the census JSON and preserve_check's result files are expected to be small, but the
  sizes were not checked.
- No comment ids are held for any owner decision.
