#!/usr/bin/env bash
# Local reconstruction of the bounded tool-acceptance suite of .github/workflows/ledger-coverage.yml
# (job `suite`, input job=tool-acceptance) at aa62f5a47454983d0b3ac771450a78118fbaaab7.
# RECONSTRUCTED procedure, written in this session from the workflow text; not the lost Codex workspace script.
#
# Workflow inputs for tool-acceptance (workflow lines 160-171, 246-300):
#   F   = "the exact reviewed fixture snapshot" S (a commit holding CFG and ${CFG%/*}/a1-staging-transition.json
#         and ${CFG%/*}/execution-control-config.json)
#   CFG = the configuration path in F
#   M   = "the exact representative anchor for a suite" (the synthetic M_rep whose first-parent path shares B with S)
#   TOOL_BASE = refs/remotes/origin/main (9be526b6458c53bb7801d094227ec27503121269 here)
#   ACCEPTED  = the checkout HEAD (GITHUB_SHA)
# The suite has no mutation step: SW1/SW2 are not run by this job (no step invokes a mutation harness).
#
# Usage:  run.sh WT OUT [F CFG M]
#   Without F CFG M, only the F-independent steps run (PARTIAL), followed by a diagnostic gate over their records.
set -u
WT=$1; O=$2; F=${3:-}; CFG=${4:-}; M=${5:-}
EXP=verification/audits/foundations/a1exit-design-r6-20261125/EXPECTATIONS.json
REQ=verification/audits/foundations/a1exit-design-r6-20261125/REQUIREMENTS.json
A=verification/audits/foundations/ledger-coverage-tool-20261123
cd "$WT" || exit 99
mkdir -p "$O"
HEAD=$(git rev-parse HEAD)
[ "$HEAD" = aa62f5a47454983d0b3ac771450a78118fbaaab7 ] || { echo "HEAD $HEAD is not the target"; exit 98; }
[ -z "$(git status --porcelain)" ] || { echo "worktree not clean"; exit 97; }
TS=$O/../timing; mkdir -p "$TS"

step() {  # step NAME CMD...
  local n=$1; shift
  local t0=$(date +%s.%N)
  /usr/bin/time -v -o "$TS/$n.time" "$@" > "$TS/$n.stdout" 2> "$TS/$n.stderr"
  local rc=$?
  local t1=$(date +%s.%N)
  echo "$rc" > "$O/$n.exit"
  printf '%s\texit=%s\twall=%.1fs\tpeakRSS_kB=%s\n' "$n" "$rc" "$(echo "$t1 - $t0" | bc)" \
    "$(awk -F': ' '/Maximum resident/{print $2}' "$TS/$n.time")" | tee -a "$TS/steps.tsv"
}

# --- F-independent steps (workflow order) ---
step self-test   python3 -I -S -B tools/ledger_coverage.py self-test --out "$O/self-test"
step engine      python3 -I -S -B tools/ledger_coverage/adapters/engine_controls.py "$O/engine"
if [ -n "$F" ]; then
  # suite guard: writes the staged configuration the purity lint reads (workflow line 180)
  git --no-replace-objects cat-file blob "$F:$CFG" > "$O/../staged-config.json"
  step purity    python3 -I -B tools/ledger_coverage/adapters/staged_purity_lint.py --repo . --config "$F:$CFG" \
                   --staged-config "$O/../staged-config.json" --out "$O/purity"
fi
step synthetic   python3 -I -B tools/ledger_coverage/adapters/synthetic_fixture.py "$O/synthetic" .
step conformance python3 -I -B tools/ledger_coverage/adapters/conformance_controls.py "$O/conformance"
step obl29       python3 -I -B tools/ledger_coverage/adapters/obl29_controls.py "$O/obl29"
step custody     python3 -I -B tools/ledger_coverage/adapters/custody_controls.py "$O/custody"
step adjudication python3 -I -B tools/ledger_coverage/adapters/adjudication_controls.py "$O/adjudication"
step staging     python3 -I -B tools/ledger_coverage/adapters/staging_controls.py "$O/staging"
step sessions    python3 -I -B tools/ledger_coverage/adapters/sessions_controls.py "$O/sessions"

# --- F-dependent steps ---
if [ -n "$F" ]; then
  step a1-conformance python3 -I -B tools/ledger_coverage/adapters/a1_conformance.py --repo . --config "$F:$CFG" \
      --tool-revision "$HEAD" --tool-acceptance --out "$O/a1-conformance"
  D="${CFG%/*}/a1-staging-transition.json"
  digest=$(git --no-replace-objects cat-file blob "$F:$D" | sha256sum)
  step a1-controls python3 -I -B tools/ledger_coverage/adapters/a1_controls.py --repo . --config "$F:$CFG" --main "$M" \
      --rep-template "$HEAD:$A/rep/control-instance.json" --rep-snapshot "$F" --rep-descriptor-sha256 "${digest%% *}" \
      --tool-candidate "$HEAD" --out "$O/a1-controls"
fi

# --- gate ---
set --
for r in engine purity synthetic conformance obl29 custody adjudication staging sessions a1-conformance a1-controls; do
  if [ -f "$O/$r/control-records.json" ]; then set -- "$@" --records "$O/$r/control-records.json"; fi
done
TOOL_BASE=$(git --no-replace-objects rev-parse --verify 'refs/remotes/origin/main^{commit}')
ACCEPTED=$HEAD
if [ -n "$F" ]; then set -- "$@" --tool-candidate "$ACCEPTED" --fixed-config "$F:$CFG"; else set -- "$@" --tool-candidate "$ACCEPTED"; fi
# The preview objects are written to a private object directory, never to the shared store.
export GIT_OBJECT_DIRECTORY=$O/../preview-objects GIT_ALTERNATE_OBJECT_DIRECTORIES=$(git rev-parse --git-common-dir)/objects
mkdir -p "$GIT_OBJECT_DIRECTORY"
TREE=$(git --no-replace-objects merge-tree --write-tree "$TOOL_BASE" "$ACCEPTED")
PREVIEW=$(GIT_AUTHOR_DATE='1700000000 +0000' GIT_COMMITTER_DATE='1700000000 +0000' git --no-replace-objects \
  -c user.name='A1 tool preview' -c user.email=preview@invalid.invalid \
  commit-tree "$TREE" -p "$TOOL_BASE" -p "$ACCEPTED" -m 'A1 tool preview')
echo "TOOL_BASE=$TOOL_BASE TREE=$TREE PREVIEW=$PREVIEW" | tee "$TS/preview.txt"
step gate python3 -I -S -B tools/ledger_coverage/gate/control_gate.py --expectations "$EXP" --requirements "$REQ" "$@" \
  --repo . --tool-base "$TOOL_BASE" --tool-preview "$PREVIEW" --out "$O/gate"
unset GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES

# --- evidence digest (workflow "evidence digest" step) ---
( cd "$O" && find . -type f ! -name evidence-digest.txt -print0 | sort -z | xargs -0 sha256sum > evidence-digest.txt
  sha256sum evidence-digest.txt ) | tee "$TS/evidence-digest.sha256"
