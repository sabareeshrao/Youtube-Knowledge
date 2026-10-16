# IA-2 — How would you control stale cached data using TTL and consistency requirements?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.22 | [12:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=776s) | 🟢 USEFUL | Cache TTL and freshness |
| YT-1.23 | [13:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=801s) | 🟢 USEFUL | Stale cached data and TTL tradeoffs |
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described TTL-based caching, recognized possible stale results, and said eventual consistency can be acceptable for some apps but not financial balances. He did not give a concrete invalidation design. | Choose freshness guarantees by business use case. On writes, invalidate or update affected cache keys; complement this with TTL, versioning/events and retryable invalidation. TTL alone bounds staleness imperfectly and short TTLs increase load. Describe race conditions, read-after-write needs and strong-consistency paths for critical values. |

