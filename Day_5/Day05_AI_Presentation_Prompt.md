============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 05
Underneath the Alert — the Machine, the Wire, the Web and the Script
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_5_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 05 NOW IS:
Day 5 is the day the tools stop being magic. On Day 3 a trainee could look up the
clue but stopped at the browser — when WKS-311 was connecting to a bad address on
port 443, nobody could name the PROCESS behind it. Day 5 closes that gap. An alert
points at four things — a process, an address and port, a web request, and a
script — and Day 5 teaches the analyst to read all four, on their own machine.

Day 5 ALSO carries the whole of the old Day 4 (there is no separate Day 4 session):
the common unit ICT311203 Perform Computer Operations, delivered as "prepare,
baseline and maintain an analyst workstation". Nothing is dropped.

  Reading the machine - processes, services, tasks   = CS-ICT251101 knowledge 1.1
  Preparing and baselining the workstation           = ICT311203 (all five elements)
  Reading addresses, ports, NAT, a connection's owner = CS-ICT251101 knowledge 1.4
  Reading a web request and an access log            = CS-ICT251101 knowledge 1.2
  Reading a script without running it                = CS-ICT251101 knowledge 1.3
  Never sending your own IP / never running a script = 400311106 LO4 reprised
  Registering the baseline, self-checking the ticket = 400311106 LO5 / ICT315202 LO2

THE FIVE TOPICS, USED AS THE DECK'S SPINE:
  5.1  The Machine Underneath
  5.2  Preparing and Maintaining the Analyst Workstation
  5.3  The Wire
  5.4  The Web Request
  5.5  Reading Scripts for Triage

DAY 05 IS A BLENDED DAY (note the hours differ from Day 3):
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 14 clearly as the transition to the afternoon self-study.

THE DAY IS BUILT AROUND SEVEN FOLLOW-ALONG DEMOS AND FOUR ACTIVITIES:
  Demos: inside the machine; build the baseline; your address and the wire; who owns
  this connection; NAT and the localhost-only scan; a web request end to end; the
  parser. The class runs each command on their own machine as the trainer does.
  1. "Where Does It Live?"    — a fast decision game, 10 items, normal vs suspicious
  2. "Follow the Connection"  — trace your own connection to its process, report in clues
  3. "Access-Log Detective"   — a team reconstructs a web attack from 40 log lines
  4. "Explain This Script"    — pairs read three scripts and predict them, running none

COLOR SCHEME (same as the rest of the course):
- Primary dark blue: #1B3A5C
- Accent blue: #2E75B6
- Accent teal: #009688
- Warning red (use sparingly): #C0392B
- Light background: #D6E4F0
- White backgrounds with blue accents, sans-serif fonts.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Use a navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Use clean sans-serif fonts. Every slide must include a visual element — icons, simple infographics, or diagrams. Do NOT use stock photos of hackers, hoodies, padlocks, or binary code. Format 16:9 widescreen. Keep all tables as real tables, and show all commands in a monospace font. Do not add an agenda slide, a thank-you slide, or a Q&A slide.

Day 05 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 14 clearly as the transition.

IMPORTANT — WRITE IN SIMPLE ENGLISH. The audience is adult vocational trainees in the Philippines. English is their second language. Use short sentences and common words. Avoid difficult words such as "deliberate", "legitimate", "reconnaissance", "anonymising". Say "on purpose", "normal / real", "looking around", "hides who you are" instead. Keep the tone plain and professional, never hyped.

Four slides are ACTIVITY INSTRUCTIONS, not lectures: slides 4, 8, 11 and 13. Those must read as clear steps a trainee can follow without the trainer repeating them.

Three words are used exactly and consistently for the triage outcome, carried over from Day 3: THREAT, DETECTION, ROUTINE. Never write "false alarm" as one of the three — a false alarm is one kind of routine. The line between threat and detection is CONTAINMENT, not size.

Two safety rules appear in the deck and must be worded plainly: "Read a suspicious script. Never run it." and "Scan only a machine you are allowed to scan — today, only your own."

SLIDE 1 — TITLE
Title: "Underneath the Alert"
Subtitle: "The Machine, the Wire, the Web and the Script — Cyber Threat Monitoring Level I, Day 05 of 15"
Kicker: "Live demo session 8:00-11:45  |  Self-study 1:00-4:00"
Visual: a calm navy title slide. Show an alert icon at the top, and four things it points at below it — a gear (process), a network plug (address/port), a globe (web request), and a document with code (script).

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics, One Job"
Table (Topic / What you will be able to do):
5.1  The Machine Underneath | List what runs on a machine, and say where files should live
5.2  Preparing the Analyst Workstation | Build, baseline and maintain your own workstation
5.3  The Wire | Read an address, a port, and a connection back to its program
5.4  The Web Request | Read a web log and tell the story of what happened
5.5  Reading Scripts for Triage | Read a script and say what it does — without running it
Add the line: "On Day 3 you looked up the clue, but you stopped at the browser. Today you read the machine, the wire, the web and the script underneath the alert."
Visual: five numbered topic cards in a row, each with a simple icon.

SLIDE 3 — THE MACHINE UNDERNEATH (Topic 5.1)
Title: "What Runs on a Machine — and Where It Should Live"
Top half — four blocks, each with a command in monospace:
PROCESSES — running programs. Get-Process
SERVICES — background programs, often from boot. Get-Service
SCHEDULED TASKS — jobs set to run at a time or an event. Get-ScheduledTask
STARTUP / AUTORUNS — programs that start by themselves. Autoruns
Bottom half — a small "Location is evidence" table (File / Lives in):
svchost.exe / lsass.exe | C:\Windows\System32
explorer.exe | C:\Windows
Big line: "A name can be faked in seconds. A location is harder. On Day 3, svhost32.exe in C:\Users\Public was a red flag BEFORE we looked anything up — wrong name, wrong place."
Add the line: "You cannot spot the strange until you know the normal. Services and scheduled tasks are favourite hiding places, because both survive a reboot."
Visual: four labelled tiles on top; below, one green "real" file and one red fake with its wrong path highlighted. Small note: macOS and Ubuntu do the same jobs with different commands.

SLIDE 4 — ACTIVITY 1: WHERE DOES IT LIVE?
Title: "Activity 1 — Where Does It Live?"
This slide is instructions for a game. Write it as steps:
- I will show you a file: its name and where it is running from.
- Answer in the chat: NORMAL or SUSPICIOUS.
- A few seconds each. Be ready to say WHY in one line.
- We go back and discuss the tricky ones.
Add the line: "Some look easy and are not. A digit one is not the letter L. Unfamiliar is not the same as bad — you installed Python this morning, remember."
Visual: a simple game-show card with a short timer.

SLIDE 5 — BUILD AND BASELINE YOUR WORKSTATION (Topic 5.2)
Title: "An Analyst Builds Their Own Instrument"
Left — the five steps of the computer-operations unit as one workflow:
PLAN & PREPARE - decide what the workstation needs, set it up safely
INPUT - record the build details
ACCESS - open the right tool for the job
PRODUCE & TRANSFER - export a baseline, copy it, verify the copy
MAINTAIN - disk space, backups, antivirus on and up to date
Right — "What is a baseline?" box: "A snapshot of a healthy machine, taken now, so that later — when something new appears — you have something to compare against."
Add the line: "A copy you have not checked is not a backup. It is a hope. Hash it, copy it, hash the copy, compare."
Visual: a five-step workflow on the left, a camera/snapshot icon on the right.

SLIDE 6 — READING THE WIRE: ADDRESSES AND PORTS (Topic 5.3)
Title: "An Address Says WHERE. A Port Says WHAT."
Top — a small table (Range / Meaning):
10.x · 172.16-31.x · 192.168.x | Private — inside a network
127.0.0.1 | This machine — "localhost"
Anything else | Public — out on the internet
Bottom — common ports in monospace, two rows:
22 SSH · 53 DNS · 80 HTTP · 443 HTTPS (encrypted web)
25/587 SMTP · 445 SMB · 3389 RDP · 3306 MySQL
Big line: "On Day 3, 'port 443' told us the traffic was encrypted — that is WHY the address was all we could read."
Add the line: "A private address is inside the building; the internet cannot reach it directly. NAT is the translation the router does so many private devices share one public address."
Visual: on the left a house (private) through a router (NAT) to a cloud (internet); on the right a host with numbered doors (ports).

SLIDE 7 — WHO OWNS THIS CONNECTION
Title: "The Command That Finishes the WKS-311 Ticket"
Show the commands in monospace:
netstat -ano | findstr ESTABLISHED      (the last column is the PID)
tasklist /fi "pid eq 6820"              (turn the PID into a name)
Then the one-line PowerShell join (small monospace):
Get-NetTCPConnection -State Established | Select LocalPort, RemoteAddress, RemotePort, @{n='Process';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
Big line: "Address, port, AND the program that owns the connection — in one line. Run this on WKS-311 and you get svhost32.exe. That is the process we could not name on Day 3."
Visual: a connection line with a magnifying glass landing on a "process" tag at the end.

SLIDE 8 — ACTIVITY 2: FOLLOW THE CONNECTION
Title: "Activity 2 — Follow Your Own Connection"
This slide is instructions. Write it as steps:
- Open a website, so you have live connections.
- Run the connection command. Pick ONE connection.
- Find: which program owns it, what port, and is the far address public or private?
- Tell your partner about it — using CLUES ONLY. The process, the port, public or private.
Big red line: "Do NOT say your own IP address out loud. That address identifies your machine. Describe it in clues — exactly like Day 3: look up the clue, never send the content."
Add the line: "This is watched and recorded. Two things: did you tie the connection to its program yourself, and did you keep your own address private?"
Visual: two people icons, one describing a connection to the other using small clue-tags, with the IP address crossed out.

SLIDE 9 — NAT, PORT FORWARDING, AND THE ONE MACHINE YOU MAY SCAN
Title: "One Machine You Are Allowed to Scan: Your Own"
Top — two short blocks:
NAT — many private devices share one public address going out. Automatic and safe.
PORT FORWARDING — a hole made on purpose, sending one public port to one inside machine. It is how inside servers get exposed. A network review looks here first.
Big red line: "Scanning any machine that is not yours, without written permission, is illegal under RA 10175, the Cybercrime Prevention Act. Today we scan only 127.0.0.1 — this machine."
Add the line: "The full lab-subnet scan needs the real lab and a signed permission. It waits for our first day on site."
Visual: a router showing outward NAT and one inward port-forward arrow; a small "127.0.0.1 only" badge.

SLIDE 10 — THE WEB REQUEST AND ITS LOG (Topic 5.4)
Title: "One Request, and What the Server Wrote Down"
Top — the request path as a horizontal flow:
BROWSER → DNS → [ WAF / proxy ] → WEB SERVER → APPLICATION → back
Middle — one log line, labelled underneath in monospace:
203.0.113.45 - - [.../09:20:11] "POST /wp-login.php HTTP/1.1" 200 6712 "-" "python-requests"
who | when | method+path | result | size | the tool
Bottom — a compact status-code table (Code / Meaning):
200 OK — served it (NOT the same as "fine")  ·  302 redirect (after login often = success)
403 forbidden — blocked, often the WAF  ·  404 not found — a BURST from one address = a scanner
Big line: "The most dangerous line in a log is often a 200, not a 403. A 200 means it WORKED."
Visual: request flow on top with the WAF highlighted; one labelled log line and the small code table below.

SLIDE 11 — ACTIVITY 3: ACCESS-LOG DETECTIVE
Title: "Activity 3 — Tell the Story in the Log"
This slide is instructions. Write it as steps:
- Your team gets 40 lines of a website's log. Six addresses appear.
- For each address: is it a normal visitor, a scanner, or the attacker? Give one line of proof.
- Put the attack in order, using the timestamps.
- Then: which single line is the WORST thing in the log? And is this THREAT, DETECTION, or ROUTINE?
Big line: "The blocked attacks (403) are the noise. Look for the request that SUCCEEDED (200). That is the fire."
Visual: a magnifying glass over a block of log lines, with three coloured tags: visitor, scanner, attacker.

SLIDE 12 — READING A SCRIPT (Topic 5.5)
Title: "A Script Is Just Instructions You Can Read"
Left — "A good script (today's parser)": opens a file, matches each line, counts status codes and addresses, prints. It touches nothing and sends nothing out.
Right — "What a bad script does": reaches out to the internet to fetch more code · hides itself with encoding · runs whatever it fetched.
Big red line: "Read a suspicious script. NEVER run it. Running it is the incident. Reading it is enough to escalate."
Add the line: "'It ran fine and found nothing' is not 'there is nothing.' Scripts have bugs. Check the silence."
Visual: two script cards side by side — one green (reads a file), one red (fetches and runs code from the internet).

SLIDE 13 — ACTIVITY 4: EXPLAIN THIS SCRIPT, DON'T RUN IT
Title: "Activity 4 — Read Three Scripts. Run None."
This slide is instructions. Write it as steps:
- In pairs, read three short scripts.
- For each: What does it do? Does it touch the internet? Would you RUN it, or ESCALATE it?
- You will not run any of them. Reading is the job.
Big line: "One is safe. One fetches and runs code from the internet — escalate it. One has a bug and reports zero problems in a log full of them."
Visual: three script cards labelled A, B, C, with a big "DO NOT RUN" stamp across all three.

SLIDE 14 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark this slide as the start of the self-study section. Keep the task table on this slide.
Table (Task / Time / Hand in):
1 | Workstation build checklist | 25 min | Signed checklist
2 | Capture and register your baseline | 25 min | 4 CSVs, hashed and named
3 | Maintain and back up | 15 min | Two matching hashes
4 | Annotate five of your own connections | 25 min | Annotated capture
5 | Draw your network's port map | 20 min | Diagram
6 | Read the web log | 25 min | Six answers
7 | Extend the parser (count 404s per IP) | 25 min | Script + output
8 | Re-ticket WKS-311 with the process named | 5 min | Ticket + self-check
9 | Reflection | 5 min | Three answers
Add the line: "Task 8 closes the loop: re-write the WKS-311 ticket with the program you can finally name, and check it against the QA checklist you wrote on Day 3."
Visual: a teal section band, then the table.

SLIDE 15 — WHAT YOU CAN DO NOW
Title: "What You Can Do Now"
Checklist with tick marks:
- List what runs on a machine, with a command
- Say where a Windows system file SHOULD live, and treat a wrong place as evidence
- Build and baseline a workstation, and register the baseline as evidence
- Tell a private address from a public one, and say what NAT does
- Tie a live connection to the program that owns it
- Read a web log line and reconstruct a simple attack
- Read a script and predict it — without running it
Closing line: "Two rules to carry out the door: read it, don't run it — and scan only what is yours. Next, Day 6: the SIEM. You will enrol a Wazuh agent, so bring a machine you can install software on."
Visual: a completed checklist and a small "Day 5 of 15" progress bar.

============================================================
END OF PROMPT
============================================================
