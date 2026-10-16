# IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) uh yes so session level uh is called L1 caching and session Factory is the L2 so by default we enable the session level caching which is like limited to particular session so<br>[16:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=970s) but if you want some data which should be like could be cached across the all the sessions then we put it in the L2 level caching which is under the session Factory | Hibernate has two useful cache levels. The first-level cache belongs to one Session and is always there. If I read the same entity twice in that session, Hibernate can avoid a second database fetch. The optional second-level cache can share eligible entity data across sessions using a configured provider. For example, product categories that rarely change might benefit from it. The memory trick is: L1 belongs to one conversation with the database; L2 can serve many conversations. |

