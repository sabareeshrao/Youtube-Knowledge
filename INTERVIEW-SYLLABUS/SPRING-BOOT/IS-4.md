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

## Video option — YT-3: Mock Interview | Core Java Mock Interview Question and Answers | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=d22oNW1W6ms)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.18 | [16:46](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1006s) | 🟢 USEFUL | Which JWT claims are safe to expose to clients? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [17:00](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1020s) you you said there is something called as body uh in the JG token that is the second part in the three parts of it so what does body contains in JWT token body contains<br>[17:16](https://www.youtube.com/watch?v=d22oNW1W6ms&t=1036s) the the data which is like a request body which contains information related to the particular user like response body not the response body yes that's right that it contains data about the | A typical signed JWT payload is encoded, not encrypted, so clients can read its claims. For example, a token may carry a subject and roles, but it should not include a password or secret. The signature helps detect tampering; confidential data belongs in protected storage. |


## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.71 | [1:10:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4245s) | 🟢 USEFUL | How are JWT claims different from encrypted confidential data? |
| YT-4.72 | [1:11:50](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4310s) | 🟢 USEFUL | Follow-up: How are JWT claims different from encrypted confidential data? |
| YT-4.73 | [1:13:00](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4380s) | 🟢 USEFUL | Follow-up: How are JWT claims different from encrypted confidential data? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:10:58](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4258s) implementation in your project uh I have used uh JWT JWT is nothing but Json web token so once the token is being uh created uh based on the response I mean we'll be having also expiry time so once<br>[1:11:16](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4276s) the expiry time is expired like uh of that particular token again a new token will be generated okay and so inside the Json the J toen consist of three particular parameters one is the header | A normal signed JWT exposes readable claims after Base64URL decoding. For example, a subject identifier and role may be acceptable, but a password must never be placed in the token. The signature gives integrity, not confidentiality. When an API needs private data it should retrieve it through authorization-checked backend services. |

