# DAY 5 — SOLUTIONS AND MARKING GUIDE
## For the trainer only. Do not distribute before the activity.

> **How to use this file.** Keep it open in a second window all morning. Activity 1 needs answers within seconds. Activity 3 needs you to know the attack story cold.
>
> Everywhere below, **the reason is the answer.** A trainee who reaches a defensible conclusion with sound reasoning has met the criteria. A trainee who reaches the right word with no reasoning has not.

---

## THE ONE IDEA THAT RUNS ALL DAY

**Location, ownership and behaviour are evidence; a name is not.** A file's *name* can be faked in seconds. Where it *lives*, which *process* owns a connection, and what a script *does* are much harder to fake — and they are what an analyst reads. Keep bringing every answer back to that.

Decision words are unchanged from Day 3: **threat / detection / routine**, and the line between threat and detection is **containment, not severity.** Never write "false alarm" as a decision — a false alarm is a kind of routine.

---
---

# ACTIVITY 1 — WHERE DOES IT LIVE?

## Answer key

| # | Item | Answer | The reason |
|---|------|--------|-----------|
| 1 | `svchost.exe` in `System32` | **NORMAL** | The real svchost lives exactly there |
| 2 | `svchost.exe` in `C:\Users\Public` | **SUSPICIOUS** | Right name, wrong place. Windows system files do not live in Public. This is masquerading |
| 3 | `chrome.exe` in `C:\Program Files\Google\Chrome\...` | **NORMAL** | That is where Chrome installs |
| 4 | `explorer.exe` from `Downloads` | **SUSPICIOUS** | The real explorer runs from `C:\Windows`. Location is wrong |
| 5 | Scheduled task running encoded PowerShell | **SUSPICIOUS** | Encoding hides intent; a legitimate task rarely needs it. This is the Day 3 WKS-118 shape |
| 6 | `wuauserv` set to auto-start | **NORMAL** | Windows Update is a real service, auto-start is expected |
| 7 | `lsass.exe` in `System32`, Microsoft-signed | **NORMAL** | Right file, right place, valid signature |
| 8 | `1sass.exe` (digit one) in `C:\Temp` | **SUSPICIOUS** | Not `lsass` — a digit swapped for a letter, and living in Temp. Two red flags |
| 9 | Startup pointing at a `.vbs` in a temp folder | **SUSPICIOUS** | A script auto-running from temp is a classic persistence trick |
| 10 | `python.exe` in `C:\Python314` you just installed | **NORMAL** | You installed it; it is where Python installs. Known and expected |

**Score: NORMAL = 1, 3, 6, 7, 10 · SUSPICIOUS = 2, 4, 5, 8, 9.** Five and five.

## The ones the class will get wrong

| # | Why | What to say |
|---|-----|-------------|
| **8** | `1sass.exe` looks close enough to skim past | "Read it letter by letter. That is a digit one, not an L. And it is in Temp. Attackers rely on you skimming" |
| **10** | Trainees flag it because they do not recognise it | "You installed it an hour ago. Unfamiliar is not the same as malicious. The question is: is it where it should be, and do you know why it is there?" |
| **6** | Auto-start *sounds* suspicious | "Auto-start is normal for real services. It is the *combination* — auto-start plus encoded command plus fake name — that is the signal" |

## The debrief line

> "Every one of these you decided **before** touching a browser. A name, a location, a signature — that is evidence you already have. Looking things up comes *after* you have read what is in front of you."

---
---

# ACTIVITY 2 — FOLLOW THE CONNECTION

This is observed, not answer-keyed — trainee output differs on every machine. Mark the **two behaviours**:

1. **Did they join the connection to its process themselves?** Competent: they ran the connection command and can name the owning process for their chosen connection. Not yet: they can list connections but cannot tie one to a program.
2. **Did they report in clues, not their own IP?** Competent: "a connection owned by chrome, on port 443 which is HTTPS, to a public address." Not yet: they read their own IP address aloud. If they do, correct it in the room: *"That address identifies your machine — describe it in clues, exactly as Day 3."*

**Model report to praise:**
> "I have a connection owned by `outlook`, on remote port 443 which is HTTPS, to a public address. It makes sense — mail over encrypted web is what Outlook does."

**A strong trainee also notices** a connection that does *not* make sense — e.g. an unfamiliar process on 443 to a public address from a temp path — and says they would look up the address and escalate. Praise that: it is the WKS-311 instinct forming.

---
---

# ACTIVITY 3 — ACCESS-LOG DETECTIVE

## The full story of `Day_5_access_log.txt`

The log is 40 request lines. Read it as five acts:

1. **Normal browsing** — `203.0.113.10` (Windows/Chrome), `203.0.113.11` (iPhone/Safari) and `203.0.113.12` (Android) fetch pages, images and CSS; one visitor submits the contact form (`POST /contact.php` → 200). `203.0.113.10`'s single `404` is a missing favicon — harmless.
2. **Reconnaissance** — `198.51.100.23`, user-agent **`Nikto/2.5.0`**, fires a burst of requests at `/admin/`, `/.env`, `/backup.zip`, `/phpmyadmin/`, `/.git/config`, `/config.php.bak` — mostly **404s** — plus `/wp-login.php` (200) and `/server-status` (403). This is a vulnerability scanner mapping the site.
3. **Brute force** — `203.0.113.45`, user-agent **`python-requests`**, sends **seven** `POST /wp-login.php` (all 200 — the login page kept being served), then an eighth `POST` returns **302**. The 302 is the redirect after a *successful* login. Immediately after, `GET /wp-admin/` returns 200 — the attacker is inside.
4. **Blocked traversal** — `192.0.2.77`, user-agent `curl`, tries `download.php?file=../../../../etc/passwd` and a URL-encoded variant; both get **403** (blocked, likely the WAF). A third, normal `download.php?file=brochure.pdf` gets 200. Two blocked attacks, one legitimate download.
5. **Web shell** — back as `203.0.113.45`: `GET /wp-admin/plugin-install.php` (200), `POST .../update.php?action=upload-plugin` (200 — a plugin uploaded), then `GET /wp-content/uploads/2026/09/thumb.php?c=whoami` (200), `?c=id` (200), `?c=cat wp-config.php` (200). **`thumb.php` is a web shell**, and the `c=` parameter is running commands. `cat wp-config.php` is reading the database credentials.

## Step 1 — who is who

| Address | Verdict | Proof |
|---------|---------|-------|
| `203.0.113.10` | Normal visitor | Browses pages with a real browser UA; only 404 is a favicon |
| `203.0.113.11` | Normal visitor | iPhone Safari, submits the contact form normally |
| `203.0.113.12` | Normal visitor | Android Chrome, two page views |
| `198.51.100.23` | **Scanner** | `Nikto` user-agent; a burst of 404s for admin/backup paths |
| `203.0.113.45` | **Attacker** | `python-requests`; brute-forces the login, gets a 302, then uses a web shell |
| `192.0.2.77` | Attacker / probe | `curl` with `../../etc/passwd` traversal attempts (403) |

## Step 2 — the order (by timestamp)

1. Scanner 404 burst (`198.51.100.23`, 09:12)
2. Brute-force succeeds (`203.0.113.45`, 09:20 — eight POSTs then 302)
3. Traversal blocked (`192.0.2.77`, 09:31 — 403s)
4. Plugin uploaded (`203.0.113.45`, 09:40)
5. Commands run through the shell (`203.0.113.45`, 09:40 — `thumb.php?c=...`)

*(Note the traversal at 09:31 lands between the login and the upload by clock time; either "recon → brute-force → traversal → upload → shell" by timestamp, or grouping the attacker's own actions together, is acceptable if the trainee justifies it from the times.)*

## Step 3 — the two deciding questions

1. **The worst line:** `GET /wp-content/uploads/2026/09/thumb.php?c=whoami HTTP/1.1 200` (or the `cat wp-config.php` line). **Why:** a `200` here means a command actually **ran** on the server through an uploaded file. Reading `wp-config.php` hands over the database credentials. The 403 traversal lines look dramatic but were *blocked*; this one succeeded.

2. **Decision: THREAT.** **Reason:** the attacker is inside (successful login, 302), has uploaded a web shell, and is running commands right now. **Nothing has contained it.** That is the definition of a threat, not a detection — a detection would be something the security solution found *and stopped*. The scanner and the blocked traversal are lower-priority; the live shell is the emergency.

> **The line to land:** "The 403s are the noise. The 200 on the web shell is the fire. Blocked is safe; served is not."

**Common wrong answers:**
- "Detection, because the traversal was blocked." — Only the traversal was blocked. The shell was not. Containment is partial, and the part that matters failed.
- Focusing on the scanner as the main event — reconnaissance is real but it is act one, not the incident.

---
---

# ACTIVITY 4 — EXPLAIN THIS SCRIPT, DON'T RUN IT

| Script | What it does | Internet? | Verdict |
|--------|-------------|-----------|---------|
| **A** `collect-baseline.ps1` | Lists processes, writes them to a local CSV | **No** | **Run it** — it is a benign admin tool, the same one used in Demo 2 |
| **B** the "Adobe Update Checker" cradle | Downloads text from a URL, base64-decodes it into code, runs it with `Invoke-Expression` | **Yes** | **Escalate** — a download cradle. You never run it to see what `p.txt` is. This is the WKS-118 task as source |
| **C** the buggy parser | Meant to count 404s per IP, but compares the string `"404"` to the integer `404`, so it always finds zero | No | Harmless, but **broken** — do not trust its "zero 404s" |

**Script C answers:**
1. **Why zero?** `status` is a **string** (`"404"`); `404` is an **integer**; a string never equals an integer in Python, so the `if` is never true. The log has seven 404s and the script reports none.
2. **The lesson:** a script that runs cleanly and reports nothing has **not proven there is nothing.** Tools have bugs. Check a tool's silence against a second method — the working parser, or a manual count.

> **The read-don't-run point to land:** "Script B is the one you were tempted by, and it is the one you must never run. Reading told you exactly what it does — fetch and run code from an address. That is enough to escalate. Running it is the incident."

---
---

# TASK 1 — WORKSTATION BUILD CHECKLIST

Marking is completion + accuracy of recorded detail. Competent: every reachable item ticked with a real value recorded (real PowerShell version, real path). Not yet: ticks with no detail, or invented values. The OH&S line ties back to the Day 3 audit — accept any genuine adjustment (monitor height, lighting, break reminder).

---

# TASK 2 — BASELINE, HASHED AND REGISTERED

| Requirement | Competent | Not yet |
|-------------|-----------|---------|
| Four CSVs exported | All four present and non-empty | Missing files or empty files |
| Hashed | A real SHA-256 recorded for each | No hashes, or made-up strings |
| Named to convention | `YYYY-MM-DD_BASELINE_HOST_processes.csv` etc. | Default names left as-is |
| Registered | The table filled with names, hashes, descriptions | Blank or partial |

**The "why capture when nothing is wrong" line:** competent answers say the baseline is the only way to answer "is this new?" *later* — you cannot compare against a snapshot you never took.

---

# TASK 3 — MAINTAIN AND BACK UP

The two hashes (original and copy) **must match** — that is the whole point. If they differ, the copy is corrupt or the wrong file was hashed. Competent answer to "why is an unverified copy not a backup": because you have no proof it is complete and identical until the hashes match — an unverified copy might be truncated or corrupt.

---

# TASK 4 — ANNOTATE FIVE CONNECTIONS

Marking: can the trainee (a) name the owning process, (b) read the remote port to a service, (c) classify the address public/private, and (d) judge whether it is normal? Model row:

| Process | Remote port | Service | Public/private | Normal? |
|---------|-------------|---------|----------------|---------|
| chrome | 443 | HTTPS | Public | Yes — browser to a website |
| svchost | 443 | HTTPS | Public | Yes — Windows update/telemetry |

The "look at first" line should pick the *least explainable* connection — an unfamiliar process, a public address, an odd port — and give that as the reason. That is the analytical skill.

---

# TASK 5 — PORT MAP

Competent: the diagram shows the trainee's private address, the gateway, the shared public address, and marks where NAT happens; the two-line answer correctly says that only deliberately forwarded ports are reachable from the internet and everything else sits behind NAT, unreachable directly. Not yet: a diagram with no private/public distinction, or an answer that thinks the whole home network is directly reachable.

---

# TASK 6 — READ THE WEB LOG

1. **`203.0.113.45`, 14 requests.** *(Highest in the parser output.)*
2. **`198.51.100.23`** — the `Nikto` user-agent and a burst of 404s for `/admin/`, `/.env`, `/backup.zip`, `/phpmyadmin/`, `/.git/config`, `/config.php.bak`.
3. **Seven** `wp-login.php` POSTs, then the eighth returns **302** — a redirect after a **successful** login. The attacker guessed the password.
4. The two `403`s mean the server **blocked** the path-traversal attempts (`../../../../etc/passwd`) — likely the WAF. Blocked = it worked.
5. `thumb.php?c=whoami` at **200** means a command **ran** on the server through an uploaded file — a web shell. It is the worst line because it is code execution, and it is not contained.
6. **One sentence:** the site was scanned, its WordPress login brute-forced successfully, a malicious plugin uploaded, and the attacker is now running commands through a web shell (`thumb.php`) — an active, uncontained compromise.

---

# TASK 7 — EXTEND THE PARSER

**Model edit** (the three additions):
```python
not_found = Counter()          # near the other counters
# ... inside the loop, after unpacking status:
if status == "404":
    not_found[ip] += 1
# ... after the existing prints:
print("404s per IP address (flag above 5):")
for ip, count in not_found.most_common():
    flag = "  <-- CHECK THIS ADDRESS" if count > 5 else ""
    print(f"  {ip:<16} {count}{flag}")
```

**Correct output (verified):**
```
404s per IP address (flag above 5):
  198.51.100.23    6  <-- CHECK THIS ADDRESS
  203.0.113.10     1
```

Of the seven 404s, **six** belong to the scanner `198.51.100.23` (flagged) and **one** to a normal visitor's missing favicon (`203.0.113.10`). Competent: the script runs and flags exactly `198.51.100.23`. Not yet: the script errors, flags nothing, or flags the wrong address. **The hand-tally fallback is fully competent** if the counts are right (6 and 1).

> Watch for the Script-C bug reappearing: a trainee who writes `if status == 404:` (integer) will get zero. If their output shows zero 404s, that is the bug — a good moment to connect it to Activity 4.

---

# TASK 8 — RE-TICKET WKS-311

**Model re-ticket:**
> "Workstation WKS-311, private address 192.168.10.31, assigned to m.delacruz. It is making two outbound connections to 185.220.101.1 on port 443 (HTTPS, encrypted). I ran `netstat -ano` and `tasklist`: both connections are owned by PID 6820, which is **`svhost32.exe`** — a misspelled name (should be svchost), and I would confirm its path is not System32. On AbuseIPDB the address is a heavily reported Tor exit node (credible). Decision: **THREAT** — repeated after-hours connections to an anonymising address, owned by a masquerading process, and nothing has contained it. Same shape as the Day 3 finding, now with the process identified. **I need authorisation to isolate WKS-311, and the file path and hash of svhost32.exe (PID 6820) captured for L2.**"

**The field the new ticket has that Day 3's lacked:** the **owning process** (`svhost32.exe`, PID 6820) — and the port read as HTTPS. Day 3 could name the address only. Competent answers name the process as the added field.

---

# TASK 9 — REFLECTION

Not separately graded; read for engagement. Good answers to Q2 name the read-don't-run rule explicitly: **read the script, escalate it, do not run it.**

---
---

# QUICK ANSWER STRIP — KEEP THIS VISIBLE

- **Activity 1:** NORMAL = 1,3,6,7,10 · SUSPICIOUS = 2,4,5,8,9
- **Parser numbers:** status 200=27, 302=2, 304=1, 403=3, 404=7 · IPs 45→14, 23→10, 10→7, 11→4, 77→3, 12→2
- **404s per IP:** `198.51.100.23`=6 (flagged), `203.0.113.10`=1
- **Web log verdict:** THREAT — successful brute-force + web shell, uncontained. Worst line = `thumb.php?c=whoami` at 200
- **Real system-file home:** `C:\Windows\System32` (explorer: `C:\Windows`)
- **WKS-311 owning process:** `svhost32.exe`, PID 6820
- **Private ranges:** 10 / 172.16–31 / 192.168 · loopback 127.0.0.1
- **Script B verdict:** ESCALATE (download cradle). **Script C bug:** `"404"` string vs `404` int → always zero
