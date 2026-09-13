============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 06
Check for Alerts — Where They Come From, and How to Read Them
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_6_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 06 IS:
Day 6 starts the core unit CS-ICT251101 for real, with Element 1 "Check for alerts",
performance criteria 1.1-1.3: a detection alert or an incident report ARRIVES, the
analyst receives it properly, reads it, and checks it for red flags.

TWO HARD CONSTRAINTS THAT SHAPE THE DECK:
- NO SIEM SERVER YET. The class Wazuh box is not built. Everything runs on each
  trainee's OWN Windows machine, using tools already there: Event Viewer, Microsoft
  Defender, Protection history, the firewall log. Do not show a SIEM dashboard as if
  it exists. Mention Wazuh only as "the server we will use once it is set up".
- TOTAL BEGINNERS. Define every acronym in plain words the first time. Short
  sentences, common words, calm and encouraging tone.

THE FIVE TOPICS, USED AS THE DECK'S SPINE:
  6.1  The Alert Arrives
  6.2  Where Detection Alerts Come From
  6.3  How Incident Reports Arrive
  6.4  Reading Alerts on Your Own Machine
  6.5  Red Flags and Severity

DAY 06 IS A BLENDED DAY (same hours as Day 5):
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Name That Source (matching game); 2 Take the Call (intake
role-play, observed); 3 Make a Real Alert (each trainee safely triggers one EICAR
detection); 4 Red Flag or Routine? (team card sort with severity).

COLOR SCHEME (same as the rest of the course):
- Primary dark blue #1B3A5C · accent blue #2E75B6 · teal #009688
- Warning red #C0392B (sparingly) · light background #D6E4F0
- White backgrounds, sans-serif fonts.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. Do NOT use stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Keep tables as real tables and commands in monospace. No agenda, thank-you, or Q&A slide.

Day 06 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, and they are complete beginners. Short sentences, common words. Define every acronym the first time. Avoid hard words: say "on purpose", "normal", "hides", "written down". Calm, encouraging tone — never hyped, never scary.

Three words for the triage outcome, carried from Day 3: THREAT, DETECTION, ROUTINE. Never write "false alarm" as one of the three — a false alarm is a kind of routine.

Reassure clearly on the EICAR slides: the EICAR test file is HARMLESS, not a virus, made on purpose so people can test antivirus safely.

SLIDE 1 — TITLE
Title: "Check for Alerts"
Subtitle: "Where They Come From, and How to Read Them — Cyber Threat Monitoring Level I, Day 06 of 15"
Kicker: "Live demo session 8:00-11:45  |  Self-study 1:00-4:00  |  Today: on your own machine, no server needed"
Visual: a calm navy title slide. An alert bell in the centre with two arrows into it — one from a computer/tool icon, one from a person icon — showing the two ways an alert arrives.

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics, One Job: Receive the Alert"
Table (Topic / What you will be able to do):
6.1  The Alert Arrives | Know the two ways an alert reaches you, and record it
6.2  Where Alerts Come From | Name the security tools, and what each cannot see
6.3  How Incident Reports Arrive | Take a report from a person and write it down right
6.4  Reading Alerts on Your Machine | Find events in Windows, and make a safe real detection
6.5  Red Flags and Severity | Spot ransomware and viruses, and say how serious it is
Add the line: "There is no big security server yet. Today everything runs on YOUR computer, with tools already on it. That is the right way to begin."
Visual: five numbered topic cards in a row with simple icons.

SLIDE 3 — THE ALERT ARRIVES (Topic 6.1)
Title: "Every Alert Arrives One of Two Ways"
Two big cards branching from an alert bell:
A TOOL TELLS YOU — the antivirus caught a file; the firewall blocked a connection. The standard calls this a "detection alert".
A PERSON TELLS YOU — someone calls and says their files have strange names. The standard calls this an "incident report".
Big line: "Both are alerts. Both must be WRITTEN DOWN the same way every time. 'I remember someone mentioned it' is not receiving an alert."
Add the line: "This is step one of the six-step lifecycle from Day 3. Today and tomorrow, we live inside step one."
Visual: an alert bell with two arrows in — a tool icon and a person icon.

SLIDE 4 — WHERE ALERTS COME FROM (Topic 6.2, part 1)
Title: "The Tools That Raise Alerts"
Table (Tool / Full name / What it watches):
SIEM | Security Information & Event Management | All the logs, in one place (the server we don't have yet)
AV | Antivirus | Files and programs on a machine
Firewall | — | Traffic in and out of the network
WAF | Web Application Firewall | Requests coming to a website
DLP | Data Loss Prevention | Sensitive data trying to leave
EDR | Endpoint Detection & Response | Behaviour on a computer (an advanced antivirus)
NDR | Network Detection & Response | Suspicious patterns on the network
Add the line: "You do not operate these today. You need to know which tool an alert came from — because that tells you what it can, and cannot, see."
Visual: a row of labelled tool icons; a small SIEM "funnel" collecting the others.

SLIDE 5 — EVERY TOOL HAS A BLIND SPOT (Topic 6.2, part 2)
Title: "What Each Tool CANNOT See"
Table (Tool / It cannot see):
Antivirus | A brand-new threat nobody has caught yet ("0 detections" is not "safe")
Firewall | What happens inside a connection it allowed
WAF | An attack that does not go through the web app
DLP | Data it was never told to watch for
EDR | A machine with no agent installed
NDR | Encrypted traffic it cannot read
Big line: "A tool can be right about the world and still miss what matters on your network. Just like the lookup websites on Day 3."
Visual: keep as a table; give the "cannot see" column visual weight.

SLIDE 6 — ACTIVITY 1: NAME THAT SOURCE
Title: "Activity 1 — Name That Source"
Instructions as steps:
- I show you an alert. You answer in the chat: which tool raised it?
- Then tell me ONE thing that tool cannot see.
- A few seconds each. We discuss the tricky ones.
Add the line: "Half your alerts come from tools like these. The other half come from people — that's next."
Visual: a game-show card with a short timer.

SLIDE 7 — HOW INCIDENT REPORTS ARRIVE (Topic 6.3)
Title: "When a Person Reports an Incident"
Top — the six channels as icons: PHONE · WALK-IN · EMAIL · SMS · CHAT · VIDEO CALL
Bottom — the five facts to capture, as a checklist:
WHO is reporting, and their callback number
WHAT they saw, in their own words
WHEN it happened, and when they noticed
WHICH machine, account, or system
WHAT they have already done
Big line: "People never give you all five. Record what they said, then gently ASK for what is missing. Stay calm — a frightened caller calms down when you are calm."
Add the line: "The callback number is the one fact you cannot get back later. Always ask for it."
Visual: six channel icons on top, a five-item intake checklist below.

SLIDE 8 — ACTIVITY 2: TAKE THE CALL
Title: "Activity 2 — Take the Call"
Instructions as steps:
- I will play people reporting incidents — a panicked caller, a walk-in, a manager.
- Fill in your intake form as they speak.
- Each report is missing ONE fact. Notice it, and ask for it — calmly.
Big line: "This one is watched. I am looking for two things: did you capture the core facts, and did you catch the missing one and ask?"
Visual: a headset icon and a blank intake form with five fields.

SLIDE 9 — READING ALERTS ON YOUR OWN MACHINE (Topic 6.4)
Title: "Where Windows Writes Down Security Events"
Table (Place / What is in it / How to open):
Event Viewer | Windows logs, incl. the Windows Defender / Operational log | Type "Event Viewer"
Protection history | Every threat Defender found, and what it did | Windows Security app -> Virus & threat protection
Firewall log | Blocked/allowed connections (if logging is on) | A text file at %systemroot%\system32\LogFiles\Firewall\pfirewall.log
Big line: "Event Viewer looks overwhelming — it is, for everyone. Nobody reads it all. You filter to what matters. Protection history is the friendly view; look there first."
Visual: three panels — an Event Viewer tree, the Protection history screen, a log file icon.

SLIDE 10 — MAKE A REAL ALERT, SAFELY (Topic 6.4, the EICAR demo)
Title: "The EICAR Test File — a Safe, Real Detection"
Reassurance box (teal, calm): "EICAR is NOT a virus. It has never been a virus. It is a harmless line of text that every antivirus agreed to treat as dangerous, so people can test their antivirus safely. Nothing here can harm your computer."
Then three steps with icons:
1. Paste the EICAR text into Notepad and save it as eicar_test.txt
2. The antivirus catches it instantly — a pop-up, or the file disappears
3. Open Protection history and read WHAT it found, WHEN, and the ACTION it took
Big line: "Those three things — what, when, action — are your detection record."
Visual: a three-step flow; a friendly shield icon, not an alarming one. Show the EICAR string in monospace.

SLIDE 11 — ACTIVITY 3: MAKE A REAL ALERT
Title: "Activity 3 — Make Your Own Detection"
Instructions as steps:
- Paste the EICAR text (in your Activity Pack) into Notepad and save it.
- Find your detection in Protection history.
- Write down the three things: what was found, when, and the action taken.
Big line: "If your machine blocks the file from saving at all — that block IS the detection. Read it in Protection history. Nobody can break anything."
Visual: a checklist: paste, save, find it, record the three things.

SLIDE 12 — RED FLAGS (Topic 6.5, part 1)
Title: "Two Red Flags to Know: Ransomware and Viruses"
Two columns of indicators:
RANSOMWARE — many files renamed at once (e.g. .locked) · a ransom note in every folder · files won't open · backups deleted · a sudden burst of file changes
VIRUS / PE INFECTION — a program file (.exe, .dll) flagged by antivirus · a process running from the wrong place · a name pretending to be a system file (svhost32.exe) · a file that copies itself
Add the line: "Red flags are patterns you can learn. A fake system-file name looks wrong — you spotted exactly that on Day 5. (PE just means a Windows program file.)"
Visual: two columns with clear icons; keep it calm, not alarming.

SLIDE 13 — HOW SERIOUS IS IT? (Topic 6.5, part 2)
Title: "Severity — How Fast, How Loud"
Table (Band / Meaning / Example):
CRITICAL | Business-stopping or spreading now | Ransomware active; a server down
HIGH | Serious, not yet contained | Confirmed malware still running
MEDIUM | Real, but handled or single | One malware file quarantined
LOW | Note it, no rush | A blocked ad; an EICAR test
Big line: "The tool gives a severity. That's your START, not your answer. Adjust for two things: is it contained, and whose machine is it? Then write down WHY."
Add the line: "Severity is about how fast and how loud — not about whether it is real."
Visual: a four-step severity ladder, Critical at top.

SLIDE 14 — ACTIVITY 4: RED FLAG OR ROUTINE?
Title: "Activity 4 — Sort the Cards"
Instructions as steps:
- In your team, sort each indicator card: RANSOMWARE, VIRUS, or ROUTINE.
- Give each one a severity band: Critical, High, Medium, or Low.
- Write the REASON for your band. The reason is what is marked, not the band.
Big line: "The same detection can be Medium on a training PC and High on the finance server. Say why."
Visual: cards being sorted into three labelled trays, with a small severity dial.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark this slide as the start of the self-study section. Keep the task table.
Table (Task / Time / Hand in):
1 | Process 6 incident reports onto intake forms | 30 min | 6 intake forms
2 | Make and record your own detection | 25 min | 1 detection record
3 | Find 3 real events in your logs | 25 min | Event log worksheet
4 | Build your sources reference (7 tools + blind spots) | 20 min | Sources table
5 | Write two red-flag cards (ransomware, virus) | 25 min | 2 indicator cards
6 | Fill in the severity mapping sheet | 20 min | Severity sheet
7 | Reflection | 10 min | Three answers
Closing line: "Today you received alerts the two ways they really arrive, and made a real detection on your own machine — no server, no danger. Next, Day 7: decide what each alert IS, write the ticket, and check the security tool is actually working."
Visual: a teal section band, then the table, and a small "Day 6 of 15" progress bar.

============================================================
END OF PROMPT
============================================================
