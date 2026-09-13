# DAY 6 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### Written for a trainer running Day 6 for the first time, to a class of complete beginners

---

## READ THIS FIRST

This guide assumes **nothing** — not from you, and not from the class. It tells you which button to click, what you will see, what to say, and what to do when it does not work.

**Remember two things about Day 6:**
1. **No server.** Everything runs on your own Windows machine and theirs. No Wazuh, no internet dependency after the joining note.
2. **Total beginners.** Say every term once in plain words. Go slowly. Nobody here has opened Event Viewer before.

**How to read the formatting:**

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` / `command` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic in brackets)* | A note for you — never read aloud |
| **What you will see** | What should appear. If not, see the problems table |

**Four demonstrations, all follow-along** (the class does them too):

| # | Demonstration | When | Min | Topic |
|---|--------------|------|-----|-------|
| **1** | Where alerts come from — the source snippets | 8:30 | in 6.2 | 6.2 |
| **2** | Reading your own logs — Event Viewer & Protection History | 10:10 | in 6.4 | 6.4 |
| **3** | Make a real alert — the EICAR detection | 10:30 | 15 | 6.4 |
| **4** | Red flags and severity — reading a detection | 11:10 | in 6.5 | 6.5 |

---
---

# BEFORE ANY DEMONSTRATION — SETTING UP YOUR SCREEN

Same as always: clean desktop, large text, notifications off (Windows + `N`, Do Not Disturb), share the window or a clean whole screen, narrate as you go, and **slow down**. Beginners on a projector need everything twice as slowly as feels natural.

**One extra thing for today:** when you demonstrate the EICAR file, a Defender pop-up may appear over your shared screen. That is expected and it is the point — do not dismiss it in a panic. Let the class see it.

---
---

# DEMONSTRATION 1 — WHERE ALERTS COME FROM
### 8:30 AM · part of Topic 6.2 · Slides 4–5 · knowledge 1.5

## Why this demonstration exists
Beginners need to attach the acronyms (AV, firewall, WAF, DLP) to something they can see. You are not operating these tools — you are showing four example alerts and naming which tool made each.

## What you need
- The four source snippets from `Day_6_Sample_Data.md` §2, on slides 4–5

## The steps
**1. Put snippet A on screen** *(the Defender/AV one)*.
> "Read this. A file called invoice.exe, in a Public folder, and something called Defender quarantined it. Which tool raised this? It says Defender — that is antivirus. Antivirus watches files. So this is an AV alert."

**2. Ask the blind-spot question — every time.**
> "What can antivirus NOT see? A brand-new threat that nobody has caught yet. Zero detections is not 'safe' — remember Day 3."

**3. Repeat for B (firewall), C (WAF), D (DLP)**, each in under a minute, always ending on the blind spot.
> "Firewall watches traffic in and out. WAF watches requests to a website. DLP watches sensitive data trying to leave. Four tools, four jobs, and every one has something it cannot see."

**4. Land the map.**
> "You will not operate these today. You need to know which tool an alert came from, because that tells you what it can and cannot tell you. Today, the tool raising your alerts is the antivirus already on your own machine — Defender."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "A file was quarantined. Which tool?" | Antivirus (AV) |
| "A connection was blocked leaving the network. Which tool?" | Firewall |
| "What can a firewall not see?" | What happens inside an allowed connection |

## If you are offline
Everything here is on the slides. No internet needed.

---
---

# DEMONSTRATION 2 — READING YOUR OWN LOGS
### 10:10 AM · part of Topic 6.4 · Slide 9 · knowledge 1.6

## Why this demonstration exists
The class must know **where a Windows machine writes down security events**, before they make one happen in Demo 3. This is their first time in Event Viewer — go slowly.

## What you need
- Your own Windows machine. No admin needed for the parts below.

## The steps
**1. Open Event Viewer.**
> "Press the Windows key, type Event Viewer, and open it. This is where Windows writes down almost everything that happens."

**What you will see:** a window with a tree on the left — Custom Views, Windows Logs, Applications and Services Logs.

**2. Open the System log first (it needs no admin).**
> "Expand Windows Logs, click System. Every line is an event — a time, an ID number, and a message. Thousands of them. This is normal. The skill is not reading all of them — it is filtering to the ones that matter."

**3. Show the Defender log — where today's detection will land.**
> "Now expand Applications and Services Logs, then Microsoft, then Windows, then Windows Defender, then Operational. THIS is where the antivirus writes down what it finds. Right now it is probably quiet. In fifteen minutes it will not be."

*(Full path: Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational.)*

**4. Show Protection History — the friendly view, no admin, no Event Viewer.**
> "There is an easier view. Press Windows, type Windows Security, open it. Click Virus & threat protection, then Protection history. This is the same information as the Defender log, but in plain language. This is where you will look first on a real desk."

**5. Mention the firewall log briefly** *(do not open it live — it needs admin and may be empty):*
> "There is also a firewall log — a text file that records blocked connections, if logging is turned on. We will not open it today; just know it exists, here." *(Show the path on the slide: `%systemroot%\system32\LogFiles\Firewall\pfirewall.log`.)*

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "Where does the antivirus write what it finds?" | The Windows Defender / Operational log, or Protection history |
| "Which is easier to read for a beginner?" | Protection history, in the Windows Security app |

## Common problems
| Problem | Fix |
|---------|-----|
| Security log says "access denied" | Needs admin. Use the Defender Operational log and Protection history instead — no admin needed |
| Can't find the Defender log in the tree | Use Protection history in the Windows Security app; same information |
| Event Viewer is overwhelming | That is normal — say so. Nobody reads it all. We filter |

---
---

# DEMONSTRATION 3 — MAKE A REAL ALERT (EICAR)
### 10:30 AM · 15 minutes · Slide 10 · Topic 6.4 · the highlight of the day

## Why this demonstration exists
Nothing teaches "a detection alert" like making one happen safely, on your own machine, and watching the tool react. This is that moment.

## What you need
- The EICAR string from `Day_6_Sample_Data.md` §1, ready to paste
- Notepad and a folder you can write to (e.g. Documents)

## Before class
**Do this once yourself the night before.** Create the file, watch Defender react, check Protection history — so you know the exact wording and behaviour on your build. Behaviour varies: some machines quarantine silently, some pop up, some block the save entirely.

## The steps
**1. Reassure first — say this before you do anything:**
> "We are about to make the antivirus catch something, on purpose. What we use is called the EICAR test file. It is NOT a virus. It has never been a virus. It is a harmless line of text that every antivirus in the world agreed to treat as if it were dangerous, just so we can test them safely. Nothing here can harm your computer. Watch."

**2. Open Notepad and paste the EICAR string** *(paste, never type):*
```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

**3. Save it as `eicar_test.txt` in Documents.**

**What you will see (one of three, all fine):**
- A Defender notification pops up: "Threat found" / "Threats found".
- The file vanishes as you save it (Defender removed it instantly).
- Or a message that the file could not be saved because it contains a threat.

> "There it is. The antivirus saw it the moment it hit the disk. That is a detection alert — a tool telling you it found something. Now let's read what it recorded."

**4. Open Protection history** (Windows Security → Virus & threat protection → Protection history).

**What you will see:** an entry, usually **Virus:DOS/EICAR_Test_File**, with a time and an action (Quarantined or Removed).

> "Read the three things it tells us. WHAT it found — the EICAR test file. WHEN — this timestamp. And WHAT IT DID — it quarantined or removed it. Those three things are your detection record. Write them down and you have received an alert, properly."

**5. Show the same event in the Defender log** (Event Viewer → the Operational log from Demo 2).

**What you will see:** event **1116** (detected) and **1117** (action taken).

> "Same event, two places. The friendly view in Protection history, and the raw log here — event 1116, malware detected. On a real desk you use both."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "Is the EICAR file dangerous?" | No — a harmless test string, never malware |
| "What three things does the detection tell you?" | What was found, when, and what action was taken |
| "Where did we see the detection?" | Protection history, and the Defender Operational log (event 1116) |

## Common problems
| Problem | Fix |
|---------|-----|
| Nothing happens on save | Real-time protection may be off. Check Windows Security → Virus & threat protection settings. Or the machine's AV differs — use its history |
| The file saves and stays | Some builds catch it only on scan. Run a quick scan of Documents, then check history |
| A trainee is scared | Repeat: it is a test string, not malware. Show them the EICAR explanation on the slide |
| Managed machine blocks creating the file | The block IS the detection. Go to Protection history and read the blocked entry |

## If you are offline
No internet needed — EICAR detection is entirely local. This demo works with the network unplugged.

---
---

# DEMONSTRATION 4 — READING A DETECTION FOR RED FLAGS AND SEVERITY
### 11:10 AM · part of Topic 6.5 · Slides 12–13 · knowledge 1.9, 1.10

## Why this demonstration exists
Turn the detection the class just made (and the indicator cards) into the two analyst judgements: **is this a red flag?** and **how serious is it?**

## The steps
**1. Go back to the EICAR entry in Protection history.**
> "Here is our detection. Is it a red flag — ransomware or a virus? No. It is a test file. What severity? Defender shows Low or Severe depending on version, but WE know it is a test on a training machine, so the company band is Low. See how the tool's severity is a starting point, and we make the final call?"

**2. Contrast with a red flag, using indicator card 1 or 5** *(from Sample Data §4):*
> "Now imagine this instead — hundreds of files renamed .locked and a ransom note in every folder. That is ransomware. Even before any tool labels it, the PATTERN tells you. That is a red flag, and the band is Critical, because it is spreading and it stops the business."

**3. Show the severity matrix (slide 13)** and teach the mapping rule:
> "Start from the tool's severity. Then adjust for two things: is it contained — stopped — yes or no? And whose machine is it — a training PC, or the finance server? The same detection can be Medium on a lab PC and High on a server. And always — always — write down WHY you chose the band."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "Two red-flag categories the standard names?" | Ransomware, and PE infection (virus) |
| "The tool says Low. It's on the CEO's laptop and not contained. Your band?" | Higher than Low — adjust for asset and containment, and say why |

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Open Event Viewer; find the Windows Defender / Operational log
- [ ] Open Windows Security → Protection history
- [ ] Create the EICAR file once; watch what your machine does; check history and the log (event 1116/1117)
- [ ] Note which of the three behaviours your build shows, so you can tell the class what to expect
- [ ] Read the six intake scripts aloud once, so you can deliver them in character tomorrow

## The three sentences you should be able to say without notes
1. **An alert is either a tool telling you or a person telling you — both must be written down.**
2. **EICAR is a harmless test file; making it detected is a safe, real detection alert.**
3. **The tool's severity is the start; you adjust for containment and asset, and write the reason.**
