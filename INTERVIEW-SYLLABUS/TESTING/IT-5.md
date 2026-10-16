# IT-5 — How do unit, integration and end-to-end tests differ for communicating microservices?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.116 | [1:19:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4794s) | 🟢 USEFUL | Integration tests for entities and services |
| YT-1.117 | [1:20:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4805s) | 🟢 USEFUL | Microservice end-to-end testing |
| YT-1.118 | [1:21:15](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4875s) | 🟢 USEFUL | Avoid real cross-service calls in unit tests |
| YT-1.119 | [1:21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4890s) | 🟢 USEFUL | Use separate integration/system-test suites |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:20:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4816s) I have written the test cases but generally it's more like a integration test case only where<br>[1:20:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4827s) we make the call to the uh rest template uh with by passing the payload so so one way we have to ensure like these uh services are running and also like the for this particular request the<br>[1:20:40](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4840s) corresponding response is coming back or not so we don't have to test cases itself you have involved this particular part yes uh because like even when we make a call to different micros service | I keep three levels of testing separate. Unit tests check one service's logic quickly, using mocks for outside calls. Integration tests check real pieces working together, like a repository with a test database. A smaller end-to-end suite checks the full journey—for example, cart to order to payment—in a test environment. If every unit test calls ten live services, builds become slow and unreliable. Test small things quickly and complete journeys deliberately. |

