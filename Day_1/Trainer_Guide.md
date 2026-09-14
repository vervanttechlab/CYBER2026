# DAY 1 — TRAINER GUIDE
## Orientation and the Watch-Desk Voice
### Mode: HYBRID — ONLINE SYNCHRONOUS (8:00 AM – 12:00 PM) | FULL ASYNCHRONOUS (1:00 – 5:00 PM)

---

## HOW DAY 1 IS SPLIT, AND WHY IT SPLITS THERE

Day 1 carries two assessable units. They do not have the same delivery requirements, and that is what decides the split.

| Unit | Element | Needs live delivery? | Where it sits |
|------|---------|---------------------|---------------|
| **400311101** | **LO1** — Follow routine **spoken** messages | ✅ **Yes.** The candidate must receive verbal instructions, record them, and seek clarification while you watch | **Morning — synchronous** |
| **400311102** | **LO1 & LO2** — Work with others | ✅ **Yes.** Requires observed participation in a work group | **Morning — synchronous** |
| **400311107** | (induction only) | ⚠️ Ergonomics and the audit can be done on camera | **Morning — synchronous**, lab-specific items deferred |
| **400311108** | (induction only) | ⚠️ Principles can be taught live; the lab pledge cannot be signed remotely | **Morning — synchronous**, pledge deferred |
| **400311101** | **LO2** — Perform duties following **written** notices | ❌ **No.** Entirely document-based | **Afternoon — asynchronous** |

> **The rule that drives everything below:** anything an assessor has to *watch* happens in the morning while everyone is on the call. Anything that is a person alone with a document happens in the afternoon, when they are not.

### The two documents that cannot be signed today

The **Lab OSH Checklist** and the **Green Lab Pledge** apply to the training lab itself. Nobody is in it today. Do not send them out and do not accept a remote signature — the evidence would be false.

- Teach both **topics** live this morning (ergonomics, lab rules, the scanning boundary, energy and e-waste practice)
- Collect the **Home Workstation Audit** this morning instead — it is real evidence against 400311107 and it is honest, because they really are at that desk
- **Both lab documents are signed on the first on-site day.** Put that in your delivery record now so it does not get lost. Day 3 delivers 400311107 and 400311108 in full and is the natural place for it if Day 3 is on site.

---

## UNITS OF COMPETENCY COVERED TODAY

| Code | Unit of Competency | Elements Touched |
|------|-------------------|------------------|
| 400311101 | Receive and respond to workplace communication | LO1 Follow routine spoken messages *(AM, live)*; LO2 Perform workplace duties following written notices *(PM, async)* |
| 400311102 | Work with others | LO1 Develop effective workplace relationships; LO2 Contribute to work group activities *(AM, live)* |
| 400311107 | Follow OSH policies and procedures | *Induction only — home workstation audit today; lab checklist on the first on-site day; full unit on Day 3* |
| 400311108 | Apply environmental work standards | *Induction only — principles today; lab pledge signed on the first on-site day; full unit on Day 3* |

---

## BEFORE CLASS CHECKLIST

### The platform (do this the day before, not at 7:55)
- [ ] Meeting link created, **breakout rooms enabled**, and the link sent with the joining note
- [ ] You have tested screen share, and the text on your shared screen is readable at 100% zoom
- [ ] **Recording is configured and you know how to start it** — see the consent note below
- [ ] A digital whiteboard is open and shared, or a slide you can annotate live
- [ ] You have a second device logged in as a trainee, so you can see what they see
- [ ] Waiting room off, or someone assigned to admit late joiners so you are not the doorkeeper

### Recording and consent
- [ ] Announce at the start that the session is recorded, and why — the huddle and read-back drills are observed evidence
- [ ] Anyone who objects to being recorded is accommodated: they run their drill with camera on but recording paused, and you sign the observation checklist yourself in real time
- [ ] Store recordings where only you can reach them, and delete on the schedule your institution requires

### The afternoon pack (must go out BEFORE the morning session ends)
- [ ] `Self_Study_Pack` — the afternoon instruction sheet, everything else hangs off it
- [ ] `SOP_Pack` — needed for the two big afternoon tasks, and every day after
- [ ] `Student_Handout` — the afternoon reading
- [ ] `Home_Workstation_Audit` — used **live this morning**, so send it with the joining note
- [ ] `Sample_Alert_Log.csv`
- [ ] The pre-test link
- [ ] Submission method confirmed and stated in writing — folder, email, or LMS upload

> **Trainer Tip:** Send the Home Workstation Audit with the joining note, not at 9:15. If a trainee has to hunt for an attachment mid-session you lose four minutes of a thirty-minute block, and you lose it from the induction — the block you can least afford to rush.

### The server box (nothing today needs it — test it anyway)
- [ ] VirtualBox is installed and the **Wazuh OVA is imported and boots**
- [ ] The Wazuh VM network adapter is set to **Bridged**, not NAT
- [ ] The default `admin` dashboard password has been **changed** — never demo with `admin/admin`

> **Trainer Tip:** Today is the only day you do not need the Wazuh server. But test it today anyway — if it is broken you have until Day 6 to fix it, and that is a comfortable margin. Discovering it on Day 6 morning is not.

### Your own machine
- [ ] A blank `Shift_Handover_Log` template ready to share on screen **and** already sent to trainees, because they fill one in during the afternoon
- [ ] The Demo 1 handover script printed on paper next to you — do not read it off the shared screen where they can see it
- [ ] A timer visible to the class for the huddle drill

---

# MORNING — ONLINE SYNCHRONOUS (8:00 AM – 12:00 PM)

## MORNING RUNNING ORDER

| Time | Session | Minutes |
|------|---------|---------|
| 8:00 – 8:15 | Join, tech check, welcome | 15 |
| 8:15 – 8:35 | Programme orientation and how this hybrid day runs | 20 |
| 8:35 – 9:00 | Icebreaker: "The incident you already survived" | 25 |
| 9:00 – 9:15 | Team formation and breakout assignment | 15 |
| 9:15 – 9:45 | OSH and environmental induction, delivered remotely | 30 |
| 9:45 – 10:15 | Inside a Security Operations Centre | 30 |
| 10:15 – 10:25 | Break | 10 |
| 10:25 – 11:30 | **Follow routine spoken messages — LO1, the whole block** | 65 |
| 11:30 – 11:50 | **Work with others — the shift huddle drill** | 20 |
| 11:50 – 12:00 | Hand off to the afternoon | 10 |

> **The morning has no slack in it.** Every minute you overrun comes out of the read-back drill or the huddle, and those are the two things you cannot deliver any other way. If you are behind at 10:15, cut the SOC block short — the trainees read that material this afternoon anyway.

---

## 8:00 – 8:15 AM | JOIN, TECH CHECK, WELCOME (15 min)

### Steps:
1. Open the room at **7:45**. Trainees join to a shared slide that says what to check.
2. As people arrive, have each one confirm in the chat: **audio works, camera works, they can see your shared screen.** Do not start until you have that from everyone.
3. State the recording announcement and the reason for it.
4. Set the three ground rules for the morning and leave them on screen:
   - **Cameras on for the drills.** Not for the lectures — for the read-back drill and the huddle. Those are observed evidence, and an assessor cannot observe a black square.
   - **Mic muted unless speaking**, but unmute to ask — do not make people type questions.
   - **Say your name before you speak.** For fifteen days. It is how a real bridge call runs.

### What to Say:
> "Good morning, everyone. Welcome to Cyber Threat Monitoring Level One. My name is [Your Name] and I will be your trainer for the next fifteen days. In fifteen days you will not become a hacker, and you will not become a security engineer. You will become something the industry is short of and hiring for right now: a Level One analyst — the person who watches the alerts, decides which ones are real, and gets the right people out of bed at two in the morning."

> **Trainer Tip:** The "say your name before you speak" rule sounds like an online-meeting nicety. It is not. On a real incident bridge call nobody can see who is talking either, and analysts who do not identify themselves cause exactly the kind of confusion this course spends fifteen days training out of them. Say that when you set the rule — it lands much better as a job skill than as an etiquette request.

---

## 8:15 – 8:35 AM | PROGRAMME ORIENTATION AND HOW THIS HYBRID DAY RUNS (20 min)

### Steps:
1. Put the qualification on the shared screen and walk through it:

| | |
|---|---|
| **Qualification** | Cyber Threat Monitoring Level I |
| **Sector** | Information and Communications Technology (ICT) |
| **Core Unit 1** | `CS-ICT251101` Monitor and report cyber threats |
| **Core Unit 2** | `CS-ICT251102` Conduct vulnerability scanning of assets |
| **Job roles you can hold** | Cybersecurity Analyst (L1), Cybersecurity Support Staff, Cybersecurity Help Desk Staff |

2. Walk through the fifteen days:
   - **Phase A (Days 1–3):** Workplace foundation — communication, teamwork, problem solving, safety, information handling, quality
   - **Phase B (Days 4–10):** Monitor and report cyber threats — the whole alert lifecycle
   - **Phase C (Days 11–14):** Conduct vulnerability scanning — schedule, scan, report
   - **Phase D (Day 15):** Portfolio and a full mock national assessment

3. Explain **competency-based training** — the part trainees most often misunderstand:
   > "This is not a course where you pass by getting seventy percent on a test. This is competency-based. You are either **Competent** or **Not Yet Competent** on each unit. 'Not Yet Competent' is not a failure — it means you get more practice and you try again. Nobody is graded on a curve here. Everybody can be competent."

4. Explain the **evidence portfolio**:
   > "Almost every day you will produce something — a signed log, a completed worksheet, a ticket, a report. Keep every single one. On Day Fifteen we assemble them into your portfolio, and that portfolio is what an assessor looks at. If you lose your paperwork, you lose your evidence."

5. **Explain today's shape explicitly.** Put this on screen and leave it up for a minute:

   > "Today runs in two halves, and they work differently.
   >
   > **This morning we are all here together, and that is deliberate.** Everything we do before lunch is something that only works with other people present — receiving a spoken briefing, reading an instruction back to the person who gave it, running a shift huddle with your team. An assessor has to see you do those. So we do them now.
   >
   > **This afternoon you work alone, and that is also deliberate.** From one o'clock you have four hours and a pack of documents. Reading an SOP correctly, working out whether a change notice explains an alert — that is solitary work in the real job too. You do not read a procedure in a huddle.
   >
   > The afternoon is **not** optional and it is **not** a half day. It produces evidence that goes in your portfolio, it is marked, and we will not repeat it in class. If you skip it you arrive on Day Two missing a unit element."

6. Confirm the practical details on screen: submission method, deadline for the afternoon pack, and how to reach you during the afternoon.

> **Trainer Tip:** Say the phrase "the afternoon is not a half day" out loud. Every hybrid cohort contains people who will hear "asynchronous" as "free". Naming it in the first twenty minutes, in front of everyone, costs you thirty seconds and saves the conversation you would otherwise have on Day 2 with three people who did nothing.

---

## 8:35 – 9:00 AM | ICEBREAKER: "THE INCIDENT YOU ALREADY SURVIVED" (25 min)

### What to Say:
> "Everybody on this call has already been on the receiving end of a cyber incident, even if you did not call it that. Let us start there."

### Steps:
1. Model it first with your own example:
   > "I will go first. My mother got a text saying her bank account was locked and she needed to click a link. She clicked it. That is a phishing attack, and it worked. What alerted us was that her phone started sending the same message to everyone in her contacts."

2. Go around the call — **call names in a fixed order and show the order on screen**, so nobody is caught out and nobody talks over anybody. Each trainee gives their **name** and **one security thing that has happened to them or someone they know** — a phishing text, a hacked Facebook account, a ransomware note at a former job, a stolen phone, an SMS scam, a GCash scam.

3. Keep the tally on a shared whiteboard or an annotated slide as they speak:

| Incident type | Tally | How they found out |
|--------------|-------|-------------------|
| Phishing SMS / email | | |
| Account takeover | | |
| Malware / virus | | |
| Ransomware | | |
| Scam call | | |
| Lost / stolen device | | |

4. When everyone has spoken, point at the third column and say:
   > "Look at the column on the right. Almost nobody said 'a security system told me.' You found out because something looked wrong, or somebody told you. That is exactly the job you are training for. A Level One analyst is the person who notices, and the person people tell. The tools help. But the noticing is the job."

5. Circle the two most common incident types and say:
   > "By Day Ten you will be able to detect both of those on a real system, write them up, and escalate them to the right manager. Fifteen days."

> **Trainer Tip:** Online, this round drifts long — people cannot read the room to know when to stop. Give a hard limit up front: **"name, the incident, and how you found out. Three sentences."** Hold the first two speakers to it and the rest will follow.

---

## 9:00 – 9:15 AM | TEAM FORMATION AND BREAKOUT ASSIGNMENT (15 min)

> **Do this before the drills, not after.** Online, teams have to exist as breakout rooms before you can use them, and building rooms mid-session burns time you do not have.

### Steps:
1. Divide the class into teams of 3–4. **Mix deliberately** — put the person who has never used a command line with the person who runs a home server. Use the icebreaker answers you just heard to do it.
2. Announce the teams on screen and **create the breakout rooms now**. They stay the same all morning and for the next three days.
3. Each team gets 5 minutes in their room to:
   - Pick a **team name** — SOC teams traditionally use shift names or colours: Blue Watch, Night Shift, Team Sentinel
   - Assign roles, which **rotate every three days** so everyone practises every role:

| Role | Responsibility |
|------|---------------|
| **Shift Lead** | Runs the team, makes the call when the team disagrees, owns the handover |
| **Scribe** | Keeps the team's log and worksheets, ensures evidence is filed |
| **Presenter** | Speaks for the team in class debriefs |
| **Timekeeper** | Watches the clock during timed drills — critical from Day 6 onward |

4. Back in the main room, each team posts **name and roles in the chat**. Save the chat log — that is your team formation record, and it is competency evidence.
5. Have each team exchange contact details inside their room before they leave it. They will need each other this afternoon.

> **Say:** "These are your teams. In a real SOC you do not choose your shift-mates, and you still have to hand over cleanly to them at five in the morning. Same rule here."

---

## 9:15 – 9:45 AM | OSH AND ENVIRONMENTAL INDUCTION, DELIVERED REMOTELY (30 min)

> **Note to trainer:** This is safety **induction**, not the full OSH unit. Units 400311107 and 400311108 are delivered properly on Day 3. Today produces **one** evidence document — the Home Workstation Audit. The Lab OSH Checklist and the Green Lab Pledge are signed on the first on-site day, because they describe a lab nobody is sitting in.

### Part A: Ergonomics, live on camera (12 min)

**Demonstrate each at your own desk on camera, then have trainees adjust theirs while you watch. This part works better remotely than it does in a lab — they are adjusting the actual desk they will use for fifteen days.**

1. **Chair height** — feet flat on the floor, thighs parallel to the ground
   > "If your feet dangle, your lower back takes the load. Eight hours a day for a year and you will feel it."
2. **Monitor** — top of the screen at eye level, about an arm's length away
   > "Laptop users: your screen is too low, always. A stack of books and a separate keyboard fixes it for nothing."
3. **Keyboard and mouse** — elbows at about 90 degrees, wrists straight, mouse close to the keyboard
4. **Lighting** — no window directly behind the screen, no lamp directly behind you on camera
5. **The 20-20-20 rule** — every 20 minutes, look at something 20 feet away for 20 seconds
   > "Analysts stare at screens all day. This is the single cheapest thing you can do for your eyes, and I will remind you all fifteen days."

Ask three or four trainees to tilt their camera to show their setup. Coach on air. It is quick, it is concrete, and the rest of the class learns from watching you correct someone.

### Part B: Home Workstation Audit — completed live (12 min)
1. Trainees open the **Home Workstation Audit** you sent with the joining note
2. They complete it **now, on the call**, for the desk they are sitting at
3. Be explicit about honesty:
   > "Failing items are the point. A sheet of twenty passes and no notes tells me you did not really look. I am not marking your furniture. I am marking whether you can run a safety check honestly, which is the actual competency."
4. Any FAIL gets an action written next to it — fix it now if it is fixable, note it if it is not
5. Trainees sign and submit it with the afternoon pack
6. **This is competency evidence for 400311107.**

### Part C: Lab rules and the scanning boundary (6 min)
1. State the lab rules that will apply from the first on-site day, and put them on the shared screen:
   - No food or drinks at the workstations
   - No installing software that is not part of the course
   - **No scanning, probing, or testing anything outside the lab network** — this one is not negotiable, and you will repeat it on Days 11–13
   - Report damaged cables or equipment; do not fix them yourself
2. Draw the lab network: the switch, the trainee machines, the server box, and a big circle around all of it labelled **"everything inside this circle is ours; everything outside it is not."**
3. Cover the environmental practice briefly — paperless working, monitors off at lunch, proper shutdown, e-waste handling, no printing evidence you can store digitally:
   > "A security lab is an energy-hungry place. Machines run all day. Servers run all night. Old equipment gets replaced and thrown away with batteries and heavy metals in it. That is what this unit is about."
4. **Say plainly what is deferred:**
   > "There are two documents you would normally sign on Day One — the Lab OSH Checklist and the Green Lab Pledge. Both of them describe the training lab, and none of us is in it. You will sign both on our first day on site. I have recorded that they are outstanding, so nobody has to remember it."

> **Trainer Tip:** Do not be tempted to send the Green Lab Pledge out for a remote signature to keep the paperwork tidy. It is a pledge about a room they have never entered. An assessor who notices will be right to, and you will have taught the cohort on Day 1 that signing a document you have not verified is acceptable — which is precisely the habit this qualification exists to prevent.

---

## 9:45 – 10:15 AM | INSIDE A SECURITY OPERATIONS CENTRE (30 min)

> **This block is compressed, deliberately.** The full detail — the sensor list, the shift hour-by-hour, the RACI grid — is in the Student Handout, which they read this afternoon. Teach the shape here. Let the handout carry the detail.

### Part A: The Alert Pipeline (15 min)

**Draw this on the shared whiteboard as you talk — draw it, do not show a finished slide:**

```
            THE ALERT PIPELINE

  SENSORS          →   SIEM        →   ANALYST   →   ACTION
  (AV, firewall,       (collects,      (you)         (ticket,
   EDR, WAF,            correlates,                   escalate,
   DLP, NDR)            ranks)                        notify)
```

1. **Sensors** — the things that watch. Antivirus on the endpoint. The firewall at the edge. EDR watching process behaviour. A WAF in front of the website. DLP watching data leaving. Each one sees a slice.
2. **SIEM** — Security Information and Event Management. It collects everything the sensors say, puts it in one place, and ranks it.
   > "Without a SIEM you have ten tools each shouting in a different room. With a SIEM you have one room."
3. **Analyst** — you. The SIEM says 'this looks interesting.' You decide whether it is real.
4. **Action** — a ticket, an escalation, a phone call to a client at 2 AM.

### Part B: The Tiers (15 min)

| Tier | Who they are | What they do | Typical response |
|------|-------------|-------------|-----------------|
| **L1** | **You, after this course** | Watch the queue, triage alerts, verify, ticket, escalate | "This is real. Escalating." |
| **L2** | Investigator | Digs into what L1 escalated, scopes the incident | "It spread to four machines. Containing." |
| **L3** | Threat hunter / IR | Hunts for what nobody alerted on, leads major incidents | "This is a targeted campaign." |
| **SOC Manager** | Runs the desk | Staffing, SLAs, client communication | "Who has the bridge call?" |

> **Say:** "Notice what L1 does *not* do. You do not decide to disconnect a company from the internet. You do not rebuild a server. You do not talk to the press. Knowing the edge of your authority is a competency, and assessors test for it."

**Then set up this afternoon's reading in one sentence:**
> "The handout you read this afternoon walks you through a real eight-hour shift, hour by hour, and shows you exactly who owns an alert at each stage. Read it. The thing to watch for is the moment the analyst does the single most valuable thing anybody did all night — and no tool did it. A person did."

---

## 10:15 – 10:25 AM | BREAK (10 min)

> "Ten minutes. Stand up, walk, look at something far away. Back at twenty-five past, cameras on — the next block is the one you cannot do on your own."

---

## 10:25 – 11:30 AM | FOLLOW ROUTINE SPOKEN MESSAGES (65 min)
### Unit 400311101 — LO1 · **This is the block the morning exists for**

> **Protect this block.** If the morning has slipped, take the time from the SOC block, not from here. This element cannot be delivered asynchronously and cannot be caught up later without reconvening the whole cohort.

### Part A: Why Listening Is a Technical Skill (8 min)

### What to Say:
> "In security, the most expensive mistakes are communication mistakes. An analyst who mishears a hostname escalates the wrong machine. An analyst who does not ask a clarifying question spends four hours investigating the wrong thing. Listening precisely is not a soft skill in this job. It is a technical control. And on a call like this one — where you cannot see the speaker's face and the audio drops out — it is harder, which is exactly why we are practising it here."

**Put the four performance criteria on screen and keep them there all block:**

1. Required information is gathered by **listening attentively** and correctly interpreting instructions
2. Instructions are **recorded** in accordance with workplace requirements
3. Instructions are **acted upon immediately** in accordance with information received
4. **Clarification is sought** from the workplace supervisor whenever any instruction is not clear

### Part B: The Shift Handover Briefing (20 min)

1. Explain the handover:
   > "Every shift begins and ends with a handover. It is the highest-risk moment in a SOC, because information gets dropped. There is a standard shape to it, and you are going to learn it."

2. Put the **handover structure** on screen:

| Section | What goes in it |
|---------|----------------|
| **Open items** | Tickets still in progress, with ticket number and current state |
| **Escalated** | What went to L2/L3 and who owns it now |
| **Watch items** | Things that are not yet incidents but need eyes |
| **System status** | Anything down, degraded, or in maintenance |
| **Client notes** | Anything a client asked for or complained about |

3. **Demonstrate: deliver a 90-second spoken handover from the prepared script** (see Demonstration Steps, Demo 1). Speak at normal pace. Do not slow down for them.

   > **Stop sharing your screen before you start.** They must take this down by ear. If your slide is still up they will copy the structure off it instead of listening, and you will have tested nothing.

4. Trainees take notes as you speak — **no handout, no slides, no chat.**
5. Ask three trainees to unmute and read back what they wrote. Compare against your script.
   > "Notice the differences. Nobody got everything. That is why we write it down and that is why we read it back."

> **Trainer Tip:** Deliver the briefing **twice** if the class is large, and the second time tell them in advance you are going to repeat it. The gap between attempt one and attempt two is the most instructive thing in the block — they discover for themselves what they were not listening for.

### Part C: Recording and Read-Back (17 min)

1. Teach the **read-back rule**, borrowed from aviation and medicine:
   > "When you receive an instruction that matters, you repeat it back in your own words before you act on it. 'So you want me to isolate WKS-042, not WKS-024, and notify the IT manager. Confirming.' It takes four seconds and it catches almost every mishearing."

2. **Practise in breakout rooms, in pairs.** Send teams to their rooms with the instruction card list. One gives an instruction, the other reads it back. Swap. Ten rounds. **8 minutes.**
3. Drop into each room for a minute. You are listening for one thing: does the receiver repeat the *identifier* — the hostname, the ticket number, the IP — or does the read-back skip it?
4. Back in the main room, introduce the **Shift Handover Log** template on screen and walk through where each of the five sections goes.
   > "You fill one of these in this afternoon, from the handover I just gave you. Task 3 in your pack. Do it from your notes, not from a recording."

### Part D: Escalation Calls and Clarifying Questions (20 min)

1. Explain when to seek clarification:
   > "Three situations mean stop and ask: you do not understand the instruction, the instruction contradicts the SOP, or acting on it would exceed your authority. In all three, asking is not weakness. Not asking is the error."

2. Teach the four clarifying questions an L1 always has available:
   - "Can you repeat the hostname / IP / ticket number?"
   - "Do you want me to do that now, or after I finish the current ticket?"
   - "That is above my authority — should I escalate it, or are you authorising it?"
   - "The SOP says X and you are asking for Y. Which do you want me to follow?"

3. **Role-play drill, in the main room so everyone observes.** You play an agitated shift supervisor giving a fast, partially unclear instruction. The trainee must record it, read it back, and ask at least one clarifying question. Run **6–8 trainees at roughly 90 seconds each.** Class critiques between rounds — one observation each, no piling on.

> **Trainer Tip:** Deliberately mumble one hostname each time. The trainees who ask you to repeat it are demonstrating the competency. The ones who guess are demonstrating the failure mode. Name both, kindly. Online this drill is *better* than it is in a room — the audio is genuinely imperfect, so "I could not hear that clearly, can you repeat the hostname" is a real request rather than a piece of theatre.

> **Record who you ran.** If you only got through six trainees, note the names of the rest and run them at the start of Day 2. Do not let a trainee reach Day 15 without having done this once under observation.

---

## 11:30 – 11:50 AM | WORK WITH OTHERS — THE SHIFT HUDDLE DRILL (20 min)
### Unit 400311102 — LO1 and LO2

> The RACI grid — who is Responsible, Accountable, Consulted and Informed at each stage of an alert — is in the Student Handout and is read this afternoon. Do not teach it here. Make the one point that matters and run the drill.

### Part A: The edge of your authority (3 min)

> **Say:** "One thing before the drill, and it is the thing an assessor will ask you about. On a single alert you are **Responsible** for the triage and for the ticket. You are never **Accountable** for a containment decision — that belongs to the SOC Manager. If somebody asks you to make one, that is your cue to escalate, not to be brave. The full grid is in your handout this afternoon."

### Part B: The Huddle Drill (17 min)

1. Explain the huddle:
   > "A huddle is a five-minute stand-up at the start of a shift. Everyone speaks. Nobody drifts. In an office everybody stands up, and that is what keeps it to five minutes — on a call, the timer does that job instead."

2. Give each team a **huddle scenario card** with three open tickets and one watch item. Post the cards in the chat, one per team, or drop them into the breakout rooms.

3. **Run the huddles sequentially in the main room**, timed to **exactly 4 minutes** each, with everyone else observing:
   - Shift Lead opens and states the priorities
   - Each member reports their open items in one sentence each
   - The team agrees who picks up the watch item
   - Shift Lead closes with the single most important thing for the shift

4. Observing trainees complete the **Huddle Observation Checklist** from the Student Handout for the team they watch: did everyone speak? did they stay in time? was the priority clear at the end?

5. **Collect the observation checklists with the afternoon pack. This is competency evidence.**

> **Trainer Tip on sequencing:** Sequential in the main room, not parallel in breakouts. You can only observe one room at a time, and 400311102 LO2 requires *observed* participation. If the cohort is large enough that four minutes each will not fit, run them in parallel breakout rooms **with recording on in each room**, and review the recordings the same evening. Do not run them in parallel with nothing capturing them — you will have no evidence, and you will know it.

> **Watch for the silent trainee.** The huddle exposes them, and online it exposes them faster — a person who does not speak on a call is unmistakable. Do not let a team carry a member who says nothing. The unit requires *contribution*, and the assessor will look for it. If someone is silent, note it and give them the Shift Lead role in the Day 2 rotation.

---

## 11:50 AM – 12:00 PM | HAND OFF TO THE AFTERNOON (10 min)

> **This is not a wrap-up. It is a briefing, and the afternoon depends on it.** Ten minutes spent here saves you an evening of answering the same four questions by message.

### Steps:

1. **Share your screen and open the Self-Study Pack in front of them.** Do not describe it — show it. Scroll through the task list so every trainee has seen the document they are about to work from.

2. Walk the eight tasks, one line each:

| # | Task | Time | Hand in |
|---|------|------|---------|
| 1 | Take the pre-test | 45 min | Submitted automatically |
| 2 | Set up your evidence folder | 15 min | Screenshot of the folder tree |
| 3 | Write up this morning's shift handover | 20 min | Completed Shift Handover Log |
| 4 | Read the Day 1 Student Handout | 30 min | Nothing — but Tasks 5 and 6 assume it |
| 5 | **Mark up the Alert Intake SOP** | 45 min | Worksheet + four answers |
| 6 | **Triage three written notices** | 30 min | Grid + three answers |
| 7 | Find and evaluate a real security advisory | 25 min | Evaluation sheet |
| 8 | Day 1 reflection and Day 2 preparation | 10 min | Short written answer |

3. **Name the two that carry the unit:**
   > "Tasks 5 and 6 are the ones that matter most. Between them they are the whole of LO2 — performing workplace duties following written notices — and they are marked. The others are real work too, but if you run out of afternoon, those two are the ones that cannot slip."

4. **Flag the trap, without giving it away:**
   > "Task 5, question one, is about a clock. Almost everybody gets it wrong the first time, and the reason they get it wrong is the single most common cause of missed SLAs in real security operations centres. Read section 3.3 twice. We open Day Two with it."

5. Confirm the mechanics on screen:
   - **Where** to submit and **by when**
   - Everything also goes in their own `Evidence/Day_01/` folder
   - How to reach you this afternoon, and **what your response time actually is** — if you will not be at your desk from 1:00 to 5:00, say so now
   - Teams have each other's contact details: they may discuss, but the worksheets are individual work

6. Rapid recall before you close — two minutes, and it tells you what landed:
   - "What are the five sections of a handover?" *(Open items, escalated, watch items, system status, client notes)*
   - "What is the read-back rule?" *(Repeat the instruction in your own words before acting)*
   - "What three situations mean stop and ask for clarification?"
   - "Are you Accountable for a containment decision?" *(**No** — escalate)*

7. Preview Day 2:
   > "Tomorrow is problem solving. Not 'here is a puzzle' problem solving — real desk faults. An agent that stopped reporting. Duplicate tickets. A false-positive storm that buries your queue. You will learn a method for taking those apart, and you will use it every day for the rest of your career. We start with the SOP debrief, so bring your marked-up copy."

8. **Do not close the meeting on the dot.** Stay in the room for five minutes after twelve. The trainee who is confused about the pack will not say so in front of everyone, and this is the only chance they get to catch you.

---

# AFTERNOON — FULL ASYNCHRONOUS (1:00 – 5:00 PM)

## WHAT THE TRAINEES ARE DOING

Eight tasks, roughly **3 hours 40 minutes** of genuine work in a four-hour window. The instruction sheet is the **Self-Study Pack**; everything else hangs off it.

| Task | Time | Unit | Evidence produced |
|------|------|------|------------------|
| 1 Pre-test | 45 min | Diagnostic | Auto-recorded to your sheet |
| 2 Evidence folder | 15 min | ICT311203 preview | Screenshot |
| 3 Shift handover write-up | 20 min | **400311101 LO1** (reinforcement) | Completed Shift Handover Log |
| 4 Read the handout | 30 min | — | None (feeds Tasks 5, 6, 8) |
| 5 SOP markup | 45 min | **400311101 LO2** | Worksheet + 4 answers |
| 6 Written notice triage | 30 min | **400311101 LO2** | Grid + 3 answers |
| 7 Source evaluation | 25 min | 400311106 preview | Evaluation sheet |
| 8 Reflection and Day 2 prep | 10 min | — | Short written answer |

---

## YOUR AFTERNOON — WHAT THE TRAINER DOES BETWEEN 1:00 AND 5:00

Asynchronous does not mean absent. Three things, in this order.

### 1. Be reachable, and be specific about when (ongoing)
State a window — "I am at my desk 1:00 to 3:00 and I will answer within fifteen minutes; after three, by the end of the day." A stated window that you keep is worth far more than a vague promise of availability.

**The three questions you will actually get, and the answers:**

| They ask | You answer |
|----------|-----------|
| "Can I look things up for the pre-test?" | No. An honest low score tells me where to spend fifteen days. A researched high score tells me nothing. |
| "Which document is the SOP?" | Document 1 in the SOP Pack, `SOP-SOC-001`. |
| "Can I work on this with my team?" | Discuss it, yes. Submit the same words, no. The worksheets are individual. |

### 2. Read the pre-test results and the morning's evidence (about an hour)
You now have four things you did not have this morning: the pre-test scores, the Home Workstation Audits, the huddle observation checklists, and your own notes from the read-back drill. Read them together. **You will be teaching two different classes in the same cohort for fifteen days** — the person who has never opened a command line and the person who administers a network. Knowing who is who today is worth an hour.

Note specifically:
- Who scored lowest on the pre-test, and in which section
- Who did not speak in the huddle
- Who guessed in the read-back drill instead of asking you to repeat
- Whose workstation audit was all passes and no notes *(they did not really look)*

### 3. Mark the afternoon submissions as they arrive (rolling)
Do not wait for the deadline and mark thirty packs at once. Mark them as they land — you will be finished by six, and you will have a far better sense of where the cohort is.

---

## MODEL ANSWERS FOR THE MARKED TASKS

### Task 5 — SOP markup

| Step | Binding word | Requires | Clock |
|------|-------------|----------|-------|
| 3.1 | SHALL | Record four fields: alert ID, source system, timestamp, affected host | **Yes** — 5 min from receipt |
| 3.2 | SHALL | Assess against the Severity Matrix **before any other action** | No, but it is a sequence lock |
| 3.3 | MUST | Notify the client for Critical or High | **Yes** — 15 min from **assessment** |
| 3.4 | SHOULD check / SHALL record | Check for a Change Notice; if one explains it, recording the reference is mandatory | No |
| 3.5 | MAY | Discretion to close a Low **provided it is documented** | No |
| 3.6 | SHALL NOT | No containment authority at all | No |
| 3.7 | SHALL | Record every action, its time, and who authorised it | No |
| 3.8 | SHALL | Complete a handover log at end of shift | Yes — end of shift |

**Q1 — 22:35.** The clock in §3.3 runs from **assessment**, not receipt. They were already late on §3.1's five-minute recording requirement, but that does not move the §3.3 deadline. *This is the item most of the class will get wrong. It is also the single most common cause of missed SLAs in real operations, so open Day 2 with it.*

**Q2 — Step 3.5.** "May close" is conditional on "provided the assessment is documented." Undocumented discretion is not discretion.

**Q3 — Refuse and escalate. Step 3.6.** The correct response: *"I do not have authority to do that. I am escalating to the SOC Manager now and they will call you back."* Then escalate immediately. Watch for trainees who want to be helpful and say yes — that instinct is good and needs redirecting, not crushing.

**Q4 — The change reference.** Step 3.4 makes recording it **shall**, not should.

### Task 6 — Written notices

**A. Not an incident.** CHG-2026-1177 covers exactly those four hosts, in that window. Record the change reference and close as expected activity.

**B. Incident.** Cebu is not in the change notice. The notice tells you what is **not** covered just as much as what is — that is the whole point of the exercise.

**C. Follow the Northwind notice.** It explicitly says *"This supersedes… FOR THIS CLIENT ONLY."* A document with the authority to override says so.

> **The teaching point, and it is the best one available today:** the correct behaviour when two documents conflict is not to pick the stricter, newer, or preferred one. It is to check whether the notice **has authority to override** — and if you cannot tell, to ask. Anyone who answered "follow the stricter one" has reasoned sensibly and still got it wrong, which makes them the most useful person to hear from when you debrief.

### Task 3 — Shift handover write-up
Mark against **your own script**, not against a model answer. You are looking for the five sections, the ticket numbers recorded accurately, and — most tellingly — whether they wrote down the item you mumbled. A trainee who left a gap and noted *"could not hear the hostname — would confirm"* has demonstrated the competency better than one who filled in a plausible guess.

### Task 7 — Source evaluation
There is no single right answer. Mark on **whether they identified the publisher correctly** and **whether they placed it in the right tier**. A trainee who picked a news article and correctly ranked it *Unverified* has done better work than one who picked a vendor advisory and could not say why it was authoritative.

---

## MARKING APPROACH

**Mark for reasoning, not neatness.** Every one of these tasks follows a single morning of instruction. What you are looking for is:

- Did they find the binding verbs? *(Task 5)*
- Did they notice the boundary — what a notice does **not** cover? *(Task 6, Q B)*
- Did they refuse the containment request? *(Task 5, Q3)*
- Did they record the handover honestly, gaps and all? *(Task 3)*

Give a mark of **Attempted / Developing / Solid** rather than a score. LO2 is assessed properly across Days 1–3; nothing today is a final competency judgement.

---

## IF A TRAINEE DOES NOT SUBMIT

Chase it the same evening, not on Day 3. One message, no lecture:

> "I do not have your Day 1 pack. Tasks 5 and 6 are the written-notices element of unit 400311101 and I need them for your portfolio. Send what you have by tomorrow morning even if it is incomplete — I would rather see a half-finished attempt than nothing."

A trainee who misses the first asynchronous block and hears nothing about it has learned that asynchronous work is optional. There are fourteen days left in which that lesson will cost you.

---

## COMPETENCY EVIDENCE COLLECTED TODAY

**From the synchronous morning:**
- ✅ **400311101 LO1** — Handover notes taken from a live spoken briefing; read-back drill observed; clarifying-question role-play observed
- ✅ **400311102 LO1 & LO2** — Team formation record (chat log); Huddle Observation Checklists
- ✅ **400311107 (induction)** — Signed Home Workstation Audit

**From the asynchronous afternoon:**
- ✅ **400311101 LO1** — Completed Shift Handover Log written up from the morning briefing
- ✅ **400311101 LO2** — Marked-up SOP with worksheet and four answers; written notice grid with three answers
- ✅ **400311106 (preview)** — Source Evaluation Sheet
- ✅ Pre-test result *(trainer planning record, not graded)*
- ✅ Evidence folder screenshot

**Outstanding — carry forward to the first on-site day:**
- ⬜ **400311107** — Lab OSH Checklist, signed on site
- ⬜ **400311108** — Green Lab Pledge, signed on site

> **File these today.** Set up one folder per trainee now and put today's documents in it, including the note about the two outstanding lab documents. Fifteen days of evidence is a lot to reconstruct later, and a deferred item that is not written down is a deferred item that never happens.

---

## TRAINER NOTES

- **Protect the morning drills above everything else.** The read-back drill and the shift huddle are the only two things today that cannot be delivered any other way. Every other morning block has a written fallback in the afternoon pack. If you are running late, cut the SOC block — they read it this afternoon regardless.
- **Watch for the confident guesser.** In the read-back drill, the trainee who never asks you to repeat anything is not the strongest — they are the one most likely to escalate the wrong hostname on Day 9. Coach them today, while the audio is genuinely imperfect and asking is obviously reasonable.
- **Watch for the silent trainee.** The huddle exposes them, and a video call exposes them faster than a room does. Note names and give them the Shift Lead role on Day 2.
- **Do not teach tools today.** There is a strong pull to open a terminal on Day 1 because it feels like progress. Resist it. Days 4 and 5 are built for that, and today's units are genuinely assessed on communication.
- **Set the scanning boundary today, hard.** Say the "nothing outside the lab network" rule out loud on Day 1, put it on the shared screen, and repeat it every time you open a tool. By Day 12 they will have Nmap in their hands.
- **Say "the afternoon is not a half day" in the first twenty minutes.** Hybrid cohorts lose people in the first unstructured block, and the fix is entirely in how you frame it before lunch — not in how you chase it afterwards.
