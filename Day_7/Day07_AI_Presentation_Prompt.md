============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 07
Decide, Ticket, and Check the Tool Is Working
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_7_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 07 IS:
Day 7 completes Element 1 of the core unit (PC 1.4 assess against criteria, PC 1.5
issue a ticket) and delivers all of Element 2 (PC 2.1-2.3: is the security solution
installed, operational, and able to clean or delete?). Day 6 received the alert;
Day 7 decides what it is, tickets it, and checks the tool that raised it.

TWO HARD CONSTRAINTS (same as Day 6):
- NO SIEM SERVER YET. The ticket "system" is a shared SPREADSHEET register. Every
  status check runs on the trainee's OWN Windows machine (Get-MpComputerStatus,
  Windows Security app). The Wazuh management console is shown only as a PREVIEW
  screenshot — "what you'll use once the server is built".
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone.

THE FIVE TOPICS:
  7.1  Decide What It Is (threat / detection / routine)
  7.2  Raise the Ticket
  7.3  Is the Tool Even Working? (installed, operational, up to date)
  7.4  Can It Clean Up? (the action range, proven with EICAR)
  7.5  The Management Console (local Windows Security + a Wazuh preview)

DAY 07 IS A BLENDED DAY (same hours as Days 5-6):
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Threat/Detection/Routine (team sort of 8 alerts); 2 Write the
Ticket (into the register, observed); 3 Is the Solution Working? (status checks on
own machine); 4 Read the Console (team reading of several machines' status).

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables as real tables, commands in monospace. No agenda, thank-you, or Q&A slide.

Day 07 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, complete beginners. Short sentences, common words, calm tone. Define every term the first time (SLA, quarantine, operational, console).

Three words for the triage outcome, used exactly, carried from Day 3: THREAT, DETECTION, ROUTINE. Never write "false alarm" as one of the three — a false alarm is a kind of routine. Repeat the key idea plainly: the line between THREAT and DETECTION is CONTAINMENT, not size.

SLIDE 1 — TITLE
Title: "Decide, Ticket, and Check the Tool"
Subtitle: "Cyber Threat Monitoring Level I, Day 07 of 15"
Kicker: "Live demo 8:00-11:45  |  Self-study 1:00-4:00  |  On your own machine; ticket register is a spreadsheet"
Visual: a calm navy title slide. An alert on the left flowing to three outcomes (threat/detection/routine), then to a ticket, then to a shield being checked.

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: Decide, Ticket, Check the Tool"
Table (Topic / What you will be able to do):
7.1 Decide What It Is | Say if an alert is a threat, a detection, or routine — with a reason
7.2 Raise the Ticket | Write a ticket the next person can use
7.3 Is the Tool Even Working? | Check the security tool is installed, on, and up to date
7.4 Can It Clean Up? | Read the action the tool took, and the actions it can take
7.5 The Management Console | See many machines at once (and a first look at Wazuh)
Add the line: "Yesterday you received the alert. Today you decide what it is, write it up, and check whether the tool that raised it is even working."
Visual: five numbered topic cards.

SLIDE 3 — THE THREE DECISION WORDS (Topic 7.1, part 1)
Title: "Threat, Detection, or Routine"
Three cards branching from an alert:
THREAT — dangerous and NOT contained. May still be happening. Ticket, escalate, say what you need.
DETECTION — bad, but the tool found AND handled it. Ticket, check the action worked, monitor.
ROUTINE — expected, authorised, or a false alarm. Close it with a written reason.
Big line: "Two questions for every alert: is it real and bad? And is it contained?"
Visual: three cards from one alert; an open padlock on THREAT, a closed padlock on DETECTION.

SLIDE 4 — CONTAINMENT, NOT SIZE (Topic 7.1, part 2)
Title: "What Separates a Threat from a Detection"
Big line: "The line between THREAT and DETECTION is CONTAINMENT, not size."
Two contrasting examples, side by side:
A FAILED quarantine of small malware = THREAT (found, but not stopped)
A SUCCESSFUL block of a serious attack = DETECTION (found and handled)
Add the line: "'The antivirus found it' is never the end of the story. You must check the action actually worked — that is the rest of today."
Visual: two example cards, one red (failed/uncontained), one green (handled/contained).

SLIDE 5 — ACTIVITY 1: THREAT, DETECTION, OR ROUTINE?
Title: "Activity 1 — Sort the Eight Alerts"
Instructions as steps:
- In your team, sort each of eight alerts: THREAT, DETECTION, or ROUTINE.
- Give the reason for each. The reason is what is marked.
- Watch the tricky ones — some the antivirus "found", but did it actually STOP them?
Big line: "A failed quarantine is a threat. A successful one is a detection. Check containment."
Visual: eight alert cards sorting into three trays.

SLIDE 6 — RAISE THE TICKET (Topic 7.2)
Title: "A Ticket Is Written for the Next Person"
Left — the fields (from YOUR Day 3 checklist):
Ticket ID + one-line summary · host / user · TIME it happened AND time you saw it · what the tool detected · decision + REASON · severity · what you did / did not do · what you need next, from whom
Right — "The SLA clock": "An SLA is a promise about speed. Critical = notify in 10 minutes. High = within an hour. The clock starts when you raise the ticket — so raise it promptly and stamp the time."
Big line: "Two timestamps, always. A clear reason. A specific ask. A ticket with no ask is a diary entry."
Note: "No ticket server yet — our register is a shared spreadsheet with these fields as columns."
Visual: a ticket form with the fields; a small clock for the SLA.

SLIDE 7 — ACTIVITY 2: WRITE THE TICKET
Title: "Activity 2 — Write One Real Ticket"
Instructions as steps:
- Pick an alert. Fill a full ticket in the register.
- Use your Day 3 checklist as your field list.
- Include: a decision WITH a reason, two timestamps, and a specific next-step ask.
Big line: "This one is watched. I'm looking for a reason, two times, and a real ask."
Visual: a spreadsheet register row being filled.

SLIDE 8 — IS THE TOOL INSTALLED AND OPERATIONAL? (Topic 7.3, part 1)
Title: "Before You Trust the Tool, Check the Tool"
Three questions as a checklist:
INSTALLED? — is the antivirus service present? (Get-Service WinDefend)
OPERATIONAL? — is it switched on and watching right now? (Windows Security: green ticks)
UP TO DATE? — are its signatures recent?
Big line: "Installed and operational are NOT the same thing. A tool can be installed and switched off — and a tool that is off is worse than none, because people think they are safe."
Visual: a three-step check with a shield; green tick / red cross states.

SLIDE 9 — READING THE TOOL'S STATUS (Topic 7.3, part 2)
Title: "One Command Answers All Three"
Show in monospace:
Get-MpComputerStatus | Select AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
Then a small table (Field / Healthy / A finding):
RealTimeProtectionEnabled | True | False = installed but NOT protecting -> report it
AntivirusSignatureLastUpdated | recent | 41 days ago = will miss recent threats -> report it
Add the line: "You saw this exact command on Day 5, for the baseline. Now you know why it matters."
Visual: the command, and two example outputs — one healthy (green), one with a finding (amber).

SLIDE 10 — ACTIVITY 3: IS THE SOLUTION WORKING?
Title: "Activity 3 — Check Your Own Machine"
Instructions as steps:
- Run the two checks on your OWN machine.
- Write down: installed? operational? up to date?
- If anything is off or old — that is your finding. Write it as you would report it.
Big line: "A tool that is switched off is a real finding. Reporting it is a real analyst job."
Visual: a checklist with three lights: installed, operational, updated.

SLIDE 11 — CAN IT CLEAN UP? (Topic 7.4)
Title: "Did the Tool Actually Fix It?"
Top — the action range (from the standard): FAILED · CLEAN · DELETE · QUARANTINE · BLOCKED · RE-IMAGE
Middle: "Quarantine means the file is caged, not deleted — it can be let back out if it was a mistake."
Big line: "CLEAN and QUARANTINE are successes. FAILED is not — and a failed action turns a DETECTION back into a THREAT."
Add the line: "We prove it with yesterday's EICAR detection: open Protection history and read the action."
Visual: the six actions as chips, with FAILED highlighted red and linked back to "THREAT".

SLIDE 12 — THE MANAGEMENT CONSOLE (Topic 7.5, part 1)
Title: "One Screen for Many Machines"
Explain: "Everything today was for ONE machine. A management console does the same checks for hundreds of machines at once: which have the tool, which are protected now, which are out of date, what each has found."
Add the line: "Windows Security is your own machine's little console. A big console does it for the whole company."
Visual: one machine's status card multiplying into a grid of many machines.

SLIDE 13 — A LOOK AHEAD: THE WAZUH DASHBOARD (Topic 7.5, part 2)
Title: "The Console You'll Use — Once the Server Is Built"
Content: "Our SIEM server is not set up yet. When it is, you'll use a console called Wazuh. It shows every machine: connected or not, the tool's status, and every detection — the SAME questions you asked today, for everyone at once."
Big line: "The console is not a new skill. It shows the same answers, for the whole fleet."
Visual: a labelled screenshot-style mockup of an agent list (connected / disconnected / last check-in). Mark it clearly as "preview — coming when the server is ready".

SLIDE 14 — ACTIVITY 4: READ THE CONSOLE
Title: "Activity 4 — Read Several Machines"
Instructions as steps:
- Here is the status of several machines.
- Which are healthy? Which have a problem?
- Which would you report FIRST, and why?
Big line: "Same three questions — installed, operational, up to date — read across many machines."
Visual: a small grid of machine status cards, some green, some with a red/amber flag.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark as the start of self-study. Keep the table.
Table (Task / Time / Hand in):
1 | Triage 8 alerts (criteria + severity + reason) | 35 min | 8 decisions
2 | Ticket-register rows for all 8; write 2 in full | 30 min | Register + 2 tickets
3 | Solution-status report on your own machine | 25 min | Status report
4 | Record the EICAR clean action + the action range | 20 min | Clean record
5 | Self-check 2 tickets against your Day 3 checklist | 15 min | 2 self-checks
6 | Management-console worksheet | 20 min | Worksheet
7 | Reflection | 10 min | Three answers
Closing line: "Today you finished the front of the job — decide, ticket, and check the tool. Next, Day 8: does the tool's story actually match the raw evidence?"
Visual: a teal section band, the table, and a small "Day 7 of 15" progress bar.

============================================================
END OF PROMPT
============================================================
