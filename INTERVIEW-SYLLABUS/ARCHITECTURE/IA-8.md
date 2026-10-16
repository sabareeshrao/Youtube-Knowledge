# IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.51 | [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | 🟢 USEFUL | Client and web/mobile system entry point |
| YT-1.52 | [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) | 🟢 USEFUL | Load balancers for replicated services |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.55 | [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) | 🟢 USEFUL | Search service and microservice boundary |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He drew clients feeding an Nginx-like reverse proxy/load balancer, which routes requests to replicated microservices. | A solid overview includes clients, CDN/WAF, gateway or reverse proxy, load-balanced stateless services, authentication, service discovery, databases, caching, messaging and observability. Define service ownership and request flow, scaling/failure modes and consistency, not just the drawing. Add health checks, retries with limits and graceful degradation. |

