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
    r"^### (YT-([1-9][0-9]*)\.([1-9][0-9]*)) — \[([0-9:]+)\]"
    r"\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=([0-9]+)s\)"
    r" — (🔴 NO NEED|🟡 INTRO|🟢 USEFUL): .+"
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
    contents = (ROOT / expected_timestamps).read_text(encoding="utf-8")
    seen_sections = set()
    last_time = -1
    for line in contents.splitlines():
        if not line.startswith("### YT-"):
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
        fail(f"{vid}: no validated timestamp headings")
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

for prefix in SUBJECTS:
    value = next_question.get(prefix)
    if type(value) is not int or value <= max_question.get(prefix, 0):
        fail(f"REGISTRY/counters.json: next_question.{prefix} must exceed all registered {prefix} IDs")

if errors:
    print(f"FAILED: {len(errors)} validation error(s)")
    for problem in errors:
        print(f" - {problem}")
    sys.exit(1)
print(f"PASS: {len(seen_videos)} video(s), {len(seen_questions)} question(s), all IDs/references valid")
