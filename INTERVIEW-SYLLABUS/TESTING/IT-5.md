# IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.116 | [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | 🟢 USEFUL | Integration tests for entities and services |
| YT-1.117 | [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) | 🟢 USEFUL | Microservice end-to-end testing |
| YT-1.118 | [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) | 🟢 USEFUL | Avoid real cross-service calls in unit tests |
| YT-1.119 | [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) | 🟢 USEFUL | Use separate integration/system-test suites |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described calling actual REST endpoints across microservices in tests and checking responses, then agreed those calls should be separated from fast unit tests. | Unit tests mock remote clients and run quickly. Integration tests check adapters and real dependencies (often via Testcontainers or stubbed services); contract tests validate provider/consumer interfaces. A small end-to-end suite exercises deployed service flows. Separate suites by CI stage to avoid flaky, slow unit builds. |

