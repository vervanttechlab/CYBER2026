# DAY 2 — INSTRUCTOR RUNBOOK
## Solving Routine Problems on a Real Desk
### Online 8:00 AM – 12:00 PM · Self-study 1:00 – 5:00 PM

---

# BEFORE THE DAY

- [ ] `Fault_Log_Team_A.csv` to `_D.csv` ready to send, one per team
- [ ] Activity Pack sent to trainees. It has the clean fault cards and the worksheets
- [ ] Your copy of `Demonstration_Steps.md` open for the answers. Do not copy from it into the chat. The answers are printed under each card
- [ ] Day 1 work marked and ready to give back
- [ ] Your Day 1 SOP answer key open. You start today with that review
- [ ] A timer you can see. You need it two times today
- [ ] **Teams.** If you formed them on Day 1, they stay the same today and roles change tomorrow. **If you did not form them, you do this at 8:05 — see the Team Formation block**
- [ ] Breakout rooms created and named after the teams. You use them three times today

**Send with the joining note:** Day 2 Student Handout, Day 2 Activity Pack.

### Three things to know about today

**Today uses no new tools. We planned it that way.** The method you teach today is the same one they will use on Days 8, 9 and 13, when a real tool has a problem. Without it, those days become guessing.

**The sixty-second rule is the most useful thing you will do today.** Stop them at sixty seconds every time. A trainee who talks too long in class will talk too long on a real call.

**Watch for the trainee who wants to fix things right away.** They will skip the problem statement and jump to an answer. Make them write the statement anyway. On Day 9, that is the person who escalates before checking.

---

## HOW TO USE THIS SCRIPT

Normal text is what you say. When you feel ready, say it in your own words.

Text inside square brackets is a note for you. Do not read it out loud.

**This script uses simple English on purpose.** Short sentences are easier to say out loud, and easier for your trainees to follow. Keep it that way when you use your own words.

---

## WORDS YOU MAY NEED TO EXPLAIN

Some words in today's material are job words. Trainees will not know them yet. Here is a short, simple meaning for each one. Give the meaning the first time you use the word.

| Word | Simple meaning to give the class |
|------|--------------------------------|
| **Symptom** | What people see and complain about |
| **Root cause** | The real reason it is happening |
| **Escalate** | Pass it to someone with more authority than you |
| **Triage** | Look at an alert quickly and decide how serious it is |
| **Persistence** | Something the attacker leaves behind so the problem comes back |
| **False positive** | The tool says it is bad, but it is not bad |
| **Scope** | How many machines or people are affected |
| **Boundary** | What is NOT affected |
| **Reversible** | You can undo it |
| **On-call** | The person you can phone at night when there is an emergency |

---
---

# THE SCRIPT

**Times:** 8:00 start · 8:05 team formation · 8:20 SOP review · 8:35 problem and cause · 10:00 break · 10:10 options and plans · 11:20 cost · 11:50 afternoon.

[If your teams already exist, skip the team formation block. Start the SOP review at 8:05 and give the extra fifteen minutes back to the SOP review and the fishbone.]

---

# SLIDE 1 — TITLE
### 8:00–8:05

Good morning, everyone. Welcome back.

Please check your camera and your microphone now. Type in the chat if something is not working.

Yesterday we learned how to receive information. Someone tells you something, and you write it down correctly.

Today we learn what to do when the information is that **something is broken**.

It is not an attack. Something is simply broken. For example: an agent stopped sending data three days ago and nobody noticed. Or the same ticket appears four times. Or one hundred alerts all say the same wrong thing.

These problems fill an analyst's week. Attacks are the exciting part of the job, but they are maybe five percent of it. Today we study the other ninety-five percent.

Here is the good news. The method is the same every time. You learn it once, today. You will use it for the rest of your career.

First, we finish yesterday.

---

---

# TEAM FORMATION
### 8:05–8:20 · 15 minutes

[Do this today if you did not form teams on Day 1. **You cannot run either drill without teams**, and the breakout rooms must exist before 9:42.]

[If your teams already exist, skip this block and start the SOP review at 8:05.]

Before we start today's lesson, we need to put you into teams.

You will stay in the same team for the next three days. You will use these teams every day for the rest of this course.

Teams are three or four people. I will read the names now.

[Read out the teams. See the guidance below on how to choose them.]

Now I will send you to your breakout room for five minutes. You have three jobs while you are in there.

**Job one. Choose a team name.**

In real security teams, people use shift names or colours. Blue Watch. Night Shift. Team Sentinel. Choose anything you like, but keep it appropriate for work.

**Job two. Give each person a role.**

There are four roles. Here they are.

The **Shift Lead** runs the team. When the team cannot agree, the Shift Lead decides. The Shift Lead also speaks first in the huddle.

The **Scribe** keeps the team's papers. Worksheets, notes, and answers. If the Scribe loses it, the team has no evidence.

The **Presenter** speaks for the team when we report to the class. This is the person who gives the sixty-second report later this morning.

The **Timekeeper** watches the clock during timed exercises. That job becomes very important from Day 6, when the drills are strict.

If your team has three people, one person takes two roles.

**These roles change every three days.** So everybody will do every role before the course finishes. If you are not the Shift Lead today, you will be soon.

**Job three, and please do not skip this one. Exchange contact numbers.**

Write down each other's phone numbers or messaging names. You will need them this afternoon, because one of your afternoon tasks needs a partner.

Five minutes. Please start.

[Send them to breakout rooms. Visit each room once.]

[Bring them back after five minutes.]

Each team, please type two things in the chat now. Your team name, and the four roles with the names.

[Save the chat log. **This is your evidence record for team formation.**]

Thank you. One last thing about your teams.

In a real security operations centre, you do not choose the people on your shift. You still have to hand your work over to them cleanly at five in the morning. It is the same rule here.

---

## HOW TO CHOOSE THE TEAMS

**Mix the experience levels on purpose.** Put someone who has never opened a command line together with someone who runs a server at home.

This helps both of them. The beginner learns faster from a classmate than from a trainer. And the experienced one discovers that explaining something is much harder than doing it.

**Use what you already know about them.** If you ran the Day 1 icebreaker, use their answers. The trainee who said "no incident, I run my own server" is your strongest person. Put them with a beginner.

If you have no information yet, ask one question before you divide them:

> "Raise your hand if you have ever used a command line, or set up a computer network, or worked in IT support."

Then spread those hands across the teams.

**Create the breakout rooms now, not later.** Name each room after the team. You will use these same rooms three times today. Building rooms in the middle of a lesson wastes time you do not have.

---

## IF DAY 1 TEAM FORMATION DID NOT HAPPEN

Two Day 1 items depend on teams, and you should check whether they are still outstanding.

| Item | Unit | What to do |
|------|------|-----------|
| Team formation record | `400311102` LO1 | You are collecting it today. The chat log is your evidence |
| The shift huddle drill | `400311102` LO2 | **This still needs to be run.** It cannot be done alone, and it needs an observer |

The huddle drill takes twenty minutes. It is in the Day 1 Instructor Runbook, Demo 3, and the materials are in the Day 1 Activity Pack.

**Run it at the start of Day 3.** Do not leave it later than that. `400311102` requires you to watch each trainee take part in a group activity, and you cannot record something you did not see.

---

# SOP REVIEW
### 8:20–8:35 · 15 minutes

[Short version, fifteen minutes. Team formation took the other ten. Cover **Alerts 4 and 5**, then **Alert 2**. Give Alert 7 back in writing, or cover it on Day 3.]

Please take out your Night Shift worksheet.

I will cover three of the eight alerts this morning. You will get the rest back with my comments.

**First, Alerts 4 and 5.**

Alert 4. At 23:40, two Manila servers go offline. The change notice covers them. So it is not an incident. Raise your hand if you got that one right.

[Hands.]

Good. Now Alert 5. Seven minutes later, a Cebu server goes offline. Raise your hand if you also wrote "not an incident."

[Hands go up. Be kind here.]

Thank you for being honest. This is the most useful mistake on the whole sheet.

Cebu is not on the change notice. That notice lists four servers, and all four are in Manila.

**A change notice is a list. It is not permission to ignore everything.** If the server is not on the list, the notice says nothing about it. And if a notice says nothing about it, you treat it in the normal way.

**Second, Alert 7, the Northwind alert.** The SOP says tell the client within fifteen minutes. The Northwind notice says thirty minutes. Which one did you follow?

[Someone will say "the stricter one." Ask them to explain why.]

That is good thinking, but it is wrong. When two documents disagree, you do not choose the stricter one. You do not choose the newer one.

**You check if the notice is allowed to change the rule.**

The Northwind notice tells you. It says: "This supersedes SOP-SOC-001 section 3.3 for this client only." Supersedes means "replaces."

A document that can change the rule will say so. If it does not say so, it cannot.

**Third, Alert 2.** Ransomware. The client phones you and asks you to disconnect the laptop. Raise your hand if you said yes.

[Some hands.]

Your feeling was right. The client was scared. Wanting to help is good.

**The feeling is right. Doing it yourself is wrong.**

You do not have the authority. Step 3.6 says so. What you say is this: "I am not allowed to do that. I am passing this to the SOC Manager now, and they will call you back." Then you pass it immediately.

Keep those sheets. Now, today.

---

# SLIDE 2 — HOW TODAY RUNS
### 8:35–8:38

Today is organised the same way as yesterday. We work together in the morning. You work alone in the afternoon.

This morning we are all here together, because every task before lunch needs other people.

You will work on faults with your team. You will write action plans together. And you will report to me as if I am your supervisor, in sixty seconds, while the class watches.

This afternoon you work by yourself. Today's afternoon tasks are more personal than yesterday's.

You will write down your goals. You will think about how you handle pressure. You will find out how you learn best. And you will write one idea to improve the way we work.

The rule is the same as yesterday. **Team work in the morning. Your own writing in the afternoon.**

And the same reminder: the afternoon is not a half day.

---

# SLIDE 3 — THIS MORNING'S PLAN
### 8:38–8:40

Here is the morning.

The first ninety minutes: finding the real problem, and finding the cause. We break at ten o'clock. After the break: choosing what to do, and writing the plan.

We have two team drills today. At the end of the second one, each team reports to me in sixty seconds. I will stop you at sixty seconds.

That is not me being unkind. Sixty seconds is what you really get in this job.

---

# SLIDE 4 — UNITS COVERED TODAY
### 8:40–8:42

Four units today. That is the most in any day of this course.

**Solving routine problems** takes the whole morning. It is the biggest one.

**Entrepreneurial mindset** sounds strange in a security course. I will explain it before lunch. It takes ten minutes and it is very useful.

This afternoon: **self-management** and **supporting innovation**. Both are writing tasks you do alone.

---

# SLIDE 5 — SYMPTOM OR PROBLEM?
### 8:42–8:52

This is the most important idea today. Everything else depends on it.

**What someone tells you is almost never the real problem.**

Look at the left column. That is what people say. "The dashboard is empty." "I am getting one hundred alerts." "The same ticket keeps coming back."

Now look at the right column. That is what is really happening.

Let me give you an example with no computers in it.

Someone tells you the ceiling in their bedroom is wet. That is the **symptom**. That is what they can see.

So you clean the ceiling and you paint it. It looks fixed. Then it rains again, and the ceiling is wet again.

The real problem is a hole in the roof. And the hole may not even be above that bedroom. Water travels.

Every line in the left column is a wet ceiling. And every one of them will happen to you in your first six months.

One more reason this matters. If you only fix the symptom, the problem comes back tomorrow, on someone else's shift. Now they have to work on something you already touched. That is worse than doing nothing.

---

# SLIDE 6 — THREE QUESTIONS
### 8:52–9:02

So how do you move from the left column to the right column? You ask three questions. Always in this order.

**Question one. What exactly is happening?**

Say what you can see. No guessing yet. Not "the SIEM is broken." Say what is actually on the screen.

**Question two. When did it start? And what else changed at that time?**

I want to stay on question two, because it solves more faults than any tool you will ever be given.

Almost nothing in IT breaks by itself. Things break because **something changed**. A patch. A rule. A password that expired. Someone unplugged a cable so they could plug in an electric fan.

So when a person tells you something broke at two o'clock, your next question is simple: **what else happened at two o'clock?**

**Question three. What is the scope?**

Scope means: how many machines are affected? One computer? One team? One office? Everything?

Scope tells you where to look. One computer means a computer problem. One office usually means a network problem. Everything usually means a server problem.

Three questions. Write them somewhere you can see them at your desk.

---

# SLIDE 7 — BAD AND GOOD
### 9:02–9:10

Here is what those three questions give you.

The bad one is: "The SIEM is broken." Four words. The next person learns nothing. They must start again from zero.

Now read the good one.

"Since about 14:20 today, four Manila servers, SRV-MNL-01 to 04, have shown no events in the dashboard. All other servers are working normally. The four servers reply to ping."

It is longer. That is fine.

Look at what is inside it.

It gives you a **start time**, which is 14:20.
It gives you the **scope**, which is four servers, and it names them.
It gives you the **boundary**: all the other servers are working. That is as useful as the problem itself.
And it gives you **one piece of evidence**: the servers reply to ping. So the machines are switched on, and it is not a power problem.

An analyst who has never seen this fault can read that paragraph and continue the work.

**That is the test.** When you write a problem statement, ask yourself: can the next analyst continue from this? If yes, it is good enough. If no, keep writing.

---

# SLIDE 8 — THE FIVE WHYS
### 9:10–9:20

Now we find the cause. The method is called the Five Whys. You keep asking "why" until the answer becomes something you can change.

Let me walk down this example.

**The problem:** the same malware is detected on one computer every morning.

Why? Because the antivirus finds the file and cleans it every morning.

Why does it come back? Because something writes it back to the disk.

Why does something write it back? Because a scheduled task runs when the user logs in, and it downloads the file again.

Why is there a scheduled task? Because the first infection created it.

Why was it not removed? **Because the antivirus removed the file, but not the thing that keeps downloading the file.**

That is the root cause. Notice: it is not "there is malware." It is "our cleaning was not complete."

It does not need to be exactly five questions. Sometimes three. Sometimes seven. Five is just the usual number.

---

# SLIDE 9 — WHERE IT STOPS
### 9:20–9:30

There are two ways to get this wrong.

**First way: you stop too early.**

If your answer is "because there is malware on the machine," you are not finished. You cannot do anything with that answer. It is just the problem again, in different words.

**Second way: you go too far.**

If you keep asking, you will reach "because the user clicked a link in an email." That is true. But it does not help you at two in the morning. You cannot un-click a link.

**So where do you stop? You stop at the first thing you can actually do.** Remove the scheduled task. That is an action. Stop there.

Now the warning on the slide.

**If your fifth answer is a person's name, go back one step.**

"Because Maria clicked a link." "Because the night analyst did not check." Maybe both are true. But those are training problems. Someone should fix them later, in a meeting, in the daytime. Not you, tonight.

There is a practical reason for this rule, and it is more important than the method.

When your analysis ends with a person's name, it stops being troubleshooting and becomes blame. And when your team thinks you are looking for someone to blame, **they stop telling you things**. Then you cannot fix anything, because nobody reports anything to you.

Find the technical cause first. Every time.

---

# SLIDE 10 — THE FISHBONE
### 9:30–9:42

One more method, then you will try it yourselves.

This is a fishbone diagram. The problem goes at the head of the fish. The bones are the places where a cause can hide. It stops you from fixing on your first idea.

In a security operations centre, six branches cover almost everything.

**Agent.** Is the service running? Is it the correct version? Is the setting correct?

**Network.** Can the computer reach the server at all? Is a firewall rule blocking it?

**Server.** Is the server running? Is the disk full? A full disk is a very boring cause of a very dramatic problem.

**Configuration.** Did someone change a rule, a filter, or a setting?

**Host.** Did the machine restart? Is it updated? Is it switched on?

**Process.** Is there a change notice? Did a person do this on purpose and forget to tell us?

Now here is the question that turns this list into a method.

**Which of these can I check in less than five minutes?**

You will always have twelve possible causes. You cannot check twelve. So you put them in order, from cheapest to check to most expensive.

Five minutes of ping, and checking if a service is running, will remove half the diagram. And it costs you nothing.

**Check the cheap ones first. Every time.**

---

# TEAM FAULT DRILL 1
### 9:42–10:00

Now it is your turn. Teams, go to your breakout rooms.

Fault Card 1 is Part 1 of your Activity Pack. Open it now. Worksheet A is Part 2, just below it. I am also sending each team your own fault log file.

You have fifteen minutes. I want three things on Worksheet A.

**One. A problem statement.** One paragraph. What, when, scope, boundary. The good version, not "the dashboard is broken."

**Two. A Five Whys chain.** Go as far as you can. If you run out of information, write down what you would need to find out.

**Three. A list of possible causes, in order.** Next to each one, write how you would check it in five minutes.

You will not have enough information to be sure. We did that on purpose. In real work, you are never sure.

Fifteen minutes. Please start.

[Send them to the breakout rooms. Visit each room. If a team jumped to an answer, send them back to the problem statement.]

[Bring them back at 9:56. Two minutes per team. The presenter speaks.]

[After all the teams have spoken:]

Thank you. Now here is the real cause.

The Manila office had a planned power interruption. It was announced by **Facilities**, not by IT. The backup power system switched over at 14:20. The network switch for those four servers restarted.

The servers stayed on. That is why they reply to ping. But the agents lost their connection, and they never reconnected, because the agent service does not keep trying forever.

Now, raise your hand if you looked for a change notice.

[Several hands.]

Good. That is the correct habit, and you found nothing. Here is why. You were looking for an **IT** change notice. This change came from Facilities.

**That is the first real lesson of the day. Look in more places.** The thing that changed does not have to be a change you were told about. It does not have to come from IT. Buildings have maintenance. Power has schedules. Cleaners unplug cables.

Let us break. Ten minutes. Please come back at ten past ten.

---

# BREAK
### 10:00–10:10

---

# SLIDE 11 — THREE OPTIONS, THREE FILTERS
### 10:10–10:25

Welcome back. You found the cause. Now, what do you actually do?

New analysts pick the first idea they think of. Experienced analysts write down three, because **the first idea is often the most expensive one**.

Look at the table. Four options for the four servers that stopped reporting.

**Restart the agent service.** Five minutes. You lose the events that were still travelling. You are allowed to do this.

**Restart the four servers.** Thirty minutes, plus downtime. The business is affected. **You are not allowed to do this.** It needs approval.

**Wait for the maintenance to finish.** It costs nothing. The risk is that you waited for no reason, if maintenance was not the cause.

**Pass it to IT now.** Five minutes. The risk is that you waste their time, if this was expected.

Now use three filters. **In this order.**

**Filter one. Am I allowed to do it?** If the answer is no, it is not an option. It is an escalation. Cross it out.

**Filter two. Can I undo it?** Choose the fix you can undo. You can undo a service restart. You cannot undo a deletion.

**Filter three. Is it the smallest thing that could work?** Restart the service before you restart the computer. Restart the computer before you rebuild it.

Here is the sentence to remember from this slide.

**The dangerous analyst is not the one who does not know the answer.** That person asks a question, and asking is fine.

**The dangerous one is the person who does something big that cannot be undone, because it felt strong and decisive.** Restarting four production servers at two in the morning feels like taking action. It is also how a small monitoring fault becomes a real outage.

---

# SLIDE 12 — THE SHAPE OF A PLAN
### 10:25–10:35

You chose your action. Now write it down properly, because you will give it to another person.

There are seven parts.

**Problem.** The paragraph you already wrote.

**Cause.** The root cause, written as something you can change.

**Action.** Numbered steps. Each step is one thing, and you can check that it happened.

**Who.** A name or a job title for every step. Not "someone."

**When.** A time or a deadline for every step.

**How we will know it worked.** Something you can see or measure.

**If it does not work.** The backup plan, and who you pass it to.

The last two are the parts people forget. They are also the two parts that make this a plan and not a wish.

Here is what happens without them. You do the fix. Someone asks, "is it fixed?" You say, "I think so." That goes into the ticket. Three days later, nobody knows if it worked.

---

# SLIDE 13 — A REAL PLAN
### 10:35–10:45

Here is one written out completely, for the repeating detection from earlier.

Read the action block. Five steps. Each one is one action you can check. Each one has a person and a time.

Now look at **step three**. It says "pass the task removal to L2."

Why is step three not "delete the scheduled task"?

[Take answers.]

Because deleting a scheduled task **changes the system**. That is above a Level 1 analyst. You found it. You wrote it down. You pass it up.

That is not being afraid. That is being correct, and an assessor will look for exactly that.

Now look at the **success** line. It says: "No detection between 08:05 and 08:20, for three working days in a row."

Read that sentence again, and notice what is inside it.

There is a **time window**: 08:05 to 08:20.
There is a **number of days**: three.
And there is a **test you can answer yes or no**: did a detection appear, or not?

So tomorrow morning you open the screen and you look. Did a detection appear between 08:05 and 08:20? Yes or no. You do the same thing the next day, and the next day. After three clean days, the ticket is finished.

Now think about the words "seems fixed."

How do you check "seems fixed"? You cannot. There is no time window. There is no number of days. There is no yes-or-no test. It is only a feeling in your head.

**That is the difference.** A good success line can be checked by another person, on a different day, without asking you.

**Decide what "fixed" means before you start.** If you do not, you can never close the ticket honestly. So you will close it dishonestly. That is exactly how Fault Card 3 happens, where four analysts close the same ticket four times, because nobody decided what "fixed" meant.

---

# SLIDE 14 — THREE AUDIENCES
### 10:45–10:55

One plan. You will say it three different ways.

**To your supervisor:** the technical details, what you already checked, and what you need from them. Three or four sentences.

**To the client:** what is happening, what it means for them, and when you will contact them again. Two sentences, and **no technical words at all**.

**To the ticket:** everything, in order, with times. This is the permanent record.

Let me show you all three, for the same fault.

**To the Level 2 analyst:** "Ticket 6602, computer WKS-118. The same malware is detected every morning at logon. Antivirus quarantines the file, but it comes back. I think a scheduled task is downloading it again at logon. I already exported the task list. I need you to remove the task, because I am not allowed to."

**To the client:** "Good morning. One computer in your office is finding the same malware every morning. It is blocked every time, so nothing has spread. We found why it keeps coming back, and we are removing it today. I will confirm with you by tomorrow afternoon."

Notice what disappeared for the client. No task names. No ticket number. No mention of who is allowed to do what.

Now notice what was **added**: "nothing has spread." That is the only thing the client really wanted to know.

And notice what must **never** disappear from the ticket. All of it. Every step, every time, every name. The ticket is what someone reads in six months, when they ask you why you did that.

---

# TEAM FAULT DRILL 2 AND THE SIXTY-SECOND REPORT
### 10:55–11:20

Second drill. This one is harder. The first symptom will send you in the wrong direction.

Fault Card 2 is Part 3 of your Activity Pack. Worksheet B is Part 4. Twelve minutes in your rooms. This time I want the complete action plan, all the parts.

Then your presenter reports to me as if I am your Level 2. Sixty seconds. I will stop you at sixty.

Please start.

[Twelve minutes. Visit the rooms. Bring them back.]

Presenters, please. Sixty seconds each. I am timing you.

[Run each team. Stop them at exactly sixty seconds, even in the middle of a sentence.]

[After all teams:]

Some of you were stopped. Let me explain why that rule is here.

Your Level 2 at ten at night has eleven other things happening. **Sixty seconds is what you really get.** If you use forty of them explaining the background, you never reach the important part.

**Start with the ticket number and what you need. Give the details after.**

Now, the real cause of Card 2.

The computer started a Windows Update at 21:50. The update program was contacting Microsoft's download servers. A firewall rule is blocking that whole group of addresses. Every blocked connection creates one alert.

It is a false positive. A normal, scheduled program met a badly written blocking rule.

Raise your hand if you thought this was malware.

[Hands.]

That is the correct instinct. Read the symptom again. A computer whose user went home four hours ago is making hundreds of outbound connections, on port 443, to hundreds of different addresses. That looks exactly like malware calling home.

The one piece of evidence that tells you the difference is the Windows Update starting **five minutes before the alerts began**.

That is the same lesson as question two this morning. **What changed just before it started?** It is the most reliable question in troubleshooting.

---

# SLIDE 16 — WHAT AN ALERT COSTS
### 11:20–11:35

[Slide 15, the sixty-second slide, was covered during the drill. Show it quickly if you skipped it.]

Now we move to a different unit. The name sounds strange in a security course, so let me explain it.

**Entrepreneurial mindset.** Nobody is asking you to start a business. Here it means one thing: think about the work the way the owner of the company thinks. You think about cost, waste, quality, and the company's reputation.

Let me make it real, because a security service is sold by the hour.

An alert handled correctly the first time costs about **eight minutes** of your time.

The same alert passed wrongly to Level 2 costs about **forty-five minutes** of their time, plus your eight. So one wrong escalation costs about six times more than a correct one.

A **missed** critical alert costs a client incident, a contract penalty, and sometimes the whole contract.

And a wrong escalation at three in the morning costs an on-call manager their sleep. It also costs their trust in you. That is expensive, and it takes a long time to rebuild.

Nobody gives a Level 1 analyst a budget. But every decision you make spends someone's money. Analysts who understand this get promoted, because they escalate the right things, and people learn to trust their work.

---

# TEAM SCENARIO
### 11:35–11:50

A short team exercise, then I will let you go.

It is Part 6 of your Activity Pack. Here is the situation.

Your security operations centre has forty clients and three analysts on the night shift. The number of alerts has doubled in one month. Nothing has been missed yet. But the queue is not finished before the shift ends.

I want three recommendations. For each one: what it would change, what it would cost in time or money or risk, and what could go wrong.

Ten minutes in your rooms.

[Bring them back. One recommendation from each team.]

Notice something about your answers. Almost every team said **reduce the noise**. Fix the noisy rule. Group the same alerts together. Fill the ticket fields automatically. Find out which client creates the most alerts, and why.

Almost nobody said "hire more people."

**That instinct — fix the process before you spend money — is exactly what this unit is asking you to show.** It is also what a manager wants to hear from an analyst.

---

# SLIDES 17 TO 20 — YOUR AFTERNOON
### 11:50–11:56

Here is your afternoon. It is more personal than yesterday's.

Six tasks, about three and a half hours. They are listed in Part 7 of your Activity Pack.

**One. Your goals.** Personal and career, at one year and three years.

Look at the ladder on the slide. Level 1, then Level 2, then Level 3 or threat hunter, with side paths into vulnerability management and incident response. That is a real ladder. People climb it in three or four years.

One item on that sheet matters more than the others: **the one thing you will do in the next thirty days.** Everything above that line is only a wish until you do something. Make it small, and make it real.

**Two. Recognising emotions.** Four feelings that change how you work: alert fatigue, panic, frustration, and overconfidence. Read them, then write three honest sentences about times you felt three of them.

I want to say something about this task, because some of you will want to skip it, or write something safe.

This looks like the easy unit. It is not. **Shift work in this job tires people out faster than almost any other IT job.** The analysts who last five years are the ones who noticed they were getting tired and did something about it. The ones who leave are usually fine, fine, fine, and then suddenly gone.

Your writing is private. Only I will read it. I am not marking whether your feelings are correct. I am marking whether you can **notice** them. That is the whole skill.

**Three. The learning-style questions.** They are short. The useful part is the last line, where you write one clear plan for the part of the course you think will be hardest for you.

Do not write "I learn by doing." That is just a fact, and it does not help you. Write something like: "On Day 5, when it becomes theory, I will ask for a demonstration instead of losing attention." **That** is self-management.

**Four. One improvement proposal.** This is where people freeze, because they think an idea must be clever.

It does not. Look at the four signals: something repeats, people use a workaround, someone complains, or you nearly missed something. Choose something you really noticed on Day 1 or today.

"Add one field to the handover form" is a completely good proposal. It is also the kind that actually gets used, unlike the clever ones.

**Five. Swap with your partner.** One good comment and one question about their proposal. This is a graded part of the unit, so please do not skip it. You have their contact number from yesterday.

**Six. Finish your two worksheets** from this morning.

---

# WHICH FILE DO I OPEN?
### 11:56–12:00 · 4 minutes

[Share your screen and show the table below while you say this. Trainees get confused about which document to open. Four minutes here saves you many messages this afternoon.]

Before you go, I will tell you which file to open for each task. Please write this down.

**You have two documents today. Only two.**

The first one is the **Student Handout**. This is the one you **read**. It explains the ideas from this morning. It also has two forms inside it. Your Goal Sheet, and your Improvement Proposal form.

The second one is the **Activity Pack**. This is the one you **write in**. It has the fault cards, your two worksheets, the team scenario, and the list of your six afternoon tasks.

Here is the simple rule.

**The Activity Pack tells you what to do. The Student Handout is where you write two of the answers.**

Now let me go through the six tasks and tell you where each one is.

**Task 1, your goals.** Open the Student Handout. Look for "My Goal Sheet."

**Task 2, recognising emotions.** Same document. The Student Handout, in the self-management section.

**Task 3, how you learn.** Same document again. It is part two of the Goal Sheet.

**Task 4, your improvement proposal.** Still the Student Handout. Look for "SOP Improvement Proposal."

**Task 5, swapping with your partner.** Send them your proposal. They send you theirs. You write one good comment and one question on their form. Then send it back.

**Task 6, your two worksheets.** These are in the Activity Pack, Part 2 and Part 4. If you did not finish them this morning, finish them now.

So: **four tasks in the Student Handout. Two tasks in the Activity Pack.**

You also have one more file, your team's fault log. That is the CSV file I sent to your room. You only need it if you are still finishing Worksheet A.

## What you send me tonight

Six things. Let me read them.

One, Worksheet A. Two, Worksheet B. Three, your team scenario answers. Four, your Goal Sheet, with all three parts filled in. Five, your Improvement Proposal. Six, your comment and question on your partner's proposal.

Save all of them in your **Evidence, Day 02** folder on your own computer. Then send me copies.

If you cannot finish something, send it anyway and tell me what is missing. I would much rather see an unfinished worksheet tonight than nothing tomorrow.

---

## THE FILE GUIDE — put this on screen

| What you need | Which file | Where inside it |
|---------------|-----------|----------------|
| Fault Card 1 | **Activity Pack** | Part 1 |
| Worksheet A | **Activity Pack** | Part 2 |
| Fault Card 2 | **Activity Pack** | Part 3 |
| Worksheet B | **Activity Pack** | Part 4 |
| The sixty-second report | **Activity Pack** | Part 5 |
| Team scenario | **Activity Pack** | Part 6 |
| Your six afternoon tasks | **Activity Pack** | Part 7 |
| Today's ideas, explained | **Student Handout** | All of it |
| **Goal Sheet** (Tasks 1, 2, 3) | **Student Handout** | "My Goal Sheet" |
| **Improvement Proposal** (Task 4) | **Student Handout** | "SOP Improvement Proposal" |
| Your team's fault data | **Fault_Log_Team_[your letter].csv** | — |

---

# CLOSING
### 12:00

Tomorrow is information handling, safety, environment, and quality. The most useful part is learning how to judge whether a threat information source can be trusted. Acting on a bad source is worse than doing nothing.

Good work this morning. I will stay on the call for five minutes if anyone wants to ask me something privately.

---
---

# QUICK REFERENCE

## When you stop presenting

| Time | What happens |
|------|-------------|
| 8:05–8:20 | Team formation and breakout rooms *(only if not done on Day 1)* |
| 9:42–10:00 | Team fault drill 1, then the Facilities answer |
| 10:55–11:20 | Team fault drill 2 and the sixty-second reports. Stop them at sixty every time |
| 11:35–11:50 | Team scenario, the forty-clients problem |

## The three answers

| Drill | The cause | The lesson |
|-------|----------|-----------|
| **Fault Card 1** | A Facilities power interruption restarted the switch. The agents did not reconnect | The change notice was not from IT. Look in more places |
| **Fault Card 2** | Windows Update contacting download servers, blocked by a bad firewall rule | Check what started just before the symptom |
| **Fault Card 3** *(spare)* | Cleaning was not complete, and four analysts closed it without checking the history | Two causes: one technical, one process. The process one costs more |

## Evidence to collect today

- Two Problem-Solving Worksheets per trainee *(400311103 LO1–LO4)*
- Sixty-second report, watched, from every trainee *(400311103 LO4)*
- Goal Sheet: goals, emotions, learning style *(400311104 LO1–LO3)*
- SOP Improvement Proposal and partner comment *(400311105 LO1–LO3)*
- Team scenario recommendations *(400311109 LO1–LO2)*

---

## THE FOUR DAY 2 FILES — TRAINER SUMMARY

| File | Who gets it | What it is for |
|------|------------|---------------|
| `Day_2_Student_Handout` | Trainees | Reading, **and** the two forms they fill in — Goal Sheet, Improvement Proposal |
| `Day_2_Activity_Pack` | Trainees | Fault cards, both worksheets, team scenario, and the afternoon task list |
| `Fault_Log_Team_A` to `_D` | One per team | The data for Fault Card 1 |
| `Day_2_Instructor_Runbook` | **You only** | This document |

**Send the first two with your joining note, before the session starts.** Send the fault logs into the breakout rooms at 9:42.

> **A known rough edge.** The afternoon task *list* is in the Activity Pack, but four of those six tasks are *completed* in the Student Handout. Trainees find this confusing, which is why the file guide above exists. If you would rather have all the fillable forms in one place, the Goal Sheet and the Proposal form can be moved into the Activity Pack. Ask and it can be changed.
