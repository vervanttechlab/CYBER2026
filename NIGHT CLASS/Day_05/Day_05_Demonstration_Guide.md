# DAY 05 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 05 for the first time, to complete beginners

---

## READ THIS FIRST

Assumes nothing. **No server** — every tool runs on your own Windows machine; Sysinternals runs portable from a folder, no install, no admin. **Total beginners** — every click shown, calm pace.

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic)* | A note for you — never read aloud |
| **What you will see** | What should appear |

**One housekeeping step and five demonstrations:**

| # | Demonstration | When | Topic |
|---|--------------|------|-------|
| **0** | Rename yesterday's evidence folder | 8:00 | — |
| **1** | Five channels, not a wall — the tour | 8:15 | 5.1 |
| **2** | Custom views — build it, read the XML, export it | 8:40 | 5.2 |
| **3** | Ask in PowerShell — the same question three ways, then keep it | 9:20 | 5.3 |
| **4** | Sysinternals — Process Explorer, Autoruns, TCPView | 10:10 | 5.4 |
| **5** | Baseline v2 — export, hash, compare | 10:55 | 5.5 |

Screen setup as Day 04: clean desktop, large text, notifications off, narrate, slow down. **Have Event Viewer, a normal (non-admin) PowerShell window, and the Sysinternals folder open before 8:00.**

> **The one thing you must NOT do today:** tick **Check VirusTotal.com** in Autoruns or Process Explorer. It uploads file hashes to a third party. If a trainee's tool already has it on, show them where to turn it off.

---
---

# DEMONSTRATION 0 — RENAME YESTERDAY'S FOLDER
### 8:00 AM · Slide 1 · two minutes · everyone does it with you

**1. In PowerShell:**
```powershell
Rename-Item "C:\Evidence\Day_05" "C:\Evidence\Day_04"
New-Item -ItemType Directory "C:\Evidence\Day_05" | Out-Null
Get-ChildItem C:\Evidence
```
**What you will see:** two folders — `Day_04` (with yesterday's four `baseline_*.csv`) and an empty `Day_05`.

> "Yesterday's folder was named Day_05 because that material was written for the 15-day course. We are on Day 05 of the 30-day course today, so yesterday becomes Day_04. Two seconds — and it is the first thing 'maintain' means in the computer-operations unit: keep the evidence folder honest."

*(If a trainee has no `Day_05` folder from yesterday: they create `Day_04` and re-run yesterday's four export lines — Sample Data §6 step 1, with `baseline_` instead of `baseline_v2_` — two minutes.)*

---
---

# DEMONSTRATION 1 — FIVE CHANNELS, NOT A WALL
### 8:15 AM · Slide 3 · Topic 5.1 · knowledge 1.1, 1.6

## Why this exists
Yesterday they opened Event Viewer and saw thousands of lines. Today they see that only five logs matter, and where each one is.

## The steps
**1. Open Event Viewer and collapse everything.**
> "Windows key, type Event Viewer, open it. Left side: a tree. Hundreds of logs in here. You will use five. Let me show you exactly five."

**2. Channel 1 — Security.** Expand **Windows Logs**, click **Security**.
**What you will see:** either a list of logons, or a red **"access denied"** bar.
> "Security. Logons, failed logons, account changes. On a normal account this often says access denied — that is a permission, not a fault. Nothing we do today needs it. Move on."

**3. Channel 2 — System.** Click **System**.
> "System. Services installed, started, stopped. Boots and shutdowns. This is where a new service — a favourite hiding place — writes event 7045."

**4. Channel 3 — Application.** Click **Application**.
> "Application. Programs crashing, installers running. Event 1000 is a crash."

**5. Channel 4 — Defender.** Expand **Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational**.
> "Windows Defender, Operational. The antivirus's diary. Detections are 1116, actions 1117, failures 1118. You saw this log yesterday for a moment; from next week you will live in it."

**6. Channel 5 — PowerShell.** Same tree → **PowerShell → Operational**.
> "PowerShell, Operational. If script logging is on, event 4104 holds the text of every script that ran. Attackers use PowerShell; this log is where they leave fingerprints."

**7. Land the rule.**
> "Five channels. Before you open Event Viewer, decide which one holds the answer. That single habit is the difference between a wall and a tool."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "A new service was installed. Which channel?" | System (7045) |
| "The antivirus found something. Which channel?" | Windows Defender / Operational (1116) |
| "Security says access denied. Broken?" | No — a permission; nothing today needs it |

## Common problems
| Problem | Fix |
|---------|-----|
| Cannot find the Defender log in the tree | Applications and Services Logs → Microsoft → Windows → **Windows Defender** → Operational (alphabetical under Windows; scroll) |
| Third-party AV, no Defender log entries | The log still exists; it will be quiet. The channel is still the answer |

---
---

# DEMONSTRATION 2 — CUSTOM VIEWS
### 8:40 AM · Slides 5–6 · Topic 5.2 · knowledge 1.6

## Why this exists
A saved question. Beginners build one by clicking, then see the XML the clicks produced, then export it.

## The steps
**1. Create the view.** Right-click **Custom Views** → **Create Custom View…**
> "A custom view is a saved question. We are going to ask: show me every Defender detection, action, failure, and every time real-time protection was switched off."

**2. Fill the form.** Logged: **Last 7 days** · tick all levels · **By log** → expand to *Windows Defender* → tick **Operational** · in the Event IDs box type `1116,1117,1118,1119,5001` → **OK**.

**3. Name it.** `Defender — detections and failures` · description: *Detections, actions, failures, protection off* → **OK**.

**What you will see:** the view appears under Custom Views and opens — with your Day 04 EICAR events in it if they are within seven days.

**4. Now read the XML.** Right-click the new view → **Properties** → **Edit Filter…** → **XML** tab.
**What you will see:** the `<QueryList>` block from Sample Data §3.
> "This is what your clicks wrote. Four words. Query — one question. Path — which log. Select — keep the events where… EventID — the ID is one of these. You can read it. Later you could write it. That is all a custom view is."

*(Cancel out — change nothing.)*

**5. Export it.** Right-click the view → **Export Custom View…** → save as `C:\Evidence\Day_05\CV_Defender.xml`.
> "Exported. That file is the question, written down. If this machine were rebuilt tomorrow, Action → Import Custom View brings it straight back. A view that lives only in one Event Viewer is lost with that machine."

**6. Prove the round-trip** *(optional, 30 seconds)*: right-click the view → Delete → **Action → Import Custom View…** → pick the `.xml`. It returns.

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "Filter Current Log vs a custom view — difference?" | A filter is temporary; a custom view is saved |
| "What does `<Select Path=…>` mean?" | Keep the events from that log where the condition is true |
| "Why export it?" | So it survives a rebuild and travels to other machines |

## Common problems
| Problem | Fix |
|---------|-----|
| The view is empty | Correct if no Defender events in 7 days; widen "Logged" to 30 days or recreate the EICAR (Day 04) |
| "Query is invalid" on import | The XML was hand-edited with a typo; re-export the GUI-built one |

---
---

# DEMONSTRATION 3 — ASK IN POWERSHELL
### 9:20 AM · Slides 8–9 · Topic 5.3 · knowledge 1.1, 1.3

## Why this exists
The same question, asked in PowerShell so it can be kept as a file and later compared. Four keys, one export.

## The steps
**1. The four keys, on the slide, then the first query.**
```powershell
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1116,1117; StartTime=(Get-Date).AddDays(-30) }
```
**What you will see:** your Day 04 EICAR events, or a red "No events were found" line.
> "Four keys. LogName — which channel. Id — which events. StartTime — how far back. And a fourth we will use in a moment, ProviderName. Everything I ask a log today is those four keys."

**2. The red line is a number.** *(If you have events, run cookbook #7 — signature update failures — which is probably empty.)*
```powershell
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=2001 }
```
> "Red text: 'No events were found'. That is not an error. It is the answer zero — this machine has never had a signature update fail. Write zero. If red text bothers you, add `-ErrorAction SilentlyContinue` and it goes quiet."

**3. The question of the day — new services, three ways.**
*Way one — GUI:* Event Viewer → System → **Filter Current Log…** → Event IDs `7045` → Logged: Last 30 days. Count the rows.
*Way two — custom view:* create `CV_NewServices` (System, 7045) exactly as in Demo 2. Same rows.
*Way three — PowerShell:*
```powershell
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-30) } |
  Select-Object TimeCreated, Id, ProviderName, Message
```
> "Same rows, three tools. The GUI is for looking. The custom view is for every morning. PowerShell is for keeping — watch."

**4. Keep it.**
```powershell
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-30) } |
  Select-Object TimeCreated, Id, ProviderName, Message |
  Export-Csv "C:\Evidence\Day_05\q3_new_services.csv" -NoTypeInformation -Encoding UTF8
Get-ChildItem C:\Evidence\Day_05
```
**What you will see:** `q3_new_services.csv` in the folder. Open it in Calc/Excel briefly.
> "A file. Named, dated, in the evidence folder. Next week you will compare files like this against each other. A screenshot cannot be compared. A CSV can."

**5. The fourth key, once.**
```powershell
Get-WinEvent -FilterHashtable @{ LogName='System'; ProviderName='Service Control Manager'; StartTime=(Get-Date).Date } | Select-Object -First 5 TimeCreated, Id, Message
```
> "ProviderName — who wrote the event. Everything the Service Control Manager said since midnight. That is the fourth key; you now have all four."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "The four keys?" | LogName, Id, StartTime (EndTime), ProviderName |
| "Red 'No events were found' — what do you write?" | Zero |
| "Why export to CSV instead of a screenshot?" | It can be compared, searched and hashed |

## Common problems
| Problem | Fix |
|---------|-----|
| `Id='7045'` in quotes | Works; teach unquoted numbers so `1116,1117` reads naturally |
| Message column truncated in the console | Fine — it is complete in the CSV; or add `| Format-List` |
| `Export-Csv` path error | The `Day_05` folder must exist — Demo 0 made it |

---
---

# DEMONSTRATION 4 — SYSINTERNALS
### 10:10 AM · Slides 11–12 · Topic 5.4 · knowledge 1.1

## Why this exists
Day 04's text lists, shown live and in colour — and the three things to read on every entry: path, publisher, name.

## What you need
- The Sysinternals Suite unzipped to `C:\Tools\Sysinternals\` (or a USB). EULAs already accepted the night before. Run **without admin**.

## The steps
**1. Process Explorer.** Double-click `procexp64.exe`.
**What you will see:** a tree of processes, coloured; some rows say "access denied" in the details without admin — *say that this is expected.*
> "Process Explorer is Get-Process as a tree. Every process has a parent — the thing that started it. Look for wrong shapes: a Word document starting PowerShell is a wrong shape."

**2. Turn on signature checking.** **Options → Verify Image Signatures**. Then **View → Select Columns → Verified Signer** (tick) → OK.
> "Now every row says who signed it. 'Microsoft Windows' verified — fine. '(No signature was present)' — read the path before you decide anything."

**3. Read one process three ways.** Find `explorer.exe` → right-click → **Properties → Image** tab.
> "Path — where it really lives, System32 or Windows. Command line — how it was started. Parent — who started it. Path, publisher, name. Those three, on every entry, all day."

**4. The lower pane, once.** Select a browser process → **Ctrl+L**.
> "What the process has open — files, network handles. We will not go deeper today; know it is here."

**5. Autoruns.** Close Process Explorer; double-click `autoruns64.exe`.
**What you will see:** a long list across tabs; without admin, a yellow warning bar that some entries need elevation.
> "Autoruns answers: what starts without you? Every tab is a way to start at boot or logon. Without admin it shows this user's entries and warns — that is fine and still evidence."

**6. Shrink it.** **Options → Hide Microsoft Entries** (tick). Then **Options → Scan Options…** → tick **Verify code signatures**; **leave Check VirusTotal.com unticked** → **Rescan**.
> "Hide Microsoft, and the list becomes what a person — or an attacker — added. Verify signatures on. VirusTotal OFF — that box uploads file hashes to a third party. Day 03's rule: you do not paste client data anywhere without permission. Same here."

**7. Read the colours.** Click the **Logon** tab, then **Scheduled Tasks**, then **Services**.
> "Pink — the publisher could not be verified. Yellow — the file it points to is missing. Neither is proof of anything on its own. Pink plus a path in Users\Public plus a name that imitates Windows — that is a finding."

**8. TCPView, thirty seconds.** Double-click `tcpview64.exe`.
> "Yesterday's netstat -ano with the names filled in. New connections flash green, closed ones red. Same evidence, easier to watch. Close it."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Three things to read on every entry?" | Path, publisher, name |
| "Pink in Autoruns means?" | Publisher not verified — read the path before judging |
| "Which box stays off, and why?" | Check VirusTotal.com — it uploads hashes to a third party |

## Common problems
| Problem | Fix |
|---------|-----|
| Portable exe blocked by policy | Fallback screenshots (Resources Part 3); Activity 4 is on paper; baseline uses the `Get-CimInstance` fallback |
| SmartScreen "unrecognised app" | More info → Run anyway (Sysinternals is Microsoft-signed; this is the zip's mark-of-the-web) |
| "Access denied" rows in Process Explorer | Expected without admin — say so once |

---
---

# DEMONSTRATION 5 — BASELINE v2: EXPORT, HASH, COMPARE
### 10:55 AM · Slide 14 · Topic 5.5 · `ICT311203` LO4 · trainees run every line with you

## Why this exists
A baseline is only useful when you compare it. Version 2 adds listening ports and Autoruns hashes, hashes the evidence, and diffs against Day 04.

## The steps
**1. The four exports** *(Sample Data §6 step 1 — read each line before you run it):*
```powershell
$E = "C:\Evidence\Day_05"
Get-Process | Select-Object Name, Id, Path, Company | Sort-Object Name | Export-Csv "$E\baseline_v2_processes.csv" -NoTypeInformation
Get-Service | Select-Object Name, Status, StartType | Export-Csv "$E\baseline_v2_services.csv" -NoTypeInformation
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort | Export-Csv "$E\baseline_v2_ports.csv" -NoTypeInformation
```
> "Processes, services — as yesterday — and new today: listening ports. What is waiting for a connection on this machine. Tomorrow we read this list against the wire."

**2. Autoruns to CSV, with hashes.** In the Sysinternals folder:
```powershell
cd C:\Tools\Sysinternals
.\autorunsc64.exe -accepteula -nobanner -a * -c -h -s > "$E\baseline_v2_autoruns.csv"
```
**What you will see:** a pause, then a CSV in the folder (a warning line about elevation is normal).
> "The command-line Autoruns. Every category, CSV, with hashes and signature checks. Every entry now has a fingerprint."
*(Blocked? `Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location | Export-Csv "$E\baseline_v2_autoruns.csv" -NoTypeInformation` — yesterday's line.)*

**3. Hash the evidence.**
```powershell
Get-ChildItem "$E\baseline_v2_*.csv" | Get-FileHash -Algorithm SHA256 |
  Select-Object @{n='File';e={Split-Path $_.Path -Leaf}}, Hash | Export-Csv "$E\baseline_v2_hashes.csv" -NoTypeInformation
Import-Csv "$E\baseline_v2_hashes.csv"
```
> "Four files, four fingerprints. Day 03's rule — hash it, name it, lock it, log it. If anyone changes one line in any of these, the hash changes."

**4. Compare — services first (should be near-identical).**
```powershell
$old = Import-Csv "C:\Evidence\Day_04\baseline_services.csv"
$new = Import-Csv "$E\baseline_v2_services.csv"
Compare-Object $old $new -Property Name, StartType | Sort-Object Name
```
**What you will see:** nothing, or a few lines with `=>` / `<=`.
> "Nothing — good: no service appeared or disappeared overnight. If a line says `=>`, it is only in today's list: a new service. That is the same fact event 7045 would show in the System log. Two sources, one fact. That is verification, and you will do it properly next week."

**5. Compare — processes (will differ).**
```powershell
$old = Import-Csv "C:\Evidence\Day_04\baseline_processes.csv"
$new = Import-Csv "$E\baseline_v2_processes.csv"
Compare-Object $old $new -Property Name | Sort-Object Name
```
> "This one is long. That is churn — a browser open, a tool closed. Normal. The skill is telling churn from a new svhost32.exe in Users\Public. Services and autoruns should not churn; processes do."

**6. Register it.** Open the evidence register (Day 03's) and add one row per file: name, SHA-256, date, what it is.

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "What is the point of a baseline?" | The compare — the difference against a known-good copy |
| "`=>` in Compare-Object means?" | Only in the second (today's) list |
| "Which lists should not churn?" | Services and autoruns; processes do |

## Common problems
| Problem | Fix |
|---------|-----|
| `Compare-Object` shows everything different | `-Property` was omitted — name the property |
| No `Day_04` folder | Re-run yesterday's four exports into `Day_04` (2 min), then compare |
| Autoruns CSV shows odd characters in Calc | UTF-16 — choose it in the import dialog, or read with `Import-Csv` in PowerShell |

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Unzip Sysinternals to `C:\Tools\Sysinternals\`; run `procexp64`, `autoruns64`, `tcpview64` once **without admin**; accept EULAs; confirm VirusTotal is off
- [ ] Build `CV_Defender` in Event Viewer; read its XML; export it; delete it; import it
- [ ] Run cookbook #1, #2, #3, #7 — note which return "No events found" on your build
- [ ] Run the three-ways sequence for 7045 and the `Export-Csv` line; open the CSV
- [ ] Run all of Sample Data §6 against your own Day 04 CSVs; read the two compares
- [ ] Run `autorunsc64.exe … > file.csv`; open the file; note the encoding
- [ ] Take the fallback screenshots (Resources Part 3)

## The three sentences you should be able to say without notes
1. **Five channels — and know which one before you open Event Viewer.**
2. **A custom view is a saved question — build it once, export the XML, it is there every morning.**
3. **A baseline is only useful when you compare it — export, hash, diff.**
