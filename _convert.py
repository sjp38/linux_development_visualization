#!/usr/bin/env python2.7

import sys

"""
Example input is as below:
```
0c97bf8 1558615535 Miguel Ojeda

kernel/trace/trace.c     |  6 +-----
kernel/trace/trace.h     | 18 ++++++++++++++++++
kernel/trace/trace_kdb.c |  6 +-----
3 files changed, 20 insertions(+), 10 deletions(-)
66883da 1558756103 Gabriel Krisman Bertazi

in_loanged, 1 insertion(+), 1 deletion(-)
51816e9 1558726942 Waiman Long

kernel/locking/lock_events.h | 42 ++++++++++++++++++++++++++++++++++++++++--
1 file changed, 40 insertions(+), 2 deletions(-)
```
"""

in_log = False
for line in sys.stdin:
    line = line.strip()
    fields = line.split()
    if not in_log:
        time = fields[1]
        name = ' '.join(fields[2:])
        in_log = True
        continue
    if line == "":
        continue
    if ((fields[1] == "file" or fields[1] == "files") and
            fields[2] == "changed,"):
        in_log = False
        continue
    if len(fields) < 4:
        print "something wrong! %s" % line
        sys.exit(1)
    file_ = fields[0]
    diff = fields[3]
    action = 'M'
    if diff.find('+') == -1:
        action = 'D'
    elif diff.find('-') == -1:
        action = 'A'
    print "%s|%s|%s|%s" % (time, name, action, file_)
