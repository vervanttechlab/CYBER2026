# DAY 2 — ACTIVITY PACK
## Solving Routine Problems on a Real Desk
### Everything you work on today

---

## WHAT IS IN THIS PACK

| Part | What | When |
|------|------|------|
| **1** | Fault Card 1 — "The Empty Dashboard" | Morning, 9:40 |
| **2** | Problem-Solving Worksheet A | Morning, with Fault Card 1 |
| **3** | Fault Card 2 — "The Alert Storm" | Morning, 10:55 |
| **4** | Problem-Solving Worksheet B | Morning, with Fault Card 2 |
| **5** | The 60-second briefing — what has to fit | Morning, 11:00 |
| **6** | Team scenario — "Forty Clients, Three Analysts" | Morning, 11:35 |
| **7** | Your afternoon — six tasks | Afternoon, from 1:00 |

Your **Goal Sheet** and your **SOP Improvement Proposal form** are in the Student Handout, not in here.

> **You will not have enough information to be certain about these faults.** That is deliberate. You never do in real life either. Work with what you have and say clearly what you would need to find out.

---
---

# PART 1 — FAULT CARD 1

## "The Empty Dashboard"

```
It is 14:47. A colleague says: "The dashboard is empty for Manila."

WHAT YOU CAN SEE

  - SRV-MNL-01, -02, -03, -04: last event 14:20, 14:20, 14:21, 14:20
  - All other 46 hosts: events arriving normally, right now
  - All four Manila hosts reply to ping
  - Server disk usage: 61%
  - No change notice is listed for today
  - The Manila site had a scheduled power interruption notice
    posted by Facilities (not IT) for 14:00 - 14:30
```

**You also have your team's fault log file** — `Fault_Log_Team_A.csv` or whichever your team was sent.

**You have 15 minutes.** Fill in Worksheet A.

---
---

# PART 2 — PROBLEM-SOLVING WORKSHEET A

**Team:** _________________________ **Fault Card:** 1 **Date:** _____________

---

## STEP 1 — The problem statement

Write **one paragraph.** It must contain all four of these. Tick them off when you have them.

☐ **What exactly is happening** — observable, no interpretation
☐ **When it started** — and what else changed at that time
☐ **The scope** — one host, one site, everything?
☐ **The boundary** — what is *not* affected

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

> **The test:** could an analyst who has never seen this fault pick it up from your paragraph and carry on? If not, keep writing.

---

## STEP 2 — Five Whys

**PROBLEM:** ___________________________________________________________________

**Why?** → _____________________________________________________________________

**Why?** → _____________________________________________________________________

**Why?** → _____________________________________________________________________

**Why?** → _____________________________________________________________________

**Why?** → _____________________________________________________________________

**ROOT CAUSE:** ________________________________________________________________

> **Stop at the first thing you could actually do something about.** If you run out of information, write down what you would need to find out to go one step further.
>
> **If your last answer is a person's name, back up.** That is a training gap, not a root cause you fix tonight.

---

## STEP 3 — Where could it be hiding?

Use the six branches. Write down every possibility — do not filter yet.

| Branch | Possible causes |
|--------|----------------|
| **Agent** | |
| **Network** | |
| **Server** | |
| **Configuration** | |
| **Host** | |
| **Process** | |

---

## STEP 4 — What can you test cheaply?

Now rank them. **Cheapest to test goes first.**

| Rank | Possible cause | How I would test it in under 5 minutes |
|------|---------------|---------------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

**Which one would you test first, and why that one?**

_______________________________________________________________________________

---

## STEP 5 — What you would need to know

**What information is missing that would settle this?**

_______________________________________________________________________________

_______________________________________________________________________________

---
---

# PART 3 — FAULT CARD 2

## "The Alert Storm"

> This one is harder, and the first symptom is misleading. Read everything before you decide.

```
It is 22:10. Your queue has 214 open alerts. It normally has 30.

WHAT YOU CAN SEE

  - 186 of them are the same alert: "Blocked outbound connection"
  - All 186 are from one host: WKS-204
  - They started at 21:55 and are still arriving, about 12 per minute
  - The destination IPs are all different
  - The destinations are all on port 443
  - WKS-204's user, aflores, logged off at 18:00
  - WKS-204 ran a Windows Update cycle starting 21:50
```

**You have 12 minutes.** Fill in Worksheet B — the full action plan this time.

---
---

# PART 4 — PROBLEM-SOLVING WORKSHEET B

**Team:** _________________________ **Fault Card:** 2 **Date:** _____________

---

## STEP 1 — The problem statement

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

---

## STEP 2 — The cause

**Root cause, stated as something you could change:**

_______________________________________________________________________________

_______________________________________________________________________________

> **Before you commit to an answer — what happened just before the symptom started?** Look at the timings again.

---

## STEP 3 — Three options, three filters

Write **three** options. Do not stop at the first idea.

| Option | What it costs | What it risks | Within my authority? |
|--------|--------------|--------------|---------------------|
| 1 | | | ☐ Yes ☐ No |
| 2 | | | ☐ Yes ☐ No |
| 3 | | | ☐ Yes ☐ No |

Now apply the filters **in this order** and circle your choice above.

1. **Is it within my authority?** If no, it is not an option — it is an escalation.
2. **Is it reversible?** Prefer the fix you can undo.
3. **Is it the smallest thing that could work?**

**Which option did you choose, and which filter decided it?**

_______________________________________________________________________________

---

## STEP 4 — The action plan

| Field | Your answer |
|-------|------------|
| **PROBLEM** | |
| **CAUSE** | |
| **ACTION 1** | *(who / when)* |
| **ACTION 2** | *(who / when)* |
| **ACTION 3** | *(who / when)* |
| **ACTION 4** | *(who / when)* |
| **HOW WE WILL KNOW IT WORKED** | |
| **IF IT DOES NOT WORK** | |

> **Every action needs a named person and a time.** "Someone should check" is not an action.
>
> **"How we will know it worked" must be testable.** A number, a window, an observation. "Seems fixed" is not a test.

---
---

# PART 5 — THE 60-SECOND BRIEFING

Your presenter briefs the trainer as if they were your L2 supervisor.

**Sixty seconds. You will be cut off at sixty, mid-sentence if necessary.**

That is not the trainer being difficult. Your L2 at ten past ten at night has eleven other things happening. Sixty seconds is genuinely what you get.

## What has to fit

| | | Tick |
|---|---|---|
| **1** | The ticket or host — say it first | ☐ |
| **2** | What is wrong, in one sentence | ☐ |
| **3** | What you have already checked | ☐ |
| **4** | **What you are asking them for** | ☐ |

> **Number 4 is the one people run out of time for**, and it is the only one that cannot be dropped. A briefing without it is a complaint, not an escalation.
>
> **Lead with the host and what you need. Fill in the detail afterwards.** If you spend forty seconds on background you will never reach the ask.

## Practise it once before your turn

Say it out loud to your team. Time it. If you are over sixty seconds, cut the background — not the ask.

---
---

# PART 6 — TEAM SCENARIO

## "Forty Clients, Three Analysts"

```
Your security operations centre has 40 clients.
Three analysts work the night shift.

Alert volume has DOUBLED in the last month.

Nothing has been missed yet.
But the queue is not clearing before shift end,
and it is getting worse each week.
```

**You have 10 minutes.** Produce **three** recommendations.

| | What it would change | What it would cost *(time, money or risk)* | What could go wrong |
|---|---|---|---|
| **1** | | | |
| **2** | | | |
| **3** | | | |

**Which of your three would you do first, and why?**

_______________________________________________________________________________

_______________________________________________________________________________

> **A hint about what good looks like here.** Before you recommend hiring anyone, ask what is generating the extra volume — and whether all of it needed to become an alert in the first place.

---
---

# PART 7 — YOUR AFTERNOON

**1:00 to 5:00, on your own. About 3 hours 30 minutes.**

| # | Task | Time | Where | Hand in |
|---|------|------|-------|---------|
| 1 | Set your personal and career goals | 40 min | Student Handout — My Goal Sheet | Goal Sheet |
| 2 | Recognising emotions — written reflection | 30 min | Student Handout | Three honest sentences |
| 3 | Learning-style inventory and your strategy | 30 min | Student Handout — Goal Sheet part 2 | Goal Sheet |
| 4 | Write one SOP Improvement Proposal | 40 min | Student Handout — proposal form | Proposal form |
| 5 | **Swap proposals with a partner** | 20 min | Message your teammate | One comment, one question |
| 6 | Finish Worksheets A and B from this morning | 30 min | This pack | Both worksheets |

> **Task 5 needs another person.** You have your team's contact details from Day 1. Do not leave it until five o'clock — your partner is working to the same deadline.

## Three notes on the afternoon tasks

**Task 1 — the thirty-day item is the one that matters.** One personal goal, a one-year and a three-year career goal, two things you must learn. Then one thing you will actually do in the next thirty days. Everything above that line is a wish until something below it is done. Make it small and real.

**Task 2 — your reflection is private.** Nobody reads it but your trainer, and they are not marking whether your feelings are correct. They are marking whether you can notice them. Write it honestly or the task is worthless.

**Task 4 — innovation does not mean clever.** Look at the four signals: repetition, a workaround, a complaint, a near miss. Something you genuinely noticed on Day 1 or today. *"Add one field to the handover template"* is a completely valid proposal — and it is the kind that actually gets adopted.

---

## HANDING IN

- [ ] Problem-Solving Worksheet A — Fault Card 1
- [ ] Problem-Solving Worksheet B — Fault Card 2, with the action plan
- [ ] Team scenario recommendations
- [ ] Goal Sheet — goals, emotions, learning style
- [ ] SOP Improvement Proposal
- [ ] My comment and question on a partner's proposal

Save everything in `Evidence/Day_02/` **and** send copies to your trainer.

**Your name:** _________________________ **Date:** _____________
