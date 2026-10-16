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

