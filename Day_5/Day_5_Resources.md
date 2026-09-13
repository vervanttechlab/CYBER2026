# DAY 5 — RESOURCES AND MATERIALS
## Everything you need to have ready before 8:00 AM

---

## THE DAY 5 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_5_Instructor_Guide.md` | Trainer only | — |
| `Day_5_Presenter_Script.md` | **Trainer only. The words, slide by slide** | Open on a second screen while presenting |
| `Day_5_Demonstration_Guide.md` | Trainer only | — |
| `Day_5_Solutions.md` | **Trainer only. Never send to trainees** | — |
| `Day_5_Sample_Data.md` | Trainer; §4 scripts reproduced in the Activity Pack | — |
| `Day_5_Student_Handout.md` | Every trainee | With the joining note, the night before |
| `Day_5_Student_Activity_Pack.md` | Every trainee | With the joining note, the night before |
| `Day_5_Resources.md` | Trainer, and the trainee section below | — |
| **`Day_5_access_log.txt`** | **Every trainee** | With the joining note — Activity 3, Tasks 6 & 7 |
| **`Day_5_log_parser.py`** | **Every trainee** | With the joining note — Demo 7, Task 7 |
| `Day05_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> There is no separate ticket file today. The WKS-311 material lives in `Day_5_Sample_Data.md` §1.

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform

| Item | Why | Note |
|------|-----|------|
| Video platform with **breakout rooms** | Activities 2, 3 and 4 need them | Create and name before 8:00 |
| **Recording** enabled | Activity 2 is observed | Tell the class it is recording |
| **Chat**, visible to all | Activity 1 runs through it | Test that everyone can post |
| A way to **paste the log** into each breakout | Activity 3 teams read `Day_5_access_log.txt` | Have it ready to paste, or confirm they have the file |
| **Private messaging** | Not strictly needed today | — |

## On the trainer's machine

| Item | Why | Where to get it |
|------|-----|-----------------|
| **PowerShell** | Every demo | Built into Windows |
| **Python 3** | `http.server` (Demo 6), the parser (Demo 7) | `python.org` — tick "Add to PATH" |
| **A browser with developer tools** | Demo 6 | Any modern browser, `F12` |
| **TCPView** (portable) | Demo 4 | Sysinternals — `learn.microsoft.com/sysinternals`, no install |
| **Autoruns** (portable) | Demo 1 | Sysinternals, no install |
| **Nmap** *(optional)* | Demo 5 localhost scan | `nmap.org` — screenshot fallback if absent |
| **Wireshark + Npcap** *(optional)* | Demo 8 only | `wireshark.org` — trainer machine only |
| `Day_5_access_log.txt` and `Day_5_log_parser.py` | Demos 6–7 | In this folder |
| **Fallback screenshots** | For when something will not run | Take the night before — see Part 3 |

## Printed or on paper

Nothing is required on paper — Day 5 is a remote day. If you like paper for yourself:
- `Day_5_Presenter_Script.md`
- The **Quick Answer Strip** at the end of `Day_5_Solutions.md`
- The **Activity 2 observation sheet** in Part 5 below

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send this list with the joining note the night before.**

| Item | Why |
|------|-----|
| A computer with a **working browser and PowerShell** | Every demo is follow-along |
| **Camera and microphone** | Activity 2 is observed |
| **Python 3** installed | For Task 7 and the http.server task *(with a by-hand fallback if it will not install)* |
| The **Student Handout** and **Activity Pack**, open or printed | You write in both all day |
| **`Day_5_access_log.txt`** and **`Day_5_log_parser.py`** | Sent with this note — put them in one folder |
| A folder called `Evidence/Day_05/` | Everything you produce goes in it |
| **TCPView** and **Autoruns** (portable) if you can | Optional — the built-in commands cover everything |
| Your **Day 3 class QA checklist** | You self-check the re-ticket against it in Task 8 |

> **Two warnings for the joining note:** *"(1) Today you will run commands on your own machine — that is expected and safe. (2) Do not run any script we ask you to read, and do not scan any machine that is not your own. We explain why at 10:15."*

---
---

# PART 3 — TOOLS AND LINKS

## Free tools used today

| Tool | Link | Footprint |
|------|------|-----------|
| Python 3 | `python.org` | ~25 MB |
| TCPView (portable) | Microsoft Sysinternals | ~1 MB, no install |
| Autoruns (portable) | Microsoft Sysinternals | ~2 MB, no install |
| Nmap *(optional)* | `nmap.org` | ~30 MB |
| Wireshark *(optional, trainer)* | `wireshark.org` | ~75 MB |

## Fallback screenshots — take these the night before

Because most of today is your own live output, the screenshots are for when a tool will not run:

- [ ] `Get-Process` showing the `Path` column and a real `svchost` path
- [ ] `netstat -ano` output with the PID column
- [ ] The one-line PowerShell connection→process join, with results
- [ ] A router NAT / port-forwarding page (blur any real detail)
- [ ] `nmap -sT 127.0.0.1` result
- [ ] A browser DevTools Network tab showing a 200 and a 404
- [ ] The parser output (status counts and IP counts)
- [ ] *(Optional)* a Wireshark capture with `http` and `dns` filters

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS

## Role rotation
Rotate roles from Day 3: Shift Lead → Scribe → Presenter → next. Announce at 8:00, ten seconds to sort out.

## Breakout schedule

| Activity | Time | Rooms | What happens |
|----------|------|-------|--------------|
| Activity 2 "Follow the Connection" | 9:40–10:05 | Pairs | Each trainee traces one own connection, reports it in clues |
| Activity 3 "Access-Log Detective" | 10:40–11:05 | Teams | Reconstruct the attack from the log, then present |
| Activity 4 "Explain This Script" | 11:15–11:33 | Pairs | Read three scripts, predict behaviour |

> **Fewer than four teams for Activity 3?** Run it with any number — every team reads the same log. Bring two teams back to present; take the rest from the Solutions walkthrough.

---
---

# PART 5 — ACTIVITY 2 OBSERVATION SHEET
### Open this at 9:40. One row per trainee.

Two things are observed. Tick each.

| Trainee | Joined a connection to its **process** unprompted? | Reported in **clues**, not their own IP? | Note |
|---------|---------------------------------------------------|------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both ticks. If a trainee reads out their own IP, correct it live and note it — the point is the Day 3 rule holding on their own machine.

---
---

# PART 6 — EVIDENCE COLLECTION LOG
### What each trainee should submit by 4:00 PM

| # | Item | Received? |
|---|------|-----------|
| 1 | Signed build checklist | ☐ |
| 2 | 4 baseline CSVs (named) + hashes + register table | ☐ |
| 3 | Maintenance note + two matching hashes | ☐ |
| 4 | Five annotated connections | ☐ |
| 5 | Port-map diagram | ☐ |
| 6 | Six web-log answers + own two log lines | ☐ |
| 7 | Extended parser + output (or hand tally) | ☐ |
| 8 | Re-written WKS-311 ticket + self-check | ☐ |
| 9 | Three reflection answers | ☐ |

## Still outstanding — keep chasing

| Item | From | Why still open |
|------|------|----------------|
| Lab OSH Checklist | Day 1 | Describes the physical lab; signed on the first on-site day |
| Green Lab Pledge | Day 1 | Same |
| **Live lab-subnet Nmap sweep** | Day 5 | Needs the physical lab and a signed authorisation; done on the first on-site day. Day 5 covered the knowledge and the localhost-only scan |

---
---

# PART 7 — TIMING CARD
### Tape this to the corner of your monitor

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall Day 3 | — |
| 8:15 | Demo 1 + Activity 1 | Trim Activity 1 to 6 items |
| 8:47 | Demo 2 (baseline) | Show export only; hashing → PM |
| 9:05 | Demo 3 (the wire) | Skip `tracert` |
| 9:25 | Demo 4 (connection→process) | **Never cut — it is the day** |
| 9:40 | **Activity 2 (observed)** | **Never cut** |
| 10:05 | Break | — |
| 10:15 | Demo 5 (NAT, localhost scan) | Screenshot instead of live Nmap |
| 10:25 | Demo 6 (web request) | — |
| 10:40 | Activity 3 (log) | Two teams present, not four |
| 11:05 | Demo 7 (parser) | Show Python only, skip PowerShell version |
| 11:15 | Activity 4 (scripts) | Two scripts (A + B), drop C to PM |
| 11:33 | Afternoon brief | — |
| 11:40 | Close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| A trainee has no Python | Task 7 by hand from the log; Demo 6 http.server they watch on your screen |
| `http.server` port in use | Use `8080`; browse `http://localhost:8080` |
| TCPView / Autoruns blocked | `netstat -ano` + `tasklist`, and `Get-CimInstance Win32_StartupCommand` cover them |
| Nmap absent | Screenshot fallback; the RA 10175 rule matters more than the tool |
| A trainee wants to run script B | "No. Read it, escalate it. Running it is the incident" |
| A trainee scans a neighbour's machine | Stop it immediately. Only `127.0.0.1`. It is an offence under RA 10175 |
| Whole class network is down | Everything localhost still works: Demos 1, 2, 4, 6, 7 need no internet |

---
---

# PART 9 — LINKS FOR TRAINEES

- Python — `python.org`
- Sysinternals TCPView & Autoruns — search "Sysinternals TCPView"
- Status codes reference — MDN "HTTP response status codes"
- Private address ranges — RFC 1918 (informational)
- RA 10175, Cybercrime Prevention Act — the law that makes unauthorised scanning an offence
