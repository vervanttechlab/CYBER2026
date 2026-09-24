# DAY 10 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM, and before 1:00 PM

---

## THE DAY 10 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_10_Instructor_Guide.md` | Trainer only | — |
| `Day_10_Presenter_Script.md` | **Trainer only. The words, slide by slide** | Second screen |
| `Day_10_Demonstration_Guide.md` | Trainer only | — |
| `Day_10_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_10_Sample_Data.md` | Trainer. **§3 (the evidence set) is already in the trainees' Activity Pack, Part 0** | — |
| `Day_10_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_10_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| `Day_10_Resources.md` | Trainer, and the trainee section | — |
| `Day10_AI_Presentation_Prompt.md` | Trainer only: the prompt the deck was built from | Before the day |
| `Day_10_Unit_Assessment_Guide.md` | **Trainer / assessor only. Contains every key** | — |
| `Day_10_Written_Exam.docx` | Candidates | **1:10 PM only** |
| `Day_10_Practical_Assessment_Brief.docx` | Candidates | **2:00 PM only** |

> The Handout, Activity Pack, Solutions and the two candidate papers are **Word documents (.docx)**, as requested.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms**: **pairs** for Activity 1, teams for 2 and 3, **ORAL-1 / ORAL-2** for the afternoon | Activities 1–3 · the orals |
| **Recording on, all day** | Activity 1 is observed. **The whole afternoon is assessment evidence** |
| **Camera on** for Demo 1 | The notification is a role-play |
| A **co-host** to play R. Santos in Demo 1 *(optional)* | Demo 1 |
| The **shared ticket register** with the SRV-BAK-02 and WKS-311 rows updated to *Isolated* | Demo 1 |
| **Chat**, visible in the morning, **monitored** in the afternoon | The rule is no chat between candidates |
| **Submission folders** or an online form for the exam and the practical | The afternoon |

## On the trainer's machine
| Item | Why |
|------|-----|
| **PowerShell** (normal window) | Demo 3: `Get-NetTCPConnection` |
| A browser tab on **`https://mitre-attack.github.io/attack-navigator/`** | Demo 4, Activity 3 |
| A browser tab on **`https://attack.mitre.org`** | Checking technique IDs |
| A document with the **written-notification template** (Sample Data §5) | Demo 1 |
| A document with the **two tables** (hosts, path) | Demo 2 |
| The **threat report template** (Sample Data §6) | Topic 10.5 |
| **Fallback screenshots** | Part 3 |

> **No live Wazuh server, no Atomic Red Team, no TCPView, no Hayabusa.** All four are previewed from screenshots in Demo 5. **None is used in the assessment.**

## Printed or on paper
- `Day_10_Presenter_Script.md`
- The **N1 call** (Sample Data §2), on the second screen for Demo 1
- The **evidence set** (§3) and the **twelve behaviours** (§4)
- The **Activity 1 observation sheet** (Part 5)
- **Assessment:** the observation checklist (Assessment Guide Part 5), one per candidate · the oral bank (Part 6) · the result sheet (Part 8)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows machine with Defender on** | Demo 3 in the morning. **Part 2 of the assessment** in the afternoon (EICAR, status, scan) |
| A **browser** that can open `mitre-attack.github.io` | Activity 3, and Part 4 of the assessment |
| **Camera and microphone** | Activity 1 is a role-play. **The afternoon is observed, cameras on** |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| **All their Evidence folders, Day 3 and Days 5–9, filed** | The portfolio interview |
| **The portfolio checklist** (last page of the Handout), filled in | Collected at 8:10 |
| Their **Day 6 EICAR string** (from the Day 6 materials), ready to paste | Assessment Part 2 |
| Their **Day 6 severity matrix, Day 9 failure-kind card and authority matrix** | Open book in the demonstration |
| A folder `Evidence/Day_10/` and a folder `Evidence/Assessment/<surname>/` | Everything goes there |

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] A filled written notification for N1 (the Demo 1 model)
- [ ] The two Demo 2 tables filled (hosts and path), and the path drawn
- [ ] `Get-NetTCPConnection -State Established` on your machine, with one egress row circled
- [ ] `Get-NetTCPConnection -State Listen` with one port circled
- [ ] **ATT&CK Navigator**: an empty Enterprise matrix · the search box with `T1566.001` · a finished layer with B1–B12 coloured · the download button circled
- [ ] A finished threat report (the Solutions model), for Topic 10.5
- [ ] **Wazuh**: one screenshot of the MITRE ATT&CK module dashboard (preview only)
- [ ] **Atomic Red Team**: one screenshot of a test being run in a sandbox (preview only)
- [ ] **Hayabusa**: one screenshot of a CSV timeline (preview only; the Day 9 one can be reused)

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 9. Announce them at 8:00. **Activity 1 is in pairs.** If the class is odd, one trio (analyst, owner, observer).

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Ten Minutes" | 8:35–8:55 | **Pairs** (observed) |
| Activity 2 "Draw the Path" | 9:20–9:40 | Teams |
| Activity 3 "Name It, Map It" | 10:35–10:55 | Teams (10 min), then individually (10 min) |
| Activity 4 "Assemble the Report" | 11:05–11:30 | Individually |
| **Oral questioning** | **2:00–3:50** | **ORAL-1** (and **ORAL-2** if a second assessor), one candidate at a time |

---
---

# PART 5 — ACTIVITY 1 OBSERVATION SHEET
### Open it at 8:35. Visit each pair once during the N2 call. One row per trainee playing the analyst.

| Trainee | Severity + reason, what is known, and a specific "do / do not"? | One ask + next-update time + read-back, and no blaming the user? | N3 decided with a reason? | Note |
|---------|------------------------------------------------------------------|------------------------------------------------------------------|---------------------------|------|
| | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | |
| | ☐ | ☐ | ☐ | |

This is **practice** for the assessed notification this afternoon. Give feedback in the room. It is E5 PC 5.1, and `400311101` LO1 (spoken messages, read-back).

---
---

# PART 6 — EVIDENCE COLLECTION LOG

## Morning (portfolio evidence, submitted at 11:45 as it stands)

| # | Item | Received? |
|---|------|-----------|
| 1 | N2 written notification + call notes + the N3 decision | ☐ |
| 2 | Hosts table + path drawing | ☐ |
| 3 | Own-machine ingress / egress record | ☐ |
| 4 | ATT&CK mapping table + **Navigator layer JSON** | ☐ |
| 5 | Threat report on SRV-BAK-02 (draft or complete; complete by the end of Day 11) | ☐ |

## Afternoon (assessment evidence)

| # | Item | Received? |
|---|------|-----------|
| 1 | Written exam | ☐ |
| 2 | Practical brief, filled in | ☐ |
| 3 | Screenshots A1–A7 | ☐ |
| 4 | Observation checklist completed by the assessor | ☐ |
| 5 | Oral + portfolio interview recorded | ☐ |

## Still outstanding: keep chasing
| Item | From | Why it is open |
|------|------|----------------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 1 | First on-site day |
| Lab-subnet Nmap sweep | Day 5 | Needs the lab and authorisation |
| Windows Sandbox / Atomic Red Team | Day 8, Day 10 | Previewed only |
| Hayabusa / DeepBlueCLI / EvtxECmd + Timeline Explorer | Day 9 | Previewed only |
| **TCPView**, **Wazuh ATT&CK module** | Day 10 | Previewed only |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall, checklists | — |
| 8:15 | **10.1 + Demo 1 (notification)** | **Never cut** |
| 8:35 | **Activity 1 (observed)** | **Never cut** |
| 8:55 | 10.2 + Demo 2 | **Never cut the SRV-FIN-02 step** |
| 9:20 | Activity 2 | Hosts table only |
| 9:40 | 10.3 + Demo 3 | Steps 2, 4 and 6 only |
| 10:00 | Break | — |
| 10:10 | 10.4 + Demo 4 | Map B1 only |
| 10:35 | Activity 3 | B6, B7, B9, B10, B12 |
| 10:55 | 10.5 + Demo 5 | Skip Demo 5 |
| 11:05 | Activity 4 | Sections 3–10 only |
| 11:30 | Assessment briefing + close | **Never cut slide 15** |
| **1:00** | **Assessment** (Assessment Guide) | **Nothing in the afternoon is cut. Move it (Assessment Guide Part 9)** |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| No co-host for Demo 1 | Read both parts |
| Odd number for pairs | One trio, rotating |
| Navigator blocked or down | Paper mapping table. The JSON is made later |
| `Get-NetTCPConnection` output too long | `| Select-Object -First 15` |
| A trainee's machine shows an odd connection | `Get-Process -Id` names it. If it is still odd, note it for L2. No investigation in class |
| A trainee cannot attend the afternoon | Record them as **not yet assessed** (not NYC). Arrange the full assessment live, before Day 15 |
| Platform fails in the afternoon | Assessment Guide Part 9. **Never convert the assessment to self-study** |

---
---

# PART 9 — LINKS FOR TRAINEES
- **ATT&CK Navigator:** `https://mitre-attack.github.io/attack-navigator/` (runs in the browser; no account)
- **MITRE ATT&CK:** `https://attack.mitre.org` (the technique pages, as on Day 3)
- The seven lines of the notification call: in your handout (Topic 10.1)
- The four words for a host, and the path: in your handout (Topic 10.2)
- The ingress / egress commands for your own machine: in your Activity Pack (Demo 3 record)
- The threat report template: in your Activity Pack (Activity 4)
- The portfolio checklist: the last page of your handout. Fill it in before 8:00
- Wazuh ATT&CK module, Atomic Red Team, TCPView, Hayabusa: preview only. You will meet them in the on-site lab and once the server is built
