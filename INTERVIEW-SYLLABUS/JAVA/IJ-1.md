# IJ-1 — Compare HashMap and ConcurrentHashMap under concurrent access.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.128 | [1:28:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5299s) | 🟢 USEFUL | ConcurrentHashMap internal design question |
| YT-1.129 | [1:28:46](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5326s) | 🟢 USEFUL | HashMap fail-fast iteration |
| YT-1.130 | [1:29:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5372s) | 🟢 USEFUL | Concurrent access and synchronization |
| YT-1.131 | [1:30:07](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5407s) | 🟢 USEFUL | Legacy segment-lock explanation caveat |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said HashMap iterators can fail when entries change during iteration, while ConcurrentHashMap handles concurrent writes without that iterator exception. He described an older segmented-locking model. | HashMap is not thread-safe; fail-fast iteration is best-effort and does not make access safe. ConcurrentHashMap supports safe concurrent operations and weakly consistent iterators; modern implementations use fine-grained synchronization/CAS, not a fixed simple set of 16 segment locks. Use atomic APIs such as computeIfAbsent when coordination is needed. |

