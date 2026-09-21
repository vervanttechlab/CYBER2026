# DAY 05 — SAMPLE DATA
## The channel drill, the custom-view recipe, the filter cookbook, the Autoruns entries, and the baseline v2 commands
### Trainer, and trainees where marked.

> **Safety note.** Nothing today touches malware. Every command reads a log or lists what is already running; nothing is changed, stopped, or deleted. The Autoruns entries in §4 are **on paper** — invented to look real. Hostnames, paths and names are fictional. Do **not** enable the VirusTotal option in Autoruns or Process Explorer in class — it uploads file hashes to a third party, and Day 03's rule ("would you paste this?") applies.

> **Continuity.** Yesterday was **Day 04 — The Machine Underneath** (the folder is named `Day_5` because it was authored for the 15-day plan). Its baseline CSVs are in `C:\Evidence\Day_05\`. First thing this morning the class **renames that folder to `Day_04`** so today's evidence has a clean `Day_05`.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The five channels — what lives where | Topic 5.1, Handout |
| 2 · The "Which Channel?" drill — ten events | Activity 1 |
| 3 · The custom-view recipe and the XML filter | Demo 2, Activity 2, PM Task 1 |
| 4 · The filter cookbook — eight `Get-WinEvent` queries | Demo 3, Activity 3, PM Task 2 |
| 5 · The Autoruns entry set (paper) | Activity 4 |
| 6 · Baseline v2 — the commands and the compare | Demo 5, PM Task 3 |
| 7 · The OS-equivalents seed table | PM Task 5 |
| 8 · Event IDs worth knowing | Handout, PM Task 2 |

---
---

# 1 — THE FIVE CHANNELS
### Topic 5.1. Event Viewer has hundreds of logs. An L1 analyst lives in five.

| # | Channel | Path in Event Viewer | What lands here | Admin needed to read? |
|---|---------|----------------------|-----------------|-----------------------|
| 1 | **Security** | Windows Logs → Security | Logons (4624 / 4625), new process (4688, if auditing is on), account changes | **Yes** — usually. If it says "access denied", that is expected on a standard account |
| 2 | **System** | Windows Logs → System | Services installed / started / stopped (7045 / 7036), boots and shutdowns (6005 / 6006 / 1074), drivers, time changes | No |
| 3 | **Application** | Windows Logs → Application | Application crashes (1000), hangs (1002), installers (MsiInstaller 11707 / 11724) | No |
| 4 | **Windows Defender / Operational** | Applications and Services Logs → Microsoft → Windows → Windows Defender → Operational | Detections (1116), actions (1117), failures (1118 / 1119), real-time protection off (5001), signature updates (2000 / 2001) | No |
| 5 | **PowerShell / Operational** | Applications and Services Logs → Microsoft → Windows → PowerShell → Operational | Script blocks that ran (4104) — if script-block logging is on; pipeline start (4103) | No |

> **The rule to teach:** *know which channel before you open Event Viewer.* The skill is not reading everything — it is going straight to the one log that would hold the answer.

---
---

# 2 — THE "WHICH CHANNEL?" DRILL
### Activity 1 — ten events, read aloud one at a time; trainees answer in chat with the channel number (1–5). Answers in `Day_05_Solutions.docx`.

1. "Someone logged on to this machine at 2 a.m."
2. "A new service called *Adobe Update Checker* was installed yesterday."
3. "The antivirus found something and removed it."
4. "The machine restarted unexpectedly at 03:41."
5. "A PowerShell script ran that contained the word *DownloadString*."
6. "Real-time protection was switched off."
7. "Word crashed three times this morning."
8. "Somebody tried the wrong password twelve times in a row."
9. "The signature update has been failing every day."
10. "A program was installed using an .msi installer."

---
---

# 3 — THE CUSTOM-VIEW RECIPE AND THE XML FILTER
### Demo 2, Activity 2, PM Task 1. A custom view is a saved filter — you build it once and it is there every morning.

**Recipe — the GUI way (Event Viewer):**
1. Right-click **Custom Views** → **Create Custom View…**
2. **Logged:** Last 7 days · **Event level:** tick all · **By log:** expand *Applications and Services Logs → Microsoft → Windows → Windows Defender* → tick **Operational**
3. **Includes/Excludes Event IDs:** type `1116,1117,1118,1119,5001` → **OK**
4. **Name:** `Defender — detections and failures` · **Description:** one line saying what it is for → **OK**
5. It now appears under Custom Views. Right-click it → **Export Custom View…** → save as `CV_Defender.xml` in `Evidence\Day_05\`

**The same view as XML** *(the XML tab of Create Custom View, "Edit query manually")*:
```xml
<QueryList>
  <Query Id="0" Path="Microsoft-Windows-Windows Defender/Operational">
    <Select Path="Microsoft-Windows-Windows Defender/Operational">
      *[System[(EventID=1116 or EventID=1117 or EventID=1118 or EventID=1119 or EventID=5001)]]
    </Select>
  </Query>
</QueryList>
```

**Read it aloud:** *Query* — one question. *Path* — which log. *Select* — keep the events where… *System/EventID* — the ID is one of these. That is all a custom view is: a saved question.

**Import (on a new machine, or after a rebuild):** Action → **Import Custom View…** → pick the `.xml`. This is why you export them — the view travels with you.

**The five views PM Task 1 asks for** *(one line of purpose each)*:

| View | Log | IDs | Purpose |
|------|-----|-----|---------|
| `CV_Defender` | Defender / Operational | 1116, 1117, 1118, 1119, 5001 | Detections, actions, failures, protection off |
| `CV_Updates` | Defender / Operational | 2000, 2001, 2002, 2003 | Signature and engine updates — and failures |
| `CV_NewServices` | System | 7045 | A service was installed — a favourite hiding place |
| `CV_Reboots` | System | 6005, 6006, 1074, 41 | Boots, shutdowns, who requested them, unexpected restarts |
| `CV_Crashes` | Application | 1000, 1002 | Application crashes and hangs |

---
---

# 4 — THE FILTER COOKBOOK
### Demo 3 runs the first three. Activity 3 (observed) runs #3 three ways. PM Task 2 runs all eight and records the count.

**The four keys that cover 90% of the job:** `LogName` · `Id` · `StartTime` / `EndTime` · `ProviderName`. Everything below is those four in different combinations.

```powershell
# 1  Defender detections and actions, last 30 days
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1116,1117; StartTime=(Get-Date).AddDays(-30) }

# 2  Any failed action or protection-off, ever
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=1118,1119,5001 }

# 3  New services installed, last 30 days  (the one Activity 3 does three ways)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-30) }

# 4  Boots, shutdowns and who asked for them, last 14 days
Get-WinEvent -FilterHashtable @{ LogName='System'; Id=6005,6006,1074; StartTime=(Get-Date).AddDays(-14) }

# 5  Everything the Service Control Manager said today
Get-WinEvent -FilterHashtable @{ LogName='System'; ProviderName='Service Control Manager'; StartTime=(Get-Date).Date }

# 6  Application crashes, last 7 days
Get-WinEvent -FilterHashtable @{ LogName='Application'; Id=1000; StartTime=(Get-Date).AddDays(-7) }

# 7  Signature update failures, ever
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-Windows Defender/Operational'; Id=2001 }

# 8  PowerShell script blocks, last 7 days (may be empty if logging is off — that is a finding)
Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104; StartTime=(Get-Date).AddDays(-7) }
```

**Two things to add to any of them:**
```powershell
 | Select-Object TimeCreated, Id, ProviderName, Message                                   # read it
 | Export-Csv "$env:USERPROFILE\Evidence\Day_05\q3_new_services.csv" -NoTypeInformation -Encoding UTF8   # keep it
```

**Counting instead of reading:**
```powershell
(Get-WinEvent -FilterHashtable @{ LogName='System'; Id=7045; StartTime=(Get-Date).AddDays(-30) } -ErrorAction SilentlyContinue).Count
```

> **"No events were found that match the specified selection criteria"** is a **result**, not an error. The count is zero. Write zero. *(The `-ErrorAction SilentlyContinue` above turns the red text into a quiet zero.)*

**The same question three ways** *(Activity 3 — new services in the last 30 days)*:

| Way | How |
|-----|-----|
| GUI filter | System log → **Filter Current Log…** → Event IDs `7045` → Logged: Last 30 days |
| Custom view | `CV_NewServices` from §3 (saved; it is there tomorrow) |
| PowerShell | Cookbook #3, piped to `Export-Csv` |

Same answer, three tools. The GUI is for looking; the custom view is for every morning; PowerShell is for keeping and comparing.

---
---

# 5 — THE AUTORUNS ENTRY SET (PAPER)
### Activity 4. Eight entries as Autoruns would show them. For each: **normal Windows · legitimate third-party · suspicious** — and the reason. Answers in Solutions.

Autoruns colours: **pink** = publisher not verified / unsigned · **yellow** = the file the entry points to is missing · white = verified.

| # | Tab | Entry | Image path | Publisher (Verified?) | Colour |
|---|-----|-------|------------|-----------------------|--------|
| A | Logon | SecurityHealth | `C:\Windows\System32\SecurityHealthSystray.exe` | Microsoft Windows (Verified) | white |
| B | Logon | OneDrive | `C:\Users\trainee\AppData\Local\Microsoft\OneDrive\OneDrive.exe` | Microsoft Corporation (Verified) | white |
| C | Logon | WindowsUpdateHelper | `C:\Users\Public\svhost32.exe` | *(Not verified)* | **pink** |
| D | Scheduled Tasks | \Adobe Update Checker | `C:\Users\trainee\AppData\Roaming\update-check.ps1` (via powershell.exe -w hidden) | *(Not verified)* | **pink** |
| E | Scheduled Tasks | \Microsoft\Windows\Defrag\ScheduledDefrag | `C:\Windows\System32\defrag.exe` | Microsoft Windows (Verified) | white |
| F | Services | Steam Client Service | `C:\Program Files (x86)\Common Files\Steam\steamservice.exe` | Valve Corporation (Verified) | white |
| G | Services | WinDefendHelper | `C:\ProgramData\wdh\wdh.exe` | *(Not verified)* | **pink** |
| H | Logon | Discord | `C:\Users\trainee\AppData\Local\Discord\Update.exe` | *(File not found)* | **yellow** |

---
---

# 6 — BASELINE v2 — THE COMMANDS AND THE COMPARE
### Demo 5 and the follow-along; PM Task 3. Day 04's baseline had four lists. Version 2 has the same four, plus hashes, plus a comparison.

**0. Housekeeping (8:00 — everyone):**
```powershell
Rename-Item "C:\Evidence\Day_05" "C:\Evidence\Day_04"          # yesterday's folder gets yesterday's name
New-Item -ItemType Directory "C:\Evidence\Day_05" | Out-Null
```

**1. The four lists, version 2:**
```powershell
$E = "C:\Evidence\Day_05"
Get-Process | Select-Object Name, Id, Path, Company | Sort-Object Name | Export-Csv "$E\baseline_v2_processes.csv" -NoTypeInformation
Get-Service | Select-Object Name, Status, StartType          | Export-Csv "$E\baseline_v2_services.csv"  -NoTypeInformation
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess |
    Sort-Object LocalPort | Export-Csv "$E\baseline_v2_ports.csv" -NoTypeInformation
```
**Autoruns, the proper way** *(the command-line Autoruns writes a CSV with hashes; run from the Sysinternals folder)*:
```powershell
.\autorunsc64.exe -accepteula -nobanner -a * -c -h -s > "$E\baseline_v2_autoruns.csv"
```
*(`-a *` every category · `-c` CSV · `-h` hashes · `-s` verify signatures. Without admin it lists the current user's entries and warns — that is fine; note it in the register.)*
**Fallback if Autoruns is blocked:** `Get-CimInstance Win32_StartupCommand | Select-Object Name, Command, Location | Export-Csv "$E\baseline_v2_autoruns.csv" -NoTypeInformation` — the Day 04 command.

**2. Hash the evidence:**
```powershell
Get-ChildItem "$E\baseline_v2_*.csv" | Get-FileHash -Algorithm SHA256 |
    Select-Object @{n='File';e={Split-Path $_.Path -Leaf}}, Hash | Export-Csv "$E\baseline_v2_hashes.csv" -NoTypeInformation
```

**3. Compare v2 to Day 04's v1** *(the point of a baseline is the difference)*:
```powershell
$old = Import-Csv "C:\Evidence\Day_04\baseline_services.csv"
$new = Import-Csv "C:\Evidence\Day_05\baseline_v2_services.csv"
Compare-Object $old $new -Property Name, StartType | Sort-Object Name
```
**What you will see:** either nothing (identical), or lines marked `=>` (only in today's) and `<=` (only in Day 04's). A new service with `=>` is exactly what a 7045 event would also show — two sources, one fact.

```powershell
$old = Import-Csv "C:\Evidence\Day_04\baseline_processes.csv"
$new = Import-Csv "C:\Evidence\Day_05\baseline_v2_processes.csv"
Compare-Object $old $new -Property Name | Sort-Object Name
```
*(Processes differ every time — a browser open or closed. That is normal; the skill is telling normal churn from a new `svhost32.exe` in `C:\Users\Public`.)*

---
---

# 7 — THE OS-EQUIVALENTS SEED TABLE
### PM Task 5. Knowledge 1.1 names Windows, macOS and Linux. Trainees complete the table; the seed gives the shape.

| What you did today on Windows | macOS | Ubuntu / Linux |
|-------------------------------|-------|----------------|
| Event Viewer / `Get-WinEvent` | Console.app · `log show --last 1h` | `journalctl -u <service>` · `/var/log/syslog`, `/var/log/auth.log` |
| Process Explorer / `Get-Process` | Activity Monitor · `ps aux` | `top` · `ps aux` · `htop` |
| Autoruns | Login Items · `launchctl list` · `~/Library/LaunchAgents` | `systemctl list-unit-files --state=enabled` · `crontab -l` · `/etc/cron.*` |
| TCPView / `Get-NetTCPConnection` | `lsof -i` · `netstat -an` | `ss -tulpn` · `lsof -i` |
| `Get-Service` | `launchctl list` | `systemctl list-units --type=service` |
| `Get-FileHash` | `shasum -a 256` | `sha256sum` |

---
---

# 8 — EVENT IDs WORTH KNOWING
### Handout and PM Task 2. Not for memorising — for the cookbook.

| Channel | ID | Meaning |
|---------|----|---------|
| Security | 4624 / 4625 | Logon succeeded / failed |
| Security | 4688 | New process created (only if process auditing is on) |
| Security | 4720 / 4732 | User created / added to a group |
| System | 7045 | A service was **installed** |
| System | 7036 / 7040 | Service started or stopped / start type changed |
| System | 6005 / 6006 | Event log started (boot) / stopped (shutdown) |
| System | 1074 | Shutdown or restart requested — by whom, why |
| System | 41 | Unexpected restart (no clean shutdown) |
| Application | 1000 / 1002 | Application crash / hang |
| Application | 11707 / 11724 | MSI install completed / removal completed |
| Defender / Operational | 1116 / 1117 / 1118 / 1119 | Detected / action taken / action failed / critical failure |
| Defender / Operational | 5001 · 2000 / 2001 | Real-time protection off · signatures updated / failed |
| PowerShell / Operational | 4104 | Script block logged (the script text itself) |
