#!/bin/sh
# Build the stage-6 evidence archive (deterministic: sorted entries, fixed mtime/owner) and its sha256 manifest.
# Run from the scratchpad directory after pt/INTEGRATION-NOTE-STAGE6.md and the audits exist.
set -eu
cd "$(dirname "$0")/.."
OUT=evidence/pt-stage6-evidence.tar.gz
MAN=evidence/stage6.manifest.sha256
mkdir -p evidence
LIST=$(mktemp)
{
  echo pt/PROTOCOL-STAGE6.md; echo pt/PROTOCOL-STAGE6.sha256
  echo pt/PROTOCOL-STAGE6-AMENDMENT-1.md; echo pt/PROTOCOL-STAGE6-AMENDMENT-1.sha256
  echo pt/PROTOCOL-STAGE6-AMENDMENT-2.md; echo pt/PROTOCOL-STAGE6-AMENDMENT-2.sha256
  echo pt/INTEGRATION-NOTE-STAGE6.md
  echo pt/audit/STAGE3-RELAUNCH-LOG.md
  find pt/I1 pt/I2 pt/I3 pt/I4 pt/G6 pt/R6 pt/T6 -type f
  find pt/audit/stage6-inputs -type f
} | sort -u > "$LIST"
while read -r f; do [ -f "$f" ] || { echo "missing: $f" >&2; exit 1; }; done < "$LIST"
tar --sort=name --mtime='2026-10-10 00:00:00Z' --owner=0 --group=0 --numeric-owner -cf - -T "$LIST" | gzip -n > "$OUT"
sha256sum $(cat "$LIST") > "$MAN"
printf '%s entries; archive %s\n' "$(wc -l < "$LIST")" "$(sha256sum "$OUT" | cut -c1-64)"
sha256sum "$MAN" | cut -c1-64
rm -f "$LIST"
