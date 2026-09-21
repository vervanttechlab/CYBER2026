# DAY 8 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 8 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_8_Instructor_Guide.md` | Trainer only | — |
| `Day_8_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_8_Demonstration_Guide.md` | Trainer only | — |
| `Day_8_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_8_Sample_Data.md` | Trainer — the 5 cases, event IDs, patch and scan scenarios, the worksheet | — |
| `Day_8_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_8_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_8_Resources.md` | Trainer, and the trainee section | — |
| `Day08_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> Handout, Activity Pack and Solutions are **Word documents (.docx)**, not markdown, on request.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** | Activities 1 and 4 |
| **Recording** on | Activity 3 is observed |
| **Chat**, visible | Quick answers; the fallback for Activity 4 if behind |
| A way to paste the **five cases** to each team | Activity 1 |

## On the trainer's machine — built into Windows
| Item | Why |
|------|-----|
| **PowerShell** (a normal window; admin only if a command asks) | Demos 1–4 |
| **Event Viewer** | Demo 1 fallback (the Operational log) |
| **Windows Security app** | Protection history; Protection updates; Scan options (Demos 1, 3, 4) |
| Your **Day 6 EICAR detection** still in the log | Demos 1, 2, 5 — recreate it the night before if it is gone |
| The folder **`Documents\ScanTest`** with one harmless `.txt` | Demo 4 |
| **Fallback screenshots** | Part 3 |

> **No live Wazuh server needed. No Windows Sandbox needed.** Both are previewed from screenshots in Demo 5.

## Printed or on paper
- `Day_8_Presenter_Script.md`
- The **Activity 3 observation sheet** (Part 5)
- The **five cases** (Sample Data §1) and the **seven scan scenarios** (§4)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows machine with Defender on** | Every check today |
| Their **Day 6 EICAR detection** still in Protection history / the log | Activity 2, PM Task 2 — *if it is gone, the Day 6 steps recreate it in two minutes* |
| **Camera and microphone** | Activity 3 is observed |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| Their **Day 3 class QA checklist** | Self-checking a worksheet (Task 6) |
| A **screenshot tool** (Win + Shift + S) | Three proof screenshots in Activity 2 |
| A folder `Evidence/Day_08/` | Everything goes here |

> Tell them plainly in the joining note: **do not run the "Microsoft Defender Offline scan" during the session** — it restarts the machine.

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] Protection history showing the EICAR entry (the story)
- [ ] `Get-WinEvent` output showing a 1116 and a 1117 (the evidence)
- [ ] Event Viewer → Windows Defender → Operational, filtered to 1116–1119
- [ ] `Get-MpThreatDetection` output with `ActionSuccess : True` and `ThreatStatusID : 3` or `4`
- [ ] `Test-Path` returning `False`
- [ ] `Get-MpComputerStatus` four-layer output — **before** and **after** `Update-MpSignature`
- [ ] Windows Security → Protection updates page
- [ ] `Get-HotFix` top five
- [ ] `MpCmdRun -Scan -ScanType 3` result: "found no threats"
- [ ] Windows Security → Scan options page, **with the Offline scan button circled in red** ("never in class")
- [ ] A completed verification worksheet (your EICAR, all 8 rows)
- [ ] **Windows Sandbox** — one screenshot of a Sandbox window (preview only)
- [ ] **Wazuh** — one screenshot of an alert search showing Defender events from an agent (preview only)

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 7. Announce at 8:00.

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Match the Story" | 8:35–8:55 | Teams |
| Activity 2 "Prove Your Action" | 9:10–9:30 | Individually, pairs for help |
| Activity 3 "Update, Then Scan" | 10:30–11:00 | Individually (observed) |
| Activity 4 "Which Scan Would You Run?" | 11:15–11:35 | Teams |

---
---

# PART 5 — ACTIVITY 3 OBSERVATION SHEET
### Open at 10:30. One row per trainee.

| Trainee | Signature version read BEFORE and AFTER the update, both recorded? | Custom scan chosen for `ScanTest`, run, and the result explained (incl. "nothing found" = expected)? | Note |
|---------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both. This is E3 PC 3.3 and PC 3.4, observed. A trainee whose update fails (no internet, event 2001) and who *reports* it as a finding is competent on the first box.

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | 5 verification worksheets (the paper cases) | ☐ |
| 2 | Own-EICAR worksheet + 3 screenshots (1117 · `ActionSuccess` · `Test-Path`) | ☐ |
| 3 | Patch-state report (before / after / engine / platform / OS) | ☐ |
| 4 | Scan logs — quick, custom, full; offline plan (offline log only if run after class) | ☐ |
| 5 | 7 "which scan?" answers with reasons | ☐ |
| 6 | 1 worksheet self-check | ☐ |
| 7 | Reflection | ☐ |

## Still outstanding — keep chasing
| Item | From | Why open |
|------|------|----------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 1 | First on-site day |
| Lab-subnet Nmap sweep | Day 5 | Needs lab + authorisation |
| **Windows Sandbox / Atomic Red Team** | Day 8 | Previewed only — needs Pro edition and RAM the room does not have |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall | — |
| 8:15 | **8.1 + Demo 1 (story vs log)** | **Never cut** |
| 8:35 | Activity 1 | Three cases (1, 2, 5) |
| 8:55 | **8.2 + Demo 2 (three proofs)** | **Never cut** |
| 9:10 | Activity 2 | Proof 3 only, live; rest → PM Task 2 |
| 9:30 | 8.3 + Demo 3 | Skip `Get-HotFix`; say the OS line |
| 10:00 | Break | — |
| 10:10 | 8.4 + Demo 4 | Skip the quick scan; keep the custom scan and the offline warning |
| 10:30 | **Activity 3 (observed)** | **Never cut** |
| 11:00 | 8.5 + Demo 5 | Rows + verdict table only; skip preview |
| 11:15 | Activity 4 | Three scenarios in chat |
| 11:35 | Brief & close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| No EICAR events in the log | Recreate EICAR (Day 6 Demo 3) — two minutes |
| `Get-WinEvent` access denied | Event Viewer GUI on the same log; else Protection history + `Get-MpThreatDetection` |
| Third-party AV, not Defender | Its own history and log answer the same four questions; pair for the commands |
| `Update-MpSignature` / `Start-MpScan` need admin | Windows Security GUI — same evidence |
| No internet | Update fails → event 2001 → a finding to show and report |
| `Test-Path` returns True on a trainee's machine | The file is still there — a real finding; have them report it |
| Custom scan finds nothing | Expected — say it *before* the scan |
| Someone runs the offline scan | They drop for ~20 min; note it for Task 4; remind the room |
| Behind at 11:00 | 8.5 to the rows + verdict table; Activity 4 in chat |

---
---

# PART 9 — LINKS FOR TRAINEES
- The Defender Operational log — Event Viewer → Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational
- Event IDs that matter today — 1116 detected · 1117 action taken · 1118/1119 action failed · 1000/1001/1002 scan started/finished/stopped · 2000/2001 signatures updated/failed — table in your handout
- `Get-MpThreatDetection` status numbers — table in your handout
- The four scans and when to use each — table in your handout
- Offline scan — **only after class, with your work saved; it restarts your machine**
- Windows Sandbox and Wazuh — preview only today; you will meet them once the lab and the server are ready
