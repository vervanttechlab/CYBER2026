# DAY 8 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 8 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics are notes — never read them.)* Times match the Instructor Guide. Demo steps are in `Day_8_Demonstration_Guide.md`; this script cues the switch. Cut order at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 7 |
| 2 | 8:10 | Five topics |
| 3–4 | 8:15 | Topic 8.1 → Demo 1 two stories, one event |
| 5 | 8:35 | Activity 1 Match the Story |
| 6 | 8:55 | Topic 8.2 → Demo 2 did the action really happen |
| 7 | 9:10 | Activity 2 Prove Your Action |
| 8 | 9:30 | Topic 8.3 → Demo 3 up to date, or patched |
| — | 10:00 | Break |
| 9–10 | 10:10 | Topic 8.4 → Demo 4 the four scans |
| 11 | 10:30 | Activity 3 Update, Then Scan (observed) |
| 12–13 | 11:00 | Topic 8.5 → Demo 5 the worksheet · preview |
| 14 | 11:15 | Activity 4 Which Scan Would You Run? |
| 15 | 11:35 | Afternoon brief & close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 8. Yesterday you decided what each alert was, wrote the ticket, and checked that the security tool was actually working. Today you check something bigger: whether what the tool SAID is true. The tool tells a story. The log is the evidence. An analyst doesn't repeat the story — they verify it."

> "Quick recall — yesterday, what separates a threat from a detection?" *(Containment.)* "Good. Hold onto that, because today you find out whether the containment actually happened."

> "Still no server — so the 'infected system' today is your own machine, which already has a real detection on it: your EICAR from Day 6. And still going slowly."

*(Collect outstanding evidence. Announce role rotation.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 8.1, two stories, one event — the tool's story against the raw log. 8.2, did the action really happen — proving it, three ways. 8.3, up to date or patched — four version numbers and one update you run yourself. 8.4, scan the suspect machine — four kinds of scan, and which one when. And 8.5, the verification worksheet that ties it all together — the document you'll fill five times this afternoon."

# SLIDES 3–4 — TOPIC 8.1: TWO STORIES, ONE EVENT → DEMO 1
### 8:15 – 8:35 · 20 minutes
> "Every detection lives in two places. The friendly view — Protection history, the popup, the ticket somebody wrote. That's the STORY. And the raw log — the antivirus's own record, event by event. That's the EVIDENCE. Four things must match between them: the time, the threat name, the file path, and the action. Follow along."

*(Run **Demonstration 1** — Protection history, then `Get-WinEvent` on the Operational log, tick off the four, then show what a mismatch looks like with Case 2.)*

> "When the story and the log disagree, you believe the log. And the log often says MORE than the story — an extra file, an extra time, or no action at all. Read the lines around your event."

# SLIDE 5 — ACTIVITY 1: MATCH THE STORY
### 8:35 – 8:55 · 20 minutes
> "In teams: five cases. Each has a story and a log. For each one, tick or cross the four things — time, name, path, action — and write what doesn't match, and whether the action is proven. Two of the five are clean. Three are not, in three different ways."

*(Five cases in `Day_8_Sample_Data.md` §1. Answers in Solutions. Bring out Case 2 — the ticket says quarantined, the log says failed — and Case 5 — found, nothing done.)*

# SLIDE 6 — TOPIC 8.2: DID THE ACTION REALLY HAPPEN? → DEMO 2
### 8:55 – 9:10 · 15 minutes
> "Yesterday you READ the action — 'quarantined'. Today you PROVE it. Three proofs: the log says it acted — the 1117. The tool says it succeeded — ActionSuccess True. And the file is actually gone — Test-Path says False. Follow along."

*(Run **Demonstration 2** — `Get-MpThreatDetection`, `Test-Path`, `MpCmdRun -Restore -ListAll`, then the sixth action: re-image.)*

> "A ThreatStatusID of 1, or anything over 100, means not contained — and not contained means threat. And the last action on the list, re-image: wipe and rebuild. You'll never do it. You'll record that the others didn't hold, and recommend it."

# SLIDE 7 — ACTIVITY 2: PROVE YOUR ACTION
### 9:10 – 9:30 · 20 minutes
> "Now on your own machine. Your EICAR from Day 6. Prove the action three ways: find the 1117 in the log, read ActionSuccess and the status number, and run Test-Path on the file. Screenshot each one — those three pictures go in your evidence folder. If Test-Path says True — the file is still there — don't panic. That is a finding. Write it down as you would report it."

*(Pairs for help. Circulate. Anyone whose file is still there has real-time protection off or a different AV — a genuine finding; praise it.)*

# SLIDE 8 — TOPIC 8.3: UP TO DATE, OR PATCHED → DEMO 3
### 9:30 – 10:00 · 30 minutes
> "Four layers can be out of date, and most people only ever look at one. The signatures — the list of known threats. The engine — the scanner. The platform — the product. And the operating system underneath all of it. Follow along — we read all four, then we update one of them ourselves."

*(Run **Demonstration 3** — four layers before, `Update-MpSignature` or the GUI, four layers after, `Get-HotFix`, then draw the line.)*

> "You patch the signatures. Before and after — that's your evidence. You do NOT patch the operating system on a server by yourself; that's IT's job in a change window. You find it's behind, you report it. 'As required' means as the SOP requires."

# BREAK
### 10:00 – 10:10

# SLIDES 9–10 — TOPIC 8.4: SCAN THE SUSPECT MACHINE → DEMO 4
### 10:10 – 10:30 · 20 minutes
> "Four scans. Quick — the usual hiding places, minutes. Full — every file, hours. Custom — one folder or drive, seconds. Offline — the machine restarts into a scanner that runs BEFORE Windows, for things that hide from Windows. The rule: quick for routine, custom for one place, full when you suspect and don't know where, offline when the machine itself can't be trusted."

> "Before I scan anything — it will find nothing, and that is correct. Real-time protection already removed the EICAR the second it was saved. Scans are for what real-time protection MISSED. Watch the process."

*(Run **Demonstration 4** — `MpCmdRun -Scan -ScanType 3` on `ScanTest`, the GUI scan options, point at Offline without clicking, start a quick scan and leave it.)*

> "The offline scan restarts your machine. We do not run it in class. Not once. If you want its log, run it after four o'clock, with your work saved."

# SLIDE 11 — ACTIVITY 3: UPDATE, THEN SCAN
### 10:30 – 11:00 · 30 minutes · OBSERVED
> "Your own machine, three steps, and I'm watching two things. One: read your signature version, run the update, read it again — write BOTH numbers down. Two: make a folder called ScanTest in Documents, put a text file in it, and run a custom scan on it — and tell me what the result means. Then start a quick scan and leave it running. Do not touch the offline scan."

*(Observation sheet open. Circulate. Bring them back at 11:00.)*

# SLIDES 12–13 — TOPIC 8.5: THE VERIFICATION WORKSHEET → DEMO 5
### 11:00 – 11:15 · 15 minutes
> "Everything this morning goes into one document — the verification worksheet. Eight rows. Story, evidence, match, proven, outcome, up to date, scan — and last, the verdict. Let me fill one, in order, with the EICAR case."

*(Run **Demonstration 5** — rows 1–8 on screen, then the two-minute Sandbox / Wazuh preview from screenshots.)*

> "Four verdicts: verified detection; failed action — threat, escalate; more than the story — follow up; not yet acted on — act now. Three of the four mean the job isn't finished. The verdict comes last and it must agree with your own rows. And when we get the server, the worksheet doesn't change — only where the evidence comes from."

# SLIDE 14 — ACTIVITY 4: WHICH SCAN WOULD YOU RUN?
### 11:15 – 11:35 · 20 minutes
> "In teams: seven situations. For each, which scan — quick, full, custom, or offline — and the reason. Same rule as always: the reason is what's marked. One of the seven is the offline scan. Find it."

*(Seven scenarios in `Day_8_Sample_Data.md` §4. Answers in Solutions. Scenario 4 — malware that comes back after every restart — is the offline one.)*

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:35 – 11:45 · 10 minutes
> "This afternoon: five verification worksheets from the five cases; one more for your own EICAR with your three screenshots; a patch-state report on your machine — before and after; scan logs for quick, custom and full — start the full one and let it run; the seven 'which scan' answers; a self-check of one worksheet against your Day 3 checklist; and the reflection. Offline scan: write the plan for everyone, run it only if you choose to, after four, with your work saved. Marked as always — the reason matters more than the answer."

> "Today you stopped taking the tool's word for it. You put the story next to the log, proved the action, found how far behind the machine was, and picked the right scan for the right reason. Tomorrow, Day 9: three of those four verdicts mean the job isn't done — so tomorrow is what happens next. Tell the client. Find the action that failed. Hand it to the right person. Same hours. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
1. Activity 1 to three cases (1, 2, 5)
2. Activity 4 to three scenarios (2, 4, 6), answered in chat
3. Demo 5 — the worksheet rows and the verdict table only; skip the preview
**Never cut** Demo 1 (story vs log), Demo 2 (the three proofs) or Activity 3 (observed).

# THE THREE SENTENCES OF THE DAY
1. **The tool tells a story; the log is the evidence — match time, name, path, action.**
2. **An action is proven, not assumed — event 1117, `ActionSuccess`, and the file itself.**
3. **Quick for routine, custom for one place, full when you suspect, offline when the machine can't be trusted.**
