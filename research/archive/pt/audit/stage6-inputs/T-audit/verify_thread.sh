#!/bin/sh
# Coordinator's mechanical verification of a thread directory: (1) every file the thread's RESULT.md lists with a
# sha256 verifies; (2) every final script (<name>.py, not .runN.py) replays byte-identically into <outdir>/replay/.
# Usage: sh verify_thread.sh <thread-dir> <outdir>   (paths absolute or relative to the cwd)
# Scripts that write files are detected by a pattern scan and listed, not replayed (the thread's own replay stands).
set -u
T=$(cd "$1" && pwd); O=$(cd "$2" && pwd); mkdir -p "$O/replay"
echo "== hashes listed in RESULT.md ($(date -u +%H:%M:%SZ))"
# the hash block: lines of 64 hex + two spaces + filename
grep -E '^[0-9a-f]{64}  ' "$T/RESULT.md" > "$O/listed_hashes.txt"
( cd "$T" && sha256sum -c "$O/listed_hashes.txt" ) > "$O/listed_hashes.check" 2>&1
NOK=$(grep -c ': OK$' "$O/listed_hashes.check"); NALL=$(wc -l < "$O/listed_hashes.txt")
echo "hashes OK $NOK / $NALL"; grep -v ': OK$' "$O/listed_hashes.check" | sed 's/^/  not-ok: /'
echo "RESULT.md $(sha256sum "$T/RESULT.md" | cut -c1-64)"
echo "== replays ($(date -u +%H:%M:%SZ))" | tee "$O/replay/REPLAY-LOG.txt"
for s in "$T"/*.py; do
  n=$(basename "$s" .py)
  case "$n" in *.run[0-9]*|*.replay) continue;; esac
  if grep -Eq "open\([^)]*['\"][wa]|write_text|writelines|shutil\.|os\.rename|os\.remove|\.to_csv|mkdir" "$s"; then
    echo "SKIP $n (writes files; thread's own replay stands)" | tee -a "$O/replay/REPLAY-LOG.txt"; continue
  fi
  ( cd "$T" && python3 -I -B "$n.py" > "$O/replay/$n.out" 2> "$O/replay/$n.err"; echo "exit $?" >> "$O/replay/$n.err" )
  so=DIFFER; se=DIFFER
  cmp -s "$T/$n.out" "$O/replay/$n.out" && so=IDENTICAL
  cmp -s "$T/$n.err" "$O/replay/$n.err" && se=IDENTICAL
  echo "REPLAY $n stdout=$so stderr=$se $(date -u +%H:%M:%SZ)" | tee -a "$O/replay/REPLAY-LOG.txt"
done
echo "DONE $(date -u +%H:%M:%SZ)" | tee -a "$O/replay/REPLAY-LOG.txt"
