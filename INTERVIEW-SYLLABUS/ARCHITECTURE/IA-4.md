# IA-4 — How does GraphQL field selection compare with REST DTO responses?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.36 | [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | 🟢 USEFUL | GraphQL field-level selection |
| YT-1.37 | [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) | 🟢 USEFUL | REST DTO and field filtering alternatives |
| YT-1.38 | [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) | 🟢 USEFUL | Variable response fields across clients |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) returned with the graph we can also limit in the rest API as well based on like what kind of dto we are returning because like uh yeah I I didn't go in depth about this but uh in rest AP also<br>[21:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1269s) we can limit what response we are responding back we also come up with something called Json ignore and yeah some crucial Fields if you don't want to ex we don't want to export we can at the<br>[21:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1279s) rate and out with Json ignore ignore so yeah but I feel like it's still like too much of laborious task to do this using rest API which can be easily automated with the graph | GraphQL lets the caller choose fields in a query. For example, a customer screen can request just an employee's ID and name instead of the whole employee record. REST can return smaller responses too, using DTOs or field-selection options. The difference is that GraphQL makes client-driven selection a central feature. I would use whichever approach keeps the API predictable, secure, and easy to maintain. Less unnecessary data is good; extra complexity isn't always worth it. |

