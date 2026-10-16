# IS-3 — How should a Spring Boot backend validate an incoming JWT and detect tampering?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.11 | [7:02](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=422s) | 🟢 USEFUL | How a backend validates JWTs |
| YT-1.12 | [7:28](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=448s) | 🟢 USEFUL | JWT signature and payload discussion — JWT payload is encoded, not automatically encrypted |
| YT-1.13 | [8:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=500s) | 🟢 USEFUL | Questionable JWT validation explanation — WARNING: candidate's token-validation claim is incorrect; validate signature and claims |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said a JWT has three parts and a signature that reveals tampering, but suggested decoding or hashing it back and comparing a password or user ID against the database to trust the caller. | JWT verification is not reverse hashing. A resource server validates a trusted signature (or MAC), expected algorithm, issuer, audience, expiration/not-before and relevant authorization claims. Spring Security OAuth2 Resource Server can validate JWTs using an issuer/JWK set. Never place passwords inside JWT payloads or trust a token just because its decoded fields match a database record. |

