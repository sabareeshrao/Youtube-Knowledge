# IS-8 — Why reuse Hibernate SessionFactory and what happens when an application has several databases?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.31 | [16:47](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1007s) | 🟢 USEFUL | Why SessionFactory is expensive and shared |
| YT-1.32 | [17:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1059s) | 🟢 USEFUL | Multiple databases and SessionFactory instances |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He said SessionFactory is expensive, should be reused as a singleton, and different databases generally need separate SessionFactory instances. He also compared one SessionFactory to one database connection. | SessionFactory is expensive to build but thread-safe and reused, typically one per persistence unit/configuration. It creates many short-lived Sessions and works with a connection pool; it is not one database connection. With multiple independently configured databases/persistence units, configure corresponding factories/entity managers and transaction boundaries. |

