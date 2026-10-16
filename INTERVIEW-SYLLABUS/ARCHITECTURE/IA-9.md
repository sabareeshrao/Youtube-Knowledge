# IA-9 — Design product search using a cache, database and search index.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.56 | [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) | 🟢 USEFUL | Redis cache for product search |
| YT-1.57 | [35:31](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2131s) | 🟢 USEFUL | NoSQL choices for product search |
| YT-1.58 | [36:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2165s) | 🟢 USEFUL | Elasticsearch for product queries |
| YT-1.59 | [37:39](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2259s) | 🟢 USEFUL | Text search and typo-tolerant indexing |
| YT-1.60 | [38:17](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2297s) | 🟢 USEFUL | Hot search queries cached in Redis |

### Candidate answer vs. AI-corrected answer — YT-1

**Left:** Candidate's answer, paraphrased from the transcript. **Right:** Independently corrected technical answer, not spoken by the candidate.

| Candidate answer (paraphrased from YT-1) | AI-corrected interview answer |
|---|---|
| He combined product search with Redis caching, Cassandra/MongoDB as product storage and Elasticsearch for keyword/typo search, assuming search can tolerate some staleness. | Keep authoritative product/catalog data in a suitable operational store, maintain a dedicated search index asynchronously via a reliable change pipeline, and cache hot queries in Redis with expiration/invalidation. Use an Elasticsearch/OpenSearch query service for text relevance. Protect inventory/pricing correctness at checkout; search-index and cache consistency need explicit update/rebuild plans. |

