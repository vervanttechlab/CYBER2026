# DAY 06 — DEMONSTRATION GUIDE
## Every demonstration, click by click, for the trainer
### For a trainer running Day 06 for the first time, to complete beginners

---

## READ THIS FIRST

Assumes nothing. **No server** — the capture is of your own browsing, the web server runs on your own machine, the firewall log is a supplied file. **Total beginners** — every click shown, calm pace.

| Style | Meaning |
|-------|---------|
| **Numbered step** | Something you do, in order |
| `code` | Type or click exactly this |
| > Grey quote | Words you say |
| *(Italic)* | A note for you — never read aloud |
| **What you will see** | What should appear |

**Five demonstrations:**

| # | Demonstration | When | Topic |
|---|--------------|------|-------|
| **1** | Read the wire — one live minute, four filters | 8:15 | 6.1 |
| **2** | The web server from both sides — four status codes on purpose | 8:55 | 6.2 |
| **3** | Ports, NAT and the router — your port map, the lab subnet, the forwards | 9:40 | 6.3 |
| **4** | The firewall log — the real one for ten seconds, then the supplied file | 10:25 | 6.4 |
| **5** | Parser v2 — read it, run it on both logs, change one line | 11:05 | 6.5 |

Screen setup as Days 04–05: clean desktop, large text, notifications off, narrate, slow down. **Before 8:00 have open:** Wireshark (Npcap installed, adapter chosen), two PowerShell windows (one in `Documents\www`), a browser, and the `Day_06` folder with the two files.

> **The one rule you must SAY today, before the capture starts:** *you capture only your own machine's traffic, on a network you own or are authorised on — never a colleague's, never the office's.* It is the same rule as Day 04's localhost-only scan, and it is a professional-conduct rule, not a technical one.

---
---

# DEMONSTRATION 1 — READ THE WIRE
### 8:15 AM · Slides 3–4 · Topic 6.1 · knowledge 1.4

## Why this exists
Day 04 gave the class a five-minute glimpse. Today they see one minute of packets read properly — and learn that five things are findable in any capture.

## What you need
- Wireshark + Npcap on **your** machine; the practice server already running (`python -m http.server 8000` in `Documents\www`)
- The packet list (Sample Data §1) on the second screen — it is the paper version of what you are about to do
- Fallback screenshots (Resources Part 3) in case the capture misbehaves

## The steps
**1. Say the rule, then start the capture.**
> "One rule before I click anything. I am capturing my own machine's traffic, on my own network. You never capture a colleague's traffic, or the office's, without written authorisation. Same as Day 04's scan: only what is yours."

Open Wireshark → double-click your active adapter (Wi-Fi or Ethernet). **What you will see:** lines scrolling immediately — background noise.
> "Already busy — Windows talks constantly. We are going to make three things happen and then find them."

**2. Make the traffic.** In the browser: open `https://www.example-client.ph` *(any HTTPS site you trust — say which)*, then `http://localhost:8000/about.html`, then `http://localhost:8000/nothere.html`. Wait ten seconds. Click the red square to **stop**.

*(Note: localhost traffic may not appear on the Wi-Fi adapter. If it does not, capture on the "Adapter for loopback traffic capture" that Npcap installs, or simply use the paper list for packets 13–21 — say so.)*

**3. Filter one — the name lookup.** In the green filter bar type `dns` → Enter.
**What you will see:** pairs of lines — *Standard query A …* and *Standard query response … A 203.0.113.80*.
> "A name is one question and one answer. Your machine asked the router: what is the address of this name? The router answered. That answer is the first thing you find in any capture — because it tells you the name that goes with the address."

**4. Filter two — every new connection.** Type `tcp.flags.syn==1 && tcp.flags.ack==0` → Enter.
**What you will see:** one line per connection attempt — SYN only.
> "A connection starts with a SYN. This filter shows every *attempt* — including the ones that never got an answer. Count the destinations. Every one is a place your machine tried to reach."

**5. Filter three — the handshake, for one connection.** Clear the filter; click the first SYN to your HTTPS site; right-click → **Follow → TCP Stream**, then close the pop-up — the filter bar now reads `tcp.stream eq N`.
**What you will see:** SYN, SYN-ACK, ACK — then TLS lines.
> "Three packets. SYN — can we talk? SYN-ACK — yes. ACK — good. That is every TCP connection ever. After it, on port 443, TLS takes over and the content is encrypted."

**6. Filter four — the one readable thing on HTTPS.** Type `tls.handshake.type==1` → Enter. Click the Client Hello; expand *Transport Layer Security → Handshake Protocol → Extension: server_name*.
**What you will see:** the site's name, in plain text.
> "The SNI — Server Name Indication. Even on HTTPS, the very first packet names the site. You cannot read the pages. You can read *where*, *when*, and *how much*. That is usually enough."

**7. Filter five — plaintext, for contrast.** Type `http` → Enter.
**What you will see:** `GET /about.html HTTP/1.1` and `HTTP/1.0 200 OK`, then `GET /nothere.html` and `404`.
> "Port 8000, no encryption — every word readable. This is why HTTP is dead on the internet and why the Day 04 access log could show us paths. Same requests you will make yourself in ten minutes."

**8. The unanswered one** *(paper — packets 22–24):*
> "Look at the printed list, lines 22 to 24. A SYN to 185.220.101.1, port 443. No SYN-ACK. Three seconds later, the same SYN again. And again. Nobody answered — but WKS-311 *tried*, three times, to reach a Tor node. That is Day 03's case, seen on the wire. A SYN that is never answered is still a fact."

## Checkpoint questions
| Ask | Answer you want |
|-----|-----------------|
| "How many packets make a connection?" | Three — SYN, SYN-ACK, ACK |
| "On HTTPS, what can you still read?" | The SNI (site name), addresses, times, sizes — not the content |
| "A SYN with no SYN-ACK, repeated — what does it mean?" | Something tried to connect and nothing answered; it is still evidence |

## Common problems
| Problem | Fix |
|---------|-----|
| Npcap not installed / no adapters listed | Fallback screenshots; the paper list carries the activity |
| Localhost traffic invisible | Use the Npcap loopback adapter, or the paper list for 13–21 |
| Too much noise | Type the filter *before* explaining; never scroll unfiltered |
| A trainee asks to install Wireshark | Reading a saved capture needs no admin (WiresharkPortable); capturing needs Npcap (admin) — optional for PM Task 1 |

---
---

# DEMONSTRATION 2 — THE WEB SERVER FROM BOTH SIDES
### 8:55 AM · Slide 6 · Topic 6.2 · knowledge 1.2

## Why this exists
The trainee becomes the server and the client, and makes every status code happen on purpose.

## What you need
- The `www` folder built the night before (Sample Data §2); **two** PowerShell windows side by side

## The steps
**1. Window 1 — the server.**
```powershell
cd "$env:USERPROFILE\Documents\www"
python -m http.server 8000
```
**What you will see:** `Serving HTTP on :: port 8000 (http://[::]:8000/) ...`
> "This window is now a web server. It will print one line for every request anyone makes to it. Leave it alone — it is the log."

**2. Window 2 + browser — the client. Make a 200.** Browser → `http://localhost:8000/about.html`.
**What you will see:** the page; in window 1: `"GET /about.html HTTP/1.1" 200 -`
> "Two hundred. Found it, here it is. Read the server's line: who asked, what for, what it answered."

**3. Make a 404.** Browser → `http://localhost:8000/nothere.html`.
**What you will see:** *Error response 404*; window 1: `"GET /nothere.html HTTP/1.1" 404 -`
> "Four-oh-four. No such file. The client asked for something wrong — 4xx is the *client's* fault."

**4. Make a 301.** Browser → `http://localhost:8000/docs` (no trailing slash).
**What you will see:** the folder listing; window 1 shows **two** lines: `"GET /docs HTTP/1.1" 301 -` then `"GET /docs/ HTTP/1.1" 200 -`
> "Three-oh-one. Moved — it lives at `/docs/` with the slash. The browser followed the redirect automatically, so you saw two lines for one click. 3xx means go elsewhere."

**5. Make a 501.** Window 2:
```powershell
curl.exe -X DELETE http://localhost:8000/
```
**What you will see:** an error page; window 1: `code 501, message Unsupported method ('DELETE')`
> "Five-oh-one. The server does not do that. 5xx is the *server's* side — here, honestly, 'I cannot'. A 500 would be 'I broke'. Both are the server's fault, not the client's."

**6. Headers only.**
```powershell
curl.exe -I http://localhost:8000/about.html
```
**What you will see:** `HTTP/1.0 200 OK` · `Server: SimpleHTTP/0.6 Python/3.x` · `Content-type: text/html`
> "Dash capital I: headers only. Look at *Server:* — the software names itself. On Day 25 a scanner reads this line to guess what to attack. That is why real servers hide it."

**7. Land the rule** *(slide)*:
> "2xx fine. 3xx elsewhere. 4xx — the client asked wrong. 5xx — the server failed. And a burst of 404s from one address is someone guessing filenames — you saw that in Day 04's log."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Whose fault is a 404? A 500?" | The client's; the server's |
| "Why two lines for the /docs click?" | 301 redirect, then the browser fetched /docs/ → 200 |
| "What does `curl.exe -I` show?" | Headers only — including the Server: line |

## Common problems
| Problem | Fix |
|---------|-----|
| Port 8000 in use | `python -m http.server 8080` — and say: a forgotten server is itself a finding |
| `python` not found | `py -m http.server 8000` |
| `curl` without `.exe` behaves oddly | It is PowerShell's alias for Invoke-WebRequest — always `curl.exe` |
| Browser caches the 404 page | Ctrl+F5 |

---
---

# DEMONSTRATION 3 — PORTS, NAT AND THE ROUTER
### 9:40 AM · Slide 8 · Topic 6.3 · knowledge 1.4

## Why this exists
"Which ports are open on my machine and why" — then NAT and a port forward drawn on the lab subnet, with one forward that should not exist.

## What you need
- Your router's port-forwarding page as a **screenshot, private details blurred** (Resources Part 3)
- The lab-subnet table (Sample Data §4) on the slide

## The steps
**1. Your port map.**
```powershell
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess,
    @{n='Process'; e={ (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName }} |
  Sort-Object LocalPort | Format-Table -AutoSize
```
**What you will see:** a short table — 135, 139, 445, 5040, 7680, a few 496xx, and **8000 (python)** because your server is still running.
> "Everything waiting for a connection on this machine. Three questions per row: what is it, who owns it, should it be there. 135, 139, 445 — Windows itself, normal. 5040, 7680 — Windows, normal. 496-something — Windows RPC, normal. And 8000, python — that is *me*, and it should be closed by four o'clock. If I saw 3389 here on a laptop, that would be a finding."

**2. NAT in one line** *(slide — the lab subnet)*:
> "Inside the office, every machine has a 192.168.10 address. Outside, the whole office looks like one address: 203.0.113.5. That is NAT — many inside, one outside. The router keeps the table."

**3. The port forwards** *(your router screenshot, then the slide's table)*:
> "This is my own router's forwarding page — details blurred. A port forward is a hole: traffic arriving at the outside address on one port is sent to one inside machine. Now the lab's two forwards. 443 to the file server, .22 — documented, that is the company website. And 3389 — Remote Desktop — to .31, a *workstation*. Nobody can say who added it. In an hour you will read a firewall log where an outside address is hammering that exact port on that exact machine. This forward is how a workstation ends up on the internet."

**4. Draw the arrow.**
> "Public address and port on the left, private on the right, arrow pointing in. Every forward gets an arrow, and every arrow gets a name of who approved it. No name — it is a finding."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "Three questions for each listening port?" | What is it, who owns it, should it be there |
| "What does NAT do?" | Many inside addresses, one outside address |
| "Which forward is the finding, and why?" | 3389 → .31 — RDP to a workstation, undocumented |

## Common problems
| Problem | Fix |
|---------|-----|
| A trainee's map shows 3389 | A real finding — have them note it as they would report it |
| Process column blank | The owning process needs elevation to read — write the PID and say so |
| No router page available | The slide's table is enough; the screenshot is a nice-to-have |

---
---

# DEMONSTRATION 4 — THE FIREWALL LOG
### 10:25 AM · Slides 10–11 · Topic 6.4 · knowledge 1.5, 1.6

## Why this exists
The first detection source the class reads raw — the firewall's own record of what it allowed and dropped — with four findings hiding in twenty-eight lines.

## What you need
- Firewall logging turned on on **your** machine the night before (admin): `Set-NetFirewallProfile -Profile Domain,Private,Public -LogBlocked True -LogAllowed True`
- `Day_06_pfirewall.log` open in Notepad, large font

## The steps
**1. The real one, for ten seconds** *(admin PowerShell)*:
```powershell
Get-Content "$env:SystemRoot\System32\LogFiles\Firewall\pfirewall.log" -Tail 10
```
**What you will see:** ten lines in the same format as the supplied file.
> "This is my machine's real firewall log. Turning it on and reading it needs admin, which most of you do not have — so we all read the same supplied file. Same format, exactly."

**2. Open `Day_06_pfirewall.log`. Read the header.**
> "Lines starting with a hash are the header. The Fields line is the column names. Date, time, **action**, protocol, **source**, **destination**, source port, **destination port**, size, flags … and at the end, **path** — RECEIVE is inbound, SEND is outbound. Five columns carry the story: action, source, destination, destination port, path."

**3. Read one line aloud, left to right** *(line 08:03:45)*:
> "Eighteenth of September, 08:03:45. DROP. TCP. From 203.0.113.45 — outside. To 192.168.10.31 — WKS-311. Destination port 3389 — Remote Desktop. Flag S — a new connection attempt. RECEIVE — inbound. The firewall dropped it. Now read the next five lines."

**4. Finding one — the rhythm.**
> "Same source, same target, same port — 08:03:45, 48, 51, 54, 57, 08:04:00. Every three seconds. A person does not type that evenly. That is a script trying Remote Desktop, over and over. One source, one port, steady rhythm — a brute-force script."

**5. Finding two — the scan.** *(Lines 08:31:10–12.)*
> "New source, 198.51.100.23. Look at the destination ports: 21, 22, 23, 25, 80, 110, 135, 139, 443, 445, 3389, 8080 — twelve ports in two seconds. And the *source* port never changes: 44001. One source, many destination ports, all SYN — that is a port scanner walking the door handles. Day 04 you ran Nmap against localhost; this is what it looks like from the other side."

**6. Finding three — the one that matters most.** *(Lines 18:41:07–16.)*
> "Now 18:41 — after hours. Source 192.168.10.31 — WKS-311, *inside*. Destination 185.220.101.1, port 443. Path: SEND. Outbound. DROP. Four times. The firewall stopped it — good. But read it again: something *on* WKS-311 tried to reach a Tor node four times at a quarter to seven in the evening. 'Dropped, so fine' is the wrong reading. Dropped outbound means something inside tried. That is the finding — and it is Day 03's WKS-311 case, in a third source."

**7. Finding four — what normal looks like.** *(Lines 08:15:02.)*
> "And two ALLOW lines — WKS-311 to the file server on port 8000. That is somebody using the practice web server. Expected. You need to know what normal looks like to see the rest."

**8. Count it, once, before the parser.**
```powershell
Select-String -Path .\Day_06_pfirewall.log -Pattern " DROP " | Measure-Object | Select-Object Count
```
**What you will see:** `22`.
> "Twenty-two drops. By eye that took us five minutes. In half an hour the parser does it in one second."

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "One source, many destination ports, two seconds?" | A port scan |
| "One source, one port, every three seconds?" | A script — brute force |
| "A DROP with path SEND — fine?" | No — something inside tried to get out; that is the finding |

## Common problems
| Problem | Fix |
|---------|-----|
| Your real log is empty | Logging was just enabled; browse for a minute; or skip step 1 — the supplied file is the lesson |
| Lines wrap in Notepad | Turn off Word Wrap; or open in VS Code / Notepad++ |
| Trainees read src-port as the target | Point at the column header every time |

---
---

# DEMONSTRATION 5 — PARSER v2
### 11:05 AM · Slides 13–14 · Topic 6.5 · knowledge 1.3 · trainees run every step with you

## Why this exists
Day 04's parser read one log. Version 2 reads two. The class reads it, runs it on both files, and changes one line.

## What you need
- `Day_06_fw_parser.py`, `Day_06_pfirewall.log` and Day 04's `Day_5_access_log.txt` in the same folder — everyone's, not just yours

## The steps
**1. Read it first — Day 04's rule.** Open `Day_06_fw_parser.py` in Notepad or VS Code. Scroll slowly.
> "Read before you run. Three parts. Part one — the access-log code from Day 04, exactly the same, just moved into a function. Part two — new: the firewall log. Skip hash lines, split on spaces, take the first eight fields, count. Part three, the last six lines — look at the first line of the file: if it starts with '#Version', it is a firewall log; otherwise, an access log. Does it write anything? No. Does it send anything? No. It reads. Safe to run."

**2. Run it on the firewall log.**
```powershell
python .\Day_06_fw_parser.py .\Day_06_pfirewall.log
```
**What you will see:** the three blocks from Sample Data §6 — `DROP 22`, `198.51.100.23 12`, `3389 7`.
> "One second. Top of the source list: 198.51.100.23, twelve drops — the scan. Second: 203.0.113.45, six — the RDP script. Third: 192.168.10.31, four — the outbound Tor attempts. Top port: 3389. Everything we found by eye in five minutes, in three lines."

**3. Run it on Day 04's access log.**
```powershell
python .\Day_06_fw_parser.py .\Day_5_access_log.txt
```
**What you will see:** Day 04's numbers — `200 27 … 404 7`, top IP `203.0.113.45 14`.
> "Same script, different file, it chose the right part. And look at the top IP: 203.0.113.45. The same address that is hammering RDP in the firewall log is the top requester in the web log — with fourteen requests, seven of them 404s. Two logs, one attacker. Cross-referencing is the whole job."

**4. Change one line.** In the editor find `drop_by_port.most_common(5)` → change `5` to `10` → save → re-run on the firewall log.
**What you will see:** ten ports instead of five.
> "One number. Save. Run. Ten ports. That is how you change a script safely: one line, run, look. If it breaks, change it back."

**5. The second change** *(if time — otherwise PM Task 5)*: add after `drop_by_port = Counter()` a line `drop_by_path = Counter()`; after `drop_by_port[dport] += 1` add `drop_by_path[fields[16]] += 1` *(path is the 17th field)*; add a print block. *(Show, don't require.)*

## Checkpoint questions
| Ask | Answer |
|-----|--------|
| "How does the script know which kind of file it has?" | The first line — `#Version` means firewall |
| "Which address appears at the top of both logs?" | 203.0.113.45 |
| "How do you change a script safely?" | One line, save, run, look; change it back if it breaks |

## Common problems
| Problem | Fix |
|---------|-----|
| `python` not recognised | `py .\Day_06_fw_parser.py …`; or the Store Python; check the night before |
| `FileNotFoundError` | Wrong folder — `cd` to where the files are; `Get-ChildItem` to prove it |
| IndentationError after the edit | They changed the indent, not just the number — undo with Ctrl+Z, retry |

---
---

# YOUR PRACTICE RUN — DO THIS THE NIGHT BEFORE

- [ ] Wireshark + Npcap installed; one capture; all four filters typed and working; Follow → TCP Stream once; find the SNI once
- [ ] Build `Documents\www` (Sample Data §2); start the server; cause 200 / 404 / 301 / 501; read each in the server window; `curl.exe -I` once
- [ ] Run the port-map command; name every listener on your own machine
- [ ] Router page screenshot taken and blurred
- [ ] Firewall logging enabled (admin); `Get-Content … -Tail 10` shows lines
- [ ] `Day_06_fw_parser.py` run on both files; outputs match §6; the `most_common(10)` change made and undone
- [ ] Take the fallback screenshots (Resources Part 3)
- [ ] **Stop your server** when you finish — then check the port map shows no 8000

## The three sentences you should be able to say without notes
1. **A connection is three packets; a name is one question and one answer; on HTTPS only the SNI is readable.**
2. **2xx fine · 3xx elsewhere · 4xx the client's fault · 5xx the server's fault.**
3. **One source, many ports = a scan; one source, one port, steady rhythm = a script; outbound after hours = ask why.**
