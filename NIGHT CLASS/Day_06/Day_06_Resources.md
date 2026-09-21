# DAY 06 — RESOURCES AND MATERIALS
## Everything you need ready before 8:00 AM

---

## THE DAY 06 FILE SET

| File | Who gets it | When |
|------|------------|------|
| `Day_06_Instructor_Guide.md` | Trainer only | — |
| `Day_06_Presenter_Script.md` | **Trainer only. Words, slide by slide** | Second screen |
| `Day_06_Demonstration_Guide.md` | Trainer only | — |
| `Day_06_Solutions.docx` | **Trainer only. Never send to trainees** | — |
| `Day_06_Activity_Solutions.docx` | **Trainer only** — the morning activity keys, one page per activity | Second screen, 8:30–11:35 |
| `Day_06_Sample_Data.md` | Trainer — the packet list, recipes, port map, subnet, firewall findings, parser notes | — |
| `Day_06_Student_Handout.docx` | Every trainee | With the joining note, the night before |
| `Day_06_Student_Activity_Pack.docx` | Every trainee | With the joining note, the night before |
| **`Day_06_pfirewall.log`** | **Every trainee** — the firewall log they read | With the joining note |
| **`Day_06_fw_parser.py`** | **Every trainee** — parser v2 | With the joining note |
| `Day_06_Resources.md` | Trainer, and the trainee section | — |
| `Day06_AI_Presentation_Prompt.md` | Trainer only — the prompt the deck was built from | Before the day |

> Handout, Activity Pack and Solutions are **Word documents (.docx)**, not markdown, on request. The `.log` and `.py` are plain files — send them as attachments, not pasted into chat (chat mangles the spacing).

---
---

# PART 1 — WHAT THE TRAINER NEEDS

## Platform
| Item | Why |
|------|-----|
| Video platform with **breakout rooms** | Activities 1 and 4 |
| **Recording** on | Activity 2 is observed |
| **Chat**, visible | "stopped" confirmations at 11:40 |

## On the trainer's machine
| Item | Why |
|------|-----|
| **Wireshark + Npcap** (admin install, done the night before) | Demo 1 — the only live capture of the day |
| **Python 3** and the `Documents\www` folder from Sample Data §2 | Demo 2 |
| **Two PowerShell windows** side by side — one for the server, one for the client | Demos 2, 3, 5 |
| **`curl.exe`** (built into Windows 10 1803+) | Demo 2 |
| **Defender Firewall logging enabled** (admin, the night before) | Demo 4 — ten seconds of the real `pfirewall.log` |
| `Day_06_pfirewall.log`, `Day_06_fw_parser.py`, and Day 04's `Day_5_access_log.txt` in one folder | Demos 4–5 |
| A **screenshot of your own router's port-forwarding page**, private details blurred | Demo 3 |
| **Fallback screenshots** | Part 3 |

> **No server.** Everything runs on your own machine. The only admin steps are yours (Npcap, firewall logging) — trainees need neither.

## Printed or on paper
- `Day_06_Presenter_Script.md`
- The **packet list** (Sample Data §1) — one per team
- The **Activity 2 observation sheet** (Part 5)
- The **lab subnet table** (§4)

---
---

# PART 2 — WHAT EACH TRAINEE NEEDS

**Send with the joining note.**

| Item | Why |
|------|-----|
| A **Windows 10/11 machine** — standard account is fine | Every activity |
| **Python 3** working from Day 04 (`python --version` or `py --version`) | Activities 2, 3; Demo 5 |
| **`Day_06_pfirewall.log`** and **`Day_06_fw_parser.py`** saved in one folder with Day 04's **`Day_5_log_parser.py`** and **`Day_5_access_log.txt`** | Activity 4; Demo 5; PM Tasks 3–5 |
| **Camera and microphone** | Activity 2 is observed |
| The **Handout** and **Activity Pack** (Word docs) | They write in both |
| Their **Day 03 evidence register and class QA checklist** | PM Task 6 |
| *Optional:* **Wireshark** (or WiresharkPortable — no admin to *read* a capture; **Npcap needs admin to capture**) | PM Task 1 bonus only |
| A folder `C:\Evidence\Day_06\` | Everything goes here |

> Tell them in the joining note: **you will run a small web server on your own machine — and you will stop it before you leave.** And the rule: capture only your own traffic, on your own network.

---
---

# PART 3 — FALLBACK SCREENSHOTS
- [ ] Wireshark packet list, unfiltered (the "noise")
- [ ] `dns` filter — a query and its response
- [ ] `tcp.flags.syn==1 && tcp.flags.ack==0` — the list of new connections
- [ ] Follow → TCP Stream showing SYN / SYN-ACK / ACK
- [ ] `tls.handshake.type==1` with the **server_name** extension expanded
- [ ] `http` filter — a GET and a 200, a GET and a 404
- [ ] Three retransmitted SYNs to one address (or the paper list §1 lines 22–24 enlarged)
- [ ] The server window after 200 / 404 / 301 / 501 have been caused
- [ ] `curl.exe -I` output showing the `Server:` header
- [ ] Port-map output on a healthy machine, and one with 8000 (python) present
- [ ] **Your router's port-forwarding page, blurred**
- [ ] `Get-Content pfirewall.log -Tail 10` from your real log
- [ ] `Day_06_pfirewall.log` in Notepad with the four findings highlighted
- [ ] Parser v2 output on both files

---
---

# PART 4 — TEAMS AND BREAKOUT ROOMS
Rotate roles from Day 05. Announce at 8:00.

| Activity | Time | Rooms |
|----------|------|-------|
| Activity 1 "Find the Handshake" | 8:40–8:55 | Teams |
| Activity 2 "Make the Status Codes Happen" | 9:15–9:40 | Individually (observed) |
| Activity 3 "Your Port Map" | 10:10–10:25 | Individually, pairs for help |
| Activity 4 "Read the Firewall Log" | 10:45–11:05 | Teams |
| Parser v2 follow-along | 11:05–11:35 | Whole class, everyone running the lines |

---
---

# PART 5 — ACTIVITY 2 OBSERVATION SHEET
### Open at 9:15. One row per trainee.

| Trainee | Server in one window, client in another; 200, 404, 301 and 501 caused on purpose? | Each server line read back — code, meaning, and whose fault (client / server)? | Note |
|---------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------|
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |
| | ☐ | ☐ | |

**Competent** on both. This is knowledge 1.2 applied, and `ICT311203` (computer operations) observed. If a machine has no Python and the trainee is paired, mark the *pair* on box 1 and each trainee individually on box 2.

---
---

# PART 6 — EVIDENCE COLLECTION LOG

| # | Item | Received? |
|---|------|-----------|
| 1 | Annotated capture sheet (5 findings) — or own capture + sheet | ☐ |
| 2 | Port map + lab-subnet diagram (forwards drawn, one flagged) | ☐ |
| 3 | Access-log worksheet (6 lines + own server lines) | ☐ |
| 4 | Firewall-log worksheet (4 findings as sentences) | ☐ |
| 5 | Parser v2 — 2 outputs + the changed line + new output | ☐ |
| 6 | Evidence register + 1 self-check | ☐ |
| 7 | Reflection | ☐ |
| — | **"stopped" in chat** at 11:40 (server closed) | ☐ |

## Still outstanding — keep chasing
| Item | From | Why open |
|------|------|----------|
| **Wazuh SIEM server** | Phase B | Not built yet |
| Lab OSH Checklist, Green Lab Pledge | Day 01 | First on-site day |
| **Lab-subnet Nmap sweep** | Day 06 | Needs the lab and written authorisation — the subnet is on paper until then |

---
---

# PART 7 — TIMING CARD

| Time | Do | Cut first if behind |
|------|-----|--------------------|
| 8:00 | Welcome, recall, **the rule** | — |
| 8:15 | 6.1 + Demo 1 | Skip Follow TCP Stream; paper list for the handshake |
| 8:40 | Activity 1 | Three findings (DNS, SNI, unanswered SYN) |
| 8:55 | **6.2 + Demo 2 (the server)** | **Never cut** |
| 9:15 | **Activity 2 (observed)** | **Never cut** |
| 9:40 | 6.3 + Demo 3 | Skip the router screenshot |
| 10:00 | Break | — |
| 10:10 | Activity 3 | Five rows only |
| 10:25 | **6.4 + Demo 4 (firewall log)** | **Never cut** |
| 10:45 | Activity 4 | Two findings (scan, outbound Tor) |
| 11:05 | 6.5 + Demo 5 | Run only; read-through → PM Task 5 |
| 11:35 | Brief, **stop the server**, close | — |

---
---

# PART 8 — CONTINGENCY

| If this happens | Do this |
|----------------|---------|
| Wireshark/Npcap fails on your machine | Fallback screenshots for Demo 1; the activity is on paper |
| Localhost traffic not visible in the capture | Npcap loopback adapter; or the paper list for packets 13–21 |
| `python` not found on a trainee machine | `py`; if no Python, pair them — one machine, two people |
| Port 8000 in use | 8080; note the forgotten server as a finding |
| `curl.exe` missing | `Invoke-WebRequest -Method DELETE http://localhost:8000/` for the 501 |
| Process column blank in the port map | Needs elevation; record the PID and say so |
| A trainee's port map shows 3389 | A real finding — have them write it as a report line |
| Your real firewall log is empty | Browse for a minute, or skip the ten seconds; the supplied file is the lesson |
| Activity 2 overruns | 200 and 404 observed; 301 and 501 → PM Task 3 |
| Behind at 11:05 | Parser run only; read-through → PM Task 5 |

---
---

# PART 9 — LINKS FOR TRAINEES
- **Wireshark** (optional) — `https://www.wireshark.org/download.html` — reading a saved capture needs no admin; capturing needs Npcap (admin)
- **Python 3** — `https://www.python.org/downloads/windows/` (from Day 04) — or `winget install Python.Python.3.12`
- The four Wireshark filters, the status-code rule, the normal-listeners table, the firewall-log columns — tables in your handout
- The status-code recipes — in your Activity Pack (Activity 2)
- `Day_06_pfirewall.log` and `Day_06_fw_parser.py` — attached to the joining note; keep them in the same folder as Day 04's parser and access log
- **The rule:** capture only your own machine's traffic, on a network you own. **Stop your server** before you leave.
