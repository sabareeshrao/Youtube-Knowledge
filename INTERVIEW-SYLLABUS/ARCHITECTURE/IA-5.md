# IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.43 | [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | 🟢 USEFUL | Distributed transactions in microservices |
| YT-1.44 | [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) | 🟢 USEFUL | Saga versus two-phase commit |
| YT-1.45 | [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) | 🟢 USEFUL | Saga events and compensating actions |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He contrasted Saga’s event-triggered local transactions and compensating operations with synchronous two-phase commit, but at times spoke as if Saga could provide one atomic end-to-end transaction. | Saga coordinates independently committed local transactions through orchestration or choreography and compensating actions after failure; it does not provide global ACID atomicity or instant rollback. Two-phase commit coordinates participants for atomic commit but adds blocking, availability and operational costs. Choose based on consistency requirements, failure recovery and service autonomy. |

