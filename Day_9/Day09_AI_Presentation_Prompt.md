============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 09
Close the Loop — Tell the Client, Find What Failed, Escalate It
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_9_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 09 IS:
Day 9 delivers all of Element 4 of the core unit CS-ICT251101 — Conduct case
follow-up (PC 4.1 verify scan results to the customer/client/stakeholder, 4.2 check
scan logs for failed action per SOP, 4.3 escalate failed action to the appropriate
authority per SOP). Day 8 ended with verdicts meaning "not finished"; Day 9 finishes:
the client call and written confirmation, the failed-action pass, and the escalation
pack to one of four authorities (IT department manager, information security
manager, security vendor, CISO).

TWO HARD CONSTRAINTS (same as Days 6-8):
- NO SIEM SERVER YET. Failed actions are read from Defender's own log on the
  trainee's machine and from a printed log extract. The ticket "system" is a shared
  spreadsheet register; the escalation goes by email. Hayabusa / DeepBlueCLI /
  Timeline Explorer and the Wazuh console appear only as a PREVIEW slide.
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone.

THE FIVE TOPICS:
  9.1  The Case Is Not Closed Yet (what follow-up is; the lifecycle)
  9.2  Tell the Client (the call, then the written confirmation)
  9.3  Read the Log for What Failed (five kinds of failure; the SOP next step)
  9.4  Who Do You Call? (the four authorities and what each needs)
  9.5  The Escalation Pack (build it, send it, log the trail)

DAY 09 IS A BLENDED DAY (same hours as Days 5-8):
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Make the Call (pairs role-play, a clean case and a not-clean
case, observed); 2 Find the Failure (teams, eight log entries, name the kind);
3 Who Gets This? (teams, eight situations, which authority); 4 Build the Pack
(individually, start one escalation pack).

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables as real tables, commands in monospace. No agenda, thank-you, or Q&A slide.

Day 09 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, complete beginners. Short sentences, common words, calm tone. Define every term the first time (stakeholder, read-back, escalate, authority, false positive, CISO, re-image).

Carry two rules from earlier days and use them exactly: NOT CONTAINED = THREAT (Day 7); the tool tells a STORY, the log is the EVIDENCE (Day 8). Today's key idea, repeated plainly: a case is closed when the client knows the truth and the authority has what they need — not before.

SLIDE 1 — TITLE
Title: "Close the Loop: Tell the Client, Find What Failed, Escalate It"
Subtitle: "Cyber Threat Monitoring Level I, Day 09 of 15"
Kicker: "Live demo 8:00-11:45  |  Self-study 1:00-4:00  |  Your own machine, a printed log extract, and the ticket register"
Visual: a calm navy title slide. A loop drawn as three arrows: a phone (tell the client), a log page with a red mark (find what failed), and an upward arrow to a person icon (escalate).

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: Finish the Case"
Table (Topic / What you will be able to do):
9.1 The Case Is Not Closed Yet | Say what follow-up is, and who decides a case is closed
9.2 Tell the Client | Make the verification call and write the same-day confirmation — clean or not
9.3 Read the Log for What Failed | Name five kinds of failure and the SOP's next step for each
9.4 Who Do You Call? | Choose the right authority — and say why them
9.5 The Escalation Pack | Build the pack with evidence, an ask and a deadline; log the trail
Add the line: "Yesterday three of the four verdicts meant 'not finished'. Today is what finishing looks like."
Visual: five numbered topic cards.

SLIDE 3 — THE CASE IS NOT CLOSED YET (Topic 9.1)
Title: "Two People Decide When a Case Is Closed"
Show the lifecycle as a chain: alert -> decide -> ticket -> check the tool -> verify -> FOLLOW UP -> ESCALATE or CLOSE -> report. Mark "Days 6-8" over the first five, "TODAY" over follow up / escalate or close.
Two arrows from the desk:
OUTSIDE the desk — the CLIENT / STAKEHOLDER (owns the machine, the data, the service). Must know the result.
ABOVE the desk — the APPROPRIATE AUTHORITY. Must have what they need if anything failed.
Big line: "A case is closed when the client knows the truth and the authority has what they need. Not before."
Add the line: "A failed action re-opens a closed ticket. Not contained = threat."
Visual: a desk icon in the middle with one arrow out (to a person) and one arrow up (to a manager).

SLIDE 4 — TELL THE CLIENT (Topic 9.2)
Title: "The Call, Then the Confirmation — Same Facts, Same Day"
Left — the eight steps of the call, numbered:
1 Who you are + the TICKET ID · 2 What was found, in plain words · 3 What was done, and what the scan showed · 4 What it means for them · 5 What happens next · 6 One specific ask · 7 READ-BACK ("tell me back what you'll do") · 8 "In writing within the hour"
Right — the written confirmation: "Subject: <ticket> — <host> — CLEAN / NOT CLEAN. Six numbered lines: found, done, scan result, what it means, what next, what we need. Pasted into the ticket."
Big line: "When the result is bad, say it plainly: 'The scan finished, and the threat is still there. It is not clean.'"
Add: "Match the words to the person — a user gets 'a malicious program'; a backup administrator gets the times."
Visual: a phone icon on the left, an email/document icon on the right, joined by an equals sign.

SLIDE 5 — ACTIVITY 1: MAKE THE CALL
Title: "Activity 1 — One Clean Call, One Not"
Instructions as steps:
- In pairs. V1: WKS-118, CLEAN, the user is not technical. V2: SRV-BAK-02, NOT CLEAN, the backup administrator is technical and worried.
- One is the analyst, one is the client. Do V1. Swap. Do V2.
- Eight steps. Ticket ID first. One specific ask. Get the read-back.
Big line: "This one is watched on V2: did you say 'not clean' plainly, and did you get an ask and a read-back?"
Visual: two speech bubbles, one green "clean", one amber "not clean".

SLIDE 6 — READ THE LOG FOR WHAT FAILED (Topic 9.3, part 1)
Title: "Silence in the Log Is Not Good News"
Show in monospace, two short commands:
Get-MpThreatDetection | Where-Object { -not $_.ActionSuccess }
Get-WinEvent ... | Where-Object { $_.Id -in 1118, 1119, 1002, 2001 }
Explain: "On a healthy machine these return nothing — and 'no failed actions on <host>, checked <time>' is a correct record. Write it down."
Then three log fragments in monospace, one line each:
1118  Action: Quarantine  FAILED — file is in use          <- action failed
1116  Detected ... (nothing follows)                          <- no action taken
1002  Scan stopped before completion — user cancelled        <- scan did not complete
Big line: "Two kinds of failure never say the word 'failed'."
Visual: a log page with three highlighted lines, two of them marked with a "silent" icon.

SLIDE 7 — THE FIVE KINDS OF FAILURE (Topic 9.3, part 2)
Title: "Five Kinds — the Kind Decides the Next Step"
Table (Kind / Where you see it / Next step per SOP):
1 Action failed | Event 1118 / 1119; ThreatStatusID 102-107; ActionSuccess False | Threat -> re-open the ticket -> escalate
2 Action incomplete | 1117 + "Restart required"; history says "remediation incomplete" | Get the restart done -> verify after (three proofs)
3 No action taken | 1116 with nothing after it; ThreatStatusID 1 | Threat -> scan now -> escalate if it stays
4 Scan did not complete | Event 1002; no finish time | Does not count -> re-run -> ask who cancelled
5 Threat came back | A new 1116 for the same thing after a good 1117 | Offline scan -> if again, recommend RE-IMAGE -> escalate
Add the line: "Also found in the same pass: the TOOL failing — event 2001 repeated (update failing). That goes to the vendor."
Visual: five numbered chips, kinds 3 and 4 marked "no word 'failed'".

SLIDE 8 — ACTIVITY 2: FIND THE FAILURE
Title: "Activity 2 — Eight Entries, Name the Kind"
Instructions as steps:
- In your team, read the eight log entries A-H.
- For each: success or failure? If failure — which of the five kinds, and the SOP's next step.
- Two are successes. One is the tool failing, not the action. One entry is two kinds at once.
Big line: "Read forward in time. The first 1117 can look fine — and then it comes back."
Visual: eight log-entry cards, some with a green tick, some with a red flag.

SLIDE 9 — WHO DO YOU CALL? (Topic 9.4, part 1)
Title: "Four Authorities — Pick the One Who Can DO the Thing"
Table (Authority / They own / Send them):
IT department manager | Machines, network, the change calendar | Isolate a host, restart, re-image, patch an OS, force a user restart
Information security manager | The security decision | Any threat not contained, any sign of spread, any decision above your level
Security solution / vendor | The product | Updates failing, engine faults, a suspected FALSE POSITIVE, a legitimate file quarantined
CISO | The business risk | CRITICAL only — ransomware live, data leaving, many hosts. One paragraph, within 10 minutes, usually via the security manager
Three habits: "First stop is your L2 / shift lead. One primary authority, copy the rest. Critical goes up fast."
Visual: four person icons in a row, each with a one-word label of what they own.

SLIDE 10 — THREE SITUATIONS, WORKED (Topic 9.4, part 2)
Title: "Who Gets These?"
Three cards:
SRV-BAK-02 — quarantine failed twice, process restarts itself, scan says still there -> INFORMATION SECURITY MANAGER (copy IT manager for the isolation)
payroll_calc.xlsm — the payroll macro quarantined; used safely for two years; payroll tomorrow -> SECURITY VENDOR, a false-positive case (copy security manager). Do NOT restore it yourself.
SRV-FIN-02 — files renaming to .locked right now, spreading, Finance down -> CISO within 10 minutes, one paragraph, via the security manager; IT manager isolates
Big line: "Uncontained -> security manager. Machine action -> IT manager. Tool broken or wrong -> vendor. Business on fire -> CISO, now."
Visual: three cards with an arrow to the right authority icon.

SLIDE 11 — ACTIVITY 3: WHO GETS THIS?
Title: "Activity 3 — Eight Situations, One Primary Each"
Instructions as steps:
- In your team, read the eight situations.
- For each: the PRIMARY authority, who is copied, and WHY — what does that person own that you need?
- Three were worked with you. Do all eight; three become full packs this afternoon.
Big line: "The reason is what is marked."
Visual: eight situation cards routing to four authority trays.

SLIDE 12 — THE ESCALATION PACK (Topic 9.5, part 1)
Title: "Twelve Fields — Three Decide Whether It Works"
Show the fields as a compact numbered list:
1 To + WHY them · 2 From / date / time / ticket ID · 3 One-line summary (host · what · status) · 4 What was detected (the story) · 5 WHAT THE EVIDENCE SHOWS (the log lines, attached) · 6 What was tried, and what failed — by kind · 7 Status: contained? severity, SLA clock · 8 Impact · 9 WHAT I NEED FROM YOU — a verb, with a DEADLINE · 10 My recommendation · 11 Attachments · 12 Escalation LOGGED in the ticket (time, copied to)
Highlight 5, 9 and 12.
Big line: "No evidence = an opinion. No ask = a diary entry. No deadline = it waits. No ticket update = no trail."
Visual: a form with fields 5, 9 and 12 highlighted in teal.

SLIDE 13 — A LOOK AHEAD: TIMELINE TOOLS AND WAZUH (Topic 9.5, part 2)
Title: "Finding Failures Faster — Later"
Two preview cards, both clearly marked "preview — not today":
HAYABUSA + TIMELINE EXPLORER — one command turns the whole event log into a spreadsheet timeline with every failed action flagged. Coming with the on-site lab.
WAZUH — once our server is built, every machine's 1118s in one search, with the host name beside each.
Big line: "Faster finding. Same five kinds, same four authorities, same pack."
Visual: two labelled mock-up cards with a "coming later" ribbon.

SLIDE 14 — ACTIVITY 4: BUILD THE PACK
Title: "Activity 4 — Start One Pack"
Instructions as steps:
- On your own. Pick Situation 2 (updates failing on 40 PCs) or Situation 5 (live ransomware).
- Fill fields 1-3, 5, 6 and 9 now: who and why, the summary, the evidence lines from the extract, what failed by kind, and the ask with a deadline.
- Finish the rest this afternoon.
Big line: "Verb, object, time. Not 'please advise'."
Visual: a pack form with six fields being filled.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark as the start of self-study. Keep the table.
Table (Task / Time / Hand in):
1 | Client verification records — call notes + written confirmation for V1 (clean) and V2 (not clean) | 25 min | 2 records
2 | Failed-action extract — all eight entries named by kind + the same pass on your own machine | 30 min | Annotated extract + own extract
3 | Three escalation packs — Situations 1, 2 and 5 | 45 min | 3 packs
4 | Escalation trail — update the three register rows | 15 min | 3 rows
5 | The failed-action SOP card — five kinds, where seen, next step | 15 min | 1 card
6 | Self-check one pack against your Day 3 QA checklist | 10 min | 1 self-check
7 | Reflection | 10 min | Three answers
Closing line: "Today you closed the loop. Next, Day 10: the threat report — and the first unit assessment. Bring every Day 6-9 artefact, filed."
Visual: a teal section band, the table, and a small "Day 9 of 15" progress bar.

============================================================
END OF PROMPT
============================================================
