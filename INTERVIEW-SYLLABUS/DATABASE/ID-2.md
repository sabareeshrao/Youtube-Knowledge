# ID-2 — Explain table partitioning versus database sharding.

## Video option — YT-1: Mock Interview 5+ year experienced | Spring Boot | Java | Microservice | System Design | Code Decode

**Video:** [Play video](https://www.youtube.com/watch?v=xMlcsFLk-CU)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-1.83 | [54:45](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3285s) | 🟢 USEFUL | Database partitioning |
| YT-1.84 | [55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) | 🟢 USEFUL | Sharding versus partitioning |

### Original candidate transcript vs. simple AI answer — YT-1

**Left:** Original caption excerpt, without rewritten wording. Speaker boundaries are inferred because the source does not label speakers; [read the entire original transcript](../../VIDEO-LIBRARY/YT-1/transcript.md). **Right:** New, independently authored spoken interview answer.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [54:56](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3296s) there is no difference between much in the sharding and uh partitioning<br>[55:08](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3308s) but the main difference is sharding means like we keep the database in a different uh servers like it's like a same uh same table but we keep it in a different places whereas like in<br>[55:19](https://www.youtube.com/watch?v=xMlcsFLk-CU&t=3319s) partitioning it comes under the same servers but replica not replica like the partitioning happens in the same servers so since the e-commerce can be one in us one in India and everything so | Partitioning and sharding both split data, but for different reasons. Partitioning divides a table into manageable pieces within a database setup, such as orders by month. Sharding spreads responsibility across separate database instances, perhaps by customer region or ID. For example, one large orders table could be partitioned by date before the business ever needs multiple shards. Partitioning helps organize and query data; sharding helps distribute ownership and scale, but adds complexity. |

## Video option — YT-4: Mock Interview 3+ years experience | SDE-1 | Microservice | Java 8 | Spring boot | Code Decode | ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=ekLB9t9DBAk)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-4.67 | [1:05:57](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3957s) | 🟢 USEFUL | What is horizontal and vertical database partitioning? |

### Original candidate transcript vs. simple AI answer — YT-4

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-4/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [1:06:22](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3982s) want to store three columns in one table and two other columns in another table so this is based up basically ver vertical partitioning and in case of horizontal partitioning for example I<br>[1:06:34](https://www.youtube.com/watch?v=ekLB9t9DBAk&t=3994s) have 10,000 records I want to store 5,000 records in one table second 5,000 records in another table this is called as horizontal partition so basically with rows that's | Horizontal partitioning splits rows by a key, while vertical partitioning separates columns or related groups of fields. Sharding distributes subsets across database nodes. For example, order rows may be partitioned by month, while cold profile attributes can live separately. I choose a partition key based on access patterns and data growth. |


## Video option — YT-6: System Design of Youtube | Mock Interview 5+ years of Experience | HLD | Code Decode ⭐ Repeated question

**Video:** [Play this source video](https://www.youtube.com/watch?v=35lPXRd00-8)

| ID ⭐ | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.38 | [34:06](https://www.youtube.com/watch?v=35lPXRd00-8&t=2046s) | 🟢 USEFUL | How does partitioning or sharding scale a video metadata database? |
| YT-6.39 | [35:16](https://www.youtube.com/watch?v=35lPXRd00-8&t=2116s) | 🟢 USEFUL | Follow-up: How does partitioning or sharding scale a video metadata database? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [34:29](https://www.youtube.com/watch?v=35lPXRd00-8&t=2069s) horizontal scaling in that sense but having said that if we do want to do that if we want to scale it horizontally by adding a couple of more pods to it we can we can do that with basic uh uh<br>[34:39](https://www.youtube.com/watch?v=35lPXRd00-8&t=2079s) scaling or you know like scaling practices by spawning new record new uh New Ports for it and then start storing sequentially in terms of the uh uh you know SQL servers maybe or or by spawning | Partitioning groups rows by a useful key, while sharding spreads data across database nodes. For example, video metadata can be sharded by a stable video ID when one database can no longer handle write volume. The routing key must spread load without breaking common queries. Replication serves a different purpose from sharding. |

