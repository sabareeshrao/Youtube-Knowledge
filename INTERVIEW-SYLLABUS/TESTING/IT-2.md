# IT-2 — How do JUnit tests and mocks isolate logic from databases and other services?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.112 | [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) | 🟢 USEFUL | JUnit tests and mocked dependencies |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4593s) the mocking is something I use a lot because there are few things<br>[1:16:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4605s) when you're checking about the functionality you don't have to make a DB call every time in that case we can mock those calls and test the you can Mark what data you want to back and<br>[1:16:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4615s) write your functionality for the test cases so that will increase my test cases I also use some code coverage tool and also sonar Cube U to do the static analysis of my code base to see what | I use JUnit to check what my service does and Mockito when I don't want to call a real database or API. For example, I can mock the repository to return one customer, call my service, and verify the result. Then I test what happens when the customer isn't found. Those are fast unit tests. Separate integration tests make sure the real database connection works. Mocking helps isolate the logic; integration tests make sure the pieces actually fit. |

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.52 | [51:47](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3107s) | 🟢 USEFUL | How does Mockito isolate a service class from database calls? |
| YT-4.53 | [53:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3184s) | 🟢 USEFUL | Follow-up: How does Mockito isolate a service class from database calls? |
| YT-4.54 | [54:12](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3252s) | 🟢 USEFUL | Follow-up: How does Mockito isolate a service class from database calls? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [52:10](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3130s) uh all the classes which are required we'll be mocking them using at Mock Bean for example uh I'm using any service class I I should mock them and the data which I'm getting from the<br>[52:25](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3145s) repository layer I'll not be uh able to get directly from the database right I should not hit the database directly I I should not save anything directly to the database when I'm uh calling the test | Mockito can replace a repository with a mock while I test real service logic. For example, I make a mocked repository return a customer and verify the service calculates the right discount. This keeps the unit test fast and independent of a real database. Separate integration tests still verify actual persistence behavior. |


## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.28 | [26:10](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1570s) | 🟢 USEFUL | How do unit tests, integration tests, and Mockito relate? |
| YT-8.29 | [27:22](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1642s) | 🟢 USEFUL | Follow-up: How do unit tests, integration tests, and Mockito relate? |
| YT-8.30 | [28:41](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1721s) | 🟢 USEFUL | Follow-up: How do unit tests, integration tests, and Mockito relate? |
| YT-8.56 | [53:52](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3232s) | 🟢 USEFUL | Why mock database or network calls in unit tests? |
| YT-8.57 | [55:04](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=3304s) | 🟢 USEFUL | Follow-up: Why mock database or network calls in unit tests? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [26:27](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1587s) manually means once the code is getting deployed and all other components are getting communicate so one one kind of sity before hand overing it to the testers soting yes any knowledge about the<br>[26:46](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1606s) bdds or test yeah that uh uh I I don't much work on that but yes I have that uh understanding about the um test driven development dddd so writing the scenarios into that uh that file by when | Unit tests isolate one component and mock its dependencies, while integration tests exercise real boundaries such as repositories and external services. Mockito lets me control collaborators without hitting a real database. For example, I test discount rules using a mocked repository, then verify SQL mappings separately in an integration test. |

