# IC-6 — How would you run and scale ten microservices with Kubernetes?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.103 | [1:09:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4196s) | 🟢 USEFUL | Managing multiple microservice containers |
| YT-1.104 | [1:10:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4209s) | 🟢 USEFUL | Kubernetes orchestration and replicas |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He suggested Kubernetes orchestrates containers, adds/removes replicas based on load and runs packaged microservice images in production. | Push immutable images to a container registry, deploy each workload via Kubernetes Deployment/Service resources, and configure health probes, resource requests/limits and autoscaling (HPA where appropriate). Kubernetes reconciles desired state but you must configure autoscaling policies, rollout strategy, networking and observability. |

