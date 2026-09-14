============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 01
THE SOP PACK — The Written Procedures That Run the Desk
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is intentionally short: 12 slides.

WHAT THIS DECK IS FOR:
The SOP Pack is the single most reused document in the whole 15 days. Trainees
open it on Day 1, again on Days 6 to 10 when they triage real alerts, and again on
Day 15 in the assessment.

Send this deck with the afternoon pack. Trainees read it before they start the SOP
activity. It teaches the three documents; the activity makes them use all three.

COLOR SCHEME:
- Primary dark blue: #1B3A5C
- Accent blue: #2E75B6
- Accent teal: #009688
- Warning red (use sparingly): #C0392B
- White backgrounds with blue accents, sans-serif fonts.

============================================================
PROMPT (12 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 12 slides. Use a navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Use clean sans-serif fonts. Every slide must include a visual element — icons, simple infographics, or diagrams. Do NOT use stock photos of hackers, hoodies, padlocks, or binary code. Format 16:9 widescreen. Keep all tables as real tables. Keep text short and readable.

IMPORTANT: This deck is read by a student working ALONE, with no teacher present. Write it as a direct explanation to that student, using "you". Audience is adult vocational trainees in the Philippines with mixed technical background — most have never worked in an office that has written procedures. Keep the tone plain and practical, never legalistic.

SLIDE 1 — TITLE
Title: "The Three Documents That Run Your Desk"
Subtitle: "The SOP Pack — Cyber Threat Monitoring Level I"
Kicker: "You will use this on Day 1, on Days 6 to 10, and in your final assessment. Keep it."
Visual: three stacked document icons on a navy ground.

SLIDE 2 — WHY WRITTEN PROCEDURES EXIST
Title: "Why Anyone Writes This Down"
Big statement in the middle of the slide:
  "An SOP is the answer to 'why did you do that?'
   when somebody asks you six months later."
Two contrasting boxes below:
- YOU FOLLOWED THE SOP and the outcome was bad → that is a PROCESS problem. The company fixes the process.
- YOU IGNORED THE SOP and the outcome was bad → that is YOUR problem.
Add the line: "This is not about obedience. A written procedure is the thing that protects you when a decision you made at 2am gets reviewed in daylight by people who were asleep at the time."
Visual: two contrasting outcome cards, one teal, one muted red.

SLIDE 3 — YOUR THREE DOCUMENTS
Title: "Three Documents, Three Jobs"
Open with a definition box, prominent: "SOP = STANDARD OPERATING PROCEDURE — a written instruction for how a job is done, the same way, every time, by whoever is on shift."
Table with three columns (Document, What it tells you, When you open it):
SOP-SOC-001 Alert Intake | Exactly what to do when an alert arrives, step by step | Every alert
SOP-SOC-002 Severity Matrix | How to rank it: Critical, High, Medium, Low | Every alert
SOP-SOC-003 Escalation Matrix | Who to contact, how, and how fast | Every escalation
Add the line: "Plus three sample notices — a vendor advisory, a change notice, and a client SLA notice. Those tell you when the rules change."
Visual: three labelled document cards in a row.

SLIDE 4 — THE SMALL WORDS ARE THE IMPORTANT ONES
Title: "Read the Verbs, Not the Sentences"
Table (Word / What it means for you):
  shall / must | Mandatory. You have no choice.
  should | Expected. If you skip it, you must be able to justify why.
  may | Your judgement — and usually only if you write it down.
  shall not | You have no authority. This is the edge of your role.
  within X minutes | A clock is running. Know exactly when it starts.
Example to show below the table:
  "The analyst MAY close a Low alert, provided the assessment is documented."
Add the line: "Read quickly, you hear 'I can close Low alerts.' Read properly, the permission has a price. Close it without writing anything and you did not use your judgement — you broke the procedure."
Visual: a highlighter pen marking words in a paragraph.

SLIDE 5 — THE ALERT INTAKE SOP
Title: "SOP-SOC-001 — What You Do With Every Alert"
Show the eight steps as a compact numbered flow:
3.1 SHALL record 4 fields within 5 minutes of receipt
3.2 SHALL assess severity BEFORE anything else
3.3 MUST notify client (Critical/High) within 15 min of assessment
3.4 SHOULD check for a Change Notice — SHALL record the reference if one applies
3.5 MAY close a Low, provided it is documented
3.6 SHALL NOT take containment action — ever
3.7 SHALL record every action, the time, and who authorised it
3.8 SHALL complete a handover log at end of shift
Highlight 3.6 in red.
Visual: a vertical 8-step flow, step 3.6 marked with a stop icon.

SLIDE 6 — THE CLOCK THAT CATCHES EVERYBODY
Title: "When Does the Clock Start?"
Show a timeline across the slide:
  22:00 — alert arrives (RECEIPT)
  22:20 — you finish assessing it as High (ASSESSMENT)
  22:35 — client notification deadline
Big statement: "The 15 minutes runs from ASSESSMENT, not from receipt."
Add the line: "Almost every new analyst reads section 3.3 and starts the clock at 22:00. It is the single most common cause of missed deadlines in real security operations centres. Read 3.3 twice."
Second note: "Being late on step 3.1 does not move the 3.3 deadline. They are two separate clocks."
Visual: a horizontal timeline with the two clocks drawn separately.

SLIDE 7 — THE SEVERITY MATRIX
Title: "SOP-SOC-002 — How Bad Is It?"
Table with four rows (Severity, What it means, Notify client, Escalate to):
CRITICAL | Active harm happening now, or about to | Within 10 min | L2 AND SOC Manager, immediately
HIGH | Confirmed malicious, contained or not yet spreading | Within 15 min | L2
MEDIUM | Suspicious, needs checking, no confirmed harm | Within 4 hours | L2 if unresolved at end of shift
LOW | Routine, expected, or the tool already handled it | End of shift summary | Nobody — you may close it
Add the line: "Judge impact and certainty together."
Visual: a four-level severity ladder, colour-graded.

SLIDE 8 — THE FOUR RULES THAT BEAT THE TABLE
Title: "Four Rules That Override the Matrix"
Numbered list with icons:
1. Anything on a domain controller, backup server, or finance system goes UP one level.
2. Anything a client reports BY PHONE is at least Medium until assessed — a human bothered to call.
3. Stuck between two levels? Take the higher one and write down why.
4. Uncertainty is NOT Low. "I don't know what this is" is Medium at minimum.
Big closing line: "Nobody has ever been disciplined for over-assessing with a documented reason."
Visual: four rule cards, teal accent.

SLIDE 9 — THE ESCALATION MATRIX
Title: "SOP-SOC-003 — Who Do You Call?"
Table (Severity, Contact, How, Within, If nobody answers):
CRITICAL | L2, THEN SOC Manager | Phone, then ticket | Immediately | Call the next name on the on-call list. Keep calling. Never leave a Critical unowned.
HIGH | L2 on shift | Ticket, then chat | 15 min | SOC Manager after 30 min of silence
MEDIUM | L2 on shift | Ticket | End of shift | Carry it in the handover
LOW | Nobody | Ticket only | — | —
Add the line: "You never contact the CISO directly. That goes through the SOC Manager, always."
Visual: an escalation ladder with the CISO marked as out of reach for L1.

SLIDE 10 — WHAT GOES IN AN ESCALATION
Title: "The Six Things — Every Escalation, No Exceptions"
Numbered list:
1. Ticket number
2. What was detected — in one sentence
3. Affected hosts and users — exact names, spelled out
4. What you have already checked — including whether a Change Notice covers it
5. Your severity assessment, and why
6. What you are asking for — a decision, an action, or just awareness
Big closing line in a highlighted box:
  "An escalation without number 6 is a complaint, not an escalation."
Visual: a six-item checklist card, item 6 emphasised.

SLIDE 11 — WHEN DOCUMENTS DISAGREE
Title: "Three Notices That Change the Rules"
Three columns:
- VENDOR ADVISORY: "This tool is giving false positives." Changes how you treat a detection type.
- CHANGE NOTICE: "This system will be worked on at this time." Scheduled change is the number one cause of false alerts.
- CLIENT SLA NOTICE: "This client has different timings." Can override the SOP — for that client only.
Big statement below:
  "When two documents conflict, do not pick the stricter one, the newer one, or the one you prefer.
   Check whether the notice HAS THE AUTHORITY to override. A document that can override says so."
Add the line: "And a notice tells you what it does NOT cover just as clearly as what it does. If it lists four Manila servers, a Cebu server going down is not covered."
Visual: three document cards, with an arrow from the SLA notice overriding one line of the SOP.

SLIDE 12 — YOUR ACTIVITY
Title: "Now Use All Three — The Night Shift"
Explain the activity:
- Eight alerts arrive across one night shift
- For each one you decide: the severity, why, who you notify and by when, and who you escalate to
- You will need all three documents open, plus the three notices
- About 45 minutes
Add the line: "This is the actual job. Not a quiz about the documents — the thing analysts do every night, using the documents. Get it wrong here, where it costs nothing."
Closing line: "Answers are discussed on Day 2. Bring your worksheet."
Visual: a shift clock from 21:00 to 05:00 with eight alert markers along it.

============================================================
END OF PROMPT
============================================================
