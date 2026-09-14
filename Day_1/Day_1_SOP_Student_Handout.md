# THE SOP PACK — STUDENT HANDOUT
## The Three Documents That Run Your Desk
### Cyber Threat Monitoring Level I · Day 1 Afternoon

---

## HOW TO USE THIS

**Read this first, then do the Night Shift activity with it open beside you.**

This handout explains the three procedures. It does **not** contain the answers to the activity — you work those out yourself, and we go through them on Day 2.

The last page is a **quick reference card**. Once you have read the rest, that one page is all you need open while you work.

**Keep this.** You will use it again on Days 6 to 10 when you triage real alerts, and again on Day 15 in your assessment.

---
---

# 1. WHAT AN SOP IS

**SOP stands for Standard Operating Procedure.**

That is all it means: a written instruction for how a job gets done — the same way, every time, by whoever happens to be on shift.

Nothing more mysterious than that. A recipe is an SOP. The laminated card next to a coffee machine is an SOP.

## Why "the same way, every time" matters

You work a shift. Somebody else takes over from you. If you assess alerts your way and they assess them their way, nobody can trust anybody else's tickets — and a queue you cannot trust is worse than no queue at all.

## Why anyone bothers writing it down

An SOP is the answer to one question:

> ## "Why did you do that?"
> asked six months later, by somebody who was asleep when you did it.

Here is the practical version:

| What happened | Whose problem it is |
|---------------|-------------------|
| You **followed** the procedure and the outcome was bad | A **process** problem. The company fixes the process |
| You **ignored** the procedure and the outcome was bad | **Your** problem. Entirely |

**The procedure protects you.** It is the reason you can make a decision at two in the morning, alone, with incomplete information, and still be defensible in daylight.

People who resent procedures usually have not yet had a decision reviewed. People who have been through that review love them.

---
---

# 2. YOUR THREE DOCUMENTS

| Document | What it tells you | When you open it |
|----------|------------------|-----------------|
| **`SOP-SOC-001`** Alert Intake | Exactly what to do when an alert arrives, step by step | **Every alert** |
| **`SOP-SOC-002`** Severity Matrix | How bad is it — Critical, High, Medium, Low | **Every alert** |
| **`SOP-SOC-003`** Escalation Matrix | Who to contact, how, and how fast | Every escalation |

Plus three sample notices — a **vendor advisory**, a **change notice**, and a **client SLA notice**. Those are the documents that *change* the rules, and you will need all three tonight.

---
---

# 3. READ THE VERBS, NOT THE SENTENCES

The most important words in any procedure are the small ones.

| Word | What it means for you |
|------|----------------------|
| **shall** / **must** | Mandatory. You have no choice |
| **should** | Expected. If you skip it, you must be able to justify why |
| **may** | Your judgement — and almost always there is a condition attached |
| **shall not** | You have no authority. This is the edge of your role |
| **within X minutes** | A clock is running. Your job is to know **when it starts** |

## Work through one example

> *"The analyst **may** close an alert assessed as Low without escalation, **provided the assessment is documented.**"*

Read it quickly and you hear: *I am allowed to close Low alerts.* Fine. Moving on.

Read it properly and the permission has a price attached. You may close it — **if** you write down why.

Close it without writing anything and you did not use your judgement. **You broke the procedure**, while getting the severity completely right.

> **When you read a procedure, find the verb first.** Then find the condition attached to it. The condition is usually the part that matters.

---
---

# 4. `SOP-SOC-001` — THE ALERT INTAKE PROCEDURE

Eight steps. You do not need to memorise them. You need to know what is in there so you can find it fast.

| Step | Verb | What it requires |
|------|------|-----------------|
| **3.1** | SHALL | Record alert ID, source system, timestamp, affected host — **within 5 minutes of receipt** |
| **3.2** | SHALL | Assess against the Severity Matrix **before any other action** |
| **3.3** | MUST | Notify the client for Critical or High — **within 15 minutes of assessment** |
| **3.4** | SHOULD check / SHALL record | Check for a Change Notice. If one explains the alert, recording the reference is **mandatory** |
| **3.5** | MAY | Close a Low without escalation — **provided it is documented** |
| **3.6** | **SHALL NOT** | **Take containment action on any host.** Containment is the SOC Manager's, only |
| **3.7** | SHALL | Record every action, its time, and who authorised it |
| **3.8** | SHALL | Complete a handover log at end of shift |

## Step 3.6 is the one to remember

> ## You cannot disconnect, isolate, or shut down anything. Ever.

Not "should avoid." Not "only with care." **Shall not.**

At some point — possibly in your first month — a frightened client will ask you to do exactly this. What you say is:

> *"I do not have the authority to do that. I am escalating this to the SOC Manager now and they will call you back."*

Then you escalate **immediately** — not just say it to end the call.

**Wanting to help is right. Doing it yourself is what is wrong.** You do not know what else that machine is doing, whether disconnecting it destroys evidence somebody needs, or whether it takes a production system down with it.

---
---

# 5. THE CLOCK

This is the detail that catches almost every new analyst, so read this page twice.

## Worked example

```
22:00   The alert arrives in your queue           ← RECEIPT
22:20   You finish assessing it as High           ← ASSESSMENT
22:35   Client notification deadline
```

**Step 3.3 says "within 15 minutes of assessment."**

Assessment was 22:20. Fifteen minutes later is **22:35**.

## The mistake almost everyone makes

Reading 3.3 quickly, you start the clock at 22:00 — when the alert arrived — and answer 22:15.

That is a completely sensible way to read it. It is also wrong, and it is the **single most common cause of missed notification deadlines in real security operations centres.** Not laziness. This exact misreading.

## Two separate clocks

Step 3.1 gave you a different clock: record four fields within 5 minutes of **receipt** — so by 22:05.

If you missed that, you have breached 3.1. **But breaching 3.1 does not move the 3.3 deadline.** They run from two different events, and missing one does not buy you time on the other.

> **For the rest of your career:** when you see "within X minutes," the question is never *how long.* It is **from when.**

---
---

# 6. `SOP-SOC-002` — THE SEVERITY MATRIX

You judge **impact and certainty together.** How bad would this be, and how sure am I?

| Severity | What it means | Examples | Notify client | Escalate to |
|----------|--------------|----------|--------------|-------------|
| **CRITICAL** | Active harm now, or imminent | Ransomware encrypting · confirmed C2 traffic · active data exfiltration · domain admin compromise | **Within 10 min** | L2 **and** SOC Manager, immediately |
| **HIGH** | Confirmed malicious, contained or not yet spreading | Malware that failed to clean · credential dumping tool · successful logon after many failures · DLP block on sensitive data | Within 15 min | L2 |
| **MEDIUM** | Suspicious, needs verification, no confirmed harm | Adware · blocked exploit attempt · unusual process on one host · unexpected agent offline | Within 4 hours | L2 if unresolved at end of shift |
| **LOW** | Routine, expected, or already handled by the tool | Blocked port scan · quarantined test file · policy violation with no data at risk | End of shift summary | Nobody — you may close it |

> **Critical is faster than High.** Ten minutes, not fifteen. Check the row — do not assume.

## THE FOUR RULES THAT BEAT THE TABLE

**These sit underneath the Matrix, and they override it.** Most people read the table, find their row, and never scroll down. Do not be most people.

### Rule 1 — Sensitive systems go up one level

Anything on a **domain controller**, a **backup server**, or a **finance system** is raised one level.

*Why:* a domain controller holds every credential in the organisation. A problem there is not one machine — it is potentially every account in the company.

### Rule 2 — A phone call is at least Medium

Anything a client reports **by phone** is treated as at least Medium until assessed.

*Why:* a human being bothered to pick up a phone. That is a signal in itself.

### Rule 3 — When stuck, go higher

If you cannot decide between two levels, **take the higher one and write down why.**

### Rule 4 — Uncertainty is not Low

> ## "I don't know what this is" is Medium, minimum.

**Low is not a filing cabinet for things you have not worked out yet.** Low is a positive statement: *I know what this is, and it does not matter.*

An unknown process is not routine. It is not expected. The tool did not handle it. So it is not Low.

> **Nobody has ever been disciplined for over-assessing with a documented reason.**
>
> Over-assessing with a reason costs somebody twenty minutes. Under-assessing can cost a company its weekend.

---
---

# 7. `SOP-SOC-003` — THE ESCALATION MATRIX

| Severity | Contact | Method | Within | If no answer |
|----------|---------|--------|--------|-------------|
| **CRITICAL** | L2 on shift, **then** SOC Manager | Phone, then ticket | Immediately | Call the next name on the on-call list. **Keep calling. Never leave a Critical unowned** |
| **HIGH** | L2 on shift | Ticket, then chat | 15 min | SOC Manager after 30 min with no response |
| **MEDIUM** | L2 on shift | Ticket | End of shift | Carry it in the handover |
| **LOW** | Nobody | Ticket only | — | — |

## Who is who

| Role | When you contact them |
|------|----------------------|
| **L2 Analyst** | Your first escalation for anything above Low |
| **SOC Manager** | Critical incidents · containment decisions · client disputes · anything you were asked to do that you believe you should not |
| **IT Department Manager** | Things the client's own IT team must act on — patching, account lockouts, server access |
| **Information Security Manager** | Policy breaches, insider concerns, anything involving staff conduct |
| **Security solution vendor** | The tool itself is failing — not detecting, not updating, console down |
| **Chief Information Security Officer (CISO)** | **Only through the SOC Manager.** An L1 never contacts the CISO directly |

## The six things in every escalation

No exceptions. All six, every time.

| | |
|---|---|
| **1** | **Ticket number** |
| **2** | **What was detected** — in one sentence |
| **3** | **Affected hosts and users** — exact names, spelled out |
| **4** | **What you have already checked** — including whether a Change Notice covers it |
| **5** | **Your severity assessment, and why** |
| **6** | **What you are asking for** — a decision, an action, or just awareness |

> ## An escalation without number 6 is a complaint, not an escalation.

If you tell L2 "there is credential dumping on DC-01," you have told them something is wrong. You have not told them what you want. Do you need a decision? An action? Are you just making sure they know?

Say it. *"I am asking you to take ownership and scope this."* Six seconds of extra typing, and it is the difference between an escalation people act on and one that sits there.

---
---

# 8. THE THREE NOTICES

These change the rules. Three of tonight's eight alerts turn on them.

## Vendor advisory

**Says:** the tool itself is misbehaving.

Changes how you treat a particular detection type — usually "verify manually before escalating."

> **Read the last paragraph.** Advisories state what they do **not** apply to. An advisory about signed Microsoft files says nothing about an unsigned file in a Downloads folder.

## Change notice

**Says:** a system will be worked on, at this time.

**Scheduled change is the number one cause of false alerts.** If you do not read the change notices, you will spend a whole night investigating an "attack" that is the IT team patching servers exactly as they said they would.

> **A change notice is a LIST, not a general permission to ignore things.** If it names four servers, it says nothing about a fifth. And "the notice says nothing" means you treat it completely normally.

## Client SLA notice

**Says:** this client's timings are different from the standard.

**SLA = Service Level Agreement** — the contract term for how fast you must respond.

---

## WHEN TWO DOCUMENTS DISAGREE

This is the most transferable idea in the whole pack.

> ## Do not pick the stricter one. Do not pick the newer one. Do not pick the one you prefer.
> ## Check whether the notice has the AUTHORITY to override.

**A document that can override says so, in words.** It will contain a sentence like *"this supersedes section X."*

If it does not say so, it cannot. And if you genuinely cannot tell — **ask.**

> Choosing the stricter option feels safe and responsible. It is still guessing. The rule is about authority, not caution.

---
---

# 9. QUICK REFERENCE CARD

**Once you have read the rest, this page is all you need open while you work.**

---

### For every single alert

```
1. RECORD IT          4 fields, within 5 min of receipt        [3.1]
2. ASSESS IT          Severity Matrix, before anything else    [3.2]
3. CHECK THE RULES    The four override rules under the table
4. CHECK FOR A NOTICE Advisory? Change notice? SLA notice?     [3.4]
5. NOTIFY             Critical 10 min · High 15 min            [3.3]
                      — from ASSESSMENT, not receipt
6. ESCALATE           Escalation Matrix. All six items
7. RECORD EVERYTHING  Actions, times, who authorised           [3.7]
```

### The four override rules

```
1. Domain controller / backup / finance   →  UP one level
2. Client reported it by phone            →  at least MEDIUM
3. Stuck between two levels               →  take the HIGHER, say why
4. "I don't know what this is"            →  MEDIUM minimum, never Low
```

### Severity at a glance

| | Notify | Escalate |
|---|---|---|
| **CRITICAL** | 10 min | L2 **+** SOC Manager, phone first |
| **HIGH** | 15 min | L2 |
| **MEDIUM** | 4 hours | L2 if unresolved at shift end |
| **LOW** | Shift summary | Nobody — close it, **with documentation** |

### The six things in an escalation

```
1 Ticket number          4 What you already checked
2 What was detected      5 Your severity, and why
3 Hosts and users        6 WHAT YOU ARE ASKING FOR
```

### Three things you can never do

```
✗  Take containment action                        [3.6]
✗  Close a Low without documenting it             [3.5]
✗  Contact the CISO directly                      [SOP-SOC-003]
```

---
---

## NOTES

*Use this space while you work through the Night Shift activity. Write down anything you had to look up twice — that is the thing you will forget on Day 6.*

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________

---

**Name:** _________________________ **Date issued:** _____________

> **Bring this to every session.** Mark it up. A clean SOP is one nobody has read.
