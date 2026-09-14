# DAY 2 — TRAINER GUIDE
## Solving Routine Problems on a Real Desk
### Mode: FACE-TO-FACE | Schedule: 8:00 AM – 5:00 PM

---

## UNITS OF COMPETENCY COVERED TODAY

| Code | Unit of Competency | Elements |
|------|-------------------|----------|
| 400311103 | Solve/address routine problems | LO1 Identify the problem · LO2 Assess fundamental causes · LO3 Determine corrective action · LO4 Communicate action plans |
| 400311104 | Enhance self-management skills | LO1 Set personal and career goals · LO2 Recognize emotions · LO3 Describe oneself as a learner |
| 400311105 | Support innovation | LO1 Identify the need for innovation · LO2 Recognize innovative and creative ideas · LO3 Support access to flexible and innovative practice |
| 400311109 | Adopt entrepreneurial mindset in the workplace | LO1 Determine entrepreneurial mindset · LO2 Identify entrepreneurial practices |

---

## BEFORE CLASS CHECKLIST

- [ ] Print: Student Handout, three Fault Cards per team, Problem-Solving Worksheet (×4 per trainee)
- [ ] Print: SOP Improvement Proposal form (×1 per trainee)
- [ ] `Fault_Log_Team_A.csv` through `Fault_Log_Team_D.csv` copied to the shared folder
- [ ] Whiteboard cleared; teams from Day 1 still listed on the board
- [ ] Your machine: PowerShell open, `Sample_Alert_Log.csv` ready to project
- [ ] Collect any Day 1 evidence that was not handed in

> **Trainer Tip:** Today has no new tools. That is deliberate. The method taught today is the one trainees will use on Days 8, 9 and 13 when a real tool misbehaves. If they leave today without a method, those days become guesswork.

---

## 8:00 – 8:15 AM | RECAP AND SETTLE (15 min)

1. Quick recall from Day 1 — ask four trainees at random:
   - "What are the five sections of a handover?"
   - "What three things does a good read-back contain?"
   - "What does 'shall not' mean in an SOP?"
   - "Who is Accountable for a containment decision?"
2. Return any marked Day 1 worksheets
3. Confirm every trainee has an evidence folder with Day 1 documents in it

### What to Say:
> "Yesterday you learned how to receive information. Today you learn what to do when the information is that something is broken. Not a cyber attack — just broken. An agent that stopped reporting. Tickets that duplicated themselves. A hundred alerts that all say the same wrong thing. These are the problems that fill an analyst's actual week, and the method for taking them apart is the same every time."

---

## 8:15 – 10:00 AM | IDENTIFY THE PROBLEM, ASSESS THE CAUSE (1 hr 45 min)
### Unit 400311103 — LO1 and LO2

### Part A: Problem vs Symptom (25 min)

**Write these two columns on the whiteboard:**

| What people report (symptom) | What is actually wrong (problem) |
|------------------------------|----------------------------------|
| "The dashboard is empty" | The agent stopped sending events |
| "I'm getting a hundred alerts" | One rule is matching normal activity |
| "The same ticket keeps appearing" | The integration is retrying on timeout |
| "The scan never finished" | The target went offline mid-scan |
| "Antivirus says it cleaned it but it's back" | The persistence mechanism was not removed |

### What to Say:
> "Notice the pattern. The left column is what somebody tells you. The right column is what you have to find. If you fix the left column, the problem comes back tomorrow. Every one of these is a real thing that will happen to you in your first six months."

**Teach the three questions that turn a symptom into a problem statement:**

1. **What exactly is happening?** — observable, specific, no interpretation
2. **When did it start?** — and what else changed at that time
3. **What is the scope?** — one host, one team, one site, or everything

**Demonstrate on the board with a bad and a good problem statement:**

| | |
|---|---|
| **Bad** | "The SIEM is broken." |
| **Good** | "Since approximately 14:20 today, four Manila servers (SRV-MNL-01 to 04) have shown no events in the dashboard. All other hosts are reporting normally. The four affected hosts respond to ping." |

> **Say:** "The good statement is longer, and that is fine. It contains a start time, a scope, a boundary — what is affected and what is not — and one piece of evidence. Somebody who has never seen this problem could pick it up from that sentence."

### Part B: The Five Whys (30 min)

1. Explain the technique in one line:
   > "You ask 'why' until the answer stops being a symptom and starts being something you can actually change."

2. **Demonstrate live on the whiteboard** with the recurring AV detection fault:

```
PROBLEM: The same malware detection reappears on WKS-118 every morning.

Why? → Antivirus detects and cleans the file each morning.
Why does it come back? → Something writes it back to disk.
Why does something write it back? → A scheduled task runs at logon and
                                    downloads it.
Why is there a scheduled task? → It was created by the original infection.
Why wasn't it removed? → The antivirus removed the FILE but not the
                          PERSISTENCE MECHANISM.

ROOT CAUSE: Remediation was incomplete — the persistence was never removed.
CORRECTIVE ACTION: Remove the scheduled task, then re-scan. Verify at next
                   logon before closing the ticket.
```

3. Make the teaching point explicitly:
   > "Look at where we stopped. We stopped at something we can *do* — remove the scheduled task. If you stop at 'because there is malware', you have not finished. If you go past it to 'because the user clicked a link', that is true but it is not tonight's fix. Root cause analysis stops at the first thing you can act on."

4. **Trap to name:** the Five Whys can drift into blaming a person.
   > "If your fifth 'why' is somebody's name, back up. 'The user clicked a link' is a training gap, not a root cause you fix at 2 AM. Find the technical cause first."

### Part C: Cause-and-Effect Analysis (25 min)

1. Draw a fishbone (Ishikawa) diagram on the whiteboard for the fault: **"Alerts stopped arriving from one site."**
2. Use these six branches, which map to what actually goes wrong in a SOC:

| Branch | Ask |
|--------|-----|
| **Agent** | Is the service running? Is it the right version? Is the config right? |
| **Network** | Can the host reach the server? Is a firewall rule blocking it? |
| **Server** | Is the manager up? Is the disk full? Is the indexer accepting writes? |
| **Configuration** | Did somebody change a rule, a filter, or a log level? |
| **Host** | Did it reboot? Is it patched? Is it even powered on? |
| **Process** | Is there a change notice? Did somebody do this deliberately? |

3. Fill in the branches with the class calling out possibilities. Do not filter — write down everything.
4. Then narrow: **"Which of these can we test in under five minutes?"** Circle those.

> **Say:** "That last question is the difference between a method and a mess. You will always have twelve possible causes. Test the cheap ones first. Five minutes of `ping` and `Get-Service` eliminates half the fishbone."

### Part D: Team Fault Drill 1 (25 min)

1. Each team gets **Fault Card 1** and their team's fault log CSV
2. Teams have **15 minutes** to produce, on the Problem-Solving Worksheet:
   - A one-paragraph problem statement (what, when, scope, boundary)
   - A Five Whys chain
   - A ranked list of possible causes with "how I would test this in 5 minutes" next to each
3. Each team presents for **2 minutes**
4. Trainer reveals the actual cause and debriefs

---

## 10:00 – 10:15 AM | BREAK

---

## 10:15 AM – 12:00 PM | CORRECTIVE ACTION AND COMMUNICATING THE PLAN (1 hr 45 min)
### Unit 400311103 — LO3 and LO4

### Part A: Generating and Evaluating Options (30 min)

### What to Say:
> "You have found the cause. Now — what do you do about it? New analysts jump to the first fix they think of. Experienced ones write down three, because the first idea is often the most expensive one."

**Teach the option table. Draw it on the board and fill it in with the class for the 'four servers stopped reporting' fault:**

| Option | What it costs | What it risks | Is it within my authority? |
|--------|--------------|--------------|---------------------------|
| Restart the agent service on all four | 5 min | Loses in-flight events | **Yes** — routine |
| Reboot the four servers | 30 min + downtime | Business impact, needs a change | **No** — escalate |
| Wait for the maintenance window to end | 0 | Delay if it is not the change | **Yes** — with documentation |
| Escalate to IT immediately | 5 min | Wastes their time if it is expected | **Yes** |

Then apply the three filters, in this order:

1. **Is it within my authority?** — if no, the option is not an option; it is an escalation
2. **Is it reversible?** — prefer the fix you can undo
3. **Is it the smallest thing that could work?** — restart the service before you reboot the host

> **Say:** "Those three questions in that order will keep you out of trouble for your whole career. The dangerous analyst is not the one who does not know the answer. It is the one who does something big and irreversible because it felt decisive."

### Part B: Writing an Action Plan (30 min)

**Put the required shape on the board:**

| Field | Content |
|-------|---------|
| **Problem** | One paragraph: what, when, scope, boundary |
| **Cause** | The root cause, stated as something changeable |
| **Action** | Numbered steps, each one a single verifiable act |
| **Who** | A named person or role per step |
| **When** | A time or a deadline per step |
| **How we will know it worked** | The observable test |
| **If it does not work** | The fallback, and who to escalate to |

**Model one live on the projector.** Use the recurring-detection fault from Part B of the morning:

```
PROBLEM   Since 2026-04-18, malware detection "Trojan.Agent.XZ" has been
          detected and cleaned on WKS-118 every weekday morning between
          08:05 and 08:20. No other host is affected. The user logs in
          at approximately 08:00.

CAUSE     Remediation is incomplete. A scheduled task created by the
          original infection re-downloads the payload at user logon. AV
          removes the file but not the task.

ACTION    1. Export the current scheduled task list from WKS-118      (L1, today 14:00)
          2. Identify and document the task that runs at logon        (L1, today 14:30)
          3. Escalate task removal to L2 — deletion is above L1        (L1, today 15:00)
          4. After removal, run a full AV scan                        (L2, today 16:00)
          5. Verify at next user logon                                (L1, tomorrow 08:30)

SUCCESS   No detection on WKS-118 at the 08:05–08:20 window for three
          consecutive working days.

FALLBACK  If the detection recurs after task removal, escalate to the
          information security manager — this indicates a second
          persistence mechanism we have not found.
```

3. Make two points about this plan:
   - **Step 3 is an escalation, and that is correct.** Deleting a scheduled task changes system state — an L1 documents it and hands it up.
   - **Success is defined in advance, with a number.** "Three consecutive working days" is testable. "Seems fixed" is not.

### Part C: Communicating It Upward and Sideways (25 min)

1. Teach that the **same plan is said three different ways** depending on the audience:

| Audience | What they need | Length |
|----------|---------------|--------|
| **Your L2 / supervisor** | Technical detail, what you have already tested, what you need from them | 3–4 sentences |
| **The client / user** | What is happening, what it means for them, when they will hear next | 2 sentences, no jargon |
| **The ticket** | Everything, in order, with timestamps — the permanent record | As long as it needs to be |

2. **Demonstrate all three** for the same fault (see Demonstration Steps, Demo 3). Have the class notice what gets dropped for the client and what must never be dropped from the ticket.

3. **Pairs drill:** each trainee explains their fault from the morning drill to a partner playing (a) the L2, then (b) the client. Partner scores them against the audience table.

### Part D: Team Fault Drill 2 (20 min)

1. Each team receives **Fault Card 2** — a harder fault, with a misleading first symptom
2. Teams produce a full action plan on the worksheet in **12 minutes**
3. Presenter delivers it as if speaking to the L2 — **60 seconds only**
4. Trainer times them strictly and cuts them off at 60 seconds
   > "That cut-off is not cruelty. Your L2 has eleven other things happening. Sixty seconds is genuinely what you get."

---

## 12:00 – 1:00 PM | LUNCH BREAK

---

## 1:00 – 2:30 PM | ENHANCE SELF-MANAGEMENT SKILLS (1 hr 30 min)
### Unit 400311104 — LO1, LO2, LO3

### Part A: Personal and Career Goals (30 min)

### What to Say:
> "This unit looks like the soft one on the list. It is not. Shift work in a security operations centre burns people out faster than almost any other IT role, and the people who last are the ones who knew why they were there and could tell when they were running out."

1. Teach the difference the unit requires:

| | **Personal goal** | **Career goal** |
|---|---|---|
| **About** | Who you want to be | What you want to do |
| **Timeframe** | Often lifelong | Usually 1–5 years |
| **Example** | "Support my family without being absent from it" | "Move from L1 to L2 within two years" |
| **Measured by** | Your own judgement | Role, certification, salary, responsibility |

2. Put the **real career ladder** on the board so the goal-setting is grounded in something true:

```
  L1 Analyst  →  L2 Analyst  →  L3 / Threat Hunter  →  SOC Lead
      ↓              ↓                  ↓
  Help desk     Vulnerability      Incident Response
   support        Management          / Forensics
```

3. Each trainee completes the **Goal Sheet** in the Student Handout:
   - One personal goal
   - One career goal at 1 year and one at 3 years
   - Two things they must learn to reach the 1-year goal
   - One thing they will do in the next 30 days
4. **Collect. This is competency evidence.**

### Part B: Recognising Emotions (30 min)

### What to Say:
> "At some point in your first year, an alert is going to come in that frightens you. Ransomware spreading in real time, at three in the morning, and you are the only person awake. What you do in that moment depends on whether you can notice what is happening to you."

1. Name the four emotional states that most affect analyst performance, and their tells:

| State | What it feels like | What it does to your work | What to do |
|-------|-------------------|--------------------------|-----------|
| **Alert fatigue** | Numb, clicking through | You start closing things without reading | Stand up. Take five. Re-read the last three you closed. |
| **Panic** | Racing, tunnel vision | You skip steps and forget to record | Go back to the SOP. Follow it literally. It exists for this. |
| **Frustration** | Snappy, blaming the tool | You stop asking for help | Say out loud that you are stuck. That is the whole fix. |
| **Overconfidence** | Certain, fast, skipping verification | You escalate the wrong thing | Slow down and verify one thing you "already know". |

2. **Positive states matter too** — the unit asks for both:

| State | Why it helps | How to protect it |
|-------|-------------|------------------|
| **Curiosity** | It is the engine of good triage | Give yourself ten minutes on the odd alert |
| **Calm** | Lets you follow the process under pressure | Comes from having run the drill before |
| **Satisfaction** | Sustains you through quiet shifts | Notice the catches, not just the misses |

3. **Individual reflection (10 min):** each trainee writes one honest sentence about a time they experienced each of: frustration, panic, and satisfaction at work or in study. Not shared unless they choose to.
4. **Pair discussion (10 min):** in pairs, share **one** of the three. Partner listens without advising.

> **Trainer Tip:** Do not force sharing. The competency is *recognising* emotions, which is internal. Sharing is optional and some trainees will decline. Note their written reflection as the evidence instead.

### Part C: Describe Yourself as a Learner (30 min)

1. Run the **learning-style inventory** in the Student Handout (Kolb-style, four short scales)
2. Discuss the four styles as they apply specifically to this course:

| If you learn mainly by... | You will find easy | You will find hard | What to do about it |
|--------------------------|-------------------|-------------------|-------------------|
| **Doing** | Days 6–14, the hands-on days | Days 1–3, the discussion days | Turn every concept into a "show me" — ask the trainer to demonstrate |
| **Watching** | Demonstrations, the projector | Being first to try it | Take notes during the demo, then do it immediately while it is fresh |
| **Thinking it through** | SOPs, frameworks, ATT&CK | Fast timed drills | Read ahead the night before; you will be faster in the drill |
| **Trying and adjusting** | Timed drills, troubleshooting | Long written procedures | Ask "what breaks if I get this wrong" — you learn from the edge cases |

3. Each trainee writes, on their Goal Sheet:
   - My dominant style
   - The part of this course I expect to find hardest
   - **One concrete strategy** I will use to get through it

> **Say:** "That last line matters more than the inventory. Knowing you are a hands-on learner is trivia. Deciding 'on Day 5, when it gets theoretical, I will ask the trainer for a demonstration instead of zoning out' — that is self-management."

---

## 2:30 – 2:45 PM | BREAK

---

## 2:45 – 4:00 PM | SUPPORT INNOVATION (1 hr 15 min)
### Unit 400311105 — LO1, LO2, LO3

### Part A: Where Innovation Lives in a SOC (20 min)

### What to Say:
> "Innovation in a security operations centre almost never means a new product. It means somebody noticed that the same annoying thing happens forty times a week and did something about it. That is the whole thing."

1. Identify the need for innovation — teach the four signals:

| Signal | What it sounds like | Example from a SOC |
|--------|-------------------|-------------------|
| **Repetition** | "I do this every single shift" | Manually copying alert details into the ticket |
| **Workaround** | "You just have to know to do X first" | Undocumented step everyone learned the hard way |
| **Complaint** | "This always happens on Mondays" | A rule that fires on a scheduled backup job |
| **Near miss** | "We nearly missed that one" | A real alert buried under false positives |

2. Have the class call out anything from **Day 1 and today** that matched one of those signals. Write them on the board.

### Part B: Recognising a Good Idea (25 min)

1. Teach that recognising ideas is a competency in itself, and that most ideas die because nobody wrote them down.
2. Give the class a set of **six proposed improvements** (Demonstration Steps, Demo 4). In teams, rank them using this table:

| Criterion | Question |
|-----------|----------|
| **Impact** | How much time or risk does it remove, per week? |
| **Effort** | Can one person do it in a shift, or does it need a project? |
| **Risk** | What breaks if it goes wrong? Can we undo it? |
| **Authority** | Can an L1 do it, or does it need approval? |

3. Teams report their top two and their bottom one, with reasoning
4. Debrief: the highest-impact idea is rarely the most technically interesting one

### Part C: Write an SOP Improvement Proposal (30 min)

1. Each trainee writes **one** proposal on the form, based on something they genuinely noticed on Day 1 or Day 2:

| Field | Content |
|-------|---------|
| **What I noticed** | The observation — repetition, workaround, complaint, or near miss |
| **Why it matters** | Time cost per week, or the risk it creates |
| **What I propose** | The change, in one or two sentences |
| **Who needs to approve it** | Named role |
| **How we would know it worked** | The measure |

2. Trainees swap proposals with a partner. The partner writes **one supportive comment and one question** — this is LO3, supporting others' access to innovative practice.
3. **Collect. This is competency evidence.**

> **Trainer Tip:** Some trainees will freeze on this because they think "innovation" means something clever. Say plainly: "Propose adding one field to the handover template. That is a completely valid proposal and it is the kind that actually gets adopted."

---

## 4:00 – 4:45 PM | ADOPT ENTREPRENEURIAL MINDSET IN THE WORKPLACE (45 min)
### Unit 400311109 — LO1 and LO2

### Part A: What the Mindset Means Here (20 min)

### What to Say:
> "Entrepreneurial does not mean start a business. In this unit it means you think about the work the way an owner would — cost, waste, quality, and reputation. Let me make it concrete, because a security service is sold by the hour."

1. Put the economics on the board:

| Thing | What it costs the business |
|-------|---------------------------|
| An alert triaged well the first time | ~8 minutes of L1 time |
| The same alert escalated wrongly to L2 | ~45 minutes of L2 time, plus the L1 time |
| A missed critical alert | Client incident, contractual penalty, sometimes the contract |
| A false escalation at 3 AM | An on-call manager's night, and their trust in your judgement |

2. Draw the conclusion:
   > "Nobody is going to hand you a budget. But every triage decision you make spends somebody's money. Analysts who understand that get promoted, because they escalate the right things."

3. Cover the workplace-thinking elements the unit asks for:
   - **Quality assurance** — checking your own ticket before submitting it
   - **Cost of rework** — a badly written ticket is done twice
   - **Reliable sources** — using authoritative intel, not a forum post
   - **Customer focus** — the client wants to know what it means for them, not what the tool said
   - **Reputation** — one wrongly closed critical alert is remembered for years

### Part B: Entrepreneurial Practices Drill (25 min)

1. Give each team a **service scenario**: "Your SOC has 40 clients and 3 analysts on the night shift. Alert volume has doubled in a month. Nothing is being missed yet, but the queue is not clearing before shift end."
2. Teams have **15 minutes** to produce three recommendations, each with:
   - What it would change
   - What it would cost (time, money, or risk)
   - What could go wrong
3. Present and debrief. Expect and reward answers like: tune the noisiest rule, automate the ticket fields, group similar alerts, ask which client generates the most noise and why.

> **Debrief point:** "Notice that almost every answer was 'reduce the noise', not 'hire more people'. That instinct — fix the process before adding cost — is what this unit is asking you to demonstrate."

---

## 4:45 – 5:00 PM | DAY 2 WRAP-UP (15 min)

1. Rapid recall:
   - "What three questions turn a symptom into a problem statement?" (What exactly is happening? When did it start? What is the scope?)
   - "Where does the Five Whys stop?" (At the first thing you can act on)
   - "What are the three filters for choosing a corrective action?" (Within my authority? Reversible? Smallest thing that could work?)
   - "How long do you get to brief your L2?" (About sixty seconds)
   - "What are the four signals that innovation is needed?" (Repetition, workaround, complaint, near miss)

2. Preview Day 3:
   > "Tomorrow: information handling, safety, environment, and quality. You will learn how to judge whether a threat intelligence source can be trusted — which matters, because acting on a bad source is worse than acting on nothing."

---

## COMPETENCY EVIDENCE COLLECTED TODAY

- ✅ **400311103 LO1–LO4** — Three completed Problem-Solving Worksheets; one written action plan; observed 60-second L2 briefing
- ✅ **400311104 LO1–LO3** — Goal Sheet with personal and career goals; emotion reflection; learning-style inventory and strategy
- ✅ **400311105 LO1–LO3** — SOP Improvement Proposal; peer comment and question on a partner's proposal
- ✅ **400311109 LO1–LO2** — Service scenario recommendations with cost and risk

---

## TRAINER NOTES

- **The 60-second cut-off is the most valuable thing today.** Enforce it exactly. Trainees who ramble in class ramble on a bridge call.
- **Watch for the fixer.** Some trainees will want to jump straight to a solution and skip the problem statement. Make them write the statement anyway. On Day 9 they will be the ones who escalate before verifying.
- **Do not let the emotions session become therapy.** Fifteen minutes of honest naming, then move. The competency is recognition, not resolution.
- **Keep the fault cards.** You will reuse the "agent stopped reporting" fault as a live exercise on Day 7 when Wazuh is running, and the trainees who did the paper version today will solve the live version in half the time.
