"""Reviewer probe: run the v8 dry run (combinatorics only) with an import trap that makes any
import of the engine, the reference or the native evaluator fail, so that no context or
closure can be built. Usage: dryrun_trap.py <code dir> [l2plan args...]"""
import sys, runpy
class Trap:
    def find_spec(self, name, path=None, target=None):
        if name.split('.')[0] in ('s0geom', 's0ref', 's0native', 'l2analysis', 'l2refcheck', 'l2enum', 'l2s1a'):
            raise ImportError('TRAPPED import of ' + name)
        return None
sys.meta_path.insert(0, Trap())
code = sys.argv[1]
sys.path.insert(0, code)
sys.argv = [code + '/l2plan.py'] + sys.argv[2:]
runpy.run_path(code + '/l2plan.py', run_name='__main__')
