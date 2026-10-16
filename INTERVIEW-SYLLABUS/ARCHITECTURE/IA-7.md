# IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.50 | [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | 🟢 USEFUL | Abusive traffic and peak sale load |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.54 | [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) | 🟢 USEFUL | Rate limiting suspicious requests |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He proposed a proxy/load balancer and request limits, including watching repeated calls from an IP, to stop abusive traffic. | Apply rate limiting at an API gateway/edge using token bucket or sliding-window policies per identity, token, endpoint and IP, backed by a shared limiter when necessary. Add WAF/bot controls, authentication, quotas and observability. IP-only throttling can punish shared networks; tune legitimate burst allowances and abuse responses. |

