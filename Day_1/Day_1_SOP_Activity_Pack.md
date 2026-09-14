# THE NIGHT SHIFT
## SOP Activity Pack · Day 1 Afternoon
### Cyber Threat Monitoring Level I

---

## WHAT THIS IS

Eight alerts arrive across one night shift. For each one you decide four things:

1. **How severe is it?**
2. **Why — which rule or document tells you that?**
3. **Do you notify the client, and by when?**
4. **Who do you escalate to?**

That is the job. Not a quiz about the documents — **the thing an analyst does every night, using the documents.**

**Time: about 45 minutes.** Have your SOP Pack open. You will need all three procedures and all three notices.

---

## BEFORE YOU START

**Read the SOP Student Handout first.** It explains all three procedures and the notices, and its last page is a quick reference card — once you have read it, that one page is all you need open while you work.

Then open your **SOP Pack** and keep these where you can see them:

| Document | You will need it for |
|----------|---------------------|
| `SOP-SOC-001` Alert Intake | The steps and the clocks |
| `SOP-SOC-002` Severity Matrix | Ranking every alert |
| `SOP-SOC-003` Escalation Matrix | Who to contact |
| Document 4 — Vendor Advisory | Alert 3 |
| Document 5 — Change Notice | Alerts 4 and 5 |
| Document 6 — Northwind SLA Notice | Alert 7 |

> **Two things before you begin.**
>
> **You will not be sure about some of these.** That is deliberate and it is realistic. When you are stuck between two levels, the Severity Matrix tells you what to do — find that rule and use it.
>
> **Write your reasoning, not just your answer.** "High" on its own scores nothing. "High, because the Severity Matrix lists credential dumping under High" is the answer.

---

## TONIGHT'S SHIFT

**Your shift: 21:00 to 05:00. Tonight is 22 April 2026.**
**Your client tonight is Northwind Trading unless the alert says otherwise.**

---
---

# ALERT 1 · 21:15

```
Source system  : Perimeter firewall
Detection      : Repeated blocked inbound connection attempts
                 from 203.0.113.90 to the public web server
Action taken   : All attempts blocked automatically
Host           : WEB-PUB-01
Client         : Sunrise Manufacturing
```

**1. Severity:** ____________________

**2. Why — which rule or document?** _________________________________________

_______________________________________________________________________________

**3. Notify the client? By when?** ____________________________________________

**4. Escalate to whom?** ______________________________________________________

**5. Can you close this yourself? What must you do first?** ___________________

_______________________________________________________________________________

---

# ALERT 2 · 22:04

```
Source system  : Endpoint detection (EDR)
Detection      : Rapid file modification across a mapped drive.
                 File extensions changing to .locked
                 Ransom note file created in three folders
Action taken   : None — detection only
Host           : WKS-244
Client         : Sunrise Manufacturing
```

**1. Severity:** ____________________

**2. Why — which rule or document?** _________________________________________

**3. Notify the client? By when?** ____________________________________________

**4. Escalate to whom, and how?** _____________________________________________

**5. The client phones you at 22:10 and asks you to disconnect WKS-244 from the network immediately. What do you say, and which step of the SOP tells you that?**

_______________________________________________________________________________

_______________________________________________________________________________

---

# ALERT 3 · 22:40

```
Source system  : Endpoint Agent 7.4.2
Detection      : Trojan.Generic.Heur
Affected file  : C:\Windows\System32\powershell.exe
                 (signed by Microsoft)
Action taken   : Quarantine attempted, failed — file in use
Host           : WKS-118
Client         : Sunrise Manufacturing
```

**1. Is this what it appears to be?** _________________________________________

**2. Which document tells you that, and what exactly does it say?**

_______________________________________________________________________________

**3. What are you instructed to do before escalating?** ______________________

_______________________________________________________________________________

**4. Would your answer change if the detection were on an unsigned file in a user's Downloads folder? Why?**

_______________________________________________________________________________

---

# ALERT 4 · 23:40

```
Source system  : Monitoring platform
Detection      : Agent offline — no heartbeat for 8 minutes
Hosts          : SRV-MNL-02, SRV-MNL-03
Action taken   : None
Client         : Sunrise Manufacturing
```

**1. Incident, or not an incident?** __________________________________________

**2. Which document decides it, and what is its reference number?**

_______________________________________________________________________________

**3. What must you record before you close this? Which step makes that mandatory?**

_______________________________________________________________________________

---

# ALERT 5 · 23:47

```
Source system  : Monitoring platform
Detection      : Agent offline — no heartbeat for 6 minutes
Host           : SRV-CEB-02
Action taken   : None
Client         : Sunrise Manufacturing
```

**1. Incident, or not an incident?** __________________________________________

**2. Why is your answer different from Alert 4?**

_______________________________________________________________________________

**3. Severity:** ____________________  **4. Escalate to whom?** ______________

---

# ALERT 6 · 01:22

```
Source system  : Endpoint detection (EDR)
Detection      : Known credential-dumping tool executed
                 Process ran for 4 seconds, then exited
Action taken   : None — detection only
Host           : DC-01  (domain controller)
Client         : Sunrise Manufacturing
```

**1. What does the Severity Matrix list this detection as?** _________________

**2. What is your final severity — and what changed it?**

_______________________________________________________________________________

**3. Notify the client? By when?** ____________________________________________

**4. Escalate to whom, how, and by when?** ____________________________________

_______________________________________________________________________________

---

# ALERT 7 · 02:50

```
Source system  : Data loss prevention (DLP)
Detection      : Blocked upload of a file marked CONFIDENTIAL
                 to a personal file-sharing account
Action taken   : Upload blocked
User           : r.santos
Host           : WKS-402
Client         : NORTHWIND TRADING
```

**1. Severity:** ____________________

**2. Notify the client? By when — and be careful here.** _____________________

**3. Which document changes the answer to question 2, and what exactly does it say?**

_______________________________________________________________________________

**4. How do you contact them, and who is the named contact?**

_______________________________________________________________________________

**5. Does this notice change the timings for Sunrise Manufacturing too? How do you know?**

_______________________________________________________________________________

---

# ALERT 8 · 04:10

```
Source system  : Endpoint detection (EDR)
Detection      : Unrecognised process "svhost32.exe" running from
                 C:\Users\Public\
                 No signature match. No known-bad match.
                 Behaviour unclear.
Action taken   : None
Host           : WKS-091
Client         : Sunrise Manufacturing
```

**1. You genuinely do not know what this is. What severity do you give it?**

____________________

**2. Which rule tells you that, and what does it say?**

_______________________________________________________________________________

**3. Explain in one sentence why "Low" would be the wrong answer here.**

_______________________________________________________________________________

---
---

# END OF SHIFT · 05:00

## Your handover log

You are handing over to the day shift. Using the five sections from this morning, write a short handover from tonight.

**OPEN ITEMS** *(tickets still in progress — which of tonight's eight are still open?)*

_______________________________________________________________________________

_______________________________________________________________________________

**ESCALATED** *(what went to L2 or the SOC Manager, and who owns it now)*

_______________________________________________________________________________

**WATCH ITEMS** *(not incidents yet, but the next shift should keep an eye on them)*

_______________________________________________________________________________

**SYSTEM STATUS** *(anything down, degraded, or under maintenance)*

_______________________________________________________________________________

**CLIENT NOTES** *(anything a client asked for or complained about)*

_______________________________________________________________________________

---

## One last question

**Of tonight's eight alerts, which one was the most dangerous — and which one was most likely to be ignored by a tired analyst at 4am? Are they the same alert?**

_______________________________________________________________________________

_______________________________________________________________________________

---

## HANDING IN

- [ ] All eight alerts answered, **with reasoning**
- [ ] End-of-shift handover log completed
- [ ] Final question answered

**Your name:** _________________________ **Date:** _____________

> **Do not worry about getting them all right.** This is your first attempt after one morning of training. What your trainer is marking is whether you **used the documents** — whether your answer points at a rule, a step, or a notice. An answer with a wrong severity but sound reasoning is worth more than a right severity you guessed.

**Answers are discussed on Day 2. Bring this sheet.**
