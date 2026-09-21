# Day_06_fw_parser.py  --  parser v2
# Reads EITHER a web access log (Day 04 format) OR a Windows Firewall log
# (pfirewall.log) and prints simple counts. It only READS the file. It changes
# nothing and sends nothing anywhere.
#
# Usage:  python Day_06_fw_parser.py Day_5_access_log.txt
#         python Day_06_fw_parser.py Day_06_pfirewall.log
import re
import sys
from collections import Counter

# ---- part 1: the web access log (same regex as Day 04) ---------------------
ACCESS_LINE = re.compile(r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) [^"]*" (\d{3}) ')

def parse_access_log(lines):
    statuses = Counter()
    ips = Counter()
    for line in lines:
        match = ACCESS_LINE.match(line)
        if not match:
            continue                      # skip lines that are not requests
        ip, when, method, path, status = match.groups()
        statuses[status] += 1
        ips[ip] += 1
    print("Requests by status code:")
    for status, count in sorted(statuses.items()):
        print(f"  {status}  {count}")
    print("Requests by IP address:")
    for ip, count in ips.most_common():
        print(f"  {ip:<16} {count}")

# ---- part 2: the Windows Firewall log (new today) --------------------------
# #Fields: date time action protocol src-ip dst-ip src-port dst-port size ...
def parse_firewall_log(lines):
    actions = Counter()
    drop_by_src = Counter()
    drop_by_port = Counter()
    for line in lines:
        if line.startswith("#") or not line.strip():
            continue                      # skip the header and blank lines
        fields = line.split()
        if len(fields) < 8:
            continue                      # not a complete record
        date, time, action, proto, src, dst, sport, dport = fields[:8]
        actions[action] += 1
        if action == "DROP":
            drop_by_src[src] += 1
            drop_by_port[dport] += 1
    print("Records by action:")
    for action, count in sorted(actions.items()):
        print(f"  {action:<6} {count}")
    print("DROP by source address:")
    for src, count in drop_by_src.most_common():
        print(f"  {src:<16} {count}")
    print("DROP by destination port (top 5):")
    for port, count in drop_by_port.most_common(5):
        print(f"  {port:<6} {count}")

# ---- decide which kind of file this is, from its first line ----------------
with open(sys.argv[1], encoding="utf-8") as log:
    lines = log.readlines()

if lines and lines[0].startswith("#Version"):
    parse_firewall_log(lines)
else:
    parse_access_log(lines)
