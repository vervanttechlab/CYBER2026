# DAY 05 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 05 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_05_Instructor_Guide.md` | Trainer only | — |
| `Day_05_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_05_Demonstration_Guide.md` | Trainer only | — |
| `Day_05_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_05_Activity_Solutions.docx` | **Trainer only** — the morning activity keys, one page per activity | Second screen, 8:30–11:35 |
| `Day_05_Sample_Data.md` | Trainer — the drill, the recipe, the cookbook, the Autoruns set, the baseline commands | — |
| `Day_05_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_05_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_05_Resources.md` | Trainer, and the trainee section | — |
| `Day05_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> Handout, Activity Pack and Solutions are **Word documents (.docx)**, not markdown, on request.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** | Activity 4 |
| **Recording** on | Activity 3 is observed |
| **Chat**, visible | Activity 1 is a chat drill; the Sysinternals link is pinned here |

## On the trainer's machine
| Item | Why |
|------|-----|
| **Event Viewer** | Demos 1–3 |
| **PowerShell** — a normal, non-admin window | Demos 0, 3, 5 — so you see what trainees see |
| **Sysinternals Suite**, unzipped to `C:\Tools\Sysinternals\`, EULAs accepted, **VirusTotal option off** | Demo 4, Demo 5 (`autorunsc64.exe`) |
| `C:\Evidence\Day_05\` from Day 04 (to be renamed `Day_04` in Demo 0) | Demo 0, Demo 5 compare |
| **LibreOffice Calc / Excel** | Opening the exported CSVs |
| **Fallback screenshots** | Part 3 |

> **No server, no admin.** Every demo today runs on a standard user account. If your account is an administrator, still open PowerShell *without* "Run as administrator".

## Printed or on paper
- `Day_05_Presenter_Script.md`
- The **Activity 3 observation sheet** (Part 5)
- The **ten drill events** (Sample Data §2) and the **eight Autoruns entries** (§5)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows 10/11 machine** — standard account is fine | Every demo |
| Their **Day 04 evidence folder** `C:\Evidence\Day_05\` with the four `baseline_*.csv` | Renamed at 8:00; compared in Demo 5 |
| The **Sysinternals Suite** downloaded and unzipped — link in Part 9 (~50 MB) | Demo 4, Demo 5 — *if it cannot be run, every step has a PowerShell fallback* |
| **Camera and microphone** | Activity 3 is observed |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| Their **Day 03 evidence register and class QA checklist** | PM Task 6 |
| **LibreOffice Calc / Excel / Sheets** | Opening CSVs |

> Tell them in the joining note: **do not tick "Check VirusTotal.com"** in Autoruns or Process Explorer. We will say why in class.

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] Event Viewer tree with the five channels highlighted
- [ ] Security log showing "access denied" on a standard account
- [ ] Create Custom View dialog filled in (Defender, five IDs)
- [ ] The XML tab of that view
- [ ] Export Custom View dialog and the resulting `.xml` in the folder
- [ ] `Get-WinEvent` cookbook #3 output, and the red "No events were found" for #7
- [ ] `q3_new_services.csv` open in Calc
- [ ] Process Explorer with the Verified Signer column, one Properties → Image dialog
- [ ] Autoruns with Hide Microsoft Entries on — Logon, Scheduled Tasks, Services tabs — with at least one pink and one yellow row
- [ ] Autoruns **Scan Options** dialog showing VirusTotal **unticked**
- [ ] TCPView with a browser's connections
- [ ] `autorunsc64` CSV open in Calc
- [ ] `Compare-Object` output for services (empty) and for processes (churn)

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 04. Announce at 8:00.

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Which Channel?" | 8:30–8:40 | Whole class, chat |
| Activity 2 "Build the View" | 9:00–9:20 | Individually, pairs for help |
| Activity 3 "The Same Question, Three Ways" | 9:40–10:00 | Individually (observed) |
| Activity 4 "What Starts Without You?" | 10:40–10:55 | Teams |
| Baseline v2 follow-along | 10:55–11:35 | Whole class, everyone running the lines |

---
---

# PART 5 — ACTIVITY 3 OBSERVATION SHEET
### Open at 9:40. One row per trainee.

| Trainee | Hashtable with the right keys (LogName · Id · StartTime) and a named CSV that exists in `Day_05`? | All three counts stated (zero included) and whether they agree? | Note |
|---------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both. This is knowledge 1.1 / 1.3 applied, and `ICT311203` (computer operations) observed. A trainee whose three ways all return **zero** and who says so is competent — a quiet machine is a valid result.

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | 5 custom views (`.xml`) + purpose list | ☐ |
| 2 | Filter cookbook sheet (8 counts) + 2 CSVs | ☐ |
| 3 | Baseline v2 — 4 CSVs + `baseline_v2_hashes.csv` + compare note | ☐ |
| 4 | Autoruns worksheet (10 own-machine entries) | ☐ |
| 5 | OS-equivalents table | ☐ |
| 6 | Evidence register + 1 self-check | ☐ |
| 7 | Reflection | ☐ |

## Still outstanding — keep chasing
| Item | From | Why open |
|------|------|----------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 01 | First on-site day |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall, **rename folder** | — |
| 8:15 | 5.1 + Demo 1 | Channels 1 and 5 briefly |
| 8:30 | Activity 1 | Six events |
| 8:40 | **5.2 + Demo 2 (custom view)** | **Never cut** |
| 9:00 | Activity 2 | `CV_Defender` only |
| 9:20 | 5.3 + Demo 3 | Skip ProviderName |
| 9:40 | **Activity 3 (observed)** | **Never cut** |
| 10:00 | Break | — |
| 10:10 | 5.4 + Demo 4 | Cut TCPView |
| 10:40 | Activity 4 | Four entries (A, C, D, H) |
| 10:55 | 5.5 + Demo 5 | Exports + hashes live; compare → PM |
| 11:35 | Brief & close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| Sysinternals blocked or not downloaded | Screenshots for Demo 4; Activity 4 is on paper; `Get-CimInstance` fallback for autoruns in Demo 5 |
| SmartScreen blocks `procexp64.exe` | More info → Run anyway (Microsoft-signed; it is the zip's mark-of-the-web) |
| Security log "access denied" | Expected; nothing today needs it |
| Cookbook #3 returns zero on most machines | Correct. Use #4 (boots) to show a non-zero result |
| No Day 04 folder on a trainee's machine | Re-run yesterday's four exports into `Day_04` (2 min) |
| Custom view import "query invalid" | Hand-edited XML with a typo; re-export the GUI-built one |
| Compare-Object shows everything different | `-Property` omitted |
| Behind at 10:55 | Exports and hashes live; the compare → PM Task 3 |

---
---

# PART 9 — LINKS FOR TRAINEES
- **Sysinternals Suite** (Microsoft, free) — `https://learn.microsoft.com/sysinternals/downloads/sysinternals-suite` — download the zip, unzip to `C:\Tools\Sysinternals\`. No install.
- Process Explorer, Autoruns, TCPView — each has its own page under `https://learn.microsoft.com/sysinternals/`
- The five channels, the four `Get-WinEvent` keys, the Autoruns colours — tables in your handout
- The custom-view XML — in your handout; copy it, do not retype it
- macOS and Linux equivalents — the seed table in your Activity Pack (Task 5)
- **Do not** enable the VirusTotal option in any Sysinternals tool
