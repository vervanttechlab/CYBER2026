# CYBER THREAT MONITORING LEVEL I
## Day 2: Solving Routine Problems on a Real Desk
### Student Handout

---

## Today's Units

| Code | Unit of Competency |
|------|-------------------|
| 400311103 | Solve/address routine problems |
| 400311104 | Enhance self-management skills |
| 400311105 | Support innovation |
| 400311109 | Adopt entrepreneurial mindset in the workplace |

---

## Problem vs Symptom

| What people report (symptom) | What is actually wrong (problem) |
|------------------------------|----------------------------------|
| "The dashboard is empty" | The agent stopped sending events |
| "I'm getting a hundred alerts" | One rule is matching normal activity |
| "The same ticket keeps appearing" | The integration is retrying on timeout |
| "The scan never finished" | The target went offline mid-scan |
| "Antivirus cleaned it but it's back" | The persistence mechanism was not removed |

> If you fix the symptom, the problem comes back tomorrow.

### Three Questions That Turn a Symptom Into a Problem Statement

1. **What exactly is happening?** — observable and specific, with no interpretation
2. **When did it start?** — and what else changed at that time
3. **What is the scope?** — one host, one team, one site, or everything

| | |
|---|---|
| **Bad** | "The SIEM is broken." |
| **Good** | "Since approximately 14:20 today, four Manila servers (SRV-MNL-01 to 04) have shown no events in the dashboard. All other hosts are reporting normally. The four affected hosts respond to ping." |

A good problem statement contains a **start time**, a **scope**, a **boundary** (what is *not* affected), and at least one piece of **evidence**.

---

## The Five Whys

Ask "why" until the answer stops being a symptom and becomes something you can change.

```
PROBLEM: The same malware detection reappears on WKS-118 every morning.

Why? → Antivirus detects and cleans the file each morning.
Why does it come back? → Something writes it back to disk.
Why? → A scheduled task runs at logon and downloads it.
Why is there a scheduled task? → It was created by the original infection.
Why wasn't it removed? → AV removed the FILE but not the PERSISTENCE.

ROOT CAUSE: Remediation was incomplete.
ACTION: Remove the scheduled task, re-scan, verify at next logon.
```

### Two Rules for the Five Whys

- **Stop at the first thing you can act on.** Going further gives you a philosophy, not a fix.
- **If your answer is a person's name, back up.** "The user clicked a link" is a training gap, not tonight's root cause. Find the technical cause first.

---

## Cause-and-Effect Analysis (Fishbone)

For any SOC fault, check these six branches:

| Branch | Ask |
|--------|-----|
| **Agent** | Is the service running? Right version? Right config? |
| **Network** | Can the host reach the server? Is a firewall rule blocking it? |
| **Server** | Is the manager up? Is the disk full? Is it accepting writes? |
| **Configuration** | Did somebody change a rule, a filter, or a log level? |
| **Host** | Did it reboot? Is it patched? Is it even powered on? |
| **Process** | Is there a change notice? Did somebody do this deliberately? |

> Then ask the question that saves your night: **"Which of these can I test in under five minutes?"** Test those first.

---

## Choosing a Corrective Action

Write down **three** options before you choose one. Then apply the filters **in this order**:

| # | Filter | If the answer is no |
|---|--------|-------------------|
| 1 | **Is it within my authority?** | It is not an option — it is an escalation |
| 2 | **Is it reversible?** | Prefer an option you can undo |
| 3 | **Is it the smallest thing that could work?** | Restart the service before you reboot the host |

> The dangerous analyst is not the one who does not know the answer. It is the one who does something big and irreversible because it felt decisive.

---

## The Action Plan

| Field | Content |
|-------|---------|
| **Problem** | One paragraph: what, when, scope, boundary |
| **Cause** | The root cause, stated as something changeable |
| **Action** | Numbered steps — each one a single verifiable act |
| **Who** | A named person or role for each step |
| **When** | A time or deadline for each step |
| **How we will know it worked** | The observable test, with a number |
| **If it does not work** | The fallback, and who to escalate to |

> **Define success in advance, with a number.** "No detection for three consecutive working days" is testable. "Seems fixed" is not.

---

## Saying the Same Plan Three Ways

| Audience | What they need | Length |
|----------|---------------|--------|
| **Your L2 / supervisor** | Technical detail, what you already tested, what you need from them | 3–4 sentences |
| **The client / user** | What is happening, what it means for them, when they hear next | 2 sentences, no jargon |
| **The ticket** | Everything, in order, with timestamps — the permanent record | As long as it needs |

> You get about **sixty seconds** with your L2. They have eleven other things happening.

---

## Unit 400311104 — Enhance Self-Management Skills

### Personal Goals vs Career Goals

| | **Personal goal** | **Career goal** |
|---|---|---|
| **About** | Who you want to be | What you want to do |
| **Timeframe** | Often lifelong | Usually 1–5 years |
| **Example** | "Support my family without being absent from it" | "Move from L1 to L2 within two years" |

### The Ladder You Are Standing On

```
  L1 Analyst  →  L2 Analyst  →  L3 / Threat Hunter  →  SOC Lead
      ↓              ↓                   ↓
  Help desk     Vulnerability      Incident Response
   support        Management          / Forensics
```

---

## MY GOAL SHEET

**Name:** _________________________ **Date:** _____________

**My personal goal:**

_______________________________________________________________

**My career goal — 1 year from now:**

_______________________________________________________________

**My career goal — 3 years from now:**

_______________________________________________________________

**Two things I must learn to reach the 1-year goal:**

1. _____________________________________________________________

2. _____________________________________________________________

**One thing I will do in the next 30 days:**

_______________________________________________________________

---

### Recognising Emotions on the Desk

| State | What it feels like | What it does to your work | What to do |
|-------|-------------------|--------------------------|-----------|
| **Alert fatigue** | Numb, clicking through | You close things without reading | Stand up. Take five. Re-read the last three. |
| **Panic** | Racing, tunnel vision | You skip steps and forget to record | Go back to the SOP. Follow it literally. |
| **Frustration** | Snappy, blaming the tool | You stop asking for help | Say out loud that you are stuck. |
| **Overconfidence** | Certain, fast, skipping checks | You escalate the wrong thing | Verify one thing you "already know". |

| Positive state | Why it helps | How to protect it |
|---------------|-------------|------------------|
| **Curiosity** | It is the engine of good triage | Give yourself ten minutes on the odd alert |
| **Calm** | Lets you follow process under pressure | Comes from having run the drill before |
| **Satisfaction** | Sustains you through quiet shifts | Notice the catches, not just the misses |

### My Reflection

**A time I felt frustrated at work or in study:**

_______________________________________________________________

**A time I felt panic or pressure:**

_______________________________________________________________

**A time I felt real satisfaction in my work:**

_______________________________________________________________

---

### Learning Style Inventory

For each pair, tick the one that is *more* true of you.

| # | A | B |
|---|---|---|
| 1 | [ ] I learn by trying it myself | [ ] I learn by watching first |
| 2 | [ ] I want the reason before the steps | [ ] I want the steps, the reason can come later |
| 3 | [ ] I like timed drills | [ ] I like time to think it through |
| 4 | [ ] I remember what I did | [ ] I remember what I read |
| 5 | [ ] I ask "what happens if I break it?" | [ ] I ask "what is the correct procedure?" |
| 6 | [ ] I get bored in long explanations | [ ] I get anxious when rushed |

**Mostly A → you learn by doing and experimenting.**
**Mostly B → you learn by watching and thinking it through.**

| If you learn mainly by... | Easy for you | Hard for you | Your strategy |
|--------------------------|-------------|-------------|--------------|
| **Doing** | Days 6–14 | Days 1–3 | Ask for a demonstration of every concept |
| **Watching** | Demonstrations | Going first | Take notes, then do it immediately while fresh |
| **Thinking it through** | SOPs, frameworks | Fast timed drills | Read ahead the night before |
| **Trying and adjusting** | Timed drills | Long procedures | Ask "what breaks if I get this wrong?" |

**My dominant style:** _________________________

**The part of this course I expect to find hardest:**

_______________________________________________________________

**One concrete strategy I will use to get through it:**

_______________________________________________________________

---

## Unit 400311105 — Support Innovation

### The Four Signals That Innovation Is Needed

| Signal | What it sounds like | Example |
|--------|-------------------|---------|
| **Repetition** | "I do this every single shift" | Manually copying alert details into the ticket |
| **Workaround** | "You just have to know to do X first" | An undocumented step everyone learned the hard way |
| **Complaint** | "This always happens on Mondays" | A rule that fires on a scheduled backup job |
| **Near miss** | "We nearly missed that one" | A real alert buried under false positives |

### Ranking an Idea

| Criterion | Question |
|-----------|----------|
| **Impact** | How much time or risk does it remove, per week? |
| **Effort** | One person in a shift, or a project? |
| **Risk** | What breaks if it goes wrong? Can we undo it? |
| **Authority** | Can an L1 do it, or does it need approval? |

---

## SOP IMPROVEMENT PROPOSAL

**Proposed by:** _________________________ **Date:** _____________

**What I noticed** *(repetition / workaround / complaint / near miss)*

_______________________________________________________________

_______________________________________________________________

**Why it matters** *(time cost per week, or the risk it creates)*

_______________________________________________________________

**What I propose**

_______________________________________________________________

_______________________________________________________________

**Who needs to approve it**

_______________________________________________________________

**How we would know it worked**

_______________________________________________________________

---

**Peer review — completed by:** _________________________

**One thing I like about this proposal:**

_______________________________________________________________

**One question I have about it:**

_______________________________________________________________

---

## Unit 400311109 — Entrepreneurial Mindset

### What Your Decisions Cost

| Thing | What it costs the business |
|-------|---------------------------|
| An alert triaged well the first time | ~8 minutes of L1 time |
| The same alert escalated wrongly to L2 | ~45 minutes of L2 time, plus your time |
| A missed critical alert | A client incident, a penalty, sometimes the contract |
| A false escalation at 3 AM | A manager's night — and their trust in your judgement |

> Nobody hands an L1 a budget. But every triage decision spends somebody's money. Analysts who understand that get promoted, because they escalate the right things.

### Entrepreneurial Practices in a SOC

- **Quality assurance** — check your own ticket before you submit it
- **Cost of rework** — a badly written ticket gets done twice
- **Reliable sources** — authoritative intel, not a forum post
- **Customer focus** — the client wants to know what it means for *them*
- **Reputation** — one wrongly closed critical alert is remembered for years

---

## Notes

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________

_______________________________________________________________
