# IJ-2 — What is the equals and hashCode contract when a custom Employee object is a HashMap key?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.132 | [1:31:11](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5471s) | 🟢 USEFUL | Using employee objects as HashMap keys |
| YT-1.133 | [1:31:24](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=5484s) | 🟢 USEFUL | equals and hashCode contract |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said a custom Employee key should override equals() and hashCode() to distinguish logically equal keys and avoid duplicate entries. | Implement equals() and hashCode() consistently: equal objects must produce equal hash codes, and key fields should remain stable while stored. HashMap uses hash buckets and equality comparisons on collisions/matches. Prefer immutable identifiers/keys, and test equal, unequal and collision scenarios. |

