# DAY 6 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 6 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_6_Instructor_Guide.md` | Trainer only | — |
| `Day_6_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_6_Demonstration_Guide.md` | Trainer only | — |
| `Day_6_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_6_Sample_Data.md` | Trainer — scripts, cards, matrix | — |
| `Day_6_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_6_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_6_Resources.md` | Trainer, and the trainee section below | — |
| `Day06_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> The student handout, activity pack and solutions are **Word documents (.docx)**, not markdown, on request.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** | Activities 2, 3, 4 |
| **Recording** on | Activity 2 is observed |
| **Chat**, visible to all | Activity 1 |
| **Private messaging** | Sending source cards / intake context per team |

## On the trainer's machine — all built into Windows, nothing to install
| Item | Why |
|------|-----|
| **Microsoft Defender** (on) | Demo 3, the EICAR detection |
| **Event Viewer** (`eventvwr.msc`) | Demo 2 |
| **Windows Security app** → Protection history | Demos 2–4 |
| **Notepad** | Making the EICAR file |
| The EICAR string from `Day_6_Sample_Data.md` §1 | Demo 3 |
| **Fallback screenshots** | See Part 3 |

> **No server, no Wazuh, no Python, no extra tools today.** That is deliberate — everything is already on every Windows machine.

## Printed or on paper
- `Day_6_Presenter_Script.md`
- The **Activity 2 observation sheet** (Part 5)
- The six **intake scripts** (Sample Data §3) — easier to read aloud from paper

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note the night before.**

| Item | Why |
|------|-----|
| A **Windows machine with Microsoft Defender on** | The EICAR detection, the logs |
| **Camera and microphone** | Activity 2 is observed |
| The **Student Handout** and **Activity Pack** (Word docs), open or printed | You write in both |
| A folder `Evidence/Day_06/` | Everything you produce goes here |
| Your **Day 3 class QA checklist** and **Day 5 notes** | Referenced today and tomorrow |

> **Reassurance to put in the joining note:** *"Tomorrow we will safely make your antivirus catch a test file. It is 100% safe — a harmless test, not a virus. Do not worry when you see the pop-up; that is the point of the exercise."*

---
---

# PART 3 — FALLBACK SCREENSHOTS

Because everything is local, screenshots are for when a machine misbehaves:
- [ ] Event Viewer with the Windows Defender / Operational log open
- [ ] Windows Security → Protection history showing an EICAR entry
- [ ] A Defender "threat found" pop-up
- [ ] The Defender Operational log showing event 1116 and 1117
- [ ] The four alert-source snippets (also on the slides)

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS

## Role rotation
Rotate from Day 5. Announce at 8:00.

## Breakout schedule
| Activity | Time | Rooms |
|----------|------|-------|
| Activity 2 "Take the Call" | 9:30–10:00 | Pairs (observed) |
| Activity 3 "Make a Real Alert" | 10:45–11:10 | Individually, in pairs for help |
| Activity 4 "Red Flag or Routine?" | 11:25–11:38 | Teams |

---
---

# PART 5 — ACTIVITY 2 OBSERVATION SHEET
### Open at 9:30. One row per trainee.

Two things observed. Tick each.

| Trainee | Captured all core facts (who/what/when/where/callback)? | Asked the clarifying question for the missing fact, calmly? | Note |
|---------|--------------------------------------------------------|------------------------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both ticks. This is `400311101` (workplace communication) observed on the job.

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | 6 intake forms across ≥4 channels | ☐ |
| 2 | 1 detection record (EICAR) | ☐ |
| 3 | Event log worksheet — 3 events | ☐ |
| 4 | Sources reference table | ☐ |
| 5 | 2 red-flag indicator cards | ☐ |
| 6 | Severity mapping sheet | ☐ |
| 7 | Reflection | ☐ |

## Still outstanding — keep chasing
| Item | From | Why still open |
|------|------|----------------|
| **Wazuh SIEM server** (agent enrolment, dashboard, rule levels 0–15) | Phase B | Not built yet; a half-day add-on once the server box is set up |
| Lab OSH Checklist, Green Lab Pledge | Day 1 | Signed on the first on-site day |
| Lab-subnet Nmap sweep | Day 5 | Needs the lab and signed authorisation |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall Day 5 | — |
| 8:15 | 6.1 alert arrives | — |
| 8:30 | 6.2 + Demo 1 | — |
| 8:55 | Activity 1 | Trim to 3 items |
| 9:15 | 6.3 intake | — |
| 9:30 | **Activity 2 (observed)** | **Never cut** |
| 10:00 | Break | — |
| 10:10 | 6.4 + Demo 2 | — |
| 10:30 | **Demo 3 EICAR** | **Never cut** |
| 10:45 | Activity 3 EICAR | — |
| 11:10 | 6.5 + Demo 4 | Two red flags only |
| 11:25 | Activity 4 | Fewer cards |
| 11:38 | Brief & close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| Defender blocks creating the EICAR file | The block is the detection — read Protection history |
| Third-party AV instead of Defender | Use its own detection history |
| No admin / Security log locked | Defender Operational log + Protection history need no admin |
| A trainee is scared of "a virus" | Reassure: harmless test string, never malware |
| Class connection poor | Everything is local — no bandwidth needed after joining |
| Behind at 11:10 | 6.5 to two red flags; severity → PM Task 6 |

---
---

# PART 9 — LINKS FOR TRAINEES
- EICAR test file — search "EICAR test file" (the official standard antivirus test)
- Microsoft Defender Protection history — Windows Security app
- Event Viewer — built into Windows (`eventvwr.msc`)
- The alert-source acronyms (SIEM, AV, EDR, WAF, DLP, NDR) — glossary in your handout
