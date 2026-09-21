# DAY 9 — INSTRUCTOR GUIDE
## Topic: Close the Loop — Tell the Client, Find What Failed, Escalate It
### Cyber Threat Monitoring Level I · Day 09 of 15 · 8 hours

**Mode:** Online synchronous and demonstration-led 8:00 – 11:45 AM · Fully asynchronous 1:00 – 4:00 PM

> **Same two conditions as Days 6–8.** (1) **No SIEM server yet** — failed actions are read from Defender's own log on the trainee's machine and from a paper log extract; the "ticket system" is the spreadsheet register; escalation goes by email. (2) **Total beginners** — assume nothing, every click shown, calm pace.

---

## HOW THIS GUIDE WORKS

The **topic guide** — what Day 9 teaches, why, what you must know, and how it is assessed. Not a script. Keep these open:

| File | For |
|------|-----|
| **`Day_9_Instructor_Guide.md`** | *(this file)* topic, sequence, teaching points |
| **`Day_9_Presenter_Script.md`** | the words, slide by slide (15-slide deck) |
| **`Day_9_Demonstration_Guide.md`** | every demo, click by click |
| **`Day_9_Student_Activity_Pack.docx`** | what the trainees do |
| **`Day_9_Solutions.docx`** | answer keys and marking bands (trainer only) |
| **`Day_9_Student_Handout.docx`** | the trainee's topic reference |
| **`Day_9_Resources.md`** | kit, links, contingency, observation sheet |
| **`Day_9_Sample_Data.md`** | the 2 client cases, the log extract, the 8 situations, the authority matrix, the templates |

---
---

# PART A — WHAT DAY 9 IS

## The one-sentence topic

> **Day 8 ended with three verdicts that mean "the job is not finished". Day 9 finishes it: tell the client what the scan found — honestly — read the scan log for the action that failed, and hand the failure to the right authority with the pack they actually need.**

## Where Day 9 sits

Day 9 delivers all of **Element 4** of the core unit — *Conduct case follow-up*:

| Element / PC | What Day 9 does |
|--------------|-----------------|
| **E4 PC 4.1** Results of the scan are verified to customer / client / stakeholder | Topics 9.1–9.2 — the call, then the written confirmation, for a clean case and a not-clean case |
| **E4 PC 4.2** Security solution scan logs are checked for failed action as per company SOP | Topic 9.3 — five kinds of failure, where each shows, the next step; read on paper and on their own machine |
| **E4 PC 4.3** Failed action is escalated to appropriate authority as per company SOP | Topics 9.4–9.5 — the four authorities, the matrix, and the escalation pack |

After today, Elements 1–4 are done. Day 10 is Element 5 (alert reporting) and the **unit assessment** for `CS-ICT251101`.

## What "no server" changes

The plan used Wazuh alert search and three portable timeline tools (Hayabusa, DeepBlueCLI, EvtxECmd + Timeline Explorer) to find the failed action. With no server, low-spec machines and total beginners:

| Plan's bench (not used today) | Day 9 uses instead |
|-------------------------------|--------------------|
| Wazuh alert search across agents | **`Get-MpThreatDetection` filtered on `ActionSuccess`** + `Get-WinEvent` on 1118 / 1119 / 1002 / 2001, on the endpoint |
| Hayabusa / DeepBlueCLI / Timeline Explorer | **A paper scan-log extract** (Sample Data §2) written as the timeline those tools would produce — eight entries, five failure kinds |
| osTicket + email for the escalation trail | **Spreadsheet register** row updates + a written pack pasted into email |

The timeline tools and Wazuh become a **two-minute preview** in Topic 9.5. The failed-action *taxonomy* and the *pack* are the skills; the tools only change how fast the failures are found.

## The five topics of Day 9

| # | Topic (what the trainee sees) | Competency | Time |
|---|-------------------------------|-----------|------|
| **9.1** | **The Case Is Not Closed Yet** — what follow-up is, and the case lifecycle | E4 · knowledge 4.2 | 15 min |
| **9.2** | **Tell the Client** — the call, then the written confirmation | E4 PC 4.1 | 20 min + Activity 1 |
| **9.3** | **Read the Log for What Failed** — five kinds of failure, and the next step | E4 PC 4.2 | 25 min + Activity 2 |
| **9.4** | **Who Do You Call?** — the four authorities and what each needs | E4 PC 4.3 | 20 min + Activity 3 |
| **9.5** | **The Escalation Pack** — build it, send it, log the trail | E4 PC 4.3 | 20 min + Activity 4 |

---

## Competency map

### Core unit — `CS-ICT251101`, delivering Element 4

**Required knowledge today:** 4.1 *Log and detection management* (the failed-action pass), 4.2 *Knowledge in organization SOP* (the taxonomy and the authority matrix **are** the SOP today).

**Required skills today:** **communication** (the call, the confirmation, the pack — three audiences, three registers), **interpersonal** (a not-clean call to a worried stakeholder), analytical (which failure kind, which authority), interpreting work instructions (the matrix).

### Basic and common units reprised — the heaviest reprise so far

| Code | How it appears |
|------|---------------|
| `400311101` Receive and respond to workplace communication | **LO1 spoken messages** — the verification call, with read-back (Day 1's drill, now with a real result to convey). **LO2 written** — the confirmation and the pack |
| `400311102` Work with others | Escalation *is* working with others — handing the case up with everything the next person needs |
| `ICT315202` Apply quality standards | **LO2** — one pack self-checked against the Day 3 class QA checklist (PM Task 6) |
| `400311106` Access and maintain information | Confirmations, extracts and packs named and filed in `Evidence/Day_09/` |

> **Still outstanding — say it:** the **Wazuh SIEM server**, the **Day 1 lab OSH checklist + green pledge**, the **Day 5 lab-subnet scan**, **Sandbox / Atomic Red Team** (Day 8). Add today: **Hayabusa / DeepBlueCLI / Timeline Explorer** (previewed only).

---

## The idea that anchors the whole day

> **A case is closed when the person outside the desk knows the truth, and the person above the desk has what they need. Not before.**

Two honest sentences run the morning:
- **To the client:** "The scan finished, and the threat is still there." Beginners want to soften it. Don't let them.
- **To the authority:** "Here is what failed, here is the evidence, here is what I need from you, by when." A pack with no ask is a diary entry (Day 7); a pack with no evidence is an opinion; a pack with no deadline will wait.

And the failed-action rule from Day 8, stated once more: **not contained = threat.** A failed action re-opens a closed ticket.

---

## What a trainee can do at 4:00 PM that they could not at 8:00 AM

1. **Call** a client or stakeholder, tell them the scan result plainly — clean or not — and get a read-back.
2. Write the **same-day confirmation** that follows the call, and paste it into the ticket.
3. Read a scan log and name **which of five kinds of failure** each entry is, and the SOP's next step.
4. Choose the **right authority** — IT manager, infosec manager, vendor, CISO — and say why them.
5. Build an **escalation pack** with evidence, an ask and a deadline, and log the trail in the register.

---
---

# PART B — RUNNING THE DAY

## Timetable

### Morning — online synchronous, demonstration-led, 8:00 to 11:45 AM

| Time | Min | Slide | What | Format | Topic |
|------|-----|-------|------|--------|-------|
| 8:00 | 10 | 1 | Welcome · recall Day 8 (three verdicts mean "not finished") | Whole class | — |
| 8:10 | 5 | 2 | Today's five topics | Whole class | — |
| 8:15 | 15 | 3 | **Topic 9.1** The case is not closed yet | Short input | 9.1 |
| 8:30 | 20 | 4 | **Topic 9.2** + **Demo 1** Tell the client — the call, then the confirmation | Demonstration | 9.2 |
| 8:50 | 30 | 5 | **Activity 1** "Make the Call" — V1 and V2 | Breakout pairs, observed | 9.2 |
| 9:20 | 25 | 6–7 | **Topic 9.3** + **Demo 2** Read the log for what failed | Follow-along | 9.3 |
| 9:45 | 15 | 8 | **Activity 2** "Find the Failure" | Breakout teams | 9.3 |
| 10:00 | 10 | — | **BREAK** | | |
| 10:10 | 20 | 9–10 | **Topic 9.4** + **Demo 3** Who do you call? | Short input + worked cases | 9.4 |
| 10:30 | 15 | 11 | **Activity 3** "Who Gets This?" | Breakout teams | 9.4 |
| 10:45 | 20 | 12–13 | **Topic 9.5** + **Demo 4** Build the pack · **Demo 5** preview | Follow-along | 9.5 |
| 11:05 | 30 | 14 | **Activity 4** "Build the Pack" | Individually | 9.5 |
| 11:35 | 10 | 15 | Afternoon brief · how it is marked · close | Whole class | — |

Morning sums to 225 (8:00 → 11:45). Lecture time is about 80 minutes.

### Afternoon — fully asynchronous, 1:00 to 4:00 PM

Seven tasks, about 2 hours 30 minutes.

| # | Task | Min | Evidence |
|---|------|-----|----------|
| 1 | Client verification records — call notes + written confirmation for V1 (clean) and V2 (not clean) | 25 | 2 verification records |
| 2 | Failed-action log extract — annotate all eight entries; then the failed-action pass on your own machine | 30 | Annotated extract + own-machine extract |
| 3 | Three escalation packs — Situations 1, 2 and 5 (one per authority type) | 45 | 3 escalation packs |
| 4 | Escalation trail — update the three register rows (status, escalated to, time, next update due) | 15 | 3 register rows |
| 5 | The failed-action SOP card — five kinds, where each shows, next step | 15 | 1 SOP card |
| 6 | Self-check one pack against the Day 3 QA checklist | 10 | 1 self-check sheet |
| 7 | Reflection | 10 | Three answers |

---

## Before the day
### The night before
- [ ] Rehearse Demo 1 aloud — the V1 call. Decide whether a co-host plays M. Lopez or you read both parts
- [ ] Run the Sample Data §8 commands on your own machine; expect "nothing" — know what that looks like so you can say it
- [ ] Have the log extract (§2) ready to paste, and the eight situations (§4)
- [ ] Prepare the register with the three rows from Days 7–8 (CTM-0007-001 SRV-BAK-02; the WKS-118 and WKS-205 rows) so Demo 4 updates a real row
- [ ] Take the fallback screenshots in `Day_9_Resources.md` — including one Hayabusa timeline and one Wazuh alert search, for the preview

### On the morning
- [ ] Breakout rooms in pairs for Activity 1; teams for 2 and 3
- [ ] Activity Pack, Handout, Resources sent
- [ ] Observation sheet (Resources Part 5) open at 8:50
- [ ] Collect outstanding Day 1–8 evidence in the first fifteen minutes

---
---

# PART C — TEACHING NOTES, TOPIC BY TOPIC

## TOPIC 9.1 — THE CASE IS NOT CLOSED YET
### 8:15–8:30 · 15 minutes · Slide 3 · E4 · knowledge 4.2

### The point
Name what "follow-up" is and where it sits in the lifecycle, so the three skills of the day are seen as one job.

### What you must know
The case lifecycle on our desk: **alert → decide → ticket → check the tool → verify → follow up → escalate or close → report.** Days 6–8 got as far as *verify*. Element 4 is *follow up → escalate or close*. Two people define "closed": the **client / stakeholder** (the person outside the desk who owns the machine, data or service) must know the result; the **appropriate authority** (the person above the desk) must have what they need if anything failed.

The three Day 8 verdicts that land here: *failed action*, *more than the story*, *not yet acted on*. Each one is a follow-up case today.

### Key messages
- A case is closed when the client knows the truth and the authority has what they need. Not before.
- "Verified to the client" is a conversation and a document — both, same day.
- A failed action re-opens a closed ticket.

### Mistakes to expect
- Trainees think "the scan finished" closes the case. Ask: does the owner know? Did anything fail?
- Trainees confuse the client (outside) with the authority (above). Draw the two arrows.

---

## TOPIC 9.2 — TELL THE CLIENT
### 8:30–9:20 with Demo 1 and Activity 1 · Slides 4–5 · E4 PC 4.1

### The point
The verification call, then the written confirmation — for a clean result and a not-clean one. This is where Day 1's spoken-message skill meets a real result.

### What you must know
The **eight-step call** in Sample Data §1: who you are + ticket ID · what was found · what was done + the scan result · what it means for them · what happens next · what you need from them · **read-back** · "in writing within the hour". Then the **written confirmation** (§7), pasted into the ticket.

**Register matters.** M. Lopez (V1) is not technical: no event IDs, no threat names beyond "a malicious program". R. Santos (V2) is technical and worried: give the facts, the times, and the one thing they must not do (restore from backups after 03:40). Both get the truth.

**The not-clean call is the hard one.** Beginners soften: "there might still be something". The sentence is: *"The scan finished, and the threat is still on the server. It is not clean. Here is what happens next."*

### Key messages
- Same facts by voice and in writing, same day. The writing is the record; the call is the courtesy — and the read-back is how you know you were understood.
- Match the register to the person. Truth for both.
- One specific ask per call. "Don't download cracked software" is an ask. "Be careful" is not.

### Mistakes to expect
- No ticket ID at the start. Every call starts with it.
- Softening the bad result. Stop them and have them say the sentence again, plainly.
- Skipping the read-back. That was Day 1's whole drill — remind them.

---

## TOPIC 9.3 — READ THE LOG FOR WHAT FAILED
### 9:20–10:00 with Demo 2 and Activity 2 · Slides 6–8 · E4 PC 4.2

### The point
"Scan logs are checked for failed action as per company SOP." The SOP is the **five-kind taxonomy** in Sample Data §3. Beginners learn to name the kind, because the kind decides the next step.

### What you must know
| Kind | Signature in the log | Next step |
|------|----------------------|-----------|
| 1 Action failed | 1118 / 1119 · `ThreatStatusID` 102–107 · `ActionSuccess False` | Threat → re-open → escalate |
| 2 Action incomplete | 1117 + *Restart required* · history "remediation incomplete" | Get the restart; verify after |
| 3 No action taken | 1116 with nothing after · `ThreatStatusID` 1 / 106 | Threat → scan now → escalate if it stays |
| 4 Scan did not complete | 1002 · no finish time | Doesn't count → re-run → ask who cancelled |
| 5 Threat came back | New 1116 for the same thing after a good 1117 | Offline scan → if again, recommend re-image → escalate |

Plus the **tool** failing — event 2001 repeated — which is found in the same pass and goes to the vendor.

The extract in §2 has eight entries; **A** and **G** are successes, the other six are one kind each (B = 1 *and* 5; C = 4; D = 3; E = 2; F = 1, second attempt; H = tool failure). Demo 2 reads A, B and C aloud; Activity 2 does the rest.

On the trainee's **own machine** the pass finds nothing — and "no failed actions on <host>, checked <time>" is the correct record. Say that before they run it.

### Key messages
- Five kinds. Name the kind, and the SOP tells you the next step.
- A 1116 with nothing after it is a failure. Silence in the log is not good news.
- A scan that did not finish (1002) is not a scan. Re-run it, and find out who stopped it.

### Mistakes to expect
- Trainees only look for the word "failed". Kinds 3 and 4 have no such word — teach the silence and the 1002.
- Kind 5 is missed because the first 1117 looked fine. Read forward in time.
- "Restart required" treated as done. Not clean until the restart and the re-check.

---

## TOPIC 9.4 — WHO DO YOU CALL?
### 10:10–10:45 with Demo 3 and Activity 3 · Slides 9–11 · E4 PC 4.3

### The point
The CS names four "appropriate authorities". The matrix in Sample Data §5 says who gets what. The skill is choosing **the one who can do the thing you need**.

### What you must know
| Authority | Owns | Send them |
|-----------|------|-----------|
| **IT department manager** | Machines, network, change calendar | Isolate, restart, re-image, OS patch, force a user restart |
| **Information security manager** | The security decision | Any uncontained threat, any sign of spread, any decision above your level |
| **Security vendor** | The product | Updates failing, engine faults, **false positives**, a legitimate file quarantined |
| **CISO** | Business risk | **Critical** — ransomware live, data leaving, many hosts; one paragraph, 10-minute SLA, normally via the infosec manager |

Three rules: your **first stop is L2 / shift lead** (Day 3 tiers) — the pack is addressed to the authority, the SOP says who sends it; **one primary authority**, others copied; **Critical goes up fast** and the CISO line is one paragraph.

Demo 3 works Situations 1, 3 and 5 aloud: 1 → infosec manager (uncontained threat; IT manager copied for isolation); 3 → vendor (probable false positive on a business file; infosec manager copied — and *do not restore the file yourself*); 5 → CISO via infosec manager, now (Critical), IT manager for isolation.

### Key messages
- Pick the person who can *do* what you need. That is the whole rule.
- Uncontained → security manager. Machine action → IT manager. Tool broken or wrong → vendor. Business on fire → CISO, now.
- A false positive is a vendor case. You don't "un-quarantine" a business file on your own authority.

### Mistakes to expect
- Everything to the CISO "because it's serious". The CISO gets Critical, in one paragraph.
- Everything to IT "because they fix computers". Ask: is this a machine action or a security decision?
- Trainees restore `payroll_calc.xlsm` themselves. That is above their level and it may be real.

---

## TOPIC 9.5 — THE ESCALATION PACK
### 10:45–11:35 with Demos 4–5 and Activity 4 · Slides 12–14 · E4 PC 4.3

### The point
The 12-field pack in Sample Data §6, filled live for Situation 1, then started by every trainee. This is the document the authority actually reads.

### What you must know
The pack's spine: **To + why them · summary · story · evidence (the extract) · what was tried and what failed (with the kind) · status + severity + SLA · impact · the ask with a deadline · recommendation · attachments · logged in the ticket.** Demo 4 builds it from CTM-0007-001 (SRV-BAK-02) — the ticket the class wrote on Day 7 — so they see one case travel Day 7 → 8 → 9. Then Demo 4 updates the **register row**: status *Escalated*, escalated to, time, next update due. That row is the **trail** — PC 4.3's evidence.

Then the two-minute **preview**: Hayabusa (one command → a CSV timeline of the whole log with the 1118s flagged), Timeline Explorer (reads it), Wazuh (the same failures from every machine, one search). Screenshots. "They find the failures faster. The kinds, the matrix and the pack do not change."

### Key messages
- Evidence, ask, deadline. Without evidence it is an opinion; without an ask it is a diary; without a deadline it waits.
- Log the escalation in the ticket the moment it is sent. The trail is the evidence that you escalated.
- The tools will find failures faster. What you do with them is today's skill.

### Mistakes to expect
- Pack written from the story only — no log lines. Send them back to §2.
- "Please advise" as the ask. Push for the verb: isolate, re-image, open a vendor case, approve a change window — and by when.
- Register row not updated. The pack alone is not the trail.

---
---

# PART D — ASSESSMENT AND EVIDENCE

## What Day 9 produces for each portfolio

| Evidence item | From | Unit / element |
|--------------|------|----------------|
| 2 client verification records — call notes + written confirmation (one clean, one not) | PM Task 1 + Activity 1 | E4 PC 4.1 · `400311101` LO1–LO2 |
| Annotated failed-action log extract (8 entries, kinds named) + own-machine failed-action pass | PM Task 2 + Activity 2 | E4 PC 4.2 |
| 3 escalation packs naming the authority and the justification | PM Task 3 + Activity 4 | E4 PC 4.3 |
| Escalation trail — 3 updated register rows | PM Task 4 | E4 PC 4.3 |
| Failed-action SOP card (5 kinds) | PM Task 5 | knowledge 4.2 |
| 1 pack self-check against the class QA checklist | PM Task 6 | `ICT315202` LO2 |
| Reflection | PM Task 7 | metacognition — not separately assessed |

## Observation during the live session

**Activity 1 "Make the Call" is observed.** Observation sheet from `Day_9_Resources.md` open at 8:50; visit each pair once. Two things, for whoever is playing the analyst on V2 (the not-clean call):
1. **Did they open with the ticket ID and state the result plainly — "not clean, the threat is still there" — without softening it?**
2. **Did they give one specific ask, state what happens next, and get a read-back?**

## How the afternoon is marked

**The reason matters more than the answer.**

| Band | What it looks like |
|------|-------------------|
| **Competent** | Confirmations carry the same facts as the call, in the right register, with an ask · every extract entry named by kind, with the SOP next step · each pack addressed to the authority who can do the thing, with log-line evidence, a verb-ask and a deadline · register rows show the trail |
| **Not yet competent** | A softened not-clean result · failures found only where the word "failed" appears (kinds 3, 4, 5 missed) · packs built from the story with no log lines · "please advise" as the ask · CISO for everything, or IT for everything · packs sent but the ticket never updated |

Full keys in `Day_9_Solutions.docx`.

---

## Contingency

| If this happens | Do this |
|----------------|---------|
| No co-host for Demo 1 | Read both parts; change your voice slightly for M. Lopez; it works |
| Pairs are odd-numbered | A trio: analyst, client, observer — rotate on V2 |
| A trainee's own machine shows a real failed action | Excellent — it becomes their Task 2 extract *and* a live example; have them name the kind |
| `Get-WinEvent` access denied | Protection history: "Action needed" / "Remediation incomplete" / "Failed" are the same kinds in words |
| No email tool for the pack | Paste it into the register row's notes; the pack is the document, the channel is secondary |
| Activity 4 overruns | Fields 1–3 and 9 live; the rest → PM Task 3 |
| Behind at 10:45 | Demo 4 fields 1, 5, 6, 9 only; skip Demo 5 preview; Activity 4 starts in the afternoon |

---

## End of day checklist
- [ ] Activity 1 observation notes written up
- [ ] Verification records, extracts and packs chased
- [ ] Outstanding still listed: Wazuh server, Day 1 lab docs, Day 5 lab-subnet scan, Sandbox / Atomic Red Team; timeline tools previewed only
- [ ] Tomorrow announced: **Day 10 — alert reporting, then the CS-ICT251101 unit assessment.** Tell them what to bring: every Day 6–9 artefact, filed, because the portfolio interview draws on them. Same hours for the morning; the afternoon is the assessment

## What to say at the close
Today the class closed the loop. They told a user the good news and a stakeholder the bad news, both plainly; they read a log and found six failures — including the three that don't say "failed"; they picked the right person for each one and wrote the pack that person needs, with evidence, an ask and a deadline. One case — SRV-BAK-02 — has now travelled from a Day 7 alert to a Day 8 verdict to a Day 9 escalation. Tomorrow it becomes a report, and then the first unit is assessed. Say that, and let them go.
