# ID-5 — How would you choose SQL or NoSQL for video metadata?

## Video option — YT-6: System Design of Youtube | Mock Interview 5+ years of Experience | HLD | Code Decode

**Video:** [Play this source video](https://www.youtube.com/watch?v=35lPXRd00-8)

| ID | Watch | Type | What you will learn |
|---|---|---|---|
| YT-6.31 | [27:49](https://www.youtube.com/watch?v=35lPXRd00-8&t=1669s) | 🟢 USEFUL | How would you choose SQL or NoSQL for video metadata? |
| YT-6.32 | [29:02](https://www.youtube.com/watch?v=35lPXRd00-8&t=1742s) | 🟢 USEFUL | Follow-up: How would you choose SQL or NoSQL for video metadata? |

### Original candidate transcript vs. simple AI answer — YT-6

**Source:** [Unedited linked captions](../../VIDEO-LIBRARY/YT-6/transcript.md) · Caption excerpts may contain both speakers; speaker boundaries are inferred, not verified.

| Candidate response — original caption transcript (unedited excerpt) | AI answer — clear interview explanation |
|---|---|
| [28:05](https://www.youtube.com/watch?v=35lPXRd00-8&t=1685s) very wide column sort of a thing it could be description it could be uh it could be like uh what what particular channel is is is the video coming from it could be how what users are we uh<br>[28:20](https://www.youtube.com/watch?v=35lPXRd00-8&t=1700s) trying to Target in that sense it could be like all the sort of backend things which which people generally put up on YouTube videos I'm not too sure because I've never actually upad a YouTube video | Video metadata commonly has stable fields such as ID, owner, title, and status, which can fit a relational database. Flexible attributes or enormous access patterns may justify a document store. For example, comments and view events may be stored separately from core video records. I choose based on queries and consistency, not simply because a video is a large file. |

