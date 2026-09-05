# Capstone evidence and feedback

The project passes the practice course when every applicable gate has evidence. A quality score cannot compensate for a missing gate.

| Gate | Required evidence |
| --- | --- |
| Behavior | Required journeys, empty input, boundaries and failures work |
| Reproduction | A clean copy runs through the documented uv commands |
| Quality | Focused pytest tests, Ruff and Pyright pass for your project |
| Understanding | Explain the main data flow and one design alternative |
| Independence | One complete behavior and test were implemented without generated source |
| Recovery | Inspect a diff and restore a known state while preserving an unrelated file |
| Collaboration workflow | Live issue/PR/review/checks/merge OR labelled local review and conflict simulation |
| Agent review | Bounded proposal, inspected diff, specific keep/revise/reject decision and verification |
| Handoff | Accurate README, data location, limitations, commands and recovery |

## Distinguish the two collaboration records

**Live human collaboration** requires another person's review and your response, plus final checks and the merge decision. Preserve the real links and commit. A self-review, stored comment or agent review cannot claim this designation.

**Local review simulation** requires the supplied two-branch exercise, stored-comment response, resolved conflict, passing commands and final local commit. It completes the practice workflow gate without claiming a remote PR, hosted CI or another participant.

## Quality feedback after the gates

For each area, record 1 (works but needs explanation), 2 (clear and consistent), or 3 (a new contributor can verify and extend it): behavior, tests, design, command experience, collaboration record and maintenance. Explain each score with one example. Scores are feedback, not a substitute for the gates.

## Reviewer questions

- Which input would disprove the claimed behavior?
- Where does external data become trusted internal data?
- What happens if the data file is malformed?
- Which changed line was unnecessary, and why?
- What was implemented independently?
- How can the previous working version be restored?

If there is no live reviewer, answer these in writing and label the record as self-review. Keep the live-collaboration designation pending until another person participates.
