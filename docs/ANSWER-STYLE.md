# Clear Spoken Answers & Verbatim Candidate Transcripts — REQUIRED

These rules override any older instructions suggesting candidate paraphrasing or dense textbook-style AI answers.

## Candidate response (interviews only)

- **Never paraphrase, rewrite, correct spelling/grammar, or polish candidate speech.** Copy the **original subtitle/transcript text verbatim** and link each excerpt to its actual starting caption timestamp. Preserve filler words and even incorrect technical claims.
- Source transcript captions sometimes combine speakers and have no diarization. Only call text a candidate response when reasonably supported by the exchange. If a turn boundary is uncertain, label it **unedited caption excerpt; speaker boundaries inferred** and link to the complete source. Never claim an excerpt is a complete quote if it is not.
- Store `candidate_answer` as exact selected raw caption text joined with spaces, `candidate_transcript_rows` as `[{seconds, clock, text}, ...]`, `candidate_answer_status` as `verbatim_excerpt` or `no_substantive_answer`. The validator verifies row text is present in the untouched transcript.
- When the candidate only acknowledges a question, display that acknowledgement exactly and state **No substantive candidate answer**, rather than inventing an explanation. Do not copy the interviewer's speech as the candidate's answer.
- Existing video subtitles and clickable timestamp tables remain unchanged.

## AI answer (both interviews and non-interview tutorials)

Write as a skilled developer **speaking naturally in a real interview**, not as a textbook, specification, or bullet dump. The inspiration is Steve Jobs-style **clarity and simplicity**, not impersonating anyone.

1. **Start with the answer** in a short everyday sentence.
2. Explain in simple words; introduce only the technical terms that matter.
3. Give **one memorable practical example** directly related to the question.
4. Finish with **one clear takeaway** that an interviewer would remember.
5. Keep it usually **65–100 spoken words**, approximately 30–60 seconds. Complex topics may need a little more.
6. Keep **technical correctness**. Simple must never mean vague or false. Add essential constraints, failure cases, and tradeoffs naturally, without jargon stacking.
7. Use natural first-person phrasing when appropriate ("I'd use...", "For example..."). Do not invent a candidate's personal work history or pretend the AI answer was actually spoken in the source.
8. Do not append tangential technical lists, and avoid generic openings ("Certainly", "In today's world").

For interviews: the right column holds the AI answer. For tutorials: there is **no candidate column**, just a **one-column AI answer table** in this same easy spoken style. If the source teacher said something wrong, the AI answer corrects it independently, without altering the source transcript.

## Recommended layout

```md
## IT-1 — How should a team interpret 95% test coverage?

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.111 | [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | 🟢 USEFUL | Test coverage discussion |

### Original candidate transcript vs. simple AI answer — YT-1

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) Okay so when we write the automations... | 95% coverage is good, but it doesn't mean 95% bug-free. For example, a payment service needs tests for both successful and failed payments. Good testing is about catching real problems, not chasing numbers. |
```

The example left excerpt is illustrative and shortened; live records must retain **exact** caption text. Each distinct YT-n video has its own response and AI answer, never mixed into another video.
