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

