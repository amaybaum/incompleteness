#!/bin/sh
# Build the stage-3 evidence archive (deterministic: sorted entries, fixed mtime/owner) and its sha256 manifest.
# Run from the scratchpad directory after the stage-3 integration note is in place at pt/INTEGRATION-NOTE-STAGE3.md.
set -eu
cd "$(dirname "$0")/.."
OUT=evidence/pt-stage3-evidence.tar.gz
MAN=evidence/stage3.manifest.sha256
mkdir -p evidence
LIST=$(mktemp)
{
  echo pt/PROTOCOL-STAGE3.md; echo pt/PROTOCOL-STAGE3.sha256
  echo pt/STAGE3-LAUNCH-LOG.md; echo pt/INTEGRATION-NOTE-STAGE3.md; echo pt/inputs4.manifest.sha256
  find pt/X pt/U -type f
  find pt/audit/X pt/audit/U pt/audit/NS pt/audit/reviews pt/audit/stage3-inputs pt/audit/aborted-launches -type f
  echo pt/audit/STAGE3-RELAUNCH-LOG.md
} | sort -u > "$LIST"
# every listed file must exist
while read -r f; do [ -f "$f" ] || { echo "missing: $f" >&2; exit 1; }; done < "$LIST"
tar --sort=name --mtime='2026-10-10 00:00:00Z' --owner=0 --group=0 --numeric-owner -cf - -T "$LIST" | gzip -n > "$OUT"
sha256sum $(cat "$LIST") > "$MAN"
printf '%s entries; archive %s\n' "$(wc -l < "$LIST")" "$(sha256sum "$OUT" | cut -c1-64)"
sha256sum "$MAN" | cut -c1-64
rm -f "$LIST"
