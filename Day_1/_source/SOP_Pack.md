# SOP PACK
## The Written Procedures That Run This Desk
### SOP = **Standard Operating Procedure** — a written instruction for how a job is done, the same way, every time
### Cyber Threat Monitoring Level I — issued Day 1, used every day

---

> **Keep this pack.** You will use it on Day 1, again on Days 6 to 10 when you triage real
> alerts, and again on Day 15 in the assessment. Bring it to every session. Mark it up —
> a clean SOP is one nobody has read.

---

# DOCUMENT 1 — ALERT INTAKE SOP
### `SOP-SOC-001` · revision 4 · owner: SOC Manager · review: annually

## 1. Purpose
This procedure defines how a Level 1 analyst receives, records, assesses and escalates a
detection alert or incident report.

## 2. Scope
Applies to all Level 1 analysts on all shifts, for all monitored clients.

## 3. Procedure

**3.1** On receipt of a detection alert, the analyst **SHALL** record the alert ID, source
system, timestamp, and affected host within **5 minutes** of receipt.

**3.2** The analyst **SHALL** assess the alert against the Severity Matrix (`SOP-SOC-002`)
before any other action.

**3.3** Where the alert is assessed as **Critical** or **High**, the analyst **MUST** notify
the client contact within **15 minutes of assessment**.

**3.4** The analyst **SHOULD** check for a matching Change Notice before escalating. Where a
Change Notice explains the alert, the analyst **SHALL** record the change reference and close
the alert as expected activity.

**3.5** The analyst **MAY** close an alert assessed as **Low** without escalation, provided
the assessment is documented.

**3.6** The analyst **SHALL NOT** take containment action on any host. Containment is
authorised by the SOC Manager only.

**3.7** The analyst **SHALL** record every action taken, with the time it was taken and the
name of anyone who authorised it.

**3.8** At end of shift the analyst **SHALL** complete a handover log covering open items,
escalated items, watch items, system status, and client notes.

## 4. Records
All actions are recorded in the ticket system. Handover logs are retained for 12 months.

---

# DOCUMENT 2 — SEVERITY MATRIX
### `SOP-SOC-002` · revision 2

Assess **impact** and **certainty** together. Where two levels could apply, **choose the
higher one** and note why.

| Severity | What it means | Examples | Notify client | Escalate to |
|----------|--------------|----------|--------------|-------------|
| **CRITICAL** | Active harm happening now, or imminent | Ransomware encrypting files · confirmed C2 traffic · active data exfiltration · domain admin compromise | **Immediately**, within 10 min of assessment | L2 **and** SOC Manager, immediately |
| **HIGH** | Confirmed malicious activity, contained or not yet spreading | Malware that failed to clean · credential dumping tool detected · successful logon after many failures · DLP block on sensitive data | Within 15 min of assessment | L2 |
| **MEDIUM** | Suspicious, needs verification, no confirmed harm | Adware · blocked exploit attempt · unusual process on one host · unexpected agent offline | Within 4 hours | L2 if unresolved at end of shift |
| **LOW** | Routine, expected, or already handled by the tool | Blocked port scan from the internet · quarantined test file · policy violation with no data at risk | End of shift summary | None — L1 may close with documentation |

### Rules that override the table

1. **Anything on a domain controller, backup server, or finance system is raised one level.**
2. **Anything a client reports by phone is treated as at least Medium** until assessed —
   a human bothered to call.
3. **If you cannot decide between two levels, take the higher one and write down why.**
   Nobody has ever been disciplined for over-assessing with a documented reason.
4. **Uncertainty is not Low.** "I don't know what this is" is Medium at minimum.

---

# DOCUMENT 3 — ESCALATION MATRIX
### `SOP-SOC-003` · revision 3

| Severity | Contact | Method | Within | If no answer |
|----------|---------|--------|--------|-------------|
| **CRITICAL** | L2 on shift, **then** SOC Manager | Phone, then ticket | Immediately | Call the next name on the on-call list. Keep calling. Never leave a Critical unowned |
| **HIGH** | L2 on shift | Ticket, then chat | 15 min | Escalate to SOC Manager after 30 min with no response |
| **MEDIUM** | L2 on shift | Ticket | End of shift | Carry it in the handover |
| **LOW** | None | Ticket only | — | — |

### Who is who

| Role | When you contact them |
|------|----------------------|
| **L2 Analyst** | Your first escalation for anything above Low |
| **SOC Manager** | Critical incidents · containment decisions · client disputes · anything you were asked to do that you believe you should not |
| **IT Department Manager** | Systems the client's own IT team must act on — patching, account lockouts, server access |
| **Information Security Manager** | Policy breaches, insider concerns, anything involving staff conduct |
| **Security solution vendor** | The tool itself is failing — not detecting, not updating, console down |
| **Chief Information Security Officer** | Only through the SOC Manager. An L1 never contacts the CISO directly |

### The escalation pack — what you hand over
Every escalation, no exceptions, includes all six:

1. **Ticket number**
2. **What was detected** — the alert, in one sentence
3. **Affected host(s) and user(s)** — exact names, spelled out
4. **What you have already checked** — including whether a Change Notice covers it
5. **Your severity assessment, and why**
6. **What you are asking for** — a decision, an action, or just awareness

> An escalation without item 6 is a complaint, not an escalation.

---

# DOCUMENT 4 — SAMPLE VENDOR ADVISORY

```
ADVISORY 2026-0418 — Endpoint Agent 7.4.2 Signature Regression
Issued: 2026-04-18 09:00   Severity: Informational

A signature regression in Endpoint Agent 7.4.2 may cause false positive
detections identified as "Trojan.Generic.Heur" on signed Microsoft
binaries, including powershell.exe and wmiprvse.exe.

Affected versions: 7.4.2 only.
Not affected:      7.4.1 and earlier, 7.4.3 and later.
Fixed in:          7.4.3, released 2026-04-19.

Recommended action: update to 7.4.3. Until updated, treat
Trojan.Generic.Heur detections on signed Microsoft binaries as
suspected false positives and verify manually before escalating.

This advisory does not apply to detections on unsigned binaries or on
binaries outside the Windows system directories.
```

---

# DOCUMENT 5 — SAMPLE CHANGE NOTICE

```
CHANGE NOTICE CHG-2026-1177
Raised: 2026-04-19    Approved: Change Advisory Board, 2026-04-20

System:     Manila file server cluster
            SRV-MNL-01, SRV-MNL-02, SRV-MNL-03, SRV-MNL-04
Window:     2026-04-22, 22:00 – 03:00
Change:     Quarterly operating system patching and reboot cycle
Impact:     Hosts will reboot. Monitoring agents will report offline
            during reboot. Elevated process creation and service
            restart activity is expected throughout the window.
Requester:  IT Infrastructure
Approver:   Change Advisory Board
Back-out:   Snapshot restore, 45 minutes per host
```

---

# DOCUMENT 6 — SAMPLE CLIENT SLA NOTICE
> **SLA = Service Level Agreement** — the contract term that says how fast you must respond to a client.

```
INTERNAL NOTICE — Client SLA Change, Northwind Trading
Issued: 2026-04-21   Effective: immediately

Northwind Trading has moved to an enhanced service level:

  Critical alerts : client notified within 10 minutes of assessment
  High alerts     : client notified within 30 minutes of assessment
  Method          : phone to the on-call number, followed by email
  Named contact   : Ms. R. Aguilar, IT Manager (on-call 24/7)

This supersedes the standard notification timings in SOP-SOC-001
section 3.3 FOR THIS CLIENT ONLY. All other clients are unchanged.
```

---

## HOW TO READ ANY OF THESE — the verbs

| Word | What it means for you |
|------|----------------------|
| **shall** / **must** | Mandatory. You have no discretion. |
| **should** | Expected. If you deviate you must be able to justify it. |
| **may** | Your judgement — usually conditional on documenting it. |
| **shall not** | You have no authority. This is the edge of your role. |
| **within X minutes** | A clock is running. Know exactly **when it starts**. |

> The most commonly missed detail in this pack: the 15-minute clock in SOP-SOC-001 §3.3
> starts at **assessment**, not at receipt. Read it again.

---

*Issued to: _________________________  Date: _____________*
