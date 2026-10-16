# IA-8 — Design a load-balanced high-level architecture for a large e-commerce application.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.51 | [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) | 🟢 USEFUL | Client and web/mobile system entry point |
| YT-1.52 | [32:03](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1923s) | 🟢 USEFUL | Load balancers for replicated services |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.55 | [33:34](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2014s) | 🟢 USEFUL | Search service and microservice boundary |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:27](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1887s) simple design first then I'll keep on add the enhancement based on the non-functionality as well so yeah generally we have a client here client could be either uh like a mobile or it<br>[31:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1897s) could be uh web or any uh lab yeah this has to be like a responsive web screen so that every different resolution can see that uh HTML page in a clear way and um there<br>[31:52](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1912s) could be many uh users because since we are talking about the e-commerce website we can come up with like um millions of user in know we call that as like a daily active users So based on that we | I would start with the customer, then follow one request through the system. The browser hits a CDN or gateway, a load balancer selects a healthy application instance, and the right service handles the request. Search might use a cache and search index; orders and payments need reliable storage and clear ownership. For example, if one search instance crashes, another should keep serving customers. I design for the customer journey first, then scale and failures. |

