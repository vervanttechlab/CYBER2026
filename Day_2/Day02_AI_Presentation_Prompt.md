============================================================
AI PRESENTATION BUILDER PROMPT
Cyber Threat Monitoring Level I (15-Day Program) — Day 02
Solving Routine Problems on a Real Desk
============================================================

HOW TO USE:
1. Copy the prompt below (from "Create a modern..." to the end).
2. Paste it into your AI presentation builder (Gamma, Canva AI, SlidesAI, etc.).
3. Generate the slides, then export as 16:9 widescreen via Canva.
4. This deck is capped at 20 slides: the maximum for a full 8-hour day.

DAY 02 IS A HYBRID DAY — same shape as Day 1:
- Slides 1-16 — morning, 8:00 AM to 12:00 PM, ONLINE SYNCHRONOUS
- Slides 17-20 — afternoon, 1:00 to 5:00 PM, FULLY ASYNCHRONOUS

The split follows the same rule as Day 1. Anything a team does together, or that
an assessor has to watch, is in the morning. Anything that is one person writing
on their own is in the afternoon.

  MORNING (live)  : 400311103 problem solving — team fault drills, the 60-second
                    briefing. Plus 400311109 entrepreneurial — team scenario.
  AFTERNOON (solo): 400311104 self-management — goals, emotions, learning style.
                    400311105 innovation — the SOP improvement proposal.

IF YOU ARE RUNNING DAY 2 FACE-TO-FACE INSTEAD:
Only three slides change. Slide 2 becomes a normal agenda, slide 17 becomes
"this afternoon in the room," and slide 20 keeps the same content. Everything
else is identical — the teaching does not depend on the delivery mode.

COLOR SCHEME:
- Primary dark blue: #1B3A5C
- Accent blue: #2E75B6
- Accent teal: #009688
- Light background: #D6E4F0
- White backgrounds with blue accents, sans-serif fonts.

============================================================
PROMPT (20 SLIDES) — COPY EVERYTHING BELOW
============================================================

Create a modern, professional training presentation of EXACTLY 20 slides. Use a navy and white color scheme (#1B3A5C navy, #2E75B6 accent blue, #009688 teal, white background). Use clean sans-serif fonts. Every slide must include a visual element — icons, simple infographics, or diagrams. Do NOT use stock photos of hackers, hoodies, padlocks, or binary code. Format 16:9 widescreen. Keep all comparison tables as real tables. Keep text short and readable; the speaker explains the detail. Do not add an agenda slide, a thank-you slide, or a Q&A slide.

Day 02 is a hybrid day: slides 1-16 are the live morning session, slides 17-20 are the self-study afternoon. Mark slide 17 clearly as the transition.

Audience: adult vocational trainees in the Philippines, day 2 of 15, mixed technical background. Today is about fixing things that are broken — not attacks, just faults. Keep the tone plain and practical, never hyped. Do not write "cyber warriors" or "threat landscape."

SLIDE 1 — TITLE
Title: "Solving Routine Problems on a Real Desk"
Subtitle: "Cyber Threat Monitoring Level I — Day 02 of 15"
Kicker: "Live session 8:00-12:00  |  Self-study 1:00-5:00"
Visual: a calm navy title slide with a simple troubleshooting or wrench-and-screen motif.

SLIDE 2 — HOW TODAY RUNS
Title: "Two Halves Again"
Two-column comparison:
- MORNING, TOGETHER: 8:00-12:00. Team fault drills. Writing action plans. Briefing your supervisor in 60 seconds. Watched and marked.
- AFTERNOON, ON YOUR OWN: 1:00-5:00. Your goals. How you handle pressure. How you learn. One improvement proposal.
Add the line: "Same rule as yesterday. Team work in the morning. Writing that is yours alone in the afternoon."
Visual: a split screen, video-call grid on the left, notebook on the right.

SLIDE 3 — THIS MORNING'S PLAN
Title: "This Morning — Live Together"
Timetable:
- 8:05-8:30 Day 1 SOP debrief
- 8:30-10:00 Finding the real problem, and its cause
- 10:00-10:10 Break
- 10:10-10:55 Choosing what to do, and writing the plan
- 10:55-11:20 Team fault drill 2 and the 60-second briefing
- 11:20-11:50 What an alert costs, and the team scenario
- 11:50-12:00 Your afternoon
Visual: a vertical timeline.

SLIDE 4 — UNITS COVERED TODAY
Title: "Units of Competency — Day 02"
Table (Code, Unit, When):
400311103 | Solve and address routine problems | This morning, live
400311109 | Adopt an entrepreneurial mindset | This morning, live
400311104 | Enhance self-management skills | This afternoon, on your own
400311105 | Support innovation | This afternoon, on your own
Add the line: "Four units in one day. The morning two need other people. The afternoon two need quiet."
Visual: clean table with a blue header row.

SLIDE 5 — SYMPTOM OR PROBLEM?
Title: "What They Tell You Is Not What Is Wrong"
Two-column table (What people report / What is actually wrong):
"The dashboard is empty" | The agent stopped sending events
"I'm getting a hundred alerts" | One rule is matching normal activity
"The same ticket keeps appearing" | The integration is retrying on timeout
"The scan never finished" | The target went offline mid-scan
"Antivirus says it cleaned it but it's back" | The persistence was never removed
Big line below: "Fix the left column and the problem comes back tomorrow."
Visual: two contrasting columns, left in grey, right in navy.

SLIDE 6 — THREE QUESTIONS
Title: "Three Questions That Turn a Symptom Into a Problem"
Numbered, large:
1. WHAT EXACTLY IS HAPPENING? — observable, specific, no interpretation
2. WHEN DID IT START? — and what else changed at that time
3. WHAT IS THE SCOPE? — one host, one team, one site, or everything
Add the line: "Question 2 solves more faults than any tool. Most things break because something changed."
Visual: three numbered question cards.

SLIDE 7 — BAD AND GOOD
Title: "What a Good Problem Statement Looks Like"
Two boxes, stacked.
BAD (small, grey): "The SIEM is broken."
GOOD (large, navy): "Since approximately 14:20 today, four Manila servers (SRV-MNL-01 to 04) have shown no events in the dashboard. All other hosts are reporting normally. The four affected hosts respond to ping."
Below, label what the good one contains: a start time · a scope · a boundary (what is NOT affected) · one piece of evidence
Add the line: "The good one is longer, and that is fine. Somebody who has never seen this problem could pick it up from that sentence."
Visual: highlight the four labelled elements inside the good statement.

SLIDE 8 — THE FIVE WHYS
Title: "The Five Whys"
Show as a descending chain:
PROBLEM: The same malware detection reappears on WKS-118 every morning.
Why? → Antivirus detects and cleans the file each morning.
Why does it come back? → Something writes it back to disk.
Why? → A scheduled task runs at logon and downloads it.
Why is the task there? → It was created by the original infection.
Why was it not removed? → AV removed the FILE but not the PERSISTENCE.
ROOT CAUSE: Remediation was incomplete.
Visual: a vertical chain with each answer stepping down and to the right.

SLIDE 9 — WHERE THE FIVE WHYS STOPS
Title: "Stop at the First Thing You Can Actually Do"
Two warnings side by side:
- STOP TOO EARLY: "Because there is malware." That is not a cause you can act on.
- GO TOO FAR: "Because the user clicked a link." True, but it is not tonight's fix.
Big highlighted box: "If your fifth WHY is a person's name, back up. 'The user clicked a link' is a training gap, not a root cause you fix at 2am. Find the technical cause first."
Visual: a chain with a green marker at the right stopping point and red markers either side.

SLIDE 10 — THE FISHBONE
Title: "Six Places a SOC Fault Hides"
Fishbone (Ishikawa) diagram with six branches:
- AGENT: Is the service running? Right version? Right config?
- NETWORK: Can the host reach the server? A firewall rule blocking it?
- SERVER: Manager up? Disk full? Indexer accepting writes?
- CONFIGURATION: Did somebody change a rule, filter, or log level?
- HOST: Did it reboot? Is it patched? Is it even on?
- PROCESS: Is there a change notice? Did somebody do this on purpose?
Add the line: "You will always have twelve possible causes. Then ask the question that turns a mess into a method: WHICH OF THESE CAN I TEST IN UNDER FIVE MINUTES?"
Visual: a proper fishbone diagram, six labelled bones.

SLIDE 11 — THREE OPTIONS, THREE FILTERS
Title: "Never Fix It With Your First Idea"
Top half — an option table for "four servers stopped reporting" (Option, Costs, Risks, Within my authority?):
Restart the agent service on all four | 5 min | Loses in-flight events | YES
Reboot the four servers | 30 min + downtime | Business impact | NO — escalate
Wait for the maintenance window to end | 0 | Delay if it is not the change | YES, with documentation
Escalate to IT immediately | 5 min | Wastes their time if expected | YES
Bottom half — the three filters, in order:
1. Is it within my authority? If no, it is not an option — it is an escalation.
2. Is it reversible? Prefer the fix you can undo.
3. Is it the smallest thing that could work? Restart the service before you reboot the host.
Add the line: "The dangerous analyst is not the one who does not know. It is the one who does something big and irreversible because it felt decisive."
Visual: table on top, three numbered filter gates below.

SLIDE 12 — THE SHAPE OF AN ACTION PLAN
Title: "Seven Things Every Action Plan Has"
Table (Field / What goes in it):
PROBLEM | One paragraph: what, when, scope, boundary
CAUSE | The root cause, stated as something changeable
ACTION | Numbered steps, each one a single verifiable act
WHO | A named person or role per step
WHEN | A time or deadline per step
HOW WE WILL KNOW IT WORKED | The observable test
IF IT DOES NOT WORK | The fallback, and who to escalate to
Add the line: "The last two are the ones people leave out, and they are the two that make it a plan rather than a wish."
Visual: a seven-field form layout.

SLIDE 13 — A REAL ACTION PLAN
Title: "One Written Out in Full"
Show the worked plan in a monospace block:
PROBLEM  Since 2026-04-18, detection "Trojan.Agent.XZ" is cleaned on WKS-118
         every weekday between 08:05 and 08:20. No other host affected.
         The user logs in at approximately 08:00.
CAUSE    Remediation incomplete. A scheduled task re-downloads the payload
         at logon. AV removes the file, not the task.
ACTION   1. Export scheduled task list from WKS-118      (L1, today 14:00)
         2. Identify the task that runs at logon         (L1, today 14:30)
         3. Escalate task removal to L2                  (L1, today 15:00)
         4. Full AV scan after removal                   (L2, today 16:00)
         5. Verify at next user logon                    (L1, tomorrow 08:30)
SUCCESS  No detection in the 08:05-08:20 window for three consecutive
         working days.
FALLBACK If it recurs after removal, escalate to the information security
         manager — a second persistence mechanism exists.
Add two callouts: "Step 3 is an escalation, and that is CORRECT — deleting a task changes system state." and "Success is defined in advance, with a number. 'Seems fixed' is not a test."
Visual: keep the monospace block; highlight step 3 and the SUCCESS line.

SLIDE 14 — SAME PLAN, THREE AUDIENCES
Title: "You Will Say It Three Different Ways"
Three columns:
- YOUR L2 / SUPERVISOR: technical detail · what you already tested · what you need from them · 3-4 sentences
- THE CLIENT: what is happening · what it means for them · when they hear next · 2 sentences, NO jargon
- THE TICKET: everything, in order, with timestamps · the permanent record · as long as it needs to be
Add the line: "Notice what gets dropped for the client, and notice that nothing is ever dropped from the ticket."
Visual: one plan icon with three arrows to three different recipient icons.

SLIDE 15 — SIXTY SECONDS
Title: "You Get Sixty Seconds"
Big central statement: "60 SECONDS"
Below: "That is genuinely how long you have to brief your supervisor. Your L2 has eleven other things happening."
What has to fit:
- The ticket number
- What is wrong, in one sentence
- What you already checked
- What you are asking for
Add the line: "Your trainer will cut you off at 60 seconds. That is not cruelty — it is the actual job."
Visual: a large stopwatch at 60 seconds with a four-item list beside it.

SLIDE 16 — WHAT AN ALERT COSTS
Title: "Every Decision You Make Spends Somebody's Money"
Table (Thing / What it costs the business):
An alert triaged well the first time | About 8 minutes of L1 time
The same alert escalated wrongly to L2 | About 45 minutes of L2 time, plus yours
A missed critical alert | A client incident, a contract penalty, sometimes the contract
A false escalation at 3am | An on-call manager's night, and their trust in you
Add the line: "Nobody hands an L1 analyst a budget. But analysts who understand this get promoted, because they escalate the right things."
Visual: a cost-comparison bar chart, the missed-critical bar dramatically larger.

SLIDE 17 — THIS AFTERNOON
Title: "This Afternoon — On Your Own, 1:00 to 5:00"
Mark this as the start of a new section, but keep the task list on this slide.
Table (Task, Time, Hand in):
1 | Set your personal and career goals | 40 min | Goal Sheet
2 | Recognising emotions — written reflection | 30 min | Three honest sentences
3 | Learning-style inventory and your strategy | 30 min | Goal Sheet, part 2
4 | Write one SOP Improvement Proposal | 40 min | Proposal form
5 | Swap proposals — comment on a partner's | 20 min | One comment, one question
6 | Finish your fault drill worksheets | 30 min | Problem-Solving Worksheets
Add the line: "Task 5 needs a partner. Message your teammate — you have their number from yesterday."
Visual: a teal section band, then the table.

SLIDE 18 — YOUR GOALS AND THE LADDER
Title: "Where Can This Actually Go?"
Show the career ladder as a diagram:
  L1 Analyst → L2 Analyst → L3 / Threat Hunter → SOC Lead
  with side branches from L1: Help desk support; from L2: Vulnerability Management;
  from L3: Incident Response / Forensics
Below, the two kinds of goal (Personal / Career):
PERSONAL: who you want to be · often lifelong · "Support my family without being absent from it"
CAREER: what you want to do · 1-5 years · "Move from L1 to L2 within two years"
On your Goal Sheet, write: one personal goal · a 1-year and a 3-year career goal · two things you must learn · ONE thing you will do in the next 30 days.
Add the line: "The 30-day item is the only one that is really a decision. The rest are wishes until it is done."
Visual: the ladder diagram with branches.

SLIDE 19 — WHAT PRESSURE DOES TO YOU
Title: "Four States That Change How You Work"
Table (State / What it feels like / What it does to your work / What to do):
ALERT FATIGUE | Numb, clicking through | You close things without reading | Stand up. Take five. Re-read the last three you closed.
PANIC | Racing, tunnel vision | You skip steps and forget to record | Go back to the SOP. Follow it literally. It exists for this.
FRUSTRATION | Snappy, blaming the tool | You stop asking for help | Say out loud that you are stuck. That is the whole fix.
OVERCONFIDENCE | Certain, fast, skipping checks | You escalate the wrong thing | Slow down. Verify one thing you "already know."
Add the line: "Shift work burns people out faster than almost any other IT role. The ones who last are the ones who can tell when they are running out."
Second line: "Your reflection is private. Write it honestly — nobody reads it but you and your trainer."
Visual: four state cards with simple face or gauge icons.

SLIDE 20 — INNOVATION, AND WHAT IS NEXT
Title: "Notice One Annoying Thing — Then Write It Down"
Four signals that something needs improving (with examples):
REPETITION | "I do this every single shift" | Copying alert details into the ticket by hand
WORKAROUND | "You just have to know to do X first" | An undocumented step everyone learned the hard way
COMPLAINT | "This always happens on Mondays" | A rule that fires on a scheduled backup job
NEAR MISS | "We nearly missed that one" | A real alert buried under false positives
Then: "Write ONE proposal about something you genuinely noticed yesterday or today."
Big reassurance box: "Innovation does not mean clever. 'Add one field to the handover template' is a completely valid proposal — and it is the kind that actually gets adopted."
Closing line: "Next — Day 3: information handling, safety, environment and quality. You will learn how to judge whether a threat intelligence source can be trusted. Acting on a bad source is worse than acting on nothing."
Visual: four signal cards, then a proposal form icon and a small Day 2 of 15 progress bar.

============================================================
END OF PROMPT
============================================================
