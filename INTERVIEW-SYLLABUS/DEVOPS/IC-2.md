# IC-2 — How do feature branches progress through QA, staging and production?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.95 | [1:04:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3845s) | 🟢 USEFUL | Git branch, feature and promotion strategy |
| YT-1.96 | [1:05:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3931s) | 🟢 USEFUL | Environment-specific configuration and profiles |
| YT-1.98 | [1:06:18](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3978s) | 🟢 USEFUL | How commits trigger deployments |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:04:54](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3894s) so once the qls also test we uh merge this to our a pre-pro branch it's not directly merch to the stable so<br>[1:05:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3905s) in the pre-pro branch we going to it looks like a same production Branch uh like it but customers are not using that uh changes this will just to ensure that our changes are working fine in the<br>[1:05:16](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3916s) customer environment once everything is looks fine then we deploy it on the production | I don't assume every environment needs its own Git branch. I build the application once, test it, and move the same version through QA, staging, and production. Each environment supplies its own configuration and secrets. For example, staging uses a test payment provider while production uses the real one, but the application code is the same. Promoting one known build is safer than rebuilding something slightly different at each stage. |

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.31 | [29:15](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1755s) | 🟢 USEFUL | How do Git branches map to development, QA, and production deployments? |
| YT-4.32 | [30:23](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1823s) | 🟢 USEFUL | Follow-up: How do Git branches map to development, QA, and production deployments? |
| YT-4.33 | [31:38](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1898s) | 🟢 USEFUL | Follow-up: How do Git branches map to development, QA, and production deployments? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [29:28](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1768s) one QA and all of them are working together so how do you follow your branching techniques your repository being either they foged or cloned what is the envirment what is profiling what is<br>[29:45](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=1785s) environments that you're using everything I would like to know so when I talk about the environments uh we have different environments like feature main Dev for developers both both feature M and | A team may use feature, development, release, and production branches, with pull requests and tests before promotion. For example, a release candidate is tested in QA before deployment to production. The exact branch model varies; what's important is controlled promotion and an auditable commit. |

