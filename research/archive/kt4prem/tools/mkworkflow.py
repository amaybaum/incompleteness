"""Print D's workflow with exactly the frozen edit of the controls.py given as argv[1]."""
import importlib.util, subprocess, sys
spec = importlib.util.spec_from_file_location('c', sys.argv[1]); c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
sys.stdout.write(c.apply_edit(c.show(c.D, c.WORKFLOW)))
