# DAY 5 — STUDENT HANDOUT
## Underneath the Alert — the Machine, the Wire, the Web and the Script
### Cyber Threat Monitoring Level I · Day 05 of 15

---

## WHAT TODAY IS ABOUT

On Day 3 you took an alert, looked up the clue, judged the source, and wrote a ticket. But you stopped at the browser. When the alert said WKS-311 was connecting to a bad address on port 443, you could look up the address — but you could not yet say **which program** was making the connection, whether port 443 was normal, or where on the machine the file lived.

Today you close that gap. An alert points at four things: a **process**, an **address and port**, a **web request**, and a **script**. Today you learn to read all four, on your own machine, with real commands — and to prepare and baseline the workstation you read them on.

> **Two rules hold all day, and they are not negotiable:**
> - **Read a suspicious script. Never run it.** Running it is the incident.
> - **Scan only a machine you are authorised to scan.** Today that means your own — `127.0.0.1` — and nothing else. Scanning anyone else's machine without permission is illegal under RA 10175.

---

## TODAY'S FIVE TOPICS

| # | Topic | What you will be able to do |
|---|-------|----------------------------|
| **5.1** | The Machine Underneath | List what runs on a machine, and say where files should live |
| **5.2** | Preparing and Maintaining the Analyst Workstation | Build, baseline and maintain your workstation |
| **5.3** | The Wire | Read an address, a port and a connection to its process |
| **5.4** | The Web Request | Read an access log and tell an attack story |
| **5.5** | Reading Scripts for Triage | Read a script and say what it does — without running it |

---

## Units of competency covered today

| Code | Unit | What today does |
|------|------|-----------------|
| `CS-ICT251101` | Monitor and report cyber threats | Builds the required knowledge 1.1–1.4 that every element stands on |
| `ICT311203` | Perform Computer Operations | Completed today — plan, input, access, output/transfer, maintain |
| `400311106` | Access and maintain information | LO4 (never send content) reprised; LO5 (manage) is the baseline registered |
| `ICT315202` | Apply quality standards | LO2 (self-check) on the re-ticket |

---
---

# TOPIC 5.1 — THE MACHINE UNDERNEATH

You cannot spot the abnormal until you know the normal. Four things run on a machine, and you should be able to list each with a command.

| What runs | Windows command | macOS | Ubuntu |
|-----------|-----------------|-------|--------|
| Processes | `Get-Process` | Activity Monitor · `ps` | `ps`, `top` |
| Services | `Get-Service` | `launchctl list` | `systemctl` |
| Scheduled tasks | `Get-ScheduledTask` | `launchd` (LaunchAgents/Daemons) | `crontab -l`, `systemd` timers |
| Autoruns / startup | `Get-CimInstance Win32_StartupCommand`, Autoruns | Login Items, LaunchAgents | `systemd` units, `~/.config/autostart` |

> **Android and iOS** are in the range as *managed* devices. An L1 analyst reads their telemetry through a management console (MDM), not by opening a shell on the phone.

## Location is evidence

A process **name** can be faked in seconds. Where a file **lives** is much harder to fake. Learn where the common Windows system files really live:

| File | Lives in | If it is anywhere else |
|------|----------|------------------------|
| `svchost.exe` | `C:\Windows\System32` | Not Windows. Suspicious |
| `lsass.exe`, `services.exe` | `C:\Windows\System32` | Not Windows. Suspicious |
| `explorer.exe` | `C:\Windows` | Not Windows. Suspicious |

This is why, on Day 3, `svhost32.exe` running from `C:\Users\Public` was a red flag **before anyone looked anything up.** One letter missing from the name, and living in the wrong place. Two pieces of evidence, no internet needed.

---

# TOPIC 5.2 — PREPARING AND MAINTAINING THE ANALYST WORKSTATION

An analyst builds their own instrument. `ICT311203` in one workflow:

| Step | What you do |
|------|-------------|
| **Plan and prepare** | Decide what the workstation needs — portable tools, browser, PowerShell — and set it up safely |
| **Input** | Record the build details accurately |
| **Access** | Open the right tool for each job |
| **Produce and transfer** | Export a **baseline** to CSV, copy it, verify the copy by hash |
| **Maintain** | Disk space, backups, antivirus on and up to date |

## The baseline

A **baseline** is a snapshot of what runs on a healthy machine, captured now, so that a future "is this new?" has an answer. You capture four lists — processes, services, scheduled tasks, autoruns — export each to CSV, hash it, name it, and register it. That single act is the heart of `ICT311203` and it also completes `400311106` LO5 (manage information).

> **A copy you have not verified is not a backup — it is a hope.** Hash the file, copy it, hash the copy, compare. If the two hashes match, the copy is exact.

---

# TOPIC 5.3 — THE WIRE

Half of every alert is an address and a port. Learn to read both.

## Private vs public addresses

| Range | Meaning |
|-------|---------|
| `10.0.0.0` – `10.255.255.255` | Private — inside a network |
| `172.16.0.0` – `172.31.255.255` | Private — inside a network |
| `192.168.0.0` – `192.168.255.255` | Private — inside a network |
| `127.0.0.1` | Loopback — **this machine**, "localhost" |
| Anything else | Public — routable on the internet |

A private address is a device inside the building; the internet cannot reach it directly. **NAT** is the translation the router does so many private devices share one public address. **Port forwarding** is a deliberate hole the other way — it maps a public port to one internal host, and it is the first thing a network review checks.

## Ports worth knowing cold

| Port | Service | Port | Service |
|------|---------|------|---------|
| 22 | SSH | 445 | SMB (file sharing) |
| 25 / 587 | SMTP (mail) | 3306 | MySQL |
| 53 | DNS | 3389 | RDP (remote desktop) |
| 80 | HTTP | 443 | HTTPS (encrypted web) |

An address answers **where**. A port answers **what service**. A process answers **who on this machine**. You need all three.

## Joining a connection to its process — the WKS-311 answer

```
netstat -ano | findstr ESTABLISHED        (the last column is the PID)
tasklist /fi "pid eq 6820"                 (turn the PID into a name)
```

Or in one PowerShell line:

```powershell
Get-NetTCPConnection -State Established |
  Select-Object LocalPort, RemoteAddress, RemotePort,
    @{Name='Process'; Expression={ (Get-Process -Id $_.OwningProcess).ProcessName }}
```

This is the line that finishes the WKS-311 ticket: it gives you the address, the port, **and** the program that owns the connection.

---

# TOPIC 5.4 — THE WEB REQUEST

Web servers generate a large share of L1 alerts, and the evidence is almost always an **access log**.

## The request path

```
browser  →  DNS  →  [ WAF / proxy ]  →  web server  →  application  →  back
```

The **WAF** (web application firewall) sits in front of the application and is where a hostile request is often turned into a **403** before the app ever sees it.

## Reading one log line

```
203.0.113.45 - - [14/Sep/2026:09:20:11 +0800] "POST /wp-login.php HTTP/1.1" 200 6712 "-" "python-requests/2.32.3"
   who              when                        method  path        result  size          user-agent (the tool)
```

## Status codes at L1 depth

| Code | Meaning | What it tells you |
|------|---------|-------------------|
| 200 | OK | The server served it. Not the same as "this was fine" |
| 301 / 302 | Redirect | Sent elsewhere — a 302 after a login POST often means success |
| 304 | Not modified | Cached — normal |
| **403** | Forbidden | Blocked — often the WAF or a permission |
| **404** | Not found | A few are normal; a **burst** from one address hunting admin paths is a scanner |
| 500 | Server error | The app broke |

> **The most dangerous line in a log is often a 200, not a 403.** `thumb.php?c=whoami` returning 200 means a command *ran*. A 403 means something was *blocked*.

---

# TOPIC 5.5 — READING SCRIPTS FOR TRIAGE

Scripts arrive as evidence — in a scheduled task, a log, a ticket. Read one well enough to say what it does. Reading is your job; **running a suspicious one is an escalation.**

## What a malicious script tends to do

- **Reach out** to the internet to fetch more code (a "download cradle").
- **Hide** what it is doing behind encoding (base64, `-EncodedCommand`).
- **Run** whatever it fetched (`Invoke-Expression`, `eval`).

A script that does all three is a launcher for code it does not even contain. That is the WKS-118 scheduled task from Day 3, seen as source. **You escalate it. You do not run it to find out.**

## The languages you will meet

| Language | You will see it as |
|----------|--------------------|
| Python | Log parsers and analyst tools (like today's) |
| PowerShell | The same jobs on Windows; also, sadly, attacker scripts |
| bash | The same jobs on Linux |
| PHP | A `.php` file in an uploads folder is a **web shell** candidate |
| Visual Basic | A macro inside a document — a classic delivery method |

> **"It ran without errors and found nothing" is not "there is nothing."** Scripts have bugs. A parser that compares the text `"404"` to the number `404` will always find zero 404s — even in a log full of them. Check silence against a second method.

---
---

# WORDS YOU WILL HEAR TODAY

| Word | Plain meaning |
|------|---------------|
| **Process** | A running program. Has a PID (a number) and a path (where it lives) |
| **Service** | A program that runs in the background, often from boot |
| **Scheduled task** | A job set to run at a time or an event — a favourite hiding place |
| **Baseline** | A snapshot of a healthy machine, to compare against later |
| **Private / public address** | Inside the building vs routable on the internet |
| **NAT** | The router's translation between private and public addresses |
| **Port forwarding** | A deliberate hole mapping a public port to one internal host |
| **Port** | Which service on a host — 443 is HTTPS, 22 is SSH |
| **PID** | Process ID — the number that ties a connection to a program |
| **Access log** | The server's line-by-line record of every request |
| **WAF** | Web application firewall — turns hostile requests into 403s |
| **Status code** | The three-digit result of a request — 200 OK, 404 not found, 403 forbidden |
| **Web shell** | A script uploaded to a server that lets an attacker run commands |
| **Download cradle** | A script whose whole job is to fetch and run more code |

---

# THE THREE SENTENCES OF DAY 5

1. **Location is evidence** — the real `svchost.exe` lives in `System32`, and nowhere else.
2. **A connection has an owner** — `netstat -ano` plus the process name finishes the ticket Day 3 could not.
3. **Read it, don't run it; scan only what is yours.**

---

## MY NOTES

*(space for the trainee)*
