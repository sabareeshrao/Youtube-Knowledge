# IS-4 — What information must not be stored in JWT claims, and why?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.14 | [9:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=543s) | 🟢 USEFUL | Sensitive data inside JWT claims |
| YT-1.15 | [9:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=589s) | 🟢 USEFUL | Password and JWT payload safety |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He initially argued that JWT hashing prevented outsiders from recovering sensitive information, but later agreed that passwords and personal details should not be placed in the token body. | A common signed JWT is base64url-encoded, not encrypted: anyone holding it can read header and payload. Never put passwords, credential hashes, access secrets or unnecessary personal data in its claims. Signatures protect integrity, not confidentiality; use TLS, minimal claims, and encryption only when separately required. |

