#!/usr/bin/env python3
"""Validate unique IDs and cross-references. Uses Python standard library only."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
VIDEO_RE = re.compile(r"YT-([1-9][0-9]*)$")
QUESTION_RE = re.compile(r"(IJ|IP|IS|IA|ID|IC|IT)-([1-9][0-9]*)$")
SECTION_RE = re.compile(
    r"^\| (YT-([1-9][0-9]*)\.([1-9][0-9]*)) \| \[([0-9:]+)\]"
    r"\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=([0-9]+)s\)"
    r" \| (🔴 NO NEED|🟡 INTRO|🟢 USEFUL) \| .+ \|$"
)
SUBJECTS = {"IJ": "JAVA", "IP": "PYTHON", "IS": "SPRING-BOOT", "IA": "ARCHITECTURE", "ID": "DATABASE", "IC": "DEVOPS", "IT": "TESTING"}


def fail(msg):
    errors.append(msg)


def load(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"{path}: {exc}")
        return {}


def exists(path):
    if not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts:
        fail(f"Invalid relative file path: {path!r}")
        return False
    if not (ROOT / path).is_file():
        fail(f"Missing file: {path}")
        return False
    return True


def time_seconds(text):
    try:
        components = [int(v) for v in text.split(":")]
        if len(components) == 2 and components[1] < 60:
            return components[0] * 60 + components[1]
        if len(components) == 3 and components[1] < 60 and components[2] < 60:
            return components[0] * 3600 + components[1] * 60 + components[2]
    except ValueError:
        pass
    return None


counters = load("REGISTRY/counters.json")
videos_doc = load("REGISTRY/videos.json")
questions_doc = load("REGISTRY/questions.json")
videos = videos_doc.get("videos", [])
questions = questions_doc.get("questions", [])
if not isinstance(videos, list):
    fail("REGISTRY/videos.json: videos must be a list")
    videos = []
if not isinstance(questions, list):
    fail("REGISTRY/questions.json: questions must be a list")
    questions = []

seen_videos = {}
seen_youtube = {}
known_sections = {}
max_video = 0

for video in videos:
    if not isinstance(video, dict):
        fail(f"Invalid video: {video!r}")
        continue
    vid, youtube_id = video.get("id"), video.get("youtube_id")
    match = VIDEO_RE.fullmatch(str(vid))
    if not match:
        fail(f"Invalid video ID: {vid}")
        continue
    number = int(match.group(1))
    max_video = max(max_video, number)
    if vid in seen_videos:
        fail(f"Duplicate video ID: {vid}")
    if video.get("type") not in ("interview", "tutorial"):
        fail(f"{vid}: type must be 'interview' or 'tutorial'")
    seen_videos[vid] = video
    if not isinstance(youtube_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{11}", youtube_id):
        fail(f"{vid}: invalid original YouTube video ID {youtube_id!r}")
    if youtube_id in seen_youtube:
        fail(f"Duplicate original YouTube ID: {youtube_id} ({vid}, {seen_youtube[youtube_id]})")
    seen_youtube[youtube_id] = vid

    expected_transcript = f"VIDEO-LIBRARY/{vid}/transcript.md"
    expected_timestamps = f"VIDEO-LIBRARY/{vid}/timestamps.md"
    if video.get("transcript") != expected_transcript:
        fail(f"{vid}: transcript path must be {expected_transcript}")
    if video.get("timestamps") != expected_timestamps:
        fail(f"{vid}: timestamps path must be {expected_timestamps}")
    exists(expected_transcript)
    if not exists(expected_timestamps):
        continue
    expected_timeline = f"VIDEO-LIBRARY/{vid}/timeline.md"
    if video.get("timeline") != expected_timeline:
        fail(f"{vid}: timeline path must be {expected_timeline}")
    if not exists(expected_timeline):
        continue
    contents = (ROOT / expected_timeline).read_text(encoding="utf-8")
    seen_sections = set()
    last_time = -1
    for line in contents.splitlines():
        if not line.startswith("| YT-"):
            continue
        section = SECTION_RE.match(line)
        if not section:
            fail(f"{vid}: malformed section heading: {line[:140]}")
            continue
        section_id, owner, _, display_time, linked_youtube, target_secs, _ = section.groups()
        seconds = time_seconds(display_time)
        if owner != str(number):
            fail(f"{vid}: section belongs to wrong video: {section_id}")
        if section_id in seen_sections:
            fail(f"{vid}: duplicate timestamp section ID: {section_id}")
        seen_sections.add(section_id)
        if linked_youtube != youtube_id:
            fail(f"{section_id}: timestamp URL points to different video")
        if seconds is None or seconds != int(target_secs):
            fail(f"{section_id}: displayed time differs from linked seconds")
        if seconds is not None and seconds < last_time:
            fail(f"{vid}: section headings must be chronological")
        if seconds is not None:
            last_time = seconds
    if not seen_sections:
        fail(f"{vid}: no validated timeline rows")
    if exists(expected_timestamps):
        grouped = (ROOT / expected_timestamps).read_text(encoding="utf-8")
        for sid in seen_sections:
            if f"| {sid} |" not in grouped:
                fail(f"{vid}: missing section {sid} from video question tables")
    known_sections[vid] = seen_sections

if type(counters.get("next_video")) is not int or counters["next_video"] <= max_video:
    fail("REGISTRY/counters.json: next_video must be greater than all registered video IDs")
next_question = counters.get("next_question", {})
if not isinstance(next_question, dict):
    fail("REGISTRY/counters.json: next_question must be an object")
    next_question = {}
seen_questions = set()
max_question = {}

for question in questions:
    if not isinstance(question, dict):
        fail(f"Invalid question: {question!r}")
        continue
    qid = question.get("id")
    match = QUESTION_RE.fullmatch(str(qid))
    if not match:
        fail(f"Invalid question ID: {qid}")
        continue
    prefix, numeric = match.group(1), int(match.group(2))
    max_question[prefix] = max(max_question.get(prefix, 0), numeric)
    if qid in seen_questions:
        fail(f"Duplicate question ID: {qid}")
    seen_questions.add(qid)
    subject = SUBJECTS[prefix]
    if question.get("subject") != subject:
        fail(f"{qid}: expected subject {subject}")
    expected_path = f"INTERVIEW-SYLLABUS/{subject}/{qid}.md"
    if question.get("path") != expected_path:
        fail(f"{qid}: expected path {expected_path}")
    if exists(expected_path):
        contents = (ROOT / expected_path).read_text(encoding="utf-8")
        if not contents.startswith(f"# {qid} —"):
            fail(f"{qid}: interview question Markdown heading must start with '# {qid} —'")
    if not isinstance(question.get("question"), str) or not question["question"].strip():
        fail(f"{qid}: question text missing")
    sources = question.get("sources", [])
    if not isinstance(sources, list) or not sources:
        fail(f"{qid}: must reference at least one video source")
        continue
    source_video_ids = set()
    for source in sources:
        if not isinstance(source, dict):
            fail(f"{qid}: invalid source {source!r}")
            continue
        vid = source.get("video_id")
        ids = source.get("timestamp_ids", [])
        if vid in source_video_ids:
            fail(f"{qid}: repeated video source {vid}; group timestamps once per video")
        source_video_ids.add(vid)
        if vid not in seen_videos:
            fail(f"{qid}: unknown video source {vid}")
        if not isinstance(ids, list) or not ids:
            fail(f"{qid}: source {vid} has no timestamps")
            continue
        if len(ids) != len(set(ids)):
            fail(f"{qid}: duplicate timestamp references in {vid}")
        for section_id in ids:
            if section_id not in known_sections.get(vid, set()):
                fail(f"{qid}: unknown timestamp {section_id} under {vid}")
            if f"| {section_id} |" not in contents:
                fail(f"{qid}: missing timestamp table row {section_id}")

for prefix in SUBJECTS:
    value = next_question.get(prefix)
    if type(value) is not int or value <= max_question.get(prefix, 0):
        fail(f"REGISTRY/counters.json: next_question.{prefix} must exceed all registered {prefix} IDs")

# Validate source-specific interview comparisons or tutorial AI-only answers.
comparisons_document = load("REGISTRY/answer-comparisons.json")
answer_comparisons = comparisons_document.get("comparisons", [])
if not isinstance(answer_comparisons, list):
    fail("answer-comparisons.json: comparisons must be a list")
    answer_comparisons = []

keys = set()
source_pairs = {
    (q.get("id"), s.get("video_id"))
    for q in questions if isinstance(q, dict)
    for s in q.get("sources", []) if isinstance(s, dict)
}
source_modes = {}
for comparison in answer_comparisons:
    if not isinstance(comparison, dict):
        fail("Answer record must be a JSON object")
        continue
    key = (comparison.get("question_id"), comparison.get("video_id"))
    if key in keys:
        fail(f"Duplicate answer record: {key}")
    keys.add(key)
    if key not in source_pairs:
        fail(f"Answer source not in question registry: {key}")
    video_id = comparison.get("video_id")
    video = seen_videos.get(video_id, {})
    video_type = video.get("type")
    explicit_mode = comparison.get("answer_type")
    if explicit_mode not in (None, "ai_only", "interview_comparison"):
        fail(f"Invalid answer_type {explicit_mode!r}: {key}")
        continue

    # Historical YT-1 interview records legitimately lack answer_type.
    mode = explicit_mode or "interview_comparison"
    source_modes[key] = mode
    if video_type == "tutorial" and mode != "ai_only":
        fail(f"Tutorial video must use AI-only answer mode: {key}")

    if mode == "ai_only":
        if explicit_mode != "ai_only":
            fail(f"AI-only answer must explicitly set answer_type: {key}")
        if video_type == "interview" and comparison.get("source_role") != "instructor_only":
            fail(f"AI-only segment in interview needs source_role=instructor_only: {key}")
        if "candidate_answer" in comparison or "ai_corrected_answer" in comparison:
            fail(f"AI-only answer must OMIT candidate and corrected-answer fields: {key}")
        value = comparison.get("ai_answer")
        if not isinstance(value, str) or len(value.strip()) < 30:
            fail(f"AI-only answer is missing or too brief: {key}")
    else:
        if video_type != "interview":
            fail(f"Only actual interviews can have candidate comparisons: {key}")
        if "ai_answer" in comparison:
            fail(f"Interview comparison must not include ai_answer: {key}")
        candidate = comparison.get("candidate_answer")
        correction = comparison.get("ai_corrected_answer")
        status = comparison.get("candidate_answer_status")
        if status not in (None, "verbatim_excerpt", "no_substantive_answer"):
            fail(f"Invalid candidate_answer_status: {key}")
        minimum = 3 if status == "no_substantive_answer" else 20
        if not isinstance(candidate, str) or len(candidate.strip()) < minimum:
            fail(f"Candidate transcript missing or too brief: {key}")
        if not isinstance(correction, str) or len(correction.strip()) < 30:
            fail(f"AI interview answer missing or too brief: {key}")
        if comparison.get("answer_style") not in (None, "simple_spoken"):
            fail(f"Unrecognized answer_style: {key}")
        caption_rows = comparison.get("candidate_transcript_rows")
        if status in ("verbatim_excerpt", "no_substantive_answer"):
            if not isinstance(caption_rows, list) or not caption_rows:
                fail(f"Verbatim candidate answer needs source caption rows: {key}")
            else:
                assembled = []
                transcript_path = video.get("transcript")
                transcript_text = ""
                if isinstance(transcript_path, str) and (ROOT / transcript_path).is_file():
                    transcript_text = (ROOT / transcript_path).read_text(encoding="utf-8")
                video_youtube_id = video.get("youtube_id", "")
                for caption in caption_rows:
                    if not isinstance(caption, dict):
                        fail(f"Invalid source caption row: {key}")
                        continue
                    second = caption.get("seconds")
                    clock = caption.get("clock")
                    spoken = caption.get("text")
                    if (type(second) is not int or not isinstance(clock, str)
                            or time_seconds(clock) != second):
                        fail(f"Source caption time mismatch: {key}")
                    if not isinstance(spoken, str) or not spoken.strip():
                        fail(f"Empty source caption text: {key}")
                        continue
                    assembled.append(spoken)
                    if isinstance(second, int) and isinstance(video_youtube_id, str):
                        caption_target = (
                            f"(https://www.youtube.com/watch?v={video_youtube_id}&t={second}s) "
                        )
                        lines = [
                            line.split(caption_target, 1)[1]
                            for line in transcript_text.splitlines()
                            if line.startswith("- [") and caption_target in line
                        ]
                        if not lines or not any(spoken in original for original in lines):
                            fail(f"Source caption not found verbatim at {second}s: {key}")
                if isinstance(candidate, str) and candidate != " ".join(assembled):
                    fail(f"Candidate answer is not an exact caption excerpt: {key}")

for key in source_pairs:
    if key not in keys:
        fail(f"Missing answer record for question/video source: {key}")

for q in questions:
    if not isinstance(q, dict) or not isinstance(q.get("path"), str):
        continue
    page = ROOT / q["path"]
    if not page.is_file():
        continue
    source_text = page.read_text(encoding="utf-8")
    for source in q.get("sources", []):
        if not isinstance(source, dict):
            continue
        vid = source.get("video_id")
        key = (q["id"], vid)
        mode = source_modes.get(key)
        video = seen_videos.get(vid, {})
        grouped_path = video.get("timestamps")
        grouped_text = ""
        if isinstance(grouped_path, str) and (ROOT / grouped_path).is_file():
            grouped_text = (ROOT / grouped_path).read_text(encoding="utf-8")
        if mode == "ai_only":
            heading = f"### AI answer — {vid}"
            if heading not in source_text:
                fail(f"Tutorial question page missing AI-only answer table: {key}")
            if heading not in grouped_text:
                fail(f"Tutorial video page missing AI-only answer table: {key}")
        elif mode == "interview_comparison":
            record = next((entry for entry in answer_comparisons if isinstance(entry, dict)
                           and (entry.get("question_id"), entry.get("video_id")) == key), {})
            if record.get("candidate_transcript_rows"):
                heading = f"### Original candidate transcript vs. simple AI answer — {vid}"
            else:
                heading = f"### Candidate answer vs. AI-corrected answer — {vid}"
            if heading not in source_text:
                fail(f"Interview question page missing comparison table: {key}")
            if heading not in grouped_text:
                fail(f"Interview video page missing comparison table: {key}")

if errors:
    print(f"FAILED: {len(errors)} validation error(s)")
    for problem in errors:
        print(f" - {problem}")
    sys.exit(1)
print(f"PASS: {len(seen_videos)} video(s), {len(seen_questions)} question(s), all IDs/references valid")
