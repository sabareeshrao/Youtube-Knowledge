# IA-7 — How would you protect e-commerce APIs from abusive traffic and request floods?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.50 | [30:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1833s) | 🟢 USEFUL | Abusive traffic and peak sale load |
| YT-1.53 | [32:36](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1956s) | 🟢 USEFUL | Nginx reverse proxy and load balancing |
| YT-1.54 | [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) | 🟢 USEFUL | Rate limiting suspicious requests |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [32:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1967s) handlers like it will keep track of like how many requests are coming from like same uh IP address so if if it find it like uh if the the number of request is miscellaneous like it's not something uh<br>[33:01](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1981s) it's like active uh user request in that case we can uh it will like stop the user to hit that part so which we call that as rate limits yeah rate limits that's what sorry that's what I was<br>[33:14](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1994s) trying to say no problem okay yeah I yeah I don't have any filter kind of icons so I would have used that here so okay no problem uh um okay so then we have like different | I protect an e-commerce API by limiting how many requests a client can send in a short time. For example, one account shouldn't be allowed to call product search thousands of times per second. I put rate limits at the API gateway, and I can add WAF rules or bot protection for suspicious traffic. I wouldn't rely only on IP addresses because many real users can share one IP. Protecting the system means slowing abuse without blocking genuine shoppers. |

