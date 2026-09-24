# DAY 10 — UNIT ASSESSMENT GUIDE
## CS-ICT251101 Monitor and Report Cyber Threats · Institutional Assessment
### Cyber Threat Monitoring Level I · Day 10 of 15 · 1:00–4:00 PM · Trainer / assessor only

> **Keep this file secure.** It contains the keys. The two candidate files, `Day_10_Written_Exam.docx` and `Day_10_Practical_Assessment_Brief.docx`, are released **at 1:10 and at 2:00**. They are never included in the joining note.

> **Two conditions still hold.** There is no SIEM server, so every instrument uses what the candidates have actually done on their own machines and on paper. The candidates are beginners, which is why the wording is plain, the instructions come in numbered steps, and the time is generous. **Nothing in the assessment needs Wazuh, Sandbox, Atomic Red Team, Hayabusa or TCPView.**

---

## WHAT IS IN HERE

| Part | What | Use |
|------|------|-----|
| 1 | The assessment plan: methods, evidence rule, result rule | Read before the day |
| 2 | Set-up and rules (online, cameras on) | 12:45 |
| 3 | The briefing script (1:00) | Read aloud |
| 4 | The written exam: **key** | Marking |
| 5 | The demonstration: Case WKS-164: data, **key**, observation checklist | 2:00–3:30 |
| 6 | Oral questioning: the bank and what counts as competent | 2:00–3:50 |
| 7 | Portfolio with interview: the portfolio map and the interview questions | 2:00–3:50 |
| 8 | The result sheet and the reassessment rule | After 4:00 |
| 9 | Contingency | Anytime |

---
---

# PART 1 — THE ASSESSMENT PLAN

## The three methods the CS names, and what each one carries

| Method | Instrument | Time | What it proves |
|--------|-----------|------|----------------|
| **Written exam** | 25 multiple-choice (1 mark each) + 5 short answer (3 marks each) = **40 marks** | 40 min | Required knowledge across all five elements: sources of alerts, log and detection management, severity, SOP, malicious software behaviours, attack framework, and the basic OS, web, scripting and network knowledge (1.1–1.4) |
| **Demonstration with oral questioning** | Case **WKS-164**, four parts, done alone on their own machine and on the brief's forms · **3 oral questions** in an individual breakout | 90 min + orals | Critical aspects **1.1.1 to 1.5.4**, performed on a case the candidate has not seen |
| **Portfolio with interview** | The Day 3 and Day 5–10 evidence, checked against the portfolio map (Part 7) · **2 interview questions** | During the orals | That the portfolio is the candidate's own work, and that it covers every critical aspect a second time |

## The evidence rule

Each **critical aspect** (1.1.1–1.5.4, nineteen in all) needs **at least one piece of direct evidence** that the assessor has seen or heard. The demonstration is the main source. The portfolio and the oral questions **confirm** it, or **fill a gap** when the demonstration did not show something clearly.

## The result rule

| Result | When |
|--------|------|
| **Competent** on the unit | All 19 critical aspects are evidenced **and** the written exam is **28 / 40 (70%) or more** |
| **Not Yet Competent (NYC)**, one or more aspects | An aspect has no acceptable evidence from any method. **Only that aspect is reassessed** (Part 8) |
| **NYC on the written exam** | Below 28 / 40. The candidate re-sits a **parallel** written paper before Day 15. The demonstration result stands |

> **The reason matters more than the answer. It is the same rule the class has had since Day 3.** A decision that differs from the key but comes with a reason that names the evidence and the SOP is accepted. The oral questions are where you find out whether the reason is there.

## Who assesses

The trainer is the institutional assessor. If a second assessor is available, use them for the **orals** so that the trainer can watch the demonstration. **One assessor can take up to 16 candidates** in the 2:00–3:50 window, at about 6 minutes each. For more than 16, see Part 9.

---
---

# PART 2 — SET-UP AND RULES

## Before 12:45
- [ ] A **submission folder** per candidate, e.g. `Assessment/CTM-U1/<surname>/`, or one online form for the exam and one upload for the practical
- [ ] The **written exam** as an online form (auto-marks Part A) **or** the `.docx` sent at 1:10 and returned by 1:50. Both work
- [ ] Breakout rooms named **ORAL-1**, **ORAL-2** (if two assessors)
- [ ] This file open at Part 5 and Part 6. The result sheet (Part 8) open to fill in
- [ ] **Recording on** for the whole afternoon. It is the assessor's evidence of the orals and the notification call

## The rules, read aloud at 1:00

| Rule | Why |
|------|-----|
| **Camera on** for the whole afternoon, face and hands in view during the exam | It is an observed assessment |
| **Written exam: closed book.** No notes, no browser, no chat | It tests what they know |
| **Demonstration: open book.** Handout, Activity Packs, their own templates and `attack.mitre.org` are allowed. **No talking to other candidates, no AI tools, no chat** | At work, an analyst uses the SOP and the references. They do not use a colleague to do the job for them |
| **EICAR only.** The only thing created on the machine is the EICAR test file | The same safety rule as Days 6–8 |
| **Own machine, own traffic** | The same rule as Days 5–10 |
| If the connection drops, **rejoin and tell the assessor by chat** the time it dropped | The time is added back |
| Candidates may **ask for an instruction to be repeated**, not for an answer | Fairness |
| Results are **not** given today. Each candidate gets their result and feedback **individually** at the start of Day 11 | Moderation, and privacy |

---
---

# PART 3 — THE BRIEFING SCRIPT (1:00–1:10)

> "Good afternoon. This is the assessment for the first core unit, CS-ICT251101, Monitor and report cyber threats. It has three parts. A written exam, forty minutes, closed book. Then a demonstration: a new case you have not seen, ninety minutes, open book, on your own machine and on forms. While you work, I will call each of you into a breakout room for about six minutes. There you will make one short phone call to me, I will ask you three questions, and I will ask you two questions about your portfolio."

> "There is no trick in it. Everything in it you have done between Day 3 and this morning. It is marked the way everything has been marked: the reason matters more than the answer. If you are not sure, write your reason."

> "The rules: camera on the whole time. No chat and no talking to each other. In the demonstration you may use your handouts, your activity packs and the ATT&CK website, but no AI tools. The only test file you make is EICAR. If you drop off, rejoin and tell me the time in the chat."

> "If something is not competent today, it is not the end. You redo only that part, before Day 15. You will get your result and your feedback individually at the start of tomorrow."

> "Any questions about the rules?" *(Answer them.)* "Then I am sending the written exam now. It is 1:10. You have until 1:50."

---
---

# PART 4 — THE WRITTEN EXAM: KEY

### 40 marks · pass 28 · the paper is `Day_10_Written_Exam.docx`

## Part A: multiple choice (25 × 1 mark)

| Q | Key | Why (for moderation) | Element |
|---|-----|----------------------|---------|
| 1 | **C** | A DLP alert is a detection alert source in the CS range. A walk-in is an incident-report channel | E1 · 1.5 |
| 2 | **B** | Phone, walk-in, email, SMS, chat and video conference are incident-report channels | E1 · PC 1.2 |
| 3 | **D** | Mass renaming plus a ransom note is the ransomware red flag | E1 · PC 1.3 |
| 4 | **A** | Containment, not severity, separates a threat from a detection | E1 · PC 1.4 |
| 5 | **C** | A blocked attempt is contained, so it is a detection | E1 · PC 1.4 |
| 6 | **B** | "When it happened" and "when I saw it" are kept apart. The gap between them matters | E1 · PC 1.5 |
| 7 | **D** | `RealTimeProtectionEnabled False` means it is installed but not operational | E2 · PC 2.2 |
| 8 | **A** | EICAR is a harmless agreed test string | E2 · PC 2.3 |
| 9 | **C** | Event 1116 = detected | E3 · PC 3.1 |
| 10 | **B** | Event 1117 = action taken, and error code 0 means success | E3 · PC 3.2 |
| 11 | **C** | The three proofs are the 1117, `ActionSuccess True`, and `Test-Path False` | E3 · PC 3.2 |
| 12 | **A** | Signatures 41 days old means it will miss recent threats. Update them | E3 · PC 3.3 |
| 13 | **D** | An offline scan is for something that hides from Windows while Windows runs | E3 · PC 3.4 |
| 14 | **B** | Event 1002 = the scan stopped early. It does not count | E4 · PC 4.2 |
| 15 | **C** | A 1116 followed by nothing is kind 3, no action taken | E4 · PC 4.2 |
| 16 | **A** | A suspected false positive on a business file goes to the vendor | E4 · PC 4.3 |
| 17 | **D** | An OS patch and a change window are IT department manager actions | E4 · PC 4.3 |
| 18 | **B** | High and Critical are notified. Medium is recorded | E5 · PC 5.1 |
| 19 | **C** | The source is an inside address, so it is lateral movement | E5 · PC 5.2 |
| 20 | **A** | Many failed logons and no success means attempted, not confirmed | E5 · PC 5.2 |
| 21 | **D** | Huge `bytes_out` in one outbound session is the shape of data leaving (egress) | E5 · PC 5.3 |
| 22 | **B** | Tactic = the goal (why). Technique = the method (how) | E5 · 5.3 |
| 23 | **C** | 7045 = a service was installed. That is installation behaviour | E5 · PC 5.4 |
| 24 | **A** | Port 3389 = RDP | knowledge 1.4 |
| 25 | **B** | Port forwarding maps a public port to an inside host | knowledge 1.4 |

## Part B: short answer (5 × 3 marks)

**Q26.** *A Defender alert says a Trojan was "quarantined". Name the three things you check to prove the action really happened.* (3)
- 1 mark each: **event 1117** with error code 0 · **`Get-MpThreatDetection` shows `ActionSuccess True`** · **the file is gone from disk (`Test-Path` False)**. Accept "Protection history says Quarantined" for **half** a mark only, because that is the story, not the evidence.

**Q27.** *Name the four "appropriate authorities" and say, for one of them, what you would send them.* (3)
- 2 marks for all four (IT department manager · information security manager · security solution / vendor · CISO). 1 mark if only three are named.
- 1 mark for a correct pairing, e.g. *vendor: updates failing on many PCs / a false positive* · *IT manager: isolate, re-image, patch* · *infosec manager: an uncontained threat* · *CISO: Critical, one paragraph, within 10 minutes*.

**Q28.** *What is the difference between "spread" and "lateral movement"? Give an example of each.* (3)
- 1 mark: **spread** = which hosts are affected and how far. 1 mark: **lateral movement** = how it moved from one inside host to another (method, account). 1 mark: examples, e.g. *spread: WKS-311 and SRV-BAK-02 confirmed, SRV-FILE-01 attempted* · *lateral: WKS-311 → SRV-BAK-02 over SMB with svc_backup*.

**Q29.** *A report says: "SRV-FIN-02 was also part of this attack because it was encrypted at the same time." What is wrong with this, and what should the analyst do?* (3)
- 1 mark: **the same time is not evidence**, so link with evidence, not with the clock. 1 mark: name what would join them, e.g. *the same source address, account, file hash or outside address*. 1 mark: *check, then report it as "not linked" (or "under investigation") and keep it a separate case unless a line joins them*.

**Q30.** *Explain "exploitation activity" and "installation behaviour", with one example of each and an ATT&CK ID for either.* (3)
- 1 mark: **exploitation** = how the attacker got in or got more access, e.g. *password guessing (T1110.001), a user tricked into running a macro (T1204.002), an exploit of unpatched software*. 1 mark: **installation** = what they leave behind to stay or restart, e.g. *a scheduled task (T1053.005), a Windows service (T1543.003), a Run key (T1547.001)*. 1 mark: **one correct ID** that matches the example given.

---
---

# PART 5 — THE DEMONSTRATION: CASE WKS-164

### 2:00–3:30 · 90 minutes · open book · submitted to the candidate's folder · the brief is `Day_10_Practical_Assessment_Brief.docx`

## What the candidate receives (summary: the full text is in the brief)

| Part | Time guide | Critical aspects | The task |
|------|-----------|------------------|----------|
| **1 Check for alerts** | 15 min | 1.1.1–1.1.5 | Four inputs arrive (I1–I4). Record each as received, check for red flags, decide threat / detection / routine + severity + reason, and issue a ticket for each confirmed detection |
| **2 The tool, on your own machine** | 20 min | 1.2.1–1.2.3 · 1.3.1–1.3.4 | Check that Defender is installed and operational. Prove it can clean (EICAR). Verify the detection and the action with the three proofs. Check and update the signatures. Run a quick scan. Screenshots |
| **3 Follow-up on WKS-164** | 20 min | 1.4.1–1.4.3 | Read the scan-log extract and name the failure kinds. Write the verification confirmation to the user. Write a short escalation pack to the right authority |
| **4 Report the threat** | 35 min | 1.5.1–1.5.4 | Write the Critical notification. Fill the short threat report (hosts, path, ingress, egress, exploitation, installation, ATT&CK). **The notification call is made to the assessor in the oral breakout** |

## The case data (as the candidate sees it)

**Part 1: the four inputs, Monday 21 Sep 2026**

```
I1  09:02  Defender (AV) alert — WKS-152
           Event 1116  Trojan:Win32/Agent.QK!ml   file:_C:\Users\rcruz\Downloads\free_fonts.exe
           Event 1117  Action: Quarantine   Error Code: 0x00000000

I2  09:14  Phone call to the desk from L. Garcia, HR clerk, WKS-164:
           "The files on the HR share (drive H:) all have .crypt at the end and they won't open.
            There's a file called README_RESTORE.txt in every folder. It started about five past nine.
            I also opened my payslip from an email just before."

I3  08:43  Perimeter firewall alert — 203.0.113.5 (public address of SRV-WEB-01)
           BLOCKED  214 inbound connection attempts, ports 1–1024, from 198.51.100.23, 08:40–08:43

I4  06:00  Windows Update — 9 workstations installed the monthly security update; restart pending
```

**Part 2: the candidate's own machine.** No data is given. They run the commands.

**Part 3: the WKS-164 scan-log extract**

```
09:05:31  Event 1116  Ransom:Win32/Filecoder.PX   file:_C:\Users\lgarcia\AppData\Roaming\PayslipViewer\upd.dll
09:05:32  Event 1118  Action: Quarantine   FAILED   Error: The file is in use by another process
09:18:00  (IT isolated WKS-164 — switch port disabled)
09:20:00  Event 1000  Full scan started (L2, remotely)
09:47:12  Event 1002  Scan stopped before completion   (Reason: user cancelled)
10:05:00  Event 1000  Full scan started
11:31:40  Event 1001  Full scan finished   (1 threat found: Ransom:Win32/Filecoder.PX)
11:32:00  Get-MpThreatDetection:  ActionSuccess False   ThreatStatusID 102
```

**Part 4: the WKS-164 evidence set.** Lab addresses: WKS-164 = `192.168.10.164` · WKS-170 = `.170` · WKS-171 = `.171` · SRV-FILE-01 = `.22`.

```
C01  08:51:10  Email gateway   DELIVERED  to: l.garcia   from: payroll@hr-portal-ph.example
                               subject: "Your September payslip"   attachment: Payslip_Sept.zip

C02  08:58:44  WKS-164  Security 4688   explorer.exe → cmd.exe /c rundll32.exe
                               %APPDATA%\PayslipViewer\upd.dll,Start     (started from Payslip_Sept.lnk)
                               User: l.garcia

C03  08:58:40  Firewall/proxy  ALLOW OUT  192.168.10.164:50122 -> 203.0.113.88:443
                               bytes_in=2,301,440   bytes_out=1,020

C04  08:59:02  WKS-164  Registry Run key created (found by L2 with Autoruns, 21 Sep)
                               HKCU\Software\Microsoft\Windows\CurrentVersion\Run
                               "PayslipViewer" = rundll32.exe %APPDATA%\PayslipViewer\upd.dll,Start

C05  09:00:15  Firewall/proxy  ALLOW OUT  192.168.10.164:50140 -> 198.51.100.140:443
     to 09:04  one session   bytes_out=251,658,240 (≈ 240 MB)   bytes_in=31,004

C06  09:05:10  SRV-FILE-01  Security 5145 × 3,412   Share: \\SRV-FILE-01\HR   Access: WriteData
     onward    Account: l.garcia   Source: 192.168.10.164     (files renamed to .crypt)

C07  09:05:31  WKS-164  Defender 1116 / 1118   (see Part 3)

C08  09:09:40  WKS-170  Security 4625 × 9   Failed logon   Account: l.garcia
     to 09:11  Logon type 3   Source: 192.168.10.164      (no 4624 follows)

C09  09:12:20  WKS-171  Security 4624   Logon type 3   Account: l.garcia   Source: 192.168.10.164
     09:12:31  WKS-171  Security 5145   Share: \\*\C$   Target: Users\Public\upd.dll   WriteData
     09:12:40  WKS-171  Defender 1116 Ransom:Win32/Filecoder.PX  →  1117 Quarantine  Error Code: 0x00000000

C10  SHA-256 of upd.dll on WKS-164 and on WKS-171: 7936E8F69DA3DC07...AAA1A220  (the same)

C11  Firewall/proxy: NO inbound connection from the internet to 192.168.10.164, 20–21 Sep

C12  SRV-WEB-01: the I3 port scan from 198.51.100.23 was blocked at the perimeter.
     No connection from 198.51.100.23 reached any inside host. Nothing links it to WKS-164.
```

**The stakeholders:** M. Aquino, **HR manager**, owns the HR share data · P. Dizon, the user of WKS-171 (Finance) · the IT file-server team, which owns SRV-FILE-01.

## The key

### Part 1: check for alerts

| Input | Received as | Red flag? | Decision | Severity | Reason | Ticket? |
|-------|------------|-----------|----------|----------|--------|---------|
| I1 | Detection alert: AV | No | **Detection** | **Medium** | Quarantined, error 0, so contained (to be verified). One file | **Yes**, a detection is confirmed |
| I2 | **Incident report, by phone** (record: caller, time, channel, words, read-back) | **Yes: ransomware** (mass rename to .crypt, ransom note in every folder) | **Threat** | **Critical** | Business data encrypted **now**, not contained, and the user opened an attachment | **Yes, first**, Critical, notify within 10 min |
| I3 | Detection alert: firewall | No | **Detection** | **Low** (accept Medium) | Blocked at the perimeter, so contained | Accept a ticket or a log entry. Either with a reason |
| I4 | Routine notice | No | **Routine** | **Low** | Normal patching | **No** ticket (or a note). A routine never becomes Critical |

**Competent:** I2 identified as the **ransomware red flag** and ticketed **first** as Critical. The phone report recorded with caller, time, channel and the words used. Every decision has a reason that names containment. I1 **ticketed**. **Not yet:** I2 treated as a detection; I1 called a threat "because it is a Trojan"; no ticket issued; decisions without reasons.

### Part 2: the tool, on the candidate's own machine

| Aspect | What the candidate must show | Competent |
|--------|------------------------------|-----------|
| **1.2.1** Installed | `Get-Service WinDefend` (Status Running) **or** `Get-MpComputerStatus` `AMServiceEnabled True` | Screenshot + "Installed: yes" |
| **1.2.2** Operational | `AntivirusEnabled True`, `RealTimeProtectionEnabled True`, signatures dated | Screenshot + "Operational: yes/no, because …" |
| **1.2.3** Can clean or delete | EICAR created and **quarantined or removed** | Protection history or a popup screenshot |
| **1.3.1** Detection checked per procedure | The **1116** for EICAR found in the Operational log (or `Get-MpThreatDetection`) and matched to the story: name, path, time | Name, path and time match |
| **1.3.2** Action checked per SOP | The three proofs: **1117** error 0 · `ActionSuccess True` · `Test-Path` False | All three, or two with the third explained |
| **1.3.3** Updates checked and patched | `AntivirusSignatureLastUpdated` / version read · `Update-MpSignature` **or** GUI *Check for updates* · read again | Before and after, or "already current" shown |
| **1.3.4** Scan used | `Start-MpScan -ScanType QuickScan` **or** GUI quick scan · **1000 / 1001** or `QuickScanEndTime` · **plus one sentence on WKS-164**: *isolated first; a full scan run remotely by L2; if it keeps failing, offline scan and then re-image; the L1 analyst does not run scans on the live ransomware host from their own seat* | Scan evidence + a sensible WKS-164 sentence |

> **If a managed machine blocks a command:** the GUI route is accepted for every row (Windows Security app). If Defender is replaced by another product on the candidate's machine, they show the same three questions in that product. **Record what they showed.** Do not fail a candidate for a locked-down machine.

### Part 3: follow-up on WKS-164

**(a) The failure kinds**

| Line | Kind |
|------|------|
| 09:05:32 **1118** | **Kind 1: action failed** (file in use) |
| 09:47:12 **1002** | **Kind 4: scan did not complete**. Re-run it, and find out who cancelled it |
| 11:32 `ActionSuccess False`, `ThreatStatusID 102` after the full scan | **Still kind 1**. The threat is present and not contained |

**(b) The verification confirmation to L. Garcia.** Subject: `<ticket> — WKS-164 — scan result: NOT CLEAN`. Found: ransomware in a file from the payslip email. Done: computer disconnected at 09:18; removal attempted and failed. Scan: full scan finished 11:31, 1 threat still present. Means: do not use or reconnect the computer, and do not open the payslip email again on any device. Next: escalated to <authority>, and a loan machine will be arranged. Ask: forward nothing, and tell the desk if you opened the attachment anywhere else. **Plain register.** L. Garcia is not technical. **Competent:** says **not clean** plainly, gives an ask, uses plain words. **Not yet:** softened, or full of event IDs.

**(c) The escalation pack (short form: fields 1, 3, 5, 6, 7, 9)**
- **To:** **Information security manager**: an uncontained threat that has spread to a share and a second workstation, and needs a security decision. **Copy:** IT department manager (keep it isolated, re-image WKS-164). **CISO** informed through the infosec manager within 10 minutes, because it is **Critical** (data encrypted and data left, C05).
- **Evidence:** 1118 at 09:05:32 · 1002 at 09:47 · the full scan finished 11:31 with 1 threat · `ThreatStatusID 102`.
- **Tried / failed by kind:** quarantine: kind 1 · first full scan: kind 4 · second full scan: completed, threat still present.
- **Status:** not contained · Critical · SLA 10 min from the I2 ticket.
- **Ask (verb + object + deadline):** e.g. *approve re-imaging WKS-164 and keeping it isolated, by 12:00* · *decide whether to take the HR share offline now*.
- **Competent:** the infosec manager as primary, **or** another authority with a reason naming what they own. A verb-ask with a deadline. Log lines in the evidence. **Not yet:** "please advise"; no evidence lines; the vendor as primary with no reason.

### Part 4: report the threat

**1.5.1 The notification.** To **M. Aquino, HR manager**, who owns the HR data. **Critical**, because HR files were encrypted on the share and about 240 MB left WKS-164 just before (C05). Known: since about 09:05, a malicious attachment on WKS-164 encrypted files on `\\SRV-FILE-01\HR`, and data was sent out before that. Done: WKS-164 isolated at 09:18, and it has been escalated. **Do / do not:** *tell the HR team not to open the payslip email, do not use drive H: until told, do not pay or contact anyone named in the README.* **Ask:** *who in HR received the same payslip email, by 11:00* (or: *which HR folders hold personal data*, which matters for what may have left). Next update: <time>. **P. Dizon (WKS-171) is not notified as Critical**: that detection was quarantined successfully (C09), so it is contained, Medium, and recorded. *Accept a courtesy note that is not called a Critical notification.*

**1.5.2 Spread and lateral movement**

| Host | Role | Involvement | Line |
|------|------|-------------|------|
| WKS-164 | HR workstation | **Origin** | C02–C05, C07 |
| SRV-FILE-01 (HR share) | File server | **Confirmed impact**: files encrypted over the share. The malware did not run *on* the server | C06 |
| WKS-171 | Finance workstation | **Confirmed, then contained**: the file was copied in, detected and quarantined | C09, C10 |
| WKS-170 | Workstation | **Attempted**: 9 failed logons, no success | C08 |
| SRV-WEB-01 | Web server | **Not linked**: the blocked port scan from outside, with no line joining it | C12 |

**Path:** WKS-164 → WKS-171 over **SMB to the C$ admin share** with the **user's own account l.garcia**, at **09:12** (C09). **Also:** WKS-164 → `\\SRV-FILE-01\HR`, writing encrypted files over SMB from 09:05 (C06). *Accept the share as "spread of impact" rather than lateral movement, if it is explained.*

**1.5.3 Ingress and egress**

| | What | Line |
|---|------|------|
| **Ingress** | The email with `Payslip_Sept.zip` (C01) · **2.3 MB** `upd.dll` pulled in from `203.0.113.88:443` on an outbound connection (C03) · **no inbound** from the internet (C11) | C01, C03, C11 |
| **Egress** | **≈ 240 MB** out to `198.51.100.140:443` in one session, 09:00–09:04, **before** the encryption. Data left, which is the double-extortion pattern | C05 |

**1.5.4 Exploitation and installation, with ATT&CK**

| Behaviour | Tactic | Technique | Line |
|-----------|--------|-----------|------|
| Payslip email with an attachment | Initial Access | **T1566.001** Phishing: Spearphishing Attachment | C01 |
| The user opened the shortcut in the ZIP (**exploitation**: a user tricked, not a software exploit) | Execution | **T1204.002** User Execution: Malicious File | C02 |
| `rundll32.exe` used to run the DLL | Defense Evasion | **T1218.011** System Binary Proxy Execution: Rundll32 | C02 |
| The DLL pulled in from outside | Command and Control | **T1105** Ingress Tool Transfer | C03 |
| **Run key** starts it at every logon (**installation**) | Persistence | **T1547.001** Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | C04 |
| 240 MB sent out over HTTPS | Exfiltration | **T1048.002** Exfiltration Over Asymmetric Encrypted Non-C2 Protocol *(accept T1041 or T1567 with a reason)* | C05 |
| Files encrypted on the share | Impact | **T1486** Data Encrypted for Impact | C06 |
| Logon to WKS-171 with the user's real account, over the admin share | Lateral Movement | **T1021.002** SMB/Windows Admin Shares (+ **T1078** Valid Accounts) | C09 |
| The DLL copied to WKS-171 | Lateral Movement | **T1570** Lateral Tool Transfer | C09 |

**Competent on 1.5.4:** exploitation **and** installation both named in plain words, with **at least four** correct technique IDs that each point to a line. **Not yet:** only IDs with no lines; the Run key missing; "exploit" asserted with no evidence of a software vulnerability.

## The observation checklist (fill in during 2:00–3:50)

One sheet per candidate. Tick **S** (satisfactory: evidence seen or heard) or **NS** (not shown). Write a note for every NS.

| Aspect | What to look for | Source | S / NS | Note |
|--------|------------------|--------|--------|------|
| 1.1.1 | I1 / I3 recorded as detection alerts | Part 1 | | |
| 1.1.2 | I2 recorded as an incident report: caller, time, channel, words | Part 1 | | |
| 1.1.3 | Ransomware red flag named on I2 | Part 1 | | |
| 1.1.4 | Threat / detection / routine + severity + reason, for all four | Part 1 | | |
| 1.1.5 | Tickets issued for the confirmed detections, I2 first | Part 1 | | |
| 1.2.1 | Installed, shown | Part 2 | | |
| 1.2.2 | Operational, shown and stated | Part 2 | | |
| 1.2.3 | Can clean or delete: EICAR action shown | Part 2 | | |
| 1.3.1 | Detection checked: 1116 matched to the story | Part 2 | | |
| 1.3.2 | Action checked: three proofs | Part 2 | | |
| 1.3.3 | Updates checked and updated | Part 2 | | |
| 1.3.4 | Scan run, plus the WKS-164 sentence | Part 2 | | |
| 1.4.1 | Verification confirmation: NOT CLEAN, plain, with an ask | Part 3 | | |
| 1.4.2 | Failure kinds named: 1 and 4 | Part 3 | | |
| 1.4.3 | Escalation to an appropriate authority, with a reason, evidence, ask and deadline | Part 3 | | |
| 1.5.1 | Critical notification: **the call in the oral breakout** + the written version | Part 4 + oral | | |
| 1.5.2 | Hosts by involvement + the path | Part 4 | | |
| 1.5.3 | Ingress and egress separated, with bytes | Part 4 | | |
| 1.5.4 | Exploitation + installation + ≥ 4 IDs on lines | Part 4 | | |

---
---

# PART 6 — ORAL QUESTIONING

### In the breakout, about 6 minutes per candidate: **(1) the notification call, (2) three questions from the bank, (3) two portfolio questions (Part 7).**

## Step 1: the notification call (about 2 minutes) · critical aspect 1.5.1

> *You play M. Aquino, HR manager. Say:* "Hello, HR, this is Aquino." *Then let the candidate lead.*

Listen for the seven lines: **ticket ID · "Critical" + what system · what is known and since when · what has been done · do / do not · one ask · next update + read-back**. If they are silent, ask once: "Is there anything my team should do?" **Competent:** severity stated, a specific do / do not, an ask, a next update. **No blaming L. Garcia.**

## Step 2: three questions from the bank

Choose one question from **each of three different rows**. Choose to **fill gaps**: if the candidate's Part 2 was thin, ask from row B. Record the answer in a few words.

| Row | Question | What a competent answer contains |
|-----|----------|----------------------------------|
| **A · Alerts (E1)** | A1. Name three sources of detection alerts and one blind spot of one of them. | Any three from AV, firewall, WAF, SIEM, DLP, EDR, NDR, plus a real blind spot (e.g. *AV does not see network traffic*) |
| | A2. Why is a failed quarantine a threat and a successful block a detection, even if the blocked attack was bigger? | **Containment, not severity** |
| | A3. What are the two red flags the SOP names, and one sign of each? | Ransomware (mass rename, ransom note) · PE infection / virus (changed executables, many exes modified) |
| **B · The tool (E2–E3)** | B1. What is the difference between "installed" and "operational"? | Present on the machine versus actually protecting (service running, real-time on, signatures current) |
| | B2. The popup says "quarantined". Why is that not enough? | It is the story. The evidence is the log: the 1117, `ActionSuccess`, the file gone |
| | B3. When would you choose an offline scan instead of a full scan? | A threat that hides while Windows runs, or keeps coming back. It restarts the machine, so it is planned |
| | B4. Why check signature age before trusting a clean scan? | Old signatures miss recent threats, so a clean result means less |
| **C · Follow-up (E4)** | C1. Which two kinds of failed action never contain the word "failed"? | No action taken (1116 then silence) · scan did not complete (1002) |
| | C2. A business file was quarantined, and the user says it is safe. What do you do? | A vendor false-positive case, the infosec manager copied. **Do not restore it yourself** |
| | C3. What makes an escalation pack more than an opinion? | The evidence (log lines), an ask, a deadline, and a logged trail |
| **D · Reporting (E5)** | D1. Why did you not notify P. Dizon as Critical? | WKS-171's detection was contained (1117 success), so it is Medium. Only High and Critical are notified |
| | D2. How do you tell egress from ingress in a firewall line? | Who started it (OUT versus IN) plus bytes in and out. What crossed in which direction |
| | D3. What is the difference between a tactic and a technique in ATT&CK? | Goal (why) versus method (how), column versus box, and the ID is the technique's |
| | D4. Why is SRV-WEB-01 not in the path? | No line joins it. The port scan was blocked outside. Link with evidence, not the clock |
| **E · Underpinning (1.1–1.4, 1.11)** | E1. What is port forwarding, and why does a reviewer care? | It maps a public port to an inside host, which is how inside services get exposed |
| | E2. What does a web server's status 302 after many POSTs to a login page usually mean? | A successful login after guessing (Day 5) |
| | E3. What does a script do for an analyst that reading by eye cannot? | It counts and filters at scale, so you can judge (Day 5) |
| | E4. Name one Windows, one macOS or Linux, and one network command you would use to see what a machine is talking to. | e.g. `Get-NetTCPConnection` / `netstat -ano` · `lsof -i` or `ss -tunap` · `arp -a` / `ipconfig` |

**Competent:** each answer contains the core idea in the right-hand column, in the candidate's own words. One weak answer can be followed up once ("Can you say more about…?").

---
---

# PART 7 — PORTFOLIO WITH INTERVIEW

## The portfolio map: what should be in `Evidence/Day_03` and `Day_05` to `Day_10`

| Critical aspect | Portfolio evidence (day · item) |
|-----------------|---------------------------------|
| 1.1.1 Detection alert received | Day 6 · detection record (Task 2) · event log worksheet (Task 3) |
| 1.1.2 Incident report received | Day 6 · 6 intake forms across ≥ 4 channels (Task 1) |
| 1.1.3 Red flag checked | Day 6 · 2 indicator cards: ransomware and PE infection (Task 5) |
| 1.1.4 Assessed on criteria | Day 3 · relay decisions · Day 7 · 8 triage decisions (Task 1) |
| 1.1.5 Ticket issued | Day 3 · first ticket · Day 7 · register with 8 rows + 2 full tickets (Task 2) |
| 1.2.1–1.2.2 Installed / operational | Day 7 · solution-status report on own machine (Task 3) |
| 1.2.3 Can clean or delete | Day 7 · prove-it-cleans record (Task 4) |
| 1.3.1–1.3.2 Detection and action checked | Day 8 · 5 verification worksheets + own EICAR worksheet (Tasks 1–2) |
| 1.3.3 Updates checked and patched | Day 8 · patch-state report (Task 3) |
| 1.3.4 Scan used | Day 8 · scan logs for 3 types + offline plan (Task 4) |
| 1.4.1 Verified to client | Day 9 · 2 verification records (Task 1) |
| 1.4.2 Failed action checked | Day 9 · annotated extract + own-machine pass (Task 2) |
| 1.4.3 Escalated | Day 9 · 3 escalation packs + 3 register rows (Tasks 3–4) |
| 1.5.1 Notified | Day 10 · N2 notification (Activity 1) |
| 1.5.2–1.5.4 Reported | Day 10 · threat report + Navigator layer (Activities 2–4) |
| Underpinning 1.1–1.4 | Day 5 · workstation baseline, log parser run, network map |

**Check before the interview:** open the candidate's folders and note **two** items to ask about. Choose one strong item and one thin or unusual one.

## The interview questions (choose two per candidate)

| # | Question | What you are checking |
|---|----------|----------------------|
| P1 | "Walk me through this ticket from Day 7. Why that severity?" | They wrote it, and the reason is theirs |
| P2 | "In your Day 8 worksheet, which of the three proofs was hardest to get on your machine, and why?" | They did it on their own machine |
| P3 | "This Day 9 pack goes to <authority>. What would you change now?" | Reflection, and ownership |
| P4 | "Show me where this morning's report proves WKS-311 and SRV-BAK-02 are linked." | That they understand E16 and E07–E10 |
| P5 | "Something is missing from Day <N>. What happened, and can you show it another way?" | Honest gaps. Offer another way to show it, or record the aspect as a gap |

**Competent:** answers are consistent with the evidence and the candidate can explain their own work. **If a candidate cannot explain an item at all**, note it. That item is **not counted** as evidence for its aspect.

---
---

# PART 8 — THE RESULT SHEET AND THE REASSESSMENT RULE

## Result sheet (one row per candidate)

| Candidate | Written (/40) | Demo: aspects NS | Oral | Portfolio | **Unit result** | Aspects to reassess | Feedback given (Day 11) |
|-----------|---------------|------------------|------|-----------|-----------------|---------------------|-------------------------|
| | | | S / NS | S / NS | C / NYC | | ☐ |
| | | | S / NS | S / NS | C / NYC | | ☐ |
| | | | S / NS | S / NS | C / NYC | | ☐ |
| | | | S / NS | S / NS | C / NYC | | ☐ |
| | | | S / NS | S / NS | C / NYC | | ☐ |

## Reassessment rule

- **Only the aspect that was not shown is reassessed**, using a **different** case (the assessor writes a short parallel case, for example a WKS-311-style beacon for 1.5.3).
- It is arranged **before Day 15**, live, observed. Day 11 or Day 12 at 1:00 PM works well, when the rest of the class is on asynchronous work.
- The **written exam** re-sit uses a parallel paper: same topics, different items. Keep the same 28 / 40 pass mark.
- Record the reassessment date, the case used, and the outcome on the result sheet.

## Feedback at the start of Day 11 (individual, 2–3 min each, during the async afternoon or by chat)

Say **one thing done well**, then **the result**, then **what happens next**. For NYC, name the aspect and the date of the reassessment. **Never** share results in front of the class.

---
---

# PART 9 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| **More than 16 candidates** and one assessor | Orals for the first 16 today. The rest at **Day 11, 1:00 PM**, live, in breakouts, while the class is on async work |
| A candidate's connection fails for more than 15 min | Their demonstration moves to Day 11 at 1:00 PM on the **same** case. Keep their brief closed until then |
| The whole session is lost (power, platform) | Written exam at Day 11, 1:00. Demonstration and orals Day 12, 1:00. **Never as self-study** |
| A candidate's machine cannot run Defender commands (managed / locked) | The GUI route for Part 2. If no Defender at all, they show the same aspects in the product they have, or on the trainer's shared screen *with the candidate driving* |
| EICAR blocked before saving (managed machines) | **The block is the detection.** They record Protection history. Same as Day 6 |
| ATT&CK site down during Part 4 | Candidates write the tactic and technique **names** without IDs. Accept, and ask one ID question in the oral |
| A candidate uses AI or chat during the demonstration | Stop, note it, and continue the orals. The demonstration is **void** and redone on a parallel case |
| A candidate is visibly distressed | Pause their clock. Offer five minutes. Assessment is not an endurance test |
