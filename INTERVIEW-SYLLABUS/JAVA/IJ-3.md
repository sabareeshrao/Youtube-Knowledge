# IJ-3 — How does HashMap fail-fast iteration compare with ConcurrentHashMap iteration?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:28:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5336s) exception called concurrent hash exception to avoid this kind of like uh scenario we can go with like a new family of the uh hashing is called concurrent hashmap so it will works in<br>[1:29:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5350s) efficient way so that even if you do add any entities to the hashmap while you are iterating so it will be uh efficient to handle that kind of scenarios so that will be very useful when we have a yeah<br>[1:29:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5362s) exception will be uh I don't think any exception will come because this is kind of like a main uh uh hashing we use especially for the multi- thread environments when there are more than | A HashMap iterator usually notices structural changes and may throw ConcurrentModificationException, but that fail-fast behavior is only a best-effort warning. It isn't thread safety. ConcurrentHashMap uses weakly consistent iteration: another thread can update the map while I'm looping, without that exception, but I may not see a perfect snapshot. For example, a live metrics dashboard can often tolerate that. If I need an exact snapshot, I must coordinate it explicitly. |

