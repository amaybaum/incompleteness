"""Compute the CompositeDimension warning summary from the saved job log.

Usage:
  git show <commit>:<path> | python3 -I analyze.py <raw.log> <raw_tool_response.json> <summary.md> \
      --source-commit <sha> --source-path <path> --source-blob <blob id> --run-meta '<json>'

Every figure in the output is computed here from the saved files (and, for the
source-position control only, from the file content piped on stdin).
"""
import argparse
import hashlib
import json
import re
import sys

ap = argparse.ArgumentParser()
ap.add_argument("log")
ap.add_argument("response")
ap.add_argument("out")
ap.add_argument("--source-commit", required=True)
ap.add_argument("--source-path", required=True)
ap.add_argument("--source-blob", required=True)
ap.add_argument("--run-meta", required=True)
args = ap.parse_args()

# ---------------------------------------------------------------- inputs
with open(args.response, "rb") as fh:
    resp_bytes = fh.read()
resp = json.loads(resp_bytes.decode("utf-8"))
with open(args.log, "rb") as fh:
    log_bytes = fh.read()
text = log_bytes.decode("utf-8")
raw_matches_response = text == resp["logs_content"]

src_bytes = sys.stdin.buffer.read()
src_blob = hashlib.sha1(b"blob %d\0" % len(src_bytes) + src_bytes).hexdigest()
src_lines = src_bytes.decode("utf-8").split("\n")
meta = json.loads(args.run_meta)

lines = text.split("\n")
N = len(lines)
orig = resp["original_length"]

TS = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) ?")


def ts(line):
    m = TS.match(line)
    return m.group(1) if m else None


def content(line):
    m = TS.match(line)
    return line[m.end():] if m else line


all_ts = [ts(l) for l in lines]
n_missing_ts = sum(t is None for t in all_ts)
ts_lengths = {len(t) for t in all_ts if t}
nondecreasing = all(a <= b for a, b in zip(all_ts, all_ts[1:]) if a and b) if len(ts_lengths) == 1 else None
first_ts, last_ts = all_ts[0], all_ts[-1]

PROGRESS = re.compile(r"\[\d+/\d+\]")
HEADER = re.compile(r"^(warning|info|error): ")
BUILD = re.compile(r"\b(Built|Replayed)\s+OIBridge\.CompositeDimension(?![\w.])")

build_hits = [(i, l) for i, l in enumerate(lines, 1) if BUILD.search(l)]
replayed_hits = [(i, l) for i, l in build_hits if "Replayed" in l]
mention = [i for i, l in enumerate(lines, 1) if "CompositeDimension" in l]

# Block opened by the (first) build line: up to the next build-progress line.
block = None
if build_hits:
    b0 = build_hits[0][0]
    nxt = next((i for i in range(b0 + 1, N + 1) if PROGRESS.search(content(lines[i - 1]))), None)
    block_end = (nxt - 1) if nxt else N
    block = (b0, block_end, nxt)

# ---------------------------------------------------------------- warnings
crit = [(i, l) for i, l in enumerate(lines, 1) if "CompositeDimension.lean" in l and "warning" in l]
crit_ci = [(i, l) for i, l in enumerate(lines, 1) if "CompositeDimension.lean" in l and "warning" in l.lower()]
HDR = re.compile(r"^warning: OIBridge/CompositeDimension\.lean:(\d+):(\d+): (.*)$")
hdr = [(i, l) for i, l in enumerate(lines, 1) if HDR.match(content(l))]
gh_ann = [(i, l) for i, l in enumerate(lines, 1) if "##[warning]" in l and "CompositeDimension" in l]
errs = [(i, l) for i, l in enumerate(lines, 1)
        if "CompositeDimension.lean" in l and re.search(r"\berror\b", content(l), re.I)]

LOC = re.compile(r"CompositeDimension\.lean:(\d+):(\d+):")
parsed = []  # (window line, (line, col), message, raw line)
for i, l in crit:
    locs = LOC.findall(l)
    m = HDR.match(content(l))
    parsed.append((i, tuple(int(x) for x in locs[0]) if len(locs) == 1 else None,
                   m.group(3) if m else None, l, len(locs)))

SIMP = "This simp argument is unused"
SEQ = "Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice"
REQ = [((2591, 23), SIMP), ((2591, 52), SIMP), ((2593, 10), SIMP), ((2607, 25), SIMP),
       ((2607, 54), SIMP), ((2608, 70), SIMP), ((2608, 93), SEQ)]
req_set = {loc for loc, _ in REQ}


def msg_check(actual, expected):
    if actual is None:
        return "n/a"
    if actual == expected:
        return "yes (exact)"
    if actual.rstrip(":") == expected:
        return "yes (log adds a trailing ':')"
    if actual.startswith(expected):
        return "yes (expected text is a prefix)"
    return "NO: reads " + repr(actual)


def block_lines(start):
    """Header line plus continuation lines up to the next diagnostic header or progress line."""
    out = [start]
    for j in range(start + 1, N + 1):
        c = content(lines[j - 1])
        if HEADER.match(c) or PROGRESS.search(c):
            break
        out.append(j)
    return out


def named_in_log(i, msg):
    if msg is None:
        return None
    if msg.startswith(SIMP):
        return content(lines[i]).strip() if i < N else None  # next line holds the argument
    m = re.match(r"Variable name `([^`]+)` is not explicitly referenced", msg)
    if m:
        return m.group(1)
    if msg.startswith("Used `tac1 <;> tac2`"):
        return "<;>"
    return None


def token_at(line_no, col):
    if not (1 <= line_no <= len(src_lines)):
        return None
    m = re.match(r"[^\s,\[\]()]+", src_lines[line_no - 1][col:])
    return m.group(0) if m else ""


DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
                  r"(theorem|lemma|def|abbrev|instance|structure|class|inductive|example)\s+(\S+)")


def enclosing_decl(line_no):
    start = next((k for k in range(line_no, 0, -1) if DECL.match(src_lines[k - 1])), None)
    if start is None:
        return None
    nxt = next((k for k in range(line_no + 1, len(src_lines) + 1) if DECL.match(src_lines[k - 1])), None)
    return DECL.match(src_lines[start - 1]).group(2), start, nxt


# ---------------------------------------------------------------- render
o = []
w = o.append
w("# Mathlib bridge job log: CompositeDimension.lean warnings")
w("")
w(f"Run `37299337191`, job \"Mathlib bridge\" id `{resp['job_id']}`. Every figure below is computed by "
  "`rcs/dim1log_scripts/analyze.py` from the saved files in this directory; nothing was read off by eye.")
w("")
w("## Provenance")
w("")
w("- Tool call: `mcp__github__get_job_logs(owner=amaybaum, repo=incompleteness, "
  f"job_id={resp['job_id']}, return_content=true, tail_lines=5000)`.")
w(f"- Response fields: `job_id={resp['job_id']}`, `message={resp['message']!r}`, "
  f"`original_length={orig}`, `logs_content` = {len(resp['logs_content']):,} characters.")
w(f"- `raw_tool_response.json`: {len(resp_bytes):,} bytes, sha256 `{hashlib.sha256(resp_bytes).hexdigest()}`.")
w(f"- `raw.log`: {len(log_bytes):,} bytes, sha256 `{hashlib.sha256(log_bytes).hexdigest()}`; "
  f"identical to the response's `logs_content`: {'yes' if raw_matches_response else 'NO'}.")
w(f"- Run metadata (GitHub API, not from the log): event `{meta.get('event')}`, head_sha "
  f"`{meta.get('head_sha')}`, branch `{meta.get('head_branch')}`, run_attempt {meta.get('run_attempt')}, "
  f"conclusion `{meta.get('conclusion')}`; job conclusion `{meta.get('job_conclusion')}`.")
w("")
w("## 1. Coverage")
w("")
w(f"- Reported original length (`original_length`): **{orig}**. It is not a character count: the "
  f"returned window alone is {len(text):,} characters. Read as the full log's line count, the window "
  f"is lines {orig - N + 1}–{orig} of {orig}.")
w(f"- Lines returned: **{N}** (split on `\\n`; text ends with a newline: "
  f"{'yes' if text.endswith(chr(10)) else 'no'}; `\\r` characters: {text.count(chr(13))}; "
  f"`splitlines()` count: {len(text.splitlines())}).")
w(f"- Lines without a leading timestamp: {n_missing_ts}. Timestamps non-decreasing through the window: "
  f"{'yes' if nondecreasing else ('no' if nondecreasing is False else 'not checked (mixed formats)')}.")
w(f"- First timestamp (window line 1): `{first_ts}`")
w(f"- Last timestamp (window line {N}): `{last_ts}`")
if build_hits:
    w(f"- **The build line for `OIBridge.CompositeDimension` is inside the window**: "
      f"{len(build_hits)} line(s) matching `Built|Replayed OIBridge.CompositeDimension`; "
      f"`Replayed` lines: {len(replayed_hits)}.")
    for i, l in build_hits:
        w(f"  - window line {i} (full-log line {orig - N + i} on the line-count reading):")
        w("")
        w("    ```text")
        w("    " + l)
        w("    ```")
        w("")
    b0, b1, nxt = block
    w(f"- The block that line opens runs over window lines {b0}–{b1}. It ends where the next "
      f"build-progress line begins, window line {nxt}:")
    w("")
    w("  ```text")
    w("  " + (lines[nxt - 1] if nxt else "(none)"))
    w("  ```")
    w("")
    inside = all(b0 <= i <= b1 for i in mention)
    w(f"- Window lines mentioning `CompositeDimension` anywhere: {len(mention)}, spanning window lines "
      f"{mention[0]}–{mention[-1]}; all inside the block: {'yes' if inside else 'NO'}. "
      f"No CompositeDimension line occurs before the build line or after the block.")
else:
    w("- **The build line for `OIBridge.CompositeDimension` is NOT inside the window.**")
w("")
w("## 2. Lines containing both `CompositeDimension.lean` and `warning` (verbatim, in order)")
w("")
w(f"Count: **{len(crit)}**")
w("")
w("```text")
for i, l in crit:
    w(l)
w("```")
w("")
w("Window line numbers, in the same order: " + ", ".join(str(i) for i, _ in crit) + ".")
w("")
same_hdr = [i for i, _ in crit] == [i for i, _ in hdr]
same_ci = [i for i, _ in crit] == [i for i, _ in crit_ci]
one_loc = all(k == 1 for *_, k in parsed)
w(f"Cross-checks: the same {len(hdr)} lines match the Lean header pattern "
  f"`warning: OIBridge/CompositeDimension.lean:<line>:<col>: …` ({'identical set' if same_hdr else 'SETS DIFFER'}); "
  f"case-insensitive `warning` gives {len(crit_ci)} ({'identical set' if same_ci else 'SETS DIFFER'}); "
  f"each line carries exactly one location: {'yes' if one_loc else 'NO'}; "
  f"`##[warning]` annotations mentioning CompositeDimension: {len(gh_ann)}; "
  f"`error` lines for `CompositeDimension.lean`: {len(errs)}.")
w("")
w("### The seven requested locations")
w("")
w("| location | present | window line | message as expected |")
w("|---|---|---|---|")
req_rows = []
for loc, exp in REQ:
    hits = [p for p in parsed if p[1] == loc]
    if hits:
        for p in hits:
            req_rows.append((loc, p))
            w(f"| `{loc[0]}:{loc[1]}` | yes | {p[0]} | {msg_check(p[2], exp)} |")
    else:
        req_rows.append((loc, None))
        w(f"| `{loc[0]}:{loc[1]}` | **no** | – | – |")
w("")
w("The seven lines, verbatim, in the table's order:")
w("")
w("```text")
for loc, p in req_rows:
    w(p[3] if p else f"(no line for CompositeDimension.lean:{loc[0]}:{loc[1]})")
w("```")
w("")
others = [p for p in parsed if p[1] not in req_set]
w(f"### Other `CompositeDimension.lean` warning locations present ({len(others)})")
w("")
w("| location | window line | message |")
w("|---|---|---|")
for p in others:
    w(f"| `{p[1][0]}:{p[1][1]}` | {p[0]} | {p[2]} |")
w("")
w("## 3. Total")
w("")
n_req = sum(1 for _, p in req_rows if p)
w(f"**{len(crit)}** warning lines for `CompositeDimension.lean` in the window: {n_req} at the requested "
  f"locations and {len(others)} elsewhere. Distinct locations: {len({p[1] for p in parsed})}.")
w("")
w("## Appendix A. Full message blocks of the seven requested warnings (verbatim)")
w("")
w("Each block is the header line and its continuation lines, up to the next diagnostic header or build-progress line.")
w("")
for loc, p in req_rows:
    if not p:
        continue
    blk = block_lines(p[0])
    w(f"`{loc[0]}:{loc[1]}` (window lines {blk[0]}–{blk[-1]}):")
    w("")
    w("```text")
    for j in blk:
        w(lines[j - 1])
    w("```")
    w("")
w("## Appendix B. Source-position control")
w("")
w(f"Source: `git show {args.source_commit}:{args.source_path}`. Its git blob id, recomputed here from the "
  f"bytes piped in, is `{src_blob}`, against `{args.source_blob}` from `git rev-parse`: "
  f"{'match' if src_blob == args.source_blob else 'MISMATCH'}. The file has {len(src_lines)} newline-separated "
  "segments. For each warning, the table gives the token that begins at the reported line and "
  "(0-based, codepoint) column, next to the name the log message gives.")
w("")
w("| location | token at position in source | named in log | match |")
w("|---|---|---|---|")
n_match = 0
for p in parsed:
    (ln, col) = p[1]
    tok = token_at(ln, col)
    nm = named_in_log(p[0], p[2])
    ok = tok is not None and nm is not None and tok == nm
    n_match += ok
    w(f"| `{ln}:{col}` | `{tok}` | `{nm}` | {'yes' if ok else 'NO'} |")
w("")
w(f"Matches: {n_match}/{len(parsed)}.")
w("")


def byte_col_token(line_no, col):
    """Token if the column were read as a UTF-8 byte offset instead of a codepoint offset."""
    b = src_lines[line_no - 1].encode("utf-8")[col:]
    m = re.match(r"[^\s,\[\]()]+", b.decode("utf-8", errors="replace"))
    return m.group(0) if m else ""


shift_ok = sum(token_at(p[1][0], p[1][1] + 1) == named_in_log(p[0], p[2]) for p in parsed)
byte_fail = [p for p in parsed if byte_col_token(p[1][0], p[1][1]) != named_in_log(p[0], p[2])]
mb_before = {f"{p[1][0]}:{p[1][1]}": sorted({ch for ch in src_lines[p[1][0] - 1][:p[1][1]] if ord(ch) > 127})
             for p in byte_fail}
w(f"Countercontrol (the comparison discriminates): with every column shifted by +1, matches fall to "
  f"{shift_ok}/{len(parsed)}; reading the columns as UTF-8 byte offsets instead of codepoints gives "
  f"{len(parsed) - len(byte_fail)}/{len(parsed)}, failing at "
  + (", ".join(f"`{k}` (non-ASCII before the column: {' '.join(v)})" for k, v in mb_before.items()) or "none")
  + ".")
w("")
for ln in sorted({loc[0] for loc, _ in REQ}):
    d = enclosing_decl(ln)
    if d:
        top = [k for k in range(d[1] + 1, ln + 1) if src_lines[k - 1] and not src_lines[k - 1][0].isspace()]
        w(f"- Source line {ln}: inside `{d[0]}` (declaration at line {d[1]}; next declaration at line {d[2]}; "
          f"non-indented lines between line {d[1]} and line {ln}: {len(top)}).")
    else:
        w(f"- Source line {ln}: no enclosing declaration found.")
w("")

with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(o))

print("\n".join(o))
