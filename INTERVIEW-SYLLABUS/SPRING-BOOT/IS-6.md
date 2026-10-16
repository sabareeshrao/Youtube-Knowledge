# IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.17 | [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | 🟢 USEFUL | Duplicate scheduled jobs across replicas |
| YT-1.18 | [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) | 🟢 USEFUL | ShedLock for single scheduler execution |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He correctly noted that @Scheduled runs independently in each application replica and proposed ShedLock to prevent three instances from writing the same record. | A local Spring scheduler does not coordinate replicas. Use a shared distributed lock such as ShedLock with a properly configured persistent lock provider, or a dedicated scheduler/queue with leader election. Set lock durations carefully and still make the job idempotent, because retries and crashes can otherwise cause duplicates. |

