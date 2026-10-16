# IC-7 — How would you troubleshoot a repeatedly crashing Kubernetes pod in production?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.105 | [1:11:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4261s) | 🟢 USEFUL | Repeated Kubernetes pod crashes and CrashLoopBackOff scenario |
| YT-1.106 | [1:12:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4327s) | 🟢 USEFUL | Crash triage, logs and PagerDuty |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:11:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4288s) so generally the developer will get pager Duty Call sometimes if if the periodic fail happens so we can still smart these alerts to think like<br>[1:11:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4303s) something which can control or something which we can't for example if something is a my scale is going down which is something which we can't control so that we can't do anything until the database<br>[1:11:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4313s) team has to fix but if server is going crash and our kubernetes is can't able to get it up the worst case is we have to manually bring this up uh but uh I I never encoun the case where uh we used | If a Kubernetes pod keeps crashing, I first find out why instead of restarting it repeatedly. I check the pod events, the previous container logs, and whether it ran out of memory, has bad configuration, or can't reach a dependency. For example, a missing environment variable can make every new pod fail immediately. If a new release caused it, I roll back and investigate. Restore the service first; fix the root cause next. |

