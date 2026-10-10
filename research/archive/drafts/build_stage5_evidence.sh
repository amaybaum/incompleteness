#!/bin/sh
# Build the stage-5 evidence archive (deterministic: sorted entries, fixed mtime/owner) and its sha256 manifest.
# Run from the scratchpad directory after the stage-5 integration note is in place at pt/INTEGRATION-NOTE-STAGE5.md
# and both thread audits exist (pt/audit/D5/AUDIT-D.md, pt/audit/C5/AUDIT-C.md).
set -eu
cd "$(dirname "$0")/.."
OUT=evidence/pt-stage5-evidence.tar.gz
MAN=evidence/stage5.manifest.sha256
mkdir -p evidence
LIST=$(mktemp)
{
  echo pt/PROTOCOL-STAGE5.md; echo pt/PROTOCOL-STAGE5.sha256; echo pt/PROTOCOL-STAGE5-AMENDMENT-1.md; echo pt/PROTOCOL-STAGE5-AMENDMENT-1.sha256
  echo pt/INTEGRATION-NOTE-STAGE5.md
  echo pt/audit/STAGE3-RELAUNCH-LOG.md
  find pt/D5 pt/C5 -type f
  find pt/audit/D5 pt/audit/C5 pt/audit/stage5-inputs pt/audit/aborted-launches/stage5-launch1.md -type f
} | sort -u > "$LIST"
# every listed file must exist
while read -r f; do [ -f "$f" ] || { echo "missing: $f" >&2; exit 1; }; done < "$LIST"
tar --sort=name --mtime='2026-10-10 00:00:00Z' --owner=0 --group=0 --numeric-owner -cf - -T "$LIST" | gzip -n > "$OUT"
sha256sum $(cat "$LIST") > "$MAN"
printf '%s entries; archive %s\n' "$(wc -l < "$LIST")" "$(sha256sum "$OUT" | cut -c1-64)"
sha256sum "$MAN" | cut -c1-64
rm -f "$LIST"
