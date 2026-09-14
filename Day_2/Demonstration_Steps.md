# DAY 2 — DEMONSTRATION STEPS
## Scripts and Step-by-Step Guides for Every Demo (For the Trainer)

> **How to use this guide:** Grey quote blocks are read aloud as written. Numbered items are steps you perform. Everything today is done on the whiteboard or the projector — no tools are installed on Day 2.

---

## Demo 1: Turning a Symptom Into a Problem Statement

**What trainees will learn:** How to write a problem statement somebody else could pick up.

### Steps:

1. Write on the whiteboard, in large letters:
   ```
   "THE SIEM IS BROKEN"
   ```

2. Say:
   > "This is what somebody is going to say to you. It is not useful. Everything I would need to help is missing from it. Let us fix it together."

3. Ask the class the three questions one at a time, and write the answers underneath:

   **"What exactly is happening?"**
   - Push back on vague answers. If somebody says "it's not working", ask "what would I see on the screen?"
   - Land on: *"Four hosts show no events in the dashboard."*

   **"When did it start?"**
   - Ask: "How would you find that out?" *(Look at the last event timestamp for each host.)*
   - Land on: *"Last event from each was approximately 14:20 today."*

   **"What is the scope?"**
   - Ask the question that most trainees miss: **"What is NOT affected?"**
   - Land on: *"All other hosts reporting normally. The four affected hosts respond to ping."*

4. Now write the complete statement underneath, and read it aloud:
   > "Since approximately 14:20 today, four Manila servers — SRV-MNL-01 through 04 — have shown no events in the dashboard. All other hosts are reporting normally. The four affected hosts respond to ping."

5. Make the point:
   > "Count the difference. The first version was four words. This is three sentences. And with these three sentences, somebody who has never seen this problem can start work immediately. The boundary line — 'all other hosts are reporting normally' — is the most valuable sentence in it, because it eliminates half the possible causes before anyone touches a keyboard."

6. **Checkpoint question to the class:** "What does 'the four affected hosts respond to ping' rule out?"
   > *(The network path is up and the hosts are powered on. So the fault is above the network layer — the agent, the config, or the server side.)*

---

## Demo 2: The Five Whys, Live

**What trainees will learn:** How to drive to a root cause and know when to stop.

**Setup:** Whiteboard. Write the problem at the top and work downward so the chain is visible.

### Steps:

1. Write the problem:
   ```
   The same malware detection reappears on WKS-118 every morning.
   ```

2. Ask the class "Why?" and take answers. Steer to: *"Because antivirus detects and cleans the file each morning."*
   Write it. Then ask the sharper question:
   > "That tells us what AV does. But why is there a file to clean, every single morning?"

3. Continue the chain, writing each link. Do not accept the first vague answer at any step:

| Ask | Steer the class to |
|-----|-------------------|
| Why does it come back? | Something writes it back to disk |
| Why does something write it back? | A scheduled task runs at logon and downloads it |
| Why is there a scheduled task? | It was created by the original infection |
| Why wasn't it removed? | **AV removed the file but not the persistence mechanism** |

4. Draw a box around the last answer and label it **ROOT CAUSE**.

5. Now teach the stopping rule. Ask:
   > "Should we keep going? Why wasn't the persistence removed? Because the AV product only removes files. Why does it only remove files? Because that is how it is designed."

   Then say:
   > "Notice what just happened. We went from something we can fix tonight — delete the scheduled task — to a complaint about a vendor's product design. That is one 'why' too far. **Stop at the first thing you can act on.**"

6. Teach the second rule with a deliberate wrong turn. Ask:
   > "Someone might say: why was there an infection at all? Because the user clicked a link. Why did the user click a link? Because they were not trained."

   Then say:
   > "That is all true, and none of it helps at two in the morning. When your chain arrives at a person, back up and find the technical cause. Awareness training is a real fix — it is just not tonight's fix, and it is not yours to implement."

7. Write the corrective action underneath the root cause and note that step 3 is an escalation:
   ```
   1. Export the scheduled task list from WKS-118        (L1)
   2. Identify and document the task that runs at logon  (L1)
   3. Escalate task removal to L2 — deletion is above L1 (L1 → L2)
   4. Full AV scan after removal                         (L2)
   5. Verify at next user logon                          (L1)
   ```

---

## Demo 3: The Same Plan, Three Audiences

**What trainees will learn:** How to pitch the same information to an L2, a client, and the ticket.

**Setup:** Use the fault from Demo 1 — four Manila servers stopped reporting at 14:20.

### Step 1: Say it to your L2

Read this aloud at normal speed, then stop and let it land:

> "Four Manila servers stopped sending events at about 14:20 — MNL-01 through 04. Everything else is reporting fine and all four answer ping, so it is not the network and they are not down. I have checked the change calendar and there is no change notice covering it. I would like to restart the agent service on one of them as a test before I do all four. Are you happy for me to do that?"

Then ask the class:
- "How long was that?" *(About twenty seconds.)*
- "What did it contain?" — write on the board:

| Element | The words |
|---------|-----------|
| The fact | "Four Manila servers stopped sending events at about 14:20" |
| The boundary | "Everything else is reporting fine... it is not the network" |
| What I already checked | "no change notice covering it" |
| What I want to do | "restart the agent service on one of them as a test" |
| The ask | "Are you happy for me to do that?" |

> **Say:** "That last part is the difference between a competent L1 and a good one. They did not just report a problem — they arrived with a proposed next step and asked for authority. Your L2 has to say one word: yes."

### Step 2: Say it to the client

Read aloud:

> "Good afternoon — I am calling to let you know we have lost monitoring visibility on four of your Manila servers since about two twenty this afternoon. The servers themselves are running normally and your users are not affected. We are working on restoring the monitoring now and I will call you back within the hour with an update."

Then ask the class:
- "What is missing compared to the L2 version?" *(Agent service, ping, change calendar — all the technical detail.)*
- "What is in it that was NOT in the L2 version?" *(**"Your users are not affected"** and **"I will call you back within the hour."**)*

> **Say:** "The client does not care what an agent service is. They care about two things: is my business affected, and when will I hear from you again. Answer both, every time, and you will never have an angry client — even when the news is bad."

**Then teach the trap.** Say:
> "What you must never do is this: 'We are having some issues with the monitoring, we are looking into it, I will get back to you.' That sentence has no scope, no impact statement, and no time commitment. It sounds reassuring and it is the reason clients escalate to your manager."

### Step 3: Write it in the ticket

Project this and read it:

```
14:47  Detected loss of event flow from SRV-MNL-01, -02, -03, -04.
       Last event from each host approx 14:20.
14:49  Verified all other monitored hosts reporting normally.
14:52  ICMP reply received from all four affected hosts.
14:55  Checked change calendar — no change notice in effect for
       Manila cluster on this date.
15:01  Briefed L2 (R. Aguilar). Authorised to restart agent service
       on SRV-MNL-01 as a single-host test.
15:04  Client contact notified by phone. Advised no user impact,
       callback committed within 1 hour.
```

Then ask:
- "What does the ticket have that neither conversation had?" *(**Timestamps**, and the name of who authorised what.)*

> **Say:** "In six months, nobody will remember this afternoon. The ticket is the only thing that will. Two things must always be in it that people forget: the exact times, and the name of whoever gave you authority to act. If you are ever asked 'why did you restart that server?', the answer is a line in a ticket with a name on it."

---

## Demo 4: Ranking Six Improvement Ideas

**What trainees will learn:** That the best idea is usually not the most technically interesting one.

### Steps:

1. Project these six proposals. Give teams **10 minutes** to rank them.

```
IDEA 1  Add a "change reference" field to the ticket template so
        analysts stop writing it in the free-text notes.

IDEA 2  Build a machine-learning model to predict which alerts are
        false positives.

IDEA 3  Tune the firewall rule that fires 200 times a night on the
        scheduled backup job.

IDEA 4  Add a line to the handover template: "changes in effect
        tonight".

IDEA 5  Buy a second SIEM so we have redundancy.

IDEA 6  Write a one-page cheat sheet of the ten most common alert
        types and what each one usually means.
```

2. Take each team's ranking, then reveal the analysis:

| Idea | Impact | Effort | Risk | Authority | Verdict |
|------|--------|--------|------|-----------|---------|
| **3** Tune the backup rule | **Very high** — removes ~200 alerts/night | Medium — needs rule change + testing | Medium — could suppress a real alert | Needs L2/engineering | **Do this first** |
| **4** Handover "changes tonight" line | High — prevents whole categories of false escalation | **Trivial** — edit a template | Very low | **An L1 can do it** | **Do this today** |
| **6** Cheat sheet | High for new starters | Low — one shift to write | None | **An L1 can do it** | **Do this week** |
| **1** Change reference field | Medium — improves records | Low | None | Needs ticket admin | Do this month |
| **5** Second SIEM | Low for this problem | Enormous | High | Way above L1 | Not the answer |
| **2** ML false-positive model | Unknown | Enormous | **High** — suppressing real alerts | Way above L1 | Not the answer |

3. Debrief with these points:
   > "Idea 4 is the smallest idea on the list. It is one line in a template. It is also the second-best idea on the list, because it costs nothing, an L1 can just do it, and it prevents an entire category of wasted work."

   > "Ideas 2 and 5 are the ones that sound most impressive in a meeting. Both are enormous, both are above your authority, and neither addresses the fact that one badly tuned rule is generating two hundred alerts a night. Idea 3 does."

   > "This is the whole lesson: the highest-impact improvement is usually boring, cheap, and close to the work. If your idea requires a budget, it is somebody else's idea. Propose the one you can do on Tuesday."

4. **Checkpoint question:** "Which of these six is the riskiest, and why?"
   > *(**Idea 2.** A model that hides alerts it thinks are false positives will eventually hide a real one, and nobody will know. Any change that suppresses information needs far more scrutiny than a change that adds it.)*

---

## FAULT CARDS

> ## DO NOT PASTE FROM THIS PAGE
>
> **The actual cause is printed directly under every card.** If you copy from here into the
> chat you will paste the answer with it.
>
> **The clean cards trainees work from are in the Activity Pack, Parts 1 and 3** — along with
> the Problem-Solving Worksheets they write on. Send them that.
>
> Use this page for the reveal *after* each drill. Card 3 is spare, for fast teams or revision.

### FAULT CARD 1 — "The Empty Dashboard"

```
It is 14:47. A colleague says: "The dashboard is empty for Manila."

WHAT YOU CAN SEE
  - SRV-MNL-01, -02, -03, -04: last event 14:20, 14:20, 14:21, 14:20
  - All other 46 hosts: events arriving normally, right now
  - All four Manila hosts reply to ping
  - Server disk usage: 61%
  - No change notice is listed for today
  - The Manila site had a scheduled power interruption notice
    posted by Facilities (not IT) for 14:00–14:30
```

**Actual cause:** The site UPS switched over at 14:20 during the Facilities power interruption. The network switch serving the four servers rebooted. Hosts stayed up (hence ping works now), but the agents lost their connection and did not re-establish it because the agent service does not retry indefinitely.
**Teaching point:** The change notice they were told to check was an *IT* change notice. This change came from Facilities. Broaden where you look.

### FAULT CARD 2 — "The Alert Storm"

```
It is 22:10. Your queue has 214 open alerts. It normally has 30.

WHAT YOU CAN SEE
  - 186 of them are the same alert: "Blocked outbound connection"
  - All 186 are from one host: WKS-204
  - They started at 21:55 and are still arriving, ~12 per minute
  - The destination IPs are all different
  - The destinations are all on port 443
  - WKS-204's user, aflores, logged off at 18:00
  - WKS-204 ran a Windows Update cycle starting 21:50
```

**Actual cause:** The Windows Update client is contacting a content delivery network, and a firewall rule is blocking the CDN range. It is a false positive caused by a legitimate scheduled process meeting a badly scoped block rule.
**Teaching point:** The misleading first symptom is "logged-off machine making hundreds of outbound connections", which reads like malware. The disambiguating evidence is the update cycle starting five minutes before the storm. **Always check what started just before the symptom.**

### FAULT CARD 3 — "The Ticket That Keeps Coming Back" (spare)

```
It is 09:30. Ticket 6602 has been created four times this week
for the same thing: "AV detection on WKS-118 — Trojan.Agent.XZ".

WHAT YOU CAN SEE
  - Each ticket was created between 08:05 and 08:20
  - Each one was closed as "cleaned, no further action"
  - Each was closed by a different analyst
  - The user, mreyes, starts work at 08:00
  - The AV scan log shows the file quarantined each time
  - No other host has this detection
```

**Actual cause:** Incomplete remediation — a logon-triggered scheduled task re-downloads the payload. Also a *process* failure: four analysts each closed it without checking the history, so nobody saw the pattern.
**Teaching point:** There are two root causes here, one technical and one procedural. The procedural one — "closing a ticket without checking whether it has happened before" — is the more expensive of the two.
