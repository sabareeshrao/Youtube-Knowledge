# IS-7 — Explain Hibernate first-level and second-level caching, including defaults and scope.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.27 | [15:00](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=900s) | 🟢 USEFUL | JPA/Hibernate entity caching |
| YT-1.28 | [15:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=945s) | 🟢 USEFUL | Compare Hibernate L1 and L2 caching |
| YT-1.29 | [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) | 🟢 USEFUL | Default L1 and opt-in L2 cache |
| YT-1.30 | [16:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=994s) | 🟢 USEFUL | Second-level cache beyond Session lifetime |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=955s) uh yes so session level uh is called L1 caching and session Factory is the L2 so by default we enable the session level caching which is like limited to particular session so<br>[16:10](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=970s) but if you want some data which should be like could be cached across the all the sessions then we put it in the L2 level caching which is under the session Factory | Hibernate has two useful cache levels. The first-level cache belongs to one Session and is always there. If I read the same entity twice in that session, Hibernate can avoid a second database fetch. The optional second-level cache can share eligible entity data across sessions using a configured provider. For example, product categories that rarely change might benefit from it. The memory trick is: L1 belongs to one conversation with the database; L2 can serve many conversations. |

## Video option — YT-3: Mock Interview | Core Java Mock Interview Question and Answers | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=d22oNW1W6ms)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.27 | [26:28](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1588s) | 🟢 USEFUL | How does Hibernate caching differ from Spring method caching? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:43](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1603s) then with the help of entity is the cash and other things is going to use internally this right or manager so uh yes uh you can use at theate cashable and atate cash and all<br>[27:02](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1622s) these things these if if you're using it on your entity and entity managers in session then it is the internal one that is provided by hnet for you and there are two levels of caching uh for the | Hibernate's first-level cache is scoped to a persistence context; second-level caching is optional and shared across sessions within a session factory. Spring method caching instead caches method results through a configured cache manager. For example, reloading one managed entity is different from caching the output of a service method. |


## Video option — YT-7: Java Full-Stack Web Developer Mock Interview 4+ year experience | Angular Spring Boot | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=X2bPVTRruUM)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-7.18 | [15:30](https://www.youtube.com/watch?v=X2bPVTRruUM&t=930s) | 🟢 USEFUL | What are Hibernate first-level and second-level caches? |

### Original candidate transcript vs. simple AI answer — YT-7

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-7/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:44](https://www.youtube.com/watch?v=X2bPVTRruUM&t=944s) layer is disabled by default so for that uh to enable second layer caching we need to do extra configuration for that but I have not used that second level much no worries so uh how is it linked<br>[15:57](https://www.youtube.com/watch?v=X2bPVTRruUM&t=957s) uh so there are two things s session Factory so who which is linked with which sorry what so first level cash is linked with session or session Factory session fact uh session it is it | The first-level Hibernate cache is associated with the persistence context and is enabled by default. An optional second-level cache can reuse entity state across sessions within a SessionFactory. For example, reading the same managed entity twice may avoid a second query. It's separate from method-level Spring caching. |

