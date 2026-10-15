# YouTube Knowledge

A permanent, searchable library of timestamped YouTube tutorials and interview questions.

## Two separate study views

**[VIDEO-LIBRARY/](VIDEO-LIBRARY/)** — Open a video on its own. Each `YT-n` folder keeps the original linked transcript and an independent chronological list of clickable starting timestamps, topic classifications (🔴 NO NEED / 🟡 INTRO / 🟢 USEFUL), and code demonstrated in that video. Never mix timestamps from different videos.

**[INTERVIEW-SYLLABUS/](INTERVIEW-SYLLABUS/)** — Open a specific interview question. Its page groups video timestamps by `YT-n`, so you can choose one video's complete relevant sections and code instead of watching ten repeat explanations. Different subjects have independent question IDs.

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
    timestamps.md       # pure video timeline, clickable links, codes

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

Folder paths containing `YT-1` and `IJ-1` above are **examples of files to be added**, not video records already ingested. Everything starts empty.

## First transcript workflow

1. Upload a Markdown (`.md`) file with the main YouTube URL and clickable subtitle timestamps.
2. Read [REGISTRY/videos.json](REGISTRY/videos.json), [REGISTRY/questions.json](REGISTRY/questions.json), and [REGISTRY/counters.json](REGISTRY/counters.json) from GitHub first.
3. Identify existing video/question matches; allocate IDs only when new. Preserve original transcript, create a pure video-timeline file and corresponding interview syllabus question files.
4. Add video-grouped references, keep each code sample with its video's sections, update registries and [INDEX.md](INDEX.md), and validate before committing.

See [INDEX.md](INDEX.md) to browse, [docs/WORKFLOW.md](docs/WORKFLOW.md) for the schemas and rules, or [TEMPLATES/](TEMPLATES/) for starter page formats.

**Current state:** Initialized, waiting for the first transcript. Next unallocated video ID: `YT-1`; question IDs: `IJ-1`, `IP-1`, `IS-1`.
