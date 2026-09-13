# DAY 6 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 6 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics in brackets are notes — never read them.)* Times match the Instructor Guide timetable. When a slide has a demo, this script cues the switch; the steps are in `Day_6_Demonstration_Guide.md`. Cut order is at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 5 |
| 2 | 8:10 | Five topics · no server, we use your own machine |
| 3 | 8:15 | Topic 6.1 the alert arrives |
| 4–5 | 8:30 | Topic 6.2 → Demo 1 sources |
| 6 | 8:55 | Activity 1 Name That Source |
| 7 | 9:15 | Topic 6.3 intake channels |
| 8 | 9:30 | Activity 2 Take the Call (observed) |
| — | 10:00 | Break |
| 9 | 10:10 | Topic 6.4 → Demo 2 reading logs |
| 10 | 10:30 | Demo 3 EICAR |
| 11 | 10:45 | Activity 3 Make a Real Alert |
| 12–13 | 11:10 | Topic 6.5 → Demo 4 red flags & severity |
| 14 | 11:25 | Activity 4 Red Flag or Routine? |
| 15 | 11:38 | Afternoon brief & close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 6, and this is where the real job starts. For five days we built the ground — how to work, how to look things up, and yesterday, how to read the machine and the network under an alert. Today, the first step of the actual analyst job: an alert arrives, and you receive it and read it."

> "Quick recall from yesterday — when a connection went to a bad address, what command told us which program owned it?" *(Take answers: netstat -ano.)*

> "Two honest things about today. One: our SIEM server — the big security dashboard — is not built yet. So everything today runs on your OWN computer, with tools already on it. That is not a shortcut; it is the right way to start. Two: most of you have never opened these tools before. That is fine. We go slowly, and I show you every click."

*(Collect outstanding evidence. Announce role rotation.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 6.1, the alert arrives. 6.2, where alerts come from. 6.3, how people report incidents to you. 6.4 — the big one — reading alerts on your own machine, where you will make a real, safe detection happen. And 6.5, red flags and how serious an alert is."

> "By this afternoon you will have made an antivirus catch something, on purpose, and read exactly what it recorded. Let's go."

# SLIDE 3 — TOPIC 6.1: THE ALERT ARRIVES
### 8:15 – 8:30 · 15 minutes
> "Remember the six-step lifecycle from Day 3? It arrives, you look it up, you judge the source, you decide, you write the ticket, you check your work. Today and tomorrow we live inside step one: it arrives."

> "An alert reaches you in exactly two ways. A TOOL tells you — the antivirus caught a file. Or a PERSON tells you — someone calls and says their files have strange names. The standard calls the first a detection alert and the second an incident report. Both are alerts. Both must be written down the same way every time. 'I remember someone mentioned it' is not receiving an alert — receiving it means it is recorded."

# SLIDES 4–5 — TOPIC 6.2: WHERE ALERTS COME FROM → DEMO 1
### 8:30 – 8:55 · 25 minutes
> "Tools raise alerts, and there are a handful you should know by name. Let me show you four real examples and we'll name the tool behind each."

*(Run **Demonstration 1** — the four snippets, A=AV, B=firewall, C=WAF, D=DLP, each ending on its blind spot.)*

> "Antivirus watches files. Firewall watches traffic. WAF watches web requests. DLP watches data trying to leave. And a SIEM — the server we don't have yet — collects all of them in one place. Every single one has a blind spot, exactly like the lookup websites on Day 3. Today, the tool raising your alerts is the antivirus on your own machine: Defender."

# SLIDE 6 — ACTIVITY 1: NAME THAT SOURCE
### 8:55 – 9:15 · 20 minutes
> "Quick game in the chat. I show an alert, you tell me which tool made it, and — the important part — one thing that tool cannot see. A few seconds each."

*(Run the items from the Activity Pack. Answers in `Day_6_Solutions.docx`.)*

> "You now know the sources. Half your alerts come from tools like these. The other half come from people — that's next."

# SLIDE 7 — TOPIC 6.3: HOW INCIDENT REPORTS ARRIVE
### 9:15 – 9:30 · 15 minutes
> "A person reports an incident six ways, and the standard names all of them: phone, walk-in, email, SMS, chat, and video call. Whichever way, you capture the same five things: who is telling you and how to reach them back, what they saw in their own words, when it happened, which machine or account, and what they've already done."

> "The skill is the clarifying question. People never give you all five. 'The internet is broken' might be ransomware. You record what they said, and you gently ask for what's missing — especially a callback number, because that's the one thing you can't reconstruct later. And you stay calm. A frightened caller calms down when you are calm."

# SLIDE 8 — ACTIVITY 2: TAKE THE CALL
### 9:30 – 10:00 · 30 minutes · OBSERVED
> "Into pairs. I am going to play people reporting incidents — a panicked caller, a walk-in, a manager on a video call. Your job: fill in the intake form, and ask ONE clarifying question for the fact I leave out. This is watched: I'm looking for whether you capture the core facts, and whether you catch the missing one and ask for it, calmly."

*(Use the six intake scripts in `Day_6_Sample_Data.md` §3. Observation sheet open. Bring them back at 10:00 for the break.)*

# BREAK
### 10:00 – 10:10

# SLIDE 9 — TOPIC 6.4: READING YOUR OWN LOGS → DEMO 2
### 10:10 – 10:30 · 20 minutes
> "Now the heart of the day. Where does a computer write down security events? Three places, all already on your machine. Follow along with me."

*(Run **Demonstration 2** — Event Viewer, the System log, the Windows Defender / Operational log, and Protection history. Go slowly; it is their first time.)*

> "Event Viewer looks overwhelming. It is, for everyone. Nobody reads it all — we filter to what matters. And the friendliest view is Protection history in the Windows Security app. That's where you look first."

# SLIDE 10 — DEMO 3: MAKE A REAL ALERT (EICAR)
### 10:30 – 10:45 · 15 minutes
> "We are going to make the antivirus catch something on purpose. Before I do — this is completely safe. It's called the EICAR test file: a harmless line of text that every antivirus agreed to treat as dangerous, just so we can test them. It is not a virus and never was. Watch."

*(Run **Demonstration 3** — paste the EICAR string, save it, watch Defender react, read Protection history, then show event 1116 in the log.)*

> "That is a detection alert, start to finish. It tells you three things: what it found, when, and what it did about it. Write those three down and you've received an alert properly."

# SLIDE 11 — ACTIVITY 3: MAKE A REAL ALERT
### 10:45 – 11:10 · 25 minutes
> "Now you do it. Paste the EICAR string — it's in your Activity Pack — save it, and find your detection in Protection history. Write down the three things: what, when, and the action. If your machine blocks the file from saving at all, that block IS the detection — read it in Protection history. Nobody can break anything. Go."

*(Circulate the breakout rooms. Reassure anyone worried. This becomes PM Task 2 evidence.)*

# SLIDES 12–13 — TOPIC 6.5: RED FLAGS AND SEVERITY → DEMO 4
### 11:10 – 11:25 · 15 minutes
> "Last topic. 'Checking the red flag' means knowing the patterns that make an alert serious. The standard names two: ransomware, and a virus — a PE infection. Ransomware: many files renamed at once, a ransom note in every folder, backups deleted. A virus: a program file flagged, or a process with a fake system name running from the wrong place — you spotted exactly that on Day 5."

*(Run **Demonstration 4** — read the EICAR detection as 'not a red flag, Low', then contrast with a ransomware indicator card as 'Critical'. Show the severity matrix.)*

> "The tool gives a severity. That's your starting point, not your answer. You adjust for two things — is it contained, and whose machine is it — and you always write down why. The same detection is Medium on a training PC and High on the finance server."

# SLIDE 14 — ACTIVITY 4: RED FLAG OR ROUTINE?
### 11:25 – 11:38 · 13 minutes
> "In your teams: sort these indicator cards into ransomware, virus, or routine — and give each a severity band with a reason. The reason is what's marked, not the band. Argue it out."

*(Cards in `Day_6_Sample_Data.md` §4. Answers in Solutions.)*

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:38 – 11:45 · 7 minutes
> "This afternoon, on your own: process six incident reports onto intake forms, make and record your own detection, find three real events in your logs, build your sources reference, write two red-flag cards, and fill in a severity sheet. Marked the usual way — the reason matters more than the answer."

> "Today you received alerts the two ways they really arrive — from a tool and from a person — and you made a real detection happen on your own machine, with no server and no danger. Tomorrow, Day 7: you decide what each alert IS, you write the ticket, and you check whether the security tool is even working. Same hours. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
Cut in this order:
1. Activity 1 to 3 items
2. Activity 2 to three intake scripts (rest → PM Task 1)
3. Topic 6.5 live to the two red flags only (severity → PM Task 6)
**Never cut** Demo 3 (EICAR) or Activity 2 (observed). They are the highlight and the observed evidence.

# THE THREE SENTENCES OF THE DAY
1. **An alert is a tool telling you or a person telling you — both get written down.**
2. **EICAR is a safe test file; catching it is a real detection, start to finish.**
3. **The tool's severity is the start; you adjust for containment and asset, and write the reason.**
