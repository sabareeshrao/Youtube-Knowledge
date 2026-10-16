# IS-5 — How do access-token expiry and refresh tokens work?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.6 | [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | 🟢 USEFUL | Token expiration and refresh tokens |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| **No substantive response; only this brief acknowledgement is captured.**<br>[4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) yes yeah exactly | An access token is a short-lived pass to call an API. When it expires, the user shouldn't necessarily have to sign in again. The app can use a properly protected refresh token to request a new access token from the authorization server. For example, while someone browses an online store, their session can continue without interrupting every few minutes. Refresh tokens need strong protection and sometimes rotation or revocation. Short-lived access plus carefully managed refresh is the balance. |

