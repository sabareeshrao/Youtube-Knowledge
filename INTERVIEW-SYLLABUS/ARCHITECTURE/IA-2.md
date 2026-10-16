# IA-2 — How would you control stale cached data using TTL and consistency requirements?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.22 | [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | 🟢 USEFUL | Cache TTL and freshness |
| YT-1.23 | [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) | 🟢 USEFUL | Stale cached data and TTL tradeoffs |
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) uh so generally for the server it can't get to know whether the data is dirty or not because only the database has a clear idea whether this data was corrupted so there could<br>[13:58](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=838s) be be a chances of reading this diry data but this kind of data we keep this kind of data especially for the applications like where some datas need not to be accurate like for example if<br>[14:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=849s) you use Twitter so we don't want like what I see on my table sorry page is need not to be like as accurate as yours so when we can compromise on the consistency we can go with like this | A cache is useful only if we know how fresh its data needs to be. For example, an old product description may be acceptable for a minute, but an incorrect bank balance is not. I use a time-to-live to expire cached entries and invalidate or update them when important data changes. I also plan for timing races between a database write and a cache read. The question isn't 'How long can we cache?'; it's 'How wrong can this data safely be?' |

