# DAY 7 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 7 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_7_Instructor_Guide.md` | Trainer only | — |
| `Day_7_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_7_Demonstration_Guide.md` | Trainer only | — |
| `Day_7_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_7_Sample_Data.md` | Trainer — the 8 alerts, register, status scenarios | — |
| `Day_7_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_7_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_7_Resources.md` | Trainer, and the trainee section | — |
| `Day07_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> Handout, Activity Pack and Solutions are **Word documents (.docx)**, not markdown, on request.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** | Activities 1, 2, 3, 4 |
| **Recording** on | Activity 2 is observed |
| A **shared spreadsheet** everyone can see | The ticket register — Demo 1, Activity 2 |
| **Chat**, visible | Quick answers |

## On the trainer's machine — built into Windows
| Item | Why |
|------|-----|
| **PowerShell** | `Get-Service WinDefend`, `Get-MpComputerStatus` |
| **Windows Security app** | Demos 2, 4, 5 (local console) |
| **A spreadsheet tool** (LibreOffice Calc / Excel) | The ticket register |
| The **Wazuh preview screenshot** | Demo 5 — see Part 3 |
| **Fallback screenshots** | Part 3 |

> **No live Wazuh server needed.** The console is previewed from a screenshot; everything else is local.

## Printed or on paper
- `Day_7_Presenter_Script.md`
- The **Activity 2 observation sheet** (Part 5)
- The **8 alerts** (Sample Data §1)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows machine with Defender on** | The status checks, the EICAR action |
| **Camera and microphone** | Activity 2 is observed |
| A **spreadsheet tool** (LibreOffice Calc / Excel / Sheets) | Their ticket register |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| Their **Day 3 class QA checklist** | Self-checking tickets (Task 5) |
| Their **Day 6 EICAR detection** in Protection history | Reused for Task 4 |
| A folder `Evidence/Day_07/` | Everything goes here |

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] `Get-MpComputerStatus` output on a healthy machine
- [ ] `Get-MpComputerStatus` with RealTimeProtectionEnabled **False** (a finding)
- [ ] Windows Security app with green ticks
- [ ] Protection history showing the EICAR action (Quarantined/Removed)
- [ ] A completed ticket-register row
- [ ] **A Wazuh dashboard screenshot** (agent list: connected/disconnected) — the only "server" image, used as a preview

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 6. Announce at 8:00.

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Threat, Detection, or Routine?" | 8:35–8:55 | Teams |
| Activity 2 "Write the Ticket" | 9:15–9:45 | Individually (observed) |
| Activity 3 "Is the Solution Working?" | 10:30–10:55 | Individually, pairs for help |
| Activity 4 "Read the Console" | 11:25–11:38 | Teams |

---
---

# PART 5 — ACTIVITY 2 OBSERVATION SHEET
### Open at 9:15. One row per trainee.

| Trainee | Decision + a REASON present? | Two timestamps + a specific next-step ask? | Note |
|---------|------------------------------|--------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both. This is E1 PC 1.5, and `ICT315202` LO2 (quality of own work), observed.

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | 8 triage decisions (criteria + severity + reason) | ☐ |
| 2 | Ticket register — 8 rows + 2 full tickets | ☐ |
| 3 | Solution-status report | ☐ |
| 4 | Clean/quarantine record + action range | ☐ |
| 5 | 2 ticket self-checks | ☐ |
| 6 | Management-console worksheet | ☐ |
| 7 | Reflection | ☐ |

## Still outstanding — keep chasing
| Item | From | Why open |
|------|------|----------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 1 | First on-site day |
| Lab-subnet Nmap sweep | Day 5 | Needs lab + authorisation |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall | — |
| 8:15 | 7.1 decide | — |
| 8:35 | Activity 1 | Five alerts |
| 8:55 | 7.2 + Demo 1 | — |
| 9:15 | **Activity 2 (observed)** | **Never cut** |
| 9:45 | 7.3 p1 + Demo 2 | — |
| 10:00 | Break | — |
| 10:10 | **7.3 p2 + Demo 3 (status)** | **Never cut** |
| 10:30 | Activity 3 | — |
| 10:55 | 7.4 + Demo 4 | — |
| 11:10 | 7.5 + Demo 5 | Console idea + 1 screenshot |
| 11:25 | Activity 4 | Quick discussion |
| 11:38 | Brief & close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| Third-party AV, not Defender | Its own status page answers the same three questions |
| `Get-MpComputerStatus` errors | Windows Security app GUI |
| No spreadsheet | Any shared table with the same columns |
| Real-time protection off on a machine | That IS a finding — have the trainee report it |
| Behind at 11:10 | 7.5 to the console idea + one Wazuh screenshot |

---
---

# PART 9 — LINKS FOR TRAINEES
- Microsoft Defender status — `Get-MpComputerStatus` (PowerShell) or the Windows Security app
- The action range (Failed/Clean/Delete/Quarantine/Blocked/Re-image) — in your handout
- SLA (service-level agreement) — glossary in your handout
- Wazuh dashboard — the console you'll use once the server is built (preview only today)
