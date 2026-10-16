# IT-4 — Should DTO getters be tested just to increase coverage, and how are exclusions configured?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.114 | [1:17:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4679s) | 🟢 USEFUL | Do not test trivial getters just for coverage |
| YT-1.115 | [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) | 🟢 USEFUL | Exclude DTO boilerplate from coverage |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:18:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4724s) we can write like a rejects patterns which can uh exclude these kind of<br>[1:18:59](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4739s) packages which we don't want to track in our coveres so uh we uh I mean have written in XML with mavin like we can specify like what kind of packages you can use like dot star for the dtos like<br>[1:19:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4754s) generally we follow the vering sorry package patterns for all the files like some dto should go under dto package and entity should go so these Getters and Setters pojo files uh we don't have to | I don't write tests for trivial getters just to make the coverage number look impressive. I spend that time on validation, calculations, and failure handling—places where bugs hurt customers. For example, a DTO getter usually needs no special test, but a custom JSON mapping or validation rule might. If generated boilerplate should be excluded, I configure and explain that in the coverage tool. The goal is honest coverage that reflects valuable tests. |

