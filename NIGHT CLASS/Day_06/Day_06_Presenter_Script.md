# DAY 06 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 06 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics are notes — never read them.)* Times match the Instructor Guide. Demo steps are in `Day_06_Demonstration_Guide.md`; this script cues the switch. Cut order at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 05, the rule |
| 2 | 8:10 | Five topics |
| 3–4 | 8:15 | Topic 6.1 → Demo 1 read the wire |
| 5 | 8:40 | Activity 1 Find the Handshake |
| 6 | 8:55 | Topic 6.2 → Demo 2 the web server from both sides |
| 7 | 9:15 | Activity 2 Make the Status Codes Happen (observed) |
| 8 | 9:40 | Topic 6.3 → Demo 3 ports, NAT, the router |
| — | 10:00 | Break |
| 9 | 10:10 | Activity 3 Your Port Map |
| 10–11 | 10:25 | Topic 6.4 → Demo 4 the firewall log |
| 12 | 10:45 | Activity 4 Read the Firewall Log |
| 13–14 | 11:05 | Topic 6.5 → Demo 5 parser v2 (follow-along) |
| 15 | 11:35 | Afternoon brief, stop the server, close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 6. Two days ago Event Viewer was a wall; yesterday you learned to ask it a question. Today we do the same thing on the wire. Day 4 showed you a web request and a glimpse of Wireshark. Today you read a full minute of packets and find five things in it. You run a web server yourself and break it on purpose, four different ways. You map every port your own machine is listening on. You read the firewall's own log, raw, and find a scan, a brute-force script, and a machine trying to reach a Tor node. And your parser grows up."

> "Quick recall — yesterday, what are the three things you read on every Autoruns entry?" *(Path, publisher, name.)* "Good. Today it's action, source, destination, port, path."

> "One rule before anything, and it is a professional rule, not a technical one: today you capture only your own machine's traffic, on your own network. Never a colleague's. Never the office's. Same rule as Day 4's localhost-only scan."

*(Collect outstanding evidence. Announce role rotation. Confirm everyone has `Day_06_pfirewall.log`, `Day_06_fw_parser.py`, and yesterday's parser and access log.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 6.1, read the wire — one minute of packets, four filters. 6.2, the web server from both sides — you are the server and the client. 6.3, ports, NAT and the router — your port map, and a port forward nobody documented. 6.4, the firewall log — four findings in twenty-eight lines. And 6.5, parser version 2 — one script, two logs. One idea runs all five: every connection leaves a line somewhere, and you learn which line to read."

# SLIDES 3–4 — TOPIC 6.1: READ THE WIRE → DEMO 1
### 8:15 – 8:40 · 25 minutes
> "Wireshark shows every packet. Nobody reads every packet. You type a filter and find one of five things: the name lookup, every new connection, the handshake, the one readable thing on HTTPS, and plaintext HTTP. Watch — I'll capture one minute of my own browsing and find all five."

*(Run **Demonstration 1** — the rule, the capture, `dns`, the SYN filter, Follow TCP Stream, the SNI, `http`, then the unanswered SYNs on paper.)*

> "A connection is three packets. A name is one question and one answer. On HTTPS you cannot read the content — but the SNI names the site, and addresses and times are still evidence. And a SYN nobody answered is still a fact: something tried."

# SLIDE 5 — ACTIVITY 1: FIND THE HANDSHAKE
### 8:40 – 8:55 · 15 minutes
> "Teams. The printed packet list — twenty-four lines. Find five things and write the packet numbers: the DNS answer for the site; the three packets of the handshake to it; the one packet that names the site in plain text even though it's HTTPS; a request and its response you can read word for word; and a connection that was tried and never answered — and where it was going. Bonus: which filter finds each one."

*(Packet list in `Day_06_Sample_Data.md` §1. Answers in Solutions. Bring out 22–24 — the Tor node.)*

# SLIDE 6 — TOPIC 6.2: THE WEB SERVER FROM BOTH SIDES → DEMO 2
### 8:55 – 9:15 · 20 minutes
> "On Day 4 you made one request. Today you are the server AND the client. Two windows: one runs the server and prints a line for every request; the other asks. And we make every status code happen on purpose, so the numbers stop being abstract. Follow along — build the www folder as I do."

*(Run **Demonstration 2** — server in window 1, then 200, 404, 301, 501, `curl.exe -I`, the rule.)*

> "2xx fine. 3xx elsewhere. 4xx — the client asked wrong. 5xx — the server failed. And read both ends: the browser sees the page, the server's window sees the line."

# SLIDE 7 — ACTIVITY 2: MAKE THE STATUS CODES HAPPEN
### 9:15 – 9:40 · 25 minutes · OBSERVED
> "Your own machine. Start your server in one window. In the other, cause a 200, a 404, a 301 and a 501 — the recipes are in your pack. For each one, read the server's line back to me: the code, what it means, and whose fault it is — client or server. I'm watching for two things: two windows with four codes caused on purpose, and each line read back with its meaning."

*(Observation sheet open. Circulate. Bring them back at 9:40. Servers stay running — they need them for Activity 3.)*

# SLIDE 8 — TOPIC 6.3: PORTS, NAT AND THE ROUTER → DEMO 3
### 9:40 – 10:00 · 20 minutes
> "Now: which ports is my machine listening on, and why? Three questions for every row — what is it, who owns it, should it be there. Then the network the whole of Phase B lives on — the lab subnet — and what NAT and a port forward are. One of the lab's two forwards should not exist. Follow along for the port map."

*(Run **Demonstration 3** — the port-map command, NAT in one line, the router screenshot, the two forwards, draw the arrow.)*

> "135, 139, 445 — Windows, normal. 8000, python — that's my server, and it closes at four. 3389 on a laptop — a finding. And a port forward is a hole from the outside to one inside machine. Every one needs a name of who approved it. No name, it's a finding."

# BREAK
### 10:00 – 10:10

# SLIDE 9 — ACTIVITY 3: YOUR PORT MAP
### 10:10 – 10:25 · 15 minutes
> "Your own machine. Run the port-map line. For every row: port, process, what it is, and expected or not. Your own server on 8000 should be there — write it, and write when you'll close it. Anyone who finds 3389 or something they can't name: that's a finding — write it as you'd report it. Pairs for help."

*(Circulate. The normal-listeners table is in their handout.)*

# SLIDES 10–11 — TOPIC 6.4: THE FIREWALL LOG → DEMO 4
### 10:25 – 10:45 · 20 minutes
> "The firewall keeps its own diary — every connection it allowed or dropped. Turning it on needs admin, so I'll show you my real one for ten seconds, and then we all read the same supplied file. Five columns carry the story: action, source, destination, destination port, path — RECEIVE is inbound, SEND is outbound. There are four things hiding in twenty-eight lines. I'll find three with you; your teams find all four."

*(Run **Demonstration 4** — the real log, the header, one line left to right, the RDP rhythm, the port scan, the outbound Tor drops, the ALLOW lines, the count.)*

> "One source, many destination ports, two seconds — a scan. One source, one port, every three seconds — a script. And the one that matters most: DROP with path SEND, after hours. The firewall stopped it — but something inside tried. 'Dropped, so fine' is the wrong reading."

# SLIDE 12 — ACTIVITY 4: READ THE FIREWALL LOG
### 10:45 – 11:05 · 20 minutes
> "Teams. The whole file. Find all four findings and write each as one sentence someone could act on: who, to what, which port, what pattern, and what you'd do. Also: how many DROP lines are there in total? Count by eye — in twenty minutes you'll count them in one second."

*(Findings in Sample Data §5. Answers in Solutions. Make sure every team writes the outbound Tor finding as a finding, not as "blocked, fine".)*

# SLIDES 13–14 — TOPIC 6.5: PARSER v2 → DEMO 5
### 11:05 – 11:35 · 30 minutes · everyone runs every step
> "Day 4's parser read one kind of log. Version 2 reads two, and picks which by looking at the first line. Day 4's rule first: read it before you run it. Then run it on the firewall log, then on Day 4's access log. Then we change one line. Open the file with me."

*(Run **Demonstration 5** — read the three parts, run on the firewall log, run on the access log, the cross-reference, change `most_common(5)` to `10`.)*

> "One second, four findings. And look at the top address in both logs: 203.0.113.45 — hammering RDP in the firewall log, and the top requester in the web log with seven 404s. Two logs, one attacker. Cross-referencing is the whole job. And a script is changed one line at a time: change, save, run, look."

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:35 – 11:45 · 10 minutes
> "This afternoon: the annotated capture — five findings with packet numbers and the filter that finds each, or your own sixty-second capture if you can install Wireshark; your port map, plus the lab-subnet diagram with both forwards drawn and one flagged; the access-log worksheet — six lines from Day 4's log decoded, plus your own server's lines from this morning; the firewall-log worksheet — four findings as sentences someone could act on; parser v2 run on both logs with one line changed; the evidence register with one row self-checked; and the reflection. Marked as always — the reason matters more than the answer."

> "And right now, before you go: stop your server. Ctrl+C in the server window. Then run the port-map line once more and confirm 8000 is gone. A web server left running is a finding on your own machine tomorrow. Type 'stopped' in chat."

> "Every connection leaves a line somewhere — on the wire, in the server's log, in the firewall's log. You now know which line to read, and how to read it from both ends. Tomorrow, Day 7: who is on the other end of those lines — threat intelligence, and how attackers actually behave. It's a browser day. Same hours. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
1. Demo 1 — skip Follow TCP Stream; use the paper list for the handshake
2. Activity 1 to three findings (DNS answer, SNI, the unanswered SYN)
3. Demo 3 — skip the router screenshot; the slide's table carries it
4. Demo 5 — run only, no read-through; the read-through → PM Task 5
**Never cut** Demo 2 (the server), Activity 2 (observed) or Demo 4 (the firewall log).

# THE THREE SENTENCES OF THE DAY
1. **A connection is three packets; a name is one question and one answer; on HTTPS only the SNI is readable.**
2. **2xx fine · 3xx elsewhere · 4xx the client's fault · 5xx the server's fault.**
3. **One source, many ports = a scan; one source, one port, steady rhythm = a script; outbound after hours = ask why.**
