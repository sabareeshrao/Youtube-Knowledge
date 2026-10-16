# IC-8 — How would you roll back a broken deployment to a previous container image?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.107 | [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | 🟢 USEFUL | Rollback to previous application version |
| YT-1.108 | [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) | 🟢 USEFUL | Release versioning and rollback workflow |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said Docker images have versions and Kubernetes can go back to a previous version when the newest one fails, but the actual rollback mechanics were vague. | Tag/digest images immutably, use rollout history and a controlled rollback such as kubectl rollout undo deployment/name or redeploy a known-good image. Kubernetes does not automatically roll back every failed Deployment by default. Verify readiness, error rates and dependencies after rollback. |

