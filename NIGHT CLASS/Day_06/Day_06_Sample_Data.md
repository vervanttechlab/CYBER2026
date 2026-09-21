# DAY 06 — SAMPLE DATA
## The packet list, the status-code recipes, the port map, the lab subnet, the firewall log, and parser v2
### Trainer, and trainees where marked.

> **Safety note.** Nothing today touches malware or anyone else's network. The only capture is of **your own** browsing; the only web server is one **you** run on your own machine; the only port scan is the localhost-only one from Day 04. The packet list and the firewall log are **on paper** — written to look real. Addresses use documentation-only ranges (`203.0.113.x`, `198.51.100.x`), the lab subnet `192.168.10.0/24`, and the Day 03 Tor node `185.220.101.1`.

> **Two files ship with this day** (in the `Day_06` folder): **`Day_06_pfirewall.log`** — the firewall log the class reads — and **`Day_06_fw_parser.py`** — parser v2. Trainees also need Day 04's `Day_5_log_parser.py` and `Day_5_access_log.txt`.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The packet list (paper capture) and the four filters | Demo 1, Activity 1, PM Task 1 |
| 2 · The web server from both sides — status-code recipes | Demo 2, Activity 2, PM Task 3 |
| 3 · The port map — what a healthy Windows machine listens on | Demo 3, Activity 3, PM Task 2 |
| 4 · The lab subnet and the router's port forwards | Demo 3, PM Task 2 |
| 5 · The firewall log — format and the findings in it | Demo 4, Activity 4, PM Task 4 |
| 6 · Parser v2 — what changed from Day 04 | Demo 5, PM Task 5 |
| 7 · The commands trainees run | all |

---
---

# 1 — THE PACKET LIST (PAPER CAPTURE) AND THE FOUR FILTERS
### Demo 1 captures live on the trainer's machine; the class works from this list. It is what Wireshark's packet list shows for one minute of browsing from WKS-311.

**Client:** `192.168.10.31` (WKS-311) · **DNS:** `192.168.10.1` (the router) · **Website:** `www.example-client.ph` = `203.0.113.80` · **Practice web server:** `192.168.10.22:8000` (SRV-FILE-01, running `python -m http.server`).

```
No.  Time      Source           Destination      Proto  Info
 1   0.000000  192.168.10.31    192.168.10.1     DNS    Standard query 0x1a2b A www.example-client.ph
 2   0.018420  192.168.10.1     192.168.10.31    DNS    Standard query response 0x1a2b A www.example-client.ph A 203.0.113.80
 3   0.019105  192.168.10.31    203.0.113.80     TCP    51402 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
 4   0.041377  203.0.113.80     192.168.10.31    TCP    443 → 51402 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
 5   0.041450  192.168.10.31    203.0.113.80     TCP    51402 → 443 [ACK] Seq=1 Ack=1 Win=64240 Len=0
 6   0.042010  192.168.10.31    203.0.113.80     TLSv1.3 Client Hello (SNI=www.example-client.ph)
 7   0.066882  203.0.113.80     192.168.10.31    TLSv1.3 Server Hello, Change Cipher Spec, Application Data
 8   0.068100  192.168.10.31    203.0.113.80     TLSv1.3 Change Cipher Spec, Application Data
 9   0.070455  192.168.10.31    203.0.113.80     TLSv1.3 Application Data
10   0.101203  203.0.113.80     192.168.10.31    TLSv1.3 Application Data
11   0.101950  203.0.113.80     192.168.10.31    TLSv1.3 Application Data
12   0.102001  192.168.10.31    203.0.113.80     TCP    51402 → 443 [ACK] Seq=1234 Ack=5678 Win=64240 Len=0
13   4.210000  192.168.10.31    192.168.10.22    TCP    51410 → 8000 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
14   4.210311  192.168.10.22    192.168.10.31    TCP    8000 → 51410 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
15   4.210340  192.168.10.31    192.168.10.22    TCP    51410 → 8000 [ACK] Seq=1 Ack=1 Win=64240 Len=0
16   4.210900  192.168.10.31    192.168.10.22    HTTP   GET /about.html HTTP/1.1
17   4.213402  192.168.10.22    192.168.10.31    HTTP   HTTP/1.0 200 OK  (text/html)
18   4.214001  192.168.10.31    192.168.10.22    TCP    51410 → 8000 [FIN, ACK] Seq=310 Ack=4501 Win=64240 Len=0
19   4.214220  192.168.10.22    192.168.10.31    TCP    8000 → 51410 [FIN, ACK] Seq=4501 Ack=311 Win=65535 Len=0
20   9.500000  192.168.10.31    192.168.10.22    HTTP   GET /nothere.html HTTP/1.1
21   9.502110  192.168.10.22    192.168.10.31    HTTP   HTTP/1.0 404 File not found  (text/html)
22  41.007000  192.168.10.31    185.220.101.1    TCP    52001 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460
23  44.010000  192.168.10.31    185.220.101.1    TCP    [TCP Retransmission] 52001 → 443 [SYN] Seq=0 Win=64240 Len=0
24  47.014000  192.168.10.31    185.220.101.1    TCP    [TCP Retransmission] 52001 → 443 [SYN] Seq=0 Win=64240 Len=0
```

**The four display filters** *(type each into Wireshark's green filter bar)*:

| Filter | Shows | On the list above |
|--------|-------|-------------------|
| `dns` | Name lookups — the question and the answer | 1, 2 |
| `tcp.flags.syn==1 && tcp.flags.ack==0` | Every **new connection attempt** (the first SYN) | 3, 13, 22, 23, 24 |
| `tls.handshake.type==1` | Client Hello — the **SNI** names the site even though the rest is encrypted | 6 |
| `http` | Plaintext web requests and responses — readable only on HTTP, never on HTTPS | 16, 17, 20, 21 |

**The five things to find** *(Activity 1 questions)*: (1) the DNS answer for the site; (2) the three packets of the handshake to it; (3) the one packet that names the site in plain text even on HTTPS; (4) a request and its response you can read word for word; (5) a connection that was **tried and never answered** — and where to.

---
---

# 2 — THE WEB SERVER FROM BOTH SIDES — STATUS-CODE RECIPES
### Demo 2 and Activity 2 (observed). Python's `http.server` on your own machine; the browser and `curl.exe` as the client.

**Set-up (one folder, four things in it):**
```powershell
New-Item -ItemType Directory "$env:USERPROFILE\Documents\www\docs" -Force | Out-Null
Set-Content "$env:USERPROFILE\Documents\www\index.html" "<h1>Practice server</h1>"
Set-Content "$env:USERPROFILE\Documents\www\about.html" "<p>About page</p>"
Set-Content "$env:USERPROFILE\Documents\www\docs\readme.txt" "hello"
cd "$env:USERPROFILE\Documents\www"
python -m http.server 8000
```
*(Leave that window open — it is the **server**, and every request prints there as a log line. Open a second PowerShell window as the **client**.)*

**Make each code happen on purpose:**

| Code | Meaning | How to cause it | What the server window logs |
|------|---------|-----------------|-----------------------------|
| **200** OK | Found it, here it is | Browser → `http://localhost:8000/about.html` | `"GET /about.html HTTP/1.1" 200 -` |
| **404** Not Found | No such file | Browser → `http://localhost:8000/nothere.html` | `"GET /nothere.html HTTP/1.1" 404 -` |
| **301** Moved Permanently | It lives at a different address (here: a folder without the trailing `/`) | Browser → `http://localhost:8000/docs` | `"GET /docs HTTP/1.1" 301 -` then `"GET /docs/ HTTP/1.1" 200 -` |
| **501** Not Implemented | The server does not do that method | `curl.exe -X DELETE http://localhost:8000/` | `code 501, message Unsupported method ('DELETE')` |
| **403** Forbidden | Exists, but you may not have it | *(paper — `http.server` rarely produces it)* | In Day 04's Apache log: `"GET /admin/ HTTP/1.1" 403` |
| **500** Internal Server Error | The server broke while answering | *(paper)* | `"POST /login HTTP/1.1" 500` — the server's fault, not the client's |

**The headers only, without the page** — `curl.exe -I http://localhost:8000/about.html` → `HTTP/1.0 200 OK`, `Server: SimpleHTTP/0.6 Python/3.x`, `Content-type: text/html`. *(The `Server:` header is what a scanner reads on Day 25 to guess the software.)*

**The rule to teach:** **2xx** = fine · **3xx** = go elsewhere · **4xx** = the *client* asked for something wrong · **5xx** = the *server* failed. A burst of 404s from one address is someone guessing filenames; a 500 after a strange request is someone breaking things.

---
---

# 3 — THE PORT MAP — WHAT A HEALTHY WINDOWS MACHINE LISTENS ON
### Demo 3, Activity 3, PM Task 2. Trainees run this on their own machine and name each listener.

```powershell
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess,
    @{n='Process'; e={ (Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName }} |
  Sort-Object LocalPort | Format-Table -AutoSize
```

**What most machines show, and what each is:**

| Port | Process | What it is | Expected on a workstation? |
|------|---------|-----------|----------------------------|
| 135 | svchost (RpcSs) | Windows RPC endpoint mapper | Yes |
| 139 | System (PID 4) | NetBIOS session — file sharing | Yes (old, but normal) |
| 445 | System (PID 4) | SMB — file and printer sharing | Yes — and the most-attacked port on Windows |
| 5040 | svchost (CDPSvc) | Connected Devices Platform | Yes |
| 5357 | System | WSD — network discovery | Often |
| 7680 | svchost (DoSvc) | Delivery Optimization (Windows Update sharing) | Often |
| 49664–49670 | wininit, lsass, services, svchost | RPC dynamic ports | Yes |
| **3389** | svchost (TermService) | **Remote Desktop** | **Only if someone turned it on — on a laptop this is a finding** |
| **8000 / 8080** | python | **A web server** | Only while you are running one — close it after class |
| anything else | ? | — | Name it or note it |

**The three questions for every row:** *what is it · who owns it · should it be there?*

---
---

# 4 — THE LAB SUBNET AND THE ROUTER'S PORT FORWARDS
### Demo 3 and PM Task 2. The network the Phase B cases live on. Draw it; you will meet every host again.

**`192.168.10.0/24` — gateway `192.168.10.1`, public side `203.0.113.5`**

| Address | Host | Role | Notes |
|---------|------|------|-------|
| .1 | Router | Gateway, DNS forwarder, NAT | Its page: `http://192.168.10.1` (screenshot in Resources) |
| .20 | SRV-FIN-02 | Finance file server | You will meet it on Day 10 |
| .21 | SRV-BAK-02 | Backup server | The running case from Day 10 onward |
| .22 | SRV-FILE-01 | File server; runs the practice web server on **:8000** for this day | |
| .31 | WKS-311 | Marketing workstation | Day 03's Tor-node case |
| .118 | WKS-118 | Marketing workstation | |
| .205 | WKS-205 | Workstation | |
| .107 | TRN-PC-07 | Training PC | |

**Port forwards configured on the router** *(from its "Virtual Server / Port Forwarding" page)*:

| Public | → Private | Intended? |
|--------|-----------|-----------|
| `203.0.113.5:443` → `192.168.10.22:443` | The company web site | **Yes** — documented |
| `203.0.113.5:3389` → `192.168.10.31:3389` | Remote Desktop **to a workstation** | **No** — nobody can say who added it. This is why `203.0.113.45` is hammering port 3389 in the firewall log |

**What NAT means, in one line:** inside, everyone has a `192.168.10.x` address; outside, the whole office looks like `203.0.113.5`. A **port forward** is a hole punched from outside to one inside machine — every one must be documented, and this one is not.

---
---

# 5 — THE FIREWALL LOG — FORMAT AND THE FINDINGS IN IT
### Demo 4, Activity 4, PM Task 4. The file is `Day_06_pfirewall.log`. It is what Defender Firewall writes when logging is on.

**Where the real one lives:** `%systemroot%\system32\LogFiles\Firewall\pfirewall.log`. **Turning logging on** (needs admin — the trainer does it; trainees read the supplied file):
```powershell
Set-NetFirewallProfile -Profile Domain,Private,Public -LogBlocked True -LogAllowed True -LogMaxSizeKilobytes 4096
```
*(GUI: `wf.msc` → Windows Defender Firewall Properties → each profile tab → Logging → Customize → Log dropped packets: Yes.)*

**The format** — W3C, space-separated, one record per line, header lines start with `#`:
```
#Fields: date time action protocol src-ip dst-ip src-port dst-port size tcpflags tcpsyn tcpack tcpwin icmptype icmpcode info path
2026-09-18 08:03:45 DROP TCP 203.0.113.45 192.168.10.31 51234 3389 52 S 3311204418 0 65535 - - - RECEIVE
```
**Read it left to right:** date · time · **action** (ALLOW / DROP) · protocol · **source** · **destination** · source port · **destination port** · size · flags (`S` = SYN, a new connection attempt) · … · **path** (RECEIVE = inbound, SEND = outbound).

**The four findings in the supplied file** *(Activity 4 — teams find them; answers in Solutions)*:

| Lines | What it is | The tell |
|-------|------------|----------|
| 08:03:45–08:04:00 | **Six RDP attempts** from `203.0.113.45` to WKS-311 port 3389, three seconds apart, all dropped | One source, one port, a steady rhythm — a script, not a person |
| 08:31:10–08:31:12 | **A port scan** from `198.51.100.23` — twelve different destination ports in two seconds | One source, one *source port* (44001), many destination ports, all SYN — the signature of a scanner |
| 18:41:07–18:41:16 | **Outbound to the Tor node** `185.220.101.1:443` from WKS-311, four times, **dropped** | Path = SEND, after hours; the firewall stopped it — but *something on WKS-311 tried*, and that is the Day 03 case |
| 08:15:02 | Two **allowed** connections to `192.168.10.22:8000` | The practice web server — expected; shows what an ALLOW looks like |

---
---

# 6 — PARSER v2 — WHAT CHANGED FROM DAY 04
### Demo 5 (follow-along) and PM Task 5. The file is `Day_06_fw_parser.py`. Read it; then run it.

Day 04's parser read one kind of file. Version 2 reads **two**, and decides which by looking at the first line:

| Part | What it does | New? |
|------|-------------|------|
| `parse_access_log()` | Day 04's regex and counts, moved into a function | Moved, not changed |
| `parse_firewall_log()` | Skips `#` lines, splits on spaces, takes the first eight fields, counts ALLOW/DROP, DROP by source, DROP by destination port | **New** |
| The last six lines | If line 1 starts with `#Version` → firewall; else → access log | **New** |

**Expected output on `Day_06_pfirewall.log`:**
```
Records by action:
  ALLOW  6
  DROP   22
DROP by source address:
  198.51.100.23    12
  203.0.113.45     6
  192.168.10.31    4
DROP by destination port (top 5):
  3389   7
  443    5
  21     1
  22     1
  23     1
```
*(Read the top line of each block and you have the four findings from §5 in three seconds — that is what a parser is for.)*

**Expected output on `Day_5_access_log.txt`:** the same as Day 04 — `200 27 · 302 2 · 304 1 · 403 3 · 404 7`, top IP `203.0.113.45` with 14. *(Yes — the same address that is hammering RDP in the firewall log. Two logs, one attacker.)*

**The one-line change for PM Task 5:** `drop_by_port.most_common(5)` → `most_common(10)`; or add a fourth counter, `drop_by_path`, and print SEND vs RECEIVE.

---
---

# 7 — THE COMMANDS TRAINEES RUN
### Nothing here needs admin except turning firewall logging on (trainer only) and capturing packets (optional, Npcap).

```powershell
# Ports — who is listening, and who owns it (Topic 6.3)
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort
Get-Process -Id <PID> | Select-Object ProcessName, Path

# The web server (Topic 6.2) — window 1
cd "$env:USERPROFILE\Documents\www"; python -m http.server 8000
# The client — window 2
curl.exe -I http://localhost:8000/about.html
curl.exe -X DELETE http://localhost:8000/
Invoke-WebRequest http://localhost:8000/docs -MaximumRedirection 0 -ErrorAction SilentlyContinue | Select-Object StatusCode   # shows the 301

# The firewall log (Topic 6.4) — read the supplied file (no admin)
Get-Content .\Day_06_pfirewall.log | Select-Object -First 8
Select-String -Path .\Day_06_pfirewall.log -Pattern " DROP " | Measure-Object | Select-Object Count
Select-String -Path .\Day_06_pfirewall.log -Pattern "3389"

# Parser v2 (Topic 6.5)
python .\Day_06_fw_parser.py .\Day_06_pfirewall.log
python .\Day_06_fw_parser.py .\Day_5_access_log.txt

# Hash the day's files (400311106)
Get-ChildItem C:\Evidence\Day_06 | Get-FileHash -Algorithm SHA256
```

> **Wireshark for trainees is optional.** Reading a saved capture needs only Wireshark (or WiresharkPortable, no admin). *Capturing* needs Npcap, which needs admin. Trainees who can install it may make their own 60-second capture for PM Task 1; everyone else works from the packet list in §1 and the trainer's screen. **Stop the server** (`Ctrl+C` in its window) at the end of the day — a web server left running on port 8000 is a finding on your own port map tomorrow.
