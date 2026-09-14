# CYBER THREAT MONITORING LEVEL I
## Day 1: Orientation and the Watch-Desk Voice
### Student Handout

---

## Welcome

Over the next fifteen days you will train for a real job: **Level 1 Cybersecurity Analyst**. That is the person who watches the alert queue, decides which alerts are real, writes them up, and gets the right people involved.

**By the end of this course you will be able to:**
- Receive and assess security alerts from many different sources
- Check whether a security solution is installed, running, and doing its job
- Verify a detection manually instead of trusting the tool blindly
- Follow up a case and escalate it to the correct authority
- Report threat activity clearly enough that somebody can act on it
- Schedule, run, and report a vulnerability scan of an organisation's assets

**What you will be qualified for:**
Cybersecurity Analyst (L1) · Cybersecurity Support Staff · Cybersecurity Help Desk Staff

---

## Your Qualification at a Glance

| | |
|---|---|
| **Qualification** | Cyber Threat Monitoring Level I |
| **Sector** | Information and Communications Technology |
| **Core Unit 1** | `CS-ICT251101` — Monitor and report cyber threats |
| **Core Unit 2** | `CS-ICT251102` — Conduct vulnerability scanning of assets |
| **Basic units** | 9 units (communication, teamwork, problem solving, self-management, innovation, information, OSH, environment, entrepreneurial mindset) |
| **Common units** | 2 units (apply quality standards, perform computer operations) |

---

## How Competency-Based Training Works

This is **not** a course where you pass with a score. For every unit you are rated:

| Rating | What it means |
|--------|--------------|
| **C — Competent** | You demonstrated the skill to the standard, consistently |
| **NYC — Not Yet Competent** | You need more practice. You try again. This is normal. |

There is no curve and no ranking. **Everyone on this course can finish Competent.**

### Your Evidence Portfolio
Almost every day you produce something that proves you can do the work — a signed log, a completed worksheet, a ticket, a report. **Keep every one of them.** On Day 15 you assemble them into a portfolio, and that portfolio is what an assessor examines.

> If you lose your paperwork, you lose your evidence. Get a folder today.
---
---

## How Day 1 Runs

Today has two halves, and they work differently.

| | Morning — **live on the call** | Afternoon — **on your own** |
|---|---|---|
| **Time** | 8:00 AM – 12:00 PM | 1:00 – 5:00 PM |
| **Where** | Online, together | Wherever you are working |
| **What** | Orientation, icebreaker, teams, OSH induction, inside a SOC, **spoken messages**, **the shift huddle** | The afternoon Self-Study Pack — eight tasks, about 3 hours 40 minutes |
| **Why this half is here** | These only work with other people present. An assessor has to *see* you take down a spoken briefing, read an instruction back, and contribute to a huddle | Reading a procedure correctly is solitary work in the real job too. Nobody reads an SOP in a huddle |

### The morning, block by block

| Time | Session |
|------|---------|
| 8:00 – 8:15 | Join, tech check, welcome |
| 8:15 – 8:35 | Programme orientation and how this day runs |
| 8:35 – 9:00 | Icebreaker: the incident you already survived |
| 9:00 – 9:15 | Team formation |
| 9:15 – 9:45 | OSH and environmental induction · **Home Workstation Audit** |
| 9:45 – 10:15 | Inside a Security Operations Centre |
| 10:15 – 10:25 | Break |
| 10:25 – 11:30 | **Follow routine spoken messages** — handover, read-back drill, clarifying questions |
| 11:30 – 11:50 | **Work with others** — the shift huddle drill |
| 11:50 – 12:00 | Briefing for the afternoon |

**Cameras on for the drills.** Not for the lectures — for the read-back drill and the huddle. Those are observed evidence, and an assessor cannot observe a black square.

**Say your name before you speak.** For fifteen days. On a real incident bridge call nobody can see who is talking either, and analysts who do not identify themselves cause exactly the confusion this course trains out of you.

### The afternoon is not a half day

It is the second half of Day 1 and it carries a unit element the morning did not — *LO2, perform workplace duties following written notices*. It produces marked evidence for your portfolio, and it is not repeated in class.

---

## The 15 Days

| Phase | Days | What you learn |
|-------|------|---------------|
| **A — Foundation** | 1–3 | Communication, teamwork, problem solving, safety, information handling, quality |
| **B — Monitor & report cyber threats** | 4–10 | The complete alert lifecycle, from detection to reporting |
| **C — Conduct vulnerability scanning** | 11–14 | Scheduling, scanning, and reporting on organisational assets |
| **D — Assessment** | 15 | Portfolio build and full mock national assessment |

---

## Inside a Security Operations Centre

### The Alert Pipeline

```
   SENSORS        →      SIEM       →     ANALYST    →     ACTION
   AV, firewall,         collects,        you             ticket,
   EDR, WAF,             correlates,      decide if       escalate,
   DLP, NDR              ranks            it is real      notify
```

### What Each Sensor Sees

| Sensor | Full name | What it watches |
|--------|-----------|----------------|
| **AV** | Antivirus | Files and processes on one machine |
| **Firewall** | — | Traffic entering and leaving the network |
| **WAF** | Web Application Firewall | Requests going to a website |
| **DLP** | Data Loss Prevention | Sensitive data leaving the organisation |
| **EDR** | Endpoint Detection and Response | Process behaviour on the endpoint |
| **NDR** | Network Detection and Response | Behaviour across network traffic |
| **SIEM** | Security Information and Event Management | Everything above, in one place |

### A Real Shift, Hour by Hour

This is a plausible eight-hour night shift. Read it slowly — it is the job you are training for.

| Time | What happens | What you, as L1, do |
|------|-------------|--------------------|
| 21:00 | Shift start | Read the handover log from the previous shift |
| 21:10 | 47 alerts in the queue | Start triage — oldest and highest severity first |
| 21:40 | AV alert: PE infection on a workstation | Check the detection, check the action taken, issue a ticket |
| 22:15 | Client calls: "my files have weird names" | Take the intake, ask the scripted questions, raise a ticket |
| 22:20 | Same client's endpoint shows encryption activity | **Ransomware.** Notify immediately, escalate to L2 |
| 23:00 | Firewall alert storm from one IP | Assess against criteria — routine scanning noise, not a threat |
| 01:00 | Quiet | Clear the low-severity backlog, update ticket notes |
| 04:00 | EDR alert: credential dumping tool | Escalate — this is above L1 |
| 05:00 | Write the handover log | Hand over cleanly to the day shift |

**Two things to notice.**

First, most of the shift is not exciting. That is normal, and it is good.

Second, look at **22:20**. The analyst did the most valuable thing anybody did all night — they connected a phone call at 22:15 to an alert at 22:20. No tool did that. A person did. That is the whole job in one line.


### The Tiers — and Where You Sit

| Tier | What they do | You? |
|------|-------------|------|
| **L1** | Triage the queue, verify, ticket, escalate | **This is you** |
| **L2** | Investigate what L1 escalated, scope the incident | |
| **L3** | Hunt for threats nobody alerted on, lead major incidents | |
| **SOC Manager** | Staffing, SLAs, client communication, containment decisions | |

> **Know the edge of your authority.** An L1 does not decide to disconnect a company from the internet, rebuild a server, or talk to the press. If somebody asks you to make that call, escalate — do not be brave.

---

## Unit 400311101 — Receive and Respond to Workplace Communication

### LO1: Follow Routine Spoken Messages

You must be able to show that:
1. You gather required information by **listening attentively** and interpreting instructions correctly
2. You **record** instructions and information as the workplace requires
3. You **act on instructions immediately**, in line with what you received
4. You **seek clarification** from your supervisor whenever an instruction is not clear

### The Shift Handover

Every shift begins and ends with a handover. It has a standard shape:

| Section | What goes in it |
|---------|----------------|
| **Open items** | Tickets still in progress — ticket number and current state |
| **Escalated** | What went to L2/L3, and who owns it now |
| **Watch items** | Not yet incidents, but need eyes |
| **System status** | Anything down, degraded, or in maintenance |
| **Client notes** | Anything a client asked for or complained about |

### The Read-Back Rule

When you receive an instruction that matters, **repeat it back in your own words before you act on it.**

> "So you want me to isolate WKS-042 — not WKS-024 — and notify the IT manager. Confirming."

It takes four seconds and catches almost every mishearing. Pilots do it. Nurses do it. Analysts should do it.

### When to Stop and Ask

Three situations mean **stop and seek clarification**:
1. You do not understand the instruction
2. The instruction contradicts the SOP
3. Acting on it would exceed your authority

**Four questions you always have available:**
- "Can you repeat the hostname / IP / ticket number?"
- "Do you want me to do that now, or after I finish the current ticket?"
- "That is above my authority — should I escalate, or are you authorising it?"
- "The SOP says X and you are asking for Y. Which should I follow?"

> Asking is not weakness. **Not asking is the error.**

---

### LO2: Perform Workplace Duties Following Written Notices

### The Three Documents That Run a SOC

| Document | What it tells you | When you read it |
|----------|------------------|------------------|
| **Alert Intake SOP** *(SOP = Standard Operating Procedure)* | Exactly what to do when an alert arrives | Every alert |
| **Severity Matrix** | How to rank an alert: Critical / High / Medium / Low | Every alert |
| **Escalation Matrix** | Who to contact, at what severity, within what time | Every escalation |

### Reading an SOP: Watch the Verbs

| Word | What it means |
|------|--------------|
| **shall** / **must** | Mandatory. No discretion. |
| **should** | Expected. If you deviate, you must justify it. |
| **may** | Your judgement. |
| **within X minutes** | A clock is running. Note the start time. |

### Advisories vs Change Notices

| | **Advisory** | **Change Notice** |
|---|---|---|
| **Tells you** | A threat, a patch, or a vulnerability exists | A system will be modified at a set time |
| **Usually** | Informational, sometimes actionable | Always relevant to your queue |
| **Why L1 cares** | May generate new alert types | **Scheduled change is the most common cause of false alerts** |

> If you do not read the change notices, you will spend your night investigating an "attack" that is really the IT team patching servers.

---

## Unit 400311102 — Work With Others

### Who Owns What on a Single Alert

| Stage | L1 | L2 | SOC Manager |
|-------|----|----|-------------|
| Alert triage | **Responsible** | Consulted | Informed |
| Ticket creation | **Responsible** | — | Informed |
| Investigation | Consulted | **Responsible** | Informed |
| Client notification | **Responsible** (high/critical) | Consulted | **Accountable** |
| Containment decision | — | Consulted | **Accountable** |

### The Shift Huddle

A very short team meeting at the start of a shift. **Four minutes. Everyone speaks once. Then you go to work.**

It is not a presentation, and it is not a discussion. Nobody prepares anything. If somebody starts explaining *how* they will fix something, the Shift Lead stops them — that conversation happens after the huddle, with the people who need to be in it.

1. **Shift Lead opens** — what matters most tonight, and why
2. **Each member reports** their open items — one sentence each
3. **The team assigns the watch item** — to a named person, not to "somebody"
4. **Shift Lead closes** with the single thing that cannot slip tonight

In an office everybody stands, and standing is what keeps it short. On a call, the timer does that job instead.

> **Your full drill materials — what a good huddle sounds like, your scenario card, and the checklist — are in the Huddle Drill Pack.**

---

## Huddle Observation Checklist

**Team observed:** _________________________ **Observer:** _________________________

| # | Item | YES | NO | Notes |
|---|------|-----|----|----|
| 1 | The Shift Lead opened by stating priorities | [ ] | [ ] | |
| 2 | **Every** member spoke at least once | [ ] | [ ] | |
| 3 | Open items were given with ticket numbers | [ ] | [ ] | |
| 4 | The watch item was assigned to a named person | [ ] | [ ] | |
| 5 | The huddle finished within 4 minutes | [ ] | [ ] | |
| 6 | At the end, the top priority was clear to an outsider | [ ] | [ ] | |
| 7 | Members listened without interrupting | [ ] | [ ] | |
| 8 | At least one clarifying question was asked | [ ] | [ ] | |

**Signature:** _________________________ **Date:** _____________

---

## My Team

| | |
|---|---|
| **Team Name** | _________________________ |
| **Shift Lead** | _________________________ |
| **Scribe** | _________________________ |
| **Presenter** | _________________________ |
| **Timekeeper** | _________________________ |

> Roles **rotate every three days** so that everyone practises every role.

**Contact details** — collect these in your breakout room this morning. You work alone this afternoon, but you can still ask each other what a word in the SOP means.

| Name | How to reach them |
|------|------------------|
| | |
| | |
| | |

---

## Lab Rules — Non-Negotiable

These apply in the training lab from our first day on site. **One of them applies from today.**

- No food or drinks at the workstations
- No installing software that is not part of the course
- **No scanning, probing, or testing anything outside the lab network** — this applies from Day 1 to Day 15 and beyond, wherever you are working
- Report damaged cables or equipment; do not repair them yourself
- Monitors off at lunch; proper shutdown at the end of the day

### Your Desk Today

You are not in the lab, so today your OSH evidence is the **Home Workstation Audit** you completed on the call this morning. It covers the desk you are actually sitting at, which for the next fifteen days matters more than the lab does.

**Set it up properly:**

| | |
|---|---|
| **Chair** | Feet flat on the floor, thighs parallel to the ground |
| **Monitor** | Top of the screen at eye level, about an arm's length away |
| **Laptop users** | Your screen is too low. A stack of books and a separate keyboard fixes it for nothing |
| **Keyboard and mouse** | Elbows at about 90 degrees, wrists straight, mouse close to the keyboard |
| **Lighting** | No window directly behind the screen |

### The 20-20-20 Rule
Every **20 minutes**, look at something **20 feet** away for **20 seconds**.

> Analysts stare at screens for eight to twelve hours at a stretch, often at night. The people who last in this job are the ones who set their desk up properly in their first month.

### Two Documents Still Outstanding

| Document | Why it waits |
|----------|-------------|
| **Lab OSH Checklist** | It is a safety check of the training lab workstation you will use — not the desk you are at today |
| **Green Lab Pledge** | It is a commitment about how the training lab is run and powered down |

You sign both on our first day on site. Your trainer has recorded them as outstanding.

### Working Green — From Today

- Paperless where you can: store evidence digitally, do not print what you can file
- Monitors off at lunch; shut down properly at the end of the day
- E-waste — batteries, drives, old equipment — never goes in general rubbish

---

## Words and Short Forms You Will Hear

This job is full of short forms. Nobody will explain them twice, so here they are once.

### The ones you need today

| Short form | Stands for | What it actually means |
|-----------|-----------|----------------------|
| **SOP** | **Standard Operating Procedure** | A written instruction for how a job is done — the same way, every time, by whoever is on shift |
| **SOC** | **Security Operations Centre** | The team, and the room, that watches for attacks |
| **SIEM** | **Security Information and Event Management** | The system that collects what every tool reports and puts it in one place |
| **L1 / L2 / L3** | Level 1, 2, 3 | The tiers of analyst. You are L1 |
| **SLA** | **Service Level Agreement** | The contract term saying how fast you must respond to a client |
| **OSH** | **Occupational Safety and Health** | Workplace safety — your chair, your screen, the room |
| **RACI** | Responsible, Accountable, Consulted, Informed | A grid showing who owns what at each stage |

### The sensors

| Short form | Stands for | What it watches |
|-----------|-----------|----------------|
| **AV** | **Antivirus** | Files and programs on one machine |
| **EDR** | **Endpoint Detection and Response** | How programs *behave* on a machine |
| **NDR** | **Network Detection and Response** | How traffic behaves across the network |
| **WAF** | **Web Application Firewall** | Requests arriving at a website |
| **DLP** | **Data Loss Prevention** | Sensitive data leaving the organisation |
| **IPS** | **Intrusion Prevention System** | Attacks in network traffic — and blocks them |

### Coming later in the course

| Short form | Stands for | When you meet it |
|-----------|-----------|-----------------|
| **IoC** | **Indicator of Compromise** | Day 6 onward |
| **C2** | **Command and Control** | The attacker's remote control channel |
| **PUP** | **Potentially Unwanted Program** | Not quite malware, not wanted either |
| **CVE** | **Common Vulnerabilities and Exposures** | The public numbering system for known flaws — Days 11 to 14 |
| **CERT** | **Computer Emergency Response Team** | A national body that publishes advisories |
| **CISO** | **Chief Information Security Officer** | The most senior security person. An L1 never contacts them directly |

> **Ask when you do not know one.** Every person in this industry has nodded along to an acronym they did not know. The ones who ask stop having to.

---

## Notes — This Morning's Shift Handover

_Take the trainer's spoken handover down here. No slides, no chat — by ear only._

_You write this up properly as **Task 3** of the afternoon pack, from these notes and nothing else. If you miss something, leave a gap and write "could not hear — would confirm." An honest gap is better work than a plausible guess._

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________
