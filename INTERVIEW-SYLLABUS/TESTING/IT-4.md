# IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.114 | [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | 🟢 USEFUL | Do not test trivial getters just for coverage |
| YT-1.115 | [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) | 🟢 USEFUL | Exclude DTO boilerplate from coverage |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He agreed that testing every DTO getter/setter is low value and said Maven XML exclusion patterns can omit boilerplate packages from coverage reporting. | Test behavior and meaningful serialization/validation contracts, not trivial accessors for percentages. Configure JaCoCo report exclusions or coverage rules explicitly, document why generated/DTO code is omitted, and do not use blanket exclusions to conceal untested logic. |

