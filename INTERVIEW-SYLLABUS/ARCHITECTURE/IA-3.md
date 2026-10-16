# IA-3 — When would you choose GraphQL over REST for an API?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.33 | [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) | 🟢 USEFUL | Why GraphQL instead of REST |
| YT-1.34 | [19:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1145s) | 🟢 USEFUL | GraphQL query entry point |
| YT-1.35 | [19:29](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1169s) | 🟢 USEFUL | GraphQL versus REST decision criteria |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [18:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1108s) uh generally U it's not a limitation of the rest API it's just<br>[18:43](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1123s) like when we go with the rest API there are so many end points come to picture like it's very hard for the any client applications or any like third party to remember this so like for example if I<br>[18:53](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1133s) have like a a student as the uh main entity and if you have like all the crude operation then like it end up with like so many end points for suent TBL and similarly for like account again | I choose GraphQL when different clients need different pieces of the same data. For example, a mobile screen might need only a product's name and price, while the website needs reviews and images too. GraphQL lets each client ask for the fields it needs. REST still works very well for straightforward resource APIs. So I don't choose GraphQL because it's trendy. I choose it when flexible queries genuinely make the client simpler, while controlling query cost and permissions. |

