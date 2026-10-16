#!/usr/bin/env python3
"""Regression tests: old interview comparisons and tutorial AI-only answers."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

VALIDATOR = Path(__file__).with_name("validate.py")
SAMPLE_VIDEO = "aBcDeFgH123"  # 11-character placeholder used only in test fixtures


def make_fixture(root, video_type, record):
    def write(path, content):
        file = root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

    vid = "YT-2"
    qid = "IJ-1"
    row = f"| YT-2.1 | [0:05](https://www.youtube.com/watch?v={SAMPLE_VIDEO}&t=5s) | 🟢 USEFUL | Sample topic |"
    timeline = (
        "# YT-2 — Sample video\n\n"
        "## What is the example topic?\n\n"
        "| ID | Watch | Type | What you will learn |\n"
        "|---|---|---|---|\n"
        f"{row}\n"
    )
    if record.get("answer_type") == "ai_only":
        answer_heading = "### AI answer — YT-2"
        answer_table = "| AI answer |\n|---|\n| Example answer |\n"
    else:
        answer_heading = (
            "### Original candidate transcript vs. simple AI answer — YT-2"
            if record.get("candidate_transcript_rows") else
            "### Candidate answer vs. AI-corrected answer — YT-2"
        )
        answer_table = "| Candidate answer | AI corrected answer |\n|---|---|\n| A | B |\n"
    grouped = (
        "# YT-2 — Sample topic\n\n"
        "## IJ-1 — What is the example topic?\n\n"
        "| ID | Watch | Type | What you will learn |\n"
        "|---|---|---|---|\n"
        f"{row}\n\n"
        f"{answer_heading}\n\n{answer_table}"
    )
    qpage = "# IJ-1 — What is the example topic?\n\n" + grouped.replace(
        "## IJ-1 — What is the example topic?\n\n", "", 1
    )
    source_text = f"Video: https://www.youtube.com/watch?v={SAMPLE_VIDEO}\\n"
    if record.get("candidate_transcript_rows"):
        source_text += (
            f"- [0:05](https://www.youtube.com/watch?v={SAMPLE_VIDEO}&t=5s) "
            "This is the candidate speaking about the example topic exactly as transcribed.\\n"
        )
    write("VIDEO-LIBRARY/YT-2/transcript.md", source_text)
    write("VIDEO-LIBRARY/YT-2/timestamps.md", grouped)
    write("VIDEO-LIBRARY/YT-2/timeline.md", timeline)
    write("INTERVIEW-SYLLABUS/JAVA/IJ-1.md", qpage)
    write("REGISTRY/videos.json", json.dumps({"videos": [{
        "id": vid, "youtube_id": SAMPLE_VIDEO, "title": "Sample",
        "type": video_type,
        "transcript": "VIDEO-LIBRARY/YT-2/transcript.md",
        "timestamps": "VIDEO-LIBRARY/YT-2/timestamps.md",
        "timeline": "VIDEO-LIBRARY/YT-2/timeline.md"
    }]}))
    write("REGISTRY/questions.json", json.dumps({"questions": [{
        "id": qid, "subject": "JAVA", "question": "What is the example topic?",
        "path": "INTERVIEW-SYLLABUS/JAVA/IJ-1.md",
        "sources": [{"video_id": vid, "timestamp_ids": ["YT-2.1"]}]
    }]}))
    write("REGISTRY/counters.json", json.dumps({
        "next_video": 3,
        "next_question": {"IJ": 2, "IP": 1, "IS": 1, "IA": 1, "ID": 1, "IC": 1, "IT": 1}
    }))
    write("REGISTRY/answer-comparisons.json", json.dumps({"comparisons": [record]}))
    write("scripts/validate.py", VALIDATOR.read_text(encoding="utf-8"))


class TestAnswerModeValidator(unittest.TestCase):
    def check(self, video_type, record, should_pass, expected_error=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root, video_type, record)
            result = subprocess.run(
                [sys.executable, str(root / "scripts/validate.py")],
                cwd=root, capture_output=True, text=True, check=False
            )
            if should_pass:
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            else:
                self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                if expected_error:
                    self.assertIn(expected_error, result.stdout)

    def test_tutorial_ai_only_without_candidate(self):
        self.check("tutorial", {
            "question_id": "IJ-1", "video_id": "YT-2", "answer_type": "ai_only",
            "ai_answer": "A well-grounded interview explanation of the example topic, with useful detail."
        }, True)

    def test_legacy_interview_two_column(self):
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2",
            "candidate_answer": "The candidate explained the basic topic and gave a supporting example.",
            "ai_corrected_answer": "A technically corrected explanation of the topic with conditions and caveats."
        }, True)

    def test_tutorial_cannot_claim_candidate(self):
        self.check("tutorial", {
            "question_id": "IJ-1", "video_id": "YT-2", "answer_type": "ai_only",
            "candidate_answer": "This field must not exist because the instructor is not a candidate.",
            "ai_answer": "A well-grounded interview explanation of the example topic, with useful detail."
        }, False, "must OMIT candidate")

    def test_tutorial_cannot_use_interview_mode(self):
        self.check("tutorial", {
            "question_id": "IJ-1", "video_id": "YT-2",
            "candidate_answer": "A candidate never answered, so this answer would be fabricated.",
            "ai_corrected_answer": "A technically corrected explanation of the topic with conditions and caveats."
        }, False, "Tutorial video must use AI-only")

    def test_tutorial_must_have_actual_ai_answer(self):
        self.check("tutorial", {
            "question_id": "IJ-1", "video_id": "YT-2", "answer_type": "ai_only",
            "ai_answer": "Tiny"
        }, False, "too brief")

    def test_interview_ai_only_requires_instructor_only_marker(self):
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2", "answer_type": "ai_only",
            "ai_answer": "A well-grounded interview explanation of the example topic, with useful detail."
        }, False, "source_role=instructor_only")

    def test_interview_instructor_segment_may_be_ai_only(self):
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2", "answer_type": "ai_only",
            "source_role": "instructor_only",
            "ai_answer": "A well-grounded interview explanation of the example topic, with useful detail."
        }, True)

    def test_verbatim_candidate_captions_are_accepted(self):
        recorded = "This is the candidate speaking about the example topic exactly as transcribed."
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2",
            "answer_type": "interview_comparison",
            "candidate_answer_status": "verbatim_excerpt",
            "candidate_answer": recorded,
            "candidate_transcript_rows": [{"seconds": 5, "clock": "0:05", "text": recorded}],
            "ai_corrected_answer": "I would explain the example directly, add a practical scenario, and finish with a clear takeaway.",
            "answer_style": "simple_spoken",
        }, True)

    def test_changed_candidate_quote_fails_source_check(self):
        fake = "These are words never actually spoken in the candidate's original subtitle."
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2",
            "candidate_answer_status": "verbatim_excerpt",
            "candidate_answer": fake,
            "candidate_transcript_rows": [{"seconds": 5, "clock": "0:05", "text": fake}],
            "ai_corrected_answer": "A technically accurate, simple interview explanation with an example and key takeaway.",
        }, False, "not found verbatim")

    def test_short_acknowledgement_is_not_fabricated(self):
        words = "This"
        self.check("interview", {
            "question_id": "IJ-1", "video_id": "YT-2",
            "candidate_answer_status": "no_substantive_answer",
            "candidate_answer": words,
            "candidate_transcript_rows": [{"seconds": 5, "clock": "0:05", "text": words}],
            "ai_corrected_answer": "A direct, simple interview explanation that gives the missing technical details accurately.",
        }, True)


if __name__ == "__main__":
    unittest.main()
