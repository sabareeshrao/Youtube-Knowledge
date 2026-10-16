# IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.105 | [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | 🟢 USEFUL | Repeated Kubernetes pod crashes and CrashLoopBackOff scenario |
| YT-1.106 | [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) | 🟢 USEFUL | Crash triage, logs and PagerDuty |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He mentioned PagerDuty alerts and manual intervention when a pod repeatedly restarts; he said he had not implemented an additional automation solution. | For CrashLoopBackOff inspect kubectl describe pod, events, logs --previous, exit codes/OOMKilled, configuration, secrets, dependencies and probes. Compare rollout changes, mitigate via rollback or corrected config, and monitor recovery. PagerDuty routes an incident; it is not the technical fix. |

