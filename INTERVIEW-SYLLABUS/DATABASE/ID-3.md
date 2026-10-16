# ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) I will go with the Cassandra here okay so so<br>[35:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2143s) basically you're going with no SQL for s Service yeah no SQL so it can be uh yeah it's need not be like no SQL but I find it here more relevant as a Cassandra I uh | I wouldn't choose SQL or NoSQL just because a service is called 'search' or 'cart.' I'd ask what it reads and what must never go wrong. For example, product descriptions might live in SQL or a document store, while search uses a separate index. Cart and inventory updates often need reliable transactions. Order tracking may be a simple relational history table. Use the simplest database that meets the actual data and consistency needs. |

## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.17 | [15:15](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=915s) | 🟢 USEFUL | How do database-per-service and shared databases compare? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [15:38](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=938s) micros Services yeah um I will use um based on the requirement uh we can use the database we can have multiple database also um so like for search related thing<br>[15:53](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=953s) we can use the mongodb kind of thing and for other think we can use the um rdbms also we can use I mean when will you use noq when will you use my SQ um for uh search related means | A database-per-service design gives each service ownership of its data schema and migrations. For example, payments and catalog can evolve independently. A shared database can simplify transactions initially but creates tight coupling. I choose SQL or NoSQL based on each service's access patterns and consistency requirements, not the microservice label alone. |

