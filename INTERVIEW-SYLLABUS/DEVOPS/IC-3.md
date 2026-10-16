# IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said GitHub Actions or Jenkins notices a new commit/merge, runs tests and automatically deploys, suggesting it periodically checks changed commit IDs. | A PR merge normally triggers a push/webhook or CI workflow event; it need not rely on periodic commit polling. The pipeline checks out an immutable commit, builds, runs tests/scans, publishes a versioned artifact and deploys under approval/health gates. Distinguish CI triggers, artifact promotion and production-release policy. |

