# Transcript-to-Question Ingestion — Mandatory AI Playbook

This is the detailed execution plan for [AGENTS.md](../AGENTS.md). It applies to **both mock interviews and non-interview YouTube tutorials**. A user can paste a transcript in chat, upload `.md`/`.txt`, or provide a properly timestamped source.

## 0. Source classification

Look at who is actually speaking:

| Source | Questions generated | Answer display |
|---|---|---|
| Mock interview, with candidate responses | Interview questions from interviewer prompts and relevant follow-ups | **Two columns:** source-grounded verbatim candidate transcript excerpt vs AI-corrected answer |
| Tutorial / lecture / demo / lesson / programming walkthrough | Realistic interview-style questions distilled from topics in the tutor's explanation, including prerequisites when relevant | **One column:** AI answer only; do **not** show a candidate column |
| A tutorial narrator asks rhetorical interview questions | Interview-style questions based on taught content | **One column:** AI answer only; rhetorical questions are not candidate responses |
| A combined recording where an actual candidate answers some questions and an instructor teaches others | Evaluate **each video/question pair** accurately | Interview comparison for actual candidate responses; AI-only for instructor-only content |

A video's `type` is the predominant source type, `interview` or `tutorial`. If a genuinely mixed video contains an instructor-only segment, a tutorial answer record may explicitly declare `answer_type: "ai_only"` even when the parent video is `interview`, but the reviewer must confirm there is *no candidate answer* for that particular question. Never change an interview answer to AI-only just to hide a weak, incorrect, or missing candidate reply.

## 1. Parse and preserve the original

- Read the *entire* submitted transcript, including the end. Extract the original 11-character YouTube video ID and actual starting times from subtitle hyperlinks or SRT/VTT timing. If the file contains only un-timed prose, **do not invent exact timestamps**; request a timestamped version or state the limitation.
- Parse time as seconds; verify the video IDs of all provided links agree and display time and link target agree. When they disagree, resolve against trusted source data, otherwise flag/stop.
- Save **verbatim original input** in `VIDEO-LIBRARY/YT-n/transcript.md`, retaining original subtitles and links. If lessons are in other languages, provide the question titles, summaries and AI answers in English without replacing or misrepresenting raw source material.
- Detect duplicate original YouTube ID in `REGISTRY/videos.json` before allocating a new `YT-n`. If already present, update the existing video while preserving stable section IDs and existing question associations.
- Register the video `type` and `timeline`, `transcript`, `timestamps` paths.

## 2. Build the *pure independent video library*

- Every video is completely separate, e.g. `VIDEO-LIBRARY/YT-2/`. Do not embed YT-1 content into YT-2.
- Assign `YT-2.1`, `YT-2.2`, etc. to the video’s curated sections; preserve **all** section IDs on future editing. Source start links, never fake end times.
- **`timeline.md`** = all unique curated sections in video order. Group under question-shaped chapter headings; give every chapter a dedicated Markdown table with ID, Watch, Type and What you will learn. Include skip/intro/useful. One timestamp record per ID in this page.
- **`timestamps.md`** = source video only, question-first. Under each `## IJ-... — complete question?` or other subject prefix, show **isolated table** of this video's relevant sections (can reuse a section ID under several questions). Immediately below, place the correct answer form for that *source video* (see step 4).
- Keep a way to reach `timeline.md` and `transcript.md` from the video page. Do not replace the pure chronological view with syllabus aggregation.

### Clickable table format

```md
## IJ-4 — What causes HashMap collisions, and how are they handled?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-2.4 | [04:18](https://www.youtube.com/watch?v=ACTUAL_ID_1&t=258s) | 🟢 USEFUL | hashCode, buckets, collision handling |
| YT-2.6 | [07:32](https://www.youtube.com/watch?v=ACTUAL_ID_1&t=452s) | 🟢 USEFUL | equals and key matching |
```

Above is a *format illustration*; `ACTUAL_ID_1` is a placeholder, not a real ID. Never commit it as actual media.

## 3. Generate the shared interview syllabus

- For each meaningful topic, write a **specific, answerable interview-style question**. Do not force one new question for every subtitle fragment, and do not omit key taught material. A code demonstration may yield its own question if it teaches an independently testable concept.
- Existing questions may already cover the same idea using different wording. Search and compare `REGISTRY/questions.json` and current question files by meaning; **reuse the same permanent ID** whenever appropriate.
- Only after that comparison, allocate subject code from `REGISTRY/counters.json`: `IJ-n` Java, `IP-n` Python, `IS-n` Spring Boot, `IA-n` architecture, `ID-n` database, `IC-n` DevOps, `IT-n` testing; add new prefixes deliberately.
- Each question file has one canonical question at top, followed by **separate video options**, never interleaved:
  - `## Video option — YT-1: mock interview` → YT-1-only timestamp table + 2-column candidate/AI comparison.
  - `## Video option — YT-2: tutorial` → YT-2-only timestamp table + **AI answer only**.
- Code, terminology and examples belong with the actual video's section. AI-created code must be labeled. Distinguish tutorial content from AI elaboration.

## 4. Answer-mode rules and stored schema

Canonical registry `REGISTRY/answer-comparisons.json` is historically named for comparisons but also stores **tutorial AI-only answers**. Key is **`(question_id, video_id)`**. No two records can share that key.

**Interview source** (legacy entries without `answer_type` are valid):

```json
{
  "question_id": "IJ-1",
  "video_id": "YT-1",
  "candidate_answer": "Verbatim original candidate caption excerpt (do not rewrite).",
  "ai_corrected_answer": "Technically corrected interview response, separately authored."
}
```

Corresponding **2-column** Markdown table *under that video*:

```md
### Candidate answer vs. AI-corrected answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| Exact subtitle words copied without grammatical changes... | Explain hashing, collisions, equals and hashCode correctly... |
```

**Tutorial source** (no actual candidate exists):

```json
{
  "question_id": "IJ-1",
  "video_id": "YT-2",
  "answer_type": "ai_only",
  "ai_answer": "HashMap stores key-value entries and resolves key equality using hashCode and equals..."
}
```

Corresponding **1-column AI-answer-only** table; **never create an empty or invented candidate column**:

```md
### AI answer — YT-2

| AI answer |
|---|
| HashMap stores key-value pairs. A bucket is selected from the key's hash; equals distinguishes keys when hashes collide. |
```

This same answer block goes on `VIDEO-LIBRARY/YT-2/timestamps.md` beneath the question and on `INTERVIEW-SYLLABUS/JAVA/IJ-1.md` within `YT-2`'s video option. The AI answer is not a verbatim quotation from the tutor. Explain important technical corrections, if any, clearly and separately from what the tutor demonstrably said. If a tutorial fails to cover an aspect of the canonical question, either narrow its linked timestamps to the supported parts or clearly mark extra reasoning as AI enrichment.

**Enforced invariants:** Interviews cannot silently omit candidate comparisons. AI-only records must not include `candidate_answer` or `ai_corrected_answer`. Each video/question source requires exactly one answer record. Mixed `interview` + AI-only is permitted only when the particular segment genuinely has no candidate. Do not attribute answers to a fabricated student or interviewer.

## 5. Commit and verify, every time

1. Read live registries + `INDEX.md` from GitHub before ID allocation.
2. Preserve transcript, create/update `timeline.md` and `timestamps.md`, and generate question files with the correct source-specific tables.
3. Update `videos.json`, `questions.json`, `counters.json`, `answer-comparisons.json`, `INDEX.md` in one coherent change. Reuse question IDs and preserve all permanent time section IDs; avoid double registration.
4. Run `python scripts/validate.py` and `python scripts/test_validator_modes.py` and inspect the results; inspect relevant original transcript sections for fidelity.
5. Confirm GitHub Actions passes. Only then tell the user the video was ingested with links to the pure timeline and question syllabus.

**What the validator cannot prove:** semantic question deduplication, source-to-topic alignment, accurate paraphrasing, technical correctness, authentic code, or audio-level seeking precision. Manually audit those parts; do not claim perfect synchronization because numerical timestamp checks pass.

## 6. New input checklist

Given the next transcript:
- [ ] Source has original YouTube URL and reliable start timestamps
- [ ] Original video ID duplicate check, source classified as interview/tutorial/mixed
- [ ] All content read and important concepts grouped into interview-style questions
- [ ] Original transcript preserved; chronological timeline produced
- [ ] Per-video question-first tables and correct candidate/AI-only answers
- [ ] Existing canonical interview question reused where topic already exists
- [ ] Video-option timestamps/answers separated by YT ID
- [ ] Registries/index updated; validation and GitHub Actions pass

## New permanent answer-writing standard

All AI answers must follow [docs/ANSWER-STYLE.md](ANSWER-STYLE.md): spoken, direct, simple, one useful example, a memorable final takeaway, usually 65–100 words, technically accurate. The candidate side must contain original verbatim subtitle excerpts, not AI summaries. Store each excerpt's source caption times and verbatim text in `candidate_transcript_rows`; if no substantive answer exists, mark it explicitly. For tutorial/non-interview video sections, use only one AI-answer column with the same simple spoken style.
