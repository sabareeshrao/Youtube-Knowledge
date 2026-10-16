# IC-8 — How would you roll back a broken deployment to a previous container image?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.107 | [1:12:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4354s) | 🟢 USEFUL | Rollback to previous application version |
| YT-1.108 | [1:12:48](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4368s) | 🟢 USEFUL | Release versioning and rollback workflow |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:12:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4379s) we also give something called versioning so it's like a name space followed by name and the version so it means like the kubernetes have the<br>[1:13:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4391s) versioning of our of the image so it means if last version is not working fine so it automatically goes to the previous one and create a new instance out of it so sorry new container out of<br>[1:13:22](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4402s) that image | I always keep a known-good application image so I can return to it after a bad release. If version 12 starts failing in production, I can roll back the Deployment to version 11 and check that requests recover. Kubernetes keeps rollout history when configured, but it doesn't automatically undo every failed release. I verify readiness, error rates, and customer impact after rollback. A rollback isn't finished when the command runs—it's finished when users are healthy again. |

