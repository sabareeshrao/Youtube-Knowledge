#!/usr/bin/env python3
"""Independent structural/source-integrity audit for the six interview ingestions.
Does not claim to detect every missing topic or prove speaker diarization.
"""
import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'REGISTRY/ingestion-audits/six-interviews-20261016.json'
violations=[]
def check(expr,msg):
 if not expr:violations.append(msg)
def seconds(clock):
 v=list(map(int,clock.split(':')))
 return v[0]*60+v[1] if len(v)==2 else v[0]*3600+v[1]*60+v[2]
try:
 data=json.loads(AUDIT.read_text(encoding='utf8'))
 regv={x['id']:x for x in json.loads((ROOT/'REGISTRY/videos.json').read_text(encoding='utf8'))['videos']}
 regq=json.loads((ROOT/'REGISTRY/questions.json').read_text(encoding='utf8'))['questions']
 answers=json.loads((ROOT/'REGISTRY/answer-comparisons.json').read_text(encoding='utf8'))['comparisons']
except (OSError,ValueError,KeyError) as e:
 print('FAILED: unable to read six-video audit/registries:',e);sys.exit(1)
seen_original=set();all_paired=set()
for a in data['videos']:
 vid=a['id'];v=regv.get(vid)
 check(v is not None,vid+' missing registry');
 if not v:continue
 check(v['youtube_id']==a['youtube_id'],vid+' youtube ID changed')
 check(v['type']=='interview',vid+' not an interview')
 original=(ROOT/v['transcript']).read_text(encoding='utf8')
 check(hashlib.sha256(original.encode()).hexdigest()==a['source_sha256'],vid+' original transcript modified')
 cap=[]
 for ln in original.splitlines():
  if not ln.startswith('- ['):continue
  m=re.fullmatch(r'- \[([^]]+)\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=(\d+)s\) (.*)',ln)
  if not m:
   violations.append(vid+' invalid original caption line');continue
  clock,yid,ss,spoken=m.groups();sec=int(ss)
  check(yid==v['youtube_id'],vid+' wrong source video in transcript')
  check(seconds(clock)==sec,vid+' mismatched source caption time')
  cap.append((sec,spoken))
 check(len(cap)==a['captions'],vid+' lost transcript subtitle entries')
 check(len(set(t for t,_ in cap))==len(cap),vid+' repeated original timestamp')
 check(sum(a['caption_bucket_counts'])==len(cap),vid+' transcript section coverage mismatch')
 check((cap[0][0],cap[-1][0])==(a['first_caption'],a['last_caption']),vid+' beginning or ending subtitle lost')
 check(v['youtube_id'] not in seen_original,vid+' duplicate native video ID')
 seen_original.add(v['youtube_id'])
 page=(ROOT/v['timeline']).read_text(encoding='utf8')
 grouped=(ROOT/v['timestamps']).read_text(encoding='utf8')
 sections=[];times=[]
 for ln in page.splitlines():
  if not ln.startswith('| YT-'):continue
  m=re.fullmatch(r'\| (YT-\d+\.\d+) \| \[([^]]+)\]\(https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{11})&t=(\d+)s\) \| (🔴 NO NEED|🟡 INTRO|🟢 USEFUL) \| (.*) \|',ln)
  if not m:
   violations.append(vid+' malformed timestamp '+ln[:80]);continue
  sid,clock,yid,ss,tag,title=m.groups();sec=int(ss)
  check(sid.startswith(vid+'.'),vid+' foreign section ID '+sid)
  check(yid==v['youtube_id'],vid+' wrong YouTube timestamp link '+sid)
  check(seconds(clock)==sec,vid+' wrong displayed timestamp '+sid)
  check(sec in {x[0] for x in cap},vid+' timestamp not grounded in original captions '+sid)
  sections.append(sid);times.append(sec)
 check(len(sections)==a['curated_sections'],vid+' curated section count changed')
 check(len(set(sections))==len(sections),vid+' duplicate section IDs')
 check(times==sorted(times),vid+' chronological timeline out of order')
 check(max([b-a for a,b in zip(times,times[1:])],default=0)==a['max_navigation_gap_s'],vid+' navigation gap changed')
 check(all(f'| {s} |' in grouped or any(s in it.get('timestamp_ids',[]) for q in regq for it in q.get('sources',[]) if it['video_id']==vid)==False for s in sections),vid+' missing section in grouped page')
 qfor=[q for q in regq if any(src['video_id']==vid for src in q.get('sources',[]))]
 check(len(qfor)==a['distinct_questions'],vid+' question coverage count changed')
 check(sum(1 for q in qfor if q['id'] in data['repeated_question_ids'])==a['reused_question_count'],vid+' repeated question count changed')
 for q in qfor:
  qid=q['id'];source=next(s for s in q['sources'] if s['video_id']==vid)
  all_paired.add((qid,vid))
  check(all(sid in sections for sid in source['timestamp_ids']),f'{qid} {vid} references missing section')
  check(all(f'| {sid} |' in grouped for sid in source['timestamp_ids']),f'{qid} {vid} lacks video table row')
  question_md=(ROOT/q['path']).read_text(encoding='utf8')
  check(f'## Video option — {vid}:' in question_md,f'{qid} no separate {vid} section')
  check(all(f'| {sid} |' in question_md for sid in source['timestamp_ids']),f'{qid} {vid} lacks syllabus row')
  if qid in data['repeated_question_ids']:
   check('⭐' in grouped[grouped.find(f'## {qid} —'):grouped.find(f'## {qid} —')+400],f'{qid} {vid} repeated question has no ⭐')
 check(len(set(zip(sections,times)))==len(sections),vid+' duplicate ID/time pair')
record={(r['question_id'],r['video_id']):r for r in answers}
for qid,vid in all_paired:
 rec=record.get((qid,vid));check(rec is not None,f'{qid} {vid}: missing comparison');
 if not rec:continue
 check(rec.get('answer_type')=='interview_comparison',f'{qid} {vid}: wrong answer type')
 check(rec.get('candidate_answer_status') in ('verbatim_excerpt','no_substantive_answer'),f'{qid} {vid}: candidate status missing')
 source=(ROOT/regv[vid]['transcript']).read_text(encoding='utf8')
 rowtexts=[]
 for row in rec.get('candidate_transcript_rows',[]):
  sec=row['seconds'];clock=row['clock'];utterance=row['text']
  check(seconds(clock)==sec,f'{qid} {vid}: quote clock mismatch')
  check(f'(https://www.youtube.com/watch?v={regv[vid]["youtube_id"]}&t={sec}s) {utterance}' in source,f'{qid} {vid}: candidate quote altered')
  rowtexts.append(utterance)
 check(' '.join(rowtexts)==rec.get('candidate_answer'),f'{qid} {vid}: candidate transcript not verbatim')
 check(len(rec.get('ai_corrected_answer',''))>100,f'{qid} {vid}: AI answer too short')
 check(f'### Original candidate transcript vs. simple AI answer — {vid}' in (ROOT/regv[vid]['timestamps']).read_text(encoding='utf8'),f'{qid} {vid}: comparison table absent')
check(len(all_paired)==data['total_distinct_question_video_pairs'],'six-interview question/video pairs changed')
check(sum(a['curated_sections'] for a in data['videos'])==data['total_curated_sections'],'overall timeline coverage changed')
check(sum(a['captions'] for a in data['videos'])==data['total_caption_lines'],'overall transcript caption count changed')
if violations:
 print('FAILED: six-interview audit has',len(violations),'issue(s)')
 for x in violations[:60]:print('-',x)
 sys.exit(1)
print(f"PASS: six interviews, {data['total_caption_lines']} original captions, {data['total_curated_sections']} timestamps, {len(all_paired)} question/video comparisons, repeat stars and cross-references checked")
