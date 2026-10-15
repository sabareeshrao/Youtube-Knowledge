# YouTube Knowledge

A permanent GitHub library of timestamped YouTube lessons and interview questions.

## Two independent ways to study

1. **[VIDEO-LIBRARY](VIDEO-LIBRARY/)** — One folder per YouTube video, preserving its full linked transcript and its own chronological, clickable topic timestamps. Sections are classified 🔴 NO NEED / 🟡 INTRO / 🟢 USEFUL. Never mix two videos on a video page.
2. **[INTERVIEW-SYLLABUS](INTERVIEW-SYLLABUS/)** — One file per interview question. Questions group relevant timestamps **by source video**, so you can pick one explanation and its related code instead of watching ten redundant videos.

## ID system (no leading zeros)

| Record | Example | Rule |
| --- | --- | --- |
| YouTube video | `YT-1`, `YT-2000` | One ID per original YouTube video ID |
| Timestamp section | `YT-1.1`, `YT-1.2` | Unique within that video; IDs never recycled |
| Java interview question | `IJ-1` | One permanent question per distinct interview concept |
| Python interview question | `IP-1` | Independent Python sequence |
| Spring Boot interview question | `IS-1` | Independent Spring Boot sequence |

Question pages reference the **original timestamp IDs** (not copies of timestamp records). Each video option stays in its own group. Similar interview questions are checked before assigning a new question ID.

## Repository layout

```text
VIDEO-LIBRARY/YT-1/transcript.md       # original timestamped transcript, preserved
VIDEO-LIBRARY/YT-1/timestamps.md       # sorted video topics + clickable video links + code
INTERVIEW-SYLLABUS/JAVA/IJ-1.md        # one question, video options grouped separately
INTERVIEW-SYLLABUS/PYTHON/IP-1.md
INTERVIEW-SYLLABUS/SPRING-BOOT/IS-1.md
REGISTRY/counters.json                 # next available numbers
REGISTRY/videos.json                   # unique source videos and their paths
REGISTRY/questions.json                # questions, topics, and referenced section IDs
INDEX.md                               # human-friendly entry point
TEMPLATES/                             # templates for new records
docs/WORKFLOW.md                       # ingestion and uniqueness rules
scripts/validate.py                    # integrity checks; also runs in GitHub Actions
```

Folders named with IDs above are **future examples**, not registered content. The live registry begins empty; the first transcript is assigned `YT-1`.

## Add the first transcript

Upload a `.md` file containing the YouTube URL and clickable timestamped subtitles in the chat. Processing should:

1. Read existing registries **before** allocating any IDs.
2. Check the original 11-character YouTube video ID for duplicates.
3. Preserve the original transcript in its own video folder; create sorted 🔴/🟡/🟢 timestamp sections with opening-time hyperlinks and code when present.
4. Identify interview questions; reuse existing matching question IDs after semantic review; link each question to this video's specific `YT-<n>.<m>` sections.
5. Update registries and [INDEX.md](INDEX.md) together; run `python scripts/validate.py` before merging.

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the exact schemas and publishing checklist.
