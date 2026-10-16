# IC-1 — What Git branching and release promotion workflow have you used?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) we generally use the git for the versioning control and uh generally we have like a Dev branches and the QA and uh yeah generally we have like a master branch which is we also<br>[1:04:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3860s) called like a stable branch and for every monthly releases we create a new Branch from that it depends on how many what's the scale of our team so if there are many team members in the team so in<br>[1:04:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3872s) that case we also consider called a feature branch which uh so once the changes are done on the feature so we will do a kind of like a testing so this will get deployed on the testing | I like short-lived feature branches, pull requests, and one clear path to production. A developer finishes a change, automated tests run, teammates review it, and we build a versioned artifact. That same artifact moves through testing and staging before release. For example, if a release breaks checkout, we know exactly which version to roll back. Git branches organize work; tested builds and release gates make deployment dependable. |

## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.22 | [20:14](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1214s) | 🟢 USEFUL | How do pull requests and release branches support teamwork? |
| YT-8.23 | [21:19](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1279s) | 🟢 USEFUL | Follow-up: How do pull requests and release branches support teamwork? |
| YT-8.24 | [22:33](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1353s) | 🟢 USEFUL | Follow-up: How do pull requests and release branches support teamwork? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [20:38](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1238s) raising the pool request PR we call it as okay so yeah so in that case whenever he is raising the pr firstly he is getting the pool and suppose some developer is also working on the same<br>[20:52](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1252s) file then he will get the conflict so he will resolve those conflict or he will take other Stranges and then he will pull and once we raise the pull request we ask for the code review the architect | Developers work in focused branches, open pull requests, get reviews, and merge after required checks pass. For example, a small inventory change can move through development and QA before production. I keep a clear release history and avoid bypassing branch protections just to ship faster. |

