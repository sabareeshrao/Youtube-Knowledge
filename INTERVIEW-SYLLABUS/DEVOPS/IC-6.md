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

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.34 | [31:53](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1913s) | 🟢 USEFUL | How are Docker images deployed through Amazon EKS? |
| YT-4.35 | [33:04](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1984s) | 🟢 USEFUL | Follow-up: How are Docker images deployed through Amazon EKS? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [32:09](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1929s) create a Docker file once the docker file is done uh it will create an image from the image uh it will pick the all the particular dependencies from a container registry okay uh all the all the images<br>[32:23](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1943s) will be stored in the container registry and from the container registry it will be creating an uh I mean we are following kubernetes as of now so it will be moved to the kubernetes instance of of | A build pipeline creates a container image, pushes it to a registry, and updates a Kubernetes Deployment manifest or image reference. EKS schedules the pods and reconciles the desired replicas. For example, deploying three order pods uses one versioned image and a Deployment. EKS manages orchestration; it does not build the Java code for you. |


## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.33 | [31:18](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1878s) | 🟢 USEFUL | How does Kubernetes manage Docker-compatible containers? |
| YT-8.34 | [32:40](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1960s) | 🟢 USEFUL | Follow-up: How does Kubernetes manage Docker-compatible containers? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [31:35](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1895s) and whatever the our project code libraries and everything Java Java version whichever we want jdk same same jdk okay okay um and you when when you have multiple containers with all the<br>[31:55](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=1915s) microsof you have n number of containers created right one container having this one having another micros service another container you have suppose you have 100 microservices working 100 | Kubernetes schedules application pods, manages desired replica counts, and replaces failed pods according to configuration. For example, a Deployment declares three replicas for the catalog service. Kubernetes uses OCI-compatible images and does not require Docker as the node runtime. Its main job is to reconcile desired and observed state. |

