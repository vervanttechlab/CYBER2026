# DAY 9 — SAMPLE DATA
## The two client cases, the scan-log extract, the escalation situations, the authority matrix, and the templates
### Trainer, and trainees where marked.

> **Safety note.** No live malware, no client data. EICAR remains the only "threat" that touches a real machine. Everything else below is **on paper** — log lines and cases written to look like the real thing. Hostnames, people, threat names and companies are invented. Addresses use documentation-only ranges (`203.0.113.x`, `198.51.100.x`) and the Day 3 Tor node `185.220.101.1`.

> **Continuity.** The cases deliberately continue Days 7–8: **SRV-BAK-02 / Alert G** (the failed quarantine, ticket CTM-0007-001), **WKS-118 / Day 8 Case 2** (the Trojan whose quarantine failed while the file was in use), **SRV-FILE-01 / Day 8 Case 4** (two copies of Emotet) and **WKS-205 / Day 8 Case 5** (found, nothing done). The class already knows these machines.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The two client-verification cases (call + written confirmation) | Demo 1, Activity 1, PM Task 1 |
| 2 · The scan-log extract with failed actions | Demo 2, Activity 2, PM Task 2 |
| 3 · The failed-action taxonomy (our SOP) | Topic 9.3, PM Task 5 |
| 4 · The eight escalation situations | Activity 3, PM Task 3 |
| 5 · The authority matrix (our SOP) | Topic 9.4, Demo 3 |
| 6 · The escalation pack template | Demo 4, Activity 4, PM Task 3 |
| 7 · The written-confirmation template | Demo 1, PM Task 1 |
| 8 · The commands trainees run | Demo 2, PM Task 2 |

---
---

# 1 — THE TWO CLIENT-VERIFICATION CASES
### Demo 1 (the trainer runs V1 live), Activity 1 (pairs run V1 and V2), PM Task 1 (written confirmations for both). Answers and model wording in `Day_9_Solutions.docx`.

**"Verified to the customer / client / stakeholder"** (PC 4.1) means: the person who owns the machine, the data, or the service is **told the scan result, plainly, and what it means for them** — first by voice (the call), then in writing the same day (the confirmation). One case is clean. One is not. Both calls must be honest.

---

**Case V1 — WKS-118, the user M. Lopez — CLEAN**

*Background (from Day 8, Case 2):* the night analyst wrote "quarantined, contained" but the log showed an **1118 — quarantine failed, file in use**. Day 8 verdict: failed action → threat. L2 was called.

*What happened since:*
```
2026-09-17 09:10  L2 ended the running process (setup_crack.exe) and re-ran the quarantine
2026-09-17 09:11  Event 1117  Trojan:Win32/Wacatac.B!ml   Action: Quarantine   Error Code: 0x00000000
2026-09-17 09:12  Get-MpThreatDetection: ActionSuccess True   ThreatStatusID 3
2026-09-17 09:15  Event 1000  Full scan started
2026-09-17 10:48  Event 1001  Full scan finished   (0 threats found)
2026-09-17 10:50  Test-Path C:\Users\mlopez\Downloads\setup_crack.exe  -> False
```

*The person to call:* M. Lopez, the user of WKS-118 (Marketing). Not technical. Was told yesterday not to use the machine.

*What they need to hear:* the ticket ID; that the file was malware; that it has now been quarantined and a **full scan finished clean**; that they may use the machine again; that the file came from a cracked-software download — and the one thing you need from them: **do not download cracked software again, and report anything odd**. Then the written confirmation.

---

**Case V2 — SRV-BAK-02, the stakeholder R. Santos (backup administrator) — NOT CLEAN**

*Background (from Day 7, Alert G — ticket CTM-0007-001):* Defender detected `Trojan.Agent.XZ` in `svhost32.exe` at 03:40; **quarantine failed, file in use**. Decision: threat, Critical. Ask: L2 to isolate and identify the process holding the file.

*What happened since:*
```
2026-09-17 08:20  L2 attempted to end the process; it restarted itself within 4 seconds
2026-09-17 08:22  Event 1118  Trojan.Agent.XZ   Action: Quarantine   Error: The file is in use by another process
2026-09-17 08:25  Event 1000  Full scan started
2026-09-17 09:58  Event 1001  Full scan finished   (1 threat found: Trojan.Agent.XZ, C:\Windows\Temp\svhost32.exe)
2026-09-17 09:59  Get-MpThreatDetection: ActionSuccess False   ThreatStatusID 102
2026-09-17 10:00  Test-Path C:\Windows\Temp\svhost32.exe  -> True
```

*The person to call:* R. Santos, who runs the backup system. Technical, busy, and worried about whether last night's backups are safe.

*What they need to hear:* the ticket ID; that the scan **finished and the threat is still there**; that two quarantine attempts have failed because something keeps the file running; that the server is **not clean and not contained**; that it is being escalated now (Topic 9.4 — to whom); what that means for them (do not restore from backups taken after 03:40 until told; expect the server to be isolated); and what you need from them: **when were the last backups taken, and can the server be taken off the network now?** Then the written confirmation — the same facts, in writing, same day.

---

**The shape of the call (from Day 1 — routine spoken messages, and read-back):**

1. Who you are, which desk, and the **ticket ID**
2. **What was found**, in one plain sentence
3. **What was done**, and **what the scan showed** — the honest result, even when it is bad
4. **What it means for them** — can they use it / restore from it / must they stop
5. **What happens next**, and by when
6. **What you need from them** — one specific ask
7. **Read-back** — "Can you tell me back what you'll do, so I know I said it clearly?"
8. "I'll send this to you in writing within the hour."

---
---

# 2 — THE SCAN-LOG EXTRACT WITH FAILED ACTIONS
### Demo 2 walks the first three lines. Activity 2: teams find every failed action and name its kind. PM Task 2: the full annotated extract. All on **2026-09-17**.

The extract is what an analyst would assemble from three places on one machine — the Operational log, `Get-MpThreatDetection`, and `MpCmdRun.log`. **Eight entries. Not all are failures.**

```
[A] 02:14:06  Event 1116  Detected  Trojan:Win32/Emotet.A   file:_C:\Temp\inv0ice.doc.exe             SRV-FILE-01
    02:14:07  Event 1117  Action: Quarantine   Error Code: 0x00000000

[B] 02:17:52  Event 1116  Detected  Trojan:Win32/Emotet.A   file:_C:\Users\Public\inv0ice.doc.exe     SRV-FILE-01
    02:17:53  Event 1118  Action: Quarantine   FAILED   Error: The file is in use by another process
    02:17:58  Event 1116  Detected  Trojan:Win32/Emotet.A   file:_C:\Users\Public\inv0ice.doc.exe     SRV-FILE-01

[C] 03:05:00  Event 1000  Full scan started                                                             SRV-FILE-01
    03:41:19  Event 1002  Scan stopped before completion   (Reason: user cancelled)

[D] 06:30:11  Event 1116  Detected  TrojanDownloader:O97M/Emotet   file:_C:\Users\jreyes\AppData\Local\Temp\update_helper.exe   WKS-205
    (no 1117 / 1118 follows)
    Get-MpThreatDetection:  ActionSuccess False   ThreatStatusID 1

[E] 07:12:40  Event 1116  Detected  Trojan:Win32/Wacatac.B!ml   file:_C:\Users\aramos\Downloads\photo_viewer.exe   WKS-140
    07:12:41  Event 1117  Action: Remove   Error Code: 0x00000000
              Additional actions: Restart required
    Protection history:  "Action needed — remediation incomplete. Restart your device."

[F] 08:22:03  Event 1118  Action: Quarantine   FAILED   Error: The file is in use by another process    SRV-BAK-02
              Threat: Trojan.Agent.XZ   file:_C:\Windows\Temp\svhost32.exe
    Get-MpThreatDetection:  ActionSuccess False   ThreatStatusID 102   (2nd attempt; 1st was 2026-09-15 03:40)

[G] 09:15:00  Event 1000  Full scan started                                                             WKS-118
    10:48:33  Event 1001  Full scan finished   (0 threats)

[H] 11:02:15  Event 2001  Signature update FAILED   Error: 0x80072EE2 (the operation timed out)         TRN-PC-11
    MpCmdRun.log:  "Update failed ... Signature update attempts: 21 consecutive failures since 2026-08-27"
```

---
---

# 3 — THE FAILED-ACTION TAXONOMY (OUR SOP)
### Topic 9.3 and PM Task 5. "Checked for failed action as per company SOP" — this is the SOP: five kinds, where each shows, and the next step.

| Kind | What it means | Where you see it | Next step per SOP |
|------|---------------|------------------|-------------------|
| **1 · Action failed** | The tool tried to quarantine / remove / clean / block and could not | Event **1118 / 1119**; `ThreatStatusID` **102 / 103 / 104 / 107**; `ActionSuccess False` | Not contained → **threat**. Re-open the ticket if closed. Escalate (Topic 9.4) |
| **2 · Action incomplete** | The tool acted, but the job is not finished until something else happens — usually a **restart** | Event 1117 with *Additional actions: Restart required*; Protection history *remediation incomplete* | Get the restart done (user or IT). Verify after the restart (Day 8 three proofs). Not clean until then |
| **3 · No action taken** | Detected, and then nothing | Event 1116 with **no 1117/1118 after it**; `ThreatStatusID` **1** (or **106** abandoned) | Not contained → **threat**. Act now: run the scan; if it still does nothing, escalate |
| **4 · Scan did not complete** | The scan stopped before the end — cancelled, crashed, machine went to sleep | Event **1002**; scan history shows no finish time | The scan does not count. Re-run it; find out who cancelled it and why |
| **5 · Threat came back** | Action succeeded, then the same threat is detected again on the same machine | A new 1116 for the same file/name **after** a good 1117 | Something is re-creating it. Offline scan (Day 8); if it returns again, **recommend re-image**. Escalate |

> **Also a failure of the *tool*, not the action** — the signature update failing (event **2001**, repeated). It is not a scan failure, but it is checked in the same pass and it goes to the vendor (Topic 9.4).

---
---

# 4 — THE EIGHT ESCALATION SITUATIONS
### Activity 3 (teams: which authority, and why) and PM Task 3 (three of them become full packs). Answers in `Day_9_Solutions.docx`.

1. **SRV-BAK-02** — `Trojan.Agent.XZ`, quarantine failed **twice**, the process restarts itself, full scan confirms it is still there. Backup server. Not contained.
2. **40 training-room PCs** — signature updates have been **failing daily for three weeks** (event 2001 × 21). The tool is three weeks blind on every one of them.
3. **FIN-WKS-03** — Defender quarantined `payroll_calc.xlsm`, the macro workbook the payroll team runs every month-end. Payroll is tomorrow. The file has been used safely for two years.
4. **SRV-FILE-01** — the operating system has had **no security update for four months** (Day 8, Machine C). The antivirus itself is current.
5. **SRV-FIN-02** — files renaming to `.locked` **right now**, ransom note in every folder, Finance cannot work, and it is spreading to a second share.
6. **WKS-140** — Trojan removed, but **restart required** and the user says they cannot restart until Friday because of a deadline.
7. **SRV-FILE-01** — Emotet found in **two locations** three minutes apart (Day 8 Case 4). Both quarantined. But two copies means it moved.
8. **WKS-205** — Wacatac quarantined, then **came back after every restart**, three times. Offline scan found and removed it; it came back again.

---
---

# 5 — THE AUTHORITY MATRIX (OUR SOP)
### Topic 9.4, Demo 3. The CS names four "appropriate authorities". This is who gets what, on our desk.

| Authority | Send them | Because they own | They need from you |
|-----------|-----------|------------------|--------------------|
| **IT department manager** | Anything needing an **IT action or IT resources**: isolate a host, restart or re-image a machine, patch an operating system, force a user's restart, a change window | The machines, the network, the change calendar | The host, what must be done, by when, and what happens if it is not |
| **Information security manager** | Any **confirmed threat that is not contained**, any sign of **spread**, any security **decision** above your level (isolate now or wait? notify the client?) | The security decision and the response | The evidence (log extract), what was tried, current status, severity, your recommendation |
| **Security solution / security vendor** | The **tool itself is failing**: updates failing across machines, the engine crashing, a suspected **false positive** on a business file, a legitimate file quarantined | The product | The versions, the exact detection name and file hash, the log lines, how many machines |
| **Chief information security officer (CISO)** | **Critical** business impact: active ransomware, data leaving, many hosts, anything regulatory or that the executive must know **now** — normally *through* the information security manager, but the SOP says notify **within 10 minutes** for Critical | The business risk | One paragraph: what, since when, how many, what is being done, what decision is needed |

**Three rules the trainee applies:**
1. **Your first stop is your L2 / shift lead** (the tiers from Day 3). The escalation *pack* is addressed to the authority; the SOP says whether L2 sends it or you do. Today, you write it — that is the skill.
2. **One primary authority per escalation.** Others are copied. Pick the one who can *do* the thing you need.
3. **Critical goes up fast** — the 10-minute SLA from Day 7 — and the CISO line is one paragraph, not the whole pack.

---
---

# 6 — THE ESCALATION PACK TEMPLATE
### Demo 4 fills it live for Situation 1. Activity 4 starts one; PM Task 3 finishes three.

| # | Field | Your entry |
|---|-------|------------|
| 1 | **To** — the authority, **and why them** (what they own that you need) | |
| 2 | **From / date / time / ticket ID** | |
| 3 | **One-line summary** — host · what · current status | |
| 4 | **What was detected** — the story (name, file, time), in the tool's words | |
| 5 | **What the evidence shows** — the log lines (event IDs, `ThreatStatusID`), attached as an extract | |
| 6 | **What was tried, and what failed** — each attempt, with the **failure kind** (§3) | |
| 7 | **Current status** — contained / not contained · severity band · SLA clock (raised at, due by) | |
| 8 | **Impact** — who and what is affected, or would be | |
| 9 | **What I need from you** — one specific ask, with a **deadline** | |
| 10 | **My recommendation** — one line (isolate / re-image / vendor case / change window) | |
| 11 | **Attachments** — verification worksheet · log extract · screenshots | |
| 12 | **Escalation logged** — ticket updated at (time), copied to | |

> A pack with no ask is a diary entry (Day 7). A pack with no evidence is an opinion. A pack with no deadline will wait.

---
---

# 7 — THE WRITTEN-CONFIRMATION TEMPLATE
### PC 4.1 — the second half of "verified to the client". Sent the same day as the call; pasted into the ticket.

```
To:       <client / stakeholder>
Subject:  <Ticket ID> — <host> — scan result: CLEAN / NOT CLEAN
Date:     <date, time>

Hello <name>,

As discussed by phone at <time>:

1. What was found:     <threat name>, in <file>, on <date/time>.
2. What was done:      <quarantined / removed / attempts failed>.
3. Scan result:        Full scan finished <date/time> — <0 threats / 1 threat still present>.
4. What this means:    <you may use the machine again / do not restore from backups after 03:40 / the server will be isolated>.
5. What happens next:  <closed / escalated to <authority> at <time>; next update by <time>>.
6. What we need from you:  <one specific ask>.

Please reply to confirm you have received this.

<Your name>, L1 analyst, <desk>   ·   Ticket <ID>
```

---
---

# 8 — THE COMMANDS TRAINEES RUN
### PM Task 2 — the failed-action pass on their own machine. Nothing here needs the internet. Their own machine will (almost certainly) show no failures; the result "no failed actions found on <host>" is itself the record.

```powershell
# 1. Any detection whose action did not succeed?
Get-MpThreatDetection | Where-Object { -not $_.ActionSuccess } |
  Select-Object InitialDetectionTime, Resources, ActionSuccess, ThreatStatusID

# 2. Any failed-action or stopped-scan events in the log?
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 200 |
  Where-Object { $_.Id -in 1118, 1119, 1002, 2001 } |
  Select-Object TimeCreated, Id, Message | Format-List

# 3. Any threat still active?
Get-MpThreat | Select-Object ThreatName, IsActive

# 4. When did the last scans actually finish?
Get-MpComputerStatus | Select-Object QuickScanEndTime, FullScanEndTime, QuickScanAge, FullScanAge
```

*GUI: Windows Security → Virus & threat protection → Protection history — look for **"Action needed"**, **"Remediation incomplete"**, or **"Failed"**.*

> **Preview only today (not run):** **Hayabusa** turns the whole event log into one CSV timeline with the failed actions flagged; **DeepBlueCLI** does the same in PowerShell; **Timeline Explorer** reads that CSV; **Wazuh** shows the 1118s from every machine in one search. They arrive with the on-site lab and the server. The commands above do the same job for one machine.
