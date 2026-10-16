# IS-4 — What information must not be stored in JWT claims, and why?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.14 | [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | 🟢 USEFUL | Sensitive data inside JWT claims |
| YT-1.15 | [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) | 🟢 USEFUL | Password and JWT payload safety |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [9:13](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=553s) uh no I think it's Works based on like a hashing is only like a one way of uh it's called like one way like<br>[9:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=567s) mapping it means like from the the keywords we can get to know like what's the hash code but other way can't be possible so you can't get to know the actual password sorry I said password<br>[9:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=577s) but you can't get to know the password so generally anyone can't get to know only the user know his own passwords so when we save it in the database so it's always be the hashing so we never save | I treat a JWT payload like a postcard: someone holding the token can usually read what's written on it. That's why I never put passwords, secrets, or unnecessary personal information inside. For example, including a customer's password in a token would expose it to anyone who gets a copy. A signature prevents undetected changes; it doesn't hide the text. My rule is simple: keep claims minimal, protect tokens, and never mistake encoding for encryption. |

