============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 08
Verify — Does the Tool's Story Match the Evidence?
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_8_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 08 IS:
Day 8 delivers all of Element 3 of the core unit CS-ICT251101 — Perform manual
checking and verification (PC 3.1 check the detection, 3.2 check the action, 3.3
check and patch updates, 3.4 scan the infected system). Day 7 checked that the tool
was working; Day 8 checks whether what the tool SAID is true, by matching its story
to the raw log, proving the action, updating, and scanning.

TWO HARD CONSTRAINTS (same as Days 6-7):
- NO SIEM SERVER YET. Every check runs on the trainee's OWN Windows machine with
  Microsoft Defender; the "infected system" is their own machine with the EICAR
  detection from Day 6. Windows Sandbox and the Wazuh console appear only as a
  PREVIEW slide. Nothing depends on them.
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone.

THE FIVE TOPICS:
  8.1  Two Stories, One Event (the tool's story vs the raw log)
  8.2  Did the Action Really Happen? (three proofs; the action range incl. re-image)
  8.3  Up to Date, or Patched (signatures, engine, platform, OS)
  8.4  Scan the Suspect Machine (quick, full, custom, offline)
  8.5  The Verification Worksheet (detection -> action -> outcome -> verdict)

DAY 08 IS A BLENDED DAY (same hours as Days 5-7):
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Match the Story (teams, five paper cases); 2 Prove Your Action
(own machine, three proofs of the EICAR action); 3 Update, Then Scan (own machine,
observed); 4 Which Scan Would You Run? (teams, seven scenarios).

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables as real tables, commands in monospace. No agenda, thank-you, or Q&A slide.

Day 08 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, complete beginners. Short sentences, common words, calm tone. Define every term the first time (event ID, signature, engine, platform, quarantine, re-image, offline scan).

Carry the Day 7 rule and use it exactly: the line between THREAT and DETECTION is CONTAINMENT. Today's key idea, repeated plainly: the tool tells a STORY; the log is the EVIDENCE; an analyst verifies, never repeats.

SLIDE 1 — TITLE
Title: "Verify: Does the Tool's Story Match the Evidence?"
Subtitle: "Cyber Threat Monitoring Level I, Day 08 of 15"
Kicker: "Live demo 8:00-11:45  |  Self-study 1:00-4:00  |  On your own machine — your Day 6 EICAR is the case"
Visual: a calm navy title slide. On the left a speech bubble labelled "the story", on the right a log document labelled "the evidence", with a magnifying glass between them and four small ticks: time, name, path, action.

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: Check What the Tool Said"
Table (Topic / What you will be able to do):
8.1 Two Stories, One Event | Put the tool's story next to the raw log and check four things match
8.2 Did the Action Really Happen? | Prove an action three ways instead of assuming it
8.3 Up to Date, or Patched | Read four version layers, run the update, report what is behind
8.4 Scan the Suspect Machine | Choose quick, full, custom or offline — and say why
8.5 The Verification Worksheet | Fill the SOP worksheet and write a verdict with a reason
Add the line: "Yesterday you checked the tool was working. Today you check whether what it said is true."
Visual: five numbered topic cards.

SLIDE 3 — TWO STORIES, ONE EVENT (Topic 8.1, part 1)
Title: "The Story and the Evidence"
Two columns:
THE STORY — Protection history, the popup, the ticket. A summary written by the tool or by a person.
THE EVIDENCE — the Windows Defender Operational log. Event 1116 = detected. Event 1117 = action taken. Event 1118 / 1119 = action FAILED.
Big line: "Four things must match: TIME · THREAT NAME · FILE PATH · ACTION."
Add the line: "When the story and the log disagree, believe the log."
Visual: two panels side by side with four connecting lines, each ending in a tick box.

SLIDE 4 — WHAT A MISMATCH LOOKS LIKE (Topic 8.1, part 2)
Title: "The Ticket Said Quarantined. The Log Said Failed."
Show a short two-line contrast in monospace:
Ticket: "Wacatac quarantined — contained. Closed."
Log:    "14:05:12  Event 1118  ... the action FAILED. File is in use."
Add: "And sometimes the log says MORE than the story — an extra file, another time, or a 1116 with no 1117 at all (found, nothing done)."
Big line: "Read the lines around your event. The summary is not the whole record."
Visual: a ticket card (green, "contained") with a red log line beneath it contradicting it.

SLIDE 5 — ACTIVITY 1: MATCH THE STORY
Title: "Activity 1 — Five Cases, Four Ticks Each"
Instructions as steps:
- In your team, take the five cases. Each has a story and a raw log.
- For each: tick or cross TIME, NAME, PATH, ACTION. Write every mismatch.
- Then: is the action PROVEN? (Is there a 1117 with error code 0?)
Big line: "Two cases are clean. Three are not — in three different ways. Find them."
Visual: five case cards, each with a row of four small tick boxes.

SLIDE 6 — DID THE ACTION REALLY HAPPEN? (Topic 8.2)
Title: "Proven, Not Assumed — Three Proofs"
Three numbered proofs:
1. THE LOG SAID SO — Event 1117, Error Code 0x00000000
2. THE TOOL SAYS IT SUCCEEDED — Get-MpThreatDetection: ActionSuccess = True; ThreatStatusID 2 cleaned / 3 quarantined / 4 removed / 6 blocked
3. THE FILE IS GONE — Test-Path "<file>" = False
Then the action range as chips: FAILED · CLEAN · DELETE · QUARANTINE · BLOCKED · RE-IMAGE, with RE-IMAGE marked "new today — wipe and rebuild; used when the others cannot be trusted; an L1 recommends, does not do it".
Big line: "ThreatStatusID 1, or anything over 100, = NOT contained = THREAT."
Visual: three proof cards in a row leading to a green "proven" badge.

SLIDE 7 — ACTIVITY 2: PROVE YOUR ACTION
Title: "Activity 2 — Your Own EICAR, Three Ways"
Instructions as steps:
- Find the 1117 for your EICAR in the log. Screenshot it.
- Run Get-MpThreatDetection. Read ActionSuccess and the status number. Screenshot it.
- Run Test-Path on the EICAR file. Screenshot it.
- If Test-Path says TRUE — the file is still there — that is a FINDING. Write it as you would report it.
Big line: "Three screenshots = one proven action. Into Evidence/Day_08."
Visual: three small screenshot frames with a tick under each.

SLIDE 8 — UP TO DATE, OR PATCHED (Topic 8.3)
Title: "Four Layers Can Be Out of Date"
Table (Layer / Field / "Behind" means):
Signatures (the list of known threats) | AntivirusSignatureVersion, AntivirusSignatureAge | Over 1-2 days old — cannot see this week's threats
Engine (the scanner) | AMEngineVersion | Months old
Platform (the product) | AMProductVersion | Months old
Operating system | Get-HotFix; Settings > Windows Update | No security update in over a month
Show in monospace: Update-MpSignature   (or Windows Security > Protection updates > Check for updates)
Big line: "You patch the SIGNATURES yourself — read the version before and after. You REPORT the operating system; IT patches it in a change window."
Visual: four stacked layers, the bottom one (OS) widest; a small "before / after" version pair.

SLIDE 9 — THE FOUR SCANS (Topic 8.4, part 1)
Title: "Quick, Full, Custom, Offline"
Table (Scan / Looks at / Takes / Right call when):
Quick | The usual hiding places — memory, startup, system folders | Minutes | Routine; daily; "just check"
Full | Every file on every drive | Hours | You suspect and don't know where; protection was off; before handing a machine back
Custom | One folder, file or drive you choose | Seconds-minutes | You know exactly where — a download, a USB drive
Offline | The whole system from OUTSIDE Windows — the machine restarts into a small scanner | 15-20 min + restart | Malware that comes back, or hides from Windows
Big line: "Quick for routine. Custom for one place. Full when you suspect. Offline when the machine can't be trusted."
Visual: four scan icons of increasing depth.

SLIDE 10 — WHAT A SCAN IS FOR (Topic 8.4, part 2)
Title: "Nothing Found Is Not a Failed Scan"
Explain: "On a healthy machine, real-time protection removes a threat the moment it lands. A scan is for what real-time protection MISSED: a file that arrived while protection was off, a drive just plugged in, something that hides."
Show in monospace: MpCmdRun.exe -Scan -ScanType 3 -File "<folder>"   ->  Scan finished. ... found no threats.
Add: "Every scan writes event 1000 (started) and 1001 (finished). A 1002 means it stopped early — and a scan that did not finish is not a scan."
Warning box (red, sparing): "NEVER run the OFFLINE scan in class. It restarts your machine immediately."
Visual: a shield with a "real-time" label catching a file mid-air, and a scan icon sweeping the floor for what got past it.

SLIDE 11 — ACTIVITY 3: UPDATE, THEN SCAN
Title: "Activity 3 — On Your Own Machine"
Instructions as steps:
- Read your signature version. Run the update. Read it again. Write BOTH numbers.
- Make Documents\ScanTest with one text file. Run a CUSTOM scan on it. Say what the result means.
- Start a QUICK scan and leave it running.
- Do NOT touch the offline scan.
Big line: "This one is watched: before-and-after versions, and the right scan with the right reason."
Visual: a three-step checklist with a small red "no" mark on an offline-scan button.

SLIDE 12 — THE VERIFICATION WORKSHEET (Topic 8.5, part 1)
Title: "Eight Rows, Filled in Order"
Show the worksheet rows as a numbered list:
1 The story (name · path · time · action)  2 The evidence (the same four, from the log)  3 Do they match?  4 Is the action proven?  5 Outcome: contained / not  6 Up to date? (four layers)  7 Scan: type · why · result  8 VERDICT + reason
Then the four verdicts as chips: VERIFIED DETECTION · FAILED ACTION -> threat, escalate · MORE THAN THE STORY -> follow up · NOT YET ACTED ON -> act now
Big line: "The verdict comes last, and it must agree with your own rows. Three of the four mean the job is not finished."
Visual: a worksheet form with row 8 highlighted.

SLIDE 13 — A LOOK AHEAD: SANDBOX AND WAZUH (Topic 8.5, part 2)
Title: "Where the Evidence Will Come From Later"
Two preview cards, both clearly marked "preview — not today":
WINDOWS SANDBOX — a throw-away copy of Windows inside your Windows; open something suspicious, close it, it is gone. Needs Windows Pro and more memory than most of our machines have.
WAZUH — once our server is built, every 1116 and 1117 from every machine arrives in one place, one search.
Big line: "The worksheet does not change. Only where the evidence comes from."
Visual: two labelled mock-up cards with a "coming later" ribbon.

SLIDE 14 — ACTIVITY 4: WHICH SCAN WOULD YOU RUN?
Title: "Activity 4 — Seven Situations, One Scan Each"
Instructions as steps:
- In your team, read the seven situations.
- For each: quick, full, custom, or offline — and the reason.
- One of the seven is the offline scan. Find it.
Big line: "The reason is what is marked."
Visual: seven situation cards sorting into four trays.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark as the start of self-study. Keep the table.
Table (Task / Time / Hand in):
1 | Five verification worksheets — the five cases, all eight rows | 40 min | 5 worksheets
2 | Your own EICAR worksheet, with your three screenshots | 20 min | 1 worksheet + 3 screenshots
3 | Patch-state report on your machine (before / after, engine, platform, OS) | 25 min | Patch-state report
4 | Scan logs: quick, custom, full (start it and let it run) + the offline plan | 30 min | 3 scan logs + plan
5 | "Which scan?" — seven scenarios with reasons | 15 min | 7 answers
6 | Self-check one worksheet against your Day 3 QA checklist | 10 min | 1 self-check
7 | Reflection | 10 min | Three answers
Closing line: "Today you stopped taking the tool's word for it. Next, Day 9: tell the client, find the action that failed, and escalate it to the right person."
Visual: a teal section band, the table, and a small "Day 8 of 15" progress bar.

============================================================
END OF PROMPT
============================================================
