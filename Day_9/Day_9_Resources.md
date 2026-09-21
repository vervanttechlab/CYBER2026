# DAY 9 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 9 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_9_Instructor_Guide.md` | Trainer only | — |
| `Day_9_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_9_Demonstration_Guide.md` | Trainer only | — |
| `Day_9_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_9_Sample_Data.md` | Trainer — the 2 client cases, the extract, the 8 situations, the matrix, the templates | — |
| `Day_9_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_9_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_9_Resources.md` | Trainer, and the trainee section | — |
| `Day09_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> Handout, Activity Pack and Solutions are **Word documents (.docx)**, not markdown, on request.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** — **pairs** for Activity 1, teams for 2 and 3 | Activities 1–3 |
| **Recording** on | Activity 1 is observed |
| **Camera on** for Demo 1 | The call is a role-play, not a screen |
| A **co-host** to play M. Lopez in Demo 1 *(optional — you can read both parts)* | Demo 1 |
| The **shared ticket register** with the SRV-BAK-02, WKS-118 and WKS-205 rows already in it | Demos 1 and 4 |
| **Chat**, visible | Quick answers; fallback for Activity 3 if behind |

## On the trainer's machine — built into Windows
| Item | Why |
|------|-----|
| **PowerShell** (normal window) | Demo 2 — the failed-action pass |
| **Windows Security app** | Protection history wording for the GUI fallback |
| A document with the **written-confirmation template** (Sample Data §7) | Demo 1 |
| A document with the **escalation pack template** (Sample Data §6) | Demo 4 |
| An **email client or a shared doc** to "send" the pack | Demo 4 — or paste into the register row |
| **Fallback screenshots** | Part 3 |

> **No live Wazuh server needed. No Hayabusa / DeepBlueCLI / Timeline Explorer needed.** All are previewed from screenshots in Demo 5.

## Printed or on paper
- `Day_9_Presenter_Script.md`
- The **call script for V1** (Sample Data §1) — on the second screen for Demo 1
- The **Activity 1 observation sheet** (Part 5)
- The **log extract** (§2) and the **eight situations** (§4)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows machine with Defender on** | PM Task 2 — the failed-action pass on their own machine |
| **Camera and microphone** | Activity 1 is a role-play, observed |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| Their **Day 7 ticket register** (with CTM-0007-001) and their **Day 8 worksheets** | The SRV-BAK-02 case travels Day 7 → 8 → 9 |
| Their **Day 3 class QA checklist** | Self-checking a pack (Task 6) |
| An **email tool**, or the shared register | "Sending" the packs (Task 3) |
| A folder `Evidence/Day_09/` | Everything goes here |

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] A filled written confirmation for V1 (CLEAN) — the Demo 1 model
- [ ] A filled written confirmation for V2 (NOT CLEAN)
- [ ] `Get-MpThreatDetection | Where-Object { -not $_.ActionSuccess }` returning nothing
- [ ] `Get-WinEvent` for 1118/1119/1002/2001 returning "No events were found"
- [ ] Protection history showing **"Action needed — remediation incomplete"** (any machine that has one; or a cropped image from Microsoft's documentation)
- [ ] The register row for WKS-118 after Demo 1 (status *Verified with client*)
- [ ] The register row for SRV-BAK-02 after Demo 4 (status *Escalated*, to whom, time, next update due)
- [ ] A filled escalation pack for Situation 1 — the Demo 4 model
- [ ] **Hayabusa** — one screenshot of a CSV timeline open in Timeline Explorer (preview only)
- [ ] **Wazuh** — one screenshot of an alert search showing Defender 1118 events across agents (preview only)

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 8. Announce at 8:00. **Activity 1 is in pairs** — if the class is odd, one trio (analyst, client, observer).

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Make the Call" | 8:50–9:20 | **Pairs** (observed) |
| Activity 2 "Find the Failure" | 9:45–10:00 | Teams |
| Activity 3 "Who Gets This?" | 10:30–10:45 | Teams |
| Activity 4 "Build the Pack" | 11:05–11:35 | Individually |

---
---

# PART 5 — ACTIVITY 1 OBSERVATION SHEET
### Open at 8:50. Visit each pair once during the V2 (not-clean) call. One row per trainee playing the analyst.

| Trainee | Ticket ID first, and "not clean — the threat is still there" said plainly, not softened? | One specific ask + what happens next + a read-back obtained? | Note |
|---------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both. This is E4 PC 4.1, and `400311101` LO1 (spoken messages, read-back) observed. If you only catch a pair's V1 call, mark what you heard and note "V1 only".

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | 2 client verification records (V1 clean, V2 not clean) — call notes + confirmation | ☐ |
| 2 | Annotated log extract (8 entries by kind) + own-machine failed-action pass | ☐ |
| 3 | 3 escalation packs (Situations 1, 2, 5) | ☐ |
| 4 | Escalation trail — 3 register rows | ☐ |
| 5 | Failed-action SOP card | ☐ |
| 6 | 1 pack self-check | ☐ |
| 7 | Reflection | ☐ |

## Still outstanding — keep chasing
| Item | From | Why open |
|------|------|----------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 1 | First on-site day |
| Lab-subnet Nmap sweep | Day 5 | Needs lab + authorisation |
| Windows Sandbox / Atomic Red Team | Day 8 | Previewed only — Pro edition + RAM |
| **Hayabusa / DeepBlueCLI / EvtxECmd + Timeline Explorer** | Day 9 | Previewed only — scheduled for the on-site lab |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall | — |
| 8:15 | 9.1 lifecycle | Two sentences + the diagram |
| 8:30 | **9.2 + Demo 1 (the call)** | **Never cut** |
| 8:50 | **Activity 1 (observed)** | **Never cut** |
| 9:20 | **9.3 + Demo 2 (five kinds)** | **Never cut** |
| 9:45 | Activity 2 | Entries B, C, D, E only |
| 10:00 | Break | — |
| 10:10 | 9.4 + Demo 3 | Situations 1 and 5 only |
| 10:30 | Activity 3 | Five situations (1, 2, 3, 5, 8) |
| 10:45 | 9.5 + Demo 4 + Demo 5 | Fields 1, 5, 6, 9; skip Demo 5 |
| 11:05 | Activity 4 | Starts in the afternoon |
| 11:35 | Brief & close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| No co-host for Demo 1 | Read both parts |
| Odd number for pairs | One trio — analyst, client, observer — rotate on V2 |
| A trainee's own machine shows a real failed action | A live example — name the kind together; it becomes their Task 2 extract |
| `Get-WinEvent` access denied | Protection history wording ("Action needed", "Remediation incomplete", "Failed") — the same kinds |
| No email tool | Paste the pack into the register row's notes; the pack is the document |
| A trainee restores `payroll_calc.xlsm` in Activity 3's reasoning | Stop and teach: above their level, might be real — vendor case |
| Activity 4 overruns | Fields 1–3 and 9 live; the rest → PM Task 3 |
| Behind at 10:45 | Demo 4 fields 1, 5, 6, 9; skip Demo 5; Activity 4 → afternoon |

---
---

# PART 9 — LINKS FOR TRAINEES
- The eight steps of the verification call — in your handout (Topic 9.2)
- The written-confirmation template — in your Activity Pack (Task 1)
- The five kinds of failure and where each shows — table in your handout (Topic 9.3)
- The four authorities and what each needs — table in your handout (Topic 9.4)
- The escalation pack template — in your Activity Pack (Task 3)
- Failed-action commands for your own machine — in your Activity Pack (Task 2)
- Hayabusa, Timeline Explorer, Wazuh — preview only today; you will meet them in the on-site lab and once the server is built
