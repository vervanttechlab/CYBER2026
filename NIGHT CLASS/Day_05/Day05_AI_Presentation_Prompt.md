============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (30-Day Program) — Day 05
Deeper Into the Machine — Event Viewer and Sysinternals Mastery
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 15 slides.
5. The words for each slide are in Day_05_Presenter_Script.md, keyed to these same
   15 slide numbers.

WHAT DAY 05 IS:
Day 05 of the 30-day program is the second "underpinning" day. Day 04 introduced
Event Viewer, Get-Process, the wire and a first baseline. Day 05 turns those tools
into instruments: the five log channels an analyst uses, custom views (a saved
question, with its XML), Get-WinEvent -FilterHashtable with export to CSV, the
Sysinternals tools (Process Explorer, Autoruns, TCPView) read as evidence, and a
baseline v2 that is hashed and compared against Day 04's. It delivers required
knowledge 1.1 (Windows / macOS / Linux) and ICT311203 LO4 (maintain).

TWO HARD CONSTRAINTS:
- NO SIEM SERVER. Everything runs on the trainee's OWN Windows machine; Sysinternals
  runs portable, without admin.
- TOTAL BEGINNERS. Define every term. Short sentences, calm tone. English is a
  second language.

THE FIVE TOPICS:
  5.1  Five Channels, Not a Wall
  5.2  Custom Views (a saved question, and its XML)
  5.3  Ask in PowerShell (Get-WinEvent -FilterHashtable; three ways; export)
  5.4  Sysinternals (Process Explorer, Autoruns, TCPView — path, publisher, name)
  5.5  Baseline v2 (export, hash, compare)

DAY 05 IS A BLENDED DAY:
- Slides 1-14 — morning, 8:00 to 11:45 AM, ONLINE SYNCHRONOUS and DEMONSTRATION-LED
- Slide 15 — the afternoon, 1:00 to 4:00 PM, FULLY ASYNCHRONOUS
- Mark slide 15 as the transition.

FOUR ACTIVITIES: 1 Which Channel? (chat drill, ten events); 2 Build the View (own
machine); 3 The Same Question, Three Ways (own machine, observed); 4 What Starts
Without You? (teams, eight Autoruns entries on paper). Plus a 40-minute
follow-along for baseline v2.

COLOR SCHEME (course standard): navy #1B3A5C, accent blue #2E75B6, teal #009688,
warning red #C0392B (sparingly), light background #D6E4F0, white, sans-serif.

============================================================
PROMPT (15 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 15 slides. Navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Clean sans-serif fonts. Every slide has a visual element — icons, simple infographics, or diagrams. No stock photos of hackers, hoodies, padlocks, or binary code. 16:9 widescreen. Tables as real tables, commands and XML in monospace. No agenda, thank-you, or Q&A slide.

Day 05 is a blended day. Slides 1-14 are the live, demonstration-led morning (8:00-11:45). Slide 15 is the self-study afternoon (1:00-4:00). Mark slide 15 as the transition.

WRITE IN SIMPLE ENGLISH. Adult vocational trainees in the Philippines, English is a second language, complete beginners. Short sentences, common words, calm tone. Define every term the first time (channel, custom view, XML, hashtable, publisher, signature, baseline, hash).

The one idea of the day, repeated plainly: KNOW THE QUESTION BEFORE YOU OPEN THE TOOL. Three rules carried from earlier days: location is evidence (Day 04); hash it, name it, lock it, log it (Day 03); would you paste this? (Day 03 — so the VirusTotal option stays OFF).

SLIDE 1 — TITLE
Title: "Deeper Into the Machine"
Subtitle: "Cyber Threat Monitoring Level I, Day 05 of 30 — Event Viewer and Sysinternals mastery"
Kicker: "Live demo 8:00-11:45  |  Self-study 1:00-4:00  |  Your own machine, no admin needed"
Small note box: "8:00 housekeeping — rename C:\Evidence\Day_05 to Day_04 (yesterday's folder used the 15-day name)."
Visual: a calm navy title slide. A wall of tiny grey lines on the left turning into five clean labelled drawers on the right.

SLIDE 2 — TODAY'S FIVE TOPICS
Title: "Five Topics: Ask the Tools a Question"
Table (Topic / What you will be able to do):
5.1 Five Channels, Not a Wall | Name the five logs that matter and pick the right one before opening Event Viewer
5.2 Custom Views | Save a question as a view, read its XML, export it
5.3 Ask in PowerShell | Write a Get-WinEvent query with four keys and keep the answer as a CSV
5.4 Sysinternals | Read Process Explorer, Autoruns and TCPView as evidence — path, publisher, name
5.5 Baseline v2 | Export, hash and compare a baseline against yesterday's
Add the line: "Yesterday you met the tools. Today you learn to ask them a question."
Visual: five numbered topic cards.

SLIDE 3 — FIVE CHANNELS, NOT A WALL (Topic 5.1)
Title: "Hundreds of Logs. You Use Five."
Table (# / Channel / What lands here / Admin?):
1 | Security | Logons 4624 / 4625, account changes | Usually yes — "access denied" is normal
2 | System | Services installed 7045, boots and shutdowns 6005 / 6006 / 1074 | No
3 | Application | Crashes 1000, installers | No
4 | Windows Defender / Operational | Detections 1116, actions 1117, failures 1118, protection off 5001 | No
5 | PowerShell / Operational | Script blocks 4104 | No
Big line: "Know which channel BEFORE you open Event Viewer. That habit is the whole difference."
Visual: five drawers in a cabinet, each labelled; the Security drawer has a small lock icon.

SLIDE 4 — ACTIVITY 1: WHICH CHANNEL?
Title: "Activity 1 — Ten Events, Answer in Chat"
Instructions as steps:
- The trainer reads an event. You type the channel number (1-5) in chat.
- First correct answer wins the point.
- Two of the ten are in a log you may not be able to open. Name it anyway.
Big line: "The question comes first. The tool comes second."
Visual: a chat window with numbers popping in.

SLIDE 5 — CUSTOM VIEWS (Topic 5.2, part 1)
Title: "A Custom View Is a Saved Question"
Left — the recipe as five steps: Create Custom View → Logged: last 7 days → By log: Windows Defender / Operational → Event IDs 1116,1117,1118,1119,5001 → Name it → Export Custom View as .xml
Right — contrast box: "Filter Current Log = temporary. Custom view = saved, there every morning."
Big line: "Build it once. Export it. It travels with you."
Visual: a question mark being placed into a folder icon.

SLIDE 6 — THE XML YOUR CLICKS WROTE (Topic 5.2, part 2)
Title: "You Can Read It"
Show in monospace:
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Windows Defender/Operational">
    <Select Path="Microsoft-Windows-Windows Defender/Operational">
      *[System[(EventID=1116 or EventID=1117 or EventID=5001)]]
    </Select>
  </Query>
</QueryList>
Four callouts: Query = one question · Path = which log · Select = keep the events where… · EventID = the ID is one of these.
Big line: "Four words. That is all a custom view is."
Visual: the XML block with four coloured callout arrows.

SLIDE 7 — ACTIVITY 2: BUILD THE VIEW
Title: "Activity 2 — Your Own Defender View"
Instructions as steps:
- Build the Defender view exactly as shown — five IDs, seven days. Name it.
- Export it to C:\Evidence\Day_05\CV_Defender.xml.
- Open its XML tab. Find the five IDs in the text.
- Finished early? Build CV_NewServices: System log, ID 7045.
Big line: "An exported .xml is evidence. A screenshot of a view is not."
Visual: Event Viewer tree with a new custom view highlighted and a small .xml file beside it.

SLIDE 8 — ASK IN POWERSHELL (Topic 5.3, part 1)
Title: "Four Keys Cover Almost Everything"
Show in monospace:
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-30) }
Table (Key / Means / Example):
LogName | which channel | 'System', 'Microsoft-Windows-Windows Defender/Operational'
Id | which events | 7045  or  1116,1117
StartTime / EndTime | how far back | (Get-Date).AddDays(-30)
ProviderName | who wrote it | 'Service Control Manager'
Warning box (amber): "Red text 'No events were found' is NOT an error. It is the number zero. Write zero."
Visual: a key ring with four labelled keys.

SLIDE 9 — THE SAME QUESTION, THREE WAYS — THEN KEEP IT (Topic 5.3, part 2)
Title: "GUI to Look. Custom View Every Morning. PowerShell to Keep."
Three columns: GUI — Filter Current Log, ID 7045, last 30 days · Custom view — CV_NewServices · PowerShell — the query, piped to Export-Csv
Show in monospace: ... | Select-Object TimeCreated, Id, ProviderName, Message | Export-Csv "C:\Evidence\Day_05\q3_new_services.csv" -NoTypeInformation -Encoding UTF8
Big line: "Same rows, three tools. Only the CSV can be hashed, searched and compared."
Visual: three paths converging on one CSV file icon.

SLIDE 10 — ACTIVITY 3: THE SAME QUESTION, THREE WAYS
Title: "Activity 3 — New Services, Last 30 Days"
Instructions as steps:
- Way 1: Filter Current Log on System, ID 7045, last 30 days. Count the rows.
- Way 2: your CV_NewServices custom view. Count.
- Way 3: the PowerShell line, exported to q3_new_services.csv. Count.
- Write all three counts — zero is a count — and say whether they agree.
Big line: "This one is watched: the right keys, a CSV that exists, and three counts stated."
Visual: three tally boxes and an equals sign.

SLIDE 11 — SYSINTERNALS (Topic 5.4, part 1)
Title: "Three Portable Tools, No Install, No Admin"
Three cards:
PROCESS EXPLORER — Get-Process as a tree. Parent → child. Options → Verify Image Signatures; add the Verified Signer column. Properties → Image = path and command line.
AUTORUNS — what starts without you. Options → Hide Microsoft Entries. Verify code signatures ON. Check VirusTotal.com OFF.
TCPVIEW — yesterday's netstat -ano with names filled in; new connections flash green.
Big line: "On every entry read three things: PATH, PUBLISHER, NAME."
Visual: three tool icons in a row with the three words beneath.

SLIDE 12 — READING THE COLOURS (Topic 5.4, part 2)
Title: "Pink Is Not Malware. Path and Name Decide."
Table (Colour / Means / What you do):
Pink | Publisher could not be verified (unsigned) | Read the path and the name before judging
Yellow | The file the entry points to is missing | Untidy leftover — note it, low priority
White | Verified publisher | Still read the path — a real name in a wrong place is a finding
Two contrast examples: "svhost32.exe in C:\Users\Public, unsigned = FINDING" vs "OneDrive.exe in AppData\Local\Microsoft, verified Microsoft = normal".
Red note (sparing): "The VirusTotal box stays OFF. It uploads file hashes to a third party. Day 03's rule."
Visual: three colour swatches with a magnifying glass over the path.

SLIDE 13 — ACTIVITY 4: WHAT STARTS WITHOUT YOU?
Title: "Activity 4 — Eight Entries, Three Verdicts"
Instructions as steps:
- In your team, read the eight Autoruns entries on paper.
- For each: normal Windows, legitimate third-party, or suspicious — and the reason (path, publisher, name).
- Two should worry you. One is just untidy.
Big line: "The reason is what is marked."
Visual: eight entry cards sorting into three trays.

SLIDE 14 — BASELINE v2 (Topic 5.5)
Title: "Export. Hash. Compare."
Three steps with one monospace line each:
1 EXPORT — Get-Process / Get-Service / Get-NetTCPConnection -State Listen / autorunsc64 -a * -c -h -s  → four CSVs
2 HASH — Get-ChildItem baseline_v2_*.csv | Get-FileHash -Algorithm SHA256  → baseline_v2_hashes.csv
3 COMPARE — Compare-Object $old $new -Property Name, StartType   ( => only in today's · <= only in yesterday's )
Add: "Services and autoruns should NOT change overnight. Processes churn — that is normal."
Big line: "A baseline is only useful when you compare it. A new service in the compare is the same fact as a 7045 in the log — two sources, one fact."
Visual: two stacked lists with a diff arrow between them and a padlock-with-hash icon.

SLIDE 15 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 4:00"
Mark as the start of self-study. Keep the table.
Table (Task / Time / Hand in):
1 | Five custom views built and exported as .xml, one purpose line each | 30 min | 5 .xml + purpose list
2 | The filter cookbook — all eight queries run, count recorded, two exported | 35 min | Cookbook sheet + 2 CSVs
3 | Baseline v2 — four exports, hash file, compare note against Day 04 | 35 min | 4 CSVs + hashes + note
4 | Autoruns on your own machine — ten entries classified | 20 min | Autoruns worksheet
5 | OS-equivalents table — Windows · macOS · Ubuntu | 15 min | Table
6 | Evidence register — every file named, hashed, logged; one row self-checked | 10 min | Register + self-check
7 | Reflection | 10 min | Three answers
Closing line: "Today you learned to ask the tools a question. Next, Day 06: the same discipline on the wire — a real capture, your own web server, the firewall's log."
Visual: a teal section band, the table, and a small "Day 5 of 30" progress bar.

============================================================
END OF PROMPT
============================================================
