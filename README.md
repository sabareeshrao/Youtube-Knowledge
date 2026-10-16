# YouTube Knowledge

A permanent, searchable library that turns **any timestamped YouTube video (including tutorials and mock interviews)** into interview-style questions and precise clickable source sections.

**AI contributor instructions:** [AGENTS.md](AGENTS.md) · [Transcript ingestion playbook](docs/TRANSCRIPT-INGESTION.md). Read these before handling a new transcript.

## Two separate study views

**[VIDEO-LIBRARY/](VIDEO-LIBRARY/)** — Open a video on its own. Each `YT-n` folder keeps the original linked transcript and isolated interview-question timestamp tables, a separate chronological `timeline.md`, and topic classifications (🔴 NO NEED / 🟡 INTRO / 🟢 USEFUL), and code demonstrated in that video. Never mix timestamps from different videos.

**[INTERVIEW-SYLLABUS/](INTERVIEW-SYLLABUS/)** — Open a specific interview question. Its page groups video timestamps by `YT-n`, so you can choose one video's group of timestamp links in its **own table**, without mixing timestamps from ten videos. Different subjects have independent question IDs.

## Simple, permanent IDs

| Record | IDs | Meaning |
|---|---|---|
| YouTube videos | `YT-1`, `YT-2`, ... `YT-2000` | One ID for each distinct original YouTube video ID |
| Timestamp sections | `YT-1.1`, `YT-1.2` | One numbered section within a video |
| Java interview questions | `IJ-1`, `IJ-2` | One canonical Java interview question per concept |
| Python interview questions | `IP-1`, `IP-2` | Separate Python sequence |
| Spring Boot interview questions | `IS-1`, `IS-2` | Separate Spring Boot sequence |

Never add leading zeros or reuse IDs. If a video is added twice, reuse its existing `YT-n`. If a new video teaches an existing interview question, add its video group under the *existing question ID*.

## Repository organization

```text
VIDEO-LIBRARY/
  YT-1/
    transcript.md       # original timestamped source
    timestamps.md       # questions as headings, separate clickable timestamp tables
    timeline.md         # all timestamps chronologically, grouped in tables

INTERVIEW-SYLLABUS/
  JAVA/IJ-1.md          # one interview question, separate video options
  PYTHON/IP-1.md
  SPRING-BOOT/IS-1.md

REGISTRY/
  counters.json         # next IDs
  videos.json           # unique YouTube IDs, paths, keywords
  questions.json        # canonical questions, tags, video-section references
  redirects.json        # never reuse retired IDs

TEMPLATES/               # examples, not real registered content
docs/WORKFLOW.md         # detailed naming, schema and ingestion rules
scripts/validate.py      # structural duplicate and broken-link checks
INDEX.md                 # human-friendly navigation
```

The repository already contains **YT-1** (an interview) and its question bank. Paths elsewhere in this README can also illustrate future videos; always read the live registries for actual IDs.

## Next transcript workflow

1. Upload a Markdown (`.md`) file with the main YouTube URL and clickable subtitle timestamps.
2. Read [REGISTRY/videos.json](REGISTRY/videos.json), [REGISTRY/questions.json](REGISTRY/questions.json), and [REGISTRY/counters.json](REGISTRY/counters.json) from GitHub first.
3. Identify existing video/question matches; allocate IDs only when new. Preserve original transcript, create a pure video-timeline file and corresponding interview syllabus question files.
4. Add video-grouped references, keep each code sample with its video's sections, update registries and [INDEX.md](INDEX.md), and validate before committing.

See [INDEX.md](INDEX.md) to browse, [docs/WORKFLOW.md](docs/WORKFLOW.md) for the schemas and rules, or [TEMPLATES/](TEMPLATES/) for starter page formats.

**Existing interview:** YT-1. Next video ID and all question IDs must be read live from the registries—do not trust old instructions for counters.

## Presentation rules

- **Every relevant group has a full interview-question heading and a dedicated Markdown table.** Never output a loose list of random linked timestamps.
- The VIDEO-LIBRARY/timestamps.md page shows question-grouped tables for a **single video only**; its timeline.md is the complete chronological single-video index.
- Each INTERVIEW-SYLLABUS question contains a separate headed table for **each video option**. Do not mix timestamps from different YT IDs.
- Preserve original linked transcript independently. No "Detailed video notes" clutter or invented runnable code.

## Side-by-side candidate and AI-corrected answers

Every interview-question page now contains a **two-column comparison** under the timestamp table of each source video. Left: candidate's original timestamped caption excerpt, copied without rewriting. Right: independently authored AI correction, including missing details or fixes. The [answer-comparison registry](REGISTRY/answer-comparisons.json) keeps the pair associated with its question ID and video ID. These answers also appear on the question-grouped video page.

## Interview versus tutorial answer modes

| Uploaded recording | Question treatment | Answer section below each video's timestamps |
|---|---|---|
| Mock interview with candidate | Existing interviewer questions plus meaningful follow-ups | **Two columns:** candidate response (verbatim raw transcript excerpt) **vs** AI-corrected answer |
| Tutorial, lecture, walkthrough, lesson, coding demonstration | Convert taught concepts into realistic interview-style questions | **One column:** AI answer only — no candidate column, no invented candidate |

The same canonical `IJ-n` question may have a **YT-1 interview video option** with a candidate comparison and a **YT-2 tutorial option** with an AI-only answer. IDs, timestamp tables, and video code are never mixed. The backend stores both formats in [REGISTRY/answer-comparisons.json](REGISTRY/answer-comparisons.json); tutorial records have `answer_type: "ai_only"` and `ai_answer`. See the [playbook](docs/TRANSCRIPT-INGESTION.md).

## Permanent answer standard (applies to all future transcripts)

**Read [ANSWER-STYLE](docs/ANSWER-STYLE.md) before generating answers.** AI answers are **simple spoken interview responses**: direct explanation, one concrete example, memorable takeaway, usually 65–100 words. The actual candidate column is an **unaltered excerpt of original timed captions**, never a paraphrase. Uncertain speaker boundaries are identified honestly. [Browse IT-1 as the model](INTERVIEW-SYLLABUS/TESTING/IT-1.md).
