# IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.112 | [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | 🟢 USEFUL | JUnit tests and mocked dependencies |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said JUnit 5 tests cover individual methods and mocks stand in for database calls or other external dependencies. | Use JUnit 5 plus Mockito to inject mocked repositories/clients, arrange behavior, call the service and assert outputs and important interactions. Test edge/error cases without real external services in unit tests. Use separate integration tests with realistic dependencies for persistence and wire behavior. |

