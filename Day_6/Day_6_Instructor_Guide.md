# DAY 6 — INSTRUCTOR GUIDE
## Topic: Check for Alerts — Where They Come From, and How to Read Them
### Cyber Threat Monitoring Level I · Day 06 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **Two things to know before you plan this day.**
> 1. **There is no SIEM server yet.** The class Wazuh box is not built. Day 6 runs entirely on **each trainee's own Windows machine**, using tools that are already there — Event Viewer, Microsoft Defender, and the firewall log. Nothing today needs a server. When the Wazuh box is ready, the agent-enrolment work is a half-day add-on (see the outstanding list).
> 2. **The class are complete beginners.** Assume no prior knowledge of security tools, logs, or the acronyms. Every term is defined the first time it appears. Go slowly. The demonstrations are click-by-click for exactly this reason.

---

## HOW THIS GUIDE WORKS

This is the **topic guide** — what Day 6 teaches, why, what you must know, and how each part is assessed. It is **not** a script.

Keep these files open today:

| File | What it is for |
|------|---------------|
| **`Day_6_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_6_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_6_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_6_Student_Activity_Pack.docx`** | what the trainees do — send before the session |
| **`Day_6_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_6_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_6_Resources.md`** | kit, links, printing, contingency, observation sheets |
| **`Day_6_Sample_Data.md`** | the intake scripts, the source cards, the indicator cards |

---
---

# PART A — WHAT DAY 6 IS

## The one-sentence topic

> **Day 6 is the first step of the core job: an alert arrives — from a security tool or from a person — and the analyst receives it properly, reads it on the machine it came from, and checks it for the red flags that decide how serious it is.**

## Where Day 6 sits

Days 1–5 built the ground. Day 3 gave the whole shape of the job — the six-step alert lifecycle. Day 5 taught the machine, the wire, the web and the script underneath an alert. **Day 6 starts the core unit for real.**

The core unit `CS-ICT251101` *Monitor and report cyber threats* has five elements. Day 6 delivers the **first half of Element 1, "Check for alerts":**

| Performance criterion | What Day 6 does |
|----------------------|-----------------|
| **PC 1.1** Detection alert received per SOP | Topics 6.2 and 6.4 — where alerts come from, and reading them on your own machine |
| **PC 1.2** Incident report received per SOP | Topic 6.3 — the six ways a person reports an incident, and recording it properly |
| **PC 1.3** Red flag detection checked per SOP | Topic 6.5 — ransomware and PE-infection indicators, and severity |

PC 1.4 (assess against criteria) and PC 1.5 (issue a ticket) are **Day 7**. Day 6 is receive and read; Day 7 is decide and ticket.

## What "no server" changes, and why it is fine

The 15-day plan built Phase B around a shared Wazuh SIEM. That server is not set up yet, so Day 6 uses the **Tier-1 local detection stack** the plan always kept as the fallback:

| The plan's Tier-2 (not available yet) | What Day 6 uses instead, on the trainee's own machine |
|---------------------------------------|-------------------------------------------------------|
| Wazuh dashboard, live alerts | **Event Viewer** custom views + **Microsoft Defender Protection History** |
| Wazuh rule levels 0–15 as severity | **Defender's own severity** + a written company **severity matrix** |
| Agent enrolment | *Deferred* to the first day the server is up |

This is not a downgrade for beginners — it is better. Before you hand someone a SIEM, they should see a real detection happen **on their own machine** and find it in the raw logs. That is exactly what Day 6 does with the **EICAR test file** — a completely safe file every antivirus is built to detect on purpose. When the Wazuh box arrives, the class will already understand what it is showing them.

## The five topics of Day 6

Give these at 8:00. Same wording in the handout and the activity pack.

| # | Topic title (what the trainee sees) | Primary competency | Time |
|---|-----------------------------------|-------------------|------|
| **6.1** | **The Alert Arrives** — step one of the lifecycle, in depth | `CS-ICT251101` E1 | 15 min |
| **6.2** | **Where Detection Alerts Come From** — the security tools, and what each can and cannot see | E1 PC 1.1 · knowledge 1.5 | 25 min + Activity 1 |
| **6.3** | **How Incident Reports Arrive** — the six ways a person tells you, and recording it right | E1 PC 1.2 | 15 min + Activity 2 |
| **6.4** | **Reading Alerts on Your Own Machine** — Event Viewer, Defender, the firewall log, a real EICAR detection | E1 PC 1.1 · knowledge 1.6 | 35 min + Activity 3 |
| **6.5** | **Red Flags and Severity** — ransomware and virus indicators, and how serious is it | E1 PC 1.3 · knowledge 1.9, 1.10 | 15 min + Activity 4 |

> **Say the topic number out loud when you start it.** "This is Topic 6.3."

---

## Competency map — the full picture

### Core unit — `CS-ICT251101`, Element 1 "Check for alerts"

| PC | Delivered today by | Completed? |
|----|--------------------|-----------|
| 1.1 detection alert received per SOP | 6.2, 6.4, Activity 3 (EICAR) | Substantially — repeated on Wazuh once the server is up |
| 1.2 incident report received per SOP | 6.3, Activity 2 (intake role-play) | Yes |
| 1.3 red flag checked per SOP | 6.5, Activity 4 | Yes |

**Required knowledge delivered today:** 1.5 *Sources of detection alert / incident reports* (in full), 1.6 *Log and detection management* (introduced — Event Viewer, Defender history, firewall log), 1.9 *Security solution severity classifications* (introduced via Defender severity + the company matrix), 1.10 *Malicious software behaviours* (ransomware and PE-infection indicators).

**Required skills exercised today:** computer operation, communication (heavily — the intake role-play), interpreting work instructions, interpersonal skills, and analytical skills.

### Basic and common units reprised

| Code | How it appears |
|------|---------------|
| `400311101` Receive and respond to workplace communication | Activity 2 — taking an incident report by phone/chat/email, recording it, asking clarifying questions. This is the Day 1 communication skill applied to real intake |
| `400311106` Access and maintain information | The detection record and intake forms are named and filed as evidence |

> **Still outstanding — say it out loud today:** the **Wazuh SIEM server** (agent enrolment, live dashboard, rule levels), the **Day 1 lab OSH checklist and green pledge**, and the **lab-subnet scan** from Day 5. Keep them on the list so nobody thinks they were forgotten.

---

## The 21st century design

You lecture for well under 90 of the 225 morning minutes. Four demonstrations and four activities carry the rest.

| Skill | Where | How you see it |
|-------|-------|----------------|
| **Communication** | Activity 2 "Take the Call" — you record what a stressed caller tells you | A trainee asks a caller for the one missing fact |
| **Critical thinking** | Every source's blind spot; is this a red flag or routine | A trainee says what a tool cannot see |
| **Digital literacy** | Making and finding a real Defender detection on your own machine | A trainee finds their EICAR detection in Protection History unaided |
| **Collaboration** | Activity 4 sorting indicator cards as a team | The team argues about a severity band |
| **Metacognition** | The reflection, and self-checking the intake forms | A trainee notices a field they left blank |

### The four teaching methods today

1. **Matching drill** *(Activity 1 — Name That Source)*. Fast, low-stakes, builds the vocabulary of alert sources before anything else.
2. **Role-play with observation** *(Activity 2 — Take the Call)*. A person reports an incident; the trainee receives it. This is where the communication unit is observed. It is the human half of "an alert arrives".
3. **Follow-along practical** *(Activity 3 — Make a Real Alert)*. Every trainee triggers one safe EICAR detection on their own machine and finds it in the logs. The single most memorable ten minutes of the day.
4. **Card sort** *(Activity 4 — Red Flag or Routine?)*. Teams sort indicator cards and assign severity, arguing the reasons.

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. Name the common **sources** of a detection alert, and say what each one **cannot** see.
2. **Receive an incident report** by phone, email or chat, and record it so nothing is lost.
3. Ask the right **clarifying question** when a report is missing something.
4. Find a real security event in **Event Viewer** and in **Defender Protection History**.
5. Trigger one **safe** antivirus detection on purpose, and read what the tool recorded.
6. List the **red flags** of ransomware and of a virus / PE infection.
7. Take a detection's **severity** and map it to a company severity band, with a reason.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 5 (the machine, the wire) | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics · "no server yet, we use your own machine" | Whole class | — |
| 8:15 | 15 | 3 | **Topic 6.1** The alert arrives — step one of the lifecycle | Short input | 6.1 |
| 8:30 | 25 | 4–5 | **Topic 6.2** + **Demo 1** Where alerts come from | Follow-along | 6.2 |
| 8:55 | 20 | 6 | **Activity 1** "Name That Source" | Gamified, chat | 6.2 |
| 9:15 | 15 | 7 | **Topic 6.3** How incident reports arrive | Short input | 6.3 |
| 9:30 | 30 | 8 | **Activity 2** "Take the Call" — intake role-play | Breakout pairs, observed | 6.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 20 | 9 | **Topic 6.4** + **Demo 2** Reading your own logs | Follow-along | 6.4 |
| 10:30 | 15 | 10 | **Demo 3** Make a real alert (EICAR) — trainer shows | Demonstration | 6.4 |
| 10:45 | 25 | 11 | **Activity 3** "Make a Real Alert" — trainees do it | Follow-along | 6.4 |
| 11:10 | 15 | 12–13 | **Topic 6.5** + **Demo 4** Red flags and severity | Follow-along | 6.5 |
| 11:25 | 13 | 14 | **Activity 4** "Red Flag or Routine?" | Breakout teams | 6.5 |
| 11:38 | 7 | 15 | Afternoon brief · how it is marked · close | Whole class | — |

**Total lecture time is well under 90 minutes.** Morning sums to 225 (8:00 → 11:45).

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 35 minutes, submitted by 4:00.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Intake practical — process 6 incident reports across ≥4 channels | 30 | 6 completed intake forms |
| 2 | The detection record — trigger/confirm one Defender detection, record it as an alert | 25 | 1 detection record |
| 3 | Read your own logs — find and log 3 real security events | 25 | Event log worksheet |
| 4 | Build the sources reference — 7 sources, what each sees and its blind spot | 20 | Sources reference table |
| 5 | Red-flag indicator cards — ransomware + PE infection | 25 | 2 indicator cards |
| 6 | Severity mapping sheet — detection severity → company band, with reasons | 20 | Severity mapping sheet |
| 7 | Reflection | 10 | Three answers |

> **Task 2 depends on Defender being on.** If a trainee's machine is managed and blocks the EICAR file, the **block itself is the detection** — they record what Protection History shows. Nobody is stuck. The by-hand fallback is in the Solutions.

---

## Before the day

### The night before
- [ ] **Run every demonstration once, on your own machine.** The EICAR demo especially — see exactly what Defender does on your build
- [ ] Confirm you can open Event Viewer and see the **Windows Defender / Operational** log
- [ ] Create the EICAR file once yourself, watch Defender catch it, then check Protection History — so you know the exact wording your class will see
- [ ] Take the fallback screenshots in `Day_6_Resources.md`
- [ ] Have the intake scripts from `Day_6_Sample_Data.md` ready — you will read them aloud in Activity 2

### On the morning
- [ ] Breakout rooms created and named
- [ ] Activity Pack, Handout, Resources sent with the joining note
- [ ] Intake scripts and source cards ready to send privately
- [ ] Chat open — Activity 1 runs through it
- [ ] Collect outstanding Day 1–5 evidence in the first fifteen minutes

> **Roles rotate today.** Announce at 8:00.

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 6.1 — THE ALERT ARRIVES
### 8:15–8:30 · 15 minutes · Slide 3 · `CS-ICT251101` E1

### The point
Reconnect to the Day 3 six-step lifecycle, then zoom all the way in on **step 1: it arrives.** Today and tomorrow are step 1 done thoroughly — everything else in the unit depends on receiving the alert properly.

### What you must know
An alert reaches an analyst in one of two ways, and the CS names both:
- **A detection alert** — a security *tool* saw something and raised it (PC 1.1).
- **An incident report** — a *person* told you something (PC 1.2).

Both must be **received per the company SOP** — meaning recorded the same way every time, so nothing is lost and the next analyst can pick it up. "Received per SOP" is the phrase the assessor looks for.

### Key messages
- Every alert is either a machine telling you or a person telling you. Both count. Both must be written down the same way.
- "I remember someone mentioned it" is not receiving an alert. Receiving it means it is **recorded**.
- Today you learn to receive both kinds. Tomorrow you decide what they are and raise a ticket.

### Mistakes to expect
- Trainees think only tool alerts are "real". A phone call from a panicking user is an alert too, and often the most important one.

---

## TOPIC 6.2 — WHERE DETECTION ALERTS COME FROM
### 8:30–8:55 · 25 minutes · Slides 4–5 · Demo 1 · knowledge 1.5

### The point
Give beginners the map of security tools that raise alerts, and — the analyst's habit — what each one **cannot** see.

### What you must know
The CS range for "detection alert" names these sources. Define each in one plain line:

| Source | Full name | What it watches | What it cannot see |
|--------|-----------|-----------------|--------------------|
| **SIEM** | Security Information & Event Management | Logs from everywhere, in one place | Only what it is fed; a source not sending logs is invisible |
| **AV** | Antivirus | Files and programs on a machine | A brand-new threat no one has caught yet |
| **Firewall** | — | Traffic in and out of the network | What happens *inside* an allowed connection |
| **WAF** | Web Application Firewall | Requests to a website | Attacks that do not go through the web app |
| **DLP** | Data Loss Prevention | Sensitive data leaving the company | Data it was never told to watch for |
| **EDR** | Endpoint Detection & Response | Behaviour on a computer (an advanced AV) | A machine with no agent installed |
| **NDR** | Network Detection & Response | Suspicious patterns on the network | Encrypted content it cannot read |

The point that ties it to Day 3: **every source has a blind spot**, exactly like every lookup website did.

### Key messages
- These are just tools with different jobs. AV watches files. Firewall watches traffic. EDR watches behaviour. A SIEM collects them all.
- You do not need to operate these tools today. You need to know which one an alert came from, and therefore what it can and cannot tell you.
- We do not have a SIEM server yet, so today the "tool" raising your alerts is **Microsoft Defender**, the antivirus already on your machine.

### Mistakes to expect
- Trainees blur AV and EDR. Keep it simple: EDR is AV that also watches *behaviour* over time, and reports back to a central console.
- Trainees assume a tool sees everything. Name the blind spot every time.

---

## TOPIC 6.3 — HOW INCIDENT REPORTS ARRIVE
### 9:15–9:30 · 15 minutes · Slide 7 · `CS-ICT251101` E1 PC 1.2

### The point
Half of all alerts come from **people**, not tools, and the CS lists six channels. Receiving a report well is a communication skill — the Day 1 skill, now on the job.

### What you must know
The CS range for "detection report": **phone call, walk-in, email, SMS, chat, video conference.** Whichever channel, the analyst must capture the same core facts:

| Capture | Why |
|---------|-----|
| **Who** is reporting, and how to reach them back | You will need to verify results later (Day 9) |
| **What** they saw or experienced, in their words | Their words matter — do not translate too early |
| **When** it happened, and when they noticed | The gap is often the key fact |
| **Which machine / account / system** | Nothing can be done without knowing where |
| **What they have already done** | So you do not undo it or repeat it |

The clarifying question is the skill: when a report is missing one of these, you **ask**, calmly, before hanging up.

### Key messages
- A user rarely uses the right words. "The internet is broken" might be ransomware. Your job is to record what they said **and** ask the questions that fill the gaps.
- Write it down as they speak. Memory is not receiving an alert.
- Stay calm. A panicking caller calms down when the person on the line is calm.

### Mistakes to expect
- Trainees argue with or correct the caller. Don't. Record first, clarify gently, judge later.
- Trainees forget to get a callback number. It is the one field you cannot reconstruct afterwards.

---

## TOPIC 6.4 — READING ALERTS ON YOUR OWN MACHINE
### 10:10–11:10 · 60 minutes with Demos 2–3 and Activity 3 · Slides 9–11 · knowledge 1.6

### The point
This is the heart of the day. Beginners see, on their own machine, where security events are recorded — and they make a **real, safe detection happen** and find it.

### What you must know
Three places every Windows machine records security events, all free, all already there:

| Place | What is in it | How to open it | Needs admin? |
|-------|---------------|----------------|--------------|
| **Event Viewer** | Windows logs: System, Security, and the **Windows Defender / Operational** log | `eventvwr.msc` | The **Security** log needs admin; **Defender Operational** and System usually do not |
| **Defender Protection History** | Every threat Defender found and what it did | Windows Security app → Protection history | No |
| **Firewall log** | Blocked/allowed connections, if logging is on | `%systemroot%\system32\LogFiles\Firewall\pfirewall.log` | Reading the file: usually yes |

**The EICAR test file** is the safe way to make a detection. It is a harmless text string that every antivirus is *designed* to detect, so people can test AV without real malware. When a trainee creates it, Defender catches it instantly, and it appears in Protection History and in the Defender Operational log (event **1116** = detected, **1117** = action taken). That is a real detection alert, start to finish, with nothing dangerous involved.

> **Beginner watch-outs, and the fallbacks:**
> - On a managed machine Defender may block *creating* the file at all. **That block is the detection** — go straight to Protection History.
> - If the Security log is locked (no admin), use the **Defender Operational** log and Protection History, which do not need admin.
> - If Defender is replaced by another AV, that AV's own history is the equivalent — show yours, let them find theirs.

### Key messages
- You just made a security tool raise an alert, on purpose, safely. That is exactly what happens on a real desk — except the file is real, and you did not create it.
- The tool tells you three things: **what** it found, **when**, and **what it did about it**. Write those three down. That is your detection record.
- Zero threats in your history does not mean you are safe. It means nothing has been *caught*. (The Day 3 lesson, again.)

### Mistakes to expect
- Trainees panic that they "downloaded a virus". Reassure firmly: EICAR is not and has never been malware. It is a test string.
- Trainees cannot find Protection History. Walk them: Start → "Windows Security" → Virus & threat protection → Protection history.

---

## TOPIC 6.5 — RED FLAGS AND SEVERITY
### 11:10–11:38 · with Demo 4 and Activity 4 · Slides 12–14 · knowledge 1.9, 1.10 · E1 PC 1.3

### The point
"Checking the red flag" (PC 1.3) means knowing the indicators that make an alert serious. The CS names two red-flag categories, and the analyst must know each.

### What you must know
The CS names **ransomware** and **PE infection / virus** as the red-flag detections. The indicators, at beginner depth:

| Red flag | Indicators an analyst can recognise |
|----------|-------------------------------------|
| **Ransomware** | Many files renamed or with a new extension at once · a ransom note file (e.g. `README.txt`) in many folders · files that will not open · sudden spike in file changes · backups being deleted |
| **PE infection / virus** | A program file (`.exe`, `.dll`) flagged by AV · a process running from the wrong place (Day 5!) · a file that copies itself · a name pretending to be a system file (`svhost32.exe`) |

*(PE = Portable Executable, the format of Windows `.exe` and `.dll` files. Say it once.)*

**Severity**, at L1 depth: the tool gives a severity (Defender uses **Low / Moderate / High / Severe**). A future SIEM like Wazuh uses **rule levels 0–15**. Either way, the analyst maps the tool's severity onto the **company's own severity band** and its required response time. Today the class writes/uses a simple company matrix:

| Company band | Meaning | Example |
|--------------|---------|---------|
| **Critical** | Business-stopping, act now | Ransomware spreading; a server down |
| **High** | Serious, act within the hour | Confirmed malware not yet contained |
| **Medium** | Real, act this shift | A single blocked malware file |
| **Low** | Note it, no rush | A blocked ad / PUA |

### Key messages
- Red flags are patterns you can learn. Ransomware looks like ransomware. A fake system-file name looks wrong (you learned that on Day 5).
- The tool's severity is a starting point, not the final word. **You** map it to what it means for this company.
- Severity is about *how fast and how loud*, not about whether it is real.

### Mistakes to expect
- Trainees treat the tool's severity as the answer. It is an input. A "Low" from the tool on the CEO's laptop may be your High.
- Trainees confuse severity with the threat/detection/routine decision. Severity = how serious. Threat/detection/routine (Day 7) = what it is and whether it is contained.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 6 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 6 completed intake forms across ≥4 channels | PM Task 1 + Activity 2 | E1 PC 1.2 · `400311101` |
| 1 detection record from a real EICAR detection | PM Task 2 + Activity 3 | E1 PC 1.1 |
| Event log worksheet — 3 real events found and logged | PM Task 3 | knowledge 1.6 |
| Sources reference table — 7 sources + blind spots | PM Task 4 + Activity 1 | knowledge 1.5 |
| Two red-flag indicator cards (ransomware, PE infection) | PM Task 5 + Activity 4 | E1 PC 1.3 · knowledge 1.10 |
| Severity mapping sheet | PM Task 6 | knowledge 1.9 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

## Observation during the live session

**Activity 2 "Take the Call" is observed.** Have the observation sheet from `Day_6_Resources.md` open at 9:30. Two things:
1. **Did the trainee record the core facts** (who, what, when, where, callback) without being prompted for each?
2. **Did they ask a clarifying question** when the report was missing something, calmly?

## How the afternoon is marked

**The reason matters more than the answer** — the Day 3 rule holds. For the intake forms, a missing callback number or a blank "which machine" is not competent even if the rest is neat. For the severity sheet, a band with no reason is not competent.

| Band | What it looks like |
|------|-------------------|
| **Competent** | Intake forms capture all core facts · the detection record names the source, time, what was found and the action · red-flag cards list real indicators · each severity mapped with a reason |
| **Not yet competent** | Intake forms missing core fields · a detection record that just says "found a virus" · indicator cards that are vague ("looks bad") · severity with no reason |

Full keys and bands are in `Day_6_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| A trainee's Defender blocks the EICAR file entirely | That block **is** the detection — record it from Protection History |
| A machine uses third-party AV, not Defender | Use that AV's own detection history; the skill is the same |
| No admin, Security log locked | Use the Defender Operational log and Protection History — no admin needed |
| A trainee is frightened by "making a virus" | Reassure: EICAR is a harmless test string, not malware, never was |
| Activity 2 overruns | Run three intake scripts instead of all six; the rest move to PM Task 1 |
| Whole class is remote with poor connection | Everything today is local to each machine — no server, no bandwidth needed after the joining note |
| You are behind at 11:10 | Cut Topic 6.5 live to the two red flags only; Activity 4 and PM Tasks 5–6 carry severity |

---

## End of day checklist
- [ ] Activity 2 observation notes written up
- [ ] Intake forms and detection records chased
- [ ] Outstanding items still on the list: **Wazuh server**, Day 1 lab OSH checklist + green pledge, Day 5 lab-subnet scan
- [ ] Tomorrow announced: **Day 7 — decide what the alert is, raise the ticket, and check the security tool is actually working.** Same blended hours

## What to say at the close
Today the class received alerts the two ways alerts really arrive — from a tool and from a person — and made a real detection happen on their own machine. They did it with no server and no danger. Tomorrow they decide what those alerts *are*, and write the ticket. Say that, and let them go.
