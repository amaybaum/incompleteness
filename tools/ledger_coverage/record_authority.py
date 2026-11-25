"""The record directories the tool authorizes for the record-directory rule (design amendment r4, A.3).

A configuration's directory is admitted to the rule only if it equals a member of this tuple by string equality. The
tuple is part of the tool's files: no configuration, record or command-line argument adds to it, and changing it is a
tool revision. It lies outside the engine, which carries no retirement constant (design sec. 16.1).
"""

authorized_record_directories = ('verification/audits/foundations/a1exit-deletion-20261121',)
