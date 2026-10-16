# IC-4 — Explain CI versus continuous delivery and deployment, including automated gates.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.99 | [1:07:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4037s) | 🟢 USEFUL | CI/CD definition and tool choices |
| YT-1.100 | [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) | 🟢 USEFUL | Continuous integration checks |
| YT-1.101 | [1:08:42](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4122s) | 🟢 USEFUL | Continuous delivery and deployment |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:07:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4050s) uh sure so as a name indicates CI is the continuous integration and uh continuous uh deliv deployments for the CD so when you see continuous integration means like uh generally I<br>[1:07:44](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4064s) write my code uh so that uh I mean I also write something called junit so that my codes are more uh unit test case based and U we could also follow some some tdd patterns so ensure that our<br>[1:07:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=4075s) codes are more robust uh but once the changes is done we have to integrate with other component as well to find it whether it's working fine so that's where our CI come into picture so | CI means checking changes continuously so problems appear early. Every pull request can run a build, tests, and code checks. CD is what happens after that: continuous delivery keeps a tested release ready, while continuous deployment actually releases passing changes automatically. For example, a bank may require a human approval for production, even if its tests are green. I think of CI as 'Is it safe to merge?' and delivery as 'Is it ready to release?' |

## Video option — YT-3: Mock Interview | Core Java Mock Interview Question and Answers | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=d22oNW1W6ms)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-3.43 | [41:09](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2469s) | 🟢 USEFUL | What steps belong in a typical GitHub-to-Kubernetes CI/CD pipeline? |
| YT-3.44 | [42:26](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2546s) | 🟢 USEFUL | Follow-up: What steps belong in a typical GitHub-to-Kubernetes CI/CD pipeline? |

### Original candidate transcript vs. simple AI answer — YT-3

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-3/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [41:23](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2483s) the jenin C pipeline it is going to get the latest repo from the GitHub repository and it generates an artifact based on that artifact it is going to get get the unit tests done and Son<br>[41:38](https://www.youtube.com/watch?v=d22oNW1W6ms&t=2498s) our code quality and code coverage it is going to test once it meets the particular particular Point particular points that we had different yeah threshold once it done it is going | A typical flow is commit, build, unit tests, quality and security checks, image creation, registry push, and deployment verification. For example, a failed test should stop the pipeline before the image reaches production. The point is to make each promotion visible and repeatable. |


## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.78 | [1:17:32](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4652s) | 🟢 USEFUL | What checks should run before a service is deployed to production? |
| YT-4.79 | [1:18:42](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4722s) | 🟢 USEFUL | Follow-up: What checks should run before a service is deployed to production? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:17:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4665s) different okay so once uh all the all the four stages passed you'll be creating a merge request to that particular envir onment you want to push so then then next CD pipeline will start<br>[1:17:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=4677s) so again the four stages will be common uh integration test unit test case Sona code coverage and then publish and then deploy okay okay and you deploy using any particular deployment | I'd require a build, tests, static quality checks, security scanning, and release verification before promotion. For example, a failing unit test or vulnerability gate should stop a deployment. Different organizations use different tools, but the important requirement is consistent evidence that the release is ready. |


## Video option — YT-7: Java Full-Stack Web Developer Mock Interview 4+ year experience | Angular Spring Boot | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=X2bPVTRruUM)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-7.33 | [29:06](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1746s) | 🟢 USEFUL | What is continuous integration and how does it relate to deployment? |
| YT-7.34 | [30:28](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1828s) | 🟢 USEFUL | Follow-up: What is continuous integration and how does it relate to deployment? |

### Original candidate transcript vs. simple AI answer — YT-7

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-7/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [29:22](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1762s) uh which helps us in automating the flow of the deployment and integration process so for example we are we are having a code and there is a Version Control like kit is there so whenever we<br>[29:33](https://www.youtube.com/watch?v=X2bPVTRruUM&t=1773s) push our code to any Version Control like kit so that in genkins we can uh we can automate the script so that whenever there is a there is code changes or if someone pushes a code into into the git | Continuous integration builds and tests changes as developers merge work. Delivery prepares an approved release, and continuous deployment can release automatically when gates pass. For example, a failed JUnit test stops the pipeline before production. I separate validation from the decision to deploy. |


## Video option — YT-8: Mock Interview 8+ year Experience Java Developer | Spring Boot | Microservices | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=PHIQJeKzMCU)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-8.37 | [34:26](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2066s) | 🟢 USEFUL | What stages belong in a Jenkins deployment pipeline? |

### Original candidate transcript vs. simple AI answer — YT-8

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-8/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:41](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2081s) flow yeah so um there are various jobs configured build build is there then some uh security uh means in in in my current project 45 is uh 45 is configur to check some security related things<br>[34:59](https://www.youtube.com/watch?v=PHIQJeKzMCU&t=2099s) then um deploying to the cloud for that um terraforms files are written in our project for each of the environment those file are read and the services getting deployed into the ECS elastic container | A typical Jenkins pipeline checks out code, compiles it, runs tests and scans, packages the artifact, builds an image, and promotes the release after approval or gates. For example, a failing code-quality check should prevent production deployment. I publish build results so the team knows exactly what was released. |

