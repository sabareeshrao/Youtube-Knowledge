# IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.31 | [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | 🟢 USEFUL | Why SessionFactory is expensive and shared |
| YT-1.32 | [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) | 🟢 USEFUL | Multiple databases and SessionFactory instances |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) U first thing is like it's a costly<br>[17:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1020s) operation I would say but I mean in the normal words U this as same as like creating the instance of the database so we generally want it to be like U highly uh synchronized uh applications so that<br>[17:12](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1032s) no two uh interactions can corrupt the datas so when we make it as single turn so that uh every time every new sessions we use the same uh sorry every uh New Creations will create the only one | I reuse SessionFactory because building it takes work: it holds Hibernate's mapping and database configuration. It isn't a single database connection. Think of it as a factory that creates many short-lived Sessions, usually using pooled connections underneath. If my application connects to three separately configured databases, I generally set up an appropriate factory or persistence unit for each. Reuse the factory; open and close sessions for the actual work. |

