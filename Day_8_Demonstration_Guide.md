# DAY 8 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 8 for the first time, to complete beginners

---

## READ THIS FIRST

Assumes nothing. **No server** — every check runs on your own Windows machine, using the EICAR detection you made on Day 6. **Total beginners** — every click shown, calm pace.

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic)* | A note for you — never read aloud |
| **What you will see** | What should appear |

**Five demonstrations, all follow-along:**

| # | Demonstration | When | Topic |
|---|--------------|------|-------|
| **1** | Two stories, one event — history vs the raw log | 8:15 | 8.1 |
| **2** | Did the action really happen? — three proofs | 8:55 | 8.2 |
| **3** | Up to date, or patched — four layers, one update | 9:30 | 8.3 |
| **4** | The four scans — a custom scan live | 10:10 | 8.4 |
| **5** | The worksheet end to end · Sandbox and Wazuh preview | 11:00 | 8.5 |

Screen setup is the same as Days 5–7: clean desktop, large text, notifications off, narrate, slow down. **Have PowerShell open before 8:00** — a normal window is fine; only open an admin window if a command tells you it needs one.

> **The one thing you must NOT do today: run the offline scan.** `Start-MpWDOScan`, or the "Microsoft Defender Offline scan" button, restarts the machine immediately. You would drop off the call for twenty minutes.

---
---

# DEMONSTRATION 1 — TWO STORIES, ONE EVENT
### 8:15 AM · Slides 3–4 · Topic 8.1 · E3 PC 3.1

## Why this exists
Beginners see the friendly view and the raw log of the *same* detection side by side, and tick off the four things that must match.

## What you need
- Your Day 6 EICAR detection still in Protection history and the Operational log *(if it is gone, recreate it tonight — Day 6 Demo 3, two minutes)*

## The steps
**1. Open the story — Protection history.**
> "Windows key, type Windows Security, open it. Virus & threat protection, then Protection history. Here is our EICAR from Day 6. This is the tool's STORY — its summary of what happened. Read the four things: the name, the file, the time, and the action."

**What you will see:** `Virus:DOS/EICAR_Test_File`, the file path in Documents, a date and time, and *Removed* or *Quarantined*.

**2. Now open the evidence — the raw log, in PowerShell.**
```powershell
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 60 |
  Where-Object { $_.Id -in 1116, 1117, 1118, 1119 } |
  Select-Object TimeCreated, Id, Message | Format-List
```
> "This reads the antivirus's own log — the one we opened in Event Viewer on Day 6 — and keeps only four kinds of line. 1116 means detected. 1117 means action taken. 1118 and 1119 mean the action FAILED."

**What you will see:** at least two entries — a **1116** and a **1117** — each with a `TimeCreated`, and a long `Message` that contains `Name:`, `Path:` and (on the 1117) `Action:`.

*(If the window is too busy, scroll up slowly and point. If `Get-WinEvent` says access denied, open Event Viewer → Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational, then Filter Current Log → Event IDs `1116,1117,1118,1119`. Same lines.)*

**3. Put them side by side and tick off the four things.**
> "Story says EICAR — log 1116 says EICAR. Tick. Story says Documents\eicar_test.txt — log says the same path. Tick. Story says 10:47 — log says 10:47 and two seconds. Tick; seconds don't matter, twenty minutes would. Story says Removed — log 1117 says Action: Remove. Tick. Four ticks. The story matches the evidence."

**4. Say what a mismatch would look like** *(slide 4 — Case 2 from Sample Data):*
> "Now imagine the ticket says 'quarantined, contained' — and the log has no 1117. It has an 1118: action FAILED, file in use. The story and the evidence disagree. Which one do you believe? The log. Always the log. That is a finding, and it changes the decision."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "What four things must match?" | Time, threat name, file path, action |
| "Which event ID proves the action was taken?" | 1117 |
| "Story and log disagree — which do you believe?" | The log; it is the evidence |

## Common problems
| Problem | Fix |
|---------|-----|
| No 1116/1117 in the log | The EICAR is too old or the log was cleared. Recreate it (Day 6 Demo 3) — the events appear within seconds |
| Message text is cut off | Add `| Out-String -Width 200` at the end, or read it in Event Viewer |
| Third-party AV on a trainee's machine | Their AV has its own history and its own log; pair them with a Defender machine for the commands |

---
---

# DEMONSTRATION 2 — DID THE ACTION REALLY HAPPEN?
### 8:55 AM · Slide 6 · Topic 8.2 · E3 PC 3.2

## Why this exists
Yesterday the class *read* the action. Today they *prove* it — three ways — so "quarantined" is never taken on trust again.

## The steps
**1. Proof one — the log said so.**
> "Proof one, we already have: the 1117. The tool logged that it acted, with error code zero — zero means no error."

**2. Proof two — the tool says it succeeded.**
```powershell
Get-MpThreatDetection | Select-Object InitialDetectionTime, Resources, ActionSuccess, ThreatStatusID
```
**What you will see:** one entry per detection; for EICAR, `ActionSuccess : True` and `ThreatStatusID : 3` (quarantined) or `4` (removed).

> "ActionSuccess True — the tool says it worked. And this number: 3 means quarantined, 4 means removed, 2 cleaned, 6 blocked. If you ever see a 1 — detected, nothing done — or anything over 100, that is a failure. Not contained. Which, from yesterday, means what?" *(A threat.)*

**3. Proof three — the file is actually gone.**
```powershell
Test-Path "$env:USERPROFILE\Documents\eicar_test.txt"
```
**What you will see:** `False`.

> "Test-Path asks Windows: does this file exist? False — it's gone. That is the physical proof. Three proofs: the log said so, the tool says it succeeded, and the file isn't there. Now it's proven."

**4. Show what quarantine actually holds** *(list only — restore nothing):*
```powershell
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Restore -ListAll
```
**What you will see:** a list of quarantined items (EICAR among them if it was quarantined rather than removed), or an empty list if it was removed.

> "This is the cage. Quarantined files sit here. If the tool caged a real work file by mistake, this is where you'd get it back — but not today, and never without your supervisor."

**5. Add the sixth action to the range** *(slide):*
> "Failed, clean, delete, quarantine, blocked — and the last one: RE-IMAGE. Wipe the machine and rebuild it. You use it when none of the others can be trusted — the malware keeps coming back, or the machine is too deep in. You won't re-image anything. Your job is to record that the other actions didn't hold, and recommend it. That's tomorrow."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Three proofs of an action?" | Event 1117; `ActionSuccess` True; `Test-Path` False |
| "`ThreatStatusID` is 102. Contained?" | No — quarantine failed. Threat |
| "When is re-image the answer?" | When clean/delete/quarantine cannot be trusted; an L1 recommends, does not do it |

## Common problems
| Problem | Fix |
|---------|-----|
| `Get-MpThreatDetection` returns nothing | The detection history was cleared, or third-party AV. Recreate EICAR; or read `ActionSuccess` from Protection history wording ("Removed" = success) |
| `Test-Path` returns True | The file is still there — real-time protection is off, or the AV differs. **That is a finding.** Check Windows Security; report it as you would on a real desk |
| `MpCmdRun.exe` path not found | Try `"C:\ProgramData\Microsoft\Windows Defender\Platform\<newest folder>\MpCmdRun.exe"` — or skip; steps 1–3 are the proof |

---
---

# DEMONSTRATION 3 — UP TO DATE, OR PATCHED
### 9:30 AM · Slide 8 · Topic 8.3 · E3 PC 3.3

## Why this exists
Four version numbers most people never read, one update the trainee runs and evidences, and the line between what an L1 patches and what they report.

## The steps
**1. Read the four layers — before.**
```powershell
Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AntivirusSignatureVersion, AntivirusSignatureLastUpdated, AntivirusSignatureAge
```
**What you will see:** four version strings and an age in days.

> "Four layers. AMProductVersion — the platform, the product itself. AMEngineVersion — the scanner engine. AntivirusSignatureVersion — the list of known threats, and its age in days. Write the signature version down. We're about to change it."

**2. Run the signature update.**
```powershell
Update-MpSignature
```
*(If it says access denied, do not fight it:)* Windows key → `Windows Security` → Virus & threat protection → **Virus & threat protection updates** → **Check for updates**.

**What you will see:** the command returns quietly after a few seconds (or the GUI shows "checking…" then a new "last updated" time).

> "Silence is good news in PowerShell. Now read it again."

**3. Read the four layers — after.**
*(Run the step-1 command again.)*
> "Signature version changed — or the age is now zero. Before and after. That is your evidence that you patched it. And in the log, this writes an event 2000, signature updated. If it ever writes 2001, the update failed — that's a finding."

**4. Now the operating system.**
```powershell
Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5 HotFixID, Description, InstalledOn
```
**What you will see:** the five most recent Windows updates with dates. *(`InstalledOn` may be blank on some builds — then open Settings → Windows Update and read "last checked" / update history.)*

> "The newest security update — how old is it? A month, fine. Four months — that's a finding. The antivirus can be perfect and the machine still be open, because the operating system has holes the AV doesn't cover."

**5. Draw the line.**
> "You update the antivirus signatures yourself — you just did. You do NOT patch the operating system on a server by yourself. That needs a change window and IT's say-so. Your job on the OS is to find that it's behind, and report it. 'As required' means as the SOP requires — and the SOP doesn't say reboot the file server at half past nine."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Four layers?" | Signatures, engine, platform, operating system |
| "What is your evidence that you updated?" | The signature version / age before and after (and event 2000) |
| "OS on a server is four months behind. What do you do?" | Report it to IT for a change window — not patch it yourself |

## Common problems
| Problem | Fix |
|---------|-----|
| `Update-MpSignature` access denied | Windows Security GUI → Check for updates |
| No internet | The update fails (event 2001) — which is itself a finding to show; read versions anyway |
| `InstalledOn` blank | Settings → Windows Update → Update history |

---
---

# DEMONSTRATION 4 — THE FOUR SCANS · A CUSTOM SCAN LIVE
### 10:10 AM · Slides 9–10 · Topic 8.4 · E3 PC 3.4

## Why this exists
Four scan types and the rule for choosing. The class watches one run end to end and learns why "nothing found" on a healthy machine is the correct result.

## What you need
- The folder `Documents\ScanTest` with one harmless `.txt` in it *(made the night before)*

## The steps
**1. Name the four** *(slide 9):*
> "Quick — the usual hiding places, minutes. Full — every file on every drive, hours. Custom — one folder or drive you pick, seconds. Offline — the machine restarts into a small scanner that runs BEFORE Windows, for malware that hides from Windows. Rule: quick for routine, custom for one place, full when you suspect and don't know where, offline when the machine itself can't be trusted."

**2. Say the honest thing BEFORE you scan.**
> "I'm about to scan a folder. It will find nothing — and that is correct. Real-time protection already removed the EICAR the moment it was saved on Day 6. A scan is for what real-time protection MISSED — a file that arrived while protection was off, a USB drive just plugged in, something hiding. Watch the process, not the result."

**3. Run a custom scan on the folder — the version that shows its result.**
```powershell
& "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -Scan -ScanType 3 -File "$env:USERPROFILE\Documents\ScanTest"
```
**What you will see:** `Scan starting...` then `Scan finished.` then a line like `Scanning C:\Users\...\ScanTest found no threats.`

> "Scan type 3 is custom. It scanned that one folder and found no threats. That line is your scan log. It's also written to a file — MpCmdRun.log in your Temp folder — and the antivirus log gets an event 1000, scan started, and 1001, scan finished."

*(The PowerShell equivalent is `Start-MpScan -ScanType CustomScan -ScanPath "..."` — it returns silently; the result is in the log. Use `MpCmdRun` live because beginners need to see the words.)*

**4. Show where the same four scans live in the GUI.**
> "Windows Security → Virus & threat protection → Scan options. Quick, Full, Custom — and there, at the bottom, Microsoft Defender Offline scan. Do NOT click that one. It restarts your computer right now. We'll talk about when it's the right call; we will not run it in class."

**5. Start a quick scan and leave it.**
```powershell
Start-MpScan -ScanType QuickScan
```
*(Or GUI → Quick scan. If it needs admin, GUI.)*
> "A quick scan takes a few minutes. Start it, let it run, carry on. Never sit and watch a scan. When it finishes, the log gets a 1001. If it stops early, a 1002 — and a scan that didn't finish is not a scan."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "A user hands you a USB drive. Which scan?" | Custom — you know exactly where |
| "Custom scan found nothing. Did it fail?" | No — real-time protection got there first; scans are for what it missed |
| "Which scan restarts the machine?" | Offline — never in class |

## Common problems
| Problem | Fix |
|---------|-----|
| `MpCmdRun.exe` not found at that path | `Start-MpScan -ScanType CustomScan -ScanPath ...`, then show the 1000/1001 events in the log |
| `Start-MpScan` access denied | Windows Security → Scan options |
| A trainee's scan finds something | Wonderful — read it as an alert (Day 6), record it, and it goes on their worksheet as a real detection |

---
---

# DEMONSTRATION 5 — THE WORKSHEET END TO END · SANDBOX AND WAZUH PREVIEW
### 11:00 AM · Slides 12–13 · Topic 8.5 · E3 all

## Why this exists
Fill one verification worksheet on screen, in order, so the afternoon's five are not a surprise — then two minutes on where this goes once the room has a server.

## What you need
- The worksheet template (Sample Data §5) open in a document, empty
- Your EICAR case — you have every row already from Demos 1–4

## The steps
**1. Fill rows 1–3 from Demo 1.**
> "Row 1, the story: EICAR, Documents, 10:47, removed. Row 2, the evidence: 1116 and 1117, same name, same path, same minute, Action: Remove. Row 3: four ticks, no mismatch."

**2. Fill rows 4–5 from Demo 2.**
> "Row 4, proven? 1117 present — yes. ActionSuccess True — yes. Test-Path False — yes. Row 5, outcome: contained."

**3. Fill rows 6–7 from Demos 3–4.**
> "Row 6, up to date: signatures age zero after my update, engine and platform this month, OS patched this month. Row 7, scan: custom on ScanTest, because it's one folder; result, nothing found — expected."

**4. Write the verdict — last, and with a reason.**
> "Row 8. Four possible verdicts: verified detection; failed action, which is a threat, escalate; more than the story, follow up; not yet acted on, act now. Here: VERIFIED DETECTION — because rows 3, 4 and 5 all say so. The verdict comes last, and it has to agree with your own rows."

**5. The two-minute preview** *(screenshots from Resources — nothing live):*
> "Two things you'll meet later. Windows Sandbox — a throw-away copy of Windows inside your Windows, where you can open something suspicious and then close it and it's gone. Needs Windows Pro and more memory than most of our machines have, so today it's a picture. And Wazuh — when our server exists, every 1116 and 1117 from every machine arrives there, in one search. The worksheet doesn't change. Only where the evidence comes from."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Which row do you fill last?" | Row 8, the verdict — it must agree with rows 3–5 |
| "Story says quarantined, log has an 1118. Verdict?" | Failed action → threat, escalate |
| "Does Wazuh change the worksheet?" | No — only where the evidence comes from |

## If you are offline
Everything is local except the signature update (which then fails — a finding you can show) and the two preview screenshots (in Resources).

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Confirm your EICAR events 1116/1117 are in the Operational log (`Get-WinEvent` above); if not, recreate EICAR
- [ ] `Get-MpThreatDetection` — read your `ActionSuccess` and `ThreatStatusID`
- [ ] `Test-Path` on the EICAR path — expect `False`
- [ ] `MpCmdRun.exe -Restore -ListAll` once (list only)
- [ ] `Get-MpComputerStatus` four layers; run `Update-MpSignature` (or the GUI); read again
- [ ] `Get-HotFix` top five — note whether `InstalledOn` is populated on your build
- [ ] Create `Documents\ScanTest` with one `.txt`; run the `MpCmdRun -Scan -ScanType 3` line; read the result
- [ ] Find the Scan options page and note where the Offline button is — **so you can point at it without clicking it**
- [ ] Fill one worksheet from your own values; keep it as your Demo 5 model

## The three sentences you should be able to say without notes
1. **The tool tells a story; the log is the evidence — match time, name, path, action.**
2. **An action is proven, not assumed — event 1117, `ActionSuccess`, and the file itself.**
3. **Quick for routine, custom for one place, full when you suspect, offline when the machine can't be trusted.**
