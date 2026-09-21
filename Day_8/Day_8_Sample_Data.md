# DAY 8 — SAMPLE DATA
## The five verification cases, the patch-state scenarios, the scan scenarios, and the worksheet
### Trainer, and trainees where marked.

> **Safety note.** No live malware, no client data. EICAR is the only "threat" that ever touches a real machine, and it is a harmless test string. Every other case below is **on paper** — log lines written to look like the real thing. Addresses use documentation-only ranges (`203.0.113.x`, `198.51.100.x`) and the Day 3 Tor node `185.220.101.1`. Hostnames, users and threat names are invented.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The five verification cases | Activity 1, PM Task 1 |
| 2 · The Defender event IDs you will read | Demos 1–2, Handout |
| 3 · The patch-state scenarios | Topic 8.3, PM Task 3 |
| 4 · The "which scan?" scenarios | Activity 4, PM Task 5 |
| 5 · The verification worksheet template | Demo 5, Activity 1, PM Tasks 1–2 |
| 6 · The commands trainees run | Demos 1–4, Activities 2–3, PM Tasks 2–4 |

---
---

# 1 — THE FIVE VERIFICATION CASES
### Activity 1 (teams find the match or the mismatch) and PM Task 1 (a full worksheet per case). Answers in `Day_8_Solutions.docx`.

Each case has two halves. **The story** is what the tool's friendly view — or the ticket written from it — says happened. **The evidence** is the raw Defender Operational log, as the trainee would see it in Event Viewer or with `Get-WinEvent`. The trainee's job is to check whether the story matches the evidence on four things: **time · threat name · file path · action**, and then decide whether the action is **proven**.

Every case uses the same date, **2026-09-16**, so times can be compared directly.

---

**Case 1 — The EICAR test on TRN-PC-07**

*The story (Protection history):*
```
Virus:DOS/EICAR_Test_File
Status: Removed          Date: 2026-09-16 10:47
Affected item: file: C:\Users\trainee\Documents\eicar_test.txt
Severity: Severe
```

*The evidence (Defender Operational log):*
```
10:47:02  Event 1116  Microsoft Defender Antivirus has detected malware or other potentially unwanted software.
                      Name: Virus:DOS/EICAR_Test_File   Severity: Severe
                      Path: file:_C:\Users\trainee\Documents\eicar_test.txt
10:47:03  Event 1117  Microsoft Defender Antivirus has taken action to protect this machine from malware or other potentially unwanted software.
                      Name: Virus:DOS/EICAR_Test_File   Action: Remove   Error Code: 0x00000000
```

---

**Case 2 — The Trojan in Downloads on WKS-118**

*The story (the ticket written by the night analyst at 14:20):*
```
CTM-0007-014  WKS-118 — Trojan:Win32/Wacatac.B!ml quarantined
Detected 14:05 in C:\Users\mlopez\Downloads\setup_crack.exe.
Decision: Detection — quarantined, contained.  Severity: Medium.  Status: Closed.
```

*The evidence (Defender Operational log):*
```
14:05:11  Event 1116  Microsoft Defender Antivirus has detected malware or other potentially unwanted software.
                      Name: Trojan:Win32/Wacatac.B!ml   Severity: Severe
                      Path: file:_C:\Users\mlopez\Downloads\setup_crack.exe
14:05:12  Event 1118  Microsoft Defender Antivirus has attempted to perform an action to protect this machine from malware or other potentially unwanted software, but the action failed.
                      Name: Trojan:Win32/Wacatac.B!ml   Action: Quarantine
                      Error Description: The file is in use by another process.
14:06:40  Event 1116  Microsoft Defender Antivirus has detected malware or other potentially unwanted software.
                      Name: Trojan:Win32/Wacatac.B!ml   Severity: Severe
                      Path: file:_C:\Users\mlopez\Downloads\setup_crack.exe
```

---

**Case 3 — The ad toolbar on TRN-PC-03**

*The story (Protection history):*
```
PUA:Win32/Adload
Status: Blocked          Date: 2026-09-16 09:31
Affected item: file: C:\Users\trainee\Downloads\free_pdf_setup.exe
Severity: Low
```

*The evidence (Defender Operational log):*
```
09:31:44  Event 1116  Microsoft Defender Antivirus has detected malware or other potentially unwanted software.
                      Name: PUA:Win32/Adload   Severity: Low
                      Path: file:_C:\Users\trainee\Downloads\free_pdf_setup.exe
09:31:45  Event 1117  Microsoft Defender Antivirus has taken action to protect this machine from malware or other potentially unwanted software.
                      Name: PUA:Win32/Adload   Action: Block   Error Code: 0x00000000
```

---

**Case 4 — Two files, one name, on SRV-FILE-01**

*The story (Protection history):*
```
Trojan:Win32/Emotet.A
Status: Quarantined      Date: 2026-09-16 03:12
Affected item: file: C:\Temp\inv0ice.doc.exe
Severity: Severe
```

*The evidence (Defender Operational log):*
```
03:12:07  Event 1116  ... detected malware ...
                      Name: Trojan:Win32/Emotet.A   Severity: Severe
                      Path: file:_C:\Temp\inv0ice.doc.exe
03:12:08  Event 1117  ... has taken action ...
                      Name: Trojan:Win32/Emotet.A   Action: Quarantine   Error Code: 0x00000000
03:15:52  Event 1116  ... detected malware ...
                      Name: Trojan:Win32/Emotet.A   Severity: Severe
                      Path: file:_C:\Users\Public\inv0ice.doc.exe
03:15:53  Event 1117  ... has taken action ...
                      Name: Trojan:Win32/Emotet.A   Action: Quarantine   Error Code: 0x00000000
```

---

**Case 5 — Found, but nothing done, on WKS-205**

*The story (Protection history):*
```
Trojan:Win32/Wacatac.B!ml
Status: Action needed — remediation incomplete     Date: 2026-09-16 08:02
Affected item: file: C:\Users\jreyes\AppData\Local\Temp\update_helper.exe
Severity: Severe
```

*The evidence (Defender Operational log):*
```
08:02:19  Event 1116  ... detected malware ...
                      Name: Trojan:Win32/Wacatac.B!ml   Severity: Severe
                      Path: file:_C:\Users\jreyes\AppData\Local\Temp\update_helper.exe
(no Event 1117 or 1118 follows — the log goes quiet)
```

*Also on the machine — `Get-MpThreatDetection`:*
```
InitialDetectionTime : 16/09/2026 08:02:19
ThreatID             : 2147735503
Resources            : {file:_C:\Users\jreyes\AppData\Local\Temp\update_helper.exe}
ActionSuccess        : False
ThreatStatusID       : 1
```

---
---

# 2 — THE DEFENDER EVENT IDs YOU WILL READ
### For Demos 1–2 and the Handout. The Operational log is at Event Viewer → Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational.

| Event ID | Plain meaning | You use it to |
|----------|---------------|---------------|
| **1116** | Malware **detected** | Confirm *what* was found, *where*, and *when* |
| **1117** | **Action taken** (quarantine / remove / clean / block) | **Prove** the action happened |
| **1118** | Action **failed** (non-critical) | Spot a failed action — Day 9 lives here |
| **1119** | Action **failed** (critical error) | Same — and it is worse |
| **1000 / 1001** | Scan **started** / scan **finished** | Prove a scan ran and how it ended |
| **1002** | Scan **stopped before completion** | A scan that did not finish is not a scan |
| **2000** | Signatures **updated** | Prove the update happened |
| **2001** | Signature update **failed** | A finding — the tool is falling behind |
| **2002** | Engine **updated** | Same, for the engine |
| **5001** | Real-time protection **disabled** | The Day 7 finding, in the log |

**`Get-MpThreatDetection` → `ThreatStatusID`** — the number that says what the tool did:

| ID | Meaning | Contained? |
|----|---------|-----------|
| 1 | Detected (nothing done yet) | **No** |
| 2 | Cleaned | Yes |
| 3 | Quarantined | Yes |
| 4 | Removed | Yes |
| 5 | Allowed (someone allowed it) | **No — and ask why** |
| 6 | Blocked | Yes |
| 102 | Quarantine **failed** | **No** |
| 103 | Remove **failed** | **No** |
| 104 | Clean **failed** | **No** |
| 106 | Abandoned | **No** |
| 107 | Block **failed** | **No** |

> The 100-series numbers are the ones Day 9 is built on. Today, trainees only need to see that **1 and anything over 100 means "not contained"**.

---
---

# 3 — THE PATCH-STATE SCENARIOS
### Topic 8.3 and PM Task 3. Trainees report their OWN machine; these three are for reading practice and the marking key.

The four things to read, and where:

| What | Field / command | "Good" looks like |
|------|-----------------|-------------------|
| Signature version and age | `AntivirusSignatureVersion`, `AntivirusSignatureAge` | Age 0–1 days |
| Engine version | `AMEngineVersion` | Updated within the month |
| Platform (product) version | `AMProductVersion` | Updated within the month |
| Operating-system patch state | `Get-HotFix` newest `InstalledOn`; Settings → Windows Update | A security update within the last month |

**Machine A**
```
AMProductVersion              : 4.18.25080.5
AMEngineVersion               : 1.1.25080.3
AntivirusSignatureVersion     : 1.437.512.0
AntivirusSignatureAge         : 0
Get-HotFix (newest)           : KB5063xxx  Security Update  2026-09-10
```
*(Signatures today, engine and platform this month, OS patched this month → healthy. Nothing to report.)*

**Machine B**
```
AMProductVersion              : 4.18.25050.2
AMEngineVersion               : 1.1.25050.1
AntivirusSignatureVersion     : 1.431.208.0
AntivirusSignatureAge         : 23
Operational log               : Event 2001 — signature update failed (x 9, daily since 2026-08-24)
```
*(Signatures 23 days old, engine and platform three months old, and the log shows the update has been failing daily → a finding. Try the update; if it still fails, report it — the tool is falling behind and will miss new threats.)*

**Machine C**
```
AMProductVersion              : 4.18.25080.5
AMEngineVersion               : 1.1.25080.3
AntivirusSignatureVersion     : 1.437.512.0
AntivirusSignatureAge         : 0
Get-HotFix (newest)           : KB5058xxx  Security Update  2026-05-14
```
*(The antivirus is perfect, but the operating system has had no security update for four months → a finding. The AV cannot protect an unpatched OS from everything. Report to IT; an L1 analyst does not install OS patches on a server without a change window.)*

---
---

# 4 — THE "WHICH SCAN?" SCENARIOS
### Activity 4 (teams) and PM Task 5. For each, the trainee names the scan type and the reason.

The four scan types, in one line each:

| Scan | What it looks at | How long | When it is the right call |
|------|------------------|----------|---------------------------|
| **Quick** | The places malware usually hides — memory, startup, system folders | Minutes | Routine; daily; "just check" |
| **Full** | Every file on every drive | Hours | You suspect something and don't know where; protection was off; before handing a machine back |
| **Custom** | One folder, file or drive you choose | Seconds to minutes | You know exactly where — a download, a USB drive, one folder |
| **Offline** | The whole system, from outside Windows (the machine restarts into a small scanner) | 15–20 min, with a restart | Malware that comes back after removal, or hides from Windows — something that loads before Windows does |

**The scenarios**

1. Start of shift. Your own machine. Nothing suspicious. You want to "just check".
2. A user brings a USB drive from home and wants it checked before opening anything on it.
3. On Day 7 you found a machine whose real-time protection had been off for nine days.
4. A machine had a Trojan quarantined — but the same Trojan comes back after every restart.
5. A user downloaded an installer that looks suspicious. They have not run it. It is in their Downloads folder.
6. A server showed unusual outbound connections last night. A quick scan found nothing.
7. You have cleaned a laptop and are about to hand it back to the client.

---
---

# 5 — THE VERIFICATION WORKSHEET TEMPLATE
### Demo 5 walks one through. Activity 1 fills the first three rows per case; PM Task 1 fills all eight for all five cases; PM Task 2 fills it for your own EICAR.

| # | Field | Your entry |
|---|-------|------------|
| — | Case / ticket ID | |
| 1 | **What the story says** — threat name · file path · time · action (from Protection history, the popup, or the ticket) | |
| 2 | **What the evidence says** — the same four things, from the raw log (events 1116 / 1117 / 1118) | |
| 3 | **Do they match?** — time ✓/✗ · name ✓/✗ · path ✓/✗ · action ✓/✗ — name every mismatch | |
| 4 | **Is the action proven?** — event 1117 present? · `ActionSuccess` True? · file gone from disk (`Test-Path` = False)? | |
| 5 | **Outcome** — contained / not contained | |
| 6 | **Is the tool up to date?** — signature age · engine · platform · OS patch | |
| 7 | **Scan** — type chosen · why · result (threats found / none) | |
| 8 | **Verdict** — verified detection · failed action (→ threat, escalate) · more than the story (→ follow up) · not yet acted on (→ act now) | |

> Rows 1–5 are **PC 3.1 and 3.2**. Row 6 is **PC 3.3**. Row 7 is **PC 3.4**. Row 8 is the analyst's judgement — and the reason matters more than the answer.

---
---

# 6 — THE COMMANDS TRAINEES RUN
### None of these needs the internet. Marked **(admin?)** where a locked-down machine may say "access denied" — the GUI fallback is given.

**Read the story (Topic 8.1)**
```powershell
Get-MpThreat | Select-Object ThreatName, ThreatID, SeverityID, IsActive
Get-MpThreatDetection | Select-Object InitialDetectionTime, ThreatID, Resources, ActionSuccess, ThreatStatusID
```
*GUI: Windows Security → Virus & threat protection → Protection history.*

**Read the evidence (Topic 8.1)**
```powershell
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 60 |
  Where-Object { $_.Id -in 1116, 1117, 1118, 1119 } |
  Select-Object TimeCreated, Id, Message | Format-List
```
*GUI: Event Viewer → Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational. Filter Current Log → Event IDs `1116,1117,1118,1119`.*

**Prove the action (Topic 8.2)**
```powershell
Test-Path "$env:USERPROFILE\Documents\eicar_test.txt"      # False = the file is gone
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Restore -ListAll   # what is in quarantine (list only)
```

**Check versions and update (Topic 8.3)**
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AntivirusSignatureVersion, AntivirusSignatureLastUpdated, AntivirusSignatureAge
Update-MpSignature                                            # (admin?) GUI: Windows Security → Virus & threat protection → Protection updates → Check for updates
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5 HotFixID, Description, InstalledOn
```
*GUI for the OS: Settings → Windows Update.*

**Scan (Topic 8.4)**
```powershell
Start-MpScan -ScanType QuickScan                              # (admin?) GUI: Windows Security → Scan options → Quick scan
Start-MpScan -ScanType CustomScan -ScanPath "$env:USERPROFILE\Documents\ScanTest"
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Scan -ScanType 3 -File "$env:USERPROFILE\Documents\ScanTest"   # custom scan, prints the result in the window
Start-MpScan -ScanType FullScan                               # long — start it and let it run
```
*`MpCmdRun` writes its own log to `%TEMP%\MpCmdRun.log`. Scan start/finish also appear as events **1000 / 1001** in the Operational log.*

> **OFFLINE SCAN — never run it in class.** `Start-MpWDOScan` (or Windows Security → Scan options → Microsoft Defender Offline scan) **restarts the machine immediately** and takes 15–20 minutes. Show where the button is; explain when it is the right call; leave it for the afternoon, and only for trainees who have saved their work and can afford the restart.
