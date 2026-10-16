# IS-6 — How can you avoid duplicate Spring scheduled jobs running across multiple application instances?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.17 | [10:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=630s) | 🟢 USEFUL | Duplicate scheduled jobs across replicas |
| YT-1.18 | [11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) | 🟢 USEFUL | ShedLock for single scheduler execution |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [10:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=653s) uh yeah I mean generally we go with the spring scheduler but the drawback as you mentioned uh if there are multiple<br>[11:04](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=664s) instances the spring Schuler can't able to handle this instance it end up with running on all the three instance so we want something like a single turn Behavior here like for that we can go<br>[11:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=674s) with something called shedlock so how it orchestrate is like rather than uh it will let it to run only once and like and ra for the all the instances so that's how internal architectures are | If I run the same Spring scheduler on three servers, all three may execute the job. That's a problem if the job must send only one email or create only one record. I would use a shared lock, such as ShedLock backed by the database, so only one instance runs at a time. I would also make the job safe to retry after a crash. A scheduler knows when to run; a shared lock helps decide who runs. |

