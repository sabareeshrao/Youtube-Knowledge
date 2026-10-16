# IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He associated Hibernate L1 with an individual Session and L2 with SessionFactory, saying L1 is enabled by default and L2 can share entities across sessions. | Hibernate’s first-level cache (persistence context) is mandatory and scoped to a Session/EntityManager. The optional second-level cache is managed at SessionFactory scope through a configured cache provider and caching policies. L2 is not a magical cache of every entity; explain regions, invalidation, transaction consistency and when it is appropriate. |

