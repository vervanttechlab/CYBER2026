# DAY 7 — SAMPLE DATA
## The 8 alerts, the ticket register, and the solution-status scenarios
### Trainer, and trainees where marked.

> **Safety note.** No live malware, no client data. EICAR is the only "threat" and it is a harmless test file. Addresses use documentation-only ranges (`203.0.113.x`, `198.51.100.x`) and the Day 3 Tor node `185.220.101.1`.

---

## WHAT IS IN HERE

| Section | Used by |
|---------|---------|
| 1 · The eight alerts to triage | Activity 1, PM Tasks 1–2 |
| 2 · The ticket register template | Demo 1, Activity 2, PM Task 2 |
| 3 · The solution-status scenarios | Activity 3, PM Task 3 |

---
---

# 1 — THE EIGHT ALERTS TO TRIAGE
### Activity 1 (sort them), and PM Tasks 1–2 (decision + severity + reason + ticket). Answers in `Day_7_Solutions.docx`.

Several are deliberate callbacks to Days 3, 5 and 6, so the class sees continuity.

**Alert A**
> Defender on training PC 7 removed `eicar_test.txt` (`Virus:DOS/EICAR_Test_File`) at 09:12. No other activity.

**Alert B**
> WKS-311 (192.168.10.31) is making outbound connections to 185.220.101.1 on port 443. `netstat` shows the owning process is `svhost32.exe` in `C:\Users\Public`. The user logged off at 18:30 last night. Nothing has stopped the connections.

**Alert C**
> Defender quarantined `Trojan:Win32/Wacatac.B!ml` — file `setup_crack.exe` in a user's Downloads folder — at 14:05. Quarantine succeeded.

**Alert D**
> Finance server SRV-FIN-02: hundreds of files renamed to `.locked` since 03:40, a `HOW_TO_DECRYPT.txt` in every folder, and users cannot open documents. Still spreading.

**Alert E**
> The email gateway blocked a phishing link (`hxxp://secure-bpi-verification.net`) sent to nine Finance users at 08:50. The link was rewritten and blocked. No click recorded yet.

**Alert F**
> Windows Update installed the monthly security patch on 12 machines overnight; they are waiting for a restart.

**Alert G**
> Backup server SRV-BAK-02: Defender detected `Trojan.Agent.XZ` in `svhost32.exe` at 03:40 but the **quarantine FAILED** — the file is in use and could not be isolated. It is still there.

**Alert H**
> Defender blocked a bundled advertising toolbar (PUA:Win32/Adload) during a software install on a training PC. Blocked successfully.

---
---

# 2 — THE TICKET REGISTER TEMPLATE
### Demo 1, Activity 2, PM Task 2. Build this as columns in a shared LibreOffice Calc / Excel sheet (no ticket server yet).

| Column | Example |
|--------|---------|
| **Ticket ID** | CTM-0007-001 |
| **Summary** (host + detection) | SRV-BAK-02 — failed quarantine of Trojan.Agent.XZ |
| **Host / user / system** | SRV-BAK-02 |
| **Time it happened** | 2026-09-15 03:40 |
| **Time I saw it** | 2026-09-15 09:05 |
| **What the tool detected** | Trojan.Agent.XZ in svhost32.exe; quarantine failed |
| **Decision** | Threat |
| **Reason** | Action failed = not contained; on a backup server |
| **Severity** | Critical |
| **What I did / did not do** | Raised ticket; did NOT isolate (above my level) |
| **What I need next, from whom** | L2 to isolate host and identify the process holding the file |
| **SLA / due** | Critical → notify ≤10 min |
| **Status** | Open |

> The register carries exactly what a ticketing tool would. When the Wazuh/osTicket system is set up, these same columns become the ticket form.

---
---

# 3 — THE SOLUTION-STATUS SCENARIOS
### Activity 3 and PM Task 3. Trainees run the checks on their OWN machine; these scenarios are for reading practice and the marking key.

For each machine, the analyst answers the three Element-2 questions from the status output.

**Machine 1 — output**
```
AMServiceEnabled          : True
AntivirusEnabled          : True
RealTimeProtectionEnabled : True
AntivirusSignatureLastUpdated : today
```
*(Installed? Yes. Operational? Yes. Up to date? Yes. → healthy.)*

**Machine 2 — output**
```
AMServiceEnabled          : True
AntivirusEnabled          : True
RealTimeProtectionEnabled : False
AntivirusSignatureLastUpdated : today
```
*(Installed? Yes. Operational? NO — real-time protection is off. → a finding: the tool is present but not protecting. Report it.)*

**Machine 3 — output**
```
AMServiceEnabled          : True
AntivirusEnabled          : True
RealTimeProtectionEnabled : True
AntivirusSignatureLastUpdated : 41 days ago
```
*(Installed? Yes. Operational? Yes. Up to date? NO — signatures 41 days old. → a finding: it will miss recent threats. Report it.)*

**The commands trainees run on their own machine:**
```powershell
Get-Service WinDefend | Select-Object Name, Status, StartType
Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureVersion, AntivirusSignatureLastUpdated, QuickScanAge
```

> **The action range (for Topic 7.4), from the CS:** Failed · Clean · Delete · Quarantine · Blocked · Re-image. For EICAR, Defender **quarantines** or **removes** — a success. `MpCmdRun.exe` lists and restores quarantined items if a legitimate file was caught by mistake.
