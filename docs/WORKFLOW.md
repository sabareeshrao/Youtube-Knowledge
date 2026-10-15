# Ingestion, indexing, and identity rules

## 1. Separate layers — do not mix

**VIDEO-LIBRARY** is the chronological and standalone record of *one* video. Each folder has `transcript.md` (as received, including its YouTube URL and linked subtitles) and `timestamps.md` (curated timestamp sections, importance classification, summaries, and any demonstrated code). Timestamp links jump to opening positions, never invented end positions. All sections, even NO NEED, can be shown in the video library.

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
Each `timestamp_ids` entry MUST exist as a heading in its parent video's `timestamps.md`. The question file groups the source timestamps in exactly these per-video batches. Code stays with the video section demonstrating it; the syllabus links to that section. An existing question may gain another video source without getting another question ID.

`REGISTRY/counters.json` stores the **next unallocated** video number and next question number for each subject prefix. Counters must be strictly greater than any registered number and never decremented, including after deletions.

## 4. Video timestamp format

In `VIDEO-LIBRARY/YT-1/timestamps.md`, each section begins with a machine-readable heading:
```md
### YT-1.1 — [03:34](https://www.youtube.com/watch?v=ndTM5I2vtYQ&t=214s) — 🟢 USEFUL: Anonymous object definition

Brief explanation based on the source video.
```
Classification must be exactly one of `🔴 NO NEED`, `🟡 INTRO`, `🟢 USEFUL`. Keep original source terminology unless correcting it is specifically requested; if adding independent technical notes, mark them clearly as such. Timestamps are **starting positions** only. Group contiguous subtitle rows into useful sections without inventing timing or demonstrations.

## 5. Ingestion transaction

1. Read all three registries and `INDEX.md` from GitHub; do not trust remembered counters.
2. Parse the incoming `.md` transcript's original URL and all linked subtitle starting positions. Verify URLs refer to the same video.
3. Normalize the 11-character YouTube video ID; if registered, **update that YT folder** rather than allocate another `YT-n`.
4. If new, allocate `YT-n` from the counter; preserve the incoming transcript in `transcript.md`, classify video sections into `timestamps.md`, and register the original video ID. Do not modify existing timestamp IDs when revising segmentation; retire or redirect obsolete references deliberately.
5. Search existing interview-question registry for exact and semantic matches, then **reuse** or allocate `IJ-n` / `IP-n` / other subject IDs. Link each question's sources by video ID and timestamp IDs, keeping code with each video.
6. Update question Markdown files, all registries, and `INDEX.md` together.
7. Run `python scripts/validate.py`. Commit a single coherent change; use a PR/branch and passing validation for concurrent contributions. If GitHub rejects a stale branch update, reread current registries and reassign based on latest counters.

## 6. Important limitations

The validator detects duplicate *IDs*, duplicate original YouTube video IDs, dangling references, improper timestamp URLs, missing records, and stale counters. It **cannot** automatically judge whether two differently worded questions ask the same thing, whether subtitles are accurate, or whether code in the transcript is correct. Those need review.
