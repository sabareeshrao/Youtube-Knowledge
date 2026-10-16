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

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.16 | [14:21](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=861s) | 🟢 USEFUL | How can Saga handle a distributed order transaction? |
| YT-4.17 | [15:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=938s) | 🟢 USEFUL | Follow-up: How can Saga handle a distributed order transaction? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=885s) assigned and Order reaches to you what if the payment fails in between you have to roll back all you have to cancel the order right we need to roll back yeah so the this transaction you can see is not<br>[14:59](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=899s) in one particular application it is across the whole micros services so what what kind of distributed transactions you can handle how how can you handle this particular distributed transactions | A Saga coordinates a sequence of local transactions, with compensating actions when a step fails. For example, if payment fails after reserving inventory, a compensation can release the reservation. This is not the same as a single atomic database rollback. The advantage is managing cross-service work without one global transaction. |


## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.18 | [16:37](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=997s) | 🟢 USEFUL | How do you handle a payment failure across several microservices? |
| YT-8.19 | [17:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1066s) | 🟢 USEFUL | Follow-up: How do you handle a payment failure across several microservices? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [16:49](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1009s) the products added to the card placed an order did the payment the delivery partner is assigned I'm waiting for my order what happens if uh my payment is failed then I have to<br>[17:02](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1022s) roll back it up completely so how will you manage this yeah uh we can manage this by using distributed uh transaction uh by making use of The Saga design pattern okay and what is Saga design | A distributed workflow can use a Saga with compensating actions. For example, an order reserves stock, payment fails, and a compensation releases stock and marks the order failed. Unlike one database rollback, these actions happen in separate local transactions. I include idempotency and retries because partial failures are expected. |

