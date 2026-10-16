# IA-1 — Explain cache-aside caching using Redis and a database.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.19 | [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | 🟡 INTRO | Caching discussion begins |
| YT-1.20 | [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) | 🟢 USEFUL | Redis cache-aside lookup |
| YT-1.21 | [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) | 🟢 USEFUL | In-memory caching and latency |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) uh the caching generally uh I<br>[11:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=701s) mean uh either we can use the third party which is already available so which is like uh redis is one of the popular caching uh it's nowadays which we use uh to enhance the performance<br>[11:51](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=711s) there are few datas which we find like frequently are getting used so rather than hitting the database which takes some additional time as a latency so we can use this caching which is like | Redis helps me avoid asking the database the same question again and again. Suppose a popular product page gets 10,000 requests. I first look for its details in Redis. If they're there, I return them quickly. If not, I read the database, put a copy in Redis, and return it. That's called cache-aside. The trick is remembering that Redis is a fast copy, while the database remains the source of truth. |

