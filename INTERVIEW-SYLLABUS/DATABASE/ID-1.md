# ID-1 — How would you troubleshoot and optimize a slow SQL query over a large table?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.81 | [53:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3234s) | 🟢 USEFUL | Slow SQL query diagnosis |
| YT-1.82 | [54:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3262s) | 🟢 USEFUL | Indexing and query profiling |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He suggested first profiling the slow query and checking indexes, then partitioning large datasets if the table itself is a bottleneck. | Capture the slow SQL and use EXPLAIN/EXPLAIN ANALYZE plus query and database metrics. Check missing/poor indexes, selectivity, join plans, row counts, locking, statistics, overfetching and N+1 access. Benchmark changes and account for index write costs before trying partitioning, caching or sharding. |

