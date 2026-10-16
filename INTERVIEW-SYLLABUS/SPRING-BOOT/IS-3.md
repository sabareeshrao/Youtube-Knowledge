# IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.11 | [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | 🟢 USEFUL | How a backend validates JWTs |
| YT-1.12 | [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) | 🟢 USEFUL | JWT signature and payload discussion — JWT payload is encoded, not automatically encrypted |
| YT-1.13 | [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) | 🟢 USEFUL | Questionable JWT validation explanation — WARNING: candidate's token-validation claim is incorrect; validate signature and claims |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [7:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=434s) the token what uh it's getting generated it's B is based on<br>[7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) some hashing algorithms it means it it's a one way like u based on that hash code if I just use JWT uh which can if you hash back it like we can get like three part out of it so we I think one of the<br>[7:41](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=461s) part is signature which is just to authenticate whether this hash is corrupted or some someone like uh changed it or not hacked it or not uh but in our case if let's assume like if | A JWT is like a signed entry pass. Before trusting it, my Spring Boot API checks the signature, the issuer, who the token is meant for, and whether it has expired. Then I check the user's permission for the request. For example, changing the word 'admin' inside the token should break its signature. I use Spring Security's JWT support instead of writing my own verification. The key point: reading a token is easy; proving it's genuine is what matters. |

## Video option — YT-3: Mock Interview | Core Java Mock Interview Question and Answers | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=d22oNW1W6ms)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.16 | [14:29](https://www.youtube.com/watch?v=d22oNW1W6ms&t=869s) | 🟢 USEFUL | How does a Spring resource server validate a JWT? |
| YT-3.17 | [15:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=941s) | 🟢 USEFUL | Follow-up: How does a Spring resource server validate a JWT? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [14:41](https://www.youtube.com/watch?v=d22oNW1W6ms&t=881s) particular communication between the front end and your back end what secures your uh communication how is your communication secured with JWT token what that JWT token has that<br>[14:53](https://www.youtube.com/watch?v=d22oNW1W6ms&t=893s) your communication from front end to back end is secured okay when it comes to JWT token it contains a header payload and the signature part but signature part is optional but when it comes to payload | A resource server validates a JWT signature using a trusted key, then checks expiry, issuer, audience, and permissions as appropriate. For example, a forged admin role should fail signature verification. Base64 decoding alone does not validate a token or protect the connection; HTTPS is also required. |

