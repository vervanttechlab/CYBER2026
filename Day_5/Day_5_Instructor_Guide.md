# DAY 5 — INSTRUCTOR GUIDE
## Topic: Underneath the Alert — the Machine, the Wire, the Web and the Script
### Cyber Threat Monitoring Level I · Day 05 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

---

## HOW THIS GUIDE WORKS

This is the **topic guide**. It tells you what Day 5 teaches, why it is built this way, what you must know before you stand in front of the class, and how each part is assessed.

It is **not** a word-for-word script. You are a trainer, not a reader.

There are five other files you need today. Keep them all open.

| File | What it is for |
|------|---------------|
| **`Day_5_Instructor_Guide.md`** | *(this file)* The topic, the sequence, the teaching points |
| **`Day_5_Presenter_Script.md`** | **The words, slide by slide.** Keyed to the 15-slide deck. This is the one you read from |
| **`Day_5_Demonstration_Guide.md`** | Every demonstration, step by step, command by command. Read it the night before |
| **`Day_5_Student_Activity_Pack.md`** | What the trainees do. Send it before the session |
| **`Day_5_Solutions.md`** | Answer keys, marking guides, and the reasoning behind each answer |
| **`Day_5_Resources.md`** | Equipment, links, printing list, and what to do when something does not run |

Two data files ship with today. Send both to the class with the joining note: **`Day_5_access_log.txt`** (the web log they read) and **`Day_5_log_parser.py`** (the parser they run). **`Day_5_Sample_Data.md`** holds the same material as readable text plus the three scripts for Activity 4.

---
---

# PART A — WHAT DAY 5 IS

## The one-sentence topic

> **Day 5 teaches the analyst to read the four things an alert points at — a process, an address and port, a web request, and a script — against the machine and the network they came from, and to prepare and baseline the workstation they read them on.**

## Why Day 5 looks like this

By Day 3 a trainee can take an alert, look up the clue, judge the source, decide **threat / detection / routine**, and write a ticket. But Day 3 stopped at the browser. When the relay alert said WKS-311 was making outbound connections to `185.220.101.1` on port 443, the class could look up the *address* — but nobody could yet say **which process** was making the connection, whether port 443 was normal, or where on the machine the file lived.

Day 5 is where that gap closes. It is the **ground underneath the alert**: the operating system, the wire, the web request and the script. Without it, an analyst can only ever repeat what the tool already said.

**Day 5 also carries the whole of the old Day 4.** Day 4 was going to be a separate "prepare the workstation" day covering the common unit `ICT311203` *Perform Computer Operations* and the core underpinning knowledge about operating systems. It has been **folded into Day 5**, because preparing and baselining a machine and then reading what runs on it is one continuous piece of work, not two. Nothing from `ICT311203` is dropped — every element still produces evidence, in the afternoon.

Day 5 assumes **nothing** from a Day 4 session. Everything the trainee needs — the tools, the baseline, the commands — is introduced here.

| The core moment | The unit it delivers |
|-----------------|---------------------|
| Knowing what runs on a machine, and where files legitimately live | `CS-ICT251101` knowledge 1.1 · `ICT311203` E1, E3 |
| Planning, preparing, maintaining and baselining the analyst workstation | `ICT311203` E1–E5 *(the compressed Day 4)* |
| Reading an address, a port and a connection to its owning process | `CS-ICT251101` knowledge 1.4 · E1 PC 1.3 |
| Reading a web request and an access log | `CS-ICT251101` knowledge 1.2 |
| Reading a script well enough to say what it does, without running it | `CS-ICT251101` knowledge 1.3 |
| Never running a suspicious script; never scanning a machine that is not yours | `400311106` LO4 reprised · RA 10175 |
| Registering the baseline as evidence, and self-checking the re-ticket | `400311106` LO5 · `ICT315202` LO2 |

---

## The five topics of Day 5

Give these to the trainees at 8:00 AM. They are printed at the front of the Student Handout and the Activity Pack, in exactly this wording, so the class and the trainer use the same names all day.

| # | Topic title (what the trainee sees) | Primary competency | Time |
|---|-----------------------------------|-------------------|------|
| **5.1** | **The Machine Underneath** — processes, services, scheduled tasks, and where files really live | Knowledge 1.1 · `ICT311203` E1, E3 | 32 min live |
| **5.2** | **Preparing and Maintaining the Analyst Workstation** — plan, prepare, baseline, maintain | `ICT311203` E1–E5 | 18 min live + 40 min PM |
| **5.3** | **The Wire** — addresses, ports, NAT, and reading a connection to its owner | Knowledge 1.4 | 60 min live + 45 min PM |
| **5.4** | **The Web Request** — the request path, status codes, and the access log | Knowledge 1.2 | 40 min live + 25 min PM |
| **5.5** | **Reading Scripts for Triage** — read a script, never run it | Knowledge 1.3 | 28 min live + 25 min PM |

> **Say the topic number out loud when you start each one.** "This is Topic 5.3." Adult trainees who lose the thread can find their way back if they know where they are.

---

## Competency map — the full picture

### Core unit — `CS-ICT251101` Monitor and report cyber threats

Day 5 does **not** add a new element of the core unit. It builds the **required knowledge** that Elements 1–5 all stand on — items 1.1, 1.2, 1.3 and 1.4 — and it deepens **E1 PC 1.3** (checking a red flag) by teaching the class to read the machine evidence behind a detection, not just the tool's verdict.

| Required knowledge | What Day 5 does with it |
|--------------------|------------------------|
| **1.1** Basic knowledge of Windows, macOS & Linux OS | Topic 5.1 — processes, services, scheduled tasks, autoruns, file locations, taught on Windows with the macOS and Ubuntu equivalents named |
| **1.2** Web server and website design and architecture | Topic 5.4 — the request path, methods, status codes, the access log, where a WAF sits |
| **1.3** Scripting and coding language (PHP, Python, Java, VB) | Topic 5.5 — reading PowerShell, Python and bash for triage; recognising a PHP/JS web shell |
| **1.4** Network infrastructure and architecture (LAN, WAN, port forwarding) | Topic 5.3 — private vs public addressing, subnets, ports, NAT, port forwarding, read from live evidence |

### Common unit completed today — the compressed Day 4

| Code | Unit | Elements covered today |
|------|------|----------------------|
| `ICT311203` | Perform Computer Operations | **E1** plan and prepare · **E2** input data · **E3** access information · **E4** produce/output and transfer data · **E5** maintain equipment and systems — all five, through "prepare, baseline and maintain an analyst workstation" |

### Basic units reprised, not newly taught

| Code | Unit | How it appears |
|------|------|---------------|
| `400311106` | Access and maintain information | **LO4** *(never send the content)* returns the moment the class touches their own IP addresses and a suspicious script; **LO5** *(manage)* is the baseline registered as evidence in PM Task 2 |
| `ICT315202` | Apply quality standards | **LO2** *(assess own work)* is the self-check on the re-ticket in PM Task 8, marked against the class QA checklist the trainees wrote on Day 3 |

> **Still outstanding from Day 1:** the **Lab OSH Checklist** and the **Green Lab Pledge**, and the **live lab-subnet Nmap sweep** that this remote day cannot run. Keep them on your outstanding list and say so today. Day 5 does the network knowledge and the *localhost-only* scan; the full authorised sweep of the lab subnet happens on the first day on site.

---

## The 21st century design — why the day looks like this

You are talking, in pure lecture, for well under **90 minutes out of 225**. The rest is **seven demonstrations the class follows on their own machines**, and **four activities**. This is a hands-on day: almost everything you say, they immediately type.

| 21st century skill | Where it is built into Day 5 | How you can see it happening |
|-------------------|----------------------------|----------------------------|
| **Critical thinking** | "Where does it live?" — a name is not evidence; a path is | A trainee rejects `svhost32.exe` in `C:\Users\Public` on location alone |
| **Communication** | Activity 2 pairs report a connection **without** naming their own IP | A trainee describes their traffic in clues, not content |
| **Collaboration** | Activity 3 — a team reconstructs an attack from a log nobody can read alone | The team argues about the order the requests happened in |
| **Digital literacy** | Every trainee runs `netstat`, `Test-NetConnection`, `http.server` and a parser on their own machine | A trainee joins a connection to its process unprompted |
| **Information literacy** | Reading a script to predict its behaviour before running it | A trainee explains what a download cradle does without executing it |
| **Metacognition** | The re-ticket of WKS-311, self-checked against their own Day 3 standard | A trainee finds the field their Day 3 ticket was missing |

### The teaching methods used today, and why

1. **Follow-along demonstration** *(Demos 1–7)*. You run a command; they run the same command on their own machine and see their own output. This is the spine of the morning. It is why the day is demonstration-led and not lecture-led — a network command means nothing until you have watched it print your own address.

2. **Gamified decision drill** *(Activity 1 — "Where Does It Live?")*. Ten items, a few seconds each, answers in the chat. It trains the single most useful reflex of the day: a file's **location and name** are evidence, before you look anything up.

3. **Constrained pair reporting** *(Activity 2 — "Follow the Connection")*. Each trainee traces one of their own live connections to its process, then reports it to a partner **using only clues** — process, port, public or private — never their own IP address. It is the Day 3 never-paste rule, now applied to their own machine.

4. **Collaborative reconstruction** *(Activity 3 — "Access-Log Detective")*. A team is handed forty lines of a real-shaped web log and must tell the story: reconnaissance, a brute-force, a path-traversal that failed, a plugin upload that succeeded, and a web shell being used. Then they decide **threat / detection / routine** and give the reason.

5. **Read-don't-run** *(Activity 4 — "Explain This Script, Don't Run It")*. Pairs read three scripts and predict what each does. One is benign, one is a defanged download cradle, one has a bug. Nobody runs anything. The point is that a Level I analyst reads scripts to understand them and **escalates** the ones that need running.

---

## What a trainee can do at 4:00 PM that they could not do at 8:00 AM

Read these out at the start of the day. Read them again at the end and ask for a show of hands.

1. List what is running on a machine — processes, services, scheduled tasks, autoruns — with a command, not a mouse.
2. Say where a Windows system file **should** live, and treat a wrong location as evidence.
3. Prepare and **baseline** a workstation, and register that baseline as evidence.
4. Tell a **private** address from a **public** one, and say what NAT does between them.
5. Read a port number and say, roughly, what service it belongs to.
6. Join a live network connection to the **process** that owns it.
7. Read a line of a web access log — method, path, status code — and say what happened.
8. Reconstruct a simple web attack from a log, and decide threat, detection or routine.
9. Read a short script and predict what it does **without running it**.
10. State the two rules that bound all of it: **read a suspicious script, never run it**, and **scan only a machine you are authorised to scan.**

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 3: "what was missing from the WKS-311 alert?" | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 20 | 3 | **Topic 5.1** + **Demo 1** Inside the machine | Follow-along | 5.1 |
| 8:35 | 12 | 4 | **Activity 1** "Where Does It Live?" — ten items | Gamified, chat | 5.1 |
| 8:47 | 18 | 5 | **Topic 5.2** + **Demo 2** Build the baseline | Follow-along | 5.2 |
| 9:05 | 20 | 6 | **Topic 5.3 part 1** + **Demo 3** Your address and the wire | Follow-along | 5.3 |
| 9:25 | 15 | 7 | **Demo 4** Who owns this connection | Follow-along | 5.3 |
| 9:40 | 25 | 8 | **Activity 2** "Follow the Connection" | Breakout pairs | 5.3 |
| 10:05 | 10 | — | **BREAK** | | |
| 10:15 | 10 | 9 | **Topic 5.3 part 2** + **Demo 5** NAT, port forwarding, localhost-only scan | Follow-along | 5.3 |
| 10:25 | 15 | 10 | **Topic 5.4** + **Demo 6** A web request, end to end | Follow-along | 5.4 |
| 10:40 | 25 | 11 | **Activity 3** "Access-Log Detective" | Breakouts, then teach-back | 5.4 |
| 11:05 | 10 | 12 | **Topic 5.5** + **Demo 7** The twenty-line parser | Follow-along | 5.5 |
| 11:15 | 18 | 13 | **Activity 4** "Explain This Script, Don't Run It" | Breakout pairs | 5.5 |
| 11:33 | 7 | 14 | Afternoon brief · how it is marked | Whole class | — |
| 11:40 | 5 | 15 | Close · open floor | Whole class | — |

> **Optional Demo 8** — a 60-second Wireshark capture of one DNS query and one HTTP request to localhost — runs **only if you are ahead** and is not on the timetable. It needs Wireshark and Npcap on the trainer machine only; trainees do not install it. Screenshot fallback is in the Demonstration Guide.

**Total pure-lecture time is under 90 minutes. The rest of the 225 is them typing.**

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Nine tasks, about 2 hours 50 minutes of work, submitted by 4:00 PM.

| # | Task | Min | Evidence produced |
|---|------|-----|------------------|
| 1 | Workstation build checklist, signed | 25 | Signed build checklist |
| 2 | Baseline export — processes, services, scheduled tasks, autoruns — hashed, named, registered | 25 | Baseline CSVs + evidence register row |
| 3 | Maintain and transfer — disk space, Defender status, a backup copy verified by hash | 15 | Maintenance note + verified-copy hash |
| 4 | Annotate five of your own connections | 25 | Annotated netstat/TCPView capture |
| 5 | Draw the port-mapping diagram of your own network | 20 | Port-mapping diagram |
| 6 | Web log — make your own 200 and 404, then answer six questions on the attacked-site log | 25 | Web-log worksheet |
| 7 | Extend the parser — count 404s per IP, flag a threshold | 25 | Working parser script + its output |
| 8 | Re-ticket WKS-311 with the new evidence, self-checked against the class QA checklist | 5 | Re-written ticket + self-check |
| 9 | Reflection | 5 | Three written answers |

> **Task 7 builds directly on `Day_5_log_parser.py`.** Trainees edit the file you already sent them. If somebody cannot get Python running, the fallback is to do the same counting by hand from `Day_5_access_log.txt` and submit the tally — the marked skill is *reading the log*, not installing Python.

---

## Before the day

### The night before

- [ ] **Run every demonstration once, yourself, start to finish.** The Demonstration Guide has a practice checklist at the end. Network output differs on every machine — you must have seen yours
- [ ] Run `python Day_5_log_parser.py Day_5_access_log.txt` and confirm you get the numbers in `Day_5_Solutions.md` (status 200=27, 404=7; top talker `203.0.113.45` = 14)
- [ ] Confirm `python -m http.server 8000` starts, and that you can open `http://localhost:8000` and see a 404 in the console when you request a missing page
- [ ] Confirm the portable tools launch: **TCPView** and **Autoruns** from the USB drive
- [ ] Take the fallback screenshots listed in `Day_5_Resources.md` — the router NAT page, a `netstat -ano` result, DevTools Network tab
- [ ] Open the deck and check it runs to 15 slides

### On the morning

- [ ] Breakout rooms created and named after the teams
- [ ] Activity Pack, Student Handout, Resources, **`Day_5_access_log.txt`** and **`Day_5_log_parser.py`** all sent with the joining note
- [ ] Chat open and visible — Activity 1 runs through it
- [ ] The attacked-site log ready to paste into each Activity 3 breakout room
- [ ] Collect outstanding Day 1, 2 and 3 evidence in the first fifteen minutes

> **Roles rotate today.** Announce it at 8:00 and give them ten seconds to sort it out.

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

Each topic gives you the same five things: the point, what you must know, the key messages, questions to ask, and mistakes to expect.

---

## TOPIC 5.1 — THE MACHINE UNDERNEATH
### 8:15–8:47 · 32 minutes (incl. Activity 1) · Deck slides 3–4 · Knowledge 1.1 · `ICT311203` E1, E3

### The point

Before a trainee can judge a detection, they must know what a *normal* machine looks like: what runs, what starts by itself, and where files legitimately live. A detection is only suspicious against a background of normal.

### What you must know

- The four things that run on a Windows machine and how to list each one:

| What | Command | The GUI equivalent |
|------|---------|-------------------|
| Processes | `Get-Process` | Task Manager · Details |
| Services | `Get-Service` | `services.msc` |
| Scheduled tasks | `Get-ScheduledTask` | Task Scheduler |
| Autoruns / startup | `Get-CimInstance Win32_StartupCommand`, or **Autoruns** | Task Manager · Startup |

- **Where Windows system files live.** The real `svchost.exe`, `lsass.exe`, `services.exe` and `explorer.exe` live in `C:\Windows\System32` (explorer in `C:\Windows`). They do **not** live in `C:\Users\Public`, `%TEMP%`, or a downloads folder. This is the Day 3 Alert B point, now made general: **location is evidence.**
- The **equivalents on other systems**, named so the class knows the CS range is covered: macOS uses Activity Monitor, `ps`, `launchctl` and LaunchAgents/LaunchDaemons; Ubuntu uses `ps`, `systemctl`, `crontab` and `systemd` units. Android and iOS are in the CS range as *managed* devices — an L1 analyst reads their telemetry through an MDM console, not by opening a shell on the phone.

### Key messages

- You cannot spot the abnormal until you know the normal. Today you capture what normal looks like on your own machine.
- A process **name** can be faked in seconds. A **path** is much harder to fake, and a **digital signature** harder still.
- `svchost.exe` in `System32`, signed by Microsoft, is Windows. `svhost32.exe` in `C:\Users\Public` is not — and you knew that before you looked anything up.

### Questions to ask

- "The real `svchost.exe` lives in one folder. Which one?" *(`C:\Windows\System32`.)*
- "A process is called `explorer.exe` but it is running from your Downloads folder. Is that normal?" *(No. The real one runs from `C:\Windows`. Location is evidence.)*

### Mistakes to expect

- Trainees trust a name because it looks like a Windows name. That is exactly what masquerading relies on. Push them to the path.
- Trainees think every unfamiliar process is malware. Most unfamiliar processes are just software you have not learned yet. The question is not "do I recognise it" but "is it where it should be, and is it signed."

---

## TOPIC 5.2 — PREPARING AND MAINTAINING THE ANALYST WORKSTATION
### 8:47–9:05 live, plus PM Tasks 1–3 · Deck slide 5 · `ICT311203` E1–E5

### The point

This is the whole of `ICT311203`, delivered as one honest piece of work: an analyst does not get a magic workstation, they **build** one, **baseline** it, and **maintain** it. Eighteen minutes live sets it up; the afternoon produces the evidence.

### What you must know — the five elements, as one workflow

| Element | In the analyst's words | Where the evidence comes from |
|---------|------------------------|-------------------------------|
| **E1** Plan and prepare | Decide what an analyst workstation needs — the portable toolset, a browser, PowerShell — and follow OH&S while setting it up | PM Task 1 build checklist |
| **E2** Input data | Enter the build details accurately and save them per SOP | PM Task 1 |
| **E3** Access information | Open the right tool for the job — Task Manager, `services.msc`, TCPView | Demonstrated in 5.1; used all day |
| **E4** Produce and transfer | Export the baseline to CSV, and transfer a copy safely, verified by hash | PM Task 2 and 3 |
| **E5** Maintain | Disk space, backups, and virus/definition checks | PM Task 3 |

- **The baseline is the deliverable that ties the unit to the job.** A baseline is a snapshot of what runs on a healthy machine, captured *now*, so that a future "is this new?" question has an answer. The class exports processes, services, scheduled tasks and autoruns to CSV, hashes each file, names it to the Day 3 convention, and registers it. That single act satisfies `ICT311203` E4 **and** `400311106` LO5.
- **Maintenance is not housekeeping.** `Get-MpComputerStatus` shows whether Defender is on and when its signatures last updated — that is E5's "regular virus checks", and it is also the E2 *"is the security solution operational"* check the core unit will lean on from Day 7.

### Key messages

- Your workstation is your instrument. An analyst with an unbaselined, unmaintained machine cannot tell their own noise from a real signal.
- A copy you have not verified is not a backup, it is a hope. Hash it, copy it, hash the copy, compare.

### Mistakes to expect

- Trainees treat the baseline as busywork. Land it with the future question: "In three weeks a scheduled task appears. Is it new? Your baseline is the only thing that can answer that."
- Trainees back a file up and never check the copy. Require the two hashes to match in Task 3.

---

## TOPIC 5.3 — THE WIRE
### 9:05–9:40 and 10:15–10:25 live, plus PM Tasks 4–5 · Deck slides 6–9 · Knowledge 1.4

### The point

Half of every alert is an address and a port. Topic 5.3 makes those two things readable: which addresses are inside the building and which are outside, what a port tells you, what NAT does in between, and — the skill that pays off immediately — how to join a connection to the **process** that owns it. This is the direct answer to the WKS-311 gap.

### What you must know

- **Private vs public addressing.** The private ranges — memorise these, the class will ask:

| Range | Size |
|-------|------|
| `10.0.0.0` – `10.255.255.255` | /8 |
| `172.16.0.0` – `172.31.255.255` | /12 |
| `192.168.0.0` – `192.168.255.255` | /16 |
| `127.0.0.0/8` | loopback — this machine, "localhost" |

  A private address is a device inside a network; it is not reachable directly from the internet. A public address is globally routable. NAT is the translation the router does between the two.
- **Ports, at L1 depth.** A port is which service on a host. The handful worth knowing cold: 22 SSH, 80 HTTP, 443 HTTPS, 53 DNS, 25/587 SMTP, 3389 RDP, 445 SMB, 3306 MySQL. "Port 443" in the WKS-311 alert meant the traffic was encrypted, which is why the address was all the class could read on Day 3.
- **NAT and port forwarding.** Outbound NAT lets many private devices share one public address. **Port forwarding** deliberately pokes a hole inward — it maps a public port to a private host — and it is exactly the thing a network review looks for, because it is how internal services end up exposed.
- **Joining a connection to its process.** `netstat -ano` gives connections with a PID in the last column; `tasklist /fi "pid eq <n>"` names it. PowerShell does it in one pipeline (`Get-NetTCPConnection` joined to `Get-Process`), and **TCPView** does it live with names already attached. This is the command that would have finished the WKS-311 ticket.

### Key messages

- An address answers *where*. A port answers *what*. A process answers *who on this machine*. You need all three.
- `127.0.0.1` is always this machine. It never means the internet. Scanning it is scanning yourself — which is why it is the only thing we scan today.
- Encrypted traffic (443) hides the content, not the connection. You can still see who talked to whom, when, and how much.

### Questions to ask

- "Is `192.168.1.42` inside or outside the building?" *(Inside — it is private.)*
- "You see an ESTABLISHED connection to a public address on port 443, and the owning process is a program you have never heard of running from a temp folder. What do you do?" *(Look up the address, note the path as evidence, and escalate — this is the WKS-311 shape.)*

### Mistakes to expect

- Trainees read "the firewall allowed it" as "it is fine." The Day 3 correction stands: **allowed means it worked, not that it was safe.**
- Trainees confuse the port on their end with the port on the far end. In `netstat` the local port is often a high random number; the *remote* port is the service.

---

## TOPIC 5.4 — THE WEB REQUEST
### 10:25–11:05 live, plus PM Task 6 · Deck slides 10–11 · Knowledge 1.2

### The point

Web servers generate a large share of the alerts an L1 analyst sees, and the evidence is almost always an **access log**. Topic 5.4 teaches the anatomy of one request and then reads a whole attack out of a log.

### What you must know

- **The request path:** browser → DNS → the server (often behind a **WAF** and a reverse proxy) → the application → back. The WAF sits *in front* of the application and is where a blocked request (a 403) is often decided.
- **Methods:** GET fetches, POST submits. A storm of POSTs to `wp-login.php` is a brute-force; a storm of GETs to paths that do not exist is a scanner.
- **Status codes, at L1 depth:** 200 OK, 301/302 redirect, 304 not-modified, **403 forbidden** (often the WAF or a permission), **404 not found** (the single most useful code for spotting a scanner), 500 server error.
- **One access-log line reads left to right:** who (IP), when (timestamp), what (`"METHOD path PROTOCOL"`), the result (status code), the size, then the referrer and user-agent. The user-agent often names the tool — `Nikto`, `python-requests`, `curl` — and a tool in the user-agent of a normal website's log is itself a red flag.
- **The story in `Day_5_access_log.txt`**, which you must be able to tell before Activity 3: normal browsing, then a Nikto scan throwing 404s (`198.51.100.23`), then a WordPress brute-force that succeeds (`203.0.113.45`, eight POSTs then a 302), then a path-traversal that the server blocks with 403s (`192.0.2.77`), and finally the attacker uploading a plugin and using a web shell (`thumb.php?c=whoami`). Full walkthrough in `Day_5_Solutions.md`.

### Key messages

- A 404 is a request for something that is not there. A *few* are normal. A *burst* of them, from one address, for admin paths, is somebody trying doors.
- The status code tells you what the server *did*. It does not tell you whether that was the right thing — a 200 on `wp-login.php` after fifty tries means the server happily served the login page fifty times.
- The most dangerous line in the whole log is a **200**, not a 403: `thumb.php?c=whoami` returning 200 means a command ran.

### Mistakes to expect

- Trainees fixate on the 403s ("blocked, so we are fine") and miss the 200 web shell. Containment again: the traversal was blocked, the shell was not.
- Trainees ignore the timestamps. The order and the spacing (eight logins two seconds apart) are the evidence that it is automated.

---

## TOPIC 5.5 — READING SCRIPTS FOR TRIAGE
### 11:05–11:33 live, plus PM Task 7 · Deck slides 12–13 · Knowledge 1.3

### The point

Scripts arrive as evidence — in a scheduled task, in a log, attached to a ticket. An L1 analyst must read one well enough to say what it does, and must know that **reading is the job and running is an escalation.**

### What you must know

- **The parser you ship** (`Day_5_log_parser.py`) is deliberately small and readable: open a file, match each line with a regular expression, count status codes and IPs, print. Walk it line by line. It is the class's proof that "a script" is just instructions they can read.
- **The three languages the CS names, at reading depth:** Python (the parser), PowerShell (the same job with `Get-Content` and `Group-Object`), and bash (`awk '{print $9}' | sort | uniq -c`). PHP and Visual Basic appear as *things you recognise in evidence* — a `.php` file in an uploads folder is a web shell candidate; a VB macro in a document is a classic delivery mechanism.
- **What a malicious script looks like** without ever running one: it reaches out to the internet to fetch more code (a "download cradle"), it hides what it is doing behind encoding (base64, `-EncodedCommand`), and it tries to run whatever it fetched. In the training material every such example is **defanged** — URLs written `hxxp://`, addresses from the documentation-only ranges — so nothing is runnable even by accident.
- **The bug in the third Activity 4 script:** it compares the status code to the integer `404` when the parser reads it as the string `"404"`, so it always finds zero. This is the everyday reason a script "runs fine and reports nothing" — and why an analyst confirms a tool's silence against a second method.

### Key messages

- A script you can read is a script you can judge. If you cannot read it, that is a reason to escalate, not to run it.
- **You never run a suspicious script to see what it does.** That is what a sandbox and an authorised analyst are for. Running it *is* the incident.
- "It ran without errors and found nothing" is not the same as "there is nothing." Tools have bugs. Check silence.

### Mistakes to expect

- Trainees want to run the suspicious script "just to see." Stop it the way Day 3 stopped the file upload: reading is L1, running is escalation.
- Trainees assume a script that produces no output is safe or empty. The buggy script produces no output and the log is full of 404s. Silence is a finding to check, not a result to trust.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 5 produces for each portfolio

| Evidence item | Where it comes from | Unit and element |
|--------------|--------------------|-----------------|
| Signed workstation build checklist | PM Task 1 | `ICT311203` E1, E2 |
| Baseline export — processes, services, tasks, autoruns — hashed, named, registered | PM Task 2 | `ICT311203` E3, E4 · `400311106` LO5 |
| Maintenance note + a backup copy verified by matching hashes | PM Task 3 | `ICT311203` E4, E5 |
| Annotated capture of five own connections | PM Task 4 | Knowledge 1.4 · `CS-ICT251101` E1 PC 1.3 |
| Port-mapping diagram of own network | PM Task 5 | Knowledge 1.4 |
| Web-log worksheet, six questions on the attacked-site log | PM Task 6 | Knowledge 1.2 |
| Working parser that counts 404s per IP, with its output | PM Task 7 | Knowledge 1.3 |
| WKS-311 re-ticket, self-checked against the class QA checklist | PM Task 8 | `ICT315202` LO2 · `CS-ICT251101` E1 PC 1.5 |
| "Where Does It Live?" answer sheet | Activity 1 | Knowledge 1.1 |
| Access-Log Detective team finding | Activity 3 | Knowledge 1.2 · analytical skill |
| Reflection | PM Task 9 | Metacognition — not separately assessed |

## Observation during the live session

Two things are observed and recorded today, both in Activity 2.

1. **Did the trainee join a connection to its process without being told the command?** That is the core-unit analytical skill — and the WKS-311 gap being closed.
2. **Did the trainee report their connection using clues, not their own IP?** That is `400311106` LO4 holding under pressure on their own machine.

Have the observation sheet from `Day_5_Resources.md` open at 9:40.

## How the afternoon is marked

**The reason matters more than the answer.** Same rule as Day 3. Say it in the morning brief and mean it in the marking.

| Band | What it looks like |
|------|-------------------|
| **Competent** | Baseline captured and registered · a connection correctly read as public/private and tied to a process · the web attack story told in the right order with the web shell identified · a parser that runs and flags the scanner · the re-ticket carries the process and port the Day 3 ticket lacked |
| **Not yet competent** | Baseline missing or not registered · a name trusted over a path · the 403s called "safe" while the 200 web shell is missed · a script run instead of read · a re-ticket no better than the Day 3 one |

Full worked answers and per-item marking notes are in `Day_5_Solutions.md`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| A trainee has no Python | They do Task 7 by hand from `Day_5_access_log.txt` and submit the tally. The marked skill is reading the log |
| `http.server` will not start (port in use) | Use `python -m http.server 8080` and open `http://localhost:8080`. The port number is not the point |
| A trainee cannot install TCPView | `netstat -ano` plus `tasklist` does the whole job from the built-in command line |
| Autoruns is blocked by policy | `Get-CimInstance Win32_StartupCommand` and Task Manager · Startup cover it |
| Activity 3 overruns | Cut to two teams presenting; take the rest of the log walkthrough from the handout. Keep the "which line is the worst" question |
| You are behind at 11:15 | Cut Activity 4 to two scripts (benign + the download cradle) and let PM Task 7 carry the reading. Never cut Activity 2 — it is the observed evidence |
| A trainee asks to run the suspicious script | "No. Reading is your job; running is an escalation. That is the whole point of the topic" |

---

## End of day checklist

- [ ] Activity 3 team findings collected
- [ ] Observation notes from Activity 2 written up while fresh
- [ ] Outstanding Day 1–3 evidence chased
- [ ] Day 1 lab OSH checklist, green lab pledge, **and the live lab-subnet Nmap sweep** still on the outstanding list
- [ ] Tomorrow announced: **Day 6, the SIEM.** Trainees enrol a Wazuh agent — they must bring a machine they can install software on

---

## What to say at the close

Day 5 is the day the tools stopped being magic. This morning the class saw, on their own machines, the process behind a connection, the code behind a status page, and the instructions inside a script. Nothing an alert points at is a mystery any more — it is a process, an address, a request or a script, and they can now read all four.

Say that. Then remind them: **read it, don't run it; scan only what is yours.** Then let them go.
