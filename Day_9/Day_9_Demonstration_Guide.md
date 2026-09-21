# DAY 9 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 9 for the first time, to complete beginners

---

## READ THIS FIRST

Assumes nothing. **No server** — failed actions come from Defender's own log on your machine and from a paper extract; the ticket register is the shared spreadsheet; the escalation goes by email or is pasted into the register. **Total beginners** — every click shown, calm pace.

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic)* | A note for you — never read aloud |
| **What you will see** | What should appear |

**Five demonstrations:**

| # | Demonstration | When | Topic |
|---|--------------|------|-------|
| **1** | Tell the client — the V1 call, then the written confirmation | 8:30 | 9.2 |
| **2** | Read the log for what failed — own machine, then the extract | 9:20 | 9.3 |
| **3** | Who do you call? — three situations worked aloud | 10:10 | 9.4 |
| **4** | Build the escalation pack — Situation 1, live, and log the trail | 10:45 | 9.5 |
| **5** | Preview — timeline tools and Wazuh alert search | 11:00 | 9.5 |

Screen setup as Days 5–8: clean desktop, large text, notifications off, narrate, slow down. **Demo 1 is a role-play, not a screen** — turn your camera on and put the call script (Sample Data §1) on your second screen.

---
---

# DEMONSTRATION 1 — TELL THE CLIENT
### 8:30 AM · Slide 4 · Topic 9.2 · E4 PC 4.1

## Why this exists
Beginners hear a verification call done properly — ticket ID first, the result plainly, one ask, a read-back — and then watch the same facts become the written confirmation. Case V1 (clean) is the model; Activity 1 adds V2 (not clean).

## What you need
- Case V1 from Sample Data §1 on your second screen
- A co-host to play **M. Lopez** *(or read both parts — change your voice a little; it works)*
- The written-confirmation template (Sample Data §7) open in a document
- The ticket register open at the WKS-118 row

## The steps
**1. Set the scene.**
> "Yesterday's Case 2 — WKS-118. The quarantine had failed. L2 stopped the process, quarantined it, ran a full scan: clean. The machine's user, M. Lopez in Marketing, has been told not to touch it since yesterday. She is not technical. I'm going to call her. Listen for eight things."

**2. Make the call** *(camera on; read the analyst; co-host reads Lopez):*
> "Good morning, Ms Lopez, this is Chester from the security desk, about ticket CTM-0007-014 — your computer, WKS-118."
> "Yesterday our antivirus found a malicious program in a file you had downloaded — setup_crack.exe. Our second-line team removed it this morning, and then we ran a full scan of the whole computer. The scan finished at 10:48 and found nothing else. Your computer is clean."
> "What that means for you: you can use it again now."
> "What happens next: I'm closing the ticket today."
> "One thing I need from you: that file came from a cracked-software site. Please don't download software from sites like that again — if you need a program, ask IT. And if anything looks odd on the machine, call this desk."
> "Just so I know I've explained it clearly — could you tell me back what you'll do?"

*(Lopez reads back: use the machine, no cracked downloads, call the desk if odd.)*

> "Perfect. I'll send you all of this in writing within the hour. Thanks, Ms Lopez."

**3. Debrief — count the eight.**
> "Eight things. Who I am and the ticket ID. What was found — in plain words, no threat names. What was done and what the scan showed. What it means for her. What happens next. One specific ask — not 'be careful', a thing she can do. The read-back. And 'in writing within the hour'. That last one is what we do now."

**4. Write the confirmation** *(fill the template on screen, thinking aloud):*
> "Same facts, in writing. Subject line: ticket, host, and the word CLEAN. Six numbered lines — found, done, scan result, what it means, what next, what we need. Then 'please reply to confirm'. This goes to her — and it goes into the ticket."

**5. Paste it into the register row.**
> "WKS-118 row. Status: Verified with client. Notes: confirmation sent 08:41. That's the record. The call was the courtesy; this is the evidence."

**6. Say the hard sentence for V2, before the activity.**
> "In a moment half of you will make the OTHER call — SRV-BAK-02, where the scan finished and the threat is STILL THERE. Beginners soften that: 'there might still be something'. No. The sentence is: 'The scan finished, and the threat is still on the server. It is not clean. Here is what happens next.' Say it plainly. The stakeholder needs the truth to protect the backups."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "What is the first thing you say after your name?" | The ticket ID |
| "Why the read-back?" | To know you were understood — Day 1's rule |
| "Which is the record — the call or the confirmation?" | The written confirmation, in the ticket |

## Common problems
| Problem | Fix |
|---------|-----|
| No co-host | Read both parts |
| The call runs long | Cut the small talk; the eight steps take under two minutes |
| Trainees ask "what if she argues?" | Stay on the facts, repeat the ask, offer to have IT call her — and note it in the ticket |

---
---

# DEMONSTRATION 2 — READ THE LOG FOR WHAT FAILED
### 9:20 AM · Slides 6–7 · Topic 9.3 · E4 PC 4.2

## Why this exists
The failed-action pass, first on your own machine (where it finds nothing — and that is the correct result), then on the paper extract where the class learns the five kinds.

## What you need
- PowerShell open
- The extract (Sample Data §2) ready to paste on screen
- The taxonomy (§3) on slide 7

## The steps
**1. Say what you expect, before you run anything.**
> "I'm going to ask my own machine: did any action fail? Did any scan stop early? It will say no — my machine is healthy. And 'no failed actions on this host, checked at 9:22' is a correct record. On a real desk you write that down too."

**2. Any detection whose action did not succeed?**
```powershell
Get-MpThreatDetection | Where-Object { -not $_.ActionSuccess } |
  Select-Object InitialDetectionTime, Resources, ActionSuccess, ThreatStatusID
```
**What you will see:** nothing (an empty result).
> "Empty. Every detection on this machine had a successful action. If there were a line here, its ThreatStatusID would be 1 — nothing done — or 102, 103, 104 — quarantine, remove, clean failed."

**3. Any failed-action or stopped-scan events?**
```powershell
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 200 |
  Where-Object { $_.Id -in 1118, 1119, 1002, 2001 } |
  Select-Object TimeCreated, Id, Message | Format-List
```
**What you will see:** nothing, or a "No events were found" message in red — *which is fine; say so.*
> "1118 and 1119 — an action failed. 1002 — a scan stopped early. 2001 — the update failed. None here. Good. Now let's read a machine where it is not good."

**4. Paste the extract and read entry A.**
> "Eight entries from one desk, one morning. A: 1116 detected, 1117 quarantine, error code zero. That's a success — Day 8, four ticks. Move on."

**5. Read entry B — two kinds at once.**
> "B: 1116 detected, same threat, different path — then 1118: quarantine FAILED, file in use. That's kind one, ACTION FAILED. And five seconds later — another 1116 for the same file. It's still there and the tool is detecting it again. That is also kind five, THREAT CAME BACK. Not contained. Threat. This ticket re-opens, and it escalates."

**6. Read entry C — the one without the word 'failed'.**
> "C: 1000, full scan started 03:05. Then 1002 at 03:41 — scan stopped before completion. Reason: user cancelled. Nobody wrote 'failed'. But a scan that didn't finish is not a scan. Kind four. Re-run it — and find out who cancelled a scan on a file server at three in the morning."

**7. Hand over the rest** *(slide 7 — the five kinds):*
> "Five kinds. Action failed. Action incomplete — usually 'restart required'. No action taken — a 1116 with silence after it. Scan did not complete — the 1002. Threat came back — a new 1116 after a good 1117. Two of the five have no word 'failed' anywhere. Your teams find the other five entries."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Your own machine shows nothing. What do you write?" | "No failed actions on <host>, checked <time>" |
| "Which two kinds have no word 'failed' in the log?" | No action taken (silence after 1116) and scan did not complete (1002) |
| "Entry B — which kinds?" | 1 (action failed) and 5 (came back) |

## Common problems
| Problem | Fix |
|---------|-----|
| `Get-WinEvent` shows a red "No events were found" | That is the answer — read it aloud as such |
| Access denied on the log | Protection history — "Action needed", "Remediation incomplete", "Failed" are the same kinds in words |
| A trainee's machine actually shows an 1118 | Real finding. Name the kind together; it becomes their Task 2 extract |

---
---

# DEMONSTRATION 3 — WHO DO YOU CALL?
### 10:10 AM · Slides 9–10 · Topic 9.4 · E4 PC 4.3

## Why this exists
The four authorities from the CS, made concrete with three worked situations, so Activity 3 is not a guess.

## What you need
- The authority matrix (Sample Data §5) on slide 9
- Situations 1, 3 and 5 (§4) on slide 10

## The steps
**1. The matrix, one line each.**
> "Four people the standard names. IT department manager — owns the machines and the change calendar; send them anything that needs an IT action: isolate, restart, re-image, patch. Information security manager — owns the security decision; send them any threat that is not contained, any sign of spread. The security vendor — owns the product; send them the tool failing, or a false positive. And the CISO — owns the business risk; gets Critical, in one paragraph, within ten minutes, usually through the security manager."

**2. The one rule.**
> "Pick the person who can DO the thing you need. That's the whole rule. And three habits: your first stop is your L2 or shift lead. One primary authority — copy the others. Critical goes up fast."

**3. Situation 1 — SRV-BAK-02.**
> "Quarantine failed twice, the process restarts itself, the scan says it's still there. Not contained, on a backup server. What do I need? A security decision — isolate now? — and someone to physically isolate it. Primary: the information security manager. Copy: the IT manager, because the isolation is his action. Severity Critical, so the security manager will take it to the CISO."

**4. Situation 3 — payroll_calc.xlsm.**
> "Defender quarantined the payroll macro workbook. Used safely for two years, payroll is tomorrow. This is probably a false positive — but 'probably' is not my call. Who owns whether the product is wrong? The vendor. Primary: open a vendor case with the detection name, the file hash, the versions. Copy: the security manager. And what I do NOT do: restore the file myself. It might be real. Above my level."

**5. Situation 5 — SRV-FIN-02.**
> "Files renaming to .locked right now, spreading. Finance is down. This is Critical, business on fire. The CISO must know within ten minutes — one paragraph: what, since when, how many, what's being done, what decision is needed. Through the security manager, who is also the one deciding isolation, and the IT manager pulls the cable. Everybody, now — but the CISO paragraph is the short one."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "A legitimate business file got quarantined. Who?" | The vendor — false-positive case; don't restore it yourself |
| "An OS four months unpatched. Who?" | The IT department manager — a change window |
| "What does the CISO get?" | Critical only; one paragraph; within ten minutes |

## Common problems
| Problem | Fix |
|---------|-----|
| "Why not the CISO for everything serious?" | The CISO decides business risk, not machines. Send the decision-maker who can act |
| Trainees split hairs between IT and infosec manager | Ask: is the thing you need a machine action or a security decision? |

---
---

# DEMONSTRATION 4 — BUILD THE ESCALATION PACK
### 10:45 AM · Slides 12 · Topic 9.5 · E4 PC 4.3

## Why this exists
The 12-field pack, filled live for Situation 1 — the same SRV-BAK-02 case the class ticketed on Day 7 and verified on Day 8 — and then the register row updated so the trail exists.

## What you need
- The pack template (Sample Data §6) open, empty
- The extract entry F (§2) and ticket CTM-0007-001 (Day 7) on screen
- The ticket register open at the SRV-BAK-02 row

## The steps
**1. Fields 1–3 — to whom, from whom, one line.**
> "To: Information security manager — because I need a security decision, isolate now, and he owns that. Copy: IT department manager, for the isolation itself. From: me, 10:48, ticket CTM-0007-001 — the ticket we wrote on Day 7. Summary: SRV-BAK-02 — Trojan.Agent.XZ — quarantine failed twice, not contained."

**2. Fields 4–5 — the story, then the evidence.**
> "What was detected: Trojan.Agent.XZ in svhost32.exe, first seen 2026-09-15 03:40. What the evidence shows — and this is the part that makes it a pack and not an opinion — the log lines: 1118 on the 15th at 03:40, quarantine failed, file in use. 1118 again on the 17th at 08:22. Full scan 08:25 to 09:58 — one threat found, same file. ThreatStatusID 102. Test-Path True. Attached as an extract."

**3. Field 6 — what was tried, and what failed, by kind.**
> "Tried: quarantine, 15th — failed, kind one, file in use. L2 ended the process, 17th — it restarted itself in four seconds. Quarantine again — failed, kind one. Full scan — completed, threat still present. That's kind five as well: it keeps coming back."

**4. Fields 7–8 — status, severity, clock, impact.**
> "Not contained. Critical — backup server. Ticket raised 15th 09:05, so the Critical SLA is long blown — say so. Impact: every backup taken since the 15th 03:40 may be tainted; restores from them are unsafe until this is cleared."

**5. Field 9 — the ask, with a deadline.**
> "What I need from you: a decision to isolate SRV-BAK-02 from the network — by 11:30 today — and L2 or IT to identify the process that keeps restarting the file. Verb, object, time. Not 'please advise'."

**6. Fields 10–12 — recommendation, attachments, logged.**
> "Recommendation: isolate now; if the process can't be identified and removed, re-image from a build before the 15th. Attachments: Day 8 verification worksheet, the log extract, two screenshots. Logged: ticket updated 10:52, escalated to the security manager, copied IT manager."

**7. Update the register row — the trail.**
> "Now the row. Status: Escalated. Escalated to: Information security manager. Time: 10:52. Next update due: 11:30. Without this row, the pack is a document somebody sent. With it, there's a trail an assessor — or an auditor — can follow."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "What turns an opinion into a pack?" | The log lines — the evidence |
| "What is wrong with 'please advise'?" | No verb, no deadline — it will wait |
| "Where is the trail?" | The register row — status, to whom, when, next update due |

---
---

# DEMONSTRATION 5 — PREVIEW: TIMELINE TOOLS AND WAZUH
### 11:00 AM · Slide 13 · Topic 9.5 · two minutes, screenshots only

## Why this exists
Set the expectation that the failed-action pass gets faster with tools — and that the kinds, the matrix and the pack do not change.

## The steps
**1. Hayabusa / Timeline Explorer** *(one screenshot from Resources):*
> "This is Hayabusa. One command, and it reads the whole event log into a spreadsheet timeline — every 1118 flagged, in order. Timeline Explorer opens it. Same log you read by hand today, in seconds. You'll use it in the on-site lab."

**2. Wazuh alert search** *(one screenshot):*
> "And once our server exists — every machine's 1118s in one search. Entry F from today's extract would be one line here, with the host name next to it."

**3. The point.**
> "Faster finding. Same five kinds. Same four authorities. Same pack. Today you learned the part that doesn't change."

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Read the V1 call aloud once, with a timer — under two minutes
- [ ] Fill the written confirmation for V1 from the template; keep it as your Demo 1 model
- [ ] Run the two `Get-MpThreatDetection` / `Get-WinEvent` failed-action commands; note exactly what "nothing" looks like on your build (empty, or red "No events were found")
- [ ] Read extract entries A, B, C aloud and name the kinds without looking at the key
- [ ] Say the three Demo 3 situations aloud — 1 infosec manager, 3 vendor, 5 CISO via infosec manager
- [ ] Fill the pack for Situation 1 from the template; keep it as your Demo 4 model
- [ ] Add the SRV-BAK-02, WKS-118 and WKS-205 rows to the register so Demo 1 and Demo 4 update real rows
- [ ] Have the Hayabusa and Wazuh screenshots ready

## The three sentences you should be able to say without notes
1. **A case is closed when the client knows the truth and the authority has what they need — not before.**
2. **Five kinds of failure — and two of them never say "failed": silence after a 1116, and a 1002.**
3. **Evidence, ask, deadline — and pick the authority who can do the thing you need.**
