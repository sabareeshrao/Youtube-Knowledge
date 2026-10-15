# Ingestion, indexing, and identity rules

## 1. Separate layers — do not mix

**VIDEO-LIBRARY** is the chronological and standalone record of *one* video. Each folder has `transcript.md` (as received, including its YouTube URL and linked subtitles) and `timestamps.md` (individually headed question tables), and `timeline.md` (pure chronological tables). Timestamp links jump to opening positions, never invented end positions. All sections, even NO NEED, can be shown in the video library.

**INTERVIEW-SYLLABUS** organizes interview questions by topic and groups timestamp references by `YT-n` video. It never combines sections from two videos into a single video option. The interview question is a single canonical record even when ten videos cover it. Show video choices rather than forcing repeated viewing.

## 2. IDs

- `YT-1`, `YT-2`: one per **distinct original YouTube video ID**, not title or URL formatting.
- `YT-1.1`, `YT-1.2`: permanently assigned timestamp-section IDs within YT-1. A later insertion gets a NEW numeric suffix even if its display position is earlier. Sort video sections by actual time, **not** by suffix.
- `IJ-1`, `IP-1`, `IS-1`: distinct interview-question concepts for Java / Python / Spring Boot. Add other subject prefixes to `REGISTRY/counters.json` as needed.
- No zero padding, no ID reuse, no reassignment. Sort numbers numerically, not lexically.
- Merge/rename questions without reusing old IDs; add any redirect to `REGISTRY/redirects.json`. Reuse the existing ID if the new transcript explains the same interview question.
- Structural duplicate detection is automatic. Semantic question matching requires comparing questions **before** allocating IDs. Similar wording may represent the same interview concept.

## 3. Exact registry schemas

`REGISTRY/videos.json` has an array `videos`:
```json
{
  "videos": [
    {
      "id": "YT-1",
      "youtube_id": "ndTM5I2vtYQ",
      "title": "#46 Anonymous Object in Java",
      "tags": ["java", "objects", "anonymous-objects"],
      "transcript": "VIDEO-LIBRARY/YT-1/transcript.md",
      "timestamps": "VIDEO-LIBRARY/YT-1/timestamps.md"
    }
  ]
}
```
The above is **an example of a future first record**, not a claim that it has been ingested.

`REGISTRY/questions.json` has an array `questions`:
```json
{
  "questions": [
    {
      "id": "IJ-1",
      "subject": "JAVA",
      "question": "What is an anonymous object in Java?",
      "tags": ["java", "anonymous-objects", "object-creation"],
      "path": "INTERVIEW-SYLLABUS/JAVA/IJ-1.md",
      "sources": [
        {"video_id": "YT-1", "timestamp_ids": ["YT-1.1", "YT-1.3"]}
      ]
    }
  ]
}
```
Each `timestamp_ids` entry MUST exist as a table row in the source video's `timeline.md` and also in the matching question table. The question file groups the source timestamps in exactly these per-video batches. Code stays with the video section demonstrating it; the syllabus links to that section. An existing question may gain another video source without getting another question ID.

`REGISTRY/counters.json` stores the **next unallocated** video number and next question number for each subject prefix. Counters must be strictly greater than any registered number and never decremented, including after deletions.

## 4. Mandatory headings and tables

**Three maintained documents per video:**
- `transcript.md` stores the exact uploaded linked transcript, unchanged.
- `timestamps.md` shows **only this video's** timestamps, grouped under **full interview-question headings** like `## IJ-1 — What is a HashMap in Java?`. Each heading is followed by an isolated 4-column Markdown table: `ID | Watch | Type | What you will learn`. A section can be referenced by several question groups without changing its permanent ID.
- `timeline.md` stores every unique `YT-n.m` video timestamp **exactly once**, strictly in chronological video order, with topic/question chapter headings followed by separate Markdown tables. This file is the canonical timestamp inventory validated by GitHub Actions.

**One interview question document per question:** `INTERVIEW-SYLLABUS/SUBJECT/ID.md` begins with the complete actual-or-curated interview question. Then create a `## Video option — YT-n: title` heading and separate table for each relevant video. Never mix two YT IDs in one table. Clicking a timestamp goes to its start position in the original video; closing timestamps are unnecessary.

**Use this row shape:**

```md
| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.4 | [02:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) | 🟢 USEFUL | Spring Security end-to-end question |
```

Avoid bare link lists and 'Detailed video notes' links. Intro, useful and skip labels are preserved. Questions may be *curated from the discussion*, rather than asserted verbatim. Never invent code that was not included in the provided source transcript. Consult [TEMPLATES/](../TEMPLATES/).

## 5. Ingestion transaction

1. Read all three registries and `INDEX.md` from GitHub; do not trust remembered counters.
2. Parse the incoming `.md` transcript's original URL and all linked subtitle starting positions. Verify URLs refer to the same video.
3. Normalize the 11-character YouTube video ID; if registered, **update that YT folder** rather than allocate another `YT-n`.
4. If new, allocate `YT-n` from the counter; preserve the incoming transcript in `transcript.md`, classify video sections into question-headed `timestamps.md` and fully chronological `timeline.md` tables, and register the original video ID. Do not modify existing timestamp IDs when revising segmentation; retire or redirect obsolete references deliberately.
5. Search existing interview-question registry for exact and semantic matches, then **reuse** or allocate `IJ-n` / `IP-n` / other subject IDs. Link each question's sources by video ID and timestamp IDs, keeping code with each video.
6. Update question Markdown files, all registries, and `INDEX.md` together.
7. Run `python scripts/validate.py`. Commit a single coherent change; use a PR/branch and passing validation for concurrent contributions. If GitHub rejects a stale branch update, reread current registries and reassign based on latest counters.

## 6. Important limitations

The validator detects duplicate *IDs*, duplicate original YouTube video IDs, dangling references, improper timestamp URLs, missing records, and stale counters. It **cannot** automatically judge whether two differently worded questions ask the same thing, whether subtitles are accurate, or whether code in the transcript is correct. Those need review.

## Subject codes introduced with YT-1

`IJ` Java; `IP` Python; `IS` Spring Boot (including Spring Security/Hibernate); `IA` System Design/Architecture; `ID` Database; `IC` Cloud/DevOps; `IT` Testing. Each is independently numbered from 1, and none may be reused for a different subject. The question groups remain separate from the standalone per-video chronology.
