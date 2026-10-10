#!/bin/sh
# Build the stage-4 evidence archive (deterministic: sorted entries, fixed mtime/owner) and its sha256 manifest.
# Run from the scratchpad directory after the stage-4 integration note is in place at pt/INTEGRATION-NOTE-STAGE4.md
# and both thread audits exist (pt/audit/Y/AUDIT-Y.md, pt/audit/Z/AUDIT-Z.md).
set -eu
cd "$(dirname "$0")/.."
OUT=evidence/pt-stage4-evidence.tar.gz
MAN=evidence/stage4.manifest.sha256
mkdir -p evidence
LIST=$(mktemp)
{
  echo pt/PROTOCOL-STAGE4.md; echo pt/PROTOCOL-STAGE4.sha256
  echo pt/INTEGRATION-NOTE-STAGE4.md
  echo pt/audit/STAGE3-RELAUNCH-LOG.md
  find pt/Y pt/Z -type f
  find pt/audit/Y pt/audit/Z pt/audit/stage4-inputs -type f
} | sort -u > "$LIST"
# every listed file must exist
while read -r f; do [ -f "$f" ] || { echo "missing: $f" >&2; exit 1; }; done < "$LIST"
tar --sort=name --mtime='2026-10-10 00:00:00Z' --owner=0 --group=0 --numeric-owner -cf - -T "$LIST" | gzip -n > "$OUT"
sha256sum $(cat "$LIST") > "$MAN"
printf '%s entries; archive %s\n' "$(wc -l < "$LIST")" "$(sha256sum "$OUT" | cut -c1-64)"
sha256sum "$MAN" | cut -c1-64
rm -f "$LIST"
