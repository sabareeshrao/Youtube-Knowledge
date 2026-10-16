# IA-4 — How does GraphQL field selection compare with REST DTO responses?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.36 | [20:32](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1232s) | 🟢 USEFUL | GraphQL field-level selection |
| YT-1.37 | [20:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1255s) | 🟢 USEFUL | REST DTO and field filtering alternatives |
| YT-1.38 | [21:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=1290s) | 🟢 USEFUL | Variable response fields across clients |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He argued REST can reduce response fields via DTOs or @JsonIgnore, while GraphQL lets each caller select requested fields more conveniently. | GraphQL clients specify selected fields at query time. REST can also provide sparse fieldsets, projections, query parameters or alternate DTOs without always changing source code. @JsonIgnore is mostly static serialization exclusion, not the same as per-request selection. Compare schema governance, authorization, overfetching and resolver performance. |

