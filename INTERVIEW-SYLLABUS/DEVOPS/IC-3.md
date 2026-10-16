# IC-3 — What happens after a pull request is merged and what tools trigger the pipeline?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:06:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4005s) GitHub action or it could be junkins so generally it will uh check periodic changes are available so that's the reason we use like continuous inte Integrations and deployment continuous<br>[1:06:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4015s) deployment so this to ensure that uh every changes has to get deployed as soon as the new changes come into picture so it automatically see if there is any change in the commit IDs if it<br>[1:07:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4027s) figure it out then it automatically start to run the continuous to run the test cases then it will automatically deploy the changes | When a pull request is merged, GitHub Actions or Jenkins can start a pipeline from that push event. The pipeline checks out the commit, builds the code, runs tests, and publishes a versioned artifact. Depending on our release rules, it then deploys to staging or waits for production approval. For example, a failed security check should block deployment. A merge starts the process; passing the checks earns the release. |

