============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 10
Report the Threat — Notify, Trace It, Name It, Write It Up
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_10_Presenter_Script.md, keyed to these same
   15 slide numbers.
6. The afternoon assessment has NO slides. Do not add any.

WHAT DAY 10 IS:
Day 10 delivers all of Element 5 of the core unit CS-ICT251101, Perform alert
reporting. PC 5.1: stakeholder/client with high and critical threats notified. 5.2: threat
activity reported by spread and lateral movement. 5.3: by egress and ingress. 5.4:
threats identified by exploitation activity and installation behaviour. The running case
SRV-BAK-02 (Day 7 alert, Day 8 verdict, Day 9 escalation) turns out to be data leaving
the building. The class notifies the owners, traces the path from WKS-311, separates
ingress from egress, maps the behaviours to MITRE ATT&CK in Navigator, and writes the
threat report. In the afternoon the whole unit is assessed (written exam, demonstration
with oral questioning, portfolio with interview). There are no slides for that.

TWO HARD CONSTRAINTS (same as Days 6-9):
- NO SIEM SERVER YET. The evidence is a printed 18-line set. Ingress and egress are read
  on the trainee's own machine with Get-NetTCPConnection. ATT&CK Navigator runs in the
  browser. The Wazuh ATT&CK module, Atomic Red Team and Hayabusa appear only on
  a PREVIEW slide.
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone.

THE FIVE TOPICS:
  10.1  Tell Them in Ten Minutes (the High / Critical notification)
  10.2  Where Did It Go? (spread and lateral movement)
  10.3  What Came In, What Went Out (ingress and egress)
  10.4  How It Got In, How It Stays (exploitation, installation, ATT&CK)
  10.5  The Threat Report (one document, every claim on a line)

DAY 10 SHAPE:
- Slides 1-13: the morning, 8:00 to 11:30 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slides 14-15: 11:30 to 11:45, the assessment briefing and the handover to the
  afternoon. The afternoon, 1:00 to 4:00 PM, is the LIVE unit assessment (not self-study).
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Ten Minutes (pairs, the N2 notification call + written, and
the N3 "do not notify" decision; observed); 2 Draw the Path (teams: hosts table + path
drawing); 3 Name It, Map It (teams map behaviours B4-B12 to ATT&CK, then each trainee
builds and exports a Navigator layer); 4 Assemble the Report (individually).

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Use a navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background) and clean sans-serif fonts. Every slide has a visual element: icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables are real tables, and commands are in monospace. No agenda, thank-you, or Q&A slide.

Day 10 is a learning morning followed by an assessment afternoon. Slides 1-13 are the live, demonstration-led morning. Slide 14 explains how the unit assessment works. Slide 15 is the handover to the afternoon assessment (1:00-4:00, live, cameras on). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. The audience is adult vocational trainees in the Philippines. English is a second language and they are complete beginners. Use short sentences, common words and a calm tone. Define every term the first time it appears: notification, stakeholder, spread, lateral movement, ingress, egress, beacon, exploitation, installation, tactic, technique, ATT&CK Navigator, layer.

Carry these rules from earlier days and use them exactly: NOT CONTAINED = THREAT (Day 7). The tool tells a STORY, and the log is the EVIDENCE (Day 8). A claim without a line is an opinion (Day 9). Today's key idea, repeated plainly: LINK WITH EVIDENCE, NOT WITH THE CLOCK.

SLIDE 1 — TITLE
Title: "Report the Threat: Notify, Trace It, Name It, Write It Up"
Subtitle: "Cyber Threat Monitoring Level I, Day 10 of 15"
Kicker: "Learn 8:00-11:45  |  Unit assessment 1:00-4:00  |  Paper evidence, your own machine, and ATT&CK Navigator in the browser"
Visual: a calm navy title slide. A single case file icon labelled "SRV-BAK-02" with four small date tags above it: "Day 7 alert", "Day 8 verdict", "Day 9 escalation", "Day 10 report".

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: From Alert to Report"
Table (Topic / What you will be able to do):
10.1 Tell Them in Ten Minutes | Notify the owner of a High or Critical threat, by voice and in writing
10.2 Where Did It Go? | Place every host as origin, confirmed, attempted or not linked, and draw the path
10.3 What Came In, What Went Out | Separate ingress from egress, with direction and bytes
10.4 How It Got In, How It Stays | Name exploitation and installation, and map them to ATT&CK
10.5 The Threat Report | Put it all in one report where every claim points to a line
Add the line: "Morning: learn it. Afternoon: show it, alone, on a new case."
Visual: five numbered topic cards, and a small clock icon labelled "1:00 assessment".

SLIDE 3 — TELL THEM IN TEN MINUTES (Topic 10.1)
Title: "Three Messages This Week, and Today's Is the Fastest"
Table (Message / To / About / When):
Verification (Day 9) | The client | A scan result | After the scan
Escalation (Day 9) | An authority | A failed action | When an action fails
NOTIFICATION (today) | The OWNER of the affected system or data | A HIGH or CRITICAL threat | Within 10 min (Critical), 1 h (High)
Below it, the seven lines of the call, numbered: 1 Who you are + ticket ID · 2 "Critical / High notification about <system>" · 3 What is known, since when · 4 What has been done · 5 What you must DO / NOT DO · 6 One ask · 7 Next update + read-back
Big line: "Fast beats complete. Only High and Critical are notified. Medium goes in the report."
Visual: a phone icon with a 10-minute timer ring.

SLIDE 4 — ACTIVITY 1: TEN MINUTES
Title: "Activity 1: Make the Notification"
Instructions as steps:
- In pairs. Case N2: J. Mendoza, Operations supervisor. WKS-311 is infected and isolated. HIGH.
- One of you is the analyst, one is Mendoza. Make the call using the seven lines. Swap.
- Write the notification together.
- Decide N3: do you notify SRV-FILE-01's owner (12 failed logons, no success)? Write your reason.
Big line: "Watched for: severity with a reason, a real DO / DO NOT, one ask, a next update, a read-back. No blaming the user."
Visual: two speech bubbles and a small checklist.

SLIDE 5 — WHERE DID IT GO? (Topic 10.2)
Title: "Every Host Gets One Word, and One Line"
Four word cards: ORIGIN (where it started inside) · CONFIRMED (evidence it is there) · ATTEMPTED (tried, and the log shows it failed) · NOT LINKED (checked, and nothing joins it)
A simple path diagram: WKS-311 (origin) --solid arrow "SMB to ADMIN$, svc_backup, 03:33"--> SRV-BAK-02 (confirmed). WKS-311 --dotted arrow "12 failed logons"--> SRV-FILE-01 (attempted). SRV-FIN-02 off to the side, grey, labelled "not linked: different account, address, file".
Big line: "Link with evidence, not with the clock."
Visual: the path diagram is the visual.

SLIDE 6 — ACTIVITY 2: DRAW THE PATH
Title: "Activity 2: Hosts Table and Path"
Instructions as steps:
- In your team, use the 18-line evidence set.
- Hosts table: every host, its word, its lines.
- Path: from, to, method, account, time, line.
- Draw it: solid arrows for what happened, dotted for what was only attempted. Put SRV-FIN-02 on the page, with the line that proves it is not linked.
Big line: "The strongest link is the same file hash on two machines."
Visual: four boxes and arrows being drawn on a whiteboard.

SLIDE 7 — WHAT CAME IN, WHAT WENT OUT (Topic 10.3, part 1)
Title: "Who Started It Decides the Direction. Bytes Decide How Serious."
Two columns:
INGRESS (in): the invoice email · 1.2 MB file pulled in from 203.0.113.45 · the tool copied into the server from inside · NO inbound from the internet
EGRESS (out): small check-ins every 5 minutes to 185.220.101.1:443 (a BEACON) · 1.8 GB out in one session (DATA LEAVING)
Show one firewall line in monospace:
04:10 ALLOW OUT 192.168.10.21 -> 185.220.101.1:443  bytes_out=1,874,329,600  bytes_in=48,212
Big line: "Small, regular, repeated = a beacon. One huge one-way connection = data leaving."
Visual: a building outline with arrows in and out, the outbound arrow much thicker.

SLIDE 8 — ON YOUR OWN MACHINE (Topic 10.3, part 2)
Title: "Read Your Own Connections"
Show in monospace:
Get-NetTCPConnection -State Established   (egress: what my machine started)
Get-NetTCPConnection -State Listen        (a door open, waiting for someone to come in)
Get-Process -Id <number>                  (which program owns it)
Table (You see / It is): My port high, remote port 443 | Egress, I started it · State Listen | A possible door in · 127.0.0.1 | Only this machine can reach it
Big line: "Only your own machine, only your own traffic. We read. We do not scan."
Visual: a laptop with outbound arrows and one open door icon.

SLIDE 9 — HOW IT GOT IN, HOW IT STAYS (Topic 10.4, part 1)
Title: "Exploitation Is How They Got In. Installation Is How They Stay."
Two columns:
EXPLOITATION: WKS-311, a user opened a macro document and it ran PowerShell (no software was broken) · SRV-BAK-02, 38 passwords guessed on a service account, then success
INSTALLATION: a scheduled task at every logon · a Windows SERVICE set to restart after every failure · the tool copied into the server first
Callout box: "Day 9 mystery solved: the service kept restarting the file, so the quarantine always failed."
Visual: a door (in) and an anchor (stay).

SLIDE 10 — ATT&CK NAVIGATOR (Topic 10.4, part 2)
Title: "Tactic = Why. Technique = How, and It Has the ID."
Show a simplified matrix strip: columns Initial Access · Execution · Persistence · Credential Access · Lateral Movement · Command and Control · Exfiltration, with one coloured box in each.
Five Navigator steps as icons: Create layer · Search the ID · Select and colour · Comment with the evidence line · Download JSON
Examples: T1566.001 Spearphishing Attachment (E01) · T1204.002 User Execution: Malicious File (E02) · T1059.001 PowerShell (E02)
Big line: "ATT&CK names it. Your line proves it. No line, no box."
Visual: the matrix strip with teal boxes.

SLIDE 11 — ACTIVITY 3: NAME IT, MAP IT
Title: "Activity 3: Twelve Behaviours, Twelve Boxes"
Instructions as steps:
- Teams, 10 minutes: behaviours B4-B12. For each, the tactic, the technique ID and name, and the evidence line. Check each ID on attack.mitre.org.
- On your own, 10 minutes: add them to your Navigator layer, colour them, comment with the line, and download the JSON to Evidence/Day_10.
Big line: "If Navigator will not load, use the paper table. The mapping is the skill."
Visual: behaviour cards flowing into matrix boxes.

SLIDE 12 — THE THREAT REPORT (Topic 10.5)
Title: "Fifteen Sections, One Rule"
Compact numbered list, with 3-10 highlighted: 1 Header · 2 Summary · 3 SEVERITY AND NOTIFICATION · 4 HOSTS AND SPREAD · 5 LATERAL MOVEMENT · 6 INGRESS · 7 EGRESS · 8 EXPLOITATION · 9 INSTALLATION · 10 ATT&CK MAPPING · 11 Timeline · 12 Containment status · 13 What we do not know yet · 14 Recommendations (verb, owner, date) · 15 Attachments
Big line: "Every claim points to a line."
Small preview strip at the bottom, clearly marked "preview, not today": Wazuh ATT&CK module · Atomic Red Team · Hayabusa, with the line "Faster finding. Same report."
Visual: a report page with sections 3-10 in teal.

SLIDE 13 — ACTIVITY 4: ASSEMBLE THE REPORT
Title: "Activity 4: Put It Together"
Instructions as steps:
- On your own. Paste in sections 3-10 from this morning.
- Write the summary (4 sentences), the timeline (8-12 events), what we do not know yet, and 3 recommendations.
- Check three sentences: does each point to a line?
Big line: "SRV-FIN-02 goes in section 4 as NOT LINKED, with its line. Not in the path."
Visual: puzzle pieces labelled with the morning's activities fitting into a report.

SLIDE 14 — HOW THE ASSESSMENT WORKS
Title: "This Afternoon: Three Methods, One Unit"
Table (Method / What / Time):
Written exam | 25 multiple-choice + 5 short answers, closed book, pass 70% | 40 min
Demonstration | A NEW case (WKS-164), open book, four parts: check alerts · check the tool with EICAR · follow up · report | 90 min
Oral questions + portfolio | In a breakout: one notification call, three questions, two questions about your own portfolio | about 6 min each
Big line: "The reason matters more than the answer. If one part is not there yet, you redo only that part, before Day 15."
Visual: three icons: a paper, a laptop, a speech bubble.

SLIDE 15 — THIS AFTERNOON
Title: "1:00 to 4:00: The Unit Assessment (Live, Cameras On)"
Mark it as the transition to the afternoon.
Checklist:
- Submit this morning's work to Evidence/Day_10 now, as it stands
- At 1:00: camera on · Handouts and Activity Packs from Days 6-10 open · Windows Security working · your Day 6 EICAR string ready
- No AI, no chat. Your own machine, your own traffic.
Closing line: "Day 7 was a failed quarantine. Today it is a finished report. This afternoon you show you can do it alone."
Visual: a teal section band, the checklist, and a small "Day 10 of 15" progress bar with "Unit 1 of 2" beneath it.

============================================================
END OF PROMPT
============================================================
