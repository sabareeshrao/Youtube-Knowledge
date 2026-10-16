# IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.132 | [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | 🟢 USEFUL | Using employee objects as HashMap keys |
| YT-1.133 | [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) | 🟢 USEFUL | equals and hashCode contract |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) if you want to make any object as the key uh the two things we have to override one is the<br>[1:31:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5497s) equal method and other one is uh hash code so the main reason is like even though uh we have to ensure that whether these two object are same or not it can be easily distinguished based on these<br>[1:31:49](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5509s) two methods so whenever uh when we we do any put it will automatically call these methods and get to ensure that whether it is a update to the same object or it is a new insert So based on the | If I use Employee objects as HashMap keys, Java needs to know when two Employee objects represent the same key. That's why I implement equals and hashCode consistently. For example, two objects with the same immutable employee ID should normally compare equal and return the same hash code. If the ID changes after insertion, lookup may break. The simple rule is: equal keys need equal hash codes, and keys should stay stable in the map. |

