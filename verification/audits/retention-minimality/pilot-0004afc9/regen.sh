#!/bin/sh
# regen.sh -- regeneration test (rule K1) for the pilot's archive entries against main's history alone.
# Usage: sh regen.sh <full-history clone holding only main, archive NOT materialized>
# For each id: is it in the clone's object store, is it reachable from main (rev-list --objects), and at which
# paths outside the archive does main's history carry it. An id main carries outside the archive would then be
# byte-compared with the archive's decoded copy; an id main does not carry cannot be regenerated from main.
set -u
R=$1
MAIN=92de3143046b26d7fa2ce3b13ce3ea4b1e18a37a
test "$(git -C "$R" rev-parse --is-shallow-repository)" = false || { echo "shallow clone: void"; exit 2; }
git -C "$R" rev-list --objects "$MAIN" > "$R.main-objects.txt" || exit 2
echo "objects reachable from main: $(wc -l < "$R.main-objects.txt")"
for o in 0004afc9360117ba61523b72854de1aaf63705f0 e5e70bc53a1c23a7b83ed902d9879868292cf5d9 \
         dda14af07f862ee459a803e4e888c286b1f6bd57 f7042861b741c353e989fc0f390a525bd1604a45 \
         23ddaf02eb50809f4d87cf426c20c81a8e30cf18 016e542872383b296bb0255d8e9ff1561d36fbcc \
         4151e7c65fbb9ceb331636cb5becce876eddacfa 17de29c27ed43d7f105aa8518451d8ed61c59937 \
         e8e9a726ad688afc447214cbdc52b96675513307 a2a2a7762446225c91ef1bfa17af98d14ecece26; do
  t=$(git -C "$R" cat-file -t "$o" 2>/dev/null || echo absent)
  n=$(grep -c "^$o" "$R.main-objects.txt")
  paths=$(git -C "$R" log "$MAIN" -m --format= --name-only --find-object="$o" 2>/dev/null | sort -u |
          grep -v '^$' | grep -v '^verification/audits/evidence-retention/' | tr '\n' ' ')
  echo "$o store=$t reachable_from_main=$n paths_outside_archive=[${paths}]"
done
