# IC-2 — How do feature branches progress through QA, staging and production?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described development branches progressing through QA and preproduction before stable production, with different environment settings. | Treat environments as deployment targets, not necessarily one Git branch each. Build once and promote immutable artifacts through test, staging and production with approvals and environment-specific secrets/configuration. Use protected branches and clear release ownership to prevent drift. |

