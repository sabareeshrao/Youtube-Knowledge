# IA-5 — Compare Saga and two-phase commit for distributed microservice transactions.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.43 | [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) | 🟢 USEFUL | Distributed transactions in microservices |
| YT-1.44 | [25:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1507s) | 🟢 USEFUL | Saga versus two-phase commit |
| YT-1.45 | [25:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1531s) | 🟢 USEFUL | Saga events and compensating actions |
| YT-1.72 | [47:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2844s) | 🟢 USEFUL | Saga is not one global ACID transaction |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [24:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1467s) uh so when it comes to distributed transactions uh it's easy to handle that in the monolith architecture<br>[24:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1484s) because we can have one transaction and write all the operations we want to perform but in case of distributed we uh bate the functionalities to different micros service the main problem is if<br>[24:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1496s) something goes wrong then we have to roll back but since it is under in different transactions we have a I think two-way of approach so whether we can go with synchronized or asynchronized I | A Saga helps several microservices complete one business process without pretending they share a single database transaction. Picture placing an order: reserve stock, take payment, and create the order. If payment fails, we release the stock through a compensating action. Two-phase commit tries to coordinate an atomic commit across participants, but can be harder to operate and less available. A Saga doesn't magically roll back the whole world; it plans how to recover from each step. |

