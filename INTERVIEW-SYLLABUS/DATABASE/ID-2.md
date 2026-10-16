# ID-2 — Explain table partitioning versus database sharding.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.83 | [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | 🟢 USEFUL | Database partitioning |
| YT-1.84 | [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) | 🟢 USEFUL | Sharding versus partitioning |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He distinguished partitioning as splitting data within one server and sharding as distributing portions of the dataset across different servers or locations. | Partitioning divides a table logically or physically by a key, often within one database instance, improving pruning and maintenance when queries align. Sharding distributes ownership of data across independent database instances/nodes. Both can span physical machines depending on implementation; explain shard keys, routing, cross-shard queries and rebalancing. |

