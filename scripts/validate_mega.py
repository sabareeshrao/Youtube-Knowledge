#!/usr/bin/env python3
"""Verify full-course source integrity, chapter coverage and every YT-2 reference.

Reads committed files rather than relying on the course generator.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VID = 'YT-2'
YT = 'xTtL8E4LzTQ'
BASE = ROOT / 'VIDEO-LIBRARY' / VID
errors = []
def check(ok, msg):
    if not ok: errors.append(msg)

def read(path): return path.read_text(encoding='utf-8')
def data(path): return json.loads(read(path))
def sec_clock(clock):
    digits = [int(s) for s in clock.split(':')]
    if len(digits) not in (2, 3) or any(k >= 60 for k in digits[1:]): return -1
    if len(digits) == 2: return digits[0] * 60 + digits[1]
    return digits[0] * 3600 + digits[1] * 60 + digits[2]

manifest = data(BASE/'ingestion-manifest.json')
coverage = data(BASE/'chapter-coverage.json')
transcript_bytes = (BASE/'transcript.md').read_bytes()
raw = transcript_bytes.decode('utf-8')
sub_re = re.compile(r'^- \[([0-9:]+)\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=(\d+)s\) (.*)$',re.M)
subs = [(m[1],m[2],int(m[3]),m[4]) for m in sub_re.finditer(raw)]
check(hashlib.sha256(transcript_bytes).hexdigest() == manifest['transcript_sha256'], 'Source file changed: SHA-256 mismatch')
check(len(subs) == manifest['captions'] == coverage['original_subtitle_count'] == 2693, 'Missing source subtitles')
check(all(v == YT and sec_clock(clock) == sec for clock,v,sec,_ in subs), 'Original caption URL, ID or displayed time mismatch')
check(all(x[2] < y[2] for x,y in zip(subs,subs[1:])), 'Original transcript is not strictly chronological')
check(len({s[2] for s in subs}) == len(subs), 'Duplicate subtitle start seconds')
check(subs[-1][2] == 43195, 'Final alarm-clock subtitle missing')

chapters = coverage['chapters']
check(len(chapters) == 71 and len(chapters) == manifest['chapters'], 'Missing official chapter')
check([c['chapter'] for c in chapters] == list(range(1,72)), 'Chapter numbering skipped or rearranged')
check([c['name'] for c in chapters] == [c['name'] for c in manifest['chapter_audit']], 'Chapter naming differs between audit files')
check(sum(c['source_subtitles'] for c in chapters) == len(subs), 'Not all subtitles assigned to chapters')
for i,chapter in enumerate(chapters):
    lo = chapter['official_start_seconds']
    hi = chapters[i+1]['official_start_seconds'] if i+1 < len(chapters) else 43196
    slice_subs = [x for x in subs if lo <= x[2] < hi]
    check(len(slice_subs) == chapter['source_subtitles'], f'Chapter {i+1}: source subtitle count changed')
    check(bool(slice_subs) and slice_subs[0][2] == chapter['first_caption'] and slice_subs[-1][2] == chapter['last_caption'], f'Chapter {i+1}: missing start/end evidence')
    check(len(chapter['question_ids']) == 2 and len(chapter['section_ids']) >= 6, f'Chapter {i+1}: question or navigation coverage missing')
    check(0 <= chapter['subtitle_start_drift_seconds'] <= 15, f'Chapter {i+1}: source timing drift changed')

row_re = re.compile(r'^\| (YT-2\.\d+) \| \[([0-9:]+)\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=(\d+)s\) \| (?:🔴 NO NEED|🟡 INTRO|🟢 USEFUL) \| (.*?) \|$',re.M)
rows = [(m[1],m[2],m[3],int(m[4]),m[5]) for m in row_re.finditer(read(BASE/'timeline.md'))]
ids = [r[0] for r in rows]
check(len(rows) == manifest['curated_timestamps'] == coverage['curated_section_count'] == 588,'Wrong curated time-link total')
check(len(set(ids)) == len(rows),'Duplicate YT-2 section IDs')
check(ids == [f'YT-2.{i}' for i in range(1,len(rows)+1)],'Section ID numbering contains gaps')
check(all(r[2] == YT and sec_clock(r[1]) == r[3] for r in rows),'Timestamp URLs or displayed times differ')
check(all(a[3] < b[3] for a,b in zip(rows,rows[1:])),'Curated timestamps out of order')
check(all(r[3] in {s[2] for s in subs} for r in rows),'Curated timestamp absent from original source')
gaps = [b[3]-a[3] for a,b in zip(rows,rows[1:])]
check(max(gaps) <= 150,'Navigation gap greater than 150 seconds')
check(max(gaps) == manifest['max_gap_seconds'],'Maximum navigation gap metadata outdated')
check([sid for c in chapters for sid in c['section_ids']] == ids,'Not all curated timestamps assigned to the correct chapters')
grouped = read(BASE/'timestamps.md')
check(grouped.count('### AI answer — YT-2') == 142,'Video page does not have 142 independent AI answers')
check(len(re.findall(r'^## IJ-\d+ — ',grouped,re.M)) == 142,'Missing question headings in video page')
check(all(f'| {sid} |' in grouped for sid in ids),'Timeline row missing from video page')
questions = data(ROOT/'REGISTRY/questions.json')['questions']
answers = data(ROOT/'REGISTRY/answer-comparisons.json')['comparisons']
video_qs = [q for q in questions if any(s.get('video_id') == VID for s in q.get('sources',[]))]
video_ans = [a for a in answers if a.get('video_id') == VID]
check(len(video_qs) == len(video_ans) == manifest['new_questions'] == 142,'Missing question or answer registry records')
check({q['id'] for q in video_qs} == {a['question_id'] for a in video_ans},'Missing answers for some source questions')
check(all(a.get('answer_type') == 'ai_only' and 'candidate_answer' not in a and bool(a.get('ai_answer')) for a in video_ans),'Tutorial incorrectly has a candidate answer')
for q in video_qs:
    doc = read(ROOT/q['path'])
    check(doc.startswith(f"# {q['id']} — ") and '### AI answer — YT-2' in doc, f"{q['id']}: missing AI answer heading")
    for src in q['sources']:
        if src['video_id'] == VID:
            check(all(f'| {sid} |' in doc for sid in src['timestamp_ids']), f"{q['id']}: missing timestamp link")
check({q['id'] for q in video_qs} == {qid for c in chapters for qid in c['question_ids']},'Some chapters or questions are not connected')

if errors:
    for e in errors: print('ERROR:',e)
    sys.exit(1)
print(f"PASS: {len(subs)} original subtitles; {len(chapters)} chapters; {len(rows)} curated starts; {len(video_qs)} questions and AI-only answers; maximum navigation gap {max(gaps)}s.")