# DAY 1 — AFTERNOON SELF-STUDY PACK
## Asynchronous session · 1:00 – 5:00 PM
### Cyber Threat Monitoring Level I

---

## Read this first

This morning we were all on the call together. That was deliberate — everything we did before lunch only works with other people present: taking down a spoken handover, reading an instruction back to the person who gave it, running a shift huddle with your team.

**This afternoon you work alone, and that is also deliberate.** Reading a procedure correctly and working out whether a change notice explains an alert is solitary work in the real job too. Nobody reads an SOP in a huddle.

Three things to be clear about:

- **This is not a half day.** It is the second half of Day 1 and it carries a unit element that the morning did not.
- **Everything below produces real evidence** that goes into your portfolio. None of it is busy-work, and none of it will be repeated in class.
- **Tasks 5 and 6 are the ones that matter most.** Between them they are the whole of *LO2 — perform workplace duties following written notices*, and they are marked. If you run short of afternoon, those two are the ones that cannot slip.

**Total time: about 3 hours 40 minutes**, in a four-hour window. You can take the tasks in any order except that Task 4 comes before Tasks 5, 6 and 8.

---

## What to complete this afternoon

| # | Task | Time | What you hand in |
|---|------|------|-----------------|
| 1 | Take the pre-test | 45 min | Submitted automatically |
| 2 | Set up your evidence folder | 15 min | A screenshot of the folder tree |
| 3 | Write up this morning's shift handover | 20 min | Completed Shift Handover Log |
| 4 | Read the Day 1 Student Handout | 30 min | Nothing — but Tasks 5, 6 and 8 assume you read it |
| 5 | **Mark up the Alert Intake SOP** | 45 min | Completed SOP Markup Worksheet |
| 6 | **Triage three written notices** | 30 min | Completed Written Notice Worksheet |
| 7 | Find and evaluate a real security advisory | 25 min | Completed Source Evaluation Sheet |
| 8 | Day 1 reflection and Day 2 preparation | 10 min | Short written answer |

**Also submit with this pack** the two documents you completed on the call this morning, if you have not already sent them:

- Your signed **Home Workstation Audit**
- Your **Huddle Observation Checklist** for the team you observed

---

# TASK 1 — Take the pre-test *(45 minutes)*

Open the link your trainer sent you.

- Sign in with the **Google account you use for this course**
- **Do not look anything up.** An honest low score is far more useful to us than a researched high one. Most people score low on a pre-test — that is exactly what it is for
- You get **one attempt**
- Do not switch tabs or Alt+Tab once you have started. The test records it

> If you see *"Google hasn't verified this app"* — click **Advanced**, then **Go to … (unsafe)**. It is our own training app.

---

# TASK 2 — Set up your evidence folder *(15 minutes)*

You will produce something almost every day for fifteen days. If you lose it, you lose your evidence. Build the filing system now, before there is anything to lose.

On your Desktop, create this structure:

```
Desktop/
  └── CTM_Level1/
        ├── Evidence/
        │     ├── Day_01/
        │     ├── Day_02/
        │     │   ... through ...
        │     └── Day_15/
        ├── Worksheets/
        ├── Tools/
        └── Scans/
```

**How:** right-click an empty part of the Desktop → **New** → **Folder** → type the name → **Enter**. Double-click to go inside, and repeat.

> **Use `Day_01`, not `Day_1`.** Windows sorts text, not numbers. With the leading zero, `Day_10` sorts after `Day_09` where it belongs. Without it, `Day_10` sorts before `Day_2`. Small habit, saves confusion for fifteen days.

**Hand in:** a screenshot of `CTM_Level1` with the folders visible.
*(Press `Win + Shift + S`, drag a box around it, then paste into a document and save.)*

Save everything from today into `Evidence/Day_01/` — this morning's audit and observation checklist included.

---

# TASK 3 — Write up this morning's shift handover *(20 minutes)*
### Unit 400311101 · LO1 — Follow routine spoken messages

This morning your trainer delivered a spoken shift handover and you took notes while listening. Now turn those notes into the document a real analyst produces.

## Step 1 — Open the Shift Handover Log template

Fill in every one of the five sections from **your own notes**:

| Section | What goes in it |
|---------|----------------|
| **Open items** | Tickets still in progress, with ticket number and current state |
| **Escalated** | What went to L2/L3 and who owns it now |
| **Watch items** | Things that are not yet incidents but need eyes |
| **System status** | Anything down, degraded, or in maintenance |
| **Client notes** | Anything a client asked for or complained about |

## Step 2 — Be honest about the gaps

**Work from your notes only.** Do not go back to a recording, and do not ask a classmate to fill in what you missed.

If you did not catch something — a hostname, a ticket number, a time — **write that down as a gap**, like this:

> *Watch item: connection attempts to — could not hear the hostname clearly. Would confirm with outgoing shift before acting.*

> **This is the point of the task.** A handover log with an honest gap and a note saying you would confirm it is *better work* than one where every field is filled in with a plausible guess. In a real SOC, a guessed hostname sends the next shift to the wrong machine. Your trainer is marking for exactly this.

## Step 3 — Sign and date it

**Hand in:** the completed Shift Handover Log.

---

# TASK 4 — Read the Day 1 Student Handout *(30 minutes)*

Read it properly — not a skim. This morning covered the shape of a SOC in half an hour; the handout carries the detail, and Tasks 5, 6 and 8 assume you have it.

Pay particular attention to:

- **What each sensor sees** — AV, firewall, WAF, DLP, EDR, NDR
- **A real shift, hour by hour** — watch for the moment the analyst does the most valuable thing anybody did all night, and notice that no tool did it
- **The RACI grid** — who is Responsible, Accountable, Consulted and Informed at each stage of a single alert. We only touched this on the call
- **Who is *not* allowed to decide containment** — and what you say when somebody asks you to
- **The four tiers**, and where a Level 1 analyst sits

You will be asked about these on Day 2. Nothing on that list needs a computer to understand — it needs thirty quiet minutes.

---

# TASK 5 — Mark up the Alert Intake SOP *(45 minutes)*
### Unit 400311101 · LO2 — Perform workplace duties following written notices

**This is the most important task this afternoon.** An SOP is not a suggestion and it is not a training document. It is the answer to *"why did you do that?"* when somebody asks you six months later.

## Step 1 — Highlight the verbs
Open **Document 1** in your SOP Pack — `SOP-SOC-001`. Go through it line by line and mark every occurrence of:

**shall** · **must** · **should** · **may** · **shall not**

Use a highlighter on paper, or bold them in a copy on your computer.

Here is what each one binds you to:

| Word | What it means for you |
|------|----------------------|
| **shall** / **must** | Mandatory. No discretion |
| **should** | Expected. Deviating means justifying it |
| **may** | Your judgement — usually with a condition attached |
| **shall not** | Prohibited. Usually a limit on your authority |
| **within X minutes** | A clock is running. Note when it starts |

## Step 2 — Complete the worksheet

For each step of `SOP-SOC-001`, fill in this table.

| Step | Binding word | What exactly it requires of you | Is a clock running? From when? |
|------|-------------|--------------------------------|-------------------------------|
| 3.1 | | | |
| 3.2 | | | |
| 3.3 | | | |
| 3.4 | | | |
| 3.5 | | | |
| 3.6 | | | |
| 3.7 | | | |
| 3.8 | | | |

## Step 3 — Answer these four questions in writing

**Q1.** An alert arrives at 22:00. You assess it as High at 22:20. What is your notification deadline, and why?

_______________________________________________________________

**Q2.** You assess an alert as Low and close it without writing anything down. Which step did you breach, and what exactly was missing?

_______________________________________________________________

**Q3.** A client phones you directly and asks you to disconnect an infected laptop from the network. What do you do, and which step of the SOP tells you that?

_______________________________________________________________

**Q4.** A Change Notice explains an alert, so you close it. What must you record before you do, and which step makes it mandatory?

_______________________________________________________________

> **Take your time on Q1.** Almost everybody gets it wrong the first time, and the reason they get it wrong is the single most common source of missed SLAs in real security operations centres. Read §3.3 twice. We open Day 2 with this question.

> **Q3 is the one that connects to this morning.** You already know the answer from the huddle briefing — you are Responsible for the triage and the ticket, never Accountable for a containment decision. Now find the step that says so.

**Hand in:** the completed table and your four answers.

---

# TASK 6 — Triage three written notices *(30 minutes)*
### Unit 400311101 · LO2

Read **Documents 4, 5 and 6** in your SOP Pack — the vendor advisory, the change notice, and the client SLA notice.

For **each** of the three, answer these four questions:

| | Advisory 2026-0418 | Change Notice CHG-2026-1177 | Northwind SLA Notice |
|---|---|---|---|
| **1. What am I being told?** | | | |
| **2. What am I required to do, and by when?** | | | |
| **3. Which systems or clients does it affect — and which does it NOT?** | | | |
| **4. What would I do if this conflicted with the SOP?** | | | |

## Then answer these three

**A.** It is 23:30 on 22 April. Four servers just went offline in your console: `SRV-MNL-01` through `SRV-MNL-04`. Incident, or not? Why?

_______________________________________________________________

**B.** Same night, same time. `SRV-CEB-02` goes offline. Incident, or not? Why?

_______________________________________________________________

**C.** The Northwind SLA notice tells you to do something different from what SOP-SOC-001 §3.3 says. Which do you follow, and how do you know?

_______________________________________________________________

> Question C is the one worth thinking hardest about. When two documents give you contradictory instructions, the correct behaviour is **not** to pick the stricter one, or the newer one, or the one you prefer. Work out what the actual rule is.

> **Row 3 is doing more work than it looks like.** A notice tells you what it does **not** cover just as clearly as what it does. That is the whole of question B.

**Hand in:** the completed grid and your three answers.

---

# TASK 7 — Find and evaluate a real security advisory *(25 minutes)*
### Unit 400311106 (preview) — Access and maintain information

An analyst's day is full of information that might be true. Judging a source is a skill, and it is one you can start practising today.

## Step 1 — Find one
Search for a **security advisory or vulnerability notice published in the last 30 days**. Good starting points:

- A vendor's own security advisory page — Microsoft, Cisco, Fortinet, VMware, Google
- A national CERT — CERT-PH, US-CISA, and their equivalents
- The NVD / CVE database
- A recognised security news site

Pick **one** advisory. Any product, any vendor.

## Step 2 — Complete the evaluation sheet

| Question | Your answer |
|----------|------------|
| What is the advisory called, and what is its reference number? | |
| **Who published it?** Is that the vendor themselves, a government body, a news site, or an individual? | |
| **When was it published?** Is it current? | |
| **What product and versions are affected — and which are NOT?** | |
| **Is there a fix?** What is it? | |
| **How would this change what a Level 1 analyst does tonight?** | |
| **How confident are you in this source, and why?** | |

## Step 3 — Rank your source

| Tier | What it means | Is yours here? |
|------|--------------|---------------|
| **Authoritative** | The vendor, or a national CERT. Act on it | |
| **Credible** | An established security firm or researcher. Verify against the vendor | |
| **Unverified** | A news article, forum post, or social media. **Never act on it alone** | |

> This is a genuinely useful habit. The single fastest way for a new analyst to lose credibility is to escalate something they read on a forum, which turned out to be wrong.

**Hand in:** the completed evaluation sheet with a link to your advisory.

---

# TASK 8 — Day 1 reflection and Day 2 preparation *(10 minutes)*

Short answers. Be honest — this is not marked for correctness, it tells your trainer where to spend Day 2.

**1. In this morning's handover, what did you miss?** Be specific — a hostname, a ticket number, a whole section?

_______________________________________________________________

**2. In the huddle drill, did you speak?** If your team ran out of time before you did, say so.

_______________________________________________________________

**3. Which of this afternoon's tasks took you longest, and where exactly did you get stuck?**

_______________________________________________________________

**4. One thing from today you would want explained again on Day 2:**

_______________________________________________________________

**5. What do you most want to be able to do by Day 15?**

_______________________________________________________________

> Question 3 is the useful one. "The SOP task was hard" tells your trainer nothing. "I could not work out whether the fifteen-minute clock started at 22:00 or 22:20" tells them exactly what to teach first tomorrow.

---

## HANDING IN YOUR WORK

Put everything into `Evidence/Day_01/` on your own computer, **and** submit copies to your trainer by the method they gave you on the call this morning.

### Checklist before you finish

**From this morning:**
- [ ] Home Workstation Audit — completed and signed
- [ ] Huddle Observation Checklist — for the team I observed

**From this afternoon:**
- [ ] Pre-test submitted — I saw the confirmation screen
- [ ] Screenshot of my `CTM_Level1` folder structure
- [ ] Shift Handover Log — written from my own notes, gaps included
- [ ] Day 1 Student Handout read
- [ ] SOP Markup Worksheet — table + four answers
- [ ] Written Notice Worksheet — grid + three answers
- [ ] Source Evaluation Sheet — with a link to the advisory
- [ ] Day 1 reflection — five answers

**Your name:** _________________________ **Date completed:** _____________

---

## WORKING TOGETHER — WHERE THE LINE IS

You have your team's contact details from this morning. Use them.

| You may | You may not |
|---------|------------|
| Ask a teammate what a word in the SOP means | Copy their worksheet |
| Argue about the answer to Task 6 question C | Submit the same wording |
| Check you found the right document in the pack | Fill in your handover log from their notes |

Task 3 in particular is **yours alone** — the whole point is what *you* heard this morning. Borrowing someone else's notes destroys the evidence.

---

## STILL OUTSTANDING — FOR OUR FIRST DAY ON SITE

Two documents cannot be signed while we are working remotely, because both of them describe the training lab itself:

| Document | Why it waits |
|----------|-------------|
| **Lab OSH Checklist** | It is a safety check of the training lab workstation you will use — not the desk you are at today |
| **Green Lab Pledge** | It is a commitment about how the training lab is run and powered down |

Your trainer has recorded both as outstanding. You will sign them on our first day on site. Your **Home Workstation Audit**, completed on the call this morning, is your OSH evidence until then — and it stays in your portfolio either way.

---

## WHAT DAY 2 LOOKS LIKE

Day 2 is problem solving — not puzzle problem solving, real desk faults. An agent that stopped reporting. Duplicate tickets. A false-positive storm that buries your queue.

**We open with the SOP debrief.** Bring your marked-up copy and your answer to Q1. Most of the class will have it wrong, and the conversation about *why* is the most useful twenty minutes of the week.
