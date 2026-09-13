# DAY 7 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 7 for the first time, to complete beginners

---

## READ THIS FIRST

Assumes nothing. **No server** — the ticket "system" is a shared spreadsheet, and every status check runs on your own Windows machine. **Total beginners** — every click shown, calm pace.

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
| **1** | Raise the ticket — the register | 8:55 | 7.2 |
| **2** | Is it installed and operational? | 9:45 | 7.3 |
| **3** | Reading the tool's own status | 10:10 | 7.3 |
| **4** | Can it clean up? — the EICAR action | 10:55 | 7.4 |
| **5** | The management console · Wazuh preview | 11:10 | 7.5 |

Screen setup is the same as Days 5–6: clean desktop, large text, notifications off, narrate, slow down.

---
---

# DEMONSTRATION 1 — RAISE THE TICKET
### 8:55 AM · Slide 6 · Topic 7.2 · E1 PC 1.5

## Why this exists
Beginners see a ticket built field by field, in a real register, using their own Day 3 QA checklist as the field list.

## What you need
- The shared **ticket register** spreadsheet (columns from `Day_7_Sample_Data.md` §2)
- One alert to ticket — use **Alert G** (the failed quarantine); it is the richest

## The steps
**1. Open the shared register and show the columns.**
> "This is our ticket system for now — a shared spreadsheet. Each column is a field a ticketing tool would have. Same information, no server needed. And look — these fields are almost exactly the checklist YOU wrote on Day 3."

**2. Take Alert G and fill one row live, thinking aloud.**
> "Summary: backup server, failed quarantine of a Trojan. Host: SRV-BAK-02. Time it happened, 03:40. Time I saw it, now. What the tool detected — and here's the key part — the quarantine FAILED."

**3. Stop on the decision field and make the containment point.**
> "Decision. The antivirus found it — so is this a detection? No. The quarantine failed. It is not contained. That makes it a THREAT, not a detection. Reason: action failed, not contained, and it's a backup server. Severity: Critical."

**4. Fill the two timestamps, the action, and the ask.**
> "Two times, always — when it happened and when I saw it. What I did: raised this ticket, did not isolate the host because that's above my level. What I need: L2 to isolate the machine and find what's holding the file. A ticket with no ask is a diary entry."

**5. Point at the SLA column.**
> "Critical means notify within ten minutes — that's the SLA, the promise about how fast. The clock started the moment I raised this. That's why we raise it promptly and stamp the time."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "Why is Alert G a threat, not a detection?" | The quarantine failed — it is not contained |
| "How many timestamps, and which?" | Two — when it happened, and when you saw it |
| "What makes a ticket useful to the next person?" | A clear reason, and a specific ask |

---
---

# DEMONSTRATION 2 — IS IT INSTALLED AND OPERATIONAL?
### 9:45 AM · Slide 8 · Topic 7.3 · E2 PC 2.1, 2.2

## Why this exists
Element 2's first questions, checked on the endpoint. Beginners run the same commands.

## The steps
**1. Is the tool installed? Check the service.**
```powershell
Get-Service WinDefend | Select-Object Name, Status, StartType
```
**What you will see:** `WinDefend  Running  Automatic`.
> "The antivirus is a Windows service called WinDefend. Running and Automatic means it is installed and starts with the machine. That answers question one: installed? Yes."

**2. Is it operational? Open the Windows Security app.**
> "Windows key, type Windows Security, open it. Green ticks mean it is protecting the machine right now. A red or yellow mark means something is off — and that is a finding."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "What service is Defender?" | WinDefend |
| "Installed and operational — same thing?" | No. A tool can be installed and switched off |

## Common problems
| Problem | Fix |
|---------|-----|
| Third-party AV instead of Defender | WinDefend may be stopped because another AV took over — show that AV's own status; same three questions |

---
---

# DEMONSTRATION 3 — READING THE TOOL'S OWN STATUS
### 10:10 AM · Slide 9 · Topic 7.3 · E2 PC 2.2

## Why this exists
The precise command that answers "operational and up to date" — the same one from Day 5's baseline, now for its real purpose.

## The steps
**1. Run the status command.**
```powershell
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureVersion, AntivirusSignatureLastUpdated, QuickScanAge
```
**What you will see:** a list; on a healthy machine everything is `True` and the signature date is recent.

**2. Read it out, question by question.**
> "AMServiceEnabled True — the engine is running. AntivirusEnabled True — it's on. RealTimeProtectionEnabled True — it's watching right now. Signature date recent — it knows about recent threats. QuickScanAge small — it scanned recently. All good."

**3. Show what a FINDING looks like** *(use scenario 2 or 3 from Sample Data §3 on the slide):*
> "Now imagine RealTimeProtectionEnabled said False. The tool is installed, but it is NOT protecting the machine. That is a real finding — you would report it. A tool that is off is worse than no tool, because people think they're safe."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Which field tells you it's watching right now?" | RealTimeProtectionEnabled |
| "Signatures are 41 days old. Problem?" | Yes — it will miss recent threats. Report it |

## Common problems
| Problem | Fix |
|---------|-----|
| Command errors | Use the Windows Security app GUI — same information in words |

---
---

# DEMONSTRATION 4 — CAN IT CLEAN UP? (THE EICAR ACTION)
### 10:55 AM · Slide 11 · Topic 7.4 · E2 PC 2.3

## Why this exists
The last Element 2 question, proven with the safe EICAR detection from Day 6.

## The steps
**1. Open Protection history** (Windows Security → Virus & threat protection → Protection history) and find the EICAR entry.
> "Here is yesterday's EICAR detection. Look at the action — Quarantined, or Removed. That answers question three: can it clean or delete? Yes, it did."

**2. Name the full action range** *(slide):*
> "The standard lists the actions a tool can take: Failed, Clean, Delete, Quarantine, Blocked, Re-image. Quarantine means the file is caged, not deleted — it can be let back out if it turns out to be safe."

**3. Show the quarantine tool** *(optional, don't restore anything live):*
```
"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Restore -ListAll
```
> "This lists what's in quarantine. If the antivirus caged a file it shouldn't have — a real work file — this is how you'd get it back. We won't restore anything now."

**4. Tie it back to the decision.**
> "And the key link: if the action had said FAILED — like Alert G this morning — the issue is NOT contained, and that makes it a threat, not a detection. Checking the action is how you find that out."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "What action did Defender take on EICAR?" | Quarantined or removed — a success |
| "The action says Failed. Threat or detection?" | Threat — not contained |
| "Is quarantine the same as delete?" | No — quarantine cages it; it can be restored |

---
---

# DEMONSTRATION 5 — THE MANAGEMENT CONSOLE · WAZUH PREVIEW
### 11:10 AM · Slides 12–13 · Topic 7.5 · knowledge 1.8

## Why this exists
Show the idea of one screen for many machines, and set expectations for the Wazuh dashboard once the server exists.

## The steps
**1. Use the Windows Security app as the local console.**
> "Everything we checked today was for ONE machine. Windows Security is that machine's own little console — installed, operational, up to date, what has it found. All on one screen."

**2. Show the Wazuh preview screenshot** *(from Resources — do not need a live server):*
> "Once our server is built, you'll use a real console called Wazuh. Here's what it looks like. This list is every machine — which ones are connected, which have the tool, which are out of date, and what each has detected. It answers the exact same questions we asked today, but for the whole company at once."

**3. Set the expectation honestly.**
> "We don't have that server yet, so today you learned the questions on your own machine. When the server is ready, the console won't be a new skill — it'll just be showing you the same answers for everyone."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "What does a management console do?" | Answers the same status questions for many machines at once |
| "Is the Wazuh console a new skill?" | No — the same checks, shown for the whole fleet |

## If you are offline
Everything except the Wazuh screenshot is local. The screenshot is in Resources.

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Build/open the ticket register; fill one row from Alert G
- [ ] `Get-Service WinDefend` and `Get-MpComputerStatus` — read your own values
- [ ] Open Windows Security; note where the green ticks and any warnings are
- [ ] Find the EICAR entry in Protection history; read its action
- [ ] Run `MpCmdRun.exe -Restore -ListAll` once (list only; restore nothing)
- [ ] Have the Wazuh preview screenshot ready

## The three sentences you should be able to say without notes
1. **Threat vs detection is CONTAINMENT — a failed action makes it a threat.**
2. **A ticket has two timestamps, a reason, and a specific ask — it is written for the next person.**
3. **Installed, operational, up to date — three separate checks; a tool that is off is worse than none.**
