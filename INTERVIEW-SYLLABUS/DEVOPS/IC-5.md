# IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.102 | [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | 🟢 USEFUL | Dockerfile, image and container |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He described a Dockerfile with JDK version, application startup entry point, exposed ports and dependencies that run a Java JAR. | A Dockerfile describes an image build: select a suitable base runtime (up to Java 21 here), copy the built JAR, configure a non-root user and ENTRYPOINT, and optionally document EXPOSE. Images are immutable packages; containers are running instances. Inject secrets and environment config at runtime and scan/minimize image layers. |

