Anomaly sweep 1 of thread D5 (stage 5), 17:07:10Z-17:08:38Z.
Entries under pt/ newer than pt/D5/.start_marker (16:44:35Z) outside pt/D5/, pt/C5/, pt/audit/, pt/audit*-replay/:
pt/PROTOCOL-STAGE6.md (16:49:36Z), pt/PROTOCOL-STAGE6.sha256 (16:49:55Z), and directories pt/I1, pt/I2, pt/I3,
pt/I4 (start markers 16:51:44Z-16:53:28Z; files still being written at 17:08Z). Not written by this thread.
LIST.txt: the sweep's path list (find ... -newer .start_marker, exclusions pruned), 17:08:20Z.
MANIFEST-at-sweep.txt: mtime, size, sha256 of every listed file at 17:08:20Z (hashing only; content not read).
files/: byte copies (cp -p) made 17:08:37Z; originals left in place, untouched (moving them would write outside
pt/D5/ and remove files an active writer is using). COPY-MANIFEST.txt: sha256 and mtime of each copy.
One file changed between the sweep and the copy: ./I2/INVENTORY.md (actively written); its copy is the 17:08:37Z state.
Nothing here was read or used by this thread's work.
