# AI Build Instructions — YouTube Knowledge

**Read this file first whenever the user uploads or pastes a YouTube transcript.** This repository is the long-term source of truth; never assign IDs based only on chat memory.

## Goal

Turn **any timestamped video transcript**, including ordinary tutorials, lectures, walkthroughs, code demonstrations, and mock interviews, into:
1. A **pure, independent YT-n video library** containing the unmodified original transcript, every unique curated timestamp in chronological question-headed tables, and a question-grouped video view.
2. A **shared subject interview syllabus** of real interview-style questions with permanent IDs. Reuse existing questions across videos, but isolate every video's timestamps, examples, and answers.

**Tutorial does NOT mean an interview occurred.** Turn its taught concepts into useful interview-style questions; never invent an interviewer or candidate.

## Read order for each ingestion

1. `AGENTS.md` (this document).
2. [Detailed ingestion playbook](docs/TRANSCRIPT-INGESTION.md).
3. [Existing repository identity rules](docs/WORKFLOW.md).
4. Live `REGISTRY/videos.json`, `REGISTRY/questions.json`, `REGISTRY/counters.json`, `REGISTRY/answer-comparisons.json`, and `INDEX.md`.
5. [Examples and templates](TEMPLATES/); then the incoming transcript, **all the way through**, not merely an excerpt.

## Decide source type by actual conversation, not filename

- **`interview`**: An identifiable candidate actually answers questions. Use a **2-column comparison table** under each video's timestamp group: `Candidate response — original caption transcript (unedited excerpt)` | `AI answer — clear interview explanation`. If there is no response, say that instead of inventing one.
- **`tutorial`**: A single instructor teaches, codes, demonstrates, narrates, or explains (even if the instructor asks rhetorical questions or the video title says “interview”). **No candidate answer column.** Show a **1-column AI answer table**, immediately below the related timestamp table, headed `### AI answer — YT-n`. Explain the concept accurately and in a natural interview-answer voice, explicitly separating facts taught in the source from added AI clarification.
- Different videos linked to the **same question** may use different answer modes, because the mode is per **source video**, not per question.
- Videos with both a real candidate interview and tutorial segments should classify each question/video source accurately, using a mode override only if necessary; avoid attributing instructor explanations to the candidate. See the playbook.

## Permanent naming and no duplicate data

- Allocate the next free unpadded video ID `YT-1`, `YT-2`, ..., based on the original 11-character YouTube ID, not the title or URL parameters.
- For each video, independent permanent section IDs `YT-2.1`, `YT-2.2`, etc. Never renumber previously published IDs; sort the **display** by actual video time.
- Java questions `IJ-1`, Python `IP-1`, Spring Boot `IS-1`, and other existing subject-specific ID streams from the registry.
- Search existing questions **semantically** before assigning a new question ID. Ten videos teaching the same HashMap concept can be ten *video options under one IJ question*, not ten duplicate questions.
- A section ID must never reference timestamps from a different video. No invented start times or misleading “exact” precision when the transcript is not timed.

## Exact output rules

- Original `VIDEO-LIBRARY/YT-n/transcript.md` remains unchanged.
- `VIDEO-LIBRARY/YT-n/timeline.md`: all **unique** curated `YT-n.m` sections exactly once, chronological, including 🔴 NO NEED, 🟡 INTRO, 🟢 USEFUL; individual question-shaped chapter headings and isolated tables.
- `VIDEO-LIBRARY/YT-n/timestamps.md`: topics reframed as **full interview questions** with a separate timestamp table per question; same **single video** only; beneath each, show that video's correct answer mode.
- `INTERVIEW-SYLLABUS/SUBJECT/QUESTION-ID.md`: one canonical question. Under each `## Video option — YT-n: title` show ONLY that video's relevant timestamp table and corresponding interview comparison **or** tutorial AI-only answer.
- Timestamp links must be `[mm:ss](https://www.youtube.com/watch?v=REAL_VIDEO_ID&t=SECONDSs)` using **start positions only**.
- No “Detailed video notes” link spam, random timestamp lists, merged video groups, fabricated candidate speech, or fabricated code.
- If the video demonstrates code and its exact code is in the transcript, attribute it to that video. Clearly mark any newly authored runnable code as `AI-created example`; keep source code separate and ensure any Java voice-typing teaching example includes `// Voice:` comments and expected output where applicable.
- Index both video navigation and questions/tags. Keep existing ID references working.

## Answer registry contract (backward compatible)

Canonical file: `REGISTRY/answer-comparisons.json`, **one record per** `(question_id, video_id)`.

- Interview: `{"question_id":"IJ-1","video_id":"YT-1","candidate_answer":"Verbatim candidate caption text...","candidate_transcript_rows":[{"seconds":12,"clock":"0:12","text":"Verbatim caption text..."}],"ai_corrected_answer":"Clear spoken interview answer with one example..."}`.
- Tutorial: `{"question_id":"IJ-1","video_id":"YT-2","answer_type":"ai_only","ai_answer":"Accurate AI-authored response..."}`. **Omit** `candidate_answer` and `ai_corrected_answer`.
- Mark each video in `REGISTRY/videos.json` with `"type":"interview"` or `"type":"tutorial"`. Existing video `YT-1` is `interview`. Legacy interview records with no `answer_type` remain valid.
- Optional mixed-mode override `"answer_type":"ai_only"` is only for a video section with no candidate at all; an otherwise interviewed candidate must not be silently erased. Consult detailed rules before overriding.
- AI answers may be richer than the transcript, but make clear which details are independent explanations/corrections and never describe them as spoken or demonstrated.

## Publish checklist

1. Read the current registries and all transcript sections; detect duplicates and preserve timestamps.
2. Classify video source and question-level answer mode; build the 3 source files and all affected existing/new syllabus files with isolated tables.
3. Update `videos.json`, `questions.json`, `answer-comparisons.json`, `counters.json`, and `INDEX.md` together.
4. Run `python scripts/validate.py` and `python scripts/test_validator_modes.py`.
5. Commit a coherent update (prefer one atomic commit or PR), verify GitHub Actions passes, and report created/reused IDs and links. **Never claim success before verification.**

If the supplied transcript has no reliable timed captions or original video ID, obtain the missing input rather than inventing timestamps or videos.

## Mandatory answer writing instructions

Read [docs/ANSWER-STYLE.md](docs/ANSWER-STYLE.md) for the full enforced standard. **Every new and revised interview answer must use simple spoken English, one relevant example, and a memorable takeaway. Interview candidate text is verbatim captions, not a paraphrase. Tutorials have only an AI answer.**
