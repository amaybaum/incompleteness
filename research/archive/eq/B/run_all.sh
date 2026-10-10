#!/bin/sh
# EQ-B replay: run every script twice, compare outputs byte for byte, print hashes.
# Exact scripts: b1..b6.  Exploration (float, seeded, certifies nothing): x1..x4.
set -u
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1
status=0
for s in b1_conditioning b2_qt b3_rolex b4_jkflow b5_localwords b6_qb2 \
         x1_jk_flow_float x2_local_words_float x3_simple_words_float x4_d7_word_float; do
  python3 -I -B -u "$s.py" > "$s.out" 2>&1
  python3 -I -B -u "$s.py" > "$s.rerun" 2>&1
  if cmp -s "$s.out" "$s.rerun"; then same=identical; else same=DIFFERENT; status=1; fi
  hs=$(sha256sum "$s.py" | cut -c1-16)
  ho=$(sha256sum "$s.out" | cut -c1-16)
  verdict=$(grep '^VERDICT' "$s.out" | tail -1)
  echo "$s  script=$hs  out=$ho  replay=$same  ${verdict:-exploration}"
done
for f in blib.py qlib.py jk.py EqBDraft.lean; do
  echo "$f  $(sha256sum "$f" | cut -c1-16)"
done
exit $status
