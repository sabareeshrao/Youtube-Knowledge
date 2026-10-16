# IS-2 — How does a Spring Security application integrate with Okta and OAuth 2.0?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.7 | [4:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=259s) | 🟢 USEFUL | Okta OAuth authorization server |
| YT-1.8 | [4:57](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=297s) | 🟢 USEFUL | Authentication redirect and authorization flow |
| YT-1.9 | [5:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=321s) | 🟢 USEFUL | Callback URLs and identity-provider configuration |
| YT-1.10 | [6:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=394s) | 🟢 USEFUL | Frontend-to-Okta-to-backend flow |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described using Okta with Spring Security, an Okta sign-in page, configured callback URLs, and tokens forwarded from the frontend to the API. He loosely referred to API/access keys for configuration. | Use OpenID Connect/OAuth 2.0 authorization-code flow, typically with PKCE for a browser client. Redirect to Okta, receive an authorization code at a registered redirect URI, exchange it securely for tokens, then have Spring Security validate access tokens. Configure issuer, client credentials where applicable, audience, scopes and role mapping; do not put confidential client secrets in browser code. |

