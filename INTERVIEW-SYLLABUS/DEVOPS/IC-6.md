# IC-6 — How would you run and scale ten microservices with Kubernetes?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.103 | [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | 🟢 USEFUL | Managing multiple microservice containers |
| YT-1.104 | [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) | 🟢 USEFUL | Kubernetes orchestration and replicas |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) we use uh popularly kubernetes for the orchestration as a tool so generally this the job of the kubernetes is like scaling of these<br>[1:10:21](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4221s) containers so we can push or commit our uh images to our GitHub cloud and we can make it like very automated with our kubernetes so that whenever it sees like there is some over overhead in the<br>[1:10:35](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4235s) services it can create a new instance from our container so from our image sorry from the image it will create a new containers or if something is not getting used then it will can do the reverse way | Kubernetes helps me run many service containers without managing each one by hand. For example, I can tell it I want three order-service pods. If one dies, Kubernetes works to restore the desired number. A Service routes traffic to healthy pods, and autoscaling can add replicas when configured metrics say they're needed. It's useful, but it still needs proper health checks, limits, and monitoring. Kubernetes manages the desired state; I define what healthy looks like. |

