#!/usr/bin/env bash
# Run one evidence-retention check for the `retention-tests` workflow, from the repository root.
#
#   retention_mutant_run.sh CHECK - LOG                    run CHECK; exit with its status
#   retention_mutant_run.sh CHECK EXPECT LOG CLASSIFIER    run CHECK on a mutant and classify the run with
#                                                          CLASSIFIER (tools/mutant_verdict.py or a copy of
#                                                          it); exit with the classifier's status
#
# Every check, control and mutant in the workflow goes through this one command table. Each run is bounded
# by `timeout -k 30s 27m`, so a hung check ends with a timeout or kill status, which the classifier reads as
# INFRA. The last 60 lines of the output are echoed; the full output is in LOG.
set -u
if [ "$#" -lt 3 ]; then
  echo "usage: $0 CHECK - LOG | CHECK EXPECT LOG CLASSIFIER" >&2
  exit 2
fi
check=$1 expect=$2 log=$3
d=verification/audits/evidence-retention
case "$check" in
  gate)                 cmd=(python3 -B "$d/check_retention.py" --gate) ;;
  retention)            cmd=(python3 -B "$d/check_retention.py") ;;
  retention-self-test)  cmd=(python3 -B "$d/check_retention.py" --self-test) ;;
  objects)              cmd=(python3 -B "$d/check_objects.py") ;;
  objects-reconstitute) cmd=(python3 -B "$d/check_objects.py" --reconstitute) ;;
  objects-self-test)    cmd=(python3 -B "$d/check_objects.py" --self-test) ;;
  tools-self-test)      cmd=(bash -c "python3 -B '$d/compare_result.py' --self-test && python3 -B '$d/job_outputs.py' --self-test") ;;
  *) echo "INVALID  unknown check $check"; exit 2 ;;
esac
timeout -k 30s 27m "${cmd[@]}" > "$log" 2>&1
rc=$?
tail -n 60 "$log"
if [ "$expect" = "-" ]; then
  echo "$check exited $rc"
  exit "$rc"
fi
if [ "$#" -ne 4 ]; then
  echo "INVALID  a classified run needs CLASSIFIER" >&2
  exit 2
fi
python3 -I -B "$4" "$check" "$rc" "$expect" "$log"
