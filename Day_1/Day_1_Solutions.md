# DAY 1 — SOLUTIONS AND ANSWER KEY
## Cyber Threat Monitoring Level I

> ## TRAINER COPY ONLY
> **Do not send this file to trainees.** It contains the answers to everything they are marked on today.

---

## WHAT IS IN THIS FILE

| Part | What |
|------|------|
| **1** | The six exercises, with model answers |
| **2** | Huddle drill — all four cards |
| **3** | Afternoon Tasks 5 and 6 — the marked ones |
| **4** | How to mark, and what a good answer looks like |

---
---

# PART 1 — THE SIX EXERCISES

### Complete Exercise Pack with Model Answers

---

### Where each exercise sits in the hybrid day

| Exercise | When | How it runs |
|----------|------|------------|
| **1 — Set Up Your Evidence Folder** | Afternoon | Alone. Task 2 of the Self-Study Pack |
| **2 — Capture a Shift Handover** | **Morning, live** — written up in the afternoon | Notes taken by ear on the call; the log is written up alone as Task 3 |
| **3 — Read-Back Drill (Pairs)** | **Morning, live** | Paired practice in breakout rooms, 8 minutes |
| **4 — Mark Up an SOP** | Afternoon | Alone. Task 5 — **marked** |
| **5 — Triage a Written Notice** | Afternoon | **Now individual, not a team activity.** Task 6 — **marked** |
| **6 — The Huddle** | **Morning, live** | Teams run sequentially in the main room, 4 minutes each |

> **The two marked exercises are 4 and 5.** Between them they are the whole of LO2. Everything else today is either observed live or is preparation.

---

### Exercise 1: Set Up Your Evidence Folder

**Objective:** Create the folder structure you will use for all fifteen days.
**Unit link:** ICT311203 (previewed) — file management for evidence handling

#### Instructions:
1. On your Desktop, create a folder called `CTM_Level1`
2. Inside it, create these sub-folders:
   - `Evidence` — everything that goes into your portfolio
   - `Worksheets` — exercises in progress
   - `Tools` — portable tools you will collect from Day 4 onward
   - `Scans` — scan output from Days 11–14
3. Inside `Evidence`, create `Day_01` through `Day_15`

#### Solution (Step-by-Step):

1. **Create the main folder:**
   - Right-click an empty area of the Desktop
   - Hover over **New** → click **Folder**
   - Type `CTM_Level1` → press **Enter**

2. **Create the four sub-folders:**
   - Double-click `CTM_Level1` to open it
   - Right-click inside → **New** → **Folder** → type `Evidence` → **Enter**
   - Repeat for `Worksheets`, `Tools`, `Scans`

3. **Create the fifteen day folders quickly:**
   - Double-click `Evidence`
   - Right-click → **New** → **Folder** → type `Day_01` → **Enter**
   - Repeat through `Day_15`

> **Why `Day_01` and not `Day_1`?** Because Windows sorts text, not numbers. With a leading zero, `Day_10` sorts after `Day_09` where it belongs. Without it, `Day_10` sorts before `Day_2`. Small habit, saves confusion for fifteen days.

**Final structure:**
```
Desktop/
  └── CTM_Level1/
        ├── Evidence/
        │     ├── Day_01/  ...  Day_15/
        ├── Worksheets/
        ├── Tools/
        └── Scans/
```

---

### Exercise 2: Capture a Shift Handover

**Objective:** Listen to a spoken briefing and record it accurately in the required format.
**Unit link:** 400311101 LO1 — PC 1.1, 1.2

#### Instructions:
Your trainer will deliver a spoken shift handover **once**, at normal speed. Take notes on blank paper, then transfer them into the Shift Handover Log below.

#### Shift Handover Log

**Received by:** _________________________ **Date/Time:** _____________
**Handed over by:** _________________________

| Section | Content |
|---------|---------|
| **Open items** | |
| **Escalated** | |
| **Watch items** | |
| **System status** | |
| **Client notes** | |

**Questions I need to ask before I start:**

_______________________________________________

_______________________________________________

**Signature:** _________________________

---

#### Model Answer:

| Section | Content |
|---------|---------|
| **Open items** | **4471** — PE infection, WKS-042. Defender quarantined; full scan not finished. Confirm before midnight. |
| | **4478** — Phishing report, Finance. 3 users clicked. Credential entry **not confirmed** — follow-up call required. |
| | **4482** — Firewall alert storm from 203.0.113.45. Assessed as routine scanning noise, documented. May close if it does not recur. |
| **Escalated** | **4469** — EDR credential-dumping alert, Manila server. Sent to L2 ~20:00. **Ryan owns it. Do not touch.** |
| **Watch items** | Cebu branch firewall dropping log feed intermittently since ~19:00. Not down. **If it stops completely, raise with IT immediately.** |
| **System status** | Vulnerability scanner in maintenance until 06:00 — **no scans tonight**. All else green. |
| **Client notes** | Northwind called twice about Tuesday's report. **Do not promise a date.** Log it and pass to day shift. |

**Good clarifying questions to have asked:**
- "Confirming the host on 4471 — WKS-042, four-two, not two-four?"
- "For 4482, what counts as 'coming back' — same IP, or same alert type from any IP?"
- "On the Cebu watch item, what is the threshold for 'stopped completely'? Fifteen minutes with no events? An hour?"
- "For the Northwind note — do I log that in the ticket system or in the handover only?"

#### Self-Check Scoring

| Item captured correctly | Points |
|------------------------|--------|
| All three open ticket numbers | 3 |
| The IP address 203.0.113.45 exactly | 1 |
| The escalated ticket **and** the instruction not to touch it | 2 |
| The Cebu watch item **and** its trigger condition | 2 |
| "No scans tonight" | 1 |
| The instruction not to promise Northwind a date | 1 |
| **Total** | **10** |

> 7 or above is a solid first attempt. Below 5 means you were listening for the story instead of the facts — that is a fixable habit, and this is exactly the right week to fix it.

---

### Exercise 3: Read-Back Drill (Pairs)

**Objective:** Confirm an instruction correctly before acting on it.
**Unit link:** 400311101 LO1 — PC 1.4

#### Instructions:
Work in pairs. Partner A reads an instruction from the card list below at normal speed, exactly once. Partner B must:
1. Read the instruction back in their **own words**
2. Include the identifier, the action, and the notification
3. Ask **at least one** clarifying question

Then swap. Do all eight.

#### Instruction Cards

| # | Partner A reads aloud |
|---|----------------------|
| 1 | "Check WKS-207 for the quarantine failure and let the IT manager know when you have." |
| 2 | "Ticket 3390 needs a client call before the end of shift — it is High severity." |
| 3 | "Do not close 3402 yet, L2 is still looking at it." |
| 4 | "Run the daily agent-status check and tell me anything that is disconnected more than an hour." |
| 5 | "The Davao firewall alerts are expected tonight, there is a change on. Just document them." |
| 6 | "If the DLP alert on jdelacruz comes back, escalate it straight to the information security manager." |
| 7 | "Take the intake on this phone call, then hand it to me — I will do the assessment." |
| 8 | "Two things: confirm the scan on 4471, and do not start anything new after four." |

#### Model Read-Backs

| # | A good read-back sounds like | Good clarifying question |
|---|------------------------------|-------------------------|
| 1 | "Confirming — WKS-207, checking the quarantine failure, then notifying the IT manager. Correct?" | "Notify by email or phone?" |
| 2 | "Confirming — ticket 3390, High severity, client call before end of shift. Correct?" | "Which contact — the primary or the on-call?" |
| 3 | "Confirming — leave 3402 open, L2 still investigating. I will not close it." | "Should I still add notes to it, or leave it alone entirely?" |
| 4 | "Confirming — daily agent-status check, and I report anything disconnected over one hour, to you." | "Report as I find them, or one list at the end?" |
| 5 | "Confirming — Davao firewall alerts are expected, there is a change on, I document them and do not escalate." | "What is the change reference so I can record it?" |
| 6 | "Confirming — if the DLP alert on jdelacruz recurs, I escalate directly to the information security manager, not to L2." | "Does that skip you as well, or should I copy you?" |
| 7 | "Confirming — I take the intake only, then hand the ticket to you for assessment." | "Do you want me to fill in a severity, or leave it blank?" |
| 8 | "Confirming two things — confirm the scan on 4471, and start nothing new after 16:00." | "Does 'nothing new' include intake calls, or just queue work?" |

#### Common Failures to Watch For

| Failure | What it sounds like | Why it matters |
|---------|-------------------|---------------|
| Empty acknowledgement | "Okay." / "Got it." | Confirms nothing. The sender learns nothing about what you heard. |
| Dropping the notification | Repeats the action, forgets "tell the IT manager" | The most commonly dropped half of an instruction. |
| Parroting | Word-for-word repetition | Catches mishearing but not misunderstanding. |
| Guessing an identifier | Says "WKS-270" when they heard "207" | This is the failure that escalates the wrong machine at 3 AM. |

---

### Exercise 4: Mark Up an SOP

**Objective:** Extract mandatory, expected, and discretionary actions from a written procedure.
**Unit link:** 400311101 LO2 — PC 2.1, 2.2

#### Instructions:
Using your printed copy of **SOP-SOC-001 rev 4** (Alert Intake SOP), complete the table below. For each step, identify the binding word and state exactly what you are required to do.

| Step | Binding word | What it requires of you | Clock? |
|------|-------------|------------------------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

#### Model Answer:

| Step | Binding word | What it requires of you | Clock? |
|------|-------------|------------------------|--------|
| 1 | **SHALL** | Record four fields: alert ID, source system, timestamp, affected host | **Yes** — 5 minutes from receipt |
| 2 | **SHALL** | Assess against the Severity Matrix **before any other action** | No, but it is a sequence lock |
| 3 | **MUST** | Notify the client contact for Critical or High | **Yes** — 15 minutes from **assessment**, not from receipt |
| 4 | **SHOULD** check, **SHALL** record | Check for a matching Change Notice before escalating; if one explains the alert, recording the reference is mandatory | No |
| 5 | **MAY** | You have discretion to close a Low alert without escalation — **provided the assessment is documented** | No |
| 6 | **SHALL NOT** | You have no authority to contain. Containment is the SOC Manager's decision only | No |

#### Follow-up Questions

**Q1.** An alert arrives at 22:00. You assess it as High at 22:20. What is your notification deadline?
> **A:** 22:35. The 15-minute clock in step 3 runs from **assessment**, not from receipt. You were already 20 minutes late on step 1's five-minute recording requirement, but that does not move the step 3 deadline.

**Q2.** You assess an alert as Low and close it without writing anything down. Which step did you breach?
> **A:** Step 5. "May close" is conditional on "provided the assessment is documented." Undocumented discretion is not discretion.

**Q3.** A client phones and asks you to disconnect an infected laptop from the network. What do you do?
> **A:** Refuse politely and escalate. Step 6 says **shall not** — containment is authorised by the SOC Manager only. The correct response is: "I do not have authority to do that. I am escalating to the SOC Manager now and they will call you back." Then escalate immediately.

**Q4.** A Change Notice explains the alert, but you are in a hurry and just close it. What is missing?
> **A:** The change reference. Step 4 makes recording it **shall**, not should. Six months later, "why was this closed?" has no answer without it.

---

### Exercise 5: Triage a Written Notice (Individual — Afternoon)

**Objective:** Determine what a written notice requires of you and what it does not.
**Unit link:** 400311101 LO2 — PC 2.1, 2.2, 2.3
**When:** Afternoon, asynchronous. Task 6 of the Self-Study Pack. **This is marked.**

#### Instructions:
You work through **all three** notices — the vendor advisory, the change notice, and the client SLA notice — on your own. Answer four questions for each, then the three scenario questions that follow. Take about thirty minutes.

You may discuss the notices with your team. You may not submit the same words. The grid is individual work.

1. What am I being told?
2. What am I required to do, and by when?
3. Which systems or clients does it affect?
4. What would I do if this conflicted with the SOP?

1. What am I being told?
2. What am I required to do, and by when?
3. Which systems or clients does it affect?
4. What would I do if this conflicted with the SOP?

#### Notice A — Vendor Advisory

```
ADVISORY 2026-0418 — Endpoint Agent 7.4.2 Signature Regression
A signature regression in Endpoint Agent 7.4.2 may cause false positive
detections identified as "Trojan.Generic.Heur" on signed Microsoft
binaries, including powershell.exe and wmiprvse.exe.
Affected versions: 7.4.2 only.  Fixed in: 7.4.3 (2026-04-19).
Recommended action: update to 7.4.3. Until updated, treat
Trojan.Generic.Heur detections on signed Microsoft binaries as
suspected false positives and verify manually before escalating.
```

#### Model Answer — Notice A:
1. **What I am being told:** Version 7.4.2 of the endpoint agent produces false positives with a specific detection name on signed Microsoft binaries. A fix exists.
2. **What I must do:** For any `Trojan.Generic.Heur` detection on a signed Microsoft binary, **verify manually before escalating**. This is not permission to ignore the alerts — it changes the handling, not the priority. Check which agent version our endpoints run.
3. **Who it affects:** Only endpoints running agent 7.4.2. Endpoints on 7.4.1 or 7.4.3 are unaffected — so the first job is finding out which hosts are on 7.4.2.
4. **If it conflicted with the SOP:** It does not conflict — the SOP requires assessment before escalation, and this advisory tells me what that assessment should consider. If an advisory ever did contradict the SOP, I would follow the SOP and raise the conflict with my supervisor.

#### Notice B — Change Notice

```
CHANGE NOTICE CHG-2026-1177
System:    Manila file server cluster (SRV-MNL-01 .. SRV-MNL-04)
Window:    2026-04-22, 22:00 – 03:00
Change:    Quarterly OS patching and reboot cycle
Impact:    Hosts will reboot. Agent will report offline during reboot.
           Elevated process creation and service restart activity is expected.
Requester: IT Infrastructure    Approver: Change Advisory Board
```

#### Model Answer — Notice B:
1. **What I am being told:** Four named Manila servers will be patched and rebooted between 22:00 and 03:00 on 22 April. Offline agents and unusual process activity are expected during that window.
2. **What I must do:** During the window, alerts of that type from **those four hosts** are expected activity. Per SOP step 4, I record the change reference `CHG-2026-1177` on each and close them as expected. Outside the window, or from any other host, normal handling applies.
3. **Who it affects:** SRV-MNL-01 through SRV-MNL-04 only. **Not** SRV-CEB-anything, not workstations, not any other site.
4. **If it conflicted with the SOP:** No conflict — the SOP explicitly directs me to check for change notices. The trap would be over-applying it: a change notice for Manila does not excuse an alert from Cebu.

#### Notice C — Client SLA Reminder

```
INTERNAL NOTICE — Client SLA Reminder, Northwind Trading
Effective immediately, Northwind Trading is on an enhanced SLA:
  - Critical alerts: client notified within 10 minutes of assessment
  - High alerts:     client notified within 30 minutes of assessment
  - All notifications by phone to the on-call number, followed by email
  - Named contact: Ms. R. Aguilar, IT Manager (on-call 24/7)
This supersedes the standard 15-minute notification for this client only.
```

#### Model Answer — Notice C:
1. **What I am being told:** One specific client has faster notification targets than the standard SOP, and a named contact with a required method.
2. **What I must do:** For Northwind only — Critical in 10 minutes, High in 30 minutes, phone first then email, to Ms. R. Aguilar. Start the clock at assessment.
3. **Who it affects:** Northwind Trading only. Every other client stays on the standard 15 minutes.
4. **If it conflicted with the SOP:** It **does** conflict — the SOP says 15 minutes for High and Critical alike. This notice explicitly supersedes it for one client. That is legitimate, because it is a formal notice that says so. **If it did not say "this supersedes," I would follow the SOP and ask my supervisor which applies.** Never resolve a conflict silently by choosing the one you prefer.

> **Teaching point for the debrief:** Notice C is the one worth spending time on. Two documents gave contradictory instructions and the correct behaviour is *not* to pick the stricter one, or the newer one, or the one you like. It is to check whether the notice has authority to override — and if you cannot tell, to ask.

---

### Exercise 6: The Huddle (Team Activity)

**Objective:** Contribute effectively to a work-group activity.
**Unit link:** 400311102 LO1, LO2
**When:** Morning, live on the call. **This is observed evidence — it cannot be done asynchronously.**

#### Instructions:
Using the scenario card your trainer provides, run a **four-minute** shift huddle on camera while the rest of the class watches. Everyone speaks, every time. The other teams observe you using the Huddle Observation Checklist in your Student Handout.

> **Cameras on.** In an office everybody stands, and that is what keeps a huddle short. On a call, the timer does that job — and the camera is what makes your contribution assessable. An assessor cannot observe a black square.

#### Model Answer — Prioritising the Scenario Card

| Ticket | Severity call | Reasoning |
|--------|--------------|-----------|
| **5524** DLP: 400 MB to personal cloud | **Top priority** | Unassessed, high consequence. Potential data exfiltration by an insider. The largest unknown on the board — and unknowns with big consequences go first. |
| **5519** Adware cleaned but browser still redirecting | **Second** | The tool reported success but the symptom persists. That gap between "solution says clean" and "user says broken" is the single most common sign of an incomplete remediation. |
| **5524 → watch** SRV-BAK-01 silent since 16:00 | **Third** | Five hours of silence from a backup server is either a logging fault or something worse. Needs one look, not a panic. |
| **5512** Recurring blocked inbound, Low | **Last, but not never** | Correctly assessed Low. The trap is that "recurring for 3 nights" is a pattern — worth ten minutes to check whether the source is changing behaviour. |
| **Client note** Summary of blocked traffic | **Log and hand over** | It is a request, not an alert. Do not promise a date; make sure it does not disappear. |

#### What a Good Huddle Sounds Like

**Shift Lead opens:**
> "Huddle, two minutes. Top priority is 5524 — the DLP upload — it is unassessed and it is the biggest unknown we have. Second is 5519, adware that came back. Ana, open items?"

**Member reports:**
> "Two open. 5519, adware on WKS-118 — the AV says cleaned but the user says the browser is still redirecting, so I do not trust the clean. I will verify manually. And 5512, the recurring firewall blocks, assessed Low three nights running — I want ten minutes on whether the source is changing."

**Shift Lead closes:**
> "Ana owns 5519 and 5512. Marco takes 5524 and assesses it within the hour — if it looks like exfiltration, escalate immediately, do not sit on it. Ben checks SRV-BAK-01 and tells me whether it is a logging fault or a dead server. I will answer the client about the traffic summary and I am not promising them a date. 5524 is the one that cannot slip. Go."

#### Scoring Guide (for the observing team)

| Score | What it looks like |
|-------|-------------------|
| **Strong** | Everyone spoke, ticket numbers were used, the watch item got a named owner, priority was obvious to an outsider, finished under five minutes |
| **Adequate** | Everyone spoke, priorities stated, but ownership or timing was vague |
| **Needs work** | One member silent, no ticket numbers, no clear top priority, or ran over time |

---

### ANSWER KEY SUMMARY

| Exercise | Unit | Key Learning |
|----------|------|-------------|
| 1 | ICT311203 (preview) | Evidence folder structure for the full 15 days |
| 2 | 400311101 LO1 | Capture a spoken handover accurately into the required format |
| 3 | 400311101 LO1 | Read-back: identifier + action + notification, plus one clarifying question |
| 4 | 400311101 LO2 | shall / must / should / may / shall not — and where the clocks start |
| 5 | 400311101 LO2 | Extract required action from advisories, change notices, and SLA notices; never resolve a conflict silently |
| 6 | 400311102 | Contribute to a work group; prioritise by consequence of the unknown |

---
---

# PART 2 — HUDDLE DRILL: ALL FOUR CARDS

Every card is built the same way. Once you see the pattern you can debrief any of them without looking it up.

| Every card contains | Why it is there |
|---------------------|-----------------|
| **One unassessed item with a big consequence** | Always the correct top priority |
| **One Low item that keeps recurring** | The trap — easy to keep ignoring, but a repeat is a pattern |
| **One "tool says fixed, user says broken"** | The gap between a tool reporting success and reality |
| **One watch item** | Must be assigned to a **named person** |
| **One unanswered client note** | Not an alert. Still must not disappear |

| Card | Top priority | Why | The trap |
|------|-------------|-----|----------|
| **A** | **5524** — 400 MB uploaded to a personal cloud account, not assessed | Possible data theft. Biggest unknown, biggest consequence | **5512** — Low, recurring 3 nights |
| **B** | **6115** — new admin account created at 02:14, not assessed | Attackers create accounts so they can come back. Admin-level and unexplained | **6103** — Low, recurring 4 nights |
| **C** | **7248** — 12 Finance users got the same attachment, nobody checked who opened it | Unknown blast radius across twelve people | **7233** — Low, recurring 5 nights |
| **D** | **8830** — admin account accessed from another country at 03:40 | Likely account compromise, at admin level | **8817** — Low, blocked, recurring 3 nights |

## The rule that covers every card

> "Your top priority is always the thing nobody has looked at yet that could be really bad. Not the loudest item — the biggest unknown with the biggest consequence.
>
> And the trap is always the one marked Low that keeps coming back. 'It happened again' is a pattern, and a pattern deserves ten minutes of somebody's attention."

## Two bonus points — only if a team spots them

**Card B:** the client note asks who accessed the payroll folder, and the new admin account is on the HR server. Those may be the same story.

**Card D:** the client asked yesterday who has admin access to their cloud account, and last night an admin account logged in from abroad. Nobody connected them.

> **If someone spots either:** *"Stop — say that again for everyone. [Name] just connected the client's question to an alert. That is exactly the Level One skill."*

## If a team picks the trap as their top priority

Do not just correct them. Ask:

> *"What is the worst thing that happens if you are wrong about the Low one? Now what is the worst thing if you are wrong about the unassessed one?"*

They get there themselves, and it teaches consequence-based prioritising rather than a memorised answer.

---
---

# PART 3 — AFTERNOON TASKS 5 AND 6

### TASK 5 — THE SOP MARKUP TABLE

| Step | Binding word | What it requires | Clock? |
|------|-------------|-----------------|--------|
| 3.1 | **SHALL** | Record four fields: alert ID, source system, timestamp, affected host | **Yes** — 5 min from receipt |
| 3.2 | **SHALL** | Assess against the Severity Matrix **before any other action** | No — but it is a sequence lock |
| 3.3 | **MUST** | Notify the client for Critical or High | **Yes** — 15 min from **assessment** |
| 3.4 | SHOULD check / **SHALL** record | Check for a Change Notice. If one explains the alert, recording the reference is mandatory | No |
| 3.5 | **MAY** | Discretion to close a Low — **provided it is documented** | No |
| 3.6 | **SHALL NOT** | No containment authority at all | No |
| 3.7 | **SHALL** | Record every action, its time, and who authorised it | No |
| 3.8 | **SHALL** | Complete a handover log at end of shift | Yes — end of shift |

---

### TASK 5 — THE FOUR QUESTIONS

#### Q1. An alert arrives at 22:00. You assess it as High at 22:20. What is your notification deadline, and why?

> ## ANSWER: **22:35**

The clock in §3.3 runs from **assessment**, not from receipt. Assessment was 22:20, plus
15 minutes, equals 22:35.

They were already late on §3.1 — that required recording within 5 minutes of receipt, so by
22:05. **But being late on 3.1 does not move the 3.3 deadline.** Two separate clocks.

> **This is the one most of the class gets wrong**, and the usual wrong answer is 22:15 —
> they start the clock at receipt. Spend real time here. Ask: *"Read 3.3 out loud. What word
> comes immediately before the words 'the analyst must notify'?"*
>
> It is also the single most common cause of missed SLAs in real operations, so say that.
> It makes the pedantry feel worth it.

#### Q2. You assess an alert as Low and close it without writing anything down. Which step did you breach, and what exactly was missing?

> ## ANSWER: **Step 3.5.** The missing thing is the **documented assessment**.

"May close" is conditional on "provided the assessment is documented." The permission and the
condition are in the same sentence.

**Undocumented discretion is not discretion.** If you cannot show the reasoning, you did not
exercise judgement — you just closed a ticket.

#### Q3. A client phones you directly and asks you to disconnect an infected laptop from the network. What do you do, and which step tells you that?

> ## ANSWER: **Refuse and escalate. Step 3.6.**

The words to use:

> *"I do not have the authority to do that. I am escalating this to the SOC Manager now and
> they will call you back."*

Then escalate immediately — not just say it to end the call.

> **Watch for the trainees who wanted to say yes.** That instinct is good and it needs
> redirecting, not crushing. Say so out loud: *"Wanting to help is right. Doing it yourself
> is the part that is wrong."*

#### Q4. A Change Notice explains an alert, so you close it. What must you record before you do, and which step makes it mandatory?

> ## ANSWER: **The change reference.** Step 3.4 makes it **shall**, not should.

The trap in 3.4 is that it contains both words. Checking for a notice is **should**.
Recording the reference once you have found one is **shall**.

---

### TASK 6 — THE THREE SCENARIO QUESTIONS

#### A. It is 23:30 on 22 April. `SRV-MNL-01` through `SRV-MNL-04` just went offline. Incident or not?

> ## ANSWER: **Not an incident.**

CHG-2026-1177 covers exactly those four hosts, in exactly that window (22:00–03:00 on
22 April). Record the change reference and close it as expected activity.

#### B. Same night, same time. `SRV-CEB-02` goes offline. Incident or not?

> ## ANSWER: **Incident.**

Cebu is not in the change notice. The notice lists Manila hosts only.

> **This is the whole point of the exercise.** A notice tells you what it does **not** cover
> just as clearly as what it does. Ask the class: *"How many of you saw 'servers going
> offline is expected tonight' and applied that to all servers?"* Several hands will go up,
> and that is the lesson.

#### C. The Northwind SLA notice tells you to do something different from SOP-SOC-001 §3.3. Which do you follow?

> ## ANSWER: **Follow the Northwind notice.**

It explicitly says *"This supersedes… FOR THIS CLIENT ONLY."* **A document that has the
authority to override says so.** That sentence is the answer.

> **This is the best twenty minutes available in the whole debrief.**
>
> The correct behaviour when two documents conflict is **not** to pick the stricter one, or
> the newer one, or the one you prefer. It is to check whether the notice **has the authority
> to override** — and if you cannot tell, to ask.
>
> Anyone who answered "follow the stricter one" reasoned sensibly and still got it wrong.
> **Those are the most useful people to hear from.** Ask one of them to explain their
> thinking to the class before you give the answer. It is a far better lesson coming from a
> trainee than from you.

---

### HOW TO MARK TASKS 5 AND 6

Mark for **reasoning, not neatness**. These were cold attempts after one morning of
instruction.

What you are looking for:

- Did they find the binding verbs? *(Task 5 table)*
- Did they notice the boundary — what a notice does **not** cover? *(Task 6, question B)*
- Did they refuse the containment request? *(Task 5, Q3)*

Give **Attempted / Developing / Solid** rather than a score. LO2 is assessed properly across
Days 1–3. Nothing here is a final competency judgement.

"
