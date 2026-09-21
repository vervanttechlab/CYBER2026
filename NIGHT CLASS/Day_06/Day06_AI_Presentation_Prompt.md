============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (30-Day Program) — Day 06
Network and Web Evidence in Depth — the Wire, the Web Server, the Firewall Log
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_06_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 06 IS:
Day 06 of the 30-day program is the third "underpinning" day. Day 04 showed the
wire and one web request once; Day 06 reads both as evidence: a real one-minute
packet capture with four filters, a web server the trainee runs from both sides
(making 200 / 301 / 404 / 501 happen on purpose), the trainee's own port map plus
NAT and a port forward on the lab subnet, the Windows firewall log read raw (four
findings), and parser v2 that reads two kinds of log. It delivers required
knowledge 1.2 (web architecture), 1.3 (scripting) and 1.4 (network, port
forwarding).

TWO HARD CONSTRAINTS:
- NO SIEM SERVER, NO ADMIN. The capture is the trainer's own traffic; the web
  server runs on each trainee's OWN machine; the firewall log is a SUPPLIED file.
  Nothing touches anyone else's network — say so on slide 1.
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone. English is a
  second language.

THE FIVE TOPICS:
  6.1  Read the Wire (DNS, the handshake, TLS/SNI, plaintext HTTP)
  6.2  The Web Server From Both Sides (status codes on purpose)
  6.3  Ports, NAT and the Router (port map; the lab subnet; the undocumented forward)
  6.4  The Firewall Log (format; scan, script rhythm, blocked outbound)
  6.5  Parser v2 (one script, two logs)

DAY 06 IS A BLENDED DAY:
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Find the Handshake (teams, on a printed packet list); 2 Make
the Status Codes Happen (own machine, observed); 3 Your Port Map (own machine);
4 Read the Firewall Log (teams, the supplied file). Plus a 30-minute follow-along
for parser v2.

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables as real tables, commands and log lines in monospace. No agenda, thank-you, or Q&A slide.

Day 06 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, complete beginners. Short sentences, common words, calm tone. Define every term the first time (packet, filter, handshake, SYN, SNI, status code, port, NAT, port forward, firewall log, parser).

The one idea of the day, repeated plainly: EVERY CONNECTION LEAVES A LINE SOMEWHERE — on the wire, in the server's log, in the firewall's log — and an analyst knows which line to read, from both ends. Carry from Day 04: only your own machine, only your own traffic.

SLIDE 1 — TITLE
Title: "Network and Web Evidence in Depth"
Subtitle: "Cyber Threat Monitoring Level I, Day 06 of 30 — the wire, the web server, the firewall log"
Kicker: "Live demo 8:00-11:45  |  Self-study 1:00-4:00  |  Your own machine, your own traffic — nobody else's"
Small rule box: "You capture only your own machine's traffic on a network you own. Never a colleague's. Never the office's. (Same rule as Day 04's localhost-only scan.)"
Visual: a calm navy title slide. Three horizontal lines — a wire, a server log, a firewall log — each with a small magnifying glass on it.

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: Which Line to Read"
Table (Topic / What you will be able to do):
6.1 Read the Wire | Find the DNS answer, the handshake, the SNI, plaintext HTTP, and an unanswered SYN in a packet list
6.2 The Web Server From Both Sides | Run a server and a client and make 200, 301, 404 and 501 happen on purpose
6.3 Ports, NAT and the Router | Map your own listening ports; explain NAT and flag an undocumented port forward
6.4 The Firewall Log | Read the raw log and find a scan, a script's rhythm and a blocked outbound
6.5 Parser v2 | Read, run and change a script that reads two kinds of log
Add the line: "Every connection leaves a line somewhere. Today you learn which line to read."
Visual: five numbered topic cards.

SLIDE 3 — READ THE WIRE (Topic 6.1, part 1)
Title: "One Minute of Packets, Four Filters"
Table (Filter / Finds / Example):
dns | The name lookup — one question, one answer | Standard query A www.example-client.ph → A 203.0.113.80
tcp.flags.syn==1 && tcp.flags.ack==0 | Every NEW connection attempt (the first SYN) | 51402 → 443 [SYN]
tls.handshake.type==1 | The Client Hello — the SNI names the site even on HTTPS | Client Hello (SNI=www.example-client.ph)
http | Plaintext requests — readable only on HTTP, never on HTTPS | GET /about.html HTTP/1.1 → 200 OK
Big line: "A connection is three packets: SYN → SYN-ACK → ACK."
Visual: a packet list with four coloured highlight bands.

SLIDE 4 — WHAT HTTPS HIDES, AND WHAT IT DOESN'T (Topic 6.1, part 2)
Title: "You Cannot Read the Page. You Can Still Read Who, When, Where."
Two columns: HIDDEN on HTTPS — the page content, passwords, form data · STILL VISIBLE — the site name (SNI), both addresses, the port, the time, the size, how many times.
Then a three-line monospace excerpt:
22  41.007  192.168.10.31 → 185.220.101.1  443  [SYN]
23  44.010  192.168.10.31 → 185.220.101.1  443  [SYN]  Retransmission
24  47.014  192.168.10.31 → 185.220.101.1  443  [SYN]  Retransmission
Big line: "A SYN that is never answered is still a fact: something TRIED. (That is Day 03's Tor-node case, on the wire.)"
Visual: a padlock over a page, with the envelope's address label still readable.

SLIDE 5 — ACTIVITY 1: FIND THE HANDSHAKE
Title: "Activity 1 — Five Things in Twenty-Four Packets"
Instructions as steps:
- In your team, use the printed packet list.
- Find and write the packet numbers for: the DNS answer · the three-packet handshake · the SNI · a readable request and its response · a connection tried and never answered (and where to).
- Bonus: which of the four filters finds each one?
Big line: "Source and destination swap on every reply. Read the columns."
Visual: a packet list with five empty circles to fill in.

SLIDE 6 — THE WEB SERVER FROM BOTH SIDES (Topic 6.2)
Title: "Be the Server. Be the Client. Break It on Purpose."
Show in monospace (window 1): python -m http.server 8000
Table (Code / Meaning / Make it happen / The server logs):
200 | Found it | browser → /about.html | "GET /about.html HTTP/1.1" 200 -
404 | No such file | browser → /nothere.html | "GET /nothere.html HTTP/1.1" 404 -
301 | Lives elsewhere (folder without the slash) | browser → /docs | 301 then "GET /docs/" 200
501 | Server does not do that method | curl.exe -X DELETE http://localhost:8000/ | code 501, Unsupported method ('DELETE')
403 / 500 | Forbidden / server broke | (from Day 04's Apache log, on paper) | 403 · 500
Big line: "2xx fine · 3xx elsewhere · 4xx the CLIENT's fault · 5xx the SERVER's fault."
Visual: two windows side by side — browser on the left, server log on the right, an arrow each way.

SLIDE 7 — ACTIVITY 2: MAKE THE STATUS CODES HAPPEN
Title: "Activity 2 — Four Codes, Two Windows"
Instructions as steps:
- Window 1: start your server in Documents\www. Window 2 and the browser: the client.
- Cause a 200, a 404, a 301 and a 501 — recipes in your pack.
- For each: read the SERVER's line back — the code, its meaning, and whose fault (client or server).
- Leave the server running — you need it in Activity 3.
Big line: "This one is watched: four codes caused on purpose, each line read back with its meaning."
Visual: a two-window mock-up with four log lines appearing.

SLIDE 8 — PORTS, NAT AND THE ROUTER (Topic 6.3)
Title: "What Is It, Who Owns It, Should It Be There?"
Left — the port map in monospace: Get-NetTCPConnection -State Listen | Select LocalPort, OwningProcess … | Sort-Object LocalPort
Small table (Port / Process / Verdict): 135 · 139 · 445 | Windows | normal ·· 5040 · 7680 · 4966x | Windows | normal ·· 8000 | python | yours — close it by 4:00 ·· 3389 | TermService | on a laptop, a FINDING
Right — NAT and the lab subnet: "Inside: 192.168.10.x, many machines. Outside: 203.0.113.5, one address. A PORT FORWARD is a hole from outside to ONE inside machine."
Two arrows: 203.0.113.5:443 → 192.168.10.22 (web — documented ✓) · 203.0.113.5:3389 → 192.168.10.31 (RDP to a workstation — nobody approved it ✗)
Big line: "Every forward needs the name of who approved it. No name = a finding."
Visual: a router box with two arrows through it, one green, one red.

SLIDE 9 — ACTIVITY 3: YOUR PORT MAP
Title: "Activity 3 — Every Port Your Machine Is Listening On"
Instructions as steps:
- Run the port-map line on your own machine.
- For each row: port, process, what it is, expected or not — the normal-listeners table is in your handout.
- Your own server on 8000 should be there. Write it, and write when you will close it.
- 3389, or a port you cannot name? That is a finding — write it as you would report it.
Big line: "Three questions per row. The reason is what is marked."
Visual: a short table with green and amber dots.

SLIDE 10 — THE FIREWALL LOG (Topic 6.4, part 1)
Title: "The Firewall Keeps a Diary"
Show in monospace, the field line and one record:
#Fields: date time action protocol src-ip dst-ip src-port dst-port size tcpflags ... path
2026-09-18 08:03:45 DROP TCP 203.0.113.45 192.168.10.31 51234 3389 52 S ... RECEIVE
Five callouts on the record: ACTION (ALLOW / DROP) · SOURCE · DESTINATION · DESTINATION PORT · PATH (RECEIVE = inbound, SEND = outbound).
Add: "Real file: %systemroot%\system32\LogFiles\Firewall\pfirewall.log — turning it on needs admin, so today we read a supplied copy."
Big line: "Five columns carry the story."
Visual: one log line with five labelled arrows.

SLIDE 11 — THREE PATTERNS TO RECOGNISE (Topic 6.4, part 2)
Title: "Scan, Script, and the Outbound That Matters"
Three cards, each with a two-line monospace sample:
A SCAN — one source, one source port, MANY destination ports, seconds apart. "198.51.100.23 → :21 :22 :23 :25 :80 … 12 ports in 2 s"
A SCRIPT — one source, ONE port, a steady rhythm. "203.0.113.45 → :3389 every 3 seconds, six times"
A BLOCKED OUTBOUND — path SEND, after hours, DROP. "192.168.10.31 → 185.220.101.1:443 SEND DROP ×4 at 18:41"
Big line: "'Dropped, so fine' is the wrong reading. A dropped OUTBOUND means something inside tried. That is the finding."
Visual: three cards; the third with a small amber flag.

SLIDE 12 — ACTIVITY 4: READ THE FIREWALL LOG
Title: "Activity 4 — Four Findings in Twenty-Eight Lines"
Instructions as steps:
- In your team, read the whole supplied file.
- Find the four findings. Write each as ONE sentence someone could act on: who, to what, which port, what pattern, what you would do.
- Count the DROP lines by eye. (In twenty minutes a script will do it in one second.)
Big line: "Know what normal looks like — the ALLOW lines — to see the rest."
Visual: a log page with four highlighted blocks.

SLIDE 13 — PARSER v2 (Topic 6.5, part 1)
Title: "One Script, Two Logs"
Three parts as cards: PART 1 — Day 04's access-log code, moved into a function (unchanged) · PART 2 — NEW: the firewall log — skip # lines, split on spaces, first eight fields, count ALLOW/DROP, DROP by source, DROP by port · PART 3 — the last six lines: first line starts with #Version? firewall. Otherwise access log.
Add the line: "Read it before you run it. It only READS. It sends nothing."
Show in monospace: python .\Day_06_fw_parser.py .\Day_06_pfirewall.log
Visual: one script icon with two log files feeding in.

SLIDE 14 — WHAT THE PARSER FINDS (Topic 6.5, part 2)
Title: "Twenty-Eight Lines → Four Findings in One Second"
Show the output in monospace:
Records by action:  ALLOW 6  DROP 22
DROP by source:  198.51.100.23 12  |  203.0.113.45 6  |  192.168.10.31 4
DROP by destination port (top 5):  3389 7  |  443 5  |  21 1 …
Then the cross-reference line: "Day 04's access log — top requester: 203.0.113.45, 14 requests, 7 of them 404s."
Big line: "One address at the top of two different logs = one attacker. Cross-referencing is the whole job."
Add: "Change one line safely: most_common(5) → most_common(10). Save. Run. Look. Undo if it breaks."
Visual: two log icons with a line connecting the same address in each.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark as the start of self-study. Keep the table.
Table (Task / Time / Hand in):
1 | Annotated capture — five findings with packet numbers and filters (or your own 60-second capture) | 25 min | Capture sheet
2 | Port map of your machine + the lab-subnet diagram with both forwards drawn, one flagged | 25 min | Port map + diagram
3 | Access-log worksheet — six lines from Day 04's log decoded + your own server lines | 25 min | Worksheet
4 | Firewall-log worksheet — four findings as actionable sentences | 25 min | Worksheet
5 | Parser v2 — run on both logs, change one line, run again | 30 min | 2 outputs + the change
6 | Evidence register — every file named, hashed, logged; one row self-checked | 10 min | Register + self-check
7 | Reflection | 10 min | Three answers
Red note (small): "Before you go: STOP YOUR SERVER (Ctrl+C) and confirm port 8000 is gone from your port map."
Closing line: "Every connection leaves a line somewhere. Next, Day 07: who is on the other end — threat intelligence and the attack framework."
Visual: a teal section band, the table, and a small "Day 6 of 30" progress bar.

============================================================
END OF PROMPT
============================================================
