# ID-4 — How do consistency needs differ between cached social content and financial data?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said stale reads may be acceptable for social feeds but account balances must not show inaccurate values across users. | Define required consistency for each operation. Feeds and recommendation caches may tolerate bounded staleness, while available balances and payment authorization should read from an authoritative consistent source or use transactional safeguards. Invalidate related caches on writes and document read-after-write requirements and acceptable delay. |

