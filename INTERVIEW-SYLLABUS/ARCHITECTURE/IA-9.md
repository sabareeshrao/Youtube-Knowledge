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

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:30](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2070s) okay so this generally cash the uh the data like all the items which are coming<br>[34:55](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2095s) from the inventories so this data need not to be accurate like sometimes we can search the product but even though if you don't available in the car in the inventory so this need not be like 100%<br>[35:05](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=2105s) consistence it can be like uh eventual consistence as well so that's totally fine uh so and generally we can go with the database here uh of no SQL or SQL but I was thinking | For product search, I separate where product data is owned from how people search it. A product database stores the real catalog. A search index such as Elasticsearch makes text and typo-tolerant searches fast. Redis can hold common search results so we don't repeat expensive queries. For example, thousands of people searching 'running shoes' may share a cached result. But stock and price must be checked again when the customer actually buys. |

