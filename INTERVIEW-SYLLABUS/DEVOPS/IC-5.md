# IC-5 — What is a Dockerfile, and how are Docker images used to run a Java application?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.102 | [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) | 🟢 USEFUL | Dockerfile, image and container |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:09:20](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4160s) in our same project uh we can have something called docka files which have like bunch of instruction so it's could be like uh what could be the our jdk person and uh<br>[1:09:33](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4173s) I mean yeah what could be our entry point and what are the port should be enabled so these like a bunch of instruction helps the Dockers uh to uh in uh install these kind of packages and<br>[1:09:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4185s) uh uh execute the jar files okay so basically your Docker container that would have everything every Library everything that you need for your running on your instances now | A Dockerfile is a recipe for packaging my Java application. It tells Docker which runtime image to use, where to copy the JAR, and how to start it. For example, I can build a small Java 21 runtime image and run the same container locally or in the cloud. The image is the packaged recipe; the container is a running instance of it. I keep secrets outside the image and don't run as root unless necessary. |

