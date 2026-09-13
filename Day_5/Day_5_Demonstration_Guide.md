# DAY 5 — DEMONSTRATION GUIDE
## Every demonstration, step by step, for the trainer
### Written for a trainer running Day 5 for the first time

---

## READ THIS FIRST

This guide assumes **nothing**. It tells you which command to type, what you will see when you run it, what to say while you are doing it, what to do when it does not work, and what to do when a tool is missing.

Day 5 is a **follow-along** day. You run a command; the class runs the same command on their own machines and sees their own output. That is the design. It also means their output will **not match yours exactly** — different processes, different addresses. Say so up front: *"Your screen will not look identical to mine. That is correct. The shape is what matters."*

**How to read the formatting:**

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do. Do it in this order |
| `code block` | A command. Type it or paste it exactly |
| > Grey quote block | Words you say. Say them in your own words once you are comfortable |
| *(Italic in brackets)* | A note for you. Never read this out |
| **What you will see** | What should appear. If it does not, go to the problems table |

**There are eight demonstrations.** Seven are in the morning timetable. Demo 8 is optional and only runs if you are ahead.

| # | Demonstration | When | Minutes | Topic |
|---|--------------|------|---------|-------|
| **1** | Inside the machine | 8:15 | included in 5.1 | 5.1 |
| **2** | Build the baseline | 8:47 | included in 5.2 | 5.2 |
| **3** | Your address and the wire | 9:05 | included in 5.3 | 5.3 |
| **4** | Who owns this connection | 9:25 | 15 | 5.3 |
| **5** | NAT, port forwarding, and the localhost-only scan | 10:15 | included in 5.3 | 5.3 |
| **6** | A web request, end to end | 10:25 | included in 5.4 | 5.4 |
| **7** | The twenty-line parser | 11:05 | included in 5.5 | 5.5 |
| **8** | A 60-second capture *(optional)* | If ahead | 5 | 5.3 / 5.4 |

---
---

# BEFORE ANY DEMONSTRATION — SETTING UP YOUR SCREEN

A demonstration that nobody can read is worse than no demonstration. Ten minutes of setup, once.

**1. Use a clean desktop.** Close your email, your chat, your personal browser tabs. You are about to share a terminal and a browser on a projector.

**2. Make the terminal text big.** In PowerShell or Windows Terminal, hold `Ctrl` and scroll up, or raise the font size in settings until text is clearly readable in your own share preview. Stand one metre back. If you cannot read it, they cannot.

**3. Use a light-on-dark or dark-on-light scheme with high contrast.** Avoid low-contrast themes on a projector.

**4. Turn off notifications.** Windows key + `N`, turn on **Do not disturb**.

**5. Share the window, not the whole screen** — but note that today you switch between a terminal and a browser, so sharing the **whole screen** is acceptable *if* your desktop is clean. Decide which before 8:00 and test it.

**6. Narrate while you type.** Trainees on a laggy connection see your screen seconds late. Say *"I am typing netstat dash a dash n dash o now"* rather than pointing.

**7. Slow down.** Everything takes twice as long online. If you feel slow, you are close to right.

---
---

# DEMONSTRATION 1 — INSIDE THE MACHINE
### 8:15 AM · ~10 minutes · Slide 3 · Topic 5.1 · Knowledge 1.1 · `ICT311203` E3

## Why this demonstration exists

Everything the rest of the day builds on starts here: what runs on a machine, and where files legitimately live. The class must leave this demo able to list processes, services and scheduled tasks with a command, and able to say that **`svchost.exe` lives in `System32` and nowhere else.**

## What you need

- A PowerShell window, text enlarged
- **Autoruns** from the USB drive (optional — the commands cover it if Autoruns is blocked)

## The steps

**1. Open PowerShell and list processes:**

```powershell
Get-Process | Select-Object Name, Id, Path | Sort-Object Name | more
```

**What you will see:** a long, alphabetical list of process names, their PIDs, and the full path each one runs from.

> "This is everything running right now. Look at the third column — the path. That is where each program actually lives on disk. Remember that column. It is evidence."

**2. Find the real svchost, and point at its path:**

```powershell
Get-Process svchost | Select-Object -First 1 Name, Id, Path
```

**What you will see:** `svchost` with a path of `C:\Windows\System32\svchost.exe`.

> "The real svchost lives in System32. Always. If you ever see svchost, or a name close to it, running from Users, from Public, or from a Downloads folder — that is not Windows. You knew that on Day 3 with svhost32. Now you know how to check it."

**3. List services and scheduled tasks:**

```powershell
Get-Service | Where-Object Status -eq 'Running' | Select-Object -First 15 Name, DisplayName
Get-ScheduledTask | Where-Object State -ne 'Disabled' | Select-Object -First 15 TaskName, TaskPath, State
```

**What you will see:** running services, then scheduled tasks with their paths and state.

> "Services and scheduled tasks are the two most common places attackers hide, because both survive a reboot. On Day 3 the WKS-118 attacker used a scheduled task. This is the command that finds it."

**4. Show autoruns** *(Autoruns if available, otherwise the command):*

```powershell
Get-CimInstance Win32_StartupCommand | Select-Object Name, Location, Command
```

**What you will see:** the programs set to start automatically, and from where.

> "Everything here starts by itself when the machine boots or you log in. On a machine you own, you should recognise all of it. On an alert machine, this list is where you look first."

**5. Name the other systems** *(no command — just say it):*

> "This is Windows. macOS does the same jobs with Activity Monitor and launchctl; Ubuntu with ps and systemctl. Phones — Android and iOS — you read through a management console, not by opening a shell on the phone. Same idea everywhere: what runs, what starts itself, and where it lives."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "Where does the real svchost.exe live?" | `C:\Windows\System32` |
| "Name two places an attacker hides to survive a reboot" | A service, and a scheduled task (also autoruns/startup) |
| "A process called explorer.exe is running from your Downloads folder. Normal?" | No — the real one runs from `C:\Windows`. Location is evidence |

## Common problems

| Problem | Fix |
|---------|-----|
| `Get-ScheduledTask` prints nothing useful | Add `| Format-Table -AutoSize`; some tasks have long paths that wrap |
| A trainee's `Path` column is blank for some processes | Normal — protected system processes hide their path from a non-admin. Say so; it is not an error |
| Autoruns warns about signatures / VirusTotal | Do not enable the VirusTotal option in class — it uploads hashes. `Get-CimInstance` is the safe fallback |

## If a command is blocked

`Get-Process`, `Get-Service` and `Get-CimInstance` are built in and rarely blocked. If execution policy stops anything, everything here also exists in the GUI: Task Manager (Details, Startup), `services.msc`, Task Scheduler. Walk those instead.

---
---

# DEMONSTRATION 2 — BUILD THE BASELINE
### 8:47 AM · ~10 minutes · Slide 5 · Topic 5.2 · `ICT311203` E4, E5 · `400311106` LO5

## Why this demonstration exists

This is the compressed Day 4 made concrete. The class produces a **baseline** — a snapshot of what runs on a healthy machine — and treats it as evidence: exported, hashed, named, registered. It is the deliverable that satisfies `ICT311203` and it is what PM Task 2 repeats for marks.

## What you need

- PowerShell
- A folder `C:\Evidence\Day_05\` — create it in step 1

## Before class

Run the whole sequence once. Confirm the CSV is written and `Get-FileHash` returns a hash.

## The steps

**1. Make the evidence folder:**

```powershell
New-Item -ItemType Directory -Force -Path C:\Evidence\Day_05 | Out-Null
```

**2. Export the four baseline lists to CSV:**

```powershell
Get-Process       | Select-Object Name, Id, Path, Company | Sort-Object Name | Export-Csv C:\Evidence\Day_05\baseline_processes.csv -NoTypeInformation
Get-Service       | Select-Object Name, Status, StartType | Export-Csv C:\Evidence\Day_05\baseline_services.csv  -NoTypeInformation
Get-ScheduledTask | Select-Object TaskName, TaskPath, State | Export-Csv C:\Evidence\Day_05\baseline_tasks.csv    -NoTypeInformation
Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location | Export-Csv C:\Evidence\Day_05\baseline_autoruns.csv -NoTypeInformation
```

**What you will see:** four CSV files created, no error.

> "That is a baseline. It says what this machine looked like today, when it was healthy. In three weeks, when something new appears, this file is the only thing that can tell you it is new."

**3. Check the machine's health — this is the maintenance element, and it is the same check the core unit will use from Day 7:**

```powershell
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
Get-PSDrive C | Select-Object @{n='UsedGB';e={[math]::Round($_.Used/1GB,1)}}, @{n='FreeGB';e={[math]::Round($_.Free/1GB,1)}}
```

**What you will see:** Defender enabled/true, the signature date, and free space on C.

> "Antivirus on, signatures recent, disk not full. That is maintenance. It is also, word for word, the 'is the security solution operational' check you will do on real alerts from Day 7."

**4. Hash the baseline, so any later change is provable:**

```powershell
Get-FileHash C:\Evidence\Day_05\baseline_processes.csv -Algorithm SHA256
```

**What you will see:** a 64-character SHA-256 hash.

> "Same idea as Day 3. The hash is the fingerprint of this exact file. If one byte changes, the hash changes. That is how you prove your evidence has not been altered."

**5. Name and register it** *(say it, don't retype — they do this in PM Task 2):*

> "This afternoon you will rename these to the Day 3 convention — date, ticket, host, description — and log them in your evidence register. Exporting, hashing, naming and registering is the whole of the computer-operations unit, done properly."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "What is a baseline for?" | To answer 'is this new?' later — you compare against it |
| "Why hash the CSV?" | To prove it has not been altered since capture |
| "What does `Get-MpComputerStatus` tell you that matters on a real alert?" | Whether the security solution is installed, on, and up to date |

## Common problems

| Problem | Fix |
|---------|-----|
| `Get-MpComputerStatus` errors | Defender may be replaced by third-party AV on that machine. Show it on yours; note the equivalent is that vendor's console |
| `Export-Csv` "access denied" | The folder is protected. Use a path under the user's own profile, e.g. `$env:USERPROFILE\Evidence\Day_05` |
| Hash looks different on two machines | Correct — different machines have different processes, so different files, so different hashes. That is the point of a fingerprint |

---
---

# DEMONSTRATION 3 — YOUR ADDRESS AND THE WIRE
### 9:05 AM · ~15 minutes · Slide 6 · Topic 5.3 · Knowledge 1.4

## Why this demonstration exists

An address and a port are half of every alert. The class must be able to read their own address, say whether it is private or public, find their gateway, and test whether a port is reachable. All of it on their own machine.

## What you need

- PowerShell (or Command Prompt — every command here works in both)
- Internet access, for the public-IP step

## The steps

**1. Show your own addressing:**

```powershell
ipconfig /all
```

**What you will see:** for each adapter, an IPv4 address, a subnet mask, and a Default Gateway.

> "Find your IPv4 address. Mine is 192.168-something. That is a private address — it means I am inside a network, behind a router. The internet cannot reach it directly."

**2. Teach the private ranges** *(point at the slide):*

> "Three ranges are private: 10-dot-anything, 172-dot-16 through 31, and 192-dot-168. And 127-dot-0-0-1 is always this machine — localhost. If your address starts with one of those, you are inside. Anything else is a public, internet-routable address."

**3. Show the gateway and what is beyond it:**

```powershell
Test-NetConnection
```

**What you will see:** it pings the default route and reports the gateway and whether it responded.

> "The gateway is the door out of your network. Everything you send to the internet goes through it, and it does the translation — NAT — between my private address and the one public address my whole network shares."

**4. Resolve a name to an address:**

```powershell
nslookup tesda.gov.ph
```

**What you will see:** the server used, then one or more addresses for the name.

> "DNS turns a name into an address. Every web request starts here. If DNS is pointed somewhere it should not be, every request goes to the wrong place — which is why DNS itself is something analysts watch."

**5. Test whether a port is open:**

```powershell
Test-NetConnection tesda.gov.ph -Port 443
```

**What you will see:** `TcpTestSucceeded : True`.

> "Port 443 is HTTPS — secure web. This says the door for encrypted web traffic is open on that host. Try port 25 and it will almost certainly fail, because they do not run mail there. A port is which service, on which host."

**6. Trace the path** *(optional, can be slow — skip if behind):*

```powershell
tracert -h 10 tesda.gov.ph
```

> "Each line is one hop between here and there. The first hop is almost always your own gateway."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "Is your address private or public? How do you know?" | Private if it starts 10 / 172.16–31 / 192.168 |
| "What does the gateway do?" | It is the way out, and it does NAT between private and public |
| "Port 443 is which service?" | HTTPS — encrypted web |

## Common problems

| Problem | Fix |
|---------|-----|
| `Test-NetConnection` is slow or blocked | Corporate firewalls block ICMP. Use the `-Port` form, which uses TCP and usually works |
| `nslookup` returns a private DNS server | Normal on a managed network. Say so — it is the company's own resolver |
| A trainee has a public IPv4 directly | Rare, but possible on some connections. Use it as the teaching contrast: "you are directly on the internet — most of us are not" |

## If you are offline

`ipconfig /all` and the private-range teaching work with no internet. Skip the `nslookup`, `Test-NetConnection -Port` and `tracert` steps and use the fallback screenshots in `Day_5_Resources.md`.

---
---

# DEMONSTRATION 4 — WHO OWNS THIS CONNECTION
### 9:25 AM · 15 minutes · Slide 7 · Topic 5.3 · Knowledge 1.4 · closes the WKS-311 gap

## Why this demonstration exists

**This is the most important demo of the day.** It is the command that would have finished the Day 3 WKS-311 ticket. The class must leave able to take a connection and name the **process** that owns it.

## What you need

- PowerShell
- **TCPView** from the USB drive (optional but excellent for this)

## The steps

**1. Recall the Day 3 gap out loud, first:**

> "On Day 3 the alert said WKS-311 was talking to a bad address on port 443. We looked up the address. But nobody could say which *program* was making the connection. That was the hole in the ticket. This is how you fill it."

**2. List connections with their owning process ID:**

```
netstat -ano | findstr ESTABLISHED
```

**What you will see:** columns of Local Address, Foreign Address, State, and a **PID** in the last column.

> "The last column is a PID — a process ID. It says which running program owns this connection. Now I turn that number into a name."

**3. Turn a PID into a name** *(pick a PID from your own output):*

```
tasklist /fi "pid eq 1234"
```

**What you will see:** the image name for that PID.

**4. Do it in one step in PowerShell — this is the line to remember:**

```powershell
Get-NetTCPConnection -State Established |
  Select-Object LocalPort, RemoteAddress, RemotePort,
    @{Name='Process'; Expression={ (Get-Process -Id $_.OwningProcess).ProcessName }} |
  Format-Table -AutoSize
```

**What you will see:** connections with the **process name already attached** — no PID lookup needed.

> "Address, port, and the program that owns it, in one line. If I run this on WKS-311, I get svhost32.exe sitting on that connection to the bad address — and now the ticket is complete."

**5. Show TCPView** *(if available):*

> "TCPView does the same thing live, with names already filled in and new connections highlighted as they appear. Same information, easier to watch."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "In `netstat -ano`, what is the last column?" | The PID — the process that owns the connection |
| "What did this demo let us do that Day 3 could not?" | Name the process behind the WKS-311 connection |
| "The local port is 52210 and the remote port is 443. Which is the service?" | The remote one — 443, HTTPS. The local high number is just this end |

## Common problems

| Problem | Fix |
|---------|-----|
| `findstr` shows nothing | You may have no ESTABLISHED connections at that instant. Open a website first, then re-run |
| `Get-Process -Id` errors for a PID | The process ended between the two commands. Re-run; note this is why TCPView's live view is handy |
| TCPView flags itself / lots of svchost | Normal. svchost from System32 owning connections is Windows doing its job |

## If you are offline

Open `python -m http.server 8000` in one window and browse to it in another — that creates a local connection you can then find with `netstat -ano`. No internet needed.

---
---

# DEMONSTRATION 5 — NAT, PORT FORWARDING, AND THE LOCALHOST-ONLY SCAN
### 10:15 AM · ~10 minutes · Slide 9 · Topic 5.3 · Knowledge 1.4 · RA 10175

## Why this demonstration exists

Two ideas the class needs and one rule they must never forget. NAT and port forwarding explain how internal services get exposed; the localhost-only scan teaches discovery **without** teaching them to scan things that are not theirs.

## What you need

- The router NAT/port-forwarding screenshot in `Day_5_Resources.md` (do **not** log into a live router in class)
- **Nmap** on the trainer machine only (optional). If you do not have it, the screenshot fallback is complete

## The steps

**1. Explain NAT with the addresses from Demo 3:**

> "Twenty machines in this building, all with private 192.168 addresses, and one public address the whole network shares. NAT is the translation the router does so all twenty can reach the internet through that one address. Outbound, it is automatic and safe."

**2. Explain port forwarding from the screenshot:**

> "Port forwarding is the opposite, and it is deliberate. It maps a port on the public address to one specific internal machine — so the world can reach an internal server. It is how you host a website from inside. It is also how an internal machine ends up exposed by mistake. When you review a network, forwarded ports are the first thing you look at."

**3. The scan — and the rule, first:**

> "I am about to scan a machine. There is exactly one machine I am allowed to scan without written authorisation: **my own**. Scanning any other machine or network without permission is illegal access under RA 10175, the Cybercrime Prevention Act. Not rude — illegal. So I scan 127.0.0.1, which is this machine, and nothing else."

```
nmap -sT 127.0.0.1
```

**What you will see:** a short list of open ports on your own machine, if any.

> "That is discovery — finding which doors are open on a host. On the lab subnet, on the first day on site, with written authorisation, you will do this properly across real targets. Today, only localhost."

**4. Name the deferred work** *(say it):*

> "The full authorised lab-subnet sweep is on our outstanding list, with the lab safety documents from Day 1. It needs the physical lab and a signed authorisation, so it waits for the first on-site day. That is not us being cautious for no reason — it is the law and the SOP."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "What is the one machine you may scan without authorisation?" | Your own — `127.0.0.1` |
| "What law makes scanning someone else's machine an offence?" | RA 10175, the Cybercrime Prevention Act |
| "What is port forwarding, and why does a reviewer care?" | A deliberate hole from the public address to an internal host — it is how internal services get exposed |

## If Nmap is not installed

The screenshot fallback in Resources shows a localhost scan result. Walk it and say the same words. The rule matters more than the tool.

---
---

# DEMONSTRATION 6 — A WEB REQUEST, END TO END
### 10:25 AM · ~15 minutes · Slide 10 · Topic 5.4 · Knowledge 1.2

## Why this demonstration exists

The class needs to see, on their own machine, that a web request is a plain exchange: a method, a path, a status code — and that the server writes down every one. It sets up Activity 3, where they read an attack out of exactly this kind of log.

## What you need

- Python 3 (for `http.server`)
- A browser with developer tools (any modern browser)

## The steps

**1. Start a tiny web server in a folder that has a file or two:**

```
cd %USERPROFILE%\Documents
python -m http.server 8000
```

**What you will see:** `Serving HTTP on :: port 8000 ...` and the window now waits.

> "That is a real web server, running on my own machine, on port 8000. Nothing leaves this laptop — 8000 on localhost. Watch this window; it is the access log, live."

**2. In the browser, open developer tools first (`F12`), go to the Network tab, then visit:**

```
http://localhost:8000
```

**What you will see:** in the browser, a directory listing; in DevTools, a request with **Status 200**; in the server window, a log line ending in `200`.

> "One request. In the browser I see the page. In DevTools I see the request and a 200 — OK. And in the server window, the server wrote it down. Every visit is one line."

**3. Ask for something that is not there:**

```
http://localhost:8000/does-not-exist.html
```

**What you will see:** an error page, **Status 404**, and a `404` line in the server window.

> "404 — not found. I asked for a page that is not there. One 404 is nothing. Now imagine a hundred of them, from one address, all asking for admin and backup and dot-git. That is somebody trying doors. Hold that thought for the next activity."

**4. Show the headers with curl:**

```
curl.exe -I http://localhost:8000
```

**What you will see:** the response headers, starting `HTTP/1.0 200 OK`, server type, content length.

> "Same request, no browser. The status line is the first thing every response carries. Analysts read these all day."

**5. Name the request path and the WAF** *(point at slide 10):*

> "In the real world your request goes browser, DNS, then usually through a WAF — a web application firewall — and a proxy before it reaches the application. The WAF is what turns a hostile request into a 403 before the app ever sees it. Remember 403: forbidden, usually the WAF or a permission saying no."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "What does a 404 mean, and when is it suspicious?" | Not found — suspicious in bursts from one address hunting paths |
| "What does a 403 usually mean?" | Forbidden — often the WAF or a permission blocking the request |
| "Where does the server write down every request?" | The access log — the window we watched |

## Common problems

| Problem | Fix |
|---------|-----|
| `python -m http.server` says port in use | Use `8080` and browse `http://localhost:8080`. Any free port works |
| Browser caches and shows no new request | Hard-refresh (`Ctrl`+`F5`), or tick "Disable cache" in the DevTools Network tab |
| `curl` not found | Use `curl.exe` explicitly (built into Windows 10/11); or show the headers in the DevTools Network tab instead |

## If you are offline

Everything here is localhost — **no internet is needed at all.** This demo works identically with the network unplugged. That is worth saying to the class.

---
---

# DEMONSTRATION 7 — THE TWENTY-LINE PARSER
### 11:05 AM · ~10 minutes · Slide 12 · Topic 5.5 · Knowledge 1.3

## Why this demonstration exists

The class must see that "a script" is just readable instructions, and that running a good script on the attack log turns forty lines into a two-line verdict. It sets up Activity 4 (reading scripts) and PM Task 7 (extending this one).

## What you need

- Python 3
- `Day_5_log_parser.py` and `Day_5_access_log.txt` in the same folder

## Before class

Run it once and confirm the numbers:

```
python Day_5_log_parser.py Day_5_access_log.txt
```

You must see status **200=27, 302=2, 304=1, 403=3, 404=7**, and top IP **203.0.113.45 = 14**.

## The steps

**1. Open the parser in a text editor and walk it in five parts** *(the five parts are laid out in `Day_5_Sample_Data.md` §3 — read them in order):*

> "Do not be afraid of this. Twenty lines. Import three tools, define one pattern that pulls the pieces out of a log line, open the file, count status codes and addresses, print. That is the whole thing. You can read it."

**2. Run it on the attack log:**

```
python Day_5_log_parser.py Day_5_access_log.txt
```

**What you will see:**
```
Requests by status code:
  200  27
  302  2
  304  1
  403  3
  404  7
Requests by IP address:
  203.0.113.45     14
  198.51.100.23    10
  203.0.113.10     7
  203.0.113.11     4
  192.0.2.77       3
  203.0.113.12     2
```

> "Forty lines of log, and now I can see it. One address made fourteen requests — 203.0.113.45. Another made ten and threw a lot of 404s — that is a scanner. This is what a script does for you: it does not judge, it counts, so you can judge."

**3. Show the same job in PowerShell, so they see it is not a Python-only trick:**

```powershell
Get-Content .\Day_5_access_log.txt | ForEach-Object { ($_ -split ' ')[8] } | Group-Object | Sort-Object Name | Select-Object Count, Name
```

**What you will see:** the same status-code counts, from PowerShell.

> "Python, PowerShell, or bash — the job is the same: read the file, count the field. Pick whichever your desk has."

**4. Set up the afternoon:**

> "This afternoon you will add one thing to this script: count the 404s *per address*, and flag any address over a threshold. That is how you make the scanner jump out automatically. The file is yours; you edit it."

## Checkpoint questions

| Ask | The answer you want |
|-----|--------------------|
| "What does the parser actually do — in one sentence?" | Reads the log line by line and counts status codes and addresses |
| "Which address looks like a scanner, and why?" | `198.51.100.23` — ten requests, many of them 404s |
| "Does the script decide anything?" | No — it counts. The analyst decides |

## Common problems

| Problem | Fix |
|---------|-----|
| `python` not recognised | Try `py` instead of `python`, or use the full path. On the day, a trainee without Python does Task 7 by hand |
| Numbers do not match | The log file was edited. Re-copy `Day_5_access_log.txt` from the pack |
| `sys.argv[1]` IndexError | The filename was not passed. The command is `python Day_5_log_parser.py Day_5_access_log.txt` — two names |

---
---

# DEMONSTRATION 8 — A 60-SECOND CAPTURE *(optional)*
### If ahead · 5 minutes · Topics 5.3 / 5.4

## Only run this if you are ahead of time

Wireshark is not required for the qualification, and trainees do **not** install it. This is a "look what is really on the wire" moment, nothing more.

## What you need

- Wireshark + Npcap on the **trainer** machine only
- A screenshot fallback in `Day_5_Resources.md` if you skip the live capture

## The steps

**1. Start a capture on your active adapter, then in a browser hit `http://localhost:8000` (your Demo 6 server).**

**2. Stop after a few seconds. In the filter bar type `http` then `dns`.**

> "Every request we have talked about, as the actual packets. There is the DNS question turning a name into an address, and there is the HTTP GET with the path in plain text. On 443 this would be encrypted — you would see the connection but not the content. That is why on Day 3 all we could read about WKS-311 was the address."

**3. Stop there.** Do not go down a Wireshark rabbit hole; it is above L1.

## If you are offline

Use the fallback screenshot. The single teaching point — plaintext HTTP versus encrypted HTTPS — shows perfectly in a still image.

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

The single most valuable hour you will spend on Day 5. Network output is different on every machine, so you **must** have seen yours.

## Screen and platform
- [ ] Terminal font large, notifications off, desktop clean
- [ ] Decide: share whole screen (clean desktop) or switch windows

## Every demo, run once, end to end
- [ ] Demo 1 — `Get-Process`, find your real `svchost` path, list services and tasks
- [ ] Demo 2 — create `C:\Evidence\Day_05`, export all four CSVs, `Get-MpComputerStatus`, hash one file
- [ ] Demo 3 — `ipconfig /all`, find your private address and gateway, `nslookup`, `Test-NetConnection -Port 443`
- [ ] Demo 4 — `netstat -ano`, turn one PID into a name, run the one-line PowerShell join
- [ ] Demo 5 — open the router screenshot; `nmap -sT 127.0.0.1` if you have Nmap
- [ ] Demo 6 — start `http.server`, make a 200 and a 404, watch the log, `curl.exe -I`
- [ ] Demo 7 — run the parser, confirm 200=27 / 404=7 / top IP 203.0.113.45=14, run the PowerShell version
- [ ] Optional Demo 8 — one capture, `http` and `dns` filters

## The three sentences you should be able to say without notes
1. **The real svchost lives in System32 — location is evidence.**
2. **`netstat -ano` plus the process name is the line that finishes the WKS-311 ticket.**
3. **Read a suspicious script, never run it; scan only a machine you are authorised to scan.**
