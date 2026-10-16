# IT-8 — How can JUnit 5 assert that code throws an expected exception?

## Video option — YT-7: Java Full-Stack Web Developer Mock Interview 4+ year experience | Angular Spring Boot | Code Decode

**Video:** [Play this source video](https://www.youtube.com/watch?v=X2bPVTRruUM)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-7.35 | [30:56](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1856s) | 🟢 USEFUL | How can JUnit 5 assert that code throws an expected exception? |
| YT-7.36 | [32:12](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1932s) | 🟢 USEFUL | Follow-up: How can JUnit 5 assert that code throws an expected exception? |

### Original candidate transcript vs. simple AI answer — YT-7

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-7/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:08](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1868s) executes if there is no exception in that so unit will consider that test as past if there is an exception in that so it will fail the test okay now suppose I am expecting an<br>[31:20](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1880s) exception now suppose there's a method who validates the age and throws an exception if age is greater than 50 this is the business use case I have to write a J unit for this so I know that I'm | I use assertThrows with the expected exception class and executable code. For example, withdrawing more than the balance should throw InsufficientFundsException. The test passes only when that expected exception occurs. I can inspect the returned exception to check its message or other details. |

