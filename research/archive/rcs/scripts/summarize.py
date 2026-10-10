"""Summarize the saved GitHub Actions job log (job 113148584104, "Mathlib bridge").

Usage: python3 -I summarize.py <data_dir> <repo_dir>

Every count and every quoted line in the output is computed from <data_dir>/raw.log.
Decision rules (fixed before reading results):
  (a) a line "mentions RelcSelect" iff it contains the case-sensitive substring "RelcSelect".
  (b) a Lean error line is one whose post-timestamp body starts with "error:";
      a ##[error] line contains "##[error]"; a failed-build marker line contains U+2716 (✖).
  (c) a sorry line contains "sorryAx" or "declaration uses 'sorry'".
  (d) the gate table is the run of lines strictly between the two "====" rules that follow
      the "##[group]Run python3 tools/release_gate.py" header; a row is PASS/FAIL by its
      leading status word.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

data_dir, repo_dir = sys.argv[1], sys.argv[2]
LOG = os.path.join(data_dir, "raw.log")
RESP = os.path.join(data_dir, "raw_tool_response.json")
JOB = os.path.join(data_dir, "job_api.json")
OUT = os.path.join(data_dir, "log_summary.md")

HEAD = "1003b029b4949516e615cea8fbf0531c0ced583b"
BASE = "e2426ba4109dcd719d518aefbd3c417b7c6fdc5b"


def sha256(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


text = open(LOG, encoding="utf-8", newline="").read()
resp = json.load(open(RESP, encoding="utf-8"))
job = json.load(open(JOB, encoding="utf-8"))

lines = text.split("\n")
N = len(lines)
TS = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z) ?")


def split_ts(line):
    m = TS.match(line)
    return (m.group(1), line[m.end():]) if m else (None, line)


stamps = [split_ts(l)[0] for l in lines]
bodies = [split_ts(l)[1] for l in lines]
untimed = sum(1 for s in stamps if s is None)
timed = [s for s in stamps if s is not None]


def vis(s):
    """Render control characters visibly (ANSI ESC as \\x1b); everything else verbatim."""
    return "".join(("\\x%02x" % ord(c)) if ord(c) < 32 else c for c in s)


def fence(block_lines):
    longest = max([len(m) for l in block_lines for m in re.findall(r"`+", l)] + [0])
    return "`" * max(3, longest + 1)


def block(idxs):
    rendered = ["%5d | %s" % (i + 1, vis(lines[i])) for i in idxs]
    f = fence(rendered)
    return "\n".join([f + "text"] + rendered + [f])


def find(pred):
    return [i for i in range(N) if pred(i)]


def listing(idxs, cap=30):
    if not idxs:
        return "(none)"
    shown = idxs[:cap]
    out = block(shown)
    if len(idxs) > cap:
        out += "\n(%d further lines not listed)" % (len(idxs) - cap)
    return out


# ---- integrity -------------------------------------------------------------------------
identical = resp.get("logs_content") == text

# ---- read-only git context ---------------------------------------------------------------
def git(*args):
    r = subprocess.run(["git", "-C", repo_dir, *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else "(git error: %s)" % r.stderr.strip()


parents = git("rev-list", "--parents", "-n", "1", HEAD)
name_status = git("diff", "--name-status", BASE, HEAD)
gate_src = git("show", HEAD + ":tools/release_gate.py")
gate_fmt = [l.strip() for l in gate_src.splitlines() if "tail[:" in l]
lean_in_diff = [l for l in name_status.splitlines() if l.endswith(".lean")]

# ---- 0. coverage -----------------------------------------------------------------------
PROG = re.compile(r"\[(\d+)/(\d+)\]")
prog_idx = find(lambda i: PROG.search(bodies[i]) is not None)
prog_glyph = Counter(bodies[i][:1] for i in prog_idx)
prog_verb = Counter(
    (re.search(r"\]\s+(\S+)", bodies[i]).group(1) if re.search(r"\]\s+(\S+)", bodies[i]) else "?")
    for i in prog_idx
)
built_any = find(lambda i: re.search(r"\]\s+Built\b", bodies[i]) is not None)
lake_final = find(lambda i: re.match(r"^Build completed successfully \(\d+ jobs\)\.$", bodies[i]) is not None)
lake_failed = find(lambda i: re.search(r"Build failed|build failed", bodies[i]) is not None)
timing = find(lambda i: bodies[i].startswith("TIMING "))

# ---- step boundaries (from the log) ------------------------------------------------------
gate_hdr = find(lambda i: bodies[i] == "##[group]Run python3 tools/release_gate.py")
assert len(gate_hdr) == 1, gate_hdr
g0 = gate_hdr[0]
endgroup = next(i for i in range(g0, N) if bodies[i] == "##[endgroup]")
title = next(i for i in range(endgroup + 1, N) if bodies[i] == "release gate")
rules = [i for i in range(title, N) if bodies[i].startswith("====")][:2]
r1, r2 = rules
table = list(range(r1 + 1, r2))
verdict = [i for i in range(r2 + 1, N) if bodies[i].startswith("release gate:")]
assert len(verdict) == 1, verdict
v = verdict[0]
cleanup = [i for i in range(v + 1, N) if bodies[i] == "Post job cleanup."]

ROW = re.compile(r"^  (PASS|FAIL)  (\S+)")
rows = []
for i in table:
    m = ROW.match(bodies[i])
    if m:
        status, name = m.group(1), m.group(2)
        rest = bodies[i][len("  PASS  "):]
        detail = rest[max(16, len(name)) + 1:]
        rows.append((i, status, name, detail))
non_row = [i for i in table if not ROW.match(bodies[i])]
n_pass = sum(1 for r in rows if r[1] == "PASS")
n_fail = sum(1 for r in rows if r[1] == "FAIL")
at60 = sum(1 for r in rows if len(r[3]) == 60)
over60 = sum(1 for r in rows if len(r[3]) > 60)
byname = {r[2]: r for r in rows}

WANT = ["lean-axioms", "lean-manuscript", "v3-receipts", "legacy-records", "artifact-placement", "manifest-drift"]


def num(name, pat):
    r = byname.get(name)
    if not r:
        return None
    m = re.search(pat, r[3])
    return m.groups() if m else None


axioms_n = num("lean-axioms", r"(\d+) named result\(s\) reported")
receipts_n = num("v3-receipts", r"RECEIPTS\s+(\d+) receipt\(s\)")
legacy_n = num("legacy-records", r"LEGACY\s+(\d+) record\(s\) in (\d+) closed namespace\(s\)")

# ---- (a) (b) (c) -----------------------------------------------------------------------
a_hits = find(lambda i: "RelcSelect" in lines[i])
a_ci = find(lambda i: "relcselect" in lines[i].lower())
a_relc = find(lambda i: "relc" in lines[i].lower())

b_lean = find(lambda i: bodies[i].startswith("error:"))
b_colon = find(lambda i: "error:" in lines[i])
b_gh = find(lambda i: "##[error]" in lines[i])
b_x = find(lambda i: "✖" in lines[i])
b_x_occ = text.count("✖")
b_word = find(lambda i: re.search(r"error", lines[i], re.I) is not None)
b_failed_word = find(lambda i: re.search(r"\bfail(ed|ure)?\b", bodies[i], re.I) is not None and i not in table)

c_ax = find(lambda i: "sorryAx" in lines[i])
c_decl = find(lambda i: "declaration uses 'sorry'" in lines[i])
c_ci = find(lambda i: "sorry" in lines[i].lower())
AX = re.compile(r"depends on axioms: \[([^\]]*)\]")
ax_lines = find(lambda i: AX.search(bodies[i]) is not None)
ax_sets = Counter(AX.search(bodies[i]).group(1) for i in ax_lines)
no_ax = find(lambda i: "does not depend on any axioms" in bodies[i])

n_warn = sum(1 for b in bodies if b.startswith("warning:"))
n_info = sum(1 for b in bodies if b.startswith("info:"))
gh_warn = find(lambda i: "##[warning]" in lines[i])

build_lines = list(range(0, g0))
build_first, build_last = stamps[0], stamps[g0 - 1]
first_prog = prog_idx[0]
DIAG = re.compile(r"^(warning|info|error): (OIBridge[^\s:]*\.lean):\d+:\d+:")
pre_files = Counter(DIAG.match(bodies[i]).group(2) for i in range(first_prog) if DIAG.match(bodies[i]))
pre_diag = sum(pre_files.values())

# ---- write -----------------------------------------------------------------------------
o = []
w = o.append
w("# Job log summary: job 113148584104 (\"Mathlib bridge\"), run 37727395526")
w("")
w("Source: `mcp__github__get_job_logs` with owner `amaybaum`, repo `incompleteness`, "
  "job_id `113148584104`, return_content `true`, tail_lines `5000`. "
  "Every count and quoted line below was computed by Python (`scripts/summarize.py`, run with "
  "`python3 -I`) over `raw.log`; line numbers are 1-based positions in `raw.log`.")
w("")
w("## Provenance")
w("")
w("| file | sha256 |")
w("|---|---|")
for fn in ("raw.log", "raw_tool_response.json", "job_api.json"):
    w("| `%s` | `%s` |" % (fn, sha256(os.path.join(data_dir, fn))))
w("")
w("- `raw.log` is byte-identical to the decoded `logs_content` field of `raw_tool_response.json`: **%s**." % identical)
w("- Tool message: `%s`." % resp.get("message"))
w("- Job API (`job_api.json`): name `%s`, run_id `%s`, head_sha `%s`, head_branch `%s`, "
  "run_attempt `%s`, status `%s`, conclusion `%s`, started `%s`, completed `%s`."
  % (job.get("name"), job.get("run_id"), job.get("head_sha"), job.get("head_branch"),
     job.get("run_attempt"), job.get("status"), job.get("conclusion"),
     job.get("started_at"), job.get("completed_at")))
w("- Job API steps (number | name | conclusion | started -> completed):")
for s in job.get("steps", []):
    w("  - %s | %s | %s | %s -> %s" % (s.get("number"), s.get("name"), s.get("conclusion"),
                                       s.get("started_at"), s.get("completed_at")))
w("- Read-only git context: `git rev-list --parents -n 1 %s` -> `%s`; "
  "`git diff --name-status %s %s` -> %s; `.lean` paths in that diff: %d."
  % (HEAD[:8], parents, BASE[:8], HEAD[:8],
     "; ".join("`%s`" % l for l in name_status.splitlines()) or "(empty)", len(lean_in_diff)))
w("")
w("## 0. Coverage")
w("")
w("- Reported original length (`original_length` field of the tool response): **%s**." % resp.get("original_length"))
w("- Lines returned: **%d** (%d newline characters, no trailing newline; %d characters). "
  "Lines without a timestamp prefix: %d." % (N, text.count("\n"), len(text), untimed))
ol = resp.get("original_length")
if isinstance(ol, int) and ol >= N:
    w("- Read as a line count (the unit of `tail_lines`), the window is original lines %d-%d; "
      "the first %d lines of the job log are not in it." % (ol - N + 1, ol, ol - N))
w("- First timestamp (line 1): `%s`. Last timestamp (line %d): `%s`. Min/max over all lines: `%s` / `%s`."
  % (stamps[0], N, stamps[-1], min(timed), max(timed)))
w("- Step layout inside the window: lines 1-%d are the tail of the **Build** step's output "
  "(timestamps `%s` to `%s`; the job API puts Build at %s -> %s); lines %d-%d are the **Release gate** "
  "step; lines %d-%d are post-job cleanup."
  % (g0, build_first, build_last,
     next(s.get("started_at") for s in job["steps"] if s.get("name") == "Build"),
     next(s.get("completed_at") for s in job["steps"] if s.get("name") == "Build"),
     g0 + 1, v + 1, (cleanup[0] + 1) if cleanup else v + 2, N))
w("- The window opens inside one module's messages: lines 1-%d (before the first progress line) "
  "carry %d Lean diagnostics citing %s, plus their continuation and blank lines; that module's own "
  "`[k/n]` line precedes the window, so whether it was built or replayed is not visible here."
  % (first_prog, pre_diag, ", ".join("`%s` (%d)" % kv for kv in pre_files.most_common())))
w("- Build-progress lines `[k/n]` in the window: **%d** (status glyphs: %s; verbs: %s; "
  "lines with `] Built`: %d):"
  % (len(prog_idx), ", ".join("`%s` %d" % kv for kv in sorted(prog_glyph.items())),
     ", ".join("`%s` %d" % kv for kv in sorted(prog_verb.items())), len(built_any)))
w("")
w(block(prog_idx))
w("")
w("- Final lake line (%d match; lines matching `Build failed`/`build failed`: %d):" % (len(lake_final), len(lake_failed)))
w("")
w(block(lake_final + timing))
w("")
w("  (the two `TIMING` lines that follow it are included for context.)")
w("")
w("## (a) `RelcSelect`")
w("")
w("- Lines containing `RelcSelect` (case-sensitive): **%d**." % len(a_hits))
if a_hits:
    w("")
    w(listing(a_hits))
    w("")
w("- Supplementary: lines containing `relcselect` case-insensitively: %d; containing `relc` "
  "case-insensitively: %d. (The window holds no checkout output; the branch name "
  "`claude/relc-select-1` above comes from the job API.)" % (len(a_ci), len(a_relc)))
w("")
w("## (b) Errors and failure markers")
w("")
w("- Lean `error:` lines (post-timestamp body starts with `error:`): **%d**." % len(b_lean))
w("- `##[error]` lines: **%d**." % len(b_gh))
w("- Failed-build marker lines (contain `✖`, U+2716): **%d** (total occurrences: %d)." % (len(b_x), b_x_occ))
w("- Supplementary: lines containing `error:` anywhere: %d; lines containing `error` "
  "case-insensitively anywhere: %d; non-table lines with the word `fail`/`failed`/`failure`: %d."
  % (len(b_colon), len(b_word), len(b_failed_word)))
if b_word:
    w(listing(b_word))
if b_failed_word:
    w(listing(b_failed_word))
w("- Context: Lean `warning:` lines %d; Lean `info:` lines %d; `##[warning]` lines %d:"
  % (n_warn, n_info, len(gh_warn)))
w("")
w(block(gh_warn))
w("")
w("## (c) `sorry`")
w("")
w("- Lines containing `sorryAx`: **%d**." % len(c_ax))
w("- Lines containing `declaration uses 'sorry'`: **%d**." % len(c_decl))
w("- Supplementary: lines containing `sorry` case-insensitively: %d; `depends on axioms: [...]` "
  "lines: %d; `does not depend on any axioms` lines: %d. Distinct axiom lists in the window:"
  % (len(c_ci), len(ax_lines), len(no_ax)))
for k, c in ax_sets.most_common():
    w("  - `[%s]`: %d" % (k, c))
if c_ci:
    w(listing(c_ci))
w("")
w("## (d) Release gate")
w("")
w("Step header (the runner's group for the step, then the gate's own title and rule):")
w("")
w(block(list(range(g0, endgroup + 1)) + [title, r1]))
w("")
w("Per-step table, every row verbatim (ANSI escapes would appear as `\\x1b`; none occur in these rows):")
w("")
w(block(table))
w("")
w("Closing rule and final verdict line:")
w("")
w(block([r2] + verdict))
w("")
w("- Table rows: **%d**; PASS **%d**; FAIL **%d**; lines between the rules that are not PASS/FAIL rows: %d."
  % (len(rows), n_pass, n_fail, len(non_row)))
w("- Row details are limited to 60 characters by the gate itself: `tools/release_gate.py` at `%s` "
  "prints `%s`. Rows whose detail sits at exactly the 60-character limit: %d; longer than 60: %d. "
  "So the truncated rows are truncated in the job log as printed, not by the fetch."
  % (HEAD[:8], "; ".join(gate_fmt) or "(not found)", at60, over60))
w("")
w("Requested rows (verbatim):")
w("")
w(block([byname[n][0] for n in WANT if n in byname]))
w("")
w("- `lean-axioms` named results, as printed: **%s**." % (axioms_n[0] if axioms_n else "(not found)"))
w("- `v3-receipts` receipt count, as printed: **%s** (`all hold`)." % (receipts_n[0] if receipts_n else "(not found)"))
w("- `legacy-records` count, as printed: **%s** record(s) in **%s** closed namespace(s) (`all intact`)."
  % ((legacy_n[0], legacy_n[1]) if legacy_n else ("(not found)", "(not found)")))
w("- Final verdict line body: `%s`" % bodies[v])
w("- Job API conclusion of the `Release gate` step: `%s`."
  % next((s.get("conclusion") for s in job["steps"] if s.get("name") == "Release gate"), "(not found)"))
w("")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(o))

# console digest
print("identical:", identical, "| lines:", N, "| original_length:", resp.get("original_length"))
print("first/last ts:", stamps[0], stamps[-1])
print("progress:", len(prog_idx), dict(prog_glyph), dict(prog_verb), "built:", len(built_any))
print("lake_final:", [bodies[i] for i in lake_final], "failed:", len(lake_failed))
print("(a)", len(a_hits), "ci", len(a_ci), "relc", len(a_relc))
print("(b) lean error:", len(b_lean), "##[error]:", len(b_gh), "x-mark lines:", len(b_x), "occ:", b_x_occ,
      "| error: anywhere:", len(b_colon), "error ci:", len(b_word), "fail words:", len(b_failed_word))
print("(c) sorryAx:", len(c_ax), "decl uses sorry:", len(c_decl), "sorry ci:", len(c_ci),
      "axiom lines:", len(ax_lines), "no-axiom lines:", len(no_ax), "sets:", dict(ax_sets))
print("(d) rows:", len(rows), "PASS:", n_pass, "FAIL:", n_fail, "non-row:", len(non_row), "at60:", at60, "over60:", over60)
print("    axioms:", axioms_n, "receipts:", receipts_n, "legacy:", legacy_n)
print("    verdict:", bodies[v])
print("warn/info/##[warning]:", n_warn, n_info, len(gh_warn))
print("wrote", OUT)
