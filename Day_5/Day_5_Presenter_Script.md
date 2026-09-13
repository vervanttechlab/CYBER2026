# DAY 5 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 5 deck — 15 slides

---

## HOW TO USE THIS SCRIPT

Grey quote blocks are the words. Say them in your own voice once you are comfortable. *(Italics in brackets are notes for you — never read them out.)* The times are the same as the Instructor Guide timetable.

Day 5 is **follow-along**. After most slides you switch to your terminal or browser and run the demonstration; the class runs it too. The demo *steps* are in `Day_5_Demonstration_Guide.md` — this script tells you what to say **around** them, and cues when to switch.

**Cut order if you are running late** is at the end of this file.

---

## THE MORNING AT A GLANCE

| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 3 |
| 2 | 8:10 | Five topics |
| 3 | 8:15 | Topic 5.1 → Demo 1 |
| 4 | 8:35 | Activity 1 |
| 5 | 8:47 | Topic 5.2 → Demo 2 |
| 6 | 9:05 | Topic 5.3 part 1 → Demo 3 |
| 7 | 9:25 | Demo 4 |
| 8 | 9:40 | Activity 2 |
| — | 10:05 | Break |
| 9 | 10:15 | Topic 5.3 part 2 → Demo 5 |
| 10 | 10:25 | Topic 5.4 → Demo 6 |
| 11 | 10:40 | Activity 3 |
| 12 | 11:05 | Topic 5.5 → Demo 7 |
| 13 | 11:15 | Activity 4 |
| 14 | 11:33 | Afternoon brief |
| 15 | 11:40 | Close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes

> "Good morning. Day 5. On Day 3 you took an alert, looked up the clue, decided threat, detection or routine, and wrote a ticket. You were good at it. But we hit a wall. Remember the WKS-311 alert — the workstation connecting to a bad address on port 443 in the middle of the night?"

*(Take answers.)*

> "You looked up the address. But there was a question none of us could answer: **which program** was making that connection? We had the address. We did not have the process. That hole is where today starts."

> "An alert points at four things: a **process**, an **address and a port**, a **web request**, and a **script**. Today you learn to read all four — on your own machine, with real commands. And you learn to build and baseline the workstation you read them on."

> "Two rules for the whole day, and I mean them: **read a suspicious script, never run it**, and **scan only a machine you are allowed to scan** — which today means your own, and nothing else. Both of those are not just etiquette. One of them is the law."

*(Collect outstanding Day 1–3 evidence now. Announce role rotation.)*

---

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes

> "Five topics today, and they are printed at the front of your handout in these exact words. 5.1, the machine underneath — what runs, and where things live. 5.2, preparing and baselining your workstation. 5.3, the wire — addresses and ports. 5.4, the web request. 5.5, reading scripts."

> "This is a hands-on day. I will talk for less than an hour and a half all morning. The rest of the time, you are typing the same commands I am. Your screen will not look exactly like mine — different machine, different connections. That is correct. The shape is what matters."

---

# SLIDE 3 — TOPIC 5.1: THE MACHINE UNDERNEATH → DEMO 1
### 8:15 – 8:35 · 20 minutes

> "You cannot spot the abnormal until you know the normal. Four things run on a machine: processes, services, scheduled tasks, and the programs that start themselves. Let me show you all four on my machine — and you follow along on yours."

*(Switch to PowerShell. Run **Demonstration 1** from the Demo Guide — `Get-Process` with the path column, find the real svchost, list services and scheduled tasks, show autoruns.)*

> "The most important column is the path — where each program lives. On Day 3, `svhost32.exe` in `C:\Users\Public` was suspicious before we looked anything up. Now you know why: the real svchost lives in System32, always. A name can be faked in seconds. A location is much harder to fake — that is the bottom half of this slide, and it is the whole idea: location is evidence."

*(Name the macOS/Ubuntu equivalents, and phones as managed devices.)*

---

# SLIDE 4 — ACTIVITY 1: WHERE DOES IT LIVE?
### 8:35 – 8:47 · 12 minutes

> "Quick game, answers in the chat. I show you a file, a name and a location. You type NORMAL or SUSPICIOUS, and be ready to say why in one line. A few seconds each. Speed matters — this is a reflex you are building."

*(Run the ten items. Answers and the reasons are in `Day_5_Solutions.md`. Go back to items 8 and 10 — the misspelled `1sass.exe`, and the freshly installed Python that trainees wrongly flag.)*

> "Every one of those you decided before touching a browser. A name, a location, a signature — evidence you already have. Looking things up comes after you read what is in front of you."

---

# SLIDE 5 — TOPIC 5.2: BUILD THE WORKSTATION → DEMO 2
### 8:47 – 9:05 · 18 minutes

> "An analyst does not get a magic workstation. You build it, you baseline it, you maintain it. A baseline is a snapshot of a healthy machine, captured now, so that later — when something new appears — you have something to compare against. Watch, then do it with me."

*(Switch to PowerShell. Run **Demonstration 2** — make the evidence folder, export the four baseline CSVs, `Get-MpComputerStatus`, disk space, hash one file.)*

> "That last check — antivirus on, signatures recent — is maintenance today. It is also, word for word, the 'is the security solution operational' check you will run on real alerts from Day 7. Nothing here is busywork. This afternoon you will name and register these files as evidence, and that completes the whole computer-operations unit."

---

# SLIDE 6 — TOPIC 5.3 PART 1: READING THE WIRE → DEMO 3
### 9:05 – 9:25 · 20 minutes

> "Half of every alert is an address and a port. Let us make both readable. First, your own address — follow along."

*(Switch to terminal. Run **Demonstration 3** — `ipconfig /all`, the private ranges, the gateway, `nslookup`, `Test-NetConnection -Port 443`.)*

> "Three private ranges — 10, 172-16-to-31, and 192-168 — mean 'inside the building'. 127-0-0-1 is always this machine. Anything else is public — out on the internet. An address answers *where*. A port answers *what service* — 443 is encrypted web, 22 is SSH. On Day 3, 'port 443' was why we could not read the WKS-311 traffic: it was encrypted."

---

# SLIDE 7 — DEMO 4: WHO OWNS THIS CONNECTION
### 9:25 – 9:40 · 15 minutes

> "This is the most important fifteen minutes of the day. This is the command that finishes the WKS-311 ticket."

*(Switch to terminal. Run **Demonstration 4** — `netstat -ano`, turn a PID into a name with `tasklist`, then the one-line PowerShell join. Show TCPView if available.)*

> "Address, port, and the program that owns the connection, in one line. Run this on WKS-311 and you get svhost32.exe sitting on the bad connection. That is the process we could not name on Day 3. The hole is filled."

---

# SLIDE 8 — ACTIVITY 2: FOLLOW THE CONNECTION
### 9:40 – 10:05 · 25 minutes · OBSERVED

> "Into pairs. Each of you traces one of your **own** live connections to the program that owns it, then reports it to your partner — using only clues. Process, port, public or private. **Do not say your own IP address out loud.** That address identifies your machine, and this is the Day 3 rule, now on your own screen: look up the clue, never send the content."

*(This is observed and recorded. Have the observation sheet open. You are watching for two things: did they join a connection to its process themselves, and did they report in clues rather than their own IP.)*

*(Bring them back at 10:05 for the break.)*

---

# BREAK
### 10:05 – 10:15

---

# SLIDE 9 — TOPIC 5.3 PART 2: NAT AND THE ONE MACHINE YOU MAY SCAN → DEMO 5
### 10:15 – 10:25 · 10 minutes

> "Two more ideas about the wire, and one rule you never break. NAT is how twenty private machines share one public address going out — automatic and safe. Port forwarding is the opposite: a deliberate hole letting the world reach one internal machine. It is the first thing a network review looks at."

> "Now — I am about to scan a machine. There is exactly one machine I may scan without written permission: my own. Scanning anyone else's is illegal access under RA 10175, the Cybercrime Prevention Act. Not rude — illegal. So I scan 127.0.0.1 and nothing else."

*(Run **Demonstration 5** — the router screenshot, and `nmap -sT 127.0.0.1` if you have Nmap.)*

> "The full authorised sweep of the lab subnet is on our outstanding list, with the Day 1 lab documents. It needs the physical lab and a signed authorisation, so it waits for our first day on site."

---

# SLIDE 10 — TOPIC 5.4: THE WEB REQUEST AND ITS LOG → DEMO 6
### 10:25 – 10:40 · 15 minutes

> "Web servers make a lot of the alerts you will see, and the evidence is almost always an access log. Let me show you one request, start to finish, on my own machine."

*(Switch to terminal + browser. Run **Demonstration 6** — start `http.server`, make a 200, make a 404, watch the server log, `curl.exe -I`, name the WAF and the 403.)*

> "One 404 is nothing — a missing favicon. A hundred 404s from one address, all asking for admin and backup paths — that is somebody trying doors. And remember this: the status code tells you what the server *did*, not whether it was right. The most dangerous line in a log is often a 200, not a 403 — because a 200 means it worked."

---

# SLIDE 11 — ACTIVITY 3: ACCESS-LOG DETECTIVE
### 10:40 – 11:05 · 25 minutes

> "Into teams. You each have forty lines of a real-shaped web log — six addresses. Some are normal visitors, one is a scanner, one is the attacker. Tell me the story: what happened, in what order, and which single line is the worst thing in the log. Then decide — threat, detection, or routine — and give the reason."

*(Paste the log or confirm they have `Day_5_access_log.txt`. The full walkthrough is in `Day_5_Solutions.md`. At 10:55 bring two teams back to present.)*

> "The 403s are the noise — those attacks were blocked. The 200 on the web shell is the fire — that command ran. Blocked is safe. Served is not. Nothing contained the shell, so this is a threat, not a detection."

---

# SLIDE 12 — TOPIC 5.5: READING SCRIPTS → DEMO 7
### 11:05 – 11:15 · 10 minutes

> "A script is just instructions you can read. Do not be afraid of it. Let me walk the parser I sent you — twenty lines — and then run it on that attack log."

*(Switch to editor + terminal. Run **Demonstration 7** — walk the parser in five parts, run it, show the counts, show the PowerShell version.)*

> "Forty lines of log became two lines of counts. The script does not judge — it counts, so you can judge. This afternoon you will add one thing to it: count the 404s per address, so the scanner jumps out on its own."

---

# SLIDE 13 — ACTIVITY 4: EXPLAIN THIS SCRIPT, DON'T RUN IT
### 11:15 – 11:33 · 18 minutes

> "Into pairs. Three scripts. For each: what does it do, does it touch the internet, and would you run it or escalate it? **You do not run any of them.** Reading is the job."

*(The three scripts are in the Activity Pack Part 4 and `Day_5_Sample_Data.md` §4. Answers in Solutions.)*

> "Script B is the one you were tempted by — and it is the one you must never run. Reading it told you exactly what it does: fetch code from an address and run it. That is enough to escalate. Running it *is* the incident. And Script C — it runs perfectly and reports zero 404s, in a log with seven. A script that runs clean and finds nothing has not proven there is nothing. Check silence."

---

# SLIDE 14 — THIS AFTERNOON
### 11:33 – 11:40 · 7 minutes

> "This afternoon, on your own, one to four. Nine tasks. You build and register your baseline, annotate five of your own connections, draw your network's port map, read the web log, extend the parser, and — the one that closes the loop — re-write the WKS-311 ticket with the process we can finally name, and self-check it against the QA checklist you wrote on Day 3."

> "Marked the same way as always: **the reason matters more than the answer.** A right action with no reason is not competent. A well-reasoned answer that reaches a defensible conclusion is."

---

# SLIDE 15 — CLOSE
### 11:40 – 11:45 · 5 minutes

> "Today the tools stopped being magic. This morning you saw the process behind a connection, the code behind a status page, and the instructions inside a script — on your own machine. Nothing an alert points at is a mystery any more. It is a process, an address, a request, or a script, and you can read all four."

> "Two things to carry out the door: **read it, don't run it**, and **scan only what is yours.** Tomorrow, Day 6, the SIEM — you will enrol a Wazuh agent, so bring a machine you can install software on. See you at eight."

---
---

# IF YOU ARE RUNNING LATE

Cut in this order:
1. `tracert` in Demo 3
2. The PowerShell version in Demo 7 (Python only)
3. Activity 4 down to two scripts (A + B), move Script C to the afternoon
4. Activity 3 to two teams presenting, not four
5. Demo 5 live Nmap → screenshot

**Never cut:** Demo 4 (connection → process) or Activity 2 (observed). They are the spine and the evidence.

---

# THE THREE SENTENCES OF THE DAY

1. **Location is evidence** — the real svchost lives in System32.
2. **A connection has an owner** — `netstat -ano` plus the process name finishes the ticket Day 3 could not.
3. **Read it, don't run it; scan only what is yours.**
