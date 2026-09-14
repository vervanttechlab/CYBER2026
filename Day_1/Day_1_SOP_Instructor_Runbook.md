# THE SOP PACK — PRESENTER SCRIPT
## For the 12-slide SOP deck
### Cyber Threat Monitoring Level I

---

## WHEN YOU USE THIS

**Day 2, first thing in the morning. Allow 45 to 50 minutes.**

Trainees worked through the SOP Pack and the Night Shift activity on their own on Day 1 afternoon. They arrive with completed answers. About half of those answers will be wrong.

This script debriefs that attempt. You are not teaching a document. You are explaining why their own answer was wrong. That is a much faster way to learn.

**Have open:** this script, and `Day_1_SOP_Solutions.md` for the full answer key.

**Trainees have:** the SOP Student Handout, the SOP Pack, and their completed Night Shift sheet.

**If you are delivering this cold**, with no attempt beforehand, the script still works. Change "yesterday afternoon" to "later today" and skip the show-of-hands questions.

---

## HOW TO READ THIS SCRIPT

Everything in normal text is what you say. Once you are comfortable, say it in your own words.

Anything in square brackets is an instruction to you. Do not read it aloud.

Each slide is timed. The timings assume a class of twelve to twenty.

---
---

# SLIDE 1 — TITLE
### 2 minutes

Good morning. Please take out your Night Shift worksheet.

Raise your hand if you completed all eight alerts.

[Count the hands. Note who did not. Follow up privately at the break.]

Thank you. Now raise your hand if you found it harder than you expected.

That is normal, and there is a reason for it. Yesterday afternoon was the first time you did this job rather than learned about it. You had eight alerts, three procedures, three notices, and no one to ask.

This morning we go through it together. Some of you will find that you were wrong about things you felt sure about. That is the most useful part of the session, so we will not rush it.

One request before we start. When I ask what you wrote, please tell me what you actually wrote. Not what you now think the right answer is. The wrong answers are where the learning happens.

---

# SLIDE 2 — WHY WRITTEN PROCEDURES EXIST
### 4 minutes

Let us begin with why these documents exist at all.

An SOP answers one question. That question is: why did you do that?

It is asked six months later, by someone who was asleep when you made the decision.

Look at the two boxes on the slide.

If you followed the procedure and the outcome was bad, that is a process problem. The company fixes the process. Nobody examines your judgement.

If you ignored the procedure and the outcome was bad, that is your problem.

So the procedure is not there to restrict you. It is there to protect you. It is the reason you can make a decision alone, at two in the morning, with incomplete information, and still defend it in daylight.

Most people who dislike procedures have never had a decision reviewed. Once you have been through that, your view usually changes.

---

# SLIDE 3 — YOUR THREE DOCUMENTS
### 3 minutes

First, the word itself. We have been using it since yesterday and I have not yet told you what it stands for.

SOP means Standard Operating Procedure.

It is a written instruction for how a job is done. The same way, every time, by whoever is on shift.

The reason it must be the same way every time is handover. If you assess alerts one way and the next analyst assesses them another way, no one can rely on anyone else's tickets.

Now the three documents.

SOP-SOC-001 is the Alert Intake procedure. It tells you what to do when an alert arrives. The steps, and the deadlines.

SOP-SOC-002 is the Severity Matrix. It tells you how serious the alert is.

SOP-SOC-003 is the Escalation Matrix. It tells you who to contact, how, and how quickly.

You also have three sample notices. A vendor advisory, a change notice, and a client service level notice. Those three documents change the rules. Three of last night's eight alerts depended on them.

One quick question. Which document did you have open the most last night?

[Take two or three answers.]

Most people say the Severity Matrix. That is correct. You use it on every single alert.

---

# SLIDE 4 — THE SMALL WORDS
### 4 minutes

Here is something most people are never taught. In a procedure, the important words are the small ones.

Shall and must mean mandatory. You have no choice.

Should means expected. You may deviate, but you must be able to explain why.

May means your judgement. There is almost always a condition attached to it.

Shall not means you have no authority. That is the edge of your role.

Within X minutes means a clock is running. Your job is to know when that clock starts.

Now look at the example on the slide.

"The analyst may close a Low alert, provided the assessment is documented."

If you read that quickly, you hear that you are allowed to close Low alerts.

If you read it properly, the permission has a condition. You may close it, but only if you write down why.

That was Alert 1 last night. The blocked port scan.

Raise your hand if you assessed it as Low and closed it.

[Hands go up.]

Now keep your hand up only if you also wrote down your reasoning.

[Most hands go down.]

Everyone assessed the severity correctly. Some of you breached the procedure while doing so, because you did not complete the second half of the sentence.

Undocumented judgement is not judgement. It is just closing a ticket.

---

# SLIDE 5 — THE ALERT INTAKE PROCEDURE
### 5 minutes

Eight steps. You do not need to memorise them. You need to know what is in there so you can find it quickly.

Record four fields within five minutes. Assess the severity before doing anything else. Notify the client if it is Critical or High. Check for a change notice. You may close a Low if you document it. Record every action with the time and who authorised it. Complete a handover log at the end of your shift.

Then there is step 3.6, which is marked in red.

The analyst shall not take containment action on any host.

Shall not. It does not say "should avoid." It does not say "only with care." You have no authority to disconnect a machine, isolate a host, or shut anything down. That decision belongs to the SOC Manager.

That was Alert 2 last night. Ransomware, and the client telephones at ten past ten asking you to disconnect the laptop.

Raise your hand if you said yes.

[Some hands. Respond warmly.]

Thank you for being honest. I want to say something to those of you with your hands up.

Your instinct was correct. The client was frightened. It was genuinely ransomware. Wanting to help was the right response.

The instinct is right. Acting on it yourself is what is wrong.

There are three reasons. You do not know what else that machine is doing. You do not know whether disconnecting it destroys evidence that Level 2 will need in an hour. And you do not know whether it will take a production system down with it.

What you say instead is this. "I do not have the authority to do that. I am escalating to the SOC Manager now, and they will call you back."

Then escalate immediately. Do not simply say it to end the call.

That answer is not unhelpful. It is professional, and an assessor will ask you about it.

---

# SLIDE 6 — THE CLOCK
### 6 minutes

This next item catches almost everyone. We will spend a few minutes on it.

Look at the timeline on the slide.

At 22:00 the alert arrives. That is receipt.

At 22:20 you finish assessing it as High. That is assessment.

What time is your notification deadline?

[Take answers. You will hear both 22:15 and 22:35.]

Raise your hand for 22:15.

Now raise your hand for 22:35.

The answer is 22:35.

Read section 3.3 again. Look at the three words immediately before the requirement. It says "within fifteen minutes of assessment." Not of receipt. The clock starts when you finish assessing, at 22:20.

To those who answered 22:15. Your reasoning was that the alert arrived at 22:00, and fifteen minutes later is 22:15. That is a reasonable way to read the sentence. It is also wrong, and you are in very large company.

This exact misreading is the most common cause of missed notification deadlines in real security operations centres. It is not carelessness. It is this sentence.

There is one more point. Look at step 3.1. You were also required to record four fields within five minutes of receipt, so by 22:05. If you missed that, you breached 3.1.

But breaching 3.1 does not move the 3.3 deadline. They are two separate clocks, starting from two different events. Missing one does not give you extra time on the other.

For the rest of your career, whenever you see "within X minutes" in a procedure, the question is not how long. The question is: from when?

---

# SLIDE 7 — THE SEVERITY MATRIX
### 4 minutes

Four levels. You use this on every alert.

Critical means active harm now, or about to happen. Ransomware encrypting files. Confirmed command and control traffic. Data leaving the organisation.

High means confirmed malicious activity, but contained or not yet spreading. Malware that failed to clean. A credential dumping tool. A successful login after many failed attempts.

Medium means suspicious and requiring verification, with no confirmed harm.

Low means routine, expected, or already handled by the tool.

Notice what you are judging. You judge impact and certainty together. How serious would this be, and how confident am I?

Something serious that you are unsure about is not automatically Low. We will return to that point shortly.

One detail that is easy to miss. Alert 2 was Critical, and Critical has a different notification deadline from High. Ten minutes, not fifteen. Read the row. Do not assume.

---

# SLIDE 8 — THE FOUR RULES
### 5 minutes

This is the section most of you missed last night, and it is not your fault. These four rules sit underneath the table, and people stop reading at the bottom of a table.

These four rules override the Matrix.

Rule one. Anything on a domain controller, a backup server, or a finance system is raised one level.

That was Alert 6. A credential dumping tool on DC-01. What did you write?

[Most will say High.]

High is what the table says. Credential dumping is listed as a High example. But DC-01 is a domain controller, and rule one raises it one level. The correct answer is Critical.

This is not a technicality. A domain controller holds every credential in the organisation. Credential dumping on a workstation affects one machine. Credential dumping on a domain controller potentially affects every account in the company.

Rule two. Anything a client reports by telephone is at least Medium until you have assessed it. The reason is simple. A person took the trouble to pick up a phone. That is information in itself.

Rule three. If you cannot decide between two levels, take the higher one and write down why.

Rule four. Uncertainty is not Low. If you do not know what something is, it is Medium at minimum.

Rule four is the whole of Alert 8, and we will come back to it at the end.

Read the line at the bottom of the slide. No one has ever been disciplined for over-assessing with a documented reason.

Over-assessing costs someone twenty minutes. Under-assessing can cost a company its weekend.

---

# SLIDE 9 — THE ESCALATION MATRIX
### 3 minutes

This document tells you who to contact and how quickly.

Critical goes to Level 2 and the SOC Manager, immediately. Telephone first, then a ticket.

High goes to Level 2 within fifteen minutes.

Medium goes to Level 2 by the end of your shift.

Low goes to no one. You close it yourself.

Now look at the final column on the Critical row. It says: call the next name on the on-call list, keep calling, and never leave a Critical unowned.

That sentence exists because this has gone wrong before. At three in the morning, people do not answer telephones. Your job is not to leave a message and consider the matter closed. Your job is to keep working down the list until a person takes ownership.

One more rule from this document. You never contact the Chief Information Security Officer directly. That goes through the SOC Manager. A Level 1 analyst who emails the CISO has skipped four people, and it will be noticed.

---

# SLIDE 10 — WHAT GOES IN AN ESCALATION
### 3 minutes

Every escalation contains six items. There are no exceptions.

The ticket number. What was detected, in one sentence. The affected hosts and users, with exact names. What you have already checked, including whether a change notice covers it. Your severity assessment and your reason for it. And finally, what you are asking for.

That last item is the one people leave out. Read the line beneath it.

An escalation without item six is a complaint, not an escalation.

If you send Level 2 a message saying "there is credential dumping on DC-01," you have told them something is wrong. You have not told them what you want from them.

Do you need a decision? Do you need them to take action? Are you informing them so they are not surprised later?

State it clearly. "I am asking you to take ownership and scope this." Or, "I am asking whether we should contain." Or, "This is for your awareness. I have it under control."

That is six seconds of extra typing. It is the difference between an escalation someone acts on and one that sits in a queue.

---

# SLIDE 11 — WHEN DOCUMENTS DISAGREE
### 6 minutes

This is the most important slide of the session. Three of last night's eight alerts depended on it.

Three types of notice change the rules.

A vendor advisory tells you the tool itself is misbehaving.

That was Alert 3. Trojan.Generic.Heur detected on powershell.exe, using agent version 7.4.2. The advisory states that this exact combination produces false positives. So you verify manually before escalating.

Now read the final line of that advisory. It states that it does not apply to unsigned files, or to files outside the Windows system directories. So if you had seen the same detection on an unsigned file in a user's Downloads folder, the advisory would not apply. You would treat it as a genuine detection.

A change notice tells you a system is being worked on.

That was Alerts 4 and 5, and this pair is worth our time.

Alert 4. At 23:40, servers SRV-MNL-02 and 03 go offline. Change notice CHG-2026-1177 covers exactly those hosts, in exactly that window. So it is not an incident.

Before you closed it, what were you required to record?

[Wait for an answer.]

The change reference. And which step makes that mandatory? Is it "should" or is it "shall"?

It is shall. Step 3.4. Checking for a notice is "should." Recording the reference once you have found one is "shall."

Now Alert 5. Seven minutes later. SRV-CEB-02 goes offline. Same night, same symptom.

Raise your hand if you also marked that one as not an incident.

[Hands go up. Respond warmly.]

Thank you. That is the most useful mistake on the entire sheet.

Cebu is not in the change notice. That notice lists four hosts, and all four are in Manila.

A change notice is a list. It is not general permission to ignore things. If the host is not on the list, the notice says nothing about it. And when a notice says nothing about something, you treat it normally.

The third type is a client service level notice. That was Alert 7, Northwind Trading. The SOP says notify High within fifteen minutes. The Northwind notice says thirty minutes.

Which do you follow?

[Take answers. Someone will say the stricter one.]

To whoever said the stricter one: please explain your reasoning to the class.

[Let them explain. Then continue.]

That is sound reasoning, and it is wrong. I want everyone to understand why.

You do not resolve conflicting documents by choosing the stricter one, or the newer one, or the one you prefer. You check whether the notice has the authority to override.

Look at the Northwind notice. It states this in words. "This supersedes the standard notification timings in SOP-SOC-001 section 3.3 for this client only."

A document that can override says so. If it does not say so, it cannot. And if you cannot tell, you ask.

Read the last four words of that sentence again. "For this client only." That answers the final question. Sunrise Manufacturing's timings did not change.

---

# SLIDE 12 — CLOSING
### 2 minutes

One last point, then we move on to today's material.

Look at the final question on your sheet. It asked which alert was the most dangerous, and which was most likely to be missed at four in the morning.

Most of you identified the credential dumping on the domain controller, or the ransomware, as the most dangerous. Both are good answers.

For the one most likely to be missed, most of you chose Alert 8. The unknown process at four in the morning, with nothing confirmed either way. The file was named svhost32.exe, which is one letter away from a genuine Windows process. That was deliberate.

Notice that these are two different alerts. That is the central problem of this job.

The dangerous alert announced itself. The one you would actually miss did not.

That is what the next thirteen days are training you for. Not to handle the obvious ones. Anyone can escalate ransomware. You are training to notice the quiet one at four in the morning, when you are tired, the queue is finally clear, and it would be very easy to mark it Low and move on.

Low is not a place to put things you have not worked out. Low means you know what it is, and it does not matter.

Keep your marked sheets. Keep the SOP Pack. You will use it again on Days 6 to 10 with real alerts, and again on Day 15 in your assessment.

---
---

# IF YOU ARE SHORT OF TIME

You will not always have fifty minutes. Deliver these three items and hand the rest back with written comments.

| Priority | Where | Why |
|----------|-------|-----|
| **1** | Slide 11, Alerts 4 and 5 | Teaches careful reading better than anything else in the pack |
| **2** | Slide 11, Alert 7 | Document authority is the most transferable idea in the course |
| **3** | Slide 5, Alert 2 | Short, and an assessor will ask about it |

Slides 6 and 8 are the next two to protect.

---

# THREE THINGS THAT MAKE THIS SESSION WORK

**Ask for their actual answers.** If nobody admits to a wrong answer, this becomes a lecture about documents and teaches very little. Get the first wrong answer out early. If necessary, offer your own: "I got this one wrong the first time I saw it."

**Never let a wrong answer sound foolish.** Every mistake on this sheet is a reasonable reading of an ambiguous document. Say so each time, before you explain why it does not hold. You need these trainees volunteering answers for another thirteen days.

**Name the person, not just the answer.** For example: "Marco noticed that Cebu was not on the list." Trainees repeat the behaviour that gets recognised.
