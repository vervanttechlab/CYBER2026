# DAY 8 — INSTRUCTOR GUIDE
## Topic: Verify — Does the Tool's Story Match the Evidence?
### Cyber Threat Monitoring Level I · Day 08 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **Same two conditions as Days 6–7.** (1) **No SIEM server yet** — everything runs on each trainee's own Windows machine with Microsoft Defender; the "infected system" is their own machine with yesterday's EICAR detection on it. (2) **Total beginners** — assume nothing, every click shown, calm pace.

---

## HOW THIS GUIDE WORKS

The **topic guide** — what Day 8 teaches, why, what you must know, and how it is assessed. Not a script. Keep these open:

| File | For |
|------|-----|
| **`Day_8_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_8_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_8_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_8_Student_Activity_Pack.docx`** | what the trainees do |
| **`Day_8_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_8_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_8_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_8_Sample_Data.md`** | the 5 verification cases, event IDs, patch and scan scenarios, the worksheet |

---
---

# PART A — WHAT DAY 8 IS

## The one-sentence topic

> **Day 7 checked that the security tool was working. Day 8 checks what the tool *said*: match its story to the raw log, prove the action really happened, bring the tool and the machine up to date, and run the right kind of scan — then write a verdict you can defend.**

## Where Day 8 sits

Day 8 delivers all of **Element 3** of the core unit — *Perform manual checking and verification*:

| Element / PC | What Day 8 does |
|--------------|-----------------|
| **E3 PC 3.1** Detection from the security solution software is checked as per procedure | Topic 8.1 — the story (Protection history / ticket) against the evidence (the Operational log) |
| **E3 PC 3.2** Action of the security solution software is checked as per company SOP | Topic 8.2 — proving the action three ways; the action range revisited |
| **E3 PC 3.3** Security solution software updates are checked and patched as required | Topic 8.3 — signatures, engine, platform, OS patch state; run the update |
| **E3 PC 3.4** Security solution software is used to scan infected system/s | Topic 8.4 — quick, full, custom, offline; which one and why |
| **E3 (all)** | Topic 8.5 — the verification worksheet that ties the four together |

After today, Elements 1, 2 and 3 are done. Element 4 (case follow-up and escalation) is Day 9; Element 5 (reporting) and the unit assessment are Day 10.

## What "no server" changes

The plan used Windows Sandbox as a disposable "infected system" and Atomic Red Team for safe attack behaviour. With no server, low-spec machines and total beginners, Day 8 does the same job on the trainee's own machine:

| Plan's bench (not used today) | Day 8 uses instead |
|-------------------------------|--------------------|
| Windows Sandbox as the "infected system" | **The trainee's own machine** — it already holds a real detection (Day 6 EICAR) with a real log trail |
| Atomic Red Team behaviours | **Five paper cases** in Sample Data §1, written as real Defender log lines, incl. a failed action and a missing action |
| Wazuh agent log, server-side | **Defender Operational log + `Get-MpThreatDetection`** on the endpoint |

Sandbox and Wazuh become a two-minute **preview** in Topic 8.5. Nothing in Element 3 depends on them.

## The five topics of Day 8

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **8.1** | **Two Stories, One Event** — the tool's story against the raw log | E3 PC 3.1 | 20 min + Activity 1 |
| **8.2** | **Did the Action Really Happen?** — proving it three ways | E3 PC 3.2 | 15 min + Activity 2 |
| **8.3** | **Up to Date, or Patched** — signatures, engine, platform, OS | E3 PC 3.3 | 30 min |
| **8.4** | **Scan the Suspect Machine** — quick, full, custom, offline | E3 PC 3.4 | 20 min + Activity 3 |
| **8.5** | **The Verification Worksheet** — detection → action → outcome → verdict | E3 all | 15 min + Activity 4 |

---

## Competency map

### Core unit — `CS-ICT251101`, delivering Element 3

**Required knowledge today:** 3.1 *Log and detection management* (reading the Operational log, event IDs), 3.2 *Security solution scan and operations procedure* (the four scan types; update procedure), 3.3 *Knowledge in organization SOP* (the verification worksheet **is** the SOP).

**Required skills today:** **3.6 Verification skills** — this is the only element in the unit that names verification as a skill; it is the whole day. Also computer operation (the commands), analytical (match / mismatch / verdict), interpreting work instructions (the worksheet).

### Basic and common units reprised

| Code | How it appears |
|------|---------------|
| `ICT315202` Apply quality standards | **LO2** — one worksheet is self-checked against the Day 3 class QA checklist (PM Task 6) |
| `400311106` Access and maintain information | Worksheets, patch report and scan logs named and filed in `Evidence/Day_08/` |
| `ICT311203` Perform computer operations | The same PowerShell habits from Day 5, now doing analyst work |

> **Still outstanding — say it:** the **Wazuh SIEM server**, the **Day 1 lab OSH checklist + green pledge**, and the **Day 5 lab-subnet scan**. Add today: **Windows Sandbox / Atomic Red Team** (previewed only).

---

## The idea that anchors the whole day

> **The tool tells a story. The log is the evidence. An analyst does not repeat the story — they verify it.**

Four things must match between the story and the evidence: **time, threat name, file path, action**. And an action is **proven**, never assumed, by three checks:

| Check | Where | Proven if |
|-------|-------|-----------|
| The tool logged the action | Event **1117** in the Operational log | 1117 is there, with `Error Code: 0x00000000` |
| The tool says it succeeded | `Get-MpThreatDetection` → `ActionSuccess` | `True` (and `ThreatStatusID` 2, 3, 4 or 6) |
| The file is actually gone | `Test-Path` on the file | `False` |

If any check fails, the issue is **not contained** — and the Day 7 rule applies: **not contained = threat**, however small. Everything today feeds that one rule.

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. Put the tool's story and the raw log side by side and say, on four points, whether they **match**.
2. **Prove** an action happened — event 1117, `ActionSuccess`, and the file itself — rather than assume it.
3. Read the **signature, engine, platform and OS patch state**, run the update, and report what is behind.
4. Choose the **right scan** — quick, full, custom, offline — and say why; run three of them.
5. Fill a **verification worksheet** end to end and write a **verdict** with a reason.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 7 (we checked the tool works; now check what it said) | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 20 | 3–4 | **Topic 8.1** + **Demo 1** Two stories, one event | Follow-along | 8.1 |
| 8:35 | 20 | 5 | **Activity 1** "Match the Story" | Breakout teams | 8.1 |
| 8:55 | 15 | 6 | **Topic 8.2** + **Demo 2** Did the action really happen? | Follow-along | 8.2 |
| 9:10 | 20 | 7 | **Activity 2** "Prove Your Action" — own EICAR, three ways | Individually, pairs for help | 8.2 |
| 9:30 | 30 | 8 | **Topic 8.3** + **Demo 3** Up to date, or patched | Follow-along | 8.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 20 | 9–10 | **Topic 8.4** + **Demo 4** The four scans; a custom scan live | Follow-along | 8.4 |
| 10:30 | 30 | 11 | **Activity 3** "Update, Then Scan" | Individually, observed | 8.3, 8.4 |
| 11:00 | 15 | 12–13 | **Topic 8.5** + **Demo 5** The worksheet, end to end · Sandbox/Wazuh preview | Follow-along | 8.5 |
| 11:15 | 20 | 14 | **Activity 4** "Which Scan Would You Run?" | Breakout teams | 8.4 |
| 11:35 | 10 | 15 | Afternoon brief · how it is marked · close | Whole class | — |

Morning sums to 225 (8:00 → 11:45). Lecture time is about 85 minutes.

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 30 minutes.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Five verification worksheets — the five paper cases, all eight rows | 40 | 5 worksheets (detection → action → outcome) |
| 2 | Your own EICAR — the worksheet for your own machine, with screenshots | 20 | 1 worksheet + 3 screenshots |
| 3 | Patch-state report for your machine — before/after the update, OS state | 25 | Patch-state report on the SOP template |
| 4 | Scan logs — quick, custom, and a full scan (started and left to run); offline described | 30 | Scan log for 3 types + the offline plan |
| 5 | "Which scan?" — the 7 scenarios, each with a reason | 15 | 7 answers |
| 6 | Self-check one worksheet against the Day 3 QA checklist | 10 | 1 self-check sheet |
| 7 | Reflection | 10 | Three answers |

---

## Before the day
### The night before
- [ ] Run all five demos on your own machine — especially Demo 1 (`Get-WinEvent` on the Operational log must show your Day 6 EICAR events 1116/1117) and Demo 4 (the custom scan)
- [ ] If your Day 6 EICAR is more than a few days old, create it again tonight so the log is fresh
- [ ] Check whether `Update-MpSignature` and `Start-MpScan` need admin on your build; know the GUI route either way
- [ ] Create the folder `Documents\ScanTest` with one harmless `.txt` in it, for the custom scan
- [ ] Take the fallback screenshots in `Day_8_Resources.md`
- [ ] **Do not run the offline scan** — not tonight, not in class. It restarts the machine

### On the morning
- [ ] Breakout rooms; the five cases ready to paste per team
- [ ] Activity Pack, Handout, Resources sent
- [ ] Observation sheet (Resources Part 5) open at 10:30
- [ ] Collect outstanding Day 1–7 evidence in the first fifteen minutes

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 8.1 — TWO STORIES, ONE EVENT
### 8:15–8:55 with Demo 1 and Activity 1 · Slides 3–5 · E3 PC 3.1

### The point
The tool has a friendly view (Protection history) and a raw log (the Operational log). They describe the same event. Beginners learn to put them side by side and check four things match.

### What you must know
- **The story** is the friendly view — Protection history, the popup, or the ticket someone wrote from it. It is a *summary*.
- **The evidence** is the Operational log: event **1116** (detected) and **1117** (action taken), or **1118 / 1119** (action failed). The full path is in Sample Data §2 — the same log the class opened on Day 6.
- **Four points to match:** time · threat name · file path · action. A mismatch on any one is a finding.
- **The log can say more than the story.** Case 4 has two files where the history shows one. Case 5 has a 1116 with no 1117 at all — found, but nothing done.

### Key messages
- The story is a summary written by the tool. The log is what actually happened. Verify, don't repeat.
- Four things: time, name, path, action. Tick them off, every time.
- The log often holds more than the summary — read the lines around your event.

### Mistakes to expect
- Trainees read Protection history and stop. Push: "Now show me the 1117."
- Trainees see a 1116 and call it "handled". A 1116 is only *detected*; the action is the 1117.
- Time confusion — the history rounds to the minute; the log has seconds. A minute's difference is not a mismatch; twenty minutes is.

---

## TOPIC 8.2 — DID THE ACTION REALLY HAPPEN?
### 8:55–9:30 with Demo 2 and Activity 2 · Slides 6–7 · E3 PC 3.2

### The point
Yesterday the class read the action in Protection history. Today they **prove** it, three ways, on their own EICAR.

### What you must know
The three proofs in the box in Part A: **event 1117** · **`ActionSuccess` True** (with a "good" `ThreatStatusID` — 2 cleaned, 3 quarantined, 4 removed, 6 blocked) · **the file is gone** (`Test-Path` False). Then `MpCmdRun.exe -Restore -ListAll` shows what quarantine actually holds — the physical proof.

The action range returns: **Failed · Clean · Delete · Quarantine · Blocked · Re-image.** New today: **re-image**. When none of the others can be trusted — the malware keeps coming back, or the machine was compromised deeply — the answer is to wipe and rebuild. An L1 analyst does not re-image; they **record that clean/delete/quarantine did not hold and recommend it** (Day 9 escalates it).

### Key messages
- An action is proven, not assumed. 1117, `ActionSuccess`, and the file itself.
- A `ThreatStatusID` of 1, or anything over 100, means **not contained** — and not contained is a threat.
- Re-image is the last action on the list because it is the one you use when the others failed.

### Mistakes to expect
- Trainees take "Quarantined" in the history as proof. Ask for the 1117 and the `Test-Path`.
- Trainees confuse "file gone" with "file was never there". The 1116 proves it was there; the `Test-Path` False proves it is gone now. Both are needed.

---

## TOPIC 8.3 — UP TO DATE, OR PATCHED
### 9:30–10:00 with Demo 3 · Slide 8 · E3 PC 3.3

### The point
"Checked and patched as required." Four version numbers, one update to run, and one honest line about what an L1 analyst does and does not patch.

### What you must know
| Layer | Field | What "behind" means |
|-------|-------|---------------------|
| **Signatures** (the list of known threats) | `AntivirusSignatureVersion`, `AntivirusSignatureAge` | Age over 1–2 days — the tool cannot see this week's threats |
| **Engine** (the scanner itself) | `AMEngineVersion` | Months old — new detection methods missing |
| **Platform** (the product) | `AMProductVersion` | Months old — event 2007 warns "will soon be out of date" |
| **Operating system** | `Get-HotFix`, Settings → Windows Update | No security update in over a month — the AV cannot cover an unpatched OS |

**What the trainee patches:** the **signatures** — `Update-MpSignature`, or Windows Security → Protection updates → Check for updates. Read the version before and after. Event **2000** in the log proves it; **2001** means it failed (Machine B in Sample Data §3).

**What the trainee does not patch alone:** the **operating system on a server**. That needs a change window and IT's approval. The L1 job is to *find* that it is four months behind (Machine C) and **report** it. "As required" in the PC means as the SOP requires — and the SOP says report, don't reboot the file server at 9 AM.

### Key messages
- Four layers: signatures, engine, platform, OS. Read all four; most people only ever look at one.
- Run the signature update yourself. Read the number before and after — that is the evidence.
- The OS is patched by IT in a change window. You find it, you report it.

### Mistakes to expect
- Trainees say "up to date" because signatures are today's, without reading the engine or the OS.
- Trainees try to run Windows Update on a "server" in a scenario. Ask who owns the change window.
- `Update-MpSignature` says access denied — use the GUI; same result.

---

## TOPIC 8.4 — SCAN THE SUSPECT MACHINE
### 10:10–11:00 with Demo 4 and Activity 3 · Slides 9–11 · E3 PC 3.4

### The point
Four scan types. Beginners run three of them and learn when each is the right call — and why the fourth is never run in class.

### What you must know
The table in Sample Data §4. The teaching rule: **quick for routine, custom for one place, full when you suspect and don't know where, offline when the machine itself cannot be trusted.**

**The honest point about scans and real-time protection:** on a healthy machine the custom scan of `ScanTest` finds **nothing** — because real-time protection already removed the EICAR the moment it was saved on Day 6. That is not a failed demo; it is the lesson. **A scan is for what real-time protection missed** — files that arrived while it was off (Day 7's Machine 2), a drive that was just plugged in, or something that hides. Say this out loud, before the result appears, so nobody thinks the scan is broken.

**Offline scan:** it restarts the machine into a small scanner that runs before Windows loads, so malware that hides from Windows cannot hide from it. It is the right call for Scenario 4 (malware that comes back). **It is never run live** — show the button, explain, leave it for the afternoon with a warning.

**The scan log:** `MpCmdRun.exe` prints its result in the window and writes `%TEMP%\MpCmdRun.log`; every scan also writes event **1000** (started) and **1001** (finished) — or **1002** (stopped early — which is not a scan).

### Key messages
- Quick for routine, custom for one place, full when you suspect, offline when the machine can't be trusted.
- A scan finding nothing on a healthy machine is normal — real-time protection got there first. Scans are for what it missed.
- A scan that did not finish (1002) is not a scan. Say so in the log.

### Mistakes to expect
- Trainees start a full scan in class and wait for it. Start it, let it run, move on.
- Trainees click the offline scan. **Warn twice** — it restarts the machine, and they lose the session.
- "The custom scan found nothing, so the demo failed." No — explain before, not after.

---

## TOPIC 8.5 — THE VERIFICATION WORKSHEET
### 11:00–11:35 with Demo 5 and Activity 4 · Slides 12–14 · E3 all · knowledge 3.3

### The point
Tie the four PCs into one document — the worksheet in Sample Data §5 — walked end to end on the EICAR case, so the afternoon's five worksheets are not a surprise.

### What you must know
Eight rows: story · evidence · match · proven · outcome · up to date · scan · **verdict**. The verdict is one of four, and the reason is what is marked:

| Verdict | When |
|---------|------|
| **Verified detection** | Match on all four; action proven; contained |
| **Failed action → threat, escalate** | 1118/1119, `ActionSuccess` False, or the file is still there |
| **More than the story → follow up** | The log shows extra files, hosts or times the summary did not |
| **Not yet acted on → act now** | 1116 with no 1117; `ThreatStatusID` 1 |

Then the **two-minute preview**: Windows Sandbox (a throw-away Windows inside Windows for testing suspicious things safely — needs Pro and more RAM than most of the room has) and Wazuh (the same 1116/1117 events arriving on a server for the whole fleet). Screenshots only. "When we have the server, the worksheet does not change — the evidence just arrives in one place."

### Key messages
- The worksheet *is* the SOP. Fill every row; the verdict comes last and carries a reason.
- Four verdicts. Three of them mean the job is not finished.
- Sandbox and Wazuh do not change the method — they change where the evidence comes from.

### Mistakes to expect
- Verdict written before rows 3–4 are filled. Make them fill in order.
- "Verified" on Case 2 because the ticket said so. The ticket is the story; the 1118 is the evidence.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 8 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 5 verification worksheets (detection → action → outcome → verdict) | PM Task 1 + Activity 1 | E3 PC 3.1, 3.2 |
| Own-machine EICAR worksheet with 3 screenshots (1117 · `ActionSuccess` · `Test-Path`) | PM Task 2 + Activity 2 | E3 PC 3.1, 3.2 |
| Patch-state report (signature before/after, engine, platform, OS) | PM Task 3 + Activity 3 | E3 PC 3.3 |
| Scan logs for quick, custom, full; offline scan plan | PM Task 4 + Activity 3 | E3 PC 3.4 |
| 7 "which scan?" answers with reasons | PM Task 5 + Activity 4 | E3 PC 3.4 · knowledge 3.2 |
| 1 worksheet self-check against the class QA checklist | PM Task 6 | `ICT315202` LO2 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

> The plan asks for "scan logs for all four scan types". The **offline** scan restarts the machine and cannot be run inside a live online session; Task 4 asks for its log **only from trainees who choose to run it after class**, and for a written plan (when, why, what to save first) from everyone. Record this in the portfolio note.

## Observation during the live session

**Activity 3 "Update, Then Scan" is observed.** Observation sheet from `Day_8_Resources.md` open at 10:30. Two things:
1. **Did the trainee read the signature version before AND after the update, and record both?**
2. **Did the trainee choose the custom scan for `ScanTest`, run it, and say what the result means (including "nothing found" on a healthy machine)?**

## How the afternoon is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Story and evidence compared on all four points, mismatches named · action proven by evidence (1117 / `ActionSuccess` / file gone), not assumed · all four update layers read, the signature update run and evidenced · scan type chosen with a reason that names what the scan is for · verdicts that follow from rows 3–5 |
| **Not yet competent** | "Verified" because the history said so · a 1116 treated as an action · "up to date" from signatures alone · a full scan "because it's the biggest" · verdict with no reason, or a verdict that contradicts the trainee's own rows |

Full keys in `Day_8_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| No EICAR events in a trainee's log (machine changed, log cleared) | Create the EICAR again (Day 6 steps, 2 minutes); the log refreshes instantly |
| `Get-WinEvent` says access denied on the Operational log | Event Viewer GUI on the same log; if that is also blocked, Protection history + `Get-MpThreatDetection` cover rows 1–4 |
| Third-party AV, not Defender | Its own history and its own log answer the same four questions; pair the trainee with a Defender machine for the commands |
| `Update-MpSignature` / `Start-MpScan` need admin | Windows Security GUI — Protection updates / Scan options. Same evidence |
| Custom scan finds nothing | That is the expected result — teach it (Topic 8.4) |
| Someone starts the offline scan | Their machine restarts; they rejoin in ~20 min. Note it as evidence for Task 4 — and remind the room |
| Activity 3 overruns | Do the update live; the custom scan → PM Task 4 |
| Behind at 11:00 | Cut 8.5 to the worksheet rows + the verdict table; skip the preview; Activity 4 → three scenarios in chat |

---

## End of day checklist
- [ ] Activity 3 observation notes written up
- [ ] Worksheets, patch reports and scan logs chased
- [ ] Outstanding still listed: Wazuh server, Day 1 lab docs, Day 5 lab-subnet scan; Sandbox / Atomic Red Team previewed only
- [ ] Tomorrow announced: **Day 9 — case follow-up and escalation** (tell the client, find the action that failed, and hand it to the right person). Same hours

## What to say at the close
Today the class stopped taking the tool's word for it. They put the story next to the log, proved the action with evidence, found out how far behind the tool and the machine were, and chose the right scan for the right reason. Three of the four verdicts on the worksheet mean the job is not finished — and tomorrow is what happens next: closing the loop with the client, reading the log for the action that failed, and escalating it to the right person with the right pack. Say that, and let them go.
