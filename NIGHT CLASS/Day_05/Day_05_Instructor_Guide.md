# DAY 05 — INSTRUCTOR GUIDE
## Topic: Deeper Into the Machine — Event Viewer and Sysinternals Mastery
### Cyber Threat Monitoring Level I · 30-Day Program · Day 05 of 30 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **The two standing conditions.** (1) **No SIEM server** — everything runs on each trainee's own Windows machine with built-in tools plus the portable Sysinternals Suite. (2) **Total beginners** — assume nothing, every click shown, calm pace. Yesterday (Day 04) they opened Event Viewer and ran `Get-Process` for the first time. Today they learn to make those tools *work for them* instead of overwhelm them.

---

## HOW THIS GUIDE WORKS

The **topic guide** — what Day 05 teaches, why, what you must know, and how it is assessed. Not a script. Keep these open:

| File | For |
|------|-----|
| **`Day_05_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_05_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_05_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_05_Student_Activity_Pack.docx`** | what the trainees do |
| **`Day_05_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_05_Activity_Solutions.docx`** | the four morning activities answered in the trainee's own tables — keep open during the live session (trainer only) |
| **`Day_05_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_05_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_05_Sample_Data.md`** | the channel drill, the custom-view recipe, the filter cookbook, the Autoruns set, the baseline v2 commands |

> **Numbering.** This is **Day 05 of the 30-day program**. Yesterday, Day 04, used the folder `../Day_5/` from the 15-day set — so the trainees' evidence from yesterday sits in `C:\Evidence\Day_05\`. The first thing the class does at 8:00 is rename it to `Day_04`. Say this plainly; it is a two-second `ICT311203` "maintain" task and it avoids a whole day of confusion.

---
---

# PART A — WHAT DAY 05 IS

## The one-sentence topic

> **Yesterday the trainees met the tools. Today they learn to ask the tools a question: which log, which filter, which saved view, which Sysinternals window — and to keep the answer as evidence, hashed and compared against yesterday's.**

## Where Day 05 sits

Day 05 is the second of the three Phase A "underpinning" days that the 15-day plan could not afford. It deepens **required knowledge 1.1** (basic knowledge with Windows, macOS and Linux OS) and delivers the *maintain* side of `ICT311203`, while producing the habits every Phase B day depends on:

| Unit / knowledge | What Day 05 does |
|------------------|------------------|
| **CS-ICT251101 knowledge 1.1** Basic knowledge with Windows, MAC & Linux OS | Topics 5.1–5.4 — the five channels, custom views, `Get-WinEvent`, Sysinternals; the OS-equivalents table (PM Task 5) |
| **CS-ICT251101 knowledge 1.6** Log and detection management *(preview)* | Custom views and the filter cookbook are exactly what Days 08 and 12 will use |
| **`ICT311203` Perform computer operations — LO4 maintain** | Topic 5.5 — baseline v2, hashed, compared to Day 04's |
| **`400311106` Access and maintain information** | Every export is named, hashed and registered; the VirusTotal option stays off (LO4) |
| **`ICT315202` Apply quality standards — LO2** | PM Task 6 — the evidence register row self-checked |

After today the class has five saved custom views, a filter cookbook, and a baseline they can diff. Day 06 does the same for the wire and the web; Day 07 for threat intelligence. Then Phase B begins.

## What "no server" changes

Nothing today needed a server in the original plan either. The one adjustment: **Sysinternals runs portable, without admin**, so Process Explorer shows less detail and Autoruns lists the current user's entries with a warning. Both are still correct and still evidence — the guide says where the warning appears and what to say.

## The five topics of Day 05

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **5.1** | **Five Channels, Not a Wall** — the five logs an analyst actually uses | knowledge 1.1, 1.6 | 15 min + Activity 1 |
| **5.2** | **Custom Views** — the saved question, and its XML | knowledge 1.6 | 20 min + Activity 2 |
| **5.3** | **Ask in PowerShell** — `Get-WinEvent -FilterHashtable`, the same question three ways, export to CSV | knowledge 1.1, 1.3 | 20 min + Activity 3 |
| **5.4** | **Sysinternals** — Process Explorer, Autoruns, TCPView read as evidence | knowledge 1.1 | 30 min + Activity 4 |
| **5.5** | **Baseline v2** — export, hash, compare | `ICT311203` LO4 · `400311106` | 40 min follow-along |

---

## Competency map

### Core unit — `CS-ICT251101`, underpinning knowledge

**Required knowledge today:** 1.1 *Basic knowledge with Windows, MAC & Linux OS* (the whole day, plus the equivalents table), 1.3 *scripting* (PowerShell as the query language), 1.6 *Log and detection management* (introduced through custom views — completed on Day 08).

**Required skills today:** computer operation (every command), interpreting work instructions (the recipe and the cookbook), analytical (Activity 4 — normal, legitimate, suspicious, with a reason).

### Basic and common units delivered

| Code | How it appears |
|------|---------------|
| `ICT311203` Perform computer operations | **LO4 maintain** — baseline v2 exported, hashed, compared; the evidence folder tidied at 8:00 |
| `400311106` Access and maintain information | Files named to the convention, hashed, registered; the VirusTotal upload option explicitly left off |
| `ICT315202` Apply quality standards | LO2 — the register row self-checked (PM Task 6) |

> **Still outstanding — say it:** the **Wazuh SIEM server**, the **Day 01 lab OSH checklist + green pledge**. (The lab-subnet scan joins the list tomorrow.)

---

## The idea that anchors the whole day

> **Know the question before you open the tool.** Which channel would hold the answer? Which IDs? What time window? Then the tool is fast. Open Event Viewer with no question and it is a wall.

Three habits come out of that, and they are the three sentences of the day:
1. **Five channels, and know which one before you open Event Viewer.**
2. **A custom view is a saved question — build it once, export the XML, it is there every morning.**
3. **A baseline is only useful when you compare it — export, hash, diff.**

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. Name the **five channels** and say which one holds a given event.
2. Build a **custom view**, read its **XML**, export and import it.
3. Write a `Get-WinEvent -FilterHashtable` query with the four keys, **export it to CSV**, and treat "no events found" as the answer zero.
4. Read **Process Explorer, Autoruns and TCPView** as evidence — parent, path, publisher, colour — and classify an entry as normal, legitimate or suspicious with a reason.
5. Produce **baseline v2**, hash it, and **diff** it against Day 04's.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 04 · **rename the evidence folder** | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 15 | 3 | **Topic 5.1** + **Demo 1** Five channels, not a wall | Follow-along | 5.1 |
| 8:30 | 10 | 4 | **Activity 1** "Which Channel?" | Gamified, chat | 5.1 |
| 8:40 | 20 | 5–6 | **Topic 5.2** + **Demo 2** Custom views — build, XML, export | Follow-along | 5.2 |
| 9:00 | 20 | 7 | **Activity 2** "Build the View" | Individually, pairs for help | 5.2 |
| 9:20 | 20 | 8–9 | **Topic 5.3** + **Demo 3** Ask in PowerShell — three ways, CSV | Follow-along | 5.3 |
| 9:40 | 20 | 10 | **Activity 3** "The Same Question, Three Ways" | Individually, observed | 5.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 30 | 11–12 | **Topic 5.4** + **Demo 4** Sysinternals — Process Explorer, Autoruns, TCPView | Follow-along | 5.4 |
| 10:40 | 15 | 13 | **Activity 4** "What Starts Without You?" | Breakout teams | 5.4 |
| 10:55 | 40 | 14 | **Topic 5.5** + **Demo 5** Baseline v2 — export, hash, compare (trainees run alongside) | Follow-along | 5.5 |
| 11:35 | 10 | 15 | Afternoon brief · how it is marked · close | Whole class | — |

Morning sums to 225 (8:00 → 11:45). Lecture time is about 75 minutes; the rest is hands-on.

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 35 minutes.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Five saved custom views — built, exported as XML, one purpose line each | 30 | 5 `.xml` files + purpose list |
| 2 | The filter cookbook — all eight queries run; the count recorded; two exported to CSV | 35 | Cookbook sheet + 2 CSVs |
| 3 | Baseline v2 — four exports, the hash file, and the compare against Day 04 with the differences explained | 35 | 4 CSVs + hashes + compare note |
| 4 | Autoruns on your own machine — ten entries classified with reasons | 20 | Autoruns worksheet |
| 5 | The OS-equivalents table — Windows · macOS · Ubuntu, six rows | 15 | Equivalents table |
| 6 | Evidence register — every file today named, hashed, logged; one row self-checked | 10 | Register + self-check |
| 7 | Reflection | 10 | Three answers |

---

## Before the day
### The night before
- [ ] Download the **Sysinternals Suite** zip and unzip it to `C:\Tools\Sysinternals\` (or a USB); run `procexp64.exe`, `autoruns64.exe`, `tcpview64.exe` once each and accept the EULAs — **without admin**, so you see what the trainees will see
- [ ] Run cookbook queries #1–#3 on your machine; note which return "no events found" on your build
- [ ] Build the `CV_Defender` custom view, export it, delete it, import it — so the export/import round-trip holds no surprises
- [ ] Run the whole of Sample Data §6 (baseline v2 + compare) against your own Day 04 CSVs
- [ ] Confirm your `C:\Evidence\Day_05\` from Day 04 exists so the rename in Demo 0 works on screen
- [ ] Take the fallback screenshots in `Day_05_Resources.md`

### On the morning
- [ ] Breakout rooms (Activity 4 only); chat visible (Activity 1)
- [ ] Activity Pack, Handout, Resources sent; the Sysinternals download link pinned in chat
- [ ] Observation sheet (Resources Part 5) open at 9:40
- [ ] Collect outstanding Day 01–04 evidence in the first fifteen minutes

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 5.1 — FIVE CHANNELS, NOT A WALL
### 8:15–8:40 with Demo 1 and Activity 1 · Slides 3–4 · knowledge 1.1, 1.6

### The point
Event Viewer has hundreds of logs. Beginners freeze. Give them the five that matter and the habit of choosing one *before* opening the tool.

### What you must know
The table in Sample Data §1: Security (admin), System, Application, Defender/Operational, PowerShell/Operational. What lands in each, and which need admin. The **Security log usually says "access denied" on a standard account** — that is normal, and every question a beginner needs answered today has a non-admin channel.

### Key messages
- Five channels. Know which before you open the tool.
- Security needs admin. Everything else today does not.
- The Defender log is the one Phase B lives in — you have already seen it once (Day 04's `Get-MpComputerStatus` was the tool's status; this is the tool's diary).

### Mistakes to expect
- Trainees open Windows Logs → Application because it is first, and read from the top. Ask: "What is the question?"
- "Access denied" on Security read as a broken machine. It is a permission, not a fault.

---

## TOPIC 5.2 — CUSTOM VIEWS
### 8:40–9:20 with Demo 2 and Activity 2 · Slides 5–7 · knowledge 1.6

### The point
A custom view is a **saved question**. Beginners build one by clicking, then read the XML that the clicks produced, then export it so it travels.

### What you must know
The recipe in Sample Data §3, and the XML. The XML has four words worth teaching: **Query** (one question), **Path** (which log), **Select** (keep the events where…), **EventID** (…the ID is one of these). Do not teach XPath beyond that. **Export Custom View…** writes the `.xml`; **Import Custom View…** reads it back — which is how the view moves to a rebuilt machine, and why PM Task 1 asks for five exported files rather than five screenshots.

### Key messages
- A custom view is a saved question — build once, use every morning.
- The XML is the same question written down. You can read it; you do not have to write it (but you can).
- Export it. A view that lives only on one machine is lost with that machine.

### Mistakes to expect
- Trainees filter the *current* log and think they have a custom view. A filter is temporary; a custom view is saved. Show the tree.
- The Event IDs box typed with spaces after commas. Event Viewer accepts it, but teach `1116,1117` clean.

---

## TOPIC 5.3 — ASK IN POWERSHELL
### 9:20–10:00 with Demo 3 and Activity 3 · Slides 8–10 · knowledge 1.1, 1.3

### The point
The same question, asked in PowerShell, so it can be **kept** (CSV) and later **compared**. Four hashtable keys cover almost everything an L1 asks.

### What you must know
`Get-WinEvent -FilterHashtable @{ LogName=…; Id=…; StartTime=…; ProviderName=… }` — the cookbook in Sample Data §4. Two additions to any query: `Select-Object TimeCreated, Id, ProviderName, Message` to read, `Export-Csv … -NoTypeInformation -Encoding UTF8` to keep. The red **"No events were found"** is a *result*: the count is zero. `-ErrorAction SilentlyContinue` turns it into a quiet zero.

**Activity 3 is observed.** The trainee runs cookbook #3 (new services, 30 days) three ways — GUI filter, custom view, PowerShell with export — and says whether the three agree.

### Key messages
- Four keys: LogName, Id, StartTime, ProviderName. Learn the four, not the tool.
- "No events found" is the number zero. Write it down.
- The GUI is for looking; the custom view is for every morning; PowerShell is for keeping and comparing.

### Mistakes to expect
- `Id='7045'` with quotes — it still works, but teach numbers unquoted so `Id=1116,1117` reads naturally.
- Trainees read "No events found" as a broken command and re-run it five times. Say the zero out loud.
- Forgetting `-NoTypeInformation`, then a strange first line in the CSV. Harmless; name it.

---

## TOPIC 5.4 — SYSINTERNALS
### 10:10–10:55 with Demo 4 and Activity 4 · Slides 11–13 · knowledge 1.1

### The point
Three portable tools that show, live and in colour, what `Get-Process`, the startup list and `netstat` showed in text on Day 04 — and what to *read* in them: parent, path, publisher, colour.

### What you must know
- **Process Explorer** — the tree (parent → child; `winword.exe` spawning `powershell.exe` is the classic wrong shape), **Options → Verify Image Signatures** and the **Verified Signer** column, the lower pane (Ctrl+L) for what a process has open, **Properties → Image** for the path and command line. Without admin some system processes show "access denied" details — that is expected.
- **Autoruns** — the tabs that matter (Logon, Scheduled Tasks, Services, Drivers), **Options → Hide Microsoft Entries** to shrink the list to what a person or an attacker added, **Scan Options → Verify code signatures** (on) and **Check VirusTotal.com** (**off** — it uploads hashes; Day 03's rule). Colours: **pink** unverified, **yellow** file missing. Without admin: a warning and only the current user's entries — say so, it is still evidence.
- **TCPView** — Day 04's `netstat -ano` with names filled in and new connections flashing green, closed ones red.

**Activity 4:** eight paper entries (Sample Data §5) → normal Windows · legitimate third-party · suspicious, with a reason. The answers turn on **path + publisher + name**: `svhost32.exe` in `C:\Users\Public` (C) and a hidden PowerShell task named after Adobe (D) are the suspicious pair; G is a made-up "Defender helper" in ProgramData — unsigned; H is yellow — a leftover, not a threat, but untidy.

### Key messages
- Read three things on every entry: **path, publisher, name**. Wrong path or no publisher is a finding; a name is only a name.
- Parent → child matters: a document reader should not be starting a shell.
- The VirusTotal box stays off. You do not send a client's file hashes to a third party without permission.

### Mistakes to expect
- Trainees call everything pink "malware". Pink means *unverified* — many legitimate small programs are unsigned. Path and name decide.
- Trainees enable VirusTotal because the tool offers it. Stop them and say why.
- "Access denied" in Process Explorer without admin read as a fault. It is a permission.

---

## TOPIC 5.5 — BASELINE v2
### 10:55–11:35 with Demo 5 · Slide 14 · `ICT311203` LO4 · `400311106`

### The point
Day 04 produced a baseline. Today the class produces version 2 the proper way — with a listening-ports list and Autoruns hashes — **hashes the files**, and **diffs** against yesterday. A baseline nobody compares is a screenshot.

### What you must know
Sample Data §6, in order: rename yesterday's folder (done at 8:00), four exports, `autorunsc64.exe -a * -c -h -s` (or the Day 04 `Get-CimInstance` fallback), `Get-FileHash` on the CSVs, then `Compare-Object` on services (should be near-identical) and on processes (will differ — normal churn). Teach the reading of `=>` (only in today's) and `<=` (only in yesterday's). A new service in the compare is the same fact a 7045 event shows — **two sources, one fact** — which is the Day 12 verification habit, a week early.

Trainees run every line alongside you; this is the follow-along that replaces a fifth activity.

### Key messages
- Export, hash, compare. The compare is the point.
- Processes churn; services and autoruns should not. A new service or autorun that you did not add is a finding.
- Two sources, one fact — the compare and the 7045 event agree, or you have a question.

### Mistakes to expect
- `Compare-Object` with no `-Property` compares whole objects and shows everything as different. Always name the property.
- Trainees panic at a long process diff. Say "churn" and show them the services diff first.
- Autoruns CSV opens with odd characters — it is UTF-16 on some builds; open it in Calc with the encoding prompt, or read the hashes from the `-h` columns in PowerShell.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 05 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 5 exported custom views (`.xml`) with purpose lines | PM Task 1 + Activity 2 | knowledge 1.6 (preview of E1 PC 1.1) |
| Filter cookbook sheet — 8 queries, counts, 2 CSVs | PM Task 2 + Activity 3 | knowledge 1.1, 1.3 |
| Baseline v2 — 4 CSVs + hash file + compare note | PM Task 3 + Demo 5 follow-along | `ICT311203` LO4 |
| Autoruns worksheet — 10 own-machine entries classified | PM Task 4 + Activity 4 | knowledge 1.1 · analytical skill |
| OS-equivalents table | PM Task 5 | knowledge 1.1 (macOS, Linux) |
| Evidence register + 1 self-check | PM Task 6 | `400311106` · `ICT315202` LO2 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

## Observation during the live session

**Activity 3 "The Same Question, Three Ways" is observed.** Observation sheet from `Day_05_Resources.md` open at 9:40. Two things:
1. **Did the trainee write the hashtable with the right keys (LogName, Id, StartTime) and export the result to a named CSV that exists?**
2. **Did the trainee state the count from all three ways — including a zero — and say whether they agree?**

## How the afternoon is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Five views that open and filter what their purpose line says · eight queries run with a count each, zeros included · baseline v2 with hashes and a compare note that separates churn from a real difference · Autoruns entries classified by path + publisher + name, with a reason each · equivalents table with the right tool in each cell |
| **Not yet competent** | Screenshots instead of `.xml` exports · queries copied but not run ("it gave an error") · a baseline with no compare, or a compare with every process listed as "suspicious" · "pink = malware" with no path or publisher read · VirusTotal enabled |

Full keys in `Day_05_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| Sysinternals download blocked | Use the fallback screenshots for Demo 4; Activity 4 is on paper anyway; baseline v2 uses the `Get-CimInstance` fallback for autoruns |
| A machine blocks running unsigned/portable exes (AppLocker) | Same as above — the PowerShell commands cover every export |
| Security log "access denied" | Expected. Nothing today needs it; say so once |
| `Get-WinEvent` returns "No events found" for cookbook #3 | Correct on a quiet machine — count = 0. Use #4 (boots) to show a non-zero result |
| No `C:\Evidence\Day_05\` from Day 04 on a trainee's machine | They re-run the four Day 04 export lines (2 minutes) into `Day_04`, then continue |
| Custom view import fails ("query invalid") | The XML was edited by hand with a typo — re-export from the GUI version |
| Activity 3 overruns | Do the PowerShell way live and observed; GUI and custom view → PM Task 2 |
| Behind at 10:55 | Baseline v2 exports only (skip the compare live); compare → PM Task 3 with the Sample Data lines |

---

## End of day checklist
- [ ] Activity 3 observation notes written up
- [ ] `.xml` exports, cookbook sheets and baseline v2 folders chased
- [ ] Outstanding still listed: Wazuh server, Day 01 lab docs
- [ ] Tomorrow announced: **Day 06 — Network and web evidence in depth** (the wire, the web server from both sides, the firewall log, parser v2). Same hours. Tell them: Python 3 must still work from Day 04, and to bring the `Day_5_log_parser.py` and `Day_5_access_log.txt` files

## What to say at the close
Yesterday the class met the tools; today they learned to ask them questions. They can name the five logs that matter, save a question as a custom view and carry it in an XML file, ask the same question in PowerShell and keep the answer, read Process Explorer and Autoruns for path, publisher and name — and they have a baseline they can actually compare. Tomorrow the same discipline goes onto the wire: a real capture, a web server they run themselves, and the firewall's own log. Say that, and let them go.
