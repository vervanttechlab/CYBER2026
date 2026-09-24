# DAY 10 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 10 for the first time, to complete beginners

---

## READ THIS FIRST

This guide assumes nothing. **No server:** the evidence is the paper set in Sample Data §3, ingress and egress come from your own machine, and ATT&CK Navigator runs in the browser. **Total beginners:** show every click and go at a calm pace. **The afternoon is the unit assessment.** Nothing in this guide is used after 11:45. The assessment has its own file.

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic)* | A note for you. Never read it aloud |
| **What you will see** | What should appear |

**Five demonstrations:**

| # | Demonstration | When | Topic |
|---|--------------|------|-------|
| **1** | Tell them in ten minutes: the N1 Critical notification, then the written version | 8:15 | 10.1 |
| **2** | Where did it go? The hosts table and the path, from the evidence | 8:55 | 10.2 |
| **3** | What came in, what went out: your own machine, then the firewall lines | 9:40 | 10.3 |
| **4** | Name it, map it: exploitation, installation, and ATT&CK Navigator (B1–B3) | 10:10 | 10.4 |
| **5** | Preview: Wazuh ATT&CK module, Atomic Red Team, Hayabusa | 10:55 | 10.5 |

The screen setup is the same as Days 5–9: clean desktop, large text, notifications off. Narrate, and slow down. **Have open before 8:00:** PowerShell (a normal window), a browser tab on `https://mitre-attack.github.io/attack-navigator/`, a second tab on `https://attack.mitre.org`, the evidence set (Sample Data §3) ready to paste, and the ticket register at the SRV-BAK-02 row.

---
---

# DEMONSTRATION 1 — TELL THEM IN TEN MINUTES
### 8:15 AM · Slide 3 · Topic 10.1 · E5 PC 5.1

## Why this exists
Beginners hear a **Critical notification** done properly: fast, plain, with a "do / do not" and one ask. Then they watch the same facts become the written version. It is the third kind of message this week, and they need to hear how it differs from Day 9's verification call and escalation pack.

## What you need
- Sample Data §1 (what happened after Day 9) and §2 (N1) on your second screen
- A co-host to play **R. Santos**, the backup administrator *(or read both parts)*
- The written-notification template (Sample Data §5) open in a document
- Camera on. This is a role-play, not a screen

## The steps
**1. Read §1 aloud, slowly, and stop on 11:29.**
> "Yesterday at 10:52 we escalated SRV-BAK-02 to the security manager. At 11:18 he approved isolation. At 11:26 IT disabled the switch port. And at 11:29, L2 said this: the firewall log shows one point eight gigabytes LEFT that server on the 15th, between 04:10 and 04:52, to 185.220.101.1. That's the same address WKS-311 was talking to on Day 3."

> "On Day 6's severity matrix, 'data leaving' is Critical. And Critical means notify within ten minutes. It's 11:29. The clock started. Who owns SRV-BAK-02? R. Santos. I'm calling now, before I know everything."

**2. Say the difference, in one breath.**
> "Yesterday I called a client to tell them a scan result. That was verification. I sent a pack up to an authority to get a decision. That was escalation. This is a third thing: a notification. I'm warning the owner, so they can protect what's theirs. Fast beats complete."

**3. Make the call** *(camera on. You read the analyst; the co-host reads Santos):*
> "Mr Santos, this is Chester from the security desk, ticket CTM-0007-001."
> "This is a Critical security notification about SRV-BAK-02."
> "What we know: about one point eight gigabytes left the server early on the 15th, between 4:10 and 4:52 in the morning, to an outside address used for hiding traffic. Just before that, the finance backup file from the 14th was read."
> "What's been done: the server was taken off the network at 11:26, and the svc_backup password was reset at 11:45."
> "What you must NOT do: please don't reconnect SRV-BAK-02, don't use the svc_backup account anywhere, and don't restore from any backup taken after 4:51 PM on the 14th until we clear it."
> "One thing I need from you: which backup sets were on the D drive on the 15th? That tells us what may have left. Can you send me that by 1 PM?"
> "I'll update you by 2 PM. Can you tell me back what you'll do and not do?"

*(Santos reads back: not reconnect, not use svc_backup, not restore after 14 Sep 16:51, send the list of backup sets by 1 PM.)*

> "That's right. I'll send this in writing within the hour. Thank you."

**4. Debrief: count the seven lines.**
> "Seven lines. Who I am and the ticket. 'Critical' and what system. What's known, and since when. What's been done. What NOT to do. One ask, with a time. Next update, and a read-back. Did I mention an event ID? A hash? No. He needs the what, the since-when, and what not to touch."

**5. Write the notification** *(fill Sample Data §5 on screen, thinking aloud):*
> "Subject: [CRITICAL] Security notification, CTM-0007-001, SRV-BAK-02. Line 1: Critical, because data left the server. Line 4, what you must do: the three 'do nots'. And look at this last sentence: 'based on what is known at 11:31. It will be updated.' That sentence is what lets me send it fast. I'm not pretending it's the whole story."

**6. The one you do NOT call.**
> "SRV-FILE-01. Twelve failed logons from WKS-311, and no success. An attempt that failed is Medium on our matrix. The standard says high and critical are notified. So SRV-FILE-01 goes in the report, and I don't phone its owner in a panic. If you notify everyone about everything, people stop listening."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "What is the difference between a notification and an escalation?" | Notification warns the **owner** of a High / Critical threat. Escalation hands a **failure** to an authority for action |
| "What line makes a notification more than news?" | The do / do not |
| "Why don't we notify SRV-FILE-01's owner?" | An attempt that failed is Medium. Only High and Critical are notified |

## Common problems
| Problem | Fix |
|---------|-----|
| No co-host | Read both parts |
| Trainees ask "should we wait until we know what was in the 1.8 GB?" | No. Fast beats complete. Say what is known and when you will update |
| Trainees ask who notifies the CISO | The security manager, through the Day 9 escalation. The analyst's notification goes to the **owner** |

---
---

# DEMONSTRATION 2 — WHERE DID IT GO?
### 8:55 AM · Slide 5 · Topic 10.2 · E5 PC 5.2

## Why this exists
Trainees learn to place every host in one of four words (**origin, confirmed, attempted, not linked**), and to write the lateral-movement path as *from, to, method, account, time, line*. The SRV-FIN-02 trap teaches the day's anchor: **link with evidence, not with the clock**.

## What you need
- The evidence set (Sample Data §3) on screen, large font
- A blank document with two tables: **Hosts** (host · role · involvement · line) and **Path** (from · to · method · account · time · line)

## The steps
**1. Put the four words on screen.**
> "Every host in an incident gets one of four words. ORIGIN: where it started inside. CONFIRMED: evidence it's there. ATTEMPTED: they tried, and the log shows it failed. NOT LINKED: we suspected it, we checked, and nothing joins it. Every word needs a line number."

**2. WKS-311: origin.**
> "E02: on the 14th at 16:51, PowerShell starts, and its parent is WINWORD. Word started PowerShell. It downloads a file and saves it as svhost32.exe in Public. E05: a scheduled task to run it at every logon. That's where it began inside our network. Origin, with lines E02 to E05."

**3. SRV-BAK-02: confirmed. Build the path live.**
> "Now read with me: E07. Thirty-eight failed logons on SRV-BAK-02, account svc_backup, source 192.168.10.31. Whose address is .31? WKS-311. E08: logon type 3, success, same account, same source. Type 3 means over the network. E10: that account writes svhost32.exe into the ADMIN$ share, into the Temp folder. E11: a service is installed to run it."

*(Fill the Path row as you speak: WKS-311 → SRV-BAK-02 · SMB to ADMIN$ · svc_backup (after 38 guessed passwords) · 15 Sep 03:33–03:39 · E07, E08, E10, E11.)*

> "From, to, method, account, time, line. That's lateral movement: from one inside machine to another."

**4. The strongest line: E16.**
> "And E16: the same file hash on both machines. Not a similar name. The same file. That's the line that joins them beyond argument."

**5. SRV-FILE-01: attempted.**
> "E09: twelve failed logons from .31 to SRV-FILE-01, and then? Nothing. No 4624. They tried, and they failed. It's not infected. It's ATTEMPTED. And that's a finding: it tells the report where they tried to go."

**6. SRV-FIN-02: the trap.**
> "SRV-FIN-02. Encrypted at 03:40 on the 15th, the same minute the quarantine failed on SRV-BAK-02. Same case?" *(Let them answer. Most will say yes.)*
> "Read E17. The logon was type 10, remote desktop, from the VPN, as fin_admin. Not from .31. The file was lck.exe, not svhost32. No connection to 185.220.101.1. Which line joins it to our case?" *(Pause.)* "None. So it's NOT LINKED, a separate case, and the report says why. Link with evidence, not with the clock."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Why is E08 lateral movement and not an attack from outside?" | The source `192.168.10.31` is an inside address |
| "Is SRV-FILE-01 infected?" | No. Attempted: failed logons and no success |
| "What is the strongest link between WKS-311 and SRV-BAK-02?" | E16, the same hash |

## Common problems
| Problem | Fix |
|---------|-----|
| The class insists SRV-FIN-02 is linked | Ask for the line. There is none. Offer: "What would change your mind?" A logon from .31, or the same hash |
| Logon types confuse them | Only two today: type 3 = network (shares), type 10 = remote desktop |

---
---

# DEMONSTRATION 3 — WHAT CAME IN, WHAT WENT OUT
### 9:40 AM · Slides 7–8 · Topic 10.3 · E5 PC 5.3

## Why this exists
Direction is decided by **who started it**, and seriousness by **how many bytes**. Trainees see it first on their own machine, where everything is normal, and then on the evidence, where one line is 1.8 GB.

## What you need
- PowerShell open (normal window)
- Sample Data §7 commands ready to paste
- Evidence lines E01, E03, E06, E13, E14, E18 highlighted

## The steps
**1. Say what you expect first.**
> "I'm going to ask my own machine what it's connected to right now. You'll see lots of connections to port 443. That's normal: the browser, Teams, updates. We're learning to read direction, not hunting for something bad. Follow along on yours."

**2. Egress: what my machine started.**
```powershell
Get-NetTCPConnection -State Established |
  Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess |
  Sort-Object RemotePort | Format-Table -AutoSize
```
**What you will see:** a table, often 10–40 rows. Most have **RemotePort 443**, and **LocalPort** is a high number (49152 or more).
> "Look at one row. My port is high, 51 thousand something. The remote port is 443. High number on my side means I'm the client. I started it. That's egress: going out."

**3. Name the owner of one line.** *(Pick a row and put its OwningProcess number in the command.)*
```powershell
Get-Process -Id 1234 | Select-Object Id, ProcessName, Path
```
> "That's msedge, my browser. Good. On WKS-311 the same command would have said svhost32, from C:\Users\Public. Same command, different answer."

**4. Ingress: the doors that are open.**
```powershell
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Sort-Object LocalPort | Format-Table -AutoSize
```
> "Listen means waiting for someone to come IN. 135, 445: Windows' own services. If the LocalAddress is 127.0.0.1, only my own machine can reach it. If it's 0.0.0.0, other machines could try, and that's why the firewall is there. A listening port is a door, not a visitor."

**5. How much, in total?**
```powershell
Get-NetAdapterStatistics | Select-Object Name, ReceivedBytes, SentBytes
```
> "Received is much bigger than sent. That's normal for a person who browses: we download more than we upload. Remember the shape. Now look at a server that sent far more than it received."

**6. Now the evidence: read three lines.**
> "E03: OUT from .31 to 203.0.113.45 port 80, bytes IN 1.2 million. The connection went OUT, but what came IN? A file, one point two megabytes: the malware itself. That's ingress of a tool, carried on an outbound connection."
> "E06 and E13: out to 185.220.101.1 on 443, every five minutes, about two kilobytes each. Small, regular, repeated. That's a beacon: the malware checking in."
> "E14: one session, bytes OUT one billion eight hundred and seventy-four million, bytes IN forty-eight thousand. Out is forty thousand times bigger than in. That's the shape of data leaving. That's the Critical line."

**7. The finding that is a 'nothing'.**
> "E18: no inbound connection from the internet to either machine. Nothing broke in through an open port. It came in by email and was pulled in from the inside. Write that down. It's a finding."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "My port is 51022, the remote port is 443. Who started it?" | My machine. It is egress |
| "E03 is an OUT connection. Why is it in the ingress section?" | A file came in on it: 1.2 MB, the malware |
| "What does a beacon look like in bytes?" | Small, regular, repeated |

## Common problems
| Problem | Fix |
|---------|-----|
| Hundreds of rows | Add `| Select-Object -First 15` |
| `Get-NetAdapterStatistics` shows nothing (virtual adapters) | Skip it. Steps 2–4 carry the idea |
| A trainee pastes their connection list in the chat | Ask them to remove it. Only your own machine, and not shared publicly |

---
---

# DEMONSTRATION 4 — NAME IT, MAP IT
### 10:10 AM · Slides 9–10 · Topic 10.4 · E5 PC 5.4 · knowledge 5.3

## Why this exists
Trainees separate **exploitation** (how they got in, and got more access) from **installation** (how they stay), then give each behaviour its ATT&CK name and ID, and build a **Navigator layer** they can export. This is the Day 3 ATT&CK desk, now used on a whole case.

## What you need
- `https://mitre-attack.github.io/attack-navigator/` open
- `https://attack.mitre.org` in a second tab
- Sample Data §4 (the twelve behaviours) and §8 (the Navigator steps)

## The steps
**1. Two questions, on screen.**
> "PC 5.4 asks two things. How did they get in, and get more access? That's EXPLOITATION. And what did they leave behind so it keeps running? That's INSTALLATION."

**2. Exploitation, in plain words.**
> "WKS-311: E01, an invoice email with a macro document. E02: the user opened it, and Word started PowerShell. Nobody broke a piece of software here. The user was tricked into running it. That's still how they got in. SRV-BAK-02: E07 and E08, thirty-eight passwords guessed against svc_backup, and one worked. The 'exploit' was a weak password on a service account. Say that exactly, because it decides the fix: training and blocking macros, a strong password. Not a patch."

**3. Installation, and the Day 9 mystery solved.**
> "E05: a scheduled task, at every logon. You met this technique on Day 3. And E11: a Windows service, auto-start, set to restart after every failure. Remember Day 9? 'The process restarted itself within four seconds.' 'Quarantine failed, file in use.' THIS is why. The service kept restarting it, so the file was always in use. Four days, one explanation."

**4. Tactic versus technique.**
> "On ATT&CK, the columns are tactics: the attacker's GOAL. Persistence, Lateral Movement. The boxes are techniques: the METHOD, and the method has the ID. Why and how."

**5. Open Navigator and create a layer.**
- Click **`Create New Layer`**, then **`Enterprise`**.

**What you will see:** a wide matrix. Column headings (Reconnaissance … Impact) along the top, and boxes of techniques below them.
> "Every column is a goal. Every box is a method. Let me name the layer."
- Click the layer name at the top and type `CTM-0007-001 SRV-BAK-02`.

**6. Map B1: the invoice email.**
> "B1: an email with a macro document was sent to a user. On attack.mitre.org that's Phishing, Spearphishing Attachment, T1566.001. Tactic: Initial Access."
- Click the **magnifier** (search) in the toolbar. Type `T1566.001`.
- In the results, on the technique, click **`select`**.
- Click the **paint bucket** (background colour) and choose a teal.
- Click the **speech bubble** (comment) and type `E01 Invoice_Sept.docm delivered to m.delacruz`.
- Click an empty part of the page to deselect.

**What you will see:** the *Phishing* box in the Initial Access column is coloured. *(If the sub-technique is hidden inside its parent, use the toolbar's expand sub-techniques button, or just search again.)*

**7. Map B2 and B3 the same way.**
> "B2: the user opened it and the macro ran. User Execution, Malicious File, T1204.002. Tactic: Execution. B3: PowerShell ran a hidden command. Command and Scripting Interpreter, PowerShell, T1059.001. Also Execution."
- Repeat: search → select → colour → comment (`E02 WINWORD → powershell -w hidden`).

**8. Export the layer.**
- Click the **download** button (*download layer as json*) in the toolbar.
- Save as `Evidence/Day_10/CTM-0007-001_attack_layer.json`.
> "That file is the layer. Anyone can open it in Navigator and see exactly what you mapped, with your evidence line on every box. Your team does the other nine behaviours next."

**9. The Day 3 caution, once more.**
> "ATT&CK gives the behaviour a name. It can't prove THIS event is that technique. That's what your line number is for. No line, no box."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Was a software vulnerability exploited on WKS-311?" | No, not on this evidence. A user ran a macro |
| "Which line explains Day 9's 'restarted itself in 4 seconds'?" | E11: the service set to restart after every failure |
| "Tactic or technique: which one has the ID?" | The technique |

## Common problems
| Problem | Fix |
|---------|-----|
| Navigator will not load (school or company filter) | Switch to the paper mapping table (Activity Pack Part 3). Show the fallback screenshot of a finished layer |
| Search finds nothing | Check the ID has the dot and no spaces: `T1566.001` |
| The icons are in different places | Hover over the toolbar to read the names. The five you need are: create layer · search · colour · comment · download |
| The download does nothing | The browser may have blocked it. Check the download bar, or right-click the button and allow downloads |

---
---

# DEMONSTRATION 5 — PREVIEW: WAZUH, ATOMIC RED TEAM, HAYABUSA
### 10:55 AM · Slide 12 · Topic 10.5 · two minutes, screenshots only

## Why this exists
It sets the expectation that the report gets **faster** with tools, and that the report itself does not change.

## The steps
**1. Wazuh ATT&CK module** *(one screenshot from Resources):*
> "Once our server is built, each alert arrives with its ATT&CK technique already attached, and there's a dashboard of tactics across every machine. What you did by hand this morning, it does as the alert lands."

**2. Atomic Red Team** *(one screenshot):*
> "This is a library of small, safe tests. Each one makes one technique happen, like creating a scheduled task, inside a throwaway Windows Sandbox. Why? To check whether our tools would actually DETECT it. It comes with the on-site lab."

**3. Hayabusa** *(one screenshot):*
> "And this is Hayabusa. It turns a machine's event logs into the kind of timeline you read this morning, in seconds."

**4. The point.**
> "Faster finding, and faster mapping. The report is the same: fifteen sections, and every claim on a line."

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Tell the SRV-BAK-02 story from E01 to E18 aloud without notes, in under four minutes
- [ ] Read the N1 call aloud once, timed. It should take under two minutes
- [ ] Fill the written notification for N1. Keep it as your Demo 1 model
- [ ] Fill both Demo 2 tables (hosts and path). Say the SRV-FIN-02 reasoning aloud
- [ ] Run the four §7 commands. Choose one egress row and one listening port to talk about
- [ ] Build the B1–B3 layer in Navigator and export the JSON. Note where the five buttons are on the current version
- [ ] Map B4–B12 yourself against the key in Solutions, so you can help teams quickly
- [ ] Have the Wazuh, Atomic Red Team and Hayabusa screenshots ready
- [ ] **Assessment:** read `Day_10_Unit_Assessment_Guide.md` Parts 1–3 and 5. Check the candidate files are not in the joining note

## The three sentences you should be able to say without notes
1. **Fast beats complete: notify the owner of a High or Critical threat within the clock, and tell them what to do and not do.**
2. **Link with evidence, not with the clock: origin, confirmed, attempted, not linked, and every word on a line.**
3. **Exploitation is how they got in. Installation is how they stay. ATT&CK names both, and the line proves it.**
