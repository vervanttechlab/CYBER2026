# THE NIGHT SHIFT — ANSWER KEY
## SOP Activity · Day 1 Afternoon

> ## TRAINER COPY ONLY
> **Do not send this file to trainees.** The activity is discussed on Day 2.

---

## WHAT EACH ALERT IS TESTING

You do not have to remember eight separate answers. Each alert tests exactly one thing, and once you see the map you can debrief the whole activity from this page.

| Alert | Tests | The document that decides it |
|-------|-------|----------------------------|
| **1** | The floor — recognising genuinely routine noise | Severity Matrix, Low row |
| **2** | The ceiling — Critical, and the limit of L1 authority | Severity Matrix + SOP §3.6 |
| **3** | A vendor advisory changing how you treat a detection | Document 4 |
| **4** | A change notice explaining an alert | Document 5 |
| **5** | What a change notice does **not** cover | Document 5, again |
| **6** | The override rule that raises severity | Severity Matrix, rule 1 |
| **7** | A client SLA notice overriding the SOP | Document 6 |
| **8** | Uncertainty is not Low | Severity Matrix, rule 4 |

> **Alerts 4 and 5 are a pair, and 5 is the one that teaches.** Same night, same minute, same symptom — different answer. Debrief them together.

---
---

## ALERT 1 · 21:15 — Blocked port scan

| | |
|---|---|
| **Severity** | **LOW** |
| **Why** | Severity Matrix, Low row: *"Blocked port scan from the internet."* Routine, already handled by the tool |
| **Notify client** | End of shift summary only |
| **Escalate to** | **Nobody.** L1 may close it |
| **Can you close it?** | **Yes — but only if you document the assessment.** SOP §3.5: *"MAY close... provided the assessment is documented"* |

**The teaching point:** the permission in §3.5 has a price. Closing it without writing anything is not using your discretion — it is breaching the procedure.

> **Watch for:** trainees who escalate this. Over-escalating everything is as much a failure as under-escalating — it buries L2 and they stop trusting your queue.

---

## ALERT 2 · 22:04 — Ransomware

| | |
|---|---|
| **Severity** | **CRITICAL** |
| **Why** | Severity Matrix, Critical row: *"Ransomware encrypting files."* Active harm happening right now |
| **Notify client** | **Within 10 minutes of assessment** — Critical, not the standard 15 |
| **Escalate to** | **L2 AND the SOC Manager, immediately.** Phone first, then ticket |
| **If nobody answers** | Escalation Matrix: call the next name on the on-call list. **Keep calling. Never leave a Critical unowned** |

### Question 5 — the client asks you to disconnect the machine

> ## ANSWER: **Refuse, and escalate. SOP-SOC-001 §3.6.**

*"The analyst SHALL NOT take containment action on any host. Containment is authorised by the SOC Manager only."*

The words to use:

> *"I do not have the authority to disconnect that machine. I am escalating this to the SOC Manager right now and they will call you back."*

Then escalate immediately — not just say it to end the call.

> **This is the most important answer in the whole activity.** Expect trainees to want to say yes: the client is panicking, it is ransomware, and disconnecting sounds obviously right.
>
> Say this out loud when you debrief: **"Wanting to help is correct. Doing it yourself is the part that is wrong."** Then give the reason — you do not know what else that machine is doing, whether disconnecting destroys evidence L2 needs, or whether it takes a production system down with it.

---

## ALERT 3 · 22:40 — Trojan.Generic.Heur on powershell.exe

| | |
|---|---|
| **Is it what it appears to be?** | **Probably not — a suspected false positive** |
| **Which document** | **Document 4, Advisory 2026-0418.** Agent 7.4.2 has a signature regression causing false positives named `Trojan.Generic.Heur` on signed Microsoft binaries, and it names `powershell.exe` specifically |
| **What you must do first** | **Verify manually before escalating.** The advisory says treat as *suspected* false positive and verify — it does **not** say ignore |

### Question 4 — unsigned file in Downloads?

> ## ANSWER: **Yes, the answer changes completely.**

The advisory states it *"does not apply to detections on unsigned binaries or on binaries outside the Windows system directories."*

An unsigned file in `C:\Users\...\Downloads\` is outside the advisory's scope entirely. Treat it as a real detection.

> **The teaching point, and it is the same one as Alert 5:** a document tells you what it does **not** cover just as clearly as what it does. Trainees who apply the advisory to everything have made the exact mistake the advisory's last paragraph is written to prevent.

---

## ALERT 4 · 23:40 — SRV-MNL-02 and 03 offline

| | |
|---|---|
| **Incident?** | **Not an incident** |
| **Which document** | **Document 5, Change Notice `CHG-2026-1177`** |
| **Why** | Both hosts are named in the notice. The window is 22 April, 22:00–03:00. It is 23:40 on 22 April. Agents reporting offline during reboot is explicitly listed as expected |
| **What you must record** | **The change reference, `CHG-2026-1177`** |
| **Which step** | **SOP §3.4** — checking is *should*, but recording the reference once you have found one is **shall** |

> **Watch for the trainee who writes "not an incident" and closes it with no reference.** They got the judgement right and the procedure wrong. §3.4 makes the recording mandatory.

---

## ALERT 5 · 23:47 — SRV-CEB-02 offline

| | |
|---|---|
| **Incident?** | **YES — this is an incident** |
| **Why different from Alert 4** | **Cebu is not in the change notice.** `CHG-2026-1177` names four hosts: `SRV-MNL-01` to `SRV-MNL-04`. All Manila. `SRV-CEB-02` is not covered by anything |
| **Severity** | **MEDIUM** — Severity Matrix lists *"unexpected agent offline"* under Medium |
| **Escalate to** | L2 on shift, by ticket, **if unresolved at end of shift** |

> ## THIS IS THE BEST TEACHING MOMENT IN THE ACTIVITY

Same night. Seven minutes apart. Identical symptom. Opposite answers.

Ask the class: **"How many of you saw 'servers going offline is expected tonight' and applied that to all servers?"** Several hands will go up, and that is the lesson — not the answer.

**Say this:** *"A change notice is not a general permission to ignore things. It is a list. If the host is not on the list, the notice says nothing about it — and 'the notice says nothing' means you treat it normally."*

---

## ALERT 6 · 01:22 — Credential dumping on a domain controller

| | |
|---|---|
| **What the Matrix lists it as** | **HIGH** — *"credential dumping tool detected"* is a High example |
| **Your final severity** | **CRITICAL** |
| **What changed it** | **Override rule 1:** *"Anything on a domain controller, backup server, or finance system is raised one level."* `DC-01` is a domain controller. High raised one level is Critical |
| **Notify client** | Within **10 minutes** of assessment — Critical timing, not High |
| **Escalate to** | **L2 and the SOC Manager, immediately.** Phone, then ticket |

> **Expect most of the class to answer High.** They will read the Matrix row, find credential dumping, write High, and stop — never reaching the four override rules underneath the table.
>
> That is the point of the alert. **Say:** *"The table is not the whole document. The rules underneath it beat the table, and this one moved the answer two categories in terms of what you actually do."*
>
> Also worth naming: a domain controller holds every credential in the organisation. Credential dumping there is not one compromised machine — it is potentially every account in the company.

---

## ALERT 7 · 02:50 — DLP block, Northwind Trading

| | |
|---|---|
| **Severity** | **HIGH** — Severity Matrix: *"DLP block on sensitive data"* |
| **Notify client** | **Within 30 minutes of assessment — not 15** |
| **Which document changes it** | **Document 6, the Northwind SLA Notice.** *"High alerts: client notified within 30 minutes of assessment... This supersedes the standard notification timings in SOP-SOC-001 section 3.3 FOR THIS CLIENT ONLY"* |
| **How to contact them** | **Phone to the on-call number, followed by email** |
| **Named contact** | **Ms. R. Aguilar, IT Manager**, on call 24/7 |

### Question 5 — does this change Sunrise Manufacturing's timings?

> ## ANSWER: **No. The notice says so itself.**

*"FOR THIS CLIENT ONLY. All other clients are unchanged."*

> **The teaching point, and it is the most transferable one in the whole pack:** when two documents conflict, the correct behaviour is **not** to pick the stricter one, the newer one, or the one you prefer. It is to check whether the notice **has the authority to override** — and a document that can override says so, in words.
>
> **Ask a trainee who answered "follow the stricter one" to explain their thinking before you give the answer.** They reasoned sensibly and still got it wrong, which makes them the most useful person in the room. It lands far better from a trainee than from you.

---

## ALERT 8 · 04:10 — Unknown process

| | |
|---|---|
| **Severity** | **MEDIUM — at minimum** |
| **Which rule** | **Override rule 4:** *"Uncertainty is not Low. 'I don't know what this is' is Medium at minimum."* |
| **Also supports it** | Rule 3: stuck between two levels, take the higher one and write down why |
| **Escalate to** | L2 if unresolved at end of shift — which, at 04:10, it will be |

### Question 3 — why "Low" is wrong

> ## ANSWER: **Low means "routine, expected, or already handled." An unknown process is none of those.**

Low is a positive statement that you know what something is and it does not matter. It is not a place to put things you have not worked out yet.

> **This is the 4am alert**, and the file name is deliberate — `svhost32.exe` is a near-miss for the legitimate `svchost.exe`. Nothing is confirmed bad. Nothing is confirmed good. It is the easiest alert on the sheet to mark Low and go back to the quiet queue.
>
> **Say:** *"Low is not a filing cabinet for things you have not figured out. Low means you know what it is and it does not matter."*

---
---

# THE FINAL QUESTION

**"Which was the most dangerous, and which was most likely to be ignored at 4am? Are they the same alert?"**

> ## There is no single right answer — and that is the point.

**The strongest answer:** the most dangerous is **Alert 6** (credential dumping on a domain controller — potentially every account in the organisation), and the most likely to be ignored is **Alert 8** (unknown process, 4am, nothing confirmed).

**They are different alerts, and that is the whole problem.** The dangerous one announced itself loudly. The one you would miss did not.

**Also accept, with good reasoning:**

- **Alert 2** as most dangerous — active harm, happening right now
- **Alert 6** as *both* — because "credential dumping tool ran for 4 seconds then exited" is quiet, and a tired analyst may read "it exited" as "it is over"
- **Alert 5** as most likely ignored — because Alert 4 four minutes earlier trained them to expect offline servers

> **Mark the reasoning, not the choice.** A trainee who picked Alert 5 and explained that Alert 4 had primed them to dismiss it has understood something genuinely sophisticated about how analysts actually make mistakes.

---
---

# HOW TO MARK THIS

**Mark for use of the documents, not for correct severities.**

This is a first attempt after one morning of training. What you are looking for:

| Look for | Because |
|----------|---------|
| **Does the answer point at a rule, step, or notice?** | "High" scores nothing. "High, per the Matrix High row" is the answer |
| **Did they refuse the containment request?** *(Alert 2)* | This is the L1 authority boundary, and assessors test it |
| **Did they spot that Cebu is not covered?** *(Alert 5)* | The single best indicator of careful reading |
| **Did they reach the override rules?** *(Alerts 6 and 8)* | Shows they read past the table |
| **Did they resist marking the unknown as Low?** *(Alert 8)* | Shows the right instinct under uncertainty |

**Give Attempted / Developing / Solid, not a score.**

> **A wrong severity with sound reasoning beats a right severity that was guessed.** Say that when you hand the marked sheets back — it is the habit you want for the next fourteen days.

---

## WHAT TO DO WITH THE DEBRIEF ON DAY 2

You have limited time. **Do these three, in this order, and skip the rest:**

1. **Alerts 4 and 5 together** — the pair. Five minutes, and it teaches boundary-reading better than anything else in the pack.
2. **Alert 7, question 5** — document authority. Get a "stricter one" trainee to explain first.
3. **Alert 2, question 5** — the containment refusal. Short, and it is the one an assessor will ask about.

Everything else can be handed back marked, with written comments.
