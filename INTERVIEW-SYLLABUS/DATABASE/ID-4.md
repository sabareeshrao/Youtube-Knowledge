# ID-4 — How do consistency needs differ between cached social content and financial data?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.24 | [13:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=824s) | 🟢 USEFUL | Cache consistency requirements |
| YT-1.25 | [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) | 🟢 USEFUL | Financial data and eventual consistency |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=861s) if it's highly Financial then I would say dirty read can't be something which we can compromise because we can't we don't want to see<br>[14:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=872s) like the account balance something inaccurate on the two different accounts | Not every piece of data needs to be fresh to the exact same millisecond. A social feed can often show a post a few seconds late without hurting anyone. A bank balance before a withdrawal is a different story: we need the authoritative value and transaction checks. I may cache read-heavy feed data, but I take a much stricter approach to financial decisions. Consistency is a business promise, not just a database setting. |

