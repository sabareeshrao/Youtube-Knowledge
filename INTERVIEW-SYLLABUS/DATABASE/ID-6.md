# ID-6 — What is the difference between data partitioning and replication?

## Video option — YT-6: System Design of Youtube | Mock Interview 5+ years of Experience | HLD | Code Decode

**Video:** [Play this source video](https://www.youtube.com/watch?v=35lPXRd00-8)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.40 | [36:15](https://www.youtube.com/watch?v=35lPXRd00-8&t=2175s) | 🟢 USEFUL | What is the difference between data partitioning and replication? |
| YT-6.41 | [37:27](https://www.youtube.com/watch?v=35lPXRd00-8&t=2247s) | 🟢 USEFUL | Follow-up: What is the difference between data partitioning and replication? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [36:33](https://www.youtube.com/watch?v=35lPXRd00-8&t=2193s) could be having um what else I think that's about it that's that's we can live with this right right so as in when the field start getting populated into this uh uh database let's say I have<br>[36:47](https://www.youtube.com/watch?v=35lPXRd00-8&t=2207s) filled probably 1 million rows in this format so I would just want to exact same replica of this database once again okay sounds good so that that's why the Partition by row would imply that I have | Partitioning divides the data set, and replication keeps additional copies of the same data. For example, two shards may store different video ID ranges, while each shard has multiple replicas for resilience. Partitioning addresses data volume or load; replication protects availability and reads. They are often used together. |

