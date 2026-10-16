# IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.128 | [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | 🟢 USEFUL | ConcurrentHashMap internal design question |
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |
| YT-1.131 | [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) | 🟢 USEFUL | Legacy segment-lock explanation caveat |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) with the regular hashmap what we use is is something called like a a fail fast<br>[1:28:37](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5317s) sorry it's a fail first uh hashing it means what like whenever uh we are iterating on this hash map and concurrently if something is going change in this hash let's say like we're<br>[1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) adding new entries so it will throw an exception because it the uh the way it works in a different because it keep on check the hash size if something is getting changed it will throw the | HashMap works well when one thread controls the data, but it isn't safe for unsynchronized concurrent updates. ConcurrentHashMap is built for multiple threads reading and updating the map together. For example, several requests may update different entries in a shared counter map. It offers operations such as compute that help update values safely, and its iterators can tolerate changes. It doesn't make every multi-step business operation atomic, so I still choose the right operation. |

