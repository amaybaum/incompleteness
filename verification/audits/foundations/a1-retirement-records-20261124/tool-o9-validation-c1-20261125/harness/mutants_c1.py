"""Mutants of correction 1 (3184c7f9): (id, file under tools/, [(old, new), ...], rule)."""
CK = 'ledger_coverage/engine/checker.py'
SC = 'ledger_coverage/engine/schemas/oi-ledger-coverage-5.schema.json'
DL = 'ledger_coverage/engine/delegation.py'
CF = 'ledger_coverage/engine/config.py'
CC = 'ledger_coverage/adapters/conformance_controls.py'
OWNER = "uses: [A-Za-z0-9](?:-?[A-Za-z0-9])*/"

MUTANTS = [
    ('C01', CK, [(OWNER, "uses: [A-Za-z0-9_.-]+/")], 'B-1: the owner is a GitHub account name (the rule before the fix)'),
    ('C02', CK, [(OWNER, "uses: [A-Za-z0-9.](?:-?[A-Za-z0-9.])*/")], 'B-1: the owner admits no dot'),
    ('C03', CK, [(OWNER, "uses: (?:\\.\\./)?[A-Za-z0-9](?:-?[A-Za-z0-9])*/")], 'B-1: the owner admits no parent path'),
    ('C04', CK, [(OWNER, "uses: [A-Za-z0-9-](?:-?[A-Za-z0-9])*/")],
     'B-1: the owner does not start with a hyphen (outside the B-1 counterexamples)'),
    ('C05', SC, [('    "blob_sha256",\n    "admission"\n', '    "blob_sha256"\n')],
     'N-2: the /5 schema requires config.admission'),
    ('C06', CK, [("    try:\n        repo.resolve(M)\n    except Exception as exc:\n        raise ValueError('the resolved main cannot be read: %s' % exc)\n", "")],
     'N-1: the re-resolved main must be readable by the verified reader'),
    ('C07', DL, [("        env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)\n        r = subprocess.run(['git', 'clone'",
                  "        env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1')\n        r = subprocess.run(['git', 'clone'")],
     'D-11 (O-3): the delegated clone ignores the global git configuration'),
    ('C08', DL, [("        env = dict(os.environ, GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull)\n        r = subprocess.run(['git', 'clone'",
                  "        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull)\n        r = subprocess.run(['git', 'clone'")],
     'D-11 (O-3): the delegated clone ignores the system git configuration (outside the local control)'),
    ('C09', CF, [("            except Unresolvable:\n                raise stop('CONFIG_INCONSISTENT', 'merge %s is not resolvable' % m['commit'][:12])",
                  "            except Unresolvable:\n                continue")],
     'D-6: an unresolvable HP merge is an error (GV4 accepts either error class)'),
    ('C10', CF, [("            except Unresolvable:\n                raise stop('CONFIG_INCONSISTENT', 'merge %s is not resolvable' % m['commit'][:12])",
                  "            except Unresolvable:\n                return")],
     'D-6: an unresolvable HP merge ends the HP check with an error, not a pass'),
    ('C11', CC, [("    p = subprocess.run([sys.executable, '-I', '-S', '-c', 'import sys, json; print(json.dumps(sys.path))'], cwd='/',",
                  "    p = subprocess.run([sys.executable, '-I', '-c', 'import sys, json; print(json.dumps(sys.path))'], cwd='/',")],
     'D-7: EI6 admits only the standard library (the -I import path before the correction)'),
    ('C12', CC, [("    def entry(self, d, extra=(), flags=('-I', '-S', '-B'), out_name='out'):",
                  "    def entry(self, d, extra=(), flags=('-I', '-B'), out_name='out'):"),
                 ("    code6, res6, err6 = e.entry(d6, flags=('-I', '-S', '-B', '-v'))",
                  "    code6, res6, err6 = e.entry(d6, flags=('-I', '-B', '-v'))")],
     'D-7: the EI runs use the workflow\'s flags -I -S -B'),
]
