# DAY 10 — PRESENTER SCRIPT
## Read this out loud, slide by slide
### Matched to the Day 10 deck — 15 slides

---

## HOW TO USE THIS SCRIPT
The grey quote blocks are the words. *(Italics are notes. Never read them.)* The times match the Instructor Guide. The demo steps are in `Day_10_Demonstration_Guide.md`, and this script cues the switch. The cut order is at the end. **The afternoon assessment has its own script**, in `Day_10_Unit_Assessment_Guide.md` Part 3.

## THE MORNING AT A GLANCE
| Slide | Time | What |
|-------|------|------|
| 1 | 8:00 | Welcome, recall Day 9, portfolio checklist |
| 2 | 8:10 | Five topics, and the shape of the day |
| 3 | 8:15 | Topic 10.1 → Demo 1: tell them in ten minutes |
| 4 | 8:35 | Activity 1 Ten Minutes (observed) |
| 5 | 8:55 | Topic 10.2 → Demo 2: where did it go? |
| 6 | 9:20 | Activity 2 Draw the Path |
| 7–8 | 9:40 | Topic 10.3 → Demo 3: what came in, what went out |
| — | 10:00 | Break |
| 9–10 | 10:10 | Topic 10.4 → Demo 4: how it got in, how it stays, ATT&CK Navigator |
| 11 | 10:35 | Activity 3 Name It, Map It |
| 12 | 10:55 | Topic 10.5 the threat report · Demo 5 preview |
| 13 | 11:05 | Activity 4 Assemble the Report |
| 14 | 11:30 | How the assessment works |
| 15 | 11:40 | This afternoon, and close |

---
---

# SLIDE 1 — TITLE
### 8:00 – 8:10 · 10 minutes
> "Good morning. Day 10. This is a big one. This morning you learn the last element of the first core unit, alert reporting. This afternoon, that whole unit is assessed. So this morning is also your last practice."

> "Quick recall from yesterday. What three things make an escalation pack more than an opinion?" *(Evidence, an ask, a deadline.)* "Good. And where did we leave SRV-BAK-02?" *(Escalated to the information security manager at 10:52.)* "Today you find out what happened next, and it gets worse."

> "Still no server. The evidence is on paper, your own machine shows you ingress and egress, and the ATT&CK tool runs in your browser. And still going slowly."

*(Collect the portfolio checklists from the last page of the Handout. Anyone missing items has until 12:45.)*

# SLIDE 2 — FIVE TOPICS, AND THE SHAPE OF THE DAY
### 8:10 – 8:15 · 5 minutes
> "Five topics. 10.1: tell them in ten minutes, the Critical notification. 10.2: where did it go, spread and lateral movement. 10.3: what came in and what went out, ingress and egress. 10.4: how it got in and how it stays, mapped to MITRE ATT&CK. And 10.5: the threat report, which puts all of it in one document."

> "One idea runs through the whole morning: link with evidence, not with the clock. You'll see why at nine o'clock."

> "The afternoon is different today. It is not self-study. It's the unit assessment, live, cameras on, from one to four. I'll explain it at 11:30. For now, focus on the learning."

# SLIDE 3 — TOPIC 10.1: TELL THEM IN TEN MINUTES → DEMO 1
### 8:15 – 8:35 · 20 minutes
> "First, what happened after yesterday's escalation." *(Read Sample Data §1 aloud. Stop on 11:29.)* "One point eight gigabytes LEFT the backup server. On our severity matrix from Day 6, 'data leaving' is Critical. Critical means the owner is told within ten minutes. The clock just started."

> "This week you've learned two messages. Verification: telling the client a scan result. Escalation: sending a failure up to an authority. Today there's a third. Notification: warning the owner of a High or Critical threat, so they can protect what's theirs. Fast beats complete. Watch me call R. Santos."

*(Run **Demonstration 1**: read §1, the N1 call, count the seven lines, write the notification, then explain why SRV-FILE-01's owner is not called.)*

> "Seven lines. And the one that makes it a notification, not just news, is the 'do and do not'. And only High and Critical are notified. Medium goes in the report."

# SLIDE 4 — ACTIVITY 1: TEN MINUTES
### 8:35 – 8:55 · 20 minutes · OBSERVED
> "Pairs. The case is N2: J. Mendoza, the Operations supervisor, whose team member uses WKS-311. It's High. One of you is the analyst, one is Mendoza. Make the call using the seven lines, then swap. Then, together, write the notification in writing. Last, decide N3: do you notify SRV-FILE-01's owner? Write your reason."

> "I'm visiting each room, listening for two things: severity with a reason, and a real 'do or do not'. And one ask, a next-update time, and a read-back. One more thing: do not blame the user. The call is about protecting the team."

*(Observation sheet open. Visit each pair once. Bring them back at 8:55.)*

# SLIDE 5 — TOPIC 10.2: WHERE DID IT GO? → DEMO 2
### 8:55 – 9:20 · 25 minutes
> "PC 5.2 asks for two things. Spread: which machines, and how far. Lateral movement: how it got from one machine to the next. Every machine gets one of four words: origin, confirmed, attempted, or not linked. And every word needs a line number."

*(Run **Demonstration 2**: WKS-311 origin, the path to SRV-BAK-02 built live, E16, SRV-FILE-01 attempted, then the SRV-FIN-02 trap.)*

> "SRV-FIN-02 was encrypted in the same minute. And it's still not linked, because no line joins it. Different account, different address, different file. Two things at the same time are not one case until a line of evidence joins them. Link with evidence, not with the clock."

# SLIDE 6 — ACTIVITY 2: DRAW THE PATH
### 9:20 – 9:40 · 20 minutes
> "Teams. Two tables from the evidence set. First, the hosts table: all four machines, each with its word and its lines. Second, the path: from, to, method, account, time, line. Then draw it: four boxes and arrows, with a solid arrow for what happened and a dotted arrow for what was only attempted. Put the SRV-FIN-02 box on the page too, off to the side, with 'not linked' and the line that proves it."

*(Answers in Solutions. Bring out: SRV-FILE-01 is attempted, not infected, and E08 is lateral because the source is inside.)*

# SLIDES 7–8 — TOPIC 10.3: WHAT CAME IN, WHAT WENT OUT → DEMO 3
### 9:40 – 10:00 · 20 minutes
> "Ingress is what came in. Egress is what went out. Two rules. Who started the connection decides the direction. And bytes decide how serious it is. Follow along on your own machine. You'll see lots of normal connections. We're learning to read, not hunting."

*(Run **Demonstration 3**: the four commands on your own machine, then E03, E06 / E13, E14 and E18.)*

> "E03 went out and brought a file in: 1.2 megabytes. That's the malware arriving. E06 and E13: two kilobytes, every five minutes, which is a beacon. E14: 1.8 gigabytes out, forty-eight kilobytes in. That's what data leaving looks like. And E18, no inbound from the internet, is a finding too. It came in by email."

*(Trainees write their own-machine record: one egress row, one listening port. This goes in the portfolio.)*

# BREAK
### 10:00 – 10:10

# SLIDES 9–10 — TOPIC 10.4: HOW IT GOT IN, HOW IT STAYS → DEMO 4
### 10:10 – 10:35 · 25 minutes
> "PC 5.4. Exploitation activity: how they got in, and how they got more access. Installation behaviour: what they left behind so it keeps running. On WKS-311, nobody broke any software. The user was tricked into running a macro. On SRV-BAK-02, the way in was a weak password, guessed on the thirty-ninth try."

> "And the installation explains Day 9. A Windows service, set to restart after every failure. That's why the process 'restarted itself in four seconds', and why the quarantine kept failing. Four days, one explanation."

*(Run **Demonstration 4**: tactic versus technique, then Navigator. Create a layer, map B1–B3, and export the JSON.)*

> "The tactic is the goal: the column. The technique is the method: the box, with the ID. ATT&CK names the behaviour, and your line proves it. No line, no box."

# SLIDE 11 — ACTIVITY 3: NAME IT, MAP IT
### 10:35 – 10:55 · 20 minutes
> "Teams first, ten minutes. The behaviours B4 to B12. For each one: the tactic, the technique ID and name, and the evidence line. Check each ID on attack.mitre.org. Then on your own, ten minutes: open Navigator, add your team's techniques to the B1 to B3 layer, colour them, put the line in the comment, and download the JSON into your Day 10 folder."

*(Key in Solutions. If Navigator won't load for someone, they use the paper table. The mapping is the skill.)*

# SLIDE 12 — TOPIC 10.5: THE THREAT REPORT → DEMO 5
### 10:55 – 11:05 · 10 minutes
> "One document, fifteen sections. Look at sections 3 to 10. You've already written them this morning: the notification, the hosts, the path, ingress, egress, exploitation, installation, ATT&CK. What's left is the summary, the timeline, the containment status, what we don't know yet, and the recommendations."

> "Section 13, 'what we do not know yet', is not a weakness. It tells the next person where to look. And the rule of the whole report: every claim points to a line."

*(Run **Demonstration 5**: three screenshots, two minutes.)*

> "Tools will map it faster and build the timeline for you. The report stays the same."

# SLIDE 13 — ACTIVITY 4: ASSEMBLE THE REPORT
### 11:05 – 11:30 · 25 minutes
> "On your own. Open the report template. Paste in what you made this morning: sections 3 to 10. Then write the summary in four sentences, the timeline with eight to twelve events, section 13, and three recommendations. Each recommendation is a verb, an owner and a date. Before you stop, check three of your sentences. Does each one point to a line?"

*(Circulate. Anyone putting SRV-FIN-02 in the path: send them to E17. Anyone writing "improve security": ask for the verb.)*

# SLIDE 14 — HOW THE ASSESSMENT WORKS
### 11:30 – 11:40 · 10 minutes
> "This afternoon is the assessment for the whole unit, Monitor and report cyber threats. The standard gives three methods, and we use all three."

> "One: a written exam. Forty minutes, closed book. Twenty-five multiple-choice and five short answers. Pass is seventy percent."

> "Two: a demonstration. A new case you have not seen, called WKS-164. Ninety minutes, open book. You can use your handouts, your packs and the ATT&CK website, but no AI and no chat. Four parts, one for each part of the job: check the alerts, check the tool on your own machine with EICAR, follow up, and report."

> "Three: oral questions and your portfolio. While you work, I'll call each of you into a breakout for about six minutes. You'll make one short notification call to me. I'll ask you three questions, and I'll ask two questions about your portfolio: your own work, from Day 3 to today."

> "It's marked the way everything has been marked: the reason matters more than the answer. And if one part isn't there yet, you redo only that part, before Day 15. It's not the end of anything."

# SLIDE 15 — THIS AFTERNOON
### 11:40 – 11:45 · 5 minutes
> "Before you go. Submit this morning's work, the notification, the path, your own-machine record, the layer and the report, into Evidence, Day 10, as it stands. It's portfolio evidence. The report can be finished by the end of tomorrow. Don't spend your lunch on it."

> "At one o'clock: camera on, your Handouts and Activity Packs from Days 6 to 10 open, Windows Security working, and your Day 6 EICAR string ready to paste. Eat something."

> "This morning you finished the case. A failed quarantine on Day 7 turned out to be data leaving the building. You warned the owners, traced it from one workstation to one server, set aside a ransomware attack in the same minute because no line joined them, and named how it got in and how it stayed. This afternoon, you show you can do it alone. See you at one."

---
---

# IF YOU ARE RUNNING LATE
1. Activity 2 to the hosts table only. The drawing goes into Activity 4
2. Demo 4 maps B1 only. Activity 3 does B6, B7, B9, B10, B12 (the two PCs)
3. Activity 4 assembles sections 3–10 only. The rest is finished by the end of Day 11
4. Slide 14 can be shortened to the three methods. The full briefing is read at 1:00 anyway

**Never cut** Demo 1 (the notification), Activity 1 (observed), the SRV-FIN-02 step in Demo 2, or slide 15 (they must know what to bring at 1:00).

# THE THREE SENTENCES OF THE DAY
1. **Fast beats complete: notify the owner of a High or Critical threat within the clock, and tell them what to do and not do.**
2. **Link with evidence, not with the clock: origin, confirmed, attempted, not linked, and every word on a line.**
3. **Exploitation is how they got in. Installation is how they stay. ATT&CK names both, and the line proves it.**
