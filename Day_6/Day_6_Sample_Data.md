# DAY 6 — SAMPLE DATA
## The scripts, cards and scenarios the activities use
### Trainer, and trainees where marked.

> **Safety note.** The EICAR test file is the only "threat" used today, and it is not a threat — it is a harmless text string every antivirus is built to detect on purpose, so people can safely test AV. No real malware, no client data anywhere in the Day 6 set. Addresses use the documentation-only ranges (`203.0.113.x`, `198.51.100.x`).

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The EICAR test string | Demo 3, Activity 3, PM Task 2 |
| 2 · The four alert-source snippets | Activity 1 "Name That Source" |
| 3 · The six intake scripts | Activity 2 "Take the Call" (trainer reads aloud) |
| 4 · The red-flag indicator cards | Activity 4 "Red Flag or Routine?" |
| 5 · The company severity matrix | Topic 6.5, PM Task 6 |

---
---

# 1 — THE EICAR TEST STRING

This is the exact 68-character string that makes up the EICAR test file. Type it as one line, with no spaces and no line break, into a new text file and save it as `eicar_test.txt`. Defender will detect it the instant it is saved.

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

> Copy it, do not retype it — one wrong character and it will not be detected, which confuses beginners.

**What it is:** a string agreed by the European antivirus industry (EICAR) as a universal test. Every AV recognises it and treats it as if it were a threat, so you can prove your AV works without ever touching real malware. **It cannot harm anything. It never could.**

**How Defender reports it:** the threat name is usually `Virus:DOS/EICAR_Test_File` (wording varies by version). It appears in **Protection history** and in the **Windows Defender / Operational** event log as event **1116** (malware detected) followed by **1117** (action taken — quarantined or removed).

---
---

# 2 — THE FOUR ALERT-SOURCE SNIPPETS
### Activity 1 — for each, the class answers: which SOURCE raised this, and what can it NOT see?

**Snippet A**
```
[Defender] Threat found: Trojan:Win32/Wacatac.B!ml
File: C:\Users\Public\invoice.exe   Action: Quarantined
```

**Snippet B**
```
[Firewall] Blocked outbound connection
192.168.1.54  ->  203.0.113.45 : 4444   Rule: Block-Uncommon-Ports
```

**Snippet C**
```
[Web Application Firewall] Request blocked (403)
GET /search?q=' OR 1=1 --   from 198.51.100.23   Rule: SQL-Injection
```

**Snippet D**
```
[Data Loss Prevention] Policy violation
User r.santos attached "customer_list.xlsx" to an external email. Action: Blocked
```

*(Answers in `Day_6_Solutions.docx`: A = Antivirus/AV; B = Firewall; C = WAF; D = DLP — with each one's blind spot.)*

---
---

# 3 — THE SIX INTAKE SCRIPTS
### Activity 2 — the TRAINER reads each aloud, in character. The trainee records it on an intake form and may ask ONE clarifying question.

Each script deliberately **leaves out one core fact**, so the trainee has to notice and ask. The missing fact is marked for you *(never read the italics aloud)*.

**Script 1 — PHONE CALL (panicked user)**
> "Hi, yes, my computer — all my files have weird names now and there's a text file on my desktop asking for money in Bitcoin. It started maybe twenty minutes ago. I'm on the third floor, finance."
> *(Missing: their name and a callback number. The trainee should ask for it.)*

**Script 2 — WALK-IN (calm, vague)**
> "Someone from IT told me to come report this. My email was sending messages I didn't write — my colleagues got emails from me about an invoice. I didn't send anything."
> *(Missing: when it happened / when noticed. Ask.)*

**Script 3 — EMAIL (forwarded)**
> "Forwarding this — I got an email saying my account will be closed unless I 'verify' at this link: hxxp://login-verify-account.com. Looks fake. I did not click it. — J. Cruz, Sales, ext. 214"
> *(Missing: which machine / did anyone else get it. Ask.)*

**Script 4 — SMS (short)**
> "txt from unknown num: 'Your parcel is held, pay fee here hxxp://track-ph-parcel.net'. Should I be worried? — this is Ana from reception"
> *(Missing: did she click or reply. Ask.)*

**Script 5 — CHAT (IT helpdesk chat)**
> "hey the antivirus popup keeps appearing on the training-room PC number 4, says it removed something called eicar test file, is that bad?? it's been popping up since this morning"
> *(Missing: who is reporting / their contact. Ask. NOTE: this one is routine — EICAR is a test — good bridge to Day 7.)*

**Script 6 — VIDEO CONFERENCE (manager, urgent)**
> "I need this logged now. Two of my team can't access the shared drive, and a third says her screen showed a countdown timer this morning before it went black. This is the accounts department. I'm the department head."
> *(Missing: her name/contact and which machines. Ask. NOTE: countdown + no drive access = possible ransomware — a red flag.)*

---
---

# 4 — THE RED-FLAG INDICATOR CARDS
### Activity 4 — teams sort each card into RANSOMWARE / PE INFECTION (VIRUS) / ROUTINE, and give a severity band with a reason.

| # | The indicator on the card | *(Trainer: answer)* |
|---|---------------------------|---------------------|
| 1 | Hundreds of files suddenly renamed to `.locked`, and a `HOW_TO_DECRYPT.txt` in every folder | *Ransomware · Critical* |
| 2 | Defender quarantined one `.exe` in the Downloads folder; nothing else happened | *PE infection · Medium (contained)* |
| 3 | A pop-up says "EICAR test file removed" on a training PC | *Routine · Low (it is a test file)* |
| 4 | A process named `svhost32.exe` running from `C:\Users\Public`, making network connections | *PE infection · High (fake system name, uncontained — Day 5!)* |
| 5 | The backup server's scheduled backups were all deleted last night, and files won't open | *Ransomware · Critical (backups gone = recovery at risk)* |
| 6 | Windows Update installed a patch and asked to restart | *Routine · Low (normal maintenance)* |
| 7 | AV blocked an advertising toolbar (PUA) during a software install | *Routine / PE-adjacent · Low (blocked PUA)* |
| 8 | A staff member reports files opening slowly and a new `.exe` on the desktop they didn't put there | *PE infection · High (unknown executable, not yet contained)* |

---
---

# 5 — THE COMPANY SEVERITY MATRIX
### Topic 6.5 and PM Task 6 — the band each detection is mapped onto.

| Band | Meaning | Response time (example SOP) | Typical example |
|------|---------|-----------------------------|-----------------|
| **Critical** | Business-stopping or spreading now | Notify immediately (≤10 min) | Ransomware active; server down; data leaving |
| **High** | Serious, not yet contained | Act within the hour | Confirmed malware still running; fake-named process with network activity |
| **Medium** | Real, but handled or single | Act this shift | One malware file quarantined; one blocked intrusion attempt |
| **Low** | Note and monitor | End of shift | Blocked PUA/ad; an EICAR test; a normal patch |

> **Mapping rule to teach:** start from the tool's severity, then adjust for **containment** (is it stopped?) and **asset** (whose machine — a training PC or the finance server?). The same detection can be Medium on a lab PC and High on a server. **Write the reason for the band you chose.**
