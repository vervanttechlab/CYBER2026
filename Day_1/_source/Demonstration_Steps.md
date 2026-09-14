# DAY 1 — DEMONSTRATION STEPS
## The three things you personally have to perform

---

## START HERE

Most of Day 1 you are talking, and the Presenter Script gives you the words. **Three times in the morning you stop talking and actually perform something.** Those three are in this document, in the order you do them.

| | What you do | Time | How long |
|---|---|---|---|
| **DEMO 1** | Read out a shift handover. They write it down by ear. | 10:35 | 15 min |
| **DEMO 2** | Show the wrong way and the right way to confirm an instruction. | 11:00 | 12 min |
| **DEMO 3** | Run a team huddle yourself, then the teams run theirs. | 11:30 | 20 min |

There is a fourth script at the back of this document. **You do not use it on Day 1.** It is for the Day 2 debrief. Ignore it until tomorrow.

---

## HOW TO READ THIS DOCUMENT

Two things appear over and over. They are marked clearly, and they never mix.

> **SAY** — the words in the box are what comes out of your mouth. You can change the wording. Do not change the meaning.

**DO** — an action. Share a screen, stop sharing, pick a person, start a timer, stay silent.

---

## BEFORE THE DAY — 15 MINUTES OF PREPARATION

Do this the night before, not at 10:30 in the morning.

- [ ] **Print the Demo 1 handover script on paper.** On paper. Not on your screen — you will be sharing your screen and they will see it.
- [ ] **Read the handover script out loud once, timed.** It should take about 90 seconds. If you are taking three minutes, you are reading too slowly.
- [ ] **Pick which hostname you will mumble.** Decide now. `WKS-042` is the one this document assumes.
- [ ] **Check your breakout rooms work.** Create them, join one, come back. Do not discover a problem at 11:00.
- [ ] **Have a timer you can see** — phone, kitchen timer, anything. You need it for Demo 3.
- [ ] **Copy the huddle scenario card** into a document ready to paste into the chat.

---

## FIVE THINGS THAT MATTER MORE THAN BEING POLISHED

You are new at this. Read these five before you read anything else — they are what actually decides whether these demos work.

**1. Do not slow down the handover.** Every instinct will tell you to speak slowly and clearly so they can keep up. Fight it. The entire point is that a real handover comes at real speed. If you slow down, everyone succeeds, nobody learns anything, and you have wasted the best fifteen minutes of the day.

**2. The ten seconds of silence is real.** After you finish reading, you say nothing for ten seconds. It will feel unbearably long to you. It feels normal to them, because they are writing. Count it in your head. Do not fill it.

**3. You are allowed to be imperfect.** If you stumble over a ticket number, keep going. Real handovers have stumbles in them. The only mistake that matters is slowing down or explaining as you go.

**4. Say people's names when they do it right.** "Ana just repeated the hostname back before agreeing. That is exactly the skill." Trainees copy whatever gets named out loud. This is the cheapest teaching tool you have and new instructors always forget it.

**5. If you get lost, say so.** "Give me a second, I have lost my place." Nobody thinks less of you. Pretending is worse than pausing.

---

# DEMO 1 — THE SPOKEN HANDOVER
### 10:35–10:50 · 15 minutes

## What this is

You read out a shift handover, once, at normal speed. They write down what they can. Then you show them what was actually said and they see the gaps.

## Why it matters more than anything else today

This cannot be done any other way. It cannot be a worksheet, it cannot be homework, and it cannot be caught up later. **If this demo does not happen, that part of the unit does not happen.** If your morning is running late, take the time from somewhere else.

## Before you start

- [ ] The script is **on paper** in front of you
- [ ] You know which hostname you are mumbling
- [ ] Everyone has a pen and paper — ask them, do not assume

---

## STEP 1 — Stop sharing your screen

**DO:** Stop the screen share. Completely. Camera on, screen off.

> **SAY:**
> "I am taking the slide down now. You have to do this by ear, and if the slide stays up you will just copy the five headings off it and learn nothing."

**Why this matters:** if the handover-structure slide is still on screen, they copy the five section headings and fill them in. You will have tested their reading, not their listening. This is the single most common way this demo fails.

---

## STEP 2 — Set it up

> **SAY:**
> "Get a pen and paper. Not a document on your computer — paper, if you have it.
>
> Here is the situation. It is nine o'clock at night. You have just arrived for your shift. The analyst who is going home is about to hand over to you. I am going to say it once, at normal speed. I am not going to slow down, because in real life nobody slows down for you.
>
> Write down whatever you think matters. Go."

**DO:** Do not answer questions at this point. If someone asks "how long is it?" — say "you will find out," and start.

---

## STEP 3 — Read the script

**DO:** Read it at normal conversational pace. Mumble the one hostname you chose. Do not explain anything as you go.

> "Okay, handover. Three open items. Ticket 4471, that's the PE infection on WKS-042, Defender quarantined it but the scan hasn't finished, so someone needs to check that before midnight. Ticket 4478, phishing report from the Finance team, three users clicked, I've raised it but I haven't confirmed whether credentials were entered — that one needs a follow-up call. Ticket 4482 is a firewall alert storm from 203.0.113.45, I assessed it as routine scanning noise, it's documented, you can close it if it doesn't come back.
>
> One escalation: I sent ticket 4469 to L2 about an hour ago, that's the EDR credential-dumping alert on the Manila server, Ryan owns it now, don't touch it.
>
> Watch item: the Cebu branch firewall has been dropping its log feed intermittently since about seven. It's not down, it just gaps. If it stops completely, raise it with IT immediately.
>
> System status: the vulnerability scanner is in maintenance until six in the morning, so no scans tonight. Everything else is green.
>
> Client note: Northwind called twice asking about the report from Tuesday. Don't promise them a date, just log it and tell the day shift. That's everything."

---

## STEP 4 — Say nothing for ten seconds

**DO:** Silence. Count to ten in your head. Do not fill it. Do not ask "everyone okay?"

---

## STEP 5 — Get three read-backs

**DO:** Pick three people, in this order — someone confident, someone quiet, someone at random. Name them directly. Do not ask for volunteers, you will get the same two people all fifteen days.

> **SAY:**
> "Okay. Pens down.
>
> [Name] — read me back what you wrote.
>
> [Name] — what did you get?
>
> [Name] — and you?"

---

## STEP 6 — Show them the real answer

**DO:** Share your screen. Put this table up.

| Section | What was actually said |
|---------|----------------------|
| **Open items** | 4471 — PE infection WKS-042, quarantined, scan unfinished, **check before midnight** |
| | 4478 — Phishing, Finance, 3 clicked, **credential entry unconfirmed, follow-up call needed** |
| | 4482 — Firewall alert storm from 203.0.113.45, assessed routine, **may close if it does not recur** |
| **Escalated** | 4469 — EDR credential dumping, Manila server, **owned by Ryan (L2), do not touch** |
| **Watch items** | Cebu branch firewall dropping log feed since ~19:00. **If it stops completely, raise with IT immediately** |
| **System status** | Vulnerability scanner in maintenance until 06:00. **No scans tonight.** Everything else green |
| **Client notes** | Northwind called twice re: Tuesday's report. **Do not promise a date.** Log and pass to day shift |

**DO:** Ask these four questions one at a time. Hands up, or answers out loud.

**Ask each one, count the hands, then give the answer below and say what it means.** The
count matters as much as the answer — it is how they see the gap for themselves.

---

### Question 1 — "Who wrote down all three ticket numbers?"

> ## ANSWER: **4471, 4478, 4482**

- **4471** — PE infection on WKS-042
- **4478** — Phishing in Finance
- **4482** — Firewall alert storm

**Expect: about half the class.** Most people get two of the three. The one usually missed
is 4482, because it came last and sounded least urgent.

> **SAY:** "Ticket numbers are how you find the thing again. A note that says 'the phishing
> one' is useless at three in the morning when there are four phishing tickets."

---

### Question 2 — "Who got 203.0.113.45 exactly right?"

> ## ANSWER: **203.0.113.45**

**Expect: very few. Often nobody.** This is the point of the question.

Common wrong versions: `203.0.113.5`, `203.0.13.45`, `203.113.0.45`, or just "the firewall IP".

> **SAY:** "Almost nobody gets the address. And an address that is one digit wrong is not a
> near miss — it is a different machine, owned by somebody else, possibly in a different
> country. This is exactly why we read things back, which is the next thing we do."

---

### Question 3 — "Who caught that you must not touch ticket 4469?"

> ## ANSWER: **4469 was escalated to Level 2. Ryan owns it. Do not touch it.**

**Expect: fewer than you would like.** People write down "4469 escalated" and drop the
instruction attached to it.

> **SAY:** "This is the most expensive one to miss. If you start working 4469, you are now
> two people investigating the same incident without knowing about each other. You will
> undo each other's work, and you may destroy evidence Ryan needs."

---

### Question 4 — "Who caught that there are no scans tonight?"

> ## ANSWER: **The vulnerability scanner is in maintenance until 06:00. No scans tonight.**

**Expect: the fewest hands of all four.** System status is the section people stop listening
to, because it sounds like admin rather than work.

> **SAY:** "Here is why that one matters. If you did not write that down, at two in the
> morning you would try to run a scan, it would fail, and you would spend forty minutes
> troubleshooting a scanner that is not broken. It is switched off on purpose, and somebody
> told you so."

---

> **If a lot of hands go up on all four:** you read too slowly. Say so honestly —
> *"that was easier than it should have been, I slowed down"* — and move on. Do not redo it.

---

## STEP 7 — Make the point and move on

> **SAY:**
> "Look at the differences.
>
> Nobody got everything. That includes the people who sounded confident. That is not a criticism of anyone — it is the entire point of this exercise. Nobody's memory is good enough. Not mine either. I have the script in front of me and I would not have got it all by ear.
>
> That is exactly why this gets written down. And it is exactly why we read it back — which is the next thing."

---

## IF IT GOES WRONG

| What happens | What you do |
|---|---|
| **Someone asks you to repeat it** | Say no, kindly: *"Not this time — in a real handover you get one pass. But hold that thought, because asking me to repeat something is the next thing we are learning."* Then genuinely praise them for asking when you get to Demo 2. |
| **Nobody has paper** | Let them type. It is worse but it is not fatal. Say: *"Typing is fine, but do not open the handout."* |
| **You lose your place mid-script** | Stop, say *"give me a second"*, find it, carry on. Do not restart. A real handover has stumbles too. |
| **Someone was disconnected and missed it** | Do not re-read it for the whole class. Note their name and run them privately during the break, or at the start of Day 2. |
| **They all got it nearly perfect** | You read too slowly. Say so honestly: *"That was easier than it should have been — I slowed down. Let me tell you what real speed sounds like."* Then move on. Do not redo it. |
| **The silence feels unbearable** | It is supposed to. Count. They are writing. |

## How you know it worked

Nobody got all seven items. Two or three people missed the "do not touch 4469" line. At least one person wrote the mumbled hostname wrong or left it blank. **That is a successful demo, not a failed one.**

---

# DEMO 2 — THE READ-BACK RULE
### 11:00–11:12 · 12 minutes

## What this is

You give one trainee an instruction and let them say "okay." Then you show why "okay" is dangerous. Then you do it again properly with a second trainee.

## Why it works

Because you deliberately reuse a hostname from the handover fifteen minutes ago — and the number is slightly different. Almost nobody notices. That moment does more teaching than any explanation.

## Before you start

- [ ] You said `WKS-042` in the handover
- [ ] You will now say `WKS-024` — **the digits are swapped**. Check you have this the right way round before you speak.

---

## STEP 1 — Explain the rule in one sentence

> **SAY:**
> "Before you act on an instruction that matters, you repeat it back in your own words and wait for confirmation. That is the whole rule."

---

## STEP 2 — Show the wrong way

**DO:** Pick a trainee. Say this quickly and casually, like you are busy.

> **SAY:**
> "[Name], can you check WKS-024 for me, the one with the quarantine failure, and let the IT manager know?"

**DO:** They will say "okay" or "sure." That is what you want. Thank them.

> **SAY:**
> "Thank you. Now everybody notice what just happened.
>
> I said WKS-024. In the handover fifteen minutes ago, I said WKS-042. Those are different machines. Nobody caught it. Including me — and I am the one who said it.
>
> That is how it happens. Not through carelessness. Through two people being polite and efficient with each other."

**If someone does catch it:** even better. Name them immediately — *"[Name] caught it. That is exactly the skill, and most classes do not spot that."* Then carry on with the same teaching point.

---

## STEP 3 — Show the right way

**DO:** Pick a different trainee. Same instruction.

> **SAY:**
> "[Name], same instruction, but this time read it back to me before you agree.
>
> Can you check WKS-024, the one with the quarantine failure, and let the IT manager know?"

**DO:** Coach them if they hesitate. Feed them the words if you need to — this is a demonstration, not a test.

> The answer you are looking for:
> "Confirming — WKS-024, not WKS-042, checking the quarantine failure, notifying the IT manager. Is that right?"

> **SAY:**
> "That. That is the whole skill. Four seconds."

---

## STEP 4 — Name the three parts

> **SAY:**
> "Three things in every good read-back.
>
> One: the identifier, said back exactly. The machine name, the address, the ticket number.
>
> Two: the action. What you are actually being asked to do.
>
> Three: the notification. Who you are going to tell. This is the part that gets dropped most often."

**DO:** If you have time, put these four failure modes on screen. If you are behind, skip the table and just say the first row.

| Mistake | Why it fails |
|---------|-------------|
| Saying "okay" or "got it" | Confirms nothing. The sender learns nothing about what you heard |
| Repeating word for word without understanding | Catches mishearing but not misunderstanding |
| Reading back only part of it | The part you drop is usually the notification |
| Asking after you have already started | Too late — you already acted on a guess |

---

## STEP 5 — Go round the room

**No breakout rooms. No pairs. No cards to hand out. No scoring.** You do this yourself, in
the main room, one trainee at a time, while everybody else watches.

It is the simplest drill of the day to run, and it gives you better evidence than pairs did —
because you personally see and hear every single trainee do it.

### WHAT YOU SAY

> "Now we go round. I am going to give each of you one instruction, the way a supervisor
> would. You do two things back:
>
> **One — read it back to me in your own words.**
> **Two — ask me one question about it.**
>
> Any question. There is always something worth asking.
>
> I am not trying to catch anybody out. If you get stuck, I will help you. Let us start."

### WHAT YOU DO

Work down your list of names. Read **one instruction** to each trainee, at normal speed.
Use the list below — it does not matter which order.

After each read-back, say **one sentence** of feedback and move straight on. Do not stop to
teach. Keep it moving — you want everybody to get a turn.

**Eight or nine trainees, about 45 seconds each, is ten minutes.**

### YOUR INSTRUCTIONS — read one to each trainee

| # | Read this out loud | Watch for |
|---|-------------------|-----------|
| 1 | "Check WKS-207 for the quarantine failure — not WKS-270 — and tell the IT manager before midnight." | Do they say **207**, not 270? |
| 2 | "Confirm the scan on ticket 4471 has finished and tell me, and do not start anything new after four." | Do they get **both** halves? |
| 3 | "Do not close ticket 3402. Level 2 is still on it." | Do they keep the word **not**? |
| 4 | "If the DLP alert on jdelacruz comes back, escalate it straight to the information security manager." | Do they keep the **if**? |
| 5 | "Run the agent-status check and tell me anything offline for more than an hour." | Do they say who to tell? |
| 6 | "The Davao firewall alerts are expected tonight, there is a change on. Just document them." | Do they catch **do not escalate**? |
| 7 | "Take the intake on this call, then hand it to me. I will do the assessment." | Do they stop at intake? |
| 8 | "Ticket 3390 needs a client call before end of shift. It is High severity." | Do they say the **ticket number**? |
| 9 | "Two things: chase the Northwind report, and hand over to the day shift by five." | Do they get **both**? |

### WHAT A GOOD ANSWER SOUNDS LIKE

Using instruction 1:

> *"Confirming — WKS-207, not 270, checking the quarantine failure, and I tell the IT manager
> before midnight. Is that right?"*
>
> *"Should I tell them by email or by phone?"*

### YOUR ONE SENTENCE OF FEEDBACK

Pick whichever fits and move on:

- **They got it:** *"Good — you said the machine name back. That is the whole skill."*
- **They dropped who to tell:** *"You got the action but not who to tell. That is the half people always lose."*
- **They said 'okay':** *"That is what most people do, and it confirms nothing. Try it again — say the machine name back to me."*
- **They asked no question:** *"Read-back was good. Now ask me something — anything."*
- **They got the wrong number:** *"I said 207, you said 270. Different machine, different office. That is exactly why we do this."*

**Say people's names when they get it right.** Trainees copy whatever gets named out loud.

### TICK THEM OFF AS YOU GO

Keep a list of names and tick each one. That tick is your evidence for this element.

**Anybody you do not get to, run at the start of Day 2.** Do not let a trainee reach Day 15
without doing this once while you watched.

## IF IT GOES WRONG

| What happens | What you do |
|---|---|
| **The first trainee reads it back correctly instead of saying "okay"** | Praise them, then ask the class: *"How many of you would have just said okay? Be honest."* Hands go up. The point still lands. |
| **A trainee freezes and says nothing** | Feed them the words. *"Try starting with: confirming, WKS-207..."* This is a demonstration, not a test. Nobody fails it. |
| **They just repeat your sentence word for word** | Accept it, then say: *"That works, but say it in your own words next time — parroting catches mishearing, not misunderstanding."* |
| **You are running out of time** | Stop at whoever you have reached. Note the remaining names and run them at the start of Day 2. |
| **Somebody cannot think of a question** | Give them one: *"Try 'by email or by phone?'"* Then move on. |

## How you know it worked

**You ticked off every name on your list.** That is it.

The read-backs being clumsy is fine — first attempt, hour and a half in. What matters is that
every trainee said an instruction back to you out loud while you listened.

---

# DEMO 3 — THE SHIFT HUDDLE
### 11:30–11:50 · 20 minutes

## In one sentence

**You show them one huddle. Then each team runs their own for four minutes while the other teams watch and tick a checklist.**

That is the whole activity. Everything below is just the detail.

---

## WHAT YOU NEED OPEN IN FRONT OF YOU

- [ ] **This page** — everything you need is here, including the answers
- [ ] **`Huddle_Drill_Pack.md`** — Part 3 has the worked example you read aloud, Part 4 has the four cards
- [ ] **A timer you can see** — phone is fine
- [ ] **The four cards ready to paste** into chat, one per team

Trainees need their own copy of `Huddle_Drill_Pack.md`. Send it with the joining note.

---

## HOW MANY TEAMS DO YOU HAVE?

This decides your timing. Find your row before the day starts.

| Teams | Time you need | What to do |
|-------|--------------|-----------|
| **2–3** | 20 min | Fits the slot exactly. Nothing to change |
| **4** | 25 min | Start at 11:25. Take the 5 minutes from the SOC block at 9:45 |
| **5** | 30 min | Run 3 teams today, 2 first thing on Day 2. Do **not** cut to 2 minutes each |
| **6+** | — | Run 3 today. The rest on Day 2 morning. Note the names |

> **Never rush the huddles to fit.** A rushed huddle is not evidence you can sign for. It is better to run three properly and finish two tomorrow.

---

# THE FIVE PHASES

---

## PHASE 1 · 11:30 — You show them one · 3 minutes

They have never seen a huddle. If you send them straight in with no model, you get four rambling meetings and nobody learns anything.

**You have two ways to do this. Pick one now.**

### Option A — Read it aloud yourself *(recommended for your first time)*

**WHAT YOU DO:** Open `Huddle_Drill_Pack.md`, Part 3. Read the whole dialogue out loud, playing all four people. Change your voice slightly for each one, or just say the name before each line.

No volunteers. Nothing can go wrong. Takes 90 seconds.

**WHAT YOU SAY first:**

> "Before you run one, let me show you what one sounds like. I am going to read out a full huddle and play all four people. Listen for how short it is."

**WHAT YOU SAY after:**

> "That is it. Under three minutes.
>
> Four things I want you to notice.
>
> Ana opened with the priority, not with a greeting. No 'how is everyone doing.'
>
> Every single person spoke — including Ken, who had nothing open. 'Nothing open, here is what I am doing' is a real report. Silence is not.
>
> Ken repeated the watch item back before agreeing to it. That is the read-back rule from an hour ago, and nobody had to remind him.
>
> And Ana closed by naming who owns what. Not 'someone should look at Cebu.' **Ken** looks at Cebu."

### Option B — Run it live with volunteers

Pick three volunteers, you play Shift Lead. Use the scripts in Part 3. Feed people their lines if they freeze.

More engaging. Also more that can go wrong. Do this the second time you teach Day 1, not the first.

---

## PHASE 2 · 11:33 — Hand out the card · 2 minutes

**One card. Every team gets the same one.** It is in the Activity Pack, Part 4.

You may wonder whether later teams get an advantage from watching earlier ones. They do, a
little — and it does not matter. What you are assessing is **whether every member speaks, and
whether the team names a person for the watch item.** Not whether they solve a puzzle. A team
that has watched two other huddles usually runs a better one, which is rather the point.

**WHAT YOU SAY:**

> "Everybody has the same shift. It is Part 4 of your Activity Pack — open it now.
>
> Two minutes to read it. That is all the preparation you get. In a real shift you would have
> read the handover log and that is it."

---

## PHASE 3 · 11:35 — Tell the watchers what to do · 1 minute

This is the phase new instructors skip, and then the watching teams sit there doing nothing.

**WHAT YOU SAY:**

> "While one team runs their huddle, everybody else has a job.
>
> Open the Observation Checklist — it is Part 5 of your Drill Pack. Eight questions. You fill one in for the team you are watching, and it comes in with your afternoon pack. It is evidence, so put your name on it.
>
> The one I care about most is number two: **did every member speak?** That is what this unit is assessed on.
>
> Cameras on, everybody. Both the team running it and the teams watching."

---

## PHASE 4 · 11:36 — Run the teams · 4 minutes each

### How you start each team

**WHAT YOU SAY:**

> "Team [name], you are up. Shift Lead, open when you are ready. Four minutes starts now."

**WHAT YOU DO:** Start the timer. Say nothing during the huddle. Do not coach mid-huddle.

### What you are watching for

Only three things. Write them down as you go — you will not remember afterwards.

1. **Did every member speak?** Tick each name as they talk.
2. **Was the watch item given to a named person?**
3. **Was the priority clear at the end?**

### How you stop each team

**Stop them at four minutes even if they are mid-sentence.** That is part of the exercise, not rudeness.

**WHAT YOU SAY:**

> "Four minutes. Stop there."

### Between teams

Take **one** comment from the watching teams. One, not a discussion.

**WHAT YOU SAY:**

> "One observation from the watchers — someone who is not on that team. What did they do well, or what was missing?"

Then go straight to the next team. Save the real discussion for the debrief.

---

## PHASE 5 · Debrief · 4 minutes

**Do this once, at the end, for all teams together.**

### Question 1

**WHAT YOU SAY:**

> "Hands up — how many teams had every single member speak?"

Let them answer honestly. If a team did not, name it gently and move on: *"That is the one to fix. Everybody speaks, every time."*

### Question 2 — the teaching one

**WHAT YOU SAY:**

> "Now the important one. Each team — which item on **your** card should have been your top priority, and why that one?"

**WHAT YOU DO:** Let them argue for a moment before you confirm. The reasoning matters more than the answer. Then use the box below.

---

### ANSWERS — ALL FOUR CARDS

| Card | Top priority | Why | The trap |
|------|-------------|-----|----------|
| **A** | **5524** — 400 MB uploaded to a personal cloud account, not assessed | Possible data theft. Biggest unknown, biggest consequence | **5512** — Low, recurring 3 nights |
| **B** | **6115** — new admin account created at 02:14, not assessed | Attackers create accounts so they can come back. Admin-level and unexplained | **6103** — Low, recurring 4 nights |
| **C** | **7248** — 12 Finance users got the same attachment, nobody checked who opened it | Unknown blast radius across twelve people | **7233** — Low, recurring 5 nights |
| **D** | **8830** — admin account accessed from another country at 03:40 | Likely account compromise, at admin level | **8817** — Low, blocked, recurring 3 nights |

### Question 3 — the trap

**WHAT YOU SAY:**

> "And which item on your card is the trap — the one that is easy to keep ignoring?"

*(Answers in the right-hand column above.)*

### Then say the rule that covers every card

**WHAT YOU SAY:**

> "The pattern is the same on all four cards, and it is the same in the real job.
>
> **Your top priority is always the thing nobody has looked at yet that could be really bad.** Not the loudest item. Not the newest one. The biggest unknown with the biggest consequence.
>
> **And the trap is always the one marked Low that keeps coming back.** Low and repeated is easy to keep ignoring. But 'it happened again' is a pattern, and a pattern deserves ten minutes of somebody's attention."

### Two bonus points — only if a team spots them

**Card B:** the client note asks who accessed the payroll folder, and the new admin account is on the HR server. Those may be the same story.

**Card D:** the client asked yesterday who has admin access to their cloud account, and last night an admin account logged in from abroad. Nobody connected them.

**WHAT YOU SAY if someone spots either:**

> "Stop — say that again for everyone. [Name] just connected the client's question to an alert. That is exactly the Level One skill. It is the same move as the analyst in the shift timeline who linked a phone call at 22:15 to an alert at 22:20. No tool does that. A person does."

### Close the activity

**WHAT YOU SAY:**

> "Some of those were rough, and they were supposed to be. You met these people ninety minutes ago.
>
> Here is what I want you to take away. The teams that worked were the ones where the Shift Lead named a person for the watch item. The teams that drifted were the ones where it stayed as 'somebody should check that.'
>
> **Somebody is not a person. Nobody is called Somebody.**
>
> Hand your observation checklists in with your afternoon pack."

---

## IF IT GOES WRONG

| What happens | What you do |
|---|---|
| **A team member says nothing at all** | Stop the huddle. *"[Name], we have not heard from you — what is on your list?"* Do not let it slide. You cannot record what did not happen |
| **A team finishes in 90 seconds** | Ask the watchers: *"What did they not cover?"* Usually the watch item or the client note. Send them back for one more minute |
| **A team runs over four minutes** | Stop at four. *"That is the lesson. Four minutes goes fast, which is why the Shift Lead opens with priorities and not with a story"* |
| **A team picks the trap as top priority** | Do not just correct them. Ask: *"What is the worst thing that happens if you are wrong about the Low one? Now what is the worst thing if you are wrong about the unassessed one?"* They get there themselves |
| **Nobody volunteers an observation between teams** | Call a name. *"[Name], you were watching — one thing."* |
| **A Shift Lead freezes** | Point them at Part 6 of their Drill Pack. It has four lines they can read straight off the page. Say: *"Read the opener from Part 6, it is written out for you."* |
| **Cameras off in the watching teams** | Ask by name. This is one of two moments today where it genuinely matters |
| **You forget to start the timer** | Estimate and move on. Nobody will know. Start it for the next team |
| **You run out of time** | Stop cleanly. Note which teams have not gone and run them first thing on Day 2. Do not squeeze four teams into ten minutes |

---

## HOW YOU KNOW IT WORKED

Three things. If you have all three, you are done and you have your evidence.

1. **Every trainee in every team said at least one sentence.**
2. **You can name who took the watch item in each team.**
3. **You collected an observation checklist from every trainee.**

That is it. The huddles themselves being messy is completely fine — first attempt, strangers, ninety minutes in.

---

---

# APPENDIX — NOT FOR DAY 1
## The SOP and Change Notice walkthrough — use this on **Day 2**

**Do not deliver this today.** Trainees meet the SOP and the change notice on their own this afternoon, as Tasks 5 and 6 of the Self-Study Pack. That cold attempt is the point of the exercise.

This script is written to be walked through **after** they have already tried it. Use it at the start of Day 2, when they arrive with their marked-up copies and their answers.

If you teach it today, you give away the answer to Task 5 question one, and you lose the best twenty minutes of the week.

---

### The Alert Intake SOP

```
ALERT INTAKE SOP — SOP-SOC-001 rev 4

1.  On receipt of a detection alert, the analyst SHALL record the alert
    ID, source system, timestamp, and affected host within 5 minutes.

2.  The analyst SHALL assess the alert against the Severity Matrix
    (SOP-SOC-002) before any other action.

3.  Where the alert is assessed as Critical or High, the analyst MUST
    notify the client contact within 15 minutes of assessment.

4.  The analyst SHOULD check for a matching Change Notice before
    escalating. Where a Change Notice explains the alert, the analyst
    SHALL record the change reference and close the alert as expected
    activity.

5.  The analyst MAY close an alert assessed as Low without escalation,
    provided the assessment is documented.

6.  The analyst SHALL NOT take containment action on any host.
    Containment is authorised by the SOC Manager only.
```

**Questions to ask, step by step:**

1. **Step 1** — "What exactly is required, and what is the clock?" *(Four fields. Five minutes from receipt.)*
2. **Step 2** — "What must happen before anything else?" *(Severity assessment. Not investigation, not a phone call.)*
3. **Step 3** — "What is the deadline, and when does it start?" *(15 minutes from **assessment**, not from receipt. **This is the one everybody gets wrong.** Spend time here.)*
4. **Step 4** — "'Should' check, then 'shall' record. What is the difference?" *(You are expected to check; if you do not, justify it. If a change explains it, recording is mandatory.)*
5. **Step 5** — "What does 'may' give you?" *(Discretion — but only with documentation.)*
6. **Step 6** — "What does this remove from you?" *(Authority to contain. The boundary of the L1 role, written down.)*

---

### A Vendor Advisory

```
ADVISORY 2026-0418 — Endpoint Agent 7.4.2 Signature Regression

A signature regression in Endpoint Agent 7.4.2 may cause false
positive detections identified as "Trojan.Generic.Heur" on signed
Microsoft binaries, including powershell.exe and wmiprvse.exe.

Affected versions: 7.4.2 only.
Fixed in: 7.4.3, released 2026-04-19.

Recommended action: update to 7.4.3. Until updated, treat
Trojan.Generic.Heur detections on signed Microsoft binaries as
suspected false positives and verify manually before escalating.
```

**Ask:**
- "What changed for your queue **tonight**?" *(A specific detection name on specific files is now suspect.)*
- "Does this mean ignore those alerts?" *(**No.** It means verify manually before escalating — a completely different instruction.)*
- "What happens if you never read this?" *(You escalate a wave of false positives and waste your L2's night.)*

---

### A Change Notice

```
CHANGE NOTICE CHG-2026-1177

System:     Manila file server cluster (SRV-MNL-01 .. SRV-MNL-04)
Window:     2026-04-22, 22:00 – 03:00
Change:     Quarterly OS patching and reboot cycle
Impact:     Hosts will reboot. Agent will report offline during reboot.
            Elevated process creation and service restart activity is
            expected throughout the window.
Requester:  IT Infrastructure
Approver:   Change Advisory Board
```

**Ask:**
- "It is 23:30 and four servers just went offline in your console. Incident or not?" *(**Not** — CHG-2026-1177 covers it.)*
- "It is 23:30 and **SRV-CEB-02** went offline. Incident or not?" *(**Yes** — Cebu is not in the change window. A notice tells you what it does *not* cover just as clearly as what it does.)*
- "What do you record on the alert?" *(The change reference, CHG-2026-1177 — per SOP step 4.)*

> **Say:** "This is the single most useful habit you can build in your first month. Before you escalate anything, ask: is there a change notice for this? It will save you and your L2 an enormous amount of wasted work.

---

# ANSWER KEY — WHAT THE TRAINEES HANDED IN

They completed **Task 5** (SOP markup) and **Task 6** (notice triage) on their own on Day 1
afternoon. These are the answers to what they actually wrote. Have this open when you debrief.

---

## TASK 5 — THE SOP MARKUP TABLE

| Step | Binding word | What it requires | Clock? |
|------|-------------|-----------------|--------|
| 3.1 | **SHALL** | Record four fields: alert ID, source system, timestamp, affected host | **Yes** — 5 min from receipt |
| 3.2 | **SHALL** | Assess against the Severity Matrix **before any other action** | No — but it is a sequence lock |
| 3.3 | **MUST** | Notify the client for Critical or High | **Yes** — 15 min from **assessment** |
| 3.4 | SHOULD check / **SHALL** record | Check for a Change Notice. If one explains the alert, recording the reference is mandatory | No |
| 3.5 | **MAY** | Discretion to close a Low — **provided it is documented** | No |
| 3.6 | **SHALL NOT** | No containment authority at all | No |
| 3.7 | **SHALL** | Record every action, its time, and who authorised it | No |
| 3.8 | **SHALL** | Complete a handover log at end of shift | Yes — end of shift |

---

## TASK 5 — THE FOUR QUESTIONS

### Q1. An alert arrives at 22:00. You assess it as High at 22:20. What is your notification deadline, and why?

> ## ANSWER: **22:35**

The clock in §3.3 runs from **assessment**, not from receipt. Assessment was 22:20, plus
15 minutes, equals 22:35.

They were already late on §3.1 — that required recording within 5 minutes of receipt, so by
22:05. **But being late on 3.1 does not move the 3.3 deadline.** Two separate clocks.

> **This is the one most of the class gets wrong**, and the usual wrong answer is 22:15 —
> they start the clock at receipt. Spend real time here. Ask: *"Read 3.3 out loud. What word
> comes immediately before the words 'the analyst must notify'?"*
>
> It is also the single most common cause of missed SLAs in real operations, so say that.
> It makes the pedantry feel worth it.

### Q2. You assess an alert as Low and close it without writing anything down. Which step did you breach, and what exactly was missing?

> ## ANSWER: **Step 3.5.** The missing thing is the **documented assessment**.

"May close" is conditional on "provided the assessment is documented." The permission and the
condition are in the same sentence.

**Undocumented discretion is not discretion.** If you cannot show the reasoning, you did not
exercise judgement — you just closed a ticket.

### Q3. A client phones you directly and asks you to disconnect an infected laptop from the network. What do you do, and which step tells you that?

> ## ANSWER: **Refuse and escalate. Step 3.6.**

The words to use:

> *"I do not have the authority to do that. I am escalating this to the SOC Manager now and
> they will call you back."*

Then escalate immediately — not just say it to end the call.

> **Watch for the trainees who wanted to say yes.** That instinct is good and it needs
> redirecting, not crushing. Say so out loud: *"Wanting to help is right. Doing it yourself
> is the part that is wrong."*

### Q4. A Change Notice explains an alert, so you close it. What must you record before you do, and which step makes it mandatory?

> ## ANSWER: **The change reference.** Step 3.4 makes it **shall**, not should.

The trap in 3.4 is that it contains both words. Checking for a notice is **should**.
Recording the reference once you have found one is **shall**.

---

## TASK 6 — THE THREE SCENARIO QUESTIONS

### A. It is 23:30 on 22 April. `SRV-MNL-01` through `SRV-MNL-04` just went offline. Incident or not?

> ## ANSWER: **Not an incident.**

CHG-2026-1177 covers exactly those four hosts, in exactly that window (22:00–03:00 on
22 April). Record the change reference and close it as expected activity.

### B. Same night, same time. `SRV-CEB-02` goes offline. Incident or not?

> ## ANSWER: **Incident.**

Cebu is not in the change notice. The notice lists Manila hosts only.

> **This is the whole point of the exercise.** A notice tells you what it does **not** cover
> just as clearly as what it does. Ask the class: *"How many of you saw 'servers going
> offline is expected tonight' and applied that to all servers?"* Several hands will go up,
> and that is the lesson.

### C. The Northwind SLA notice tells you to do something different from SOP-SOC-001 §3.3. Which do you follow?

> ## ANSWER: **Follow the Northwind notice.**

It explicitly says *"This supersedes… FOR THIS CLIENT ONLY."* **A document that has the
authority to override says so.** That sentence is the answer.

> **This is the best twenty minutes available in the whole debrief.**
>
> The correct behaviour when two documents conflict is **not** to pick the stricter one, or
> the newer one, or the one you prefer. It is to check whether the notice **has the authority
> to override** — and if you cannot tell, to ask.
>
> Anyone who answered "follow the stricter one" reasoned sensibly and still got it wrong.
> **Those are the most useful people to hear from.** Ask one of them to explain their
> thinking to the class before you give the answer. It is a far better lesson coming from a
> trainee than from you.

---

## HOW TO MARK TASKS 5 AND 6

Mark for **reasoning, not neatness**. These were cold attempts after one morning of
instruction.

What you are looking for:

- Did they find the binding verbs? *(Task 5 table)*
- Did they notice the boundary — what a notice does **not** cover? *(Task 6, question B)*
- Did they refuse the containment request? *(Task 5, Q3)*

Give **Attempted / Developing / Solid** rather than a score. LO2 is assessed properly across
Days 1–3. Nothing here is a final competency judgement.

"
