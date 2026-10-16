# IT-7 — What do JUnit 5 @BeforeEach and @BeforeAll do?

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode |

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.55 | [54:26](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3266s) | 🟢 USEFUL | What do JUnit 5 @BeforeEach and @BeforeAll do? |
| YT-4.56 | [55:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3341s) | 🟢 USEFUL | Follow-up: What do JUnit 5 @BeforeEach and @BeforeAll do? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:41](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3281s) all at before each before calling any test class uh test method this particular method will be called setup method which is annotated with at before which will be called and at before all<br>[54:54](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3294s) will be called at the start of executing all the methods all the test class methods okay so you mean to say before each is Method level before each method it is called | @BeforeEach runs before every test method and can create fresh objects. @BeforeAll normally runs once before all tests in a test class and is useful for shared expensive setup. For example, each test can get a clean shopping cart. Cleanup is handled by @AfterEach and @AfterAll. Isolation matters more than saving a few setup lines. |

