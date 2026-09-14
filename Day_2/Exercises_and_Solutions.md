# DAY 2 — EXERCISES AND SOLUTIONS
## Complete Exercise Pack with Model Answers

---

## Exercise 1: Rewrite the Symptom as a Problem

**Objective:** Turn what somebody tells you into something somebody else could work on.
**Unit link:** 400311103 LO1 — PC 1.1, 1.2

### Instructions:
Each row below is what a colleague actually says to you. Rewrite it as a problem statement
containing all four elements: **what exactly is happening**, **when it started**, **the
scope**, and **the boundary** (what is *not* affected).

| # | What they say | Your problem statement |
|---|--------------|----------------------|
| 1 | "The dashboard is empty." | |
| 2 | "I'm getting a hundred alerts." | |
| 3 | "Antivirus says it cleaned it but it's back." | |
| 4 | "The scan never finished." | |
| 5 | "Nothing's working." | |

### Model Answers:

**1.** "Since approximately 14:20 today, four Manila servers — SRV-MNL-01 through 04 — have
shown no events in the dashboard. All other monitored hosts are reporting normally. The four
affected hosts respond to ping."

**2.** "Since 21:55, the alert queue has received 186 instances of 'Blocked outbound
connection', all from one host, WKS-204, arriving at about 12 per minute. No other host is
generating this alert. All destination addresses are different and all are on port 443."

**3.** "Detection 'Trojan.Agent.XZ' has been raised on WKS-118 on four consecutive working
days, each time between 08:05 and 08:20. The AV log shows the file quarantined successfully
each time. No other host is affected. The user logs in at approximately 08:00."

**4.** "The scheduled vulnerability scan of the Cebu subnet started at 02:00 and stopped at
02:47 with 34 of 96 hosts completed. The scanner reports no error. The remaining 62 hosts
were not attempted. The previous night's scan of the same subnet completed normally."

**5.** "As of 09:15, this workstation cannot open the Wazuh dashboard, cannot browse to any
external site, and has no reply from the default gateway. Other workstations in the same room
are working. The network cable is connected and the port light is on."

### What to check in your own answers

| Element | Was it there? |
|---------|--------------|
| A specific, observable symptom — not an interpretation | |
| A **time** the problem started | |
| The **scope** — how many, which ones | |
| The **boundary** — an explicit statement of what is working | |
| At least one piece of **evidence** you actually checked | |

> The boundary line is the one people leave out, and it is the most valuable sentence in the
> statement. "All other hosts are reporting normally" eliminates half the possible causes
> before anybody touches a keyboard.

---

## Exercise 2: Five Whys

**Objective:** Drive to a root cause, and stop at the right place.
**Unit link:** 400311103 LO2 — PC 2.1

### Instructions:
Complete the chain for the fault below. Stop when you reach something you could actually
act on tonight.

```
PROBLEM: A user's browser keeps redirecting to unwanted pages, even
         though antivirus reported the adware as "cleaned" three days ago.

Why? →

Why? →

Why? →

Why? →

Why? →

ROOT CAUSE:

CORRECTIVE ACTION:
```

### Model Answer:

```
PROBLEM: A user's browser keeps redirecting, though AV reported the adware
         cleaned three days ago.

Why does it still redirect?     → Something is still altering the browser's
                                   traffic or settings.
Why, if AV cleaned it?          → AV removed the executable, but not
                                   everything the adware installed.
What else did it install?       → A browser extension and a changed proxy
                                   setting.
Why weren't those removed?      → AV signatures target the payload file, not
                                   browser configuration.
Why does that matter here?      → Because the extension re-applies the
                                   redirect at every browser launch.

ROOT CAUSE: Remediation was incomplete — the browser extension and proxy
            setting were never removed.

CORRECTIVE ACTION:
  1. Export the browser extension list and proxy settings          (L1)
  2. Document what is present and does not belong                  (L1)
  3. Escalate removal to L2 — changing user config is above L1     (L1 → L2)
  4. Re-scan after removal                                         (L2)
  5. Verify with the user at next browser launch                   (L1)
```

### The two rules, and where they bite here

**Stop at the first thing you can act on.** If your chain ended at *"because antivirus
products only remove files"* you went one step too far — that is a complaint about product
design, not tonight's fix.

**If your answer is a person, back up.** *"Because the user installed a dodgy extension"* may
be true and it is not the technical cause. Awareness training is a real fix; it is not yours
to implement and it does not stop the redirect this afternoon.

---

## Exercise 3: Cause-and-Effect, and the Five-Minute Test

**Objective:** Generate possible causes, then rank them by how cheaply you can eliminate them.
**Unit link:** 400311103 LO2 — PC 2.1, 2.2

### Instructions:
**Fault:** *Alerts stopped arriving from one site at 14:20. Hosts respond to ping.*

**Step 1.** Fill in at least two possible causes under each branch.

| Branch | Possible causes |
|--------|----------------|
| **Agent** | |
| **Network** | |
| **Server** | |
| **Configuration** | |
| **Host** | |
| **Process** | |

**Step 2.** For each cause, write how you would test it, and how long that test takes.
Then rank them cheapest-first.

| Rank | Possible cause | How I test it | Time |
|------|---------------|--------------|------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Model Answer:

| Branch | Possible causes |
|--------|----------------|
| **Agent** | Service stopped · agent crashed · agent version mismatch after an update |
| **Network** | Switch rebooted · firewall rule change blocking the agent port · DNS failure |
| **Server** | Manager service down · indexer disk full · manager rejecting new connections |
| **Configuration** | Somebody changed a log filter · rule set edited · log level lowered |
| **Host** | Hosts rebooted · time drift breaking authentication · disk full on the host |
| **Process** | A change window nobody told you about · maintenance by another team |

**Ranked by cost to eliminate:**

| Rank | Cause | Test | Time |
|------|-------|------|------|
| 1 | Change in effect | Check the change calendar — **and Facilities notices, not just IT** | 1 min |
| 2 | Server side down | Is any *other* host still reporting? If yes, the server is fine | 1 min |
| 3 | Agent service stopped | `Get-Service` on one affected host | 2 min |
| 4 | Network path blocked | `Test-NetConnection <server> -Port <agent port>` | 2 min |
| 5 | Server disk full | Check the manager's disk usage | 3 min |
| 6 | Config change | Compare the rule set against yesterday's | 15 min |

> **Ranks 1 and 2 are free and they eliminate the most.** If other hosts are still reporting,
> the entire "Server" branch is gone in sixty seconds. Always ask what is still *working* —
> it is faster than asking what is broken.

**The trap in this fault:** the actual cause was a **Facilities** power interruption that
rebooted the site switch. Everybody checks the IT change calendar. Almost nobody checks
whether another department scheduled something. Broaden where you look.

---

## Exercise 4: Options, Filters, and an Action Plan

**Objective:** Choose a corrective action defensibly and write a plan somebody can follow.
**Unit link:** 400311103 LO3 and LO4 — PC 3.1, 4.1

### Instructions:
**Fault:** *Four servers stopped reporting at 14:20. No change notice found. All respond to ping.*

**Step 1 — write down three options before choosing one.**

| Option | What it costs | What it risks | Within my authority? |
|--------|--------------|--------------|---------------------|
| | | | |
| | | | |
| | | | |

**Step 2 — apply the filters in order**, and say which option survives:
1. Is it within my authority?
2. Is it reversible?
3. Is it the smallest thing that could work?

**Step 3 — write the full action plan** using the seven-field format.

### Model Answer — Step 1:

| Option | Costs | Risks | Authority |
|--------|-------|-------|-----------|
| Restart the agent service on **one** host as a test | 5 min | Loses a few in-flight events on that host | **Yes** — routine |
| Restart the agent service on all four | 10 min | Same, four times. If it works you learn less about why | **Yes** |
| Reboot the four servers | 30 min + downtime | Business impact, needs a change request | **No** — escalate |
| Wait for the maintenance window to end | 0 | Delay, if there is no maintenance window | Yes, with documentation |

**Surviving option: restart the agent service on one host as a test.** It is within
authority, reversible, and the smallest thing that could work — and it tells you whether
the other three will respond the same way.

### Model Answer — Step 3:

```
PROBLEM   Since approximately 14:20 today, SRV-MNL-01 through 04 have sent no
          events. All other monitored hosts are reporting normally. All four
          affected hosts reply to ICMP. No IT change notice is in effect.

CAUSE     Not yet confirmed. Most likely the agent lost its connection and did
          not re-establish it. Server side is ruled out — other hosts are fine.

ACTION    1. Check Facilities as well as IT for scheduled work   (L1, 15:00)
          2. Restart the agent service on SRV-MNL-01 only        (L1, 15:10)
          3. Confirm events resume from that host within 5 min   (L1, 15:15)
          4. If yes, restart the remaining three                 (L1, 15:25)
          5. If no, escalate to L2 with the test result          (L1, 15:20)

WHO       L1 analyst on shift, with L2 informed before step 2

SUCCESS   Events arriving from all four hosts, and still arriving 30 minutes
          later. A host that reports for two minutes and stops again is NOT
          a success.

FALLBACK  If a service restart does not restore reporting, escalate to L2.
          Do not reboot — that requires a change request and is above L1.
```

### What to check in your own plan

- [ ] Does every action step name **one** verifiable act?
- [ ] Does every step have a person and a time?
- [ ] Is success defined with something **measurable**? ("Still arriving 30 minutes later")
- [ ] Does the fallback name **who** you escalate to?
- [ ] Did you avoid putting anything above your authority into the ACTION list?

> The most common failure in this exercise is a plan whose success criterion is "monitoring
> restored". That is not testable. A host that reports for two minutes and dies again would
> pass it.

---

## Exercise 5: One Plan, Three Audiences

**Objective:** Say the same thing three ways without losing what matters.
**Unit link:** 400311103 LO4 — PC 4.1

### Instructions:
Using your action plan from Exercise 4, write the same situation three ways.

**A. To your L2 — you have 60 seconds. Aim for 3–4 sentences.**

_______________________________________________________________

_______________________________________________________________

**B. To the client — 2 sentences, no jargon.**

_______________________________________________________________

**C. Into the ticket — with timestamps.**

_______________________________________________________________

### Model Answers:

**A — to the L2:**
> "Four Manila servers stopped sending events at about 14:20 — MNL-01 through 04. Everything
> else is reporting fine and all four answer ping, so it is not the network and they are not
> down. I have checked the change calendar and there is no notice covering it. I would like to
> restart the agent service on one of them as a test before I do all four. Are you happy for
> me to do that?"

Five parts, and the last one is what separates a competent L1 from a good one:

| Element | The words |
|---------|-----------|
| The fact | "Four Manila servers stopped sending events at about 14:20" |
| The boundary | "Everything else is reporting fine… it is not the network" |
| What you already checked | "no notice covering it" |
| What you propose | "restart the agent service on one of them as a test" |
| **The ask** | **"Are you happy for me to do that?"** |

> You did not just report a problem. You arrived with a proposed next step and asked for
> authority. Your L2 has to say one word.

**B — to the client:**
> "Good afternoon — I am calling to let you know we have lost monitoring visibility on four
> of your Manila servers since about two twenty this afternoon. The servers themselves are
> running normally and your users are not affected. We are restoring monitoring now and I
> will call you back within the hour."

Two things the technical version did not have, and both are mandatory:
**"your users are not affected"** and **"I will call you back within the hour."**

> **The sentence to never say:** *"We are having some issues with the monitoring, we are
> looking into it, I will get back to you."* No scope, no impact statement, no time
> commitment. It sounds reassuring and it is why clients escalate to your manager.

**C — into the ticket:**
```
14:47  Detected loss of event flow from SRV-MNL-01, -02, -03, -04.
       Last event from each host approx 14:20.
14:49  Verified all other monitored hosts reporting normally.
14:52  ICMP reply received from all four affected hosts.
14:55  Checked IT change calendar — no notice in effect. Facilities
       notice found: power interruption 14:00–14:30, Manila site.
15:01  Briefed L2 (R. Aguilar). Authorised to restart agent service on
       SRV-MNL-01 as a single-host test.
15:04  Client contact notified by phone. Advised no user impact,
       callback committed within 1 hour.
```

Two things the ticket has that neither conversation had: **exact times**, and **the name of
who authorised the action**. In six months nobody will remember this afternoon. If you are
ever asked "why did you restart that server?", the answer needs to be a line in a ticket with
a name on it.

---

## Exercise 6: Recognising Your Own Patterns

**Objective:** Set goals, recognise emotional states, describe yourself as a learner.
**Unit link:** 400311104 LO1, LO2, LO3

### Instructions:
Complete the **Goal Sheet**, the **Reflection**, and the **Learning Style Inventory** in your
Student Handout. There are no wrong answers and none of it is marked.

### What a strong response looks like

| Section | Weak | Strong |
|---------|------|--------|
| **Career goal** | "Get a good job in IT" | "Move from L1 to L2 within two years, which means I need to be able to investigate an escalation on my own, not just raise it" |
| **30-day action** | "Study more" | "Spend 30 minutes every Saturday practising PowerShell log queries until I can write one without looking it up" |
| **Emotion reflection** | "I get frustrated sometimes" | "When a tool did not do what the manual said, I kept trying the same thing for an hour instead of asking. I lost most of an afternoon to it" |
| **Learner strategy** | "I am a visual learner" | "I learn by doing, so on Day 5 when it gets theoretical I will ask the trainer to show me on a real machine instead of zoning out" |

> The last row is the one that matters. Knowing your learning style is trivia. Deciding in
> advance what you will *do* on the day you struggle — that is self-management, and that is
> what the unit is actually asking for.

---

## Exercise 7: Write an SOP Improvement Proposal

**Objective:** Identify a need for innovation, and support a colleague's idea.
**Unit link:** 400311105 LO1, LO2, LO3

### Instructions:
**Part A.** Based on something you genuinely noticed on Day 1 or today, complete the
**SOP Improvement Proposal** in your Student Handout.

**Part B.** Swap with a partner. On their sheet, write **one thing you like** and
**one question** you have. That is LO3 — supporting somebody else's access to innovative
practice.

### Model Answer:

```
WHAT I NOTICED
  In the Day 1 handover exercise, three of us wrote down the ticket numbers
  but missed that the vulnerability scanner was in maintenance. Two people
  said they only realised at the end. (Signal: near miss.)

WHY IT MATTERS
  If an analyst does not know scanning is unavailable, they will spend time
  trying to run one, or tell a client a scan is scheduled when it is not.
  It happened to three of five people in one exercise.

WHAT I PROPOSE
  Add one line to the handover template: "Systems unavailable tonight".
  Separate from "system status", so it cannot be skimmed past.

WHO NEEDS TO APPROVE IT
  SOC Manager — it is a change to a shared template.

HOW WE WOULD KNOW IT WORKED
  Ask the next five incoming shifts to state which systems are unavailable.
  If all five can, it worked.
```

### Why this is a good proposal — and what makes a weak one

| Good proposal | Weak proposal |
|--------------|--------------|
| Names a **specific observation**, with a number | "Communication could be better" |
| Costs almost nothing to implement | Requires a budget |
| **An L1 could raise it on a Tuesday** | Needs a project team |
| Success is **measurable** | "Things would improve" |

> Some trainees freeze on this because they think "innovation" has to be clever. It does not.
> *"Add one field to a template"* is a completely valid proposal, and it is the kind that
> actually gets adopted.

---

## Exercise 8: The Service Scenario

**Objective:** Think about the work the way an owner would.
**Unit link:** 400311109 LO1, LO2

### The scenario:
> Your SOC has 40 clients and 3 analysts on the night shift. Alert volume has doubled in a
> month. Nothing has been missed yet, but the queue is no longer clearing before shift end.

### Instructions:
In your team, produce **three** recommendations. For each one give: what it changes, what it
costs, and what could go wrong.

| # | Recommendation | What it changes | What it costs | What could go wrong |
|---|---------------|----------------|--------------|--------------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Model Answer:

| # | Recommendation | Changes | Costs | Risk |
|---|---------------|---------|-------|------|
| 1 | **Find the noisiest rule and tune it** | One rule often generates a large share of the volume. Tuning it can remove hundreds of alerts a night | A few hours of L2/engineering time | A badly tuned rule suppresses a real detection. Must be tested and reviewed |
| 2 | **Group duplicate alerts from the same host into one ticket** | 186 alerts from one host become 1 ticket with 186 events | Configuration time in the ticket system | A second, different alert from that host could be swallowed by the grouping |
| 3 | **Find which client generates the most noise, and ask why** | Often one client's environment or a recent change is the cause. The fix may be theirs, not yours | A conversation and some analysis | The client may hear "your environment is a problem" as criticism. Frame carefully |

### The debrief point

Notice that almost every sensible answer is **"reduce the noise"**, not **"hire more people"**.

| Approach | Cost | Effect |
|----------|------|--------|
| Hire a fourth night analyst | A full salary, every month, forever | The queue clears — until volume doubles again |
| Tune the noisiest rule | A few hours, once | The queue clears, and stays cleared |

> Fixing the process before adding cost is exactly what this unit means by an entrepreneurial
> mindset. Nobody will hand an L1 a budget — but every triage decision you make spends
> somebody's money, and analysts who understand that get promoted, because they escalate the
> right things.

### What your decisions actually cost

| Thing | Cost |
|-------|------|
| An alert triaged well the first time | ~8 minutes of L1 time |
| The same alert escalated wrongly to L2 | ~45 minutes of L2 time, plus yours |
| A missed critical alert | A client incident, a penalty, sometimes the contract |
| A false escalation at 3 AM | A manager's night — and their trust in your judgement |

---

## ANSWER KEY SUMMARY

| Exercise | Unit | Key learning |
|----------|------|-------------|
| 1 | 400311103 LO1 | A problem statement needs what, when, scope, **boundary**, evidence |
| 2 | 400311103 LO2 | Stop at the first actionable cause; if the answer is a person, back up |
| 3 | 400311103 LO2 | Rank causes by cost to eliminate. Ask what is still **working** |
| 4 | 400311103 LO3 | Three options, then: authority → reversible → smallest thing that works |
| 5 | 400311103 LO4 | L2 gets the ask; the client gets impact and a callback time; the ticket gets timestamps and names |
| 6 | 400311104 | Self-management is deciding in advance what you will do when you struggle |
| 7 | 400311105 | The best improvements are cheap, small, and close to the work |
| 8 | 400311109 | Fix the process before you add cost |
