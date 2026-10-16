# IS-1 — How would you secure a Spring Boot REST API from frontend to backend?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.4 | [2:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) | 🟢 USEFUL | Spring Security end-to-end question |
| YT-1.5 | [3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) | 🟢 USEFUL | Stateless REST and JWT |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [2:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=175s) so generally we enforce the security mainly on the back end itself<br>[3:06](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=186s) because uh the client browsers uh it is secured like we can have like multiple browsers running but main thing which we have to ensure is our servers are running fine so we generally go with<br>[3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) some of the security features like JWT uh because generally we go with the HTTP rest apis these are like stateless applications which means like when every time when you make a request you don't | I secure a Spring Boot API by making the backend check every request, not by trusting the browser. When a user signs in, the identity provider gives them an access token. The frontend sends it with API requests, and Spring Security checks that it's genuine, hasn't expired, and permits the action. For example, a normal customer should never access an admin endpoint. The simple rule is: the frontend offers the experience, but the backend makes the security decision. |

