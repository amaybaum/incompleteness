"""Replay a prior thread's script read-only: run it with its own directory first on sys.path (so its local helpers
resolve), under the caller's -I -B (no bytecode is written anywhere). stdout is the caller's redirect, inside eq2/C.
usage: python3 -I -B replay_prior.py <script.py> [args...]"""
import os
import runpy
import sys

script = os.path.abspath(sys.argv[1])
sys.path.insert(0, os.path.dirname(script))
sys.argv = [script] + sys.argv[2:]
runpy.run_path(script, run_name="__main__")
