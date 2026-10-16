# IS-1 — How would you secure a Spring Boot REST API from frontend to backend?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.4 | [2:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=164s) | 🟢 USEFUL | Spring Security end-to-end question |
| YT-1.5 | [3:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=198s) | 🟢 USEFUL | Stateless REST and JWT |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said security should mainly be enforced on the backend, and stateless REST APIs can reuse a JWT sent by the frontend in cookies or a session. He described it as a hash of authentication. | Enforce authentication and authorization at the backend, not merely in the browser. With Spring Security, configure request authorization, validate the access token’s signature, issuer, audience and expiry, and enforce roles/scopes. Use HTTPS, secure token storage and appropriate CSRF/CORS protections. A JWT is not simply an authentication hash. |

