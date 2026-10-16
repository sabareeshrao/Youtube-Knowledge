# ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.81 | [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | 🟢 USEFUL | Slow SQL query diagnosis |
| YT-1.82 | [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) | 🟢 USEFUL | Indexing and query profiling |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3250s) uh the first thing is like I need to figure it out what is why it is<br>[54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) taking time so couple of Reason could be possible one is uh if the query is taking time because uh it lack with the indexing then it's better we can add a index because indexing is nothing but a<br>[54:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3274s) compound of data structure we use to get the items in a fast way so so that's the first thing I will check I mean it's called analyzing the query uh or profiling the query so get to know | When a SQL query is slow, I measure before changing anything. I find the exact query, inspect its execution plan, and check whether it scans too many rows or misses a useful index. For example, searching a million orders by customer ID may be slow without the right index. I then test the change and watch its effect on reads and writes. Partitioning can help some workloads, but I'd never start by splitting the database just because one query is slow. |

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.64 | [1:03:43](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3823s) | 🟢 USEFUL | How would you diagnose a slow database query in production? |
| YT-4.65 | [1:04:51](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3891s) | 🟢 USEFUL | Follow-up: How would you diagnose a slow database query in production? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:03:55](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3835s) scenario I'll check the logs to understand which particular method is taking long time okay based on the logs I'll be understanding which particular query is taking long time perfect I'll<br>[1:04:07](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3847s) go to that particular table I'll understand how much data is available right now okay if indexing is required I need to index the table and even if even if even this is taking time I need to | I measure where the time goes, inspect an execution plan, and check indexes, joins, filtering, and table statistics. For example, searching a million orders without a useful index can force an expensive scan. I compare before-and-after latency instead of guessing. Scaling hardware is not my first step. |

