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

