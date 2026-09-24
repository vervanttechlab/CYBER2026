# DAY 10 — INSTRUCTOR GUIDE
## Topic: Report the Threat — Notify, Trace It, Name It, Write It Up · then the Unit Assessment
### Cyber Threat Monitoring Level I · Day 10 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led, 8:00–11:45 AM · **Institutional assessment for `CS-ICT251101`, 1:00–4:00 PM, online synchronous with cameras on**

> **Same two conditions as Days 6–9.** (1) **No SIEM server yet.** The report is built from a paper evidence set (Sample Data §3). Ingress and egress are read on the trainee's own machine. ATT&CK Navigator runs in the browser and needs no server. (2) **Total beginners.** Assume nothing, show every click, and keep a calm pace.

> **Why the afternoon is not asynchronous today.** Days 5–9 ran the afternoon as self-study. Today it cannot. The CS assesses this unit through **demonstration with oral questioning, a written exam, and a portfolio with interview**. The demonstration and the oral questions have to be **observed live**. This is the same reason Day 1 put observed work in the live morning. The afternoon is therefore **synchronous** from 1:00 to 4:00, on the same hours, and everything in it is set out in `Day_10_Unit_Assessment_Guide.md`.

---

## HOW THIS GUIDE WORKS

This is the **topic guide**: what Day 10 teaches, why, what you must know, and how it is assessed. It is not a script. Keep these files open:

| File | For |
|------|-----|
| **`Day_10_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_10_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_10_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_10_Student_Activity_Pack.docx`** | what the trainees do in the morning |
| **`Day_10_Solutions.docx`** | answer keys and marking bands for the morning (trainer only) |
| **`Day_10_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_10_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_10_Sample_Data.md`** | the notification cases, the 18-line evidence set, the ATT&CK behaviours, the templates |
| **`Day_10_Unit_Assessment_Guide.md`** | **the afternoon**: the assessment plan, rules, all four instruments, the keys, the result sheet (trainer only) |
| **`Day_10_Written_Exam.docx`** | candidate paper, released at **1:10 PM**, not before |
| **`Day_10_Practical_Assessment_Brief.docx`** | candidate brief and case data, released at **2:00 PM**, not before |

---
---

# PART A — WHAT DAY 10 IS

## The one-sentence topic

> **The SRV-BAK-02 case began on Day 7 as one failed quarantine. Today it turns out that data left the building. The analyst warns the owners within ten minutes, traces where the threat went and what crossed the boundary in each direction, names how it got in and how it stays, and writes it all into one threat report. Then the first unit is assessed.**

## Where Day 10 sits

Day 10 delivers all of **Element 5** of the core unit, *Perform alert reporting*, and then assesses the whole unit:

| Element / PC | What Day 10 does |
|--------------|------------------|
| **E5 PC 5.1** Stakeholder / client with high and critical threats are notified | Topic 10.1: the ten-minute notification, by voice and in writing, and who is **not** notified |
| **E5 PC 5.2** Activity of the threats reported based on the spread and lateral movement | Topic 10.2: the hosts table (origin / confirmed / attempted / not linked) and the path |
| **E5 PC 5.3** Activity of the threats reported based on egress and ingress | Topic 10.3: what came in, what went out, and how much, on paper and on their own machine |
| **E5 PC 5.4** Threats identified based on exploitation activity and installation behaviour | Topic 10.4: how they got in, how they stay, and mapping both to MITRE ATT&CK in Navigator |
| **The whole of `CS-ICT251101`** | 1:00–4:00: written exam, demonstration with oral questioning, portfolio with interview |

After today, `CS-ICT251101` is complete. **Day 11** begins the second core unit, `CS-ICT251102` *Conduct vulnerability scanning*.

## What "no server" changes

| Plan's bench (not used today) | Day 10 uses instead |
|-------------------------------|---------------------|
| Wazuh MITRE ATT&CK module (the mapping arrives attached to the alert) | **Mapping by hand** from plain-words behaviours to IDs, checked on `attack.mitre.org`, then **ATT&CK Navigator in the browser** with the layer exported as JSON. Both run with no server |
| Atomic Red Team tests in Windows Sandbox (lateral movement, exfiltration, persistence) | **The paper evidence set** (Sample Data §3). It shows the same behaviours as log lines. Atomic Red Team stays on the outstanding list |
| Get-NetTCPConnection and TCPView | **`Get-NetTCPConnection` on their own machine**, which is built in. TCPView is preview only |
| The Hayabusa timeline as the narrative spine | **The 18-line evidence set is written as that timeline** |

## The five topics of Day 10

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **10.1** | **Tell Them in Ten Minutes**: the High / Critical notification | E5 PC 5.1 | 20 min + Activity 1 |
| **10.2** | **Where Did It Go?**: spread and lateral movement | E5 PC 5.2 | 25 min + Activity 2 |
| **10.3** | **What Came In, What Went Out**: ingress and egress | E5 PC 5.3 | 20 min (follow-along) |
| **10.4** | **How It Got In, How It Stays**: exploitation, installation, ATT&CK | E5 PC 5.4 · knowledge 5.3 | 25 min + Activity 3 |
| **10.5** | **The Threat Report**: one document, every claim on a line of evidence | E5 all · skill 5.2 | 10 min + Activity 4 |

---

## Competency map

### Core unit: `CS-ICT251101`, delivering Element 5, then assessed

**Required knowledge today:** 5.1 *Malicious software behaviours* (download, masquerade, persist, move, beacon, send out), 5.2 *Threats*, 5.3 *Knowledge in attack framework* (ATT&CK tactics and techniques, Navigator).

**Required skills today:** communication (the notification: two audiences, one ten-minute clock), analytical (linking hosts **only with evidence**), interpreting work instructions (the severity matrix decides who is notified), computer operation (`Get-NetTCPConnection`, Navigator), interpersonal (a Critical call to a worried owner).

### Basic and common units reprised

| Code | How it appears |
|------|---------------|
| `400311101` Receive and respond to workplace communication | **LO1 spoken**: the notification call with read-back. **LO2 written**: the written notification and the report |
| `400311102` Work with others | The report is written for the people who act next (IT, the security manager, the owners) |
| `ICT315202` Apply quality standards | The report rule: every claim points to an evidence line. Self-checked in Activity 4 |
| `400311106` Access and maintain information | The report, the layer JSON and the evidence filed in `Evidence/Day_10/`. The portfolio is assembled for the interview |

> **Still outstanding: say it at 8:00.** The **Wazuh SIEM server** · the **Day 1 lab OSH checklist and green pledge** · the **Day 5 lab-subnet scan** · **Windows Sandbox and Atomic Red Team** (Day 8) · **Hayabusa, DeepBlueCLI and Timeline Explorer** (Day 9). Add today: **TCPView** and the **Wazuh ATT&CK module** (preview only). **None of these is required for the unit assessment.** The assessment is built on what the class has actually done.

---

## The idea that anchors the whole day

> **Link with evidence, not with the clock.**

SRV-FIN-02 was encrypted at 03:40 on 15 Sep, the same minute SRV-BAK-02's quarantine failed. Beginners will put it in the same case. The evidence says otherwise: a different account, a different source address, a different file, and no connection to the anonymising address (line E17). **Two things that happen at the same time are not one case until a line of evidence joins them.** The line that *does* join WKS-311 and SRV-BAK-02 is **E16**, the same file hash on both, together with E07–E10, logons and a file copy coming *from* `.31`.

Two sentences run the morning:
- **To the owner:** "This is a Critical notification. Here is what is known, here is what you must not do, and I will update you at <time>." *Fast beats complete.*
- **In the report:** "Every sentence here points to a line." *A claim without a line is an opinion (Day 9).*

---

## What a trainee can do at 11:45 AM that they could not at 8:00 AM

1. **Notify** the owner of a High or Critical threat within the clock, by voice and in writing, including what they must **do and not do**, and say who is **not** notified and why.
2. List every host in an incident as **origin, confirmed, attempted or not linked**, and draw the **lateral-movement path** with the method, account, time and line.
3. Separate **ingress** from **egress**, with direction, address, time and **bytes**, and read both on their own machine.
4. Name the **exploitation activity** and the **installation behaviour**, and map each to an **ATT&CK** technique ID in **Navigator**.
5. Assemble a **threat report** in which every claim points to an evidence line.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning: online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 9 · collect the portfolio checklist | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics · the shape of the day (learn, then be assessed) | Whole class | — |
| 8:15 | 20 | 3 | **Topic 10.1** + **Demo 1**: read §1, then the N1 Critical notification | Demonstration | 10.1 |
| 8:35 | 20 | 4 | **Activity 1** "Ten Minutes": N2 in pairs, then decide on N3 | Breakout pairs, observed | 10.1 |
| 8:55 | 25 | 5 | **Topic 10.2** + **Demo 2**: where did it go? Hosts table and path | Follow-along | 10.2 |
| 9:20 | 20 | 6 | **Activity 2** "Draw the Path" | Breakout teams | 10.2 |
| 9:40 | 20 | 7–8 | **Topic 10.3** + **Demo 3**: ingress and egress, own machine, then the evidence | Follow-along | 10.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 25 | 9–10 | **Topic 10.4** + **Demo 4**: exploitation, installation, ATT&CK Navigator | Follow-along | 10.4 |
| 10:35 | 20 | 11 | **Activity 3** "Name It, Map It": map, then build and export your own layer | Teams, then individually | 10.4 |
| 10:55 | 10 | 12 | **Topic 10.5**: the report · **Demo 5** preview | Short input | 10.5 |
| 11:05 | 25 | 13 | **Activity 4** "Assemble the Report" | Individually | 10.5 |
| 11:30 | 15 | 14–15 | How the assessment works · this afternoon · close | Whole class | — |

The morning sums to 225 minutes (8:00 → 11:45). Lecture time is about 90 minutes.

### Afternoon: the unit assessment, 1:00 to 4:00 PM (synchronous, cameras on)

| Time | Min | What | Evidence guide |
|------|-----|------|----------------|
| 1:00 | 10 | Assessment briefing, candidate agreement, rules, appeals | — |
| 1:10 | 40 | **Written exam**: 25 multiple-choice + 5 short answer | Knowledge 1.1–5.3 |
| 1:50 | 10 | Break | — |
| 2:00 | 90 | **Demonstration**: Case WKS-164, four parts, on their own machine and on forms · **oral questioning and portfolio interview** in individual breakouts, running alongside | Critical aspects 1.1–1.5 |
| 3:30 | 20 | Remaining oral questions and portfolio interviews · candidates finish and submit | 1.1–1.5 |
| 3:50 | 10 | Close: what happens next, when results come, reassessment | — |

Everything for the afternoon (rules, instruments, keys, observation checklist, oral bank, result sheet) is in **`Day_10_Unit_Assessment_Guide.md`**.

### The morning report and the afternoon assessment are different evidence

The morning's threat report is **learning evidence**. It is submitted at 11:45 as it stands and goes into the portfolio. **Element 5 is assessed in the afternoon** on a *new* case (WKS-164), so that the assessment shows the trainee can do it on something they have not rehearsed. Say this at 11:30 so no one spends lunch polishing the morning report.

---

## Before the day
### The night before
- [ ] Read Sample Data §1–§3 twice. You must be able to tell the SRV-BAK-02 story from E01 to E18 without notes
- [ ] Rehearse Demo 1, the N1 call, aloud. Decide whether a co-host plays R. Santos
- [ ] Open ATT&CK Navigator on the machine you will present from. Build the B1–B3 layer once and export it (Demo 4)
- [ ] Run the four Sample Data §7 commands on your own machine. Pick **one** egress line and **one** listening port you will talk about
- [ ] Take the fallback screenshots in `Day_10_Resources.md` Part 3
- [ ] **Assessment:** print or open the Assessment Guide. Check the two candidate files are **not** in the joining note. Set up the online form or shared folder for the written exam and the practical submission (Assessment Guide Part 2)
- [ ] Update the register: SRV-BAK-02 row with *Isolated 17 Sep 11:26*, WKS-311 row with *Isolated 17 Sep 11:40*

### On the morning
- [ ] Breakout rooms: pairs for Activity 1, teams for 2 and 3
- [ ] Handout, Activity Pack and Resources sent. **Not** the exam or the brief
- [ ] Observation sheet (Resources Part 5) open at 8:35
- [ ] Collect the **portfolio checklist** (Handout, last page) from each trainee by 8:10. Anyone missing items has until 12:45

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 10.1 — TELL THEM IN TEN MINUTES
### 8:15–8:55 with Demo 1 and Activity 1 · Slides 3–4 · E5 PC 5.1

### The point
A High or Critical threat is **notified to the owner** fast, before the full picture is known. It is the third kind of message this week, and trainees must keep the three apart.

### What you must know
Read Sample Data **§1** aloud first. The **11:29** line (1.8 GB left) moves the case into Critical ("data leaving" on the Day 6 matrix), and the clock starts.

**The three messages** (Sample Data §2 table):

| Message | To | About |
|---------|----|-------|
| **Verification** (Day 9) | The client | A scan **result** |
| **Escalation** (Day 9) | An authority | A **failure**, for a decision or an action |
| **Notification** (today) | The **owner** of the affected system or data | A **High / Critical threat**, so they can protect what is theirs |

**The seven lines of the call** (§5), and the **written notification** within the hour. Two things set a notification apart: the **"do / do not"** line (R. Santos: *do not reconnect, do not use svc_backup, do not restore from anything after 14 Sep 16:51*), and "based on what is known at <time>, **it will be updated**".

**Who is notified.** N1 R. Santos, Critical. N2 J. Mendoza, High. **N3, the owner of SRV-FILE-01, is not notified**: an attempt that failed is Medium, and it goes in the report. The PC says *high and critical*. Teach the discipline: someone who notifies everyone about everything soon gets ignored.

### Key messages
- **Fast beats complete.** Send what is known now, and say it will be updated.
- **Tell them what to do.** A notification with no "do / do not" is only news.
- **Only High and Critical** are notified. Medium and Low go in the report.

### Mistakes to expect
- Trainees wait for the whole report before notifying. Ask: "What time is it, and when did the clock start?"
- The N1 call turns into a technical briefing (event IDs, hashes). R. Santos needs the **what, since when, and what not to do**.
- Trainees blame the user on the N2 call ("your staff member opened a virus"). Stop it. The call is about protecting the team. Blame is not the analyst's job, and it makes people hide the next mistake.
- Everyone notifies N3 "to be safe". Take them back to the PC's wording and the matrix.

---

## TOPIC 10.2 — WHERE DID IT GO?
### 8:55–9:40 with Demo 2 and Activity 2 · Slides 5–6 · E5 PC 5.2

### The point
PC 5.2 names two things. **Spread** is *which hosts, and how far*. **Lateral movement** is *how it got from one to the next*. Both are reported from evidence.

### What you must know
**The four words for a host** (the hosts table, report section 4):

| Word | Means | In this case |
|------|-------|--------------|
| **Origin** | Where it started inside the network | WKS-311 (E02–E05) |
| **Confirmed** | Evidence the threat is running or was placed there | SRV-BAK-02 (E08, E10–E12, E16) |
| **Attempted** | Tried, and the evidence shows it failed | SRV-FILE-01 (E09: 12 × 4625, no 4624) |
| **Not linked** | Suspected, checked, and no evidence joins it | SRV-FIN-02 (E17) |

**The path** (report section 5): **WKS-311 → SRV-BAK-02**, over **SMB (445) to the ADMIN$ share**, using **svc_backup** after **38 guessed passwords**, at **03:33–03:39 on 15 Sep**, lines **E07, E08, E10, E11**. Say each part aloud: *from, to, method, account, time, line*.

**Logon types**, at L1 depth: **type 3 = network** (a share, a remote command). **Type 10 = remote desktop.** That difference is part of why SRV-FIN-02 is a separate case: its logon was type 10, from the VPN, as fin_admin.

### Key messages
- **Link with evidence, not with the clock.** SRV-FIN-02 was hit in the same minute and is still not linked.
- **"Attempted" is a finding.** Twelve failed logons tell the report where the attacker *tried* to go.
- The strongest link is **the same file hash** on two machines (E16).

### Mistakes to expect
- SRV-FIN-02 goes into the path "because it was 03:40". Ask: "Which line joins them?"
- SRV-FILE-01 is marked "infected" because it appears in the log. Failed logons are **attempted**, not confirmed.
- Trainees read E08 as the attacker logging on *from outside*. The source is `192.168.10.31`, an **inside** address. That is what makes it *lateral*.

---

## TOPIC 10.3 — WHAT CAME IN, WHAT WENT OUT
### 9:40–10:00 with Demo 3 · Slides 7–8 · E5 PC 5.3

### The point
**Ingress** is what came **in** across a boundary. **Egress** is what went **out**. The report states each one with direction, address, time, and **how much**.

### What you must know
**Direction is decided by who started it**, which is the local and remote port logic from Day 5. The firewall line says `OUT` when the inside host started the connection, even though bytes flowed both ways.

| | Ingress (in) | Egress (out) |
|---|---|---|
| **In this case** | E01 the email and its attachment · E03 **1.2 MB** pulled in from `203.0.113.45` · E10 the tool copied **into** SRV-BAK-02 from `.31` (internal) | E06 / E13 beacons every ~5 min to `185.220.101.1:443` · E14 **1.8 GB** out in one session |
| **The trap** | E18: **no** inbound connection from the internet. Everything was started from the inside | E03 is an `OUT` connection that brought a file **in**. That is ingress of a **tool**, carried by an egress connection |

**Bytes tell the story.** A beacon sends about 2 KB. A backup file sends 1.8 GB. `bytes_out` far bigger than `bytes_in` is the shape of **data leaving**.

**On their own machine** (Sample Data §7): Established with remote port 443 is egress, and Listen is a possible door in. Their machine will show dozens of normal 443 connections. The skill is **reading direction**, not finding something bad.

### Key messages
- Who started it decides the direction. Bytes decide how serious it is.
- A tiny, regular, repeated connection is a **beacon**. One huge one-way connection is **data leaving**.
- "No inbound from the internet" is a finding too. It tells the reader the attacker came in by email, not through an open port.

### Mistakes to expect
- E03 recorded as egress only. Ask: "What came into the building on that connection?"
- Trainees alarmed by their own 443 connections. Most are Microsoft, the browser, or cloud sync. Show `Get-Process -Id` naming them.
- Confusing Listen with "being attacked". Listening is a door, not a visitor.

---

## TOPIC 10.4 — HOW IT GOT IN, HOW IT STAYS
### 10:10–10:55 with Demo 4 and Activity 3 · Slides 9–11 · E5 PC 5.4 · knowledge 5.3

### The point
PC 5.4 asks for two things. **Exploitation activity** is *how they got in, and how they got more access*. **Installation behaviour** is *what they left behind so it keeps running*. ATT&CK gives each one an agreed name and ID.

### What you must know
**Exploitation activity**, at L1 depth, is anything the attacker did to make a system do what they wanted:
- **WKS-311:** the user was tricked into running a macro (E01–E02). *No software vulnerability was exploited on this evidence.* Say that precisely. It matters for the recommendation: user training and macro blocking, not a patch.
- **SRV-BAK-02:** 38 passwords guessed against svc_backup, then a success (E07–E08). The "exploit" was a **weak password on a service account**.

**Installation behaviour**, what makes it survive:
- **E05:** a scheduled task at every logon (the Day 3 technique, T1053.005, now on a real case).
- **E11:** a **Windows service**, auto-start, **restart after every failure**. *This is why the process "restarted itself within 4 seconds" on Day 9, and why the quarantine kept failing.* Tie the whole case together here.
- **E10:** the tool was copied in first.

**ATT&CK: tactic versus technique.** The **tactic** is the attacker's *goal* (the column: Persistence, Lateral Movement). The **technique** is the *method* (the box, with the ID). The twelve behaviours and their IDs are in Solutions. Demo 4 maps B1–B3 live in **Navigator**: create layer, search, select, colour, comment, download JSON.

### Key messages
- Exploitation is how they got in. Installation is how they stay. Both are needed to clean up properly.
- The service with auto-restart explains the Day 9 failures. **The report connects the days.**
- ATT&CK names the behaviour. **You still need the line that proves it** (Day 3: it cannot confirm *this* event is that technique).

### Mistakes to expect
- "Exploitation" read only as "a software exploit". Widen it: tricking a user or guessing a password is also how they got in.
- Tactic and technique swapped. Point at the column (why) and the box (how).
- Navigator: the sub-technique cannot be found. Use search by ID, or the expand-sub-techniques button.
- A whole team stuck on Navigator. Switch them to the paper table. The mapping is the skill and the JSON can follow.

---

## TOPIC 10.5 — THE THREAT REPORT
### 10:55–11:30 with Demo 5 and Activity 4 · Slides 12–13 · E5 all

### The point
One document that carries all four PCs, written for the people who act next. It has fifteen sections, and the rule is that **every claim points to a line**.

### What you must know
The template is in Sample Data §6. Sections **3–10** carry the four PCs. By 11:05 the trainees have already produced most of it: Activity 1 gives section 3, Activity 2 gives sections 4–5, Demo 3 gives sections 6–7, and Activity 3 gives sections 8–10. Activity 4 is **assembly**, plus the summary, the timeline, **what we do not know yet**, and the recommendations.

**Section 13, "What we do not know yet"**, is where beginners are most honest and most useful: how the macro passed the email gateway, whether svc_backup is used on other servers, what else was in the 1.8 GB, and whether `OneDriveSyncHelper` or `WinHostSvc` exists on any other host.

**Demo 5 preview**, two minutes, screenshots only: the **Wazuh ATT&CK module** (the mapping arrives already attached to the alert), **Atomic Red Team** (safe tests that *make* these behaviours happen in a sandbox so detections can be tested), and **Hayabusa** (the timeline you read by hand today). *Same report, same rule.*

### Key messages
- The report is the case, told once, in order, with its evidence.
- "What we do not know yet" is not a weakness. It tells the next person where to look.
- A recommendation is a verb, an owner and a date (Day 9's ask, carried over).

### Mistakes to expect
- A report that retells the story with no line numbers. Send them back to §3.
- SRV-FIN-02 put in the report as part of the incident. It belongs in section 4 as **not linked**, with E17.
- Recommendations like "improve security". Push for the verb: re-image SRV-BAK-02 and WKS-311 · block `203.0.113.45` and `185.220.101.1` · change svc_backup to a long password and stop it logging on over the network · block macros from internet email · search every host for `OneDriveSyncHelper` and `WinHostSvc`.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What the morning produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 1 written notification (N2) + call notes, and the N3 decision with its reason | Activity 1 | E5 PC 5.1 · `400311101` LO1–LO2 |
| Hosts table + lateral-movement path | Activity 2 | E5 PC 5.2 |
| Own-machine ingress / egress record | Demo 3 (follow-along) | E5 PC 5.3 |
| ATT&CK mapping table + **Navigator layer (JSON)** | Activity 3 | E5 PC 5.4 · knowledge 5.3 |
| **1 threat report** (draft or complete) on SRV-BAK-02 | Activity 4 | E5 PC 5.1–5.4 |

These match the plan's evidence: **1 complete threat report, 1 ATT&CK Navigator layer**. A report that is still a draft at 11:45 is accepted as portfolio evidence and can be finished by the end of Day 11.

## Observation during the live session

**Activity 1 "Ten Minutes" is observed** on the N2 call. Two things:
1. **Did they state the severity with its reason, what is known, and a specific "do / do not"?**
2. **Did they give one ask, a next-update time, and get a read-back, without blaming the user?**

This is practice for the assessed notification this afternoon. Give feedback in the room.

## How the morning is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Notification with severity + reason, "do / do not", an ask, a next-update time; N3 not notified, with the reason · every host placed as origin / confirmed / attempted / not linked with a line · the path given as from → to, method, account, time, line · ingress and egress separated, with bytes · exploitation and installation named and mapped to IDs · the report's claims point to lines |
| **Not yet competent** | A notification that is a technical dump, or has no "do / do not" · SRV-FIN-02 linked "because of the time" · SRV-FILE-01 called infected · ingress and egress mixed up, no bytes · techniques with no evidence line · a report that retells the story with no lines |

Full keys in `Day_10_Solutions.docx`.

## The afternoon: the unit assessment (summary)

| Method (from the CS) | Instrument | Covers |
|----------------------|-----------|--------|
| **Written exam** | 25 multiple-choice + 5 short answer, 40 min | Required knowledge, all five elements |
| **Demonstration with oral questioning** | Case WKS-164, four parts, 90 min, with an observation checklist keyed to critical aspects 1.1.1–1.5.4 · 3 oral questions per candidate | Critical aspects 1.1–1.5 |
| **Portfolio with interview** | The Day 3 and Day 5–10 evidence, checked against the portfolio map · 2 interview questions per candidate | Consistency and authenticity |

**The rule for a result:** *Competent* on the unit needs every critical aspect (1.1.1–1.5.4) evidenced by at least one method, and the written exam at 70% or more. A gap in one critical aspect means **Not Yet Competent** on that aspect, followed by a **reassessment of that aspect only**, arranged before Day 15. Full rules in `Day_10_Unit_Assessment_Guide.md` Parts 1 and 8.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| No co-host for Demo 1 | Read both parts. Change your voice a little for R. Santos |
| Pairs are odd-numbered | One trio: analyst, owner, observer. Rotate |
| ATT&CK Navigator will not load | Map on the paper table (Activity Pack Part 3). The JSON can be made later from home, or at the start of Day 11 |
| `Get-NetTCPConnection` shows hundreds of lines | Add `| Select-Object -First 15`. The skill is reading direction, not reading all of them |
| A trainee finds a connection they cannot explain on their own machine | `Get-Process -Id` names it. If it is still odd, note it for L2 and do not investigate further in class |
| Behind at 10:10 | Demo 4 maps B1 only. Activity 3 does B6, B7, B9, B10, B12 |
| Behind at 11:05 | Activity 4 assembles sections 3–10 only. The rest is finished by the end of Day 11 |
| **The assessment afternoon is disrupted** (outage, trainer ill) | See Assessment Guide Part 9. The written exam can move to Day 11 at 1:00. The demonstration and orals are rescheduled **live**, never done as self-study |

---

## End of morning checklist
- [ ] Activity 1 observation notes written up
- [ ] Morning evidence submitted to `Evidence/Day_10/` at 11:45, as it stands
- [ ] Portfolio checklists collected. Anyone missing items reminded: **12:45**
- [ ] Assessment set up: form or folder open, candidate files ready to release at 1:10 and 2:00, breakout rooms named for orals

## What to say at 11:45
One case has now run for four days. On Day 7 it was a failed quarantine. On Day 8 the verdict was *not contained*. On Day 9 it was escalated. Today it turned out to be data leaving the building, and the class warned the owners, traced it from one workstation to one server, and set aside a ransomware attack in the same minute because **no line joined them**. They put a name and an ID to how it got in and how it stayed, and wrote it all up with every claim on a line. This afternoon they show they can do it alone, on a case they have not seen. Say that, then send them to lunch.
