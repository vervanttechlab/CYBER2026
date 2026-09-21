# DAY 9 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 9 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics are notes — never read them.)* Times match the Instructor Guide. Demo steps are in `Day_9_Demonstration_Guide.md`; this script cues the switch. Cut order at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 8 |
| 2 | 8:10 | Five topics |
| 3 | 8:15 | Topic 9.1 the case is not closed yet |
| 4 | 8:30 | Topic 9.2 → Demo 1 tell the client |
| 5 | 8:50 | Activity 1 Make the Call (observed) |
| 6–7 | 9:20 | Topic 9.3 → Demo 2 read the log for what failed |
| 8 | 9:45 | Activity 2 Find the Failure |
| — | 10:00 | Break |
| 9–10 | 10:10 | Topic 9.4 → Demo 3 who do you call |
| 11 | 10:30 | Activity 3 Who Gets This? |
| 12–13 | 10:45 | Topic 9.5 → Demo 4 build the pack · Demo 5 preview |
| 14 | 11:05 | Activity 4 Build the Pack |
| 15 | 11:35 | Afternoon brief & close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 9. Yesterday you stopped taking the tool's word for it — and three of the four verdicts on your worksheet meant 'the job is not finished'. Today is what finishing looks like. Tell the client what the scan found, honestly. Read the log for the action that failed. And hand that failure to the right person, with the pack they actually need."

> "Quick recall — yesterday, what were the three proofs of an action?" *(1117, ActionSuccess, Test-Path.)* "Good. Today you find out what to do when one of those proofs is missing."

> "Still no server — so failed actions come from your own machine's log and from a printed extract, and the escalation goes by email and into our register. And still going slowly."

*(Collect outstanding evidence. Announce role rotation — pairs today for Activity 1.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 9.1, the case is not closed yet — what follow-up is. 9.2, tell the client — the call, then the written confirmation. 9.3, read the log for what failed — five kinds of failure, and two of them never say 'failed'. 9.4, who do you call — the four authorities. And 9.5, the escalation pack — the document that person reads."

# SLIDE 3 — TOPIC 9.1: THE CASE IS NOT CLOSED YET
### 8:15 – 8:30 · 15 minutes
> "Here's the lifecycle on our desk: alert, decide, ticket, check the tool, verify — that's Days 6 to 8 — then follow up, escalate or close, report. Today is follow up, escalate or close. Two people decide whether a case is closed. The client — the person OUTSIDE the desk who owns the machine, the data, or the service. They must know the result. And the authority — the person ABOVE the desk. If anything failed, they must have what they need."

> "A case is closed when the client knows the truth and the authority has what they need. Not before. And one rule from yesterday, once more: a failed action re-opens a closed ticket. Not contained is a threat."

# SLIDE 4 — TOPIC 9.2: TELL THE CLIENT → DEMO 1
### 8:30 – 8:50 · 20 minutes
> "'Verified to the client' means two things, same day: a call, and a written confirmation. The call has eight steps — and the first one after your name is the ticket ID. Watch me make one."

*(Run **Demonstration 1** — the V1 call with the co-host, count the eight, fill the confirmation, paste it into the register row, then say the hard sentence for V2.)*

> "Same facts by voice and in writing. Match the words to the person — Ms Lopez gets 'a malicious program', not a threat name. And when the result is bad, the sentence is: 'The scan finished, and the threat is still there. It is not clean.' Plainly. The stakeholder needs the truth to protect the backups."

# SLIDE 5 — ACTIVITY 1: MAKE THE CALL
### 8:50 – 9:20 · 30 minutes · OBSERVED
> "Pairs. Two cases. V1 — WKS-118, clean, the user isn't technical. V2 — SRV-BAK-02, NOT clean, the backup administrator is technical and worried. One of you is the analyst, one is the client. Do V1, swap, do V2. Eight steps, ticket ID first, one specific ask, and get the read-back. I'm visiting each room and I'm listening to the V2 call for two things: did you say 'not clean' plainly, and did you get an ask and a read-back."

*(Observation sheet open. Visit each pair once during V2. Bring them back at 9:20.)*

# SLIDES 6–7 — TOPIC 9.3: READ THE LOG FOR WHAT FAILED → DEMO 2
### 9:20 – 9:45 · 25 minutes
> "'Scan logs are checked for failed action as per company SOP.' Our SOP is five kinds of failure — and the kind decides the next step. First, on my own machine, where it'll find nothing — and 'nothing' is a correct record. Then a machine where it's not nothing."

*(Run **Demonstration 2** — the two failed-action commands on your machine, then extract entries A, B, C, then the five kinds on slide 7.)*

> "Five kinds. Action failed — the 1118. Action incomplete — 'restart required'. No action taken — a 1116 and then silence. Scan did not complete — the 1002. Threat came back — a new 1116 after a good 1117. Two of those five never use the word 'failed'. Silence in the log is not good news."

# SLIDE 8 — ACTIVITY 2: FIND THE FAILURE
### 9:45 – 10:00 · 15 minutes
> "Teams. The extract has eight entries. I read A, B and C. You do all eight: for each, success or failure — and if failure, which kind, and the SOP's next step. Two entries are successes. One is the tool failing, not the action. One entry is two kinds at once."

*(Extract in `Day_9_Sample_Data.md` §2, taxonomy §3. Answers in Solutions. Bring out D — silence — and E — restart required.)*

# BREAK
### 10:00 – 10:10

# SLIDES 9–10 — TOPIC 9.4: WHO DO YOU CALL? → DEMO 3
### 10:10 – 10:30 · 20 minutes
> "The standard names four 'appropriate authorities'. IT department manager — machines and the change calendar. Information security manager — the security decision. The security vendor — the product. The CISO — the business risk. One rule: pick the person who can DO the thing you need. Three habits: first stop is your L2 or shift lead; one primary, copy the rest; Critical goes up fast, in one paragraph."

*(Run **Demonstration 3** — Situations 1, 3 and 5 worked aloud.)*

> "Uncontained, go to the security manager. Machine action, the IT manager. Tool broken or wrong, the vendor. Business on fire, the CISO, now. And a false positive on a business file is a vendor case — you don't un-quarantine it yourself."

# SLIDE 11 — ACTIVITY 3: WHO GETS THIS?
### 10:30 – 10:45 · 15 minutes
> "Teams. Eight situations. For each: the primary authority, who's copied, and why — what does that person own that you need? Three of the eight I've done with you. Do all eight anyway; you'll build packs for three of them this afternoon."

*(Eight situations in §4. Answers in Solutions. Bring out 4 — OS unpatched → IT manager — and 8 — comes back after offline scan → re-image → IT manager, security manager copied.)*

# SLIDES 12–13 — TOPIC 9.5: THE ESCALATION PACK → DEMOS 4 AND 5
### 10:45 – 11:05 · 20 minutes
> "This is the document the authority actually reads. Twelve fields — and three of them decide whether it works: the evidence, the ask, and the deadline. Without evidence it's an opinion. Without an ask it's a diary entry. Without a deadline it waits. Let me build one for SRV-BAK-02 — the ticket you wrote on Day 7, verified on Day 8, escalated today."

*(Run **Demonstration 4** — the 12 fields live for Situation 1, then update the register row.)*

> "And the row in the register — status escalated, to whom, when, next update due. Without that row, the pack is a document somebody sent. With it, there's a trail."

*(Run **Demonstration 5** — two screenshots, two minutes.)*

> "Tools like Hayabusa and the Wazuh server will find the failures in seconds instead of by hand. Same five kinds, same four authorities, same pack. Today you learned the part that doesn't change."

# SLIDE 14 — ACTIVITY 4: BUILD THE PACK
### 11:05 – 11:35 · 30 minutes
> "On your own. Pick Situation 2 or Situation 5 — the failing updates, or the live ransomware — and start the pack. Get fields 1 to 3, 5, 6 and 9 done before 11:35: who and why, the summary, the evidence lines from the extract, what failed by kind, and the ask with a deadline. The rest you finish this afternoon. Verb, object, time. Not 'please advise'."

*(Circulate. Anyone writing the pack from the story with no log lines — send them to the extract.)*

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:35 – 11:45 · 10 minutes
> "This afternoon: two client verification records — call notes and written confirmation for V1 and V2; the failed-action extract, all eight entries named by kind, plus the same pass on your own machine; three escalation packs — Situations 1, 2 and 5, one per authority type; the three register rows that make the trail; a one-page SOP card of the five kinds; a self-check of one pack against your Day 3 checklist; and the reflection. Marked as always — the reason matters more than the answer."

> "Today you closed the loop. You told a user the good news and a stakeholder the bad news — plainly. You found six failures in a log, including the three that never say 'failed'. You picked the right person for each and wrote the pack they need. One case — SRV-BAK-02 — has now gone from a Day 7 alert, to a Day 8 verdict, to a Day 9 escalation. Tomorrow, Day 10, it becomes a report — and then the first unit is assessed. Bring every Day 6 to 9 artefact, filed. Same hours for the morning. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
1. Activity 2 to entries B, C, D, E (skip A, F, G, H)
2. Activity 3 to five situations (1, 2, 3, 5, 8)
3. Demo 4 to fields 1, 5, 6, 9; skip Demo 5; Activity 4 starts in the afternoon
**Never cut** Demo 1 (the call), Activity 1 (observed) or Demo 2 (the five kinds).

# THE THREE SENTENCES OF THE DAY
1. **A case is closed when the client knows the truth and the authority has what they need — not before.**
2. **Five kinds of failure — and two of them never say "failed": silence after a 1116, and a 1002.**
3. **Evidence, ask, deadline — and pick the authority who can do the thing you need.**
