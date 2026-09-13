# Day_5_log_parser.py
# Counts requests by status code and by IP address in a web access log.
# Usage:  python Day_5_log_parser.py Day_5_access_log.txt
# It only READS the log. It changes nothing and sends nothing anywhere.
import re
import sys
from collections import Counter

# IP  -  -  [time]  "METHOD PATH PROTOCOL"  STATUS
LINE = re.compile(r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) [^"]*" (\d{3}) ')

statuses = Counter()
ips = Counter()

with open(sys.argv[1], encoding="utf-8") as log:
    for line in log:
        match = LINE.match(line)
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
