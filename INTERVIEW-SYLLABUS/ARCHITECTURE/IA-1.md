# IA-1 — Explain cache-aside caching using Redis and a database.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.19 | [11:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=687s) | 🟡 INTRO | Caching discussion begins |
| YT-1.20 | [12:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=721s) | 🟢 USEFUL | Redis cache-aside lookup |
| YT-1.21 | [12:25](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=745s) | 🟢 USEFUL | In-memory caching and latency |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described Redis as an in-memory key-value cache checked before querying the database, reducing latency for frequently read data. | That is cache-aside: read cache, on miss read authoritative storage, write the result to cache with appropriate TTL, and return it. Redis is a separate shared in-memory service, not necessarily local RAM inside each app instance. Plan invalidation, miss storms, serialization and failure fallback. |

