# DAY 06 — INSTRUCTOR GUIDE
## Topic: Network and Web Evidence in Depth — the Wire, the Web Server, the Firewall Log
### Cyber Threat Monitoring Level I · 30-Day Program · Day 06 of 30 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **The two standing conditions.** (1) **No SIEM server** — the capture is of your own browsing, the web server is one you run yourself, the firewall log is read from a supplied file; nothing touches anyone else's network. (2) **Total beginners** — assume nothing, every click shown, calm pace. Day 04 gave them `ipconfig`, `netstat`, one web request and a twenty-line parser. Today each of those becomes a piece of evidence they can read and keep.

---

## HOW THIS GUIDE WORKS

The **topic guide** — what Day 06 teaches, why, what you must know, and how it is assessed. Not a script. Keep these open:

| File | For |
|------|-----|
| **`Day_06_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_06_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_06_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_06_Student_Activity_Pack.docx`** | what the trainees do |
| **`Day_06_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_06_Activity_Solutions.docx`** | the four morning activities answered in the trainee's own tables — keep open during the live session (trainer only) |
| **`Day_06_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_06_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_06_Sample_Data.md`** | the packet list, the status-code recipes, the port map, the lab subnet, the firewall log findings, parser v2 |
| **`Day_06_pfirewall.log`** · **`Day_06_fw_parser.py`** | the two files the class reads and runs — send both with the joining note |

---
---

# PART A — WHAT DAY 06 IS

## The one-sentence topic

> **Day 04 showed the trainees the wire and the web request once. Today they read both as evidence — a real capture, a web server they run from both sides, the ports their own machine listens on, the firewall's own log — and their parser grows up to read two kinds of log instead of one.**

## Where Day 06 sits

Day 06 is the third Phase A "underpinning" day. It deepens **required knowledge 1.2** (web server and website architecture) and **1.4** (network infrastructure — LAN, WAN, port forwarding), keeps **1.3** (scripting) alive, and produces the network habits Phase B depends on — especially Days 16–17 (spread, egress and ingress), which are read from exactly these sources.

| Unit / knowledge | What Day 06 does |
|------------------|------------------|
| **CS-ICT251101 knowledge 1.4** Network infrastructure and architecture — LAN, WAN, port forwarding | Topics 6.1, 6.3 — the capture, the port map, NAT and the router's forwards |
| **CS-ICT251101 knowledge 1.2** Web server and website design and architecture | Topic 6.2 — the server run from both sides, every status code made to happen |
| **CS-ICT251101 knowledge 1.3** Scripting and coding language | Topic 6.5 — parser v2, read then run then changed by one line |
| **CS-ICT251101 knowledge 1.5 / 1.6** Sources of alert · log management *(preview)* | Topic 6.4 — the firewall log as a detection source, read raw |
| **`ICT311203`** Perform computer operations | Running a server, a client and a parser; stopping the server at the end |
| **`400311106`** Access and maintain information | Every capture, log and output named, hashed and registered |
| **`ICT315202`** LO2 | PM Task 6 — one register row self-checked |

Tomorrow (Day 07) is threat intelligence and the attack framework; then Phase B begins on Day 08.

## What "no server" changes

The original plan had "Wireshark for one 60-second capture" and the firewall log read live. With standard accounts and low-spec machines:

| Plan | Day 06 does instead |
|------|---------------------|
| Trainees capture with Wireshark | **The trainer captures live**; the class works from a **paper packet list** (Sample Data §1) that matches the capture. Trainees with admin may capture their own for PM Task 1 |
| Read `pfirewall.log` on the trainee machine | Enabling and reading it needs admin, so a **supplied `Day_06_pfirewall.log`** carries the findings; the trainer shows the real one once |
| Nmap on the lab subnet | Still deferred (authorisation) — the **lab-subnet diagram** is on paper (§4); the localhost scan was Day 04 |

## The five topics of Day 06

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **6.1** | **Read the Wire** — one minute of packets: DNS, the handshake, TLS, plaintext HTTP | knowledge 1.4 | 25 min + Activity 1 |
| **6.2** | **The Web Server From Both Sides** — run it, request it, make every status code happen | knowledge 1.2 | 20 min + Activity 2 |
| **6.3** | **Ports, NAT and the Router** — your port map; the lab subnet; the port forward nobody documented | knowledge 1.4 | 20 min + Activity 3 |
| **6.4** | **The Firewall Log** — the format, and the four things hiding in it | knowledge 1.5, 1.6 | 20 min + Activity 4 |
| **6.5** | **Parser v2** — one script, two logs | knowledge 1.3 | 30 min follow-along |

---

## Competency map

### Core unit — `CS-ICT251101`, underpinning knowledge

**Required knowledge today:** 1.2 web server and website architecture, 1.3 scripting, 1.4 network infrastructure (LAN, WAN, port forwarding), 1.5 sources of detection alert (firewall — previewed), 1.6 log and detection management (previewed).

**Required skills today:** computer operation, interpreting work instructions (the recipes), analytical (the findings in the log), communication (each finding written as one sentence someone else can act on).

### Basic and common units delivered

| Code | How it appears |
|------|---------------|
| `ICT311203` Perform computer operations | Start a server, drive a client, run a script, **stop the server** — and file the output |
| `400311106` Access and maintain information | The packet list, log and outputs hashed and registered; nothing captured from anyone else's traffic |
| `400311107` Practice OSH *(light)* | The "only your own machine, only your own traffic" rule stated as a professional-conduct rule |
| `ICT315202` Apply quality standards | LO2 — the register row self-checked (PM Task 6) |

> **Still outstanding — say it:** the **Wazuh SIEM server**, the **Day 01 lab OSH checklist + green pledge**, and — from today — the **lab-subnet Nmap sweep** (needs the lab and written authorisation).

---

## The idea that anchors the whole day

> **Every connection leaves a line somewhere — on the wire, in the server's log, in the firewall's log. An analyst knows which line to read, and reads it from both ends.**

Three habits come out of that, and they are the three sentences of the day:
1. **A connection is three packets; a name is one question and one answer; on HTTPS only the SNI is readable.**
2. **2xx fine · 3xx elsewhere · 4xx the client's fault · 5xx the server's fault.**
3. **One source, many ports = a scan; one source, one port, a steady rhythm = a script; outbound after hours = ask why.**

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. Find, in a packet list, the **DNS answer**, the **three-way handshake**, the **SNI** in a Client Hello, a **plaintext GET**, and a connection that was **never answered**.
2. Run a **web server** and a client on the same machine and **make 200, 301, 404 and 501 happen** on purpose — and read them in the server's log.
3. Produce their machine's **port map** — port, process, expected or not — and explain **NAT** and a **port forward** on the lab diagram.
4. Read a **firewall log** raw and find a scan, a brute-force rhythm, and a blocked outbound.
5. Read **parser v2**, run it on two logs, and change one line safely.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 05 · the "only your own traffic" rule | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 25 | 3–4 | **Topic 6.1** + **Demo 1** Read the wire — live capture, four filters | Demonstration | 6.1 |
| 8:40 | 15 | 5 | **Activity 1** "Find the Handshake" | Breakout teams | 6.1 |
| 8:55 | 20 | 6 | **Topic 6.2** + **Demo 2** The web server from both sides | Follow-along | 6.2 |
| 9:15 | 25 | 7 | **Activity 2** "Make the Status Codes Happen" | Individually, observed | 6.2 |
| 9:40 | 20 | 8 | **Topic 6.3** + **Demo 3** Ports, NAT and the router | Follow-along | 6.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 15 | 9 | **Activity 3** "Your Port Map" | Individually, pairs for help | 6.3 |
| 10:25 | 20 | 10–11 | **Topic 6.4** + **Demo 4** The firewall log | Follow-along | 6.4 |
| 10:45 | 20 | 12 | **Activity 4** "Read the Firewall Log" | Breakout teams | 6.4 |
| 11:05 | 30 | 13–14 | **Topic 6.5** + **Demo 5** Parser v2 — read, run, change one line (trainees run alongside) | Follow-along | 6.5 |
| 11:35 | 10 | 15 | Afternoon brief · **stop the server** · close | Whole class | — |

Morning sums to 225 (8:00 → 11:45). Lecture time is about 80 minutes.

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 30 minutes.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Annotated capture — five findings on the packet list (or your own 60-second capture) | 25 | Annotated capture sheet |
| 2 | Port map of your own machine + the lab-subnet diagram with the port forwards marked and one flagged | 25 | Port map + diagram |
| 3 | Access-log worksheet — six lines from Day 04's `Day_5_access_log.txt` decoded, plus your own server's log lines from Activity 2 | 25 | Access-log worksheet |
| 4 | Firewall-log worksheet — the four findings in `Day_06_pfirewall.log`, each as one sentence someone could act on | 25 | Firewall-log worksheet |
| 5 | Parser v2 — run on both logs (output pasted), then one line changed and re-run | 30 | 2 outputs + the changed line + new output |
| 6 | Evidence register — every file today named, hashed, logged; one row self-checked | 10 | Register + self-check |
| 7 | Reflection | 10 | Three answers |

---

## Before the day
### The night before
- [ ] **Wireshark + Npcap** on your machine; one test capture of `http://localhost:8000` and one HTTPS site; the four filters typed and working
- [ ] Build the `Documents\www` folder (Sample Data §2), start `http.server`, cause 200 / 404 / 301 / 501 and read each in the server window
- [ ] Turn on Defender Firewall logging on your machine (admin) so Demo 4 can show the **real** `pfirewall.log` for ten seconds before switching to the supplied file
- [ ] Run `Day_06_fw_parser.py` on both files; confirm the expected outputs in §6
- [ ] Run the port-map command; know which of your own listeners is which
- [ ] Have the router screenshot (Resources Part 3) — your own router's port-forwarding page, with anything private blurred
- [ ] Take the rest of the fallback screenshots

### On the morning
- [ ] Breakout rooms (Activities 1 and 4); chat visible
- [ ] Activity Pack, Handout, Resources, **`Day_06_pfirewall.log` and `Day_06_fw_parser.py`** sent; remind them to have `Day_5_log_parser.py` and `Day_5_access_log.txt`
- [ ] Observation sheet (Resources Part 5) open at 9:15
- [ ] Collect outstanding Day 01–05 evidence in the first fifteen minutes

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 6.1 — READ THE WIRE
### 8:15–8:55 with Demo 1 and Activity 1 · Slides 3–5 · knowledge 1.4

### The point
Day 04 ended with a five-minute glimpse of Wireshark. Today the class reads one minute of packets properly — and learns that five things are findable in any capture.

### What you must know
The packet list in Sample Data §1 and the **four filters**: `dns` · `tcp.flags.syn==1 && tcp.flags.ack==0` · `tls.handshake.type==1` · `http`. What each finds: the name lookup (a question and an answer), every new connection attempt (the first SYN), the **SNI** (the site's name, in the clear, inside an otherwise encrypted TLS session), and plaintext HTTP (readable only on port 80/8000 — never on 443). The handshake is **SYN → SYN-ACK → ACK**; a **SYN with no SYN-ACK, retransmitted** is a connection that was tried and never answered — packets 22–24 to the Tor node.

**Only your own traffic.** Say it as a professional-conduct rule before the capture starts: you capture on your own machine, your own browsing; never on a network you do not own or a colleague's traffic. That is the same rule as Day 04's localhost-only scan.

### Key messages
- A connection is three packets. A name is one question and one answer.
- On HTTPS you cannot read the content — but the SNI names the site, and the addresses and timing are still evidence.
- A SYN that is never answered is still a fact: something *tried*.

### Mistakes to expect
- Trainees expect to read passwords. Show that HTTPS content is opaque; the value is *who, when, where*.
- Trainees read the SYN-ACK as the client. Source and destination swap on each line — point at the columns.

---

## TOPIC 6.2 — THE WEB SERVER FROM BOTH SIDES
### 8:55–9:40 with Demo 2 and Activity 2 · Slides 6–7 · knowledge 1.2

### The point
Day 04 made one request. Today the trainee **is** the server and the client, and makes every status code happen on purpose so the numbers stop being abstract.

### What you must know
Sample Data §2: the `www` folder, `python -m http.server 8000` in window 1 (the server — every request prints there), browser and `curl.exe` in window 2 (the client). **200** exists · **404** missing · **301** a folder without the trailing slash · **501** an unsupported method via `curl.exe -X DELETE`. **403** and **500** come from Day 04's Apache log on paper. `curl.exe -I` shows headers only — including `Server:`, which a scanner reads on Day 25. The rule: **2xx / 3xx / 4xx client / 5xx server**.

**Activity 2 is observed:** the trainee runs the server, causes the four codes, and reads each line back from the server window — code and meaning.

### Key messages
- 2xx fine, 3xx elsewhere, 4xx the client's fault, 5xx the server's.
- The server's log is the other half of the story your browser sees. Read both ends.
- A burst of 404s from one address is someone guessing filenames.

### Mistakes to expect
- Port 8000 already in use (a Day 04 server left running). Use 8080 — and note that a forgotten server is itself a finding.
- Trainees close the server window to "tidy up" mid-activity. Two windows, both open, until the end.
- `curl` without `.exe` in PowerShell is an alias for `Invoke-WebRequest` and behaves differently. Always `curl.exe`.

---

## TOPIC 6.3 — PORTS, NAT AND THE ROUTER
### 9:40–10:25 with Demo 3 and Activity 3 · Slides 8–9 · knowledge 1.4

### The point
"Which ports are open on my machine and why" — a table every trainee can produce — then NAT and the port forward on a drawn network, with one forward that should not be there.

### What you must know
The port-map command and the table of normal Windows listeners in Sample Data §3 (135, 139, 445, 5040, 5357, 7680, 49664–49670). Three questions per row: **what is it · who owns it · should it be there.** 3389 open on a laptop is a finding; 8000 open after class is a finding. Then §4: the lab subnet (every Phase B host lives on it — draw it once, reuse it for weeks), NAT in one line, and the two forwards — `:443 → .22` documented, `:3389 → .31` **not** — which is why `203.0.113.45` is hammering RDP in the firewall log an hour later. Show your own router's forwarding page (screenshot, blurred) so the concept has a real screen.

### Key messages
- What is it, who owns it, should it be there — three questions for every listening port.
- NAT: inside many addresses, outside one. A port forward is a hole punched from outside to one inside machine — every one must be documented.
- The undocumented 3389 forward is how a workstation ends up on the internet.

### Mistakes to expect
- Trainees panic at 445 or 135. Normal on Windows — say so, then say why 445 is still the most-attacked port.
- Trainees confuse the port forward's *public* and *private* sides. Draw the arrow every time.

---

## TOPIC 6.4 — THE FIREWALL LOG
### 10:25–11:05 with Demo 4 and Activity 4 · Slides 10–12 · knowledge 1.5, 1.6

### The point
Day 04 mentioned the firewall log exists. Today the class reads one raw and finds four things in it — the first "detection source" they meet before Phase B names the seven.

### What you must know
Sample Data §5: where the real file lives, how logging is switched on (admin — you, not them), the W3C format read left to right (**action · src · dst · dst-port · flags · path**), and the four findings: the **RDP rhythm** (one source, one port, every three seconds), the **port scan** (one source, one *source* port, twelve destination ports in two seconds), the **blocked outbound to the Tor node** after hours (path = SEND — something on WKS-311 tried), and the **allowed** connections to the practice server (what normal looks like). Show your real `pfirewall.log` for ten seconds, then switch to the supplied file so everyone reads the same lines.

### Key messages
- Action, source, destination, port, path. Five columns carry the story.
- One source, many ports = a scan. One source, one port, steady rhythm = a script. Outbound after hours = ask why.
- DROP is the firewall doing its job — but a dropped *outbound* means something inside tried. That is the finding.

### Mistakes to expect
- Trainees stop at "it was dropped, so fine". The outbound drops to `185.220.101.1` are the most important lines in the file.
- Reading src-port as the target. The scanner's *source* port is constant; its *destination* port changes.

---

## TOPIC 6.5 — PARSER v2
### 11:05–11:35 with Demo 5 · Slides 13–14 · knowledge 1.3

### The point
Day 04's parser read one log. Version 2 reads two, chosen by the first line. The class **reads** it (Day 04's rule: read a script before you run it), **runs** it on both files, and **changes one line** — safely, because it only reads.

### What you must know
Sample Data §6: the access-log part is Day 04's code moved into a function; the firewall part skips `#` lines, splits on spaces, takes eight fields, counts; the last six lines choose by `#Version`. Expected outputs are printed there. The **top line of each output block is a finding**: `198.51.100.23 12` is the scan; `3389 7` is the RDP hammering; and `203.0.113.45` — top of the DROP list *and* top of Day 04's access-log IPs — is one attacker in two logs. The one-line change for PM Task 5 is `most_common(5)` → `most_common(10)`, or a fourth counter for SEND vs RECEIVE.

### Key messages
- Read it, then run it — it only reads files; it sends nothing.
- A parser turns twenty-eight lines into four findings in three seconds. That is what scripting is for on this desk.
- One address at the top of two different logs is one attacker. Cross-reference.

### Mistakes to expect
- `python` not found (Day 04's install missing). `py` launcher, or the Microsoft Store Python; ten minutes lost if not checked the night before.
- Editing the wrong line and breaking the indentation. Show the one line, change it, run, undo.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 06 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| Annotated capture — five findings | PM Task 1 + Activity 1 | knowledge 1.4 |
| Port map + lab-subnet diagram with forwards marked | PM Task 2 + Activity 3 | knowledge 1.4 (LAN, WAN, port forwarding) |
| Access-log worksheet — six lines + own server log | PM Task 3 + Activity 2 | knowledge 1.2 |
| Firewall-log worksheet — four findings as actionable sentences | PM Task 4 + Activity 4 | knowledge 1.5, 1.6 |
| Parser v2 — two outputs + the change | PM Task 5 + Demo 5 | knowledge 1.3 |
| Evidence register + 1 self-check | PM Task 6 | `400311106` · `ICT315202` LO2 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

## Observation during the live session

**Activity 2 "Make the Status Codes Happen" is observed.** Observation sheet from `Day_06_Resources.md` open at 9:15. Two things:
1. **Did the trainee run the server and the client in two windows and cause 200, 404, 301 and 501 on purpose?**
2. **Did the trainee read each line back from the server window — code and its meaning — and say which side (client / server) was "at fault"?**

## How the afternoon is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Five findings located by packet number with the filter that finds each · a port map with every row named and 3389 / 8000 judged correctly · the undocumented forward flagged with a reason · status codes decoded with the fault side named · the four firewall findings as sentences that name source, target, port, rhythm and what to do · parser run on both files with a working one-line change |
| **Not yet competent** | "HTTPS so nothing to see" · a port map with numbers but no process or judgement · a diagram with no arrow direction on the forwards · "dropped, so fine" on the outbound Tor lines · parser output pasted without the change, or a change that breaks it |

Full keys in `Day_06_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| Wireshark/Npcap not working on your machine | Demo 1 from the fallback screenshots + the paper list; the activity is on paper anyway |
| `python` not found on a trainee machine | `py -m http.server 8000`; if no Python at all, pair them — one machine, two people, both windows visible |
| Port 8000 in use | 8080, and note the forgotten server as a finding |
| `curl.exe` missing (old Windows 10) | `Invoke-WebRequest -Method DELETE http://localhost:8000/` produces the same 501 |
| No admin to enable firewall logging | That is the design — the supplied file carries the day; show yours for ten seconds |
| A trainee's port map shows 3389 | Excellent — a real finding on a real machine; have them write it as they would report it |
| Activity 2 overruns | 200 and 404 observed; 301 and 501 → PM Task 3 |
| Behind at 11:05 | Demo 5 — run only; the read-through → PM Task 5 with §6 as the guide |

---

## End of day checklist
- [ ] Activity 2 observation notes written up
- [ ] **Every trainee's `http.server` stopped** (ask in chat before closing)
- [ ] Capture sheets, port maps, firewall worksheets, parser outputs chased
- [ ] Outstanding still listed: Wazuh server, Day 01 lab docs, **lab-subnet Nmap sweep**
- [ ] Tomorrow announced: **Day 07 — Threat intelligence and the attack framework** (MITRE ATT&CK, malware behaviours, the lookup desks in depth). Browser day; same hours

## What to say at the close
Two days ago the class opened Event Viewer and saw a wall. Yesterday they learned to ask it a question. Today they did the same on the wire: read a minute of packets and found five things, ran a web server and broke it on purpose in four different ways, mapped their own ports, read a firewall log raw and found a scan, a brute-force rhythm and a machine trying to reach a Tor node — and their parser now reads two logs. Every connection leaves a line somewhere; they now know which line to read. Tomorrow: who is on the other end of those lines, and how attackers actually behave. Say that, and let them go — after they stop their servers.
