# IT-1 — How should a team interpret a claim of 90 to 95 percent unit-test coverage?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.111 | [1:15:50](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4550s) | 🟢 USEFUL | High test coverage question |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:16:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4579s) Okay so when we write the automations I generally concentrate on the unit test cases like every method should have its own test cases and I write with a junit f which supports<br>[1:16:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4593s) something called nested classes like uh so we can I can segregate the functionalities in the test cases and uh the mocking is something I use a lot because there are few things<br>[1:16:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4605s) when you're checking about the functionality you don't have to make a DB call every time in that case we can mock those calls and test the you can Mark what data you want to back and | 95% test coverage is a good number, but it doesn't mean our application is 95% bug-free. Coverage only tells us how much code our tests exercised. Imagine a payment service: testing successful payments isn't enough. We should also test failed payments and what happens when the bank doesn't respond. So I look at which important behaviors we test, not just the percentage. For me, good testing is about catching real problems, not chasing numbers. |

