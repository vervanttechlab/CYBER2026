# DAY 05 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 05 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
Grey quote blocks are the words. *(Italics are notes — never read them.)* Times match the Instructor Guide. Demo steps are in `Day_05_Demonstration_Guide.md`; this script cues the switch. Cut order at the end.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 04, rename the folder |
| 2 | 8:10 | Five topics |
| 3 | 8:15 | Topic 5.1 → Demo 1 five channels |
| 4 | 8:30 | Activity 1 Which Channel? |
| 5–6 | 8:40 | Topic 5.2 → Demo 2 custom views |
| 7 | 9:00 | Activity 2 Build the View |
| 8–9 | 9:20 | Topic 5.3 → Demo 3 ask in PowerShell |
| 10 | 9:40 | Activity 3 The Same Question, Three Ways (observed) |
| — | 10:00 | Break |
| 11–12 | 10:10 | Topic 5.4 → Demo 4 Sysinternals |
| 13 | 10:40 | Activity 4 What Starts Without You? |
| 14 | 10:55 | Topic 5.5 → Demo 5 baseline v2 (follow-along) |
| 15 | 11:35 | Afternoon brief & close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 5. Yesterday you went underneath the machine for the first time — processes, services, the wire, a web request, a script. You opened Event Viewer and it was a wall of thousands of lines. Today we turn that wall into a tool. Five logs that matter. A saved question you can carry in a file. The same question asked in PowerShell so you can keep the answer. Three portable tools that show it all in colour. And a baseline you can actually compare."

> "Quick recall — yesterday, where does the real svchost live?" *(System32 — location is evidence.)* "Good. Today you learn to read location, publisher and name on everything."

> "First, two seconds of housekeeping. Yesterday's evidence folder is called Day_05, because that material was written for the 15-day course. We are on Day 5 of the 30-day course. Rename it with me."

*(Run **Demonstration 0** — rename to `Day_04`, create `Day_05`. Collect outstanding evidence. Announce role rotation.)*

# SLIDE 2 — FIVE TOPICS
### 8:10 – 8:15 · 5 minutes
> "Five topics. 5.1, five channels, not a wall. 5.2, custom views — a saved question. 5.3, ask in PowerShell — the same question three ways, and keep it. 5.4, Sysinternals — Process Explorer, Autoruns, TCPView, read as evidence. And 5.5, baseline version 2 — export, hash, compare. One idea runs all five: know the question before you open the tool."

# SLIDE 3 — TOPIC 5.1: FIVE CHANNELS, NOT A WALL → DEMO 1
### 8:15 – 8:30 · 15 minutes
> "Event Viewer has hundreds of logs. You will use five. Security — logons; it usually needs admin, and that's fine. System — services, boots, shutdowns. Application — crashes and installers. Windows Defender Operational — the antivirus's diary. PowerShell Operational — the scripts that ran. Follow along; we visit each one."

*(Run **Demonstration 1** — the tour of the five, ending on the rule.)*

> "Before you open Event Viewer, decide which of the five holds the answer. That one habit is the whole difference."

# SLIDE 4 — ACTIVITY 1: WHICH CHANNEL?
### 8:30 – 8:40 · 10 minutes
> "Ten events, I read them one at a time, you answer in chat with the channel number — one to five. First correct answer wins the point. Go."

*(Ten events in `Day_05_Sample_Data.md` §2. Answers in Solutions. Bring out #5 — PowerShell — and #8 — Security, which they cannot open, and that is fine.)*

# SLIDES 5–6 — TOPIC 5.2: CUSTOM VIEWS → DEMO 2
### 8:40 – 9:00 · 20 minutes
> "A custom view is a saved question. You build it once by clicking, and it's there every morning. And here's the part nobody shows beginners — your clicks write a little piece of XML, and you can read it. Four words: Query, Path, Select, EventID. Follow along."

*(Run **Demonstration 2** — build `CV_Defender`, read the XML, export it, optionally delete and re-import.)*

> "Export it. A view that lives only in one Event Viewer is lost with that machine. The XML file is the question, written down — it travels."

# SLIDE 7 — ACTIVITY 2: BUILD THE VIEW
### 9:00 – 9:20 · 20 minutes
> "Your turn, on your own machine. Build the Defender view exactly as I did — five event IDs, seven days — name it, and export it to your Day_05 folder as CV_Defender.xml. Then open its XML tab and find the five IDs in the text. Pairs for help; ask the person next to you before you ask me."

*(Circulate. Anyone finished early builds `CV_NewServices` — System, 7045 — which Activity 3 needs.)*

# SLIDES 8–9 — TOPIC 5.3: ASK IN POWERSHELL → DEMO 3
### 9:20 – 9:40 · 20 minutes
> "Now the same question in PowerShell — because a PowerShell answer can be saved as a file, and a file can be compared. Four keys cover almost everything: LogName, Id, StartTime, ProviderName. And one rule: red text saying 'no events were found' is not an error. It is the number zero. Follow along."

*(Run **Demonstration 3** — the first query, the zero, new services three ways, `Export-Csv`, the fourth key.)*

> "The GUI is for looking. The custom view is for every morning. PowerShell is for keeping and comparing. Same rows, three tools."

# SLIDE 10 — ACTIVITY 3: THE SAME QUESTION, THREE WAYS
### 9:40 – 10:00 · 20 minutes · OBSERVED
> "On your own machine: new services in the last 30 days, three ways. One — Filter Current Log on System, ID 7045. Two — your CV_NewServices custom view. Three — the PowerShell line, exported to q3_new_services.csv. Write the count from each way — zero is a count — and say whether they agree. I'm watching for two things: the right keys in the hashtable with a CSV that exists, and the three counts stated."

*(Observation sheet open. Bring them back at 10:00.)*

# BREAK
### 10:00 – 10:10

# SLIDES 11–12 — TOPIC 5.4: SYSINTERNALS → DEMO 4
### 10:10 – 10:40 · 30 minutes
> "Three portable tools from Microsoft, no install, no admin. Process Explorer — Get-Process as a tree, with who signed each program. Autoruns — what starts without you. TCPView — yesterday's netstat with the names filled in. On every entry you read three things: path, publisher, name. Follow along."

*(Run **Demonstration 4** — Process Explorer with Verified Signer, Autoruns with Hide Microsoft, the colours, VirusTotal OFF, TCPView for thirty seconds.)*

> "Pink means unverified — not malware. Yellow means the file is missing. Path and name decide. And the VirusTotal box stays off — it uploads hashes to a third party, and you do not send a client's data anywhere without permission."

# SLIDE 13 — ACTIVITY 4: WHAT STARTS WITHOUT YOU?
### 10:40 – 10:55 · 15 minutes
> "Teams. Eight Autoruns entries on paper. For each: normal Windows, legitimate third-party, or suspicious — and the reason, using path, publisher, name. Two of the eight should worry you. One is just untidy. Find them."

*(Eight entries in `Day_05_Sample_Data.md` §5. Answers in Solutions. Bring out C — svhost32 in Users\Public — and D — a hidden PowerShell task called Adobe.)*

# SLIDE 14 — TOPIC 5.5: BASELINE v2 → DEMO 5
### 10:55 – 11:35 · 40 minutes · everyone runs every line
> "Yesterday you made a baseline. Today, version 2 — the same lists plus listening ports and Autoruns with hashes. Then we hash the files themselves. Then the part that makes a baseline worth having: we compare it to yesterday's. Run every line with me; I'll wait at each one."

*(Run **Demonstration 5** — four exports, `autorunsc`, hashes, compare services, compare processes, register.)*

> "Services and autoruns should not change overnight. Processes churn. A new service in the compare is the same fact as a 7045 in the log — two sources, one fact. Next week that becomes verification."

# SLIDE 15 — AFTERNOON BRIEF & CLOSE
### 11:35 – 11:45 · 10 minutes
> "This afternoon: five custom views built and exported as XML with one purpose line each; the filter cookbook — all eight queries run, the count written down, two exported; baseline v2 complete with the hash file and a compare note that says what changed and whether it's churn; Autoruns on your own machine — ten entries classified; the OS-equivalents table for macOS and Ubuntu; the evidence register with one row self-checked; and the reflection. Marked as always — the reason matters more than the answer."

> "Yesterday you met the tools. Today you learned to ask them a question — which log, which filter, which saved view — and to keep the answer as evidence you can compare. Tomorrow, Day 6: the same discipline on the wire. A real packet capture, a web server you run yourself, the firewall's own log, and your parser grows up. Bring Python and yesterday's parser. Same hours. See you at eight."

---
---

# IF YOU ARE RUNNING LATE
1. Activity 1 to six events
2. Demo 3 — skip the fourth key (ProviderName); it is in the cookbook
3. Demo 4 — TCPView cut entirely; Activity 4 to four entries (A, C, D, H)
4. Demo 5 — exports and hashes live; the compare → PM Task 3 with the Sample Data lines
**Never cut** Demo 2 (the custom view) or Activity 3 (observed).

# THE THREE SENTENCES OF THE DAY
1. **Five channels — and know which one before you open Event Viewer.**
2. **A custom view is a saved question — build it once, export the XML, it is there every morning.**
3. **A baseline is only useful when you compare it — export, hash, diff.**
