# DAY 7 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 7 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics are notes — never read them.)* Times match the Instructor Guide. Demo steps are in `Day_7_Demonstration_Guide.md`; this script cues the switch. Cut order at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 6 |
| 2 | 8:10 | Five topics |
| 3–4 | 8:15 | Topic 7.1 decide what it is |
| 5 | 8:35 | Activity 1 Threat/Detection/Routine |
| 6 | 8:55 | Topic 7.2 → Demo 1 the ticket |
| 7 | 9:15 | Activity 2 Write the Ticket (observed) |
| 8 | 9:45 | Topic 7.3 p1 → Demo 2 installed/operational |
| — | 10:00 | Break |
| 9 | 10:10 | Topic 7.3 p2 → Demo 3 status |
| 10 | 10:30 | Activity 3 Is the Solution Working? |
| 11 | 10:55 | Topic 7.4 → Demo 4 can it clean up |
| 12–13 | 11:10 | Topic 7.5 → Demo 5 console · Wazuh preview |
| 14 | 11:25 | Activity 4 Read the Console |
| 15 | 11:38 | Afternoon brief & close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 7. Yesterday you received alerts — from a tool and from a person — and made a real detection on your own machine. Today you finish the front of the job: you DECIDE what each alert is, you write the ticket, and then you check something people forget to check — whether the security tool that raised the alert is even working."

> "Quick recall — yesterday, when the antivirus caught the EICAR file, what three things did the detection tell us?" *(what, when, action.)*

> "Still no server — so today the ticket system is a shared spreadsheet, and every check runs on your own machine. And still going slowly, because this is new."

*(Collect outstanding evidence. Announce role rotation.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 7.1, decide what it is — threat, detection, or routine. 7.2, raise the ticket. 7.3 — the big one — is the tool even working. 7.4, can it clean up. And 7.5, the management console, with a first look at the Wazuh dashboard you'll use once the server's built."

# SLIDES 3–4 — TOPIC 7.1: DECIDE WHAT IT IS
### 8:15 – 8:35 · 20 minutes
> "Three words, from Day 3, and they run the whole job. THREAT — dangerous and NOT contained. DETECTION — bad, but the tool found AND handled it. ROUTINE — expected, authorised, or a false alarm."

> "Here's the one thing beginners get wrong, so learn it now: the line between threat and detection is CONTAINMENT, not size. A failed quarantine of small malware is a THREAT — found, but not stopped. A successful block of a serious attack is a DETECTION — found and handled. So 'the antivirus found it' is never the end of the story. You have to check whether the action actually worked — and that's the rest of today."

> "Two questions for every alert: is it real and bad? And is it contained? And always give a reason."

# SLIDE 5 — ACTIVITY 1: THREAT, DETECTION, OR ROUTINE?
### 8:35 – 8:55 · 20 minutes
> "In teams: I'll give you eight alerts. Sort each into threat, detection, or routine, and give the reason. Watch the tricky ones — some the antivirus 'found', but check whether it actually stopped them."

*(Eight alerts in `Day_7_Sample_Data.md` §1. Answers in Solutions. Bring out that Alert G — failed quarantine — is a threat, and Alert C — successful quarantine — is a detection.)*

# SLIDE 6 — TOPIC 7.2: RAISE THE TICKET → DEMO 1
### 8:55 – 9:15 · 20 minutes
> "A confirmed alert becomes a ticket. And a ticket is written for the NEXT person, not for you. Let me build one in our register — which, look, is almost exactly the checklist you wrote on Day 3."

*(Run **Demonstration 1** — fill a register row from Alert G, thinking aloud; stop on the decision to make the containment point; two timestamps; the ask; the SLA clock.)*

> "Two timestamps, always. A clear reason. And a specific ask — a ticket with no ask is a diary entry."

# SLIDE 7 — ACTIVITY 2: WRITE THE TICKET
### 9:15 – 9:45 · 30 minutes · OBSERVED
> "Now you write one. Pick an alert, and fill a full ticket in the register. Use your Day 3 checklist. This is watched — I'm looking for two things: a decision WITH a reason, and the two timestamps plus a real next-step ask."

*(Observation sheet open. Bring them back at 9:45.)*

# SLIDE 8 — TOPIC 7.3 PART 1: IS IT INSTALLED AND OPERATIONAL? → DEMO 2
### 9:45 – 10:00 · 15 minutes
> "Now Element 2 of the job. Before you trust what a tool told you, check the tool is actually working. Three questions: is it installed, is it operational, is it up to date. Follow along."

*(Run **Demonstration 2** — `Get-Service WinDefend`, then the Windows Security app green ticks.)*

> "Installed and operational are not the same thing. A tool can be installed and switched off."

# BREAK
### 10:00 – 10:10

# SLIDE 9 — TOPIC 7.3 PART 2: READING THE STATUS → DEMO 3
### 10:10 – 10:30 · 20 minutes
> "Here's the exact command — and you've seen it before, on Day 5, when we baselined the machine. Now you know why it matters."

*(Run **Demonstration 3** — `Get-MpComputerStatus`, read each field, then show what a finding looks like: real-time off, or old signatures.)*

> "A tool that is switched off is worse than no tool, because people think they're protected. Finding that it's off is a real, everyday analyst job."

# SLIDE 10 — ACTIVITY 3: IS THE SOLUTION WORKING?
### 10:30 – 10:55 · 25 minutes
> "Run the two checks on your OWN machine. Write down: installed? operational? up to date? And if anything is off or old, that's your finding — write it as you would report it. This becomes your solution-status report this afternoon."

*(Circulate. Anyone whose real-time protection or signatures show a problem has found a genuine finding — praise it.)*

# SLIDE 11 — TOPIC 7.4: CAN IT CLEAN UP? → DEMO 4
### 10:55 – 11:10 · 15 minutes
> "Last Element 2 question: can the tool actually clean or delete the problem? Let's prove it with yesterday's EICAR detection."

*(Run **Demonstration 4** — Protection history action on EICAR; name the action range; MpCmdRun list; tie back to containment.)*

> "Cleaned and quarantined are successes. Failed is not — and a failed action turns a detection into a threat. That's the link back to this morning: checking the action is how you tell them apart."

# SLIDES 12–13 — TOPIC 7.5: THE MANAGEMENT CONSOLE → DEMO 5
### 11:10 – 11:25 · 15 minutes
> "Everything today was for one machine. A management console does the same checks for hundreds of machines on one screen."

*(Run **Demonstration 5** — Windows Security as the local console, then the Wazuh preview screenshot.)*

> "Once our server is built you'll use the real Wazuh console. It's not a new skill — it just shows the same answers, installed, operational, up to date, what's detected, for the whole company at once."

# SLIDE 14 — ACTIVITY 4: READ THE CONSOLE
### 11:25 – 11:38 · 13 minutes
> "In teams: here's a console view of several machines. Which ones are healthy, which have a problem, and which would you report first? Give the reason."

*(Use the solution-status scenarios in `Day_7_Sample_Data.md` §3. Answers in Solutions.)*

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:38 – 11:45 · 7 minutes
> "This afternoon: triage eight alerts with reasons, turn them into ticket rows and write two in full, produce a solution-status report on your own machine, record the EICAR clean action, self-check two tickets against your Day 3 checklist, and fill the console worksheet. Marked as always — the reason matters more than the answer."

> "Today you finished the front of the job. You decided what each alert was, wrote a ticket the next person can use, and checked whether the tool was even working. You now know 'the antivirus found it' is a beginning, not an ending. Tomorrow, Day 8: does the tool's story actually match the raw evidence? Same hours. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
1. Activity 1 to five alerts
2. Activity 2 — one ticket live, rest → PM Task 2
3. Topic 7.5 to the console idea + one Wazuh screenshot; Activity 4 → quick discussion
**Never cut** Demo 3 (status) or Activity 2 (observed).

# THE THREE SENTENCES OF THE DAY
1. **Threat vs detection is CONTAINMENT — a failed action makes it a threat.**
2. **A ticket has two timestamps, a reason, and a specific ask — written for the next person.**
3. **Installed, operational, up to date — three separate checks; a tool that is off is worse than none.**
