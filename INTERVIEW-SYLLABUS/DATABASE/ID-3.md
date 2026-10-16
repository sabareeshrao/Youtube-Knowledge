# ID-3 — When would SQL or NoSQL be appropriate for search, cart and tracking data?

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.62 | [39:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2357s) | 🟢 USEFUL | SQL database choice for cart |
| YT-1.79 | [52:09](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3129s) | 🟢 USEFUL | Choosing SQL for structured tracking rows |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He selected Cassandra/MongoDB for search-related product data and SQL for cart relationships; for shipment tracking he revised an initial NoSQL decision to SQL. | For product catalog, choose SQL/document storage from update and query needs; maintain a search index separately for text queries. Use relational transactions where cart/order/stock invariants require them. Tracking is often an append-only relational event table. Operational simplicity and access patterns matter more than a rule that every microservice needs NoSQL. |

