# DAY 7 — INSTRUCTOR GUIDE
## Topic: Decide, Ticket, and Check the Tool Is Working
### Cyber Threat Monitoring Level I · Day 07 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **Same two conditions as Day 6.** (1) **No SIEM server yet** — everything runs on each trainee's own Windows machine, and the "ticket system" is a shared **spreadsheet ticket register** (the plan's documented fallback for osTicket). (2) **Total beginners** — assume nothing, every click shown, calm pace.

---

## HOW THIS GUIDE WORKS

The **topic guide** — what Day 7 teaches, why, what you must know, and how it is assessed. Not a script. Keep these open:

| File | For |
|------|-----|
| **`Day_7_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_7_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_7_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_7_Student_Activity_Pack.docx`** | what the trainees do |
| **`Day_7_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_7_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_7_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_7_Sample_Data.md`** | the 8 alerts, the ticket register template, the solution-status scenarios |

---
---

# PART A — WHAT DAY 7 IS

## The one-sentence topic

> **Day 6 received the alert. Day 7 finishes the front of the job: decide what the alert is (threat, detection, or routine), raise a proper ticket, and then check whether the security tool that raised it is actually installed, working, and able to clean up.**

## Where Day 7 sits

Day 7 completes **Element 1** of the core unit and delivers all of **Element 2**:

| Element / PC | What Day 7 does |
|--------------|-----------------|
| **E1 PC 1.4** Alert assessed against pre-identified criteria | Topic 7.1 — threat / detection / routine, plus severity |
| **E1 PC 1.5** Ticket issued upon confirmation | Topic 7.2 — the ticket register, fields, timestamps, the SLA clock |
| **E2 PC 2.1** Enterprise security solution checked if installed | Topic 7.3 — `Get-MpComputerStatus` on the endpoint |
| **E2 PC 2.2** Checked if operational | Topic 7.3 — service running, real-time on, signatures current |
| **E2 PC 2.3** Checked if it can clean or delete the issue | Topic 7.4 — the EICAR quarantine action, and the action range |

After today, Elements 1 and 2 are done. Element 3 (manual checking and verification) is Day 8; Element 4 (case follow-up) Day 9; Element 5 (reporting) Day 10.

## What "no server" changes

The plan used the Wazuh dashboard as the "enterprise management console" and its agent list to check solution status. With no server, Day 7 does the same job **from the endpoint itself** — which is arguably the purer skill:

| Plan's Tier-2 (not available) | Day 7 uses instead |
|-------------------------------|--------------------|
| Wazuh dashboard as ticket system | **Spreadsheet ticket register** (LibreOffice Calc / Excel) |
| Wazuh agent inventory for solution status | **`Get-MpComputerStatus`, `Get-Service WinDefend`, Windows Security** on the machine |
| Wazuh console "clean/quarantine" evidence | **Defender Protection history** action + `MpCmdRun` |

The Wazuh management console becomes a **preview** in Topic 7.5 — "here is what you will do on it once it is built" — using the local Windows Security app as the stand-in console.

## The five topics of Day 7

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **7.1** | **Decide What It Is** — threat, detection, or routine, and how serious | E1 PC 1.4 | 20 min + Activity 1 |
| **7.2** | **Raise the Ticket** — the fields, the times, the SLA clock | E1 PC 1.5 | 20 min + Activity 2 |
| **7.3** | **Is the Tool Even Working?** — installed, operational, up to date | E2 PC 2.1, 2.2 | 35 min + Activity 3 |
| **7.4** | **Can It Clean Up?** — the action range, proven with EICAR | E2 PC 2.3 | 15 min |
| **7.5** | **The Management Console** — what it does, and a preview of Wazuh | E2 · knowledge | 15 min + Activity 4 |

---

## Competency map

### Core unit — `CS-ICT251101`, completing Element 1 and delivering Element 2

**Required knowledge today:** 1.6 *Log and detection management* (reading the tool's own status), 1.7 *Security solution scan and operations procedure*, 1.8 *Security solution management application* (the console, previewed), 1.9 *Severity classifications* (applied in the ticket).

**Required skills today:** analytical (the threat/detection/routine decision), computer operation (the status checks), communication (the ticket is written for the next person), interpreting work instructions (SOP fields).

### Basic and common units reprised

| Code | How it appears |
|------|---------------|
| `ICT315202` Apply quality standards | **LO2** — every ticket is self-checked against the class QA checklist written on Day 3 |
| `400311106` Access and maintain information | Tickets and the solution-status report are named and filed as evidence |

> **Still outstanding — say it:** the **Wazuh SIEM server**, the **Day 1 lab OSH checklist + green pledge**, and the **Day 5 lab-subnet scan**.

---

## The decision that anchors the whole day

The three words from Day 3 return, and they are the heart of Topic 7.1. Use these exact definitions:

| Word | Meaning | What you do |
|------|---------|-------------|
| **THREAT** | Genuinely dangerous and **not contained** — may still be happening or succeeding | Ticket, escalate, say what you need |
| **DETECTION** | Genuinely bad but the tool **found and handled** it — confirmed bad, contained | Ticket, verify the action worked, monitor |
| **ROUTINE** | Expected, authorised, or benign (including a false alarm) | Close with a written reason; report for tuning if it keeps firing |

> **The distinction that matters, and the one beginners miss: the line between threat and detection is CONTAINMENT, not severity.** A *failed* quarantine of small malware is a **threat**. A *successful* block of a serious attack is a **detection**. This is why "the antivirus found it" does not automatically mean "we are safe" — you must check the action actually worked (which is exactly why Element 2 exists, and it is the rest of today).

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. Take a received alert and decide **threat, detection, or routine**, with a reason.
2. Explain why **containment**, not severity, separates a threat from a detection.
3. Raise a **ticket** with every field the next analyst needs, and start the **SLA clock**.
4. Check, on a machine, whether the security tool is **installed** and **operational**.
5. Check whether the tool **can clean or delete** the issue, and read the action it took.
6. Say what a **management console** is for, and what they will do on the Wazuh one once it exists.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 6 (we received alerts; now decide) | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 20 | 3–4 | **Topic 7.1** Decide what it is — threat / detection / routine | Short input | 7.1 |
| 8:35 | 20 | 5 | **Activity 1** "Threat, Detection, or Routine?" | Breakout teams | 7.1 |
| 8:55 | 20 | 6 | **Topic 7.2** + **Demo 1** Raise the ticket (the register) | Follow-along | 7.2 |
| 9:15 | 30 | 7 | **Activity 2** "Write the Ticket" | Individually, observed | 7.2 |
| 9:45 | 15 | 8 | **Topic 7.3 part 1** + **Demo 2** Is it installed and operational? | Follow-along | 7.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 20 | 9 | **Topic 7.3 part 2** + **Demo 3** Reading the tool's own status | Follow-along | 7.3 |
| 10:30 | 25 | 10 | **Activity 3** "Is the Solution Working?" | Follow-along | 7.3 |
| 10:55 | 15 | 11 | **Topic 7.4** + **Demo 4** Can it clean up? (EICAR action) | Follow-along | 7.4 |
| 11:10 | 15 | 12–13 | **Topic 7.5** + **Demo 5** The management console · Wazuh preview | Follow-along | 7.5 |
| 11:25 | 13 | 14 | **Activity 4** "Read the Console" | Breakout teams | 7.5 |
| 11:38 | 7 | 15 | Afternoon brief · how it is marked · close | Whole class | — |

Morning sums to 225 (8:00 → 11:45). Lecture time is under 90 minutes.

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 35 minutes.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Triage 8 alerts — criteria + severity + reason | 35 | 8 triage decisions |
| 2 | Turn the 8 into ticket-register rows; write 2 in full | 30 | Register with 8 rows + 2 full tickets |
| 3 | Solution-status report on your own machine | 25 | Status report on the SOP template |
| 4 | Prove-it-cleans record — the EICAR action and the action range | 20 | Clean/quarantine record |
| 5 | Self-check 2 of your tickets against the Day 3 QA checklist | 15 | 2 completed self-check sheets |
| 6 | Management-console worksheet — what you'd check, local equivalents | 20 | Console worksheet |
| 7 | Reflection | 10 | Three answers |

---

## Before the day
### The night before
- [ ] Run all five demos on your own machine — especially the EICAR quarantine action (Demo 4) and `MpCmdRun` restore
- [ ] Prepare the shared **ticket register** spreadsheet; have the link ready to paste at 8:55
- [ ] Confirm `Get-MpComputerStatus` and `Get-Service WinDefend` run and show sensible values on your build
- [ ] Have the 8 alerts from `Day_7_Sample_Data.md` ready to send to the class
- [ ] Take the fallback screenshots in `Day_7_Resources.md`

### On the morning
- [ ] Breakout rooms; ticket register link ready
- [ ] Activity Pack, Handout, Resources sent
- [ ] The 8 alerts ready to paste per team
- [ ] Collect outstanding Day 1–6 evidence in the first fifteen minutes

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 7.1 — DECIDE WHAT IT IS
### 8:15–8:55 with Activity 1 · Slides 3–5 · E1 PC 1.4

### The point
The core judgement of the whole job: given an alert, is it a **threat**, a **detection**, or **routine**? Beginners can learn the rule that separates them.

### What you must know
The three definitions in the box above (Part A). Drill the containment rule with the two Day 3 examples:
- A failed quarantine of small malware → **threat** (found, but not contained).
- A successful block of a serious attack → **detection** (found and handled).

Then add **severity** (from Day 6) as a second, separate axis: threat/detection/routine says *what it is*; severity says *how fast and how loud*. A routine can never be Critical; a threat is usually High or Critical because it is uncontained.

### Key messages
- Ask two questions of every alert: **Is it real and bad?** and **Is it contained?** Real+bad+uncontained = threat. Real+bad+contained = detection. Not real / expected = routine.
- "The antivirus found it" is not the end of the story. Found is not the same as stopped. Check the action (that is Element 2, later today).
- Give a reason. A decision with no reason is not competent — that rule has held since Day 3.

### Mistakes to expect
- Trainees call anything the AV touched a "detection". Push them to check containment — a failed action makes it a threat.
- Trainees merge severity with the decision. Keep them separate: *what is it* vs *how serious*.

---

## TOPIC 7.2 — RAISE THE TICKET
### 8:55–9:45 with Demo 1 and Activity 2 · Slides 6–7 · E1 PC 1.5

### The point
A confirmed alert becomes a **ticket** — the record the whole rest of the response hangs off. Beginners write one into a real register.

### What you must know
"Ticket issued upon confirmation" (PC 1.5). The fields, which map onto the **class QA checklist the trainees wrote on Day 3** — use their own standard:

| Field | Why |
|-------|-----|
| Ticket ID + one-line summary (host + detection) | So the next analyst knows in three seconds if it's theirs |
| Host / user / system | Nothing can be done without knowing where |
| Time it happened **and** time you saw it | The gap is often the key fact |
| What the tool detected, in its words | Matched to the raw log later (Day 8) |
| Decision (threat/detection/routine) + **reason** | The most valuable line |
| Severity band | How fast, how loud |
| What you did / did not do | So work isn't repeated or assumed |
| What you need next, from whom | A ticket with no ask is a diary entry |

The **SLA clock**: a service-level agreement sets how fast each severity must be responded to (e.g. Critical ≤10 min, High ≤1 h). The clock starts when the ticket is raised — so raising it promptly and stamping the time matters.

Since there is no ticketing server, the register is a **spreadsheet** with these fields as columns. It carries exactly the same information a tool would.

### Key messages
- A ticket is written for the **next person**, not for you. Your work is good when someone else can continue it without asking you a question (the Day 3 close).
- Two timestamps, always: when it happened, and when you saw it. Keep them separate.
- The SLA clock starts at the ticket. Raise it promptly and stamp the time.

### Mistakes to expect
- Tickets with a decision but no reason. Not competent.
- One timestamp instead of two. Push for both.
- "Fix the computer" as the next-step. Push for a specific, addressed ask.

---

## TOPIC 7.3 — IS THE TOOL EVEN WORKING?
### 9:45–10:55 with Demos 2–3 and Activity 3 · Slides 8–10 · E2 PC 2.1, 2.2

### The point
Element 2: before you trust what a security tool told you, check the tool is **installed**, **operational**, and **up to date**. Beginners run these checks on their own machine.

### What you must know
Three questions, three checks, all built into Windows:

| Question (PC) | Check on the endpoint | Good answer looks like |
|---------------|-----------------------|------------------------|
| **Installed?** (2.1) | `Get-Service WinDefend` · Windows Security app opens | Service present; app shows "protections" |
| **Operational?** (2.2) | `Get-MpComputerStatus` → `AntivirusEnabled`, `RealTimeProtectionEnabled`; `AMServiceEnabled` | All **True** |
| **Up to date?** (part of 2.2) | `Get-MpComputerStatus` → `AntivirusSignatureVersion`, `AntivirusSignatureLastUpdated`, `QuickScanAge` | Signatures recent; scan not ancient |

*(These are the exact commands you touched on Day 5 for the workstation baseline — now they are the Element 2 skill.)* If `RealTimeProtectionEnabled` is **False**, the tool is installed but **not operational** — a real finding, and exactly the kind of thing an analyst reports.

### Key messages
- A security tool that is off is worse than no tool, because people think they are protected. Checking it is *on* is a real, daily analyst job.
- Installed, operational, up to date — three separate questions. A tool can be installed and switched off.
- These are the same commands from Day 5's baseline. You already know them; now you know why they matter.

### Mistakes to expect
- Trainees equate "installed" with "working". Separate the three: present, on, current.
- Trainees don't notice real-time protection off. Make one machine (yours) show it off, if you can, so they see the finding.

---

## TOPIC 7.4 — CAN IT CLEAN UP?
### 10:55–11:10 with Demo 4 · Slide 11 · E2 PC 2.3

### The point
The last Element 2 question: can the tool actually **clean or delete** the issue? Prove it with the EICAR detection from Day 6.

### What you must know
The CS **action range**: **Failed · Clean · Delete · Quarantine · Blocked · Re-image.** For EICAR, Defender **quarantines** (isolates) or **removes** it — that is a successful action. Show where the action appears in **Protection history**, and mention `MpCmdRun.exe` as the tool that can list and restore quarantined items (for when a *legitimate* file is quarantined by mistake).

The link back to 7.1: if the action is **Failed** or **Quarantine that didn't hold**, the issue is **not contained** — which makes it a **threat**, not a detection. Element 2 is how you find that out.

### Key messages
- "Cleaned" and "quarantined" are successes. "Failed" is not — and a failed action turns a detection into a threat.
- Quarantine is isolation, not deletion — the file is caged, and can be restored if it was a mistake.
- Checking the action worked is not paperwork; it is the difference between safe and not.

### Mistakes to expect
- Trainees assume every AV action succeeds. It doesn't — Day 9 is built on failed actions.

---

## TOPIC 7.5 — THE MANAGEMENT CONSOLE
### 11:10–11:38 with Demo 5 and Activity 4 · Slides 12–14 · E2 · knowledge 1.8

### The point
Introduce the idea of a **central console** that shows the status of many machines at once — and preview the Wazuh dashboard the class will use once the server is built.

### What you must know
A management console is one screen that answers, for the whole fleet: which machines have the tool, which are protected right now, which are out of date, and what each has detected. Today there is **no server**, so:
- The **local stand-in** is the **Windows Security app** — the same three questions (installed/operational/updated) for *one* machine.
- The **preview**: on Wazuh, you will see an agent list (connected / disconnected / last check-in), each agent's inventory, and its detections — the same questions, for *every* machine at once. Show screenshots only; set the expectation for the day the server is ready.

### Key messages
- A console scales the check you did today from one machine to hundreds.
- The questions never change: installed, operational, up to date, what has it found. The console just answers them for everyone at once.
- You will meet the real Wazuh console once the server is set up. Today you learned exactly what it will be telling you.

### Mistakes to expect
- Trainees think the console is a different skill. It is the same three checks, shown for many machines.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 7 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 8 triage decisions (criteria + severity + reason) | PM Task 1 + Activity 1 | E1 PC 1.4 |
| Ticket register with 8 rows + 2 full tickets | PM Task 2 + Activity 2 | E1 PC 1.5 |
| Solution-status report (installed/operational/updated) | PM Task 3 + Activity 3 | E2 PC 2.1, 2.2 |
| Clean/quarantine record with the action range | PM Task 4 | E2 PC 2.3 |
| 2 ticket self-checks against the class QA checklist | PM Task 5 | `ICT315202` LO2 |
| Management-console worksheet | PM Task 6 | knowledge 1.8 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

## Observation during the live session

**Activity 2 "Write the Ticket" is observed.** Observation sheet from `Day_7_Resources.md` open at 9:15. Two things:
1. **Did the trainee include a decision AND a reason?**
2. **Did the ticket carry the two timestamps and a specific next-step ask?**

## How the afternoon is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Each alert decided with a reason tied to containment · tickets carry all fields incl. reason, two times, and an ask · solution status correctly read as installed/operational/updated · the EICAR action correctly named and tied back to containment |
| **Not yet competent** | A decision with no reason · "AV found it, so detection" without checking the action · tickets missing the reason or the ask · status report that confuses installed with operational |

Full keys in `Day_7_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| A machine has third-party AV, not Defender | Its own console/status page answers the same three questions; show yours |
| `Get-MpComputerStatus` errors | Use the Windows Security app GUI — same information |
| No spreadsheet tool | Any table — a shared doc, or a printed register grid — carries the same fields |
| Real-time protection is off on a machine | Perfect — that IS a finding. Have the trainee report it |
| Activity 2 overruns | Write one ticket live, the rest → PM Task 2 |
| Behind at 11:10 | Cut 7.5 to the console idea + one Wazuh screenshot; Activity 4 → discussion |

---

## End of day checklist
- [ ] Activity 2 observation notes written up
- [ ] Tickets and status reports chased
- [ ] Outstanding still listed: Wazuh server, Day 1 lab docs, Day 5 lab-subnet scan
- [ ] Tomorrow announced: **Day 8 — manual checking and verification** (does the tool's story match the raw log?). Same hours

## What to say at the close
Today the class finished the front of the job: they decided what each alert was, wrote a ticket the next person can use, and — crucially — checked whether the tool that raised the alert was even working. They now know that "the antivirus found it" is a beginning, not an ending. Tomorrow they verify the tool's story against the raw evidence. Say that, and let them go.
