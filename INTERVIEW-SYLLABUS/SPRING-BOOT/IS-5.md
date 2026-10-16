# IS-5 — How do access-token expiry and refresh tokens work?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.6 | [4:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=247s) | 🟢 USEFUL | Token expiration and refresh tokens |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He mentioned a short token lifetime and reauthentication after expiry; the interviewer introduced refresh tokens, which he acknowledged without explaining the refresh exchange. | Access tokens expire according to the exp claim. Before or after expiry, an authorized client can exchange a valid refresh token at the authorization server for a new access token; it does not re-send the user’s password on every API call. Protect refresh tokens, use rotation/revocation where supported, and handle expired or stolen tokens safely. |

